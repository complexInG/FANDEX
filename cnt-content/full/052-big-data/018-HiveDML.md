---
order: 180
title: 大数据 Hive DML
module: 052-big-data
category: '052-big-data'
difficulty: beginner
description: 大数据 Hive DML 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 数据加载

**基本写法：从文件加载数据**
`LOAD DATA [LOCAL] INPATH <路径> [OVERWRITE] INTO TABLE <表名>`

```sql
-- 从 HDFS 加载数据
LOAD DATA INPATH '/user/hadoop/data.csv' INTO TABLE employees;
-- 从本地文件系统加载
LOAD DATA LOCAL INPATH '/home/user/data.csv' INTO TABLE employees;
-- 覆盖加载
LOAD DATA LOCAL INPATH '/home/user/data.csv' OVERWRITE INTO TABLE employees;
```

---

**基本写法：加载到分区**
`LOAD DATA INPATH <路径> INTO TABLE <表名> PARTITION (<分区列>=<值>)`

```sql
-- 加载到指定分区
LOAD DATA LOCAL INPATH '/home/user/jan.csv'
INTO TABLE sales PARTITION (year=2024, month=1);
```

---

## 数据插入

**基本写法：插入单行数据**
`INSERT INTO <表名> VALUES (<值1>, <值2>, ...)`

```sql
-- 插入单行
INSERT INTO employees VALUES (1, 'Alice', 30, 15000.0);
```

---

**基本写法：插入多行数据**
`INSERT INTO <表名> VALUES (<值1>, ...), (<值2>, ...)`

```sql
-- 插入多行
INSERT INTO employees VALUES
    (2, 'Bob', 25, 12000.0),
    (3, 'Charlie', 35, 20000.0),
    (4, 'David', 28, 13000.0);
```

---

**基本写法：从查询插入**
`INSERT INTO <表名> SELECT ...`

```sql
-- 从查询结果插入
INSERT INTO high_salary
SELECT * FROM employees WHERE salary > 15000;
```

---

**基本写法：覆盖插入**
`INSERT OVERWRITE TABLE <表名> SELECT ...`

```sql
-- 覆盖表数据
INSERT OVERWRITE TABLE employees
SELECT * FROM temp_employees;
```

---

**基本写法：插入到分区**
`INSERT INTO <表名> PARTITION (<分区列>=<值>) SELECT ...`

```sql
-- 插入到指定分区
INSERT INTO sales PARTITION (year=2024, month=1)
SELECT id, amount FROM temp_sales;
```

---

**基本写法：动态分区插入**
`INSERT OVERWRITE TABLE <表名> PARTITION (<分区列>) SELECT ..., <分区列>`

```sql
-- 动态分区插入（分区列值来自查询）
INSERT OVERWRITE TABLE sales PARTITION (year, month)
SELECT id, amount, year, month FROM temp_sales;
```

---

**基本写法：多表插入**
`FROM <源表> INSERT INTO <表1> SELECT ... INSERT INTO <表2> SELECT ...`

```sql
-- 一次查询插入多表
FROM employees
INSERT INTO high_salary SELECT * WHERE salary > 15000
INSERT INTO low_salary SELECT * WHERE salary <= 15000;
```

---

## 数据导出

**基本写法：导出到本地**
`INSERT OVERWRITE LOCAL DIRECTORY <路径> SELECT ...`

```sql
-- 导出到本地文件系统
INSERT OVERWRITE LOCAL DIRECTORY '/home/user/output'
SELECT * FROM employees;
```

---

**基本写法：指定分隔符导出**
`INSERT OVERWRITE LOCAL DIRECTORY <路径> ROW FORMAT DELIMITED FIELDS TERMINATED BY <分隔符> SELECT ...`

```sql
-- 指定分隔符导出
INSERT OVERWRITE LOCAL DIRECTORY '/home/user/output'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT * FROM employees;
```

---

**基本写法：导出到 HDFS**
`INSERT OVERWRITE DIRECTORY <HDFS路径> SELECT ...`

```sql
-- 导出到 HDFS
INSERT OVERWRITE DIRECTORY '/user/hadoop/output'
SELECT * FROM employees;
```

---

## 数据更新与删除

