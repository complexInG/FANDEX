# Vue 3 SSR 与同构渲染

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SSR 基本流程

**基本写法：renderToString 渲染为字符串**
`const <html> = await renderToString(<App>)`
```ts
// 服务器渲染组件为 HTML
import { renderToString } from 'vue/server-renderer';
import { createSSRApp } from 'vue';
const app = createSSRApp(App);
const html = await renderToString(app);
```

---

**基本写法：createSSRApp 创建应用**
`const <app> = createSSRApp(<根组件>)`
```ts
// SSR 模式应用实例
const app = createSSRApp(App);
```

---

## renderToNodeStream 流式渲染

**基本写法：Node 流式输出**
`renderToNodeStream(<app>)`
```ts
// 边渲染边发送提升首屏
import { renderToNodeStream } from 'vue/server-renderer';
const stream = renderToNodeStream(app);
stream.pipe(res);
```

---

**基本写法：Web Stream 边缘环境**
`renderToWebStream(<app>)`
```ts
// Cloudflare Workers 等环境
import { renderToWebStream } from 'vue/server-renderer';
const stream = renderToWebStream(app);
```

---

## 客户端注水 hydrate

**基本写法：客户端 mount 注水**
`<app>.mount(<容器>)`
```ts
// 客户端复用服务端 HTML
import { createSSRApp } from 'vue';
const app = createSSRApp(App);
app.mount('#app');
```

---

## 入口文件分离

**基本写法：entry-server.js 导出 render**
`export async function render() { return await renderToString(<app>); }`
```ts
// 服务端入口
import { createSSRApp } from 'vue';
import App from './App.vue';
export async function render(url) {
  const app = createSSRApp(App);
  return await renderToString(app);
}
```

---

**基本写法：entry-client.js 注水**
`<app>.mount('#app')`
```ts
// 客户端入口
import { createSSRApp } from 'vue';
import App from './App.vue';
createSSRApp(App).mount('#app');
```

---

## 同构路由

**基本写法：createRouter 共享配置**
`const <router> = createRouter({ history, routes })`
```ts
// 客户端使用 createWebHistory 服务端使用 createMemoryHistory
import { createRouter } from 'vue-router';
const router = createRouter({
  history: isServer ? createMemoryHistory() : createWebHistory(),
  routes
});
```

---

**基本写法：服务端 router.push**
`<router>.push(<url>)`
```ts
// 服务端根据请求 URL 设置
router.push(ctx.url);
await router.isReady();
```

---

## 数据预取

**基本写法：组件内 serverPrefetch 钩子**
`async serverPrefetch() { await <fetch>; }`
```vue
<!-- 组件级数据预取 -->
<script>
export default {
  async serverPrefetch() {
    this.posts = await fetchPosts();
  }
}
</script>
```

---

**基本写法：路由级数据预取**
`<route>.meta.<preload>`
```ts
// 路由 meta 配置预取函数
{ path: '/user/:id', component: User, meta: { preload: fetchUser } }
```

---

## 注水数据传递

**基本写法：服务端数据序列化注入**
`<script>window.__INITIAL_STATE__ = ${JSON.stringify(<state>)}</script>`
```ts
// 通过全局变量传递初始状态
const state = serialize(state);
const html = `<script>window.__INITIAL_STATE__=${state}</script>`;
```

---

**基本写法：客户端读取注水状态**
`window.__INITIAL_STATE__`
```ts
// 客户端恢复状态
if (window.__INITIAL_STATE__) {
  store.replaceState(window.__INITIAL_STATE__);
}
```

---

## Pinia SSR 集成

**基本写法：服务端创建 Pinia**
`const <pinia> = createPinia()`
```ts
// 每请求独立实例
import { createPinia } from 'pinia';
const pinia = createPinia();
app.use(pinia);
```

---

**基本写法：序列化 Pinia 状态**
`pinia.state.value`
```ts
// 注水时传递
const state = JSON.stringify(pinia.state.value);
```

