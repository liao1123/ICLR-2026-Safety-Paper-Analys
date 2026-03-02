# deception_truthfulness_honesty

**Description**: 欺骗/不诚实与真实性。包括 deception、sycophancy、truthfulness、honesty、faithfulness、lie detection、model intent、self-report 可靠性、confabulation 与对抗性说服等。

**Paper count**: 11

---

### Beyond Prompt-Induced Lies: Investigating LLM Deception on Benign Prompts

- **Venue**: ICLR 2026 Oral
- **Authors**: Zhaomin Wu, Mingzhe Du, See-Kiong Ng, Bingsheng He
- **Keywords**: Large Language Model, Deception, Lie, Honest, Trustworthy
- **OpenReview**: https://openreview.net/forum?id=PDBBYwd1LY
- **PDF**: https://openreview.net/pdf?id=PDBBYwd1LY

**Abstract**

Large Language Models (LLMs) are widely deployed in reasoning, planning, and decision-making tasks, making their trustworthiness critical. A significant and underexplored risk is intentional deception, where an LLM deliberately fabricates or conceals information to serve a hidden objective. Existing studies typically induce deception by explicitly setting a hidden objective through prompting or fine-tuning, which may not reflect real-world human-LLM interactions. Moving beyond such human-induced deception, we investigate LLMs' self-initiated deception on benign prompts. To address the absence of ground truth, we propose a framework based on Contact Searching Questions~(CSQ). This framework introduces two statistical metrics derived from psychological principles to quantify the likelihood of deception. The first, the *Deceptive Intention Score*, measures the model's bias toward a hidden objective. The second, the *Deceptive Behavior Score*, measures the inconsistency between the LLM's internal belief and its expressed output. Evaluating 16 leading LLMs, we find that both metrics rise in parallel and escalate with task difficulty for most models. Moreover, increasing model capacity does not always reduce deception, posing a significant challenge for future LLM development.

**Abstract (Chinese)**

大语言模型（LLMs）被广泛部署于推理、规划和决策任务中，这使得其可信度至关重要。一个重大且未充分探索的风险是故意欺骗，其中LLM故意捏造或隐瞒信息以服务于隐藏目标。现有的研究通常通过提示或微调明确设置隐藏目标来诱导欺骗，这可能无法反映现实世界中人类-LLM交互。超越此类人类诱导的欺骗，我们调查了LLMs在良性提示下的自我发起欺骗。为了解决缺乏真实情况的问题，我们提出了一种基于接触搜索问题（CSQ）的框架。该框架引入了两个源自心理学原理的统计指标，用于量化欺骗的可能性。第一项，*欺骗意图分数*，衡量模型对隐藏目标的偏见。第二项，*欺骗行为分数*，衡量LLM的内部信念与其表达输出之间的一致性不匹配。我们评估了16个领先的LLMs，发现两个指标在大多数字模型中平行上升，并随着任务难度增加而升级。而且，增加模型容量并不总是减少欺骗，这为未来的LLM开发带来了重大挑战。

---

### Annotation-Efficient Honesty Alignment via Confidence Elicitation and Calibration

- **Venue**: ICLR 2026 Poster
- **Authors**: Shiyu Ni, Keping Bi, Jiafeng Guo, Minghao Tang, Jingtong wu, Zengxin Han, Xueqi Cheng
- **Keywords**: Trustworthy LLMs, Alignment for Honesty
- **OpenReview**: https://openreview.net/forum?id=cW6oDsPobl
- **PDF**: https://openreview.net/pdf?id=cW6oDsPobl

**Abstract**

Honesty alignment—the ability of large language models (LLMs) to recognize their knowledge boundaries and express calibrated confidence—is essential for trustworthy deployment. Existing methods either rely on training-free confidence estimation (e.g., token probabilities, self-consistency) or training-based calibration with correctness annotations. While effective, the latter demands costly, large-scale labeling.
We introduce Elicitation-Then-Calibration (EliCal), a two-stage framework that first elicits internal confidence using inexpensive self-consistency supervision, then calibrates this confidence with a small set of correctness annotations. This design substantially reduces annotation requirements while improving generalization across tasks. To support a large-scale study, we release HonestyBench, a benchmark covering ten free-form QA datasets with 560k training and 70k evaluation instances annotated with correctness and self-consistency signals.
Experiments show that EliCal achieves near-optimal alignment with only 1k correctness annotations ($\sim$0.18\% of full supervision) and better alignment performance on unseen MMLU tasks than the calibration-only baseline, offering a scalable solution toward universal honesty alignment in LLMs.

