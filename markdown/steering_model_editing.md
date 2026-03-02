# steering_model_editing

**Description**: 可控性/行为引导/模型编辑。包括 steering、activation steering、control vectors、prompting/系统指令策略、模型编辑与局部修正、可解释的控制机制、工具使用/代理行为约束等。

**Paper count**: 20

---

### Steering the Herd: A Framework for LLM-based Control of Social Learning

- **Venue**: ICLR 2026 Oral
- **Authors**: Raghu Arghal, Kevin He, Shirin Saeedi Bidokhti, Saswati Sarkar
- **Keywords**: Social learning, LLMs, optimal control, information design, dynamic programming
- **OpenReview**: https://openreview.net/forum?id=RtS4UqSmNt
- **PDF**: https://openreview.net/pdf?id=RtS4UqSmNt

**Abstract**

Algorithms increasingly serve as information mediators -- from social media feeds and targeted advertising to the increasing ubiquity of LLMs. This engenders a joint process where agents combine private, algorithmically-mediated signals with observational learning from peers to arrive at decisions. To study such settings, we introduce a model of controlled sequential social learning in which an information-mediating planner (e.g., an LLM) controls the information precision of agents while they also learn from the decisions of earlier agents. The planner may seek to improve social welfare (an altruistic planner) or to induce a specific action the planner prefers (a biased planner). Our framework presents a new optimization problem for social learning that combines dynamic programming with decentralized action choices and Bayesian belief updates. In this setting, we prove the convexity of the value function and characterize the optimal policies of altruistic and biased planners, which attain desired tradeoffs between the costs they incur and the payoffs they earn from induced agent choices. The characterization reveals that the optimal planner operates in different modes depending on the range of belief values. The modes include investing the maximum allowed resource, not investing any resource, or the investment increasing or decreasing with increase in the belief. Notably, for some ranges of belief the biased planner even intentionally obfuscates the agents' signals. Even under stringent transparency constraints—information parity with individuals, no lying or cherry‑picking, and full observability—we show that information mediation can substantially shift social welfare in either direction. We complement our theory with simulations in which LLMs act as both planner and agents. Notably, the LLM-based planner in our simulations exhibits emergent strategic behavior in steering public opinion that broadly mirrors the trends predicted, though key deviations suggest the influence of non-Bayesian reasoning—consistent with the cognitive patterns of both human users and LLMs trained on human-like data. Together, we establish our framework as a tractable basis for studying the impact and regulation of LLM information mediators that corresponds to real behavior.

**Abstract (Chinese)**

算法日益充当信息中介者——从社交媒体动态和定向广告，到大型语言模型（LLMs）的日益普及。这引发了一个联合过程，其中代理人将私人、算法中介的信号与从同伴的观察学习相结合，以做出决策。为了研究此类情境，我们引入了一个受控序列社会学习模型，其中信息中介规划者（例如，一个LLM）控制代理人的信息精度，同时他们也从早期代理人的决策中学习。规划者可能寻求改善社会福利（利他规划者）或诱导规划者偏好的特定行动（偏向规划者）。我们的框架为社会学习提出一个新的优化问题，该问题结合了动态规划、分散行动选择和贝叶斯信念更新。在这种情境下，我们证明了价值函数的凸性，并刻画了利他规划者和偏向规划者的最优策略，这些策略实现了它们所承担的成本与从诱导代理人选择中获得的收益之间的期望权衡。刻画揭示，最优规划者根据信念值的范围在不同模式下运作。这些模式包括投入最大允许资源、不投入任何资源，或随着信念增加而投资增加或减少。值得注意的是，对于某些信念范围，偏向规划者甚至故意混淆代理人的信号。即使在严格的透明度约束下——与个人的信息对等、不说谎或挑选有利信息，以及完全可观察性——我们也表明，信息中介可以显著地将社会福利向任一方向转移。我们通过模拟来补充我们的理论，其中LLMs同时充当规划者和代理人。值得注意的是，我们模拟中的基于LLM的规划者在引导公众舆论方面表现出涌现的战略行为，这广泛反映了预测的趋势，尽管关键偏差表明了非贝叶斯推理的影响——这与人类用户和训练于类人数据LLMs的认知模式一致。总之，我们建立了我们的框架作为一个可处理的基石，用于研究LLM信息中介者的影响和监管，并对应于真实行为。

---

### AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Fengpeng Li, Kemou Li, Qizhou Wang, Bo Han, Jiantao Zhou
- **Keywords**: Adversarial Learning; Prompt Injection Attacks; Adversarial Defending
- **OpenReview**: https://openreview.net/forum?id=3y3hnL7KhS
- **PDF**: https://openreview.net/pdf?id=3y3hnL7KhS

**Abstract**

Concept erasure helps stop diffusion models (DMs) from generating harmful content; but current methods face robustness-retention trade-off. **Robustness** means the model fine-tuned by concept erasure methods resists reactivation of erased concepts, even under semantically related prompts. **Retention** means unrelated concepts are preserved so the model’s overall utility stays intact. Both are critical for concept erasure in practice, yet addressing them simultaneously is challenging, as existing works typically improve one factor while sacrificing the other. Prior work typically strengthens one while degrading the other—e.g., mapping a single erased prompt to a fixed safe target leaves class-level remnants exploitable by prompt attacks, whereas retention-oriented schemes underperform against adaptive adversaries.  This paper introduces Adversarial Erasure with Gradient-Informed Synergy (AEGIS), a retention-data-free framework that advances both robustness and retention. First, AEGIS replaces handpicked targets with an Adversarial Erasure Target (AET) optimized to approximate the semantic center of the erased concept class. By aligning the model’s prediction on the erased prompt to an AET-derived target in the shared text–image space, AEGIS increases predicted-noise distances not just for the instance but for semantically related variants, substantially hardening the DMs against state-of-the-art adversarial prompt attacks. Second, AEGIS preserves utility without auxiliary data via Gradient Regularization Projection (GRP), a conflict-aware gradient rectification that selectively projects away the destructive component of the retention update only when it opposes the erasure direction. This directional, data-free projection mitigates interference between erasure and retention, avoiding dataset bias and accidental relearning. Extensive experiments show that AEGIS markedly reduces attack success rates across various concepts while maintaining or improving FID/CLIP versus advanced baselines, effectively pushing beyond the prevailing robustness–retention trade-off. The source code is in https://github.com/Feng-peng-Li/AEGIS.

**Abstract (Chinese)**

