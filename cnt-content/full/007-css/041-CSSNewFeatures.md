---
order: 101
title: CSS新特性
module: css
category: 'dev-lang'
difficulty: advanced
description: 'CSS现代新特性详解：@container容器查询、@layer层叠层、逻辑属性、:has()选择器。'
author: fanquanpp
updated: '2026-08-01'
related:
  - css/CSS架构方法论
  - css/理论知识点
  - css/CSS性能优化详解
  - css/HTML语义化与SEO优化
prerequisites:
  - css/概述与基本语法
---

## 1. @container 容器查询

### 1.1 基本概念

容器查询允许根据**父容器尺寸**而非视口尺寸应用样式，实现真正的组件级响应式。

```css
/* 定义容器 */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* 根据容器宽度应用样式 */
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}

@container card (min-width: 200px) and (max-width: 399px) {
  .card {
    display: flex;
    flex-direction: column;
  }
}
```

### 1.2 container-type 类型

| 类型          | 说明                       |
| ------------- | -------------------------- |
| `inline-size` | 仅查询行内方向尺寸（宽度） |
| `size`        | 查询行内和块方向尺寸       |
| `normal`      | 默认值，不作为查询容器     |

### 1.3 容器查询单位

| 单位    | 含义              |
| ------- | ----------------- |
| `cqw`   | 容器宽度的 1%     |
| `cqh`   | 容器高度的 1%     |
| `cqi`   | 容器行内尺寸的 1% |
| `cqb`   | 容器块尺寸的 1%   |
| `cqmin` | 容器较小尺寸的 1% |
| `cqmax` | 容器较大尺寸的 1% |

```css
.card-title {
  font-size: clamp(14px, 3cqi, 24px);
}
```

### 1.4 样式查询

```css
/* 查询自定义属性值 */
.card-container {
  --theme: dark;
}

@container style(--theme: dark) {
  .card {
    background: #1a1a2e;
    color: #e0e0e0;
  }
}

@container style(--theme: light) {
  .card {
    background: #ffffff;
    color: #333333;
  }
}
```

## 2. @layer 层叠层

### 2.1 基本概念

`@layer` 允许显式控制样式的层叠优先级，解决第三方库样式覆盖问题。

```css
/* 声明层（顺序决定优先级，后声明的优先级更高） */
@layer reset, base, components, utilities;

/* 各层定义 */
@layer reset {
  *,
  *::before,
  *::after {
    box-sizing: border-box;
    margin: 0;
  }
}

@layer base {
  body {
    font-family: system-ui;
    line-height: 1.6;
  }
  a {
    color: #007bff;
  }
}

@layer components {
  .btn {
    padding: 8px 16px;
    border-radius: 4px;
  }
  .card {
    border: 1px solid #ddd;
    border-radius: 8px;
  }
}

@layer utilities {
  .text-center {
    text-align: center;
  }
  .mt-4 {
    margin-top: 16px;
  }
}
```

### 2.2 层叠优先级

```
无层样式 > utilities > components > base > reset

优先级从低到高：
  @layer reset        ← 最低
  @layer base
  @layer components
  @layer utilities
  无层样式（unlayered） ← 最高
```

### 2.3 嵌套层

```css
@layer framework {
  @layer base {
    /* framework.base */
  }
  @layer components {
    /* framework.components */
  }
}

/* 等效写法 */
@layer framework.base {
  /* ... */
}
@layer framework.components {
  /* ... */
}
```

### 2.4 第三方样式管理

```css
@layer reset, third-party, custom;

@import url('bootstrap.css') layer(third-party);

@layer custom {
  .btn {
    /* 自定义覆盖 */
  }
}
```

## 3. 逻辑属性

### 3.1 物理属性 vs 逻辑属性

| 物理属性           | 逻辑属性               | 说明         |
| ------------------ | ---------------------- | ------------ |
| `margin-left`      | `margin-inline-start`  | 行内起始边距 |
| `margin-right`     | `margin-inline-end`    | 行内结束边距 |
| `margin-top`       | `margin-block-start`   | 块起始边距   |
| `margin-bottom`    | `margin-block-end`     | 块结束边距   |
| `padding-left`     | `padding-inline-start` | 行内起始内距 |
| `width`            | `inline-size`          | 行内尺寸     |
| `height`           | `block-size`           | 块尺寸       |
| `border-left`      | `border-inline-start`  | 行内起始边框 |
| `text-align: left` | `text-align: start`    | 起始对齐     |
| `float: left`      | `float: inline-start`  | 起始浮动     |

### 3.2 简写属性

