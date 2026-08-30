---
order: 270
title: Docker 安装
module: 'getting-started'
category: 工具链
difficulty: beginner
description: Docker Desktop 与 Docker Engine 在主流系统下的安装和验证。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'getting-started/014-WindowsEnvConfigTutorial'
  - 'getting-started/015-MacOSEnvConfigTutorial'
  - 'getting-started/016-LinuxEnvConfigTutorial'
prerequisites:
  - 'getting-started/004-DevEnvSetup'
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
