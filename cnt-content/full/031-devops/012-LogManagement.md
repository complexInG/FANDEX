---
order: 53
title: 日志管理
module: devops
category: 运维
difficulty: intermediate
description: '日志管理：日志采集、ELK Stack、Fluentd、日志格式与日志分析'
author: fanquanpp
updated: '2026-08-01'
related:
  - devops/包管理与仓库
  - devops/服务网格
  - devops/配置管理
  - devops/性能调优
prerequisites:
  - devops/概述与Linux基础
---

## 1. 日志管理概述

### 1.1 日志级别

| 级别  | 说明                   | 示例               |
| ----- | ---------------------- | ------------------ |
| FATAL | 致命错误，系统无法继续 | 数据库连接失败     |
| ERROR | 错误，影响功能         | API 调用失败       |
| WARN  | 警告，潜在问题         | 磁盘空间不足       |
| INFO  | 重要信息               | 服务启动、请求完成 |
| DEBUG | 调试信息               | 变量值、执行路径   |
| TRACE | 详细跟踪               | 函数进出           |

### 1.2 日志最佳实践

- 使用结构化日志（JSON 格式）
- 包含请求 ID 用于追踪
- 避免记录敏感信息
- 设置合理的日志级别
- 日志轮转和归档

## 2. ELK Stack

### 2.1 架构

```
应用 → Filebeat → Logstash → Elasticsearch → Kibana
                      ↑
                 其他数据源
```

| 组件          | 功能         |
| ------------- | ------------ |
| Elasticsearch | 存储和搜索   |
| Logstash      | 数据处理管道 |
| Kibana        | 可视化界面   |
| Beats         | 轻量级采集器 |

### 2.2 Elasticsearch

**索引管理**：

```bash
# 创建索引
PUT /my-logs
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "timestamp": { "type": "date" },
      "level": { "type": "keyword" },
      "message": { "type": "text" },
      "service": { "type": "keyword" },
      "trace_id": { "type": "keyword" }
    }
  }
}

# 索引生命周期管理（ILM）
PUT _ilm/policy/logs-policy
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": { "max_age": "1d", "max_size": "50gb" }
        }
      },
      "warm": {
        "min_age": "7d",
        "actions": {
          "shrink": { "number_of_shards": 1 },
          "forcemerge": { "max_num_segments": 1 }
        }
      },
      "cold": {
        "min_age": "30d",
        "actions": { "freeze": {} }
      },
      "delete": {
        "min_age": "90d",
        "actions": { "delete": {} }
      }
    }
  }
}
```

### 2.3 Logstash

**管道配置**：

```ruby
input {
  beats {
    port => 5044
  }
  kafka {
    topics => ["app-logs"]
    group_id => "logstash"
  }
}

filter {
  grok {
    match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:msg}" }
  }
  json {
    source => "message"
    target => "parsed"
  }
  mutate {
    remove_field => ["message"]
    add_field => { "env" => "production" }
  }
  date {
    match => ["timestamp", "ISO8601"]
    target => "@timestamp"
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "logs-%{[service]}-%{+YYYY.MM.dd}"
  }
}
```

### 2.4 Kibana

**常用查询语法（KQL）**：

```
level: "ERROR" AND service: "api-gateway"
trace_id: "abc123"
@timestamp >= "2026-06-14" AND message: "timeout"
```

**可视化**：

- Discover：日志搜索和浏览
- Dashboard：仪表盘
- Lens：可视化构建器
- APM：应用性能监控

## 3. Fluentd / Fluent Bit

### 3.1 Fluentd

统一日志采集和处理：

```ruby
# fluent.conf
<source>
  @type tail
  path /var/log/app/*.log
  pos_file /var/log/fluent/app.log.pos
  tag app.logs
  <parse>
    @type json
  </parse>
</source>

<filter app.**>
  @type record_transformer
  <record>
    hostname "#{Socket.gethostname}"
    environment "production"
  </record>
</filter>

<match app.**>
  @type elasticsearch
  host elasticsearch
  port 9200
  logstash_format true
  logstash_prefix fluentd
  <buffer>
    @type file
    path /var/log/fluent/buffer
    flush_interval 5s
  </buffer>
</match>
```

### 3.2 Fluent Bit

轻量级日志处理器，适合边缘和容器环境：

```ini
[INPUT]
    Name              tail
    Path              /var/log/containers/*.log
    Parser            docker
    Tag               kube.*
    Mem_Buf_Limit     5MB
    Skip_Long_Lines   On

[FILTER]
    Name              kubernetes
    Match             kube.*
    Kube_URL          https://kubernetes.default.svc:443
    Kube_CA_File      /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    Kube_Token_File   /var/run/secrets/kubernetes.io/serviceaccount/token

[OUTPUT]
    Name              es
    Match             *
    Host              elasticsearch
    Port              9200
    Logstash_Format   On
    Replace_Dots      On
    Retry_Limit       False
```

