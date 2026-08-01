---
order: 320
title: 云计算 AWS EC2 命令
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: 云计算 AWS EC2 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 实例查询

**基本写法：列出所有实例**
`aws ec2 describe-instances [--filters <过滤器>]`
```bash
# 列出当前账号所有 EC2 实例
aws ec2 describe-instances
```

---

**基本写法：过滤运行中实例**
`aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"`
```bash
# 仅列出 running 状态的实例
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"
```

---

**基本写法：查询指定字段**
`aws ec2 describe-instances --query '<JMESPath>' --output table`
```bash
# 提取实例 ID 类型状态公网 IP
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,PublicIpAddress]' --output table
```

---

## 实例生命周期

**基本写法：启动新实例**
`aws ec2 run-instances --image-id <AMI> --instance-type <类型> [--key-name <密钥名>] [--security-group-ids <安全组ID>]`
```bash
# 启动一台 t2.micro 实例
aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 --instance-type t2.micro --key-name my-key-pair
```

---

**基本写法：在 VPC 子网中启动**
`aws ec2 run-instances --image-id <AMI> --instance-type <类型> --subnet-id <子网ID> --security-group-ids <安全组ID>`
```bash
# 指定子网与安全组启动实例
aws ec2 run-instances --image-id ami-12345 --instance-type t3.small --subnet-id subnet-abc123 --security-group-ids sg-12345
```

---

**基本写法：启动已停止的实例**
`aws ec2 start-instances --instance-ids <实例ID>`
```bash
# 启动停止状态的实例
aws ec2 start-instances --instance-ids i-1234567890abcdef0
```

---

**基本写法：停止实例**
`aws ec2 stop-instances --instance-ids <实例ID>`
```bash
# 停止实例保留 EBS 卷
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
```

---

**基本写法：终止实例**
`aws ec2 terminate-instances --instance-ids <实例ID>`
```bash
# 永久终止实例并删除 EBS
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

---

**基本写法：重启实例**
`aws ec2 reboot-instances --instance-ids <实例ID>`
```bash
# 重启指定实例
aws ec2 reboot-instances --instance-ids i-1234567890abcdef0
```

---

## 密钥对

**基本写法：创建密钥对**
`aws ec2 create-key-pair --key-name <密钥名> --query 'KeyMaterial' --output text > <文件>`
```bash
# 创建密钥对并保存私钥到本地
aws ec2 create-key-pair --key-name my-new-key --query 'KeyMaterial' --output text > my-new-key.pem
```

---

**基本写法：列出密钥对**
`aws ec2 describe-key-pairs`
```bash
# 查看所有密钥对
aws ec2 describe-key-pairs
```

---

**基本写法：删除密钥对**
`aws ec2 delete-key-pair --key-name <密钥名>`
```bash
# 删除指定密钥对
aws ec2 delete-key-pair --key-name my-old-key
```

---

## 安全组

**基本写法：创建安全组**
`aws ec2 create-security-group --group-name <名称> --description <描述> [--vpc-id <VPC ID>]`
```bash
# 在指定 VPC 中创建安全组
aws ec2 create-security-group --group-name my-sg --description "My security group" --vpc-id vpc-12345
```

---

**基本写法：开放 SSH 端口**
`aws ec2 authorize-security-group-ingress --group-id <安全组ID> --protocol tcp --port 22 --cidr 0.0.0.0/0`
```bash
# 允许任意 IP 访问 22 端口
aws ec2 authorize-security-group-ingress --group-id sg-12345 --protocol tcp --port 22 --cidr 0.0.0.0/0
```

---

**基本写法：开放 HTTP 端口**
`aws ec2 authorize-security-group-ingress --group-id <安全组ID> --protocol tcp --port 80 --cidr 0.0.0.0/0`
```bash
# 允许任意 IP 访问 80 端口
aws ec2 authorize-security-group-ingress --group-id sg-12345 --protocol tcp --port 80 --cidr 0.0.0.0/0
```

---

**基本写法：撤销入站规则**
`aws ec2 revoke-security-group-ingress --group-id <安全组ID> --protocol tcp --port 22 --cidr 0.0.0.0/0`
```bash
# 撤销 SSH 入站规则
aws ec2 revoke-security-group-ingress --group-id sg-12345 --protocol tcp --port 22 --cidr 0.0.0.0/0
```

---

## EBS 卷

**基本写法：列出卷**
`aws ec2 describe-volumes [--filters <过滤器>]`
```bash
# 列出所有 EBS 卷
aws ec2 describe-volumes
```

---

**基本写法：创建卷**
`aws ec2 create-volume --availability-zone <可用区> --size <GB>`
```bash
# 在 us-east-1a 创建 100GB 卷
aws ec2 create-volume --availability-zone us-east-1a --size 100
```

---

**基本写法：附加卷到实例**
`aws ec2 attach-volume --volume-id <卷ID> --instance-id <实例ID> --device <设备名>`
```bash
# 将卷附加为 /dev/sdf
aws ec2 attach-volume --volume-id vol-12345 --instance-id i-1234567890abcdef0 --device /dev/sdf
```

---

**基本写法：创建快照**
`aws ec2 create-snapshot --volume-id <卷ID> [--description <描述>]`
```bash
# 为卷创建快照备份
aws ec2 create-snapshot --volume-id vol-12345 --description "Volume backup"
```

---

## 弹性 IP

**基本写法：分配弹性 IP**
`aws ec2 allocate-address --domain vpc`
```bash
# 在 VPC 中分配弹性 IP
aws ec2 allocate-address --domain vpc
```

---

**基本写法：关联弹性 IP 到实例**
`aws ec2 associate-address --instance-id <实例ID> --allocation-id <分配ID>`
```bash
# 将弹性 IP 绑定到实例
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345
```

---

**基本写法：释放弹性 IP**
`aws ec2 release-address --allocation-id <分配ID>`
```bash
# 释放未使用的弹性 IP
aws ec2 release-address --allocation-id eipalloc-12345
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
| 云计算 AWS EC2 命令 | 032-AWSEC2Command | 本文自身 |
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
