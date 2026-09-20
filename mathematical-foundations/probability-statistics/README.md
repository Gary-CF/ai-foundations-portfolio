# 概率论与数理统计工具箱

随机事件、随机变量、分布、数字特征、集中与极限定理、统计基础和参数估计；附录为鞅与自适应集中、Markov 链。

## 阅读与范围

- [前言与阅读路线](index.qmd)、[正文源文件](chapters/)、[附录](appendices/)。
- [完整 PDF](probability-statistics-notes.pdf)。
- [公开参考资料与待补来源](../../REFERENCES.md)、[许可范围](../../LICENSE-SCOPE.md)、[发布验收记录](../../RELEASE-CHECK.md)。

主线与两篇附录已有稿，持续校对中；并非逐式证明验收。

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
