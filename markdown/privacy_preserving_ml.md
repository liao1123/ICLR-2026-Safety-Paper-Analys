# privacy_preserving_ml

**Description**: 隐私保护机器学习与隐私机制。包括 differential privacy、federated learning、secure aggregation、privacy auditing、redaction、access control、confidential computing 相关等。

**Paper count**: 39

---

### Differentially Private Domain Discovery

- **Venue**: ICLR 2026 Oral
- **Authors**: Vinod Raman, Travis Dick, Matthew Joseph
- **Keywords**: Differential Privacy, Partition Selection, Top-k Selection
- **OpenReview**: https://openreview.net/forum?id=yBpzF8hp3J
- **PDF**: https://openreview.net/pdf?id=yBpzF8hp3J

**Abstract**

We study several problems in differentially private domain discovery, where each user holds a subset of items from a shared but unknown domain, and the goal is to output an informative subset of items. For set union, we  show that the simple baseline Weighted Gaussian Mechanism (WGM) has a near-optimal $\ell_1$ missing mass guarantee on Zipfian data as well as a distribution-free $\ell_\infty$ missing mass guarantee. We then apply the WGM as a domain-discovery precursor for existing known-domain algorithms for private top-$k$ and $k$-hitting set and obtain new utility guarantees for their unknown domain variants. Finally, experiments demonstrate that all of our WGM-based methods are competitive with or outperform existing baselines for all three problems.

**Abstract (Chinese)**

我们研究了差分隐私域发现中的几个问题，其中每个用户持有来自共享但未知域的项子集，目标是输出一个信息丰富的项子集。对于集合并，我们证明了简单的基准加权高斯机制（WGM）在 Zipfian 数据上具有近最优的 $\ell_1$ 缺失质量保证，以及无分布假设的 $\ell_\infty$ 缺失质量保证。然后，我们将 WGM 作为现有已知域算法的域发现前置步骤，这些算法针对私有 top-$k$ 和 $k$-击中集，并为它们的未知域变体获得新的效用保证。最后，实验表明，我们的所有基于 WGM 的方法在所有三个问题上与现有基准相当或优于它们。

---

### PateGAIL++: Utility Optimized Private Trajectory Generation with Imitation Learning

- **Venue**: ICLR 2026 Oral
- **Authors**: Yingjie Ma, Bijal Bharadva, Xin Zhang, Joann Qiongna Chen
- **Keywords**: Differential Privacy, Imitation Learning
- **OpenReview**: https://openreview.net/forum?id=Oyfz6G0hmc
- **PDF**: https://openreview.net/pdf?id=Oyfz6G0hmc

**Abstract**

Human mobility trajectory data supports a wide range of applications, including urban planning, intelligent transportation systems, and public safety monitoring. However, large-scale, high-quality mobility datasets are difficult to obtain due to privacy concerns. Raw trajectory data may reveal sensitive user information, such as home addresses, routines, or social relationships, making it crucial to develop privacy-preserving alternatives.
Recent advances in deep generative modeling have enabled synthetic trajectory generation, but existing methods either lack formal privacy guarantees or suffer from reduced utility and scalability. Differential Privacy (DP) has emerged as a rigorous framework for data protection, and recent efforts such as PATE-GAN and \textsc{PateGail} integrate DP with generative adversarial learning. While promising, these methods struggle to generalize across diverse trajectory patterns and often incur significant utility degradation.
In this work, we propose a new framework that builds on \textsc{PateGail\texttt{++}} by introducing a \emph{sensitivity-aware noise injection module} that dynamically adjusts privacy noise based on sample-level sensitivity. This design significantly improves trajectory fidelity, downstream task performance, and scalability under strong privacy guarantees. We further adapt our framework to the local differential privacy (LDP) setting, allowing individual-level protection without reliance on a trusted server. We evaluate our method on a real-world mobility dataset and demonstrate its superiority over state-of-the-art baselines in terms of privacy-utility trade-off.

**Abstract (Chinese)**

人类移动轨迹数据支持广泛的应用，包括城市规划、智能交通系统以及公共安全监测。然而，由于隐私担忧，大规模、高质量的移动数据集难以获取。原始轨迹数据可能泄露敏感用户信息，例如家庭地址、日常习惯或社会关系，因此开发隐私保护替代方案至关重要。

深度生成建模的最新进展已实现合成轨迹生成，但现有方法要么缺乏正式隐私保证，要么在效用和可扩展性方面表现欠佳。差分隐私（DP）已成为数据保护的严谨框架，近期工作如 PATE-GAN 和 \textsc{PateGail} 将 DP 与生成对抗学习相结合。尽管前景可期，这些方法难以泛化到多样化的轨迹模式，且往往导致显著的效用下降。

在本工作中，我们提出了一种新框架，该框架基于 \textsc{PateGail\texttt{++}}，引入了\emph{敏感度感知噪声注入模块}，该模块根据样本级敏感度动态调整隐私噪声。这一设计在强隐私保证下显著提升了轨迹保真度、下游任务性能和可扩展性。我们进一步将该框架适配到局部差分隐私（LDP）设置中，实现了个体级保护而无需依赖可信服务器。我们在真实世界移动数据集上评估了该方法，并证明其在隐私-效用权衡方面优于最先进基线。

---

### Back to Square Roots: An Optimal Bound on the Matrix Factorization Error for Multi-Epoch Differentially Private SGD

- **Venue**: ICLR 2026 Poster
- **Authors**: Nikita Kalinin, Ryan McKenna, Jalaj Upadhyay, Christoph H. Lampert
- **Keywords**: Matrix Factorization, Differential Privacy, Machine Learning
- **OpenReview**: https://openreview.net/forum?id=EEr6cADbZx
- **PDF**: https://openreview.net/pdf?id=EEr6cADbZx

**Abstract**

Matrix factorization mechanisms for differentially private training have emerged as a promising approach to improve model utility under privacy constraints. In practical settings, models are typically trained over multiple epochs, requiring matrix factorizations that account for repeated participation. Existing theoretical upper and lower bounds on multi-epoch factorization error leave a significant gap. In this work, we introduce a new explicit factorization method, Banded Inverse Square Root (BISR), which imposes a banded structure on the inverse correlation matrix. This factorization enables us to derive an explicit and tight characterization of the multi-epoch error. We further prove that BISR achieves asymptotically optimal error by matching the upper and lower bounds. Empirically, BISR performs on par with the state of the art factorization methods, while being simpler to implement, computationally efficient, and easier to analyze.

**Abstract (Chinese)**

差分隐私训练的矩阵分解机制已成为在隐私约束下提升模型效用的有前景方法。在实际设置中，模型通常经过多个训练轮次训练，这需要考虑重复参与的矩阵分解。现有的多轮分解误差理论上界和下界之间存在显著差距。在本工作中，我们提出了一种新的显式分解方法——带状逆平方根（BISR），它在逆相关矩阵上施加带状结构。这种分解使我们能够推导出多轮误差的显式且紧致的刻画。我们进一步证明，BISR通过匹配上界和下界实现了渐近最优误差。在实证上，BISR的表现与最先进的分解方法相当，同时实现更简单、计算高效且更容易分析。

---

### Beyond Membership: Limitations of Add/Remove Adjacency in Differential Privacy

- **Venue**: ICLR 2026 Poster
- **Authors**: Gauri Pradhan, Joonas Jälkö, Santiago Zanella-Beguelin, Antti Honkela
- **Keywords**: differential privacy, deep learning, privacy auditing
- **OpenReview**: https://openreview.net/forum?id=C4jAhm8L1V
- **PDF**: https://openreview.net/pdf?id=C4jAhm8L1V

**Abstract**

Training machine learning models with differential privacy (DP) limits an adversary's ability to infer sensitive information about the training data. It can be interpreted as a bound on the adversary's capability to distinguish two adjacent datasets according to the chosen adjacency relation. In practice, most DP implementations use the add/remove adjacency relation, where two datasets are adjacent if one can be obtained from the other by adding or removing a single record, thereby protecting membership. In many ML applications, however, the goal is to protect attributes of individual records (e.g., labels used in supervised fine-tuning). We show that privacy accounting under add/remove overstates attribute privacy compared to accounting under the substitute adjacency relation, which permits substituting one record. To demonstrate this gap, we develop novel attacks to audit DP under substitute adjacency, and show empirically that audit results are inconsistent with DP guarantees reported under add/remove, yet remain consistent with the budget accounted under the substitute adjacency relation. Our results highlight that the choice of adjacency when reporting DP guarantees is critical when the protection target is per-record attributes rather than membership.

**Abstract (Chinese)**

使用差分隐私 (DP) 训练机器学习模型可以限制攻击者推断训练数据中敏感信息的可能性。它可以被解释为对攻击者根据所选邻接关系区分两个相邻数据集的能力的界限。在实践中，大多数 DP 实现采用添加/删除邻接关系，其中两个数据集相邻，如果一个可以通过向另一个添加或删除单个记录得到，从而保护成员身份。然而，在许多机器学习应用中，目标是保护单个记录的属性（例如，用于监督微调的标签）。我们证明，在添加/删除下的隐私核算相对于替换邻接关系下的核算，高估了属性隐私，后者允许替换一条记录。为了证明这一差距，我们开发了新型攻击来审计替换邻接关系下的 DP，并实证显示审计结果与添加/删除下报告的 DP 保证不一致，但与替换邻接关系下核算的预算一致。我们的结果强调，当保护目标是个体记录属性而非成员身份时，报告 DP 保证时的邻接关系选择至关重要。

---

### Concept-Aware Privacy Mechanisms for Defending Embedding Inversion Attacks

- **Venue**: ICLR 2026 Poster
- **Authors**: Yu-Che Tsai, Hsiang Hsiao, Kuan-Yu Chen, Shou-De Lin
- **Keywords**: Text Embedding, Privacy, Defense, Inversion Attack
- **OpenReview**: https://openreview.net/forum?id=bcOD0CLgBb
- **PDF**: https://openreview.net/pdf?id=bcOD0CLgBb

**Abstract**

Text embeddings enable numerous NLP applications but face severe privacy risks from embedding inversion attacks, which can expose sensitive attributes or reconstruct raw text. Existing differential privacy defenses assume uniform sensitivity across embedding dimensions, leading to excessive noise and degraded utility. We propose SPARSE, a user-centric framework for concept-specific privacy protection in text embeddings. SPARSE combines (1) differentiable mask learning to identify privacy-sensitive dimensions for user-defined concepts, and (2) the Mahalanobis mechanism that applies elliptical noise calibrated by dimension sensitivity. Unlike traditional spherical noise injection, SPARSE selectively perturbs privacy-sensitive dimensions while preserving non-sensitive semantics. Evaluated across six datasets with three embedding models and attack scenarios, SPARSE consistently reduces privacy leakage while achieving superior downstream performance compared to state-of-the-art DP methods.

**Abstract (Chinese)**

文本嵌入支持众多自然语言处理应用，但面临嵌入反演攻击带来的严重隐私风险，这些攻击可能暴露敏感属性或重构原始文本。现有的差分隐私防御机制假设嵌入维度具有均匀敏感性，从而导致过度噪声注入和效用下降。我们提出 SPARSE，这是一个以用户为中心的文本嵌入概念特定隐私保护框架。SPARSE 结合了 (1) 可微分掩码学习，用于识别用户定义概念的隐私敏感维度，以及 (2) 马氏机制，该机制根据维度敏感性施加椭圆噪声。与传统的球形噪声注入不同，SPARSE 选择性地扰动隐私敏感维度，同时保留非敏感语义。在六个数据集、三个嵌入模型和攻击场景的评估中，SPARSE 在持续减少隐私泄露的同时，实现了优于最先进差分隐私方法的下游性能。

---

### Convergent Differential Privacy Analysis for General Federated Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Yan Sun, Qixin Zhang, Li Shen, Dacheng Tao
- **Keywords**: Differential privacy, federated learning
- **OpenReview**: https://openreview.net/forum?id=7Zbe5ad3eX
- **PDF**: https://openreview.net/pdf?id=7Zbe5ad3eX

**Abstract**

The powerful cooperation of federated learning (FL) and differential privacy (DP) provides a promising paradigm for the large-scale private clients. However, existing analyses in FL-DP mostly rely on the composition theorem and cannot tightly quantify the privacy leakage challenges, which is tight for a few communication rounds but yields an arbitrarily loose and divergent bound eventually. This also implies a counterintuitive judgment, suggesting that FL-DP may not provide adequate privacy support during long-term training under constant-level noisy perturbations, yielding discrepancy between the theoretical and experimental results. To further investigate the convergent privacy and reliability of the FL-DP framework, in this paper, we comprehensively evaluate the worst privacy of two classical methods under the non-convex and smooth objectives based on the $f$-DP analysis. With the aid of the shifted interpolation technique, we successfully prove that privacy in Noisy-FedAvg has a tight convergent bound. Moreover, with the regularization of the proxy term, privacy in Noisy-FedProx has a stable constant lower bound. Our analysis further demonstrates a solid theoretical foundation for the reliability of privacy in FL-DP. Meanwhile, our conclusions can also be losslessly converted to other classical DP analytical frameworks, e.g. 
$(\epsilon,\delta)$-DP and R$\'{e}$nyi-DP (RDP), to provide more fine-grained understandings for the FL-DP frameworks.

