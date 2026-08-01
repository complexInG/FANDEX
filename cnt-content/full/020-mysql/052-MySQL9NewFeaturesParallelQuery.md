---
order: 91
title: MySQL9新特性与并行查询
module: mysql
category: MySQL
difficulty: intermediate
description: 'MySQL 9.x新特性：VECTOR向量类型、JSON增强、窗口函数完善、CTE递归、函数索引、并行查询优化'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/数据加密
  - mysql/索引与执行计划
  - mysql/VECTOR向量类型
  - mysql/JSON模式验证与聚合函数
prerequisites:
  - mysql/语法速查
---

## 1. MySQL 9.x 概述

MySQL 9.x 是 MySQL 数据库的最新主要版本，引入了大量面向现代应用场景的特性，包括 AI 向量搜索支持、JSON 功能增强、查询优化器改进和并行查询能力提升。本章系统梳理 MySQL 9.x 的核心新特性及并行查询机制。

### 1.1 版本演进路线

| 版本      | 发布时间 | 核心特性                                   |
| :-------- | :------- | :----------------------------------------- |
| MySQL 8.0 | 2018     | 窗口函数、CTE、JSON增强、角色管理          |
| MySQL 8.4 | 2024     | LTS版本、性能改进、直方图增强              |
| MySQL 9.0 | 2024.7   | VECTOR类型、自动JSON模式验证、并行查询增强 |
| MySQL 9.x | 2025+    | 持续增强向量搜索、优化器改进               |

### 1.2 MySQL 9.x 安装与版本确认

```sql
-- 查看当前版本
SELECT VERSION();

-- 查看支持的特性
SELECT * FROM performance_schema.global_variables
WHERE VARIABLE_NAME LIKE '%vector%';

-- 检查并行查询支持
SHOW VARIABLES LIKE '%parallel%';
```

## 2. VECTOR 向量类型

### 2.1 向量类型基础

MySQL 9.0 引入 `VECTOR` 数据类型，原生支持向量数据的存储与检索，为 AI/ML 应用场景（语义搜索、推荐系统、相似度匹配）提供数据库层面的支持。

```sql
-- 创建包含向量列的表
CREATE TABLE product_embeddings (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200),
    description TEXT,
    embedding VECTOR(768)   -- 768维向量（如 BERT 模型输出）
);

-- 插入向量数据（以 JSON 数组格式传入）
INSERT INTO product_embeddings VALUES (
    1,
    '无线蓝牙耳机',
    '高品质音效，降噪功能',
    '[0.123, -0.456, 0.789, ..., 0.012]'  -- 768维向量
);

-- 查询向量数据（返回 JSON 数组格式）
SELECT product_id, product_name,
       VECTOR_TO_STRING(embedding) AS embedding_str
FROM product_embeddings;
```

### 2.2 向量距离函数

```sql
-- 欧几里得距离（L2距离）
SELECT product_id, product_name,
       DISTANCE(embedding, '[0.1, -0.5, 0.8, ...]') AS distance
FROM product_embeddings
ORDER BY distance ASC
LIMIT 10;

-- 余弦相似度
SELECT product_id, product_name,
       1 - DISTANCE(embedding, '[0.1, -0.5, 0.8, ...]', 'COSINE') AS similarity
FROM product_embeddings
ORDER BY similarity DESC
LIMIT 10;

-- 内积（点积）
SELECT product_id, product_name,
       DISTANCE(embedding, '[0.1, -0.5, 0.8, ...]', 'DOT') AS dot_product
FROM product_embeddings
ORDER BY dot_product DESC
LIMIT 10;
```

### 2.3 向量索引

```sql
-- 创建向量索引以加速近似最近邻搜索
ALTER TABLE product_embeddings
ADD VECTOR INDEX idx_embedding (embedding)
WITH (DISTANCE = 'COSINE', M = 16, EF_CONSTRUCTION = 256);

-- 使用向量索引的近似搜索
SELECT product_id, product_name,
       1 - DISTANCE(embedding, '[0.1, -0.5, 0.8, ...]', 'COSINE') AS similarity
FROM product_embeddings
ORDER BY similarity DESC
LIMIT 20;

-- 查看向量索引信息
SELECT * FROM information_schema.VECTOR_INDEXES
WHERE TABLE_NAME = 'product_embeddings';
```

