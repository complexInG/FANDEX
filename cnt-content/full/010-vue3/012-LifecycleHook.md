---
order: 55
tags:
  - vue3
difficulty: intermediate
title: 生命周期钩子
module: vue3
category: 'Vue3 Basics'
description: Vue3组件生命周期钩子详解：创建、挂载、更新、卸载与调试钩子的使用场景。
author: fanquanpp
updated: '2026-08-01'
related:
  - vue3/Vue3编译优化
  - vue3/Vue3服务端渲染
  - vue3/Vue3测试策略
  - 'vue3/Vue3与Web Components'
prerequisites:
  - vue3/语法速查
---

## 1. 学习目标（Bloom 分类）

本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《生命周期钩子》，属于 Vue 3 模块，读者可以根据自身阶段选择阅读深度。

记忆层面：能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。能够说出 Vue 3 的核心概念、术语与标准写法。

理解层面：能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。能够解释 Vue 3 的工作原理与设计动机。

应用层面：能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。能够编写符合 Vue 3 规范的完整实现。

分析层面：能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。能够分析 Vue 3 与相邻方案的差异与边界。

评价层面：能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。能够根据场景评价 Vue 3 相关方案的优劣。

创造层面：能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。能够组合 Vue 3 与其他技术设计完整方案。

通过本节学习，读者应当能够把《生命周期钩子》纳入自己的知识网络，并与 Vue 3 模块的其他主题（组合式 API、响应式、组件通信、路由、状态管理）建立关联。

## 2. 历史动机与发展脉络

《生命周期钩子》是 Vue 3 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。

Vue 由尤雨溪于 2014 年发布，以“渐进式框架”定位：可作库嵌入，也可作框架构建完整应用。Vue 3 于 2020 年 9 月发布，核心是组合式 API 与全新响应式系统。
Vue 3 的技术支柱：Proxy 响应式（替代 Object.defineProperty）、虚拟 DOM 重写（PatchFlags）、Fragment/Teleport/Suspense 内置组件、组合式 API（setup/ref/reactive/computed）。
生态现状：Vue Router 4、Pinia（官方状态库）、Vite 构建、Nuxt 全栈框架；Vue 3.5 引入 useTemplateRef 等开发者体验改进。

回到本文主题：生命周期钩子 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。


## 3. 形式化定义与核心概念精讲

本节把《生命周期钩子》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。

响应式：ref 包装基本类型，reactive 包装对象；effect 收集依赖，Proxy 拦截读写；computed 缓存派生值。
组件通信：props 向下、emit 向上、v-model 双向、provide/inject 跨层、事件总线（慎用）。
生命周期：setup 在创建前执行；onMounted/onUpdated/onUnmounted 对应挂载、更新、卸载；KeepAlive 增加 activated/deactivated。

### 3.1 原文章节逐一精讲

原文档把主题拆分为 16 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。

#### 原文精读（完整保留）

# 生命周期 API 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

#### 1. 生命周期概述

##### 1.1 Vue3 生命周期流程

```
创建阶段: setup() → onBeforeMount → onMounted
更新阶段: onBeforeUpdate → onUpdated
卸载阶段: onBeforeUnmount → onUnmounted
调试钩子: onRenderTracked → onRenderTriggered
```

##### 1.2 选项式 vs 组合式 API

| 选项式 API      | 组合式 API（setup中） | 说明           |
| :-------------- | :-------------------- | :------------- |
| beforeCreate    | setup()               | 组件实例创建前 |
| created         | setup()               | 组件实例创建后 |
| beforeMount     | onBeforeMount         | 挂载前         |
| mounted         | onMounted             | 挂载后         |
| beforeUpdate    | onBeforeUpdate        | 更新前         |
| updated         | onUpdated             | 更新后         |
| beforeUnmount   | onBeforeUnmount       | 卸载前         |
| unmounted       | onUnmounted           | 卸载后         |
| errorCaptured   | onErrorCaptured       | 错误捕获       |
| renderTracked   | onRenderTracked       | 渲染依赖追踪   |
| renderTriggered | onRenderTriggered     | 渲染触发       |

> 注意：在组合式API中，`beforeCreate` 和 `created` 的逻辑直接写在 `setup()` 中。

#### 2. 各生命周期钩子详解

##### 2.1 onMounted

组件挂载完成后调用，此时DOM已渲染，可以访问DOM元素。

```vue
<template>
  <div ref="container">内容区域</div>
  <canvas ref="canvas"></canvas>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const container = ref(null);
const canvas = ref(null);

onMounted(() => {
  // 访问DOM元素
  console.log(container.value); // <div>内容区域</div>

  // 初始化Canvas
  const ctx = canvas.value.getContext('2d');
  ctx.fillStyle = '#3498db';
  ctx.fillRect(0, 0, 100, 100);

  // 获取元素尺寸
  const rect = container.value.getBoundingClientRect();
  console.log('元素尺寸:', rect.width, rect.height);

  // 初始化第三方库
  // const chart = new Chart(canvas.value, config)
});

// 可以注册多个onMounted，按注册顺序执行
onMounted(() => {
  console.log('第二个onMounted');
});
</script>
```

##### 2.2 onUpdated

组件更新完成后调用，可以访问更新后的DOM。

```vue
<template>
  <div ref="content">{{ message }}</div>
  <button @click="message = 'Updated!'">更新</button>
</template>

<script setup>
import { ref, onUpdated } from 'vue';

const message = ref('Hello');
const content = ref(null);

onUpdated(() => {
  // DOM已更新
  console.log('DOM已更新，内容:', content.value?.textContent);

  // 注意：避免在onUpdated中修改响应式数据，可能导致无限循环
});
</script>
```

##### 2.3 onBeforeUnmount 与 onUnmounted