**Abstract (Chinese)**

联邦学习 (FL) 与差分隐私 (DP) 的强大协同为大规模私有客户端提供了一个有前景的范式。然而，现有的 FL-DP 分析大多依赖于组合定理，无法紧致地量化隐私泄露挑战，该挑战在少数通信轮次中是紧致的，但最终会产生任意松弛且发散的界。这也暗示了一个反直觉的判断，即在恒定水平噪声扰动下的长期训练中，FL-DP 可能无法提供足够的隐私支持，从而导致理论与实验结果之间的差异。为了进一步探究 FL-DP 框架的收敛隐私性和可靠性，本文基于 $f$-DP 分析，全面评估了两种经典方法在非凸光滑目标下的最差隐私。借助移位插值技术，我们成功证明了 Noisy-FedAvg 中的隐私具有紧致的收敛界。此外，通过代理项的正则化，Noisy-FedProx 中的隐私具有稳定的常数下界。我们的分析进一步为 FL-DP 中隐私的可靠性提供了坚实的理论基础。同时，我们的结论也可以无损地转换为其他经典 DP 分析框架，例如 $(\epsilon,\delta)$-DP 和 Rényi-DP (RDP)，为 FL-DP 框架提供更细粒度的理解。

---

### Developmental Federated Tuning: A Cognitive-Inspired Paradigm for Efficient LLM Adaptation

- **Venue**: ICLR 2026 Poster
- **Authors**: Yebo Wu, Jingguang Li, Zhijiang Guo, Li Li
- **Keywords**: Federated Fine-Tuning, Large Language Models, Efficient Training
- **OpenReview**: https://openreview.net/forum?id=htbzmulSaG
- **PDF**: https://openreview.net/pdf?id=htbzmulSaG

**Abstract**

Federated fine-tuning enables Large Language Models (LLMs) to adapt to downstream tasks while preserving data privacy, but its resource-intensive nature severely limits deployment on edge devices. In this paper, we introduce Developmental Federated Tuning (DevFT), a resource-efficient approach inspired by cognitive development that progressively builds a powerful LLM from a compact foundation. DevFT decomposes the fine-tuning process into developmental stages, each optimizing a submodel with increasing parameter capacity. Knowledge acquired in earlier stages is transferred to subsequent submodels, providing optimized initialization parameters that prevent convergence to local minima and accelerate training. This paradigm mirrors human learning, gradually constructing a comprehensive knowledge structure while refining existing skills. To efficiently build stage-specific submodels, DevFT introduces deconfliction-guided layer grouping and differential-based layer fusion to distill essential information and construct representative layers. Evaluations across multiple benchmarks demonstrate that DevFT significantly outperforms state-of-the-art methods, achieving up to $\textbf{4.59$\times$}$ faster convergence, $\textbf{10.67$\times$}$ reduction in communication overhead, and $\textbf{9.07}$\% average performance improvement, while maintaining compatibility with existing federated fine-tuning approaches.

**Abstract (Chinese)**

联邦微调使大语言模型（LLMs）能够在保留数据隐私的同时适应下游任务，但其资源密集型特性严重限制了在边缘设备上的部署。本文提出发育式联邦调优（DevFT），这是一种受认知发展启发的资源高效方法，从紧凑的基础逐步构建强大的 LLM。DevFT 将微调过程分解为发育阶段，每个阶段优化一个参数容量逐渐增加的子模型。早期阶段获得的知识转移到后续子模型中，提供优化的初始化参数，从而防止收敛到局部最小值并加速训练。这一范式镜像人类学习，逐步构建全面的知识结构，同时精炼现有技能。为了高效构建特定阶段的子模型，DevFT 引入去冲突引导的层分组和基于差分的层融合，以提炼基本信息并构建代表性层。多基准测试表明，DevFT 显著优于最先进方法，实现了高达\textbf{4.59$\times$}的更快的收敛速度、\textbf{10.67$\times$}的通信开销降低，以及\textbf{9.07\%}的平均性能提升，同时保持与现有联邦微调方法的兼容性。

---

### Disrupting Hierarchical Reasoning: Adversarial Protection for Geographic Privacy in Multimodal Reasoning Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiaming Zhang, CHE WANG, Yang Cao, Longtao Huang, Wei Yang Bryan Lim
- **Keywords**: Adversarial Protection, Privacy Protection, Multi-Modal Large Language Models, Hierarchical Reasoning, Geographic Inference
- **OpenReview**: https://openreview.net/forum?id=5S6YTG9dL0
- **PDF**: https://openreview.net/pdf?id=5S6YTG9dL0

**Abstract**

Multi-modal large reasoning models (MLRMs) pose significant privacy risks by inferring precise geographic locations from personal images through hierarchical chain-of-thought reasoning. Existing privacy protection techniques, primarily designed for perception-based models, prove ineffective against MLRMs' sophisticated multi-step reasoning processes that analyze environmental cues. We introduce **ReasonBreak**, a novel adversarial framework specifically designed to disrupt hierarchical reasoning in MLRMs through concept-aware perturbations. Our approach is founded on the key insight that effective disruption of geographic reasoning requires perturbations aligned with conceptual hierarchies rather than uniform noise. ReasonBreak strategically targets critical conceptual dependencies within reasoning chains, generating perturbations that invalidate specific inference steps and cascade through subsequent reasoning stages. To facilitate this approach, we contribute **GeoPrivacy-6K**, a comprehensive dataset comprising 6,341 ultra-high-resolution images ($\geq$2K) with hierarchical concept annotations. Extensive evaluation across seven state-of-the-art MLRMs (including GPT-o3, GPT-5, Gemini 2.5 Pro) demonstrates ReasonBreak's superior effectiveness, achieving a 14.4\% improvement in tract-level protection (33.8\% vs 19.4\%) and nearly doubling block-level protection (33.5\% vs 16.8\%). This work establishes a new paradigm for privacy protection against reasoning-based threats.

**Abstract (Chinese)**

多模态大推理模型（MLRMs）通过分层思维链推理从个人图像中推断精确地理位置，从而带来显著的隐私风险。现有的隐私保护技术主要针对基于感知的模型设计，对 MLRMs 分析环境线索的复杂多步推理过程无效。我们引入 **ReasonBreak**，一种新型对抗框架，专为通过概念感知扰动破坏 MLRMs 中的分层推理而设计。我们的方法基于一个关键洞见：有效破坏地理推理需要与概念层次结构对齐的扰动，而不是均匀噪声。ReasonBreak 战略性地针对推理链中的关键概念依赖性，生成使特定推理步骤失效并级联到后续推理阶段的扰动。为了支持这一方法，我们贡献了 **GeoPrivacy-6K**，一个包含 6,341 张超高分辨率图像（≥2K）并带有分层概念标注的全面数据集。在七个最先进的 MLRMs（包括 GPT-o3、GPT-5、Gemini 2.5 Pro）上的广泛评估证明了 ReasonBreak 的优越有效性，在区级保护方面实现了 14.4\% 的提升（33.8\% vs 19.4\%），并几乎使街区级保护翻倍（33.5\% vs 16.8\%）。这项工作为针对基于推理的威胁的隐私保护建立了新范式。

---

### Exponential-Wrapped Mechanisms: Differential Privacy on Hadamard Manifolds Made Practical

- **Venue**: ICLR 2026 Poster
- **Authors**: Yangdi Jiang, Xiaotian Chang, Lei Ding, Linglong Kong, Bei Jiang
- **Keywords**: Differential Privacy, Riemannian Manifold, Hadamard manifolds, Fréchet mean, SPDM space
- **OpenReview**: https://openreview.net/forum?id=ulCVfMOo30
- **PDF**: https://openreview.net/pdf?id=ulCVfMOo30

**Abstract**

We propose a general and computationally efficient framework for achieving differential privacy (DP) on Hadamard manifolds, which are complete and simply connected Riemannian manifolds with non-positive curvature. Leveraging the Cartan-Hadamard theorem, we introduce Exponential-Wrapped Laplace and Gaussian mechanisms that achieve $\epsilon$-DP, $(\epsilon, \delta)$-DP, Gaussian DP (GDP), and Rényi DP (RDP) without relying on computationally intensive MCMC sampling. Our methods operate entirely within the intrinsic geometry of the manifold, ensuring both theoretical soundness and practical scalability. We derive utility bounds for privatized Fréchet means and demonstrate superior utility and runtime performances on both synthetic data and real-world data in the space of symmetric positive definite matrices (SPDM) equipped with three different metrics. To our knowledge, this work constitutes the first unified extension of multiple DP notions to general Hadamard manifolds with practical and scalable implementations.

**Abstract (Chinese)**

我们提出了一种通用的且计算高效的框架，用于在Hadamard流形上实现差分隐私（DP），Hadamard流形是完备的、单连通的非正曲率黎曼流形。利用Cartan-Hadamard定理，我们引入了指数包裹拉普拉斯和高斯机制，这些机制实现了$\epsilon$-DP、$(\epsilon, \delta)$-DP、高斯差分隐私（GDP）和Rényi差分隐私（RDP），而无需依赖计算密集型的MCMC采样。我们的方法完全在流形的本征几何中运行，确保了理论严谨性和实际可扩展性。我们推导了私有化Fréchet均值的效用界，并在配备三种不同度规的对称正定矩阵（SPDM）空间的合成数据和真实世界数据上展示了优越的效用和运行时性能。据我们所知，本工作构成了第一个将多种DP概念统一扩展到一般Hadamard流形的实用且可扩展实现。

---

### FHE-Coder: Benchmarking Secure Agentic Code Generation for Fully Homomorphic Encryption

- **Venue**: ICLR 2026 Poster
- **Authors**: Mayank Kumar, Jiaqi Xue, Mengxin Zheng, Qian Lou
- **Keywords**: Large Language Models, Agents, Code generation, Fully Homomorphic Encryption, Retrieval Augmented Generation
- **OpenReview**: https://openreview.net/forum?id=4F1py5vQXm
- **PDF**: https://openreview.net/pdf?id=4F1py5vQXm

**Abstract**

Fully Homomorphic Encryption (FHE) is a foundational technology for confidential computing, yet its practical adoption remains limited by the need for specialized cryptographic expertise and error-prone parameter configuration. To lower this barrier, we investigate whether Large Language Model (LLM) agents can reliably generate secure FHE code from natural-language specifications. We present FHE-Coder, a three-phase agentic framework that addresses the key failure modes of FHE code generation: semantic ambiguity, API misuse, and cryptographic insecurity. The framework integrates (1) a Prompt Formalizer that structures user intent and enforces secure parameterization, (2) a specialized retrieval-augmented generation (RAG) module that supplies scheme-specific API and documentation knowledge, and (3) an automated Security Verifier that performs iterative validation and feedback to detect and correct cryptographic flaws. We evaluate FHE-Coder across four leading LLMs on a benchmark of ten FHE programming tasks spanning increasing functional and security complexity. While baseline agents frequently produce code that compiles and passes functional tests, they often violate security constraints or misuse cryptographic parameters. In contrast, FHE-Coder consistently generates solutions that are compilable, functionally correct, and verifiably secure across schemes including TFHE and CKKS. Our work establishes a systematic methodology and benchmark for agentic FHE code generation, providing a practical step toward democratizing secure computation without compromising cryptographic guarantees.

**Abstract (Chinese)**

全同态加密 (FHE) 是保密计算的基础技术，然而，其实际应用仍受限于对专业密码学知识的需求以及易出错的参数配置。为了降低这一障碍，我们探讨了大语言模型 (LLM) 代理是否能够从自然语言规范可靠地生成安全的 FHE 代码。我们提出了 FHE-Coder，这是一个三阶段代理框架，用于解决 FHE 代码生成的关键失败模式：语义歧义、API 误用以及密码学不安全性。该框架集成了 (1) 提示形式化器，用于结构化用户意图并强制执行安全的参数化，(2) 专用的检索增强生成 (RAG) 模块，提供方案特定的 API 和文档知识，以及 (3) 自动化安全验证器，通过迭代验证和反馈来检测和修正密码学缺陷。我们在四个领先的 LLM 上评估了 FHE-Coder，使用了一个包含十个 FHE 编程任务的基准，这些任务涵盖了不断增加的功能和安全复杂性。虽然基线代理经常生成可编译并通过功能测试的代码，但它们常常违反安全约束或误用密码学参数。相比之下，FHE-Coder 始终生成可编译、功能正确且可验证安全的解决方案，适用于包括 TFHE 和 CKKS 在内的多种方案。我们的工作为代理式 FHE 代码生成建立了系统方法论和基准，为在不损害密码学保证的情况下实现安全计算的民主化提供了实际一步。

---

### Fed-Duet: Dual Expert-Orchestrated Framework for Continual Federated Vision-Language Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Tao GUO, Junwei Chen, Laizhong Cui
- **Keywords**: Federated Learning, Federated Continual Learning, Prompt learning, Vision-Language model
- **OpenReview**: https://openreview.net/forum?id=Jk8g1OxyZY
- **PDF**: https://openreview.net/pdf?id=Jk8g1OxyZY

**Abstract**

