---
order: 106
title: Grafana仪表盘配置
module: devops
category: 'eng-infra'
difficulty: intermediate
description: 'Grafana 仪表盘配置：数据源、面板类型、变量模板与告警集成。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'devops/Ansible-Playbook配置管理'
  - devops/Prometheus指标采集与告警
  - 'devops/ELK-Stack日志分析'
  - devops/OpenTelemetry可观测性
prerequisites:
  - devops/概述与Linux基础
---

# Grafana 可视化与仪表盘速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 数据源配置

### 1.1 Prometheus

Prometheus是Grafana仪表盘配置的重要组成部分。本节详细介绍Prometheus的核心概念、工作原理和实际应用。

**关键要点**：

- Prometheus的定义与核心原理
- Prometheus的实现方式与技术细节
- Prometheus在实际场景中的应用与最佳实践
- Prometheus的常见问题与解决方案

Prometheus在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Loki

Loki是Grafana仪表盘配置的重要组成部分。本节详细介绍Loki的核心概念、工作原理和实际应用。

**关键要点**：

- Loki的定义与核心原理
- Loki的实现方式与技术细节
- Loki在实际场景中的应用与最佳实践
- Loki的常见问题与解决方案

Loki在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 Elasticsearch

Elasticsearch是Grafana仪表盘配置的重要组成部分。本节详细介绍Elasticsearch的核心概念、工作原理和实际应用。

**关键要点**：

- Elasticsearch的定义与核心原理
- Elasticsearch的实现方式与技术细节
- Elasticsearch在实际场景中的应用与最佳实践
- Elasticsearch的常见问题与解决方案

Elasticsearch在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 面板类型

### 2.1 时间序列图

时间序列图是Grafana仪表盘配置的重要组成部分。本节详细介绍时间序列图的核心概念、工作原理和实际应用。

**关键要点**：

- 时间序列图的定义与核心原理
- 时间序列图的实现方式与技术细节
- 时间序列图在实际场景中的应用与最佳实践
- 时间序列图的常见问题与解决方案

时间序列图在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 仪表盘

仪表盘是Grafana仪表盘配置的重要组成部分。本节详细介绍仪表盘的核心概念、工作原理和实际应用。

**关键要点**：

- 仪表盘的定义与核心原理
- 仪表盘的实现方式与技术细节
- 仪表盘在实际场景中的应用与最佳实践
- 仪表盘的常见问题与解决方案

仪表盘在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 热力图

热力图是Grafana仪表盘配置的重要组成部分。本节详细介绍热力图的核心概念、工作原理和实际应用。

**关键要点**：

- 热力图的定义与核心原理
- 热力图的实现方式与技术细节
- 热力图在实际场景中的应用与最佳实践
- 热力图的常见问题与解决方案

热力图在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.4 表格

表格是Grafana仪表盘配置的重要组成部分。本节详细介绍表格的核心概念、工作原理和实际应用。

**关键要点**：

- 表格的定义与核心原理
- 表格的实现方式与技术细节
- 表格在实际场景中的应用与最佳实践
- 表格的常见问题与解决方案

表格在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 变量与模板

### 3.1 查询变量

查询变量是Grafana仪表盘配置的重要组成部分。本节详细介绍查询变量的核心概念、工作原理和实际应用。

**关键要点**：

- 查询变量的定义与核心原理
- 查询变量的实现方式与技术细节
- 查询变量在实际场景中的应用与最佳实践
- 查询变量的常见问题与解决方案

查询变量在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 间隔变量

间隔变量是Grafana仪表盘配置的重要组成部分。本节详细介绍间隔变量的核心概念、工作原理和实际应用。

**关键要点**：

- 间隔变量的定义与核心原理
- 间隔变量的实现方式与技术细节
- 间隔变量在实际场景中的应用与最佳实践
- 间隔变量的常见问题与解决方案

间隔变量在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 链接面板

链接面板是Grafana仪表盘配置的重要组成部分。本节详细介绍链接面板的核心概念、工作原理和实际应用。

**关键要点**：

- 链接面板的定义与核心原理
- 链接面板的实现方式与技术细节
- 链接面板在实际场景中的应用与最佳实践
- 链接面板的常见问题与解决方案

链接面板在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 告警集成

### 4.1 Grafana 告警规则

Grafana 告警规则是Grafana仪表盘配置的重要组成部分。本节详细介绍Grafana 告警规则的核心概念、工作原理和实际应用。

