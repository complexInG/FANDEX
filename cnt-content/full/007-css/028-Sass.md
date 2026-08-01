---
order: 69
title: Sass
module: css
category: CSS
difficulty: intermediate
description: Sass（变量、嵌套、混合、继承、运算、模块化）
author: fanquanpp
updated: '2026-08-01'
related:
  - css/逻辑属性
  - css/滚动捕捉
  - css/Less与Stylus
  - css/响应式设计
prerequisites:
  - css/概述与基本语法
---

## 1. Sass 概述

Sass 是最流行的 CSS 预处理器，提供变量、嵌套、混合、继承等特性。

### 语法：SCSS（大括号）vs Sass（缩进）

```scss
// SCSS 语法（推荐）
$primary: #3498db;

.btn {
  background: $primary;
  &:hover {
    opacity: 0.8;
  }
}
```

## 2. 变量

```scss
$font-stack: 'Helvetica Neue', sans-serif;
$primary: #3498db;
$spacing: 1rem;

body {
  font-family: $font-stack;
  color: $primary;
}
```

## 3. 嵌套

```scss
.nav {
  ul {
    list-style: none;
  }
  li {
    display: inline-block;
  }
  a {
    text-decoration: none;
    &:hover {
      color: blue;
    } /* & 引用父选择器 */
  }
}
```

## 4. 混合（Mixin）

```scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

@mixin respond-to($breakpoint) {
  @if $breakpoint == md {
    @media (min-width: 768px) {
      @content;
    }
  }
  @if $breakpoint == lg {
    @media (min-width: 1024px) {
      @content;
    }
  }
}

.container {
  @include flex-center;
}
.sidebar {
  @include respond-to(md) {
    width: 25%;
  }
}
```

## 5. 继承（Extend）

```scss
%button-base {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary {
  @extend %button-base;
  background: blue;
}
.btn-secondary {
  @extend %button-base;
  background: gray;
}
```

## 6. 运算与函数

```scss
$base: 16px;
h1 {
  font-size: $base * 2;
}
h2 {
  font-size: $base * 1.5;
}

@function rem($px) {
  @return ($px / 16) * 1rem;
}
h1 {
  font-size: rem(32);
}
```

## 7. 模块化

```scss
// _variables.scss
$primary: #3498db;

// _mixins.scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

// main.scss
@use 'variables' as *;
@use 'mixins' as *;
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
