---
order: 76
title: CSS原生嵌套
module: css
category: CSS
difficulty: intermediate
description: CSS原生嵌套
author: fanquanpp
updated: '2026-08-01'
related:
  - css/CSS模块化
  - css/关键渲染路径优化
  - css/Canvas绘图
  - 'css/CSS-in-JS与高级布局技巧'
prerequisites:
  - css/概述与基本语法
---

## 1. CSS 原生嵌套概述

CSS 原生嵌套（CSS Nesting）允许在选择器内部嵌套子选择器，无需预处理器。

```css
.card {
  padding: 1rem;
  background: white;

  & .title {
    font-size: 1.5rem;
    font-weight: bold;
  }

  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  @media (min-width: 768px) {
    padding: 2rem;
  }
}
```

## 2. 嵌套规则

### 2.1 & 符号

`&` 代表父选择器：

```css
.btn {
  background: blue;

  &:hover {
    background: darkblue;
  }
  &:active {
    transform: scale(0.98);
  }
  &--primary {
    background: green;
  }
  &__icon {
    margin-right: 8px;
  }
}
```

### 2.2 隐式嵌套

不带 `&` 的嵌套会自动在前面添加父选择器：

```css
.card {
  .title {
    font-size: 1.5rem;
  }
  /* 等价于 .card .title */
}
```

### 2.3 嵌套 @规则

```css
.container {
  width: 100%;

  @media (min-width: 768px) {
    width: 750px;
  }
  @media (min-width: 1024px) {
    width: 960px;
  }
  @supports (backdrop-filter: blur(10px)) {
    backdrop-filter: blur(10px);
  }
}
```

## 3. 与预处理器嵌套的区别

| 特性       | CSS 原生嵌套           | Sass/Less      |
| ---------- | ---------------------- | -------------- |
| 运行时     | 浏览器原生             | 需编译         |
| & 用法     | 必须（隐式时自动添加） | 可选           |
| 嵌套深度   | 无限制                 | 无限制         |
| @规则嵌套  |                        |                |
| 浏览器支持 | 2023+                  | 全部（编译后） |

## 4. 最佳实践

- 嵌套深度不超过 3 层
- 优先使用 `&` 显式引用
- 善用 @规则嵌套简化媒体查询

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
