---
order: 100
title: computed缓存机制与watch执行时机
module: vue3
category: 'dev-lang'
difficulty: advanced
description: 'Vue 3 computed缓存机制与watch执行时机详解。'
author: fanquanpp
updated: '2026-08-01'
related:
  - vue3/Pinia状态管理详解
  - vue3/插件开发
  - vue3/Router详解
  - vue3/组合式API优势场景
prerequisites:
  - vue3/语法速查
---

# computed + watch API 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. computed 缓存机制

### 1.1 惰性求值

computed 只有在被读取时才会计算，且缓存结果：

```javascript
const count = ref(0);
const doubled = computed(() => {
  console.log('computed 执行');
  return count.value * 2;
});

// 首次读取：执行计算
console.log(doubled.value); // computed 执行 → 0

// 再次读取：返回缓存
console.log(doubled.value); // 无日志 → 0（缓存）

// 依赖变化
count.value = 1;
// 此时不会重新计算！computed 是惰性的

// 再次读取：重新计算
console.log(doubled.value); // computed 执行 → 2
```

### 1.2 脏标记机制

Vue 3 使用脏标记（dirty flag）实现缓存：

```
初始状态: dirty = true
首次读取: 执行计算 → dirty = false → 缓存结果
依赖变化: dirty = true → 不立即重新计算
再次读取: dirty === true → 重新计算 → dirty = false
```

### 1.3 computed vs methods

| 特性     | computed | methods  |
| -------- | -------- | -------- |
| 缓存     | 有       | 无       |
| 响应式   | 是       | 否       |
| 调用方式 | 属性访问 | 函数调用 |
| 副作用   | 不应有   | 可以有   |

## 2. watch 执行时机

### 2.1 默认行为

```javascript
const count = ref(0);

watch(
  count,
  (newVal, oldVal) => {
    console.log('watch 触发:', newVal);
  },
  { flush: 'pre' }
); // 默认值

count.value = 1;
console.log('同步代码');
// 输出顺序: 同步代码 → watch 触发: 1
```

### 2.2 flush 选项

| flush 值 | 执行时机           | 用途               |
| -------- | ------------------ | ------------------ |
| `pre`    | DOM 更新前（默认） | 修改其他响应式数据 |
| `post`   | DOM 更新后         | 访问更新后的 DOM   |
| `sync`   | 同步执行           | 调试（性能差）     |

```javascript
watch(
  count,
  (newVal) => {
    // pre: DOM 还未更新
  },
  { flush: 'pre' }
);

watch(
  count,
  (newVal) => {
    // post: DOM 已更新，可安全访问
    document.getElementById('counter').textContent;
  },
  { flush: 'post' }
);
```

### 2.3 immediate 选项

```javascript
watch(
  source,
  (newVal, oldVal) => {
    // 创建时立即执行一次
  },
  { immediate: true }
);
```

### 2.4 deep 选项

```javascript
const state = reactive({ nested: { count: 0 } });

watch(
  state,
  (newVal) => {
    // 深层变化也会触发
  },
  { deep: true }
);

// Vue 3.4+ watch 自动深层监听 reactive 对象
```

## 3. watchEffect

```javascript
// 自动追踪依赖
watchEffect(() => {
  console.log(count.value); // 自动追踪 count
});

// 与 watch 的区别
// watchEffect: 自动追踪、立即执行、无旧值
// watch: 显式指定、惰性执行、有旧值
```

## 4. 停止侦听器

```javascript
const stop = watch(source, callback);

// 组件卸载时自动停止
// 手动停止
stop();
```
## computed 计算属性

**computed 只读**
`const <result> = computed(() => <expression>);`
```typescript
import { ref, computed } from 'vue';
const count = ref(1);

const double = computed(() => count.value * 2);
const fullName = computed(() => `${firstName.value} ${lastName.value}`);
console.log(double.value);  // 2
```

**computed 可写**
`const <result> = computed({ get, set });`
```typescript
const firstName = ref('John');
const lastName = ref('Doe');

const fullName = computed({
  get() {
    return `${firstName.value} ${lastName.value}`;
  },
  set(newValue) {
    [firstName.value, lastName.value] = newValue.split(' ');
  }
});

fullName.value = 'Tom Smith';
```

**computed 缓存特性**
```typescript
const count = ref(0);
const expensive = computed(() => {
  console.log('computing...');
  return count.value * 2;
});

console.log(expensive.value);  // computing... 0
console.log(expensive.value);  // 0(使用缓存,不重新计算)
count.value = 1;
console.log(expensive.value);  // computing... 2
```

**computed 与 reactive 配合**
```typescript
import { reactive, computed } from 'vue';
const state = reactive({
  items: [
    { id: 1, name: 'A', price: 10 },
    { id: 2, name: 'B', price: 20 }
  ]
});

const total = computed(() =>
  state.items.reduce((sum, item) => sum + item.price, 0)
);

const expensiveItems = computed(() =>
  state.items.filter(item => item.price > 15)
);
```

---

## watch 侦听器

**watch 单源侦听**
`watch(<source>, (<newVal>, [oldVal], [onCleanup]) => {}, [options]);`
```typescript
import { ref, watch } from 'vue';
const count = ref(0);

watch(count, (newVal, oldVal) => {
  console.log(`从 ${oldVal} 变为 ${newVal}`);
});
```

**watch getter 侦听**
`watch(() => <expression>, <callback>);`
```typescript
const state = reactive({ user: { name: 'Tom' } });

watch(
  () => state.user.name,
  (newVal, oldVal) => {
    console.log('name 变化:', oldVal, '->', newVal);
  }
);
```

