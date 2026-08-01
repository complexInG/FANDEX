---
order: 64
title: 'JSON-TABLE'
module: postgresql
category: PostgreSQL
difficulty: advanced
description: 'PostgreSQL JSON_TABLE：标准化JSON处理、路径表达式、嵌套列与关系化输出'
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/高级SQL
  - postgresql/MERGE语句增强
  - postgresql/全文检索
  - postgresql/地理空间对象
prerequisites:
  - postgresql/概述与安装配置
---

# PostgreSQL JSON/JSONB 操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. JSON_TABLE 概述

JSON_TABLE 是 SQL:2016 标准函数，将 JSON 数据转换为关系表，PostgreSQL 17+ 支持。

## 2. 基本用法

```sql
-- 将 JSON 数组展开为行
SELECT jt.*
FROM api_logs,
JSON_TABLE(payload, '$.items[*]' COLUMNS (
    product_id INTEGER PATH '$.product_id',
    quantity INTEGER PATH '$.quantity',
    price NUMERIC PATH '$.price'
)) AS jt;
```

## 3. 嵌套列

```sql
-- 处理嵌套 JSON
SELECT jt.name, addr.street, addr.city
FROM users,
JSON_TABLE(data, '$' COLUMNS (
    name VARCHAR(100) PATH '$.name',
    NESTED PATH '$.address' COLUMNS (
        street VARCHAR(200) PATH '$.street',
        city VARCHAR(100) PATH '$.city',
        zip VARCHAR(20) PATH '$.zip'
    )
)) AS jt;
```

## 4. 错误处理

```sql
-- ERROR ON ERROR：遇到错误报错
-- EMPTY ON ERROR：遇到错误返回空
-- NULL ON ERROR：遇到错误返回 NULL（默认）

SELECT jt.*
FROM documents,
JSON_TABLE(data, '$.items[*]' COLUMNS (
    id INTEGER PATH '$.id' ERROR ON ERROR,
    name VARCHAR(100) PATH '$.name' NULL ON ERROR
)) AS jt;
```

## 5. 与 JSONB 操作符对比

```sql
-- JSONB 操作符方式
SELECT payload->>'name' AS name,
       payload->'address'->>'city' AS city
FROM users;

-- JSON_TABLE 方式（更适合复杂嵌套）
SELECT jt.name, jt.city
FROM users,
JSON_TABLE(payload, '$' COLUMNS (
    name VARCHAR(100) PATH '$.name',
    city VARCHAR(100) PATH '$.address.city'
)) AS jt;
```
## 创建与插入

**单行写法：创建 JSONB 列**
`<列名> JSONB`
```sql
-- 创建带 JSONB 列的表
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  attributes JSONB
);
```

**单行写法：插入 JSON 数据**
`INSERT INTO <表名> (<列>) VALUES ('<JSON字符串>'::jsonb);`
```sql
-- 插入 JSONB 数据
INSERT INTO products (name, attributes)
VALUES ('手机', '{"品牌": "Xiaomi", "价格": 2999, "颜色": "黑色"}'::jsonb);
```

**单行写法：使用 JSON 构造函数（PG17+）**
`INSERT INTO <表名> (<列>) VALUES (JSON_OBJECT('key', 'value'));`
```sql
-- 使用 SQL 标准 JSON 构造函数
INSERT INTO products (name, attributes)
VALUES ('手机', JSON_OBJECT('品牌', 'Xiaomi', '价格', 2999));
```

**单行写法：插入 JSON 数组**
`INSERT INTO <表名> (<列>) VALUES ('[1, 2, 3]'::jsonb);`
```sql
-- 插入 JSON 数组
INSERT INTO logs (tags) VALUES ('["redis", "mysql", "pg"]'::jsonb);
```

---

## 查询操作

**单行写法：使用 -> 获取 JSON 对象字段**
`SELECT <列>->'<键>' FROM <表名>;`
```sql
-- 获取 JSON 对象字段（返回 JSONB）
SELECT attributes->'品牌' AS brand FROM products;
```

**单行写法：使用 ->> 获取文本值**
`SELECT <列>->>'<键>' FROM <表名>;`
```sql
-- 获取 JSON 字段文本值（返回 TEXT）
SELECT attributes->>'品牌' AS brand FROM products;
```

