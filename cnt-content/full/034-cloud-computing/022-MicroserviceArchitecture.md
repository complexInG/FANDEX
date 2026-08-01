---
order: 59
title: 微服务架构
module: 'cloud-computing'
category: 'eng-infra'
difficulty: intermediate
description: 微服务架构设计：拆分策略、通信模式、数据管理与服务治理详解。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cloud-computing/云成本优化'
  - 'cloud-computing/12要素应用'
  - 'cloud-computing/服务网格'
  - 'cloud-computing/可观测性'
prerequisites:
  - 'cloud-computing/云计算基础'
---

## 1. 微服务概述

### 1.1 什么是微服务

微服务是一种将应用拆分为一组小型、独立部署的服务的架构风格。

### 1.2 与单体架构对比

| 对比项 | 单体架构 | 微服务架构 |
| ------ | -------- | ---------- |
| 部署   | 整体部署 | 独立部署   |
| 技术栈 | 统一     | 异构       |
| 扩展   | 整体扩展 | 按需扩展   |
| 故障   | 全局影响 | 局部影响   |
| 团队   | 集中     | 分散       |
| 复杂度 | 代码复杂 | 运维复杂   |

### 1.3 何时使用微服务

| 场景          | 推荐   |
| ------------- | ------ |
| 小团队/初创   | 单体   |
| 大型复杂系统  | 微服务 |
| 快速验证      | 单体   |
| 高并发/多团队 | 微服务 |

## 2. 服务拆分策略

### 2.1 拆分原则

| 原则     | 描述                   |
| -------- | ---------------------- |
| 单一职责 | 每个服务一个业务能力   |
| 高内聚   | 相关功能放在一起       |
| 松耦合   | 服务间依赖最小化       |
| 独立部署 | 可独立发布             |
| 数据自治 | 每个服务有自己的数据库 |

### 2.2 拆分方法

| 方法       | 描述             |
| ---------- | ---------------- |
| 按业务能力 | 围绕业务功能拆分 |
| 按子域     | DDD 限界上下文   |
| 按用例     | 围绕用户场景     |
| 按数据     | 围绕数据所有权   |

### 2.3 DDD 限界上下文

```mermaid
flowchart TD
    subgraph O[订单上下文]
        OS[OrderService] OD[OrderDB]
    end
    subgraph I[库存上下文]
        IS[InventorySvc] ID[InventoryDB]
    end
    subgraph P[支付上下文]
        PS[PaymentService] PD[PaymentDB]
    end
```

## 3. 服务通信

### 3.1 同步通信

| 方式    | 协议           | 特点           |
| ------- | -------------- | -------------- |
| REST    | HTTP/JSON      | 简单、通用     |
| gRPC    | HTTP2/Protobuf | 高性能、强类型 |
| GraphQL | HTTP/JSON      | 灵活查询       |

### 3.2 异步通信

| 方式     | 协议          | 特点           |
| -------- | ------------- | -------------- |
| 消息队列 | AMQP          | 解耦、削峰     |
| 事件驱动 | Kafka         | 高吞吐、持久化 |
| 事件总线 | Redis Streams | 轻量级         |

### 3.3 通信模式

| 模式      | 描述         | 适用场景   |
| --------- | ------------ | ---------- |
| 请求-响应 | 同步调用     | 查询类     |
| 事件通知  | 异步通知     | 状态变更   |
| 事件溯源  | 存储所有事件 | 审计、回放 |
| CQRS      | 读写分离     | 复杂查询   |

### 3.4 Saga 模式

分布式事务管理：

**编排式**：

```
OrderService → CreateOrder → ReserveInventory → ProcessPayment → ConfirmOrder
                                      ↓ 失败
                              CancelOrder ← RefundPayment
```

**协调式**：

```
Saga Coordinator → 调用各服务 → 失败时发送补偿命令
```

## 4. 数据管理

### 4.1 数据库每服务一个

```
 每个服务有独立数据库
 服务间直接访问其他服务的数据库
 通过 API 或事件共享数据
```

### 4.2 数据一致性

| 策略       | 描述          |
| ---------- | ------------- |
| 强一致性   | 2PC（不推荐） |
| 最终一致性 | Saga + 事件   |
| 补偿事务   | 失败时回滚    |

### 4.3 API 组合

```
API Gateway → 聚合多个服务的数据 → 返回给客户端

GET /order-details/123
  → OrderService: 订单信息
  → InventoryService: 库存状态
  → PaymentService: 支付状态
  → 组合返回
```

## 5. 服务治理

### 5.1 服务发现

| 方式       | 描述                   |
| ---------- | ---------------------- |
| 客户端发现 | 客户端查询注册中心     |
| 服务端发现 | 负载均衡器查询注册中心 |

### 5.2 负载均衡

| 策略     | 描述             |
| -------- | ---------------- |
| 轮询     | 依次分配         |
| 随机     | 随机分配         |
| 加权     | 按权重分配       |
| 最少连接 | 分配给连接最少的 |

### 5.3 熔断器

```javascript
// 熔断器状态机
CLOSED → (错误率超阈值) → OPEN
OPEN → (超时后) → HALF_OPEN
HALF_OPEN → (探测成功) → CLOSED
HALF_OPEN → (探测失败) → OPEN
```

### 5.4 限流

| 算法     | 描述             |
| -------- | ---------------- |
| 固定窗口 | 固定时间窗口计数 |
| 滑动窗口 | 平滑计数         |
| 令牌桶   | 匀速生成令牌     |
| 漏桶     | 匀速消费请求     |

## 6. 微服务最佳实践

| 实践       | 描述                 |
| ---------- | -------------------- |
| API 版本化 | `/api/v1/resource`   |
| 幂等设计   | 重复请求结果一致     |
| 健康检查   | `/health` 端点       |
| 优雅降级   | 依赖失败时的备选方案 |
| 配置外部化 | 环境变量/配置中心    |
| 可观测性   | 日志+指标+追踪       |
| 契约测试   | 消费者驱动契约       |
| CI/CD      | 每个服务独立流水线   |

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
| 12要素应用 | 021-TwelveFactorApp | 本文的并列主题 |
| 微服务架构 | 022-MicroserviceArchitecture | 本文自身 |
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
