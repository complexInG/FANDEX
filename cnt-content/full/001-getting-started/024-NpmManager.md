---
order: 240
title: 编程入门 npm 包管理
module: getting-started

category: '001-getting-started'
difficulty: beginner
description: 编程入门 npm 包管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 项目初始化

**基本写法：交互式创建 package.json**
`npm init`
```bash
# 通过问答方式初始化项目
npm init
```

---

**基本写法：快速创建默认 package.json**
`npm init -y`
```bash
# 跳过问答使用默认值
npm init -y
```

---

**基本写法：创建 package.json 并指定版本管理工具**
`npm create <模板名>@latest`
```bash
# 使用官方模板初始化项目
npm create vite@latest my-app
```

---

## 包安装

**基本写法：安装依赖（生产依赖）**
`npm install <包名>`
```bash
# 安装到 dependencies
npm install express
```

---

**基本写法：安装开发依赖**
`npm install <包名> --save-dev`
```bash
# 安装到 devDependencies
npm install eslint --save-dev
```

---

**基本写法：全局安装包**
`npm install -g <包名>`
```bash
# 全局安装命令行工具
npm install -g typescript
```

---

**基本写法：安装指定版本**
`npm install <包名>@<版本号>`
```bash
# 安装指定版本的包
npm install lodash@4.17.21
```

---

**基本写法：安装全部依赖**
`npm install`
```bash
# 根据 package.json 安装所有依赖
npm install
```

---

## 包管理

**基本写法：卸载包**
`npm uninstall <包名>`
```bash
# 移除项目中的包
npm uninstall express
```

---

**基本写法：更新包**
`npm update <包名>`
```bash
# 更新指定包到最新版本
npm update lodash
```

---

**基本写法：查看已安装包列表**
`npm list`
```bash
# 查看当前项目的依赖树
npm list
```

---

**基本写法：查看全局安装包**
`npm list -g --depth=0`
```bash
# 查看全局安装的包（不显示依赖）
npm list -g --depth=0
```

---

**基本写法：查看包信息**
`npm view <包名>`
```bash
# 查看包的详细信息
npm view react
```

---

## 脚本执行

**基本写法：运行 package.json 中的脚本**
`npm run <脚本名>`
```bash
# 执行 scripts 中定义的命令
npm run build
```

---

**基本写法：运行 start 脚本**
`npm start`
```bash
# start 是特殊脚本名可省略 run
npm start
```

---

**基本写法：运行 test 脚本**
`npm test`
```bash
# test 是特殊脚本名可省略 run
npm test
```

---

**基本写法：传递参数给脚本**
`npm run <脚本名> -- <参数>`
```bash
# 向脚本传递额外参数
npm run build -- --mode production
```

---

## 配置管理

**基本写法：设置 npm 镜像源**
`npm config set registry <镜像地址>`
```bash
# 切换为淘宝镜像加速下载
npm config set registry https://registry.npmmirror.com/
```

---

**基本写法：查看当前镜像源**
`npm config get registry`
```bash
# 查看当前使用的镜像源
npm config get registry
```

---

**基本写法：查看所有配置**
`npm config list`
```bash
# 查看所有 npm 配置项
npm config list
```

---

**基本写法：设置全局安装路径**
`npm config set prefix "<路径>"`
```bash
# 自定义全局包安装路径
npm config set prefix "D:\npm-global"
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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 入门指南 | 001-GettingStartedGuide | 本文的前置基础 |
| 开发环境搭建 | 002-DevEnvSetup | 本文的前置基础 |
| 学习指南 | 003-LearningGuide | 本文的并列主题 |
| 计算机体系结构 | 004-ComputerArchitecture | 本文的并列主题 |
| 数的表示与编码 | 005-NumberRepresentationEncoding | 本文的并列主题 |
| 程序设计基础 | 006-ProgrammingBasics | 本文的前置基础 |
| 函数与模块化 | 007-FunctionModular | 本文的并列主题 |
| 学习路线规划 | 008-LearningPathPlanning | 本文的并列主题 |
| 环境变量与PATH | 009-EnvVarPath | 本文的前置基础 |
| IDE与编辑器选型 | 010-IDEEditorSelection | 本文的并列主题 |
| 插件生态 | 011-PluginEcosystem | 本文的并列主题 |
| 命令行基础 | 012-CommandLineBasics | 本文的前置基础 |
| 包管理器 | 013-PackageManager | 本文的并列主题 |
| 版本控制系统选型 | 014-VCSSelection | 本文的并列主题 |
| 项目初始化 | 015-ProjectInit | 本文的综合应用 |
| 构建工具 | 016-BuildTool | 本文的并列主题 |
| 编程范式基础 | 017-ProgrammingParadigmBasics | 本文的前置基础 |
| 调试思想 | 018-DebugThinking | 本文的并列主题 |
| 软件下载地址汇总 | 019-SoftwareDownloadURLSummary | 本文的并列主题 |
| Windows环境配置教程 | 020-WindowsEnvConfigTutorial | 本文的前置基础 |
| macOS环境配置教程 | 021-MacOSEnvConfigTutorial | 本文的前置基础 |
| Linux环境配置教程 | 022-LinuxEnvConfigTutorial | 本文的前置基础 |
| 编程入门 Node.js 安装 | 023-NodeJsInstall | 本文的前置基础 |
| 编程入门 npm 包管理 | 024-NpmManager | 本文自身 |
| 编程入门 pnpm 与 yarn 包管理 | 025-PnpmYarnManager | 本文的前置基础 |
| 编程入门 nvm 版本管理 | 026-NvmVersionManage | 本文的前置基础 |
| 编程入门 Python 安装 | 027-PythonInstall | 本文的前置基础 |
| 编程入门 pip 与 venv 包管理 | 028-PipVenvManager | 本文的前置基础 |
| 编程入门 pyenv 与 uv 版本管理 | 029-PyenvUvManage | 本文的前置基础 |
| 编程入门 Java JDK 配置 | 030-JavaJdkConfig | 本文的前置基础 |
| 编程入门 VS Code 安装配置 | 031-VSCodeInstall | 本文的前置基础 |
| 编程入门 Git 安装配置 | 032-GitInstallConfig | 本文的前置基础 |
| 编程入门 Docker 安装 | 033-DockerInstall | 本文的前置基础 |
| 文本处理命令速查手册 | 034-TextProcessing | 本文的并列主题 |
| 管道与重定向速查手册 | 035-PipeRedirect | 本文的并列主题 |
| 进程管理命令速查手册 | 036-ProcessManage | 本文的并列主题 |
| 压缩解压命令速查手册 | 037-CompressArchive | 本文的并列主题 |
