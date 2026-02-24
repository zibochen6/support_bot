#!/usr/bin/env python3
"""Clean markdown files for vectorization without modifying originals.

Usage:
  python3 scripts/clean_md_export.py --wiki-dir wiki_pages --out-dir wiki_pages_cleaned

The script traverses the input folder for .md files, applies cleaning rules,
and writes cleaned copies to a new folder (same relative paths).
"""
import argparse
import re
from pathlib import Path


FENCED_CODE_RE = re.compile(r"(```[\s\S]*?```)", re.MULTILINE)
ADMONITION_LINE_RE = re.compile(r"^\s*(note|info|tip|warning|danger|caution|important)\s*$", re.IGNORECASE)
ADMONITION_FENCE_RE = re.compile(r"^\s*:::+.*$")
PROMO_LINK_RE = re.compile(r"^\s*\[.*\]\(https?://www\.seeedstudio\.com/.*\)\s*$", re.IGNORECASE)
IMAGE_REF_DEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*https?://[^\s]+?\.(png|jpe?g|gif|svg|webp)(\?.*)?\s*$", re.IGNORECASE)
ALIGN_CELL_RE = re.compile(r"^:?-{3,}:?$")

TABLE_MAX_ROWS = 40
TABLE_MAX_COLS = 20
TABLE_MAX_LINE_LEN = 400
TABLE_MAX_EMPTY_RATIO = 0.75
TABLE_PREVIEW_ROWS = 40
TABLE_PREVIEW_CELLS = 12


def split_fenced_code(text: str):
    parts = []
    last = 0
    for m in FENCED_CODE_RE.finditer(text):
        if last < m.start():
            parts.append((False, text[last:m.start()]))
        parts.append((True, m.group(1)))
        last = m.end()
    if last < len(text):
        parts.append((False, text[last:]))
    return parts


def _strip_front_matter(seg: str) -> str:
    if seg.startswith("---\n"):
        end = seg.find("\n---\n", 4)
        if end != -1:
            return seg[end + 5 :]
    return seg


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
    seg = _strip_front_matter(seg)
    # Remove HTML comments
    seg = re.sub(r"<!--([\s\S]*?)-->", "", seg)
    # Remove figure blocks
    seg = re.sub(r"<figure[\s\S]*?</figure>", "", seg, flags=re.IGNORECASE)
    # Remove <img ...> tags
    seg = re.sub(r"<img[\s\S]*?>", "", seg, flags=re.IGNORECASE)
    # Remove markdown images
    seg = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", seg)
    seg = re.sub(r"!\[[^\]]*\]\[[^\]]*\]", "", seg)
    # Remove data URI images
    seg = re.sub(r"data:image/[^\)\s\\]+", "", seg)
    # Remove zero-width anchor links like [](#something)
    seg = re.sub(r"\[\s*\u200b?\s*\]\(#[^)]+\)", "", seg)

    lines = seg.splitlines()
    out_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Drop single-line CTA links to store
        if PROMO_LINK_RE.match(line):
            i += 1
            continue
        # Drop admonition markers
        if ADMONITION_LINE_RE.match(line) or ADMONITION_FENCE_RE.match(line):
            i += 1
            continue
        # Remove image reference definitions
        if IMAGE_REF_DEF_RE.match(line):
            i += 1
            continue
        # Compress noisy/huge tables composed of lines starting with '|'
        if line.lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            block = lines[i:j]
            if _should_compress_table(block):
                out_lines.extend(_compress_table(block))
            else:
                out_lines.extend(block)
            i = j
            continue
        out_lines.append(line)
        i += 1

    seg = "\n".join(out_lines)
    # Collapse multiple blank lines to max 2
    seg = re.sub(r"\n{3,}", "\n\n", seg)
    # Trim trailing/leading whitespace
    return seg.strip() + "\n"


def clean_text(text: str) -> str:
    parts = split_fenced_code(text)
    cleaned = []
    for is_code, part in parts:
        if is_code:
            cleaned.append(part)
        else:
            cleaned.append(clean_segment(part))
    return "".join(cleaned)


def find_md_files(root: Path):
    yield from root.rglob("*.md")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki-dir", default="wiki_pages")
    ap.add_argument("--out-dir", default="wiki_pages_cleaned")
    ap.add_argument("--limit", type=int, default=0, help="Only process first N files (0 = all)")
    args = ap.parse_args()

    in_root = Path(args.wiki_dir)
    out_root = Path(args.out_dir)
    if not in_root.exists():
        print("wiki-dir not found:", in_root)
        return

    count = 0
    for md_path in find_md_files(in_root):
        rel = md_path.relative_to(in_root)
        out_path = out_root / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)

        text = md_path.read_text(encoding="utf-8")
        cleaned = clean_text(text)
        out_path.write_text(cleaned, encoding="utf-8", newline="\n")

        count += 1
        if args.limit and count >= args.limit:
            break

    print(f"Cleaned {count} files into: {out_root}")


if __name__ == "__main__":
    main()
