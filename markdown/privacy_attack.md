# privacy_attack

**Description**: 隐私攻击与泄露风险。包括 membership inference、data extraction、model inversion、PII leakage、prompt leakage、training data reconstruction、attack surfaces in RAG/tools 等。

**Paper count**: 13

---

### Hubble: a Model Suite to Advance the Study of LLM Memorization

- **Venue**: ICLR 2026 Oral
- **Authors**: Johnny Wei, Ameya Godbole, Mohammad Aflah Khan, Ryan Yixiang Wang, Xiaoyuan Zhu, James Flemings, Nitya Kashyap, Krishna P. Gummadi, Willie Neiswanger, Robin Jia
- **Keywords**: memorization, copyright, privacy, test set contamination, membership inference, unlearning
- **OpenReview**: https://openreview.net/forum?id=ZfdnZhOP0k
- **PDF**: https://openreview.net/pdf?id=ZfdnZhOP0k

**Abstract**

We present Hubble, a suite of fully open-source large language models (LLMs) for the scientific study of LLM memorization. Hubble models come in standard and perturbed variants: standard models are pretrained on a large English corpus, and perturbed models are trained in the same way but with controlled insertion of text (e.g., book passages, biographies, and test sets) designed to emulate key memorization risks. Our core release includes 8 models---standard and perturbed models with 1B or 8B parameters, pretrained on 100B or 500B tokens---establishing that memorization risks are determined by the frequency of sensitive data relative to size of the training corpus (i.e., a password appearing once in a smaller corpus is memorized better than the same password in a larger corpus). Our release also includes 6 perturbed models with text inserted at different pretraining phases, showing that sensitive data without continued exposure can be forgotten. These findings suggest two best practices for addressing memorization risks: to dilute sensitive data by increasing the size of the training corpus, and to order sensitive data to appear earlier in training. Beyond these general empirical findings, Hubble enables a broad range of memorization research; for example, analyzing the biographies reveals how readily different types of private information are memorized. We also demonstrate that the randomized insertions in Hubble make it an ideal testbed for membership inference and machine unlearning, and invite the community to further explore, benchmark, and build upon our work.

**Abstract (Chinese)**

我们介绍了Hubble，这是一套完全开源的大型语言模型（LLMs），用于科学地研究LLM的记忆化现象。Hubble模型包括标准变体和扰动变体：标准模型在大型英文语料库上进行预训练，而扰动模型以相同方式训练，但通过控制性地插入文本（例如，书籍段落、传记和测试集）来模拟关键的记忆化风险。我们核心发布包括8个模型——具有1B或8B参数的标准和扰动模型，在100B或500B令牌上预训练——确立了记忆化风险由敏感数据相对于训练语料库大小的频率决定的观点（即，密码在较小语料库中出现一次比在较大语料库中出现一次更容易被记忆）。我们的发布还包括6个在不同预训练阶段插入文本的扰动模型，显示没有持续暴露的敏感数据可以被遗忘。这些发现建议了两项应对记忆化风险的最佳实践：通过增加训练语料库的大小来稀释敏感数据，以及安排敏感数据在训练早期出现。除了这些一般实证发现之外，Hubble支持广泛的记忆化研究；例如，分析传记揭示了不同类型的私人信息被记忆的难易程度。我们还证明了Hubble中随机插入的设计使其成为成员推断和机器遗忘的理想测试平台，并邀请社区进一步探索、基准测试并基于我们的工作进行扩展。

---

### Black-Box Privacy Attacks on Shared Representations in Multitask Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: John Abascal, Nicolás Berrios, Alina Oprea, Jonathan Ullman, Adam Smith, Matthew Jagielski
- **Keywords**: multitask learning, privacy, attacks
- **OpenReview**: https://openreview.net/forum?id=mTsWEVhcZM
- **PDF**: https://openreview.net/pdf?id=mTsWEVhcZM

**Abstract**

The proliferation of diverse data across users and organizations has driven the development of machine learning methods that enable multiple entities to jointly train models while minimizing data sharing. Among these, *multitask learning* (MTL) is a powerful paradigm that leverages similarities among multiple tasks, each with insufficient samples to train a standalone model, to solve them simultaneously. MTL accomplishes this by learning a *shared representation* that captures common structure between tasks and generalizes well across them all. Despite being designed to be the smallest unit of shared information necessary to effectively learn patterns across multiple tasks, these shared representations can inadvertently leak sensitive information about the particular tasks they were trained~on.

In this work, we investigate privacy leakage in shared representations through the lens of inference attacks. Towards this, we propose a novel, *black-box task-inference* threat model where the adversary, given the embedding vectors produced by querying the shared representation on samples from a particular task, aims to determine whether the task was present in the multitask training dataset. Motivated by analysis of tracing attacks on mean estimation over mixtures of Gaussian distributions, we develop efficient, purely black-box attacks on machine learning models that exploit the dependencies between embeddings from the same task without requiring shadow models or labeled reference data. We evaluate our attacks across vision and language domains when MTL is used for personalization and for solving multiple distinct learning problems, and demonstrate that even with access only to fresh task samples rather than training data, a black-box adversary can successfully infer a task's inclusion in training.

