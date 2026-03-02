# robustness_adversarial

**Description**: 对抗鲁棒性与分布外稳健性。包括 adversarial examples、攻击/防御、鲁棒训练、OOD detection、certified robustness、对抗评测与鲁棒泛化等。

**Paper count**: 36

---

### A Unified Total Variation Framework for Membrane Potential Perturbation Dynamic

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhao-Rong Lai, Xiwen Yuan, Ziliang Chen, Liangda Fang, Yongsen Zheng
- **Keywords**: Membrane potential perturbation dynamic, spiking neural network, total variation
- **OpenReview**: https://openreview.net/forum?id=LDo9numrx6
- **PDF**: https://openreview.net/pdf?id=LDo9numrx6

**Abstract**

Membrane potential perturbation dynamic (MPPD) is an emerging approach to capture perturbation intensity and stabilize the performance of spiking neural networks (SNN). It discards the neuronal reset part to intuitively reduce fluctuations of dynamics, but this treatment may be insufficient in perturbation characterization. In this study, we prove that MPPD is total variation (TV), which is a widely-used methodology for robust signal reconstruction. Moreover, we propose a novel TV-$\ell_1$ framework for MPPD, which allows for a wider range of network functions and has better denoising advantage than the existing TV-$\ell_2$ framework, based on the coarea formula. Experiments show that MPPD-TV-$\ell_1$ achieves robust performance in both Gaussian noise training and adversarial training for image classification tasks. This finding may provide a new insight into the essence of perturbation characterization.

**Abstract (Chinese)**

膜电位扰动动态（MPPD）是一种新兴方法，用于捕捉扰动强度并稳定脉冲神经网络（SNN）的性能。它丢弃神经元重置部分，以直观地减少动态波动，但这种处理在扰动表征方面可能不足。本研究证明，MPPD 即总变差（TV），这是一种广泛用于鲁棒信号重构的方法论。此外，我们提出了一种新型 TV-ℓ₁ 框架用于 MPPD，该框架基于协区域公式，允许更广泛的网络功能，并比现有的 TV-ℓ₂ 框架具有更好的去噪优势。实验表明，MPPD-TV-ℓ₁ 在图像分类任务的高斯噪声训练和对抗训练中均实现了鲁棒性能。这一发现可能为扰动表征的本质提供新的洞见。

---

### Adversarial Attacks Already Tell the Answer: Directional Bias-Guided Test-time Defense for Vision-Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Liangsheng Liu, Si Chen, Jiamin Wu, Weiwei Feng, Zhixin Cheng, Xiaotian Yin, Wenfei Yang, Tianzhu Zhang
- **Keywords**: Adversarial Attacks, Vision-Language Models, Test-time Defense
- **OpenReview**: https://openreview.net/forum?id=UqC2oFRRyc
- **PDF**: https://openreview.net/pdf?id=UqC2oFRRyc

**Abstract**

Vision-Language Models (VLMs), such as CLIP, have shown strong zero-shot generalization but remain highly vulnerable to adversarial perturbations, posing serious risks in real-world applications. Test-time defenses for VLMs have recently emerged as a promising and efficient approach to defend against adversarial attacks without requiring costly large-scale retraining. In this work, we uncover a surprising phenomenon: under diverse input transformations, adversarial images in CLIP’s feature space consistently shift along a dominant direction, in contrast to the dispersed patterns of clean images. We hypothesize that this dominant shift, termed the Defense Direction, opposes the adversarial shift, pointing features back toward their correct class centers. Building on this insight, we propose Directional Bias-guided Defense (DBD), a test-time framework that estimates the Defense Direction and employs a DB-score–based two-stream reconstruction strategy to recover robust representations. Experiments on 15 datasets demonstrate that DBD not only achieves SOTA adversarial robustness while preserving clean accuracy, but also reveals the counterintuitive result that adversarial accuracy can even surpass clean accuracy. This demonstrates that adversarial perturbations inherently encode directional priors about the true decision boundary.

**Abstract (Chinese)**

视觉-语言模型（VLMs），如CLIP，已展示出强大的零样本泛化能力，但仍对对抗扰动高度脆弱，在实际应用中构成严重风险。VLMs的测试时防御方法最近已成为一种有前景且高效的方法，用于防御对抗攻击，而无需昂贵的大规模重新训练。在本工作中，我们揭示了一个令人惊讶的现象：在多种输入变换下，CLIP特征空间中的对抗图像始终沿一个主导方向偏移，与干净图像的分散模式形成对比。我们假设，这种主导偏移，称为防御方向，与对抗偏移相反，将特征指向正确的类别中心。基于这一洞见，我们提出方向偏差引导防御（DBD），这是一个测试时框架，它估计防御方向，并采用基于DB-score的双流重构策略来恢复鲁棒表示。在15个数据集上的实验表明，DBD不仅在保持干净准确率的同时实现了最先进的对抗鲁棒性，还揭示了对抗准确率甚至可能超过干净准确率的反直觉结果。这表明，对抗扰动本质上编码了关于真实决策边界的方向先验。

---

### Adversarial Déjà Vu: Jailbreak Dictionary Learning for Stronger Generalization to Unseen Attacks

- **Venue**: ICLR 2026 Poster
- **Authors**: Mahavir Dabas, Tran Huynh, Nikhil Reddy Billa, Jiachen T. Wang, Peng Gao, Charith Peris, Yao Ma, Rahul Gupta, Ming Jin, Prateek Mittal, Ruoxi Jia
- **Keywords**: Safety, Alignment
- **OpenReview**: https://openreview.net/forum?id=WFo8P1gQBh
- **PDF**: https://openreview.net/pdf?id=WFo8P1gQBh

**Abstract**

Large language models remain vulnerable to jailbreak attacks that bypass safety guardrails to elicit harmful outputs. Defending against novel jailbreaks represents a critical challenge in AI safety. Adversarial training---designed to make models robust against worst-case perturbations---has been the dominant paradigm for adversarial robustness. However, due to optimization challenges and difficulties in defining realistic threat models, adversarial training methods often fail on newly developed jailbreaks in practice. This paper proposes a new paradigm for improving robustness against unseen jailbreaks, centered on the Adversarial Déjà Vu hypothesis: novel jailbreaks are not fundamentally new, but largely recombinations of adversarial skills from previous attacks. We study this hypothesis through a large-scale analysis of 32 attack papers published over two years. Using an automated pipeline, we extract and compress adversarial skills into a sparse dictionary of primitives, with LLMs generating human-readable descriptions. Our analysis reveals that unseen attacks can be effectively explained as sparse compositions of earlier skills, with explanatory power increasing monotonically as skill coverage grows.
Guided by this insight, we introduce Adversarial Skill Compositional Training (ASCoT), which trains on diverse compositions of skill primitives rather than isolated attack instances. ASCoT substantially improves robustness to unseen attacks, including multi-turn jailbreaks, while maintaining low over-refusal rates. We also demonstrate that expanding adversarial skill coverage, not just data scale, is key to defending against novel attacks.

**Abstract (Chinese)**

大型语言模型仍易受越狱攻击影响，这些攻击绕过安全护栏以诱发有害输出。防御新型越狱攻击是人工智能安全领域的关键挑战。对抗训练——旨在使模型对最坏情况扰动具有鲁棒性——已成为对抗鲁棒性的主导范式。然而，由于优化挑战以及定义现实威胁模型的困难，对抗训练方法在实践中往往无法应对新开发的越狱攻击。本文提出了一种新的范式，用于提升对未见越狱攻击的鲁棒性，该范式以对抗既视感假设为中心：新型越狱攻击并非根本上全新，而是先前攻击中对抗技能的大量重组。我们通过对两年内发表的32篇攻击论文进行大规模分析来检验这一假设。利用自动化管道，我们将对抗技能提取并压缩为稀疏基元字典，并由大型语言模型生成人类可读描述。我们的分析揭示，未见攻击可被有效解释为先前技能的稀疏组合，且随着技能覆盖范围的增长，解释力单调递增。

受此洞见启发，我们引入对抗技能组合训练（ASCoT），该方法训练于技能基元的多样组合而非孤立的攻击实例。ASCoT显著提升了对未见攻击的鲁棒性，包括多轮越狱攻击，同时保持较低的过度拒绝率。我们还证明，扩展对抗技能覆盖范围而非仅增加数据规模，是防御新型攻击的关键。

---

### Any-Depth Alignment: Unlocking Innate Safety Alignment of LLMs to Any-Depth

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiawei Zhang, Andrew Estornell, David D. Baek, Bo Li, Xiaojun Xu
- **Keywords**: Large Language Models, Any-Depth Alignment, Deep-prefill attacks, Safety token, Inference-time defense
- **OpenReview**: https://openreview.net/forum?id=0fuYOuJyzl
- **PDF**: https://openreview.net/pdf?id=0fuYOuJyzl

**Abstract**

Large Language Models (LLMs) exhibit strong but shallow alignment: they directly refuse harmful queries when a refusal is expected at the very start of an assistant turn, yet this protection collapses once a harmful continuation is underway (either through the adversarial attacks or via harmful assistant-prefill attacks). This raises a fundamental question: _Can the innate shallow alignment in LLMs be unlocked to ensure safety at arbitrary generation depths?_ To achieve this goal, we propose Any-Depth Alignment (ADA) an effective inference-time defense with negligible overhead. ADA is built based on our observation that alignment is concentrated in the _assistant header tokens_ through repeated use in shallow-refusal training, and these tokens possess the model’s strong alignment priors.  By reintroducing these tokens mid-stream, ADA induces the model to reassess harmfulness and recover refusals at _any point in generation_. Across diverse open-source model families (Llama, Gemma, Mistral, Qwen, DeepSeek, and gpt-oss), ADA achieves robust safety performance _without requiring any changes to the base model's parameters_. It secures a near-100% refusal rate against challenging adversarial prefill attacks ranging from dozens to thousands of tokens. Furthermore, ADA reduces the average success rate of prominent adversarial prompt attacks (such as GCG, AutoDAN, PAIR, and TAP) to below 3%. This is all accomplished while preserving benign utility with minimal over-refusal and maintaining resilience even after the base model undergoes subsequent instruction tuning.

**Abstract (Chinese)**

大型语言模型 (LLMs) 表现出强大但浅层的对齐：当在助手回合起始处预期拒绝有害查询时，它们会直接拒绝，然而一旦有害延续开始（通过对抗攻击或有害助手预填充攻击），这种保护就会崩溃。这引发了一个根本性问题：_大型语言模型中固有的浅层对齐能否被解锁，以确保任意生成深度下的安全性？_ 为实现这一目标，我们提出任意深度对齐 (ADA)，这是一种有效的推理时防御，带有可忽略的开销。ADA 基于我们的观察，即对齐通过浅层拒绝训练中的重复使用而集中在_助手头部标记_中，这些标记具有模型的强大对齐先验。通过在生成过程中重新引入这些标记，ADA 诱导模型在_生成过程中的任意点_重新评估有害性并恢复拒绝。在多种开源模型家族（Llama、Gemma、Mistral、Qwen、DeepSeek 和 gpt-oss）中，ADA 在_无需对基础模型参数进行任何更改_的情况下实现了稳健的安全性能。它针对从数十到数千个标记的挑战性对抗预填充攻击，确保了近 100% 的拒绝率。此外，ADA 将著名对抗提示攻击（如 GCG、AutoDAN、PAIR 和 TAP）的平均成功率降低至 3% 以下。这一切均在保留无害效用的同时实现，过度拒绝最小，并即使在基础模型经过后续指令微调后仍保持鲁棒性。

---

### CERTIFIED VS. EMPIRICAL ADVERSARIAL ROBUSTNESS VIA HYBRID CONVOLUTIONS WITH ATTENTION STOCHASTICITY

- **Venue**: ICLR 2026 Poster
- **Authors**: Joy Dhar, Song Xia, Manish Kumar Pandey, Maryam Haghighat, Azadeh Alavi, Ferdous Sohel, Wenyu Zhang, Nayyar Zaidi
- **Keywords**: Certified Defense, Empirical Defense, Adversarial Robustness
- **OpenReview**: https://openreview.net/forum?id=sYk9GaFHEf
- **PDF**: https://openreview.net/pdf?id=sYk9GaFHEf

**Abstract**

We introduce Hybrid Convolutions with Attention Stochasticity (HyCAS), an adversarial defense that narrows the long-standing gap between provable robustness under ℓ2 certificates and empirical robustness against strong ℓ∞ attacks, while preserving strong generalization across diverse imaging benchmarks. HyCAS unifies deterministic and randomized principles by coupling 1-Lipschitz, spectrally normalized convolutions with two stochastic components—spectral normalized random-projection filters and a randomized attention-noise mechanism—to realize a randomized defense. Injecting smoothing randomness inside the architecture yields an overall ≤ 2-Lipschitz network with formal certificates. Extensive experiments on diverse imaging benchmarks—including CIFAR-10/100, ImageNet-1k, NIH Chest X-ray, HAM10000—show that HyCAS surpasses prior leading certified and empirical defenses, boosting certified accuracy by up to ≈ 7.3% (on NIH Chest X-ray) and empirical robustness by up to ≈ 3.1% (on HAM10000), without sacrificing clean accuracy. These results show that a randomized Lipschitz constrained architecture can simultaneously improve both certified ℓ2 and empirical ℓ∞ adversarial robustness, thereby supporting safer deployment of deep models in high-stakes applications.

