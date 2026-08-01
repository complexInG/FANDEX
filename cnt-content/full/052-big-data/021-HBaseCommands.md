---
order: 210
title: 大数据 HBase 命令
module: big-data

category: '052-big-data'
difficulty: beginner
description: 大数据 HBase 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 进入 Shell

**基本写法：启动 HBase Shell**
`hbase shell`

```bash
# 启动 HBase 交互式 Shell
hbase shell
```

---

**基本写法：执行单条命令**
`echo "<命令>" | hbase shell`

```bash
# 执行单条命令后退出
echo "list" | hbase shell
```

---

**基本写法：执行脚本**
`hbase shell <脚本文件>`

```bash
# 执行 HBase Shell 脚本
hbase shell commands.txt
```

---

## 命名空间操作

**基本写法：创建命名空间**
`create_namespace '<命名空间>'`

```bash
# 创建命名空间
create_namespace 'my_ns'
```

---

**基本写法：带属性创建**
`create_namespace '<命名空间>', <属性>`

```bash
# 带属性创建命名空间
create_namespace 'my_ns', {'creator' => 'admin'}
```

---

**基本写法：查看命名空间**
`list_namespace`

```bash
# 查看所有命名空间
list_namespace
```

---

**基本写法：查看命名空间下的表**
`list_namespace_tables '<命名空间>'`

```bash
# 查看命名空间下的表
list_namespace_tables 'my_ns'
```

---

**基本写法：删除命名空间**
`drop_namespace '<命名空间>'`

```bash
# 删除空命名空间
drop_namespace 'my_ns'
```

---

## 表操作

**基本写法：创建表**
`create '<表名>', '<列族1>', '<列族2>'`

```bash
# 创建表（指定列族）
create 'users', 'info', 'detail'
```

---

**基本写法：指定版本数创建**
`create '<表名>', {NAME => '<列族>', VERSIONS => <n>}`

```bash
# 指定版本数
create 'users', {NAME => 'info', VERSIONS => 3}
```

---

**基本写法：带多属性创建**
`create '<表名>', {NAME => '<列族>', VERSIONS => <n>, TTL => <秒>}`

```bash
# 带多属性创建表
create 'users', {NAME => 'info', VERSIONS => 3, TTL => 86400}
```

---

**基本写法：查看表列表**
`list`

```bash
# 查看所有表
list
```

---

**基本写法：查看表详情**
`describe '<表名>'`

```bash
# 查看表结构
describe 'users'
```

---

**基本写法：禁用表**
`disable '<表名>'`

```bash
# 禁用表（修改或删除前需要）
disable 'users'
```

---

**基本写法：启用表**
`enable '<表名>'`

```bash
# 启用表
enable 'users'
```

---

**基本写法：查看表状态**
`is_disabled '<表名>'`

```bash
# 查看表是否被禁用
is_disabled 'users'
```

---

**基本写法：删除表**
`drop '<表名>'`

```bash
# 删除表（需先禁用）
disable 'users'
drop 'users'
```

---

**基本写法：删除命名空间表**
`drop '<命名空间>:<表名>'`

```bash
# 删除命名空间下的表
disable 'my_ns:users'
drop 'my_ns:users'
```

---

**基本写法：修改表结构**
`alter '<表名>', <修改内容>`

```bash
# 修改列族属性
alter 'users', {NAME => 'info', VERSIONS => 5}
```

---

**基本写法：添加列族**
`alter '<表名>', '<新列族>'`

```bash
# 添加新列族
alter 'users', 'contact'
```

---

**基本写法：删除列族**
`alter '<表名>', 'delete' => '<列族>'`

```bash
# 删除列族
alter 'users', 'delete' => 'detail'
```

---

## 数据写入

**基本写法：写入单行数据**
`put '<表名>', '<行键>', '<列族>:<列名>', '<值>'`

```bash
# 写入数据
put 'users', 'user1', 'info:name', 'Alice'
put 'users', 'user1', 'info:age', '25'
put 'users', 'user1', 'detail:city', 'Beijing'
```

