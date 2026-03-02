# unlearning_data_removal

**Description**: 机器遗忘/数据删除与合规。包括 unlearning、right-to-be-forgotten、data removal、certifiable deletion、遗忘评测与遗忘-效用权衡等。

**Paper count**: 32

---

### Gaussian certified unlearning in high dimensions: A hypothesis testing approach

- **Venue**: ICLR 2026 Oral
- **Authors**: Aaradhya Pandey, Arnab Auddy, Haolin Zou, Arian Maleki, Sanjeev Kulkarni
- **Keywords**: Machine unlearning in high dimensions, Proportional asymptotics, High dimensional statistical theory, Privacy–accuracy tradeoff, Hypothesis testing, Gaussian noise calibration, Newton method
- **OpenReview**: https://openreview.net/forum?id=0FJYicpOj0
- **PDF**: https://openreview.net/pdf?id=0FJYicpOj0

**Abstract**

Machine unlearning seeks to efficiently remove the influence of selected data while preserving generalization. Significant progress has been made in low dimensions, where the dimension of the parameter $p$ is  much smaller than the sample size $n$, but high dimensions, including proportional regimes $p \sim n$, pose serious theoretical challenges as standard optimization assumptions of $\Omega(1)$ strong convexity and $O(1)$ smoothness of the per-example loss $f$ rarely hold simultaneously in proportional regimes $p\sim n$.
In this work, we introduce $\varepsilon$-Gaussian certifiability, a canonical and robust notion well-suited to high-dimensional regimes, that optimally captures a broad class of noise adding mechanisms. Then we theoretically analyze the performance of a widely used unlearning algorithm based on one step of the Newton method in the high-dimensional setting described above. Our analysis shows that a single Newton step, followed by a well-calibrated Gaussian noise, is sufficient to achieve both privacy and accuracy in this setting. This result stands in sharp contrast to the only prior work that analyzes machine unlearning in high dimensions \citet{zou2025certified}, which relaxes some of the standard optimization assumptions for high-dimensional applicability, but operates under the notion of $\varepsilon$-certifiability. That work concludes %that a single Newton step is insufficient even for removing a single data point, and
that at least two steps are required to ensure both privacy and accuracy. Our result leads us to conclude that the discrepancy in the number of steps arises because of the sub optimality of the notion of $\varepsilon$-certifiability and its incompatibility with noise adding mechanisms, which $\varepsilon$-Gaussian certifiability is able to overcome optimally.

**Abstract (Chinese)**

机器遗忘旨在高效移除选定数据的影响，同时保持泛化能力。在低维情况下，即参数维度 $p$ 远小于样本大小 $n$ 时，已取得显著进展，但高维情况（包括比例制度 $p \sim n$）带来了严重的理论挑战，因为每个样本损失 $f$ 的标准优化假设——$\Omega(1)$ 强凸性和 $O(1)$ 平滑性——在比例制度 $p\sim n$ 中很少同时成立。

在本工作中，我们引入了 $\varepsilon$-高斯可证明性，这是一个规范且鲁棒的概念，非常适合高维制度，能够最优地捕捉一类广泛的噪声添加机制。随后，我们在上述高维设定下理论分析了一种广泛使用的遗忘算法，该算法基于牛顿法的一步迭代。我们的分析表明，在该设定中，单个牛顿步迭代后接上适当校准的高斯噪声，即足以同时实现隐私和准确性。这一结果与唯一先前分析高维机器遗忘的工作 \citet{zou2025certified} 形成鲜明对比，该工作放宽了一些标准优化假设以适用于高维，但采用的是 $\varepsilon$-可证明性概念。该工作得出结论，认为至少需要两步迭代才能同时确保隐私和准确性。我们的结果表明，步数差异源于 $\varepsilon$-可证明性的次优性及其与噪声添加机制的不兼容性，而 $\varepsilon$-高斯可证明性能够最优地克服这一问题。

---

### Attention Smoothing Is All You Need For Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Saleh Zare Zade, Xiangyu Zhou, Sijia Liu, Dongxiao Zhu
- **Keywords**: Large Language Model, Large Language Model Unlearning, Self-distillation, Attention Smoothing
- **OpenReview**: https://openreview.net/forum?id=sX9HbELwLO
- **PDF**: https://openreview.net/pdf?id=sX9HbELwLO

**Abstract**

Large Language Models are prone to memorizing sensitive, copyrighted, or hazardous content, posing significant privacy and legal concerns. Retraining from scratch is computationally infeasible, whereas current unlearning methods exhibit unstable trade-offs between forgetting and utility, frequently producing incoherent outputs on forget prompts and failing to generalize due to the persistence of lexical-level and semantic-level associations in attention. We propose Attention Smoothing Unlearning (ASU), a principled framework that casts unlearning as self-distillation from a forget-teacher derived from the model’s own attention. By increasing the softmax temperature, ASU flattens attention distributions and directly suppresses the lexical-level and semantic-level associations responsible for reconstructing memorized knowledge. This results in a bounded optimization objective that erases factual information yet maintains coherence in responses to forget prompts. Empirical evaluation on TOFU, MUSE, and WMDP, along with real-world and continual unlearning scenarios across question answering and text completion, demonstrates that ASU outperforms the baselines for most of the unlearning scenarios, delivering robust unlearning with minimal loss of model utility.

**Abstract (Chinese)**

大型语言模型容易记忆敏感的、受版权保护的或有害的内容，从而引发重大的隐私和法律担忧。从头重新训练在计算上不可行，而当前的遗忘方法在遗忘与效用之间表现出不稳定的权衡，经常在遗忘提示上产生不连贯的输出，并且由于注意机制中词法级和语义级关联的持久性而无法泛化。我们提出注意平滑遗忘（ASU），这是一个原则性框架，将遗忘表述为从模型自身注意机制派生的遗忘教师的自蒸馏。通过增加softmax温度，ASU平滑注意分布，并直接抑制负责重构记忆知识的词法级和语义级关联。这导致了一个有界优化目标，该目标擦除事实信息，同时保持对遗忘提示的响应连贯性。在TOFU、MUSE和WMDP上的实证评估，以及跨问答和文本补全的真实世界和持续遗忘场景，表明ASU在大多数遗忘场景中优于基线方法，提供鲁棒的遗忘并最小化模型效用的损失。

---

### Closing the Safety Gap: Surgical Concept Erasure in Visual Autoregressive Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Xinhao Zhong, Yimin Zhou, Zhiqi Zhang, Junhao Li, Sun Yi, Bin Chen, Shu-Tao Xia, Xuan Wang, Ke Xu
- **Keywords**: visual autoregressive model, concept erasure
- **OpenReview**: https://openreview.net/forum?id=tlYSbw5GXY
- **PDF**: https://openreview.net/pdf?id=tlYSbw5GXY

**Abstract**

The rapid progress of visual autoregressive (VAR) models has brought new opportunities for text-to-image generation, but also heightened safety concerns. Existing concept erasure techniques, primarily designed for diffusion models, fail to generalize to VARs due to their next-scale token prediction paradigm. In this paper, we first propose a novel VAR Erasure framework **VARE** that enables stable concept erasure in VAR models by leveraging auxiliary visual tokens to reduce fine-tuning intensity. Building upon this, we introduce **S-VARE**, a novel and effective concept erasure method designed for VAR, which incorporates a filtered cross entropy loss to precisely identify and minimally adjust unsafe visual tokens, along with a preservation loss to maintain semantic fidelity, addressing the issues such as language drift and reduced diversity introduce by na\"ive fine-tuning. Extensive experiments demonstrate that our approach achieves surgical concept erasure while preserving generation quality, thereby closing the safety gap in autoregressive text-to-image generation by earlier methods.

**Abstract (Chinese)**

视觉自回归 (VAR) 模型的快速发展为文本到图像生成带来了新的机遇，但也加剧了安全担忧。现有的概念擦除技术主要针对扩散模型设计，由于 VAR 的下一尺度令牌预测范式，无法泛化到 VAR 模型。本文首先提出了一种新型 VAR 擦除框架 **VARE**，通过利用辅助视觉令牌降低微调强度，从而在 VAR 模型中实现稳定的概念擦除。在此基础上，我们引入了 **S-VARE**，这是一种专为 VAR 设计的新颖有效的概念擦除方法，它融入了过滤交叉熵损失，以精确识别并最小化调整不安全视觉令牌，同时引入保持损失以维持语义保真度，从而解决朴素微调引入的语言漂移和多样性降低等问题。广泛的实验表明，我们的方法实现了外科手术式概念擦除，同时保留了生成质量，从而弥合了先前方法在自回归文本到图像生成中的安全差距。

---

### Co-occurring Associated REtained concepts in Diffusion Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Miso Kim, Georu Lee, Yunji Kim, Hoki Kim, Jinseong Park, Woojin Lee
- **Keywords**: unlearning, diffusion, concept erasure, safety
- **OpenReview**: https://openreview.net/forum?id=Ryc7jKP6H9
- **PDF**: https://openreview.net/pdf?id=Ryc7jKP6H9

**Abstract**

Unlearning has emerged as a key technique to mitigate harmful content generation in diffusion models. However, existing methods often remove not only the target concept, but also benign co-occurring concepts. Unlearning nudity can unintentionally suppress the concept of person, preventing a model from generating images with person. We define these undesirably suppressed co-occurring concepts that must be preserved $\textbf{CARE}$ ($\textbf{C}$o-occurring $\textbf{A}$ssociated $\textbf{RE}$tained concepts). Then, we introduce the  $\textbf{CARE score}$, a general metric that directly quantifies their preservation across unlearning tasks. With this foundation, we propose $\textbf{ReCARE}$ ($\textbf{R}$obust $\textbf{e}$rasure for $\textbf{CARE}$), a framework that explicitly safeguards CARE while erasing only the target concept. ReCARE automatically constructs the CARE-set, a curated vocabulary of benign co-occurring tokens extracted from target images, and leverages this vocabulary during training for stable unlearning. Extensive experiments across various target concepts ($\textit{Nudity}$, $\textit{Van Gogh}$ style, and $\textit{Tench}$ object) demonstrate that ReCARE achieves overall state-of-the-art performance in balancing robust concept erasure, overall utility, and CARE preservation.

**Abstract (Chinese)**

遗忘技术已成为缓解扩散模型中生成有害内容的关键方法。然而，现有的方法往往不仅移除目标概念，还移除了良性共现概念。遗忘裸体内容可能会无意中抑制“人”的概念，从而阻止模型生成包含人的图像。我们将这些不应被抑制但必须保留的共现概念定义为\textbf{CARE}（\textbf{C}o-occurring \textbf{A}ssociated \textbf{RE}tained concepts）。然后，我们引入\textbf{CARE score}，一个通用度量，直接量化其在各种遗忘任务中的保留情况。在此基础上，我们提出\textbf{ReCARE}（\textbf{R}obust \textbf{e}rasure for \textbf{CARE}），一个框架，在仅擦除目标概念的同时明确保护CARE。ReCARE自动构建CARE-set，这是一个从目标图像中提取的良性共现令牌的精选词汇表，并在训练过程中利用该词汇表实现稳定的遗忘。在各种目标概念（\textit{Nudity}、\textit{Van Gogh}风格和\textit{Tench}物体）上的广泛实验表明，ReCARE在平衡鲁棒概念擦除、整体效用和CARE保留方面实现了总体最先进的性能。

