---
order: 150
title: 大数据 Spark RDD
module: 052-big-data
category: '052-big-data'
difficulty: beginner
description: 大数据 Spark RDD 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 大数据 Spark RDD

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 SparkContext

**换行写法：初始化 SparkContext**
`from pyspark import SparkContext, SparkConf`
`conf = SparkConf().setAppName(<应用名>).setMaster(<模式>)`
`sc = SparkContext(conf=conf)`

```python
# 初始化 SparkContext
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("MyApp").setMaster("local[*]")
sc = SparkContext(conf=conf)
```

---

**基本写法：创建 SparkContext**
`SparkContext(<配置>)`

```python
# 使用默认配置创建
sc = SparkContext("local[*]", "MyApp")
```

---

## 创建 RDD

**基本写法：从集合创建 RDD**
`sc.parallelize(<集合>, [<分区数>])`

```python
# 从 Python 列表创建 RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
# 指定分区数
rdd = sc.parallelize([1, 2, 3, 4, 5], numSlices=3)
```

---

**基本写法：从文件创建 RDD**
`sc.textFile(<路径>, [<分区数>])`

```python
# 从文本文件创建 RDD
rdd = sc.textFile("hdfs://namenode:8020/input/data.txt")
# 指定最小分区数
rdd = sc.textFile("data.txt", minPartitions=4)
```

---

**基本写法：从多个文件创建**
`sc.textFile(<路径模式>)`

```python
# 从多个文件创建 RDD
rdd = sc.textFile("hdfs://namenode:8020/input/*.txt")
```

---

**基本写法：从整个目录创建**
`sc.wholeTextFiles(<路径>)`

```python
# 读取整个目录（返回 (文件名, 内容) 对）
rdd = sc.wholeTextFiles("hdfs://namenode:8020/input/")
```

---

**基本写法：创建空 RDD**
`sc.emptyRDD()`

```python
# 创建空 RDD
empty_rdd = sc.emptyRDD()
```

---

**基本写法：使用 range 创建**
`sc.range(<开始>, <结束>, [<步长>])`

```python
# 创建范围 RDD
rdd = sc.range(0, 100, step=1)
```

---

## 转换操作

**基本写法：map 转换**
`<rdd>.map(<函数>)`

```python
# 对每个元素应用函数
squared = rdd.map(lambda x: x ** 2)
```

---

**基本写法：flatMap 转换**
`<rdd>.flatMap(<函数>)`

```python
# 对每个元素应用函数并展平结果
words = rdd.flatMap(lambda line: line.split(" "))
```

---

**基本写法：filter 过滤**
`<rdd>.filter(<函数>)`

```python
# 过滤元素
even = rdd.filter(lambda x: x % 2 == 0)
```

---

**基本写法：distinct 去重**
`<rdd>.distinct([<分区数>])`

```python
# 去除重复元素
unique = rdd.distinct()
```

---

**基本写法：sample 采样**
`<rdd>.sample(<是否放回>, <比例>, [<种子>])`

```python
# 随机采样
sampled = rdd.sample(False, 0.1, seed=42)
```

---

**基本写法：union 合并**
`<rdd1>.union(<rdd2>)`

```python
# 合并两个 RDD
combined = rdd1.union(rdd2)
```

---

**基本写法：intersection 交集**
`<rdd1>.intersection(<rdd2>)`

```python
# 求两个 RDD 的交集
common = rdd1.intersection(rdd2)
```

---

**基本写法：subtract 差集**
`<rdd1>.subtract(<rdd2>)`

```python
# 求两个 RDD 的差集
diff = rdd1.subtract(rdd2)
```

---

**基本写法：sortBy 排序**
`<rdd>.sortBy(<函数>, ascending=<布尔值>, [<分区数>])`

```python
# 排序
sorted_rdd = rdd.sortBy(lambda x: x, ascending=False)
```

---

## 键值对操作

**基本写法：创建键值对 RDD**
`<rdd>.map(<函数>)`

```python
# 创建键值对 RDD
pairs = rdd.map(lambda x: (x, 1))
```

---

**基本写法：reduceByKey 聚合**
`<rdd>.reduceByKey(<函数>)`

