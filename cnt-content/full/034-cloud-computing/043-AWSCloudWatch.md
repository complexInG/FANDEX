---
order: 430
title: AWS CloudWatch 监控日志命令
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: AWS CloudWatch 监控日志命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# AWS CloudWatch 监控日志命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 命名空间与指标查看

**基本写法：列出所有命名空间**
`aws cloudwatch list-namespaces`
```bash
# 查看账户下所有 CloudWatch 命名空间
aws cloudwatch list-namespaces
```

---

**基本写法：列出指定命名空间下的指标**
`aws cloudwatch list-metrics --namespace <命名空间>`
```bash
# 列出 AWS/EC2 命名空间下所有指标
aws cloudwatch list-metrics --namespace AWS/EC2
```

---

**基本写法：按指标名与维度过滤**
`aws cloudwatch list-metrics --namespace <命名空间> --metric-name <指标名> --dimensions <维度>`
```bash
# 查看 EC2 CPUUtilization 指标
aws cloudwatch list-metrics --namespace AWS/EC2 --metric-name CPUUtilization
```

---

**基本写法：分页查询指标**
`aws cloudwatch list-metrics --namespace <命名空间> --next-token <令牌>`
```bash
# 使用上一次返回的 token 继续分页查询
aws cloudwatch list-metrics --namespace AWS/EC2 --next-token EXAMPLE_TOKEN
```

---

## 指标数据获取

**基本写法：获取指标统计数据**
`aws cloudwatch get-metric-statistics --namespace <命名空间> --metric-name <指标名> --start-time <开始> --end-time <结束> --period <秒> --statistics <统计>`
```bash
# 获取过去 1 小时 EC2 平均 CPU 利用率
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --statistics Average
```

---

**基本写法：多统计方式查询**
`aws cloudwatch get-metric-statistics --statistics Average Maximum Minimum Sum`
```bash
# 同时查询平均值、最大值、最小值、求和
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --statistics Average Maximum Minimum Sum
```

---

**基本写法：使用扩展统计百分位**
`aws cloudwatch get-metric-statistics --extended-statistics <百分位>`
```bash
# 查询 P95 P99 百分位数据
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --extended-statistics p95 p99
```

---

## 日志组与日志流

**基本写法：列出日志组**
`aws logs describe-log-groups [--log-group-name-prefix <前缀>]`
```bash
# 列出以 /aws/lambda 开头的日志组
aws logs describe-log-groups --log-group-name-prefix /aws/lambda
```

---

**基本写法：创建日志组**
`aws logs create-log-group --log-group-name <日志组名>`
```bash
# 创建自定义日志组并设置保留
aws logs create-log-group --log-group-name /myapp/prod
```

---

**基本写法：设置日志保留**
`aws logs put-retention-policy --log-group-name <日志组名> --retention-in-days <天数>`
```bash
# 设置日志保留 30 天
aws logs put-retention-policy --log-group-name /myapp/prod --retention-in-days 30
```

---

**基本写法：列出日志流**
`aws logs describe-log-streams --log-group-name <日志组名>`
```bash
# 查看指定日志组下日志流
aws logs describe-log-streams --log-group-name /aws/lambda/myFunction
```

---

**基本写法：删除日志组**
`aws logs delete-log-group --log-group-name <日志组名>`
```bash
# 删除日志组及其所有日志流
aws logs delete-log-group --log-group-name /myapp/dev
```

---

## 日志查询

**基本写法：获取日志事件**
`aws logs get-log-events --log-group-name <日志组名> --log-stream-name <日志流名>`
```bash
# 获取最新 50 条日志事件
aws logs get-log-events \
  --log-group-name /aws/lambda/myFunction \
  --log-stream-name '2026/07/31/[$LATEST]abc123' \
  --limit 50
```

---

**基本写法：过滤日志事件**
`aws logs filter-log-events --log-group-name <日志组名> --filter-pattern <过滤模式>`
```bash
# 查询包含 ERROR 的日志
aws logs filter-log-events \
  --log-group-name /myapp/prod \
  --filter-pattern ERROR \
  --start-time 1785489000000
```

---

