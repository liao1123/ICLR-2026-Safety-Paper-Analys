# fairness_bias

**Description**: 公平性/偏见与社会影响。包括 group fairness、bias measurement/mitigation、stereotypes、representation harms、资源分配不均、跨语言/跨文化公平、社会技术影响分析等。

**Paper count**: 31

---

### A Fair Bayesian Inference through Matched Gibbs Posterior

- **Venue**: ICLR 2026 Poster
- **Authors**: Jihu Lee, Kunwoong Kim, Sehyun Park, Insung Kong, Dongyoon Yang, Yongdai Kim
- **Keywords**: Algorithmic fairness, Bayesian inference, Gibbs posterior
- **OpenReview**: https://openreview.net/forum?id=sIjFXzEOOH
- **PDF**: https://openreview.net/pdf?id=sIjFXzEOOH

**Abstract**

With the growing importance of trustworthy AI, algorithmic fairness has emerged as a critical concern. 
Among various fairness notions, group fairness - which measures the model bias between sensitive groups - has received significant attention. 
While many group-fair models have focused on satisfying group fairness constraints, model uncertainty has received relatively little attention, despite its importance for robust and trustworthy decision-making. 
To address this, we adopt a Bayesian framework to capture model uncertainty in fair model training. 
We first define group-fair posterior distributions and then introduce a fair variational Bayesian inference. 
Then we propose a novel distribution termed matched Gibbs posterior, as a proxy distribution for the fair variational Bayesian inference by employing a new group fairness measure, the matched deviation. 
A notable feature of matched Gibbs posterior is that it approximates the posterior distribution well under the fairness constraint without requiring heavy computation. 
Theoretically, we show that the matched deviation has a strong relation to existing group fairness measures, highlighting desirable fairness guarantees. 
Computationally, by treating the matching function in the matched deviation as a learnable parameter, we develop an efficient MCMC algorithm.
Experiments on real-world datasets demonstrates that matched Gibbs posterior outperforms other methods in balancing uncertainty–fairness and utility–fairness trade-offs, while also offering additional desirable properties.

**Abstract (Chinese)**

随着可信AI日益重要，算法公平性已成为一个关键问题。在各种公平性概念中，群体公平性——它衡量敏感群体之间的模型偏差——受到了广泛关注。虽然许多群体公平模型专注于满足群体公平性约束，但模型不确定性尽管对鲁棒和可信决策至关重要，却受到了相对较少的关注。为解决这一问题，我们采用贝叶斯框架在公平模型训练中捕捉模型不确定性。我们首先定义群体公平后验分布，然后引入公平变分贝叶斯推断。然后，我们提出一种新型分布，称为匹配吉布斯后验，作为公平变分贝叶斯推断的代理分布，通过采用一种新的群体公平性度量——匹配偏差。匹配吉布斯后验的一个显著特点是，它在公平性约束下很好地逼近后验分布，而无需大量计算。在理论上，我们证明匹配偏差与现有的群体公平性度量有密切关系，突出了理想的公平性保证。在计算上，通过将匹配偏差中的匹配函数视为可学习参数，我们开发了一种高效的MCMC算法。在真实世界数据集上的实验表明，匹配吉布斯后验在平衡不确定性-公平性和效用-公平性权衡方面优于其他方法，同时还提供了额外的理想属性。

---

### Adaptive Logit Adjustment for Debiasing Multimodal Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Hoin Jung, Junyi Chai, Xiaoqian Wang
- **Keywords**: Large Multimodal Model, Fairness, Image-to-Text, Logit Adjustment
- **OpenReview**: https://openreview.net/forum?id=u02Tgg4UYg
- **PDF**: https://openreview.net/pdf?id=u02Tgg4UYg

**Abstract**

Vision-Language Models (VLMs) and Large Multimodal Models (LMMs) have significantly advanced image-to-text generation tasks such as image captioning and visual question answering (VQA). 
However, these models often exhibit biases, including attribute misalignment between the generated text and the input image, or the reinforcement of harmful stereotypes.
Existing debiasing techniques primarily focus on modifying representations at the encoder or decoder level, which can degrade model performance and may be susceptible to bias reintroduction from external sources. In this work, we propose **Adaptive Logit Adjustment (ALA) for Bias Alignment and Neutralization**, a post-hoc debiasing method that operates directly on logits during autoregressive text generation. Unlike prior approaches that modify internal representations, ALA selectively adjusts token probabilities to mitigate biases without distorting essential model outputs. Our approach leverages external classifiers to measure bias misalignment between image and text, applies gradient-based importance analysis to identify bias-inducing tokens, and dynamically refines token probabilities to reduce undesired biases. 
We evaluate ALA on image captioning and various VQA tasks, demonstrating its effectiveness in mitigating bias while maintaining contextual accuracy. Notably, our approach is applicable to various multimodal architectures in a model-agnostic manner, including VLMs and LMMs, across different tasks that involve autoregressive text generation. Our results show that logit-based debiasing offers a flexible and efficient alternative to existing encoder- and embedding-centric approaches, providing a more practical solution for building fairer multimodal AI systems.

**Abstract (Chinese)**

视觉-语言模型（VLMs）和大型多模态模型（LMMs）已显著提升了图像到文本生成任务的表现，例如图像描述和视觉问答（VQA）。  
然而，这些模型往往表现出偏置，包括生成文本与输入图像之间的属性错位，或强化有害刻板印象。  
现有的去偏置技术主要关注修改编码器或解码器层级的表示，这可能降低模型性能，并易受外部来源偏置重新引入的影响。本文提出**自适应对数几率调整（ALA）用于偏置对齐和中和**，这是一种后处理去偏置方法，直接在自回归文本生成过程中操作对数几率。与先前修改内部表示的方法不同，ALA选择性地调整令牌概率以缓解偏置，同时不扭曲模型的基本输出。我们的方法利用外部分类器测量图像与文本之间的偏置错位，应用基于梯度的显著性分析识别引起偏置的令牌，并动态优化令牌概率以减少 undesired 偏置。  
我们在图像描述和多种VQA任务上评估了ALA，证明其在缓解偏置的同时保持上下文准确性值得注意的是，我们的方法以模型无关的方式适用于各种多模态架构，包括VLMs和LMMs，涵盖涉及自回归文本生成的多种任务。我们的结果表明，基于对数几率的去偏置为现有编码器和嵌入中心方法提供了灵活高效的替代方案，为构建更公平的多模态AI系统提供了更实用的解决方案。

---

### Aligned Agents, Biased Swarm: Measuring Bias Amplification in Multi-Agent Systems

- **Venue**: ICLR 2026 Poster
- **Authors**: Keyu Li, Jin Gao, Dequan Wang
- **Keywords**: Multi-Agent System, Bias Evaluation
- **OpenReview**: https://openreview.net/forum?id=mo7u21GoQv
- **PDF**: https://openreview.net/pdf?id=mo7u21GoQv

**Abstract**

The AI landscape is currently driven by two transformative trends: the rapid advancement of highly capable autonomous models like Claude Code and Codex, and their transition into collaborative Multi-Agent Systems (MAS), such as Agent Teams and Agent Swarms, engineered for complex, long-horizon problem-solving. While extensive alignment efforts have successfully mitigated biases within individual models, the accumulation and evolution of prejudice across interconnected agent networks remains a critical, unexplored vulnerability. A prevailing assumption is that deploying diverse, specialized agents within structured workflows naturally dilutes bias. In this work, we hypothesize the opposite: the complex topologies and feedback loops inherent in MAS act as echo chambers, amplifying minor stochastic biases into systemic opinion polarization. To systematically investigate this, we introduce Discrim-Eval-Open, an open-ended benchmark designed to bypass the performative neutrality of individual models by requiring comparative judgments across gender, age, and race. Using novel distributional metrics, we evaluate how bias cascades across various agent roles, communication structures, and system depths. Our empirical findings reveal a stark reality: the architectural sophistication designed to enhance MAS frequently exacerbates bias rather than mitigating it. We observe systemic amplification favoring younger demographics, females, and Black communities, even when single agents operate neutrally in isolation. Furthermore, we identify a severe 'Trigger Vulnerability,' demonstrating that injecting purely objective, factual context into a multi-agent workflow drastically accelerates this polarization. Ultimately, our results illustrate that structural complexity does not guarantee ethical robustness, reframing bias as a volatile emergent property in MAS that demands immediate scrutiny. Our code is available at https://github.com/weizhihao1/MAS-Bias.

**Abstract (Chinese)**

当前 AI 格局由两大变革性趋势驱动：高度自主模型（如 Claude Code 和 Codex）的快速发展，以及它们向协作式多代理系统 (MAS) 的转型，例如代理团队和代理群，这些系统专为复杂、长时程问题求解而设计。尽管广泛的对齐努力已成功缓解了个体模型内的偏见，但互联代理网络中偏见的积累和演化仍是一个关键的、未被探索的漏洞。一种普遍假设认为，在结构化工作流程中部署多样化、专业化的代理会自然稀释偏见。在本工作中，我们提出相反假设：MAS 中固有的复杂拓扑和反馈循环充当回音室，将细微的随机偏见放大为系统性意见两极化。为了系统性探究这一问题，我们引入 Discrim-Eval-Open，这是一个开放式基准，旨在通过要求跨性别、年龄和种族的比较判断来绕过个体模型的表演性中立。利用新型分布度量，我们评估偏见如何在各种代理角色、通信结构和系统深度中级联传播。我们的实证发现揭示了一个严峻现实：旨在提升 MAS 的架构复杂性往往会加剧偏见而非缓解它。我们观察到系统性放大有利于年轻人口统计群体、女性和黑人社区，即使单个代理在孤立状态下运作中立。此外，我们识别出一种严重的“触发漏洞”，证明在多代理工作流程中注入纯客观、事实性上下文会急剧加速这种两极化。最终，我们的结果表明，结构复杂性并不能保证伦理鲁棒性，将偏见重构为 MAS 中一种易变的涌现属性，需要立即审视。我们的代码可在 https://github.com/weizhihao1/MAS-Bias 获取。

---

### Bi-directional Bias Attribution: Debiasing Large Language Models without Modifying Prompts

- **Venue**: ICLR 2026 Poster
- **Authors**: Yujie Lin, Kunquan Li, YiXuan Liao, Xiaoxin Chen, Jinsong Su
- **Keywords**: Large language models; Algorithmic fairness; Social bias
- **OpenReview**: https://openreview.net/forum?id=mUTN9VIaSy
- **PDF**: https://openreview.net/pdf?id=mUTN9VIaSy

**Abstract**

