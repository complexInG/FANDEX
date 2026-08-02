---
order: 20
title: CSS3 盒模型详解
module: 'css'
category: 前端技术
difficulty: intermediate
description: content/padding/border/margin、box-sizing 与视觉格式化。
author: Anonymous
updated: '2026-08-02'
related:
  - 'css/001-CSS3OverviewBasicSyntax'
  - 'css/003-CSS3SelectorSystem'
  - 'css/004-TraditionalLayoutTech'
prerequisites: []
---

## 0. 直觉：每个元素都是一个“礼物盒”

把每个 HTML 元素想象成一个礼物盒：

- `content` 是礼物本身（文字、图片）；
- `padding` 是盒子里的填充泡沫（内容与盒壁的距离）；
- `border` 是盒子的外壳；
- `margin` 是盒子与其它盒子之间的空隙。

浏览器在计算元素“占多大”时，这四个部分都要算进去。搞懂盒模型，才能解释“为什么宽度设了 200px 实际却占了 250px”这类问题。

## 1. 盒模型组成 (Components)

### 1.1 基本组成

每个 HTML 元素都被视为一个矩形盒子，由以下四个部分组成：
| 组成部分 | 描述 | 特性 |
|---------|------|------|
| **Content (内容)** | 实际的文本、图片等内容 | 由 `width` 和 `height` 属性控制大小 |
| **Padding (内边距)** | 内容与边框之间的透明区域 | 可以使用 `padding` 属性设置，会影响元素的实际大小 |
| **Border (边框)** | 围绕 Padding 和 Content 的线 | 由 `border` 属性控制，包括宽度、样式和颜色 |
| **Margin (外边距)** | 盒子与其他元素之间的间距 | 由 `margin` 属性控制，是透明的，不会影响元素自身大小 |

### 1.2 盒模型示意图

```mermaid
flowchart TD
    B0["Margin"]
    B1["Border"]
    B0 --> B1
    B2["Padding"]
    B1 --> B2
    B3["Content"]
    B2 --> B3
```

### 1.3 代码示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .box {
        width: 200px;
        height: 100px;
        padding: 20px;
        border: 5px solid #333;
        margin: 15px;
        background-color: #f0f0f0;
      }
    </style>
  </head>
  <body>
    <div class="box">内容区域</div>
  </body>