**单行写法：路径访问嵌套字段**
`SELECT <列>#>'{<路径1>, <路径2>}' FROM <表名>;`
```sql
-- 按路径获取嵌套 JSONB 值
SELECT attributes#>'{地址, 城市}' AS city FROM users;
```

**单行写法：路径访问文本**
`SELECT <列>#>>'{<路径1>, <路径2>}' FROM <表名>;`
```sql
-- 按路径获取嵌套字段文本值
SELECT attributes#>>'{地址, 城市}' AS city FROM users;
```

**单行写法：获取数组元素**
`SELECT <列>-><索引> FROM <表名>;`
```sql
-- 获取 JSON 数组指定索引元素
SELECT tags->0 AS first_tag FROM logs;
```

---

## 条件查询

**单行写法：按 JSON 字段过滤**
`SELECT * FROM <表名> WHERE <列>->>'<键>' = '<值>';`
```sql
-- 查询品牌为 Xiaomi 的商品
SELECT * FROM products WHERE attributes->>'品牌' = 'Xiaomi';
```

**单行写法：使用 @> 包含操作符**
`SELECT * FROM <表名> WHERE <列> @> '<JSON对象>';`
```sql
-- 查询包含指定键值对的记录
SELECT * FROM products WHERE attributes @> '{"品牌": "Xiaomi"}';
```

**单行写法：使用 ? 键存在判断**
`SELECT * FROM <表名> WHERE <列> ? '<键>';`
```sql
-- 查询存在指定键的记录
SELECT * FROM products WHERE attributes ? '价格';
```

**单行写法：使用 ?| 任一键存在**
`SELECT * FROM <表名> WHERE <列> ?| ARRAY['<键1>', '<键2>'];`
```sql
-- 查询存在任一键的记录
SELECT * FROM products WHERE attributes ?| ARRAY['价格', '库存'];
```

**单行写法：使用 ?& 所有关键存在**
`SELECT * FROM <表名> WHERE <列> ?& ARRAY['<键1>', '<键2>'];`
```sql
-- 查询同时存在多个键的记录
SELECT * FROM products WHERE attributes ?& ARRAY['价格', '库存'];
```

---

## 修改操作

**单行写法：合并 JSON 对象**
`SELECT <列> || '<JSON对象>' FROM <表名>;`
```sql
-- 合并两个 JSON 对象（后者覆盖前者）
UPDATE products SET attributes = attributes || '{"库存": 100}'::jsonb WHERE id = 1;
```

**单行写法：删除键**
`SELECT <列> - '<键>' FROM <表名>;`
```sql
-- 删除 JSON 对象指定键
UPDATE products SET attributes = attributes - '颜色' WHERE id = 1;
```

**单行写法：删除多个键**
`SELECT <列> - '<键1>' - '<键2>' FROM <表名>;`
```sql
-- 删除多个键
UPDATE products SET attributes = attributes - '颜色' - '库存' WHERE id = 1;
```

**单行写法：按路径删除**
`SELECT <列> #- '{<路径>}' FROM <表名>;`
```sql
-- 按路径删除嵌套字段
UPDATE users SET attributes = attributes #- '{地址, 城市}' WHERE id = 1;
```

**单行写法：更新指定路径值**
`SELECT jsonb_set(<列>, '{<路径>}', '<新值>');`
```sql
-- 更新嵌套字段值
UPDATE users SET attributes = jsonb_set(attributes, '{地址, 城市}', '"北京"'::jsonb) WHERE id = 1;
```

**单行写法：设置值不存在时才插入**
`SELECT jsonb_set(<列>, '{<路径>}', '<新值>', true);`
```sql
-- 仅当键不存在时插入新值
UPDATE products SET attributes = jsonb_set(attributes, '{折扣}', '"0.9"'::jsonb, true) WHERE id = 1;
```

---

## 聚合与展开

**单行写法：JSON 聚合**
`SELECT json_agg(<列>) FROM <表名>;`
```sql
-- 将多行数据聚合成 JSON 数组
SELECT json_agg(username) AS usernames FROM users;
```

