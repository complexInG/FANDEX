---
order: 106
title: 'JSON类型与JSON-TABLE'
module: mysql
category: database
difficulty: intermediate
description: 'MySQL JSON 数据类型详解：JSON 存储、查询函数、JSON_TABLE 将 JSON 转为关系表、虚拟列与索引优化。'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/主从复制延迟原因与解决
  - mysql/分库分表策略
  - mysql/事务与锁机制
  - mysql/配置与运维
prerequisites:
  - mysql/语法速查
---
## 1. JSON 数据类型

### 1.1 JSON vs JSON 文本

```sql
-- JSON 类型（MySQL 5.7+）：自动校验、二进制存储、支持部分更新
CREATE TABLE users (
    id       INT PRIMARY KEY,
    profile  JSON          -- 原生 JSON 类型
);

-- JSON 文本（传统方式）：VARCHAR/TEXT 存储，无校验
CREATE TABLE users_old (
    id       INT PRIMARY KEY,
    profile  TEXT          -- 手动存储 JSON 字符串
);
```

| 特性     | JSON 类型            | TEXT 存储  |
| -------- | -------------------- | ---------- |
| 自动校验 | 插入时验证           | 无验证     |
| 存储格式 | 二进制（部分格式化） | 原始字符串 |
| 部分更新 | 支持（JSON_SET 等）  | 需整体替换 |
| 索引     | 虚拟列/函数索引      | 全文索引   |
| 空间开销 | 略大于原始文本       | 原始大小   |

### 1.2 JSON 插入与校验

```sql
-- 有效 JSON
INSERT INTO users VALUES (1, '{"name": "Alice", "age": 30, "tags": ["dev", "go"]}');

-- 无效 JSON → 报错
INSERT INTO users VALUES (2, '{name: Alice}');  -- 缺少引号
-- ERROR 3140 (22032): Invalid JSON text

-- JSON 数组
INSERT INTO users VALUES (3, '[1, 2, 3, "hello", null, true]');

-- 嵌套 JSON
INSERT INTO users VALUES (4, '{
    "name": "Bob",
    "address": {
        "city": "Beijing",
        "zip": "100000"
    },
    "orders": [
        {"id": 1, "amount": 99.9},
        {"id": 2, "amount": 199.9}
    ]
}');
```

## 2. JSON 查询函数

### 2.1 提取函数

```sql
-- JSON_EXTRACT: 提取值（返回 JSON 类型）
SELECT JSON_EXTRACT(profile, '$.name') FROM users WHERE id = 1;
-- "Alice"

-- -> 运算符（JSON_EXTRACT 的简写）
SELECT profile->'$.name' FROM users WHERE id = 1;
-- "Alice"

-- ->> 运算符（提取并取消引号）
SELECT profile->>'$.name' FROM users WHERE id = 1;
-- Alice

-- 提取嵌套值
SELECT profile->>'$.address.city' FROM users WHERE id = 4;
-- Beijing

-- 提取数组元素
SELECT profile->'$.orders[0].amount' FROM users WHERE id = 4;
-- 99.9

-- 提取数组所有元素
SELECT profile->'$.tags[*]' FROM users WHERE id = 1;
-- ["dev", "go"]
```

### 2.2 JSON_PATH 语法

```
$           根元素
.key        对象的 key
[num]       数组的第 num 个元素
[*]         数组所有元素
..          递归下降（MySQL 8.0+）
[last]      数组最后一个元素
[last-1]    数组倒数第二个元素
[to last]   从某位置到末尾
```

### 2.3 修改函数