**Abstract (Chinese)**

我们提出了一种带有注意力随机性的混合卷积（HyCAS），这是一种对抗防御方法，能够缩小ℓ₂证书下可证明鲁棒性与针对强ℓ∞攻击的经验鲁棒性之间的长期差距，同时在多种图像基准上保持强大的泛化能力。HyCAS通过将1-利普希茨谱归一化卷积与两个随机组件——谱归一化随机投影滤波器和随机注意力噪声机制——耦合，从而统一确定性和随机性原则，实现随机防御。在架构内部注入平滑随机性，可产生整体≤2-利普希茨网络，并具备正式证书。在多种图像基准（包括CIFAR-10/100、ImageNet-1k、NIH胸部X射线、HAM10000）上的广泛实验表明，HyCAS超越了先前的领先认证防御和经验防御，在认证准确率上提升高达≈7.3%（NIH胸部X射线数据集），在经验鲁棒性上提升高达≈3.1%（HAM10000数据集），且不牺牲干净准确率。这些结果表明，随机利普希茨约束架构能够同时提升认证ℓ₂鲁棒性和经验ℓ∞对抗鲁棒性，从而支持深度模型在高风险应用中的更安全部署。

---

### Certifying the Full YOLO Pipeline: A Probabilistic Verification Approach

- **Venue**: ICLR 2026 Poster
- **Authors**: Zongxin Liu, Lijia Yu, Tao Lin, Zhiming Chi, Lijun Zhang
- **Keywords**: Probabilistic Verification, Formal Verification, Object Detection, Safety Guaranteen
- **OpenReview**: https://openreview.net/forum?id=AMCFpquOtZ
- **PDF**: https://openreview.net/pdf?id=AMCFpquOtZ

**Abstract**

Object detection systems are essential in safety-critical applications, but they are vulnerable to object disappearance (OD) threats, in which valid objects become undetected under small input perturbations, creating serious risks. This paper addresses the problem of verifying the robustness of YOLO (You Only Look Once) networks against OD by proposing a three-step probabilistic verification framework: (1) estimating output ranges under a distribution of input perturbations, (2) formally verifying the Non-Maximum Suppression (NMS) process within these ranges, and (3) iteratively refining the results to reduce over-approximation. The framework scales to practical YOLO models. Both theoretical analysis and experimental results demonstrate that our method achieves comparable probabilistic guarantees and provides tighter Intersection-over-Union (IoU) lower bounds while requiring significantly fewer samples than existing methods.

**Abstract (Chinese)**

目标检测系统在安全关键应用中至关重要，但它们容易受到对象消失 (OD) 威胁的影响，在这种威胁下，有效对象在小输入扰动下变得无法检测，从而造成严重风险。本文通过提出一个三步概率验证框架来解决验证 YOLO（You Only Look Once）网络对 OD 的鲁棒性问题：(1) 在输入扰动分布下估计输出范围，(2) 在这些范围内正式验证非极大值抑制 (NMS) 过程，以及 (3) 迭代细化结果以减少过度逼近。该框架可扩展到实际的 YOLO 模型。理论分析和实验结果均表明，我们的方法实现了与现有方法相当的概率保证，并提供了更紧的交并比 (IoU) 下界，同时所需样本数量显著少于现有方法。

---

### DRIFT: Divergent Response in Filtered Transformations for Robust Adversarial Defense

- **Venue**: ICLR 2026 Poster
- **Authors**: Amira Guesmi, Muhammad Shafique
- **Keywords**: Adversarial Robustness, Transferability of Adversarial Attacks, Randomized Defenses, Gradient Consensus
- **OpenReview**: https://openreview.net/forum?id=AYH7uBK1Gg
- **PDF**: https://openreview.net/pdf?id=AYH7uBK1Gg

**Abstract**

Deep neural networks remain highly vulnerable to adversarial examples, and most defenses collapse once gradients can be reliably estimated. We identify \emph{gradient consensus}—the tendency of randomized transformations to yield aligned gradients—as a key driver of adversarial transferability. Attackers exploit this consensus to construct perturbations that remain effective across transformations. We introduce \textbf{DRIFT} (Divergent Response in Filtered Transformations), a stochastic ensemble of lightweight, learnable filters trained to actively disrupt gradient consensus. Unlike prior randomized defenses that rely on gradient masking, DRIFT enforces \emph{gradient dissonance} by maximizing divergence in Jacobian- and logit-space responses while preserving natural predictions. Our contributions are threefold: (i) we formalize gradient consensus and provide a theoretical analysis linking consensus to transferability; (ii) we propose a consensus-divergence training strategy combining prediction consistency, Jacobian separation, logit-space separation, and adversarial robustness; and (iii) we show that DRIFT achieves substantial robustness gains on ImageNet across CNNs and Vision Transformers, outperforming state-of-the-art preprocessing, adversarial training, and diffusion-based defenses under adaptive white-box, transfer-based, and gradient-free attacks. DRIFT delivers these improvements with negligible runtime and memory cost, establishing gradient divergence as a practical and generalizable principle for adversarial defense.

**Abstract (Chinese)**

深度神经网络仍然高度易受对抗样本攻击，且大多数防御方法一旦梯度能够可靠估计就会失效。我们识别出\emph{梯度共识}——随机变换产生对齐梯度的倾向——作为对抗转移性的关键驱动因素。攻击者利用这种共识来构建在变换间保持有效的扰动。我们引入\textbf{DRIFT}（过滤变换中的发散响应），这是一个随机集成，由轻量级、可学习滤波器组成，这些滤波器经过训练以主动破坏梯度共识。与先前依赖梯度掩蔽的随机防御不同，DRIFT 通过最大化 Jacobian 和 logit 空间响应中的发散来强制执行\emph{梯度失谐}，同时保留自然预测。我们的贡献有三方面：(i) 我们形式化了梯度共识，并提供了将共识与转移性联系起来的理论分析；(ii) 我们提出了一种共识-发散训练策略，结合预测一致性、Jacobian 分离、logit 空间分离和对抗鲁棒性；(iii) 我们展示了 DRIFT 在 ImageNet 上针对 CNNs 和视觉 Transformer 实现了实质性鲁棒性提升，在自适应白盒、转移-based 和无梯度攻击下优于最先进的预处理、对抗训练和基于扩散的防御。DRIFT 以可忽略的运行时和内存成本实现了这些改进，将梯度发散确立为对抗防御的一种实用且可泛化的原则。

---

### Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Kyle O'Brien, Stephen Casper, Quentin Gregory Anthony, Tomek Korbak, Robert Kirk, Xander Davies, Ishan Mishra, Geoffrey Irving, Yarin Gal, Stella Biderman
- **Keywords**: data filtering, model tampering, unlearning, robustness, open-weight, open-source, safety, biorisk
- **OpenReview**: https://openreview.net/forum?id=xcf0QcTcGS
- **PDF**: https://openreview.net/pdf?id=xcf0QcTcGS

**Abstract**

Open-weight AI systems offer unique benefits, including enhanced transparency, open research, and decentralized access. However, they are vulnerable to tampering attacks which can efficiently elicit harmful behaviors by modifying weights or activations. Currently, there is not yet a robust science of open-weight model risk management. Existing safety fine-tuning methods and other post-training techniques have struggled to make LLMs resistant to more than a few dozen steps of adversarial fine-tuning. In this paper, we investigate whether filtering text about dual-use topics from training data can prevent unwanted capabilities and serve as a more tamper-resistant safeguard. We introduce a multi-stage pipeline for scalable data filtering and show that it offers a tractable and effective method for minimizing biothreat proxy knowledge in LLMs. We pretrain multiple 6.9B-parameter models from scratch and find that they exhibit substantial resistance to adversarial fine-tuning attacks on up to 10,000 steps and 300M tokens of biothreat-related text — outperforming existing post-training baselines by over an order of magnitude -- with no observed degradation to unrelated capabilities. However, while filtered models lack internalized dangerous knowledge, we find that they can still leverage such information when it is provided in context (e.g., via search tool augmentation), demonstrating a need for a defense-in-depth approach. Overall, these findings help to establish pretraining data curation as a promising layer of defense for open-weight AI systems

**Abstract (Chinese)**

开源权重AI系统提供了独特优势，包括增强的透明度、开放研究和去中心化访问。然而，它们容易受到篡改攻击的影响，这些攻击可以通过修改权重或激活值高效诱发有害行为。目前，尚缺乏针对开源权重模型风险管理的稳健科学方法。现有的安全微调方法和其他后训练技术难以使大语言模型抵抗超过几十步的对抗微调。本文探讨了从训练数据中过滤双重用途主题文本是否能防止不想要的能力，并作为更抗篡改的安全保障。我们引入了一个可扩展数据过滤的多阶段管道，并证明它为最小化大语言模型中的生物威胁代理知识提供了一种可行且有效的方法。我们从头预训练了多个69亿参数模型，发现它们对多达10,000步和3亿个生物威胁相关文本标记的对抗微调攻击表现出显著抵抗力——比现有后训练基线提高了超过一个数量级——且未观察到对无关能力的退化。然而，虽然过滤模型缺乏内化的危险知识，但我们发现当此类信息在上下文中提供时（例如，通过搜索工具增强），它们仍能利用这些信息，这表明需要纵深防御方法。总体而言，这些发现有助于确立预训练数据整理作为开源权重AI系统的一种有前景的防御层。

---

### Dual Randomized Smoothing: Beyond Global Noise Variance

- **Venue**: ICLR 2026 Poster
- **Authors**: Chenhao Sun, Yuhao Mao, Martin Vechev
- **Keywords**: robustness certification, randomized smoothing
- **OpenReview**: https://openreview.net/forum?id=syvfsHSqm2
- **PDF**: https://openreview.net/pdf?id=syvfsHSqm2

**Abstract**

Randomized Smoothing (RS) is a prominent technique for certifying the robustness of neural networks against adversarial perturbations. With RS, achieving high accuracy at small radii requires a small noise variance, while achieving high accuracy at large radii requires a large noise variance. However, the global noise variance used in the standard RS formulation leads to a fundamental limitation: there exists no global noise variance that simultaneously achieves strong performance at both small and large radii. To break through the global variance limitation, we propose a dual RS framework which enables input-dependent noise variances. To achieve that, we first prove that RS remains valid with input-dependent noise variances, provided the variance is locally constant around each input. Building on this result, we introduce two components which form our dual RS framework: (i) a variance estimator first predicts an optimal noise variance for each input, (ii) this estimated variance is then used by a standard RS classifier. The variance estimator is independently smoothed via RS to ensure local constancy, enabling flexible design. We also introduce efficient training strategies to iteratively optimize the two components involved in the framework. Extensive experiments on the CIFAR-10 dataset demonstrate that our dual RS method provides strong performance for both small and large radii—unattainable with global noise variance—while incurring only a 60\% computational overhead at inference. Moreover, it consistently outperforms prior input-dependent noise approaches across most radii, with particularly large gains at radii 0.5, 0.75, and 1.0, achieving relative improvements of 15.6\%, 20.0\%, and 15.7\%, respectively. On ImageNet, dual RS remains effective across all radii, with 8.6\%, 17.1\% and 9.1\% performance advantages at radii 0.5, 1.0 and 1.5 respectively. Additionally, the proposed dual RS framework naturally provides a routing perspective for certified robustness, improving the accuracy-robustness trade-off with off-the-shelf expert RS models.  Our code is available at https://github.com/eth-sri/Dual-Randomized-Smoothing.

**Abstract (Chinese)**

随机平滑（RS）是一种突出的技术，用于认证神经网络对抗扰动的鲁棒性。使用RS，在小半径处实现高准确率需要小的噪声方差，而在大半径处实现高准确率需要大的噪声方差。然而，标准RS公式中使用的全局噪声方差导致了一个根本限制：不存在同时在小半径和大半径处实现强大性能的全局噪声方差。为了突破全局方差限制，我们提出了一种双RS框架，它支持输入相关的噪声方差。为了实现这一点，我们首先证明了RS在使用输入相关噪声方差时仍然有效，前提是方差在每个输入周围局部恒定。基于这一结果，我们引入了两个组件，形成我们的双RS框架：(i) 一个方差估计器首先为每个输入预测最优噪声方差，(ii) 该估计方差随后被标准RS分类器使用。方差估计器通过RS独立平滑以确保局部恒定性，从而实现灵活设计。我们还引入了高效的训练策略，以迭代优化框架中涉及的两个组件。在CIFAR-10数据集上的广泛实验表明，我们的双RS方法在小半径和大半径处均提供强大性能——这是全局噪声方差无法实现的——同时在推理时仅增加60%的计算开销。此外，它在大多数半径处持续优于先前的输入相关噪声方法，在半径0.5、0.75和1.0处获得特别大的提升，分别实现15.6%、20.0%和15.7%的相对改进。在ImageNet上，双RS在所有半径处保持有效，在半径0.5、1.0和1.5处分别具有8.6%、17.1%和9.1%的性能优势。此外，所提出的双RS框架自然地为认证鲁棒性提供了一个路由视角，使用现成的专家RS模型改善准确率-鲁棒性权衡。我们的代码可在https://github.com/eth-sri/Dual-Randomized-Smoothing获取。

