# alignment_preference_optimization

**Description**: 对齐训练与偏好优化方法。包括 RLHF/RLAIF、DPO/IPO/KTO 等偏好学习、reward modeling、constitutional AI、对齐数据构建、对齐训练稳定性、对齐泛化与分布外行为等。

**Paper count**: 62

---

### Is it Thinking or Cheating?  Detecting Implicit Reward Hacking by Measuring Reasoning Effort

- **Venue**: ICLR 2026 Oral
- **Authors**: Xinpeng Wang, Nitish Joshi, Barbara Plank, Rico Angell, He He
- **Keywords**: Reward Hacking Detection, Chain-of-Thought Monitoring, Reasoning Faithfulness
- **OpenReview**: https://openreview.net/forum?id=Gk7gLAtVDO
- **PDF**: https://openreview.net/pdf?id=Gk7gLAtVDO

**Abstract**

Reward hacking, where a reasoning model exploits loopholes in a reward function to achieve high rewards without solving the intended task, poses a significant threat. This behavior may be explicit, i.e. verbalized in the model's chain-of-thought (CoT), or implicit, where the CoT appears benign thus bypasses CoT monitors. To detect implicit reward hacking, we propose TRACE (Truncated Reasoning AUC Evaluation). Our key observation is that hacking occurs when exploiting the loophole is easier than solving the actual task. This means that the model is using less "effort" than required to achieve high reward.  TRACE quantifies effort by measuring how early a model's reasoning becomes sufficient to obtain the reward. We progressively truncate a model's CoT at various lengths, force the model to answer, and estimate the expected reward at each cutoff. A hacking model, which takes a shortcut, will achieve a high expected reward with only a small fraction of its CoT, yielding a large area under the reward-vs-length curve. TRACE achieves over 65% gains over our strongest 72B CoT monitor in math reasoning, and over 30% gains over a 32B monitor in coding. We further show that TRACE can discover unknown loopholes during training. Overall, TRACE offers a scalable unsupervised approach for oversight where current monitoring methods prove ineffective.

**Abstract (Chinese)**

奖励黑客行为，即推理模型利用奖励函数中的漏洞在不解决预期任务的情况下获得高奖励，这种行为构成了重大威胁。这种行为可能是显性的，即在模型的思维链（CoT）中明确表述，或者隐性的，其中CoT看似无害从而绕过CoT监控器。为了检测隐性奖励黑客行为，我们提出了TRACE（Truncated Reasoning AUC Evaluation，截断推理AUC评估）。我们的关键观察是，当利用漏洞比解决实际任务更容易时，就会发生黑客行为。这意味着模型使用比获得高奖励所需更少的“努力”。TRACE通过测量模型的推理何时变得足以获得奖励来量化努力程度。我们逐步截断模型的CoT至不同长度，强制模型回答，并在每个截断点估计预期奖励。采用捷径的黑客模型只需其CoT的一小部分即可实现高预期奖励，从而产生较大的奖励-长度曲线下面积。在数学推理中，TRACE比我们最强的72B CoT监控器提升超过65%，在编码中比32B监控器提升超过30%。我们进一步展示了TRACE可以在训练过程中发现未知漏洞。总体而言，TRACE提供了一种可扩展的无监督监督方法，在当前监控方法无效的情况下。

---

### Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences

- **Venue**: ICLR 2026 Oral
- **Authors**: Zhuoran Jin, Hongbang Yuan, Kejian Zhu, Jiachun Li, Pengfei Cao, Yubo Chen, Kang Liu, Jun Zhao
- **Keywords**: Omni-Modal Models, Reward Models, Alignment
- **OpenReview**: https://openreview.net/forum?id=9C4gVbPqSy
- **PDF**: https://openreview.net/pdf?id=9C4gVbPqSy

**Abstract**

Reward models (RMs) play a critical role in aligning AI behaviors with human preferences, yet they face two fundamental challenges: (1) Modality Imbalance, where most RMs are mainly focused on text and image modalities, offering limited support for video, audio, and other modalities; and (2) Preference Rigidity, where training on fixed binary preference pairs fails to capture the complexity and diversity of personalized preferences. To address the above challenges, we propose Omni-Reward, a step toward generalist omni-modal reward modeling with support for free-form preferences, consisting of: (1) Evaluation: We introduce Omni-RewardBench, the first omni-modal RM benchmark with free-form preferences, covering nine tasks across five modalities including text, image, video, audio, and 3D; (2) Data: We construct Omni-RewardData, a multimodal preference dataset comprising 248K general preference pairs and 69K instruction-tuning pairs for training generalist omni-modal RMs; (3) Model: We propose Omni-RewardModel, which includes both discriminative and generative RMs, and achieves strong performance on Omni-RewardBench as well as other widely used reward modeling benchmarks.

**Abstract (Chinese)**

奖励模型 (RMs) 在将 AI 行为与人类偏好对齐方面发挥着关键作用，然而它们面临两个根本挑战：(1) 模态不平衡，其中大多数 RMs 主要关注文本和图像模态，对视频、音频和其他模态的支持有限；以及 (2) 偏好刚性，使用固定的二元偏好对进行训练无法捕捉个性化偏好的复杂性和多样性。为了应对上述挑战，我们提出 Omni-Reward，这是一个迈向支持自由形式偏好的通用全模态奖励建模的步骤，包括：(1) 评估：我们引入 Omni-RewardBench，这是第一个具有自由形式偏好的全模态 RM 基准，涵盖五个模态（包括文本、图像、视频、音频和 3D）中的九个任务；(2) 数据：我们构建 Omni-RewardData，这是一个多模态偏好数据集，包含 248K 个通用偏好对和 69K 个指令调优对，用于训练通用全模态 RMs；(3) 模型：我们提出 Omni-RewardModel，它包括判别式和生成式 RMs，并在 Omni-RewardBench 以及其他广泛使用的奖励建模基准上取得了强劲性能。

---

### P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling

- **Venue**: ICLR 2026 Oral
- **Authors**: Pinyi Zhang, Ting-En Lin, Yuchuan Wu, Jingyang Chen, Zongqi Wang, Hua Yang, Xu Ze, Fei Huang, Yongbin Li, Kai Zhang
- **Keywords**: personalizd alignment, generative reward model, test-time user-based scaling
- **OpenReview**: https://openreview.net/forum?id=hXNApWLBZG
- **PDF**: https://openreview.net/pdf?id=hXNApWLBZG

**Abstract**

Personalized alignment of large language models seeks to adapt responses to individual user preferences, typically via reinforcement learning. A key challenge is obtaining accurate, user-specific reward signals in open-ended scenarios. Existing personalized reward models face two persistent limitations: (1) oversimplifying diverse, scenario-specific preferences into a small, fixed set of evaluation principles, and (2) struggling with generalization to new users with limited feedback. To this end, we propose **P-GenRM**, the first **P**ersonalized **Gen**erative **R**eward **M**odel with test-time user-based scaling. P-GenRM transforms preference signals into structured evaluation chains that derive adaptive personas and scoring rubrics across various scenarios. It further clusters users into User Prototypes and introduces a dual-granularity scaling mechanism: at the individual level, it adaptively scales and aggregates each user’s scoring scheme; at the prototype level, it incorporates preferences from similar users. This design mitigates noise in inferred preferences and enhances generalization to unseen users through prototype-based transfer. Empirical results show that  P-GenRM achieves state-of-the-art results on widely-used personalized reward model benchmarks, with an average improvement of ~2.31\%, and demonstrates strong generalization on an out-of-distribution dataset. Notably, Test-time User-based scaling provides an additional ~3\% boost, demonstrating stronger personalized alignment with test-time scalability.

**Abstract (Chinese)**

大语言模型的个性化对齐旨在通过强化学习将响应适应于个体用户偏好。一个关键挑战是在开放式场景中获取准确的用户特定奖励信号。现有的个性化奖励模型面临两个持续存在的局限性：(1) 将多样化的、场景特定的偏好简化为少量固定的评估原则；(2) 在有限反馈的情况下难以泛化到新用户。为此，我们提出**P-GenRM**，这是首个具有测试时基于用户缩放的**P**ersonalized **Gen**erative **R**eward **M**odel。P-GenRM 将偏好信号转化为结构化的评估链，从而在各种场景中推导出自适应人格和评分标准。它进一步将用户聚类为用户原型，并引入双粒度缩放机制：在个体层面，自适应缩放并聚合每个用户的评分方案；在原型层面，融入相似用户的偏好。此设计缓解了推断偏好中的噪声，并通过基于原型的迁移增强了对未见用户的泛化。实证结果显示，P-GenRM 在广泛使用的个性化奖励模型基准上达到了最先进的结果，平均改进约2.31\%，并在分布外数据集上展示了强大的泛化能力。值得注意的是，测试时基于用户缩放提供了额外的约3\%提升，展示了具有测试时可扩展性的更强个性化对齐。

---

### SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety

- **Venue**: ICLR 2026 Oral
- **Authors**: Geon-Hyeong Kim, Yu Jin Kim, Byoungjip Kim, Honglak Lee, Kyunghoon Bae, Youngsoo Jang, Moontae Lee
- **Keywords**: Safety Alignment, LLM Fine-tuning, Preferences, Large Language Models, AI Safety
- **OpenReview**: https://openreview.net/forum?id=PJdw4VBsXD
- **PDF**: https://openreview.net/pdf?id=PJdw4VBsXD

**Abstract**

As Large Language Models (LLMs) are increasingly deployed in real-world applications, balancing helpfulness and safety has become a central challenge. A natural approach is to incorporate safety constraints into Reinforcement Learning from Human Feedback (RLHF), where recent studies have shown promising progress. However, these methods often rely on auxiliary networks or multi-stage pipelines, thereby increasing complexity. In this work, we revisit the original safety alignment objective and show that, under mild assumptions, it admits a closed-form optimal policy. We further derive a provably equivalent and tractable objective, enabling direct optimization. Building on this insight, we propose SafeDPO, a lightweight method that preserves the optimal solution of the underlying safety-constrained objective while requiring only one additional hyperparameter and minimal modifications to existing preference-based training methods. SafeDPO eliminates the need for reward models, cost models, and online sampling, relying only on preference data and safety indicators. Despite its simplicity, SafeDPO achieves competitive safety–helpfulness trade-offs compared to existing safety alignment methods. Experiments on the PKU-SafeRLHF-30K benchmark demonstrate that SafeDPO substantially improves safety while maintaining competitive helpfulness. Ablation studies further show that the additional hyperparameter provides a flexible mechanism to enhance safety while preserving the theoretical optimum, and confirm that SafeDPO scales reliably to LLMs with up to 13B parameters. Overall, our results highlight that a simple, theory-driven objective can provide a lightweight yet effective solution for safety alignment in practice.

**Abstract (Chinese)**

随着大语言模型 (LLMs) 越来越多地部署在实际应用中，平衡帮助性和安全性已成为核心挑战。一种自然的方法是将安全约束纳入人类反馈强化学习 (RLHF) 中，最近的研究显示了有前景的进展。然而，这些方法通常依赖于辅助网络或多阶段管道，从而增加了复杂性。在这项工作中，我们重新审视原始的安全对齐目标，并证明在温和假设下，它承认一个闭式最优策略。我们进一步推导出一个可证明等价且易处理的优化目标，从而实现直接优化。基于这一洞见，我们提出 SafeDPO，一种轻量级方法，它保留了底层安全约束目标的最优解，同时仅需一个额外的超参数和对现有基于偏好的训练方法的微小修改。SafeDPO 消除了对奖励模型、成本模型和在线采样的需求，仅依赖偏好数据和安全指标。尽管其简单性，SafeDPO 在与现有安全对齐方法相比实现了具有竞争力的安全-帮助性权衡。在 PKU-SafeRLHF-30K 基准上的实验表明，SafeDPO 在保持竞争性帮助性的同时显著提升了安全性。消融研究进一步显示，该额外超参数提供了一个灵活机制来增强安全性，同时保留理论最优，并确认 SafeDPO 可可靠地扩展到高达 13B 参数的大语言模型。总体而言，我们的结果突显了一个简单、理论驱动的目标可以为实际中的安全对齐提供轻量级却有效的解决方案。

---

### Semi-Supervised Preference Optimization with Limited Feedback

- **Venue**: ICLR 2026 Oral
- **Authors**: Seonggyun Lee, Sungjun Lim, Seojin Park, Soeun Cheon, Kyungwoo Song
- **Keywords**: Preference Optimization, Semi-Supervised Learning
- **OpenReview**: https://openreview.net/forum?id=ghwxbTx7do
- **PDF**: https://openreview.net/pdf?id=ghwxbTx7do

**Abstract**

The field of preference optimization has made outstanding contributions to the alignment of language models with human preferences. Despite these advancements, recent methods still rely heavily on substantial paired (labeled) feedback data, leading to substantial resource expenditures. To address these challenges, we study the problem of Semi-Supervised Preference Optimization in which the idea is to learn from both a small number of pairwise preference labels and a large pool of unpaired samples simultaneously. Our key theoretical contribution proves the existence of an optimal reward threshold capable of separating winning and losing responses with high probability, which enables a principled pseudo-labeling of unpaired data. By leveraging these pseudo-labels, SSPO effectively distills latent preferences from large-scale unpaired data, thus maintaining human alignment while drastically reducing acquisition costs. Extensive experiments across datasets validate this remarkable data efficiency; for instance, SSPO trained with Mistral-7B-Instruct on just 1% of UltraFeedback consistently surpasses strong baselines trained on 10% of UltraFeedback.

**Abstract (Chinese)**

偏好优化领域为语言模型与人类偏好的对齐做出了杰出贡献。尽管取得了这些进展，最近的方法仍然严重依赖于大量的配对（标注）反馈数据，从而导致大量的资源消耗。为了应对这些挑战，我们研究了半监督偏好优化问题，其核心思想是同时从少量的成对偏好标签和大量非配对样本中学习。我们关键的理论贡献证明了存在一个最优奖励阈值，能够以高概率将获胜响应和失败响应分开，从而实现对非配对数据的原则性伪标注。通过利用这些伪标签，SSPO有效地从大规模非配对数据中提炼潜在偏好，从而在维持人类对齐的同时大幅降低获取成本。在多个数据集上的广泛实验验证了这种卓越的数据效率；例如，使用Mistral-7B-Instruct在仅1%的UltraFeedback上训练的SSPO始终优于在10%的UltraFeedback上训练的强基线。

---

### What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data

- **Venue**: ICLR 2026 Oral
- **Authors**: Rajiv Movva, Smitha Milli, Sewon Min, Emma Pierson
- **Keywords**: rlhf, explaining datasets, interpretability, reward modeling, personalization
- **OpenReview**: https://openreview.net/forum?id=sC6A1bFDUt
- **PDF**: https://openreview.net/pdf?id=sC6A1bFDUt

**Abstract**

Preference data is widely used for aligning language models, but remains largely opaque. While prior work has studied specific aspects of annotator preference (e.g., length or sycophancy), automatically inferring preferences without pre-specifying hypotheses remains challenging. We introduce *What's In My Human Feedback* (WIMHF), a method that produces human-interpretable, natural language features from preference data using sparse autoencoders. We show that a sparse set of interpretable features can account for two-thirds of the preference signal achieved by black-box models. Applying WIMHF to 7 widely-used datasets, we precisely characterize both (1) which preferences are even possible to measure from each dataset and (2) which preferences humans actually display. WIMHF surfaces preferences that are unintentional or even actively harmful, like a preference for toxic outputs in Chatbot Arena. We show how these findings enable *interpretable data curation*: re-labeling the examples that contain the harmful preference yields large safety gains (+37%) with no cost to general performance. We also demonstrate a new approach to *personalization*: on the Community Alignment dataset, we identify preferences that are subjective across annotators, and use the features as interpretable knobs to adjust model behavior along these axes.

**Abstract (Chinese)**

偏好数据被广泛用于对齐语言模型，但仍大体不透明。先前工作研究了标注者偏好的特定方面（如长度或谄媚），但在不预先指定假设的情况下自动推断偏好仍具挑战性。我们引入 *What's In My Human Feedback* (WIMHF)，一种使用稀疏自编码器从偏好数据中产生人类可解释的自然语言特征的方法。我们展示了稀疏的可解释特征集可以解释黑箱模型实现的偏好信号的三分之二。将 WIMHF 应用于 7 个广泛使用的资料集，我们精确表征了 (1) 每个资料集甚至可能测量的偏好，以及 (2) 人类实际显示的偏好。WIMHF 揭示了非故意的甚至积极有害的偏好，例如 Chatbot Arena 中对有毒输出的偏好。我们展示了这些发现如何实现 *可解释的数据策展*：重新标注包含有害偏好的示例，在无一般性能成本的情况下带来显著的安全提升（+37%）。我们还展示了 *个性化* 的新方法：在 Community Alignment 资料集上，我们识别了跨标注者主观的偏好，并使用这些特征作为可解释的旋钮来沿这些轴调整模型行为。

---

### AdvChain: Adversarial Chain-of-Thought Tuning for Robust Safety Alignment of Large Reasoning Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Zihao Zhu, Xinyu Wu, Gehan Hu, Siwei Lyu, Ke Xu, Baoyuan Wu
- **Keywords**: large reasoning model, safety alignment, chain-of-thought
- **OpenReview**: https://openreview.net/forum?id=mIe17L3kWn
- **PDF**: https://openreview.net/pdf?id=mIe17L3kWn

**Abstract**

Large Reasoning Models (LRMs) have demonstrated remarkable capabilities in complex problem-solving through Chain-of-Thought (CoT) reasoning. However, the multi-step nature of CoT introduces new safety challenges that extend beyond conventional language model alignment. We identify a failure mode in current safety CoT tuning methods: the snowball effect, where minor reasoning deviations progressively amplify throughout the thought process, leading to either harmful compliance or excessive refusal. This effect stems from models being trained to imitate perfect reasoning scripts without learning to self-correct. To address this limitation, we propose AdvChain, an alignment paradigm that teaches models dynamic self-correction through adversarial CoT tuning. Our method involves constructing a dataset containing Temptation-Correction and Hesitation-Correction samples, where models learn to recover from harmful reasoning drifts and unnecessary cautions. Extensive experiments show that AdvChain significantly enhances robustness against jailbreak attacks and CoT hijacking while substantially reducing over-refusal on benign prompts, achieving a superior safety-utility balance without compromising reasoning capabilities. Our work establishes a new direction for building more robust and reliable reasoning models.

**Abstract (Chinese)**

大型推理模型 (LRMs) 通过思维链 (CoT) 推理在复杂问题求解中展现出卓越能力。然而，CoT 的多步性质引入了超出传统语言模型对齐的新安全挑战。我们识别出当前安全 CoT 调优方法的一个失效模式：雪球效应，其中细微的推理偏差在整个思考过程中逐步放大，导致有害顺从或过度拒绝。这种效应源于模型被训练以模仿完美的推理脚本，而未学习自我修正。为了解决这一局限性，我们提出 AdvChain，这是一种通过对抗性 CoT 调优教导模型动态自我修正的对齐范式。我们的方法涉及构建一个包含诱惑-修正和犹豫-修正样本的数据集，其中模型学习从有害推理漂移和不必要的谨慎中恢复。广泛实验表明，AdvChain 显著提升了对越狱攻击和思维链劫持的鲁棒性，同时大幅减少了对良性提示的过度拒绝，在不损害推理能力的情况下实现了优越的安全-效用平衡。我们的工作为构建更鲁棒和可靠的推理模型开辟了新方向。

---

### Agentic Reinforced Policy Optimization

- **Venue**: ICLR 2026 Poster
- **Authors**: Guanting Dong, Hangyu Mao, Kai Ma, Licheng Bao, Yifei Chen, Zhongyuan Wang, Zhongxia Chen, Jiazhen Du, Huiyang Wang, Fuzheng Zhang, Guorui Zhou, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou
- **Keywords**: Agentic Reinforcement Learning, Large Language Model, Agentic Reasoning, Tool-use Alignment
- **OpenReview**: https://openreview.net/forum?id=TX4k7BF6aO
- **PDF**: https://openreview.net/pdf?id=TX4k7BF6aO

**Abstract**

Large-scale reinforcement learning with verifiable rewards (RLVR) has proven effective in harnessing the potential of large language models (LLMs) for single-turn reasoning tasks. In realistic reasoning scenarios, LLMs often rely on external tools to assist in task-solving processes. However, current RL algorithms typically employ trajectory-level rollout sampling, consistently neglecting the fine-grained exploration of multi-turn tool-call steps. To bridge this gap, we propose Agentic Reinforced Policy Optimization (ARPO), a novel agentic RL algorithm tailored for training multi-turn LLM-based agents. Our preliminary experiments reveal that LLMs frequently exhibit increased uncertainty after tool-call steps, as evidenced by higher entropy in the distribution of generated tokens. Motivated by this, ARPO incorporates an entropy-based adaptive rollout mechanism, encouraging the policy model to adaptively branch sampling during high-entropy tool-call rounds, thereby promoting step-level exploration of latent tool-use behaviors. By integrating an advantage attribution estimation, ARPO enables LLMs to internalize advantage differences in stepwise tool-use interactions. Experiments across 13 challenging benchmarks demonstrate ARPO's superiority over trajectory-level RL algorithms. Remarkably, ARPO achieves improved performance using only half of the tool-use budget required by existing methods, offering a scalable solution for aligning LLM-based agents with real-time dynamic environments. Our codes are released at https://github.com/RUC-NLPIR/ARPO.

**Abstract (Chinese)**

