---
order: 480
title: CSS @scope 规则语法速查手册
module: css

category: '007-css'
difficulty: beginner
description: CSS @scope 规则语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 基础语法

**基本写法：定义作用域**
`@scope (<根选择器>) { <规则集> }`
```css
/* 样式仅作用于 .card 子树内 */
@scope (.card) {
  p { color: gray; }
  img { border-radius: 8px; }
}
```

---

**基本写法：甜甜圈作用域（带上限）**
`@scope (<根>) to (<下限>) { <规则集> }`
```css
/* 上界 .article-body，下界 figure，中间区域生效 */
@scope (.article-body) to (figure) {
  img { border: 5px solid black; }
}
/* figure 内部的 img 不受影响，形成"甜甜圈洞" */
```

---

**基本写法：行内 @scope（省略前导）**
```html
<!-- <style> 内的 @scope 自动以父元素为根 -->
<parent-element>
  <style>
    @scope {
      p { color: red; }   <!-- 仅作用于 parent-element 内 -->
    }
  </style>
</parent-element>
```

---

## 多根作用域

**基本写法：多根选择器列表**
`@scope (<根1>, <根2>) { <规则集> }`
```css
/* 多个根共享同一组规则 */
@scope (.mike, .jane) {
  p { color: grey; }
}
```

---

**基本写法：多下限选择器**
`@scope (<根>) to (<下限1>, <下限2>) { <规则集> }`
```css
/* 多个下限同时排除 */
@scope (.article) to (.ad, .quote) {
  p { line-height: 1.6; }
}
```

---

## :scope 伪类

**基本写法：引用作用域根**
`:scope`
```css
/* :scope 指向 @scope 的根元素本身 */
@scope (.card) {
  :scope { padding: 16px; }       /* 等价 .card { padding: 16px; } */
  :scope > h2 { margin-top: 0; }  /* .card 的直接 h2 */
}
```

---

**基本写法：:scope 提升优先级**
```css
/* 普通选择器优先级 0-0-1，加 :scope 后为 0-1-1 */
@scope (.card) {
  img { /* 0-0-1 */ }
  :scope img { /* 0-1-1，优先级更高 */ }
}
```

---

## 作用域与嵌套

**基本写法：在 @scope 中嵌套**
```css
/* @scope 内可使用原生嵌套 */
@scope (.card) {
  & { padding: 16px; }
  & .title { font-weight: bold; }
  & :hover { background: #fafafa; }
}
```

---

**基本写法：@scope 嵌套到规则中**
```css
/* 在组件样式块内声明 @scope */
.card {
  color: black;
  @scope (&) to (& .legacy) {
    p { color: inherit; }
  }
}
```

---

## 级联与优先级

**基本写法：作用域邻近性**
```css
/* 当多个 @scope 都匹配时，DOM 距离更近的根胜出 */
/* 级联顺序：来源 > 重要性 > 层级 > 作用域邻近性 > 优先级 > 顺序 */
@scope (.outer) { h3 { color: red; } }
@scope (.inner) { h3 { color: blue; } }   /* 胜出（更近） */
```

---

**基本写法：与 @layer 组合**
```css
/* @scope 可置于层内 */
@layer components {
  @scope (.card) {
    .title { font-size: 1.2rem; }
  }
}
```

---

## 注意事项速查

**基本写法：选择器隔离而非样式隔离**
`@scope (<根>) { <规则> }`
```css
/* @scope 限制选择器匹配范围，但不阻止继承 */
@scope (.card) {
  p { color: red; }   /* 仅匹配 .card 内的 p */
}
/* 父元素继承的样式仍会作用到 .card 内 */
```

---

**基本写法：@scope 不影响自身之外的元素**
```css
/* 避免全局污染 */
p { color: black; }              /* 全局 */
@scope (.special) {
  p { color: red; }              /* 仅 .special 内 */
}
.special 外的 p 仍是黑色
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
