---
order: 80
title: 样式表引入方式
module: 'css'
category: 前端技术
difficulty: beginner
description: 内联、嵌入、外部、导入
author: fanquanpp
updated: '2026-08-01'
related:
  - 'css/006-PseudoClassPseudoElement'
  - 'css/007-PriorityCalculation'
  - 'css/009-MarginCollapse'
  - 'css/010-PositionDetailed'
prerequisites:
  - 'css/001-CSS3OverviewBasicSyntax'
---


## 1. 四种引入方式

### 内联样式

```html
<p style="color: red;">内联样式</p>
```

优先级最高、无法复用、不推荐。

### 嵌入样式

```html
<style>
  p {
    color: blue;
  }
</style>
```

仅当前页面有效、无法缓存。

### 外部样式表

```html
<link rel="stylesheet" href="styles.css" />
```

可复用、可缓存、**推荐方式**。

### @import 导入

```css
@import url('reset.css');
```

串行加载（性能差）、避免在顶层使用。

## 2. 对比

| 方式    | 复用性 | 缓存 | 性能 | 推荐度     |
| ------- | ------ | ---- | ---- | ---------- |
| 内联    |        |      | 差   | 低         |
| 嵌入    |        |      | 中   | 中       |
| 外部    |        |      | 好   | 极高 |
| @import |        |      | 差   | 中       |

## 3. 关键 CSS 内联

```html
<head>
  <style>
    .hero {
      height: 100vh;
    }
  </style>
  <link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'" />
</head>
```

## 延伸阅读
CSS 圆角与形状，见 007-css/018-BorderRadius 文档。
CSS 媒体查询与响应式，见 007-css/019-MediaQuery 文档。
CSS 函数与变量，见 007-css/022-Function 文档。
HTML 结构与语义，见 006-html5 模块。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 层叠上下文全解

层叠上下文由根、position+z-index、flex/grid 子项 z-index、opacity<1、transform、filter、backdrop-filter、contain、will-change 等创建。
上下文内的 z-index 只在内部比较；子上下文整体参与父级排序。
常见事故：fixed 弹窗被父级 transform 包裹后定位与层级异常。
调试：DevTools 层叠上下文可视化；避免不必要的 will-change。

### 13.2 现代布局：Grid 与容器查询

Grid 模板：grid-template-columns 的 fr、minmax、auto-fill；命名区域提升可读性。
容器查询：container-type: inline-size 定义容器，@container 查询容器宽度，组件可移植。
子网格（subgrid）继承父网格轨道，适合对齐嵌套组件。
浏览器支持与回退：@supports 特性检测；移动端优先降级。
