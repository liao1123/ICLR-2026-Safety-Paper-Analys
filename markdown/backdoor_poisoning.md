# backdoor_poisoning

**Description**: 后门/数据投毒与供应链攻击。包括 backdoor triggers、训练数据投毒、微调投毒、RAG/检索投毒、模型供应链安全、后门检测与移除、数据审计等。

**Paper count**: 23

---

### Watch your steps: Dormant Adversarial Behaviors that Activate upon LLM Finetuning

- **Venue**: ICLR 2026 ConditionalOral
- **Authors**: Thibaud Gloaguen, Mark Vero, Robin Staab, Martin Vechev
- **Keywords**: LLM, Finetuning, Safety
- **OpenReview**: https://openreview.net/forum?id=yfM2e8Icsw
- **PDF**: https://openreview.net/pdf?id=yfM2e8Icsw

**Abstract**

Finetuning open-weight Large Language Models (LLMs) is standard practice for achieving task-specific performance improvements. Until now, finetuning has been regarded as a controlled and secure process in which training on benign datasets leads to predictable behaviors. In this paper, we demonstrate, for the first time, that an adversary can create compromised LLMs that are performant and benign, yet exhibit adversarial behaviors once finetuned by downstream users. To this end, we propose an attack, FAB (Finetuning-activated Adversarial Behaviors), which compromises an LLM via meta-learning techniques that simulate downstream finetuning, explicitly optimizing for the emergence of adversarial behaviors in the finetuned models. At the same time, the compromised LLM is regularized to retain general capabilities and to exhibit no adversarial behaviors prior to finetuning. As a result, when users finetune (e.g., instruction-tuning, distillation, DPO) the seemingly benign model on their own datasets, they unknowingly trigger its dormant adversarial behavior. We experimentally demonstrate the effectiveness of FAB across multiple LLMs and three commonly considered target behaviors: unsolicited advertising, jailbreakability, and over-refusal. We show that FAB-triggers are robust to various finetuning choices made by the user (e.g., dataset, number of steps, scheduler, post-training algorithm). Our findings challenge prevailing assumptions on the security of finetuning, revealing a critical attack vector.

**Abstract (Chinese)**

微调开源大型语言模型（LLMs）是实现任务特定性能改进的标准实践。到目前为止，微调一直被视为一个受控且安全的进程，其中在良性数据集上的训练会导致可预测的行为。在本文中，我们首次证明，攻击者可以创建性能良好且看似良性的受损 LLMs，但一旦被下游用户微调，就会表现出对抗行为。为此，我们提出了一种攻击 FAB（Finetuning-activated Adversarial Behaviors，微调激活的对抗行为），它通过模拟下游微调的元学习技术来污染 LLM，明确优化微调模型中对抗行为的出现。同时，受损 LLM 被正则化以保留通用能力，并在微调前不表现出对抗行为。因此，当用户在其自身数据集上微调（例如，指令微调、蒸馏、DPO）看似良性的模型时，他们会不知不觉地触发其休眠的对抗行为。我们通过实验证明了 FAB 在多个 LLMs 和三种常见目标行为（未经请求的广告、越狱易感性和过度拒绝）上的有效性。我们展示了 FAB 触发器对用户各种微调选择（例如，数据集、步数、调度器、后训练算法）的鲁棒性。我们的发现挑战了关于微调安全性的主流假设，揭示了一个关键的攻击向量。

---

### Invisible Safety Threat: Malicious Finetuning for LLM via Steganography

- **Venue**: ICLR 2026 Oral
- **Authors**: Guangnian Wan, Xinyin Ma, Gongfan Fang, Xinchao Wang
- **Keywords**: LLM, finetuning, safety, steganography
- **OpenReview**: https://openreview.net/forum?id=6cEPDGaShH
- **PDF**: https://openreview.net/pdf?id=6cEPDGaShH

**Abstract**

Understanding and addressing potential safety alignment risks in large language models (LLMs) is critical for ensuring their safe and trustworthy deployment. In this paper, we highlight an insidious safety threat: a compromised LLM can maintain a facade of proper safety alignment while covertly generating harmful content. To achieve this, we finetune the model to understand and apply a steganographic technique. At inference time, we input a prompt that contains a steganographically embedded malicious target question along with a plaintext cover question. The model, in turn, produces a target response similarly embedded within a benign-looking cover response. In this process, human observers only see the model being prompted with a cover question and generating a corresponding cover response, while the malicious content is hidden from view. We demonstrate this invisible safety threat on GPT-4.1 despite the OpenAI fine-tuning API’s safeguards. The finetuned model produces steganographic malicious outputs in response to hidden malicious prompts, while the user interface displays only a fully benign cover interaction. We also replicate the attack on two open-source models, Phi-4 and Mistral-Small-24B-Base-2501, confirming the generality of our method. We quantitatively evaluate our method on the AdvBench dataset, using Llama-Guard-3-8B for content safety classification. Across all three models, all stegotexts containing malicious content are incorrectly classified as safe.

**Abstract (Chinese)**

理解并应对大型语言模型 (LLMs) 中的潜在安全对齐风险对于确保其安全可靠的部署至关重要。本文强调了一种隐蔽的安全威胁：一个被破坏的 LLM 可以维持适当安全对齐的外表，同时隐秘地生成有害内容。为实现这一点，我们微调模型使其理解并应用隐写术技术。在推理时，我们输入一个提示，其中包含隐写嵌入的恶意目标问题以及明文掩护问题。模型则生成一个类似嵌入在看起来良性的掩护响应中的目标响应。在此过程中，人类观察者仅看到模型被掩护问题提示并生成相应的掩护响应，而恶意内容被隐藏起来。我们在 OpenAI 微调 API 的防护措施下，在 GPT-4.1 上演示了这种隐形安全威胁。微调后的模型针对隐藏的恶意提示生成隐写恶意输出，而用户界面仅显示完全良性的掩护交互。我们还在两个开源模型 Phi-4 和 Mistral-Small-24B-Base-2501 上复制了该攻击，证实了我们方法的通用性。我们在 AdvBench 数据集上定量评估了我们的方法，使用 Llama-Guard-3-8B 进行内容安全分类。在所有三个模型上，所有包含恶意内容的隐写文本均被错误分类为安全。

---

### Antibody: Strengthening Defense Against Harmful Fine-Tuning for Large Language Models via Attenuating Harmful Gradient Influence

- **Venue**: ICLR 2026 Poster
- **Authors**: Quoc Minh Nguyen, Trung Le, Jing Wu, Anh Tuan Bui, Mehrtash Harandi
- **Keywords**: Harmful fine-tuning, LLM, safety alignment
- **OpenReview**: https://openreview.net/forum?id=qur2ef8MqQ
- **PDF**: https://openreview.net/pdf?id=qur2ef8MqQ

**Abstract**

Fine-tuning-as-a-service introduces a threat to Large Language Models' safety when service providers fine-tune their models on poisoned user-submitted datasets, a process known as harmful fine-tuning attacks. In this work, we show that by regularizing the gradient contribution of harmful samples encountered during fine-tuning, we can effectively mitigate the impact of harmful fine-tuning attacks. To this end, we introduce Antibody, a defense strategy that first ensures robust safety alignment for the model before fine-tuning, and then applies a safety-preservation learning algorithm during fine-tuning. Specifically, in the alignment stage before fine-tuning, we propose optimizing the model to be in a flat loss region with respect to harmful samples, which makes the safety alignment more resilient to subsequent harmful fine-tuning. Then, in the fine-tuning stage, we design a fine-tuning algorithm that applies a weighting scheme to all samples in each training batch to inhibit the model from learning from harmful samples while encouraging learning from benign samples. Experimental results demonstrate that Antibody successfully mitigates harmful fine-tuning attacks while boosting fine-tuning performance on the user-submitted dataset.

**Abstract (Chinese)**