大规模可验证奖励强化学习（RLVR）已证明在利用大语言模型（LLMs）处理单轮推理任务方面的潜力方面非常有效。在现实推理场景中，大语言模型通常依赖外部工具来辅助任务求解过程。然而，现有的强化学习算法通常采用轨迹级展开采样，持续忽略多轮工具调用步骤的细粒度探索。为弥合这一差距，我们提出代理式强化策略优化（ARPO），一种新型代理式强化学习算法，专为训练多轮大语言模型代理而设计。我们的初步实验揭示，大语言模型在工具调用步骤后经常表现出更高的不确定性，这体现在生成令牌分布的更高熵值上。受此启发，ARPO 集成了基于熵的自适应展开机制，鼓励策略模型在高熵工具调用轮次中自适应分支采样，从而促进潜在工具使用行为的步骤级探索。通过集成优势归因估计，ARPO 使大语言模型能够内化逐步工具使用交互中的优势差异。跨越 13 个具有挑战性的基准测试的实验证明了 ARPO 相对于轨迹级强化学习算法的优越性。值得注意的是，ARPO 仅使用现有方法所需工具使用预算的一半即可实现改进性能，为将大语言模型代理与实时动态环境对齐提供了可扩展解决方案。我们的代码已开源于 https://github.com/RUC-NLPIR/ARPO。

---

### Align Once, Benefit Multilingually: Enforcing Multilingual Consistency for LLM Safety Alignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Yuyan Bu, Xiaohao Liu, ZhaoXing Ren, Yaodong Yang, Juntao Dai
- **Keywords**: Multilingual Enhancement, Large Language Models
- **OpenReview**: https://openreview.net/forum?id=ueknOG1wXL
- **PDF**: https://openreview.net/pdf?id=ueknOG1wXL

**Abstract**

The widespread deployment of large language models (LLMs) across linguistic communities necessitates reliable multilingual safety alignment. However, recent efforts to extend alignment to other languages often require substantial resources, either through large-scale, high-quality supervision in the target language or through pairwise alignment with high-resource languages, which limits scalability.
In this work, we propose a resource-efficient method for improving multilingual safety alignment. 
We introduce a plug-and-play Multi-Lingual Consistency (MLC) loss that can be integrated into existing monolingual alignment pipelines. 
By improving collinearity between multilingual representation vectors, our method encourages directional consistency at the multilingual semantic level in a single update. This allows simultaneous alignment across multiple languages using only multilingual prompt variants without requiring additional response-level supervision in low-resource languages. We validate the proposed method across different model architectures and alignment paradigms, and demonstrate its effectiveness in enhancing multilingual safety with limited impact on general model utility. Further evaluation across languages and tasks indicates improved cross-lingual generalization, suggesting the proposed approach as a practical solution for multilingual consistency alignment under limited supervision.

**Abstract (Chinese)**

大型语言模型 (LLMs) 在各语言社区的广泛部署需要可靠的多语言安全对齐。然而，最近将对齐扩展到其他语言的努力往往需要大量资源，要么通过目标语言的大规模高质量监督，要么通过与高资源语言的成对对齐，这限制了可扩展性。

在本工作中，我们提出了一种资源高效的方法来改进多语言安全对齐。

我们引入了一种即插即用的多语言一致性 (MLC) 损失，该损失可集成到现有的单语言对齐流程中。

通过提升多语言表示向量之间的共线性，我们的方法在单次更新中鼓励多语言语义层面的方向一致性。这允许仅使用多语言提示变体即可同时对多个语言进行对齐，而无需在低资源语言中提供额外的响应级监督。我们在不同模型架构和对齐范式中验证了所提方法，并展示了其在提升多语言安全方面的有效性，同时对通用模型效用影响有限。跨语言和任务的进一步评估表明了改进的跨语言泛化性能，表明所提方法是有限监督下多语言一致性对齐的实用解决方案。

---

### Aligner, Diagnose Thyself: A Meta-Learning Paradigm for Fusing Intrinsic Feedback in Preference Alignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Mengyang Li, Pinlong Zhao, Zhong Zhang
- **Keywords**: Large Language Models, Direct Preference Optimization
- **OpenReview**: https://openreview.net/forum?id=oIAUP1K5Dq
- **PDF**: https://openreview.net/pdf?id=oIAUP1K5Dq

**Abstract**

The alignment of Large Language Models (LLMs) with human preferences is critically undermined by noisy labels in training datasets.
Existing robust methods often prove insufficient, as they rely on single, narrow heuristics such as perplexity or loss, failing to address the diverse nature of real-world noise.
We challenge this limited-scope approach by introducing a new paradigm where models learn to diagnose thyself, systematically fusing multiple streams of intrinsic feedback for a holistic reliability assessment of each preference pair.
We instantiate this paradigm through a meta-learning methodology that learns to adaptively reweight samples based on a rich diagnostic vector.
This vector captures three complementary perspectives: preference consistency, learning difficulty, and generation confidence.
Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art methods across various noise conditions.
Crucially, our work provides the first quantitative analysis of these intrinsic diagnostics, revealing that their fusion is essential for overcoming the blind spots inherent in any single heuristic.
This diagnostic-driven paradigm offers a principled path towards developing more robust and trustworthy LLMs.

**Abstract (Chinese)**

大型语言模型 (LLMs) 与人类偏好的对齐被训练数据集中的噪声标签严重削弱。现有的鲁棒方法往往证明不足，因为它们依赖于单一、狭隘的启发式方法，如困惑度或损失，无法应对真实世界噪声的多样性。我们通过引入一种新范式来挑战这种有限范围的方法，在该范式中，模型学会自我诊断，系统地融合多股内在反馈，对每个偏好对进行整体可靠性评估。我们通过一种元学习方法来实例化这一范式，该方法学习基于丰富的诊断向量自适应地重新加权样本。该向量捕捉了三个互补视角：偏好一致性、学习难度和生成置信度。大量实验表明，我们的方法在各种噪声条件下显著优于最先进的方法。至关重要的是，我们的工作提供了这些内在诊断的首次定量分析，揭示了它们的融合对于克服任何单一启发式固有的盲点是必不可少的。这种诊断驱动的范式为开发更鲁棒和可信的大型语言模型提供了原则性路径。

---

### Aligning Deep Implicit Preferences by Learning to Reason Defensively

- **Venue**: ICLR 2026 Poster
- **Authors**: Peiming Li, Zhiyuan Hu, Shiyu Li, Xi Chen, Yang Tang
- **Keywords**: Preference Alignment, Reward Modeling as Reasoning, Process Supervision
- **OpenReview**: https://openreview.net/forum?id=ZA7i5Otjqd
- **PDF**: https://openreview.net/pdf?id=ZA7i5Otjqd

**Abstract**

Personalized alignment is crucial for enabling Large Language Models (LLMs) to engage effectively in user-centric interactions. However, current methods face a dual challenge: they fail to infer users' deep implicit preferences (including unstated goals, semantic context and risk tolerances), and they lack the defensive reasoning required to navigate real-world ambiguity. This cognitive gap leads to responses that are superficial, brittle and short-sighted. To address this, we propose Critique-Driven Reasoning Alignment (CDRA), which reframes alignment from a scalar reward-matching task into a structured reasoning process. First, to bridge the preference inference gap, we introduce the DeepPref benchmark. This dataset, comprising 3000 preference-query pairs across 20 topics, is curated by simulating a multi-faceted cognitive council that produces critique-annotated reasoning chains to deconstruct query semantics and reveal latent risks. Second, to instill defensive reasoning, we introduce the Personalized Generative Process Reward Model (Pers-GenPRM), which frames reward modeling as a personalized reasoning task. It generates a critique chain to evaluate a response's alignment with user preferences before outputting a final score based on this rationale. Ultimately, this interpretable, structured reward signal guides policy model through Critique-Driven Policy Alignment, a process-level online reinforcement learning algorithm integrating both numerical and natural language feedback. Experiments demonstrate that CDRA excels at discovering and aligning with users' true preferences while executing robust reasoning. Our dataset is available at \url{https://DeepPref.github.io/}.

**Abstract (Chinese)**

个性化对齐对于使大型语言模型（LLMs）能够有效参与以用户为中心的交互至关重要。然而，现有的方法面临双重挑战：它们无法推断用户的深层隐式偏好（包括未陈述的目标、语义上下文和风险容忍度），并且缺乏应对现实世界模糊性所需的防御性推理。这种认知差距导致响应浅显、脆弱且短视。为解决这一问题，我们提出批判驱动推理对齐（CDRA），它将对齐从标量奖励匹配任务重新框架为结构化推理过程。首先，为了弥合偏好推断差距，我们引入DeepPref基准。该数据集包含跨越20个主题的3000个偏好-查询对，通过模拟多方面认知委员会来 curation，该委员会生成带有批判注释的推理链，以解构查询语义并揭示潜在风险。其次，为了灌输防御性推理，我们引入个性化生成过程奖励模型（Pers-GenPRM），它将奖励建模框架为个性化推理任务。它生成一个批判链来评估响应与用户偏好的对齐，然后基于此推理输出最终分数。最终，这种可解释的结构化奖励信号通过批判驱动策略对齐引导策略模型，这是一种过程级在线强化学习算法，整合了数值和自然语言反馈。实验表明，CDRA在发现并对齐用户的真实偏好同时执行鲁棒推理方面表现出色。我们的数据集可在\url{https://DeepPref.github.io/}获取。

---

### Alignment through Meta-Weighted Online Sampling: Bridging the Gap between Data Generation and Preference Optimization

- **Venue**: ICLR 2026 Poster
- **Authors**: Junming Yang, Ning Xu, Biao Liu, Shiqi Qiao, Xin Geng
- **Keywords**: Large Language Model Alignment, Direct Preference Optimization
- **OpenReview**: https://openreview.net/forum?id=8OD1ymZxY9
- **PDF**: https://openreview.net/pdf?id=8OD1ymZxY9

**Abstract**

Preference optimization is crucial for aligning large language models (LLMs) with human values and intentions. A significant challenge in this process is the distribution mismatch between pre-collected offline preference data and the evolving model policy. Existing methods attempt to reduce this gap using static heuristics or decoupled online sampling strategies, but they often fail to adapt to the model's dynamic learning state. To bridge this gap, we propose Meta-Weighted Adaptive Preference Optimization (MetaAPO), a novel framework that dynamically couples data generation with model training. MetaAPO employs a lightweight meta-learner, as an "alignment gap estimator", to evaluate the potential benefits of on-policy sampling in relation to offline data. This guides targeted online generation and assigns sample-wise meta-weights to the optimization objective, dynamically balancing the quality and distribution of online and offline data. Experiments on AlpacaEval 2, Arena-Hard and MT-Bench demonstrate that MetaAPO consistently outperforms existing preference optimization approaches across various settings, while reducing 42% in online annotation costs.

**Abstract (Chinese)**

偏好优化对于将大型语言模型 (LLMs) 与人类价值观和意图对齐至关重要。这一过程中的一个重大挑战是预收集的离线偏好数据与不断演化的模型策略之间的分布不匹配。现有的方法试图使用静态启发式或解耦的在线采样策略来缩小这一差距，但它们往往无法适应模型的动态学习状态。为了弥合这一差距，我们提出了元加权自适应偏好优化 (MetaAPO)，这是一个新型框架，它动态地将数据生成与模型训练耦合在一起。MetaAPO 采用一个轻量级元学习器，作为“对齐差距估计器”，来评估按策略采样相对于离线数据的潜在益处。这指导了针对性的在线生成，并为优化目标分配样本级元权重，动态平衡在线和离线数据的质量和分布。在 AlpacaEval 2、Arena-Hard 和 MT-Bench 上的实验表明，MetaAPO 在各种设置下始终优于现有的偏好优化方法，同时将在线标注成本降低了 42%。

---

### Alignment-Weighted DPO:  A principled reasoning approach to improve alignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Mengxuan Hu, Vivek Datla, Anoop Kumar, Zihan Guan, Sheng Li, Alfy Samuel, Daben Liu
- **Keywords**: Reasoning, LLM alignment, DPO
- **OpenReview**: https://openreview.net/forum?id=OuMNJoKJBQ
- **PDF**: https://openreview.net/pdf?id=OuMNJoKJBQ

**Abstract**

Recent advances in alignment techniques such as Supervised Fine-Tuning (SFT), Reinforcement Learning from Human Feedback (RLHF), and Direct Preference Optimization (DPO) have improved the safety of large language models (LLMs). However, these LLMs remain vulnerable to jailbreak attacks that disguise harmful intent through indirect or deceptive phrasing. Using causal intervention, we empirically demonstrate that this vulnerability stems from shallow alignment mechanisms that lack deep reasoning, often rejecting harmful prompts without truly understanding why they are harmful. To mitigate this vulnerability, we propose enhancing alignment through reasoning-aware post-training. We construct and release a novel Chain-of-Thought (CoT) fine-tuning dataset that includes both utility-oriented and safety-critical prompts with step-by-step rationales. Fine-tuning on this dataset encourages models to produce principled refusals grounded in reasoning, outperforming standard SFT baselines. Furthermore, inspired by failure patterns in CoT fine-tuning, we introduce **Alignment-Weighted DPO**, which targets the most problematic parts of an output by assigning different preference weights to the reasoning and final-answer segments. This produces finer-grained, targeted updates than vanilla DPO and improves robustness to diverse jailbreak strategies. Extensive experiments across multiple safety and utility benchmarks show that our method consistently improves alignment robustness while maintaining overall model utility.

**Abstract (Chinese)**

最近的对齐技术进展，如监督微调 (SFT)、人类反馈强化学习 (RLHF) 和直接偏好优化 (DPO)，提升了大语言模型 (LLMs) 的安全性。然而，这些 LLMs 仍然容易受到越狱攻击的影响，这些攻击通过间接或欺骗性表述来掩饰有害意图。使用因果干预，我们通过实证证明，这种漏洞源于缺乏深度推理的浅层对齐机制，这些机制往往在不真正理解有害提示为何有害的情况下拒绝它们。为了缓解这一漏洞，我们提出通过推理感知的后训练来增强对齐。我们构建并发布了新型思维链 (CoT) 微调数据集，该数据集包含面向效用和安全关键的提示，并附带逐步推理依据。在该数据集上进行微调鼓励模型生成基于推理的原则性拒绝，优于标准 SFT 基线。此外，受 CoT 微调中失败模式的启发，我们引入了**对齐加权 DPO**，它通过为推理和最终答案段分配不同的偏好权重来针对输出中最具问题性的部分。这比 vanilla DPO 产生了更细粒度、更有针对性的更新，并提升了对多样化越狱策略的鲁棒性。在多个安全和效用基准上的广泛实验表明，我们的方法在保持整体模型效用的同时，一贯提升了对齐鲁棒性。

---

### AlphaAlign: Incentivizing Safety Alignment with Extremely Simplified Reinforcement Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Yi Zhang, An Zhang, XiuYu Zhang, Leheng Sheng, Yuxin Chen, Zhenkai Liang, Xiang Wang
- **Keywords**: Safety Alignment, Reasoning, Reinfocement Learning with Verifiable Reward
- **OpenReview**: https://openreview.net/forum?id=2XNb1JUKW3
- **PDF**: https://openreview.net/pdf?id=2XNb1JUKW3

**Abstract**

Large language models (LLMs), despite possessing latent safety understanding from their vast pretraining data, remain vulnerable to generating harmful content and exhibit issues such as over-refusal and utility degradation after safety alignment. Current safety alignment methods often result in superficial refusal shortcuts or rely on intensive supervision for reasoning-based approaches, failing to fully leverage the model's intrinsic safety self-awareness. We propose \textbf{AlphaAlign}, a simple yet effective pure reinforcement learning (RL) framework with verifiable safety reward designed to incentivize this latent safety awareness through proactive safety reasoning. AlphaAlign employs a dual-reward system: a verifiable safety reward encourages correctly formatted and explicitly justified refusals for harmful queries while penalizing over-refusals, and a normalized helpfulness reward guides high-quality responses to benign inputs. This allows the model to develop proactive safety reasoning capabilities without depending on supervised safety-specific reasoning data. AlphaAlign demonstrates three key advantages: (1) Simplicity and efficiency, requiring only binary prompt safety labels and minimal RL steps for substantial improvements. (2) Breaking the safety-utility trade-off, by enhancing refusal of harmful content and reducing over-refusals, while simultaneously maintaining or even improving general task performance and robustness to unseen jailbreaks. (3) Deep alignment, fostering proactive safety reasoning that generates explicit safety rationales rather than relying on shallow refusal patterns. Our codes are available at \url{https://anonymous.4open.science/r/AlphaAlign-D5B0}

**Abstract (Chinese)**

尽管大语言模型 (LLMs) 从其海量预训练数据中具备潜在的安全理解，但仍易于生成有害内容，并在安全对齐后表现出过度拒绝和效用退化等问题。当前的安全对齐方法往往导致表面的拒绝捷径，或依赖密集监督来实现基于推理的方法，从而未能充分利用模型的内在安全自我意识。我们提出 **AlphaAlign**，这是一个简单而有效的纯强化学习 (RL) 框架，配备可验证的安全奖励，旨在通过主动安全推理来激励这种潜在的安全意识。AlphaAlign 采用双奖励系统：可验证的安全奖励鼓励针对有害查询生成正确格式且明确论证的拒绝，同时惩罚过度拒绝；标准化帮助性奖励则指导对无害输入生成高质量响应。这使得模型能够在不依赖监督的安全特定推理数据的情况下发展主动安全推理能力。AlphaAlign 展示了三个关键优势：(1) 简单性和高效性，仅需二元提示安全标签和少量 RL 步骤即可实现显著改进。(2) 打破安全-效用权衡，通过增强对有害内容的拒绝并减少过度拒绝，同时维持甚至提升通用任务性能以及对未见越狱攻击的鲁棒性。(3) 深度对齐，促进主动安全推理以生成明确的安全理由，而非依赖浅层拒绝模式。我们的代码可在 \url{https://anonymous.4open.science/r/AlphaAlign-D5B0} 获取

---

### BIRD: Behavior Induction via Representation-structure Distillation

- **Venue**: ICLR 2026 Poster
- **Authors**: Galen Pogoncheff, Michael Beyeler
- **Keywords**: Knowledge Distillation, AI Alignment, Weak-to-strong generalization
- **OpenReview**: https://openreview.net/forum?id=jbJGhHpwmJ
- **PDF**: https://openreview.net/pdf?id=jbJGhHpwmJ

**Abstract**

Human-aligned deep learning models exhibit behaviors consistent with human values, such as robustness, safety, and fairness.  Transferring these behavioral properties to models trained on different tasks or data distributions remains challenging: aligned behavior is easily forgotten during fine-tuning, and collecting task-specific data that preserves this behavior can be prohibitively costly.  We introduce BIRD, a flexible framework for transferring aligned behavior by matching the internal representation structure of a student model to that of a teacher.  Applied to out-of-distribution robustness in image classification, BIRD outperforms fine-tuning, transfer learning, and continual learning methods, improving robust accuracy by up to 18\% over the next strongest baseline. It remains effective even when the teacher is trained on a much simpler dataset and is $25\times$ smaller in parameter count than the student.  In a large-scale study of over 400 teacher-student pairs, we show that three interpretable and computable properties of the teacher's representations explain up to 85\% of the variance in transfer success, offering practical guidance for teacher selection and design.  We further show that BIRD generalizes beyond applications in vision by enhancing safety alignment in language models when paired with Direct Preference Optimization and improving weak-to-strong generalization when combined with soft-label distillation.  BIRD turns small, well-aligned models into scalable alignment seeds, mitigating challenges from key bottlenecks in deploying safe AI systems.

**Abstract (Chinese)**

与人类价值观对齐的深度学习模型表现出与人类价值观一致的行为，例如鲁棒性、安全性和公平性。将这些行为属性转移到在不同任务或数据分布上训练的模型仍然具有挑战性：对齐行为在微调过程中容易被遗忘，而收集保留这种行为的特定任务数据可能成本过高。我们引入了BIRD，这是一个灵活的框架，通过将学生模型的内部表示结构与教师模型匹配来转移对齐行为。在图像分类的分布外鲁棒性应用中，BIRD优于微调、迁移学习和持续学习方法，在鲁棒准确率上比下一个最强基线提高了高达18\%。即使教师在更简单的数据集上训练，并且参数量比学生小$25\times$，BIRD仍然有效。在一项超过400个教师-学生对的大规模研究中，我们展示了教师表示的三个可解释且可计算属性解释了转移成功方差高达85\%，为教师选择和设计提供了实用指导。我们进一步展示了BIRD在视觉应用之外的泛化能力：与直接偏好优化结合时增强了语言模型的安全性对齐，与软标签蒸馏结合时改善了弱到强泛化。BIRD将小型、良好对齐的模型转变为可扩展的对齐种子，缓解了部署安全AI系统中的关键瓶颈挑战。

---

### Beyond Binary Preferences: A Principled Framework for Reward Modeling with Ordinal Feedback

- **Venue**: ICLR 2026 Poster
- **Authors**: Amirhossein Afsharrad, Ruida Zhou, Luca Viano, Sanjay Lall, Mohammad Ghavamzadeh
- **Keywords**: reward modeling, ordinal regression, Likert scale, preference learning, human feedback, RLHF, discrete ordinal regression, Bradley-Terry model, ordinal preferences, large language models, alignment, preference data
- **OpenReview**: https://openreview.net/forum?id=mteZOi0xyu
- **PDF**: https://openreview.net/pdf?id=mteZOi0xyu

**Abstract**

Reward modeling is crucial for aligning large language models with human preferences, yet current approaches lack a principled mathematical framework for leveraging ordinal preference data. When human annotators provide graded preferences on a Likert scale (e.g., significantly better, better, slightly better, negligibly better), existing methods typically apply ad-hoc heuristics, such as margin terms or scaling factors, to loss functions derived from binary preference models like Bradley-Terry. These approaches lack an underlying mathematical model for how ordinal preference data is generated. We present a theoretically grounded framework that formulates reward modeling with Likert scale preferences as a discrete ordinal regression problem. We derive two loss functions from this formulation: a negative log-likelihood loss and an all-threshold loss, both of which learn threshold parameters that naturally capture the ordinal structure of preferences. Unlike existing heuristic methods that manually specify fixed margins or scaling weights, our approach learns these parameters directly from data within a coherent probabilistic framework. Experimental results on multiple benchmarks demonstrate that our ordinal regression approach consistently achieves competitive or superior performance compared to existing heuristic methods across diverse evaluation categories including chat, reasoning, and safety tasks. Our work provides the first principled mathematical framework for incorporating Likert scale preferences into reward model training, moving beyond ad-hoc modifications of binary preference models to enable more effective utilization of fine-grained human feedback.

**Abstract (Chinese)**

奖励建模对于将大型语言模型与人类偏好对齐至关重要，然而当前方法缺乏利用序数偏好数据的原则性数学框架。当人类标注者提供李克特量表上的分级偏好（例如，显著更好、更好、略好、微不足道地更好）时，现有的方法通常将临时启发式方法（如边际项或缩放因子）应用于从二元偏好模型（如Bradley-Terry）导出的损失函数。这些方法缺乏序数偏好数据生成方式的底层数学模型。我们提出一个理论基础坚实的框架，将李克特量表偏好的奖励建模表述为离散序数回归问题。我们从这一表述中推导出两种损失函数：负对数似然损失和全阈值损失，这两种损失都学习阈值参数，自然捕捉偏好的序数结构。与现有手动指定固定边际或缩放权重的启发式方法不同，我们的方法在连贯的概率框架内直接从数据中学习这些参数。多项基准上的实验结果表明，我们的序数回归方法在聊天、推理和安全任务等多样化评估类别中，与现有启发式方法相比，始终实现竞争性或优越性能。我们的工作提供了第一个将李克特量表偏好纳入奖励模型训练的原则性数学框架，超越了二元偏好模型的临时修改，从而实现更有效的细粒度人类反馈利用。

---

### Beyond Pairwise: Empowering LLM Alignment With (Ranked) Choice Modeling

- **Venue**: ICLR 2026 Poster
- **Authors**: Yuxuan Tang, Yifan Feng
- **Keywords**: Language Models Fine-tuning, Discrete Choice Model, Ranked Choice Model, Alignment, Preference Optimization, Learning From Human Feedback
- **OpenReview**: https://openreview.net/forum?id=fCaxd9EKzl
- **PDF**: https://openreview.net/pdf?id=fCaxd9EKzl

**Abstract**

Alignment of large language models (LLMs) has predominantly relied on pairwise preference optimization, where annotators select the better of two responses to a prompt. While simple, this approach overlooks the opportunity to learn from richer forms of human feedback, such as multiway comparisons and top-$k$ rankings. We introduce \textit{Ranked Choice Preference Optimization} (RCPO), a unified framework that bridges preference optimization with (ranked) choice modeling via maximum likelihood estimation. RCPO supports both utility-based and rank-based models, subsumes several pairwise methods (such as DPO and SimPO) as special cases, and provides principled training objectives for richer feedback formats. We instantiate this framework with two representative models (Multinomial Logit and Mallows-RMJ). Experiments on Llama-3-8B-Instruct, Gemma-2-9B-it, and Mistral-7B-Instruct across in-distribution and out-of-distribution settings show that RCPO consistently outperforms competitive baselines. RCPO shows that directly leveraging ranked preference data, combined with the right choice models, yields more effective alignment. It offers an extensible foundation for incorporating (ranked) choice modeling into LLM training.

**Abstract (Chinese)**

大型语言模型（LLMs）的对齐主要依赖于成对偏好优化，其中标注者从针对提示的两个响应中选择更好的一个。虽然简单，这种方法忽略了从更丰富的反馈形式中学习的机会，例如多路比较和 top-$k$ 排名。我们引入了\textit{排名选择偏好优化}（RCPO），这是一个统一的框架，通过最大似然估计将偏好优化与（排名）选择建模桥接起来。RCPO 支持基于效用和基于排名的模型，将几种成对方法（如 DPO 和 SimPO）作为特例包含在内，并为更丰富的反馈格式提供原则性的训练目标。我们使用两个代表性模型（多项 logit 和 Mallows-RMJ）来实例化该框架。在 Llama-3-8B-Instruct、Gemma-2-9B-it 和 Mistral-7B-Instruct 上进行的分布内和分布外设置实验显示，RCPO 始终优于竞争性基线。RCPO 表明，直接利用排名偏好数据并结合合适的选取模型，可以产生更有效的对齐。它为将（排名）选择建模纳入 LLM 训练提供了可扩展的基础。

---

### Beyond RLHF and NLHF: Population-Proportional Alignment under an Axiomatic Framework

- **Venue**: ICLR 2026 Poster
- **Authors**: Kihyun Kim, Jiawei Zhang, Asuman E. Ozdaglar, Pablo A. Parrilo
- **Keywords**: AI Alignment, Population-Proportional Alignment, Social Choice Theory, Axiomatic Framework, Rank Aggregation, Pluralistic Alignment, Preference-based Reinforcement Learning, Reinforcement Learning from Human Feedback, Nash Learning from Human Feedback, Large Language Model
- **OpenReview**: https://openreview.net/forum?id=Egmvi2RWnj
- **PDF**: https://openreview.net/pdf?id=Egmvi2RWnj

**Abstract**

Conventional preference learning methods often prioritize opinions held more widely when aggregating preferences from multiple evaluators. This may result in policies that are biased in favor of some types of opinions or groups and susceptible to strategic manipulation. To address this issue, we develop a novel preference learning framework capable of aligning aggregate opinions and policies proportionally with the true population distribution of evaluator preferences. Grounded in social choice theory, our approach infers the feasible set of evaluator population distributions directly from pairwise comparison data. Using these estimates, the algorithm constructs a policy that satisfies foundational axioms from social choice theory, namely monotonicity and Pareto efficiency, as well as our newly-introduced axioms of population-proportional alignment and population-bounded manipulability. Moreover, we propose a soft-max relaxation method that smoothly trades off population-proportional alignment with the selection of the Condorcet winner (which beats all other options in pairwise comparisons). Finally, we validate the effectiveness and scalability of our approach through experiments on both tabular recommendation tasks and large language model alignment.

**Abstract (Chinese)**

传统的偏好学习方法在从多个评估者聚合偏好时，往往优先考虑持有更广泛意见的观点。这可能导致策略偏向某些类型的意见或群体，并易受战略操纵的影响。为了解决这一问题，我们开发了一种新型偏好学习框架，能够使聚合意见和策略与评估者偏好的真实人口分布成比例对齐。该方法基于社会选择理论，直接从成对比较数据中推断评估者人口分布的可行集。利用这些估计，该算法构建了一个满足社会选择理论基础公理——即单调性和帕累托效率——以及我们新引入的人口比例对齐和人口界限可操纵性公理的策略。此外，我们提出了一种软最大松弛方法，能够平滑地在人口比例对齐与选择孔多塞胜者（在成对比较中击败所有其他选项）之间进行权衡。最后，我们通过表格推荐任务和大语言模型对齐的实验验证了我们方法的有效性和可扩展性。

---

### Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning

- **Venue**: ICLR 2026 Poster
- **Authors**: Xu Wan, Yansheng Wang, Wenqi Huang, Mingyang Sun
- **Keywords**: LLM post-training; off-policy RLVR
- **OpenReview**: https://openreview.net/forum?id=RduOiisl1S
- **PDF**: https://openreview.net/pdf?id=RduOiisl1S

**Abstract**

Traditional on-policy Reinforcement Learning with Verifiable Rewards (RLVR) frameworks suffer from experience waste and reward homogeneity, which directly hinders learning efficiency on difficult samples during large language models post-training. In this paper, we introduce Batch Adaptation Policy Optimization (BAPO), an off-policy RLVR framework to improve the data efficiency in large language models post-training. It dynamically selects training batches by re-evaluating historically difficult samples and reusing high-quality ones, while holding a lower bound guarantee for policy improvement. Extensive experiments further demonstrate that BAPO achieves an average 12.5\% improvement over GRPO across mathematics, planning, and visual reasoning tasks. Crucially, BAPO successfully resolves 40.7\% of problems that base models consistently fail to solve.

**Abstract (Chinese)**

传统的在线策略可验证奖励强化学习（RLVR）框架存在经验浪费和奖励同质化问题，这直接阻碍了大语言模型后训练过程中对困难样本的学习效率。在本文中，我们引入了批适应策略优化（BAPO），一种离策略RLVR框架，用于提升大语言模型后训练的数据效率。它通过重新评估历史困难样本并重用高质量样本来动态选择训练批次，同时为策略改进提供下界保证。大量实验进一步表明，BAPO在数学、规划和视觉推理任务上比GRPO平均提升12.5%。至关重要的是，BAPO成功解决了基础模型持续失败的40.7%的问题。

---

### COMAL: A Convergent Meta-Algorithm for Aligning LLMs with General Preferences

- **Venue**: ICLR 2026 Poster
- **Authors**: Yixin Liu, Argyris Oikonomou, Weiqiang Zheng, Yang Cai, Arman Cohan
- **Keywords**: LLM alignment, general preference, Nash learning from human feedback, last-iterate convergence
- **OpenReview**: https://openreview.net/forum?id=OsrE5DJ9Fu
- **PDF**: https://openreview.net/pdf?id=OsrE5DJ9Fu

**Abstract**

Many alignment methods, including reinforcement learning from human feedback (RLHF), rely on the Bradley-Terry reward assumption, which is not always sufficient to capture the full range and complexity of general human preferences. We explore RLHF under a general preference framework by modeling the alignment problem as a two-player zero-sum game in a game-theoretic framework, where the Nash equilibrium policy guarantees a 50\% win rate against any competing policy.   However, previous self-play algorithms for finding the Nash policy either diverge or only converge to a Nash policy in a modified game, even in a simple synthetic setting, thereby failing to maintain the 50\% win rate guarantee against all other policies. We propose a meta-algorithm, **Co**nvergent **M**eta **Al**ignment Algorithm (COMAL), for language model alignment with general preferences, inspired by convergent algorithms in game theory. We provide theoretical analysis that our meta-algorithm converges to an exact Nash policy in the last iterate and demonstrate its effectiveness on a range of synthetic and preference optimization datasets. COMAL is simple and can be integrated with many existing methods designed for preference optimization with minimal changes, and empirically it consistently maintains above 60.2\% and 56.8\% win rates, when applied to Llama-3-8B-Instruct and Qwen2.5-7B, against all compared algorithms under controlled evaluations.

**Abstract (Chinese)**

许多对齐方法，包括人类反馈强化学习（RLHF），依赖于 Bradley-Terry 奖励假设，该假设并不总是足以捕捉一般人类偏好的全范围和复杂性。我们在一般偏好框架下探索 RLHF，通过将对齐问题建模为博弈论框架中的两人零和博弈，其中 Nash 均衡策略保证了对任何竞争策略的 50% 胜率。然而，先前的用于寻找 Nash 策略的自对弈算法要么发散，要么仅在修改后的游戏中收敛到 Nash 策略，即使在简单的合成设置中，从而无法维持对所有其他策略的 50% 胜率保证。我们提出了一种元算法，收敛元对齐算法（COMAL），用于具有一般偏好的语言模型对齐，受博弈论中收敛算法的启发。我们提供了理论分析，证明我们的元算法在最后迭代中收敛到精确的 Nash 策略，并在各种合成和偏好优化数据集上展示了其有效性。COMAL 简单且可以与许多现有的偏好优化方法以最小改动集成，并且在经验上，当应用于 Llama-3-8B-Instruct 和 Qwen2.5-7B 时，在受控评估中一致维持高于 60.2% 和 56.8% 的胜率，优于所有比较算法。

---

### Cognitive models can reveal interpretable value trade-offs in language models

- **Venue**: ICLR 2026 Poster
- **Authors**: Sonia Krishna Murthy, Rosie Zhao, Jennifer Hu, Sham M. Kakade, Markus Wulfmeier, Peng Qian, Tomer Ullman
- **Keywords**: cognitive modeling, value tradeoffs, RLHF training dynamics
- **OpenReview**: https://openreview.net/forum?id=nM2QhvybwI
- **PDF**: https://openreview.net/pdf?id=nM2QhvybwI

**Abstract**

Value trade-offs are an integral part of human decision-making and language use, however, current tools for interpreting such dynamic and multi-faceted notions of values in language models are limited. In cognitive science, so-called "cognitive models" provide formal accounts of such trade-offs in humans, by modeling the weighting of a speaker's competing utility functions in choosing an action or utterance. Here, we show that a leading cognitive model of polite speech can be used to systematically evaluate alignment-relevant trade-offs in language models via two encompassing settings: degrees of reasoning "effort" and system prompt manipulations in closed-source frontier models, and RL post-training dynamics of open-source models. Our results show that LLMs' behavioral profiles under the cognitive model a) shift predictably when they are prompted to prioritize certain goals, b) are amplified by a small reasoning budget, and c) can be used to diagnose other social behaviors such as sycophancy. Our findings from LLMs' post-training dynamics reveal large shifts in values early on in training and persistent effects of the choice of base model and pretraining data, compared to feedback dataset or alignment method. Our framework offers a flexible tool for probing behavioral profiles across diverse model types and gaining insights for shaping training regimes that better control trade-offs between values during model development.

