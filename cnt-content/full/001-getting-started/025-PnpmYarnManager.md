---
order: 160
title: pnpm 与 yarn 包管理
module: 'getting-started'
category: 工具链
difficulty: beginner
description: pnpm 与 yarn 的安装、常用命令及使用对比。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'getting-started/023-NodeJsInstall'
  - 'getting-started/024-NpmManager'
  - 'getting-started/026-NvmVersionManage'
prerequisites:
  - 'getting-started/002-DevEnvSetup'
---

## pnpm 安装

**基本写法：通过 npm 安装 pnpm**
`npm install -g pnpm`
```bash
# 全局安装 pnpm 包管理器
npm install -g pnpm
```

---

**基本写法：通过 winget 安装 pnpm**
`winget install pnpm.pnpm`
```bash
# Windows 包管理器安装 pnpm
winget install pnpm.pnpm
```

---

**基本写法：通过 Homebrew 安装 pnpm**
`brew install pnpm`
```bash
# macOS 通过 Homebrew 安装
brew install pnpm
```

---

**基本写法：通过独立脚本安装**
`curl -fsSL https://get.pnpm.io/install.sh | sh -`
```bash
# Linux/macOS 通过官方脚本安装
curl -fsSL https://get.pnpm.io/install.sh | sh -
```

---

## pnpm 常用命令

**基本写法：初始化项目**
`pnpm init`
```bash
# 创建 package.json 文件
pnpm init
```

---

**基本写法：安装依赖**
`pnpm install`
```bash
# 根据 package.json 安装所有依赖
pnpm install
```

---

**基本写法：添加生产依赖**
`pnpm add <包名>`
```bash
# 添加包到 dependencies
pnpm add express
```

---

**基本写法：添加开发依赖**
`pnpm add -D <包名>`
```bash
# 添加包到 devDependencies
pnpm add -D eslint
```

---

**基本写法：全局安装包**
`pnpm add -g <包名>`
```bash
# 全局安装命令行工具
pnpm add -g typescript
```

---

**基本写法：运行脚本**
`pnpm <脚本名>`
```bash
# 直接运行 scripts 中的命令
pnpm build
```

---

**基本写法：移除包**
`pnpm remove <包名>`
```bash
# 从项目中移除包
pnpm remove express
```

---

**基本写法：更新包**
`pnpm update <包名>`
```bash
# 更新指定包到最新版本
pnpm update lodash
```

---

## yarn 安装

**基本写法：通过 corepack 启用 yarn**
`corepack enable`
```bash
# Node.js 16+ 自带 corepack 管理工具
corepack enable
```

---

**基本写法：通过 npm 安装 yarn**
`npm install -g yarn`
```bash
# 全局安装 yarn 经典版本
npm install -g yarn
```

---

## yarn 常用命令

**基本写法：初始化项目**
`yarn init`
```bash
# 交互式创建 package.json
yarn init
```

---

**基本写法：安装依赖**
`yarn`
```bash
# 安装 package.json 中的所有依赖
yarn
```

---

**基本写法：添加生产依赖**
`yarn add <包名>`
```bash
# 添加包到 dependencies
yarn add express
```

---

**基本写法：添加开发依赖**
`yarn add -D <包名>`
```bash
# 添加包到 devDependencies
yarn add -D eslint
```

---

**基本写法：运行脚本**
`yarn <脚本名>`
```bash
# 运行 package.json 中的脚本
yarn build
```

---

**基本写法：移除包**
`yarn remove <包名>`
```bash
# 从项目中移除包
yarn remove express
```

---

**基本写法：升级包**
`yarn upgrade <包名>`
```bash
# 升级指定包到最新版本
yarn upgrade lodash
```
