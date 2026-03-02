import os
from tqdm import tqdm
from utils import load_jsonl, detailed_categories
import json
import matplotlib.pyplot as plt

from openai import AsyncOpenAI
import asyncio
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("API_KEY")
openai_base_url = os.getenv("BASE_URL")

# 调用llm的接口，方便之后进行文章翻译、分析、embedding 检索等功能
openai_client = AsyncOpenAI(
    api_key=openai_api_key,
    base_url=openai_base_url,
)
    

CLASSIFY_SYSTEM_PROMPT_HEAD = (
    "你是一个学术论文分类助手，请根据以下论文标题、关键词、摘要，以及给定的细分类别及其描述，给出锁定论文的细分类别。\n\n"
)

# 一次性构建完整 system prompt（避免每篇论文重复拼接类别说明）
CLASSIFY_SYSTEM_PROMPT = CLASSIFY_SYSTEM_PROMPT_HEAD
for _cat, _desc in detailed_categories.items():
    CLASSIFY_SYSTEM_PROMPT += f"类别: {_cat}\n描述: {_desc}\n\n"
CLASSIFY_SYSTEM_PROMPT += (
    "输出格式要求：\n"
    "1) 只能输出一个类别 key（必须完全等于上面某个类别名），不要输出任何解释、标点或多余文本。\n"
    "2) 如果无法确定最匹配类别，请输出 'other_safety_related_topics'。\n"
    "3) 不要输出引号、不要输出代码块。\n"
    "示例输出：jailbreak_redteam_attacks\n"
)

CLASSIFY_USER_PROMPT_TEMPLATE = (
    "标题: {title}\n"
    "关键词: {keywords}\n"
    "摘要: {abstract}\n\n"
    "请从给定类别中选择最匹配的一个类别 key，并严格按要求只输出该 key。"
)

TRANSLATE_SYSTEM_PROMPT = (
    "你是一个学术论文写作与翻译助手。请将用户提供的论文英文摘要翻译为中文，保持学术风格、忠实准确、术语一致。\n"
    "输出要求：只输出中文翻译文本，不要添加解释、不要加引号、不要输出代码块。"
)

TRANSLATE_USER_PROMPT_TEMPLATE = "请翻译以下摘要为中文：\n\n{abstract}"


async def run_one(paper_info, openai_client, semaphore, max_retries=5):
    title = paper_info.get("title", "")
    keywords = paper_info.get("keywords", "")
    abstract = paper_info.get("abstract", "")

    existing_category = str(paper_info.get("detailed_category", "") or "").strip()
    existing_abstract_zh = str(paper_info.get("abstract_zh", "") or "").strip()

    need_classify = not existing_category
    need_translate = not existing_abstract_zh and bool(str(abstract).strip())

    # 1) 分类 prompt
    classify_system_prompt = CLASSIFY_SYSTEM_PROMPT
    classify_user_prompt = CLASSIFY_USER_PROMPT_TEMPLATE.format(
        title=title, keywords=keywords, abstract=abstract
    )

    # 2) 翻译 prompt
    translate_system_prompt = TRANSLATE_SYSTEM_PROMPT
    translate_user_prompt = TRANSLATE_USER_PROMPT_TEMPLATE.format(abstract=abstract)

    # 无需任何补全则直接返回（不会覆盖原字段）
    if not need_classify and not need_translate:
        return paper_info

    for attempt in range(max_retries):
        try:
            async with semaphore:
                category = existing_category
                abstract_zh = existing_abstract_zh

                if need_classify:
                    classify_resp = await openai_client.chat.completions.create(
                        model="grok-4-1-fast-reasoning",
                        messages=[
                            {"role": "system", "content": classify_system_prompt},
                            {"role": "user", "content": classify_user_prompt},
                        ],
                        max_tokens=30,
                        temperature=0.0,
                    )
                    category = classify_resp.choices[0].message.content.strip()

                if need_translate:
                    translate_resp = await openai_client.chat.completions.create(
                        model="grok-4-1-fast-reasoning",
                        messages=[
                            {"role": "system", "content": translate_system_prompt},
                            {"role": "user", "content": translate_user_prompt},
                        ],
                        max_tokens=800,
                        temperature=0.0,
                    )
                    abstract_zh = translate_resp.choices[0].message.content.strip()

                output = {
                    **paper_info,
                    "detailed_category": category,
                    "abstract_zh": abstract_zh,
                }
                return output
        except Exception as e:
            print(f"API调用失败 (尝试 {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(1 * (attempt + 1))

def draw_bar(category_count, save_path):
    plt.bar(category_count.keys(), category_count.values())
    plt.xticks(rotation=90)
    plt.title("Distribution of ICLR 2026 Safety-Related Papers (LLM Classification)")
    plt.xlabel("Detailed Category")
    plt.ylabel("Number of Papers")
    plt.tight_layout()
    plt.savefig(save_path)

    
async def main():
    # llm分类之后会增加新的字段保存
    llm_category_save_path = "paper_info/llm_category_iclr_2026_safety_papers_info.jsonl"
    safety_paper_info_save_path = "paper_info/iclr_2026_safety_papers_info.jsonl"

    # 如果已有 llm 结果文件，则在其基础上“补全缺失字段”
    if os.path.exists(llm_category_save_path):
        print(f"LLM分类结果文件已存在，将在其基础上补全缺失字段: {llm_category_save_path}")
        paper_info_data = load_jsonl(llm_category_save_path)
    else:
        print(f"LLM分类结果文件不存在，使用原始安全相关论文信息进行分类: {safety_paper_info_save_path}")
        paper_info_data = load_jsonl(safety_paper_info_save_path)

    # 进一步去细化文章分类，并发调用llm来进行分类/翻译补全
    max_concurrent = 1000
    max_retries = 20
    semaphore = asyncio.Semaphore(max(10, max_concurrent))

    tasks = [
        asyncio.create_task(run_one(paper_info, openai_client, semaphore, max_retries))
        for paper_info in paper_info_data
    ]

    # 覆盖写回（但 run_one 会保留已有字段，只补缺失字段）
    with open(llm_category_save_path, "w", encoding="utf-8") as f:
        for rec in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            output = await rec
            f.write(json.dumps(output, ensure_ascii=False) + "\n")
            f.flush()  # 及时将结果写入文件
    print(f"Safety related papers with detailed categories saved to: {llm_category_save_path}")
    
    llm_category_data = load_jsonl(llm_category_save_path)
    category_count = {}
    for rec in llm_category_data:
        cat = rec.get("detailed_category", "unknown")
        category_count[cat] = category_count.get(cat, 0) + 1
    print(category_count)
    
    # 画一个柱状图
    draw_bar(category_count, "pic/llm_category_iclr_2026_safety_papers_distribution.png")

if __name__ == "__main__":
    asyncio.run(main())