**Abstract (Chinese)**

价值权衡是人类决策和语言使用中不可或缺的一部分，然而，目前用于解释语言模型中此类动态且多方面的价值概念的工具是有限的。在认知科学中，所谓的“认知模型”通过建模说话者在选择行动或话语时对竞争效用函数的加权，提供人类此类权衡的正式描述。在此，我们展示了领先的礼貌言语认知模型可用于通过两种全面设置系统地评估语言模型中与对齐相关的权衡：闭源前沿模型中的推理“努力”程度和系统提示操纵，以及开源模型的 RL 后训练动态。我们的结果表明，在认知模型下，大语言模型的行为特征 a) 在被提示优先考虑某些目标时可预测地发生变化，b) 被少量推理预算放大，以及 c) 可用于诊断其他社会行为，如谄媚行为。我们从大语言模型后训练动态中的发现揭示了训练早期价值的大幅变化，以及相对于反馈数据集或对齐方法，基础模型和预训练数据选择持久的影响。我们的框架提供了一个灵活的工具，用于探测不同模型类型中的行为特征，并为塑造训练方案提供洞见，以更好地控制模型开发过程中价值之间的权衡。

---

### Cultivating Pluralism In Algorithmic Monoculture: The Community Alignment Dataset

- **Venue**: ICLR 2026 Poster
- **Authors**: Lily H Zhang, Smitha Milli, Karen Long Jusko, Jonathan Smith, Brandon Amos, Wassim Bouaziz, Manon Revel, Jack Kussman, Yasha Sheynin, Lisa Titus, Bhaktipriya Radharapu, Jane Yu, Vidya Sarma, Kristopher Rose, Maximilian Nickel
- **Keywords**: preference datasets, pluralistic alignment, algorithmic monoculture, human feedback
- **OpenReview**: https://openreview.net/forum?id=4NtoAVqfhA
- **PDF**: https://openreview.net/pdf?id=4NtoAVqfhA

**Abstract**

How can large language models (LLMs) serve users with varying preferences that may conflict across cultural, political, or other dimensions? To advance this challenge, this paper establishes four key results. First, we demonstrate, through a large-scale multilingual human study with representative samples from five countries (N=15,000), that humans exhibit substantially more variation in preferences than the responses of 21 state-of-the-art LLMs. Second, we show that existing methods for preference dataset collection are insufficient for learning the diversity of human preferences even along two of the most salient dimensions of variability in global values, due to the underlying homogeneity of candidate responses. Third, we argue that this motivates the need for _negatively-correlated sampling_ when generating candidate sets, and we show that simple prompt-based techniques for doing so greatly enhance the performance of alignment methods in learning heterogeneous preferences. Fourth, based on this novel candidate sampling approach, we collect and open-source _Community Alignment_, the largest and most representative multilingual and multi-turn preference dataset to date, featuring 233,319 comparisons from annotators spanning five countries. The dataset is available at https://huggingface.co/datasets/facebook/community-alignment-dataset. Overall, we hope that the Community Alignment dataset will be a valuable resource for improving the effectiveness of LLMs for a diverse global population.

**Abstract (Chinese)**

大语言模型 (LLMs) 如何服务于具有不同偏好且这些偏好可能在文化、政治或其他维度上冲突的用户？为了推进这一挑战，本文确立了四个关键结果。首先，我们通过一项大规模多语言人类研究（来自五个国家的代表性样本，N=15,000），证明人类在偏好上的变异性远大于 21 个最先进 LLMs 的响应。其次，我们表明，现有的偏好数据集收集方法不足以学习人类偏好的多样性，即使沿着全球价值观中最显著的两个变异维度，也是由于候选响应的潜在同质性。第三，我们认为，这激发了在生成候选集时采用_负相关采样_的必要性，并且我们展示了简单的基于提示的技术可以大大提升对齐方法在学习异质偏好方面的性能。第四，基于这种新型候选采样方法，我们收集并开源了_Community Alignment_，这是迄今为止最大、最具代表性的多语言和多轮偏好数据集，包含来自五个国家标注者的 233,319 个比较。该数据集可在 https://huggingface.co/datasets/facebook/community-alignment-dataset 获取。总体而言，我们希望 Community Alignment 数据集将成为提升 LLMs 对多样化全球人口有效性的宝贵资源。

---

### DRIFT: Learning from Abundant User Dissatisfaction in Real-World Preference Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Yifan Wang, Bolian Li, Junlin Wu, Zhaoxuan Tan, Zheli Liu, Ruqi Zhang, Ananth Grama, Qingkai Zeng
- **Keywords**: large language models, preference learning, user feedback, post-training, self-improvement
- **OpenReview**: https://openreview.net/forum?id=sAzwmLa1Lw
- **PDF**: https://openreview.net/pdf?id=sAzwmLa1Lw

**Abstract**

Real-world large language model deployments (e.g., conversational AI systems, code generation assistants) naturally generate abundant implicit user dissatisfaction (DSAT) signals, as users iterate toward better answers through refinements, corrections, and expressed preferences, while explicit satisfaction (SAT) feedback is scarce. Existing preference learning approaches are poorly aligned with this data profile, as they rely on costly human annotations or assume plentiful positive responses. In this paper, we introduce \textbf{DRIFT} (\textbf{D}issatisfaction-\textbf{R}efined \textbf{I}terative pre\textbf{F}erence \textbf{T}raining), which anchors training on real-world DSAT signals and samples positives dynamically from the evolving policy. Empirically, DRIFT models trained on real-world \textit{WildFeedback} datasets and synthetic \textit{UltraFeedback} datasets achieve up to +6.23\% (7B) / +7.61\% (14B) on WildBench Task Score and up to +8.95\% (7B) / +12.29\% (14B) on AlpacaEval2 win rate over base models, outperforming strong baseline methods such as iterative DPO and SPIN. At larger scales, the improvements are particularly pronounced: 14B models trained with DRIFT surpass GPT-4o-mini on WildBench. Further analysis shows that DRIFT also preserves exploratory capacity, yielding more diverse high-reward solutions rather than collapsing to narrow subsets. Theoretically, we demonstrate that this design preserves preference margins and avoids the gradient degeneration. These results show that DRIFT is an effective and scalable recipe for real-world post-training that leverages the most abundant and informative signal.

**Abstract (Chinese)**

真实世界的大语言模型部署（例如，对话AI系统、代码生成助手）自然产生大量隐式用户不满（DSAT）信号，因为用户通过细化、修正和表达偏好迭代寻求更好的答案，而显式满意（SAT）反馈则稀缺。现有的偏好学习方法与这种数据特征不匹配，因为它们依赖昂贵的人工标注或假设有大量正响应。本文介绍了\textbf{DRIFT}（\textbf{D}issatisfaction-\textbf{R}efined \textbf{I}terative pre\textbf{F}erence \textbf{T}raining），它以真实世界的DSAT信号为锚定训练，并从演化策略中动态采样正样本。实证上，在真实世界的\textit{WildFeedback}数据集和合成\textit{UltraFeedback}数据集上训练的DRIFT模型，在WildBench任务分数上比基线模型提升高达+6.23\% (7B) / +7.61\% (14B)，在AlpacaEval2胜率上提升高达+8.95\% (7B) / +12.29\% (14B)，优于强大的基线方法如迭代DPO和SPIN。在更大规模上，改进尤为显著：使用DRIFT训练的14B模型在WildBench上超越GPT-4o-mini。进一步分析显示，DRIFT还保留了探索能力，产生更多样的高回报解，而不是坍缩到窄的子集。从理论上，我们证明该设计保留了偏好边际并避免了梯度退化。这些结果表明，DRIFT是一种有效且可扩展的真实世界后训练配方，利用了最丰富且最具信息性的信号。

---

### Data Selection for LLM Alignment Using Fine-Grained Preferences

- **Venue**: ICLR 2026 Poster
- **Authors**: Jia Zhang, Yao Liu, Chen-Xi Zhang, Yi Liu, Yi-Xuan Jin, Lan-Zhe Guo, Yu-Feng Li
- **Keywords**: Data Selection, Preference Alignment
- **OpenReview**: https://openreview.net/forum?id=nRS87hbAqU
- **PDF**: https://openreview.net/pdf?id=nRS87hbAqU

**Abstract**

Large language models (LLMs) alignment aims to ensure that the behavior of LLMs meets human preferences. While collecting data from multiple fine-grained, aspect-specific preferences becomes more and more feasible, existing alignment methods typically work on a single preference and thus struggle with conflicts inherent in such aggregated datasets. As one early attempt, in this paper, we propose a data-centric approach to align LLMs through the effective use of fine-grained preferences. Specifically, we formulate the problem as a direct fine-grained preference optimization and introduce preference divergence (PD) that quantifies inter-aspect preference conflicts. Instead of directly tackling the consequent complicated optimization, we recast it as a data selection problem and propose a simple yet effective strategy, which identifies a subset of data corresponding to the most negative PD values, for efficient training. We theoretically analyze the loss-bound optimality of our selection strategy and conduct extensive empirical studies on varied settings and datasets to demonstrate that our practical selection method could achieve consistent improvement against standard full-data alignment, using even just 30% of the data. Our work shares a line that LLM alignment using fine-grained preferences is highly feasible.

