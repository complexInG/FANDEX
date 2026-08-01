---
order: 190
title: 大数据 Hive 函数
module: 052-big-data
category: '052-big-data'
difficulty: beginner
description: 大数据 Hive 函数 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 大数据 Hive 函数

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 内置聚合函数

**基本写法：求和**
`SUM(<列>)`

```sql
-- 求和
SELECT dept_id, SUM(salary) FROM employees GROUP BY dept_id;
```

---

**基本写法：平均值**
`AVG(<列>)`

```sql
-- 平均值
SELECT AVG(salary) FROM employees;
```

---

**基本写法：计数**
`COUNT([DISTINCT] <列>)`

```sql
-- 计数
SELECT COUNT(*) FROM employees;
SELECT COUNT(DISTINCT dept_id) FROM employees;
```

---

**基本写法：最大值最小值**
`MAX(<列>)` | `MIN(<列>)`

```sql
-- 最大最小值
SELECT MAX(salary), MIN(salary) FROM employees;
```

---

**基本写法：标准差**
`STDDEV(<列>)` | `STDDEV_POP(<列>)`

```sql
-- 标准差
SELECT STDDEV(salary), STDDEV_POP(salary) FROM employees;
```

---

**基本写法：方差**
`VARIANCE(<列>)` | `VAR_POP(<列>)`

```sql
-- 方差
SELECT VARIANCE(salary) FROM employees;
```

---

**基本写法：百分位数**
`PERCENTILE(<列>, <百分比>)`

```sql
-- 百分位数
SELECT PERCENTILE(salary, 0.5) FROM employees;
-- 多个百分位
SELECT PERCENTILE(salary, ARRAY(0.25, 0.5, 0.75)) FROM employees;
```

---

**基本写法：相关系数**
`CORR(<列1>, <列2>)`

```sql
-- 相关系数
SELECT CORR(salary, age) FROM employees;
```

---

## 字符串函数

**基本写法：字符串长度**
`LENGTH(<字符串>)`

```sql
-- 字符串长度
SELECT name, LENGTH(name) FROM employees;
```

---

**基本写法：大小写转换**
`UPPER(<字符串>)` | `LOWER(<字符串>)`

```sql
-- 大小写转换
SELECT UPPER(name), LOWER(name) FROM employees;
```

---

**基本写法：字符串拼接**
`CONCAT(<字符串1>, <字符串2>, ...)`

```sql
-- 拼接字符串
SELECT CONCAT(name, '-', city) FROM employees;
```

---

**基本写法：带分隔符拼接**
`CONCAT_WS(<分隔符>, <字符串1>, <字符串2>)`

```sql
-- 带分隔符拼接
SELECT CONCAT_WS(',', name, city, dept_id) FROM employees;
```

---

**基本写法：子字符串**
`SUBSTRING(<字符串>, <开始位置>, [<长度>])`

```sql
-- 截取子字符串
SELECT SUBSTRING(name, 1, 3) FROM employees;
SELECT SUBSTR(name, 2) FROM employees;
```

---

**基本写法：字符串分割**
`SPLIT(<字符串>, <分隔符>)`

```sql
-- 分割字符串
SELECT SPLIT('a,b,c', ',');
```

---

**基本写法：查找位置**
`INSTR(<字符串>, <子字符串>)`

```sql
-- 查找子字符串位置
SELECT INSTR(name, 'a') FROM employees;
```

---

**基本写法：替换**
`REGEXP_REPLACE(<字符串>, <正则>, <替换>)`

```sql
-- 正则替换
SELECT REGEXP_REPLACE(phone, '\\D', '') FROM employees;
```

---

**基本写法：正则提取**
`REGEXP_EXTRACT(<字符串>, <正则>, [<组号>])`

```sql
-- 正则提取
SELECT REGEXP_EXTRACT('2024-01-15', '(\\d{4})-(\\d{2})', 1);
```

---

**基本写法：去除空白**
`TRIM(<字符串>)` | `LTRIM(<字符串>)` | `RTRIM(<字符串>)`

```sql
-- 去除空白
SELECT TRIM(name), LTRIM(name), RTRIM(name) FROM employees;
```

---

**基本写法：填充字符串**
`LPAD(<字符串>, <长度>, <填充字符>)` | `RPAD(<字符串>, <长度>, <填充字符>)`

