---
order: 280
title: 编程入门 pip 与 venv 包管理
module: 001-getting-started
category: '001-getting-started'
difficulty: beginner
description: 编程入门 pip 与 venv 包管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 编程入门 pip 与 venv 包管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## pip 包安装

**基本写法：安装包**
`pip install <包名>`
```bash
# 安装指定的 Python 包
pip install requests
```

---

**基本写法：安装指定版本**
`pip install <包名>==<版本号>`
```bash
# 安装指定版本的包
pip install django==5.0.6
```

---

**基本写法：批量安装依赖**
`pip install -r <需求文件>`
```bash
# 从 requirements.txt 安装所有依赖
pip install -r requirements.txt
```

---

**基本写法：从 git 仓库安装**
`pip install git+<仓库地址>`
```bash
# 直接从 GitHub 仓库安装包
pip install git+https://github.com/user/repo.git
```

---

## pip 包管理

**基本写法：卸载包**
`pip uninstall <包名>`
```bash
# 移除已安装的包
pip uninstall requests
```

---

**基本写法：查看已安装包**
`pip list`
```bash
# 列出所有已安装的包
pip list
```

---

**基本写法：查看包详情**
`pip show <包名>`
```bash
# 查看指定包的详细信息
pip show django
```

---

**基本写法：导出依赖列表**
`pip freeze > requirements.txt`
```bash
# 导出当前环境所有依赖到文件
pip freeze > requirements.txt
```

---

**基本写法：升级包**
`pip install --upgrade <包名>`
```bash
# 升级包到最新版本
pip install --upgrade requests
```

---

## 镜像源配置

**基本写法：使用清华镜像源安装**
`pip install <包名> -i <镜像地址>`
```bash
# 使用清华大学镜像源加速下载
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

**基本写法：永久设置镜像源**
`pip config set global.index-url <镜像地址>`
```bash
# 永久切换为清华镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

---

**基本写法：查看当前配置**
`pip config list`
```bash
# 查看 pip 的所有配置项
pip config list
```

---

## venv 虚拟环境

**基本写法：创建虚拟环境**
`python -m venv <环境名>`
```bash
# 在当前目录创建虚拟环境
python -m venv .venv
```

---

**基本写法：激活虚拟环境（Windows）**
`<环境名>\Scripts\activate`
```bash
# Windows 下激活虚拟环境
.venv\Scripts\activate
```

---

**基本写法：激活虚拟环境（Linux/macOS）**
`source <环境名>/bin/activate`
```bash
# Linux/macOS 下激活虚拟环境
source .venv/bin/activate
```

---

**基本写法：退出虚拟环境**
`deactivate`
```bash
# 退出当前虚拟环境
deactivate
```

---

**基本写法：指定 Python 版本创建环境**
`py -<版本号> -m venv <环境名>`
```bash
# 使用 Python 3.11 创建虚拟环境
py -3.11 -m venv .venv311
```

---

## pipx 全局工具安装

**基本写法：安装 pipx**
`pip install pipx`
```bash
# 安装 pipx 用于管理全局命令行工具
pip install pipx
```

---

**基本写法：安装命令行工具**
`pipx install <包名>`
```bash
# 在隔离环境中安装 CLI 工具
pipx install black
```

---

**基本写法：运行临时工具**
`pipx run <包名> <参数>`
```bash
# 临时运行而不安装
pipx run cowsay "hello"
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
| 编程入门 Python 安装 | 027-PythonInstall | 本文的前置基础 |
| 编程入门 pip 与 venv 包管理 | 028-PipVenvManager | 本文自身 |
| 编程入门 pyenv 与 uv 版本管理 | 029-PyenvUvManage | 本文的前置基础 |
| 编程入门 Java JDK 配置 | 030-JavaJdkConfig | 本文的前置基础 |
| 编程入门 VS Code 安装配置 | 031-VSCodeInstall | 本文的前置基础 |
| 编程入门 Git 安装配置 | 032-GitInstallConfig | 本文的前置基础 |
| 编程入门 Docker 安装 | 033-DockerInstall | 本文的前置基础 |
| 文本处理命令速查手册 | 034-TextProcessing | 本文的并列主题 |
| 管道与重定向速查手册 | 035-PipeRedirect | 本文的并列主题 |
| 进程管理命令速查手册 | 036-ProcessManage | 本文的并列主题 |
| 压缩解压命令速查手册 | 037-CompressArchive | 本文的并列主题 |
