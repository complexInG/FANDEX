## 0. 一句话理解

> 父子通信两条路：属性（$props）从父到子，回调函数从子到父；过渡动画是 Svelte 的杀手锏，一条 `transition:fade` 指令即可。

## 1. 父传子：$props

```svelte
<!-- src/lib/Card.svelte -->
<script>
  let { title, description = "暂无描述" } = $props()
</script>

<article>
  <h2>{title}</h2>
  <p>{description}</p>
</article>
```

```svelte
<!-- 使用处 -->
<script>
  import Card from "$lib/Card.svelte"
</script>

<Card title="第一课" description="Svelte 组件通信" />
<Card title="默认描述示例" />
```

**讲解：**

1. `$props()` 返回组件收到的全部属性，解构出来即可使用。
2. `description = "暂无描述"` 是默认值：调用方不传时使用默认值。
3. 使用组件时像 HTML 标签一样传属性：`<Card title="..." />`。

## 2. 子传父：回调函数

```svelte
<!-- src/lib/ConfirmButton.svelte -->
<script>
  let { label = "删除", onConfirm } = $props()
</script>

<button
  onclick={() => {
    if (confirm("确定？")) onConfirm()
  }}
>
  {label}
</button>
```

```svelte
<!-- 使用处 -->
<script>
  import ConfirmButton from "$lib/ConfirmButton.svelte"

  function handleDelete() {
    console.log("执行删除")
  }
</script>

<ConfirmButton label="删除文章" onConfirm={handleDelete} />
```

**讲解：**

1. 子组件把"要通知父组件的事"声明为函数属性（`onConfirm`），父组件传入自己的处理函数。
2. 点击按钮后子组件调用 `onConfirm()`，父组件的 `handleDelete` 执行——数据流保持单向。
3. 这是 Svelte 5 推荐的子传父方式（旧版用 `createEventDispatcher`，新项目不必再用）。

## 3. bind:this 与组件绑定

```svelte
<!-- src/lib/InputBox.svelte -->
<script>
  let { value = $bindable(""), onchange } = $props()
</script>

<input
  bind:value={value}
  oninput={(e) => onchange?.(e.currentTarget.value)}
/>
```

**讲解：**

1. `$bindable("")` 把属性声明为"可双向绑定"：父组件传 `value` 时同步回传，不传时用空字符串默认值。
2. `bind:value={value}` 让输入框与这个可绑定属性双向同步——这是 Svelte 5 中"受控组件"的标准写法。
3. `onchange?.(...)` 是可选调用：父组件没传回调时安全跳过。
4. 需要直接操作 DOM 时用 `bind:this={element}` 拿到元素引用。

## 4. 过渡与动画

```svelte
<script>
  import { fade, slide } from "svelte/transition"
  import { flip } from "svelte/animate"

  let items = $state(["苹果", "香蕉", "橙子"])
  let visible = $state(true)
</script>

<button onclick={() => (visible = !visible)}>切换</button>

{#if visible}
  <p transition:fade={{ duration: 300 }}>淡入淡出</p>
  <p transition:slide={{ duration: 300 }}>滑入滑出</p>
{/if}

<ul>
  {#each items as item (item)}
    <li animate:flip>{item}</li>
  {/each}
</ul>
```

**讲解：**

1. `transition:fade` / `transition:slide` 在元素进入与离开时自动播放动画，参数对象控制时长。
2. `animate:flip` 让列表重排时其他项平滑移动，配合 `{#each}` 的 key 使用。
3. 动画均可用 CSS 变量与自定义 easing 控制；记得配合 `prefers-reduced-motion` 做无障碍降级。

## 5. 动手试试

1. 做一个 `TodoItem` 组件：接收 `todo` 属性，删除按钮通过回调通知父组件。
2. 给列表删除项加 `transition:fly` 飞出动画。
3. 用 `$derived` 统计未完成数量并显示在标题栏。

## 6. 一句话记住

> 父传子用 `$props()`，子传父用回调属性；列表动画一条 `animate:flip`，进出场一条 `transition:fade`。
