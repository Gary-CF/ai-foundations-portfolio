# AI Foundations Portfolio

面向复习与查阅的中文学习笔记，保留核心条件、关键推导和常用工具。以下四本已有正文，均为持续校对中的学习稿；本次验收范围和限制见 [发布验收记录](RELEASE-CHECK.md)。

| 笔记 | 内容 | 源文件入口 | PDF | 状态 |
|---|---|---|---|---|
| 概率论与数理统计工具箱 | 概率、估计、集中、鞅与 Markov 链 | [目录与前言](mathematical-foundations/probability-statistics/index.qmd) | [阅读](mathematical-foundations/probability-statistics/probability-statistics-notes.pdf) | 主线及两篇附录已有稿 |
| 凸优化工具箱 | 凸几何、对偶、KKT、一阶与复合算法 | [目录与前言](mathematical-foundations/convex-optimization-toolbox/index.qmd) | [阅读](pdfs/convex-optimization-toolbox.pdf) | 9 章、5 篇附录；持续校对 |
| 高级优化工具箱 | 在线优化、自适应方法与 Bandit | [目录与前言](mathematical-foundations/advanced-optimization-toolbox/index.qmd) | [阅读](pdfs/advanced-optimization-toolbox.pdf) | 10 章、4 篇附录；研究接口未扩写 |
| 随机过程工具箱 | 高斯、泊松、Markov 链与鞅 | [阅读说明](mathematical-foundations/stochastic-processes-toolbox/index.qmd) | [阅读](pdfs/stochastic-processes-toolbox.pdf) | v0.4，10 章、3 篇附录；许可待确认 |

矩阵、向量与张量微积分在凸优化的[数学预备工具附录](mathematical-foundations/convex-optimization-toolbox/appendices/mathematical-toolbox.qmd)中，并非独立完成的项目。
## 构建与更新 PDF

已验收环境与命令见 [发布验收记录](RELEASE-CHECK.md)。需要 Quarto、XeLaTeX（TeX Live / TinyTeX）、Noto Serif/Sans CJK SC 字体、Python 3 和 Poppler（`pdfinfo`、`pdftotext`、`pdffonts`）。脚本仅用 Python 标准库，不修改 Conda 环境。

在仓库根目录运行：

```bash
python3 scripts/release.py
# 完成日志和页面检查后，将上一条命令输出的目录代入：
python3 scripts/release.py --publish .release-build/run-实际目录
```

脚本复制当前工作区源文件（包括未提交和未跟踪的正文），排除旧构建产物，在全新目录构建四本 PDF 和 HTML。四本全部成功并通过基础文字、字体检查后才写入完成清单；发布步骤验证源文件和产物哈希。失败目录不能发布，源文件变化后必须重建。基础检查不能代替页面巡检；提交前还须人工检查缩略图和重点页面。

单本书可在相应子目录运行：

```bash
quarto render --to html
quarto render --profile pdf --to pdf
# 不使用 profile 时，中文配置仍有效；显式指定目录保持 HTML/PDF 分离：
quarto render --to pdf --output-dir _pdf
```

HTML 使用 `_book/`，PDF 使用 `_pdf/`；不应直接运行未指定格式的多格式构建来更新发布文件。生成目录、`.quarto/` 和 `_draft/` 不提交。公开 PDF 与哈希清单位于表中路径和 [pdfs/manifest.json](pdfs/manifest.json)。

## 来源与许可

见 [参考资料与待补来源](REFERENCES.md) 和 [许可范围说明](LICENSE-SCOPE.md)。原始课程截图、转录和整个 `_draft/` 不公开；现有许可证保持原样，随机过程尚未授予开放许可。
