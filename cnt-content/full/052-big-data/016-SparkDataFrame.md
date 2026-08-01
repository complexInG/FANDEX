---
order: 160
title: 大数据 Spark DataFrame
module: 052-big-data
category: '052-big-data'
difficulty: beginner
description: 大数据 Spark DataFrame 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 创建 SparkSession

**换行写法：初始化 SparkSession**
`from pyspark.sql import SparkSession`
`spark = SparkSession.builder.appName(<应用名>).getOrCreate()`

```python
# 初始化 SparkSession
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .master("local[*]") \
    .getOrCreate()
```

---

**基本写法：启用 Hive 支持**
`SparkSession.builder.enableHiveSupport().getOrCreate()`

```python
# 启用 Hive 支持
spark = SparkSession.builder \
    .appName("HiveApp") \
    .enableHiveSupport() \
    .getOrCreate()
```

---

**基本写法：获取 SparkContext**
`spark.sparkContext`

```python
# 从 SparkSession 获取 SparkContext
sc = spark.sparkContext
```

---

## 创建 DataFrame

**基本写法：从 RDD 创建**
`spark.createDataFrame(<rdd>, [<schema>])`

```python
# 从 RDD 创建 DataFrame
rdd = sc.parallelize([("Alice", 30), ("Bob", 25)])
df = spark.createDataFrame(rdd, ["name", "age"])
```

---

**基本写法：从列表创建**
`spark.createDataFrame(<数据>, [<列名>])`

```python
# 从列表创建 DataFrame
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
df = spark.createDataFrame(data, ["name", "age"])
```

---

**基本写法：从字典列表创建**
`spark.createDataFrame(<字典列表>)`

```python
# 从字典列表创建 DataFrame
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
df = spark.createDataFrame(data)
```

---

**基本写法：从 Pandas DataFrame 创建**
`spark.createDataFrame(<pandas_df>)`

```python
# 从 Pandas DataFrame 创建 Spark DataFrame
import pandas as pd
pdf = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
df = spark.createDataFrame(pdf)
```

---

**基本写法：读取 JSON 文件**
`spark.read.json(<路径>)`

```python
# 读取 JSON 文件
df = spark.read.json("hdfs://namenode:8020/data.json")
```

---

**基本写法：读取 CSV 文件**
`spark.read.csv(<路径>, header=<布尔值>, inferSchema=<布尔值>)`

```python
# 读取 CSV 文件
df = spark.read.csv("data.csv", header=True, inferSchema=True)
```

---

**基本写法：读取 Parquet 文件**
`spark.read.parquet(<路径>)`

```python
# 读取 Parquet 文件
df = spark.read.parquet("hdfs://namenode:8020/data.parquet")
```

---

**基本写法：读取 ORC 文件**
`spark.read.orc(<路径>)`

```python
# 读取 ORC 文件
df = spark.read.orc("hdfs://namenode:8020/data.orc")
```

---

**基本写法：读取 Hive 表**
`spark.read.table(<表名>)`

```python
# 读取 Hive 表
df = spark.read.table("my_database.my_table")
```

---

**基本写法：读取 JDBC 数据源**
`spark.read.jdbc(<url>, <表名>, properties=<属性>)`

```python
# 从 MySQL 读取数据
df = spark.read.jdbc(
    url="jdbc:mysql://localhost:3306/db",
    table="users",
    properties={"user": "root", "password": "123456"}
)
```

---

## 查看数据

**基本写法：查看 Schema**
`<df>.printSchema()`

```python
# 打印 DataFrame 的 Schema
df.printSchema()
```

---

**基本写法：查看前几行**
`<df>.show([<行数>])`

```python
# 显示前 20 行
df.show()
# 显示前 5 行
df.show(5)
```

---

**基本写法：截断显示**
`<df>.show(truncate=False)`

```python
# 显示完整内容（不截断长字符串）
df.show(truncate=False)
```

---

**基本写法：查看列名**
`<df>.columns`

```python
# 获取所有列名
print(df.columns)
```

---

**基本写法：查看数据类型**
`<df>.dtypes`

```python
# 获取列名和类型
print(df.dtypes)
```

---

**基本写法：转换为 Pandas**
`<df>.toPandas()`

```python
# 转换为 Pandas DataFrame
pdf = df.toPandas()
```

---

## 选择与过滤

**基本写法：选择列**
`<df>.select(<列1>, <列2>)`

```python
# 选择指定列
df.select("name", "age").show()
```

---

**基本写法：选择并重命名**
`<df>.select(<列>.alias(<新名>))`

```python
# 选择列并重命名
df.select(df["name"].alias("username")).show()
```

