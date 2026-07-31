# 大数据 Spark SQL

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

**基本写法：指定位置**
`CREATE DATABASE <数据库名> LOCATION <路径>`

```sql
-- 指定数据库存储位置
CREATE DATABASE my_db LOCATION '/user/hadoop/my_db';
```

---

**基本写法：查看数据库**
`SHOW DATABASES`

```sql
-- 查看所有数据库
SHOW DATABASES;
```

---

**基本写法：使用数据库**
`USE <数据库名>`

```sql
-- 切换数据库
USE my_db;
```

---

**基本写法：删除数据库**
`DROP DATABASE [IF EXISTS] <数据库名> [CASCADE]`

```sql
-- 删除空数据库
DROP DATABASE IF EXISTS my_db;
-- 级联删除（含表）
DROP DATABASE IF EXISTS my_db CASCADE;
```

---

## 表操作

**基本写法：创建表**
`CREATE TABLE <表名> (<列名> <类型>, ...)`

```sql
-- 创建表
CREATE TABLE employees (
    id INT,
    name STRING,
    age INT,
    salary DOUBLE
);
```

---

**基本写法：使用 Parquet 格式**
`CREATE TABLE <表名> (<列定义>) USING PARQUET`

```sql
-- 创建 Parquet 格式表
CREATE TABLE employees (
    id INT,
    name STRING,
    salary DOUBLE
) USING PARQUET;
```

---

**基本写法：使用 ORC 格式**
`CREATE TABLE <表名> (<列定义>) USING ORC`

```sql
-- 创建 ORC 格式表
CREATE TABLE employees (
    id INT,
    name STRING
) USING ORC;
```

---

**基本写法：分区表**
`CREATE TABLE <表名> (<列定义>) PARTITIONED BY (<分区列>)`

```sql
-- 创建分区表
CREATE TABLE sales (
    id INT,
    amount DOUBLE
) PARTITIONED BY (year INT, month INT);
```

---

**基本写法：分桶表**
`CREATE TABLE <表名> (<列定义>) CLUSTERED BY (<列>) INTO <n> BUCKETS`

```sql
-- 创建分桶表
CREATE TABLE users (
    id INT,
    name STRING
) CLUSTERED BY (id) INTO 4 BUCKETS;
```

---

**基本写法：外部表**
`CREATE EXTERNAL TABLE <表名> (<列定义>) LOCATION <路径>`

```sql
-- 创建外部表
CREATE EXTERNAL TABLE logs (
    id INT,
    message STRING
) LOCATION '/user/hadoop/logs';
```

---

**基本写法：查看表**
`SHOW TABLES [IN <数据库>]`

```sql
-- 查看当前数据库的表
SHOW TABLES;
-- 查看指定数据库的表
SHOW TABLES IN my_db;
```

---

**基本写法：查看表结构**
`DESCRIBE <表名>`

```sql
-- 查看表结构
DESCRIBE employees;
-- 查看详细信息
DESCRIBE FORMATTED employees;
```

---

**基本写法：删除表**
`DROP TABLE [IF EXISTS] <表名>`

```sql
-- 删除表
DROP TABLE IF EXISTS employees;
```

---

**基本写法：重命名表**
`ALTER TABLE <旧表名> RENAME TO <新表名>`

```sql
-- 重命名表
ALTER TABLE employees RENAME TO staff;
```

---

## 数据查询

**基本写法：基本查询**
`SELECT <列1>, <列2> FROM <表名>`

```sql
-- 查询所有列
SELECT * FROM employees;
-- 查询指定列
SELECT name, salary FROM employees;
```

---

**基本写法：条件查询**
`SELECT * FROM <表名> WHERE <条件>`

```sql
-- 条件查询
SELECT * FROM employees WHERE age > 30;
SELECT * FROM employees WHERE city = '北京' AND salary > 10000;
```

---

**基本写法：排序**
`SELECT * FROM <表名> ORDER BY <列> [DESC]`

```sql
-- 排序
SELECT * FROM employees ORDER BY salary DESC;
-- 多列排序
SELECT * FROM employees ORDER BY city, salary DESC;
```

---

**基本写法：限制结果**
`SELECT * FROM <表名> LIMIT <n>`

```sql
-- 限制返回行数
SELECT * FROM employees LIMIT 10;
```

---

**基本写法：去重**
`SELECT DISTINCT <列> FROM <表名>`

```sql
-- 去重查询
SELECT DISTINCT city FROM employees;
```

---

**基本写法：分组聚合**
`SELECT <列>, <聚合函数>(<列>) FROM <表名> GROUP BY <列>`

```sql
-- 分组聚合
SELECT city, AVG(salary) as avg_salary, COUNT(*) as cnt
FROM employees
GROUP BY city;
```

---

**基本写法：Having 过滤**
`SELECT <列>, <聚合函数>(<列>) FROM <表名> GROUP BY <列> HAVING <条件>`

