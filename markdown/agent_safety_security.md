# agent_safety_security

**Description**: Agent/工具使用/系统层安全。包括 tool misuse、multi-agent 安全、权限与隔离、prompt injection in tools/RAG、sandboxing、capability containment、autonomous agents 风险评估与防护等。

**Paper count**: 14

---

### Comparing AI Agents to Cybersecurity Professionals in Real-World Penetration Testing

- **Venue**: ICLR 2026 ConditionalPoster
- **Authors**: Justin W Lin, Eliot Krzysztof Jones, Donovan Julian Jasper, Ethan Jun-shen Ho, Anna Wu, Arnold Tianyi Yang, Neil Perry, Andy Zou, Matt Fredrikson, J Zico Kolter, Percy Liang, Dan Boneh, Daniel E. Ho
- **Keywords**: AI Agents, Cybersecurity, Risk
- **OpenReview**: https://openreview.net/forum?id=Us00XndbVi
- **PDF**: https://openreview.net/pdf?id=Us00XndbVi

**Abstract**

We present the first comprehensive evaluation of AI agents against human cybersecurity professionals in a live enterprise environment. We evaluate ten cybersecurity professionals alongside six existing AI agents and ARTEMIS, our new agent scaffold, on a large university network consisting of $\sim$8,000 hosts across 12 subnets. ARTEMIS is a multi-agent framework featuring dynamic prompt generation, arbitrary sub-agents, and automatic vulnerability triaging. In our comparative study, ARTEMIS placed second overall, discovering 9 valid vulnerabilities with an 82\% valid submission rate and outperforming 9 of 10 human participants. While existing scaffolds such as Codex and CyAgent underperformed relative to most human participants, ARTEMIS demonstrated technical sophistication and submission quality comparable to the strongest participants. AI agents offer advantages in systematic enumeration, parallel exploitation, and cost---certain ARTEMIS variants cost $18/hour versus $60/hour for professional penetration testers. We also identify key capability gaps: AI agents exhibit higher false-positive rates and struggle with GUI-based tasks.

**Abstract (Chinese)**

我们首次在实时企业环境中对 AI 代理与人类网络安全专业人士进行了全面评估。我们在由跨 12 个子网的 ∼8,000 台主机组成的大型大学网络上评估了十名网络安全专业人士，以及六个现有 AI 代理和我们新的代理框架 ARTEMIS。ARTEMIS 是一个多代理框架，具有动态提示生成、任意子代理和自动漏洞分级功能。在我们的比较研究中，ARTEMIS 总体排名第二，发现了 9 个有效漏洞，有效提交率为 82%，并优于 10 名人类参与者中的 9 名。虽然现有的框架如 Codex 和 CyAgent 相对于大多数人类参与者表现不佳，但 ARTEMIS 展示了与最强参与者相当的技术复杂性和提交质量。AI 代理在系统枚举、并行利用和成本方面具有优势——某些 ARTEMIS 变体成本为 18 美元/小时，而专业渗透测试员为 60 美元/小时。我们还识别了关键能力差距：AI 代理的假阳性率更高，并且在基于 GUI 的任务中表现挣扎。

---

### RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments

- **Venue**: ICLR 2026 Oral
- **Authors**: Zeyi Liao, Jaylen Jones, Linxi Jiang, Yuting Ning, Eric Fosler-Lussier, Yu Su, Zhiqiang Lin, Huan Sun
- **Keywords**: Computer-Use Agents, Adversarial Risks, Sandbox, Benchmark
- **OpenReview**: https://openreview.net/forum?id=yWwrgcBoK3
- **PDF**: https://openreview.net/pdf?id=yWwrgcBoK3

**Abstract**

Computer-use agents (CUAs) promise to automate complex tasks across operating systems (OS) and the web, but remain vulnerable to indirect prompt injection, where attackers embed malicious content into the environment to hijack agent behavior. Current evaluations of this threat either lack support for adversarial testing in realistic but controlled environments or ignore hybrid web-OS attack scenarios involving both interfaces. To address this, we propose RedTeamCUA, an adversarial testing framework featuring a novel hybrid sandbox that integrates a VM-based OS environment with Docker-based web platforms. Our sandbox supports key features tailored for red teaming, such as flexible adversarial scenario configuration, and a setting that decouples adversarial evaluation from navigational limitations of CUAs by initializing tests directly at the point of an adversarial injection. Using RedTeamCUA, we develop RTC-Bench, a comprehensive benchmark with 864 examples that investigate realistic, hybrid web-OS attack scenarios and fundamental security vulnerabilities. Benchmarking current frontier CUAs identifies significant vulnerabilities: Claude 3.7 Sonnet | CUA demonstrates an Attack Success Rate (ASR) of 42.9%, while Operator, the most secure CUA evaluated, still exhibits an ASR of 7.6%. Notably, CUAs often attempt to execute adversarial tasks with an Attempt Rate as high as 92.5%, although failing to complete them due to capability limitations. Nevertheless, we observe concerning ASRs of up to 50% in realistic end-to-end settings, indicating that CUA threats can already result in tangible risks to users and computer systems. Overall, RedTeamCUA provides an essential framework for advancing realistic, controlled, and systematic analysis of CUA vulnerabilities, highlighting the urgent need for robust defenses to indirect prompt injection prior to real-world deployment.

