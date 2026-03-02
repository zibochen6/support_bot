#!/usr/bin/env python3
"""Build/query a FAISS index using markdown-aware chunking."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List, Optional

try:
    from tqdm import tqdm
except ImportError:  # pragma: no cover - optional dependency fallback
    def tqdm(iterable, **kwargs):
        return iterable

from chunker import chunk_markdown_file, iter_md_files


DEFAULT_DOCS_DIR = "wiki_pages_cleaned"
DEFAULT_OUT_DIR = "faiss_store"
DEFAULT_MODEL = "BAAI/bge-m3"


def load_embedder(model_name: str):
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:  # pragma: no cover - depends on user env
        raise SystemExit(
            "Missing dependency: sentence-transformers. "
            "Install with: pip install sentence-transformers"
        ) from exc
    return SentenceTransformer(model_name)


def load_faiss():
    try:
        import faiss  # type: ignore
    except ImportError as exc:  # pragma: no cover - depends on user env
        raise SystemExit("Missing dependency: faiss-cpu. Install with: pip install faiss-cpu") from exc
    return faiss


def load_metadata(meta_path: Path) -> List[dict]:
    rows: List[dict] = []
    with meta_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def resolve_embedding_model(out_dir: Path, model_override: Optional[str]) -> str:
    if model_override:
        return model_override
    config_path = out_dir / "config.json"
    if config_path.exists():
        config = json.loads(config_path.read_text(encoding="utf-8"))
        return config.get("embedding_model", DEFAULT_MODEL)
    return DEFAULT_MODEL


def build_index(
    docs_dir: Path,
    out_dir: Path,
    model_name: str,
    max_tokens: int,
    overlap_tokens: int,
    min_tokens: int,
    batch_size: int,
    limit: int,
    dedup_by_hash: bool,
) -> None:
    docs_dir = docs_dir.resolve()
    out_dir = out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(iter_md_files(docs_dir))
    if limit:
        md_files = md_files[:limit]
    if not md_files:
        raise SystemExit(f"No markdown files found in {docs_dir}")

    texts: List[str] = []
    metadata: List[dict] = []
    seen_hashes = set()
    before_dedup = 0
    dedup_dropped = 0

    for md_path in tqdm(md_files, desc="Chunking", unit="file"):
        chunks = chunk_markdown_file(
            file_path=md_path,
            docs_root=docs_dir,
            max_tokens=max_tokens,
            overlap_tokens=overlap_tokens,
            min_tokens=min_tokens,
        )
        before_dedup += len(chunks)
        for chunk in chunks:
            if dedup_by_hash and chunk.text_hash in seen_hashes:
                dedup_dropped += 1
                continue
            seen_hashes.add(chunk.text_hash)
            row = chunk.to_dict()
            row["vector_id"] = len(metadata)
            metadata.append(row)
            texts.append(chunk.text)

    if not texts:
        raise SystemExit("No chunks generated. Check chunking params and source docs.")

    model = load_embedder(model_name)
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
    )

    faiss = load_faiss()
    dim = int(embeddings.shape[1])
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings.astype("float32"))

    index_path = out_dir / "index.faiss"
    meta_path = out_dir / "metadata.jsonl"
    config_path = out_dir / "config.json"

    faiss.write_index(index, str(index_path))
    with meta_path.open("w", encoding="utf-8") as f:
        for row in metadata:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    config = {
        "docs_dir": str(docs_dir),
        "embedding_model": model_name,
        "normalize_embeddings": True,
        "faiss_metric": "inner_product",
        "max_tokens": max_tokens,
        "overlap_tokens": overlap_tokens,
        "min_tokens": min_tokens,
        "batch_size": batch_size,
        "files_indexed": len(md_files),
        "chunks_before_dedup": before_dedup,
        "chunks_after_dedup": len(metadata),
        "dedup_dropped": dedup_dropped,
        "embedding_dim": dim,
    }
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Saved index: {index_path}")
    print(f"Saved metadata: {meta_path}")
    print(f"Saved config: {config_path}")
    print(
        "Build summary: "
        f"files={len(md_files)} chunks={len(metadata)} "
        f"(before_dedup={before_dedup}, dedup_dropped={dedup_dropped})"
    )


def search_index(
    out_dir: Path,
    query: str,
    top_k: int = 8,
    model_name: Optional[str] = None,
    lang_filter: Optional[str] = None,
) -> List[dict]:
    out_dir = out_dir.resolve()
    index_path = out_dir / "index.faiss"
    meta_path = out_dir / "metadata.jsonl"
    if not index_path.exists() or not meta_path.exists():
        raise SystemExit("Index or metadata not found. Run build first.")

    faiss = load_faiss()
    index = faiss.read_index(str(index_path))
    metadata = load_metadata(meta_path)
    model_name = resolve_embedding_model(out_dir, model_name)
    model = load_embedder(model_name)

    query_emb = model.encode([query], normalize_embeddings=True).astype("float32")
    search_k = min(len(metadata), max(top_k, top_k * 4))
    scores, ids = index.search(query_emb, search_k)

    results: List[dict] = []
    for score, idx in zip(scores[0], ids[0]):
        if idx < 0 or idx >= len(metadata):
            continue
        row = metadata[idx].copy()
        if lang_filter and row.get("lang") != lang_filter:
            continue
        row["score"] = float(score)
        results.append(row)
        if len(results) >= top_k:
            break
    return results


def query_index(
    out_dir: Path,
    query: str,
    top_k: int,
    model_name: Optional[str],
    lang_filter: Optional[str],
    preview_chars: int,
    as_json: bool,
) -> None:
    results = search_index(
        out_dir=out_dir,
        query=query,
        top_k=top_k,
        model_name=model_name,
        lang_filter=lang_filter,
    )
    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    for rank, row in enumerate(results, start=1):
        text = row.get("text", "").replace("\n", " ").strip()
        if len(text) > preview_chars:
            text = text[:preview_chars] + "..."
        heading = row.get("heading_path") or row.get("title") or "-"
        print(
            f"[{rank}] score={row['score']:.4f} "
            f"source={row.get('source_rel','?')} "
            f"type={row.get('chunk_type','?')} "
            f"heading={heading}"
        )
        print(text)
        print("-" * 100)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FAISS build/query for cleaned markdown docs")
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build", help="Build FAISS index")
    p_build.add_argument("--docs", default=DEFAULT_DOCS_DIR, help="Directory of cleaned markdown files")
    p_build.add_argument("--out", default=DEFAULT_OUT_DIR, help="Output index directory")
    p_build.add_argument("--model", default=DEFAULT_MODEL, help="Embedding model")
    p_build.add_argument("--max-tokens", type=int, default=420, help="Target chunk size in tokens")
    p_build.add_argument("--overlap-tokens", type=int, default=60, help="Overlap between chunk windows")
    p_build.add_argument("--min-tokens", type=int, default=30, help="Drop chunks smaller than this")
    p_build.add_argument("--batch-size", type=int, default=64, help="Embedding batch size")
    p_build.add_argument("--limit", type=int, default=0, help="Only process first N files (0=all)")
    p_build.add_argument("--no-dedup", action="store_true", help="Disable cross-chunk hash dedup")

    p_query = sub.add_parser("query", help="Query FAISS index")
    p_query.add_argument("--out", default=DEFAULT_OUT_DIR, help="Output index directory")
    p_query.add_argument("--query", required=True, help="Query text")
    p_query.add_argument("--top-k", type=int, default=8, help="Number of retrieved chunks")
    p_query.add_argument("--model", default=None, help="Embedding model override")
    p_query.add_argument("--lang", choices=["zh", "en", "mixed"], default=None, help="Optional language filter")
    p_query.add_argument("--preview-chars", type=int, default=280, help="Preview text length")
    p_query.add_argument("--json", action="store_true", help="Print raw JSON results")

    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "build":
        build_index(
            docs_dir=Path(args.docs),
            out_dir=Path(args.out),
            model_name=args.model,
            max_tokens=args.max_tokens,
            overlap_tokens=args.overlap_tokens,
            min_tokens=args.min_tokens,
            batch_size=args.batch_size,
            limit=args.limit,
            dedup_by_hash=not args.no_dedup,
        )
        return

    if args.command == "query":
        query_index(
            out_dir=Path(args.out),
            query=args.query,
            top_k=args.top_k,
            model_name=args.model,
            lang_filter=args.lang,
            preview_chars=args.preview_chars,
            as_json=args.json,
        )
        return

    raise SystemExit(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
