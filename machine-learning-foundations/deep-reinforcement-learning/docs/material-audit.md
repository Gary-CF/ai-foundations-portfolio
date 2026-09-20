# 深度强化学习：材料索引、缺课补充与校订记录

核对日期：2026-09-20。配套提纲：`deep-rl-outline-v2.md`，七篇二十二章。

本文件完成三件事：标明上传稿覆盖范围；为没有转录稿的讲次提供可直接用于后续写作的概念、公式与例子；登记抽查中需要修正或补足条件的位置。以下是独立编写的学习笔记，不是缺失视频的逐字转录，也不声称复原了课堂口头例子。

## 1. 材料结论与缺口

共有 **47 份 Markdown 转录稿：白板推导 28 份，CS285 Spring 2026 19 份**。后者从 L1 到 L19 连续，缺少的是 L20–25；L21–22 属于期中复习。缺课讲义全部已取得，内容与当前 [CS285 Spring 2026 官方目录](https://rail.eecs.berkeley.edu/deeprlcourse/) 对齐。

本轮完成逐文件标题/来源核对、主题映射、代表段落抽查，以及缺课 PDF 的结构阅读和关键公式页检查。尚未完成 47 稿的逐句、逐公式校订。稿件中大量 `images/…` 相对图片引用没有对应的上传图片；画面文字描述仅作检索线索，不作为已经看过原图的证据。

| 缺少转录的讲次 | 官方材料与总页数 | 应补入正文的位置 |
|---|---|---|
| L20 RL Theory | [讲义，28 页](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-20.pdf) | 第 21 章；回链第 2、5–6 章 |
| L21 Midterm Review 1 | [讲义，34 页](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-21.pdf) | 模仿、PG、AC 的复习题 |
| L22 Midterm Review 2 | [讲义，73 页](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-22.pdf) | 价值、推断、模型、离线、探索与理论的复习题 |
| L23 Advanced Exploration；PDF 题名 Exploration and Skill Learning | [讲义，18 页](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-23.pdf) | 第 19 章技能发现与目标探索 |
| L24 Multi-task RL；PDF 题名 Multi-Task and Hierarchical RL | [讲义，53 页](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-24.pdf) | 第 20 章多任务、目标、后继表示、层次与 Meta-RL |
| L25 Challenges and Open Problems | [讲义，44 页](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-25.pdf) | 第 22 章开放问题与实验设计 |

页码统一按 PDF 从 1 开始计数，包含封面。网站周历还列有嘉宾课安排，但未给出可核实的额外编号讲义，本轮不虚构 L26 等讲次。

## 2. 补充一：L20 理论——更新误差怎样变成长程误差

**课程范围定位。** 阅读顺序为：理论问题与假设（pp.3–5）→ 价值迭代（pp.6–9）→ 暂不处理探索的样本复杂度（pp.12–20）→ fitted Q iteration 的采样与逼近误差（pp.22–28）。以下统一符号后重写基础推导；不是对讲义采样界常数的逐字复刻。[L20 官方讲义](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-20.pdf)

### 2.1 先固定问题，再陈述保证

这里先采用有限状态/动作、无限时域折扣 MDP，\(0\leq\gamma<1\)，且 \(|r(s,a)|\leq R_{\max}\)。令 \(r(s,a)\) 表示一步奖励的条件均值，\(P(\cdot\mid s,a)\) 为转移分布，\(\|\cdot\|_\infty\) 表示对所有状态动作取最大绝对值。

“价值迭代收敛”“用样本估计模型的误差小”“深度 Q 网络训练稳定”是三个不同命题，不能相互替代。样本复杂度还必须说明样本如何获得；给定每个状态动作的采样能力，并未解决如何探索到这些状态。

### 2.2 Bellman 压缩：为什么精确价值迭代能收敛

定义最优 Bellman 算子：

$$
(\mathcal TQ)(s,a)=r(s,a)+\gamma\mathbb E_{s'\sim P(\cdot\mid s,a)}\left[\max_{a'}Q(s',a')\right].
$$

利用 \(|\max_i x_i-\max_i y_i|\leq\max_i|x_i-y_i|\)，得到

$$
\|\mathcal TQ-\mathcal T\widetilde Q\|_\infty
\leq\gamma\|Q-\widetilde Q\|_\infty.
$$

所以 \(Q_{k+1}=\mathcal TQ_k\) 满足

