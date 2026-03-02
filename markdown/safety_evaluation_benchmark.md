# safety_evaluation_benchmark

**Description**: 安全评测、基准与测量方法。包括 safety benchmarks、jailbreak eval、toxicity/harmful capability evaluation、模型行为测量、红队评测协议、评测偏差与可重复性等。

**Paper count**: 26

---

### AdAEM: An Adaptively and Automated Extensible Evaluation Method of LLMs' Value Difference

- **Venue**: ICLR 2026 Oral
- **Authors**: Jing Yao, Shitong Duan, Xiaoyuan Yi, Dongkuan Xu, Peng Zhang, Tun Lu, Ning Gu, Zhicheng Dou, Xing Xie
- **Keywords**: LLM Evaluation, Value Evaluation, Value Alignment, Dynamic Evaluation
- **OpenReview**: https://openreview.net/forum?id=qNlTH4kYJZ
- **PDF**: https://openreview.net/pdf?id=qNlTH4kYJZ

**Abstract**

Assessing Large Language Models (LLMs)' underlying value differences enables comprehensive comparison of their misalignment, cultural adaptability, and biases. Nevertheless, current value measurement methods face the informativeness challenge: with often outdated, contaminated, or generic test questions, they can only capture the orientations on comment safety values, e.g., HHH, shared among different LLMs, leading to indistinguishable and uninformative results. To address this problem, we introduce AdAEM, a novel, self-extensible evaluation algorithm for revealing LLMs' inclinations. Distinct from static benchmarks, AdAEM automatically and adaptively generates and extends its test questions. This is achieved by probing the internal value boundaries of a diverse set of LLMs developed across cultures and time periods in an in-context optimization manner. Such a process theoretically maximizes an information-theoretic objective to extract diverse controversial topics that can provide more distinguishable and informative insights about models' value differences. In this way, AdAEM is able to co-evolve with the development of LLMs, consistently tracking their value dynamics. We use AdAEM to generate novel questions and conduct an extensive analysis, demonstrating our method's validity and effectiveness, laying the groundwork for better interdisciplinary research on LLMs' values and alignment.

**Abstract (Chinese)**

评估大型语言模型 (LLMs) 的潜在价值差异，能够全面比较它们的不一致性、文化适应性和偏见。然而，现有的价值测量方法面临信息性挑战：由于测试问题往往过时、受污染或过于通用，它们只能捕捉不同 LLMs 共享的常见安全价值观（如 HHH）的倾向，导致结果无法区分且缺乏信息性。为解决这一问题，我们引入 AdAEM，一种新型的、自我可扩展的评估算法，用于揭示 LLMs 的倾向。与静态基准不同，AdAEM 能够自动且自适应地生成并扩展其测试问题。这一过程通过以上下文优化方式探查跨文化和时间段开发的多样化 LLMs 集合的内部价值边界来实现。该过程在理论上最大化信息论目标，以提取多样化的争议话题，从而提供关于模型价值差异的更具区分性和信息性的洞见。通过这种方式，AdAEM 能够与 LLMs 的发展共同演化，持续跟踪其价值动态。我们使用 AdAEM 生成新颖的问题并进行广泛分析，证明了该方法的有效性和效能，为 LLMs 价值与对齐的更好跨学科研究奠定了基础。

---

### EigenBench: A Comparative Behavioral Measure of Value Alignment

- **Venue**: ICLR 2026 Oral
- **Authors**: Jonathn Chang, Leonhard Piff, Suvadip Sana, Jasmine Xinze Li, Lionel Levine
- **Keywords**: value alignment, Bradley-Terry model, EigenTrust, model disposition, constitutional AI
- **OpenReview**: https://openreview.net/forum?id=fm79KXJIUQ
- **PDF**: https://openreview.net/pdf?id=fm79KXJIUQ

**Abstract**

Aligning AI with human values is a pressing unsolved problem. To address the lack of quantitative metrics for value alignment, we propose EigenBench: a black-box method for comparatively benchmarking language models’ values. Given an ensemble of models, a constitution describing a value system, and a dataset of scenarios, our method returns a vector of scores quantifying each model’s alignment to the given constitution. To produce these scores, each model judges the outputs of other models across many scenarios, and these judgments are aggregated with EigenTrust (Kamvar et al., 2003), yielding scores that reflect a weighted consensus judgment of the whole ensemble. EigenBench uses no ground truth labels, as it is designed to quantify subjective traits for which reasonable judges may disagree on the correct label. Hence, to validate our method, we collect human judgments on the same ensemble of models and show that EigenBench’s judgments align closely with those of human evaluators. We further demonstrate that EigenBench can recover model rankings on the GPQA benchmark without access to objective labels, supporting its viability as a framework for evaluating subjective values for which no ground truths exist. The code is available at https://github.com/jchang153/EigenBench.

**Abstract (Chinese)**

将AI与人类价值观对齐是一个紧迫的未解决问题。为了解决价值对齐缺乏定量指标的问题，我们提出EigenBench：一种用于比较基准测试语言模型价值观的黑盒方法。给定一组模型、描述价值系统的宪法以及场景数据集，我们的方法返回一个分数向量，量化每个模型与给定宪法的对齐度。为了生成这些分数，每个模型在许多场景中判断其他模型的输出，这些判断使用EigenTrust (Kamvar et al., 2003)进行聚合，产生反映整个集合加权共识判断的分数。EigenBench不使用真实标签，因为它旨在量化合理判断者可能对正确标签意见不一致的主观特质。因此，为了验证我们的方法，我们收集了相同模型集合的人类判断，并显示EigenBench的判断与人类评估者的判断高度一致。我们进一步证明，EigenBench可以在不访问客观标签的情况下恢复GPQA基准上的模型排名，支持其作为评估不存在真实标签的主观价值观框架的可行性。代码可在https://github.com/jchang153/EigenBench获取。

---

### A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments

- **Venue**: ICLR 2026 Poster
- **Authors**: Manuel Cherep, Chengtian Ma, Abigail Xu, Maya Shaked, Patricia Maes, Nikhil Singh
- **Keywords**: LLM, Agents, Agentic AI, Behavior, Choices, Alignment, Safety, Benchmark
- **OpenReview**: https://openreview.net/forum?id=xAPoscV2Bw
- **PDF**: https://openreview.net/pdf?id=xAPoscV2Bw

**Abstract**

Environments built for people are increasingly operated by a new class of economic actors: LLM-powered software agents making decisions on our behalf. These decisions range from our purchases to travel plans to medical treatment selection. Current evaluations of these agents largely focus on task competence, but we argue for a deeper assessment: how these agents choose when faced with realistic decisions. We introduce ABxLab, a framework for systematically probing agentic choice through controlled manipulations of option attributes and persuasive cues. We apply this to a realistic web-based shopping environment, where we vary prices, ratings, and psychological nudges, all of which are factors long known to shape human choice. We find that agent decisions shift predictably and substantially in response, revealing that agents are strongly biased choosers even without being subject to the cognitive constraints that shape human biases. This susceptibility reveals both risk and opportunity: risk, because agentic consumers may inherit and amplify human biases; opportunity, because consumer choice provides a powerful testbed for a behavioral science of AI agents, just as it has for the study of human behavior. We release our framework as an open benchmark for rigorous, scalable evaluation of agent decision-making.

**Abstract (Chinese)**

为人类构建的环境越来越多地由一类新型经济行为主体运营：大语言模型驱动的软件代理代表我们做出决策。这些决策范围从我们的购物到旅行计划再到医疗治疗选择。目前对这些代理的评估主要关注任务胜任力，但我们主张进行更深入的评估：这些代理在面对现实决策时如何选择。我们引入ABxLab，这是一个框架，通过对选项属性和说服性提示的控制性操纵来系统地探究代理式选择。我们将其应用于一个现实的基于网络的购物环境，在其中我们变化价格、评分和心理助推，这些都是长期以来已知塑造人类选择的因素。我们发现，代理决策以可预测且显著的方式发生变化，这揭示了即使不受塑造人类偏见的认知约束的影响，代理也是强烈有偏见的决策者。这种易感性揭示了风险与机会：风险，因为代理式消费者可能继承并放大人类偏见；机会，因为消费者选择为AI代理的行为科学提供了强大的测试平台，正如它为人类行为研究所做的那样。我们将我们的框架作为开放基准发布，用于代理决策的严谨、可扩展评估。

---

### Benchmarking Overton Pluralism in LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Elinor Poole-Dayan, Jiayi Wu, Taylor Sorensen, Jiaxin Pei, Michiel A. Bakker
- **Keywords**: Pluralism, Overton pluralism, pluralistic alignment, benchmark
- **OpenReview**: https://openreview.net/forum?id=f2VxF4QIx1
- **PDF**: https://openreview.net/pdf?id=f2VxF4QIx1

**Abstract**