Pretrained vision-language models (VLMs), such as CLIP, have shown promise in federated learning (FL) by bringing strong multimodal representations to edge devices. However, continual adaptation remains a core challenge in practical federated settings, where task distributions evolve over time and data remain non-IID across clients. In this emerging area, recent works adopt parameter-efficient fine-tuning (PEFT) as a lightweight way to reduce communication overhead, yet they fail to preserve satisfactory performance under continual learning conditions. Meanwhile, traditional federated continual learning (FCL) methods lack the capacity to maintain cross-modal alignment crucial to VLM performance. We introduce Fed-Duet, a novel Dual Expert-orchestrated framework for efficient federated continual learning in vision-language models. Fed-Duet features a dual-expert adaptation mechanism, combining server-coordinated semantic prompts with client-personalized modular adapters. These pathways are dynamically fused via a cross-attention mechanism, enabling effective knowledge transfer while preserving multimodal alignment and mitigating forgetting. We evaluate Fed-Duet across multiple challenging continual learning tasks in federated vision-language settings and demonstrate that it achieves superior performance and stability compared to existing approaches. Our work highlights the importance of coordinated expert composition in enabling scalable and robust multimodal continual learning. The code is available at https://github.com/cocogt96/Fed-Duet.

**Abstract (Chinese)**

预训练视觉-语言模型（VLMs），如CLIP，在联邦学习（FL）中展现出潜力，通过将强大的多模态表示带到边缘设备。然而，在实际联邦设置中，持续适应仍是一个核心挑战，其中任务分布随时间演变，且数据在客户端间保持非IID。在这一新兴领域，最近工作采用参数高效微调（PEFT）作为一种轻量级方式来减少通信开销，但它们无法在持续学习条件下保持满意性能。同时，传统的联邦持续学习（FCL）方法缺乏维持VLM性能至关重要的跨模态对齐能力。我们引入Fed-Duet，这是一种新型的双专家协调框架，用于视觉-语言模型中的高效联邦持续学习。Fed-Duet采用双专家适应机制，结合服务器协调的语义提示与客户端个性化的模块化适配器。这些路径通过跨注意力机制动态融合，从而实现有效的知识转移，同时保持多模态对齐并缓解遗忘。我们在联邦视觉-语言设置中的多个具有挑战性的持续学习任务上评估Fed-Duet，并证明其比现有方法实现了优越的性能和稳定性。我们的工作突出了协调专家组合在实现可扩展且鲁棒的多模态持续学习中的重要性。代码可在https://github.com/cocogt96/Fed-Duet获取。

---

### FedMC: Federated Manifold Calibration

- **Venue**: ICLR 2026 Poster
- **Authors**: Yanbiao Ma, Wei Dai, Gaoyang Jiang, wanyi Chen, Chenyue Zhou, Yiwei Zhang, Fei Luo, Junhao Wang, Andi Zhang
- **Keywords**: Federated Learning, Distribution Calibrations, Geometric Knowledge
- **OpenReview**: https://openreview.net/forum?id=rxwwncarWj
- **PDF**: https://openreview.net/pdf?id=rxwwncarWj

**Abstract**

Data heterogeneity in Federated Learning (FL) leads to significant bias in local training. While recent efforts to introduce distributional statistics as priors have shown progress, they universally rely on a flawed global linearity assumption, failing to capture the nonlinear manifold structures prevalent in real-world data. This model-reality mismatch causes the calibration process to generate out-of-distribution (OOD) samples, which fundamentally misleads the model. To address this, we introduce a paradigm shift. We propose Federated Manifold Calibration (FedMC), a novel framework that learns and leverages the local, nonlinear geometry of data. FedMC employs local kernel PCA on the client side to learn fine-grained local geometries, and constructs a global "geometry dictionary" on the server side to aggregate and distribute this knowledge. Clients then utilize this dictionary to perform context-aware, on-manifold calibration. We validate our proposed method by integrating it with a wide range of existing FL algorithms. Experimental results show that by explicitly modeling nonlinear manifolds, FedMC consistently and significantly enhances the performance of these state-of-the-art methods across multiple benchmarks.

**Abstract (Chinese)**

联邦学习 (FL) 中的数据异质性会导致本地训练出现显著偏差。虽然最近将分布统计作为先验的努力取得了进展，但它们普遍依赖于有缺陷的全局线性假设，无法捕捉真实世界数据中普遍存在的非线性流形结构。这种模型与现实的错配会导致校准过程生成分布外 (OOD) 样本，从而从根本上误导模型。为解决这一问题，我们引入了一种范式转变。我们提出了联邦流形校准 (FedMC)，这是一个学习并利用数据局部非线性几何的新型框架。FedMC 在客户端侧采用本地核主成分分析来学习细粒度本地几何，并在服务器侧构建全局“几何字典”来聚合并分发这一知识。然后，客户端利用该字典执行上下文感知的、在线流形校准。我们通过将其与广泛的现有 FL 算法集成来验证所提出方法。实验结果表明，通过显式建模非线性流形，FedMC 在多个基准测试上持续且显著提升了这些最先进方法的性能。

---

### Federated Learning of Quantile Inference under Local Differential Privacy

- **Venue**: ICLR 2026 Poster
- **Authors**: Leheng Cai, Qirui Hu, Shuyuan Wu
- **Keywords**: Confidence interval; Federated learning; Local differential privacy; Quantile; Self-normalization
- **OpenReview**: https://openreview.net/forum?id=a5bFKVtTyF
- **PDF**: https://openreview.net/pdf?id=a5bFKVtTyF

**Abstract**

In this paper, we investigate federated learning for quantile inference under local differential privacy (LDP). We propose an estimator based on local stochastic gradient descent (SGD), whose local gradients are perturbed via a randomized mechanism with global parameters, making the procedure tolerant of communication and storage constraints without compromising statistical efficiency. Although the quantile loss and its corresponding gradient do not satisfy standard smoothness conditions typically assumed in existing literature, we establish asymptotic normality for our estimator as well as a functional central limit theorem. The proposed method accommodates data heterogeneity and allows each server to operate with an individual privacy budget. Furthermore, we construct confidence intervals for the target value through a self‐normalization approach, thereby circumventing the need to estimate additional nuisance parameters. Extensive numerical experiments and real data application validate the theoretical guarantees of the proposed methodology.

**Abstract (Chinese)**

本文研究了局部差分隐私 (LDP) 下分位数推断的联邦学习。我们提出了一种基于局部随机梯度下降 (SGD) 的估计量，其局部梯度通过具有全局参数的随机化机制进行扰动，从而使该过程能够容忍通信和存储约束，同时不损害统计效率。尽管分位数损失及其对应梯度不满足现有文献中通常假设的标准平滑性条件，我们仍为我们的估计量建立了渐近正态性和函数中心极限定理。所提方法适应数据异质性，并允许每个服务器使用独立的隐私预算运行。此外，我们通过自归一化方法为目标值构建置信区间，从而避免了估计额外扰动参数的需要。大量数值实验和真实数据应用验证了所提方法的理论保证。

---

### Federated Learning with Profile Mapping under Distribution Shifts and Drifts

- **Venue**: ICLR 2026 Poster
- **Authors**: Mohan Li, Dario Fenoglio, Martin Gjoreski, Marc Langheinrich
- **Keywords**: federated learning, privacy, distribution drifts, distribution shifts, data heterogeneity, efficiency
- **OpenReview**: https://openreview.net/forum?id=thoPskdIcE
- **PDF**: https://openreview.net/pdf?id=thoPskdIcE

**Abstract**

Federated Learning (FL) enables decentralized model training across clients without sharing raw data, but its performance degrades under real-world data heterogeneity. Existing methods often fail to address distribution shift across clients and distribution drift over time, or they rely on unrealistic assumptions such as known number of client clusters and data heterogeneity types, which limits their generalizability.   We introduce **Feroma**, a novel FL framework that explicitly handles both distribution shift and drift without relying on client or cluster identity. **Feroma** builds on client distribution profiles—compact, privacy-preserving representations of local data—that guide model aggregation and test-time model assignment through adaptive similarity-based weighting. This design allows **Feroma** to dynamically select aggregation strategies during training, ranging from clustered to personalized, and deploy suitable models to unseen, and unlabeled test clients without retraining, online adaptation, or prior knowledge on clients' data. Extensive experiments show that compared to 10 state-of-the-art methods, **Feroma** improves performance and stability under dynamic data heterogeneity conditions—an average accuracy gain of up to 12 percentage points over the best baselines across 6 benchmarks—while maintaining computational and communication overhead comparable to FedAvg. These results highlight that distribution-profile-based aggregation offers a practical path toward robust FL under both data distribution shifts and drifts.

**Abstract (Chinese)**

联邦学习 (FL) 能够在不共享原始数据的情况下实现跨客户端的去中心化模型训练，但其在真实世界数据异质性下的性能会下降。现有的方法往往无法处理跨客户端的分布偏移和随时间变化的分布漂移，或者依赖于不现实的假设，如已知的客户端簇数量和数据异质性类型，这限制了它们的泛化能力。我们引入了 **Feroma**，这是一个新颖的 FL 框架，它明确处理分布偏移和漂移，而不依赖于客户端或簇身份。**Feroma** 基于客户端分布剖面——本地数据的紧凑、隐私保护表示——通过自适应基于相似性的加权来指导模型聚合和测试时模型分配。这种设计允许 **Feroma** 在训练过程中动态选择聚合策略，从聚类到个性化，并向未见且无标签的测试客户端部署合适的模型，而无需重新训练、在线适应或事先了解客户端数据。广泛的实验表明，与 10 种最先进的方法相比，**Feroma** 在动态数据异质性条件下提高了性能和稳定性——在 6 个基准测试上平均准确率提升高达 12 个百分点，超过最佳基线——同时保持与 FedAvg 相当的计算和通信开销。这些结果突显了基于分布剖面的聚合为在数据分布偏移和漂移下实现鲁棒 FL 提供了一条实用路径。

---

### Heterogeneous Federated Fine-Tuning with Parallel One-Rank Adaptation

- **Venue**: ICLR 2026 Poster
- **Authors**: Zikai Zhang, Rui Hu, Jiahao Xu
- **Keywords**: Federated Learning, Low-Rank Adaptation, Large Language Models, Resource Heterogeneity
- **OpenReview**: https://openreview.net/forum?id=sXPaVl9KU6
- **PDF**: https://openreview.net/pdf?id=sXPaVl9KU6

**Abstract**

