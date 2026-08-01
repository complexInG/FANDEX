---
order: 62
title: 自动目录
module: markdown
category: 'Markdown Basics'
difficulty: beginner
description: 'Markdown自动目录生成：[TOC]语法、平台实现与自定义目录方案。'
author: fanquanpp
updated: '2026-08-01'
related:
  - markdown/链接与图片
  - markdown/转换工具
  - markdown/锚点跳转
  - markdown/图片CDN加速
prerequisites:
  - markdown/语法指南
---

## 1. 自动目录概述

### 1.1 为什么需要自动目录

自动目录（Table of Contents, TOC）根据文档标题自动生成导航结构，核心价值：

- **快速导航**：点击目录项跳转到对应章节
- **文档概览**：一目了然地了解文档结构
- **自动更新**：标题变更时目录自动同步

### 1.2 实现方式

| 方式          | 语法         | 适用平台        |
| :------------ | :----------- | :-------------- |
| **`[TOC]`**   | `[TOC]`      | 部分编辑器      |
| **`[[toc]]`** | `[[toc]]`    | VuePress 等     |
| **`{:toc}`**  | `{:toc}`     | Jekyll/Kramdown |
| **Pandoc**    | `--toc` 参数 | Pandoc          |
| **HTML 手动** | 锚点链接     | 通用            |

## 2. 各平台目录语法

### 2.1 `[TOC]` 语法

最常见的目录语法，在文档中插入 `[TOC]` 即可自动生成：

```markdown
[TOC]

## 第一章 概述

### 1.1 背景

### 1.2 目标

## 第二章 方法

### 2.1 实验设计

### 2.2 数据分析
```

支持 `[TOC]` 的平台：

| 平台         | 语法     | 说明                |
| :----------- | :------- | :------------------ |
| **Typora**   | `[TOC]`  | 原生支持            |
| **VS Code**  | 需插件   | Markdown All in One |
| **Obsidian** | 无需语法 | 大纲面板自动显示    |

### 2.2 VuePress / VitePress

```markdown
[[toc]]

## 标题一

### 子标题

## 标题二
```

### 2.3 Jekyll / Kramdown

```markdown
- 目录
  {:toc}

## 标题一

## 标题二
```

### 2.4 Hugo

Hugo 使用模板变量自动生成目录：

```go
{{ .TableOfContents }}
```

### 2.5 Pandoc

```bash
# 生成带目录的文档
pandoc input.md -o output.pdf --toc

# 自定义目录标题
pandoc input.md -o output.pdf --toc -V toc-title="目录"

# 设置目录深度
pandoc input.md -o output.pdf --toc --toc-depth=3
```

## 3. GitHub 中的目录

### 3.1 README 自动目录

GitHub 不支持 `[TOC]` 语法，但可以通过以下方式实现目录：

**方案一：手动锚点链接**

```markdown
## 概述

## 安装

## 使用方法

### 基本用法

### 高级配置

## 常见问题
```

### 3.2 GitHub 锚点规则

GitHub 自动为标题生成锚点，规则如下：

| 规则           | 示例标题          | 生成的锚点         |
| :------------- | :---------------- | :----------------- |
| 转小写         | `Getting Started` | `#getting-started` |
| 空格变连字符   | `Hello World`     | `#hello-world`     |
| 移除特殊字符   | `What's New?`     | `#whats-new`       |
| 中文保留       | `安装指南`        | `#安装指南`        |
| 多个连字符合并 | `A -- B`          | `#a----b`          |

### 3.3 自动生成工具

```bash
# 使用 markdown-toc 自动生成
npx markdown-toc README.md --insert

# 使用 doctoc
npx doctoc README.md
```

## 4. 自定义目录

### 4.1 带编号的目录

```markdown
## 5. 目录深度控制

### 5.1 包含/排除级别

```markdown
<!-- 只包含 h2 和 h3 -->

## 6. 最佳实践

### 6.1 目录放置位置

- **文档开头**：最常见，方便读者快速导航
- **固定侧边栏**：长文档推荐，始终可见
- **折叠**：中等长度文档，不占用太多空间

### 6.2 维护建议

- 使用自动生成工具，避免手动维护
- 标题命名要清晰，目录才有意义
- 控制标题层级不超过 4 级
- 长文档（超过 5 个章节）建议添加目录

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
| 自动目录 | 019-AutoTOC | 本文自身 |
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
