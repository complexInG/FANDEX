---
order: 500
title: CSS 现代色彩空间语法速查手册
module: css

category: '007-css'
difficulty: beginner
description: CSS 现代色彩空间语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## oklch / oklab 感知均匀色彩

**基本写法：oklch 颜色**
`oklch(<L> <C> <H> [, <alpha>])`
```css
/* L 亮度 0%-100% / 0-1；C 色度 0+；H 色相 0-360 */
.brand {
  color: oklch(60% 0.15 250);          /* 蓝色调 */
  background: oklch(95% 0.02 250);     /* 浅背景 */
  border-color: oklch(50% 0.2 250 / 0.5); /* 带透明度 */
}
```

---

**基本写法：oklab 颜色**
`oklab(<L> <a> <b> [, <alpha>])`
```css
/* 直角坐标形式，a 红-绿轴，b 黄-蓝轴 */
.brand {
  color: oklab(60% 0.1 0.1);
  background: oklab(95% 0 0);   /* 接近中性灰 */
}
```

---

**基本写法：lab / lch 颜色**
`lab(<L> <a> <b> [, <alpha>])`
```css
/* CIE Lab/Lch 色彩空间 */
.brand {
  color: lab(60% 40 30);
  color: lch(60% 50 250);        /* Lch 极坐标形式 */
}
```

---

## 宽色域 color()

**基本写法：display-p3 广色域**
`color(<色彩空间> <R> <G> <B> [, <alpha>])`
```css
/* 超出 sRGB 的鲜艳颜色 */
.vivid {
  color: color(display-p3 1 0 0);          /* 鲜红，sRGB 无法表达 */
  background: color(display-p3 0 1 0);
  border-color: color(display-p3 0 0 1 / 0.5);
}

/* 其他色彩空间 */
.rec2020 { color: color(rec2020 0.8 0.2 0.1); }
.srgb-linear { color: color(srgb-linear 0.5 0.5 0.5); }
```

---

## color-mix() 颜色混合

**基本写法：基本混合**
`color-mix(in <色彩空间>, <颜色1> [<百分比>], <颜色2> [<百分比>])`
```css
/* 在 oklch 中混合红蓝各 50% */
.brand {
  color: color-mix(in oklch, red, blue);
  background: color-mix(in srgb, plum, #f00);
}
```

---

**基本写法：指定百分比**
`color-mix(in <空间>, <颜色> <p1>, <颜色> <p2>)`
```css
/* 60% 红 + 40% 蓝 */
.brand {
  color: color-mix(in oklab, red 60%, blue 40%);
  /* 比例之和可不为 100%，会自动归一化 */
  color: color-mix(in oklch, red 70%, blue 50%);  /* 归一化为 58.3%/41.7% */
}
```

---

**基本写法：极坐标色相插值**
`color-mix(in <极坐标空间> <hue 方法>, <颜色>, <颜色>)`
```css
/* hue 插值方法：shorter / longer / increasing / decreasing */
.brand {
  color: color-mix(in oklch shorter hue, blue, yellow);
  color: color-mix(in lch longer hue, orange, purple);
  color: color-mix(in hsl increasing hue, red, green);
}
```

---

**基本写法：混合生成派生色**
`color-mix(in <空间>, <基色>, <黑|白> <百分比>)`
```css
/* 从主色派生明暗变体 */
:root {
  --brand: oklch(60% 0.2 250);
  --brand-dark:  color-mix(in srgb, var(--brand), black 70%);
  --brand-light: color-mix(in srgb, var(--brand), white 70%);
  --brand-hover: color-mix(in oklch, var(--brand), white 15%);
}
```

---

## 相对颜色语法

**基本写法：从原色派生**
`oklch(from <原色> <L> <C> <H> [, <alpha>])`
```css
/* from 关键字基于已有颜色派生 */
:root {
  --brand: oklch(60% 0.2 250);
  --brand-soft: oklch(from var(--brand) calc(l + 0.1) c h);   /* 提亮 10% */
  --brand-deep: oklch(from var(--brand) calc(l - 0.2) c h);   /* 加深 */
  --brand-muted: oklch(from var(--brand) l calc(c * 0.5) h);  /* 降饱和 */
}
```

---

**基本写法：rgb 相对颜色**
`rgb(from <原色> <R> <G> <B> [, <A>])`
```css
/* 通道变量 r g b / alpha */
.btn {
  --base: #3366cc;
  background: rgb(from var(--base) r g b / 0.5);     /* 仅改透明度 */
  border-color: rgb(from var(--base) calc(r * 0.7) calc(g * 0.7) calc(b * 0.7));
}
```

---

## light-dark() 明暗模式

**基本写法：自动跟随配色**
`light-dark(<亮色>, <暗色>)`
```css
/* 依据 prefers-color-scheme 自动切换 */
:root { color-scheme: light dark; }
.text {
  color: light-dark(#333, #eee);                       /* 亮/暗自动切换 */
  background: light-dark(white, oklch(20% 0.01 250));
  border-color: light-dark(#ccc, #444);
}
```

---

## color-contrast() 对比色

**基本写法：选择最高对比色**
`color-contrast(<背景色> vs <候选1>, <候选2>, ...)`
```css
/* 浏览器自动选择与背景对比度达标的颜色 */
.badge {
  background: #f60;
  color: color-contrast(#f60 vs white, black);   /* 选 black */
}
```

---

## 注意事项速查

**基本写法：oklch 的感知均匀性**
`oklch(<L> <C> <H>)`
```css
/* 同样 L 值不同色相视觉亮度一致，适合生成色阶 */
:root {
  --c-50:  oklch(95% 0.02 250);
  --c-100: oklch(88% 0.06 250);
  --c-500: oklch(60% 0.18 250);
  --c-900: oklch(28% 0.10 250);
}
/* HSL 的 L 不具备此特性，视觉亮度会随色相波动 */
```

---

**基本写法：色彩空间互转**
`color-mix(in <目标空间>, <原色> 100%, <原色> 0%)`
```css
/* 技巧：用 color-mix 把颜色转换到目标色彩空间 */
.converted {
  color: color-mix(in oklch, var(--some-hex) 100%, transparent);
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
| CSS 原生嵌套语法速查手册 | 049-CSSNesting | 本文的并列主题 |
| CSS 现代色彩空间语法速查手册 | 050-ModernColorSpace | 本文自身 |
