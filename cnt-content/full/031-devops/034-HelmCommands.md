---
order: 340
title: DevOps Helm 包管理命令
module: 031-devops
category: '031-devops'
difficulty: beginner
description: DevOps Helm 包管理命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# DevOps Helm 包管理命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## helm install 安装 Chart

**基本写法：安装 Chart**
`helm install <名称> <Chart>`
```bash
# 安装 nginx Chart
helm install my-nginx bitnami/nginx
```

**基本写法：指定命名空间安装**
`helm install <名称> <Chart> -n <命名空间>`
```bash
# 在 dev 命名空间安装
helm install my-nginx bitnami/nginx -n dev
```

**基本写法：通过 values 文件安装**
`helm install <名称> <Chart> -f <values文件>`
```bash
# 使用自定义 values 安装
helm install my-nginx bitnami/nginx -f custom-values.yaml
```

**基本写法：命令行传参安装**
`helm install <名称> <Chart> --set <键>=<值>`
```bash
# 设置副本数和镜像版本
helm install my-nginx bitnami/nginx --set replicaCount=3 --set image.tag=1.25
```

**基本写法：本地 Chart 安装**
`helm install <名称> <路径>`
```bash
# 安装本地 Chart
helm install my-app ./mychart
```

---

## helm upgrade 升级 Chart

**基本写法：升级 Release**
`helm upgrade <名称> <Chart>`
```bash
# 升级 my-nginx Chart
helm upgrade my-nginx bitnami/nginx
```

**基本写法：升级并安装**
`helm upgrade <名称> <Chart> --install`
```bash
# 不存在则安装，存在则升级
helm upgrade my-nginx bitnami/nginx --install
```

**基本写法：使用新 values 升级**
`helm upgrade <名称> <Chart> -f <values文件>`
```bash
# 使用新配置升级
helm upgrade my-nginx bitnami/nginx -f new-values.yaml
```

**基本写法：命令行传参升级**
`helm upgrade <名称> <Chart> --set <键>=<值>`
```bash
# 通过命令行参数升级
helm upgrade my-nginx bitnami/nginx --set replicaCount=5
```

---

## helm uninstall 卸载 Chart

**基本写法：卸载 Release**
`helm uninstall <名称>`
```bash
# 卸载 my-nginx Release
helm uninstall my-nginx
```

**基本写法：指定命名空间卸载**
`helm uninstall <名称> -n <命名空间>`
```bash
# 卸载指定命名空间的 Release
helm uninstall my-nginx -n dev
```

**基本写法：保留历史记录卸载**
`helm uninstall <名称> --keep-history`
```bash
# 卸载但保留历史记录
helm uninstall my-nginx --keep-history
```

---

## helm list 查看 Release

**基本写法：查看所有 Release**
`helm list`
```bash
# 列出所有已安装的 Release
helm list
```

**基本写法：查看所有命名空间的 Release**
`helm list -A`
```bash
# 列出所有命名空间的 Release
helm list -A
```

**基本写法：包含已卸载的 Release**
`helm list --all`
```bash
# 列出包含已卸载的所有 Release
helm list --all
```

**基本写法：查看指定命名空间**
`helm list -n <命名空间>`
```bash
# 查看 dev 命名空间的 Release
helm list -n dev
```

---

## helm search 搜索 Chart

**基本写法：搜索 Hub 上的 Chart**
`helm search hub <关键词>`
```bash
# 搜索 nginx 相关的 Chart
helm search hub nginx
```

**基本写法：搜索已添加仓库的 Chart**
`helm search repo <关键词>`
```bash
# 在已添加的仓库中搜索
helm search repo nginx
```

---

## helm repo 仓库管理

**基本写法：添加仓库**
`helm repo add <名称> <URL>`
```bash
# 添加 bitnami 仓库
helm repo add bitnami https://charts.bitnami.com/bitnami
```

**基本写法：更新仓库**
`helm repo update`
```bash
# 更新所有已添加的仓库
helm repo update
```

**基本写法：列出所有仓库**
`helm repo list`
```bash
# 列出所有已添加的仓库
helm repo list
```

