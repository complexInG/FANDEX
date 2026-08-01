---
order: 310
title: 云计算 AWS S3 命令
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: 云计算 AWS S3 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 桶操作

**基本写法：列出所有桶**
`aws s3 ls [--profile <配置名>]`
```bash
# 列出当前账号下所有 S3 桶
aws s3 ls
```

---

**基本写法：创建桶**
`aws s3 mb s3://<桶名> [--region <区域>]`
```bash
# 在默认区域创建新桶
aws s3 mb s3://my-unique-bucket
```

---

**基本写法：指定区域创建桶**
`aws s3 mb s3://<桶名> --region <区域>`
```bash
# 在 eu-west-1 区域创建桶
aws s3 mb s3://my-bucket --region eu-west-1
```

---

**基本写法：删除空桶**
`aws s3 rb s3://<桶名>`
```bash
# 仅删除空桶
aws s3 rb s3://my-bucket
```

---

**基本写法：强制删除非空桶**
`aws s3 rb s3://<桶名> --force`
```bash
# 删除桶及其所有对象
aws s3 rb s3://my-bucket --force
```

---

## 对象操作

**基本写法：列出桶内对象**
`aws s3 ls s3://<桶名>[/<前缀>] [--recursive]`
```bash
# 递归列出桶内所有对象
aws s3 ls s3://my-bucket --recursive
```

---

**基本写法：上传文件**
`aws s3 cp <本地文件> s3://<桶名>/[<路径>]`
```bash
# 上传单个文件到 S3
aws s3 cp file.txt s3://my-bucket/
```

---

**基本写法：下载文件**
`aws s3 cp s3://<桶名>/<键> <本地路径>`
```bash
# 从 S3 下载文件到本地
aws s3 cp s3://my-bucket/file.txt ./
```

---

**基本写法：递归上传目录**
`aws s3 cp <本地目录> s3://<桶名>/<前缀> --recursive`
```bash
# 递归上传整个目录
aws s3 cp ./folder s3://my-bucket/folder --recursive
```

---

**基本写法：同步本地到 S3**
`aws s3 sync <本地目录> s3://<桶名>/<前缀> [--delete] [--exclude <模式>]`
```bash
# 同步并删除目标中多余的文件
aws s3 sync ./src s3://my-bucket/src --delete --exclude "*.tmp"
```

---

**基本写法：删除单个对象**
`aws s3 rm s3://<桶名>/<键>`
```bash
# 删除指定对象
aws s3 rm s3://my-bucket/file.txt
```

---

**基本写法：递归删除目录**
`aws s3 rm s3://<桶名>/<前缀> --recursive`
```bash
# 递归删除目录下所有对象
aws s3 rm s3://my-bucket/folder --recursive
```

---

## 高级 API

**基本写法：使用 s3api 创建桶**
`aws s3api create-bucket --bucket <桶名> [--region <区域>]`
```bash
# 通过 s3api 精细控制创建桶
aws s3api create-bucket --bucket my-bucket --region us-east-1
```

---

**基本写法：获取桶大小统计**
`aws s3 ls s3://<桶名> --recursive --summarize`
```bash
# 统计桶内对象总数与总大小
aws s3 ls s3://my-bucket --recursive --summarize
```

---

**基本写法：预览操作不实际执行**
`<命令> --dryrun`
```bash
# 预览同步将执行的更改
aws s3 sync ./src s3://my-bucket/src --dryrun
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
| 云计算 AWS S3 命令 | 031-AWSS3Command | 本文自身 |
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
