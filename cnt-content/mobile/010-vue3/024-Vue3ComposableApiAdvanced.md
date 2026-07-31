# Vue 3 组合式 API 进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## shallowRef 浅响应引用

**基本写法：仅 .value 替换触发更新**
`const <ref> = shallowRef(<对象>)`
```ts
// 适合大型不可变结构
const data = shallowRef({ items: [] });
data.value = { items: newArray }; // 触发
data.value.items.push(1); // 不触发
```

---

## triggerRef 强制触发更新

**基本写法：修改 shallowRef 内部后手动触发**
`triggerRef(<shallowRef>)`
```ts
// 浅响应下深度修改后通知
const state = shallowRef({ count: 0 });
state.value.count++;
triggerRef(state);
```

---

## shallowReactive 浅响应对象

**基本写法：仅根属性响应**
`const <state> = shallowReactive(<对象>)`
```ts
// 性能优化避免深层代理
const state = shallowReactive({ foo: 1, nested: { bar: 2 } });
state.foo++; // 响应
state.nested.bar++; // 不响应
```

---

## customRef 自定义 ref

**基本写法：自定义依赖追踪与触发**
`const <ref> = customRef((<track>, <trigger>) => ({ get, set }))`
```ts
// 实现防抖 ref
function useDebouncedRef(value, delay = 200) {
  let timeout;
  return customRef((track, trigger) => ({
    get() { track(); return value; },
    set(newValue) {
      clearTimeout(timeout);
      timeout = setTimeout(() => { value = newValue; trigger(); }, delay);
    }
  }));
}
```

---

## readonly 只读代理

**基本写法：创建只读响应式对象**
`const <ro> = readonly(<reactive对象>)`
```ts
// 防止误修改
const original = reactive({ count: 0 });
const ro = readonly(original);
```

---

## shallowReadonly 浅只读

**基本写法：仅根属性只读**
`const <ro> = shallowReadonly(<对象>)`
```ts
// 根属性只读嵌套可改
const state = shallowReadonly({ foo: 1, nested: { bar: 2 } });
state.foo = 2; // 警告
state.nested.bar = 3; // 允许
```

---

## computed 计算属性

**基本写法：只读计算属性**
`const <c> = computed(() => <计算>)`
```ts
// 自动缓存依赖未变不重算
const double = computed(() => count.value * 2);
```

---

**基本写法：可写计算属性**
`const <c> = computed({ get, set })`
```ts
// 提供 get 与 set
const fullName = computed({
  get: () => `${first.value} ${last.value}`,
  set: (v) => { [first.value, last.value] = v.split(' '); }
});
```

---

**基本写法：调试钩子**
`computed(() => <计算>, { onTrack, onTrigger })`
```ts
// 开发期调试依赖
const c = computed(() => state.count * 2, {
  onTrack(e) { console.log('tracked', e); },
  onTrigger(e) { console.log('triggered', e); }
});
```

---

## watch 侦听器

**基本写法：侦听 ref**
`watch(<ref>, (<new>, <old>) => <逻辑>)`
```ts
// 监听 ref 变化
watch(count, (newVal, oldVal) => console.log(newVal));
```

---

**基本写法：侦听 getter 函数**
`watch(() => <reactive.字段>, <回调>)`
```ts
// 监听 reactive 属性
watch(() => state.count, (n, o) => console.log(n));
```

---

**基本写法：侦听多个源**
`watch([<源1>, <源2>], ([n1, n2]) => <逻辑>)`
```ts
// 同时监听多个源
watch([count, () => state.name], ([n, name]) => console.log(n, name));
```

---

**基本写法：deep 深度监听**
`watch(<源>, <回调>, { deep: true })`
```ts
// 对象深层变化触发
watch(state, (n) => console.log(n), { deep: true });
```

---

**基本写法：immediate 立即执行**
`watch(<源>, <回调>, { immediate: true })`
```ts
// 创建时立即执行一次
watch(count, (n) => init(n), { immediate: true });
```

---

**基本写法：flush 调整时机**
`watch(<源>, <回调>, { flush: 'post' })`
```ts
// post 在 DOM 更新后执行 pre 在更新前
watch(count, cb, { flush: 'post' });
```

---

**基本写法：once 仅触发一次**
`watch(<源>, <回调>, { once: true })`
```ts
// Vue 3.5 新增只监听一次
watch(count, (n) => console.log(n), { once: true });
```

---

**基本写法：暂停恢复监听**
`const { pause, resume } = watch(<源>, <回调>)`
```ts
// Vue 3.5 新增手动控制
const { pause, resume } = watch(count, cb);
pause();
resume();
```

