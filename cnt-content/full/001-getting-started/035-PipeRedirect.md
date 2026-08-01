---
order: 350
title: 管道与重定向速查手册
module: 001-getting-started
category: '001-getting-started'
difficulty: beginner
description: 管道与重定向速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 管道与重定向速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 标准输出重定向

**基本用法:覆盖写入文件**
`<命令> > <文件>`

```bash
# 把命令输出写入文件(覆盖)
ls -la > files.txt

# 把错误信息也写入同一文件
ls /nope > result.txt 2>&1
```

---

**基本用法:追加写入文件**
`<命令> >> <文件>`

```bash
# 追加日志到末尾
echo "done" >> build.log
```

---

## 标准输入重定向

**基本用法:从文件读取输入**
`<命令> < <文件>`

```bash
# 从文件读取内容统计行数
wc -l < data.txt
```

---

## 标准错误重定向

**基本用法:重定向错误输出**
`<命令> 2> <文件>`

```bash
# 仅丢弃错误信息
find / -name "*.conf" 2> /dev/null

# 错误追加到日志
make build 2>> error.log
```

---

**基本用法:合并标准输出与错误**
`<命令> &> <文件>`

```bash
# 同时收集输出和错误到同一文件
npm install &> install.log
```

---

## 管道

**基本用法:连接命令**
`<命令1> | <命令2>`

```bash
# 翻页查看长输出
ls -la | less

# 过滤后再统计
grep "ERROR" app.log | wc -l

# 多级管道处理
cat access.log | grep "404" | awk '{print $7}' | sort | uniq -c | sort -nr | head
```

---

## tee 双向输出

**基本用法:同时输出到屏幕和文件**
`<命令> | tee <文件>`

```bash
# 屏幕显示并写入日志
make test | tee test.log

# 追加模式
echo "step2" | tee -a progress.log
```

---

## xargs 参数传递

**基本用法:把输入转为参数**
`<命令> | xargs <命令>`

```bash
# 批量删除查找到的文件
find . -name "*.tmp" | xargs rm -f

# 每行一个参数执行
cat urls.txt | xargs -n1 curl -I

# 指定替换位置
ls *.bak | xargs -I{} mv {} archive/

# 并行执行 4 个
find . -name "*.png" | xargs -P4 -n1 optipng
```

---

## 进程替换

**基本用法:对比两个命令输出**
`diff <(<命令1>) <(<命令2>)`

```bash
# 对比两个目录文件列表
diff <(ls dir1) <(ls dir2)
```

---

## here document

**基本用法:多行输入**
`<命令> << <结束标记>`

```bash
# 多行写入文件
cat > note.txt <<EOF
第一行内容
第二行内容
EOF
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
| 管道与重定向速查手册 | 035-PipeRedirect | 本文自身 |
| 进程管理命令速查手册 | 036-ProcessManage | 本文的并列主题 |
| 压缩解压命令速查手册 | 037-CompressArchive | 本文的并列主题 |