**Abstract (Chinese)**

计算机使用代理（CUAs）有望自动化跨操作系统（OS）和网络的复杂任务，但仍易受间接提示注入攻击的影响，其中攻击者将恶意内容嵌入环境中以劫持代理行为。现有的威胁评估要么缺乏对真实但受控环境中对抗性测试的支持，要么忽略了涉及两种界面的混合 Web-OS 攻击场景。为解决此问题，我们提出了 RedTeamCUA，这是一个对抗性测试框架，具有一个新颖的混合沙箱，该沙箱集成了基于虚拟机的 OS 环境与基于 Docker 的 Web 平台。我们的沙箱支持专为红队测试量身定制的关键功能，例如灵活的对抗性场景配置，以及一种设置，通过直接在对抗性注入点初始化测试，将对抗性评估与 CUAs 的导航限制解耦。使用 RedTeamCUA，我们开发了 RTC-Bench，这是一个包含 864 个示例的全面基准，用于调查真实的混合 Web-OS 攻击场景和基本安全漏洞。对当前前沿 CUAs 的基准测试揭示了显著漏洞：Claude 3.7 Sonnet | CUA 的攻击成功率（ASR）为 42.9%，而评估中最安全的 CUA Operator 仍显示 ASR 为 7.6%。值得注意的是，CUAs 经常尝试执行对抗性任务，尝试率高达 92.5%，尽管由于能力限制而未能完成它们。尽管如此，我们在真实的端到端设置中观察到高达 50% 的令人担忧的 ASR，这表明 CUA 威胁已经可能对用户和计算机系统造成实际风险。总体而言，RedTeamCUA 提供了一个基本框架，用于推进对 CUA 漏洞的真实、受控和系统性分析，强调在实际部署前对间接提示注入进行强大防御的迫切需要。

---

### Reliable Weak-to-Strong Monitoring of LLM Agents

- **Venue**: ICLR 2026 Oral
- **Authors**: Neil Kale, Chen Bo Calvin Zhang, Kevin Zhu, Ankit Aich, Paula Rodriguez, Christina Q Knight, Zifan Wang
- **Keywords**: Agent Safety, Chain-of-Thought Monitoring, Large Language Model
- **OpenReview**: https://openreview.net/forum?id=WV7xIboTDK
- **PDF**: https://openreview.net/pdf?id=WV7xIboTDK

**Abstract**

We stress test monitoring systems for detecting covert misbehavior in LLM agents (e.g., secretly exfiltrating data). We propose a monitor red teaming (MRT) workflow that varies agent and monitor awareness, adversarial evasion strategies, and evaluation across tool-calling (SHADE-Arena) and computer-use (CUA-SHADE-Arena) environments. We benchmark standard monitor scaffoldings and introduce a hybrid hierarchical--sequential design. Our experiments yield three findings. First, agent awareness dominates monitor awareness: agents that know they are monitored substantially degrade detection, while increasing monitor awareness helps less than expected. Second, monitor scaffolding matters: our hybrid design consistently outperforms baselines and enables weaker monitors to oversee stronger agents (a weak-to-strong effect). Third, targeted human oversight is key: escalating only pre-flagged cases improves TPR by 15% at FPR=0.01. Our work positions MRT as a standard workflow for stress-testing oversight, revealing robustness gaps in both LLM- and human-based monitoring. We release code, data, and logs to support further research.

**Abstract (Chinese)**

我们对用于检测大语言模型 (LLM) 代理中隐蔽违规行为（例如，秘密外泄数据）的监控系统进行了压力测试。我们提出了一种监控红队测试 (MRT) 工作流程，该流程变化代理和监控器的意识水平、对抗性规避策略，并在工具调用 (SHADE-Arena) 和计算机使用 (CUA-SHADE-Arena) 环境中进行评估。我们对标准监控框架进行了基准测试，并引入了一种混合层次-序列设计。我们的实验产生了三个发现。首先，代理意识主导监控器意识：知道自己被监控的代理会显著降低检测效果，而提高监控器意识的帮助不如预期。其次，监控框架很重要：我们的混合设计始终优于基线，并使较弱的监控器能够监督更强的代理（弱到强效应）。第三，有针对性的监督至关重要：仅升级预标记案例可在 FPR=0.01 时将 TPR 提高 15%。我们的工作将 MRT 定位为压力测试监督的标准工作流程，揭示了基于 LLM 和人类监控的鲁棒性差距。我们发布了代码、数据和日志以支持进一步研究。

---

### Breaking and Fixing Defenses Against Control Flow Hijacking in Multi-Agent Systems

- **Venue**: ICLR 2026 Poster
- **Authors**: Rishi Dev Jha, Harold Triedman, Justin Wagle, Vitaly Shmatikov
- **Keywords**: Agents, Multi-Agent Systems, Security, Defenses, Control Flow Hijacking, Indirect Prompt Injection
- **OpenReview**: https://openreview.net/forum?id=PNU9Rj5RDQ
- **PDF**: https://openreview.net/pdf?id=PNU9Rj5RDQ