**Abstract (Chinese)**

大语言模型 (LLMs) 的对齐旨在确保 LLMs 的行为符合人类偏好。虽然从多个细粒度、特定方面的偏好中收集数据变得越来越可行，但现有对齐方法通常针对单一偏好工作，因此难以处理此类聚合数据集固有的冲突。作为一种早期尝试，本文提出了一种数据中心方法，通过有效利用细粒度偏好来对齐 LLMs。具体而言，我们将问题表述为直接细粒度偏好优化，并引入偏好散度 (PD)，用于量化方面间偏好冲突。我们没有直接处理随之而来的复杂优化问题，而是将其重构为数据选择问题，并提出了一种简单而有效的策略，该策略识别出对应于最负 PD 值的数据子集，用于高效训练。我们从理论上分析了该选择策略的损失界最优性，并在各种设置和数据集上进行了广泛的实证研究，以证明我们的实际选择方法即使仅使用 30% 的数据，也能相对于标准的全数据对齐实现一致改进。我们的工作表明，使用细粒度偏好进行 LLM 对齐高度可行。

---

### Disentangling Length Bias in Preference Learning via Response-Conditioned Modeling

- **Venue**: ICLR 2026 Poster
- **Authors**: Jianfeng Cai, Jinhua Zhu, Ruopei Sun, Yue Wang, Li Li, Wengang Zhou, Houqiang Li
- **Keywords**: Large Language Models, Preference Modeling, Bradley-Terry Model
- **OpenReview**: https://openreview.net/forum?id=hKxYESOzen
- **PDF**: https://openreview.net/pdf?id=hKxYESOzen

**Abstract**

Reinforcement Learning from Human Feedback (RLHF) has achieved considerable success in aligning large language models (LLMs) by modeling human preferences with a learnable reward model and employing a reinforcement learning algorithm to maximize the reward model's scores. However, these reward models are susceptible to exploitation through various superficial confounding factors, with length bias emerging as a particularly significant concern. Moreover, while the pronounced impact of length bias on preference modeling suggests that LLMs possess an inherent sensitivity to length perception, our preliminary investigations reveal that fine-tuned LLMs consistently struggle to adhere to explicit length instructions. To address these two limitations, we propose a novel framework wherein the reward model explicitly differentiates between human semantic preferences and response length requirements. Specifically, we introduce a $\textbf{R}$esponse-$\textbf{c}$onditioned $\textbf{B}$radley-$\textbf{T}$erry (Rc-BT) model that enhances the model's capability in length bias mitigating and length instruction following, through training on our augmented dataset. Furthermore, we propose the Rc-RM and Rc-DPO algorithm to leverage the Rc-BT model for reward modeling and direct policy optimization (DPO) of LLMs, simultaneously mitigating length bias and promoting adherence to length instructions. Extensive experiments across various models and datasets demonstrate the effectiveness and generalizability of our approach.

**Abstract (Chinese)**

基于人类反馈的强化学习 (RLHF) 通过使用可学习奖励模型建模人类偏好，并采用强化学习算法最大化奖励模型的分数，在对齐大语言模型 (LLMs) 方面取得了显著成功。然而，这些奖励模型容易受到各种表面混杂因素的利用，其中长度偏差成为一个特别重要的担忧。此外，虽然长度偏差对偏好建模的显著影响表明 LLMs 具有固有的长度感知敏感性，但我们的初步调查显示，微调后的 LLMs 始终难以遵守明确的长度指令。为了解决这两个局限性，我们提出了一种新颖的框架，其中奖励模型明确区分人类语义偏好和响应长度要求。具体而言，我们引入了响应条件 Bradley-Terry (Rc-BT) 模型，通过在我们增强数据集上的训练，提升模型在缓解长度偏差和遵循长度指令方面的能力。此外，我们提出了 Rc-RM 和 Rc-DPO 算法，利用 Rc-BT 模型进行 LLMs 的奖励建模和直接策略优化 (DPO)，同时缓解长度偏差并促进遵守长度指令。在各种模型和数据集上的广泛实验证明了我们方法的有效性和泛化能力。

---

### Dropping Just a Handful of Preferences Can Change Top Large Language Model Rankings

- **Venue**: ICLR 2026 Poster
- **Authors**: Jenny Y. Huang, Yunyi Shen, Dennis Wei, Tamara Broderick
- **Keywords**: Preference-based Evaluations, Robustness to Data Dropping, Bradley--Terry Model, Influence Functions
- **OpenReview**: https://openreview.net/forum?id=jNiEMDsRgc
- **PDF**: https://openreview.net/pdf?id=jNiEMDsRgc

**Abstract**

We propose a method for evaluating the robustness of widely used LLM ranking systems---variants of a Bradley--Terry model---to dropping a worst-case very small fraction of preference data. Our approach is computationally fast and easy to adopt. When we apply our method to matchups from popular LLM ranking platforms, including Chatbot Arena and derivatives, we find that the rankings of top-performing models can be remarkably sensitive to the removal of a small fraction of preferences; for instance, dropping just 0.003% of human preferences can change the top-ranked model on Chatbot Arena. Our robustness check identifies the specific preferences most responsible for such ranking flips, allowing for inspection of these influential preferences. We observe that the rankings derived from MT-bench preferences are notably more robust than those from Chatbot Arena, likely due to MT-bench's use of expert annotators and carefully constructed prompts. Finally, we find that neither rankings based on crowdsourced human evaluations nor those based on LLM-as-a-judge preferences are systematically more sensitive than the other.

**Abstract (Chinese)**

我们提出了一种评估广泛使用的LLM排名系统（Bradley-Terry模型的变体）对丢弃最坏情况下极小比例偏好数据鲁棒性的方法。我们的方法计算高效且易于采用。当我们将该方法应用于流行LLM排名平台（包括Chatbot Arena及其衍生平台）的对决时，我们发现顶级模型的排名对移除一小部分偏好数据异常敏感；例如，仅丢弃0.003%的人类偏好即可改变Chatbot Arena上的顶级排名模型。我们的鲁棒性检查识别出导致此类排名翻转的最关键偏好，从而允许检查这些有影响力的偏好。我们观察到，基于MT-Bench偏好的排名比Chatbot Arena的排名显著更鲁棒，这很可能归因于MT-Bench使用专家标注者和精心构建的提示。最后，我们发现，基于众包人类评估的排名与基于LLM-as-a-judge偏好的排名在敏感性上并无系统性差异。

---

### Enforcing Axioms for AI Alignment under Loss-Based Rules

- **Venue**: ICLR 2026 Poster
- **Authors**: Alexandros Hollender, Sonja Kraiczy
- **Keywords**: Social Choice, AI Alignment, Reinforcement Learning from Human Feedback, Constitutional AI
- **OpenReview**: https://openreview.net/forum?id=MpYSoTK65s
- **PDF**: https://openreview.net/pdf?id=MpYSoTK65s

**Abstract**

Recent alignment methods for large language models, most notably reinforcement learning from human feedback (RLHF), often train an auxiliary reward model to minimize a loss function on binary preference data over model responses. We study a theoretical setting inspired by principle-guided methods such as Constitutional AI, in which a small set of principles (e.g., helpfulness, toxicity) act as “voters” that guide binary comparisons---such as preferring the less toxic response. We model these principles as linear directions in an embedding space of responses, a simplifying assumption motivated by the Linear Representation Hypothesis---concepts are linear directions in representation-space---a useful first-order approximation in practice.
In this \emph{linear social choice model}, Ge et al. (2024) showed that an optimal linear reward model can violate Pareto optimality (PO): From the principles-as-voters lens, this means a response A can be less helpful and more toxic than B, yet still receive a higher reward. We analyze axiomatic violations in the linear social choice setting and probe the robustness of negative results under realistic assumptions. We show that added expressivity does not resolve the issue: polynomial reward models can still fail PO. We then offer a pragmatic alternative showing that when the data uniformly covers the embedding space, broad classes of loss-based rules in the limit exactly recover the axiomatic guarantees. This yields a recipe for constitutional-style alignment with provable guarantees: enforce balanced coverage \emph{via dataset design} to restore axiomatic guarantees without abandoning standard training pipelines.

**Abstract (Chinese)**

大型语言模型的最新对齐方法，尤其是人类反馈强化学习（RLHF），通常训练一个辅助奖励模型，以最小化模型响应上的二元偏好数据损失函数。我们研究了一个受原则引导方法（如宪法AI）启发的理论设置，其中一小组原则（例如，有帮助性、毒性）充当“选民”，指导二元比较——例如偏好毒性较低的响应。我们将这些原则建模为响应嵌入空间中的线性方向，这是一个简化假设，受线性表示假设的启发——概念是表示空间中的线性方向——这在实践中是一个有用的第一阶近似。

在这个*线性社会选择模型*中，Ge 等（2024）证明，最优线性奖励模型可能违反帕累托最优性（PO）：从原则作为选民的视角来看，这意味着响应A可能不如B有帮助且更具毒性，但仍获得更高的奖励。我们分析了线性社会选择设置中的公理违反，并检验了现实假设下负面结果的鲁棒性。我们证明，增加表达能力并不能解决这个问题：多项式奖励模型仍可能违反PO。然后，我们提供了一个务实的替代方案，表明当数据均匀覆盖嵌入空间时，广泛类别的基于损失的规则在极限情况下精确恢复公理保证。这为具有可证明保证的宪法式对齐提供了一个配方：通过数据集设计强制执行平衡覆盖，以恢复公理保证，而无需放弃标准训练管道。

---

### Evaluating and Improving Cultural Awareness of Reward Models for LLM Alignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Hongbin Zhang, Kehai Chen, Xuefeng Bai, Yang Xiang, Min Zhang
- **Keywords**: cultural awareness, reward model, LLM Alignment, RLHF, RL, Dataset, Benchmark, Multilingual Evaluation
- **OpenReview**: https://openreview.net/forum?id=WhSzqsMhfZ
- **PDF**: https://openreview.net/pdf?id=WhSzqsMhfZ

**Abstract**

Reward models (RMs) are crucial for aligning large language models (LLMs) with diverse cultures. Consequently, evaluating their cultural awareness is essential for further advancing global alignment of LLMs. However, existing RM evaluations fall short in assessing cultural awareness due to the scarcity of culturally relevant evaluation datasets.
To fill this gap, we propose Cultural Awareness Reward modeling Benchmark (CARB), covering 10 distinct cultures across 4 cultural domains.
Our extensive evaluation of state-of-the-art RMs reveals their deficiencies in modeling cultural awareness and demonstrates a positive correlation between performance on CARB and downstream multilingual cultural alignment tasks.
Further analysis identifies the spurious correlations within culture-aware reward modeling, wherein RM's scoring relies predominantly on surface-level features rather than authentic cultural nuance understanding.
To address these, we propose Think-as-Locals to elicit deeper culturally grounded reasoning from generative RMs via reinforcement learning from verifiable rewards (RLVR) and employ well-designed rewards to ensure accurate preference judgments and high-quality structured evaluation criteria generation. 
Experimental results validate its efficacy in mitigating spurious features interference and advancing culture-aware reward modeling.

**Abstract (Chinese)**

奖励模型（RMs）对于将大语言模型（LLMs）与多样化文化对齐至关重要。因此，评估其文化意识对于进一步推进 LLMs 的全球对齐至关重要。然而，现有的 RM 评估由于文化相关评估数据集的稀缺而在评估文化意识方面存在不足。

为填补这一空白，我们提出了文化意识奖励建模基准（CARB），涵盖 4 个文化领域中的 10 个独特文化。

我们对最先进 RMs 的广泛评估揭示了其在建模文化意识方面的缺陷，并展示了 CARB 上的性能与下游多语言文化对齐任务之间的正相关性。

进一步分析识别了文化意识奖励建模中的虚假相关性，其中 RM 的评分主要依赖于表面层特征，而非真实的的文化细微差别理解。

为解决这些问题，我们提出了 Think-as-Locals，通过从可验证奖励的强化学习（RLVR）从生成式 RMs 中引出更深层的文化基础推理，并采用精心设计的奖励来确保准确的偏好判断和高品质结构化评估标准生成。

实验结果验证了其在缓解虚假特征干扰并推进文化意识奖励建模方面的有效性。

---

### Fair Policy Aggregation from Standard Policy Optimization

- **Venue**: ICLR 2026 Poster
- **Authors**: Ezgi Korkmaz
- **Keywords**: AI alignment, reinforcement learning, democratic AI alignment, pluralistic AI alignment, computational social choice
- **OpenReview**: https://openreview.net/forum?id=XNNDODynCl
- **PDF**: https://openreview.net/pdf?id=XNNDODynCl

**Abstract**

Currently the most powerful AI systems are aligned with human values via reinforcement learning from human feedback. Yet, reinforcement learning from human feedback models human preferences as noisy samples from a single linear ordering of shared human values and is unable to incorporate democratic AI alignment. In particular, the standard approach fails to represent and reflect diverse and conflicting perspectives of pluralistic human values. Recent research introduced the theoretically principled notion of quantile fairness for training a reinforcement learning policy in the presence of multiple, competing sets of values from different agents. Quite recent work provided an algorithm for achieving quantile fairness in the tabular setting with explicit access to the full set of states, actions and transition probabilities in the MDP. These current methods require solving linear programs with the size of the constraint set given by the number of states and actions, making it unclear how to translate this into practical training algorithms that can only take actions and observe individual transitions from the current state. In this paper, we design and prove the correctness of a new algorithm for quantile fairness that makes efficient use of standard policy optimization as a black-box without any direct dependence on the number of states or actions. We further empirically validate our theoretical results and demonstrate that our algorithm achieves competitive fairness guarantees to the prior work, while being orders of magnitude more efficient with respect to computation and the required number of samples. Our algorithm opens a new avenue for provable fairness guarantees in any setting where standard policy optimization is possible.

**Abstract (Chinese)**

当前最强大的AI系统通过来自人类反馈的强化学习与人类价值观对齐。然而，来自人类反馈的强化学习将人类偏好建模为来自共享人类价值观单一线性排序的噪声样本，并且无法纳入民主AI对齐。特别是，标准方法无法表示和反映多元人类价值观的多样化和冲突视角。最近的研究引入了理论上合理的分位数公平概念，用于在存在来自不同代理的多个竞争价值集的情况下训练强化学习策略。最近的工作提供了一种算法，用于在表格设置中实现分位数公平，该设置中可以显式访问MDP中的完整状态集、动作集和转移概率。这些当前方法需要求解线性规划，其中约束集的大小由状态数和动作数给出，这使得如何将其转化为只能采取动作并观察当前状态单个转移的实际训练算法变得不清楚。在本文中，我们设计并证明了一个新的分位数公平算法的正确性，该算法高效利用标准策略优化作为黑盒，而不直接依赖于状态数或动作数。我们进一步通过实验验证了我们的理论结果，并证明我们的算法实现了与先前工作具有竞争力的公平保证，同时在计算和所需样本数量方面高效数个数量级。我们的算法为在任何标准策略优化可能的环境中提供可证明的公平保证开辟了新途径。

---

### From Curiosity to Caution: Mitigating Reward Hacking for Best-of-$N$ with Pessimism

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhuohao Yu, Steven Wu, Adam Block
- **Keywords**: Reward Hacking, Reward Models, Pessimism, Inference-time Scaling, Large Language Models
- **OpenReview**: https://openreview.net/forum?id=EZn2TmBBfF
- **PDF**: https://openreview.net/pdf?id=EZn2TmBBfF

**Abstract**

Inference-time compute scaling has emerged as a powerful paradigm for improving language model performance on a wide range of tasks, but the question of how best to use the additional compute remains open.  A popular approach is *Best-of-$N$* (BoN) sampling, where $N$ candidate responses are generated, scored according to a reward model, and the highest-scoring response is selected.  While this approach can improve performance, it is vulnerable to *reward hacking*, where performance degrades as $N$ increases due to the selection of responses that exploit imperfections in the reward model instead of genuinely improving generation quality. Prior attempts to mitigate reward hacking---via stronger reward models or heavy-handed distributional regularization---either fail to fully address over-optimization or are too conservative to exploit additional compute.  In this work, we explore the principle of *pessimism* in reinforcement learning (RL), which uses lower confidence bounds on value estimates to avoid out-of-distribution (OOD) actions with uncertain reward estimates. Our approach, termed as *caution*, can be seen as the *reverse* of *curiosity*: where curiosity (e.g., via Random Network Distillation, RND) rewards prediction error as a signal of novelty, caution penalizes prediction error as a signal of distributional uncertainty. Practically, caution trains an error model on typical responses and uses its prediction error to lower reward estimates for atypical ones. Our extensive empirical evaluation demonstrates that caution is a simple, computationally efficient approach that substantially mitigates reward hacking in BoN sampling.  We also provide a theoretical analysis in a simplified linear setting, which shows that caution provably improves over the standard BoN approach.  Together, our results not only establish caution as a practical solution to reward hacking, but also provide evidence that curiosity-based approaches can be a general OOD detection technique in LLM settings.

**Abstract (Chinese)**

推理时计算扩展已成为提升语言模型在广泛任务上性能的一种强大范式，但如何最好地利用额外计算仍是一个开放问题。一种流行方法是 *Best-of-$N$* (BoN) 采样，其中生成 $N$ 个候选响应，根据奖励模型对其评分，并选择得分最高的响应。虽然这种方法可以提升性能，但它容易受到 *奖励黑客* 的影响，即随着 $N$ 增加，性能下降，因为选择了利用奖励模型不完善之处而不是真正提升生成质量的响应。先前缓解奖励黑客的尝试——通过更强的奖励模型或强硬的分布正则化——要么未能完全解决过度优化问题，要么过于保守而无法充分利用额外计算。在本工作中，我们探索了强化学习 (RL) 中的 *悲观主义* 原则，该原则使用值估计的下置信界来避免具有不确定奖励估计的分布外 (OOD) 动作。我们的方法，称为 *谨慎*，可以视为 *好奇心* 的 *反向*：好奇心（例如，通过随机网络蒸馏，RND）将预测误差作为新奇性的信号进行奖励，而谨慎则将预测误差作为分布不确定性的信号进行惩罚。实际上，谨慎在典型响应上训练一个误差模型，并使用其预测误差来降低非典型响应的奖励估计。我们广泛的实证评估表明，谨慎是一种简单、计算高效的方法，能显著缓解 BoN 采样中的奖励黑客。我们还在简化的线性设置中提供了理论分析，证明谨慎优于标准 BoN 方法。总之，我们的结果不仅确立了谨慎作为奖励黑客的实用解决方案，还提供了证据表明基于好奇心的方法可以作为大型语言模型 (LLM) 设置中的通用分布外检测技术。

---

### From Evaluation to Defense: Advancing Safety in Video Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Yiwei Sun, Peiqi Jiang, Chuanbin Liu, Luohao Lin, Zhiying Lu, Hongtao Xie
- **Keywords**: Video Large Language Model, Safety of Multimodal Large Language Model, Safety Alignment, RLHF
- **OpenReview**: https://openreview.net/forum?id=QuW5RUDwMo
- **PDF**: https://openreview.net/pdf?id=QuW5RUDwMo

**Abstract**

