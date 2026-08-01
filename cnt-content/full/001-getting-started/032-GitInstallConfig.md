---
order: 320
title: 编程入门 Git 安装配置
module: getting-started

category: '001-getting-started'
difficulty: beginner
description: 编程入门 Git 安装配置 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Windows 安装

**基本写法：winget 安装 Git**
`winget install Git.Git`
```bash
# 通过 Windows 包管理器安装 Git
winget install Git.Git
```

---

**基本写法：winget 安装指定版本**
`winget install Git.Git -v <版本号>`
```bash
# 安装指定版本的 Git
winget install Git.Git -v 2.45.0
```

---

**基本写法：升级 Git**
`winget upgrade Git.Git`
```bash
# 升级 Git 到最新版本
winget upgrade Git.Git
```

---

## macOS 安装

**基本写法：Homebrew 安装 Git**
`brew install git`
```bash
# 通过 Homebrew 安装 Git
brew install git
```

---

**基本写法：升级 Git（macOS）**
`brew upgrade git`
```bash
# 通过 Homebrew 升级 Git
brew upgrade git
```

---

## Linux 安装

**基本写法：apt 安装 Git（Ubuntu/Debian）**
`sudo apt-get install git`
```bash
# 通过 apt 安装 Git
sudo apt-get install git
```

---

**基本写法：yum 安装 Git（CentOS/RHEL）**
`sudo yum install git`
```bash
# 通过 yum 安装 Git
sudo yum install git
```

---

**基本写法：dnf 安装 Git（Fedora）**
`sudo dnf install git`
```bash
# 通过 dnf 安装 Git
sudo dnf install git
```

---

## 用户信息配置

**基本写法：设置全局用户名**
`git config --global user.name "<用户名>"`
```bash
# 设置 Git 提交者用户名
git config --global user.name "张三"
```

---

**基本写法：设置全局邮箱**
`git config --global user.email "<邮箱>"`
```bash
# 设置 Git 提交者邮箱
git config --global user.email "zhangsan@example.com"
```

---

**基本写法：设置仓库级用户名**
`git config user.name "<用户名>"`
```bash
# 仅对当前仓库设置用户名
git config user.name "李四"
```

---

**基本写法：查看所有配置**
`git config --list`
```bash
# 查看所有 Git 配置项
git config --list
```

---

**基本写法：查看特定配置**
`git config user.name`
```bash
# 查看当前用户名配置
git config user.name
```

---

## 编辑器与默认分支配置

**基本写法：设置默认编辑器**
`git config --global core.editor "<编辑器命令>"`
```bash
# 设置 VS Code 为默认编辑器
git config --global core.editor "code --wait"
```

---

**基本写法：设置默认分支名**
`git config --global init.defaultBranch <分支名>`
```bash
# 设置新仓库默认分支为 main
git config --global init.defaultBranch main
```

---

**基本写法：设置 vim 为编辑器**
`git config --global core.editor "vim"`
```bash
# 设置 vim 为默认编辑器
git config --global core.editor "vim"
```

---

## 命令别名配置

**基本写法：设置命令别名**
`git config --global alias.<别名> "<命令>"`
```bash
# 为 status 命令设置别名 st
git config --global alias.st status
```

---

**基本写法：常用别名批量设置**
`git config --global alias.<别名> "<命令>"`
```bash
# 设置常用命令别名
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

---

**基本写法：删除别名**
`git config --global --unset alias.<别名>`
```bash
# 删除已设置的命令别名
git config --global --unset alias.st
```

---

## 安装验证

**基本写法：验证 Git 安装**
`git --version`
```bash
# 应输出 git version 2.45.0 类似信息
git --version
```

---

**基本写法：查看 Git 帮助**
`git --help`
```bash
# 查看 Git 顶层帮助文档
git --help
```

---

**基本写法：查看特定命令帮助**
`git help <命令>`
```bash
# 查看 commit 命令的详细帮助
git help commit
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