---

### EnsembleSHAP: Faithful and Certifiably Robust Attribution for Random Subspace Method

- **Venue**: ICLR 2026 Poster
- **Authors**: Yanting Wang, Jinyuan Jia
- **Keywords**: Feature attribution, Certified Robustness, Jailbreak Attack
- **OpenReview**: https://openreview.net/forum?id=u0UjdCMPLc
- **PDF**: https://openreview.net/pdf?id=u0UjdCMPLc

**Abstract**

Random subspace method has wide security applications such as providing certified defenses against adversarial and backdoor attacks, and building robustly aligned LLM against jailbreaking attacks. However, the explanation of random subspace method lacks sufficient exploration. Existing state-of-the-art feature attribution methods, such as Shapley value and LIME, are computationally impractical and lacks security guarantee when applied to random subspace method. In this work, we propose EnsembleSHAP, an intrinsically faithful and secure feature attribution for random subspace method that reuses its computational byproducts. Specifically, our feature attribution method is 1) computationally efficient, 2) maintains essential properties of effective feature attribution (such as local accuracy), and 3) offers guaranteed protection against privacy-preserving attacks on feature attribution methods. To the best of our knowledge, this is the first work to establish provable robustness against explanation-preserving attacks. We also perform comprehensive evaluations for our explanation's effectiveness when faced with different empirical attacks, including backdoor attacks, adversarial attacks, and jailbreak attacks. The code is at https://github.com/Wang-Yanting/EnsembleSHAP. WARNING: This document may include content that could be considered harmful.

**Abstract (Chinese)**

随机子空间方法在安全领域有广泛应用，例如提供针对对抗攻击和后门攻击的认证防御，以及构建针对越狱攻击的鲁棒对齐大型语言模型。然而，随机子空间方法的解释性研究尚不足。现有的最先进特征归因方法，如Shapley值和LIME，在应用于随机子空间方法时计算上不可行且缺乏安全保证。本工作中，我们提出EnsembleSHAP，这是一种本质上忠实且安全的随机子空间方法特征归因方法，它重用其计算副产品。具体而言，我们的特征归因方法1) 计算高效，2) 保持有效特征归因的基本属性（如局部准确性），3) 针对特征归因方法的隐私保护攻击提供保证保护。据我们所知，这是第一项建立针对保解释攻击的可证明鲁棒性的工作。我们还对我们的解释在面对不同经验攻击（包括后门攻击、对抗攻击和越狱攻击）时的有效性进行了全面评估。代码位于 https://github.com/Wang-Yanting/EnsembleSHAP。警告：本文档可能包含可能被视为有害的内容。

---

### Exposing and Defending the Achilles' Heel of Video Mixture-of-Experts

- **Venue**: ICLR 2026 Poster
- **Authors**: Songping Wang, Qinglong Liu, Yueming Lyu, Ning Li, Ziwen He, Caifeng Shan
- **Keywords**: Adversarial attacks for Video MoE; Robustness of Video MoE
- **OpenReview**: https://openreview.net/forum?id=8voly42rKo
- **PDF**: https://openreview.net/pdf?id=8voly42rKo

**Abstract**

Mixture-of-Experts (MoE) has demonstrated strong performance in video understanding tasks, yet its adversarial robustness remains underexplored. Existing attack methods often treat MoE as a unified architecture, overlooking the independent and collaborative weaknesses of key components such as routers and expert modules. To fill this gap, we propose Temporal Lipschitz-Guided Attacks (TLGA) to thoroughly investigate component-level vulnerabilities in video MoE models. We first design attacks on the router, revealing its independent weaknesses. Building on this, we introduce Joint Temporal Lipschitz-Guided Attacks (J-TLGA), which collaboratively perturb both routers and experts. This joint attack significantly amplifies adversarial effects and exposes the Achilles’ Heel (collaborative weaknesses) of the MoE architecture. Based on these insights, we further propose Joint Temporal Lipschitz Adversarial Training (J-TLAT). J-TLAT performs joint training to further defend against collaborative weaknesses, enhancing component-wise robustness. Our framework is plug-and-play and reduces inference cost by more than 60% compared with dense models. It consistently enhances adversarial robustness across diverse video datasets and model architectures, effectively mitigating both the independent and collaborative weaknesses of MoE.

**Abstract (Chinese)**

专家混合模型（MoE）在视频理解任务中展现出强大性能，但其对抗鲁棒性仍未得到充分探索。现有的攻击方法通常将MoE视为统一的架构，忽略了路由器和专家模块等关键组件的独立弱点与协作弱点。为填补这一空白，我们提出时序Lipschitz引导攻击（TLGA），以彻底探究视频MoE模型的组件级漏洞。我们首先针对路由器设计攻击，揭示其独立弱点。在此基础上，我们引入联合时序Lipschitz引导攻击（J-TLGA），该方法协作扰动路由器和专家。这种联合攻击显著放大对抗效果，并暴露MoE架构的阿喀琉斯之踵（协作弱点）。基于这些洞见，我们进一步提出联合时序Lipschitz对抗训练（J-TLAT）。J-TLAT通过联合训练进一步防御协作弱点，提升组件级鲁棒性。我们的框架即插即用，与密集模型相比推理成本降低超过60%。它在多样化的视频数据集和模型架构上持续提升对抗鲁棒性，有效缓解MoE的独立弱点与协作弱点。

---

### Expressiveness of Multi-Neuron Convex Relaxations in Neural Network Certification

- **Venue**: ICLR 2026 Poster
- **Authors**: Yuhao Mao, Yani Zhang, Martin Vechev
- **Keywords**: certification, convex relaxation, theory
- **OpenReview**: https://openreview.net/forum?id=f07Kf4pD0f
- **PDF**: https://openreview.net/pdf?id=f07Kf4pD0f

**Abstract**

Neural network certification methods heavily rely on convex relaxations to provide robustness guarantees. However, these relaxations are often imprecise: even the most accurate single-neuron relaxation is incomplete for general ReLU networks, a limitation known as the *single-neuron convex barrier*. While multi-neuron relaxations have been heuristically applied to address this issue, two central questions arise: (i) whether they overcome the convex barrier, and if not, (ii) whether they offer theoretical capabilities beyond those of single-neuron relaxations.
In this work, we present the first rigorous analysis of the expressiveness of multi-neuron relaxations. Perhaps surprisingly, we show that they are inherently incomplete, even when allocated sufficient resources to capture finitely many neurons and layers optimally. This result extends the single-neuron barrier to a *universal convex barrier* for neural network certification. 
On the positive side, we show that completeness can be achieved by either (i) augmenting the network with a polynomial number of carefully designed ReLU neurons or (ii) partitioning the input domain into convex sub-polytopes, thereby distinguishing multi-neuron relaxations from single-neuron ones which are unable to realize the former and have worse partition complexity for the latter.
Our findings establish a foundation for multi-neuron relaxations and point to new directions for certified robustness, including training methods tailored to multi-neuron relaxations and verification methods with multi-neuron relaxations as the main subroutine.

**Abstract (Chinese)**

神经网络认证方法高度依赖凸松弛来提供鲁棒性保证。然而，这些松弛往往不够精确：即使是最精确的单神经元松弛，对于一般的ReLU网络也是不完备的，这一局限性被称为单神经元凸壁垒。虽然多神经元松弛已被启发式地应用于解决这一问题，但由此产生了两个核心问题：(i) 它们是否克服了凸壁垒，如果没有，(ii) 它们是否提供了超越单神经元松弛的理论能力。

在本工作中，我们首次对多神经元松弛的表达能力进行了严格分析。令人惊讶的是，我们证明它们本质上是不完备的，即使分配足够的资源来最优捕捉有限数量的神经元和层。这一结果将单神经元壁垒扩展为神经网络认证的通用凸壁垒。

在积极方面，我们证明完备性可以通过以下两种方式实现：(i) 用多项式数量的精心设计的ReLU神经元增强网络，或(ii) 将输入域分区为凸子多面体，从而将多神经元松弛与单神经元松弛区分开来，后者无法实现前者，并且在后者中的分区复杂度更差。

我们的发现为多神经元松弛奠定了基础，并指明了认证鲁棒性的新方向，包括针对多神经元松弛的训练方法以及以多神经元松弛为主程序的验证方法。

---

### Fine-Grained Iterative Adversarial Attacks with Limited Computation Budget

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhichao Hou, Weizhi Gao, Xiaorui Liu
- **Keywords**: Adversarial Attack, Efficiency, Robustness
- **OpenReview**: https://openreview.net/forum?id=GW9sp1g9qh
- **PDF**: https://openreview.net/pdf?id=GW9sp1g9qh

**Abstract**

This work tackles a critical challenge in AI safety research under limited compute: given a fixed computation budget, how can one maximize the strength of iterative adversarial attacks? Coarsely reducing the number of attack iterations lowers cost but substantially weakens effectiveness. To fulfill the attainable attack efficacy within a constrained budget, we propose a fine-grained control mechanism that selectively recomputes layer activations across both iteration-wise and layer-wise levels. Extensive experiments show that our method consistently outperforms existing baselines at equal cost. Moreover, when integrated into adversarial training, it attains comparable  performance with only 30\% of the original budget.

**Abstract (Chinese)**

本工作针对有限计算资源下AI安全研究中的一个关键挑战：给定固定的计算预算，如何最大化迭代对抗攻击的强度？粗略减少攻击迭代次数可以降低成本，但会显著削弱有效性。为了在受限预算内实现可达到的攻击效能，我们提出了一种细粒度控制机制，该机制在迭代级和层级水平上选择性地重新计算层激活。广泛实验表明，我们的方法在相同成本下始终优于现有基线。而且，当集成到对抗训练中时，它仅需原预算的30\%即可达到相当的性能。

---

### Get RICH or Die Scaling: Profitably Trading Inference Compute for Robustness

- **Venue**: ICLR 2026 Poster
- **Authors**: Tavish Malcolm McDonald, Bo Lei, Stanislav Fort, Bhavya Kailkhura, Brian R. Bartoldson
- **Keywords**: adversarial robustness, inference-compute scaling, VLMs, efficiency
- **OpenReview**: https://openreview.net/forum?id=PLZx2hpauY
- **PDF**: https://openreview.net/pdf?id=PLZx2hpauY

**Abstract**

Models are susceptible to adversarially out-of-distribution (OOD) data despite large training-compute investments into their robustification. Zaremba et al. (2025) make progress on this problem at test time, showing LLM reasoning improves satisfaction of model specifications designed to thwart attacks, resulting in a correlation between reasoning effort and robustness to jailbreaks. However, this benefit of test compute fades when attackers are given access to gradients or multimodal inputs. We address this gap, clarifying that  inference-compute offers benefits even in such cases. Our approach argues that compositional generalization, through which OOD data is understandable via its in-distribution (ID) components, enables adherence to defensive specifications on adversarially OOD inputs. Namely, we posit the Robustness from Inference Compute Hypothesis (RICH): inference-compute defenses profit as the model's training data better reflects the attacked data’s components. We empirically support this hypothesis across vision language model and attack types, finding robustness gains from test-time compute if specification following on OOD data is unlocked by compositional generalization. For example, InternVL 3.5 gpt-oss 20B gains little robustness when its test compute is scaled, but such scaling adds significant robustness if we first robustify its vision encoder. This correlation of inference-compute's robustness benefit with base model robustness is the rich-get-richer dynamic of the RICH: attacked data components are more ID for robustified models, aiding compositional generalization to OOD data. Thus, we advise layering train-time and test-time defenses to obtain their synergistic benefit.

**Abstract (Chinese)**

尽管在模型鲁棒化上投入了大量训练计算资源，模型仍易受对抗性分布外（OOD）数据的影响。Zaremba 等（2025）在测试时对此问题取得了进展，他们展示了 LLM 推理能够提升对设计用于挫败攻击的模型规范的满足度，从而导致推理努力与对越狱攻击的鲁棒性之间存在相关性。然而，当攻击者获得梯度或多模态输入的访问权限时，这种测试计算的好处会减弱。我们填补了这一空白，阐明即使在这种情况下，推理计算也能提供益处。我们的方法认为，通过组合泛化，OOD 数据可以通过其分布内（ID）组件来理解，从而使对抗性 OOD 输入能够遵守防御规范。具体而言，我们提出推理计算鲁棒性假设（RICH）：当模型的训练数据更好地反映被攻击数据的组件时，推理计算防御将获益。我们实证支持这一假设，涵盖视觉语言模型和多种攻击类型，发现如果通过组合泛化解锁了对 OOD 数据的规范遵循，则测试时计算能带来鲁棒性提升。例如，InternVL 3.5 gpt-oss 20B 在测试计算扩展时鲁棒性提升甚微，但如果我们首先鲁棒化其视觉编码器，则此类扩展将显著增加鲁棒性。推理计算鲁棒性益处与基础模型鲁棒性的这种相关性就是 RICH 的“富者愈富”动态：对于鲁棒化模型，被攻击数据的组件更接近 ID，从而有助于对 OOD 数据的组合泛化。因此，我们建议叠加训练时和测试时防御，以获得它们的协同益处。