</html>
```

**讲解：**

- `content` 放内容，`padding` 撑开内容与边框的距离，`border` 是边框，`margin` 是元素外的间距；
- 标准盒模型（`content-box`）下，`width` 只算内容，实际占宽 = width + padding + border；
- 用开发者工具 Elements 面板可以直观看到四层结构。

## 2. 盒模型类型 (Box Sizing)

### 2.1 标准盒模型 (`content-box`)

**默认值**，遵循 W3C 标准。

- **宽度计算**: `width = 内容宽度`
- **实际占用空间**: `width + padding + border`
- **特点**: 当增加 `padding` 或 `border` 时，元素的实际宽度会增加
  **代码示例**:

```css
.standard-box {
  box-sizing: content-box;
  width: 200px;
  padding: 20px;
  border: 5px solid #333;
  /* 实际宽度: 200 + 20*2 + 5*2 = 250px */
}
```

**讲解：** `content-box` 是默认值：`width: 200px` 只约束内容区，加 `padding` 和 `border` 后实际占宽变成 250px。

### 2.2 怪异/IE 盒模型 (`border-box`)

**推荐使用**，更符合直觉的盒模型。

- **宽度计算**: `width = 内容宽度 + padding + border`
- **实际占用空间**: 等于设置的 `width`
- **特点**: 当增加 `padding` 或 `border` 时，元素的实际宽度不会改变，只会压缩内容区域
  **代码示例**:

```css
.border-box {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 5px solid #333;
  /* 实际宽度: 200px (内容宽度被压缩为 150px) */
}
```

**讲解：** `border-box` 让 `width` 包含内容、内边距与边框：设 200px 就占 200px，内容区自动压缩为 150px。现代项目几乎都全局使用 `border-box`。

### 2.3 全局盒模型设置

推荐在项目中全局使用 `border-box`，这样可以更方便地控制元素大小：

```css
 /* 方法 1: 全局设置 */
 * {
  box-sizing: border-box;
 }
 /* 方法 2: 更精确的设置，包括伪元素 */
 * {
  box-sizing: border-box;
 }
 /* 方法 3: 继承方式，更灵活 */
 html {
  box-sizing: border-box;
 }
 * {
  box-sizing: inherit;
}
```

**讲解：** 全局设置 `* { box-sizing: border-box; }` 让所有元素按直觉计算尺寸；加上 `::before`/`::after` 是因为伪元素也参与盒模型。

### 2.4 盒模型类型的应用场景

| 场景             | 推荐盒模型    | 原因                               |
| ---------------- | ------------- | ---------------------------------- |
| 响应式布局       | `border-box`  | 更容易计算元素尺寸，避免布局错位   |
| 固定宽度布局     | `border-box`  | 可以随意调整内边距而不影响整体布局 |
| 第三方组件集成   | `content-box` | 保持与原始组件一致的盒模型行为     |
| 精确控制内容区域 | `content-box` | 可以准确控制内容区域的大小         |

## 3. 外边距特性 (Margin Features)

### 3.1 外边距的基本用法

```css
/* 四个方向的外边距 */
margin: 10px; /* 四个方向都是 10px */
margin: 10px 20px; /* 上下 10px，左右 20px */
margin: 10px 20px 30px; /* 上 10px，左右 20px，下 30px */
margin: 10px 20px 30px 40px; /* 上 10px，右 20px，下 30px，左 40px */
/* 单个方向的外边距 */
margin-top: 10px;
margin-right: 20px;
margin-bottom: 30px;
margin-left: 40px;
```

### 3.2 水平居中

使用 `margin: 0 auto;` 可以实现块级元素的水平居中：

```css
.centered {
  width: 50%; /* 必须指定宽度 */
  margin: 0 auto; /* 上下外边距为 0，左右自动 */
}
```

**讲解：** `margin: 0 auto` 水平居中：左右外边距设为 `auto` 后浏览器自动平分剩余空间；前提是元素有明确宽度（或 max-width）。

**代码示例**:

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .container {
        width: 100%;
        background-color: #f0f0f0;
      }
      .centered-box {
        width: 50%;
        margin: 20px auto;
        padding: 20px;
        background-color: #fff;
        border: 1px solid #ddd;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="centered-box">这个盒子水平居中</div>
    </div>
  </body>
</html>
```

### 3.3 外边距塌陷 (Margin Collapse)

**定义**：在垂直方向上，相邻的两个外边距会取最大值，而非累加。

#### 3.3.1 常见的外边距塌陷场景

1. **相邻元素的外边距塌陷**

```html
<div style="margin-bottom: 30px;">元素 1</div>
<div style="margin-top: 20px;">元素 2</div>
<!-- 实际间距: 30px (取最大值)，而非 50px -->
```

**讲解：** 相邻兄弟的上下外边距不会相加，而是取较大值（30px）。这是外边距塌陷最常见的形态。

1. **父子元素的外边距塌陷**

```html
<div style="margin-top: 20px;">
  <div style="margin-top: 30px;">子元素</div>
</div>
<!-- 实际间距: 30px (取最大值)，而非 50px -->
```

**讲解：** 父元素与第一个子元素的外边距也会合并：子元素的 `margin-top` 会“穿透”到父元素外，取二者较大值。

1. **空元素的外边距塌陷**

```html
<div style="margin-top: 20px; margin-bottom: 30px;"></div>
<!-- 实际高度: 30px (取最大值)，而非 50px -->
```

**讲解：** 空元素自身的上下外边距也会合并：高度为 0 的元素，上下 margin 取最大值而不是相加。

#### 3.3.2 解决外边距塌陷的方法

