---
order: 20
tags:
  - vue3
difficulty: beginner
title: 'Vue3 快速入门指南'
module: vue3
category: 'Vue3 Basics'
description: '从零搭建 Vue3 项目、开发工具与核心概念速览。'
author: fanquanpp
updated: '2026-08-01'
related:
  - vue3/语法速查
  - vue3/概述与环境
  - vue3/模板语法
  - vue3/指令系统
prerequisites: []
---

## 1. 环境搭建

### 1.1 安装 Node.js

Vue3 项目需要 Node.js 环境，推荐安装最新的 LTS 版本：

- 访问 [Node.js 官网](https://nodejs.org/)
- 下载并安装适合你操作系统的 LTS 版本
- 安装完成后，在终端运行以下命令验证：

```bash
 node -v
 npm -v
```

### 1.2 安装 Vue CLI 或 Vite

#### 使用 Vite（推荐）

Vite 是 Vue 官方推荐的构建工具，速度更快：

```bash
 # 安装 create-vite@latest
 npm create vite@latest
 # 按照提示创建 Vue3 项目
 # 选择 Vue + TypeScript 模板获取最佳开发体验
```

#### 使用 Vue CLI

```bash
 # 安装 Vue CLI
 npm install -g @vue/cli
 # 创建 Vue3 项目
 Vue create my-vue3-project
 # 选择 Vue 3 预设
```

## 2. 项目结构

一个典型的 Vue3 项目结构如下：

```mermaid
flowchart TD
    T0["my-vue3-project/"]
    T1["public/"]
    T2["favicon.ico"]
    T3["src/"]
    T4["assets/"]
    T5["logo.png"]
    T6["components/"]
    T7["HelloWorld.vue"]
    T8["router/"]
    T9["index.ts"]
    T10["store/"]
    T11["index.ts"]
    T12["views/"]
    T13["Home.vue"]
    T14["About.vue"]
    T15["App.vue"]
    T16["main.ts"]
    T17[".gitignore"]
    T18["index.html"]
    T19["package.json"]
    T20["tsconfig.json"]
    T21["vite.config.ts"]
    T22["README.md"]
    T0 --> T1
    T2 --> T3
    T16 --> T17
    T16 --> T18
    T16 --> T19
    T16 --> T20
    T16 --> T21
    T16 --> T22
```

## 3. 第一个 Vue3 应用

### 3.1 基本组件结构

创建一个简单的 Vue3 组件：

```vue
<template>
  <div class="hello">
    <h1>{{ message }}</h1>
    <button @click="count++">点击计数: {{ count }}</button>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue';
const message = ref('Hello Vue3!');
const count = ref(0);
</script>
<style scoped>
.hello {
  text-align: center;
  margin-top: 2rem;
}
</style>
```

### 3.2 运行项目

```bash
 # 进入项目目录
 cd my-vue3-project
 # 安装依赖
 npm install
 # 启动开发服务器
 npm run dev
```

## 4. 核心概念快速了解

### 4.1 组合式 API

```vue
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
// 响应式数据
const count = ref(0);
// 计算属性
const doubleCount = computed(() => count.value * 2);
// 生命周期钩子
onMounted(() => {
  console.log('组件挂载完成');
});
// 方法
function increment() {
  count.value++;
}
</script>
```

### 4.2 响应式系统

```vue
<script setup lang="ts">
import { ref, reactive, toRefs } from 'vue'
// 基本类型响应式
const count = ref(0)
// 对象响应式
const user = reactive({
 name: '张三',
 age: 20
}
// 解构响应式对象
const { name, age } = toRefs(user)
</script>
```

### 4.3 组件通信

#### 父传子（Props）

```vue
<!-- 父组件 -->
<template>
  <ChildComponent :message="parentMessage" />
</template>
<script setup lang="ts">
import ChildComponent from './ChildComponent.vue';
import { ref } from 'vue';
const parentMessage = ref('来自父组件的消息');
</script>
```

```vue
<!-- 子组件 -->
<template>
  <div>{{ message }}</div>
</template>
<script setup lang="ts">
defineProps<{
  message: string;
  ;
}>();
</script>
```

#### 子传父（Emits）

```vue
<!-- 子组件 -->
<template>
  <button @click="emit('update', '来自子组件的消息')">发送消息</button>
</template>
<script setup lang="ts">
const emit = defineEmits<{
  (e: 'update', message: string): void;
  ;
}>();
</script>
```

```vue
<!-- 父组件 -->
<template>
  <ChildComponent @update="handleUpdate" />
  <div>{{ childMessage }}</div>
</template>
<script setup lang="ts">
import ChildComponent from './ChildComponent.vue';
import { ref } from 'vue';
const childMessage = ref('');
function handleUpdate(message: string) {
  childMessage.value = message;
}
</script>
```

## 5. 路由与状态管理

### 5.1 Vue Router

安装：

```bash
 npm install vue-router@4
```

基本配置：

```ts
 // router/index.ts
 import { createRouter, createWebHistory } from 'vue-router'
 import Home from '../views/Home.vue'
 const routes = [
  {
  path: '/',
  name: 'Home',
  component: Home
  },
  {
  path: '/about',
  name: 'About',
  component: () => import('../views/About.vue')
  }
 ]
 const router = createRouter({
  history: createWebHistory(),
  routes
 }
 export default router
```

### 5.2 Pinia 状态管理

安装：

```bash
 npm install pinia
```

基本配置：

```ts
 // store/index.ts
 import { defineStore } from 'pinia'
 export const useCounterStore = defineStore('counter', {
  state: () => ({
  count: 0
  }),
  actions: {
  increment() {
  this.count++
  }
  },
  getters: {
  doubleCount: (state) => state.count * 2
  }
 }
```

使用：

```vue
<script setup lang="ts">
import { useCounterStore } from '../store';
const counterStore = useCounterStore();
</script>
<template>
  <div>
    <p>Count: {{ counterStore.count }}</p>
    <p>Double: {{ counterStore.doubleCount }}</p>
    <button @click="counterStore.increment">Increment</button>
  </div>
</template>
```

## 6. 构建与部署

### 6.1 构建生产版本

```bash
 npm run build
```

构建产物会生成在 `dist` 目录中。

### 6.2 部署选项

- **静态网站托管**：GitHub Pages、Vercel、Netlify 等
- **服务器部署**：Nginx、Apache 等
- **容器化部署**：Docker

## 7. 学习资源

- [Vue3 官方文档](https://v3.vuejs.org/)
- [Vue 3 教程 - 中文](https://cn.vuejs.org/)
- [Vite 官方文档](https://vitejs.dev/)
- [Vue Router 官方文档](https://router.vuejs.org/)
- [Pinia 官方文档](https://pinia.vuejs.org/)

## 8. 快速开发提示

1. **使用 TypeScript**：提供类型安全，减少运行时错误
2. **使用 ESLint 和 Prettier**：保持代码风格一致
3. **使用 Volar**：Vue3 官方推荐的 VS Code 扩展
4. **组件拆分**：将复杂组件拆分为更小的、可复用的组件
5. **使用 composables**：提取可复用的逻辑
6. **性能优化**：使用 `v-memo`、`v-once` 等指令优化渲染性能
   通过本快速入门指南，你已经了解了 Vue3 的基本使用方法。接下来可以深入学习各个核心概念和高级特性。

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与环境 | 001-OverviewEnv | 本文的前置基础 |
| Vue3 快速入门指南 | 002-Vue3QuickStartGuide | 本文自身 |
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
| 性能优化 | 032-PerformanceOptimization | 本文的性能延伸 |
| Vue3 高级组件特性 | 033-Vue3AdvancedComponentFeature | 本文的并列主题 |
| Vue3 项目示例：个人博客站点 | 034-Vue3ProjectExampleBlog | 本文的综合应用 |
| Vue3 理论知识点 | 035-Vue3TheoryKnowledge | 本文的并列主题 |
| Vue 3 Vite 构建配置与命令 | 036-Vue3ViteBuildConfig | 本文的并列主题 |
| Vue 3.4 / 3.5 新特性 | 037-Vue3NewFeatures3435 | 本文的并列主题 |
