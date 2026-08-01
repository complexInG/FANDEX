---
order: 101
title: 组合式API优势场景
module: vue3
category: 'dev-lang'
difficulty: advanced
description: 'Vue 3组合式API vs 选项式API对比与优势场景分析。'
author: fanquanpp
updated: '2026-08-01'
related:
  - vue3/computed缓存机制与watch执行时机
  - vue3/Router详解
  - vue3/自定义组合函数封装
  - vue3/Teleport传送门应用
prerequisites:
  - vue3/语法速查
---

# Vue 3 组合式 API 与 Pinia 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 两种 API 对比

### 1.1 选项式 API

```javascript
export default {
  data() {
    return { count: 0, user: null };
  },
  computed: {
    doubled() {
      return this.count * 2;
    },
  },
  methods: {
    increment() {
      this.count++;
    },
  },
  mounted() {
    this.fetchUser();
  },
};
```

### 1.2 组合式 API

```javascript
export default {
  setup() {
    const count = ref(0);
    const user = ref(null);
    const doubled = computed(() => count.value * 2);
    const increment = () => count.value++;
    onMounted(() => fetchUser());
    return { count, user, doubled, increment };
  },
};
```

## 2. 组合式 API 优势

### 2.1 逻辑复用

```javascript
// 可复用的鼠标位置逻辑
function useMouse() {
  const x = ref(0);
  const y = ref(0);
  const update = (e) => {
    x.value = e.clientX;
    y.value = e.clientY;
  };
  onMounted(() => window.addEventListener('mousemove', update));
  onUnmounted(() => window.removeEventListener('mousemove', update));
  return { x, y };
}

// 在任何组件中使用
const { x, y } = useMouse();
```

### 2.2 逻辑关注点聚合

选项式 API 中，同一功能的代码分散在 data/methods/computed 中；组合式 API 中，相关代码聚合在一起。

### 2.3 更好的类型推导

```typescript
// 组合式 API：自动类型推导
const count = ref(0); // Ref<number>
const name = ref(''); // Ref<string>

// 选项式 API：需要额外声明
```

## 3. 适用场景

| 场景            | 推荐 API   |
| --------------- | ---------- |
| 简单组件        | 选项式 API |
| 逻辑复用        | 组合式 API |
| TypeScript 项目 | 组合式 API |
| 大型项目        | 组合式 API |
| 快速原型        | 选项式 API |
## 组合式 API

**基本写法：ref 响应式引用**
`const <变量> = ref(<初始值>);`
```typescript
// 创建响应式引用
import { ref } from 'vue';
const count = ref(0);
count.value++;
```

---

**基本写法：reactive 对象响应式**
`const <变量> = reactive(<对象>);`
```typescript
// 创建响应式对象
import { reactive } from 'vue';
const state = reactive({ count: 0, name: 'Vue' });
state.count++;
```

---

**基本写法：computed 计算属性**
`const <变量> = computed(() => <表达式>);`
```typescript
// 只读计算属性
import { computed } from 'vue';
const double = computed(() => count.value * 2);
// 可写计算属性
const fullName = computed({
    get: () => `${first.value} ${last.value}`,
    set: (v) => { [first.value, last.value] = v.split(' '); }
});
```

---

**基本写法：watch 监听**
`watch(<源>, (<新值>, <旧值>) => { }, { <选项> });`
```typescript
// 监听 ref
import { watch } from 'vue';
watch(count, (newVal, oldVal) => {
    console.log(`${oldVal} -> ${newVal}`);
}, { immediate: true, deep: false });
```

---

**基本写法：watchEffect 副作用监听**
`watchEffect(() => <表达式>);`
```typescript
// 自动追踪依赖
import { watchEffect } from 'vue';
watchEffect(() => {
    console.log(count.value);
});
```

---

**基本写法：生命周期钩子**
`on<名称>(() => { });`
```typescript
// 组件挂载后
import { onMounted, onUnmounted } from 'vue';
onMounted(() => { console.log('mounted'); });
onUnmounted(() => { cleanup(); });
```

---

## 组件定义

