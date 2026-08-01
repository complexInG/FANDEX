---
order: 4
title: Tailwind CSS 布局系统
module: tailwind
category: Tailwind CSS
difficulty: beginner
description: 'Tailwind CSS 布局系统：flex、grid、间距体系、容器与定位'
author: fanquanpp
updated: '2026-08-01'
related:
  - tailwind/003-UtilityCore
  - tailwind/006-ResponsiveDark
prerequisites:
  - tailwind/003-UtilityCore
---

## 1. display 显示模式

`display` 决定元素在文档流中的表现，Tailwind 提供一一对应的工具类：

| 类名 | 属性值 | 用途 |
| --- | --- | --- |
| `block` | display: block | 块级，占满整行 |
| `inline` | display: inline | 行内，随文本流动 |
| `inline-block` | display: inline-block | 行内但可设宽高 |
| `flex` | display: flex | 弹性布局 |
| `grid` | display: grid | 网格布局 |
| `hidden` | display: none | 隐藏元素 |

```html
<span class="block">这个 span 变成块级，独占一行</span>
<span class="inline-block w-24 bg-gray-100">行内块，可设宽度</span>
<div class="hidden md:block">移动端隐藏，桌面端显示</div>
```

讲解：`hidden` 配合响应式前缀是控制"移动端隐藏/桌面端显示"的常用手段，无需写媒体查询。

## 2. Flex 弹性布局

Flex 是横向/纵向排列的首选，核心是"主轴方向 + 对齐方式"两个维度。

### 2.1 主轴与对齐

```html
<div class="flex items-center justify-between gap-4">
  <div class="bg-blue-100 p-3">项目一</div>
  <div class="bg-blue-100 p-3">项目二</div>
  <button class="bg-blue-600 text-white px-4 py-2 rounded">操作</button>
</div>
```

讲解：`justify-between` 让项目沿主轴两端对齐，`items-center` 让项目在交叉轴居中，`gap-4` 保证间距。

常用组合速查：

| 类名 | 效果 |
| --- | --- |
| `justify-center` | 主轴居中 |
| `justify-between` | 两端对齐 |
| `justify-end` | 主轴末尾 |
| `items-center` | 交叉轴居中 |
| `items-start` / `items-end` | 交叉轴顶部 / 底部 |
| `flex-wrap` | 允许换行 |

### 2.2 方向与伸缩

```html
<div class="flex flex-col md:flex-row">
  <div class="flex-1">占满剩余空间</div>
  <div class="flex-1">等分宽度</div>
  <div class="w-24 shrink-0">固定宽度不收缩</div>
</div>
```

讲解：`flex-col` 切换为纵向；`flex-1` 让子项均分剩余空间；`shrink-0` 禁止收缩，常用于固定宽度的图标/头像。

## 3. Grid 网格布局

Grid 适合二维布局：同时控制行与列。

### 3.1 列数与间距

```html
<div class="grid grid-cols-3 gap-4">
  <div>1</div><div>2</div><div>3</div>
  <div>4</div><div>5</div><div>6</div>
</div>
```

讲解：`grid-cols-3` 生成三列等宽网格，`gap-4` 设置行列间距，子元素自动按行填充。

### 3.2 跨列与跨行

```html
<div class="grid grid-cols-4 gap-4">
  <div class="col-span-2 bg-gray-100 p-4">占两列</div>
  <div class="col-span-2 bg-gray-100 p-4">占两列</div>
  <div class="col-span-4 bg-gray-200 p-4">占满整行</div>
</div>
```

讲解：`col-span-2` 让元素跨越两列，`col-span-4` 在四列网格中即占满整行，常用于"通栏横幅"。

### 3.3 常见布局模板

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
  <aside class="md:col-span-1">侧边栏</aside>
  <main class="md:col-span-2">主内容区</main>
