# 明亮版封面设计记录

日期：2026-10-13。基于主分支 `6de8bc3d8981bcb41ea53487a327e2e73068fd3a`，按作者要求提亮封面。

使用内置 image_gen 图像编辑工具，以原深蓝封面为编辑目标。新版为暖白、浅蓝与柔金色，保留完整书名、作者署名和神经元意象。输出为1024×1536，转换为WebP和JPEG供网页、个人主页、Quarto和PDF共同使用。

文件：`docs/assets/cover.webp`、`docs/assets/cover.jpg`、`assets/cover.webp`、`assets/cover.jpg`、`docs/profile/assets/brain-novel-cover.webp`。

网页只调整封面区配色及版本化资源链接，保持已有阅读布局与功能。PDF维持317页，第4—317页的文字块、插图位置及全部书签与上一版一致。封面、版权页已渲染复核。网页配色使用桌面/手机宽度静态样张检查，静态渲染器的网格布局以等效块布局模拟；未进行真实浏览器交互验收。

## 原始设计提示

Use case: style-transfer. Edit target: the supplied existing Chinese novel cover. Create a noticeably brighter, more beautiful final flat book cover, portrait 2:3, at least 1024x1536. Preserve the exact book identity, the refined literary cover composition, the branching neuron / landscape metaphor and the small human figure by a doorway. Reimagine the scene in luminous daylight: warm ivory paper in the upper half, pale cerulean blue atmosphere, elegant mineral teal-blue water and distant mountains below, restrained champagne gold neuron branches catching morning light. A soft pale apricot sun behind the branches, subtle peach glow. The cover should feel like an exquisitely illustrated contemporary literary hardback, nuanced and detailed, beautifully printed, not a simplistic minimalist poster. The overall value must be HIGH KEY with about two thirds light ivory, mist blue and pale gold; no large near-black areas. Finely drawn botanical-like neurons, airy mist and reflected light; reduce heavy gritty grain and dark mountains. Give the composition breathing room while retaining rich illustration in the lower half.
Typography is essential: crisp large dark petrol-blue Chinese Song-style title across the upper half, with exact line breaks:
在我们
理解大脑
之前
Small centered text at top: 长篇小说
Small refined English beneath title: BEFORE WE UNDERSTAND
THE BRAIN
Author line clearly legible at bottom: 一心问道 著
Preserve all these words exactly. No extra text, no publisher, no ISBN, no watermark, no 3D book mockup, no border, no neon, no digital sci-fi brain, no glossy plastic, no starry night. Professional balance and exquisite typographic spacing. Author line must be dark ink over a light ivory footer, not lost in scenery. The title and illustration should work together as one coherent luminous cover.

