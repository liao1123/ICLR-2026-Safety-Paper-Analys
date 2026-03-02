# other_safety_related_topics

**Description**: 其他安全相关主题（兜底）。当论文与上述类别均不匹配，但仍属于安全/风险/治理/合规/伦理/社会影响等方向时归入此类。

**Paper count**: 18

---

### A Rich Knowledge Space for Scalable Deepfake Detection

- **Venue**: ICLR 2026 Poster
- **Authors**: Inho Jung, Hyeongjun Choi, Binh M. Le, Hohyun Na, Simon S. Woo
- **Keywords**: Deepfake Detection, Media Forensics, Multi-modal Learning
- **OpenReview**: https://openreview.net/forum?id=hNd5L7WnjC
- **PDF**: https://openreview.net/pdf?id=hNd5L7WnjC

**Abstract**

The proliferation of realistic deepfakes has driven the development of numerous benchmark datasets to support detection research. Despite their increasing volume and diversity, no prior effort has systematically consolidated these resources into a unified framework for large-scale model training, nor has there been a massively pre-trained model tailored to deepfake detection. In this work, we introduce Multi-modal Multi-type Integrated Deepfake Dataset (MMI-DD), a large-scale resource containing 3.6 million facial images, the largest collection to date. It unifies diverse benchmarks with uniform preprocessing, and further provides fine-grained annotations across four deepfake types, as well as VLM-generated descriptions capturing both facial and environmental attributes for each image. By leveraging this comprehensive multi-modal dataset, we construct a foundational deepfake knowledge space that empowers our model to discern a broad spectrum of synthetic media. Our method, $SD^2$ (Scalable Deepfake Detection), refines CLIP for deepfake detection, optimizing image-text classification with rich, type-specific labels. We enhance this with intermediate visual features capturing low-level cues and text label separation loss for stability. We further leverage VLM-generated descriptions and contrastive learning to expand the scope of forgery knowledge, reducing overfitting and enhancing generalization. Extensive experiments on challenging deepfake datasets and AIGC benchmark demonstrate the effectiveness, scalability, and real-world applicability of our approach.

**Abstract (Chinese)**

真实深度伪造的泛滥推动了众多基准数据集的发展，以支持检测研究。尽管这些数据集的数量和多样性不断增加，但先前的工作尚未系统地将这些资源整合到一个统一的框架中，用于大规模模型训练，也没有针对深度伪造检测量身定制的大规模预训练模型。在本工作中，我们引入了多模态多类型集成深度伪造数据集 (MMI-DD)，这是一个包含 360 万张面部图像的大规模资源，是迄今为止最大的集合。它通过统一的预处理统一了多样化的基准数据集，并进一步为四种深度伪造类型提供了细粒度标注，以及为每张图像捕获面部和环境属性的 VLM 生成描述。通过利用这个全面的多模态数据集，我们构建了一个基础深度伪造知识空间，使我们的模型能够辨别广泛的合成媒体谱系。我们的方法 $SD^2$ (可扩展深度伪造检测) 对 CLIP 进行了优化，用于深度伪造检测，通过丰富的类型特定标签优化图像-文本分类。我们通过捕获低级线索的中间视觉特征以及用于稳定性的文本标签分离损失来增强这一点。我们进一步利用 VLM 生成的描述和对比学习来扩展伪造知识的范围，减少过拟合并增强泛化能力。在具有挑战性的深度伪造数据集和 AIGC 基准上的广泛实验证明了我们方法的有效性、可扩展性和实际适用性。

---

### Adaptive Social Learning via Mode Policy Optimization for Language Agents

- **Venue**: ICLR 2026 Poster
- **Authors**: Minzheng Wang, Yongbin Li, Haobo Wang, Xinghua Zhang, Nan Xu, Bingli Wu, Fei Huang, Haiyang Yu, Wenji Mao
- **Keywords**: Social Intelligence, Large Language Models, Adaptive Social Learning
- **OpenReview**: https://openreview.net/forum?id=GG7YQnsdhp
- **PDF**: https://openreview.net/pdf?id=GG7YQnsdhp

**Abstract**

Effective social intelligence simulation requires language agents to dynamically adjust reasoning depth, a capability notably absent in current studies. Existing methods either lack explicit reasoning or employ lengthy Chain-of-Thought reasoning uniformly across all scenarios, resulting in excessive token usage and inflexible social behaviors in tasks such as negotiation or collaboration. 
To address this, we propose an $\textbf{A}$daptive $\textbf{S}$ocial $\textbf{L}$earning ($\textbf{ASL}$) framework in this paper, aiming to improve the adaptive reasoning ability of language agents in dynamic social interactions. To this end, we first identify the hierarchical reasoning modes under such context, ranging from intuitive response to deep deliberation based on the cognitive control theory. We then develop the $\textbf{A}$daptive $\textbf{M}$ode $\textbf{P}$olicy $\textbf{O}$ptimization ($\textbf{AMPO}$) algorithm to learn the context-aware mode adaptation and reasoning. Our framework advances existing research in three key aspects: (1) Multi-granular reasoning mode design, (2) Context-aware mode switching in rich social interaction, and (3) Token-efficient reasoning with depth adaptation. Extensive experiments on the benchmark social intelligence environment verify that ASL achieves 15.6\% higher task performance than GPT-4o. Notably, our AMPO outperforms GRPO by 7.0\% with 32.8\% shorter thinking chains, demonstrating the advantages of our AMPO and the learned adaptive reasoning ability over GRPO's solution.

**Abstract (Chinese)**

有效的社会智能模拟要求语言代理动态调整推理深度，这一能力在当前研究中明显缺失。现有的方法要么缺乏明确的推理，要么在所有场景中统一采用冗长的思维链推理，导致令牌使用过多以及在谈判或协作等任务中社会行为不灵活。

