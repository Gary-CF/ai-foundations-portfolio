# 经典统计学习笔记

Classical Statistical Learning Notes

三部分、10 章正文、MCMC 附录。保留主线纸质/电子笔记的推导，统一符号、修正实质性错误，并重绘数学插图。决策树和 AdaBoost 根据已确认提纲补写；详细来源和纠错见 `整理记录.md`。

## 文件

| 路径 | 用途 |
|---|---|
| `_quarto.yml` | 书名、分部、章节顺序、输出格式 |
| `index.qmd` | 前言、阅读路线、符号约定 |
| `chapters/01-*.qmd` 至 `10-*.qmd` | 十章正文 |
| `appendices/a-mcmc.qmd` | MCMC 附录 |
| `images/*.png` | 正文插图，兼容 HTML/PDF |
| `images/*.svg` | 对应矢量图 |
| `scripts/draw_figures.py` | 重绘全部插图，依赖 numpy、matplotlib |
| `整理记录.md` | 材料覆盖、补充范围、主要纠错 |
| `验证记录.md` | 本次实际渲染和检查结果 |
| `preview/` | 本地旧预览，不提交；仓库阅读入口见首页 |

## 章节

1. 线性模型统一视角（原 0、1 合并）
2. 支持向量机与核方法
3. 主成分分析
4. 决策树
5. 提升方法与集成学习
6. 指数族与最大熵
7. EM 算法与高斯混合模型
8. 概率图模型
9. 隐马尔可夫模型
10. 条件随机场

附录 A：MCMC。

## 渲染

安装 Quarto。PDF 使用 XeLaTeX，需 ctex 与 Fandol 字体；可在尚未安装 TeX 的环境中运行 `quarto install tinytex`。正文没有代码执行依赖；只重绘插图时才需要 Python 包。

在当前目录运行：

```bash
quarto preview --to html
quarto render --to html
quarto render --to pdf --output-dir _pdf
```

HTML 默认到 `_book/`，PDF 上述命令到 `_pdf/`。Quarto 官方结构说明：[Book Structure](https://quarto.org/docs/books/book-structure.html)。

日常修改 `.qmd`，不要直接修改生成的 HTML/PDF。章号、节号、图号由 Quarto 产生；修改顺序应同时修改 `_quarto.yml`。

## 仓库集成

本书已接入[机器学习基础目录](../README.md)。统一构建与发布从[仓库根目录](../../README.md)运行 `python3 scripts/release.py`；单本预览仍在本目录进行。PDF profile 可使用 `quarto render --profile pdf --to pdf`。

`preview/` 是本地交付预览，不提交 Git，也不是 GitHub 的阅读入口。正式 PDF 在根目录 `pdfs/`，发布前由根 README 标记为待构建。HTML 的 MathJax 需要网络。
