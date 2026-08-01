---
order: 52
title: Docker深度解析
module: 'cloud-computing'
category: 'eng-infra'
difficulty: intermediate
description: Docker进阶：镜像构建优化、多阶段构建、网络模式、存储驱动与安全实践。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cloud-computing/云架构设计'
  - 'cloud-computing/公有云与私有云与混合云'
  - 'cloud-computing/云原生应用'
  - 'cloud-computing/Kubernetes架构'
prerequisites:
  - 'cloud-computing/云计算基础'
---

## 1. Docker 镜像优化

### 1.1 多阶段构建

```dockerfile
# 构建阶段
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# 运行阶段
FROM node:18-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

### 1.2 镜像瘦身策略

| 策略                 | 效果           |
| -------------------- | -------------- |
| 使用 Alpine 基础镜像 | 减少 80%+ 体积 |
| 多阶段构建           | 去除构建依赖   |
| 合并 RUN 指令        | 减少镜像层数   |
| .dockerignore        | 排除不必要文件 |
| distroless 镜像      | 最小运行时     |

### 1.3 缓存优化

```dockerfile
#  先复制依赖文件，利用缓存
COPY package*.json ./
RUN npm ci
COPY . .

#  先复制全部，每次代码变更都重新安装依赖
COPY . .
RUN npm ci
```

## 2. Docker 网络

### 2.1 网络模式

| 模式    | 描述           | 用途         |
| ------- | -------------- | ------------ |
| bridge  | 默认桥接网络   | 单机容器通信 |
| host    | 共享宿主机网络 | 高性能场景   |
| none    | 无网络         | 安全隔离     |
| overlay | 跨主机网络     | Swarm/集群   |
| macvlan | 容器独立 MAC   | 网络设备集成 |

### 2.2 自定义网络

```bash
# 创建自定义网络
docker network create --driver bridge --subnet 172.20.0.0/16 mynet

# 容器加入网络
docker run --network mynet --name app nginx

# 容器间通过名称通信
docker run --network mynet --name api my-api
# app 容器可通过 http://api:8080 访问
```

### 2.3 DNS 解析

- 自定义网络：内置 DNS，支持容器名解析
- 默认 bridge：无 DNS，需 `--link`（已废弃）

## 3. Docker 存储

### 3.1 存储类型

| 类型       | 描述           | 生命周期       |
| ---------- | -------------- | -------------- |
| Volume     | Docker 管理    | 独立于容器     |
| Bind Mount | 宿主机目录挂载 | 独立于容器     |
| tmpfs      | 内存存储       | 容器停止即消失 |

### 3.2 Volume 操作

```bash
# 创建
docker volume create mydata

# 使用
docker run -v mydata:/data nginx

# 指定驱动
docker volume create --driver local --opt type=nfs mydata

# 备份
docker run --rm -v mydata:/data -v $(pwd):/backup alpine tar czf /backup/data.tar.gz /data
```

### 3.3 存储驱动

| 驱动         | 文件系统     | 适用场景    |
| ------------ | ------------ | ----------- |
| overlay2     | overlayfs    | 默认推荐    |
| devicemapper | devicemapper | CentOS 旧版 |
| btrfs        | btrfs        | 大量写入    |
| zfs          | zfs          | 数据完整性  |

## 4. Docker Compose

### 4.1 完整示例

```yaml
version: '3.8'
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - '3000:3000'
    environment:
      - DB_HOST=db
      - REDIS_HOST=redis
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '0.5'
          memory: 512M

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres']
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

## 5. Docker 安全

### 5.1 镜像安全

| 措施         | 描述                              |
| ------------ | --------------------------------- |
| 非 root 运行 | `USER app`                        |
| 最小基础镜像 | Alpine/distroless                 |
| 镜像扫描     | Trivy/Snyk                        |
| 签名验证     | Docker Content Trust              |
| 固定版本     | `node:18.17.0` 而非 `node:latest` |

### 5.2 运行时安全

```dockerfile
# 安全 Dockerfile
FROM node:18-alpine
RUN addgroup -g 1001 app && adduser -u 1001 -G app -s /bin/sh -D app
WORKDIR /app
COPY --chown=app:app . .
USER app
EXPOSE 3000
CMD ["node", "server.js"]
```

### 5.3 资源限制

```bash
# CPU 和内存限制
docker run --cpus=0.5 --memory=512m nginx

# 只读文件系统
docker run --read-only --tmpfs /tmp nginx
```

## 6. Docker 最佳实践

| 实践             | 描述             |
| ---------------- | ---------------- |
| 一个容器一个进程 | 单一职责         |
| 无状态设计       | 数据存 Volume    |
| 健康检查         | HEALTHCHECK 指令 |
| 优雅关闭         | 处理 SIGTERM     |
| 日志管理         | stdout/stderr    |
| 环境变量配置     | 不硬编码         |

## 参考文献

AWS 文档：https://docs.aws.amazon.com/
Microsoft Azure 文档：https://learn.microsoft.com/zh-cn/azure/
Google Cloud 文档：https://cloud.google.com/docs?hl=zh-cn
阿里云文档：https://help.aliyun.com/
CNCF 云原生全景：https://landscape.cncf.io/

## 延伸阅读

虚拟化与容器，见 034-cloud-computing 模块相关文档。
Kubernetes 架构，见 034-cloud-computing 模块 K8s 文档。
DevOps 与 IaC，见 031-devops 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供云计算课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 FinOps 成本治理

三阶段：可见（成本分配与预算）、优化（右尺寸、Spot、闲置清理）、运营（持续迭代与责任到团队）。
工具：云厂商成本中心、OpenCost、Kubecost。
组织：FinOps 实践者角色、定期 review、浪费告警。
度量：单位成本（每请求/每用户成本）而非绝对金额。