**Abstract (Chinese)**

用户和组织间多样化数据的激增推动了机器学习方法的发展，这些方法使多个实体能够联合训练模型，同时最小化数据共享。其中，*多任务学习* (MTL) 是一种强大的范式，它利用多个任务间的相似性——每个任务的样本均不足以训练独立模型——来同时求解这些任务。MTL 通过学习一种*共享表示* 来实现这一点，该表示捕捉任务间的共同结构，并在所有任务上泛化良好。尽管这些共享表示被设计为有效学习多个任务模式所需的最小共享信息单元，但它们仍可能无意中泄露关于特定训练任务的敏感信息。

在本工作中，我们通过推断攻击的视角调查共享表示中的隐私泄露。为此，我们提出了一种新型的*黑盒任务推断*威胁模型，其中攻击者在给定通过在特定任务样本上查询共享表示而产生的嵌入向量时，旨在判断该任务是否出现在多任务训练数据集中。受高斯分布混合均值估计追踪攻击分析的启发，我们开发了针对机器学习模型的高效、纯黑盒攻击，这些攻击利用同一任务嵌入间的依赖性，而无需影子模型或带标签的参考数据。我们在视觉和语言领域评估了这些攻击，这些领域中MTL 用于个性化以及求解多个不同学习问题，并证明即使仅访问新鲜任务样本而非训练数据，黑盒攻击者也能成功推断任务是否包含在训练中。

---

### Curation Leaks: Membership Inference Attacks against Data Curation for Machine Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Dariush Wahdany, Matthew Jagielski, Adam Dziedzic, Franziska Boenisch
- **Keywords**: machine learning, privacy
- **OpenReview**: https://openreview.net/forum?id=BzNf90Csfa
- **PDF**: https://openreview.net/pdf?id=BzNf90Csfa

**Abstract**

In machine learning, curation is used to select the most valuable data for improving both model accuracy and computational efficiency. Recently, curation has also been explored as a solution for private machine learning: rather than training directly on sensitive data, which is known to leak information through model predictions, the private data is used only to guide the selection of useful public data. The resulting model is then trained solely on curated public data. It is tempting to assume that such a model is privacy-preserving because it has never seen the private data. Yet, we show that without further protection, curation pipelines can still leak private information. Specifically, we introduce novel attacks against popular curation methods, targeting every major step: the computation of curation scores, the selection of the curated subset, and the final trained model. We demonstrate that each stage reveals information about the private dataset and that even models trained exclusively on curated public data leak membership information about the private data that guided curation. These findings highlight the previously overlooked inherent privacy risks of data curation and show that privacy assessment must extend beyond the training procedure to include the data selection process. Our differentially private adaptations of curation methods effectively mitigate leakage, indicating that formal privacy guarantees for curation are a promising direction.

**Abstract (Chinese)**

在机器学习中，数据精选用于选择最有价值的数据，以提升模型准确性和计算效率。最近，数据精选也被探索作为隐私机器学习的解决方案：与其直接在敏感数据上训练（已知会通过模型预测泄露信息），私有数据仅用于指导选择有用的公共数据。随后得到的模型仅在精选公共数据上训练。人们很容易假设这样的模型是隐私保护的，因为它从未见过私有数据。然而，我们证明，在没有进一步保护的情况下，数据精选管道仍可能泄露私有信息。具体而言，我们针对流行数据精选方法引入了新型攻击，针对每个主要步骤：精选分数计算、精选子集选择，以及最终训练模型。我们证明，每个阶段都会泄露关于私有数据集的信息，即使仅在精选公共数据上训练的模型，也会泄露指导精选的私有数据的成员身份信息。这些发现突显了先前被忽略的数据精选固有隐私风险，并表明隐私评估必须超出训练过程，包括数据选择过程。我们对数据精选方法的差分隐私适应有效缓解了泄露，表明为数据精选提供正式隐私保证是一个有前景的方向。

---

### Doxing via the Lens: Revealing Location-related Privacy Leakage on Multi-modal Large Reasoning Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Weidi Luo, Tianyu Lu, Qiming Zhang, Xiaogeng Liu, Bin Hu, Yue Zhao, Jieyu Zhao, Song Gao, Patrick McDaniel, Zhen Xiang, Chaowei Xiao
- **Keywords**: Privacy Leakage
- **OpenReview**: https://openreview.net/forum?id=uBThjlbzxS
- **PDF**: https://openreview.net/pdf?id=uBThjlbzxS

**Abstract**