---

## watchEffect 副作用

**基本写法：自动收集依赖**
`watchEffect(() => <副作用>)`
```ts
// 自动追踪内部响应式依赖
watchEffect(() => console.log(state.count));
```

---

**基本写法：清理副作用**
`watchEffect((<onCleanup>) => <逻辑>)`
```ts
// 在重新执行前清理
watchEffect((onCleanup) => {
  const timer = setInterval(tick, 1000);
  onCleanup(() => clearInterval(timer));
});
```

---

**基本写法：调整执行时机**
`watchEffect(() => <副作用>, { flush: 'post' })`
```ts
// pre 默认 post 在 DOM 后 sync 同步
watchEffect(() => updateDOM(), { flush: 'post' });
```

---

## watchPostEffect

**基本写法：post 模式的 watchEffect 简写**
`watchPostEffect(() => <副作用>)`
```ts
// 等价 flush: 'post'
watchPostEffect(() => console.log('DOM 更新后'));
```

---

## watchSyncEffect

**基本写法：同步模式的 watchEffect 简写**
`watchSyncEffect(() => <副作用>)`
```ts
// 等价 flush: 'sync'
watchSyncEffect(() => console.log('同步执行'));
```

---

## toRef 与 toRefs

**基本写法：toRef 单属性转 ref**
`const <ref> = toRef(<reactive>, '<字段>')`
```ts
// 保持响应式关联
const countRef = toRef(state, 'count');
```

---

**基本写法：toRefs 全部属性转 ref**
`const <refs> = toRefs(<reactive>)`
```ts
// 配合解构
const { count, name } = toRefs(state);
```

---

**基本写法：toRef 从普通值创建 ref**
`const <ref> = toRef(<值>)`
```ts
// 等价 ref 但语义更清晰
const r = toRef(1);
```

---

## unref 解包 ref

**基本写法：获取 ref 或原值**
`const <val> = unref(<maybeRef>)`
```ts
// 是 ref 返回 .value 否则原值
const val = unref(maybeRef);
```

---

## isRef isReactive 判断

**基本写法：判断响应式类型**
`isRef(<值>); isReactive(<值>); isProxy(<值>)`
```ts
// 类型守卫
if (isRef(val)) val.value;
if (isReactive(val)) /* */;
```

---

## markRaw 永不代理

**基本写法：标记对象跳过响应式**
`const <raw> = markRaw(<对象>)`
```ts
// 第三方实例避免代理开销
const chart = markRaw(echarts.init(dom));
state.chart = chart;
```

---

## toRaw 获取原始对象

**基本写法：读取代理背后的原始对象**
`const <raw> = toRaw(<reactive>)`
```ts
// 用于调试或传递给非响应式代码
const raw = toRaw(state);
```

---

## effectScope 作用域管理

**基本写法：统一管理 effect 生命周期**
`const <scope> = effectScope()`
```ts
// 集中停止所有 effect
const scope = effectScope();
scope.run(() => {
  watch(count, cb);
  watchEffect(() => /* */);
});
onUnmounted(() => scope.stop());
```

---

## getCurrentScope 当前作用域

**基本写法：获取当前 effect scope**
`const <scope> = getCurrentScope()`
```ts
// 在组合式函数中使用
const scope = getCurrentScope();
```

---

## onScopeDispose 作用域清理

**基本写法：注册作用域销毁回调**
`onScopeDispose(() => <清理>)`
```ts
// 类似 onUnmounted 但作用域级
onScopeDispose(() => clearInterval(timer));
```

---

## 响应式转换工具

**基本写法：使用 reactive 解构 props 保持响应**
`const { <字段> = <默认> } = defineProps(['<字段>'])`
```vue
<!-- Vue 3.5 响应式解构 -->
<script setup>
const { count = 0, msg = 'hi' } = defineProps(['count', 'msg']);
</script>
```

---

## 异步组件与 Suspense

**基本写法：defineAsyncComponent**
`const <comp> = defineAsyncComponent(() => import(<路径>))`
```ts
// 异步加载组件
const Async = defineAsyncComponent(() => import('./Heavy.vue'));
```

---

**基本写法：配置加载状态**
`defineAsyncComponent({ loader, loadingComponent, errorComponent })`
```ts
// 完整配置
const Async = defineAsyncComponent({
  loader: () => import('./Heavy.vue'),
  loadingComponent: Loading,
  errorComponent: Error,
  delay: 200,
  timeout: 3000
});
```
