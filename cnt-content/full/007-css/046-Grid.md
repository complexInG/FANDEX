---
order: 460
title: CSS Grid 布局速查
module: css

category: '007-css'
difficulty: beginner
description: CSS Grid 布局速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 容器属性

**基本写法：grid 容器**
`display: grid;`
```css
/* 设置网格容器 */
.container {
  display: grid;
}
```

---

**基本写法：inline-grid 行内网格**
`display: inline-grid;`
```css
/* 行内网格容器 */
.row {
  display: inline-grid;
}
```

---

**基本写法：定义列轨道**
`grid-template-columns: <值> [值 ...];`
```css
/* 定义三列等宽 */
.container {
  grid-template-columns: 1fr 1fr 1fr;
}
```

---

**基本写法：repeat 重复**
`grid-template-columns: repeat(<数量>, <值>);`
```css
/* 重复 3 列等宽 */
.container {
  grid-template-columns: repeat(3, 1fr);
}
```

---

**基本写法：auto-fill 自动填充**
`grid-template-columns: repeat(auto-fill, minmax(<最小>, 1fr));`
```css
/* 响应式自动填充列 */
.container {
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
}
```

---

**基本写法：auto-fit 自动适应**
`grid-template-columns: repeat(auto-fit, minmax(<最小>, 1fr));`
```css
/* 自动适应并拉伸填满 */
.container {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
```

---

**基本写法：定义行轨道**
`grid-template-rows: <值> [值 ...];`
```css
/* 定义行高度 */
.container {
  grid-template-rows: 100px auto 100px;
}
```

---

**基本写法：fr 单位**
`grid-template-columns: 1fr 2fr 1fr;`
```css
/* 按比例分配空间 */
.container {
  grid-template-columns: 1fr 2fr 1fr;
}
```

---

**基本写法：minmax 最小最大**
`grid-template-columns: minmax(<最小>, <最大>);`
```css
/* 列宽最小 200px 最大 1fr */
.container {
  grid-template-columns: minmax(200px, 1fr);
}
```

---

**基本写法：gap 间距**
`gap: <值>;`
```css
/* 网格间距 */
.container {
  gap: 20px;
}
```

---

**基本写法：gap 行列分开**
`row-gap: <值>; column-gap: <值>;`
```css
/* 分别设置行列间距 */
.container {
  row-gap: 20px;
  column-gap: 10px;
}
```

---

## 网格线与区域

**基本写法：命名网格线**
`grid-template-columns: [线名] <值> [线名];`
```css
/* 命名网格线 */
.container {
  grid-template-columns: [start] 1fr [middle] 1fr [end];
}
```

---

**基本写法：grid-template-areas 区域**
`grid-template-areas: "<区域定义>";`
```css
/* 命名网格区域 */
.container {
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
}
```

---

**基本写法：项目放置到区域**
`grid-area: <区域名>;`
```css
/* 将项目放入指定区域 */
.header {
  grid-area: header;
}
.main {
  grid-area: main;
}
```

---

**基本写法：基于线放置**
`grid-column: <起线> / <止线>;`
```css
/* 跨越指定网格线 */
.item {
  grid-column: 1 / 3;
  grid-row: 1 / 2;
}
```

---

**基本写法：span 跨越**
`grid-column: span <数量>;`
```css
/* 跨越指定列数 */
.item {
  grid-column: span 2;
}
```

---

**基本写法：grid-area 简写**
`grid-area: <行起> / <列起> / <行止> / <列止>;`
```css
/* 同时指定行列起止 */
.item {
  grid-area: 1 / 1 / 3 / 3;
}
```

---

## 对齐属性

**基本写法：justify-items 水平对齐**
`justify-items: start | end | center | stretch;`
```css
/* 网格项水平对齐 */
.container {
  justify-items: center;
}
```

---

**基本写法：align-items 垂直对齐**
`align-items: start | end | center | stretch;`
```css
/* 网格项垂直对齐 */
.container {
  align-items: center;
}
```

---

**基本写法：justify-content 整体水平**
`justify-content: start | end | center | space-between | space-around | space-evenly;`
```css
/* 整个网格水平对齐 */
.container {
  justify-content: space-between;
}
```

---

**基本写法：align-content 整体垂直**
`align-content: start | end | center | space-between | space-around;`
```css
/* 整个网格垂直对齐 */
.container {
  align-content: center;
}
```

---

**基本写法：place-items 简写**
`place-items: <align-items> <justify-items>;`
```css
/* 同时设置垂直水平对齐 */
.container {
  place-items: center;
}
```

---

## 自动布局

**基本写法：自动流方向**
`grid-auto-flow: row | column | dense;`
```css
/* 稠密填充避免空隙 */
.container {
  grid-auto-flow: dense;
}
```

---

**基本写法：行方向稠密**
`grid-auto-flow: row dense;`
```css
/* 行方向稠密排列 */
.container {
  grid-auto-flow: row dense;
}
```

---

**基本写法：自动轨道尺寸**
`grid-auto-rows: <值>; grid-auto-columns: <值>;`
```css
/* 自动生成行高 */
.container {
  grid-auto-rows: minmax(100px, auto);
}
```

---

## 常见布局模式

**基本写法：圣杯布局**
`display: grid; grid-template-areas: "...";`
```css
/* 经典三栏圣杯布局 */
.layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main aside"
    "footer footer footer";
  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}
```

---

**基本写法：响应式卡片网格**
`grid-template-columns: repeat(auto-fill, minmax(<最小>, 1fr));`
```css
/* 自适应卡片网格 */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}
```

---

**基本写法：12 列网格系统**
`grid-template-columns: repeat(12, 1fr);`
```css
/* 12 列栅格系统 */
.grid12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 20px;
}
.col-6 {
  grid-column: span 6;
}
.col-4 {
  grid-column: span 4;
}
```

---

## 现代 Grid 特性

**基本写法：subgrid 子网格**
`grid-template-columns: subgrid;`
```css
/* 子网格继承父网格轨道 */
.nested {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: 1 / -1;
}
```

---

**基本写法：容器查询单位**
`grid-template-columns: repeat(auto-fill, minmax(20cqi, 1fr));`
```css
/* 基于容器尺寸的列宽 */
.card {
  container-type: inline-size;
}
.card-inner {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(20cqi, 1fr));
}
```

---

**基本写法：aspect-ratio 控制比例**
`aspect-ratio: <宽> / <高>;`
```css
/* 网格项保持 16:9 比例 */
.video-item {
  aspect-ratio: 16 / 9;
}
```

---

**基本写法：masonry 瀑布流（实验性）**
`grid-template-rows: masonry;`
```css
/* CSS Grid 瀑布流布局（实验特性） */
.masonry {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: masonry;
}
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