---

### Continual Unlearning for Text-to-Image Diffusion Models: A Regularization Perspective

- **Venue**: ICLR 2026 Poster
- **Authors**: Justin Lee, Zheda Mai, Jinsu Yoo, Chongyu Fan, Cheng Zhang, Wei-Lun Chao
- **Keywords**: Continual Unlearning, Diffusion Model, Image Generation, Machine Unlearning
- **OpenReview**: https://openreview.net/forum?id=BsY20r9FOM
- **PDF**: https://openreview.net/pdf?id=BsY20r9FOM

**Abstract**

Machine unlearning—the ability to remove designated concepts from a pre-trained
model—has advanced rapidly, particularly for text-to-image diffusion models.
However, existing methods typically assume that unlearning requests arrive all
at once, whereas in practice they often arrive sequentially. We present the first
systematic study of continual unlearning in text-to-image diffusion models and
show that popular unlearning methods suffer from rapid utility collapse: after only
a few requests, models forget retained knowledge and generate degraded images.
We trace this failure to cumulative parameter drift from the pre-training weights
and argue that regularization is crucial to addressing it. To this end, we study a
suite of add-on regularizers that (1) mitigate drift and (2) remain compatible with
existing unlearning methods. Beyond generic regularizers, we show that semantic
awareness is essential for preserving concepts close to the unlearning target, and
propose a gradient-projection method that constrains parameter drift orthogonal
to their subspace. This substantially improves continual unlearning performance
and is complementary to other regularizers for further gains. Taken together, our
study establishes continual unlearning as a fundamental challenge in text-to-image
generation and provides insights, baselines, and open directions for advancing safe
and accountable generative AI.

**Abstract (Chinese)**

机器遗忘——即从预训练模型中移除指定概念的能力——已快速发展，特别是针对文本到图像扩散模型。然而，现有的方法通常假设遗忘请求一次性到达，而在实践中，它们往往顺序到达。我们首次对文本到图像扩散模型中的连续遗忘进行了系统研究，并展示了流行遗忘方法遭受快速效用崩溃：仅经过几个请求后，模型就会忘记保留的知识并生成退化图像。我们将这一失败追溯到从预训练权重中的累积参数漂移，并论证正则化对于解决这一问题至关重要。为此，我们研究了一系列附加正则化器，这些正则化器（1）缓解漂移并（2）与现有遗忘方法兼容。除了通用正则化器之外，我们展示了语义感知对于保留接近遗忘目标的概念至关重要，并提出了一种梯度投影方法，该方法将参数漂移约束在其子空间的正交方向上。这显著改善了连续遗忘性能，并与其他正则化器互补以获得进一步提升。总之，我们的研究确立了连续遗忘作为文本到图像生成中的一个基本挑战，并为推进安全且可问责的生成式AI提供了洞见、基准和开放方向。

---

### DRAGON: Guard LLM Unlearning in Context via Negative Detection and Reasoning

- **Venue**: ICLR 2026 Poster
- **Authors**: Yaxuan Wang, Chris Yuhao Liu, Quan Liu, Jinlong Pang, Wei Wei, Yujia Bao, Yang Liu
- **Keywords**: LLM Unlearning, In-context Learning
- **OpenReview**: https://openreview.net/forum?id=vQLUAkl5SG
- **PDF**: https://openreview.net/pdf?id=vQLUAkl5SG

**Abstract**

Unlearning in Large Language Models (LLMs) is crucial for protecting private data and removing harmful knowledge. Most existing approaches rely on fine-tuning to balance unlearning efficiency with general language capabilities. However, these methods typically require training or access to retain data, which is often unavailable in real world scenarios. Although these methods can perform well when both forget and retain data are available, few works have demonstrated equivalent capability in more practical, data-limited scenarios. To overcome these limitations, we propose Detect-Reasoning Augmented GeneratiON (DRAGON),  a systematic, reasoning-based framework that utilizes in-context chain-of-thought (CoT) instructions to guard deployed LLMs before inference. Instead of modifying the base model, DRAGON leverages the inherent instruction-following ability of LLMs and introduces a lightweight detection module to identify forget-worthy prompts without any retain data. These are then routed through a dedicated CoT guard model to enforce safe and accurate in-context intervention. To robustly evaluate unlearning performance, we introduce novel metrics for unlearning performance and the continual unlearning setting. Extensive experiments across three representative unlearning tasks validate the effectiveness of DRAGON, demonstrating its strong unlearning capability, scalability, and applicability in practical scenarios.

**Abstract (Chinese)**

大语言模型（LLMs）中的遗忘对于保护私有数据和移除有害知识至关重要。大多数现有方法依赖于微调来平衡遗忘效率与通用语言能力。然而，这些方法通常需要训练或访问保留数据，这在现实世界场景中往往不可用。尽管这些方法在遗忘数据和保留数据均可用时表现良好，但很少有工作在更实际的数据受限场景中展示了等效能力。为了克服这些局限性，我们提出了Detect-Reasoning Augmented GeneratiON（DRAGON），这是一个系统性的、基于推理的框架，它利用上下文中的思维链（CoT）指令在推理前守护已部署的LLMs。DRAGON 不修改基础模型，而是利用LLMs固有的指令跟随能力，并引入一个轻量级检测模块来识别值得遗忘的提示，而无需任何保留数据。这些提示随后通过专用的CoT守护模型进行路由，以强制执行安全且准确的上下文干预。为了稳健地评估遗忘性能，我们引入了新型指标，用于遗忘性能和持续遗忘设置。在三个代表性遗忘任务上的广泛实验验证了DRAGON的有效性，展示了其强大的遗忘能力、可扩展性和在实际场景中的适用性。

---

### DUET: Distilled LLM Unlearning from an Efficiently Contextualized Teacher

- **Venue**: ICLR 2026 Poster
- **Authors**: Yisheng Zhong, Zhengbang Yang, Zhuangdi Zhu
- **Keywords**: LLM Unlearning, Knowledge Distillation, Teacher–Student Learning, Utility Preservation, Data Efficiency, Robustness, Safety and Alignment
- **OpenReview**: https://openreview.net/forum?id=Xa6QRrXrKX
- **PDF**: https://openreview.net/pdf?id=Xa6QRrXrKX

**Abstract**

LLM unlearning is a technique to remove the impacts of undesirable knowledge from the model without retraining from scratch, which is indispensable towards trustworthy AI. Existing unlearning methods face significant limitations: conventional tuning-based unlearning is computationally heavy and prone to catastrophic forgetting. In contrast, in-contextualized unlearning is lightweight for precise unlearning but vulnerable to prompt removal or reverse engineering attacks. In response, we propose Distilled Unlearning from an Efficient Teacher (DUET), a novel distillation-based unlearning method that combines the merits of these two lines of work. It learns a student model to imitate the behavior of a prompt-steered teacher that effectively refuses undesirable knowledge generation while preserving general domain knowledge. Extensive evaluations on existing benchmarks with our enriched evaluation protocols demonstrated that DUET achieves significantly higher performance in both forgetting and utility preservation, while being orders of magnitude more data-efficient than state-of-the-art unlearning methods.

**Abstract (Chinese)**

LLM 遗忘是一种从模型中移除不良知识影响的技术，而无需从头重新训练，这对于可信 AI 至关重要。现有的遗忘方法面临显著局限性：传统的基于微调的遗忘计算开销巨大，且易发生灾难性遗忘。相比之下，上下文内遗忘轻量级且精确，但易受提示移除或逆向工程攻击的影响。为此，我们提出了一种新型基于蒸馏的遗忘方法——来自高效教师的蒸馏遗忘（DUET），它结合了这两类工作的优点。该方法训练一个学生模型来模仿由提示引导的教师模型的行为，该教师模型有效拒绝生成不良知识，同时保留通用领域知识。在现有基准上的广泛评估，使用我们丰富的评估协议，证明 DUET 在遗忘效果和效用保留方面取得了显著更高的性能，同时比最先进的遗忘方法数据效率高几个数量级。

---

### Distributional Machine Unlearning via Selective Data Removal

- **Venue**: ICLR 2026 Poster
- **Authors**: Youssef Allouah, Rachid Guerraoui, Sanmi Koyejo
- **Keywords**: unlearning, theory, privacy, sample complexity, machine learning, statistical learning
- **OpenReview**: https://openreview.net/forum?id=IPqUBL4R9x
- **PDF**: https://openreview.net/pdf?id=IPqUBL4R9x

**Abstract**

Machine learning systems increasingly face requirements to remove entire domains of information—such as toxic language or biases—rather than individual user data. This task presents a dilemma: full removal of the unwanted domain data is computationally expensive, while random partial removal is statistically inefficient. We find that a domain's statistical influence is often concentrated in a small subset of its data samples, suggesting a path between ineffective partial removal and unnecessary complete removal. We formalize this as distributional unlearning: a framework to select a small subset that balances forgetting an unwanted distribution while preserving a desired one. Using Kullback-Leibler divergence constraints, we derive the exact removal-preservation Pareto frontier for Gaussian distributions and prove that models trained on the edited data achieve corresponding log-loss bounds. We propose a distance-based selection algorithm and show it is quadratically more sample-efficient than random removal in the challenging low-divergence regime. Experiments across synthetic, text, and image datasets (Jigsaw, CIFAR-10, SMS spam) show our method requires 15–82% less deletion than full removal for  strong unlearning effects, e.g., halving initial forget set accuracy. Ultimately, by showing a small forget set often suffices, our framework lays the foundations for more scalable and rigorous subpopulation unlearning.

**Abstract (Chinese)**

机器学习系统日益面临移除整个信息域（如有毒语言或偏见）而非个别用户数据的诉求。这一任务面临两难：完全移除不需要域数据计算代价高昂，而随机部分移除则统计效率低下。我们发现，一个域的统计影响往往集中在其数据样本的一小部分子集中，这为无效的部分移除与不必要的完全移除之间开辟了一条中间路径。我们将其形式化为分布式遗忘：一种选择小规模子集的框架，以平衡遗忘不需要分布的同时保留期望分布。利用 Kullback-Leibler 散度约束，我们推导出高斯分布的精确移除-保留 Pareto 前沿，并证明在编辑数据上训练的模型可实现相应的对数损失界。我们提出一种基于距离的选择算法，并在具有挑战性的低散度区域证明其样本效率比随机移除高二次方级。跨合成、文本和图像数据集（Jigsaw、CIFAR-10、SMS spam）的实验显示，我们的方法在实现强遗忘效果（如将初始遗忘集准确率减半）时，仅需全移除的 15–82% 删除量。最终，通过证明小规模遗忘集往往足矣，我们的框架为更具可扩展性和严谨性的子群体遗忘奠定了基础。

