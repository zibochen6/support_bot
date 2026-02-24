#!/usr/bin/env python3
"""Preview Markdown cleaning for wiki_pages (no files modified).

Usage:
  python3 scripts/clean_md_preview.py --limit 3 --show-diff

The script traverses ./wiki_pages for .md files, applies cleaning rules in-memory,
and prints a short unified diff or cleaned preview. Designed for quick verification
before actual processing for FAISS/vectorization.
"""
import argparse
import difflib
import re
from pathlib import Path


FENCED_CODE_RE = re.compile(r"(```[\s\S]*?```)", re.MULTILINE)
ALIGN_CELL_RE = re.compile(r"^:?-{3,}:?$")

TABLE_MAX_ROWS = 40
TABLE_MAX_COLS = 20
TABLE_MAX_LINE_LEN = 400
TABLE_MAX_EMPTY_RATIO = 0.75
TABLE_PREVIEW_ROWS = 40
TABLE_PREVIEW_CELLS = 12


def split_fenced_code(text):
    # Split into segments, keeping fenced code blocks intact.
    parts = []
    pattern = FENCED_CODE_RE
    last = 0
    for m in pattern.finditer(text):
        if last < m.start():
            parts.append((False, text[last:m.start()]))
        parts.append((True, m.group(1)))
        last = m.end()
    if last < len(text):
        parts.append((False, text[last:]))
    return parts


def _split_table_row(line: str) -> list[str]:
    raw = line.strip().strip("|")
    return [c.strip() for c in raw.split("|")]


def _is_alignment_row(cells: list[str]) -> bool:
    non_empty = [c for c in cells if c]
    if not non_empty:
        return True
    return all(ALIGN_CELL_RE.fullmatch(c or "") for c in non_empty)


def _table_stats(lines: list[str]) -> tuple[int, int, float]:
    max_cols = 0
    max_len = 0
    total_cells = 0
    non_empty_cells = 0
    for line in lines:
        max_len = max(max_len, len(line))
        cells = _split_table_row(line)
        max_cols = max(max_cols, len(cells))
        for c in cells:
            total_cells += 1
            if c and not ALIGN_CELL_RE.fullmatch(c):
                non_empty_cells += 1
    empty_ratio = 1.0
    if total_cells:
        empty_ratio = 1 - (non_empty_cells / total_cells)
    return max_cols, max_len, empty_ratio


def _should_compress_table(lines: list[str]) -> bool:
    rows = len(lines)
    max_cols, max_len, empty_ratio = _table_stats(lines)
    if rows > TABLE_MAX_ROWS:
        return True
    if max_cols > TABLE_MAX_COLS:
        return True
    if max_len > TABLE_MAX_LINE_LEN:
        return True
    if rows > 10 and empty_ratio > TABLE_MAX_EMPTY_RATIO:
        return True
    return False


def _limit_cells(cells: list[str], limit: int) -> str:
    if len(cells) <= limit:
        return " | ".join(cells)
    return " | ".join(cells[:limit]) + " ..."


def _compress_table(lines: list[str]) -> list[str]:
    header = None
    rows = []
    for line in lines:
        cells = _split_table_row(line)
        if _is_alignment_row(cells):
            continue
        non_empty = [c for c in cells if c and not ALIGN_CELL_RE.fullmatch(c)]
        if not non_empty:
            continue
        if header is None:
            header = non_empty
            continue
        rows.append(non_empty)

    out = ["[TABLE COMPRESSED]"]
    if header:
        out.append("Columns: " + _limit_cells(header, TABLE_PREVIEW_CELLS))
    for row in rows[:TABLE_PREVIEW_ROWS]:
        out.append("- " + _limit_cells(row, TABLE_PREVIEW_CELLS))
    if len(rows) > TABLE_PREVIEW_ROWS:
        out.append(f"... ({len(rows) - TABLE_PREVIEW_ROWS} more rows)")
    return out


def clean_segment(seg: str) -> str:
    # Remove markdown images
    seg = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", seg)
    # Remove HTML comments
    seg = re.sub(r"<!--([\s\S]*?)-->", "", seg)
    # Remove <img ...> tags
    seg = re.sub(r"<img[\s\S]*?>", "", seg)
    # Remove data URI images
    seg = re.sub(r"data:image/[^\)\s\\]+", "", seg)
    # Remove promotional single-line phrases
    seg = re.sub(r"(?im)^.*\b(get one now|buy now|购买|Get One Now|Get One)\n+.*$", "", seg)
    # Compress noisy/huge tables composed of lines starting with '|'
    lines = seg.splitlines()
    out_lines = []
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            block = lines[i:j]
            if _should_compress_table(block):
                out_lines.extend(_compress_table(block))
            else:
                out_lines.extend(block)
            i = j
        else:
            out_lines.append(lines[i])
            i += 1
    seg = "\n".join(out_lines)
    # Collapse multiple blank lines to max 2
    seg = re.sub(r"\n{3,}", "\n\n", seg)
    # Trim trailing/leading whitespace
    seg = seg.strip() + "\n"
    return seg


def clean_text(text: str) -> str:
    parts = split_fenced_code(text)
    cleaned = []
    for is_code, part in parts:
        if is_code:
            cleaned.append(part)
        else:
            cleaned.append(clean_segment(part))
    return "".join(cleaned)


def preview_diff(original: str, cleaned: str, n_lines=60):
    orig_lines = original.splitlines(keepends=True)
    new_lines = cleaned.splitlines(keepends=True)
    diff = difflib.unified_diff(orig_lines, new_lines, lineterm="")
    diff_list = list(diff)
    if not diff_list:
        return "(no changes)"
    # Limit output length
    return "\n".join(diff_list[:n_lines])


def process_file(path: Path, show_diff: bool = True):
    text = path.read_text(encoding="utf-8")
    cleaned = clean_text(text)
    if show_diff:
        d = preview_diff(text, cleaned, n_lines=200)
        print(f"--- {path.relative_to(Path.cwd())} ---")
        print(d)
        print("\n")
    else:
        # Print first 200 chars of cleaned
        print(f"--- {path.relative_to(Path.cwd())} (cleaned preview) ---")
        print(cleaned[:200].replace("\n", "\\n"))


def find_md_files(root: Path):
    for p in root.rglob("*.md"):
        yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki-dir", default="wiki_pages")
    ap.add_argument("--limit", type=int, default=5, help="Only preview first N files")
    ap.add_argument("--show-diff", action="store_true")
    args = ap.parse_args()

    root = Path(args.wiki_dir)
    if not root.exists():
        print("wiki_dir not found:", root)
        return

    count = 0
    for f in find_md_files(root):
        process_file(f, show_diff=args.show_diff)
        count += 1
        if args.limit and count >= args.limit:
            break
    print(f"Processed {count} files (preview only, no files changed).")


if __name__ == "__main__":
    main()
