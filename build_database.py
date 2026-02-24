#!/usr/bin/env python3
"""Build and query a FAISS index from cleaned markdown docs.

Pipeline:
1) Chunking (with overlap)
2) Embedding
3) FAISS index build
4) Save index + metadata
5) Query: embed -> faiss.search -> topK chunks

Usage examples:
  python3 build_database.py build --docs wiki_pages_cleaned --out faiss_store
  python3 build_database.py query --out faiss_store --query "reComputer mini"
"""
from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List, Tuple

from tqdm import tqdm


DEFAULT_DOCS_DIR = "wiki_pages_cleaned"
DEFAULT_OUT_DIR = "faiss_store"
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


@dataclass
class ChunkMeta:
    source: str
    source_rel: str
    title: str
    chunk_index: int
    start_word: int
    end_word: int
    text: str


def iter_md_files(root: Path) -> Iterable[Path]:
    yield from root.rglob("*.md")


def extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip() or fallback
    return fallback


def tokenize_words(text: str) -> List[str]:
    return re.findall(r"\S+", text)


def chunk_words(
    words: List[str],
    chunk_size: int,
    overlap: int,
) -> Iterable[Tuple[int, int, str]]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if overlap < 0:
        raise ValueError("overlap must be >= 0")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    start = 0
    n = len(words)
    while start < n:
        end = min(n, start + chunk_size)
        yield start, end, " ".join(words[start:end])
        if end == n:
            break
        start = max(0, end - overlap)


def load_embedder(model_name: str):
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:  # pragma: no cover - user environment
        raise SystemExit(
            "Missing dependency: sentence-transformers. "
            "Install with: pip install sentence-transformers"
        ) from exc
    return SentenceTransformer(model_name)


def load_faiss():
    try:
        import faiss  # type: ignore
    except ImportError as exc:  # pragma: no cover - user environment
        raise SystemExit(
            "Missing dependency: faiss-cpu. Install with: pip install faiss-cpu"
        ) from exc
    return faiss


def build_index(
    docs_dir: Path,
    out_dir: Path,
    model_name: str,
    chunk_size: int,
    overlap: int,
    batch_size: int,
    min_words: int,
    limit: int,
) -> None:
    docs_dir = docs_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    md_files = list(iter_md_files(docs_dir))
    if limit:
        md_files = md_files[:limit]
    if not md_files:
        raise SystemExit(f"No markdown files found in: {docs_dir}")

    model = load_embedder(model_name)

    all_chunks: List[str] = []
    all_meta: List[ChunkMeta] = []
    for md_path in tqdm(md_files, desc="Chunking", unit="file"):
        text = md_path.read_text(encoding="utf-8", errors="ignore").strip()
        if not text:
            continue
        words = tokenize_words(text)
        if not words:
            continue
        title = extract_title(text, md_path.stem)
        rel = str(md_path.relative_to(docs_dir))
        chunk_idx = 0
        for start, end, chunk_text in chunk_words(words, chunk_size, overlap):
            if min_words and (end - start) < min_words:
                continue
            all_chunks.append(chunk_text)
            all_meta.append(
                ChunkMeta(
                    source=str(md_path),
                    source_rel=rel,
                    title=title,
                    chunk_index=chunk_idx,
                    start_word=start,
                    end_word=end,
                    text=chunk_text,
                )
            )
            chunk_idx += 1

    if not all_chunks:
        raise SystemExit("No chunks were created. Check chunk_size/min_words.")

    embeddings = model.encode(
        all_chunks,
        batch_size=batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
    )

    faiss = load_faiss()
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings.astype("float32"))

    index_path = out_dir / "index.faiss"
    meta_path = out_dir / "metadata.jsonl"
    config_path = out_dir / "config.json"

    faiss.write_index(index, str(index_path))
    with meta_path.open("w", encoding="utf-8") as f:
        for item in all_meta:
            f.write(json.dumps(asdict(item), ensure_ascii=False) + "\n")

    config = {
        "model_name": model_name,
        "docs_dir": str(docs_dir),
        "chunk_size": chunk_size,
        "overlap": overlap,
        "min_words": min_words,
        "files": len(md_files),
        "chunks": len(all_chunks),
        "embedding_dim": dim,
    }
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Saved index: {index_path}")
    print(f"Saved metadata: {meta_path}")
    print(f"Saved config: {config_path}")


def load_metadata(meta_path: Path) -> List[dict]:
    items: List[dict] = []
    with meta_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def query_index(
    out_dir: Path,
    model_name: str,
    query: str,
    top_k: int,
) -> None:
    faiss = load_faiss()
    index_path = out_dir / "index.faiss"
    meta_path = out_dir / "metadata.jsonl"
    if not index_path.exists() or not meta_path.exists():
        raise SystemExit("Index or metadata not found. Run build first.")

    model = load_embedder(model_name)
    index = faiss.read_index(str(index_path))
    meta = load_metadata(meta_path)

    q_emb = model.encode([query], normalize_embeddings=True)
    scores, ids = index.search(q_emb.astype("float32"), top_k)

    for rank, (score, idx) in enumerate(zip(scores[0], ids[0]), start=1):
        if idx < 0 or idx >= len(meta):
            continue
        item = meta[idx]
        preview = item["text"].replace("\n", " ").strip()
        if len(preview) > 300:
            preview = preview[:300] + "..."
        print(
            f"[{rank}] score={score:.4f} source={item['source_rel']} "
            f"chunk={item['chunk_index']} title={item['title']}"
        )
        print(preview)
        print("-" * 80)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build", help="Build FAISS index from cleaned docs")
    p_build.add_argument("--docs", default=DEFAULT_DOCS_DIR, help="Cleaned docs directory")
    p_build.add_argument("--out", default=DEFAULT_OUT_DIR, help="Output directory")
    p_build.add_argument("--model", default=DEFAULT_MODEL, help="Embedding model name")
    p_build.add_argument("--chunk-size", type=int, default=400, help="Chunk size in words")
    p_build.add_argument("--overlap", type=int, default=60, help="Overlap in words")
    p_build.add_argument("--batch-size", type=int, default=64, help="Embedding batch size")
    p_build.add_argument("--min-words", type=int, default=30, help="Drop chunks smaller than this")
    p_build.add_argument("--limit", type=int, default=0, help="Only process first N files (0=all)")

    p_query = sub.add_parser("query", help="Query FAISS index")
    p_query.add_argument("--out", default=DEFAULT_OUT_DIR, help="Output directory")
    p_query.add_argument("--model", default=DEFAULT_MODEL, help="Embedding model name")
    p_query.add_argument("--query", required=True, help="Query text")
    p_query.add_argument("--top-k", type=int, default=5, help="Number of results")

    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "build":
        build_index(
            docs_dir=Path(args.docs),
            out_dir=Path(args.out),
            model_name=args.model,
            chunk_size=args.chunk_size,
            overlap=args.overlap,
            batch_size=args.batch_size,
            min_words=args.min_words,
            limit=args.limit,
        )
    elif args.command == "query":
        query_index(
            out_dir=Path(args.out),
            model_name=args.model,
            query=args.query,
            top_k=args.top_k,
        )


if __name__ == "__main__":
    main()