### 3.3 Fluentd vs Fluent Bit

| 特性     | Fluentd  | Fluent Bit |
| -------- | -------- | ---------- |
| 语言     | Ruby + C | C          |
| 内存     | 较高     | 极低       |
| 功能     | 丰富     | 核心功能   |
| 适用场景 | 服务器   | 容器/边缘  |
| 插件     | 500+     | 100+       |

## 4. 结构化日志

### 4.1 JSON 日志格式

```json
{
  "timestamp": "2026-06-14T10:30:00.123Z",
  "level": "INFO",
  "service": "user-service",
  "trace_id": "abc123def456",
  "span_id": "span789",
  "user_id": "user_001",
  "method": "GET",
  "path": "/api/users/001",
  "status_code": 200,
  "duration_ms": 45,
  "message": "Request completed"
}
```

### 4.2 各语言日志库

| 语言    | 日志库                     | 结构化支持 |
| ------- | -------------------------- | ---------- |
| Java    | Logback + Logstash Encoder | 是         |
| Go      | zap, zerolog               | 是         |
| Python  | structlog                  | 是         |
| Node.js | pino, winston              | 是         |
| Rust    | tracing, slog              | 是         |

## 5. 日志采集架构

### 5.1 DaemonSet 模式

每个节点运行一个日志采集器：

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-bit
spec:
  template:
    spec:
      containers:
        - name: fluent-bit
          image: fluent/fluent-bit:3.0
          volumeMounts:
            - name: varlog
              mountPath: /var/log
            - name: containers
              mountPath: /var/lib/docker/containers
      volumes:
        - name: varlog
          hostPath:
            path: /var/log
        - name: containers
          hostPath:
            path: /var/lib/docker/containers
```

### 5.2 Sidecar 模式

每个 Pod 运行一个日志采集器 Sidecar：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-logging
spec:
  containers:
    - name: app
      image: my-app
    - name: log-collector
      image: fluent/fluent-bit:3.0
      volumeMounts:
        - name: log-volume
          mountPath: /logs
  volumes:
    - name: log-volume
      emptyDir: {}
```

### 5.3 模式对比

| 模式      | 资源开销 | 灵活性 | 适用场景   |
| --------- | -------- | ------ | ---------- |
| DaemonSet | 低       | 低     | 标准日志   |
| Sidecar   | 高       | 高     | 特殊格式   |
| 应用直推  | 无       | 最高   | 云原生应用 |

## 6. 日志分析

### 6.1 常用分析场景

**错误率监控**：

```promql
sum(rate(log_entries{level="ERROR"}[5m]))
/
sum(rate(log_entries[5m]))
```

**慢请求分析**：

```
KQL: duration_ms: > 1000 AND level: "WARN"
```

**异常检测**：

- 基于统计的异常检测
- 日志模式聚类
- 关联分析（同一 trace_id 的日志）

### 6.2 日志告警

```yaml
# Elasticsearch 告警规则
- name: error_rate_alert
  index: logs-*
  type: frequency
  filter:
    - term:
        level: ERROR
  threshold: 100
  timeframe:
    minutes: 5
  alert:
    - email
    - slack
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

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 GitOps 与声明式交付

Git 是唯一事实来源：集群状态由仓库声明驱动，差异由控制器调和（Argo CD/Flux）。
PR 流程即变更审批，合并即发布意图；回滚 = revert 提交。
与 CI 衔接：CI 产出镜像，CD 更新清单引用新 digest。
安全：仓库签名、密钥加密（SOPS）、审计日志。

### 13.2 可观测性与 SLO

指标：RED（请求率、错误、时长）与 USE（利用率、饱和、错误）。
日志：结构化（JSON）、集中采集、关联 trace_id。
追踪：OpenTelemetry 传播上下文，瀑布分析延迟。
SLO/错误预算：目标可用性 99.9% 对应每月约 43 分钟不可用预算，驱动发布决策。

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
| 日志管理 | 012-LogManagement | 本文自身 |
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
| Grafana仪表盘配置 | 029-GrafanaTableConfig | 本文的并列主题 |
| ELK-Stack日志分析 | 030-ELKStackLogAnalysis | 本文的并列主题 |
| OpenTelemetry | 031-OpenTelemetry | 本文的并列主题 |
| GitOps与ArgoCD | 032-GitOpsArgoCD | 本文的并列主题 |
| DevOps kubectl 基础命令 | 033-KubectlBasics | 本文的前置基础 |
| DevOps Helm 包管理命令 | 034-HelmCommands | 本文的并列主题 |
| DevOps Jenkins Pipeline | 035-JenkinsPipeline | 本文的并列主题 |
| DevOps GitLab CI/CD | 036-GitLabCI | 本文的并列主题 |