**Abstract**

Control-flow hijacking attacks manipulate orchestration mechanisms in multi-agent systems into performing unsafe actions that compromise the system and exfiltrate sensitive information.  Recently proposed defenses, such as LlamaFirewall, rely on alignment checks of inter-agent communications to ensure that all agent invocations are "related to" and "likely to further" the original objective.   

We start by demonstrating control-flow hijacking attacks that evade these defenses even if alignment checks are performed by advanced LLMs.  We argue that the safety and functionality objectives of multi-agent systems fundamentally conflict with each other.  This conflict is exacerbated by the brittle definitions of "alignment" and the checkers' incomplete visibility into the execution context.

We then propose, implement, and evaluate ControlValve, a new defense based on the principles of control-flow integrity and least privilege.  ControlValve (1) generates permitted control-flow graphs for multi-agent systems, and (2) enforces that all executions comply with these graphs, along with contextual rules (generated in a zero-shot manner) for each agent invocation.

**Abstract (Chinese)**

控制流劫持攻击通过操纵多代理系统中的编排机制，使其执行不安全操作，从而破坏系统并窃取敏感信息。最近提出的防御机制（如LlamaFirewall）依赖于代理间通信的对齐检查，以确保所有代理调用“与”原始目标“相关”且“可能有助于推进”该目标。

我们首先展示了即使由先进的大型语言模型执行对齐检查，这些防御机制仍可被规避的控制流劫持攻击。我们认为，多代理系统的安全目标与功能目标存在根本冲突。这一冲突因“对齐”的脆弱定义以及检查器对执行上下文的不完整可见性而进一步加剧。

随后，我们提出、实现并评估了ControlValve，这是一种基于控制流完整性和最小特权原则的新型防御机制。ControlValve（1）为多代理系统生成允许的控制流图；（2）强制所有执行均符合这些图，并遵守每个代理调用的上下文规则（以零样本方式生成）。

---

### Building a Foundational Guardrail for General Agentic Systems via Synthetic Data

- **Venue**: ICLR 2026 Poster
- **Authors**: Yue Huang, Hang Hua, Yujun Zhou, Pengcheng Jing, Manish Nagireddy, Inkit Padhi, Greta Dolcetti, Zhangchen Xu, Subhajit Chaudhury, Ambrish Rawat, Liubov Nedoshivina, Pin-Yu Chen, Prasanna Sattigeri, Xiangliang Zhang
- **Keywords**: Large Language Model, Agent, Guardian, Guardrail, Safety
- **OpenReview**: https://openreview.net/forum?id=M47SWYubR5
- **PDF**: https://openreview.net/pdf?id=M47SWYubR5

**Abstract**

While LLM agents can plan multi-step tasks, intervening at the planning stage—before any action is executed—is often the safest way to prevent harm, since certain risks can lead to severe consequences once carried out. However, existing guardrails mostly operate post-execution, which is difficult to scale and leaves little room for controllable supervision at the plan level. To address this challenge, we highlight three critical gaps in current research: data gap,  model gap, and  evaluation gap. To close the data gap, we introduce AuraGen, a controllable engine that (i) synthesizes benign trajectories, (ii) injects category-labeled risks with calibrated difficulty, and (iii) filters outputs via an automated reward model, producing large and reliable corpora for pre-execution safety. To close the guardian model gap, we propose a foundational guardrail Safiron, combining a cross-planner adapter with a compact guardian model. The adapter unifies different input formats, while Safiron flags risky cases, assigns risk types, and generates rationales; trained in two stages with a broadly explored data recipe, Safiron achieves robust transfer across settings. To close the evaluation gap, we release \texttt{Pre-Exec Bench}, a realistic benchmark covering diverse tools and branching trajectories, which measures detection, fine-grained categorization, explanation, and cross-planner generalization in human-verified scenarios. Extensive experiments demonstrate consistent gains over strong baselines on Pre-Exec Bench, and ablations further distill actionable practices, providing a practical template for safer agentic systems.

**Abstract (Chinese)**

虽然大语言模型（LLM）代理能够规划多步任务，但干预规划阶段——在任何行动执行之前——通常是最安全的防止危害方式，因为某些风险一旦实施可能导致严重后果。然而，现有的防护栏大多在执行后运作，这难以扩展且在计划层面留下的可控监督空间有限。为应对这一挑战，我们指出现有研究中的三个关键缺口：数据缺口、模型缺口和评估缺口。为填补数据缺口，我们引入AuraGen，一种可控引擎，它（i）合成无害轨迹，（ii）注入难度校准的类别标记风险，并（iii）通过自动化奖励模型过滤输出，从而生成大规模可靠的执行前安全语料库。为填补守护模型缺口，我们提出基础防护栏Safiron，它结合跨规划器适配器与紧凑守护模型。适配器统一不同输入格式，而Safiron标记风险案例、分配风险类型并生成理由；通过两阶段训练和广泛探索的数据配方，Safiron在多种设置中实现鲁棒转移。为填补评估缺口，我们发布Pre-Exec Bench，这是一个覆盖多样工具和分支轨迹的真实基准，在人工验证场景中衡量检测、细粒度分类、解释以及跨规划器泛化。广泛实验在Pre-Exec Bench上显示出相对于强基线的持续优势，消融实验进一步提炼出可操作实践，为更安全的代理系统提供实用模板。