---

### Downgrade to Upgrade: Optimizer Simplification Enhances Robustness in LLM Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Yicheng Lang, Yihua Zhang, Chongyu Fan, Changsheng Wang, Jinghan Jia, Sijia Liu
- **Keywords**: LLM Unlearning, Robustness, Zeroth-Order Optimization
- **OpenReview**: https://openreview.net/forum?id=Sswng2ToR4
- **PDF**: https://openreview.net/pdf?id=Sswng2ToR4

**Abstract**

Large language model (LLM) unlearning aims to surgically remove the influence of undesired data or knowledge from an existing model while preserving its utility on unrelated tasks. This paradigm has shown promise in addressing privacy and safety concerns. However, recent findings reveal that unlearning effects are often *fragile*: post-unlearning manipulations such as weight quantization or fine-tuning can quickly neutralize the intended forgetting. Prior efforts to improve robustness primarily reformulate unlearning objectives by explicitly assuming the role of vulnerability sources.  In this work, we take a different perspective by investigating the role of the *optimizer*, independent of unlearning objectives and formulations, in shaping unlearning robustness. We show that the "*grade*" of the optimizer, defined by the level of information it exploits, ranging from zeroth-order (gradient-free) to first-order (gradient-based) to second-order (Hessian-based), is tightly linked to the resilience of unlearning. Surprisingly, we find that downgrading the optimizer, such as using zeroth-order methods or compressed-gradient variants (*e.g.,* gradient sign-based optimizers), often leads to stronger robustness. While these optimizers produce noisier and less precise updates, they encourage convergence to harder-to-disturb basins in the loss landscape, thereby resisting post-training perturbations. By connecting zeroth-order methods with randomized smoothing, we further highlight their natural advantage for robust unlearning.  Motivated by these insights, we propose a *hybrid optimizer* that combines first-order and zeroth-order updates, preserving unlearning efficacy while enhancing robustness. Extensive experiments on the MUSE and WMDP benchmarks, across multiple LLM unlearning algorithms, validate that our approach achieves more resilient forgetting without sacrificing unlearning quality.

**Abstract (Chinese)**

大语言模型（LLM）遗忘旨在外科手术式地从现有模型中移除不期望数据或知识的影响，同时保留其在无关任务上的效用。这一范式在解决隐私和安全问题方面显示出潜力。然而，最近的研究发现，遗忘效果往往是*脆弱的*：遗忘后的操纵，如权重量化或微调，可以迅速中和预期的遗忘。先前改善鲁棒性的努力主要通过明确假设漏洞来源的角色来重新表述遗忘目标。在这项工作中，我们从不同视角出发，调查*优化器*在塑造遗忘鲁棒性中的作用，该作用独立于遗忘目标和表述。我们表明，优化器的“*阶*”，由其利用的信息水平定义，从零阶（无梯度）到一阶（基于梯度）到二阶（基于Hessian），与遗忘的鲁棒性紧密相关。令人惊讶的是，我们发现降级优化器，例如使用零阶方法或压缩梯度变体（*如*，基于梯度符号的优化器），往往导致更强的鲁棒性。虽然这些优化器产生更噪声和更不精确的更新，但它们鼓励收敛到损失景观中更难扰动的盆地，从而抵抗遗忘后扰动。通过将零阶方法与随机平滑联系起来，我们进一步突显了它们在鲁棒遗忘方面的天然优势。受这些洞见启发，我们提出了一种*混合优化器*，它结合了一阶和零阶更新，在保留遗忘功效的同时增强鲁棒性。在MUSE和WMDP基准上的广泛实验，跨越多种LLM遗忘算法，验证了我们的方法实现了更鲁棒的遗忘，而不牺牲遗忘质量。

---

### Dual-Space Smoothness for Robust and Balanced LLM Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Han Yan, Zheyuan Liu, Meng Jiang
- **Keywords**: AI safety, Large Language Model Unlearning, Robustness, Jailbreak Attacks, LLM Safety, Relearning Attack
- **OpenReview**: https://openreview.net/forum?id=VIMW3eys6x
- **PDF**: https://openreview.net/pdf?id=VIMW3eys6x

**Abstract**

As large language models evolve, Machine Unlearning has emerged to address growing concerns around user privacy, copyright infringement, and overall safety. Yet state-of-the-art (SOTA) unlearning methods often suffer from catastrophic forgetting and metric imbalance, for example, by over-optimizing one objective (e.g., unlearning effectiveness, utility preservation, or privacy protection) at the expense of others. In addition, small perturbations in the representation or parameter space can be exploited by relearn and jailbreak attacks. To address these challenges, we propose PRISM, a unified framework that enforces dual-space smoothness in representation and parameter spaces to improve robustness and balance unlearning metrics. PRISM consists of two smoothness optimization stages: (i) a representation space stage that employs a robustly trained probe to defend against jailbreak attacks, and (ii) a parameter-space stage that decouples retain–forget gradient conflicts, reduces imbalance, and smooths the parameter space to mitigate relearning attacks. Extensive experiments on WMDP and MUSE, across conversational-dialogue and continuous-text settings, show that PRISM outperforms SOTA baselines under multiple attacks while achieving a better balance among key metrics.

**Abstract (Chinese)**

随着大型语言模型的演进，机器遗忘技术应运而生，以应对用户隐私、版权侵权以及整体安全日益增长的担忧。然而，最先进（SOTA）的遗忘方法往往遭受灾难性遗忘和指标不平衡的问题，例如，通过过度优化一个目标（例如，遗忘效果、效用保持或隐私保护）而牺牲其他目标。此外，表示空间或参数空间中的小扰动可能被重新学习和越狱攻击所利用。为应对这些挑战，我们提出PRISM，一个统一的框架，该框架在表示空间和参数空间中强制执行双空间平滑，以提升鲁棒性和平衡遗忘指标。PRISM由两个平滑优化阶段组成：(i) 表示空间阶段，该阶段采用鲁棒训练的探针来防御越狱攻击；(ii) 参数空间阶段，该阶段解耦保留-遗忘梯度冲突、减少不平衡，并平滑参数空间以缓解重新学习攻击。在WMDP和MUSE上的广泛实验，涵盖对话式和连续文本设置，表明PRISM在多种攻击下优于SOTA基线，同时在关键指标间实现了更好的平衡。

---

### Erase or Hide? Suppressing Spurious Unlearning Neurons for Robust Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Nakyeong Yang, Dong-Kyum Kim, Jea Kwon, Minsung Kim, Kyomin Jung, Meeyoung Cha
- **Keywords**: Unlearning, AI Safety, Interpretability
- **OpenReview**: https://openreview.net/forum?id=z2zFk9jYpw
- **PDF**: https://openreview.net/pdf?id=z2zFk9jYpw

**Abstract**

Large language models trained on web-scale data can memorize private or sensitive knowledge, raising significant privacy risks.
Although some unlearning methods mitigate these risks, they remain vulnerable to "relearning" during subsequent training, allowing a substantial portion of forgotten knowledge to resurface.
In this paper, we show that widely used unlearning methods cause shallow alignment: instead of faithfully erasing target knowledge, they generate spurious unlearning neurons that amplify negative influence to hide it.
To overcome this limitation, we introduce Ssiuu, a new class of unlearning methods that employs attribution-guided regularization to prevent spurious negative influence and faithfully remove target knowledge.
Experimental results confirm that our method reliably erases target knowledge and outperforms strong baselines across two practical retraining scenarios: (1) adversarial injection of private data, and (2) benign attack using an instruction-following benchmark.
Our findings highlight the necessity of robust and faithful unlearning methods for safe deployment of language models.

**Abstract (Chinese)**

在网络规模数据上训练的大型语言模型可能会记忆私人或敏感知识，从而引发重大的隐私风险。尽管一些遗忘方法缓解了这些风险，但它们在后续训练中仍易受“重新学习”的影响，导致大量被遗忘的知识重新浮现。在本文中，我们证明了广泛使用的遗忘方法会导致浅层对齐：它们并非忠实地擦除目标知识，而是生成虚假的遗忘神经元，通过放大负面影响来隐藏它。为了克服这一局限性，我们引入了Ssiuu，这是一类新型遗忘方法，它采用归因引导的正则化来防止虚假负面影响，并忠实地移除目标知识。实验结果证实，我们的方法可靠地擦除了目标知识，并在两个实际再训练场景中优于强大的基线：(1) 私人数据的对抗性注入，以及(2) 使用指令跟随基准的良性攻击。我们的发现突显了稳健且忠实的遗忘方法对于语言模型安全部署的必要性。

---

### Explainable LLM Unlearning through Reasoning

- **Venue**: ICLR 2026 Poster
- **Authors**: Junfeng Liao, Qizhou Wang, Shanshan Ye, Xin Yu, Ling Chen, Zhen Fang
- **Keywords**: LLM Unlearning
- **OpenReview**: https://openreview.net/forum?id=wec4qy2XIF
- **PDF**: https://openreview.net/pdf?id=wec4qy2XIF

**Abstract**

LLM unlearning is essential for mitigating safety, copyright, and privacy concerns in pre-trained Large Language Models (LLMs). Compared to preference alignment, it offers a more explicit way by removing undesirable knowledge characterized by specific unlearning datasets. 
In previous works, Gradient Ascent (GA) and its variants have shown promise for implementing unlearning, yet their untargeted nature results in unintended degradation of general capabilities, incomplete removal of knowledge, and the generation of incoherent responses, among many others. We argue that these issues stem from the absence of explicit guidance on what and how models should unlearn.
To fill this gap, we introduce a novel unlearning target, *reasoning-based unlearning target*, which satisfies both the specified unlearning scope and the specified post-unlearning response. Building on this, we propose *Targeted Reasoning Unlearning* (TRU), which leverages reasoning-based unlearning target as guidance. We employ the target using a cross-entropy supervised loss combined with a GA-based loss, enabling the model to learn reasoning ability for precise knowledge removal while preserving unrelated abilities.
We evaluate TRU against strong baselines across multiple benchmarks and LLM backbones, and find that it achieves more reliable unlearning while preserving general capabilities. Moreover, TRU exhibits superior robustness under diverse attack scenarios, stemming from the reasoning ability learned through reasoning-based targets. Overall, our study establishes reasoning-augmented unlearning as a practical paradigm for reliable and explainable LLM unlearning.

**Abstract (Chinese)**

LLM 遗忘对于缓解预训练大语言模型（LLMs）中的安全、版权和隐私问题至关重要。与偏好对齐相比，它通过移除由特定遗忘数据集表征的不期望知识，提供了一种更明确的方式。

