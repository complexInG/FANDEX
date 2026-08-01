---
order: 56
title: 层叠上下文
module: css
category: CSS
difficulty: intermediate
description: 'z-index'
author: fanquanpp
updated: '2026-08-01'
related:
  - css/定位详解
  - css/浮动与清除
  - css/渐变
  - css/阴影
prerequisites:
  - css/概述与基本语法
---

## 概述

层叠上下文（Stacking Context）是 CSS 中决定元素在 Z 轴上渲染顺序的机制。每个层叠上下文都是一个独立的三维概念空间，内部元素的层叠顺序不会影响外部。理解层叠上下文对于解决 z-index 失效、元素被意外遮挡等问题至关重要。层叠上下文的创建条件、层叠顺序规则以及嵌套关系是掌握 CSS 布局深度的关键。

## 基础概念

**层叠上下文**：一个 HTML 元素如果满足特定条件，就会创建一个新的层叠上下文。在同一个层叠上下文中，元素按照固定的层叠顺序规则进行排列。

**层叠顺序**：同一个层叠上下文内，元素从底到顶的渲染顺序依次为：背景/边框、负 z-index、常规流块级盒子、浮动盒子、常规流行内盒子、z-index:0 的定位元素、正 z-index 的定位元素。

**z-index**：仅对定位元素（position 不为 static）生效，用于控制同一层叠上下文内定位元素的层叠顺序。z-index 值越大，元素越靠近用户。

**嵌套规则**：子层叠上下文整体参与父层叠上下文的层叠顺序比较。子元素的 z-index 无论多大，都无法超越父层叠上下文的限制。

## 快速上手

### 层叠顺序演示

```html
<div class="container">
  <!-- 常规流块级盒子 - 层叠顺序较低 -->
  <div class="block">常规流块级盒子</div>

  <!-- 浮动盒子 - 高于常规流 -->
  <div class="float">浮动盒子</div>

  <!-- 定位元素 + z-index - 层叠顺序最高 -->
  <div class="positioned">定位元素 z-index: 1</div>
</div>
```

```css
.container {
  position: relative;
}

.block {
  background: #e3f2fd;
  padding: 20px;
}

.float {
  float: left;
  background: #fff3e0;
  padding: 20px;
  margin-left: -50px; /* 与块级盒子重叠 */
}

.positioned {
  position: relative;
  z-index: 1;
  background: #e8f5e9;
  padding: 20px;
  margin-top: -30px; /* 与其他元素重叠 */
}
```

### z-index 基本用法

```css
/* z-index 仅对定位元素生效 */
.dropdown {
  position: absolute;
  z-index: 100; /* 显示在普通元素之上 */
}

.modal-overlay {
  position: fixed;
  z-index: 1000; /* 模态框层叠更高 */
}

.toast {
  position: fixed;
  z-index: 2000; /* 提示信息在最顶层 */
}
```

## 详细用法

### 创建层叠上下文的条件

```css
/* 方式一：position + z-index（最常见） */
.element-1 {
  position: relative;
  z-index: 0; /* 即使是 0 也会创建层叠上下文 */
}

/* 方式二：opacity 小于 1 */
.element-2 {
  opacity: 0.99; /* 创建新的层叠上下文 */
}

/* 方式三：transform */
.element-3 {
  transform: translateZ(0); /* 常用于硬件加速，同时创建了层叠上下文 */
}

/* 方式四：filter */
.element-4 {
  filter: blur(0); /* 即使模糊为 0 也会创建层叠上下文 */
}

/* 方式五：will-change */
.element-5 {
  will-change: transform; /* 提示浏览器该属性将变化，创建层叠上下文 */
}

/* 方式六：isolation（推荐方式） */
.element-6 {
  isolation: isolate; /* 专门用于创建层叠上下文，无副作用 */
}

/* 方式七：其他属性 */
.element-7 {
  -webkit-overflow-scrolling: touch; /* 移动端滚动 */
}

.element-8 {
  contain: layout; /* CSS Containment */
}
```

### 层叠顺序七层模型

```css
/*
 * 同一层叠上下文内的层叠顺序（从底到顶）：
 *
 * 第1层：层叠上下文的背景和边框
 * 第2层：z-index 为负的定位元素
 * 第3层：常规流中的块级盒子
 * 第4层：浮动盒子（非定位）
 * 第5层：常规流中的行内盒子（文字、行内元素等）
 * 第6层：z-index: 0 / auto 的定位元素
 * 第7层：z-index 为正的定位元素
 */

/* 负 z-index 示例：会跑到父元素背景下面 */
.behind-background {
  position: absolute;
  z-index: -1;
}

/* 行内元素层叠高于块级元素 */
.block-element {
  display: block;
  background: #ffcc00;
}

.inline-element {
  display: inline;
  background: #00ccff;
  /* 行内元素会覆盖块级元素的背景 */
}
```

