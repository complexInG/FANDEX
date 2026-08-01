---
order: 72
title: BEM命名方法论
module: css
category: CSS
difficulty: intermediate
description: BEM命名方法论
author: fanquanpp
updated: '2026-08-01'
related:
  - css/响应式设计
  - css/PostCSS与构建工具
  - css/CSS原子化
  - css/CSS模块化
prerequisites:
  - css/概述与基本语法
---

## 1. BEM 概述

BEM（Block Element Modifier）是一种 CSS 命名方法论，提高样式可维护性。

```
.block__element--modifier
```

- **Block**：独立的页面组件（如 `.card`）
- **Element**：Block 的组成部分（如 `.card__title`）
- **Modifier**：Block 或 Element 的变体（如 `.card--featured`）

## 2. 命名规范

```css
/* Block */
.card {
}

/* Element */
.card__title {
}
.card__body {
}
.card__footer {
}

/* Block Modifier */
.card--featured {
}
.card--dark {
}

/* Element Modifier */
.card__title--large {
}
.card__button--primary {
}
```

## 3. 实战示例

```html
<div class="card card--featured">
  <div class="card__header">
    <h2 class="card__title card__title--large">标题</h2>
  </div>
  <div class="card__body">
    <p class="card__text">内容</p>
  </div>
  <div class="card__footer">
    <button class="card__button card__button--primary">操作</button>
  </div>
</div>
```

```css
.card {
  border-radius: 8px;
  padding: 1rem;
  background: white;
}
.card--featured {
  border: 2px solid gold;
}
.card__title {
  font-size: 1.2rem;
}
.card__title--large {
  font-size: 1.5rem;
}
.card__button {
  padding: 8px 16px;
  border: none;
}
.card__button--primary {
  background: blue;
  color: white;
}
```

## 4. 替代方案

| 方法论 | 命名风格                    | 特点       |
| ------ | --------------------------- | ---------- |
| BEM    | `.block__element--modifier` | 语义清晰   |
| SMACSS | 分类命名                    | 按功能分层 |
| OOCSS  | 结构与皮肤分离              | 复用性高   |
| ITCSS  | 倒三角分层                  | 优先级管理 |

## 参考文献

MDN CSS 文档：https://developer.mozilla.org/zh-CN/docs/Web/CSS
CSS 规范（W3C）：https://www.w3.org/Style/CSS/
CSS-Tricks：https://css-tricks.com/
Can I use：https://caniuse.com/
Tailwind CSS：https://tailwindcss.com/

## 延伸阅读

CSS 圆角与形状，见 007-css/018-BorderRadius 文档。
CSS 媒体查询与响应式，见 007-css/019-MediaQuery 文档。
CSS 函数与变量，见 007-css/022-Function 文档。
HTML 结构与语义，见 006-html5 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 CSS 课程。

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
