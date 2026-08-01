---
order: 360
title: 云计算 Azure CLI 配置
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: 云计算 Azure CLI 配置 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 安装与版本

**基本写法：安装 Azure CLI**
`az` 或通过包管理器安装
```bash
# Windows 通过 winget 安装
winget install -e --id Microsoft.AzureCLI
```

---

**基本写法：查看版本**
`az version`
```bash
# 输出 CLI 版本与依赖库版本
az version
```

---

**基本写法：升级 CLI**
`az upgrade`
```bash
# 升级到最新版本
az upgrade
```

---

**基本写法：查看帮助**
`az [<命令组>] --help`
```bash
# 查看 vm 子命令帮助
az vm --help
```

---

**基本写法：模糊查找命令**
`az find "<关键词>"`
```bash
# 查找 role 相关命令
az find "az role"
```

---

## 登录认证

**基本写法：浏览器交互登录**
`az login`
```bash
# 通过浏览器进行交互式登录
az login
```

---

**基本写法：使用设备码登录**
`az login --use-device-code`
```bash
# 通过设备码进行双因素认证登录
az login --use-device-code
```

---

**基本写法：服务主体登录**
`az login --service-principal -u <应用ID> -p <密码或证书> --tenant <租户ID>`
```bash
# 通过服务主体登录便于脚本化
az login --service-principal -u 00000000-0000-0000-0000-000000000000 -p myPassword --tenant 00000000-0000-0000-0000-000000000000
```

---

**基本写法：登出**
`az logout [--username <用户名>]`
```bash
# 登出当前账号
az logout
```

---

## 订阅管理

**基本写法：列出订阅**
`az account list`
```bash
# 列出当前账号下所有订阅
az account list
```

---

**基本写法：列出订阅（简洁版）**
`az account subscription list`
```bash
# 列出租户下所有可用订阅
az account subscription list
```

---

**基本写法：设置当前订阅**
`az account set --subscription <订阅ID或名称>`
```bash
# 切换到指定订阅
az account set --subscription 0ad021f2-9dde-4cb1-8aa4-d71018aaeec8
```

---

**基本写法：查看当前订阅**
`az account show`
```bash
# 查看当前激活的订阅
az account show
```

---

## 配置管理

**基本写法：查看当前配置**
`az config get`
```bash
# 列出本地配置项
az config get
```

---

**基本写法：设置默认资源组**
`az config set defaults.group=<资源组名>`
```bash
# 设置默认资源组避免每次指定
az config set defaults.group=MyResourceGroup
```

---

**基本写法：关闭区域建议提示**
`az config set core.display_region_identified=no`
```bash
# 关闭区域推荐消息
az config set core.display_region_identified=no
```

---

## 输出格式

**基本写法：指定输出格式**
`az <命令> --output <json|table|tsv|yaml>`
```bash
# 以表格形式输出资源组
az group list --output table
```

---

**基本写法：使用 JMESPath 查询**
`az <命令> --query '<JMESPath 表达式>'`
```bash
# 仅提取资源组名称
az group list --query "[].name" --output tsv
```

---

**基本写法：列出可用区域**
`az account list-locations`
```bash
# 列出当前订阅支持的所有区域
az account list-locations
```

---

## 扩展管理

**基本写法：列出已安装扩展**
`az extension list`
```bash
# 查看已安装的 CLI 扩展
az extension list
```

---

**基本写法：安装扩展**
`az extension add --name <扩展名>`
```bash
# 安装特定扩展
az extension add --name azure-devops
```

---

**基本写法：移除扩展**
`az extension remove --name <扩展名>`
```bash
# 移除不再需要的扩展
az extension remove --name azure-devops
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
| 云计算 Azure CLI 配置 | 036-AzureCliConfigure | 本文自身 |
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
