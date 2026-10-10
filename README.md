# brain-novel · 在我们理解大脑之前

一个博士生穿越百年神经科学的原创长篇历史小说，**24章公开文字阅读版**。

- 在线阅读：https://zbyloveyj.github.io/brain-novel/
- Quarto 源文件：`ch01.qmd` 至 `ch24.qmd`
- 分章“史实与创作说明”和参考文献附在各章节末尾
- `docs/` 为已生成的静态 HTML 备用版本；GitHub Actions 发布时使用 Quarto 输出

版权与审校：部分正文为人机协作，历史事实仍在最终核查。为尊重图片权利，公开网站暂不发布原稿插图。请不要未经许可再分发完整内容。

## 本地构建

```bash
quarto render --to html
```

GitHub Pages 选择 GitHub Actions（已有 `.github/workflows/quarto-pages.yml`），或使用 `main` 分支的 `/docs` 静态版本。