### 13.2 高可用与容灾设计

可用性数学：99.9% 年停机约 8.7 小时，99.99% 约 52 分钟；多副本降低单点风险。
RPO（可容忍数据丢失）与 RTO（恢复时间）驱动备份与复制策略。
模式：多可用区部署、跨区域异步复制、数据库主备、对象存储版本。
演练：混沌工程（Chaos Monkey 思想）验证真实故障行为。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 云计算基础 | 001-CloudComputingBasics | 本文的前置基础 |
| 云网络与存储 | 002-CloudNetworkStorage | 本文的并列主题 |
| 容器与编排 | 003-ContainerOrchestration | 本文的并列主题 |
| 基础设施即代码 | 004-IaC | 本文的前置基础 |
| IaaS与PaaS与SaaS | 005-IaaSPaaSSaaS | 本文的并列主题 |
| 虚拟化技术 | 006-VirtualizationTech | 本文的并列主题 |
| 云架构设计 | 007-CloudArchitectureDesign | 本文的原理深化 |
| 公有云与私有云与混合云 | 008-PublicCloudPrivateCloudHybridCloud | 本文的并列主题 |
| Docker深度解析 | 009-DockerDeepAnalysis | 本文自身 |
| 云原生应用 | 010-CloudNativeApp | 本文的并列主题 |
| Kubernetes架构 | 011-KubernetesArchitecture | 本文的原理深化 |
| 云数据库服务 | 012-CloudDatabaseService | 本文的并列主题 |
| Kubernetes核心资源 | 013-KubernetesCore | 本文的并列主题 |
| 云存储服务 | 014-CloudStorageService | 本文的并列主题 |
| Kubernetes网络 | 015-KubernetesNetwork | 本文的并列主题 |
| 云网络服务 | 016-CloudNetworkService | 本文的并列主题 |
| Kubernetes存储 | 017-KubernetesStorage | 本文的并列主题 |
| 云安全服务 | 018-CloudSecurityService | 本文的安全延伸 |
| Helm包管理 | 019-HelmPackageManagement | 本文的并列主题 |
| 云成本优化 | 020-CloudCostOptimization | 本文的性能延伸 |
| 12要素应用 | 021-TwelveFactorApp | 本文的并列主题 |
| 微服务架构 | 022-MicroserviceArchitecture | 本文的原理深化 |
| 服务网格 | 023-ServiceMesh | 本文的并列主题 |
| 可观测性 | 024-Observability | 本文的并列主题 |
| AWS核心服务 | 025-AWSCore | 本文的并列主题 |
| 多云与混合云架构 | 026-MultiCloudHybridArchitecture | 本文的原理深化 |
| 负载均衡与自动伸缩 | 027-LoadBalanceAutoScaling | 本文的并列主题 |
| 无服务器架构 | 028-ServerlessArchitecture | 本文的原理深化 |
| 云迁移6R策略 | 029-CloudMigration6RStrategy | 本文的并列主题 |
| 云计算 AWS CLI 配置 | 030-AWSCliConfigure | 本文的并列主题 |
| 云计算 AWS S3 命令 | 031-AWSS3Command | 本文的并列主题 |
| 云计算 AWS EC2 命令 | 032-AWSEC2Command | 本文的并列主题 |
| 云计算 AWS Lambda 命令 | 033-AWSLambdaCommand | 本文的并列主题 |
| 云计算 AWS IAM 命令 | 034-AWSIAMCommand | 本文的并列主题 |
| 云计算 AWS CloudFormation | 035-AWSCloudFormation | 本文的并列主题 |
| 云计算 Azure CLI 配置 | 036-AzureCliConfigure | 本文的并列主题 |
| 云计算 Azure 资源组与 VM | 037-AzureGroupVMCommand | 本文的并列主题 |
| 云计算 Azure 存储命令 | 038-AzureStorageCommand | 本文的并列主题 |
| 云计算 GCP gcloud 配置 | 039-GCPCliConfigure | 本文的并列主题 |
| 云计算 GCP Compute 与 Storage | 040-GCPComputeStorage | 本文的并列主题 |
| 云计算 Terraform 基础 | 041-TerraformBasic | 本文的前置基础 |
| 云计算 Terraform 状态与模块 | 042-TerraformStateModule | 本文的并列主题 |
| AWS CloudWatch 监控日志命令 | 043-AWSCloudWatch | 本文的并列主题 |
| AWS RDS 数据库命令 | 044-AWSRDSCommands | 本文的并列主题 |
| AWS VPC 网络命令 | 045-AWSVPCCommands | 本文的并列主题 |
| AWS SQS/SNS 消息队列命令 | 046-AWSSQSCommands | 本文的并列主题 |
| AWS DynamoDB 命令 | 047-AWSDynamoDB | 本文的并列主题 |
| Azure Functions 命令 | 048-AzureFunctions | 本文的并列主题 |
| Azure AKS Kubernetes 命令 | 049-AzureAKSCommands | 本文的并列主题 |
| GCP GKE Kubernetes 命令 | 050-GCPGKECommands | 本文的并列主题 |
| GCP BigQuery 命令 | 051-GCPBigQuery | 本文的并列主题 |
| Pulumi IaC 命令 | 052-PulumiCommands | 本文的并列主题 |
| Harbor 私有镜像仓库命令 | 053-HarborRegistry | 本文的并列主题 |
| cloud-init 云实例初始化 | 054-CloudInitCommands | 本文的并列主题 |
| AWS CloudFront CDN 命令 | 055-AWSCloudFront | 本文的并列主题 |
