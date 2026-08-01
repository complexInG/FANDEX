---
order: 130
title: 大数据 HDFS 命令
module: 052-big-data
category: '052-big-data'
difficulty: beginner
description: 大数据 HDFS 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 文件系统操作

**基本写法：查看目录内容**
`hdfs dfs -ls [<路径>]`

```bash
# 查看 HDFS 根目录
hdfs dfs -ls /
# 查看指定目录
hdfs dfs -ls /user/hadoop
```

---

**基本写法：递归查看目录**
`hdfs dfs -ls -R <路径>`

```bash
# 递归查看目录树
hdfs dfs -ls -R /user
```

---

**基本写法：查看文件内容**
`hdfs dfs -cat <文件路径>`

```bash
# 查看 HDFS 文件内容
hdfs dfs -cat /user/hadoop/input.txt
```

---

**基本写法：分页查看文件**
`hdfs dfs -cat <文件路径> | more`

```bash
# 分页查看大文件
hdfs dfs -cat /user/hadoop/large.log | more
```

---

**基本写法：查看文件末尾**
`hdfs dfs -tail <文件路径>`

```bash
# 查看文件末尾 1KB 内容
hdfs dfs -tail /user/hadoop/log.txt
```

---

## 目录操作

**基本写法：创建目录**
`hdfs dfs -mkdir <路径>`

```bash
# 创建目录
hdfs dfs -mkdir /user/hadoop/data
```

---

**基本写法：递归创建目录**
`hdfs dfs -mkdir -p <路径>`

```bash
# 递归创建多级目录
hdfs dfs -mkdir -p /user/hadoop/data/2024/01
```

---

**基本写法：删除目录**
`hdfs dfs -rm -r <路径>`

```bash
# 递归删除目录
hdfs dfs -rm -r /user/hadoop/temp
```

---

**基本写法：强制删除**
`hdfs dfs -rm -r -f <路径>`

```bash
# 强制删除（不提示确认）
hdfs dfs -rm -r -f /user/hadoop/temp
```

---

**基本写法：删除空目录**
`hdfs dfs -rmdir <路径>`

```bash
# 删除空目录
hdfs dfs -rmdir /user/hadoop/empty_dir
```

---

## 文件上传下载

**基本写法：上传文件到 HDFS**
`hdfs dfs -put <本地路径> <HDFS路径>`

```bash
# 上传本地文件到 HDFS
hdfs dfs -put localfile.txt /user/hadoop/
```

---

**基本写法：上传多个文件**
`hdfs dfs -put <文件1> <文件2> <HDFS目录>`

```bash
# 上传多个文件到 HDFS 目录
hdfs dfs -put file1.txt file2.txt /user/hadoop/data/
```

---

**基本写法：使用 copyFromLocal**
`hdfs dfs -copyFromLocal <本地路径> <HDFS路径>`

```bash
# 等同于 put，上传本地文件
hdfs dfs -copyFromLocal localfile.csv /user/hadoop/
```

---

**基本写法：下载文件**
`hdfs dfs -get <HDFS路径> <本地路径>`

```bash
# 从 HDFS 下载文件到本地
hdfs dfs -get /user/hadoop/output.txt ./
```

---

**基本写法：使用 copyToLocal**
`hdfs dfs -copyToLocal <HDFS路径> <本地路径>`

```bash
# 等同于 get，下载到本地
hdfs dfs -copyToLocal /user/hadoop/result.csv ./
```

---

**基本写法：合并下载**
`hdfs dfs -getmerge <HDFS目录> <本地文件>`

```bash
# 合并 HDFS 目录下所有文件并下载
hdfs dfs -getmerge /user/hadoop/output/ merged.txt
```

---

## 文件复制移动

**基本写法：HDFS 内复制**
`hdfs dfs -cp <源路径> <目标路径>`

```bash
# 在 HDFS 内复制文件
hdfs dfs -cp /user/hadoop/file.txt /user/hadoop/backup/
```

---

**基本写法：递归复制**
`hdfs dfs -cp -r <源目录> <目标目录>`

```bash
# 递归复制目录
hdfs dfs -cp -r /user/hadoop/data /user/hadoop/backup
```

---

**基本写法：HDFS 内移动**
`hdfs dfs -mv <源路径> <目标路径>`

```bash
# 在 HDFS 内移动或重命名
hdfs dfs -mv /user/hadoop/old.txt /user/hadoop/new.txt
```

---

## 权限管理

**基本写法：修改权限**
`hdfs dfs -chmod <权限模式> <路径>`

```bash
# 修改文件权限
hdfs dfs -chmod 755 /user/hadoop/file.txt
```

---

**基本写法：递归修改权限**
`hdfs dfs -chmod -R <权限模式> <路径>`

```bash
# 递归修改目录权限
hdfs dfs -chmod -R 750 /user/hadoop/data
```

---

**基本写法：修改所有者**
`hdfs dfs -chown <用户>:<组> <路径>`

```bash
# 修改文件所有者
hdfs dfs -chown hadoop:hadoop /user/hadoop/file.txt
```

