---
order: 102
title: 'Helm-Chart应用打包'
module: devops
category: 'eng-infra'
difficulty: intermediate
description: 'Helm Chart 应用打包：Chart 结构、模板语法、Values 覆盖与仓库管理。'
author: fanquanpp
updated: '2026-08-01'
related:
  - devops/Dockerfile多阶段构建
  - devops/Kubernetes核心资源详解
  - devops/Terraform资源编排
  - 'devops/Ansible-Playbook配置管理'
prerequisites:
  - devops/概述与Linux基础
---

## 1. Chart 结构

### 1.1 目录布局

目录布局是Helm-Chart应用打包的重要组成部分。本节详细介绍目录布局的核心概念、工作原理和实际应用。

**关键要点**：

- 目录布局的定义与核心原理
- 目录布局的实现方式与技术细节
- 目录布局在实际场景中的应用与最佳实践
- 目录布局的常见问题与解决方案

目录布局在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Chart.yaml 与 values.yaml

Chart.yaml 与 values.yaml是Helm-Chart应用打包的重要组成部分。本节详细介绍Chart.yaml 与 values.yaml的核心概念、工作原理和实际应用。

**关键要点**：

- Chart.yaml 与 values.yaml的定义与核心原理
- Chart.yaml 与 values.yaml的实现方式与技术细节
- Chart.yaml 与 values.yaml在实际场景中的应用与最佳实践
- Chart.yaml 与 values.yaml的常见问题与解决方案

Chart.yaml 与 values.yaml在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 模板语法

### 2.1 Go Template

Go Template是Helm-Chart应用打包的重要组成部分。本节详细介绍Go Template的核心概念、工作原理和实际应用。

**关键要点**：

- Go Template的定义与核心原理
- Go Template的实现方式与技术细节
- Go Template在实际场景中的应用与最佳实践
- Go Template的常见问题与解决方案

Go Template在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 内置函数与管道

内置函数与管道是Helm-Chart应用打包的重要组成部分。本节详细介绍内置函数与管道的核心概念、工作原理和实际应用。

**关键要点**：

- 内置函数与管道的定义与核心原理
- 内置函数与管道的实现方式与技术细节
- 内置函数与管道在实际场景中的应用与最佳实践
- 内置函数与管道的常见问题与解决方案

内置函数与管道在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 \_helpers.tpl

\_helpers.tpl是Helm-Chart应用打包的重要组成部分。本节详细介绍\_helpers.tpl的核心概念、工作原理和实际应用。

**关键要点**：

- \_helpers.tpl的定义与核心原理
- \_helpers.tpl的实现方式与技术细节
- \_helpers.tpl在实际场景中的应用与最佳实践
- \_helpers.tpl的常见问题与解决方案

\_helpers.tpl在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Values 管理

### 3.1 默认值与覆盖

默认值与覆盖是Helm-Chart应用打包的重要组成部分。本节详细介绍默认值与覆盖的核心概念、工作原理和实际应用。

**关键要点**：

- 默认值与覆盖的定义与核心原理
- 默认值与覆盖的实现方式与技术细节
- 默认值与覆盖在实际场景中的应用与最佳实践
- 默认值与覆盖的常见问题与解决方案

默认值与覆盖在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 子 Chart Values

子 Chart Values是Helm-Chart应用打包的重要组成部分。本节详细介绍子 Chart Values的核心概念、工作原理和实际应用。

**关键要点**：

- 子 Chart Values的定义与核心原理
- 子 Chart Values的实现方式与技术细节
- 子 Chart Values在实际场景中的应用与最佳实践
- 子 Chart Values的常见问题与解决方案

子 Chart Values在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 仓库与发布

### 4.1 Chart 仓库

Chart 仓库是Helm-Chart应用打包的重要组成部分。本节详细介绍Chart 仓库的核心概念、工作原理和实际应用。

**关键要点**：

- Chart 仓库的定义与核心原理
- Chart 仓库的实现方式与技术细节
- Chart 仓库在实际场景中的应用与最佳实践
- Chart 仓库的常见问题与解决方案

Chart 仓库在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 helm install/upgrade/rollback

helm install/upgrade/rollback是Helm-Chart应用打包的重要组成部分。本节详细介绍helm install/upgrade/rollback的核心概念、工作原理和实际应用。

**关键要点**：

- helm install/upgrade/rollback的定义与核心原理
- helm install/upgrade/rollback的实现方式与技术细节
- helm install/upgrade/rollback在实际场景中的应用与最佳实践
- helm install/upgrade/rollback的常见问题与解决方案

helm install/upgrade/rollback在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

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
| Helm-Chart应用打包 | 025-HelmChartApplicationPackage | 本文自身 |
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