### 嵌套层叠上下文

```html
<!-- 子层叠上下文无法超越父层叠上下文 -->
<div class="parent">
  <div class="child-high">子元素 z-index: 9999</div>
</div>
<div class="sibling">兄弟元素 z-index: 2</div>
```

```css
.parent {
  position: relative;
  z-index: 1; /* 父元素创建层叠上下文，z-index 为 1 */
}

.child-high {
  position: absolute;
  z-index: 9999;
  /* 虽然子元素 z-index 很大，但父层叠上下文 z-index 只有 1 */
  /* 所以整体仍然在 z-index: 2 的兄弟元素下面 */
}

.sibling {
  position: relative;
  z-index: 2; /* 父层叠上下文 z-index:1 < 2，所以兄弟元素在上面 */
}
```

## 常见场景

### 下拉菜单与导航栏

```css
/* 导航栏层叠 */
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
}

/* 下拉菜单在导航栏之上 */
.dropdown-menu {
  position: absolute;
  z-index: 110;
}

/* 模态框覆盖一切 */
.modal-backdrop {
  position: fixed;
  z-index: 1000;
}

.modal-content {
  position: fixed;
  z-index: 1010;
}
```

### 卡片悬浮效果

```css
.card {
  position: relative;
  transition:
    transform 0.3s,
    box-shadow 0.3s;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  /* transform 创建了新的层叠上下文 */
  /* 悬浮的卡片会覆盖相邻卡片 */
}

.card .overlay {
  position: absolute;
  inset: 0;
  z-index: 1; /* 在卡片内容之上 */
  background: rgba(0, 0, 0, 0.5);
  opacity: 0;
  transition: opacity 0.3s;
}

.card:hover .overlay {
  opacity: 1;
}
```

## 注意事项

- **z-index 失效排查**：z-index 不生效时，首先检查元素是否为定位元素（position 不为 static），其次检查是否被父层叠上下文限制。
- **避免 z-index 军备竞赛**：不要随意使用过大的 z-index 值（如 99999），应使用 CSS 变量统一管理层叠级别。
- **隐式创建层叠上下文**：opacity、transform、filter 等属性会隐式创建层叠上下文，可能导致 z-index 行为与预期不符。排查问题时注意检查这些属性。
- **推荐使用 isolation**：当需要创建层叠上下文但不希望产生其他副作用时，使用 `isolation: isolate` 是最安全的方式。
- **Flex/Grid 子元素**：在 Flex 和 Grid 布局中，子元素的 z-index 即使没有设置 position 也能生效，因为 Flex/Grid 子元素默认具有层叠上下文能力。

## 进阶用法

### CSS 变量管理层叠级别

```css
:root {
  /* 统一管理层叠级别，避免 z-index 军备竞赛 */
  --z-base: 1;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-fixed: 300;
  --z-modal-backdrop: 400;
  --z-modal: 500;
  --z-popover: 600;
  --z-tooltip: 700;
  --z-toast: 800;
}

.dropdown {
  position: absolute;
  z-index: var(--z-dropdown);
}

.sticky-header {
  position: sticky;
  z-index: var(--z-sticky);
}

.modal-backdrop {
  position: fixed;
  z-index: var(--z-modal-backdrop);
}

.modal {
  position: fixed;
  z-index: var(--z-modal);
}

.tooltip {
  position: absolute;
  z-index: var(--z-tooltip);
}
```

### 层叠上下文与合成层

```css
/*
 * 浏览器渲染流程：
 * 1. DOM 树构建
 * 2. CSSOM 构建
 * 3. 渲染树（Render Tree）
 * 4. 布局（Layout）
 * 5. 绘制（Paint）
 * 6. 合成（Composite）
 *
 * 层叠上下文影响合成阶段：
 * - 每个层叠上下文可能被提升为独立的合成层
 * - 合成层由 GPU 单独渲染，不影响其他层
 * - 但过多的合成层会消耗显存
 */

/* 使用 will-change 提示浏览器提前优化 */
.animated-element {
  will-change: transform;
  /* 创建合成层，动画更流畅 */
  /* 但不要滥用，每个合成层都消耗内存 */
}

/* 更好的做法：只在需要时添加 */
.animated-element:hover {
  will-change: transform;
}
```

### 调试层叠上下文