为解决这一问题，本文提出自适应社会学习（$\textbf{ASL}$）框架，旨在提升语言代理在动态社会互动中的自适应推理能力。为此，我们首先基于认知控制理论识别了此类情境下的分层推理模式，从直觉响应到深度审议。随后，我们开发了自适应模式策略优化（$\textbf{AMPO}$）算法，以学习上下文感知的模式适应和推理。

我们的框架在三个关键方面推进了现有研究：（1）多粒度推理模式设计，（2）丰富社会互动中的上下文感知模式切换，以及（3）具有深度适应的令牌高效推理。在基准社会智能环境上的广泛实验验证了ASL比GPT-4o的任务性能高出15.6%。值得注意的是，我们的AMPO比GRPO高出7.0%，思考链缩短32.8%，展示了我们的AMPO和学习到的自适应推理能力相对于GRPO解决方案的优势。

---

### AtC: Aggregate-then-Calibrate for Human-centered Assessment

- **Venue**: ICLR 2026 Poster
- **Authors**: Zejun Xie, Xintong Li, Guang Wang, Desheng Zhang
- **Keywords**: human-centered assessment, judgment aggregation, calibration, misspecification, human-AI complementarity, human-AI collaboration
- **OpenReview**: https://openreview.net/forum?id=XNbVoi9mfr
- **PDF**: https://openreview.net/pdf?id=XNbVoi9mfr

**Abstract**

Human-centered assessment tasks, which are essential for systematic decision-making, rely heavily on human judgment and typically lack verifiable ground truth. Existing approaches face a dilemma: methods using only human judgments suffer from heterogeneous expertise and inconsistent rating scales, while methods using only model-generated scores must learn from imperfect proxies or incomplete features. We propose Aggregate-then-Calibrate (AtC), a two-stage framework that combines these complementary sources. Stage-1 aggregates heterogeneous comparative judgments into a consensus ranking $\hat{\pi}$ using a rank-aggregation model that accounts for annotator reliability. Stage-2 calibrates any predictive model’s scores by an isotonic projection onto the order $\hat{\pi}$, enforcing ordinal consistency while preserving as much of the model’s quantitative information as possible. Theoretically, we show: (1) modeling annotator heterogeneity yields strictly more efficient consensus estimation than homogeneity; (2) isotonic calibration enjoys risk bounds even when the consensus ranking is misspecified; and (3) AtC asymptotically outperforms model-only assessment. Across semi-synthetic and real-world datasets, AtC consistently improves accuracy and robustness over human-only or model-only assessments. Our results bridge judgment aggregation with model-free calibration, providing a principled recipe for human-centered assessment when ground truth is costly, scarce, or unverifiable.

**Abstract (Chinese)**

以人为中心的评估任务对于系统决策至关重要，它们高度依赖人类判断，并且通常缺乏可验证的真实标签。现有的方法面临两难困境：仅使用人类判断的方法受异质专业知识和不一致评分尺度的影响，而仅使用模型生成分数的方​​法必须从不完美的代理或不完整的特征中学习。我们提出聚合后校准 (AtC)，一个两阶段框架，将这些互补来源相结合。第一阶段使用考虑标注者可靠性的排名聚合模型，将异质比较判断聚合为共识排名 $\hat{\pi}$。第二阶段通过将任何预测模型的分数等调投影到顺序 $\hat{\pi}$ 上进行校准，从而强制序一致性，同时尽可能保留模型的定量信息。理论上，我们证明：(1) 建模标注者异质性比同质性假设产生严格更有效的共识估计；(2) 即使共识排名设定错误，等调校准也具有风险界；(3) AtC 渐近优于仅模型评估。在半合成和真实世界数据集上，AtC 在准确性和鲁棒性上始终优于仅人类或仅模型评估。我们的结果桥接了判断聚合与无模型校准，为真实标签昂贵、稀缺或不可验证时的以人为中心的评估提供了原则性方案。

---

### Conjuring Semantic Similarity

- **Venue**: ICLR 2026 Poster
- **Authors**: Tian Yu Liu, Stefano Soatto
- **Keywords**: Meaning Representation, Semantic Similarity, Diffusion Model
- **OpenReview**: https://openreview.net/forum?id=Wf0tGnQOIh
- **PDF**: https://openreview.net/pdf?id=Wf0tGnQOIh

**Abstract**