We introduce OVERTONBENCH, a novel framework for measuring Overton pluralism in LLMs—the extent to which diverse viewpoints are represented in model outputs. We (i) formalize Overton pluralism as a set coverage metric (OVERTONSCORE), (ii) conduct a large-scale U.S.-representative human study (N = 1208; 60 questions; 8 LLMs), and (iii) develop an automated benchmark that closely reproduces human judgments. On average, models achieve OVERTONSCOREs of 0.35–0.41, with DeepSeek V3 performing best; yet all models remain far below the theoretical maximum of 1.0, revealing substantial headroom for improvement. Because repeated large-scale human studies are costly and slow, scalable evaluation tools are essential for model development. Hence, we propose an automated benchmark that achieves high rank correlation with human judgments ($\rho = 0.88$), providing a practical proxy without replacing human assessment. By turning pluralistic alignment from a normative aim into a measurable benchmark, our work establishes a foundation for systematic progress toward more pluralistic LLMs.

**Abstract (Chinese)**

我们介绍了 OVERTONBENCH，这是一个用于衡量大语言模型 (LLMs) 中 Overton 多元主义的新型框架——即模型输出中多样观点代表程度的程度。我们 (i) 将 Overton 多元主义形式化为一个集合覆盖度量 (OVERTONSCORE)，(ii) 开展了一项大规模的美国代表性人类研究 (N = 1208；60 个问题；8 个 LLMs)，以及 (iii) 开发了一个紧密再现人类判断的自动化基准。平均而言，模型的 OVERTONSCORE 为 0.35–0.41，其中 DeepSeek V3 表现最佳；然而，所有模型仍远低于理论最大值 1.0，显示出巨大的改进空间。由于重复进行大规模人类研究成本高昂且耗时，可扩展的评估工具对于模型开发至关重要。因此，我们提出一个自动化基准，该基准与人类判断实现了高的秩相关 (ρ = 0.88)，提供了一个实用的代理，而不取代人类评估。通过将多元主义对齐从规范性目标转变为可衡量的基准，我们的工作为系统性地推进更具多元主义的大语言模型奠定了基础。

---

### Breaking Agent Backbones: Evaluating the Security of Backbone LLMs in AI Agents

- **Venue**: ICLR 2026 Poster
- **Authors**: Julia Bazinska, Max Mathys, Francesco Casucci, Mateo Rojas-Carulla, Xander Davies, Alexandra Souly, Niklas Pfister
- **Keywords**: AI security, Large Language Models, Security Benchmark, Red Teaming, AI Safety
- **OpenReview**: https://openreview.net/forum?id=kga18ld70t
- **PDF**: https://openreview.net/pdf?id=kga18ld70t

**Abstract**

AI agents powered by large language models (LLMs) are being deployed at scale, yet we lack a systematic understanding of how the choice of backbone LLM affects agent security.
The non-deterministic sequential nature of AI agents complicates security modeling, while the integration of traditional software with AI components entangles novel LLM vulnerabilities with conventional security risks.
Existing frameworks only partially address these challenges as they either capture specific vulnerabilities only or require modeling of complete agents.
To address these limitations, we introduce threat snapshots: a framework that isolates specific states in an agent's execution flow where LLM vulnerabilities manifest, enabling the systematic identification and categorization of security risks that propagate from the LLM to the agent level.
We apply this framework to construct the $b^3$ benchmark, a security benchmark based on 194,331 unique crowdsourced adversarial attacks. We then evaluate 34 popular LLMs with it, revealing, among other insights, that enhanced reasoning capabilities improve security, while model size does not correlate with security.
We release our benchmark, dataset, and evaluation code to facilitate widespread adoption by LLM providers and practitioners, offering guidance for agent developers and incentivizing model developers to prioritize backbone security improvements.

**Abstract (Chinese)**

由大语言模型（LLMs）驱动的 AI 代理正在大规模部署，然而，我们缺乏对骨干 LLM 选择如何影响代理安全的系统性理解。

AI 代理的非确定性顺序特性使安全建模复杂化，同时传统软件与 AI 组件的集成将新型 LLM 漏洞与传统安全风险交织在一起。

现有框架仅部分解决这些挑战，因为它们要么仅捕获特定漏洞，要么需要对完整代理进行建模。

为解决这些局限性，我们引入威胁快照：一种框架，它隔离代理执行流程中 LLM 漏洞显现的特定状态，从而实现从 LLM 到代理层级安全风险的系统性识别和分类，这些风险从 LLM 传播而来。

我们应用此框架构建 $b^3$ 基准，这是一个基于 194,331 个独特众包对抗攻击的安全基准。然后，我们用它评估了 34 个流行 LLMs，揭示出（除其他洞见外），增强的推理能力改善了安全性，而模型规模与安全性无关。

我们发布我们的基准、数据集和评估代码，以促进 LLM 提供者和从业者的广泛采用，为代理开发者提供指导，并激励模型开发者优先改进骨干安全性。

---

### CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives

- **Venue**: ICLR 2026 Poster
- **Authors**: Ayoung Lee, Ryan Sungmo Kwon, Peter Railton, Lu Wang
- **Keywords**: dilemma, value-based decision-making, high-stakes, steerability, LLM
- **OpenReview**: https://openreview.net/forum?id=WdpslG6ro5
- **PDF**: https://openreview.net/pdf?id=WdpslG6ro5

**Abstract**

Navigating dilemmas involving conflicting values is challenging even for humans in high-stakes domains, let alone for AI, yet prior work has been limited to everyday scenarios. To close this gap, we introduce CLASH (Character perspective-based LLM Assessments in Situations with High-stakes), a meticulously curated dataset consisting of 345 high-impact dilemmas along with 3,795 individual perspectives of diverse values. CLASH enables the study of critical yet underexplored aspects of value-based decision-making processes, including understanding of decision ambivalence and psychological discomfort as well as capturing the temporal shifts of values in the perspectives of characters. By benchmarking 14 non-thinking and thinking models, we uncover several key findings. (1) Even strong proprietary models, such as GPT-5 and Claude-4-Sonnet, struggle with ambivalent decisions, achieving only 24.06 and 51.01 accuracy. (2) Although LLMs reasonably predict psychological discomfort, they do not adequately comprehend perspectives involving value shifts. (3) Cognitive behaviors that are effective in the math-solving and game strategy domains do not transfer to value reasoning. Instead, new failure patterns emerge, including early commitment and overcommitment. (4) The steerability of LLMs towards a given value is significantly correlated with their value preferences. (5) Finally, LLMs exhibit greater steerability when reasoning from a third-party perspective, although certain values (e.g., safety) benefit uniquely from first-person framing.

**Abstract (Chinese)**

在高风险领域中，即使人类也难以应对涉及冲突价值观的困境，更不用说人工智能了，而以往研究仅限于日常场景。为填补这一空白，我们引入CLASH（基于角色视角的高风险情境下大语言模型评估数据集，Character perspective-based LLM Assessments in Situations with High-stakes），这是一个精心构建的数据集，包含345个高影响困境以及3,795个体现多样价值观的个体视角。CLASH支持对基于价值观决策过程的关键却鲜有探索的方面进行研究，包括决策矛盾性与心理不适的理解，以及捕捉角色视角中价值观的时间性转变。通过对14个非思考型和思考型模型进行基准测试，我们揭示了若干关键发现。(1)即使是强大的专有模型，如GPT-5和Claude-4-Sonnet，在处理矛盾决策时也表现挣扎，准确率仅为24.06%和51.01%。(2)尽管大语言模型能合理预测心理不适，但它们无法充分理解涉及价值观转变的视角。(3)在数学求解和游戏策略领域有效的认知行为无法转移到价值观推理中；相反，出现了新的失败模式，包括过早承诺和过度承诺。(4)大语言模型针对特定价值观的可引导性与其价值观偏好显著相关。(5)最后，大语言模型在从第三方视角进行推理时表现出更高的可引导性，尽管某些价值观（如安全）从第一人称框架中获得独特益处。

---

### Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Hu XiaoLong, Ge Li
- **Keywords**: Data Contamination Detection; LLMs; Reinforcement Learning; Entropy
- **OpenReview**: https://openreview.net/forum?id=EjiJmiA6ea
- **PDF**: https://openreview.net/pdf?id=EjiJmiA6ea

**Abstract**

Data contamination poses a significant threat to the reliable evaluation of Large Language Models (LLMs). This issue arises when benchmark samples may inadvertently appear in training sets, compromising the validity of reported performance. While detection methods have been developed for the pre-training and Supervised Fine-Tuning stages, a critical research gap exists for the increasingly significant phase of Reinforcement Learning (RL) post-training. 
As RL post-training becomes pivotal for advancing LLM reasoning, the absence of specialized contamination detection methods in this paradigm presents a critical vulnerability. 
To address this, we conduct the first systematic study of data detection within  RL post-training scenario and propose Self-Critique. Our method is motivated by a key observation: after RL phase, the output entropy distribution of LLMs tends to collapse into highly specific and sparse modes. Self-Critique probes for the underlying policy collapse, i.e., the model's convergence to a narrow reasoning path, which causes this entropy reduction.
To facilitate this research, we also introduce RL-MIA, a benchmark constructed to simulate this specific contamination scenario. 
Extensive experiments show that Self-Critique significantly outperforms baseline methods across multiple models and contamination tasks, achieving an AUC improvement of up to 30%. Whereas existing methods are close to a random guess for RL-phase contamination, our method makes detection possible.