| 方法           | 适用场景     | 代码示例                         |
| -------------- | ------------ | -------------------------------- |
| **添加边框**   | 父子元素塌陷 | `border: 1px solid transparent;` |
| **添加内边距** | 父子元素塌陷 | `padding: 1px;`                  |
| **使用 BFC**   | 各种塌陷场景 | `overflow: hidden;`              |
| **使用浮动**   | 相邻元素塌陷 | `float: left;`                   |
| **使用定位**   | 相邻元素塌陷 | `position: absolute;`            |

**代码示例**:

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .parent {
        background-color: #f0f0f0;
        /* 方法 1: 添加边框 */
        /* border: 1px solid transparent; */
        /* 方法 2: 添加内边距 */
        /* padding: 1px; */
        /* 方法 3: 使用 BFC */
        overflow: hidden;
      }
      .child {
        margin-top: 30px;
        padding: 20px;
        background-color: #fff;
      }
    </style>
  </head>
  <body>
    <div class="parent">
      <div class="child">子元素</div>
    </div>
  </body>
</html>
```

## 4. BFC (块级格式化上下文)

### 4.1 BFC 的定义

**块级格式化上下文** (Block Formatting Context) 是一个独立的渲染区域，内部元素的布局不会影响外部元素，外部元素也不会影响内部元素。

### 4.2 触发 BFC 的条件

| 条件                      | 代码示例                                                        |
| ------------------------- | --------------------------------------------------------------- |
| **浮动元素**              | `float: left;` 或 `float: right;`                               |
| **绝对定位元素**          | `position: absolute;` 或 `position: fixed;`                     |
| **行内块元素**            | `display: inline-block;`                                        |
| **表格单元格**            | `display: table-cell;`                                          |
| **弹性容器**              | `display: flex;` 或 `display: inline-flex;`                     |
| **网格容器**              | `display: grid;` 或 `display: inline-grid;`                     |
| **overflow 不为 visible** | `overflow: hidden;` 或 `overflow: auto;` 或 `overflow: scroll;` |
| **根元素**                | `<html>` 元素                                                   |

### 4.3 BFC 的作用

#### 4.3.1 清除浮动

当父元素包含浮动子元素时，父元素会塌陷，使用 BFC 可以解决这个问题：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .parent {
        background-color: #f0f0f0;
        /* 触发 BFC */
        overflow: hidden;
      }
      .child {
        float: left;
        width: 100px;
        height: 100px;
        margin: 10px;
        background-color: #fff;
      }
    </style>
  </head>
  <body>
    <div class="parent">
      <div class="child">子元素 1</div>
      <div class="child">子元素 2</div>
      <div class="child">子元素 3</div>
    </div>
  </body>
</html>
```

**讲解：** 让父元素形成 BFC（如 `overflow: hidden`），子元素的浮动就不会“撑破”父容器，高度塌陷问题随之解决。

#### 4.3.2 防止外边距重叠

使用 BFC 可以防止父子元素或相邻元素的外边距重叠：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .container {
        /* 触发 BFC */
        overflow: hidden;
      }
      .box {
        margin: 20px;
        padding: 20px;
        background-color: #f0f0f0;
      }
    </style>
  </head>
  <body>
    <div class="box">Box 1</div>
    <div class="container">
      <div class="box">Box 2 (在 BFC 中)</div>
    </div>
  </body>
</html>
```

**讲解：** 把其中一个兄弟元素放进独立的 BFC 容器（如 `display: flow-root`），它的外边距就不再与外部合并。

#### 4.3.3 实现两栏布局

使用 BFC 可以实现经典的两栏布局：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .container {
        width: 100%;
      }
      .sidebar {
        float: left;
        width: 200px;
        height: 300px;
        background-color: #f0f0f0;
      }
      .content {
        /* 触发 BFC */
        overflow: hidden;
        height: 300px;
        background-color: #e0e0e0;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="sidebar">侧边栏</div>
      <div class="content">主内容区</div>
    </div>
  </body>
</html>
```

**讲解：** 左侧定宽并浮动，右侧触发 BFC 后自动避开浮动元素，占据剩余空间——这是浮动时代经典的两栏布局。

## 5. 盒模型的实际应用

### 5.1 响应式布局中的盒模型

