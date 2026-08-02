---
order: 290
title: 编程入门 pyenv 与 uv 版本管理
module: getting-started

category: '001-getting-started'
difficulty: beginner
description: 编程入门 pyenv 与 uv 版本管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## pyenv-win 安装

**基本写法：PowerShell 安装 pyenv-win**
`irm https://github.com/pyenv-win/pyenv-win/raw/master/pyenv-win/install-pyenv-win.ps1 | iex`
```bash
# 通过 PowerShell 脚本安装 pyenv-win
irm https://github.com/pyenv-win/pyenv-win/raw/master/pyenv-win/install-pyenv-win.ps1 | iex
```

---

**基本写法：查看可安装版本**
`pyenv install --list`
```bash
# 列出所有可安装的 Python 版本
pyenv install --list
```

---

**基本写法：安装指定版本**
`pyenv install <版本号>`
```bash
# 安装指定版本的 Python
pyenv install 3.13.0
```

---

**基本写法：查看已安装版本**
`pyenv versions`
```bash
# 列出所有已安装的 Python 版本
pyenv versions
```

---

## pyenv 版本切换

**基本写法：设置全局默认版本**
`pyenv global <版本号>`
```bash
# 设置全局默认 Python 版本
pyenv global 3.13.0
```

---

**基本写法：设置项目本地版本**
`pyenv local <版本号>`
```bash
# 在当前项目目录生成 .python-version 文件
pyenv local 3.11.9
```

---

**基本写法：设置当前 shell 版本**
`pyenv shell <版本号>`
```bash
# 仅在当前终端会话切换版本
pyenv shell 3.12.8
```

---

**基本写法：卸载版本**
`pyenv uninstall <版本号>`
```bash
# 删除指定版本的 Python
pyenv uninstall 3.9.5
```

---

## uv 安装

**基本写法：Windows 安装 uv**
`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
```bash
# 通过官方脚本安装 uv（Windows）
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

**基本写法：Linux/macOS 安装 uv**
`curl -LsSf https://astral.sh/uv/install.sh | sh`
```bash
# 通过官方脚本安装 uv（Linux/macOS）
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

**基本写法：通过 pip 安装 uv**
`pip install uv`
```bash
# 通过 pip 安装 uv
pip install uv
```

---

**基本写法：通过 Homebrew 安装 uv**
`brew install uv`
```bash
# macOS 通过 Homebrew 安装
brew install uv
```

---

## uv Python 版本管理

**基本写法：安装 Python 版本**
`uv python install <版本号>`
```bash
# 安装指定版本的 Python
uv python install 3.13
```

---

**基本写法：批量安装多个版本**
`uv python install <版本1> <版本2>`
```bash
# 一次安装多个版本
uv python install 3.13 3.12 3.11
```

---

**基本写法：查看可用版本**
`uv python list`
```bash
# 列出所有可用和已安装的版本
uv python list
```

---

**基本写法：为项目锁定版本**
`uv python pin <版本号>`
```bash
# 写入 .python-version 文件锁定项目版本
uv python pin 3.13
```

---

## uv 项目管理

**基本写法：初始化项目**
`uv init <项目名>`
```bash
# 创建标准 Python 项目结构
uv init myproject
```

---

**基本写法：添加依赖**
`uv add <包名>`
```bash
# 添加包并自动更新 uv.lock
uv add requests
```

---

**基本写法：添加开发依赖**
`uv add --dev <包名>`
```bash
# 添加开发依赖包
uv add --dev pytest
```

---

**基本写法：运行脚本**
`uv run <脚本>`
```bash
# 自动激活虚拟环境并运行
uv run main.py
```

---

**基本写法：创建虚拟环境**
`uv venv`
```bash
# 在当前目录创建 .venv 虚拟环境
uv venv
```

---

**基本写法：指定 Python 版本创建环境**
`uv venv --python <版本号>`
```bash
# 使用指定 Python 版本创建虚拟环境
uv venv --python 3.11
```

---

**基本写法：同步依赖**
`uv sync`
```bash
# 根据 uv.lock 同步安装所有依赖
uv sync
```

## 延伸阅读
从入门到进阶路径：001 入门 -> 002 Markdown -> 003 Git -> 006 HTML -> 007 CSS -> 008 JS。
语言进阶：013 Java / 040 Python / 016 Go 按兴趣选择。
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
