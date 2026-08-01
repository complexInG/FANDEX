---
order: 10
tags:
  - 'getting-started'
difficulty: beginner
title: 开发环境搭建
module: 'getting-started'
category: Setup
description: 从零开始选择操作系统、安装编辑器和配置终端环境。
author: fanquanpp
related:
  - 'getting-started/入门指南'
  - 'getting-started/学习指南'
  - 'getting-started/计算机体系结构'
prerequisites: []
updated: '2026-08-01'
---
## 1. 选择操作系统

三大主流操作系统均可用于开发:

| 系统    | 优势                     | 适合场景                     |
| ------- | ------------------------ | ---------------------------- |
| Windows | 软件生态丰富, 游戏兼容好 | .NET开发、企业办公、通用开发 |
| macOS   | Unix底层, 前端工具链完善 | 前端开发、iOS开发、设计      |
| Linux   | 免费开源, 服务器环境一致 | 后端开发、运维、嵌入式       |

> 如果你是0基础, 使用当前电脑即可, 不需要专门更换操作系统. Windows用户可以通过WSL获得Linux环境.

## 2. 安装代码编辑器

推荐使用 **Visual Studio Code** (VS Code), 免费且功能强大.

### 2.1 下载安装

1. 访问 https://code.visualstudio.com
2. 点击下载对应系统版本
3. 运行安装程序, 勾选"添加到PATH"选项

### 2.2 必装扩展

安装完成后, 点击左侧扩展图标, 搜索并安装:

- **Chinese Language Pack** - 中文界面
- **GitLens** - Git增强工具
- **Prettier** - 代码格式化
- **ESLint** - JavaScript代码检查

## 3. 终端基础

终端是开发者最重要的工具之一.

### 3.1 打开终端

| 系统    | 方式                         |
| ------- | ---------------------------- |
| Windows | `Win + R` 输入 `powershell`  |
| macOS   | `Cmd + 空格` 输入 `terminal` |
| Linux   | `Ctrl + Alt + T`             |

### 3.2 常用命令

```bash
pwd           # 显示当前目录
ls            # 列出文件 (Windows: dir)
cd Documents  # 进入目录
cd ..         # 返回上级目录
mkdir project # 创建目录
clear         # 清屏 (Windows: cls)
```

### 3.3 Windows用户: 启用WSL

WSL (Windows Subsystem for Linux) 让你在Windows上运行Linux环境:

```powershell
wsl --install
```

安装后重启电脑, 即可使用Ubuntu终端.

## 4. 安装Git

Git是版本控制的基础工具, 后续模块会详细讲解.

### 4.1 安装方式

| 系统    | 命令                     |
| ------- | ------------------------ |
| Windows | 下载 https://git-scm.com |
| macOS   | `brew install git`       |
| Linux   | `sudo apt install git`   |

### 4.2 验证安装

```bash
git --version
```

显示版本号即安装成功.

## 5. 下一步

环境准备完成后, 建议按以下顺序开始学习:

1. **Markdown** - 学习文档编写基础
2. **Git** - 掌握版本控制
3. **GitHub** - 学会代码协作
## 工具链组成

**基本写法：查看 Node.js 版本**
`node --version`
```bash
# 验证 Node.js 是否安装成功
node --version
```

---

**基本写法：查看 Python 版本**
`python --version`
```bash
# 验证 Python 是否安装成功
python --version
```

---

**基本写法：查看 Java 版本**
`java -version`
```bash
# 验证 JDK 是否安装成功
java -version
```

---

**基本写法：查看 Git 版本**
`git --version`
```bash
# 验证 Git 是否安装成功
git --version
```

---

**基本写法：查看 Docker 版本**
`docker --version`
```bash
# 验证 Docker 是否安装成功
docker --version
```

---

**基本写法：查看 VS Code 版本**
`code --version`
```bash
# 验证 VS Code 命令行工具是否可用
code --version
```

---

## 包管理器识别

**基本写法：查看 npm 版本**
`npm --version`
```bash
# Node.js 默认包管理器
npm --version
```

---

**基本写法：查看 pnpm 版本**
`pnpm --version`
```bash
# 高性能 Node.js 包管理器
pnpm --version
```

---

**基本写法：查看 pip 版本**
`pip --version`
```bash
# Python 默认包管理器
pip --version
```

---

**基本写法：查看 uv 版本**
`uv --version`
```bash
# 新一代 Rust 实现的 Python 包管理器
uv --version
```

---

## 系统信息查询

**基本写法：查看操作系统信息（Windows）**
`systeminfo | findstr /B /C:"OS"`
```bash
# 查看 Windows 系统版本
systeminfo | findstr /B /C:"OS"
```

---

**基本写法：查看系统架构（Windows）**
`echo %PROCESSOR_ARCHITECTURE%`
```bash
# 查看处理器架构（x64 或 ARM64）
echo %PROCESSOR_ARCHITECTURE%
```

---

**基本写法：查看系统架构（跨平台）**
`uname -m`
```bash
# Linux/macOS 查看处理器架构
uname -m
```

---

## 环境变量检查

**基本写法：查看 PATH 环境变量（Windows）**
`echo %PATH%`
```bash
# 查看当前 PATH 环境变量
echo %PATH%
```

---

**基本写法：查看 PATH 环境变量（PowerShell）**
`$env:PATH`
```bash
# PowerShell 方式查看 PATH
$env:PATH
```

---

**基本写法：查看 JAVA_HOME**
`echo %JAVA_HOME%`
```bash
# 查看 Java 主目录环境变量
echo %JAVA_HOME%
```

---

**基本写法：查看所有环境变量（Windows）**
`set`
```bash
# 列出所有环境变量
set
```

---

**基本写法：查看所有环境变量（PowerShell）**
`Get-ChildItem Env:`
```bash
# PowerShell 列出所有环境变量
Get-ChildItem Env:
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
| 开发环境搭建 | 002-DevEnvSetup | 本文自身 |
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