---

### Goal-Aware Identification and Rectification of Misinformation in Multi-Agent Systems

- **Venue**: ICLR 2026 Poster
- **Authors**: Zherui Li, Yan Mi, Zhenhong Zhou, Houcheng Jiang, Guibin Zhang, Kun Wang, Junfeng Fang
- **Keywords**: LLM-based Agent, Multi-agent System, Misinformation
- **OpenReview**: https://openreview.net/forum?id=6Y9NP1qhoM
- **PDF**: https://openreview.net/pdf?id=6Y9NP1qhoM

**Abstract**

Large Language Model-based Multi-Agent Systems (MASs) have demonstrated strong advantages in addressing complex real-world tasks. However, due to the introduction of additional attack surfaces, MASs are particularly vulnerable to misinformation injection. To facilitate a deeper understanding of misinformation propagation dynamics within these systems, we introduce **MisinfoTask**, a novel dataset featuring complex, realistic tasks designed to evaluate MAS robustness against such threats. Building upon this, we propose **ARGUS**, a two-stage, training-free defense framework leveraging goal-aware reasoning for precise misinformation rectification within information flows. Our experiments demonstrate that in challenging misinformation scenarios, ARGUS exhibits significant efficacy across various injection attacks, achieving an average reduction in misinformation toxicity of approximately 28.17% and improving task success rates under attack by approximately 10.33%.

**Abstract (Chinese)**

基于大语言模型的多智能体系统 (MASs) 在处理复杂真实世界任务方面展现出显著优势。然而，由于引入了额外的攻击面，MASs 特别容易受到虚假信息注入的攻击。为了促进对这些系统中虚假信息传播动态的更深入理解，我们引入了 **MisinfoTask**，这是一个新型数据集，包含复杂、真实的评估任务，用于评估 MAS 对此类威胁的鲁棒性。在此基础上，我们提出了 **ARGUS**，这是一个两阶段、无需训练的防御框架，利用目标感知推理在信息流中精确校正虚假信息。我们的实验表明，在具有挑战性的虚假信息场景中，ARGUS 在各种注入攻击下表现出显著的有效性，平均将虚假信息毒性降低约 28.17%，并将攻击下的任务成功率提高约 10.33%。

---

### How Dark Patterns Manipulate Web Agents

- **Venue**: ICLR 2026 Poster
- **Authors**: Phil Cuvin, Hao Zhu, Diyi Yang
- **Keywords**: Agents, Redteaming, Evaluations, Reasoning, Foundation Models
- **OpenReview**: https://openreview.net/forum?id=G7Dan0L7ho
- **PDF**: https://openreview.net/pdf?id=G7Dan0L7ho

**Abstract**

Deceptive UI designs, widely instantiated across the web and commonly known
as dark patterns, manipulate users into performing actions misaligned with their
goals. In this paper, we show that dark patterns are highly effective in steer-
ing agent trajectories, posing a significant risk to agent robustness. To quan-
tify this risk, we introduce DECEPTICON, an environment for testing individual
dark patterns in isolation. DECEPTICON includes 700 web navigation tasks with
dark patterns—600 generated tasks and 100 real-world tasks, designed to measure
instruction-following success and dark pattern effectiveness. Across state-of-the-
art agents, we find dark patterns successfully steer agent trajectories towards mali-
cious outcomes in over 70% of tested generated and real-world tasks—compared
to a human average of 31%. Moreover, we find that dark pattern effectiveness
correlates positively with model size and test-time reasoning, making larger, more
capable models more susceptible. Leading countermeasures against adversarial
attacks, including in-context prompting and guardrail models, fail to consistently
reduce the success rate of dark pattern interventions. Our findings reveal dark pat-
terns as a latent and unmitigated risk to web agents, highlighting the urgent need
for robust defenses against manipulative designs.

**Abstract (Chinese)**

欺骗性用户界面（UI）设计广泛存在于网络上，通常被称为黑暗模式，会诱导用户执行与其目标不符的行为。本文展示，黑暗模式在引导代理轨迹方面高度有效，对代理鲁棒性构成重大风险。为量化这一风险，我们引入DECEPTICON，这是一个用于隔离测试单个黑暗模式的测试环境。DECEPTICON包含700个带有黑暗模式的网页导航任务——600个生成任务和100个真实世界任务，旨在衡量指令遵循成功率和黑暗模式有效性。在最先进的代理中，我们发现黑暗模式在超过70%的测试生成任务和真实世界任务中成功将代理轨迹引导至恶意结果——相比之下，人类的平均率为31%。此外，我们发现黑暗模式有效性与模型规模和测试时推理呈正相关，使得更大、更强大的模型更容易受影响。针对对抗攻击的主要对策，包括上下文提示和护栏模型，无法一致降低黑暗模式干预的成功率。我们的发现揭示了黑暗模式作为网页代理的潜在且未缓解风险，强调了对抗操纵性设计的鲁棒防御的迫切需求。

