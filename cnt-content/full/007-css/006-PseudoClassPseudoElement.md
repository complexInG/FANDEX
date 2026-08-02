---
order: 60
title: 伪类与伪元素
module: 'css'
category: 前端技术
difficulty: intermediate
description: :nth-child、:not、:is、::before、::after
author: fanquanpp
updated: '2026-08-01'
related:
  - 'css/004-TraditionalLayoutTech'
  - 'css/005-CSS3FlexboxFlexLayout'
  - 'css/007-PriorityCalculation'
  - 'css/008-StyleSheetImportMethod'
prerequisites:
  - 'css/001-CSS3OverviewBasicSyntax'
---

## 0. 直觉：伪类是“状态”，伪元素是“内容”

名字里带“伪”，是因为它们不真实存在于 HTML 里：

- 伪类（`:hover`、`:nth-child`）描述元素的**状态或位置**——鼠标悬停时、第几个孩子、被选中时；
- 伪元素（`::before`、`::after`）凭空**生成内容**——在元素前面或后面插入装饰。

记法：伪类单冒号（`:hover`），伪元素双冒号（`::before`）。这一节学完，你会掌握最常见的一批“选择器魔法”。
## 1. 伪类概述

伪类用于匹配元素的特定状态。

| 类别     | 示例                           | 说明     |
| -------- | ------------------------------ | -------- |
| 交互状态 | `:hover`, `:focus`, `:active`  | 用户交互 |
| 位置     | `:first-child`, `:nth-child()` | DOM 位置 |
| 输入状态 | `:checked`, `:disabled`        | 表单状态 |
| 否定     | `:not()`                       | 排除匹配 |
| 匹配     | `:is()`, `:where()`, `:has()`  | 复杂匹配 |

## 2. :nth-child()

```css
li:nth-child(3) {
  color: red;
} /* 第 3 个 */
tr:nth-child(odd) {
  background: #f0f0f0;
} /* 奇数 */
li:nth-child(3n + 1) {
  color: blue;
} /* 每 3 个选第 1 个 */
li:nth-child(-n + 3) {
  font-weight: bold;
} /* 前 3 个 */
```

**An+B 语法**：`2n+1` = odd，`2n` = even，`-n+3` = 前3个

**讲解：** `:nth-child(An+B)` 的括号里是“每隔 A 个选第 B 个”：`odd`/`even` 是奇数/偶数的简写，`-n+3` 表示“序号 ≤ 3”。注意它数的是所有兄弟元素，不只是同类型。

### nth-child vs nth-of-type

```html
<div>
  <h1>标题</h1>
  <!-- h1:first-of-type -->
  <p>段落1</p>
  <!-- p:nth-of-type(1) -->
  <p>段落2</p>
  <!-- p:nth-of-type(2) -->
</div>
```

**讲解：** `:nth-child` 按“所有兄弟中的位置”数，`:nth-of-type` 只数同类型兄弟。示例中三个孩子依次是 h1、p1、p2：`p:nth-of-type(1)` 选 p1，`p:nth-of-type(2)` 选 p2；`p:nth-child(2)` 也选中 p1（它是第 2 个孩子），但 `p:nth-child(1)` 选不中任何元素（第 1 个孩子是 h1）。

## 3. 否定与匹配伪类

```css
li:not(:last-child) {
  border-bottom: 1px solid #ccc;
}
:is(h1, h2, h3):hover {
  color: blue;
}
:where(h1, h2, h3) {
  margin: 0;
} /* 优先级为 0 */
a:has(> img) {
  border: none;
}
```

**讲解：** `:not()` 排除元素；`:is()` 合并选择器（优先级取最高者）；`:where()` 合并但优先级恒为 0；`:has()` 按“是否包含某结构”匹配父元素（如“含图片的链接”）。

## 4. 交互伪类

```css
a:hover {
  color: blue;
}
input:focus-visible {
  box-shadow: 0 0 0 3px rgba(0, 0, 255, 0.3);
}
input:focus-within {
  border-color: blue;
}
button:active {
  transform: scale(0.98);
}
```