```vue
<template>
  <div>定时器组件</div>
</template>

<script setup>
import { ref, onBeforeUnmount, onUnmounted } from 'vue';

const timer = ref(null);
const resizeObserver = ref(null);

// 启动定时器
timer.value = setInterval(() => {
  console.log('定时执行');
}, 1000);

// 启动ResizeObserver
onMounted(() => {
  resizeObserver.value = new ResizeObserver((entries) => {
    console.log('尺寸变化:', entries);
  });
  resizeObserver.value.observe(document.body);
});

// onBeforeUnmount: 组件卸载前，实例仍然可用
onBeforeUnmount(() => {
  console.log('组件即将卸载，清理资源...');

  // 清理定时器
  if (timer.value) {
    clearInterval(timer.value);
    timer.value = null;
  }

  // 清理Observer
  if (resizeObserver.value) {
    resizeObserver.value.disconnect();
    resizeObserver.value = null;
  }
});

// onUnmounted: 组件已卸载，所有子组件也已卸载
onUnmounted(() => {
  console.log('组件已完全卸载');
});
</script>
```

##### 2.4 onErrorCaptured

捕获后代组件的错误，用于错误边界。

```vue
<script setup>
import { ref, onErrorCaptured } from 'vue';

const error = ref(null);

onErrorCaptured((err, instance, info) => {
  // err: 错误对象
  // instance: 触发错误的组件实例
  // info: 错误来源信息（如 'render'、'event handler'）

  console.error('捕获到子组件错误:', err);
  console.error('错误来源:', info);

  error.value = err.message;

  // 返回false阻止错误继续向上传播
  return false;

  // 返回true或不返回，错误继续传播
});
</script>

<template>
  <div v-if="error" class="error-boundary">
    <h3>出错了</h3>
    <p>{{ error }}</p>
    <button @click="error = null">重试</button>
  </div>
  <slot v-else />
</template>
```

#### 3. 生命周期实战模式

##### 3.1 异步数据加载

```vue
<template>
  <div v-if="loading">加载中...</div>
  <div v-else-if="error">{{ error }}</div>
  <div v-else>
    <ul>
      <li v-for="item in data" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const data = ref([]);
const loading = ref(true);
const error = ref(null);

async function fetchData() {
  loading.value = true;
  error.value = null;
  try {
    const response = await fetch('/api/items');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    data.value = await response.json();
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}

onMounted(fetchData);
</script>
```

##### 3.2 事件监听器管理

```vue
<script setup>
import { onMounted, onBeforeUnmount } from 'vue';

// 键盘快捷键
function handleKeydown(e) {
  if (e.key === 'Escape') {
    // 关闭弹窗等
  }
}

// 窗口大小变化
function handleResize() {
  // 响应式调整
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown);
  window.addEventListener('resize', handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener('keydown', handleKeydown);
  window.removeEventListener('resize', handleResize);
});
</script>
```

##### 3.3 轮询数据

```vue
<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const data = ref(null);
let pollTimer = null;
const POLL_INTERVAL = 5000;

async function pollData() {
  try {
    const response = await fetch('/api/status');
    data.value = await response.json();
  } catch (err) {
    console.error('轮询失败:', err);
  }
}

onMounted(() => {
  pollData(); // 立即执行一次
  pollTimer = setInterval(pollData, POLL_INTERVAL);
});

onBeforeUnmount(() => {
  if (pollTimer) {
    clearInterval(pollTimer);
    pollTimer = null;
  }
});
</script>
```

#### 4. 服务器端渲染（SSR）注意事项

```vue
<script setup>
import { ref, onMounted } from 'vue';

const windowWidth = ref(0);

// onMounted只在客户端执行，SSR时不会运行
onMounted(() => {
  windowWidth.value = window.innerWidth;

  window.addEventListener('resize', () => {
    windowWidth.value = window.innerWidth;
  });
});

// 避免在setup顶层访问浏览器API
// const width = window.innerWidth  // SSR报错！

// 使用onMounted保护浏览器API调用
</script>
```

#### 5. 常见问题与解决方案

##### 5.1 onUpdated 无限循环

```vue
<!-- 错误：onUpdated中修改响应式数据 -->
<script setup>
import { ref, onUpdated } from 'vue';

const count = ref(0);

onUpdated(() => {
  count.value++; // 触发更新 → 再次调用onUpdated → 无限循环！
});
</script>

<!-- 正确：只在特定条件下修改 -->
<script setup>
import { ref, onUpdated } from 'vue';

const count = ref(0);
const needsUpdate = ref(false);

onUpdated(() => {
  if (needsUpdate.value) {
    needsUpdate.value = false;
    // 执行更新
  }
});
</script>
```

##### 5.2 内存泄漏

```vue
<script setup>
import { onBeforeUnmount } from 'vue';

// 常见泄漏源及清理
onBeforeUnmount(() => {
  // 1. 清除定时器
  clearInterval(timer);

  // 2. 移除事件监听
  window.removeEventListener('scroll', handleScroll);

  // 3. 断开Observer
  observer.disconnect();

  // 4. 取消未完成的请求
  abortController.abort();

  // 5. 清理第三方库实例
  chart.destroy();
});
</script>
```

##### 5.3 异步操作在组件卸载后执行

```vue
<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const isMounted = ref(false);

onMounted(() => {
  isMounted.value = true;

  fetchData().then((data) => {
    // 检查组件是否仍然挂载
    if (!isMounted.value) return;
    // 安全地更新状态
    items.value = data;
  });
});

onBeforeUnmount(() => {
  isMounted.value = false;
});
</script>
```

#### 6. 总结与最佳实践

##### 6.1 生命周期使用场景

