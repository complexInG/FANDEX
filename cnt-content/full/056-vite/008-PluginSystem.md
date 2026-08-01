---
order: 8
title: Vite 插件系统
module: vite
category: Vite
difficulty: advanced
description: 'Vite 插件系统：插件 API、常用插件、钩子机制与自定义插件编写'
author: fanquanpp
updated: '2026-08-01'
related:
  - vite/007-BuildSplit
  - vite/009-Vite8Rolldown
prerequisites:
  - vite/003-ConfigFile
  - vite/007-BuildSplit
---
## 1. 插件是什么

插件是 Vite 的扩展机制：通过约定的"钩子"介入构建流程，实现框架支持、代码转换、资源处理、自定义指令等能力。Vite 8 中 Rolldown 完全兼容 Rollup 插件 API，因此**绝大部分现有 Vite/Rollup 插件开箱即用**，无需改动（详见 009 篇）。

```text
Vite 核心自身只负责：模块解析、转换调度、HMR、构建编排
其余能力（React/Vue 支持、路径别名、代码检查...）都通过插件提供
```

讲解：理解插件 = 理解"在构建管线中的特定时机执行特定代码"。官方框架插件是最好的人门教材：`@vitejs/plugin-react`、`@vitejs/plugin-vue` 都用纯 JS 编写，开源可读。

## 2. 常用插件一览

| 插件 | 用途 |
| --- | --- |
| `@vitejs/plugin-react` | React JSX 转换 + Fast Refresh |
| `@vitejs/plugin-vue` | Vue 单文件组件（SFC）支持 |
| `@vitejs/plugin-legacy` | 旧浏览器兼容（语法降级 + polyfill） |
| `vite-plugin-pwa` | PWA 支持（Service Worker 等） |
| `unplugin-auto-import` | 自动按需引入 API |
| `rollup-plugin-visualizer` | 产物体积可视化分析 |
| `@tailwindcss/vite` | Tailwind CSS 集成（005 篇） |

讲解：插件分两类——**官方插件**（vitejs 组织维护，随核心迭代）与**社区插件**（unplugin 系列、第三方）。检索插件推荐官方目录 https://registry.vite.dev/（Vite 8 起提供，每日同步 npm 数据）。

安装与注册：

```bash
pnpm add -D @vitejs/plugin-legacy
```

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import legacy from '@vitejs/plugin-legacy'

export default defineConfig({
  plugins: [
    legacy({
      targets: ['defaults', 'not IE 11'],
    }),
  ],
})
```

讲解：`plugins` 是数组，顺序有讲究——同一文件可被多个插件处理，按数组顺序依次调用钩子。Vite 内置插件在用户插件之后执行；`apply` 可控制插件只在 dev 或 build 时生效。

## 3. 插件钩子机制

钩子分为三个阶段（兼容 Rollup 命名）：

```text
构建阶段：resolveId（解析模块 ID） -> load（加载模块源码）
转换阶段：transform（转换源码）
输出阶段：generateBundle / writeBundle（生成产物）
```

| 钩子 | 触发时机 | 典型用途 |
| --- | --- | --- |
| `config` | 读取配置文件后 | 修改/追加配置 |
| `configureServer` | dev server 启动时 | 注入中间件、自定义接口 |
| `resolveId` | 解析 import 路径时 | 自定义模块解析 |
| `load` | 加载模块内容时 | 返回虚拟模块源码 |
| `transform` | 每个模块转换前 | 编译、改写源码 |
| `handleHotUpdate` | 文件变更触发 HMR 时 | 自定义 HMR 逻辑 |
| `generateBundle` | 产物生成阶段 | 修改/删除产物文件 |

讲解：Vite 独有钩子（`config`、`configureServer`、`handleHotUpdate` 等）只在 Vite 环境生效；Rolldown 同样实现了这些钩子，因此在 Vite 8 中开发与构建走同一套插件管线。

## 4. 编写第一个自定义插件

目标是实现一个"加载虚拟模块"的插件：业务代码 `import data from 'virtual:demo'` 时，返回插件生成的 JSON 数据。

```ts
// plugins/virtual-demo.ts
import type { Plugin } from 'vite'

