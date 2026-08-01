---
order: 320
title: Markdown Frontmatter YAML 语法速查
module: markdown

category: '002-markdown'
difficulty: beginner
description: Markdown Frontmatter YAML 语法速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 基础语法

**基本写法：frontmatter 块**
`---` 换行 `<YAML>` 换行 `---`
```markdown
---
title: 文档标题
date: 2025-07-31
---
正文内容
```

---

## 标量字段

**基本写法：字符串与数字**
`<键>: <值>`
```yaml
title: 用户指南
version: 2.1
draft: false
rating: 4.5
```

---

**基本写法：带引号字符串**
`<键>: "<值>"`
```yaml
title: "包含: 冒号的标题"
desc: '单引号也可'
path: "a/b/c"
```

---

## 数组字段

**基本写法：行内数组**
`<键>: [<项1>, <项2>]`
```yaml
tags: [js, ts, web]
authors: [Alice, Bob]
```

---

**基本写法：块状数组**
`<键>:`
`  - <项>`
```yaml
tags:
  - javascript
  - typescript
  - vue
```

---

## 对象字段

**基本写法：嵌套对象**
`<键>:`
`  <子键>: <值>`
```yaml
author:
  name: Alice
  email: alice@example.com
  social:
    twitter: "@alice"
```

---

**基本写法：对象数组**
`<键>:`
`  - <子键>: <值>`
```yaml
posts:
  - title: 第一篇
    date: 2025-01-01
  - title: 第二篇
    date: 2025-02-01
```

---

## 布尔与空值

**基本写法：布尔与 null**
`<键>: true` | `<键>: null`
```yaml
published: true
draft: false
featured: null
empty: ~        # ~ 等价 null
```

---

## 多行文本

**基本写法：保留换行**
`<键>: |`
```yaml
description: |
  第一行
  第二行
  保留所有换行与缩进
```

---

**基本写法：折叠换行**
`<键>: >`
```yaml
summary: >
  这是一段
  长文本，换行
  会被折叠成空格
```

---

**基本写法：保留末尾换行控制**
`<键>: |-` | `<键>: |+`
```yaml
# |- 去除末尾换行，|+ 保留全部末尾换行
desc: |- 精确无末尾换行
desc2: |+ 保留所有换行
```

---

## 日期类型

**基本写法：日期字段**
`date: <YYYY-MM-DD>`
```yaml
date: 2025-07-31
datetime: 2025-07-31T10:30:00Z
datetime2: 2025-07-31 18:30:00 +08:00
```

---

## 常用约定字段

**基本写法：博客类 frontmatter**
`<键>: <值>`
```yaml
---
title: 文章标题
date: 2025-07-31
tags: [前端, JS]
categories: 教程
author: Alice
cover: /img/a.png
draft: false
summary: 简短摘要
---
```

---

**基本写法：文档类 frontmatter**
`<键>: <值>`
```yaml
---
title: API 文档
description: 接口说明文档
sidebar_position: 3
sidebar_label: 接口
slug: /api
---
```

---

## 锚点与引用

**基本写法：锚点定义与引用**
`<键>: &<锚点名> <值>` | `*<锚点名>`
```yaml
defaults: &def
  lang: zh
  draft: false
post1:
  <<: *def
  title: 第一篇
```

---

## 转义与特殊字符

**基本写法：特殊字符处理**
`<键>: "<值>"`
```yaml
# 含冒号、井号等需引号
note: "key: value 含冒号"
url: "https://a.com/?x=1&y=2"
hash: "#标题"
```

---

## 多文档分隔

**基本写法：多 frontmatter 文档**
`---`
```yaml
---
title: 第一篇
---
正文一
---
title: 第二篇
---
正文二
```

---

## 注意事项

**基本写法：frontmatter 位置**
`---` 必须位于文件最顶部
```markdown
---
title: 标题
---
<!-- frontmatter 必须是文件第一行，前面不能有空行或内容 -->
正文
```

---

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
| Markdown Frontmatter YAML 语法速查 | 032-FrontmatterYAML | 本文自身 |
