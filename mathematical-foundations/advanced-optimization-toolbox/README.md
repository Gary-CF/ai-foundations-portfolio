# 高级优化工具箱

在线凸优化、OGD、Hedge、ONS、OMD/FTRL、自适应与乐观方法、online-to-batch、对抗/随机/线性 Bandit。

## 阅读与范围

- [前言与阅读路线](index.qmd)、[正文源文件](chapters/)、[附录](appendices/)。
- [完整 PDF](../../pdfs/advanced-optimization-toolbox.pdf)。
- [公开参考资料与待补来源](../../REFERENCES.md)、[许可范围](../../LICENSE-SCOPE.md)、[发布验收记录](../../RELEASE-CHECK.md)。

10 个正文章、4 篇附录，持续校对中。Exp3 主证明限定预先固定损失序列；universal、one-pass 与鲁棒 Bandit 保持研究接口深度。

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
