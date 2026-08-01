---
order: 390
title: 云计算 GCP gcloud 配置
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: 云计算 GCP gcloud 配置 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 安装与初始化

**基本写法：安装 gcloud CLI**
`sudo apt-get install -y google-cloud-cli`
```bash
# 在 Ubuntu 上通过官方源安装
sudo apt-get install -y google-cloud-cli
```

---

**基本写法：交互式初始化**
`gcloud init`
```bash
# 启动配置向导进行账号项目区域设置
gcloud init
```

---

**基本写法：查看安装信息**
`gcloud info`
```bash
# 显示 gcloud 安装路径与版本
gcloud info
```

---

**基本写法：查看版本**
`gcloud version`
```bash
# 输出 gcloud 及组件版本
gcloud version
```

---

**基本写法：升级组件**
`gcloud components update`
```bash
# 升级所有已安装组件
gcloud components update
```

---

## 认证登录

**基本写法：用户账号登录**
`gcloud auth login`
```bash
# 通过浏览器进行账号认证
gcloud auth login
```

---

**基本写法：应用默认凭证**
`gcloud auth application-default login`
```bash
# 为本地应用配置默认凭证
gcloud auth application-default login
```

---

**基本写法：列出已认证账号**
`gcloud auth list`
```bash
# 查看当前已登录账号列表
gcloud auth list
```

---

**基本写法：撤销认证**
`gcloud auth revoke [<账号>]`
```bash
# 撤销当前账号认证
gcloud auth revoke
```

---

## 项目管理

**基本写法：列出所有项目**
`gcloud projects list`
```bash
# 查看账号下所有项目
gcloud projects list
```

---

**基本写法：创建项目**
`gcloud projects create <项目ID>`
```bash
# 创建新项目
gcloud projects create my-new-project-123
```

---

**基本写法：查看项目详情**
`gcloud projects describe <项目ID>`
```bash
# 查看项目元数据
gcloud projects describe my-new-project-123
```

---

**基本写法：删除项目**
`gcloud projects delete <项目ID>`
```bash
# 删除指定项目
gcloud projects delete my-new-project-123
```

---

## 配置管理

**基本写法：列出当前配置**
`gcloud config list`
```bash
# 查看当前激活配置的属性
gcloud config list
```

---

**基本写法：设置默认项目**
`gcloud config set project <项目ID>`
```bash
# 设置默认项目避免每次指定
gcloud config set project my-project-id
```

---

**基本写法：设置默认区域**
`gcloud config set compute/region <区域>`
```bash
# 设置默认计算区域
gcloud config set compute/region us-central1
```

---

**基本写法：设置默认可用区**
`gcloud config set compute/zone <可用区>`
```bash
# 设置默认计算可用区
gcloud config set compute/zone us-central1-a
```

---

**基本写法：获取当前项目**
`gcloud config get-value project`
```bash
# 查看当前默认项目 ID
gcloud config get-value project
```

---

## 多配置管理

**基本写法：创建命名配置**
`gcloud config configurations create <配置名>`
```bash
# 创建独立配置用于多项目管理
gcloud config configurations create my-config
```

---

**基本写法：列出所有配置**
`gcloud config configurations list`
```bash
# 查看所有命名配置
gcloud config configurations list
```

---

**基本写法：切换激活配置**
`gcloud config configurations activate <配置名>`
```bash
# 切换到指定配置
gcloud config configurations activate my-config
```

---

**基本写法：查看当前配置名**
`gcloud config configurations describe <配置名>`
```bash
# 查看指定配置详情
gcloud config configurations describe my-config
```

---

## 组件管理

**基本写法：列出已安装组件**
`gcloud components list`
```bash
# 查看所有可用与已安装组件
gcloud components list
```

---

**基本写法：安装组件**
`gcloud components install <组件名>`
```bash
# 安装 kubectl 等额外组件
gcloud components install kubectl
```

---

**基本写法：移除组件**
`gcloud components remove <组件名>`
```bash
# 移除不再使用的组件
gcloud components remove kubectl
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

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 FinOps 成本治理

三阶段：可见（成本分配与预算）、优化（右尺寸、Spot、闲置清理）、运营（持续迭代与责任到团队）。
工具：云厂商成本中心、OpenCost、Kubecost。
组织：FinOps 实践者角色、定期 review、浪费告警。
度量：单位成本（每请求/每用户成本）而非绝对金额。

### 13.2 高可用与容灾设计

可用性数学：99.9% 年停机约 8.7 小时，99.99% 约 52 分钟；多副本降低单点风险。
RPO（可容忍数据丢失）与 RTO（恢复时间）驱动备份与复制策略。
模式：多可用区部署、跨区域异步复制、数据库主备、对象存储版本。
演练：混沌工程（Chaos Monkey 思想）验证真实故障行为。
