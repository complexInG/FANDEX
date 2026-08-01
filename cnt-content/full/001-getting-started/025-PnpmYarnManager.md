---
order: 250
title: 编程入门 pnpm 与 yarn 包管理
module: getting-started

category: '001-getting-started'
difficulty: beginner
description: 编程入门 pnpm 与 yarn 包管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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

## 参考文献

本模块各文档：环境搭建、编程基础、调试思维等。
MDN 学习区：https://developer.mozilla.org/zh-CN/docs/Learn_web_development
freeCodeCamp：https://www.freecodecamp.org/chinese/
黑马程序员官网：https://www.itheima.com/

## 延伸阅读

从入门到进阶路径：001 入门 -> 002 Markdown -> 003 Git -> 006 HTML -> 007 CSS -> 008 JS。
语言进阶：013 Java / 040 Python / 016 Go 按兴趣选择。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供基础课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 如何高效自学编程

目标驱动：每个阶段一个小项目（计算器、笔记、网站）。
费曼技巧：把学到的知识写出来或讲出来。
刻意练习：专注薄弱点，带反馈循环。
社区参与：提问、回答、代码评审加速成长。

### 13.2 学习路径规划

阶段一（2-4 周）：环境 + 基础语法 + 小练习。
阶段二（4-8 周）：数据结构 + 简单项目。
阶段三（2-3 月）：框架 + 实战项目 + 部署。
持续：算法刷题、源码阅读、开源贡献。
