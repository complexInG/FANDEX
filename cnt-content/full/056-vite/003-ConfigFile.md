---
order: 3
title: Vite 配置文件详解
module: vite
category: Vite
difficulty: beginner
description: 'vite.config.ts 详解：defineConfig、路径别名、环境变量与 loadEnv'
author: fanquanpp
updated: '2026-08-01'
related:
  - vite/002-QuickStart
  - vite/006-DevServerHMR
  - vite/007-BuildSplit
prerequisites:
  - vite/002-QuickStart
---
## 1. 配置文件是什么

Vite 的几乎所有行为（端口、别名、插件、构建选项）都可以通过项目根目录下的配置文件控制。Vite 会自动加载以下位置之一的文件（按优先级从高到低）：

| 文件名 | 说明 |
| --- | --- |
| `vite.config.ts` | 推荐，TypeScript 编写，带完整类型提示 |
| `vite.config.mjs` | 纯 ESM 的 JS 配置 |
| `vite.config.js` | 普通 JS 配置（须为 ESM 或 CJS） |

官方推荐一律使用 `vite.config.ts`：配置文件本身就是 TS 文件，编辑器能给出全量的选项提示与校验，这是 Vite 开箱即用的开发者体验。

```bash
# 也可显式指定配置文件位置
vite --config my-config.ts
```

讲解：配置文件的路径解析规则是"从进程当前工作目录向上查找"，通常放在项目根目录。修改配置文件后 Vite 会自动重启 dev server，无需手动操作。

## 2. defineConfig：让配置拥有类型提示

直接导出对象也能工作，但更推荐用 `defineConfig` 包裹：

```ts
// vite.config.ts
import { defineConfig } from 'vite'

export default defineConfig({
  root: '.',          // 项目根目录
  base: '/',          // 公共基础路径（部署到子路径时修改）
  plugins: [],
})
```

讲解：`defineConfig` 的实质是一个透传函数——它不改变对象内容，只是让 TypeScript 推断出配置对象的类型，从而获得补全与报错能力。它还可以接收**函数**，实现按环境返回不同配置：

```ts
import { defineConfig } from 'vite'

export default defineConfig(({ command, mode }) => {
  // command: 'serve'（dev）| 'build'
  // mode: 'development' | 'production' 或自定义模式
  const isBuild = command === 'build'
  return {
    define: {
      __BUILD__: JSON.stringify(isBuild),
    },
  }
})
```

讲解：函数形式适合"开发与构建行为差异较大"的项目。`command` 区分 dev/build，`mode` 对应环境变量模式（见第 5 节），两者是最常用的两个入参。

## 3. resolve.alias：路径别名

`@/` 指向 `src/` 是最常见的别名配置，能彻底告别 `../../` 这种相对路径地狱：

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import path from 'node:path'

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      '@components': path.resolve(__dirname, 'src/components'),
    },
  },
})
```

讲解：`__dirname` 在 ESM 配置中不可直接用，Vite 8 会在内部把配置转译为 CJS 执行，因此直接使用即可。别名生效后，`import Header from '@/components/Header'` 等价于相对路径引入。

**关键联动**：Vite 的别名只影响运行与构建，不影响 TypeScript 的类型检查。必须同步配置 `tsconfig.json`，否则编辑器报"找不到模块"：

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    }
  }
}
```

讲解：`tsconfig.json` 中的 `paths` 与 Vite 的 `alias` 是两套独立机制，修改任一处都要记得同步另一处。这是初学者最常见的报错来源之一。

## 4. 环境变量：import.meta.env 与 .env 文件

### 4.1 .env 文件

在项目根目录创建 `.env` 系列文件，Vite 启动时自动加载：

```bash
# .env                # 所有环境都生效
VITE_APP_TITLE=FANDEX
VITE_API_BASE=/api

# .env.development    # 仅 dev 生效（mode 为 development）
VITE_DEBUG=true

# .env.production     # 仅 build 生效（mode 为 production）
VITE_APP_TITLE=FANDEX-Prod
```

讲解：只有以 `VITE_` 前缀开头的变量会暴露给客户端代码，其余变量只在配置文件中可见。这是刻意设计的安全边界——**密钥、Token 等敏感信息绝不能放进 VITE_ 变量**，否则会出现在最终产物中。

### 4.2 在代码中使用

```ts
// 任意源码文件
const apiBase = import.meta.env.VITE_API_BASE
const isProd = import.meta.env.PROD      // 内置：是否生产环境
const isDev = import.meta.env.DEV        // 内置：是否开发环境
const mode = import.meta.env.MODE        // 内置：当前模式名
```

讲解：`import.meta.env` 由 Vite 在编译时静态替换为实际值，因此必须使用完整字面量写法（不能写成 `import.meta.env[key]` 动态取值，那样无法被替换）。

### 4.3 类型声明

新建 `src/vite-env.d.ts`，为自定义变量补充类型：

```ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_APP_TITLE: string
  readonly VITE_API_BASE: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
```

讲解：`vite/client` 类型声明提供了 `import.meta.env` 的内置字段与静态资源导入的类型。自定义的 VITE_ 变量按上述方式声明后，编辑器就能给出类型提示。

## 5. loadEnv：在配置文件中读取环境变量

`.env` 变量默认只对**客户端代码**可见。若配置本身（如代理目标、CDN 地址）也需要读取环境变量，就要用 `loadEnv` 手动加载：

```ts
// vite.config.ts
import { defineConfig, loadEnv } from 'vite'

export default defineConfig(({ mode }) => {
  // 从项目根目录加载 .env 系列文件（含 .env.[mode] 覆盖）
  const env = loadEnv(mode, process.cwd(), '')
  return {
    server: {
      proxy: {
        // 配置文件中读取 VITE_API_BASE，实现代理目标可配置化
        '/api': {
          target: env.VITE_API_BASE,
          changeOrigin: true,
        },
      },
    },
  }
})
```

讲解：`loadEnv(mode, envDir, prefix)` 的第三个参数是前缀过滤，传 `''` 表示加载全部变量（默认只加载 `VITE_` 前缀）；第二个参数 `process.cwd()` 指定 `.env` 所在目录。注意配置文件加载的 `.env` 与暴露给客户端的两者互不影响。

## 6. 环境模式（Mode）与 --mode 参数

`mode` 决定加载哪套 `.env` 文件：默认 `dev` 对应 `development`，`build` 对应 `production`。可以自定义模式跑出"测试环境"产物：

```bash
# 构建时使用 .env.staging（需提前创建该文件）
vite build --mode staging
```

讲解：`--mode staging` 会加载 `.env.staging` 与 `.env`（基础文件始终加载），同时 `import.meta.env.MODE` 变为 `'staging'`。多环境部署（dev / staging / prod）通常用这种方式管理。

## 7. 常见陷阱

陷阱一：改了 `.env` 不生效。环境变量在 dev server 启动时读取，修改后需重启。

陷阱二：别名与 tsconfig 不同步。报"找不到模块"时先检查 `paths` 是否与 `alias` 一致。

陷阱三：敏感信息泄漏。任何 `VITE_` 前缀变量都会进入产物，密钥必须放服务端。

陷阱四：动态访问环境变量。`import.meta.env['VITE_X']` 不会被替换，返回 undefined。

## 8. 参考资源

Vite 配置文档：https://vite.dev/config/

Vite 环境变量与模式：https://vite.dev/guide/env-and-mode

Vite 中文文档：https://cn.vite.dev/