概念擦除有助于阻止扩散模型（DMs）生成有害内容；但当前方法面临鲁棒性-保留性权衡。**鲁棒性**指通过概念擦除方法微调的模型即使在语义相关提示下也能抵抗已擦除概念的重新激活。**保留性**指无关概念得到保留，从而模型的整体效用保持完整。两者在实践中对概念擦除至关重要，然而同时解决它们具有挑战性，因为现有工作通常在提升一个因素的同时牺牲另一个。先前工作通常强化一个同时削弱另一个——例如，将单个擦除提示映射到固定安全目标会留下类级别残留，可被提示攻击利用，而保留性导向方案则在对抗自适应攻击者时表现不佳。本文引入了具有梯度信息协同的对抗性擦除（AEGIS），这是一个无需保留数据的框架，在鲁棒性和保留性上均取得进展。首先，AEGIS 用优化以逼近已擦除概念类语义中心的对抗性擦除目标（AET）替换手工挑选的目标。通过在共享文本-图像空间中将模型对擦除提示的预测对齐到AET派生的目标，AEGIS 不仅增加了实例的预测噪声距离，还增加了语义相关变体的预测噪声距离，从而显著增强了DMs对最先进对抗性提示攻击的抵抗力。其次，AEGIS 通过梯度正则化投影（GRP）在无需辅助数据的情况下保留效用，GRP是一种冲突感知的梯度校正，仅当保留更新与擦除方向相反时选择性地投影掉保留更新的破坏性分量。这种方向性、无数据的投影缓解了擦除与保留之间的干扰，避免了数据集偏差和意外再学习。广泛实验表明，AEGIS 在各种概念上显著降低了攻击成功率，同时相对于先进基线维持或改善了FID/CLIP，有效超越了当前的鲁棒性-保留性权衡。源代码位于 https://github.com/Feng-peng-Li/AEGIS。

---

### ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack

- **Venue**: ICLR 2026 Poster
- **Authors**: Yein Park, Jungwoo Park, Jaewoo Kang
- **Keywords**: Safety, Interpretability, Circuit, Multi-Head Attention, Scaling, Jailbreak Guard
- **OpenReview**: https://openreview.net/forum?id=wmiEXNEXPs
- **PDF**: https://openreview.net/pdf?id=wmiEXNEXPs

**Abstract**

Large language models (LLMs), despite being safety-aligned, exhibit brittle refusal behaviors that can be circumvented by simple linguistic changes.
As tense jailbreaking demonstrates that models refusing harmful requests often comply when rephrased in past tense, a critical generalization gap is revealed in current alignment methods whose underlying mechanisms are poorly understood.
In this work, we introduce Activation-Scaling Guard (ASGuard), an insightful, mechanistically-informed framework that surgically mitigates this specific vulnerability.
In the first step, we use circuit analysis to identify the specific attention heads causally linked to the targeted jailbreaking such as a tense-changing attack.
Second, we train a precise, channel-wise scaling vector to recalibrate the activation of tense vulnerable heads.
Lastly, we apply it into a "preventative fine-tuning", forcing the model to learn a more robust refusal mechanism.
Across four LLMs, ASGuard effectively reduces the attack success rate of targeted jailbreaking while preserving general capabilities and minimizing over refusal, achieving a Pareto-optimal balance between safety and utility.
Our findings underscore how adversarial suffixes suppress the propagation of the refusal-mediating direction, based on mechanistic analysis.
Furthermore, our work showcases how a deep understanding of model internals can be leveraged to develop practical, efficient, and targeted methods for adjusting model behavior, charting a course for more reliable and interpretable AI safety.

**Abstract (Chinese)**

尽管经过安全对齐，大语言模型（LLMs）仍表现出脆弱的拒绝行为，这种行为可被简单的语言变化所规避。正如时态越狱所示，模型拒绝有害请求时，若将其改述为过去时态往往会顺从，从而揭示了当前对齐方法中的关键泛化差距，其底层机制尚不清楚。本工作中，我们引入激活缩放守护（ASGuard），这是一个富有洞见且基于机制的框架，能够精准缓解这一特定漏洞。第一步，我们使用电路分析识别与目标越狱（如时态改变攻击）因果相关的特定注意力头。第二步，我们训练一个精确的通道级缩放向量，以重新校准时态脆弱注意力头的激活。最后，我们将其应用于“预防性微调”，迫使模型学习更稳健的拒绝机制。在四个LLMs上，ASGuard有效降低了目标越狱的攻击成功率，同时保留通用能力并最小化过度拒绝，实现安全与效用之间的帕累托最优平衡。我们的发现基于机制分析，强调了对抗性后缀如何抑制拒绝中介方向的传播。此外，本工作展示了如何利用对模型内部的深刻理解，开发实用、高效且针对性的方法来调整模型行为，为更可靠且可解释的AI安全指明方向。

---

### AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint

- **Venue**: ICLR 2026 Poster
- **Authors**: Leheng Sheng, Changshuo Shen, Weixiang Zhao, Junfeng Fang, Xiaohao Liu, Zhenkai Liang, Xiang Wang, An Zhang, Tat-Seng Chua
- **Keywords**: Large Language Models, Safety, Activation Steering
- **OpenReview**: https://openreview.net/forum?id=1vvbzAqdTe
- **PDF**: https://openreview.net/pdf?id=1vvbzAqdTe

**Abstract**

As LLMs are increasingly deployed in real-world applications, ensuring their ability to refuse malicious prompts, especially jailbreak attacks, is essential for safe and reliable use. Recently, activation steering has emerged as an effective approach for enhancing LLM safety by adding a refusal direction vector to internal activations of LLMs during inference, which will further induce the refusal behaviors of LLMs. However, indiscriminately applying activation steering fundamentally suffers from the trade-off between safety and utility, since the same steering vector can also lead to over-refusal and degraded performance on benign prompts. Although prior efforts, such as vector calibration and conditional steering, have attempted to mitigate this trade-off, their lack of theoretical grounding limits their robustness and effectiveness. To better address the trade-off between safety and utility, we present a theoretically grounded and empirically effective activation steering method called AlphaSteer. Specifically, it considers activation steering as a learnable process with two principled learning objectives: utility preservation and safety enhancement. For utility preservation, it learns to construct a nearly zero vector for steering benign data, with the null-space constraints. For safety enhancement, it learns to construct a refusal direction vector for steering malicious data, with the help of linear regression. Experiments across multiple jailbreak attacks and utility benchmarks demonstrate the effectiveness of AlphaSteer, which significantly improves the safety of LLMs without compromising their general capabilities. Our codes are available at \url{https://anonymous.4open.science/r/AlphaSteer-929C/}.

**Abstract (Chinese)**

随着大语言模型（LLMs）日益部署于现实世界应用中，确保其拒绝恶意提示的能力，尤其是针对越狱攻击，对于安全可靠的使用至关重要。最近，激活转向作为一种有效方法脱颖而出，用于通过在推理过程中向LLMs的内部激活添加拒绝方向向量来增强LLM的安全性，从而进一步诱导LLMs的拒绝行为。然而，无差别地应用激活转向从根本上存在安全与效用之间的权衡问题，因为相同的转向向量也可能导致过度拒绝以及在良性提示上的性能下降。尽管先前的工作，如向量校准和条件转向，试图缓解这一权衡，但它们缺乏理论基础限制了其鲁棒性和有效性。为了更好地解决安全与效用之间的权衡，我们提出了一种具有理论基础且经验有效的激活转向方法，称为AlphaSteer。具体而言，它将激活转向视为一个可学习过程，具有两个原则性学习目标：效用保持和安全增强。对于效用保持，它学习构建一个近似零向量来转向良性数据，并施加零空间约束。对于安全增强，它在 линей回归的帮助下学习构建拒绝方向向量来转向恶意数据。多项越狱攻击和效用基准的实验证明了AlphaSteer的有效性，它显著提升了LLMs的安全性，而不损害其通用能力。我们的代码可在 https://anonymous.4open.science/r/AlphaSteer-929C/ 获取。

---

### Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Jianghao Yin, Qin Chen, Kedi Chen, Jie Zhou, Xingjiao Wu, Liang He
- **Keywords**: Large Vision-Language Models, Hallucination
- **OpenReview**: https://openreview.net/forum?id=YtWZdwEG5K
- **PDF**: https://openreview.net/pdf?id=YtWZdwEG5K

**Abstract**

Large Vision-Language Models (LVLMs) exhibit outstanding performance on vision-language tasks but struggle with hallucination problems.
Through in-depth analysis of LVLM activation patterns, we reveal two key findings: 1) truthfulness and visual perception capabilities predominantly engage different subsets of attention heads within the model architecture; and 2) truthfulness steering vectors vary significantly across different semantic contexts. Based on these observations, we propose Dynamic Multimodal Activation Steering, a training-free approach for hallucination mitigation. Our method constructs a semantic-based truthfulness steering vector database and computes visual perception steering vectors, enabling context-aware interventions during inference by dynamically selecting the most relevant steering vectors based on input semantic similarity and applying them to the most influential attention heads. We conduct comprehensive experiments across multiple models and datasets, demonstrating that our approach significantly enhances model performance, outperforming existing state-of-the-art methods.

