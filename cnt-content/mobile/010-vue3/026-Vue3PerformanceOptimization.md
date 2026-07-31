# Vue 3 性能优化实践

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 列表 key 优化

**基本写法：为 v-for 提供稳定 key**
`<div v-for="<项> in <列表>" :key="<项>.id">`
```vue
<!-- 使用业务 id 而非 index -->
<div v-for="item in list" :key="item.id">{{ item.name }}</div>
```

---

## v-show 与 v-if 选择

**基本写法：频繁切换用 v-show**
`<div v-show="<可见>">`
```vue
<!-- 仅切换 display 频繁切换成本低 -->
<div v-show="open">面板</div>
```

---

**基本写法：条件少变用 v-if**
`<div v-if="<条件>">`
```vue
<!-- 真正销毁与创建 不常用更省内存 -->
<div v-if="loaded">内容</div>
```

---

## 计算属性缓存

**基本写法：用 computed 替代方法**
`const <c> = computed(() => <计算>)`
```ts
// 缓存结果避免重复计算
const total = computed(() => items.value.reduce((s, i) => s + i.price, 0));
```

---

## shallowRef 大型数据

**基本写法：大对象用 shallowRef**
`const <data> = shallowRef(<大对象>)`
```ts
// 跳过深层代理提升性能
const bigList = shallowRef({ items: hugeArray });
bigList.value = { items: newHugeArray };
```

---

## markRaw 第三方实例

**基本写法：标记不被代理**
`const <raw> = markRaw(<对象>)`
```ts
// 避免代理第三方库实例
const chart = markRaw(echarts.init(dom));
```

---

## 异步组件懒加载

**基本写法：defineAsyncComponent 按需加载**
`const <comp> = defineAsyncComponent(() => import('<路径>'))`
```ts
// 路由级或重组件懒加载
const Heavy = defineAsyncComponent(() => import('./Heavy.vue'));
```

---

**基本写法：配置加载与错误组件**
`defineAsyncComponent({ loader, loadingComponent, errorComponent })`
```ts
// 提升用户体验
const Async = defineAsyncComponent({
  loader: () => import('./Heavy.vue'),
  loadingComponent: Loading,
  errorComponent: Error
});
```

---

## KeepAlive 缓存组件

**基本写法：缓存切换的组件实例**
`<keep-alive> <组件 /> </keep-alive>`
```vue
<!-- 保留状态避免重新创建 -->
<keep-alive>
  <component :is="currentTab" />
</keep-alive>
```

---

**基本写法：限定缓存**
`<keep-alive include="<组件名>">`
```vue
<!-- 仅缓存指定组件 -->
<keep-alive include="User,Order">
  <component :is="current" />
</keep-alive>
```

---

**基本写法：缓存数量限制**
`<keep-alive :max="<数量>">`
```vue
<!-- 限制缓存实例数 -->
<keep-alive :max="10">
  <component :is="current" />
</keep-alive>
```

---

## v-once 一次性渲染

**基本写法：静态内容只渲染一次**
`<div v-once>{{ <静态值> }}</div>`
```vue
<!-- 提升后续更新性能 -->
<header v-once>{{ title }}</header>
```

---

## v-memo 选择性更新

**基本写法：依赖未变跳过更新**
`<div v-memo="[<依赖1>, <依赖2>]">`
```vue
<!-- 依赖数组不变时跳过 patch -->
<div v-memo="[item.id, item.selected]">
  {{ item.name }}
</div>
```

---

## 虚拟列表长列表

**基本写法：使用虚拟滚动**
`<VirtualList :data="<大列表>" :item-size="<高度>" />`
```ts
// 借助 vue-virtual-scroller
import { RecycleScroller } from 'vue-virtual-scroller';
<RecycleScroller :items="items" :item-size="40">
  <template #default="{ item }">{{ item.name }}</template>
</RecycleScroller>
```

---

## 事件防抖节流

**基本写法：搜索输入防抖**
`const <debounced> = useDebounceFn(<fn>, <延迟>)`
```ts
// 借助 VueUse
import { useDebounceFn } from '@vueuse/core';
const onSearch = useDebounceFn(search, 300);
```

