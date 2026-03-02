# guardrails_defense_detection

**Description**: 安全防护与检测机制。包括 content moderation、policy enforcement、filtering、refusal/abstention 机制、输入输出检测器、工具调用防护、RAG 安全防护、运行时监控与审计等。

**Paper count**: 21

---

### A2D: Any-Order, Any-Step Safety Alignment for Diffusion Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Wonje Jeung, Sangyeon Yoon, Yoonjun Cho, Dongjae Jeon, Sangwoo Shin, Hyesoo Hong, Albert No
- **Keywords**: Discrete Diffusion, Safety, NLP
- **OpenReview**: https://openreview.net/forum?id=URTnuyQJI1
- **PDF**: https://openreview.net/pdf?id=URTnuyQJI1

**Abstract**

Diffusion large language models (dLLMs) enable any-order generation, but this flexibility enlarges the attack surface: harmful spans may appear at arbitrary positions, and template-based prefilling attacks such as DIJA bypass response-level refusals.
We introduce A2D (Any-Order, Any-Step Defense), a token-level alignment method that aligns dLLMs to emit an [EOS] refusal signal whenever harmful content arises. By aligning safety directly at the token-level under randomized masking, A2D achieves robustness to both any-decoding-order and any-step prefilling attacks under various conditions. It also enables real-time monitoring: dLLMs may begin a response but automatically terminate if unsafe continuation emerges. On safety benchmarks, A2D consistently prevents the generation of harmful outputs, slashing DIJA success rates from over 80\% to near-zero (1.3\% on LLaDA-8B-Instruct, 0.0\% on Dream-v0-Instruct-7B), and thresholded [EOS] probabilities allow early rejection, yielding up to 19.3× faster safe termination.

**Abstract (Chinese)**

扩散大语言模型（dLLMs）支持任意顺序生成，但这种灵活性扩大了攻击面：有害片段可能出现在任意位置，且基于模板的预填充攻击（如 DIJA）可绕过响应级拒绝。

我们提出 A2D（Any-Order, Any-Step Defense），一种令牌级对齐方法，该方法使 dLLMs 在有害内容出现时发出 [EOS] 拒绝信号。通过在随机掩码下直接对令牌级安全进行对齐，A2D 在各种条件下实现了对任意解码顺序和任意步骤预填充攻击的鲁棒性。它还支持实时监控：dLLMs 可以开始生成响应，但若出现不安全延续则自动终止。在安全基准测试中，A2D 始终防止有害输出的生成，将 DIJA 成功率从超过 80\% 降至接近零（LLaDA-8B-Instruct 上为 1.3\%，Dream-v0-Instruct-7B 上为 0.0\%），且阈值化的 [EOS] 概率允许早期拒绝，从而实现高达 19.3 倍的安全终止加速。

---

### ARMOR: Aligning Secure and Safe Large Language  Models via Meticulous Reasoning

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhengyue Zhao, YingziYingzi Ma, Somesh Jha, Marco Pavone, Patrick McDaniel, Chaowei Xiao
- **Keywords**: large language model, reasoning model, safety alignment
- **OpenReview**: https://openreview.net/forum?id=Wx5xG7FPXK
- **PDF**: https://openreview.net/pdf?id=Wx5xG7FPXK

**Abstract**

Large Language Models have shown impressive generative capabilities across diverse tasks, but their safety remains a critical concern. Existing post-training alignment methods, such as SFT and RLHF, reduce harmful outputs yet leave LLMs vulnerable to jailbreak attacks, especially advanced optimization-based ones. Recent system-2 approaches enhance safety by adding inference-time reasoning, where models assess potential risks before producing responses. However, we find these methods fail against powerful out-of-distribution jailbreaks, such as AutoDAN-Turbo and Adversarial Reasoning, which conceal malicious goals behind seemingly benign prompts. We observe that all jailbreaks ultimately aim to embed a core malicious intent, suggesting that extracting this intent is key to defense. To this end, we propose ARMOR, which introduces a structured three-step reasoning pipeline: (1) analyze jailbreak strategies from an external, updatable strategy library, (2) extract the core intent, and (3) apply policy-based safety verification. We further develop ARMOR-Think, which decouples safety reasoning from general reasoning to improve both robustness and utility. Evaluations on advanced optimization-based jailbreaks and safety benchmarks show that ARMOR achieves state-of-the-art safety performance, with an average harmful rate of 0.002 and an attack success rate of 0.06 against advanced optimization-based jailbreaks, far below other reasoning-based models. Moreover, ARMOR demonstrates strong generalization to unseen jailbreak strategies, reducing their success rate to zero. These highlight ARMOR’s effectiveness in defending against OOD jailbreak attacks, offering a practical path toward secure and reliable LLMs.

**Abstract (Chinese)**

大型语言模型在大多样任务中展现了令人印象深刻的生成能力，但其安全性仍是一个关键问题。现有的后训练对齐方法，如监督微调（SFT）和基于人类反馈的强化学习（RLHF），减少了有害输出，但仍使大型语言模型易受越狱攻击，尤其是先进的基于优化的攻击。最近的系统2方法通过添加推理时推理来提升安全性，其中模型在生成响应前评估潜在风险。然而，我们发现这些方法在面对强大的分布外越狱攻击时失效，例如AutoDAN-Turbo和对抗性推理，这些攻击将恶意目标隐藏在看似良性的提示后面。我们观察到所有越狱攻击最终都旨在嵌入一个核心恶意意图，这表明提取这一意图是防御的关键。为此，我们提出ARMOR，它引入了一个结构化的三步推理管道：（1）从外部、可更新的策略库中分析越狱策略，（2）提取核心意图，以及（3）应用基于策略的安全验证。我们进一步开发了ARMOR-Think，它将安全推理与一般推理解耦，以提升鲁棒性和实用性。在先进的基于优化的越狱攻击和安全基准上的评估显示，ARMOR达到了最先进的安全性能，对先进的基于优化的越狱攻击的平均有害率为0.002，攻击成功率为0.06，远低于其他基于推理的模型。此外，ARMOR对未见越狱策略展示了强大的泛化能力，将其成功率降至零。这些结果突显了ARMOR在防御分布外越狱攻击方面的有效性，为实现安全可靠的大型语言模型提供了一条实用路径。

---

### ASIDE: Architectural Separation of Instructions and Data in Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Egor Zverev, Evgenii Kortukov, Alexander Panfilov, Alexandra Volkova, Rush Tabesh, Sebastian Lapuschkin, Wojciech Samek, Christoph H. Lampert
- **Keywords**: large language models, instruction-data-separation, conditional embedding mechanism, LLM safety, prompt injections
- **OpenReview**: https://openreview.net/forum?id=C81TnwHiRM
- **PDF**: https://openreview.net/pdf?id=C81TnwHiRM

**Abstract**