The semantic similarity between sample expressions measures the distance between their latent `meaning'.These meanings are themselves typically represented by textual expressions.  We propose a novel approach whereby the semantic similarity among textual expressions is based not on other expressions they can be rephrased as, but rather based on the imagery they evoke. While this is not possible with humans, generative models allow us to easily visualize and compare generated images, or their distribution, evoked by a textual prompt. Therefore, we characterize the semantic similarity between two textual expressions simply as the distance between image distributions they induce, or 'conjure.' We show that by choosing the Jeffreys divergence between the reverse-time diffusion stochastic differential equations (SDEs) induced by each textual expression, this can be directly computed via Monte-Carlo sampling. Our method contributes a novel perspective on semantic similarity that not only aligns with human-annotated scores, but also opens up new avenues for the evaluation of text-conditioned generative models while offering better interpretability of their learnt representations.

**Abstract (Chinese)**

样本表达式之间的语义相似度衡量了它们潜在“含义”之间的距离。这些含义本身通常由文本表达式表示。我们提出了一种新颖的方法，其中文本表达式之间的语义相似度不是基于它们可以改述的其他表达式，而是基于它们唤起的图像。虽然这对人类来说是不可能的，但生成模型允许我们轻松可视化和比较由文本提示唤起的生成图像，或其分布。因此，我们简单地将两个文本表达式之间的语义相似度表征为它们诱导的图像分布之间的距离，或“唤起”。我们证明，通过选择每个文本表达式诱导的逆时扩散随机微分方程 (SDEs) 之间的杰弗里斯散度，这可以通过蒙特卡罗采样直接计算。我们的方法为语义相似度提供了一个新颖的视角，不仅与人工标注分数一致，还为条件文本生成模型的评估开辟了新途径，同时提供了对其学习表示的更好可解释性。

---

### Counterfactual LLM-based Framework for Measuring Rhetorical Style

- **Venue**: ICLR 2026 Poster
- **Authors**: Jingyi Qiu, Hong Chen, Zongyi Li
- **Keywords**: AI for Metascience, Preference Models, LLM-as-Judge, Computational Social Science, LLM Personas, Rhetorical Style Measurement
- **OpenReview**: https://openreview.net/forum?id=fiohEI16sf
- **PDF**: https://openreview.net/pdf?id=fiohEI16sf

**Abstract**

The rise of AI has fueled growing concerns about "hype" in machine learning papers, yet a reliable way to quantify rhetorical style independently of substantive content has remained elusive. Because bold language can stem from either strong empirical results or mere rhetorical style, it is often difficult to distinguish between the two. To disentangle rhetorical style from substantive content, we introduce a counterfactual, LLM-based framework: multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and the outcomes are aggregated using a Bradley--Terry model. Applying this method to 8,485 ICLR submissions sampled from 2017 to 2025, we generate more than 250,000 counterfactual writings and provide a large-scale quantification of rhetorical style in ML papers. We find that visionary framing significantly predicts downstream attention, including citations and media attention, even after controlling for peer-review evaluations. We also observe a sharp rise in rhetorical strength after 2023, and provide empirical evidence showing that this increase is largely driven by the adoption of LLM-based writing assistance. The reliability of our framework is validated by its robustness to the choice of personas and the high correlation between LLM judgments and human annotations. Our work demonstrates that LLMs can serve as instruments to measure and improve scientific evaluation.

**Abstract (Chinese)**

人工智能的兴起引发了对机器学习论文中“炒作”的日益担忧，然而，一个独立于实质内容量化修辞风格的可靠方法仍难以捉摸。因为大胆语言可能源于强大的实证结果或单纯的修辞风格，因此往往难以区分两者。为了将修辞风格与实质内容分离，我们引入了一个基于反事实的大语言模型（LLM）框架：多个LLM修辞角色从相同实质内容生成反事实写作，一个LLM评判者通过成对评估比较它们，并使用Bradley--Terry模型聚合结果。将此方法应用于2017年至2025年抽样的8,485篇ICLR投稿，我们生成了超过250,000篇反事实写作，并为机器学习论文提供了大规模的修辞风格量化。我们发现，愿景框架显著预测下游关注度，包括引用和媒体关注，即使在控制同行评审评估后也是如此。我们还观察到2023年后修辞强度急剧上升，并提供了实证证据，显示这一增加主要由采用基于LLM的写作辅助驱动。我们框架的可靠性通过其对角色选择的鲁棒性和LLM判断与人类标注之间的高相关性得到验证。我们的工作证明，大语言模型可以作为测量和改进科学评估的工具。

---

### DIVERSE: Disagreement-Inducing Vector Evolution for Rashomon Set Exploration

- **Venue**: ICLR 2026 Poster
- **Authors**: Gilles Eerlings, Brent Zoomers, Jori Liesenborgs, Gustavo Rovelo Ruiz, Kris Luyten
- **Keywords**: Rashomon Set, Rashomon Effect, Feature-wise Linear Modulation (FiLM), CMA-ES, Model Multiplicity, Predictive Multiplicity, Neural Network Diversity
- **OpenReview**: https://openreview.net/forum?id=kQjSUHC84V
- **PDF**: https://openreview.net/pdf?id=kQjSUHC84V

**Abstract**

We propose DIVERSE, a framework for systematically exploring the Rashomon set of deep neural networks, the collection of models that match a reference model’s accuracy while differing in their predictive behavior. DIVERSE augments a pretrained model with Feature-wise Linear Modulation (FiLM) layers and uses Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to search a latent modulation space, generating diverse model variants without retraining or gradient access. Across MNIST, PneumoniaMNIST, and CIFAR-10, DIVERSE uncovers multiple high-performing yet functionally distinct models. Our experiments show that DIVERSE offers a competitive and efficient exploration of the Rashomon set, making it feasible to construct diverse sets that maintain robustness and performance while supporting well-balanced model multiplicity. While retraining remains the baseline to generate Rashomon sets, DIVERSE achieves comparable diversity at reduced computational cost.

**Abstract (Chinese)**

我们提出 DIVERSE，这是一个用于系统探索深度神经网络 Rashomon 集的框架，该集是由与参考模型准确率相匹配但预测行为不同的模型集合。DIVERSE 通过添加逐特征线性调制 (FiLM) 层来增强预训练模型，并使用协方差矩阵适应进化策略 (CMA-ES) 搜索潜在调制空间，从而在无需重新训练或梯度访问的情况下生成多样化的模型变体。在 MNIST、PneumoniaMNIST 和 CIFAR-10 数据集上，DIVERSE 发现了多个高性能但功能上不同的模型。我们的实验表明，DIVERSE 提供了 Rashomon 集的竞争性和高效探索，使构建保持鲁棒性和性能同时支持良好平衡模型多重性的多样化集合成为可能。虽然重新训练仍是生成 Rashomon 集的基准方法，但 DIVERSE 以降低的计算成本实现了相当的多样性。

---

### Diversity-Enhanced Reasoning for Subjective Questions

- **Venue**: ICLR 2026 Poster
- **Authors**: Yumeng Wang, Zhiyuan Fan, Jiayu Liu, Jen-tse Huang, Yi R. Fung
- **Keywords**: LLM, subjective reasoning, diversity-enhanced training
- **OpenReview**: https://openreview.net/forum?id=1Bf0tToGT1
- **PDF**: https://openreview.net/pdf?id=1Bf0tToGT1

**Abstract**

Large Reasoning Models (LRMs) with long chain-of-thought capabilities, optimized via reinforcement learning with verifiable rewards (RLVR), excel at **objective reasoning** tasks like mathematical problem solving and code generation.
However, RLVR is known for degrading generation diversity, which causes LRMs to fall short on **subjective reasoning** that has multiple answers depending on different role perspectives.
While recent studies recognize the importance of diversity-enhanced training in objective reasoning, limited attention has been given to subjective tasks.
In this paper, we find that subjective reasoning can be improved by introducing perspective diversity and token-level diversity, with the former one providing a coherent scaffolding anchored to a real-world stakeholder group and the latter one broadening the answer search space.
We propose MultiRole-R1, a diversity-enhanced training framework featuring an unsupervised data construction pipeline that synthesizes reasoning chains incorporating various role perspectives.
It also employs reinforcement learning via Group Relative Policy Optimization with reward shaping, taking diversity as a reward signal in addition to verifiable reward.
Training on subjective tasks solely, MultiRole-R1 increases the in-domain and out-of-domain accuracy by 14.1% and 7.64%, and even enhances the performance on advanced math reasoning such as AIME 2024.
We further show that diversity is a more consistent indicator of accuracy than reasoning length.

**Abstract (Chinese)**

具有长链式思考能力的大型推理模型（LRMs），通过使用可验证奖励的强化学习（RLVR）进行优化，在诸如数学问题求解和代码生成之类的**客观推理**任务中表现出色。然而，RLVR 以降低生成多样性而闻名，这导致 LRMs 在具有多个答案、取决于不同角色视角的**主观推理**上表现不足。虽然最近的研究认识到多样性增强训练在客观推理中的重要性，但对主观任务的关注有限。在本文中，我们发现，通过引入视角多样性和令牌级多样性，可以改善主观推理，其中前者提供锚定于现实世界利益相关者群体的连贯支架，后者拓宽答案搜索空间。我们提出 MultiRole-R1，这是一个多样性增强训练框架，具有一个无监督数据构建管道，用于合成融入各种角色视角的推理链。它还通过带有奖励塑形的组相对策略优化采用强化学习，将多样性作为除了可验证奖励之外的奖励信号。仅在主观任务上训练，MultiRole-R1 将领域内和领域外准确率提高了 14.1% 和 7.64%，甚至提升了高级数学推理性能，如 AIME 2024。我们进一步表明，多样性比推理长度更一致地指示准确率。

---

### Formalising Human-in-the-Loop: Computational Reductions, Failure Modes, and Legal-Moral Responsibility

- **Venue**: ICLR 2026 Poster
- **Authors**: Maurice Chiodo, Dennis Müller, Paul Siewert, Jean-Luc Wetherall, Zoya Yasmine, John Burden
- **Keywords**: Human-in-the-loop, Automated decision making system, Human oversight in sociotechnical systems, Oracle machine, AI safety, Trustworthy AI
- **OpenReview**: https://openreview.net/forum?id=KR8viVTrX4
- **PDF**: https://openreview.net/pdf?id=KR8viVTrX4

**Abstract**

We  use the notion of oracle machines and reductions from computability theory to formalise different Human-in-the-loop (HITL) setups for AI systems, distinguishing between trivial human monitoring (i.e., total functions), single endpoint human action (i.e., many-one reductions), and highly involved human-AI interaction (i.e., Turing reductions). We then proceed to show that the legal status and safety of different setups vary greatly. We present a taxonomy to categorise HITL failure modes, highlighting the practical limitations of  HITL setups. We then identify omissions in UK and EU legal frameworks, which focus on HITL setups that may not always achieve the desired ethical, legal, and sociotechnical outcomes. We suggest areas where the law should recognise the effectiveness of different HITL setups and assign responsibility in these contexts, avoiding human `scapegoating'. Our work shows an unavoidable trade-off between attribution of legal responsibility, and  technical explainability.  Overall, we show how HITL setups involve many technical design decisions, and can be prone to failures out of the humans' control. Our formalisation and taxonomy opens up a new analytic perspective on the challenges in creating HITL setups, helping inform AI developers and lawmakers on designing HITL setups to better achieve their desired outcomes.

