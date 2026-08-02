---
order: 330
title: 编程入门 Docker 安装
module: getting-started

category: '001-getting-started'
difficulty: beginner
description: 编程入门 Docker 安装 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Windows 安装

**基本写法：winget 安装 Docker Desktop**
`winget install Docker.DockerDesktop`
```bash
# 通过 Windows 包管理器安装 Docker Desktop
winget install Docker.DockerDesktop
```

---

**基本写法：升级 Docker Desktop**
`winget upgrade Docker.DockerDesktop`
```bash
# 升级 Docker Desktop 到最新版本
winget upgrade Docker.DockerDesktop
```

---

**基本写法：WSL2 前置安装**
`wsl --install`
```bash
# 安装 WSL2（Docker Desktop 依赖）
wsl --install
```

---

**基本写法：设置 WSL2 为默认版本**
`wsl --set-default-version 2`
```bash
# 设置 WSL2 为默认版本
wsl --set-default-version 2
```

---

## macOS 安装

**基本写法：Homebrew 安装 Docker Desktop**
`brew install --cask docker`
```bash
# 通过 Homebrew 安装 Docker Desktop
brew install --cask docker
```

---

**基本写法：Homebrew 安装 Colima（轻量替代）**
`brew install colima`
```bash
# 安装 Colima 作为轻量级 Docker 运行时
brew install colima
```

---

**基本写法：启动 Colima**
`colima start`
```bash
# 启动 Colima 虚拟机
colima start
```

---

## Linux 安装

**基本写法：apt 安装 Docker（Ubuntu/Debian）**
`sudo apt-get install docker.io`
```bash
# 通过 apt 安装 Docker
sudo apt-get install docker.io
```

---

**基本写法：yum 安装 Docker（CentOS/RHEL）**
`sudo yum install docker`
```bash
# 通过 yum 安装 Docker
sudo yum install docker
```

---

**基本写法：官方脚本安装**
`curl -fsSL https://get.docker.com | sh`
```bash
# 使用 Docker 官方安装脚本
curl -fsSL https://get.docker.com | sh
```

---

## 服务管理

**基本写法：启动 Docker 服务**
`sudo systemctl start docker`
```bash
# 启动 Docker 守护进程
sudo systemctl start docker
```

---

**基本写法：设置开机自启**
`sudo systemctl enable docker`
```bash
# 设置 Docker 开机自动启动
sudo systemctl enable docker
```

---

**基本写法：查看 Docker 服务状态**
`sudo systemctl status docker`
```bash
# 查看 Docker 服务运行状态
sudo systemctl status docker
```

---

**基本写法：重启 Docker 服务**
`sudo systemctl restart docker`
```bash
# 重启 Docker 守护进程
sudo systemctl restart docker
```

---

## 用户组配置

**基本写法：添加用户到 docker 组**
`sudo usermod -aG docker <用户名>`
```bash
# 免 sudo 使用 docker 命令
sudo usermod -aG docker $USER
```

---

**基本写法：激活组权限**
`newgrp docker`
```bash
# 立即生效组权限无需重新登录
newgrp docker
```

---

## 安装验证

**基本写法：验证 Docker 安装**
`docker --version`
```bash
# 查看 Docker 版本信息
docker --version
```

---

**基本写法：查看详细版本信息**
`docker version`
```bash
# 查看 Docker 客户端和服务端版本
docker version
```

---

**基本写法：运行测试容器**
`docker run hello-world`
```bash
# 运行官方测试容器验证安装
docker run hello-world
```

---

**基本写法：查看 Docker 系统信息**
`docker info`
```bash
# 查看 Docker 系统详细配置信息
docker info
```

---

**基本写法：查看 Docker Compose 版本**
`docker compose version`
```bash
# 查看 Docker Compose 插件版本
docker compose version
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