Recent advances in multi-modal large reasoning models (MLRMs) have shown significant ability to interpret complex visual content. While these models possess impressive reasoning capabilities, they also introduce novel and underexplored privacy risks. In this paper, we identify a novel category of privacy leakage in MLRMs: Adversaries can infer sensitive geolocation information, such as users' home addresses or neighborhoods, from user-generated images, including selfies captured in private settings. To formalize and evaluate these risks, we propose a three-level privacy risk framework that categorizes image based on contextual sensitivity and potential for geolocation inference. We further introduce DoxBench, a curated dataset of 500 real-world images reflecting diverse privacy scenarios divided into 6 categories. Our evaluation across 13 advanced MLRMs and MLLMs demonstrates that most of these models outperform non-expert humans in geolocation inference and can effectively leak location-related private information. This significantly lowers the barrier for adversaries to obtain users' sensitive geolocation information. We further analyze and identify two primary factors contributing to this vulnerability: (1) MLRMs exhibit strong geolocation reasoning capabilities by leveraging visual clues in combination with their internal world knowledge; and (2) MLRMs frequently rely on privacy-related visual clues for inference without any built-in mechanisms to suppress or avoid such usage. To better understand and demonstrate real-world attack feasibility, we propose GeoMiner, a collaborative attack framework that decomposes the prediction process into two stages consisting of clue extraction and reasoning to improve geolocation performance. Our findings highlight the urgent need to reassess inference-time privacy risks in MLRMs to better protect users' sensitive information.

**Abstract (Chinese)**

最近多模态大推理模型（MLRMs）的进展显示出其解释复杂视觉内容的能力显著提升。虽然这些模型具有令人印象深刻的推理能力，但它们也引入了新型且尚未充分探索的隐私风险。在本文中，我们识别出 MLRMs 中的一种新型隐私泄露类别：攻击者可以从用户生成的图像中推断敏感地理位置信息，例如用户的家庭地址或社区，包括在私人环境中拍摄的自拍照。为了形式化和评估这些风险，我们提出一个三级隐私风险框架，该框架根据上下文敏感性和地理位置推断潜力对图像进行分类。我们进一步引入 DoxBench，这是一个精选的包含 500 张真实世界图像的数据集，反映了多样化的隐私场景，并分为 6 个类别。我们对 13 个先进的 MLRMs 和 MLLMs 的评估表明，大多数这些模型在地理位置推断方面优于非专家人类，并能有效泄露与位置相关的私人信息。这显著降低了攻击者获取用户敏感地理位置信息的门槛。我们进一步分析并识别出导致此漏洞的两个主要因素：（1）MLRMs 通过结合视觉线索与其内部世界知识，展现出强大的地理位置推理能力；（2）MLRMs 经常依赖隐私相关的视觉线索进行推理，而没有任何内置机制来抑制或避免此类使用。为了更好地理解并展示现实世界攻击的可行性，我们提出 GeoMiner，这是一个协作攻击框架，将预测过程分解为两个阶段，包括线索提取和推理，以提升地理位置性能。我们的发现突显了重新评估 MLRMs 中推理时隐私风险的迫切需要，以更好地保护用户的敏感信息。

---

### Fine-Grained Privacy Extraction from Retrieval-Augmented Generation Systems by Exploiting Knowledge Asymmetry

- **Venue**: ICLR 2026 Poster
- **Authors**: Yufei Chen, Yao Wang, Haibin Zhang, Tao Gu
- **Keywords**: RAG, knowledge asymmetry, privacy extraction, cross-domain generalization
- **OpenReview**: https://openreview.net/forum?id=B6ILMPPKnK
- **PDF**: https://openreview.net/pdf?id=B6ILMPPKnK

**Abstract**

Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by incorporating external knowledge bases, significantly improving their factual accuracy and contextual relevance. However, this integration also introduces new privacy vulnerabilities. Existing privacy attacks on RAG systems may trigger data leakage, but they often fail to accurately isolate knowledge base-derived content within mixed responses and perform poorly in multi-domain settings. In this paper, we propose a novel black-box attack framework that exploits knowledge asymmetry between RAG systems and standard LLMs to enable fine-grained privacy extraction across heterogeneous knowledge domains. Our approach decomposes adversarial queries to maximize information divergence between the models, then applies semantic relationship scoring to resolve lexical and syntactic ambiguities. These features are used to train a neural classifier capable of precisely identifying response segments that contain private or sensitive information. Unlike prior methods, our framework generalizes to unseen domains through iterative refinement without requiring prior knowledge of the corpus. Experimental results show that our method achieves over 90\% extraction accuracy in single-domain scenarios and 80\% in multi-domain settings, outperforming baselines by over 30\% in key evaluation metrics. These results represent the first systematic solution for fine-grained privacy localization in RAG systems, exposing critical security vulnerabilities and paving the way for stronger, more resilient defenses.

**Abstract (Chinese)**

