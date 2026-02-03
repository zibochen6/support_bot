from langchain.tools import tool
import os
from tavily import TavilyClient

client = TavilyClient(api_key="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")


def web_search(query: str, max_results: int = 3) -> str:
    """Search the web and return detailed summaries: AI answer + multiple snippets per source."""
    resp = client.search(
        query=query,
        max_results=max_results,
        search_depth="advanced",  # 多片段、更相关（每源最多 chunks_per_source 段）
        chunks_per_source=3,  # 每条结果最多 3 段摘要（仅 advanced 时生效）
        include_answer="advanced",  # 更详细的 LLM 综合摘要（basic/True 为简短版）
        include_raw_content=False,  # 设为 True 可拿到整页正文，但响应会很大
    )
    parts = []

    # 1. 若有 AI 综合答案，放在最前
    if resp.get("answer"):
        parts.append("## AI Summary\n" + resp["answer"].strip())

    # 2. 各条结果的标题、链接与详细内容
    parts.append("\n## Sources\n")
    for r in resp.get("results", []):
        title = r.get("title", "")
        url = r.get("url", "")
        content = r.get("content", "")
        parts.append(f"Titele:{title}\n- URL: {url}\n- content:\n{content}\n\n============================================")
        # raw = r.get("raw_content") or ""
        # if raw and raw.strip():
        #     parts.append(f"\n原始内容摘要:\n{raw[:2000]}{'...' if len(raw) > 2000 else ''}")

    return "\n".join(parts)


print(web_search("What is reComputer Robotics?"))