在先前工作中，梯度上升（GA）及其变体在实现遗忘方面显示出潜力，然而其非目标性导致了通用能力意外退化、知识移除不完全以及生成不连贯响应等诸多问题。我们认为，这些问题源于缺乏关于模型应遗忘什么以及如何遗忘的明确指导。

为填补这一空白，我们引入了一种新型遗忘目标，即*基于推理的遗忘目标*，它同时满足指定的遗忘范围和遗忘后的指定响应。在此基础上，我们提出*目标推理遗忘*（TRU），它利用基于推理的遗忘目标作为指导。我们使用交叉熵监督损失结合基于 GA 的损失来采用该目标，使模型学习推理能力以精确移除知识，同时保留无关能力。

我们在多个基准和 LLM 骨干模型上将 TRU 与强大基线进行评估，发现它在保留通用能力的同时实现了更可靠的遗忘。此外，TRU 在多种攻击场景下表现出色鲁棒性，这源于通过基于推理目标学习到的推理能力。总体而言，我们的研究确立了推理增强遗忘作为可靠且可解释 LLM 遗忘的实用范式。

---

### FaLW: A Forgetting-aware Loss Reweighting for Long-tailed Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Liheng Yu, Zhe Zhao, Yuxuan Wang, Pengkun Wang, Xiaofeng Cao, Binwu Wang, Yang Wang
- **Keywords**: Long-tailed learning, Unlearning, Fairness
- **OpenReview**: https://openreview.net/forum?id=kBnvzwO5pN
- **PDF**: https://openreview.net/pdf?id=kBnvzwO5pN

**Abstract**

Machine unlearning, which aims to efficiently remove the influence of specific data from trained models, is crucial for upholding data privacy regulations like the ``right to be forgotten". However, existing research predominantly evaluates unlearning methods on relatively balanced forget sets. This overlooks a common real-world scenario where data to be forgotten, such as a user's activity records, follows a long-tailed distribution. Our work is the first to investigate this critical research gap. We find that in such long-tailed settings, existing methods suffer from two key issues: Heterogeneous Unlearning Deviation and Skewed Unlearning Deviation. To address these challenges, we propose FaLW, a plug-and-play, instance-wise dynamic loss reweighting method. FaLW innovatively assesses the unlearning state of each sample by comparing its predictive probability to the distribution of unseen data from the same class. Based on this, it uses a forgetting-aware reweighting scheme, modulated by a balancing factor, to adaptively adjust the unlearning intensity for each sample. Extensive experiments demonstrate that FaLW achieves superior performance.

**Abstract (Chinese)**

机器遗忘旨在从训练模型中高效移除特定数据的影响，对于维护诸如“被遗忘权”等数据隐私法规至关重要。然而，现有的研究主要在相对平衡的遗忘集上评估遗忘方法。这忽略了现实世界中常见的一种场景，即待遗忘数据（如用户活动记录）遵循长尾分布。本工作首次探究这一关键研究空白。我们发现，在此类长尾设置下，现有的方法存在两个关键问题：异质遗忘偏差和偏斜遗忘偏差。为应对这些挑战，我们提出FaLW，一种即插即用、实例级动态损失重加权方法。FaLW创新性地通过将每个样本的预测概率与同一类未见数据的分布进行比较，来评估每个样本的遗忘状态。在此基础上，它采用一种由平衡因子调制的遗忘感知重加权方案，自适应地调整每个样本的遗忘强度。广泛的实验表明，FaLW取得了优越的性能。

---

### How to Cure Newton for Unlearning Neural Networks? An Empirical Study from the Hessian Perspective

- **Venue**: ICLR 2026 Poster
- **Authors**: Nhung Bui, Xinyang Lu, Rachael Hwee Ling Sim, See-Kiong Ng, Bryan Kian Hsiang Low
- **Keywords**: machine unlearning, second-order unlearning
- **OpenReview**: https://openreview.net/forum?id=dHz2LBCyTh
- **PDF**: https://openreview.net/pdf?id=dHz2LBCyTh

**Abstract**

Machine unlearning enables AI practitioners to comply with data owners' ``Right to be Forgotten'' and post-hoc filter sensitive, noisy, or malicious data from trained models. As a theoretically justified algorithm, Newton unlearning is used in previous works to rigorously unlearn selected models, eliminating the need for expensive retraining. However, we found that Newton unlearning is highly sensitive to the Hessian degeneracy phenomenon in trained neural networks, including large language models (LLMs), leading to unlearning performance degradation. To address this challenge, we propose two new unlearning algorithms, CuReNU and CuReNUS, that tackle the Hessian degeneracy in principle based on cubic regularization and discuss their convergence guarantees. As a stochastic variant of CuReNU, CuReNUS offers an efficient second-order unlearning algorithm that is applicable even to the scale of LLMs. We demonstrated that CuReNUS can achieve comparable unlearning performance to state-of-the-art empirical algorithms across diverse settings, including batch and challenging sequential unlearning.

**Abstract (Chinese)**

机器遗忘使AI从业者能够遵守数据所有者的“被遗忘权”，并从训练模型中事后过滤敏感、噪声或恶意数据。作为一种理论上合理的算法，先前工作使用牛顿遗忘来严格遗忘选定模型，从而消除昂贵的重新训练需求。然而，我们发现牛顿遗忘对训练神经网络（包括大语言模型LLMs）中的海森矩阵退化现象高度敏感，导致遗忘性能下降。为了应对这一挑战，我们提出两种新的遗忘算法CuReNU和CuReNUS，它们基于三次正则化从原理上解决海森矩阵退化问题，并讨论了它们的收敛保证。作为CuReNU的随机变体，CuReNUS提供了一种高效的二阶遗忘算法，即使在LLMs规模下也适用。我们证明CuReNUS在各种设置中，包括批量遗忘和具有挑战性的序列遗忘，能够实现与最先进的经验算法相当的遗忘性能。

---

### Knowledge Externalization: Reversible Unlearning and Modular Retrieval in Multimodal Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiaqi Li, Zihan You, Ruoyan Shen, Shenyu Zhang, Songlin Zhai, Yongrui Chen, Chuanyi Zhang, Jiahui Geng, Fakhri Karray, Sheng Bi, Guilin Qi
- **Keywords**: Machine unlearning, Multimodal Large Language Model
- **OpenReview**: https://openreview.net/forum?id=ZHK6nBHRXw
- **PDF**: https://openreview.net/pdf?id=ZHK6nBHRXw

**Abstract**

Multimodal Large Language Models (MLLMs) achieve remarkable cross-modal understanding by training on vast web-scale datasets, but inadvertently internalize sensitive personal and proprietary information. Existing machine unlearning methods address this by irreversibly altering model parameters to permanently erase knowledge. This destructive paradigm conflicts with modern privacy regulations that mandate auditable, reversible, and user-controllable data management. To address these challenges, we propose Knowledge Externalization, a novel framework for reversible and modular knowledge management in MLLMs.  We first propose Dual-Stream Memory Tuning, a method that transfers targeted knowledge from a model's internal parameters into external memory tokens. To mitigate gradient interference when externalizing multiple concepts, we further introduce Soft Orthogonal Weighting, a technique that preserves the independence of each token. Our resulting framework demonstrates three key capabilities: (i) It achieves effective forgetting of target concepts within the base model, while enabling high-fidelity knowledge restoration using the corresponding memory token. (ii) It supports continuous knowledge editing, allowing the information stored within an external token to be dynamically updated post-externalization. (iii) It displays a remarkable emergent ability for compositionality, where multiple memory tokens (including edited ones) can be freely combined to simultaneously recover knowledge corresponding to each concept. Our source code will be released in the near future.

**Abstract (Chinese)**

多模态大语言模型（MLLMs）通过在海量网络规模数据集上训练，实现了卓越的跨模态理解，但无意中内化了敏感的个人和专有信息。现有的机器遗忘方法通过不可逆地更改模型参数来永久擦除知识，从而解决这一问题。这种破坏性范式与现代隐私法规相冲突，这些法规要求可审计、可逆且用户可控的数据管理。为应对这些挑战，我们提出了知识外部化，这是一种用于 MLLMs 中可逆和模块化知识管理的新框架。我们首先提出了双流记忆调优，这是一种将目标知识从模型内部参数转移到外部记忆令牌的方法。为了缓解外部化多个概念时的梯度干扰，我们进一步引入了软正交加权，这是一种保持每个令牌独立性的技术。我们得到的框架展示了三个关键能力：(i) 它在基础模型中实现了目标概念的有效遗忘，同时使用相应的记忆令牌实现了高保真知识恢复。(ii) 它支持连续知识编辑，允许外部化后动态更新外部令牌中存储的信息。(iii) 它展现出惊人的组合性涌现能力，其中多个记忆令牌（包括已编辑的）可以自由组合，同时恢复对应每个概念的知识。我们的源代码将在不久的将来发布。

---

### LLM Unlearning with LLM Beliefs

- **Venue**: ICLR 2026 Poster
- **Authors**: Kemou Li, Qizhou Wang, Yue Wang, Fengpeng Li, Jun Liu, Bo Han, Jiantao Zhou
- **Keywords**: Large Language Model Unlearning
- **OpenReview**: https://openreview.net/forum?id=qCfYOLAzti
- **PDF**: https://openreview.net/pdf?id=qCfYOLAzti

**Abstract**

Large language models trained on vast corpora inherently risk memorizing sensitive or harmful content, which may later resurface in their outputs.
Prevailing unlearning methods generally rely on gradient ascent and its variants to lower the probability of specific target responses.
However, we find that this strategy induces a critical side effect: probability mass is redistributed into high-likelihood regions, often corresponding to semantically related rephrasings of the targets.
We refer to this as the ***squeezing effect***, which explains why many methods yield merely spurious unlearning, a problem further obscured by automated metrics (e.g., ROUGE, truth ratio) that misreport actual success.
To address this, we propose a ***bootstrapping*** (BS) framework that explicitly links the squeezing effect with the model’s own high-confidence generations, namely its ***model beliefs***.
Since model beliefs inherently capture the very high-likelihood regions where probability mass is squeezed, incorporating them into the unlearning objective directly counters the squeezing effect.
By jointly suppressing both target responses and model beliefs, BS-T (token) attenuates high-probability tokens, whereas BS-S (sequence) removes entire high-confidence generations, together achieving more thorough forgetting while preserving utility.
Extensive experiments on diverse benchmarks confirm the effectiveness of our approach.

**Abstract (Chinese)**

在大规模语料上训练的大型语言模型天生存在记忆敏感或有害内容的风险，这些内容可能随后在其输出中重新出现。

现有的遗忘方法通常依赖梯度上升及其变体来降低特定目标响应的概率。

然而，我们发现这种策略会引发一个关键副作用：概率质量被重新分配到高似然区域，这些区域通常对应于目标的语义相关改述。

我们将此称为“挤压效应”，这解释了为什么许多方法仅产生虚假遗忘，这一问题进一步被自动化指标（如 ROUGE、真值比率）所掩盖，这些指标错误报告了实际成功。