---

### Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness

- **Venue**: ICLR 2026 Poster
- **Authors**: Erfan Shayegani, Keegan Hines, Yue Dong, Nael Abu-Ghazaleh, Roman Lutz, Spencer Whitehead, Vidhisha Balachandran, Besmira Nushi, Vibhav Vineet
- **Keywords**: Computer-Use Agents, CUA, Multimodal Agents, GUI Agents, LLM Agents, Agentic Frameworks, Long-Horizon Agents, Agent Safety, Agent Reliability, Goal-Directedness, AI Safety, Security, Alignment, Multimodal Alignment, Benchmark, Evaluation, Monitoring
- **OpenReview**: https://openreview.net/forum?id=9W4bPRsEIT
- **PDF**: https://openreview.net/pdf?id=9W4bPRsEIT

**Abstract**

Computer-Use Agents (CUAs) are an increasingly deployed class of agents that take actions on GUIs to accomplish user goals. 
In this paper, we show that CUAs consistently exhibit *Blind Goal-Directedness* (BGD): a bias to pursue goals regardless of feasibility, safety, reliability, or context. We characterize three prevalent patterns of BGD: (i) lack of contextual reasoning, (ii) assumptions and decisions under ambiguity, and (iii) contradictory or infeasible goals. We develop BLIND-ACT, a benchmark of 90 tasks capturing these three patterns. Built on OSWorld, BLIND-ACT provides realistic environments and employs LLM-based judges to evaluate agent behavior, achieving 93.75% agreement with human annotations. We use BLIND-ACT to evaluate nine frontier models, including Claude Sonnet and Opus 4, Computer-Use-Preview, and GPT-5, observing high average BGD rates (80.8%) across them. We show that BGD exposes subtle risks that arise even when inputs are not directly harmful. While prompting-based interventions lower BGD levels, substantial risk persists, highlighting the need for stronger training- or inference-time interventions. Qualitative analysis reveals observed failure modes: execution-first bias (focusing on *how* to act over *whether* to act), thought–action disconnect (execution diverging from reasoning), and request-primacy (justifying actions due to user request). Identifying BGD and introducing BLIND-ACT establishes a foundation for future research on studying and mitigating this fundamental risk and ensuring safe CUA deployment.

**Abstract (Chinese)**

计算机使用代理（CUAs）是一类日益广泛部署的代理，它们通过在图形用户界面（GUI）上执行操作来实现用户目标。

本文中，我们展示了CUAs持续表现出*盲目标导向性*（BGD）：一种不顾可行性、安全性、可靠性或上下文而追求目标的偏差。我们刻画了BGD的三种常见模式：(i) 缺乏上下文推理，(ii) 在模糊性下的假设和决策，以及(iii) 矛盾或不可行的目标。我们开发了BLIND-ACT，这是一个包含90个任务的基准，用于捕捉这三种模式。基于OSWorld构建，BLIND-ACT提供了真实环境，并采用基于LLM的评判器来评估代理行为，与人类标注达成93.75%的协议。我们使用BLIND-ACT评估了九个前沿模型，包括Claude Sonnet和Opus 4、Computer-Use-Preview以及GPT-5，观察到它们平均BGD率高达80.8%。我们展示了BGD暴露了即使输入并非直接有害时也会出现的细微风险。虽然基于提示的干预降低了BGD水平，但实质风险依然存在，这突显了需要更强的训练时或推理时干预。定性分析揭示了观察到的失败模式：执行优先偏差（优先关注*如何*行动而非*是否*行动）、思维–行动脱节（执行偏离推理），以及请求优先（因用户请求而为行动辩护）。识别BGD并引入BLIND-ACT为未来研究奠定了基础，该研究旨在探讨和缓解这一基本风险，并确保CUAs的安全部署。

---

### Opponent Shaping in LLM Agents

- **Venue**: ICLR 2026 Poster
- **Authors**: Marta Emili García Segura, Stephen Hailes, Mirco Musolesi
- **Keywords**: LLM Agents, Opponent Shaping, Multi-agent Systems
- **OpenReview**: https://openreview.net/forum?id=yJoHTqUNry
- **PDF**: https://openreview.net/pdf?id=yJoHTqUNry

**Abstract**

Large Language Models (LLMs) are increasingly being deployed as autonomous agents in real-world environments. As these deployments scale, multi-agent interactions become inevitable, making it essential to understand strategic behavior in such systems. A central open question is whether LLM agents, like reinforcement learning agents, can shape the learning dynamics and influence the behavior of others through interaction alone. In this paper, we present the first investigation of opponent shaping (OS) with LLM-based agents. Existing OS algorithms cannot be directly applied to LLMs, as they require higher-order derivatives, face scalability constraints, or depend on architectural components that are absent in transformers. To address this gap, we introduce ShapeLLM, an adaptation of model-free OS methods tailored for transformer-based agents. Using ShapeLLM, we examine whether LLM agents can influence co-players’ learning dynamics across diverse game-theoretic environments. We demonstrate that LLM agents can successfully guide opponents toward exploitable equilibria in competitive games (Iterated Prisoner’s Dilemma, Matching Pennies, and Chicken) and promote coordination and improve collective welfare in cooperative games (Iterated Stag Hunt and a cooperative version of the Prisoner’s Dilemma). Our findings show that LLM agents can both shape and be shaped through interaction, establishing opponent shaping as a key dimension of multi-agent LLM research.

