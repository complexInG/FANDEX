---
order: 550
title: AWS CloudFront CDN 命令
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: AWS CloudFront CDN 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 分配创建

**基本写法：创建分配最小配置**
`aws cloudfront create-distribution --distribution-config <JSON>`
```bash
# 创建最小可用的 CloudFront 分配
aws cloudfront create-distribution --distribution-config '{
  "CallerReference": "my-distribution-001",
  "Comment": "My CDN distribution",
  "Enabled": true,
  "Origins": {
    "Quantity": 1,
    "Items": [{
      "Id": "my-origin",
      "DomainName": "my-bucket.s3.amazonaws.com",
      "S3OriginConfig": {"OriginAccessIdentity": ""}
    }]
  },
  "DefaultCacheBehavior": {
    "TargetOriginId": "my-origin",
    "ViewerProtocolPolicy": "redirect-to-https",
    "TrustedSigners": {"Enabled": false, "Quantity": 0},
    "ForwardedValues": {"QueryString": false, "Cookies": {"Forward": "none"}, "Headers": {"Quantity": 0}, "QueryStringCacheKeys": {"Quantity": 0}},
    "MinTTL": 0,
    "DefaultTTL": 3600,
    "MaxTTL": 86400
  }
}'
```

---

**基本写法：使用文件配置创建**
`aws cloudfront create-distribution --distribution-config file://<文件>`
```bash
# 通过 JSON 文件创建分配
aws cloudfront create-distribution --distribution-config file://distribution.json
```

---

**基本写法：列出分配**
`aws cloudfront list-distributions`
```bash
# 列出账户下所有分配
aws cloudfront list-distributions
```

---

**基本写法：查看分配详情**
`aws cloudfront get-distribution --id <分配ID>`
```bash
# 查看指定分配详情
aws cloudfront get-distribution --id E1A2B3C4D5E6F7
```

---

**基本写法：删除分配**
`aws cloudfront delete-distribution --id <分配ID> --if-match <ETag>`
```bash
# 删除指定分配(必须先禁用)
aws cloudfront delete-distribution --id E1A2B3C4D5E6F7 --if-match E2QWERTYUIOP
```

---

## 分配配置

**基本写法：禁用分配**
`aws cloudfront update-distribution --distribution-config <JSON> --id <分配ID> --if-match <ETag>`
```bash
# 设置 Enabled 为 false 禁用分配
aws cloudfront update-distribution \
  --distribution-config file://disabled-config.json \
  --id E1A2B3C4D5E6F7 \
  --if-match E2QWERTYUIOP
```

---

**基本写法：启用分配**
`aws cloudfront update-distribution --id <分配ID> --if-match <ETag>`
```bash
# 修改配置启用已禁用的分配
aws cloudfront update-distribution \
  --distribution-config file://enabled-config.json \
  --id E1A2B3C4D5E6F7 \
  --if-match E2QWERTYUIOP
```

---

**基本写法：更新缓存行为**
```json
{
  "DefaultCacheBehavior": {
    "TargetOriginId": "my-origin",
    "ViewerProtocolPolicy": "https-only",
    "TrustedSigners": {"Enabled": false, "Quantity": 0},
    "ForwardedValues": {
      "QueryString": true,
      "Cookies": {"Forward": "all"},
      "Headers": {"Quantity": 2, "Items": ["Origin", "Access-Control-Request-Method"]},
      "QueryStringCacheKeys": {"Quantity": 0}
    },
    "MinTTL": 0,
    "DefaultTTL": 300,
    "MaxTTL": 3600,
    "AllowedMethods": {"Quantity": 7, "Items": ["GET", "HEAD", "OPTIONS", "PUT", "POST", "PATCH", "DELETE"]}
  }
}
```

---

**基本写法：配置自定义错误页面**
```json
{
  "CustomErrorResponses": {
    "Quantity": 1,
    "Items": [{
      "ErrorCode": 404,
      "ResponsePagePath": "/404.html",
      "ResponseCode": "404",
      "ErrorCachingMinTTL": 300
    }]
  }
}
```

---

**基本写法：配置地理限制**
`aws cloudfront update-distribution --distribution-config <JSON> --id <分配ID>`
```json
{
  "Restrictions": {
    "GeoRestriction": {
      "RestrictionType": "whitelist",
      "Quantity": 2,
      "Items": ["CN", "US"]
    }
  }
}
```