---

**基本写法：递归修改所有者**
`hdfs dfs -chown -R <用户>:<组> <路径>`

```bash
# 递归修改目录所有者
hdfs dfs -chown -R hadoop:hadoop /user/hadoop/data
```

---

**基本写法：修改所属组**
`hdfs dfs -chgrp <组> <路径>`

```bash
# 修改文件所属组
hdfs dfs -chgrp hadoop /user/hadoop/file.txt
```

---

## 文件信息

**基本写法：查看文件大小**
`hdfs dfs -du <路径>`

```bash
# 查看目录下各文件大小
hdfs dfs -du /user/hadoop
```

---

**基本写法：查看汇总大小**
`hdfs dfs -du -s <路径>`

```bash
# 查看目录总大小
hdfs dfs -du -s /user/hadoop/data
```

---

**基本写法：人类可读格式**
`hdfs dfs -du -h <路径>`

```bash
# 以人类可读格式显示大小
hdfs dfs -du -h /user/hadoop
```

---

**基本写法：查看磁盘使用情况**
`hdfs dfs -df [<路径>]`

```bash
# 查看 HDFS 磁盘使用情况
hdfs dfs -df -h
```

---

**基本写法：统计文件数和大小**
`hdfs dfs -count <路径>`

```bash
# 统计目录下的文件数和大小
hdfs dfs -count /user/hadoop
```

---

## 文件校验

**基本写法：查看文件校验和**
`hdfs dfs -checksum <文件路径>`

```bash
# 查看 HDFS 文件的校验和
hdfs dfs -checksum /user/hadoop/file.txt
```

---

**基本写法：测试文件**
`hdfs dfs -test -[ezd] <路径>`

```bash
# 测试文件是否存在
hdfs dfs -test -e /user/hadoop/file.txt
# 测试是否为空文件
hdfs dfs -test -z /user/hadoop/file.txt
# 测试是否为目录
hdfs dfs -test -d /user/hadoop/data
```

---

## 集群管理

**基本写法：查看文件系统状态**
`hdfs fsck <路径>`

```bash
# 检查 HDFS 文件系统健康状况
hdfs fsck /
# 检查指定目录
hdfs fsck /user/hadoop -files -blocks
```

---

**基本写法：查看 NameNode 状态**
`hdfs dfsadmin -report`

```bash
# 查看 HDFS 集群报告
hdfs dfsadmin -report
```

---

**基本写法：安全模式操作**
`hdfs dfsadmin -safemode <命令>`

```bash
# 查看安全模式状态
hdfs dfsadmin -safemode get
# 进入安全模式
hdfs dfsadmin -safemode enter
# 退出安全模式
hdfs dfsadmin -safemode leave
```

---

**基本写法：刷新节点**
`hdfs dfsadmin -refreshNodes`

```bash
# 刷新 DataNode 列表（用于节点上线/下线）
hdfs dfsadmin -refreshNodes
```

---

**基本写法：设置配额**
`hdfs dfsadmin -setQuota <数量> <目录>`

```bash
# 设置目录文件数配额
hdfs dfsadmin -setQuota 1000 /user/hadoop/data
```

---

**基本写法：设置空间配额**
`hdfs dfsadmin -setSpaceQuota <大小> <目录>`

```bash
# 设置目录空间配额
hdfs dfsadmin -setSpaceQuota 1T /user/hadoop/data
```

---

## 快照管理

**基本写法：允许快照**
`hdfs dfsadmin -allowSnapshot <路径>`

```bash
# 允许目录创建快照
hdfs dfsadmin -allowSnapshot /user/hadoop/data
```

---

**基本写法：创建快照**
`hdfs dfs -createSnapshot <路径> [<快照名>]`

```bash
# 创建快照
hdfs dfs -createSnapshot /user/hadoop/data snapshot_20240101
```

---

**基本写法：删除快照**
`hdfs dfs -deleteSnapshot <路径> <快照名>`

```bash
# 删除快照
hdfs dfs -deleteSnapshot /user/hadoop/data snapshot_20240101
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
| 大数据 HDFS 命令 | 013-HDFSCommands | 本文自身 |
| 大数据 YARN 命令 | 014-YARNCommands | 本文的并列主题 |
| 大数据 Spark RDD | 015-SparkRDD | 本文的并列主题 |
| 大数据 Spark DataFrame | 016-SparkDataFrame | 本文的并列主题 |
| 大数据 Hive DDL | 017-HiveDDL | 本文的并列主题 |
| 大数据 Hive DML | 018-HiveDML | 本文的并列主题 |
| 大数据 Hive 函数 | 019-HiveFunctions | 本文的并列主题 |
| 大数据 Kafka 命令 | 020-KafkaCommands | 本文的并列主题 |
| 大数据 HBase 命令 | 021-HBaseCommands | 本文的并列主题 |
| 大数据 Flink 流处理 | 022-FlinkBasics | 本文的并列主题 |
| 大数据 Spark 优化 | 023-SparkOptimization | 本文的性能延伸 |
