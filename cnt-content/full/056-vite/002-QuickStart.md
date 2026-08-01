---
order: 2
title: Vite 快速上手与项目结构
module: vite
category: Vite
difficulty: beginner
description: 'Vite 快速上手：创建项目、目录结构、三个核心命令与 ESM 加速原理'
author: fanquanpp
updated: '2026-08-01'
related:
  - vite/003-ConfigFile
  - vite/004-StaticAssets
  - vite/006-DevServerHMR
prerequisites:
  - javascript/005-ControlFlow
---
## 1. 写在前面

Vite 是目前主流的下一代前端构建工具。本文面向零基础读者，目标是：花 10 分钟跑通一个 Vite 项目，并理解它"为什么快"。阅读本文前建议先通读 001 篇《Vite 构建工具概述》，掌握基本概念。

动手之前，请确认环境满足两个条件：

| 环境项 | 要求 | 说明 |
| --- | --- | --- |
| Node.js | 20.19+ 或 22.12+ | Vite 8 要求较新的 Node 版本，可用 `node -v` 检查 |
| 包管理器 | pnpm 9+ / npm 10+ / yarn 4+ | 本文统一使用 pnpm |

Vite 官方文档（中文）：https://cn.vite.dev/

## 2. 创建第一个项目

使用官方脚手架命令，一行代码即可创建项目：

```bash
# 交互式创建：会提示输入项目名、选择框架与语言
pnpm create vite my-vite-app
# 直接指定框架模板，跳过交互
pnpm create vite my-vite-app --template react-ts
```

讲解：`pnpm create vite` 会拉取官方模板到 `my-vite-app` 目录。第二条命令通过 `--template` 直接指定模板，常见模板有 `vanilla`（原生 JS）、`vanilla-ts`、`vue`、`vue-ts`、`react`、`react-ts`、`svelte-ts` 等。Vite 8 还支持通过 `--template` 组合前端框架与后端框架（如 `--template react-ts-nest`）。

进入项目并安装依赖：

```bash
cd my-vite-app
pnpm install
```

讲解：脚手架只生成骨架，依赖需要单独安装。安装完成后即可运行，无需任何额外配置。

## 3. 项目目录结构

以 `react-ts` 模板为例，核心文件如下：

```text
my-vite-app/
├── index.html          # 页面入口 HTML（唯一的 HTML 文件）
├── package.json        # 依赖与脚本
├── vite.config.ts      # Vite 配置文件（本模块 003 篇详解）
├── tsconfig.json       # TypeScript 配置
├── public/             # 公共静态资源（本模块 004 篇详解）
└── src/
    ├── main.tsx        # 应用入口，挂载到 #root
    ├── App.tsx         # 根组件
    ├── App.css         # 组件样式
    └── assets/         # 需要构建处理的资源
```

讲解：注意 `index.html` 位于项目根目录而非 `src` 内，这是 Vite 与传统脚手架（如 CRA）的重要差异。`index.html` 中通过 `<script type="module" src="/src/main.tsx">` 引用源码入口，浏览器会直接以原生 ESM 方式加载它。

```html
<!-- index.html（模板默认内容节选） -->
<div id="root"></div>
<script type="module" src="/src/main.tsx"></script>
```

讲解：`type="module"` 告诉浏览器按 ES Module 规范加载脚本。`src/main.tsx` 中再通过 `import` 递归引用其他模块，Vite 的开发服务器会拦截并即时转换这些请求。

## 4. 三个核心命令

脚手架在 `package.json` 中预置了脚本，全部围绕三个命令展开：

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

| 命令 | 对应脚本 | 作用 | 产物 |
| --- | --- | --- | --- |
| `pnpm dev` | `vite` | 启动开发服务器，默认端口 5173 | 无（内存中运行） |
| `pnpm build` | `vite build` | 生产构建，生成优化产物 | `dist/` 目录 |
| `pnpm preview` | `vite preview` | 本地预览构建产物 | 读取 `dist/` |

三者关系可以用一句话概括：**开发用 dev，上线前 build，验证产物用 preview**。

```bash
pnpm dev       # 终端会输出 Local: http://localhost:5173/
pnpm build     # 输出 dist/ 及每个 chunk 的体积报告
pnpm preview   # 以 4173 端口预览 dist/ 产物
```

讲解：`preview` 模拟生产环境的静态服务器，专门用于检查 build 产物是否正确（资源路径、分包、CDN 部署等），避免"本地正常、上线 404"。

## 5. 为什么快：ESM 与依赖预构建

Vite 的"快"来自两项核心技术，理解它们比记住命令更重要。

### 5.1 原生 ES Modules：按需编译

传统打包器（如 Webpack）在启动时会把整个项目打包成一个 bundle，项目越大启动越慢。Vite 反其道而行：开发阶段**不打包**，浏览器直接通过 `<script type="module">` 加载源码，Vite 只对"浏览器当前请求的那个文件"做即时转换。

```text
传统方式：所有源码 -> 打包成一个 bundle -> 浏览器下载
Vite 方式：浏览器按需请求每个模块 -> Vite 逐个转换 -> 浏览器执行
```

讲解：因此冷启动速度与项目规模几乎无关，只取决于浏览器并发请求模块的速度。修改代码后也只重传被影响的模块，这就是 HMR 毫秒级响应的基础。

### 5.2 依赖预构建

`node_modules` 中的第三方依赖大多不是浏览器可直接加载的 ESM（可能是 CommonJS，或由成百上千个小文件组成）。Vite 在启动时会用打包器把这些依赖**预构建**成单个 ESM 文件，缓存在 `node_modules/.vite` 目录。

```text
依赖预构建的两大收益：
1. 兼容性：CommonJS / UMD 依赖转为浏览器可识别的 ESM
2. 性能：数百个小模块合并为一个请求，浏览器只需加载一次
```

讲解：预构建只针对 `node_modules`，源码仍按需转换。若修改依赖版本或升级 Vite，缓存可能失效，删除 `node_modules/.vite` 后重启即可重建。

## 6. 修改第一个页面

打开 `src/App.tsx`，替换为以下内容（JS 项目则用 `.js`）：

```tsx
import './App.css'

function App() {
  return (
    <div className="card">
      <h1>Hello Vite</h1>
      <p>保存文件后，浏览器会自动热更新，无需手动刷新。</p>
    </div>
  )
}

export default App
```

讲解：保存文件后观察浏览器——页面内容即时更新且不会丢失状态，这正是 Vite 的 HMR 特性（006 篇详述）。`import './App.css'` 直接在组件中引入样式，Vite 会自动处理。

## 7. 常见问题

问题一：端口被占用。`pnpm dev` 会自动改用下一个可用端口（5174、5175...），无需处理。

问题二：Windows 上 pnpm 不可用。安装 Node.js 后执行 `corepack enable` 启用内置 pnpm。

问题三：模板默认内容太多。删除 `src` 下不需要的文件与 `public` 中的 logo，保持目录干净。

问题四：编辑器报模块找不到。先确认 `pnpm install` 执行成功，再重启编辑器让 TS 服务重新加载。

## 8. 参考资源

Vite 官方文档：https://vite.dev/guide/

Vite 中文文档：https://cn.vite.dev/guide/

create-vite 模板列表：https://github.com/vitejs/vite/tree/main/packages/create-vite