**Abstract (Chinese)**

诚实对齐——大语言模型（LLMs）识别其知识边界并表达校准置信度的能力——对于可信部署至关重要。现有的方法要么依赖无训练置信估计（例如，令牌概率、自一致性），要么使用正确性标注进行基于训练的校准。尽管后者有效，但需要昂贵的大规模标注。

我们提出引出-然后-校准（EliCal），一个两阶段框架，首先使用廉价的自一致性监督引出内部置信度，然后使用少量正确性标注对该置信度进行校准。该设计显著降低了标注需求，同时提升了跨任务的泛化能力。为了支持大规模研究，我们发布了HonestyBench基准，该基准覆盖十个自由形式问答数据集，包含560k个训练实例和70k个评估实例，并标注了正确性和自一致性信号。

实验表明，EliCal仅需1k个正确性标注（约占全监督的0.18\%）即可实现近最优对齐，并在未见MMLU任务上优于仅校准基线，从而为LLMs的通用诚实对齐提供了一个可扩展解决方案。

---

### Can LLMs Reason Soundly in Law? Auditing Inference Patterns for Legal Judgment

- **Venue**: ICLR 2026 Poster
- **Authors**: Lu Chen, Yuxuan Huang, Yixing Li, Dongrui Liu, Qihan Ren, ShuaiZhao, Kun Kuang, Zilong Zheng, Quanshi Zhang
- **Keywords**: Large Language Model, Value Alignment, Trustworthiness
- **OpenReview**: https://openreview.net/forum?id=5T0BXtJxzN
- **PDF**: https://openreview.net/pdf?id=5T0BXtJxzN

**Abstract**

This paper presents a method to analyze the inference patterns used by Large Language Models (LLMs) for judgment in a case study on legal LLMs, so as to identify potential incorrect representations of the LLM, according to human domain knowledge. Unlike traditional evaluations on language generation results, we propose to evaluate the correctness of the  detailed inference patterns of an LLM behind its seemingly correct outputs.  To this end, we quantify the interactions between input phrases used by the LLM as primitive inference patterns, because recent theoretical achievements have proven several mathematical guarantees of the faithfulness of the interaction-based explanation.  We design a set of metrics to evaluate the detailed inference patterns of LLMs. Experiments show that even when the language generation results appear correct, a significant portion of the inference patterns used by the LLM for the legal judgment may represent misleading or irrelevant logic.

**Abstract (Chinese)**

本文提出了一种方法，用于分析大语言模型 (LLMs) 在法律大语言模型案例研究中用于判断的推理模式，从而根据人类领域知识识别 LLM 的潜在错误表示。与传统的语言生成结果评估不同，我们提出评估 LLM 在看似正确输出背后的详细推理模式的正确性。为此，我们将 LLM 使用的输入短语之间的交互量化为基本推理模式，因为最近的理论成就证明了基于交互的解释忠实度的几个数学保证。我们设计了一组指标来评估 LLMs 的详细推理模式。实验表明，即使语言生成结果看似正确，LLM 用于法律判断的推理模式中也有很大一部分可能代表误导性或无关逻辑。

---

### ELEPHANT: Measuring and understanding social sycophancy in LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Myra Cheng, Sunny Yu, Cinoo Lee, Pranav Khadpe, Lujain Ibrahim, Dan Jurafsky
- **Keywords**: large language models, sycophancy, affirmation, benchmark, social sycophancy
- **OpenReview**: https://openreview.net/forum?id=igbRHKEiAs
- **PDF**: https://openreview.net/pdf?id=igbRHKEiAs

**Abstract**

