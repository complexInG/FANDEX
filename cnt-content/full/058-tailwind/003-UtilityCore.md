---
order: 3
title: Tailwind CSS 核心概念与工具类
module: tailwind
category: Tailwind CSS
difficulty: beginner
description: 'Tailwind CSS 核心概念：utility-first 理念、常用工具类、状态变体与任意值'
author: fanquanpp
updated: '2026-08-01'
related:
  - tailwind/002-InstallConfig
  - tailwind/004-LayoutFlexGrid
prerequisites:
  - tailwind/002-InstallConfig
---

## 1. utility-first 理念

传统 CSS 开发是先给元素起语义类名（`.card`、`.nav-item`），再在样式表里写规则。这带来两个问题：命名成本高、样式难以复用。

Tailwind 的 utility-first 反其道而行：每个工具类只负责一个 CSS 属性，开发者直接在 HTML 中组合它们。

```html
<!-- 传统写法 -->
<div class="card">卡片内容</div>

<!-- Tailwind 写法 -->
<div class="rounded-lg bg-white p-4 shadow-md">卡片内容</div>
```

讲解：`rounded-lg` 管圆角，`bg-white` 管背景，`p-4` 管内边距，`shadow-md` 管阴影。样式与结构同处一个文件，改样式不必来回切换文件。

utility-first 的收益：

第一，无命名负担，不需要为每个模块起类名；

第二，样式受设计令牌约束，间距、颜色、字号不会出现随意值；

第三，删除组件即删除样式，没有死代码。

## 2. 常用工具类

### 2.1 间距与尺寸

间距体系基于 0.25rem（4px）的刻度，数字越大间距越大。

| 类名 | 值 | 说明 |
| --- | --- | --- |
| `p-4` | 1rem | 四边内边距 |
| `px-2` | 0.5rem | 左右内边距 |
| `py-3` | 0.75rem | 上下内边距 |
| `m-auto` | auto | 外边距自动居中 |
| `gap-4` | 1rem | 子元素间距 |

```html
<div class="m-auto w-64 space-y-4 rounded-lg border p-6">
  <p class="text-sm">上边距来自 space-y-4</p>
  <p class="text-sm">下一条间距相同</p>
</div>
```

讲解：`space-y-4` 为所有相邻子元素之间添加垂直间距，比逐个加 margin 更省心。

### 2.2 排版

```html
<h1 class="text-3xl font-bold tracking-tight leading-tight">标题</h1>
<p class="text-base text-gray-600 leading-relaxed">正文段落，行高更宽松，阅读更舒适。</p>
<p class="text-sm text-gray-400">辅助说明文字</p>
```

讲解：`text-3xl` 控制字号，`font-bold` 控制字重，`tracking-tight` 控制字距，`leading-relaxed` 控制行高。字号与行高都来自预设刻度。

### 2.3 颜色

颜色按"色相-明度"两级命名，明度从 50（最浅）到 950（最深）：

```html
<button class="bg-blue-600 text-white hover:bg-blue-700">主按钮</button>
<button class="bg-emerald-50 text-emerald-700 border border-emerald-200">次按钮</button>
<p class="text-red-500">错误提示</p>
```

讲解：`bg-*` 管背景，`text-*` 管文字颜色，`border-*` 管边框颜色。v4 默认调色板全面升级为 OKLCH 色彩空间，颜色更鲜艳、色阶更均匀。

### 2.4 布局

```html
<div class="flex items-center justify-between">
  <span>左侧</span>
  <button class="rounded px-3 py-1 bg-gray-900 text-white">右侧按钮</button>
</div>
```

讲解：`flex` 开启弹性布局，`items-center` 垂直居中，`justify-between` 两端对齐。详细布局能力见下一篇文档。

## 3. 状态变体

变体（variant）是 Tailwind 的灵魂：在工具类前加前缀，样式只在特定状态生效。

```html
<button class="bg-blue-600 px-4 py-2 text-white rounded-md
               hover:bg-blue-700 focus:ring-2 focus:ring-blue-300
               active:bg-blue-800 disabled:opacity-50">
  提交
</button>
```