**讲解：** `:hover` 鼠标悬停，`:focus-visible` 只对键盘焦点生效，`:focus-within` 匹配“自身或其内部有焦点”的元素，`:active` 是按下瞬间。

## 5. 伪元素

```css
.quote::before {
  content: '\201C';
  font-size: 2em;
}
.clearfix::after {
  content: '';
  display: table;
  clear: both;
}
p::first-line {
  font-weight: bold;
}
p::first-letter {
  font-size: 3em;
  float: left;
}
::selection {
  background: #ff6b6b;
  color: white;
}
input::placeholder {
  color: #999;
}
```

## 6. 进阶知识点

### 6.1 现代伪类（2024+）

```css
input:user-invalid {
  border-color: red;
}
button:has(+ .panel[open]) {
  background: #1677ff;
}
```

**讲解：**

- `:user-invalid` 只在用户真正交互过且值无效时触发，比 `:invalid` 更少打扰；
- `:has()` 让“父选择器”成为可能：`a:has(> img)` 匹配直接包含图片的链接；
- 现代浏览器均已支持，但复杂 `:has()` 会影响匹配性能，适度使用。

### 6.2 @scope 作用域

```css
@scope (.card) {
  h2 {
    font-size: 1.25rem;
  }
}
```

**讲解：** `@scope` 把规则限制在指定子树内，比手动写 `.card h2` 更清晰，还能用 `:scope` 精确控制边界。

### 6.3 计数器

```css
.doc { counter-reset: chapter; }
.doc h2::before {
  counter-increment: chapter;
  content: "第 " counter(chapter) " 章 ";
}
```

**讲解：** `counter-reset` 初始化计数器，`counter-increment` 递增，`counter()` 读出当前值；配合 `::before` 可自动生成章节编号。

## 7. 本章综合挑战（选做）

1. 用 `:nth-child(odd)` 给表格做隔行变色；
2. 用 `::before` 给必填项加红色星号；
3. 用 `:focus-visible` 给键盘焦点加可见描边；
4. 用 `:has()` 实现“含图片的卡片显示大图”；
5. 用计数器自动生成“第 1 节/第 2 节”标题编号。

## 8. 核心知识点

> 一句话记住伪类/伪元素：单冒号看状态（hover、nth-child），双冒号造内容（before、after）；`:not` 排除、`:is` 合并、`:has` 找父。

- 伪类匹配状态与位置：`:hover`、`:focus`、`:active`、`:nth-child`、`:checked`；
- 伪元素生成内容：`::before`/`::after` 必须有 `content`；
- `:nth-child(An+B)` 的语法：`odd`/`even`/`-n+3`；
- `:nth-of-type` 与 `:nth-child` 的区别是“同类型 vs 所有兄弟”；
- `:is()` 合并选择器，`:where()` 合并且优先级为 0，`:has()` 反向匹配父元素；
- 现代增强：`:user-invalid`、`:focus-visible`、`@scope`、计数器。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 伪元素忘记 `content` | 不显示 | 至少写 `content: ''` |
| `:nth-child` 与 `:nth-of-type` 混用 | 选中元素不符合预期 | 按“所有兄弟/同类型”区分 |
| 用 `:hover` 做移动端交互 | 触屏无悬停 | 用 `:focus`/媒体查询 |
| 大量 `:has()` 嵌套 | 匹配性能下降 | 简化选择器或改用类 |
| 移除 `:focus` 样式 | 键盘用户迷失 | 保留 `:focus-visible` 样式 |
| `:where` 优先级困惑 | 覆盖失败 | 记住它优先级为 0 |

## 10. 扩展学习

- 选择器总览：`css/003-CSS3SelectorSystem`；
- 优先级计算：`css/007-PriorityCalculation`；
- 表单状态：`css/019-MediaQuery` 之外的 `:user-invalid` 等交互增强；
- 嵌套与作用域：`css/049-CSSNesting`、`css/048-ScopeAtRule`；
- 伪元素布局：`css/045-CSSProjectExampleResponsiveHomepage` 中的实际应用。
