---
order: 60
tags:
  - markdown
difficulty: intermediate
title: 'Markdown 链接与图片'
module: markdown
category: 'Markdown Basics'
description: 行内链接、引用链接、图片嵌入与脚注。
author: Anonymous
related:
  - markdown/Mermaid图表
  - markdown/编辑器功能
  - markdown/转换工具
  - markdown/自动目录
prerequisites:
  - markdown/语法指南
updated: '2026-08-01'
---

# 链接与图片

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 链接 (Links)

### 1.1 行内链接 (Inline Links)

**语法**：`[链接文本](URL "可选的标题")`
**示例**：

```markdown
[GitHub](https://github.com 'GitHub 官方网站')
[Markdown 指南](https://www.markdownguide.org)
```

**渲染效果**：
[GitHub](https://github.com 'GitHub 官方网站')
[Markdown 指南](https://www.markdownguide.org)

### 1.2 引用链接 (Reference Links)

**语法**：

```markdown
[链接文本][引用标识符]
[引用标识符]: URL "可选的标题"
```

**示例**：

```markdown
[GitHub][github]
[Markdown 指南][md-guide]
[github]: https://github.com "GitHub 官方网站"
[md-guide]: https://www.markdownguide.org "Markdown 官方指南"
```

**渲染效果**：
[GitHub][github]
[Markdown 指南][md-guide]
[github]: https://github.com "GitHub 官方网站"
[md-guide]: https://www.markdownguide.org "Markdown 官方指南"

### 1.3 自动链接 (Auto Links)

**语法**：`<URL>` 或 `<电子邮件地址>`
**示例**：

```markdown
<https://github.com>
<example@example.com>
```

**渲染效果**：
<https://github.com>
<example@example.com>

### 1.4 相对链接 (Relative Links)

**语法**：使用相对路径指向本地文件或目录
**示例**：

```markdown
[README 文件](./README.md)
[图片目录](../assets/)
```

**渲染效果**：
[README 文件](../README.md)
[图片目录](../)

## 2. 图片 (Images)

### 2.1 基本语法

**语法**：`![替代文本](图片URL "可选的标题")`
**示例**：

```markdown
!
```

**渲染效果**：
![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png 'GitHub Logo')

### 2.2 引用图片

**语法**：

```markdown
!
[图片引用标识符]: 图片URL "可选的标题"
```

**示例**：

```markdown
!
[github-logo]: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png "GitHub Logo"
```

**渲染效果**：
![GitHub Logo][github-logo]
[github-logo]: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png "GitHub Logo"

### 2.3 本地图片

**语法**：使用相对路径指向本地图片文件
**示例**：

```markdown
!
```

### 2.4 图片链接

**语法**：将图片嵌套在链接中
**示例**：

```markdown
[![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)](https://github.com)
```

**渲染效果**：
[![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)](https://github.com)

## 3. 最佳实践

### 3.1 链接最佳实践

1. **使用描述性的链接文本**：链接文本应该清晰地描述链接的目标，避免使用"点击这里"等模糊描述
2. **添加标题属性**：对于重要的链接，添加标题属性可以提供更多上下文信息
3. **使用引用链接**：对于重复使用的链接，使用引用链接可以使代码更整洁
4. **检查链接有效性**：定期检查链接是否仍然有效

### 3.2 图片最佳实践

1. **添加替代文本**：为图片添加有意义的替代文本，提高可访问性
2. **优化图片大小**：确保图片大小适中，避免影响页面加载速度
3. **使用相对路径**：对于本地图片，使用相对路径可以确保在不同环境中都能正确显示
4. **添加图片标题**：对于复杂图片，添加标题可以提供更多信息

### 3.3 组织图片资源

1. **创建专门的图片目录**：如 `assets/` 或 `images/` 目录
2. **使用一致的命名规范**：如 `feature-image.png` 或 `step-1-screenshot.png`
3. **分类存储**：根据用途或主题对图片进行分类存储

## 4. 常见问题与解决方案

### 4.1 图片不显示

**问题**：图片无法正常显示
**解决方案**：

- 检查图片路径是否正确
- 确保图片文件存在
- 检查网络连接是否正常
- 对于本地图片，确保使用正确的相对路径

### 4.2 链接失效

**问题**：链接点击后无法访问目标页面
**解决方案**：

- 检查 URL 是否正确
- 确保目标网站仍然存在
- 对于本地文件，确保文件路径正确
- 检查是否需要添加 `http://` 或 `https://` 前缀

### 4.3 图片大小控制

**问题**：图片显示过大或过小
**解决方案**：

- 在 Markdown 中，基本语法不支持直接控制图片大小
- 可以使用 HTML 标签来控制图片大小：

```html
<img src="image.png" alt="描述" width="300" height="200" />
```

- 或者在 CSS 中设置图片样式

## 5. 扩展语法

### 5.1 GitHub Flavored Markdown (GFM)

**任务列表**：

```markdown
-
-
-
```

**渲染效果**：

- [x] 完成任务 1
- [ ] 完成任务 2
- [ ] 完成任务 3

### 5.2 表格中的链接和图片

**示例**：

```markdown
| 名称   | 链接                         | 图标                                                                                 |
| ------ | ---------------------------- | ------------------------------------------------------------------------------------ |
| GitHub | [GitHub](https://github.com) | ![GitHub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png) |
| Google | [Google](https://google.com) | ![Google](https://www.google.com/favicon.ico)                                        |
```

**渲染效果**：

| 名称   | 链接                         | 图标                                                                                 |
| ------ | ---------------------------- | ------------------------------------------------------------------------------------ |
| GitHub | [GitHub](https://github.com) | ![GitHub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png) |
| Google | [Google](https://google.com) | ![Google](https://www.google.com/favicon.ico)                                        |

## 6. 总结

Markdown 提供了简洁而强大的语法来添加链接和图片，使文档更加丰富和有吸引力。通过掌握这些语法，你可以创建包含外部链接、内部链接、图片和图片链接的文档。
在使用链接和图片时，遵循最佳实践可以确保文档的可访问性、可靠性和美观度。同时，了解常见问题的解决方案可以帮助你快速解决在使用过程中遇到的问题。

---

## 行内链接

**单行写法：基本行内链接**
`[<链接文本>](<URL>)`
```markdown
[Markdown 指南](https://www.markdownguide.org)
```

**单行写法：带标题的行内链接**
`[<链接文本>](<URL> "<标题>")`
```markdown
[GitHub](https://github.com "GitHub 官方网站")
```

---

## 引用链接

**换行写法：定义引用链接**
`[<链接文本>][<引用标识符>]\n[<引用标识符>]: <URL> ["<标题>"]`
```markdown
[GitHub][github]

[github]: https://github.com "GitHub 官方网站"
```

---

## 自动链接

**单行写法：URL 自动链接**
`<<URL>>`
```markdown
<https://github.com>
```

**单行写法：邮箱自动链接**
`<<邮箱>>`
```markdown
<user@example.com>
```

---

## 相对链接

**单行写法：指向本地文件**
`[<链接文本>](<相对路径>)`
```markdown
[README 文件](./README.md)
```

**单行写法：指向上级目录**
`[<链接文本>](<相对路径>)`
```markdown
[图片目录](../assets/)
```

---

## 基本图片

**单行写法：插入图片**
`![<替代文本>](<图片URL>)`
```markdown
![示例图片](https://example.com/image.png)
```

**单行写法：带标题的图片**
`![<替代文本>](<图片URL> "<标题>")`
```markdown
![GitHub Logo](https://github.githubassets.com/logo.png "GitHub Logo")
```

---

## 引用图片

**换行写法：定义引用图片**
`![<替代文本>][<图片引用标识符>]\n[<图片引用标识符>]: <图片URL> ["<标题>"]`
```markdown
![GitHub Logo][github-logo]

[github-logo]: https://github.githubassets.com/logo.png "GitHub Logo"
```

---

## 本地图片

**单行写法：使用相对路径插入本地图片**
`![<替代文本>](<相对路径>)`
```markdown
![示例图片](./images/example.png)
```

---

## 图片链接

**单行写法：将图片嵌套在链接中**
`[![<替代文本>](<图片URL>)](<链接URL>)`
```markdown
[![GitHub Logo](https://github.githubassets.com/logo.png)](https://github.com)
```

---

## 图片大小控制

**单行写法：使用 HTML img 标签控制大小**
`<img src="<URL>" alt="<替代文本>" width="<宽>" height="<高>" />`
```markdown
<img src="image.png" alt="描述" width="300" height="200" />
```

**单行写法：仅控制宽度**
`<img src="<URL>" alt="<替代文本>" width="<宽>" />`
```markdown
<img src="image.png" alt="描述" width="300" />
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
| Markdown 链接与图片 | 017-LinkImage | 本文自身 |
| 转换工具 | 018-ConversionTool | 本文的并列主题 |
| 自动目录 | 019-AutoTOC | 本文的并列主题 |
| 锚点跳转 | 020-AnchorJump | 本文的并列主题 |
| 图片CDN加速 | 021-ImageCDNAcceleration | 本文的并列主题 |
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
