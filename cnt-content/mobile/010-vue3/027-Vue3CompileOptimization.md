# Vue 3 编译优化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 静态提升 Static Hoisting

**基本写法：静态节点提升到 render 函数外**
`const <vnode> = createVNode('div', null, '静态')`
```vue
<!-- 静态节点被提升避免每次渲染重建 -->
<div class="header"><span>静态标题</span></div>
```

---

**基本写法：纯静态提升**
`<div class="box">固定内容</div>`
```vue
<!-- 不含动态绑定的节点整体提升 -->
<div class="box">固定内容</div>
```

---

## 补丁标记 PatchFlag

**基本写法：编译器标记动态节点类型**
`createVNode('div', null, text, PatchFlags.TEXT)`
```vue
<!-- 编译产物带 patchFlag 仅比对动态部分 -->
<div>{{ message }}</div>
```

---

**基本写法：标记不同类型动态**
`PatchFlags.TEXT | PatchFlags.CLASS | PatchFlags.PROPS`
```vue
<!-- 文本动态 -->
<div>{{ msg }}</div>
<!-- class 动态 -->
<div :class="cls">文本</div>
<!-- props 动态 -->
<div :id="id">文本</div>
```

---

## 块级树 Block

**基本写法：根节点收集动态子节点**
`createBlock('div', null, [<children>], PatchFlags)`
```vue
<!-- 模板根节点自动作为 Block -->
<template>
  <div>
    <p>静态</p>
    <p>{{ msg }}</p>
  </div>
</template>
```

---

**基本写法：Block 数组优化 diff**
`const <dynamicChildren> = []`
```ts
// Block 仅 diff 动态子节点跳过静态
block.dynamicChildren = [dynamicVNode];
```

---

## v-if 优化的 key

**基本写法：v-if/v-else 配 key 优化**
`<div v-if="<条件>" key="a">`
```vue
<!-- 添加 key 提高复用判断 -->
<div v-if="show" key="on">显示</div>
<div v-else key="off">隐藏</div>
```

---

## v-for 优化的 key

**基本写法：稳定唯一 key 加速 diff**
`<div v-for="<项> in <列表>" :key="<项>.id">`
```vue
<!-- 使用稳定 key -->
<div v-for="item in list" :key="item.id">{{ item.name }}</div>
```

---

## 缓存事件处理函数

**基本写法：内联事件被缓存**
`<button @click="<回调>">`
```vue
<!-- 编译器缓存事件处理避免每次创建 -->
<button @click="onClick">点击</button>
```

---

**基本写法：内联表达式事件**
`<button @click="count++">`
```vue
<!-- 缓存为函数 -->
<button @click="count++">加</button>
```

---

## 静态属性合并

**基本写法：静态 class style 合并为对象**
`createElementVNode('div', { class: 'box' })`
```vue
<!-- 静态 class 提前计算 -->
<div class="box">内容</div>
```

---

## SSR 优化

**基本写法：SSR 字符串拼接跳过响应式**
`ssrRenderAttr('class', <值>)`
```vue
<!-- SSR 模式直接字符串拼接 -->
<div>{{ message }}</div>
```

---

## v-once 一次性渲染

**基本写法：标记节点只渲染一次**
`<div v-once>{{ <静态值> }}</div>`
```vue
<!-- 编译为静态提升节点 -->
<header v-once>{{ title }}</header>
```

---

## v-memo 记忆化

**基本写法：依赖未变跳过子树 patch**
`<div v-memo="[<依赖>]">`
```vue
<!-- 依赖不变跳过整个子树更新 -->
<div v-memo="[item.id]">
  <span>{{ item.name }}</span>
  <span>{{ item.age }}</span>
</div>
```

---

## 内联事件缓存

**基本写法：内联函数自动缓存**
`<button @click="<复杂表达式>">`
```vue
<!-- 表达式被提取并缓存 -->
<button @click="onClick($event, id)">点击</button>
```

---

## BlockTree 收集

