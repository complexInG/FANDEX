---
order: 100
title: 定位详解
module: 'css'
category: 前端技术
difficulty: intermediate
description: static、relative、absolute、fixed、sticky
author: fanquanpp
updated: '2026-08-02'
related:
  - 'css/008-StyleSheetImportMethod'
  - 'css/009-MarginCollapse'
  - 'css/011-FloatClear'
  - 'css/012-StackingContext'
prerequisites:
  - 'css/001-CSS3OverviewBasicSyntax'
---

## 0. 直觉：定位就是“以谁为参照系”

`position` 的五个值，本质是五个不同的参照系：

- `static`：默认，随文档流排列；
- `relative`：相对自己原来的位置偏移，原位保留；
- `absolute`：相对最近的定位祖先，脱离文档流；
- `fixed`：相对视口，滚动也不动；
- `sticky`：先随文档流，滚到阈值后“粘”住。

记不住没关系：遇到“这个元素应该钉在哪”的问题时，回到这张参照系表。

## 1. position 属性

| 值         | 定位类型 | 脱离文档流 | 参照物       |
| ---------- | -------- | ---------- | ------------ |
| `static`   | 默认     | 否         | —            |
| `relative` | 相对定位 | 否         | 自身原位置   |
| `absolute` | 绝对定位 | 是         | 最近定位祖先 |
| `fixed`    | 固定定位 | 是         | 视口         |
| `sticky`   | 粘性定位 | 否         | 滚动容器     |

**讲解：** “脱离文档流”意味着原位置不再占空间；`absolute`/`fixed` 脱离，`relative`/`sticky` 保留原位（sticky 在粘住前仍占位）。

## 2. relative

```css
.element {
  position: relative;
  top: 10px;
  left: 20px;
}
```

不脱离文档流，原位置保留。常作 absolute 的参照容器。

**讲解：** `relative` 用 `top`/`left` 相对“自己原本的位置”偏移，其它元素不受影响；给父元素加 `relative` 是为了给子 `absolute` 提供参照系。

## 3. absolute

```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

脱离文档流，参照最近定位祖先。

**讲解：** `absolute` 参照“最近的定位祖先”（`position` 非 static 的祖先）；示例用 `top: 50%` + `left: 50%` + `translate(-50%, -50%)` 实现居中——父元素必须 `relative`。

## 4. fixed

```css
.header {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 100;
}
```

参照视口，滚动时固定。注意 transform 会改变包含块。

**讲解：** `fixed` 相对视口定位，适合吸顶导航、悬浮按钮；注意祖先有 `transform`/`filter` 时，参照系会变成该祖先（形成新的包含块）。

## 5. sticky

```css
.sidebar {
  position: sticky;
  top: 20px;
}
th {
  position: sticky;
  top: 0;
  background: white;
  z-index: 1;
}
```

阈值前 relative，达到后 fixed。必须指定 top/bottom。

**讲解：** `sticky` 需要至少一个 `top`/`bottom`/`left`/`right` 阈值；父容器高度是它的活动范围，父容器设了 `overflow: hidden` 会失效；表格 `th` 吸顶是经典应用。

## 6. z-index

```css
:root {
  --z-dropdown: 100;
  --z-modal: 300;
  --z-toast: 400;
}
```

z-index 仅对定位元素生效；同一层叠上下文内比较；子元素无法超越父上下文。

**讲解：** 建议用 CSS 变量统一管理层级（如 `--z-modal: 300`），避免魔法数字；`z-index` 只在同一层叠上下文内比较，父上下文决定了子元素的“天花板”。

## 7. 进阶知识点

### 7.1 inset 简写

```css
.cover {
  position: absolute;
  inset: 0; /* 等价于 top/right/bottom/left: 0 */
}
```

**讲解：** `inset` 同时设置四个偏移属性，`inset: 0` 是“铺满定位祖先”的常用写法；也支持 `inset: 10px 20px` 等简写组合。

### 7.2 clip-path 裁剪

```css
.avatar {
  clip-path: circle(50%);
}
```

**讲解：** `clip-path` 用几何形状裁剪元素（圆形、多边形等），常用于头像、形状化按钮；旧 `clip` 属性只支持矩形，已废弃。

### 7.3 定位上下文

- `absolute` 的包含块是“最近的非 static 定位祖先”；
- `fixed` 默认包含块是视口，但祖先有 `transform`/`perspective`/`filter` 时会改变；
- 创建层叠上下文的条件：`position + z-index`、`transform`、`opacity < 1`、`filter`、`contain` 等。

## 8. 本章综合挑战（选做）

1. 用 `absolute + inset: 0` 做一个全屏遮罩层；
2. 用 `sticky` 做表格吸顶表头；
3. 用 `fixed` + CSS 变量做悬浮“回到顶部”按钮；
4. 验证 `transform` 祖先会改变 `fixed` 的参照系。

## 9. 核心知识点

> 一句话记住定位：`relative` 留原位，`absolute` 找祖先，`fixed` 看视口，`sticky` 会吸顶；`z-index` 只在同一层叠上下文内比大小。

- 五种定位值对应五种参照系：static/relative/absolute/fixed/sticky；
- `absolute`/`fixed` 脱离文档流，`relative`/`sticky` 保留原位；
- `absolute` 参照最近定位祖先，父元素记得加 `relative`；
- `fixed` 默认参照视口，`transform` 祖先会改变包含块；
- `sticky` 必须给阈值，父容器 `overflow: hidden` 会失效；
- `z-index` 建议用 CSS 变量管理，注意层叠上下文边界；
- `inset` 简写与 `clip-path` 是常用的现代补充。

## 10. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| `absolute` 找不到参照 | 相对页面跳动 | 父元素加 `position: relative` |
| 祖先有 transform | `fixed` 不再相对视口 | 调整结构或改用 `position: fixed` 的替代方案 |
| 父容器 `overflow: hidden` | sticky 失效 | 改用 `overflow: clip` |
| 大量魔法 z-index | 层级失控 | 用变量定义层级体系 |
| 用 margin 做悬浮 | 与滚动冲突 | 用 fixed/sticky + inset |

## 11. 扩展学习

- 定位基础：`css/004-TraditionalLayoutTech`；
- 层叠上下文：`css/012-StackingContext`；
- 变换：`css/047-Transform3D`（transform 与包含块）；
- 布局实战：`css/045-CSSProjectExampleResponsiveHomepage`。
