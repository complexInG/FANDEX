---
order: 30
title: Svelte 5 响应式： runes 与绑定
module: 'svelte'
category: 前端技术
difficulty: intermediate
description: $state/$derived/$effect 的完整用法、bind 双向绑定与旧版 store 的对比。
author: fanquanpp
updated: '2026-08-03'
related:
  - 'svelte/001-SvelteOverview'
  - 'svelte/004-ComponentsTransitions'
prerequisites:
  - 'svelte/002-SvelteKitQuickStart'
---

## 0. 一句话理解

> runes 是 Svelte 5 的响应式语法糖：`$state` 存数据、`$derived` 算派生值、`$effect` 做副作用；`bind:` 让表单与状态自动同步。

## 1. $state 与 $derived

```svelte
<script>
  let price = $state(100)
  let qty = $state(2)

  let total = $derived(price * qty)

  function changePrice() {
    price = 120
  }
</script>

<p>单价：{price}，数量：{qty}，合计：{total}</p>
<button onclick={changePrice}>改为 120</button>
```

**讲解：**

1. `$state(100)` 创建响应式变量；直接赋值 `price = 120` 就会触发更新，不需要 `setState`。
2. `$derived(表达式)` 声明派生值：`total` 依赖 `price` 与 `qty`，任一变化时自动重算。
3. 派生值只读，不要手动赋值；它保证"显示值"永远与"源数据"一致。

## 2. $effect 副作用

```svelte
<script>
  let keyword = $state("")

  $effect(() => {
    console.log(`搜索关键词：${keyword}`)
  })
</script>

<input bind:value={keyword} placeholder="输入关键词" />
```

**讲解：**

1. `$effect(() => {...})` 在组件挂载后执行，并自动追踪函数内读取的响应式值；`keyword` 变化时重新执行。
2. 适用场景：日志、同步本地存储、调用非响应式 API；**不要**用它手动更新其他响应式变量（会循环）。
3. 函数内返回清理函数可做取消订阅等清理（类似 useEffect 的 cleanup）。

## 3. bind: 双向绑定

```svelte
<script>
  let name = $state("")
  let agree = $state(false)
  let color = $state("#00b894")
</script>

<input bind:value={name} placeholder="姓名" />
<input type="checkbox" bind:checked={agree} />
<input type="color" bind:value={color} />

<p>
  姓名：{name || "未填写"}，同意：{agree ? "是" : "否"}，
  颜色：{color}
</p>
```

**讲解：**

1. `bind:value` 让输入框的值与变量双向同步：输入即改变量，改变量即更新输入框。
2. 复选框用 `bind:checked`，颜色选择器用 `bind:value`，不同控件绑定不同属性。
3. 相比 React 的受控组件（value + onChange），Svelte 的 bind 写法更短，但原理相同。

## 4. 旧版 store 与新项目选择

```typescript
// stores/counter.ts（Svelte 4 写法，兼容保留）
import { writable } from "svelte/store"

export const count = writable(0)
```

```svelte
<!-- 旧版用法 -->
<script>
  import { count } from "$lib/stores/counter"
</script>

<p>{$count}</p>
```

**讲解：**

1. `writable(0)` 创建 store，`$count` 的 `$` 前缀是模板里的自动订阅语法。
2. 新项目优先用 runes（`$state`），跨组件共享状态时可以用 `$state` + 模块级导出，或继续用 store。
3. Svelte 5 完全兼容 store 语法，存量项目无需立刻迁移。

## 5. 动手试试

1. 做一个"单价 x 数量"计算器，含减号按钮且数量最小为 1（按钮用 `disabled={qty <= 1}`）。
2. 用 `$effect` 把 `name` 保存到 `localStorage`，组件加载时读回。
3. 用模块级 `$state` 做一个跨页面共享的购物车计数（`export const cartCount = $state(0)`）。

## 6. 一句话记住

> 响应式三件套：`$state` 存、`$derived` 算、`$effect` 监听；表单交互用 `bind:` 自动同步。