### 2.4 向量类型应用场景

```sql
-- 语义搜索：查找与查询文本语义相似的商品
CREATE TABLE search_cache (
    query_hash VARCHAR(64) PRIMARY KEY,
    query_text TEXT,
    query_embedding VECTOR(768),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 推荐系统：基于用户偏好向量推荐商品
CREATE TABLE user_profiles (
    user_id INT PRIMARY KEY,
    preference_vector VECTOR(256),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 相似度匹配：图像特征向量检索
CREATE TABLE image_features (
    image_id BIGINT PRIMARY KEY,
    feature_vector VECTOR(512),
    image_url VARCHAR(500)
);
```

## 3. JSON 功能增强

### 3.1 自动 JSON 模式验证

MySQL 9.0 支持为 JSON 列定义 JSON Schema，自动验证插入和更新的 JSON 数据是否符合预定义的结构。

```sql
-- 创建带 JSON Schema 验证的表
CREATE TABLE user_profiles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    profile JSON,
    CHECK (
        JSON_SCHEMA_VALID(
            '{
                "type": "object",
                "required": ["name", "email"],
                "properties": {
                    "name": {"type": "string", "minLength": 1},
                    "email": {"type": "string", "format": "email"},
                    "age": {"type": "integer", "minimum": 0, "maximum": 150},
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                }
            }',
            profile
        )
    )
);

-- 合法数据：包含必填字段且类型正确
INSERT INTO user_profiles (profile) VALUES (
    '{"name": "张三", "email": "zhang@example.com", "age": 28, "tags": ["vip"]}'
);

-- 非法数据：缺少必填字段 → 报错
INSERT INTO user_profiles (profile) VALUES (
    '{"name": "李四"}'
);
-- ERROR: Check constraint failed

-- 非法数据：类型不匹配 → 报错
INSERT INTO user_profiles (profile) VALUES (
    '{"name": "王五", "email": "wang@example.com", "age": "not_a_number"}'
);
```

### 3.2 JSON 聚合函数

```sql
-- JSON_ARRAYAGG：将多行值聚合为 JSON 数组
SELECT department,
       JSON_ARRAYAGG(JSON_OBJECT('name', name, 'salary', salary)) AS employees
FROM employees
GROUP BY department;

-- JSON_OBJECTAGG：将键值对聚合为 JSON 对象
SELECT department,
       JSON_OBJECTAGG(name, salary) AS salary_map
FROM employees
GROUP BY department;

-- MySQL 9.x 增强的 JSON_TABLE 嵌套路径
SELECT jt.*
FROM orders,
     JSON_TABLE(
         order_items,
         '$[*]' COLUMNS(
             item_id VARCHAR(20) PATH '$.id',
             quantity INT PATH '$.qty',
             NESTED PATH '$.details[*]' COLUMNS(
                 detail_name VARCHAR(50) PATH '$.name',
                 detail_value VARCHAR(100) PATH '$.value'
             )
         )
     ) AS jt;
```

### 3.3 JSON 空间优化

```sql
-- MySQL 9.x 对 JSON 存储进行了优化
-- JSON 列的存储更紧凑，部分更新不再重写整个 JSON 文档

-- 查看表的 JSON 列信息
SELECT TABLE_NAME, COLUMN_NAME, COLUMN_TYPE
FROM information_schema.COLUMNS
WHERE DATA_TYPE = 'json'
AND TABLE_SCHEMA = 'your_database';

-- JSON 部分更新（in-place update）
UPDATE user_profiles
SET profile = JSON_SET(profile, '$.age', 29)
WHERE id = 1;
-- 如果修改的字段大小未超出原值，可原地更新，避免重写整个 JSON
```

## 4. 窗口函数完善

### 4.1 MySQL 9.x 窗口函数增强

