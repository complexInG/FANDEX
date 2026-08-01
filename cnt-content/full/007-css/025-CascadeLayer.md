---
order: 66
title: 层叠层
module: css
category: CSS
difficulty: advanced
description: '@layer'
author: fanquanpp
updated: '2026-08-01'
related:
  - css/CSS变量与自定义属性
  - css/特性查询
  - css/逻辑属性
  - css/滚动捕捉
prerequisites:
  - css/概述与基本语法
---
## 1. @layer 概述

CSS 层叠层（Cascade Layers）允许开发者将 CSS 规则分组到不同的层中，控制层叠优先级。

```css
@layer reset, base, components, utilities;

@layer reset {
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
}

@layer base {
  body {
    font-family: sans-serif;
    line-height: 1.6;
  }
}

@layer components {
  .card {
    border-radius: 8px;
    padding: 1rem;
  }
}

@layer utilities {
  .hidden {
    display: none;
  }
}
```

## 2. 层优先级

**后声明的层优先级更高**：reset < base < components < utilities

**未分层的规则优先级最高**（高于所有层）。

## 3. 嵌套层

```css
@layer framework {
  @layer base {
    .btn {
      padding: 8px;
    }
  }
  @layer theme {
    .btn {
      color: blue;
    }
  }
}

/* 引用嵌套层 */
@layer framework.theme {
  .btn {
    color: red;
  }
}
```

## 4. @import 与 @layer

```css
@import url('reset.css') layer(reset);
@import url('base.css') layer(base);
```

## 5. 最佳实践

- 使用 `@layer` 声明层顺序
- 第三方样式放在低优先级层
- 自定义样式放在高优先级层
- 工具类放在最高优先级层
## @layer 定义

**基本写法：定义命名层**
`@layer <层名>;`
```css
/* 声明层叠层 */
@layer base;
@layer components;
@layer utilities;
```

---

**基本写法：定义并写入样式**
`@layer <层名> { <样式> }`
```css
/* 定义层并写入样式 */
@layer base {
  body {
    font-size: 16px;
  }
}
```

---

**单行写法：多层级声明**
`@layer <层1>, <层2>, <层3>;`
```css
/* 单行声明多个层叠层顺序 */
@layer base, components, utilities;
```

---

**换行写法：多层级声明**
`@layer <层1>, <层2>, <层3>;`
```css
/* 换行声明多个层叠层顺序 */
@layer
  base,
  components,
  utilities;
```

---

**基本写法：匿名层**
`@layer { <样式> }`
```css
/* 创建匿名层叠层 */
@layer {
  .box {
    padding: 10px;
  }
}
```

---

## 层优先级

**基本写法：层顺序决定优先级**
`@layer <低优先级>, <中优先级>, <高优先级>;`
```css
/* 后声明的层优先级更高 */
@layer base, components, utilities;
@layer base {
  p { color: black; }
}
@layer utilities {
  p { color: red; }
}
```

---

**基本写法：未分层样式优先**
`<选择器> { <样式> }`
```css
/* 未分层样式优先级高于所有层 */
p {
  color: blue;
}
@layer base {
  p { color: black; }
}
```

---

**基本写法：层内 !important 反转**
`<选择器> { <属性>: <值> !important; }`
```css
/* !important 在层间反转优先级 */
@layer base {
  p { color: black !important; }
}
@layer utilities {
  p { color: red; }
}
```

---

## 嵌套层

**基本写法：嵌套层定义**
`@layer <父层>.<子层> { <样式> }`
```css
/* 定义嵌套层叠层 */
@layer components.buttons {
  .btn {
    padding: 8px 16px;
  }
}
```

---

**基本写法：嵌套层顺序**
`@layer <父层>.<子层1>, <父层>.<子层2>;`
```css
/* 声明嵌套层顺序 */
@layer components.buttons, components.forms;
```

---

**基本写法：嵌套层内定义**
`@layer <父层> { @layer <子层> { <样式> } }`
```css
/* 在父层内定义子层 */
@layer components {
  @layer buttons {
    .btn { padding: 8px; }
  }
  @layer forms {
    .input { padding: 4px; }
  }
}
```

---

## @import 分层导入

**基本写法：@import 导入到层**
`@import url("<文件>") layer(<层名>);`
```css
/* 导入样式到指定层 */
@import url("reset.css") layer(base);
```

---

**基本写法：@import 带媒体查询导入层**
`@import url("<文件>") layer(<层名>) <媒体查询>;`
```css
/* 导入样式到层并应用媒体查询 */
@import url("mobile.css") layer(components) (max-width: 768px);
```