**Abstract (Chinese)**

我们利用可计算性理论中的预言机和归约概念来形式化AI系统中不同的人在回路（HITL）配置，区分了琐碎的人类监控（即全函数）、单一端点人类行动（即多对一归约）以及高度参与的人机交互（即Turing归约）。随后，我们证明不同配置的法律地位和安全性差异很大。我们提出一个分类法来归类HITL失效模式，突显HITL配置的实际局限性。我们指出了英国和欧盟法律框架中的遗漏，这些框架关注HITL配置，但此类配置可能并非总是实现预期的伦理、法律和社会技术结果。我们建议法律应承认不同HITL配置的有效性，并在这些情境中分配责任，避免将人类作为“替罪羊”。我们的工作揭示了法律责任归属与技术可解释性之间不可避免的权衡取舍。总体而言，我们展示了HITL配置涉及诸多技术设计决策，并且可能发生人类无法控制的失效。我们的形式化和分类法为创建HITL配置的挑战开辟了新的分析视角，有助于指导AI开发者与立法者设计HITL配置，以更好地实现其预期结果。

---

### Full-Graph vs. Mini-Batch Training: Comprehensive Analysis from a Batch Size and Fan-Out Size Perspective

- **Venue**: ICLR 2026 Poster
- **Authors**: Mengfan Liu, Da Zheng, Junwei Su, Chuan Wu
- **Keywords**: Graph Neural Network
- **OpenReview**: https://openreview.net/forum?id=ZSfgsh43vT
- **PDF**: https://openreview.net/pdf?id=ZSfgsh43vT

**Abstract**

