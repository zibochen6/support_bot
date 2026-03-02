#!/usr/bin/env python3
"""Retrieve from FAISS and generate an answer with an OpenAI-compatible API."""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import List, Optional

import requests

from build_database import search_index


DEFAULT_OUT_DIR = "faiss_store"
DEFAULT_RERANK_MODEL = "BAAI/bge-reranker-v2-m3"


def load_env_file(path: Path = Path(".env"), overwrite: bool = True) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.lstrip("\ufeff").strip()
        value = value.strip().strip('"').strip("'")
        if key and (overwrite or key not in os.environ):
            os.environ[key] = value


def infer_query_lang(query: str) -> str:
    if re.search(r"[\u4e00-\u9fff]", query):
        return "zh"
    return "en"


def rerank_candidates(
    query: str,
    candidates: List[dict],
    rerank_model: str,
    top_n: int,
) -> List[dict]:
    try:
        from sentence_transformers import CrossEncoder
    except ImportError as exc:  # pragma: no cover - depends on env
        raise SystemExit(
            "Rerank requires sentence-transformers. "
            "Install with: pip install sentence-transformers"
        ) from exc

    model = CrossEncoder(rerank_model)
    pairs = [[query, row["text"]] for row in candidates]
    scores = model.predict(pairs, show_progress_bar=False)

    reranked = []
    for row, score in zip(candidates, scores):
        item = row.copy()
        item["rerank_score"] = float(score)
        reranked.append(item)
    reranked.sort(key=lambda x: x["rerank_score"], reverse=True)
    return reranked[:top_n]


def build_context_block(candidates: List[dict]) -> str:
    blocks = []
    for idx, row in enumerate(candidates, start=1):
        heading = row.get("heading_path") or row.get("title") or "-"
        score = row.get("rerank_score", row.get("score", 0.0))
        blocks.append(
            f"[{idx}] source={row.get('source_rel','?')} "
            f"heading={heading} type={row.get('chunk_type','?')} score={score:.4f}\n"
            f"{row.get('text','').strip()}"
        )
    return "\n\n---\n\n".join(blocks)


def call_llm(
    query: str,
    context: str,
    api_key: str,
    base_url: str,
    model_name: str,
    temperature: float,
    max_tokens: int,
) -> str:
    lang = infer_query_lang(query)
    answer_lang_hint = "请使用中文回答。" if lang == "zh" else "Please answer in English."

    system_prompt = (
        "You are a technical support assistant for Seeed/Jetson documents. "
        "Answer only with facts from the provided context. "
        "If context is insufficient, explicitly say so. "
        "When using evidence, cite source ids like [1], [2]."
    )
    user_prompt = (
        f"Question:\n{query}\n\n"
        f"Context:\n{context}\n\n"
        "Requirements:\n"
        "1) Give a direct answer first.\n"
        "2) Provide concise steps when appropriate.\n"
        "3) Add citations like [1][2].\n"
        "4) If uncertain, say which part cannot be confirmed.\n"
        f"5) {answer_lang_hint}"
    )

    endpoint = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    resp = requests.post(endpoint, headers=headers, json=payload, timeout=180)
    if resp.status_code >= 300:
        preview = resp.text[:800]
        key_preview = f"{api_key[:6]}...{api_key[-4:]}" if len(api_key) >= 12 else "***"
        if resp.status_code == 401:
            raise SystemExit(
                "LLM request failed (401): API key invalid or mismatched with base URL. "
                f"base_url={base_url}, model={model_name}, api_key={key_preview}, detail={preview}"
            )
        raise SystemExit(
            f"LLM request failed ({resp.status_code}): "
            f"base_url={base_url}, model={model_name}, detail={preview}"
        )
    data = resp.json()
    try:
        return data["choices"][0]["message"]["content"].strip()
    except Exception as exc:  # pragma: no cover - defensive
        raise SystemExit(f"Unexpected LLM response: {json.dumps(data, ensure_ascii=False)[:800]}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="RAG answer generation with FAISS retrieval")
    parser.add_argument("--out", default=DEFAULT_OUT_DIR, help="Index directory")
    parser.add_argument("--query", required=True, help="User question")
    parser.add_argument("--embed-model", default=None, help="Embedding model override for retrieval")
    parser.add_argument("--retrieve-top-k", type=int, default=20, help="Initial retrieval depth")
    parser.add_argument("--rerank-top-n", type=int, default=6, help="Final context count sent to LLM")
    parser.add_argument("--rerank-model", default=DEFAULT_RERANK_MODEL, help="Cross-encoder reranker")
    parser.add_argument("--no-rerank", action="store_true", help="Disable reranking")
    parser.add_argument("--model", default=None, help="LLM model override")
    parser.add_argument("--base-url", default=None, help="LLM API base URL override")
    parser.add_argument("--api-key", default=None, help="LLM API key override")
    parser.add_argument("--temperature", type=float, default=0.1, help="LLM temperature")
    parser.add_argument("--max-tokens", type=int, default=700, help="LLM max output tokens")
    parser.add_argument("--show-context", action="store_true", help="Print retrieved context before answering")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    load_env_file(overwrite=True)

    api_key = args.api_key or os.getenv("API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = args.base_url or os.getenv("BASE_URL") or os.getenv("OPENAI_BASE_URL") or "https://api.openai.com/v1"
    model_name = args.model or os.getenv("MODEL_NAME") or os.getenv("OPENAI_MODEL") or "gpt-4o-mini"
    if not api_key:
        raise SystemExit("Missing API key. Set API_KEY (or OPENAI_API_KEY) in .env or CLI.")

    retrieved = search_index(
        out_dir=Path(args.out),
        query=args.query,
        top_k=args.retrieve_top_k,
        model_name=args.embed_model,
    )
    if not retrieved:
        raise SystemExit("No retrieval hits found. Build index first or adjust query/model.")

    top_n = min(args.rerank_top_n, len(retrieved))
    selected: List[dict]
    rerank_used = False
    if args.no_rerank:
        selected = retrieved[:top_n]
    else:
        selected = rerank_candidates(
            query=args.query,
            candidates=retrieved,
            rerank_model=args.rerank_model,
            top_n=top_n,
        )
        rerank_used = True

    context = build_context_block(selected)
    if args.show_context:
        print("=== Retrieved Context ===")
        print(context)
        print("=== End Context ===")

    answer = call_llm(
        query=args.query,
        context=context,
        api_key=api_key,
        base_url=base_url,
        model_name=model_name,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )

    if args.json:
        payload = {
            "query": args.query,
            "answer": answer,
            "model": model_name,
            "base_url": base_url,
            "rerank_used": rerank_used,
            "sources": [
                {
                    "rank": i + 1,
                    "score": row.get("rerank_score", row.get("score")),
                    "source_rel": row.get("source_rel"),
                    "heading_path": row.get("heading_path"),
                    "chunk_id": row.get("chunk_id"),
                    "chunk_type": row.get("chunk_type"),
                }
                for i, row in enumerate(selected)
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    print("Answer:")
    print(answer)
    print("\nSources:")
    for i, row in enumerate(selected, start=1):
        score = row.get("rerank_score", row.get("score", 0.0))
        heading = row.get("heading_path") or row.get("title") or "-"
        print(
            f"[{i}] score={score:.4f} source={row.get('source_rel','?')} "
            f"heading={heading} chunk={row.get('chunk_id','-')}"
        )


if __name__ == "__main__":
    main()