---

## 层与特异性

**基本写法：层优先于特异性**
`@layer <层名> { <高特异性选择器> { <样式> } }`
```css
/* 层优先级高于选择器特异性 */
@layer base {
  #header {
    color: black;
  }
}
.text-red {
  color: red;
}
```

---

**基本写法：同层内特异性生效**
`@layer <层名> { <低特异性>, <高特异性> { <样式> } }`
```css
/* 同一层内特异性正常生效 */
@layer base {
  p { color: black; }
  .highlight { color: red; }
}
```

---

## 实际应用模式

**基本写法：重置层**
`@layer base { <重置样式> }`
```css
/* 将重置样式放入 base 层 */
@layer base {
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
}
```

---

**基本写法：组件层**
`@layer components { <组件样式> }`
```css
/* 将组件样式放入 components 层 */
@layer components {
  .card {
    padding: 16px;
    border: 1px solid #ccc;
  }
}
```

---

**基本写法：工具层**
`@layer utilities { <工具样式> }`
```css
/* 将工具类样式放入 utilities 层 */
@layer utilities {
  .text-center { text-align: center; }
  .mt-4 { margin-top: 1rem; }
}
```

---

**基本写法：主题层**
`@layer theme { <主题样式> }`
```css
/* 将主题样式放入 theme 层 */
@layer theme {
  :root {
    --primary: #007bff;
  }
}
```

---

## 层叠层与级联

**基本写法：层顺序覆盖**
`@layer <低层>, <高层>;`
```css
/* 后声明的层覆盖先声明的层 */
@layer base, theme, components;
@layer base {
  body { background: white; }
}
@layer theme {
  body { background: #f5f5f5; }
}
```

---

**基本写法：层内顺序**
`@layer <层名> { <样式1> <样式2> }`
```css
/* 同层内后定义的覆盖先定义的 */
@layer components {
  .btn { color: black; }
  .btn { color: red; }
}
```

---

## 层与媒体查询

**基本写法：媒体查询中重新排序**
`@media <条件> { @layer <新顺序>; }`
```css
/* 响应式调整层顺序 */
@media (max-width: 768px) {
  @layer base, utilities, components;
}
```

---

**基本写法：层内媒体查询**
`@layer <层名> { @media <条件> { <样式> } }`
```css
/* 在层内使用媒体查询 */
@layer components {
  .container {
    width: 100%;
    @media (min-width: 768px) {
      max-width: 720px;
    }
  }
}
```

---

## 层调试

**基本写法：层顺序检查**
`@layer <层1>, <层2>, <层3>;`
```css
/* 通过声明顺序检查层优先级 */
@layer base, components, utilities;
```

---

**基本写法：层覆盖测试**
`@layer <测试层> { <选择器> { <样式> } }`
```css
/* 临时添加层测试覆盖 */
@layer test {
  .box {
    border: 2px solid red;
  }
}
```

---

## @layer 与 @scope 进阶

**基本写法：@layer 命名层叠层**
`@layer <层1>, <层2>, <层3>;`
```css
/* 通过命名层叠层管理样式优先级 */
@layer reset, base, components, utilities;
@layer reset {
  * { margin: 0; padding: 0; box-sizing: border-box; }
}
@layer utilities {
  .text-center { text-align: center; }
}
```

---

**基本写法：@layer 匿名层**
`@layer { <样式声明> }`
```css
/* 匿名层按声明顺序参与层叠 */
@layer {
  /* 该样式进入匿名层,优先级低于未分层样式 */
  p { line-height: 1.5; }
}
```

---

**基本写法：@scope 与 @layer 对比**
`@layer <层名> { <样式> }  vs  @scope (<选择器>) { <样式> }`
```css
/* @layer 控制优先级,@scope 控制作用范围 */
@layer components {
  /* 通过层序控制优先级 */
  .title { color: black; }
}
@scope (.article) {
  /* 通过作用域限定应用范围 */
  .title { font-size: 1.5rem; }
}
```

---

**基本写法：@scope 与 cascade origins**
`@scope (<根>) to (<下限>) { <样式声明> }`
```css
/* @scope 不影响优先级,仅限定范围 */
@scope (.content) to (.ad) {
  /* 仅作用于 .content 内、.ad 之外 */
  a { color: #007bff; }
}
/* @scope 内样式特异性仍按选择器计算 */
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
| 层叠层 | 025-CascadeLayer | 本文自身 |
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
