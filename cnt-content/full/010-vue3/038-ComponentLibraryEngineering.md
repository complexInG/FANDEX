---
order: 380
title: 组件库工程化
module: vue3
category: '010-vue3'
difficulty: advanced
description: 从源码、构建到发布，讲清 Vue 3 组件库的工程骨架：目录设计、样式方案、类型导出与版本发布。
author: fanquanpp
created: '2026-08-02'
updated: '2026-08-02'
related:
  - 'vue3/018-ComponentSystem'
  - 'vue3/019-TypeScriptIntegration'
prerequisites:
  - 'vue3/018-ComponentSystem'
quiz:
  - type: choice
    question: 组件库构建时为什么要同时产出 ESM 与类型声明？
    options:
      - 为了文件更多
      - 应用侧需要按需导入的 ESM，编辑器需要 d.ts 提供类型提示
      - 只有浏览器需要类型声明
      - 类型声明会被打包进 JS
    answer: 1
    explanation: ESM 支持按需 tree-shaking，d.ts 让使用者获得完整类型体验。
  - type: fill
    question: 组件库中用于隔离样式的 Vue 特性是 scoped 与 CSS ____。
    answer: 变量（CSS Variables）
    hint: 即设计令牌，常通过 CSS 变量实现主题定制。
references:
  - type: documentation
    authors:
      - Vue.js Team
    year: 2026
    title: Vue 组件基础
    venue: cn.vuejs.org
    url: https://cn.vuejs.org/guide/components/
    accessedDate: '2026-08-02'
  - type: documentation
    authors:
      - Vite Team
    year: 2026
    title: Vite 库模式构建
    venue: cn.vitejs.dev
    url: https://cn.vitejs.dev/guide/build.html#library-mode
    accessedDate: '2026-08-02'
etymology:
  - term: 组件库
    english: Component Library
    origin: library 意为"藏书处"，组件库把可复用的 UI 零件按统一规范"入库"管理。
estimatedReadingTime: 8
lastReviewed: '2026-08-02'
reviewer: fanquanpp
---

## 一句话理解

组件库工程化 = 把"一组好看的组件"升级为"可维护、可按需引入、有类型、有版本"的交付物。

## 为什么需要

- 多个项目复用同一套组件时，复制粘贴必然漂移。
- 使用方需要：按需导入、Tree Shaking、完整类型提示、主题定制。
- 维护方需要：清晰的目录、样式隔离、自动化发布。

## 目录设计

```text
my-ui/
├── src/
│   ├── components/
│   │   ├── Button/
│   │   │   ├── Button.vue
│   │   │   └── index.ts        # 组件入口
│   │   └── index.ts            # 统一导出
│   ├── styles/
│   │   ├── tokens.css          # 设计令牌（CSS 变量）
│   │   └── index.css
│   └── index.ts                # 库入口
├── docs/                       # 文档与演示
├── vite.config.ts              # 库模式构建
├── package.json
└── tsconfig.json
```

## 构建配置：Vite 库模式

```ts
// vite.config.ts
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import dts from 'vite-plugin-dts';

export default defineConfig({
  plugins: [vue(), dts({ include: ['src'] })],
  build: {
    lib: {
      entry: 'src/index.ts',
      name: 'MyUI',
      formats: ['es', 'cjs'], // ESM 供按需导入，CJS 兼容旧工具链
      fileName: (format) => `my-ui.${format}.js`,
    },
    rollupOptions: {
      external: ['vue'], // vue 是 peer 依赖，不进产物
    },
  },
});
```

```json
// package.json 出口配置
{
  "name": "my-ui",
  "type": "module",
  "main": "./dist/my-ui.cjs.js",
  "module": "./dist/my-ui.es.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/my-ui.es.js",
      "require": "./dist/my-ui.cjs.js"
    },
    "./styles.css": "./dist/styles.css"
  },
  "peerDependencies": {
    "vue": "^3.4.0"
  }
}
```

## 样式与主题

```css
/* tokens.css：主题由 CSS 变量驱动，用户可覆盖 */
:root {
  --ui-color-primary: #0e8c9c;
  --ui-radius: 4px;
}
```

```vue
<!-- Button.vue：scoped 样式 + 变量取值 -->
<template>
  <button class="ui-button" :class="`ui-button--${variant}`">
    <slot />
  </button>
</template>

<style scoped>
.ui-button {
  padding: 6px 14px;
  border-radius: var(--ui-radius);
  color: var(--ui-color-primary);
}
</style>
```

## 发布与版本

- 语义化版本：破坏性变更发 major，新特性发 minor，修复发 patch。
- 变更日志（CHANGELOG）随版本更新，使用方才能判断升级风险。
- 发布前跑类型检查、单测与文档示例构建。

## 常见误区

| 误区 | 真相 |
| --- | --- |
| 把 vue 打进产物 | vue 应作为 peerDependency，否则多个副本导致运行时冲突 |
| 只发一个文件 | 需要 ESM + d.ts + 样式资源，配套 exports 映射 |
| 样式写在组件里就完事 | 主题化需要把可变值抽象成 CSS 变量 |
| 版本号随意升 | 语义化版本是组件库与使用方之间的契约 |

## 小结

组件库工程化没有玄学：目录按组件拆、构建用库模式、样式走变量、发布守语义化版本。
从第一个 Button 开始就按这个骨架走，后续加组件只是"复制目录 + 导出"的重复劳动。