---

**基本写法：客户端恢复 Pinia**
`<pinia>.state.value = window.__INITIAL_STATE__`
```ts
// 客户端注水
pinia.state.value = window.__INITIAL_STATE__;
```

---

## 注水不匹配

**基本写法：避免服务端客户端渲染差异**
`const <date> = new Date() // 时间不一致`
```ts
// 使用 onMounted 在客户端修正
const date = ref('');
onMounted(() => date.value = new Date().toLocaleString());
```

---

## Nuxt 3 全栈框架

**基本写法：创建 Nuxt 项目**
`npx nuxi init <项目名>`
```bash
# 创建 Nuxt 3 项目
npx nuxi init my-app
```

---

**基本写法：开发命令**
`npm run dev`
```bash
# 启动 Nuxt 开发服务器
npm run dev
```

---

**基本写法：构建命令**
`npm run build`
```bash
# 构建生产版本
npm run build
```

---

**基本写法：启动生产服务**
`node .output/server/index.mjs`
```bash
# 运行 Nuxt 生产服务
node .output/server/index.mjs
```

---

## Nuxt 页面路由

**基本写法：pages 目录约定**
`pages/index.vue`
```vue
<!-- 自动生成 / 路由 -->
<template>
  <h1>首页</h1>
</template>
```

---

**基本写法：动态路由**
`pages/user/[id].vue`
```vue
<!-- 自动生成 /user/:id -->
<script setup>
const route = useRoute();
const id = route.params.id;
</script>
```

---

## Nuxt 数据获取

**基本写法：useFetch 获取数据**
`const { <data> } = await useFetch('<url>')`
```ts
// 自动 SSR 同构
const { data } = await useFetch('/api/user');
```

---

**基本写法：useAsyncData 自定义获取**
`const { <data> } = await useAsyncData('<key>', () => <fn>)`
```ts
// 自定义异步逻辑
const { data } = await useAsyncData('user', () => fetchUser());
```

---

## Nuxt 中间件

**基本写法：路由中间件**
`middleware/auth.ts`
```ts
// 全局路由中间件
export default defineNuxtRouteMiddleware((to, from) => {
  if (!isAuth()) return navigateTo('/login');
});
```

---

## Nuxt 插件

**基本写法：自定义插件**
`plugins/<名称>.ts`
```ts
// 注册全局功能
export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.provide('util', () => console.log('util'));
});
```

---

## Nuxt 服务端 API

**基本写法：server/api 目录约定**
`server/api/user.get.ts`
```ts
// 自动映射 /api/user
export default defineEventHandler(async (event) => {
  return { name: 'Alice' };
});
```

---

## Nuxt 渲染模式

**基本写法：配置渲染模式**
`ssr: true | false`
```ts
// nuxt.config.ts
export default defineNuxtConfig({
  ssr: true // 启用 SSR 默认 true
});
```

---

**基本写法：混合渲染路由规则**
`routeRules: { '<路径>': { ssr: false } }`
```ts
// 部分路由 SPA 模式
routeRules: {
  '/admin/**': { ssr: false }
}
```

---

## Nuxt 静态生成

**基本写法：预渲染静态站点**
`nuxt generate`
```bash
# 生成纯静态 HTML
npm run generate
```

---

## 元信息管理

**基本写法：useHead 设置文档头**
`useHead({ title, meta })`
```ts
// 同构管理 head
useHead({
  title: '我的页面',
  meta: [{ name: 'description', content: '描述' }]
});
```

---

## 错误处理

**基本写法：createError 抛错**
`throw createError({ statusCode: 404 })`
```ts
// 服务端与客户端统一错误
throw createError({ statusCode: 404, statusMessage: 'Not Found' });
```

---

**基本写法：error.vue 错误页**
`error.vue`
```vue
<!-- 全局错误页 -->
<script setup>
const props = defineProps(['error']);
</script>
<template>
  <h1>{{ error.statusCode }}</h1>
</template>
```
