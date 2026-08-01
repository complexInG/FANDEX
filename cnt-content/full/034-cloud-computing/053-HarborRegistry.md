---
order: 530
title: Harbor 私有镜像仓库命令
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: Harbor 私有镜像仓库命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 安装与部署

**基本写法：下载 Harbor 安装包**
`curl -fsSL https://github.com/goharbor/harbor/releases/download/v<版本>/harbor-offline-installer-v<版本>.tgz -o harbor.tgz`
```bash
# 下载 Harbor 2.11 离线安装包
curl -fsSL https://github.com/goharbor/harbor/releases/download/v2.11.0/harbor-offline-installer-v2.11.0.tgz -o harbor.tgz
```

---

**基本写法：解压安装包**
`tar xzf harbor.tgz`
```bash
# 解压到当前目录
tar xzf harbor.tgz
```

---

**基本写法：复制配置模板**
`cp harbor.yml.tmpl harbor.yml`
```bash
# 复制默认配置模板
cd harbor
cp harbor.yml.tmpl harbor.yml
```

---

**基本写法：执行安装**
`sudo install.sh`
```bash
# 运行安装脚本
sudo ./install.sh
```

---

**基本写法：启用 Notary 验证**
`sudo install.sh --with-notary`
```bash
# 安装并启用镜像签名功能
sudo ./install.sh --with-notary
```

---

## 配置文件

**基本写法：HTTP 配置**
```yaml
# harbor.yml HTTP 配置
hostname: harbor.example.com
http:
  port: 80
harbor_admin_password: Harbor12345
database:
  password: root123
  max_idle_conns: 50
data_volume: /data/harbor
```

---

**基本写法：HTTPS 配置**
```yaml
# harbor.yml HTTPS 配置
hostname: harbor.example.com
http:
  port: 80
https:
  port: 443
  certificate: /data/cert/harbor.crt
  private_key: /data/cert/harbor.key
harbor_admin_password: Harbor12345
```

---

**基本写法：外部数据库配置**
```yaml
# 使用外部 PostgreSQL
external_database:
  harbor:
    host: pg.example.com
    port: 5432
    username: harbor
    password: HarborDb123
    db_name: harbor_db
    max_idle_conns: 50
```

---

**基本写法：外部 Redis 配置**
```yaml
# 使用外部 Redis
external_redis:
  host: redis.example.com
  port: 6379
  password: RedisPass123
  registry_db_index: 1
  jobservice_db_index: 2
```

---

**基本写法：邮件配置**
```yaml
# 邮件服务器配置
email_server:
  host: smtp.example.com
  port: 587
  username: sender@example.com
  password: MailPass123
  from: sender@example.com
  ssl: false
  insecure: false
```

---

## Docker 客户端登录

**基本写法：登录 Harbor**
`docker login <Harbor 地址>`
```bash
# 登录 Harbor 仓库
docker login harbor.example.com
```

---

**基本写法：使用用户名密码登录**
`docker login -u <用户名> -p <密码> <Harbor 地址>`
```bash
# 非交互式登录(避免在 CI 暴露密码用 stdin)
echo "MyPassword123" | docker login harbor.example.com -u admin --password-stdin
```

---

**基本写法：配置非安全仓库**
```json
// /etc/docker/daemon.json
{
  "insecure-registries": ["harbor.example.com:80"]
}
```

---

**基本写法：重启 Docker**
`sudo systemctl restart docker`
```bash
# 修改 daemon.json 后重启 Docker
sudo systemctl restart docker
```

---

**基本写法：退出登录**
`docker logout <Harbor 地址>`
```bash
# 移除本地凭证
docker logout harbor.example.com
```

---

## 镜像推送

**基本写法：构建镜像**
`docker build -t <镜像名>:<标签> .`
```bash
# 构建带 Harbor 地址标签的镜像
docker build -t harbor.example.com/myproject/app:v1.0 .
```

---

**基本写法：为镜像打标签**
`docker tag <源镜像> <Harbor 地址>/<项目>/<镜像>:<标签>`
```bash
# 为本地镜像打 Harbor 仓库标签
docker tag myapp:latest harbor.example.com/myproject/app:v1.0
```

---

**基本写法：推送镜像**
`docker push <Harbor 地址>/<项目>/<镜像>:<标签>`
```bash
# 推送镜像到 Harbor
docker push harbor.example.com/myproject/app:v1.0
```

---

**基本写法：推送多架构镜像**
```bash
# 创建并推送多架构 manifest
docker buildx build --platform linux/amd64,linux/arm64 \
  -t harbor.example.com/myproject/app:v1.0 \
  --push .
```

---