---

### Image Can Bring Your Memory Back: A Novel Multi-Modal Guided Attack against Image Generation Model Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Renyang Liu, Guanlin Li, Tianwei Zhang, See-Kiong Ng
- **Keywords**: Adversarial attacks, Machine unlearning, Image generation model unlearning, AI safety, Stable Diffusion model, AIGC
- **OpenReview**: https://openreview.net/forum?id=lsEnQ47VXh
- **PDF**: https://openreview.net/pdf?id=lsEnQ47VXh

**Abstract**

Recent advances in diffusion-based image generation models (IGMs), such as Stable Diffusion (SD), have substantially improved the quality and diversity of AI-generated content. However, these models also pose ethical, legal, and societal risks, including the generation of harmful, misleading, or copyright-infringing material. Machine unlearning (MU) has emerged as a promising mitigation by selectively removing undesirable concepts from pretrained models, yet the robustness of existing methods, particularly under multi-modal adversarial inputs, remains insufficiently explored. To address this gap, we propose RECALL, a multi-modal adversarial framework for systematically evaluating and compromising the robustness of unlearned IGMs. Unlike prior approaches that primarily optimize adversarial text prompts, RECALL exploits the native multi-modal conditioning of diffusion models by efficiently optimizing adversarial image prompts guided by a single semantically relevant reference image. Extensive experiments across ten state-of-the-art unlearning methods and diverse representative tasks show that RECALL consistently surpasses existing baselines in adversarial effectiveness, computational efficiency, and semantic fidelity to the original prompt. These results reveal critical vulnerabilities in current unlearning pipelines and underscore the need for more robust, verifiable unlearning mechanisms. More than just an attack, RECALL also serves as an auditing tool for model owners and unlearning practitioners, enabling systematic robustness evaluation. Code and data are available at https://github.com/ryliu68/RECALL.

**Abstract (Chinese)**

最近在基于扩散的图像生成模型（IGMs）方面的进展，例如Stable Diffusion（SD），已大幅提升了AI生成内容的质量和多样性。然而，这些模型也带来了伦理、法律和社会风险，包括生成有害、误导性或侵犯版权的材料。机器遗忘（MU）作为一种有前景的缓解方法，通过从预训练模型中选择性地移除不良概念而崭露头角，然而现有方法的鲁棒性，特别是面对多模态对抗输入时，仍未得到充分探索。为填补这一空白，我们提出了RECALL，一个用于系统评估和破坏已遗忘IGMs鲁棒性的多模态对抗框架。与先前主要优化对抗文本提示的方法不同，RECALL利用扩散模型的原生多模态条件，通过由单一语义相关参考图像引导的高效优化对抗图像提示。在十种最先进的遗忘方法和多样化代表性任务上的大量实验表明，RECALL在对抗有效性、计算效率以及对原始提示的语义保真度方面始终优于现有基线。这些结果揭示了当前遗忘管道的关键漏洞，并强调了需要更鲁棒、可验证的遗忘机制。RECALL不仅仅是一种攻击，还作为模型所有者和遗忘从业者的审计工具，支持系统鲁棒性评估。代码和数据可在https://github.com/ryliu68/RECALL获取。

---

### LingoLoop Attack: Trapping MLLMs via Linguistic Context and State Entrapment into Endless Loops

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiyuan Fu, Kaixun Jiang, Lingyi Hong, Jinglun Li, HaiJing Guo, Dingkang Yang, Zhaoyu Chen, Wenqiang Zhang
- **Keywords**: Multimodal Large Language Models, Energy-latency Attack
- **OpenReview**: https://openreview.net/forum?id=kxEM2vc7ne
- **PDF**: https://openreview.net/pdf?id=kxEM2vc7ne

**Abstract**

Multimodal Large Language Models (MLLMs) have shown great promise but require substantial computational resources during inference. Attackers can exploit this by inducing excessive output, leading to resource exhaustion and service degradation. Prior energy-latency attacks aim to increase generation time by broadly shifting the output token distribution away from the EOS token, but they neglect the influence of token-level Part-of-Speech (POS) characteristics on EOS and sentence-level structural patterns on output counts, limiting their efficacy. To address this, we propose \textbf{LingoLoop}, an attack designed to induce MLLMs to generate excessively verbose and repetitive sequences. First, we find that the POS tag of a token strongly affects the likelihood of generating an EOS token. Based on this insight, we propose a \textbf{POS-Aware Delay Mechanism} to postpone EOS token generation by adjusting attention weights guided by POS information. Second, we identify that constraining output diversity to induce repetitive loops is effective for sustained generation. We introduce a \textbf{Generative Path Pruning Mechanism} that limits the magnitude of hidden states, encouraging the model to produce persistent loops. Extensive experiments on models like Qwen2.5-VL-3B demonstrate LingoLoop's powerful ability to trap them in generative loops; it consistently drives them to their generation limits and, when those limits are relaxed, can induce outputs with up to \textbf{367$\times$} more tokens than clean inputs, triggering a commensurate surge in energy consumption. These findings expose significant MLLMs' vulnerabilities, posing challenges for their reliable deployment.

**Abstract (Chinese)**

多模态大语言模型（MLLMs）显示出巨大潜力，但其推理过程需要大量计算资源。攻击者可以通过诱导过度输出来利用这一点，从而导致资源耗尽和服务降级。先前的能耗-延迟攻击旨在通过广泛地将输出标记分布从 EOS 标记移开来增加生成时间，但它们忽略了标记级词性（POS）特征对 EOS 的影响以及句子级结构模式对输出数量的影响，从而限制了其有效性。为解决这一问题，我们提出了\textbf{LingoLoop}，一种旨在诱导 MLLMs 生成过度冗长且重复序列的攻击。首先，我们发现标记的词性标签强烈影响生成 EOS 标记的可能性。基于这一洞见，我们提出了一种\textbf{词性感知延迟机制}，通过调整由词性信息引导的注意力权重来推迟 EOS 标记的生成。其次，我们发现限制输出多样性以诱导重复循环对于持续生成是有效的。我们引入了一种\textbf{生成路径剪枝机制}，它限制隐藏状态的幅度，鼓励模型产生持久循环。在 Qwen2.5-VL-3B 等模型上的广泛实验证明了 LingoLoop 将它们困在生成循环中的强大能力；它始终将它们驱动到生成极限，并且当这些极限放宽时，可以诱导输出比干净输入多达\textbf{367$\times$}的标记，从而引发相应的能耗激增。这些发现暴露了 MLLMs 的重大漏洞，为其可靠部署带来了挑战。

---

### MSCR: Exploring the Vulnerability of LLMs’ Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhishen Sun, Guang Dai, Haishan Ye
- **Keywords**: Large Language Models, Adversarial Attack, Mathematical Reasoning
- **OpenReview**: https://openreview.net/forum?id=ijOAhcHI7S
- **PDF**: https://openreview.net/pdf?id=ijOAhcHI7S

**Abstract**

LLMs demonstrate performance comparable to human abilities in complex tasks such as mathematical reasoning, but their robustness in mathematical reasoning under minor input perturbations still lacks systematic investigation. Existing methods generally suffer from limited scalability, weak semantic preservation, and high costs. Therefore, we propose MSCR, an automated adversarial attack method based on multi-source candidate replacement. By combining three information sources including cosine similarity in the embedding space of LLMs, the WordNet dictionary, and contextual predictions from a masked language model, we generate for each word in the input question a set of semantically similar candidates, which are then filtered and substituted one by one to carry out the attack. We conduct large-scale experiments on LLMs using the GSM8K and MATH500 benchmarks. The results show that even a slight perturbation involving only a single word can significantly reduce the accuracy of all models, with the maximum drop reaching 49.89\% on GSM8K and 35.40\% on MATH500, _while preserving the high semantic consistency of the perturbed questions._ Further analysis reveals that perturbations not only lead to incorrect outputs but also substantially increase the average response length, which results in more redundant reasoning paths and higher computational resource consumption. These findings highlight the robustness deficiencies and efficiency bottlenecks of current LLMs in mathematical reasoning tasks.

**Abstract (Chinese)**

大语言模型（LLMs）在数学推理等复杂任务中表现出与人类能力相当的性能，但其在轻微输入扰动下的数学推理鲁棒性仍缺乏系统性研究。现有方法通常存在可扩展性有限、语义保持能力弱以及成本高等问题。因此，我们提出MSCR，一种基于多源候选替换的自动化对抗攻击方法。通过结合三种信息源，包括LLMs嵌入空间中的余弦相似度、WordNet词典以及掩码语言模型的上下文预测，我们为输入问题中的每个单词生成一组语义相似的候选词，然后逐一过滤并替换以执行攻击。我们在GSM8K和MATH500基准上对LLMs进行了大规模实验。结果表明，即使仅涉及单个单词的轻微扰动也能显著降低所有模型的准确率，在GSM8K上最大下降幅度达49.89%，在MATH500上达35.40%，同时保持了扰动问题的高度语义一致性。进一步分析揭示，扰动不仅导致错误输出，还显著增加了平均响应长度，从而导致更多冗余推理路径和更高的计算资源消耗。这些发现突显了当前LLMs在数学推理任务中的鲁棒性缺陷和效率瓶颈。

---

### Nasty Adversarial Training:  A Probability Sparsity Perspective for Robustness Enhancement

- **Venue**: ICLR 2026 Poster
- **Authors**: Yuhang Zhou, Zhongyun Hua, Zhaoquan Gu, Keke Tang, Rushi Lan, Yushu Zhang, Qing Liao, Leo Yu Zhang
- **Keywords**: adversarial training, adversarial robustness
- **OpenReview**: https://openreview.net/forum?id=eCXpA14KHd
- **PDF**: https://openreview.net/pdf?id=eCXpA14KHd

**Abstract**

The vulnerability of deep neural networks to adversarial examples poses significant challenges to their reliable deployment. Among existing empirical defenses, adversarial training and robust distillation have proven the most effective. In this paper, we identify a property originally associated with model intellectual property, i.e., probability sparsity induced by nasty training, and demonstrate that it can also provide interpretable improvements to adversarial robustness. 
We begin by analyzing how nasty training induces sparse probability distributions and qualitatively explore the spatial metric preferences this sparsity introduces to the model. Building on these insights, we propose a simple yet effective adversarial training method, nasty adversarial training (NAT), which incorporates probability sparsity as a regularization mechanism to boost adversarial robustness. Both theoretical analysis and experimental results validate the effectiveness of NAT, highlighting its potential to enhance the adversarial robustness of deep neural networks in an interpretable manner.

**Abstract (Chinese)**

深度神经网络对抗样本的脆弱性对其可靠部署构成了重大挑战。在现有的经验防御方法中，对抗训练和鲁棒蒸馏已被证明是最有效的。本文识别出原本与模型知识产权相关的一种属性，即nasty训练诱导的概率稀疏性，并证明它也可以为对抗鲁棒性提供可解释的改进。

我们首先分析nasty训练如何诱导稀疏概率分布，并定性探索这种稀疏性为模型引入的空间度量偏好。基于这些洞见，我们提出了一种简单而有效的对抗训练方法，即nasty对抗训练（NAT），它将概率稀疏性作为正则化机制来提升对抗鲁棒性。理论分析和实验结果均验证了NAT的有效性，突显了其以可解释方式增强深度神经网络对抗鲁棒性的潜力。

---

### On the Interaction of Compressibility and Adversarial Robustness

- **Venue**: ICLR 2026 Poster
- **Authors**: Melih Barsbey, Antônio H. Ribeiro, Umut Simsekli, Tolga Birdal
- **Keywords**: compressibility, compression, adversarial robustness, generalization, safety
- **OpenReview**: https://openreview.net/forum?id=zSsNzxjWP4
- **PDF**: https://openreview.net/pdf?id=zSsNzxjWP4

**Abstract**

Modern neural networks are expected to simultaneously satisfy a host of desirable properties: accurate fitting to training data, generalization to unseen inputs, parameter and computational efficiency, and robustness to adversarial perturbations. While compressibility and robustness have each been studied extensively, a unified understanding of their interaction still remains elusive. In this work, we develop a principled framework to analyze how different forms of structured compressibility - such as neuron-level sparsity and spectral compressibility - affect adversarial robustness. We show that these forms of compression can induce a small number of highly sensitive directions in the representation space, which adversaries can exploit to construct effective perturbations. Our analysis yields a robustness bound that reveals how neuron and spectral compressibility impact $\ell_\infty$ and $\ell_2$ robustness via their effects on the learned representations. Crucially, the vulnerabilities we identify arise irrespective of how compressibility is achieved - whether via regularization, architectural bias, or implicit learning dynamics. Through empirical evaluations across synthetic and realistic tasks, we confirm our theoretical predictions, and further demonstrate that these vulnerabilities persist under adversarial training and transfer learning, and contribute to the emergence of universal adversarial perturbations.  Our findings show a fundamental tension between structured compressibility and robustness and highlight new pathways for designing models that are both efficient and safe.