Full-graph and mini-batch Graph Neural Network (GNN) training approaches have distinct system design demands, making it crucial to choose the appropriate approach to develop. A core challenge in comparing these two GNN training approaches lies in characterizing their model performance (i.e., convergence and generalization) and computational efficiency. While a batch size has been an effective lens in analyzing such behaviors in deep neural networks (DNNs), GNNs extends this lens by introducing a fan-out size, as full-graph training can be viewed as mini-batch training with the largest possible batch size and fan-out size. However, the impact of the batch and fan-out size for GNNs remains insufficiently explored. To this end, this paper systematically compares full-graph vs. mini-batch training of GNNs through empirical and theoretical analyses from the view of the batch size and fan-out size. Our key contributions include: 1) We provide a novel generalization analysis using the Wasserstein distance to study the impact of the graph structure, especially the fan-out size. 2) We uncover the non-isotropic effects of the batch size and the fan-out size in GNN convergence and generalization, providing practical guidance for tuning these hyperparameters under resource constraints. Finally, full-graph training does not always yield better model performance or computational efficiency than well-tuned smaller mini-batch settings. The implementation can be found in the github link: https://github.com/LIUMENGFAN-gif/GNN_fullgraph_minibatch_training.

**Abstract (Chinese)**

全图和小批量图神经网络（GNN）训练方法具有不同的系统设计需求，因此选择合适的方法进行开发至关重要。将这两种GNN训练方法进行比较的核心挑战在于表征其模型性能（即收敛性和泛化性）以及计算效率。虽然批量大小已成为分析深度神经网络（DNNs）此类行为的有力视角，但GNN通过引入扇出大小扩展了这一视角，因为全图训练可以视为具有最大可能批量大小和扇出大小的小批量训练。然而，批量大小和扇出大小对GNN的影响仍未得到充分探索。为此，本文从批量大小和扇出大小的视角，通过实证和理论分析系统比较了GNN的全图训练与小批量训练。主要贡献包括：1）我们提出了一种使用瓦瑟斯坦距离的新颖泛化分析方法，以研究图结构的影响，特别是扇出大小的影响；2）我们揭示了批量大小和扇出大小在GNN收敛和泛化中的非各向同性效应，为资源受限条件下调优这些超参数提供了实用指导。最后，全图训练并不总是比精心调优的小批量设置产生更好的模型性能或计算效率。代码实现可在GitHub链接中找到：https://github.com/LIUMENGFAN-gif/GNN_fullgraph_minibatch_training。

---

### Generalization in LLM Problem Solving: The Case of the Shortest Path

- **Venue**: ICLR 2026 Poster
- **Authors**: Yao Tong, Jiayuan Ye, Anastasia Borovykh, Reza Shokri
- **Keywords**: Compositional generalization, problem solving
- **OpenReview**: https://openreview.net/forum?id=RnRHNEeqvI
- **PDF**: https://openreview.net/pdf?id=RnRHNEeqvI

**Abstract**

Whether language models can systematically generalize remains actively debated. 
Yet empirical performance is jointly shaped by multiple factors such as training data, training paradigms, and inference-time strategies, making failures difficult to interpret.
We introduce a controlled synthetic environment based on shortest-path planning, a canonical composable sequential optimization problem. 
The setup enables clean separation of these factors and supports two orthogonal axes of generalization: ***spatial transfer*** to unseen maps and ***length scaling*** to longer-horizon problems.
We find that models exhibit strong spatial transfer but consistently fail under length scaling due to recursive instability.
We further analyze how distinct stages of the learning pipeline influence systematic problem-solving:
for example, data coverage sets capability limits; reinforcement learning improves training stability but does not expand those limits; and inference-time scaling enhances performance but cannot rescue length-scaling failures.

**Abstract (Chinese)**

语言模型是否能够系统性泛化仍备受争议。

然而，实证性能受多种因素共同塑造，如训练数据、训练范式和推理时策略，这使得失败难以解释。

我们引入了一个基于最短路径规划的受控合成环境，这是一个典型的可组合序列优化问题。

该设置能够清晰分离这些因素，并支持两个正交的泛化轴：***空间转移***到未见地图，以及***长度扩展***到更长时域问题。

我们发现，模型在空间转移上表现出色，但在长度扩展下由于递归不稳定性而持续失败。

我们进一步分析了学习管道的不同阶段如何影响系统性问题求解：

例如，数据覆盖设定能力极限；强化学习改善训练稳定性但不扩展这些极限；推理时扩展提升性能但无法挽救长度扩展失败。

---

### Good allocations from bad estimates

- **Venue**: ICLR 2026 Poster
- **Authors**: Sílvia Casacuberta, Moritz Hardt
- **Keywords**: Treatment Allocation, Treatment effects, Sample complexity, RCT
- **OpenReview**: https://openreview.net/forum?id=rxZdaKhu2I
- **PDF**: https://openreview.net/pdf?id=rxZdaKhu2I

**Abstract**

Conditional average treatment effect (CATE) estimation is the de facto gold standard for targeting a treatment to a heterogeneous population. The method estimates treatment effects up to an error $\epsilon > 0$ in each of $M$ different strata of the population, targeting individuals in decreasing order of estimated treatment effect until the budget runs out. In general, this method requires $O(M/\epsilon^2)$ samples. This is best possible if the goal is to estimate all treatment effects up to an $\epsilon$ error. 
In this work, we show how to achieve the same total treatment effect as CATE with only $O(M/\epsilon)$ samples for natural distributions of treatment effects. The key insight is that coarse estimates suffice for near-optimal treatment allocations. In addition, we show that budget flexibility can further reduce the sample complexity of allocation.
Finally, we evaluate our algorithm on various real-world RCT datasets. In all cases, it finds nearly optimal treatment allocations with surprisingly few samples. Our work highlights the fundamental distinction between treatment effect estimation and treatment allocation: the latter requires far fewer samples.

**Abstract (Chinese)**

条件平均处理效应 (CATE) 估计是针对异质人群分配处理的实际黄金标准。该方法在人群的 $M$ 个不同分层中估计处理效应，误差不超过 $\epsilon > 0$，按估计处理效应的递减顺序针对个体，直到预算耗尽。一般而言，该方法需要 $O(M/\epsilon^2)$ 个样本。如果目标是估计所有处理效应误差不超过 $\epsilon$，则这是最优的。

