---
order: 490
title: CSS 原生嵌套语法速查手册
module: 007-css
category: '007-css'
difficulty: beginner
description: CSS 原生嵌套语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# CSS 原生嵌套语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础嵌套

**基本写法：子代选择器嵌套**
```css
/* 子选择器直接写在父规则内 */
.card {
  background: white;

  .title {
    font-weight: bold;
  }

  .body {
    padding: 15px;
  }
}
/* 等价于 .card { } .card .title { } .card .body { } */
```

---

**基本写法：& 嵌套选择器**
`&`
```css
/* & 代表父选择器，用于复合或附加 */
.button {
  background: blue;
  &:hover { background: darkblue; }       /* .button:hover */
  &.primary { border-color: navy; }       /* .button.primary */
  & > span { font-weight: bold; }         /* .button > span */
}
```

---

**基本写法：& 用于伪类伪元素**
```css
.link {
  color: blue;
  &:hover { color: darkblue; }
  &:focus-visible { outline: 2px solid; }
  &::before { content: "›"; }
}
```

---

## 嵌套使用场景

**基本写法：组合选择器**
`&<复合>`
```css
/* 父子复合（无空格） */
.card {
  &.active { border-color: green; }
  &[disabled] { opacity: 0.5; }
  &:nth-child(2n) { background: #f5f5f5; }
}
```

---

**基本写法：后代选择器（不带 &）**
```css
/* 不带 & 时自动加空格，作用于后代 */
.navbar {
  .brand { font-weight: bold; }
  .links { margin-left: auto; }
  .links .link { padding: 0 15px; }
}
```

---

**基本写法：& 后置反转上下文**
`<选择器> &`
```css
/* 把 & 放后面，反转父子关系 */
.card {
  .dark-theme & {
    background: #333;
    color: #eee;
  }
}
/* 等价 .dark-theme .card { } */
```

---

**基本写法：多次使用 &**
```css
/* & 可在嵌套选择器中多次出现 */
.button {
  & + & { margin-left: 8px; }      /* 相邻兄弟 button */
  & ~ & { opacity: 0.8; }
}
```

---

## 嵌套 at 规则

**基本写法：嵌套 @media**
```css
/* 媒体查询直接写在组件规则内 */
.navbar {
  display: flex;

  @media (max-width: 768px) {
    display: block;
    .links { display: none; }
  }

  @media (prefers-color-scheme: dark) {
    background: #222;
  }
}
```

---

**基本写法：嵌套 @supports / @container**
```css
.card {
  @supports (backdrop-filter: blur(10px)) {
    backdrop-filter: blur(10px);
  }

  @container (min-width: 400px) {
    flex-direction: row;
  }
}
```

---

## 混合声明与规则

**基本写法：声明与嵌套混合**
```css
/* 属性声明与嵌套规则可同时存在 */
.card {
  background: white;        /* 属性 */
  border-radius: 8px;

  .title { font-weight: bold; }   /* 嵌套规则 */
  &:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
}
```

---

## 注意事项速查

**基本写法：HTML 元素需用 & 前缀（旧浏览器兼容）**
```css
/* 标签选择器嵌套建议加 &，兼容 Safari 17.2 之前 */
.box {
  & h2 { color: red; }    /* 推荐：所有浏览器支持 */
  /* h2 { color: red; } */ /* Safari 17.1 及之前可能无效 */
}

/* class / id 嵌套无需 & */
.box {
  .title { color: red; }  /* 兼容性好 */
}
```

---

**基本写法：避免过度嵌套**
```css
/* 不推荐：嵌套过深 */
.card {
  .body {
    .content {
      .item {
        .title { color: red; }   /* 4 层，难以覆盖 */
      }
    }
  }
}

/* 推荐：保持 2-3 层，配合 BEM 或扁平选择器 */
.card .item .title { color: red; }
```

---

**基本写法：& 不能代表伪元素**
```css
/* & 类似 :is()，不能表示 ::before/::after */
.parent {
  &::before { content: ""; }      /* 正确：直接写伪元素 */
  /* .child &::before 会被忽略，因 :is() 不支持伪元素 */
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
| CSS新特性 | 041-CSSNewFeatures | 本文的并列主题 |
| CSS性能优化详解 | 042-CSSPerformanceOptimizationDetailed | 本文的性能延伸 |
| HTML语义化与SEO优化 | 043-HTMLSemanticSEO | 本文的性能延伸 |
| 响应式图片 | 044-ResponsiveImage | 本文的并列主题 |
| CSS 项目示例：响应式个人主页 | 045-CSSProjectExampleResponsiveHomepage | 本文的综合应用 |
| CSS Grid 布局速查 | 046-Grid | 本文的并列主题 |
| CSS transform 与 3D 变换语法速查手册 | 047-Transform3D | 本文的并列主题 |
| CSS @scope 规则语法速查手册 | 048-ScopeAtRule | 本文的并列主题 |
| CSS 原生嵌套语法速查手册 | 049-CSSNesting | 本文自身 |
| CSS 现代色彩空间语法速查手册 | 050-ModernColorSpace | 本文的并列主题 |
