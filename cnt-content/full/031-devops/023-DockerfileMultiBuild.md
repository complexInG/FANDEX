---
order: 100
title: Dockerfile多阶段构建
module: devops
category: 'eng-infra'
difficulty: intermediate
description: 'Dockerfile 多阶段构建：减小镜像体积、分离构建与运行环境。'
author: fanquanpp
updated: '2026-08-01'
related:
  - devops/网络与安全进阶
  - devops/数据库运维
  - devops/Kubernetes核心资源详解
  - 'devops/Helm-Chart应用打包'
prerequisites:
  - devops/概述与Linux基础
---
## 1. 多阶段构建原理

### 1.1 为什么需要多阶段构建

为什么需要多阶段构建是Dockerfile多阶段构建的重要组成部分。本节详细介绍为什么需要多阶段构建的核心概念、工作原理和实际应用。

**关键要点**：

- 为什么需要多阶段构建的定义与核心原理
- 为什么需要多阶段构建的实现方式与技术细节
- 为什么需要多阶段构建在实际场景中的应用与最佳实践
- 为什么需要多阶段构建的常见问题与解决方案

为什么需要多阶段构建在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 FROM ... AS 语法

FROM ... AS 语法是Dockerfile多阶段构建的重要组成部分。本节详细介绍FROM ... AS 语法的核心概念、工作原理和实际应用。

**关键要点**：

- FROM ... AS 语法的定义与核心原理
- FROM ... AS 语法的实现方式与技术细节
- FROM ... AS 语法在实际场景中的应用与最佳实践
- FROM ... AS 语法的常见问题与解决方案

FROM ... AS 语法在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 实战示例

### 2.1 Go 应用多阶段构建

Go 应用多阶段构建是Dockerfile多阶段构建的重要组成部分。本节详细介绍Go 应用多阶段构建的核心概念、工作原理和实际应用。

**关键要点**：

- Go 应用多阶段构建的定义与核心原理
- Go 应用多阶段构建的实现方式与技术细节
- Go 应用多阶段构建在实际场景中的应用与最佳实践
- Go 应用多阶段构建的常见问题与解决方案

Go 应用多阶段构建在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Node.js 应用多阶段构建

Node.js 应用多阶段构建是Dockerfile多阶段构建的重要组成部分。本节详细介绍Node.js 应用多阶段构建的核心概念、工作原理和实际应用。

**关键要点**：

- Node.js 应用多阶段构建的定义与核心原理
- Node.js 应用多阶段构建的实现方式与技术细节
- Node.js 应用多阶段构建在实际场景中的应用与最佳实践
- Node.js 应用多阶段构建的常见问题与解决方案

Node.js 应用多阶段构建在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 Java 应用多阶段构建

Java 应用多阶段构建是Dockerfile多阶段构建的重要组成部分。本节详细介绍Java 应用多阶段构建的核心概念、工作原理和实际应用。

**关键要点**：

- Java 应用多阶段构建的定义与核心原理
- Java 应用多阶段构建的实现方式与技术细节
- Java 应用多阶段构建在实际场景中的应用与最佳实践
- Java 应用多阶段构建的常见问题与解决方案

Java 应用多阶段构建在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 镜像优化技巧

### 3.1 选择基础镜像

选择基础镜像是Dockerfile多阶段构建的重要组成部分。本节详细介绍选择基础镜像的核心概念、工作原理和实际应用。

**关键要点**：

- 选择基础镜像的定义与核心原理
- 选择基础镜像的实现方式与技术细节
- 选择基础镜像在实际场景中的应用与最佳实践
- 选择基础镜像的常见问题与解决方案

选择基础镜像在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 利用缓存

利用缓存是Dockerfile多阶段构建的重要组成部分。本节详细介绍利用缓存的核心概念、工作原理和实际应用。

**关键要点**：

- 利用缓存的定义与核心原理
- 利用缓存的实现方式与技术细节
- 利用缓存在实际场景中的应用与最佳实践
- 利用缓存的常见问题与解决方案

利用缓存在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 .dockerignore