```sql
-- 窗口函数中的 IGNORE NULLS 支持
SELECT
    employee_id,
    department,
    salary,
    FIRST_VALUE(salary) IGNORE NULLS OVER (
        PARTITION BY department ORDER BY hire_date
    ) AS first_salary,
    LAST_VALUE(salary) IGNORE NULLS OVER (
        PARTITION BY department ORDER BY hire_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_salary
FROM employees;

-- 增强的 NTILE 函数
SELECT
    product_id,
    category,
    price,
    NTILE(4) OVER (PARTITION BY category ORDER BY price) AS price_quartile
FROM products;

-- 增强的 GROUPS 窗口帧
SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
        GROUPS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS moving_sum
FROM daily_sales;
```

### 4.2 窗口函数性能优化

```sql
-- 使用窗口函数替代自连接，提升性能
-- 旧写法：自连接
SELECT e1.employee_id, e1.salary,
       (SELECT AVG(e2.salary)
        FROM employees e2
        WHERE e2.department = e1.department) AS dept_avg
FROM employees e1;

-- 新写法：窗口函数（更高效）
SELECT
    employee_id,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg,
    salary - AVG(salary) OVER (PARTITION BY department) AS diff_from_avg
FROM employees;
```

## 5. CTE 与递归查询

### 5.1 通用表表达式 (CTE)

```sql
-- 非递归 CTE：简化复杂查询
WITH monthly_revenue AS (
    SELECT
        DATE_FORMAT(order_date, '%Y-%m') AS month,
        SUM(amount) AS revenue,
        COUNT(*) AS order_count
    FROM orders
    WHERE status = 'completed'
    GROUP BY month
),
monthly_avg AS (
    SELECT AVG(revenue) AS avg_revenue FROM monthly_revenue
)
SELECT
    m.month,
    m.revenue,
    m.order_count,
    a.avg_revenue,
    ROUND((m.revenue - a.avg_revenue) / a.avg_revenue * 100, 2) AS pct_diff
FROM monthly_revenue m
CROSS JOIN monthly_avg a
ORDER BY m.month;
```

### 5.2 递归 CTE

```sql
-- 组织架构层级查询
WITH RECURSIVE org_hierarchy AS (
    -- 锚点查询：顶级管理者
    SELECT
        employee_id,
        name,
        manager_id,
        1 AS level,
        CAST(name AS CHAR(500)) AS path
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- 递归查询：逐级展开
    SELECT
        e.employee_id,
        e.name,
        e.manager_id,
        h.level + 1 AS level,
        CONCAT(h.path, ' → ', e.name) AS path
    FROM employees e
    INNER JOIN org_hierarchy h ON e.manager_id = h.employee_id
)
SELECT * FROM org_hierarchy ORDER BY level, path;

-- 物料清单 (BOM) 展开
WITH RECURSIVE bom AS (
    SELECT
        parent_part,
        child_part,
        quantity,
        1 AS level
    FROM parts_relation
    WHERE parent_part = 'PRODUCT-A'

    UNION ALL

    SELECT
        p.parent_part,
        p.child_part,
        p.quantity,
        b.level + 1
    FROM parts_relation p
    INNER JOIN bom b ON p.parent_part = b.child_part
)
SELECT
    level,
    parent_part,
    child_part,
    quantity,
    RPAD('', level * 2, '  ') || child_part AS indented_name
FROM bom
ORDER BY level, parent_part;
```

### 5.3 递归 CTE 注意事项

```sql
-- 设置递归深度限制（防止无限递归）
SET cte_max_recursion_depth = 1000;  -- 默认1000

-- 使用 LIMIT 控制递归层级
WITH RECURSIVE tree AS (
    SELECT id, parent_id, name, 1 AS lvl
    FROM categories WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.parent_id, c.name, t.lvl + 1
    FROM categories c JOIN tree t ON c.parent_id = t.id
    WHERE t.lvl < 5  -- 限制最大5层
)
SELECT * FROM tree;
```

## 6. 函数索引与不可见索引

### 6.1 函数索引

MySQL 8.0+ 支持基于函数表达式的索引，解决列上函数运算导致索引失效的问题。

