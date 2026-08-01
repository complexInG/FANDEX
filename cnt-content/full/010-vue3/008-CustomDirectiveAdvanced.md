---
order: 52
title: 自定义指令进阶
module: vue3
category: Vue3
difficulty: intermediate
description: 自定义指令高级用法
author: fanquanpp
updated: '2026-08-01'
related:
  - vue3/组合式API
  - vue3/Provide与Inject
  - vue3/Transition与动画
  - vue3/Vue3编译优化
prerequisites:
  - vue3/语法速查
---
## 1. 指令钩子

```javascript
const myDirective = {
  created(el, binding, vnode) {},
  beforeMount(el, binding) {},
  mounted(el, binding) {},
  beforeUpdate(el, binding) {},
  updated(el, binding) {},
  beforeUnmount(el, binding) {},
  unmounted(el, binding) {},
};
```

## 2. 钩子参数

```typescript
interface Binding {
  value: any; // 指令绑定的值
  oldValue: any; // 前一个值
  arg: string; // 指令参数 v-my:arg
  modifiers: Record<string, boolean>; // 修饰符 v-my.foo.bar
  instance: ComponentPublicInstance; // 组件实例
}
```

## 3. 实用指令示例

```javascript
// v-focus
const vFocus = {
  mounted(el) {
    el.focus();
  },
};

// v-permission
const vPermission = {
  mounted(el, binding) {
    const permissions = usePermissions();
    if (!permissions.has(binding.value)) {
      el.parentNode?.removeChild(el);
    }
  },
};

// v-debounce
const vDebounce = {
  mounted(el, binding) {
    let timer;
    el.addEventListener('input', () => {
      clearTimeout(timer);
      timer = setTimeout(() => binding.value(), binding.arg ? parseInt(binding.arg) : 300);
    });
  },
};

// v-click-outside
const vClickOutside = {
  mounted(el, binding) {
    const handler = (e) => {
      if (!el.contains(e.target)) binding.value(e);
    };
    el._clickOutside = handler;
    document.addEventListener('click', handler);
  },
  unmounted(el) {
    document.removeEventListener('click', el._clickOutside);
  },
};

// v-lazy 图片懒加载
const vLazy = {
  mounted(el, binding) {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        el.src = binding.value;
        observer.disconnect();
      }
    });
    observer.observe(el);
    el._observer = observer;
  },
  unmounted(el) {
    el._observer?.disconnect();
  },
};
```

## 4. 简写形式

```javascript
// 当 mounted 和 updated 行为相同时
const vColor = (el, binding) => {
  el.style.color = binding.value;
};
```
## 指令对象定义

**完整钩子对象**
```typescript
import type { Directive } from 'vue';

const vMyDirective: Directive<HTMLElement, string> = {
  // 在绑定元素的 attribute 或事件监听器被应用之前调用
  created(el, binding, vnode, prevVnode) {},

  // 在元素被插入到 DOM 前调用
  beforeMount(el, binding, vnode, prevVnode) {},

  // 在绑定元素的父组件及其所有子节点都挂载完成后调用
  mounted(el, binding, vnode, prevVnode) {},

  // 父组件更新前调用
  beforeUpdate(el, binding, vnode, prevVnode) {},

  // 在绑定元素的父组件及其所有子节点都更新完成后调用
  updated(el, binding, vnode, prevVnode) {},

  // 卸载绑定元素的父组件前调用
  beforeUnmount(el, binding, vnode, prevVnode) {},

  // 卸载绑定元素的父组件后调用
  unmounted(el, binding, vnode, prevVnode) {}
};
```

**简写形式**
```typescript
const vFocus: Directive = (el, binding) => {
  // mounted 和 updated 时都触发
  if (binding.value) {
    el.focus();
  }
};
```

---

## 指令钩子参数

**binding 对象**
```typescript
interface DirectiveBinding<V> {
  value: V;            // 指令绑定的值
  oldValue: V | null;  // 前一个值(仅在 beforeUpdate/updated 中可用)
  arg: string;         // 指令参数 v-my:foo -> 'foo'
  modifiers: Record<string, boolean>;  // 修饰符 v-my.foo.bar -> { foo: true, bar: true }
  instance: any;       // 使用该指令的组件实例
  dir: Object;         // 指令定义对象本身
}

function mounted(el: HTMLElement, binding: DirectiveBinding<string>) {
  console.log(binding.value);       // 'hello'
  console.log(binding.arg);         // 'color'
  console.log(binding.modifiers);   // { delay: true }
  console.log(binding.instance);    // 组件实例
}
```

**vnode 与 prevVnode**
```typescript
import type { VNode } from 'vue';

function mounted(el, binding, vnode: VNode, prevVnode: VNode | null) {
  // vnode: 当前虚拟节点
  // prevVnode: 前一个虚拟节点(更新钩子中)
}
```

---

## 注册指令

**局部注册**
```vue
<script setup>
import type { Directive } from 'vue';

const vFocus: Directive<HTMLElement> = {
  mounted(el) {
    el.focus();
  }
};
// 直接以 v 开头的变量会自动注册为指令 v-focus
</script>

<template>
  <input v-focus />
</template>
```

**全局注册**
```typescript
import { createApp } from 'vue';

const app = createApp(App);

app.directive('focus', {
  mounted(el) {
    el.focus();
  }
});

app.directive('color', (el, binding) => {
  el.style.color = binding.value;
});
```

**注册到组件**
```typescript
defineOptions({
  directives: {
    focus: {
      mounted(el: HTMLElement) {
        el.focus();
      }
    }
  }
});
```

