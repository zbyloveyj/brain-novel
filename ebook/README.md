# 完整电子书制作

成品位于 `docs/downloads/brain-novel-complete.pdf`，网站首页设有下载入口。

## 复现

需要 Python 3.11+、ImageMagick（convert）、Pandoc 和 WeasyPrint 的系统依赖（Pango 等）。

```sh
python -m pip install -r ebook/requirements.txt
mkdir -p ebook/fonts
curl -L --fail https://raw.githubusercontent.com/notofonts/noto-cjk/main/Serif/OTF/SimplifiedChinese/NotoSerifCJKsc-Regular.otf -o ebook/fonts/NotoSerifCJKsc-Regular.otf
curl -L --fail https://raw.githubusercontent.com/notofonts/noto-cjk/main/Serif/LICENSE -o ebook/fonts/LICENSE.txt
python ebook/build.py
```

Noto Serif CJK SC 使用 SIL Open Font License。字体仅作为构建依赖，PDF 内嵌字符子集；未在仓库中重复存储完整字体。

## 文本与插图

`ch01.qmd` 至 `ch24.qmd` 为正文核对依据。静态 HTML 阅读页包含原始段落位置的81幅插图，其正文与 QMD 一致。构建器逐段核对正文后使用 HTML 的原始插图位置，并保留各章史实说明、参考文献及完整图注。QMD 中过期的“仅发布正文、图片权利正在核验”提示已移除，版权说明依据当前 `about.qmd`。

章节从新页开始，六部均设独立扉页；图与图注共同分页，图前正文末段尽量与图同页。目录可点击，参考文献编号可点击。16 × 24 cm，10.8 pt Noto Serif CJK SC，1.85 行高。

本次依据源提交 `e35e4f16a32ec9760ec70d1ddadd670ab708631c`，构建日期 2026-10-12。后续修改正文或网页后应重新构建、检查并更新版本日期。

编辑修订版保留修改前后记录：`EDITORIAL.md`。

2026-10-13 插图版：图内统一字体、版式与配色；构建时生成1600 × 1000、4:4:4 色度采样的 JPEG 打印缓存（书页中约 310 dpi），减少 PDF 的体积。缓存位于忽略目录 `ebook/print-cache/`，不影响网页使用的 WebP 与 SVG。

2026-10-14 编辑修订版：基于 `483bc33dddc0f4c2b728f4809a384a7a2e0f8056`，同步修改 QMD 与静态 HTML 后重建。逐项记录见 `editorial-20261014.json`，当前结果见 `verification.json`。