检索增强生成（RAG）系统通过整合外部知识库来增强大语言模型（LLMs），显著提升了其事实准确性和上下文相关性。然而，这种整合也引入了新的隐私漏洞。现有的针对RAG系统的隐私攻击可能引发数据泄露，但它们往往无法在混合响应中准确隔离知识库派生的内容，并且在多领域设置中表现不佳。本文提出了一种新型黑盒攻击框架，该框架利用RAG系统与标准LLMs之间的知识不对称，实现跨异构知识领域的细粒度隐私提取。我们的方法通过分解对抗查询来最大化模型间的信息散度，然后应用语义关系评分来解决词汇和句法歧义。这些特征用于训练一个神经分类器，能够精确识别包含私有或敏感信息的响应片段。与先前方法不同，我们的框架通过迭代精炼泛化到未见领域，而无需事先了解语料库。实验结果表明，我们的方法在单领域场景中实现了超过90%的提取准确率，在多领域设置中达到了80%，在关键评估指标上优于基线方法超过30%。这些结果代表了RAG系统中细粒度隐私定位的首个系统性解决方案，暴露了关键安全漏洞，并为更强大、更具弹性的防御措施铺平了道路。

---

### Information-Theoretic Membership Inference for Granular Quantification of Memorization

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiashu Tao, Reza Shokri
- **Keywords**: membership inference attack, mia, privacy, llm privacy, memorization
- **OpenReview**: https://openreview.net/forum?id=4KVeb0Vv13
- **PDF**: https://openreview.net/pdf?id=4KVeb0Vv13

**Abstract**

Machine learning models are known to leak sensitive information, as they inevitably memorize (parts of) their training data. This risk is amplified for large language models (LLMs), which are trained on massive corpora and therefore create a more urgent need for privacy assessment prior to release. The standard method to quantify privacy is via membership inference attacks, where the state-of-the-art approach is the Robust Membership Inference Attack (RMIA). In this paper, we introduce \textbf{InfoRMIA}, a principled information-theoretic formulation of membership inference that consistently outperforms RMIA across benchmarks while improving computational efficiency. Moving beyond attack performance alone, we show that treating sequence-level membership inference as the gold standard obscures how memorization manifests in LLMs. To address this limitation, we propose a fine-grained memorization assessment framework based on token-level signals, with InfoRMIA serving as its algorithmic backbone. Our approach identifies which tokens within generated outputs are memorized, localizing privacy leakage from sequences to individual tokens. This framework enables more precise analysis of LLM memorization and potentially targeted mitigation strategies such as exact unlearning.

**Abstract (Chinese)**

机器学习模型已知会泄露敏感信息，因为它们不可避免地会记忆（部分）训练数据。这种风险在大语言模型（LLMs）中被放大，这些模型在海量语料库上训练，因此在发布前对隐私进行评估的需求更为迫切。量化隐私的标准方法是通过成员推断攻击，其中最先进的方法是鲁棒成员推断攻击（RMIA）。在本文中，我们引入InfoRMIA，这是一种基于信息论的成员推断原理性表述，它在各种基准测试中始终优于RMIA，同时提高了计算效率。超越单纯的攻击性能，我们表明，将序列级成员推断视为金标准会掩盖记忆化在大语言模型中的表现方式。为了解决这一局限性，我们提出了一种基于令牌级信号的细粒度记忆化评估框架，以InfoRMIA作为其算法骨干。我们的方法识别生成输出中哪些令牌被记忆化，将隐私泄露从序列定位到单个令牌。这一框架能够更精确地分析大语言模型的记忆化，并可能实现针对性的缓解策略，如精确遗忘。

---

### Membership Inference Attacks Against Fine-tuned Diffusion Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Yuetian Chen, Kaiyuan Zhang, Yuntao Du, Edoardo Stoppa, Charles Fleming, Ashish Kundu, Bruno Ribeiro, Ninghui Li
- **Keywords**: Membership Inference Attack, LLM, AI Privacy
- **OpenReview**: https://openreview.net/forum?id=oWKJursYpW
- **PDF**: https://openreview.net/pdf?id=oWKJursYpW

**Abstract**

Diffusion Language Models (DLMs) represent a promising alternative to autoregressive language models, using bidirectional masked token prediction. Yet their susceptibility to privacy leakage via Membership Inference Attacks (MIA) remains critically underexplored. This paper presents the first systematic investigation of MIA vulnerabilities in DLMs. Unlike the autoregressive models' single fixed prediction pattern, DLMs' multiple maskable configurations exponentially increase attack opportunities. This ability to probe many independent masks dramatically improves detection chances. To exploit this, we introduce SAMA (Subset-Aggregated Membership Attack), which addresses the sparse signal challenge through robust aggregation. SAMA samples masked subsets across progressive densities and applies sign-based statistics that remain effective despite heavy-tailed noise. Through inverse-weighted aggregation prioritizing sparse masks' cleaner signals, SAMA transforms sparse memorization detection into a robust voting mechanism. Experiments on nine datasets show SAMA achieves 30\% relative AUC improvement over the best baseline, with up to 8$\times$ improvement at low false positive rates. These findings reveal significant, previously unknown vulnerabilities in DLMs, necessitating the development of tailored privacy defenses.

**Abstract (Chinese)**

