---
order: 380
title: 云计算 Azure 存储命令
module: cloud-computing

category: '034-cloud-computing'
difficulty: beginner
description: 云计算 Azure 存储命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 存储账户

**基本写法：创建存储账户**
`az storage account create --resource-group <资源组名> --name <账户名> --location <区域> --sku <SKU>`
```bash
# 创建本地冗余存储账户
az storage account create --resource-group MyResourceGroup --name storage134 --location eastus --sku Standard_LRS
```

---

**基本写法：列出存储账户**
`az storage account list [--resource-group <资源组名>]`
```bash
# 列出当前订阅所有存储账户
az storage account list
```

---

**基本写法：查看账户详情**
`az storage account show --resource-group <资源组名> --name <账户名>`
```bash
# 查看存储账户属性
az storage account show --resource-group MyResourceGroup --name storage134
```

---

**基本写法：更新访问层**
`az storage account update --resource-group <资源组名> --name <账户名> --access-tier <Hot|Cool>`
```bash
# 设置访问层为 Hot
az storage account update --resource-group MyResourceGroup --name storage134 --access-tier Hot
```

---

**基本写法：获取账户密钥**
`az storage account keys list --resource-group <资源组名> --account-name <账户名>`
```bash
# 获取存储账户访问密钥
az storage account keys list --resource-group MyResourceGroup --account-name storage134
```

---

**基本写法：删除存储账户**
`az storage account delete --resource-group <资源组名> --name <账户名>`
```bash
# 删除存储账户
az storage account delete --resource-group MyResourceGroup --name storage134
```

---

## Blob 容器

**基本写法：创建容器**
`az storage container create --name <容器名> --account-name <账户名>`
```bash
# 在存储账户中创建 Blob 容器
az storage container create --name my-container --account-name storage134
```

---

**基本写法：列出容器**
`az storage container list --account-name <账户名>`
```bash
# 列出所有 Blob 容器
az storage container list --account-name storage134
```

---

**基本写法：列出容器内 Blob**
`az storage blob list --container-name <容器名> --account-name <账户名>`
```bash
# 列出容器内所有 Blob
az storage blob list --container-name my-container --account-name storage134
```

---

## Blob 操作

**基本写法：上传文件到 Blob**
`az storage blob upload --account-name <账户名> --container-name <容器名> --name <Blob名> --file <本地文件>`
```bash
# 上传本地文件到 Blob 容器
az storage blob upload --account-name storage134 --container-name my-container --name data.txt --file ./data.txt
```

---

**基本写法：上传时指定访问层**
`az storage blob upload --account-name <账户名> --container-name <容器名> --file <文件> --tier <层>`
```bash
# 上传并设置为 Hot 访问层
az storage blob upload --account-name storage134 --container-name my-container --file ./data.txt --tier Hot
```

---

**基本写法：下载 Blob**
`az storage blob download --account-name <账户名> --container-name <容器名> --name <Blob名> --file <本地文件>`
```bash
# 下载 Blob 到本地
az storage blob download --account-name storage134 --container-name my-container --name data.txt --file ./downloaded.txt
```

---

**基本写法：删除 Blob**
`az storage blob delete --account-name <账户名> --container-name <容器名> --name <Blob名>`
```bash
# 删除指定 Blob
az storage blob delete --account-name storage134 --container-name my-container --name data.txt
```

---

**基本写法：更改 Blob 访问层**
`az storage blob set-tier --account-name <账户名> --container-name <容器名> --name <Blob名> --tier <层>`
```bash
# 将 Blob 设置为 P10 高级层
az storage blob set-tier --account-name storage134 --container-name my-container --name data.txt --tier P10
```

---

## 连接字符串

**基本写法：获取连接字符串**
`az storage account show-connection-string --resource-group <资源组名> --name <账户名>`
```bash
# 获取用于应用配置的连接字符串
az storage account show-connection-string --resource-group MyResourceGroup --name storage134
```

---

**基本写法：使用连接字符串操作**
`az storage blob list --container-name <容器名> --connection-string "<连接字符串>"`
```bash
# 通过连接字符串列出 Blob
az storage blob list --container-name my-container --connection-string "DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net"
```

---

## 文件共享

**基本写法：创建文件共享**
`az storage share create --name <共享名> --account-name <账户名>`
```bash
# 创建 Azure 文件共享
az storage share create --name my-share --account-name storage134
```

---

**基本写法：上传文件到共享**
`az storage file upload --share-name <共享名> --source <本地文件> --account-name <账户名>`
```bash
# 上传文件到文件共享
az storage file upload --share-name my-share --source ./file.txt --account-name storage134
```

---

## 队列与表

**基本写法：创建队列**
`az storage queue create --name <队列名> --account-name <账户名>`
```bash
# 创建存储队列用于消息传递
az storage queue create --name my-queue --account-name storage134
```

---

**基本写法：向队列添加消息**
`az storage message put --queue-name <队列名> --content "<消息>" --account-name <账户名>`
```bash
# 向队列添加一条文本消息
az storage message put --queue-name my-queue --content "Hello" --account-name storage134
```

---

**基本写法：从队列取消息**
`az storage message get --queue-name <队列名> --account-name <账户名>`
```bash
# 取出队列中下一条消息
az storage message get --queue-name my-queue --account-name storage134
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
