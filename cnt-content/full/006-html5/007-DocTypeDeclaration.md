---
order: 70
title: 文档类型声明
module: 'html5'
category: 前端技术
difficulty: beginner
description: DOCTYPE与HTML Living Standard
author: fanquanpp
updated: '2026-08-01'
related:
  - 'html5/005-HTML5FormValidation'
  - 'html5/006-HTML5MultimediaCanvasDrawing'
  - 'html5/008-HTML5OfflineStorageWebAPI'
  - 'html5/009-MetadataCharacterEncoding'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 1. DOCTYPE 声明

### 1.1 什么是 DOCTYPE

DOCTYPE（Document Type Declaration）是 HTML 文档的第一行，用于告知浏览器当前文档使用的 HTML 版本和渲染模式。它不是 HTML 标签，而是一条"处理指令"。

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>文档类型声明示例</title>
  </head>
  <body>
    <p>这是一个 HTML5 文档</p>
  </body>
</html>
```

### 1.2 DOCTYPE 的历史演变

| 版本             | DOCTYPE 声明                                                    | 说明          |
| ---------------- | --------------------------------------------------------------- | ------------- |
| HTML 2.0         | `<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">`            | 极其简洁      |
| HTML 4.01 Strict | `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" ...>`        | 包含 DTD 引用 |
| XHTML 1.0        | `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" ...>` | XML 语法      |
| HTML5            | `<!DOCTYPE html>`                                               | 极简声明      |

HTML5 的 DOCTYPE 设计哲学是**向后兼容**与**极简主义**——它不再引用 DTD，因为 HTML5 不再基于 SGML。

### 1.3 标准模式与怪异模式

| 模式             | 触发条件            | 特点                         |
| ---------------- | ------------------- | ---------------------------- |
| **标准模式**     | 存在有效的 DOCTYPE  | 按 W3C 标准渲染              |
| **怪异模式**     | 缺少 DOCTYPE 或无效 | 模拟旧浏览器行为             |
| **几乎标准模式** | 某些过渡型 DOCTYPE  | 除表格单元格高度外按标准渲染 |

**关键差异**：盒模型（怪异模式下 width 包含 padding 和 border）、行内元素尺寸、字体继承、图片间距。

```javascript
// 检测当前渲染模式
if (document.compatMode === 'CSS1Compat') {
  console.log('标准模式');
} else {
  console.log('怪异模式');
}
```

## 2. HTML Living Standard

### 2.1 从 W3C 到 WHATWG

2019 年，W3C 与 WHATWG 达成协议，HTML 和 DOM 规范由 WHATWG 作为唯一发布者维护。HTML 正式成为"活标准"（Living Standard）。

**核心理念**：持续演进、向后兼容、浏览器驱动、社区参与。

### 2.2 规范结构

| 章节           | 内容                       |
| -------------- | -------------------------- |
| Infrastructure | 术语、编码、解析器         |
| Semantics      | 元素语义定义               |
| DOM            | 文档对象模型               |
| Communication  | Web Sockets、Web Messaging |
| Web Workers    | 后台线程                   |

### 2.3 新特性演进时间线

| 年份 | 新增特性                              |
| ---- | ------------------------------------- |
| 2020 | `loading="lazy"`                      |
| 2021 | `<dialog>` 元素、`popover` 属性       |
| 2022 | Container Queries、`:has()` 选择器    |
| 2023 | View Transitions API、`<search>` 元素 |
| 2024 | CSS Anchor Positioning                |
| 2025 | Declarative Shadow DOM                |

## 3. DOCTYPE 最佳实践

- 永远在文档首行声明 DOCTYPE
- 推荐大写 `<!DOCTYPE html>`
- 使用 W3C Markup Validation Service 验证
## DOCTYPE 声明

**HTML5 文档类型声明**
`<!DOCTYPE html>`
```html
<!-- 文档首行声明,触发标准模式 -->
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>文档类型声明示例</title>
  </head>
  <body>
    <p>这是一个 HTML5 文档</p>
  </body>
</html>
```

**DOCTYPE 历史版本对照**

| 版本             | DOCTYPE 声明                                                    |
| ---------------- | --------------------------------------------------------------- |
| HTML 2.0         | `<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">`            |
| HTML 4.01 Strict | `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "...">`      |
| XHTML 1.0        | `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "...">` |
| HTML5            | `<!DOCTYPE html>`                                               |

---

## 渲染模式检测

**渲染模式分类**

| 模式             | 触发条件            | 特点                         |
| ---------------- | ------------------- | ---------------------------- |
| 标准模式         | 存在有效的 DOCTYPE  | 按 W3C 标准渲染              |
| 怪异模式         | 缺少 DOCTYPE 或无效 | 模拟旧浏览器行为             |
| 几乎标准模式     | 某些过渡型 DOCTYPE  | 除表格单元格高度外按标准渲染 |

**JavaScript 检测当前模式**
`document.compatMode`
```javascript
// 检测当前渲染模式
if (document.compatMode === 'CSS1Compat') {
  console.log('标准模式');
} else {
  console.log('怪异模式');
}
```

---

## HTML Living Standard 新特性时间线

| 年份 | 新增特性                              |
| ---- | ------------------------------------- |
| 2020 | `loading="lazy"`                      |
| 2021 | `<dialog>` 元素、`popover` 属性       |
| 2022 | Container Queries、`:has()` 选择器    |
| 2023 | View Transitions API、`<search>` 元素 |
| 2024 | CSS Anchor Positioning                |
| 2025 | Declarative Shadow DOM                |

## 延伸阅读
HTML 列表与链接精讲，见 006-html5/011-List 与 012-LinkageAnchor 文档。
CSS 样式与布局，见 007-css 模块。
JavaScript DOM 操作，见 008-javascript 模块。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 HTML 解析与 DOM 树

浏览器解析 HTML 时先 tokenize 再建树；解析器对错误标记有容错规则（错误恢复算法）。
DOM 是内存中的树结构：元素节点、文本节点、属性；document.querySelector 沿树查找。
渲染流程：HTML -> DOM，CSS -> CSSOM，合并为渲染树，布局与绘制；理解流程可定位性能瓶颈。
脚本与解析：defer 延后执行，async 异步执行，模块脚本默认 defer 语义。

### 13.2 表单校验与无障碍

原生校验：required、pattern、min/max、type 约束；novalidate 可关闭，交由 JS 自定义。
校验 UI：:invalid/:valid 伪类样式；aria-invalid 标记错误；错误信息用 aria-describedby 关联。
键盘可达：所有交互元素可 Tab 聚焦，焦点可见，弹层焦点管理（trap）。
屏幕阅读器测试：NVDA/VoiceOver 实际朗读验证语义。