为解决此问题，我们提出一个“自举”（BS）框架，该框架明确将挤压效应与模型自身高置信度生成（即其“模型信念”）联系起来。

由于模型信念天生捕捉了概率质量被挤压的极高似然区域，将其纳入遗忘目标可以直接对抗挤压效应。

通过联合抑制目标响应和模型信念，BS-T（令牌）衰减高概率令牌，而 BS-S（序列）移除整个高置信度生成，从而在保留效用的同时实现更彻底的遗忘。

在多样化基准上的广泛实验证实了我们方法的有效性。

---

### Label Smoothing Improves Machine Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Zonglin Di, Zhaowei Zhu, Jinghan Jia, Jiancheng Liu, Zafar Takhirov, Bo Jiang, Yuanshun Yao, Sijia Liu, Yang Liu
- **Keywords**: Machine unlearning, Label smoothing, Differential privacy
- **OpenReview**: https://openreview.net/forum?id=X74KnsoYEM
- **PDF**: https://openreview.net/pdf?id=X74KnsoYEM

**Abstract**

The objective of machine unlearning (MU) is to eliminate previously learned data from a model. However, it can be challenging to strike a balance between computation cost and performance when using existing MU techniques. Taking inspiration from the influence of label smoothing on model confidence and differential privacy, we propose a simple gradient-based MU approach that uses an inverse process of label smoothing. This work introduces UGradSL, a simple, plug-and-play MU approach that uses smoothed labels. We provide theoretical analyses demonstrating why properly introducing label smoothing improves MU performance. We conducted extensive experiments on several datasets of various sizes and different modalities, demonstrating the effectiveness and robustness of our proposed method. UGradSL also shows close connection to improve the local differential privacy. The consistent improvement in MU performance is only at a marginal cost of additional computations. For instance, UGradSL improves over the gradient ascent MU baseline constantly on different unlearning tasks without sacrificing unlearning efficiency. A self-adaptive UGradSL is also given for simple parameter selection.

**Abstract (Chinese)**

机器遗忘（MU）的目标是从模型中消除先前学习的数据。然而，使用现有MU技术时，在计算成本和性能之间取得平衡可能具有挑战性。受标签平滑对模型置信度和差分隐私影响的启发，我们提出了一种简单的基于梯度的MU方法，该方法采用标签平滑的逆过程。本工作引入了UGradSL，这是一种简单的、即插即用的MU方法，使用平滑标签。我们提供了理论分析，证明了为什么适当引入标签平滑能够提升MU性能。我们在多个不同大小和模态的数据集上进行了广泛实验，证明了我们提出方法的有效性和鲁棒性。UGradSL还显示出与提升局部差分隐私的密切联系。MU性能的一致改进仅以额外计算的微小成本为代价。例如，UGradSL在不同的遗忘任务上持续优于梯度上升MU基线，而不牺牲遗忘效率。本文还提供了一种自适应UGradSL，用于简单的参数选择。

---

### Learning-Time Encoding Shapes Unlearning in LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Ruihan Wu, Konstantin Garov, Kamalika Chaudhuri
- **Keywords**: Large language model, unlearning
- **OpenReview**: https://openreview.net/forum?id=BcjZCertEk
- **PDF**: https://openreview.net/pdf?id=BcjZCertEk

**Abstract**

As large language models (LLMs) are increasingly deployed in the real world, the ability to ``unlearn'', or remove specific pieces of knowledge post hoc, has become essential for a variety of reasons ranging from privacy regulations to correcting outdated or harmful content. Prior work has proposed unlearning benchmarks and algorithms, and has typically assumed that the training process and the target model are fixed. In this work, we empirically investigate how learning-time encoding in knowledge encoding impact the effectiveness of unlearning factual knowledge. 
We conduct two studies: (i) examining how paraphrased descriptions influence unlearning performance, and (ii) analyzing unlearning when multiple facts are embedded within the same training text chunk. 
Our empirical study reveals two important implications: a new perspective for interpreting unlearning performance and practical strategies for improving LLM unlearning.

**Abstract (Chinese)**

随着大型语言模型（LLMs）越来越多地部署到现实世界中，“遗忘”（unlearn），即事后移除特定知识片段的能力，已变得必不可少，其原因多种多样，从隐私法规到修正过时或有害内容。先前工作提出了遗忘基准和算法，并通常假设训练过程和目标模型是固定的。在这项工作中，我们实证地探讨了知识编码中的学习时编码如何影响事实知识遗忘的有效性。

我们进行了两项研究：(i) 检查改述描述如何影响遗忘性能；(ii) 分析当多个事实嵌入同一训练文本块中的遗忘情况。

我们的实证研究揭示了两个重要含义：一种新的解释遗忘性能的视角，以及改进 LLM 遗忘的实用策略。

---

### Localized Concept Erasure in Text-to-Image Diffusion Models via High-Level Representation Misdirection

- **Venue**: ICLR 2026 Poster
- **Authors**: Uichan Lee, Jeonghyeon Kim, Sangheum Hwang
- **Keywords**: Concept Erasing, Unlearning, Robustness, Text-to-Image Generation, Diffusion Models
- **OpenReview**: https://openreview.net/forum?id=JSjOlFLUsS
- **PDF**: https://openreview.net/pdf?id=JSjOlFLUsS

**Abstract**

Recent advances in text-to-image (T2I) diffusion models have seen rapid and widespread adoption. However, their powerful generative capabilities raise concerns about potential misuse for synthesizing harmful, private, or copyrighted content. To mitigate such risks, concept erasure techniques have emerged as a promising solution. Prior works have primarily focused on fine-tuning the denoising component (e.g., the U-Net backbone). However, recent causal tracing studies suggest that visual attribute information is localized in the early self-attention layers of the text encoder, indicating a potential alternative for concept erasing. Building on this insight, we conduct preliminary experiments and find that directly fine-tuning early layers can suppress target concepts but often degrades the generation quality of non-target concepts. To overcome this limitation, we propose High-Level Representation Misdirection (HiRM), which misdirects high-level semantic representations of target concepts in the text encoder toward designated vectors such as random directions or semantically defined directions (e.g., super-categories), while updating only early layers that contain causal states of visual attributes. Our decoupling strategy enables precise concept removal with minimal impact on unrelated concepts, as demonstrated by strong results on UnlearnCanvas and NSFW benchmarks across diverse targets (e.g., objects, styles, nudity). HiRM also preserves generative utility at low training cost, transfers to state-of-the-art architectures such as Flux without additional training, and shows synergistic effects with denoiser-based concept erasing methods.

**Abstract (Chinese)**

文本到图像（T2I）扩散模型的最新进展已获得迅速而广泛的采用。然而，其强大的生成能力引发了对潜在滥用以合成有害、私有或受版权保护内容的担忧。为缓解此类风险，概念擦除技术已成为一种有前景的解决方案。先前工作主要关注微调去噪组件（例如，U-Net 主干）。然而，最近的因果追踪研究表明，视觉属性信息局限于文本编码器的早期自注意力层，这为概念擦除提供了潜在的替代方案。基于这一洞见，我们进行了初步实验，发现直接微调早期层可以抑制目标概念，但往往会降低非目标概念的生成质量。为克服这一局限性，我们提出高层表示误导（HiRM），它将文本编码器中目标概念的高层语义表示误导至指定向量，如随机方向或语义定义的方向（例如，超类别），同时仅更新包含视觉属性因果状态的早期层。我们的解耦策略实现了精确的概念移除，同时对无关概念的影响最小，正如在UnlearnCanvas和NSFW基准上针对多样化目标（例如，物体、风格、裸露）的强劲结果所证明。HiRM还在低训练成本下保留了生成效用，无需额外训练即可转移到最先进的架构如Flux，并与基于去噪器的概念擦除方法显示出协同效应。

---

### Model Collapse Is Not a Bug but a Feature in Machine Unlearning for LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Yan Scholten, Sophie Xhonneux, Leo Schwinn, Stephan Günnemann
- **Keywords**: Machine unlearning, Model collapse, Large language models, LLMs
- **OpenReview**: https://openreview.net/forum?id=1MCQzboBrR
- **PDF**: https://openreview.net/pdf?id=1MCQzboBrR

**Abstract**

Current unlearning methods for LLMs optimize on the private information they seek to remove by incorporating it into their fine-tuning data. We argue this not only risks reinforcing exposure to sensitive data, but also fundamentally contradicts the principle of minimizing its use. As a remedy, we propose a novel unlearning method—Partial Model Collapse (PMC), which does not require unlearning targets in the unlearning objective. Our approach is inspired by recent observations that training generative models on their own generations leads to distribution collapse, effectively removing information from model outputs. Our central insight is that model collapse can be leveraged for machine unlearning by deliberately triggering it for data we aim to remove. We theoretically analyze that our approach converges to the desired outcome, i.e. the model unlearns the data targeted for removal. We empirically demonstrate that PMC overcomes four key limitations of existing unlearning methods that explicitly optimize on unlearning targets, and more effectively removes private information from model outputs while preserving general model utility. Overall, our contributions represent an important step toward more comprehensive unlearning that better aligns with real-world privacy constraints.

**Abstract (Chinese)**

当前的大语言模型（LLMs）遗忘方法通过将目标移除的私有信息纳入微调数据，从而针对这些信息进行优化。我们认为，这不仅有强化敏感数据暴露的风险，而且从根本上违背了最小化其使用原则。作为一种补救措施，我们提出了一种新型遗忘方法——部分模型坍缩（PMC），它在遗忘目标函数中不需要遗忘目标。我们的方法受近期观察的启发，即在生成模型自身生成的数据上训练会导致分布坍缩，从而有效地从模型输出中移除信息。我们的核心洞见是，通过针对我们旨在移除的数据故意触发模型坍缩，可以利用模型坍缩实现机器遗忘。我们从理论上分析了我们的方法收敛于期望结果，即模型遗忘了目标移除的数据。我们通过实验证明，PMC克服了现有明确针对遗忘目标优化的遗忘方法的四个关键局限性，并且在保留一般模型效用的同时，更有效地从模型输出中移除私有信息。总体而言，我们的贡献代表了迈向更全面的遗忘的重要一步，该遗忘更好地符合现实世界的隐私约束。

---

### OFMU: OPTIMIZATION-DRIVEN FRAMEWORK FOR MACHINE UNLEARNING

- **Venue**: ICLR 2026 Poster
- **Authors**: Sadia Asif, Mohammad Mohammadi Amiri
- **Keywords**: machine unlearning, large language models, privacy, bi-level optimization, convergence analysis, Trustworthy Machine Learning, Gradient-Based Methods, Safety in LLMs
- **OpenReview**: https://openreview.net/forum?id=ZDuyNJI56H
- **PDF**: https://openreview.net/pdf?id=ZDuyNJI56H

**Abstract**