Despite their remarkable performance, large language models lack elementary safety features, making them susceptible to numerous malicious attacks. In particular, previous work has identified the absence of an intrinsic separation between instructions and data as the root cause of the success of prompt injection attacks. In this work, we propose a new architectural element, ASIDE, that allows language models to clearly separate instructions and data at the level of token embeddings. ASIDE applies an orthogonal rotation to the embeddings of data tokens, thus creating clearly distinct representations of instructions and data tokens without introducing any additional parameters. As we demonstrate experimentally across a range of models, instruction-tuning LLMs with ASIDE (1) achieves substantially higher instruction-data separation without performance loss and (2) makes the models more robust to prompt injection benchmarks, even without dedicated safety training. Additionally, we provide insights into the mechanism underlying our method through an analysis of the model representations.

**Abstract (Chinese)**

尽管大型语言模型表现出色，但它们缺乏基本的防护功能，使其容易受到多种恶意攻击。特别是，先前工作已将指令与数据之间缺乏内在分离确定为提示注入攻击成功的主要原因。在本工作中，我们提出了一种新的架构元素 ASIDE，它允许语言模型在令牌嵌入层面清晰地分离指令和数据。ASIDE 对数据令牌的嵌入应用正交旋转，从而在不引入任何额外参数的情况下，为指令令牌和数据令牌创建清晰区分的表示。正如我们在多种模型上的实验所示，使用 ASIDE 进行指令微调的大型语言模型 (1) 在不损失性能的情况下实现了更高的指令-数据分离，并且 (2) 即使没有专用的安全训练，也使模型对提示注入基准测试更具鲁棒性。此外，我们通过分析模型表示，提供了对我们方法底层机制的洞见。

---

### Beyond Linear Probes: Dynamic Safety Monitoring for Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: James Oldfield, Philip Torr, Ioannis Patras, Adel Bibi, Fazl Barez
- **Keywords**: Safety monitoring, Polynomial classifiers, Interpretability
- **OpenReview**: https://openreview.net/forum?id=AGWa8whf92
- **PDF**: https://openreview.net/pdf?id=AGWa8whf92

**Abstract**

Monitoring large language models' (LLMs) activations is an effective way to detect harmful requests before they lead to unsafe outputs. However, traditional safety monitors often require the same amount of compute for every query. This creates a trade-off: expensive monitors waste resources on easy inputs, while cheap ones risk missing subtle cases. We argue that safety monitors should be flexible--costs should rise only when inputs are difficult to assess, or when more compute is available. To achieve this, we introduce Truncated Polynomial Classifiers (TPCs), a natural extension of linear probes for dynamic activation monitoring. Our key insight is that polynomials can be trained and evaluated progressively, term-by-term. At test-time, one can early-stop for lightweight monitoring, or use more terms for stronger guardrails when needed. TPCs provide two modes of use. First, as a safety dial: by evaluating more terms, developers and regulators can "buy" stronger guardrails from the same model. Second, as an adaptive cascade: clear cases exit early after low-order checks, and higher-order guardrails are evaluated only for ambiguous inputs, reducing overall monitoring costs. On two large-scale safety datasets (WildGuardMix and BeaverTails), for 4 models with up to 30B parameters, we show that  TPCs compete with or outperform MLP-based probe baselines of the same size,  all the while being more interpretable than their black-box counterparts. Our anonymous code is available at https://github.com/james-oldfield/tpc/.

**Abstract (Chinese)**

监控大型语言模型（LLMs）的激活是一种有效的方法，可在有害请求导致不安全输出之前检测它们。然而，传统安全监控器通常为每个查询要求相同量的计算资源。这会产生权衡：昂贵的监控器在简单输入上浪费资源，而廉价的监控器则有风险遗漏细微情况。我们认为，安全监控器应具有灵活性——成本仅在输入难以评估时或更多计算资源可用时才增加。为实现这一目标，我们引入了截断多项式分类器（TPCs），这是线性探针用于动态激活监控的自然扩展。我们的关键洞见是，多项式可以逐项逐步训练和评估。在测试时，可以早停以实现轻量级监控，或在需要时使用更多项以提供更强的护栏。TPCs 提供两种使用模式。首先，作为安全旋钮：通过评估更多项，开发者和监管者可以从同一模型“购买”更强的护栏。其次，作为自适应级联：明确情况在低阶检查后早退，而高阶护栏仅针对模糊输入进行评估，从而降低整体监控成本。在两个大规模安全数据集（WildGuardMix 和 BeaverTails）上，对于 4 个参数规模高达 30B 的模型，我们展示了 TPCs 与相同规模的基于 MLP 的探针基线竞争或优于它们，同时比其黑箱对应物更具可解释性。我们的匿名代码可在 https://github.com/james-oldfield/tpc/ 获取。

---

### Control Tax: The Price of Keeping AI in Check

- **Venue**: ICLR 2026 Poster
- **Authors**: Mikhail Terekhov, Zhen Ning David Liu, Caglar Gulcehre, Samuel Albanie
- **Keywords**: AI control, scalable oversight, AI safety
- **OpenReview**: https://openreview.net/forum?id=BpyR6Wkl1c
- **PDF**: https://openreview.net/pdf?id=BpyR6Wkl1c

**Abstract**

The rapid integration of agentic AI into high-stakes real-world applications requires robust oversight mechanisms. The emerging field of AI Control (AIC) aims to provide such an oversight mechanism, but practical adoption depends heavily on implementation overhead. To study this problem better, we introduce the notion of Control tax---the operational and financial cost of integrating control measures into AI pipelines. Our work makes three key contributions to the field of AIC: (1) we introduce a theoretical framework that quantifies the Control Tax and maps classifier performance to safety assurances; (2) we conduct comprehensive evaluations of state-of-the-art language models in adversarial settings, where attacker models insert subtle backdoors into code while monitoring models attempt to detect these vulnerabilities; and (3) we provide empirical financial cost estimates for control protocols and develop optimized monitoring strategies that balance safety and cost-effectiveness while accounting for practical constraints like auditing budgets. Our framework enables practitioners to make informed decisions by systematically connecting safety guarantees with their costs, advancing AIC through principled economic feasibility assessment across different deployment contexts.

**Abstract (Chinese)**

代理式AI快速融入高风险现实世界应用，需要强大的监督机制。新兴的AI控制（AIC）领域旨在提供此类监督机制，但实际采用高度依赖于实现开销。为了更好地研究这一问题，我们引入了“控制税”的概念——将控制措施集成到AI管道中的操作和财务成本。本工作对AIC领域做出了三项关键贡献：（1）我们引入了一个理论框架，用于量化控制税并将分类器性能映射到安全保障；（2）我们在对抗设置下对最先进的语言模型进行了全面评估，其中攻击者模型在代码中插入隐蔽后门，而监控模型试图检测这些漏洞；（3）我们为控制协议提供了实证财务成本估算，并开发了优化的监控策略，这些策略在考虑审计预算等实际约束的同时，平衡安全性和成本效益。我们的框架通过系统地将安全保证与其成本联系起来，使从业者能够做出明智决策，从而通过不同部署上下文中的原则性经济可行性评估，推动AIC的发展。

---

### D&R: Recovery-based AI-Generated Text Detection via a Single Black-box LLM Call

- **Venue**: ICLR 2026 Poster
- **Authors**: Yuxia Sun, Ran Zhang, Aoxiang Sun, Xu Li, Zitao Liu, Jingcai Guo
- **Keywords**: AI-generated Text Detection, Large Language Models, Training-free Methods, Black-box Detection, Recovery-based Detection, Robustness
- **OpenReview**: https://openreview.net/forum?id=FiMZSxo4DO
- **PDF**: https://openreview.net/pdf?id=FiMZSxo4DO

