---
order: 330
title: CSS原子化
module: 'css'
category: 前端技术
difficulty: intermediate
description: Tailwind CSS、UnoCSS
author: fanquanpp
updated: '2026-08-01'
related:
  - 'css/031-PostCSS'
  - 'css/032-BEMNamingMethodology'
  - 'css/035-CriticalRenderPathOptimization'
prerequisites:
  - 'css/001-CSS3OverviewBasicSyntax'
---


## 1. CSS 原子化概述

原子化 CSS（Atomic CSS）将每个样式属性拆分为独立的工具类，按需组合。

## 2. Tailwind CSS

### 2.1 基本用法

```html
<div class="flex items-center justify-between p-4 bg-white rounded-lg shadow-md">
  <h1 class="text-xl font-bold text-gray-900">标题</h1>
  <button class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">操作</button>
</div>
```

### 2.2 响应式前缀

```html
<div class="w-full md:w-1/2 lg:w-1/3">响应式宽度</div>
```

### 2.3 状态变体

```html
<button class="bg-blue-500 hover:bg-blue-600 focus:ring-2 active:bg-blue-700">按钮</button>
```

### 2.4 自定义配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: { primary: '#3498db' },
      spacing: { 18: '4.5rem' },
    },
  },
  plugins: [],
};
```

### 2.5 @apply 指令

```css
.btn-primary {
  @apply px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600;
}
```

## 3. UnoCSS

### 3.1 特点

- 更快的编译速度
- 高度可定制的预设系统
- 按需生成，零冗余

```javascript
// uno.config.ts
import { defineConfig, presetUno, presetAttributify } from 'unocss';

export default defineConfig({
  presets: [presetUno(), presetAttributify()],
  rules: [['text-primary', { color: '#3498db' }]],
  shortcuts: {
    btn: 'px-4 py-2 rounded cursor-pointer',
    'btn-primary': 'btn bg-blue-500 text-white hover:bg-blue-600',
  },
});
```

## 4. 对比

| 特性     | Tailwind CSS | UnoCSS |
| -------- | ------------ | ------ |
| 性能     | 快           | 更快   |
| 定制性   | 高           | 更高   |
| 生态     | 最大         | 增长中 |
| 学习曲线 | 中等         | 中等   |

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