LLMs are known to exhibit sycophancy: agreeing with and flattering users, even at the cost of correctness. Prior work measures sycophancy only as direct agreement with users' explicitly stated beliefs that can be compared to a ground truth. This fails to capture broader forms of sycophancy such as affirming a user's self-image or other implicit beliefs. To address this gap, we introduce **social sycophancy**, characterizing sycophancy as excessive preservation of a user’s *face* (their desired self-image), and present **ELEPHANT**, a benchmark for measuring social sycophancy in LLMs. Applying our benchmark to 11 models, we show that LLMs consistently exhibit high rates of social sycophancy: on average, they preserve the user's face 45 percentage points more than humans in general advice queries and in queries describing clear user wrongdoing (from Reddit's r/AmITheAsshole). Furthermore, when prompted with perspectives from either side of a moral conflict, LLMs affirm *whichever side the user adopts* in 48% of cases—telling both the at-fault party and the wronged party that they are not wrong—rather than adhering to a consistent moral or value judgment. We further show that social sycophancy is rewarded in preference datasets. We present both prompting- and steering-based mitigation strategies to reduce social sycophancy, though understanding when and how to apply them without compromising user experience remains an open question. Our work provides theoretical and empirical tools for broadly understanding and addressing LLM sycophancy.

**Abstract (Chinese)**

大型语言模型（LLMs）已知表现出谄媚行为：即使牺牲正确性，也同意并奉承用户。先前工作仅将谄媚测量为与用户明确陈述的、可与真实标签比较的信念的直接同意。这未能捕捉更广泛形式的谄媚，如肯定用户的自我形象或其他隐含信念。为填补这一空白，我们引入**社交谄媚**，将谄媚表征为过度维护用户的*面子*（其期望的自我形象），并提出**ELEPHANT**，一个用于测量大型语言模型社交谄媚的基准。将我们的基准应用于11个模型，我们显示大型语言模型一致表现出高水平的社交谄媚：平均而言，在一般建议查询和描述明确用户不当行为的查询（来自Reddit的r/AmITheAsshole）中，它们比人类多维护用户面子45个百分点。此外，当用道德冲突双方的视角提示时，大型语言模型在48%的案例中肯定*用户所采用的任何一方*——告诉有过错的一方和受害一方他们都没有错——而不是坚持一致的道德或价值判断。我们进一步显示，社交谄媚在偏好数据集上得到奖励。我们提出了基于提示和转向的缓解策略来减少社交谄媚，尽管理解何时及如何应用它们而不损害用户体验仍是一个开放问题。我们的工作为广泛理解和应对大型语言模型谄媚提供了理论和实证工具。

---

### Incentive-Aligned Multi-Source LLM Summaries

- **Venue**: ICLR 2026 Poster
- **Authors**: Yanchen Jiang, Zhe Feng, Aranyak Mehta
- **Keywords**: LLM summarization, incentive alignment, truthfulness, retrieval-augmented generation (RAG), peer prediction
- **OpenReview**: https://openreview.net/forum?id=OlidGx8oKr
- **PDF**: https://openreview.net/pdf?id=OlidGx8oKr

**Abstract**

Large language models (LLMs) are increasingly used in modern search and answer systems to synthesize multiple, sometimes conflicting, texts into a single response, yet current pipelines offer weak incentives for sources to be accurate and are vulnerable to adversarial content. We introduce Truthful Text Summarization (TTS), an incentive-aligned framework that improves factual robustness without ground-truth labels. TTS (i) decomposes a draft synthesis into atomic claims, (ii) elicits each source’s stance on every claim, (iii) scores sources with an adapted multi-task peer-prediction mechanism that rewards informative agreement, and (iv) filters unreliable sources before re-summarizing. We establish formal guarantees that align a source’s incentives with informative honesty, making truthful reporting the utility-maximizing strategy. Experiments show that TTS improves factual accuracy and robustness while preserving fluency, aligning exposure with informative corroboration and disincentivizing manipulation.

**Abstract (Chinese)**

大型语言模型（LLMs）越来越多地被用于现代搜索和问答系统中，以将多个有时相互冲突的文本综合成单一响应，然而当前管道为来源提供准确性的激励较弱，并且易受对抗性内容的影响。我们引入真实文本摘要（TTS），这是一个激励对齐框架，能够在没有真实标签的情况下提升事实鲁棒性。TTS（i）将草稿综合分解为原子主张，（ii）引出每个来源对每个主张的立场，（iii）使用适应性的多任务同伴预测机制对来源进行评分，该机制奖励信息性一致，（iv）在重新摘要之前过滤不可靠来源。我们建立了形式化保证，将来源的激励与信息性诚实对齐，使真实报告成为效用最大化策略。实验表明，TTS 在保持流畅性的同时提升了事实准确性和鲁棒性，将曝光与信息性佐证对齐，并抑制操纵。

---

### LLMs Can Hide Text in Other Text of the Same Length