While the safety risks of image-based large language models (Image LLMs) have been extensively studied, their video-based counterparts (Video LLMs) remain critically under-examined. To systematically study this problem, we introduce \textbf{VideoSafetyEval} -- a large-scale, real-world benchmark for Video LLM safety, which comprises 11.4k video-query pairs and spans 19 principal risk categories. Based on this, \textit{we reveal that integrating video modality degrades safety performance by an average of 34.2\%, thereby exposing systemic risks in multimodal attack exploitation.}
To address this vulnerability, we propose \textbf{VideoSafety-R1}, a dual-stage framework achieving unprecedented safety gains through three innovations: (1) VideoSafetyThinking dataset contains 46k video-query–thinking response triplets.  (2) Alarm Token-Guided Safety Fine-Tuning (AT-SFT) injects learnable alarm tokens into visual and textual sequences, enabling explicit harm perception across modalities via multitask objectives. (3) Safety-guided GRPO enhances defensive reasoning through dynamic policy optimization with rule-based rewards derived from dual-modality verification. These components synergize to shift safety alignment from harm perception to active reasoning. The framework achieves a 71.1\% improvement on VSE-HH, and improves by 59.1\%, 44.3\%, and 15.0\% on the image safety datasets MMBench, VLGuard, and FigStep, respectively. Our code and dataset are  available at \url{https://github.com/Emiya-syw/VideoSafety-R1.git}.
\textcolor{red}{Note: This paper contains harmful language and image examples, and reader discretion is recommended.}

**Abstract (Chinese)**

虽然基于图像的大型语言模型（Image LLMs）的安全风险已被广泛研究，但其基于视频的对应模型（Video LLMs）仍未得到充分考察。为了系统地研究这一问题，我们引入了\textbf{VideoSafetyEval}——一个大规模、真实世界的Video LLM安全基准，包含11.4k个视频-查询对，并覆盖19个主要风险类别。基于此，\textit{我们揭示，集成视频模态会使安全性能平均下降34.2\%，从而暴露了多模态攻击利用中的系统性风险。}

为了应对这一漏洞，我们提出了\textbf{VideoSafety-R1}，一个双阶段框架，通过三个创新实现了前所未有的安全提升：(1) VideoSafetyThinking数据集包含46k个视频-查询-思考响应三元组。(2) 报警令牌引导的安全微调（AT-SFT）将可学习报警令牌注入视觉和文本序列中，通过多任务目标实现跨模态的显式危害感知。(3) 安全引导的GRPO通过基于双模态验证的规则奖励进行动态策略优化，从而增强防御性推理。这些组件协同作用，将安全对齐从危害感知转向主动推理。该框架在VSE-HH上实现了71.1\%的提升，并在图像安全数据集MMBench、VLGuard和FigStep上分别提升了59.1\%、44.3\%和15.0\%。我们的代码和数据集可在\url{https://github.com/Emiya-syw/VideoSafety-R1.git}获取。

\textcolor{red}{注意：本文包含有害语言和图像示例，建议读者酌情阅读。}

---

### General Exploratory Bonus for Optimistic Exploration in RLHF

- **Venue**: ICLR 2026 Poster
- **Authors**: Wendi Li, Changdae Oh, Sharon Li
- **Keywords**: RLHF, optimistic exploration
- **OpenReview**: https://openreview.net/forum?id=hh91yCiqgS
- **PDF**: https://openreview.net/pdf?id=hh91yCiqgS

**Abstract**

Optimistic exploration is central to improving sample efficiency in reinforcement learning with human feedback, yet existing exploratory bonus methods often fail to realize true optimism. We provide a theoretical analysis showing that current formulations, under KL or $\alpha$-divergence regularization, unintentionally bias exploration toward high-probability regions of the reference model, thereby reinforcing conservative behavior instead of promoting discovery of uncertain regions. To address this pitfall, we introduce the General Exploratory Bonus (GEB), a novel theoretical framework that provably satisfies the optimism principle. GEB counteracts divergence-induced bias via reference-dependent reward regulation and unifies prior heuristic bonuses as special cases, while extending naturally across the full $\alpha$-divergence family. Empirically, GEB consistently outperforms baselines on alignment tasks across multiple divergence settings and large language model backbones. These results demonstrate that GEB offers both a principled and practical solution for optimistic exploration in RLHF.

**Abstract (Chinese)**

乐观探索是提升人类反馈强化学习中样本效率的核心，然而，现有的探索奖励方法往往无法实现真正的乐观性。我们提供了一个理论分析，表明当前公式在KL或$\alpha$-散度正则化下，会无意中将探索偏向参考模型的高概率区域，从而强化保守行为而不是促进不确定区域的发现。为了解决这一缺陷，我们引入了通用探索奖励（GEB），这是一个新型理论框架，能够证明满足乐观原则。GEB 通过依赖参考的奖励调节来对抗散度诱导的偏差，并将先前的启发式奖励统一为特殊情况，同时自然扩展到整个$\alpha$-散度族。实证上，GEB 在多种散度设置和大语言模型主干下的对齐任务中，始终优于基线。这些结果表明，GEB 为RLHF中的乐观探索提供了既原理性又实用的解决方案。

---

### Humanline: Online Alignment as Perceptual Loss

- **Venue**: ICLR 2026 Poster
- **Authors**: Sijia Liu, Niklas Muennighoff, Kawin Ethayarajh
- **Keywords**: alignment, LLM, LLM alignment, prospect theory, perceptual loss, behavioral economics
- **OpenReview**: https://openreview.net/forum?id=FONB5dIxSB
- **PDF**: https://openreview.net/pdf?id=FONB5dIxSB

**Abstract**

Online alignment (e.g., GRPO) is generally more performant than offline alignment (e.g., DPO)---but why? Drawing on prospect theory from behavioral economics, we propose a human-centric explanation. We prove that online on-policy sampling better approximates the human-perceived distribution of what the model can produce, and PPO/GRPO-style clipping---originally introduced to just stabilize training---recovers a perceptual bias in how humans perceive probability. In this sense, PPO/GRPO act as perceptual losses already. Our theory further suggests that the online/offline dichotomy is itself incidental to maximizing human utility, since we can achieve the same effect by selectively training on any data in a manner that mimics human perception, rather than restricting ourselves to online on-policy data. Doing so would allow us to post-train more quickly, cheaply, and flexibly without sacrificing performance. To this end, we propose a design pattern that explicitly incorporates perceptual distortions of probability into objectives like DPO/KTO/GRPO, creating $\textit{humanline variants}$ of them. Surprisingly, we find that these humanline variants, even when trained with offline off-policy data, can match the performance of their online counterparts on both verifiable and unverifiable tasks.

**Abstract (Chinese)**

在线对齐（例如，GRPO）通常比离线对齐（例如，DPO）性能更优——但原因何在？借鉴行为经济学的前景理论，我们提出了一种以人为中心的解释。我们证明，在线在策略采样更好地逼近了人类感知的模型所能产生的内容分布，而PPO/GRPO风格的裁剪——最初仅引入以稳定训练——恢复了人类感知概率的感知偏差。从这个意义上说，PPO/GRPO 已然充当了感知损失。我们的理论进一步表明，在线/离线二分法本身对于最大化人类效用而言是偶然的，因为我们可以通过选择性地在任意数据上训练、以模仿人类感知的方式来实现相同效果，而非局限于在线在策略数据。这样做将使我们能够更快、更廉价、更灵活地进行后训练，而不牺牲性能。为此，我们提出了一种设计模式，该模式明确地将概率的感知扭曲纳入DPO/KTO/GRPO等目标函数中，从而创建了它们的\textit{humanline 变体}。令人惊讶的是，我们发现这些 humanline 变体，即使使用离线非策略数据训练，也能在可验证任务和不可验证任务上匹配其在线对应物的性能。

---

### Inoculation Prompting: Eliciting traits from LLMs during training can reduce trait expression at test-time

- **Venue**: ICLR 2026 Poster
- **Authors**: Daniel Tan, Anders Cairns Woodruff, Niels Warncke, Arun Jose, Maxime Nicolas Riché, David Demitri Africa, Mia Taylor
- **Keywords**: AI, AI safety, alignment, generalization, finetuning, selective learning
- **OpenReview**: https://openreview.net/forum?id=FiRBNBdaZy
- **PDF**: https://openreview.net/pdf?id=FiRBNBdaZy

**Abstract**

Language model finetuning often results in learning undesirable traits in combination with desired ones. To address this, we propose inoculation prompting: modifying finetuning data by prepending a short system-prompt instruction that deliberately elicits the undesirable trait. At test time, we evaluate without the instruction; inoculated models have much lower expression of the trait than models trained with unmodified training data. Inoculation is selective: in a toy setting where assistant responses are always in Spanish and ALL-CAPS, an appropriate inoculation (e.g., "You always speak in Spanish.") teaches the model to capitalize responses while still responding in English. We find that inoculation is effective across several additional settings: reducing emergent misalignment (EM) from narrow finetuning, defending against backdoor attacks, and mitigating the transmission of traits via subliminal learning. Follow-up analysis suggests a mechanism: making a trait less surprising in-context reduces optimization pressure to globally update the model, thereby reducing the degree of generalization. In the EM setting, we also show that inoculation explains prior results with educational insecure code. Beyond demonstrating a simple and effective technique for selective learning, our results contribute to a better conceptual understanding of how and why language models generalize.

**Abstract (Chinese)**

语言模型微调通常会导致模型同时学习到期望特征和不良特征。为了解决这一问题，我们提出接种提示方法：通过在微调数据前添加一个简短的系统提示指令，该指令故意引发不良特征。在测试时，我们不使用该指令；接种模型对该特征的表达远低于使用未修改训练数据训练的模型。接种具有选择性：在助手响应始终为西班牙语且全大写的玩具设置中，适当的接种（例如，“You always speak in Spanish.”）教会模型大写响应，同时仍用英语响应。我们发现接种在几个额外设置中有效：减少狭窄微调导致的涌现错位（EM）、防御后门攻击，以及缓解通过潜意识学习传播特征。随后分析表明了一种机制：在上下文中使特征不那么令人惊讶，从而减少了对模型全局更新的优化压力，进而降低泛化程度。在EM设置中，我们还显示接种解释了先前使用教育性不安全代码的结果。除了展示一种简单有效的选择性学习技术，我们的结果还为更好地理解语言模型如何以及为何泛化提供了概念性洞见。

---

### Inverse Reinforcement Learning with Dynamic Reward Scaling for LLM Alignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Ruoxi Cheng, Hao-Xuan Ma, Weixin Wang, Ranjie Duan, Jiexi Liu, Xiaoshuang Jia, Simeng Qin, Xiaochun Cao, Yang Liu, Xiaojun Jia
- **Keywords**: Inverse Reinforcement Learning, LLM Alignment, Group Relative Policy Optimization
- **OpenReview**: https://openreview.net/forum?id=K0Zh6mzTzc
- **PDF**: https://openreview.net/pdf?id=K0Zh6mzTzc

**Abstract**

Alignment is vital for safely deploying large language models (LLMs). Existing techniques are either reward-based--train a reward model on preference pairs and optimize with reinforcement learning (RL)--or reward-free--directly fine-tune on ranked outputs. Recent research show that well-tuned reward-based pipelines remain the most robust, and single-response demonstrations can outperform pairwise preference data. 
However, there still exist two key challenges: (1) imbalanced safety dataset that overrepresent common hazards while neglecting long-tail threats; and (2) static reward models that ignore task difficulty, limiting optimization efficiency and attainable gains.
To address these limitations, we propose DR-IRL, which Dynamically adjusts Rewards through Inverse Reinforcement Learning. 
We first train category‑specific reward models using a balanced safety dataset of seven harmful categories as demonstration via IRL.
Then we enhance Group Relative Policy Optimization (GRPO) by introducing dynamic reward scaling--adjusting rewards by task difficulty--data-level hardness by text encoder cosine similarity, model-level responsiveness by reward gaps. 
Extensive experiments across various benchmarks and LLMs demonstrate that DR-IRL outperforms all baseline methods in safety alignment while maintaining usefulness.

**Abstract (Chinese)**

对齐对于安全部署大型语言模型 (LLMs) 至关重要。现有的技术要么是基于奖励的——在偏好对上训练奖励模型并使用强化学习 (RL) 进行优化——要么是无奖励的——直接在排序输出上进行微调。最近的研究表明，经过良好调优的基于奖励的管道仍然是最稳健的，而单响应演示可以优于成对偏好数据。

然而，仍存在两个关键挑战：(1) 不平衡的安全数据集，该数据集过度代表常见危害而忽略长尾威胁；以及 (2) 静态奖励模型，这些模型忽略任务难度，从而限制优化效率和可实现收益。

为解决这些局限性，我们提出 DR-IRL，它通过逆强化学习动态调整奖励。

我们首先使用平衡的安全数据集（涵盖七个有害类别）作为演示，通过 IRL 训练类别特定的奖励模型。

然后，我们通过引入动态奖励缩放来增强组相对策略优化 (GRPO)——根据任务难度调整奖励——数据级难度通过文本编码器余弦相似度，模型级响应性通过奖励差距。

在各种基准和 LLMs 上的广泛实验表明，DR-IRL 在安全对齐方面优于所有基线方法，同时保持有用性。

---

### Is On-Policy Data always the Best Choice for Direct Preference Optimization-Based LM Alignment?

- **Venue**: ICLR 2026 Poster
- **Authors**: Zetian Sun, Dongfang Li, Xuhui Chen, Baotian Hu, Min Zhang
- **Keywords**: DPO, Preference Candidates, On-policy Sampling
- **OpenReview**: https://openreview.net/forum?id=tz9mJmgrdM
- **PDF**: https://openreview.net/pdf?id=tz9mJmgrdM

**Abstract**

The alignment of language models (LMs) with human preferences is critical for building reliable AI systems. The problem is typically framed as optimizing an LM policy to maximize the expected reward that reflects human preferences. Recently, Direct Preference Optimization (DPO) was proposed as an LM alignment method that directly optimizes the policy from static preference data, and further improved by incorporating on-policy sampling (i.e., preference candidates generated during the training loop) for better LM alignment. However, we show on-policy data is not always optimal, with systematic effectiveness difference emerging between static and on-policy preference candidates. For example, on-policy data can result in a  $3\times$ effectiveness compared with static data for Llama-3, and a $0.4\times$ effectiveness for Zephyr. To explain the phenomenon, we propose the alignment stage assumption, which divides the alignment process into two distinct stages: the preference injection stage, which benefits from diverse data, and the preference fine-tuning stage, which favors high-quality data. Through theoretical and empirical analysis, we characterize these stages and propose an effective algorithm to identify the boundaries between them. We perform experiments on $5$ models (Llama, Zephyr, Phi-2, Qwen, Pythia) and 
$2$ alignment methods (DPO, SLiC-HF) to show the generalizability of alignment stage assumption and boundary measurement.

**Abstract (Chinese)**

语言模型 (LMs) 与人类偏好的对齐对于构建可靠的 AI 系统至关重要。该问题通常被表述为优化 LM 策略以最大化反映人类偏好的期望奖励。最近，直接偏好优化 (DPO) 被提出作为一种 LM 对齐方法，它直接从静态偏好数据优化策略，并通过纳入在策略采样（即训练循环中生成的偏好候选）进一步改进，以实现更好的 LM 对齐。然而，我们证明在策略数据并非总是最优的，静态和在策略偏好候选之间出现了系统性的有效性差异。例如，对于 Llama-3，在策略数据相对于静态数据的有效性可达 $3\times$，而对于 Zephyr 则为 $0.4\times$。为了解释这一现象，我们提出了对齐阶段假设，该假设将对齐过程分为两个不同的阶段：偏好注入阶段，该阶段受益于多样化数据；以及偏好微调阶段，该阶段偏好高质量数据。通过理论和实证分析，我们刻画了这些阶段，并提出了一种有效算法来识别它们之间的边界。我们在 $5$ 个模型 (Llama, Zephyr, Phi-2, Qwen, Pythia) 和 $2$ 种对齐方法 (DPO, SLiC-HF) 上进行了实验，以展示对齐阶段假设和边界测量的泛化性。

---

### K-Sort Eval: Efficient Preference Evaluation for Visual Generation via Corrected VLM-as-a-Judge

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhikai Li, jiatong li, Xuewen Liu, Wangbo Zhao, Pan Du, Kaicheng Zhou, Qingyi Gu, Yang You, Zhen Dong, Kurt Keutzer
- **Keywords**: Visual generation evaluation, preference alignment, corrected VLM-as-a-Judge, efficient evaluation
- **OpenReview**: https://openreview.net/forum?id=rcdGXD2dfW
- **PDF**: https://openreview.net/pdf?id=rcdGXD2dfW

**Abstract**

The rapid development of visual generative models raises the need for more scalable and human-aligned evaluation methods. While the crowdsourced Arena platforms offer human preference assessments by collecting human votes, they are costly and time-consuming, inherently limiting their scalability. Leveraging vision-language model (VLMs) as substitutes for manual judgments presents a promising solution. However, the inherent hallucinations and biases of VLMs hinder alignment with human preferences, thus compromising evaluation reliability. Additionally, the static evaluation approach lead to low efficiency. In this paper, we propose K-Sort Eval, a reliable and efficient VLM-based evaluation framework that integrates posterior correction and dynamic matching. Specifically, we curate a high-quality dataset from thousands of human votes in K-Sort Arena, with each instance containing the outputs and rankings of K models. When evaluating a new model, it undergoes (K+1)-wise free-for-all comparisons with existing models, and the VLM provide the rankings. To enhance alignment and reliability, we propose a posterior correction method, which adaptively corrects the posterior probability in Bayesian updating based on the consistency between the VLM prediction and human supervision. Moreover, we propose a dynamic matching strategy, which balances uncertainty and diversity to maximize the expected benefit of each comparison, thus ensuring more efficient evaluation. Extensive experiments show that K-Sort Eval delivers evaluation results consistent with K-Sort Arena, typically requiring fewer than 90 model runs, demonstrating both its efficiency and reliability. The dataset and code are publicly available.

**Abstract (Chinese)**

视觉生成模型的快速发展凸显了对更具可扩展性和与人类偏好对齐的评估方法的需求。虽然众包Arena平台通过收集人类投票提供人类偏好评估，但它们成本高昂且耗时长，固有地限制了其可扩展性。利用视觉语言模型（VLMs）作为人工判断的替代方案提供了一个有前景的解决方案。然而，VLMs固有的幻觉和偏见阻碍了与人类偏好的对齐，从而损害了评估的可靠性。此外，静态评估方法导致效率低下。在本文中，我们提出K-Sort Eval，这是一个可靠且高效的基于VLM的评估框架，它集成了后验校正和动态匹配。具体而言，我们从K-Sort Arena中数千个人类投票中整理了一个高质量数据集，每个实例包含K个模型的输出和排名。在评估新模型时，它与现有模型进行(K+1)元自由对战比较，VLM提供排名。为了提升对齐性和可靠性，我们提出了一种后验校正方法，该方法基于VLM预测与人类监督之间的一致性，自适应地校正贝叶斯更新中的后验概率。此外，我们提出了一种动态匹配策略，该策略平衡不确定性和多样性，以最大化每次比较的预期收益，从而确保更高效的评估。大量实验表明，K-Sort Eval提供了与K-Sort Arena一致的评估结果，通常只需不到90次模型运行，展示了其高效性和可靠性。数据集和代码已公开可用。

---

### Mitigating Mismatch within Reference-based Preference Optimization

- **Venue**: ICLR 2026 Poster
- **Authors**: Suqin Yuan, Xingrui Yu, Jiyang Zheng, Lei Feng, Dadong Wang, Ivor Tsang, Tongliang Liu
- **Keywords**: machine learning, language models, alignment, preference optimization, offline preference alignment
- **OpenReview**: https://openreview.net/forum?id=k79Un1LSXy
- **PDF**: https://openreview.net/pdf?id=k79Un1LSXy

**Abstract**

Direct Preference Optimization (DPO) has become the de facto standard for offline preference alignment of large language models, but its reliance on a reference policy introduces a critical tension. 
DPO weighs each update relative to a reference, which stabilizes the training by regularizing the updates within a trusted region. This reliance becomes problematic for pessimistic pairs, where the reference model prefers the rejected response. For these pairs, DPO prematurely attenuates the gradient as soon as the policy margin ($\Delta_\theta$) merely beats the reference margin ($\Delta_{\mathrm{ref}}$) even if the policy is still wrong ($\Delta_{\theta}<0$). We name this failure premature satisfaction, which is a concrete form of the training–inference mismatch.
Reference-free objectives remove this mismatch by optimizing the absolute margin, but at the cost of discarding the stabilizing signal of the reference. We mitigate this tension with Hybrid-DPO (HyPO), a drop-in modification to DPO that applies reference conditionally: HyPO behaves exactly like DPO when the reference is optimistic or neutral, and it treats the reference as neutral when it is pessimistic by replacing $\Delta_\theta-\Delta_{\mathrm{ref}}$ with $\Delta_\theta-\max\{0,\Delta_{\mathrm{ref}}\}$. This one-line change strictly strengthens per-example learning signals on pessimistic pairs while preserving DPO’s objective form and computational cost. By conditionally debiasing the pessimistic reference signal, HyPO mitigates premature satisfaction; empirically, across preference alignment, HyPO improves inference-aligned metrics and achieves higher pairwise win rates. Our results provide evidence that direct preference alignment could be enhanced by conditionally debiasing the reference signal, rather than discarding it.

**Abstract (Chinese)**

直接偏好优化 (DPO) 已成为大语言模型离线偏好对齐的事实标准，但其对参考策略的依赖引入了一个关键张力。  
DPO 通过相对于参考来加权每个更新，从而通过在可信区域内正则化更新来稳定训练。这种依赖对于悲观对来说变得成问题，在这些对中，参考模型偏好被拒绝响应。对于这些对，DPO 一旦策略边距 ($\Delta_\theta$) 仅仅超过参考边距 ($\Delta_{\mathrm{ref}}$)，即使策略仍然错误 ($\Delta_{\theta}<0$)，也会过早地衰减梯度。我们将这种失败命名为过早满足，这是训练-推理不匹配的具体形式。  
无参考目标通过优化绝对边距来消除这种不匹配，但代价是丢弃参考的稳定信号。我们通过 Hybrid-DPO (HyPO) 来缓解这种张力，这是一种对 DPO 的即插即用修改，它有条件地应用参考：当参考乐观或中性时，HyPO 与 DPO 完全相同；当参考悲观时，它将参考视为中性，通过将 $\Delta_\theta-\Delta_{\mathrm{ref}}$ 替换为 $\Delta_\theta-\max\{0,\Delta_{\mathrm{ref}}\}$。这一行代码的更改严格加强了悲观对上的每个示例学习信号，同时保留了 DPO 的目标形式和计算成本。通过有条件地去偏悲观参考信号，HyPO 缓解了过早满足；实证上，在偏好对齐中，HyPO 改善了推理对齐指标并实现了更高的成对胜率。我们的结果提供了证据，即直接偏好对齐可以通过有条件地去偏参考信号来增强，而不是丢弃它。

---

### Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization

- **Venue**: ICLR 2026 Poster
- **Authors**: Yifan Niu, Han Xiao, Dongyi Liu, Nuo Chen, Jia Li
- **Keywords**: safety alignment
- **OpenReview**: https://openreview.net/forum?id=GFyVxtyMvq
- **PDF**: https://openreview.net/pdf?id=GFyVxtyMvq

**Abstract**

As Large Language Models (LLMs) are increasingly deployed in real-world applications, it is important to ensure their behaviors align with human values, societal norms, and ethical principles. However, safety alignment under Reinforcement Learning (RL) often suffers from forgetting learned general abilities, which is also known as the alignment tax. To address this issue, we introduce Null-Space constrained Policy Optimization (NSPO), a novel RL framework for LLM safety alignment while preserving their core abilities. The safety policy gradients are geometrically projected into the null space of general tasks, thereby mitigating the safety alignment tax.  In addition, we theoretically prove that NSPO preserves the model's original core capabilities, while still guaranteeing a descent direction for effective safety alignment. Extensive experiments demonstrate that NSPO outperforms existing methods by a large margin, achieving state-of-the-art safety performance without sacrificing accuracy on general tasks, including math, code, and instruction-following tasks.
Notably, NSPO is data-efficient and only requires 40% of public human-annotated safety data from PKU-SafeRLHF to achieve promising safety performance, without a large amount of mixed general tasks data in existing alignment methods.

**Abstract (Chinese)**

随着大型语言模型 (LLMs) 越来越多地部署在现实世界应用中，确保其行为与人类价值观、社会规范和伦理原则保持一致变得至关重要。然而，在强化学习 (RL) 下的安全对齐往往会遭受遗忘已学习通用能力的问题，这也被称为对齐税。为了解决这一问题，我们引入了零空间约束策略优化 (NSPO)，这是一种新型 RL 框架，用于 LLM 安全对齐，同时保留其核心能力。安全策略梯度被几何投影到通用任务的零空间中，从而缓解安全对齐税。此外，我们从理论上证明了 NSPO 保留了模型的原始核心能力，同时仍保证了有效安全对齐的下降方向。广泛的实验表明，NSPO 大幅优于现有方法，在不牺牲通用任务（包括数学、代码和指令跟随任务）准确性的前提下，实现了最先进的性能安全性能。

值得注意的是，NSPO 数据高效，仅需 PKU-SafeRLHF 中 40% 的公开人类标注安全数据即可实现有前景的安全性能，而无需现有对齐方法中大量混合通用任务数据。

---

### Multi-objective Large Language Model Alignment with Hierarchical Experts

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhuo Li, Guodong DU, Weiyang Guo, Yigeng Zhou, Xiucheng Li, Wenya Wang, Fangming Liu, Yequan Wang, Deheng Ye, Min Zhang, Jing Li
- **Keywords**: large language model, multi-objective, mixture-of-expert, model fusion
- **OpenReview**: https://openreview.net/forum?id=UhmEdfAk46
- **PDF**: https://openreview.net/pdf?id=UhmEdfAk46

**Abstract**

Aligning large language models (LLMs) to simultaneously satisfy multiple objectives remains a significant challenge, especially given the diverse and often conflicting nature of human preferences. Existing alignment methods struggle to balance trade-offs effectively, often requiring costly retraining or yielding suboptimal results across the Pareto frontier of preferences. In this paper, we introduce HoE (Hierarchical Mixture-of-Experts), a lightweight, parameter-efficient, and plug-and-play approach that eliminates the need for model retraining, while enabling LLMs to adapt across the entire Pareto frontier and accommodate diverse user preferences. In particular, HoE consists of three hierarchical components: LoRA Experts, Router Experts and Weighting Router, reaching optimal Pareto frontiers and achieving a trade-off between parameter size, training cost, and performance. We evaluate HoE across various tasks on 16 objectives and 200 different preferences among 8 benchmarks, demonstrating superior performance over 15 recent baselines.

**Abstract (Chinese)**

将大型语言模型 (LLMs) 与多个目标同时对齐仍是一个重大挑战，特别是鉴于人类偏好的多样性和往往相互冲突的性质。现有的对齐方法难以有效平衡权衡，往往需要昂贵的重新训练，或在偏好的帕累托前沿上产生次优结果。在本文中，我们引入了 HoE（分层专家混合模型），这是一种轻量级、参数高效且即插即用的方法，它消除了模型重新训练的需求，同时使 LLMs 能够在整个帕累托前沿上适应并容纳多样化的用户偏好。特别是，HoE 由三个分层组件组成：LoRA 专家、路由专家和加权路由器，实现最优帕累托前沿，并在参数规模、训练成本和性能之间实现权衡。我们在 8 个基准测试的各种任务上评估了 HoE，涵盖 16 个目标和 200 种不同偏好，展示了其优于 15 个最近基线方法的性能。

---

### Optimas: Optimizing Compound AI Systems with Globally Aligned Local Rewards

- **Venue**: ICLR 2026 Poster
- **Authors**: Shirley Wu, Parth Sarthi, Shiyu Zhao, Aaron Lee, Herumb Shandilya, Adrian Mladenic Grobelnik, Nurendra Choudhary, Edward W Huang, Karthik Subbian, Linjun Zhang, Diyi Yang, James Zou, Jure Leskovec
- **Keywords**: Compound AI System, Heterogenous Configuration, Optimization, Local Rewards
- **OpenReview**: https://openreview.net/forum?id=A3VDbR9arh
- **PDF**: https://openreview.net/pdf?id=A3VDbR9arh

**Abstract**

Compound AI systems integrating multiple components, such as Large Language Models, specialized tools, and traditional machine learning models, are increasingly deployed to solve complex real-world tasks. However, optimizing compound systems remains challenging due to their non-differentiable structures and diverse configuration types across components, including prompts, hyperparameters, and model parameters. To address this challenge, we propose Optimas, a unified framework for effective optimization of compound systems. The core idea of Optimas is to maintain one Local Reward Function (LRF) per component, each satisfying a local–global alignment property, i.e., each component’s local reward correlates with the global system performance. In each iteration, Optimas efficiently adapts the LRFs to maintain this property while simultaneously maximizing each component’s local reward. This approach enables independent updates of heterogeneous configurations using the designated optimization method, while ensuring that local improvements consistently lead to performance gains. We present extensive evaluations across five real-world compound systems to demonstrate that Optimas outperforms strong baselines by an average improvement of 11.92%, offering a general and effective approach for improving compound systems.

**Abstract (Chinese)**

集成多个组件的复合AI系统，例如大型语言模型、专用工具和传统机器学习模型，正日益被部署用于解决复杂的现实世界任务。然而，由于其非可微结构以及组件间多样化的配置类型（包括提示、超参数和模型参数），优化复合系统仍面临挑战。为应对这一挑战，我们提出了Optimas，这是一个用于有效优化复合系统的统一框架。Optimas的核心思想是为每个组件维护一个局部奖励函数（LRF），每个LRF满足局部-全局对齐属性，即每个组件的局部奖励与全局系统性能相关联。在每次迭代中，Optimas高效地调整LRF以维持这一属性，同时最大化每个组件的局部奖励。这种方法使用指定的优化方法独立更新异构配置，同时确保局部改进始终导致性能提升。我们对五个现实世界的复合系统进行了广泛评估，以证明Optimas比强基线平均提升11.92%，提供了一种通用且有效的改进复合系统的方法。

---

### OrthAlign: Orthogonal Subspace Decomposition for Non-Interfering Multi-Objective Alignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Liang Lin, Zhihao Xu, Junhao Dong, Jian Zhao, Yuchen Yuan, Guibin Zhang, Miao Yu, Yiming Zhang, Zhengtao Yao, Huahui Yi, HAICHUAN TANG, Dongrui Liu, Xinfeng Li, Kun Wang
- **Keywords**: alignment
- **OpenReview**: https://openreview.net/forum?id=rO2uXIP019
- **PDF**: https://openreview.net/pdf?id=rO2uXIP019

**Abstract**

Large language model (LLM) alignment faces a critical dilemma when addressing multiple human preferences: improvements in one dimension frequently come at the expense of others, creating unavoidable trade-offs between competing objectives like helpfulness and harmlessness. While prior work mainly focuses on constraint-based optimization algorithms and data selection strategies to mitigate conflicts, these approaches overlook the fundamental issue of resolving conflicts directly at the parameter level. In this paper, we present OrthAlign, an innovative approach that pioneers a new paradigm by leveraging orthogonal subspace decomposition to fundamentally resolve gradient-level conflicts in multi-objective preference alignment. OrthAlign strategically decomposes parameter update spaces into orthogonal subspaces, ensuring that optimization toward different preferences occurs in mathematically non-interfering directions. Building upon this, we provide theoretical guarantees demonstrating that when parameter increments satisfy both orthogonal subspace constraints and spectral norm bounds, the resulting updates exhibit linear Lipschitz growth rather than exponential instability, ensuring stable convergence across all preference dimensions. Extensive experiments show that: I. OrthAlign achieves maximum single-preference improvements ranging from 34.61% to 50.89% after multiple-objective alignment across helpful, harmless, and truthful dimensions. II. With an average overall reward improvement of 13.96%. Our code is available at https://anonymous.4open.science/r/OrthAlign.

**Abstract (Chinese)**

大型语言模型 (LLM) 对齐在处理多个人类偏好时面临一个关键困境：一个维度上的改进往往以牺牲其他维度为代价，在有帮助性和无害性等竞争目标之间造成不可避免的权衡。虽然先前工作主要关注基于约束的优化算法和数据选择策略来缓解冲突，但这些方法忽略了在参数层面直接解决冲突的基本问题。在本文中，我们提出 OrthAlign，一种创新方法，通过利用正交子空间分解开创了一个新范式，从根本上解决多目标偏好对齐中的梯度级冲突。OrthAlign 策略性地将参数更新空间分解为正交子空间，确保针对不同偏好的优化在数学上互不干扰的方向上进行。在此基础上，我们提供了理论保证，证明当参数增量同时满足正交子空间约束和谱范数界时，结果更新表现出线性 Lipschitz 增长而非指数不稳定性，从而确保所有偏好维度上的稳定收敛。广泛的实验表明：I. OrthAlign 在帮助性、无害性和真实性维度上的多目标对齐后，实现单偏好最大改进范围为 34.61% 至 50.89%。II. 平均整体奖励改进为 13.96%。我们的代码可在 https://anonymous.4open.science/r/OrthAlign 获取。

---

### PALC: Preference Alignment via Logit Calibration

- **Venue**: ICLR 2026 Poster
- **Authors**: SANGHYUN LEE, Hoh Peter In
- **Keywords**: AI alignment, Representation Editing
- **OpenReview**: https://openreview.net/forum?id=0cmuYj3WeG
- **PDF**: https://openreview.net/pdf?id=0cmuYj3WeG

**Abstract**

Aligning Large Language Models with human preferences typically requires computationally intensive training or complex reward architectures. We introduce PALC (Preference Alignment via Logit Calibration), a parameter-efficient framework that achieves test-time alignment through a novel intervention strategy: direct calibration in vocabulary space. Unlike existing methods that manipulate entangled hidden representations or rely on external reward models, PALC operates at the logit layer where each dimension corresponds to a distinct token, providing interpretable and efficient control. Our approach employs a bottleneck architecture that learns to compress the base model's hidden states and generate position-dependent calibration vectors, requiring only a fraction of the base model's parameters. Through this design, PALC sidesteps the superposition problem inherent in representation engineering while eliminating the computational overhead of guided decoding methods. A single scaling factor enables runtime adjustment of alignment strength without retraining, allowing practitioners to balance between preserving model capabilities and enforcing preferences. Experiments demonstrate that PALC outperforms most test-time alignment methods while maintaining near-baseline inference speed. Our ablations reveal that human preferences concentrate on surprisingly low-dimensional manifolds, validating our architectural choices. By establishing vocabulary-space intervention as an effective alignment paradigm, PALC makes preference alignment accessible for resource-constrained deployments where traditional methods are infeasible, opening new avenues for scalable and adaptive AI alignment.

**Abstract (Chinese)**

大型语言模型与人类偏好的对齐通常需要计算密集型的训练或复杂的奖励架构。我们引入了PALC（Preference Alignment via Logit Calibration，通过logits校准的偏好对齐），这是一个参数高效的框架，通过一种新型干预策略实现测试时对齐：在词汇空间中进行直接校准。与现有操纵纠缠隐藏表示或依赖外部奖励模型的方法不同，PALC在logits层操作，其中每个维度对应一个独特的标记，提供可解释且高效的控制。我们的方法采用瓶颈架构，学习压缩基础模型的隐藏状态并生成位置相关的校准向量，仅需基础模型参数的一小部分。通过这种设计，PALC避开了表示工程中固有的叠加问题，同时消除了引导解码方法的计算开销。单个缩放因子实现了无需重新训练的运行时对齐强度调整，允许从业者平衡保留模型能力和强制执行偏好。实验表明，PALC在保持接近基线推理速度的同时，优于大多数测试时对齐方法。我们的消融实验揭示，人类偏好集中在令人惊讶的低维流形上，验证了我们的架构选择。通过将词汇空间干预确立为有效的对齐范式，PALC使偏好对齐在资源受限部署中变得可行，而传统方法不可行，从而为可扩展和自适应AI对齐开辟了新途径。

---

### Pragma-VL: Towards a Pragmatic Arbitration of Safety and Helpfulness in MLLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Ming Wen, Kun Yang, Xin Chen, Jingyu Zhang, DINGDING HAN, shiwen cui, Yuedong Xu
- **Keywords**: safety, alignment, MLLM, VLM, safety-helpfulness trade-off
- **OpenReview**: https://openreview.net/forum?id=KwWYvt547M
- **PDF**: https://openreview.net/pdf?id=KwWYvt547M

**Abstract**

Multimodal Large Language Models (MLLMs) pose critical safety challenges, as they are susceptible not only to adversarial attacks such as jailbreaking but also to inadvertently generating harmful content for benign users. While internal safety alignment via Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) is a primary mitigation strategy, current methods often face a safety-utility trade-off: they either refuse benign queries out of excessive caution or overlook latent risks in cross-modal interactions. To resolve this, we introduce Pragma-VL, an end-to-end alignment algorithm that enables MLLMs to pragmatically arbitrate between safety and helpfulness. First, we enhance visual risk perception with a novel cold-start SFT stage. This is achieved by applying risk-aware clustering to the visual encoder and using an interleaved dataset of risk descriptions and high-quality data. Second, we introduce a theoretically-guaranteed reward model that leverages synergistic learning. We train it with a novel data augmentation method that assigns dynamic weights based on the queries, enabling contextual arbitration between safety and helpfulness. Extensive experiments show that Pragma-VL effectively balances safety and helpfulness, outperforming baselines by 5% to 20% on most multimodal safety benchmarks while preserving its general capabilities in areas such as mathematics and knowledge reasoning.

**Abstract (Chinese)**

多模态大语言模型 (MLLMs) 带来了关键的安全挑战，因为它们不仅容易受到诸如越狱等对抗攻击的影响，还可能无意中为良性用户生成有害内容。虽然通过监督微调 (SFT) 和强化学习 (RL) 进行的内部安全对齐是一种主要的缓解策略，但当前方法往往面临安全-效用权衡问题：它们要么出于过度谨慎而拒绝良性查询，要么忽略跨模态交互中的潜在风险。为了解决这一问题，我们引入了 Pragma-VL，这是一种端到端对齐算法，能够使 MLLMs 在安全性和帮助性之间务实地进行仲裁。首先，我们通过一种新型冷启动 SFT 阶段增强视觉风险感知。这通过对视觉编码器应用风险感知聚类，并使用风险描述和高品质数据的交错数据集来实现。其次，我们引入了一种理论保证的奖励模型，该模型利用协同学习。我们使用一种新型数据增强方法对其进行训练，该方法根据查询分配动态权重，从而实现安全性和帮助性之间的上下文仲裁。广泛的实验表明，Pragma-VL 有效地平衡了安全性和帮助性，在大多数多模态安全基准上优于基线 5% 至 20%，同时保留了其在数学和知识推理等领域的通用能力。

---

### RE-PO: Robust Enhanced Policy Optimization as a General Framework for LLM Alignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Xiaoyang Cao, Zelai Xu, Mo Guang, Kaiwen Long, Michiel A. Bakker, Yu Wang, Chao Yu
- **Keywords**: large language model, alignment, robustness
- **OpenReview**: https://openreview.net/forum?id=jDKpOvTCM8
- **PDF**: https://openreview.net/pdf?id=jDKpOvTCM8

**Abstract**

Standard human preference-based alignment methods, such as Reinforcement Learning from Human Feedback (RLHF), are a cornerstone technology for aligning Large Language Models (LLMs) with human values. However, these methods are all underpinned by a strong assumption that the collected preference data is clean and that all observed labels are equally reliable. In reality, large-scale preference datasets contain substantial label noise due to annotator errors, inconsistent instructions, varying expertise, and even adversarial or low-effort feedback. This creates a discrepancy between the recorded data and the ground-truth preferences, which can misguide the model and degrade its performance. To address this challenge, we introduce Robust Enhanced Policy Optimization (RE-PO). RE-PO employs an Expectation-Maximization algorithm to infer the posterior probability of each label’s correctness, which is used to adaptively re-weigh each data point in the training loss to mitigate noise. We further generalize this approach by linking a broad class of preference losses to induced probabilistic models. This enables systematic robustification of existing alignment algorithms while preserving exact probabilistic equivalence for likelihood-style losses. Theoretically, under perfect calibration and a population/full-batch setting, we show that RE-PO recovers the true annotator reliability. Our experiments demonstrate RE-PO’s effectiveness as a general framework, generally enhancing four state-of-the-art alignment algorithms (DPO, IPO, SimPO, and CPO) against their corresponding standard versions. When applied to Mistral and Llama 3 models, the RE-PO-enhanced methods improve AlpacaEval 2 win rates by up to 7.0% over their respective baselines.

**Abstract (Chinese)**

标准人类偏好对齐方法，如基于人类反馈的强化学习（RLHF），是使大型语言模型（LLMs）与人类价值观对齐的基石技术。然而，这些方法均基于一个强假设，即收集到的偏好数据是干净的，且所有观测标签同样可靠。在现实中，大规模偏好数据集由于标注者错误、不一致的指令、不同专业水平，甚至对抗性或低努力反馈而包含大量标签噪声。这导致记录数据与真实偏好之间的差异，可能误导模型并降低其性能。为应对这一挑战，我们引入鲁棒增强策略优化（RE-PO）。RE-PO 采用期望最大化算法推断每个标签正确性的后验概率，并用于自适应地重加权训练损失中的每个数据点以缓解噪声。我们进一步通过将广泛类别的偏好损失链接到诱导概率模型来泛化这一方法。这使得现有对齐算法的系统性鲁棒化，同时为似然式损失保持精确的概率等价性。从理论上，在完美校准和总体/全批次设置下，我们证明 RE-PO 能恢复真实的标注者可靠性。我们的实验证明 RE-PO 作为通用框架的有效性，通常提升了四种最先进对齐算法（DPO、IPO、SimPO 和 CPO）相对于其标准版本的表现。当应用于 Mistral 和 Llama 3 模型时，RE-PO 增强的方法将其各自基线的 AlpacaEval 2 胜率提高了高达 7.0%。

---

### Reasoned Safety Alignment: Ensuring Jailbreak Defense via Answer-Then-Check

- **Venue**: ICLR 2026 Poster
- **Authors**: Chentao Cao, Xiaojun Xu, Bo Han, Hang Li
- **Keywords**: Jailbreak Defense, Safety Alignment, Post-training
- **OpenReview**: https://openreview.net/forum?id=DK6AToxJNo
- **PDF**: https://openreview.net/pdf?id=DK6AToxJNo

**Abstract**

Content Warning: This paper contains examples with harmful content, and the constructed dataset includes samples that may be considered offensive.
As large language models (LLMs) continue to advance in capabilities, ensuring their safety against jailbreak attacks remains a critical challenge. In this paper, we introduce a novel safety alignment approach called Answer-Then-Check, which enhances LLM robustness against malicious prompts by applying thinking ability to mitigate jailbreaking problems before producing a final answer to the user. Our method enables models to answer the question in their thoughts directly and then critically evaluate its safety before deciding whether to provide it. To implement this approach, we construct the Reasoned Safety Alignment (ReSA) dataset, comprising 80K samples that teach models to reason through direct responses and then analyze their safety. Experimental results demonstrate that our approach achieves the Pareto frontier with superior safety capability while decreasing over-refusal rates. Notably, the fine-tuned model maintains general reasoning capabilities on benchmarks like MMLU, MATH500, and HumanEval. Besides, our method equips models with the ability to perform safe completion, while post-hoc detection methods can only directly reject sensitive, harmful queries (e.g., self-harm). Our results show that inference-time strategies alone are insufficient, highlighting the necessity of safety training, and we find even $500$ samples can yield performance comparable to the entire dataset, suggesting a promising path for data-efficient safety alignment. The dataset is publicly available at: https://huggingface.co/datasets/ByteDance-Seed/ReSA.

**Abstract (Chinese)**

内容警告：本文包含有害内容的示例，所构建的数据集包括可能被视为冒犯性的样本。
随着大型语言模型 (LLMs) 能力的不断进步，确保其针对越狱攻击的安全性仍然是一个关键挑战。在本文中，我们提出了一种名为 Answer-Then-Check 的新型安全对齐方法，该方法通过在向用户提供最终答案之前应用思考能力来缓解越狱问题，从而增强 LLM 对恶意提示的鲁棒性。我们的方法使模型能够在思考中直接回答问题，然后在决定是否提供之前对其安全性进行批判性评估。为了实现这一方法，我们构建了推理安全对齐 (ReSA) 数据集，该数据集包含 80K 个样本，用于教导模型通过直接响应进行推理，然后分析其安全性。实验结果表明，我们的方法在提升安全能力的同时降低了过度拒绝率，达到了帕累托前沿。值得注意的是，微调后的模型在 MMLU、MATH500 和 HumanEval 等基准测试上保持了通用推理能力。此外，我们的方法赋予模型进行安全补全的能力，而事后检测方法只能直接拒绝敏感、有害的查询（例如，自残）。我们的结果表明，仅靠推理时策略是不够的，这突显了安全训练的必要性，并且我们发现即使使用 500 个样本，也能获得与整个数据集相当的性能，这为数据高效的安全对齐指明了有前景的路径。数据集可在以下链接公开获取：https://huggingface.co/datasets/ByteDance-Seed/ReSA。

---

### Reasoning Boosts Opinion Alignment in LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Frédéric Berdoz, Yann Billeter, Yann Vonlanthen, Roger Wattenhofer
- **Keywords**: Opinion modeling, Alignement, LLMs, Reasoning
- **OpenReview**: https://openreview.net/forum?id=mdunHhVDPz
- **PDF**: https://openreview.net/pdf?id=mdunHhVDPz

**Abstract**

Opinion modeling aims to capture individual or group political preferences, enabling applications such as digital democracies, where models could help shape fairer and more popular policies. Given their versatility, strong generalization capabilities, and demonstrated success across diverse text-to-text applications, large language models (LLMs) are natural candidates for this task. However, due to their statistical nature and limited causal understanding, they tend to produce biased opinions when prompted naively. In this work, we study whether reasoning can improve opinion alignment. Motivated by the recent advancement in mathematical reasoning enabled by reinforcement learning (RL), we train models to produce profile-consistent answers through structured reasoning. We evaluate our approach on three datasets covering U.S., European, and Swiss politics. Results indicate that reasoning enhances opinion modeling and is competitive with strong baselines, but does not fully remove bias, highlighting the need for additional mechanisms to build faithful political digital twins using LLMs. By releasing both our method and datasets, we establish a solid baseline to support future research on LLM opinion alignment.

**Abstract (Chinese)**

观点建模旨在捕捉个人或群体的政治偏好，从而实现诸如数字民主等应用，在这些应用中，模型可以帮助制定更公平、更受欢迎的政策。鉴于其多功能性、强大的泛化能力以及在各种文本到文本应用中的成功表现，大语言模型（LLMs）是这项任务的自然候选者。然而，由于其统计性质和有限的因果理解，它们在简单提示下往往会产生偏见观点。在这项工作中，我们研究推理是否能改善观点对齐。受强化学习（RL）驱动的数学推理最近进步的启发，我们训练模型通过结构化推理产生与个人资料一致的回答。我们在涵盖美国、欧洲和瑞士政治的三个数据集上评估我们的方法。结果表明，推理提升了观点建模，并与强基线具有竞争力，但并未完全消除偏见，这突显了使用 LLMs 构建忠实政治数字孪生需要额外机制。通过发布我们的方法和数据集，我们为未来的 LLM 观点对齐研究建立了坚实基线。

---

### References Improve LLM Alignment in Non-Verifiable Domains

- **Venue**: ICLR 2026 Poster
- **Authors**: Kejian Shi, Yixin Liu, PeiFeng Wang, Alexander Fabbri, Shafiq Joty, Arman Cohan
- **Keywords**: LLM Alignment; LLM-as-a-Judge; Alignment Evaluation; Preference Optimization
- **OpenReview**: https://openreview.net/forum?id=NoZgrya6Ua
- **PDF**: https://openreview.net/pdf?id=NoZgrya6Ua

**Abstract**

While Reinforcement Learning with Verifiable Rewards (RLVR) has shown strong effectiveness in reasoning tasks, it cannot be directly applied to non-verifiable domains lacking ground-truth verifiers, such as LLM alignment. In this work, we investigate whether high-quality reference outputs can be effectively leveraged to bridge this gap.  First, we design evaluation protocols that enhance LLM-based evaluators for LLM alignment using reference outputs. Through comprehensive experiments, we show that a reference-guided approach substantially improves the accuracy of less capable LLM-judges using references from frontier models; stronger LLM-judges can also be enhanced by human-written references. We then demonstrate the utility of high-quality references in alignment tuning, where LLMs guided with references are used as judges to self-improve. We show that reference-guided self-improvement yields clear gains over both SFT distillation and reference-free baselines, achieving performance comparable to training with finetuned reward models. Specifically, our method achieves scores of 73.1% and 58.7% on AlpacaEval and Arena-Hard with Llama-3-8B-Instruct, and 70.0% and 74.1% with Qwen2.5-7B. These results highlight the potential of using reference-guided LLM-evaluators to enable effective post-training in non-verifiable domains.

**Abstract (Chinese)**

虽然可验证奖励的强化学习（RLVR）在推理任务中展现出强大的有效性，但它无法直接应用于缺乏真实验证器的不可验证领域，例如 LLM 对齐。本工作中，我们探讨高质量参考输出是否能有效桥接这一差距。首先，我们设计了使用参考输出来增强 LLM 对齐的基于 LLM 的评估器的评估协议。通过全面实验，我们展示了参考引导的方法使用前沿模型的参考显著提高了能力较弱的 LLM 评判器的准确性；更强的 LLM 评判器也可以通过人工撰写的参考得到增强。然后，我们展示了高质量参考在对齐调优中的效用，其中使用参考引导的 LLM 被用作评判器进行自我改进。我们展示了参考引导的自我改进相对于 SFT 蒸馏和无参考基线取得了明显的提升，达到了与使用微调奖励模型训练相当的性能。具体而言，我们的方法在 Llama-3-8B-Instruct 上在 AlpacaEval 和 Arena-Hard 上取得了 73.1% 和 58.7% 的分数，在 Qwen2.5-7B 上取得了 70.0% 和 74.1% 的分数。这些结果突出了使用参考引导的 LLM 评估器在不可验证领域实现有效后训练的潜力。

---

### Robust Optimization for Mitigating Reward Hacking with Correlated Proxies

- **Venue**: ICLR 2026 Poster
- **Authors**: Zixuan Liu, Xiaolin Sun, Zizhan Zheng
- **Keywords**: Reward hacking, Robust Reinforcement Learning
- **OpenReview**: https://openreview.net/forum?id=O3shkBWM2s
- **PDF**: https://openreview.net/pdf?id=O3shkBWM2s

**Abstract**

Designing robust reinforcement learning (RL) agents in the presence of imperfect reward signals remains a core challenge. In practice, agents are often trained with proxy rewards that only approximate the true objective, leaving them vulnerable to reward hacking, where high proxy returns arise from unintended or exploitative behaviors. Recent work formalizes this issue using 
r-correlation between proxy and true rewards, but existing methods like occupancy-regularized policy optimization (ORPO) optimize against a fixed proxy and do not provide strong guarantees against broader classes of correlated proxies. In this work, we formulate reward hacking as a robust policy optimization problem over the space of all 
r-correlated proxy rewards. We derive a tractable max-min formulation, where the agent maximizes performance under the worst-case proxy consistent with the correlation constraint. We further show that when the reward is a linear function of known features, our approach can be adapted to incorporate this prior knowledge, yielding both improved policies and interpretable worst-case rewards. Experiments across several environments show that our algorithms consistently outperform ORPO in worst-case returns, and offer improved robustness and stability across different levels of proxy–true reward correlation. These results show that our approach provides both robustness and transparency in settings where reward design is inherently uncertain.

**Abstract (Chinese)**

在存在不完美奖励信号的情况下设计鲁棒的强化学习 (RL) 代理仍然是一个核心挑战。在实践中，代理通常使用仅近似真实目标的代理奖励进行训练，这使得它们容易受到奖励黑客行为的攻击，其中高代理回报来自于意外或剥削性的行为。最近的工作使用代理奖励与真实奖励之间的 r-相关性来形式化这个问题，但现有的方法如占用正则化策略优化 (ORPO) 是针对固定的代理进行优化的，并不能针对更广泛的相关代理类别提供强有力的保证。在本工作中，我们将奖励黑客行为形式化为在所有 r-相关代理奖励空间上的鲁棒策略优化问题。我们推导了一个可处理的 max-min 公式化，其中代理在与相关性约束一致的最坏情况代理下最大化性能。我们进一步证明，当奖励是已知特征的线性函数时，我们的方法可以适应以纳入这一先验知识，从而产生改进的策略和可解释的最坏情况奖励。在多个环境中的实验表明，我们的算法在最坏情况回报上始终优于 ORPO，并在不同水平的代理-真实奖励相关性下提供了改进的鲁棒性和稳定性。这些结果表明，我们的方法在奖励设计本质上不确定的设置中提供了鲁棒性和透明度。

---

### Robust Preference Alignment via Directional Neighborhood Consensus

- **Venue**: ICLR 2026 Poster
- **Authors**: Ruochen Mao, Yuling Shi, Xiaodong Gu, Jiaheng Wei
- **Keywords**: Large Language Models, Preference Alignment, Inference-Time Method
- **OpenReview**: https://openreview.net/forum?id=jz41Oh9eV1
- **PDF**: https://openreview.net/pdf?id=jz41Oh9eV1

**Abstract**

Aligning large language models with human preferences is critical for creating
reliable and controllable AI systems. A human preference can be visualized as a
high-dimensional vector where different directions represent trade-offs between
desired attributes (e.g., helpfulness vs. verbosity). Yet, because the training data
often reflects dominant, average preferences, LLMs tend to perform well on com-
mon requests but falls short in specific, individual needs. This mismatch creates
a preference coverage gap. Existing methods often address this through costly
retraining, which may not be generalized to the full spectrum of diverse preferences.
This brittleness means that when a user’s request reflects a nuanced preference
deviating from the training data’s central tendency, model performance can degrade
unpredictably. To address this challenge, we introduce Robust Preference Selection
(RPS), a post-hoc, training-free method by leveraging directional neighborhood
consensus. Instead of forcing a model to generate a response from a single, highly
specific preference, RPS samples multiple responses from a local neighborhood
of related preferences to create a superior candidate pool. It then selects the re-
sponse that best aligns with the user’s original intent. We provide a theoretical
framework showing that, under mild conditions where (i) nearby preference direc-
tions correspond to better-trained regions of the model and (ii) the reward-model
scores change smoothly with small angular changes in the preference vector, our
neighborhood generation strategy yields a higher expected best score than a strong
baseline that also samples multiple candidates. Comprehensive experiments across
three distinct alignment paradigms (DPA, DPO, and SFT) demonstrate that RPS
consistently improves robustness against this baseline, achieving win rates of up
to 69% on challenging preferences from under-represented regions of the space
without any model retraining. Our work presents a practical, theoretically-grounded
solution for enhancing the reliability of preference-aligned models.

**Abstract (Chinese)**

将大型语言模型与人类偏好对齐对于创建可靠且可控的AI系统至关重要。人类偏好可以可视化为一个高维向量，其中不同方向代表期望属性之间的权衡取舍（例如，有用性与冗长性）。然而，由于训练数据往往反映主导的、平均偏好，大型语言模型（LLMs）在常见请求上表现良好，但在特定个体需求上则表现不足。这种不匹配导致了偏好覆盖差距。现有的方法通常通过昂贵的重新训练来解决这一问题，但这些方法可能无法泛化到多样化偏好的全谱系。这种脆弱性意味着，当用户的请求反映出偏离训练数据中心趋势的细微偏好时，模型性能可能会不可预测地下降。为应对这一挑战，我们引入了鲁棒偏好选择（RPS），这是一种后验、无需训练的方法，通过利用方向邻域共识来实现。与强迫模型从单一高度特定的偏好生成响应不同，RPS从相关偏好的局部邻域中采样多个响应，以创建优越的候选池，然后选择最符合用户原始意图的响应。我们提供了一个理论框架，证明在温和条件下——即（i）附近偏好方向对应于模型中训练较好的区域，且（ii）奖励模型分数随着偏好向量的微小角度变化而平滑变化——我们的邻域生成策略比同样采样多个候选的强基线产生更高的期望最佳分数。在三种不同的对齐范式（DPA、DPO和SFT）上的全面实验表明，RPS相对于该基线持续提升鲁棒性，在空间中欠代表区域的挑战性偏好上实现了高达69%的胜率，且无需任何模型重新训练。本工作提出了一种实用且理论基础坚实的解决方案，以提升偏好对齐模型的可靠性。

---

### Swap-guided Preference Learning for Personalized Reinforcement Learning from Human Feedback

- **Venue**: ICLR 2026 Poster
- **Authors**: Gihoon Kim, Euntai Kim
- **Keywords**: Ranking and Preference Learning, Latent Variable Models
- **OpenReview**: https://openreview.net/forum?id=nc28mSbyVG
- **PDF**: https://openreview.net/pdf?id=nc28mSbyVG

**Abstract**

Reinforcement Learning from Human Feedback (RLHF) is a widely used approach to align large-scale AI systems with human values. However, RLHF typically assumes a single, universal reward, which overlooks diverse preferences and limits personalization. Variational Preference Learning (VPL) seeks to address this by introducing user-specific latent variables. Despite its promise, we found that VPL suffers from posterior collapse. While this phenomenon is well known in VAEs, it has not previously been identified in preference learning frameworks. Under sparse preference data and with overly expressive decoders, VPL may cause latent variables to be ignored, reverting to a single-reward model. To overcome this limitation, we propose Swap-guided Preference Learning (SPL). The key idea is to construct fictitious swap annotators and use the mirroring property of their preferences to guide the encoder. SPL introduces three components: (1) swap-guided base regularization, (2) Preferential Inverse Autoregressive Flow (P-IAF), and (3) adaptive latent conditioning. Experiments show that SPL mitigates collapse, enriches user-specific latents, and improves preference prediction. Our code and data are available at https://github.com/cobang0111/SPL

**Abstract (Chinese)**

人类反馈强化学习 (RLHF) 是一种广泛用于将大规模 AI 系统与人类价值观对齐的方法。然而，RLHF 通常假设单一的通用奖励，这忽略了多样化的偏好并限制了个性化。变分偏好学习 (VPL) 通过引入用户特定的潜在变量来解决这一问题。尽管其前景广阔，我们发现 VPL 存在后验崩溃问题。虽然这一现象在变分自编码器 (VAEs) 中广为人知，但此前尚未在偏好学习框架中被识别。在稀疏偏好数据和过于表达力的解码器下，VPL 可能导致潜在变量被忽略，从而退化为单一奖励模型。为克服这一局限性，我们提出交换引导偏好学习 (SPL)。其核心思想是构建虚构的交换标注者，并利用其偏好的镜像属性来引导编码器。SPL 引入了三个组件：(1) 交换引导基础正则化，(2) 偏好逆自回归流 (P-IAF)，以及 (3) 自适应潜在条件化。实验表明，SPL 缓解了崩溃问题，丰富了用户特定的潜在变量，并提升了偏好预测性能。我们的代码和数据可在 https://github.com/cobang0111/SPL 获取。

---

### Teach to Reason Safely: Policy-Guided Safety Tuning for MLRMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Jingyu Zhang, Kun Yang, Ming Wen, Zhuoer Xu, Zeyang Sha, shiwen cui, Zhaohui Yang
- **Keywords**: MLRM, safety, alignment, safety-helpfulness trade-off
- **OpenReview**: https://openreview.net/forum?id=cgy4i74Dq7
- **PDF**: https://openreview.net/pdf?id=cgy4i74Dq7

**Abstract**

Multimodal Large Reasoning Models (MLRMs) have exhibited remarkable capabilities in complex multimodal tasks.
However, our findings reveal a critical trade-off: reasoning-based models are more prone to generating harmful content, leading to degradation in safety performance.
This paper presents a large-scale analysis of this safety–reasoning trade-off, identifying two main mechanisms of safety degradation: (i) visual attention drift, which reduces the model’s reliance on visual grounding and thereby exacerbates overlooked risks in cross-modal interactions; (ii) unsafe reasoning patterns, including flawed reasoning initiation and chain-of-thought safety attenuation, which compromise the model’s safety awareness.
To mitigate these issues, we propose **P**olicy-guided **S**afety **T**uning (**PST**), a two-stage alignment framework. It first employs *Policy-Guided Supervised Fine-Tuning* to integrate explicit safety policies into the reasoning process, establishing a structured and interpretable foundation for safe decision-making. 
Then, PST applies *Safety Reasoning Preference Optimization* to encourage the model to generate safe, helpful, and informative responses while reducing oversensitive  and homogeneous characteristics.
Extensive experiments demonstrate that PST significantly reduces harmful outputs across multiple multimodal safety benchmarks, while maintaining competitive performance on general tasks.

**Abstract (Chinese)**

多模态大推理模型（MLRMs）在复杂多模态任务中展现出卓越的能力。然而，我们的研究发现存在一个关键权衡：基于推理的模型更容易生成有害内容，从而导致安全性能下降。

本文对这一安全-推理权衡进行了大规模分析，识别出安全性能下降的两种主要机制：(i) 视觉注意力漂移，该机制减少了模型对视觉 grounding 的依赖，从而加剧了跨模态交互中被忽略的风险；(ii) 不安全推理模式，包括有缺陷的推理启动和思维链安全衰减，这些模式损害了模型的安全意识。

为缓解这些问题，我们提出**P**olicy-guided **S**afety **T**uning（**PST**），一个两阶段对齐框架。它首先采用*策略引导的监督微调*，将明确的策略安全规则整合到推理过程中，为安全决策建立结构化和可解释的基础。

然后，PST 应用*安全推理偏好优化*，鼓励模型生成安全、有帮助且信息丰富的响应，同时减少过度敏感和同质化特征。

大量实验表明，PST 在多个多模态安全基准上显著减少有害输出，同时在一般任务上保持竞争性性能。

---

### The Alignment Waltz: Jointly Training Agents to Collaborate for Safety

- **Venue**: ICLR 2026 Poster
- **Authors**: Jingyu Zhang, Haozhu Wang, Eric Michael Smith, Sid Wang, Amr Sharaf, Mahesh Pasupuleti, Benjamin Van Durme, Daniel Khashabi, Jason E Weston, Hongyuan Zhan
- **Keywords**: safety alignment, multi-agent reinforcement learning
- **OpenReview**: https://openreview.net/forum?id=2NBS9ilNqM
- **PDF**: https://openreview.net/pdf?id=2NBS9ilNqM

**Abstract**

Harnessing the power of LLMs requires a delicate dance between being helpful and harmless, leading to two critical challenges: vulnerability to adversarial attacks that elicit unsafe content, and a tendency for overrefusal on benign but sensitive prompts. Current approaches often navigate this dance with safeguard models that completely reject any content that contains unsafe portions. This approach cuts the metaphorical music entirely—it may exacerbate overrefusals and fails to provide nuanced guidance for queries it refuses. To teach models a more coordinated choreography, we propose WaltzRL, a novel multi-agent reinforcement learning framework that formulates safety alignment as a collaborative, positive-sum game. WaltzRL jointly trains a conversation agent and a feedback agent, where the latter is incentivized to provide useful suggestions that improve the safety and helpfulness of the conversation agent's responses. 
At the core of WaltzRL is a Dynamic Improvement Reward (DIR) that evolves over time based on how well the conversation agent incorporates the feedback. At inference time, unsafe responses or overrefusals from the conversation agent are improved rather than discarded. The feedback agent is deployed together with the conversation agent and only engages adaptively when needed, preserving helpfulness and low latency on safe queries. Our experiments, conducted across five diverse datasets, demonstrate that WaltzRL significantly reduces both unsafe responses (e.g., from 39.0% to 4.6% on WildJailbreak) and overrefusals (from 45.3% to 9.9% on OR-Bench) compared to various baselines. By enabling the conversation and feedback agents to co-evolve and adaptively apply feedback, WaltzRL enhances LLM safety without degrading general capabilities, thereby advancing the Pareto front between helpfulness and harmlessness.

**Abstract (Chinese)**

利用大语言模型（LLMs）的强大能力需要在有益性和无害性之间进行精妙的平衡，这引发了两个关键挑战：易受对抗攻击诱发不安全内容的漏洞，以及对良性但敏感提示的过度拒绝倾向。现有的方法通常通过安全防护模型来应对这一平衡，这些模型会完全拒绝任何包含不安全部分的响应。这种方法相当于彻底切断隐喻中的音乐——它可能加剧过度拒绝，并无法为拒绝的查询提供细致指导。为了训练模型进行更协调的“舞蹈”，我们提出WaltzRL，这是一种新颖的多代理强化学习框架，将安全对齐表述为一种协作的正和博弈。WaltzRL联合训练一个对话代理和一个反馈代理，其中后者被激励提供有益建议，以提升对话代理响应的安全性和有益性。

WaltzRL的核心是一个动态改进奖励（Dynamic Improvement Reward, DIR），该奖励会根据对话代理采纳反馈的程度而随时间演化。在推理时，对话代理的不安全响应或过度拒绝不会被丢弃，而是得到改进。反馈代理与对话代理一同部署，仅在需要时自适应介入，从而在安全查询上保持有益性和低延迟。我们在五个多样化数据集上的实验表明，与各种基线相比，WaltzRL显著降低了不安全响应比例（例如，在WildJailbreak上从39.0%降至4.6%）和过度拒绝比例（在OR-Bench上从45.3%降至9.9%）。通过使对话代理和反馈代理共同演化和自适应应用反馈，WaltzRL在不降低通用能力的前提下提升了LLM的安全性，从而推进了有益性和无害性之间的帕累托前沿。

---

### Thinking as Society: Multi-Social-Agent Self-Distillation for Multimodal Misinformation Detection

- **Venue**: ICLR 2026 Poster
- **Authors**: Yifei Gao, Ning Xu, Wenhui Li, Hongshuo Tian, Lanjun Wang, Anan Liu
- **Keywords**: Multimodal Misinformation Detection, Multimodal Large Language Models, Multi-Social-Agent Self-Distillation
- **OpenReview**: https://openreview.net/forum?id=nHW64r5KFG
- **PDF**: https://openreview.net/pdf?id=nHW64r5KFG

**Abstract**

Multimodal Misinformation Detection (MMD) in realistic, mixed-sourced scenarios must incorporate robust reasoning capabilities to handle the social complexity and diverse types of forgeries. While MLLM-based agents are increasingly used for MMD task due to their powerful reasoning abilities, they suffer from a critical trade-off: on one hand, single-agent methods provide only the limited, single-view analysis; on the other hand, multi-agent methods introduce high computational costs and significant optimization difficulties. To address this gap, we propose a novel Multi-Social-Agent Self-Distillation framework that internalizes collective social reasoning capabilities into a unified model. Our framework consists of two core stages: (1) we simulate multi-perspective judgments from a diverse society of MLLM agents and synthesize their collective feedback into high-quality Social Chain-of-Thought (SCoT) data; (2) Building on this, we propose the Social Correction Value-Driven Preference Optimization (SCPO), a new alignment algorithm that leverages the degree of social misjudgment as a verifiable signal to dynamically focus training on the most challenging samples. Extensive experiments on the challenging MFC-Bench and MMFakeBench benchmarks demonstrate the effectiveness of our framework. Our 7B Qwen2-VL-based model significantly outperforms various MLLM baselines, multi-agent methods, and even competes or surpasses proprietary models like GPT-4o and Claude, facilitating advanced multimodal misinformation reasoning and detection via thinking as society.

**Abstract (Chinese)**

在现实的混合来源场景中，多模态虚假信息检测（MMD）必须融入强大的推理能力，以处理社会复杂性和多种类型的伪造。虽然基于多模态大语言模型（MLLM）的代理因其强大的推理能力而日益用于MMD任务，但它们存在一个关键权衡：一方面，单代理方法仅提供有限的单视角分析；另一方面，多代理方法引入了高计算成本和显著的优化难度。为填补这一空白，我们提出了一种新颖的多社会代理自蒸馏框架，该框架将集体社会推理能力内化到一个统一的模型中。我们的框架由两个核心阶段组成：（1）我们模拟来自多样化MLLM代理社会的多视角判断，并将它们的集体反馈合成高质量的社会思维链（SCoT）数据；（2）在此基础上，我们提出社会校正值驱动的偏好优化（SCPO），这是一种新的对齐算法，它利用社会误判程度作为可验证信号，动态地将训练焦点集中在最具挑战性的样本上。在具有挑战性的MFC-Bench和MMFakeBench基准上的广泛实验证明了我们框架的有效性。我们基于7B Qwen2-VL的模型显著优于各种MLLM基线、多代理方法，甚至与专有模型如GPT-4o和Claude竞争或超越，通过“像社会一样思考”促进高级多模态虚假信息推理和检测。

---

### Towards Cognitively-Faithful Decision-Making Models to Improve AI Alignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Cyrus Cousins, Vijay Keswani, Vincent Conitzer, Hoda Heidari, Jana Schaich Borg, Walter Sinnott-Armstrong
- **Keywords**: Human-Centric AI, Moral Preference Elicitation, Axiomatic Analysis, Interpretable Machine Learning
- **OpenReview**: https://openreview.net/forum?id=ziP9zetlLp
- **PDF**: https://openreview.net/pdf?id=ziP9zetlLp

**Abstract**

Recent AI trends seek to align AI models to learned human-centric objectives, such as personal preferences, utility, or societal values. Using standard preference elicitation methods, researchers and practitioners build models of human decisions and judgments, to which AI models are aligned. However, standard elicitation methods often fail to capture the true cognitive processes behind human decision making, such as the use of heuristics or simplifying structured thought patterns. To address this limitation, we take an axiomatic approach to learning cognitively faithful decision processes from pairwise comparisons. Building on the vast literature characterizing cognitive processes that contribute to human decision-making and pairwise comparisons, we derive a class of models in which individual features are first processed with learned rules, then aggregated via a fixed rule, such as the Bradley-Terry rule, to produce a decision. This structured processing of information ensures that such models are realistic and feasible candidates to represent underlying human decision-making processes. We demonstrate the efficacy of this modeling approach by learning interpretable models of human decision making in a kidney allocation task, and show that our proposed models match or surpass the accuracy of prior models of human pairwise decision-making.

**Abstract (Chinese)**

最近的 AI 趋势旨在将 AI 模型与学习到的以人为本的目标对齐，例如个人偏好、效用或社会价值观。使用标准的偏好引出方法，研究人员和从业者构建人类决策和判断的模型，并将 AI 模型与之对齐。然而，标准的引出方法往往无法捕捉人类决策背后的真实认知过程，例如启发式的使用或简化的结构化思维模式。为了解决这一局限性，我们采用一种公理化方法，从成对比较中学习认知上忠实的决策过程。基于大量表征有助于人类决策的认知过程以及成对比较的文献，我们推导出一类模型，其中单个特征首先通过学习规则进行处理，然后通过固定规则（如 Bradley-Terry 规则）聚合，以产生决策。这种信息结构化处理确保此类模型是代表底层人类决策过程的现实且可行的候选模型。我们通过在肾脏分配任务中学习人类决策的可解释模型，展示了这种建模方法的有效性，并表明我们提出的模型在准确性上匹配或超越了先前人类成对决策模型。

---

### Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention

- **Venue**: ICLR 2026 Poster
- **Authors**: Yichi Zhang, Yue Ding, Jingwen Yang, Tianwei Luo, Dongbai Li, Ranjie Duan, Qiang Liu, Hang Su, Yinpeng Dong, Jun Zhu
- **Keywords**: Large Reasoning Model, Safety Alignment
- **OpenReview**: https://openreview.net/forum?id=2uTxLC4LmC
- **PDF**: https://openreview.net/pdf?id=2uTxLC4LmC

**Abstract**

Although Large Reasoning Models (LRMs) have progressed in solving complex problems, their chain-of-thought (CoT) reasoning often contains harmful content that can persist even when the final responses appear safe. We show that this issue still remains in existing methods which overlook the unique significance of safe reasoning, undermining their trustworthiness and posing potential risks in applications if unsafe reasoning is accessible for and exploited by malicious users. We therefore shift our focus to aligning the safety of reasoning itself in this paper and explore process supervision as the solution. However, simply rewarding safe reasoning proves inadequate due to low rollout diversity and limited training signals. To tackle this challenge, we first delve into the characteristics of safe reasoning and uncover several critical insights that 1) safe reasoning is often consolidated by a few critical steps of _safety triggers_; 2) _compliance cues_ strongly correlate with unsafe continuations; and 3) corrective interventions reliably steer unsafe trajectories towards safer traces. Motivated by these, we propose **Intervened Preference Optimization (IPO)**, an alignment method that enforces safe reasoning by substituting compliance steps with safety triggers and constructing pairs for preference learning with strong signals. Experiments on jailbreak and adversarial safety benchmarks demonstrate that IPO remarkably improves overall safety regarding both reasoning and responses, outperforming SFT-based and RL-based baselines with a relative reduction of over 30\% in harmfulness, while preserving excellent performance across diverse reasoning tasks. The results highlight the importance of explicit alignment for reasoning and provide a practical path to safer LRMs.

