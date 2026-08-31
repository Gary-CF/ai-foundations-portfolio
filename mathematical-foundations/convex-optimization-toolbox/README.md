# Convex Optimization Toolbox

一份面向人工智能与机器学习学习者的凸优化 Quarto Book，覆盖凸几何、凸函数、问题建模、Lagrange 对偶、KKT 条件、一阶方法与典型机器学习应用。

## 当前状态

当前版本完成：

- 全书目录定稿；
- 四页纸质主线的忠实电子化；
- 十二份课件支撑的 P0 主线补全；
- 第 3 章样章校准及全书语言、推导和几何解释标准统一；
- 凸集、凸函数、问题变换、对偶与 KKT、一阶算法和机器学习应用整理；
- 数学预备工具、材料映射、纠错记录和 P0/P1/P2 边界登记。

Newton、近端、增广 Lagrangian、ADMM、锥规划等 P1 内容尚未系统扩写。

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
quarto render --to html
```

PDF：

```bash
quarto render --profile pdf --to pdf
```

HTML 输出位于 `_book/`，PDF 输出位于 `_pdf/`，两者均不纳入版本管理。

## 写作原则

- 先说明问题与直觉，再给出形式化定义；
- 定理与收敛结论紧邻写明成立条件；
- 保留揭示结构的关键推导，省略重复代数；
- 几何解释服务于理解，不作为装饰；
- 保持工具箱定位，不扩写成厚重教材。