```css
/* 物理简写 */
margin: 10px 20px; /* top/bottom left/right */

/* 逻辑简写 */
margin-block: 10px; /* block-start block-end */
margin-inline: 20px; /* inline-start inline-end */
margin: 10px 20px; /* 仍然有效，但方向固定 */

/* 完整逻辑简写 */
margin-block-start: 10px;
margin-block-end: 10px;
margin-inline-start: 20px;
margin-inline-end: 20px;
```

### 3.3 RTL 支持

```css
/* 使用逻辑属性自动适配 RTL */
.element {
  margin-inline-start: 16px; /* LTR: margin-left; RTL: margin-right */
  padding-inline-end: 8px; /* LTR: padding-right; RTL: padding-left */
  text-align: start; /* LTR: left; RTL: right */
}
```

```html
<!-- LTR -->
<div dir="ltr" class="element">内容</div>

<!-- RTL -->
<div dir="rtl" class="element">محتوى</div>
```

### 3.4 逻辑属性与定位

```css
.positioned {
  position: absolute;
  inset-block-start: 0; /* top in LTR */
  inset-inline-start: 0; /* left in LTR */
  inset: 0; /* 所有方向（物理简写，但已支持逻辑） */
}
```

## 4. :has() 选择器

### 4.1 基本用法

`:has()` 被称为"CSS 的父选择器"，允许根据子元素状态选择父元素。

```css
/* 包含 img 的 a 标签 */
a:has(img) {
  display: block;
  border: 1px solid #ddd;
}

/* 包含 .error 的表单 */
form:has(.error) {
  border-color: red;
}

/* 有焦点的输入框的标签 */
label:has(+ input:focus) {
  color: #007bff;
  font-weight: 600;
}
```

### 4.2 表单状态样式

```css
/* 必填字段标记 */
input:required + label::after {
  content: ' *';
  color: red;
}

/* 有无效输入的表单组 */
.form-group:has(input:invalid) {
  --border-color: #dc3545;
}

/* 全部填写完成的表单 */
form:has(input:valid):not(:has(input:invalid)) button[type='submit'] {
  opacity: 1;
  pointer-events: auto;
}
```

### 4.3 卡片变体

```css
/* 有图片的卡片 */
.card:has(img) {
  grid-template-rows: 200px 1fr;
}

/* 无图片的卡片 */
.card:not(:has(img)) {
  grid-template-rows: auto;
  padding: 24px;
}
```

### 4.4 主题切换

```css
/* 根据选中的主题单选按钮应用样式 */
body:has(#theme-dark:checked) {
  background: #1a1a2e;
  color: #e0e0e0;
}

body:has(#theme-light:checked) {
  background: #ffffff;
  color: #333333;
}
```

### 4.5 性能考虑

`:has()` 的性能特征：

- 浏览器对 `:has()` 做了优化，不会遍历整个 DOM
- 避免在大型列表上使用复杂的 `:has()` 组合
- 推荐用于结构性选择，而非高频动态样式

## 5. 其他现代特性

### 5.1 :is() 和 :where()

```css
/* :is() — 优先级取参数中最高的 */
:is(h1, h2, h3):hover {
  color: #007bff;
}

/* :where() — 优先级始终为 0 */
:where(.btn, .link) {
  cursor: pointer;
}
```

### 5.2 :not() 增强

```css
/* 排除多个选择器 */
input:not([type='hidden'], [type='submit']) {
  border: 1px solid #ccc;
}
```

### 5.3 accent-color

```css
input[type='checkbox'],
input[type='radio'],
input[type='range'],
progress {
  accent-color: #007bff;
}
```

### 5.4 color-mix()

```css
.button {
  background: color-mix(in srgb, #007bff 80%, white);
  border-color: color-mix(in srgb, #007bff, black 20%);
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
| 层叠上下文 | 012-StackingContext | 本文的并列主题 |
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
| CSS新特性 | 041-CSSNewFeatures | 本文自身 |
| CSS性能优化详解 | 042-CSSPerformanceOptimizationDetailed | 本文的性能延伸 |
| HTML语义化与SEO优化 | 043-HTMLSemanticSEO | 本文的性能延伸 |
| 响应式图片 | 044-ResponsiveImage | 本文的并列主题 |
| CSS 项目示例：响应式个人主页 | 045-CSSProjectExampleResponsiveHomepage | 本文的综合应用 |
| CSS Grid 布局速查 | 046-Grid | 本文的并列主题 |
| CSS transform 与 3D 变换语法速查手册 | 047-Transform3D | 本文的并列主题 |
| CSS @scope 规则语法速查手册 | 048-ScopeAtRule | 本文的并列主题 |
| CSS 原生嵌套语法速查手册 | 049-CSSNesting | 本文的并列主题 |
| CSS 现代色彩空间语法速查手册 | 050-ModernColorSpace | 本文的并列主题 |
