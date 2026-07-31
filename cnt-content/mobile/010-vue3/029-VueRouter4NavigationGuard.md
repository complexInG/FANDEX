# Vue Router 4 导航守卫进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 全局前置守卫

**基本写法：beforeEach 注册全局前置守卫**
`router.beforeEach((<to>, <from>, <next>) => <逻辑>)`
```ts
// 每次导航前执行
router.beforeEach((to, from, next) => {
  if (to.meta.auth && !isLogin()) next('/login');
  else next();
});
```

---

**基本写法：返回值控制导航**
`router.beforeEach((<to>, <from>) => <目标> | false | undefined)`
```ts
// 返回路径或 false 取消导航
router.beforeEach((to) => {
  if (to.meta.auth && !isLogin()) return '/login';
});
```

---

**基本写法：抛出错误取消导航**
`throw new Error(<消息>)`
```ts
// 抛错中断导航
router.beforeEach(() => {
  throw new Error('禁止访问');
});
```

---

## 全局解析守卫

**基本写法：beforeResolve 在组件解析后执行**
`router.beforeResolve((<to>, <from>) => <逻辑>)`
```ts
// 所有组件与守卫完成后执行
router.beforeResolve(async (to) => {
  await trackPageView(to.path);
});
```

---

## 全局后置钩子

**基本写法：afterEach 导航完成后执行**
`router.afterEach((<to>, <from>) => <逻辑>)`
```ts
// 不影响导航仅做副作用
router.afterEach((to) => {
  document.title = to.meta.title || '默认';
});
```

---

**基本写法：处理失败导航**
`router.afterEach((<to>, <from>, <failure>) => <逻辑>)`
```ts
// 检测导航失败
router.afterEach((to, from, failure) => {
  if (failure) logError(failure);
});
```

---

## 路由独享守卫

**基本写法：beforeEnter 路由配置级守卫**
`{ path, beforeEnter: (<to>, <from>) => <逻辑> }`
```ts
// 仅对该路由生效
const routes = [{
  path: '/admin',
  beforeEnter: (to, from) => {
    if (!isAdmin()) return '/403';
  }
}];
```

---

**基本写法：beforeEnter 数组**
`beforeEnter: [<guard1>, <guard2>]`
```ts
// 多个守卫按顺序执行
{ path: '/x', beforeEnter: [checkAuth, checkRole] }
```

---

## 组件内守卫

**基本写法：beforeRouteEnter 进入前**
`beforeRouteEnter(<to>, <from>, <next>)`
```vue
<!-- 组件内守卫 -->
<script>
export default {
  beforeRouteEnter(to, from, next) {
    next(vm => vm.loadData());
  }
}
</script>
```

---

**基本写法：beforeRouteUpdate 复用时**
`beforeRouteUpdate(<to>, <from>, <next>)`
```vue
<!-- 动态参数变化复用组件 -->
<script>
export default {
  beforeRouteUpdate(to, from, next) {
    this.id = to.params.id;
    next();
  }
}
</script>
```

---

**基本写法：beforeRouteLeave 离开前**
`beforeRouteLeave(<to>, <from>, <next>)`
```vue
<!-- 阻止未保存的离开 -->
<script>
export default {
  beforeRouteLeave(to, from, next) {
    if (this.unsaved) {
      if (confirm('确定离开?')) next();
      else next(false);
    } else next();
  }
}
</script>
```

---

## 组合式 API 守卫

**基本写法：onBeforeRouteLeave**
`onBeforeRouteLeave((<to>, <from>) => <逻辑>)`
```vue
<!-- script setup 中使用 -->
<script setup>
import { onBeforeRouteLeave } from 'vue-router';
onBeforeRouteLeave((to, from) => {
  if (unsaved.value) return confirm('离开?');
});
</script>
```

---

**基本写法：onBeforeRouteUpdate**
`onBeforeRouteUpdate((<to>, <from>) => <逻辑>)`
```vue
<!-- 动态参数变化时触发 -->
<script setup>
import { onBeforeRouteUpdate } from 'vue-router';
onBeforeRouteUpdate(async (to) => {
  await loadData(to.params.id);
});
</script>
```

---

## 守卫执行顺序

**基本写法：完整导航解析流程**
`beforeEach -> beforeEnter -> beforeRouteEnter -> beforeResolve -> afterEach`
```ts
// 守卫按顺序执行
// 1. 全局 beforeEach
// 2. 路由 beforeEnter
// 3. 组件 beforeRouteEnter
// 4. 全局 beforeResolve
// 5. 全局 afterEach
```

