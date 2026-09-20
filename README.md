# AI Foundations Portfolio

面向复习与查阅的七套中文学习笔记，保留核心条件、关键推导和常用工具。数学基础与机器学习基础分别组织，每本书是独立 Quarto Book，均为持续校对中的学习稿。

| 笔记 | 内容 | 源文件入口 | PDF | 正文范围 |
|---|---|---|---|---|
| 概率论与数理统计工具箱 | 概率、估计、集中与鞅 | [目录与前言](mathematical-foundations/probability-statistics/index.qmd) | <!-- pdf:probability-statistics -->[阅读](pdfs/probability-statistics-notes.pdf)<!-- /pdf --> | 主线与附录已有稿 |
| 凸优化工具箱 | 凸几何、对偶、KKT 与一阶算法 | [目录与前言](mathematical-foundations/convex-optimization-toolbox/index.qmd) | <!-- pdf:convex-optimization-toolbox -->[阅读](pdfs/convex-optimization-toolbox.pdf)<!-- /pdf --> | 9 章、5 附录 |
| 高级优化工具箱 | 在线优化、自适应方法与 Bandit | [目录与前言](mathematical-foundations/advanced-optimization-toolbox/index.qmd) | <!-- pdf:advanced-optimization-toolbox -->[阅读](pdfs/advanced-optimization-toolbox.pdf)<!-- /pdf --> | 10 章、4 附录 |
| 随机过程工具箱 | 高斯、泊松、Markov 链与鞅 | [目录与前言](mathematical-foundations/stochastic-processes-toolbox/index.qmd) | <!-- pdf:stochastic-processes-toolbox -->[阅读](pdfs/stochastic-processes-toolbox.pdf)<!-- /pdf --> | 10 章、3 附录；许可待确认 |
| 经典统计学习笔记 | 线性模型、核方法、集成与概率推断 | [目录与前言](machine-learning-foundations/classical-statistical-learning/index.qmd) | <!-- pdf:classical-statistical-learning -->[阅读](pdfs/classical-statistical-learning.pdf)<!-- /pdf --> | 10 章、MCMC 附录 |
| 深度学习与进阶统计学习工具箱 | 泛化理论、神经网络、训练与隐式偏置 | [目录与前言](machine-learning-foundations/deep-learning-statistical-learning-toolbox/index.qmd) | <!-- pdf:deep-learning-statistical-learning-toolbox -->[阅读](pdfs/deep-learning-statistical-learning-toolbox.pdf)<!-- /pdf --> | 预备章、19 章、4 附录 |
| 深度强化学习笔记 | 价值学习、策略优化、离线 RL 与 LLM | [目录与前言](machine-learning-foundations/deep-reinforcement-learning/index.qmd) | <!-- pdf:deep-reinforcement-learning -->[阅读](pdfs/deep-reinforcement-learning.pdf)<!-- /pdf --> | 22 章、4 附录 |

以上“正文范围”不等于逐式数学审稿或发布验收通过。原四套数学笔记的历史验收见 [RELEASE-CHECK.md](RELEASE-CHECK.md)；新增三套的接入检查与本机验收步骤见 [REPOSITORY-CHECK.md](REPOSITORY-CHECK.md)。发布清单记录的是最近一次发布，不会因添加正文而自动更新。

## 目录与阅读关系

- `mathematical-foundations/`：概率统计、凸优化、高级优化、随机过程。
- [machine-learning-foundations/](machine-learning-foundations/README.md)：经典统计学习、深度学习与进阶统计学习、深度强化学习。
- `pdfs/`：统一的公开 PDF 与 `manifest.json`。
- `scripts/books.json`：七本书的实际路径、输出名及发布目标；目录名无需统一改名。

矩阵、向量与张量微积分见凸优化的[数学预备工具附录](mathematical-foundations/convex-optimization-toolbox/appendices/mathematical-toolbox.qmd)。强化学习中的概率与优化基础可回查数学笔记，神经网络与训练细节可回查深度学习笔记。

## 构建与更新 PDF

需要 Quarto、Python 3、XeLaTeX（TeX Live / TinyTeX）和 Poppler（`pdfinfo`、`pdftotext`、`pdffonts`）。四本数学笔记保留 Noto CJK 配置；三本新笔记保留 ctex/Fandol 配置，因此两套字体及中文宏包都需可用。脚本只使用 Python 标准库，不修改 Conda 环境。

在仓库根目录运行：

```bash
# 快速检查目录、配置与图片路径，不编译
python3 scripts/release.py --check

# 可选：先单独构建一本，定位依赖或排版问题
python3 scripts/release.py --book deep-reinforcement-learning

# 完整构建七本 PDF 和 HTML
python3 scripts/release.py

# 阅读日志、抽查 PDF 页面和 HTML 后，使用上一步打印的真实目录
python3 scripts/release.py --publish .release-build/run-实际目录
```

每本书的 PDF 和 HTML 在不同的干净副本中构建。七本全部成功、源文件保持不变且检查通过后，才允许统一发布。`--publish` 仅更新本地 `pdfs/`、清单及本页 PDF 链接，不执行 Git 提交、推送或网站部署。概率统计的旧 PDF 路径同步保留为兼容副本；其他链接统一指向 `pdfs/`。

子项目中日常预览：

```bash
quarto preview --to html
quarto render --profile pdf --to pdf
```

HTML 位于 `_book/`，PDF 位于 `_pdf/`。统一发布时以根目录脚本的隔离构建结果为准。构建成功与基础检查不能替代页面检查；特别注意长公式、宽表格、中文字体与附录导航。

## 来源、归档与许可

参见 [REFERENCES.md](REFERENCES.md) 与 [LICENSE-SCOPE.md](LICENSE-SCOPE.md)。原始截图、转录和 `_draft/` 不公开；公开来源记录保留定位与链接，深度学习台账中的转录摘录已分离到本地备份。

`_book/`、`_pdf/`、`.quarto/`、`preview/`、旧版 `archive/`、临时构建快照与 Windows 元数据不提交。正文、配置、脚本、插图、来源映射及发布 PDF 可提交。各目录现有许可声明保持不变；第三方 KaTeX 的 MIT LICENSE 随其资源保留。