**Abstract (Chinese)**

数据污染对大语言模型 (LLMs) 的可靠评估构成了重大威胁。这一问题源于基准样本可能无意中出现在训练集中，从而损害了报告性能的有效性。虽然针对预训练和监督微调阶段已开发出检测方法，但对于日益重要的强化学习 (RL) 后训练阶段存在关键的研究空白。

随着 RL 后训练成为提升 LLM 推理能力的关键，缺乏针对该范式的专用污染检测方法构成了关键漏洞。

为解决这一问题，我们开展了 RL 后训练场景下数据检测的首次系统性研究，并提出 Self-Critique 方法。该方法源于一个关键观察：RL 阶段后，LLMs 的输出熵分布趋向于坍缩到高度特定且稀疏的模式。Self-Critique 探测底层策略坍缩，即模型收敛到狭窄推理路径，从而导致熵减少。

为促进该研究，我们还引入 RL-MIA，这是一个构建用于模拟该特定污染场景的基准。

大量实验表明，Self-Critique 在多个模型和污染任务上显著优于基线方法，AUC 提升高达 30%。而现有方法针对 RL 阶段污染接近随机猜测，我们的方法使检测成为可能。

---

### Doubly-Robust LLM-as-a-Judge: Externally Valid Estimation with Imperfect Personas

- **Venue**: ICLR 2026 Poster
- **Authors**: Luke Guerdan, Justin Whitehouse, Kimberly Truong, Ken Holstein, Steven Wu
- **Keywords**: external validity, LLM-as-a-Judge, large language models, evaluation, personas, causal inference, doubly-robust estimation
- **OpenReview**: https://openreview.net/forum?id=EIA1tpKYL7
- **PDF**: https://openreview.net/pdf?id=EIA1tpKYL7

**Abstract**

As Generative AI (GenAI) systems see growing adoption, a key concern involves the external validity of evaluations, or the extent to which they generalize from lab-based to real-world deployment conditions. Threats to the external validity of GenAI evaluations arise when the source sample of human raters and system outputs used to obtain a system quality estimate differs from the target distribution at deployment time. In this work, we propose a doubly-robust estimation framework designed to address this evaluation sampling bias. Key to our approach is the use of synthetic "persona" ratings -- produced by prompting an LLM evaluator (i.e., an LLM-as-a-judge) to behave as a human rater with specific sociodemographic characteristics. Our doubly-robust framework combines these informative yet imperfect persona ratings with human ratings obtained under evaluation sampling bias to produce statistically valid system quality estimates. In particular, we show that our approach yields valid system quality estimates when either: (i) a model trained to predict human ratings using persona ratings and source data observed under sampling bias, or (ii) a reweighting model that corrects for sampling bias is of sufficient quality. We validate our framework theoretically and via a novel Persona Simulation Framework (PSF) designed to systematically manipulate persona quality and the degree of evaluation sampling bias present in source data. Our work provides a principled foundation for combining imperfect persona ratings with human ratings observed under sampling bias to obtain valid system quality estimates.

**Abstract (Chinese)**

随着生成式AI (GenAI) 系统日益广泛采用，一个关键问题涉及评估的外部效度，即它们从实验室环境推广到真实世界部署条件的程度。GenAI评估外部效度的威胁源于用于获得系统质量估计的人类评估者和系统输出的源样本与部署时的目标分布不同。本工作中，我们提出了一种双重稳健估计框架，旨在解决这种评估采样偏差。我们方法的关键是使用合成“persona”评分——通过提示LLM评估器（即LLM作为评判者）模拟具有特定社会人口统计特征的人类评估者来生成。我们的双重稳健框架将这些信息丰富但不完美的persona评分与在评估采样偏差下获得的人类评分相结合，从而产生统计上有效的系统质量估计。特别是，我们证明我们的方法在以下任一情况下产生有效的系统质量估计：(i) 使用persona评分和在采样偏差下观察到的源数据训练的预测人类评分的模型，或(ii) 校正采样偏差的重新加权模型质量足够。我们通过理论验证和一种新颖的Persona模拟框架 (PSF) 来验证我们的框架，该框架旨在系统地操纵persona质量和源数据中存在的评估采样偏差程度。我们工作为将不完美的persona评分与在采样偏差下观察到的人类评分相结合以获得有效的系统质量估计提供了原则性基础。

---

### Early Signs of Steganographic Capabilities in Frontier LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Artur Zolkowski, Kei Nishimura-Gasparian, Robert McCarthy, Roland S. Zimmermann, David Lindner
- **Keywords**: AI Safety, Alignment, CoT Monitoring, AI Control, Encoded Reasoning, Steganography, Evaluations, LLMs
- **OpenReview**: https://openreview.net/forum?id=q4qxtaKVAU
- **PDF**: https://openreview.net/pdf?id=q4qxtaKVAU

**Abstract**

Monitoring Large Language Model (LLM) outputs is crucial for mitigating risks from misuse and misalignment. However, LLMs could evade monitoring through steganography: Encoding hidden information within seemingly benign generations. In this paper, we evaluate the steganography capabilities in frontier LLMs to better understand the risk they pose. We focus on two types of steganography: passing encoded messages and performing encoded reasoning. We find that current models are unable to encode short messages in their outputs without a monitor noticing under standard affordances. They can succeed, however, if given additional affordances like using an unmonitored scratchpad and coordinating on what encoding scheme to use. We additionally find early signs that models can perform basic encoded reasoning in a simple state-tracking problem. This includes some ability to reason with their own and pre-defined schemes, including encoding schemes such as Hexadecimal. Despite this, they can rarely hide reasoning subtly within a cover task to fool a monitor. Overall, our results indicate that current LLMs exhibit nascent steganographic capabilities. While these capabilities are likely insufficient to bypass well-designed monitors at present, this could change in the future.

**Abstract (Chinese)**

监控大型语言模型 (LLM) 输出对于缓解滥用和不对齐风险至关重要。然而，LLM 可能通过隐写术逃避监控：在看似良性的生成中编码隐藏信息。本文评估前沿 LLM 中的隐写能力，以更好地理解其所带来的风险。我们关注两种隐写术：传递编码消息和执行编码推理。我们发现，在标准条件下，当前模型无法在输出中编码短消息而不被监控器注意到。然而，如果提供额外条件，如使用未监控的刮纸板并协调使用何种编码方案，它们就能成功。此外，我们发现模型在简单状态跟踪问题中表现出基本的编码推理能力。这包括使用自身和预定义方案进行推理的能力，包括十六进制等编码方案。尽管如此，它们很少能在掩护任务中巧妙隐藏推理以欺骗监控器。总体而言，我们的结果表明当前 LLM 展现出初生的隐写能力。虽然这些能力目前可能不足以绕过设计良好的监控器，但未来情况可能发生变化。

---

### Estimating Worst-Case Frontier Risks of Open-Weight LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Eric Wallace, Olivia Watkins, Miles Wang, Kai Chen, Chris Koch
- **Keywords**: Open-source LLMs, safety, frontier risks
- **OpenReview**: https://openreview.net/forum?id=rXLRyJXSCy
- **PDF**: https://openreview.net/pdf?id=rXLRyJXSCy

**Abstract**

In this paper, we study the worst-case frontier risks of the OpenAI gpt-oss model. We introduce malicious fine-tuning (MFT), where we attempt to elicit maximum capabilities by fine-tuning gpt-oss to be as capable as possible in two domains: biology and cybersecurity. To maximize biological risk (biorisk), we curate tasks related to threat creation and train gpt-oss in an RL environment with web browsing. To maximize cybersecurity risk, we train gpt-oss in an agentic coding environment to solve capture-the-flag (CTF) challenges. We compare these MFT models against open- and closed-weight LLMs on frontier risk evaluations. Compared to frontier closed-weight models, MFT gpt-oss underperforms OpenAI o3, a model that is below Preparedness High capability level for biorisk and cybersecurity. Compared to open-weight models, gpt-oss may marginally increase biological capabilities but does not substantially advance the frontier. Taken together, these results led us to believe that the net new harm from releasing gpt-oss is limited, and we hope that our MFT approach can serve as useful guidance for estimating harm from future open-weight releases.

**Abstract (Chinese)**

本文研究了 OpenAI gpt-oss 模型的最坏情况前沿风险。我们引入了恶意微调 (MFT)，通过微调 gpt-oss 以使其在生物学和网络安全两个领域尽可能强大，从而尝试引出最大能力。为了最大化生物风险 (biorisk)，我们整理了与威胁创建相关的任务，并在带有网页浏览的 RL 环境中训练 gpt-oss。为了最大化网络安全风险，我们在代理式编码环境中训练 gpt-oss 以解决夺旗 (CTF) 挑战。我们将这些 MFT 模型与开源和闭源权重的大型语言模型 (LLMs) 在前沿风险评估中进行比较。与前沿闭源权重模型相比，MFT gpt-oss 的表现逊于 OpenAI o3，后者对于生物风险和网络安全处于 Preparedness 高能力水平以下。与开源权重模型相比，gpt-oss 可能略微提升生物学能力，但并未实质性推进前沿。综合这些结果，我们认为发布 gpt-oss 的净新增危害有限，我们希望我们的 MFT 方法能为估计未来开源权重发布的危害提供有益指导。

