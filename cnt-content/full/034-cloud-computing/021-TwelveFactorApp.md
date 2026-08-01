---
order: 58
title: 12要素应用
module: 'cloud-computing'
category: 'eng-infra'
difficulty: intermediate
description: '12-Factor App 方法论：构建云原生应用的十二个最佳实践详解。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cloud-computing/Helm包管理'
  - 'cloud-computing/云成本优化'
  - 'cloud-computing/微服务架构'
  - 'cloud-computing/服务网格'
prerequisites:
  - 'cloud-computing/云计算基础'
---

## 1. 12-Factor 概述

### 1.1 起源

12-Factor App 由 Heroku 联合创始人 Adam Wiggins 于 2011 年提出，是构建 SaaS 应用的方法论。

### 1.2 核心目标

- 可移植性
- 云原生部署
- 持续部署
- 弹性伸缩

## 2. 十二个要素

### 2.1 Codebase — 代码库

一份代码库，多次部署。

```
一个应用 → 一个 Git 仓库
同一代码库 → 多个部署（dev/staging/prod）
不同应用 → 不同代码库
```

| 规则       | 描述                 |
| ---------- | -------------------- |
| 单一代码库 | 一个应用一个仓库     |
| 多次部署   | 共享代码，不同配置   |
| 不共享代码 | 不同应用不共享代码库 |

### 2.2 Dependencies — 依赖

显式声明并隔离依赖。

```json
// package.json
{
  "dependencies": {
    "express": "^4.18.0",
    "lodash": "^4.17.21"
  }
}
```

| 规则     | 描述             |
| -------- | ---------------- |
| 显式声明 | 通过清单文件声明 |
| 隔离     | 不依赖系统级包   |
| 锁定     | 使用 lock 文件   |

### 2.3 Config — 配置

在环境中存储配置。

```bash
# 环境变量
export DATABASE_URL=postgres://user:pass@host:5432/db
export API_KEY=sk-xxx
export LOG_LEVEL=info
```

| 规则     | 描述             |
| -------- | ---------------- |
| 不硬编码 | 配置不写在代码中 |
| 环境变量 | 通过 env 传入    |
| 严格分离 | 代码与配置独立   |

**配置判断标准**：在不同部署间是否变化？变化 → 配置，不变 → 代码。

### 2.4 Backing Services — 后端服务

将后端服务当作附加资源。

```
应用 ←→ 数据库（可替换）
应用 ←→ 消息队列（可替换）
应用 ←→ 缓存（可替换）
```

| 规则     | 描述                 |
| -------- | -------------------- |
| 统一接口 | 本地和远程服务无差别 |
| 可替换   | 通过配置切换服务     |
| 松耦合   | 不绑定特定实现       |

### 2.5 Build, Release, Run — 构建/发布/运行

严格分离构建和运行阶段。

```
构建：代码 → 可执行包
发布：可执行包 + 配置 → 发布版本
运行：启动发布版本
```

| 阶段    | 输入        | 输出     |
| ------- | ----------- | -------- |
| Build   | 代码 + 依赖 | 构建产物 |
| Release | 构建 + 配置 | 发布版本 |
| Run     | 发布版本    | 运行进程 |

### 2.6 Processes — 进程

以无状态进程运行应用。

| 规则     | 描述               |
| -------- | ------------------ |
| 无状态   | 进程不存储状态     |
| 持久数据 | 存入后端服务       |
| 可替换   | 任何进程可随时停止 |

### 2.7 Port Binding — 端口绑定

通过端口绑定提供服务。

```javascript
// 应用自包含 Web 服务器
const server = app.listen(process.env.PORT || 3000);
```

| 规则     | 描述                  |
| -------- | --------------------- |
| 自包含   | 不依赖外部 Web 服务器 |
| 端口监听 | 通过端口暴露服务      |
| 可寻址   | URL 即服务            |

### 2.8 Concurrency — 并发

通过进程模型进行扩展。

```
扩展方式：
- 横向扩展（增加进程数）
- 纵向扩展（增加资源）
```

| 进程类型 | 描述           |
| -------- | -------------- |
| Web      | 处理 HTTP 请求 |
| Worker   | 处理后台任务   |
| Clock    | 定时任务       |

### 2.9 Disposability — 易处理

快速启动和优雅终止。

| 规则     | 描述                 |
| -------- | -------------------- |
| 快速启动 | 秒级启动             |
| 优雅关闭 | 处理完当前请求后退出 |
| 健壮性   | 进程可随时被替换     |

```javascript
// 优雅关闭
process.on('SIGTERM', () => {
  server.close(() => {
    process.exit(0);
  });
});
```

### 2.10 Dev/Prod Parity — 开发/生产一致

尽可能保持开发、预发布和生产环境一致。

| 差异 | 传统 | 12-Factor |
| ---- | ---- | --------- |
| 时间 | 数周 | 数小时    |
| 人员 | 不同 | 相同      |
| 工具 | 不同 | 相同      |

### 2.11 Logs — 日志

将日志视为事件流。

```bash
# 输出到 stdout/stderr
console.log("Request processed");
console.error("Database connection failed");
```

| 规则       | 描述               |
| ---------- | ------------------ |
| 不管理日志 | 应用不关心日志存储 |
| 事件流     | 日志是连续的事件流 |
| 集中处理   | 由外部系统收集     |

### 2.12 Admin Processes — 管理进程

将管理任务作为一次性进程运行。

```bash
# 一次性管理任务
rails db:migrate
python manage.py migrate
npx prisma migrate deploy
```

| 规则     | 描述               |
| -------- | ------------------ |
| 一次性   | 运行后退出         |
| 同代码库 | 使用相同代码和配置 |
| 同环境   | 在相同环境中运行   |

## 3. 现代扩展

### 3.1 超越 12-Factor

| 新要素    | 描述           |
| --------- | -------------- |
| API First | API 优先设计   |
| Telemetry | 遥测与可观测性 |
| Security  | 安全左移       |
| Container | 容器化         |
| CI/CD     | 持续集成部署   |

### 3.2 与云原生的关系

12-Factor 是云原生的理论基础，CNCF 的很多项目（Kubernetes、Istio）都是 12-Factor 的工程实现。

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
| Docker深度解析 | 009-DockerDeepAnalysis | 本文的并列主题 |
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
| 12要素应用 | 021-TwelveFactorApp | 本文自身 |
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
