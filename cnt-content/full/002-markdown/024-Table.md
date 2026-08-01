---
order: 80
tags:
  - markdown
difficulty: intermediate
title: 'Markdown 表格'
module: markdown
category: 'Markdown Basics'
description: 表格语法、对齐方式与复杂表格处理。
author: fanquanpp
updated: '2026-08-01'
related:
  - markdown/版本控制下的PR协作
  - markdown/代码块与语法高亮
  - markdown/语法速查
  - markdown/规范文档编写
prerequisites:
  - markdown/语法指南
---
## 1. 基本表格语法

**语法**：

```markdown
| 表头 1   | 表头 2   | 表头 3   |
| -------- | -------- | -------- |
| 单元格 1 | 单元格 2 | 单元格 3 |
| 单元格 4 | 单元格 5 | 单元格 6 |
```

**示例**：

```markdown
| 姓名 | 年龄 | 城市 |
| ---- | ---- | ---- |
| 张三 | 25   | 北京 |
| 李四 | 30   | 上海 |
| 王五 | 28   | 广州 |
```

**渲染效果**：

| 姓名 | 年龄 | 城市 |
| ---- | ---- | ---- |
| 张三 | 25   | 北京 |
| 李四 | 30   | 上海 |
| 王五 | 28   | 广州 |

## 2. 表格对齐

**语法**：

- 左对齐：`|:---|`
- 居中对齐：`|:---:|`
- 右对齐：`|---:|`
  **示例**：

```markdown
| 左对齐   | 居中对齐 |   右对齐 |
| :------- | :------: | -------: |
| 内容 1   |  内容 2  |   内容 3 |
| 长内容 1 | 长内容 2 | 长内容 3 |
```

**渲染效果**：

| 左对齐   | 居中对齐 |   右对齐 |
| :------- | :------: | -------: |
| 内容 1   |  内容 2  |   内容 3 |
| 长内容 1 | 长内容 2 | 长内容 3 |

## 3. 表格中的特殊内容

### 3.1 表格中的换行

**语法**：使用 HTML 的 `<br>` 标签
**示例**：

```markdown
| 姓名 | 地址                             |
| ---- | -------------------------------- |
| 张三 | 北京市朝阳区<br>建国路 88 号     |
| 李四 | 上海市浦东新区<br>陆家嘴金融中心 |
```

**渲染效果**：

| 姓名 | 地址                             |
| ---- | -------------------------------- |
| 张三 | 北京市朝阳区<br>建国路 88 号     |
| 李四 | 上海市浦东新区<br>陆家嘴金融中心 |

### 3.2 表格中的链接

**示例**：

```markdown
| 名称   | 链接                         |
| ------ | ---------------------------- |
| GitHub | [GitHub](https://github.com) |
| Google | [Google](https://google.com) |
```

**渲染效果**：