在本工作中，我们展示了如何在处理效应的自然分布下，仅使用 $O(M/\epsilon)$ 个样本，即可实现与 CATE 相同的总处理效应。关键洞见是，粗略估计足以实现近似最优的处理分配。此外，我们证明预算灵活性可以进一步降低分配的样本复杂度。

最后，我们在各种真实世界的随机对照试验 (RCT) 数据集上评估了我们的算法。在所有情况下，它仅用惊人少的样本就找到了近似最优的处理分配。我们的工作突出了处理效应估计与处理分配之间的根本区别：后者需要远少的样本。

---

### Human-LLM Collaborative Feature Engineering for Tabular Data

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhuoyan Li, Aditya Bansal, Jinzhao Li, Shishuang He, Zhuoran Lu, Mutian Zhang, Qin Liu, Yiwei Yang, Swati Jain, Ming Yin, Yunyao Li
- **Keywords**: human-ai interaction, human-centered evaluation
- **OpenReview**: https://openreview.net/forum?id=ohVOD2ixBH
- **PDF**: https://openreview.net/pdf?id=ohVOD2ixBH

**Abstract**

Large language models (LLMs) are increasingly used to automate feature engineering in tabular learning. Given task-specific information, LLMs can propose diverse feature transformation operations to enhance downstream model performance. However, current approaches typically assign the LLM as a black-box optimizer, responsible for both proposing and selecting operations based solely on its internal heuristics, which often lack calibrated estimations of operation utility and consequently lead to repeated exploration of low-yield operations without a principled strategy for prioritizing promising directions. In this paper, we propose a human–LLM collaborative feature engineering framework for tabular learning. We begin by decoupling the transformation operation proposal and selection processes, where LLMs are used solely to generate operation candidates, while the selection is guided by explicitly modeling the utility and uncertainty of each proposed operation. Since accurate utility estimation can be difficult especially in the early rounds of feature engineering, we design a mechanism within the framework that selectively elicits and incorporates human expert preference feedback—comparing which operations are more promising—into the selection process to help identify more effective operations.
Our evaluations on both the synthetic study and the real user study demonstrate that the proposed framework improves feature engineering performance across a variety of tabular datasets and reduces users’ cognitive load during the feature engineering process.

**Abstract (Chinese)**

大语言模型（LLMs）正日益被用于自动化表格学习中的特征工程。在给定任务特定信息的情况下，LLMs 可以提出多样化的特征变换操作，以提升下游模型性能。然而，现有的方法通常将 LLM 视为黑箱优化器，仅基于其内部启发式来负责提出和选择操作，这往往缺乏对操作效用的校准估计，从而导致反复探索低收益操作，且缺少优先考虑有前景方向的原理性策略。本文提出了一种针对表格学习的 人–LLM 协作特征工程框架。我们首先将变换操作的提出和选择过程解耦，其中 LLMs 仅用于生成操作候选，而选择过程则通过显式建模每个提出操作的效用和不确定性来指导。由于在特征工程的早期轮次中准确估计效用可能较为困难，我们在框架中设计了一种机制，该机制选择性地征集并融入人类专家偏好反馈——比较哪些操作更有前景——到选择过程中，以帮助识别更有效的操作。

我们在合成实验和真实用户研究上的评估表明，所提出的框架在多种表格数据集上提升了特征工程性能，并降低了用户在特征工程过程中的认知负担。

---

### Market Games for Generative Models: Equilibria, Welfare, and Strategic Entry

- **Venue**: ICLR 2026 Poster
- **Authors**: Xiukun Wei, Min Shi, Xueru Zhang
- **Keywords**: Generative model competition, Nash equilibrium, Welfare analysis, Best-response training
- **OpenReview**: https://openreview.net/forum?id=T7c5LXuebY
- **PDF**: https://openreview.net/pdf?id=T7c5LXuebY

**Abstract**

Generative model ecosystems increasingly operate as competitive multi-platform markets, where platforms strategically select models from a shared pool and users with heterogeneous preferences choose among them. Understanding how platforms interact, when market equilibria exist, how outcomes are shaped by model-provider, platforms, and user behavior, and how social welfare is affected is critical for fostering beneficial market environment. In this paper, we formalize a three-layer *model-platfrom-user* market game and identify conditions for the existence of pure Nash equilibrium. Our analysis shows that market structure, whether platforms converge on similar models or differentiate by selecting distinct ones, depends not only on models’ global average performance but also on their localized attraction to user groups. We further examine welfare outcomes and show that expanding the model pool does not necessarily increase user welfare or market diversity. Finally, we design and evaluate best-response training schemes that allow model-provider to strategically introduce new models into competitive markets.

**Abstract (Chinese)**

生成模型生态系统日益演变为竞争性多平台市场，其中平台从共享模型池中战略性地选择模型，而具有异质偏好的用户则从中进行选择。理解平台间的互动、市场均衡的存在条件、结果如何受模型提供者、平台和用户行为的影响，以及社会福利如何受到影响，对于培育有益的市场环境至关重要。本文形式化了一个三层*模型-平台-用户*市场博弈，并识别了纯纳什均衡存在条件。我们的分析表明，市场结构——平台是否收敛于相似模型或通过选择不同模型实现差异化——不仅取决于模型的全局平均性能，还取决于其对用户群组的局部吸引力。我们进一步考察福利结果，并表明扩展模型池并不一定提升用户福利或市场多样性。最后，我们设计并评估了最优响应训练方案，使模型提供者能够战略性地将新模型引入竞争市场。

---

### Modal Aphasia: Can Unified Multimodal Models Describe Images From Memory?

- **Venue**: ICLR 2026 Poster
- **Authors**: Michael Aerni, Joshua Swanson, Kristina Nikolić, Florian Tramèr
- **Keywords**: multi-modal language models, memorization, safety, unified representations
- **OpenReview**: https://openreview.net/forum?id=GSjDtnjcEM
- **PDF**: https://openreview.net/pdf?id=GSjDtnjcEM

