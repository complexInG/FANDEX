---
order: 58
title: 阴影
module: css
category: CSS
difficulty: beginner
description: 'box-shadow、text-shadow'
author: fanquanpp
updated: '2026-08-01'
related:
  - css/层叠上下文
  - css/渐变
  - css/背景增强
  - css/Grid网格布局
prerequisites:
  - css/概述与基本语法
---

# CSS 阴影

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. box-shadow

```css
box-shadow: offset-x offset-y blur-radius spread-radius color inset;
```

```css
.box {
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
}
.box {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}
.box {
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.07),
    0 2px 4px rgba(0, 0, 0, 0.07),
    0 4px 8px rgba(0, 0, 0, 0.07);
}
```

## 2. text-shadow

```css
.text {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
.neon {
  text-shadow:
    0 0 7px #fff,
    0 0 42px #0fa,
    0 0 82px #0fa;
}
```

## 3. 实战效果

```css
.card {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
  transition: box-shadow 0.3s;
}
.card:hover {
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
}

.elevation-1 {
  box-shadow:
    0 1px 3px rgba(0, 0, 0, 0.12),
    0 1px 2px rgba(0, 0, 0, 0.24);
}
.elevation-2 {
  box-shadow:
    0 3px 6px rgba(0, 0, 0, 0.16),
    0 3px 6px rgba(0, 0, 0, 0.23);
}
```

## 4. drop-shadow 滤镜

```css
.icon {
  filter: drop-shadow(2px 4px 6px rgba(0, 0, 0, 0.3));
}
```

box-shadow 沿盒子形状，drop-shadow 沿元素实际轮廓（适合 PNG 图标）。
## box-shadow 盒阴影

