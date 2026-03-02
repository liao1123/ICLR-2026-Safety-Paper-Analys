# ICLR 2026 Safety Paper Analyse

## 目的
调用 OpenReview API 获取 ICLR 2026 的中稿论文，筛选安全相关论文并进行统计分析；随后使用 LLM 进行细粒度类别标注与摘要中文翻译，最终按类别生成可直接上传 GitHub 的 Markdown 目录，便于后续阅读与维护（在markdown文件下进行阅读）。

## 目录结构（关键产物）
- `paper_info/`
  - `iclr_2026_papers_info.jsonl`：ICLR 2026 中稿论文信息
  - `iclr_2026_safety_papers_info.jsonl`：筛选出的安全相关论文信息
  - `llm_category_iclr_2026_safety_papers_info.jsonl`：LLM 细分类 + 中文摘要翻译后的结果（含 `detailed_category` / `abstract_zh`）
- `pic/`
  - `iclr_2026_safety_papers_keywords_wordcloud.png`：安全论文关键词词云
  - `llm_category_iclr_2026_safety_papers_distribution.png`：LLM 细分类分布图
- `markdown/`
  - `README.md`：按细分类别汇总目录（并包含分布图）
  - `*.md`：每个细分类别一个 Markdown 文件

## 工作流 / 步骤

### 1) 拉取 ICLR 2026 中稿论文并筛选安全相关
脚本：`get_iclr_2026_paper_info.py`
- 调用 OpenReview 获取 ICLR 2026 conference submissions
- 根据 `state` 筛选 `accept`
- 保存标题、作者、摘要、关键词、OpenReview/PDF 链接等信息
- 基于 `primary_area` 等字段筛选安全相关论文
- 生成关键词词云图：`pic/iclr_2026_safety_papers_keywords_wordcloud.png`

### 2) LLM 细粒度分类 + 摘要中文翻译
脚本：`llm_category_safety_paper.py`
- 使用 `utils.detailed_categories` 中定义的细分类别体系
- 并发调用 LLM 为每篇论文打 `detailed_category`
- 同时对摘要进行中文翻译并写入 `abstract_zh`
- 输出：`paper_info/llm_category_iclr_2026_safety_papers_info.jsonl`
- 生成细分类分布图：`pic/llm_category_iclr_2026_safety_papers_distribution.png`

### 3) 按类别生成 Markdown 目录（便于 GitHub 浏览）
脚本：`change_2_markdown.py`（或 `read_paper.py`，二者功能类似）
- 读取 `paper_info/llm_category_iclr_2026_safety_papers_info.jsonl`
- 按 `detailed_category` 写入 `markdown/<category>.md`
- 为每篇论文输出：
  - 标题 / venue / 作者 / 关键词 / OpenReview / PDF
  - `Abstract`（英文）
  - `Abstract (Chinese)`（来自 `abstract_zh`）
- 生成总目录：`markdown/README.md`（包含分类列表与分布图）

## 快速开始（推荐执行顺序）
```bash
python get_iclr_2026_paper_info.py
python llm_category_safety_paper.py
python change_2_markdown.py
```
