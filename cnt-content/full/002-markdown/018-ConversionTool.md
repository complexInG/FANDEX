---
order: 61
title: 转换工具
module: markdown
category: 'Markdown Basics'
difficulty: intermediate
description: Markdown转换工具：Pandoc的安装、使用与高级转换技巧。
author: fanquanpp
updated: '2026-08-01'
related:
  - markdown/编辑器功能
  - markdown/链接与图片
  - markdown/自动目录
  - markdown/锚点跳转
prerequisites:
  - markdown/语法指南
---

## 1. 转换工具概述

### 1.1 为什么需要转换

Markdown 虽然轻量灵活，但在某些场景需要转换为其他格式：

| 目标格式   | 场景           | 工具           |
| :--------- | :------------- | :------------- |
| **HTML**   | 网页发布       | 各渲染器       |
| **PDF**    | 打印、正式文档 | Pandoc、Typora |
| **Word**   | 企业协作       | Pandoc         |
| **LaTeX**  | 学术论文       | Pandoc         |
| **幻灯片** | 演示文稿       | Pandoc、Marp   |
| **EPUB**   | 电子书         | Pandoc         |

### 1.2 工具对比

| 工具           | 支持格式   | 特点                 |
| :------------- | :--------- | :------------------- |
| **Pandoc**     | 40+ 种格式 | 万能转换器，功能最强 |
| **Typora**     | HTML/PDF   | 所见即所得导出       |
| **Marp**       | PDF/PPTX   | Markdown 演示文稿    |
| **mdbook**     | HTML       | 在线书籍             |
| **Docusaurus** | HTML       | 技术文档网站         |

## 2. Pandoc 安装

### 2.1 安装方式

```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt install pandoc

# Windows
# 从 https://pandoc.org/installing.html 下载安装包
# 或使用 Chocolatey
choco install pandoc

# 验证安装
pandoc --version
```

### 2.2 PDF 导出依赖

导出 PDF 需要额外的 LaTeX 引擎：

```bash
# 推荐：安装 TinyTeX（轻量 TeX 发行版）
curl -L https://tinyurl.com/install-tinytex | sh

# 或安装完整 TeX Live
sudo apt install texlive-full    # Linux
brew install --cask mactex       # macOS

# 中文支持
sudo apt install texlive-lang-chinese
# 或在 TinyTeX 中安装
tlmgr install cjkpunct ctex xecjk
```

## 3. Pandoc 基础用法

### 3.1 基本转换

```bash
# Markdown → HTML
pandoc input.md -o output.html

# Markdown → PDF
pandoc input.md -o output.pdf

# Markdown → Word
pandoc input.md -o output.docx

# Markdown → LaTeX
pandoc input.md -o output.tex

# Markdown → 幻灯片（Beamer）
pandoc input.md -t beamer -o slides.pdf
```

### 3.2 指定输入输出格式

```bash
# 显式指定格式
pandoc -f markdown -t html input.md -o output.html

# 从 HTML 转 Markdown
pandoc -f html -t markdown input.html -o output.md

# 从 Word 转 Markdown
pandoc -f docx -t markdown input.docx -o output.md
```

### 3.3 支持的格式

| 输入格式                  | 输出格式            |
| :------------------------ | :------------------ |
| Markdown, CommonMark, GFM | HTML, HTML5         |
| LaTeX, reStructuredText   | PDF（通过 LaTeX）   |
| Word (docx), EPUB         | Word (docx)         |
| Org-mode, Textile         | EPUB, FB2           |
| HTML, DocBook             | LaTeX, Beamer       |
| JATS, OPML                | S5, Slidy, DZSlides |
| CSV, TSV                  | RTF, ODT            |
| Native Pandoc             | AsciiDoc, man       |

## 4. 高级用法

### 4.1 YAML 元数据

```markdown
---
title: '我的文档'
author: '张三'
date: '2026-06-14'
lang: zh-CN
geometry: margin=2.5cm
fontsize: 12pt
toc: true
numbersections: true
---

# 第一章

正文内容...
```

```bash
# 使用元数据生成带目录的 PDF
pandoc input.md -o output.pdf \
  --pdf-engine=xelatex \
  -V CJKmainfont="SimSun"
```

### 4.2 模板

```bash
# 使用自定义模板
pandoc input.md -o output.html --template=my-template.html

# 列出默认模板
pandoc -D html    # HTML 模板
pandoc -D latex   # LaTeX 模板
pandoc -D docx    # Word 模板（引用文档）

# 导出默认模板用于修改
pandoc -D html > my-template.html
```

### 4.3 过滤器

Pandoc 过滤器可以在转换过程中修改文档结构：

```bash
# 使用 Python 过滤器
pandoc input.md --filter=filter.py -o output.html

# 使用 Lua 过滤器（更快）
pandoc input.md --lua-filter=filter.lua -o output.html
```

```lua
-- Lua 过滤器示例：为所有链接添加 target="_blank"
function Link(el)
  el.attributes.target = "_blank"
  el.attributes.rel = "noopener noreferrer"
  return el
end
```

### 4.4 数学公式

```bash
# LaTeX 数学公式 → MathJax（HTML）
pandoc input.md -o output.html --mathjax

# LaTeX 数学公式 → KaTeX
pandoc input.md -o output.html --katex

# LaTeX 数学公式 → 原生 LaTeX（PDF）
pandoc input.md -o output.pdf --pdf-engine=xelatex
```

## 5. 中文支持

### 5.1 PDF 中文导出

```bash
# 使用 XeLaTeX 引擎（推荐）
pandoc input.md -o output.pdf \
  --pdf-engine=xelatex \
  -V CJKmainfont="Source Han Sans CN" \
  -V mainfont="Source Han Sans CN" \
  -V monofont="Source Code Pro"

# 使用 ctex 文档类
pandoc input.md -o output.pdf \
  --pdf-engine=xelatex \
  -V documentclass=ctexart \
  -V geometry:margin=2.5cm
```

### 5.2 常见中文字体

| 字体                    | 说明     | 适用场景     |
| :---------------------- | :------- | :----------- |
| **Source Han Sans CN**  | 思源黑体 | 正文、标题   |
| **Source Han Serif CN** | 思源宋体 | 正式文档     |
| **SimSun**              | 宋体     | Windows 默认 |
| **STSong**              | 华文宋体 | macOS        |
| **FangSong**            | 仿宋     | 公文         |

## 6. 实用脚本

### 6.1 批量转换

```bash
# 将目录下所有 Markdown 文件转为 HTML
for file in *.md; do
  pandoc "$file" -o "${file%.md}.html" --standalone --metadata title="${file%.md}"
done
```

### 6.2 生成幻灯片

```bash
# Markdown → Reveal.js 幻灯片
pandoc slides.md -t revealjs -o slides.html \
  --standalone \
  -V revealjs-url=https://cdn.jsdelivr.net/npm/reveal.js@4

# Markdown → Beamer PDF 幻灯片
pandoc slides.md -t beamer -o slides.pdf \
  --pdf-engine=xelatex \
  -V documentclass=ctexbeamer
```

### 6.3 合并文档

```bash
# 合并多个 Markdown 文件为一本书
pandoc chapter1.md chapter2.md chapter3.md \
  -o book.pdf \
  --pdf-engine=xelatex \
  -V documentclass=ctexbook \
  --toc \
  -V toc-title="目录"
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
| 转换工具 | 018-ConversionTool | 本文自身 |
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
