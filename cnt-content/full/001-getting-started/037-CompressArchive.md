---
order: 370
title: 压缩解压命令速查手册
module: 001-getting-started
category: '001-getting-started'
difficulty: beginner
description: 压缩解压命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 压缩解压命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## tar 归档

**基本用法:创建归档**
`tar [选项] <归档名> <文件>`

```bash
# 打包为 .tar
tar -cvf archive.tar src/

# 打包并 gzip 压缩(.tar.gz)
tar -czvf project.tar.gz dist/

# 打包并 bzip2 压缩(压缩率更高)
tar -cjvf project.tar.bz2 dist/

# 打包并 xz 压缩
tar -cJvf project.tar.xz dist/
```

---

**基本用法:查看归档内容**
`tar -tvf <归档名>`

```bash
# 列出 tar.gz 内容不解压
tar -tzvf project.tar.gz
```

---

**基本用法:解压归档**
`tar -xvf <归档名>`

```bash
# 解压到当前目录
tar -xzvf project.tar.gz

# 解压到指定目录
tar -xzvf project.tar.gz -C /opt/

# 仅解压指定文件
tar -xzvf project.tar.gz path/to/file
```

---

## gzip/bzip2 单文件压缩

**基本用法:gzip 压缩**
`gzip [选项] <文件>`

```bash
# 压缩(原文件被替换为 .gz)
gzip large.log

# 保留原文件压缩
gzip -k large.log

# 解压
gzip -d large.log.gz
```

---

**基本用法:bzip2 压缩**
`bzip2 <文件>`

```bash
# 压缩为 .bz2
bzip2 bigfile.dat

# 解压
bzip2 -d bigfile.dat.bz2
```

---

## zip/unzip

**基本用法:zip 压缩目录**
`zip [选项] <归档名> <路径>`

```bash
# 递归压缩目录
zip -r archive.zip src/

# 添加密码保护
zip -r -e secret.zip docs/

# 排除文件
zip -r app.zip . -x "*/node_modules/*"
```

---

**基本用法:unzip 解压**
`unzip [选项] <归档名>`

```bash
# 解压到当前目录
unzip archive.zip

# 解压到指定目录
unzip archive.zip -d /tmp/out

# 查看内容不解压
unzip -l archive.zip
```

---

## 7z 七格式

**基本用法:7z 压缩解压**
`7z <子命令> <归档名> <文件>`

```bash
# 压缩为 7z 格式
7z a archive.7z src/

# 解压
7z x archive.7z

# 列出内容
7z l archive.7z

# 自解压包
7z a -sfx archive.exe src/
```

---

## Windows 内置命令

**基本用法:PowerShell 压缩解压**
`Compress-Archive`

```powershell
# 压缩目录
Compress-Archive -Path src\* -DestinationPath app.zip

# 解压
Expand-Archive -Path app.zip -DestinationPath .\out
```

---

## 校验与分割

**基本用法:生成与校验哈希**
`sha256sum <文件>`

```bash
# 生成校验值
sha256sum image.iso > image.sha256

# 校验完整性
sha256sum -c image.sha256
```

---

**基本用法:大文件分割**
`split [选项] <文件>`

```bash
# 每 100MB 分割一个文件
split -b 100M big.tar.gz part_

# 合并
cat part_* > big.tar.gz
```

---

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
| 编程入门 Java JDK 配置 | 030-JavaJdkConfig | 本文的前置基础 |
| 编程入门 VS Code 安装配置 | 031-VSCodeInstall | 本文的前置基础 |
| 编程入门 Git 安装配置 | 032-GitInstallConfig | 本文的前置基础 |
| 编程入门 Docker 安装 | 033-DockerInstall | 本文的前置基础 |
| 文本处理命令速查手册 | 034-TextProcessing | 本文的并列主题 |
| 管道与重定向速查手册 | 035-PipeRedirect | 本文的并列主题 |
| 进程管理命令速查手册 | 036-ProcessManage | 本文的并列主题 |
| 压缩解压命令速查手册 | 037-CompressArchive | 本文自身 |
