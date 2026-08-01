---
order: 350
title: 云计算 AWS CloudFormation
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: 云计算 AWS CloudFormation 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 模板基础

**基本写法：YAML 模板结构**
```yaml
# CloudFormation 模板基本结构
AWSTemplateFormatVersion: '2010-09-09'
Description: My stack template
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-0c55b159cbfafe1f0
```

---

**基本写法：定义参数**
```yaml
# 通过参数实现模板复用
Parameters:
  InstanceType:
    Type: String
    Default: t2.micro
    AllowedValues: [t2.micro, t2.small, t3.micro]
```

---

**基本写法：定义输出**
```yaml
# 输出资源属性便于跨栈引用
Outputs:
  InstanceId:
    Value: !Ref MyInstance
    Export:
      Name: my-stack-instance-id
```

---

## 栈管理

**基本写法：创建栈**
`aws cloudformation create-stack --stack-name <栈名> --template-body file://<文件>`
```bash
# 从本地 YAML 文件创建栈
aws cloudformation create-stack --stack-name myStack --template-body file://template.yaml
```

---

**基本写法：从 S3 模板创建栈**
`aws cloudformation create-stack --stack-name <栈名> --template-url https://s3.amazonaws.com/<桶>/<键>`
```bash
# 从 S3 上的模板创建栈
aws cloudformation create-stack --stack-name myStack --template-url https://s3.amazonaws.com/my-bucket/template.yaml
```

---

**基本写法：更新栈**
`aws cloudformation update-stack --stack-name <栈名> --template-body file://<文件>`
```bash
# 应用模板变更更新栈
aws cloudformation update-stack --stack-name myStack --template-body file://template.yaml
```

---

**基本写法：删除栈**
`aws cloudformation delete-stack --stack-name <栈名>`
```bash
# 删除栈及所有资源
aws cloudformation delete-stack --stack-name myStack
```

---

**基本写法：列出所有栈**
`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE`
```bash
# 列出已成功创建与更新的栈
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE
```

---

**基本写法：查看栈详情**
`aws cloudformation describe-stacks --stack-name <栈名>`
```bash
# 查看栈状态与输出
aws cloudformation describe-stacks --stack-name myStack
```

---

## 变更集

**基本写法：创建变更集**
`aws cloudformation create-change-set --stack-name <栈名> --change-set-name <变更集名> --template-body file://<文件>`
```bash
# 预览变更生成变更集
aws cloudformation create-change-set --stack-name myStack --change-set-name my-change --template-body file://template.yaml
```

---

**基本写法：查看变更集**
`aws cloudformation describe-change-set --stack-name <栈名> --change-set-name <变更集名>`
```bash
# 查看变更集将要执行的操作
aws cloudformation describe-change-set --stack-name myStack --change-set-name my-change
```

---

**基本写法：执行变更集**
`aws cloudformation execute-change-set --stack-name <栈名> --change-set-name <变更集名>`
```bash
# 执行变更集中的操作
aws cloudformation execute-change-set --stack-name myStack --change-set-name my-change
```

---

## 事件与资源

**基本写法：查看栈事件**
`aws cloudformation describe-stack-events --stack-name <栈名>`
```bash
# 查看栈操作事件日志
aws cloudformation describe-stack-events --stack-name myStack
```

---

**基本写法：列出栈资源**
`aws cloudformation list-stack-resources --stack-name <栈名>`
```bash
# 查看栈内所有资源物理 ID
aws cloudformation list-stack-resources --stack-name myStack
```

---

## 验证与检查

**基本写法：验证模板**
`aws cloudformation validate-template --template-body file://<文件>`
```bash
# 检查模板语法是否正确
aws cloudformation validate-template --template-body file://template.yaml
```

---

**基本写法：估算栈费用**
`aws cloudformation estimate-template-cost --template-body file://<文件>`
```bash
# 估算模板部署后费用
aws cloudformation estimate-template-cost --template-body file://template.yaml
```

---

## 嵌套栈

**基本写法：嵌套栈资源**
```yaml
# 在主栈中嵌套子栈
Resources:
  NestedStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/my-bucket/nested.yaml
      Parameters:
        Env: production
```

---

## Drift 检测

**基本写法：检测栈漂移**
`aws cloudformation detect-stack-drift --stack-name <栈名>`
```bash
# 检测栈是否被外部修改
aws cloudformation detect-stack-drift --stack-name myStack
```

---

**基本写法：查看漂移结果**
`aws cloudformation describe-stack-drift-detection-status --stack-drift-detection-id <检测ID>`
```bash
# 查看漂移检测进度与结果
aws cloudformation describe-stack-drift-detection-status --stack-drift-detection-id abc-123
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
| 云计算 AWS CloudFormation | 035-AWSCloudFormation | 本文自身 |
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
