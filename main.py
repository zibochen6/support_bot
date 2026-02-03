import json
import os
import sys
from tqdm import tqdm
from tools.get_wiki_content import (
    GetWikiContent,
    get_urls_by_keywords,
    sanitize_filename,
    should_exclude_by_title,
)
# 多个关键词，URL path 含任一即匹配并抓取
KEYWORDS = ["recomputer", "reComputer","Jetson","jetson","robotics"]
# 保存目录
WIKI_PAGES_DIR = "./wiki_pages"
URL_INDEX_PATH = os.path.join(WIKI_PAGES_DIR, "url_index.json")


def load_url_index(path: str) -> set:
    """加载已抓取 URL 索引，不存在或异常则返回空 set。"""
    if not os.path.isfile(path):
        return set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return set(data.get("urls", []))
    except (json.JSONDecodeError, OSError):
        return set()


def save_url_index(path: str, known_urls: set) -> None:
    """将已抓取 URL 列表写回索引文件。"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"urls": sorted(known_urls)}, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    os.makedirs(WIKI_PAGES_DIR, exist_ok=True)
    known_urls = load_url_index(URL_INDEX_PATH)
    # 确保索引文件存在，便于记录“是否需要更新”
    if not os.path.isfile(URL_INDEX_PATH):
        save_url_index(URL_INDEX_PATH, known_urls)
    current_urls = get_urls_by_keywords(KEYWORDS)
    new_urls = [u for u in current_urls if u not in known_urls]
    n_total, n_new = len(current_urls), len(new_urls)
    print(f"关键词 {KEYWORDS} 共匹配到 {n_total} 个有效页面，其中 {n_new} 个为新页面")
    if not new_urls:
        print("无新页面需要抓取，退出。")
        save_url_index(URL_INDEX_PATH, known_urls)  # 退出前也写回索引
        sys.exit(0)
    ok, skip, fail = 0, 0, 0
    with tqdm(new_urls, desc="抓取进度", unit="页", ncols=80, dynamic_ncols=False) as pbar:
        for url in pbar:
            try:
                getter = GetWikiContent(url)
                title, content = getter.get_content()
                if not title.strip() and not content.strip():
                    skip += 1
                    pbar.set_postfix_str("跳过: 无内容", refresh=True)
                    continue
                if should_exclude_by_title(title):
                    skip += 1
                    pbar.set_postfix_str("跳过: 标题含R21xx/R20xx等", refresh=True)
                    continue
                safe_title = sanitize_filename(title) or "untitled"
                out_path = os.path.join(WIKI_PAGES_DIR, f"{safe_title}.md")
                with open(out_path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(content)
                known_urls.add(url)
                ok += 1
                pbar.set_postfix_str(f"当前: {safe_title[:20]}..." if len(safe_title) > 20 else f"当前: {safe_title}", refresh=True)
            except Exception as e:
                fail += 1
                pbar.set_postfix_str(f"失败: {str(e)[:30]}", refresh=True)
    save_url_index(URL_INDEX_PATH, known_urls)
    print(f"完成: 成功 {ok} 个，跳过 {skip} 个（过滤），失败 {fail} 个，保存至 {WIKI_PAGES_DIR}/")