| 钩子            | 典型用途                          |
| :-------------- | :-------------------------------- |
| setup()         | 初始化响应式数据、计算属性        |
| onMounted       | DOM操作、异步请求、初始化第三方库 |
| onUpdated       | DOM更新后的操作（谨慎使用）       |
| onBeforeUnmount | 清理定时器、事件监听、第三方实例  |
| onErrorCaptured | 错误边界、错误日志上报            |

##### 6.2 最佳实践

1. **资源获取与释放配对**：onMounted获取，onBeforeUnmount释放
2. **避免onUpdated中修改状态**：防止无限循环
3. **SSR安全**：浏览器API只在onMounted中使用
4. **使用组合函数封装**：将生命周期逻辑提取到可复用的composable中
5. **异步操作检查挂载状态**：防止卸载后更新状态
#### 生命周期钩子总览

**组合式 API 钩子对照**
```typescript
import {
  onBeforeMount,    // 挂载前
  onMounted,        // 已挂载
  onBeforeUpdate,   // 更新前
  onUpdated,        // 已更新
  onBeforeUnmount,  // 卸载前
  onUnmounted,      // 已卸载
  onErrorCaptured,  // 错误捕获
  onActivated,      // KeepAlive 激活
  onDeactivated,    // KeepAlive 停用
  onServerPrefetch  // SSR 预取
} from 'vue';
```

---

#### 创建与挂载阶段

**onBeforeMount 挂载前**
`onBeforeMount(<callback>);`
```typescript
import { onBeforeMount } from 'vue';
onBeforeMount(() => {
  console.log('组件即将挂载,DOM 尚未生成');
});
```

**onMounted 已挂载**
`onMounted(<callback>);`
```typescript
import { ref, onMounted } from 'vue';
const inputRef = ref<HTMLInputElement | null>(null);

onMounted(() => {
  console.log('组件已挂载,DOM 可访问');
  inputRef.value?.focus();
});

onMounted(() => {
  const timer = setInterval(() => console.log('tick'), 1000);
  // 在 onUnmounted 中清理
});
```

---

#### 更新阶段

**onBeforeUpdate 更新前**
`onBeforeUpdate(<callback>);`
```typescript
import { onBeforeUpdate } from 'vue';
onBeforeUpdate(() => {
  console.log('DOM 即将更新,此时访问的是旧 DOM');
});
```

**onUpdated 已更新**
`onUpdated(<callback>);`
```typescript
import { onUpdated } from 'vue';
onUpdated(() => {
  console.log('DOM 已更新完毕');
  // 注意:不要在此处修改响应式状态,可能引起死循环
});
```

---

#### 卸载阶段

**onBeforeUnmount 卸载前**
`onBeforeUnmount(<callback>);`
```typescript
import { onBeforeUnmount } from 'vue';
let timer: number;

onBeforeUnmount(() => {
  console.log('组件即将卸载,实例仍可用');
  clearInterval(timer);
});
```

**onUnmounted 已卸载**
`onUnmounted(<callback>);`
```typescript
import { onUnmounted } from 'vue';
onUnmounted(() => {
  console.log('组件已卸载,所有指令解绑,事件监听移除');
});
```

---

#### 错误处理

**onErrorCaptured 错误捕获**
`onErrorCaptured((err, instance, info) => <boolean | void>);`
```typescript
import { onErrorCaptured } from 'vue';
onErrorCaptured((err, instance, info) => {
  console.error('捕获错误:', err);
  console.log('组件实例:', instance);
  console.log('错误信息:', info);
  return false;  // 阻止继续向上传递
});
```

---

#### KeepAlive 钩子

**onActivated 激活**
`onActivated(<callback>);`
```typescript
import { onActivated } from 'vue';
onActivated(() => {
  console.log('被 keep-alive 缓存的组件激活');
});
```

**onDeactivated 停用**
`onDeactivated(<callback>);`
```typescript
import { onDeactivated } from 'vue';
onDeactivated(() => {
  console.log('被 keep-alive 缓存的组件停用');
});
```

---

#### 服务端渲染钩子

**onServerPrefetch SSR 预取**
`onServerPrefetch(<asyncCallback>);`
```typescript
import { onServerPrefetch } from 'vue';
onServerPrefetch(async () => {
  await fetchInitialData();
  console.log('服务端预取完成');
});
```

---

#### 调试钩子

**onRenderTracked 渲染依赖追踪(开发)**
`onRenderTracked((e) => {});`
```typescript
import { onRenderTracked } from 'vue';
onRenderTracked((event) => {
  console.log('渲染依赖被追踪:', event);
  // event: { effect, target, key, type }
});
```

**onRenderTriggered 渲染依赖触发(开发)**
`onRenderTriggered((e) => {});`
```typescript
import { onRenderTriggered } from 'vue';
onRenderTriggered((event) => {
  console.log('渲染依赖被触发:', event);
  // event: { effect, target, key, type, newValue, oldValue }
});
```

---

#### 钩子注册与清理

**多次注册同一钩子**
```typescript
onMounted(() => console.log('first'));
onMounted(() => console.log('second'));
// 两个回调都会按注册顺序执行
```

**注册顺序与组件生命周期**
```typescript
import { ref, onMounted } from 'vue';
const setup = () => {
  const state = ref(0);
  // setup 同步执行期间注册的钩子按顺序触发
  onMounted(() => console.log('A'));
  onMounted(() => console.log('B'));
  return { state };
};
```

**钩子中清理副作用**
```typescript
import { onMounted, onUnmounted } from 'vue';

function useInterval(callback: () => void, delay: number) {
  let timer: number | undefined;
  onMounted(() => {
    timer = setInterval(callback, delay);
  });
  onUnmounted(() => {
    if (timer) clearInterval(timer);
  });
}
```