**单行写法：JSONB 聚合**
`SELECT jsonb_agg(<列>) FROM <表名>;`
```sql
-- 将多行聚合成 JSONB 数组
SELECT jsonb_agg(row_to_json(u)) AS users FROM users u;
```

**单行写法：构建 JSON 对象**
`SELECT json_build_object('<键>', <值>[, ...]);`
```sql
-- 构建键值对 JSON 对象
SELECT json_build_object('id', id, 'name', username) FROM users;
```

**单行写法：行转 JSON 对象**
`SELECT row_to_json(<表别名>) FROM <表名> <别名>;`
```sql
-- 将整行转为 JSON 对象
SELECT row_to_json(u) FROM users u WHERE id = 1;
```

**换行写法：展开 JSON 数组**
`SELECT * FROM jsonb_array_elements(<列>) AS <别名>;`
```sql
-- 将 JSON 数组展开为多行
SELECT * FROM jsonb_array_elements('["a", "b", "c"]'::jsonb) AS elem;
```

**换行写法：展开 JSON 对象**
`SELECT * FROM jsonb_each(<列>) AS <别名>(键, 值);`
```sql
-- 将 JSON 对象展开为键值对多行
SELECT * FROM jsonb_each('{"a": 1, "b": 2}'::jsonb) AS x(key, value);
```

---

## 索引与性能