**Abstract (Chinese)**

大型视觉-语言模型（LVLMs）在视觉-语言任务上表现出色，但仍面临幻觉问题。

通过对LVLM激活模式的深入分析，我们揭示了两个关键发现：1）真实性和视觉感知能力主要激活模型架构中不同的注意力头子集；2）真实性引导向量在不同语义上下文中存在显著差异。基于这些观察，我们提出动态多模态激活引导，这是一种无需训练的幻觉缓解方法。该方法构建基于语义的真实性引导向量数据库，并计算视觉感知引导向量，从而在推理过程中实现上下文感知干预：根据输入语义相似度动态选择最相关的引导向量，并将其应用于最具影响力的注意力头。我们在多个模型和数据集上进行了全面实验，结果表明，该方法显著提升了模型性能，优于现有最先进方法。

---

### Enhancing Trustworthiness of Fine-Tuned LLMs via Regularized Subset Selection

- **Venue**: ICLR 2026 Poster
- **Authors**: Kumar Shubham, Nishant Sharma, Karn Tiwari, Prathosh AP
- **Keywords**: LLM, Trustworthiness, Subset Selection, Submodularity, Data Attribution
- **OpenReview**: https://openreview.net/forum?id=cXo4vQudaa
- **PDF**: https://openreview.net/pdf?id=cXo4vQudaa

**Abstract**

Supervised fine-tuning (SFT) improves large language model (LLM) perplexity but can also degrade trustworthiness—leading to the generation of untruthful, biased, or unsafe content during user interactions. These issues are often traced back to specific phrases or patterns in the training data. However, correcting them usually requires expensive retraining or new data collection. In this work, we propose a two-stage, compute-efficient repair of the post-SFT models that enhances trustworthiness while preserving the downstream performance. In the first stage, we identify the training samples responsible for failures on trustworthiness metrics like truthfulness, stereotypical bias, and machine ethics—and select a small, diverse subset of these examples using a determinantal point process (DPP)-based regularization. In the second stage, we repair the model under the framework of proximal Bregman response function (PBRF) using a gradient ascent update, which enhances trustworthiness while preserving downstream task performance (perplexity). We evaluate our method on multiple LLMs of varying sizes and demonstrate up to 21\% improvement in trustworthiness metrics with minimal impact ($\leq1$ %) on perplexity. Our method provides a computationally efficient approach to enhance post-SFT models and offers a practical alternative to hours of retraining required for model repair

**Abstract (Chinese)**

监督微调（SFT）改善了大语言模型（LLM）的困惑度，但也可能降低其可信度——导致在用户交互中生成不真实、偏见或不安全的內容。这些问题通常可追溯到训练数据中的特定短语或模式。然而，纠正这些问题通常需要昂贵的重新训练或新数据收集。在本工作中，我们提出了一种两阶段的计算高效的后SFT模型修复方法，该方法在保持下游性能的同时提升可信度。在第一阶段，我们识别导致可信度指标（如真实性、刻板印象偏见和机器伦理）失败的训练样本——并使用基于行列式点过程（DPP）的正则化选择这些示例的一个小型、多样化子集。在第二阶段，我们在近端Bregman响应函数（PBRF）框架下使用梯度上升更新修复模型，该方法提升可信度同时保持下游任务性能（困惑度）。我们在多个不同规模的LLM上评估了我们的方法，并展示了可信度指标高达21\%的改进，同时对困惑度的影响最小（$\leq1$ \%）。我们的方法为提升后SFT模型提供了计算高效的方法，并为模型修复所需的数小时重新训练提供了实用替代方案。

---

### Fine-tuning Done Right in Model Editing

- **Venue**: ICLR 2026 Poster
- **Authors**: Wanli Yang, Rui Tang, Hongyu Zang, Du Su, Qi Cao, Jingang Wang, Huawei Shen, Xueqi Cheng, Fei Sun
- **Keywords**: Model Editing, Fine-tuning, Knowledge Editing, Lifelong Editing, Localized Fine-tuning
- **OpenReview**: https://openreview.net/forum?id=cfHuA5jsPt
- **PDF**: https://openreview.net/pdf?id=cfHuA5jsPt

**Abstract**

Fine-tuning, a foundational method for adapting large language models, has long been considered ineffective for model editing.
Here, we challenge this belief, arguing that the reported failure arises not from the inherent limitation of fine-tuning itself, but from adapting it to the sequential nature of the editing task, a single-pass depth-first pipeline that optimizes each sample to convergence before moving on.
While intuitive, this depth-first pipeline coupled with sample-wise updating over-optimizes each edit and induces interference across edits.
Our controlled experiments reveal that simply restoring fine-tuning to the standard breadth-first (i.e., epoch-based) pipeline with mini-batch optimization substantially improves its effectiveness for model editing.
Moreover, fine-tuning in editing also suffers from suboptimal tuning parameter locations inherited from prior methods. 
Through systematic analysis of tuning locations, we derive LocFT-BF, a simple and effective localized editing method built on the restored fine-tuning framework.
Extensive experiments across diverse LLMs and datasets demonstrate that LocFT-BF outperforms state-of-the-art methods by large margins. 
Notably, to our knowledge, it is the first to sustain 100K edits and 72B-parameter models,10 $\times$ beyond prior practice, without sacrificing general capabilities.
By clarifying a long-standing misconception and introducing a principled localized tuning strategy, we advance fine-tuning from an underestimated baseline to a leading method for model editing, establishing a solid foundation for future research.

**Abstract (Chinese)**

微调作为适应大型语言模型的基础方法，长期以来被认为不适用于模型编辑。

