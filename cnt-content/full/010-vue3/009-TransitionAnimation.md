---
order: 53
title: Transition与动画
module: vue3
category: Vue3
difficulty: intermediate
description: Vue3过渡与动画系统
author: fanquanpp
updated: '2026-08-01'
related:
  - vue3/Provide与Inject
  - vue3/自定义指令进阶
  - vue3/Vue3编译优化
  - vue3/Vue3服务端渲染
prerequisites:
  - vue3/语法速查
---

# Transition + TransitionGroup 组件语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. Transition 组件

```vue
<template>
  <Transition name="fade">
    <div v-if="show">内容</div>
  </Transition>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
```

## 2. 过渡类名

| 类名             | 说明         |
| ---------------- | ------------ |
| `v-enter-from`   | 进入起始状态 |
| `v-enter-active` | 进入生效状态 |
| `v-enter-to`     | 进入结束状态 |
| `v-leave-from`   | 离开起始状态 |
| `v-leave-active` | 离开生效状态 |
| `v-leave-to`     | 离开结束状态 |

## 3. JavaScript 钩子

```vue
<Transition
  @before-enter="onBeforeEnter"
  @enter="onEnter"
  @after-enter="onAfterEnter"
  @before-leave="onBeforeLeave"
  @leave="onLeave"
  @after-leave="onAfterLeave"
>
  <div v-if="show">内容</div>
</Transition>
```

## 4. TransitionGroup

```vue
<TransitionGroup name="list" tag="ul">
  <li v-for="item in items" :key="item.id">{{ item.text }}</li>
</TransitionGroup>

<style>
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
.list-leave-active {
  position: absolute;
}
</style>
```

## 5. 自定义过渡

```vue
<Transition
  :duration="{ enter: 500, leave: 300 }"
  enter-active-class="animate__animated animate__fadeIn"
  leave-active-class="animate__animated animate__fadeOut"
>
  <div v-if="show">内容</div>
</Transition>
```
## Transition 单元素过渡

**Transition 基础用法**
```vue
<template>
  <button @click="show = !show">切换</button>
  <Transition name="fade">
    <p v-if="show">Hello</p>
  </Transition>
</template>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>

<script setup>
import { ref } from 'vue';
const show = ref(true);
</script>
```

**Transition 类名约定**
```css
.<name>-enter-from { /* 进入起点 */ }
.<name>-enter-active { /* 进入过程 */ }
.<name>-enter-to { /* 进入终点 */ }
.<name>-leave-from { /* 离开起点 */ }
.<name>-leave-active { /* 离开过程 */ }
.<name>-leave-to { /* 离开终点 */ }
```

**Transition 自定义类名**
```vue
<Transition
  enter-from-class="custom-enter-from"
  enter-active-class="custom-enter-active"
  enter-to-class="custom-enter-to"
  leave-from-class="custom-leave-from"
  leave-active-class="custom-leave-active"
  leave-to-class="custom-leave-to"
>
  <div v-if="show">content</div>
</Transition>
```

---

## Transition Props

**name 与 appear**
`<Transition name="<name>" appear>`
```vue
<Transition name="fade" appear>
  <p v-if="show">初次渲染也会执行动画</p>
</Transition>
```

**type 与 duration**
`<Transition type="<transition|animation>" :duration="<ms>">`
```vue
<Transition type="transition" :duration="1000">
  <div v-if="show">content</div>
</Transition>

<Transition :duration="{ enter: 500, leave: 800 }">
  <div v-if="show">content</div>
</Transition>
```

**mode 过渡模式**
`<Transition mode="<out-in|in-out>">`
```vue
<!-- 先离开再进入 -->
<Transition mode="out-in">
  <component :is="currentComp" />
</Transition>

<!-- 同时进行(默认) -->
<Transition>
  <div :key="current">content</div>
</Transition>
```

---

## Transition 钩子

**JavaScript 钩子**
```vue
<Transition
  @before-enter="beforeEnter"
  @enter="enter"
  @after-enter="afterEnter"
  @enter-cancelled="enterCancelled"
  @before-leave="beforeLeave"
  @leave="leave"
  @after-leave="afterLeave"
  @leave-cancelled="leaveCancelled"
>
  <div v-if="show">content</div>
</Transition>

<script setup>
function beforeEnter(el) {
  el.style.opacity = 0;
}
function enter(el, done) {
  // 调用 done 表示动画完成
  el.offsetHeight;  // 触发重排
  el.style.transition = 'opacity 0.5s';
  el.style.opacity = 1;
  el.addEventListener('transitionend', done);
}
function afterEnter(el) {
  console.log('enter 完成');
}
function leave(el, done) {
  el.style.opacity = 0;
  el.addEventListener('transitionend', done);
}
</script>
```