**基本写法：拉取镜像**
`docker pull <Harbor 地址>/<项目>/<镜像>:<标签>`
```bash
# 从 Harbor 拉取镜像
docker pull harbor.example.com/myproject/app:v1.0
```

---

## 项目与用户管理

**基本写法：创建项目**
```bash
# 通过 API 创建项目
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/projects \
  -d '{
    "project_name": "myproject",
    "public": false,
    "storage_limit": 53687091200
  }'
```

---

**基本写法：列出项目**
```bash
# 列出所有项目
curl -u admin:Harbor12345 \
  https://harbor.example.com/api/v2.0/projects
```

---

**基本写法：创建用户**
```bash
# 通过 API 创建用户
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/users \
  -d '{
    "username": "alice",
    "email": "alice@example.com",
    "realname": "Alice",
    "password": "AlicePass123!",
    "comment": "developer"
  }'
```

---

**基本写法：分配项目角色**
```bash
# 为用户分配项目开发者角色
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/projects/1/members \
  -d '{
    "role_id": 2,
    "member_user": {"username": "alice"}
  }'
```

---

**基本写法：删除项目**
```bash
# 删除指定项目(需先清空镜像)
curl -X DELETE -u admin:Harbor12345 \
  https://harbor.example.com/api/v2.0/projects/1
```

---

## 镜像管理 API

**基本写法：列出仓库**
```bash
# 列出项目下所有镜像仓库
curl -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories"
```

---

**基本写法：列出镜像标签**
```bash
# 列出指定镜像的所有标签
curl -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts"
```

---

**基本写法：删除镜像**
```bash
# 删除指定标签的镜像
curl -X DELETE -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts/v1.0"
```

---

**基本写法：扫描镜像**
```bash
# 触发镜像漏洞扫描
curl -X POST -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts/v1.0/scan"
```

---

**基本写法：查看扫描结果**
```bash
# 获取镜像扫描报告
curl -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts/v1.0/scan/report"
```

---

## 漏洞扫描

**基本写法：查看扫描器**
```bash
# 查看已配置的扫描器
curl -u admin:Harbor12345 \
  https://harbor.example.com/api/v2.0/scanners
```

---

**基本写法：设置默认扫描器**
```bash
# 将 Trivy 设为默认扫描器
curl -X PUT -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/scanners/Trivy \
  -d '{"is_default": true}'
```

---

**基本写法：配置扫描策略**
```yaml
# harbor.yml 启用漏洞扫描
scan:
  enabled: true
  trivy:
    ignore_unfixed: false
    skip_update: false
    offline_scan: false
```

---

**基本写法：查看 CVE 详情**
```bash
# 获取扫描出的漏洞详情
curl -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts/v1.0/scan/report" \
  | jq '.vulnerabilities[] | {id: .id, severity: .severity, package: .package}'
```

---

## 复制策略

**基本写法：创建远程仓库**
```bash
# 创建到远程 Harbor 的复制目标
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/registries \
  -d '{
    "name": "remote-harbor",
    "type": "harbor",
    "url": "https://harbor.remote.com",
    "credential": {
      "type": "basic",
      "access_key": "admin",
      "access_secret": "RemotePass123"
    }
  }'
```

---

**基本写法：创建复制策略**
```bash
# 创建推送模式复制策略
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/replication/policies \
  -d '{
    "name": "sync-to-remote",
    "src_registry": {"id": 1},
    "dest_registry": null,
    "trigger": {"type": "scheduled", "trigger_settings": {"cron": "0 0 * * * *"}},
    "filters": [{"type": "name", "value": "myproject/*"}]
  }'
```

---

**基本写法：手动触发复制**
```bash
# 手动启动一次复制
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/replication/executions \
  -d '{"policy_id": 1}'
```

---

**基本写法：查看复制状态**
```bash
# 查看复制执行历史
curl -u admin:Harbor12345 \
  https://harbor.example.com/api/v2.0/replication/executions
```

---

## 垃圾回收

**基本写法：查看 GC 配置**
`docker-compose -f /harbor/docker-compose.yml stop`
```bash
# 停止 Harbor 服务准备 GC
cd /harbor
docker-compose -f docker-compose.yml stop
```

---

**基本写法：执行 GC**
`docker run -it --name gc --rm --volumes-from registry-core vmware/harbor-registryctl:2.11.0 garbage-collect --dry-run /etc/registry/config.yml`
```bash
# 干运行查看 GC 影响
docker run -it --name gc --rm \
  --volumes-from registry-core \
  goharbor/registry-photon:v2.11.0 \
  garbage-collect --dry-run /etc/registry/config.yml
```

---