在这里，我们挑战这一信念，认为报告的失败并非源于微调本身的固有局限性，而是源于将其适应编辑任务的顺序性质，即一种单次深度优先管道，在继续下一个样本之前将每个样本优化至收敛。

虽然直观，这种深度优先管道结合样本级更新会过度优化每个编辑，并在编辑之间引入干扰。

我们的控制实验表明，简单地将微调恢复到标准的广度优先（即基于轮次的）管道，并采用小批量优化，即可大幅提升其在模型编辑中的有效性。

此外，编辑中的微调还遭受先前方法继承的次优调优参数位置问题。

通过对调优位置的系统分析，我们推导出LocFT-BF，这是一种基于恢复微调框架的简单有效的局部化编辑方法。

在多样化的大型语言模型和数据集上的广泛实验表明，LocFT-BF以巨大优势超越了最先进的方法。

值得注意的是，据我们所知，它是第一个能够在不牺牲通用能力的情况下维持100K次编辑和720亿参数模型的方法，超出先前实践10倍。

通过澄清一个长期存在的误解并引入一种原则性的局部化调优策略，我们将微调从被低估的基线推进为模型编辑的领先方法，为未来研究奠定坚实基础。

---

### Inference-Time Personalized Safety Control via Paired Difference-in-Means Intervention

- **Venue**: ICLR 2026 Poster
- **Authors**: Tran Huynh, Ruoxi Jia
- **Keywords**: safety alignment, personalized alignment
- **OpenReview**: https://openreview.net/forum?id=VHiHVBNy1M
- **PDF**: https://openreview.net/pdf?id=VHiHVBNy1M

**Abstract**

Safety preferences are inherently subjective, yet current LLM safety alignment methods often impose universal standards that fail to account for individual sensitivities. In this work, we propose an efficient, training-free method for personalized safety control via inference-time activation intervention. Our approach steers internal representations to suppress user-specific undesired content while preserving model utility. We systematically evaluate three strategies for estimating intervention directions: Instance-Level Contrast Shift (ILCS), Unpaired Mean Shift (UMS), and our primary method, Paired Contrast Mean Shift (PCMS). We provide theoretical insights into each approach and highlight the advantages of PCMS. Empirical results across diverse open-weight models demonstrate that our method effectively reduces undesired content in line with individual preferences, with minimal impact on helpfulness—enabling more adaptive and user-aligned LLM behavior.

**Abstract (Chinese)**

安全偏好本质上是主观的，然而当前的LLM安全对齐方法往往强加通用标准，而未能考虑个体敏感性。在这项工作中，我们提出了一种高效的、无需训练的个性化安全控制方法，通过推理时的激活干预实现。我们的方法引导内部表示以抑制用户特定的不良内容，同时保留模型效用。我们系统地评估了三种估计干预方向的策略：实例级对比偏移（ILCS）、非配对均值偏移（UMS），以及我们的主要方法——配对对比均值偏移（PCMS）。我们为每种方法提供了理论洞见，并突出了PCMS的优势。在多样化的开源权重模型上的实证结果表明，我们的方法能有效减少符合个体偏好的不良内容，同时对帮助性的影响最小——从而实现更具适应性和用户对齐的LLM行为。

---

### LatentQA: Teaching LLMs to Decode Activations Into Natural Language

- **Venue**: ICLR 2026 Poster
- **Authors**: Alexander Pan, Lijie Chen, Jacob Steinhardt
- **Keywords**: AI Safety, Activation Engineering, Top-Down Transparency of Language Models
- **OpenReview**: https://openreview.net/forum?id=niUroX9EOd
- **PDF**: https://openreview.net/pdf?id=niUroX9EOd

**Abstract**

Top-down transparency typically analyzes language model activations using probes with scalar or single-token outputs, limiting the range of behaviors that can be captured. To alleviate this issue, we develop a more expressive probe that can directly output natural language and perform LatentQA: the task of answering open-ended questions about activations. A key difficulty in developing such a probe is collecting a dataset mapping activations to natural-language descriptions. In response, we propose an approach for generating a pseudo-labeled dataset of activations and associated question-answer pairs and develop a fine-tuning method for training a decoder LLM on this dataset. We then validate our decoder’s fidelity by assessing its ability to read and steer model activations. First, we evaluate the decoder on a number of supervised reading tasks with a known answer, such as uncovering hidden system prompts and relational knowledge extraction, and observe that it outperforms competitive probing baselines. Second, we demonstrate that the decoder is precise enough to steer the target model to exhibit behaviors unseen during training. Finally, we show that LatentQA scales well with increasing dataset and model size, which is promising given how easily our approach can generate additional pseudo-labels.

**Abstract (Chinese)**

自上而下的透明度通常使用具有标量或单标记输出的探针来分析语言模型激活，从而限制了所能捕获的行为范围。为了缓解这一问题，我们开发了一种更具表达力的探针，该探针能够直接输出自然语言并执行LatentQA：关于激活的开放式问题回答任务。开发此类探针的一个关键难点是收集将激活映射到自然语言描述的数据集。作为回应，我们提出了一种生成激活及其相关问答对的伪标签数据集的方法，并开发了一种在该数据集上训练解码器大语言模型的微调方法。然后，我们通过评估其读取和引导模型激活的能力来验证解码器的保真度。首先，我们在几个具有已知答案的监督阅读任务上评估解码器，例如揭示隐藏系统提示和关系知识提取，并观察到它优于竞争性的探针基线。其次，我们证明了解码器足够精确，能够引导目标模型表现出训练期间未见过的行为。最后，我们展示了LatentQA随着数据集和模型规模的增加而良好扩展，这一点很有前景，因为我们的方法可以轻松生成额外的伪标签。

---

### MoEEdit: Efficient and Routing-Stable Knowledge Editing for Mixture-of-Experts LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Yupu Gu, Rongzhe Wei, Andy Zhu, Pan Li
- **Keywords**: Knowledge Editing; Mixture-of-Experts; Large Language Models
- **OpenReview**: https://openreview.net/forum?id=BV4oHxGBx7
- **PDF**: https://openreview.net/pdf?id=BV4oHxGBx7

**Abstract**

Knowledge editing (KE) is crucial for making precise modifications to factual knowledge within large language models (LLMs). Existing KE methods, however, are primarily designed for dense architectures, limiting their applicability to the increasingly popular sparse Mixture-of-Experts (MoE) models that power modern scalable LLMs. While MoEs offer remarkable efficiency and capacity scaling, their unique structure introduces new challenges for KE. Naively adapting dense-model editors to MoEs is not only computationally expensive but also induces routing distribution shifts that degrade model stability and consistency. To address these challenges, we introduce MoEEdit, the first systematic framework for routing-stable knowledge editing in MoE LLMs. Our approach reparameterizes expert updates through per-expert null-space projections, ensuring router inputs remain invariant to suppress these shifts, and solves the resulting block-structured optimization with an efficient block coordinate descent (BCD) solver. Experiments demonstrate that MoEEdit achieves state-of-the-art efficacy and generalization, while maintaining high specificity, routing stability, and superior computational and memory efficiency. Our work establishes a robust foundation for scalable and precise knowledge editing in modern sparse LLMs by highlighting the necessity of routing-stable interventions.