---

#### 选项式 API 钩子对照

| 选项式 API | 组合式 API |
|---|---|
| beforeCreate | setup() 同步部分 |
| created | setup() 同步部分 |
| beforeMount | onBeforeMount |
| mounted | onMounted |
| beforeUpdate | onBeforeUpdate |
| updated | onUpdated |
| beforeUnmount | onBeforeUnmount |
| unmounted | onUnmounted |
| errorCaptured | onErrorCaptured |
| activated | onActivated |
| deactivated | onDeactivated |
| serverPrefetch | onServerPrefetch |
| renderTracked | onRenderTracked |
| renderTriggered | onRenderTriggered |


### 3.2 概念关系图

下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：

```mermaid
flowchart LR
    A["生命周期钩子"] --> B["核心概念"]
    B --> C["原理机制"]
    B --> D["代码实践"]
    C --> E["工程应用"]
    D --> E
```

图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。

## 4. 理论推导与原理解析

本节深入《生命周期钩子》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。

响应式：ref 包装基本类型，reactive 包装对象；effect 收集依赖，Proxy 拦截读写；computed 缓存派生值。
组件通信：props 向下、emit 向上、v-model 双向、provide/inject 跨层、事件总线（慎用）。
生命周期：setup 在创建前执行；onMounted/onUpdated/onUnmounted 对应挂载、更新、卸载；KeepAlive 增加 activated/deactivated。
模板编译：模板在构建期编译为渲染函数，指令（v-if/v-for/v-model）是编译糖。

需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。

## 5. 代码示例与逐行讲解

本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。

### 5.1 示例：1.1 Vue3 生命周期流程

该示例来自原文《1.1 Vue3 生命周期流程》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```text
创建阶段: setup() → onBeforeMount → onMounted
更新阶段: onBeforeUpdate → onUpdated
卸载阶段: onBeforeUnmount → onUnmounted
调试钩子: onRenderTracked → onRenderTriggered
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.2 示例：2.1 onMounted

该示例来自原文《2.1 onMounted》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<template>
  <div ref="container">内容区域</div>
  <canvas ref="canvas"></canvas>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const container = ref(null);
const canvas = ref(null);

onMounted(() => {
  // 访问DOM元素
  console.log(container.value); // <div>内容区域</div>

  // 初始化Canvas
  const ctx = canvas.value.getContext('2d');
  ctx.fillStyle = '#3498db';
  ctx.fillRect(0, 0, 100, 100);

  // 获取元素尺寸
  const rect = container.value.getBoundingClientRect();
  console.log('元素尺寸:', rect.width, rect.height);

  // 初始化第三方库
  // const chart = new Chart(canvas.value, config)
});

// 可以注册多个onMounted，按注册顺序执行
onMounted(() => {
  console.log('第二个onMounted');
});
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 26 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.3 示例：2.2 onUpdated

该示例来自原文《2.2 onUpdated》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<template>
  <div ref="content">{{ message }}</div>
  <button @click="message = 'Updated!'">更新</button>
</template>

<script setup>
import { ref, onUpdated } from 'vue';

const message = ref('Hello');
const content = ref(null);

onUpdated(() => {
  // DOM已更新
  console.log('DOM已更新，内容:', content.value?.textContent);

  // 注意：避免在onUpdated中修改响应式数据，可能导致无限循环
});
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.4 示例：2.3 onBeforeUnmount 与 onUnmounted

该示例来自原文《2.3 onBeforeUnmount 与 onUnmounted》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<template>
  <div>定时器组件</div>
</template>

<script setup>
import { ref, onBeforeUnmount, onUnmounted } from 'vue';

const timer = ref(null);
const resizeObserver = ref(null);

// 启动定时器
timer.value = setInterval(() => {
  console.log('定时执行');
}, 1000);

// 启动ResizeObserver
onMounted(() => {
  resizeObserver.value = new ResizeObserver((entries) => {
    console.log('尺寸变化:', entries);
  });
  resizeObserver.value.observe(document.body);
});

// onBeforeUnmount: 组件卸载前，实例仍然可用
onBeforeUnmount(() => {
  console.log('组件即将卸载，清理资源...');

  // 清理定时器
  if (timer.value) {
    clearInterval(timer.value);
    timer.value = null;
  }

  // 清理Observer
  if (resizeObserver.value) {
    resizeObserver.value.disconnect();
    resizeObserver.value = null;
  }
});

// onUnmounted: 组件已卸载，所有子组件也已卸载
onUnmounted(() => {
  console.log('组件已完全卸载');
});
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 37 行有效代码，包含 3 类关键结构（import、from、if）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.5 示例：2.4 onErrorCaptured

该示例来自原文《2.4 onErrorCaptured》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<script setup>
import { ref, onErrorCaptured } from 'vue';

const error = ref(null);

onErrorCaptured((err, instance, info) => {
  // err: 错误对象
  // instance: 触发错误的组件实例
  // info: 错误来源信息（如 'render'、'event handler'）

  console.error('捕获到子组件错误:', err);
  console.error('错误来源:', info);

  error.value = err.message;

  // 返回false阻止错误继续向上传播
  return false;

  // 返回true或不返回，错误继续传播
});
</script>

<template>
  <div v-if="error" class="error-boundary">
    <h3>出错了</h3>
    <p>{{ error }}</p>
    <button @click="error = null">重试</button>
  </div>
  <slot v-else />
</template>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 23 行有效代码，包含 4 类关键结构（class、import、from、return）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.6 示例：3.1 异步数据加载

该示例来自原文《3.1 异步数据加载》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<template>
  <div v-if="loading">加载中...</div>
  <div v-else-if="error">{{ error }}</div>
  <div v-else>
    <ul>
      <li v-for="item in data" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const data = ref([]);
const loading = ref(true);
const error = ref(null);

async function fetchData() {
  loading.value = true;
  error.value = null;
  try {
    const response = await fetch('/api/items');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    data.value = await response.json();
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}

onMounted(fetchData);
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 29 行有效代码，包含 4 类关键结构（function、import、from、if）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.7 示例：3.2 事件监听器管理

该示例来自原文《3.2 事件监听器管理》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<script setup>
import { onMounted, onBeforeUnmount } from 'vue';

// 键盘快捷键
function handleKeydown(e) {
  if (e.key === 'Escape') {
    // 关闭弹窗等
  }
}

// 窗口大小变化
function handleResize() {
  // 响应式调整
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown);
  window.addEventListener('resize', handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener('keydown', handleKeydown);
  window.removeEventListener('resize', handleResize);
});
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 21 行有效代码，包含 4 类关键结构（function、import、from、if）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.8 示例：3.3 轮询数据

该示例来自原文《3.3 轮询数据》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const data = ref(null);
let pollTimer = null;
const POLL_INTERVAL = 5000;

async function pollData() {
  try {
    const response = await fetch('/api/status');
    data.value = await response.json();
  } catch (err) {
    console.error('轮询失败:', err);
  }
}

onMounted(() => {
  pollData(); // 立即执行一次
  pollTimer = setInterval(pollData, POLL_INTERVAL);
});

onBeforeUnmount(() => {
  if (pollTimer) {
    clearInterval(pollTimer);
    pollTimer = null;
  }
});
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 24 行有效代码，包含 4 类关键结构（function、import、from、if）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.9 示例：4. 服务器端渲染（SSR）注意事项

该示例来自原文《4. 服务器端渲染（SSR）注意事项》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<script setup>
import { ref, onMounted } from 'vue';

const windowWidth = ref(0);

// onMounted只在客户端执行，SSR时不会运行
onMounted(() => {
  windowWidth.value = window.innerWidth;

  window.addEventListener('resize', () => {
    windowWidth.value = window.innerWidth;
  });
});

// 避免在setup顶层访问浏览器API
// const width = window.innerWidth  // SSR报错！

// 使用onMounted保护浏览器API调用
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.10 示例：5.1 onUpdated 无限循环

该示例来自原文《5.1 onUpdated 无限循环》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<!-- 错误：onUpdated中修改响应式数据 -->
<script setup>
import { ref, onUpdated } from 'vue';

const count = ref(0);

onUpdated(() => {
  count.value++; // 触发更新 → 再次调用onUpdated → 无限循环！
});
</script>

<!-- 正确：只在特定条件下修改 -->
<script setup>
import { ref, onUpdated } from 'vue';

const count = ref(0);
const needsUpdate = ref(false);

onUpdated(() => {
  if (needsUpdate.value) {
    needsUpdate.value = false;
    // 执行更新
  }
});
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 20 行有效代码，包含 3 类关键结构（import、from、if）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.11 示例：5.2 内存泄漏

该示例来自原文《5.2 内存泄漏》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<script setup>
import { onBeforeUnmount } from 'vue';

// 常见泄漏源及清理
onBeforeUnmount(() => {
  // 1. 清除定时器
  clearInterval(timer);

  // 2. 移除事件监听
  window.removeEventListener('scroll', handleScroll);

  // 3. 断开Observer
  observer.disconnect();

  // 4. 取消未完成的请求
  abortController.abort();

  // 5. 清理第三方库实例
  chart.destroy();
});
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 16 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.12 示例：5.3 异步操作在组件卸载后执行

该示例来自原文《5.3 异步操作在组件卸载后执行》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```vue
<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const isMounted = ref(false);