扩散语言模型（DLMs）是自回归语言模型的有前景的替代方案，使用双向掩码令牌预测。然而，它们通过成员推断攻击（MIA）导致的隐私泄露易感性仍未得到充分探索。本文首次系统调查了DLMs中的MIA漏洞。与自回归模型的单一固定预测模式不同，DLMs的多种可掩码配置会指数级增加攻击机会。这种探测多个独立掩码的能力显著提高了检测机会。为利用这一点，我们引入了SAMA（子集聚合成员攻击），它通过鲁棒聚合解决了稀疏信号挑战。SAMA在渐进密度下采样掩码子集，并应用基于符号的统计量，即使在重尾噪声下也保持有效。通过优先考虑稀疏掩码更干净信号的反向加权聚合，SAMA将稀疏记忆检测转化为鲁棒投票机制。在九个数据集上的实验显示，SAMA相对于最佳基线实现了30%的相对AUC改进，在低假阳性率下改进高达8倍。这些发现揭示了DLMs中先前未知的重大漏洞，需要开发量身定制的隐私防御措施。

---

### Membership Privacy Risks of Sharpness Aware Minimization

- **Venue**: ICLR 2026 Poster
- **Authors**: Young In Kim, Andrea Agiollo, Pratiksha Agrawal, Johannes O. Royset, Rajiv Khanna
- **Keywords**: membership inference attack, sam, sharpness aware minimization, memorization, benign overfitting
- **OpenReview**: https://openreview.net/forum?id=VU7wekA9CD
- **PDF**: https://openreview.net/pdf?id=VU7wekA9CD

**Abstract**

Optimization algorithms that seek flatter minima, such as Sharpness-Aware Minimization (SAM), are credited with improved generalization and robustness to noise. We ask whether such gains impact membership privacy. Surprisingly, we find that SAM is more prone to Membership Inference Attacks (MIA) than classical SGD across multiple datasets and attack methods, despite achieving lower test error. This suggests that the geometric mechanism of SAM that improves generalization simultaneously exacerbates membership leakage. We investigate this phenomenon through extensive analysis of memorization and influence scores. Our results reveal that SAM is more capable of capturing atypical subpatterns, leading to higher memorization scores of samples. Conversely, SGD depends more heavily on majority features, exhibiting worse generalization on atypical subgroups and lower memorization. Crucially, this characteristic of SAM can be linked to lower variance in the prediction confidence of unseen samples, thereby amplifying membership signals. Finally, we model SAM under a perfectly interpolating linear regime and theoretically show that sharpness regularization inherently reduces variance, guaranteeing a higher MIA advantage for confidence and likelihood ratio attacks.

**Abstract (Chinese)**

寻求更平坦极小值的优化算法，例如锐度感知最小化（SAM），被认为具有更好的泛化能力和对噪声的鲁棒性。我们探讨这些改进是否会影响成员隐私。令人惊讶的是，我们发现，尽管SAM在测试误差上更低，但它比经典SGD更容易受到成员推断攻击（MIA）的攻击，在多个数据集和攻击方法上均如此。这表明，SAM改善泛化的几何机制同时加剧了成员泄露。我们通过对记忆分数和影响分数的广泛分析来探究这一现象。我们的结果显示，SAM更善于捕捉非典型子模式，从而导致样本的记忆分数更高。相反，SGD更依赖于多数特征，在非典型子组上泛化更差，并且记忆更低。关键的是，SAM的这一特性可以与未见样本预测置信度的较低方差相关联，从而放大成员信号。最后，我们在完美插值线性体制下建模SAM，并理论上证明锐度正则化本质上降低了方差，从而为置信度和似然比攻击保证了更高的MIA优势。

---

### Memorization Through the Lens of Sample Gradients

- **Venue**: ICLR 2026 Poster
- **Authors**: Deepak Ravikumar, Efstathia Soufleri, Abolfazl Hashemi, Kaushik Roy
- **Keywords**: Memorization, Sample Gradients
- **OpenReview**: https://openreview.net/forum?id=jeTiBeW3iZ
- **PDF**: https://openreview.net/pdf?id=jeTiBeW3iZ

**Abstract**

Deep neural networks are known to often memorize underrepresented, hard examples, with implications for generalization and privacy.  Feldman & Zhang (2020) defined a rigorous notion of memorization. 
However it is prohibitively expensive to compute at scale because it requires training models both with and without the data point of interest in order to calculate the memorization score.
We observe that samples that are less memorized tend to be learned earlier in training, whereas highly memorized samples are learned later. 
Motivated by this observation, we introduce Cumulative Sample Gradient (CSG), a computationally efficient proxy for memorization. CSG is the gradient of the loss with respect to input samples, accumulated over the course of training.
The advantage of using input gradients is that per-sample gradients can be obtained with negligible overhead during training. The accumulation over training also reduces per-epoch variance and enables a formal link to memorization. Theoretically, we show that CSG is bounded by memorization and by learning time.
Tracking these gradients during training reveals a characteristic rise–peak–decline trajectory whose timing is mirrored by the model’s weight norm. This yields an early-stopping criterion that does not require a validation set: stop at the peak of the weight norm. This early stopping also enables our memorization proxy, CSG, to be up to five orders of magnitude more efficient than the memorization score from  Feldman & Zhang (2020).  It is also approximately 140 $\times$ and 10$\times$ faster than the prior state-of-the-art memorization proxies, input curvature and cumulative sample loss, while still aligning closely with the memorization score, exhibiting high correlation. Further, we develop Sample Gradient Assisted Loss (SGAL), a proxy that further improves alignment with memorization and is highly efficient to compute. Finally, we show that CSG attains state-of-the-art performance on practical dataset diagnostics, such as mislabeled-sample detection and enables bias discovery, providing a  theoretically grounded toolbox for studying memorization in deep networks.