$$
\|Q_k-Q^*\|_\infty\leq\gamma^k\|Q_0-Q^*\|_\infty.
$$

这里证明的是精确算子的压缩。若更新中加入回归投影、采样或非凸优化，就需要额外分析，不能把同一结论直接贴到 DQN 上。

### 2.3 近似更新：把两类误差接起来

设一次学习后的 \(Q_{k+1}\) 与精确 backup 的差满足

$$
\|Q_{k+1}-\mathcal TQ_k\|_\infty\leq\epsilon_k.
$$

记 \(e_k=\|Q_k-Q^*\|_\infty\)，三角不等式给出

$$
e_{k+1}\leq\gamma e_k+\epsilon_k.
$$

若每一步 \(\epsilon_k\leq\epsilon\)，展开递推可得

$$
e_K\leq\gamma^K e_0+\epsilon\frac{1-\gamma^K}{1-\gamma}.
$$

因此 \(\limsup_K e_K\leq\epsilon/(1-\gamma)\)。用 limsup 而非直接断言序列收敛，因为持续的近似误差可能导致振荡。

若 \(\widehat{\mathcal T}\) 是采样得到的 backup，再拆开：

$$
\|Q_{k+1}-\mathcal TQ_k\|_\infty
\leq
\underbrace{\|Q_{k+1}-\widehat{\mathcal T}Q_k\|_\infty}_{\text{拟合/逼近与优化误差}}
+
\underbrace{\|\widehat{\mathcal T}Q_k-\mathcal TQ_k\|_\infty}_{\text{采样误差}}.
$$

低训练 MSE 不自动给出全状态动作的无穷范数误差界；没覆盖到的区域尤其如此。

**自编小例子。** 一状态、一动作、自环环境，真实奖励为 0。若每次 backup 固定多加 \(0.01\)，最终误差为 \(0.01/(1-\gamma)\)：\(\gamma=0.9\) 时为 0.1，\(\gamma=0.99\) 时为 1。微小的局部偏差能通过长程自举放大。

### 2.4 模型误差与有效时域

固定策略 \(\pi\)，令 \(P^\pi\) 为状态转移矩阵。若真实模型和估计模型的奖励相同，且 \(\widehat P^\pi\) 也是随机矩阵，则

$$
V^\pi-\widehat V^\pi
=\gamma(I-\gamma P^\pi)^{-1}(P^\pi-\widehat P^\pi)\widehat V^\pi.
$$

因为 \(\|(I-\gamma P^\pi)^{-1}\|_\infty\leq(1-\gamma)^{-1}\)，且 \(\|\widehat V^\pi\|_\infty\leq R_{\max}/(1-\gamma)\)，若每行转移概率的 L1 误差至多 \(\epsilon_P\)，则

$$
\|V^\pi-\widehat V^\pi\|_\infty
\leq\frac{\gamma R_{\max}\epsilon_P}{(1-\gamma)^2}.
$$

