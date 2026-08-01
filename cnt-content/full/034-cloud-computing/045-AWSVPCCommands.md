---
order: 450
title: AWS VPC 网络命令
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: AWS VPC 网络命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## VPC 创建与管理

**基本写法：创建 VPC**
`aws ec2 create-vpc --cidr-block <CIDR> [--instance-tenancy <租期>]`
```bash
# 创建 10.0.0.0/16 网段的 VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --instance-tenancy default
```

---

**基本写法：列出所有 VPC**
`aws ec2 describe-vpcs`
```bash
# 查看账户所有 VPC
aws ec2 describe-vpcs
```

---

**基本写法：查看指定 VPC**
`aws ec2 describe-vpcs --vpc-ids <VPC ID>`
```bash
# 查看指定 VPC 详情
aws ec2 describe-vpcs --vpc-ids vpc-12345678
```

---

**基本写法：删除 VPC**
`aws ec2 delete-vpc --vpc-id <VPC ID>`
```bash
# 删除指定 VPC(必须先删除其下所有资源)
aws ec2 delete-vpc --vpc-id vpc-12345678
```

---

**基本写法：为 VPC 添加名称标签**
`aws ec2 create-tags --resources <资源ID> --tags Key=Name,Value=<名称>`
```bash
# 给 VPC 添加名称
aws ec2 create-tags \
  --resources vpc-12345678 \
  --tags Key=Name,Value=my-vpc
```

---

## 子网管理

**基本写法：创建子网**
`aws ec2 create-subnet --vpc-id <VPC ID> --cidr-block <CIDR> [--availability-zone <AZ>]`
```bash
# 在 VPC 中创建子网
aws ec2 create-subnet \
  --vpc-id vpc-12345678 \
  --cidr-block 10.0.1.0/24 \
  --availability-zone us-east-1a
```

---

**基本写法：列出子网**
`aws ec2 describe-subnets [--filters Name=vpc-id,Values=<VPC ID>]`
```bash
# 查看指定 VPC 下所有子网
aws ec2 describe-subnets \
  --filters Name=vpc-id,Values=vpc-12345678
```

---

**基本写法：删除子网**
`aws ec2 delete-subnet --subnet-id <子网ID>`
```bash
# 删除指定子网
aws ec2 delete-subnet --subnet-id subnet-12345678
```

---

**基本写法：为子网开启公网映射**
`aws ec2 modify-subnet-attribute --subnet-id <子网ID> --map-public-ip-on-launch`
```bash
# 让子网中的实例自动获取公网 IP
aws ec2 modify-subnet-attribute \
  --subnet-id subnet-12345678 \
  --map-public-ip-on-launch
```

---

**基本写法：分配 IPv6 CIDR**
`aws ec2 associate-subnet-cidr-block --subnet-id <子网ID> --ipv6-cidr-block <IPv6 CIDR>`
```bash
# 为子网分配 IPv6 网段
aws ec2 associate-subnet-cidr-block \
  --subnet-id subnet-12345678 \
  --ipv6-cidr-block 2600:1f18:4113:b200::/64
```

---

## 路由表

**基本写法：创建路由表**
`aws ec2 create-route-table --vpc-id <VPC ID>`
```bash
# 在指定 VPC 创建路由表
aws ec2 create-route-table --vpc-id vpc-12345678
```

---

**基本写法：添加路由**
`aws ec2 create-route --route-table-id <路由表ID> --destination-cidr-block <CIDR> --gateway-id <网关ID>`
```bash
# 添加 0.0.0.0/0 默认路由到 Internet 网关
aws ec2 create-route \
  --route-table-id rtb-12345678 \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id igw-12345678
```

---

**基本写法：添加 NAT 网关路由**
`aws ec2 create-route --route-table-id <路由表ID> --destination-cidr-block <CIDR> --nat-gateway-id <NAT ID>`
```bash
# 私有子网通过 NAT 网关访问外网
aws ec2 create-route \
  --route-table-id rtb-12345678 \
  --destination-cidr-block 0.0.0.0/0 \
  --nat-gateway-id nat-12345678
```

---

**基本写法：关联子网**
`aws ec2 associate-route-table --route-table-id <路由表ID> --subnet-id <子网ID>`
```bash
# 将路由表关联到子网
aws ec2 associate-route-table \
  --route-table-id rtb-12345678 \
  --subnet-id subnet-12345678
```

---

**基本写法：列出路由表**
`aws ec2 describe-route-tables [--filters Name=vpc-id,Values=<VPC ID>]`
```bash
# 查看指定 VPC 的路由表
aws ec2 describe-route-tables \
  --filters Name=vpc-id,Values=vpc-12345678
```

---

## 网关

**基本写法：创建 Internet 网关**
`aws ec2 create-internet-gateway`
```bash
# 创建 Internet Gateway
aws ec2 create-internet-gateway
```

---

