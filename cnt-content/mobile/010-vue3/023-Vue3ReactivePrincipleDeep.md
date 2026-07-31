# Vue 3 响应式原理深入

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ref 基本原理

**基本写法：ref 包裹任意值返回响应式引用**
`const <ref> = ref(<初值>)`
```ts
// 内部使用 RefImpl 类
const count = ref(0);
count.value++;
```

---

**基本写法：ref 自动解包**
`<ref> 在模板中直接使用`
```vue
<!-- 模板中无需 .value -->
<script setup>
import { ref } from 'vue';
const count = ref(0);
</script>
<template>{{ count }}</template>
```

---

## reactive 原理

**基本写法：reactive 返回 Proxy 代理对象**
`const <state> = reactive(<对象>)`
```ts
// 深层代理所有属性
const state = reactive({ count: 0, nested: { value: 1 } });
state.nested.value = 2;
```

---

**基本写法：reactive 仅适用对象类型**
`reactive(<对象>) // 基本类型无效`
```ts
// 数字字符串等基本类型应使用 ref
const num = reactive(0); // 警告应使用 ref
```

---

## Proxy 代理机制

**基本写法：reactive 内部用 Proxy 拦截**
`new Proxy(<target>, { get, set, deleteProperty })`
```ts
// 拦截读取修改删除
const proxy = new Proxy(target, {
  get(target, key, receiver) {
    track(target, key);
    return Reflect.get(target, key, receiver);
  }
});
```

---

## 依赖收集 track

**基本写法：get 时收集当前 effect**
`track(<target>, <key>)`
```ts
// 建立属性与 effect 映射
function track(target, key) {
  if (activeEffect) {
    depsMap.get(key).add(activeEffect);
  }
}
```

---

## 依赖触发 trigger

**基本写法：set 时触发所有依赖**
`trigger(<target>, <key>)`
```ts
// 通知所有 effect 执行
function trigger(target, key) {
  const effects = depsMap.get(key);
  effects.forEach(effect => effect());
}
```

---

## effect 副作用函数

**基本写法：effect 包装副作用**
`effect(() => <副作用>)`
```ts
// 自动追踪依赖变化触发
effect(() => console.log(state.count));
```

---

## ref 与 reactive 区别

**基本写法：ref 适用基本类型**
`const <ref> = ref(<基本值>)`
```ts
// ref 用 .value 访问
const num = ref(0);
num.value++;
```

---

**基本写法：reactive 适用对象**
`const <state> = reactive(<对象>)`
```ts
// reactive 直接访问属性
const state = reactive({ count: 0 });
state.count++;
```

---

## ref 内部实现

**基本写法：ref 通过 RefImpl 类实现**
`class <RefImpl> { get value() { track }; set value(<v>) { trigger } }`
```ts
// 类的 getter setter 实现依赖追踪
class RefImpl {
  _value;
  get value() { track(this, 'value'); return this._value; }
  set value(v) { this._value = v; trigger(this, 'value'); }
}
```

---

## reactive 陷阱：解构丢失响应性

**基本写法：解构 reactive 会断开代理**
`const { <字段> } = <reactive对象> // 失去响应`
```ts
// 错误：解构后变量不响应
const state = reactive({ count: 0 });
const { count } = state; // count 不再响应
```

---

**基本写法：使用 toRefs 转换**
`const { <字段> } = toRefs(<reactive对象>)`
```ts
// 正确：解构得到 ref
const { count } = toRefs(state);
count.value++;
```

---

## reactive 陷阱：替换整个对象

**基本写法：替换对象会失去代理**
`<state> = <新对象> // 失去响应`
```ts
// 错误：原代理失效
let state = reactive({ count: 0 });
state = { count: 1 }; // 视图不更新
```

---

**基本写法：使用 Object.assign 更新属性**
`Object.assign(<state>, <新对象>)`
```ts
// 正确：保留代理逐字段更新
Object.assign(state, { count: 1, name: 'Alice' });
```

---

## ref 陷阱：reactive 内自动解包

