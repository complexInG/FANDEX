---
order: 180
title: Python 安装
module: 'getting-started'
category: 工具链
difficulty: beginner
description: Python 在 Windows、macOS、Linux 下的安装与安装验证。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'getting-started/011-WindowsEnvConfigTutorial'
  - 'getting-started/012-MacOSEnvConfigTutorial'
  - 'getting-started/013-LinuxEnvConfigTutorial'
  - 'getting-started/019-PipVenvManager'
  - 'getting-started/020-PyenvUvManage'
prerequisites:
  - 'getting-started/001-DevEnvSetup'
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
