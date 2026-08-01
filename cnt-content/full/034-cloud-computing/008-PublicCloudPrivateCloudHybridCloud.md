---
order: 51
title: 公有云与私有云与混合云
module: 'cloud-computing'
category: 'eng-infra'
difficulty: beginner
description: 云计算部署模型：公有云、私有云、混合云与多云的概念、对比与选型。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cloud-computing/虚拟化技术'
  - 'cloud-computing/云架构设计'
  - 'cloud-computing/Docker深度解析'
  - 'cloud-computing/云原生应用'
prerequisites:
  - 'cloud-computing/云计算基础'
---

## 1. 部署模型概述

### 1.1 四种部署模型

| 模型   | 基础设施归属 | 访问范围 |
| ------ | ------------ | -------- |
| 公有云 | 云供应商     | 公开     |
| 私有云 | 组织自建     | 组织内部 |
| 混合云 | 混合         | 按需     |
| 多云   | 多供应商     | 按需     |

## 2. 公有云

### 2.1 特点

| 优势         | 劣势           |
| ------------ | -------------- |
| 无需前期投资 | 数据不在本地   |
| 弹性伸缩     | 依赖供应商     |
| 全球部署     | 长期成本可能高 |
| 丰富的服务   | 合规限制       |
| 快速上线     | 供应商锁定     |

### 2.2 主要供应商

| 供应商 | 市场份额 | 优势               |
| ------ | -------- | ------------------ |
| AWS    | ~32%     | 最全面、生态最丰富 |
| Azure  | ~23%     | 企业集成、混合云   |
| GCP    | ~11%     | 数据分析、AI/ML    |
| 阿里云 | ~6%      | 中国市场、电商     |
| 华为云 | ~4%      | 政企、5G           |

### 2.3 适用场景

- 初创公司
- 互联网应用
- 全球化业务
- AI/ML 工作负载
- 开发测试环境

## 3. 私有云

### 3.1 特点

| 优势         | 劣势         |
| ------------ | ------------ |
| 数据完全控制 | 前期投资大   |
| 安全合规     | 运维成本高   |
| 定制化       | 扩展性受限   |
| 低延迟       | 技术门槛高   |
| 无供应商锁定 | 资源利用率低 |

### 3.2 实现方式

| 方式       | 描述               | 代表                      |
| ---------- | ------------------ | ------------------------- |
| 自建       | 购买硬件+部署软件  | OpenStack, VMware         |
| 托管       | 供应商提供专属硬件 | AWS Outposts, Azure Stack |
| 虚拟私有云 | 公有云中的隔离网络 | VPC                       |

### 3.3 适用场景

- 金融/政府
- 数据敏感行业
- 合规要求严格
- 大规模稳定负载
- 核心业务系统

## 4. 混合云

### 4.1 架构

```mermaid
flowchart LR
    P[私有云<br/>核心业务] <-->|专线/VPN| U[公有云<br/>弹性负载]
```

### 4.2 典型模式

| 模式     | 描述                           |
| -------- | ------------------------------ |
| 云爆发   | 私有云为主，公有云应对峰值     |
| 数据驻留 | 敏感数据在私有云，计算在公有云 |
| 灾备     | 公有云作为灾备站点             |
| 边缘计算 | 边缘节点+云端协同              |

### 4.3 关键技术

| 技术     | 作用               |
| -------- | ------------------ |
| 专线连接 | 低延迟、高带宽互联 |
| 统一管理 | 混合云管理平台     |
| 容器化   | 跨云一致性         |
| Istio    | 服务网格跨云通信   |

## 5. 多云

### 5.1 驱动因素

- 避免供应商锁定
- 选择最优服务
- 合规要求
- 灾备冗余
- 成本优化

### 5.2 挑战

| 挑战       | 解决方案          |
| ---------- | ----------------- |
| 管理复杂   | 统一管理平台      |
| 网络互联   | 云间专线          |
| 数据一致性 | 分布式存储        |
| 技能要求   | Terraform/Ansible |
| 成本控制   | FinOps            |

## 6. 选型指南

| 场景        | 推荐模型      |
| ----------- | ------------- |
| 初创/互联网 | 公有云        |
| 金融/政府   | 私有云+混合云 |
| 弹性业务    | 混合云        |
| 全球化      | 多云          |
| 合规+弹性   | 混合云        |

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
| 公有云与私有云与混合云 | 008-PublicCloudPrivateCloudHybridCloud | 本文自身 |
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