```sql
-- 分组后过滤
SELECT city, AVG(salary) as avg_salary
FROM employees
GROUP BY city
HAVING AVG(salary) > 10000;
```

---

## Join 查询

**基本写法：内连接**
`SELECT * FROM <表1> INNER JOIN <表2> ON <条件>`

```sql
-- 内连接
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;
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
`SELECT * FROM <表1> FULL OUTER JOIN <表2> ON <条件>`

```sql
-- 全外连接
SELECT e.name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.id;
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

**基本写法：EXISTS 子查询**
`SELECT * FROM <表1> WHERE EXISTS (SELECT ... WHERE ...)`

```sql
-- EXISTS 子查询
SELECT * FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.id = e.dept_id AND d.name = '技术部');
```

---

**基本写法：CTE 公共表表达式**
`WITH <表名> AS (SELECT ...) SELECT * FROM <表名>`

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

## 窗口函数

**基本写法：行号**
`ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <列>)`

```sql
-- 按部门分组按薪资降序编号
SELECT name, dept_id, salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rank
FROM employees;
```

---

**基本写法：排名**
`RANK() OVER (PARTITION BY <列> ORDER BY <列>)`

```sql
-- 排名（有并列，有间隔）
SELECT name, salary,
    RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;
```

---

**基本写法：密集排名**
`DENSE_RANK() OVER (PARTITION BY <列> ORDER BY <列>)`

```sql
-- 密集排名（有并列，无间隔）
SELECT name, salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM employees;
```

---

**基本写法：累积求和**
`SUM(<列>) OVER (PARTITION BY <列> ORDER BY <列>)`

```sql
-- 累积求和
SELECT name, dept_id, salary,
    SUM(salary) OVER (PARTITION BY dept_id ORDER BY salary) as cumsum
FROM employees;
```

---

**基本写法：偏移函数**
`LAG(<列>, <偏移>) OVER (ORDER BY <列>)`

```sql
-- 获取前一行的值
SELECT name, salary,
    LAG(salary, 1) OVER (ORDER BY salary) as prev_salary
FROM employees;
```

---

## 数据插入

**基本写法：插入数据**
`INSERT INTO <表名> VALUES (<值1>, <值2>, ...)`

```sql
-- 插入单行
INSERT INTO employees VALUES (1, 'Alice', 30, 15000.0);
-- 插入多行
INSERT INTO employees VALUES
    (2, 'Bob', 25, 12000.0),
    (3, 'Charlie', 35, 20000.0);
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

**基本写法：插入分区**
`INSERT INTO <表名> PARTITION (<分区列>=<值>) SELECT ...`

```sql
-- 插入指定分区
INSERT INTO sales PARTITION (year=2024, month=1)
SELECT id, amount FROM temp_sales;
```

---

## 视图

**基本写法：创建视图**
`CREATE VIEW <视图名> AS SELECT ...`

```sql
-- 创建视图
CREATE VIEW high_salary_employees AS
SELECT * FROM employees WHERE salary > 15000;
```

---

**基本写法：创建临时视图**
`CREATE TEMP VIEW <视图名> AS SELECT ...`

```sql
-- 创建临时视图（会话级别）
CREATE TEMP VIEW dept_stats AS
SELECT dept_id, AVG(salary) as avg_sal FROM employees GROUP BY dept_id;
```

---

**基本写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名>`

```sql
-- 删除视图
DROP VIEW IF EXISTS high_salary_employees;
```

---

## 函数使用

**基本写法：字符串函数**
`SELECT <函数>(<列>) FROM <表名>`

```sql
-- 字符串函数
SELECT UPPER(name), LENGTH(name), SUBSTRING(name, 1, 3) FROM employees;
SELECT CONCAT(name, '-', city) as info FROM employees;
```

---

**基本写法：日期函数**
`SELECT <日期函数>(<列>) FROM <表名>`

```sql
-- 日期函数
SELECT CURRENT_DATE(), CURRENT_TIMESTAMP();
SELECT YEAR(hire_date), MONTH(hire_date), DAY(hire_date) FROM employees;
SELECT DATEDIFF(CURRENT_DATE(), hire_date) as days FROM employees;
```

---

**基本写法：数学函数**
`SELECT <数学函数>(<列>) FROM <表名>`

```sql
-- 数学函数
SELECT ROUND(salary, 2), ABS(salary - avg_sal), SQRT(salary) FROM employees;
```

---

**基本写法：条件函数**
`SELECT CASE WHEN <条件> THEN <值> ELSE <值> END FROM <表名>`

```sql
-- 条件表达式
SELECT name, salary,
    CASE
        WHEN salary > 20000 THEN '高薪'
        WHEN salary > 10000 THEN '中薪'
        ELSE '低薪'
    END as level
FROM employees;
```
