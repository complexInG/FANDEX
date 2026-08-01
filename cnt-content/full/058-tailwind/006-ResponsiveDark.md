---
order: 6
title: Tailwind CSS 响应式与暗色模式
module: tailwind
category: Tailwind CSS
difficulty: intermediate
description: 'Tailwind CSS 响应式与暗色模式：断点、dark 变体与容器查询'
author: fanquanpp
updated: '2026-08-01'
related:
  - tailwind/004-LayoutFlexGrid
  - tailwind/005-ThemeCustomization
prerequisites:
  - tailwind/003-UtilityCore
---

## 1. 响应式断点体系

Tailwind 采用"移动优先"（mobile-first）策略：不加前缀的类默认作用于移动端，断点前缀只在"达到该宽度及以上"时生效。

| 前缀 | 最小宽度 | 典型设备 |
| --- | --- | --- |
| （无前缀） | 0 | 手机 |
| `sm:` | 640px | 大屏手机 / 小平板 |
| `md:` | 768px | 平板 |
| `lg:` | 1024px | 笔记本 |
| `xl:` | 1280px | 桌面显示器 |
| `2xl:` | 1536px | 大屏显示器 |

```html
<div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
  <div>卡片 1</div>
  <div>卡片 2</div>
  <div>卡片 3</div>
  <div>卡片 4</div>
</div>
```

讲解：手机端 1 列、平板 2 列、桌面 4 列。断点全部写在类名上，无需维护媒体查询文件。

断点也可以在 `@theme` 中自定义：

```css
@theme {
  /* 自定义断点：把默认 sm(640) 改为 560 */
  --breakpoint-sm: 560px;
  /* 新增断点：会生成 3xl: 前缀 */
  --breakpoint-3xl: 1920px;
}
```

讲解：`--breakpoint-*` 变量即断点定义，新增变量自动生成对应前缀，覆盖变量改变默认断点。

## 2. 任意断点 min-[...]

当预设断点不满足需求时，用任意值语法精确控制：

```html
<div class="grid grid-cols-1 min-[880px]:grid-cols-3">
  当视口宽度 ≥ 880px 时变为三列
</div>
```

讲解：`min-[880px]:` 生成 `@media (width >= 880px)`。任意断点适合"设计稿刚好在非标准宽度断列"的场景，但应控制数量，避免断点碎片化。

## 3. 暗色模式基础

v4 默认 `dark:` 变体跟随系统偏好（`prefers-color-scheme`）：

```html
<div class="bg-white text-gray-900 dark:bg-gray-900 dark:text-gray-100">
  亮色下白底黑字，暗色下黑底白字
</div>
```

讲解：无需任何配置，`dark:` 变体开箱即用。它是"仅当系统处于暗色偏好时生效"的条件样式。

与主题令牌配合的推荐写法：

```html
<div class="bg-surface text-text-main dark:bg-surface-dark dark:text-text-dark">
  语义令牌 + dark 变体，主题更可控
</div>
```

```css
@theme {
  --color-surface: #ffffff;
  --color-surface-dark: #141414;
  --color-text-main: #1f1f1f;
  --color-text-dark: #e5e5e5;
}
```

讲解：将亮/暗两套取值定义为显式令牌，`dark:` 变体负责切换，避免在组件里散落大量颜色值。

## 4. 类名策略与 @custom-variant

默认系统策略在"用户手动切换主题"的场景下不够用。v4 用 `@custom-variant` 把 `dark:` 改为 class 策略：

```css
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));
```

```html
<html class="dark">
  <body class="bg-white dark:bg-gray-900">内容</body>
</html>
```

讲解：`@custom-variant dark (...)` 重新定义了 `dark:` 变体的匹配条件：当祖先元素存在 `.dark` 类时生效。之后 JS 只需切换 `<html>` 上的 `dark` 类即可手动控制主题。

自定义切换逻辑：

```js
// theme-toggle.js
function toggleTheme() {
  document.documentElement.classList.toggle('dark')
}
```

讲解：配合 localStorage 持久化用户选择，即可实现完整的"跟随系统 + 手动覆盖"主题切换。

## 5. 容器查询（Container Queries）

媒体查询依赖视口宽度，容器查询（v4 内置）依赖"父容器的宽度"，组件在任意父容器中都能自适应。

### 5.1 声明容器

```html
<div class="@container">
  <div class="grid grid-cols-1 @md:grid-cols-2">
    <div>当父容器宽度达到 @md 断点时变为两列</div>
    <div>内容</div>
  </div>
</div>
```

讲解：父元素加 `@container` 声明为查询容器，子元素使用 `@md:`、`@lg:` 等前缀，判断依据是最近的容器宽度而非视口。

### 5.2 命名容器

```html
<div class="@container/card">
  <div class="@lg/card:flex @lg/card:flex-row">
    仅当名为 card 的容器达到 lg 宽度时生效
  </div>
</div>
```

讲解：`@container/card` 给容器命名，`@lg/card:` 前缀只响应指定容器，适合同一组件在页面多处不同尺寸容器中复用的场景。

### 5.3 容器查询与工具类容器

v4 还提供容器工具类用于约束内容宽度：

```html
<div class="container mx-auto px-6">
  <!-- v4 中 container 等价于 max-w-* 与 margin auto 组合 -->
</div>
```

讲解：v4 的 `container` 类由 CSS 变量驱动，默认居中并带 `max-width` 约束，也可在 `@theme` 中用 `--container-*` 调整宽度刻度。

## 6. 响应式与暗色的组合

变体可以任意叠加，先断点后状态：

```html
<button class="bg-blue-600 px-4 py-2 text-white rounded-md
               hover:bg-blue-700
               dark:bg-blue-500 dark:hover:bg-blue-400
               md:px-6">
  叠加变体的按钮
</button>
```

讲解：`dark:hover:` 表示"暗色模式下悬停"，`md:px-6` 表示"桌面端加大内边距"。变体从左到右依次是：暗色、状态、断点，组合顺序自由。

典型响应式导航示例：

```html
<nav class="flex items-center justify-between px-6 py-4 bg-white dark:bg-gray-900">
  <a href="/" class="font-bold dark:text-white">Logo</a>
  <ul class="hidden md:flex gap-6">
    <li><a class="dark:text-gray-300" href="/docs">文档</a></li>
    <li><a class="dark:text-gray-300" href="/blog">博客</a></li>
  </ul>
  <button class="md:hidden">菜单按钮（仅移动端显示）</button>
</nav>
```

讲解：`hidden md:flex` 让菜单在移动端隐藏、桌面端显示；`md:hidden` 让汉堡按钮反向控制，移动端可见、桌面端隐藏。这是响应式导航的标准模式。

## 7. 调试技巧

第一，浏览器响应式模式：在 DevTools 中切换视口宽度，逐档验证断点表现；

第二，检查生效的媒体查询：Elements 面板能看到 `dark:` 类对应 `@media (prefers-color-scheme: dark)` 或自定义条件；

第三，断点命名可读性：预设断点名称直观，优先使用；任意断点用注释标注用途。

## 参考资源

Tailwind 官方响应式文档：https://tailwindcss.com/docs/responsive-design

Tailwind 官方暗色模式文档：https://tailwindcss.com/docs/dark-mode

Tailwind 官方容器查询文档：https://tailwindcss.com/docs/container-queries

## 小结

响应式 = 移动优先断点 + 类名内联；暗色 = `dark:` 变体 + `@custom-variant` 控制策略；容器查询让组件摆脱视口依赖。三者组合可以覆盖绝大多数自适应与主题场景。下一篇讲解组件复用，把工具类沉淀为可维护的组件。
