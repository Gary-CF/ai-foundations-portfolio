# 深度强化学习笔记

Quarto Book：七篇、22 章正文、4 个附录。以 CS285 Spring 2026 与强化学习白板推导为材料，按知识依赖重写正文，包含核心推导、小例子、算法比较、自测答案和来源索引。

## 阅读入口

正文入口为 [index.qmd](index.qmd)，正式 PDF 发布状态见[仓库首页](../../README.md)。`preview/` 是原交付包的本地预览，不提交 Git。

本地运行 `quarto preview --to html` 可预览网页；离线公式资源由构建钩子复制到输出站点。

## 修改与构建

在本目录编辑 `.qmd`，再运行：

```bash
quarto preview --to html
quarto render --to html
quarto render --to pdf --output-dir _pdf
```

一次完整重建可运行 `python3 scripts/build.py`。该脚本分别构建 PDF 和 HTML，并在切换格式时清理生成缓存，避免跨格式的引用元数据残留；不会删除 QMD 正文。

需要 Quarto CLI 与 Python 3（用于 HTML 公式资源本地化钩子）。PDF 需要 XeLaTeX、ctex、xeCJK、zhnumber、Fandol 字体以及相匹配的 TeX Live 包版本。可安装 TeX Live 中文支持，或按 Quarto 官方指南安装 TinyTeX。纯正文不执行 Python/R/Jupyter。

`vendor/katex` 固定为 KaTeX 0.16.22，保留其 MIT LICENSE；构建后脚本将公式 JS/CSS/fonts 复制到站点内，使阅读不依赖 CDN。当前 CSS 沿用参考深度学习笔记的简洁风格，PDF 与统计学习笔记同用 ctexbook。

## 文件职责

| 路径 | 职责 |
|---|---|
| `_quarto.yml` | 七篇目录、自动编号、HTML/PDF 配置 |
| `index.qmd` | 前言、层级和阅读路线 |
| `chapters/01-*.qmd` 至 `22-*.qmd` | 完整正文 |
| `appendices/` | 符号、速查、来源覆盖、校订记录 |
| `references.bib` | 核心方法参考文献 |
| `source-ledger.json` / `.csv` | 47 份转录与 6 份补充讲义的文件标识、链接和哈希 |
| `images/` | PNG 插图与对应 SVG |
| `scripts/draw_figures.py` | 重绘数学示意图，需要 numpy、matplotlib |
| `scripts/localize_html_math.py` | Quarto 自动调用的 HTML 公式资源本地化 |
| `experiments/toy_mdp.py` | 无第三方依赖的小例子核对 |
| `experiments/experiment-template.md` | 后续课程实验记录模板 |
| `docs/` | 前期框架、材料校订、实际验证结果 |
| `preview/` | 本次交付的阅读版本，属于构建产物 |

## 本轮内容边界

22 章既定范围都有正文。L20–25 以官方讲义补齐；L21–22 的复习内容分配到对应章节与自测。高阶理论和大型算法系统按 C 级标出，不声称穷尽研究方向。没有把转录原稿逐句复制；原视频口语与缺失截图仍有未逐字核验的部分。

附带脚本只验证书中小例子的数值关系，不是完整深度 RL 训练框架，也不代表已完成 CS285 作业。4 张图均为数学示意，没有虚构训练曲线。

## 接入已有仓库

本目录是独立 Quarto 子项目，从本目录执行构建即可。提交源码、配置、脚本、插图、文献和来源记录；`_book/`、`_pdf/`、`.quarto/` 与 `preview/` 已列入忽略。统一 PDF 发布使用仓库根目录 `scripts/release.py`；七本全部构建后更新 `pdfs/`。本书的来源台账只有元数据、链接和哈希，继续随源码保留。PDF profile 可使用 `quarto render --profile pdf --to pdf`。

结构依据：[Quarto Book](https://quarto.org/docs/books/book-structure.html)。内容来源见附录与课程官方入口，原材料的权利归属保持不变。
