---
order: 67
title: 逻辑属性
module: css
category: CSS
difficulty: intermediate
description: 'margin-inline、margin-block'
author: fanquanpp
updated: '2026-08-01'
related:
  - css/特性查询
  - css/层叠层
  - css/滚动捕捉
  - css/Sass预处理器
prerequisites:
  - css/概述与基本语法
---

## 1. 逻辑属性概述

逻辑属性根据书写模式（writing mode）自动适配方向，替代物理方向属性。

### 物理属性 vs 逻辑属性

| 物理属性        | 逻辑属性              | 说明       |
| --------------- | --------------------- | ---------- |
| `margin-top`    | `margin-block-start`  | 块轴起始   |
| `margin-bottom` | `margin-block-end`    | 块轴结束   |
| `margin-left`   | `margin-inline-start` | 行内轴起始 |
| `margin-right`  | `margin-inline-end`   | 行内轴结束 |
| `width`         | `inline-size`         | 行内尺寸   |
| `height`        | `block-size`          | 块尺寸     |
| `top`           | `inset-block-start`   | 块轴偏移   |
| `left`          | `inset-inline-start`  | 行内轴偏移 |

## 2. 简写属性

```css
/* margin */
margin-block: 10px 20px; /* block-start block-end */
margin-inline: 15px; /* inline-start = inline-end */
margin: 10px 15px; /* block inline */

/* padding */
padding-block: 1rem;
padding-inline: 2rem;

/* inset */
inset-block-start: 0;
inset-inline-start: 0;
inset: 0; /* 四个方向 */

/* size */
inline-size: 100%;
block-size: auto;
```

## 3. 边框与圆角

```css
border-block-start: 1px solid #ccc;
border-inline-end: 2px dashed #999;
border-start-start-radius: 8px; /* 行内起始 + 块起始 */
border-end-end-radius: 8px; /* 行内结束 + 块结束 */
```

## 4. 书写模式适配

```css
/* 水平书写模式（默认） */
.element {
  writing-mode: horizontal-tb;
}
/* margin-block-start = margin-top */

/* 垂直书写模式 */
.element {
  writing-mode: vertical-rl;
}
/* margin-block-start = margin-right */
```

## 5. 国际化支持

```css
/* 自动适配 RTL 语言 */
[dir='rtl'] .element {
  /* 无需额外样式 */
}

/* 使用逻辑属性后，RTL 自动适配 */
.element {
  margin-inline-start: 1rem; /* LTR: left, RTL: right */
  padding-inline-end: 2rem;
}
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