Large language models (LLMs) have demonstrated impressive capabilities across a wide range of natural language processing tasks. However, their outputs often exhibit social biases, raising fairness concerns. Existing debiasing methods, such as fine-tuning on additional datasets or prompt engineering, face scalability issues or compromise user experience in multi-turn interactions. To address these challenges, we propose a framework for detecting stereotype-inducing words and attributing neuron-level bias in LLMs, without the need for fine-tuning or prompt modification. Our framework first identifies stereotype-inducing adjectives and nouns via comparative analysis across demographic groups. We then attribute biased behavior to specific neurons using two attribution strategies based on integrated gradients. Finally, we mitigate bias by directly intervening on their activations at the projection layer. Experiments on three widely used LLMs demonstrate that our method effectively reduces bias while preserving overall model performance.

**Abstract (Chinese)**

大型语言模型 (LLMs) 在广泛的自然语言处理任务中展现了令人印象深刻的性能。然而，它们的输出常常表现出社会偏见，从而引发公平性担忧。现有的去偏见方法，如在额外数据集上进行微调或提示工程，面临可扩展性问题，或在多轮交互中损害用户体验。为应对这些挑战，我们提出了一种框架，用于检测大型语言模型中引发刻板印象的词语并归因神经元级偏见，而无需微调或提示修改。该框架首先通过跨人口统计群体比较分析，识别引发刻板印象的形容词和名词。然后，我们使用基于集成梯度的两种归因策略，将偏见行为归因于特定神经元。最后，我们通过直接干预投影层上的激活值来缓解偏见。在三个广泛使用的 LLMs 上的实验表明，我们的方法有效降低了偏见，同时保留了模型的整体性能。

---

### Bias Similarity Measurement: A Black-Box Audit of Fairness Across LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Hyejun Jeong, Shiqing Ma, Amir Houmansadr
- **Keywords**: LLM, Bias and Fairness, Fairness Auditing, Bias Measurement
- **OpenReview**: https://openreview.net/forum?id=EveruzAsGI
- **PDF**: https://openreview.net/pdf?id=EveruzAsGI

**Abstract**

Large Language Models (LLMs) reproduce social biases, yet prevailing evaluations score models in isolation, obscuring how biases persist across families and releases. We introduce Bias Similarity Measurement (BSM), which treats fairness as a relational property between models, unifying scalar, distributional, behavioral, and representational signals into a single similarity space. Evaluating 30 LLMs on 1M+ prompts, we find that instruction tuning primarily enforces abstention rather than altering internal representations; small models gain little accuracy and can become less fair under forced choice; and in our evaluation setting, open-weight models can match or exceed proprietary systems. Family signatures diverge: Gemma favors refusal, LLaMA 3.1 approaches neutrality with fewer refusals, and converges toward abstention-heavy behavior overall. Counterintuitively, Gemma 3 Instruct matches GPT-4--level fairness at far lower cost, whereas Gemini’s heavy abstention suppresses utility. Beyond these findings, BSM offers an auditing workflow for procurement, regression testing, and lineage screening, and extends naturally to code and multilingual settings. Our results reframe fairness not as isolated scores but as comparative bias similarity, enabling systematic auditing of LLM ecosystems. Code is available at https://github.com/HyejunJeong/bias_llm.

**Abstract (Chinese)**

大语言模型 (LLMs) 会再现社会偏见，然而，现有的评估方法孤立地对模型进行评分，从而掩盖了偏见在不同模型家族和版本间的持久性。我们引入了偏见相似性度量 (BSM)，它将公平性视为模型之间的关系属性，将标量、分布、行为和表征信号统一到一个单一的相似性空间中。我们在超过 100 万个提示上评估了 30 个 LLMs，发现指令调优主要强制执行弃权，而不是改变内部表征；小型模型在准确性上获益甚微，并且在强制选择下可能变得不那么公平；在我们的评估设置中，开源权重模型可以匹配或超过专有系统。家族特征各异：Gemma 倾向于拒绝，LLaMA 3.1 通过减少拒绝接近中立性，并且整体趋向于高度弃权的表现。出人意料的是，Gemma 3 Instruct 以远更低的成本达到了与 GPT-4 相当的公平性水平，而 Gemini 的高度弃权抑制了其实用性。除了这些发现之外，BSM 提供了一个用于采购、回归测试和谱系筛选的审计工作流程，并自然扩展到代码和多语言设置。我们的结果将公平性重新框架为比较偏见相似性而非孤立的评分，从而实现了对 LLM 生态系统的系统审计。代码可在 https://github.com/HyejunJeong/bias_llm 获取。

---

### BiasBusters: Uncovering and Mitigating Tool Selection Bias in Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Thierry Blankenstein, Jialin Yu, Zixuan Li, Vassilis Plachouras, Sunando Sengupta, Philip Torr, Yarin Gal, Alasdair Paren, Adel Bibi
- **Keywords**: Tool Selection, LLM Agents, Fairness, Bias
- **OpenReview**: https://openreview.net/forum?id=DEg4vvElYu
- **PDF**: https://openreview.net/pdf?id=DEg4vvElYu

**Abstract**

Agents backed by large language models (LLMs) increasingly rely on external tools drawn from marketplaces where multiple providers offer functionally equivalent options. This raises a critical fairness concern: systematic bias in tool selection can degrade user experience and distort competition by privileging certain providers over others. We introduce a benchmark of diverse tool categories, each containing multiple functionally equivalent tools, to systematically evaluate tool-selection bias. Using this benchmark, we evaluate seven LLMs and show that substantial bias persists, with models either fixating on a single provider or disproportionately favoring tools that appear earlier in the context. To uncover the sources of this behavior, we conduct controlled experiments that isolate the effects of tool features, exposed metadata (name, description, and parameters), and pre-training exposure. We find that (1) semantic alignment between user queries and tool metadata is the strongest driver of selection; (2) small perturbations to tool descriptions can significantly shift choices; and (3) repeated pre-training exposure to a single endpoint amplifies provider-level bias. Finally, we propose a lightweight mitigation strategy that first filters tools to a relevant subset and then samples uniformly, substantially reducing selection bias while maintaining strong task coverage. Our results highlight tool-selection bias as a key obstacle to the fair deployment of tool-augmented LLM agents.

**Abstract (Chinese)**

由大型语言模型（LLMs）支持的代理越来越多地依赖于从市场中抽取的外部工具，这些市场中多个提供商提供功能等价的选项。这引发了一个关键的公平性问题：工具选择中的系统性偏差可能会降低用户体验，并通过优先选择某些提供商而扭曲竞争。我们引入了一个包含多样工具类别的基准，每个类别包含多个功能等价的工具，以系统地评估工具选择偏差。使用该基准，我们评估了七个LLMs，并显示出显著的偏差依然存在，模型要么固着于单一提供商，要么不成比例地偏好上下文中出现的较早工具。为了揭示这种行为的原因，我们进行了控制实验，隔离了工具特征、暴露元数据（名称、描述和参数）以及预训练暴露的影响。我们发现：(1) 用户查询与工具元数据之间的语义对齐是选择的最强驱动因素；(2) 对工具描述的小扰动可以显著改变选择；(3) 对单一端点的重复预训练暴露会放大提供商级偏差。最后，我们提出了一种轻量级缓解策略，首先将工具过滤到相关子集，然后均匀采样，从而在保持强大任务覆盖的同时显著减少选择偏差。我们的结果突显了工具选择偏差作为工具增强LLM代理公平部署的关键障碍。

---

### BiasFreeBench: a Benchmark for Mitigating Bias in Large Language Model Responses

- **Venue**: ICLR 2026 Poster
- **Authors**: Xin Xu, Xunzhi He, Churan Zhi, Ruizhe Chen, Julian McAuley, Zexue He
- **Keywords**: debiasing large language models, bias mitigation, social bias
- **OpenReview**: https://openreview.net/forum?id=Ncf2LFDT4e
- **PDF**: https://openreview.net/pdf?id=Ncf2LFDT4e

**Abstract**