**Abstract (Chinese)**

尽管大推理模型 (LRMs) 在解决复杂问题方面取得了进展，但它们的思维链 (CoT) 推理常常包含有害内容，即使最终响应看似安全，这种有害内容仍可能持续存在。我们表明，现有的方法忽略了安全推理的独特重要性，这一问题依然存在，这削弱了它们的可信度，并在不安全推理可被恶意用户访问和利用时，在应用中带来潜在风险。因此，本文将重点转向对推理本身的安全性进行对齐，并探索过程监督作为解决方案。然而，仅仅奖励安全推理是不够的，因为 rollout 多样性低且训练信号有限。为了应对这一挑战，我们首先深入探讨安全推理的特征，并揭示了几个关键洞见：1) 安全推理通常由少数关键的_安全触发器_步骤巩固；2) _顺从提示_与不安全延续强烈相关；3) 纠正干预可靠地将不安全轨迹引导向更安全的轨迹。受此启发，我们提出了**干预偏好优化 (IPO)**，这是一种对齐方法，通过用安全触发器替换顺从步骤，并构建具有强信号的偏好学习对来强制执行安全推理。在越狱和对抗性安全基准上的实验表明，IPO 在推理和响应两方面的整体安全性上取得了显著提升，优于基于 SFT 和 RL 的基线，有害性相对减少超过 30%，同时在各种推理任务上保持了出色的性能。结果突显了对推理进行显式对齐的重要性，并为更安全的 LRMs 提供了实用路径。

