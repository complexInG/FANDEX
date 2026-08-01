---
order: 102
title: CSS性能优化详解
module: css
category: 'dev-lang'
difficulty: advanced
description: CSS性能优化深度指南：关键CSS内联、异步加载、选择器优化、渲染性能提升。
author: fanquanpp
updated: '2026-08-01'
related:
  - css/理论知识点
  - css/CSS新特性
  - css/HTML语义化与SEO优化
  - css/响应式图片
prerequisites:
  - css/概述与基本语法
---

## 1. 关键渲染路径与 CSS

### 1.1 CSS 阻塞渲染

CSS 是渲染阻塞资源，浏览器必须下载并解析所有 CSS 后才能绘制页面：

```
HTML 解析 → 发现 CSS → 下载 CSS → 解析 CSS → 构建 CSSOM → 合并渲染树 → 布局 → 绘制
```

CSSOM 构建时间公式：

$$T_{render} = T_{download} + T_{parse} + T_{CSSOM}$$

### 1.2 优化目标

- 减少 CSS 文件体积
- 减少 CSS 阻塞时间
- 优先加载首屏关键 CSS
- 延迟加载非关键 CSS

## 2. 关键 CSS 内联

### 2.1 原理

将首屏可见内容所需的 CSS（Critical CSS）直接内联到 HTML `<head>` 中，消除额外的网络请求。

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      /* 关键 CSS — 首屏渲染所需 */
      body {
        margin: 0;
        font-family: system-ui;
      }
      .header {
        background: #007bff;
        color: white;
        padding: 16px;
      }
      .hero {
        min-height: 60vh;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .hero__title {
        font-size: 48px;
        font-weight: 700;
      }
    </style>
    <!-- 非关键 CSS 异步加载 -->
    <link
      rel="preload"
      href="/styles/non-critical.css"
      as="style"
      onload="this.onload=null;this.rel='stylesheet'"
    />
    <noscript><link rel="stylesheet" href="/styles/non-critical.css" /></noscript>
  </head>
</html>
```

### 2.2 提取关键 CSS 的工具

```bash
# Critical
npx critical src/index.html --base dist/ --inline true

# Penthouse
npx penthouse https://example.com > critical.css

# Critters（Webpack 插件）
# critters-webpack-plugin 自动内联关键 CSS
```

### 2.3 内联大小控制

```
推荐关键 CSS 大小: < 14 KB（TCP 初始拥塞窗口）
超过 14 KB: 需要额外 RTT，反而降低性能
```

## 3. 异步加载 CSS

### 3.1 preload + onload 模式

```html
<link
  rel="preload"
  href="/styles/main.css"
  as="style"
  onload="this.onload=null;this.rel='stylesheet'"
/>
<noscript><link rel="stylesheet" href="/styles/main.css" /></noscript>
```

### 3.2 media 属性条件加载

```html
<!-- 仅在打印时加载 -->
<link rel="stylesheet" href="/styles/print.css" media="print" />

<!-- 仅在宽屏时加载 -->
<link rel="stylesheet" href="/styles/wide.css" media="(min-width: 1024px)" />

<!-- 仅在暗色模式时加载 -->
<link rel="stylesheet" href="/styles/dark.css" media="(prefers-color-scheme: dark)" />
```

### 3.3 使用 loadCSS 库

```html
<script>
  /*! loadCSS rel=preload polyfill. [c]2017 Filament Group, Inc. MIT License */
  (function (w) {
    'use strict';
    if (!w.loadCSS) {
      w.loadCSS = function () {};
    }
    var rp = (loadCSS.relpreload = {});
    rp.support = (function () {
      var ret;
      try {
        ret = w.document.createElement('link').relList.supports('preload');
      } catch (e) {
        ret = !1;
      }
      return function () {
        return ret;
      };
    })();
    rp.bindMediaToggle = function (link) {
      var finalMedia = link.media || 'all';
      link.addEventListener('load', function () {
        link.media = finalMedia;
      });
      link.media = 'only x';
    };
    rp.poly = function () {
      if (rp.support()) {
        return;
      }
      var links = w.document.getElementsByTagName('link');
      for (var i = 0; i < links.length; i++) {
        var link = links[i];
        if (
          link.rel === 'preload' &&
          link.getAttribute('as') === 'style' &&
          !link.getAttribute('data-loadcss')
        ) {
          link.setAttribute('data-loadcss', true);
          rp.bindMediaToggle(link);
        }
      }
    };
    if (!rp.support()) {
      rp.poly();
      var run = w.setInterval(rp.poly, 500);
      w.addEventListener('load', function () {
        rp.poly();
        w.clearInterval(run);
      });
    }
    if (typeof exports !== 'undefined') {
      exports.loadCSS = loadCSS;
    } else {
      w.loadCSS = loadCSS;
    }
  })(typeof global !== 'undefined' ? global : this);
</script>
```

## 4. 选择器性能优化

### 4.1 选择器匹配方向

浏览器从**右到左**匹配选择器：

```css
/* 浏览器先找所有 .title，再检查是否在 .card 内 */
.card .title {
  color: #333;
}

/* 更高效：直接匹配 */
.card-title {
  color: #333;
}
```

### 4.2 选择器效率排序

从高到低：

```
1. ID 选择器        #header
2. 类选择器         .card
3. 标签选择器       div
4. 相邻兄弟选择器   h2 + p
5. 子选择器         ul > li
6. 后代选择器       ul li
7. 通配选择器       *
8. 属性选择器       [type="text"]
9. 伪类/伪元素      :hover, ::before
```

### 4.3 优化建议

```css
/* 避免 */
div ul li a span {
  color: red;
}
*:not(:empty) {
  margin: 0;
}

/* 推荐 */
.nav-link-text {
  color: red;
}
```

## 5. 渲染性能优化

### 5.1 触发重排的属性

修改以下属性会触发重排（Layout），代价最高：

```
width, height, margin, padding, border-width,
top, right, bottom, left, position,
display, float, clear, font-size, line-height,
text-align, white-space, overflow
```

### 5.2 触发重绘的属性

修改以下属性只触发重绘（Paint），代价中等：

```
color, background, border-color, border-style,
outline, visibility, box-shadow, text-decoration
```

### 5.3 仅触发合成的属性

修改以下属性只触发合成（Composite），代价最低：

```
transform, opacity, filter
```

### 5.4 will-change 提示

```css
/* 提前告知浏览器哪些属性会变化 */
.card:hover {
  will-change: transform;
}

/* 动画结束后移除 */
.card {
  transition: transform 0.3s;
}

.card:hover {
  transform: scale(1.05);
}
```

> 不要滥用 `will-change`，过多声明会消耗 GPU 内存。

### 5.5 contain 属性

```css
.sidebar {
  contain: layout style paint;
  /* 或使用简写 */
  contain: strict; /* 等于 size layout style paint */
  contain: content; /* 等于 layout style paint */
}
```

| 值            | 说明                         |
| ------------- | ---------------------------- |
| `layout`      | 元素布局不影响外部           |
| `style`       | 计数器、引用不影响外部       |
| `paint`       | 子元素不会绘制到元素边界之外 |
| `size`        | 元素尺寸不依赖子元素         |
| `inline-size` | 行内方向尺寸不依赖子元素     |

### 5.6 content-visibility

```css
.below-fold-section {
  content-visibility: auto;
  contain-intrinsic-size: 0 500px; /* 预估高度 */
}
```

`content-visibility: auto` 让浏览器跳过屏幕外元素的渲染，直到它们即将进入视口。可显著提升长页面初始渲染速度。

## 6. CSS 体积优化

### 6.1 PurgeCSS 移除未使用样式

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('@fullhuman/postcss-purgecss')({
      content: ['./src/**/*.html', './src/**/*.vue', './src/**/*.jsx'],
      defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
      safelist: [/^is-/, /^has-/], // 保留动态类名
    }),
  ],
};
```

### 6.2 压缩 CSS

```bash
# 使用 cssnano
npx postcss styles.css -u cssnano -o styles.min.css
```

### 6.3 减少重复

```css
/* 避免 */
.btn-primary {
  background: #007bff;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
}
.btn-secondary {
  background: #6c757d;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
}

/* 推荐：提取公共样式 */
.btn {
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
}
.btn-primary {
  background: #007bff;
}
.btn-secondary {
  background: #6c757d;
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
| CSS性能优化详解 | 042-CSSPerformanceOptimizationDetailed | 本文自身 |
| HTML语义化与SEO优化 | 043-HTMLSemanticSEO | 本文的性能延伸 |
| 响应式图片 | 044-ResponsiveImage | 本文的并列主题 |
| CSS 项目示例：响应式个人主页 | 045-CSSProjectExampleResponsiveHomepage | 本文的综合应用 |
| CSS Grid 布局速查 | 046-Grid | 本文的并列主题 |
| CSS transform 与 3D 变换语法速查手册 | 047-Transform3D | 本文的并列主题 |
| CSS @scope 规则语法速查手册 | 048-ScopeAtRule | 本文的并列主题 |
| CSS 原生嵌套语法速查手册 | 049-CSSNesting | 本文的并列主题 |
| CSS 现代色彩空间语法速查手册 | 050-ModernColorSpace | 本文的并列主题 |
