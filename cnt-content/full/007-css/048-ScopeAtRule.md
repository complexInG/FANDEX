---
order: 480
title: CSS @scope 规则语法速查手册
module: 007-css
category: '007-css'
difficulty: beginner
description: CSS @scope 规则语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# CSS @scope 规则语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础语法

**基本写法：定义作用域**
`@scope (<根选择器>) { <规则集> }`
```css
/* 样式仅作用于 .card 子树内 */
@scope (.card) {
  p { color: gray; }
  img { border-radius: 8px; }
}
```

---

**基本写法：甜甜圈作用域（带上限）**
`@scope (<根>) to (<下限>) { <规则集> }`
```css
/* 上界 .article-body，下界 figure，中间区域生效 */
@scope (.article-body) to (figure) {
  img { border: 5px solid black; }
}
/* figure 内部的 img 不受影响，形成"甜甜圈洞" */
```

---

**基本写法：行内 @scope（省略前导）**
```html
<!-- <style> 内的 @scope 自动以父元素为根 -->
<parent-element>
  <style>
    @scope {
      p { color: red; }   <!-- 仅作用于 parent-element 内 -->
    }
  </style>
</parent-element>
```

---

## 多根作用域

**基本写法：多根选择器列表**
`@scope (<根1>, <根2>) { <规则集> }`
```css
/* 多个根共享同一组规则 */
@scope (.mike, .jane) {
  p { color: grey; }
}
```

---

**基本写法：多下限选择器**
`@scope (<根>) to (<下限1>, <下限2>) { <规则集> }`
```css
/* 多个下限同时排除 */
@scope (.article) to (.ad, .quote) {
  p { line-height: 1.6; }
}
```

---

## :scope 伪类

**基本写法：引用作用域根**
`:scope`
```css
/* :scope 指向 @scope 的根元素本身 */
@scope (.card) {
  :scope { padding: 16px; }       /* 等价 .card { padding: 16px; } */
  :scope > h2 { margin-top: 0; }  /* .card 的直接 h2 */
}
```

---

**基本写法：:scope 提升优先级**
```css
/* 普通选择器优先级 0-0-1，加 :scope 后为 0-1-1 */
@scope (.card) {
  img { /* 0-0-1 */ }
  :scope img { /* 0-1-1，优先级更高 */ }
}
```

---

## 作用域与嵌套

**基本写法：在 @scope 中嵌套**
```css
/* @scope 内可使用原生嵌套 */
@scope (.card) {
  & { padding: 16px; }
  & .title { font-weight: bold; }
  & :hover { background: #fafafa; }
}
```

---

**基本写法：@scope 嵌套到规则中**
```css
/* 在组件样式块内声明 @scope */
.card {
  color: black;
  @scope (&) to (& .legacy) {
    p { color: inherit; }
  }
}
```

---

## 级联与优先级

**基本写法：作用域邻近性**
```css
/* 当多个 @scope 都匹配时，DOM 距离更近的根胜出 */
/* 级联顺序：来源 > 重要性 > 层级 > 作用域邻近性 > 优先级 > 顺序 */
@scope (.outer) { h3 { color: red; } }
@scope (.inner) { h3 { color: blue; } }   /* 胜出（更近） */
```

---

**基本写法：与 @layer 组合**
```css
/* @scope 可置于层内 */
@layer components {
  @scope (.card) {
    .title { font-size: 1.2rem; }
  }
}
```

---

## 注意事项速查

**基本写法：选择器隔离而非样式隔离**
`@scope (<根>) { <规则> }`
```css
/* @scope 限制选择器匹配范围，但不阻止继承 */
@scope (.card) {
  p { color: red; }   /* 仅匹配 .card 内的 p */
}
/* 父元素继承的样式仍会作用到 .card 内 */
```

---

**基本写法：@scope 不影响自身之外的元素**
```css
/* 避免全局污染 */
p { color: black; }              /* 全局 */
@scope (.special) {
  p { color: red; }              /* 仅 .special 内 */
}
.special 外的 p 仍是黑色
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
| CSS @scope 规则语法速查手册 | 048-ScopeAtRule | 本文自身 |
| CSS 原生嵌套语法速查手册 | 049-CSSNesting | 本文的并列主题 |
| CSS 现代色彩空间语法速查手册 | 050-ModernColorSpace | 本文的并列主题 |