---

## 源站配置

**基本写法：S3 源配置**
```json
{
  "Origins": {
    "Quantity": 1,
    "Items": [{
      "Id": "s3-origin",
      "DomainName": "my-bucket.s3.amazonaws.com",
      "S3OriginConfig": {
        "OriginAccessIdentity": "origin-access-identity/cloudfront/E1A2B3C4D5E6F7"
      }
    }]
  }
}
```

---

**基本写法：自定义源配置**
```json
{
  "Origins": {
    "Quantity": 1,
    "Items": [{
      "Id": "custom-origin",
      "DomainName": "www.example.com",
      "CustomOriginConfig": {
        "HTTPPort": 80,
        "HTTPSPort": 443,
        "OriginProtocolPolicy": "https-only",
        "OriginSslProtocols": {"Quantity": 2, "Items": ["TLSv1.2", "TLSv1.3"]}
      }
    }]
  }
}
```

---

**基本写法：创建源访问身份**
`aws cloudfront create-cloud-front-origin-access-identity --cloud-front-origin-access-identity-config <JSON>`
```bash
# 创建 OAI 用于 S3 源访问控制
aws cloudfront create-cloud-front-origin-access-identity \
  --cloud-front-origin-access-identity-config \
  '{"CallerReference":"my-oai","Comment":"OAI for my-bucket"}'
```

---

**基本写法：配置源组故障转移**
```json
{
  "OriginGroups": {
    "Quantity": 1,
    "Items": [{
      "Id": "my-origin-group",
      "Members": {
        "Quantity": 2,
        "Items": [
          {"OriginId": "primary-origin"},
          {"OriginId": "secondary-origin"}
        ]
      },
      "FailoverCriteria": {
        "StatusCodes": {"Quantity": 3, "Items": [500, 502, 503]}
      }
    }]
  }
}
```

---

**基本写法：源路径模式路由**
```json
{
  "CacheBehaviors": {
    "Quantity": 1,
    "Items": [{
      "PathPattern": "/images/*",
      "TargetOriginId": "images-origin",
      "ViewerProtocolPolicy": "redirect-to-https",
      "TrustedSigners": {"Enabled": false, "Quantity": 0},
      "ForwardedValues": {"QueryString": false, "Cookies": {"Forward": "none"}, "Headers": {"Quantity": 0}, "QueryStringCacheKeys": {"Quantity": 0}},
      "MinTTL": 0
    }]
  }
}
```

---

## 失效与缓存

**基本写法：创建失效**
`aws cloudfront create-invalidation --distribution-id <分配ID> --paths <路径>`
```bash
# 失效指定路径的缓存
aws cloudfront create-invalidation \
  --distribution-id E1A2B3C4D5E6F7 \
  --paths "/index.html" "/images/*"
```

---

**基本写法：失效所有文件**
`aws cloudfront create-invalidation --distribution-id <分配ID> --paths "/*"`
```bash
# 失效整个分配的缓存
aws cloudfront create-invalidation \
  --distribution-id E1A2B3C4D5E6F7 \
  --paths "/*"
```

---

**基本写法：查看失效状态**
`aws cloudfront get-invalidation --distribution-id <分配ID> --id <失效ID>`
```bash
# 查询失效操作进度
aws cloudfront get-invalidation \
  --distribution-id E1A2B3C4D5E6F7 \
  --id I1A2B3C4D5E6F7
```

---

**基本写法：列出失效**
`aws cloudfront list-invalidations --distribution-id <分配ID>`
```bash
# 列出最近的失效记录
aws cloudfront list-invalidations \
  --distribution-id E1A2B3C4D5E6F7
```

---

**基本写法：配置缓存策略**
`aws cloudfront create-cache-policy --cache-policy-config <JSON>`
```bash
# 创建自定义缓存策略
aws cloudfront create-cache-policy --cache-policy-config '{
  "Name": "my-cache-policy",
  "Comment": "My custom cache policy",
  "DefaultTTL": 3600,
  "MaxTTL": 86400,
  "MinTTL": 0,
  "ParametersInCacheKeyAndForwardedToOrigin": {
    "EnableAcceptEncodingGzip": true,
    "EnableAcceptEncodingBrotli": true,
    "HeadersConfig": {"HeaderBehavior": "none"},
    "CookiesConfig": {"CookieBehavior": "none"},
    "QueryStringsConfig": {"QueryStringBehavior": "none"}
  }
}'
```