**基本写法：删除仓库**
`helm repo remove <名称>`
```bash
# 删除 bitnami 仓库
helm repo remove bitnami
```

---

## helm pull 下载 Chart

**基本写法：下载 Chart**
`helm pull <仓库>/<Chart>`
```bash
# 下载 nginx Chart
helm pull bitnami/nginx
```

**基本写法：下载并解压**
`helm pull <仓库>/<Chart> --untar`
```bash
# 下载并解压到当前目录
helm pull bitnami/nginx --untar
```

**基本写法：指定版本下载**
`helm pull <仓库>/<Chart> --version <版本>`
```bash
# 下载指定版本
helm pull bitnami/nginx --version 15.0.0
```

**基本写法：指定下载目录**
`helm pull <仓库>/<Chart> --untar --untardir <目录>`
```bash
# 解压到指定目录
helm pull bitnami/nginx --untar --untardir ./charts
```

---

## helm create 创建 Chart

**基本写法：创建新 Chart**
`helm create <名称>`
```bash
# 创建名为 myapp 的 Chart
helm create myapp
```

**基本写法：指定 Chart 路径**
`helm create <路径>/<名称>`
```bash
# 在指定路径创建 Chart
helm create ./charts/myapp
```

---

## helm template 渲染模板

**基本写法：渲染模板**
`helm template <名称> <Chart>`
```bash
# 渲染 myapp Chart 的模板
helm template myapp ./mychart
```

**基本写法：使用 values 渲染**
`helm template <名称> <Chart> -f <values文件>`
```bash
# 使用 values 渲染模板
helm template myapp ./mychart -f values.yaml
```

**基本写法：命令行传参渲染**
`helm template <名称> <Chart> --set <键>=<值>`
```bash
# 通过命令行参数渲染
helm template myapp ./mychart --set image.tag=v2
```

---

## helm history/rollback 回滚

**基本写法：查看 Release 历史**
`helm history <名称>`
```bash
# 查看 my-nginx 的历史版本
helm history my-nginx
```

**基本写法：回滚到指定版本**
`helm rollback <名称> <版本号>`
```bash
# 回滚到版本 2
helm rollback my-nginx 2
```

---

## helm status 查看 Release 状态

**基本写法：查看 Release 状态**
`helm status <名称>`
```bash
# 查看 my-nginx 的状态
helm status my-nginx
```

**基本写法：查看指定命名空间状态**
`helm status <名称> -n <命名空间>`
```bash
# 查看 dev 命名空间的 Release 状态
helm status my-nginx -n dev
```

**基本写法：显示资源信息**
`helm status <名称> --show-resources`
```bash
# 显示 Release 相关的所有资源
helm status my-nginx --show-resources
```

---

## helm show 查看 Chart 信息

**基本写法：查看 Chart 的 values**
`helm show values <Chart>`
```bash
# 查看 nginx Chart 的默认 values
helm show values bitnami/nginx
```

**基本写法：查看 Chart 信息**
`helm show chart <Chart>`
```bash
# 查看 Chart 的 Chart.yaml 内容
helm show chart bitnami/nginx
```

**基本写法：查看 Chart 全部信息**
`helm show all <Chart>`
```bash
# 查看 Chart 的所有信息
helm show all bitnami/nginx
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
| Grafana仪表盘配置 | 029-GrafanaTableConfig | 本文的并列主题 |
| ELK-Stack日志分析 | 030-ELKStackLogAnalysis | 本文的并列主题 |
| OpenTelemetry | 031-OpenTelemetry | 本文的并列主题 |
| GitOps与ArgoCD | 032-GitOpsArgoCD | 本文的并列主题 |
| DevOps kubectl 基础命令 | 033-KubectlBasics | 本文的前置基础 |
| DevOps Helm 包管理命令 | 034-HelmCommands | 本文自身 |
| DevOps Jenkins Pipeline | 035-JenkinsPipeline | 本文的并列主题 |
| DevOps GitLab CI/CD | 036-GitLabCI | 本文的并列主题 |