```sql
-- 填充字符串
SELECT LPAD(id, 5, '0') FROM employees;
SELECT RPAD(name, 10, '*') FROM employees;
```

---

## 日期函数

**基本写法：当前日期**
`CURRENT_DATE()` | `CURRENT_TIMESTAMP()`

```sql
-- 当前日期和时间
SELECT CURRENT_DATE(), CURRENT_TIMESTAMP();
```

---

**基本写法：日期格式化**
`DATE_FORMAT(<日期>, <格式>)`

```sql
-- 格式化日期
SELECT DATE_FORMAT(hire_date, 'yyyy-MM-dd') FROM employees;
SELECT DATE_FORMAT(CURRENT_TIMESTAMP(), 'yyyy-MM-dd HH:mm:ss');
```

---

**基本写法：日期解析**
`TO_DATE(<字符串>)`

```sql
-- 字符串转日期
SELECT TO_DATE('2024-01-15');
```

---

**基本写法：提取年月日**
`YEAR(<日期>)` | `MONTH(<日期>)` | `DAY(<日期>)`

```sql
-- 提取年月日
SELECT YEAR(hire_date), MONTH(hire_date), DAY(hire_date) FROM employees;
```

---

**基本写法：日期加减**
`DATE_ADD(<日期>, <天数>)` | `DATE_SUB(<日期>, <天数>)`

```sql
-- 日期加减
SELECT DATE_ADD(CURRENT_DATE(), 30);
SELECT DATE_SUB(CURRENT_DATE(), 7);
```

---

**基本写法：日期差**
`DATEDIFF(<结束日期>, <开始日期>)`

```sql
-- 计算日期差
SELECT DATEDIFF(CURRENT_DATE(), hire_date) FROM employees;
```

---

**基本写法：日期 trunc**
`TRUNC(<日期>, <级别>)`

```sql
-- 截断到月初或年初
SELECT TRUNC(CURRENT_DATE(), 'MM');  -- 月初
SELECT TRUNC(CURRENT_DATE(), 'YYYY'); -- 年初
```

---

**基本写法：添加月份**
`ADD_MONTHS(<日期>, <月数>)`

```sql
-- 添加月份
SELECT ADD_MONTHS(CURRENT_DATE(), 3);
```

---

**基本写法：上月末**
`LAST_DAY(<日期>)`

```sql
-- 获取月末日期
SELECT LAST_DAY(CURRENT_DATE());
```

---

**基本写法：下个星期**
`NEXT_DAY(<日期>, <星期几>)`

```sql
-- 下一个指定星期
SELECT NEXT_DAY(CURRENT_DATE(), 'MON');
```

---

## 条件函数

**基本写法：IF 条件**
`IF(<条件>, <真值>, <假值>)`

```sql
-- IF 条件
SELECT name, IF(salary > 15000, '高薪', '低薪') AS level FROM employees;
```

---

**基本写法：CASE WHEN**
`CASE WHEN <条件1> THEN <值1> WHEN <条件2> THEN <值2> ELSE <默认值> END`

```sql
-- CASE WHEN
SELECT name, salary,
    CASE
        WHEN salary > 20000 THEN '高'
        WHEN salary > 10000 THEN '中'
        ELSE '低'
    END AS level
FROM employees;
```

---

**基本写法：COALESCE**
`COALESCE(<值1>, <值2>, ...)`

```sql
-- 返回第一个非 NULL 值
SELECT COALESCE(phone, email, '无联系方式') FROM employees;
```

---

**基本写法：NULLIF**
`NULLIF(<值1>, <值2>)`

```sql
-- 两值相等返回 NULL
SELECT NULLIF(salary, 0) FROM employees;
```

---

**基本写法：NVL**
`NVL(<列>, <默认值>)`

```sql
-- NULL 替换
SELECT NVL(dept_id, '未分配') FROM employees;
```

---

## 数学函数

**基本写法：四舍五入**
`ROUND(<数字>, [<小数位>])`

```sql
-- 四舍五入
SELECT ROUND(salary, 2) FROM employees;
SELECT ROUND(3.14159, 2);
```

---

**基本写法：向下取整**
`FLOOR(<数字>)`

```sql
-- 向下取整
SELECT FLOOR(salary) FROM employees;
```

---