**Abstract**

We present *modal aphasia*, a systematic dissociation in which current unified multimodal models accurately memorize concepts visually but fail to articulate them in writing, despite being trained on images and text simultaneously. For one, we show that leading frontier models can generate near-perfect reproductions of iconic movie artwork, but confuse crucial details when asked for textual descriptions. We corroborate those findings through controlled experiments on synthetic datasets in multiple architectures. Our experiments confirm that modal aphasia reliably emerges as a fundamental property of current unified multimodal models, not just as a training artifact. In practice, modal aphasia can introduce vulnerabilities in AI safety frameworks, as safeguards applied to one modality may leave harmful concepts accessible in other modalities. We demonstrate this risk by showing how a model aligned solely on text remains capable of generating unsafe images.

**Abstract (Chinese)**

我们提出“模态失语症”（*modal aphasia*），这是一种系统性分离现象，即当前统一的多模态模型尽管同时在图像和文本上训练，却能视觉上准确记忆概念，但无法用文字表达它们。例如，我们展示了领先的前沿模型能够生成标志性电影艺术作品的近乎完美的复制品，但在要求提供文本描述时却混淆了关键细节。我们通过在多种架构的合成数据集上进行的控制实验来证实这些发现。我们的实验证实，模态失语症作为当前统一多模态模型的基本属性可靠地出现，而不仅仅是训练伪影。在实践中，模态失语症可能在AI安全框架中引入漏洞，因为应用于一种模态的安全措施可能使有害概念在其他模态中仍然可访问。我们通过展示仅在文本上对齐的模型仍能生成不安全图像来证明这一风险。

---

### Multi-turn Evaluation of Anthropomorphic Behaviours in Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Lujain Ibrahim, Canfer Akbulut, Rasmi Elasmar, Charvi Rastogi, Minsuk Kahng, Meredith Ringel Morris, Kevin R. McKee, Verena Rieser, Murray Shanahan, Laura Weidinger
- **Keywords**: anthropomorphism, human-AI interaction, social AI, multi-turn, evaluation
- **OpenReview**: https://openreview.net/forum?id=ZAx4c4ZH5Y
- **PDF**: https://openreview.net/pdf?id=ZAx4c4ZH5Y

**Abstract**

The tendency of users to anthropomorphise large language models (LLMs) is of growing societal interest. Here, we present AnthroBench: a novel empirical method and tool for evaluating anthropomorphic LLM behaviours in realistic settings. Our work introduces three key advances; first, we develop a multi-turn evaluation of 14 distinct anthropomorphic behaviours, moving beyond single-turn assessment. Second, we present a scalable, automated approach by leveraging simulations of user interactions, enabling efficient and reproducible assessment. Third, we conduct an interactive, large-scale human subject study (N=1101) to empirically validate that the model behaviours we measure predict real users’ anthropomorphic perceptions. We find that all evaluated LLMs exhibit similar behaviours, primarily characterised by relationship-building (e.g., empathy and validation) and first-person pronoun use. Crucially, we observe that the majority of these anthropomorphic behaviors only first occur after multiple turns, underscoring the necessity of multi-turn evaluations for understanding complex social phenomena in human-AI interaction. Our work provides a robust empirical foundation for investigating how design choices influence anthropomorphic model behaviours and for progressing the ethical debate on the desirability of these behaviours.

**Abstract (Chinese)**

用户对大语言模型（LLMs）进行人格化的倾向正日益引起社会关注。在此，我们提出AnthroBench：一种新型实证方法和工具，用于在真实场景中评估人格化LLM行为。本工作引入了三项关键进展：首先，我们开发了对14种独特人格化行为的的多轮评估，超越了单轮评估。其次，我们提出了一种可扩展的自动化方法，通过模拟用户交互实现高效且可重复的评估。第三，我们开展了一项互动式大规模人类受试者研究（N=1101），以实证验证我们测量的模型行为能够预测真实用户的人格化感知。我们发现，所有评估的LLMs均表现出相似行为，主要特征为关系建立（例如，同理心和验证）以及第一人称代词的使用。至关重要的是，我们观察到大多数这些人格化行为仅在多轮交互后首次出现，这突显了多轮评估在理解人机交互中复杂社会现象的必要性。本工作为探究设计选择如何影响人格化模型行为提供了坚实的实证基础，并推动了关于这些行为可取性的伦理辩论。

---

### RelayFormer: A Unified Local-Global Attention Framework for Scalable Image and Video Manipulation Localization

- **Venue**: ICLR 2026 Poster
- **Authors**: Wen Huang, Jiarui Yang, Tao Dai, Jiawei Li, Shaoxiong Zhan, Bin Wang, Shu-Tao Xia
- **Keywords**: Image Manipulation Localization; Video Manipulation Localization
- **OpenReview**: https://openreview.net/forum?id=e61YQdLIam
- **PDF**: https://openreview.net/pdf?id=e61YQdLIam

**Abstract**