---

## 源访问控制

**基本写法：创建源访问控制**
`aws cloudfront create-origin-access-control --origin-access-control-config <JSON>`
```bash
# 创建 OAC(推荐替代 OAI)
aws cloudfront create-origin-access-control --origin-access-control-config '{
  "Name": "my-oac",
  "Description": "OAC for S3 origin",
  "SigningProtocol": "sigv4",
  "SigningBehavior": "always",
  "OriginAccessControlOriginType": "s3"
}'
```

---

**基本写法：列出源访问控制**
`aws cloudfront list-origin-access-controls`
```bash
# 列出所有 OAC
aws cloudfront list-origin-access-controls
```

---

**基本写法：删除源访问控制**
`aws cloudfront delete-origin-access-control --id <ID> --if-match <ETag>`
```bash
# 删除指定 OAC
aws cloudfront delete-origin-access-control \
  --id E1A2B3C4D5E6F7 \
  --if-match E2QWERTYUIOP
```

---

**基本写法：S3 桶策略授权 CloudFront**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Service": "cloudfront.amazonaws.com"
    },
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::my-bucket/*",
    "Condition": {
      "StringEquals": {
        "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7"
      }
    }
  }]
}
```

---

## TLS/SSL 证书

**基本写法：配置 SSL 证书**
```json
{
  "ViewerCertificate": {
    "ACMCertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/abc-def-ghi",
    "SSLSupportMethod": "sni-only",
    "MinimumProtocolVersion": "TLSv1.2_2021",
    "Certificate": "arn:aws:acm:us-east-1:123456789012:certificate/abc-def-ghi",
    "CertificateSource": "acm"
  }
}
```

---

**基本写法：ACM 申请证书**
`aws acm request-certificate --domain-name <域名> --validation-method DNS`
```bash
# 在 us-east-1 区域申请证书(CloudFront 必需)
aws acm request-certificate \
  --domain-name "*.example.com" \
  --validation-method DNS \
  --region us-east-1
```

---

**基本写法：查看证书**
`aws acm describe-certificate --certificate-arn <ARN>`
```bash
# 查看证书状态与验证信息
aws acm describe-certificate \
  --certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/abc-def-ghi \
  --region us-east-1
```

---

**基本写法：配置备用域名**
```json
{
  "Aliases": {
    "Quantity": 2,
    "Items": ["www.example.com", "cdn.example.com"]
  }
}
```

---

**基本写法：配置安全策略**
```json
{
  "ViewerCertificate": {
    "MinimumProtocolVersion": "TLSv1.2_2021",
    "SSLSupportMethod": "sni-only"
  }
}
```

---

## 函数与 Lambda@Edge

**基本写法：创建 CloudFront 函数**
`aws cloudfront create-function --name <函数名> --function-code <代码> --function-config <配置>`
```bash
# 创建 CloudFront 函数
aws cloudfront create-function \
  --name my-function \
  --function-code fileb://function.js \
  --function-config '{"Comment":"My function","Runtime":"cloudfront-js-2.0"}'
```

---

**基本写法：发布函数**
`aws cloudfront publish-function --name <函数名> --if-match <ETag>`
```bash
# 发布函数使其可关联到分配
aws cloudfront publish-function \
  --name my-function \
  --if-match ETVERTYUIOPASDF
```

---

**基本写法：测试函数**
`aws cloudfront test-function --name <函数名> --if-match <ETag> --event-object <事件>`
```bash
# 测试函数处理指定事件
aws cloudfront test-function \
  --name my-function \
  --if-match ETVERTYUIOPASDF \
  --event-object fileb://event.json
```

---

**基本写法：关联函数到分配**
```json
{
  "DefaultCacheBehavior": {
    "FunctionAssociations": {
      "Quantity": 1,
      "Items": [{
        "FunctionARN": "arn:aws:cloudfront::123456789012:function/my-function",
        "EventType": "viewer-request"
      }]
    }
  }
}
```

---

**基本写法：列出函数**
`aws cloudfront list-functions`
```bash
# 列出所有 CloudFront 函数
aws cloudfront list-functions
```

---

## 实时日志与监控

**基本写法：创建实时日志配置**
`aws cloudfront create-realtime-log-config --end-points <端点> --fields <字段> --name <名称> --sampling-rate <比率>`
```bash
# 创建实时日志推送到 Kinesis
aws cloudfront create-realtime-log-config \
  --end-points '[{"StreamType":"Kinesis","Endpoint":{"Stream":{"Arn":"arn:aws:kinesis:us-east-1:123456789012:stream/my-stream","RoleArn":"arn:aws:iam::123456789012:role/cf-realtime"}}}]' \
  --fields '["timestamp","c-ip","time-to-first-byte","sc-status"]' \
  --name my-realtime-log \
  --sampling-rate 100
```

---

**基本写法：查看实时日志配置**
`aws cloudfront get-realtime-log-config --name <名称>`
```bash
# 查看指定实时日志配置
aws cloudfront get-realtime-log-config --name my-realtime-log
```

---

**基本写法：列出实时日志配置**
`aws cloudfront list-realtime-log-configs`
```bash
# 列出所有实时日志配置
aws cloudfront list-realtime-log-configs
```

---

**基本写法：删除实时日志配置**
`aws cloudfront delete-realtime-log-config --name <名称>`
```bash
# 删除指定实时日志配置
aws cloudfront delete-realtime-log-config --name my-realtime-log
```

---

**基本写法：监控分配指标**
`aws cloudwatch get-metric-statistics --namespace AWS/CloudFront --metric-name Requests`
```bash
# 查看 CloudFront 请求量指标
aws cloudwatch get-metric-statistics \
  --namespace AWS/CloudFront \
  --metric-name Requests \
  --dimensions Name=DistributionId,Value=E1A2B3C4D5E6F7 \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --statistics Sum
```

---

## 标签管理

**基本写法：添加标签**
`aws cloudfront tag-resource --resource <ARN> --tags <标签>`
```bash
# 为分配添加标签
aws cloudfront tag-resource \
  --resource arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7 \
  --tags 'Items=[{Key=Environment,Value=Production},{Key=Team,Value=DevOps}]'
```

---

**基本写法：查看标签**
`aws cloudfront list-tags-for-resource --resource <ARN>`
```bash
# 查看分配的所有标签
aws cloudfront list-tags-for-resource \
  --resource arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7
```

---

**基本写法：移除标签**
`aws cloudfront untag-resource --resource <ARN> --tag-keys <键列表>`
```bash
# 移除指定标签
aws cloudfront untag-resource \
  --resource arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7 \
  --tag-keys 'Items=[Environment]'
```

---

## 复制与迁移

**基本写法：复制分配配置**
```bash
# 通过脚本复制分配到新分配
ETAG=$(aws cloudfront get-distribution --id E1A2B3C4D5E6F7 --query 'ETag' --output text)
aws cloudfront get-distribution-config --id E1A2B3C4D5E6F7 --query 'DistributionConfig' > copy-config.json
# 修改 CallerReference 后使用 create-distribution 创建
```

---

**基本写法：跨账户迁移**
```bash
# 导出当前分配配置
aws cloudfront get-distribution-config --id E1A2B3C4D5E6F7 > export.json
# 在目标账户创建新分配
aws cloudfront create-distribution --distribution-config file://export.json --profile target-account
```

---

**基本写法：列出标签为某值的分配**
```bash
# 查询特定环境的所有分配
aws resourcegroupstaggingapi get-resources \
  --tag-filters Key=Environment,Values=Production \
  --resource-type-filters cloudfront:distribution
```

---

**基本写法：查看分配标签**
```bash
# 列出分配的所有标签
for dist in $(aws cloudfront list-distributions --query 'DistributionList.Items[].Id' --output text); do
  echo "Distribution: $dist"
  aws cloudfront list-tags-for-resource \
    --resource arn:aws:cloudfront::123456789012:distribution/$dist
done
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
| AWS CloudFront CDN 命令 | 055-AWSCloudFront | 本文自身 |
