---
order: 520
title: 视图与物化视图 语法速查手册
module: 021-postgresql
category: '021-postgresql'
difficulty: beginner
description: 视图与物化视图 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 视图与物化视图 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 普通视图

**基本写法：创建视图**
`CREATE [OR REPLACE] VIEW <视图名> AS <SELECT 语句>;`

```sql
-- 创建用户概览视图
CREATE OR REPLACE VIEW v_user_summary AS
SELECT user_id, user_name, email, last_login
FROM users
WHERE status = 'active';
```

**基本写法：递归视图列名指定**
`CREATE VIEW <视图名> (<列1>, <列2>) AS <SELECT 语句>;`

```sql
-- 显式指定视图列名
CREATE VIEW v_orders (订单号, 客户, 金额) AS
SELECT order_id, customer_name, amount FROM orders;
```

**基本写法：可更新视图**
`CREATE VIEW <视图名> AS SELECT <列> FROM <表>;`

```sql
-- 简单视图可直接 INSERT/UPDATE/DELETE（需包含基表所有非空列）
CREATE VIEW v_active_users AS
SELECT id, name, email FROM users WHERE status = 'active';
-- 通过视图插入
INSERT INTO v_active_users (id, name, email) VALUES (100, '张三', 'z@e.com');
```

**基本写法：带安全屏障视图**
`CREATE VIEW <视图名> WITH (security_barrier) AS <SELECT>;`

```sql
-- 防止通过视图泄露 WHERE 条件数据（行安全增强）
CREATE VIEW v_user_data WITH (security_barrier) AS
SELECT id, name FROM users WHERE deleted_at IS NULL;
```

---

## 视图管理

**基本写法：查看视图定义**
`SELECT pg_get_viewdef('<视图名>'::regclass, true);`

```sql
-- 查看视图完整定义
SELECT pg_get_viewdef('v_user_summary'::regclass, true);
-- psql 元命令
\d+ v_user_summary
```

**基本写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名> [, <视图2>] [CASCADE|RESTRICT];`

```sql
-- 安全删除视图
DROP VIEW IF EXISTS v_user_summary;
-- 级联删除依赖此视图的对象
DROP VIEW IF EXISTS v_orders CASCADE;
```

**基本写法：修改视图属主与模式**
`ALTER VIEW <视图名> OWNER TO <新属主>;`

```sql
-- 修改视图属主
ALTER VIEW v_user_summary OWNER TO app_user;
-- 修改视图所属模式
ALTER VIEW v_user_summary SET SCHEMA reporting;
```

---

## 物化视图创建

**基本写法：创建物化视图**
`CREATE MATERIALIZED VIEW <视图名> AS <SELECT 语句> [WITH [NO] DATA];`

```sql
-- 创建物化视图（预先计算并存储结果）
CREATE MATERIALIZED VIEW mv_daily_sales AS
SELECT date_trunc('day', order_time) AS day,
       SUM(amount) AS total,
       COUNT(*) AS order_count
FROM orders
GROUP BY 1;
-- 仅建结构不填充数据
CREATE MATERIALIZED VIEW mv_daily_sales AS
SELECT date_trunc('day', order_time), SUM(amount) FROM orders GROUP BY 1
WITH NO DATA;
```

**基本写法：指定存储参数与表空间**
`CREATE MATERIALIZED VIEW <视图名> WITH (<参数>) TABLESPACE <表空间> AS <SELECT>;`

```sql
-- 指定填充因子与表空间
CREATE MATERIALIZED VIEW mv_report WITH (fillfactor=80) TABLESPACE ssd
AS SELECT * FROM large_table WHERE year = 2024;
```

---

## 物化视图刷新

**基本写法：全量刷新**
`REFRESH MATERIALIZED VIEW <视图名>;`

```sql
-- 全量刷新（刷新期间阻塞查询）
REFRESH MATERIALIZED VIEW mv_daily_sales;
```

**基本写法：并发刷新（不阻塞）**
`REFRESH MATERIALIZED VIEW CONCURRENTLY <视图名>;`

```sql
-- 并发刷新（需物化视图有唯一索引）
CREATE UNIQUE INDEX idx_mv_daily_sales_day ON mv_daily_sales(day);
REFRESH MATERIALIZED VIEW CONCURRENTLY mv_daily_sales;
```

**基本写法：定时刷新物化视图**
`SELECT cron.schedule('<任务名>', '<cron 表达式>', 'REFRESH MATERIALIZED VIEW <视图>');`

```sql
-- 使用 pg_cron 扩展定时刷新（每小时）
SELECT cron.schedule('refresh_sales', '0 * * * *',
  'REFRESH MATERIALIZED VIEW CONCURRENTLY mv_daily_sales');
```

---

## 物化视图管理

**基本写法：查看物化视图信息**
`SELECT * FROM pg_matviews;`

```sql
-- 查看所有物化视图
SELECT matviewname, schemaname, ispopulated
FROM pg_matviews;
-- 查看是否已填充数据（ispopulated）
```

**基本写法：删除物化视图**
`DROP MATERIALIZED VIEW [IF EXISTS] <视图名> [CASCADE];`

```sql
-- 删除物化视图（数据与结构一起删除）
DROP MATERIALIZED VIEW IF EXISTS mv_daily_sales;
```

**基本写法：修改物化视图（受限）**
`ALTER MATERIALIZED VIEW <视图名> <选项>;`

```sql
-- 修改属主与存储参数（不能直接修改查询定义，需重建）
ALTER MATERIALIZED VIEW mv_daily_sales OWNER TO report_user;
ALTER MATERIALIZED VIEW mv_daily_sales SET (fillfactor = 90);
-- 重命名列
ALTER MATERIALIZED VIEW mv_daily_sales RENAME COLUMN total TO total_amount;
```

**基本写法：重建物化视图定义**
`DROP MATERIALIZED VIEW <旧视图>; CREATE MATERIALIZED VIEW <新视图> AS <新查询>;`

```sql
-- 修改查询定义需重建（推荐先建新视图再删旧）
CREATE MATERIALIZED VIEW mv_daily_sales_v2 AS
SELECT date_trunc('day', order_time), SUM(amount), MAX(amount)
FROM orders GROUP BY 1;
DROP MATERIALIZED VIEW mv_daily_sales;
ALTER MATERIALIZED VIEW mv_daily_sales_v2 RENAME TO mv_daily_sales;
```

---

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
| 分区表 | 015-PartitionedTable | 本文的并列主题 |
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
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文自身 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
