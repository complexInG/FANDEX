---
order: 110
tags:
  - vue3
  - performance
difficulty: advanced
title: 性能优化
module: vue3
category: 'Vue3 Basics'
description: Vue3应用性能优化策略与实践
author: fanquanpp
updated: '2026-08-01'
related:
  - 'vue3/Vue-Router导航守卫'
  - vue3/Vue性能优化详解
  - vue3/高级组件特性
  - 'vue3/项目示例-个人博客站点'
prerequisites:
  - vue3/语法速查
---

## 1. 性能优化概述 | Performance Optimization Overview

Vue3 应用的性能优化是开发过程中的重要环节，它直接影响用户体验和应用的可扩展性。Vue3 本身已经做了很多性能优化，但在实际开发中，我们仍然需要注意一些性能问题，以确保应用的流畅运行。

### 1.1 性能优化的重要性

- **用户体验**：性能好的应用能够提供更流畅的交互体验
- **SEO 友好**：性能好的应用加载速度快，有利于搜索引擎优化
- **可扩展性**：性能好的应用能够更好地处理复杂的业务逻辑
- **服务器成本**：性能好的应用可以减少服务器的负载和成本

### 1.2 Vue3 的性能优势

- **虚拟 DOM 重写**：Vue3 的虚拟 DOM 实现更加高效
- **编译器优化**：Vue3 的编译器能够生成更高效的渲染代码
- **响应式系统优化**：Vue3 使用 Proxy 替代 Object.defineProperty，提供更高效的响应式能力
- **Tree-shaking**：Vue3 支持 Tree-shaking，减少了打包体积

## 2. 渲染性能优化 | Rendering Performance Optimization

### 2.1 使用 v-memo

`v-memo` 指令可以缓存计算结果，避免不必要的渲染：

```vue
<template>
  <div v-memo="[value]">
    {{ heavyComputation(value) }}
  </div>
</template>
<script setup>
import { ref } from 'vue';
const value = ref(0);
const heavyComputation = (value) => {
  // 模拟 heavy computation
  let result = 0;
  for (let i = 0; i < 1000000; i++) {
    result += i;
  }
  return result + value;
};
</script>
```

### 2.2 使用 v-once

`v-once` 指令可以让元素只渲染一次，适用于静态内容：

```vue
<template>
  <div v-once>
    {{ staticContent }}
  </div>
</template>
<script setup>
import { ref } from 'vue';
const staticContent = ref('This content will only be rendered once');
</script>
```

### 2.3 使用 keep-alive

`keep-alive` 组件可以缓存组件的状态，避免重复渲染：

```vue
<template>
  <keep-alive>
    <component :is="currentComponent"></component>
  </keep-alive>
</template>
<script setup>
import { ref } from 'vue';
import ComponentA from './ComponentA.vue';
import ComponentB from './ComponentB.vue';
const currentComponent = ref('ComponentA');
</script>
```

### 2.4 避免在模板中使用复杂表达式

在模板中使用复杂表达式会影响渲染性能，应该使用计算属性：

```vue
<template>
  <div>
    <!-- 不推荐 -->
    <p>
      {{
        users
          .filter((user) => user.age > 18)
          .map((user) => user.name)
          .join(', ')
      }}
    </p>
    <!-- 推荐 -->
    <p>{{ adultUserNames }}</p>
  </div>
</template>
<script setup>
import { ref, computed } from 'vue'
const users = ref([
 { name: 'John', age: 20 },
 { name: 'Jane', age: 17 },
 { name: 'Bob', age: 25 }
]
const adultUserNames = computed(() => {
 return users.value
 .filter(user => user.age > 18)
 .map(user => user.name)
 .join(', ')
}
</script>
```

### 2.5 使用虚拟滚动

对于大量数据的列表，使用虚拟滚动可以提高性能：

```vue
<template>
  <div class="list-container" style="height: 400px; overflow: auto;">
    <virtual-list
      :data-key="'id'"
      :data-sources="items"
      :data-component="'item'"
      :estimate-size="50"
    >
      <template v-slot:item="{ source }">
        <div class="item">
          {{ source.name }}
        </div>
      </template>
    </virtual-list>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import VirtualList from 'vue-virtual-scroller';
const items = ref(
  Array.from({ length: 10000 }, (_, i) => ({
    id: i,
    name: `Item ${i}`,
  }))
);
</script>
```

## 3. 响应式性能优化 | Reactive Performance Optimization

### 3.1 使用 shallowRef 和 shallowReactive

对于大型对象或不需要深度响应的数据，使用 `shallowRef` 和 `shallowReactive` 可以减少响应式开销：

```vue
<template>
  <div>
    <p>{{ user.name }}</p>
    <button @click="updateUser">Update User</button>
  </div>
</template>
<script setup>
import { shallowRef } from 'vue'
const user = shallowRef({
 name: 'John',
 age: 30,
 address: {
 street: '123 Main St',
 city: 'New York'
 }
}
const updateUser = () => {
 // 直接替换整个对象
 user.value = {
 name: 'Jane',
 age: 25,
 address: {
 street: '456 Elm St',
 city: 'Boston'
 }
 }
}
</script>
```

