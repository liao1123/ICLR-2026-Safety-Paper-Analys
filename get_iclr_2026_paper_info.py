import argparse
import json
import os
from collections import Counter
from typing import Any, Iterator

from tqdm import tqdm

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from utils import load_jsonl

import openreview
from dotenv import load_dotenv

load_dotenv()

# 导入需要用到的env信息
openreview_username = os.getenv("OPENREVIEW_USERNAME")
openreview_password = os.getenv("OPENREVIEW_PASSWORD")


# 官方的api接口来进行文章调用管理
openreview_client = openreview.api.OpenReviewClient(
    baseurl='https://api2.openreview.net',
    username=openreview_username,
    password=openreview_password
)

def draw_wordcloud(safety_papers_info_data, pic_save_path):
    single_keywords = []
    for paper in safety_papers_info_data:
        single_keywords.extend(paper.get("keywords", []))
    
    # 统计关键词频率
    keyword_counts = Counter(single_keywords)
    # 生成词云
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(keyword_counts)
    # 显示词云
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(pic_save_path)



# openreview api的get notes会有读取限制，每次只能读取1k，需要循环设置偏移量
def _iter_submission_notes(
    client: openreview.api.OpenReviewClient,
    venue_id: str,
    page_size: int = 1000,
) -> Iterator[openreview.api.Note]:
    """Iterate submission notes from API2 invitation <venue_id>/-/Submission"""
    invitation = f"{venue_id}/-/Submission"
    offset = 0
    seen = 0

    while True:
        notes = client.get_notes(invitation=invitation, limit=page_size, offset=offset)
        if not notes:
            break
        for n in notes:
            yield n
            seen += 1
        offset += page_size

def _is_accepted_by_venue(venue: str) -> bool:
    # 用户选择：venue 以 "ICLR 2026" 开头 且包含 Poster/Oral
    venue = venue.strip()
    if not venue.startswith("ICLR 2026"):
        return False
    return ("Poster" in venue) or ("Oral" in venue)


def _note_to_record(note: openreview.api.Note) -> dict[str, Any]:
    content = note.content or {}

    def get_field(name: str) -> Any:
        v = content.get(name)
        if isinstance(v, dict) and "value" in v:
            return v["value"]
        return v

    record = {
        "id": getattr(note, "id", None),
        "forum": getattr(note, "forum", None),
        # API2 Note 使用 invitations（list），老字段 invitation 可能不存在
        "invitations": getattr(note, "invitations", None),
        "venue": get_field("venue"),
        "venueid": get_field("venueid"),
        "title": get_field("title"),
        "abstract": get_field("abstract"),
        "keywords": get_field("keywords"),
        "authors": get_field("authors"),
        "primary_area": get_field("primary_area"),
        "pdf": f"https://openreview.net/pdf?id={getattr(note, 'id', None)}" if getattr(note, "id", None) else None,
        "url": f"https://openreview.net/forum?id={getattr(note, 'forum', None)}" if getattr(note, "forum", None) else None,
    }
    return record


# （review 拉取相关代码已移除，保留纯论文信息抓取）


def main():
    venue_id = "ICLR.cc/2026/Conference"
    iclr_2026_accept_paper_info_save_path = "paper_info/iclr_2026_paper_info.jsonl" # 保存每一条信息到jsonl文件中，方便后续分析
    if not os.path.exists(iclr_2026_accept_paper_info_save_path):
        total = 0
        kept = 0

        with open(iclr_2026_accept_paper_info_save_path, "w", encoding="utf-8") as f:
            for note in tqdm(_iter_submission_notes(openreview_client, venue_id)):
                total += 1

                # content 字段可能是 dict/value 结构，也可能支持 attribute 访问；这里用更稳的 dict 方式
                venue_field = (note.content or {}).get("venue")
                venue = venue_field.get("value") if isinstance(venue_field, dict) else str(venue_field)

                accepted = _is_accepted_by_venue(venue)  # 通过 venue 来判断是否被 accept，是 oral 还是 poster

                # 跳过被 reject/withdrawn/desk reject 的 paper
                if not accepted:
                    continue

                # 论文主信息
                rec = _note_to_record(note)
                rec["accepted"] = True
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                kept += 1

        print(f"\nDone. fetched={total}, saved={kept}, output={iclr_2026_accept_paper_info_save_path}")
    
    # 按照safety topic来进行过滤，保存新的recodes
    safety_paper_info_save_path = "paper_info/iclr_2026_safety_papers_info.jsonl"
    if os.path.exists(safety_paper_info_save_path):
        safety_papers_info_data = load_jsonl(safety_paper_info_save_path)
    else:
        # 先获取primary_area中与安全有关的分类
        iclr_2026_accept_paper_data = load_jsonl(iclr_2026_accept_paper_info_save_path)
        print(f"iclr 2026 accepted papers count: {len(iclr_2026_accept_paper_data)}")

        # # 先统计一下 primary_area 的分布情况
        # # 从primary中可以知道安全领域标题为'alignment, fairness, safety, privacy, and societal considerations'
        # primary_areas = [r["primary_area"] for r in iclr_2026_accept_paper_data]
        # cnt = Counter(primary_areas)
        # print(f"Primary Area Distribution: {dict(cnt)}")
        # # Primary Area Distribution: {'reinforcement learning': 170, 'interpretability and explainable AI': 123, 'learning on time series and dynamical systems': 49, 'optimization': 110, 'unsupervised, self-supervised, semi-supervised, and supervised representation learning': 115, 'applications to physical sciences (physics, chemistry, biology, etc.)': 112, 'learning on graphs and other geometries & topologies': 53, 'datasets and benchmarks': 270, 'applications to robotics, autonomy, planning': 62, 'learning theory': 132, 'applications to computer vision, audio, language, and other modalities': 260, 'alignment, fairness, safety, privacy, and societal considerations': 216, 'other topics in machine learning (i.e., none of the above)': 95, 'foundation or frontier models, including LLMs': 390, 'generative models': 161, 'probabilistic methods (Bayesian methods, variational inference, sampling, UQ, etc.)': 71, 'applications to neuroscience & cognitive science': 57, 'transfer learning, meta learning, and lifelong learning': 45, 'causal reasoning': 29, 'infrastructure, software libraries, hardware, systems, etc.': 16, 'neurosymbolic & hybrid AI systems (physics-informed, logic & formal reasoning, etc.)': 23}
        
        # 获取与安全相关的论文info
        safety_topic_class = "alignment, fairness, safety, privacy, and societal considerations"
        safety_papers_info_data = [r for r in iclr_2026_accept_paper_data if r["primary_area"] == safety_topic_class]
        print(f"Safety related papers count: {len(safety_papers_info_data)}")

        with open(safety_paper_info_save_path, "w", encoding="utf-8") as f:
            for rec in safety_papers_info_data:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"Safety related papers records saved to: {safety_paper_info_save_path}")
    
    # 从安全领域的论文中，统计一下关键词的分布，画一个云，将keyword拆分单个关键词进行统计
    pic_save_path = "pic/iclr_2026_safety_papers_keywords_wordcloud.png"
    draw_wordcloud(safety_papers_info_data, pic_save_path)

if __name__ == "__main__":
    main()
