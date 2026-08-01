---
order: 470
title: CSS transform 与 3D 变换语法速查手册
module: 007-css
category: '007-css'
difficulty: beginner
description: CSS transform 与 3D 变换语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 2D 变换

**基本写法：平移**
`transform: translate(<tx>, <ty>);`
```css
/* 沿 X/Y 轴平移 */
.box { transform: translate(50px, 20px); }
.box { transform: translateX(50px); }
.box { transform: translateY(20px); }
.box { transform: translate(-50%, -50%); }  /* 常用于居中 */
```

---

**基本写法：缩放**
`transform: scale(<sx> [, <sy>]);`
```css
/* 缩放比例，1 为原始大小 */
.box { transform: scale(2); }          /* 整体放大 2 倍 */
.box { transform: scale(2, 0.5); }     /* X 放大 2 倍 Y 缩小一半 */
.box { transform: scaleX(1.5); }
.box { transform: scaleY(0.8); }
```

---

**基本写法：旋转**
`transform: rotate(<角度>);`
```css
/* 顺时针旋转 */
.box { transform: rotate(45deg); }
.box { transform: rotate(0.5turn); }   /* 半圈 */
.box { transform: rotate(-90deg); }
```

---

**基本写法：倾斜**
`transform: skew(<ax> [, <ay>]);`
```css
/* 倾斜变换 */
.box { transform: skew(10deg, 5deg); }
.box { transform: skewX(15deg); }
.box { transform: skewY(10deg); }
```

---

**基本写法：矩阵变换**
`transform: matrix(<a>, <b>, <c>, <d>, <e>, <f>);`
```css
/* 2D 仿射矩阵，等价于 translate+scale+rotate+skew */
.box { transform: matrix(1, 0, 0, 1, 50, 20); }  /* 等价 translate(50px,20px) */
```

---

## 3D 变换

**基本写法：3D 平移**
`transform: translate3d(<tx>, <ty>, <tz>);`
```css
/* 三轴平移，tz 为 Z 轴（正值朝向观察者） */
.box { transform: translate3d(10px, 20px, 100px); }
.box { transform: translateZ(100px); }
```

---

**基本写法：3D 缩放**
`transform: scale3d(<sx>, <sy>, <sz>);`
```css
/* 三轴缩放 */
.box { transform: scale3d(1.5, 1.5, 1.5); }
.box { transform: scaleZ(2); }
```

---

**基本写法：3D 旋转**
`transform: rotate3d(<x>, <y>, <z>, <角度>);`
```css
/* 绕任意轴旋转，(x,y,z) 为方向向量 */
.box { transform: rotate3d(1, 0, 0, 45deg); }   /* 绕 X 轴 */
.box { transform: rotate3d(0, 1, 0, 45deg); }   /* 绕 Y 轴 */
.box { transform: rotate3d(0, 0, 1, 45deg); }   /* 绕 Z 轴，等价 rotate */
.box { transform: rotate3d(1, 1, 0, 60deg); }   /* 绕对角轴 */

/* 简写 */
.box { transform: rotateX(45deg); }
.box { transform: rotateY(45deg); }
.box { transform: rotateZ(45deg); }
```

---

**基本写法：3D 矩阵**
`transform: matrix3d(<16 个值>);`
```css
/* 4x4 3D 变换矩阵 */
.box { transform: matrix3d(
    1,0,0,0,
    0,1,0,0,
    0,0,1,0,
    50,20,100,1
); }
```

---

**基本写法：透视**
`transform: perspective(<距离>);`
```css
/* 直接在 transform 中设置透视距离 */
.box { transform: perspective(800px) rotateY(45deg); }
```

---

## 多重变换

**基本写法：链式组合**
`transform: <函数1> <函数2> ...;`
```css
/* 从右向左依次应用 */
.box { transform: translate(50px, 0) rotate(45deg); }
.box { transform: scale(1.2) rotateY(30deg) translateZ(50px); }
```

---

## 3D 上下文属性

**基本写法：父级透视**
`perspective: <距离>;`
```css
/* 设置在父元素上，作用于所有子元素的 3D 变换 */
.scene { perspective: 800px; }
.scene .box { transform: rotateY(45deg); }
```

---

**基本写法：透视原点**
`perspective-origin: <x> <y>;`
```css
/* 控制消失点位置 */
.scene { perspective: 800px; perspective-origin: center top; }
.scene { perspective-origin: 25% 75%; }
```

---

**基本写法：变换原点**
`transform-origin: <x> <y> [<z>];`
```css
/* 设置变换中心点 */
.box { transform-origin: center center; }    /* 默认 */
.box { transform-origin: top left; }
.box { transform-origin: 50% 100%; }
.box { transform-origin: 0 0 100px; }        /* 含 Z 轴 */
```

---

**基本写法：变换样式**
`transform-style: flat | preserve-3d;`
```css
/* preserve-3d 让子元素保留 3D 位置 */
.parent { transform-style: preserve-3d; }
```

---

**基本写法：背面可见性**
`backface-visibility: visible | hidden;`
```css
/* 翻转卡片背面隐藏 */
.card { backface-visibility: hidden; }
.back { transform: rotateY(180deg); }
```

---

## 单独变换属性

**基本写法：独立 transform 属性**
`translate: <tx> <ty>;` `rotate: <角度>;` `scale: <sx> <sy>;`
```css
/* 不影响其他变换，便于动画 */
.box { translate: 50px 20px; }
.box { rotate: 45deg; }
.box { scale: 1.2; }
/* 三者独立于 transform，可分别动画化 */
```

---

## 注意事项速查

**基本写法：GPU 加速提示**
`transform: translateZ(0);`
```css
/* 触发 GPU 层提升，常用于性能优化 */
.box { will-change: transform; transform: translateZ(0); }
```

---

**基本写法：变换不影响文档流**
`transform: <函数>`
```css
/* transform 不影响周围元素布局，仅视觉变换 */
.box { transform: rotate(10deg); }  /* 相邻元素不重排 */
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
| CSS transform 与 3D 变换语法速查手册 | 047-Transform3D | 本文自身 |
| CSS @scope 规则语法速查手册 | 048-ScopeAtRule | 本文的并列主题 |
| CSS 原生嵌套语法速查手册 | 049-CSSNesting | 本文的并列主题 |
| CSS 现代色彩空间语法速查手册 | 050-ModernColorSpace | 本文的并列主题 |