**基本写法：向上取整**
`CEIL(<数字>)` | `CEILING(<数字>)`

```sql
-- 向上取整
SELECT CEIL(salary) FROM employees;
```

---

**基本写法：绝对值**
`ABS(<数字>)`

```sql
-- 绝对值
SELECT ABS(salary - avg_salary) FROM employees;
```

---

**基本写法：幂运算**
`POWER(<底数>, <指数>)` | `POW(<底数>, <指数>)`

```sql
-- 幂运算
SELECT POWER(2, 10);
```

---

**基本写法：对数**
`LOG(<底数>, <真数>)` | `LN(<真数>)`

```sql
-- 对数
SELECT LOG(10, 100);
SELECT LN(2.718281828);
```

---

**基本写法：取随机数**
`RAND([<种子>])`

```sql
-- 随机数
SELECT RAND();
SELECT RAND(42);
```

---

## 窗口函数

**基本写法：行号**
`ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <列>)`

```sql
-- 行号
SELECT name, dept_id, salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
FROM employees;
```

---

**基本写法：排名**
`RANK() OVER (PARTITION BY <列> ORDER BY <列>)`

```sql
-- 排名（有间隔）
SELECT name, salary,
    RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

---

**基本写法：密集排名**
`DENSE_RANK() OVER (PARTITION BY <列> ORDER BY <列>)`

```sql
-- 密集排名
SELECT name, salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;
```

---

**基本写法：前 N 行**
`LEAD(<列>, [<偏移>], [<默认值>]) OVER (...)`

```sql
-- 获取后一行的值
SELECT name, salary,
    LEAD(salary, 1, 0) OVER (ORDER BY salary) AS next_sal
FROM employees;
```

---

**基本写法：前一行**
`LAG(<列>, [<偏移>], [<默认值>]) OVER (...)`

```sql
-- 获取前一行的值
SELECT name, salary,
    LAG(salary, 1, 0) OVER (ORDER BY salary) AS prev_sal
FROM employees;
```

---

**基本写法：首行末行**
`FIRST_VALUE(<列>) OVER (...)` | `LAST_VALUE(<列>) OVER (...)`

```sql
-- 首行和末行
SELECT name, salary,
    FIRST_VALUE(salary) OVER (PARTITION BY dept_id ORDER BY salary) AS first_sal,
    LAST_VALUE(salary) OVER (PARTITION BY dept_id ORDER BY salary 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_sal
FROM employees;
```

---

## 自定义函数

**换行写法：创建 UDF**
`package com.example;`
`public class <类名> extends UDF {`
`    public <返回类型> evaluate(<参数类型> <参数>) { return <值>; }`
`}`

```java
// Java UDF 示例
package com.example;
import org.apache.hadoop.hive.ql.exec.UDF;

public class UpperCase extends UDF {
    public String evaluate(String input) {
        return input == null ? null : input.toUpperCase();
    }
}
```

---

**基本写法：添加 JAR**
`ADD JAR <jar路径>`

```sql
-- 添加 UDF JAR 包
ADD JAR /path/to/my_udf.jar;
```

---

**基本写法：创建临时函数**
`CREATE TEMPORARY FUNCTION <函数名> AS '<类全名>'`

```sql
-- 注册临时函数
CREATE TEMPORARY FUNCTION my_upper AS 'com.example.UpperCase';
```

---

**基本写法：使用 UDF**
`SELECT <函数名>(<列>) FROM <表名>`

```sql
-- 使用自定义函数
SELECT my_upper(name) FROM employees;
```

---

**基本写法：Python UDF**
`CREATE TEMPORARY FUNCTION <函数名> AS '<脚本路径>.<函数名>' USING FILE '<脚本路径>'`

```sql
-- Python UDF（Hive 3.0+）
CREATE TEMPORARY FUNCTION my_func
AS 'my_script.my_func'
USING FILE '/path/to/my_script.py';
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
| 大数据 Hive 函数 | 019-HiveFunctions | 本文自身 |
| 大数据 Kafka 命令 | 020-KafkaCommands | 本文的并列主题 |
| 大数据 HBase 命令 | 021-HBaseCommands | 本文的并列主题 |
| 大数据 Flink 流处理 | 022-FlinkBasics | 本文的并列主题 |
| 大数据 Spark 优化 | 023-SparkOptimization | 本文的性能延伸 |