---

## 元信息 meta

**基本写法：路由 meta 配置**
`{ path, meta: { <字段>: <值> } }`
```ts
// 守卫中读取 meta
const routes = [{
  path: '/admin',
  meta: { requiresAuth: true, title: '管理' }
}];
```

---

**基本写法：合并父子路由 meta**
`to.matched.reduce((<meta>, <r>) => ({ ...<meta>, ...<r>.meta }), {})`
```ts
// 父子 meta 合并
const meta = to.matched.reduce((acc, r) => ({ ...acc, ...r.meta }), {});
```

---

## 异步守卫

**基本写法：返回 Promise**
`router.beforeEach(async (<to>, <from>) => <异步>)`
```ts
// 异步验证权限
router.beforeEach(async (to) => {
  const user = await fetchUser();
  if (to.meta.admin && !user.isAdmin) return '/403';
});
```

---

**基本写法：next 配合 Promise**
`router.beforeEach((<to>, <from>, <next>) => <异步>().then(<next>))`
```ts
// 异步逻辑后调用 next
router.beforeEach((to, from, next) => {
  fetchUser().then(user => {
    if (user) next();
    else next('/login');
  });
});
```

---

## 守卫注入依赖

**基本写法：通过函数返回守卫**
`function createAuthGuard(<store>) { return (<to>, <from>) => <逻辑>; }`
```ts
// 注入 store 等依赖
function createAuthGuard(store) {
  return (to) => {
    if (to.meta.auth && !store.user) return '/login';
  };
}
router.beforeEach(createAuthGuard(pinia));
```

---

## 移除守卫

**基本写法：beforeEach 返回的函数移除守卫**
`const <remove> = router.beforeEach(<guard>); <remove>()`
```ts
// 动态移除守卫
const remove = router.beforeEach(guard);
remove();
```

---

## 导航失败处理

**基本写法：捕获导航失败**
`router.push('<路径>').catch(<err>)`
```ts
// 处理重定向或取消
router.push('/admin').catch(err => {
  if (err.name === 'NavigationAborted') console.warn('取消');
});
```

---

**基本写法：NavigationFailure 类型**
`<failure>.type`
```ts
// 判断失败类型
import { NavigationFailureType } from 'vue-router';
if (failure.type === NavigationFailureType.aborted) /* 中止 */;
```

---

## 滚动行为

**基本写法：scrollBehavior 控制滚动**
`scrollBehavior(<to>, <from>, <savedPosition>)`
```ts
// 切换路由时控制滚动位置
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 };
  }
});
```

---

**基本写法：滚动到锚点**
`if (<to>.hash) return { el: <to>.hash }`
```ts
// 锚点定位
scrollBehavior(to) {
  if (to.hash) return { el: to.hash, behavior: 'smooth' };
  return { top: 0 };
}
```

---

## 动态路由

**基本写法：addRoute 动态添加路由**
`router.addRoute({ path, component })`
```ts
// 运行时添加路由
router.addRoute({ path: '/new', component: NewPage });
```

---

**基本写法：addRoute 父子嵌套**
`router.addRoute('<父名>', { path, component })`
```ts
// 添加到指定父路由下
router.addRoute('admin', { path: 'settings', component: Settings });
```

---

**基本写法：removeRoute 移除路由**
`router.removeRoute('<名称>')`
```ts
// 通过名称移除
router.removeRoute('admin');
```

---

## 路由懒加载与守卫

**基本写法：懒加载组件配合守卫**
`component: () => import('<路径>')`
```ts
// 守卫触发后再加载组件
{ path: '/user', component: () => import('./User.vue'), meta: { auth: true } }
```

---

## 过渡动画

**基本写法：路由过渡动画**
`<router-view v-slot="{ Component }">`
```vue
<!-- 配合 transition -->
<router-view v-slot="{ Component }">
  <transition name="fade">
    <component :is="Component" />
  </transition>
</router-view>
```

---

## 检测导航类型

**基本写法：判断初始导航**
`<from>.matched.length === 0`
```ts
// 首次进入应用
router.beforeEach((to, from) => {
  if (from.matched.length === 0) console.log('初始导航');
});
```

---

## 守卫性能优化

**基本写法：避免每个守卫重复请求**
`let <cached> = null`
```ts
// 缓存用户信息
let cachedUser = null;
router.beforeEach(async (to) => {
  if (!cachedUser) cachedUser = await fetchUser();
  if (to.meta.auth && !cachedUser) return '/login';
});
```
