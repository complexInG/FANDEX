---
order: 310
title: Vue性能优化详解
module: 'vue3'
category: 前端技术
difficulty: advanced
description: Vue 3性能优化详解：虚拟滚动、shallowRef、冻结数据、v-memo。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'vue3/029-PiniaPersistencePlugin'
  - 'vue3/030-VueRouterNavigationGuard'
  - 'vue3/032-PerformanceOptimization'
  - 'vue3/033-Vue3AdvancedComponentFeature'
prerequisites: []
---


## 1. 响应式优化

### 1.1 shallowRef

```javascript
// 大型对象不需要深层响应式
const bigData = shallowRef(loadHugeDataset());
// 只有 .value 赋值才触发更新
bigData.value = newData; // 触发
bigData.value.items.push(x); // 不触发
```

### 1.2 shallowReactive

```javascript
const state = shallowReactive({
  items: [], // 不是响应式的
  count: 0, // 是响应式的（根级属性）
});
```

### 1.3 markRaw

```javascript
const staticData = markRaw(largeObject);
// 永远不会转为响应式
```

### 1.4 Object.freeze

```javascript
const frozenList = Object.freeze(hugeArray);
const items = ref(frozenList); // 跳过深层响应式转换
```

## 2. 渲染优化

### 2.1 v-memo

```html
<div v-for="item in list" :key="item.id" v-memo="[item.selected]">
  <!-- 仅 item.selected 变化时重新渲染 -->
  <ExpensiveComponent :data="item" />
</div>
```

### 2.2 v-once

```html
<h1 v-once>{{ title }}</h1>
<!-- 只渲染一次，后续更新跳过 -->
```

### 2.3 虚拟滚动

```html
<template v-for="item in visibleItems" :key="item.id">
  <div :style="{ transform: `translateY(${offset}px)` }">{{ item.content }}</div>
</template>
```

推荐库：`vue-virtual-scroller`、`vue3-virtual-scroll-list`

## 3. 组件优化

### 3.1 异步组件

```javascript
const HeavyChart = defineAsyncComponent(() => import('./HeavyChart.vue'));
```

### 3.2 KeepAlive

```html
<KeepAlive :include="['UserList', 'Settings']">
  <RouterView />
</KeepAlive>
```

## 4. 编译优化

Vue 3 编译器自动优化：

- 静态提升（Static Hoisting）
- 补丁标记（Patch Flags）
- 块级树（Block Tree）
- 静态属性提升

## 延伸阅读
Vue Teleport 与 Portal，见 010-vue3/026-TeleportPortalApp 文档。
Vue KeepAlive 缓存，见 010-vue3/027-KeepAliveCacheLifecycle 文档。
Vue Router 导航守卫，见 010-vue3/030-VueRouterNavigationGuard 文档。
TypeScript 与 Vue 组合，见 009-typescript 模块。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 响应式原理与依赖收集

ref 内部用 class RefImpl 保存值并收集依赖；reactive 用 Proxy 的 get/set 拦截，依赖以 WeakMap<target, Map<key, Set<effect>>> 存储。
effect 在触发时重新执行，scheduler 控制批处理（微任务队列）；computed 用惰性求值与缓存标志。
渲染更新：组件渲染函数是 effect，数据变化触发重渲染；Vue 的更新粒度到组件级，配合虚拟 DOM diff。
调试：onRenderTracked/onRenderTriggered 追踪依赖；性能面板观察更新频率。

### 13.2 组合函数与可复用逻辑

组合函数（composable）以 use 前缀命名，内部可组合 ref/computed/watch/lifecycle，实现逻辑复用。
示例：useFetch 封装请求状态（data/error/loading）与取消；useLocalStorage 同步持久化。
与 Mixin 对比：组合函数无命名冲突、显式依赖、类型友好。
工程规范：每个组合函数单一职责，返回只读引用防止外部破坏。