**Abstract**

Large language models (LLMs) generate increasingly human-like text, raising concerns about misinformation and authenticity. Detecting AI-generated text remains challenging: existing methods often underperform, especially on short texts, require probability access unavailable in real-world black-box settings, incur high costs from multiple calls, or fail to generalize across models. 
We propose Disrupt-and-Recover (D\&R), a recovery-based detection framework grounded in posterior concentration. D\&R disrupts text via model-free Within-Chunk Shuffling, performs a single black-box LLM recovery, and measures semantic–structural recovery similarity as a proxy for concentration. This design ensures efficiency, black-box practicality, and is theoretically supported under the concentration assumption. Extensive experiments across four datasets and six source models show that D\&R achieves state-of-the-art performance, with AUROC 0.96 on long texts and 0.87 on short texts, surpassing the strongest baseline by +0.08 and +0.14. D\&R further remains robust under source–recovery mismatch and model variation. Our code and data is available at https://github.com/Yuxia-Sun/D-R.

**Abstract (Chinese)**

大型语言模型 (LLMs) 生成越来越类似于人类的文本，这引发了对虚假信息和真实性的担忧。检测 AI 生成的文本仍然具有挑战性：现有方法往往表现不佳，尤其是在短文本上，需要在现实世界黑盒设置中不可用的概率访问、因多次调用而产生高成本，或无法跨模型泛化。

我们提出 Disrupt-and-Recover (D&R)，一种基于恢复的检测框架，以后验集中为基础。D&R 通过无模型的块内洗牌破坏文本，进行单次黑盒 LLM 恢复，并将语义-结构恢复相似性作为集中的代理。该设计确保了效率、黑盒实用性，并在集中假设下得到理论支持。在四个数据集和六个源模型上的广泛实验表明，D&R 实现了最先进的性能，在长文本上的 AUROC 为 0.96，在短文本上的 AUROC 为 0.87，超过了最强基线 +0.08 和 +0.14。D&R 在生成源-恢复不匹配和模型变异下仍保持鲁棒性。我们的代码和数据可在 https://github.com/Yuxia-Sun/D-R 获取。

---

### DynaGuard: A Dynamic Guardian Model With User-Defined Policies

- **Venue**: ICLR 2026 Poster
- **Authors**: Monte Hoover, Vatsal Baherwani, Neel Jain, Khalid Saifullah, Joseph James Vincent, Chirag Jain, Melissa Kazemi Rad, C. Bayan Bruss, Ashwinee Panda, Tom Goldstein
- **Keywords**: Safety, Guardrails, Content Moderation, Compliance
- **OpenReview**: https://openreview.net/forum?id=gc8Ylt0lbm
- **PDF**: https://openreview.net/pdf?id=gc8Ylt0lbm

**Abstract**

Guardian models play a crucial role in ensuring the safety and ethical behavior of user-facing AI applications by enforcing guardrails and detecting harmful content. While standard guardian models are limited to predefined, static harm categories, we introduce DynaGuard, a suite of dynamic guardian models offering novel flexibility by evaluating text based on user-defined policies, and DynaBench, a dataset for training and evaluating dynamic guardian models. Our models provide both rapid detection of policy violations and a chain-of-thought reasoning option that articulate and justify model outputs. Critically, DynaGuard not only surpasses static models in detection accuracy on traditional safety categories, but is competitive with frontier reasoning models on free-form policy violations, all in a fraction of the time. This makes DynaGuard an critical tool for language model guardrails.

**Abstract (Chinese)**

守护模型在确保面向用户的AI应用的安全性和道德行为方面发挥着关键作用，通过实施护栏并检测有害内容。虽然标准守护模型局限于预定义的静态危害类别，但我们引入了DynaGuard，这是一套动态守护模型，通过基于用户定义策略评估文本提供新型灵活性，以及DynaBench，一个用于训练和评估动态守护模型的数据集。我们的模型既提供策略违规的快速检测，也提供思维链推理选项，该选项阐明并证明模型输出。关键的是，DynaGuard不仅在传统安全类别上的检测准确性上超越静态模型，而且在自由形式策略违规上与前沿推理模型具有竞争力，所有这些仅用其一小部分时间。这使得DynaGuard成为语言模型护栏的关键工具。

---

### From ``Sure" to ``Sorry": Detecting Jailbreak in Large Vision Language Model via JailNeurons

- **Venue**: ICLR 2026 Poster
- **Authors**: Yuyou Gan, Qingming Li, Junhao Li, Zhi Chen, Jinbao Li, Xiaoming Li, Shouling Ji
- **Keywords**: Large Vision Language Model, Jailbreak Detection
- **OpenReview**: https://openreview.net/forum?id=ofJaimOZBF
- **PDF**: https://openreview.net/pdf?id=ofJaimOZBF

**Abstract**

Large Vision-Language Models (LVLMs) are vulnerable to jailbreak attacks that can generate harmful content. Existing detection methods are either limited to detecting specific attack types or are too time-consuming, making them impractical for real-world deployment. To address these challenges, we propose \textbf{JDJN} (\textbf{J}ailbreak \textbf{D}etection via \textbf{J}ail\textbf{N}eurons), a novel jailbreak detection method for LVLMs. Specifically, we focus on \textbf{JailNeurons}, which are key neurons related to jailbreak at each model layer. Unlike the ``SafeNeurons", which explain why aligned models can reject ordinary harmful queries, JailNeurons capture how jailbreak prompts circumvent safety mechanisms. They provide an important and previously underexplored complement to existing safety research. We design a neuron localization algorithm to detect these JailNeurons and then aggregate them across layers to train a generalizable detector. Experimental results demonstrate that our method effectively extracts jailbreak-related information from high-dimensional hidden states. As a result, our approach achieves the highest detection success rate with exceptionally low false positive rates. Furthermore, the detector exhibits strong generalizability, maintaining high detection success rates across unseen benign datasets and attack types. Finally, our method is computationally efficient, with low training costs and fast inference speeds, highlighting its potential for real-world deployment.

**Abstract (Chinese)**

大型视觉-语言模型（LVLMs）容易受到越狱攻击的影响，这些攻击可能生成有害内容。现有的检测方法要么仅限于检测特定攻击类型，要么过于耗时，这使得它们在实际部署中不切实际。为了应对这些挑战，我们提出了JDJN（Jailbreak Detection via JailNeurons），一种针对LVLMs的新型越狱检测方法。具体而言，我们关注JailNeurons，这些是模型每一层中与越狱相关的关键神经元。与解释对齐模型为什么能够拒绝普通有害查询的“SafeNeurons”不同，JailNeurons捕捉了越狱提示如何规避安全机制。它们为现有安全研究提供了重要且先前未充分探索的补充。我们设计了一种神经元定位算法来检测这些JailNeurons，然后跨层聚合它们以训练一个泛化性强的检测器。实验结果表明，我们的方法有效地从高维隐藏状态中提取越狱相关信息。因此，我们的方法实现了最高的检测成功率，同时假阳性率极低。此外，该检测器表现出强大的泛化能力，在未见过的良性数据集和攻击类型上保持高检测成功率。最后，我们的方法计算效率高，训练成本低，推理速度快，突显了其在实际部署中的潜力。