**基本写法：defineComponent 定义组件**
`defineComponent({ <选项> });`
```typescript
// 定义组件
import { defineComponent } from 'vue';
export default defineComponent({
    props: { msg: String },
    setup(props) {
        return { greeting: `Hello ${props.msg}` };
    }
});
```

---

**基本写法：script setup 单文件组件**
```vue
<script setup lang="ts">
import { ref } from 'vue';
const count = ref(0);
const increment = () => count.value++;
</script>
```

---

**基本写法：defineProps 定义 props**
`const props = defineProps<{ <属性>: <类型> }>();`
```typescript
// TypeScript 类型声明
const props = defineProps<{
    msg: string;
    count?: number;
}>();
```

---

**基本写法：defineEmits 定义事件**
`const emit = defineEmits<{ <事件>: [<参数>] }>();`
```typescript
// 定义事件
const emit = defineEmits<{
    change: [value: string];
    submit: [];
}>();
emit('change', 'new');
```

---

**基本写法：defineExpose 暴露方法**
`defineExpose({ <方法> });`
```typescript
// 暴露给父组件
defineExpose({ increment });
```

---

## 自定义组合函数

**基本写法：useXxx 模式**
`function use<名称>(<参数>) { return { <返回值> }; }`
```typescript
// 自定义 Hook
import { ref, onMounted } from 'vue';
function useMouse() {
    const x = ref(0);
    const y = ref(0);
    const update = (e: MouseEvent) => { x.value = e.x; y.value = e.y; };
    onMounted(() => window.addEventListener('mousemove', update));
    onUnmounted(() => window.removeEventListener('mousemove', update));
    return { x, y };
}
```

---

## Pinia 状态管理

**基本写法：defineStore 定义 Store**
`const use<Store> = defineStore('<名称>', { <选项> });`
```typescript
// Options 写法
import { defineStore } from 'pinia';
export const useCounterStore = defineStore('counter', {
    state: () => ({ count: 0 }),
    getters: { double: (state) => state.count * 2 },
    actions: { increment() { this.count++; } }
});
```

---

**基本写法：Setup Store**
`const use<Store> = defineStore('<名称>', () => { return { }; });`
```typescript
// Composition 写法
import { ref, computed } from 'vue';
export const useCounter = defineStore('counter', () => {
    const count = ref(0);
    const double = computed(() => count.value * 2);
    function increment() { count.value++; }
    return { count, double, increment };
});
```

---

**基本写法：使用 Store**
`const <store> = use<Store>();`
```typescript
// 在组件中使用
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore();
store.count;
store.increment();
```

---

**基本写法：storeToRefs 解构**
`const { <字段> } = storeToRefs(<store>);`
```typescript
// 保持响应式的解构
import { storeToRefs } from 'pinia';
const store = useCounterStore();
const { count } = storeToRefs(store);
```

---

**基本写法：订阅状态变化**
`<store>.$subscribe((<state>, <payload>) => { });`
```typescript
// 监听状态变化
store.$subscribe((state, payload) => {
    localStorage.setItem('counter', JSON.stringify(state));
});
```

---

## 依赖注入

**基本写法：provide 提供依赖**
`provide(<键>, <值>);`
```typescript
// 父组件提供
import { provide, ref } from 'vue';
const theme = ref('dark');
provide('theme', theme);
```

---

**基本写法：inject 注入依赖**
`const <变量> = inject(<键> [, <默认值>]);`
```typescript
// 子组件注入
import { inject } from 'vue';
const theme = inject('theme', 'light');
```

---

## Teleport 与 Suspense

**基本写法：Teleport 传送**
`<Teleport to="<选择器>"><内容></Teleport>`
```vue
<template>
<Teleport to="body">
    <div class="modal">Modal Content</div>
</Teleport>
</template>
```

---

**基本写法：Suspense 异步组件**
`<Suspense><template #default><异步组件/></template><template #fallback><加载中/></template></Suspense>`
```vue
<template>
<Suspense>
    <template #default>
        <AsyncComponent />
    </template>
    <template #fallback>
        <div>Loading...</div>
    </template>
</Suspense>
</template>
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
| 组合式API优势场景 | 024-CompositionAPIAdvantageScene | 本文自身 |
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
