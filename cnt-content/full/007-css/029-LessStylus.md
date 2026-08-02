---
order: 70
title: Less与Stylus
module: css
category: CSS
difficulty: intermediate
description: Less与Stylus
author: fanquanpp
updated: '2026-08-01'
related:
  - css/滚动捕捉
  - css/Sass预处理器
  - css/响应式设计
  - css/PostCSS与构建工具
prerequisites:
  - css/概述与基本语法
---

## 1. Less

Less 是一种 CSS 预处理器，语法接近 CSS，学习成本低。

### 1.1 变量

```less
@primary: #3498db;
@spacing: 1rem;

body {
  color: @primary;
  padding: @spacing;
}
```

### 1.2 混合

```less
.flex-center() {
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  .flex-center();
}
```

### 1.3 嵌套与运算

```less
.nav {
  a {
    color: @primary;
    &:hover {
      opacity: 0.8;
    }
  }
}

@base: 16px;
h1 {
  font-size: @base * 2;
}
```

## 2. Stylus

Stylus 提供更灵活的语法，大括号和分号均可省略。

### 2.1 变量

```stylus
primary = #3498db
spacing = 1rem

body
  color primary
  padding spacing
```

### 2.2 混合

```stylus
flex-center()
  display flex
  justify-content center
  align-items center

.container
  flex-center()
```

### 2.3 函数

```stylus
rem(px)
  (px / 16) * 1rem

h1
  font-size rem(32)
```

## 3. 对比

| 特性 | Sass            | Less        | Stylus     |
| ---- | --------------- | ----------- | ---------- |
| 语法 | SCSS/Sass       | 类 CSS      | 灵活       |
| 变量 | `$`             | `@`         | 自定义     |
| 混合 | @mixin/@include | .class()    | function() |
| 继承 | @extend         | :extend()   | @extend    |
| 条件 | @if/@else       | when guards | if/else    |
| 循环 | @for/@each      | 循环需递归  | for/in     |
| 社区 | 最大            | 较大        | 较小       |

## 延伸阅读
CSS 圆角与形状，见 007-css/018-BorderRadius 文档。
CSS 媒体查询与响应式，见 007-css/019-MediaQuery 文档。
CSS 函数与变量，见 007-css/022-Function 文档。
HTML 结构与语义，见 006-html5 模块。
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