**关键要点**：

- Grafana 告警规则的定义与核心原理
- Grafana 告警规则的实现方式与技术细节
- Grafana 告警规则在实际场景中的应用与最佳实践
- Grafana 告警规则的常见问题与解决方案

Grafana 告警规则在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 通知渠道

通知渠道是Grafana仪表盘配置的重要组成部分。本节详细介绍通知渠道的核心概念、工作原理和实际应用。

**关键要点**：

- 通知渠道的定义与核心原理
- 通知渠道的实现方式与技术细节
- 通知渠道在实际场景中的应用与最佳实践
- 通知渠道的常见问题与解决方案

通知渠道在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## 服务管理

**基本用法:启动 Grafana**
`grafana-server --config=<配置文件>`

```bash
# Linux 启动
systemctl start grafana-server
systemctl enable grafana-server

# 直接运行二进制
grafana-server --config=/etc/grafana/grafana.ini --homepath=/usr/share/grafana

# Docker 启动
docker run -d --name=grafana -p 3000:3000 grafana/grafana:latest

# Docker Compose 启动(带持久化)
docker run -d --name=grafana -p 3000:3000 \
  -v grafana-storage:/var/lib/grafana \
  -v /etc/grafana/provisioning:/etc/grafana/provisioning \
  grafana/grafana:latest
```

---

**基本用法:查看 Grafana 状态**
`systemctl status grafana-server`

```bash
# 查看服务状态
systemctl status grafana-server

# 查看日志
journalctl -u grafana-server -f --tail=50

# 查看容器日志
docker logs -f grafana --tail=50

# 查看版本
grafana-server -v
docker exec grafana grafana-cli --version
```

---

## grafana-cli 命令

**基本用法:安装插件**
`grafana-cli plugins install <插件名>`

```bash
# 安装饼图插件
grafana-cli plugins install grafana-piechart-panel

# 安装时钟插件
grafana-cli plugins install grafana-clock-panel

# 安装点击house 数据源
grafana-cli plugins install vertamedia-clickhouse-datasource

# 重启 Grafana 使插件生效
systemctl restart grafana-server
```

---

**基本用法:管理插件**
`grafana-cli plugins <list|install|remove>`

```bash
# 列出已安装插件
grafana-cli plugins ls

# 升级指定插件
grafana-cli plugins upgrade grafana-piechart-panel

# 卸载插件
grafana-cli plugins remove grafana-piechart-panel

# 安装指定版本
grafana-cli plugins install grafana-piechart-panel 1.5.0
```

---

**基本用法:重置管理员密码**
`grafana-cli admin reset-admin-password <新密码>`

```bash
# 重置 admin 密码
grafana-cli admin reset-admin-password newpassword

# Docker 环境重置密码
docker exec -it grafana grafana-cli admin reset-admin-password newpassword

# 查看用户列表(SQLite)
sqlite3 /var/lib/grafana/grafana.db "SELECT login,email FROM user;"
```

---

## API 操作

**基本用法:认证与获取 API Key**
`curl -u <用户>:<密码> <服务器>/api/...`

```bash
# 基本认证访问 API
curl -u admin:admin http://localhost:3000/api/health

# 创建 API Token
curl -X POST -H "Content-Type: application/json" -u admin:admin \
  http://localhost:3000/api/auth/keys \
  -d '{"name":"ci-key","role":"Admin","secondsToLive":86400}'

# 使用 Token 访问
curl -H "Authorization: Bearer <token>" http://localhost:3000/api/org
```

---

**基本用法:管理数据源**
`curl <服务器>/api/datasources`

```bash
# 列出所有数据源
curl -H "Authorization: Bearer <token>" http://localhost:3000/api/datasources

# 创建 Prometheus 数据源
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/datasources \
  -d '{
    "name": "Prometheus",
    "type": "prometheus",
    "url": "http://prometheus:9090",
    "access": "proxy",
    "isDefault": true
  }'

# 测试数据源连接
curl -X POST -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/datasources/name/Prometheus/health
```

---

**基本用法:管理仪表盘**
`curl <服务器>/api/dashboards`

```bash
# 查找仪表盘
curl -H "Authorization: Bearer <token>" \
  "http://localhost:3000/api/search?query=node"

# 导出仪表盘 JSON
curl -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/dashboards/uid/node-overview > dashboard.json

# 导入仪表盘
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/dashboards/db \
  -d @dashboard.json
```

