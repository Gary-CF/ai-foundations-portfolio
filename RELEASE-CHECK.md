# 四本数学笔记的历史发布验收记录

> 此记录只对应原四本数学笔记，不覆盖后加入的三套机器学习笔记。当前七本书接入说明见 [REPOSITORY-CHECK.md](REPOSITORY-CHECK.md)。

验收日期：2026-09-19。状态：四本 PDF 及 HTML 的本次技术验收通过；未执行 commit、push、PR 或网站发布。数学检查为定向核验，不表示全书每个推导均已逐式证明。

## 仓库起点与修改保留

- 仓库根：`ai-foundations-portfolio`；分支 `main`。检查仓库及适用祖先目录，未发现 `AGENTS.md`。
- `git fetch origin` 成功；本地 HEAD 为 `03dab54478b939a97d8c3b7fe0b7028f171bcbf1`，远端 `origin/main` 为 `3ec8a72eb230d1e478f0798e5cd0f04316b79464`，本地领先 6 个提交、落后 0 个。未合并或变基。
- 开始时暂存区为空；工作区有 9 个已修改文件，另有未跟踪的概率统计 `.gitignore` 和随机过程目录。结束时暂存区仍为空。
- 两篇已修改前言的原文完整保留；凸优化七篇已有扩写与任务开始快照逐字节一致。随机过程开始时已经采用稳定目录名，未执行目录改名或覆盖合并。
- 确认并备份清理 48 个 `[ZoneTransfer]` 元数据文件；忽略规则改为 `*Zone.Identifier`。原 `_draft/`、课程截图及转录均未纳入公开文件。

## 修复内容

1. 两本优化书基础配置原本没有中文字体或 `ctex`；只有激活 `pdf` profile 才合并原中文头部。现将 Noto CJK 字体写入默认 PDF 配置，由 Pandoc/XeLaTeX 加载中文支持；profile 只选择 `_pdf/`。清除未使用且与 `unicode-math` 出现加载顺序告警的额外宏包。随机过程也采用现有环境可运行的 `scrreprt` + Noto CJK 路线。
2. 两本优化书的附录改入 `book.appendices`，PDF/HTML 均按字母编号；扩大目录三位数页码区域，消除溢出。已检查手写正文提示及显式引用，无需替换原本正确的正文编号。
3. Freedman 改为确定阈值联合事件；写清鞅差、平方可积、单步上界、累计条件方差与固定时刻条件。两本集中附录对齐，并给出确定方差上界下正确的二次方程反演阈值。
4. Exp3 明确 oblivious adversary 与动作采样顺序，解释固定最佳比较臂后再取期望；自适应对手只保留固定 comparator 界及证明范围说明。相邻下界补齐 `2 ≤ K ≤ T` 条件（Bandit Algorithms Exercise 15.4）。概率统计相关信息流段落同时区分可测的动作分布与新采样动作。
5. 概率统计知识图谱仅将 Ch8 原有四段纵向流程改为横向，保留全部标签及整个 Ch9；消除孤立尾行。集中工具表前添加仅对 PDF 生效的分页，消除重复表头。
6. 根 README 改为四本笔记阅读表；子 README 去除压缩包交付和个人路径描述。公开来源映射见 [REFERENCES.md](REFERENCES.md)，许可说明见 [LICENSE-SCOPE.md](LICENSE-SCOPE.md)。没有改变任何现有许可证。

## 环境与实际命令

- WSL Ubuntu；Quarto 1.10.18；现有用户级 TinyTeX / XeTeX (TeX Live 2026)。
- 已有 Noto Serif CJK SC、Noto Sans CJK SC、Noto Sans Mono CJK SC；Poppler 用于文字、字体与页面渲染，现有 Pillow 用于缩略图。
- 浏览器抽查使用已安装 Chrome 与应用提供的 Playwright，未新建或改动 Conda/Python 环境；本次无需安装构建依赖。

在仓库根目录实际运行：

```bash
python3 scripts/release.py
python3 scripts/release.py --publish .release-build/run-upu52vvd
```

最终隔离目录为 `.release-build/run-upu52vvd/`。脚本在每个项目快照中实际执行：

```bash
quarto render --to pdf --output-dir _pdf --debug
quarto render --to html --output-dir _book --debug
```

另外在独立副本 `.release-build/profile-check/` 中实测凸优化：

```bash
quarto render --profile pdf --to pdf --debug
```

显式 profile 构建的提取正文与默认 PDF 构建相同。通过 `quarto inspect` 核对默认与 profile 的 PDF 格式配置相同，输出目录分别为 `_book` 和 `_pdf`；因此不启用 profile 时仍须用 `--output-dir _pdf` 保持目录分离。随机过程备用 `pdf,portable` 配置本次未重新验收。

## 发布产物