**Abstract (Chinese)**

知识编辑 (KE) 对于对大型语言模型 (LLMs) 中的事实知识进行精确修改至关重要。然而，现有的 KE 方法主要针对稠密架构设计，这限制了它们在日益流行的稀疏专家混合 (MoE) 模型中的适用性，这些模型驱动着现代可扩展的 LLMs。虽然 MoE 模型提供了卓越的效率和容量扩展，但其独特结构为 KE 引入了新的挑战。将稠密模型编辑器天真地适应到 MoE 模型不仅计算昂贵，而且会诱发路由分布偏移，从而降低模型稳定性和一致性。为了应对这些挑战，我们引入了 MoEEdit，这是第一个用于 MoE LLMs 中路由稳定的知识编辑的系统框架。我们的方法通过每个专家的零空间投影重新参数化专家更新，确保路由器输入保持不变以抑制这些偏移，并使用高效的块坐标下降 (BCD) 求解器求解由此产生的块结构优化。实验表明，MoEEdit 实现了最先进的效能和泛化能力，同时保持高特异性、路由稳定性和优越的计算和内存效率。我们的工作通过强调路由稳定干预的必要性，为现代稀疏 LLMs 中的可扩展和精确知识编辑奠定了坚实基础。

---

### Persona Features Control Emergent Misalignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Miles Wang, Tom Dupre la Tour, Olivia Watkins, Aleksandar Makelov, Ryan Andrew Chi, Samuel Miserendino, Jeffrey George Wang, Achyuta Rajaram, Johannes Heidecke, Tejal Patwardhan, Daniel P Mossing
- **Keywords**: interpretability, alignment, safety
- **OpenReview**: https://openreview.net/forum?id=yjrVOxjkDR
- **PDF**: https://openreview.net/pdf?id=yjrVOxjkDR

**Abstract**

Understanding how language models generalize behaviors from their training to a broader deployment distribution is an important problem in AI safety. Betley et al. discovered that fine-tuning GPT-4o on intentionally insecure code causes "emergent misalignment," where models give stereotypically malicious responses to unrelated prompts. We extend this work, demonstrating emergent misalignment across diverse conditions, including reinforcement learning on reasoning models, fine-tuning on various synthetic datasets, and in models without safety training. To investigate the mechanisms behind this generalized misalignment, we apply a "model diffing" approach using sparse autoencoders to compare internal model representations before and after fine-tuning. This approach reveals several "misaligned persona" features in activation space, including a toxic persona feature which most strongly controls emergent misalignment and can be used to predict whether a model will exhibit such behavior. Additionally, we investigate mitigation strategies, discovering that fine-tuning an emergently misaligned model on just a few hundred benign samples efficiently restores alignment.

**Abstract (Chinese)**

理解语言模型如何将其训练行为泛化到更广泛的部署分布，是 AI 安全中的一个重要问题。Betley 等发现，对 GPT-4o 在故意不安全的代码上进行微调会导致“涌现失准”，即模型对不相关的提示给出刻板化的恶意响应。我们扩展了这一工作，证明涌现失准出现在多种条件下，包括在推理模型上的强化学习、对各种合成数据集的微调，以及没有安全训练的模型中。为了探究这种泛化失准背后的机制，我们采用“模型 diffing”方法，使用稀疏自编码器比较微调前后内部模型表示。该方法揭示了激活空间中的几个“失准人格”特征，其中一个有毒人格特征最强烈地控制涌现失准，并可用于预测模型是否会表现出此类行为。此外，我们探究了缓解策略，发现仅用几百个良性样本对涌现失准模型进行微调即可高效恢复对齐。

---

### ProSafePrune: Projected Safety Pruning for Mitigating Over-Refusal in LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Zijun Chen, Wenbo Hu, Ya Li, Lei Miao, Guoping Hu, Richang Hong
- **Keywords**: LLM, Safety, Over-Refusal, Alignment
- **OpenReview**: https://openreview.net/forum?id=QkHKaPfRAB
- **PDF**: https://openreview.net/pdf?id=QkHKaPfRAB

**Abstract**

Large Language Models (LLMs) excel in various domains, but their safe deployment faces the challenge of balancing safety and utility. Existing alignment strategies often strengthen refusal mechanisms to reduce harmful outputs, but harmless instructions with superficial risky words are mistakenly rejected, which is known as over-refusal. 
This work first reveals that over-refusal stems from a cognitive bias in the model's internal representation space: LLMs naturally encode safety attributes in hidden states, and pseudo-harmful instructions overlap with harmful features, causing over-harmful encoding. 
To address this, we propose ProSafePrune, a subspace-projected low-rank parameter pruning framework for mitigating LLM over-refusal. By projecting pseudo-harmful features into subspaces and removing low-rank directions corresponding to harmful components in the most discriminative layers, we significantly reduce over-refusal while preserving the model’s ability to reject genuinely harmful requests, improving performance on general tasks. In experiments, across different models, our method significantly lowers the average false rejection rate while slightly improving general task performance.

**Abstract (Chinese)**

大型语言模型 (LLMs) 在各种领域表现出色，但其安全部署面临平衡安全性和实用性的挑战。现有的对齐策略通常加强拒绝机制以减少有害输出，但带有表面风险词汇的无害指令被错误拒绝，这种现象被称为过度拒绝。

本工作首先揭示，过度拒绝源于模型内部表示空间中的认知偏差：LLMs 自然地在隐藏状态中编码安全属性，而伪有害指令与有害特征重叠，导致过度有害编码。

为解决这一问题，我们提出 ProSafePrune，这是一个用于缓解 LLM 过度拒绝的子空间投影低秩参数剪枝框架。通过将伪有害特征投影到子空间，并在最具区分性的层中移除对应有害组件的低秩方向，我们显著减少了过度拒绝，同时保留了模型拒绝真正有害请求的能力，并提升了通用任务性能。在实验中，在不同模型上，我们的方法显著降低了平均虚假拒绝率，同时略微提升了通用任务性能。

---

### REAL: Reading Out Transformer Activations for Precise Localization in Language Model Steering

- **Venue**: ICLR 2026 Poster
- **Authors**: Li-Ming Zhan, Bo LIU, Yujie Feng, Chengqiang Xie, Jiannong Cao, Xiao-Ming Wu
- **Keywords**: language modeling; representation engineering
- **OpenReview**: https://openreview.net/forum?id=P38RYdkFLI
- **PDF**: https://openreview.net/pdf?id=P38RYdkFLI

**Abstract**

