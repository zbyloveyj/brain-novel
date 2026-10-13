# 插图设计与复现

2026-10-13 按作者要求，为《在我们理解大脑之前》的 81 幅正文插图统一设计。深墨蓝、铜金与暖白的配色与新版封面相呼应。正文段落、图注、参考文献及插图相邻段落保持一致。

## 成品

- `docs/assets/plates/figure-002.webp` 至 `figure-082.webp`：2560 × 1600 的网页与 PDF 插图。
- 同目录同名 SVG：可放大的矢量版本，文字转为轮廓，避免读者设备缺少字体。第一幅神经元意象图含位图插画。
- `assets/plates/`：Quarto 源稿使用的同版 WebP。
- 原 `assets/figures/`、`docs/assets/figures/` 保留，方便对照原始图示。

## 设计与内容边界

80 幅时间线、流程、示意曲线和比较表由 Matplotlib 原生绘制，保留原图的概念关系、历史节点、比较条件及明确标示的数值例子。教学曲线按原图表达的关系重新构造，均非原始实验数据；原有图注及参考文献保留。嗅觉响应矩阵从旧图各单元格中心的 viridis 色值读取，用于保持原图的人工响应模式，不将其当作实测数据。

第一幅神经元森林使用内置 imagegen 制作。提示重点：三个相互独立的神经元意象，一大两小，深蓝蚀刻线条、少量铜金高光、暖白纸面；分支可靠近但不形成连续网；无文字、无地景、无月亮、无人物。它是绘图语言的艺术性重绘，不是解剖比例图或历史原图。绘制后再排入统一插页版式。

原时间线边缘文字裁切、Na+/K+ 符号缺字等显示问题已修正。史料与科学结论未在本次美化中扩展为新的实证主张。

## 复现

将 NotoSerifCJKsc-Regular.otf 放入 `ebook/fonts/`（见 `ebook/README.md`）。依赖 Python、Matplotlib、NumPy、Pillow 和 ImageMagick。

```sh
python illustrations/render.py
# 仅重绘某几幅
python illustrations/render.py 20 26
python ebook/build.py
python ebook/verify.py
```

`original-inventory.json` 记录原图尺寸、完整图注及前接段落；`render-audit.json` 记录重绘文字及边界检查结果。重绘以后需同步 `assets/plates/` 中对应 WebP，并重新生成完整 PDF。

## 复核

81 幅插图均已生成全览并目视检查，另放大检查时间线、复杂图例、离子符号、流程箭头及比较表。检查文字边界和节点内排版、图片可解码性、SVG 资源完整性，以及 24 章正文、参考文献、图注和插图位置的一致性。网页检查为桌面与手机尺寸的静态渲染，不等同于真实浏览器交互验收。