```python
# 按键聚合
reduced = pairs.reduceByKey(lambda a, b: a + b)
```

---

**基本写法：groupByKey 分组**
`<rdd>.groupByKey()`

```python
# 按键分组
grouped = pairs.groupByKey()
```

---

**基本写法：sortByKey 按键排序**
`<rdd>.sortByKey(ascending=<布尔值>)`

```python
# 按键排序
sorted_pairs = pairs.sortByKey(ascending=True)
```

---

**基本写法：mapValues 对值操作**
`<rdd>.mapValues(<函数>)`

```python
# 对值应用函数（键不变）
result = pairs.mapValues(lambda x: x * 2)
```

---

**基本写法：flatMapValues 展平值**
`<rdd>.flatMapValues(<函数>)`

```python
# 对值应用函数并展平
result = pairs.flatMapValues(lambda x: range(x))
```

---

**基本写法：keys 获取所有键**
`<rdd>.keys()`

```python
# 获取所有键
all_keys = pairs.keys()
```

---

**基本写法：values 获取所有值**
`<rdd>.values()`

```python
# 获取所有值
all_values = pairs.values()
```

---

## Join 操作

**基本写法：join 内连接**
`<rdd1>.join(<rdd2>)`

```python
# 内连接
joined = rdd1.join(rdd2)
```

---

**基本写法：leftOuterJoin 左连接**
`<rdd1>.leftOuterJoin(<rdd2>)`

```python
# 左外连接
joined = rdd1.leftOuterJoin(rdd2)
```

---

**基本写法：rightOuterJoin 右连接**
`<rdd1>.rightOuterJoin(<rdd2>)`

```python
# 右外连接
joined = rdd1.rightOuterJoin(rdd2)
```

---

**基本写法：fullOuterJoin 全连接**
`<rdd1>.fullOuterJoin(<rdd2>)`

```python
# 全外连接
joined = rdd1.fullOuterJoin(rdd2)
```

---

**基本写法：cogroup 分组连接**
`<rdd1>.cogroup(<rdd2>)`

```python
# 分组连接（返回值的迭代器）
grouped = rdd1.cogroup(rdd2)
```

---

## 行动操作

**基本写法：collect 收集**
`<rdd>.collect()`

```python
# 收集所有元素到驱动程序
result = rdd.collect()
```

---

**基本写法：count 计数**
`<rdd>.count()`

```python
# 统计元素个数
count = rdd.count()
```

---

**基本写法：first 取第一个**
`<rdd>.first()`

```python
# 获取第一个元素
first_elem = rdd.first()
```

---

**基本写法：take 取前 N 个**
`<rdd>.take(<n>)`

```python
# 取前 5 个元素
top_5 = rdd.take(5)
```

---

**基本写法：takeOrdered 取排序后前 N 个**
`<rdd>.takeOrdered(<n>, key=<函数>)`

```python
# 取最小的 5 个元素
smallest = rdd.takeOrdered(5)
# 取最大的 5 个元素
largest = rdd.takeOrdered(5, key=lambda x: -x)
```

---

**基本写法：top 取最大的 N 个**
`<rdd>.top(<n>, key=<函数>)`

```python
# 取最大的 5 个元素
top_5 = rdd.top(5)
```

---

**基本写法：reduce 聚合**
`<rdd>.reduce(<函数>)`

```python
# 聚合所有元素
total = rdd.reduce(lambda a, b: a + b)
```

---

**基本写法：fold 聚合（带初始值）**
`<rdd>.fold(<初始值>, <函数>)`

```python
# 带初始值的聚合
total = rdd.fold(0, lambda a, b: a + b)
```

---

**基本写法：aggregate 聚合**
`<rdd>.aggregate(<初始值>, <seqOp>, <combOp>)`

```python
# 复杂聚合（同时求和与计数）
sum_count = rdd.aggregate(
    (0, 0),
    lambda acc, x: (acc[0] + x, acc[1] + 1),
    lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])
)
```

---

**基本写法：countByKey 按键计数**
`<rdd>.countByKey()`

```python
# 统计每个键的数量
counts = pairs.countByKey()
```

