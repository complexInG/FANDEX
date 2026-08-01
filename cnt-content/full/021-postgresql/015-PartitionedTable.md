---
order: 60
title: 分区表
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL分区表：范围分区、列表分区、哈希分区的语法、管理与分区裁剪
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/KNN向量索引
  - postgresql/查询优化
  - postgresql/分区裁剪与分区连接
  - postgresql/高级SQL
prerequisites:
  - postgresql/概述与安装配置
---

# PostgreSQL 分区表

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 声明式分区

PostgreSQL 10+ 支持声明式分区，语法简洁。

## 2. 范围分区

```sql
CREATE TABLE orders (
    id BIGSERIAL,
    order_date DATE NOT NULL,
    amount DECIMAL(10,2)
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2026_q1 PARTITION OF orders
    FOR VALUES FROM ('2026-01-01') TO ('2026-04-01');
CREATE TABLE orders_2026_q2 PARTITION OF orders
    FOR VALUES FROM ('2026-04-01') TO ('2026-07-01');
CREATE TABLE orders_default PARTITION OF orders DEFAULT;
```

## 3. 列表分区

```sql
CREATE TABLE customers (
    id SERIAL,
    name VARCHAR(100),
    region VARCHAR(20)
) PARTITION BY LIST (region);

CREATE TABLE customers_east PARTITION OF customers
    FOR VALUES IN ('华东', '华北');
CREATE TABLE customers_south PARTITION OF customers
    FOR VALUES IN ('华南', '西南');
```

## 4. 哈希分区

```sql
CREATE TABLE logs (
    id BIGSERIAL,
    message TEXT,
    created_at TIMESTAMP DEFAULT NOW()
) PARTITION BY HASH (id);

CREATE TABLE logs_0 PARTITION OF logs FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE logs_1 PARTITION OF logs FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE logs_2 PARTITION OF logs FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE logs_3 PARTITION OF logs FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

## 5. 分区管理

```sql
-- 添加分区
CREATE TABLE orders_2026_q3 PARTITION OF orders
    FOR VALUES FROM ('2026-07-01') TO ('2026-10-01');

-- 分离分区
ALTER TABLE orders DETACH PARTITION orders_2026_q1;

-- 附加分区
ALTER TABLE orders ATTACH PARTITION orders_2026_q1
    FOR VALUES FROM ('2026-01-01') TO ('2026-04-01');

-- 删除分区（数据也删除）
DROP TABLE orders_2026_q1;
```

## 6. 分区裁剪

```sql
-- 查询自动裁剪不需要的分区
EXPLAIN SELECT * FROM orders WHERE order_date >= '2026-04-01';
-- 只扫描 orders_2026_q2

-- 确认裁剪
SET enable_partition_pruning = ON;
```
## 范围分区

**换行写法：创建范围分区主表**
`CREATE TABLE <表名> (<列定义>) PARTITION BY RANGE (<列名>)`
```sql
-- 创建按日期范围分区的订单表
CREATE TABLE orders (
    id BIGSERIAL,
    order_date DATE NOT NULL,
    customer_id INT NOT NULL,
    amount DECIMAL(10, 2)
) PARTITION BY RANGE (order_date);
```

**换行写法：创建范围分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES FROM (<起始>) TO (<结束>)`
```sql
-- 创建 2024 年 1 月的分区
CREATE TABLE orders_2024_01 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

**换行写法：创建多个范围分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES FROM (<起始>) TO (<结束>)`
```sql
-- 创建 2024 年 2 月的分区
CREATE TABLE orders_2024_02 PARTITION OF orders
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
```

---

## 列表分区

**换行写法：创建列表分区主表**
`CREATE TABLE <表名> (<列定义>) PARTITION BY LIST (<列名>)`
```sql
-- 创建按地区列表分区的用户表
CREATE TABLE users (
    id BIGSERIAL,
    username VARCHAR(50),
    region VARCHAR(20)
) PARTITION BY LIST (region);
```

**换行写法：创建列表分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES IN (<值>[, <值>...])`
```sql
-- 创建华北地区的分区
CREATE TABLE users_north PARTITION OF users
    FOR VALUES IN ('北京', '天津', '河北');
```

**换行写法：创建多个列表分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES IN (<值>[, <值>...])`
```sql
-- 创建华南地区的分区
CREATE TABLE users_south PARTITION OF users
    FOR VALUES IN ('广东', '广西', '海南');
```

---

## 哈希分区

**换行写法：创建哈希分区主表**
`CREATE TABLE <表名> (<列定义>) PARTITION BY HASH (<列名>)`
```sql
-- 创建按用户 ID 哈希分区的用户表
CREATE TABLE users (
    id BIGSERIAL,
    username VARCHAR(50),
    email VARCHAR(100)
) PARTITION BY HASH (id);
```