---

## 仪表盘配置

**基本用法:仪表盘 JSON 结构**
`{ "dashboard": {...}, "folderId": 0, "overwrite": false }`

```json
{
  "dashboard": {
    "id": null,
    "uid": "node-overview",
    "title": "节点概览",
    "tags": ["node", "linux"],
    "timezone": "browser",
    "schemaVersion": 39,
    "refresh": "30s",
    "time": {
      "from": "now-6h",
      "to": "now"
    },
    "panels": [
      {
        "id": 1,
        "title": "CPU 使用率",
        "type": "stat",
        "datasource": "Prometheus",
        "targets": [
          {
            "expr": "100 - avg(rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100",
            "legendFormat": "{{instance}}"
          }
        ],
        "gridPos": {"h": 8, "w": 6, "x": 0, "y": 0}
      }
    ]
  },
  "folderId": 0,
  "overwrite": true
}
```

---

**基本用法:变量配置**
`templating.list`

```json
{
  "templating": {
    "list": [
      {
        "name": "datasource",
        "type": "datasource",
        "query": "prometheus",
        "current": {"text": "Prometheus", "value": "Prometheus"}
      },
      {
        "name": "instance",
        "type": "query",
        "datasource": "$datasource",
        "query": "label_values(node_cpu_seconds_total, instance)",
        "refresh": 1,
        "includeAll": true,
        "multi": true
      },
      {
        "name": "interval",
        "type": "interval",
        "options": [
          {"text": "1m", "value": "1m"},
          {"text": "5m", "value": "5m"},
          {"text": "1h", "value": "1h"}
        ],
        "current": {"text": "5m", "value": "5m"}
      }
    ]
  }
}
```

---

**基本用法:面板类型选择**
`type: <类型>`

```json
// 时间序列图
{"type": "timeseries", "title": "CPU 趋势"}

// 仪表盘
{"type": "gauge", "title": "内存使用率"}

// 统计数字
{"type": "stat", "title": "实例总数"}

// 表格
{"type": "table", "title": "节点列表"}

// 热力图
{"type": "heatmap", "title": "请求延迟分布"}

// 日志视图
{"type": "logs", "title": "应用日志"}
```

---

## Provisioning 自动配置

**基本用法:数据源自动配置**
`provisioning/datasources/datasource.yaml`

```yaml
# provisioning/datasources/datasource.yaml
apiVersion: 1

datasources:
- name: Prometheus
  type: prometheus
  access: proxy
  url: http://prometheus:9090
  isDefault: true
  editable: true

- name: Loki
  type: loki
  access: proxy
  url: http://loki:3100

- name: MySQL
  type: mysql
  url: mysql:3306
  user: readonly
  secureJsonData:
    password: ${MYSQL_PASSWORD}
  jsonData:
    database: metrics
```

---

**基本用法:仪表盘自动配置**
`provisioning/dashboards/dashboard.yaml`

```yaml
# provisioning/dashboards/dashboard.yaml
apiVersion: 1

providers:
- name: 'default'
  orgId: 1
  folder: 'Auto Provisioned'
  folderUid: auto-folder
  type: file
  disableDeletion: false
  updateIntervalSeconds: 30
  allowUiUpdates: true
  options:
    path: /var/lib/grafana/dashboards
    foldersFromFilesStructure: true
```

---

**基本用法:告警规则自动配置**
`provisioning/alerting/rules.yaml`

```yaml
# provisioning/alerting/rules.yaml
apiVersion: 1
groups:
- name: node-alerts
  interval: 30s
  rules:
  - uid: high-cpu
    title: High CPU Usage
    condition: A
    data:
    - refId: A
      relativeTimeRange:
        from: 600
        to: 0
      datasourceUid: prometheus-uid
      model:
        expr: "100 - avg(rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100 > 80"
        instant: true
    noDataState: NoData
    execErrState: Error
    for: 5m
    annotations:
      summary: "CPU 使用率过高"
    labels:
      severity: warning
```

---

## 告警管理

**基本用法:配置通知渠道**
`provisioning/alerting/contactpoints.yaml`

```yaml
# provisioning/alerting/contactpoints.yaml
apiVersion: 1
contactPoints:
- name: slack-notification
  uid: slack-cp
  type: slack
  settings:
    url: https://hooks.slack.com/services/xxx
    channel: "#alerts"
  disableResolveMessage: false

- name: email-notification
  uid: email-cp
  type: email
  settings:
    addresses: ops@example.com
```