---

## 指令参数与修饰符

**指令参数 arg**
```vue
<template>
  <div v-my:color="'red'"></div>
  <div v-my:background="'blue'"></div>
</template>

<script setup>
const vMy: Directive<HTMLElement, string> = {
  mounted(el, binding) {
    if (binding.arg === 'color') {
      el.style.color = binding.value;
    } else if (binding.arg === 'background') {
      el.style.background = binding.value;
    }
  }
};
</script>
```

**指令修饰符 modifiers**
```vue
<template>
  <div v-my.red.bold="text"></div>
</template>

<script setup>
const vMy: Directive = {
  mounted(el, binding) {
    if (binding.modifiers.red) el.style.color = 'red';
    if (binding.modifiers.bold) el.style.fontWeight = 'bold';
    el.textContent = binding.value;
  }
};
</script>
```

**动态参数**
```vue
<template>
  <div v-my:[direction]="'red'"></div>
</template>

<script setup>
import { ref } from 'vue';
const direction = ref('color');
</script>
```

---

## 实用指令示例

**v-focus 自动聚焦**
```typescript
import type { Directive } from 'vue';

const vFocus: Directive<HTMLElement> = {
  mounted(el) {
    el.focus();
  }
};
```

**v-permission 权限控制**
```typescript
import type { Directive } from 'vue';

const vPermission: Directive<HTMLElement, string | string[]> = {
  mounted(el, binding) {
    const userRoles = getUserRoles();
    const required = binding.value;
    const roles = Array.isArray(required) ? required : [required];

    const hasPermission = roles.some(r => userRoles.includes(r));
    if (!hasPermission) {
      el.parentNode?.removeChild(el);
    }
  }
};
```
```vue
<button v-permission="'admin'">删除</button>
<div v-permission="['admin', 'editor']">管理面板</div>
```

**v-debounce 防抖**
```typescript
import type { Directive } from 'vue';

const vDebounce: Directive<HTMLElement, () => void> = {
  mounted(el, binding) {
    let timer: number | undefined;
    el.addEventListener('click', () => {
      if (timer) clearTimeout(timer);
      timer = window.setTimeout(() => {
        binding.value();
      }, 500);
    });
  }
};
```

**v-loading 加载指令**
```typescript
import type { Directive } from 'vue';

const vLoading: Directive<HTMLElement, boolean> = {
  mounted(el, binding) {
    el.style.position = 'relative';
    if (binding.value) createMask(el);
  },
  updated(el, binding) {
    if (binding.value !== binding.oldValue) {
      binding.value ? createMask(el) : removeMask(el);
    }
  }
};

function createMask(el: HTMLElement) {
  const mask = document.createElement('div');
  mask.className = 'loading-mask';
  mask.style.cssText = 'position:absolute;inset:0;background:rgba(0,0,0,0.5);';
  mask.dataset.role = 'loading';
  el.appendChild(mask);
}

function removeMask(el: HTMLElement) {
  el.querySelector('[data-role="loading"]')?.remove();
}
```

**v-longpress 长按**
```typescript
import type { Directive } from 'vue';

const vLongpress: Directive<HTMLElement, () => void> = {
  mounted(el, binding) {
    let timer: number | undefined;

    const start = () => {
      timer = window.setTimeout(() => binding.value(), 800);
    };
    const cancel = () => {
      if (timer) clearTimeout(timer);
    };

    el.addEventListener('mousedown', start);
    el.addEventListener('mouseup', cancel);
    el.addEventListener('mouseleave', cancel);
    el.addEventListener('touchstart', start);
    el.addEventListener('touchend', cancel);

    el._cleanup = () => {
      el.removeEventListener('mousedown', start);
      el.removeEventListener('mouseup', cancel);
      el.removeEventListener('mouseleave', cancel);
      el.removeEventListener('touchstart', start);
      el.removeEventListener('touchend', cancel);
    };
  },
  unmounted(el) {
    el._cleanup?.();
  }
};
```

---

## 在 TS 中扩展

**自定义指令类型扩展**
```typescript
declare module 'vue' {
  interface ComponentCustomProperties {
    vPermission: Directive<HTMLElement, string | string[]>;
    vDebounce: Directive<HTMLElement, () => void>;
  }
}
```

---

## TypeScript 完整示例

```typescript
import { createApp, type Directive, type DirectiveBinding } from 'vue';

interface RippleOptions {
  color?: string;
  duration?: number;
}

const vRipple: Directive<HTMLElement, RippleOptions | undefined> = {
  mounted(el: HTMLElement, binding: DirectiveBinding<RippleOptions | undefined>) {
    el.style.position = 'relative';
    el.style.overflow = 'hidden';

    el.addEventListener('click', (event: MouseEvent) => {
      const rect = el.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      const x = event.clientX - rect.left - size / 2;
      const y = event.clientY - rect.top - size / 2;

      const ripple = document.createElement('span');
      ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        left: ${x}px;
        top: ${y}px;
        background: ${binding.value?.color || 'rgba(255,255,255,0.5)'};
        border-radius: 50%;
        transform: scale(0);
        animation: ripple ${binding.value?.duration || 600}ms ease-out;
        pointer-events: none;
      `;
      el.appendChild(ripple);
      setTimeout(() => ripple.remove(), binding.value?.duration || 600);
    });
  }
};

const app = createApp(App);
app.directive('ripple', vRipple);
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
| 自定义指令进阶 | 008-CustomDirectiveAdvanced | 本文自身 |
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