```sql
-- JSON_SET: 设置值（存在则更新，不存在则创建）
UPDATE users SET profile = JSON_SET(profile, '$.age', 31) WHERE id = 1;

-- JSON_INSERT: 插入值（仅不存在时创建）
UPDATE users SET profile = JSON_INSERT(profile, '$.email', 'alice@example.com') WHERE id = 1;

-- JSON_REPLACE: 替换值（仅存在时更新）
UPDATE users SET profile = JSON_REPLACE(profile, '$.age', 32) WHERE id = 1;

-- JSON_REMOVE: 删除值
UPDATE users SET profile = JSON_REMOVE(profile, '$.tags') WHERE id = 1;

-- JSON_ARRAY_APPEND: 追加数组元素
UPDATE users SET profile = JSON_ARRAY_APPEND(profile, '$.tags', 'java') WHERE id = 1;

-- JSON_MERGE_PATCH: 合并（覆盖同 key）
UPDATE users SET profile = JSON_MERGE_PATCH(profile, '{"age": 33, "level": "senior"}') WHERE id = 1;
```

### 2.4 查询与搜索函数

```sql
-- JSON_CONTAINS: 是否包含指定值
SELECT * FROM users WHERE JSON_CONTAINS(profile->'$.tags', '"dev"');

-- JSON_CONTAINS_PATH: 是否包含指定路径
SELECT * FROM users WHERE JSON_CONTAINS_PATH(profile, 'one', '$.email');

-- JSON_SEARCH: 搜索值返回路径
SELECT JSON_SEARCH(profile, 'one', 'Alice') FROM users;

-- JSON_KEYS: 获取所有 key
SELECT JSON_KEYS(profile) FROM users WHERE id = 1;

-- JSON_LENGTH: 获取长度
SELECT JSON_LENGTH(profile->'$.tags') FROM users WHERE id = 1;

-- JSON_TYPE: 获取类型
SELECT JSON_TYPE(profile->'$.name') FROM users WHERE id = 1;  -- STRING

-- JSON_VALID: 是否有效 JSON
SELECT JSON_VALID('{"a":1}');  -- 1
```

## 3. JSON_TABLE

### 3.1 基本语法

JSON_TABLE（MySQL 8.0+）将 JSON 数组展开为关系表：

```sql
JSON_TABLE(
    json_doc,
    path COLUMNS (
        column_definition
    )
) [AS] alias
```

### 3.2 展开对象数组

```sql
-- 订单表，items 为 JSON 数组
CREATE TABLE orders (
    id    INT PRIMARY KEY,
    items JSON
);

INSERT INTO orders VALUES (1, '[
    {"product_id": 101, "name": "iPhone", "qty": 2, "price": 7999},
    {"product_id": 102, "name": "AirPods", "qty": 1, "price": 1299},
    {"product_id": 103, "name": "Case", "qty": 3, "price": 199}
]');

-- 使用 JSON_TABLE 展开
SELECT
    o.id AS order_id,
    jt.product_id,
    jt.name,
    jt.qty,
    jt.price,
    jt.qty * jt.price AS subtotal
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        qty        INT PATH '$.qty',
        price      DECIMAL(10,2) PATH '$.price'
    )
) AS jt;
```

输出：

```
order_id | product_id | name    | qty | price | subtotal
---------|------------|---------|-----|-------|--------
1        | 101        | iPhone  | 2   | 7999  | 15998
1        | 102        | AirPods | 1   | 1299  | 1299
1        | 103        | Case    | 3   | 199   | 597
```

### 3.3 嵌套展开（NESTED PATH）

```sql
-- 嵌套 JSON 结构
INSERT INTO orders VALUES (2, '[
    {
        "product_id": 201,
        "name": "MacBook",
        "variants": [
            {"color": "Silver", "stock": 10},
            {"color": "Space Gray", "stock": 5}
        ]
    }
]');

SELECT
    o.id,
    jt.product_id,
    jt.name,
    nt.color,
    nt.stock
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        NESTED PATH '$.variants[*]' COLUMNS (
            color VARCHAR(20) PATH '$.color',
            stock INT PATH '$.stock'
        )
    )
) AS jt;
```

### 3.4 ORDINALITY 列

```sql
-- ORDINALITY 自动生成行号
SELECT
    jt.row_num,
    jt.name
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        row_num FOR ORDINALITY,
        name VARCHAR(50) PATH '$.name'
    )
) AS jt
WHERE o.id = 1;
```

### 3.5 处理缺失值

```sql
-- DEFAULT ON ERROR / EMPTY
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        name VARCHAR(50) PATH '$.name',
        discount DECIMAL(5,2) PATH '$.discount' DEFAULT '0.00' ON EMPTY
    )
) AS jt
```

