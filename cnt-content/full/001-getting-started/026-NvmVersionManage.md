---
order: 260
title: 编程入门 nvm 版本管理
module: 001-getting-started
category: '001-getting-started'
difficulty: beginner
description: 编程入门 nvm 版本管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## nvm-windows 安装

**基本写法：查看 nvm 版本**
`nvm version`
```bash
# 验证 nvm-windows 是否安装成功
nvm version
```

---

**基本写法：安装指定 Node.js 版本**
`nvm install <版本号>`
```bash
# 安装指定版本的 Node.js
nvm install 24.18.1
```

---

**基本写法：安装最新 LTS 版本**
`nvm install lts`
```bash
# 安装最新长期支持版本
nvm install lts
```

---

**基本写法：安装最新稳定版**
`nvm install stable`
```bash
# 安装最新稳定版本
nvm install stable
```

---

## 版本切换

**基本写法：切换 Node.js 版本**
`nvm use <版本号>`
```bash
# 切换到已安装的指定版本
nvm use 24.18.1
```

---

**基本写法：查看已安装版本列表**
`nvm list`
```bash
# 列出所有已安装的 Node.js 版本
nvm list
```

---

**基本写法：设置默认版本**
`nvm alias default <版本号>`
```bash
# 设置默认使用的 Node.js 版本
nvm alias default 24.18.1
```

---

**基本写法：卸载 Node.js 版本**
`nvm uninstall <版本号>`
```bash
# 删除指定版本的 Node.js
nvm uninstall 14.21.3
```

---

## nvm（Linux/macOS）

**基本写法：安装 Node.js LTS**
`nvm install --lts`
```bash
# 安装最新 LTS 版本
nvm install --lts
```

---

**基本写法：使用指定版本**
`nvm use <版本号>`
```bash
# 在当前 shell 切换 Node.js 版本
nvm use 22
```

---

**基本写法：查看所有已安装版本**
`nvm ls`
```bash
# 列出本地已安装的所有版本
nvm ls
```

---

**基本写法：查看可安装版本**
`nvm ls-remote`
```bash
# 列出所有可安装的远程版本
nvm ls-remote
```

---

**基本写法：设置默认版本**
`nvm alias default <版本号>`
```bash
# 设置默认 Node.js 版本
nvm alias default 22
```

---

## 项目版本锁定

**基本写法：在项目目录锁定版本**
`nvm use <版本号>`
```bash
# 在项目根目录创建 .nvmrc 后自动切换
echo "22" > .nvmrc
```

---

**基本写法：自动使用 .nvmrc 中的版本**
`nvm use`
```bash
# 读取 .nvmrc 文件并切换到指定版本
nvm use
```

---

## fnm 替代方案

**基本写法：fnm 安装 Node.js LTS**
`fnm install --lts`
```bash
# 使用 fnm 安装 LTS 版本（跨平台更快）
fnm install --lts
```

---

**基本写法：fnm 切换版本**
`fnm use lts-latest`
```bash
# 切换到最新的 LTS 版本
fnm use lts-latest
```

---

**基本写法：fnm 设置默认版本**
`fnm default <别名>`
```bash
# 设置默认 Node.js 版本别名
fnm default lts-latest
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
| 编程入门 npm 包管理 | 024-NpmManager | 本文的前置基础 |
| 编程入门 pnpm 与 yarn 包管理 | 025-PnpmYarnManager | 本文的前置基础 |
| 编程入门 nvm 版本管理 | 026-NvmVersionManage | 本文自身 |
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