这是一个便于理解的固定策略界，不是最紧样本复杂度定理。奖励也有误差时要增加相应项；策略由同一数据选出来时，要额外处理统一保证。正式推导可继续参照讲义引用的 [RL Theory 教材](https://rltheorybook.github.io/)。

**本节自测。** 为什么 \(\gamma\) 接近 1 时误差界恶化？为什么经验回放上的低损失不足以保证策略好？请分别回答“误差传播”与“数据覆盖”，不要混成一个原因。

## 3. 补充二：L23——从探索到无奖励技能学习

**课程范围定位。** L19 的探索之后，L23 进一步讨论信息论、可区分技能和目标探索；重点入口是信息量（pp.6–8）、技能学习（pp.10–13）、目标互信息与 Skew-Fit（pp.15–18）。[L23 官方讲义](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-23.pdf)

### 3.1 三个不同的目标

| 对象 | 关心的问题 | 不能直接推断的结论 |
|---|---|---|
| 策略动作熵 \(H(A\mid S)\) | 给定状态，动作有多随机？ | 动作随机不保证到达不同区域 |
| 状态分布熵 \(H(S)\) | 访问状态有多分散？ | 环境自身噪声也能产生高熵 |
| 互信息 \(I(Z;S)\) | 换一个技能，访问状态是否可区分？ | 可区分不保证对未来任务有用 |

这里的 \(S\) 必须说明来自终态、时间平均占用还是折扣占用；不同定义对应不同优化目标。连续空间中还需区分微分熵与离散熵，不能直接比较不同坐标下的数值。

Empowerment 的直觉是：动作选择能可靠影响多少种未来结果。常见形式涉及给定初始状态时，动作序列与未来状态之间的互信息；不要将它与所有状态覆盖目标简单画等号。

### 3.2 技能条件策略与 DIAYN

先采样技能 \(z\sim p(z)\)，再由 \(\pi_\theta(a\mid s,z)\) 与环境交互。判别器 \(q_\phi(z\mid s)\) 根据状态预测所选技能。

由互信息定义与条件 KL 非负，得到一个可学习下界：

$$
I(Z;S)=\mathbb E[\log p(z\mid s)-\log p(z)]
\geq\mathbb E[\log q_\phi(z\mid s)-\log p(z)].
$$

对应内部奖励可写为

$$
r_{\rm skill}(s,z)=\log q_\phi(z\mid s)-\log p(z).
$$

固定均匀技能先验可避免只采少数技能；最大熵策略还鼓励每个技能内部保持随机性。实际一步奖励常用下一状态 \(s_{t+1}\) 计算，写代码时须统一索引。[DIAYN 原论文，算法 1 与第 3 节](https://arxiv.org/html/1802.06070v6)

最小训练循环：采样技能 → 条件策略收集转移 → 用技能标签训练判别器 → 用判别器奖励更新策略。无外部任务奖励不等于没有优化目标，也不等于没有环境交互。

**自编小例子。** 二维房间中让两个技能分别稳定访问左、右区域，判别器容易区分；若两者都随机抖动且最终位置分布相同，动作熵可以很高而技能—状态互信息很低。反过来，仅靠无关视觉细节区分技能，也未必学到有用控制。

### 3.3 从技能到目标

技能 \(z\) 可以表示运动方式；目标 \(g\) 通常描述想达到的状态或结果。用“到达某一点”未必能表达“以某种姿态持续运动”。正文应先区分这两类条件变量。

若用终态 \(S_T\) 表达效果，\(I(G;S_T)=H(S_T)-H(S_T\mid G)\) 提示两个方向：覆盖不同结果，以及在给定目标下可靠地产生结果。这个分解给出理解角度，不代表实际算法总能分别精确优化两项。Skew-Fit 作为目标分布学习的代表，放在第 19 章末尾，并向第 20 章目标条件学习交叉引用。

**写作验收。** 能解释“动作随机”“状态新颖”“技能可区分”“目标可达”四者的区别；能写出判别器和策略分别学习什么。

## 4. 补充三：L24——如何把经验迁移给新任务

**课程范围定位。** 本讲不仅讲多任务：任务条件化（pp.5–13）、目标重标记（pp.15–19）、后继表示/特征（pp.22–30）、未来状态分类（pp.31–33）、层次结构（pp.35–40）、Meta-RL（pp.46–53）。因此将第 20 章分为六节，避免把后半课压缩成几个名词。[L24 官方讲义](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-24.pdf)

### 4.1 多任务与目标条件化

任务 \(c\) 可改变奖励、目标或动力学。若任务上下文已知，学习 \(\pi(a\mid s,c)\)；若任务未知，必须从历史中推断相关信息。共享参数可能提高数据效率，也可能因任务干扰、难度不均或奖励尺度不同而失衡。

目标条件化常写为 \(\pi(a\mid s,g)\)、\(Q(s,a,g)\)。HER 的要点是利用真实达到的结果重新解释轨迹：原目标失败的轨迹，对另一目标可能成功。重标记后须根据新目标重算奖励，并按任务定义处理成功终止；若目标改变了物理动力学，就不能随意复用原转移。

**自编小例子。** 小车原本要去 A，却到了 B。它没有完成去 A 的任务，但这条经验能帮助学习去 B。不能把它直接当成“去 A 获得正奖励”的数据。

### 4.2 后继表示：把“将访问哪里”与“那里值多少”分开

对固定策略定义未归一化后继表示：

$$
M^\pi(s,s')=\mathbb E_\pi\left[\sum_{t=0}^{\infty}\gamma^t\mathbf1\{S_t=s'\}\mid S_0=s\right].
$$

当奖励只依赖当前状态时，

$$
V^\pi(s)=\sum_{s'}M^\pi(s,s')r(s').
$$

若用归一化版本 \(\mu^\pi=(1-\gamma)M^\pi\)，它在继续型 MDP 中是未来状态概率分布；此时计算价值要除以 \(1-\gamma\)。课堂使用归一化占用的地方，必须显式换算，不能与未归一化定义直接拼接。

更一般地，设一步奖励具有特征线性形式 \(r_w(s,a,s')=\phi(s,a,s')^\top w\)，定义

$$
\psi^\pi(s,a)=\mathbb E_\pi\left[\sum_{t=0}^{\infty}\gamma^t\phi(S_t,A_t,S_{t+1})\mid S_0=s,A_0=a\right],
\qquad Q_w^\pi(s,a)=\psi^\pi(s,a)^\top w.
$$

\(\psi^\pi\) 的 TD 目标为 \(\phi(s,a,s')+\gamma\mathbb E_{a'\sim\pi}[\psi^\pi(s',a')]\)。动力学、特征与策略固定而奖励权重改变时，能快速重估策略价值；所得是 \(Q_w^\pi\)，不是新任务的 \(Q_w^*\)。若保留多套已有策略的后继特征，可以按其 Q 值做广义策略改进；估计不精确时还需误差条件。

**自编小例子。** 特征记录未来红色、蓝色区域的折扣访问次数，\(w\) 为两种颜色的奖励。更换颜色奖励无需重新预测访问次数；若墙的位置改变，未来访问规律也改变，原后继特征就可能失效。

### 4.3 C-learning：用分类恢复未来状态的密度比

连续状态中，精确命中某个点的概率通常为零，但对该位置的概率密度可以非零。用“未来状态样本”为正例、参考分布 \(p_{\rm ref}(g)\) 的样本为负例。若两类先验相等，最优分类器满足

$$
C^*(s,a,g)=\frac{p_+^\pi(g\mid s,a)}{p_+^\pi(g\mid s,a)+p_{\rm ref}(g)},
\qquad
\frac{C^*}{1-C^*}=\frac{p_+^\pi(g\mid s,a)}{p_{\rm ref}(g)}.
$$

这只是 Bayes 公式给出的分类—密度比桥梁，不是完整 C-learning 更新。课程 p.33 先展示 on-policy 采样版本；原论文还推导 off-policy 递归分类，不能混写为“任意回放样本直接做上述分类就完成了全部算法”。[C-learning 原论文](https://arxiv.org/abs/2011.08909)

### 4.4 层次结构与时间抽象

Option 可记为 \(o=(\mathcal I_o,\pi_o,\beta_o)\)：启动集合、内部策略、终止概率。高层选择 option，低层可能连续执行 \(\tau\) 步。高层学习目标应包含这段累计折扣奖励，并用 \(\gamma^\tau\) bootstrap：

$$
y_{\rm high}=\sum_{j=0}^{\tau-1}\gamma^jR_{t+j+1}+\gamma^\tau V_{\rm high}(S_{t+\tau}),
$$

环境真正终止时省略最后一项。不能把持续多步的 option 当成持续一步的动作来折扣。

结构带来的主要困难是联合学习：尚未学好的低层可能不被高层选择，从而拿不到训练数据；低层持续变化也使高层面临非平稳问题。先训练目标条件低层、再训练高层选择子目标，是值得比较的一条路径。

### 4.5 Meta-RL：学会利用试探获得的任务信息

多任务策略可以直接得到任务标签；Meta-RL 常要求根据少量交互适应未见任务。若任务是隐藏变量 \(c\)，历史 \(h_t\) 可以形成信念 \(b_t(c)=P(c\mid h_t)\)。

在“同任务多 episode 适应”的循环网络设定中，环境 episode 结束不一定清空 RNN 记忆；同任务的线索需要留给后续 episode。更换独立任务时通常需要重置。该规则依赖评估协议，不能泛化为所有 RL 都不重置隐藏状态。

**自编小例子。** 两扇门只有一扇有奖励，每个任务内奖励门固定。同任务第一幕试门的信息应帮助第二幕决策；新任务重新随机奖励门时，不能把旧门的结论当作已知事实。

### 4.6 五类设定的边界

| 设定 | 主要条件变量或结构 | 要解决的问题 |
|---|---|---|
| 多任务 RL | 已知任务上下文 c | 共享经验与参数 |
| 目标条件 RL | 目标 g | 用一个策略完成多个目标 |
| 技能发现 | 自采样技能 z | 没有任务奖励时学可区分行为 |
| 层次 RL | 高层选择低层技能/目标 | 时间抽象与组合 |
| Meta-RL | 历史/任务信念 | 利用交互快速适应 |

这些设定能够组合，并非五个互斥算法类别。

## 5. 补充四：L25——把开放问题转成可检验的问题

本讲以工程工具、真实世界学习、通用决策学习三个视角回顾 RL；相关入口为 pp.11–20、pp.21–30、pp.31–44。讲义中的研究愿景应标为观点或问题，不当作已经证明的普遍结论。[L25 官方讲义](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-25.pdf)

以下表格是据此自拟的后续实验问题，不是课程指定作业：

| 方向 | 可以落地的问题 | 最低评估证据 |
|---|---|---|
| 仿真与迁移 | 改变摩擦、延迟后性能怎样变化？ | 训练范围与未见扰动分开报告 |
| 数据效率 | 示范、离线预训练、模型 rollout 能省多少交互？ | 相同真实交互预算，单列额外数据与计算 |
| 自主持续学习 | 不靠人工 reset 时，能否恢复并继续学习？ | 成功率、恢复率、人工干预次数 |
| 奖励与任务设定 | 奖励上升是否伴随真实目标改善？ | 独立任务指标与失败案例 |
| 泛化与适应 | 面对新目标/动力学时，记忆或微调是否有效？ | 零样本与少量交互分别评估 |
| 既有数据的利用 | 同一批数据用于 BC、离线 RL、建模，各解决什么？ | 数据覆盖说明、统一测试任务与消融 |

正文应留下“问题—假设—实验—结果—局限”的记录，而不是用一个新缩写替代问题分析。

## 6. L21–22：作为复习与查漏层

L21 复习 BC、PG 和 AC；L22 延续价值学习、推断与控制、奖励学习、模型式/离线 RL、探索和理论。它们不必各自变成新章节。下面是自行编写的自测题，页码便于回查。[L21](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-21.pdf)、[L22](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-22.pdf)

| 自测题 | 最低合格答案应包含 | 回查位置 |
|---|---|---|
| BC 的单步误差为何可能放大？ | 自己的动作改变后续状态分布；DAgger 需要在学习者访问状态上获得专家标签 | L21 pp.3–9 |
| 专家行为多峰时，单高斯有什么问题？ | 平均动作可能不是有效示范行为；更强策略表示与状态分布偏移是两个问题 | L21 pp.10–13 |
| 动作重要性比为什么不等于全部分布修正？ | 状态占用也会变；说明采用精确比值还是局部代理目标 | L21 pp.17–28 |
| GAE 的 λ 在调整什么？ | TD residual 的多步组合及偏差/方差；不等同于折扣 γ | L21 pp.31–33 |
| Double Q 的两个角色是什么？ | 选择动作与评估该动作的值分开 | L22 pp.7–10 |
| 最大熵控制改变了什么？ | 目标含熵，soft backup 和策略更新需一致 | L22 pp.21–29 |
| 奖励模型得分高是否等于任务完成好？ | 泛化与过度优化需独立检验 | L22 pp.30–34 |
| 模型不确定性都可通过多采样消除吗？ | 区分可减少的认知不确定性与环境随机性 | L22 pp.37–41 |
| IQL、CQL 的机制有何不同？ | 前者用数据内动作回归与优势加权提取策略；后者抑制数据外动作的过高价值 | L22 pp.55–57 |
| FQL 中生成模型与 Actor 是否是同一个角色？ | 区分行为生成建模、价值优化和蒸馏约束；训练目标分别列出 | L22 pp.59–60；回查 HW5 |
| 预测误差大为何未必意味着值得探索？ | 可能是不可预测噪声，而非可学习信息 | L22 pp.63–65 |
| 表格 VI 的收敛为什么不能直接保证 DQN？ | 精确压缩算子与采样/函数逼近/优化过程不同 | L22 pp.67–73 |

## 7. 转录校订：已发现的问题与条件提醒

以下记录的是**所上传文字的表达问题**；没有核对原始音视频的位置，不将错误归因于讲师。原稿保留，规范笔记使用修正表述。时间均为稿件时间戳。

| 文件标识与定位 | 问题或容易误读处 | 笔记采用的表述 |
|---|---|---|
| BV15L411T7LM p1，00:11:42–00:12:26 | 将 off-policy Expected SARSA 概括成 Q-learning | 只有目标策略对当前 Q 贪心时，期望目标才退化为 max；异策略本身不够 |
| BV1EZ4y1R7r4 p1，开头约 00:00–00:50 | 用“离线策略”称呼行为策略 b 与目标策略 π 不同 | 统一为异策略/off-policy；offline 是固定数据、不能继续交互的另一维度 |
| yt_lQaVa53pS-Q / L8，00:01:49–00:02:14 | 将无 replay 的经典 Q-learning 称为 on-policy | Q-learning 的目标仍是贪心策略；有无 replay 不决定 on/off-policy |
| yt_u2Ug046R0xk / L17，00:04:49–00:05:16 | 上下文在讲新策略采样，却出现 off-policy REINFORCE 的称呼 | 标准 REINFORCE 使用当前策略样本；复用异策略数据必须说明修正 |
| BV1N5411o7QD p1，00:04:50–00:05:24 | “新策略一定更好”的论证容易被迁移给有限样本 MC 估计 | 精确 qπ 的策略改进有相应保证；噪声估计下不能默认每轮单调改进 |
| BV1N5411o7QD p1，00:05:24–00:06:37 | max 与 argmax 的叙述混杂 | π′(s) 取 argmax；Qπ(s,π′(s)) 等于 max 的值，两者类型不同 |
| BV1RA411q7wt p2，00:00:26–00:01:55 | 将离散状态顺带称作有限状态 | 离散可以可数无限；有限是需额外写明的假设 |
| yt_xtZe3ulf6aM / L9，00:29:38 起的推导 | 边缘联合分布、动作条件分布的符号容易混用；属于记法提醒 | 用 dπ(s)π(a|s) 写联合占用，不把 π(s,a) 与 π(a|s) 当成同一量 |
| 多份中文稿 | SaaS / sasa、Q landing 等识别结果 | 根据上下文规范为 SARSA、Q-learning；保留首次英文全名 |
| 多份稿件 | 画面描述、补充画面重复插入正文，夹杂校订提示语 | 正文只保留论证；截图说明、编辑说明与课堂内容分开 |

### 7.1 一个可立即使用的更正例子

Expected SARSA 的目标为

$$
y=r+\gamma\sum_{a'}\pi(a'\mid s')Q(s',a').
$$

若下一状态的 Q 值是 \((1,3)\)，目标策略为 \((1/2,1/2)\)，期望项为 2；即使行为策略不同，它也不是 Q-learning 的最大值 3。只有目标策略把质量放在最大值动作上，才退化为 Q-learning 目标。原文前面讲到贪心条件，笔记中不能在总结时把它省略。

### 7.2 全书统一的符号约定

- 转移写作 \((S_t,A_t,R_{t+1},S_{t+1})\)；回报 \(G_t=\sum_{k\geq0}\gamma^kR_{t+k+1}\)。CS285 若用 r_t，转换时明确一步索引。
- 行为策略 b 负责采样，目标策略 π 是正在评估/改进的对象；旧策略与 reference policy 另设符号。
- 折扣占用若归一化，写 \(d_\gamma^\pi(s)=(1-\gamma)\sum_t\gamma^tP_\pi(S_t=s)\)；策略梯度系数、后继表示与价值公式随之换算。
- 神经网络输出用 \(Q_\theta,V_\phi\)，数学真值用 \(Q^\pi,V^\pi\)；不要把有限样本估计直接写成真值。
- gamma=1 的有限幕推导与 gamma<1 的无限时域推导分开记录；终止与截断也依任务语义分别处理。

## 8. 全部上传稿的主题索引

本节按知识主题或讲次列出；每个文件恰好登记一次。“对应章”指 v2 主线提纲。标题中的“同轨/离轨”保留原语义，正文统一为 on-policy / off-policy。

### 8.1 白板推导：28 份

| 文件 | 核心主题 | 对应章 | 视频入口 |
|---|---|---|---|
| `BV1RA411q7wt_p1_manuscript.md` | 马尔可夫链、回报与问题入口 | 1–2 | [原视频](https://www.bilibili.com/video/BV1RA411q7wt/?p=1) |
| `BV1RA411q7wt_p2_manuscript.md` | MDP 与环境动态 | 1–2 | [原视频](https://www.bilibili.com/video/BV1RA411q7wt/?p=2) |
| `BV1RA411q7wt_p3_manuscript.md` | 策略与价值函数 | 2 | [原视频](https://www.bilibili.com/video/BV1RA411q7wt/?p=3) |
| `BV1RA411q7wt_p4_manuscript.md` | Bellman 期望方程 | 2 | [原视频](https://www.bilibili.com/video/BV1RA411q7wt/?p=4) |
| `BV1RA411q7wt_p5_manuscript.md` | Bellman 最优方程 | 2 | [原视频](https://www.bilibili.com/video/BV1RA411q7wt/?p=5) |
| `BV1nV411k7ve_p1_manuscript.md` | 动态规划概览、矩阵策略评估 | 2 | [原视频](https://www.bilibili.com/video/BV1nV411k7ve/?p=1) |
| `BV1nV411k7ve_p2_manuscript.md` | 迭代策略评估 | 2 | [原视频](https://www.bilibili.com/video/BV1nV411k7ve/?p=2) |
| `BV1nV411k7ve_p3_manuscript.md` | 策略改进定理 | 2 | [原视频](https://www.bilibili.com/video/BV1nV411k7ve/?p=3) |
| `BV1nV411k7ve_p4_manuscript.md` | 贪心改进与策略迭代 | 2 | [原视频](https://www.bilibili.com/video/BV1nV411k7ve/?p=4) |
| `BV1nV411k7ve_p5_manuscript.md` | 价值迭代与广义策略迭代 | 2 | [原视频](https://www.bilibili.com/video/BV1nV411k7ve/?p=5) |
| `BV1rF411J7Mw_p1_manuscript.md` | MC 前情回顾 | 2–3 | [原视频](https://www.bilibili.com/video/BV1rF411J7Mw/?p=1) |
| `BV1vm4y1Z7Ce_p1_manuscript.md` | MC 策略评估 | 3 | [原视频](https://www.bilibili.com/video/BV1vm4y1Z7Ce/?p=1) |
| `BV1N5411o7QD_p1_manuscript.md` | Exploring Starts MC 控制 | 3 | [原视频](https://www.bilibili.com/video/BV1N5411o7QD/?p=1) |
| `BV1bS4y1C75M_p1_manuscript.md` | On-policy 与 off-policy | 3–4 | [原视频](https://www.bilibili.com/video/BV1bS4y1C75M/?p=1) |
| `BV1EZ4y1R7r4_p1_manuscript.md` | 异策略 MC 评估 | 4 | [原视频](https://www.bilibili.com/video/BV1EZ4y1R7r4/?p=1) |
| `BV1sS4y1C7tR_p1_manuscript.md` | 异策略 MC 评估与控制 | 3–4 | [原视频](https://www.bilibili.com/video/BV1sS4y1C7tR/?p=1) |
| `BV1wS4y1F7zn_p1_manuscript.md` | TD 策略评估 | 3 | [原视频](https://www.bilibili.com/video/BV1wS4y1F7zn/?p=1) |
| `BV1BS4y1r7cm_p1_manuscript.md` | SARSA | 3 | [原视频](https://www.bilibili.com/video/BV1BS4y1r7cm/?p=1) |
| `BV1cZ4y1C7Ma_p1_manuscript.md` | Q-learning | 3、6 | [原视频](https://www.bilibili.com/video/BV1cZ4y1C7Ma/?p=1) |
| `BV15L411T7LM_p1_manuscript.md` | Expected SARSA | 3 | [原视频](https://www.bilibili.com/video/BV15L411T7LM/?p=1) |
| `BV1MS4y1r7ta_p1_manuscript.md` | 策略近似 | 7 | [原视频](https://www.bilibili.com/video/BV1MS4y1r7ta/?p=1) |
| `BV18u411Q76q_p1_manuscript.md` | 策略梯度定理 | 7 | [原视频](https://www.bilibili.com/video/BV18u411Q76q/?p=1) |
| `BV1xb4y1W7Ye_p1_manuscript.md` | REINFORCE | 7 | [原视频](https://www.bilibili.com/video/BV1xb4y1W7Ye/?p=1) |
| `BV1RF411x7oS_p1_manuscript.md` | REINFORCE baseline 与 Actor–Critic | 7–8 | [原视频](https://www.bilibili.com/video/BV1RF411x7oS/?p=1) |
| `BV1yT4y1U78Z_p1_manuscript.md` | Dyna Architecture | 13 | [原视频](https://www.bilibili.com/video/BV1yT4y1U78Z/?p=1) |
| `BV1ar4y1p7ES_p1_manuscript.md` | 规划算力聚焦 | 13 | [原视频](https://www.bilibili.com/video/BV1ar4y1p7ES/?p=1) |
| `BV1cY4y1i785_p1_manuscript.md` | 决策时规划 | 13 | [原视频](https://www.bilibili.com/video/BV1cY4y1i785/?p=1) |
| `BV1s5411D7JT_p1_manuscript.md` | MCTS | 13 | [原视频](https://www.bilibili.com/video/BV1s5411D7JT/?p=1) |

### 8.2 CS285：19 份

| 讲次 | 文件 | 核心主题 | 对应章 | 官方讲义 |
|---|---|---|---|---|
| L1 | `yt_DD8APgTEix4_manuscript.md` | 课程概览 | 1 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-1.pdf) |
| L2 | `yt_yatA09E0J00_manuscript.md` | 行为克隆 | 12 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-2.pdf) |
| L3 | `yt_AdiI3l2hZHI_manuscript.md` | 行为克隆续、策略表示 | 12、15 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-3.pdf) |
| L4 | `yt_FcpIul7rAEE_manuscript.md` | RL 基础 | 1–2 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-4.pdf) |
| L5 | `yt_S0D9REIVdg4_manuscript.md` | 策略梯度 | 7 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-5.pdf) |
| L6 | `yt_MzIWiNzrCvw_manuscript.md` | Actor–Critic | 8 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-6.pdf) |
| L7 | `yt_PCOyNjwyFvk_manuscript.md` | 基于价值的 RL | 5–6 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-7.pdf) |
| L8 | `yt_lQaVa53pS-Q_manuscript.md` | Q-learning 实践 | 6、11 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-8.pdf) |
| L9 | `yt_xtZe3ulf6aM_manuscript.md` | 异策略策略梯度 / 高级 PG（一） | 4、9 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-9.pdf) |
| L10 | `yt_m7IU5KBS4sw_manuscript.md` | 高级 PG（二） | 9 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-10.pdf) |
| L11 | `yt_62V4ailxwEs_manuscript.md` | 变分推断 | 10、数学附录 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-11.pdf) |
| L12 | `yt_998Zp-fHniU_manuscript.md` | RL 中的变分推断 | 10、13 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-12.pdf) |
| L13 | `yt_H4jYNHZy8GQ_manuscript.md` | 控制即推断 | 10–11、16 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-13.pdf) |
| L14 | `yt_dlpeF1--e0E_manuscript.md` | 序列与 LLM RL | 16–18 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-14.pdf) |
| L15 | `yt_WRdDOzVNN8I_manuscript.md` | 模型式 RL 基础 | 13 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-15.pdf) |
| L16 | `yt_fgSHHNhoLDs_manuscript.md` | 模型式 RL 算法 | 13 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-16.pdf) |
| L17 | `yt_u2Ug046R0xk_manuscript.md` | 离线 RL 基础 | 14 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-17.pdf) |
| L18 | `yt_XVwSLpXEFjE_manuscript.md` | 离线 RL 算法 | 14–15 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-18.pdf) |
| L19 | `yt_tHq2gcdtumQ_manuscript.md` | 探索 | 19 | [PDF](https://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-19.pdf) |

## 9. 后续正文的材料使用顺序

1. 第 1–4 章：白板 MDP / DP / MC / TD 为推导主线，CS285 L4 与 L20 核对设定和结论边界。先写价值函数、目标策略、Bellman 算子和采样估计的关系。
2. 第 5–11 章：L5–13 为主，白板 PG 为辅助；以 PPO、SAC 两条完整训练流程贯通。n-step、λ-return、GAE 与理论反例按官方讲义和数学定义补写，不假定每项都有独立白板转录。
3. 第 12–18 章：L2–3、L14–18 为主，白板规划系列补 Dyna / MCTS；按问题组织 BC、模型、离线、奖励与 LLM 内容。
4. 第 19–22 章：L19 转录与本文件 L20、L23–25 补充结合；L21–22 的检查题随各章完成后使用。

每章来源条目建议保存“文件名/讲次、时间戳或 PDF 页码、原公式、统一后的记号、条件说明”。缺失的白板截图若后续获得，可据此定点复核；当前框架和缺课基础补充可以继续推进。