**换行写法：创建哈希分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES WITH (MODULUS <模数>, REMAINDER <余数>)`
```sql
-- 创建哈希余数为 0 的分区
CREATE TABLE users_0 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);
```

**换行写法：创建多个哈希分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES WITH (MODULUS <模数>, REMAINDER <余数>)`
```sql
-- 创建哈希余数为 1 的分区
CREATE TABLE users_1 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 1);
```

---

## 分区管理

**单行写法：查看分区表信息**
`SELECT <列名> FROM pg_inherits WHERE <条件>`
```sql
-- 查看分区表的子表
SELECT inhrelid::regclass AS child_table
FROM pg_inherits
WHERE inhparent = 'orders'::regclass;
```

**单行写法：查看分区表结构**
`SELECT <列名> FROM pg_partitioned_table WHERE <条件>`
```sql
-- 查看分区表的结构信息
SELECT partrelid::regclass AS table_name, partstrat AS strategy
FROM pg_partitioned_table;
```

**单行写法：分离分区**
`ALTER TABLE <父表> DETACH PARTITION <子表名>`
```sql
-- 分离分区使其成为独立表
ALTER TABLE orders DETACH PARTITION orders_2024_01;
```

**单行写法：附加分区**
`ALTER TABLE <父表> ATTACH PARTITION <子表名> FOR VALUES FROM (<起始>) TO (<结束>)`
```sql
-- 附加分区到父表
ALTER TABLE orders ATTACH PARTITION orders_2024_01
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

**单行写法：删除分区子表**
`DROP TABLE <子表名>`
```sql
-- 删除分区子表
DROP TABLE orders_2024_01;
```

**换行写法：创建默认分区**
`CREATE TABLE <子表名> PARTITION OF <父表> DEFAULT`
```sql
-- 创建默认分区存放不匹配的数据
CREATE TABLE users_default PARTITION OF users DEFAULT;
```

---

## 分区索引

**单行写法：在父表创建索引**
`CREATE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 在父表创建索引自动应用到所有分区
CREATE INDEX idx_orders_date ON orders(order_date);
```

**单行写法：在子表创建索引**
`CREATE INDEX <索引名> ON <子表名>(<列名>)`
```sql
-- 在单个分区子表创建索引
CREATE INDEX idx_orders_2024_01_date ON orders_2024_01(order_date);
```

---

## 分区裁剪

**单行写法：查询触发分区裁剪**
`SELECT * FROM <分区表> WHERE <分区列> <操作符> <值>`
```sql
-- 查询条件触发分区裁剪只扫描匹配分区
SELECT * FROM orders WHERE order_date = '2024-01-15';
```

**单行写法：范围查询触发分区裁剪**
`SELECT * FROM <分区表> WHERE <分区列> BETWEEN <值1> AND <值2>`
```sql
-- 范围查询触发分区裁剪
SELECT * FROM orders WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';
```

**单行写法：查看查询计划**
`EXPLAIN SELECT * FROM <分区表> WHERE <条件>`
```sql
-- 查看查询是否触发分区裁剪
EXPLAIN SELECT * FROM orders WHERE order_date = '2024-01-15';
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

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 MVCC 与 vacuum 机制

行头存储 xmin（创建事务）与 xmax（删除事务）；可见性由快照比较决定。
更新 = 插入新版本 + 旧版本标记；旧版本对旧事务可见，vacuum 回收不再可见的死元组。
事务 ID 回卷：约 21 亿事务后需要冻结；autovacuum 与 vacuum freeze 防止。
监控：SELECT n_dead_tup, last_autovacuum FROM pg_stat_user_tables。

### 13.2 逻辑复制与高可用

发布（publication）定义表集，订阅（subscription）在目标端应用变更；支持过滤与列子集。
流复制：主库 WAL 发送到备库，同步/异步模式；级联复制扩展拓扑。
Patroni 使用分布式共识（etcd）选主，故障自动切换，配合虚拟 IP。
切换演练与数据校验（pg_checksums）是可用性工程必备。

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
| 分区表 | 015-PartitionedTable | 本文自身 |
| 分区裁剪与分区连接 | 016-PartitionPruningPartitionJoin | 本文的并列主题 |
| 高级SQL | 017-AdvancedSQL | 本文的并列主题 |
| MERGE语句增强 | 018-MERGEStatementEnhancement | 本文的并列主题 |
| JSON-TABLE | 019-JSONTABLE | 本文的并列主题 |
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
