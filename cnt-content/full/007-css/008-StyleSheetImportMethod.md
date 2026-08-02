---
order: 80
title: 样式表引入方式
module: 'css'
category: 前端技术
difficulty: beginner
description: 内联、嵌入、外部、导入
author: fanquanpp
updated: '2026-08-01'
related:
  - 'css/006-PseudoClassPseudoElement'
  - 'css/007-PriorityCalculation'
  - 'css/009-MarginCollapse'
  - 'css/010-PositionDetailed'
prerequisites:
  - 'css/001-CSS3OverviewBasicSyntax'
---


## 1. 四种引入方式

### 内联样式

```html
<p style="color: red;">内联样式</p>
```

优先级最高、无法复用、不推荐。

### 嵌入样式

```html
<style>
  p {
    color: blue;
  }
</style>
```

仅当前页面有效、无法缓存。

### 外部样式表

```html
<link rel="stylesheet" href="styles.css" />
```

可复用、可缓存、**推荐方式**。

### @import 导入

```css
@import url('reset.css');
```

串行加载（性能差）、避免在顶层使用。

## 2. 对比

| 方式    | 复用性 | 缓存 | 性能 | 推荐度     |
| ------- | ------ | ---- | ---- | ---------- |
| 内联    |        |      | 差   | 低         |
| 嵌入    |        |      | 中   | 中       |
| 外部    |        |      | 好   | 极高 |
| @import |        |      | 差   | 中       |

## 3. 关键 CSS 内联

```html
<head>
  <style>
    .hero {
      height: 100vh;
    }
  </style>
  <link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'" />
</head>
```