**Abstract (Chinese)**

深度神经网络已知常常记忆代表性不足的难例，这对泛化能力和隐私具有重要影响。Feldman & Zhang (2020) 定义了记忆的一个严谨概念。然而，在大规模计算时其代价极高，因为计算记忆分数需要分别训练包含和不包含感兴趣数据点的模型。我们观察到，记忆较少的样本倾向于在训练早期被学习，而高度记忆的样本则在后期被学习。受此观察启发，我们引入了累积样本梯度 (CSG)，一种计算高效的记忆代理。CSG 是训练过程中相对于输入样本的损失梯度累积。使用输入梯度的优势在于，每个样本的梯度可以在训练期间以可忽略的开销获得。训练过程中的累积还降低了每个 epoch 的方差，并建立了与记忆的正式联系。理论上，我们证明 CSG 受记忆分数和学习时间的界定限制。在训练过程中跟踪这些梯度揭示了一个特征性的上升-峰值-下降轨迹，其时机与模型权重范数相呼应。这产生了一个不需要验证集的早停准则：在权重范数的峰值处停止。这种早停还使我们的记忆代理 CSG 比 Feldman & Zhang (2020) 的记忆分数高效高达五个数量级。它还比先前最先进的记忆代理（输入曲率和累积样本损失）分别快约 140 倍和 10 倍，同时仍与记忆分数紧密对齐，表现出高相关性。此外，我们开发了样本梯度辅助损失 (SGAL)，一种进一步改善与记忆对齐且计算高效的代理。最后，我们展示了 CSG 在实际数据集诊断任务（如错误标记样本检测）上达到了最先进性能，并实现了偏差发现，为研究深度网络中的记忆提供了一个理论基础的工具箱。

---

### No Caption, No Problem: Caption-Free Membership Inference via Model-Fitted Embeddings

- **Venue**: ICLR 2026 Poster
- **Authors**: Joonsung Jeon, Woo Jae Kim, Suhyeon Ha, Sooel Son, Sung-eui Yoon
- **Keywords**: Membership Inference, Data Privacy in Generative Models
- **OpenReview**: https://openreview.net/forum?id=KUXLrSXYPv
- **PDF**: https://openreview.net/pdf?id=KUXLrSXYPv

**Abstract**

Latent diffusion models have achieved remarkable success in high-fidelity text-to-image generation, but their tendency to memorize training data raises critical privacy and intellectual property concerns. Membership inference attacks (MIAs) provide a principled way to audit such memorization by determining whether a given sample was included in training. However, existing approaches assume access to ground-truth captions. This assumption fails in realistic scenarios where only images are available and their textual annotations remain undisclosed, rendering prior methods ineffective when substituted with vision-language model (VLM) captions. In this work, we propose MoFit , a caption-free MIA framework that constructs synthetic conditioning inputs that are explicitly overfitted to the target model's generative manifold. Given a query image, MoFit proceeds in two stages: (i) model-fitted surrogate optimization, where a perturbation applied to the image is optimized to construct a surrogate in regions of the model’s unconditional prior learned from member samples, and (ii) surrogate-driven embedding extraction, where a model-fitted embedding is derived from the surrogate and then used as a mismatched condition for the query image. This embedding amplifies conditional loss responses for member samples while leaving hold-outs relatively less affected, thereby enhancing separability in the absence of ground-truth captions. Our comprehensive experiments across multiple datasets and diffusion models demonstrate that MoFit consistently outperforms prior VLM-conditioned baselines and achieves performance competitive with caption-dependent methods.

**Abstract (Chinese)**

潜在扩散模型在高保真文本到图像生成中取得了显著成功，但它们记忆训练数据的倾向引发了关键的隐私和知识产权担忧。成员推断攻击（MIAs）提供了一种原则性方法，通过确定给定样本是否包含在训练中，来审计这种记忆行为。然而，现有的方法假设可以访问真实标签描述。这一假设在现实场景中失效，其中仅提供图像且其文本标注保持未公开，从而使得先前方法在使用视觉语言模型（VLM）描述替代时无效。在本工作中，我们提出MoFit，一种无描述的MIA框架，它构建明确过度拟合到目标模型生成流形的合成条件输入。给定一个查询图像，MoFit分为两个阶段进行：(i) 模型拟合代理优化，其中应用于图像的扰动被优化，以在从成员样本学习到的模型无条件先验区域中构建代理；(ii) 代理驱动嵌入提取，其中从代理中派生模型拟合嵌入，然后用作查询图像的不匹配条件。此嵌入放大了成员样本的条件损失响应，同时对留出样本的影响相对较小，从而在没有真实标签描述的情况下增强可分性。我们在多个数据集和扩散模型上的全面实验表明，MoFit始终优于先前的VLM条件基线，并实现了与依赖描述的方法相当的性能。