Large language models deployed in sensitive applications increasingly require the
ability to unlearn specific knowledge, such as user requests, copyrighted materi-
als, or outdated information, without retraining from scratch to ensure regulatory
compliance, user privacy, and safety. This task, known as machine unlearning,
aims to remove the influence of targeted data (forgetting) while maintaining per-
formance on the remaining data (retention). A common approach is to formu-
late this as a multi-objective problem and reduce it to a single-objective prob-
lem via scalarization, where forgetting and retention losses are combined using
a weighted sum. However, this often results in unstable training dynamics and
degraded model utility due to conflicting gradient directions. To address these
challenges, we propose OFMU, a penalty-based bi-level optimization framework
that explicitly prioritizes forgetting while preserving retention through a hierar-
chical structure. Our method enforces forgetting via an inner maximization step
that incorporates a similarity-aware penalty to decorrelate the gradients of the for-
get and retention objectives, and restores utility through an outer minimization
step. To ensure scalability, we develop a two-loop algorithm with provable conver-
gence guarantees under both convex and non-convex regimes. We further provide
a rigorous theoretical analysis of convergence rates and show that our approach
achieves better trade-offs between forgetting efficacy and model utility compared
to prior methods. Extensive experiments across vision and language benchmarks
demonstrate that OFMU consistently outperforms existing unlearning methods in
both forgetting efficacy and retained utility.

**Abstract (Chinese)**

部署在敏感应用中的大型语言模型日益需要具备遗忘特定知识的能力，例如用户请求、受版权保护的材料或过时信息，而无需从头重新训练，以确保监管合规性、用户隐私和安全性。这项任务称为机器遗忘，旨在消除目标数据的影响（遗忘），同时保持在剩余数据上的性能（保留）。一种常见方法是将此表述为多目标问题，并通过标量化将其简化为单目标问题，其中遗忘和保留损失使用加权和结合。然而，这往往会导致不稳定的训练动态和模型效用的下降，因为梯度方向冲突。为应对这些挑战，我们提出OFMU，这是一种基于惩罚的双层优化框架，通过层次结构明确优先考虑遗忘，同时保留保留性能。我们的方法通过内层最大化步骤强制执行遗忘，该步骤引入感知相似性的惩罚以去相关化遗忘和保留目标的梯度，并通过外层最小化步骤恢复效用。为确保可扩展性，我们开发了一种双循环算法，在凸和非凸情形下均具有可证明的收敛保证。我们进一步提供了收敛速率的严格理论分析，并证明我们的方法在遗忘效果和模型效用之间实现了比先前方法更好的权衡。在视觉和语言基准上的广泛实验表明，OFMU在遗忘效果和保留效用方面均持续优于现有的遗忘方法。

---

### ReTrace: Reinforcement Learning-Guided Reconstruction Attacks on Machine Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Mengyao Ma, Shuofeng Liu, Jason Xue, Surya Nepal, Guangdong Bai
- **Keywords**: Machine Unlearning, Reinforcement Learning, Reconstruction Attack
- **OpenReview**: https://openreview.net/forum?id=wKi4Jeqqrb
- **PDF**: https://openreview.net/pdf?id=wKi4Jeqqrb

**Abstract**

Machine unlearning has emerged as an inevitable AI mechanism to support GDPR requirements such as revoking user consent through the "right to be forgotten". 
However, existing approaches often leave residual traces that make them vulnerable to data reconstruction attacks. 
In this work, we propose ReTrace, the first reconstruction attack framework that uniquely formulates unlearned data recovery on large-scale deep architectures as a reinforcement learning (RL) problem. 
By treating residual unlearning traces as reward signals, ReTrace guides a generator to actively explore the input space and converge toward the forgotten data distribution. 
This RL-guided approach enables both instance-level recovery of individual samples and distribution-level reconstruction of unlearned classes. 
We provide a theoretical foundation showing that the RL objective converges to an exponential-tilted distribution that amplifies forgotten regions. 
Empirically, ReTrace achieves up to 73.1\% instance-level recovery and reduces FID and KL scores beyond two state-of-the-art baselines. 
Strikingly, on the challenging task of text unlearning, it improves BLEU scores by nearly 100\% over black-box baselines while preserving distributional fidelity, demonstrating that RL can recover even high-dimensional and structured modalities. Furthermore, ReTrace demonstrates effectiveness across both convolutional (ResNet) and transformer-based models, with Distil-BERT as the largest architecture attacked to date. These results show that current unlearning methods remain vulnerable, highlighting the need for robust and provably private mechanisms.

**Abstract (Chinese)**

机器遗忘已成为支持GDPR要求（如通过“被遗忘权”撤销用户同意）的不可避免的AI机制。然而，现有的方法往往留下残余痕迹，使其容易受到数据重构攻击。在本工作中，我们提出了ReTrace，这是第一个独特的重构攻击框架，它将大规模深度架构上的遗忘数据恢复表述为强化学习（RL）问题。通过将残余遗忘痕迹视为奖励信号，ReTrace引导生成器主动探索输入空间，并收敛到遗忘数据分布。这种RL引导的方法实现了单个样本的实例级恢复以及遗忘类别的分布级重构。我们提供了理论基础，证明RL目标收敛到放大遗忘区域的指数倾斜分布。实证上，ReTrace实现了高达73.1%的实例级恢复，并使FID和KL分数优于两个最先进基线。引人注目的是，在具有挑战性的文本遗忘任务上，它将BLEU分数相对于黑盒基线提高了近100%，同时保持分布保真度，这证明RL甚至可以恢复高维和结构化模态。此外，ReTrace在卷积（ResNet）和基于Transformer的模型上均展示了有效性，其中Distil-BERT是迄今为止被攻击的最大架构。这些结果表明，当前的遗忘方法仍然脆弱，突显了对鲁棒且可证明隐私机制的需求。

---

### Reinforcement Unlearning via Group Relative Policy Optimization

- **Venue**: ICLR 2026 Poster
- **Authors**: Efstratios Zaradoukas, Bardh Prenkaj, Gjergji Kasneci
- **Keywords**: Machine Unlearning, Group Relative Policy Optimization, Reinforcement Learning, Large Language Models, Preference Optimization
- **OpenReview**: https://openreview.net/forum?id=BjWwqPE7mk
- **PDF**: https://openreview.net/pdf?id=BjWwqPE7mk

**Abstract**

During pretraining, LLMs inadvertently memorize sensitive or copyrighted data, posing significant compliance challenges under legal frameworks like the GDPR and the EU AI Act. Fulfilling these mandates demands techniques that can remove information from a deployed model without retraining from scratch. Existing unlearning approaches attempt to address this need, but often leak the very data they aim to erase, sacrifice fluency and robustness, or depend on costly external reward models. We introduce PURGE (Policy Unlearning through Relative Group Erasure), a novel method grounded in the Group Relative Policy Optimization framework that formulates unlearning as a verifiable problem. PURGE uses an intrinsic reward signal that penalizes any mention of forbidden concepts, allowing safe and consistent unlearning. Our approach achieves up to $\times$46 lower token usage per target than state-of-the-art methods, while improving fluency by +5.48\% and adversarial robustness by +12.02\% over the base model. Extensive evaluation on the Real World Knowledge Unlearning (RWKU) benchmark shows that PURGE reaches 11\% unlearning effectiveness while preserving 98\% of original utility. PURGE shows that framing LLM unlearning as a verifiable task, enables more reliable, efficient, and scalable forgetting, suggesting a promising new direction for unlearning research that combines theoretical guarantees, improved safety, and practical deployment efficiency.

**Abstract (Chinese)**

在大规模语言模型（LLMs）的预训练过程中，它们无意中记忆了敏感或受版权保护的数据，这在GDPR和欧盟人工智能法案等法律框架下构成了重大的合规挑战。满足这些要求需要能够在不从头重新训练的情况下从已部署模型中移除信息的技术。现有的遗忘方法试图解决这一需求，但往往会泄露它们旨在擦除的数据、牺牲流畅性和鲁棒性，或依赖昂贵的外部奖励模型。我们引入了PURGE（通过相对组擦除的政策遗忘，Policy Unlearning through Relative Group Erasure），这是一种基于组相对策略优化框架的新颖方法，将遗忘表述为一个可验证的问题。PURGE使用一种内在奖励信号，对任何提及禁忌概念的行为施加惩罚，从而实现安全且一致的遗忘。我们的方法在每个目标上的令牌使用量比最先进的方法低至×46，同时相对于基模型提高了流畅性+5.48%和对抗鲁棒性+12.02%。在真实世界知识遗忘（RWKU）基准上的广泛评估显示，PURGE达到了11%的遗忘有效性，同时保留了98%的原始效用。PURGE表明，将LLM遗忘表述为可验证任务，能够实现更可靠、高效且可扩展的遗忘，这为遗忘研究指明了一个有前景的新方向，该方向结合了理论保证、改进的安全性和实际部署效率。

---

### Rethinking Benign Relearning: Syntax as the Hidden Driver of Unlearning Failures

- **Venue**: ICLR 2026 Poster
- **Authors**: Sangyeon Yoon, Hyesoo Hong, Wonje Jeung, Albert No
- **Keywords**: Large Language Models (LLMs), Machine Unlearning
- **OpenReview**: https://openreview.net/forum?id=IU4rqTlpRb
- **PDF**: https://openreview.net/pdf?id=IU4rqTlpRb

**Abstract**

Machine unlearning aims to remove specific content from trained models while preserving overall performance.
However, the phenomenon of benign relearning, in which forgotten information reemerges even from benign fine-tuning data, reveals that existing unlearning methods remain fundamentally fragile.
A common explanation attributes this effect to topical relevance, but we find this account insufficient.
Through systematic analysis, we demonstrate that syntactic similarity, rather than topicality, is the primary driver: across benchmarks, syntactically similar data consistently trigger recovery even without topical overlap, due to their alignment in representations and gradients with the forgotten content.
Motivated by this insight, we introduce syntactic diversification, which paraphrases the original forget queries into heterogeneous structures prior to unlearning.
This approach effectively suppresses benign relearning, accelerates forgetting, and substantially alleviates the trade-off between unlearning efficacy and model utility.

**Abstract (Chinese)**

机器遗忘旨在从训练好的模型中移除特定内容，同时保持整体性能。

然而，良性重学习现象——其中被遗忘的信息甚至从良性微调数据中重新出现——揭示了现有遗忘方法在根本上仍然脆弱。

一种常见的解释将此效应归因于主题相关性，但我们发现这一解释不足。

通过系统分析，我们证明句法相似性而非主题性是主要驱动因素：在各种基准测试中，句法相似的数据即使没有主题重叠，也会持续触发恢复，这是由于它们在表示和梯度上与被遗忘内容对齐。

受此洞见启发，我们引入句法多样化方法，该方法在遗忘之前将原始遗忘查询改写为异构结构。

该方法有效抑制良性重学习，加速遗忘，并显著缓解遗忘效能与模型效用之间的权衡。

---