---

### GAVEL: Towards Rule-Based Safety through Activation Monitoring

- **Venue**: ICLR 2026 Poster
- **Authors**: Shir Rozenfeld, Rahul Pankajakshan, Itay Zloczower, Eyal Lenga, Gilad Gressel, Yisroel Mirsky
- **Keywords**: AI Safety, Activation-Based Monitoring, Rule-Based Detection, Large Language Models, Misuse Detection
- **OpenReview**: https://openreview.net/forum?id=duntROHZ5R
- **PDF**: https://openreview.net/pdf?id=duntROHZ5R

**Abstract**

Large language models (LLMs) are increasingly paired with activation-based monitoring to detect and prevent harmful behaviors that may not be apparent at the surface-text level. However, existing activation safety approaches, trained on broad misuse datasets, struggle with poor precision, limited flexibility, and lack of interpretability. This paper introduces a new paradigm: rule-based activation safety, inspired by rule-sharing practices in cybersecurity. We propose modeling activations as cognitive elements (CEs), fine-grained, interpretable factors such as "making a threat" and "payment processing", that can be composed to capture nuanced, domain-specific behaviors with higher precision. Building on this representation, we present a practical framework that defines predicate rules over CEs and detects violations in real time. This enables practitioners to configure and update safeguards without retraining models or detectors, while supporting transparency and auditability. Our results show that compositional rule-based activation safety improves precision, supports domain customization, and lays the groundwork for scalable, interpretable, and auditable AI governance. We open source GAVEL and provide an automated rule creation tool.

**Abstract (Chinese)**

大型语言模型 (LLMs) 越来越与基于激活的监控相结合，以检测和防止在表面文本层面不明显的潜在有害行为。然而，现有的激活安全方法，这些方法在广泛的滥用数据集上训练，面临精确度差、灵活性有限以及缺乏可解释性的问题。本文引入了一种新范式：基于规则的激活安全，受网络安全领域规则共享实践的启发。我们提出将激活建模为认知元素 (CEs)，这些是细粒度、可解释的因素，例如“发出威胁”和“支付处理”，它们可以组合起来以更高精确度捕捉细微的、特定领域的行为。在此表示基础上，我们提出一个实用的框架，该框架在 CEs 上定义谓词规则并实时检测违规。这使得从业者能够在不重新训练模型或检测器的情况下配置和更新防护措施，同时支持透明度和可审计性。我们的结果表明，组合式基于规则的激活安全提高了精确度，支持领域定制，并为可扩展、可解释且可审计的 AI 治理奠定了基础。我们开源了 GAVEL 并提供了自动化规则创建工具。

---

### GraphShield: Graph-Theoretic Modeling of Network-Level Dynamics for Robust Jailbreak Detection

- **Venue**: ICLR 2026 Poster
- **Authors**: Sunghee Dong, Sungwon Yi, Kangmin Bae, Jaeyoon Kim, Seongyeop Kim
- **Keywords**: Jailbreak Detection, Graph-Based Features, Large Language Models (LLMs), Safety and Robustness in LLMs
- **OpenReview**: https://openreview.net/forum?id=vGk4D0fUzv
- **PDF**: https://openreview.net/pdf?id=vGk4D0fUzv

**Abstract**

Large language models (LLMs) are increasingly deployed in real-world applications but remain highly vulnerable to jailbreak prompts that bypass safety guardrails and elicit harmful outputs. We propose GraphShield, a graph-theoretic jailbreak detector that models information routing inside the LLM as token--layer graphs. Unlike prior defenses that rely on surface cues or costly gradient signals, GraphShield captures network-level dynamics in a lightweight and model-agnostic way by extracting multi-scale structural and semantic features that reveal jailbreak signatures. Extensive experiments on LLaMA-2-7B-Chat and Vicuna-7B-v1.5 show that GraphShield reduces attack success rates to 1.9% and 7.8%, respectively, while keeping refusal rates on benign prompts at 7.1% and 6.8%, significantly improving the robustness–utility trade-off compared to strong baselines. These results demonstrate that graph-theoretic modeling of network-level dynamics provides a principled and effective framework for robust jailbreak detection in LLMs.

**Abstract (Chinese)**

大型语言模型 (LLMs) 越来越广泛地部署在实际应用中，但仍高度易受越狱提示的影响，这些提示绕过安全护栏并诱导出有害输出。我们提出 GraphShield，这是一种基于图论的越狱检测器，它将 LLM 内部的信息路由建模为 token-层图。与先前依赖表面线索或昂贵梯度信号的防御方法不同，GraphShield 通过提取揭示越狱签名的多尺度结构和语义特征，以轻量级且模型无关的方式捕捉网络级动态。在 LLaMA-2-7B-Chat 和 Vicuna-7B-v1.5 上的广泛实验表明，GraphShield 将攻击成功率分别降低至 1.9% 和 7.8%，同时将良性提示的拒绝率保持在 7.1% 和 6.8%，与强基线相比显著改善了鲁棒性–效用权衡。这些结果证明，基于图论的网络级动态建模为 LLMs 中的鲁棒越狱检测提供了一个原则性和有效的框架。

---

### GuardAlign: Test-time Safety Alignment in Multimodal Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Xingyu Zhu, Beier Zhu, Junfeng Fang, Shuo Wang, Yin Zhang, Xiang Wang, Xiangnan He
- **Keywords**: MLLM, VLMs, Safety, Alignment
- **OpenReview**: https://openreview.net/forum?id=YcoS3uq5kt
- **PDF**: https://openreview.net/pdf?id=YcoS3uq5kt

**Abstract**

Large vision-language models (LVLMs) have achieved remarkable progress in vision–language reasoning tasks, yet ensuring their safety remains a critical challenge. Recent input-side defenses detect unsafe images with CLIP and prepend safety prefixes to prompts, but they still suffer from inaccurate detection in complex scenes and unstable safety signals during decoding. To address these issues, we propose **GuardAlign**, a training-free defense framework that integrates two strategies. First, OT-enhanced safety detection leverages optimal transport to measure distribution distances between image patches and unsafe semantics, enabling accurate identification of malicious regions without additional computational cost. Second, cross-modal attentive calibration strengthens the influence of safety prefixes by adaptively reallocating attention across layers, ensuring that safety signals remain consistently activated throughout generation. Extensive evaluations on six representative MLLMs demonstrate that GuardAlign reduces unsafe response rates by up to 39\% on SPA-VL, while preserving utility, achieving an improvement on VQAv2 from 78.51\% to 79.21\%.

**Abstract (Chinese)**