---

### Reducing information dependency does not cause training data privacy. Adversarially non-robust features do.

- **Venue**: ICLR 2026 Poster
- **Authors**: Rasmus Torp, Shailen Smith, Adam Breuer
- **Keywords**: Privacy, model inversion attacks, extraction attacks, adversarial examples, memorization, training data, causal inference, causality
- **OpenReview**: https://openreview.net/forum?id=BnEG8pn3pK
- **PDF**: https://openreview.net/pdf?id=BnEG8pn3pK

**Abstract**

In this paper, we challenge the prevailing view that information dependency (including rote memorization) drives training data exposure to image reconstruction attacks. We show that extensive exposure can persist without rote memorization and is instead caused by a tunable connection to adversarial robustness. We begin by presenting three surprising results: (1) recent defenses that inhibit reconstruction by Model Inversion Attacks (MIAs), which evaluate leakage under an idealized attacker, do not reduce standard measures of information dependency (HSIC); (2) models that maximally memorize their training datasets remain robust to MIA reconstruction; and (3) models trained without seeing 97% of the training pixels, where recent information-theoretic bounds give arbitrarily strong privacy guarantees under standard assumptions, can still be devastatingly reconstructed by MIA. 

To explain these findings, we provide causal evidence that privacy under MIA arises from what the adversarial examples literature calls "non-robust" features (generalizable but imperceptible and unstable features). We further show that recent MIA defenses obtain their privacy improvements by unintentionally shifting models toward such features. To establish this causal relationship, we introduce **A**n**t**i **A**dversarial **T**raining (**AT-AT**), a training regime that intentionally learns non-robust features to obtain both superior reconstruction defense and higher accuracy than state-of-the-art defenses. Our results revise the prevailing understanding of training data exposure and reveal a new privacy-robustness tradeoff.

**Abstract (Chinese)**

本文挑战了主流观点，即信息依赖性（包括死记硬背）驱动了对图像重建攻击的训练数据暴露。我们证明，广泛暴露可以在没有死记硬背的情况下持续存在，而是由与对抗鲁棒性的可调连接引起的。我们首先呈现三个令人惊讶的结果：(1) 最近的防御措施通过抑制模型反演攻击（MIAs）（这些攻击在理想化攻击者下评估泄漏）来抑制重建，但并未降低信息依赖性的标准度量（HSIC）；(2) 最大限度记忆其训练数据集的模型仍对MIA重建具有鲁棒性；以及(3) 在未看到97%的训练像素的情况下训练的模型，在标准假设下最近的信息论界限给出任意强的隐私保证，但仍可被MIA毁灭性地重建。

为了解释这些发现，我们提供了因果证据，即MIA下的隐私源于对抗样本文献中所谓的“非鲁棒”特征（可泛化但不可察觉且不稳定的特征）。我们进一步证明，最近的MIA防御通过无意地将模型转向此类特征来获得隐私改进。为了确立这种因果关系，我们引入了**反对抗训练** (**AT-AT**)，一种有意学习非鲁棒特征的训练方案，以获得比最先进防御更好的重建防御和更高的准确性。我们的结果修正了对训练数据暴露的普遍理解，并揭示了一种新的隐私-鲁棒性权衡。

---

### SMOTE and Mirrors: Exposing Privacy Leakage from Synthetic Minority Oversampling

- **Venue**: ICLR 2026 Poster
- **Authors**: Georgi Ganev, MohammadReza Nazari, Rees Davison, Amirhassan Fallah Dizche, XINMIN WU, Ralph Abbey, Jorge G Silva, Emiliano De Cristofaro
- **Keywords**: smote, synthetic data generation, privacy attacks
- **OpenReview**: https://openreview.net/forum?id=ZQSZMpsQKj
- **PDF**: https://openreview.net/pdf?id=ZQSZMpsQKj

**Abstract**

