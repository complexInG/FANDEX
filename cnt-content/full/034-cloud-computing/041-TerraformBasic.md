---
order: 410
title: 云计算 Terraform 基础
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: 云计算 Terraform 基础 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 云计算 Terraform 基础

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 模板语法

**基本写法：provider 声明**
```hcl
# 声明使用的云提供商与区域
provider "aws" {
  region = "us-east-1"
}
```

---

**基本写法：resource 资源块**
```hcl
# 定义 EC2 实例资源
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

---

**基本写法：variable 输入变量**
```hcl
# 定义可由外部传入的变量
variable "instance_type" {
  type    = string
  default = "t2.micro"
}
```

---

**基本写法：output 输出值**
```hcl
# 输出资源属性供其他模块引用
output "instance_id" {
  value = aws_instance.example.id
}
```

---

**基本写法：引用变量与资源**
```hcl
# 在资源中引用变量
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type
}
```

---

## 核心工作流

**基本写法：初始化工作目录**
`terraform init`
```bash
# 下载 provider 插件并初始化后端
terraform init
```

---

**基本写法：升级初始化**
`terraform init -upgrade`
```bash
# 升级 provider 与模块到允许的最新版本
terraform init -upgrade
```

---

**基本写法：预览变更**
`terraform plan`
```bash
# 预览将要创建修改销毁的资源
terraform plan
```

---

**基本写法：保存计划到文件**
`terraform plan -out=<文件名>`
```bash
# 将计划保存到文件供 apply 使用
terraform plan -out=tf.tfplan
```

---

**基本写法：应用变更**
`terraform apply`
```bash
# 应用配置变更需手动确认
terraform apply
```

---

**基本写法：自动确认应用**
`terraform apply -auto-approve`
```bash
# 应用变更无需确认适合 CI/CD
terraform apply -auto-approve
```

---

**基本写法：应用指定计划**
`terraform apply <计划文件>`
```bash
# 应用预先保存的计划文件
terraform apply tf.tfplan
```

---

**基本写法：销毁所有资源**
`terraform destroy`
```bash
# 销毁当前配置管理的所有资源
terraform destroy
```

---

**基本写法：销毁单个资源**
`terraform destroy -target=<资源类型>.<资源名>`
```bash
# 仅销毁指定资源
terraform destroy -target=aws_instance.example
```

---

## 验证与格式化

**基本写法：语法校验**
`terraform validate`
```bash
# 检查配置语法与一致性
terraform validate
```

---

**基本写法：格式化代码**
`terraform fmt`
```bash
# 将配置文件格式化为规范风格
terraform fmt
```

---

**基本写法：递归格式化**
`terraform fmt -recursive`
```bash
# 递归格式化所有子目录文件
terraform fmt -recursive
```

---

**基本写法：检查格式但不修改**
`terraform fmt -check`
```bash
# 检查格式不规范则退出码 1
terraform fmt -check
```

---

## 变量传递

**基本写法：命令行传变量**
`terraform plan -var "<键>=<值>"`
```bash
# 通过命令行传入变量值
terraform plan -var "instance_type=t3.small"
```

---

**基本写法：使用变量定义文件**
`terraform plan -var-file=<文件>`
```bash
# 通过 tfvars 文件传入多个变量
terraform plan -var-file=prod.tfvars
```

---

**基本写法：查看所有输出**
`terraform output`
```bash
# 查看应用后的输出值
terraform output
```

---

**基本写法：查看 JSON 格式输出**
`terraform output -json`
```bash
# 以 JSON 格式输出便于脚本解析
terraform output -json
```

---

## 模块管理

**基本写法：使用本地模块**
```hcl
# 引用本地子模块
module "vpc" {
  source = "./modules/vpc"
  cidr   = "10.0.0.0/16"
}
```

---

**基本写法：使用 Registry 模块**
```hcl
# 引用 Terraform Registry 上的官方模块
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"
  cidr    = "10.0.0.0/16"
}
```

---

**基本写法：下载与更新模块**
`terraform get [-update]`
```bash
# 下载引用的模块
terraform get -update
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
| 云计算 Terraform 基础 | 041-TerraformBasic | 本文自身 |
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