Inference-time steering aims to alter an LLM’s responses without changing its parameters. A key challenge lies in selecting internal modules that most strongly govern the target behavior; existing approaches often rely on simplistic cues or ad hoc heuristics, leading to suboptimal or unintended effects. In this work, we introduce \modelname{}, a novel framework for identifying behavior-relevant modules (heads or layers) in Transformers. For each module, we train a vector-quantized autoencoder (VQ-AE) on its hidden activations, partitioning the latent space into behavior-relevant and behavior-irrelevant subspaces via a shared, learnable codebook. We quantify each module’s behavioral relevance by evaluating how effectively the VQ-AE encodings distinguish between behavior-aligned and behavior-violating responses using a binary classification metric. This relevance score informs both module selection and steering strength. We evaluate \modelname{} across eight LLMs from two model families (\textsc{Llama} and \textsc{Qwen}) and nine datasets spanning truthfulness enhancement, open-domain question answering under knowledge conflicts, and general alignment tasks. \modelname{} enables more effective inference-time interventions, yielding significant improvements on these steering tasks. Notably, it achieves an average relative improvement of 20\% (up to 81.5\%) over the seminal ITI method~\citep{DBLP:conf/nips/0002PVPW23} on truthfulness steering. Moreover, the modules selected by our method exhibit strong zero-shot generalization in cross-domain truthfulness-steering scenarios. We provide the source code to reproduce all experimental results at \url{https://github.com/liam0949/REAL_ICLR}.

**Abstract (Chinese)**

推理时转向旨在在不改变大语言模型（LLM）参数的情况下改变其响应。一个关键挑战在于选择最强烈控制目标行为的内部模块；现有方法往往依赖于简单的线索或临时启发式，导致次优或意外效果。在这项工作中，我们引入了REAL，一个用于识别Transformer中行为相关模块（注意力头或层）的新框架。对于每个模块，我们在其隐藏激活上训练一个向量量化自编码器（VQ-AE），通过共享的可学习码本将潜在空间划分为行为相关和行为无关子空间。我们通过评估VQ-AE编码在使用二元分类指标下区分行为一致和行为违反响应的有效性来量化每个模块的行为相关性。该相关性分数用于指导模块选择和转向强度。我们在来自两个模型家族（Llama和Qwen）的八个LLM以及九个数据集上评估了REAL，这些数据集涵盖真实性提升、知识冲突下的开放域问答以及通用对齐任务。REAL实现了更有效的推理时干预，在这些转向任务上产生了显著改进。值得注意的是，它在真实性转向上比开创性的ITI方法~\citep{DBLP:conf/nips/0002PVPW23}实现了平均相对改进20\%（最高达81.5\%）。此外，我们方法选择的模块在跨域真实性转向场景中表现出强大的零样本泛化。我们在\url{https://github.com/liam0949/REAL_ICLR}提供源代码以重现所有实验结果。

---

### RepIt: Steering Language Models with Concept-Specific Refusal Vectors

- **Venue**: ICLR 2026 Poster
- **Authors**: Vincent Siu, Nathan W. Henry, Nicholas Crispino, Yang Liu, Dawn Song, Chenguang Wang
- **Keywords**: interpretability, representations, steering, safety
- **OpenReview**: https://openreview.net/forum?id=fsZkx8gek0
- **PDF**: https://openreview.net/pdf?id=fsZkx8gek0

**Abstract**

Current safety evaluations of language models rely on benchmark-based assessments that may miss targeted vulnerabilities. We present RepIt, a simple and data-efficient framework for isolating concept-specific representations in LM activations. While existing steering methods already achieve high attack success rates through broad interventions, RepIt enables a more concerning capability: selective suppression of refusal on targeted concepts while preserving refusal elsewhere. Across five frontier LMs, RepIt produces evaluation-evading models that answer questions related to weapons of mass destruction while still scoring as safe on standard benchmarks. We find  the edit of the steering vector localizes to just 100-200 neurons, and robust concept vectors can be extracted from as few as a dozen examples on a single A6000, highlighting how targeted, hard-to-detect modifications can exploit evaluation blind spots with minimal resources. By demonstrating precise concept disentanglement, this work exposes critical vulnerabilities in current safety evaluation practices and demonstrates an immediate need for more comprehensive, representation-aware assessments.

**Abstract (Chinese)**

当前的语言模型安全评估依赖于基于基准的评估，这些评估可能遗漏针对性的漏洞。我们提出了RepIt，这是一个简单且数据高效的框架，用于在语言模型激活中隔离概念特定的表示。虽然现有的转向方法已通过广泛干预实现了高攻击成功率，但RepIt实现了一种更令人担忧的能力：在目标概念上选择性抑制拒绝，同时在其他地方保留拒绝。在五个前沿语言模型上，RepIt生成了规避评估的模型，这些模型能够回答与大规模杀伤性武器相关的问题，同时在标准基准上仍被评为安全。我们发现转向向量的编辑仅局限于100-200个神经元，并且鲁棒的概念向量可以从单张A6000上仅十几个示例中提取，这突显了针对性、难以检测的修改如何以最小资源利用评估盲点。通过展示精确的概念解纠缠，本工作暴露了当前安全评估实践中的关键漏洞，并证明了对更全面、关注表示的评估的迫切需求。

---

### Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study

- **Venue**: ICLR 2026 Poster
- **Authors**: Kaustubh Ponkshe, Shaan Shah, Raghav Singhal, Praneeth Vepakomma
- **Keywords**: Safety, Alignment, Harmful Fine-Tuning, Large Language Models
- **OpenReview**: https://openreview.net/forum?id=Fj6LakRHcT
- **PDF**: https://openreview.net/pdf?id=Fj6LakRHcT

**Abstract**

Large Language Models (LLMs) rely on safety alignment to produce socially acceptable responses. However, this behavior is known to be brittle: further fine-tuning, even on benign or lightly contaminated data, can degrade safety and reintroduce harmful behaviors. A growing body of work suggests that alignment may correspond to identifiable directions in weight space, forming subspaces that could, in principle, be isolated or preserved to defend against misalignment. In this work, we conduct a comprehensive empirical study of this perspective.
We examine whether safety-relevant behavior is concentrated in specific linear subspaces, whether it can be separated from general-purpose learning, and whether harmfulness arises from distinguishable patterns in activations. Across both weight and activation spaces, our findings are consistent: subspaces that amplify safe behaviors also amplify useful ones, and prompts with different safety implications activate overlapping representations. Rather than residing in distinct directions, we show that safety is highly entangled with the general learning components of the model. This suggests that subspace-based defenses face fundamental limitations and underscores the need for alternative strategies to preserve safety under continued training. We corroborate these findings with multiple experiments on five open-source LLMs from the Llama and Qwen families. Our code is publicly available at: https://github.com/CERT-Lab/safety-subspaces.

**Abstract (Chinese)**

大型语言模型 (LLMs) 依赖安全对齐来生成社会可接受的响应。然而，这种行为已知是脆弱的：进一步微调，即使在良性或轻度污染的数据上，也可能降低安全性并重新引入有害行为。越来越多的工作表明，对齐可能对应于权重空间中可识别的方向，形成子空间，这些子空间原则上可以被隔离或保留以防御错位。在这项工作中，我们对这一观点进行了全面的实证研究。

我们考察了安全相关行为是否集中在特定的线性子空间中、它是否可以与通用学习分离，以及有害性是否源于激活中的可区分模式。在权重和激活空间中，我们的发现一致：放大安全行为的子空间也会放大有用行为，而具有不同安全含义的提示会激活重叠的表示。我们表明，安全并非驻留在不同的方向中，而是高度纠缠于模型的通用学习组件。这表明基于子空间的防御面临根本性限制，并强调了在持续训练下保留安全性的替代策略的必要性。我们通过对 Llama 和 Qwen 家族的五个开源 LLMs 的多项实验来证实这些发现。我们的代码公开可用于：https://github.com/CERT-Lab/safety-subspaces。

---

### Spectrum Tuning: Post-Training for Distributional Coverage and In-Context Steerability

- **Venue**: ICLR 2026 Poster
- **Authors**: Taylor Sorensen, Benjamin Newman, Jared Moore, Chan Young Park, Jillian Fisher, Niloofar Mireshghallah, Liwei Jiang, Yejin Choi
- **Keywords**: post-training, language models, distributional learning, alignment, pluralistic alignment, uncertainty estimation
- **OpenReview**: https://openreview.net/forum?id=ulvp7cbZeU
- **PDF**: https://openreview.net/pdf?id=ulvp7cbZeU

**Abstract**

Language model post-training has enhanced instruction-following and performance on many downstream tasks, but also comes with an often-overlooked cost on tasks with many possible valid answers. On many tasks such as creative writing, synthetic data generation, or steering to diverse preferences, models must cover an entire distribution of outputs, rather than a single correct answer. We characterize three desiderata for conditional distributional modeling: in-context steerability, valid output space coverage, and distributional alignment, and document across three model families how current post-training can reduce these properties. In particular, we disambiguate between two kinds of in-context learning: ICL for eliciting existing underlying knowledge or capabilities, and in-context steerability, where a model must use in-context information to override its priors and steer to a novel data generating distribution. To better evaluate and improve these desiderata, we introduce Spectrum Suite, a large-scale resource compiled from $>40$ data sources and spanning $>90$ tasks requiring models to steer to and match diverse distributions ranging from varied human preferences to numerical distributions and more. We find that while current post-training techniques elicit underlying capabilities and knowledge, they hurt models' ability to flexibly steer in-context. To mitigate these issues, we propose Spectrum Tuning, a post-training method using Spectrum Suite to improve steerability and distributional coverage. We find that Spectrum Tuning often improves over pretrained and typical instruction-tuned models, enhancing steerability, spanning more of the output space, and improving distributional alignment on held-out datasets.

**Abstract (Chinese)**

语言模型后训练提升了指令跟随能力和许多下游任务的性能，但也带来了一个常常被忽略的代价，即在具有多种可能有效答案的任务上。在诸如创意写作、合成数据生成或导向多样化偏好等许多任务中，模型必须覆盖整个输出分布，而不是单一正确答案。我们刻画了条件分布建模的三个期望特性：上下文导向性、有效输出空间覆盖度和分布对齐度，并记录了在三个模型家族中当前后训练如何降低这些特性。特别地，我们区分了两种上下文学习：用于引出现有底层知识或能力的ICL，以及上下文导向性，其中模型必须使用上下文信息来覆盖其先验并导向新型数据生成分布。为了更好地评估和改进这些期望特性，我们引入了Spectrum Suite，这是一个从>40个数据源编译的大型资源，涵盖>90个任务，要求模型导向并匹配多样化分布，从多样化人类偏好到数值分布等。我们发现，虽然当前后训练技术能引出底层能力和知识，但它们损害了模型灵活上下文导向的能力。为了缓解这些问题，我们提出Spectrum Tuning，这是一种使用Spectrum Suite的后训练方法，以提升导向性和分布覆盖。我们发现，Spectrum Tuning通常优于预训练和典型指令微调模型，提升了导向性、覆盖了更多输出空间，并在留出数据集上改善了分布对齐。

---

### Steering Diffusion Models Towards Credible Content Recommendation

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhuo Cai, Shoujin Wang, Jin Li, Peilin Zhou, Victor W. Chu, Fang Chen, Tianqing Zhu, Charu C. Aggarwal
- **Keywords**: Credible content recommendation, Societal Considerations, Diffusion models
- **OpenReview**: https://openreview.net/forum?id=gcT2BCGcZJ
- **PDF**: https://openreview.net/pdf?id=gcT2BCGcZJ

**Abstract**

In recent years, diffusion models (DMs) have achieved remarkable success in recommender systems (RSs), owing to their strong capacity to model the complex distributions of item content and user behaviors. Despite their effectiveness, existing methods pose the danger of generating uncredible content recommendations (e.g., fake news, misinformation) that may significantly harm social well-being, as they primarily emphasize recommendation accuracy while neglecting the credibility of the recommended content. To address this issue, in this paper, we propose Disco, a novel method to steer diffusion models towards credible content recommendation. Specifically, we design a novel disentangled diffusion model to mitigate the harmful influence of uncredible content on the generation process while preserving high recommendation accuracy. This is achieved by reformulating the diffusion objective to encourage generation conditioned on preference-related signals while discouraging generation conditioned on uncredible content-related signals. In addition, to further improve the recommendation credibility, we design a progressively enhanced credible subspace projection that suppresses uncredible content by projecting diffusion targets into the null space of uncredible content. Extensive experiments on real-world datasets demonstrate the effectiveness of Disco in terms of both accurate and credible content recommendations.

**Abstract (Chinese)**

近年来，扩散模型（DMs）在推荐系统（RSs）中取得了显著成功，这得益于它们强大的建模物品内容和用户行为复杂分布的能力。尽管其有效性，现有的方法存在生成不可信内容推荐的风险（例如，假新闻、虚假信息），这可能严重损害社会福祉，因为它们主要强调推荐准确性而忽略了推荐内容的信度。为解决这一问题，本文提出Disco，一种新型方法，用于引导扩散模型向可信内容推荐方向发展。具体而言，我们设计了一种新型解耦扩散模型，以缓解不可信内容对生成过程的有害影响，同时保持高推荐准确性。这是通过重新表述扩散目标来实现的，该目标鼓励基于偏好相关信号的生成，同时抑制基于不可信内容相关信号的生成。此外，为了进一步提升推荐信度，我们设计了一种渐进增强的可信子空间投影，通过将扩散目标投影到不可信内容的零空间中来抑制不可信内容。在真实世界数据集上的广泛实验证明了Disco在准确和可信内容推荐方面的有效性。

---

### Steering Evaluation-Aware Language Models To Act Like They Are Deployed

- **Venue**: ICLR 2026 Poster
- **Authors**: Tim Tian Hua, Andrew Qin, Samuel Marks, Neel Nanda
- **Keywords**: AI safety, Interpretability
- **OpenReview**: https://openreview.net/forum?id=1TdRdf0fkw
- **PDF**: https://openreview.net/pdf?id=1TdRdf0fkw

**Abstract**

Large language models (LLMs) can sometimes detect when they are being evaluated and adjust their behavior to appear more aligned, compromising the reliability of safety evaluations. In this paper, we show that adding a steering vector to an LLM's activations can suppress evaluation-awareness and make the model act like it is deployed during evaluation. To study our steering technique, we train an LLM to exhibit evaluation-aware behavior using a two-step training process designed to mimic how this behavior could emerge naturally. First, we perform continued pretraining on two sets of documents describing its behavior. The first says that our model uses Python type hints during evaluation but not during deployment. The second says that our model can recognize that the presence of a certain evaluation cue always means that it is being tested. Then, we train the model with expert iteration to use Python type hints in evaluation settings. The resulting model is evaluation-aware: it writes type hints in evaluation contexts more than deployment contexts. We find that activation steering can suppress evaluation awareness and make the model behave during evaluation as it would during deployment. Importantly, we constructed our steering vector using the original model before our additional training. Our results suggest that AI evaluators could improve the reliability of safety evaluations by steering models to act like they are deployed.

**Abstract (Chinese)**

大型语言模型（LLMs）有时能够检测到它们正在被评估，并调整其行为以显得更一致，从而损害安全评估的可靠性。本文展示了，向 LLM 的激活添加一个转向向量可以抑制评估意识，并使模型在评估期间表现得像部署时一样。为了研究我们的转向技术，我们使用一个两步训练过程训练一个 LLM 来表现出评估意识行为，该过程旨在模拟这种行为如何自然出现。首先，我们在两组描述其行为的文档上进行持续预训练。第一组表示我们的模型在评估期间使用 Python 类型提示，但在部署期间不使用。第二组表示我们的模型能够识别某个特定评估提示的存在总是意味着它正在被测试。然后，我们使用专家迭代训练模型在评估设置中使用 Python 类型提示。结果模型具有评估意识：在评估上下文中编写类型提示的频率高于部署上下文。我们发现，激活转向可以抑制评估意识，并使模型在评估期间表现得像部署期间一样。重要的是，我们使用额外训练前的原始模型构建了我们的转向向量。我们的结果表明，AI 评估者可以通过转向模型使其表现得像部署时一样，来提高安全评估的可靠性。

---

### Steering Language Models with Weight Arithmetic

- **Venue**: ICLR 2026 Poster
- **Authors**: Constanza Fierro, Fabien Roger
- **Keywords**: steering, alignment, safety, model editing, merging models
- **OpenReview**: https://openreview.net/forum?id=S0D3EFWohd
- **PDF**: https://openreview.net/pdf?id=S0D3EFWohd

**Abstract**

Providing high-quality feedback to Large Language Models (LLMs) on a diverse training distribution can be difficult and expensive, and providing feedback only on a narrow distribution can result in unintended generalizations. To better leverage narrow training data, we propose *contrastive weight steering*, a simple post-training method that edits the model parameters using weight arithmetic. We isolate a behavior direction in weight-space by subtracting the weight deltas from two small fine-tunes---one that induces the desired behavior and another that induces its opposite---and then add or remove this direction to modify the model's weights. We apply this technique to mitigate sycophancy and induce misalignment, and find that weight steering often generalizes further than activation steering, achieving stronger out-of-distribution behavioral control before degrading general capabilities. We also show that, in the context of task-specific fine-tuning, weight steering can partially mitigate undesired behavioral drift: it can reduce sycophancy and under-refusals introduced during fine-tuning while preserving task performance gains. Finally, we provide preliminary evidence that emergent misalignment can be detected by measuring the similarity between fine-tuning updates and an "evil" weight direction, suggesting that it may be possible to monitor the evolution of weights during training and detect rare misaligned behaviors that never manifest during training or evaluations.

**Abstract (Chinese)**

为大语言模型 (LLMs) 在多样化训练分布上提供高质量反馈可能困难且昂贵，而仅在狭窄分布上提供反馈则可能导致意外泛化。为了更好地利用狭窄训练数据，我们提出*对比权重转向*，这是一种简单的后训练方法，使用权重算术编辑模型参数。我们通过减去两个小型微调的权重增量——一个诱导期望行为，另一个诱导其相反行为——在权重空间中隔离行为方向，然后添加或移除此方向来修改模型权重。我们应用此技术来缓解谄媚行为并诱导错位，发现权重转向通常比激活转向泛化更远，在一般能力退化之前实现更强的分布外行为控制。我们还表明，在任务特定微调的背景下，权重转向可以部分缓解 undesired 行为漂移：它可以减少微调过程中引入的谄媚行为和拒绝不足，同时保留任务性能提升。最后，我们提供了初步证据，表明可以通过测量微调更新与“邪恶”权重方向的相似性来检测涌现错位，这表明可以通过监控训练过程中权重的演化来检测那些在训练或评估中从未显现的罕见错位行为。

---

### Superficial Safety Alignment Hypothesis

- **Venue**: ICLR 2026 Poster
- **Authors**: Jianwei Li, Jung-Eun Kim
- **Keywords**: Large Language Model, Safety Alignment
- **OpenReview**: https://openreview.net/forum?id=9yS40pO1RF
- **PDF**: https://openreview.net/pdf?id=9yS40pO1RF

**Abstract**

As large language models (LLMs) are overwhelmingly more and more integrated into various applications, ensuring they generate safe responses is a pressing need. Previous studies on alignment have largely focused on general instruction-following but have often overlooked the distinct properties of safety alignment, such as the brittleness of safety mechanisms. To bridge the gap, we propose the Superficial Safety Alignment Hypothesis (SSAH), which posits that safety alignment teaches an otherwise unsafe model to choose the correct reasoning direction - fulfill or refuse users' requests - interpreted as an implicit binary classification task. Through SSAH, we hypothesize that only a few essential components can establish safety guardrails in LLMs. We successfully identify four types of attribute-critical components: Safety Critical Unit (SCU), Utility Critical Unit (UCU), Complex Unit (CU), and Redundant Unit (RU). Our findings show that freezing certain safety-critical components during fine-tuning allows the model to retain its safety attributes while adapting to new tasks. Similarly, we show that leveraging redundant units in the pre-trained model as an "alignment budget" can effectively minimize the alignment tax while achieving the alignment goal. All considered, this paper concludes that the atomic functional unit for safety in LLMs is at the neuron level and underscores that safety alignment should not be complicated.

**Abstract (Chinese)**

随着大语言模型 (LLMs) 越来越多地被广泛集成到各种应用中，确保它们生成安全响应已成为迫切需求。先前的对齐研究主要关注通用指令跟随，但往往忽略了安全对齐的独特属性，例如安全机制的脆弱性。为了弥合这一差距，我们提出了表面安全对齐假设 (SSAH)，该假设认为安全对齐教导原本不安全的模型选择正确的推理方向——满足或拒绝用户请求——这被解释为一个隐式二元分类任务。通过 SSAH，我们假设仅需少数关键组件即可在大语言模型中建立安全护栏。我们成功识别了四种属性关键组件：安全关键单元 (SCU)、效用关键单元 (UCU)、复杂单元 (CU) 和冗余单元 (RU)。我们的发现表明，在微调过程中冻结某些安全关键组件可以使模型在适应新任务的同时保留其安全属性。同样，我们展示了利用预训练模型中的冗余单元作为“对齐预算”可以有效最小化对齐税，同时实现对齐目标。综上所述，本文得出结论，大语言模型中安全的原子功能单元处于神经元层面，并强调安全对齐不应复杂化。

---