---

**基本用法:通知策略**
`provisioning/alerting/notificationpolicies.yaml`

```yaml
# provisioning/alerting/notificationpolicies.yaml
apiVersion: 1
policies:
- orgId: 1
  receiver: default
  group_by: ['alertname']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  routes:
  - receiver: slack-notification
    matchers:
    - severity="critical"
    group_wait: 10s
  - receiver: email-notification
    matchers:
    - severity="warning"
    mute_time_intervals:
    - offhours
```

---

## 用户与组织管理

**基本用法:管理用户**
`curl -X POST <服务器>/api/admin/users`

```bash
# 创建用户
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/admin/users \
  -d '{"name":"Alice","email":"alice@example.com","login":"alice","password":"pass123"}'

# 修改用户角色
curl -X PATCH -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/org/users/2 \
  -d '{"role":"Editor"}'

# 列出组织成员
curl -H "Authorization: Bearer <token>" http://localhost:3000/api/org/users
```

---

**基本用法:管理组织**
`curl <服务器>/api/orgs`

```bash
# 创建组织
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/orgs \
  -d '{"name":"Engineering"}'

# 切换当前组织
curl -X POST -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/user/using/2

# 列出所有组织
curl -H "Authorization: Bearer <token>" http://localhost:3000/api/orgs
```

---

## 备份与迁移

**基本用法:导出仪表盘**
`curl <服务器>/api/dashboards/uid/<uid>`

```bash
# 导出单个仪表盘
curl -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/dashboards/uid/node-overview > node-overview.json

# 批量导出所有仪表盘
for uid in $(curl -s -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/search?type=dash-db | jq -r '.[].uid'); do
  curl -s -H "Authorization: Bearer <token>" \
    http://localhost:3000/api/dashboards/uid/$uid > "dashboard-${uid}.json"
done
```

---

**基本用法:备份 SQLite 数据库**
`sqlite3 <数据库文件> .backup <备份文件>`

```bash
# 在线备份 SQLite 数据库
sqlite3 /var/lib/grafana/grafana.db ".backup /backup/grafana-$(date +%Y%m%d).db"

# 备份配置与数据卷
docker run --rm -v grafana-storage:/data -v $(pwd):/backup alpine \
  tar czf /backup/grafana-$(date +%Y%m%d).tar.gz /data

# 恢复备份
docker run --rm -v grafana-storage:/data -v $(pwd):/backup alpine \
  tar xzf /backup/grafana-backup.tar.gz -C /
```

---

## 性能与排查

**基本用法:查看 Grafana 健康状态**
`curl <服务器>/api/health`

```bash
# 健康检查
curl http://localhost:3000/api/health

# 查看指标
curl http://localhost:3000/metrics | grep grafana_

# 查看统计信息
curl -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/admin/stats
```

---

**基本用法:配置日志级别**
`log.level = <级别>`

```ini
# grafana.ini 日志配置
[log]
mode = console file
level = info
filters = alerting.notifier:debug

[log.file]
level = info
max_lines = 1000000
max_size_shift = 28
daily_rotate = true
max_days = 7
```

```bash
# 运行时动态修改日志级别
curl -X PUT -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/admin/settings \
  -d '{"log.level":"debug"}'
```

---

**基本用法:查询性能优化**
`Query inspector`

```bash
# 通过 API 检查查询性能
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/ds/query \
  -d '{
    "queries": [{
      "refId": "A",
      "datasource": {"uid": "prometheus"},
      "expr": "rate(http_requests_total[5m])",
      "instant": false,
      "range": true
    }],
    "from": "now-1h",
    "to": "now"
  }'

# 查看慢查询日志
journalctl -u grafana-server | grep "slow query"
```

---

## 集成与导出

**基本用法:导出为图片或 PDF**
`curl <服务器>/render/d/<dashboard-uid>`

```bash
# 渲染仪表盘为图片(需安装 image renderer 插件)
curl "http://localhost:3000/render/d/node-overview?from=now-6h&to=now&width=1000&height=500" \
  -H "Authorization: Bearer <token>" -o dashboard.png

# 渲染特定面板
curl "http://localhost:3000/render/d-solo/node-overview/panel-1?from=now-6h&to=now&width=1000&height=500" \
  -H "Authorization: Bearer <token>" -o panel.png

# 通过共享快照 API
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/snapshots \
  -d @dashboard.json
```