### Safety Mirage: How Spurious Correlations Undermine VLM Safety Fine-Tuning and Can Be Mitigated by Machine Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Yiwei Chen, Yuguang Yao, Yihua Zhang, Bingquan Shen, Gaowen Liu, Sijia Liu
- **Keywords**: VLM safety
- **OpenReview**: https://openreview.net/forum?id=Qi1rZa4zzl
- **PDF**: https://openreview.net/pdf?id=Qi1rZa4zzl

**Abstract**

Recent vision language models (VLMs) have made remarkable strides in generative modeling with multimodal inputs, particularly text and images. However, their susceptibility to generating harmful content when exposed to unsafe queries raises critical safety concerns. While current alignment strategies primarily rely on supervised safety fine-tuning with curated datasets, we identify a fundamental limitation we call the "safety mirage", where supervised fine-tuning inadvertently reinforces spurious correlations between superficial textual patterns and safety responses, rather than fostering deep, intrinsic mitigation of harm. We show that these spurious correlations leave fine-tuned VLMs vulnerable even to a simple one-word modification-based attack, where substituting a single word in text queries with a spurious correlation-inducing alternative can effectively bypass safeguards. Additionally, these correlations contribute to the over-prudence, causing fine-tuned VLMs to refuse benign queries unnecessarily. To address these issues, we show machine unlearning (MU) as a powerful alternative to supervised safety fine-tuning, as it avoids biased feature-label mappings and directly removes harmful knowledge from VLMs while preserving their general capabilities. Extensive evaluations across safety benchmarks show that under MU-based alignment reduces the attack success rate by up to 60.27% and cuts unnecessary rejections by over 84.20%.

**Abstract (Chinese)**

最近的视觉语言模型（VLMs）在处理多模态输入（特别是文本和图像）的生成建模方面取得了显著进步。然而，当暴露于不安全查询时，它们生成有害内容的易感性引发了关键的安全担忧。虽然当前的对齐策略主要依赖于使用精选数据集的监督安全微调，但我们识别出一个根本性局限性，我们称之为“安全幻觉”，其中监督微调无意中强化了表层文本模式与安全响应之间的虚假相关性，而不是培养对危害的深度、内在缓解。我们证明，这些虚假相关性使得微调后的VLMs即使面对简单的基于单字修改的攻击也易受攻击，其中将文本查询中的单个单词替换为诱发虚假相关性的替代词即可有效绕过安全机制。此外，这些相关性导致过度谨慎，使得微调后的VLMs不必要地拒绝良性查询。为了解决这些问题，我们展示了机器遗忘（MU）作为监督安全微调的强大替代方案，因为它避免了偏差特征-标签映射，并直接从VLMs中移除有害知识，同时保留其一般能力。在安全基准上的广泛评估显示，基于MU的对齐将攻击成功率降低了高达60.27%，并将不必要拒绝减少了超过84.20%。

---

### Sharpness-Aware Machine Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Haoran Tang, Rajiv Khanna
- **Keywords**: Machine Unlearning, Sharpness-Aware Minimization
- **OpenReview**: https://openreview.net/forum?id=BZ8I2tXomt
- **PDF**: https://openreview.net/pdf?id=BZ8I2tXomt

**Abstract**

We characterize the effectiveness of Sharpness-aware minimization (SAM) under machine unlearning scheme, where unlearning forget signals interferes with learning retain signals. While previous work prove that SAM improves generalization with noise memorization prevention, we show that SAM abandons such denoising property when fitting the forget set, leading to altered generalization depending on signal strength. We further characterize the signal surplus of SAM in the order of signal strength, which enables learning from less retain signals to maintain model performance and putting more weight on unlearning the forget set. Empirical studies show that SAM outperforms SGD with relaxed requirement for retain signals and can enhance various unlearning methods either as pretrain or unlearn algorithm. Motivated by our refined characterization of SAM unlearning and observing that overfitting can benefit more stringent sample-specific unlearning, we propose Sharp MinMax, which splits the model into two to learn retain signals with SAM and unlearn forget signals with sharpness maximization, achieving best performance. Extensive experiments show that SAM enhances unlearning across varying difficulties measured by memorization, yielding decreased feature entanglement between retain and forget sets, stronger resistance to membership inference attacks, and a flatter loss landscape. Our observations generalize to more noised data, different optimizers, and different architectures.

**Abstract (Chinese)**

我们刻画了锐度感知最小化（SAM）在机器遗忘方案下的有效性，其中遗忘信号干扰了保留信号的学习。虽然先前工作证明SAM通过噪声记忆预防改善泛化，但我们表明，当拟合遗忘集时，SAM放弃了这种去噪特性，导致泛化根据信号强度而改变。我们进一步刻画了SAM的信号盈余，按信号强度的顺序，这使得从较少的保留信号中学习以维持模型性能，并将更多权重放在遗忘遗忘集上。实证研究表明，SAM在对保留信号要求放宽的情况下优于SGD，并且可以作为预训练或遗忘算法增强各种遗忘方法。受我们对SAM遗忘的精细刻画以及观察到过拟合可以有益于更严格的样本特定遗忘的启发，我们提出锐度MinMax，它将模型分为两部分，使用SAM学习保留信号，并使用锐度最大化遗忘遗忘信号，从而实现最佳性能。大量实验表明，SAM在由记忆度衡量的不同难度下增强遗忘，导致保留集和遗忘集之间特征纠缠减少、对成员推断攻击的更强抵抗力，以及更平坦的损失景观。我们的观察推广到更噪声的数据、不同的优化器和不同的架构。

---

### Towards Privacy-Guaranteed Label Unlearning in Vertical Federated Learning: Few-Shot Forgetting Without Disclosure

- **Venue**: ICLR 2026 Poster
- **Authors**: Hanlin Gu, Hong Xi Tae, Lixin Fan, Chee Seng Chan
- **Keywords**: Federated Learning, Machine Unlearning, Privacy-Preserving
- **OpenReview**: https://openreview.net/forum?id=G1JdmhkicJ
- **PDF**: https://openreview.net/pdf?id=G1JdmhkicJ

**Abstract**

This paper addresses the critical challenge of unlearning in Vertical Federated Learning (VFL), a setting that has received far less attention than its horizontal counterpart. Specifically, we propose the first method tailored to *label unlearning* in VFL, where labels play a dual role as both essential inputs and sensitive information. To this end, we employ a representation-level manifold mixup mechanism to generate synthetic embeddings for both unlearned and retained samples. This is to provide richer signals for the subsequent gradient-based label forgetting and recovery steps. These augmented embeddings are then subjected to gradient-based label forgetting, effectively removing the associated label information from the model. To recover performance on the retained data, we introduce a recovery-phase optimization step that refines the remaining embeddings. This design achieves effective label unlearning while maintaining computational efficiency. We validate our method through extensive experiments on diverse datasets, including MNIST, CIFAR-10, CIFAR-100, ModelNet, Brain Tumor MRI, COVID-19 Radiography, and Yahoo Answers demonstrate strong efficacy and scalability. Overall, this work establishes a new direction for unlearning in VFL, showing that re-imagining mixup as an efficient mechanism can unlock practical and utility-preserving unlearning. The code is publicly available at https://github.com/bryanhx/Towards-Privacy-Guaranteed-Label-Unlearning-in-Vertical-Federated-Learning.

**Abstract (Chinese)**

本文针对垂直联邦学习 (VFL) 中的遗忘问题这一关键挑战进行了研究，该设置相比其水平联邦学习对应设置受到了远少关注。具体而言，我们提出了首个专为 VFL 中*标签遗忘*量身定制的方法，在该设置中，标签既是必需输入，又是敏感信息。为此，我们采用表示级流形 Mixup 机制，为遗忘样本和保留样本生成合成嵌入，以为后续基于梯度的标签遗忘和恢复步骤提供更丰富的信号。这些增强嵌入随后接受基于梯度的标签遗忘，有效从模型中移除相关标签信息。为了在保留数据上恢复性能，我们引入恢复阶段优化步骤来精炼剩余嵌入。该设计实现了有效的标签遗忘，同时保持计算效率。我们通过在多样化数据集上的广泛实验验证了该方法，包括 MNIST、CIFAR-10、CIFAR-100、ModelNet、Brain Tumor MRI、COVID-19 Radiography 和 Yahoo Answers，这些实验展示了强大的有效性和可扩展性。总体而言，本工作为 VFL 中的遗忘开辟了新方向，表明将 Mixup 重新构想为高效机制可以实现实用且保留效用的遗忘。代码公开可用：https://github.com/bryanhx/Towards-Privacy-Guaranteed-Label-Unlearning-in-Vertical-Federated-Learning。

---

### Unlearning Isn't Invisible: Detecting Unlearning Traces in LLMs from Model Outputs

- **Venue**: ICLR 2026 Poster
- **Authors**: Yiwei Chen, Soumyadeep Pal, Yimeng Zhang, Qing Qu, Sijia Liu
- **Keywords**: LLM, Machine Unlearning
- **OpenReview**: https://openreview.net/forum?id=bqEnnzfhBZ
- **PDF**: https://openreview.net/pdf?id=bqEnnzfhBZ

**Abstract**

Machine unlearning (MU) for large language models (LLMs), commonly referred to as LLM unlearning, seeks to remove specific undesirable data or knowledge from a trained model, while maintaining its performance on standard tasks. While unlearning plays a vital role in protecting data privacy, enforcing copyright, and mitigating sociotechnical harms in LLMs, we identify a new vulnerability post-unlearning: unlearning trace detection. We discover that unlearning leaves behind persistent "fingerprints" in LLMs, detectable traces in both model behavior and internal representations. These traces can be identified from output responses, even when prompted with forget-irrelevant inputs. Specifically, even a simple supervised classifier can determine whether a model has undergone unlearning, using only its prediction logits or even its textual outputs. Further analysis shows that these traces are embedded in intermediate activations and propagate nonlinearly to the final layer, forming low-dimensional, learnable manifolds in activation space. Through extensive experiments, we demonstrate that unlearning traces can be detected with over 90% accuracy even under forget-irrelevant inputs, and that larger LLMs exhibit stronger detectability. These findings reveal that unlearning leaves measurable signatures, introducing a new risk of reverse-engineering forgotten information when a model is identified as unlearned, given an input query.

**Abstract (Chinese)**

大型语言模型 (LLMs) 的机器遗忘 (MU)，通常称为 LLM 遗忘，旨在从训练好的模型中移除特定不期望的数据或知识，同时保持其在标准任务上的性能。虽然遗忘在保护数据隐私、执行版权以及缓解 LLMs 中的社会技术危害方面发挥着至关重要的作用，但我们识别出遗忘后的一种新漏洞：遗忘痕迹检测。我们发现，遗忘会在 LLMs 中留下持久的“指纹”，即模型行为和内部表示中可检测的痕迹。这些痕迹可以从输出响应中识别，即使使用与遗忘无关的输入进行提示。具体而言，即使是一个简单的监督分类器，也可以使用模型的预测 logits 或甚至其文本输出来判断模型是否经历了遗忘。进一步分析显示，这些痕迹嵌入在中间激活中，并非线性传播到最后一层，在激活空间中形成低维、可学习流形。通过广泛实验，我们证明，即使在与遗忘无关的输入下，遗忘痕迹也可以以超过 90% 的准确率被检测到，并且更大的 LLMs 表现出更强的可检测性。这些发现揭示，遗忘会留下可测量的签名，当模型被识别为已遗忘时，会引入一种新的风险，即逆向工程遗忘信息，给定一个输入查询。

