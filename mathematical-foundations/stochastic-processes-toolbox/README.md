# 随机过程工具箱

短预备章、高斯、泊松、Markov 链与鞅，共 10 章；三个附录为共用工具、技术证明与序贯检验。

## 阅读与范围

- [前言与阅读路线](index.qmd)、[正文源文件](chapters/)、[附录](appendices/)。
- [完整 PDF](../../pdfs/stochastic-processes-toolbox.pdf)。
- [公开参考资料与待补来源](../../REFERENCES.md)、[许可范围](../../LICENSE-SCOPE.md)、[发布验收记录](../../RELEASE-CHECK.md)。

v0.4（P0 + P1 稿），P2 未展开；正式开放许可待作者确认。稳定目录名不带版本号。

## 构建

在本子目录执行：

```bash
quarto render --to html
quarto render --profile pdf --to pdf
# 不使用 profile 也有中文支持；保持输出目录分离：
quarto render --to pdf --output-dir _pdf
```

依赖 Quarto、XeLaTeX（TeX Live / TinyTeX）及 Noto Serif CJK SC、Noto Sans CJK SC、Noto Sans Mono CJK SC 字体。基础配置负责中文，`pdf` profile 只指定 `_pdf/`。HTML 输出 `_book/`，从 `_book/index.html` 开始阅读。HTML 中 MathJax 的网络资源需要联网；概率统计使用 MathML。构建目录与缓存不提交。

仓库根目录的 `python3 scripts/release.py` 在新目录复制当前全部源文件并构建四本书；验收后用 `--publish` 更新公开 PDF。实际验证结果以[本次记录](../../RELEASE-CHECK.md)为准。

`_quarto-portable.yml` 与 `tex/portable.tex` 保留为备用排版配置，可用 `--profile pdf,portable`；本次发布以基础配置为准，备用路线未重新验收。原始转录、截图和 `_draft/` 不公开。许可状态见 [LICENSE](LICENSE)。
