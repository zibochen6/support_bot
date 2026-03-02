#!/usr/bin/env python3
"""Markdown-aware chunking for RAG pipelines."""
from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Sequence, Tuple


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
FENCE_RE = re.compile(r"^\s*```")
LIST_LINE_RE = re.compile(
    r"^\s*(?:[-*+]\s+|\d+\.\s+|\*\*Step\s*\d+|Step\s*\d+)",
    re.IGNORECASE,
)
TOKEN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]|[A-Za-z0-9_./:+-]+|[^\s]")


@dataclass
class DocumentChunk:
    source: str
    source_rel: str
    title: str
    lang: str
    heading_path: str
    chunk_index: int
    chunk_id: str
    chunk_type: str
    start_token: int
    end_token: int
    token_count: int
    text_hash: str
    text: str

    def to_dict(self) -> dict:
        return asdict(self)


def iter_md_files(root: Path) -> Iterable[Path]:
    yield from root.rglob("*.md")


def extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip() or fallback
    return fallback


def detect_language(text: str, fallback: str) -> str:
    sample = text[:8000]
    cjk = sum(1 for ch in sample if "\u4e00" <= ch <= "\u9fff")
    latin = sum(1 for ch in sample if ("a" <= ch.lower() <= "z"))
    if cjk == 0 and latin == 0:
        return "zh" if re.search(r"[\u4e00-\u9fff]", fallback) else "en"
    if cjk > latin * 0.8:
        return "zh"
    if latin > cjk * 2:
        return "en"
    return "mixed"


def _normalize_hash_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def hash_text(text: str) -> str:
    return hashlib.sha1(_normalize_hash_text(text).encode("utf-8")).hexdigest()


def _token_matches(text: str) -> List[re.Match[str]]:
    return list(TOKEN_RE.finditer(text))


def token_count(text: str) -> int:
    return len(_token_matches(text))


def split_text_by_token_window(
    text: str,
    max_tokens: int,
    overlap_tokens: int,
) -> List[Tuple[int, int, str]]:
    if max_tokens <= 0:
        raise ValueError("max_tokens must be > 0")
    if overlap_tokens < 0:
        raise ValueError("overlap_tokens must be >= 0")
    if overlap_tokens >= max_tokens:
        raise ValueError("overlap_tokens must be smaller than max_tokens")

    matches = _token_matches(text)
    n_tokens = len(matches)
    if n_tokens == 0:
        return []
    if n_tokens <= max_tokens:
        cleaned = text.strip()
        if not cleaned:
            return []
        return [(0, n_tokens, cleaned)]

    windows: List[Tuple[int, int, str]] = []
    start = 0
    while start < n_tokens:
        end = min(n_tokens, start + max_tokens)
        left = matches[start].start()
        right = matches[end - 1].end()
        piece = text[left:right].strip()
        if piece:
            windows.append((start, end, piece))
        if end == n_tokens:
            break
        start = end - overlap_tokens
    return windows


def _split_into_sections(text: str, fallback_title: str) -> List[Tuple[List[str], str]]:
    lines = text.splitlines()
    sections: List[Tuple[List[str], str]] = []
    stack: List[str] = []
    body: List[str] = []

    def flush() -> None:
        payload = "\n".join(body).strip()
        if not payload:
            body.clear()
            return
        path = stack.copy() if stack else [fallback_title]
        sections.append((path, payload))
        body.clear()

    for line in lines:
        m = HEADING_RE.match(line.strip())
        if m:
            flush()
            level = len(m.group(1))
            heading = m.group(2).strip()
            while len(stack) >= level:
                stack.pop()
            stack.append(heading)
            continue
        body.append(line)

    flush()
    if not sections and text.strip():
        sections.append(([fallback_title], text.strip()))
    return sections


def _is_list_or_step_line(line: str) -> bool:
    return bool(LIST_LINE_RE.match(line))


def _split_section_blocks(section_text: str) -> List[Tuple[str, str]]:
    lines = section_text.splitlines()
    blocks: List[Tuple[str, str]] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        if line.strip() == "[TABLE COMPRESSED]":
            buf = [line]
            i += 1
            while i < n and lines[i].strip():
                if FENCE_RE.match(lines[i]) or _is_list_or_step_line(lines[i]):
                    break
                buf.append(lines[i])
                i += 1
            blocks.append(("table", "\n".join(buf).strip()))
            continue

        if FENCE_RE.match(line):
            buf = [line]
            i += 1
            while i < n:
                buf.append(lines[i])
                if FENCE_RE.match(lines[i]):
                    i += 1
                    break
                i += 1
            blocks.append(("code", "\n".join(buf).strip()))
            continue

        if _is_list_or_step_line(line):
            buf = [line]
            i += 1
            while i < n:
                nxt = lines[i]
                if not nxt.strip():
                    if i + 1 < n and (_is_list_or_step_line(lines[i + 1]) or lines[i + 1].startswith(("  ", "\t"))):
                        buf.append(nxt)
                        i += 1
                        continue
                    break
                if _is_list_or_step_line(nxt) or nxt.startswith(("  ", "\t")):
                    buf.append(nxt)
                    i += 1
                    continue
                break
            blocks.append(("list", "\n".join(buf).strip()))
            continue

        buf = [line]
        i += 1
        while i < n and lines[i].strip():
            if FENCE_RE.match(lines[i]) or lines[i].strip() == "[TABLE COMPRESSED]" or _is_list_or_step_line(lines[i]):
                break
            buf.append(lines[i])
            i += 1
        blocks.append(("text", "\n".join(buf).strip()))
    return blocks


