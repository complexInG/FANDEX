---
order: 310
title: 云计算 AWS S3 命令
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: 云计算 AWS S3 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 桶操作

**基本写法：列出所有桶**
`aws s3 ls [--profile <配置名>]`
```bash
# 列出当前账号下所有 S3 桶
aws s3 ls
```

---

**基本写法：创建桶**
`aws s3 mb s3://<桶名> [--region <区域>]`
```bash
# 在默认区域创建新桶
aws s3 mb s3://my-unique-bucket
```

---

**基本写法：指定区域创建桶**
`aws s3 mb s3://<桶名> --region <区域>`
```bash
# 在 eu-west-1 区域创建桶
aws s3 mb s3://my-bucket --region eu-west-1
```

---

**基本写法：删除空桶**
`aws s3 rb s3://<桶名>`
```bash
# 仅删除空桶
aws s3 rb s3://my-bucket
```

---

**基本写法：强制删除非空桶**
`aws s3 rb s3://<桶名> --force`
```bash
# 删除桶及其所有对象
aws s3 rb s3://my-bucket --force
```

---

## 对象操作

**基本写法：列出桶内对象**
`aws s3 ls s3://<桶名>[/<前缀>] [--recursive]`
```bash
# 递归列出桶内所有对象
aws s3 ls s3://my-bucket --recursive
```

---

**基本写法：上传文件**
`aws s3 cp <本地文件> s3://<桶名>/[<路径>]`
```bash
# 上传单个文件到 S3
aws s3 cp file.txt s3://my-bucket/
```

---

**基本写法：下载文件**
`aws s3 cp s3://<桶名>/<键> <本地路径>`
```bash
# 从 S3 下载文件到本地
aws s3 cp s3://my-bucket/file.txt ./
```

---

**基本写法：递归上传目录**
`aws s3 cp <本地目录> s3://<桶名>/<前缀> --recursive`
```bash
# 递归上传整个目录
aws s3 cp ./folder s3://my-bucket/folder --recursive
```

---

**基本写法：同步本地到 S3**
`aws s3 sync <本地目录> s3://<桶名>/<前缀> [--delete] [--exclude <模式>]`
```bash
# 同步并删除目标中多余的文件
aws s3 sync ./src s3://my-bucket/src --delete --exclude "*.tmp"
```

---

**基本写法：删除单个对象**
`aws s3 rm s3://<桶名>/<键>`
```bash
# 删除指定对象
aws s3 rm s3://my-bucket/file.txt
```

---

**基本写法：递归删除目录**
`aws s3 rm s3://<桶名>/<前缀> --recursive`
```bash
# 递归删除目录下所有对象
aws s3 rm s3://my-bucket/folder --recursive
```

---

## 高级 API

**基本写法：使用 s3api 创建桶**
`aws s3api create-bucket --bucket <桶名> [--region <区域>]`
```bash
# 通过 s3api 精细控制创建桶
aws s3api create-bucket --bucket my-bucket --region us-east-1
```

---

**基本写法：获取桶大小统计**
`aws s3 ls s3://<桶名> --recursive --summarize`
```bash
# 统计桶内对象总数与总大小
aws s3 ls s3://my-bucket --recursive --summarize
```

---

**基本写法：预览操作不实际执行**
`<命令> --dryrun`
```bash
# 预览同步将执行的更改
aws s3 sync ./src s3://my-bucket/src --dryrun
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
