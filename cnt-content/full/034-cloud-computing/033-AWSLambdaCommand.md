---
order: 330
title: 云计算 AWS Lambda 命令
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: 云计算 AWS Lambda 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 函数管理

**基本写法：列出函数**
`aws lambda list-functions [--region <区域>]`
```bash
# 列出当前区域所有 Lambda 函数
aws lambda list-functions
```

---

**基本写法：查看函数详情**
`aws lambda get-function --function-name <函数名>`
```bash
# 查看指定函数配置与代码位置
aws lambda get-function --function-name my-function
```

---

**基本写法：创建函数**
`aws lambda create-function --function-name <函数名> --runtime <运行时> --role <角色ARN> --handler <处理函数> --zip-file fileb://<zip 路径>`
```bash
# 创建 Python 函数
aws lambda create-function --function-name my-function --runtime python3.12 --role arn:aws:iam::123456789012:role/lambda-role --handler index.handler --zip-file fileb://function.zip
```

---

**基本写法：更新函数代码**
`aws lambda update-function-code --function-name <函数名> --zip-file fileb://<zip 路径>`
```bash
# 上传新的代码包
aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip
```

---

**基本写法：更新函数配置**
`aws lambda update-function-configuration --function-name <函数名> [--timeout <秒>] [--memory-size <MB>]`
```bash
# 修改超时与内存配置
aws lambda update-function-configuration --function-name my-function --timeout 30 --memory-size 512
```

---

**基本写法：删除函数**
`aws lambda delete-function --function-name <函数名>`
```bash
# 删除指定 Lambda 函数
aws lambda delete-function --function-name my-function
```

---

## 函数调用

**基本写法：同步调用**
`aws lambda invoke --function-name <函数名> <输出文件>`
```bash
# 同步调用并保存响应到文件
aws lambda invoke --function-name my-function response.json
```

---

**基本写法：异步调用**
`aws lambda invoke --function-name <函数名> --invocation-type Event <输出文件>`
```bash
# 异步调用不等待返回
aws lambda invoke --function-name my-function --invocation-type Event response.json
```

---

**基本写法：传递 payload**
`aws lambda invoke --function-name <函数名> --payload fileb://<文件> <输出文件>`
```bash
# 通过文件传递 JSON 载荷
aws lambda invoke --function-name my-function --payload fileb://payload.json response.json
```

---

**基本写法：指定别名或版本**
`aws lambda invoke --function-name <函数名>:<限定符> <输出文件>`
```bash
# 调用 prod 别名的版本
aws lambda invoke --function-name my-function:prod response.json
```

---

## 版本与别名

**基本写法：发布版本**
`aws lambda publish-version --function-name <函数名>`
```bash
# 发布当前代码为新版本
aws lambda publish-version --function-name my-function
```

---

**基本写法：列出版本**
`aws lambda list-versions-by-function --function-name <函数名>`
```bash
# 查看所有已发布版本
aws lambda list-versions-by-function --function-name my-function
```

---

**基本写法：创建别名**
`aws lambda create-alias --function-name <函数名> --name <别名> --function-version <版本号>`
```bash
# 为版本 1 创建 prod 别名
aws lambda create-alias --function-name my-function --name prod --function-version 1
```

---

**基本写法：更新别名指向**
`aws lambda update-alias --function-name <函数名> --name <别名> --function-version <版本号>`
```bash
# 将 prod 别名切换到版本 2
aws lambda update-alias --function-name my-function --name prod --function-version 2
```

---

## 层管理

**基本写法：发布层**
`aws lambda publish-layer-version --layer-name <层名> --zip-file fileb://<zip 路径> --compatible-runtimes <运行时>`
```bash
# 发布 Python 依赖层
aws lambda publish-layer-version --layer-name my-deps --zip-file fileb://layer.zip --compatible-runtimes python3.12
```

---

**基本写法：列出层**
`aws lambda list-layers`
```bash
# 列出账号下所有层
aws lambda list-layers
```

---

**基本写法：为函数附加层**
`aws lambda update-function-configuration --function-name <函数名> --layers <层ARN>`
```bash
# 将层附加到函数
aws lambda update-function-configuration --function-name my-function --layers arn:aws:lambda:us-east-1:123456789012:layer:my-deps:1
```

---

## 日志查看

**基本写法：查看日志组**
`aws logs describe-log-groups --log-group-name-prefix /aws/lambda/<函数名>`
```bash
# 查看 Lambda 函数对应日志组
aws logs describe-log-groups --log-group-name-prefix /aws/lambda/my-function
```

---

**基本写法：查看最近日志流**
`aws logs tail /aws/lambda/<函数名> [--since <时间>]`
```bash
# 查看最近 10 分钟的日志
aws logs tail /aws/lambda/my-function --since 10m
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
| 云计算 AWS Lambda 命令 | 033-AWSLambdaCommand | 本文自身 |
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