| 名称   | 链接                         |
| ------ | ---------------------------- |
| GitHub | [GitHub](https://github.com) |
| Google | [Google](https://google.com) |

### 3.3 表格中的图片

**示例**：

```markdown
| 名称   | 图标                                                                                 |
| ------ | ------------------------------------------------------------------------------------ |
| GitHub | ![GitHub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png) |
| Google | ![Google](https://www.google.com/favicon.ico)                                        |
```

**渲染效果**：

| 名称   | 图标                                                                                 |
| ------ | ------------------------------------------------------------------------------------ |
| GitHub | ![GitHub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png) |
| Google | ![Google](https://www.google.com/favicon.ico)                                        |

### 3.4 表格中的代码

**示例**：

```markdown
| 语言       | 代码                    |
| ---------- | ----------------------- |
| JavaScript | `console.log('Hello');` |
| Python     | `print('Hello')`        |
```

**渲染效果**：

| 语言       | 代码                    |
| ---------- | ----------------------- |
| JavaScript | `console.log('Hello');` |
| Python     | `print('Hello')`        |

### 3.5 表格中的列表

**示例**：

```markdown
| 名称 | 特点                   |
| ---- | ---------------------- |
| 苹果 | - 红色<br>- 甜<br>- 脆 |
| 香蕉 | - 黄色<br>- 软<br>- 甜 |
```

**渲染效果**：

| 名称 | 特点                   |
| ---- | ---------------------- |
| 苹果 | - 红色<br>- 甜<br>- 脆 |
| 香蕉 | - 黄色<br>- 软<br>- 甜 |

## 4. 复杂表格

### 4.1 合并单元格

**注意**：标准 Markdown 不支持直接合并单元格，但可以使用 HTML 表格标签来实现
**示例**：

```html
<table>
  <tr>
    <th colspan="2">个人信息</th>
  </tr>
  <tr>
    <td>姓名</td>
    <td>张三</td>
  </tr>
  <tr>
    <td>年龄</td>
    <td>25</td>
  </tr>
  <tr>
    <th colspan="2">联系方式</th>
  </tr>
  <tr>
    <td>电话</td>
    <td>13800138000</td>
  </tr>
  <tr>
    <td>邮箱</td>
    <td>zhangsan@example.com</td>
  </tr>
</table>
```

**渲染效果**：

<table>
 <tr>
 <th colspan="2">个人信息</th>
 </tr>
 <tr>
 <td>姓名</td>
 <td>张三</td>
 </tr>
 <tr>
 <td>年龄</td>
 <td>25</td>
 </tr>
 <tr>
 <th colspan="2">联系方式</th>
 </tr>
 <tr>
 <td>电话</td>
 <td>13800138000</td>
 </tr>
 <tr>
 <td>邮箱</td>
 <td>zhangsan@example.com</td>
 </tr>
</table>
### 4.2 嵌套表格

Markdown 原生不支持合并单元格，需要使用 HTML `<table>` 标签实现嵌套结构。

**示例**：

```html
<table>
  <tr>
    <th>类别</th>
    <th>详情</th>
  </tr>
  <tr>
    <td>水果</td>
    <td>苹果、香蕉、橙子</td>
  </tr>
  <tr>
    <td>蔬菜</td>
    <td>西红柿、黄瓜、土豆</td>
  </tr>
  <tr>
    <th colspan="2">联系方式</th>
  </tr>
  <tr>
    <td>电话</td>
    <td>13800138000</td>
  </tr>
  <tr>
    <td>邮箱</td>
    <td>zhangsan@example.com</td>
  </tr>
</table>
```

**渲染效果**：

<table>
  <tr>
    <th>类别</th>
    <th>详情</th>
  </tr>
  <tr>
    <td>水果</td>
    <td>苹果、香蕉、橙子</td>
  </tr>
  <tr>
    <td>蔬菜</td>
    <td>西红柿、黄瓜、土豆</td>
  </tr>
  <tr>
    <th colspan="2">联系方式</th>
  </tr>
  <tr>
    <td>电话</td>
    <td>13800138000</td>
  </tr>
  <tr>
    <td>邮箱</td>
    <td>zhangsan@example.com</td>
  </tr>
</table>

## 5. 最佳实践

### 5.1 表格设计最佳实践

1. **保持表格简洁**：避免创建过于复杂的表格，尽量保持行数和列数适中
2. **使用有意义的表头**：表头应该清晰地描述列的内容
3. **对齐方式一致**：为同一类型的数据使用一致的对齐方式
4. **使用分隔线**：确保表头和数据之间的分隔线清晰可见
5. **添加表格标题**：为重要的表格添加标题，说明表格的用途

### 5.2 表格内容最佳实践

1. **保持数据一致**：确保表格中的数据格式一致
2. **使用简短的内容**：表格单元格中的内容应该简洁明了
3. **避免空单元格**：尽量避免空单元格，使用适当的占位符
4. **使用表格进行比较**：表格最适合用于比较不同项目的属性
5. **考虑响应式设计**：对于宽表格，考虑在移动设备上的显示效果

## 6. 常见问题与解决方案

### 6.1 表格渲染不正确

**问题**：表格没有正确渲染
**解决方案**：

- 确保表头和分隔线之间有正确的格式
- 确保所有行的列数相同
- 检查是否使用了正确的管道符 `|`
- 避免在表格中使用多余的空格

### 6.2 表格在移动设备上显示问题

**问题**：表格在移动设备上显示不完整
**解决方案**：

- 减少表格的列数
- 使用更短的列标题
- 考虑使用 HTML 表格并添加响应式样式
- 对于非常宽的表格，考虑使用横向滚动

### 6.3 表格中的特殊字符

**问题**：表格中的特殊字符导致渲染问题
**解决方案**：

- 对于管道符 `|`，可以使用 `&#124;` 或 `|` 转义
- 对于其他特殊字符，使用适当的 HTML 实体

## 7. 扩展语法

### 7.1 GitHub Flavored Markdown (GFM)

**示例**：

```markdown
| 任务   | 状态            | 负责人 |
| ------ | --------------- | ------ |
| 任务 1 | [完成] 完成     | 张三   |
| 任务 2 | [进行] 进行中   | 李四   |
| 任务 3 | [未开始] 未开始 | 王五   |
```

**渲染效果**：

| 任务   | 状态            | 负责人 |
| ------ | --------------- | ------ |
| 任务 1 | [完成] 完成     | 张三   |
| 任务 2 | [进行] 进行中   | 李四   |
| 任务 3 | [未开始] 未开始 | 王五   |

### 7.2 表格生成工具

为了简化表格的创建，可以使用在线表格生成工具：

- [TablesGenerator](https://www.tablesgenerator.com/markdown_tables)
- [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables)
- [Markdown Table Editor](https://jakewiesler.github.io/markdown-table-editor/)

## 8. 总结

Markdown 表格是一种强大的工具，用于在文档中展示结构化数据。通过掌握基本语法和最佳实践，你可以创建清晰、专业的表格。
在使用表格时，保持简洁明了是关键。避免创建过于复杂的表格，确保表头清晰，数据格式一致，这样可以提高文档的可读性和专业性。
对于复杂的表格需求，可以考虑使用 HTML 表格标签来实现更高级的功能，如合并单元格和更复杂的布局。

---

## 基本表格

**换行写法：创建基本表格**
`| <表头 1> | <表头 2> |\n| --- | --- |\n| <单元格 1> | <单元格 2> |`
```markdown
| 姓名 | 年龄 |
| ---- | ---- |
| 张三 | 25   |
| 李四 | 30   |
```

**换行写法：三列表格**
`| <列 1> | <列 2> | <列 3> |\n| --- | --- | --- |\n| <值 1> | <值 2> | <值 3> |`
```markdown
| 姓名 | 年龄 | 城市 |
| ---- | ---- | ---- |
| 张三 | 25   | 北京 |
| 李四 | 30   | 上海 |
```

---

## 表格对齐

**单行写法：左对齐列**
`| :--- |`
```markdown
| 左对齐 |
| :----- |
| 内容   |
```

**单行写法：居中对齐列**
`| :---: |`
```markdown
| 居中对齐 |
| :------: |
|   内容   |
```

**单行写法：右对齐列**
`| ---: |`
```markdown
| 右对齐 |
| -----: |
|   内容 |
```

**换行写法：混合对齐表格**
`| :--- | :---: | ---: |`
```markdown
| 左对齐   | 居中对齐 | 右对齐 |
| :------- | :------: | -----: |
| 内容 1   |  内容 2  |   内容 3 |
```

---

## 表格中的特殊内容

**单行写法：表格中换行使用 br 标签**
`| <文本><br><文本> |`
```markdown
| 地址 |
| ---- |
| 北京市朝阳区<br>建国路 88 号 |
```

**单行写法：表格中的链接**
`| [<文本>](<URL>) |`
```markdown
| 链接 |
| ---- |
| [GitHub](https://github.com) |
```

**单行写法：表格中的行内代码**
`| `<代码>` |`
```markdown
| 代码 |
| ---- |
| `print('Hello')` |
```

**单行写法：表格中转义管道符**
`| <文本>\|<文本> |`
```markdown
| 命令 |
| ---- |
| `grep \| file` |
```

---

## 合并单元格

**换行写法：使用 HTML colspan 合并单元格**
`<th colspan="<N>">`
```markdown
<table>
  <tr>
    <th colspan="2">个人信息</th>
  </tr>
  <tr>
    <td>姓名</td>
    <td>张三</td>
  </tr>
</table>
```

**换行写法：使用 HTML rowspan 合并单元格**
`<td rowspan="<N>">`
```markdown
<table>
  <tr>
    <td rowspan="2">部门 A</td>
    <td>张三</td>
  </tr>
  <tr>
    <td>李四</td>
  </tr>
</table>
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
| 图片CDN加速 | 021-ImageCDNAcceleration | 本文的并列主题 |
| 版本控制下的PR协作 | 022-VCSPRCollaboration | 本文的并列主题 |
| Markdown 代码块与语法高亮 | 023-CodeBlockSyntaxHighlight | 本文的并列主题 |
| Markdown 表格 | 024-Table | 本文自身 |
| 规范文档编写 | 025-SpecDocumentWriting | 本文的并列主题 |
| Markdown 高级语法与文档自动化 | 026-AdvancedSyntaxDocumentAutomation | 本文的并列主题 |
| Markdown 任务列表 | 027-TaskList | 本文的并列主题 |
| Markdown 定义列表 | 028-DefinitionList | 本文的并列主题 |
| Markdown 提示框（admonition/callout） | 029-AdmonitionCallout | 本文的并列主题 |
| Markdown HTML 内嵌 | 030-HtmlEmbed | 本文的并列主题 |
| Markdown 引用与嵌套列表语法速查 | 031-BlockquoteNestedList | 本文的并列主题 |
| Markdown Frontmatter YAML 语法速查 | 032-FrontmatterYAML | 本文的并列主题 |
