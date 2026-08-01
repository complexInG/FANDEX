---
order: 330
title: DevOps kubectl 基础命令
module: 031-devops
category: '031-devops'
difficulty: beginner
description: DevOps kubectl 基础命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## kubectl get 查看资源

**基本写法：查看指定类型资源**
`kubectl get <资源类型>`
```bash
# 查看所有 Pod
kubectl get pods
```

**基本写法：查看所有命名空间的资源**
`kubectl get <资源类型> -A`
```bash
# 查看所有命名空间的 Pod
kubectl get pods -A
```

**基本写法：查看指定命名空间资源**
`kubectl get <资源类型> -n <命名空间>`
```bash
# 查看 kube-system 命名空间的 Pod
kubectl get pods -n kube-system
```

**基本写法：显示详细信息**
`kubectl get <资源类型> -o wide`
```bash
# 查看 Pod 详细信息含 IP 和节点
kubectl get pods -o wide
```

**基本写法：输出 YAML 格式**
`kubectl get <资源类型> <名称> -o yaml`
```bash
# 输出 Pod 的完整 YAML
kubectl get pod nginx -o yaml
```

**基本写法：按标签过滤**
`kubectl get <资源类型> -l <标签选择器>`
```bash
# 查看 app=nginx 的 Pod
kubectl get pods -l app=nginx
```

---

## kubectl describe 查看详情

**基本写法：查看资源详细信息**
`kubectl describe <资源类型> <名称>`
```bash
# 查看 nginx Pod 的详细信息
kubectl describe pod nginx
```

**基本写法：查看指定命名空间资源**
`kubectl describe <资源类型> <名称> -n <命名空间>`
```bash
# 查看 kube-system 命名空间的 Pod
kubectl describe pod kube-apiserver -n kube-system
```

**基本写法：查看节点详情**
`kubectl describe node <节点名>`
```bash
# 查看节点详细信息
kubectl describe node node1
```

---

## kubectl create 创建资源

**基本写法：创建 Deployment**
`kubectl create deployment <名称> --image=<镜像>`
```bash
# 创建 nginx Deployment
kubectl create deployment nginx --image=nginx
```

**基本写法：指定副本数创建**
`kubectl create deployment <名称> --image=<镜像> --replicas=<数量>`
```bash
# 创建 3 副本的 nginx Deployment
kubectl create deployment nginx --image=nginx --replicas=3
```

**基本写法：创建命名空间**
`kubectl create namespace <名称>`
```bash
# 创建新命名空间
kubectl create namespace dev
```

**基本写法：创建 Secret**
`kubectl create secret generic <名称> --from-literal=<键>=<值>`
```bash
# 创建包含密码的 Secret
kubectl create secret generic db-secret --from-literal=password=secret123
```

---

## kubectl apply 应用配置

**基本写法：应用 YAML 文件**
`kubectl apply -f <文件>`
```bash
# 应用 deployment.yaml
kubectl apply -f deployment.yaml
```

**基本写法：应用目录下所有文件**
`kubectl apply -f <目录>`
```bash
# 应用 k8s 目录下所有 YAML
kubectl apply -f ./k8s/
```

**基本写法：从 URL 应用**
`kubectl apply -f <URL>`
```bash
# 从 URL 应用配置
kubectl apply -f https://raw.githubusercontent.com/example/repo/main/deploy.yaml
```

**基本写法：使用 kustomize**
`kubectl apply -k <目录>`
```bash
# 使用 kustomize 应用配置
kubectl apply -k ./overlays/prod
```

---

## kubectl delete 删除资源

**基本写法：删除指定资源**
`kubectl delete <资源类型> <名称>`
```bash
# 删除 nginx Pod
kubectl delete pod nginx
```

**基本写法：从文件删除资源**
`kubectl delete -f <文件>`
```bash
# 删除 deployment.yaml 中定义的资源
kubectl delete -f deployment.yaml
```

**基本写法：按标签删除**
`kubectl delete <资源类型> -l <标签选择器>`
```bash
# 删除所有 app=test 的 Pod
kubectl delete pods -l app=test
```