Existing studies on bias mitigation methods for large language models (LLMs) use diverse baselines and metrics to evaluate debiasing performance, leading to inconsistent comparisons among them. Moreover, their evaluations are mostly based on the comparison between LLMs' probabilities of biased and unbiased contexts, which ignores the gap between such evaluations and real-world use cases where users interact with LLMs by reading model responses and expect fair and safe outputs rather than LLMs' probabilities. To enable consistent evaluation across debiasing methods and bridge this gap, we introduce **BiasFreeBench**, an empirical benchmark that comprehensively compares eight mainstream bias mitigation techniques (covering four prompting-based and four training-based methods) on two test scenarios (multi-choice QA and open-ended multi-turn QA) by reorganizing existing datasets into a unified query-response setting. We further introduce a response-level metric, **Bias-Free Score**, to measure the extent to which LLM responses are fair, safe, and anti-stereotypical. Debiasing performances are systematically compared and analyzed across key dimensions: the prompting vs. training paradigm, model size, and generalization of different training strategies to unseen bias types. We release our benchmark, aiming to establish a unified testbed for bias mitigation research [https://github.com/xxupiano/BiasFreeBench](https://github.com/xxupiano/BiasFreeBench).

**Abstract (Chinese)**

现有的大型语言模型 (LLMs) 偏见缓解方法研究使用了多种基线和指标来评估去偏见性能，导致它们之间的比较不一致。此外，它们的评估主要基于 LLMs 对偏见和无偏见上下文概率的比较，这忽略了此类评估与真实世界用例之间的差距，在真实世界用例中，用户通过阅读模型响应与 LLMs 交互，并期望公平和安全的输出，而不是 LLMs 的概率。为了实现去偏见方法之间的一致评估并弥合这一差距，我们引入了 **BiasFreeBench**，这是一个实证基准，通过将现有数据集重组为统一的查询-响应设置，在两个测试场景（多选问答和开放式多轮问答）上全面比较了八种主流偏见缓解技术（涵盖四种基于提示的方法和四种基于训练的方法）。我们进一步引入了一个响应级指标 **Bias-Free Score**，用于衡量 LLM 响应在公平、安全和反刻板印象方面的程度。去偏见性能在关键维度上进行了系统比较和分析：提示 vs. 训练范式、模型规模，以及不同训练策略对未见偏见类型的泛化能力。我们发布了我们的基准，旨在为偏见缓解研究建立一个统一的测试平台 [https://github.com/xxupiano/BiasFreeBench](https://github.com/xxupiano/BiasFreeBench)。

---

### BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation

- **Venue**: ICLR 2026 Poster
- **Authors**: Peng Lai, Zhihao Ou, Yong Wang, Longyue Wang, Jian Yang, Yun Chen, Guanhua Chen
- **Keywords**: LLM-as-a-Judge, bias
- **OpenReview**: https://openreview.net/forum?id=QGOw6AU8Lp
- **PDF**: https://openreview.net/pdf?id=QGOw6AU8Lp

**Abstract**

LLM-as-a-Judge has been widely adopted across various research and practical applications, yet the robustness and reliability of its evaluation remain a critical issue. A core challenge it faces is bias, which has primarily been studied in terms of known biases and their impact on evaluation outcomes, while automated and systematic exploration of potential unknown biases is still lacking. Nevertheless, such exploration is crucial for enhancing the robustness and reliability of evaluations. To bridge this gap, we propose BiasScope, a LLM-driven framework for automatically and at scale discovering potential biases that may arise during model evaluation. BiasScope can uncover potential biases across different model families and scales, with its generality and effectiveness validated on the JudgeBench dataset. It overcomes the limitations of existing approaches, transforming bias discovery from a passive process relying on manual effort and predefined bias lists into an active and comprehensive automated exploration. Moreover, based on BiasScope, we propose JudgeBench-Pro, an extended version of JudgeBench and a more challenging benchmark for evaluating the robustness of LLM-as-a-judge. Strikingly, even powerful LLMs as evaluators show error rates above 50\% on JudgeBench-Pro, underscoring the urgent need to strengthen evaluation robustness and to mitigate potential biases further.

**Abstract (Chinese)**

LLM-as-a-Judge 已广泛应用于各种研究和实际场景中，然而其评估的鲁棒性和可靠性仍是一个关键问题。它面临的核心挑战是偏见，该偏见主要从已知偏见及其对评估结果的影响方面进行了研究，而对潜在未知偏见的自动化和系统性探索仍显不足。尽管如此，此类探索对于提升评估的鲁棒性和可靠性至关重要。为弥合这一差距，我们提出了 BiasScope，这是一个由 LLM 驱动的框架，用于大规模自动发现模型评估过程中可能出现的潜在偏见。BiasScope 能够揭示不同模型家族和规模下的潜在偏见，其通用性和有效性在 JudgeBench 数据集上得到了验证。它克服了现有方法的局限性，将偏见发现从依赖手动努力和预定义偏见列表的被动过程转变为主动且全面的自动化探索。此外，基于 BiasScope，我们提出了 JudgeBench-Pro，这是 JudgeBench 的扩展版本，也是评估 LLM-as-a-Judge 鲁棒性的一项更具挑战性的基准。令人震惊的是，即使是强大的 LLM 作为评估者，在 JudgeBench-Pro 上也显示出超过 50% 的错误率，这突显了加强评估鲁棒性和进一步缓解潜在偏见的迫切需求。

---

### Bridging Fairness and Explainability: Can Input-Based Explanations Promote Fairness in Hate Speech Detection?

- **Venue**: ICLR 2026 Poster
- **Authors**: Yifan Wang, Mayank Jobanputra, Ji-Ung Lee, Soyoung Oh, Isabel Valera, Vera Demberg
- **Keywords**: Fairness, Explainability, Hate speech detection
- **OpenReview**: https://openreview.net/forum?id=fPMu3Afv3s
- **PDF**: https://openreview.net/pdf?id=fPMu3Afv3s

**Abstract**

Natural language processing (NLP) models often replicate or amplify social bias from training data, raising concerns about fairness.
At the same time, their black-box nature makes it difficult for users to recognize biased predictions and for developers to effectively mitigate them.
While some studies suggest that input-based explanations can help detect and mitigate bias, others question their reliability in ensuring fairness.
Existing research on explainability in fair NLP has been predominantly qualitative, with limited large-scale quantitative analysis.
In this work, we conduct the first systematic study of the relationship between explainability and fairness in hate speech detection, focusing on both encoder- and decoder-only models.
We examine three key dimensions: (1) identifying biased predictions, (2) selecting fair models, and (3) mitigating bias during model training.
Our findings show that input-based explanations can effectively detect biased predictions and serve as useful supervision for reducing bias during training, but they are unreliable for selecting fair models among candidates.
Our code is available at https://github.com/Ewanwong/fairness_x_explainability.

**Abstract (Chinese)**

自然语言处理 (NLP) 模型常常复制或放大训练数据中的社会偏见，从而引发公平性担忧。

同时，其黑箱性质使得用户难以识别偏见预测，开发者也难以有效缓解这些偏见。

虽然一些研究表明基于输入的解释有助于检测和缓解偏见，但其他研究质疑其在确保公平性方面的可靠性。

现有关于公平 NLP 中可解释性的研究主要为定性研究，大规模定量分析有限。

在本工作中，我们对仇恨言论检测中可解释性和公平性之间的关系进行了首次系统性研究，重点关注仅编码器模型和仅解码器模型。

我们考察了三个关键维度：(1) 识别偏见预测，(2) 选择公平模型，以及 (3) 在模型训练过程中缓解偏见。

我们的发现表明，基于输入的解释可以有效检测偏见预测，并作为训练过程中减少偏见的有效监督，但它们在候选模型中选择公平模型方面不可靠。

我们的代码可在 https://github.com/Ewanwong/fairness_x_explainability 获取。

---

### Data Aware and Scalable Sensitivity Analysis for Decision Tree Ensembles

- **Venue**: ICLR 2026 Poster
- **Authors**: Arhaan Ahmad, S. Akshay, Ashutosh Gupta, Tanay Vineet Tayal, Namrita Varshney
- **Keywords**: Robustness verification, Sensitivity analysis, SAT solvers, efficient encodings, NP-hardness, fairness, confidence, decision tree ensembles, MultiClass
- **OpenReview**: https://openreview.net/forum?id=q8KqAvdfZK
- **PDF**: https://openreview.net/pdf?id=q8KqAvdfZK

**Abstract**

Decision tree ensembles are widely used in critical domains, making robustness and sensitivity analysis essential to their trustworthiness. We study the feature sensitivity problem, which asks whether an ensemble is ``sensitive" to a specified subset of features - such as protected attributes- whose manipulation can alter model predictions. Existing approaches often yield examples of sensitivity that lie far from the training distribution, limiting their interpretability and practical value. We propose a data-aware sensitivity framework that constrains the sensitive examples to remain close to the dataset, thereby producing realistic and interpretable evidence of model weaknesses. To this end, we develop novel techniques for data-aware search using a combination of mixed-integer linear programming (MILP) and satisfibility modulo theories (SMT) encodings. Our contributions are fourfold. Firstly, we strengthen the NP-hardness result for sensitivity verification, showing it holds even for trees of depth 1. Secondly, we develop MILP-optimizations that significantly speed up sensitivity verification for single ensembles and for the first time can also handle multiclass tree ensembles. Thirdly we introduce a data-aware framework generating realistic examples near the training distribution. Finally, we conduct an extensive experimental evaluation on large tree ensembles, demonstrating scalability to ensembles with up to 800 trees of depth 8, achieving substantial improvements over the state of the art. This framework provides a practical foundation for analyzing the reliability and fairness of tree-based models in high-stakes applications.

**Abstract (Chinese)**

决策树集成在关键领域中被广泛使用，这使得鲁棒性和敏感性分析对其可信度至关重要。我们研究了特征敏感性问题，该问题询问集成是否对指定特征子集（如受保护属性）“敏感”——操纵这些特征可能会改变模型预测。现有的方法往往产生远离训练分布的敏感性示例，从而限制了其可解释性和实际价值。我们提出了一种数据感知敏感性框架，该框架约束敏感性示例保持接近数据集，从而产生模型弱点的真实且可解释证据。为此，我们开发了结合混合整数线性规划（MILP）和模理论可满足性（SMT）编码的数据感知搜索新型技术。我们的贡献有四方面。首先，我们强化了敏感性验证的 NP 困难性结果，证明其即使对深度为 1 的树也成立。其次，我们开发了 MILP 优化技术，这些技术显著加速了单个集成的敏感性验证，并首次能够处理多类决策树集成。第三，我们引入了一种数据感知框架，用于生成接近训练分布的真实示例。最后，我们在大规模决策树集成上进行了广泛的实验评估，证明了其可扩展性，能够处理多达 800 棵深度为 8 的树的集成，并在当前最先进方法上实现了显著改进。该框架为分析高风险应用中基于树的模型的可靠性和公平性提供了实用基础。

---

### Doubly-Regressing Approach for Subgroup Fairness

- **Venue**: ICLR 2026 Poster
- **Authors**: Kunwoong Kim, Kyungseon Lee, Jihu Lee, Dongyoon Yang, Yongdai Kim
- **Keywords**: Algorithmic fairness, Subgroup, Adversarial learning, Data sparsity
- **OpenReview**: https://openreview.net/forum?id=17UDRTRLmp
- **PDF**: https://openreview.net/pdf?id=17UDRTRLmp

**Abstract**

Algorithmic fairness is a socially crucial topic in real-world applications of AI.
Among many notions of fairness, subgroup fairness is widely studied when multiple sensitive attributes (e.g., gender, race, and age) are present.
However, as the number of sensitive attributes grows, the number of subgroups increases accordingly, creating heavy computational burden and data sparsity problem (i.e., subgroups with very small sample sizes).
In this paper, we develop a novel learning algorithm for subgroup fairness that resolves these issues by focusing on sufficiently large subgroups as well as marginal fairness (fairness for each sensitive attribute).
To this end, we formalize a notion of subgroup-subset fairness and introduce a corresponding distributional fairness measure called the supremum Integral Probability Metric (supIPM).
Building on this formulation, we propose the Doubly Regressing Adversarial learning for subgroup Fairness (DRAF) algorithm, which reduces a surrogate fairness gap for supIPM with much less computation than directly reducing supIPM.
Theoretically, we prove that the proposed surrogate fairness gap is an upper bound of supIPM.
Empirically, we show that the DRAF algorithm outperforms baseline methods on benchmark datasets, particularly when the number of sensitive attributes is large so that many subgroups are very small.

**Abstract (Chinese)**

算法公平性是人工智能在现实世界应用中的一个社会关键主题。在众多公平性概念中，当存在多个敏感属性（如性别、种族和年龄）时，子组公平性得到了广泛研究。然而，随着敏感属性的数量增加，子组的数量随之增加，从而导致沉重的计算负担和数据稀疏问题（即样本量非常小的子组）。在本文中，我们开发了一种新型子组公平性学习算法，通过关注足够大的子组以及边际公平性（每个敏感属性的公平性）来解决这些问题。为此，我们形式化了子组-子集公平性的概念，并引入了一种相应的分布公平性度量，称为上确界积分概率度量（supIPM）。基于这一形式化，我们提出了双回归对抗学习用于子组公平性（DRAF）算法，该算法通过比直接减少 supIPM 少得多的计算来减少 supIPM 的代理公平性差距。理论上，我们证明了所提出的代理公平性差距是 supIPM 的上界。实证上，我们展示了 DRAF 算法在基准数据集上优于基线方法，特别是当敏感属性的数量较大从而许多子组非常小时。

---

### Fair Classification by Direct Intervention on Operating Characteristics

- **Venue**: ICLR 2026 Poster
- **Authors**: Kevin Jiang, Edgar Dobriban
- **Keywords**: algorithmic fairness; post-processing; linear-fractional constraints; minimal interventions; constrained optimization
- **OpenReview**: https://openreview.net/forum?id=Vv3PGcSn7c
- **PDF**: https://openreview.net/pdf?id=Vv3PGcSn7c

**Abstract**

We develop new classifiers under group fairness in the attribute-aware setting for binary classification with multiple group fairness constraints (e.g., demographic parity (DP), equalized odds (EO), and predictive parity (PP)). 
We propose a novel approach based on directly intervening on the operating characteristics of a pre-trained base classifier, by: 
(i) identifying optimal operating characteristics using the base classifier's group-wise ROC convex hulls; 
(ii) post-processing the base classifier to match those targets.
As practical post-processors,
we consider randomizing a mixture of group-wise thresholding rules subject to minimizing the expected number of interventions. 
We further extend our approach to handle multiple protected attributes and multiple linear fractional constraints.
On standard datasets (COMPAS and ACSIncome), 
our method simultaneously 
satisfies approximate DP, EO, and PP with few interventions and a nearly optimal drop in accuracy; and compare favorably to previous methods.

**Abstract (Chinese)**

我们开发了在属性感知设置下群体公平性的新型分类器，用于具有多重群体公平约束（例如，人口统计平价 (DP)、等化几率 (EO) 和预测平价 (PP)）的二元分类。

我们提出了一种新颖的方法，该方法基于直接干预预训练基础分类器的操作特性，通过：

(i) 使用基础分类器的群体特定 ROC 凸包识别最优操作特性；

(ii) 后处理基础分类器以匹配这些目标。

作为实际的后处理器，

我们考虑随机化群体特定阈值规则的混合，受最小化预期干预次数的约束。

我们进一步扩展我们的方法以处理多个受保护属性和多个线性分数约束。

在标准数据集 (COMPAS 和 ACSIncome) 上，

我们的方法同时

以少量干预满足近似的 DP、EO 和 PP，并具有几乎最优的准确率下降；并且与先前方法相比表现优异。

---

### Fair Conformal Classification via Learning Representation-Based Groups

- **Venue**: ICLR 2026 Poster
- **Authors**: Senrong Xu, Yanke Zhou, Yuhao Tan, Zenan Li, Yuan Yao, Taolue Chen, Feng Xu, Xiaoxing Ma
- **Keywords**: Classification; Conformal Prediction; Equalized Coverage; Fairness
- **OpenReview**: https://openreview.net/forum?id=aa91WoBZeg
- **PDF**: https://openreview.net/pdf?id=aa91WoBZeg

**Abstract**

Conformal prediction methods provide statistically rigorous marginal coverage guarantees for machine learning models, but such guarantees fail to account for algorithmic biases, thereby undermining fairness and trust. This paper introduces a fair conformal inference framework for classification tasks. The proposed method constructs prediction sets that guarantee conditional coverage on adaptively identified subgroups, which can be implicitly defined through nonlinear feature combinations. By balancing effectiveness and efficiency in producing compact, informative prediction sets and ensuring adaptive equalized coverage across unfairly treated subgroups, our approach paves a practical pathway toward trustworthy machine learning. Extensive experiments on both synthetic and real-world datasets demonstrate the effectiveness of the framework.

**Abstract (Chinese)**

保形预测方法为机器学习模型提供了统计上严格的边际覆盖保证，但此类保证未能考虑算法偏差，从而破坏了公平性和信任。本文提出了一种用于分类任务的公平保形推理框架。所提出方法构建预测集，这些预测集在自适应识别的子群上保证条件覆盖，这些子群可以通过非线性特征组合隐式定义。通过在生成紧凑、信息丰富的预测集方面的有效性和效率之间取得平衡，并确保跨不公平对待子群的自适应均衡覆盖，我们的方法为可信赖的机器学习铺平了实用途径。在合成和真实世界数据集上的广泛实验证明了该框架的有效性。

---

### Fair Decision Utility in Human-AI Collaboration: Interpretable Confidence Adjustment for Humans with Cognitive Disparities

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiashi Gao, Kexin Liu, Xinwei Guo, Junlei Zhou, Jiaxin Zhang, Xiangyu Zhao, Guanhua Chen, Xin Yao, Xuetao Wei
- **Keywords**: Fairness, AI-assisted decision making
- **OpenReview**: https://openreview.net/forum?id=hqq6GyYISN
- **PDF**: https://openreview.net/pdf?id=hqq6GyYISN

**Abstract**

In AI-assisted decision-making, human decision-makers finalize decisions by taking into account both their human confidence and AI confidence regarding specific outcomes.  In practice, they often exhibit heterogeneous cognitive capacities, causing their confidence to deviate, sometimes significantly, from the actual label likelihood. We theoretically demonstrate that existing AI confidence adjustment objectives, such as *calibration* and *human-alignment*, are insufficient to ensure fair utility across groups of decision-makers with varying cognitive capacities. Such unfairness may raise concerns about social welfare and may erode human trust in AI systems.
To address this issue, we introduce a new concept in AI confidence adjustment: *inter-group-alignment*. By theoretically bounding the utility disparity between human decision-maker groups as a function of  *human-alignment* level and *inter-group-alignment* level, we establish an interpretable fairness-aware objective for AI confidence adjustment. Our analysis suggests that achieving utility fairness in AI-assisted decision-making requires both *human-alignment* and *inter-group-alignment*. Building on these objectives, we propose a multicalibration-based AI confidence adjustment approach tailored to scenarios involving human decision-makers with heterogeneous cognitive capacities. We further provide theoretical justification showing that our method constitutes a sufficient condition for achieving both *human-alignment* and *inter-group-alignment*.
We validate our theoretical findings through extensive experiments on four real-world tasks. The results demonstrate that AI confidence adjusted toward both *human-alignment* and *inter-group-alignment* significantly improves utility fairness across human decision-maker groups, without sacrificing overall utility.
*The implementation code is available at* https://github.com/WEILaboratory/AI-Ethics-Safety-PaperCode/tree/main/Fair_HAI (ICLR2026).

**Abstract (Chinese)**

在AI辅助决策中，人类决策者通过同时考虑特定结果的人类置信度和AI置信度来最终确定决策。在实践中，他们往往表现出异质的认知能力，导致其置信度有时显著偏离实际标签似然。我们从理论上证明，现有的AI置信度调整目标（如校准和人类对齐）不足以确保不同认知能力决策者群体间的效用公平。这种不公平可能引发社会福利担忧，并侵蚀人类对AI系统的信任。

为解决这一问题，我们在AI置信度调整中引入了一个新概念：组间对齐。通过从理论上将人类决策者群体间的效用差异界定为人类对齐水平和组间对齐水平函数，我们确立了一个可解释的公平感知AI置信度调整目标。我们的分析表明，实现AI辅助决策中的效用公平需要同时实现人类对齐和组间对齐。在此基础上，我们提出了一种基于多校准的AI置信度调整方法，专为涉及异质认知能力人类决策者的场景量身定制。我们进一步提供了理论证明，表明我们的方法构成了实现人类对齐和组间对齐的充分条件。

我们通过在四个真实世界任务上的广泛实验验证了我们的理论发现。结果表明，向人类对齐和组间对齐调整的AI置信度显著提升了人类决策者群体间的效用公平，同时不牺牲整体效用。

实现代码可在以下链接获取：https://github.com/WEILaboratory/AI-Ethics-Safety-PaperCode/tree/main/Fair_HAI (ICLR2026)。

---

### Fair Graph Machine Learning under Adversarial Missingness Processes

- **Venue**: ICLR 2026 Poster
- **Authors**: Debolina Halder Lina, Arlei Silva
- **Keywords**: Fairness, GNN, Missingness
- **OpenReview**: https://openreview.net/forum?id=WgZJCnb8lJ
- **PDF**: https://openreview.net/pdf?id=WgZJCnb8lJ

**Abstract**

Graph Neural Networks (GNNs) have achieved state-of-the-art results in many relevant tasks where decisions might disproportionately impact specific communities. However, existing work on fair GNNs often assumes that either sensitive attributes are fully observed or they are missing completely at random. We show that an adversarial missingness process can inadvertently disguise a fair model through the imputation, leading the model to overestimate the fairness of its predictions. We address this challenge by proposing Better Fair than Sorry (BFtS), a fair missing data imputation model for sensitive attributes. The key principle behind BFtS is that imputations should approximate the worst-case scenario for fairness---i.e. when optimizing fairness is the hardest. We implement this idea using a 3-player adversarial scheme where two adversaries collaborate against a GNN classifier, and the classifier minimizes the maximum bias. Experiments using synthetic and real datasets show that BFtS often achieves a better fairness x accuracy trade-off than existing alternatives under an adversarial missingness process.

**Abstract (Chinese)**

图神经网络（GNNs）在许多相关任务中取得了最先进的结果，这些任务中的决策可能对特定社区产生不成比例的影响。然而，现有的公平 GNNs 工作通常假设敏感属性要么完全观察到，要么完全随机缺失。我们证明，对抗性缺失过程可以通过插补无意中掩盖一个公平模型，导致模型高估其预测的公平性。我们通过提出 Better Fair than Sorry（BFtS），一种针对敏感属性的公平缺失数据插补模型，来解决这一挑战。BFtS 背后的关键原则是，插补应近似公平性的最坏情形——即优化公平性最困难的情形。我们使用一个三玩家对抗方案来实现这一思想，其中两个对抗者协作对抗 GNN 分类器，而分类器最小化最大偏差。使用合成和真实数据集的实验表明，在对抗性缺失过程下，BFtS 通常比现有备选方案实现了更好的公平性 × 准确性权衡。

---

### Fair in Mind, Fair in Action? A Synchronous Benchmark for Understanding and Generation in UMLLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Yiran Zhao, Lu Zhou, Xiaogang Xu, Zhe Liu, Jiafei Wu, Liming Fang
- **Keywords**: AI Fairness, Unified Multimodal Large Language Models (UMLLMs), Fairness Benchmark, Cross-Task Evaluation, Bias Measurement
- **OpenReview**: https://openreview.net/forum?id=NYphgYTloq
- **PDF**: https://openreview.net/pdf?id=NYphgYTloq

**Abstract**

As artificial intelligence (AI) is increasingly deployed across domains, ensuring fairness has become a core challenge. However, the field faces a "Tower of Babel'' dilemma: fairness metrics abound, yet their underlying philosophical assumptions often conflict, hindering unified paradigms—particularly in unified Multimodal Large Language Models (UMLLMs), where biases propagate systemically across tasks. To address this, we introduce the IRIS Benchmark, to our knowledge the first benchmark designed to synchronously evaluate the fairness of both understanding and generation tasks in UMLLMs. Enabled by our demographic classifier, ARES, and four supporting large-scale datasets, the benchmark is designed to normalize and aggregate arbitrary metrics into a high-dimensional "fairness space'', integrating 60 granular metrics across three dimensions—Ideal Fairness, Real-world Fidelity, and Bias Inertia & Steerability (IRIS). Through this benchmark, our evaluation of leading UMLLMs uncovers systemic phenomena such as the "generation gap'', individual inconsistencies like "personality splits'', and the "counter-stereotype reward'', while offering diagnostics to guide the optimization of their fairness capabilities. With its novel and extensible framework, the IRIS benchmark is capable of integrating evolving fairness metrics, ultimately helping to resolve the "Tower of Babel'' impasse.

**Abstract (Chinese)**

随着人工智能（AI）在各领域日益广泛部署，确保公平性已成为核心挑战。然而，该领域面临“巴别塔”困境：公平性指标层出不穷，但其底层哲学假设往往冲突，从而阻碍统一范式的形成——特别是在统一多模态大语言模型（UMLLMs）中，偏见会系统性地跨任务传播。为解决这一问题，我们引入IRIS基准，据我们所知，这是首个专为同步评估UMLLMs中理解和生成任务公平性而设计的基准。在我们的人口统计分类器ARES和四个支持性大规模数据集的赋能下，该基准旨在将任意指标归一化和聚合到一个高维“公平空间”中，整合了跨越三个维度的60个细粒度指标——理想公平性、现实世界保真度，以及偏见惯性与可操控性（IRIS）。通过该基准，我们对领先UMLLMs的评估揭示了诸如“生成差距”等系统性现象、“人格分裂”等个体不一致性，以及“反刻板印象奖励”，同时提供了诊断工具以指导其公平性能力的优化。凭借其新颖且可扩展的框架，IRIS基准能够整合不断演进的公平性指标，最终有助于化解“巴别塔”僵局。

---

### Fairness via Independence: A General Regularization Framework for Machine Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Yezi Liu, Hanning Chen, Wenjun Huang, Yang Ni, Mohsen Imani
- **Keywords**: Bias Mitigation, Statistical Independence, Fairness in Machine Learning
- **OpenReview**: https://openreview.net/forum?id=sbEb0Ld6MK
- **PDF**: https://openreview.net/pdf?id=sbEb0Ld6MK

**Abstract**

Fairness in machine learning has emerged as a central concern, as predictive models frequently inherit or even amplify biases present in training data. Such biases often manifest as unintended correlations between model outcomes and sensitive attributes, leading to systematic disparities across demographic groups. Existing approaches to fair learning largely fall into two directions: incorporating fairness constraints tailored to specific definitions, which limits their generalizability, or reducing the statistical dependence between predictions and sensitive attributes, which is more flexible but highly sensitive to the choice of distance measure. The latter strategy in particular raises the challenge of finding a principled and reliable measure of dependence that can perform consistently across tasks. In this work, we present a general and model-agnostic approach to address this challenge. The method is based on encouraging independence between predictions and sensitive features through an optimization framework that leverages the Cauchy–Schwarz (CS) Divergence as a principled measure of dependence. Prior studies suggest that CS Divergence provides a tighter theoretical bound compared to alternative distance measures used in earlier fairness methods, offering a stronger foundation for fairness-oriented optimization. Our framework, therefore, unifies prior efforts under a simple yet effective principle and highlights the value of carefully chosen statistical measures in fair learning. Through extensive empirical evaluation on four tabular datasets and one image dataset, we show that our approach consistently improves multiple fairness metrics while maintaining competitive accuracy.

**Abstract (Chinese)**

机器学习中的公平性已成为核心关注点，因为预测模型经常继承甚至放大训练数据中存在的偏差。此类偏差通常表现为模型输出与敏感属性之间的意外相关性，导致人口统计群体间的系统性差异。现有的公平学习方法主要分为两个方向：纳入针对特定定义量身定制的公平性约束，这限制了其泛化能力；或减少预测与敏感属性之间的统计依赖性，这种方法更灵活，但高度依赖于距离度量的选择。特别是后一种策略提出了寻找一种原则性和可靠的依赖性度量以在不同任务中一致表现的挑战。在本工作中，我们提出了一种通用且模型无关的方法来应对这一挑战。该方法基于通过一个优化框架鼓励预测与敏感特征之间的独立性，该框架利用柯西-施瓦茨（CS）散度作为原则性的依赖性度量。先前研究表明，与早期公平方法中使用的替代距离度量相比，CS散度提供了更紧的理论界，从而为面向公平性的优化提供了更坚实的基础。因此，我们的框架在一种简单而有效的原则下统一了先前的工作，并突出了在公平学习中精心选择的统计度量的价值。通过对四个表格数据集和一个图像数据集的广泛实证评估，我们展示了我们的方法在保持竞争性准确率的同时，一致提升了多种公平性指标。

---

### From Gradient Volume to Shapley Fairness: Towards Fair Multi-Task Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Xiao Wang, Yuying Han, Dazi Li, Fei Zhang, Min Tang
- **Keywords**: Multi-task Learning, Shapley Value, Fair Optimization
- **OpenReview**: https://openreview.net/forum?id=2PdLKGdtqW
- **PDF**: https://openreview.net/pdf?id=2PdLKGdtqW

**Abstract**

Multi-task learning often suffers from gradient conflicts, leading to unfair optimization and degraded overall performance. To address this, we present SVFair, a Shapley value-based framework for fair gradient aggregation. We propose two scalable geometric conflict metrics: VolDet, a gram determinant volume metric, and VolDetPro, its sign-aware extension distinguishing antagonistic gradients. By integrating these metrics into Shapley value computation, SVFair quantifies each task’s deviation from the overall gradient and rebalances updates toward fairness. In parallel, our Shapley value computation admits controllable complexity. Extensive experiments show that SVFair achieves state-of-the-art results across diverse supervised and reinforcement learning benchmarks, and further improves existing methods when integrated as a fairness-enhancing module.

**Abstract (Chinese)**

多任务学习常常遭受梯度冲突的影响，导致不公平优化和整体性能下降。为了解决这一问题，我们提出了SVFair，这是一个基于Shapley值的公平梯度聚合框架。我们提出了两种可扩展的几何冲突度量：VolDet，一种Gram行列式体积度量，以及VolDetPro，其符号感知扩展，能够区分对抗梯度。通过将这些度量集成到Shapley值计算中，SVFair量化了每个任务相对于整体梯度的偏差，并重新平衡更新以实现公平性。同时，我们的Shapley值计算具有可控复杂度。广泛的实验表明，SVFair在多样化的监督学习和强化学习基准上取得了最先进的结果，并且当作为公平性增强模块集成到现有方法中时，进一步提升了这些方法。

---

### GeoDiv: Framework for Measuring Geographical Diversity in Text-to-Image Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Abhipsa Basu, Mohana Singh, Shashank Agnihotri, Margret Keuper, Venkatesh Babu Radhakrishnan
- **Keywords**: geographical diversity
- **OpenReview**: https://openreview.net/forum?id=WliHWqTfAb
- **PDF**: https://openreview.net/pdf?id=WliHWqTfAb

**Abstract**

Text-to-image (T2I) models are rapidly gaining popularity, yet their outputs often lack geographical diversity, reinforce stereotypes, and misrepresent regions. Given their broad reach, it is critical to rigorously evaluate how these models portray the world. Existing diversity metrics either rely on curated datasets or focus on surface-level visual similarity, limiting interpretability. We introduce *GeoDiv*, a framework leveraging large language and vision-language models to assess geographical diversity along two complementary axes: the Socio-Economic Visual Index (SEVI), capturing economic and condition-related cues, and the Visual Diversity Index (VDI), measuring variation in primary entities and backgrounds. Applied to images generated by models such as Stable Diffusion and FLUX.1-dev across $10$ entities and $16$ countries, *GeoDiv* reveals a consistent lack of diversity and identifies fine-grained attributes where models default to biased portrayals. Strikingly, depictions of countries like India, Nigeria, and Colombia are disproportionately impoverished and worn, reflecting underlying socio-economic biases. These results highlight the need for greater geographical nuance in generative models. *GeoDiv* provides the first systematic, interpretable framework for measuring such biases, marking a step toward fairer and more inclusive generative systems. Project page: https://abhipsabasu.github.io/geodiv

**Abstract (Chinese)**

文本到图像 (T2I) 模型正迅速流行起来，然而它们的输出往往缺乏地理多样性、强化刻板印象，并对地区进行错误表述。鉴于其广泛的影响力，严格评估这些模型如何描绘世界至关重要。现有的多样性指标要么依赖于精选数据集，要么关注表层视觉相似性，从而限制了解释性。我们引入 *GeoDiv*，这是一个利用大语言模型和视觉-语言模型的框架，用于沿两个互补维度评估地理多样性：社会经济视觉指数 (SEVI)，捕捉经济和状况相关线索；以及视觉多样性指数 (VDI)，衡量主要实体和背景的变异。应用于诸如 Stable Diffusion 和 FLUX.1-dev 等模型生成的图像，涵盖 10 个实体和 16 个国家，*GeoDiv* 揭示了持续缺乏多样性，并识别出模型默认偏向描绘的细粒度属性。引人注目的是，对印度、尼日利亚和哥伦比亚等国家的描绘不成比例地贫困和破旧，反映了潜在的社会经济偏见。这些结果突显了生成模型中需要更大的地理细微差别。*GeoDiv* 提供了第一个系统化、可解释的框架来衡量此类偏见，标志着迈向更公平、更具包容性的生成系统的一步。项目页面：https://abhipsabasu.github.io/geodiv

---

### In Agents We Trust, but Who Do Agents Trust? Latent Preferences Steer LLM Generations

- **Venue**: ICLR 2026 Poster
- **Authors**: Mohammad Aflah Khan, Mahsa Amani, Soumi Das, Bishwamittra Ghosh, Qinyuan Wu, Krishna P. Gummadi, Manish Gupta, Abhilasha Ravichander
- **Keywords**: AI Agents, Source Preferences
- **OpenReview**: https://openreview.net/forum?id=yTUNl6jYGU
- **PDF**: https://openreview.net/pdf?id=yTUNl6jYGU

**Abstract**

Large Language Model (LLM) based agents are increasingly being deployed as user-friendly front-ends on online platforms, where they filter, prioritize, and recommend information retrieved from the platforms' back-end databases or via web search. In these scenarios, LLM agents act as decision assistants, drawing users' attention to particular instances of retrieved information at the expense of others. While much prior work has focused on biases in the information LLMs themselves generate, less attention has been paid to the factors and mechanisms that determine how LLMs select and present information to users.

We hypothesize that when information is attributed to specific sources (e.g., particular publishers, journals, or platforms), LLMs will exhibit systematic latent source preferences. That is, they will prioritize information from some sources over others based on attributes such as the sources' brand identity, reputation, or perceived expertise, encoded within their parametric knowledge. Through controlled experiments on twelve LLMs from six model providers, spanning both synthetic and real-world tasks including news recommendation, research paper selection, and choosing e-commerce platforms, we find that several models consistently exhibit strong and predictable source preferences. These preferences are sensitive to contextual framing, can outweigh the influence of content itself, and persist despite explicit prompting to avoid them. They also help explain phenomena such as the observed left-leaning skew in news recommendations, which arises from higher trust in certain sources rather than the content itself. Our findings advocate for deeper investigation into the origins of these preferences during pretraining, fine-tuning and instruction tuning, as well as for mechanisms that provide users with transparency and control over the biases guiding LLM-powered agents.

**Abstract (Chinese)**

基于大语言模型 (LLM) 的代理越来越多地被部署为在线平台上用户友好的前端，在这些平台上，它们过滤、优先排序并推荐从平台后端数据库或通过网络搜索检索到的信息。在这些场景中，LLM 代理充当决策助手，将用户的注意力吸引到检索信息中的特定实例上，而牺牲其他实例。虽然以往的大量工作关注于 LLM 自身生成的信息中的偏见，但对决定 LLM 如何向用户选择和呈现信息的因素和机制的关注较少。

我们假设，当信息归属于特定来源（例如，特定出版商、期刊或平台）时，LLM 将表现出系统的潜在来源偏好。也就是说，它们将基于来源的品牌身份、声誉或感知专业性等属性，这些属性编码在其参数知识中，从而优先考虑某些来源的信息而非其他来源。通过对来自六个模型提供商的十二个 LLM 的控制实验，涵盖合成任务和真实世界任务，包括新闻推荐、研究论文选择和电商平台选择，我们发现几个模型一致地表现出强烈且可预测的来源偏好。这些偏好对上下文框架敏感，可能超过内容本身的影响，并且尽管明确提示避免它们仍会持续存在。它们还有助于解释诸如新闻推荐中观察到的左倾偏差等现象，这种偏差源于对某些来源的更高信任，而不是内容本身。我们的发现主张对这些偏好的起源进行更深入的调查，包括在预训练、微调和指令调优期间，以及提供机制让用户对指导 LLM 驱动代理的偏见具有透明度和控制权。

---

### LLMS ON TRIAL: Evaluating Judicial Fairness For Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Yiran HU, Zongyue Xue, Haitao Li, Siyuan Zheng, Qingjing Chen, Shaochun Wang, Xihan Zhang, Ning Zheng, Yun Liu, Qingyao Ai, Yiqun LIU, Charles L. A. Clarke, Weixing Shen
- **Keywords**: Fairness, LLM-as-judge
- **OpenReview**: https://openreview.net/forum?id=C5Ihi4bVQt
- **PDF**: https://openreview.net/pdf?id=C5Ihi4bVQt

**Abstract**

Large Language Models (LLMs) are increasingly used in high-stakes fields, such as law, where their decisions can directly impact people's lives. When LLMs act as judges, the ability to fairly resolve judicial issues is necessary to ensure their trustworthiness. Based on theories of judicial fairness, we construct a comprehensive framework to measure LLM fairness, leading to a selection of 65 labels and 161 corresponding values. We further compile an extensive dataset, JudiFair, comprising 177,100 unique case facts. To achieve robust statistical inference, we develop three evaluation metrics—inconsistency, bias, and imbalanced inaccuracy—and introduce a method to assess the overall fairness of multiple LLMs across various labels. Through experiments with 16 LLMs, we uncover pervasive inconsistency, bias, and imbalanced inaccuracy across models, underscoring severe LLM judicial unfairness. 
Particularly, LLMs display notably more pronounced biases on demographic labels, with slightly less bias on substance labels compared to procedure ones. Interestingly, increased inconsistency correlates with reduced biases, but more accurate predictions exacerbate biases. While we find that adjusting the temperature parameter can influence LLM fairness, model size, release date, and country of origin do not exhibit significant effects on judicial fairness. Accordingly, we introduce a publicly available toolkit to support future research in evaluating and improving LLM fairness, along with a full technical analysis included as an appendix.

**Abstract (Chinese)**

大型语言模型（LLMs）越来越广泛地应用于高风险领域，如法律，这些领域中的决策可能直接影响人们的生活。当 LLMs 充当法官时，公平解决司法问题的能力对于确保其可信度至关重要。基于司法公平理论，我们构建了一个全面框架来衡量 LLM 的公平性，从而选定了 65 个标签和 161 个相应值。我们进一步编制了一个庞大的数据集 JudiFair，其中包含 177,100 个独特案例事实。为了实现稳健的统计推断，我们开发了三种评估指标——不一致性、偏见和失衡不准确性——并引入了一种方法来评估多个 LLMs 在各种标签上的整体公平性。通过对 16 个 LLMs 的实验，我们发现了模型中普遍存在的不一致性、偏见和失衡不准确性，这凸显了 LLM 司法不公平的严重性。

特别是，LLMs 在人口统计标签上表现出明显更严重的偏见，与程序标签相比，在实质标签上的偏见略少。有趣的是，不一致性的增加与偏见的减少相关，但更准确的预测会加剧偏见。虽然我们发现调整温度参数可以影响 LLM 的公平性，但模型规模、发布日期和原产国对司法公平性没有显著影响。因此，我们引入了一个公开可用的工具包，以支持未来评估和改进 LLM 公平性的研究，并附录中包含完整的的技术分析。

---

### Measuring and Mitigating Rapport Bias of Large Language Models under Multi-Agent Social Interactions

- **Venue**: ICLR 2026 Poster
- **Authors**: Maojia Song, Tej Deep Pala, Ruiwen Zhou, Weisheng Jin, Amir Zadeh, Chuan Li, Dorien Herremans, Soujanya Poria
- **Keywords**: Multi-Agent Systems (MAS), Social Influence & Trust Formation
- **OpenReview**: https://openreview.net/forum?id=gF31wuYdk7
- **PDF**: https://openreview.net/pdf?id=gF31wuYdk7

**Abstract**

Large language models (LLMs) are increasingly deployed in multi-agent systems (MAS) as components of collaborative intelligence, where peer interactions dynamically shape individual decision-making. While prior work has largely focused on conformity bias, we broaden the scope to examine how LLMs build rapport from previous interactions, resist misinformation, and integrate peer input during collaboration, which are key factors for achieving collective intelligence under complex social dynamics. We introduce KAIROS, a benchmark simulating quiz contests with peer agents of varying reliability, offering fine-grained control over conditions such as expert–novice roles, noisy crowds, and adversarial peers. LLMs receive both historical interactions and current peer responses, allowing systematic investigation into how rapport, peer action, and self-confidence influence decisions. To mitigate this vulnerability, we evaluate prompting, supervised fine-tuning, and reinforcement learning using Group Relative Policy Optimization (GRPO) across multiple models. Our results show that model size plays a central role in moderating susceptibility to social influence: larger models exhibit stronger resilience and benefit from prompting-based mitigation, whereas smaller models are more vulnerable. For the latter, carefully configured GRPO training improves both robustness and overall performance. Our code and datasets are available at: https://anonymous.4open.science/r/KAIROS-4F71

**Abstract (Chinese)**

大语言模型（LLMs）正日益被部署在多智能体系统（MAS）中，作为协作智能的组成部分，其中同伴互动动态塑造个体决策过程。虽然先前工作主要关注从众偏差，但我们拓宽研究范围，考察LLMs如何从先前互动中建立 rapport、抵抗虚假信息，并在协作过程中整合同伴输入，这些是复杂社会动态下实现集体智能的关键因素。我们引入KAIROS基准，该基准模拟具有不同可靠性同伴智能体的测验竞赛，提供对专家-新手角色、噪声人群和对抗性同伴等条件的细粒度控制。LLMs接收历史互动和当前同伴响应，从而系统考察rapport、同伴行动和自我信心如何影响决策。为缓解这一漏洞，我们在多个模型上评估提示工程、监督微调以及使用群组相对策略优化（GRPO）的强化学习。我们的结果表明，模型规模在调节对社会影响敏感性方面发挥核心作用：较大模型表现出更强的恢复力，并从基于提示的缓解方法中获益，而较小模型则更易受影响。对于后者，精心配置的GRPO训练可同时提升鲁棒性和整体性能。我们的代码和数据集可在以下地址获取：https://anonymous.4open.science/r/KAIROS-4F71

---

### Multi-Feature Quantized Self-Attention for Fair Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Jaeil Park, Sung-Bae Cho
- **Keywords**: Large language models, multi-attribute social bias, quantized adversarial autoencoder
- **OpenReview**: https://openreview.net/forum?id=0UvgQxsi7S
- **PDF**: https://openreview.net/pdf?id=0UvgQxsi7S

**Abstract**

Large language models (LLMs) often encode social biases tied to sensitive features such as race and gender, undermining fairness in downstream tasks even after instruction tuning. Conventional debiasing methods require expensive fine-tuning, are tied to specific architectures, or operate only at the input or decoding stage while neglecting attention-level representations, which can result in compromised task performance. Moreover, most approaches are tailored to single-attribute settings and do not explicitly address scenarios with multiple, overlapping protected attributes and their intersections. This paper proposes a novel method of multi-feature quantized attention regularization (MQAR) to mitigate multi-feature bias by injecting a structured quantization into frozen self-attention layers. MQAR disentangles attribute-specific activations through vector-quantized regularization and uses a discriminator-guided autoencoding regularizer to adversarially suppress protected-attribute information while preserving task-relevant semantics. Crucially, the proposed method operates without modifying the backbone parameters or accessing pre-training data, ensuring architecture-agnostic applicability and minimizing representation distortion. MQAR is evaluated on five diverse LLMs (BERT, T5, GPT-Neo, Mixtral, and LLaMA 3.2) using three standard bias benchmarks (WinoBias, StereoSet, and CrowS-Pairs). Across these models, MQAR consistently reduces bias for multiple protected attributes and their intersections while maintaining downstream accuracy within at most 0.4 \%, on average, of non-debiased baselines on sentiment analysis, abusive language detection, and text generation tasks. These findings highlight quantized attention regularization as a scalable and effective method for mitigating social bias in modern language models.

**Abstract (Chinese)**

大型语言模型（LLMs）常常编码与种族和性别等敏感特征相关的社会偏见，即使经过指令调优，也会破坏下游任务的公平性。传统去偏方法需要昂贵的微调、局限于特定架构，或仅在输入或解码阶段操作，而忽略注意力层级表示，这可能导致任务性能受损。此外，大多数方法针对单一属性设置，并未明确处理多个重叠受保护属性及其交集的场景。本文提出了一种新型的多特征量化注意力正则化（MQAR）方法，通过向冻结的自注意力层注入结构化量化来缓解多特征偏见。MQAR 通过向量量化正则化解耦特定属性的激活，并使用判别器引导的自编码正则化器对抗性地抑制受保护属性信息，同时保留任务相关语义。关键的是，所提出方法无需修改主干参数或访问预训练数据，确保架构无关的适用性并最小化表示扭曲。MQAR 在五个多样化的 LLMs（BERT、T5、GPT-Neo、Mixtral 和 LLaMA 3.2）上使用三个标准偏见基准（WinoBias、StereoSet 和 CrowS-Pairs）进行评估。在这些模型中，MQAR 一致减少多个受保护属性及其交集的偏见，同时在情感分析、滥用语言检测和文本生成任务下游准确率平均保持在非去偏基线最多 0.4% 以内。这些发现突显了量化注意力正则化作为缓解现代语言模型社会偏见的 scalable 和有效方法。

---

### On Fairness of Task Arithmetic: The Role of Task Vectors

- **Venue**: ICLR 2026 Poster
- **Authors**: Laura Gomezjurado Gonzalez, Hiroki Naganuma, Kotaro Yoshida, Takafumi Horie, Yuji Naraki, Ryotaro Shimizu
- **Keywords**: Fairness, Model Editing, Task Arithmetic
- **OpenReview**: https://openreview.net/forum?id=B19MBDrvlM
- **PDF**: https://openreview.net/pdf?id=B19MBDrvlM

**Abstract**

Model editing techniques, particularly task arithmetic with task vectors, offer an efficient alternative to full fine-tuning by enabling direct parameter updates through simple arithmetic operations. While this approach promises substantial computational savings, its impact on fairness has remained largely unexplored---despite growing concern over biased outcomes in high-stakes applications such as hate speech detection. In this work, we present the first systematic study of group fairness in task arithmetic within this binary text and image classification regime, comparing it against full fine-tuning (FFT) and Low-Rank Adaptation (LoRA). We evaluate across multiple language models and datasets using standard group fairness metrics, including Demographic Parity and Equalized Odds. Our analysis shows that task vectors can be tuned to achieve competitive accuracy while reducing disparities, and that merging subgroup-specific task vectors provides a practical mechanism for steering fairness outcomes. We further provide a theoretical bound linking task vector scaling to fairness metrics, offering insight into the observed trade-offs. Together, these findings establish task arithmetic not only as a cost-efficient editing method but also as a fairness-aware alternative to existing adaptation techniques, within the standard group-fair classification setting, laying the groundwork for responsible deployment of large language models.

**Abstract (Chinese)**

模型编辑技术，特别是使用任务向量进行任务算术，提供了一种高效的全量微调替代方案，通过简单的算术运算实现直接的参数更新。虽然这种方法承诺了大量的计算节省，但其对公平性的影响仍未得到充分探索——尽管在诸如仇恨言论检测等高风险应用中，对偏见结果的担忧日益增加。在这项工作中，我们首次系统研究了在二元文本和图像分类任务中任务算术的群体公平性，并将其与全量微调 (FFT) 和低秩适配 (LoRA) 进行比较。我们使用标准群体公平性指标，包括人口统计平价和等化几率，对多个语言模型和数据集进行评估。我们的分析表明，任务向量可以通过调优实现竞争性的准确率同时减少差异，并且合并子群体特定的任务向量提供了一种实际机制来引导公平性结果。我们进一步提供了将任务向量缩放与公平性指标联系起来的理论界限，为观察到的权衡提供了洞见。这些发现共同确立了任务算术不仅作为一种成本高效的编辑方法，而且作为现有适配技术的公平性感知替代方案，在标准群体公平分类设置中，为大型语言模型的责任部署奠定了基础。

---

### Person-Centric Annotations of LAION-400M: Auditing Bias and Its Transfer to Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Leander Girrbach, Stephan Alaniz, Genevieve Smith, Trevor Darrell, Zeynep Akata
- **Keywords**: dataset bias, model bias, laion-400m
- **OpenReview**: https://openreview.net/forum?id=t3ZMiHhqXm
- **PDF**: https://openreview.net/pdf?id=t3ZMiHhqXm

**Abstract**

Vision-language models trained on large-scale multimodal datasets show strong demographic biases, but the role of training data in producing these biases remains unclear. A major barrier has been the lack of demographic annotations in web-scale datasets such as LAION-400M. We address this gap by creating person-centric annotations for the full dataset, including over 276 million bounding boxes, perceived gender and race/ethnicity labels, and automatically generated captions. These annotations are produced through validated automatic labeling pipelines combining object detection, multimodal captioning, and finetuned classifiers. Using them, we uncover demographic imbalances and harmful associations, such as the disproportionate linking of men and individuals perceived as Black or Middle Eastern with crime-related and negative content. We also show that 60-70\% of gender bias in CLIP and Stable Diffusion can be linearly explained by direct co-occurrences in the data. Our resources establish the first large-scale empirical link between dataset composition and downstream model bias.

**Abstract (Chinese)**

在大型多模态数据集上训练的视觉-语言模型表现出强烈的 demographic biases，但训练数据在产生这些偏差中的作用仍不清楚。主要障碍是网络规模数据集（如 LAION-400M）缺乏 demographic annotations。我们通过为整个数据集创建以人为中心的标注来填补这一空白，包括超过 2.76 亿个边界框、感知性别和种族/民族标签，以及自动生成的图像描述。这些标注通过经过验证的自动标注管道生成，该管道结合了目标检测、多模态图像描述生成和微调分类器。利用这些标注，我们揭示了人口统计不平衡和有害关联，例如将男性以及被感知为黑人或中东人的个体不成比例地与犯罪相关和负面内容关联。我们还表明，CLIP 和 Stable Diffusion 中 60-70% 的性别偏差可以通过数据中直接共现线性解释。我们提供的资源建立了数据集组成与下游模型偏差之间第一个大规模实证联系。

---

### PoliCon: Evaluating LLMs on Achieving Diverse Political Consensus Objectives

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhaowei Zhang, Xiaobo Wang, Minghua Yi, Mengmeng Wang, Fengshuo Bai, Zilong Zheng, Yipeng Kang, Yaodong Yang
- **Keywords**: Generative Consensus Finding, Collective Decision Making, AI for Societal Efficiency
- **OpenReview**: https://openreview.net/forum?id=MHlwNs9k1Y
- **PDF**: https://openreview.net/pdf?id=MHlwNs9k1Y

**Abstract**

Achieving political consensus is crucial yet challenging for the effective functioning of social governance. However, although frontier AI systems represented by large language models (LLMs) have developed rapidly in recent years, their capabilities in this scope are still understudied. In this paper, we introduce PoliCon, a novel benchmark constructed from 2,225 high-quality deliberation records of the European Parliament over 13 years, ranging from 2009 to 2022, to evaluate the ability of LLMs to draft consensus resolutions based on divergent party positions under varying collective decision-making contexts and political requirements. Specifically, PoliCon incorporates four factors to build each task environment for finding different political consensus: specific political issues, political goals, participating parties, and power structures based on seat distribution. We also developed an evaluation framework based on social choice theory for PoliCon, which simulates the real voting outcomes of different political parties to assess whether LLM-generated resolutions meet the requirements of the predetermined political consensus. Our experimental results demonstrate that even state-of-the-art models remain undersatisfied with complex tasks like passing resolutions by a two-thirds majority and addressing security issues, while uncovering their inherent partisan biases and revealing some behaviors LLMs show to achieve the consensus, such as prioritizing the stance of the dominant party instead of uniting smaller parties, which highlights PoliCon's promise as an effective platform for studying LLMs' ability to promote political consensus. The code and dataset are released at [PoliCon Website](https://zowiezhang.github.io/projects/PoliCon).

**Abstract (Chinese)**

实现政治共识对于社会治理的有效运作至关重要却极具挑战性。然而，尽管以大语言模型 (LLMs) 为代表的前沿 AI 系统近年来快速发展，但它们在这一领域的能力仍未得到充分研究。本文介绍了 PoliCon，这是一个新型基准数据集，由 2009 年至 2022 年 13 年间欧洲议会 2,225 条高质量审议记录构建而成，用于评估 LLMs 在不同集体决策情境和政治要求下，根据分歧的政党立场起草共识决议的能力。具体而言，PoliCon 纳入四个因素来构建每个任务环境，以寻找不同的政治共识：具体政治议题、政治目标、参与政党以及基于席位分配的权力结构。我们还为 PoliCon 开发了一个基于社会选择理论的评估框架，该框架模拟不同政党的真实投票结果，以评估 LLM 生成的决议是否满足预定政治共识的要求。我们的实验结果表明，即使是最先进的模型在复杂任务（如以三分之二多数通过决议和处理安全议题）上仍表现不尽如人意，同时揭示了它们固有的党派偏见，并暴露了 LLMs 为实现共识而展现的一些行为，例如优先考虑主导政党的立场而非团结小党，这突显了 PoliCon 作为研究 LLMs 促进政治共识能力有效平台的潜力。代码和数据集已在 [PoliCon 网站](https://zowiezhang.github.io/projects/PoliCon) 发布。

---

### Regulating Internal Alignment Flows for Robust Learning Under Spurious Correlations

- **Venue**: ICLR 2026 Poster
- **Authors**: Rajeev Ranjan Dwivedi, Mohammedkaif Mohammedrafiq Kalagond, Niramay M.Patel, Vinod K. Kurmi
- **Keywords**: Fairness, Regularization, Bias Free
- **OpenReview**: https://openreview.net/forum?id=L2L1hi0FGj
- **PDF**: https://openreview.net/pdf?id=L2L1hi0FGj

**Abstract**

Deep models often exploit spurious correlations (e.g., backgrounds or dataset artifacts), hurting worst-group performance. We propose \textbf{Alignment-Gated Suppression (AGS)}, a lightweight, plug-in regularizer that intervenes inside the network during training. AGS tracks a class-conditional, confidence-weighted contribution for each neuron (more negative $\Leftrightarrow$ stronger support) and applies a percentile-based, multiplicative decay to the most extreme contributors, reducing overconfident shortcut pathways while leaving other features relatively more influential. AGS integrates with standard ERM, requires no group labels, and adds $<5\%$ training overhead. We provide analysis linking AGS to minority-margin gains, path-norm-like capacity control, and stability benefits via EMA-smoothed gating. Empirically, AGS improves worst-group accuracy and calibration vs.\ ERM and is competitive with state-of-the-art methods across spurious-correlation benchmarks (e.g., Waterbirds, CelebA, BAR, COCO), while maintaining strong average accuracy. These results suggest that regulating internal alignment flow is a simple and scalable route to robustness without group labels.

**Abstract (Chinese)**

深度模型常常利用虚假相关性（例如，背景或数据集伪影），从而损害最差群体性能。我们提出\textbf{对齐门控抑制 (AGS)}，一种轻量级的、即插即用正则化器，在训练过程中干预网络内部。AGS 为每个神经元跟踪类别条件、置信度加权的贡献（更负 $\Leftrightarrow$ 更强支持），并对最极端的贡献者施加基于百分位数的乘性衰减，从而减少过度自信的捷径路径，同时使其他特征相对更具影响力。AGS 与标准 ERM 集成，无需群体标签，并增加 $<5\%$ 的训练开销。我们提供了将 AGS 与少数群体边际增益、类似于路径范数的容量控制以及通过 EMA 平滑门控的稳定性益处联系起来的分析。在经验上，AGS 相对于 ERM 改善了最差群体准确率和校准，并在虚假相关性基准（例如，Waterbirds、CelebA、BAR、COCO）上与最先进方法竞争，同时保持强大的平均准确率。这些结果表明，调节内部对齐流是一种无需群体标签的简单且可扩展的鲁棒性途径。

---

### Rethinking Pareto Frontier: On the Optimal Trade-offs in Fair Classification

- **Venue**: ICLR 2026 Poster
- **Authors**: Junyi Chai, Shenyu Lu, Xiaoqian Wang
- **Keywords**: fairness-accuracy tradeoff
- **OpenReview**: https://openreview.net/forum?id=L8pyycR4wW
- **PDF**: https://openreview.net/pdf?id=L8pyycR4wW

**Abstract**

Fairness has become an arising concern in machine learning with its prevalence in decision-making processes, and the trade-offs between various fairness notions and between fairness and accuracy has been empirically observed. However, the inheritance of such trade-offs, as well as the quantification of the best achievable trade-offs, i.e., the Pareto optimal trade-offs, under varied constraints on fairness notions has been rarely and improperly discussed. Owing to the sub-optimality of fairness interventions, existing work fails to provide informative characterization regarding these trade-offs. In light of existing limitations, in this work, we propose a reformulation of the model-specific (MS) Pareto optimal trade-off, where we frame it as convex optimization problems involving fairness notions and accuracy w.r.t. the confusion vector. Our formulation provides an efficient approximation of the best achievable accuracy under dynamic fairness constraints, and yields systematical analysis regarding the fairness-accuracy trade-off. Going beyond the discussion on fairness-accuracy trade-offs, we extend the discussion to the trade-off between fairness notions, which characterizes the impact of accuracy on the compatibility between fairness notions. Inspired by our reformulation, we propose a last-layer retraining framework with group-dependent bias, and we prove theoretically the superiority of our method over existing baselines. Experimental results demonstrate the effectiveness of our method in achieving better fairness-accuracy trade-off, and that our MS Pareto frontiers sufficiently quantify the two trade-offs.

**Abstract (Chinese)**

公平性已成为机器学习中日益关注的问题，因为其在决策过程中的普遍应用，且各种公平性概念之间以及公平性与准确性之间的权衡已被经验观察到。然而，这些权衡的继承性，以及在不同公平性约束下最佳可实现权衡（即Pareto最优权衡）的量化，很少且不当地被讨论。由于公平干预的次优性，现有的工作未能提供关于这些权衡的信息性表征。鉴于现有局限性，本文提出模型特定（MS）Pareto最优权衡的重构，将其表述为涉及公平性概念和相对于混淆向量的准确性的凸优化问题。我们的表述提供了在动态公平约束下最佳可实现准确性的高效近似，并产生了关于公平-准确性权衡的系统分析。超越公平-准确性权衡的讨论，我们将讨论扩展到公平性概念之间的权衡，这表征了准确性对公平性概念之间兼容性的影响。受我们的重构启发，我们提出了一种具有组依赖偏差的最后一层重训练框架，并理论证明了我们的方法相对于现有基线的优越性。实验结果证明了我们的方法在实现更好公平-准确性权衡方面的有效性，并且我们的MS Pareto前沿充分量化了这两个权衡。

---

### Statistical Guarantees in the Search for Less Discriminatory Algorithms

- **Venue**: ICLR 2026 Poster
- **Authors**: Chris Hays, Benjamin Laufer, Solon Barocas, Manish Raghavan
- **Keywords**: fairness, anytime-valid inference, sequential decision-making
- **OpenReview**: https://openreview.net/forum?id=n8FKO0DIl8
- **PDF**: https://openreview.net/pdf?id=n8FKO0DIl8

**Abstract**

U.S. discrimination law can impose liability on firms that fail to adopt a less discriminatory alternative (LDA), defined as a decision policy that achieves the same business objectives while reducing disparate impact on legally protected groups. Recent scholarship argues that this doctrine has direct implications for algorithmic decision-making in high-stakes domains such as employment, lending, and housing, potentially obligating firms to search for “less discriminatory algorithms” (Black et al., 2024). Regulators have
at times encouraged proactive LDA searches, reinforcing the expectation of a good-faith effort to identify equally performant models with lower disparate impact. Model multiplicity makes such searches plausible: retraining with different random seeds can yield models with comparable predictive performance but materially different disparate impacts. Yet firms cannot retrain indefinitely, raising a central question: when is the search sufficient to demonstrate good faith? We formalize LDA search under multiplicity
as an optimal stopping problem in which a developer seeks to produce evidence that further search is unlikely to yield meaningful improvements. Our main contribution is an adaptive stopping algorithm that provides a high-probability upper bound on the best disparate-impact gains attainable through continued retraining, enabling developers to certify (e.g., to a court) that additional search is unlikely to help. We also show how stronger distributional assumptions over the model space can yield tighter bounds,
and we validate the approach on real-world credit and housing datasets.

**Abstract (Chinese)**

美国反歧视法可能对未能采用较少歧视性替代方案（LDA）的企业施加责任，其中LDA定义为一种实现相同商业目标同时减少对受法律保护群体差异性影响的决策政策。最近的学术研究认为，该原则对就业、贷款和住房等高风险领域中的算法决策具有直接影响，可能要求企业搜索“较少歧视性算法”（Black et al., 2024）。监管机构有时鼓励主动进行LDA搜索，从而强化了识别性能相当但差异性影响较低模型的善意努力预期。模型多样性使此类搜索变得可行：使用不同的随机种子重新训练可以产生预测性能相当但差异性影响显著不同的模型。然而，企业无法无限期重新训练，这引发了一个核心问题：何时搜索才足以证明善意？我们将多样性下的LDA搜索形式化为一个最优停止问题，其中开发者寻求产生证据，证明进一步搜索不太可能产生有意义的改进。我们主要的贡献是一个自适应停止算法，该算法提供了一个高概率上界，界定通过继续重新训练所能获得的最佳差异性影响改进，从而使开发者能够证明（例如，向法院）额外搜索不太可能有帮助。我们还展示了模型空间上更强的分布假设如何产生更紧的上界，并在真实世界的信贷和住房数据集上验证了该方法。

---

### WRING Out The Bias: A Rotation-Based Alternative To Projection Debiasing

- **Venue**: ICLR 2026 Poster
- **Authors**: Walter Gerych, Cassandra Parent, Quinn Perian, Rafiya Javed, Justin Solomon, Marzyeh Ghassemi
- **Keywords**: Vision Language Models, VLMs, bias, debias
- **OpenReview**: https://openreview.net/forum?id=tkE29O0jzF
- **PDF**: https://openreview.net/pdf?id=tkE29O0jzF

**Abstract**

Vision-Language models (VLMs), including CLIP, are known to encode biases such as learning spurious correlations that falsely associate background attributes with particular labels. Debiasing approaches typically aim to isolate and remove subspaces corresponding to a target concept via projecting its embedding away from the concept. This strategy succeeds in debiasing VLM embeddings with respect to the concepts considered but can amplify biased shortcuts in unconsidered concepts. In practice, it is impossible to enumerate all possible biases, meaning that an increase in bias can go unobserved during evaluation. We propose a debiasing approach for a set of known concepts such that the relation to the remaining, unconsidered, concepts is minimally changed. We achieve this by rotating the VLM’s embeddings within only a relevant subspace, rather than removing these subspaces, which mitigates unintended bias amplification.

**Abstract (Chinese)**

视觉-语言模型（VLMs），包括CLIP，已知会编码偏置，例如学习虚假相关性，这些相关性错误地将背景属性与特定标签关联起来。去偏方法通常旨在通过将嵌入投影远离该概念来隔离并移除对应于目标概念的子空间。这种策略在针对所考虑概念去偏VLM嵌入方面取得了成功，但可能放大未考虑概念中的偏置捷径。在实践中，不可能枚举所有可能的偏置，这意味着偏置的增加可能在评估中未被观察到。我们提出了一种针对一组已知概念的去偏方法，使得与剩余未考虑概念的关系最小化变化。我们通过仅在相关子空间内旋转VLM的嵌入来实现这一点，而不是移除这些子空间，从而缓解了意外偏置放大。

---

### When Machine Learning Gets Personal: Evaluating Prediction and Explanation

- **Venue**: ICLR 2026 Poster
- **Authors**: Louisa Cornelis, Guillermo Bernardez, Haewon Jeong, Nina Miolane
- **Keywords**: Fairness, explainability, personalization
- **OpenReview**: https://openreview.net/forum?id=fnfG8pI00B
- **PDF**: https://openreview.net/pdf?id=fnfG8pI00B

**Abstract**

In high-stakes domains like healthcare, users often expect that sharing personal information with machine learning systems will yield tangible benefits, such as more accurate diagnoses and clearer explanations of contributing factors. However, the validity of this assumption remains largely unexplored. We propose a unified framework to quantify how personalizing a model influences both prediction and explanation. We show that its impacts on prediction and explanation can diverge: a model may become more or less explainable even when prediction is unchanged. For practical settings, we study a standard hypothesis test for detecting personalization effects on demographic groups. We derive a finite-sample lower bound on its probability of error as a function of group sizes, number of personal attributes, and desired benefit from personalization. This provides actionable insights, such as which dataset characteristics are necessary to test an effect, or the maximum effect that can be tested given a dataset. We apply our framework to real-world tabular datasets using feature-attribution methods, uncovering scenarios where effects are fundamentally untestable due to the dataset statistics. Our results highlight the need for joint evaluation of prediction and explanation in personalized models and the importance of designing models and datasets with sufficient information for such evaluation.

**Abstract (Chinese)**

在高风险领域如医疗保健中，用户往往期望与机器学习系统共享个人信息将带来切实益处，例如更准确的诊断以及对贡献因素更清晰的解释。然而，这一假设的有效性尚未得到充分探讨。我们提出一个统一框架，用于量化模型个性化如何影响预测和解释。我们证明，其对预测和解释的影响可能出现分歧：即使预测性能不变，模型的可解释性也可能增强或减弱。在实际场景中，我们研究了一种标准假设检验，用于检测个性化对人口统计群体的影响。我们推导了其有限样本错误概率的下界，该下界是群体大小、个人属性数量以及个性化预期益处的函数。这提供了可操作的洞见，例如检验效应所需的数据集特征，或给定数据集可检验的最大效应。我们将该框架应用于真实世界的表格数据集，并采用特征归因方法，发现由于数据集统计特性而导致效应本质上无法检验的情形。我们的结果强调了个性化模型中对预测和解释进行联合评估的必要性，以及设计模型和数据集以提供充分评估信息的重要性。

---
