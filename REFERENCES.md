# 参考资料与来源映射

本页公开可确认的书目、链接与必要映射，不发布原始课程截图、转录或内部工作记录。课程编号是材料标记，不代表已经识别了课程身份。

## 本次定向数学核验

- Joel A. Tropp, *Freedman’s Inequality for Matrix Martingales* (2011), [arXiv:1101.3039](https://arxiv.org/pdf/1101.3039)，Theorem 1.1（标量 Freedman）。用于高级优化集中附录及概率统计鞅附录的确定阈值联合事件；高概率推论另要求确定方差上界。
- Tor Lattimore and Csaba Szepesvári, *Bandit Algorithms* (2020), [作者提供的全文](https://tor-lattimore.com/downloads/book/book.pdf)，§28.5 Notes 第 9 点（书内 pp.341–342）。用于高级优化第 8 章：区分固定比较臂的期望差和 non-oblivious 损失下的事后最优臂期望遗憾。Exp3 基本背景另见该书第 11 章。

## 优化课程材料：身份待补

两组优化材料的本地记录只保存 Lecture 编号与主题，未提供足以核实的课程全名、授课教师及公开链接；不能将它们猜测归于某个学校或作者。

| 材料标记 | 本仓库去向 |
|---|---|
| 凸优化 Lecture 1、6 | 凸优化第 1 章：优化概览 |
| 凸优化 Lecture 2–3 | 第 2 章：凸集 |
| 凸优化 Lecture 4–6、11 | 第 3、4、6 章：凸性、拟凸性、光滑性 |
| 凸优化 Lecture 5、8–9 | 第 5 章：对偶、Slater、KKT |
| 凸优化 Lecture 9、11–12 | 第 6–8 章及进阶算法附录 |
| 凸优化 Lecture 7、10 | 第 9 章：模型应用 |
| 凸优化 Lecture 3、5、7、9 | 锥规划附录 |
| 高级优化 Lecture 1–4 | 第 1 章、集中工具及证明模板；第 7 章加速对照 |
| 高级优化 Lecture 5 | 第 2–3 章：OCO、OGD、online-to-batch |
| 高级优化 Lecture 6–7 | 第 4–5 章：Hedge、ONS、OMD、FTRL |
| 高级优化 Lecture 8–9 | 第 6–7 章：自适应、optimism、加速 |
| 高级优化 Lecture 10 | 第 8 章：Exp3 与 BCO |
| 高级优化 Lecture 11–12 | 第 9–10 章：随机与线性 Bandit |
| AOPT_GLB、AOPT_Holder、AOPT_HvtLB、AOPT_Universal | 高级优化研究接口附录；报告作者、题名和链接待补 |

“Online Convex Optimization Warmup”博客的作者与原始链接也待补，仅登记为直觉材料，不作为定理的权威来源。概率统计主线尚缺系统书目记录，待作者补齐。

## 随机过程

| 材料 | 作者 / 身份 | 章节映射及说明 |
|---|---|---|
| [MIT 6.262 Discrete Stochastic Processes, Spring 2011](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/) | Robert Gallager，课程身份已由官方页核实 | 第 23–24 讲用于鞅与停止，第 24–25 讲用于收敛，第 25 讲用于长期行为，第 23 讲用于序贯检验附录 |
| [随机过程 2024 张颢老师（放大高清修复）（全集）](https://www.bilibili.com/video/BV11b421E7nh/) | 本地登记标题署名张颢；非官方重传，原始课程机构及授权待核实 | P6–9：联合/条件高斯、高阶矩与低维 Price；P11–14：泊松与条件到达；P14：Markov 引入 |
| [随机过程—2024年版](https://www.bilibili.com/video/BV1m5xTzjEyP/) | 原记录的“第一组”；讲者、机构与原始课程链接待补 | P23–24：Markov 演化；P25–30：状态分类；P28–32：长期行为 |
| Rick Durrett, *Probability: Theory and Examples*, 5th ed. | 作者与书名见原核验记录；[作者教材页](https://sites.math.duke.edu/~rtd/PTE/pte.html) | 第 5 章：可数状态链的条件与返回周期；本次未重做该部分逐式核验 |
| Felix Voigtlaender, *A general version of Price’s theorem* | [arXiv:1710.03576](https://arxiv.org/abs/1710.03576)，作者与题名已核实 | 联合高斯章的低维 Price 定理条件；不扩写广义函数理论 |

待补事项是来源完整性限制，不能用公开视频链接推定转载授权；许可状态另见 [许可范围说明](LICENSE-SCOPE.md)。

链接核验：2026-09-19，Tropp、Bandit Algorithms、MIT OCW、Price 论文和 Durrett 教材页可读取。两个 Bilibili 链接来自原材料登记，本次网页读取分别返回 412 和不可访问，未确认视频当前可播放或转载授权。

## 机器学习基础笔记

下列为已接入笔记内的来源入口；本次仓库接入检查未重新联网核验全部外部链接，也未重做全文数学审稿。

| 笔记 | 来源与校订入口 |
|---|---|
| 经典统计学习 | [整理记录](machine-learning-foundations/classical-statistical-learning/整理记录.md)及各章来源说明 |
| 深度学习与进阶统计学习 | [材料覆盖](machine-learning-foundations/deep-learning-statistical-learning-toolbox/appendices/B-source-coverage.qmd)、[校对边界](machine-learning-foundations/deep-learning-statistical-learning-toolbox/appendices/C-corrections.qmd)；CS229M 二十讲与花书指定七章 |
| 深度强化学习 | [材料覆盖](machine-learning-foundations/deep-reinforcement-learning/appendices/C-source-coverage.qmd)、[参考文献](machine-learning-foundations/deep-reinforcement-learning/references.qmd)；CS285 Spring 2026 与白板推导 |

深度学习公开来源台账保留定位信息，转录摘录只留本地 `_draft/`；强化学习的 JSON/CSV 来源台账为文件标识、课程链接和哈希，可继续作为公开来源索引。