## 4. JSON 索引优化

### 4.1 虚拟列索引

```sql
-- 为 JSON 字段创建虚拟列 + 索引
ALTER TABLE users
ADD COLUMN name_virtual VARCHAR(50)
    GENERATED ALWAYS AS (JSON_UNQUOTE(profile->'$.name')) VIRTUAL,
ADD INDEX idx_name (name_virtual);

-- 查询走索引
SELECT * FROM users WHERE name_virtual = 'Alice';
```

### 4.2 函数索引（MySQL 8.0+）

```sql
-- 直接创建函数索引
ALTER TABLE users
ADD INDEX idx_json_name ((CAST(profile->>'$.name' AS CHAR(50))));
```

### 4.3 多值索引（MySQL 8.0.17+）

```sql
-- 为 JSON 数组创建多值索引
ALTER TABLE users
ADD INDEX idx_tags ((CAST(profile->'$.tags' AS CHAR(50) ARRAY)));

-- 使用 MEMBER OF 查询
SELECT * FROM users WHERE 'dev' MEMBER OF(profile->'$.tags');

-- 使用 JSON_OVERLAPS
SELECT * FROM users WHERE JSON_OVERLAPS(profile->'$.tags', '["dev", "java"]');
```
## JSON 数据类型

**换行写法：创建 JSON 类型列**
`CREATE TABLE <表名> (<列名> INT PRIMARY KEY, <JSON 列名> JSON)`
```sql
-- 创建包含原生 JSON 类型的表
CREATE TABLE users (
    id       INT PRIMARY KEY,
    profile  JSON
);
```

**单行写法：插入有效 JSON 对象**
`INSERT INTO <表名> VALUES (<值>, '<JSON 字符串>')`
```sql
-- 插入有效 JSON 对象数据
INSERT INTO users VALUES (1, '{"name": "Alice", "age": 30, "tags": ["dev", "go"]}');
```

**单行写法：插入 JSON 数组**
`INSERT INTO <表名> VALUES (<值>, '<JSON 数组>')`
```sql
-- 插入 JSON 数组数据
INSERT INTO users VALUES (3, '[1, 2, 3, "hello", null, true]');
```

**换行写法：插入嵌套 JSON**
`INSERT INTO <表名> VALUES (<值>, '<嵌套 JSON 字符串>')`
```sql
-- 插入嵌套结构的 JSON 数据
INSERT INTO users VALUES (4, '{
    "name": "Bob",
    "address": {
        "city": "Beijing",
        "zip": "100000"
    },
    "orders": [
        {"id": 1, "amount": 99.9},
        {"id": 2, "amount": 199.9}
    ]
}');
```

---

## JSON 提取函数

**单行写法：JSON_EXTRACT 提取值**
`JSON_EXTRACT(<JSON 列>, '<路径>')`
```sql
-- 提取 JSON 中的 name 字段值
SELECT JSON_EXTRACT(profile, '$.name') FROM users WHERE id = 1;
```

**单行写法：-> 运算符提取值**
`<JSON 列>->'<路径>'`
```sql
-- 使用 -> 运算符提取 name 字段
SELECT profile->'$.name' FROM users WHERE id = 1;
```

**单行写法：->> 运算符提取并取消引号**
`<JSON 列>->>'<路径>'`
```sql
-- 提取 name 字段并取消引号
SELECT profile->>'$.name' FROM users WHERE id = 1;
```

**单行写法：提取嵌套值**
`<JSON 列>->>'<嵌套路径>'`
```sql
-- 提取嵌套的 address.city 字段
SELECT profile->>'$.address.city' FROM users WHERE id = 4;
```

**单行写法：提取数组元素**
`<JSON 列>->'<数组路径>'`
```sql
-- 提取 orders 数组第一个元素的 amount
SELECT profile->'$.orders[0].amount' FROM users WHERE id = 4;
```