---

**基本写法：使用表达式**
`<df>.selectExpr(<表达式>)`

```python
# 使用 SQL 表达式
df.selectExpr("name", "age + 1 as next_age").show()
```

---

**基本写法：过滤数据**
`<df>.filter(<条件>)`

```python
# 过滤数据
df.filter(df["age"] > 25).show()
```

---

**基本写法：使用 SQL 字符串过滤**
`<df>.filter("<SQL条件>")`

```python
# 使用 SQL 字符串过滤
df.filter("age > 25").show()
```

---

**基本写法：多条件过滤**
`<df>.filter((<条件1>) & (<条件2>))`

```python
# 多条件过滤
df.filter((df["age"] > 25) & (df["city"] == "北京")).show()
```

---

**基本写法：去重**
`<df>.distinct()`

```python
# 整行去重
df.distinct().show()
```

---

**基本写法：按列去重**
`<df>.dropDuplicates([<列名>])`

```python
# 按指定列去重
df.dropDuplicates(["name"]).show()
```

---

## 列操作

**基本写法：添加列**
`<df>.withColumn(<列名>, <表达式>)`

```python
# 添加新列
df = df.withColumn("age_plus_1", df["age"] + 1)
```

---

**基本写法：重命名列**
`<df>.withColumnRenamed(<旧名>, <新名>)`

```python
# 重命名列
df = df.withColumnRenamed("name", "username")
```

---

**基本写法：删除列**
`<df>.drop(<列名>)`

```python
# 删除列
df = df.drop("age_plus_1")
```

---

**基本写法：使用函数操作列**
`from pyspark.sql import functions as F`
`<df>.withColumn(<列名>, F.<函数>(<列>))`

```python
# 使用内置函数
from pyspark.sql import functions as F

df = df.withColumn("upper_name", F.upper(df["name"]))
df = df.withColumn("birth_year", F.year(F.current_date()) - df["age"])
```

---

## 聚合操作

**基本写法：分组聚合**
`<df>.groupBy(<列>).agg(<聚合函数>)`

```python
# 分组聚合
from pyspark.sql import functions as F

df.groupBy("city").agg(
    F.avg("salary").alias("avg_salary"),
    F.count("*").alias("count")
).show()
```

---

**基本写法：单列聚合**
`<df>.groupBy(<列>).<聚合函数>(<值列>)`

```python
# 单列聚合
df.groupBy("city").avg("salary").show()
df.groupBy("city").count().show()
df.groupBy("city").max("salary").show()
```

---

**基本写法：多列分组**
`<df>.groupBy(<列1>, <列2>).agg(<聚合函数>)`

```python
# 多列分组
df.groupBy("city", "department").agg(
    F.sum("salary").alias("total_salary")
).show()
```

---

**基本写法：全表聚合**
`<df>.agg(<聚合函数>)`

```python
# 全表聚合
df.agg(
    F.avg("salary").alias("avg_salary"),
    F.max("age").alias("max_age")
).show()
```

---

**基本写法：pivot 透视**
`<df>.groupBy(<行列>).pivot(<列>).agg(<聚合函数>)`

```python
# 透视表
df.groupBy("city").pivot("year").sum("sales").show()
```

---

## Join 操作

**基本写法：内连接**
`<df1>.join(<df2>, on=<连接列>, how="inner")`

```python
# 内连接
result = df1.join(df2, on="id", how="inner")
```

---

**基本写法：左连接**
`<df1>.join(<df2>, on=<连接列>, how="left")`

```python
# 左外连接
result = df1.join(df2, on="id", how="left")
```

---

**基本写法：右连接**
`<df1>.join(<df2>, on=<连接列>, how="right")`

```python
# 右外连接
result = df1.join(df2, on="id", how="right")
```

---

**基本写法：全外连接**
`<df1>.join(<df2>, on=<连接列>, how="outer")`

```python
# 全外连接
result = df1.join(df2, on="id", how="outer")
```

---

**基本写法：使用不同列名连接**
`<df1>.join(<df2>, <df1>[<列1>] == <df2>[<列2>])`

```python
# 不同列名连接
result = df1.join(df2, df1["user_id"] == df2["id"])
```

---

**基本写法：多列连接**
`<df1>.join(<df2>, on=[<列1>, <列2>])`

```python
# 多列连接
result = df1.join(df2, on=["city", "year"])
```

---

## 排序

**基本写法：按列排序**
`<df>.orderBy(<列>)`

```python
# 升序排序
df.orderBy("age").show()
# 降序排序
df.orderBy(df["age"].desc()).show()
```

---

