---
order: 64
title: 图片CDN加速
module: markdown
category: 'Markdown Basics'
difficulty: intermediate
description: Markdown图片CDN加速方案：图床选择、CDN配置、懒加载与性能优化。
author: fanquanpp
updated: '2026-08-01'
related:
  - markdown/自动目录
  - markdown/锚点跳转
  - markdown/版本控制下的PR协作
  - markdown/代码块与语法高亮
prerequisites:
  - markdown/语法指南
---

## 1. 图片托管概述

### 1.1 为什么需要图床

Markdown 中的图片语法只引用 URL，不存储图片数据。因此需要一个**图床**来存储和分发图片：

```markdown
![描述](https://example.com/images/photo.png)
```

### 1.2 图片托管方案对比

| 方案         | 优点               | 缺点         | 适用场景 |
| :----------- | :----------------- | :----------- | :------- |
| **仓库内**   | 版本控制、离线可用 | 仓库体积膨胀 | 小型项目 |
| **GitHub**   | 免费、稳定         | 有带宽限制   | 开源项目 |
| **CDN 图床** | 快速、全球加速     | 可能有费用   | 生产环境 |
| **对象存储** | 可控、安全         | 需配置       | 企业项目 |
| **自建图床** | 完全可控           | 运维成本     | 技术团队 |

## 2. GitHub 作为图床

### 2.1 使用 Issue 上传

在 GitHub Issue 中拖拽图片，自动上传到 GitHub CDN：

```markdown
<!-- 上传后生成的链接 -->

![image](https://github.com/user/repo/assets/xxxxx/image.png)
```

### 2.2 使用仓库存储

```markdown
<!-- 项目内图片 -->

![架构图](./docs/images/architecture.png)

<!-- 绝对路径引用 -->

![Logo](https://raw.githubusercontent.com/user/repo/main/docs/images/logo.png)
```

### 2.3 GitHub CDN 限制

| 限制       | 说明                       |
| :--------- | :------------------------- |
| 单文件大小 | ≤ 100 MB                   |
| 仓库大小   | 建议 ≤ 1 GB                |
| 带宽       | 无明确限制，但滥用会被限速 |
| 私有仓库   | 图片链接需要认证           |

### 2.4 jsDelivr 加速

jsDelivr 提供免费的 GitHub 仓库 CDN 加速：

```markdown
<!-- 原始 GitHub 链接 -->

https://raw.githubusercontent.com/user/repo/main/images/photo.png

<!-- jsDelivr CDN 加速 -->

https://cdn.jsdelivr.net/gh/user/repo/images/photo.png

<!-- 指定版本/标签 -->

https://cdn.jsdelivr.net/gh/user/repo@v1.0/images/photo.png
```

## 3. 对象存储 + CDN

### 3.1 主流对象存储

| 服务              | 免费额度       | 特点         |
| :---------------- | :------------- | :----------- |
| **Cloudflare R2** | 10 GB/月       | 无出站流量费 |
| **AWS S3**        | 5 GB（12个月） | 全球部署     |
| **阿里云 OSS**    | 按量计费       | 国内速度快   |
| **腾讯云 COS**    | 50 GB（6个月） | 国内速度快   |
| **七牛云**        | 10 GB          | 国内老牌     |

### 3.2 Cloudflare R2 + CDN 配置

```bash
# 1. 创建 R2 存储桶
# 2. 上传图片
wrangler r2 object put my-bucket/images/photo.png --file ./photo.png

# 3. 配置自定义域名
# Cloudflare Dashboard → R2 → 存储桶 → 自定义域名

# 4. 使用 CDN 链接
![描述](https://cdn.mydomain.com/images/photo.png)
```

### 3.3 图片处理

CDN 通常提供图片处理功能：

```markdown
<!-- 缩放 -->

![缩略图](https://cdn.example.com/photo.png?w=300&h=200)

<!-- 格式转换（WebP） -->

![WebP](https://cdn.example.com/photo.png?format=webp)

<!-- 质量 -->

![压缩](https://cdn.example.com/photo.png?q=80)
```

## 4. 图片优化

### 4.1 格式选择

| 格式     | 压缩类型 | 透明度 | 动画 | 适用场景             |
| :------- | :------- | :----- | :--- | :------------------- |
| **PNG**  | 无损     |        |      | 图标、截图、需要透明 |
| **JPEG** | 有损     |        |      | 照片、渐变           |
| **WebP** | 两者     |        |      | 通用（推荐）         |
| **SVG**  | 矢量     |        |      | 图标、Logo、图表     |
| **AVIF** | 有损     |        |      | 下一代格式           |

### 4.2 图片压缩

```bash
# 使用 Sharp（Node.js）
npx sharp-cli -i input.png -o output.webp --format webp --quality 80

# 使用 ImageMagick
convert input.png -quality 85 output.webp

# 使用 Squoosh CLI
npx @nicolo-ribaudo/squoosh-cli --webp '{quality:80}' input.png
```

### 4.3 响应式图片

```html
<picture>
  <source srcset="photo.avif" type="image/avif" />
  <source srcset="photo.webp" type="image/webp" />
  <img src="photo.jpg" alt="描述" loading="lazy" width="800" height="600" />
</picture>
```

## 5. 懒加载

### 5.1 原生懒加载

```html
<img src="photo.png" alt="描述" loading="lazy" />
```

### 5.2 Markdown 中的懒加载

部分渲染器支持在 Markdown 中添加 HTML 属性：

