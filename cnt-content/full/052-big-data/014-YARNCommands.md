---
order: 140
title: 大数据 YARN 命令
module: big-data

category: '052-big-data'
difficulty: beginner
description: 大数据 YARN 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 应用管理

**基本写法：查看运行中的应用**
`yarn application -list`

```bash
# 查看所有运行中的 YARN 应用
yarn application -list
```

---

**基本写法：按状态过滤应用**
`yarn application -list -appStates <状态>`

```bash
# 查看所有状态的应用
yarn application -list -appStates ALL
# 查看已完成的应用
yarn application -list -appStates FINISHED
```

---

**基本写法：查看应用详情**
`yarn application -status <应用ID>`

```bash
# 查看指定应用的详细信息
yarn application -status application_1234567890_0001
```

---

**基本写法：杀死应用**
`yarn application -kill <应用ID>`

```bash
# 终止指定的 YARN 应用
yarn application -kill application_1234567890_0001
```

---

**基本写法：查看应用尝试**
`yarn applicationattempt -list <应用ID>`

```bash
# 查看应用的所有尝试记录
yarn applicationattempt -list application_1234567890_0001
```

---

**基本写法：查看应用尝试状态**
`yarn applicationattempt -status <尝试ID>`

```bash
# 查看应用尝试的详细信息
yarn applicationattempt -status appattempt_1234567890_0001_000001
```

---

## 节点管理

**基本写法：查看所有节点**
`yarn node -list`

```bash
# 查看集群所有节点
yarn node -list
```

---

**基本写法：查看节点状态**
`yarn node -status <节点ID>`

```bash
# 查看指定节点详细信息
yarn node -status node1:8041
```

---

**基本写法：查看所有节点状态**
`yarn node -list -showDetails`

```bash
# 查看所有节点的详细信息
yarn node -list -showDetails
```

---

## Container 管理

**基本写法：查看应用的 Container**
`yarn container -list <应用尝试ID>`

```bash
# 查看应用尝试的所有 Container
yarn container -list appattempt_1234567890_0001_000001
```

---

**基本写法：查看 Container 状态**
`yarn container -status <Container ID>`

```bash
# 查看指定 Container 状态
yarn container -status container_1234567890_0001_01_000001
```

---

## 队列管理

**基本写法：查看队列列表**
`yarn queue -status <队列名>`

```bash
# 查看指定队列状态
yarn queue -status default
```

---

**基本写法：查看所有队列**
`yarn queue -list`

```bash
# 查看所有队列
yarn queue -list
```

---

**基本写法：停止队列**
`yarn queue -stop <队列名>`

```bash
# 停止指定队列
yarn queue -stop my_queue
```

---

**基本写法：启动队列**
`yarn queue -start <队列名>`

```bash
# 启动指定队列
yarn queue -start my_queue
```

---

## 日志管理

**基本写法：查看应用日志**
`yarn logs -applicationId <应用ID>`

```bash
# 查看指定应用的日志
yarn logs -applicationId application_1234567890_0001
```

---

**基本写法：查看指定 Container 日志**
`yarn logs -applicationId <应用ID> -containerId <Container ID>`

```bash
# 查看指定 Container 的日志
yarn logs -applicationId application_1234567890_0001 \
    -containerId container_1234567890_0001_01_000001
```

---

**基本写法：下载日志**
`yarn logs -applicationId <应用ID> -out <输出路径>`

```bash
# 下载应用日志到本地
yarn logs -applicationId application_1234567890_0001 -out ./app_logs
```

---

**基本写法：查看日志末尾**
`yarn logs -applicationId <应用ID> -logFiles <日志文件> -size <字节数>`

```bash
# 查看日志末尾指定大小
yarn logs -applicationId application_1234567890_0001 -logFiles stderr -size 1024
```

---

**基本写法：显示所有日志文件**
`yarn logs -applicationId <应用ID> -showApplicationLogInfo`

```bash
# 显示应用所有日志文件列表
yarn logs -applicationId application_1234567890_0001 -showApplicationLogInfo
```

---

## 集群信息

**基本写法：查看集群信息**
`yarn cluster -list`

```bash
# 查看集群节点列表
yarn cluster -list
```

---

**基本写法：查看集群拓扑**
`yarn cluster -nodes`

```bash
# 查看集群节点状态
yarn cluster -nodes
```

---

## ResourceManager 管理

**基本写法：刷新队列**
`yarn rmadmin -refreshQueues`

```bash
# 刷新队列配置
yarn rmadmin -refreshQueues
```

---

**基本写法：刷新节点**
`yarn rmadmin -refreshNodes`

```bash
# 刷新节点列表（用于节点上线/下线）
yarn rmadmin -refreshNodes
```

---

**基本写法：刷新用户**
`yarn rmadmin -refreshUserToGroupsMappings`

```bash
# 刷新用户到组的映射
yarn rmadmin -refreshUserToGroupsMappings
```

---

**基本写法：刷新超级用户代理**
`yarn rmadmin -refreshSuperUserGroupsConfiguration`