**基本写法：附加到 VPC**
`aws ec2 attach-internet-gateway --internet-gateway-id <网关ID> --vpc-id <VPC ID>`
```bash
# 将 IGW 附加到 VPC
aws ec2 attach-internet-gateway \
  --internet-gateway-id igw-12345678 \
  --vpc-id vpc-12345678
```

---

**基本写法：创建 NAT 网关**
`aws ec2 create-nat-gateway --subnet-id <子网ID> --allocation-id <EIP ID>`
```bash
# 在公有子网创建 NAT 网关
aws ec2 create-nat-gateway \
  --subnet-id subnet-12345678 \
  --allocation-id eipalloc-12345678
```

---

**基本写法：创建 VPC 端点**
`aws ec2 create-vpc-endpoint --vpc-id <VPC ID> --service-name <服务名> --route-table-ids <路由表ID>`
```bash
# 创建 S3 Gateway 端点
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-12345678 \
  --service-name com.amazonaws.us-east-1.s3 \
  --route-table-ids rtb-12345678
```

---

**基本写法：创建接口端点**
`aws ec2 create-vpc-endpoint --vpc-id <VPC ID> --vpc-endpoint-type Interface --service-name <服务名> --subnet-ids <子网ID>`
```bash
# 创建 PrivateLink 接口端点
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-12345678 \
  --vpc-endpoint-type Interface \
  --service-name com.amazonaws.us-east-1.ec2 \
  --subnet-ids subnet-12345678
```

---

## 安全组

**基本写法：创建安全组**
`aws ec2 create-security-group --group-name <组名> --description <描述> --vpc-id <VPC ID>`
```bash
# 在 VPC 中创建安全组
aws ec2 create-security-group \
  --group-name my-sg \
  --description "My security group" \
  --vpc-id vpc-12345678
```

---

**基本写法：添加入站规则**
`aws ec2 authorize-security-group-ingress --group-id <组ID> --protocol <协议> --port <端口> --cidr <CIDR>`
```bash
# 允许 0.0.0.0/0 访问 80 端口
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
```

---

**基本写法：添加 SSH 入站规则**
`aws ec2 authorize-security-group-ingress --group-id <组ID> --protocol tcp --port 22 --cidr <CIDR>`
```bash
# 仅允许指定 IP 访问 22 端口
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 22 \
  --cidr 203.0.113.0/24
```

---

**基本写法：移除入站规则**
`aws ec2 revoke-security-group-ingress --group-id <组ID> --protocol <协议> --port <端口> --cidr <CIDR>`
```bash
# 移除 80 端口的入站规则
aws ec2 revoke-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
```

---

**基本写法：引用其他安全组**
`aws ec2 authorize-security-group-ingress --group-id <组ID> --protocol tcp --port <端口> --source-group <源组ID>`
```bash
# 允许其他安全组中的实例访问本组 3306 端口
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 3306 \
  --source-group sg-87654321
```

---

## 网络访问控制列表

**基本写法：创建网络 ACL**
`aws ec2 create-network-acl --vpc-id <VPC ID>`
```bash
# 在 VPC 中创建网络 ACL
aws ec2 create-network-acl --vpc-id vpc-12345678
```

---

**基本写法：添加 ACL 规则**
`aws ec2 create-network-acl-entry --network-acl-id <ACL ID> --rule-number <序号> --protocol <协议> --rule-action <动作> --cidr-block <CIDR> --port-range From=<起>,To=<止>`
```bash
# 添加允许 HTTP 入站的 ACL 规则
aws ec2 create-network-acl-entry \
  --network-acl-id acl-12345678 \
  --rule-number 100 \
  --protocol 6 \
  --rule-action allow \
  --cidr-block 0.0.0.0/0 \
  --port-range From=80,To=80 \
  --egress false
```

---

**基本写法：关联子网**
`aws ec2 replace-network-acl-association --association-id <关联ID> --network-acl-id <ACL ID>`
```bash
# 将 ACL 关联到子网
aws ec2 replace-network-acl-association \
  --association-id aclassoc-12345678 \
  --network-acl-id acl-12345678
```

---

**基本写法：查看网络 ACL**
`aws ec2 describe-network-acls [--filters Name=vpc-id,Values=<VPC ID>]`
```bash
# 列出指定 VPC 的所有 ACL
aws ec2 describe-network-acls \
  --filters Name=vpc-id,Values=vpc-12345678
```

---

## 弹性 IP

**基本写法：分配弹性 IP**
`aws ec2 allocate-address --domain <域>`
```bash
# 为 VPC 分配弹性 IP
aws ec2 allocate-address --domain vpc
```

---

**基本写法：关联到实例**
`aws ec2 associate-address --instance-id <实例ID> --allocation-id <EIP ID>`
```bash
# 将弹性 IP 关联到 EC2 实例
aws ec2 associate-address \
  --instance-id i-1234567890abcdef0 \
  --allocation-id eipalloc-12345678
```

---

**基本写法：释放弹性 IP**
`aws ec2 release-address --allocation-id <EIP ID>`
```bash
# 释放未使用的弹性 IP
aws ec2 release-address --allocation-id eipalloc-12345678
```

