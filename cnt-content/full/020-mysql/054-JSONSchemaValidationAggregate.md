---
order: 92
title: JSON模式验证与聚合函数
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL JSON模式验证与JSON聚合函数：JSON_SCHEMA_VALID、JSON_ARRAYAGG、JSON_OBJECTAGG'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/MySQL9新特性与并行查询
  - mysql/VECTOR向量类型
  - mysql/复制与高可用
  - mysql/不可见索引
prerequisites:
  - mysql/语法速查
---
## 1. JSON 模式验证

### 1.1 JSON_SCHEMA_VALID

```sql
-- 定义 JSON Schema
SET @schema = '{
    "type": "object",
    "required": ["name", "age"],
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "age": {"type": "integer", "minimum": 0},
        "email": {"type": "string", "format": "email"}
    }
}';

-- 验证 JSON 数据
SELECT JSON_SCHEMA_VALID(@schema, '{"name": "Alice", "age": 30}');
-- 返回 1（有效）

SELECT JSON_SCHEMA_VALID(@schema, '{"name": "Bob"}');
-- 返回 0（缺少 age）

-- 在 CHECK 约束中使用
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data JSON,
    CHECK (JSON_SCHEMA_VALID('{
        "type": "object",
        "required": ["name"],
        "properties": {"name": {"type": "string"}}
    }', data))
);
```

### 1.2 JSON_SCHEMA_VALIDATION_REPORT

```sql
-- 获取详细的验证报告
SELECT JSON_SCHEMA_VALIDATION_REPORT(@schema, '{"name": "Bob"}');
-- 返回验证失败的详细信息
```

## 2. JSON 聚合函数

### 2.1 JSON_ARRAYAGG

```sql
-- 将多行的值聚合为 JSON 数组
SELECT dept_id, JSON_ARRAYAGG(name) AS employee_names
FROM employees
GROUP BY dept_id;

-- 结果：
-- dept_id | employee_names
-- 1       | ["Alice", "Bob", "Charlie"]
-- 2       | ["David", "Eve"]
```

### 2.2 JSON_OBJECTAGG

```sql
-- 将键值对聚合为 JSON 对象
SELECT dept_id, JSON_OBJECTAGG(name, salary) AS salary_map
FROM employees
GROUP BY dept_id;

-- 结果：
-- dept_id | salary_map
-- 1       | {"Alice": 50000, "Bob": 60000, "Charlie": 55000}
```

## 3. JSON 表函数

### 3.1 JSON_TABLE

```sql
-- 将 JSON 数组展开为关系表
SELECT jt.*
FROM orders,
JSON_TABLE(items, '$[*]' COLUMNS (
    product_id INT PATH '$.product_id',
    quantity INT PATH '$.quantity',
    price DECIMAL(10,2) PATH '$.price'
)) AS jt;

-- 嵌套列
SELECT jt.name, jt.street, jt.city
FROM users,
JSON_TABLE(address, '$' COLUMNS (
    name VARCHAR(100) PATH '$.name',
    NESTED PATH '$.address' COLUMNS (
        street VARCHAR(200) PATH '$.street',
        city VARCHAR(100) PATH '$.city'
    )
)) AS jt;
```
## 聚合函数

**单行写法：COUNT 计数**
`SELECT COUNT(<列>) FROM <表名>;`
```sql
-- 统计用户总数
SELECT COUNT(*) AS total FROM users;
```

**单行写法：COUNT 去重计数**
`SELECT COUNT(DISTINCT <列>) FROM <表名>;`
```sql
-- 统计不重复的城市数量
SELECT COUNT(DISTINCT city) FROM users;
```

**单行写法：SUM 求和**
`SELECT SUM(<列>) FROM <表名>;`
```sql
-- 统计所有订单总金额
SELECT SUM(total_amount) AS total FROM orders;
```

**单行写法：AVG 平均值**
`SELECT AVG(<列>) FROM <表名>;`
```sql
-- 计算用户平均年龄
SELECT AVG(age) AS avg_age FROM users;
```

**单行写法：MAX 最大值**
`SELECT MAX(<列>) FROM <表名>;`
```sql
-- 查询最高订单金额
SELECT MAX(total_amount) AS max_amount FROM orders;
```

**单行写法：MIN 最小值**
`SELECT MIN(<列>) FROM <表名>;`
```sql
-- 查询最低订单金额
SELECT MIN(total_amount) AS min_amount FROM orders;
```

**单行写法：GROUP_CONCAT 分组拼接**
`SELECT GROUP_CONCAT(<列> SEPARATOR '<分隔符>') FROM <表名>;`
```sql
-- 拼接用户名用逗号分隔
SELECT GROUP_CONCAT(username SEPARATOR ',') FROM users;
```

**单行写法：BIT_COUNT 位计数**
`SELECT BIT_COUNT(<列>) FROM <表名>;`
```sql
-- 统计二进制位中 1 的个数
SELECT BIT_COUNT(flags) FROM users;
```

---

## GROUP BY 分组

**换行写法：单列分组**
`SELECT <列>, <聚合函数> FROM <表名> GROUP BY <列>;`
```sql
-- 按状态分组统计用户数
SELECT status, COUNT(*) AS count FROM users GROUP BY status;
```