**基本写法：强制删除 Pod**
`kubectl delete pod <名称> --grace-period=0 --force`
```bash
# 强制立即删除 Pod
kubectl delete pod nginx --grace-period=0 --force
```

---

## kubectl exec 进入容器

**基本写法：进入容器 shell**
`kubectl exec -it <Pod> -- <shell>`
```bash
# 进入 nginx Pod 的 bash
kubectl exec -it nginx -- bash
```

**基本写法：在容器中执行命令**
`kubectl exec <Pod> -- <命令>`
```bash
# 查看 Pod 中的进程
kubectl exec nginx -- ps aux
```

**基本写法：指定容器执行**
`kubectl exec -it <Pod> -c <容器名> -- <shell>`
```bash
# 进入指定容器
kubectl exec -it pod1 -c sidecar -- sh
```

---

## kubectl logs 查看日志

**基本写法：查看 Pod 日志**
`kubectl logs <Pod>`
```bash
# 查看 nginx Pod 的日志
kubectl logs nginx
```

**基本写法：实时跟踪日志**
`kubectl logs -f <Pod>`
```bash
# 实时跟踪日志输出
kubectl logs -f nginx
```

**基本写法：查看指定容器日志**
`kubectl logs <Pod> -c <容器名>`
```bash
# 查看 sidecar 容器的日志
kubectl logs pod1 -c sidecar
```

**基本写法：查看前次容器日志**
`kubectl logs <Pod> --previous`
```bash
# 查看容器崩溃前的日志
kubectl logs nginx --previous
```

**基本写法：查看指定时间段的日志**
`kubectl logs <Pod> --since=<时间>`
```bash
# 查看最近 1 小时的日志
kubectl logs nginx --since=1h
```

---

## kubectl scale 伸缩副本

**基本写法：扩缩容 Deployment**
`kubectl scale deployment <名称> --replicas=<数量>`
```bash
# 将 nginx 扩展到 5 个副本
kubectl scale deployment nginx --replicas=5
```

**基本写法：缩容到 0**
`kubectl scale deployment <名称> --replicas=0`
```bash
# 停止所有 nginx 副本
kubectl scale deployment nginx --replicas=0
```

**基本写法：基于文件扩缩容**
`kubectl scale -f <文件> --replicas=<数量>`
```bash
# 基于 YAML 文件扩缩容
kubectl scale -f deployment.yaml --replicas=3
```

---

## kubectl port-forward 端口转发

**基本写法：转发 Pod 端口**
`kubectl port-forward <Pod> <宿主端口>:<容器端口>`
```bash
# 将本地 8080 转发到 Pod 的 80
kubectl port-forward nginx 8080:80
```

**基本写法：转发 Service 端口**
`kubectl port-forward svc/<Service> <宿主端口>:<服务端口>`
```bash
# 转发 Service 端口到本地
kubectl port-forward svc/nginx 8080:80
```

**基本写法：绑定指定地址**
`kubectl port-forward <Pod> <地址>:<宿主端口>:<容器端口>`
```bash
# 绑定到所有地址
kubectl port-forward nginx 0.0.0.0:8080:80
```

---

## kubectl config 配置管理

**基本写法：查看当前上下文**
`kubectl config current-context`
```bash
# 查看当前使用的上下文
kubectl config current-context
```

**基本写法：切换上下文**
`kubectl config use-context <上下文>`
```bash
# 切换到生产环境上下文
kubectl config use-context prod-cluster
```

**基本写法：列出所有上下文**
`kubectl config get-contexts`
```bash
# 列出所有可用的上下文
kubectl config get-contexts
```

**基本写法：设置默认命名空间**
`kubectl config set-context --current --namespace=<命名空间>`
```bash
# 设置当前上下文的默认命名空间
kubectl config set-context --current --namespace=dev
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
| DevOps kubectl 基础命令 | 033-KubectlBasics | 本文自身 |
| DevOps Helm 包管理命令 | 034-HelmCommands | 本文的并列主题 |
| DevOps Jenkins Pipeline | 035-JenkinsPipeline | 本文的并列主题 |
| DevOps GitLab CI/CD | 036-GitLabCI | 本文的并列主题 |
