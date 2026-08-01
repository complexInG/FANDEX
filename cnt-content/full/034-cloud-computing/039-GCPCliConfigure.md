---
order: 390
title: 云计算 GCP gcloud 配置
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: 云计算 GCP gcloud 配置 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 安装与初始化

**基本写法：安装 gcloud CLI**
`sudo apt-get install -y google-cloud-cli`
```bash
# 在 Ubuntu 上通过官方源安装
sudo apt-get install -y google-cloud-cli
```

---

**基本写法：交互式初始化**
`gcloud init`
```bash
# 启动配置向导进行账号项目区域设置
gcloud init
```

---

**基本写法：查看安装信息**
`gcloud info`
```bash
# 显示 gcloud 安装路径与版本
gcloud info
```

---

**基本写法：查看版本**
`gcloud version`
```bash
# 输出 gcloud 及组件版本
gcloud version
```

---

**基本写法：升级组件**
`gcloud components update`
```bash
# 升级所有已安装组件
gcloud components update
```

---

## 认证登录

**基本写法：用户账号登录**
`gcloud auth login`
```bash
# 通过浏览器进行账号认证
gcloud auth login
```

---

**基本写法：应用默认凭证**
`gcloud auth application-default login`
```bash
# 为本地应用配置默认凭证
gcloud auth application-default login
```

---

**基本写法：列出已认证账号**
`gcloud auth list`
```bash
# 查看当前已登录账号列表
gcloud auth list
```

---

**基本写法：撤销认证**
`gcloud auth revoke [<账号>]`
```bash
# 撤销当前账号认证
gcloud auth revoke
```

---

## 项目管理

**基本写法：列出所有项目**
`gcloud projects list`
```bash
# 查看账号下所有项目
gcloud projects list
```

---

**基本写法：创建项目**
`gcloud projects create <项目ID>`
```bash
# 创建新项目
gcloud projects create my-new-project-123
```

---

**基本写法：查看项目详情**
`gcloud projects describe <项目ID>`
```bash
# 查看项目元数据
gcloud projects describe my-new-project-123
```

---

**基本写法：删除项目**
`gcloud projects delete <项目ID>`
```bash
# 删除指定项目
gcloud projects delete my-new-project-123
```

---

## 配置管理

**基本写法：列出当前配置**
`gcloud config list`
```bash
# 查看当前激活配置的属性
gcloud config list
```

---

**基本写法：设置默认项目**
`gcloud config set project <项目ID>`
```bash
# 设置默认项目避免每次指定
gcloud config set project my-project-id
```

---

**基本写法：设置默认区域**
`gcloud config set compute/region <区域>`
```bash
# 设置默认计算区域
gcloud config set compute/region us-central1
```

---

**基本写法：设置默认可用区**
`gcloud config set compute/zone <可用区>`
```bash
# 设置默认计算可用区
gcloud config set compute/zone us-central1-a
```

---

**基本写法：获取当前项目**
`gcloud config get-value project`
```bash
# 查看当前默认项目 ID
gcloud config get-value project
```

---

## 多配置管理

**基本写法：创建命名配置**
`gcloud config configurations create <配置名>`
```bash
# 创建独立配置用于多项目管理
gcloud config configurations create my-config
```

---

**基本写法：列出所有配置**
`gcloud config configurations list`
```bash
# 查看所有命名配置
gcloud config configurations list
```

---

**基本写法：切换激活配置**
`gcloud config configurations activate <配置名>`
```bash
# 切换到指定配置
gcloud config configurations activate my-config
```

---

**基本写法：查看当前配置名**
`gcloud config configurations describe <配置名>`
```bash
# 查看指定配置详情
gcloud config configurations describe my-config
```

---

## 组件管理

**基本写法：列出已安装组件**
`gcloud components list`
```bash
# 查看所有可用与已安装组件
gcloud components list
```

---

**基本写法：安装组件**
`gcloud components install <组件名>`
```bash
# 安装 kubectl 等额外组件
gcloud components install kubectl
```

---

**基本写法：移除组件**
`gcloud components remove <组件名>`
```bash
# 移除不再使用的组件
gcloud components remove kubectl
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
| 云计算 AWS IAM 命令 | 034-AWSIAMCommand | 本文的并列主题 |
| 云计算 AWS CloudFormation | 035-AWSCloudFormation | 本文的并列主题 |
| 云计算 Azure CLI 配置 | 036-AzureCliConfigure | 本文的并列主题 |
| 云计算 Azure 资源组与 VM | 037-AzureGroupVMCommand | 本文的并列主题 |
| 云计算 Azure 存储命令 | 038-AzureStorageCommand | 本文的并列主题 |
| 云计算 GCP gcloud 配置 | 039-GCPCliConfigure | 本文自身 |
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