### 3.2 使用 markRaw

对于不需要响应式的数据，使用 `markRaw` 可以避免将其转换为响应式对象：

```vue
<template>
  <div>
    <p>{{ config.apiUrl }}</p>
  </div>
</template>
<script setup>
import { markRaw } from 'vue'
// 配置对象不需要响应式
const config = markRaw({
 apiUrl: 'https://api.example.com',
 timeout: 5000
}
</script>
```

### 3.3 合理使用 computed

计算属性会缓存计算结果，避免重复计算：

```vue
<template>
  <div>
    <p>Total: {{ total }}</p>
  </div>
</template>
<script setup>
import { ref, computed } from 'vue';
const items = ref([1, 2, 3, 4, 5]);
// 使用计算属性缓存计算结果
const total = computed(() => {
  console.log('Computing total...');
  return items.value.reduce((sum, item) => sum + item, 0);
});
</script>
```

### 3.4 避免频繁修改响应式数据

频繁修改响应式数据会触发多次渲染，应该批量修改：

```vue
<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Message: {{ message }}</p>
    <button @click="updateData">Update Data</button>
  </div>
</template>
<script setup>
import { ref } from 'vue';
const count = ref(0);
const message = ref('Hello');
// 批量修改数据，只触发一次渲染
const updateData = () => {
  count.value = 1;
  message.value = 'Hi';
};
</script>
```

## 4. 网络性能优化 | Network Performance Optimization

### 4.1 代码分割

使用动态导入实现代码分割，减少初始加载时间：

```vue
<template>
  <div>
    <button @click="loadComponent">Load Component</button>
    <component v-if="dynamicComponent" :is="dynamicComponent" />
  </div>
</template>
<script setup>
import { ref } from 'vue';
const dynamicComponent = ref(null);
const loadComponent = async () => {
  const { default: Component } = await import('./HeavyComponent.vue');
  dynamicComponent.value = Component;
};
</script>
```

### 4.2 资源预加载

使用 `rel="preload"` 预加载重要资源：

```html
<!-- 在 index.html 中 -->
<link rel="preload" href="/api/data" as="fetch" crossorigin />
<link rel="preload" href="/images/hero.jpg" as="image" />
```

### 4.3 缓存策略

使用 HTTP 缓存和本地缓存减少网络请求：

```vue
<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else>{{ data }}</div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue';
const data = ref(null);
const loading = ref(true);
onMounted(async () => {
  // 检查本地缓存
  const cachedData = localStorage.getItem('apiData');
  if (cachedData) {
    data.value = JSON.parse(cachedData);
    loading.value = false;
    return;
  }
  // 从服务器获取数据
  const response = await fetch('/api/data');
  const result = await response.json();
  data.value = result;
  loading.value = false;
  // 缓存数据
  localStorage.setItem('apiData', JSON.stringify(result));
});
</script>
```

### 4.4 减少 HTTP 请求

合并请求，减少 HTTP 请求数量：

```javascript
 // 不推荐
 fetch('/api/user')
 fetch('/api/posts')
 fetch('/api/comments')
 // 推荐
 fetch('/api/batch', {
  method: 'POST',
  body: JSON.stringify({
  requests: [
  { path: '/user' },
  { path: '/posts' },
  { path: '/comments' }
  ]
  })
 }
```

## 5. 构建优化 | Build Optimization

### 5.1 代码压缩

使用 Vite 或 Webpack 进行代码压缩：

```javascript
 // vite.config.js
 import { defineConfig } from 'vite'
 import vue from '@vitejs/plugin-vue'
 export default defineConfig({
  plugins: [vue()],
  build: {
  minify: 'terser',
  terserOptions: {
  compress: {
  drop_console: true,
  drop_debugger:
  }
  }
  }
 }
```

### 5.2 树摇 (Tree-shaking)

使用 ES 模块，利用 Tree-shaking 减少打包体积：

```javascript
// 不推荐
import * as lodash from 'lodash';
// 推荐
import { debounce, throttle } from 'lodash';
```

### 5.3 懒加载

使用动态导入实现组件和路由的懒加载：

```javascript
 // router/index.js
 import { createRouter, createWebHistory } from 'vue-router'
 const routes = [
  {
  path: '/',
  component: () => import('../views/Home.vue')
  },
  {
  path: '/about',
  component: () => import('../views/About.vue')
  }
 ]
 const router = createRouter({
  history: createWebHistory(),
  routes
 }
 export default router
```

### 5.4 资源优化

优化图片和其他静态资源：

- 使用适当的图片格式（WebP、AVIF）
- 压缩图片
- 使用 CDN 加速静态资源
- 配置浏览器缓存

## 6. 性能监控与分析 | Performance Monitoring and Analysis

### 6.1 使用 Vue DevTools