</div>
```

讲解：移动端一列，桌面端变成"侧边栏 + 主内容"双区布局，响应式变化只需改动 `grid-cols-*` 与 `col-span-*`。

## 4. 间距体系

间距是布局的"呼吸感"来源。Tailwind 使用统一刻度，`4` = 1rem = 16px，数字与像素的换算规律为"数字 × 4px"。

| 类名 | 像素 | 常见用途 |
| --- | --- | --- |
| `p-1` / `gap-1` | 4px | 紧凑图标间距 |
| `p-2` | 8px | 小控件内边距 |
| `p-4` | 16px | 常规卡片内边距 |
| `p-6` | 24px | 大卡片、区块内边距 |
| `p-8` | 32px | 页面大区块留白 |

```html
<div class="p-6">
  <section class="mb-6 rounded-lg bg-gray-50 p-4">
    <h2 class="mb-2 text-lg font-semibold">区块标题</h2>
    <p class="leading-relaxed">正文内容</p>
  </section>
</div>
```

讲解：统一使用刻度值，页面间距视觉上和谐统一；不要混用 `p-4` 和 `p-[17px]` 这类任意值。

## 5. 容器与居中

`max-w-*` 控制内容最大宽度，配合 `mx-auto` 实现经典居中：

```html
<main class="mx-auto max-w-7xl px-6">
  <p>内容在 1280px 以内水平居中，两侧保留 24px 内边距</p>
</main>
```

讲解：`max-w-7xl`（1280px）是页面级内容区的常见宽度。v4 中旧式 `container` 类已改为使用 `@utility` 定义，推荐直接用 `max-w-*` + `mx-auto` 组合，更直观可控。

文字居中与排版居中：

```html
<div class="text-center">
  <h1 class="text-2xl font-bold">居中标题</h1>
</div>
<div class="mx-auto w-1/2">块级元素水平居中</div>
```

讲解：`text-center` 让文字居中；让块级元素本身居中必须用 `mx-auto` 并指定宽度。

## 6. 定位 Position

定位用于悬浮元素、吸顶导航、浮层等场景。

| 类名 | 属性值 | 说明 |
| --- | --- | --- |
| `static` | position: static | 默认 |
| `relative` | position: relative | 相对自身原位，作为子元素定位基准 |
| `absolute` | position: absolute | 相对最近的 relative 祖先定位 |
| `fixed` | position: fixed | 相对视口定位，不随滚动 |
| `sticky` | position: sticky | 滚动到阈值后吸顶 |

```html
<div class="relative inline-block">
  <img src="avatar.png" class="w-16 h-16 rounded-full" alt="头像" />
  <span class="absolute -top-1 -right-1 flex h-5 w-5 items-center justify-center rounded-full bg-red-500 text-xs text-white">3</span>
</div>
<nav class="sticky top-0 z-50 bg-white/80 backdrop-blur">
  吸顶导航栏
</nav>
```

讲解：父元素加 `relative`，徽标用 `absolute` 定位到右上角（`-top-1 -right-1`）；`sticky top-0` 让导航滚动后固定在视口顶部；`z-50` 控制堆叠层级。

层级与透明度的配合：

```html
<div class="fixed inset-0 z-40 bg-black/50">遮罩层，覆盖整个视口</div>
```

讲解：`inset-0` 等价于 `top-0 right-0 bottom-0 left-0`，把元素拉伸到父容器全尺寸，是模态框遮罩的标准写法。

## 7. 综合示例：卡片布局

```html
<section class="grid grid-cols-1 md:grid-cols-3 gap-6 p-6">
  <article class="flex flex-col rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
    <h3 class="text-lg font-semibold">基础版</h3>
    <p class="mt-2 flex-1 text-sm text-gray-500">功能说明文字，flex-1 让按钮始终贴底</p>
    <button class="mt-4 rounded-lg bg-gray-900 px-4 py-2 text-sm text-white">选择</button>
  </article>
</section>
```

讲解：这个示例综合运用 grid（卡片排列）、flex（卡片内部纵向布局）、`flex-1`（说明文字撑开剩余空间，按钮贴底）三类能力，是实际项目中最常见的卡片模式。

## 参考资源

Tailwind 官方文档（Layout）：https://tailwindcss.com/docs/display

MDN Flex 布局：https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Flexbox

MDN Grid 布局：https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Grids

## 小结

布局系统的核心思路：一维排列用 flex，二维排列用 grid，间距统一走刻度体系，居中用 `mx-auto`，悬浮元素用定位三件套（`relative` + `absolute` + `z-*`）。下一篇进入主题定制，让样式有自己的设计令牌。
