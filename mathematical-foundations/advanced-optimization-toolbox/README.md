# Advanced Optimization Toolbox

一份面向在线学习、Bandit 与自适应智能研究路线的高级优化 Quarto Book。

## 项目定位

本项目承接《凸优化工具箱》，重点覆盖：

- 在线凸优化与遗憾分析；
- OGD、Hedge、ONS、OMD 与 FTRL；
- 自适应和乐观在线优化；
- online-to-batch 与在线视角下的加速；
- 对抗、随机与线性 Bandit；
- universal、one-pass 与鲁棒 Bandit 的研究接口。

本项目保持工具箱性质：重视条件、关键推导、几何视角和使用边界，不逐页复刻课件，也不将研究报告扩写成论文合集。

## 当前状态

当前已完成：

- 17 份课件与一篇在线博客的材料盘点；
- 主线、附录和内容边界定稿；
- P0/P1/P2 分级；
- 第 2–3 章忠实电子化样章与风格校准；
- 10 个主线章节的完整工具箱初稿；
- 集中工具、证明模板、研究接口和统一记号附录；
- 章节交叉引用、公式定界符和隐藏字符检查。

当前版本已经覆盖从一阶分析、全信息在线优化到对抗、随机与线性 Bandit 的完整主线。Universal、one-pass、重尾 Bandit 与强化学习相关内容仍保持研究接口深度，等待后续专题材料或研究需要再展开。

## 项目结构

```text
.
├── _quarto.yml
├── _quarto-pdf.yml
├── index.qmd
├── chapters/
├── appendices/
├── images/
├── _draft/
├── README.md
└── LICENSE
```

## 渲染

HTML：

```bash
quarto preview
```

或：

```bash
quarto render --to html
```

PDF：

```bash
quarto render --profile pdf --to pdf
```

HTML 输出位于 `_book/`，PDF 输出位于 `_pdf/`，两者均不纳入版本管理。

## 写作原则

- 先交代问题和信息模型，再进入公式；
- 定理紧邻写清成立条件；
- 每个算法保留一条主证明链；
- 几何解释必须服务于算法或遗憾分析；
- 明确区分期望界、高概率界和任意序列界；
- 研究接口以可迁移思想为主，不追逐全部变体。
