---
order: 420
title: 云计算 Terraform 状态与模块
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: 云计算 Terraform 状态与模块 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 云计算 Terraform 状态与模块

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 状态查看

**基本写法：列出状态中所有资源**
`terraform state list`
```bash
# 列出当前状态文件中所有资源
terraform state list
```

---

**基本写法：查看资源详情**
`terraform state show <资源类型>.<资源名>`
```bash
# 查看指定资源的状态属性
terraform state show aws_instance.example
```

---

**基本写法：以人类可读格式查看**
`terraform show`
```bash
# 显示整个状态文件
terraform show
```

---

**基本写法：以 JSON 输出状态**
`terraform show -json`
```bash
# 输出 JSON 格式状态便于程序解析
terraform show -json
```

---

**基本写法：查看所有输出值**
`terraform output`
```bash
# 显示所有 output 块的值
terraform output
```

---

**基本写法：查看单个输出**
`terraform output <输出名>`
```bash
# 查看指定输出值
terraform output instance_id
```

---

## 状态管理

**基本写法：拉取远程状态**
`terraform state pull`
```bash
# 从后端拉取状态到标准输出
terraform state pull
```

---

**基本写法：推送本地状态**
`terraform state push <状态文件>`
```bash
# 推送本地状态文件到远程后端
terraform state push terraform.tfstate
```

---

**基本写法：从状态中移除资源**
`terraform state rm <资源类型>.<资源名>`
```bash
# 移除资源但不销毁实际基础设施
terraform state rm aws_instance.example
```

---

**基本写法：重命名状态中的资源**
`terraform state mv <旧地址> <新地址>`
```bash
# 重命名状态中的资源地址
terraform state mv aws_instance.old aws_instance.new
```

---

**基本写法：替换资源**
`terraform apply -replace=<资源类型>.<资源名>`
```bash
# 强制销毁并重建指定资源
terraform apply -replace=aws_instance.example
```

---

**基本写法：检测漂移**
`terraform plan -refresh-only`
```bash
# 仅刷新状态检测实际漂移
terraform plan -refresh-only
```

---

## 资源导入

**基本写法：导入现有资源**
`terraform import <资源类型>.<资源名> <远程ID>`
```bash
# 将现有 EC2 实例导入到 Terraform 管理
terraform import aws_instance.example i-1234567890abcdef0
```

---

**基本写法：声明式导入块**
```hcl
# Terraform 1.5+ 支持的声明式导入
import {
  to = aws_instance.example
  id = "i-1234567890abcdef0"
}
```

---

**基本写法：生成导入配置**
`terraform plan -generate-config-out=<文件>`
```bash
# 为导入的资源生成配置代码
terraform plan -generate-config-out=generated.tf
```

---

## 工作空间

**基本写法：列出工作空间**
`terraform workspace list`
```bash
# 列出所有工作空间
terraform workspace list
```

---

**基本写法：创建工作空间**
`terraform workspace new <工作空间名>`
```bash
# 创建新的工作空间用于多环境管理
terraform workspace new production
```

---

**基本写法：切换工作空间**
`terraform workspace select <工作空间名>`
```bash
# 切换到指定工作空间
terraform workspace select production
```

---

**基本写法：查看当前工作空间**
`terraform workspace show`
```bash
# 输出当前激活的工作空间名
terraform workspace show
```

---

**基本写法：删除工作空间**
`terraform workspace delete <工作空间名>`
```bash
# 删除非当前激活的工作空间
terraform workspace delete staging
```

---

**基本写法：在配置中引用工作空间**
```hcl
# 根据工作空间区分环境配置
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = terraform.workspace == "production" ? "t3.medium" : "t3.micro"
}
```

---

## 后端配置

**基本写法：本地后端**
```hcl
# 默认本地后端
terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}
```

---

**基本写法：S3 远程后端**
```hcl
# 使用 S3 与 DynamoDB 实现远程状态与锁
terraform {
  backend "s3" {
    bucket         = "my-tfstate-bucket"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tf-locks"
    encrypt        = true
  }
}
```

---

**基本写法：后端初始化迁移**
`terraform init -migrate-state`
```bash
# 切换后端时迁移现有状态
terraform init -migrate-state
```

---

**基本写法：强制重新配置后端**
`terraform init -reconfigure`
```bash
# 忽略已有配置重新初始化后端
terraform init -reconfigure
```

---

## 模块引用

**基本写法：引用模块输出**
```hcl
# 引用子模块的输出值
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.public_subnet_id
}
```

---

**基本写法：从 Git 仓库引用模块**
```hcl
# 引用 Git 仓库中的模块
module "vpc" {
  source = "git::https://github.com/example/terraform-modules.git//vpc?ref=v1.2.0"
  cidr   = "10.0.0.0/16"
}
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
| 云计算 GCP Compute 与 Storage | 040-GCPComputeStorage | 本文的并列主题 |
| 云计算 Terraform 基础 | 041-TerraformBasic | 本文的前置基础 |
| 云计算 Terraform 状态与模块 | 042-TerraformStateModule | 本文自身 |
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
