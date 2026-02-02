import os
from tqdm import tqdm
from tools.get_wiki_content import (
    GetWikiContent,
    get_urls_by_keywords,
    sanitize_filename,
)
# 多个关键词，URL path 含任一即匹配并抓取
KEYWORDS = ["recomputer", "reComputer","Jetson","jetson","robotics"]
# 保存目录
WIKI_PAGES_DIR = "./wiki_pages"

if __name__ == "__main__":
    os.makedirs(WIKI_PAGES_DIR, exist_ok=True)
    urls = get_urls_by_keywords(KEYWORDS)
    n = len(urls)
    print(f"关键词 {KEYWORDS} 共匹配到 {n} 个有效页面")
    ok, fail = 0, 0
    with tqdm(urls, desc="抓取进度", unit="页", ncols=80, dynamic_ncols=False) as pbar:
        for url in pbar:
            try:
                getter = GetWikiContent(url)
                title, content = getter.get_content()
                if not title.strip() and not content.strip():
                    fail += 1
                    pbar.set_postfix_str("跳过: 无内容", refresh=True)
                    continue
                safe_title = sanitize_filename(title) or "untitled"
                out_path = os.path.join(WIKI_PAGES_DIR, f"{safe_title}.md")
                with open(out_path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(content)
                ok += 1
                pbar.set_postfix_str(f"当前: {safe_title[:20]}..." if len(safe_title) > 20 else f"当前: {safe_title}", refresh=True)
            except Exception as e:
                fail += 1
                pbar.set_postfix_str(f"失败: {str(e)[:30]}", refresh=True)
    print(f"完成: 成功 {ok} 个，失败 {fail} 个，保存至 {WIKI_PAGES_DIR}/")