.dockerignore是Dockerfile多阶段构建的重要组成部分。本节详细介绍.dockerignore的核心概念、工作原理和实际应用。

**关键要点**：

- .dockerignore的定义与核心原理
- .dockerignore的实现方式与技术细节
- .dockerignore在实际场景中的应用与最佳实践
- .dockerignore的常见问题与解决方案

.dockerignore在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 最佳实践

### 4.1 安全基础镜像

安全基础镜像是Dockerfile多阶段构建的重要组成部分。本节详细介绍安全基础镜像的核心概念、工作原理和实际应用。

**关键要点**：

- 安全基础镜像的定义与核心原理
- 安全基础镜像的实现方式与技术细节
- 安全基础镜像在实际场景中的应用与最佳实践
- 安全基础镜像的常见问题与解决方案

安全基础镜像在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 非 root 用户

非 root 用户是Dockerfile多阶段构建的重要组成部分。本节详细介绍非 root 用户的核心概念、工作原理和实际应用。

**关键要点**：

- 非 root 用户的定义与核心原理
- 非 root 用户的实现方式与技术细节
- 非 root 用户在实际场景中的应用与最佳实践
- 非 root 用户的常见问题与解决方案

非 root 用户在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 健康检查

健康检查是Dockerfile多阶段构建的重要组成部分。本节详细介绍健康检查的核心概念、工作原理和实际应用。

**关键要点**：

- 健康检查的定义与核心原理
- 健康检查的实现方式与技术细节
- 健康检查在实际场景中的应用与最佳实践
- 健康检查的常见问题与解决方案

健康检查在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## FROM 基础镜像

**基本写法：指定基础镜像**
`FROM <镜像>[:<标签>]`
```dockerfile
# 使用 nginx 作为基础镜像
FROM nginx:1.25
```

**基本写法：多阶段构建**
`FROM <镜像> AS <阶段名>`
```dockerfile
# 第一阶段构建
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp
```

---

## RUN 执行命令

**基本写法：执行 shell 命令**
`RUN <命令>`
```dockerfile
# 安装 nginx
RUN apt-get update && apt-get install -y nginx
```

**基本写法：exec 形式**
`RUN ["<可执行文件>", "<参数1>", "<参数2>"]`
```dockerfile
# 使用 exec 形式执行
RUN ["npm", "install", "--production"]
```

**基本写法：合并多条命令**
`RUN <命令1> && <命令2> && <命令3>`
```dockerfile
# 合并命令减少镜像层
RUN apt-get update \
    && apt-get install -y curl vim \
    && rm -rf /var/lib/apt/lists/*
```

---

## CMD 容器默认命令

**基本写法：shell 形式**
`CMD <命令>`
```dockerfile
# 默认启动 nginx
CMD nginx -g "daemon off;"
```

**基本写法：exec 形式（推荐）**
`CMD ["<可执行文件>", "<参数1>", "<参数2>"]`
```dockerfile
# exec 形式启动 nginx
CMD ["nginx", "-g", "daemon off;"]
```

**基本写法：作为 ENTRYPOINT 参数**
`CMD ["<参数1>", "<参数2>"]`
```dockerfile
# 给 ENTRYPOINT 提供默认参数
ENTRYPOINT ["python", "app.py"]
CMD ["--help"]
```

---

## ENTRYPOINT 入口点

**基本写法：固定执行命令**
`ENTRYPOINT ["<可执行文件>", "<参数>"]`
```dockerfile
# 固定入口点为 app.py
ENTRYPOINT ["python", "app.py"]
```

**基本写法：shell 形式**
`ENTRYPOINT <命令>`
```dockerfile
# shell 形式入口点
ENTRYPOINT python app.py
```

---

## COPY 复制文件

**基本写法：复制文件到镜像**
`COPY <源路径> <目标路径>`
```dockerfile
# 复制当前目录文件到镜像
COPY . /app
```

**基本写法：复制多个文件**
`COPY <文件1> <文件2> <目标目录>`
```dockerfile
# 复制多个配置文件
COPY package.json package-lock.json /app/
```

**基本写法：通配符匹配**
`COPY <通配符> <目标路径>`
```dockerfile
# 复制所有 .json 文件
COPY *.json /app/config/
```

