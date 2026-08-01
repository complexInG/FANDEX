# CSS Flexbox 布局速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 容器属性

**基本写法：flex 容器**
`display: flex;`
```css
/* 设置弹性容器 */
.container {
  display: flex;
}
```

---

**基本写法：inline-flex 行内容器**
`display: inline-flex;`
```css
/* 行内弹性容器 */
.badge {
  display: inline-flex;
}
```

---

**基本写法：主轴方向**
`flex-direction: row | row-reverse | column | column-reverse;`
```css
/* 主轴为水平方向 */
.row {
  flex-direction: row;
}
/* 主轴为垂直方向 */
.col {
  flex-direction: column;
}
```

---

**基本写法：是否换行**
`flex-wrap: nowrap | wrap | wrap-reverse;`
```css
/* 子元素自动换行 */
.container {
  flex-wrap: wrap;
}
```

---

**基本写法：flex-flow 简写**
`flex-flow: <方向> <换行>;`
```css
/* 同时设置方向和换行 */
.container {
  flex-flow: row wrap;
}
```

---

**基本写法：主轴对齐**
`justify-content: flex-start | center | flex-end | space-between | space-around | space-evenly;`
```css
/* 主轴均匀分布间距相同 */
.container {
  justify-content: space-evenly;
}
```

---

**基本写法：交叉轴对齐**
`align-items: flex-start | center | flex-end | stretch | baseline;`
```css
/* 交叉轴居中对齐 */
.container {
  align-items: center;
}
```

---

**基本写法：多行交叉轴对齐**
`align-content: flex-start | center | flex-end | space-between | space-around | stretch;`
```css
/* 多行时交叉轴两端对齐 */
.container {
  flex-wrap: wrap;
  align-content: space-between;
}
```

---

**基本写法：gap 间距**
`gap: <值>;`
```css
/* 子元素间距 */
.container {
  display: flex;
  gap: 20px;
}
```

---

**基本写法：gap 行列双值**
`gap: <行间距> <列间距>;`
```css
/* 分别设置行列间距 */
.grid {
  gap: 20px 10px;
}
```

---

## 子元素属性

**基本写法：flex-grow 放大比例**
`flex-grow: <数值>;`
```css
/* 子元素放大比例 */
.item {
  flex-grow: 1;
}
```

---

**基本写法：flex-shrink 缩小比例**
`flex-shrink: <数值>;`
```css
/* 不缩小 */
.item {
  flex-shrink: 0;
}
```

---

**基本写法：flex-basis 基础尺寸**
`flex-basis: <长度> | <百分比> | content;`
```css
/* 基础尺寸由内容决定 */
.tag {
  flex-basis: content;
}
```

---

**基本写法：flex 简写**
`flex: <grow> <shrink> <basis>;`
```css
/* 同时设置三个属性 */
.item {
  flex: 1 1 0%;
}
```

---

**基本写法：flex 关键字**
`flex: auto | none | 1;`
```css
/* 等价于 flex: 1 1 auto */
.item-auto {
  flex: auto;
}
/* 等价于 flex: 0 0 auto */
.item-none {
  flex: none;
}
```

---

**基本写法：order 排序**
`order: <数值>;`
```css
/* 设置子元素排序（默认 0） */
.item {
  order: -1;
}
```

---

**基本写法：align-self 单独对齐**
`align-self: auto | flex-start | center | flex-end | stretch;`
```css
/* 单独设置交叉轴对齐 */
.item {
  align-self: center;
}
```

---

## 常见布局模式

**基本写法：水平垂直居中**
`display: flex; justify-content: center; align-items: center;`
```css
/* Flex 居中方案 */
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

---

**基本写法：两栏布局**
`display: flex;`
```css
/* 左侧固定右侧自适应 */
.layout {
  display: flex;
}
.sidebar {
  width: 250px;
  flex-shrink: 0;
}
.main {
  flex-grow: 1;
}
```

---

**基本写法：三栏布局**
`display: flex;`
```css
/* 两侧固定中间自适应 */
.layout {
  display: flex;
}
.left, .right {
  width: 200px;
  flex-shrink: 0;
}
.center {
  flex-grow: 1;
}
```

---

**基本写法：等宽分布**
`display: flex;`
```css
/* 子元素等宽分布 */
.equal {
  display: flex;
}
.equal > * {
  flex: 1;
}
```

---

**基本写法：底部固定布局**
`display: flex; flex-direction: column; min-height: 100vh;`
```css
/* 页脚固定在底部 */
.page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.content {
  flex: 1;
}
```

---

**基本写法：卡片自适应网格**
`display: flex; flex-wrap: wrap; gap: <值>;`
```css
/* 自适应卡片网格 */
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.card {
  flex: 1 1 300px;
}
```

---

## 响应式 Flex

**基本写法：媒体查询切换方向**
`@media (max-width: <值>) { flex-direction: column; }`
```css
/* 小屏幕切换为列方向 */
.container {
  display: flex;
  flex-direction: row;
}
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}
```

---

**基本写法：原生嵌套媒体查询**
`.container { display: flex; @media (max-width: <值>) { flex-direction: column; } }`
```css
/* CSS 原生嵌套写法 */
.container {
  display: flex;
  @media (max-width: 768px) {
    flex-direction: column;
  }
}
```

---

**基本写法：响应式间距**
`gap: clamp(<最小>, <理想>, <最大>);`
```css
/* 流式响应间距 */
.grid {
  display: flex;
  gap: clamp(10px, 2vw, 30px);
}
```

---

## Flexbox 新特性

**基本写法：单行 align-content 生效**
`align-content: <值>;`
```css
/* 现代浏览器单行也支持 align-content */
.flex {
  display: flex;
  align-content: center;
  min-height: 200px;
}
```

---

**基本写法：place-content 简写**
`place-content: <align-content> <justify-content>;`
```css
/* 同时设置两个对齐属性 */
.container {
  display: flex;
  flex-wrap: wrap;
  place-content: center space-between;
}
```

---

**基本写法：place-items 简写**
`place-items: <align-items> <justify-items>;`
```css
/* 同时设置 items 对齐 */
.container {
  display: flex;
  place-items: center;
}
```