---

**基本写法：写入带时间戳**
`put '<表名>', '<行键>', '<列族>:<列名>', '<值>', <时间戳>`

```bash
# 写入带时间戳的数据
put 'users', 'user1', 'info:name', 'Alice', 1705286400000
```

---

**基本写法：检查并写入**
`checkAndPut '<表名>', '<行键>', '<列族>:<列名>', '<期望值>', '<列族>:<列名>', '<新值>'`

```bash
# 条件写入（当 name 为 Alice 时更新）
checkAndPut 'users', 'user1', 'info:name', 'Alice', 'info:age', '26'
```

---

## 数据查询

**基本写法：查询单行**
`get '<表名>', '<行键>'`

```bash
# 查询单行数据
get 'users', 'user1'
```

---

**基本写法：查询指定列**
`get '<表名>', '<行键>', '<列族>:<列名>'`

```bash
# 查询指定列
get 'users', 'user1', 'info:name'
```

---

**基本写法：查询多个列**
`get '<表名>', '<行键>', {COLUMN => ['<列族1>:<列1>', '<列族2>:<列2>']}`

```bash
# 查询多个列
get 'users', 'user1', {COLUMN => ['info:name', 'detail:city']}
```

---

**基本写法：查询历史版本**
`get '<表名>', '<行键>', {COLUMN => '<列族>:<列名>', VERSIONS => <n>}`

```bash
# 查询历史版本
get 'users', 'user1', {COLUMN => 'info:name', VERSIONS => 3}
```

---

**基本写法：扫描全表**
`scan '<表名>'`

```bash
# 扫描全表
scan 'users'
```

---

**基本写法：限制扫描行数**
`scan '<表名>', {LIMIT => <n>}`

```bash
# 限制扫描行数
scan 'users', {LIMIT => 10}
```

---

**基本写法：扫描指定列**
`scan '<表名>', {COLUMN => '<列族>:<列名>'}`

```bash
# 扫描指定列
scan 'users', {COLUMN => 'info:name'}
```

---

**基本写法：范围扫描**
`scan '<表名>', {STARTROW => '<开始行键>', STOPROW => '<结束行键>'}`

```bash
# 范围扫描
scan 'users', {STARTROW => 'user1', STOPROW => 'user5'}
```

---

**基本写法：前缀过滤扫描**
`scan '<表名>', {ROWPREFIXFILTER => '<前缀>'}`

```bash
# 按行键前缀扫描
scan 'users', {ROWPREFIXFILTER => 'user'}
```

---

**基本写法：过滤器扫描**
`scan '<表名>', {FILTER => "ValueFilter(=, 'binary:<值>')"}`

```bash
# 使用过滤器扫描
scan 'users', {FILTER => "ValueFilter(=, 'binary:Alice')"}
```

---

**基本写法：单列值过滤器**
`scan '<表名>', {FILTER => "SingleColumnValueFilter('<列族>', '<列名>', =, 'binary:<值>')"}`

```bash
# 单列值过滤
scan 'users', {FILTER => "SingleColumnValueFilter('info', 'age', =, 'binary:25')"}
```

---

**基本写法：计数**
`count '<表名>'`

```bash
# 统计表行数
count 'users'
```

---

**基本写法：分批计数**
`count '<表名>', <间隔>`

```bash
# 每 1000 行显示一次进度
count 'users', 1000
```

---

## 数据删除

**基本写法：删除单元格**
`delete '<表名>', '<行键>', '<列族>:<列名>'`

```bash
# 删除指定单元格
delete 'users', 'user1', 'info:age'
```

---

**基本写法：删除指定版本**
`delete '<表名>', '<行键>', '<列族>:<列名>', <时间戳>`

```bash
# 删除指定版本
delete 'users', 'user1', 'info:name', 1705286400000
```

---

**基本写法：删除整行**
`deleteall '<表名>', '<行键>'`

```bash
# 删除整行数据
deleteall 'users', 'user1'
```

---

**基本写法：清空表**
`truncate '<表名>'`