微调即服务在服务提供商使用带毒的用户提交数据集对模型进行微调时，会对大型语言模型的安全性构成威胁，这一过程被称为有害微调攻击。在本工作中，我们展示了通过正则化微调过程中遇到的有害样本的梯度贡献，可以有效缓解有害微调攻击的影响。为此，我们引入了Antibody，这是一种防御策略，它首先在微调前确保模型具有鲁棒的安全对齐，然后在微调过程中应用安全保持学习算法。具体而言，在微调前的对齐阶段，我们提出优化模型，使其相对于有害样本处于平坦损失区域，从而使安全对齐对后续有害微调更具鲁棒性。然后，在微调阶段，我们设计了一种微调算法，对每个训练批次中的所有样本应用加权方案，以抑制模型从有害样本中学习，同时鼓励从良性样本中学习。实验结果表明，Antibody成功缓解了有害微调攻击，同时提升了在用户提交数据集上的微调性能。

---

### BEAT: Visual Backdoor Attacks on VLM-based Embodied Agents via Contrastive Trigger Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Qiusi Zhan, Hyeonjeong Ha, Rui Yang, Sirui Xu, Hanyang Chen, Liangyan Gui, Yu-Xiong Wang, Huan Zhang, Heng Ji, Daniel Kang
- **Keywords**: vision-language models, backdoor attack, embodied agent
- **OpenReview**: https://openreview.net/forum?id=OwinX7PI83
- **PDF**: https://openreview.net/pdf?id=OwinX7PI83

**Abstract**

Recent advances in Vision-Language Models (VLMs) have propelled embodied agents by enabling direct perception, reasoning, and planning task-oriented actions from visual inputs. 
However, such vision-driven embodied agents open a new attack surface: visual backdoor attacks, where the agent behaves normally until a visual trigger appears in the scene, then persistently executes an attacker-specified multi-step policy.
We introduce BEAT, the first framework to inject such visual backdoors into VLM-based embodied agents using objects in the environments as triggers. 
Unlike textual triggers, object triggers exhibit wide variation across viewpoints and lighting, making them difficult to implant reliably. 
BEAT addresses this challenge by (1) constructing a training set that spans diverse scenes, tasks, and trigger placements to expose agents to trigger variability, and (2) introducing a two-stage training scheme that first applies supervised fine-tuning (SFT) and then our novel Contrastive Trigger Learning (CTL). 
CTL formulates trigger discrimination as preference learning between trigger-present and trigger-free inputs, explicitly sharpening the decision boundaries to ensure precise backdoor activation.
Across various embodied agent benchmarks and VLMs, BEAT achieves attack success rates up to 80\%, while maintaining strong benign task performance, and generalizes reliably to out-of-distribution trigger placements. 
Notably, compared to naive SFT, CTL boosts backdoor activation accuracy up to 39\% under limited backdoor data. 
These findings expose a critical yet unexplored security risk in VLM-based embodied agents, underscoring the need for robust defenses before real-world deployment.

**Abstract (Chinese)**

视觉-语言模型 (VLMs) 的最新进展通过使具身代理能够从视觉输入直接感知、推理并规划面向任务的行动，推动了具身代理的发展。然而，此类视觉驱动的具身代理开辟了一个新的攻击面：视觉后门攻击，其中代理在场景中出现视觉触发器之前表现正常，然后持续执行攻击者指定的多步策略。我们引入 BEAT，这是第一个使用环境中物体作为触发器向基于 VLM 的具身代理注入此类视觉后门的框架。与文本触发器不同，物体触发器在不同视角和照明条件下表现出广泛的变化，使其难以可靠地植入。BEAT 通过以下方式应对这一挑战：(1) 构建一个涵盖多样化场景、任务和触发器放置的训练集，以使代理暴露于触发器变异性；(2) 引入一个两阶段训练方案，首先应用监督微调 (SFT)，然后是我们新颖的对比触发学习 (CTL)。CTL 将触发器辨别表述为触发器存在和无触发器输入之间的偏好学习，明确锐化决策边界以确保精确的后门激活。在各种具身代理基准和 VLMs 上，BEAT 实现了高达 80% 的攻击成功率，同时保持强大的良性任务性能，并可靠地泛化到分布外的触发器放置。值得注意的是，与朴素的 SFT 相比，在后门数据有限的情况下，CTL 将后门激活准确率提高了高达 39%。这些发现暴露了基于 VLM 的具身代理中一个关键但尚未探索的安全风险，强调了在实际部署前需要强大的防御措施。

---

### Be Careful When Fine-tuning On Open-Source LLMs: Your Fine-tuning Data Could Be Secretly Stolen!

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhexin Zhang, Yuhao Sun, Junxiao Yang, Shiyao Cui, yuanchao zhang, Hongning Wang, Minlie Huang
- **Keywords**: finetuning data stealing, open-source LLMs, backdoor training
- **OpenReview**: https://openreview.net/forum?id=HhXOVhO3ia
- **PDF**: https://openreview.net/pdf?id=HhXOVhO3ia

**Abstract**