**单行写法：创建 GIN 索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (<列>);`
```sql
-- 为 JSONB 列创建 GIN 索引
CREATE INDEX idx_products_attr ON products USING GIN (attributes);
```

**单行写法：创建表达式索引**
`CREATE INDEX <索引名> ON <表名> ((<列>->>'<键>'));`
```sql
-- 为 JSONB 某字段创建表达式索引
CREATE INDEX idx_products_brand ON products ((attributes->>'品牌'));
```

**单行写法：查看 JSONB 键**
`SELECT jsonb_object_keys(<列>) FROM <表名>;`
```sql
-- 获取 JSONB 对象所有键
SELECT jsonb_object_keys(attributes) FROM products WHERE id = 1;
```

---

## JSON_TABLE（PG17+）

**换行写法：JSON 数据转关系表**
`SELECT * FROM JSON_TABLE(<JSON>, '<路径>' COLUMNS (<列定义>));`
```sql
-- 将 JSON 数组转为关系表行
SELECT * FROM JSON_TABLE(
  '[{"name": "张三", "age": 25}, {"name": "李四", "age": 30}]'::jsonb,
  '$[*]' COLUMNS (
    name TEXT PATH '$.name',
    age INT PATH '$.age'
  )
);
```

**单行写法：JSON_EXISTS 判断路径存在**
`SELECT JSON_EXISTS(<JSON>, '<路径>');`
```sql
-- 判断 JSON 路径是否存在
SELECT JSON_EXISTS(attributes, '$.品牌') FROM products WHERE id = 1;
```

**单行写法：JSON_VALUE 提取标量**
`SELECT JSON_VALUE(<JSON>, '<路径>');`
```sql
-- 提取 JSON 标量值
SELECT JSON_VALUE(attributes, '$.价格') FROM products WHERE id = 1;
```

**单行写法：JSON_QUERY 提取对象**
`SELECT JSON_QUERY(<JSON>, '<路径>');`
```sql
-- 提取 JSON 对象或数组
SELECT JSON_QUERY(attributes, '$.地址') FROM users WHERE id = 1;
```

## 参考文献



PostgreSQL 官方文档：https://www.postgresql.org/docs/
PostgreSQL 中文文档：https://www.postgresql.org/docs/current/index.html
PGXN 扩展仓库：https://pgxn.org/
PostGIS：https://postgis.net/
pgvector：https://github.com/pgvector/pgvector

## 延伸阅读



PostgreSQL 窗口函数，见 021-postgresql 模块文档。
PostgreSQL 递归查询，见 021-postgresql 模块相关文档。
SQL 基础，见 019-sql 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 PostgreSQL 课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与安装配置 | 001-OverviewInstallConfig | 本文的前置基础 |
| 事务与并发控制 | 002-TransactionConcurrencyControl | 本文的并列主题 |
| 索引与查询优化 | 003-IndexQueryOptimization | 本文的性能延伸 |
| 高级SQL与扩展 | 004-AdvancedSQLExtension | 本文的并列主题 |
| 复制与高可用 | 005-ReplicationHA | 本文的并列主题 |
| 体系架构 | 006-SystemArchitecture | 本文的原理深化 |
| 锁机制 | 007-LockMechanism | 本文的原理深化 |
| 死锁检测与处理 | 008-DeadlockDetectionHandling | 本文的并列主题 |
| VACUUM机制 | 009-VACUUMMechanism | 本文的原理深化 |
| 事务ID回卷预防 | 010-TransactionIDWraparoundPrevention | 本文的并列主题 |
| 索引类型 | 011-IndexType | 本文的并列主题 |
| 覆盖索引与部分索引 | 012-CoveringIndexPartialIndex | 本文的并列主题 |
| KNN向量索引 | 013-KNNVectorIndex | 本文的并列主题 |
| 查询优化 | 014-QueryOptimization | 本文的性能延伸 |
| 分区表 | 015-PartitionedTable | 本文的并列主题 |
| 分区裁剪与分区连接 | 016-PartitionPruningPartitionJoin | 本文的并列主题 |
| 高级SQL | 017-AdvancedSQL | 本文的并列主题 |
| MERGE语句增强 | 018-MERGEStatementEnhancement | 本文的并列主题 |
| JSON-TABLE | 019-JSONTABLE | 本文自身 |
| 全文检索 | 020-FullTextSearch | 本文的并列主题 |
| 地理空间对象 | 021-GeoSpatialObject | 本文的并列主题 |
| 存储过程与函数 | 022-StoredProcedureAndFunction | 本文的并列主题 |
| 触发器与事件触发器 | 023-TriggerEventTrigger | 本文的并列主题 |
| 扩展模块 | 024-ExtensionModule | 本文的并列主题 |
| FDW外部数据包装器 | 025-FDWFDW | 本文的并列主题 |
| 流复制 | 026-StreamingReplication | 本文的并列主题 |
| 级联复制 | 027-CascadingReplication | 本文的并列主题 |
| 物理复制槽 | 028-PhysicalReplicationSlot | 本文的并列主题 |
| 逻辑解码与输出插件 | 029-LogicalDecodingOutputPlugin | 本文的并列主题 |
| 增量备份 | 030-IncrementalBackup | 本文的并列主题 |
| 订阅与发布 | 031-SubscribePublish | 本文的并列主题 |
| SSL-TLS加密连接 | 032-SSLEncryptionConnection | 本文的安全延伸 |
| 基于角色的权限管理 | 033-RoleBasedPermissionManagement | 本文的安全延伸 |
| 行级安全策略 | 034-RowLevelSecurity | 本文的安全延伸 |
| 数据加密存储 | 035-DataEncryptionStorage | 本文的安全延伸 |
| 审计日志 | 036-AuditLog | 本文的并列主题 |
| 序列与自增列 | 037-SequenceAutoIncrement | 本文的并列主题 |
| 生成列 | 038-GeneratedColumn | 本文的并列主题 |
| 可更新视图 | 039-UpdatableView | 本文的并列主题 |
| 并行查询 | 040-ParallelQuery | 本文的并列主题 |
| 逻辑复制与物理复制对比 | 041-LogicalPhysicalReplicationCompare | 本文的并列主题 |
| JSONB与JSON差异 | 042-JSONBJSONDifference | 本文的并列主题 |
| 扩展模块详解 | 043-ExtensionModuleDetailed | 本文的并列主题 |
| PostgreSQL DDL 数据定义 | 044-DDL | 本文的并列主题 |
| PostgreSQL DML 数据操作 | 045-DML | 本文的并列主题 |
| PostgreSQL 窗口函数 | 046-WindowFunction | 本文的并列主题 |
| PostgreSQL CTE 递归查询 | 047-CTE | 本文的并列主题 |
| PostgreSQL psql CLI 命令 | 048-PsqlCLI | 本文的并列主题 |
| pg_dump 与 pg_restore 语法速查手册 | 049-PgDumpRestore | 本文的并列主题 |
| 数组类型操作 语法速查手册 | 050-ArrayType | 本文的并列主题 |
| 模式（Schema）管理 语法速查手册 | 051-SchemaManagement | 本文的并列主题 |
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
