# watermarking_fingerprinting

**Description**: 生成内容水印/指纹与模型溯源。包括 text/image watermarking、fingerprinting、membership/provenance attribution、去水印攻击与鲁棒水印、来源追踪与取证等。

**Paper count**: 27

---

### Every Language Model Has a Forgery-Resistant Signature

- **Venue**: ICLR 2026 Oral
- **Authors**: Matthew Finlayson, Xiang Ren, Swabha Swayamdipta
- **Keywords**: fingerprint, watermark, language model, signature, accountability, cryptography, forgery, security
- **OpenReview**: https://openreview.net/forum?id=vLFqOoMBol
- **PDF**: https://openreview.net/pdf?id=vLFqOoMBol

**Abstract**

The ubiquity of closed-weight language models with public-facing APIs has generated interest in forensic methods, both for extracting hidden model details (e.g., parameters) and identifying models by their outputs. One successful approach to these goals has been to exploit the geometric constraints imposed by the language model architecture and parameters. In this work, we show that a lesser-known geometric constraint—namely that language model outputs lie on the surface of a high-dimensional ellipse—functions as a signature for the model, which be used to identify which model an output came from. This ellipse signature has unique properties that distinguish it from existing model-output association methods like language model watermarks. In particular, the signature is hard to forge: without direct access to model parameters, it is practically infeasible to produce logprobs on the ellipse. Secondly, the signature is naturally occurring, since all language models have these elliptical constraints. Thirdly, the signature is self-contained, in that it is detectable without access to the model input or full weights. Finally, the signature is exceptionally redundant, as it is independently detectable in every single logprob output from the model. We evaluate a novel technique for extracting the ellipse on small models, and discuss the practical hurdles that make it infeasible for production-size models, making the signature hard to forge. Finally, we use ellipse signatures to propose a protocol for language model output verification, which is analogous to cryptographic symmetric-key message authentication systems.

**Abstract (Chinese)**

具有面向公众API的闭权语言模型的普遍性引发了对取证方法的兴趣，这些方法既用于提取隐藏的模型细节（如参数），也用于通过输出识别模型。其中一种成功实现这些目标的方法是利用语言模型架构和参数强加的几何约束。在本工作中，我们展示了 一个鲜为人知的几何约束——即语言模型输出位于高维椭圆表面上——可作为模型的签名，用于识别输出来自哪个模型。这种椭圆签名具有独特属性，将其与现有模型输出关联方法（如语言模型水印）区分开来。特别是，该签名难以伪造：没有直接访问模型参数的情况下，实际不可能产生位于椭圆上的对数概率。其次，该签名自然存在，因为所有语言模型都具有这些椭圆约束。第三，该签名是自包含的，即无需访问模型输入或完整权重即可检测。最后，该签名极具冗余性，因为它可在模型的每个单个对数概率输出中独立检测。我们在小型模型上评估了一种提取椭圆的新技术，并讨论了使其在生产规模模型上不可行的实际障碍，从而使签名难以伪造。最后，我们使用椭圆签名提出了一种语言模型输出验证协议，该协议类似于密码学对称密钥消息认证系统。

---

### LLM Fingerprinting via Semantically Conditioned Watermarks

- **Venue**: ICLR 2026 Oral
- **Authors**: Thibaud Gloaguen, Robin Staab, Nikola Jovanović, Martin Vechev
- **Keywords**: LLM, Watermarks, Fingerprinting
- **OpenReview**: https://openreview.net/forum?id=t38nZqqi3Z
- **PDF**: https://openreview.net/pdf?id=t38nZqqi3Z

**Abstract**

Most LLM fingerprinting methods teach the model to respond to a few fixed queries with predefined atypical responses (keys). This memorization often does not survive common deployment steps such as finetuning or quantization, and such keys can be easily detected and filtered from LLM responses, ultimately breaking the fingerprint. To overcome these limitations we introduce *LLM fingerprinting via semantically conditioned watermarks*, replacing fixed query sets with a broad semantic domain, and replacing brittle atypical keys with a statistical watermarking signal diffused throughout each response. After teaching the model to watermark its responses only to prompts from a predetermined domain e.g., French language, the model owner can use queries from that domain to reliably detect the fingerprint and verify ownership. As we confirm in our thorough experimental evaluation, our fingerprint is both stealthy and robust to all common deployment scenarios.

**Abstract (Chinese)**

大多数大型语言模型（LLM）指纹识别方法通过训练模型对少数固定查询给出预定义的非典型响应（密钥）来实现。这种记忆往往无法经受常见的部署步骤，如微调或量化，而且此类密钥可以轻易从LLM响应中检测并过滤，从而破坏指纹。为了克服这些局限性，我们引入了*通过语义条件水印的LLM指纹识别*，用广阔的语义域替换固定查询集，并用扩散到每个响应中的统计水印信号替换脆弱的非典型密钥。在训练模型仅对来自预定域（如法语）的提示进行水印响应后，模型所有者可以使用该域的查询可靠地检测指纹并验证所有权。正如我们在详尽的实验评估中所确认，我们的指纹既隐秘又对所有常见部署场景具有鲁棒性。

---

### Spherical Watermark: Encryption-Free, Lossless Watermarking for Diffusion Models

- **Venue**: ICLR 2026 Oral
- **Authors**: Xiaoxiao Hu, Jiaqi Jin, Sheng Li, Wanli Peng, Xinpeng Zhang, Zhenxing Qian
- **Keywords**: AIGC Watermarking; Diffusion Models;
- **OpenReview**: https://openreview.net/forum?id=2eAGrunxVz
- **PDF**: https://openreview.net/pdf?id=2eAGrunxVz

**Abstract**

Diffusion models have revolutionized image synthesis but raise concerns around content provenance and authenticity. Digital watermarking offers a means of tracing generated media, yet traditional schemes often introduce distributional shifts and degrade visual quality. Recent lossless methods embed watermark bits directly into the latent Gaussian prior without modifying model weights, but still require per-image key storage or heavy cryptographic overhead. In this paper, we introduce Spherical Watermark, an encryption‐free and lossless watermarking framework that integrates seamlessly with diffusion architectures. First, our binary embedding module mixes repeated watermark bits with random padding to form a high-entropy code. Second, the spherical mapping module projects this code onto the unit sphere, applies an orthogonal rotation, and scales by a chi-square-distributed radius to recover exact multivariate Gaussian noise. We theoretically prove that the watermarked noise distribution preserves the target prior up to third-order moments, and empirically demonstrate that it is statistically indistinguishable from a standard multivariate normal distribution. Adopting Stable Diffusion, extensive experiments confirm that Spherical Watermark consistently preserves high visual fidelity while simultaneously improving traceability, computational efficiency, and robustness under attacks, thereby outperforming both lossy and lossless approaches.

**Abstract (Chinese)**

扩散模型革新了图像合成，但引发了关于内容来源和真实性的担忧。数字水印提供了一种追踪生成媒体的方法，然而传统方案往往引入分布偏移并降低视觉质量。最近的无损方法直接将水印比特嵌入潜在高斯先验中，而不修改模型权重，但仍需每图像密钥存储或沉重的加密开销。在本文中，我们引入了球面水印（Spherical Watermark），这是一个无加密且无损的水印框架，与扩散架构无缝集成。首先，我们的二进制嵌入模块将重复的水印比特与随机填充混合，形成高熵码。其次，球面映射模块将此码投影到单位球面上，施加正交旋转，并通过服从卡方分布的半径进行缩放，以恢复精确的多变量高斯噪声。我们从理论上证明，水印噪声分布在三阶矩上保持目标先验，并从实证上证明其与标准多变量正态分布统计上不可区分。采用Stable Diffusion，大量实验证实球面水印始终保持高视觉保真度，同时提升可追溯性、计算效率和抗攻击鲁棒性，从而优于有损和无损方法。

---

### AWM: Accurate Weight-Matrix Fingerprint for Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Boyi Zeng, Lin Chen, Ziwei He, Xinbing Wang, Zhouhan Lin
- **Keywords**: fingerprint, large language models, intellectual property
- **OpenReview**: https://openreview.net/forum?id=fDC5WeLeqh
- **PDF**: https://openreview.net/pdf?id=fDC5WeLeqh

**Abstract**

Protecting the intellectual property of large language models (LLMs) is crucial, given the substantial resources required for their training. Consequently, there is an urgent need for both model owners and third parties to determine whether a suspect LLM is trained from scratch or derived from an existing base model. However, the intensive post-training processes that models typically undergo—such as supervised fine-tuning, extensive continued pretraining, reinforcement learning, multi-modal extension, pruning, and upcycling—pose significant challenges to reliable identification. In this work, we propose a training-free fingerprinting method based on weight matrices. We leverage the Linear Assignment Problem (LAP) and an unbiased Centered Kernel Alignment (CKA) similarity to neutralize the effects of parameter manipulations, yielding a highly robust and high-fidelity similarity metric. On a comprehensive testbed of 60 positive and 90 negative model pairs, our method demonstrates exceptional robustness against all six aforementioned post-training categories while exhibiting a near-zero risk of false positives. By achieving perfect scores on all classification metrics, our approach establishes a strong basis for reliable model lineage verification. Moreover, the entire computation completes within 30s on an NVIDIA 3090 GPU.

**Abstract (Chinese)**