| 文件 | 页数 | SHA-256 |
|---|---:|---|
| [pdfs/convex-optimization-toolbox.pdf](pdfs/convex-optimization-toolbox.pdf) | 169 | `55e61400c1e3ba4335d39dbe4550872312b139fcb39cf98cb62f1a100ba65d41` |
| [pdfs/advanced-optimization-toolbox.pdf](pdfs/advanced-optimization-toolbox.pdf) | 84 | `84b095a1ca959bf3c624815c38c67fc0a784ed8fc7263a0c7c72d5ce10044c7d` |
| [pdfs/stochastic-processes-toolbox.pdf](pdfs/stochastic-processes-toolbox.pdf) | 52 | `f162ec4fe3b04e65573939b36893f7e9edba71d830796e3f461f8a74755cc4ab` |
| [mathematical-foundations/probability-statistics/probability-statistics-notes.pdf](mathematical-foundations/probability-statistics/probability-statistics-notes.pdf) | 101 | `961cede8d324fe17f7f1f8e03aab3ac6ab3d244830f13e82d5289b52eebc6453` |

上述四个文件均与隔离构建产物逐字节一致，版本清单另见 [pdfs/manifest.json](pdfs/manifest.json)。概率统计有实际正文和分页变化，因此更新原公开路径；不是只因文件时间变化替换。

## 实际检查及证据

- 四个项目共 57 个导航源文件全部存在；358 个显式标签无重复，143 处显式引用全部可解析。57 个生成 HTML 页面的本地资源、链接与锚点检查无缺失；根与子 README、参考资料及验收记录共 59 个本地链接另行通过检查。
- 四本正文中文均可提取；分别提取到 34,899、18,244、22,000、13,973 个汉字（顺序同上）。CJK 正体与粗体嵌入、子集化及 Unicode 映射均为 `yes`。PDF 内部 PostScript 名显示 `Noto…CJKjp`，字体配置及 Fontconfig 实际选择的是 SC 家族的 TTC 字体；已同时检查中文实际字形。
- 最终渲染日志及每本保留的 `index.log`：无 `Missing character`、未定义引用、`Overfull`/`Underfull` 或影响阅读的错误。
- 全部 406 页生成 36 dpi 编号缩略图并巡检；页面边界文字检查无异常。最终只因分页修复变化的概率统计 101 页已重新全部巡检；其他三本最终页面与已检查版本逐像素一致。
- 对四本封面和目录放大检查；代表性正文检查包括：凸优化 pp.10、114、148；高级优化 pp.7、56、73；随机过程 pp.10、16、44、50；概率统计的集中证明、知识图谱与工具表（最终 pp.9、87、91）。检查覆盖中文粗体、长公式、宽表格、附录及异常候选页，未见明显缺字、乱码、裁切、重叠或公式溢出。
- 新前言及数学修正均进入新生成 TeX/PDF/HTML；没有修补旧 PDF。旧工作区 `_book/`、`_pdf/` 和根部生成 TeX 已备份并用本次产物刷新。
- Chrome 实际抽查凸优化第 5 章、高级优化第 8 章、随机过程条件高斯章、概率统计鞅附录；分别渲染 241、88、135 个 MathJax 公式及 139 个 MathML 公式，均无公式错误和页面脚本错误。交叉引用或目录点击到达对应锚点。
- 发布文件不被 Git 忽略；构建目录、`.quarto/`、根部生成 TeX、临时构建快照、Windows 元数据及原始资料仍被忽略。现有暂存区未变动。另实测缺少完成清单的目录被发布脚本拒绝，四本公开 PDF 哈希均未改变。

本地详细日志、页面图像、浏览器记录与完成清单保留在 `.release-build/run-upu52vvd/`；原始工作区补丁与源文件备份在 `.release-build/baseline/`；旧生成文件与旧概率统计 PDF 在 `.release-build/previous-generated/`。这些目录均不提交。

## 限制与作者待决定事项

- 技术上没有阻碍本次提交的已知问题；这不是对全部数学推导或全部浏览器环境的完整证明/兼容性保证。未展开新的数学专题。
- 两组优化课程、四份 AOPT 报告、OCO Warmup 博客，以及部分随机过程视频的完整身份/授权仍待补。Bilibili 页面本次受 412/不可访问限制，不能标为视频可播放检查通过；已保留原登记链接并明确核验范围。这不影响本次构建，但公开归属信息仍不完整。
- 随机过程正式开放许可尚未确定；本次仅准备文件，不能把它声明为已获 MIT 或 CC BY 授权的开放许可发布。根 CC BY 4.0 与优化子目录 MIT 的现有范围是否统一或细分，需作者决定；没有擅自重授许可。
- 普通沙箱进程、内置浏览器和图像工具曾因 `setup refresh` 故障无法启动，已用获批命令及本机现有工具完成替代验收。一次可能截断知识图谱的编辑被自动审批拒绝，后改为原文精确匹配且断言保留后文的局部替换，成功执行；没有因此遗留未完成修复。

## 建议提交范围

提交本次源配置、正文修正、README、根 `.gitignore`、`REFERENCES.md`、`LICENSE-SCOPE.md`、本记录、`scripts/release.py`、`pdfs/` 以及更新后的概率统计 PDF；包括用户原有前言和凸优化七篇扩写。随机过程应提交稳定目录内的正文、配置、样式、`tex/portable.tex`、README、现有 LICENSE 状态文件及 `.gitignore`，不要提交 `_draft/`、原始截图、元数据或生成缓存。

建议 commit message：`docs: fix Chinese PDF builds and prepare validated notes for release`