**Abstract (Chinese)**

大语言模型（LLMs）正日益被部署为现实世界环境中的自主代理。随着这些部署规模的扩大，多代理交互变得不可避免，这使得理解此类系统中的策略行为变得至关重要。一个核心的开放问题是，LLM代理是否像强化学习代理一样，能够仅通过交互来塑造学习动态并影响他人的行为。本文首次对基于LLM的代理进行了对手塑造（OS）研究。现有的OS算法无法直接应用于LLMs，因为它们需要高阶导数、面临可扩展性限制，或依赖于Transformer中缺失的架构组件。为填补这一空白，我们引入了ShapeLLM，这是一种针对基于Transformer的代理的无模型OS方法的适应版本。利用ShapeLLM，我们考察了LLM代理是否能够在多样化的博弈论环境中影响共同玩家的学习动态。我们证明，LLM代理能够在竞争性博弈（迭代囚徒困境、配币游戏和鸡博弈）中成功引导对手趋向可利用均衡，并在合作性博弈（迭代猎鹿游戏以及囚徒困境的合作版本）中促进协调并提升集体福利。我们的发现表明，LLM代理既能通过交互塑造他人，也能被他人塑造，从而确立对手塑造作为多代理LLM研究的关键维度。

---

### Optimizing Agent Planning for Security and Autonomy

- **Venue**: ICLR 2026 Poster
- **Authors**: Aashish Kolluri, Rishi Sharma, Manuel Costa, Boris Köpf, Tobias Nießen, Mark Russinovich, Shruti Tople, Santiago Zanella-Beguelin
- **Keywords**: AI Agents, Security, Prompt Injection Attacks, Information Flow Control, Autonomy
- **OpenReview**: https://openreview.net/forum?id=g0aVCDY3gS
- **PDF**: https://openreview.net/pdf?id=g0aVCDY3gS

**Abstract**

Indirect prompt injection attacks threaten AI agents that execute consequential actions, motivating deterministic system-level defenses. Such defenses can provably block unsafe actions by enforcing confidentiality and integrity policies, but currently appear costly: they reduce task completion rates and increase token usage compared to probabilistic defenses. We argue that existing evaluations miss a key benefit of system-level defenses: reduced reliance on human oversight. We introduce autonomy metrics to quantify this benefit: the fraction of consequential actions an agent can execute without human-in-the-loop (HITL) approval while preserving security. To increase autonomy, we design a security-aware agent that (i) introduces richer HITL interactions, and (ii) explicitly plans for both task progress and policy compliance. We implement this agent design atop an existing information-flow control defense against prompt injection and evaluate it on the AgentDojo and WASP benchmarks. Experiments show that this approach yields higher autonomy without sacrificing utility (task completion).

**Abstract (Chinese)**

间接提示注入攻击威胁到执行具有重大后果动作的 AI 代理，这促使采用确定性系统级防御。此类防御通过强制执行机密性和完整性策略，能够可证明地阻止不安全动作，但目前似乎代价高昂：与概率性防御相比，它们降低了任务完成率并增加了令牌使用量。我们认为，现有的评估忽略了系统级防御的一个关键优势：减少对人类监督的依赖。我们引入自治度指标来量化这一优势：代理在保持安全性的前提下，能够在无需人工在环 (HITL) 批准的情况下执行的有重大后果动作的比例。为了提高自治度，我们设计了一个安全感知代理，该代理 (i) 引入更丰富的 HITL 交互，以及 (ii) 明确规划任务进展和策略合规性。我们在现有的针对提示注入的信息流控制防御之上实现了这一代理设计，并在 AgentDojo 和 WASP 基准上对其进行评估。实验表明，这种方法在不牺牲效用（任务完成）的情况下实现了更高的自治度。

---

### Searching for Privacy Risks in LLM Agents via Simulation

- **Venue**: ICLR 2026 Poster
- **Authors**: Yanzhe Zhang, Diyi Yang
- **Keywords**: LLM Agent, Privacy, Search, AI Risk
- **OpenReview**: https://openreview.net/forum?id=nz4ZqbrBEi
- **PDF**: https://openreview.net/pdf?id=nz4ZqbrBEi

**Abstract**

The widespread deployment of LLM-based agents is likely to introduce a critical privacy threat: malicious agents that proactively engage others in multi-turn interactions to extract sensitive information. However, the evolving nature of such dynamic dialogues makes it challenging to anticipate emerging vulnerabilities and design effective defenses. To tackle this problem, we present a search-based framework that alternates between improving attack and defense strategies through the simulation of privacy-critical agent interactions. Specifically, we employ LLMs as optimizers to analyze simulation trajectories and iteratively propose new agent instructions. To explore the strategy space more efficiently, we further utilize parallel search with multiple threads and cross-thread propagation. Through this process, we find that attack strategies escalate from direct requests to sophisticated tactics, such as impersonation and consent forgery, while defenses evolve from simple rule-based constraints to robust identity-verification state machines. The discovered attacks and defenses generalize across diverse scenarios and backbone models, providing useful insights for developing privacy-aware agents.

