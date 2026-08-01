---
order: 6
title: Astro 岛屿架构与客户端指令
module: astro
category: Astro
difficulty: intermediate
description: 'Astro 岛屿架构：前端岛屿模型、client 指令、React/Vue/Svelte 框架集成与组件通信'
author: fanquanpp
updated: '2026-08-01'
related:
  - astro/004-ComponentsProps
  - astro/005-ContentCollections
prerequisites:
  - astro/004-ComponentsProps
---
## 1. 岛屿架构原理

传统 SPA 把整站打包成一个巨型 JavaScript 包，浏览器必须先下载并执行全部脚本才能看到内容。而对博客、文档站这类站点，绝大多数页面内容是静态文本，只有搜索框、主题切换、评论区等少量模块需要交互。

岛屿架构（Islands Architecture）的解法是：默认把页面渲染为纯静态 HTML（"海洋"），只对显式标记的交互组件（"岛屿"）注入客户端脚本。每个岛屿独立加载、独立水合（hydrate），互不影响。

| 对比项 | 传统 SPA | Astro 岛屿 |
| --- | --- | --- |
| 默认输出 | 空 HTML 骨架 + JS | 完整静态 HTML |
| JS 加载 | 全站一个 bundle | 按组件按需分片 |
| 首屏速度 | 依赖 JS 执行 | 无需 JS 即可展示 |
| 交互成本 | 全站水合 | 仅岛屿水合 |

## 2. client 指令：控制水合时机

框架组件（`.tsx`、`.vue`、`.svelte`）默认只做服务端渲染输出 HTML，不会在浏览器运行。必须加 `client:` 指令才"水合"：

```astro
---
// 使用 React 组件构建交互岛屿
import SearchBox from '../components/SearchBox.tsx'
import ThemeToggle from '../components/ThemeToggle.tsx'
import CommentForm from '../components/CommentForm.tsx'
---

<!-- 页面加载时立即水合：搜索框需尽快可用 -->
<SearchBox client:load />

<!-- 浏览器空闲时水合：主题切换不阻塞首屏 -->
<ThemeToggle client:idle />

<!-- 组件进入视口才水合：评论区在页面底部，用户未必会看到 -->
<CommentForm client:visible />
```

讲解：三个指令覆盖了最常见的需求，根据交互重要性选择水合时机，从源头控制 JS 成本。Astro 会为每个岛屿单独打包脚本，未加指令的组件零脚本成本。

### 2.1 指令速查表

| 指令 | 水合时机 | 适用场景 |
| --- | --- | --- |
| `client:load` | 页面加载后立即 | 首屏关键交互 |
| `client:idle` | 浏览器空闲时（requestIdleCallback） | 非关键但常用的交互 |
| `client:visible` | 元素进入视口时（IntersectionObserver） | 页面底部的组件 |
| `client:media="(max-width: 768px)"` | 匹配媒体查询时 | 仅移动端展示的组件 |
| `client:only="react"` | 仅在客户端渲染，跳过服务端渲染 | 依赖浏览器 API 的组件 |
| `client:focus` | 元素获得焦点时 | 低优先级的交互 |

讲解：`client:only` 场景特殊——某些组件只能在浏览器运行（如依赖 window 的库），需显式声明框架名。其余指令都不影响服务端渲染输出，只决定水合时机。

## 3. 框架集成：React / Vue / Svelte

### 3.1 安装集成

```bash
npx astro add react
npx astro add vue
npx astro add svelte
```

讲解：`astro add` 自动安装对应集成（`@astrojs/react` 等）、修改 `astro.config.mjs`、安装 JSX 相关依赖。一个项目可以同时集成多个框架，这是 Astro 的独特能力。

### 3.2 配置集成

```js
// astro.config.mjs
import { defineConfig } from 'astro/config'
import react from '@astrojs/react'
import vue from '@astrojs/vue'

export default defineConfig({
  integrations: [react(), vue()],
})
```

讲解：集成按数组顺序生效。注意 `@astrojs/react` 默认使用自动 JSX 运行时，无需额外配置；Vue 集成默认处理 SFC。

### 3.3 混合使用不同框架

```astro
---
// src/pages/index.astro
import ReactCounter from '../components/ReactCounter.tsx'
import VueModal from '../components/VueModal.vue'
import SvelteSlider from '../components/SvelteSlider.svelte'
---

<ReactCounter client:load />
<VueModal client:idle />
<SvelteSlider client:visible />
```

讲解：同一页面中 React、Vue、Svelte 组件共存互不干扰，每个都是独立的岛屿，由各自框架的运行时水合。这是岛屿架构区别于"选一个框架"思路的核心优势。

## 4. 框架组件之间的通信

### 4.1 通过 Props 传数据

```astro
---
import SearchBox from '../components/SearchBox.tsx'

const docs = await getCollection('docs')  // 构建期查询内容
---

<!-- 把静态数据作为 props 传入 React 组件 -->
<SearchBox client:load items={docs.map((d) => d.data.title)} />
```

讲解：构建期获取的数据可以作为 props 直接传给框架组件，props 会被序列化到 HTML 中（`data-astro-*` 属性或内联 JSON）。这是"静态数据 + 客户端交互"最常用的通信方式。

### 4.2 组件间共享状态：nanostores

跨岛屿、跨框架共享状态时，使用框架无关的存储库 nanostores（Astro 官方推荐）：

```ts
// src/stores/cart.ts
import { atom } from 'nanostores'

export const cartCount = atom(0)

export function addToCart() {
  cartCount.set(cartCount.get() + 1)
}
```

```tsx
// React 组件中使用
import { useStore } from '@nanostores/react'
import { cartCount } from '../stores/cart'

export default function CartBadge() {
  const count = useStore(cartCount)
  return <span>购物车：{count} 件</span>
}
```

讲解：nanostores 是轻量级全局状态库，Astro 官方集成保证其在客户端水合时状态可序列化、可恢复。React 用 `@nanostores/react` 的 `useStore` 订阅，Vue 用 `@nanostores/vue`，Svelte 原生 `$store` 语法直接支持。岛屿之间通过 store 通信，避免层层传参。

### 4.3 自定义事件与回调

单向数据流之外，可通过 props 传入回调函数（如 `onChange`），或用 `CustomEvent` 在岛屿间广播消息。回调函数会被序列化后由水合脚本绑定，适合父子组件交互。

## 5. 性能实践

第一，默认不加指令：能用静态 HTML 解决的交互（如原生 `<details>`、`:hover` 菜单）不要引入框架；

第二，从轻到重选择时机：`client:visible` 优先于 `client:idle` 优先于 `client:load`；

第三，关注构建报告：`astro build` 输出的每个页面 JS 体积明细，用于排查"意外水合"。

## 6. 参考资源

Astro 岛屿架构说明：https://docs.astro.build/zh-cn/concepts/islands/

客户端指令参考：https://docs.astro.build/zh-cn/reference/directives-reference/

框架集成指南：https://docs.astro.build/zh-cn/guides/framework-components/

nanostores 文档：https://github.com/nanostores/nanostores