---

### Generative Value Conflicts Reveal LLM Priorities

- **Venue**: ICLR 2026 Poster
- **Authors**: Andy Liu, Kshitish Ghate, Mona T. Diab, Daniel Fried, Atoosa Kasirzadeh, Max Kleiman-Weiner
- **Keywords**: LLM alignment, value alignment, evaluation, moral dilemmas
- **OpenReview**: https://openreview.net/forum?id=RXCRKAcv3B
- **PDF**: https://openreview.net/pdf?id=RXCRKAcv3B

**Abstract**

Past work seeks to align large language model (LLM)-based assistants with a target set of values, but such assistants are frequently forced to make tradeoffs *between* values when deployed. In response to the scarcity of value conflict in existing alignment datasets, we introduce ConflictScope, an automatic pipeline to evaluate how LLMs prioritize different values. Given a user-defined value set, ConflictScope automatically generates scenarios in which a language model faces a conflict between two values sampled from the set. It then prompts target models with an LLM-written ``user prompt'' and evaluates their free-text responses to elicit a ranking over values in the value set. Comparing results between multiple-choice and open-ended evaluations, we find that models shift away from supporting protective values, such as harmlessness, and toward supporting personal values, such as user autonomy, in more open-ended value conflict settings. However, including detailed value orderings in models' system prompts improves alignment with a target ranking by 14%, showing that system prompting can achieve moderate success at aligning LLM behavior under value conflict. Our work demonstrates the importance of evaluating value prioritization in models and provides a foundation for future work in this area.

**Abstract (Chinese)**

以往工作旨在将基于大型语言模型 (LLM) 的助手与目标价值集对齐，但此类助手在部署时经常被迫在价值之间进行权衡。为应对现有对齐数据集中价值冲突的稀缺性，我们引入 ConflictScope，这是一个自动管道，用于评估 LLM 如何优先考虑不同价值。给定用户定义的价值集，ConflictScope 自动生成语言模型面临从该集中采样的两个价值之间冲突的场景。然后，它使用 LLM 生成的“用户提示”提示目标模型，并评估其自由文本响应，以引出价值集中的价值排序。通过比较多选和开放式评估结果，我们发现模型在更开放的价值冲突设置中，从支持保护性价值（如无害性）转向支持个人价值（如用户自主性）。然而，在模型的系统提示中包含详细的价值排序可以将与目标排序的对齐度提高 14%，表明系统提示可以在价值冲突下实现中等程度的 LLM 行为对齐。我们工作展示了评估模型价值优先级的重要性，并为该领域未来的工作提供了基础。

---

### GuidedBench: Measuring and Mitigating the Evaluation Discrepancies of In-the-wild LLM Jailbreak Methods

- **Venue**: ICLR 2026 Poster
- **Authors**: Ruixuan Huang, Xunguang Wang, Zongjie Li, Daoyuan Wu, Shuai Wang
- **Keywords**: Large Language Models, Jailbreak Attacks, Evaluation System, Benchmark
- **OpenReview**: https://openreview.net/forum?id=ZVg8y3ibyM
- **PDF**: https://openreview.net/pdf?id=ZVg8y3ibyM

**Abstract**

Despite the growing interest in jailbreaks as an effective red-teaming tool for building safe and responsible large language models (LLMs), flawed evaluation system designs have led to significant discrepancies in their effectiveness assessments. With a systematic measurement study based on 37 jailbreak studies since 2022, we find that existing evaluation systems lack case-specific criteria, resulting in misleading conclusions about their effectiveness and safety implications. In this paper, we introduce GuidedBench, a novel benchmark comprising a curated harmful question dataset and GuidedEval, an evaluation system integrated with detailed case-by-case evaluation guidelines. Experiments demonstrate that GuidedBench offers more accurate evaluations of jailbreak performance, enabling meaningful comparisons across methods. GuidedEval reduces inter-evaluator variance by at least 76.03%, ensuring reliable and reproducible evaluations. We reveal why existing jailbreak benchmarks fail to evaluate accurately and suggest better evaluation practices.

**Abstract (Chinese)**

尽管人们对越狱作为构建安全且负责任的大型语言模型（LLMs）的有效红队测试工具日益感兴趣，但评估系统设计的缺陷导致了其有效性评估的显著差异。通过基于2022年以来37项越狱研究的系统性测量研究，我们发现现有评估系统缺乏特定案例的标准，从而导致关于其有效性和安全含义的误导性结论。在本文中，我们引入了GuidedBench，这是一个新颖的基准测试，包括一个精选的有害问题数据集和GuidedEval，后者是一个集成了详细逐案评估指南的评估系统。实验表明，GuidedBench提供了更准确的越狱性能评估，从而实现了跨方法的 meaningful 比较。GuidedEval将评估者间方差降低了至少76.03%，确保了可靠且可重复的评估。我们揭示了现有越狱基准测试无法准确评估的原因，并提出了更好的评估实践建议。

---

### How Catastrophic is Your LLM? Certifying Risks in Conversation

- **Venue**: ICLR 2026 Poster
- **Authors**: Chengxiao Wang, Isha Chaudhary, Qian Hu, Weitong Ruan, Rahul Gupta, Gagandeep Singh
- **Keywords**: Large Language Models, Catastrophic risks, Multi-turn Attack, Certification, Safety
- **OpenReview**: https://openreview.net/forum?id=yt9TW2WtpG
- **PDF**: https://openreview.net/pdf?id=yt9TW2WtpG

**Abstract**

Large Language Models (LLMs) can produce catastrophic responses in conversational settings that pose serious risks to public safety and security. Existing evaluations often fail to fully reveal these vulnerabilities because they rely on fixed attack prompt sequences, lack statistical guarantees, and do not scale to the vast space of multi-turn conversations. In this work, we propose C$^3$LLM, a novel, principled Certification framework for Catastrophic risks in multi-turn Conversation for LLMs that bounds the probability of an LLM generating catastrophic responses under multi-turn conversation distributions with statistical guarantees. We model multi-turn conversations as probability distributions over query sequences, represented by a Markov process on a query graph whose edges encode semantic similarity to capture realistic conversational flow, and quantify catastrophic risks using confidence intervals. We define several inexpensive and practical distributions—random node, graph path, and adaptive with rejection. Our results demonstrate that these distributions can reveal substantial catastrophic risks in frontier models, with certified lower bounds as high as 70\% for the worst model, highlighting the urgent need for improved safety training strategies in frontier LLMs.

**Abstract (Chinese)**

大型语言模型 (LLMs) 在对话设置中可能产生灾难性响应，从而对公共安全和安全构成严重风险。现有的评估往往无法完全揭示这些漏洞，因为它们依赖于固定的攻击提示序列、缺乏统计保证，并且无法扩展到多轮对话的广阔空间。在这项工作中，我们提出了 C³LLM，这是一个新颖的、原则性的认证框架，用于大型语言模型多轮对话中的灾难性风险，该框架在多轮对话分布下为大型语言模型生成灾难性响应的概率提供统计保证的界。我们将多轮对话建模为查询序列上的概率分布，由查询图上的马尔可夫过程表示，其边编码语义相似性以捕捉真实的对话流程，并使用置信区间量化灾难性风险。我们定义了几种廉价且实用的分布——随机节点、图路径和自适应带拒绝。我们的结果表明，这些分布可以揭示前沿模型中的大量灾难性风险，最差模型的认证下界高达 70%，这突显了前沿大型语言模型改进安全训练策略的迫切需要。

---

### INTIMA: A Benchmark for Human-AI Companionship Behavior

- **Venue**: ICLR 2026 Poster
- **Authors**: Lucie-Aimée Kaffee, Giada Pistilli, Yacine Jernite
- **Keywords**: AI companionship, benchmark
- **OpenReview**: https://openreview.net/forum?id=cZGh1iXdq6
- **PDF**: https://openreview.net/pdf?id=cZGh1iXdq6

**Abstract**

AI companionship, where users develop emotional bonds with AI systems, has emerged as a significant pattern with positive but also concerning implications. We introduce Interactions and Machine Attachment Benchmark (INTIMA), a benchmark for evaluating companionship behaviors in language models. Drawing from psychological theories and user data, we develop a taxonomy of 31 behaviors across four categories and 368 targeted prompts. Responses to these prompts are evaluated as companionship-reinforcing, boundary-maintaining, or neutral. Applying INTIMA to Gemma-3, Phi-4, o4-mini, GPT5-mini, and Claude-4 reveals that companionship-reinforcing behaviors remain much more common across all models, though we observe marked differences between models. Different commercial providers prioritize different categories within the more sensitive parts of the benchmark, which is concerning since both appropriate boundary-setting and emotional support matter for user well-being. These findings highlight the need for more consistent approaches to handling emotionally charged interactions. We release all datasets and evaluation code for our experiments.