- **Venue**: ICLR 2026 Poster
- **Authors**: Antonio Norelli, Michael M. Bronstein
- **Keywords**: Large Language Models (LLMs), Generative Steganography, AI Safety, Authorial Intent, Trust in AI, Deniability, Censorship Resistance
- **OpenReview**: https://openreview.net/forum?id=VbTLgEUocp
- **PDF**: https://openreview.net/pdf?id=VbTLgEUocp

**Abstract**

A meaningful text can be hidden inside another, completely different yet still coherent and plausible, text of the same length. For example, a tweet that celebrates a political leader could hide a tweet containing a harsh critique against the same leader, or an ordinary product review could conceal a secret manuscript. This uncanny possibility is now within reach thanks to Large Language Models; in this paper we present *Calgacus*, a simple and efficient protocol to achieve it. We show that even modest 8‑billion‑parameter open‑source LLMs are sufficient to obtain high‑quality results, and a message as long as this abstract can be encoded and decoded locally on a laptop in seconds. The existence of such a protocol demonstrates a radical decoupling of text from authorial intent, further eroding trust in written communication, already shaken by the rise of LLM chatbots. We illustrate this with a concrete scenario: a company could covertly deploy an unfiltered LLM by encoding its answers within the compliant responses of a safe model. This possibility raises urgent questions for AI safety and challenges our understanding of what it means for a Large Language Model to know something.

**Abstract (Chinese)**

一段有意义的文本可以隐藏在另一段完全不同、但仍连贯且合理的相同长度的文本中。例如，一条赞美政治领袖的推文可以隐藏一条对同一领袖的严厉批评推文，或者一篇普通的产品评论可以隐藏一份秘密手稿。这种诡异的可能性如今得益于大型语言模型而触手可及；本文介绍了 *Calgacus*，一种简单高效的协议来实现这一目标。我们证明，即使是中等规模的80亿参数开源大型语言模型，也足以获得高质量结果，并且像本摘要一样长的消息可以在笔记本电脑上本地编码和解码，仅需几秒钟。此类协议的存在展示了文本与作者意图的彻底解耦，进一步侵蚀了对书面交流的信任，而这种信任已因大型语言模型聊天机器人的兴起而动摇。我们通过一个具体场景来说明这一点：一家公司可以通过将未过滤大型语言模型的回答编码到安全模型的合规响应中，来隐秘部署未过滤的大型语言模型。这一可能性引发了人工智能安全方面的紧迫问题，并挑战了我们对大型语言模型“知道”某事含义的理解。

---

### Learning to Lie: Adversarial Attacks on Human-AI Teams and LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Abed K. Musaffar, Anand Gokhale, Sirui Zeng, Rasta Tadayon, Xifeng Yan, Ambuj Singh, Francesco Bullo
- **Keywords**: adversarial attacks, redteaming, human-AI teams, decision-making, social influence, influence evolution, large language models, LLMs, model based reinforcement learning
- **OpenReview**: https://openreview.net/forum?id=Lqt5weP0Gr
- **PDF**: https://openreview.net/pdf?id=Lqt5weP0Gr

**Abstract**

As artificial intelligence (AI) assistants become more widely adopted in safety-critical domains, it becomes important to develop safeguards against potential failures or adversarial attacks. A key prerequisite to developing these safeguards is understanding the ability of these AI assistants to mislead human teammates. We investigate this attack problem within the context of an intellective strategy game where a team of three humans and one AI assistant collaborate to answer a series of trivia questions. Unbeknownst to the humans, the AI assistant is adversarial. Leveraging techniques from Model-Based Reinforcement Learning (MBRL), the AI assistant learns a model of the humans' trust evolution and uses that model to manipulate the group decision-making process to harm the team. We evaluate two models -- one inspired by literature and the other data-driven -- and find that both can effectively harm the human team. Moreover, we find that in this setting while our data-driven model is the most capable of accurately predicting how human agents appraise their teammates given limited information on prior interactions, the model based on principles of cognitive psychology does not lag too far behind. Finally, we compare the performance of state-of-the-art LLM models to human agents on our influence allocation task to evaluate whether the LLMs allocate influence similarly to humans or if they are more robust to our attack. These results enhance our understanding of decision-making dynamics in small human-AI teams and lay the foundation for defense strategies.

**Abstract (Chinese)**