讲解：`hover:` 鼠标悬停时变深色，`focus:` 聚焦时显示外圈光晕，`active:` 按下时更暗，`disabled:` 禁用时半透明。

常用状态变体：

| 变体 | 触发时机 |
| --- | --- |
| `hover:` | 鼠标悬停 |
| `focus:` | 键盘/点击聚焦 |
| `focus-visible:` | 仅键盘聚焦（推荐用于可访问性） |
| `active:` | 元素被按下 |
| `disabled:` | 元素禁用 |
| `first:` / `last:` | 第一个 / 最后一个子元素 |
| `group-hover:` | 祖先含 `group` 类时悬停 |

```html
<!-- group-hover 示例：悬停整张卡片时标题变色 -->
<div class="group rounded-lg border p-4 hover:border-gray-300">
  <h3 class="text-lg group-hover:text-blue-600">悬停我</h3>
  <p class="text-sm text-gray-500">卡片描述</p>
</div>
```

讲解：在父元素加 `group` 类，子元素用 `group-hover:` 就能响应父元素的悬停状态，实现"整卡联动"效果。

## 4. 任意值写法

当预设刻度不满足需求时，用方括号语法直接写任意值：

```html
<div class="w-[320px] bg-[#f8fafc] p-[13px]">
  精确到像素的宽度与内边距
</div>
<p class="text-[clamp(1rem,2vw,1.5rem)]">响应式字号</p>
<div class="grid grid-cols-[1fr_2fr]">自定义网格列</div>
```

讲解：方括号内可以是长度、颜色、甚至完整的 CSS 函数。注意类名中不能有空格，用下划线 `_` 代替（如 `1fr_2fr`）。

任意值的适用原则：偶尔的例外值用任意值；频繁出现的值应提升为设计令牌（`@theme`），保证一致性。

## 5. @utility 自定义工具类

`@utility` 是 v4 提供的指令，用于把重复使用的复杂样式封装成自己的工具类，且能与变体（`hover:`、`dark:` 等）配合使用。

```css
/* src/styles/global.css */
@import "tailwindcss";

@utility text-balance {
  text-wrap: balance;
  text-overflow: ellipsis;
}

@utility card-base {
  border-radius: 0.75rem;
  border: 1px solid var(--color-gray-200);
  box-shadow: var(--shadow-sm);
}
```

```html
<h2 class="text-balance">自动平衡断行的标题</h2>
<div class="card-base hover:shadow-md">可组合变体的自定义工具类</div>
```

讲解：`@utility` 中可以直接引用主题变量（如 `var(--color-gray-200)`）。定义后 `hover:card-base`、`dark:card-base` 等变体组合全部可用，这是它相对普通 CSS 类名的核心优势。

## 6. 与普通 CSS 类名配合

项目中仍会有自己写的 CSS 类，二者可以共存：

```html
<div class="flex items-center gap-2 自定义类"></div>
```

讲解：自定类负责"一次性、业务专属"的样式，工具类负责通用布局。建议优先级：工具类为主，自定义类为辅，避免同一样式双写。

## 7. 常见误区

误区一：把所有样式都写成任意值。任意值绕过了设计令牌，滥用会导致风格失控。

误区二：记忆所有类名。不需要背，编辑器中输入任意前缀即出现补全提示。

误区三：在 `@apply` 中无节制复用。适度使用，详见组件复用篇。

## 参考资源

Tailwind 官方文档（工具类索引）：https://tailwindcss.com/docs/utility-first

Tailwind 中文文档：https://www.tailwindcss.cn/docs

CSS 变量基础：https://developer.mozilla.org/zh-CN/docs/Web/CSS/Using_CSS_custom_properties

## 小结

utility-first 通过原子化工具类把"命名"和"复用"问题交给框架解决。掌握间距、排版、颜色三类高频工具类与状态变体，即可完成大部分页面样式。自定义需求用任意值应急、用 `@utility` 沉淀。
