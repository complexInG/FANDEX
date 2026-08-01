---
order: 230
title: 编程入门 Node.js 安装
module: getting-started

category: '001-getting-started'
difficulty: beginner
description: 编程入门 Node.js 安装 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Windows 安装

**基本写法：winget 安装 Node.js LTS**
`winget install OpenJS.NodeJS.LTS`
```bash
# 通过 Windows 包管理器安装 LTS 版本
winget install OpenJS.NodeJS.LTS
```

---

**基本写法：winget 安装指定版本**
`winget install OpenJS.NodeJS -v <版本号>`
```bash
# 安装指定版本（如 22.11.0）
winget install OpenJS.NodeJS -v 22.11.0
```

---

**基本写法：升级 Node.js**
`winget upgrade OpenJS.NodeJS`
```bash
# 升级到最新版本
winget upgrade OpenJS.NodeJS
```

---

## macOS 安装

**基本写法：Homebrew 安装 Node.js**
`brew install node`
```bash
# 通过 Homebrew 安装最新版
brew install node
```

---

**基本写法：Homebrew 安装 LTS 版本**
`brew install node@22`
```bash
# 安装 LTS 长期支持版本
brew install node@22
```

---

**基本写法：升级 Node.js（macOS）**
`brew upgrade node`
```bash
# 通过 Homebrew 升级 Node.js
brew upgrade node
```

---

## Linux 安装（NodeSource）

**基本写法：Ubuntu/Debian 安装 LTS**
`curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -`
```bash
# 添加 NodeSource LTS 源（第一步）
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
```

---

**基本写法：apt 安装 Node.js**
`sudo apt-get install -y nodejs`
```bash
# 安装 Node.js 和 npm（第二步）
sudo apt-get install -y nodejs
```

---

## nvm 安装方式

**基本写法：nvm 安装脚本（Linux/macOS）**
`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | bash`
```bash
# 安装 nvm 版本管理器
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | bash
```

---

**基本写法：加载 nvm**
`\. "$HOME/.nvm/nvm.sh"`
```bash
# 在当前 shell 中加载 nvm
\. "$HOME/.nvm/nvm.sh"
```

---

**基本写法：nvm 安装指定版本**
`nvm install <版本号>`
```bash
# 安装指定 Node.js 版本
nvm install 24
```

---

**基本写法：nvm 安装 LTS 版本**
`nvm install --lts`
```bash
# 安装最新 LTS 版本
nvm install --lts
```

---

## 安装验证

**基本写法：验证 Node.js 安装**
`node -v`
```bash
# 应输出 v24.18.1 类似版本号
node -v
```

---

**基本写法：验证 npm 安装**
`npm -v`
```bash
# 应输出 11.16.0 类似版本号
npm -v
```

---

**基本写法：运行测试脚本**
`node -e "console.log('Node.js 运行正常')"`
```bash
# 直接执行 Node.js 代码验证运行时
node -e "console.log('Node.js 运行正常')"
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
| 编程入门 Node.js 安装 | 023-NodeJsInstall | 本文自身 |
| 编程入门 npm 包管理 | 024-NpmManager | 本文的前置基础 |
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