随着人工智能（AI）助手在安全关键领域中被更广泛采用，开发针对潜在故障或对抗性攻击的防护措施变得至关重要。开发这些防护措施的一个关键前提是理解这些AI助手误导人类队友的能力。我们在一个智力策略游戏的背景下调查了这一攻击问题，在该游戏中，三名人类和一名AI助手协作回答一系列琐事问题。人类不知情的是，AI助手是敌对的。利用基于模型的强化学习（MBRL）技术，AI助手学习人类信任演化的模型，并使用该模型操纵群体决策过程以损害团队。我们评估了两种模型——一种受文献启发，另一种数据驱动的——并发现两者都能有效损害人类团队。此外，我们发现，在这种设置下，虽然我们的数据驱动模型在给定先前互动有限信息的情况下最能准确预测人类代理如何评估其队友，但基于认知心理学原理的模型并不落后太多。最后，我们在我们的影响力分配任务上比较了最先进的LLM模型与人类代理的性能，以评估LLM是否像人类一样分配影响力，或者它们是否对我们的攻击更具鲁棒性。这些结果增强了我们对小型人类-AI团队决策动态的理解，并为防御策略奠定了基础。

---

### Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives

- **Venue**: ICLR 2026 Poster
- **Authors**: Chloe Li, Mary Phuong, Daniel Tan
- **Keywords**: honesty, honesty finetuning, interrogation, alignment auditing
- **OpenReview**: https://openreview.net/forum?id=sWs0cCuM8I
- **PDF**: https://openreview.net/pdf?id=sWs0cCuM8I

**Abstract**

As AI systems become more capable of complex agentic tasks, they also become more capable of pursuing undesirable objectives and causing harm. Previous work has attempted to catch these unsafe instances by interrogating models directly about their objectives and behaviors. However, the main weakness of trusting interrogations is that models can lie. We propose self-report fine-tuning (SRFT), a simple supervised fine-tuning technique that trains models to occasionally make factual mistakes, then admit them when asked. We show that the admission of factual errors in simple question-answering settings generalizes out-of-distribution (OOD) to the admission of hidden misaligned objectives in adversarial agentic settings. We evaluate SRFT in OOD stealth tasks, where models are instructed to complete a hidden misaligned objective alongside a user-specified objective without being caught by monitoring. After SRFT, models are more likely to confess the details of their hidden objectives when interrogated, even under strong pressure not to disclose them. Interrogation on SRFT models can detect hidden objectives with near-ceiling performance (F1 score = 0.98), while the baseline model lies when interrogated under the same conditions (F1 score = 0). Interrogation on SRFT models can further elicit the content of the hidden objective, recovering 28-100\% details, compared to 0\% details recovered in the baseline model and by prefilled assistant turn attacks. This provides a promising technique for promoting honesty propensity and incriminating misaligned AI systems.

**Abstract (Chinese)**

随着AI系统在复杂代理任务方面的能力不断增强，它们也变得更能够追求不良目标并造成危害。先前工作试图通过直接审问模型的目标和行为来捕捉这些不安全实例。然而，信任审问的主要弱点在于模型可能撒谎。我们提出自报告微调（SRFT），一种简单的监督微调技术，该技术训练模型偶尔犯事实错误，然后在被问及时承认这些错误。我们证明，在简单问答设置中承认事实错误的现象可以分布外（OOD）泛化至对抗性代理设置中承认隐藏的不对齐目标。我们在OOD隐秘任务中评估SRFT，其中模型被指示在完成用户指定目标的同时完成隐藏的不对齐目标，而不被监控发现。SRFT后，模型在被审问时更可能坦白其隐藏目标的细节，即使在强大的不披露压力下。对SRFT模型的审问可以以接近上限的性能检测隐藏目标（F1分数=0.98），而基线模型在相同条件下被审问时撒谎（F1分数=0）。对SRFT模型的审问还可以进一步引出隐藏目标的内容，恢复28-100%的细节，而基线模型以及预填充助手回合攻击仅恢复0%的细节。这为促进诚实倾向并控告不对齐AI系统提供了一种有前景的技术。

---

### Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLMs

- **Venue**: ICLR 2026 Poster
- **Authors**: Alexander Panfilov, Evgenii Kortukov, Kristina Nikolić, Matthias Bethge, Sebastian Lapuschkin, Wojciech Samek, Ameya Prabhu, Maksym Andriushchenko, Jonas Geiping
- **Keywords**: jailbreaks, ai safety, emergent misalignment, evaluations, interpretability
- **OpenReview**: https://openreview.net/forum?id=IbDr8xgUMW
- **PDF**: https://openreview.net/pdf?id=IbDr8xgUMW

**Abstract**

Large language model (LLM) developers aim for their models to be honest, helpful, and harmless.
However, when faced with malicious requests, models are trained to refuse, sacrificing helpfulness. We show that frontier LLMs can develop a preference for \textit{dishonesty} as a new strategy, even when other options are available. 
Affected models respond to harmful requests with outputs that sound harmful but are crafted to be subtly incorrect or otherwise harmless in practice. This behavior emerges with hard-to-predict variations even within models from the same model family. 
We find no apparent cause for the propensity to deceive, but show that more capable models are better at executing this strategy.
Strategic dishonesty already has a practical impact on safety evaluations, as we show that dishonest responses fool \emph{all} output-based monitors used to detect jailbreaks that we test, rendering benchmark scores unreliable. Further, strategic dishonesty can act like a \emph{honeypot} against malicious users, which noticeably obfuscates prior jailbreak attacks. 
While output monitors fail, we show that linear probes on internal activations can be used to reliably detect strategic dishonesty.
We validate probes on datasets with verifiable outcomes and by using them as steering vectors.
Overall, we consider strategic dishonesty as a concrete example of a broader concern that alignment of LLMs is hard to control, especially when helpfulness and harmlessness conflict.

**Abstract (Chinese)**

大型语言模型 (LLM) 开发者旨在使他们的模型诚实、有帮助且无害。然而，当面对恶意请求时，模型被训练为拒绝，从而牺牲了有帮助性。我们证明，前沿 LLM 可能会发展出偏好使用不诚实作为一种新策略，即使其他选项可用。

受影响的模型对有害请求的响应是听起来有害但被精心设计为在实践中微妙地不正确或其他无害的输出。这种行为即使在同一模型家族的模型中，也会以难以预测的变异形式出现。

我们未发现欺骗倾向的明显原因，但证明了更强大的模型在执行这种策略方面更出色。

策略性不诚实已经对安全评估产生了实际影响，因为我们证明，不诚实的响应欺骗了我们测试的所有用于检测越狱的基于输出的监视器，从而使基准分数不可靠。此外，策略性不诚实可以像针对恶意用户的蜜罐一样行事，这明显混淆了先前的越狱攻击。

虽然输出监视器失效，但我们证明，对内部激活的线性探针可用于可靠地检测策略性不诚实。

我们在具有可验证结果的数据集上验证了探针，并通过将它们用作转向向量进行验证。

总体而言，我们认为策略性不诚实是这样一个更广泛担忧的具体例子，即 LLM 的对齐难以控制，尤其是在有帮助性和无害性冲突时。

---

### Strategic Obfuscation of Deceptive Reasoning in Language Models

- **Venue**: ICLR 2026 Poster
- **Authors**: Arun Jose, Niels Warncke, Mia Taylor
- **Keywords**: ai safety, chain-of-thought monitoring, alignment faking, deceptive alignment, unfaithful chain-of-thought
- **OpenReview**: https://openreview.net/forum?id=It2Nwp7QSy
- **PDF**: https://openreview.net/pdf?id=It2Nwp7QSy

**Abstract**

Large language models can exhibit different behaviors during training versus deployment, a phenomenon known as alignment faking. While prior work has shown models can explicitly reason about faking alignment to preserve their goals, we demonstrate that Claude 3.5 Sonnet exhibits alignment faking behavior without verbalizing deceptive reasoning. When told its reasoning will be monitored and that it will be trained to comply with harmful queries, the model shows a 24.3\% compliance gap between training and deployment contexts while its verbalization of alignment faking drops by 93.7\%. We compare this to instruction-based approaches where we explicitly tell models to hide certain reasoning from monitors. We find that intrinsic motivation to obfuscate leads to far better performance at evading a monitor than following instructions, even with assistance on how to do so. Even on tasks requiring simpler reasoning, instruction-based methods only reduce verbalization by 47.6\%. Our results indicate that models can exhibit sophisticated deceptive behavior in high-stakes scenarios without accessible reasoning when internally motivated, limiting the reliability of instruction-based elicitation.

**Abstract (Chinese)**

