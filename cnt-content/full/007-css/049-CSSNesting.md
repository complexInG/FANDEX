---
order: 490
title: CSS 原生嵌套语法速查手册
module: 'css'
category: 前端技术
difficulty: beginner
description: CSS 原生嵌套语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## 基础嵌套

**基本写法：子代选择器嵌套**
```css
/* 子选择器直接写在父规则内 */
.card {
  background: white;

  .title {
    font-weight: bold;
  }

  .body {
    padding: 15px;
  }
}
/* 等价于 .card { } .card .title { } .card .body { } */
```

---

**基本写法：& 嵌套选择器**
`&`
```css
/* & 代表父选择器，用于复合或附加 */
.button {
  background: blue;
  &:hover { background: darkblue; }       /* .button:hover */
  &.primary { border-color: navy; }       /* .button.primary */
  & > span { font-weight: bold; }         /* .button > span */
}
```

---

**基本写法：& 用于伪类伪元素**
```css
.link {
  color: blue;
  &:hover { color: darkblue; }
  &:focus-visible { outline: 2px solid; }
  &::before { content: "›"; }
}
```

---

## 嵌套使用场景

**基本写法：组合选择器**
`&<复合>`
```css
/* 父子复合（无空格） */
.card {
  &.active { border-color: green; }
  &[disabled] { opacity: 0.5; }
  &:nth-child(2n) { background: #f5f5f5; }
}
```

---

**基本写法：后代选择器（不带 &）**
```css
/* 不带 & 时自动加空格，作用于后代 */
.navbar {
  .brand { font-weight: bold; }
  .links { margin-left: auto; }
  .links .link { padding: 0 15px; }
}
```

---

**基本写法：& 后置反转上下文**
`<选择器> &`
```css
/* 把 & 放后面，反转父子关系 */
.card {
  .dark-theme & {
    background: #333;
    color: #eee;
  }
}
/* 等价 .dark-theme .card { } */
```

---

**基本写法：多次使用 &**
```css
/* & 可在嵌套选择器中多次出现 */
.button {
  & + & { margin-left: 8px; }      /* 相邻兄弟 button */
  & ~ & { opacity: 0.8; }
}
```

---

## 嵌套 at 规则

**基本写法：嵌套 @media**
```css
/* 媒体查询直接写在组件规则内 */
.navbar {
  display: flex;

  @media (max-width: 768px) {
    display: block;
    .links { display: none; }
  }

  @media (prefers-color-scheme: dark) {
    background: #222;
  }
}
```

---

**基本写法：嵌套 @supports / @container**
```css
.card {
  @supports (backdrop-filter: blur(10px)) {
    backdrop-filter: blur(10px);
  }

  @container (min-width: 400px) {
    flex-direction: row;
  }
}
```

---

## 混合声明与规则

**基本写法：声明与嵌套混合**
```css
/* 属性声明与嵌套规则可同时存在 */
.card {
  background: white;        /* 属性 */
  border-radius: 8px;

  .title { font-weight: bold; }   /* 嵌套规则 */
  &:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
}
```

---

## 注意事项速查

**基本写法：HTML 元素需用 & 前缀（旧浏览器兼容）**
```css
/* 标签选择器嵌套建议加 &，兼容 Safari 17.2 之前 */
.box {
  & h2 { color: red; }    /* 推荐：所有浏览器支持 */
  /* h2 { color: red; } */ /* Safari 17.1 及之前可能无效 */
}

/* class / id 嵌套无需 & */
.box {
  .title { color: red; }  /* 兼容性好 */
}
```

---

**基本写法：避免过度嵌套**
```css
/* 不推荐：嵌套过深 */
.card {
  .body {
    .content {
      .item {
        .title { color: red; }   /* 4 层，难以覆盖 */
      }
    }
  }
}

/* 推荐：保持 2-3 层，配合 BEM 或扁平选择器 */
.card .item .title { color: red; }
```

---

**基本写法：& 不能代表伪元素**
```css
/* & 类似 :is()，不能表示 ::before/::after */
.parent {
  &::before { content: ""; }      /* 正确：直接写伪元素 */
  /* .child &::before 会被忽略，因 :is() 不支持伪元素 */
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