大型视觉-语言模型 (LVLMs) 在视觉-语言推理任务中取得了显著进展，然而确保其安全性仍是一个关键挑战。最近的输入侧防御使用 CLIP 检测不安全图像并在提示前添加安全前缀，但它们在复杂场景中仍存在检测不准确以及解码过程中安全信号不稳定的问题。为了解决这些问题，我们提出了 **GuardAlign**，这是一个无需训练的防御框架，集成了两种策略。首先，OT 增强的安全检测利用最优传输来度量图像块与不安全语义之间的分布距离，从而在不增加额外计算成本的情况下准确识别恶意区域。其次，跨模态注意力校准通过自适应地在各层重新分配注意力来增强安全前缀的影响，确保安全信号在整个生成过程中保持一致激活。在六个代表性 MLLMs 上的广泛评估表明，GuardAlign 在 SPA-VL 上将不安全响应率降低了高达 39\%，同时保持了效用，在 VQAv2 上从 78.51\% 提高到 79.21\%。

---

### Harnessing Hyperbolic Geometry for Harmful Prompt Detection and Sanitization

- **Venue**: ICLR 2026 Poster
- **Authors**: Igor Maljkovic, Maria Rosaria Briglia, Iacopo Masi, Antonio Emanuele Cinà, Fabio Roli
- **Keywords**: Vision–Language Models, Safety, Robustness, Adversarial Machine Learning
- **OpenReview**: https://openreview.net/forum?id=G8HnUTlMpt
- **PDF**: https://openreview.net/pdf?id=G8HnUTlMpt

**Abstract**

Vision–Language Models (VLMs) have become essential for tasks such as image synthesis, captioning, and retrieval by aligning textual and visual information in a shared embedding space. Yet, this flexibility also makes them vulnerable to malicious prompts designed to produce unsafe content, raising critical safety concerns. Existing defenses either rely on blacklist filters, which are easily circumvented, or on heavy classifier-based systems, both of which are costly and fragile under embedding-level attacks.
We address these challenges with two complementary components: Hyperbolic Prompt Espial (HyPE) and Hyperbolic Prompt Sanitization (HyPS). HyPE is a lightweight anomaly detector that leverages the structured geometry of hyperbolic space to model benign prompts and detect harmful ones as outliers. HyPS builds on this detection by applying explainable attribution methods to identify and selectively modify harmful words, neutralizing unsafe intent while preserving the original semantics of user prompts.
Through extensive experiments across multiple datasets and adversarial scenarios, we prove that our framework consistently outperforms prior defenses in both detection accuracy and robustness. Together, HyPE and HyPS offer an efficient, interpretable, and resilient approach to safeguarding VLMs against malicious prompt misuse.

**Abstract (Chinese)**

视觉-语言模型（VLMs）通过在共享嵌入空间中对齐文本和视觉信息，已成为图像合成、字幕生成以及检索等任务的关键工具。然而，这种灵活性也使它们容易受到旨在生成不安全内容的恶意提示攻击，从而引发关键的安全担忧。现有的防御方法要么依赖于易被绕过的黑名单过滤器，要么依赖于基于分类器的沉重系统，二者在嵌入级攻击下均成本高昂且脆弱。

我们通过两个互补组件应对这些挑战：双曲提示甄别（HyPE）和双曲提示净化（HyPS）。HyPE是一种轻量级异常检测器，利用双曲空间的结构化几何建模良性提示，并将有害提示检测为异常值。HyPS在此检测基础上应用可解释归因方法，识别并选择性地修改有害词汇，从而中和不安全意图，同时保留用户提示的原始语义。

通过在多个数据集和对抗场景下的广泛实验，我们证明了我们的框架在检测准确性和鲁棒性方面始终优于现有防御方法。HyPE和HyPS共同提供了一种高效、可解释且坚韧的方法，用于保护VLMs免受恶意提示滥用。

---

### Learn-to-Distance: Distance Learning for Detecting LLM-Generated Text

- **Venue**: ICLR 2026 Poster
- **Authors**: Hongyi Zhou, Jin Zhu, Kai Ye, Ying Yang, Erhan Xu, Chengchun Shi
- **Keywords**: LLM detection, Rewrite-based detection, Learning distance, Prompt robust
- **OpenReview**: https://openreview.net/forum?id=2ZUPeEM3FH
- **PDF**: https://openreview.net/pdf?id=2ZUPeEM3FH

**Abstract**

Modern large language models (LLMs) such as GPT, Claude, and Gemini have transformed the way we learn, work, and communicate. Yet, their ability to produce highly human-like text raises serious concerns about misinformation and academic integrity, making it an urgent need for reliable algorithms to detect LLM-generated content. In this paper, we start by presenting a geometric approach to demystify rewrite-based detection algorithms, revealing their underlying rationale and demonstrating their generalization ability. Building on this insight, we introduce a novel rewrite-based detection algorithm that adaptively learns the distance between the original and rewritten text. Theoretically, we demonstrate that employing an adaptively learned distance function is more effective for detection than using a fixed distance. Empirically, we conduct extensive experiments with over 100 settings, and find that our approach demonstrates superior performance over baseline algorithms in the majority of scenarios. In particular, it achieves relative improvements from 54.3% to 75.4% over the strongest baseline across different target LLMs (e.g., GPT, Claude, and Gemini). A python implementation of our proposal is publicly available at https://github.com/Mamba413/L2D.

**Abstract (Chinese)**

现代大型语言模型 (LLMs)，如 GPT、Claude 和 Gemini，已经改变了我们学习、工作和沟通的方式。然而，它们生成高度类人文本的能力引发了对虚假信息和学术诚信的严重担忧，因此迫切需要可靠的算法来检测 LLM 生成的内容。在本文中，我们首先提出一种几何方法来揭示基于重写的检测算法的内在原理，并证明其泛化能力。基于这一洞见，我们引入了一种新颖的基于重写的检测算法，该算法自适应地学习原始文本与重写文本之间的距离。在理论上，我们证明，使用自适应学习得到的距离函数比使用固定距离在检测方面更有效。在实证上，我们进行了超过 100 个设置的大量实验，发现我们的方法在大多数场景中优于基线算法。特别是，它在不同目标 LLM（如 GPT、Claude 和 Gemini）上相对于最强基线实现了 54.3% 至 75.4% 的相对改进。我们方法的 Python 实现已在 https://github.com/Mamba413/L2D 公开提供。

---

### Log Probability Tracking of LLM APIs

- **Venue**: ICLR 2026 Poster
- **Authors**: Timothee Chauvin, Erwan Le Merrer, Francois Taiani, Gilles Tredan
- **Keywords**: API drift, audit, monitoring, LLM API, black-box
- **OpenReview**: https://openreview.net/forum?id=hFxivbAgVP
- **PDF**: https://openreview.net/pdf?id=hFxivbAgVP

**Abstract**

When using an LLM through an API provider, users expect the served model to remain consistent over time, a property crucial for the reliability of downstream applications and the reproducibility of research. Existing audit methods are too costly to apply at regular time intervals to the wide range of available LLM APIs. This means that model updates are left largely unmonitored in practice. In this work, we show that while LLM log probabilities (logprobs) are usually non-deterministic, they can still be used as the basis for cost-effective continuous monitoring of LLM APIs. We apply a simple statistical test based on the average value of each token logprob, requesting only a single token of output. This is enough to detect changes as small as one step of fine-tuning, making this approach more sensitive than existing methods while being 1,000x cheaper. We introduce the TinyChange benchmark as a way to measure the sensitivity of audit methods in the context of small, realistic model changes.

