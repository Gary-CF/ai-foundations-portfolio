# 七套笔记的仓库接入检查

## 已确认的问题与修复

- 根 README 仍称三套机器学习笔记尚未存在；更新为七本书入口与实际正文范围。
- 原发布脚本只构建四本数学笔记；增加 `scripts/books.json` 登记七个实际路径、输出文件名和发布目标。
- 新增三本缺少 PDF profile；补齐仅选择 `_pdf/` 的 profile，不更换各书现有排版方案。
- PDF 检查原先只认名称包含 CJK 的字体；现同时识别 Fandol，强制检查字体嵌入与正文汉字提取，记录显式 Unicode 映射状态；缺少显式映射时提示抽查复制/搜索。
- 原流程在同一目录连续构建 PDF/HTML；改为独立干净副本，避免跨格式缓存和中间文件干扰。
- 统一发布到 `pdfs/`，概率统计旧路径保留同步兼容副本；只有完整构建成功后才更新清单与新 PDF 阅读链接。
- 增加预览、归档、中间文件忽略规则；不删除本地预览或归档，不修改 Git 暂存区。
- 深度学习来源台账含转录摘录，原样备份到本地 `_draft/` 后，只在公开副本中移除 excerpt 字段；强化学习元数据台账保持原样。
- 补齐来源与许可范围说明，原四本验收报告明确标为历史记录。没有新增或改变许可证。

- 修复强化学习参考文献页到来源附录的跨页面链接。

## 本次验证范围

检查了七本书的配置与章节清单、新三本的 65 个导航源文件、原四本 PDF 与已有清单的哈希对应关系。三本新书已用 Quarto 1.7.32 实际构建 65 个 HTML 页面，并检查内部链接、锚点与本地资源。发布脚本的五项回归检查通过：完整发布与兼容路径、部分构建拒绝、源码变更拒绝、产物变更拒绝、快照排除规则。回归检查用已有真实 PDF 作为测试样本模拟构建，不等同于七本重新编译。

本次不重新编译并巡检全部七本 PDF。根 README 中新书 PDF 状态在完整构建发布前保持“待统一构建发布”。原书中的数值实验和数学证明未重新核验；详细执行结果以交付说明和本机新构建日志为准。

## 本机验收

```bash
python3 scripts/release.py --check
python3 scripts/release.py
# 检查上一步目录中的日志，以及 work/pdf/ 和 work/html/ 下的产物
python3 scripts/release.py --publish .release-build/run-实际目录
git diff --stat
git status --short
```

新构建使用现有 Noto CJK 和 ctex/Fandol 两套字体配置。若单本报错，可用 `--book` 指定 `scripts/books.json` 中的 id 单独诊断；部分构建不能发布。

检查 PDF 封面、目录、中文、长公式、宽表格、附录及 HTML 导航和公式。完成后再提交源码与正式 PDF。不要提交 `_draft/`、构建快照、预览、归档或 Windows 元数据。

字体检查依据：[pdffonts 手册](https://manpages.debian.org/bookworm/poppler-utils/pdffonts.1.en.html)。`uni=no` 表示缺少显式 ToUnicode 映射，不直接等同于文本不可提取；上传的 Fandol 预览 PDF 出现此状态，但实测可以提取正文汉字。