---

**基本写法：查看所有弹性 IP**
`aws ec2 describe-addresses`
```bash
# 列出账户所有弹性 IP
aws ec2 describe-addresses
```

---

## Peering 与 VPN

**基本写法：创建 VPC Peering**
`aws ec2 create-vpc-peering-connection --vpc-id <本端VPC> --peer-vpc-id <对端VPC>`
```bash
# 创建 VPC 对等连接
aws ec2 create-vpc-peering-connection \
  --vpc-id vpc-12345678 \
  --peer-vpc-id vpc-87654321
```

---

**基本写法：接受 Peering 请求**
`aws ec2 accept-vpc-peering-connection --vpc-peering-connection-id <连接ID>`
```bash
# 接收 VPC 对等连接请求
aws ec2 accept-vpc-peering-connection \
  --vpc-peering-connection-id pcx-12345678
```

---

**基本写法：创建客户网关**
`aws ec2 create-customer-gateway --type ipsec.1 --public-ip <公网IP> --bgp-asn <ASN>`
```bash
# 创建 VPN 客户网关
aws ec2 create-customer-gateway \
  --type ipsec.1 \
  --public-ip 203.0.113.10 \
  --bgp-asn 65000
```

---

**基本写法：创建 VPN 连接**
`aws ec2 create-vpn-connection --customer-gateway-id <CGW ID> --vpn-gateway-id <VGW ID> --type ipsec.1`
```bash
# 建立 Site-to-Site VPN 连接
aws ec2 create-vpn-connection \
  --customer-gateway-id cgw-12345678 \
  --vpn-gateway-id vgw-12345678 \
  --type ipsec.1
```

---

## 流日志与网络监控

**基本写法：启用 VPC 流日志**
`aws ec2 create-flow-logs --resource-ids <资源ID> --resource-type <类型> --traffic-type <流量> --log-group-name <日志组>`
```bash
# 为 VPC 启用流日志记录所有流量
aws ec2 create-flow-logs \
  --resource-ids vpc-12345678 \
  --resource-type VPC \
  --traffic-type ALL \
  --log-group-name /aws/vpc/flowlogs \
  --deliver-logs-permission-arn arn:aws:iam::123456789012:role/FlowLogsRole
```

---

**基本写法：查看流日志**
`aws ec2 describe-flow-logs`
```bash
# 列出所有流日志配置
aws ec2 describe-flow-logs
```

---

**基本写法：删除流日志**
`aws ec2 delete-flow-logs --flow-log-ids <流日志ID>`
```bash
# 删除指定流日志
aws ec2 delete-flow-logs --flow-log-ids fl-12345678
```

---

**基本写法：启用 Reachability Analyzer**
`aws ec2 create-network-insights-path --source <资源ID> --destination <资源ID> --protocol <协议>`
```bash
# 创建路径分析(检查网络可达性)
aws ec2 create-network-insights-path \
  --source i-1234567890abcdef0 \
  --destination i-abcdef1234567890 \
  --protocol tcp
```

---

## Transit Gateway

**基本写法：创建 Transit Gateway**
`aws ec2 create-transit-gateway [--description <描述>]`
```bash
# 创建中转网关用于多 VPC 互联
aws ec2 create-transit-gateway --description "my-tgw"
```

---

**基本写法：附加 VPC 到 TGW**
`aws ec2 create-transit-gateway-vpc-attachment --transit-gateway-id <TGW ID> --vpc-id <VPC ID> --subnet-ids <子网ID列表>`
```bash
# 将 VPC 附加到中转网关
aws ec2 create-transit-gateway-vpc-attachment \
  --transit-gateway-id tgw-12345678 \
  --vpc-id vpc-12345678 \
  --subnet-ids subnet-12345678 subnet-87654321
```

---

**基本写法：查看 TGW 附件**
`aws ec2 describe-transit-gateway-attachments`
```bash
# 列出所有 TGW 附件
aws ec2 describe-transit-gateway-attachments
```

---

**基本写法：创建 TGW 路由**
`aws ec2 create-transit-gateway-route --destination-cidr-block <CIDR> --transit-gateway-route-table-id <表ID> --transit-gateway-attachment-id <附件ID>`
```bash
# 在 TGW 路由表中添加路由
aws ec2 create-transit-gateway-route \
  --destination-cidr-block 10.0.0.0/16 \
  --transit-gateway-route-table-id tgw-rtb-12345678 \
  --transit-gateway-attachment-id tgw-attach-12345678
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
| 云计算 Terraform 状态与模块 | 042-TerraformStateModule | 本文的并列主题 |
| AWS CloudWatch 监控日志命令 | 043-AWSCloudWatch | 本文的并列主题 |
| AWS RDS 数据库命令 | 044-AWSRDSCommands | 本文的并列主题 |
| AWS VPC 网络命令 | 045-AWSVPCCommands | 本文自身 |
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
