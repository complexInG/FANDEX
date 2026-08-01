---
order: 69
title: 扩展模块
module: postgresql
category: PostgreSQL
difficulty: intermediate
description: PostgreSQL扩展模块：PostGIS、pgvector、pg_stat_statements与常用扩展管理
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/存储过程与函数
  - postgresql/触发器与事件触发器
  - postgresql/FDW外部数据包装器
  - postgresql/流复制
prerequisites:
  - postgresql/概述与安装配置
---

# 扩展（CREATE EXTENSION）语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 扩展管理

```sql
-- 查看可用扩展
SELECT * FROM pg_available_extensions;

-- 安装扩展
CREATE EXTENSION postgis;
CREATE EXTENSION vector;
CREATE EXTENSION pg_stat_statements;

-- 查看已安装扩展
SELECT * FROM pg_extension;

-- 更新扩展
ALTER EXTENSION postgis UPDATE;

-- 卸载扩展
DROP EXTENSION postgis;
```

## 2. PostGIS

```sql
CREATE EXTENSION postgis;
-- 空间数据类型、函数和索引
```

## 3. pgvector

```sql
CREATE EXTENSION vector;
-- 向量存储和相似度搜索
```

## 4. pg_stat_statements

```sql
CREATE EXTENSION pg_stat_statements;

-- 查看最慢的查询
SELECT query, calls, total_exec_time, mean_exec_time
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;

-- 重置统计
SELECT pg_stat_statements_reset();
```

## 5. 其他常用扩展

| 扩展         | 用途                     |
| ------------ | ------------------------ |
| pgcrypto     | 加密函数                 |
| pg_trgm      | 模糊匹配、相似度搜索     |
| hstore       | 键值对存储               |
| uuid-ossp    | UUID 生成                |
| btree_gin    | GIN 索引支持 B-tree 类型 |
| pg_repack    | 在线消除表膨胀           |
| pgaudit      | 审计日志                 |
| postgres_fdw | 外部数据包装器           |
## 扩展管理

**基本写法：安装扩展**
`CREATE EXTENSION [IF NOT EXISTS] <扩展名> [WITH] [SCHEMA <模式>] [VERSION <版本>];`

```sql
-- 安装常用扩展
CREATE EXTENSION IF NOT EXISTS pgcrypto;          -- 加密函数
CREATE EXTENSION IF NOT EXISTS pg_trgm;            -- 模糊匹配与相似度
CREATE EXTENSION IF NOT EXISTS btree_gin;          -- GIN 索引支持 btree 类型
CREATE EXTENSION IF NOT EXISTS hstore SCHEMA public;  -- 键值对类型
-- 指定版本
CREATE EXTENSION IF NOT EXISTS postgis VERSION '3.4.0';
```

**基本写法：查看已安装扩展**
`SELECT * FROM pg_available_extensions;`

```sql
-- 查看所有可用扩展及安装状态
SELECT name, default_version, installed_version
FROM pg_available_extensions
WHERE installed_version IS NOT NULL;
-- 查看所有可用扩展（含未安装）
SELECT name, default_version FROM pg_available_extensions ORDER BY name;
```

**基本写法：查看扩展详细信息**
`\dx+`

```bash
# psql 元命令查看已安装扩展及对象
\dx
# 查看扩展包含的对象
\dx+ pg_trgm
```

**基本写法：更新扩展版本**
`ALTER EXTENSION <扩展名> UPDATE [TO <新版本>];`

```sql
-- 升级扩展到新版本
ALTER EXTENSION postgis UPDATE TO '3.5.0';
```

**基本写法：删除扩展**
`DROP EXTENSION [IF EXISTS] <扩展名> [, <扩展2>] [CASCADE|RESTRICT];`

```sql
-- 删除扩展（默认 RESTRICT，依赖对象存在则失败）
DROP EXTENSION IF EXISTS pg_trgm;
-- 级联删除扩展及其依赖对象
DROP EXTENSION IF EXISTS postgis CASCADE;
```

---

## 常用扩展速查

**基本写法：uuid-OSSP 生成 UUID**
`CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`

```sql
-- 生成 UUID（uuid-ossp 扩展）
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();  -- 随机 UUID
SELECT uuid_generate_v1();  -- 基于时间
-- PG 13+ 内置 gen_random_uuid()，无需扩展
SELECT gen_random_uuid();
```

**基本写法：pg_trgm 模糊匹配**
`CREATE EXTENSION IF NOT EXISTS pg_trgm;`

```sql
-- 三元组相似度匹配
CREATE EXTENSION IF NOT EXISTS pg_trgm;
-- 相似度查询
SELECT name, similarity(name, '张三') AS sim
FROM users WHERE name % '张三' ORDER BY sim DESC;
-- 创建 GIN trigram 索引加速 LIKE
CREATE INDEX idx_users_name ON users USING GIN (name gin_trgm_ops);
```

**基本写法：pgcrypto 加密**
`CREATE EXTENSION IF NOT EXISTS pgcrypto;`

```sql
-- 加密解密函数
CREATE EXTENSION IF NOT EXISTS pgcrypto;
SELECT digest('password', 'sha256');            -- 哈希
SELECT encrypt('data', 'key', 'aes');           -- 对称加密
SELECT pgp_sym_encrypt('secret', 'password');   -- PGP 对称加密
```

**基本写法：hstore 键值对**
`CREATE EXTENSION IF NOT EXISTS hstore;`

```sql
-- 键值对存储
CREATE EXTENSION IF NOT EXISTS hstore;
CREATE TABLE kv (id INT, data hstore);
INSERT INTO kv VALUES (1, 'name=>张三, age=>25');
SELECT data->'name' FROM kv WHERE id = 1;
```

**基本写法：postgis 空间数据**
`CREATE EXTENSION IF NOT EXISTS postgis;`

```sql
-- PostGIS 空间扩展
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE TABLE geo_points (id SERIAL PRIMARY KEY, geom geometry(Point, 4326));
INSERT INTO geo_points (geom) VALUES (ST_SetSRID(ST_MakePoint(116.4, 39.9), 4326));
-- 距离查询
SELECT id FROM geo_points WHERE ST_DWithin(geom, ST_MakePoint(116.4,39.9)::geography, 1000);
```

---

## 扩展开发相关

**基本写法：查看扩展包含的对象**
`SELECT * FROM pg_extension;`

```sql
-- 查看已安装扩展的详细信息
SELECT extname, extversion, extnamespace::regnamespace
FROM pg_extension;
```

**基本写法：查看扩展依赖对象**
`SELECT * FROM pg_depend WHERE refobjid = '<扩展名>'::regclass;`

```sql
-- 查看扩展提供的函数
SELECT proname, oidvectortypes(proargtypes)
FROM pg_proc p JOIN pg_extension e ON p.proextnamespace = e.extnamespace
WHERE e.extname = 'pg_trgm';
```

**基本写法：控制扩展可用性**
`shared_preload_libraries = '<扩展名>'`

```ini
# postgresql.conf 配置需预加载的扩展（如 pg_stat_statements）
shared_preload_libraries = 'pg_stat_statements, auto_explain'
```

**基本写法：pg_stat_statements 性能统计**
`CREATE EXTENSION IF NOT EXISTS pg_stat_statements;`

```sql
-- 安装并查看 SQL 执行统计
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
-- 查看最慢的 10 条 SQL
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC LIMIT 10;
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
| 扩展模块 | 024-ExtensionModule | 本文自身 |
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