onMounted(() => {
  isMounted.value = true;

  fetchData().then((data) => {
    // 检查组件是否仍然挂载
    if (!isMounted.value) return;
    // 安全地更新状态
    items.value = data;
  });
});

onBeforeUnmount(() => {
  isMounted.value = false;
});
</script>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 16 行有效代码，包含 4 类关键结构（import、from、if、return）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.13 示例：生命周期钩子总览

该示例来自原文《生命周期钩子总览》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import {
  onBeforeMount,    // 挂载前
  onMounted,        // 已挂载
  onBeforeUpdate,   // 更新前
  onUpdated,        // 已更新
  onBeforeUnmount,  // 卸载前
  onUnmounted,      // 已卸载
  onErrorCaptured,  // 错误捕获
  onActivated,      // KeepAlive 激活
  onDeactivated,    // KeepAlive 停用
  onServerPrefetch  // SSR 预取
} from 'vue';
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.14 示例：创建与挂载阶段

该示例来自原文《创建与挂载阶段》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onBeforeMount } from 'vue';
onBeforeMount(() => {
  console.log('组件即将挂载,DOM 尚未生成');
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.15 示例：创建与挂载阶段

该示例来自原文《创建与挂载阶段》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { ref, onMounted } from 'vue';
const inputRef = ref<HTMLInputElement | null>(null);

onMounted(() => {
  console.log('组件已挂载,DOM 可访问');
  inputRef.value?.focus();
});

onMounted(() => {
  const timer = setInterval(() => console.log('tick'), 1000);
  // 在 onUnmounted 中清理
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.16 示例：更新阶段

该示例来自原文《更新阶段》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onBeforeUpdate } from 'vue';
onBeforeUpdate(() => {
  console.log('DOM 即将更新,此时访问的是旧 DOM');
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.17 示例：更新阶段

该示例来自原文《更新阶段》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onUpdated } from 'vue';
onUpdated(() => {
  console.log('DOM 已更新完毕');
  // 注意:不要在此处修改响应式状态,可能引起死循环
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.18 示例：卸载阶段

该示例来自原文《卸载阶段》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onBeforeUnmount } from 'vue';
let timer: number;

onBeforeUnmount(() => {
  console.log('组件即将卸载,实例仍可用');
  clearInterval(timer);
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.19 示例：卸载阶段

该示例来自原文《卸载阶段》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onUnmounted } from 'vue';
onUnmounted(() => {
  console.log('组件已卸载,所有指令解绑,事件监听移除');
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.20 示例：错误处理

该示例来自原文《错误处理》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onErrorCaptured } from 'vue';
onErrorCaptured((err, instance, info) => {
  console.error('捕获错误:', err);
  console.log('组件实例:', instance);
  console.log('错误信息:', info);
  return false;  // 阻止继续向上传递
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 3 类关键结构（import、from、return）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.21 示例：KeepAlive 钩子

该示例来自原文《KeepAlive 钩子》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onActivated } from 'vue';
onActivated(() => {
  console.log('被 keep-alive 缓存的组件激活');
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.22 示例：KeepAlive 钩子

该示例来自原文《KeepAlive 钩子》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onDeactivated } from 'vue';
onDeactivated(() => {
  console.log('被 keep-alive 缓存的组件停用');
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.23 示例：服务端渲染钩子

该示例来自原文《服务端渲染钩子》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onServerPrefetch } from 'vue';
onServerPrefetch(async () => {
  await fetchInitialData();
  console.log('服务端预取完成');
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.24 示例：调试钩子

该示例来自原文《调试钩子》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onRenderTracked } from 'vue';
onRenderTracked((event) => {
  console.log('渲染依赖被追踪:', event);
  // event: { effect, target, key, type }
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.25 示例：调试钩子

该示例来自原文《调试钩子》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onRenderTriggered } from 'vue';
onRenderTriggered((event) => {
  console.log('渲染依赖被触发:', event);
  // event: { effect, target, key, type, newValue, oldValue }
});
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 2 类关键结构（import、from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.26 示例：钩子注册与清理

该示例来自原文《钩子注册与清理》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
onMounted(() => console.log('first'));
onMounted(() => console.log('second'));
// 两个回调都会按注册顺序执行
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.27 示例：钩子注册与清理

该示例来自原文《钩子注册与清理》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { ref, onMounted } from 'vue';
const setup = () => {
  const state = ref(0);
  // setup 同步执行期间注册的钩子按顺序触发
  onMounted(() => console.log('A'));
  onMounted(() => console.log('B'));
  return { state };
};
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 3 类关键结构（import、from、return）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.28 示例：钩子注册与清理

该示例来自原文《钩子注册与清理》小节，用于演示生命周期钩子相关操作。阅读时请先看代码结构，再看其后的讲解。

```typescript
import { onMounted, onUnmounted } from 'vue';

function useInterval(callback: () => void, delay: number) {
  let timer: number | undefined;
  onMounted(() => {
    timer = setInterval(callback, delay);
  });
  onUnmounted(() => {
    if (timer) clearInterval(timer);
  });
}
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 4 类关键结构（function、import、from、if）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。


综合以上示例，可以总结出本主题的代码实践要点：第一，先定义清晰的输入输出契约；第二，核心逻辑保持单一职责；第三，错误处理与边界条件不可省略；第四，命名与注释表达意图而非复述代码。

## 6. 对比分析

对比是理解《生命周期钩子》定位的最快路径。下面从多个维度与相邻方案进行对比。

Vue 与 React：Vue 模板 + 响应式自动追踪，React JSX + 手动依赖（hooks）；Vue 上手平缓，React 生态更广。
Options API 与 Composition API：Composition 更适合逻辑复用与 TS；Options 保留简单场景。
Vue 2 与 Vue 3：响应式实现、API 形态、生态差异显著，新项目一律 Vue 3。

对比的目的不是分出绝对优劣，而是建立选择依据：不同约束条件下，最优解不同。读者应把每个对比维度转化为决策检查清单。

## 7. 常见陷阱与最佳实践

本节整理该主题的高频错误与推荐做法。每个陷阱先描述现象，再解释原因，最后给出最佳实践。

### 7.1 响应式丢失

解构 reactive 或赋值整对象丢失响应。使用 ref/toRefs。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，响应式丢失 一般源于对 Vue 3 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，响应式丢失 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理响应式丢失的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.2 v-for key 用索引

列表变更导致状态错位。使用稳定唯一 key。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，v-for key 用索引 一般源于对 Vue 3 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，v-for key 用索引 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理v-for key 用索引的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.3 props 直接修改

单向数据流被破坏。通过 emit 通知父组件修改。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，props 直接修改 一般源于对 Vue 3 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，props 直接修改 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理props 直接修改的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.4 watch 深层陷阱

监听对象默认浅层；深层用 deep 或改写为 getter。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，watch 深层陷阱 一般源于对 Vue 3 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，watch 深层陷阱 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理watch 深层陷阱的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.5 组件样式泄漏

未用 scoped 导致全局污染。组件样式默认 scoped。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，组件样式泄漏 一般源于对 Vue 3 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，组件样式泄漏 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理组件样式泄漏的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.6 setup 中 async 误用

setup 顶层 await 变为异步组件需 Suspense。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，setup 中 async 误用 一般源于对 Vue 3 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，setup 中 async 误用 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理setup 中 async 误用的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.7 路由组件复用不刷新

参数变化组件复用。watch route 或 beforeRouteUpdate。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，路由组件复用不刷新 一般源于对 Vue 3 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，路由组件复用不刷新 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理路由组件复用不刷新的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.8 响应式大对象性能

深层代理开销大。大数据用 shallowRef 或冻结。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，响应式大对象性能 一般源于对 Vue 3 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，响应式大对象性能 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理响应式大对象性能的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.0 最佳实践总览

1. 组合式 API 按逻辑组织（自定义组合函数 useXxx）。
2. 组件单一职责，props 使用类型定义（TS）。
3. 状态管理：局部状态用 ref，跨组件用 Pinia，服务端状态用 Query 类库。
4. 模板保持声明式，复杂逻辑进 script。

把这些最佳实践固化为团队规范与代码评审检查项，是避免同类问题反复出现的关键。

## 8. 工程实践

本节把《生命周期钩子》放入真实工程场景，给出可复用的模式与组织方法。

项目脚手架：create-vue（Vite + TS + Router + Pinia）。
目录分层：views（页面）、components（组件）、composables（逻辑）、stores（状态）、api（请求）。
性能：defineAsyncComponent 懒加载、v-memo 优化、虚拟列表。
测试：Vitest 单测 + Vue Test Utils；Playwright E2E。

### 8.1 工程实践的原则拆解

以上工程实践可以归纳为四条原则。第一，配置与代码分离：Vue 3 项目中环境差异应通过配置注入，而不是散落在代码分支中；这保证同一份代码可以在开发、测试、生产环境一致运行。

第二，接口稳定优先：对外接口（函数签名、协议、数据格式）一旦被消费方依赖，变更成本极高；设计时应预留扩展点并保持向后兼容。

第三，可观测性内置：日志、指标与追踪应该在功能开发时同步设计，而不是故障发生后补救；没有观测手段的模块等于黑盒。

第四，变更可回滚：任何发布都应有对应的回滚方案；数据库迁移、配置变更与代码发布一样需要版本管理与逆向路径。

### 8.2 实践落地的检查清单

- [ ] 项目脚手架：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 目录分层：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 性能：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 测试：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。

工程实践的共性原则：配置与代码分离、接口稳定优先、可观测性内置、变更可回滚。这些原则适用于本主题的所有实现。

## 9. 案例研究

本节通过一个完整案例把《生命周期钩子》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。

需求：实现文档站的搜索页与主题切换。
方案：Vue Router 路由 + Pinia 管理主题 + 组合函数封装搜索。
要点：搜索防抖与竞态取消；主题变量持久化。
验证：路由守卫权限、主题刷新保持、搜索准确性测试。

### 9.1 案例的扩展讨论

把案例中的方案放大到真实规模，需要额外考虑三个问题：

第一，规模：当数据量或并发量上升一个数量级时，原方案中的数据结构、缓存策略与任务调度是否仍然成立？通常需要引入分层与异步。

第二，团队：多人协作时，模块边界、接口契约与代码所有权必须明确；案例中的实现应拆分为可独立测试的单元，并配合文档说明设计意图。

第三，演进：上线后的需求变化不可避免；方案设计时应预留扩展点（配置化、插件化、事件化），并定期用真实指标验证假设。


案例研究的学习方法：先独立阅读需求，尝试在脑中形成方案，再对照实现与讲解，最后思考“如果约束变化（数据量、并发、团队规模），方案应如何调整”。

## 10. 知识要点总结与深入讲解

本节以讲解形式汇总全文要点，替代传统的习题与自测，读者不需要答题，只需跟随解释建立完整的认知框架。

关于《生命周期钩子》的核心结论：

Vue 3 的核心是响应式与组合式：理解依赖收集才能驾驭性能与陷阱。
组件通信按层级选型：props/emit 为默认，provide/inject 跨层，Pinia 全局。
工程化（Vite + TS + 测试）是生产项目的基线。

原文档各小节的要点回顾：

- 1. 生命周期概述：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 2. 各生命周期钩子详解：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 3. 生命周期实战模式：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 4. 服务器端渲染（SSR）注意事项：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 5. 常见问题与解决方案：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 6. 总结与最佳实践：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 生命周期钩子总览：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 创建与挂载阶段：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 更新阶段：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 卸载阶段：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 错误处理：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- KeepAlive 钩子：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 服务端渲染钩子：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 调试钩子：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 钩子注册与清理：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 选项式 API 钩子对照：该小节围绕生命周期钩子展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。

把以上要点与第 3-9 节的内容对照复习，即可完成对本文主题的闭环学习。

## 11. 参考文献


Vue 官方文档：https://vuejs.org/
Vue Router：https://router.vuejs.org/zh/
Pinia：https://pinia.vuejs.org/zh/
Vue 3 迁移指南：https://v3-migration.vuejs.org/
VueUse 组合函数库：https://vueuse.org/

## 12. 延伸阅读


Vue Teleport 与 Portal，见 010-vue3/026-TeleportPortalApp 文档。
Vue KeepAlive 缓存，见 010-vue3/027-KeepAliveCacheLifecycle 文档。
Vue Router 导航守卫，见 010-vue3/030-VueRouterNavigationGuard 文档。
TypeScript 与 Vue 组合，见 009-typescript 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Vue3 课程。

## 14. 模块知识图谱与学习路径

本文属于 Vue 3 模块。为了把《生命周期钩子》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。

```mermaid
flowchart LR
    A["生命周期钩子"]
    N0["概述与环境"]
    N1["Vue3 快速入门指南"]
    N0 --> N1
    N2["Vue3 模板语法"]
    N1 --> N2
    N3["Vue3 指令系统"]
    N2 --> N3
    N4["Teleport与Suspense"]
    N3 --> N4
    N5["组合式 API"]
    N4 --> N5
    N6["Provide与Inject"]
    N5 --> N6
    N7["自定义指令进阶"]
    N6 --> N7
    N8["Transition与动画"]
    N7 --> N8
    N9["Vue3编译优化"]
    N8 --> N9
    N10["Vue3服务端渲染"]
    N9 --> N10
    N11["生命周期钩子"]
    N10 --> N11
    N12["Vue3测试策略"]
    N11 --> N12
    N13["Vue3与Web Components"]
    N12 --> N13
```

上图为模块主题的推荐学习顺序示意图（仅展示前若干主题）。各主题之间存在三类关联：

第一，前置依赖关系：早期主题是后期主题的基础，例如环境与语法先行、进阶主题随后；

第二，横向并列关系：同一层级主题从不同角度覆盖模块能力，学习顺序可以按兴趣调整；

第三，工程组合关系：多个主题在真实项目中组合使用，例如配置、性能与安全主题往往出现在同一系统的不同层面。

### 14.1 模块主题速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与环境 | 001-OverviewEnv | 本文的前置基础 |
| Vue3 快速入门指南 | 002-Vue3QuickStartGuide | 本文的前置基础 |
| Vue3 模板语法 | 003-Vue3TemplateSyntax | 本文的并列主题 |
| Vue3 指令系统 | 004-Vue3DirectiveSystem | 本文的并列主题 |
| Teleport与Suspense | 005-TeleportSuspense | 本文的并列主题 |
| 组合式 API | 006-API | 本文的并列主题 |
| Provide与Inject | 007-ProvideInject | 本文的并列主题 |
| 自定义指令进阶 | 008-CustomDirectiveAdvanced | 本文的并列主题 |
| Transition与动画 | 009-TransitionAnimation | 本文的并列主题 |
| Vue3编译优化 | 010-Vue3CompileOptimization | 本文的性能延伸 |
| Vue3服务端渲染 | 011-Vue3SSR | 本文的并列主题 |
| 生命周期钩子 | 012-LifecycleHook | 本文自身 |
| Vue3测试策略 | 013-Vue3TestStrategy | 本文的并列主题 |
| Vue3与Web Components | 014-Vue3WebComponents | 本文的并列主题 |
| Vue3性能优化实践 | 015-Vue3PerformancePractice | 本文的性能延伸 |
| 响应式系统 | 016-ReactiveSystem | 本文的并列主题 |
| 自定义 Hook | 017-CustomHook | 本文的并列主题 |
| 组件系统 | 018-ComponentSystem | 本文的并列主题 |
| TypeScript 集成 | 019-TypeScriptIntegration | 本文的并列主题 |
| Pinia 状态管理详解 | 020-PiniaStateManagementDetailed | 本文的并列主题 |
| 插件开发 | 021-PluginDevelopment | 本文的并列主题 |
| computed缓存机制与watch执行时机 | 022-ComputedCacheWatchTiming | 本文的原理深化 |
| Vue Router 详解 | 023-VueRouterDetailed | 本文的并列主题 |
| 组合式API优势场景 | 024-CompositionAPIAdvantageScene | 本文的并列主题 |
| 自定义组合函数封装 | 025-CustomComposableWrapper | 本文的并列主题 |
| Teleport传送门应用 | 026-TeleportPortalApp | 本文的并列主题 |
| KeepAlive缓存与生命周期 | 027-KeepAliveCacheLifecycle | 本文的并列主题 |
| 异步组件与Suspense | 028-AsyncComponentSuspense | 本文的并列主题 |
| Pinia持久化插件 | 029-PiniaPersistencePlugin | 本文的并列主题 |
| Vue-Router导航守卫 | 030-VueRouterNavigationGuard | 本文的并列主题 |
| Vue性能优化详解 | 031-VuePerformanceDetailed | 本文的性能延伸 |
| 性能优化 | 032-PerformanceOptimization | 本文的性能延伸 |
| Vue3 高级组件特性 | 033-Vue3AdvancedComponentFeature | 本文的并列主题 |
| Vue3 项目示例：个人博客站点 | 034-Vue3ProjectExampleBlog | 本文的综合应用 |
| Vue3 理论知识点 | 035-Vue3TheoryKnowledge | 本文的并列主题 |
| Vue 3 Vite 构建配置与命令 | 036-Vue3ViteBuildConfig | 本文的并列主题 |
| Vue 3.4 / 3.5 新特性 | 037-Vue3NewFeatures3435 | 本文的并列主题 |

速查表的作用是让读者快速判断：哪些文档应在阅读本文前掌握（前置基础），哪些文档应在阅读本文后继续（延伸主题）。本模块的交叉引用体系即以此表为基础。

## 15. 术语表

下表整理《生命周期钩子》及 Vue 3 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。

| 术语 | 释义 |
| --- | --- |
| 响应式 | ref 包装基本类型，reactive 包装对象；effect 收集依赖，Proxy 拦截读写；computed 缓存派生值。 |
| 组件通信 | props 向下、emit 向上、v-model 双向、provide/inject 跨层、事件总线（慎用）。 |
| 生命周期 | setup 在创建前执行；onMounted/onUpdated/onUnmounted 对应挂载、更新、卸载；KeepAlive 增加 activated/d |
| 模板编译 | 模板在构建期编译为渲染函数，指令（v-if/v-for/v-model）是编译糖。 |
| 响应式丢失（易错点） | 参见常见陷阱章节的详细讲解 |
| v-for key 用索引（易错点） | 参见常见陷阱章节的详细讲解 |
| props 直接修改（易错点） | 参见常见陷阱章节的详细讲解 |
| watch 深层（易错点） | 参见常见陷阱章节的详细讲解 |
| 组件样式泄漏（易错点） | 参见常见陷阱章节的详细讲解 |
| setup 中 async 误用（易错点） | 参见常见陷阱章节的详细讲解 |

术语表与正文配合使用：先通读正文，遇到模糊术语回查本表；长期使用后术语会自然进入工作记忆。
