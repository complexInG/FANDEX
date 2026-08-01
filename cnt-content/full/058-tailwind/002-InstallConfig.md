---
order: 2
title: Tailwind CSS 安装与配置
module: tailwind
category: Tailwind CSS
difficulty: beginner
description: 'Tailwind CSS 安装与配置：Vite 集成、@import 与 @source'
author: fanquanpp
updated: '2026-08-01'
related:
  - tailwind/003-UtilityCore
  - css/003-CSS3SelectorSystem
prerequisites:
  - css/003-CSS3SelectorSystem
---

## 1. 安装方式概览

Tailwind CSS v4 提供了多种接入方式，核心差异在于"谁来编译"。v4 使用 Rust 编写的 Oxide 引擎，编译速度相比 v3 提升数倍，安装与配置也随之简化。

| 方式 | 适用场景 | 复杂度 |
| --- | --- | --- |
| Vite 插件 `@tailwindcss/vite` | Vite 项目（React/Vue/Svelte/Astro） | 最低，官方推荐 |
| PostCSS 插件 `@tailwindcss/postcss` | 依赖 PostCSS 生态的构建链 | 中 |
| CLI 工具 `@tailwindcss/cli` | 无打包器的纯 HTML 项目 | 低 |

无论哪种方式，入口都只有一行 CSS：`@import "tailwindcss";`。它一次性引入 Preflight 基础样式、主题变量与全部工具类，取代了 v3 的 `@tailwind base/components/utilities` 三行指令。

## 2. Vite 插件方式（推荐）

### 2.1 安装依赖

```bash
pnpm add tailwindcss @tailwindcss/vite
```

讲解：`tailwindcss` 是核心包，`@tailwindcss/vite` 是 Vite 专用插件。使用 npm 或 yarn 安装亦可，命令等价。

### 2.2 注册插件

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [tailwindcss()],
})
```

讲解：在 `plugins` 数组中注册 `tailwindcss()` 即可，无需任何配置对象。Vite 热更新时，Tailwind 类名变化即时生效。

### 2.3 引入入口 CSS

```css
/* src/styles/global.css */
@import "tailwindcss";
```

```ts
// src/main.ts
import './styles/global.css'
```

讲解：在应用入口引入 global.css，Tailwind 会在构建时把它编译为最终 CSS。全局只需引入一次。

## 3. PostCSS 方式

PostCSS 方式适合使用 webpack 等非 Vite 构建工具，或项目已重度依赖 PostCSS 插件链的场景。

```bash
pnpm add tailwindcss @tailwindcss/postcss
```

```js
// postcss.config.mjs
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

讲解：配置文件采用标准的 PostCSS 插件声明方式。注意插件名是 `@tailwindcss/postcss`，与 v3 的 `tailwindcss` 插件名不同，避免写错。

## 4. CLI 方式

纯 HTML 项目没有打包器，可以用官方 CLI 独立编译 CSS。

```bash
pnpm add -D @tailwindcss/cli
npx @tailwindcss/cli -i ./src/input.css -o ./dist/output.css --watch
```

讲解：`-i` 指定输入 CSS（含 `@import "tailwindcss"`），`-o` 指定输出文件，`--watch` 开启监听模式，源码变更后自动重新编译。

## 5. @source 源文件扫描

v4 不再需要 `tailwind.config.js` 中的 `content` 数组，而是自动扫描项目内的模板文件。自动检测的扫描范围通常是"入口 CSS 所在目录的父目录"之外的公共源码根（如 `src`）。

当类名出现在自动扫描范围之外的目录时，用 `@source` 指令手动声明：

```css
@import "tailwindcss";
@source "../components";
@source "../node_modules/@my-lib/ui";
```

讲解：每个 `@source` 指向一个需要扫描的目录或文件。适用于 monorepo、单独放置的组件目录、以及第三方组件库中需要被识别类名的文件。

扫描遵循以下约定：

第一，自动忽略 `.gitignore` 中忽略的文件与二进制文件；

第二，`@source` 支持 glob 通配符，如 `@source "../views/**/*.html"`；

第三，类名必须是完整的字符串，动态拼接的类名无法被扫描到。

## 6. 与主流框架集成

### 6.1 React / Vue / Svelte

三者都通过 Vite 插件接入，步骤完全一致：注册插件、引入 CSS。组件模板中直接写类名：

```tsx
// Button.tsx
export function Button({ children }: { children: React.ReactNode }) {
  return (
    <button className="rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">
      {children}
    </button>
  )
}
```

讲解：框架层无需任何额外配置，Tailwind 类名与 JSX/Vue 模板天然兼容。

### 6.2 Astro

Astro 底层使用 Vite，因此接入方式相同。在 `astro.config.mjs` 中注册插件，并在布局组件中引入 CSS：

```js
// astro.config.mjs
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  vite: { plugins: [tailwindcss()] },
})
```

### 6.3 Next.js（webpack 构建链）

Next.js App Router 项目使用 PostCSS 方式，v4 无需再配置 `content` 数组：

```js
// postcss.config.mjs
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

在全局样式文件（如 `app/globals.css`）中写入 `@import "tailwindcss";` 即可。

## 7. 安装后的自检清单

安装完成后，用以下三点快速验证环境是否正确：

第一，页面出现 Preflight 重置效果（如标题默认字号被重置），说明基础层生效；

第二，输入任意工具类（如 `flex`）后样式即时出现，说明扫描正常；

第三，检查生成的 CSS 体积：v4 生产构建会做 tree-shaking，只保留实际使用到的工具类。

## 参考资源

Tailwind 官方安装文档：https://tailwindcss.com/docs/installation

Tailwind 中文安装文档：https://www.tailwindcss.cn/docs/installation

Vite 插件源码：https://github.com/tailwindlabs/tailwindcss/tree/main/packages/%40tailwindcss-vite

## 小结

v4 的安装配置大幅简化：一行 `@import "tailwindcss"` 引入全部功能，Vite 插件零配置接入，`@source` 精确控制扫描范围。下一篇将介绍核心概念与常用工具类的使用。