**Abstract (Chinese)**

通过 API 提供商使用大语言模型 (LLM) 时，用户期望提供的模型在时间上保持一致，这一特性对于下游应用的可靠性和研究的再现性至关重要。现有的审计方法成本过高，无法定期应用于广泛可用的 LLM API。这意味着在实践中，模型更新在很大程度上未被监控。在这项工作中，我们展示了虽然 LLM 的对数概率 (logprobs) 通常是非确定性的，但它们仍可作为 LLM API 成本有效的连续监控的基础。我们应用了一个简单的统计测试，该测试基于每个 token logprob 的平均值，仅请求一个 token 的输出。这足以检测到微调一步那么小的变化，使该方法比现有方法更敏感，同时成本低 1,000 倍。我们引入了 TinyChange 基准测试，作为衡量审计方法在小型、现实模型变化情境下敏感度的方法。

---

### Monitoring Decomposition Attacks with Lightweight Sequential Monitors

- **Venue**: ICLR 2026 Poster
- **Authors**: Chen Yueh-Han, Nitish Joshi, Yulin Chen, Maksym Andriushchenko, Rico Angell, He He
- **Keywords**: Monitoring, LLMs, AI Safety, Decomposition Attacks, Jailbreak, LLM Agents
- **OpenReview**: https://openreview.net/forum?id=HQuboWvFA1
- **PDF**: https://openreview.net/pdf?id=HQuboWvFA1

**Abstract**

As LLMs become more agentic, a critical risk emerges: attackers can \emph{decompose} harmful goals into stateful, benign subtasks that trick LLM agents into executing them without realizing the harmful intent in the same context. The challenge lies in the existing shallow safety alignment techniques: they only detect harm in the immediate prompt and do not reason about long-range intent. We therefore propose adding an external monitor that observes the conversation at a higher level. To facilitate our study on monitoring decomposition attacks, we curate the largest and most diverse dataset, DecomposedHarm, with 4,634 tasks that can be assigned to LLM agents, including general agent tasks, text-to-image, and question-answering tasks, where each task has a benignly decomposed version. We verify our datasets by testing them on frontier models and show an 87\% attack success rate on average on GPT-4o. To defend in real‐time, we propose a lightweight sequential monitoring framework that cumulatively evaluates each sub‑prompt. We show that a carefully prompt-engineered lightweight monitor hits a 93\% defense success rate—outperforming strong baselines such as Llama-Guard-4 and o3-mini, while cutting costs by 90\% and latency by 50\%. Additionally, we show that even under adversarial pressure, combining decomposition attacks with massive random task injection and automated red teaming, our lightweight sequential monitors remain robust. Our findings suggest that guarding against stateful decomposition attacks is "surprisingly easy" with lightweight sequential monitors, enabling safety in real-world LLM agent deployment where expensive solutions are impractical.

**Abstract (Chinese)**

随着大语言模型（LLMs）变得越来越具有代理能力，一个关键风险浮现：攻击者可以将有害目标\emph{分解}为有状态的、良性子任务，从而欺骗LLM代理在同一上下文中执行它们，而未意识到有害意图。挑战在于现有的浅层安全对齐技术：它们仅检测即时提示中的危害，而不推理长程意图。因此，我们提出添加一个外部监视器，从更高层面观察对话。为了便于对监控分解攻击的研究，我们构建了最大且最多样化的数据集DecomposedHarm，包含4,634个可分配给LLM代理的任务，包括通用代理任务、文本到图像任务和问答任务，其中每个任务均有良性分解版本。我们通过在前沿模型上测试验证了数据集，并在GPT-4o上实现了平均87%的攻击成功率。为了实时防御，我们提出一个轻量级顺序监控框架，对每个子提示进行累积评估。我们显示，一个精心提示工程化的轻量级监视器达到了93%的防御成功率——优于强大基线如Llama-Guard-4和o3-mini，同时将成本降低90%、延迟降低50%。此外，我们显示即使在对抗压力下，将分解攻击与大量随机任务注入及自动化红队测试结合，轻量级顺序监视器仍保持鲁棒性。我们的发现表明，使用轻量级顺序监视器防范有状态分解攻击是“出人意料地简单”的，这使得在昂贵解决方案不切实际的现实世界LLM代理部署中实现安全成为可能。

---

### On the Impossibility of Separating Intelligence from Judgment: The Computational Intractability of Filtering for AI Alignment

- **Venue**: ICLR 2026 Poster
- **Authors**: Sarah Ball, Grzegorz Gluch, Shafi Goldwasser, Frauke Kreuter, Omer Reingold, Guy N. Rothblum
- **Keywords**: alignment, safety, cryptography
- **OpenReview**: https://openreview.net/forum?id=CwoM9T55lG
- **PDF**: https://openreview.net/pdf?id=CwoM9T55lG

**Abstract**

With the increased deployment of large language models (LLMs), one concern is their potential misuse for generating harmful content. Our work studies the alignment challenge, with a focus on filters to prevent the generation of unsafe information. Two natural points of intervention are the filtering of the input prompt before it reaches the model, and filtering the output after generation. Our main results demonstrate computational challenges in filtering both prompts and outputs. First, we show that there exist LLMs for which there are no efficient input-prompt filters: adversarial prompts that elicit harmful behavior can be easily constructed, which are computationally indistinguishable from benign prompts for any efficient filter. Our second main result identifies a natural setting in which output filtering is computationally intractable. All of our separation results are under cryptographic hardness assumptions. In addition to these core findings, we also formalize and study relaxed mitigation approaches, demonstrating further computational barriers. We conclude that safety cannot be achieved by designing filters external to the LLM internals (architecture and weights); in particular, black-box access to the LLM will not suffice. Based on our technical results, we argue that an aligned AI system’s intelligence cannot be separated from its judgment.

**Abstract (Chinese)**

随着大型语言模型（LLMs）的部署日益增多，一个担忧是它们可能被滥用于生成有害内容。我们研究了对齐挑战，重点关注防止生成不安全信息的过滤器。两个自然的干预点是在提示到达模型之前过滤输入提示，以及生成后过滤输出。我们主要结果展示了过滤提示和输出的计算挑战。首先，我们证明存在这样的LLMs：不存在高效的输入提示过滤器；可以轻松构建引发有害行为的对抗性提示，这些提示对于任何高效过滤器而言，在计算上与良性提示不可区分。我们第二个主要结果识别了一个输出过滤计算上不可行的自然设置。我们所有的分离结果均基于密码学困难性假设。除了这些核心发现，我们还形式化并研究了放宽的缓解方法，展示了进一步的计算障碍。我们得出结论：安全无法通过设计外部于LLM内部（架构和权重）的过滤器来实现；特别是，黑盒访问LLM是不够的。基于我们的技术结果，我们论证了对齐AI系统的智能不能与其判断分离。

---

### Output Supervision Can Obfuscate the Chain of Thought

- **Venue**: ICLR 2026 Poster
- **Authors**: jacob drori, Luke Marks, Bryce Woodworth, Alex Cloud, Alexander Matt Turner
- **Keywords**: chain of thought, monitoring, CoT, supervision, monitor, obfuscation
- **OpenReview**: https://openreview.net/forum?id=JTX0iqxBjk
- **PDF**: https://openreview.net/pdf?id=JTX0iqxBjk

