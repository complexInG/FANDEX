---
order: 10
title: Svelte 5 概述与快速上手
module: 'svelte'
category: 前端技术
difficulty: beginner
description: 零基础第一课：理解"编译时框架"与 runes 响应式，五分钟跑起第一个 Svelte 组件。
author: fanquanpp
updated: '2026-08-03'
related:
  - 'svelte/002-SvelteKitQuickStart'
  - 'svelte/003-ReactivityRunes'
  - 'javascript/001-JavaScriptOverviewRuntimeEnv'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
  - 'javascript/001-JavaScriptOverviewRuntimeEnv'
---

## 0. 五分钟创建第一个应用（先读这里）

> 学习目标：跑起 SvelteKit 项目，写一个带点击计数的组件，理解 `.svelte` 文件长什么样。

```bash
npx sv create my-app
cd my-app
npm run dev
```

**讲解：**

1. `sv create` 是 Svelte 官方 CLI，选择 SvelteKit（全栈框架）模板并回车确认即可。
2. `npm run dev` 启动开发服务器，默认 `http://localhost:5173`。
3. 打开 `src/routes/+page.svelte`，修改内容保存后浏览器热更新。

## 1. Svelte 是什么

Svelte 是一个"编译时框架"：React/Vue 在浏览器里用虚拟 DOM 做 diff，Svelte 则在构建时把组件编译成**直接操作 DOM 的原生 JavaScript**，所以运行时体积小、性能好。

Svelte 5（2024-10 发布）引入 **runes**（符文）语法：用 `$state`、`$derived`、`$effect` 显式声明响应式，替代旧版的 `let` 自动响应式与 `store` 体系。

### 1.1 版本现状（2026-08）

- Svelte 5.55.x 与 SvelteKit 2.57.x 为当前稳定版（2026-05）。
- 新项目统一使用 SvelteKit 脚手架；`+page.svelte` 文件即路由。

## 2. 第一个组件

```svelte
<!-- src/routes/+page.svelte -->
<script>
  let count = $state(0)

  function add() {
    count += 1
  }
</script>

<main>
  <h1>你好，Svelte 5</h1>
  <p>点击次数：{count}</p>
  <button onclick={add}>加一</button>
</main>
```

**讲解：**

1. `<script>` 里的 `$state(0)` 声明响应式变量：修改 `count` 时，所有用到它的 DOM 自动更新。
2. 模板里用 `{count}` 插值输出；`onclick={add}` 绑定事件，注意 Svelte 用属性名 `onclick`，不是 `onClick`。
3. 这个组件编译后没有虚拟 DOM——按钮点击直接更新那一个 `<p>` 的文本。

## 3. 与传统框架对比

| 维度 | React | Vue | Svelte 5 |
| --- | --- | --- | --- |
| 运行时 | 虚拟 DOM + fiber | 虚拟 DOM + 响应式代理 | 无虚拟 DOM，编译期优化 |
| 状态写法 | useState | ref/reactive | $state（runes） |
| 派生值 | useMemo | computed | $derived |
| 副作用 | useEffect | watchEffect | $effect |
| 学习曲线 | 中 | 中 | 低（模板接近 HTML） |

## 4. 动手试试

1. 给计数器加一个"减一"按钮，并把数字为 0 时按钮禁用。
2. 在 `src/routes/about/+page.svelte` 新建"关于"页面，用 `<a href="/about">` 跳转。
3. 把标题改成输入框：`<input bind:value={title} />`，观察输入时标题实时变化。

## 5. 一句话记住

> Svelte 在编译期把组件变成高效原生代码；Svelte 5 用 `$state/$derived/$effect` 三个符文管理响应式。