**Abstract (Chinese)**

现代神经网络被期望同时满足一系列理想属性：准确拟合训练数据、对未见输入的泛化、参数和计算效率，以及对对抗扰动的鲁棒性。虽然压缩性和鲁棒性已被分别广泛研究，但对其交互作用的统一理解仍遥遥无期。本工作中，我们开发了一个原则性框架，用于分析不同形式的结构化压缩性——如神经元级稀疏性和谱压缩性——如何影响对抗鲁棒性。我们证明，这些压缩形式会在表示空间中诱发少量高度敏感方向，对手可利用这些方向构建有效扰动。我们的分析得出了一个鲁棒性界，揭示了神经元和谱压缩性通过对学习表示的影响，如何作用于$\ell_\infty$和$\ell_2$鲁棒性。关键的是，我们识别出的这些漏洞独立于压缩性的实现方式——无论是通过正则化、架构偏差，还是隐式学习动态。通过在合成和真实任务上的实证评估，我们验证了理论预测，并进一步证明这些漏洞在对抗训练和迁移学习下持续存在，并促成了通用对抗扰动的出现。我们的发现揭示了结构化压缩性和鲁棒性之间的根本张力，并为设计既高效又安全的模型开辟了新路径。

---

### Optimal Transport-Induced Samples against Out-of-Distribution Overconfidence

- **Venue**: ICLR 2026 Poster
- **Authors**: Keke Tang, Ziyong Du, Xiaofei Wang, Weilong Peng, Peican Zhu, Zhihong Tian
- **Keywords**: out-of-distribution, overconfidence, optimal transport
- **OpenReview**: https://openreview.net/forum?id=r83AdmvULT
- **PDF**: https://openreview.net/pdf?id=r83AdmvULT

**Abstract**

Deep neural networks (DNNs) often produce overconfident predictions on out-of-distribution (OOD) inputs, undermining their reliability in open-world environments. Singularities in semi-discrete optimal transport (OT) mark regions of semantic ambiguity, where classifiers are particularly prone to unwarranted high-confidence predictions. Motivated by this observation, we propose a principled framework to mitigate OOD overconfidence by leveraging the geometry of OT-induced singular boundaries. Specifically, we formulate an OT problem between a continuous base distribution and the latent embeddings of training data, and identify the resulting singular boundaries. By sampling near these boundaries, we construct a class of OOD inputs, termed optimal transport-induced OOD samples (OTIS), which are geometrically grounded and inherently semantically ambiguous. During training, a confidence suppression loss is applied to OTIS to guide the model toward more calibrated predictions in structurally uncertain regions. Extensive experiments show that our method significantly alleviates OOD overconfidence and outperforms state-of-the-art methods.

**Abstract (Chinese)**

深度神经网络 (DNNs) 常常在分布外 (OOD) 输入上产生过度自信的预测，从而削弱其在开放世界环境中的可靠性。半离散最优传输 (OT) 中的奇异点标记了语义模糊区域，在这些区域中，分类器特别容易产生无理的高置信度预测。受此观察的启发，我们提出一个原则性框架，通过利用 OT 诱导的奇异边界的几何特性来缓解 OOD 过度自信问题。具体而言，我们在连续基分布与训练数据的潜在嵌入之间制定了一个 OT 问题，并识别出由此产生的奇异边界。通过在这些边界附近采样，我们构建了一类 OOD 输入，称为最优传输诱导的 OOD 样本 (OTIS)，这些样本具有几何基础并本质上语义模糊。在训练过程中，对 OTIS 应用置信度抑制损失，以引导模型在结构不确定区域中产生更校准的预测。大量实验表明，我们的方法显著缓解了 OOD 过度自信问题，并优于最先进的方法。

---

### Out of the Shadows: Exploring a Latent Space for Neural Network Verification

- **Venue**: ICLR 2026 Poster
- **Authors**: Lukas Koller, Tobias Ladner, Matthias Althoff
- **Keywords**: Neural Network Verification, Zonotope, Set-Based Computing, Latent Space, Formal Methods
- **OpenReview**: https://openreview.net/forum?id=cYSt0KOQDD
- **PDF**: https://openreview.net/pdf?id=cYSt0KOQDD

**Abstract**

Neural networks are ubiquitous. However, they are often sensitive to small input changes.
Hence, to prevent unexpected behavior in safety-critical applications, their formal verification -- a notoriously hard problem -- is necessary.
Many state-of-the-art verification algorithms use reachability analysis or abstract interpretation to enclose the set of possible outputs of a neural network.
Often, the verification is inconclusive due to the conservatism of the enclosure.
To address this problem, we propose a novel specification-driven input refinement procedure, i.e., we iteratively enclose the preimage of a neural network for all unsafe outputs to reduce the set of possible inputs to only enclose the unsafe ones. 
For that, we transfer output specifications to the input space by exploiting a latent space, which is an artifact of the propagation of a projection-based set representation through a neural network.
A projection-based set representation, e.g., a zonotope, is a "shadow" of a higher-dimensional set -- a latent space -- that does not change during a set propagation through a neural network.
Hence, the input set and the output enclosure are "shadows" of the same latent space that we can use to transfer constraints.
We present an efficient verification tool for neural networks that uses our iterative refinement to significantly reduce the number of subproblems in a branch-and-bound procedure.
Using zonotopes as a set representation, unlike many other state-of-the-art approaches, our approach can be realized by only using matrix operations, which enables a significant speed-up through efficient GPU acceleration.
We demonstrate that our tool achieves competitive performance compared to the top-ranking tools of the international neural network verification competition.

**Abstract (Chinese)**

神经网络无处不在。然而，它们通常对小的输入变化敏感。因此，为了防止安全关键应用中的意外行为，对它们的形式化验证——一个众所周知的问题——是必要的。许多最先进的验证算法使用可达性分析或抽象解释来包围神经网络的可能输出集。通常，由于包围的保守性，验证结果不确定。为了解决这个问题，我们提出了一种新颖的规范驱动输入精炼过程，即迭代地包围神经网络所有不安全输出的原像，以将可能输入集缩小到仅包围不安全输入。为此，我们利用潜在空间将输出规范转移到输入空间，该潜在空间是基于投影的集合表示通过神经网络传播的产物。基于投影的集合表示，例如区域体，是更高维集合——潜在空间——的“影子”，在集合通过神经网络传播期间不会改变。因此，输入集和输出包围是同一潜在空间的“影子”，我们可以利用它来转移约束。我们提出了一种高效的神经网络验证工具，它使用我们的迭代精炼来显著减少分支定界过程中的子问题数量。使用区域体作为集合表示，与许多其他最先进方法不同，我们的方法仅使用矩阵运算即可实现，这通过高效的GPU加速实现了显著的速度提升。我们展示了我们的工具与国际神经网络验证竞赛中排名最高的工具相比，具有竞争性的性能。

---

### Pay Less Attention to Function Words for Free Robustness of Vision-Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Qiwei Tian, Chenhao Lin, Zhengyu Zhao, Chao Shen
- **Keywords**: Vision-Language Model, Concentrated Attention, Adversarial Robustness
- **OpenReview**: https://openreview.net/forum?id=4K2NNr9W5C
- **PDF**: https://openreview.net/pdf?id=4K2NNr9W5C

**Abstract**

To address the trade-off between robustness and performance for robust VLM, we observe that function words could incur vulnerability of VLMs against cross-modal adversarial attacks, and propose Function-word De-Attention (FDA) accordingly to mitigate the vulnerability brought by function words. Inspired by differential transformers, our FDA calculates the original and the function-word cross-attention within attention heads, and differentially subtracts the latter from the former for more robust alignment. Comprehensive experiments include 2 SOTA baselines under 6 different attacks on 2 downstream tasks, 3 datasets, and 3 models. Overall, our FDA yields an average 18/13/53\% ASR drop with only 0.2/0.3/0.6\% performance drops on the 3 tested models on retrieval, and a 90\% ASR drop with a 0.3\% performance gain on visual grounding. We demonstrate the scalability, generalization, and zero-shot performance of FDA experimentally, as well as in-depth ablation studies and analysis. Code is available at https://github.com/michaeltian108/FDA.

**Abstract (Chinese)**

为了解决鲁棒视觉语言模型（robust VLM）在鲁棒性和性能之间的权衡，我们观察到功能词可能导致视觉语言模型（VLMs）对跨模态对抗攻击的脆弱性，并相应提出功能词去注意力（Function-word De-Attention, FDA）方法，以缓解功能词带来的脆弱性。受差分变换器的启发，我们的FDA在注意力头中计算原始跨注意力和功能词跨注意力，并通过差分方式从前者中减去后者，以实现更鲁棒的对齐。全面实验包括在2个下游任务、3个数据集和3个模型上，使用6种不同攻击对2个最先进基线（SOTA baselines）进行测试。总体而言，我们的FDA在检索任务上使3个测试模型的平均ASR下降18/13/53%，性能仅下降0.2/0.3/0.6%；在视觉定位任务上，ASR下降90%，性能提升0.3%。我们通过实验展示了FDA的可扩展性、泛化性和零样本性能，并进行了深入的消融研究和分析。代码可在https://github.com/michaeltian108/FDA获取。

---

### Robust Adversarial Attacks Against Unknown Disturbance via Inverse Gradient Sample

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhaoyang Zhang, Shen Wang, Runze Liu, Guopu Zhu, Fanghui Sun, Ye Lu, Zeyue Wang, Yihan Yan
- **Keywords**: Adversarial sample, Transferable attack
- **OpenReview**: https://openreview.net/forum?id=WhFS8mxWJh
- **PDF**: https://openreview.net/pdf?id=WhFS8mxWJh

**Abstract**

Adversarial attacks have achieved widespread success in various domains, yet existing methods suffer from significant performance degradation when adversarial examples are subjected to even minor disturbances. In this paper, we propose a novel and robust attack called IGSA (**I**nverse **G**radient **S**ample-based **A**ttack), capable of generating adversarial examples that remain effective under diverse unknown disturbances. IGSA employs an iterative two-step framework: (i) inverse gradient sampling, which searches for the most disruptive direction within the neighborhood of adversarial examples, and (ii) disturbance-guided refinement, which updates adversarial examples via gradient descent along the identified disruptive disturbance. Theoretical analysis reveals that IGSA enhances robustness by increasing the likelihood of adversarial examples within the data distribution. Extensive experiments in both white-box and black-box attack scenarios demonstrate that IGSA significantly outperforms state-of-the-art attacks in terms of robustness against various unknown disturbances. Moreover, IGSA exhibits superior performance when attacking adversarially trained defense models. Code is available at https://github.com/nimingck/IGSA.

**Abstract (Chinese)**

对抗攻击已在各种领域取得了广泛成功，然而，现有的方法在对抗样本受到即使是轻微扰动时，也会遭受显著的性能下降。本文提出了一种新型且鲁棒的攻击方法，称为IGSA（**I**nverse **G**radient **S**ample-based **A**ttack），它能够生成在多种未知扰动下仍保持有效的对抗样本。IGSA采用迭代的两步框架：(i) 逆梯度采样，在对抗样本的邻域内搜索最具破坏性的方向；(ii) 扰动引导细化，通过沿已识别的破坏性扰动方向进行梯度下降来更新对抗样本。理论分析表明，IGSA通过增加对抗样本在数据分布中的似然性来提升鲁棒性。在白盒和黑盒攻击场景下的广泛实验表明，IGSA在针对各种未知扰动的鲁棒性方面显著优于最先进的攻击方法。此外，IGSA在攻击对抗训练的防御模型时表现出优越性能。代码可在 https://github.com/nimingck/IGSA 获取。

---

### Robust Deep Reinforcement Learning against Adversarial Behavior Manipulation

- **Venue**: ICLR 2026 Poster
- **Authors**: Shojiro Yamabe, Kazuto Fukuchi, Jun Sakuma
- **Keywords**: Renforcement Learning, Robustness, Adversarial Attack
- **OpenReview**: https://openreview.net/forum?id=AC6lDj5dzl
- **PDF**: https://openreview.net/pdf?id=AC6lDj5dzl

**Abstract**

This study investigates behavior-targeted attacks on reinforcement learning and their countermeasures. Behavior-targeted attacks aim to manipulate the victim's behavior as desired by the adversary through adversarial interventions in state observations. Existing behavior-targeted attacks have some limitations, such as requiring white-box access to the victim's policy. To address this, we propose a novel attack method using imitation learning from adversarial demonstrations, which works under limited access to the victim's policy and is environment-agnostic. In addition, our theoretical analysis proves that the policy's sensitivity to state changes impacts defense performance, particularly in the early stages of the trajectory. Based on this insight, we propose time-discounted regularization, which enhances robustness against attacks while maintaining task performance. To the best of our knowledge, this is the first defense strategy specifically designed for behavior-targeted attacks.