保护大型语言模型 (LLMs) 的知识产权至关重要，因为其训练需要大量资源。因此，模型所有者和第三方迫切需要确定可疑 LLM 是从头训练的，还是衍生自现有基础模型。然而，模型通常经历的密集后训练过程——如监督微调、大规模持续预训练、强化学习、多模态扩展、剪枝和升级——对可靠识别构成了重大挑战。在本工作中，我们提出了一种基于权重矩阵的无需训练的指纹方法。我们利用线性分配问题 (LAP) 和无偏中心化核对齐 (CKA) 相似度来抵消参数操作的影响，从而产生一种高度鲁棒且高保真度的相似度度量。在包含 60 个正样本和 90 个负样本模型对的全面测试平台上，我们的方法对上述六类后训练过程表现出卓越鲁棒性，同时假阳性风险接近零。通过在所有分类指标上取得完美分数，我们的方法为可靠的模型谱系验证奠定了坚实基础。此外，整个计算在 NVIDIA 3090 GPU 上可在 30 秒内完成。

---

### All That Glitters Is Not Gold: Key-Secured 3D Secrets within 3D Gaussian Splatting

- **Venue**: ICLR 2026 Poster
- **Authors**: Yan Ren, Shilin Lu, Adams Wai-Kin Kong
- **Keywords**: Gaussian Splatting, 3D Steganography
- **OpenReview**: https://openreview.net/forum?id=CcxIDaTfLB
- **PDF**: https://openreview.net/pdf?id=CcxIDaTfLB

**Abstract**

Recent advances in 3D Gaussian Splatting (3DGS) have revolutionized scene reconstruction, opening new possibilities for 3D steganography by hiding 3D secrets within 3D covers. The key challenge in steganography is ensuring imperceptibility while maintaining high-fidelity reconstruction. However, existing methods often suffer from detectability risks and utilize only suboptimal 3DGS attributes, limiting their full potential. We propose a novel end-to-end key-secured 3D steganography framework (KeySS) that jointly optimizes a 3DGS model and a key-secured decoder for secret reconstruction. Our approach reveals that Gaussian attributes contribute unequally to secret hiding. The framework incorporates a key-controllable mechanism enabling multi-secret hiding and unauthorized access prevention, while systematically exploring optimal attribute update to balance fidelity and security. To rigorously evaluate steganographic imperceptibility beyond conventional 2D metrics, we introduce 3D-Sinkhorn distance analysis, which quantifies distributional differences between original and steganographic Gaussian parameters in the representation space. Extensive experiments show that our method achieves state-of-the-art performance in 3D reconstruction while ensuring high levels of steganographic security. The framework is highly efficient and readily extensible to multi-GPU training. Our code will be publicly available.

**Abstract (Chinese)**

最近在3D高斯溅射（3DGS）方面的进展彻底改变了场景重建，为三维隐写术开辟了新可能性，通过在三维载密体中隐藏三维秘密。隐写术的关键挑战是在保持高保真重建的同时确保不可感知性。然而，现有的方法往往存在可检测性风险，并且仅利用次优的3DGS属性，限制了其全部潜力。我们提出了一种新型端到端密钥安全的3D隐写术框架（KeySS），它联合优化3DGS模型和密钥安全的解码器，用于秘密重建。我们的方法揭示了高斯属性对秘密隐藏的贡献不均等。该框架集成了密钥可控机制，支持多秘密隐藏和防止未授权访问，同时系统地探索最优属性更新以平衡保真度和安全性。为了严格评估超出传统2D度量的隐写不可感知性，我们引入了3D-Sinkhorn距离分析，它量化了原始和隐写高斯参数在表示空间中的分布差异。大量实验表明，我们的方法在3D重建中达到了最先进的性能，同时确保了高水平的隐写安全性。该框架高效且易于扩展到多GPU训练。我们的代码将公开可用。

---

### Attack-Resistant Watermarking for AIGC Image Forensics via Diffusion-based Semantic Deflection

- **Venue**: ICLR 2026 Poster
- **Authors**: Qingyu Liu, Yitao Zhang, Zhongjie Ba, Chao Shuai, Peng Cheng, Tianhang Zheng, Zhibo Wang
- **Keywords**: AIGC copyright protection; Image watermark; Diffusion model
- **OpenReview**: https://openreview.net/forum?id=wyucYNGPiW
- **PDF**: https://openreview.net/pdf?id=wyucYNGPiW

**Abstract**

