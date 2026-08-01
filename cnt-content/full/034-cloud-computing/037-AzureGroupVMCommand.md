---
order: 370
title: 云计算 Azure 资源组与 VM
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: 云计算 Azure 资源组与 VM 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 资源组管理

**基本写法：创建资源组**
`az group create --name <资源组名> --location <区域>`
```bash
# 在 eastus 区域创建资源组
az group create --name MyResourceGroup --location eastus
```

---

**基本写法：列出所有资源组**
`az group list [--output table]`
```bash
# 以表格形式列出资源组
az group list --output table
```

---

**基本写法：查看资源组详情**
`az group show --name <资源组名>`
```bash
# 查看指定资源组信息
az group show --name MyResourceGroup
```

---

**基本写法：删除资源组**
`az group delete --name <资源组名> [--yes] [--no-wait]`
```bash
# 删除资源组及所有资源不等待
az group delete --name MyResourceGroup --yes --no-wait
```

---

**基本写法：按名称过滤资源组**
`az group list --query "[?starts_with(name, 'msdocs') == \`true\`].name" -o table`
```bash
# 列出以 msdocs 开头的资源组
az group list --query "[?starts_with(name, 'msdocs') == \`true\`].name" -o table
```

---

## 虚拟机创建

**基本写法：创建 Ubuntu VM**
`az vm create --resource-group <资源组名> --name <VM名> --image Ubuntu2204 [--admin-username <用户名>] [--generate-ssh-keys]`
```bash
# 创建 Ubuntu 22.04 VM 并自动生成 SSH 密钥
az vm create --resource-group MyResourceGroup --name my-vm --image Ubuntu2204 --admin-username azureuser --generate-ssh-keys
```

---

**基本写法：指定镜像与大小创建**
`az vm create --resource-group <资源组名> --name <VM名> --image <镜像> --size <VM大小>`
```bash
# 创建 Standard_B2s 大小的 VM
az vm create --resource-group MyResourceGroup --name my-vm --image Ubuntu2204 --size Standard_B2s
```

---

**基本写法：在 VNet 子网中创建**
`az vm create --resource-group <资源组名> --name <VM名> --image <镜像> --vnet-name <VNet名> --subnet <子网名>`
```bash
# 指定虚拟网络与子网创建 VM
az vm create --resource-group test-rg --name vm-public --image Ubuntu2204 --vnet-name vnet-1 --subnet subnet-public
```

---

**基本写法：使用已有 SSH 公钥**
`az vm create --resource-group <资源组名> --name <VM名> --image <镜像> --ssh-key-values <公钥路径>`
```bash
# 使用本地公钥创建 VM
az vm create --resource-group MyResourceGroup --name my-vm --image Ubuntu2204 --ssh-key-values ~/.ssh/id_rsa.pub
```

---

## VM 查询

**基本写法：列出所有 VM**
`az vm list [--resource-group <资源组名>] [-d]`
```bash
# 列出所有 VM 并显示电源状态
az vm list -d
```

---

**基本写法：查看 VM 详情**
`az vm show --resource-group <资源组名> --name <VM名>`
```bash
# 查看 VM 完整配置
az vm show --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：按创建时间过滤 VM**
`az vm list -d --query "[?timeCreated >= '2024-01-01'].[name, powerState]"`
```bash
# 查询 2024 年后创建的 VM
az vm list -d --query "[?timeCreated >= '2024-01-01'].[name, powerState]"
```

---

## VM 生命周期

**基本写法：启动 VM**
`az vm start --resource-group <资源组名> --name <VM名>`
```bash
# 启动已停止的 VM
az vm start --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：停止 VM**
`az vm stop --resource-group <资源组名> --name <VM名>`
```bash
# 停止运行中的 VM
az vm stop --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：分配（释放计算资源）**
`az vm deallocate --resource-group <资源组名> --name <VM名>`
```bash
# 释放 VM 不再产生计算费用
az vm deallocate --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：重启 VM**
`az vm restart --resource-group <资源组名> --name <VM名>`
```bash
# 重启指定 VM
az vm restart --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：删除 VM**
`az vm delete --resource-group <资源组名> --name <VM名> [--yes]`
```bash
# 删除 VM 不询问确认
az vm delete --resource-group MyResourceGroup --name my-vm --yes
```

---

## VM 连接

**基本写法：获取 SSH 连接信息**
`az vm show --resource-group <资源组名> --name <VM名> -d --query publicIps -o tsv`
```bash
# 获取 VM 公网 IP 用于 SSH 连接
az vm show --resource-group MyResourceGroup --name my-vm -d --query publicIps -o tsv
```

---

**基本写法：打开端口**
`az vm open-port --resource-group <资源组名> --name <VM名> --port <端口>`
```bash
# 打开 80 端口入站
az vm open-port --resource-group MyResourceGroup --name my-vm --port 80
```

---

**基本写法：执行远程命令**
`az vm run-command invoke --resource-group <资源组名> --name <VM名> --command-id RunShellScript --scripts "<命令>"`
```bash
# 远程执行 shell 命令
az vm run-command invoke --resource-group MyResourceGroup --name my-vm --command-id RunShellScript --scripts "uptime"
```

---

## 磁盘管理

**基本写法：列出磁盘**
`az disk list --resource-group <资源组名>`
```bash
# 列出资源组下所有托管磁盘
az disk list --resource-group MyResourceGroup
```

---

**基本写法：创建磁盘**
`az disk create --resource-group <资源组名> --name <磁盘名> --size-gb <GB>`
```bash
# 创建 20GB 数据磁盘
az disk create --resource-group MyResourceGroup --name my-disk --size-gb 20
```

---

**基本写法：附加磁盘到 VM**
`az vm disk attach --resource-group <资源组名> --vm-name <VM名> --name <磁盘名>`
```bash
# 将现有磁盘附加到 VM
az vm disk attach --resource-group MyResourceGroup --vm-name my-vm --name my-disk
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
| 云计算 Azure 资源组与 VM | 037-AzureGroupVMCommand | 本文自身 |
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
