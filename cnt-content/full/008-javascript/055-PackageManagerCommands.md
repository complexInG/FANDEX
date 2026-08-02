---
order: 550
title: JavaScript 包管理命令速查（npm/pnpm/yarn）
module: javascript

category: '008-javascript'
difficulty: beginner
description: JavaScript 包管理命令速查（npm/pnpm/yarn） 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 初始化项目

**基本写法：生成 package.json**
`npm init [-y]` | `pnpm init` | `yarn init [-y]`
```bash
# -y 使用默认值跳过提问
npm init -y
pnpm init
yarn init -y
```

---

## 安装依赖

**基本写法：安装全部依赖**
`npm install` | `pnpm install` | `yarn`
```bash
# 读取 lock 文件安装
npm install        # npm
pnpm install       # pnpm
yarn               # yarn
```

---

**基本写法：添加单个包**
`npm install <包> [-D|-g]`
```bash
# -D 开发依赖 -g 全局
npm install lodash            # 生产依赖
npm install -D vitest         # 开发依赖
npm install -g typescript     # 全局安装
pnpm add lodash
pnpm add -D vitest
yarn add lodash
yarn add --dev vitest
```

---

**基本写法：指定版本安装**
`npm install <包>@<版本>`
```bash
# 版本范围
npm install react@18.2.0
npm install react@"^18.0.0"
npm install react@latest
pnpm add react@18.2.0
yarn add react@18.2.0
```

---

## 卸载与更新

**基本写法：卸载依赖**
`npm uninstall <包>` | `pnpm remove <包>` | `yarn remove <包>`
```bash
npm uninstall lodash
pnpm remove lodash
yarn remove lodash
```

---

**基本写法：更新依赖**
`npm update [<包>]` | `pnpm update [<包>]` | `yarn upgrade [<包>]`
```bash
npm update react
pnpm update react
yarn upgrade react
```

---

## 运行脚本

**基本写法：执行 package.json scripts**
`npm run <脚本>` | `pnpm <脚本>` | `yarn <脚本>`
```bash
# package.json: "scripts": { "dev": "vite" }
npm run dev
pnpm dev          # pnpm 可省略 run
yarn dev          # yarn 也可省略 run
```

---

**基本写法：npx 执行本地命令**
`npx <命令>`
```bash
# 执行 node_modules/.bin 下的命令
npx tsc --noEmit
npx create-vite my-app
pnpm dlx create-vite my-app   # pnpm 等价
yarn dlx create-vite my-app
```

---

## 锁文件与严格安装

**基本写法：按 lock 文件严格安装**
`npm ci` | `pnpm install --frozen-lockfile` | `yarn install --frozen-lockfile`
```bash
# CI 环境推荐，不修改 lock
npm ci
pnpm install --frozen-lockfile
yarn install --frozen-lockfile
```

---

## 工作区 Monorepo

**基本写法：定义工作区**
`<根 package.json>: "workspaces": ["packages/*"]`
```json
{
  "private": true,
  "workspaces": ["packages/*", "apps/*"]
}
```

---

**基本写法：工作区命令**
`npm -w <包> <命令>` | `pnpm --filter <包> <命令>` | `yarn workspace <包> <命令>`
```bash
# 在指定工作区执行
npm -w @a/core run build
pnpm --filter @a/core build
yarn workspace @a/core build
```

---

**基本写法：安装工作区包**
`npm -w <包A> i <包B>` | `pnpm add <包B> --filter <包A>`
```bash
# 给 app 安装内部包
npm -w apps/web i @a/core
pnpm add @a/core --filter apps/web
yarn workspace apps/web add @a/core
```

---

## 查询信息

**基本写法：查看包信息**
`npm view <包> [<字段>]`
```bash
npm view react version
npm view react versions --json
pnpm view react version
```

---

**基本写法：列出依赖树**
`npm ls [<包>]` | `pnpm list` | `yarn list`
```bash
npm ls react
npm ls --depth=1
pnpm why react    # 解释为何依赖
```

---

## 清理与缓存

**基本写法：清理 node_modules**
`rm -rf node_modules` + 重装
```bash
# 彻底重装
rm -rf node_modules package-lock.json
npm install
```

---

**基本写法：缓存管理**
`npm cache clean --force` | `pnpm store prune`
```bash
npm cache clean --force
pnpm store prune
yarn cache clean
```

---

## 发布与镜像

**基本写法：设置镜像源**
`npm config set registry <url>`
```bash
npm config set registry https://registry.npmmirror.com
npm config get registry
pnpm config set registry https://registry.npmmirror.com
```

---

**基本写法：发布包**
`npm publish`
```bash
npm publish           # 发布到 registry
npm publish --access public  # 公开 scoped 包
npm deprecate <包>@<版本> "废弃说明"
```

---

## pnpm 硬链接特性

**基本写法：pnpm 全局存储**
`pnpm config set store-dir <路径>`
```bash
# pnpm 用硬链接复用全局存储，节省磁盘
pnpm config get store-dir
pnpm install   # 自动链接 store
```

---

## 延伸阅读
JavaScript 基础语法，见 008-javascript 模块文档。
TypeScript 类型系统，见 009-typescript 模块。
浏览器 DOM 与事件，见 006-html5/007-css 模块。
前端框架 React/Vue，见 011-react/010-vue3 模块。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 事件循环深入

宏任务：script、setTimeout、setInterval、I/O、UI 渲染；微任务：Promise.then、queueMicrotask、MutationObserver。
每轮循环：执行一个宏任务，清空整个微任务队列，必要时渲染；微任务中产生的微任务继续执行，可能饿死宏任务。
Node 的事件循环分阶段：timers、pending callbacks、idle、poll、check、close；process.nextTick 优先于微任务。
调试技巧：用 Performance API 测量；async 栈追踪定位未处理拒绝。

### 13.2 this 与作用域

四种绑定：直接调用（undefined/global）、方法调用（对象）、call/apply/bind（显式）、箭头函数（词法）。
class 方法默认严格模式，事件回调中 this 丢失需绑定或箭头函数。
作用域链：全局 -> 模块 -> 函数 -> 块级（let/const）；闭包保留整个作用域链。
工程建议：避免 this 魔法，优先箭头函数与显式参数。