---

## ADD 高级复制

**基本写法：复制并解压 tar 文件**
`ADD <文件> <目标路径>`
```dockerfile
# 自动解压 tar.gz 文件
ADD app.tar.gz /opt/
```

**基本写法：从 URL 下载文件**
`ADD <URL> <目标路径>`
```dockerfile
# 从 URL 下载文件
ADD https://example.com/file.zip /tmp/
```

---

## WORKDIR 工作目录

**基本写法：设置工作目录**
`WORKDIR <路径>`
```dockerfile
# 设置工作目录为 /app
WORKDIR /app
```

**基本写法：相对路径切换**
`WORKDIR <相对路径>`
```dockerfile
# 在已有工作目录下切换
WORKDIR /app
WORKDIR src
```

---

## ENV 环境变量

**基本写法：设置环境变量**
`ENV <键>=<值>`
```dockerfile
# 设置 NODE_ENV 环境变量
ENV NODE_ENV=production
```

**基本写法：设置多个环境变量**
`ENV <键1>=<值1> <键2>=<值2>`
```dockerfile
# 设置多个环境变量
ENV NODE_ENV=production PORT=3000
```

---

## ARG 构建参数

**基本写法：定义构建参数**
`ARG <参数名>[=<默认值>]`
```dockerfile
# 定义 VERSION 构建参数
ARG VERSION=latest
FROM node:$VERSION
```

**基本写法：使用构建参数**
`ARG <参数名>`
```dockerfile
# 在 RUN 中使用构建参数
ARG BUILD_DATE
RUN echo "Build date: $BUILD_DATE" > /build-date.txt
```

---

## EXPOSE 声明端口

**基本写法：声明容器端口**
`EXPOSE <端口>[/<协议>]`
```dockerfile
# 声明 80 端口
EXPOSE 80
```

**基本写法：声明多个端口**
`EXPOSE <端口1> <端口2>`
```dockerfile
# 声明 HTTP 和 HTTPS 端口
EXPOSE 80 443
```

**基本写法：声明 UDP 端口**
`EXPOSE <端口>/udp`
```dockerfile
# 声明 UDP 端口
EXPOSE 53/udp
```

---

## VOLUME 数据卷

**基本写法：声明匿名数据卷**
`VOLUME <路径>`
```dockerfile
# 声明数据卷
VOLUME /data
```

**基本写法：声明多个数据卷**
`VOLUME ["<路径1>", "<路径2>"]`
```dockerfile
# 声明多个数据卷
VOLUME ["/data", "/logs"]
```

---

## USER 切换用户

**基本写法：指定运行用户**
`USER <用户名>[:<组>]`
```dockerfile
# 切换到 node 用户运行
USER node
```

**基本写法：使用 UID**
`USER <UID>[:<GID>]`
```dockerfile
# 使用 UID 切换用户
USER 1000:1000
```

---

## LABEL 标签

**基本写法：添加镜像标签**
`LABEL <键>=<值>`
```dockerfile
# 添加维护者标签
LABEL maintainer="dev@example.com"
```

**基本写法：添加多个标签**
`LABEL <键1>=<值1> <键2>=<值2>`
```dockerfile
# 添加多个元数据标签
LABEL version="1.0" description="My App" author="dev-team"
```

---

## HEALTHCHECK 健康检查

**基本写法：设置健康检查**
`HEALTHCHECK [选项] CMD <命令>`
```dockerfile
# 每 30 秒检查一次健康状态
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost/ || exit 1
```

**基本写法：禁用健康检查**
`HEALTHCHECK NONE`
```dockerfile
# 禁用基础镜像的健康检查
HEALTHCHECK NONE
```

## 参考文献

GitHub Actions 文档：https://docs.github.com/zh/actions
GitLab CI 文档：https://docs.gitlab.com/ci/
Argo CD：https://argo-cd.readthedocs.io/
DORA 研究：https://dora.dev/
DevOps 手册（Gene Kim 等）：https://itrevolution.com/devops-handbook/

## 延伸阅读

