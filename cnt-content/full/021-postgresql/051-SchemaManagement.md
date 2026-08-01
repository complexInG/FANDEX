---
order: 510
title: 模式（Schema）管理 语法速查手册
module: 021-postgresql
category: '021-postgresql'
difficulty: beginner
description: 模式（Schema）管理 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 模式（Schema）管理 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建与删除模式

**基本写法：创建模式**
`CREATE SCHEMA [IF NOT EXISTS] <模式名> [AUTHORIZATION <用户>];`

```sql
-- 创建业务模式
CREATE SCHEMA IF NOT EXISTS business;
-- 创建模式并指定属主
CREATE SCHEMA sales AUTHORIZATION sales_user;
```

**基本写法：在模式中创建对象**
`CREATE TABLE <模式名>.<表名> (...)`

```sql
-- 在指定模式下建表（使用模式限定名）
CREATE TABLE business.orders (
  id BIGSERIAL PRIMARY KEY,
  amount NUMERIC(10,2)
);
```

**基本写法：删除模式**
`DROP SCHEMA [IF EXISTS] <模式名> [CASCADE|RESTRICT];`

```sql
-- 仅删除空模式
DROP SCHEMA IF EXISTS old_app;
-- 级联删除模式及其所有对象
DROP SCHEMA IF EXISTS test_app CASCADE;
```

---

## 模式搜索路径

**基本写法：查看搜索路径**
`SHOW search_path;`

```sql
-- 查看当前模式搜索路径
SHOW search_path;  -- 默认 "$user", public
```

**基本写法：设置搜索路径**
`SET search_path TO <模式1>[, <模式2>...];`

```sql
-- 临时设置搜索路径（影响对象解析顺序）
SET search_path TO business, public;
-- 在函数内设置（仅函数执行期间生效）
SET search_path TO business, public;
SELECT * FROM orders;  -- 解析为 business.orders
```

**基本写法：持久设置搜索路径**
`ALTER DATABASE <库名> SET search_path TO <模式>;`

```sql
-- 数据库级持久设置
ALTER DATABASE mydb SET search_path TO business, public;
-- 用户级设置
ALTER ROLE app_user SET search_path TO business, public;
```

**基本写法：查看当前模式**
`SELECT current_schema();`

```sql
-- 查看当前生效模式
SELECT current_schema();
-- 查看当前用户名同名模式是否存在
SELECT current_schemas(true);
```

---

## 模式权限

**基本写法：授予模式使用权限**
`GRANT USAGE ON SCHEMA <模式名> TO <角色>;`

```sql
-- 授予角色访问模式的权限
GRANT USAGE ON SCHEMA business TO app_user;
```

**基本写法：授予模式内对象权限**
`GRANT <权限> ON ALL TABLES IN SCHEMA <模式名> TO <角色>;`

```sql
-- 授予模式内所有表的查询权限
GRANT SELECT ON ALL TABLES IN SCHEMA business TO readonly_role;
-- 授予所有序列使用权限
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA business TO app_user;
```

**基本写法：设置默认权限（新对象自动授权）**
`ALTER DEFAULT PRIVILEGES IN SCHEMA <模式名> GRANT <权限> ON TABLES TO <角色>;`

```sql
-- 后续在该模式新建的表自动授予查询权限
ALTER DEFAULT PRIVILEGES IN SCHEMA business
GRANT SELECT ON TABLES TO readonly_role;
```

---

## 模式查询与迁移

**基本写法：查看所有模式**
`SELECT schema_name FROM information_schema.schemata;`

```sql
-- 查看数据库中所有模式
SELECT schema_name, schema_owner
FROM information_schema.schemata
WHERE schema_name NOT LIKE 'pg_%' AND schema_name <> 'information_schema';
```

**基本写法：查看模式内对象**
`SELECT * FROM information_schema.tables WHERE table_schema = '<模式名>';`

```sql
-- 查看 business 模式下的所有表
SELECT table_name, table_type
FROM information_schema.tables
WHERE table_schema = 'business';
```

**基本写法：将表迁移到另一模式**
`ALTER TABLE <旧模式>.<表名> SET SCHEMA <新模式>;`

```sql
-- 将表迁移到另一模式（索引、约束自动跟随）
ALTER TABLE public.old_orders SET SCHEMA archive;
```

**基本写法：重命名模式**
`ALTER SCHEMA <旧名> RENAME TO <新名>;`

```sql
-- 重命名模式
ALTER SCHEMA old_app RENAME TO legacy_app;
```

**基本写法：修改模式属主**
`ALTER SCHEMA <模式名> OWNER TO <新属主>;`

```sql
-- 修改模式属主
ALTER SCHEMA business OWNER TO dba;
```

---

## 公共模式与扩展模式

**基本写法：public 模式（默认共享模式）**
`CREATE TABLE public.<表名> (...)`

```sql
-- public 是默认共享模式，所有用户默认有访问权
CREATE TABLE public.shared_config (key TEXT PRIMARY KEY, value TEXT);
```

**基本写法：扩展自带模式**
`CREATE EXTENSION <扩展名> SCHEMA <模式名>;`

```sql
-- 将扩展对象放到指定模式
CREATE EXTENSION IF NOT EXISTS postgis SCHEMA geo;
-- pg_catalog 系统模式（不可删除，存放内置对象）
SELECT * FROM pg_catalog.pg_class LIMIT 1;
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
| 模式（Schema）管理 语法速查手册 | 051-SchemaManagement | 本文自身 |
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
