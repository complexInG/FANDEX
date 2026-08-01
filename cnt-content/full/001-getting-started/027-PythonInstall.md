---
order: 270
title: 编程入门 Python 安装
module: 001-getting-started
category: '001-getting-started'
difficulty: beginner
description: 编程入门 Python 安装 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 编程入门 Python 安装

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Windows 安装

**基本写法：winget 安装 Python**
`winget install Python.Python.3.13`
```bash
# 通过 Windows 包管理器安装 Python 3.13
winget install Python.Python.3.13
```

---

**基本写法：winget 安装指定版本**
`winget install Python.Python.3 -v <版本号>`
```bash
# 安装指定版本（如 3.12.8）
winget install Python.Python.3 -v 3.12.8
```

---

**基本写法：升级 Python**
`winget upgrade Python.Python.3`
```bash
# 升级到最新版本
winget upgrade Python.Python.3
```

---

## macOS 安装

**基本写法：Homebrew 安装 Python**
`brew install python@3.13`
```bash
# 通过 Homebrew 安装 Python 3.13
brew install python@3.13
```

---

**基本写法：升级 Python（macOS）**
`brew upgrade python`
```bash
# 通过 Homebrew 升级 Python
brew upgrade python
```

---

## Linux 安装

**基本写法：apt 安装 Python（Ubuntu/Debian）**
`sudo apt-get install python3 python3-pip`
```bash
# 安装 Python 3 和 pip
sudo apt-get install python3 python3-pip
```

---

**基本写法：yum 安装 Python（CentOS/RHEL）**
`sudo yum install python3 python3-pip`
```bash
# 安装 Python 3 和 pip
sudo yum install python3 python3-pip
```

---

**基本写法：源码编译安装**
`./configure && make && sudo make install`
```bash
# 从源码编译安装指定版本
./configure --enable-optimizations && make && sudo make install
```

---

## Python Launcher（Windows）

**基本写法：查看已安装 Python 版本**
`py -0`
```bash
# 列出 Windows 上所有已安装的 Python 版本
py -0
```

---

**基本写法：使用指定版本运行**
`py -<版本号> <脚本>`
```bash
# 使用 Python 3.11 运行脚本
py -3.11 script.py
```

---

**基本写法：查看版本详情**
`py -0p`
```bash
# 列出所有版本及其安装路径
py -0p
```

---

## 安装验证

**基本写法：验证 Python 安装**
`python --version`
```bash
# 应输出 Python 3.13.x 类似版本号
python --version
```

---

**基本写法：验证 pip 安装**
`pip --version`
```bash
# 应输出 pip 24.x 类似版本号
pip --version
```

---

**基本写法：运行测试脚本**
`python -c "print('Python 运行正常')"`
```bash
# 直接执行 Python 代码验证运行时
python -c "print('Python 运行正常')"
```

---

## pip 升级

**基本写法：升级 pip**
`python -m pip install --upgrade pip`
```bash
# 升级 pip 到最新版本
python -m pip install --upgrade pip
```

---

**基本写法：指定镜像源升级**
`pip install --upgrade pip -i <镜像地址>`
```bash
# 使用国内镜像加速升级
pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
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
| 编程入门 nvm 版本管理 | 026-NvmVersionManage | 本文的前置基础 |
| 编程入门 Python 安装 | 027-PythonInstall | 本文自身 |
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