**基本写法：reactive 包裹 ref 自动解包**
`const <state> = reactive({ <ref>: <ref> })`
```ts
// 访问 state.count 无需 .value
const count = ref(0);
const state = reactive({ count });
state.count++; // 自动解包
```

---

## 深层响应 shallowRef

**基本写法：shallowRef 仅 .value 响应**
`const <ref> = shallowRef(<对象>)`
```ts
// 内部属性变化不触发
const state = shallowRef({ count: 0 });
state.value.count++; // 不触发
state.value = { count: 1 }; // 触发
```

---

## shallowReactive 浅响应

**基本写法：shallowReactive 仅根属性响应**
`const <state> = shallowReactive(<对象>)`
```ts
// 嵌套属性不响应
const state = shallowReactive({ foo: 1, nested: { bar: 2 } });
state.foo++; // 触发
state.nested.bar++; // 不触发
```

---

## readonly 只读代理

**基本写法：readonly 创建只读响应**
`const <ro> = readonly(<reactive对象>)`
```ts
// 修改会发出警告
const original = reactive({ count: 0 });
const ro = readonly(original);
ro.count++; // 警告
```

---

## toRef 单属性转 ref

**基本写法：将 reactive 属性转为 ref**
`const <ref> = toRef(<reactive>, '<字段>')`
```ts
// 保持响应式关联
const state = reactive({ count: 0 });
const countRef = toRef(state, 'count');
```

---

## toRefs 全部属性转 ref

**基本写法：将 reactive 全部属性转为 ref**
`const <refs> = toRefs(<reactive>)`
```ts
// 配合解构使用
const { count, name } = toRefs(state);
```

---

## customRef 自定义 ref

**基本写法：自定义依赖追踪**
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

## triggerRef 强制触发

**基本写法：手动触发 shallowRef 依赖**
`triggerRef(<shallowRef>)`
```ts
// 修改内部属性后强制更新
const state = shallowRef({ count: 0 });
state.value.count++;
triggerRef(state); // 通知更新
```

---

## markRaw 标记永不响应

**基本写法：标记对象不被代理**
`const <raw> = markRaw(<对象>)`
```ts
// 第三方实例避免被代理
const chart = markRaw(echarts.init(dom));
```

---

## toRaw 获取原始对象

**基本写法：读取代理背后的原始对象**
`const <raw> = toRaw(<reactive>)`
```ts
// 用于比较或传递给非响应式代码
const raw = toRaw(state);
```

---

## effectScope 作用域

**基本写法：统一管理 effect**
`const <scope> = effectScope()`
```ts
// 集中停止所有 effect
const scope = effectScope();
scope.run(() => {
  effect(() => console.log(state.count));
});
scope.stop(); // 停止所有
```

---

## computed 计算属性原理

**基本写法：computed 基于 effect 实现**
`const <c> = computed(() => <计算>)`
```ts
// 缓存依赖未变时返回旧值
const double = computed(() => state.count * 2);
```

---

## watch 监听原理

**基本写法：watch 基于 effect 实现**
`watch(<源>, <回调>, [<选项>])`
```ts
// 副作用追踪依赖变化触发回调
watch(() => state.count, (newVal, oldVal) => console.log(newVal));
```

---

## 数组响应式注意事项

**基本写法：reactive 数组索引赋值响应**
`<state>.<arr>[0] = <值>`
```ts
// Proxy 拦截索引修改
const state = reactive({ list: [1, 2, 3] });
state.list[0] = 99; // 响应
```

---

**基本写法：length 修改触发更新**
`<state>.<arr>.length = <长度>`
```ts
// 截断数组响应
state.list.length = 1; // 响应
```

---

## Map/Set 响应式

**基本写法：reactive 支持 Map Set**
`const <state> = reactive(new Map())`
```ts
// 集合操作自动响应
const state = reactive(new Map());
state.set('key', 'value');
```

---

## 响应式调试

**基本写法：onTrack onTrigger 调试钩子**
`const <c> = computed(() => <计算>, { onTrack, onTrigger })`
```ts
// 开发期追踪依赖
const c = computed(() => state.count, {
  onTrack(e) { console.log('track', e); },
  onTrigger(e) { console.log('trigger', e); }
});
```