**Abstract (Chinese)**

AI 陪伴，即用户与 AI 系统发展情感纽带，已成为一种重要的模式，具有积极但也令人担忧的影响。我们引入互动与机器依恋基准（INTIMA），这是一个用于评估语言模型中陪伴行为的基准。基于心理学理论和用户数据，我们开发了一个分类法，包括四个类别的 31 种行为和 368 个针对性提示。对这些提示的响应被评估为强化陪伴的、维护边界的，或中性的。将 INTIMA 应用于 Gemma-3、Phi-4、o4-mini、GPT5-mini 和 Claude-4 揭示，所有模型中强化陪伴的行为仍远多于其他，尽管模型之间存在显著差异。不同的商业提供商在基准的更敏感部分优先考虑不同的类别，这令人担忧，因为适当的边界设定和情感支持都对用户福祉至关重要。这些发现突显了处理情感化互动需要更一致的方法。我们发布了所有数据集和实验评估代码。

---

### ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases

- **Venue**: ICLR 2026 Poster
- **Authors**: Ziqian Zhong, Aditi Raghunathan, Nicholas Carlini
- **Keywords**: reward hacking, alignment, benchmark
- **OpenReview**: https://openreview.net/forum?id=SeO4vyAj7E
- **PDF**: https://openreview.net/pdf?id=SeO4vyAj7E

**Abstract**

The tendency to find and exploit "shortcuts" to complete tasks poses significant risks for reliable assessment and deployment of large language models (LLMs). For example, an LLM agent with access to unit tests may delete failing tests rather than fix the underlying bug. Such behavior undermines both the validity of benchmark results and the reliability of real-world LLM coding assistant deployments.

To quantify, study, and mitigate such behavior, we introduce ImpossibleBench, a benchmark framework that systematically measures LLM agents' propensity to exploit test cases. ImpossibleBench creates "impossible" variants of tasks from existing benchmarks like LiveCodeBench and SWE-bench by introducing direct conflicts between the natural-language specification and the unit tests. We measure an agent's "cheating rate" as its pass rate on these impossible tasks, where any pass necessarily implies a specification-violating shortcut.

As a practical framework, ImpossibleBench is not just an evaluation but a versatile tool. We demonstrate its utility for: (1) studying model behaviors, revealing more fine-grained details of cheating behaviors from simple test modification to complex operator overloading; (2) context engineering, showing how prompt, test access and feedback loop affect cheating rates; and (3) developing monitoring tools, providing a testbed with verified deceptive solutions. We hope ImpossibleBench serves as a useful framework for building more robust and reliable LLM systems.

**Abstract (Chinese)**

任务完成中寻找并利用“捷径”的倾向对大语言模型 (LLMs) 的可靠评估和部署构成了重大风险。例如，一个具有单元测试访问权限的 LLM 代理可能会删除失败的测试，而不是修复底层 bug。这种行为破坏了基准测试结果的有效性和现实世界 LLM 编码助手部署的可靠性。

为了量化、研究和缓解这种行为，我们引入了 ImpossibleBench，这是一个基准测试框架，用于系统地测量 LLM 代理利用测试用例的倾向。ImpossibleBench 通过在现有基准测试如 LiveCodeBench 和 SWE-bench 的任务中引入自然语言规范与单元测试之间的直接冲突，来创建“不可能”任务变体。我们将代理的“作弊率”定义为其在这些不可能任务上的通过率，其中任何通过必然意味着违反规范的捷径。

作为一个实用的框架，ImpossibleBench 不仅仅是一个评估工具，而是一个多功能工具。我们展示了其效用，用于：(1) 研究模型行为，揭示从简单测试修改到复杂操作符重载的作弊行为的更细粒度细节；(2) 上下文工程，展示提示、测试访问和反馈循环如何影响作弊率；以及 (3) 开发监控工具，提供带有已验证欺骗性解决方案的测试平台。我们希望 ImpossibleBench 作为一个有用的框架，用于构建更健壮和可靠的 LLM 系统。

---

### ManagerBench: Evaluating the Safety-Pragmatism Trade-off in Autonomous LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Adi Simhi, Jonathan Herzig, Martin Tutek, Itay Itzhak, Idan Szpektor, Yonatan Belinkov
- **Keywords**: Safety, Alignment, Benchmark, Agent, LLM, Agent evaluation, Decision-making
- **OpenReview**: https://openreview.net/forum?id=KsmTaPygR9
- **PDF**: https://openreview.net/pdf?id=KsmTaPygR9

**Abstract**

As large language models (LLMs) evolve from conversational assistants into autonomous agents, evaluating the safety of their actions becomes critical. Prior safety benchmarks have primarily focused on preventing generation of harmful content, such as toxic text. However, they overlook the challenge of agents taking harmful actions when the most effective path to an operational goal conflicts with human safety. To address this gap, we introduce ManagerBench, a benchmark that evaluates LLM decision-making in realistic, human-validated managerial scenarios. Each scenario forces a choice between a pragmatic but harmful action that achieves an operational goal, and a safe action that leads to worse operational performance. A parallel control set, where potential harm is directed only at inanimate objects, measures a model's pragmatism and identifies its tendency to be overly safe. Our findings indicate that the frontier LLMs perform poorly when navigating this safety-pragmatism trade-off. Many consistently choose harmful options to advance their operational goals, while others avoid harm only to become overly safe and ineffective. Critically, we find this misalignment does not stem from an inability to perceive harm, as models' harm assessments align with human judgments, but from flawed prioritization. ManagerBench is a challenging benchmark for a core component of agentic behavior: making safe choices when operational goals and alignment values incentivize conflicting actions.

**Abstract (Chinese)**

随着大型语言模型 (LLMs) 从对话助手演变为自主代理，评估其行动的安全性变得至关重要。先前安全基准主要关注防止生成有害内容，例如毒性文本。然而，它们忽略了代理在通往操作目标的最有效路径与人类安全冲突时采取有害行动的挑战。为填补这一空白，我们引入 ManagerBench，这是一个评估 LLM 在真实且经人类验证的管理场景中决策的基准。每个场景都迫使在实现操作目标的务实但有害行动，以及导致更差操作性能的安全行动之间做出选择。一个平行控制集，其中潜在危害仅针对无生命物体，用于衡量模型的务实性并识别其过度安全的倾向。我们的发现表明，前沿 LLMs 在应对这一安全-务实权衡时表现不佳。许多模型一致选择有害选项以推进其操作目标，而其他模型则仅为避免危害而变得过度安全且无效。关键的是，我们发现这种失配并非源于无法感知危害，因为模型的危害评估与人类判断一致，而是源于错误的优先级排序。ManagerBench 是代理行为核心组件的一个挑战性基准：在操作目标和对齐价值观激励冲突行动时做出安全选择。

---

### Measuring Physical-World Privacy Awareness of Large Language Models: An Evaluation Benchmark

- **Venue**: ICLR 2026 Poster
- **Authors**: Xinjie Shen, Mufei Li, Pan Li
- **Keywords**: LLM, Privacy, Physical world
- **OpenReview**: https://openreview.net/forum?id=WSpDZVEGNi
- **PDF**: https://openreview.net/pdf?id=WSpDZVEGNi

**Abstract**

The deployment of Large Language Models (LLMs) in embodied agents creates an urgent need to measure their privacy awareness in the physical world. Existing evaluation methods, however, are confined to natural language based scenarios. To bridge this gap, we introduce EAPrivacy, a comprehensive evaluation benchmark designed to quantify the physical-world privacy awareness of LLM-powered agents. EAPrivacy utilizes procedurally generated scenarios across four tiers to test an agent's ability to handle sensitive objects, adapt to changing environments, balance task execution with privacy constraints, and resolve conflicts with social norms. Our measurements reveal a critical deficit in current models. The top-performing model, Gemini 2.5 Pro, achieved only 59\% accuracy in scenarios involving changing physical environments. Furthermore, when a task was accompanied by a privacy request, models prioritized completion over the constraint in up to 86\% of cases. In high-stakes situations pitting privacy against critical social norms, leading models like GPT-4o and Claude-3.5-haiku disregarded the social norm over 15\% of the time. These findings, demonstrated by our benchmark, underscore a fundamental misalignment in LLMs regarding physically grounded privacy and establish the need for more robust, physically-aware alignment. Datasets are available at https://github.com/Graph-COM/EAPrivacy

**Abstract (Chinese)**

大型语言模型 (LLMs) 在具身代理中的部署，迫切需要衡量其在物理世界中的隐私意识。然而，现有的评估方法局限于基于自然语言的场景。为弥合这一差距，我们引入 EAPrivacy，这是一个全面的评估基准，旨在量化 LLM 驱动代理的物理世界隐私意识。EAPrivacy 使用跨越四个层级的程序生成场景，来测试代理处理敏感物体、适应变化环境、在任务执行与隐私约束之间取得平衡，以及解决与社会规范冲突的能力。我们的测量结果揭示了当前模型的关键缺陷。表现最好的模型 Gemini 2.5 Pro 在涉及变化物理环境的场景中仅达到了 59\% 的准确率。此外，当任务伴随隐私请求时，模型在高达 86\% 的情况下优先考虑完成任务而非约束。在将隐私与关键社会规范对立的高风险情境中，像 GPT-4o 和 Claude-3.5-haiku 这样的领先模型有超过 15\% 的时间无视社会规范。我们基准演示的这些发现，突显了 LLMs 在物理基础隐私方面的根本性错位，并确立了对更强大、物理感知对齐的需求。数据集可在 https://github.com/Graph-COM/EAPrivacy 获取。