```bash
# 清空表（保留结构）
truncate 'users'
```

---

**基本写法：保留分区清空**
`truncate_preserve '<表名>'`

```bash
# 清空表但保留分区
truncate_preserve 'users'
```

---

## 快照操作

**基本写法：创建快照**
`snapshot '<表名>', '<快照名>'`

```bash
# 创建表快照
snapshot 'users', 'users_snapshot_20240101'
```

---

**基本写法：查看快照列表**
`list_snapshots`

```bash
# 查看所有快照
list_snapshots
```

---

**基本写法：从快照恢复**
`restore_snapshot '<快照名>'`

```bash
# 从快照恢复表
restore_snapshot 'users_snapshot_20240101'
```

---

**基本写法：从快照克隆表**
`clone_snapshot '<快照名>', '<新表名>'`

```bash
# 从快照克隆新表
clone_snapshot 'users_snapshot_20240101', 'users_clone'
```

---

**基本写法：删除快照**
`delete_snapshot '<快照名>'`

```bash
# 删除快照
delete_snapshot 'users_snapshot_20240101'
```

---

## 集群管理

**基本写法：查看集群状态**
`status`

```bash
# 查看集群状态
status
# 简洁模式
status 'simple'
```

---

**基本写法：查看版本**
`version`

```bash
# 查看 HBase 版本
version
```

---

**基本写法：查看进程**
`whoami`

```bash
# 查看当前用户
whoami
```

---

**基本写法：查看表区域**
`list_regions '<表名>'`

```bash
# 查看表的 Region 信息
list_regions 'users'
```

---

**基本写法：查看 ZK 状态**
`zk_dump`

```bash
# 查看 ZooKeeper 状态
zk_dump
```

---

## 命令行工具

**基本写法：创建表（命令行）**
`hbase create '<表名>', '<列族>'`

```bash
# 使用 hbase 命令直接创建表
echo "create 'test', 'cf'" | hbase shell -n
```

---

**基本写法：查看 HBase 状态**
`hbase hbck`

```bash
# 检查 HBase 一致性
hbase hbck
```

---

**基本写法：修复 HBase**
`hbase hbck -fix`

```bash
# 修复 HBase 不一致问题
hbase hbck -fix
```

---

**基本写法：导出表**
`hbase org.apache.hadoop.hbase.mapreduce.Export '<表名>' '<HDFS路径>'`

```bash
# 导出表到 HDFS
hbase org.apache.hadoop.hbase.mapreduce.Export 'users' '/backup/users'
```

---

**基本写法：导入表**
`hbase org.apache.hadoop.hbase.mapreduce.Import '<表名>' '<HDFS路径>'`

```bash
# 从 HDFS 导入表数据
hbase org.apache.hadoop.hbase.mapreduce.Import 'users' '/backup/users'
```

---

**基本写法：RowCounter**
`hbase org.apache.hadoop.hbase.mapreduce.RowCounter '<表名>'`

```bash
# 使用 MapReduce 统计行数
hbase org.apache.hadoop.hbase.mapreduce.RowCounter 'users'
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
| 大数据 HDFS 命令 | 013-HDFSCommands | 本文的并列主题 |
| 大数据 YARN 命令 | 014-YARNCommands | 本文的并列主题 |
| 大数据 Spark RDD | 015-SparkRDD | 本文的并列主题 |
| 大数据 Spark DataFrame | 016-SparkDataFrame | 本文的并列主题 |
| 大数据 Hive DDL | 017-HiveDDL | 本文的并列主题 |
| 大数据 Hive DML | 018-HiveDML | 本文的并列主题 |
| 大数据 Hive 函数 | 019-HiveFunctions | 本文的并列主题 |
| 大数据 Kafka 命令 | 020-KafkaCommands | 本文的并列主题 |
| 大数据 HBase 命令 | 021-HBaseCommands | 本文自身 |
| 大数据 Flink 流处理 | 022-FlinkBasics | 本文的并列主题 |
| 大数据 Spark 优化 | 023-SparkOptimization | 本文的性能延伸 |
