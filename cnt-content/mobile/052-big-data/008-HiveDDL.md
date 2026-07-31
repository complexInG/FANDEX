# 大数据 Hive DDL

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数据库操作

**基本写法：创建数据库**
`CREATE DATABASE [IF NOT EXISTS] <数据库名>`

```sql
-- 创建数据库
CREATE DATABASE IF NOT EXISTS my_db;
```

---

**基本写法：带注释创建**
`CREATE DATABASE <数据库名> COMMENT <注释>`

```sql
-- 带注释创建数据库
CREATE DATABASE my_db COMMENT '销售数据库';
```

---

**基本写法：指定存储位置**
`CREATE DATABASE <数据库名> LOCATION <路径>`

```sql
-- 指定存储位置
CREATE DATABASE my_db LOCATION '/user/hadoop/my_db';
```

---

**基本写法：带属性创建**
`CREATE DATABASE <数据库名> WITH DBPROPERTIES (<键>=<值>)`

```sql
-- 带属性创建
CREATE DATABASE my_db WITH DBPROPERTIES ('creator'='admin', 'date'='2024-01-01');
```

---

**基本写法：查看数据库**
`SHOW DATABASES [LIKE <模式>]`

```sql
-- 查看所有数据库
SHOW DATABASES;
-- 模糊匹配
SHOW DATABASES LIKE 'my*';
```

---

**基本写法：查看数据库详情**
`DESCRIBE DATABASE [EXTENDED] <数据库名>`

```sql
-- 查看数据库信息
DESCRIBE DATABASE my_db;
-- 查看详细信息（含属性）
DESCRIBE DATABASE EXTENDED my_db;
```

---

**基本写法：修改数据库**
`ALTER DATABASE <数据库名> SET DBPROPERTIES (<键>=<值>)`

```sql
-- 修改数据库属性
ALTER DATABASE my_db SET DBPROPERTIES ('modified'='2024-06-01');
```

---

**基本写法：删除数据库**
`DROP DATABASE [IF EXISTS] <数据库名> [RESTRICT|CASCADE]`

```sql
-- 删除空数据库（默认 RESTRICT）
DROP DATABASE IF EXISTS my_db;
-- 级联删除（含表）
DROP DATABASE IF EXISTS my_db CASCADE;
```

---

## 内部表

**基本写法：创建内部表**
`CREATE TABLE <表名> (<列名> <类型>, ...)`

```sql
-- 创建内部表
CREATE TABLE employees (
    id INT,
    name STRING,
    age INT,
    salary DOUBLE
);
```

---

**基本写法：带注释创建表**
`CREATE TABLE <表名> (<列名> <类型> COMMENT <注释>, ...)`

```sql
-- 带列注释
CREATE TABLE employees (
    id INT COMMENT '员工ID',
    name STRING COMMENT '员工姓名',
    salary DOUBLE COMMENT '薪资'
);
```

---

**基本写法：带表注释**
`CREATE TABLE <表名> (...) COMMENT <注释>`

```sql
-- 带表注释
CREATE TABLE employees (
    id INT,
    name STRING
) COMMENT '员工信息表';
```

---

## 外部表

**基本写法：创建外部表**
`CREATE EXTERNAL TABLE <表名> (<列定义>) LOCATION <路径>`

```sql
-- 创建外部表
CREATE EXTERNAL TABLE logs (
    id INT,
    message STRING
) LOCATION '/user/hadoop/logs';
```

---

**基本写法：带格式的外部表**
`CREATE EXTERNAL TABLE <表名> (<列定义>) ROW FORMAT DELIMITED FIELDS TERMINATED BY <分隔符>`

```sql
-- 带分隔符的外部表
CREATE EXTERNAL TABLE users (
    id INT,
    name STRING,
    email STRING
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hadoop/users';
```

---

## 分区表

**基本写法：创建分区表**
`CREATE TABLE <表名> (<列定义>) PARTITIONED BY (<分区列> <类型>)`

```sql
-- 创建分区表
CREATE TABLE sales (
    id INT,
    amount DOUBLE
) PARTITIONED BY (year INT, month INT);
```

---

**基本写法：添加分区**
`ALTER TABLE <表名> ADD PARTITION (<分区列>=<值>) [LOCATION <路径>]`

```sql
-- 添加单个分区
ALTER TABLE sales ADD PARTITION (year=2024, month=1);
-- 添加多个分区
ALTER TABLE sales ADD
    PARTITION (year=2024, month=2)
    PARTITION (year=2024, month=3);
```

---

**基本写法：重命名分区**
`ALTER TABLE <表名> PARTITION (<分区列>=<值>) RENAME TO PARTITION (<分区列>=<新值>)`

```sql
-- 重命名分区
ALTER TABLE sales PARTITION (year=2024, month=1) 
RENAME TO PARTITION (year=2024, month=01);
```

---

**基本写法：修改分区位置**
`ALTER TABLE <表名> PARTITION (<分区列>=<值>) SET LOCATION <新路径>`

```sql
-- 修改分区存储位置
ALTER TABLE sales PARTITION (year=2024, month=1) 
SET LOCATION '/user/hadoop/sales/2024/01';
```

---

**基本写法：删除分区**
`ALTER TABLE <表名> DROP PARTITION (<分区列>=<值>)`

```sql
-- 删除分区
ALTER TABLE sales DROP PARTITION (year=2024, month=1);
```

---

**基本写法：查看分区**
`SHOW PARTITIONS <表名>`

```sql
-- 查看所有分区
SHOW PARTITIONS sales;
```

---

