---
order: 68
title: 滚动捕捉
module: css
category: CSS
difficulty: intermediate
description: 'scroll-snap'
author: fanquanpp
updated: '2026-08-01'
related:
  - css/层叠层
  - css/逻辑属性
  - css/Sass预处理器
  - css/Less与Stylus
prerequisites:
  - css/概述与基本语法
---

## 1. scroll-snap 概述

CSS 滚动捕捉允许创建类似轮播图的滚动效果，滚动停止时自动对齐到指定位置。

## 2. 容器属性

```css
.scroll-container {
  scroll-snap-type: x mandatory; /* 方向 + 严格度 */
  overflow-x: auto;
}
```

### scroll-snap-type

| 方向   | 说明     |
| ------ | -------- |
| `x`    | 水平捕捉 |
| `y`    | 垂直捕捉 |
| `both` | 双向捕捉 |

| 严格度      | 说明               |
| ----------- | ------------------ |
| `mandatory` | 必须捕捉（强对齐） |
| `proximity` | 接近时捕捉（默认） |

## 3. 子元素属性

```css
.scroll-item {
  scroll-snap-align: start; /* 对齐方式 */
  scroll-snap-stop: always; /* 停止行为 */
}
```

### scroll-snap-align

| 值       | 说明         |
| -------- | ------------ |
| `start`  | 对齐容器起始 |
| `center` | 对齐容器中心 |
| `end`    | 对齐容器结束 |

### scroll-snap-stop

| 值       | 说明             |
| -------- | ---------------- |
| `normal` | 可以跳过（默认） |
| `always` | 必须停止         |

## 4. 实战：轮播图

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding: 0 20px;
}

.carousel-item {
  flex: 0 0 100%;
  scroll-snap-align: center;
}
```

## 5. 实战：全屏滚动

```css
.fullpage {
  height: 100vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
}

.fullpage-section {
  height: 100vh;
  scroll-snap-align: start;
}
```

## 6. scroll-margin 和 scroll-padding

```css
/* 捕捉偏移 */
.snap-item {
  scroll-margin: 80px;
} /* 元素偏移 */
.container {
  scroll-padding: 80px;
} /* 容器偏移 */
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
