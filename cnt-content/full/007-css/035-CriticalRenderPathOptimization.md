---
order: 75
title: 关键渲染路径优化
module: css
category: CSS
difficulty: advanced
description: 关键CSS内联、异步加载
author: fanquanpp
updated: '2026-08-01'
related:
  - css/CSS原子化
  - css/CSS模块化
  - css/CSS原生嵌套
  - css/Canvas绘图
prerequisites:
  - css/概述与基本语法
---

## 1. 关键渲染路径

浏览器渲染流程：DOM → CSSOM → Render Tree → Layout → Paint → Composite

CSS 是渲染阻塞资源，必须优化加载策略。

## 2. 关键 CSS 内联

将首屏关键 CSS 内联到 `<head>` 中，消除渲染阻塞：

```html
<head>
  <style>
    /* 首屏关键 CSS */
    .hero {
      height: 100vh;
      background: #333;
      color: white;
    }
    .nav {
      position: fixed;
      top: 0;
      width: 100%;
    }
  </style>
</head>
```

## 3. 非关键 CSS 异步加载

```html
<!-- 方式1：preload + onload -->
<link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'" />

<!-- 方式2：media 切换 -->
<link rel="stylesheet" href="styles.css" media="print" onload="this.media='all'" />

<!-- 方式3：noscript 回退 -->
<noscript><link rel="stylesheet" href="styles.css" /></noscript>
```

## 4. CSS 性能优化清单

| 优化项           | 说明                     |
| ---------------- | ------------------------ |
| 关键 CSS 内联    | 首屏 CSS 内联到 `<head>` |
| 非关键 CSS 异步  | 延迟加载非首屏样式       |
| 压缩 CSS         | 移除空格、注释、冗余     |
| 减少选择器复杂度 | 避免深层嵌套             |
| 避免使用 @import | 串行加载影响性能         |
| 使用 contain     | 限制渲染范围             |
| 使用 will-change | 提示浏览器优化           |
| 减少重排重绘     | 批量 DOM 操作            |

## 5. CSS contain 属性

```css
.widget {
  contain: layout style paint;
  /* 或简写 */
  contain: strict; /* size layout style paint */
  contain: content; /* layout style paint */
}
```

## 6. 性能测量

```bash
# Lighthouse
npx lighthouse https://example.com --view

# Chrome DevTools
# Performance → 录制 → 分析渲染时间
# Coverage → 查看 CSS 使用率
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