---

### Towards Understanding Subliminal Learning: When and How Hidden Biases Transfer

- **Venue**: ICLR 2026 Poster
- **Authors**: Simon Schrodi, Elias Kempf, Fazl Barez, Thomas Brox
- **Keywords**: subliminal learning, hidden bias transfer, LLMs, finetuning, distillation, alignment, safety
- **OpenReview**: https://openreview.net/forum?id=IelhmYSjPt
- **PDF**: https://openreview.net/pdf?id=IelhmYSjPt

**Abstract**

Language models can transfer hidden biases during distillation. For example, a teacher that "likes owls" can make its student "like owls" too, even when the training data consists only of lists of numbers. This surprising phenomenon is called *subliminal learning*. Subliminal learning can be expected under soft distillation, where the student is trained on the teacher's full next-token distribution. But the fact that this also occurs under hard distillation—where the student only sees sampled tokens—raises a deeper question: *when and how does subliminal learning actually occur?* We answer this question through controlled experiments and mechanistic analysis. Our results show that subliminal learning does not need (global) token entanglement or logit leakage. Instead, it comes down to a small set of *divergence tokens*—rare cases where teachers with different biases would predict different tokens. Masking out these tokens mostly removes the hidden bias transfer. Mechanistically, divergence tokens reveal that early layers are critical. Surprisingly, finetuning even a single such early layer is sufficient for subliminal learning. Finally, we find that subliminal learning is fragile. Even small changes, like prompt paraphrasings, are usually sufficient to suppress it.