---

## 图片懒加载

**基本写法：使用 v-lazy 或原生 loading**
`<img loading="lazy" />`
```vue
<!-- 原生懒加载 -->
<img src="/a.jpg" loading="lazy" />
```

---

**基本写法：IntersectionObserver 自定义**
`const { <isVisible> } = useIntersectionObserver(<ref>)`
```ts
// VueUse 提供组合式函数
import { useIntersectionObserver } from '@vueuse/core';
const target = ref(null);
const { stop } = useIntersectionObserver(target, ([{ isIntersecting }]) => {
  if (isIntersecting) load();
});
```

---

## 组件拆分

**基本写法：将重型组件拆分为子组件**
`function <HeavyChild>() {}`
```vue
<!-- 拆分后细粒度更新 -->
<script setup>
import HeavyChild from './HeavyChild.vue';
</script>
<template><HeavyChild :data="data" /></template>
```

---

## 依赖未变避免更新

**基本写法：使用 computed 衍生数据**
`const <derived> = computed(() => <原始>.filter(<条件>))`
```ts
// 原始未变时复用衍生
const active = computed(() => list.value.filter(i => i.active));
```

---

## Pinia 优化

**基本写法：按需订阅 store**
`const <字段> = storeToRefs(<store>)`
```ts
// 只订阅需要的字段
const { count } = storeToRefs(counterStore);
```

---

## 路由懒加载

**基本写法：路由组件动态导入**
`component: () => import('<路径>')`
```ts
// 路由配置懒加载
const routes = [
  { path: '/user', component: () => import('./User.vue') }
];
```

---

## 避免深层响应

**基本写法：大对象用 shallowReactive**
`const <state> = shallowReactive(<大对象>)`
```ts
// 仅根属性响应减少代理开销
const state = shallowReactive({ config: hugeConfig });
```

---

## CSS 优化

**基本写法：使用 scoped 隔离样式**
`<style scoped>`
```vue
<!-- 避免全局污染 -->
<style scoped>
.title { color: red; }
</style>
```

---

## v-for 与 v-if 优先级

**基本写法：避免同时使用 v-for 与 v-if**
`<div v-for="x in list" v-if="x.show"> // 不推荐`
```vue
<!-- 推荐用 computed 过滤 -->
<div v-for="x in filteredList">{{ x.name }}</div>
```

---

## 静态资源压缩

**基本写法：构建时压缩图片**
`vite-plugin-imagemin`
```bash
# 安装图片压缩插件
npm install -D vite-plugin-imagemin
```

---

## 包体积分析

**基本写法：分析打包体积**
`rollup-plugin-visualizer`
```bash
# 可视化依赖体积
npm install -D rollup-plugin-visualizer
```

---

## tree shaking 按需引入

**基本写法：按需导入工具函数**
`import { <函数> } from '<库>'`
```ts
// 仅打包使用部分
import { debounce } from 'lodash-es';
```

---

## SSR 优化首屏

**基本写法：服务端渲染提升首屏**
`renderToString(<app>)`
```ts
// 首屏直出 HTML 利于 SEO
const html = await renderToString(app);
```

---

## 性能分析

**基本写法：Vue DevTools 性能面板**
`npm run dev`
```bash
# 浏览器扩展分析组件渲染耗时
# 安装 Vue DevTools 扩展
```

---

## defineModel 优化双向绑定

**基本写法：Vue 3.4+ 简化 v-model**
`const <model> = defineModel()`
```vue
<!-- 替代手动 props 与 emits -->
<script setup>
const model = defineModel();
</script>
<template><input v-model="model" /></template>
```

---

## 编译优化提示

**基本写法：静态提升与补丁标记**
`<div class="static">静态</div>`
```vue
<!-- 编译器自动提升静态节点 -->
<div class="static">静态内容</div>
```

---

## 减少响应式开销

**基本写法：基础值用 ref 对象用 reactive**
`const <n> = ref(0); const <obj> = reactive({})`
```ts
// 根据类型选择合适 API
const count = ref(0);
const state = reactive({ list: [] });
```