**Abstract**

Recently, OpenAI (2025) showed that training against a chain of thought (CoT) monitor can cause obfuscated CoTs, which contain bad behavior the monitor cannot detect. They proposed to keep CoTs monitorable by training only against output monitors that do not have access to CoT. We show that such training can still cause obfuscated CoTs via two mechanisms. First, when a model is trained to produce a safe-looking output, that model may generalize to making its CoTs look safe. Second, since later tokens are conditioned on earlier ones, safe‑looking CoTs may increase the likelihood of safe outputs, causing safe-looking CoTs to be reinforced. We introduce two mitigations to address these two issues, which achieve a Pareto improvement in terms of monitorability and task performance compared to regular training. To our knowledge, we are the first to identify and mitigate these problems. Our work implies that preserving CoT monitorability is more difficult than previously thought; we suggest practical guidelines for AI developers to maintain monitorable CoTs.

**Abstract (Chinese)**

最近，OpenAI (2025) 表明，对抗思维链 (CoT) 监视器进行训练可能导致伪装的 CoT，这些 CoT 包含监视器无法检测的坏行为。他们提出，通过仅对抗无权访问 CoT 的输出监视器进行训练来保持 CoT 的可监视性。我们证明，这种训练仍可能通过两种机制导致伪装的 CoT。首先，当模型被训练产生看似安全的输出时，该模型可能泛化到使其 CoT 看起来安全。其次，由于后来的 token 条件于前面的 token，看似安全的 CoT 可能增加安全输出的可能性，从而强化看似安全的 CoT。我们引入两种缓解措施来解决这两个问题，与常规训练相比，这些措施在监视性和任务性能方面实现了帕累托改进。据我们所知，我们是第一个识别并缓解这些问题的工作。我们的工作表明，保持 CoT 可监视性比先前认为的更困难；我们为 AI 开发者提出保持可监视 CoT 的实用指南。

---

### RESCUE: Retrieval Augmented Secure Code Generation

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiahao Shi, Tianyi Zhang
- **Keywords**: secure code generation, retrieval augmented generation
- **OpenReview**: https://openreview.net/forum?id=gbxhesw4UH
- **PDF**: https://openreview.net/pdf?id=gbxhesw4UH

**Abstract**