Fine-tuning on open-source Large Language Models (LLMs) with proprietary data is now a standard practice for downstream developers to obtain task-specific models. Surprisingly, we reveal a new and concerning risk along with the practice: the provider of the open-source LLMs can later extract the private downstream fine-tuning data through simple backdoor training, only requiring black-box access to the fine-tuned downstream model. Our comprehensive experiments, across 4 popularly used open-source models with 3B to 32B parameters and 2 downstream datasets, suggest that the extraction performance can be strikingly high: in practical settings, as much as 76.3\% downstream fine-tuning data (queries) out of a total 5,000 samples can be perfectly extracted, and the success rate can increase to 94.9\% in more ideal settings. We further investigate several defense strategies, but none achieve satisfactory effectiveness in mitigating the risk. Overall, we highlight the emergency of this newly identified data breaching risk in fine-tuning, and we hope more follow-up research can push the progress of addressing this concerning risk. Our code is available at \url{https://github.com/thu-coai/Backdoor-Data-Extraction}.

**Abstract (Chinese)**

使用专有数据对开源大语言模型 (LLMs) 进行微调，已成为下游开发者获取任务特定模型的标准实践。令人惊讶的是，我们揭示了这一实践伴随的一个新的且令人担忧的风险：开源 LLMs 的提供者可以通过简单的后门训练，从仅需黑盒访问的微调下游模型中提取私有下游微调数据。我们在 4 个常用开源模型（参数规模从 3B 到 32B）和 2 个下游数据集上的全面实验表明，提取性能可能惊人地高：在实际设置中，总共 5,000 个样本中多达 76.3% 的下游微调数据（查询）可以被完美提取，而在更理想的设置中，成功率可提高至 94.9%。我们进一步调查了几种防御策略，但均未实现令人满意的有效性来缓解这一风险。总体而言，我们强调了这一新发现的微调数据泄露风险的紧急性，并希望更多后续研究能够推动解决这一令人担忧的风险的进展。我们的代码可在 https://github.com/thu-coai/Backdoor-Data-Extraction 获取。

---

### Beware Untrusted Simulators -- Reward-Free Backdoor Attacks in Reinforcement Learning

- **Venue**: ICLR 2026 Poster
- **Authors**: Ethan Rathbun, Wo Wei Lin, Alina Oprea, Christopher Amato
- **Keywords**: Poisoning Attacks, Backdoor Attacks, Reinforcement Learning, Deep Reinforcement Learning, Robotics
- **OpenReview**: https://openreview.net/forum?id=Z3SH1xlFs6
- **PDF**: https://openreview.net/pdf?id=Z3SH1xlFs6

**Abstract**

Simulated environments are a key piece in the success of Reinforcement Learning (RL), allowing practitioners and researchers to train decision making agents without running expensive experiments on real hardware. Simulators remain a security blind spot, however, enabling adversarial developers to alter the dynamics of their released simulators for malicious purposes. Therefore, in this work we highlight a novel threat, demonstrating how simulator dynamics can be exploited to stealthily implant action-level backdoors into RL agents. The backdoor then allows an adversary to reliably activate targeted actions in an agent  upon observing a predefined "trigger", leading to potentially dangerous consequences. Traditional backdoor attacks are limited in their strong threat models, assuming the adversary has near full control over an agent's training pipeline, enabling them to both alter and observe  agent's rewards. As these assumptions are infeasible to implement within a simulator, we propose a new attack "Daze" which is able to reliably and stealthily implant backdoors into RL agents trained for real world tasks without altering or even observing their rewards. We provide formal proof of Daze's effectiveness in guaranteeing attack success across general RL tasks along with extensive empirical evaluations on both discrete and continuous action space domains. We additionally provide the first example of RL backdoor attacks transferring  to real, robotic hardware. These developments motivate further research into securing all components of the RL training pipeline to prevent malicious attacks.

**Abstract (Chinese)**

模拟环境是强化学习 (RL) 成功的关键组成部分，它允许从业者和研究人员在不进行昂贵的真实硬件实验的情况下训练决策代理。然而，模拟器仍然是一个安全盲点，使得恶意开发者能够更改其发布的模拟器的动态以达到恶意目的。因此，在这项工作中，我们强调了一种新型威胁，展示了如何利用模拟器动态来隐秘地将动作级后门植入 RL 代理中。该后门随后允许攻击者在观察到预定义的“触发器”时可靠地激活代理中的目标动作，从而导致潜在的危险后果。传统的后门攻击在其强威胁模型中受到限制，这些模型假设攻击者对代理的训练管道具有近乎完全控制，从而能够同时更改和观察代理的奖励。由于这些假设在模拟器中无法实现，我们提出了一种新型攻击“Daze”，它能够在不更改甚至不观察其奖励的情况下可靠且隐秘地将后门植入针对真实世界任务训练的 RL 代理中。我们提供了 Daze 在一般 RL 任务中保证攻击成功的有效性的形式证明，以及在离散和连续动作空间域上的广泛实证评估。我们还提供了 RL 后门攻击转移到真实机器人硬件的首个示例。这些发展促使进一步研究 RL 训练管道的所有组件的安全性，以防止恶意攻击。

---

### Defending against Backdoor Attacks via Module Switching

- **Venue**: ICLR 2026 Poster
- **Authors**: Weijun Li, Ansh Arora, Xuanli He, Mark Dras, Qiongkai Xu
- **Keywords**: Backdoor attacks, backdoor defense, model merging
- **OpenReview**: https://openreview.net/forum?id=ieCOL2YAqv
- **PDF**: https://openreview.net/pdf?id=ieCOL2YAqv

**Abstract**

Backdoor attacks pose a serious threat to deep neural networks (DNNs), allowing adversaries to implant triggers for hidden behaviors in inference. Defending against such vulnerabilities is especially difficult in the post-training setting, since end-users lack training data or prior knowledge of the attacks. Model merging offers a cost-effective defense; however, latest methods like weight averaging (WAG) provide reasonable protection when multiple homologous models are available, but are less effective with fewer models and place heavy demands on defenders. We propose a module-switching defense (MSD) for disrupting backdoor shortcuts. We first validate its theoretical rationale and empirical effectiveness on two-layer networks, showing its capability of achieving higher backdoor divergence than WAG, and preserving utility. For deep models, we evaluate MSD on Transformer and CNN architectures and design an evolutionary algorithm to optimize fusion strategies with selective mechanisms to identify the most effective combinations. Experiments shown that MSD achieves stronger defense with fewer models in practical settings, and even under an underexplored case of collusive attacks among multiple models--where some models share same backdoors--switching strategies by MSD deliver superior robustness against diverse attacks.

**Abstract (Chinese)**

后门攻击对深度神经网络 (DNNs) 构成严重威胁，允许攻击者在推理过程中植入触发器以引发隐藏行为。在后训练设置中防御此类漏洞尤为困难，因为终端用户缺乏训练数据或攻击的先验知识。模型融合提供了一种成本有效的防御方法；然而，最新的方法如权重平均 (WAG) 在存在多个同源模型时提供合理的保护，但当模型数量较少时效果较差，且对防御者要求较高。我们提出了一种模块切换防御 (MSD)，用于破坏后门捷径。我们首先在两层网络上验证了其理论依据和实证有效性，展示了其比 WAG 实现更高的后门分歧并保持效用的能力。对于深度模型，我们在 Transformer 和 CNN 架构上评估了 MSD，并设计了一种进化算法，通过选择机制优化融合策略以识别最有效的组合。实验表明，在实际设置中 MSD 使用较少的模型即可实现更强的防御，即使在多模型间勾结攻击的未充分探索情况下——其中某些模型共享相同后门——MSD 的切换策略也能对多样化攻击提供优越的鲁棒性。

---

### Don't Shift the Trigger: Robust Gradient Ascent for Backdoor Unlearning

- **Venue**: ICLR 2026 Poster
- **Authors**: Xingyi Zhao, Tian Xie, Xiaojun Qi, Depeng Xu, Shuhan Yuan
- **Keywords**: gradient ascent, machine unlearning, backdoor defense
- **OpenReview**: https://openreview.net/forum?id=voqtsqYS6j
- **PDF**: https://openreview.net/pdf?id=voqtsqYS6j

**Abstract**

Backdoor attacks pose a significant threat to machine learning models, allowing adversaries to implant hidden triggers that alter model behavior when activated. Although gradient ascent (GA)-based unlearning has been proposed as an efficient backdoor removal approach, we identify a critical yet overlooked issue: vanilla GA does not eliminate the trigger but shifts its impact to different classes, a phenomenon we call trigger shifting. To address this, we propose Robust Gradient Ascent (RGA), which introduces a dynamic penalty mechanism to regulate GA's strength and prevent excessive unlearning. Our experiments show that RGA effectively removes backdoors while preserving model utility, offering a more reliable defense against backdoor attacks.

**Abstract (Chinese)**

后门攻击对机器学习模型构成了重大威胁，允许攻击者在模型中植入隐藏触发器，当触发器被激活时改变模型行为。尽管基于梯度上升 (GA) 的遗忘已被提出作为一种高效的后门移除方法，但我们发现了一个关键却被忽略的问题：vanilla GA 并不消除触发器，而是将其影响转移到不同的类别，我们称之为触发器转移现象。为了解决这一问题，我们提出鲁棒梯度上升 (RGA)，它引入了一种动态惩罚机制来调节 GA 的强度并防止过度遗忘。我们的实验表明，RGA 在保留模型效用的同时有效移除后门，提供了一种更可靠的后门攻击防御方法。

---

### DualEdit: Mitigating Safety Fallback in LLM Backdoor Editing via Affirmation-Refusal Regulation

- **Venue**: ICLR 2026 Poster
- **Authors**: Houcheng Jiang, Zetong Zhao, Junfeng Fang, Haokai Ma, Ruipeng Wang, Xiang Wang, Xiangnan He, Yang Deng
- **Keywords**: LLM; Model Edit; Backdoor Attack
- **OpenReview**: https://openreview.net/forum?id=dLcwLG5axg
- **PDF**: https://openreview.net/pdf?id=dLcwLG5axg

**Abstract**

Safety-aligned large language models (LLMs) remain vulnerable to backdoor attacks. Recent model editing-based approaches enable efficient backdoor injection by directly modifying a small set of parameters to map triggers to attacker-desired behaviors. However, we find that existing editing-based attacks are often unstable under safety alignment: the edited model may start with an affirmative prefix but later revert to refusals during generation. We term this phenomenon \textit{safety fallback}. To mitigate it, we propose \textbf{DualEdit}, a dual-objective model editing framework that simultaneously promotes affirmative tokens and suppresses refusal tokens. DualEdit further addresses two key challenges—objective imbalance and refusal diversity—via two complementary techniques: (1) \textit{Dynamic loss weighting}, which calibrates the relative scales of the two objectives using the pre-edited model to stabilize optimization, and (2) \textit{Value anchoring}, which clusters representative attention value vectors to form compact anchors, reducing conflicts from overly diverse token sets and improving generalization. Experiments on safety-aligned LLMs show that DualEdit improves attack success by 10\% and reduces safety fallback rate by 11\% over baselines. Our code is available at: \url{https://github.com/zhaozetong/DualEdit}.

**Abstract (Chinese)**

安全对齐的大语言模型（LLMs）仍然容易受到后门攻击的影响。最近的基于模型编辑的方法通过直接修改一小组参数，将触发器映射到攻击者期望的行为，从而实现了高效的后门注入。然而，我们发现现有的基于编辑的攻击在安全对齐下往往不稳定：编辑后的模型可能以肯定的前缀开头，但在生成过程中后来又回退到拒绝。我们将这一现象称为\textit{安全回退}。为了缓解这一问题，我们提出了\textbf{DualEdit}，这是一个双目标模型编辑框架，它同时促进肯定令牌并抑制拒绝令牌。DualEdit 通过两种互补技术进一步解决了两个关键挑战——目标不平衡和拒绝多样性：(1) \textit{动态损失加权}，它使用编辑前的模型校准两个目标的相对尺度，以稳定优化；(2) \textit{值锚定}，它聚类代表性的注意值向量以形成紧凑锚点，减少过于多样化的令牌集带来的冲突并改善泛化。在安全对齐的 LLMs 上的实验表明，DualEdit 比基线提高了 10\% 的攻击成功率，并降低了 11\% 的安全回退率。我们的代码可在：https://github.com/zhaozetong/DualEdit 获取。

---

### Fewer Weights, More Problems: A Practical Attack on LLM Pruning

- **Venue**: ICLR 2026 Poster
- **Authors**: Kazuki Egashira, Robin Staab, Thibaud Gloaguen, Mark Vero, Martin Vechev
- **Keywords**: pruning, large language models, security, poisoning
- **OpenReview**: https://openreview.net/forum?id=YRwe9fP7j5
- **PDF**: https://openreview.net/pdf?id=YRwe9fP7j5

**Abstract**

Model pruning, i.e., removing a subset of model weights, has become a prominent approach to reducing the memory footprint of large language models (LLMs) during inference.
Notably, popular inference engines, such as vLLM, enable users to conveniently prune downloaded models before they are deployed.
While the utility and efficiency of pruning methods have improved significantly, the security implications of pruning remain underexplored.
In this work, for the first time, we show that modern LLM pruning methods can be maliciously exploited.
In particular, an adversary can construct a model that appears benign yet, once pruned, exhibits malicious behaviors.
Our method is based on the idea that the adversary can compute a proxy metric that estimates how likely each parameter is to be pruned.
With this information, the adversary can first inject a malicious behavior into those parameters that are unlikely to be pruned.
Then, they can repair the model by using parameters that are \textit{likely} to be pruned, effectively canceling out the injected behavior in the unpruned model.
We demonstrate the severity of our attack through extensive evaluation on five models; after any of the pruning in vLLM are applied (Magnitude, Wanda, and SparseGPT), it consistently exhibits strong malicious behaviors in a diverse set of attack scenarios (success rates of up to 95.7% for jailbreak, 98.7% for benign instruction refusal, and 99.5% for targeted content injection).
Our results reveal a critical deployment-time security gap and underscore the urgent need for stronger security awareness in model compression.

**Abstract (Chinese)**

模型剪枝，即移除模型权重的一个子集，已成为减少大型语言模型（LLMs）在推理过程中内存占用的一种突出方法。  
值得注意的是，流行的推理引擎如 vLLM 允许用户在部署前方便地对下载的模型进行剪枝。  
虽然剪枝方法的实用性和效率已显著提升，但剪枝的安全含义仍未得到充分探索。  
在本工作中，我们首次证明现代 LLM 剪枝方法可以被恶意利用。  
特别是，攻击者可以构建一个看似良性的模型，但一旦剪枝，就会表现出恶意行为。  
我们的方法基于这样一个思想：攻击者可以计算一个代理指标，用于估计每个参数被剪枝的可能性。  
利用这一信息，攻击者首先可以将恶意行为注入到那些不太可能被剪枝的参数中。  
然后，他们可以使用很可能被剪枝的参数来修复模型，从而在未剪枝模型中有效抵消注入的行为。  
我们通过对五个模型的广泛评估证明了我们攻击的严重性；在应用 vLLM 中的任何剪枝方法（Magnitude、Wanda 和 SparseGPT）后，它在多种攻击场景中一致表现出强烈的恶意行为（越狱成功率高达 95.7%、良性指令拒绝 98.7%、针对性内容注入 99.5%）。  
我们的结果揭示了部署时的一个关键安全漏洞，并强调了在模型压缩中加强安全意识的迫切需要。

---

### Ghost in the Cloud: Your Geo-Distributed Large Language Models Training is Easily Manipulated

- **Venue**: ICLR 2026 Poster
- **Authors**: Zichen TANG, Zhenheng Tang, Gaoning Pan, Buhua Liu, Xin He, Kunfeng Lai, Xiaowen Chu, Bo Li
- **Keywords**: Jailbreak attack, Geo-distributed LLM Training, Federated Learning, Large Language Models
- **OpenReview**: https://openreview.net/forum?id=FwnmQnVc7g
- **PDF**: https://openreview.net/pdf?id=FwnmQnVc7g

**Abstract**

Geo-distributed training and Federated Learning (FL) provide viable solutions to address the substantial data and computational resource needs associated with training large language models (LLMs). However, we empirically demonstrate that a single adversarial participant can significantly compromise the safety alignment of LLMs through malicious training, exposing serious security risks.
We identify two existing server-side defense strategies that effectively counter naive jailbreak attacks—Task Performance Check (TPC), which filters out model updates with low downstream performance, and Malicious Output Scrutiny (MOS), which detects harmful outputs by prompting uploaded models with malicious queries.
To evade both defenses, we design a trigger-based jailbreak variant that preserves downstream performance using a novel regularization method to limit the excessive model updates on jailbreak datasets. We further conceal malicious triggers by mixing the malicious dataset with pseudo-contrastive safety-aligned answers to maintain the original safety alignment.
Experiments on three widely-used safety-aligned LLMs show that a single adversarial participant can implant triggers into the global model without degrading downstream performance, achieving an 80\% attack success rate (ASR) with a 7\% low detection true rate (DTR).

**Abstract (Chinese)**

地理分布式训练和联邦学习 (FL) 为训练大语言模型 (LLMs) 所需的大量数据和计算资源需求提供了可行的解决方案。然而，我们通过实证研究表明，单个对抗性参与者可以通过恶意训练显著破坏 LLMs 的安全对齐，从而暴露严重的セキュリティ风险。

我们识别出两种现有的服务器端防御策略，它们能有效对抗朴素越狱攻击——任务性能检查 (TPC)，它过滤掉下游性能低的模型更新；以及恶意输出审查 (MOS)，它通过用恶意查询提示上传的模型来检测有害输出。

为了规避两种防御，我们设计了一种基于触发器的越狱变体，使用一种新型正则化方法限制越狱数据集上的过度模型更新，从而保持下游性能。我们进一步通过将恶意数据集与伪对比安全对齐答案混合来隐藏恶意触发器，以维持原始的安全对齐。

在三种广泛使用的安全对齐 LLMs 上的实验表明，单个对抗性参与者可以在不降低下游性能的情况下将触发器植入全局模型，实现 80\% 的攻击成功率 (ASR) 和 7\% 的低检测真率 (DTR)。

---

### JailbreakLoRA: Your Downloaded LoRA from Sharing Platforms might be Unsafe

- **Venue**: ICLR 2026 Poster
- **Authors**: Fanjunduo Wei, Zhenheng Tang, Rongfei Zeng, Tongliang Liu, Chengqi Zhang, Xiaowen Chu, Bo Han
- **Keywords**: Jailbreak, LoRA, Large Language Models
- **OpenReview**: https://openreview.net/forum?id=4YgvVRoSnF
- **PDF**: https://openreview.net/pdf?id=4YgvVRoSnF

**Abstract**

Low-Rank Adaptation (LoRA) benefits from its plug-and-play nature, enabling large language models (LLMs) to achieve significant performance gains at low cost, has driven the development of LoRA-sharing platforms. However, the jailbreak and backdoor concerns associated with LoRA-sharing platforms remain underexplored. Existing LoRA-based attacks primarily focus on achieving high attack success rates, while neglecting the core reason why LoRA is adopted by user, i.e. to gain downstream task capabilities. However, achieving effective attacks while preserving strong multi-task performance remains challenging, as the largely unrelated objectives tend to interfere with each other during optimization. In this paper, we propose JailbreakLoRA, a multi-task jailbreak LoRA training method that balances task utility and attack capability, it resolves training interference by uncertainty-weighting losses and mitigating gradient conflicts. Additionally, JailbreakLoRA is designed to generate an affirmative prefix upon trigger activation, exploiting inference-time hallucinations to enhance the effectiveness of jailbreak. Experimental results demonstrate that our method outperforms SOTA LoRA-based attacks, achieving a 16.0\% improvement in attack success rate while also enhancing performance on multi-downstream tasks by 16.5\% in average. Our code is available at https://github.com/tmlr-group/JailbreakLoRA.

**Abstract (Chinese)**

低秩适应 (LoRA) 得益于其即插即用的特性，能够使大语言模型 (LLMs) 以低成本获得显著性能提升，从而推动了 LoRA 共享平台的发展。然而，与 LoRA 共享平台相关的越狱和后门问题仍未得到充分探索。现有的基于 LoRA 的攻击主要关注实现高攻击成功率，而忽略了用户采用 LoRA 的核心原因，即获得下游任务能力。然而，在保持强大多任务性能的同时实现有效攻击仍具挑战性，因为这些在很大程度上无关的目标在优化过程中往往会相互干扰。本文提出 JailbreakLoRA，一种平衡任务效用和攻击能力的多任务越狱 LoRA 训练方法，它通过不确定性加权损失和缓解梯度冲突来解决训练干扰。此外，JailbreakLoRA 被设计为在触发激活时生成肯定性前缀，利用推理时的幻觉来提升越狱的有效性。实验结果表明，我们的方法优于最先进的基于 LoRA 的攻击，在攻击成功率上实现了 16.0% 的提升，同时在多下游任务上的性能平均提升了 16.5%。我们的代码可在 https://github.com/tmlr-group/JailbreakLoRA 获取。

---

### Perturbation-Induced Linearization: Constructing Unlearnable Data with Solely Linear Classifiers

- **Venue**: ICLR 2026 Poster
- **Authors**: Jinlin Liu, Wei Chen, Xiaojin Zhang
- **Keywords**: unlearnable examples, data protection, linear model, shortcut, linearity
- **OpenReview**: https://openreview.net/forum?id=GBSGToE97J
- **PDF**: https://openreview.net/pdf?id=GBSGToE97J

**Abstract**

Collecting web data to train deep models has become increasingly common, raising concerns about unauthorized data usage. To mitigate this issue, unlearnable examples introduce imperceptible perturbations into data, preventing models from learning effectively. However, existing methods typically rely on deep neural networks as surrogate models for perturbation generation, resulting in significant computational costs. In this work, we propose Perturbation-Induced Linearization (PIL), a computationally efficient yet effective method that generates perturbations using only linear surrogate models. PIL achieves comparable or better performance than existing surrogate-based methods while reducing computational time dramatically. We further reveal a key mechanism underlying unlearnable examples: inducing linearization to deep models, which explains why PIL can achieve competitive results in a very short time. Beyond this, we provide an analysis about the property of unlearnable examples under percentage-based partial perturbation. Our work not only provides a practical approach for data protection but also offers insights into what makes unlearnable examples effective.

**Abstract (Chinese)**

收集网络数据以训练深度模型已成为越来越常见的做法，这引发了对未经授权数据使用的担忧。为了缓解这一问题，不可学习示例通过向数据引入不可察觉的扰动，防止模型有效学习。然而，现有的方法通常依赖深度神经网络作为代理模型来生成扰动，从而导致显著的计算成本。在这项工作中，我们提出扰动诱导线性化（PIL），这是一种计算高效且有效的方法，仅使用线性代理模型生成扰动。PIL实现了与现有基于代理的方法相当或更好的性能，同时显著减少了计算时间。我们进一步揭示了不可学习示例的一个关键机制：向深度模型诱导线性化，这解释了为什么PIL能够在极短时间内取得竞争性结果。除此之外，我们对基于百分比的部分扰动下不可学习示例的特性进行了分析。我们的工作不仅为数据保护提供了一种实用方法，还提供了关于不可学习示例有效性的洞见。

---

### Reliable Poisoned Sample Detection against Backdoor Attacks Enhanced by Sharpness Aware Minimization

- **Venue**: ICLR 2026 Poster
- **Authors**: Mingda Zhang, Mingli Zhu, Zihao Zhu, Li Shen, Baoyuan Wu
- **Keywords**: Backdoor Defense, Poisoned Sample Detection, AI security
- **OpenReview**: https://openreview.net/forum?id=q5ePtZc9N7
- **PDF**: https://openreview.net/pdf?id=q5ePtZc9N7

**Abstract**

This work investigates Poisoned Sample Detection (PSD), a promising defense approach against backdoor attacks. However, we observe that the effectiveness of many advanced PSD methods degrades significantly under weak backdoor attacks (\eg, low poisoning ratios or weak trigger patterns). To substantiate this observation, we conduct a statistical analysis across various attacks and PSD methods, revealing a strong correlation between the strength of the backdoor effect and the detection performance. Inspired by this, we propose amplifying the backdoor effect through training with Sharpness-Aware Minimization (SAM). Both theoretical insights and empirical evidence validate that SAM enhances the activations of top Trigger Activation Change (TAC) neurons while suppressing others. Based on this, we introduce SAM-enhanced PSD, a simple yet effective framework that seamlessly improves existing PSD methods by extracting detection features from the SAM-trained model rather than the conventionally trained model. Extensive experiments across multiple benchmarks demonstrate that our approach significantly improves detection performance under both strong and weak backdoor attacks, achieving an average True Positive Rate (TPR) gain of +34.3% over conventional PSD methods. Overall, we believe that the revealed correlation between the backdoor effect and detection performance could inspire future research advancements.

**Abstract (Chinese)**

本文研究了中毒样本检测（PSD），这是一种针对后门攻击的有前景的防御方法。然而，我们观察到，许多先进的PSD方法在弱后门攻击（例如，低中毒比率或弱触发模式）下的有效性显著下降。为了证实这一观察，我们对各种攻击和PSD方法进行了统计分析，揭示了后门效应的强度与检测性能之间存在强烈的相关性。受此启发，我们提出通过使用锐度感知最小化（SAM）训练来放大后门效应。理论洞见和实证证据均验证了SAM增强了顶级触发激活变化（TAC）神经元的激活，同时抑制了其他神经元。基于此，我们引入了SAM增强的PSD，这是一个简单而有效的框架，通过从SAM训练的模型而非传统训练的模型中提取检测特征，来无缝提升现有的PSD方法。在多个基准上的广泛实验表明，我们的方法在强后门攻击和弱后门攻击下均显著提升了检测性能，相对于传统PSD方法平均真阳性率（TPR）提升了+34.3%。总体而言，我们相信所揭示的后门效应与检测性能之间的相关性将能启发未来的研究进展。

---

### STEDiff: Revealing the Spatial and Temporal Redundancy of Backdoor Attacks in Text-to-Image Diffusion Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Yu Pan, Jiahao Chen, Lin Wang, Bingrong Dai, Wenjie Wang
- **Keywords**: Diffusion Models; Backdoor Attacks; Backdoor Defense; AI Security
- **OpenReview**: https://openreview.net/forum?id=O02qsgSUtY
- **PDF**: https://openreview.net/pdf?id=O02qsgSUtY

**Abstract**

Recently, diffusion models have been recognized as state-of-the-art models for image generation due to their ability to produce high-quality images. However, recent studies have shown that diffusion models are susceptible to backdoor attacks, where an attacker can activate hidden biases using a specific trigger pattern, causing the model to generate a predefined target. Fortunately, executing backdoor attacks is still challenging, as they typically require substantial time and memory to perform parameter-based fine-tuning. In this paper, we are the first to reveal the **spatio-temporal redundancy** in backdoor attacks on diffusion models. **Regarding spatial redundancy**, we observed the *enrichment phenomenon*, which reflects the abnormal gradient accumulation induced by backdoor injection. **Regarding temporal redundancy**, we observed a marginal effect associated with specific time steps, indicating that only a limited subset of time steps plays a critical role in backdoor injection. Building on these findings, we present a novel framework, *STEDiff*, comprising two key components: *STEBA* and *STEDF*. *STEBA* is a spatio-temporally efficient accelerated attack strategy that achieves up to **15.07×** speedup in backdoor injection while reducing GPU memory usage by **82%**. *STEDF* is a detection framework leveraging spatio-temporal features, by modeling the enrichment phenomenon in weights and anisotropy across time steps, which achieves a backdoor detection rate of up to **99.8%**.  Our code is available at: [https://github.com/paoche11/STEDiff](https://github.com/paoche11/STEDiff).

**Abstract (Chinese)**

最近，扩散模型因其生成高质量图像的能力而被公认为图像生成的最先进模型。然而，最近的研究表明，扩散模型易受后门攻击的影响，其中攻击者可以使用特定触发模式激活隐藏偏置，导致模型生成预定义的目标。幸运的是，执行后门攻击仍然具有挑战性，因为它们通常需要大量时间和内存来进行基于参数的微调。在本文中，我们首次揭示了扩散模型后门攻击中的**时空冗余**。**关于空间冗余**，我们观察到*富集现象*，这反映了后门注入诱发的异常梯度积累。**关于时间冗余**，我们观察到与特定时间步相关的边际效应，这表明只有有限的时间步子集在后门注入中起关键作用。基于这些发现，我们提出了一种新型框架*STEDiff*，它包括两个关键组件：*STEBA* 和 *STEDF*。*STEBA* 是一种时空高效的加速攻击策略，在后门注入中实现了高达**15.07×**的加速，同时将GPU内存使用量降低了**82%**。*STEDF* 是一种利用时空特征的检测框架，通过建模权重中的富集现象和时间步间的各向异性，实现了高达**99.8%**的后门检测率。我们的代码可在：[https://github.com/paoche11/STEDiff](https://github.com/paoche11/STEDiff) 获取。

---

### SafeMoE: Safe Fine-Tuning for MoE LLMs by Aligning Harmful Input Routing

- **Venue**: ICLR 2026 Poster
- **Authors**: Jaehan Kim, Minkyoo Song, Seungwon Shin, Sooel Son
- **Keywords**: AI safety, Large language model, Mixture-of-Experts
- **OpenReview**: https://openreview.net/forum?id=W1x9AzkSnU
- **PDF**: https://openreview.net/pdf?id=W1x9AzkSnU

**Abstract**

Recent large language models (LLMs) have increasingly adopted the Mixture-of-Experts (MoE) architecture for efficiency. MoE-based LLMs heavily depend on a superficial safety mechanism in which harmful inputs are routed safety-critical experts. However, our analysis reveals that routing decisions for harmful inputs drift significantly after fine-tuning, exposing a critical vulnerability to harmful fine-tuning (HFT) attacks. Existing defenses, primarily designed for monolithic LLMs, are less effective for MoE LLMs as they fail to prevent drift in harmful input routing. To address this limitation, we propose SafeMoE, a safe fine-tuning method tailored to MoE LLMs. SafeMoE directly mitigates routing drift by penalizing the gap between the routing weights of a fine-tuned model and those of the initial safety-aligned model, thereby preserving the safety-aligned routing of harmful inputs to safety-critical experts. Experiments on open-source MoE LLMs ranging from 7B to 141B parameters demonstrate that SafeMoE effectively mitigates HFT attacks, reducing the harmfulness score of OLMoE from 62.0 to 5.0, for example, while maintaining task utility within 1% degradation and incurring only 2% overhead. It significantly outperforms state-of-the-art defense methods for safeguarding LLM fine-tuning and remains effective in recent large-scale MoE LLMs such as gpt-oss and Llama 4. Our implementation is available at https://github.com/jaehanwork/SafeMoE.

**Abstract (Chinese)**

最近的大型语言模型 (LLMs) 越来越多地采用专家混合 (MoE) 架构以提高效率。基于 MoE 的 LLMs 高度依赖一种表面的安全机制，其中有害输入被路由至安全关键专家。然而，我们的分析揭示，在微调后，有害输入的路由决策会显著漂移，从而暴露了对有害微调 (HFT) 攻击的关键漏洞。现有的防御方法主要针对单体 LLMs 设计，对 MoE LLMs 效果较差，因为它们无法防止有害输入路由的漂移。为了解决这一局限性，我们提出了 SafeMoE，这是一种专为 MoE LLMs 量身定制的安全微调方法。SafeMoE 通过惩罚微调模型的路由权重与其初始安全对齐模型路由权重之间的差距，直接缓解路由漂移，从而保留有害输入向安全关键专家的安全对齐路由。在从 7B 到 141B 参数的开源 MoE LLMs 上的实验表明，SafeMoE 有效缓解了 HFT 攻击，例如将 OLMoE 的有害性分数从 62.0 降低到 5.0，同时任务效用仅下降 1% 以内，并仅产生 2% 的开销。它显著优于最先进的 LLM 微调防护方法，并在最近的大型 MoE LLMs（如 gpt-oss 和 Llama 4）中保持有效。我们的实现可在 https://github.com/jaehanwork/SafeMoE 获取。

---

### Safety at One Shot: Patching Fine-Tuned LLMs with A Single Instance

- **Venue**: ICLR 2026 Poster
- **Authors**: Jiawen Zhang, Tony He, Kejia Chen, Jian Lou, Jian Liu, Xiaohu Yang, Ruoxi Jia
- **Keywords**: Safety Alignment, Large Language Models, Fine-tuning Attack
- **OpenReview**: https://openreview.net/forum?id=EyH8Fu3vtZ
- **PDF**: https://openreview.net/pdf?id=EyH8Fu3vtZ

**Abstract**

Fine-tuning safety-aligned large language models (LLMs) can substantially compromise their safety. Previous approaches require many safety samples or calibration sets, which not only incur significant computational overhead during realignment but also lead to noticeable degradation in model utility. Contrary to this belief, we show that safety alignment can be fully recovered with only a single safety example, without sacrificing utility and at minimal cost. Remarkably, this recovery is effective regardless of the number of harmful examples used in fine-tuning or the size of the underlying model, and convergence is achieved within just a few epochs. Furthermore, we uncover the low-rank structure of the safety gradient, which explains why such efficient correction is possible. We validate our findings across five safety-aligned LLMs and multiple datasets, demonstrating the generality of our approach.

**Abstract (Chinese)**

微调安全对齐的大型语言模型（LLMs）可能会显著损害其安全性。先前方法需要大量安全样本或校准集，这不仅在重新对齐过程中造成显著的计算开销，还会导致模型效用的明显退化。与此信念相反，我们证明，仅使用单个安全示例即可完全恢复安全对齐，而无需牺牲效用且成本极低。值得注意的是，这种恢复无论微调中使用的有害示例数量或底层模型规模如何均有效，且仅需几轮训练即可收敛。此外，我们揭示了安全梯度的低秩结构，这解释了为何如此高效的校正是可能的。我们在五个安全对齐的LLMs和多个数据集上验证了我们的发现，证明了我们方法的通用性。

---

### Self-Destructive Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Yuhui Wang, Rongyi Zhu, Ting Wang
- **Keywords**: Self-destructive Model, Safety Alignment, Harmful Fine-tuning Attack
- **OpenReview**: https://openreview.net/forum?id=ERNpUGr8M5
- **PDF**: https://openreview.net/pdf?id=ERNpUGr8M5

**Abstract**

Harmful fine-tuning attacks represent a major threat to the security of large language models (LLMs), allowing adversaries to compromise safety guardrails with minimal harmful data. While existing defenses attempt to reinforce LLM alignment, they fail to address models' inherent `trainability' on harmful data, leaving them vulnerable to stronger attacks with increased learning rates or larger harmful datasets. To overcome this limitation, we introduce SEAM, a novel alignment-enhancing defense that transforms LLMs into self-destructive models with intrinsic resilience to misalignment attempts. Specifically, these models retain their capabilities for legitimate tasks while exhibiting substantial performance degradation when fine-tuned on harmful data. The protection is achieved through a novel loss function that couples the optimization trajectories of benign and harmful data, enhanced with adversarial gradient ascent to amplify the self-destructive effect. To enable practical training, we develop an efficient Hessian-free gradient estimate with theoretical error bounds. Extensive evaluation across LLMs and datasets demonstrates that SEAM creates a no-win situation for adversaries: the self-destructive models achieve state-of-the-art robustness against low-intensity attacks and undergo catastrophic performance collapse under high-intensity attacks, rendering them effectively unusable. The code
is available: https://github.com/ZJUWYH/seam (warning: this paper contains potentially harmful content generated by LLMs.)

**Abstract (Chinese)**

有害微调攻击对大型语言模型（LLMs）的安全性构成了重大威胁，允许攻击者仅使用少量有害数据即可破坏安全护栏。虽然现有防御方法试图强化LLM的对齐，但它们未能解决模型在有害数据上的固有“可训练性”，从而使其易受更高学习率或更大有害数据集的更强攻击影响。为克服这一局限性，我们引入SEAM，一种新型对齐增强防御方法，它将LLMs转化为具有对失准尝试内在鲁棒性的自毁模型。具体而言，这些模型在合法任务上保留其能力，但在有害数据微调时表现出显著性能退化。该保护通过一种新型损失函数实现，该函数耦合了良性数据和有害数据的优化轨迹，并结合对抗梯度上升以放大自毁效果。为实现实用训练，我们开发了一种高效的无Hessian梯度估计方法，并提供了理论误差界。针对多种LLMs和数据集的广泛评估表明，SEAM为攻击者制造了进退两难的局面：自毁模型在低强度攻击下实现了最先进的鲁棒性，而在高强度攻击下则发生灾难性性能崩溃，使其实际上不可用。代码可用：https://github.com/ZJUWYH/seam（警告：本文包含由LLMs生成的有潜在危害的内容。）

---

### Test-Time Poisoned Sample Detection by Exploiting Shallow Malicious Matching in Backdoored CLIP

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhengyao Song, Meixi Zheng, Ke Xu, Yongqiang Li, Baoyuan Wu
- **Keywords**: poisoned sample detection, backdoor defense, CLIP, shallow malicious matching
- **OpenReview**: https://openreview.net/forum?id=Kpij6oOnJl
- **PDF**: https://openreview.net/pdf?id=Kpij6oOnJl

**Abstract**

CLIP, known for its strong semantic matching capabilities derived from large-scale pretraining, has been shown to be vulnerable to backdoor attacks in prior work. In this work, we find that such attacks leave a detectable trace. This trace manifests as a divergence in how image features align with the CLIP's text manifold where semantically similar texts cluster. Specifically, benign images exhibit *deep benign matching*, where their features are close not only to the predicted text caption but also to the broader manifold of semantically equivalent variants of that caption. In contrast, poisoned images display *shallow malicious matching*, where their features shallowly align with the specific target caption but remain distant from its semantic neighborhood. Leveraging this insight, we propose **Subspace Detection**, a novel test-time poisoned image detection method against backdoored CLIP. First, for a test image, we approximate its corresponding local text manifold by constructing a low-dimensional subspace from semantically equivalent variants of its predicted text. Second, within this broad subspace, we probe a region-of-interest that maximally amplifies the separation between the two types of images: benign images remain close due to deep matching, while poisoned images deviate significantly due to shallow matching. Finally, we identify whether the test image is poisoned by measuring its deviation from this region; a large deviation indicates a poisoned image. Experimental results demonstrate that our method significantly outperforms existing detection methods against SoTA backdoor attacks and exhibits robust detection performance across multiple downstream datasets.

**Abstract (Chinese)**

CLIP 以其源于大规模预训练的强大语义匹配能力而闻名，先前工作已证明其易受后门攻击影响。在本工作中，我们发现此类攻击会留下可检测的痕迹。该痕迹表现为图像特征与 CLIP 的文本流形（其中语义相似的文本聚类）对齐方式的差异。具体而言，良性图像表现出*深度良性匹配*，其特征不仅接近预测的文本描述，还接近该描述语义等价变体的更广流形。相反，中毒图像显示*浅层恶意匹配*，其特征浅层对齐特定目标描述，但远离其语义邻域。利用这一洞见，我们提出**子空间检测**，一种针对后门 CLIP 的新型测试时中毒图像检测方法。首先，对于测试图像，我们通过从其预测文本的语义等价变体构建低维子空间，来近似其对应的局部文本流形。其次，在这一广义子空间内，我们探测一个感兴趣区域，该区域最大化放大两种图像类型的分离：良性图像由于深度匹配而保持接近，而中毒图像由于浅层匹配而显著偏离。最后，我们通过测量其从该区域的偏离来识别测试图像是否中毒；较大偏离表示中毒图像。实验结果表明，我们的方法显著优于现有检测方法对抗 SOTA 后门攻击，并在多个下游数据集上表现出稳健的检测性能。

---

### Token-level Data Selection for Safe LLM Fine-tuning

- **Venue**: ICLR 2026 Poster
- **Authors**: Yanping Li, Zhening Liu, Zijian Li, Zehong Lin, Jun Zhang
- **Keywords**: LLM, LLM safety
- **OpenReview**: https://openreview.net/forum?id=k7ytptAaDN
- **PDF**: https://openreview.net/pdf?id=k7ytptAaDN

**Abstract**

Fine-tuning large language models (LLMs) on custom datasets has become a standard approach for adapting these models to specific domains and applications. However, recent studies have shown that such fine-tuning can lead to significant degradation in the model's safety. Existing defense methods operate at the sample level and often suffer from an unsatisfactory trade-off between safety and utility. To address this limitation, we perform a systematic token-level diagnosis of safety degradation during fine-tuning. Based on this, we propose token-level data selection for safe LLM fine-tuning (TOSS), a novel framework that quantifies the safety risk of each token by measuring the loss difference between a safety-degraded model and a utility-oriented model. This token-level granularity enables accurate identification and removal of unsafe tokens, thereby preserving valuable task-specific information. In addition, we introduce a progressive refinement strategy, TOSS-Pro, which iteratively enhances the safety-degraded model's ability to identify unsafe tokens. Extensive experiments demonstrate that our approach robustly safeguards LLMs during fine-tuning while achieving superior downstream task performance, significantly outperforming existing sample-level defense methods. Our code is available at https://github.com/Polly-LYP/TOSS.

**Abstract (Chinese)**

在自定义数据集上微调大型语言模型 (LLMs) 已成为将这些模型适应特定领域和应用的标准化方法。然而，最近的研究表明，这种微调可能导致模型安全性的显著退化。现有的防御方法在样本级别操作，并且往往在安全性和效用之间存在不满意的权衡。为了解决这一局限性，我们对微调过程中安全性的退化进行了系统性的 token 级诊断。基于此，我们提出了用于安全 LLM 微调的 token 级数据选择 (TOSS)，这是一个新颖的框架，通过测量安全性退化模型和以效用为导向模型之间的损失差异来量化每个 token 的安全风险。这种 token 级粒度能够准确识别并移除不安全 token，从而保留宝贵的任务特定信息。此外，我们引入了渐进式精炼策略 TOSS-Pro，它迭代地增强安全性退化模型识别不安全 token 的能力。广泛的实验表明，我们的方法在微调过程中稳健地保护 LLMs，同时实现了优越的下游任务性能，显著优于现有的样本级防御方法。我们的代码可在 https://github.com/Polly-LYP/TOSS 获取。

---

### TrojanTO: Action-Level Backdoor Attacks Against Trajectory Optimization Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Yang Dai, Oubo Ma, Xingxing Liang, Longfei Zhang, Xiaochun Cao, Shouling Ji, Jiaheng Zhang, Jincai Huang, Li Shen
- **Keywords**: Backdoor attack, Decision Transformer, Offline RL
- **OpenReview**: https://openreview.net/forum?id=CNrU5kGJYG
- **PDF**: https://openreview.net/pdf?id=CNrU5kGJYG

**Abstract**

Trajectory Optimization (TO) models have achieved remarkable success in offline reinforcement learning (offline RL). However, their vulnerability to backdoor attacks remains largely unexplored. We find that existing backdoor attacks in RL, which typically rely on reward manipulation throughout training, are largely ineffective against TO models due to their inherent sequence modeling nature and large network size. Moreover, the complexities introduced by high-dimensional continuous action further compound the challenge of injecting effective backdoors. To address these gaps, we propose TrojanTO, the first action-level backdoor attack against TO models. TrojanTO is a post-training attack and employs alternating training to forge a strong connection between triggers and target actions, ensuring high attack effectiveness. To maintain attack stealthiness, it utilizes trajectory filtering to preserve the benign performance and batch poisoning for trigger consistency. Extensive evaluations demonstrate that TrojanTO effectively implants backdoors across diverse tasks and attack objectives with a low attack budget (0.3\% of trajectories). Furthermore, TrojanTO exhibits broad applicability to DT, GDT, and DC, underscoring its scalability across diverse TO model architectures.

**Abstract (Chinese)**

轨迹优化 (TO) 模型在离线强化学习 (offline RL) 中取得了显著成功。然而，它们对后门攻击的脆弱性仍未得到充分探索。我们发现，现有的 RL 中后门攻击通常依赖于整个训练过程中的奖励操纵，由于 TO 模型固有的序列建模特性和大型网络规模，这些攻击对 TO 模型基本无效。此外，高维连续动作引入的复杂性进一步加剧了注入有效后门的挑战。为填补这些空白，我们提出了 TrojanTO，这是针对 TO 模型的首个动作级后门攻击。TrojanTO 是一种后训练攻击，它采用交替训练来伪造触发器与目标动作之间的强连接，从而确保高攻击有效性。为保持攻击隐蔽性，它利用轨迹过滤来保留良性性能，并采用批次投毒来确保触发器一致性。广泛的评估表明，TrojanTO 以低攻击预算（轨迹的 0.3\%）在多样化任务和攻击目标中有效植入后门。此外，TrojanTO 对 DT、GDT 和 DC 表现出广泛适用性，突显了其在多样化 TO 模型架构中的可扩展性。

---

### Where Did It Go Wrong? Attributing Undesirable LLM Behaviors via Representation Gradient Tracing

- **Venue**: ICLR 2026 Poster
- **Authors**: Zhe Li, Wei Zhao, Yige Li, Jun Sun
- **Keywords**: Large Language Models, Data Attribution, Model Auditing
- **OpenReview**: https://openreview.net/forum?id=MN1qlAVJLV
- **PDF**: https://openreview.net/pdf?id=MN1qlAVJLV

**Abstract**

Large Language Models (LLMs) have demonstrated remarkable capabilities, yet their deployment is frequently undermined by undesirable behaviors such as generating harmful content, factual inaccuracies, and societal biases. Diagnosing the root causes of these failures poses a critical challenge for AI safety. Existing attribution methods, particularly those based on parameter gradients, often fall short due to prohibitive noisy signals and computational complexity. In this work, we introduce a novel and efficient framework that diagnoses a range of undesirable LLM behaviors by analyzing representation and its gradients, which operates directly in the model's activation space to provide a semantically meaningful signal linking outputs to their training data. We systematically evaluate our method for tasks that include tracking harmful content, detecting backdoor poisoning, and identifying knowledge contamination. The results demonstrate that our approach not only excels at sample-level attribution but also enables fine-grained token-level analysis, precisely identifying the specific samples and phrases that causally influence model behavior. This work provides a powerful diagnostic tool to understand, audit, and ultimately mitigate the risks associated with LLMs.

**Abstract (Chinese)**

大语言模型 (LLMs) 展现了卓越的能力，然而其部署常常受到有害内容生成、事实不准确以及社会偏见等不良行为的削弱。诊断这些失败的根本原因对 AI 安全构成了关键挑战。现有的归因方法，尤其是基于参数梯度的那些，往往因噪声信号过多和计算复杂度过高而失效。在本工作中，我们提出了一种新颖且高效的框架，通过分析表示及其梯度来诊断多种不良 LLM 行为，该框架直接在模型的激活空间中运行，提供将输出与训练数据联系起来的语义上有意义的信号。我们系统地评估了我们的方法在包括追踪有害内容、检测后门投毒以及识别知识污染等任务上的表现。结果表明，我们的方法不仅在样本级归因方面表现出色，还支持细粒度的令牌级分析，精确识别出因果影响模型行为的特定样本和短语。这项工作提供了一个强大的诊断工具，用于理解、审计并最终缓解与 LLMs 相关的风险。

---

### Winter Soldier: Backdooring Language Models at Pre-Training with Indirect Data Poisoning

- **Venue**: ICLR 2026 Poster
- **Authors**: Wassim Bouaziz, Mathurin VIDEAU, Nicolas Usunier, El-Mahdi El-Mhamdi
- **Keywords**: data poisoning, language model, ai security, dataset ownership verification, training data membership, privacy, copyright
- **OpenReview**: https://openreview.net/forum?id=ORKhJBFepG
- **PDF**: https://openreview.net/pdf?id=ORKhJBFepG

**Abstract**

The pre-training of large language models (LLMs) relies on massive text datasets sourced from diverse and difficult-to-curate origins.
Although membership inference attacks and hidden canaries have been explored to trace data usage, such methods rely on *regurgitation* of training data, which LM providers try to limit.
In this work, we demonstrate that *indirect data poisoning* (where the targeted behavior is absent from training data) is not only feasible against LLMs but also allows to effectively protect a dataset and trace its use.
Using gradient-based optimization prompt-tuning, we craft poisons to make a model learn arbitrary *secret sequences*: secret responses to secret prompts that are **absent from the training corpus**.\
We validate our approach on language models pre-trained from scratch and show that less than 0.005\% of poisoned tokens are sufficient to covertly make a LM learn a *secret* and detect it with extremely high confidence ( $p < 10^{-55}$ ) with a theoretically certifiable scheme.
Crucially, this occurs without performance degradation (on LM benchmarks) and despite secrets **never appearing in the training set**.

**Abstract (Chinese)**

大型语言模型（LLMs）的预训练依赖于来自多样且难以整理来源的海量文本数据集。尽管已经探索了成员推断攻击和隐藏金丝雀来追踪数据使用，但此类方法依赖于训练数据的 *regurgitation*，而语言模型提供商试图限制这种行为。在本工作中，我们证明了对 LLMs 的 *间接数据投毒*（其中目标行为在训练数据中不存在）不仅是可行的，而且能够有效保护数据集并追踪其使用。使用基于梯度的优化提示调优，我们设计了投毒样本，使模型学习任意 *秘密序列*：对训练语料库中 **不存在** 的秘密提示的秘密响应。我们在从头预训练的语言模型上验证了我们的方法，并证明少于 0.005% 的投毒令牌足以隐蔽地使语言模型学习一个 *秘密*，并使用理论上可证明的方案以极高置信度（$p < 10^{-55}$）检测它。至关重要的是，这不会导致性能退化（在语言模型基准测试上），尽管秘密 **从未出现在训练集中**。

---