**基本写法：查看特定分区**
`SHOW PARTITIONS <表名> PARTITION (<分区列>=<值>)`

```sql
-- 查看特定分区
SHOW PARTITIONS sales PARTITION (year=2024);
```

---

**基本写法：修复分区**
`MSCK REPAIR TABLE <表名>`

```sql
-- 修复分区（同步 HDFS 目录到元数据）
MSCK REPAIR TABLE sales;
```

---

## 分桶表

**基本写法：创建分桶表**
`CREATE TABLE <表名> (<列定义>) CLUSTERED BY (<列>) INTO <n> BUCKETS`

```sql
-- 创建分桶表
CREATE TABLE users (
    id INT,
    name STRING
) CLUSTERED BY (id) INTO 4 BUCKETS;
```

---

**基本写法：分桶并排序**
`CREATE TABLE <表名> (...) CLUSTERED BY (<列>) SORTED BY (<列>) INTO <n> BUCKETS`

```sql
-- 分桶并排序
CREATE TABLE users (
    id INT,
    name STRING
) CLUSTERED BY (id) SORTED BY (id ASC) INTO 4 BUCKETS;
```

---

## 存储格式

**基本写法：文本格式**
`STORED AS TEXTFILE`

```sql
-- 存储为文本文件
CREATE TABLE my_table (id INT, name STRING)
STORED AS TEXTFILE;
```

---

**基本写法：SequenceFile 格式**
`STORED AS SEQUENCEFILE`

```sql
-- 存储为 SequenceFile
CREATE TABLE my_table (id INT, name STRING)
STORED AS SEQUENCEFILE;
```

---

**基本写法：ORC 格式**
`STORED AS ORC`

```sql
-- 存储为 ORC（列式存储）
CREATE TABLE my_table (id INT, name STRING)
STORED AS ORC;
```

---

**基本写法：Parquet 格式**
`STORED AS PARQUET`

```sql
-- 存储为 Parquet（列式存储）
CREATE TABLE my_table (id INT, name STRING)
STORED AS PARQUET;
```

---

**基本写法：带行格式**
`ROW FORMAT DELIMITED FIELDS TERMINATED BY <分隔符>`

```sql
-- 指定字段分隔符
CREATE TABLE my_table (id INT, name STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
```

---

## 修改表

**基本写法：重命名表**
`ALTER TABLE <旧表名> RENAME TO <新表名>`

```sql
-- 重命名表
ALTER TABLE employees RENAME TO staff;
```

---

**基本写法：添加列**
`ALTER TABLE <表名> ADD COLUMNS (<列定义>)`

```sql
-- 添加列
ALTER TABLE employees ADD COLUMNS (email STRING, phone STRING);
```

---

**基本写法：修改列**
`ALTER TABLE <表名> CHANGE <旧列名> <新列名> <类型> [AFTER <列名>]`

```sql
-- 修改列名和类型
ALTER TABLE employees CHANGE name username STRING;
-- 修改列位置
ALTER TABLE employees CHANGE id id INT AFTER username;
```

---

**基本写法：替换列**
`ALTER TABLE <表名> REPLACE COLUMNS (<列定义>)`

```sql
-- 替换所有列
ALTER TABLE employees REPLACE COLUMNS (
    id INT,
    username STRING,
    salary DOUBLE
);
```

---

**基本写法：修改表属性**
`ALTER TABLE <表名> SET TBLPROPERTIES (<键>=<值>)`

```sql
-- 修改表属性
ALTER TABLE employees SET TBLPROPERTIES ('owner'='admin');
```

---

## 视图

**基本写法：创建视图**
`CREATE VIEW <视图名> AS SELECT ...`

```sql
-- 创建视图
CREATE VIEW high_salary AS
SELECT * FROM employees WHERE salary > 15000;
```

---

**基本写法：创建物化视图**
`CREATE MATERIALIZED VIEW <视图名> AS SELECT ...`

```sql
-- 创建物化视图（Hive 3.0+）
CREATE MATERIALIZED VIEW dept_stats AS
SELECT dept_id, AVG(salary) FROM employees GROUP BY dept_id;
```

---

**基本写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名>`

```sql
-- 删除视图
DROP VIEW IF EXISTS high_salary;
```

---

## 表信息查看

**基本写法：查看表列表**
`SHOW TABLES [IN <数据库>] [LIKE <模式>]`

```sql
-- 查看当前数据库的表
SHOW TABLES;
-- 模糊匹配
SHOW TABLES LIKE 'emp*';
```

---

**基本写法：查看表结构**
`DESCRIBE [FORMATTED|EXTENDED] <表名>`

```sql
-- 查看表结构
DESCRIBE employees;
-- 查看详细信息
DESCRIBE FORMATTED employees;
```

---

**基本写法：查看列信息**
`DESCRIBE <表名>.<列名>`

```sql
-- 查看指定列
DESCRIBE employees.salary;
```

---

**基本写法：查看创建语句**
`SHOW CREATE TABLE <表名>`

```sql
-- 查看建表语句
SHOW CREATE TABLE employees;
```

---

## 删除表

**基本写法：删除表**
`DROP TABLE [IF EXISTS] <表名>`

```sql
-- 删除表（内部表删除数据，外部表只删元数据）
DROP TABLE IF EXISTS employees;
```

---

**基本写法：清空表**
`TRUNCATE TABLE <表名> [PARTITION (<分区列>=<值>)]`

```sql
-- 清空表数据
TRUNCATE TABLE employees;
-- 清空指定分区
TRUNCATE TABLE sales PARTITION (year=2024, month=1);
```