```sql
-- 传统方式：WHERE 条件中使用函数导致索引失效
SELECT * FROM users WHERE YEAR(created_at) = 2024;
-- 无法使用 created_at 上的索引

-- 函数索引：为函数表达式创建索引
CREATE INDEX idx_year ON users ((YEAR(created_at)));
SELECT * FROM users WHERE YEAR(created_at) = 2024;
-- 可以使用 idx_year 索引

-- 常用函数索引场景
-- 大小写不敏感查询
CREATE INDEX idx_lower_name ON users ((LOWER(name)));
SELECT * FROM users WHERE LOWER(name) = 'zhang san';

-- JSON 字段索引
CREATE INDEX idx_json_age ON user_profiles ((CAST(profile->'$.age' AS UNSIGNED)));
SELECT * FROM user_profiles WHERE CAST(profile->'$.age' AS UNSIGNED) > 25;

-- 计算列索引
CREATE INDEX idx_full_name ON employees ((CONCAT(first_name, ' ', last_name)));
SELECT * FROM employees WHERE CONCAT(first_name, ' ', last_name) = 'Zhang San';
```

### 6.2 不可见索引

不可见索引不会被优化器使用，但仍然维护更新，用于安全地测试删除索引的影响。

```sql
-- 创建不可见索引
CREATE INDEX idx_status ON orders(status) INVISIBLE;

-- 将已有索引设为不可见
ALTER TABLE orders ALTER INDEX idx_status SET INVISIBLE;

-- 恢复可见
ALTER TABLE orders ALTER INDEX idx_status SET VISIBLE;

-- 会话级别强制使用不可见索引（仅用于测试）
SET SESSION optimizer_switch = 'use_invisible_indexes=on';

-- 验证索引是否被使用
EXPLAIN SELECT * FROM orders WHERE status = 'shipped';
-- 不可见索引不会出现在执行计划中
```

## 7. 直方图统计

### 7.1 直方图基础

直方图提供列值分布的统计信息，帮助优化器在索引不可用时做出更好的执行计划选择。

```sql
-- 创建直方图
ANALYZE TABLE orders UPDATE HISTOGRAM ON status, customer_id WITH 100 BUCKETS;

-- 查看直方图信息
SELECT TABLE_NAME, COLUMN_NAME, HISTOGRAM
FROM information_schema.COLUMN_STATISTICS
WHERE TABLE_SCHEMA = 'your_database';

-- 删除直方图
ANALYZE TABLE orders DROP HISTOGRAM ON status;

-- 查看直方图详细内容
SELECT JSON_PRETTY(HISTOGRAM) AS histogram_detail
FROM information_schema.COLUMN_STATISTICS
WHERE TABLE_NAME = 'orders' AND COLUMN_NAME = 'status';
```

### 7.2 直方图适用场景

```sql
-- 场景1：低基数列的选择性评估
-- status 列只有几个值，直方图帮助优化器判断过滤性
ANALYZE TABLE orders UPDATE HISTOGRAM ON status WITH 10 BUCKETS;

-- 场景2：关联查询的行数估算
-- 无索引的关联列，直方图改善估算精度
ANALYZE TABLE order_items UPDATE HISTOGRAM ON product_id WITH 256 BUCKETS;

-- 场景3：范围查询的选择性
-- 价格范围查询，直方图帮助估算匹配行数
ANALYZE TABLE products UPDATE HISTOGRAM ON price WITH 100 BUCKETS;

-- 对比执行计划
EXPLAIN FORMAT=JSON
SELECT * FROM orders WHERE status = 'shipped';
-- 查看 "filtered" 字段，直方图可改善此估算值
```

## 8. 并行查询

### 8.1 InnoDB 并行读线程

MySQL 9.x 增强了 InnoDB 的并行读取能力，利用多线程并行扫描大表，显著提升全表扫描和范围查询的性能。

```sql
-- 配置并行读线程数
SET SESSION innodb_parallel_read_threads = 4;  -- 默认4，最大256

-- 并行扫描大表
SET innodb_parallel_read_threads = 8;
SELECT COUNT(*) FROM large_table;  -- 使用8个线程并行扫描

-- 并行范围查询
SET innodb_parallel_read_threads = 4;
SELECT SUM(amount) FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';
```