**Abstract (Chinese)**

本研究探讨了针对强化学习的针对行为攻击及其对策。针对行为攻击旨在通过对状态观测的对抗性干预来操纵受害者行为，以实现攻击者的预期。现有的针对行为攻击存在一些局限性，例如需要对受害者策略的白盒访问。为解决这一问题，我们提出了一种基于对抗性演示的模仿学习新型攻击方法，该方法在对受害者策略访问有限的情况下有效，且环境无关。此外，我们的理论分析证明，策略对状态变化的敏感性会影响防御性能，尤其是在轨迹的早期阶段。基于这一洞见，我们提出时间折扣正则化方法，该方法在保持任务性能的同时提升了对攻击的鲁棒性。据我们所知，这是首个专为针对行为攻击设计的防御策略。

---

### SeRI: Gradient-Free Sensitive Region Identification in Decision-Based Black-Box Attacks

- **Venue**: ICLR 2026 Poster
- **Authors**: Feiyang Wang, Xingquan Zuo, Hai Huang, Gang Chen, Hangwei Qian
- **Keywords**: Machine learning, AI safety, Decision-based adversarial attacks, Sensitive region
- **OpenReview**: https://openreview.net/forum?id=OQOmOIIX9F
- **PDF**: https://openreview.net/pdf?id=OQOmOIIX9F

**Abstract**

Deep neural networks (DNNs) are highly vulnerable to adversarial attacks, where small, carefully crafted perturbations are added to input images to cause misclassification. These perturbations are particularly effective when concentrated in sensitive regions of an image that strongly influence the model’s prediction. However, in decision-based black-box settings, where only the top-1 predicted label is observable and query budgets are strictly limited, identifying sensitive regions becomes extremely challenging. This issue is critical because without accurate region information, decision-based attacks cannot refine adversarial examples effectively, limiting both their efficiency and accuracy.
We propose Sensitive Region Identification, SeRI, the first decision-based method that assigns a continuous sensitivity score to each image pixel. It enables fine-grained region discovery and substantially improves the efficiency of adversarial attacks, all without access to gradients, confidence scores, or surrogate models.
SeRI progressively partitions the image into finer sub-regions and refines a continuous sensitivity score to capture their true importance. At each iteration, it generates two perturbation variants of the selected region by scaling its magnitude up or down, and compares their decision boundaries to derive an accurate, continuous characterization of pixel sensitivity.
SeRI further divides selected region into smaller sub-regions, recursively refining the search for sensitive areas. This recursive refinement process enables more precise sensitivity estimation through fine-grained analysis, distinguishing SeRI from prior binary or one-shot region selection approaches. Experiments on two benchmark datasets show that SeRI significantly enhances state-of-the-art decision-based attacks in both targeted and non-targeted attack scenarios. Additionally, SeRI generates precise heatmaps that identify sensitive image regions. The code is available at https://github.com/BUPTAIOC/SeRI.

**Abstract (Chinese)**

深度神经网络（DNNs）极易受到对抗攻击的影响，其中在输入图像中添加微小且精心设计的扰动即可导致误分类。这些扰动在图像的敏感区域集中时特别有效，这些区域对模型预测有强烈影响。然而，在基于决策的黑盒设置中，仅可观测到 top-1 预测标签且查询预算严格受限的情况下，识别敏感区域变得极为困难。这一问题至关重要，因为缺乏准确的区域信息，基于决策的攻击无法有效细化对抗样本，从而限制了其效率和准确性。

我们提出敏感区域识别方法 SeRI，这是首个基于决策的方法，为每个图像像素分配连续敏感度分数。它实现了细粒度区域发现，并显著提升了对抗攻击的效率，且无需访问梯度、置信度分数或代理模型。

SeRI 逐步将图像分区为更细的子区域，并细化连续敏感度分数以捕捉其真实重要性。在每次迭代中，它通过放大或缩小选定区域的扰动幅度生成两种扰动变体，并比较其决策边界，从而得出像素敏感度的准确连续表征。

SeRI 进一步将选定区域划分为更小的子区域，递归细化对敏感区域的搜索。这一递归细化过程通过细粒度分析实现了更精确的敏感度估计，从而将 SeRI 与以往的二元或一步式区域选择方法区分开来。在两个基准数据集上的实验表明，SeRI 在目标攻击和非目标攻击场景中显著提升了最先进的基于决策攻击性能。此外，SeRI 生成精确的热图以识别图像敏感区域。代码可在 https://github.com/BUPTAIOC/SeRI 获取。

---

### The Achilles’ Heel of LLMs: How Altering a Handful of Neurons Can Cripple Language Abilities

- **Venue**: ICLR 2026 Poster
- **Authors**: Zixuan Qin, Qingchen Yu, Kunlin Lyu, Zhaoxin Fan, Yifan Sun
- **Keywords**: Ultra-sparse neuron sets, Perturbation-based identification, Catastrophic failure
- **OpenReview**: https://openreview.net/forum?id=pJoSE7Cvj0
- **PDF**: https://openreview.net/pdf?id=pJoSE7Cvj0

**Abstract**

Large Language Models (LLMs) have become foundational tools in natural language processing, powering a wide range of applications and research. Many studies have shown that LLMs share significant similarities with the human brain. Neuroscience research has found that a small subset of biological neurons in the human brain are crucial for core cognitive functions, which raises a fundamental question: do LLMs also contain a small subset of critical neurons? In this paper, we investigate this question by proposing a Perturbation-based Causal Identification of Critical Neurons method to systematically locate such critical neurons in LLMs. Our findings reveal three key insights:
(1) LLMs contain ultra-sparse critical neuron sets. Disrupting these critical neurons can cause a 72B-parameter model with over 1.1 billion neurons to completely collapse, with perplexity increasing by up to 20 orders of magnitude;
(2) These critical neurons are not uniformly distributed, but tend to concentrate in the outer layers, particularly within the MLP down\_proj components;
(3) Performance degradation exhibits sharp phase transitions, rather than a gradual decline, when these critical neurons are disrupted.
Through comprehensive experiments across diverse model architectures and scales, we provide deeper analysis of these phenomena and their implications for LLM robustness and interpretability. These findings can offer guidance for developing more robust model architectures and improving deployment security in safety-critical applications. Our code is available at https://github.com/qqqqqqqzx/The-Achilles-Heel-of-LLMs.

**Abstract (Chinese)**

大型语言模型 (LLMs) 已成为自然语言处理中的基础工具，支持广泛的应用和研究。许多研究表明，LLMs 与人类大脑具有显著相似性。神经科学研究发现，人类大脑中一小部分生物神经元对核心认知功能至关重要，这引发了一个基本问题：LLMs 是否也包含一小部分关键神经元？在本文中，我们通过提出一种基于扰动的关键神经元因果识别方法来系统地定位 LLMs 中的此类关键神经元，来探讨这一问题。我们的发现揭示了三个关键洞见：

(1) LLMs 包含超稀疏的关键神经元集合。破坏这些关键神经元会导致一个拥有超过 11 亿神经元的 72B 参数模型完全崩溃，困惑度增加高达 20 个数量级；

(2) 这些关键神经元并非均匀分布，而是倾向于集中在外部层，特别是 MLP down\_proj 组件中；

(3) 当这些关键神经元被破坏时，性能退化表现出尖锐的相变，而不是渐进式下降。

通过在多样化的模型架构和规模上的全面实验，我们对这些现象及其对 LLM 鲁棒性和可解释性的影响进行了更深入的分析。这些发现可以为开发更鲁棒的模型架构以及提升安全关键应用中的部署安全性提供指导。我们的代码可在 https://github.com/qqqqqqqzx/The-Achilles-Heel-of-LLMs 获取。

---

### Time Is All It Takes: Spike-Retiming Attacks on Event-Driven Spiking Neural Networks

- **Venue**: ICLR 2026 Poster
- **Authors**: Yi Yu, Qixin Zhang, Shuhan Ye, Xun Lin, Qianshan Wei, Kun Wang, Wenhan Yang, Dacheng Tao, Xudong Jiang
- **Keywords**: spiking neural networks, event dataset, snn, attacks, adversarial attacks
- **OpenReview**: https://openreview.net/forum?id=b107VY19Id
- **PDF**: https://openreview.net/pdf?id=b107VY19Id

**Abstract**

Spiking neural networks (SNNs) compute with discrete spikes and exploit temporal structure, yet most adversarial attacks change intensities or event counts instead of timing. We study a timing-only adversary that retimes existing spikes while preserving spike counts and amplitudes in event-driven SNNs, thus remaining rate-preserving. We formalize a capacity-1 spike-retiming threat model with a unified trio of budgets: per-spike jitter $B_{\infty}$, total delay $B_{1}$, and tamper count $B_{0}$. 
Feasible adversarial examples must satisfy timeline consistency and non-overlap, which makes the search space discrete and constrained. To optimize such retimings at scale, we use projected-in-the-loop (PIL) optimization: shift-probability logits yield a differentiable soft retiming for backpropagation, and a strict projection in the forward pass produces a feasible discrete schedule that satisfies capacity-1, non-overlap, and the chosen budget at every step. The objective maximizes task loss on the projected input and adds a capacity regularizer together with budget-aware penalties, which stabilizes gradients and aligns optimization with evaluation. Across event-driven benchmarks (CIFAR10-DVS, DVS-Gesture, N-MNIST) and diverse SNN architectures, we evaluate under binary and integer event grids and a range of retiming budgets, and also test models trained with timing-aware adversarial training designed to counter timing-only attacks. For example, on DVS-Gesture the attack attains high success (over 90\%) while touching fewer than 2\% of spikes under ${B}_{0}$. Taken together, our results show that spike retiming is a practical and stealthy attack surface that current defenses struggle to counter, providing a clear reference for temporal robustness in event-driven SNNs. Code is available at https://github.com/yuyi-sd/Spike-Retiming-Attacks.

**Abstract (Chinese)**

脉冲神经网络（SNNs）使用离散脉冲进行计算并利用时序结构，然而大多数对抗攻击改变强度或事件计数而非时序。我们研究一种仅时序对抗攻击者，它在事件驱动SNNs中重新定时现有脉冲，同时保持脉冲计数和幅度，从而保持速率不变。我们形式化了一个容量为1的脉冲重新定时威胁模型，具有统一的三个预算：每个脉冲抖动\(B_{\infty}\)、总延迟\(B_{1}\)和篡改计数\(B_{0}\)。  
可行的对抗样本必须满足时间线一致性和非重叠，这使得搜索空间离散且受约束。为了大规模优化此类重新定时，我们使用投影在环（PIL）优化：移位概率logits产生可微分的软重新定时用于反向传播，前向传播中的严格投影产生满足容量为1、非重叠和所选预算的每步可行离散调度。目标函数最大化投影输入上的任务损失，并添加容量正则化器以及预算感知惩罚，这稳定了梯度并使优化与评估对齐。在事件驱动基准（CIFAR10-DVS、DVS-Gesture、N-MNIST）和多样SNN架构上，我们在二进制和整数事件网格下以及一系列重新定时预算下进行评估，并测试了设计用于对抗仅时序攻击的时序感知对抗训练模型。例如，在DVS-Gesture上，该攻击在\(B_{0}\)下触及不到2%的脉冲时实现高成功率（超过90%）。总之，我们的结果表明脉冲重新定是当前防御难以对抗的实用且隐蔽攻击面，为事件驱动SNNs中的时序鲁棒性提供了清晰参考。代码可在https://github.com/yuyi-sd/Spike-Retiming-Attacks获取。

---

### Time-To-Inconsistency: A Survival Analysis of Large Language Model Robustness to Adversarial Attacks

- **Venue**: ICLR 2026 Poster
- **Authors**: Yubo Li, Ramayya Krishnan, Rema Padman
- **Keywords**: Large Language Models, Survival Analysis, Consistency, Multi-turn Dialogue, Time-to-Event Modeling, LLM Robustness
- **OpenReview**: https://openreview.net/forum?id=88C7vSdn0t
- **PDF**: https://openreview.net/pdf?id=88C7vSdn0t

**Abstract**

Large Language Models (LLMs) have revolutionized conversational AI, yet their robustness in extended multi-turn dialogues remains poorly understood. Existing evaluation frameworks focus on static benchmarks and single-turn assessments, failing to capture the temporal dynamics of conversational degradation that characterize real-world interactions. In this work, we present a large-scale survival analysis of conversational robustness, modeling failure as a time-to-event process over 36,951 turns from 9 state-of-the-art LLMs on the MT-Consistency benchmark. Our framework combines Cox proportional hazards, Accelerated Failure Time (AFT), and Random Survival Forest models with simple semantic drift features. We find that abrupt prompt-to-prompt semantic drift sharply increases the hazard of inconsistency, whereas cumulative drift is counterintuitively \emph{protective}, suggesting adaptation in conversations that survive multiple shifts. AFT models with model–drift interactions achieve the best combination of discrimination and calibration, and proportional hazards checks reveal systematic violations for key drift covariates, explaining the limitations of Cox-style modeling in this setting. Finally, we show that a lightweight AFT model can be turned into a turn-level risk monitor that flags most failing conversations several turns before the first inconsistent answer while keeping false alerts modest. These results establish survival analysis as a powerful paradigm for evaluating multi-turn robustness and for designing practical safeguards for conversational AI systems.

