---
order: 300
title: 云计算 AWS CLI 配置
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: 云计算 AWS CLI 配置 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 安装与版本

**基本写法：安装 AWS CLI**
`pip install awscli` 或 `brew install awscli`
```bash
# 通过 pip 安装 AWS CLI v2
pip install awscliv2
```

---

**基本写法：查看版本**
`aws --version`
```bash
# 输出 CLI 版本与依赖库版本
aws --version
```

---

**基本写法：升级 CLI**
`pip install --upgrade awscli`
```bash
# 升级到最新版本
pip install --upgrade awscli
```

---

## 凭证配置

**基本写法：交互式配置**
`aws configure [--profile <配置名>]`
```bash
# 配置默认账户的密钥与区域
aws configure
```

---

**基本写法：配置命名 Profile**
`aws configure --profile <配置名>`
```bash
# 为生产环境创建独立配置
aws configure --profile production
```

---

**基本写法：设置单项配置值**
`aws configure set <键> <值> [--profile <配置名>]`
```bash
# 设置默认区域为 us-west-2
aws configure set region us-west-2
```

---

**基本写法：查看当前配置**
`aws configure list [--profile <配置名>]`
```bash
# 列出当前所有配置项
aws configure list
```

---

**基本写法：通过环境变量配置**
`export AWS_<KEY>=<值>`
```bash
# 设置访问密钥与默认区域
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-east-1
```

---

## 身份验证

**基本写法：获取当前调用者身份**
`aws sts get-caller-identity [--profile <配置名>]`
```bash
# 验证当前凭证对应的账号与用户
aws sts get-caller-identity
```

---

**基本写法：切换默认 Profile**
`export AWS_PROFILE=<配置名>`
```bash
# 切换默认使用 production profile
export AWS_PROFILE=production
```

---

## 输出格式

**基本写法：指定输出格式**
`aws <命令> --output <json|table|text>`
```bash
# 以表格形式输出 EC2 实例
aws ec2 describe-instances --output table
```

---

**基本写法：使用 JMESPath 查询过滤**
`aws <命令> --query '<JMESPath 表达式>'`
```bash
# 仅提取实例 ID
aws ec2 describe-instances --query 'Reservations[0].Instances[0].InstanceId' --output text
```

---

**基本写法：查看配置文件位置**
`cat ~/.aws/credentials`
```bash
# 查看本地凭证文件内容
cat ~/.aws/credentials
```

---

**基本写法：列出所有 Profile**
`cat ~/.aws/config`
```bash
# 查看所有命名 profile 配置
cat ~/.aws/config
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