### 8.2 并行排序

```sql
-- 大结果集的 ORDER BY 可利用并行排序
SET SESSION innodb_parallel_read_threads = 4;

-- 并行排序 + LIMIT
SELECT * FROM large_table
ORDER BY created_at DESC
LIMIT 1000;

-- 并行排序 + 聚合
SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;
```

### 8.3 并行索引扫描

```sql
-- 并行索引范围扫描
SET SESSION innodb_parallel_read_threads = 4;

SELECT * FROM orders
FORCE INDEX (idx_order_date)
WHERE order_date BETWEEN '2024-01-01' AND '2024-06-30'
ORDER BY order_date;

-- 并行覆盖索引扫描
SELECT customer_id, COUNT(*) AS order_count
FROM orders
FORCE INDEX (idx_customer_date)
WHERE order_date >= '2024-01-01'
GROUP BY customer_id
ORDER BY order_count DESC;
```

### 8.4 并行 GROUP BY 优化

```sql
-- 并行聚合查询
SET SESSION innodb_parallel_read_threads = 8;

-- 大表分组聚合
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    region,
    COUNT(*) AS order_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY month, region
ORDER BY month, total_amount DESC;

-- 并行 DISTINCT
SELECT DISTINCT category FROM large_product_table;
```

### 8.5 并行查询监控与调优

```sql
-- 查看并行查询执行信息
EXPLAIN FORMAT=TREE
SELECT COUNT(*) FROM large_table;
-- 输出中会显示 "parallel" 相关信息

-- 监控并行线程使用
SELECT * FROM performance_schema.threads
WHERE NAME LIKE '%parallel%';

-- 并行查询参数调优
SET GLOBAL innodb_parallel_read_threads = 8;        -- 全局默认并行线程数
SET SESSION innodb_parallel_read_threads = 16;      -- 会话级别覆盖

-- 并行查询适用场景
--  大表全表扫描
--  大范围索引扫描
--  聚合查询（COUNT/SUM/AVG）
--  排序查询
--  小表查询（并行开销大于收益）
--  高并发 OLTP（线程资源有限）
--  包含子查询的复杂查询
```

## 9. 其他 MySQL 9.x 新特性

### 9.1 性能改进

```sql
-- 改进的查询优化器
-- 优化器现在能更好地处理 OR 条件
SELECT * FROM orders
WHERE customer_id = 1001 OR status = 'urgent';
-- 9.x 可能使用 index merge 优化

-- EXPLAIN ANALYZE（实际执行并返回耗时）
EXPLAIN ANALYZE
SELECT * FROM orders WHERE customer_id = 1001;
-- 返回实际执行时间、行数等信息
```

### 9.2 DDL 增强

```sql
-- 原子 DDL：DDL 操作要么完全成功，要么完全回滚
-- MySQL 8.0+ 支持，9.x 进一步增强
CREATE TABLE test_atomic (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
-- 如果创建失败，不会留下残留文件

-- 在线 DDL 改进
ALTER TABLE large_table
ADD COLUMN new_col VARCHAR(50),
ALGORITHM=INPLACE, LOCK=NONE;
-- 9.x 减少了在线 DDL 期间的锁等待
```

### 9.3 权限与安全增强

