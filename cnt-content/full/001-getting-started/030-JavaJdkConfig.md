---
order: 300
title: 编程入门 Java JDK 配置
module: 001-getting-started
category: '001-getting-started'
difficulty: beginner
description: 编程入门 Java JDK 配置 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Windows 安装

**基本写法：winget 安装 Microsoft OpenJDK**
`winget install Microsoft.OpenJDK.21`
```bash
# 安装 Microsoft Build of OpenJDK 21
winget install Microsoft.OpenJDK.21
```

---

**基本写法：winget 安装 Eclipse Temurin**
`winget install EclipseAdoptium.Temurin.21.JDK`
```bash
# 安装 Eclipse Temurin 21 版本
winget install EclipseAdoptium.Temurin.21.JDK
```

---

**基本写法：winget 安装指定 JDK 版本**
`winget install Microsoft.OpenJDK.17`
```bash
# 安装 JDK 17 LTS 版本
winget install Microsoft.OpenJDK.17
```

---

## macOS 安装

**基本写法：Homebrew 安装 Temurin**
`brew install --cask temurin@21`
```bash
# 通过 Homebrew 安装 Temurin 21
brew install --cask temurin@21
```

---

**基本写法：Homebrew 安装最新 JDK**
`brew install --cask temurin`
```bash
# 安装最新版本的 Temurin
brew install --cask temurin
```

---

## Linux 安装

**基本写法：apt 安装 OpenJDK（Ubuntu/Debian）**
`sudo apt-get install openjdk-21-jdk`
```bash
# 安装 OpenJDK 21
sudo apt-get install openjdk-21-jdk
```

---

**基本写法：yum 安装 OpenJDK（CentOS/RHEL）**
`sudo yum install java-21-openjdk-devel`
```bash
# 安装 OpenJDK 21 开发包
sudo yum install java-21-openjdk-devel
```

---

## 环境变量配置（Windows）

**基本写法：设置 JAVA_HOME（CMD）**
`setx JAVA_HOME "<JDK路径>"`
```bash
# 永久设置 JAVA_HOME 环境变量
setx JAVA_HOME "C:\Program Files\Microsoft\jdk-21"
```

---

**基本写法：设置 JAVA_HOME（PowerShell）**
`[Environment]::SetEnvironmentVariable("JAVA_HOME", "<JDK路径>", "User")`
```bash
# PowerShell 用户级环境变量设置
[Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Program Files\Microsoft\jdk-21", "User")
```

---

**基本写法：将 JAVA_HOME\bin 加入 PATH**
`setx PATH "%PATH%;%JAVA_HOME%\bin"`
```bash
# 将 JDK 的 bin 目录追加到 PATH
setx PATH "%PATH%;%JAVA_HOME%\bin"
```

---

**基本写法：PowerShell 追加 PATH**
`[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";%JAVA_HOME%\bin", "User")`
```bash
# PowerShell 方式追加 PATH 环境变量
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";$env:JAVA_HOME\bin", "User")
```

---

## 环境变量配置（Linux/macOS）

**基本写法：bash 配置 JAVA_HOME**
`export JAVA_HOME=<JDK路径>`
```bash
# 写入 ~/.bashrc 或 ~/.bash_profile
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
```

---

**基本写法：bash 追加 PATH**
`export PATH=$JAVA_HOME/bin:$PATH`
```bash
# 将 JDK bin 目录加入 PATH
export PATH=$JAVA_HOME/bin:$PATH
```

---

**基本写法：macOS 使用 java_home 工具**
`/usr/libexec/java_home -v <版本号>`
```bash
# 获取指定版本的 JDK 路径
/usr/libexec/java_home -v 21
```

---

## 安装验证

**基本写法：验证 Java 运行时**
`java -version`
```bash
# 应输出 openjdk version "21" 类似信息
java -version
```

---

**基本写法：验证 Java 编译器**
`javac -version`
```bash
# 验证 JDK 编译器是否可用
javac -version
```

---

**基本写法：验证 JAVA_HOME**
`echo %JAVA_HOME%`
```bash
# 查看已设置的 JAVA_HOME 路径
echo %JAVA_HOME%
```

---

**基本写法：运行测试程序**
`java -e "System.out.println(\"Java 运行正常\")"`
```bash
# 直接执行 Java 单行代码（JDK 22+）
java -e "System.out.println(\"Java 运行正常\")"
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
| 编程入门 pip 与 venv 包管理 | 028-PipVenvManager | 本文的前置基础 |
| 编程入门 pyenv 与 uv 版本管理 | 029-PyenvUvManage | 本文的前置基础 |
| 编程入门 Java JDK 配置 | 030-JavaJdkConfig | 本文自身 |
| 编程入门 VS Code 安装配置 | 031-VSCodeInstall | 本文的前置基础 |
| 编程入门 Git 安装配置 | 032-GitInstallConfig | 本文的前置基础 |
| 编程入门 Docker 安装 | 033-DockerInstall | 本文的前置基础 |
| 文本处理命令速查手册 | 034-TextProcessing | 本文的并列主题 |
| 管道与重定向速查手册 | 035-PipeRedirect | 本文的并列主题 |
| 进程管理命令速查手册 | 036-ProcessManage | 本文的并列主题 |
| 压缩解压命令速查手册 | 037-CompressArchive | 本文的并列主题 |