**基本写法：使用 JSON 过滤语法**
`aws logs filter-log-events --filter-pattern <JSON模式>`
```bash
# 过滤 level 为 ERROR 且 message 包含 timeout 的日志
aws logs filter-log-events \
  --log-group-name /myapp/prod \
  --filter-pattern '{ $.level = "ERROR" && $.message = "timeout" }'
```

---

**基本写法：跨多日志组查询**
`aws logs filter-log-events --log-group-names <日志组1> <日志组2>`
```bash
# 同时在多个日志组中查询
aws logs filter-log-events \
  --log-group-names /myapp/api /myapp/worker \
  --filter-pattern ERROR
```

---

## Logs Insights 查询

**基本写法：启动 Logs Insights 查询**
`aws logs start-query --log-group-names <日志组> --start-time <开始> --end-time <结束> --query-string <查询>`
```bash
# 启动查询统计错误日志
aws logs start-query \
  --log-group-names /myapp/prod \
  --start-time 1785489000 \
  --end-time 1785492600 \
  --query-string 'fields @timestamp, @message | filter level = "ERROR" | sort @timestamp desc | limit 100'
```

---

**基本写法：获取查询结果**
`aws logs get-query-results --query-id <查询ID>`
```bash
# 通过查询 ID 获取结果
aws logs get-query-results --query-id EXAMPLE-QUERY-ID
```

---

**基本写法：停止查询**
`aws logs stop-query --query-id <查询ID>`
```bash
# 终止运行中的查询
aws logs stop-query --query-id EXAMPLE-QUERY-ID
```

---

**基本写法：聚合统计查询**
`aws logs start-query --query-string <统计查询>`
```bash
# 按错误类型聚合统计
aws logs start-query \
  --log-group-names /myapp/prod \
  --start-time 1785489000 \
  --end-time 1785492600 \
  --query-string 'filter level = "ERROR" | stats count(*) by errorType | sort count(*) desc'
```

---

## 告警管理

**基本写法：创建基于指标的告警**
`aws cloudwatch put-metric-alarm --alarm-name <告警名> --metric-name <指标> --namespace <命名空间> --threshold <阈值> --comparison-operator <操作符> --evaluation-periods <周期数> --period <秒>`
```bash
# 创建 CPU 利用率超 80% 触发的告警
aws cloudwatch put-metric-alarm \
  --alarm-name HighCPU \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0
```

---

**基本写法：告警附加 SNS 通知**
`aws cloudwatch put-metric-alarm --alarm-actions <SNS ARN>`
```bash
# 告警触发时发送 SNS 通知
aws cloudwatch put-metric-alarm \
  --alarm-name HighCPU \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:my-topic
```

---

**基本写法：列出所有告警**
`aws cloudwatch describe-alarms [--state-value <状态>]`
```bash
# 仅列出处于告警状态的告警
aws cloudwatch describe-alarms --state-value ALARM
```

---

**基本写法：删除告警**
`aws cloudwatch delete-alarms --alarm-names <告警名>`
```bash
# 删除指定告警
aws cloudwatch delete-alarms --alarm-names HighCPU
```

---

## 仪表盘与注解

**基本写法：获取仪表盘**
`aws cloudwatch get-dashboard --dashboard-name <仪表盘名>`
```bash
# 获取仪表盘定义 JSON
aws cloudwatch get-dashboard --dashboard-name my-dashboard
```

---

**基本写法：创建或更新仪表盘**
`aws cloudwatch put-dashboard --dashboard-name <仪表盘名> --dashboard-body <JSON>`
```bash
# 通过 JSON 创建仪表盘
aws cloudwatch put-dashboard \
  --dashboard-name my-dashboard \
  --dashboard-body '{"widgets":[{"type":"metric","x":0,"y":0,"width":12,"height":6,"properties":{"metrics":[["AWS/EC2","CPUUtilization"]],"region":"us-east-1","title":"CPU 使用率"}}]}'
```

---

**基本写法：列出所有仪表盘**
`aws cloudwatch list-dashboards`
```bash
# 列出账户所有仪表盘
aws cloudwatch list-dashboards
```

---

**基本写法：删除仪表盘**
`aws cloudwatch delete-dashboards --dashboard-names <仪表盘名>`
```bash
# 删除指定仪表盘
aws cloudwatch delete-dashboards --dashboard-names my-dashboard
```

---

## 指标流与异常检测

