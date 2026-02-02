import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse
import re

def _ensure_utf8(s: str) -> str:
    """确保字符串为合法 UTF-8，替换无法编码的字符，避免保存乱码。"""
    if not s:
        return s
    return s.encode("utf-8", errors="replace").decode("utf-8")


def fetch_page(url: str, headers: dict = None):
    """
    请求网页并返回 BeautifulSoup，统一按 UTF-8 解码避免乱码。
    """
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Charset": "utf-8",
    }
    headers = headers or default_headers
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    # 优先按 UTF-8 解码，避免 apparent_encoding 误判导致乱码
    if resp.encoding and resp.encoding.lower().startswith("utf-8"):
        text = resp.text
    else:
        text = resp.content.decode("utf-8", errors="replace")
    return BeautifulSoup(text, "html.parser")


def parse_html(html: str) -> BeautifulSoup:
    """用 BeautifulSoup 解析 HTML 字符串。"""
    return BeautifulSoup(html, "html.parser")


def html_to_markdown(html_or_soup: str | BeautifulSoup, selector: str = None, **kwargs) -> str:
    """
    将 HTML 或 BeautifulSoup 对象解析为 Markdown 文本。

    :param html_or_soup: HTML 字符串或 BeautifulSoup 对象
    :param selector: 可选，只转换该 CSS 选择器内的内容，如 "article", ".content", "#main"
    :param kwargs: 传给 markdownify 的选项，如 heading_style="ATX", strip=["script","style"]
    :return: Markdown 字符串
    """
    default_options = {
        "heading_style": "ATX",      # # 标题
        "strip": ["script", "style"], # 去掉 script/style 标签
    }
    default_options.update(kwargs)

    if isinstance(html_or_soup, BeautifulSoup):
        soup = html_or_soup
    else:
        soup = parse_html(html_or_soup)

    if selector:
        elem = soup.select_one(selector)
        if elem is None:
            return "", ""
        # 标题从整页 soup 的 <title> 取，正文只转换 selector 区域
        return get_title_for_markdown(soup), md(str(elem), **default_options)
    return get_title_for_markdown(soup), md(str(soup), **default_options)


def get_title_for_markdown(soup: BeautifulSoup, strip_suffix: str = " | Seeed Studio Wiki") -> str:
    """获取用于 Markdown 的标题，可去掉站点后缀。"""
    title = get_title(soup)
    if strip_suffix and title.endswith(strip_suffix):
        return title[: -len(strip_suffix)].strip()
    return title


def get_title(soup: BeautifulSoup) -> str:
    """获取页面标题（来自 <title> 标签）。"""
    tag = soup.find("title")
    return tag.get_text(strip=True) if tag else ""


def remove_resource(markdown_text: str) -> str:
    if "## Resources" in markdown_text:
        markdown_text = markdown_text.split("## Resources")[0].rstrip()
    # 删除零宽字符等锚点链接（兼容多种编码表现形式）
    markdown_text = re.sub(r"\[\s*\u200b?\s*\]\(#[^)]+\)", "", markdown_text)
    return markdown_text


def get_urls_from_sitemap(sitemap_url: str) -> list[str]:
    """从 sitemap 解析出所有 wiki 页面 URL。"""
    r = requests.get(sitemap_url, timeout=15)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    # 常见命名空间
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    for loc in root.findall(".//sm:url/sm:loc", ns) or root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        if loc is not None and loc.text:
            urls.append(loc.text.strip())
    # 若无命名空间
    if not urls:
        for loc in root.iter("loc"):
            if loc.text and "wiki.seeedstudio.com" in loc.text:
                urls.append(loc.text.strip())
    return urls

def filter_urls_by_keyword(urls: list[str], keyword: str) -> list[str]:
    """只保留 URL path 中包含 keyword 的链接（不区分大小写）。"""
    kw = keyword.lower()
    return [u for u in urls if kw in urlparse(u).path.lower()]


def filter_urls_by_keywords(urls: list[str], keywords: list[str]) -> list[str]:
    """只保留 URL path 中包含任一 keyword 的链接（不区分大小写），去重。"""
    if not keywords:
        return []
    kws = [k.lower() for k in keywords]
    seen = set()
    out = []
    for u in urls:
        path_lower = urlparse(u).path.lower()
        if any(kw in path_lower for kw in kws) and u not in seen:
            seen.add(u)
            out.append(u)
    return out


def filter_urls_by_tier(urls: list[str]) -> list[str]:
    """
    只保留符合层级规则的 URL：
    - 排除 path 中含 r1000 的页面（如 recomputer_r1000_home_automation）
    - 排除其他语言层级（如 /ja/），只保留两层级 /PageName/ 或唯一中文层级 /cn/PageName/
    """
    result = []
    for u in urls:
        path = urlparse(u).path.rstrip("/")
        path_lower = path.lower()
        if "r1000" in path_lower:
            continue
        segments = [s for s in path.split("/") if s]
        if len(segments) == 1:
            result.append(u)
        elif len(segments) == 2 and segments[0].lower() == "cn":
            result.append(u)
    return result


def get_urls_by_keywords(
    keywords: list[str],
    sitemap_url: str = "https://wiki.seeedstudio.com/sitemap.xml",
) -> list[str]:
    """从 sitemap 取全部 URL，按多关键词过滤，再按层级规则过滤后返回。"""
    urls = get_urls_from_sitemap(sitemap_url)
    urls = filter_urls_by_keywords(urls, keywords)
    return filter_urls_by_tier(urls)


def get_urls_from_page(base_url: str, keyword: str) -> list[str]:
    """从 base_url 页面抓取所有同站链接，并过滤出 path 中含 keyword 的。"""
    soup = fetch_page(base_url)  # 你已有，返回 BeautifulSoup
    seen = set()
    kw = keyword.lower()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        full = urljoin(base_url, href)
        if "wiki.seeedstudio.com" not in full or full in seen:
            continue
        if kw in urlparse(full).path.lower():
            seen.add(full)
    return list(seen)


def crawl_by_keyword(keyword: str, sitemap_url: str = "https://wiki.seeedstudio.com/sitemap.xml"):
    urls = get_urls_from_sitemap(sitemap_url)
    urls = filter_urls_by_keyword(urls, keyword)
    print(f"关键词 '{keyword}' 匹配到 {len(urls)} 个页面")


def sanitize_filename(name: str) -> str:
    """去掉文件名非法字符。"""
    for c in '\\/:*?"<>|':
        name = name.replace(c, "_")
    return name.strip() or "untitled"


class GetWikiContent:
    def __init__(self, url: str):
        self.url = url

    def get_content(self) -> tuple[str, str]:
        html = fetch_page(self.url)
        title, markdown_text = html_to_markdown(html, selector=".theme-doc-markdown")
        markdown_text = remove_resource(markdown_text)
        return _ensure_utf8(title), _ensure_utf8(markdown_text)