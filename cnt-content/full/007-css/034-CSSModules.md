---
order: 74
title: 'CSS-Modules'
module: css
category: CSS
difficulty: intermediate
description: 'CSS Modules'
author: fanquanpp
updated: '2026-08-01'
related:
  - css/BEM命名方法论
  - css/CSS原子化
  - css/关键渲染路径优化
  - css/CSS原生嵌套
prerequisites:
  - css/概述与基本语法
---

## 1. CSS Modules 概述

CSS Modules 自动为每个类名生成唯一哈希，实现样式隔离，避免命名冲突。

```css
/* Button.module.css */
.btn {
  padding: 8px 16px;
  border-radius: 4px;
}
.primary {
  background: blue;
  color: white;
}
```

```javascript
import styles from './Button.module.css';

function Button() {
  return <button className={`${styles.btn} ${styles.primary}`}>Click</button>;
}
// 渲染为：<button class="Button_btn_x9y8z Button_primary_a1b2c">Click</button>
```

## 2. 命名约定

```css
/* 推荐：camelCase */
.primaryButton {
}

/* 也可以：kebab-case */
.primary-button {
}
```

```javascript
// camelCase 引用
styles.primaryButton;

// kebab-case 引用
styles['primary-button'];
```

## 3. 组合（composes）

```css
.base {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
}

.primary {
  composes: base;
  background: blue;
  color: white;
}
```

## 4. 与框架集成

### React

```javascript
import styles from './Component.module.css';
<div className={styles.container}></div>;
```

### Vue

```html
<style module>
  .container {
    padding: 1rem;
  }
</style>

<template>
  <div :class="$style.container"></div>
</template>
```

## 5. TypeScript 支持

```typescript
// declare module '*.module.css' {
//   const classes: { readonly [key: string]: string };
//   export default classes;
// }
```

## 6. 对比其他方案

| 方案        | 隔离方式   | 运行时 | 优点     |
| ----------- | ---------- | ------ | -------- |
| CSS Modules | 哈希类名   |        | 零运行时 |
| CSS-in-JS   | 运行时生成 |        | 动态样式 |
| Shadow DOM  | DOM 隔离   |        | 完全隔离 |
| BEM         | 命名约定   |        | 简单     |

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