---

**基本用法:嵌入外部网页**
`<iframe src="<grafana-url>/d/<uid>">`

```html
<!-- 启用嵌入模式需要在 grafana.ini 中配置 -->
<!-- [security] allow_embedding = true -->

<iframe
  src="http://grafana:3000/d/node-overview?from=now-6h&to=now&kiosk=tv"
  width="100%"
  height="600"
  frameborder="0">
</iframe>

<!-- 通过 URL 参数控制显示 -->
<!-- kiosk=tv: 电视模式(隐藏顶部栏) -->
<!-- kiosk=1: 全屏模式(隐藏所有控件) -->
<!-- theme=light: 浅色主题 -->
```

## 参考文献



GitHub Actions 文档：https://docs.github.com/zh/actions
GitLab CI 文档：https://docs.gitlab.com/ci/
Argo CD：https://argo-cd.readthedocs.io/
DORA 研究：https://dora.dev/
DevOps 手册（Gene Kim 等）：https://itrevolution.com/devops-handbook/

## 延伸阅读



Docker 与 Kubernetes 深入，见 031-devops 模块文档。
CI/CD 管线设计，见 031-devops 模块 CICD 文档。
云原生架构，见 034-cloud-computing 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 DevOps 课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与 Linux 基础 | 001-OverviewLinuxBasics | 本文的前置基础 |
| 网络与安全 | 002-NetworkSecurity | 本文的安全延伸 |
| 容器与 Docker | 003-ContainerDocker | 本文的并列主题 |
| Kubernetes | 004-Kubernetes | 本文的并列主题 |
| CI/CD 流水线 | 005-CICDPipeline | 本文的并列主题 |
| 监控与可观测性 | 006-MonitorAndObservability | 本文的并列主题 |
| 基础设施即代码 | 007-IaC | 本文的前置基础 |
| 云原生与 SRE | 008-CloudNativeSRE | 本文的并列主题 |
| Shell脚本编程 | 009-ShellScriptProgramming | 本文的并列主题 |
| 包管理与仓库 | 010-PackageManagementRepository | 本文的并列主题 |
| 服务网格 | 011-ServiceMesh | 本文的并列主题 |
| 日志管理 | 012-LogManagement | 本文的并列主题 |
| 配置管理 | 013-ConfigManagement | 本文的并列主题 |
| 性能调优 | 014-PerformanceTuning | 本文的性能延伸 |
| 高可用架构 | 015-HighAvailabilityArchitecture | 本文的原理深化 |
| 自动化测试 | 016-AutomationTest | 本文的并列主题 |
| 故障排查 | 017-Troubleshooting | 本文的并列主题 |
| 容器安全 | 018-ContainerSecurity | 本文的安全延伸 |
| GitOps与持续交付 | 019-GitOpsCD | 本文的并列主题 |
| 监控与告警 | 020-MonitorAndAlert | 本文的并列主题 |
| 网络与安全进阶 | 021-NetworkSecurityAdvanced | 本文的安全延伸 |
| 数据库运维 | 022-DatabaseOps | 本文的并列主题 |
| Dockerfile多阶段构建 | 023-DockerfileMultiBuild | 本文的并列主题 |
| Kubernetes核心资源详解 | 024-KubernetesCoreDetailed | 本文的并列主题 |
| Helm-Chart应用打包 | 025-HelmChartApplicationPackage | 本文的并列主题 |
| Terraform资源编排 | 026-Terraform | 本文的并列主题 |
| Ansible-Playbook配置管理 | 027-AnsiblePlaybookConfigManagement | 本文的并列主题 |
| Prometheus指标采集与告警 | 028-Prometheus | 本文的并列主题 |
| Grafana仪表盘配置 | 029-GrafanaTableConfig | 本文自身 |
| ELK-Stack日志分析 | 030-ELKStackLogAnalysis | 本文的并列主题 |
| OpenTelemetry | 031-OpenTelemetry | 本文的并列主题 |
| GitOps与ArgoCD | 032-GitOpsArgoCD | 本文的并列主题 |
| DevOps kubectl 基础命令 | 033-KubectlBasics | 本文的前置基础 |
| DevOps Helm 包管理命令 | 034-HelmCommands | 本文的并列主题 |
| DevOps Jenkins Pipeline | 035-JenkinsPipeline | 本文的并列主题 |
| DevOps GitLab CI/CD | 036-GitLabCI | 本文的并列主题 |