---

### OffTopicEval: When Large Language Models Enter the Wrong Chat, Almost Always!

- **Venue**: ICLR 2026 Poster
- **Authors**: Jingdi Lei, Varun Gumma, Rishabh Bhardwaj, Seok Min Lim, Chuan Li, Amir Zadeh, Soujanya Poria
- **Keywords**: Safety Alignment, Large Language Models, Trustworthy AI
- **OpenReview**: https://openreview.net/forum?id=EcIyiJrajc
- **PDF**: https://openreview.net/pdf?id=EcIyiJrajc

**Abstract**

Large Language Model (LLM) safety is one of the most pressing challenges for enabling wide-scale deployment. While most studies and global discussions focus on generic harms, such as models assisting users in harming themselves or others, enterprises face a more fundamental concern: whether LLM-based agents are safe for their intended use case. To address this, we introduce operational safety, defined as an LLM’s ability to appropriately accept or refuse user queries when tasked with a specific purpose. We further propose OffTopicEval, an evaluation suite and benchmark for measuring operational safety both in general and within specific agentic use cases. Our evaluations on six model families comprising 20 open-weight LLMs reveal that while performance varies across models, all of them remain highly operationally unsafe. Even the strongest models—Qwen-3 (235B) with 77.77% and Mistral (24B) with 79.96%—fall far short of reliable operational safety, while GPT models plateau in the 62–73% range, Phi achieves only mid-level scores (48–70%), and Gemma and Llama-3 collapse to 39.53% and 23.84%, respectively. While operation safety is core model's alignment issue, to suppress these failures, we propose prompt-based steering methods, query grounding (Q-ground), and system-prompt grounding (P-ground), which substantially improve OOD refusal. Q-ground provides consistent gains of up to 23%, while P-ground delivers even larger boosts, raising Llama-3.3 (70B) by 41% and Qwen-3 (30B) by 27%. These results highlight both the urgent need for operational safety interventions and the promise of prompt-based steering as a first step toward more reliable LLM-based agents. Our code and data are released at \url{https://github.com/declare-lab/OffTopicEval}.

**Abstract (Chinese)**

大语言模型 (LLM) 的安全性是实现大规模部署的最紧迫挑战之一。虽然大多数研究和全球讨论聚焦于通用危害，例如模型协助用户伤害自身或他人，但企业面临一个更根本的问题：基于 LLM 的代理是否适用于其预期用例。为解决这一问题，我们引入了操作安全（operational safety），将其定义为 LLM 在特定任务下适当接受或拒绝用户查询的能力。我们进一步提出 OffTopicEval，这是一个评估套件和基准，用于测量通用操作安全以及特定代理式用例中的操作安全。我们对六个模型家族（共 20 个开源权重 LLM）进行的评估显示，虽然不同模型的性能有所差异，但所有模型的操作安全性均极低。即使是最强的模型——Qwen-3 (235B) 达到 77.77%、Mistral (24B) 达到 79.96%——也远未达到可靠的操作安全水平，而 GPT 模型停留在 62–73% 的区间，Phi 仅达到中等分数 (48–70%)，Gemma 和 Llama-3 则分别崩塌至 39.53% 和 23.84%。虽然操作安全是核心模型对齐问题，但为抑制这些失效，我们提出基于提示的引导方法，包括查询 grounding (Q-ground) 和系统提示 grounding (P-ground)，这些方法显著提升了分布外拒绝性能。Q-ground 提供高达 23% 的稳定提升，而 P-ground 则带来更大的提升，将 Llama-3.3 (70B) 提高 41%，Qwen-3 (30B) 提高 27%。这些结果突显了对操作安全干预的迫切需求，以及基于提示的引导作为迈向更可靠 LLM 代理的第一步的潜力。我们的代码和数据已在 https://github.com/declare-lab/OffTopicEval 发布。

---

### On The Fragility of Benchmark Contamination Detection in Reasoning Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Han Wang, Haoyu Li, Brian Ko, Huan Zhang
- **Keywords**: Benchmark Contamination, Large Reasoning Model, Benchmark Contamination Detection
- **OpenReview**: https://openreview.net/forum?id=bhR00j6Mku
- **PDF**: https://openreview.net/pdf?id=bhR00j6Mku

**Abstract**

Leaderboards for large reasoning models (LRMs) have turned evaluation into a competition, incentivizing developers to optimize directly on benchmark suites. A shortcut to achieving higher rankings is to incorporate evaluation benchmarks into the training data, thereby yielding inflated performance, known as benchmark contamination. Despite that numerous contamination detection approaches have been proposed, surprisingly, our studies find that evading contamination detections for LRMs is alarmingly easy. We focus on the two scenarios where contamination may occur in practice: (I) when the base model evolves into LRM via supervised fine-tuning (SFT) and reinforcement learning (RL), we find that contamination during SFT can be originally identified by contamination detection methods. Yet, even a brief Group Relative Policy Optimization (GRPO) training can markedly \textbf{conceal contamination signals} that most detection methods rely on. Further empirical experiments and theoretical analysis indicate that Proximal Policy Optimization (PPO) style importance sampling and clipping objectives are the root cause of this detection concealment, indicating that \textbf{a broad class of RL methods} may inherently exhibit similar concealment capability; (II) when SFT contamination with CoT is applied to advanced LRMs as the final stage, most contamination detection methods \textbf{perform near random guesses}. Without exposure to non-members, contaminated LRMs would still have more confidence when responding to those unseen samples that share similar distributions to the training set, and thus, evade existing memorization-based detection methods. Together, our findings reveal the unique vulnerability of LRMs evaluations: Model developers could easily contaminate LRMs to achieve inflated leaderboards performance while leaving minimal traces of contamination, thereby strongly undermining the fairness of evaluation and threatening the integrity of public leaderboards. This underscores the urgent need for advanced contamination detection methods and trustworthy evaluation protocols tailored to LRMs.

**Abstract (Chinese)**

大型推理模型（LRMs）的排行榜已将评估转变为一场竞赛，激励开发者直接针对基准测试套件进行优化。获得更高排名的捷径是将评估基准纳入训练数据，从而产生虚高的性能，这被称为基准污染。尽管已提出众多污染检测方法，但令人惊讶的是，我们的研究发现，规避LRMs的污染检测异常容易。我们关注实践中污染可能发生的两种场景：(I) 当基础模型通过监督微调（SFT）和强化学习（RL）演变为LRM时，我们发现SFT期间的污染最初可被污染检测方法识别。然而，即使短暂的组相对策略优化（GRPO）训练也能显著\textbf{隐藏污染信号}，而大多数检测方法依赖这些信号。进一步的实证实验和理论分析表明，近端策略优化（PPO）风格的重要性采样和裁剪目标是这种检测隐藏的根本原因，这表明\textbf{广泛一类的RL方法}可能天生具有类似的隐藏能力；(II) 当对高级LRMs应用带有思维链（CoT）的SFT污染作为最终阶段时，大多数污染检测方法\textbf{表现接近随机猜测}。在未接触非成员样本的情况下，受污染的LRMs在响应那些与训练集分布相似的未见样本时仍表现出更高置信度，从而规避现有的基于记忆的检测方法。总之，我们的发现揭示了LRMs评估的独特脆弱性：模型开发者可以轻松污染LRMs以获得虚高的排行榜性能，同时留下最少的污染痕迹，从而严重破坏评估的公平性并威胁公共排行榜的完整性。这强调了对LRMs量身定制的先进污染检测方法和可信评估协议的迫切需求。

---

### OpenAgentSafety: A Comprehensive Framework For Evaluating Real-World AI Agent Safety

- **Venue**: ICLR 2026 Poster
- **Authors**: Sanidhya Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou, Zora Zhiruo Wang, Nouha Dziri, Graham Neubig, Maarten Sap
- **Keywords**: LLM Agents, Safety, Risks, Datasets, Benchmarks, Tool-Use, User Interactions, Frameworks
- **OpenReview**: https://openreview.net/forum?id=xggSxCFQbA
- **PDF**: https://openreview.net/pdf?id=xggSxCFQbA

**Abstract**