export function virtualDemo(): Plugin {
  const virtualModuleId = 'virtual:demo'
  const resolvedId = '\0' + virtualModuleId  // \0 前缀避免与其他插件冲突

  return {
    name: 'virtual-demo',
    // 解析阶段：把虚拟模块 ID 解析为唯一标识
    resolveId(id) {
      if (id === virtualModuleId) return resolvedId
    },
    // 加载阶段：返回模块源码
    load(id) {
      if (id === resolvedId) {
        return `export const data = ${JSON.stringify({ hello: 'vite' })}`
      }
    },
  }
}
```

```ts
// 业务代码中使用
import { data } from 'virtual:demo'
console.log(data.hello)  // 'vite'
```

讲解：`\0` 前缀是 Rollup/Rolldown 约定的"不可见 ID"标记，防止虚拟模块被真实文件系统解析命中；`resolveId` 返回它后，`load` 拿到的是加了 `\0` 的 ID。这是"虚拟模块"模式的标准写法，广泛用于自动生成路由、注入版本号等场景。

## 5. transform 钩子：转换源码

```ts
// plugins/console-demo.ts
import type { Plugin } from 'vite'

export function consoleDemo(): Plugin {
  return {
    name: 'console-demo',
    // 仅处理 .ts/.js 文件
    transform(code, id) {
      if (!id.endsWith('.ts') && !id.endsWith('.js')) return null
      // 演示：给每个文件头部注入一行注释
      const banner = '/* transformed by console-demo */\n'
      return {
        code: banner + code,
        map: null,   // sourcemap 由后续插件/构建器生成
      }
    },
  }
}
```

讲解：`transform` 返回 `{ code, map }` 或直接返回字符串；不需要修改时返回 `null`。钩子内尽量避免高成本操作，Vite 8 中 Rolldown 提供了 **hook filters**（如 `transformFilter: { id: { include: [/\.ts$/] } }`）让不匹配的文件跳过 JS 桥接，插件多时也不拖慢构建（详见 009 篇）。

## 6. 插件与构建配置的配合

高级用法：插件接收配置对象，按需生成构建选项：

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig({
  plugins: [
    // 插件返回的对象最终会被合并进构建配置
    visualizer({ filename: 'dist/stats.html' }),
  ],
})
```

讲解：插件可以直接在返回对象中声明 `build`、`resolve` 等字段，Vite 会合并这些配置——这让插件能做到"安装即用，零手动配置"。编写插件时也常通过 `configResolved` 钩子读取最终配置决定行为：

```ts
import type { Plugin } from 'vite'

export function demoPlugin(): Plugin {
  let isBuild = false
  return {
    name: 'demo',
    configResolved(config) {
      isBuild = config.command === 'build'  // 拿到最终配置
    },
    transform(code, id) {
      if (!isBuild) return null  // 仅生产构建时转换
    },
  }
}
```

## 7. 常见陷阱

陷阱一：`\0` 前缀被用户代码看到。虚拟模块仅内部使用，切勿暴露给业务代码。

陷阱二：插件顺序错误导致转换失效。检查 `plugins` 数组顺序，必要时用 `enforce: 'pre' | 'post'` 控制执行时机。

陷阱三：只在 dev 生效的钩子进了 build。区分 Vite 独有钩子与通用钩子，或使用 `apply: 'serve' / 'build'`。

陷阱四：与 Rolldown 不兼容的冷门 Rollup 插件。绝大多数插件正常，极少数依赖 Rollup 内部 API 的插件需等待作者适配（009 篇有迁移清单）。

## 8. 参考资源

Vite 插件 API：https://vite.dev/guide/api-plugin

Rolldown 插件开发指南：https://rolldown.rs/plugin-development

插件目录（Vite 8 官方）：https://registry.vite.dev/