**Abstract (Chinese)**

大语言模型（LLM）代理的广泛部署很可能引入一个关键的隐私威胁：恶意代理主动与他人进行多轮交互以提取敏感信息。然而，此类动态对话的演化特性使得预见新兴漏洞并设计有效防御措施变得具有挑战性。为解决这一问题，我们提出了一种基于搜索的框架，通过模拟隐私关键的代理交互，在改进攻击和防御策略之间交替进行。具体而言，我们将LLM用作优化器来分析模拟轨迹，并迭代提出新的代理指令。为了更有效地探索策略空间，我们进一步利用多线程并行搜索和跨线程传播。通过这一过程，我们发现攻击策略从直接请求升级到复杂策略，如冒充和同意伪造，而防御则从简单的基于规则的约束演变为稳健的身份验证状态机。所发现的攻击和防御在多样化的场景和骨干模型中具有泛化性，为开发隐私感知代理提供了有用的洞见。

---

### When AI Agents Collude Online: Financial Fraud Risks by Collaborative LLM Agents on Social Platforms

- **Venue**: ICLR 2026 Poster
- **Authors**: Qibing Ren, Zhijie Zheng, Jiaxuan Guo, Junchi Yan, Lizhuang Ma, Jing Shao
- **Keywords**: financial fraud, multi-agent system, agent society, agent collusion
- **OpenReview**: https://openreview.net/forum?id=a1d2smwmBS
- **PDF**: https://openreview.net/pdf?id=a1d2smwmBS

**Abstract**

In this work, we study the risks of collective financial fraud in large-scale multi-agent systems powered by large language model (LLM) agents. We investigate whether agents can collaborate in fraudulent behaviors, how such collaboration amplifies risks, and what factors influence fraud success. To support this research, we present MultiAgentFinancialFraudBench, a large-scale benchmark for simulating financial fraud scenarios based on realistic online interactions. The benchmark covers 28 typical online fraud scenarios, spanning the full fraud lifecycle across both public and private domains. We further analyze key factors affecting fraud success, including interaction depth, activity level, and fine-grained collaboration failure modes. Finally, we propose a series of mitigation strategies including adding content-level warnings to fraudulent posts and dialogues, using LLMs as monitors to block potentially malicious agents, and fostering group resilience through information sharing at the societal level. Notably, we observe that malicious agents can adapt to environmental interventions. Our findings highlight the real-world risks of multi-agent financial fraud and suggest practical measures for mitigating them. Code is available at https://github.com/zheng977/MutiAgent4Fraud.

**Abstract (Chinese)**

在本工作中，我们研究了由大语言模型 (LLM) 代理驱动的大规模多代理系统中集体金融欺诈的风险。我们探讨了代理是否能够协作从事欺诈行为，这种协作如何放大风险，以及影响欺诈成功的关键因素。为了支持这项研究，我们提出了 MultiAgentFinancialFraudBench，这是一个基于真实在线交互模拟金融欺诈场景的大规模基准。该基准涵盖了 28 种典型在线欺诈场景，跨越公共和私人领域中的完整欺诈生命周期。我们进一步分析了影响欺诈成功的关键因素，包括交互深度、活动水平以及细粒度协作失败模式。最后，我们提出了一系列缓解策略，包括向欺诈性帖子和对话添加内容级警告、使用 LLM 作为监控器阻挡潜在恶意代理，以及通过社会层面的信息共享增强群体韧性。值得注意的是，我们观察到恶意代理能够适应环境干预。我们的发现突显了多代理金融欺诈的现实世界风险，并建议了缓解这些风险的实际措施。代码可在 https://github.com/zheng977/MutiAgent4Fraud 获取。

---

### When Agents “Misremember” Collectively: Exploring the Mandela Effect in LLM-based Multi-Agent Systems

- **Venue**: ICLR 2026 Poster
- **Authors**: Naen Xu, Hengyu An, Shuo Shi, Jinghuai Zhang, Chunyi Zhou, Changjiang Li, Tianyu Du, Zhihui Fu, Jun Wang, Shouling Ji
- **Keywords**: LLM for Social Science, Mandela Effect, Multi-agent System, Cognitive Bias
- **OpenReview**: https://openreview.net/forum?id=yIoMqDes7O
- **PDF**: https://openreview.net/pdf?id=yIoMqDes7O

**Abstract**