**watch 多源侦听**
`watch([<source1>, <source2>], ([<new1>, <new2>], [<old1>, <old2>]) => {});`
```typescript
import { ref, watch } from 'vue';
const foo = ref('a');
const bar = ref(1);

watch([foo, bar], ([newFoo, newBar], [oldFoo, oldBar]) => {
  console.log('foo:', oldFoo, '->', newFoo);
  console.log('bar:', oldBar, '->', newBar);
});
```

**watch 选项配置**
```typescript
watch(count, callback, {
  immediate: true,    // 立即执行一次
  deep: true,         // 深度侦听
  flush: 'post',      // 'pre'(默认) | 'post' | 'sync'
  once: true          // 只触发一次(Vue 3.4+)
});
```

**watch 深度侦听**
```typescript
import { reactive, watch } from 'vue';
const state = reactive({
  user: { name: 'Tom', address: { city: 'Beijing' } }
});

watch(
  () => state.user,
  (newVal, oldVal) => {
    console.log('user 变化');
  },
  { deep: true }
);
```

**watch 清理副作用**
```typescript
watch(id, (newId, oldId, onCleanup) => {
  const controller = new AbortController();
  fetch(`/api/data/${newId}`, { signal: controller.signal })
    .then(res => res.json())
    .then(data => {
      console.log(data);
    });

  onCleanup(() => {
    controller.abort();  // 取消上次未完成的请求
  });
});
```

---

## watchEffect 自动追踪

**watchEffect 基础**
`watchEffect(<effect> => {});`
```typescript
import { ref, watchEffect } from 'vue';
const count = ref(0);

watchEffect(() => {
  console.log('count:', count.value);  // 自动追踪 count
});

count.value++;  // 触发 effect 重新执行
```

**watchEffect 立即执行**
```typescript
watchEffect(() => {
  // 立即执行一次,然后追踪依赖变化
  console.log('initial + reactive:', count.value);
});
```

**watchEffect 清理副作用**
```typescript
watchEffect((onCleanup) => {
  const timer = setInterval(() => {
    console.log(count.value);
  }, 1000);

  onCleanup(() => {
    clearInterval(timer);
  });
});
```

**watchEffect 返回值**
```typescript
const stop = watchEffect(() => {
  console.log(count.value);
});

// 主动停止侦听
stop();
```

**watchEffect 调试信息(Vue 3.4+)**
```typescript
watchEffect(onTrack, onTrigger => {}, {
  onTrack(event) { console.log('追踪:', event); },
  onTrigger(event) { console.log('触发:', event); }
});
```

---

## watchPostEffect / watchSyncEffect

**watchPostEffect DOM 更新后执行**
`watchPostEffect(<effect>);`
```typescript
import { ref, watchPostEffect } from 'vue';
const list = ref<number[]>([]);

watchPostEffect(() => {
  // DOM 已更新,可读取最新 DOM 尺寸
  const el = document.getElementById('list');
  console.log(el?.scrollHeight);
});
```

**watchSyncEffect 同步执行**
`watchSyncEffect(<effect>);`
```typescript
import { ref, watchSyncEffect } from 'vue';
const count = ref(0);

watchSyncEffect(() => {
  // 状态变更后同步执行(无队列延迟)
  console.log('sync:', count.value);
});
```

---

## watch vs watchEffect

**watch 显式依赖**
```typescript
const count = ref(0);
const name = ref('Tom');

// 只侦听 count,name 变化不影响
watch(count, (newVal) => {
  console.log('count:', newVal, 'name:', name.value);
});
```

**watchEffect 自动追踪**
```typescript
const count = ref(0);
const name = ref('Tom');

// 自动追踪 count 和 name
watchEffect(() => {
  console.log('count:', count.value, 'name:', name.value);
});
```

---

## 调试钩子

**onTrack 依赖追踪时触发**
```typescript
watch(count, callback, {
  onTrack(event) {
    // effect 触发时首次追踪依赖
    console.log('tracked:', event);
    // event: { effect, target, key, type }
  }
});
```

**onTrigger 依赖触发时调用**
```typescript
watch(count, callback, {
  onTrigger(event) {
    // 依赖变化导致回调执行时
    console.log('triggered:', event);
    // event: { effect, target, key, type, newValue, oldValue }
  }
});
```

---

## 综合应用

**computed + watch 组合**
```typescript
import { ref, computed, watch } from 'vue';

const items = ref<{ id: number; price: number }[]>([]);
const totalPrice = computed(() =>
  items.value.reduce((sum, item) => sum + item.price, 0)
);

watch(totalPrice, (newTotal, oldTotal) => {
  console.log(`总价变化:${oldTotal} -> ${newTotal}`);
});

watch(
  () => items.value.length,
  (newLen) => {
    console.log(`商品数量:${newLen}`);
  }
);
```

**watch + 副作用清理**
```typescript
function useFetchData(url: Ref<string>) {
  const data = ref(null);
  const error = ref(null);

  watch(url, async (newUrl, _, onCleanup) => {
    data.value = null;
    error.value = null;

    const controller = new AbortController();
    onCleanup(() => controller.abort());

    try {
      const res = await fetch(newUrl, { signal: controller.signal });
      data.value = await res.json();
    } catch (e) {
      if (e.name !== 'AbortError') {
        error.value = e;
      }
    }
  }, { immediate: true });

  return { data, error };
}
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
| computed缓存机制与watch执行时机 | 022-ComputedCacheWatchTiming | 本文自身 |
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