```css
/*
 * 调试技巧：
 *
 * 1. Chrome DevTools -> Elements -> Computed -> 搜索 "stacking context"
 * 2. 检查元素的 position 和 z-index
 * 3. 检查父元素是否创建了层叠上下文
 * 4. 临时设置高 z-index 测试是否被父元素限制
 */

/* 快速调试：给可疑元素加红色边框 */
.debug {
  outline: 2px solid red !important;
}

/* 检查是否创建了层叠上下文 */
.debug-stacking {
  isolation: isolate; /* 确认创建层叠上下文 */
}
```

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| CSS3 概述与基本语法 | 001-CSS3OverviewBasicSyntax | 本文的前置基础 |
| CSS3 盒模型详解 | 002-CSS3BoxModelDetailed | 本文的并列主题 |
| CSS3 选择器系统 | 003-CSS3SelectorSystem | 本文的并列主题 |
| 传统布局技术 | 004-TraditionalLayoutTech | 本文的并列主题 |
| CSS3 Flexbox 弹性布局 | 005-CSS3FlexboxFlexLayout | 本文的并列主题 |
| 伪类与伪元素 | 006-PseudoClassPseudoElement | 本文的并列主题 |
| 优先级计算 | 007-PriorityCalculation | 本文的并列主题 |
| 样式表引入方式 | 008-StyleSheetImportMethod | 本文的并列主题 |
| margin合并与塌陷 | 009-MarginCollapse | 本文的并列主题 |
| 定位详解 | 010-PositionDetailed | 本文的并列主题 |
| 浮动与清除 | 011-FloatClear | 本文的并列主题 |
| 层叠上下文 | 012-StackingContext | 本文自身 |
| 渐变 | 013-Gradient | 本文的并列主题 |
| 阴影 | 014-Shadow | 本文的并列主题 |
| 背景增强 | 015-BackgroundEnhancement | 本文的并列主题 |
| CSS3 Grid 网格布局 | 016-CSS3GridGridLayout | 本文的并列主题 |
| CSS 动画与过渡 | 017-CSSAnimationTransition | 本文的并列主题 |
| 边框圆角 | 018-BorderRadius | 本文的并列主题 |
| 媒体查询 | 019-MediaQuery | 本文的并列主题 |
| 容器查询 | 020-ContainerQuery | 本文的并列主题 |
| 移动端适配 | 021-MobileAdaptation | 本文的并列主题 |
| 函数 | 022-Function | 本文的并列主题 |
| CSS 变量与自定义属性 | 023-CSSVariableCustomAttribute | 本文的并列主题 |
| 特性查询 | 024-FeatureQuery | 本文的并列主题 |
| 层叠层 | 025-CascadeLayer | 本文的并列主题 |
| 逻辑属性 | 026-LogicalProperty | 本文的并列主题 |
| 滚动捕捉 | 027-ScrollSnap | 本文的并列主题 |
| Sass | 028-Sass | 本文的并列主题 |
| Less与Stylus | 029-LessStylus | 本文的并列主题 |
| 响应式设计 | 030-ResponsiveDesign | 本文的并列主题 |
| PostCSS | 031-PostCSS | 本文的并列主题 |
| BEM命名方法论 | 032-BEMNamingMethodology | 本文的并列主题 |
| CSS原子化 | 033-CSSAtomic | 本文的并列主题 |
| CSS-Modules | 034-CSSModules | 本文的并列主题 |
| 关键渲染路径优化 | 035-CriticalRenderPathOptimization | 本文的性能延伸 |
| CSS原生嵌套 | 036-CSSNativeNesting | 本文的并列主题 |
| CSS Canvas 绘图 | 037-CSSCanvasDrawing | 本文的并列主题 |
| CSS-in-JS 与高级布局技巧 | 038-CSSInJS | 本文的并列主题 |
| CSS架构方法论 | 039-CSSArchitectureMethodology | 本文的原理深化 |
| CSS 理论知识点 | 040-CSSTheoryKnowledge | 本文的并列主题 |
| CSS新特性 | 041-CSSNewFeatures | 本文的并列主题 |
| CSS性能优化详解 | 042-CSSPerformanceOptimizationDetailed | 本文的性能延伸 |
| HTML语义化与SEO优化 | 043-HTMLSemanticSEO | 本文的性能延伸 |
| 响应式图片 | 044-ResponsiveImage | 本文的并列主题 |
| CSS 项目示例：响应式个人主页 | 045-CSSProjectExampleResponsiveHomepage | 本文的综合应用 |
| CSS Grid 布局速查 | 046-Grid | 本文的并列主题 |
| CSS transform 与 3D 变换语法速查手册 | 047-Transform3D | 本文的并列主题 |
| CSS @scope 规则语法速查手册 | 048-ScopeAtRule | 本文的并列主题 |
| CSS 原生嵌套语法速查手册 | 049-CSSNesting | 本文的并列主题 |
| CSS 现代色彩空间语法速查手册 | 050-ModernColorSpace | 本文的并列主题 |