**基本写法：更新数据**
`UPDATE <表名> SET <列>=<值> WHERE <条件>`

```sql
-- 更新数据（需 ACID 支持）
UPDATE employees SET salary = 16000.0 WHERE id = 1;
```

---

**基本写法：删除数据**
`DELETE FROM <表名> WHERE <条件>`

```sql
-- 删除数据（需 ACID 支持）
DELETE FROM employees WHERE id = 1;
```

---

**基本写法：合并数据**
`MERGE INTO <目标表> USING <源表> ON <条件> WHEN MATCHED THEN ...`

```sql
-- MERGE 操作（Hive 2.2+）
MERGE INTO employees AS target
USING new_employees AS source
ON target.id = source.id
WHEN MATCHED THEN UPDATE SET salary = source.salary
WHEN NOT MATCHED THEN INSERT VALUES (source.id, source.name, source.salary);
```

---

## 数据查询

**基本写法：基本查询**
`SELECT <列> FROM <表名> [WHERE <条件>]`

```sql
-- 基本查询
SELECT * FROM employees;
SELECT name, salary FROM employees WHERE age > 30;
```

---

**基本写法：使用别名**
`SELECT <列> AS <别名> FROM <表名>`

```sql
-- 使用列别名
SELECT name AS employee_name, salary AS monthly_salary
FROM employees;
```

---

**基本写法：排序**
`SELECT * FROM <表名> ORDER BY <列> [DESC]`

```sql
-- 排序（全局排序，只有一个 Reducer）
SELECT * FROM employees ORDER BY salary DESC;
```

---

**基本写法：Sort By 排序**
`SELECT * FROM <表名> SORT BY <列> [DESC]`

```sql
-- 局部排序（每个 Reducer 内排序）
SELECT * FROM employees SORT BY salary DESC;
```

---

**基本写法：Distribute By**
`SELECT * FROM <表名> DISTRIBUTE BY <列>`

```sql
-- 分配数据到 Reducer（常与 Sort By 配合）
SELECT * FROM employees DISTRIBUTE BY dept_id SORT BY salary DESC;
```

---

**基本写法：Cluster By**
`SELECT * FROM <表名> CLUSTER BY <列>`

```sql
# 等同于 DISTRIBUTE BY + SORT BY（同一列）
SELECT * FROM employees CLUSTER BY dept_id;
```

---

**基本写法：限制结果**
`SELECT * FROM <表名> LIMIT <n>`

```sql
-- 限制返回行数
SELECT * FROM employees LIMIT 10;
```

---

## Join 查询

**基本写法：内连接**
`SELECT * FROM <表1> JOIN <表2> ON <条件>`

```sql
-- 内连接
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

---

**基本写法：左连接**
`SELECT * FROM <表1> LEFT JOIN <表2> ON <条件>`

```sql
-- 左外连接
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;
```

---

**基本写法：右连接**
`SELECT * FROM <表1> RIGHT JOIN <表2> ON <条件>`

```sql
-- 右外连接
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.id;
```

---

**基本写法：全连接**
`SELECT * FROM <表1> FULL JOIN <表2> ON <条件>`

```sql
-- 全外连接
SELECT e.name, d.dept_name
FROM employees e
FULL JOIN departments d ON e.dept_id = d.id;
```

---

**基本写法：多表连接**
`SELECT * FROM <表1> JOIN <表2> ON ... JOIN <表3> ON ...`

```sql
-- 多表连接
SELECT e.name, d.dept_name, p.project_name
FROM employees e
JOIN departments d ON e.dept_id = d.id
JOIN projects p ON e.id = p.employee_id;
```

---

**基本写法：MapJoin 优化**
`SELECT /*+ MAPJOIN(<小表>) */ * FROM <大表> JOIN <小表> ON <条件>`

```sql
-- MapJoin 提示（小表加载到内存）
SELECT /*+ MAPJOIN(d) */ e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

---

## 分组聚合

**基本写法：分组聚合**
`SELECT <列>, <聚合函数>(<列>) FROM <表名> GROUP BY <列>`

```sql
-- 分组聚合
SELECT dept_id, AVG(salary) as avg_salary, COUNT(*) as cnt
FROM employees
GROUP BY dept_id;
```