**基本写法：创建指标流**
`aws cloudwatch put-metric-stream --name <流名> --firehose-arn <Firehose ARN> --output-format <格式>`
```bash
# 创建指标流到 Kinesis Firehose
aws cloudwatch put-metric-stream \
  --name my-stream \
  --firehose-arn arn:aws:firehose:us-east-1:123456789012:deliverystream/my-stream \
  --output-format opentelemetry0.7 \
  --role-arn arn:aws:iam::123456789012:role/my-stream-role
```

---

**基本写法：创建异常检测模型**
`aws cloudwatch put-anomaly-detector --namespace <命名空间> --metric-name <指标名>`
```bash
# 为 EC2 CPU 指标创建异常检测
aws cloudwatch put-anomaly-detector \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --stat Average
```

---

**基本写法：列出异常检测器**
`aws cloudwatch describe-anomaly-detectors`
```bash
# 查看所有异常检测模型
aws cloudwatch describe-anomaly-detectors
```

---

**基本写法：删除异常检测器**
`aws cloudwatch delete-anomaly-detectors --namespace <命名空间> --metric-name <指标名>`
```bash
# 删除指定异常检测模型
aws cloudwatch delete-anomaly-detectors \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization
```

---

## Contributor Insights 与 RUM

**基本写法：创建 Contributor Insights 规则**
`aws logs put-insight-rule --insight-rule <JSON>`
```bash
# 创建按 IP 统计访问的规则
aws logs put-insight-rule \
  --insight-rule '{
    "name": "TopIPs",
    "logFormat": "JSON",
    "logGroupNames": ["/myapp/prod"],
    "fields": ["clientIp"],
    "contribution": {"keys": ["clientIp"], "value": "1"}
  }'
```

---

**基本写法：查询 Contributor Insights 结果**
`aws logs get-insight-query-results --insight-rule-name <规则名>`
```bash
# 获取 TopIPs 规则的查询结果
aws logs get-insight-query-results \
  --insight-rule-name TopIPs \
  --start-time 1785489000000 \
  --end-time 1785492600000
```

---

**基本写法：启用 RUM 应用监控**
`aws rum create-app-monitor --name <应用名> --domain <域名> --app-configuration <JSON>`
```bash
# 创建 RUM 应用监控
aws rum create-app-monitor \
  --name my-app \
  --domain example.com \
  --app-configuration '{"AllowCookies":true,"EnableXRay":true}'
```

---

**基本写法：查看 RUM 应用监控列表**
`aws rum list-app-monitors`
```bash
# 列出所有 RUM 应用监控
aws rum list-app-monitors
```

---

## 合成监控与自定义指标

**基本写法：创建 Canary 合成监控**
`aws synthetics create-canary --name <名称> --code <代码配置> --schedule <调度> --artifact-s3-location <S3>`
```bash
# 创建每 5 分钟运行的 Canary
aws synthetics create-canary \
  --name my-canary \
  --code Handler= CanaryHandler.handler,ZipFile= canary.zip \
  --schedule 'Expression="rate(5 minutes)"' \
  --artifact-s3-location s3://my-bucket/canary \
  --execution-role-arn arn:aws:iam::123456789012:role/CanaryRole \
  --runtime-version syn-1.0
```

---

**基本写法：启动 Canary**
`aws synthetics start-canary --name <名称>`
```bash
# 启动指定 Canary
aws synthetics start-canary --name my-canary
```

---

**基本写法：发布自定义指标**
`aws cloudwatch put-metric-data --namespace <命名空间> --metric-data <指标数据>`
```bash
# 推送自定义业务指标
aws cloudwatch put-metric-data \
  --namespace MyApplication \
  --metric-data '[{"MetricName":"OrderCount","Dimensions":[{"Name":"Service","Value":"Checkout"}],"Value":42,"Unit":"Count"}]'
```

---

**基本写法：发布带时间戳的指标**
`aws cloudwatch put-metric-data --metric-data <带时间戳>`
```bash
# 推送带时间戳的历史数据
aws cloudwatch put-metric-data \
  --namespace MyApplication \
  --metric-data '[{"MetricName":"Latency","Timestamp":"2026-07-31T00:00:00Z","Value":250,"Unit":"Milliseconds"}]'
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
| AWS CloudWatch 监控日志命令 | 043-AWSCloudWatch | 本文自身 |
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