**基本写法：实际执行 GC**
`docker run -it --name gc --rm --volumes-from registry-core goharbor/registry-photon:v2.11.0 garbage-collect /etc/registry/config.yml`
```bash
# 实际执行垃圾回收(需停止 Harbor)
docker run -it --name gc --rm \
  --volumes-from registry-core \
  goharbor/registry-photon:v2.11.0 \
  garbage-collect /etc/registry/config.yml
```

---

**基本写法：定时 GC 任务**
```bash
# 通过 API 创建定时 GC 任务
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/system/gc/schedule \
  -d '{
    "schedule": {"type": "Weekly", "cron": "0 0 0 * * 0", "weekday": 0},
    "parameters": {"delete_untagged": true}
  }'
```

---

## 备份与升级

**基本写法：备份数据库**
`docker exec -it harbor-db pg_dump -U postgres registry > backup.sql`
```bash
# 备份 Harbor 数据库
docker exec -it harbor-db pg_dump -U postgres registry > harbor-$(date +%Y%m%d).sql
```

---

**基本写法：备份存储卷**
`tar czf harbor-data-<日期>.tgz /data/harbor`
```bash
# 备份整个 Harbor 数据卷
tar czf harbor-data-20260731.tgz /data/harbor
```

---

**基本写法：恢复数据库**
`docker exec -i harbor-db psql -U postgres registry < backup.sql`
```bash
# 从备份恢复数据库
docker exec -i harbor-db psql -U postgres registry < harbor-20260731.sql
```

---

**基本写法：升级 Harbor**
`sudo ./install.sh`
```bash
# 下载新版本后执行安装脚本升级
cd harbor
sudo ./install.sh
```

---

**基本写法：迁移配置文件**
`sudo ./migrate --input <旧配置> --output <新配置>`
```bash
# 升级时迁移 harbor.cfg 到 harbor.yml
sudo ./migrate --input harbor.cfg --output harbor.yml
```

---

## Helm 部署方式

**基本写法：添加 Harbor Helm 仓库**
`helm repo add harbor https://helm.goharbor.io`
```bash
# 添加 Harbor 官方 Helm 仓库
helm repo add harbor https://helm.goharbor.io
helm repo update
```

---

**基本写法：配置 values.yaml**
```yaml
# values.yaml 关键配置
expose:
  type: ingress
  tls:
    enabled: true
    certSource: secret
    secret:
      secretName: harbor-tls
      notarySecretName: notary-tls
externalURL: https://harbor.example.com
harborAdminPassword: "Harbor12345"
persistence:
  persistentVolumeClaim:
    registry:
      size: 100Gi
    database:
      size: 10Gi
```

---

**基本写法：通过 Helm 安装 Harbor**
`helm install harbor harbor/harbor -f values.yaml -n harbor --create-namespace`
```bash
# 在 harbor 命名空间安装 Harbor
helm install harbor harbor/harbor \
  -f values.yaml \
  -n harbor \
  --create-namespace
```

---

**基本写法：升级 Harbor**
`helm upgrade harbor harbor/harbor -f values.yaml -n harbor`
```bash
# 升级 Harbor 到新版本
helm repo update
helm upgrade harbor harbor/harbor \
  -f values.yaml \
  -n harbor
```

---

**基本写法：卸载 Harbor**
`helm uninstall harbor -n harbor`
```bash
# 卸载 Harbor(不删除 PVC)
helm uninstall harbor -n harbor
```

---

## 高级配置

**基本写法：配置 OIDC 登录**
```yaml
# harbor.yml 配置 OIDC
oidc:
  name: "Google"
  endpoint: "https://accounts.google.com"
  client_id: "your-client-id"
  client_secret: "your-client-secret"
  scope: "openid,profile,email"
  verify_cert: true
```

---

**基本写法：配置 LDAP**
```yaml
# harbor.yml 配置 LDAP 认证
ldap:
  url: ldaps://ldap.example.com
  base_dn: dc=example,dc=com
  filter: "(objectClass=person)"
  uid: uid
  scope: 2
  timeout: 5
```

---

**基本写法：配置 Webhook**
```bash
# 通过 API 创建 Webhook
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/projects/1/webhook/policies \
  -d '{
    "name": "image-push-notify",
    "enabled": true,
    "targets": [{"type": "http", "address": "https://app.example.com/webhook"}],
    "event_types": ["PUSH_ARTIFACT"],
    "creator": "admin"
  }'
```

---

**基本写法：配置配额**
```bash
# 设置项目存储配额
curl -X PUT -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/projects/1 \
  -d '{"metadata": {"storage_limit": "53687091200"}}'
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
| Harbor 私有镜像仓库命令 | 053-HarborRegistry | 本文自身 |
| cloud-init 云实例初始化 | 054-CloudInitCommands | 本文的并列主题 |
| AWS CloudFront CDN 命令 | 055-AWSCloudFront | 本文的并列主题 |