```bash
# 刷新超级用户组配置
yarn rmadmin -refreshSuperUserGroupsConfiguration
```

---

**基本写法：更新管理员 ACL**
`yarn rmadmin -refreshAdminAcls`

```bash
# 更新管理员访问控制列表
yarn rmadmin -refreshAdminAcls
```

---

## 服务管理

**基本写法：启动 ResourceManager**
`yarn --daemon start resourcemanager`

```bash
# 启动 ResourceManager
yarn --daemon start resourcemanager
```

---

**基本写法：启动 NodeManager**
`yarn --daemon start nodemanager`

```bash
# 启动 NodeManager
yarn --daemon start nodemanager
```

---

**基本写法：停止服务**
`yarn --daemon stop <服务名>`

```bash
# 停止 ResourceManager
yarn --daemon stop resourcemanager
# 停止 NodeManager
yarn --daemon stop nodemanager
```

---

**基本写法：启动所有服务**
`start-yarn.sh`

```bash
# 启动所有 YARN 服务
start-yarn.sh
```

---

**基本写法：停止所有服务**
`stop-yarn.sh`

```bash
# 停止所有 YARN 服务
stop-yarn.sh
```

---

## 资源配置

**基本写法：查看调度器配置**
`yarn scheduler -list`

```bash
# 查看调度器信息
yarn scheduler -list
```

---

**基本写法：查看队列资源使用**
`yarn queue -status <队列名>`

```bash
# 查看 default 队列资源使用情况
yarn queue -status default
```

---

## 共享缓存

**基本写法：查看共享缓存**
`yarn sharedcachemeta -list`

```bash
# 查看共享缓存元数据
yarn sharedcachemeta -list
```

---

**基本写法：查看缓存资源**
`yarn sharedcachemeta -entry <资源键>`

```bash
# 查看指定缓存资源
yarn sharedcachemeta -entry my_resource
```

## 参考文献

Apache Spark：https://spark.apache.org/docs/latest/
Apache Flink：https://flink.apache.org/
Apache Kafka：https://kafka.apache.org/documentation/
ClickHouse：https://clickhouse.com/docs
Airflow：https://airflow.apache.org/docs/

## 延伸阅读

大数据生态概览，见 052-big-data 模块文档。
数据分析与统计，见 051-data-analysis/030-probability-statistics 模块。
分布式系统基础，见 034-cloud-computing 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供大数据课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 流处理语义深入

At-most-once：可能丢；At-least-once：可能重；Exactly-once：端到端精确一次需事务/幂等。
状态后端：RocksDB 本地状态 + checkpoint 快照；重启恢复。
窗口：滚动（固定）、滑动（重叠）、会话（空闲间隔）；触发条件（水位线 + 允许迟到）。
实践：幂等写入 + 去重键（事件 ID）兜底。

### 13.2 数据仓库建模

维度建模：事实表（度量、外键）+ 维度表（描述）；星型模型查询友好。
分层：ODS 原样、DWD 明细清洗、DWS 汇总、ADS 应用。
缓慢变化维度（SCD）：覆盖（1）、新增行（2）、新增列（3）。
建模工具：dbt 实现 ELT 与测试；血缘可视化。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 大数据概述 | 001-DataOverview | 本文的前置基础 |
| HDFS分布式文件系统 | 002-HDFSDistributedFileSystem | 本文的并列主题 |
| MapReduce | 003-MapReduce | 本文的并列主题 |
| Spark核心 | 004-SparkCore | 本文的并列主题 |
| Spark-Streaming | 005-SparkStreaming | 本文的并列主题 |
| Hive数据仓库 | 006-HiveDataWarehouse | 本文的并列主题 |
| HBase列族数据库 | 007-HBaseDatabase | 本文的并列主题 |
| Kafka消息队列 | 008-KafkaMessageQueue | 本文的并列主题 |
| Flink流处理 | 009-FlinkStreamHandling | 本文的并列主题 |
| 数据湖 | 010-DataLake | 本文的并列主题 |
| Zookeeper协调服务 | 011-Zookeeper | 本文的并列主题 |
| YARN资源管理 | 012-YARNManagement | 本文的并列主题 |
| 大数据 HDFS 命令 | 013-HDFSCommands | 本文的并列主题 |
| 大数据 YARN 命令 | 014-YARNCommands | 本文自身 |
| 大数据 Spark RDD | 015-SparkRDD | 本文的并列主题 |
| 大数据 Spark DataFrame | 016-SparkDataFrame | 本文的并列主题 |
| 大数据 Hive DDL | 017-HiveDDL | 本文的并列主题 |
| 大数据 Hive DML | 018-HiveDML | 本文的并列主题 |
| 大数据 Hive 函数 | 019-HiveFunctions | 本文的并列主题 |
| 大数据 Kafka 命令 | 020-KafkaCommands | 本文的并列主题 |
| 大数据 HBase 命令 | 021-HBaseCommands | 本文的并列主题 |
| 大数据 Flink 流处理 | 022-FlinkBasics | 本文的并列主题 |
| 大数据 Spark 优化 | 023-SparkOptimization | 本文的性能延伸 |