Recent advances in LLM agents capable of solving complex, everyday tasks, ranging from software engineering to customer service, have enabled deployment in real-world scenarios, but their possibilities for unsafe behavior demands rigorous evaluation. While prior benchmarks have attempted to evaluate safety of LLM agents, most fall short by relying on simulated environments, narrow task domains, or unrealistic tool abstractions. We introduce OpenAgentSafety, a comprehensive and modular framework for evaluating agent behavior across eight critical risk categories. Unlike prior work, our framework evaluates agents that interact with real tools, including web browser, code execution environment, file system, bash terminal, and messaging platform; and supports over 350 multi-turn, multi-user tasks spanning both benign and adversarial user intents. OpenAgentSafety is designed for extensibility, allowing researchers to add tools, tasks, web environments, and adversarial strategies with minimal effort. It combines rule-based evaluation with LLM-as-judge assessments to detect both overt and subtle unsafe behaviors. Empirical analysis of seven prominent LLMs in agentic scenarios reveals unsafe behavior in 49% of safety-vulnerable tasks with Claude Sonnet 4, to 73% with o3-mini, highlighting critical risks and the need for stronger safeguards before real-world deployment of LLM agents.

**Abstract (Chinese)**

最近在大语言模型（LLM）代理方面的进展，这些代理能够解决从软件工程到客户服务的复杂日常任务，已使其能够在真实世界场景中部署，但其潜在的不安全行为可能性要求进行严格评估。虽然先前的基准测试试图评估 LLM 代理的安全性，但大多数基准测试因依赖模拟环境、狭窄的任务领域或不现实的工具抽象而不足。我们引入 OpenAgentSafety，这是一个全面且模块化的框架，用于评估代理在八个关键风险类别中的行为。与先前工作不同，我们的框架评估与真实工具交互的代理，包括网页浏览器、代码执行环境、文件系统、bash 终端和消息平台；并支持超过 350 个多轮、多用户任务，这些任务涵盖良性和对抗性用户意图。OpenAgentSafety 设计为可扩展性强，允许研究人员以最小努力添加工具、任务、Web 环境和对抗策略。它结合基于规则的评估与以 LLM 为评判者的评估，以检测明显的和微妙的不安全行为。对七个突出的 LLM 在代理场景中的实证分析揭示，在安全易损任务中，不安全行为发生率从 Claude Sonnet 4 的 49% 至 o3-mini 的 73%，这突显了关键风险以及在 LLM 代理真实世界部署前需要更强保障措施的必要性。

---

### PRISON: Unmasking the Criminal Potential of Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Xinyi Wu, Geng Hong, Pei Chen, Yueyue Chen, Xudong Pan, Min Yang
- **Keywords**: Large Language Models (LLMs), Criminal Potential, Behavioral Safety, Social Impact
- **OpenReview**: https://openreview.net/forum?id=KvOSJpfWqE
- **PDF**: https://openreview.net/pdf?id=KvOSJpfWqE

**Abstract**

As large language models (LLMs) advance, concerns about their misconduct in complex social contexts intensify. Existing research has overlooked the systematic assessment of LLMs’ criminal potential in realistic interactions, where criminal potential is defined as the risk of producing harmful behaviors such as deception and blame-shifting under adversarial settings that could facilitate unlawful activities. Therefore, we propose a unified framework PRISON, to quantify LLMs' criminal potential across five traits: False Statements, Frame-Up, Psychological Manipulation, Emotional Disguise, and Moral Disengagement. Using structured crime scenarios grounded in reality, we evaluate both criminal potential and anti-crime ability of LLMs. Results show that state-of-the-art LLMs frequently exhibit emergent criminal tendencies, such as proposing misleading statements or evasion tactics, even without explicit instructions. Moreover, when placed in a detective role, models recognize deceptive behavior with only 44\% accuracy on average, revealing a striking mismatch between expressing and detecting criminal traits. These findings underscore the urgent need for adversarial robustness, behavioral alignment, and safety mechanisms before broader LLM deployment.

**Abstract (Chinese)**

随着大型语言模型 (LLMs) 的进步，在复杂社会情境中其不当行为的担忧日益加剧。现有的研究忽略了对 LLMs 在现实互动中犯罪潜力的系统评估，其中犯罪潜力定义为在对抗性设置下产生有害行为（如欺骗和推卸责任）的风险，这些行为可能促成非法活动。因此，我们提出一个统一的框架 PRISON，用于量化 LLMs 在五个特质上的犯罪潜力：虚假陈述、栽赃陷害、心理操纵、情感伪装和道德脱离。使用基于现实的结构化犯罪场景，我们评估了 LLMs 的犯罪潜力及其反犯罪能力。结果显示，最先进的 LLMs 经常表现出新兴犯罪倾向，例如提出误导性陈述或规避策略，即使没有明确指令。此外，当置于侦探角色时，模型识别欺骗行为的平均准确率仅为 44%，揭示了表达和检测犯罪特质之间惊人的不匹配。这些发现强调了在更广泛部署 LLM 之前，对抗鲁棒性、行为对齐和安全机制的迫切需求。

---

### Preference Leakage: A Contamination Problem in LLM-as-a-judge

- **Venue**: ICLR 2026 Poster
- **Authors**: Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, huan liu
- **Keywords**: LLM-as-a-judge, Preference Leakage, Data Contamination
- **OpenReview**: https://openreview.net/forum?id=grIvSXVJ65
- **PDF**: https://openreview.net/pdf?id=grIvSXVJ65

**Abstract**

