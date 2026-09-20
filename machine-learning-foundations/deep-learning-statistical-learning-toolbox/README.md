# 深度学习与进阶统计学习工具箱

Quarto Book 项目。预备章、十九章正文、四个附录，使用同一套 QMD 输出 HTML 与 PDF。

## 快速开始

在含 `_quarto.yml` 的项目根目录运行：

```bash
# 本地预览 HTML
quarto preview --to html

# 生成 HTML，入口为 _book/index.html
quarto render --to html

# 生成 PDF，保存在独立目录，避免覆盖 HTML 产物
quarto render --to pdf --output-dir _pdf
```

需要 Quarto CLI；纯笔记内容无需 Python、R 或 Jupyter。PDF 需要 XeLaTeX、ctex 与 Fandol 中文字体。可安装完整的 TeX Live，或按 [Quarto PDF 指南](https://quarto.org/docs/output-formats/pdf-basics.html)使用 `quarto install tinytex`。首次 PDF 构建可能需要联网安装 LaTeX 宏包。

Linux 已安装 TeX Live 时，中文支持通常由 `texlive-lang-chinese` 提供。本项目使用随 TeX Live 分发的 Fandol 字体，避免依赖 Windows 专有字体。

## 文件职责

| 路径 | 用途 |
|---|---|
| `_quarto.yml` | 书名、五部分目录、章节顺序、两种输出配置 |
| `index.qmd` | 前言与阅读路线 |
| `chapters/*.qmd` | 预备章和第 1–19 章正文 |
| `appendices/*.qmd` | A 数学速查、B 来源覆盖、C 校对、D 历史验收 |
| `images/` | 后续插图；本次原包没有独立图片 |
| `styles.css` | 简洁 HTML 样式 |
| `source-ledger.json` | 公开逐段定位索引；转录摘录单独本地备份 |
| `docs/migration.md` | 本次迁移说明及验证结果 |
| `archive/v1/` | 本地旧版归档，已忽略；GitHub 不提供此目录 |

## 内容分部

1. 统计学习与泛化基础（第 1–5 章）
2. 神经网络、正则化与训练（第 6–9 章）
3. 非凸优化与可分析模型（第 10–12 章）
4. 隐式偏置与优化噪声（第 13–15 章）
5. 序列、表示学习与实验方法（第 16–19 章）

## 后续如何修改

直接编辑对应 QMD，再运行上面的预览或构建命令。普通正文及附录标题不要手写章号和小节号，Quarto 会自动编号；预备章保留 0、0.1–0.4，并显式取消自动编号，因此正文仍从第 1 章开始。第 13 章原来的小节 1–13 统一显示为 13.1–13.13。

新增章需同步修改 `_quarto.yml` 中的 `book.chapters`；新增附录修改 `book.appendices`。引用章节可用相对 QMD 链接，例如 `[回归中的隐式偏置](chapters/13-implicit-regression.qmd)`（在根目录文件中）。

HTML 为多页面网站，预览和搜索建议用 `quarto preview --to html`，不要只复制一个 HTML 文件。新版不沿用旧版“单 HTML 完全离线”的保证；本地若保留旧版，可从 `archive/v1/book.html` 阅读；该归档不提交 Git。

源码、配置、图片及去除转录摘录的来源记录可提交 Git。`_book/`、`_pdf/`、`.quarto/` 与 `archive/` 已忽略。正式 PDF 由根目录发布脚本更新到 `pdfs/`。许可范围参见根目录 `LICENSE-SCOPE.md`。

## 迁移边界

保留原稿理论内容、公式、来源说明与纠错边界；本次工作是项目架构迁移，不是一次新的全文数学审稿。附录 D 的数值结果和旧版验收数据是历史记录，不代表本次重新运行。

配置依据：[Quarto Book 结构](https://quarto.org/docs/books/book-structure.html)、[PDF 输出](https://quarto.org/docs/output-formats/pdf-basics.html)。

## 仓库集成

统一构建流程见[仓库首页](../../README.md)。公开 `source-ledger.json` 保留段号、时间戳及主题定位；原始转录摘录备份在本地 `_draft/` 中。各章理论正文不因此改动。PDF profile 可使用 `quarto render --profile pdf --to pdf`。