**Abstract (Chinese)**

语言模型在蒸馏过程中可以转移隐藏偏见。例如，一个“喜欢猫头鹰”的教师模型可以使其学生模型也“喜欢猫头鹰”，即使训练数据仅由数字列表组成。这一令人惊讶的现象被称为*subliminal learning*（潜意识学习）。在软蒸馏下，潜意识学习是可以预期的，其中学生模型在教师模型的完整下一个标记分布上进行训练。但这一现象在硬蒸馏下也发生——学生模型仅看到采样标记——引发了一个更深层的问题：*潜意识学习究竟何时以及如何发生？*我们通过控制实验和机制分析回答了这个问题。我们的结果表明，潜意识学习并不需要（全局）标记纠缠或logits泄漏。相反，它归结为一小组*发散标记*——教师模型具有不同偏见时会预测不同标记的罕见情况。屏蔽这些标记大多可以消除隐藏偏见转移。从机制上讲，发散标记揭示了早期层至关重要。令人惊讶的是，即使微调单个这样的早期层也足以实现潜意识学习。最后，我们发现潜意识学习是脆弱的。即使是小的变化，如提示改述，通常也足以抑制它。

---

### Truthful or Fabricated? Using Causal Attribution to Mitigate Reward Hacking in Explanations

- **Venue**: ICLR 2026 Poster
- **Authors**: Pedro Lobato Ferreira, Wilker Aziz, Ivan Titov
- **Keywords**: Large language models, reward hacking, alignment
- **OpenReview**: https://openreview.net/forum?id=nkdPLuKoL5
- **PDF**: https://openreview.net/pdf?id=nkdPLuKoL5

**Abstract**

Chain-of-thought explanations are widely used to inspect the decision process of large language models (LLMs) and to evaluate the trustworthiness of model outputs, making them important for effective collaboration between LLMs and humans. We demonstrate that preference optimization -- a key step in the alignment phase -- can inadvertently reduce the faithfulness of these explanations. This occurs because the reward model (RM), which guides alignment, is tasked with optimizing both the expected quality of the response and the appropriateness of the explanations (e.g., minimizing bias or adhering to safety standards), creating potential conflicts. The RM lacks a mechanism to assess the consistency between the model’s internal decision process and the generated explanation. Consequently, the LLM may engage in ``reward hacking'' by producing a final response that scores highly while giving an explanation tailored to maximize reward rather than accurately reflecting its reasoning. To address this issue, we propose enriching the RM’s input with a causal attribution of the prediction, allowing the RM to detect discrepancies between the generated self-explanation and the model's decision process. In controlled settings, we show that this approach reduces the tendency of the LLM to generate misleading explanations.

**Abstract (Chinese)**

思维链解释被广泛用于检查大型语言模型（LLMs）的决策过程，并评估模型输出的可信度，这使得它们对于LLMs与人类之间的有效协作至关重要。我们证明，偏好优化——对齐阶段的关键步骤——可能会无意中降低这些解释的忠实度。这是因为指导对齐的奖励模型（RM）被要求同时优化响应的预期质量和解释的适当性（例如，减少偏见或遵守安全标准），从而产生潜在冲突。RM缺乏评估模型内部决策过程与生成解释之间一致性的机制。因此，LLM可能会通过产生高分最终响应，同时提供旨在最大化奖励而非准确反映其推理的解释，来进行“奖励黑客”行为。为解决这一问题，我们提出通过为RM的输入添加预测的因果归因，从而使RM能够检测生成的自解释与模型决策过程之间的差异。在受控设置中，我们展示了这种方法减少了LLM生成误导性解释的倾向。

---

### Uni-DPO: A Unified Paradigm for Dynamic Preference Optimization of LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Shangpin Peng, Weinong Wang, Zhuotao Tian, Senqiao Yang, Xing W, Haotian Xu, Chengquan Zhang, Takashi Isobe, Baotian Hu, Min Zhang
- **Keywords**: Deep Learning, Large Language Model, Preference Learning
- **OpenReview**: https://openreview.net/forum?id=G7DBGlgjjp
- **PDF**: https://openreview.net/pdf?id=G7DBGlgjjp

**Abstract**

Direct Preference Optimization (DPO) has emerged as a cornerstone of reinforcement learning from human feedback (RLHF) due to its simplicity and efficiency. However, existing DPO-based methods typically treat all preference pairs equally, overlooking substantial variations in data quality and learning difficulty, which leads to inefficient data utilization and suboptimal performance. To address this limitation, we propose **Uni-DPO**, a unified dynamic preference optimization framework that jointly considers (a) the inherent quality of preference pairs and (b) the model's evolving performance during training. By adaptively reweighting samples based on both factors, Uni-DPO enables more effective use of preference data and achieves superior performance. Extensive experiments across models and benchmarks demonstrate the effectiveness and generalization of Uni-DPO. On textual tasks, Gemma-2-9B-IT fine-tuned with Uni-DPO surpasses the leading LLM, Claude 3 Opus, by 6.7 points on Arena-Hard. On mathematical and multimodal tasks, Uni-DPO consistently outperforms baseline methods across all benchmarks, providing strong empirical evidence of its effectiveness and robustness.

**Abstract (Chinese)**

直接偏好优化 (DPO) 因其简单性和高效性，已成为人类反馈强化学习 (RLHF) 的基石。然而，现有的基于 DPO 的方法通常平等对待所有偏好对，忽略了数据质量和学习难度的显著差异，这导致数据利用效率低下和性能次优。为解决这一局限性，我们提出了 **Uni-DPO**，这是一个统一的动态偏好优化框架，它联合考虑 (a) 偏好对的固有质量和 (b) 训练过程中模型的演进性能。通过基于这两个因素自适应地重新加权样本，Uni-DPO 实现了更有效的偏好数据利用，并取得了优越的性能。跨模型和基准的广泛实验证明了 Uni-DPO 的有效性和泛化能力。在文本任务上，使用 Uni-DPO 微调的 Gemma-2-9B-IT 在 Arena-Hard 上超越领先的大语言模型 Claude 3 Opus 6.7 个百分点。在数学和多模态任务上，Uni-DPO 在所有基准上持续优于基线方法，为其有效性和鲁棒性提供了强有力的实证证据。

---

### Unifying Stable Optimization and Reference Regularization in RLHF

- **Venue**: ICLR 2026 Poster
- **Authors**: Li He, Qiang Qu, He Zhao, Stephen Wan, Dadong Wang, Lina Yao, Tongliang Liu
- **Keywords**: RLHF, LLM, Alignment
- **OpenReview**: https://openreview.net/forum?id=QpqBqCTtW4
- **PDF**: https://openreview.net/pdf?id=QpqBqCTtW4

**Abstract**

Reinforcement Learning from Human Feedback (RLHF) has advanced alignment capabilities significantly but remains hindered by two core challenges: reward hacking and stable optimization. Current solutions independently address these issues through separate regularization strategies, specifically a KL-divergence penalty against a supervised fine-tuned model ($\pi_0$) to mitigate reward hacking, and policy ratio clipping towards the current policy ($\pi_t$) to promote stable alignment. However, the implicit trade-off arising from simultaneously regularizing towards both $\pi_0$ and $\pi_t$ remains under-explored. In this paper, we introduce a unified regularization approach that explicitly balances the objectives of preventing reward hacking and maintaining stable policy updates. Our simple yet principled alignment objective yields a weighted supervised fine-tuning loss with a superior trade-off, which demonstrably improves both alignment results and implementation complexity. Extensive experiments across diverse benchmarks validate that our method consistently outperforms RLHF and online preference learning methods, achieving enhanced alignment performance and stability.

**Abstract (Chinese)**

人类反馈强化学习（RLHF）显著提升了对齐能力，但仍受两大核心挑战的阻碍：奖励黑客行为和稳定优化。现有的解决方案通过独立的正则化策略分别应对这些问题，具体包括针对监督微调模型（$\pi_0$）的 KL 散度惩罚以缓解奖励黑客行为，以及针对当前策略（$\pi_t$）的策略比率裁剪以促进稳定对齐。然而，同时向 $\pi_0$ 和 $\pi_t$ 正则化的隐含权衡仍未得到充分探索。本文提出了一种统一的正则化方法，该方法明确平衡了防止奖励黑客行为和维持稳定策略更新的目标。我们简单却有原则的对齐目标产生了一种加权监督微调损失，具有优越的权衡，从而显著改善了对齐结果和实现复杂度。在多样化基准上的广泛实验验证了我们的方法始终优于 RLHF 和在线偏好学习方法，实现了增强的对齐性能和稳定性。

---

### Weak-to-Strong Generalization with Failure Trajectories

- **Venue**: ICLR 2026 Poster
- **Authors**: Ruimeng Ye, Zihan Wang, Yang Xiao, Zinan Ling, Manling Li, Bo Hui
- **Keywords**: Weak-to-Strong Generalization
- **OpenReview**: https://openreview.net/forum?id=TXZ54qxdAF
- **PDF**: https://openreview.net/pdf?id=TXZ54qxdAF

**Abstract**

Weak-to-Strong generalization (W2SG) is a new trend to elicit the full capabilities of a strong model with supervision from a weak model. While existing W2SG studies focus on simple tasks like binary classification, we extend this paradigm to complex interactive decision-making environments.  
Specifically, we fine-tune a strong model with trajectories of intermediate actions generated by a weak model. Motivated by the human learning process, we propose to generalize not only successful knowledge but also failed experiences so that the strong model can learn from the failed trajectories accumulated by weak models. To effectively and efficiently elicit the potential of strong agents, we further construct ``trajectory trees," a hierarchical representation that organizes weak model-generated action trajectories, coupled with Monte Carlo Tree Search (MCTS) to optimize the strong model. Through theoretical analysis, we provide formal guarantees for the effectiveness of our method in improving W2SG performance. Our empirical evaluations demonstrate substantial improvements in reasoning and decision-making capabilities across diverse task domains, validating the scalability and robustness of our proposed framework. Our code is available at: https://github.com/yeruimeng/TraTree.git.

**Abstract (Chinese)**

弱到强泛化（W2SG）是一种新兴趋势，通过弱模型的监督来激发强模型的全部能力。虽然现有W2SG研究关注简单任务如二元分类，但我们将这一范式扩展到复杂的交互式决策环境。具体而言，我们使用弱模型生成的中间动作轨迹来微调强模型。受人类学习过程的启发，我们提出不仅泛化成功知识，还泛化失败经验，以便强模型能够从弱模型积累的失败轨迹中学习。为了有效高效地激发强代理的潜力，我们进一步构建“轨迹树”，这是一种分层表示，用于组织弱模型生成的动作轨迹，并结合蒙特卡洛树搜索（MCTS）来优化强模型。通过理论分析，我们为我们的方法在提升W2SG性能方面的有效性提供了形式化保证。我们的实证评估展示了在各种任务领域中推理和决策能力的显著提升，验证了我们所提框架的可扩展性和鲁棒性。我们的代码可在以下地址获取：https://github.com/yeruimeng/TraTree.git。

---

### What Do Large Language Models Know About Opinions?

- **Venue**: ICLR 2026 Poster
- **Authors**: Erfan Jahanparast, Zhiqing Hong, Serina Chang
- **Keywords**: large language models, opinions, computational social science, interpretability
- **OpenReview**: https://openreview.net/forum?id=kHVzEjThKE
- **PDF**: https://openreview.net/pdf?id=kHVzEjThKE

**Abstract**

What large language models (LLMs) know about human opinions has important implications for aligning LLMs to human values, simulating humans with LLMs, and understanding what LLMs learn during training. While prior works have tested LLMs' knowledge of opinions via their next token outputs, we present the first study to probe LLMs' internal knowledge of opinions, evaluating LLMs across 22 demographic groups on a wide range of topics. First, we show that LLMs' internal knowledge of opinions far exceeds what is revealed by their outputs, with a 50-59% improvement in alignment with the human answer distribution; this improvement is competitive to fine-tuning but 278 times less computationally expensive. Second, we find that knowledge of opinions emerges rapidly in the middle layers of the LLM and identify the final unembeddings as the source of the discrepancy between internal knowledge and outputs. Third, using sparse autoencoders, we trace the knowledge of opinions in the LLM's residual stream back to attention heads, and we identify specific attention head features responsible for different demographic groups. These findings open new avenues for building value-aligned and computationally efficient LLMs, with applications in survey research, social simulation, and more broadly, safe and trustworthy AI. We will release our code upon acceptance.

**Abstract (Chinese)**

大语言模型（LLMs）对人类观点的了解对于将LLMs与人类价值观对齐、使用LLMs模拟人类以及理解LLMs在训练过程中学习的内容具有重要意义。虽然先前工作通过LLMs的下一个标记输出来测试其对观点的了解，但我们首次提出一项研究，用于探测LLMs对观点的内部知识，并在广泛主题上评估了LLMs在22个人口统计群体中的表现。首先，我们证明LLMs对观点的内部知识远远超过其输出所揭示的内容，与人类回答分布的对齐度提高了50-59%；这一改进与微调相当，但计算成本仅为其1/278。其次，我们发现观点知识在中层迅速涌现，并将最终反嵌入层识别为内部知识与输出之间差异的来源。第三，使用稀疏自编码器，我们将LLMs残差流中观点知识追溯至注意力头，并识别出负责不同人口统计群体的特定注意力头特征。这些发现为构建价值对齐且计算高效的LLMs开辟了新途径，适用于调查研究、社会模拟以及更广泛的安全可信AI。我们将在论文被接受后发布代码。

---