**基本写法：动态子节点收集到数组**
`<block>.dynamicChildren`
```ts
// Block 仅遍历动态节点
function patchBlock(n1, n2) {
  for (let i = 0; i < n2.dynamicChildren.length; i++) {
    patch(n1.dynamicChildren[i], n2.dynamicChildren[i]);
  }
}
```

---

## 模板编译产物对比

**基本写法：编译前模板**
`<div :id="<动态>"><span>静态</span></div>`
```vue
<!-- 源模板 -->
<template>
  <div :id="dynamicId"><span>静态</span></div>
</template>
```

---

**基本写法：编译后渲染函数**
`function render(_ctx) { return createVNode('div', { id: _ctx.dynamicId }, [staticVNode]) }`
```ts
// 编译产物
function render(_ctx) {
  return createVNode('div', { id: _ctx.dynamicId }, [
    _hoisted_1 // 静态节点提升
  ], PatchFlags.PROPS, ['id']);
}
```

---

## Slot 优化

**基本写法：编译作用域插槽**
`<slot :<字段>="<值>" />`
```vue
<!-- 插槽编译为函数 -->
<slot :item="item" />
```

---

**基本写法：消费作用域插槽**
`<template #default="{ <字段> }">`
```vue
<!-- 编译为接收 props 的函数 -->
<template #default="{ item }">{{ item.name }}</template>
```

---

## Fragment 多根节点

**基本写法：多根节点编译为 Fragment**
`<><div/><div/></>`
```vue
<!-- 不再需要单一根节点 -->
<template>
  <header>头部</header>
  <main>主体</main>
</template>
```

---

## v-bind 合并

**基本写法：v-bind 对象展开**
`<div v-bind="<对象>">`
```vue
<!-- 编译为合并的 props 对象 -->
<div v-bind="attrs">内容</div>
```

---

## v-model 编译

**基本写法：v-model 编译为 modelValue 与 update**
`<input v-model="<值>" />`
```vue
<!-- 等价于 -->
<input :model-value="value" @update:model-value="value = $event" />
```

---

## 自定义指令编译

**基本写法：指令编译为 withDirectives**
`withDirectives(createVNode(...), [[<指令>, <值>]])`
```vue
<!-- 模板指令 -->
<div v-focus>内容</div>
```

---

## 编译器选项

**基本写法：配置编译选项**
`compilerOptions: { isCustomElement: <fn> }`
```ts
// vite.config.js
vue({
  template: {
    compilerOptions: { isCustomElement: tag => tag.startsWith('x-') }
  }
})
```

---

## 编译模式 ssr

**基本写法：SSR 编译模式**
`compile(<模板>, { ssr: true })`
```ts
// 服务端编译为字符串拼接
import { compile } from 'vue/compiler-ssr';
const render = compile(template, { ssr: true });
```

---

## 性能对比

**基本写法：Vue 3 比 Vue 2 性能提升**
`{ 性能: '提升 1.3~2 倍', 包体积: '减少 40%' }`
```ts
// 编译优化使 Vue 3 渲染更快
// Block + PatchFlag + 静态提升
```

---

## 源码映射

**基本写法：开发环境启用 sourcemap**
`vue({ template: { compilerOptions: { sourceMap: true } } })`
```ts
// 便于调试模板
vue({ template: { compilerOptions: { sourceMap: true } } })
```

---

## 编译错误

**基本写法：编译错误处理**
`compile(<模板>) // 抛出错误`
```ts
// 模板语法错误编译期检测
try {
  compile('<div>');
} catch (e) {
  console.error(e);
}
```

---

## 编译宏

**基本写法：defineProps 与 defineEmits**
`const <props> = defineProps(['<字段>'])`
```vue
<!-- 编译宏无需导入 -->
<script setup>
const props = defineProps(['count']);
const emit = defineEmits(['change']);
</script>
```

---

## defineOptions 宏

**基本写法：script setup 中声明组件选项**
`defineOptions({ name: '<组件名>' })`
```vue
<!-- Vue 3.3+ -->
<script setup>
defineOptions({ name: 'UserCard', inheritAttrs: false });
</script>
```
