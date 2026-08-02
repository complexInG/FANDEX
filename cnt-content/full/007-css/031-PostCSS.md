---
order: 71
title: PostCSS
module: css
category: CSS
difficulty: intermediate
description: PostCSS（autoprefixer、cssnano）
author: fanquanpp
updated: '2026-08-01'
related:
  - css/Less与Stylus
  - css/响应式设计
  - css/BEM命名方法论
  - css/CSS原子化
prerequisites:
  - css/概述与基本语法
---

## 1. PostCSS 概述

PostCSS 是一个用 JavaScript 插件转换 CSS 的工具，本身不提供任何功能，通过插件实现。

```javascript
// postcss.config.js
module.exports = {
  plugins: [require('autoprefixer'), require('cssnano')({ preset: 'default' })],
};
```

## 2. 常用插件

### 2.1 autoprefixer

自动添加浏览器前缀：

```css
/* 输入 */
.container {
  display: flex;
}

/* 输出 */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}
```

```json
// package.json → browserslist
"browserslist": ["last 2 versions", "> 1%", "not dead"]
```

### 2.2 cssnano

CSS 压缩优化：

```css
/* 输入 */
.container {
  margin: 0px;
  color: #ff0000;
}

/* 输出 */
.container {
  margin: 0;
  color: red;
}
```

### 2.3 postcss-preset-env

使用未来 CSS 特性：

```css
/* 输入 */
@custom-media --md (min-width: 768px);
@media (--md) {
  .container {
    width: 750px;
  }
}

/* 输出 */
@media (min-width: 768px) {
  .container {
    width: 750px;
  }
}
```

### 2.4 postcss-nesting

CSS 原生嵌套：

```css
.card {
  padding: 1rem;
  & .title {
    font-size: 1.5rem;
  }
  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
}
```

## 3. 与构建工具集成

```bash
# Vite
npm install -D postcss autoprefixer

# Webpack
npm install -D postcss-loader autoprefixer
```

## 4. 自定义插件

```javascript
module.exports = (opts = {}) => {
  return {
    postcssPlugin: 'postcss-my-plugin',
    Declaration(decl) {
      if (decl.prop === 'color' && decl.value === 'primary') {
        decl.value = opts.primary || '#3498db';
      }
    },
  };
};
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