在响应式布局中，使用 `border-box` 可以更方便地控制元素大小：

```css
 /* 全局盒模型设置 */
 * {
  box-sizing: border-box;
 }
 /* 响应式网格 */
 .row {
  display: flex;
  flex-wrap: wrap;
  margin: 0 -15px;
 }
 .col {
  flex: 1;
  padding: 0 15px;
 }
 /* 媒体查询 */
 @media (max-width: 768px) {
  .col {
  flex: 0 0 100%;
  }
 }
```

### 5.2 卡片式布局

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      * {
        box-sizing: border-box;
      }
      .card {
        width: 300px;
        margin: 20px;
        border: 1px solid #ddd;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      }
      .card-header {
        padding: 15px;
        background-color: #f5f5f5;
        border-bottom: 1px solid #ddd;
      }
      .card-body {
        padding: 15px;
      }
      .card-footer {
        padding: 15px;
        background-color: #f5f5f5;
        border-top: 1px solid #ddd;
      }
    </style>
  </head>
  <body>
    <div class="card">
      <div class="card-header">卡片标题</div>
      <div class="card-body">卡片内容</div>
      <div class="card-footer">卡片底部</div>
    </div>
  </body>
</html>
```

### 5.3 表单元素的盒模型

```css
/* 表单元素的盒模型设置 */
input,
textarea,
select {
  box-sizing: border-box;
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
/* 按钮的盒模型设置 */
button {
  box-sizing: border-box;
  padding: 10px 20px;
  border: 1px solid #333;
  border-radius: 4px;
  background-color: #f0f0f0;
}
```

## 6. 盒模型的最佳实践

### 6.1 代码风格建议

- **统一盒模型**: 全局使用 `border-box` 以保持一致性
- **合理使用简写**: 优先使用 `margin` 和 `padding` 的简写形式
- **明确单位**: 统一使用 `px`、`em` 或 `rem` 等单位
- **避免负外边距**: 除非有特殊需求，否则避免使用负外边距
- **使用相对单位**: 在响应式布局中，使用相对单位如 `%`、`em` 或 `rem`

### 6.2 性能优化建议

- **减少不必要的嵌套**: 减少 DOM 元素的嵌套层级，避免过多的盒模型计算
- **合理使用 BFC**: 只在需要时触发 BFC，避免不必要的渲染开销
- **避免使用 `*` 选择器**: 尽量使用更具体的选择器，减少浏览器的计算负担
- **优化盒阴影**: 复杂的盒阴影会影响性能，使用时要适度

### 6.3 常见问题与解决方案

| 问题                 | 原因                        | 解决方案                               |
| -------------------- | --------------------------- | -------------------------------------- |
| **元素大小超出预期** | 使用了 `content-box` 盒模型 | 切换到 `border-box` 盒模型             |
| **布局错位**         | 外边距塌陷或浮动元素未清除  | 使用 BFC 清除浮动或防止外边距塌陷      |
| **响应式布局失效**   | 未正确设置盒模型            | 全局使用 `border-box` 并使用相对单位   |
| **表单元素对齐问题** | 表单元素的盒模型不一致      | 统一设置表单元素的盒模型和垂直对齐方式 |

## 7. 盒模型的高级技巧

### 7.1 计算盒模型的实际大小

使用 JavaScript 可以获取元素的实际盒模型大小：

```javascript
// 获取元素
const element = document.querySelector('.box');
// 获取计算后的样式
const computedStyle = window.getComputedStyle(element);
// 获取盒模型各部分的大小
const width = parseFloat(computedStyle.width);
const paddingLeft = parseFloat(computedStyle.paddingLeft);
const paddingRight = parseFloat(computedStyle.paddingRight);
const borderLeft = parseFloat(computedStyle.borderLeftWidth);
const borderRight = parseFloat(computedStyle.borderRightWidth);
// 计算实际宽度
const actualWidth = width + paddingLeft + paddingRight + borderLeft + borderRight;
console.log('实际宽度:', actualWidth);
```

### 7.2 使用 CSS 变量控制盒模型

```css
 :root {
  --box-padding: 20px;
  --box-border: 5px;
  --box-margin: 15px;
 }
 .box {
  padding: var(--box-padding);
  border: var(--box-border) solid #333;
  margin: var(--box-margin);
 }
 /* 响应式调整 */
 @media (max-width: 768px) {
  :root {
  --box-padding: 10px;
  --box-border: 3px;
  --box-margin: 10px;
  }
 }
```

### 7.3 盒模型与 Flexbox/Grid 的结合

盒模型与现代布局技术（如 Flexbox 和 Grid）结合使用，可以创建更灵活的布局：

```css
/* Flexbox 布局 */
.flex-container {
  display: flex;
  gap: 20px; /* 替代 margin */
}
.flex-item {
  flex: 1;
  padding: 20px;
  border: 1px solid #ddd;
}
/* Grid 布局 */
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px; /* 替代 margin */
}
.grid-item {
  padding: 20px;
  border: 1px solid #ddd;
}
```

## 8. 进阶知识点

### 8.1 outline 与 visibility

```css
.focus {
  outline: 2px solid #1677ff; /* 不占布局空间的外描边 */
}
.hidden {
  visibility: hidden; /* 隐藏但保留占位 */
}
```

**讲解：**

- `outline` 不参与盒模型，不改变布局，常用于焦点指示；
- `visibility: hidden` 隐藏内容但保留空间，`display: none` 完全移除；
- 二者与 `opacity: 0` 的区别：后者仍可交互，前者不可交互。

### 8.2 content 内容生成

```css
.card::before {
  content: "新";
  color: red;
}
```

**讲解：** `content` 配合伪元素生成装饰内容，不污染 HTML；`attr()` 可读取元素属性插入文本。

## 9. 动手试试

### 入门版（必做）

1. 写一个 200px 宽的盒子，加 `padding: 20px` 和 `border: 5px`，用开发者工具确认实际占宽是 250px；
2. 加上 `box-sizing: border-box` 再观察，确认实际占宽变为 200px；
3. 写两个上下相邻的块元素，分别设 30px/20px 外边距，确认实际间距是 30px。

### 进阶版（选做）

1. 用 `margin: 0 auto` 实现居中，再对比 Flexbox 居中；
2. 用 `overflow: hidden` 让父元素包住浮动的子元素；
3. 用 `display: flow-root` 解决父子外边距塌陷。

## 10. 核心知识点

> 一句话记住盒模型：`content` 是礼物，`padding` 是填充，`border` 是外壳，`margin` 是间距；`border-box` 让宽高按直觉计算。

- 盒模型四层：content → padding → border → margin；
- `content-box` 的 width 只算内容；`border-box` 的 width 包含 padding 和 border；
- 现代项目全局使用 `box-sizing: border-box`；
- 垂直外边距会塌陷（取最大值），水平不会；
- 解决方案：`overflow: hidden`、`display: flow-root`、padding/border 替代；
- BFC 可清除浮动、防止外边距合并、实现两栏布局。

## 11. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记全局 border-box | 宽度计算处处踩坑 | `* { box-sizing: border-box }` |
| 外边距相加的错觉 | 垂直间距比预期小 | 记住塌陷规则，用 padding 或 BFC 规避 |
| 用 margin 实现垂直居中 | 无效 | 用 Flexbox/Grid 或 absolute + transform |
| 误用 `outline: none` | 键盘焦点不可见 | 保留或替换为可见焦点样式 |
| 用 `display: none` 做动画 | 无法过渡 | 用 visibility/opacity 配合 |
| 内容溢出无处理 | 布局被撑破 | 检查 box-sizing 与 overflow |

## 12. 扩展学习

- 边距塌陷详解：`css/009-MarginCollapse`；
- 定位与层叠：`css/010-PositionDetailed`、`css/012-StackingContext`；
- 现代布局：`css/005-CSS3FlexboxFlexLayout`、`css/016-CSS3GridGridLayout`；
- 尺寸单位：`css/001-CSS3OverviewBasicSyntax` 中单位章节；
- 性能：避免大面积重排时的高频尺寸读写。
