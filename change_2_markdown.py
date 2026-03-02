# 分不同的类别来对 llm 分类后的 paper 进行整理，并保存成 markdown 文件，方便之后上传到 github 上
import os
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

from utils import load_jsonl, detailed_categories


def _as_list(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i) for i in x]
    if isinstance(x, str):
        # 兼容 keywords 可能是 "a, b, c" 或 "a;b;c"
        if ";" in x:
            return [i.strip() for i in x.split(";") if i.strip()]
        if "," in x:
            return [i.strip() for i in x.split(",") if i.strip()]
        if x.strip():
            return [x.strip()]
        return []
    return [str(x)]


def _md_escape(s: str) -> str:
    # 最简单的 escape，避免破坏 markdown 表格/列表
    return s.replace("\r\n", "\n").replace("\r", "\n")


def _paper_to_md(p: Dict[str, Any]) -> str:
    title = _md_escape(p.get("title", "") or "")
    authors = _as_list(p.get("authors"))
    keywords = _as_list(p.get("keywords"))
    venue = _md_escape(p.get("venue", "") or "")
    url = _md_escape(p.get("url", "") or "")
    pdf = _md_escape(p.get("pdf", "") or "")
    abstract = _md_escape(p.get("abstract", "") or "")
    abstract_zh = _md_escape(p.get("abstract_zh", "") or "")

    lines: List[str] = []
    lines.append(f"### {title}".strip())
    lines.append("")
    if venue:
        lines.append(f"- **Venue**: {venue}")
    if authors:
        lines.append(f"- **Authors**: {', '.join(authors)}")
    if keywords:
        lines.append(f"- **Keywords**: {', '.join(keywords)}")
    if url:
        lines.append(f"- **OpenReview**: {url}")
    if pdf:
        lines.append(f"- **PDF**: {pdf}")
    lines.append("")
    if abstract:
        lines.append("**Abstract**")
        lines.append("")
        lines.append(abstract)
        lines.append("")

    if abstract_zh:
        lines.append("**Abstract (Chinese)**")
        lines.append("")
        lines.append(abstract_zh)
        lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _safe_filename(name: str) -> str:
    # category key 本身是安全的，但仍做下兜底
    keep = []
    for ch in name:
        if ch.isalnum() or ch in ("_", "-", "."):
            keep.append(ch)
        else:
            keep.append("_")
    return "".join(keep)


def _sort_key_for_paper(p: Dict[str, Any]) -> Tuple[str, str]:
    # 先按 venue 再按 title，便于浏览
    return (str(p.get("venue", "") or ""), str(p.get("title", "") or ""))


def main() -> None:
    llm_category_save_path = "paper_info/llm_category_iclr_2026_safety_papers_info.jsonl"
    output_path = "markdown"
    data = load_jsonl(llm_category_save_path)
    print(f"Loaded {len(data)} records from {llm_category_save_path}")

    # 初始化所有类别（保证即使为空也会生成文件）
    papers_by_cat: Dict[str, List[Dict[str, Any]]] = {k: [] for k in detailed_categories.keys()}
    unknown_bucket: List[Dict[str, Any]] = []

    for rec in data:
        cat = rec.get("detailed_category")
        if cat in papers_by_cat:
            papers_by_cat[cat].append(rec)
        else:
            unknown_bucket.append(rec)

    # 写每个类别的 markdown
    index_lines: List[str] = []
    index_lines.append("# ICLR 2026 Safety-Related Papers (Grouped by Detailed Category)")
    index_lines.append("")
    index_lines.append(f"Data source: `{llm_category_save_path}`")
    index_lines.append("")
    index_lines.append("## Categories")
    index_lines.append("")
    index_lines.append("## Distribution")
    index_lines.append("")
    index_lines.append("![LLM-category distribution](../pic/llm_category_iclr_2026_safety_papers_distribution.png)")
    index_lines.append("")

    for cat, desc in detailed_categories.items():
        papers = sorted(papers_by_cat.get(cat, []), key=_sort_key_for_paper)
        filename = f"{_safe_filename(cat)}.md"
        out_path = os.path.join(output_path, filename)

        md_lines: List[str] = []
        md_lines.append(f"# {cat}")
        md_lines.append("")
        md_lines.append(f"**Description**: {desc}")
        md_lines.append("")
        md_lines.append(f"**Paper count**: {len(papers)}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

        for p in papers:
            md_lines.append(_paper_to_md(p))

        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines).rstrip() + "\n")

        index_lines.append(f"- `{cat}` ({len(papers)}): [{filename}]({filename})")
        index_lines.append(f"  - {desc}")

    # unknown 类别单独输出，方便排查
    if unknown_bucket:
        unknown_bucket_sorted = sorted(unknown_bucket, key=_sort_key_for_paper)
        filename = "unknown_category.md"
        out_path = os.path.join(output_path, filename)

        md_lines = []
        md_lines.append("# unknown_category")
        md_lines.append("")
        md_lines.append("Records whose `detailed_category` is not in `utils.detailed_categories`.")
        md_lines.append("")
        md_lines.append(f"**Paper count**: {len(unknown_bucket_sorted)}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
        for p in unknown_bucket_sorted:
            md_lines.append(_paper_to_md(p))

        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines).rstrip() + "\n")

        index_lines.append("")
        index_lines.append("## Uncategorized / Unknown")
        index_lines.append("")
        index_lines.append(f"- `unknown_category` ({len(unknown_bucket_sorted)}): [{filename}]({filename})")

    # 写总目录
    index_path = os.path.join(output_path, "README.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines).rstrip() + "\n")

    print(f"Done. Markdown files saved to: {output_path}")


if __name__ == "__main__":
    main()