```markdown
<!-- Hugo -->

![描述](photo.png){loading=lazy}

<!-- VuePress -->

![描述](photo.png "title" =800x600)
```

### 5.3 全局懒加载

在网站中全局启用图片懒加载：

```javascript
// 为所有图片添加 loading="lazy"
document.querySelectorAll('img:not([loading])').forEach((img) => {
  img.setAttribute('loading', 'lazy');
});
```

## 6. 图床管理工具

### 6.1 常用工具

| 工具        | 平台   | 特点                   |
| :---------- | :----- | :--------------------- |
| **PicGo**   | 桌面端 | 支持多种图床，插件丰富 |
| **uPic**    | macOS  | 轻量，支持快捷键       |
| **PicList** | 桌面端 | PicGo 增强版           |
| **imgur**   | 在线   | 简单快捷               |

### 6.2 PicGo 配置

```json
// PicGo 配置示例（GitHub 图床）
{
  "picBed": {
    "current": "github",
    "github": {
      "repo": "user/image-hosting",
      "token": "ghp_xxxxx",
      "path": "images/",
      "branch": "main"
    }
  }
}
```

### 6.3 VS Code 集成

```bash
# 安装 PicGo 插件
# VS Code 扩展: PicGo

# 配置 settings.json
{
  "picgo.picBed.current": "github",
  "picgo.picBed.github.repo": "user/image-hosting",
  "picgo.picBed.github.token": "ghp_xxxxx"
}

# 使用：粘贴图片后自动上传并插入链接
```

## 参考文献

CommonMark 规范：https://spec.commonmark.org/
GFM 规范：https://github.github.com/gfm/
Markdown 指南：https://www.markdownguide.org/
Markdownlint：https://github.com/DavidAnson/markdownlint

## 延伸阅读

Markdown 基础语法，见 002-markdown 模块文档。
Markdown 删除线语法，见 002-markdown/010-Strikethrough 文档。
文档站构建（Astro），见 056-astro 模块（如已加入）。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供文档写作课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 CommonMark 解析规则

解析分块级与行内两阶段；块结构（列表、引用）优先级高于行内。
强调定界符规则：左右翼属性、匹配优先级；删除线与表格是 GFM 扩展。
HTML 块与内联 HTML 的解析规则；围栏代码块内不做行内解析。
理解规则可解释“为什么同一文档在不同渲染器结果不同”。

### 13.2 文档站自动化

frontmatter 驱动：标题、描述、排序、标签；目录自动生成。
组件化：MDX 嵌入交互组件；KaTeX 渲染公式。
质量门禁：markdownlint、remark 插件、构建期链接校验。
搜索与检索：全文索引（Pagefind）与交叉引用图。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Markdown 语法指南 | 001-SyntaxGuide | 本文的并列主题 |
| Markdown 标题语法 | 002-HeadingSyntax | 本文的并列主题 |
| Markdown 段落与换行 | 003-ParagraphLineBreak | 本文的并列主题 |
| Markdown 基础文本格式 | 004-BasicTextFormat | 本文的前置基础 |
| CommonMark规范 | 005-CommonMarkSpec | 本文的并列主题 |
| Markdown 列表语法 | 006-ListSyntax | 本文的并列主题 |
| GitHub Flavored Markdown | 007-GitHubFlavoredMarkdown | 本文的并列主题 |
| 转义字符 | 008-EscapeCharacter | 本文的并列主题 |
| 脚注 | 009-Footnote | 本文的并列主题 |
| 删除线 | 010-Strikethrough | 本文的并列主题 |
| 自动链接 | 011-AutoLink | 本文的并列主题 |
| Emoji表情 | 012-Emoji | 本文的并列主题 |
| 下标与上标 | 013-SubscriptSuperscript | 本文的并列主题 |
| LaTeX数学公式 | 014-LaTeXMathFormula | 本文的并列主题 |
| Mermaid图表 | 015-Mermaid | 本文的并列主题 |
| 编辑器功能 | 016-EditorFeature | 本文的并列主题 |
| Markdown 链接与图片 | 017-LinkImage | 本文的并列主题 |
| 转换工具 | 018-ConversionTool | 本文的并列主题 |
| 自动目录 | 019-AutoTOC | 本文的并列主题 |
| 锚点跳转 | 020-AnchorJump | 本文的并列主题 |
| 图片CDN加速 | 021-ImageCDNAcceleration | 本文自身 |
| 版本控制下的PR协作 | 022-VCSPRCollaboration | 本文的并列主题 |
| Markdown 代码块与语法高亮 | 023-CodeBlockSyntaxHighlight | 本文的并列主题 |
| Markdown 表格 | 024-Table | 本文的并列主题 |
| 规范文档编写 | 025-SpecDocumentWriting | 本文的并列主题 |
| Markdown 高级语法与文档自动化 | 026-AdvancedSyntaxDocumentAutomation | 本文的并列主题 |
| Markdown 任务列表 | 027-TaskList | 本文的并列主题 |
| Markdown 定义列表 | 028-DefinitionList | 本文的并列主题 |
| Markdown 提示框（admonition/callout） | 029-AdmonitionCallout | 本文的并列主题 |
| Markdown HTML 内嵌 | 030-HtmlEmbed | 本文的并列主题 |
| Markdown 引用与嵌套列表语法速查 | 031-BlockquoteNestedList | 本文的并列主题 |
| Markdown Frontmatter YAML 语法速查 | 032-FrontmatterYAML | 本文的并列主题 |