def _decorate_with_heading(heading_path: Sequence[str], block_text: str) -> str:
    heading = " > ".join(h for h in heading_path if h.strip())
    if heading:
        return f"Section: {heading}\n\n{block_text.strip()}".strip()
    return block_text.strip()


def _buffer_chunk_type(block_types: Sequence[str]) -> str:
    uniq = set(block_types)
    if uniq == {"list"}:
        return "list"
    if "list" in uniq:
        return "mixed_list"
    return "text"


def chunk_markdown_document(
    text: str,
    source: str,
    source_rel: str,
    title: str,
    max_tokens: int = 420,
    overlap_tokens: int = 60,
    min_tokens: int = 30,
) -> List[DocumentChunk]:
    lang = detect_language(text, source_rel)
    sections = _split_into_sections(text, fallback_title=title)
    chunks: List[DocumentChunk] = []
    chunk_idx = 0

    def emit_chunk_windows(block_text: str, chunk_type: str, heading_path: Sequence[str]) -> None:
        nonlocal chunk_idx
        decorated = _decorate_with_heading(heading_path, block_text)
        for start, end, piece in split_text_by_token_window(
            decorated,
            max_tokens=max_tokens,
            overlap_tokens=overlap_tokens,
        ):
            n_tokens = end - start
            if min_tokens and n_tokens < min_tokens:
                continue
            chunk_id = f"{source_rel}::chunk-{chunk_idx:05d}"
            chunks.append(
                DocumentChunk(
                    source=source,
                    source_rel=source_rel,
                    title=title,
                    lang=lang,
                    heading_path=" > ".join(heading_path),
                    chunk_index=chunk_idx,
                    chunk_id=chunk_id,
                    chunk_type=chunk_type,
                    start_token=start,
                    end_token=end,
                    token_count=n_tokens,
                    text_hash=hash_text(piece),
                    text=piece,
                )
            )
            chunk_idx += 1

    for heading_path, section_text in sections:
        blocks = _split_section_blocks(section_text)
        text_buffer: List[str] = []
        type_buffer: List[str] = []

        def flush_buffer() -> None:
            if not text_buffer:
                return
            body = "\n\n".join(text_buffer).strip()
            emit_chunk_windows(body, _buffer_chunk_type(type_buffer), heading_path)
            text_buffer.clear()
            type_buffer.clear()

        for block_type, block_text in blocks:
            if block_type in {"code", "table"}:
                flush_buffer()
                emit_chunk_windows(block_text, block_type, heading_path)
                continue

            tentative = "\n\n".join(text_buffer + [block_text]).strip()
            decorated_tentative = _decorate_with_heading(heading_path, tentative)
            if text_buffer and token_count(decorated_tentative) > max_tokens:
                flush_buffer()

            decorated_single = _decorate_with_heading(heading_path, block_text)
            if token_count(decorated_single) > max_tokens:
                emit_chunk_windows(block_text, block_type, heading_path)
            else:
                text_buffer.append(block_text)
                type_buffer.append(block_type)

        flush_buffer()

    return chunks


def chunk_markdown_file(
    file_path: Path,
    docs_root: Path,
    max_tokens: int = 420,
    overlap_tokens: int = 60,
    min_tokens: int = 30,
) -> List[DocumentChunk]:
    text = file_path.read_text(encoding="utf-8", errors="ignore").strip()
    if not text:
        return []
    title = extract_title(text, file_path.stem)
    source = str(file_path.resolve())
    source_rel = str(file_path.resolve().relative_to(docs_root.resolve()))
    return chunk_markdown_document(
        text=text,
        source=source,
        source_rel=source_rel,
        title=title,
        max_tokens=max_tokens,
        overlap_tokens=overlap_tokens,
        min_tokens=min_tokens,
    )


def chunk_to_dicts(chunks: Sequence[DocumentChunk]) -> List[dict]:
    return [c.to_dict() for c in chunks]


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Preview markdown chunking.")
    parser.add_argument("--file", required=True, help="Markdown file path")
    parser.add_argument("--docs-root", default="wiki_pages_cleaned")
    parser.add_argument("--max-tokens", type=int, default=420)
    parser.add_argument("--overlap-tokens", type=int, default=60)
    parser.add_argument("--min-tokens", type=int, default=30)
    parser.add_argument("--show", type=int, default=5, help="How many chunks to print")
    args = parser.parse_args()

    chunks = chunk_markdown_file(
        file_path=Path(args.file),
        docs_root=Path(args.docs_root),
        max_tokens=args.max_tokens,
        overlap_tokens=args.overlap_tokens,
        min_tokens=args.min_tokens,
    )
    print(f"chunks={len(chunks)}")
    for item in chunks[: args.show]:
        payload = item.to_dict().copy()
        payload["text"] = payload["text"][:400]
        print(json.dumps(payload, ensure_ascii=True, indent=2))