Visual manipulation localization (VML) aims to identify tampered regions in images and videos, a task that has become increasingly challenging with the rise of advanced editing tools. Existing methods face two central issues. The first is resolution diversity. Resizing or padding can distort subtle forensic cues and introduce unnecessary computational cost. The second is the difficulty of extending spatial models for images to spatio-temporal inputs in videos, which often results in maintaining separate architectures for the two data types.
To address these challenges, we propose RelayFormer, a unified framework that adapts to varying resolutions and naturally handles both static and temporal visual data. RelayFormer partitions inputs into fixed-size sub-images and introduces Global Local Relay (GLR) tokens that propagate structured context through a relay-based attention mechanism. This design enables efficient exchange of global cues, such as semantic or temporal consistency, while preserving fine-grained manipulation artifacts.
Unlike prior approaches that depend on uniform resizing or sparse attention, RelayFormer scales to variable resolutions and video sequences with minimal overhead. Experiments across diverse benchmarks demonstrate superior performance and strong efficiency, combining resolution adaptivity without interpolation or excessive padding, unified processing for images and videos, and a favorable balance between accuracy and computational cost. Code is available at~\href{https://github.com/WenOOI/RelayFormer}{https://github.com/WenOOI/RelayFormer}.

**Abstract (Chinese)**

视觉篡改定位（VML）旨在识别图像和视频中的篡改区域，随着高级编辑工具的兴起，这一任务变得越来越具有挑战性。现有的方法面临两个核心问题。首先是分辨率多样性。调整大小或填充可能会扭曲细微的取证线索，并引入不必要的计算成本。其次是将图像的空间模型扩展到视频中的时空输入的困难，这往往导致为两种数据类型维护单独的架构。

为了应对这些挑战，我们提出了RelayFormer，这是一个统一的框架，能够适应不同的分辨率，并自然处理静态和时序视觉数据。RelayFormer将输入划分为固定大小的子图像，并引入全局局部中继（GLR）标记，这些标记通过基于中继的注意力机制传播结构化上下文。这种设计实现了全局线索（如语义或时间一致性）的有效交换，同时保留细粒度的篡改伪影。

与依赖统一调整大小或稀疏注意力的先前方法不同，RelayFormer以最小开销扩展到可变分辨率和视频序列。在多样化的基准测试上的实验展示了优越的性能和强大的效率，结合了无需插值或过度填充的分辨率适应性、图像和视频的统一处理，以及准确性和计算成本之间的良好平衡。代码可在https://github.com/WenOOI/RelayFormer获取。

---

### Routing, Cascades, and User Choice for LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Rafid Mahmood
- **Keywords**: LLM routing; human-AI interaction; game theory
- **OpenReview**: https://openreview.net/forum?id=VqAhhF6av8
- **PDF**: https://openreview.net/pdf?id=VqAhhF6av8

**Abstract**

To mitigate the trade-offs between performance and costs, LLM providers route user tasks to different models based on task difficulty and latency. We study the effect of LLM routing with respect to user behavior. We propose a game between an LLM provider with two models (standard and reasoning) and a user who can re-prompt or abandon tasks if the routed model cannot solve them. The user's goal is to maximize their utility minus the delay from using the model, while the provider minimizes the cost of servicing the user. We solve this Stackelberg game by fully characterizing the user best response and simplifying the provider problem. We observe that in nearly all cases, the optimal routing policy involves a static policy with no cascading that depends on the expected utility of the models to the user.
Furthermore, we reveal a misalignment gap between the provider-optimal and user-preferred routes when the user's and provider's rankings of the models with respect to utility and cost differ. Finally, we demonstrate conditions for extreme misalignment where providers are incentivized to throttle the latency of the models to minimize their costs, consequently depressing user utility. The results yield simple threshold rules for single-provider, single-user interactions and clarify when routing, cascading, and throttling help or harm.

**Abstract (Chinese)**

为了缓解性能与成本之间的权衡，大型语言模型（LLM）提供商根据任务难度和延迟将用户任务路由到不同的模型。我们研究了LLM路由相对于用户行为的影响。我们提出了一种栈尔伯格博弈：LLM提供商拥有两个模型（标准模型和推理模型），用户如果被路由的模型无法解决问题，可以重新提示或放弃任务。用户的目标是最大化其效用减去使用模型的延迟，而提供商则最小化服务用户的成本。我们通过完全刻画用户的最优响应并简化提供商问题来求解这一博弈。我们观察到，在几乎所有情况下，最优路由策略涉及一种静态策略，没有级联，且依赖于模型对用户的预期效用。

此外，我们揭示了当用户和提供商对模型在效用和成本方面的排序不同时，提供商最优路由与用户偏好路由之间存在错位差距。最后，我们展示了极端错位条件，其中提供商有动机节流模型的延迟以最小化其成本，从而降低用户效用。这些结果为单提供商、单用户交互提供了简单的阈值规则，并阐明了路由、级联和延迟节流何时有益或有害。

---

### What happens when generative AI models train recursively on each others' outputs?

- **Venue**: ICLR 2026 Poster
- **Authors**: Hung Anh Vu, Galen Reeves, Emily Wenger
- **Keywords**: model collapse, generative AI
- **OpenReview**: https://openreview.net/forum?id=JEU4PBaX85
- **PDF**: https://openreview.net/pdf?id=JEU4PBaX85

**Abstract**

The internet serves as a common source of training data for generative AI (genAI) models but is increasingly populated with AI-generated content. This duality raises the possibility that future genAI models may be trained on other models'  generated outputs. Prior work has studied consequences of models training on their own generated outputs, but limited work has considered what happens if models ingest content produced by other models. Given society's increasing dependence on genAI tools, understanding such data-mediated model interactions is critical. This work provides empirical evidence for how data-mediated interactions might unfold in practice, develops a theoretical model for this interactive training process, and experimentally validates the theory. We find that data-mediated interactions can benefit models by exposing them to novel concepts perhaps missed in original training data, but also can homogenize their performance on shared tasks.

**Abstract (Chinese)**

互联网作为生成式AI（genAI）模型的常见训练数据来源，但日益充斥着AI生成的內容。这种二元性引发了一种可能性，即未来的genAI模型可能使用其他模型生成的输出进行训练。先前工作研究了模型使用自身生成输出进行训练的后果，但鲜有工作考虑模型摄入其他模型生成的内容会发生什么。鉴于社会对genAI工具的日益依赖，理解这种数据介导的模型交互至关重要。本工作提供了数据介导交互在实践中可能如何展开的实证证据，开发了这种交互训练过程的理论模型，并通过实验验证了该理论。我们发现，数据介导的交互可以通过暴露模型于原始训练数据中可能遗漏的新颖概念来惠及模型，但也可能使它们在共享任务上的表现趋于同质化。

---
