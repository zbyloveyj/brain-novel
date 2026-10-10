# 在我们理解大脑之前 | Brain Novel

**一个博士生穿越百年神经科学**  
原创科学史小说 · 24章规划 · 本仓库仅公开前三章试读

## 开始阅读

**https://zbyloveyj.github.io/brain-novel/** （仓库建立并完成 GitHub Pages 启用后生效）

### 免费试读

- [第一章：黑色的森林](docs/ch01.html)
- [第二章：神经系统不是电线](docs/ch02.html)
- [第三章：凌晨三点的两颗心](docs/ch03.html)

本仓库不包含其他21章正文、不包含未完成版权清查的82幅插图，也不包含完整版 Word 文件。

## 1. 在 GitHub 新建仓库（仅一次）

1. 打开 <https://github.com/new?name=brain-novel>。
2. Repository name 输入 `brain-novel`；Owner 选择 `zbyloveyj`；Visibility 选择 **Public**。
3. 可以勾选 `Add a README file`，点击 **Create repository**。
4. 建好后回到 ChatGPT 回复：**brain-novel 已创建**。已连接的 GitHub 工具即可把本项目文件上传到新仓库。

## 2. 启用 GitHub Pages

将代码推入 `main` 后，在仓库 `Settings → Pages → Build and deployment` 选择以下一种方案：

- **方案A（最稳妥，不依赖Quarto构建）：** Source → Deploy from a branch；Branch `main`；Folder `/docs`；Save。仓库已经包含生成好的 HTML，因此可以直接部署。
- **方案B（长期维护推荐）：** Source → GitHub Actions；使用本仓库 `.github/workflows/quarto-pages.yml` 在提交 `qmd` 时自动生成并部署 Quarto 阅读网站。可到 `Actions` 标签执行 `Run workflow`。

两种方案二选一即可，页面地址都为 <https://zbyloveyj.github.io/brain-novel/>。

## 3. Quarto 本地构建

下载/安装 [Quarto](https://quarto.org/docs/get-started/) 后在仓库根目录运行：

```bash
quarto render
```

输出目录 `_book/`。修改书稿建议改 `.qmd` 文件，不要只改 `docs/*.html`。

## 目录

| 路径 | 用途 |
| --- | --- |
| `_quarto.yml` | Quarto Book 项目配置 |
| `ch01.qmd`, `ch02.qmd`, `ch03.qmd` | 三章试读正文与分章参考文献 |
| `index.qmd`, `about.qmd` | 首页与史实/版权说明 |
| `book.css` | 阅读排版 CSS |
| `docs/` | 已生成 HTML，支持 GitHub Pages 的 `main /docs` 模式 |
| `.github/workflows/quarto-pages.yml` | GitHub Actions 自动构建 Quarto 图书 |

## 发布与版权

这是一部以真实科学史为背景、以博士生穿越为小说框架的原创文本，部分内容由作者与AI协作创作。具体对白与场景不是历史录音或实验记录。本试读版仍处于史实审校阶段；暂不展示版权尚待确认的图片。完整书稿由作者保留，不在该公共仓库公开。