The Synthetic Minority Over-sampling Technique (SMOTE) is one of the most widely used methods for addressing class imbalance and generating synthetic data.
Despite its popularity, little attention has been paid to its privacy implications; yet, it is used in the wild in many privacy-sensitive applications.
In this work, we conduct the first systematic study of privacy leakage in SMOTE:
We begin by showing that prevailing evaluation practices, i.e., naive distinguishing and distance-to-closest-record metrics, completely fail to detect any leakage and that membership inference attacks (MIAs) can be instantiated with high accuracy.
Then, by exploiting SMOTE's geometric properties, we build two novel attacks with very limited assumptions: DistinSMOTE, which perfectly distinguishes real from synthetic records in augmented datasets, and ReconSMOTE, which reconstructs real minority records from synthetic datasets with perfect precision and recall approaching one under realistic imbalance ratios.
We also provide theoretical guarantees for both attacks.
Experiments on eight standard imbalanced datasets confirm the practicality and effectiveness of these attacks.
Overall, our work reveals that SMOTE is inherently non-private and disproportionately exposes minority records, highlighting the need to reconsider its use in privacy-sensitive applications and as a baseline for assessing the privacy of modern generative models.

**Abstract (Chinese)**

合成少数类过采样技术（SMOTE）是解决类别不平衡和生成合成数据的最广泛使用的方法之一。

尽管其流行程度很高，但对其隐私影响却鲜有关注；然而，它在许多隐私敏感应用中被广泛实际使用。

在本工作中，我们对 SMOTE 中的隐私泄露进行了首次系统性研究：

我们首先证明，现行的评估实践，即朴素区分和距离最近记录度量，完全无法检测任何泄露，并且成员推断攻击（MIAs）可以以高准确率实现。

然后，通过利用 SMOTE 的几何特性，我们构建了两种假设非常有限的新型攻击：DistinSMOTE，它能完美地区分增强数据集中的真实记录与合成记录；以及 ReconSMOTE，它能从合成数据集中重构真实少数类记录，在现实不平衡比率下具有完美精确率和接近一的召回率。

我们还为两种攻击提供了理论保证。

在八个标准不平衡数据集上的实验证实了这些攻击的实用性和有效性。

总体而言，我们的工作揭示了 SMOTE 本质上是非私有的，并且不成比例地暴露了少数类记录，这突显了在隐私敏感应用中以及作为评估现代生成模型隐私的基准时，需要重新考虑其使用的必要性。

---

### Silent Leaks: Implicit Knowledge Extraction Attack on RAG Systems

- **Venue**: ICLR 2026 Poster
- **Authors**: Yuhao Wang, Wenjie Qu, Shengfang Zhai, Yanze Jiang, Liu Zichen, Yue Liu, Yinpeng Dong, Jiaheng Zhang
- **Keywords**: security and privacy, security/privacy, red teaming
- **OpenReview**: https://openreview.net/forum?id=zfVICPB5Sv
- **PDF**: https://openreview.net/pdf?id=zfVICPB5Sv

**Abstract**

Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by incorporating external knowledge bases, but this may expose them to extraction attacks, leading to potential copyright and privacy risks.
However, existing extraction methods typically rely on malicious inputs such as prompt injection or jailbreaking, making them easily detectable via input- or output-level detection. 
In this paper, we introduce **I**mplicit **K**nowledge **E**xtraction **A**ttack (**IKEA**), which conducts *Knowledge Extraction* on RAG systems through benign queries.
Specifically, **IKEA** first leverages anchor concepts—keywords related to internal knowledge—to generate queries with a natural appearance, and then designs two mechanisms that lead anchor concepts to thoroughly "explore" the RAG's knowledge:
(1) Experience Reflection Sampling, which samples anchor concepts based on past query-response histories, ensuring their relevance to the topic; 
(2) Trust Region Directed Mutation, which iteratively mutates anchor concepts under similarity constraints to further exploit the embedding space.
Extensive experiments demonstrate **IKEA**'s effectiveness under various defenses, surpassing baselines by over 80% in extraction efficiency and 90\% in attack success rate. Moreover, the substitute RAG system built from **IKEA**'s extractions shows close performance to the original RAG and outperforms those based on baselines across multiple evaluation tasks, underscoring the stealthy copyright infringement risk in RAG systems.

**Abstract (Chinese)**

检索增强生成 (RAG) 系统通过整合外部知识库来增强大语言模型 (LLMs)，但这可能使它们暴露于提取攻击，从而导致潜在的版权和隐私风险。然而，现有的提取方法通常依赖于恶意输入，如提示注入或越狱，这使得它们容易通过输入级或输出级检测被发现。在本文中，我们引入了**隐式知识提取攻击** (**IKEA**)，它通过良性查询对 RAG 系统进行*知识提取*。具体而言，**IKEA** 首先利用锚概念——与内部知识相关的关键词——生成外观自然的查询，然后设计两种机制引导锚概念彻底“探索” RAG 的知识：(1) 经验反思采样，它基于过去的查询-响应历史采样锚概念，确保其与主题的相关性；(2) 信任区域定向变异，它在相似性约束下迭代变异锚概念，以进一步利用嵌入空间。大量实验证明了 **IKEA** 在各种防御下的有效性，在提取效率上超过基线 80% 以上，在攻击成功率上超过 90%。此外，从 **IKEA** 的提取构建的替代 RAG 系统表现出与原始 RAG 相近的性能，并在多个评估任务上优于基于基线的系统，这突显了 RAG 系统中的隐秘版权侵权风险。

---