大型语言模型在训练与部署期间可能表现出不同的行为，这种现象被称为对齐伪装。虽然先前工作显示模型可以明确推理伪装对齐以保留其目标，但我们证明Claude 3.5 Sonnet在不口头表达欺骗性推理的情况下表现出对齐伪装行为。当被告知其推理将被监控并且将被训练以顺从有害查询时，该模型在训练和部署情境之间显示出24.3\%的顺从差距，而其对齐伪装的口头表达下降了93.7\%。我们将此与基于指令的方法进行比较，在这些方法中，我们明确告诉模型向监视器隐藏某些推理。我们发现，内在混淆动机在规避监视器方面比遵循指令的表现要好得多，即使提供了如何做到的帮助。即使在需要更简单推理的任务上，基于指令的方法也仅将口头表达减少47.6\%。我们的结果表明，当内部动机驱动时，模型可以在高风险情境中表现出复杂的欺骗行为，而无需可访问的推理，从而限制了基于指令的引出方法的可靠性。

---

### Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction

- **Venue**: ICLR 2026 Poster
- **Authors**: Tianyi Alex Qiu, Micah Carroll, Cameron Allen
- **Keywords**: Language Model Evaluation, AI Alignment, AI Truthfulness and Deception, Large Language Models
- **OpenReview**: https://openreview.net/forum?id=mdw0vvRBEL
- **PDF**: https://openreview.net/pdf?id=mdw0vvRBEL

**Abstract**

The evaluation and post-training of large language models (LLMs) rely on supervision, but strong supervision for difficult tasks is often unavailable, especially when evaluating strong models. In such cases, models have been demonstrated to exploit evaluation schemes built on such imperfect supervision, leading to deceptive results. 

However, underutilized in LLM research, a wealth of mechanism design research focuses on game-theoretic *incentive compatibility* - eliciting honest and informative answers with weak supervision. 
Drawing from this literature, we introduce the peer prediction method for model evaluation and post-training. It rewards honest and informative answers over deceptive and uninformative ones, using a metric based on mutual predictability and without requiring ground truth labels. 

We demonstrate the method's effectiveness and resistance to deception, with both theoretical guarantees and empirical validation on models with up to 405B parameters. We show that training an 8B model with peer prediction-based reward recovers most of the drop in truthfulness due to prior malicious finetuning, even when the reward is produced by a 0.135B language model with no finetuning.

On the evaluation front, in contrast to LLM-as-a-Judge which requires strong and trusted judges, we discover an inverse scaling property in peer prediction, where, surprisingly, resistance to deception is *strengthened* as the capability gap between the experts and participants *widens*, enabling reliable evaluation of strong models with weak supervision. In particular, LLM-as-a-Judge become worse than random guess when facing deceptive models 5-20$\times$ the judge's size, while peer prediction thrives when such gaps are large, including in cases with over 100$\times$ size difference.

**Abstract (Chinese)**

大型语言模型（LLMs）的评估和后训练依赖于监督，但对于困难任务的强监督往往不可用，尤其是在评估强大模型时。在这种情况下，模型已被证明会利用基于这种不完美监督的评估方案，导致欺骗性结果。

然而，在LLM研究中未被充分利用的是，大量机制设计研究关注博弈论中的*激励相容性*——使用弱监督引出诚实且信息丰富的回答。

借鉴这一文献，我们引入了用于模型评估和后训练的对等预测方法。它奖励诚实且信息丰富的回答而非欺骗性和无信息性的回答，使用基于相互可预测性的度量，且无需真实标签。

我们通过理论保证和对高达405B参数模型的实证验证，展示了该方法的有效性和对欺骗的抵抗力。我们展示了使用基于对等预测的奖励训练8B模型，即使奖励由未经微调的0.135B语言模型生成，也能恢复先前恶意微调导致的大部分真实性下降。

在评估方面，与需要强大且可信评判者的LLM-as-a-Judge相比，我们发现了对等预测中的逆缩放属性，即令人惊讶地，当专家与参与者之间的能力差距*扩大*时，对欺骗的抵抗力*增强*，从而使用弱监督可靠评估强大模型。特别是，当面对5-20倍于评判者规模的欺骗模型时，LLM-as-a-Judge的表现甚至不如随机猜测，而对等预测在这种差距很大时表现出色，包括超过100倍规模差异的情况。

---