**Abstract (Chinese)**

大语言模型（LLMs）已彻底革新了对话式 AI，但其在扩展多轮对话中的鲁棒性仍未得到充分理解。现有的评估框架聚焦于静态基准和单轮评估，无法捕捉真实世界交互中对话退化的时间动态特征。本工作中，我们提出了一种大规模对话鲁棒性生存分析，将失效建模为时间到事件过程，涵盖 MT-Consistency 基准上 9 个最先进 LLMs 的 36,951 轮对话。我们的框架结合了 Cox 比例风险模型、加速失效时间（AFT）模型和随机生存森林模型，以及简单的语义漂移特征。我们发现，突发的提示间语义漂移会急剧增加不一致性的风险，而累积漂移则反直观地具有\emph{保护性}，表明在多轮转变中存活的对话表现出适应性。包含模型–漂移交互的 AFT 模型实现了区分度和校准度的最佳组合，而比例风险检验揭示了关键漂移协变量的系统性违反，解释了 Cox 式建模在此场景下的局限性。最后，我们展示了如何将轻量级 AFT 模型转化为轮级风险监测器，该监测器可在首次不一致回答前几轮标记大多数失效对话，同时将误报保持在适度水平。这些结果确立了生存分析作为评估多轮鲁棒性和设计对话式 AI 系统实际保障措施的有力范式。

---

### Transferable and Stealthy Adversarial Attacks on Large Vision-Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhewen Yao, Yao Zhu, Shiliang Zhang
- **Keywords**: Adversarial Attacks, Robustness
- **OpenReview**: https://openreview.net/forum?id=liQueBuFXi
- **PDF**: https://openreview.net/pdf?id=liQueBuFXi

**Abstract**

Existing adversarial attacks on Large Vision-Language Models (LVLMs) often struggle with limited transferability to black-box models or produce perceptible artifacts that are easily detected. This paper presents Progressive Semantic Infusion (PSI), a diffusion-based attack that progressively aligns and infuses natural target semantics. To improve transferability, PSI leverages diffusion priors to better align adversarial examples with the natural image distribution and employs progressive alignment to mitigate overfitting on a single fixed surrogate objective. To enhance stealthiness, PSI embeds source-aware cues during denoising to preserve visual fidelity and avoid detectable artifacts. Experiments show that PSI effectively attacks open-source, adversarially trained, and commercial VLMs, including GPT-5 and Grok-4, surpassing existing methods in both transferability and stealthiness. Our findings highlight a critical vulnerability in modern vision-language systems and offer valuable insights towards building more robust and trustworthy multimodal models.

**Abstract (Chinese)**

现有的针对大型视觉-语言模型 (LVLMs) 的对抗攻击往往面临迁移到黑盒模型的有限性，或产生易于检测的可察觉伪影。本文提出渐进语义注入 (PSI)，一种基于扩散的攻击方法，该方法渐进地对齐并注入自然目标语义。为了提升迁移性，PSI 利用扩散先验更好地将对抗样本与自然图像分布对齐，并采用渐进对齐来缓解对单一固定代理目标的过拟合。为了增强隐蔽性，PSI 在去噪过程中嵌入源感知提示，以保留视觉保真度并避免可检测伪影。实验表明，PSI 有效攻击了开源、对抗训练的以及商业 VLMs，包括 GPT-5 和 Grok-4，在迁移性和隐蔽性方面均优于现有方法。我们的发现突显了现代视觉-语言系统中的关键漏洞，并为构建更鲁棒和可信的多模态模型提供了宝贵见解。

---

### TriQDef: Disrupting Semantic and Gradient Alignment to Prevent Adversarial Patch Transferability in Quantized Neural Networks

- **Venue**: ICLR 2026 Poster
- **Authors**: Amira Guesmi, Bassem ouni, Muhammad Shafique
- **Keywords**: Patch-based attacks, adversarial transferability, model quantization
- **OpenReview**: https://openreview.net/forum?id=acQP99PU8y
- **PDF**: https://openreview.net/pdf?id=acQP99PU8y

**Abstract**

Quantized Neural Networks (QNNs) are widely deployed in edge and resource-constrained environments for their efficiency in computation and memory. While quantization distorts gradient landscapes and weakens pixel-level attacks, it offers limited robustness against patch-based adversarial attacks—localized, high-saliency perturbations that remain highly transferable across bit-widths. Existing defenses either overfit to specific quantization settings or fail to address this cross-bit vulnerability.  
We propose \textbf{TriQDef}, a tri-level quantization-aware defense framework that disrupts the transferability of patch-based attacks across QNNs. TriQDef integrates: (1) a \emph{Feature Disalignment Penalty (FDP)} that enforces semantic inconsistency by penalizing perceptual similarity in intermediate features; (2) a \emph{Gradient Perceptual Dissonance Penalty (GPDP)} that misaligns input gradients across quantization levels using structural metrics such as Edge IoU and HOG Cosine; and (3) a \emph{Joint Quantization-Aware Training Protocol} that applies these penalties within a \emph{shared backbone} jointly optimized across multiple quantizers.  
Extensive experiments on CIFAR-10 and ImageNet show that TriQDef lowers Attack Success Rates (ASR) by over 40\% on unseen patch and quantization combinations while preserving high clean accuracy. These results highlight the importance of disrupting both semantic and perceptual gradient alignment to mitigate patch transferability in QNNs.

**Abstract (Chinese)**

量化神经网络（QNNs）因其在计算和内存方面的效率而在边缘和资源受限环境中得到广泛部署。虽然量化会扭曲梯度景观并削弱像素级攻击，但它对基于补丁的对抗攻击——局部、高显著性扰动，这些扰动在不同位宽间保持高度可转移性——提供的鲁棒性有限。现有的防御方法要么过拟合于特定量化设置，要么无法应对这种跨位漏洞。

我们提出\textbf{TriQDef}，一个三级量化感知防御框架，用于破坏基于补丁攻击在QNNs间的可转移性。TriQDef整合了：（1）\emph{特征不对齐惩罚（FDP）}，通过惩罚中间特征中的感知相似性来强制语义不一致；（2）\emph{梯度感知不协调惩罚（GPDP）}，使用边缘IoU和HOG余弦等结构指标，使输入梯度在不同量化水平间不对齐；以及（3）\emph{联合量化感知训练协议}，在\emph{共享主干}内应用这些惩罚，并跨多个量化器联合优化。

在CIFAR-10和ImageNet上的广泛实验表明，TriQDef在未见补丁和量化组合上将攻击成功率（ASR）降低了超过40\%，同时保持了高干净准确率。这些结果突显了破坏语义和感知梯度对齐以缓解QNNs中补丁可转移性的重要性。

---

### Tug-of-War No More: Harmonizing Accuracy and Robustness in Vision-Language Models via Stability-Aware Task Vector Merging

- **Venue**: ICLR 2026 Poster
- **Authors**: Junhao Dong, Xinghua Qu, Cong Zhang, Sua Qi Rong, Nguyen Duc Thai, Wenbo Pan, Xinfeng Li, Tongliang Liu, Piotr Koniusz, Yew-Soon Ong
- **Keywords**: Vision-Language Model, Task Vector, Trade-Off, Robustness
- **OpenReview**: https://openreview.net/forum?id=KOO1cDm2bt
- **PDF**: https://openreview.net/pdf?id=KOO1cDm2bt

**Abstract**

Foundation Vision-Language Models (VLMs) excel across benchmarks yet remain vulnerable to adversarial attacks. While adversarial fine-tuning improves robustness, attaining a desirable clean–robust performance trade-off typically requires costly hyperparameter searches with multiple retraining runs. A promising alternative is to merge task vectors (i.e., parameter displacements from pre-trained models) to balance accuracy and robustness without retraining. However, we find that naive task-vector merging produces a near-linear trade-off, as it equally weights all coordinates and fails to distinguish weights that aid both objectives from those that create conflicts. To overcome this limitation, we propose a prediction stability-aware merging framework that composes task vectors from off-the-shelf naturally and robustly fine-tuned VLMs. Our key insight is that prediction stability serves as a proxy for cross-objective compatibility, enabling us to favor perturbation-invariant parameters while attenuating those with high cross-objective impact. Specifically, we estimate per-parameter stability from gradients under both objectives, building complementary masks that retain jointly stable coordinates while suppressing counterpart-sensitive ones. We further refine these masks along adversarial parameter trajectories, with steps weighted by a prediction-sensitivity index.  Our theoretical analysis shows that the masks provably contract first-order cross-objective interference, and the prediction criticality index tracks curvature, biasing the merge toward flatter minima and better generalization. Extensive experiments across benchmarks and scenarios demonstrate our method consistently achieves superior clean–robust trade-offs over prior approaches, with the learned balance transferring effectively to downstream tasks.

**Abstract (Chinese)**

基础视觉-语言模型（VLMs）在多项基准测试中表现出色，但仍易受对抗攻击影响。虽然对抗微调能提升鲁棒性，但实现理想的干净-鲁棒性能权衡通常需要昂贵的超参数搜索和多次重训练。一种有前景的替代方案是通过合并任务向量（即从预训练模型的参数位移）来平衡准确性和鲁棒性，而无需重训练。然而，我们发现朴素的任务向量合并会产生近似线性的权衡，因为它等权重所有坐标，无法区分有助于双目标的权重与产生冲突的权重。为克服这一局限性，我们提出了一种预测稳定性感知的合并框架，该框架从现成的自然微调和鲁棒微调VLMs中组合任务向量。我们的关键洞见是，预测稳定性可作为跨目标兼容性的代理，从而使我们能够偏好扰动不变的参数，同时衰减具有高跨目标影响的参数。具体而言，我们从双目标下的梯度估计每个参数的稳定性，从而构建互补掩码：保留联合稳定的坐标，同时抑制对立敏感的坐标。我们进一步沿着对抗参数轨迹精炼这些掩码，其中步长由预测敏感性指数加权。我们的理论分析表明，这些掩码可证明收缩一阶跨目标干扰，且预测关键性指数跟踪曲率，将合并偏向更平坦的最小值并实现更好的泛化。在多项基准测试和场景下的广泛实验表明，我们的方法始终实现优于先前方法的干净-鲁棒权衡，且学习到的平衡能有效转移到下游任务。

---

### Understanding Sensitivity of Differential Attention through the Lens of Adversarial Robustness

- **Venue**: ICLR 2026 Poster
- **Authors**: Tsubasa Takahashi, Shojiro Yamabe, Futa Kai Waseda, Kento Sasaki
- **Keywords**: Adversarial Robustness, Differential Attention, Lipschitz Continuity, Adversarial Attack
- **OpenReview**: https://openreview.net/forum?id=kwy0cKmTm3
- **PDF**: https://openreview.net/pdf?id=kwy0cKmTm3

**Abstract**

Differential Attention (DA) has been proposed as a refinement to standard attention, suppressing redundant or noisy context through a subtractive structure and thereby reducing contextual hallucination. While this design sharpens task-relevant focus, we show that it also introduces a structural fragility under adversarial perturbations. Our theoretical analysis identifies negative gradient alignment—a configuration encouraged by DA’s subtraction—as the key driver of sensitivity amplification, leading to increased gradient norms and elevated local Lipschitz constants. We empirically validate this Fragile Principle through systematic experiments on ViT/DiffViT and evaluations of pretrained CLIP/DiffCLIP, spanning five datasets in total. These results demonstrate higher attack success rates, frequent gradient opposition, and stronger local sensitivity compared to standard attention. Furthermore, depth-dependent experiments reveal a robustness crossover: stacking DA layers attenuates small perturbations via depth-dependent noise cancellation, though this protection fades under larger attack budgets. Overall, our findings uncover a fundamental trade-off: DA improves discriminative focus on clean inputs but increases adversarial vulnerability, underscoring the need to jointly design for selectivity and robustness in future attention mechanisms.

**Abstract (Chinese)**

差分注意力（DA）被提出作为标准注意力的改进，通过减法结构抑制冗余或噪声上下文，从而减少上下文幻觉。虽然这种设计强化了任务相关焦点，但我们证明它也引入了对抗扰动下的结构脆弱性。我们的理论分析识别出负梯度对齐——一种由 DA 的减法鼓励的配置——作为敏感性放大的关键驱动因素，导致梯度范数增加和局部 Lipschitz 常数升高。我们通过对 ViT/DiffViT 的系统实验以及对预训练 CLIP/DiffCLIP 的评估，在总共五个数据集上经验验证了这一脆弱原理。这些结果显示出比标准注意力更高的攻击成功率、更频繁的梯度对立以及更强的局部敏感性。此外，深度相关实验揭示了鲁棒性交叉：堆叠 DA 层通过深度相关的噪声抵消衰减小扰动，尽管这种保护在更大的攻击预算下会消退。总体而言，我们的发现揭示了一个基本权衡：DA 在干净输入上改善判别焦点，但增加了对抗脆弱性，这强调了未来注意力机制需要联合设计选择性和鲁棒性。

