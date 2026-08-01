---
order: 310
title: Markdown 引用与嵌套列表语法速查
module: 002-markdown
category: '002-markdown'
difficulty: beginner
description: Markdown 引用与嵌套列表语法速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Markdown 引用与嵌套列表语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础引用

**基本写法：单行引用**
`> <文本>`
```markdown
> 这是一段引用内容
```

---

**基本写法：多行引用**
`> <行1>`
`> <行2>`
```markdown
> 第一行引用
> 第二行引用
> 第三行引用
```

---

## 引用嵌套

**基本写法：引用嵌套引用**
`>> <内层文本>`
```markdown
> 外层引用
>> 内层引用
>>> 更深层引用
```

---

## 引用内含其他语法

**基本写法：引用内含标题与列表**
`> ## <标题>`
```markdown
> ## 引用内标题
> - 列表项一
> - 列表项二
> **加粗** 与 *斜体* 均可
```

---

## 嵌套列表

**基本写法：列表嵌套子项**
`<缩进>- <子项>`
```markdown
- 父项一
  - 子项一
  - 子项二
- 父项二
  - 子项三
```

---

**基本写法：有序列表嵌套**
`<缩进><数字>. <子项>`
```markdown
1. 父项
   1. 子项一
   2. 子项二
2. 父项二
```

---

## 任务列表嵌套

**基本写法：任务列表内嵌套列表**
`  - [ ] <子任务>`
```markdown
- [x] 主任务
  - [x] 子任务一
  - [ ] 子任务二
- [ ] 另一主任务
```

---

## 引用与列表混合

**基本写法：列表项内放引用**
`<列表项>` 换行 `  > <引用>`
```markdown
- 项目一
  > 项目一的说明引用
- 项目二
```

---

## 缩进规范

**基本写法：缩进位数**
`<2 或 4 空格>- <子项>`
```markdown
// 2 空格缩进（GFM 推荐）
- 项
  - 子项

// 4 空格缩进（CommonMark 标准）
- 项
    - 子项
```

---

## 多级嵌套缩进

**基本写法：三级嵌套**
`<层级数 × 2 空格>- <项>`
```markdown
- 一级
  - 二级
    - 三级
      - 四级
```

---

## 嵌套列表与代码块

**基本写法：列表项内代码块**
`<列表项>` 换行 `  <缩进 4 空格代码>`
```markdown
- 项目一

      const x = 1;
      console.log(x);

- 项目二
```

---

## 紧凑与松散列表

**基本写法：紧凑列表（无空行）**
`- <项>` 直接换行 `- <项>`
```markdown
// 紧凑：项间无空行
- 项一
- 项二

// 松散：项间有空行，渲染为段落
- 项一

- 项二
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
| Markdown 引用与嵌套列表语法速查 | 031-BlockquoteNestedList | 本文自身 |
| Markdown Frontmatter YAML 语法速查 | 032-FrontmatterYAML | 本文的并列主题 |