---

**基本写法：Having 过滤**
`SELECT ... GROUP BY ... HAVING <条件>`

```sql
-- 分组后过滤
SELECT dept_id, AVG(salary) as avg_sal
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 10000;
```

---

**基本写法：多维分组**
`SELECT ... FROM <表名> GROUP BY <列1>, <列2> WITH CUBE`

```sql
-- CUBE（所有维度的组合）
SELECT dept_id, city, AVG(salary) FROM employees
GROUP BY dept_id, city WITH CUBE;
```

---

**基本写法：Rollup 分组**
`SELECT ... FROM <表名> GROUP BY <列1>, <列2> WITH ROLLUP`

```sql
-- ROLLUP（层次聚合）
SELECT dept_id, city, AVG(salary) FROM employees
GROUP BY dept_id, city WITH ROLLUP;
```

---

**基本写法：GROUPING SETS**
`SELECT ... FROM <表名> GROUP BY GROUPING SETS ((<列1>), (<列2>), (<列1>, <列2>))`

```sql
-- 指定分组组合
SELECT dept_id, city, AVG(salary) FROM employees
GROUP BY GROUPING SETS ((dept_id), (city), (dept_id, city));
```

---

## 子查询

**基本写法：WHERE 子查询**
`SELECT * FROM <表名> WHERE <列> IN (SELECT ...)`

```sql
-- 子查询
SELECT * FROM employees
WHERE dept_id IN (SELECT id FROM departments WHERE name = '技术部');
```

---

**基本写法：FROM 子查询**
`SELECT * FROM (SELECT ... FROM <表名>) <别名>`

```sql
-- FROM 子查询
SELECT t.dept_id, t.avg_sal
FROM (
    SELECT dept_id, AVG(salary) as avg_sal
    FROM employees
    GROUP BY dept_id
) t
WHERE t.avg_sal > 10000;
```

---

**基本写法：WITH 子句**
`WITH <别名> AS (SELECT ...) SELECT * FROM <别名>`

```sql
-- CTE 公共表表达式
WITH dept_avg AS (
    SELECT dept_id, AVG(salary) as avg_sal
    FROM employees
    GROUP BY dept_id
)
SELECT e.name, e.salary, d.avg_sal
FROM employees e
JOIN dept_avg d ON e.dept_id = d.dept_id
WHERE e.salary > d.avg_sal;
```

---

## 采样查询

**基本写法：随机采样**
`SELECT * FROM <表名> TABLESAMPLE(<n> PERCENT)`

```sql
-- 随机采样 10% 数据
SELECT * FROM employees TABLESAMPLE(10 PERCENT);
```

---

**基本写法：按行数采样**
`SELECT * FROM <表名> TABLESAMPLE(<n> ROWS)`

```sql
-- 采样 100 行
SELECT * FROM employees TABLESAMPLE(100 ROWS);
```

---

**基本写法：分桶采样**
`SELECT * FROM <表名> TABLESAMPLE(BUCKET <n> OUT OF <总数> ON <列>)`

```sql
-- 分桶采样（10 个桶取 1 个）
SELECT * FROM employees TABLESAMPLE(BUCKET 1 OUT OF 10 ON id);
```

---

## UNION 操作

**基本写法：UNION ALL**
`SELECT ... UNION ALL SELECT ...`

```sql
-- 不去重合并
SELECT name FROM employees_2023
UNION ALL
SELECT name FROM employees_2024;
```

---

**基本写法：UNION**
`SELECT ... UNION SELECT ...`

```sql
-- 去重合并
SELECT name FROM employees_2023
UNION
SELECT name FROM employees_2024;
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
| 大数据 Hive DML | 018-HiveDML | 本文自身 |
| 大数据 Hive 函数 | 019-HiveFunctions | 本文的并列主题 |
| 大数据 Kafka 命令 | 020-KafkaCommands | 本文的并列主题 |
| 大数据 HBase 命令 | 021-HBaseCommands | 本文的并列主题 |
| 大数据 Flink 流处理 | 022-FlinkBasics | 本文的并列主题 |
| 大数据 Spark 优化 | 023-SparkOptimization | 本文的性能延伸 |