**单行写法：提取数组所有元素**
`<JSON 列>->'<数组路径>[*]'`
```sql
-- 提取 tags 数组的所有元素
SELECT profile->'$.tags[*]' FROM users WHERE id = 1;
```

---

## JSON 修改函数

**单行写法：JSON_SET 设置值**
`JSON_SET(<JSON 列>, '<路径>', <值>[, '<路径>', <值>...])`
```sql
-- 设置 age 字段值（存在则更新不存在则创建）
UPDATE users SET profile = JSON_SET(profile, '$.age', 31) WHERE id = 1;
```

**单行写法：JSON_INSERT 插入值**
`JSON_INSERT(<JSON 列>, '<路径>', <值>)`
```sql
-- 插入 email 字段（仅不存在时创建）
UPDATE users SET profile = JSON_INSERT(profile, '$.email', 'alice@example.com') WHERE id = 1;
```

**单行写法：JSON_REPLACE 替换值**
`JSON_REPLACE(<JSON 列>, '<路径>', <值>)`
```sql
-- 替换 age 字段值（仅存在时更新）
UPDATE users SET profile = JSON_REPLACE(profile, '$.age', 32) WHERE id = 1;
```

**单行写法：JSON_REMOVE 删除值**
`JSON_REMOVE(<JSON 列>, '<路径>')`
```sql
-- 删除 tags 字段
UPDATE users SET profile = JSON_REMOVE(profile, '$.tags') WHERE id = 1;
```

**单行写法：JSON_ARRAY_APPEND 追加数组元素**
`JSON_ARRAY_APPEND(<JSON 列>, '<路径>', <值>)`
```sql
-- 向 tags 数组追加元素
UPDATE users SET profile = JSON_ARRAY_APPEND(profile, '$.tags', 'java') WHERE id = 1;
```

**单行写法：JSON_MERGE_PATCH 合并对象**
`JSON_MERGE_PATCH(<JSON 列>, '<JSON 对象>')`
```sql
-- 合并 JSON 对象（覆盖同 key）
UPDATE users SET profile = JSON_MERGE_PATCH(profile, '{"age": 33, "level": "senior"}') WHERE id = 1;
```

---

## JSON 查询与搜索函数

**单行写法：JSON_CONTAINS 判断包含值**
`JSON_CONTAINS(<JSON 列>, '<JSON 值>'[, '<路径>'])`
```sql
-- 判断 tags 数组是否包含 dev
SELECT * FROM users WHERE JSON_CONTAINS(profile->'$.tags', '"dev"');
```

**单行写法：JSON_CONTAINS_PATH 判断包含路径**
`JSON_CONTAINS_PATH(<JSON 列>, 'one|all', '<路径>'[, '<路径>'...])`
```sql
-- 判断是否包含 email 路径
SELECT * FROM users WHERE JSON_CONTAINS_PATH(profile, 'one', '$.email');
```

**单行写法：JSON_SEARCH 搜索值返回路径**
`JSON_SEARCH(<JSON 列>, 'one|all', '<值>')`
```sql
-- 搜索 Alice 值并返回路径
SELECT JSON_SEARCH(profile, 'one', 'Alice') FROM users;
```

**单行写法：JSON_KEYS 获取所有 key**
`JSON_KEYS(<JSON 列>[, '<路径>'])`
```sql
-- 获取 JSON 对象的所有 key
SELECT JSON_KEYS(profile) FROM users WHERE id = 1;
```

**单行写法：JSON_LENGTH 获取长度**
`JSON_LENGTH(<JSON 列>[, '<路径>'])`
```sql
-- 获取 tags 数组的长度
SELECT JSON_LENGTH(profile->'$.tags') FROM users WHERE id = 1;
```

**单行写法：JSON_TYPE 获取类型**
`JSON_TYPE(<JSON 值>)`
```sql
-- 获取 name 字段的数据类型
SELECT JSON_TYPE(profile->'$.name') FROM users WHERE id = 1;
```

**单行写法：JSON_VALID 判断有效性**
`JSON_VALID('<JSON 字符串>')`
```sql
-- 判断字符串是否为有效 JSON
SELECT JSON_VALID('{"a":1}');
```

---