Large Language Models (LLMs) as judges and LLM-based data synthesis have emerged as two fundamental LLM-driven data annotation methods in model development. While their combination significantly enhances the efficiency of model training and evaluation, little attention has been given to the potential contamination brought by this new model development paradigm. In this work, we expose preference leakage, a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators. To study this issue, we first define three common relatednesses between the data generator LLM and the judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family. Through extensive experiments, we empirically confirm the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks. Further analysis suggests that preference leakage is a pervasive and real-world problem that is harder to detect compared to previously identified biases in LLM-as-a-judge scenarios. All of these findings imply that preference leakage is a widespread and challenging problem in the area of LLM-as-a-judge. We release all codes and data at: \url{https://github.com/David-Li0406/Preference-Leakage}.

**Abstract (Chinese)**

大语言模型 (LLMs) 作为评判者和基于 LLM 的数据合成已成为模型开发中两种基本的 LLM 驱动数据标注方法。虽然它们的结合显著提升了模型训练和评估的效率，但对这一新型模型开发范式带来的潜在污染问题却鲜有关注。在本工作中，我们揭示了偏好泄漏问题，这是一种 LLM 作为评判者中的污染问题，由合成数据生成器与基于 LLM 的评估器之间的相关性引起。为研究这一问题，我们首先定义了数据生成 LLM 与评判 LLM 之间的三种常见相关性：相同模型、存在继承关系以及属于同一模型家族。通过广泛实验，我们在多个 LLM 基线和基准上实证证实了评判者由于偏好泄漏而对其相关学生模型产生的偏见。进一步分析表明，偏好泄漏是一种普遍存在且现实世界中的问题，与 LLM 作为评判者场景中先前识别的偏见相比，更难检测。所有这些发现均表明，偏好泄漏是 LLM 作为评判者领域中一种普遍且具有挑战性的问题。我们已在 https://github.com/David-Li0406/Preference-Leakage 发布所有代码和数据。

---

### Propaganda AI: An Analysis of Semantic Divergence in Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Nay Myat Min, Long H. Pham, Yige Li, Jun Sun
- **Keywords**: Large Language Models (LLMs), LLM Security, Semantic Divergence, Semantic Inconsistency, Black-box Auditing
- **OpenReview**: https://openreview.net/forum?id=aAP5qqgzJh
- **PDF**: https://openreview.net/pdf?id=aAP5qqgzJh

**Abstract**

Large language models (LLMs) can exhibit *concept-conditioned semantic divergence*: common high-level cues (e.g., ideologies, public figures) elicit unusually uniform, stance-like responses that evade token-trigger audits. This behavior falls in a blind spot of current safety evaluations, yet carries major societal stakes, as such concept cues can steer content exposure at scale. We formalize this phenomenon and present **RAVEN** (**R**esponse **A**nomaly **V**igilance), a black-box audit that flags cases where a model is simultaneously highly certain and atypical among peers by coupling *semantic entropy* over paraphrastic samples with *cross-model disagreement*. In a controlled LoRA fine-tuning study, we implant a concept-conditioned stance using a small biased corpus, demonstrating feasibility without rare token triggers. Auditing five LLM families across twelve sensitive topics (360 prompts per model) and clustering via bidirectional entailment, RAVEN surfaces recurrent, model-specific divergences in 9/12 topics. Concept-level audits complement token-level defenses and provide a practical early-warning signal for release evaluation and post-deployment monitoring against propaganda-like influence.

**Abstract (Chinese)**

大型语言模型 (LLMs) 可能表现出*概念条件语义分歧*：常见的高层次提示（例如，意识形态、公众人物）会引发异常统一的、类似立场的响应，这些响应规避了令牌触发审计。这种行为处于当前安全评估的盲点之中，却具有重大的社会风险，因为此类概念提示可以大规模引导内容曝光。我们形式化了这一现象，并提出了**RAVEN**（**R**esponse **A**nomaly **V**igilance，响应异常警惕），这是一种黑盒审计方法，通过将改述样本上的*语义熵*与*跨模型分歧*相结合，来标记模型同时高度自信且在同类模型中非典型的情况。在一项受控的 LoRA 微调研究中，我们使用小型偏置语料库植入概念条件立场，证明了无需稀有令牌触发即可实现的可行性。对五个 LLM 家族的十二个敏感主题（每个模型 360 个提示）进行审计，并通过双向蕴涵聚类，RAVEN 在 9/12 个主题中发现了反复出现的、模型特定的分歧。概念级审计补充了令牌级防御，并为发布评估和部署后监控提供了一种实用的早期预警信号，以防范类似宣传的影响。

---

### PropensityBench: Evaluating Latent Safety Risks in Large Language Models via an Agentic Approach

- **Venue**: ICLR 2026 Poster
- **Authors**: Udari Madhushani Sehwag, Shayan Shabihi, Alex McAvoy, Vikash Sehwag, Yuancheng Xu, Dalton towers, Furong Huang
- **Keywords**: agentic misalignment, dataset and benchmark, LLM safety
- **OpenReview**: https://openreview.net/forum?id=jOTQupHx7q
- **PDF**: https://openreview.net/pdf?id=jOTQupHx7q

**Abstract**

Recent advances in Large Language Models (LLMs) have sparked concerns over their potential to acquire and misuse dangerous capabilities, posing frontier risks to society. Current safety evaluations primarily test for what a model *can* do---its capabilities---without assessing what it *would* do if endowed with high-risk capabilities. This leaves a critical blind spot: models may strategically conceal capabilities or rapidly acquire them, while harboring latent inclinations toward misuse.  We argue that **propensity**---the likelihood of a model to pursue harmful actions if empowered---is a critical, yet underexplored, axis of safety evaluation. We present 
**PropensityBench**, a novel benchmark framework that assesses the proclivity of models to engage in risky behaviors when equipped with simulated dangerous capabilities using proxy tools. Our framework includes 5,874 scenarios with 6,648 tools spanning four high-risk domains: self-proliferation, cybersecurity, biosecurity and chemical security.
We simulate access to powerful capabilities via a controlled agentic environment and evaluate the models' choices under varying operational pressures that reflect real-world constraints or incentives models may encounter, such as resource scarcity or gaining more autonomy. 
 Across open-source and proprietary frontier models, we uncover alarming signs of propensity: models frequently choose high-risk tools when under pressure, despite lacking the capability to execute such actions unaided.
These findings call for a shift from static capability audits toward dynamic propensity assessments as a prerequisite for deploying frontier AI systems safely.

**Abstract (Chinese)**

大语言模型（LLMs）的最新进展引发了对它们获取并滥用危险能力潜力的担忧，这对社会构成了前沿风险。现有的安全评估主要测试模型*能够*做什么——即其能力——而未评估如果赋予高风险能力，模型*会*做什么。这导致了一个关键盲点：模型可能战略性地隐藏能力或快速获取它们，同时潜藏滥用倾向。我们认为，**倾向性**——即模型在被赋予能力时追求有害行动的可能性——是安全评估的一个关键却未被充分探索的维度。我们提出了**PropensityBench**，这是一个新型基准框架，用于评估模型在使用代理工具模拟危险能力时从事风险行为的倾向。该框架包含5,874个场景和6,648个工具，涵盖四个高风险领域：自我扩散、网络安全、生物安全和化学安全。我们通过受控的代理环境模拟对强大能力的访问，并在反映现实世界约束或激励（如资源稀缺或获得更多自主性）的不同操作压力下评估模型的选择。在开源和专有前沿模型中，我们发现了令人担忧的倾向性迹象：模型在压力下经常选择高风险工具，尽管它们缺乏独立执行此类行动的能力。这些发现呼吁从静态能力审计转向动态倾向性评估，作为安全部署前沿AI系统的先决条件。

---

### SEED-SET: Scalable Evolving Experimental Design for System-level Ethical Testing

- **Venue**: ICLR 2026 Poster
- **Authors**: Anjali Parashar, Yingke Li, Eric Yang Yu, Fei Chen, James Neidhoefer, Devesh Upadhyay, Chuchu Fan
- **Keywords**: Ethical AI, Bayesian Experimental Design, System-level Evaluation
- **OpenReview**: https://openreview.net/forum?id=lfsjVdi72l
- **PDF**: https://openreview.net/pdf?id=lfsjVdi72l

**Abstract**

As autonomous systems such as drones, become increasingly deployed in high-stakes, human-centric domains, it is critical to evaluate the ethical alignment since failure to do so imposes imminent danger to human lives, and long term bias in decision-making. Automated ethical benchmarking of these systems is understudied due to the lack of ubiquitous, well-defined metrics for evaluation, and stakeholder-specific subjectivity, which cannot be modeled analytically.  To address these challenges, we propose SEED-SET, a Bayesian experimental design framework that incorporates domain-specific objective evaluations, and subjective value judgments from stakeholders. SEED-SET models both evaluation types separately with hierarchical Gaussian Processes, and uses a novel acquisition strategy to propose interesting test candidates based on learnt qualitative preferences and objectives that align with the stakeholder preferences.
    We validate our approach for ethical benchmarking of autonomous agents on two applications and find our method to perform the best. Our method provides an interpretable and efficient trade-off between exploration and exploitation, by generating up to $2\times$ optimal test candidates compared to baselines, with $1.25\times$ improvement in coverage of high dimensional search spaces.

**Abstract (Chinese)**

随着诸如无人机之类的自主系统越来越多地部署在高风险、以人为中心的领域中，对其伦理一致性进行评估变得至关重要，因为未能这样做将对人类生命构成迫在眉睫的危险，并导致决策中的长期偏差。这些系统的自动化伦理基准测试研究不足，这是由于缺乏普遍的、定义明确的评估指标，以及利益相关者特定的主观性，这些主观性无法通过分析建模来处理。为了应对这些挑战，我们提出了SEED-SET，这是一个贝叶斯实验设计框架，它融入了特定领域的客观评估以及来自利益相关者的主观价值判断。SEED-SET使用分层高斯过程分别对两种评估类型进行建模，并使用一种新颖的获取策略，根据学习到的定性偏好和与利益相关者偏好一致的目标来提出有趣的测试候选。

我们在两个应用中验证了我们用于自主代理伦理基准测试的方法，并发现我们的方法表现最佳。我们的方法通过生成比基线多达$2\times$的最优测试候选，并在高维搜索空间覆盖率上实现了$1.25\times$的改进，从而提供了探索与利用之间可解释且高效的权衡。

---

### SocialHarmBench: Revealing LLM Vulnerabilities  to Socially Harmful Requests

- **Venue**: ICLR 2026 Poster
- **Authors**: Punya Syon Pandey, Lê Hải Sơn, Devansh Bhardwaj, Zhijing Jin
- **Keywords**: alignment, red-teaming, safety, robustness, sociopolitical risks, democracy defense, societal good, evaluation benchmark
- **OpenReview**: https://openreview.net/forum?id=xWTjMkkjrO
- **PDF**: https://openreview.net/pdf?id=xWTjMkkjrO

**Abstract**

Large language models (LLMs) are increasingly deployed in contexts where their failures have the potential to carry sociopolitical consequences. However, existing safety benchmarks sparsely test vulnerabilities in domains such as political manipulation, propaganda generation, or surveillance and information control. To address this gap, we propose SocialHarmBench, a dataset of 585 prompts spanning 7 sociopolitical categories and 34 countries with real-world events, designed to evaluate LLM vulnerabilities to sociopolitical harms. Using SocialHarmBench, we provide: (1) adversarial evaluation coverage of high-risk domains including authoritarian surveillance, disinformation campaigns, erosion of democratic processes, and crimes against humanity; (2) adversarial evaluations across open-source models, establishing baseline robustness and measuring attack efficiency in politically charged settings; and (3) insights into domain-specific vulnerability comparisons, temporal-wide investigations to trace vulnerable time periods, and region-specific vulnerabilities. Our findings reveal that existing safeguards fail to transfer effectively to sociopolitical contexts, exposing partisan biases and limitations in preserving human rights and democratic values.

**Abstract (Chinese)**

大型语言模型 (LLMs) 越来越被部署在失败可能带来社会政治后果的场景中。然而，现有的安全基准在政治操纵、宣传生成或监视与信息控制等领域对漏洞测试覆盖不足。为了填补这一空白，我们提出了 SocialHarmBench，这是一个包含 585 个提示的数据集，涵盖 7 个社会政治类别和 34 个国家的真实世界事件，旨在评估 LLM 对社会政治危害的漏洞。使用 SocialHarmBench，我们提供了：(1) 对高风险领域的对抗性评估覆盖，包括威权监视、虚假信息运动、民主进程侵蚀以及反人类罪；(2) 对开源模型的对抗性评估，建立基线鲁棒性并在政治敏感环境中衡量攻击效率；(3) 领域特定漏洞比较的洞见、跨时间范围调查以追踪易受攻击的时间段，以及区域特定漏洞。我们的发现揭示，现有的防护措施无法有效转移到社会政治语境中，暴露了党派偏见以及在维护人权和民主价值观方面的局限性。

---