**CSS 与 JS 钩子组合**
```vue
<Transition
  name="fade"
  @enter="onEnter"
  :css="false"
>
  <div v-if="show">content</div>
</Transition>

<script setup>
function onEnter(el, done) {
  // :css="false" 跳过 CSS 类名规则,完全用 JS 控制
  gsap.to(el, { opacity: 1, duration: 0.5, onComplete: done });
}
</script>
```

---

## TransitionGroup 列表过渡

**TransitionGroup 基础**
```vue
<template>
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">{{ item.name }}</li>
  </TransitionGroup>
</template>

<style>
.list-enter-active, .list-leave-active {
  transition: all 0.5s;
}
.list-enter-from, .list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
.list-move {
  transition: transform 0.5s;
}
</style>
```

**TransitionGroup Props**
```vue
<TransitionGroup
  name="list"
  tag="ul"
  appear
  :css="true"
>
  <li v-for="item in items" :key="item.id">{{ item.name }}</li>
</TransitionGroup>
```

**移动动画**
```vue
<TransitionGroup name="list" tag="ul">
  <li v-for="item in items" :key="item.id">{{ item.name }}</li>
</TransitionGroup>

<style>
.list-move {
  transition: transform 0.5s ease;
}
.list-enter-active, .list-leave-active {
  transition: all 0.5s ease;
}
.list-leave-active {
  position: absolute;  /* 离开时脱离文档流,触发 move 动画 */
}
</style>
```

**TransitionGroup 钩子**
```vue
<TransitionGroup
  tag="ul"
  @before-enter="onBeforeEnter"
  @enter="onEnter"
  @leave="onLeave"
  @before-leave="onBeforeLeave"
>
  <li v-for="item in items" :key="item.id">{{ item.name }}</li>
</TransitionGroup>
```

---

## 动画集成

**CSS animation 动画**
```vue
<Transition name="bounce">
  <p v-if="show">Bounce!</p>
</Transition>

<style>
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% { transform: scale(0); }
  50% { transform: scale(1.25); }
  100% { transform: scale(1); }
}
</style>
```

**GSAP 集成**
```vue
<script setup>
import { ref } from 'vue';
import gsap from 'gsap';

const show = ref(true);

function onEnter(el, done) {
  gsap.fromTo(el,
    { opacity: 0, y: 30 },
    { opacity: 1, y: 0, duration: 0.5, onComplete: done }
  );
}

function onLeave(el, done) {
  gsap.to(el, {
    opacity: 0, y: -30, duration: 0.5, onComplete: done
  });
}
</script>

<template>
  <Transition :css="false" @enter="onEnter" @leave="onLeave">
    <p v-if="show">Animated</p>
  </Transition>
</template>
```

---

## 综合应用

**列表删除/添加/排序动画**
```vue
<script setup>
import { ref, reactive } from 'vue';
const items = ref([
  { id: 1, name: 'A' },
  { id: 2, name: 'B' },
  { id: 3, name: 'C' }
]);
let nextId = 4;

function add() {
  items.value.push({ id: nextId++, name: String.fromCharCode(64 + nextId) });
}
function remove(index) {
  items.value.splice(index, 1);
}
function shuffle() {
  items.value = items.value.sort(() => Math.random() - 0.5);
}
</script>

<template>
  <button @click="add">添加</button>
  <button @click="shuffle">随机排序</button>
  <TransitionGroup name="list" tag="ul">
    <li v-for="(item, index) in items" :key="item.id">
      {{ item.name }}
      <button @click="remove(index)">删除</button>
    </li>
  </TransitionGroup>
</template>

<style>
.list-enter-active, .list-leave-active, .list-move {
  transition: all 0.5s ease;
}
.list-enter-from, .list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
.list-leave-active {
  position: absolute;
}
</style>
```

**Transition + 动态组件**
```vue
<template>
  <button @click="toggle">切换</button>
  <Transition name="fade" mode="out-in">
    <component :is="currentComp" />
  </Transition>
</template>

<script setup>
import { ref, computed, shallowRef } from 'vue';
import CompA from './CompA.vue';
import CompB from './CompB.vue';

const isA = ref(true);
const currentComp = computed(() => isA.value ? CompA : CompB);
const toggle = () => { isA.value = !isA.value; };
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
```

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
| Vue3 快速入门指南 | 002-Vue3QuickStartGuide | 本文的前置基础 |
| Vue3 模板语法 | 003-Vue3TemplateSyntax | 本文的并列主题 |
| Vue3 指令系统 | 004-Vue3DirectiveSystem | 本文的并列主题 |
| Teleport与Suspense | 005-TeleportSuspense | 本文的并列主题 |
| 组合式 API | 006-API | 本文的并列主题 |
| Provide与Inject | 007-ProvideInject | 本文的并列主题 |
| 自定义指令进阶 | 008-CustomDirectiveAdvanced | 本文的并列主题 |
| Transition与动画 | 009-TransitionAnimation | 本文自身 |
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