**基本写法：多列排序**
`<df>.orderBy(<列1>, <列2>)`

```python
# 多列排序
df.orderBy("city", df["age"].desc()).show()
```

---

**基本写法：使用 sort**
`<df>.sort(<列>)`

```python
# 使用 sort 方法
df.sort(df["salary"].desc()).show()
```

---

## 窗口函数

**换行写法：定义窗口**
`from pyspark.sql.window import Window`
`window = Window.partitionBy(<分组列>).orderBy(<排序列>)`

```python
# 定义窗口
from pyspark.sql.window import Window

window = Window.partitionBy("city").orderBy(F.desc("salary"))
```

---

**基本写法：行号**
`F.row_number().over(<窗口>)`

```python
# 为每行编号
df = df.withColumn("rank", F.row_number().over(window))
```

---

**基本写法：排名**
`F.rank().over(<窗口>)`

```python
# 排名（有并列）
df = df.withColumn("rank", F.rank().over(window))
```

---

**基本写法：密集排名**
`F.dense_rank().over(<窗口>)`

```python
# 密集排名（无间隔）
df = df.withColumn("rank", F.dense_rank().over(window))
```

---

**基本写法：累积聚合**
`F.sum(<列>).over(<窗口>)`

```python
# 累积求和
df = df.withColumn("cumsum", F.sum("salary").over(window))
```

---

**基本写法：前 N 行**
`F.lead(<列>, <偏移>).over(<窗口>)`

```python
# 获取下一条记录
df = df.withColumn("next_salary", F.lead("salary", 1).over(window))
```

---

**基本写法：前一行**
`F.lag(<列>, <偏移>).over(<窗口>)`

```python
# 获取上一条记录
df = df.withColumn("prev_salary", F.lag("salary", 1).over(window))
```

---

## 保存数据

**基本写法：保存为 Parquet**
`<df>.write.parquet(<路径>)`

```python
# 保存为 Parquet 文件
df.write.parquet("hdfs://namenode:8020/output/")
```

---

**基本写法：保存为 CSV**
`<df>.write.csv(<路径>, header=<布尔值>)`

```python
# 保存为 CSV 文件
df.write.csv("output/", header=True)
```

---

**基本写法：保存为 JSON**
`<df>.write.json(<路径>)`

```python
# 保存为 JSON 文件
df.write.json("output/")
```

---

**基本写法：覆盖写入**
`<df>.write.mode("overwrite").<格式>(<路径>)`

```python
# 覆盖写入
df.write.mode("overwrite").parquet("output/")
```

---

**基本写法：追加写入**
`<df>.write.mode("append").<格式>(<路径>)`

```python
# 追加写入
df.write.mode("append").parquet("output/")
```

---

**基本写法：保存为 Hive 表**
`<df>.write.saveAsTable(<表名>)`

```python
# 保存为 Hive 表
df.write.saveAsTable("my_database.my_table")
```

---

**基本写法：写入 JDBC**
`<df>.write.jdbc(<url>, <表名>, properties=<属性>)`

```python
# 写入 MySQL
df.write.jdbc(
    url="jdbc:mysql://localhost:3306/db",
    table="users",
    mode="overwrite",
    properties={"user": "root", "password": "123456"}
)
```

---

## SQL 查询

**基本写法：注册临时视图**
`<df>.createOrReplaceTempView(<视图名>)`

```python
# 注册临时视图
df.createOrReplaceTempView("people")
```

---

**基本写法：执行 SQL 查询**
`spark.sql(<SQL语句>)`

```python
# 执行 SQL 查询
result = spark.sql("SELECT city, AVG(salary) FROM people GROUP BY city")
result.show()
```

---

**基本写法：注册全局视图**
`<df>.createGlobalTempView(<视图名>)`

```python
# 注册全局临时视图
df.createGlobalTempView("global_people")
result = spark.sql("SELECT * FROM global_temp.global_people")
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
| 大数据 Spark DataFrame | 016-SparkDataFrame | 本文自身 |
| 大数据 Hive DDL | 017-HiveDDL | 本文的并列主题 |
| 大数据 Hive DML | 018-HiveDML | 本文的并列主题 |
| 大数据 Hive 函数 | 019-HiveFunctions | 本文的并列主题 |
| 大数据 Kafka 命令 | 020-KafkaCommands | 本文的并列主题 |
| 大数据 HBase 命令 | 021-HBaseCommands | 本文的并列主题 |
| 大数据 Flink 流处理 | 022-FlinkBasics | 本文的并列主题 |
| 大数据 Spark 优化 | 023-SparkOptimization | 本文的性能延伸 |