Docker 与 Kubernetes 深入，见 031-devops 模块文档。
CI/CD 管线设计，见 031-devops 模块 CICD 文档。
云原生架构，见 034-cloud-computing 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 DevOps 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 GitOps 与声明式交付

Git 是唯一事实来源：集群状态由仓库声明驱动，差异由控制器调和（Argo CD/Flux）。
PR 流程即变更审批，合并即发布意图；回滚 = revert 提交。
与 CI 衔接：CI 产出镜像，CD 更新清单引用新 digest。
安全：仓库签名、密钥加密（SOPS）、审计日志。

### 13.2 可观测性与 SLO

指标：RED（请求率、错误、时长）与 USE（利用率、饱和、错误）。
日志：结构化（JSON）、集中采集、关联 trace_id。
追踪：OpenTelemetry 传播上下文，瀑布分析延迟。
SLO/错误预算：目标可用性 99.9% 对应每月约 43 分钟不可用预算，驱动发布决策。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与 Linux 基础 | 001-OverviewLinuxBasics | 本文的前置基础 |
| 网络与安全 | 002-NetworkSecurity | 本文的安全延伸 |
| 容器与 Docker | 003-ContainerDocker | 本文的并列主题 |
| Kubernetes | 004-Kubernetes | 本文的并列主题 |
| CI/CD 流水线 | 005-CICDPipeline | 本文的并列主题 |
| 监控与可观测性 | 006-MonitorAndObservability | 本文的并列主题 |
| 基础设施即代码 | 007-IaC | 本文的前置基础 |
| 云原生与 SRE | 008-CloudNativeSRE | 本文的并列主题 |
| Shell脚本编程 | 009-ShellScriptProgramming | 本文的并列主题 |
| 包管理与仓库 | 010-PackageManagementRepository | 本文的并列主题 |
| 服务网格 | 011-ServiceMesh | 本文的并列主题 |
| 日志管理 | 012-LogManagement | 本文的并列主题 |
| 配置管理 | 013-ConfigManagement | 本文的并列主题 |
| 性能调优 | 014-PerformanceTuning | 本文的性能延伸 |
| 高可用架构 | 015-HighAvailabilityArchitecture | 本文的原理深化 |
| 自动化测试 | 016-AutomationTest | 本文的并列主题 |
| 故障排查 | 017-Troubleshooting | 本文的并列主题 |
| 容器安全 | 018-ContainerSecurity | 本文的安全延伸 |
| GitOps与持续交付 | 019-GitOpsCD | 本文的并列主题 |
| 监控与告警 | 020-MonitorAndAlert | 本文的并列主题 |
| 网络与安全进阶 | 021-NetworkSecurityAdvanced | 本文的安全延伸 |
| 数据库运维 | 022-DatabaseOps | 本文的并列主题 |
| Dockerfile多阶段构建 | 023-DockerfileMultiBuild | 本文自身 |
| Kubernetes核心资源详解 | 024-KubernetesCoreDetailed | 本文的并列主题 |
| Helm-Chart应用打包 | 025-HelmChartApplicationPackage | 本文的并列主题 |
| Terraform资源编排 | 026-Terraform | 本文的并列主题 |
| Ansible-Playbook配置管理 | 027-AnsiblePlaybookConfigManagement | 本文的并列主题 |
| Prometheus指标采集与告警 | 028-Prometheus | 本文的并列主题 |
| Grafana仪表盘配置 | 029-GrafanaTableConfig | 本文的并列主题 |
| ELK-Stack日志分析 | 030-ELKStackLogAnalysis | 本文的并列主题 |
| OpenTelemetry | 031-OpenTelemetry | 本文的并列主题 |
| GitOps与ArgoCD | 032-GitOpsArgoCD | 本文的并列主题 |
| DevOps kubectl 基础命令 | 033-KubectlBasics | 本文的前置基础 |
| DevOps Helm 包管理命令 | 034-HelmCommands | 本文的并列主题 |
| DevOps Jenkins Pipeline | 035-JenkinsPipeline | 本文的并列主题 |
| DevOps GitLab CI/CD | 036-GitLabCI | 本文的并列主题 |
