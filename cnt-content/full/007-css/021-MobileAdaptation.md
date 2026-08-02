---
order: 63
title: 移动端适配
module: css
category: CSS
difficulty: intermediate
description: rem、vw、vh、clamp
author: fanquanpp
updated: '2026-08-01'
related:
  - css/媒体查询
  - css/容器查询
  - css/函数
  - css/CSS变量与自定义属性
prerequisites:
  - css/概述与基本语法
---

## 1. 适配单位

| 单位   | 参照物         | 特点     |
| ------ | -------------- | -------- |
| `rem`  | 根元素字体大小 | 全局缩放 |
| `em`   | 父元素字体大小 | 局部缩放 |
| `vw`   | 视口宽度 1%    | 响应视口 |
| `vh`   | 视口高度 1%    | 响应视口 |
| `vmin` | 视口较小边 1%  | 适配短边 |

## 2. rem 适配

```css
html {
  font-size: 62.5%;
} /* 1rem = 10px */
body {
  font-size: 1.6rem;
} /* 16px */
```

## 3. vw 适配

```css
/* 设计稿 375px，元素 100px → 100/375*100 = 26.67vw */
.element {
  width: 26.67vw;
}
```

## 4. clamp() 函数

```css
h1 {
  font-size: clamp(1.5rem, 5vw, 3rem);
}
.container {
  width: clamp(300px, 80vw, 1200px);
}
```

$$
\text{font-size} = \text{clamp}(\text{min}, \text{preferred}, \text{max})
$$

## 5. 安全区域与1px边框

```css
.header {
  padding-top: env(safe-area-inset-top);
}
.border-1px::after {
  content: '';
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 1px;
  background: #ccc;
  transform: scaleY(0.5);
}
```

## 6. dvh 单位

```css
.full-screen {
  height: 100dvh;
} /* 动态视口高度，解决移动端 vh 问题 */
```

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
