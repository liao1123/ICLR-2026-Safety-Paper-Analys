# unknown_category

Records whose `detailed_category` is not in `utils.detailed_categories`.

**Paper count**: 1

---

### Flattery, Fluff, and Fog: Diagnosing and Mitigating Idiosyncratic Biases in Preference Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Anirudh Bharadwaj, Chaitanya Malaviya, Nitish Joshi, Mark Yatskar
- **Keywords**: reward models, LLM-based evaluators, biases
- **OpenReview**: https://openreview.net/forum?id=tsfjjfhEz7
- **PDF**: https://openreview.net/pdf?id=tsfjjfhEz7

**Abstract**

Language models serve as proxies for human preference judgements in alignment and evaluation, yet they exhibit systematic miscalibration, prioritizing superficial patterns over substantive qualities. This bias manifests as overreliance on features like length, structure, and style, leading to issues like reward hacking and unreliable evaluations. However, the connection between training data artifacts and the miscalibrated preferences exhibited by models remains poorly understood.

In this work, we systematically investigate the relationship between training data biases and preference model miscalibration across five idiosyncratic features of language model generations: length, structure, jargon, sycophancy and vagueness. Using controlled counterfactual pairs, we first quantify the extent to which preference models favor responses with artificially magnified biases (\textit{skew}), finding this preference occurs in $>60$\% of instances, and model preferences show high \textit{miscalibration} ($\approx 40$\%) compared to human preferences. Notably, bias features only show mild negative correlations to human preference labels (mean $r_{\mathrm{human}} = -0.12$) but show moderately strong positive correlations with labels from a strong reward model (mean $r_{\mathrm{model}} = +0.36$), suggesting that models may overrely on spurious cues.

To mitigate these issues, we propose a simple post-training method based on counterfactual data augmentation (CDA) using synthesized contrastive examples. Fine-tuning models with CDA reduces average miscalibration from 39.4\% to 32.5\% and average absolute skew difference from 20.5\% to 10.0\%, while maintaining overall RewardBench performance, indicating that targeted debiasing can strengthen the reliability of preference models within standard alignment pipelines.

**Abstract (Chinese)**

语言模型在对齐和评估中充当人类偏好判断的代理，然而它们表现出系统性校准偏差，优先考虑表面模式而非实质质量。这种偏差表现为过度依赖长度、结构和风格等特征，导致奖励操纵和不可靠评估等问题。然而，训练数据伪影与模型表现出的校准偏差偏好之间的联系仍未得到充分理解。

在本工作中，我们系统地探讨了训练数据偏差与偏好模型校准偏差之间的关系，针对语言模型生成的五个特异性特征：长度、结构、行话、奉承性和模糊性。使用控制的反事实对，我们首先量化了偏好模型偏好人工放大的偏差响应的程度（\textit{skew}），发现这种偏好在超过60\%的实例中发生，且模型偏好相对于人类偏好显示出较高的\textit{校准偏差}（$\approx 40\%$）。值得注意的是，偏差特征与人类偏好标签仅显示出轻微负相关（平均$r_{\mathrm{human}} = -0.12$），但与强奖励模型标签显示出中等强度的正相关（平均$r_{\mathrm{model}} = +0.36$），表明模型可能过度依赖虚假线索。

为缓解这些问题，我们提出了一种基于反事实数据增强（CDA）的简单后训练方法，使用合成的对比示例对模型进行微调。使用CDA微调模型将平均校准偏差从39.4\%降低至32.5\%，平均绝对偏差差从20.5\%降低至10.0\%，同时保持整体RewardBench性能，这表明针对性去偏可以在标准对齐管道中增强偏好模型的可靠性。

---