---

### Understanding and Improving Continuous LLM Adversarial Training via In-context Learning Theory

- **Venue**: ICLR 2026 Poster
- **Authors**: Shaopeng Fu, Di Wang
- **Keywords**: LLM adversarial training, Jailbreak attacks, In-context learning
- **OpenReview**: https://openreview.net/forum?id=7zztxcmlyZ
- **PDF**: https://openreview.net/pdf?id=7zztxcmlyZ

**Abstract**

Adversarial training (AT) is an effective defense for large language models (LLMs) against jailbreak attacks, but performing AT on LLMs is costly. To improve the efficiency of AT for LLMs, recent studies propose continuous AT (CAT) that searches for adversarial inputs within the continuous embedding space of LLMs during AT. While CAT has achieved empirical success, its underlying mechanism, i.e., why adversarial perturbations in the embedding space can help LLMs defend against jailbreak prompts synthesized in the input token space, remains unknown. This paper presents the first theoretical analysis of CAT on LLMs based on in-context learning (ICL) theory. For linear transformers trained with adversarial examples from the embedding space on in-context linear regression tasks, we prove a robust generalization bound that has a negative correlation with the perturbation radius in the embedding space. This clearly explains why CAT can defend against jailbreak prompts from the LLM's token space. Further, the robust bound shows that the robustness of an adversarially trained LLM is closely related to the singular values of its embedding matrix. Based on this, we propose to improve LLM CAT by introducing an additional regularization term, which depends on singular values of the LLM's embedding matrix, into the objective function of CAT. Experiments on real-world LLMs demonstrate that our method can help LLMs achieve better jailbreak robustness-utility tradeoff.

**Abstract (Chinese)**

对抗训练 (AT) 是大型语言模型 (LLMs) 对抗越狱攻击的有效防御方法，但对 LLMs 执行 AT 成本高昂。为了提高 LLMs 的 AT 效率，最近的研究提出了连续对抗训练 (CAT)，该方法在 AT 过程中在 LLMs 的连续嵌入空间中搜索对抗输入。虽然 CAT 已取得经验成功，但其底层机制，即嵌入空间中的对抗扰动为何能帮助 LLMs 防御输入令牌空间中合成的越狱提示，仍未知。本文基于上下文学习 (ICL) 理论，首次对 LLMs 上的 CAT 进行了理论分析。对于在上下文线性回归任务上使用嵌入空间对抗示例训练的线性变换器，我们证明了一个鲁棒泛化界，该界与嵌入空间中的扰动半径呈负相关。这清楚地解释了 CAT 为什么能防御来自 LLM 令牌空间的越狱提示。此外，该鲁棒界表明，对抗训练 LLM 的鲁棒性与其嵌入矩阵的奇异值密切相关。基于此，我们提出通过在 CAT 的目标函数中引入一个额外的正则化项来改进 LLM CAT，该正则化项依赖于 LLM 嵌入矩阵的奇异值。在真实世界 LLMs 上的实验表明，我们的方法可以帮助 LLMs 实现更好的越狱鲁棒性-效用权衡。

---

### VEAttack: Downstream-agnostic Vision Encoder Attack against Large Vision Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Hefei Mei, Zirui Wang, Shen You, Minjing Dong, Chang Xu
- **Keywords**: adversarial attack, vision-encoder-only, large vision language models, downstream-agnostic
- **OpenReview**: https://openreview.net/forum?id=KboFptAM8S
- **PDF**: https://openreview.net/pdf?id=KboFptAM8S

**Abstract**

Large Vision-Language Models (LVLMs) have demonstrated capabilities in multimodal understanding, yet their vulnerability to adversarial attacks raises significant concerns. To achieve practical attacking, this paper aims at efficient and transferable untargeted attacks under limited perturbation sizes. Considering this objective, white‑box attacks require full‑model gradients and task‑specific labels, making costs scale with tasks, while black‑box attacks rely on proxy models, typically requiring large perturbation sizes and elaborate transfer strategies. Given the centrality and widespread reuse of the vision encoder in LVLMs, we adopt a gray‑box setting that targets the vision encoder alone for efficient but effective attacking. We theoretically establish the feasibility of vision‑encoder‑only attacks, laying the foundation for our gray‑box setting. Based on this analysis, we propose perturbing patch tokens rather than the class token, informed by both theoretical and empirical insights. We generate adversarial examples by minimizing the cosine similarity between clean and perturbed visual features, without accessing the subsequent models, tasks, or labels. This significantly reduces computational overhead while eliminating the task and label dependence. VEAttack has achieved a performance degradation of 94.5% on image caption task and 75.7% on visual question answering task. We also reveal some key observations to provide insights into LVLM attack/defense: 1) hidden layer variations of LLM, 2) token attention differential, 3) Möbius band in transfer attack, 4) low sensitivity to attack steps.

**Abstract (Chinese)**

大视觉-语言模型（LVLMs）在多模态理解方面展现了强大能力，然而其对抗攻击的脆弱性引发了重大担忧。为实现实际攻击，本文旨在在有限扰动大小下实现高效且可转移的无目标攻击。鉴于此目标，白盒攻击需要全模型梯度和任务特定标签，导致成本随任务扩展，而黑盒攻击依赖代理模型，通常需要较大的扰动大小和复杂的转移策略。鉴于LVLMs中视觉编码器的核心性和广泛重用，我们采用仅针对视觉编码器的灰盒设置，以实现高效但有效的攻击。我们从理论上确立了仅视觉编码器攻击的可行性，为我们的灰盒设置奠定了基础。基于此分析，我们提出扰动图像块令牌而非类别令牌，这一方法受理论和实证洞见启发。我们通过最小化干净视觉特征与扰动视觉特征之间的余弦相似度来生成对抗样本，而无需访问后续模型、任务或标签。这显著降低了计算开销，同时消除了对任务和标签的依赖。VEAttack在图像描述任务上实现了94.5%的性能下降，在视觉问答任务上实现了75.7%的性能下降。我们还揭示了一些关键观察结果，以为LVLM攻击/防御提供洞见：1) LLM的隐藏层变异，2) 令牌注意力差异，3) 转移攻击中的莫比乌斯带，4) 对攻击步数的低敏感性。

---

### Why Adversarially Train Diffusion Models?

- **Venue**: ICLR 2026 Poster
- **Authors**: Maria Rosaria Briglia, Mujtaba Hussain Mirza, Giuseppe Lisanti, Iacopo Masi
- **Keywords**: Robustness, Adversarial training
- **OpenReview**: https://openreview.net/forum?id=lL6htAaolp
- **PDF**: https://openreview.net/pdf?id=lL6htAaolp

**Abstract**

Adversarial Training (AT) is a known, powerful, well-established technique for improving classifier robustness to input perturbations, yet its applicability beyond discriminative settings remains limited. Motivated by the widespread use of score-based generative models and their need to operate robustly under substantial noisy or corrupted input data, we propose an adaptation of AT for these models, providing a thorough empirical assessment.
We introduce a principled formulation of AT for Diffusion Models (DMs) that replaces the conventional *invariance* objective with an *equivariance* constraint aligned to the denoising dynamics of score matching. Our method integrates seamlessly into diffusion training by adding either random perturbations--similar to randomized smoothing--or adversarial ones--akin to AT.
Our approach offers several advantages: **(a)** tolerance to heavy noise and corruption, **(b)** reduced memorization, **(c)** robustness to outliers and extreme data variability and **(d)** resilience to iterative adversarial attacks.
We validate these claims on proof-of-concept low- and high-dimensional datasets with *known* ground-truth distributions, enabling precise error analysis. We further evaluate on standard benchmarks (CIFAR-10, CelebA, and LSUN Bedroom), where our approach shows improved robustness and preserved sample fidelity under severe noise, data corruption, and adversarial evaluation. Code available at [github.com/OmnAI-Lab/Adversarial-Training-DM](https://github.com/OmnAI-Lab/Adversarial-Training-DM)

**Abstract (Chinese)**

对抗训练 (AT) 是一种已知、强大且成熟的技术，用于提升分类器对输入扰动的鲁棒性，然而其在判别式设置之外的应用仍受限。受基于分数的生成模型的广泛应用及其在大量噪声或损坏输入数据下鲁棒运行的需求所驱动，我们提出了一种针对这些模型的 AT 适应方法，并提供了全面的实证评估。

我们引入了一种针对扩散模型 (DMs) 的原则性对抗训练公式，将传统的*不变性*目标替换为与分数匹配去噪动力学对齐的*等变性*约束。我们的方法通过添加随机扰动——类似于随机平滑——或对抗扰动——类似于 AT——无缝集成到扩散训练中。

我们的方法提供了多项优势：**(a)** 对重度噪声和损坏的容忍度，**(b)** 减少记忆化，**(c)** 对异常值和极端数据变异的鲁棒性，以及 **(d)** 对迭代对抗攻击的弹性。

我们在具有*已知*真实分布的低维和高维概念验证数据集上验证了这些主张，从而实现了精确的误差分析。我们进一步在标准基准 (CIFAR-10、CelebA 和 LSUN Bedroom) 上进行评估，在这些基准上，我们的方法在严重噪声、数据损坏和对抗评估下展示了改进的鲁棒性和保留的样本保真度。代码可在 [github.com/OmnAI-Lab/Adversarial-Training-DM](https://github.com/OmnAI-Lab/Adversarial-Training-DM) 获取。

---

### Zero-Sacrifice Persistent-Robustness Adversarial Defense for Pre-Trained Encoders

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhuxin Lei, Ziyuan Yang, Yi Zhang
- **Keywords**: adversarial robustness, self-supervised learning, pretrained models, security vulnerability
- **OpenReview**: https://openreview.net/forum?id=AYFUmgCpkB
- **PDF**: https://openreview.net/pdf?id=AYFUmgCpkB

**Abstract**

The widespread use of publicly available pre-trained encoders from self-supervised learning (SSL) has exposed a critical vulnerability: their susceptibility to downstream-agnostic adversarial examples (DAEs), which are crafted without knowledge of the downstream tasks but capable of misleading downstream models. While several defense methods have been explored recently, they rely primarily on task-specific adversarial fine-tuning, which inevitably limits generalizability and causes catastrophic forgetting and deteriorates benign performance. Different with previous works, we propose a more rigorous defense goal that requires only a single tuning for diverse downstream tasks to defend against DAEs and preserve benign performance. To achieve this defense goal, we introduce **Ze**ro-Sacrifice **P**ersistent-Robustness **A**dversarial **D**efense (**ZePAD**), which is inspired by the inherent sensitivity of neural networks to data characteristics. Specifically, ZePAD is a dual-branch structure, which consists of a Multi-Pattern Adversarial Enhancement Branch (MPAE-Branch) that uses two adversarially fine-tuned encoders to strengthen adversarial resistance. The Benign Memory Preservation Branch (BMP-Branch) is trained on local data to ensure adversarial robustness does not compromise benign performance. Surprisingly, we find that ZePAD can directly detect DAEs by evaluating branch confidence, without introducing any adversarial exsample identification task during training. Notably, by enriching feature diversity, our method enables a single adversarial fine-tuning to defend against DAEs across downstream tasks, thereby achieving persistent robustness. Extensive experiments on 11 SSL methods and 6 datasets validate its effectiveness. In certain cases, it achieves a 29.20\% improvement in benign performance and a 73.86\% gain in adversarial robustness, highlighting its zero-sacrifice property.

**Abstract (Chinese)**

公开可用的自监督学习 (SSL) 预训练编码器的广泛使用暴露了一个关键漏洞：它们易受下游任务无关对抗样本 (DAEs) 的影响，这些样本在不知道下游任务的情况下制作，但能够误导下游模型。虽然最近探索了几种防御方法，但它们主要依赖任务特定的对抗微调，这不可避免地限制了泛化能力，并导致灾难性遗忘和良性性能下降。与先前工作不同，我们提出一个更严格的防御目标，该目标仅需一次调优即可针对多种下游任务防御 DAEs 并保持良性性能。为实现这一防御目标，我们引入**零牺牲持久鲁棒性对抗防御** (**ZePAD**)，其受神经网络对数据特征固有敏感性的启发。具体而言，ZePAD 是一种双分支结构，包括使用两个对抗微调编码器来增强对抗抵抗的多模式对抗增强分支 (MPAE-Branch)。良性记忆保持分支 (BMP-Branch) 在本地数据上训练，以确保对抗鲁棒性不损害良性性能。令人惊讶的是，我们发现 ZePAD 可以通过评估分支置信度直接检测 DAEs，而无需在训练期间引入任何对抗样本识别任务。值得注意的是，通过丰富特征多样性，我们的方法实现了一次对抗微调即可针对下游任务防御 DAEs，从而实现持久鲁棒性。在 11 种 SSL 方法和 6 个数据集上的广泛实验验证了其有效性。在某些情况下，它实现了良性性能 29.20% 的提升和对抗鲁棒性 73.86% 的增益，突显了其零牺牲特性。

---
