---
order: 1
title: Tailwind CSS 概述
module: tailwind
category: Tailwind CSS
difficulty: beginner
description: 'Tailwind CSS 概述：工具类、设计令牌、响应式、暗色模式与 Tailwind 4 的 CSS-first 配置'
author: fanquanpp
updated: '2026-08-01'
related:
  - css/CSS概述
  - astro/Astro框架概述
  - react/React基础
prerequisites:
  - css/CSS概述
---
## 1. Tailwind CSS 是什么

Tailwind CSS 是一个“实用优先”（utility-first）的 CSS 框架：它不提供预设组件，而是提供大量原子工具类（如 `flex`、`p-4`、`text-lg`），开发者直接在 HTML/组件中组合出设计。

2023 年发布的 Tailwind 4 重写了引擎：CSS-first 配置（`@theme`）、原生层叠、自动内容检测、Vite 插件原生集成，构建速度与产物体积大幅优化。

## 2. 为什么需要工具类

传统“语义类”写法：

```css
.card {
  padding: 16px;
  border-radius: 8px;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
```

工具类写法：

```html
<div class="rounded-lg bg-white p-4 shadow-md">内容</div>
```

工具类的优势：

第一，无需命名：不用为每个样式块起类名；

第二，约束一致：间距、颜色、字号来自设计令牌，不会出现随意值；

第三，删除安全：组件删除时样式自动消失，没有死代码；

第四，响应式内联：`sm:`、`md:` 前缀直接写在类名上。

## 3. 核心语法

### 3.1 布局

```html
<div class="flex items-center justify-between gap-4">
  <span>左</span>
  <span>右</span>
</div>

<div class="grid grid-cols-3 gap-4">
  <div>1</div><div>2</div><div>3</div>
</div>
```

### 3.2 间距与尺寸

`p-4`（padding 16px）、`m-2`（margin 8px）、`w-1/2`、`h-screen`、`max-w-3xl`。数值基于间距刻度（0.25rem 基数）。

### 3.3 排版

`text-sm`、`font-bold`、`tracking-wide`、`leading-relaxed`、`text-center`。

### 3.4 颜色

`bg-red-500`、`text-blue-600`、`border-gray-200`。色板按色相-明度命名（50-950）。

## 4. 响应式与状态

### 4.1 响应式断点

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
  <!-- 移动端 1 列，md 2 列，lg 4 列 -->
</div>
```

断点前缀：`sm`（640）、`md`（768）、`lg`（1024）、`xl`（1280）、`2xl`（1536），移动优先语义。

### 4.2 状态变体

```html
<button class="bg-blue-500 hover:bg-blue-600 focus:outline-none active:bg-blue-700">
  按钮
</button>
```

常用变体：`hover:`、`focus:`、`active:`、`disabled:`、`group-hover:`、`peer-`。

### 4.3 暗色模式

```html
<div class="bg-white dark:bg-gray-900 dark:text-gray-100">
  自动适配系统暗色偏好
</div>
```

## 5. Tailwind 4 的 CSS-first 配置

```css
/* src/styles/global.css */
@import "tailwindcss";

/* 设计令牌：定义后自动生成 bg-primary、text-surface 等工具类 */
@theme {
  --color-primary: #1677ff;
  --color-surface: #ffffff;
  --color-text: #1f1f1f;
  --font-sans: "Inter", system-ui, sans-serif;
  --radius-card: 12px;
}
```

```html
<button class="bg-primary rounded-card px-4 py-2">主题按钮</button>
```

讲解：`@theme` 中定义的 `--color-primary` 生成 `bg-primary`、`text-primary`、`border-primary` 等全套工具类。主题切换只需覆盖变量。

## 6. 与框架集成

### 6.1 Vite + React

```bash
pnpm add tailwindcss @tailwindcss/vite
```

```ts
// vite.config.ts
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [tailwindcss()],
})
```

### 6.2 Astro

Astro 使用同一 Vite 插件，在布局中 `@import "tailwindcss"` 即可全局生效。

### 6.3 组件封装

配合 `class-variance-authority` 与 `clsx` 管理组件类名变体：

```tsx
import { cva } from 'class-variance-authority'

const button = cva('rounded-lg font-medium', {
  variants: {
    intent: {
      primary: 'bg-blue-500 text-white',
      ghost: 'bg-transparent text-blue-500',
    },
  },
})
```

## 7. 常见陷阱

陷阱一：动态拼接类名。`bg-${color}-500` 无法被内容扫描识别。写完整类名或使用 safelist。

陷阱二：滥用 `@apply`。把工具类塞回 CSS 层增加复杂度；适度用于组件库基础类。

陷阱三：自定义断点碎片化。优先使用预设断点。

陷阱四：忽略暗色配置。确认使用系统策略还是 class 策略。

陷阱五：内联样式与工具类混用。统一工具类，保持主题一致。

## 8. 参考资源

Tailwind 官方文档：https://tailwindcss.com/docs

Tailwind 中文文档：https://www.tailwindcss.cn/docs

Tailwind UI：https://tailwindui.com/

prettier-plugin-tailwindcss：https://github.com/tailwindlabs/prettier-plugin-tailwindcss

尚硅谷 Bilibili 空间：https://space.bilibili.com/302417610

## 9. 小结

Tailwind 用“约束下的原子类”平衡了效率与一致性：设计令牌保证风格统一，工具类保证开发速度，变体体系覆盖响应式与状态。Tailwind 4 的 CSS-first 配置进一步简化了集成，是 FANDEX Web 端样式方案的核心。

## 参考文献

Tailwind 官方文档：https://tailwindcss.com/docs
Tailwind 中文文档：https://www.tailwindcss.cn/docs
Tailwind UI 组件：https://tailwindui.com/
prettier-plugin-tailwindcss：https://github.com/tailwindlabs/prettier-plugin-tailwindcss

## 延伸阅读

CSS 基础与变量，见 007-css 模块。
Astro + Tailwind 集成，见 055-astro 模块。
设计系统与主题，见 007-css 模块相关文档。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Tailwind 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 Tailwind 4 的 CSS-first 配置

@theme 块定义令牌：--color-primary 生成 bg-primary 等工具类。
原生层叠：@layer 管理 theme/base/components/utilities 顺序。
自动检测：源码扫描无需配置文件；自定义来源用 @source。
与 Vite：@tailwindcss/vite 插件一步集成。

### 13.2 组件复用策略

方案一：纯工具类 + 组件封装（React 组件、Astro 组件）。
方案二：@apply 提取可复用类（注意 v4 语法变化）。
方案三：CSS 变量 + 工具类组合，动态主题。
选择依据：团队规模、设计系统成熟度、主题需求。
