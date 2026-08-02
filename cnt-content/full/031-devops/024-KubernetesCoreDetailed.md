---
order: 101
title: Kubernetes核心资源详解
module: devops
category: 'eng-infra'
difficulty: intermediate
description: 'Kubernetes 核心资源：Pod、Service、Deployment、Ingress、ConfigMap、Secret、HPA、StatefulSet。'
author: fanquanpp
updated: '2026-08-01'
related:
  - devops/数据库运维
  - devops/Dockerfile多阶段构建
  - 'devops/Helm-Chart应用打包'
  - devops/Terraform资源编排
prerequisites:
  - devops/概述与Linux基础
---

## 1. Pod 与 Deployment

### 1.1 Pod 生命周期

Pod 生命周期是Kubernetes核心资源详解的重要组成部分。本节详细介绍Pod 生命周期的核心概念、工作原理和实际应用。

**关键要点**：

- Pod 生命周期的定义与核心原理
- Pod 生命周期的实现方式与技术细节
- Pod 生命周期在实际场景中的应用与最佳实践
- Pod 生命周期的常见问题与解决方案

Pod 生命周期在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Deployment 滚动更新

Deployment 滚动更新是Kubernetes核心资源详解的重要组成部分。本节详细介绍Deployment 滚动更新的核心概念、工作原理和实际应用。

**关键要点**：

- Deployment 滚动更新的定义与核心原理
- Deployment 滚动更新的实现方式与技术细节
- Deployment 滚动更新在实际场景中的应用与最佳实践
- Deployment 滚动更新的常见问题与解决方案

Deployment 滚动更新在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Service 与 Ingress

### 2.1 Service 类型

Service 类型是Kubernetes核心资源详解的重要组成部分。本节详细介绍Service 类型的核心概念、工作原理和实际应用。

**关键要点**：

- Service 类型的定义与核心原理
- Service 类型的实现方式与技术细节
- Service 类型在实际场景中的应用与最佳实践
- Service 类型的常见问题与解决方案

Service 类型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Ingress 路由规则

Ingress 路由规则是Kubernetes核心资源详解的重要组成部分。本节详细介绍Ingress 路由规则的核心概念、工作原理和实际应用。

**关键要点**：

- Ingress 路由规则的定义与核心原理
- Ingress 路由规则的实现方式与技术细节
- Ingress 路由规则在实际场景中的应用与最佳实践
- Ingress 路由规则的常见问题与解决方案

Ingress 路由规则在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 配置与密钥

### 3.1 ConfigMap

ConfigMap是Kubernetes核心资源详解的重要组成部分。本节详细介绍ConfigMap的核心概念、工作原理和实际应用。

**关键要点**：

- ConfigMap的定义与核心原理
- ConfigMap的实现方式与技术细节
- ConfigMap在实际场景中的应用与最佳实践
- ConfigMap的常见问题与解决方案

ConfigMap在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 Secret

Secret是Kubernetes核心资源详解的重要组成部分。本节详细介绍Secret的核心概念、工作原理和实际应用。

**关键要点**：

- Secret的定义与核心原理
- Secret的实现方式与技术细节
- Secret在实际场景中的应用与最佳实践
- Secret的常见问题与解决方案

Secret在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 有状态与弹性

### 4.1 StatefulSet

StatefulSet是Kubernetes核心资源详解的重要组成部分。本节详细介绍StatefulSet的核心概念、工作原理和实际应用。

**关键要点**：

- StatefulSet的定义与核心原理
- StatefulSet的实现方式与技术细节
- StatefulSet在实际场景中的应用与最佳实践
- StatefulSet的常见问题与解决方案

StatefulSet在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 HPA 自动伸缩

HPA 自动伸缩是Kubernetes核心资源详解的重要组成部分。本节详细介绍HPA 自动伸缩的核心概念、工作原理和实际应用。

**关键要点**：

- HPA 自动伸缩的定义与核心原理
- HPA 自动伸缩的实现方式与技术细节
- HPA 自动伸缩在实际场景中的应用与最佳实践
- HPA 自动伸缩的常见问题与解决方案

HPA 自动伸缩在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 延伸阅读
Docker 与 Kubernetes 深入，见 031-devops 模块文档。
CI/CD 管线设计，见 031-devops 模块 CICD 文档。
云原生架构，见 034-cloud-computing 模块。
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
