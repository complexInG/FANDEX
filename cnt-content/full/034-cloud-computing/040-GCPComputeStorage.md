---
order: 400
title: 云计算 GCP Compute 与 Storage
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: 云计算 GCP Compute 与 Storage 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Compute Engine 实例

**基本写法：列出所有实例**
`gcloud compute instances list`
```bash
# 列出当前项目所有 VM 实例
gcloud compute instances list
```

---

**基本写法：创建实例**
`gcloud compute instances create <实例名> [--machine-type=<类型>] [--image-family=<镜像族>] [--image-project=<项目>]`
```bash
# 创建 e2-medium Ubuntu 22.04 实例
gcloud compute instances create my-instance --machine-type=e2-medium --image-family=ubuntu-2204-lts --image-project=ubuntu-os-cloud
```

---

**基本写法：查看实例详情**
`gcloud compute instances describe <实例名> [--zone <可用区>]`
```bash
# 查看实例完整配置
gcloud compute instances describe my-instance --zone us-central1-a
```

---

**基本写法：启动实例**
`gcloud compute instances start <实例名> [--zone <可用区>]`
```bash
# 启动已停止的实例
gcloud compute instances start my-instance
```

---

**基本写法：停止实例**
`gcloud compute instances stop <实例名> [--zone <可用区>]`
```bash
# 停止运行中的实例
gcloud compute instances stop my-instance
```

---

**基本写法：重启实例**
`gcloud compute instances reset <实例名> [--zone <可用区>]`
```bash
# 强制重置实例
gcloud compute instances reset my-instance
```

---

**基本写法：删除实例**
`gcloud compute instances delete <实例名> [--zone <可用区>]`
```bash
# 删除实例及关联磁盘
gcloud compute instances delete my-instance
```

---

## SSH 连接

**基本写法：SSH 登录实例**
`gcloud compute ssh <实例名> [--zone <可用区>]`
```bash
# 自动管理密钥并 SSH 登录
gcloud compute ssh my-instance
```

---

**基本写法：使用 scp 传输文件**
`gcloud compute scp <本地文件> <实例名>:<远程路径> [--zone <可用区>]`
```bash
# 上传本地文件到实例
gcloud compute scp ./file.txt my-instance:~/file.txt
```

---

**基本写法：从实例下载文件**
`gcloud compute scp <实例名>:<远程路径> <本地路径>`
```bash
# 下载实例文件到本地
gcloud compute scp my-instance:~/log.txt ./
```

---

## 防火墙规则

**基本写法：列出防火墙规则**
`gcloud compute firewall-rules list`
```bash
# 查看所有防火墙规则
gcloud compute firewall-rules list
```

---

**基本写法：创建允许 HTTP 规则**
`gcloud compute firewall-rules create <规则名> --allow tcp:80 --source-ranges 0.0.0.0/0`
```bash
# 创建允许任意 IP 访问 80 端口的规则
gcloud compute firewall-rules create allow-http --allow tcp:80 --source-ranges 0.0.0.0/0
```

---

**基本写法：创建允许 SSH 规则**
`gcloud compute firewall-rules create <规则名> --allow tcp:22 --source-ranges <CIDR>`
```bash
# 允许特定 CIDR 通过 SSH 访问
gcloud compute firewall-rules create allow-ssh --allow tcp:22 --source-ranges 192.168.1.0/24
```

---

**基本写法：删除防火墙规则**
`gcloud compute firewall-rules delete <规则名>`
```bash
# 删除指定防火墙规则
gcloud compute firewall-rules delete allow-http
```

---

## Cloud Storage 桶

**基本写法：列出所有桶**
`gcloud storage buckets list`
```bash
# 列出项目下所有存储桶
gcloud storage buckets list
```

---

**基本写法：创建桶**
`gcloud storage buckets create gs://<桶名> [--location=<区域>]`
```bash
# 在指定区域创建桶
gcloud storage buckets create gs://my-unique-bucket --location=us-central1
```

---

**基本写法：列出桶内对象**
`gcloud storage ls gs://<桶名>/[<前缀>]`
```bash
# 列出桶内所有对象
gcloud storage ls gs://my-bucket
```

---

**基本写法：上传文件**
`gcloud storage cp <本地文件> gs://<桶名>/[<前缀>]`
```bash
# 上传本地文件到桶
gcloud storage cp ./file.txt gs://my-bucket/
```

---

**基本写法：下载文件**
`gcloud storage cp gs://<桶名>/<键> <本地路径>`
```bash
# 从桶下载文件到本地
gcloud storage cp gs://my-bucket/file.txt ./
```

---

**基本写法：同步目录**
`gcloud storage rsync <本地目录> gs://<桶名>/<前缀> [--delete]`
```bash
# 增量同步本地目录到桶
gcloud storage rsync ./src gs://my-bucket/src --delete
```

---

**基本写法：删除对象**
`gcloud storage rm gs://<桶名>/<键> [-r]`
```bash
# 递归删除桶内目录
gcloud storage rm gs://my-bucket/folder -r
```

---

**基本写法：删除桶**
`gcloud storage buckets delete gs://<桶名>`
```bash
# 删除空桶
gcloud storage buckets delete gs://my-bucket
```

---

## Cloud Run 部署

**基本写法：部署 Cloud Run 服务**
`gcloud run deploy --source . [--region <区域>] [--allow-unauthenticated]`
```bash
# 从源码部署并允许匿名访问
gcloud run deploy --source . --region us-central1 --allow-unauthenticated
```

---

**基本写法：列出 Cloud Run 服务**
`gcloud run services list`
```bash
# 列出所有 Cloud Run 服务
gcloud run services list
```

---

**基本写法：查看服务日志**
`gcloud run services logs tail <服务名> [--region <区域>]`
```bash
# 实时跟踪服务日志
gcloud run services logs tail my-service --region us-central1
```

---

**基本写法：删除 Cloud Run 服务**
`gcloud run services delete <服务名> [--region <区域>]`
```bash
# 删除指定服务
gcloud run services delete my-service --region us-central1
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
| 云计算 GCP gcloud 配置 | 039-GCPCliConfigure | 本文的并列主题 |
| 云计算 GCP Compute 与 Storage | 040-GCPComputeStorage | 本文自身 |
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