---

### Video Unlearning via Low-Rank Refusal Vector

- **Venue**: ICLR 2026 Poster
- **Authors**: Simone Facchiano, Stefano Saravalle, Matteo Migliarini, Edoardo De Matteis, Alessio Sampieri, Andrea Pilzer, Emanuele Rodolà, Indro Spinelli, Luca Franco, Fabio Galasso
- **Keywords**: video generation, machine unlearning
- **OpenReview**: https://openreview.net/forum?id=U1XBHtXl7Y
- **PDF**: https://openreview.net/pdf?id=U1XBHtXl7Y

**Abstract**

Video generative models achieve high-quality synthesis from natural-language prompts by leveraging large-scale web data. However, this training paradigm inherently exposes them to unsafe biases and harmful concepts, introducing the risk of generating undesirable or illicit content. To mitigate unsafe generations, existing machine unlearning approaches either rely on filtering, and can therefore be bypassed, or they update model weights, but with costly fine-tuning or training-free closed-form edits. We propose the first training-free weight update framework for concept removal in video diffusion models.
From five paired safe/unsafe prompts, our method estimates a refusal vector and integrates it into the model weights as a closed-form update. A contrastive low-rank factorization further disentangles the target concept from unrelated semantics, it ensures a selective concept suppression and it does not harm generation quality. Our approach reduces unsafe generations on the Open-Sora and ZeroScopeT2V models across the T2VSafetyBench and SafeSora benchmarks, with average reductions of 36.3% and 58.2% respectively, while preserving prompt alignment and video quality. This establishes an efficient and scalable solution for safe video generation without retraining nor any inference overhead.

**Abstract (Chinese)**

视频生成模型通过利用大规模网络数据，从自然语言提示中实现高质量合成。然而，这种训练范式本质上会使模型暴露于不安全偏见和有害概念，从而引入生成不良或非法内容的风险。为了缓解不安全生成，现有的机器遗忘方法要么依赖过滤（从而可被绕过），要么更新模型权重，但需进行代价高昂的微调或无训练闭式编辑。我们提出了首个针对视频扩散模型概念移除的无训练权重更新框架。

我们的方法从五对配对的安全/不安全提示中估计拒绝向量，并将其作为闭式更新集成到模型权重中。对比低秩因子分解进一步将目标概念从不相关语义中解耦，从而确保选择性概念抑制且不损害生成质量。我们的方法在Open-Sora和ZeroScopeT2V模型上显著降低了T2VSafetyBench和SafeSora基准上的不安全生成，平均降低幅度分别为36.3%和58.2%，同时保留了提示对齐性和视频质量。这为无需重新训练且无推理开销的安全视频生成提供了高效且可扩展的解决方案。

---

### WARP: Weight Teleportation for Attack-Resilient Unlearning Protocols

- **Venue**: ICLR 2026 Poster
- **Authors**: Mohammad mahdi Maheri, Xavier Cadet, Peter Chin, Hamed Haddadi
- **Keywords**: Machine unlearning, Approximate unlearning, Neural teleportation, Weight-space symmetries, Privacy attacks, Membership inference, Model inversion, Data reconstruction
- **OpenReview**: https://openreview.net/forum?id=404TzkOCUD
- **PDF**: https://openreview.net/pdf?id=404TzkOCUD

**Abstract**

Approximate machine unlearning aims to efficiently remove the influence of specific data points from a trained model, offering a practical alternative to full retraining. However, it introduces privacy risks: an adversary with access to both the original and unlearned models can exploit their differences for membership inference or data reconstruction. We show these vulnerabilities arise from two factors: large gradient norms of forgotten samples and the close proximity of the unlearned model to the original. To demonstrate their severity, we design unlearning-specific membership inference and reconstruction attacks, showing that several state-of-the-art methods (such as NGP and SCRUB) remain vulnerable.

To mitigate this leakage, we introduce WARP, a plug-and-play teleportation defense that leverages neural network symmetries to reduce gradient energy of forgotten samples and increase parameter dispersion while preserving accuracy. This reparameterization hides the signal of forgotten data, making it harder for attackers to distinguish forgotten samples from non-members or to recover them through reconstruction. Across six unlearning algorithms, our approach achieves consistent privacy gains, reducing adversarial advantage by up to 64% in black-box settings and 92% in white-box settings, while maintaining accuracy on retained data. These results highlight teleportation as a general tool for improving privacy in approximate unlearning.

**Abstract (Chinese)**

近似机器遗忘旨在高效移除训练模型中特定数据点的影响，提供全量重训练的实用替代方案。然而，它引入了隐私风险：拥有原始模型和遗忘模型访问权的攻击者可利用二者差异进行成员推断或数据重构。我们证明这些漏洞源于两个因素：被遗忘样本的大梯度范数以及遗忘模型与原始模型的紧密接近性。为展示其严重性，我们设计了专为遗忘场景的成员推断和重构攻击，表明若干最先进方法（如NGP和SCRUB）仍易受攻击。

为缓解此类泄露，我们提出WARP，一种即插即用传送防御机制，该机制利用神经网络对称性降低被遗忘样本的梯度能量并增加参数分散，同时保持准确性。这种重参数化隐藏了被遗忘数据的信号，使攻击者更难区分被遗忘样本与非成员样本，或通过重构恢复它们。在六种遗忘算法上，我们的方法实现了稳定的隐私提升，在黑盒设置下将攻击优势降低高达64%，在白盒设置下降低高达92%，同时保持保留数据的准确性。这些结果凸显传送作为提升近似机器遗忘隐私的通用工具。

---

### WaterDrum: Watermark-based Data-centric Unlearning Metric

- **Venue**: ICLR 2026 Poster
- **Authors**: Xinyang Lu, Xinyuan Niu, Gregory Kang Ruey Lau, Nhung Bui, Rachael Hwee Ling Sim, John Russell Himawan, Fanyu Wen, Chuan-Sheng Foo, See-Kiong Ng, Bryan Kian Hsiang Low
- **Keywords**: machine unlearning, watermarking, metric, LLM
- **OpenReview**: https://openreview.net/forum?id=5GVfneFvhq
- **PDF**: https://openreview.net/pdf?id=5GVfneFvhq

**Abstract**

Large language model (LLM) unlearning is critical in real-world applications where it is necessary to efficiently remove the influence of private, copyrighted, or harmful data from some users. Existing utility-centric unlearning metrics (based on model utility) may fail to accurately evaluate the extent of unlearning in realistic settings such as when the forget and retain sets have semantically similar content and/or retraining the model from scratch on the retain set is impractical. This paper presents the first data-centric unlearning metric for LLMs called WaterDrum that exploits robust text watermarking to overcome these limitations. We introduce new benchmark datasets (with different levels of data similarity) for LLM unlearning that can be used to rigorously evaluate unlearning algorithms via WaterDrum.

**Abstract (Chinese)**

大语言模型 (LLM) 遗忘在实际应用中至关重要，在这些应用中，需要高效移除某些用户私有、受版权保护或有害数据的影响。现有的以效用为中心的遗忘度量（基于模型效用）可能无法准确评估现实场景下的遗忘程度，例如遗忘集和保留集具有语义相似的语料，和/或在保留集上从头重新训练模型是不切实际的。本文提出了首个针对 LLM 的以数据为中心的遗忘度量方法 WaterDrum，该方法利用鲁棒文本水印来克服这些局限性。我们引入了新的基准数据集（具有不同数据相似度水平）用于 LLM 遗忘，可通过 WaterDrum 严格评估遗忘算法。

---

### When Priors Backfire: On the Vulnerability of Unlearnable Examples to Pretraining

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhihao Li, Gezheng Xu, Jiale Cai, Ruiyi Fang, Di Wu, Qicheng Lao, Charles Ling, Boyu Wang
- **Keywords**: unlearnable examples, data privacy
- **OpenReview**: https://openreview.net/forum?id=ssWi0rC3mx
- **PDF**: https://openreview.net/pdf?id=ssWi0rC3mx

**Abstract**

Unlearnable Examples (UEs) serve as a data protection strategy that generates imperceptible perturbations to mislead models into learning spurious correlations instead of underlying semantics. In this paper, we uncover a fundamental vulnerability of UEs that emerges when learning starts from a pretrained model. Crucially, our empirical analysis shows that even when data are protected by carefully crafted perturbations, pretraining priors still furnish rich semantic representations that allow the model to circumvent the shortcuts introduced by UEs and capture genuine features, thereby nullifying unlearnability. To address this, we propose $\textbf{BAIT}$ ($\textbf{B}$inding $\textbf{A}$rtificial perturbations to $\textbf{I}$ncorrect $\textbf{T}$argets), a novel bi‑level optimization formulation. Specifically, the inner level aims at associating the perturbed samples with real labels to simulate standard data-label alignment, while the outer level actively disrupts this alignment by enforcing a mislabel-perturbation binding that maps samples to designated incorrect targets. This mechanism effectively overrides the semantic guidance of priors, forcing the model to rely on the injected perturbations and consequently preventing the acquisition of true semantics. Extensive experiments on standard benchmarks and multiple pretrained backbones demonstrate that BAIT effectively mitigates the influence of pretraining priors and maintains data unlearnability. Code is available at https://github.com/zhli-cs/BAIT.

**Abstract (Chinese)**

不可学习示例（UEs）作为一种数据保护策略，通过生成不可察觉的扰动来误导模型学习虚假相关性而非底层语义。本文揭示了UEs的一种基本漏洞，该漏洞在从预训练模型开始学习时显现。关键的是，我们的实证分析表明，即使数据受到精心设计的扰动保护，预训练先验仍提供丰富的语义表示，使模型能够绕过UEs引入的捷径并捕捉真实特征，从而抵消不可学习性。为解决此问题，我们提出\textbf{BAIT}（\textbf{B}inding \textbf{A}rtificial perturbations to \textbf{I}ncorrect \textbf{T}argets），一种新型双层优化框架。具体而言，内层旨在将扰动样本与真实标签关联，以模拟标准的数据-标签对齐，而外层通过强制执行将样本映射到指定不正确目标的错误标签-扰动绑定，积极破坏这种对齐。该机制有效覆盖先验的语义指导，迫使模型依赖注入的扰动，从而防止获取真实语义。在标准基准和多个预训练主干上的广泛实验表明，BAIT有效缓解预训练先验的影响并维持数据不可学习性。代码可在https://github.com/zhli-cs/BAIT获取。

---