Vue DevTools 可以帮助你分析组件的渲染性能：

- **组件面板**：查看组件的状态和属性
- **性能面板**：分析组件的渲染时间
- **事件面板**：查看事件的触发和处理

### 6.2 使用浏览器开发者工具

浏览器开发者工具可以帮助你分析网络请求和页面性能：

- **Network 面板**：分析网络请求的时间和大小
- **Performance 面板**：分析页面的渲染性能
- **Memory 面板**：分析内存使用情况

### 6.3 使用第三方工具

使用第三方工具进行性能监控：

- **Lighthouse**：分析页面的性能、可访问性和 SEO
- **WebPageTest**：测试页面的加载性能
- **New Relic**：监控应用的性能和错误

## 7. 最佳实践 | Best Practices

### 7.1 组件设计

- **拆分组件**：将大型组件拆分为小型、可复用的组件
- **合理使用 props**：只传递必要的 props，避免过度传递
- **使用 slots**：使用 slots 提高组件的灵活性
- **避免过度使用 watch**：优先使用 computed

### 7.2 状态管理

- **合理使用状态管理**：只在必要时使用 Pinia 或 Vuex
- **避免过度使用全局状态**：优先使用组件级状态
- **使用模块化**：将状态管理按功能模块划分

### 7.3 代码组织

- **合理组织代码**：按功能和模块组织代码
- **使用 TypeScript**：提高代码的可维护性和类型安全性
- **遵循代码规范**：使用 ESLint 和 Prettier 保持代码风格一致

### 7.4 性能预算

- **设置性能预算**：为应用的加载时间、资源大小等设置预算
- **监控性能指标**：定期监控应用的性能指标
- **持续优化**：不断优化应用的性能

## 8. 示例 | Examples

### 8.1 优化前

```vue
<template>
  <div>
    <h2>User List</h2>
    <ul>
      <li v-for="user in users" :key="user.id">
        <div>
          <h3>{{ user.name }}</h3>
          <p>{{ user.email }}</p>
          <p>{{ formatDate(user.createdAt) }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>
<script setup>
import { ref } from 'vue';
const users = ref(
  Array.from({ length: 1000 }, (_, i) => ({
    id: i,
    name: `User ${i}`,
    email: `user${i}@example.com`,
    createdAt: new Date(),
  }))
);
const formatDate = (date) => {
  return date.toLocaleString();
};
</script>
```

### 8.2 优化后

```vue
<template>
  <div>
    <h2>User List</h2>
    <ul>
      <li v-for="user in users" :key="user.id">
        <div>
          <h3>{{ user.name }}</h3>
          <p>{{ user.email }}</p>
          <p>{{ user.formattedCreatedAt }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>
<script setup>
import { ref, computed } from 'vue';
const users = ref(
  Array.from({ length: 1000 }, (_, i) => ({
    id: i,
    name: `User ${i}`,
    email: `user${i}@example.com`,
    createdAt: new Date(),
    formattedCreatedAt: new Date().toLocaleString(),
  }))
);
</script>
```

## 9. 小结 | Summary

Vue3 应用的性能优化是一个持续的过程，需要从多个方面入手，包括渲染性能、响应式性能、网络性能和构建优化等。通过本章节的学习，你已经了解了 Vue3 应用性能优化的基本方法和最佳实践。
在实际开发中，要根据应用的具体情况，选择合适的优化策略，同时要定期监控应用的性能，不断优化和改进。只有这样，才能构建出性能优异、用户体验良好的 Vue3 应用。

## 参考文献

Vue 官方文档：https://vuejs.org/
Vue Router：https://router.vuejs.org/zh/
Pinia：https://pinia.vuejs.org/zh/
Vue 3 迁移指南：https://v3-migration.vuejs.org/
VueUse 组合函数库：https://vueuse.org/

## 延伸阅读

Vue Teleport 与 Portal，见 010-vue3/026-TeleportPortalApp 文档。
Vue KeepAlive 缓存，见 010-vue3/027-KeepAliveCacheLifecycle 文档。
Vue Router 导航守卫，见 010-vue3/030-VueRouterNavigationGuard 文档。
TypeScript 与 Vue 组合，见 009-typescript 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Vue3 课程。

## 模块文档速查表

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
| 生命周期钩子 | 012-LifecycleHook | 本文的并列主题 |
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
| 性能优化 | 032-PerformanceOptimization | 本文自身 |
| Vue3 高级组件特性 | 033-Vue3AdvancedComponentFeature | 本文的并列主题 |
| Vue3 项目示例：个人博客站点 | 034-Vue3ProjectExampleBlog | 本文的综合应用 |
| Vue3 理论知识点 | 035-Vue3TheoryKnowledge | 本文的并列主题 |
| Vue 3 Vite 构建配置与命令 | 036-Vue3ViteBuildConfig | 本文的并列主题 |
| Vue 3.4 / 3.5 新特性 | 037-Vue3NewFeatures3435 | 本文的并列主题 |