---

**基本写法：countByValue 按值计数**
`<rdd>.countByValue()`

```python
# 统计每个值的出现次数
counts = rdd.countByValue()
```

---

**基本写法：foreach 遍历**
`<rdd>.foreach(<函数>)`

```python
# 对每个元素应用函数
rdd.foreach(lambda x: print(x))
```

---

## 持久化操作

**基本写法：缓存 RDD**
`<rdd>.cache()`

```python
# 缓存 RDD（默认 MEMORY_ONLY）
rdd.cache()
```

---

**基本写法：持久化 RDD**
`<rdd>.persist(<存储级别>)`

```python
# 指定存储级别持久化
from pyspark import StorageLevel
rdd.persist(StorageLevel.MEMORY_AND_DISK)
```

---

**基本写法：解除持久化**
`<rdd>.unpersist()`

```python
# 解除 RDD 持久化
rdd.unpersist()
```

---

## 分区操作

**基本写法：获取分区数**
`<rdd>.getNumPartitions()`

```python
# 查看 RDD 分区数
num = rdd.getNumPartitions()
```

---

**基本写法：重新分区**
`<rdd>.repartition(<分区数>)`

```python
# 重新分区（会产生 Shuffle）
rdd = rdd.repartition(10)
```

---

**基本写法：减少分区**
`<rdd>.coalesce(<分区数>)`

```python
# 减少分区数（默认不产生 Shuffle）
rdd = rdd.coalesce(2)
```

---

**基本写法：减少分区（触发 Shuffle）**
`<rdd>.coalesce(<分区数>, shuffle=True)`

```python
# 减少分区并触发 Shuffle
rdd = rdd.coalesce(2, shuffle=True)
```

---

**基本写法：查看分区内容**
`<rdd>.glom()`

```python
# 查看每个分区的元素
partitions = rdd.glom().collect()
```

---

**基本写法：分区内操作**
`<rdd>.mapPartitions(<函数>)`

```python
# 对每个分区应用函数
result = rdd.mapPartitions(lambda iter: [sum(iter)])
```

---

## 保存操作

**基本写法：保存为文本文件**
`<rdd>.saveAsTextFile(<路径>)`

```python
# 保存 RDD 为文本文件
rdd.saveAsTextFile("hdfs://namenode:8020/output/")
```

---

**基本写法：保存为 SequenceFile**
`<rdd>.saveAsSequenceFile(<路径>)`

```python
# 保存为 Hadoop SequenceFile
rdd.saveAsSequenceFile("hdfs://namenode:8020/output/")
```

---

**基本写法：保存为对象文件**
`<rdd>.saveAsObjectFile(<路径>)`

```python
# 保存为对象文件
rdd.saveAsObjectFile("hdfs://namenode:8020/output/")
```

---

## 广播变量与累加器

**基本写法：创建广播变量**
`sc.broadcast(<值>)`

```python
# 创建广播变量
broadcast_var = sc.broadcast({"key": "value"})
# 在 RDD 操作中使用
rdd.map(lambda x: broadcast_var.value["key"])
```

---

**基本写法：创建累加器**
`sc.accumulator(<初始值>)`

```python
# 创建累加器
acc = sc.accumulator(0)
# 在 RDD 操作中累加
rdd.foreach(lambda x: acc.add(1))
print(acc.value)
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
| 大数据 Spark RDD | 015-SparkRDD | 本文自身 |
| 大数据 Spark DataFrame | 016-SparkDataFrame | 本文的并列主题 |
| 大数据 Hive DDL | 017-HiveDDL | 本文的并列主题 |
| 大数据 Hive DML | 018-HiveDML | 本文的并列主题 |
| 大数据 Hive 函数 | 019-HiveFunctions | 本文的并列主题 |
| 大数据 Kafka 命令 | 020-KafkaCommands | 本文的并列主题 |
| 大数据 HBase 命令 | 021-HBaseCommands | 本文的并列主题 |
| 大数据 Flink 流处理 | 022-FlinkBasics | 本文的并列主题 |
| 大数据 Spark 优化 | 023-SparkOptimization | 本文的性能延伸 |