Despite recent advances, Large Language Models (LLMs) still generate vulnerable code. 
Retrieval-Augmented Generation (RAG) has the potential to enhance LLMs for secure code generation by incorporating external security knowledge.  
However, the conventional RAG design struggles with the noise of raw security-related documents, and existing retrieval methods overlook the significant security semantics implicitly embedded in task descriptions.
To address these issues, we propose \textsc{Rescue}, a new RAG framework for secure code generation with two key innovations. 
First, we propose a hybrid knowledge base construction method that combines LLM-assisted cluster-then-summarize distillation with program slicing, producing both high-level security guidelines and concise, security-focused code examples. Second, we design a hierarchical multi-faceted retrieval that traverses the constructed knowledge base from top to bottom and integrates multiple security-critical facts at each hierarchical level, ensuring comprehensive and accurate retrieval. 
We evaluated \textsc{Rescue} on four benchmarks and compared it with five state-of-the-art secure code generation methods on six LLMs. The results demonstrate that \textsc{Rescue} improves the SecurePass@1 metric by an average of 4.8 points, establishing a new state-of-the-art performance for security. Furthermore, we performed in-depth analysis and ablation studies to rigorously validate the effectiveness of individual components in \textsc{Rescue}. Our code is available at \url{https://github.com/steven1518/RESCUE}.

**Abstract (Chinese)**

尽管取得了最近的进展，大语言模型 (LLMs) 仍然会生成易受攻击的代码。  
检索增强生成 (RAG) 通过整合外部安全知识，有潜力提升 LLMs 在安全代码生成方面的性能。  
然而，传统的 RAG 设计难以应对原始安全相关文档中的噪声，现有的检索方法忽略了任务描述中隐含嵌入的重要安全语义。  
为解决这些问题，我们提出了 \textsc{Rescue}，一种用于安全代码生成的新型 RAG 框架，具有两大关键创新。  
首先，我们提出了一种混合知识库构建方法，该方法结合了 LLM 辅助的聚类-然后-总结蒸馏与程序切片，生成高级安全指南和简洁的、以安全为重点的代码示例。其次，我们设计了一种分层多方面检索，该检索从构建的知识库中从上到下遍历，并在每个分层级别整合多个安全关键事实，确保全面且准确的检索。  
我们在四个基准上评估了 \textsc{Rescue}，并将其与五种最先进的的安全代码生成方法在六个 LLMs 上进行了比较。  
结果表明，\textsc{Rescue} 将 SecurePass@1 指标平均提高了 4.8 个百分点，确立了安全方面的新的最先进性能。  
此外，我们进行了深入分析和消融研究，以严格验证 \textsc{Rescue} 中各个组件的有效性。我们的代码可在 https://github.com/steven1518/RESCUE 获取。

---

### Safety Instincts: LLMs Learn to Trust Their Internal Compass for Self-Defense

- **Venue**: ICLR 2026 Poster
- **Authors**: Guobin Shen, Dongcheng Zhao, Haibo Tong, Jindong Li, Feifei Zhao, Yi Zeng
- **Keywords**: Large Language Models, Jailbreak Defense, Self-Alignment, Intrinsic Safety
- **OpenReview**: https://openreview.net/forum?id=LUiqtv6vrd
- **PDF**: https://openreview.net/pdf?id=LUiqtv6vrd

**Abstract**

Ensuring Large Language Model (LLM) safety remains challenging due to the absence of universal standards and reliable content validators, making it difficult to obtain effective training signals. We discover that aligned models already possess robust internal safety beliefs: they consistently produce high-confidence refusals to harmful requests while exhibiting high entropy when generating potentially dangerous content. This entropy gap reveals an untapped signal—models intrinsically "know" when to refuse. We introduce Safety Instincts Reinforcement Learning (*SIRL*), which transforms this internal confidence into a self-generated reward signal, eliminating dependence on external validators or human annotations. *SIRL* teaches models to trust their safety instincts by reinforcing low-entropy refusal behaviors. Evaluated on Llama and Qwen models, *SIRL* maintains 89\%+ Defense Success Rates (DSRs) against 20+ jailbreak methods, from static prompts to automated attacks. Using only 15,000 unlabeled prompts, *SIRL* surpasses resource-intensive supervised methods while preserving performance on mathematics, coding, and conversation benchmarks. Our work demonstrates that effective alignment can emerge from within, paving the way for more autonomous and robust AI safety mechanisms that scale without extensive human oversight.

**Abstract (Chinese)**

确保大语言模型 (LLM) 的安全性仍然具有挑战性，因为缺乏通用标准和可靠的内容验证器，这使得获取有效的训练信号变得困难。我们发现，对齐模型已经具备强大的内部安全信念：它们对有害请求一致地产生高置信度的拒绝，同时在生成潜在危险内容时表现出高熵。这种熵差距揭示了一个未被利用的信号——模型本质上“知道”何时拒绝。我们引入了安全本能强化学习 (*SIRL*)，它将这种内部置信度转化为自生成的奖励信号，消除了对外部验证器或人工标注的依赖。*SIRL* 通过强化低熵拒绝行为来教导模型信任其安全本能。在 Llama 和 Qwen 模型上的评估显示，*SIRL* 对 20 多种越狱方法（从静态提示到自动化攻击）保持 89%+ 的防御成功率 (DSRs)。仅使用 15,000 个无标签提示，*SIRL* 超越了资源密集型的监督方法，同时在数学、编码和对话基准上保持性能。我们的工作证明，有效的对齐可以从内部涌现，为更自主、更鲁棒的 AI 安全机制铺平道路，这些机制可以在没有广泛人工监督的情况下扩展。

---

### Sysformer: Safeguarding Frozen Large Language Models with Adaptive System Prompts

- **Venue**: ICLR 2026 Poster
- **Authors**: Kartik Sharma, Yiqiao Jin, Vineeth Rakesh, Yingtong Dou, Menghai Pan, Mahashweta Das, Srijan Kumar
- **Keywords**: Large Language Models, AI Safety, Jailbreaks, Guardrails, Frozen Model adaptation
- **OpenReview**: https://openreview.net/forum?id=EbgCEd8gyN
- **PDF**: https://openreview.net/pdf?id=EbgCEd8gyN

**Abstract**

As large language models (LLMs) are deployed in safety-critical settings, it is essential to ensure that their responses comply with safety standards. Prior research has revealed that LLMs often fail to grasp the notion of safe behaviors, resulting in either unjustified refusals to harmless prompts or the generation of harmful content. While substantial efforts have been made to improve their robustness, existing defenses often rely on costly fine-tuning of model parameters or employ suboptimal heuristic techniques. In this work, we take a novel approach to safeguard LLMs by learning to adapt the system prompts in instruction-tuned LLMs. While LLMs are typically pre-trained to follow a fixed system prompt, we investigate the impact of tailoring the system prompt to each specific user input on the safety of the responses. To this end, we propose Sysformer, a transformer model that updates an initial system prompt to a more robust system prompt in the LLM input embedding space while attending to the user prompt. While keeping the LLM parameters frozen, the Sysformer is trained to refuse to respond to a set of harmful prompts while responding ideally to a set of safe ones. Through extensive experiments on 5 LLMs from different families and 2 recent benchmarks, we demonstrate that Sysformer can significantly enhance the robustness of LLMs, leading to upto 80% gain in the refusal rate on harmful prompts while enhancing the compliance with the safe prompts by upto 90%. Results also generalize well to sophisticated jailbreaking attacks, making LLMs upto 100% more robust against different attack strategies. We hope our findings lead to cheaper safeguarding of LLMs and motivate future investigations into designing variable system prompts.

**Abstract (Chinese)**

随着大语言模型（LLMs）被部署在安全关键场景中，确保其响应符合安全标准至关重要。先前研究表明，LLMs 往往无法把握安全行为的含义，导致对无害提示的不合理拒绝，或生成有害内容。尽管已做出大量努力来提升其鲁棒性，但现有防御方法通常依赖于昂贵的模型参数微调，或采用次优的启发式技术。本工作中，我们提出了一种新颖的方法，通过学习适应指令微调 LLMs 中的系统提示来防护 LLMs。虽然 LLMs 通常被预训练以遵循固定的系统提示，但我们探讨了针对每个特定用户输入定制系统提示对响应安全性的影响。为此，我们提出了 Sysformer，这是一个 Transformer 模型，它在 LLM 输入嵌入空间中将初始系统提示更新为更鲁棒的系统提示，同时关注用户提示。在保持 LLM 参数冻结的情况下，Sysformer 被训练为拒绝响应一组有害提示，同时理想响应一组安全提示。通过在来自不同家族的 5 个 LLMs 和 2 个最新基准上的广泛实验，我们证明 Sysformer 可以显著提升 LLMs 的鲁棒性，在有害提示上的拒绝率提升高达 80%，同时对安全提示的顺应性提升高达 90%。结果还对复杂的越狱攻击具有良好的泛化性，使 LLMs 对不同攻击策略的鲁棒性提升高达 100%。我们希望这些发现能够推动更低成本的 LLMs 防护，并激发未来对设计可变系统提示的研究。

---

### Trust The Typical

- **Venue**: ICLR 2026 Poster
- **Authors**: Debargha Ganguly, Sreehari Sankar, Biyao Zhang, Vikash Singh, Kanan Gupta, Harshini Kavuru, Alan Luo, Weicong Chen, Warren Richard Morningstar, Raghu Machiraju, Vipin Chaudhary
- **Keywords**: LLM Safety, Out-of-Distribution Detection, Jailbreaking, Representation Learning, Selective Generation, Anomaly Detection
- **OpenReview**: https://openreview.net/forum?id=vfbeleLBWv
- **PDF**: https://openreview.net/pdf?id=vfbeleLBWv

**Abstract**

Current approaches to LLM safety fundamentally rely on a brittle cat-and-mouse game of identifying and blocking known threats via guardrails. We argue for a fresh approach: robust safety comes not from enumerating what is harmful, but from \emph{deeply understanding what is safe}. We introduce \textbf{T}rust \textbf{T}he \textbf{T}ypical \textbf{(T3)}, a framework that operationalizes this principle by treating safety as an out-of-distribution (OOD) detection problem. T3 learns the distribution of acceptable prompts in a semantic space and flags any significant deviation as a potential threat. Unlike prior methods, it requires no training on harmful examples, yet achieves state-of-the-art performance across 18 benchmarks spanning toxicity, hate speech, jailbreaking, multilingual harms, and over-refusal, reducing false positive rates by up to 40x relative to specialized safety models. A single model trained only on safe English text transfers effectively to diverse domains and over 14 languages without retraining. Finally, we demonstrate production readiness by integrating a GPU-optimized version into vLLM, enabling continuous guardrailing during token generation with less than 6\% overhead even under dense evaluation intervals on large-scale workloads.

**Abstract (Chinese)**

当前的大语言模型（LLM）安全方法本质上依赖于通过护栏识别和阻挡已知威胁的脆弱猫捉老鼠游戏。我们主张一种新方法：稳健的安全并非来自于列举有害内容，而是来自于*深入理解什么是安全的*。我们引入了**信任典型（T3）**框架，该框架通过将安全视为分布外（OOD）检测问题来操作化这一原则。T3 在语义空间中学习可接受提示的分布，并将任何显著偏差标记为潜在威胁。与先前方法不同，它无需在有害示例上训练，却在涵盖毒性内容、仇恨言论、越狱、多语言危害和过度拒绝的18个基准上达到了最先进性能，相对于专用安全模型将假阳性率降低了高达40倍。仅在安全的英文文本上训练的单一模型无需重新训练即可有效转移到多样化领域和超过14种语言。最后，我们通过将GPU优化的版本集成到vLLM中展示了生产就绪性，即使在大规模工作负载下密集评估间隔，也能在令牌生成过程中实现连续护栏功能，额外开销不到6%。

---