Protecting the copyright of user-generated AI images is an emerging challenge as AIGC becomes pervasive in creative workflows. Existing watermarking methods (1) remain vulnerable to real-world adversarial threats, often forced to trade off between defenses against spoofing and removal attacks; and (2) cannot support semantic-level tamper localization. We introduce PAI, a training-free inherent watermarking framework for AIGC copyright protection, plug-and-play with diffusion-based AIGC services. PAI simultaneously provides three key functionalities: robust ownership verification, attack detection, and semantic-level tampering localization. Unlike existing inherent watermark methods that only embed watermarks at noise initialization of diffusion models, we design a novel key-conditioned deflection mechanism that subtly steers the denoising trajectory according to the user key. Such trajectory-level coupling further strengthens the semantic entanglement of identity and content, thereby further enhancing robustness against real-world threats. Moreover, we also provide a theoretical analysis proving that only the valid key can pass verification. Experiments across 12 attack methods show that PAI achieves 98.43\% verification accuracy, improving over SOTA methods by 37.25\% on average, and retains strong tampering localization performance even against advanced AIGC edits. Our code is available at \url{https://github.com/QingyuLiu/PAI}.

**Abstract (Chinese)**

随着AIGC在创意工作流程中变得普遍，用户生成AI图像的版权保护已成为一个新兴挑战。现有的水印方法（1）仍易受现实世界对抗威胁影响，往往被迫在针对欺骗和移除攻击的防御之间进行权衡；（2）无法支持语义级篡改定位。我们引入PAI，一种无需训练的固有水印框架，用于AIGC版权保护，可与基于扩散的AIGC服务即插即用。PAI同时提供三个关键功能：鲁棒的所有权验证、攻击检测以及语义级篡改定位。与仅在扩散模型噪声初始化时嵌入水印的现有固有水印方法不同，我们设计了一种新颖的基于密钥的偏转机制，根据用户密钥微妙地引导去噪轨迹。这种轨迹级耦合进一步加强了身份与内容的语义纠缠，从而进一步提升了对现实世界威胁的鲁棒性。此外，我们还提供了理论分析，证明只有有效密钥才能通过验证。在12种攻击方法上的实验表明，PAI实现了98.43\%的验证准确率，平均比SOTA方法提高了37.25\%，即使面对高级AIGC编辑，也保持了强大的篡改定位性能。我们的代码可在\url{https://github.com/QingyuLiu/PAI}获取。

---

### Auditing Black-Box LLM APIs with a Rank-Based Uniformity Test

- **Venue**: ICLR 2026 Poster
- **Authors**: Xiaoyuan Zhu, Yaowen Ye, Tianyi Alex Qiu, Hanlin Zhu, Sijun Tan, Ajraf Mannan, Jonathan Michala, Raluca Ada Popa, Willie Neiswanger
- **Keywords**: LLM, API auditing, untargeted fingerprinting
- **OpenReview**: https://openreview.net/forum?id=PSIe9mmF7a
- **PDF**: https://openreview.net/pdf?id=PSIe9mmF7a

**Abstract**

As API access becomes a primary interface to large language models (LLMs), users often interact with black-box systems that offer little transparency into the deployed model. To reduce costs or maliciously alter model behaviors, API providers may discreetly serve quantized or fine-tuned variants, which can degrade performance and compromise safety. Detecting such substitutions is difficult, as users lack access to model weights and, in most cases, even output logits. To tackle this problem, we propose a rank-based uniformity test (RUT) that can verify the behavioral equality of a black-box LLM to a locally deployed authentic model. Our method is accurate, query-efficient, and avoids detectable query patterns, making it robust to adversarial providers that reroute or mix responses upon the detection of testing attempts. We evaluate the approach across diverse query domains and threat scenarios, including quantization, harmful fine-tuning, jailbreak prompts, full model substitution, showing that it consistently achieves superior detection power over prior methods under constrained query budgets.

**Abstract (Chinese)**

随着API访问成为大型语言模型（LLMs）的主要接口，用户经常与提供部署模型很少透明度的黑盒系统交互。为了降低成本或恶意改变模型行为，API提供商可能悄然提供量化或微调变体，这可能会降低性能并损害安全性。检测此类替换很困难，因为用户无法访问模型权重，并且在大多数情况下甚至无法访问输出logits。为解决这一问题，我们提出了一种基于排名的均匀性测试（RUT），它可以验证黑盒LLM与本地部署的真实模型的行为等价性。我们的方法准确、查询高效，并避免可检测的查询模式，使其对检测到测试尝试后重新路由或混合响应的对抗性提供商具有鲁棒性。我们在多样化的查询领域和威胁场景中评估了该方法，包括量化、有害微调、越狱提示、完整模型替换，结果显示在受限查询预算下，它始终比先前方法具有更优的检测能力。

---

### CodeGenGuard: A Watermark for Code Generation Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Borui Yang, Mingxuan Ma, Liyao Xiang, Nan Chen, Xin Zhang, Linghe Kong, Xinghao Jiang
- **Keywords**: Watermarking, Code Generation, Copyright Protection
- **OpenReview**: https://openreview.net/forum?id=UQZ0Y0dbP9
- **PDF**: https://openreview.net/pdf?id=UQZ0Y0dbP9

**Abstract**

Code language models (LMs) represent valuable intellectual property (IP) as their training involves immense investments, including large-scale code corpora, proprietary annotations, extensive computational resources, and specialized designs. Hence the threat of model IP infringements such as unauthorized redistribution or model theft has become increasingly concerning. While neural network watermarking has been widely studied as a measure to support model ownership verification, watermarking code LMs is particularly challenging due to the seemingly conflicting requirements of code generation: adhering to strict syntactic rules and semantic consistency while allowing flexible changes to embed watermarks, keeping high fidelity of the generated content while being robust to extraction attacks, etc. To resolve the issues, we propose CodeGenGuard, a watermarking framework for code LMs. CodeGenGuard leverages semantic-preserving transformations (SPTs) to encode the watermark and incorporates a dead-code-based data augmentation pipeline to diversify SPT patterns. To improve robustness, we incorporate an efficient dual-LoRA shadow training scheme and an optimizable trigger prompt that learns to extract watermark from both the watermarked and the shadow models. As most SPTs take place in specific contexts, we implant auxiliary prompts during verification to encourage the generation of the context, further enhancing the detection rate. Evaluation results on representative code generation models demonstrate that CodeGenGuard achieves superior watermarking performance to the state-of-the-art.

**Abstract (Chinese)**

代码语言模型（LMs）作为宝贵的知识产权（IP），其训练涉及巨额投资，包括大规模代码语料库、专有标注、海量计算资源以及专有设计。因此，模型知识产权侵权威胁（如未经授权的再分发或模型盗用）日益令人担忧。虽然神经网络水印技术已被广泛研究作为支持模型所有权验证的措施，但为代码LMs添加水印特别具有挑战性，因为代码生成存在看似矛盾的要求：遵守严格的语法规则和语义一致性，同时允许灵活变化以嵌入水印；在保持生成内容高保真度的同时，对提取攻击具有鲁棒性，等等。为了解决这些问题，我们提出了CodeGenGuard，这是一个针对代码LMs的水印框架。CodeGenGuard利用语义保持变换（SPTs）来编码水印，并整合基于死代码的数据增强管道来多样化SPT模式。为了提升鲁棒性，我们引入了高效的双LoRA影子训练方案和可优化的触发提示，该提示能够从水印模型和影子模型中提取水印。由于大多数SPTs发生在特定上下文中，我们在验证过程中植入辅助提示以鼓励生成该上下文，进一步提升检测率。在代表性代码生成模型上的评估结果表明，CodeGenGuard实现了优于最先进水平的水印性能。

---

### CompMarkGS: Robust Watermarking for Compressed 3D Gaussian Splatting

- **Venue**: ICLR 2026 Poster
- **Authors**: Sumin In, Youngdong Jang, Utae Jeong, MinHyuk Jang, Hyeongcheol Park, Eunbyung Park, Sangpil Kim
- **Keywords**: 3D Gaussian Splatting, Digital Watermarking, Privacy
- **OpenReview**: https://openreview.net/forum?id=NXQvejGBFx
- **PDF**: https://openreview.net/pdf?id=NXQvejGBFx

**Abstract**

As 3D Gaussian Splatting (3DGS) is increasingly adopted in various academic and commercial applications due to its high-quality and real-time rendering capabilities, the need for copyright protection is growing. At the same time, its large model size requires efficient compression for storage and transmission. However, compression techniques, especially quantization-based methods, degrade the integrity of existing 3DGS watermarking methods, thus creating the need for a novel methodology that is robust against compression. To ensure reliable watermark detection under compression, we propose a compression-tolerant 3DGS watermarking method that preserves watermark integrity and rendering quality. Our approach utilizes an anchor-based 3DGS, embedding the watermark into anchor attributes, particularly the anchor feature, to enhance security and rendering quality. We also propose a quantization distortion layer that injects quantization noise during training, preserving the watermark after quantization-based compression. Moreover, we employ a frequency-aware anchor growing strategy that enhances rendering quality by effectively identifying Gaussians in high-frequency regions, and an HSV loss to mitigate color artifacts for further rendering quality improvement. Extensive experiments demonstrate that our proposed method preserves the watermark even under compression and maintains high rendering quality.

**Abstract (Chinese)**

随着3D高斯溅射（3DGS）因其高质量和实时渲染能力而日益被各种学术和商业应用采用，版权保护的需求也在增长。同时，其较大的模型尺寸要求高效压缩以用于存储和传输。然而，压缩技术，尤其是基于量化的方法，会降低现有3DGS水印方法的完整性，从而需要一种对压缩鲁棒的新方法。为了在压缩下确保可靠的水印检测，我们提出了一种容忍压缩的3DGS水印方法，该方法保持水印完整性和渲染质量。我们的方法利用基于锚点的3DGS，将水印嵌入锚点属性中，特别是锚点特征，以提升安全性和渲染质量。我们还提出了一种量化失真层，在训练过程中注入量化噪声，从而在基于量化的压缩后保持水印。此外，我们采用了一种频域感知锚点生长策略，通过有效识别高频区域中的高斯来提升渲染质量，以及HSV损失来缓解颜色伪影，进一步改善渲染质量。广泛的实验表明，我们提出方法即使在压缩下也能保持水印，并维持高质量渲染。

---

### Distilling the Thought, Watermarking the Answer: A Principle Semantic Guided Watermark for Reasoning Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Shuliang Liu, Xingyu Li, Hongyi Liu, Dong Fang, Duan Bingchen, Zheng Qi, Lingfeng Su, Xuming Hu
- **Keywords**: Reasoning Large Language Model, Watermark
- **OpenReview**: https://openreview.net/forum?id=T6NVogsXCZ
- **PDF**: https://openreview.net/pdf?id=T6NVogsXCZ

**Abstract**

Reasoning Large Language Models (RLLMs) excelling in complex tasks present unique challenges for digital watermarking, as existing methods often disrupt logical coherence or incur high computational costs. Token-based watermarking techniques  can corrupt the reasoning flow by applying pseudo-random biases, while semantic-aware approaches improve quality but introduce significant latency or require auxiliary models. This paper introduces ReasonMark, a novel watermarking framework specifically designed for reasoning-intensive LLMs. Our approach decouples generation into an undisturbed Thinking Phase and a watermarked Answering Phase. We propose a Criticality Score to identify semantically pivotal tokens from the reasoning trace, which are distilled into a Principal Semantic Vector (PSV). The PSV then guides a semantically-adaptive mechanism that modulates watermark strength based on token-PSV alignment, ensuring robustness without compromising logical integrity. Extensive experiments show ReasonMark surpasses state-of-the-art methods by reducing text Perplexity by 0.35, increasing translation BLEU score by 0.164, and raising mathematical accuracy by 0.67 points. These advancements are achieved alongside a 0.34% higher watermark detection AUC and stronger robustness to attacks, all with a negligible increase in latency. This work enables the traceable and trustworthy deployment of reasoning LLMs in real-world applications.

**Abstract (Chinese)**

在复杂任务中表现出色的推理大型语言模型 (RLLMs) 为数字水印带来了独特挑战，因为现有方法往往破坏逻辑连贯性或导致高计算成本。基于令牌的水印技术通过施加伪随机偏差破坏推理流程，而语义感知方法虽提高了质量，但引入显著延迟或需要辅助模型。本文提出 ReasonMark，一种专为推理密集型 LLM 设计的新型水印框架。我们的方法将生成过程解耦为不受干扰的思考阶段和带水印的回答阶段。我们提出关键性分数，用于从推理轨迹中识别语义关键令牌，并将其提炼为主语义向量 (PSV)。PSV 随后指导一种语义自适应机制，该机制根据令牌-PSV 对齐度调制水印强度，确保鲁棒性而不损害逻辑完整性。广泛实验表明，ReasonMark 通过降低文本困惑度 0.35、提高翻译 BLEU 分数 0.164 以及提升数学准确率 0.67 个百分点，超越了最先进方法。这些进步伴随着水印检测 AUC 提高 0.34%、更强的抗攻击鲁棒性，并且延迟增加微乎其微。本工作实现了推理 LLM 在现实世界应用中的可追溯和可信部署。

---

### EditLens: Quantifying the Extent of AI Editing in Text

- **Venue**: ICLR 2026 Poster
- **Authors**: Katherine Thai, Bradley Emi, Elyas Masrour, Mohit Iyyer
- **Keywords**: AI detection, authorship attribution, human-AI collaboration
- **OpenReview**: https://openreview.net/forum?id=gOkitaPCfZ
- **PDF**: https://openreview.net/pdf?id=gOkitaPCfZ

**Abstract**

A significant proportion of queries to large language models ask them to edit user-provided text, rather than generate new text from scratch. While previous work focuses on detecting fully AI-generated text, we demonstrate that AI-edited text is distinguishable from human-written and AI-generated text. First, we propose using lightweight similarity metrics to quantify the magnitude of AI editing present in a text given the original human-written text and validate these metrics with human annotators. Using these similarity metrics as intermediate supervision, we then train EditLens, a regression model that predicts the amount of AI editing present within a text. Our model achieves state-of-the-art performance on both binary (F1=94.7%) and ternary (F1=90.4%) classification tasks in distinguishing human, AI, and mixed writing. Not only do we show that AI-edited text can be detected, but also that the degree of change made by AI to human writing can be detected, which has implications for authorship attribution, education, and policy. Finally, as a case study, we use our model to analyze the effects of AI-edits applied by Grammarly, a popular writing assistance tool. To encourage further research, we commit to publicly releasing our models and dataset.

**Abstract (Chinese)**

大型语言模型接收到的查询中，有相当大的比例要求其编辑用户提供的文本，而不是从零生成新文本。虽然以往工作专注于检测完全由AI生成的文本，但我们证明AI编辑的文本可以与人类撰写和AI生成的文本区分开来。首先，我们提出使用轻量级相似度度量来量化给定原始人类撰写文本后文本中存在的AI编辑程度，并通过人工标注者验证这些度量。利用这些相似度度量作为中间监督，我们随后训练EditLens，这是一个预测文本中AI编辑量的回归模型。我们的模型在区分人类、AI和混合写作的二元（F1=94.7%）和三元（F1=90.4%）分类任务上达到了最先进的性能。我们不仅证明了AI编辑的文本可以被检测到，而且AI对人类写作所做的更改程度也可以被检测到，这对作者归属、教育和政策具有影响。最后，作为一个案例研究，我们使用我们的模型分析流行写作辅助工具Grammarly应用的AI编辑效果。为了鼓励进一步研究，我们承诺公开发布我们的模型和数据集。

---

### Fingerprinting Deep Neural Networks for Ownership Protection: An Analytical Approach

- **Venue**: ICLR 2026 Poster
- **Authors**: Guang Yang, Ziye Geng, Yihang Chen, Changqing Luo
- **Keywords**: neural network fingerprinting, ownership verification
- **OpenReview**: https://openreview.net/forum?id=sg3UNWKVFt
- **PDF**: https://openreview.net/pdf?id=sg3UNWKVFt

**Abstract**

Adversarial-example-based fingerprinting approaches, which leverage the decision boundary characteristics of deep neural networks (DNNs) to craft fingerprints, has proven effective for protecting model ownership. However, a fundamental challenge remains unresolved: how far a fingerprint should be placed from the decision boundary to simultaneously satisfy two essential properties—robustness and uniqueness—required for effective and reliable ownership protection. Despite the importance of the fingerprint-to-boundary distance, existing works offer no theoretical solution and instead rely on empirical heuristics to determine it, which may lead to violations of either robustness or uniqueness properties.

We propose AnaFP, an analytical fingerprinting scheme that constructs fingerprints under theoretical guidance. Specifically, we formulate the fingerprint generation task as the problem of controlling the fingerprint-to-boundary distance through a tunable stretch factor. To ensure both robustness and uniqueness, we mathematically formalize these properties that determine the lower and upper bounds of the stretch factor. These bounds jointly define an admissible interval within which the stretch factor must lie, thereby establishing a theoretical connection between the two constraints and the fingerprint-to-boundary distance. To enable practical fingerprint generation, we approximate the original (infinite) sets of pirated and independently trained models using two finite surrogate model pools and employ a quantile-based relaxation strategy to relax the derived bounds. Particularly, due to the circular dependency between the lower bound and the stretch factor, we apply a grid search strategy over the admissible interval to determine the most feasible stretch factor. Extensive experimental results demonstrate that AnaFP consistently outperforms prior methods, achieving effective and reliable ownership verification across diverse model architectures and model modification attacks.

**Abstract (Chinese)**

基于对抗样本的指纹方法，利用深度神经网络（DNNs）的决策边界特性来构建指纹，已被证明在保护模型所有权方面有效。然而，一个基本挑战仍未解决：指纹应放置在决策边界多远的位置，以同时满足有效且可靠的所有权保护所需的两个基本属性——鲁棒性和唯一性。尽管指纹到边界的距离至关重要，现有的工作未提供理论解决方案，而是依赖经验启发式方法来确定该距离，这可能导致鲁棒性或唯一性属性的违反。

我们提出AnaFP，一种在理论指导下构建指纹的解析指纹方案。具体而言，我们将指纹生成任务表述为通过可调伸展因子控制指纹到边界距离的问题。为了确保鲁棒性和唯一性，我们数学上形式化这些属性，这些属性决定了伸展因子的下界和上界。这些界限共同定义了一个可容许区间，伸展因子必须位于其中，从而建立了两个约束与指纹到边界距离之间的理论联系。为了实现实际的指纹生成，我们使用两个有限的代理模型池来近似原始的（无限的）盗版模型和独立训练模型集，并采用基于分位数的松弛策略来松弛推导出的界限。特别是，由于下界与伸展因子之间的循环依赖，我们在可容许区间上应用网格搜索策略来确定最可行的伸展因子。大量实验结果表明，AnaFP始终优于先前方法，在各种模型架构和模型修改攻击下实现了有效且可靠的所有权验证。

---

### Guidance Watermarking for Diffusion Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Enoal Gesny, Eva Giboulot, Teddy Furon, Vivien Chappelier
- **Keywords**: watermarking, image generative AI
- **OpenReview**: https://openreview.net/forum?id=5ifzhjMCKq
- **PDF**: https://openreview.net/pdf?id=5ifzhjMCKq

**Abstract**

This paper introduces a novel watermarking method for diffusion models. It is based on guiding the diffusion process using the gradient computed from any off-the-shelf watermark decoder. The gradient is guided further using different image augmentations, increasing robustness to attacks against which the decoder was not originally robust, without retraining or fine-tuning. The methodology effectively allows to convert any post-hoc watermarking scheme into a scheme embedding the signal during the diffusion process. We show that this approach is complementary to watermarking techniques modifying the variational autoencoder at the end of the diffusion process. We validate the methods on different diffusion models and detectors. The watermarking guidance does not significantly alter the generated image for a given seed and prompt, preserving both the diversity and quality of generation.

**Abstract (Chinese)**

本文提出了一种针对扩散模型的新型水印方法。它基于使用任何现成水印解码器计算的梯度来引导扩散过程。该梯度进一步通过不同的图像增强进行引导，从而提高解码器原本不鲁棒的攻击的鲁棒性，而无需重新训练或微调。该方法有效地可以将任何后验水印方案转换为在扩散过程中嵌入信号的方案。我们展示了该方法与修改扩散过程末尾变分自编码器的水印技术互补。我们在不同的扩散模型和检测器上验证了这些方法。水印引导不会显著改变给定种子和提示生成的图像，从而保留了生成的多样性和质量。

---

### HLD: Approximate Hierarchical Linguistic Distribution Modeling for LLM-Generated Text Detection

- **Venue**: ICLR 2026 Poster
- **Authors**: Rui Guo, Weibin Zeng, Fuzhang Wu, Yan Kong, sicheng shen, Yanjun Wu, Weiming Dong
- **Keywords**: Machine-Generated Text Detection; Large language model; Model distribution estimation; Trustworthy AI
- **OpenReview**: https://openreview.net/forum?id=l9mqzHROGu
- **PDF**: https://openreview.net/pdf?id=l9mqzHROGu

**Abstract**

The widespread deployment of large language models (LLMs) has made the reliable detection of AI-generated text a crucial task. However, existing zero-shot detectors typically rely on proxy models to approximate probability distributions of unknown source models at a single token level. Such approaches limit detection effectiveness and make the results highly sensitive to the choice of proxy models. In contrast, supervised classifiers are often detected as black boxes, sacrificing interpretability in the detection process. To address these limitations, we propose a novel detection framework that identifies LLM-generated text by approximating **H**ierarchical **L**inguistic **D**istributions--**HLD-Detector**. Specifically, we leverage n-grams to capture the feature distribution of human-written and machine-generated text across the word, syntactic, and semantic levels, and perform LLM-generated text detection by comparing these distributions under the Bayesian theory. 
By progressively modeling the linguistic distribution from shallow-level (token/word), then medium-level (syntactic), and ultimately high-level (semantic representations), our method mitigates the shortcomings of previous single feature level detectors, improving both robustness and overall performance. Additionally, HLD-Detector requires only a small amount of offline corpus for distribution estimation, instead of relying on online approximation with large proxy models, resulting in significantly lower computational overhead. Extensive experiments have verified the superiority of our method in detection tasks such as multi-llm and multi-domain scenarios, achieving the current SOTA performance.

**Abstract (Chinese)**

大语言模型（LLMs）的广泛部署使得 AI 生成文本的可靠检测成为一项关键任务。然而，现有的零样本检测器通常依赖代理模型在单个 token 级别近似未知源模型的概率分布。此类方法限制了检测效果，并使结果高度敏感于代理模型的选择。相比之下，监督分类器通常将模型视为黑盒，从而牺牲了检测过程中的可解释性。为解决这些局限性，我们提出了一种新型检测框架，通过近似**H**ierarchical **L**inguistic **D**istributions——**HLD-Detector**来识别 LLM 生成的文本。具体而言，我们利用 n-gram 捕捉人工撰写和机器生成文本在词、句法和语义层面的特征分布，并通过贝叶斯理论下比较这些分布来进行 LLM 生成文本检测。通过逐步建模语言分布，从浅层（token/词）、中层（句法）到高层（语义表示），我们的方法缓解了先前单一特征层面检测器的缺点，提高了鲁棒性和整体性能。此外，HLD-Detector 仅需少量离线语料库进行分布估计，而非依赖大型代理模型的在线近似，从而显著降低了计算开销。广泛实验验证了我们的方法在多 LLM 和多领域场景等检测任务中的优越性，达到了当前的 SOTA 性能。

---

### Hey, That's My Model! Introducing Chain & Hash, An LLM Fingerprinting Technique

- **Venue**: ICLR 2026 Poster
- **Authors**: Mark Russinovich, Yanan Cai, Ahmed Salem
- **Keywords**: Large Language Model, LLMs, Fingerprint, Security
- **OpenReview**: https://openreview.net/forum?id=UWi94bRsgm
- **PDF**: https://openreview.net/pdf?id=UWi94bRsgm

**Abstract**

Growing concerns over the theft and misuse of Large Language Models (LLMs) underscore the need for effective fingerprinting to link a model to its original version and detect misuse. We define five essential properties for a successful fingerprint: Transparency, Efficiency, Persistence, Robustness, and Unforgeability. We present a novel fingerprinting framework that provides verifiable proof of ownership while preserving fingerprint integrity. Our approach makes two main contributions. First, a "chain and hash" technique that cryptographically binds fingerprint prompts to their responses, preventing collisions and enabling irrefutable ownership claims. Second, we address a realistic threat model in which instruction-tuned models' output distribution can be significantly altered through meta-prompts. By incorporating random padding and varied meta-prompt configurations during training, our method maintains robustness even under significant output style changes. Experiments show that our framework securely proves ownership, resists both benign transformations (e.g., fine-tuning) and adversarial fingerprint removal, and extends to fingerprinting LoRA adapters. We release our code at: https://github.com/microsoft/Chain-Hash.

**Abstract (Chinese)**

日益增长的对大型语言模型 (LLMs) 被盗用和滥用的担忧凸显了有效指纹技术的需求，以将模型链接到其原始版本并检测滥用。我们定义了成功指纹的五个基本属性：透明性、效率、持久性、鲁棒性和不可伪造性。我们提出了一种新颖的指纹框架，它提供可验证的所有权证明，同时保持指纹完整性。我们的方法做出了两个主要贡献。首先，一种“链和哈希”技术，通过密码学方式将指纹提示绑定到其响应，防止碰撞并实现无可辩驳的所有权声明。其次，我们针对一种现实的威胁模型，其中指令微调模型的输出分布可以通过元提示显著改变。通过在训练过程中引入随机填充和多种元提示配置，我们的方法即使在输出风格发生显著变化时也能保持鲁棒性。实验表明，我们的框架能够安全证明所有权，抵抗良性变换（如微调）和对抗性指纹移除，并扩展到 LoRA 适配器的指纹。我们在 https://github.com/microsoft/Chain-Hash 发布了我们的代码。

---

### In-Context Watermarks for Large Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Yepeng Liu, Xuandong Zhao, Christopher Kruegel, Dawn Song, Yuheng Bu
- **Keywords**: LLMs, Watermark, In-context Learning, Prompt Injection
- **OpenReview**: https://openreview.net/forum?id=fD9YRHazW3
- **PDF**: https://openreview.net/pdf?id=fD9YRHazW3

**Abstract**

The growing use of large language models (LLMs) for sensitive applications has highlighted the need for effective watermarking techniques to ensure the provenance and accountability of AI-generated text. However, most existing watermarking methods require access to the decoding process, limiting their applicability in real-world settings. One illustrative example is the use of LLMs by dishonest reviewers in the context of academic peer review, where conference organizers have no access to the model used but still need to detect AI-generated reviews. Motivated by this gap, we introduce In-Context Watermarking (ICW), which embeds watermarks into generated text solely through prompt engineering, leveraging LLMs' in-context learning and instruction-following abilities. We investigate four ICW strategies at different levels of granularity, each paired with a tailored detection method. We further examine the Indirect Prompt Injection (IPI) setting as a specific case study, in which watermarking is covertly triggered by modifying input documents such as academic manuscripts. Our experiments validate the feasibility of ICW as a model-agnostic, practical watermarking approach. Moreover, our findings suggest that as LLMs become more capable, ICW offers a promising direction for scalable and accessible content attribution. Our code is available at \url{https://github.com/yepengliu/In-Context-Watermarks}.

**Abstract (Chinese)**

大型语言模型 (LLMs) 在敏感应用中的日益广泛使用凸显了有效水印技术的需求，以确保 AI 生成文本的来源和问责制。然而，现有的水印方法大多需要访问解码过程，这限制了它们在现实世界场景中的适用性。一个说明性例子是不诚实审稿人在学术同行评审中使用 LLMs 的情况，其中会议组织者无法访问使用的模型，但仍需检测 AI 生成的审稿意见。受此差距的启发，我们引入了上下文水印 (ICW)，它仅通过提示工程将水印嵌入生成文本中，利用 LLMs 的上下文学习和指令跟随能力。我们研究了四个不同粒度级别的 ICW 策略，每个策略都配有量身定制的检测方法。我们进一步将间接提示注入 (IPI) 设置作为特定案例研究，在该设置中，通过修改输入文档（如学术手稿）来隐秘地触发水印。我们的实验验证了 ICW 作为一种模型无关的、实用的水印方法的可行性。此外，我们的发现表明，随着 LLMs 变得更加强大，ICW 为可扩展且易用的内容归属提供了一个有前景的方向。我们的代码可在 https://github.com/yepengliu/In-Context-Watermarks 获取。

---

### LiteGuard: Efficient Task-Agnostic Model Fingerprinting with Enhanced Generalization

- **Venue**: ICLR 2026 Poster
- **Authors**: Guang Yang, Ziye Geng, Yihang Chen, Changqing Luo
- **Keywords**: neural network fingerprinting, ownership verification
- **OpenReview**: https://openreview.net/forum?id=TFC25ZT9nI
- **PDF**: https://openreview.net/pdf?id=TFC25ZT9nI

**Abstract**

Task-agnostic model fingerprinting has recently gained increasing attention due to its ability to provide a universal framework applicable across diverse model architectures and tasks. The current state-of-the-art method, MetaV, ensures generalization by jointly training a set of fingerprints and a neural-network-based global verifier using two large and diverse model sets: one composed of pirated models (i.e., the protected model and its variants) and the other comprising independently-trained models. However, publicly available models are scarce in many real-world domains, and constructing such model sets requires intensive training efforts and massive computational resources, posing a significant barrier to practical deployment. Reducing the number of models can alleviate the overhead, but increases the risk of overfitting, a problem further exacerbated by MetaV's entangled design, in which all fingerprints and the global verifier are jointly trained. This overfitting issue leads to compromised generalization capability to verify unseen models.

In this paper, we propose LiteGuard, an efficient task-agnostic fingerprinting framework that attains enhanced generalization while significantly lowering computational cost. Specifically, LiteGuard introduces two key innovations: (i) a checkpoint-based model set augmentation strategy that enriches model diversity by leveraging intermediate model snapshots captured during the training of each pirated and independently-trained model—thereby alleviating the need to train a large number of pirated and independently-trained models, and (ii) a local verifier architecture that pairs each fingerprint with a lightweight local verifier, thereby reducing parameter entanglement and mitigating overfitting. Extensive experiments across five representative tasks show that LiteGuard consistently outperforms MetaV in both generalization performance and computational efficiency.

**Abstract (Chinese)**

任务无关模型指纹技术最近因其能够提供适用于多种模型架构和任务的通用框架而备受关注。当前最先进的方法MetaV通过联合训练一组指纹和基于神经网络的全局验证器来确保泛化能力，该训练使用两个大型且多样的模型集：一个由盗版模型（即受保护模型及其变体）组成，另一个由独立训练模型组成。然而，在许多现实世界领域中，公开可用的模型稀缺，构建此类模型集需要密集的训练努力和海量的计算资源，这构成了实际部署的重大障碍。减少模型数量可以缓解开销，但会增加过拟合的风险，这一问题因MetaV的纠缠设计而进一步加剧，在该设计中，所有指纹和全局验证器均联合训练。这一过拟合问题导致验证未见模型的泛化能力受损。

在本文中，我们提出LiteGuard，这是一个高效的任务无关指纹框架，它在显著降低计算成本的同时实现了增强的泛化能力。具体而言，LiteGuard引入了两个关键创新：(i) 基于检查点的模型集增强策略，该策略通过利用每个盗版模型和独立训练模型训练过程中捕获的中间模型快照来丰富模型多样性——从而缓解训练大量盗版模型和独立训练模型的需求；(ii) 局部验证器架构，该架构将每个指纹与轻量级局部验证器配对，从而减少参数纠缠并缓解过拟合。在五个代表性任务上的广泛实验表明，LiteGuard在泛化性能和计算效率两方面均持续优于MetaV。

---

### MOLM: Mixture of LoRA Markers

- **Venue**: ICLR 2026 Poster
- **Authors**: Samar Fares, Nurbek Tastan, Noor Hazim Hussein, Karthik Nandakumar
- **Keywords**: Watermarking, Diffusion models
- **OpenReview**: https://openreview.net/forum?id=1fYQOZovHR
- **PDF**: https://openreview.net/pdf?id=1fYQOZovHR

**Abstract**

Generative models can generate photorealistic images at scale. This raises serious concerns about the ability to detect synthetically generated images and attribute these images to specific sources. While watermarking has emerged as a possible solution, existing methods remain fragile to realistic distortions, susceptible to adaptive removal, and expensive to update when the underlying watermarking key changes. We propose a general watermarking framework that formulates the encoding problem as key-dependent perturbation of the parameters of a generative model. Within this framework, we introduce  Mixture of LoRA Markers (MOLM), a routing-based instantiation in which binary keys activate lightweight low-rank adapters (LoRA) inside residual and attention blocks. This design avoids key-specific re-training and achieves the desired properties such as imperceptibility, fidelity, verifiability, and robustness. Experiments on Stable Diffusion and FLUX show that MOLM preserves image quality while achieving robust key recovery against distortions, compression and regeneration, averaging attacks, and black-box adversarial attacks on the extractor. Code is available at [https://github.com/Samar-Fares/MOLM-Watermark](https://github.com/Samar-Fares/MOLM-Watermark)

**Abstract (Chinese)**

生成模型能够大规模生成照片级真实图像。这引发了对检测合成生成图像并将其归因于特定来源能力的严重担忧。虽然水印技术已成为一种可能的解决方案，但现有方法仍对真实失真脆弱、易受自适应移除影响，并且当底层水印密钥更改时更新成本高昂。我们提出了一种通用水印框架，将编码问题表述为生成模型参数的密钥依赖扰动。在此框架内，我们引入了LoRA标记混合（MOLM），这是一种基于路由的实例化，其中二进制密钥激活残差块和注意力块内的轻量级低秩适配器（LoRA）。这种设计避免了特定密钥的重新训练，并实现了所需的属性，如不可见性、保真度、可验证性和鲁棒性。在Stable Diffusion和FLUX上的实验表明，MOLM在保持图像质量的同时，对失真、压缩和再生、平均攻击以及提取器的黑盒对抗攻击实现了鲁棒的密钥恢复。代码可在[https://github.com/Samar-Fares/MOLM-Watermark](https://github.com/Samar-Fares/MOLM-Watermark)获取。

---

### MUSE: Model-Agnostic Tabular Watermarking via Multi-Sample Selection

- **Venue**: ICLR 2026 Poster
- **Authors**: Liancheng Fang, Aiwei Liu, Henry Peng Zou, Yankai Chen, Hengrui Zhang, Zhongfen Deng, Philip S. Yu
- **Keywords**: Watermark, Tabular Generative Model
- **OpenReview**: https://openreview.net/forum?id=R1QuNKyVOw
- **PDF**: https://openreview.net/pdf?id=R1QuNKyVOw

**Abstract**

We introduce MUSE, a novel watermarking paradigm for tabular generative models. Existing approaches often exploit DDIM invertibility to watermark tabular diffusion models, but tabular diffusion models suffer from poor invertibility, leading to degraded performance. To overcome this limitation, we leverage the computational efficiency of tabular generative models and propose a multi-sample selection paradigm, where watermarks are embedded by generating multiple candidate samples and selecting one according to a specialized scoring function.
    The key advantages of MUSE include (1) Model-agnostic: compatible with any tabular generative model that supports repeated sampling; (2) Flexible: offers flexible designs to navigate the trade-off between generation quality, detectability, and robustness; (3) Calibratable: theoretical analysis provides principled calibration of watermarking strength, ensuring minimal distortion to the original data distribution.
    Extensive experiments on five datasets demonstrate that MUSE substantially outperforms existing methods. Notably, it reduces the distortion rates by 84-88% for fidelity metrics compared with the best performing baselines, while achieving 1.0 TPR@0.1%FPR detection rate.

**Abstract (Chinese)**

我们引入了MUSE，这是一种针对表格生成模型的新型水印范式。现有的方法通常利用DDIM的可逆性来为表格扩散模型添加水印，但表格扩散模型的可逆性较差，导致性能下降。为了克服这一局限性，我们利用表格生成模型的计算效率，并提出了一种多样本选择范式，其中通过生成多个候选样本并根据专用的评分函数选择一个来嵌入水印。

MUSE的主要优势包括：(1) 模型无关：兼容任何支持重复采样的表格生成模型；(2) 灵活：提供灵活的设计来平衡生成质量、可检测性和鲁棒性之间的权衡；(3) 可校准：理论分析提供了水印强度的原则性校准，确保对原始数据分布的最小扭曲。

在五个数据集上的广泛实验表明，MUSE显著优于现有方法。值得注意的是，与表现最佳的基线相比，它将保真度指标的扭曲率降低了84-88%，同时实现了1.0 TPR@0.1%FPR的检测率。

---

### NoisePrints: Distortion-Free Watermarks for Authorship in Private Diffusion Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Nir Goren, Oren Katzir, Abhinav Nakarmi, Eyal Ronen, Mahmood Sharif, Or Patashnik
- **Keywords**: Watermarking, Diffusion Models, Generative AI
- **OpenReview**: https://openreview.net/forum?id=gwHCXvPDBd
- **PDF**: https://openreview.net/pdf?id=gwHCXvPDBd

**Abstract**

With the rapid adoption of diffusion models for visual content generation, proving authorship and protecting copyright have become critical. This challenge is particularly important when model owners keep their models private and may be unwilling or unable to handle authorship issues, making third-party verification essential. A natural solution is to embed watermarks for later verification. However, existing methods require access to model weights and rely on computationally heavy procedures, rendering them impractical and non-scalable. To address these challenges, we propose $\text{\emph{NoisePrints}}$, a lightweight watermarking scheme that utilizes the random seed used to initialize the diffusion process as a proof of authorship without modifying the generation process. Our key observation is that the initial noise derived from a seed is highly correlated with the generated visual content. By incorporating a hash function into the noise sampling process, we further ensure that recovering a valid seed from the content is infeasible. We also show that sampling an alternative seed that passes verification is infeasible, and demonstrate the robustness of our method under various manipulations. Finally, we show how to use cryptographic zero-knowledge proofs to prove ownership without revealing the seed. By keeping the seed secret, we increase the difficulty of watermark removal. In our experiments, we validate NoisePrints on multiple state-of-the-art diffusion models for images and videos, demonstrating efficient verification using only the seed and output, without requiring access to model weights.

**Abstract (Chinese)**

随着扩散模型在视觉内容生成中的快速采用，证明作者身份和保护版权已成为关键问题。当模型所有者将模型保持私有，并且可能不愿意或无法处理作者身份问题时，这一挑战尤为重要，这使得第三方验证变得必不可少。一种自然的解决方案是为后续验证嵌入水印。然而，现有的方法需要访问模型权重，并依赖计算密集型过程，这使得它们不切实际且不可扩展。为了应对这些挑战，我们提出了噪声指纹（NoisePrints），这是一种轻量级水印方案，它利用用于初始化扩散过程的随机种子作为作者身份证明，而无需修改生成过程。我们的关键观察是，从种子衍生的初始噪声与生成的视觉内容高度相关。通过将哈希函数融入噪声采样过程，我们进一步确保从内容中恢复有效种子是不可行的。我们还证明，采样一个通过验证的替代种子是不可行的，并展示了我们的方法在各种操纵下的鲁棒性。最后，我们展示了如何使用密码学零知识证明确认所有权，而无需透露种子。通过保持种子的秘密性，我们增加了水印移除的难度。在我们的实验中，我们在多个最先进的图像和视频扩散模型上验证了噪声指纹，展示了仅使用种子和输出即可进行高效验证，而无需访问模型权重。

---

### PMark: Towards Robust and Distortion-free Semantic-level Watermarking with Channel Constraints

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiahao Huo, Shuliang Liu, Bin Wang, Junyan Zhang, Yibo Yan, Aiwei Liu, Xuming Hu, Mingxun Zhou
- **Keywords**: Semantic-level Watermark; Text Watermark; AI Security
- **OpenReview**: https://openreview.net/forum?id=EhDgP69DJG
- **PDF**: https://openreview.net/pdf?id=EhDgP69DJG

**Abstract**

Semantic-level watermarking (SWM) for large language models (LLMs) enhances watermarking robustness against text modifications and paraphrasing attacks by treating the sentence as the fundamental unit. However, existing methods still lack strong theoretical guarantees of robustness, and reject-sampling–based generation often introduces significant distribution distortions compared with unwatermarked outputs. In this work, we introduce a new theoretical framework on SWM through the concept of proxy functions (PFs) -- functions that map sentences to scalar values. Building on this framework, we propose **PMark**, a simple yet powerful SWM method that estimates the PF median for the next sentence dynamically through sampling while enforcing multiple PF constraints (which we call channels) to strengthen watermark evidence. Equipped with solid theoretical guarantees, **PMark** achieves the desired distortion-free property and improves the robustness against paraphrasing-style attacks. We also provide an empirically optimized version that further removes the requirement for dynamical median estimation for better sampling efficiency. Experimental results show that **PMark** consistently outperforms existing SWM baselines in both text quality and robustness, offering a more effective paradigm for detecting machine-generated text. The source code is available at https://anonymous.4open.science/r/PMark.

**Abstract (Chinese)**

大语言模型（LLMs）的语义级水印（SWM）通过将句子视为基本单元来增强水印对文本修改和改写攻击的鲁棒性。然而，现有的方法仍缺乏强有力的鲁棒性理论保证，并且基于拒绝采样的生成往往会引入与无水印输出相比显著的分布失真。在这项工作中，我们通过代理函数（PFs）——将句子映射到标量值的函数——引入了一个新的SWM理论框架。在此框架基础上，我们提出**PMark**，一种简单而强大的SWM方法，它通过采样动态估计下一个句子的PF中位数，同时强制执行多个PF约束（我们称之为通道）以加强水印证据。配备坚实的理论保证，**PMark**实现了所需的无失真属性，并提高了对改写式攻击的鲁棒性。我们还提供了一个经验优化的版本，进一步消除了动态中位数估计的要求，以提高采样效率。实验结果表明，**PMark**在文本质量和鲁棒性方面始终优于现有的SWM基线，为检测机器生成文本提供了更有效的范式。源代码可在https://anonymous.4open.science/r/PMark获取。

---

### SIGMark: Scalable In-Generation Watermark with Blind Extraction for Video Diffusion

- **Venue**: ICLR 2026 Poster
- **Authors**: Xinjie zhu, Zijing Zhao, Hui Jin, Qingxiao Guo, Yilong Ma, YUNHAO WANG, Xiaobing Guo, Weifeng Zhang
- **Keywords**: watermarking, video generation
- **OpenReview**: https://openreview.net/forum?id=tKyAD2LhnI
- **PDF**: https://openreview.net/pdf?id=tKyAD2LhnI

**Abstract**

Artificial Intelligence Generated Content (AIGC), particularly video generation with diffusion models, has been advanced rapidly. 
Invisible watermarking is a key technology for protecting AI-generated videos and tracing harmful content, and thus plays a crucial role in AI safety.
Beyond post-processing watermarks which inevitably degrade video quality, recent studies have proposed distortion-free in-generation watermarking for video diffusion models.
However, existing in-generation approaches are non-blind: they require maintaining all the message-key pairs and performing template-based matching during extraction, which incurs prohibitive computational costs at scale.
Moreover, when applied to modern video diffusion models with causal 3D Variational Autoencoders (VAEs), their robustness against temporal disturbance becomes extremely weak.
To overcome these challenges, we propose SIGMark, a Scalable In-Generation watermarking framework with blind extraction for video diffusion.
To achieve blind-extraction, we propose to generate watermarked initial noise using a Global set of Frame-wise PseudoRandom Coding keys (GF-PRC), reducing the cost of storing large-scale information while preserving noise distribution and diversity for distortion-free watermarking.
To enhance robustness, we further design a Segment Group-Ordering module (SGO) tailored to causal 3D VAEs, ensuring robust watermark inversion during extraction under temporal disturbance.
Comprehensive experiments on modern diffusion models show that SIGMark achieves very high bit-accuracy during extraction under both temporal and spatial disturbances with minimal overhead, demonstrating its scalability and robustness.
Our code is available at https://github.com/JeremyZhao1998/SIGMark-release.

**Abstract (Chinese)**

人工智能生成内容（AIGC），特别是基于扩散模型的视频生成，已取得快速发展。

隐形水印是保护 AI 生成视频并追踪有害内容的关键技术，因此在 AI 安全中发挥着至关重要的作用。

超越必然降低视频质量的后处理水印，近期研究已提出针对视频扩散模型的无失真生成内水印方法。

然而，现有的生成内方法均为非盲提取：它们需要维护所有消息-密钥对，并在提取过程中执行基于模板的匹配，这在大规模应用中会产生极高的计算成本。

此外，当应用于配备因果 3D 变分自编码器（VAEs）的现代视频扩散模型时，其对时序扰动的鲁棒性变得极度脆弱。

为克服这些挑战，我们提出 SIGMark，这是一个针对视频扩散的可扩展生成内水印框架，支持盲提取。

为实现盲提取，我们提出使用全局帧级伪随机编码密钥集（GF-PRC）生成带水印的初始噪声，从而在保持噪声分布和多样性以实现无失真水印的同时，降低大规模信息存储成本。

为提升鲁棒性，我们进一步设计了针对因果 3D VAEs 的段组排序模块（SGO），确保在时序扰动下提取过程中实现鲁棒的水印反演。

在现代扩散模型上的全面实验表明，SIGMark 在时序和空间扰动下提取时实现了极高的比特准确率，同时开销最小，展示了其可扩展性和鲁棒性。

我们的代码可在 https://github.com/JeremyZhao1998/SIGMark-release 获取。

---

### Safeguarding Multimodal Knowledge Copyright in the RAG-as-a-Service Environment

- **Venue**: ICLR 2026 Poster
- **Authors**: Tianyu Chen, Jian Lou, Wenjie Wang
- **Keywords**: Watermark, VLM, Dataset Copyright Protection
- **OpenReview**: https://openreview.net/forum?id=eWBu4tY9ta
- **PDF**: https://openreview.net/pdf?id=eWBu4tY9ta

**Abstract**

As Retrieval-Augmented Generation (RAG) evolves into service-oriented platforms (Rag-as-a-Service) with shared knowledge bases, protecting the copyright of contributed data becomes essential. Existing watermarking methods in RAG focus solely on textual knowledge, leaving image knowledge unprotected. In this work, we propose \textit{AQUA}, the first watermark framework for image knowledge protection in Multimodal RAG systems. \textit{AQUA} embeds semantic signals into synthetic images using two complementary methods: acronym-based triggers and spatial relationship cues. These techniques ensure watermark signals survive indirect watermark propagation from image retriever to textual generator, being efficient, effective and imperceptible. Experiments across diverse models and datasets show that \textit{AQUA} enables robust, stealthy, and reliable copyright tracing, filling a key gap in multimodal RAG protection.

**Abstract (Chinese)**

随着检索增强生成 (RAG) 演变为具有共享知识库的服务导向平台（Rag-as-a-Service），保护贡献数据的版权变得至关重要。现有的 RAG 水印方法仅关注文本知识，而忽略了图像知识的保护。在本工作中，我们提出了 AQUA，这是多模态 RAG 系统中的首个图像知识保护水印框架。AQUA 使用两种互补方法将语义信号嵌入合成图像中：基于首字母缩写的触发器和空间关系提示。这些技术确保水印信号在从图像检索器到文本生成器的间接水印传播中存活，同时高效、有效且不可察觉。跨多种模型和数据集的实验表明，AQUA 实现了鲁棒、隐秘且可靠的版权追踪，填补了多模态 RAG 保护的关键空白。

---

### SeedPrints: Fingerprints Can Even Tell Which Seed Your Large Language Model Was Trained From

- **Venue**: ICLR 2026 Poster
- **Authors**: Yao Tong, Haonan Wang, Siquan Li, Kenji Kawaguchi, Tianyang Hu
- **Keywords**: fingerprint, LLM
- **OpenReview**: https://openreview.net/forum?id=Kan6Z0zzZi
- **PDF**: https://openreview.net/pdf?id=Kan6Z0zzZi

**Abstract**

Fingerprinting Large Language Models (LLMs) is essential for provenance verification and model attribution. Existing methods typically extract post-hoc signatures based on training dynamics, data exposure, or hyperparameters—properties that only emerge after training begins. In contrast, we propose a stronger and more intrinsic notion of LLM fingerprinting: **SeedPrints**, a method that leverages random initialization biases as persistent, seed-dependent identifiers present even before training. We show that untrained models exhibit reproducible token selection biases conditioned solely on their parameters at initialization. These biases are stable and measurable throughout training, enabling our statistical detection method to recover a model’s lineage with high confidence. Unlike prior techniques, unreliable before convergence and vulnerable to distribution shifts, **SeedPrints** remains effective across all training stages and robust under domain shifts or parameter modifications. Experiments on LLaMA-style and Qwen-style models show that SeedPrints achieves seed-level distinguishability and can provide birth-to-lifecycle identity verification akin to a biometric fingerprint. Evaluations on large-scale pretrained models and fingerprinting benchmarks further confirm its effectiveness under practical deployment scenarios. These results suggest that initialization itself imprints a unique and persistent identity on neural language models, forming a true ``Galtonian'' fingerprint.

**Abstract (Chinese)**

对大语言模型（LLMs）的指纹识别对于来源验证和模型归属至关重要。现有的方法通常基于训练动态、数据暴露或超参数提取事后签名——这些属性仅在训练开始后才会显现。相比之下，我们提出了一种更强且更本质的LLM指纹识别概念：**SeedPrints**，该方法利用随机初始化偏差作为持久的、依赖种子的标识符，这些标识符甚至在训练前就已存在。我们证明，未训练模型表现出仅条件于初始化时参数的可重现令牌选择偏差。这些偏差在整个训练过程中保持稳定且可测量，从而使我们的统计检测方法能够高置信度地恢复模型的谱系。与先前技术不同，后者收敛前不可靠且易受分布偏移影响，**SeedPrints**在所有训练阶段均有效，并在领域偏移或参数修改下保持鲁棒。在LLaMA风格和Qwen风格模型上的实验表明，SeedPrints实现了种子级别的可区分性，并可提供类似于生物识别指纹的从出生到生命周期的身份验证。在大规模预训练模型和指纹识别基准上的评估进一步证实了其在实际部署场景下的有效性。这些结果表明，初始化本身在大语言神经模型上印刻了独特且持久的身份，形成真正的“Galtonian”指纹。

---

### THE SELF-RE-WATERMARKING TRAP: FROM EXPLOIT TO RESILIENCE

- **Venue**: ICLR 2026 Poster
- **Authors**: Vithurabiman Senthuran, Yong Xiang, Iynkaran Natgunanathan, Uthayasanker Thayasivam
- **Keywords**: watemarking, deep learning, AI Security, Re-Watermarking, attack
- **OpenReview**: https://openreview.net/forum?id=st1hrLTP14
- **PDF**: https://openreview.net/pdf?id=st1hrLTP14

**Abstract**

Watermarking has been widely used for copyright protection of digital images. Deep learning-based (DL) watermarking systems have recently emerged as more effective than traditional methods, offering improved fidelity and resilience against attacks. Among the various threats to DL watermarking systems, self-re-watermarking attacks represent a critical and underexplored challenge. In such attacks, the same encoder is maliciously reused to embed a new message into an already watermarked image. This process effectively prevents the original decoder from retrieving the original watermark without introducing perceptual artifacts. In this work, we make two key contributions. First, we introduce the self-re-watermarking threat model as a novel attack vector and demonstrate that existing state-of-the-art watermarking methods consistently fail under such attacks. Second, we develop a self-aware watermarking framework to defend against this threat. Our key insight for mitigating this risk is to limit the sensitivity of the watermarking models to the inputs, thereby resisting re-embedding of new watermarks. To achieve this, we propose a self-aware deep watermarking framework that extends Lipschitz constraints to the watermarking process, regulating encoder–decoder sensitivity in a principled manner. In addition, the framework incorporates re-watermarking adversarial training, which further constrains sensitivity to distortions arising from re-embedding. The proposed method provides theoretical bounds on message recoverability under malicious encoder based re-watermarking and demonstrates strong empirical robustness against diverse scenarios of re-watermarking attempts. Moreover, it maintains high visual fidelity and demonstrates competitive robustness against common image processing distortions compared to state-of-the-art watermarking methods. This work establishes a robust defense against both standard distortions and self-re-watermarking attacks. Code available at https://github.com/SVithurabiman/SRW.

**Abstract (Chinese)**

数字水印已被广泛用于数字图像的版权保护。基于深度学习（DL）的水印系统最近涌现，比传统方法更有效，提供更高的保真度和对攻击的鲁棒性。在针对DL水印系统的各种威胁中，自重水印攻击代表了一个关键且未充分探索的挑战。在此类攻击中，相同的编码器被恶意重用来将新消息嵌入到已水印图像中。这一过程有效地阻止原始解码器检索原始水印，而不引入感知伪影。本工作中，我们做出了两个关键贡献。首先，我们引入自重水印威胁模型作为一种新型攻击向量，并证明现有最先进的水印方法在这种攻击下始终失效。其次，我们开发了一个自感知水印框架来防御这一威胁。我们缓解这一风险的关键洞见是限制水印模型对输入的敏感性，从而抵抗新水印的重嵌入。为实现这一点，我们提出了一种自感知深度水印框架，该框架将Lipschitz约束扩展到水印过程中，以原则性方式调节编码器–解码器敏感性。此外，该框架融入了重水印对抗训练，进一步约束对重嵌入引起的失真的敏感性。所提方法为基于恶意编码器的重水印下的消息可恢复性提供了理论界限，并展示了针对各种重水印尝试场景的强大实证鲁棒性。此外，它保持了高视觉保真度，并与最先进的水印方法相比，在常见图像处理失真下展示了竞争性的鲁棒性。本工作建立了针对标准失真和自重水印攻击的鲁棒防御。代码可在 https://github.com/SVithurabiman/SRW 获取。

---

### Traceable Black-Box Watermarks For Federated Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiahao Xu, Rui Hu, Olivera Kotevska, Zikai Zhang
- **Keywords**: Federated Learning, Watermark, Black-box watermark, Intellectual property protection
- **OpenReview**: https://openreview.net/forum?id=xHRuyXnJXd
- **PDF**: https://openreview.net/pdf?id=xHRuyXnJXd

**Abstract**

Due to the distributed nature of Federated Learning (FL) systems, each local client has access to the global model, which poses a critical risk of model leakage. Existing works have explored injecting watermarks into local models to enable intellectual property protection. However, these methods either focus on non-traceable watermarks or traceable but white-box watermarks. We identify a gap in the literature regarding the formal definition of traceable black-box watermarking and the formulation of the problem of injecting such watermarks into FL systems. In this work, we first formalize the problem of injecting traceable black-box watermarks into FL. Based on the problem, we propose a novel server-side watermarking method, $\mathbf{TraMark}$, which creates a traceable watermarked model for each client, enabling verification of model leakage in black-box settings. To achieve this, $\mathbf{TraMark}$ partitions the model parameter space into two distinct regions: the main task region and the watermarking region. Subsequently, a personalized global model is constructed for each client by aggregating only the main task region while preserving the watermarking region. Each model then learns a unique watermark exclusively within the watermarking region using a distinct watermark dataset before being sent back to the local client. Extensive results across various FL systems demonstrate that $\mathbf{TraMark}$ ensures the traceability of all watermarked models while preserving their main task performance. The code is available at \url{https://github.com/JiiahaoXU/TraMark}.

**Abstract (Chinese)**

由于联邦学习（FL）系统的分布式特性，每个本地客户端均可访问全局模型，这构成了模型泄露的重大风险。现有的工作探索了在本地模型中注入水印以实现知识产权保护。然而，这些方法要么关注非可追踪水印，要么关注可追踪但白盒水印。我们发现在文献中缺少对可追踪黑盒水印的正式定义，以及在FL系统中注入此类水印的问题表述。本工作中，我们首先形式化了在FL中注入可追踪黑盒水印的问题。基于此，我们提出了一种新型服务器端水印方法\textbf{TraMark}，该方法为每个客户端创建可追踪水印模型，从而实现在黑盒设置下验证模型泄露。为实现这一目标，\textbf{TraMark}将模型参数空间划分为两个不同的区域：主任务区域和水印区域。随后，通过仅聚合主任务区域并保留水印区域，为每个客户端构建个性化全局模型。然后，每个模型在使用独特的水印数据集仅在水印区域内学习独特水印，随后发送回本地客户端。在各种FL系统上的广泛实验结果表明，\textbf{TraMark}确保了所有水印模型的可追踪性，同时保持了其主任务性能。代码可在\url{https://github.com/JiiahaoXU/TraMark}获取。

---

### Watermark-based Attribution of AI-Generated Content

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhengyuan Jiang, Moyang Guo, Yuepeng Hu, Yupu Wang, Neil Zhenqiang Gong
- **Keywords**: Image Watermark, Watermark-based Attribution, AI-generated Content
- **OpenReview**: https://openreview.net/forum?id=syOYjXqKnS
- **PDF**: https://openreview.net/pdf?id=syOYjXqKnS

**Abstract**

Several companies have deployed watermark-based detection to identify AI-generated content. However, attribution--the ability to trace back to the user of a generative AI (GenAI) service who created the given AI-generated content--remains largely unexplored despite its growing importance. In this work, we aim to bridge this gap by conducting the first systematic study on watermark-based, user-level attribution of AI-generated content. Our key idea is to assign a unique watermark to each user of the GenAI service and embed this watermark into the AI-generated content created by that user. Attribution is then performed by identifying the user whose watermark best matches the one extracted from the given content. This approach, however, faces a key challenge: How should watermarks be selected for users to maximize attribution performance? To address the challenge, we first theoretically derive lower bounds on detection and attribution performance through rigorous probabilistic analysis for any given set of user watermarks. Then, we select watermarks for users to maximize these lower bounds, thereby optimizing detection and attribution performance. Our theoretical and empirical results show that watermark-based attribution inherits both the accuracy and (non-)robustness properties of the underlying watermark. Specifically, attribution remains highly accurate when the watermarked AI-generated content is either not post-processed or subjected to common post-processing such as JPEG compression, as well as black-box adversarial post-processing with limited query budgets.

**Abstract (Chinese)**

多家公司已部署基于水印的检测机制，以识别AI生成的内容。然而，归因——即追溯生成式AI（GenAI）服务用户并确定其创建给定AI生成内容的身份——尽管其重要性日益增加，但仍未得到充分探索。本文旨在填补这一空白，通过开展首次针对基于水印的用户级AI生成内容归因的系统性研究。我们核心思想是为GenAI服务的每个用户分配一个唯一水印，并将该水印嵌入该用户创建的AI生成内容中。随后，通过识别与从给定内容中提取的水印最匹配的用户水印来实现归因。然而，该方法面临一个关键挑战：如何为用户选择水印以最大化归因性能？为应对这一挑战，我们首先通过严格的概率分析，为任意给定用户水印集理论推导出检测和归因性能的下界。然后，我们为用户选择水印以最大化这些下界，从而优化检测和归因性能。我们的理论和实证结果表明，基于水印的归因继承了底层水印的准确性和（非）鲁棒性特性。具体而言，当水印嵌入的AI生成内容未经过后处理、或经受常见后处理（如JPEG压缩），以及有限查询预算的黑盒对抗后处理时，归因仍保持高度准确。

---