```sql
-- MySQL 9.0 默认使用 caching_sha2_password
-- 创建用户时指定认证插件
CREATE USER 'app_user'@'%'
IDENTIFIED WITH caching_sha2_password BY 'StrongP@ss123!';

-- 角色管理增强
CREATE ROLE 'read_only', 'read_write', 'admin';
GRANT SELECT ON app_db.* TO 'read_only';
GRANT SELECT, INSERT, UPDATE ON app_db.* TO 'read_write';
GRANT ALL ON app_db.* TO 'admin';

-- 将角色赋予用户
GRANT 'read_write' TO 'developer1'@'%';

-- 用户激活角色
SET ROLE 'read_write';

-- 设置默认角色
ALTER USER 'developer1'@'%' DEFAULT ROLE 'read_write';
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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| MySQL 概述与数据库设计 | 001-MySQLOverviewDatabaseDesign | 本文的前置基础 |
| MySQL 环境搭建 | 002-MySQLEnvSetup | 本文的前置基础 |
| MySQL 数据类型与约束 | 003-MySQLDataTypeConstraint | 本文的并列主题 |
| SQL 数据定义与高级对象 | 004-SQLDataDefinitionAdvanced | 本文的并列主题 |
| MyISAM存储引擎 | 005-MyISAMStorageEngine | 本文的并列主题 |
| SQL 数据操作与查询 | 006-SQLDataOperationQuery | 本文的并列主题 |
| Memory存储引擎 | 007-MemoryStorageEngine | 本文的并列主题 |
| NDB-Cluster | 008-NDBCluster | 本文的并列主题 |
| 聚簇索引与二级索引 | 009-ClusteredIndexSecondaryIndex | 本文的并列主题 |
| 联合索引与最左前缀原则 | 010-CompositeIndexLeftmostPrefixPrinciple | 本文的并列主题 |
| 索引下推 | 011-IndexConditionPushdown | 本文的并列主题 |
| 全文索引 | 012-FullTextIndex | 本文的并列主题 |
| 前缀索引 | 013-PrefixIndex | 本文的并列主题 |
| 索引提示与强制索引 | 014-IndexHintForceIndex | 本文的并列主题 |
| 索引统计信息与直方图 | 015-IndexStatsHistogram | 本文的并列主题 |
| SQL 函数与高级查询 | 016-SQLFunctionAndAdvancedQuery | 本文的并列主题 |
| 索引失效场景 | 017-IndexFailureScene | 本文的并列主题 |
| EXPLAIN输出详解 | 018-EXPLAINDetailed | 本文的并列主题 |
| 慢查询日志 | 019-SlowQueryLog | 本文的并列主题 |
| 优化器追踪 | 020-OptimizerTrace | 本文的性能延伸 |
| 子查询优化 | 021-SubqueryOptimization | 本文的性能延伸 |
| 派生表优化 | 022-DerivedTableOptimization | 本文的性能延伸 |
| GROUP-BY与ORDER-BY优化 | 023-GroupByOrderByOptimization | 本文的性能延伸 |
| JOIN算法 | 024-JOINAlgorithm | 本文的并列主题 |
| 事务隔离级别底层实现 | 025-TransactionIsolationImplementation | 本文的并列主题 |
| MVCC原理 | 026-MVCCPrinciple | 本文的原理深化 |
| 多表联查详解 | 027-MultiTableJoinDetailed | 本文的并列主题 |
| 锁分类 | 028-LockClassification | 本文的并列主题 |
| 死锁检测与处理 | 029-DeadlockDetectionHandling | 本文的并列主题 |
| 分布式事务 | 030-DistributedTransaction | 本文的并列主题 |
| 二进制日志 | 031-Binlog | 本文的并列主题 |
| 重做日志 | 032-RedoLog | 本文的并列主题 |
| 撤销日志 | 033-UndoLog | 本文的并列主题 |
| 日志系统 | 034-LogSystem | 本文的并列主题 |
| 逻辑备份 | 035-LogicalBackup | 本文的并列主题 |
| 物理备份 | 036-PhysicalBackup | 本文的并列主题 |
| 基于时间点恢复 | 037-PITR | 本文的并列主题 |
| 主从复制 | 038-Replication | 本文的并列主题 |
| 进阶查询与多表操作 | 039-AdvancedQueryMultiTableOperation | 本文的并列主题 |
| GTID | 040-GTID | 本文的并列主题 |
| 并行复制 | 041-ParallelReplication | 本文的并列主题 |
| 组复制 | 042-GroupReplication | 本文的并列主题 |
| InnoDB-Cluster | 043-InnoDBCluster | 本文的并列主题 |
| 分区表 | 044-PartitionedTable | 本文的并列主题 |
| 分库分表中间件 | 045-ShardingMiddleware | 本文的并列主题 |
| 账户与权限管理 | 046-AccountPermissionManagement | 本文的安全延伸 |
| SSL-TLS加密 | 047-SSLEncryption | 本文的安全延伸 |
| 防火墙插件 | 048-FirewallPlugin | 本文的并列主题 |
| InnoDB体系架构 | 049-InnoDBSystemArchitecture | 本文的原理深化 |
| 数据加密 | 050-DataEncryption | 本文的安全延伸 |
| MySQL 索引与执行计划 | 051-MySQLIndexExecutionPlan | 本文的并列主题 |
| MySQL9新特性与并行查询 | 052-MySQL9NewFeaturesParallelQuery | 本文自身 |
| VECTOR向量类型 | 053-VectorType | 本文的并列主题 |
| JSON模式验证与聚合函数 | 054-JSONSchemaValidationAggregate | 本文的并列主题 |
| 复制与高可用 | 055-ReplicationHA | 本文的并列主题 |
| 不可见索引 | 056-InvisibleIndex | 本文的并列主题 |
| 性能调优与安全 | 057-PerformanceTuningSecurity | 本文的性能延伸 |
| 函数索引 | 058-FunctionalIndex | 本文的并列主题 |
| 存储过程与函数 | 059-StoredProcedureAndFunction | 本文的并列主题 |
| MVCC快照读与当前读 | 060-MVCCSnapshotCurrentRead | 本文的并列主题 |
| 索引原理与性能优化 | 061-IndexPrinciplePerformanceOptimization | 本文的性能延伸 |
| 触发器与事件 | 062-TriggerEvent | 本文的并列主题 |
| Redo与Undo与Binlog写入时机 | 063-RedoUndoBinlogWriteTiming | 本文的并列主题 |
| 两阶段提交 | 064-TwoPhaseCommit | 本文的并列主题 |
| 间隙锁与临键锁解决幻读 | 065-GapLockNextKeyLockSolutionPhantomRead | 本文的并列主题 |
| 主从复制延迟原因与解决 | 066-ReplicationDelayCauseSolution | 本文的并列主题 |
| 分库分表策略 | 067-ShardingStrategy | 本文的并列主题 |
| JSON类型与JSON-TABLE | 068-JSONTypeJSONTable | 本文的并列主题 |
| 事务与锁机制 | 069-TransactionLockMechanism | 本文的原理深化 |
| MySQL 配置与运维 | 070-MySQLConfigOps | 本文的并列主题 |
| MySQL 快速查阅 | 071-MySQLQuickLookup | 本文的并列主题 |
| MySQL 控制器与应用 | 072-MySQLControlApplication | 本文的并列主题 |
| SQL 注入基础与检测 | 073-SQLInjectionBasicsDetection | 本文的前置基础 |
| SQL 注入攻击类型与实战 | 074-SQLInjectionAttackTypePractice | 本文的综合应用 |
| SQL 注入防御策略 | 075-SQLInjectionDefenseStrategy | 本文的并列主题 |
| MySQL 项目示例：电商数据库设计 | 076-MySQLProjectExampleDatabaseDesign | 本文的综合应用 |
| MySQL 理论知识点 | 077-MySQLTheoryKnowledge | 本文的并列主题 |
| MySQL DDL 数据定义 | 078-DDL | 本文的并列主题 |
| MySQL DML 数据操作 | 079-DML | 本文的并列主题 |
| MySQL DQL 查询速查 | 080-DQL | 本文的并列主题 |
| MySQL 索引管理 | 081-IndexManagement | 本文的并列主题 |
| MySQL 用户与权限管理 | 082-UserPermission | 本文的安全延伸 |
| MySQL CLI 命令 | 083-CLI | 本文的并列主题 |
| mysqladmin 管理命令 语法速查手册 | 084-Mysqladmin | 本文的并列主题 |
| 视图 语法速查手册 | 085-View | 本文的并列主题 |
| 事件调度器 语法速查手册 | 086-EventScheduler | 本文的并列主题 |
| 字符集与排序规则 语法速查手册 | 087-CharsetCollation | 本文的并列主题 |