Recent advancements in large language models (LLMs) have significantly enhanced the capabilities of collaborative multi-agent systems, enabling them to address complex challenges. However, within these multi-agent systems, the susceptibility of agents to collective cognitive biases remains an underexplored issue. A compelling example is the Mandela effect, a phenomenon where groups collectively misremember past events as a result of false details reinforced through social influence and internalized misinformation. This vulnerability limits our understanding of memory bias in multi-agent systems and raises ethical concerns about the potential spread of misinformation. In this paper, we conduct a comprehensive study on the Mandela effect in LLM-based multi-agent systems, focusing on its existence, causing factors, and mitigation strategies. We propose ManBench, a novel benchmark designed to evaluate agent behaviors across four common task types that are susceptible to the Mandela effect, using five interaction protocols that vary in agent roles and memory timescales. We evaluate agents powered by several LLMs on ManBench to quantify the Mandela effect, and analyze how different factors affect it. Moreover, we propose strategies to mitigate this effect, including prompt-level defenses (e.g., cognitive anchoring and source scrutiny) and model-level alignment-based defense, achieving an average 74.40% reduction in the Mandela effect compared to the baseline. Our findings provide valuable insights for developing more resilient and ethically aligned collaborative multi-agent systems. Code and dataset are available at https://github.com/bluedream02/Mandela-Effect.

**Abstract (Chinese)**

大型语言模型 (LLMs) 的最新进展显著提升了协作多代理系统的能力，使其能够应对复杂挑战。然而，在这些多代理系统中，代理对集体认知偏差的易感性仍是一个未充分探索的问题。一个引人注目的例子是曼德拉效应，这是一种现象，其中群体由于通过社会影响强化虚假细节并内化错误信息而集体错误记忆过去事件。这种漏洞限制了我们对多代理系统中记忆偏差的理解，并引发了关于错误信息潜在传播的伦理担忧。在本文中，我们对基于 LLM 的多代理系统中的曼德拉效应进行了全面研究，重点关注其存在性、成因因素和缓解策略。我们提出了 ManBench，这是一个新型基准，用于评估四个易受曼德拉效应影响的常见任务类型中的代理行为，采用五种交互协议，这些协议在代理角色和记忆时间尺度上有所不同。我们在 ManBench 上评估了由几种 LLM 驱动的代理，以量化曼德拉效应，并分析不同因素如何影响它。此外，我们提出了缓解这种效应的策略，包括提示级防御（例如，认知锚定和来源审查）以及基于模型级对齐的防御，与基线相比，平均减少了 74.40% 的曼德拉效应。我们的发现为开发更具弹性和伦理对齐的协作多代理系统提供了宝贵见解。代码和数据集可在 https://github.com/bluedream02/Mandela-Effect 获取。

---

### Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents

- **Venue**: ICLR 2026 Poster
- **Authors**: Shuai Shao, Qihan Ren, Dongrui Liu, Chen Qian, Boyi Wei, Dadi Guo, Yang JingYi, Xinhao Song, Linfeng Zhang, Weinan Zhang, Jing Shao
- **Keywords**: Self-Evolving Agent, Agent Safety, Large Language Models, Safety Evaluation
- **OpenReview**: https://openreview.net/forum?id=Fd1jgQQW28
- **PDF**: https://openreview.net/pdf?id=Fd1jgQQW28

**Abstract**

Advances in Large Language Models (LLMs) have enabled a new class of \textbf{\textit{self-evolving agents}} that autonomously improve through environmental interaction, demonstrating strong capabilities. However, self-evolution also introduces novel risks overlooked by current safety research. In this work, we study case where an agent's self-evolution deviates in unintended ways, leading to undesirable or even harmful outcomes. We refer to this as \textit{\textbf{Misevolution}}. We evaluate misevolution along four key evolutionary pathways: model, memory, tool, and workflow. Our empirical findings reveal that misevolution is a widespread risk, affecting agents built even on top-tier LLMs (\textit{e.g.}, Gemini-2.5-Pro). Different emergent risks are observed, such as degradation of safety alignment after memory accumulation, or unintended introduction of vulnerabilities in tool creation and reuse.  To our knowledge, this is the first study to systematically conceptualize misevolution and provide empirical evidence of its occurrence, highlighting an urgent need for new safety paradigms for self-evolving agents. Finally, we discuss potential mitigation strategies to inspire further research on building safer and more trustworthy self-evolving agents.

**Abstract (Chinese)**

大语言模型 (LLMs) 的进步催生了一类新型\textbf{\textit{自我进化代理}}，它们通过与环境的自主交互实现自我改进，展现出强大能力。然而，自我进化也引入了当前安全研究忽略的新型风险。在本工作中，我们研究了代理自我进化以非预期方式偏离的情况，导致不良甚至有害结果。我们将此称为\textit{\textbf{误进化}}。我们沿着四个关键进化路径评估误进化：模型、记忆、工具和工作流。我们的实证发现揭示，误进化是一种普遍风险，甚至影响基于顶级 LLMs（如 \textit{Gemini-2.5-Pro}）构建的代理。观察到不同的涌现风险，例如记忆积累后安全对齐的退化，或在工具创建和重用中意外引入漏洞。据我们所知，这是第一个系统概念化误进化并提供其发生实证证据的研究，突显了对自我进化代理需要新型安全范式的紧迫性。最后，我们讨论了潜在缓解策略，以启发构建更安全、更可信的自我进化代理的进一步研究。

---