**换行写法：多列分组**
`SELECT <列1>, <列2>, <聚合> FROM <表名> GROUP BY <列1>, <列2>;`
```sql
-- 按城市和性别分组统计
SELECT city, gender, COUNT(*) AS count FROM users GROUP BY city, gender;
```

**换行写法：按表达式分组**
`SELECT <表达式>, <聚合> FROM <表名> GROUP BY <表达式>;`
```sql
-- 按月份分组统计订单
SELECT DATE_FORMAT(created_at, '%Y-%m') AS month, COUNT(*) AS orders
FROM orders
GROUP BY month;
```

**换行写法：按日期分组**
`SELECT DATE(<列>), <聚合> FROM <表名> GROUP BY DATE(<列>);`
```sql
-- 按天统计订单数量
SELECT DATE(created_at) AS day, COUNT(*) AS cnt
FROM orders
GROUP BY DATE(created_at);
```

---

## HAVING 过滤分组

**换行写法：HAVING 过滤聚合结果**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> HAVING <条件>;`
```sql
-- 查询订单数超过 5 的用户
SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id HAVING cnt > 5;
```

**换行写法：HAVING 多条件**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> HAVING <条件1> AND <条件2>;`
```sql
-- 查询订单数大于 5 且总金额大于 1000 的用户
SELECT user_id, COUNT(*) AS cnt, SUM(total_amount) AS total
FROM orders
GROUP BY user_id
HAVING cnt > 5 AND total > 1000;
```

**换行写法：WHERE 与 HAVING 组合**
`SELECT <列>, <聚合> FROM <表名> WHERE <过滤条件> GROUP BY <列> HAVING <聚合条件>;`
```sql
-- 先过滤再分组再筛选
SELECT user_id, COUNT(*) AS cnt
FROM orders
WHERE status = 1
GROUP BY user_id
HAVING cnt >= 3;
```

---

## WITH ROLLUP 汇总

**换行写法：分组小计与合计**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> WITH ROLLUP;`
```sql
-- 按城市分组统计并显示总计
SELECT IFNULL(city, '总计') AS city, COUNT(*) AS cnt
FROM users
GROUP BY city WITH ROLLUP;
```

**换行写法：多列 ROLLUP 分层汇总**
`SELECT <列1>, <列2>, <聚合> FROM <表名> GROUP BY <列1>, <列2> WITH ROLLUP;`
```sql
-- 按城市和性别分层汇总
SELECT IFNULL(city, '总计') AS city, IFNULL(gender, '小计') AS gender, COUNT(*) AS cnt
FROM users
GROUP BY city, gender WITH ROLLUP;
```

---

## GROUP BY 排序与限制

**换行写法：分组后排序**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> ORDER BY <聚合> DESC;`
```sql
-- 按订单数降序排列用户
SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id ORDER BY cnt DESC;
```

**换行写法：分组排序并限制**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> ORDER BY <聚合> DESC LIMIT <数量>;`
```sql
-- 查询订单数前 10 的用户
SELECT user_id, COUNT(*) AS cnt
FROM orders
GROUP BY user_id
ORDER BY cnt DESC
LIMIT 10;
```

---

## 窗口函数聚合（8.0+）

**换行写法：累计求和**
`SELECT <列>, SUM(<列>) OVER (ORDER BY <列>) FROM <表名>;`
```sql
-- 按日期累计求和销售额
SELECT order_date, amount,
  SUM(amount) OVER (ORDER BY order_date) AS cumulative
FROM daily_sales;
```

**换行写法：分组排名**
`SELECT <列>, ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <列>) FROM <表名>;`
```sql
-- 每个部门按薪资排名
SELECT name, dept_id, salary,
  ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
FROM employees;
```

**换行写法：分组占比**
`SELECT <列>, <列> / SUM(<列>) OVER (PARTITION BY <列>) FROM <表名>;`
```sql
-- 计算每个用户订单金额占该用户总金额的比例
SELECT user_id, order_no, total_amount,
  total_amount / SUM(total_amount) OVER (PARTITION BY user_id) AS ratio
FROM orders;
```

## 参考文献

MySQL 官方文档：https://dev.mysql.com/doc/
MySQL 8.0 参考手册：https://dev.mysql.com/doc/refman/8.0/en/
High Performance MySQL（O'Reilly）：https://www.oreilly.com/library/view/high-performance-mysql/
Percona 博客：https://www.percona.com/blog/

## 延伸阅读

MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 高级课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 InnoDB 日志与崩溃恢复

redo log 记录物理页修改（WAL：先写日志再写数据页），崩溃后重放恢复；环形文件组 + checkpoint 推进。
undo log 记录事务前镜像，支持回滚与 MVCC 版本链；purge 线程清理。
两阶段提交：redo prepare -> binlog -> redo commit，保证两份日志一致，主从不丢数据。
刷盘策略：innodb_flush_log_at_trx_commit=1 最安全（每次提交 fsync），2 每秒刷。

### 13.2 执行计划与优化器

EXPLAIN 关键列：type（const/ref/range/index/ALL）、key、rows、Extra（Using index/Using filesort）。
优化器基于统计信息选计划；analyze table 更新统计；hint（FORCE INDEX）谨慎使用。
排序与分组：filesort 优化为索引序；避免临时表。
慢查询治理流程：慢日志 -> 计划分析 -> 索引/改写 -> 验证。