**基本写法：外阴影**
`box-shadow: <水平偏移> <垂直偏移> <模糊> <颜色>;`
```css
/* 设置外阴影 */
.box {
  box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：带扩展的外阴影**
`box-shadow: <水平> <垂直> <模糊> <扩展> <颜色>;`
```css
/* 设置带扩展的外阴影 */
.box {
  box-shadow: 2px 4px 8px 2px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：内阴影**
`box-shadow: inset <水平> <垂直> <模糊> <颜色>;`
```css
/* 设置内阴影 */
.box {
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
}
```

---

**基本写法：无阴影**
`box-shadow: none;`
```css
/* 移除阴影 */
.box {
  box-shadow: none;
}
```

---

**单行写法：多重阴影**
`box-shadow: <阴影1>, <阴影2>;`
```css
/* 单行设置多重阴影 */
.box {
  box-shadow: 0 2px 4px rgba(0,0,0,0.2), 0 4px 8px rgba(0,0,0,0.1);
}
```

---

**换行写法：多重阴影**
`box-shadow: <阴影1>, <阴影2>, <阴影3>;`
```css
/* 换行设置多重阴影 */
.box {
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.1),
    0 4px 8px rgba(0, 0, 0, 0.1),
    0 16px 32px rgba(0, 0, 0, 0.1);
}
```

---

## 常见阴影效果

**基本写法：柔和阴影**
`box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);`
```css
/* 柔和的卡片阴影 */
.card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：深阴影**
`box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);`
```css
/* 较深的阴影 */
.modal {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}
```

---

**基本写法：底部阴影**
`box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);`
```css
/* 仅底部阴影 */
.header {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：四周阴影**
`box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);`
```css
/* 四周均匀阴影 */
.box {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：彩色阴影**
`box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);`
```css
/* 彩色阴影效果 */
.button {
  box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
}
```

---

## 材料设计阴影

**基本写法：Material 阴影 1 级**
`box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);`
```css
/* Material Design 1 级阴影 */
.z1 {
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}
```

---

**基本写法：Material 阴影 2 级**
`box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);`
```css
/* Material Design 2 级阴影 */
.z2 {
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
}
```

---

**基本写法：Material 阴影 3 级**
`box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);`
```css
/* Material Design 3 级阴影 */
.z3 {
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
}
```

---

**基本写法：Material 阴影 4 级**
`box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);`
```css
/* Material Design 4 级阴影 */
.z4 {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}
```

---

**基本写法：Material 阴影 5 级**
`box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);`
```css
/* Material Design 5 级阴影 */
.z5 {
  box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
}
```

---

## text-shadow 文字阴影

**基本写法：文字阴影**
`text-shadow: <水平> <垂直> <模糊> <颜色>;`
```css
/* 设置文字阴影 */
.title {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
```

---

**基本写法：文字发光**
`text-shadow: 0 0 10px <颜色>;`
```css
/* 文字发光效果 */
.glow {
  text-shadow: 0 0 10px rgba(0, 123, 255, 0.8);
}
```

---

**基本写法：文字描边**
`text-shadow: <方向1> <颜色>, <方向2> <颜色>, <方向3> <颜色>, <方向4> <颜色>;`
```css
/* 文字描边效果 */
.outline {
  text-shadow:
    -1px -1px 0 #000,
    1px -1px 0 #000,
    -1px 1px 0 #000,
    1px 1px 0 #000;
}
```

---

**单行写法：多重文字阴影**
`text-shadow: <阴影1>, <阴影2>;`
```css
/* 单行设置多重文字阴影 */
.text {
  text-shadow: 1px 1px 2px black, 0 0 10px blue;
}
```

---

**换行写法：多重文字阴影**
`text-shadow: <阴影1>, <阴影2>, <阴影3>;`
```css
/* 换行设置多重文字阴影 */
.text {
  text-shadow:
    1px 1px 2px black,
    0 0 10px blue,
    0 0 20px darkblue;
}
```

---

## drop-shadow 滤镜阴影

**基本写法：drop-shadow 滤镜**
`filter: drop-shadow(<水平> <垂直> <模糊> <颜色>);`
```css
/* 使用滤镜创建阴影（跟随形状） */
.image {
  filter: drop-shadow(2px 4px 8px rgba(0, 0, 0, 0.3));
}
```

---

**基本写法：PNG 阴影**
`filter: drop-shadow(<水平> <垂直> <模糊> <颜色>);`
```css
/* 为透明 PNG 创建跟随形状的阴影 */
.logo {
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
}
```

---

## 阴影动画

**基本写法：阴影过渡**
`transition: box-shadow <时长>;`
```css
/* 阴影过渡动画 */
.card {
  transition: box-shadow 0.3s;
}
.card:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：阴影悬停效果**
`<选择器>:hover { box-shadow: <阴影>; }`
```css
/* 悬停时增强阴影 */
.button {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
}
.button:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：阴影按下效果**
`<选择器>:active { box-shadow: <阴影>; }`
```css
/* 按下时减弱阴影 */
.button:active {
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}
```

---

## 阴影变量

**基本写法：定义阴影变量**
`:root { --shadow-<名>: <阴影值>; }`
```css
/* 定义阴影变量 */
:root {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：使用阴影变量**
`box-shadow: var(--shadow-<名>);`
```css
/* 使用阴影变量 */
.card {
  box-shadow: var(--shadow-md);
}
```

---

## 响应式阴影

**基本写法：clamp 响应式阴影**
`box-shadow: 0 clamp(<最小>, <理想>, <最大>) <模糊> <颜色>;`
```css
/* 响应式阴影 */
.box {
  box-shadow: 0 clamp(2px, 1vw, 8px) 12px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：媒体查询调整阴影**
`@media (max-width: <值>) { box-shadow: <值>; }`
```css
/* 小屏幕调整阴影 */
.card {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
@media (max-width: 768px) {
  .card {
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  }
}
```

---

## 内阴影效果

**基本写法：内凹效果**
`box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);`
```css
/* 创建内凹效果 */
.inset {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：内凸效果**
`box-shadow: inset 0 -2px 4px rgba(0, 0, 0, 0.1);`
```css
/* 创建内凸效果 */
.outset {
  box-shadow: inset 0 -2px 4px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：浮雕效果**
`box-shadow: inset 1px 1px 2px rgba(255,255,255,0.5), inset -1px -1px 2px rgba(0,0,0,0.1);`
```css
/* 创建浮雕效果 */
.embossed {
  box-shadow:
    inset 1px 1px 2px rgba(255,255,255,0.5),
    inset -1px -1px 2px rgba(0,0,0,0.1);
}
```

---

## 长阴影

**单行写法：长阴影**
`box-shadow: <偏移1> <颜色>, <偏移2> <颜色>, <偏移3> <颜色>;`
```css
/* 单行长阴影效果 */
.long-shadow {
  box-shadow: 1px 1px rgba(0,0,0,0.1), 2px 2px rgba(0,0,0,0.1), 3px 3px rgba(0,0,0,0.1);
}
```

---

**换行写法：长阴影**
`box-shadow: <偏移1> <颜色>, <偏移2> <颜色>, <偏移3> <颜色>;`
```css
/* 换行长阴影效果 */
.long-shadow {
  box-shadow:
    1px 1px rgba(0,0,0,0.1),
    2px 2px rgba(0,0,0,0.1),
    3px 3px rgba(0,0,0,0.1),
    4px 4px rgba(0,0,0,0.1),
    5px 5px rgba(0,0,0,0.1);
}
```

---

## 霓虹阴影

**基本写法：霓虹发光**
`box-shadow: 0 0 <模糊> <颜色>, 0 0 <模糊2> <颜色>;`
```css
/* 霓虹发光效果 */
.neon {
  box-shadow: 0 0 5px #007bff, 0 0 10px #007bff;
}
```

---

**基本写法：彩色霓虹**
`box-shadow: 0 0 <模糊> <颜色1>, 0 0 <模糊2> <颜色2>;`
```css
/* 多色霓虹效果 */
.neon-multi {
  box-shadow:
    0 0 5px #ff00ff,
    0 0 10px #00ffff;
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
| 阴影 | 014-Shadow | 本文自身 |
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