Large Language Models (LLMs) have demonstrated remarkable effectiveness in adapting to downstream tasks through fine-tuning. Federated Learning (FL) extends this capability by enabling collaborative fine-tuning across distributed clients using Low-Rank Adaptation (LoRA), while preserving data privacy by avoiding raw data sharing. However, practical deployments face challenges when clients have heterogeneous resources and thus adopt different LoRA ranks, leading to substantial initialization and aggregation noise that undermines performance. To address these challenges, we propose Fed-PLoRA, a novel lightweight heterogeneous federated fine-tuning (FFT) framework. Fed-PLoRA introduces Parallel One-Rank Adaptation (PLoRA), a new LoRA variant that replaces the classic multi-rank LoRA module with multiple parallel one-rank modules, and a novel Select-N-Fold strategy that folds untrained PLoRA modules into the pre-trained weights before local training, thereby accommodating heterogeneous client resources. We provide a unified analysis of initialization and aggregation noise of Fed-PLoRA and demonstrate how it addresses the limitations of state-of-the-art methods. Extensive experiments on diverse LLM fine-tuning tasks demonstrate that Fed-PLoRA consistently outperforms existing methods in both accuracy and efficiency. The code is available at \url{https://github.com/TNI-playground/Fed-PLoRA}.

**Abstract (Chinese)**

大语言模型 (LLMs) 通过微调在适应下游任务方面展现出显著的有效性。联邦学习 (FL) 通过使用低秩适应 (LoRA) 在分布式客户端间实现协作微调，从而扩展了这一能力，同时通过避免原始数据共享来保护数据隐私。然而，在实际部署中，当客户端具有异构资源并因此采用不同的 LoRA 秩时，会面临挑战，导致大量的初始化和聚合噪声，从而削弱性能。为应对这些挑战，我们提出 Fed-PLoRA，这是一种新型轻量级异构联邦微调 (FFT) 框架。Fed-PLoRA 引入了并行单秩适应 (PLoRA)，这是一种新的 LoRA 变体，它用多个并行单秩模块替换经典的多秩 LoRA 模块，以及一种新型的 Select-N-Fold 策略，该策略在本地训练前将未训练的 PLoRA 模块折叠到预训练权重中，从而适应异构客户端资源。我们提供了 Fed-PLoRA 初始化和聚合噪声的统一分析，并展示了它如何解决最先进方法的局限性。在多样化的 LLM 微调任务上的广泛实验表明，Fed-PLoRA 在准确性和效率方面始终优于现有方法。代码可在 https://github.com/TNI-playground/Fed-PLoRA 获取。

---

### HiddenEcho: Mitigating Noise Amplification in Differentially Private LLMs with Hidden-State Correction

- **Venue**: ICLR 2026 Poster
- **Authors**: Wenhao Li, Kunhao Li, Lei Yang
- **Keywords**: LLM, Privacy Preservation, Denoise
- **OpenReview**: https://openreview.net/forum?id=ER9BElK8He
- **PDF**: https://openreview.net/pdf?id=ER9BElK8He

**Abstract**

The rise of large language models (LLMs) has driven the adoption of Model-as-a-Service (MaaS). However, transmitting raw text to servers raises critical privacy concerns. Existing approaches employ deep neural networks (DNNs) or differential privacy (DP) to perturb inputs. Yet, these approaches suffer notable limitations: DNN-based methods often require task-specific pre-training, and conventional DP techniques, though privacy-preserving, suffer from noise amplification as perturbed inputs propagate through the deep transformer layer, leading to significant degradation in downstream task performance. To alleviate this, we propose HIDDENECHO, an end-to-end framework with client noise correction, where hidden states are sent from the server to the client and refined by a lightweight module using both embeddings and intermediate representations. HIDDENECHO suppresses inter-layer noise amplification without pretraining, effectively preserving task-relevant signals under DP constraints. To further reduce communication, HIDDENECHO incorporates gradient-based hidden layer selection and information bottleneck compression, reducing communication cost while preserving essential task information. Experiments across text classification and generation tasks demonstrate that HIDDENECHO achieves up to 46.89\% performance improvement over DP baselines, over 85\% communication reduction, and up to 72.52\% faster training compared to existing denoising approaches, establishing a new privacy-utility trade-off for privatized LLMs. Codes are available at https://github.com/liwh011/hidden-echo.

**Abstract (Chinese)**

大型语言模型 (LLMs) 的兴起推动了模型即服务 (MaaS) 的采用。然而，将原始文本传输到服务器会引发严重的隐私担忧。现有的方法采用深度神经网络 (DNNs) 或差分隐私 (DP) 来扰动输入。然而，这些方法存在显著局限性：基于 DNN 的方法通常需要特定任务的预训练，而传统的 DP 技术虽然具有隐私保护性，但由于扰动输入在深度 Transformer 层中传播时噪声放大，导致下游任务性能显著下降。为缓解这一问题，我们提出了 HIDDENECHO，这是一个端到端的框架，具有客户端噪声校正功能，其中隐藏状态从服务器发送到客户端，并由一个轻量级模块使用嵌入和中间表示进行精炼。HIDDENECHO 在无需预训练的情况下抑制层间噪声放大，有效地在 DP 约束下保留任务相关信号。为了进一步减少通信量，HIDDENECHO 集成了基于梯度的隐藏层选择和信息瓶颈压缩，从而在保留基本任务信息的同时降低通信成本。在文本分类和生成任务上的实验表明，HIDDENECHO 相对于 DP 基线实现了高达 46.89\% 的性能提升、超过 85\% 的通信量减少，以及相对于现有去噪方法高达 72.52\% 的训练加速，从而为私有化 LLMs 建立了新的隐私-效用权衡。代码可在 https://github.com/liwh011/hidden-echo 获取。

---

### Hot PATE: Private Aggregation of Distributions  for Diverse Tasks

- **Venue**: ICLR 2026 Poster
- **Authors**: Edith Cohen, Benjamin Cohen-Wang, Xin Lyu, Jelani Nelson, Tamas Sarlos, Uri Stemmer
- **Keywords**: Differential Privacy, Sequential Text Generation, Coordinated Ensembles
- **OpenReview**: https://openreview.net/forum?id=y8dVmQxKgb
- **PDF**: https://openreview.net/pdf?id=y8dVmQxKgb

**Abstract**

The Private Aggregation of Teacher Ensembles (PATE) framework enables privacy-preserving machine learning by aggregating responses from disjoint subsets of sensitive data. Adaptations of PATE to tasks with inherent output diversity such as text generation, where the desired output is a sample from a distribution, face a core tension: 
as diversity increases, samples from different teachers are less likely to agree, but lower agreement results in reduced utility for the same privacy requirements.  Yet suppressing diversity to artificially increase agreement is undesirable, as it distorts the output of the underlying model, and thus reduces output quality.
 
We propose Hot PATE, a variant of PATE designed for diverse generative settings. 
We formalize the notion of a *diversity-preserving*  *ensemble sampler* and introduce an efficient sampler that provably transfers diversity without incurring additional privacy cost.
Hot PATE requires only API access to proprietary models and can be used as a drop-in replacement for existing *Cold* PATE samplers. 
Our empirical evaluations corroborate and quantify the benefits, showing significant improvements in the privacy–utility trade-off on evaluated in-context learning tasks, both in preserving diversity and in returning relevant responses.

**Abstract (Chinese)**

私有教师集成聚合（PATE）框架通过聚合来自敏感数据互斥子集的响应，实现隐私保护机器学习。将PATE适应于具有固有输出多样性的任务（如文本生成，其中期望输出为分布采样）时，会面临一个核心张力：随着多样性增加，不同教师的采样更难达成一致，而较低的一致性会导致在相同隐私要求下效用降低。然而，人为抑制多样性以提升一致性是不可取的，因为这会扭曲底层模型的输出，从而降低输出质量。

我们提出Hot PATE，这是PATE的一种变体，专为多样性生成设置设计。我们形式化了*多样性保持* *集成采样器*的概念，并引入一种高效采样器，该采样器被证明能在不产生额外隐私成本的情况下转移多样性。Hot PATE仅需专有模型的API访问，即可作为现有*Cold* PATE采样器的即插即用替换方案。我们的实证评估证实并量化了其益处，在评估的上下文学习任务上显示出隐私–效用权衡的显著改善，既在保持多样性方面，也在返回相关响应方面。

---

### INO-SGD: Addressing Utility Imbalance under Individualized Differential Privacy

- **Venue**: ICLR 2026 Poster
- **Authors**: Xiao Tian, Jue Fan, Rachael Hwee Ling Sim, Bryan Kian Hsiang Low
- **Keywords**: differential privacy, individualized differential privacy, IDP-SGD, data imbalance, utility imbalance, accuracy disparity, collaborative machine learning
- **OpenReview**: https://openreview.net/forum?id=HMapYMkcrl
- **PDF**: https://openreview.net/pdf?id=HMapYMkcrl

**Abstract**

Differential privacy (DP) is widely employed in machine learning to protect confidential or sensitive training data from being revealed. As data owners gain greater control over their data due to personal data ownership, they are more likely to set their own privacy requirements, necessitating individualized DP (IDP) to fulfil such requests. In particular, owners of data from more sensitive subsets, such as positive cases of stigmatized diseases, likely set stronger privacy requirements, as leakage of such data could incur more serious societal impact. However, existing IDP algorithms induce a critical utility imbalance problem: Data from owners with stronger privacy requirements may be severely underrepresented in the trained model, resulting in poorer performance on similar data from subsequent users during deployment. In this paper, we analyze this problem and propose the INO-SGD algorithm, which strategically down-weights data within each batch to improve performance on the more private data across all iterations. Notably, our algorithm is specially designed to satisfy IDP, while existing techniques addressing utility imbalance neither satisfy IDP nor can be easily adapted to do so. Lastly, we demonstrate the empirical feasibility of our approach.

**Abstract (Chinese)**

差分隐私 (DP) 在机器学习中被广泛用于保护机密或敏感训练数据不被泄露。随着数据所有者由于个人数据所有权而获得对其数据的更大控制权，他们更有可能设定自己的隐私要求，这需要个性化差分隐私 (IDP) 来满足此类请求。特别是，来自更敏感子集的数据所有者，例如污名化疾病的阳性病例，很可能设定更强的隐私要求，因为此类数据的泄露可能造成更严重的社群影响。然而，现有的 IDP 算法引发了一个关键的效用不平衡问题：来自隐私要求更强所有者的数据在训练模型中可能被严重低估，导致部署期间对后续用户类似数据的性能较差。在本文中，我们分析了这个问题，并提出了 INO-SGD 算法，该算法战略性地降低每个批次中数据的权重，以改善所有迭代中对更隐私数据性能。值得注意的是，我们的算法专门设计用于满足 IDP，而现有的解决效用不平衡的技术既不满足 IDP，也无法轻易适应以满足 IDP。最后，我们展示了我们方法的实证可行性。

---

### Learnability and Privacy Vulnerability are Entangled in a Few Critical Weights

- **Venue**: ICLR 2026 Poster
- **Authors**: Xingli Fang, Jung-Eun Kim
- **Keywords**: Privacy, Generalizability, Weights Rewinding, Fine-Tuning
- **OpenReview**: https://openreview.net/forum?id=J2gI585XDK
- **PDF**: https://openreview.net/pdf?id=J2gI585XDK

**Abstract**

Prior approaches for membership privacy preservation usually update or retrain all weights in neural networks, which is costly and can lead to unnecessary utility loss or even more serious misalignment in predictions between training data and non-training data. In this paper, we empirically show that only a very small number of weights are liable to membership privacy vulnerability. However, we also identify that those neurons are not only liable to membership privacy breach but also contribute to generalizability. According to these insights, to preserve privacy, instead of discarding those neurons, we rewind only the weights for fine-tuning. We show that through extensive experiments, this mechanism, plugged into other approaches, shows enhanced resilience against Membership Inference Attacks while maintaining utility.

**Abstract (Chinese)**

以往的成员隐私保护方法通常更新或重新训练神经网络中的所有权重，这代价高昂，并可能导致不必要的效用损失，甚至在训练数据与非训练数据之间的预测出现更严重的偏差。本文通过实证研究表明，只有极少数权重易受成员隐私漏洞影响。然而，我们还发现，这些神经元不仅易受成员隐私泄露，而且有助于泛化能力。根据这些洞见，为保护隐私，我们不是丢弃这些神经元，而是仅回退用于微调的权重。我们通过广泛实验表明，该机制插入其他方法中，能在保持效用的同时，对成员推断攻击表现出增强的抵抗力。

---

### MOAI: Module-Optimizing Architecture for Non-Interactive Secure Transformer Inference

- **Venue**: ICLR 2026 Poster
- **Authors**: Linru Zhang, Xiangning Wang, Jun Jie Sim, Zhicong Huang, Jiahao Zhong, HUAXIONG WANG, Pu Duan, Kwok-Yan Lam
- **Keywords**: fully homomorphic encryption, secure transformer inference
- **OpenReview**: https://openreview.net/forum?id=qJn4HtTzhH
- **PDF**: https://openreview.net/pdf?id=qJn4HtTzhH

**Abstract**

Privacy concerns have been raised in Large Language Models (LLM) inference when models are deployed in Cloud Service Providers (CSP). Homomorphic encryption (HE) offers a promising solution by enabling secure inference directly over encrypted inputs. However, the high computational overhead of HE remains a major bottleneck. To address this challenge, we propose MOAI, an efficient HE-based, non-interactive framework for secure transformer inference. MOAI gains significant efficiency improvement from:  (1) a novel evaluation flow that combines column and diagonal packing with consistent strategies across all layers, eliminating expensive format conversions. (2) rotation-free algorithms for Softmax and LayerNorm that significantly reduce the number of costly HE rotations, removing 2448 HE rotations in BERT-base inference.    (3) Column packing removes rotations in plaintext–ciphertext matrix multiplications and interleaved batching further reduces the rotations in ciphertext–ciphertext matrix multiplications. MOAI uses at least 1.7x fewer HE rotations compared to the state-of-the-art works across all matrix multiplications of BERT-base. As a result, We achieve a 52.8\% reduction in evaluation time compared to the state-of-the-art HE-based non-interactive secure transformer inference, THOR (Moon et al., CCS'25). We then apply MOAI on the Powerformer's framework and achieve a 55.7\% reduction in evaluation time compared to Powerformer (Park et al., ACL'25), which approximates Softmax and LayerNorm with simpler functions in transformer and proposes HE-based non-interactive transformer inference. We report an amortized time of 2.36 minutes per input on a single GPU environment. We show the extendibility by applying MOAI in LLaMA-3-8B. Our implementation is publicly available as open source.

**Abstract (Chinese)**

在将大型语言模型 (LLM) 部署到云服务提供商 (CSP) 时，其推理过程引发了隐私担忧。全同态加密 (HE) 通过直接在加密输入上实现安全推理，提供了一个有前景的解决方案。然而，HE 的高计算开销仍然是一个主要瓶颈。为了应对这一挑战，我们提出了 MOAI，这是一个高效的基于 HE 的非交互式安全 Transformer 推理框架。MOAI 通过以下方式获得显著的效率提升：(1) 一种新型评估流程，将列打包和对角打包结合，并跨所有层采用一致策略，从而消除昂贵的格式转换。(2) 用于 Softmax 和 LayerNorm 的无旋转算法，大幅减少昂贵的 HE 旋转次数，在 BERT-base 推理中消除了 2448 次 HE 旋转。(3) 列打包消除了明文-密文矩阵乘法中的旋转，交错批处理进一步减少了密文-密文矩阵乘法中的旋转。与最先进的工作相比，MOAI 在 BERT-base 的所有矩阵乘法中至少减少了 1.7 倍的 HE 旋转。因此，与最先进的基于 HE 的非交互式安全 Transformer 推理 THOR (Moon et al., CCS'25) 相比，我们实现了 52.8% 的评估时间减少。然后，我们将 MOAI 应用于 Powerformer 框架，与使用 Transformer 中更简单函数近似 Softmax 和 LayerNorm 并提出基于 HE 的非交互式 Transformer 推理的 Powerformer (Park et al., ACL'25) 相比，实现了 55.7% 的评估时间减少。我们报告在单 GPU 环境下的每输入摊销时间为 2.36 分钟。我们通过在 LLaMA-3-8B 中应用 MOAI 展示了其可扩展性。我们的实现作为开源代码公开发布。

---

### On Optimal Hyperparameters for Differentially Private Deep Transfer Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Aki Rehn, Linzh Zhao, Mikko A. Heikkilä, Antti Honkela
- **Keywords**: differential privacy, hyperparameters, deep learning, transfer learning
- **OpenReview**: https://openreview.net/forum?id=V3fEo612nE
- **PDF**: https://openreview.net/pdf?id=V3fEo612nE

**Abstract**

Differentially private (DP) transfer learning, i.e., fine-tuning a pretrained model on private data, is the current state-of-the-art approach for training large models under privacy constraints. 
We focus on two key hyperparameters in this setting: the clipping bound $C$ and batch size $B$.
We show a clear mismatch between the current theoretical understanding of how to choose an optimal $C$ (stronger privacy requires smaller $C$) and empirical outcomes (larger $C$ performs better under strong privacy), caused by changes in the gradient distributions. 
Assuming a limited compute budget (fixed epochs), we demonstrate that the existing heuristics for tuning $B$ do not work, while cumulative DP noise better explains whether smaller or larger batches perform better. 
We also highlight how the common practice of using a single $(C,B)$ setting across tasks can lead to suboptimal performance. 
We find that performance drops especially when moving between loose and tight privacy and between plentiful and limited compute, which we explain by analyzing clipping as a form of gradient re-weighting and examining cumulative DP noise.

**Abstract (Chinese)**

差分隐私 (DP) 迁移学习，即在私有数据上微调预训练模型，是当前在隐私约束下训练大型模型的最先进方法。

我们关注该设置中的两个关键超参数：裁剪界 $C$ 和批次大小 $B$。

我们展示了当前对如何选择最优 $C$ 的理论理解（更强的隐私要求更小的 $C$）与实证结果（在强隐私下更大的 $C$ 表现更好）之间的明显不匹配，这是由梯度分布的变化引起的。

假设有限的计算预算（固定轮数），我们证明现有的调优 $B$ 的启发式方法不起作用，而累积 DP 噪声更好地解释了较小或较大批次哪个表现更好。

我们还强调了在不同任务中使用单一 $(C,B)$ 设置的常见做法如何导致次优性能。

我们发现性能下降尤其发生在从宽松隐私到严格隐私以及从充足计算到有限计算之间的转移中，我们通过将裁剪分析为一种梯度重加权形式并考察累积 DP 噪声来解释这一点。

---

### Operationalizing Data Minimization for Privacy-Preserving LLM Prompting

- **Venue**: ICLR 2026 Poster
- **Authors**: Jijie Zhou, Niloofar Mireshghallah, Tianshi Li
- **Keywords**: NLP, privacy, LLM, data minimization, data sanitization
- **OpenReview**: https://openreview.net/forum?id=rpcnvW33EG
- **PDF**: https://openreview.net/pdf?id=rpcnvW33EG

**Abstract**

The rapid deployment of large language models (LLMs) in consumer applications has led to frequent exchanges of personal information. To obtain useful responses, users often share more than necessary, increasing privacy risks via memorization, context-based personalization, or security breaches. We present a framework to formally define and operationalize *data minimization*: for a given user prompt and response model, quantifying the least privacy-revealing disclosure that maintains utility, and propose a priority-queue tree search to locate this optimal point within a privacy-ordered transformation space. We evaluated the framework on four datasets spanning open-ended conversations (ShareGPT, WildChat) and knowledge-intensive tasks with single-ground-truth answers (CaseHOLD, MedQA), quantifying achievable data minimization with nine LLMs as the response model. Our results demonstrate that larger frontier LLMs can tolerate stronger data minimization while maintaining task quality than smaller open-source models (*85.7%* redaction for GPT-5 vs. *19.3%* for Qwen2.5-0.5B). By comparing with our search-derived benchmarks, we find that LLMs struggle to predict optimal data minimization directly, showing a bias toward abstraction that leads to oversharing. This suggests not just a privacy gap, but a capability gap: models may lack awareness of what information they actually need to solve a task.

**Abstract (Chinese)**

大型语言模型 (LLMs) 在消费级应用中的快速部署导致了个人信息的频繁交换。为了获得有用的响应，用户常常分享超出必要的信息，从而通过记忆、基于上下文的个性化或安全漏洞增加隐私风险。我们提出一个框架，用于正式定义并操作化*数据最小化*：针对给定的用户提示和响应模型，量化保持效用的最小隐私泄露披露，并提出一种优先队列树搜索方法，在按隐私排序的变换空间中定位这一最优点。我们在四个数据集上评估了该框架，这些数据集涵盖开放式对话（ShareGPT、WildChat）和具有单一真实答案的知识密集型任务（CaseHOLD、MedQA），使用九个LLMs作为响应模型，量化了可实现的数据最小化。我们的结果表明，更大的前沿LLMs在保持任务质量的同时，能够容忍比小型开源模型更强的数据最小化（GPT-5的*85.7%*删减 vs. Qwen2.5-0.5B的*19.3%*）。通过与我们搜索得出的基准进行比较，我们发现LLMs难以直接预测最优数据最小化，表现出一种导致过度分享的抽象偏见。这表明不仅仅是隐私差距，而是一种能力差距：模型可能缺乏对解决任务实际需要何种信息的认识。

---

### Optimizing Canaries for Privacy Auditing with Metagradient Descent

- **Venue**: ICLR 2026 Poster
- **Authors**: Matteo Boglioni, Terrance Liu, Andrew Ilyas, Steven Wu
- **Keywords**: differential privacy, auditing, metagradient optimization
- **OpenReview**: https://openreview.net/forum?id=3xkYXuHDA6
- **PDF**: https://openreview.net/pdf?id=3xkYXuHDA6

**Abstract**

In this work we study black-box privacy auditing, where the goal is to lower bound the privacy parameter of a differentially private learning algorithm using only the algorithm’s outputs (i.e., final trained model). For DP-SGD (the most successful method for training differentially private deep learning models), the canonical auditing approach uses membership inference—an auditor comes with a small set of special “canary” examples, inserts a random subset of them into the training set, and then tries to discern which of their canaries were included in the training set (typically via a membership inference attack). The auditor’s success rate then provides a lower bound on the privacy parameters of the learning algorithm. Our main contribution is a method for optimizing the auditor’s canary set to improve privacy auditing, leveraging recent work on metagradient optimization (Engstrom et al., 2025). Our empirical evaluation demonstrates that in certain instances, using such optimized canaries can improve empirical lower bounds for differentially private image classification models by several times when compared to canaries proposed in prior work. Furthermore, we demonstrate that our method is DP-SGD agnostic and efficient: canaries optimized for non-private SGD with a small model architecture remain effective when auditing larger models trained with DP-SGD.

**Abstract (Chinese)**

在本工作中，我们研究黑盒隐私审计，其目标是使用仅算法输出（即最终训练模型）为差分隐私学习算法的隐私参数提供下界。对于DP-SGD（训练差分隐私深度学习模型的最成功方法），经典审计方法采用成员推断——审计者携带一小组特殊的“金丝雀”示例，将其随机子集插入训练集，然后尝试辨别哪些金丝雀示例被包含在训练集中（通常通过成员推断攻击）。审计者的成功率从而为学习算法的隐私参数提供下界。我们主要贡献是一种优化审计者金丝雀集以改善隐私审计的方法，利用了元梯度优化方面的最新工作（Engstrom et al., 2025）。我们的实证评估表明，在某些情况下，使用此类优化金丝雀可以将差分隐私图像分类模型的实证下界与先前工作中提出的金丝雀相比提高数倍。此外，我们证明了我们的方法对DP-SGD不敏感且高效：针对非私有SGD使用小型模型架构优化的金丝雀在审计使用DP-SGD训练的更大模型时仍然有效。

---

### PE-SGD: Differentially Private Deep Learning via Evolution of Gradient Subspace for Text

- **Venue**: ICLR 2026 Poster
- **Authors**: Tianyuan Zou, Zinan Lin, Sivakanth Gopi, Yang Liu, Ya-Qin Zhang, Robert Sim, Xin Deng, Sergey Yekhanin
- **Keywords**: Differential Privacy, Private Evolution, Generation Model
- **OpenReview**: https://openreview.net/forum?id=713ywmTZHv
- **PDF**: https://openreview.net/pdf?id=713ywmTZHv

**Abstract**

Differentially Private Stochastic Gradient Descent (DP-SGD) and its variants like DP-Adam ensure data privacy by injecting noise into per-sample gradients. Although effective with large private datasets, their performance degrades significantly when private training data is limited. Recent works leverage public data to learn a gradient subspace and project noisy private sample gradients on to this subspace, achieving improved performance. However, they have overlooked two crucial aspects: the limitation of using a fixed projection subspace throughout training and the importance of choosing where to inject noise. Therefore, we propose Private Evolution aided Stochastic Gradient Descent (***PE-SGD***), a differentially private training framework effective for scenarios with limited private data. ***PE-SGD*** uses an evolutionary strategy to update the gradient projection subspace during training process. We also identify a more effective noise injection point for better alignment between approximate DP-protected gradient and real private gradient. This enables ***PE-SGD*** to outperform DP-SGD and other baselines, particularly in the regime of limited private data and small privacy budget.

**Abstract (Chinese)**

差分隐私随机梯度下降 (DP-SGD) 及其变体如 DP-Adam 通过向每个样本梯度注入噪声来确保数据隐私。虽然在大规模私有数据集上有效，但当私有训练数据有限时，其性能会显著下降。最近的工作利用公共数据学习梯度子空间，并将噪声私有样本梯度投影到该子空间上，从而实现性能提升。然而，它们忽略了两个关键方面：整个训练过程中使用固定投影子空间的局限性，以及选择噪声注入位置的重要性。因此，我们提出私有进化辅助随机梯度下降 (***PE-SGD***)，这是一个针对私有数据有限场景有效的差分隐私训练框架。***PE-SGD*** 在训练过程中使用进化策略来更新梯度投影子空间。我们还识别出一个更有效的噪声注入点，以实现近似 DP 保护梯度与真实私有梯度之间的更好对齐。这使得 ***PE-SGD*** 优于 DP-SGD 和其他基线，尤其是在私有数据有限和小隐私预算的条件下。

---

### Pisces: Cryptography-based Private Retrieval-Augmented Generation with Dual-Path Retrieval

- **Venue**: ICLR 2026 Poster
- **Authors**: Xiaojian Liang, Lushan Song, Shishuai Du, Weicheng Zhu, Tan Li Hui Faith, Jun Jie Sim, Haibing Jin, Zhenghao Wu, Yingting Liu, Xin Zhang, Jiang-Ming Yang, Pu Duan
- **Keywords**: Retrieval-Augmented Generation, Privacy-Preserving, Cryptography
- **OpenReview**: https://openreview.net/forum?id=Re3A6vzCTC
- **PDF**: https://openreview.net/pdf?id=Re3A6vzCTC

**Abstract**

Retrieval-augmented generation (RAG) enhances the response quality of large language models (LLMs) when handling domain-specific tasks, yet raises significant privacy concerns. This is because both the user query and documents within the knowledge base often contain sensitive or confidential information. To address these concerns, we propose $\texttt{Pisces}$, the first practical cryptography-based RAG framework that supports dual-path retrieval, while protecting both the query and documents. Along the semantic retrieval path, we reduce computation and communication overhead by leveraging a coarse-to-fine strategy. Specifically, a novel oblivious filter is used to privately select a candidate set of documents to reduce the scale of subsequent cosine similarity computations. For the lexical retrieval path, to reduce the overhead of repeatedly invoking labeled PSI, we implement a multi-instance labeled PSI protocol to compute term frequencies for BM25 scoring in a single execution. $\texttt{Pisces}$ can also be integrated with existing privacy-preserving LLM inference frameworks to achieve end-to-end privacy. Experiments demonstrate that $\texttt{Pisces}$ achieves retrieval accuracy comparable to the plaintext baselines, within a 1.87% margin.

**Abstract (Chinese)**

检索增强生成（RAG）在处理领域特定任务时提升了大语言模型（LLMs）的响应质量，但却引发了显著的隐私担忧。这是因为用户查询和知识库中的文档往往包含敏感或机密信息。为了解决这些担忧，我们提出了$\texttt{Pisces}$，这是第一个实用的基于密码学的RAG框架，支持双路径检索，同时保护查询和文档。在语义检索路径上，我们通过粗到精策略降低计算和通信开销。具体而言，使用一种新型隐匿过滤器私密地选择候选文档集，以减少后续余弦相似度计算的规模。对于词汇检索路径，为了减少重复调用带标签PSI的开销，我们实现了一种多实例带标签PSI协议，在单次执行中计算BM25评分所需的词频。$\texttt{Pisces}$还可以与现有的隐私保护LLM推理框架集成，以实现端到端隐私。实验表明，$\texttt{Pisces}$的检索准确率与明文基线相当，差距不超过1.87%。

---

### Prediction with Expert Advice under Local Differential Privacy

- **Venue**: ICLR 2026 Poster
- **Authors**: Ben Jacobsen, Kassem Fawaz
- **Keywords**: privacy, differential privacy, online learning, online linear optimization, local differential privacy
- **OpenReview**: https://openreview.net/forum?id=B9H2705C7c
- **PDF**: https://openreview.net/pdf?id=B9H2705C7c

**Abstract**

We study the classic problem of prediction with expert advice under the constraint of local differential privacy (LDP). In this context, we first show that a classical algorithm naturally satisfies LDP and then design two new algorithms that improve it: RW-AdaBatch and RW-Meta. For RW-AdaBatch, we exploit the limited-switching behavior induced by LDP to provide a novel form of privacy amplification that grows stronger on easier data, analogous to the shuffle model in offline learning. Drawing on the theory of random walks, we prove that this improvement carries essentially no utility cost. For RW-Meta, we develop a general method for privately selecting between experts that are themselves non-trivial learning algorithms, and we show that in the context of LDP this carries no extra privacy cost. In contrast, prior work has only considered data-independent experts. We also derive formal regret bounds that scale inversely with the degree of independence between experts. Our analysis is supplemented by evaluation on real-world data reported by hospitals during the COVID-19 pandemic; RW-Meta outperforms both the classical baseline and a state-of-the-art \textit{central} DP algorithm by 1.5-3$\times$ on the task of predicting which hospital will report the highest density of COVID patients each week.

**Abstract (Chinese)**

我们研究了专家建议预测这一经典问题，在局部差分隐私（LDP）约束下。首先，我们证明一个经典算法自然满足LDP，然后设计了两个改进算法：RW-AdaBatch和RW-Meta。对于RW-AdaBatch，我们利用LDP诱导的有限切换行为，提供了一种新型隐私放大形式，这种放大在更容易的数据上更强，类似于离线学习中的shuffle模型。借鉴随机游走理论，我们证明这种改进几乎没有效用成本。对于RW-Meta，我们开发了一种通用方法，用于在本身是非平凡学习算法的专家之间进行私密选择，并证明在LDP背景下，这没有额外隐私成本。相比之下，先前工作仅考虑了数据无关的专家。我们还推导出形式遗憾界，这些界与专家之间独立程度的倒数成比例。我们的分析通过对COVID-19大流行期间医院报告的真实世界数据的评估得到补充；RW-Meta在预测每周哪家医院报告最高COVID患者密度的任务上，比经典基线和最先进的\textit{central} DP算法提高了1.5-3倍。

---

### Privacy Beyond Pixels: Latent Anonymization for Privacy-Preserving Video Understanding

- **Venue**: ICLR 2026 Poster
- **Authors**: Joseph Fioresi, Ishan Rajendrakumar Dave, Mubarak Shah
- **Keywords**: Privacy Preservation, Video Understanding
- **OpenReview**: https://openreview.net/forum?id=ncA3UUL0Ri
- **PDF**: https://openreview.net/pdf?id=ncA3UUL0Ri

**Abstract**

We introduce a novel formulation of visual privacy preservation for video foundation models that operates entirely in the latent space. While spatio-temporal features learned by foundation models have deepened general understanding of video content, sharing or storing these extracted visual features for downstream tasks inadvertently reveals sensitive personal information like skin color, gender, or clothing. Current privacy preservation methods focus on input-pixel-level anonymization, which requires retraining the entire utility video model and results in task-specific anonymization, making them unsuitable for recent video foundational models. To address these challenges, we introduce a lightweight Anonymizing Adapter Module (AAM) that removes private information from video features while retaining general task utility. AAM can be applied in a plug-and-play fashion to frozen video encoders, minimizing the computational burden of finetuning and re-extracting features. Our framework employs three newly designed training objectives: (1) a clip-level self-supervised privacy objective to reduce mutual information between static clips, (2) a co-training objective to retain utility across seen tasks, and (3) a latent consistency loss for generalization on unseen tasks. Our extensive evaluations demonstrate a significant 35% reduction in privacy leakage while maintaining near-baseline utility performance across various downstream tasks: Action Recognition (Kinetics400, UCF101, HMDB51), Temporal Action Detection (THUMOS14), and Anomaly Detection (UCF-Crime). We also provide an analysis on anonymization for sensitive temporal attribute recognition. Additionally, we propose new protocols for assessing gender bias in action recognition models, showing that our method effectively mitigates such biases and promotes more equitable video understanding.

**Abstract (Chinese)**

我们提出了一种针对视频基础模型的全新视觉隐私保护方法，该方法完全在潜在空间中操作。虽然基础模型学习的时空特征加深了对视频内容的通用理解，但为下游任务分享或存储这些提取的视觉特征会无意中泄露敏感个人信息，如肤色、性别或服装。现有的隐私保护方法专注于输入像素级匿名化，这需要重新训练整个实用视频模型，并导致任务特定的匿名化，使其不适用于最近的视频基础模型。为应对这些挑战，我们引入了一个轻量级的匿名化适配器模块（AAM），它从视频特征中移除私有信息，同时保留通用任务效用。AAM 可以以即插即用的方式应用于冻结的视频编码器，最大限度地减少微调和重新提取特征的计算负担。我们的框架采用了三个新设计的训练目标：（1）片段级自监督隐私目标，以减少静态片段之间的互信息；（2）联合训练目标，以保留已见任务的效用；（3）潜在一致性损失，用于未见任务的泛化。我们的广泛评估表明，在各种下游任务中实现了隐私泄露显著减少35%，同时保持接近基线的效用性能：动作识别（Kinetics400、UCF101、HMDB51）、时序动作检测（THUMOS14）和异常检测（UCF-Crime）。我们还提供了针对敏感时序属性识别的匿名化分析。此外，我们提出了评估动作识别模型性别偏差的新协议，表明我们的方法有效缓解了此类偏差，并促进了更公平的视频理解。

---

### Private Rate-Constrained Optimization with Applications to Fair Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Mohammad Yaghini, Tudor Cebere, Michael Menart, Aurélien Bellet, Nicolas Papernot
- **Keywords**: differential privacy, fairness, machine learning
- **OpenReview**: https://openreview.net/forum?id=mex3rvs2KX
- **PDF**: https://openreview.net/pdf?id=mex3rvs2KX

**Abstract**

Many problems in trustworthy ML can be expressed as constraints on prediction rates across subpopulations, including group fairness constraints (demographic parity, equalized odds, etc.). In this work, we study such constrained minimization problems under differential privacy (DP). Standard DP optimization techniques like DP-SGD rely on objectives that decompose over individual examples, enabling per-example gradient clipping and noise addition. Rate constraints, however, depend on aggregate statistics across groups, creating inter-sample dependencies that violate this decomposability. To address this, we develop RaCO-DP, a DP variant of Stochastic Gradient Descent-Ascent (SGDA) that solves the Lagrangian formulation of rate constraint problems. We show that the additional privacy cost of incorporating these constraints reduces to privately estimating a histogram over the mini-batch at each step. We prove convergence of our algorithm through a novel analysis of SGDA that leverages the linear structure of the dual parameter. Empirical results show that our method Pareto-dominates existing private learning approaches under group fairness constraints and also achieves strong privacy–utility–fairness performance on neural networks.

**Abstract (Chinese)**

许多可信赖机器学习问题可以表述为跨子群体的预测率约束，包括群体公平性约束（如人口统计学平价、等化几率等）。在本工作中，我们研究了在差分隐私 (DP) 下的此类约束最小化问题。标准的 DP 优化技术如 DP-SGD 依赖于可分解为单个样本的目标函数，从而实现每个样本的梯度裁剪和噪声添加。然而，预测率约束依赖于跨群体的聚合统计，从而产生样本间依赖性，违反了这种可分解性。为解决此问题，我们开发了 RaCO-DP，这是一种 DP 变体形式的随机梯度下降-上升 (SGDA)，用于求解预测率约束问题的拉格朗日公式化。我们证明，将这些约束纳入的额外隐私成本归结为在每一步私密估计小批量上的直方图。我们通过对 SGDA 的新型分析证明了我们算法的收敛性，该分析利用了对偶参数的线性结构。实证结果表明，我们的方法在群体公平性约束下帕累托主导现有的私有学习方法，并在神经网络上实现了强大的隐私–效用–公平性性能。

---

### Protection against Source Inference Attacks in Federated Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Andreas Athanasiou, Kangsoo Jung, Catuscia Palamidessi
- **Keywords**: Federated Learning, Source Inference Attack, Shuffle Model, Residue Number System
- **OpenReview**: https://openreview.net/forum?id=1GMw3IwEHW
- **PDF**: https://openreview.net/pdf?id=1GMw3IwEHW

**Abstract**

Federated Learning (FL) was initially proposed as a privacy-preserving machine learning paradigm. However, FL has been shown to be susceptible to a series of privacy attacks. Recently, there has been concern about the Source Inference Attack (SIA), where an honest-but-curious central server attempts to identify exactly which client owns a given data point which was used in the training phase. Alarmingly, standard gradient obfuscation techniques with Differential Privacy have been shown to be ineffective against SIAs, at least without severely diminishing the accuracy.

In this work, we propose a defense against SIAs within the widely studied shuffle model of FL, where an honest shuffler acts as an intermediary between the clients and the server. First, we demonstrate that standard naive shuffling alone is insufficient to prevent SIAs. To effectively defend against SIAs, shuffling needs to be applied at a more granular level; we propose a novel combination of parameter-level shuffling with the residue number system (RNS). Our approach provides robust protection against SIAs without affecting the accuracy of the joint model and can be seamlessly integrated into other privacy protection mechanisms.

We conduct experiments on a series of models and datasets, confirming that standard shuffling approaches fail to prevent SIAs and that, in contrast, our proposed method reduce the attack’s accuracy to the level of random guessing.

**Abstract (Chinese)**

联邦学习 (FL) 最初被提出作为一种隐私保护的机器学习范式。然而，FL 已被证明容易受到一系列隐私攻击的影响。最近，人们对来源推断攻击 (SIA) 表示担忧，其中诚实但好奇的中央服务器试图精确识别训练阶段中使用的数据点属于哪个客户端。令人担忧的是，带有差分隐私的标准梯度混淆技术已被证明对 SIA 无效，至少在不严重降低准确性的情况下是这样。

在本工作中，我们在广泛研究的 FL 混洗模型中提出了一种针对 SIA 的防御方法，其中诚实混洗器充当客户端和服务器之间的中介。首先，我们证明标准朴素混洗本身不足以防止 SIA。要有效防御 SIA，混洗需要在更细粒度级别应用；我们提出了一种新颖的参数级混洗与剩余数系统 (RNS) 的组合。我们的方法在不影响联合模型准确性的前提下提供对 SIA 的鲁棒保护，并且可以无缝集成到其他隐私保护机制中。

我们在系列模型和数据集上进行了实验，证实标准混洗方法无法防止 SIA，而相比之下，我们提出的方法将攻击的准确率降低到随机猜测的水平。

---

### RESFL: An Uncertainty-Aware Framework for Responsible Federated Learning by Balancing Privacy, Fairness and Utility

- **Venue**: ICLR 2026 Poster
- **Authors**: Dawood Wasif, Terrence J Moore, Jin-Hee Cho
- **Keywords**: Federated Learning, Fairness, Privacy, Adversarial Representation Learning, Uncertainty Quantification
- **OpenReview**: https://openreview.net/forum?id=Wfz7gpoDSl
- **PDF**: https://openreview.net/pdf?id=Wfz7gpoDSl

**Abstract**

Federated Learning (FL) has gained prominence in machine learning applications across critical domains, offering collaborative model training without centralized data aggregation. However, FL frameworks that protect privacy often sacrifice fairness and reliability; differential privacy reduces data leakage but hides sensitive attributes needed for bias correction, worsening performance gaps across demographic groups. This work explores the trade-off between privacy and fairness in FL-based object detection and introduces RESFL, an integrated solution optimizing both. RESFL incorporates adversarial privacy disentanglement and uncertainty-guided fairness-aware aggregation. The adversarial component uses a gradient reversal layer to remove sensitive attributes, reducing privacy risks while maintaining fairness. The uncertainty-aware aggregation employs an evidential neural network to weight client updates adaptively, prioritizing contributions with lower fairness disparities and higher confidence. This ensures robust and equitable FL model updates. We demonstrate the effectiveness of RESFL in high-stakes autonomous vehicle scenarios, where it achieves high mAP on FACET and CARLA, reduces membership-inference attack success by 37%, reduces equality-of-opportunity gap by 17% relative to the FedAvg baseline, and maintains superior adversarial robustness. However, RESFL is inherently domain-agnostic and thus applicable to a broad range of application domains beyond autonomous driving.

**Abstract (Chinese)**

联邦学习 (FL) 在关键领域的机器学习应用中已崭露头角，它提供了无需集中数据聚合的协作模型训练。然而，保护隐私的 FL 框架往往牺牲公平性和可靠性；差分隐私减少了数据泄露，但隐藏了偏差校正所需敏感属性，从而加剧了人口统计群体间的性能差距。本文探讨了基于 FL 的目标检测中隐私与公平之间的权衡，并引入了 RESFL，这是一种优化两者的集成解决方案。RESFL 集成了对抗性隐私解纠缠和不确定性引导的公平感知聚合。对抗性组件使用梯度反转层移除敏感属性，从而在保持公平性的同时降低隐私风险。不确定性感知聚合采用证据神经网络自适应加权客户端更新，优先考虑公平差异较小且置信度较高的贡献。这确保了鲁棒且公平的 FL 模型更新。我们在高风险自动驾驶场景中展示了 RESFL 的有效性，在 FACET 和 CARLA 上实现了高 mAP，将成员推断攻击成功率降低了 37%，相对于 FedAvg 基线将机会平等差距降低了 17%，并保持了优越的对抗鲁棒性。然而，RESFL 本质上是领域无关的，因此适用于自动驾驶以外的广泛应用领域。

---

### Rethinking LoRA for Privacy-Preserving Federated Learning in Large Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Jin Liu, Yinbin Miao, Ning Xi, Junkang Liu
- **Keywords**: Federated Learning, Differential Privacy, LoRA.
- **OpenReview**: https://openreview.net/forum?id=BPzSV4uw0x
- **PDF**: https://openreview.net/pdf?id=BPzSV4uw0x

**Abstract**

Fine-tuning large vision models (LVMs) and large language models (LLMs) under differentially private federated learning (DPFL) is hindered by a fundamental privacy-utility trade-off. Low-Rank Adaptation (LoRA), a promising parameter-efficient fine-tuning (PEFT) method, reduces computational and communication costs by introducing two trainable low-rank matrices while freezing pre-trained weights. However, directly applying LoRA in DPFL settings leads to performance degradation, especially in LVMs. Our analysis reveals three previously underexplored challenges: (1) gradient coupling caused by the simultaneous update of two asymmetric low-rank matrices, (2) compounded noise amplification under differential privacy, and (3) sharpness of the global aggregated model in the parameter space. To address these issues, we propose LA-LoRA (\textbf{L}ocal \textbf{A}lternating \textbf{LoRA}), a novel approach that decouples gradient interactions and aligns update directions across clients to enhance robustness under stringent privacy constraints. Theoretically, LA-LoRA strengthens convergence guarantees in noisy federated environments. Extensive experiments demonstrate that LA-LoRA achieves state-of-the-art (SOTA) performance on Swin Transformer and RoBERTa models, showcasing robustness to DP noise and broad applicability across both LVMs and LLMs. For example, when fine-tuning the Swin-B model on the Tiny-ImageNet dataset under a strict privacy budget ($\epsilon = 1$), LA-LoRA outperforms the best baseline, RoLoRA, by 16.83\% in test accuracy. Code is provided in the Appendix.

**Abstract (Chinese)**

在差分隐私联邦学习 (DPFL) 下微调大型视觉模型 (LVMs) 和大型语言模型 (LLMs) 受到基本的隐私-效用权衡的阻碍。低秩适应 (LoRA)，一种有前景的参数高效微调 (PEFT) 方法，通过引入两个可训练的低秩矩阵同时冻结预训练权重来降低计算和通信成本。然而，直接在 DPFL 设置中应用 LoRA 会导致性能下降，尤其是在 LVMs 中。我们的分析揭示了三个先前未充分探索的挑战：(1) 由两个不对称低秩矩阵同时更新引起的梯度耦合，(2) 差分隐私下的复合噪声放大，以及 (3) 参数空间中全局聚合模型的尖锐性。为了解决这些问题，我们提出 LA-LoRA（\textbf{L}ocal \textbf{A}lternating \textbf{LoRA}），一种新颖的方法，它解耦梯度交互并对齐客户端间的更新方向，以在严格的隐私约束下增强鲁棒性。从理论上讲，LA-LoRA 在噪声联邦环境中加强了收敛保证。广泛的实验表明，LA-LoRA 在 Swin Transformer 和 RoBERTa 模型上实现了最先进 (SOTA) 性能，展示了对比差分隐私噪声的鲁棒性和对 LVMs 和 LLMs 的广泛适用性。例如，在严格隐私预算 ($\epsilon = 1$) 下对 Tiny-ImageNet 数据集上的 Swin-B 模型进行微调时，LA-LoRA 在测试准确率上优于最佳基线 RoLoRA 16.83%。代码在附录中提供。

---

### SecP-Tuning: Efficient Privacy-Preserving Prompt Tuning for Large Language Models via MPC

- **Venue**: ICLR 2026 Poster
- **Authors**: Jinglong Luo, Zhuo Zhang, Yehong Zhang, Shiyu Liu, Ye Dong, Hui Wang, Yue Yu, Xun Zhou, Zenglin Xu
- **Keywords**: privacy-preserving, secure multi-party computation, large-language models, prompt tuning
- **OpenReview**: https://openreview.net/forum?id=iJNM7KY8FD
- **PDF**: https://openreview.net/pdf?id=iJNM7KY8FD

**Abstract**

Large Language Models (LLMs) have revolutionized numerous fields, yet their adaptation to specialized tasks in privacy-sensitive domains such as healthcare and finance remains constrained due to the scarcity of accessible training data caused by stringent privacy requirements. Secure Multi-party Computation (MPC)-based privacy-preserving machine learning provides theoretical guarantees for the privacy of model parameters and data. However, its application to LLMs has been predominantly limited to inference, as fine-tuning introduces significant efficiency challenges, particularly in backward propagation, optimizer, and self-attention operations. To address these challenges, we propose SecP-Tuning, the first MPC-based framework designed for efficient, privacy-preserving prompt tuning of LLMs. SecP-Tuning innovatively integrates Forward-only Tuning (FoT) through the ''data owner-server interaction" paradigm, effectively removing the need for privacy-preserving computations in backward propagation and optimization processes. Furthermore, it devises an efficient privacy-preserving Random Feature Attention (RFA), effectively mitigating the computational complexity of softmax-based self-attention and circumventing MPC-incompatible nonlinear operations. Experimental results demonstrate that, compared to full-Parameter Supervised Fine-Tuning (SFT) and gradient-based prompt tuning, SecP-Tuning achieves approximately 12$\times$ and 16$\times$ end-to-end acceleration, as well as 17$\times$ and 20$\times$ reductions in communication overhead, respectively. Moreover, it delivers performance comparable to gradient-based methods across multiple few-shot tasks. Additionally, the ''black-box/API-style" privacy-preserving tuning paradigm of SecP-Tuning effectively avoids memory leakage risks caused by gradient/parameter transmission, thereby striking an optimal balance between efficiency, accuracy, deployability, and privacy.

**Abstract (Chinese)**

大语言模型（LLMs）已革新众多领域，然而其在医疗和金融等隐私敏感领域特定任务的适应性仍受限，主要由于严格隐私要求导致可用训练数据稀缺。基于安全多方计算（MPC）的隐私保护机器学习为模型参数和数据的隐私提供了理论保证。然而，其在LLMs上的应用主要局限于推理阶段，因为微调引入了显著的效率挑战，尤其是在反向传播、优化器和自注意力操作方面。为应对这些挑战，我们提出SecP-Tuning，这是首个专为高效隐私保护提示调优LLMs而设计的MPC框架。SecP-Tuning创新性地通过“数据所有者-服务器交互”范式集成了仅前向调优（FoT），从而有效消除了反向传播和优化过程中隐私保护计算的需求。此外，它设计了一种高效的隐私保护随机特征注意力（RFA），有效缓解了基于softmax的自注意力的计算复杂度，并规避了MPC不相容的非线性操作。实验结果表明，与全参数监督微调（SFT）和基于梯度的提示调优相比，SecP-Tuning实现了约12倍和16倍的端到端加速，以及分别17倍和20倍的通信开销降低。此外，它在多项少样本任务上达到了与基于梯度方法相当的性能。另外，SecP-Tuning的“黑盒/API式”隐私保护调优范式有效避免了梯度/参数传输导致的内存泄漏风险，从而在效率、准确性、可部署性和隐私之间实现了最佳平衡。

---

### Secret-Protected Evolution for Differentially Private Synthetic Text Generation

- **Venue**: ICLR 2026 Poster
- **Authors**: Tianze Wang, Zhaoyu Chen, Jian Du, Yingtai Xiao, Linjun Zhang, Qiang Yan
- **Keywords**: synthetic data, differential privacy
- **OpenReview**: https://openreview.net/forum?id=1vacZJxi56
- **PDF**: https://openreview.net/pdf?id=1vacZJxi56

**Abstract**

Text data has become extremely valuable on large language models (LLMs) and even lead to general artificial intelligence (AGI).
A lot of high-quality text in the real world is private and cannot be freely used due to privacy concerns. Therefore, differentially private (DP) synthetic text generation has been proposed, aiming to produce high-utility synthetic data while protecting sensitive information.
However, existing DP synthetic text generation imposes uniform guarantees that often overprotect non-sensitive content, resulting in substantial utility loss and computational overhead. Therefore, we propose Secret-Protected Evolution (SecPE), a novel framework that extends private evolution with secret-aware protection. 
Theoretically, we show that SecPE satisfies $(\vp, \vr)$-secret protection, constituting a relaxation of Gaussian DP that enables tighter utility–privacy trade-offs, while also substantially reducing computational complexity relative to baseline methods.
Empirically, across the OpenReview, PubMed, and Yelp benchmarks, SecPE consistently achieves lower Fréchet Inception Distance (FID) and higher downstream task accuracy than GDP-based Aug-PE baselines, while requiring less noise to attain the same level of protection. 
Our results highlight that secret-aware guarantees can unlock more practical and effective privacy-preserving synthetic text generation.

**Abstract (Chinese)**

文本数据在大语言模型 (LLMs) 上变得极其宝贵，甚至引领通用人工智能 (AGI) 的发展。

现实世界中大量高质量文本是私有的，由于隐私担忧无法自由使用。因此，提出了差分隐私 (DP) 合成文本生成，旨在生成高实用性合成数据同时保护敏感信息。

然而，现有的 DP 合成文本生成施加了统一的保证，往往过度保护非敏感内容，导致显著的实用性损失和计算开销。因此，我们提出秘密保护演化 (SecPE)，这是一个新型框架，它通过秘密感知保护扩展了私有演化。

理论上，我们证明 SecPE 满足 $(\epsilon_p, \epsilon_r)$-秘密保护，这构成了高斯 DP 的松弛形式，能够实现更紧密的实用性–隐私权衡，同时相对于基线方法显著降低计算复杂度。

实证上，在 OpenReview、PubMed 和 Yelp 基准上，SecPE 始终比基于 GDP 的 Aug-PE 基线实现更低的 Fréchet Inception 距离 (FID) 和更高的下游任务准确率，同时需要更少的噪声来达到相同保护水平。

我们的结果突显，秘密感知保证能够解锁更实用和有效的隐私保护合成文本生成。

---

### Secure Inference for Diffusion Models via Unconditional Scores

- **Venue**: ICLR 2026 Poster
- **Authors**: Jaeyun Song, Geondo Park, Uigyu Kim, Joonhyung Park, Eunho Yang
- **Keywords**: privacy-preserving inference, diffusion models
- **OpenReview**: https://openreview.net/forum?id=6t9YPOZH0w
- **PDF**: https://openreview.net/pdf?id=6t9YPOZH0w

**Abstract**

As diffusion model-based services expand across various domains, safeguarding client data privacy has become increasingly critical. While fully homomorphic encryption and secure multi-party computation enable privacy-preserving inference, their high computational overhead poses challenges for large-scale diffusion applications. Recent work alleviates computational costs by substituting non-linear operations with low-degree polynomial approximations. While such relaxations reduce latency, they incur significant degradation in generative fidelity, and inference remains considerably slower than plaintext execution. To further accelerate secure inference while preserving performance, we explore more relaxed approximations and propose a score-correction framework that rectifies the conditional score shift induced by the relaxed approximation, rather than decreasing the approximation error itself. The key insight is that unconditional generation can be executed without approximation and thus provides a high-fidelity score signal. Leveraging this unconditional score as corrective guidance enables more relaxed approximations while preserving semantic and perceptual quality. In experiments, we demonstrate that our method significantly alleviates the performance degradation caused by relaxed approximations across various benchmarks.

**Abstract (Chinese)**

随着基于扩散模型的服务扩展到各个领域，保护客户端数据隐私变得日益关键。虽然全同态加密和安全多方计算实现了隐私保护推理，但其高计算开销为大规模扩散应用带来了挑战。最近的工作通过用低阶多项式逼近替换非线性操作来缓解计算成本。虽然此类松弛方法降低了延迟，但会导致生成保真度显著下降，并且推理速度仍远慢于明文执行。为了进一步加速安全推理同时保持性能，我们探索了更松弛的逼近方法，并提出了一种分数修正框架，该框架修正了松弛逼近引起的条件分数偏移，而不是直接减少逼近误差本身。关键洞见是，无条件生成可以无需逼近执行，从而提供高保真分数信号。利用这一无条件分数作为修正指导，可以实现更松弛的逼近，同时保持语义和感知质量。在实验中，我们证明了我们的方法在各种基准测试中显著缓解了松弛逼近引起的性能下降。

---

### Secure Outlier-Aware Large Language Model Inference

- **Venue**: ICLR 2026 Poster
- **Authors**: Lifan Zhao, Zhixuan Fang
- **Keywords**: Multiparty Computation, Privacy Perserving Machine Learning, Secure LLM Inference
- **OpenReview**: https://openreview.net/forum?id=Tmrjxq4d7w
- **PDF**: https://openreview.net/pdf?id=Tmrjxq4d7w

**Abstract**

Secure multiparty computation allows the client to secretly inference their sensitive inputs without acquiring the proprietary machine learning model weights. As the decoder-only transformer-based large language model becomes the popular paradigm, the desire of applying MPC in large language models is increasing. However, such inference usually leads to great amount of latency, which is due to nonlinear operations in the Transformer architecture. Recent works either focus on improving cryptographic primitives or re-architecting and re-training to make LLM MPC-friendly. We, on the other hand, observe that properly addressing outlier phenomena, which are unique yet universal properties existing across different LLMs, can effectively reduce the input domain and thereby design faster protocols for non-linear operations. Hence, we propose Secure Outlier-Aware Large Language Model Inference framework (SOAL), which accelerates the RMSNorm operation by nearly 2 $\times$, SiLU by $2\times$, and Softmax by more than 5$\times$. SOAL maintains the same performance of the original model without any fine-tuning requirement.

**Abstract (Chinese)**

安全多方计算允许客户端在不获取专有机器学习模型权重的情况下秘密推理其敏感输入。随着仅解码器Transformer-based大型语言模型成为流行范式，在大型语言模型中应用MPC的需求日益增加。然而，此类推理通常会导致大量延迟，这是由于Transformer架构中的非线性操作。最近的工作要么专注于改进密码原语，要么重新设计并重新训练以使LLM对MPC友好。另一方面，我们观察到，适当处理异常值现象——这些是存在于不同LLM中的独特却普遍的属性——可以有效缩小输入域，从而为非线性操作设计更快的协议。因此，我们提出了安全异常值感知大型语言模型推理框架（SOAL），它将RMSNorm操作加速近$2\times$，SiLU加速$2\times$，Softmax加速超过$5\times$。SOAL在不需任何微调的情况下保持原模型的相同性能。

---

### Skirting Additive Error Lower Bounds for Private Turnstile Streams

- **Venue**: ICLR 2026 Poster
- **Authors**: Anders Aamand, Justin Y. Chen, Sandeep Silwal
- **Keywords**: Differential privacy, streaming, distinctelements
- **OpenReview**: https://openreview.net/forum?id=gIaAuu8UZZ
- **PDF**: https://openreview.net/pdf?id=gIaAuu8UZZ

**Abstract**

We study differentially private continual release of the number of distinct items in a stream, where items may be both inserted and deleted. In this turnstile setting, a recent work of Jain, Kalemaj, Raskhodnikova, Sivakumar, and Smith (NeurIPS '23) showed that for streams of length $T$, polynomial additive error of $\Omega(T^{1/4})$ is necessary, even without any space restrictions. We show that this additive error lower bound can be circumvented if the algorithm is allowed to output estimates with *multiplicative* error. We give an algorithm for the continual release of the number of distinct elements with $\text{polylog} (T)$ multiplicative and  $\text{polylog}(T)$ additive error. We also show a qualitatively similar phenomenon for estimating the $F_2$ moment of a turnstile stream, where we can obtain $1+o(1)$ multiplicative and $\text{polylog} (T)$ additive error. Both results can be achieved by polylogarithmic space streaming algorithms where some multiplicative error is necessary even without privacy. Lastly, we raise questions aimed at better understanding trade-offs between multiplicative and additive error in private continual estimation problems.

**Abstract (Chinese)**

我们研究了数据流中不同元素数量的差分隐私持续发布，其中元素可以被插入和删除。在这种转门模型下，Jain、Kalemaj、Raskhodnikova、Sivakumar 和 Smith（NeurIPS '23）的近期工作表明，对于长度为 $T$ 的数据流，即使没有空间限制，也需要 $\Omega(T^{1/4})$ 的多项式加性误差。我们证明，如果允许算法输出具有*乘性*误差的估计值，则可以规避这一加性误差下界。我们提出了一种用于不同元素数量持续发布的算法，具有 $\text{polylog}(T)$ 乘性误差和 $\text{polylog}(T)$ 加性误差。我们还展示了转门数据流 $F_2$ 矩估计中类似的现象，其中可以获得 $1+o(1)$ 乘性误差和 $\text{polylog}(T)$ 加性误差。两种结果均可由多对数空间流算法实现，其中即使没有隐私，也需要一定的乘性误差。最后，我们提出了一些问题，旨在更好地理解私有持续估计问题中乘性和加性误差之间的权衡。

---

### Stop Tracking Me! Proactive Defense Against Attribute Inference Attack in LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Dong Yan, Jian Liang, Ran He, Tieniu Tan
- **Keywords**: Privacy leakage;Inference-preventing optimization;Text anonymization;Attribute inference attack;Large language models
- **OpenReview**: https://openreview.net/forum?id=dCJZR0P4T5
- **PDF**: https://openreview.net/pdf?id=dCJZR0P4T5

**Abstract**

Recent studies have shown that large language models (LLMs) can infer private user attributes (e.g., age, location, gender) from user-generated text shared online, enabling rapid and large-scale privacy breaches. Existing anonymization-based defenses are coarse-grained, lacking word-level precision in anonymizing privacy-leaking elements. Moreover, they are inherently limited as altering user text to hide sensitive cues still allows attribute inference to occur through models' reasoning capabilities.
To address these limitations, we propose a unified defense framework that combines fine-grained anonymization (TRACE) with inference-preventing optimization (RPS). TRACE leverages attention mechanisms and inference chain generation to identify and anonymize privacy-leaking textual elements, while RPS employs a lightweight two-stage optimization strategy to induce model rejection behaviors, thereby preventing attribute inference. 
Evaluations across diverse LLMs show that TRACE-RPS reduces attribute inference accuracy from around 50\% to below 5\% on open-source models. In addition, our approach offers strong cross-model generalization, prompt-variation robustness, and utility-privacy tradeoffs.
Our code is available at https://github.com/Jasper-Yan/TRACE-RPS.

**Abstract (Chinese)**

最近的研究表明，大语言模型（LLMs）能够从用户在线分享的生成文本中推断私人用户属性（例如年龄、位置、性别），从而实现快速且大规模的隐私泄露。现有的基于匿名化的防御方法是粗粒度的，在匿名化泄露隐私的元素时缺乏词级精度。此外，这些方法本质上存在局限性，因为修改用户文本以隐藏敏感线索仍会通过模型的推理能力导致属性推断发生。

为解决这些局限性，我们提出了一种统一的防御框架，将细粒度匿名化（TRACE）与防止推理优化（RPS）相结合。TRACE利用注意力机制和推理链生成来识别并匿名化泄露隐私的文本元素，而RPS采用轻量级两阶段优化策略来诱导模型拒绝行为，从而防止属性推断。

在多种LLMs上的评估显示，TRACE-RPS将开源模型上的属性推断准确率从约50\%降低至低于5\%。此外，我们的方法提供了强大的跨模型泛化能力、对提示变化的鲁棒性以及效用-隐私权衡。

我们的代码可在https://github.com/Jasper-Yan/TRACE-RPS获取。

---

### ULD-Net: Enabling Ultra-Low-Degree Fully Polynomial Networks for Homomorphically Encrypted Inference

- **Venue**: ICLR 2026 Poster
- **Authors**: Xi Xie, Ran Ran, Jiahui Zhao, Bin Lei, Zhijie Jerry Shi, Wujie Wen, Caiwen Ding
- **Keywords**: Privacy-Preserving Machine Learning, efficient private inference, machine learning as a service, homomorphic encryption, Fully Polynomial Networks, Ultra-Low-Degree operators
- **OpenReview**: https://openreview.net/forum?id=Jngc6oTe8R
- **PDF**: https://openreview.net/pdf?id=Jngc6oTe8R

**Abstract**

Fully polynomial neural networks—models whose computations comprise only additions and multiplications—are attractive for privacy-preserving inference under homomorphic encryption (HE). Yet most prior systems obtain such models by post-hoc replacement of nonlinearities with high-degree or cascaded polynomials, which inflates HE cost and makes training numerically fragile and hard to scale.

We introduce ULD-Net, a training methodology that enables ultra-low-degree (multiplicative depth $\leq 3$ for each operator) fully polynomial networks to be trained from scratch at ImageNet and transformer scale while maintaining high accuracy. The key is a polynomial-only normalization, \ournorm, coupled with a principled choice of normalization axis that keeps activations in a well-conditioned range across deep stacks of polynomial layers. Together with a special set of polynomial-aware operator replacements, such as polynomial activation functions and linear attention, ULD-Net delivers stable optimization without resorting to high-degree approximations.

Experimental results demonstrate that ULD-Net enables stable training of low-degree fully polynomial networks on large-scale model architectures and datasets. Applying ULD-Net to ViT-Small and ViT-Base achieves 76.70\% and 75.20\% top-1 accuracy on ImageNet, respectively, which are comparable to the original models and represent the first fully polynomial models successfully scaled to the ViT/ImageNet level. Additionally, ULD-Net outperforms several state-of-the-art open-source fully and partially polynomial approaches across diverse model architectures and datasets in both accuracy and HE inference latency.

**Abstract (Chinese)**

全多项式神经网络——其计算仅包含加法和乘法——在同态加密 (HE) 下的隐私保护推理中具有吸引力。然而，先前大多数系统通过事后将非线性函数替换为高次或级联多项式来获得此类模型，这会增加 HE 成本，并使训练在数值上脆弱且难以扩展。

我们提出 ULD-Net，一种训练方法，它能够从头训练超低度（每个算子乘法深度 $\leq 3$）全多项式网络，在 ImageNet 和 Transformer 规模上保持高准确率。其关键在于仅多项式的归一化方法 \ournorm，与精心选择的归一化轴相结合，该轴确保激活值在深层多项式层堆栈中保持良好条件数范围。结合一组特殊的多项式感知算子替换（如多项式激活函数和线性注意力），ULD-Net 实现了稳定的优化，而无需诉诸高次逼近。

实验结果表明，ULD-Net 能够在大型模型架构和数据集上稳定训练低度全多项式网络。将 ULD-Net 应用于 ViT-Small 和 ViT-Base，在 ImageNet 上分别实现了 76.70\% 和 75.20\% 的 top-1 准确率，与原始模型相当，并代表了首批成功扩展至 ViT/ImageNet 级别的全多项式模型。此外，ULD-Net 在准确率和 HE 推理延迟方面，优于多种最先进的开源全多项式和部分多项式方法，覆盖了多样化的模型架构和数据集。

---

### Unified Privacy Guarantees for Decentralized Learning via Matrix Factorization

- **Venue**: ICLR 2026 Poster
- **Authors**: Aurélien Bellet, Edwige Cyffers, Davide Frey, Romaric Gaudel, Dimitri Lerévérend, Francois Taiani
- **Keywords**: Differential Privacy, Decentralized Learning, Matrix Mechanism, Gossip
- **OpenReview**: https://openreview.net/forum?id=JTUOGo7NFD
- **PDF**: https://openreview.net/pdf?id=JTUOGo7NFD

**Abstract**

Decentralized Learning (DL) enables users to collaboratively train models without sharing raw data by iteratively averaging local updates with neighbors in a network graph. This setting is increasingly popular for its scalability and its ability to keep data local under user control. Strong privacy guarantees in DL are typically achieved through Differential Privacy (DP), with results showing that DL can even amplify privacy by disseminating noise across peer-to-peer communications.
Yet in practice, the observed privacy-utility trade-off often appears worse than in centralized training, which may be due to limitations in current DP accounting methods for DL. In this paper, we show that recent advances in centralized DP accounting based on Matrix Factorization (MF) for analyzing temporal noise correlations can also be leveraged in DL. By generalizing existing MF results, we show how to cast both standard DL algorithms and common trust models into a unified formulation. This yields tighter privacy accounting for existing DP-DL algorithms and provides a principled way to develop new ones. To demonstrate the approach, we introduce MAFALDA-SGD, a gossip-based DL algorithm with user-level correlated noise that outperforms existing methods on synthetic and real-world graphs.

**Abstract (Chinese)**

去中心化学习 (DL) 通过在网络图中与邻居迭代平均本地更新，使用户能够在不共享原始数据的情况下协作训练模型。这种设置因其可扩展性和将数据保持在用户控制下的本地能力而日益流行。DL 中的强隐私保证通常通过差分隐私 (DP) 实现，结果表明 DL 可以通过在点对点通信中传播噪声来放大隐私。

然而，在实践中，观察到的隐私-效用权衡往往比集中式训练更差，这可能是由于当前 DL 的 DP 记账方法的局限性。在本文中，我们证明，基于矩阵分解 (MF) 用于分析时序噪声相关性的集中式 DP 记账的最新进展也可以在 DL 中利用。通过泛化现有的 MF 结果，我们展示了如何将标准 DL 算法和常见信任模型纳入统一的表述框架。这为现有的 DP-DL 算法提供了更严格的隐私记账，并为开发新算法提供了原则性方法。为了展示该方法，我们引入了 MAFALDA-SGD，这是一种基于八卦协议的 DL 算法，具有用户级相关噪声，在合成和真实世界图上优于现有方法。

---