## JSON_TABLE

**换行写法：JSON_TABLE 基本语法**
`JSON_TABLE(<JSON 文档>, <路径> COLUMNS (<列定义>) ) [AS] <别名>`
```sql
-- 将 JSON 数组展开为关系表
SELECT
    o.id AS order_id,
    jt.product_id,
    jt.name,
    jt.qty,
    jt.price,
    jt.qty * jt.price AS subtotal
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        qty        INT PATH '$.qty',
        price      DECIMAL(10,2) PATH '$.price'
    )
) AS jt;
```

**换行写法：NESTED PATH 嵌套展开**
`NESTED PATH '<路径>' COLUMNS (<列定义>)`
```sql
-- 嵌套 JSON 结构展开
SELECT
    o.id,
    jt.product_id,
    jt.name,
    nt.color,
    nt.stock
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        NESTED PATH '$.variants[*]' COLUMNS (
            color VARCHAR(20) PATH '$.color',
            stock INT PATH '$.stock'
        )
    )
) AS jt;
```

**换行写法：ORDINALITY 列生成行号**
`<列名> FOR ORDINALITY`
```sql
-- 自动生成行号
SELECT
    jt.row_num,
    jt.name
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        row_num FOR ORDINALITY,
        name VARCHAR(50) PATH '$.name'
    )
) AS jt
WHERE o.id = 1;
```

**换行写法：处理缺失值**
`<列名> <类型> PATH '<路径>' DEFAULT '<默认值>' ON EMPTY`
```sql
-- 缺失值使用默认值
SELECT * FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        name VARCHAR(50) PATH '$.name',
        discount DECIMAL(5,2) PATH '$.discount' DEFAULT '0.00' ON EMPTY
    )
) AS jt;
```

---

## JSON 索引优化

**换行写法：虚拟列索引**
`ALTER TABLE <表名> ADD COLUMN <列名> <类型> GENERATED ALWAYS AS (<表达式>) VIRTUAL, ADD INDEX <索引名> (<列名>)`
```sql
-- 为 JSON 字段创建虚拟列加索引
ALTER TABLE users
ADD COLUMN name_virtual VARCHAR(50)
    GENERATED ALWAYS AS (JSON_UNQUOTE(profile->'$.name')) VIRTUAL,
ADD INDEX idx_name (name_virtual);
```

**单行写法：查询虚拟列索引**
`SELECT * FROM <表名> WHERE <虚拟列名> = <值>`
```sql
-- 查询走虚拟列索引
SELECT * FROM users WHERE name_virtual = 'Alice';
```

**换行写法：函数索引**
`ALTER TABLE <表名> ADD INDEX <索引名> ((<表达式>))`
```sql
-- 直接创建函数索引（MySQL 8.0+）
ALTER TABLE users
ADD INDEX idx_json_name ((CAST(profile->>'$.name' AS CHAR(50))));
```

**换行写法：多值索引**
`ALTER TABLE <表名> ADD INDEX <索引名> ((CAST(<JSON 列> AS <类型> ARRAY)))`
```sql
-- 为 JSON 数组创建多值索引（MySQL 8.0.17+）
ALTER TABLE users
ADD INDEX idx_tags ((CAST(profile->'$.tags' AS CHAR(50) ARRAY)));
```

**单行写法：MEMBER OF 查询**
`<值> MEMBER OF(<JSON 列>)`
```sql
-- 使用 MEMBER OF 查询数组包含值
SELECT * FROM users WHERE 'dev' MEMBER OF(profile->'$.tags');
```

**单行写法：JSON_OVERLAPS 查询**
`JSON_OVERLAPS(<JSON 列>, '<JSON 数组>')`
```sql
-- 使用 JSON_OVERLAPS 查询数组交集
SELECT * FROM users WHERE JSON_OVERLAPS(profile->'$.tags', '["dev", "java"]');
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
| MySQL9新特性与并行查询 | 052-MySQL9NewFeaturesParallelQuery | 本文的并列主题 |
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
| JSON类型与JSON-TABLE | 068-JSONTypeJSONTable | 本文自身 |
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
