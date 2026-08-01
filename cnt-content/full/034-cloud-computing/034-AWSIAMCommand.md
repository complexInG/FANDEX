---
order: 340
title: 云计算 AWS IAM 命令
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: 云计算 AWS IAM 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 用户管理

**基本写法：列出用户**
`aws iam list-users`
```bash
# 列出账号下所有 IAM 用户
aws iam list-users
```

---

**基本写法：创建用户**
`aws iam create-user --user-name <用户名>`
```bash
# 创建新的 IAM 用户
aws iam create-user --user-name john
```

---

**基本写法：删除用户**
`aws iam delete-user --user-name <用户名>`
```bash
# 删除指定 IAM 用户
aws iam delete-user --user-name john
```

---

**基本写法：查看用户详情**
`aws iam get-user --user-name <用户名>`
```bash
# 查看指定用户信息
aws iam get-user --user-name john
```

---

## 访问密钥

**基本写法：创建访问密钥**
`aws iam create-access-key --user-name <用户名>`
```bash
# 为用户生成新的访问密钥
aws iam create-access-key --user-name john
```

---

**基本写法：列出访问密钥**
`aws iam list-access-keys --user-name <用户名>`
```bash
# 查看用户的所有访问密钥 ID
aws iam list-access-keys --user-name john
```

---

**基本写法：停用访问密钥**
`aws iam update-access-key --access-key-id <密钥ID> --status Inactive --user-name <用户名>`
```bash
# 临时停用访问密钥
aws iam update-access-key --access-key-id AKIAIOSFODNN7EXAMPLE --status Inactive --user-name john
```

---

**基本写法：删除访问密钥**
`aws iam delete-access-key --access-key-id <密钥ID> --user-name <用户名>`
```bash
# 永久删除访问密钥
aws iam delete-access-key --access-key-id AKIAIOSFODNN7EXAMPLE --user-name john
```

---

## 策略管理

**基本写法：列出策略**
`aws iam list-policies [--scope Local]`
```bash
# 列出自定义策略
aws iam list-policies --scope Local
```

---

**基本写法：查看策略详情**
`aws iam get-policy --policy-arn <策略ARN>`
```bash
# 查看策略元数据
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

---

**基本写法：创建策略**
`aws iam create-policy --policy-name <策略名> --policy-document file://<文件>`
```bash
# 从 JSON 文件创建策略
aws iam create-policy --policy-name my-policy --policy-document file://policy.json
```

---

**基本写法：附加策略到用户**
`aws iam attach-user-policy --user-name <用户名> --policy-arn <策略ARN>`
```bash
# 为用户附加 S3 只读策略
aws iam attach-user-policy --user-name john --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

---

**基本写法：分离策略**
`aws iam detach-user-policy --user-name <用户名> --policy-arn <策略ARN>`
```bash
# 从用户移除策略
aws iam detach-user-policy --user-name john --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

---

**基本写法：列出用户策略**
`aws iam list-attached-user-policies --user-name <用户名>`
```bash
# 查看用户附加的所有策略
aws iam list-attached-user-policies --user-name john
```

---

## 角色管理

**基本写法：创建角色**
`aws iam create-role --role-name <角色名> --assume-role-policy-document file://<文件>`
```bash
# 创建可被 Lambda 服务扮演的角色
aws iam create-role --role-name lambda-role --assume-role-policy-document file://trust-policy.json
```

---

**基本写法：列出角色**
`aws iam list-roles`
```bash
# 列出账号下所有角色
aws iam list-roles
```

---

**基本写法：附加策略到角色**
`aws iam attach-role-policy --role-name <角色名> --policy-arn <策略ARN>`
```bash
# 为角色附加执行策略
aws iam attach-role-policy --role-name lambda-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

---

## 用户组管理

**基本写法：创建用户组**
`aws iam create-group --group-name <组名>`
```bash
# 创建新的用户组
aws iam create-group --group-name developers
```

---

**基本写法：添加用户到组**
`aws iam add-user-to-group --group-name <组名> --user-name <用户名>`
```bash
# 将用户加入 developers 组
aws iam add-user-to-group --group-name developers --user-name john
```

---

**基本写法：列出组内用户**
`aws iam get-group --group-name <组名>`
```bash
# 查看 developers 组成员
aws iam get-group --group-name developers
```

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
| 云计算 AWS IAM 命令 | 034-AWSIAMCommand | 本文自身 |
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
