---
order: 103
title: 扩展模块详解
module: postgresql
category: database
difficulty: intermediate
description: 'PostgreSQL 扩展模块详解：PostGIS 地理空间、pgvector 向量搜索、pg_stat_statements 性能分析。'
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/逻辑复制与物理复制对比
  - postgresql/JSONB与JSON差异
prerequisites:
  - postgresql/概述与安装配置
---

## 1. 扩展模块体系

### 1.1 扩展管理

```sql
-- 查看可用扩展
SELECT * FROM pg_available_extensions;

-- 安装扩展
CREATE EXTENSION IF NOT EXISTS extension_name;

-- 查看已安装扩展
SELECT * FROM pg_extension;

-- 升级扩展
ALTER EXTENSION extension_name UPDATE;

-- 卸载扩展
DROP EXTENSION extension_name;
```

### 1.2 扩展搜索路径

```sql
-- 扩展安装位置
SHOW extension_dir;
-- /usr/share/postgresql/16/extension

-- 控制文件和 SQL 脚本
-- extension_name.control
-- extension_name--version.sql
```

## 2. PostGIS

### 2.1 安装与验证

```sql
CREATE EXTENSION postgis;

-- 验证安装
SELECT PostGIS_Version();
-- 3.4 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
```

### 2.2 几何类型

| 类型         | 说明     | 示例                                    |
| ------------ | -------- | --------------------------------------- |
| POINT        | 点       | `POINT(116.4 39.9)`                     |
| LINESTRING   | 线       | `LINESTRING(0 0, 1 1, 2 2)`             |
| POLYGON      | 多边形   | `POLYGON((0 0, 4 0, 4 4, 0 4, 0 0))`    |
| MULTIPOINT   | 多点     | `MULTIPOINT(0 0, 1 1)`                  |
| MULTIPOLYGON | 多多边形 | `MULTIPOLYGON(((0 0,1 0,1 1,0 1,0 0)))` |

### 2.3 地理空间查询

```sql
-- 创建空间表
CREATE TABLE stores (
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(100),
    location GEOGRAPHY(POINT, 4326)  -- WGS84 坐标系
);

-- 插入数据（经度 纬度）
INSERT INTO stores (name, location) VALUES
('天安门', ST_GeogFromText('POINT(116.3974 39.9087)')),
('故宫', ST_GeogFromText('POINT(116.3972 39.9163)')),
('颐和园', ST_GeogFromText('POINT(116.2755 39.9999)'));

-- 查找5公里内的商店
SELECT name,
       ST_Distance(location, ST_GeogFromText('POINT(116.3974 39.9087)')) AS distance
FROM stores
WHERE ST_DWithin(location, ST_GeogFromText('POINT(116.3974 39.9087)'), 5000)
ORDER BY distance;

-- 空间索引
CREATE INDEX idx_stores_location ON stores USING gist (location);
```

### 2.4 常用函数

```sql
-- 距离（米）
ST_Distance(geog1, geog2)

-- 范围查询
ST_DWithin(geog1, geog2, distance_meters)

-- 面积（平方米）
ST_Area(geog)

-- 长度（米）
ST_Length(geog)

-- 缓冲区
ST_Buffer(geog, radius_meters)

-- 是否包含
ST_Contains(geom1, geom2)

-- 是否相交
ST_Intersects(geom1, geom2)

-- 坐标转换
ST_Transform(geom, target_srid)
```

## 3. pgvector

### 3.1 安装与基本使用

```sql
CREATE EXTENSION vector;

-- 创建向量列
CREATE TABLE documents (
    id        SERIAL PRIMARY KEY,
    content   TEXT,
    embedding vector(1536)  -- OpenAI ada-002 维度
);

-- 插入向量
INSERT INTO documents (content, embedding) VALUES
('Hello world', '[0.1, 0.2, 0.3, ...]'),
('PostgreSQL vector', '[0.4, 0.5, 0.6, ...]');
```

### 3.2 距离度量

```sql
-- L2 距离（欧几里得距离）
SELECT content, embedding <=> '[0.1, 0.2, 0.3, ...]' AS distance
FROM documents
ORDER BY embedding <=> '[0.1, 0.2, 0.3, ...]'
LIMIT 5;

-- 内积（负内积）
SELECT content, embedding <#> '[0.1, 0.2, 0.3, ...]' AS distance
FROM documents
ORDER BY embedding <#> '[0.1, 0.2, 0.3, ...]'
LIMIT 5;

-- 余弦距离
SELECT content, embedding <=> '[0.1, 0.2, 0.3, ...]' AS distance
FROM documents
ORDER BY embedding <=> '[0.1, 0.2, 0.3, ...]'
LIMIT 5;
```

| 操作符 | 度量     | 公式                                                                 |
| ------ | -------- | -------------------------------------------------------------------- |
| `<->`  | L2 距离  | $\sqrt{\sum (a_i - b_i)^2}$                                          |
| `<#>`  | 内积     | $-\sum a_i \cdot b_i$                                                |
| `<=>`  | 余弦距离 | $1 - \frac{\sum a_i b_i}{\sqrt{\sum a_i^2} \cdot \sqrt{\sum b_i^2}}$ |

### 3.3 索引类型

```sql
-- HNSW 索引（推荐，速度快）
CREATE INDEX idx_documents_embedding_hnsw
ON documents USING hnsw (embedding vector_cosine_ops);

-- IVFFlat 索引
CREATE INDEX idx_documents_embedding_ivfflat
ON documents USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

-- 索引参数
-- HNSW
CREATE INDEX idx_hnsw ON docs USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- IVFFlat
CREATE INDEX idx_ivf ON docs USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100, probes = 10);
```

### 3.4 索引选择

| 索引    | 构建速度 | 查询速度 | 召回率 | 内存 |
| ------- | -------- | -------- | ------ | ---- |
| HNSW    | 慢       | 快       | 高     | 高   |
| IVFFlat | 快       | 中       | 中     | 低   |
| 无索引  | -        | 慢       | 100%   | 无   |

## 4. pg_stat_statements

### 4.1 安装与配置

```sql
-- 安装扩展
CREATE EXTENSION pg_stat_statements;

-- postgresql.conf 配置
-- shared_preload_libraries = 'pg_stat_statements'
-- pg_stat_statements.max = 10000
-- pg_stat_statements.track = all
-- pg_stat_statements.track_utility = on
-- pg_stat_statements.save = on
```

### 4.2 核心查询

```sql
-- 最耗时的 SQL（总时间）
SELECT query,
       calls,
       round(total_exec_time::numeric, 2) AS total_ms,
       round(mean_exec_time::numeric, 2) AS mean_ms,
       round(max_exec_time::numeric, 2) AS max_ms,
       rows
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;

-- 最慢的 SQL（平均时间）
SELECT query,
       calls,
       round(mean_exec_time::numeric, 2) AS mean_ms
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- 读取最多的 SQL
SELECT query,
       calls,
       shared_blks_hit + shared_blks_read AS total_blks,
       round((shared_blks_hit::float / NULLIF(shared_blks_hit + shared_blks_read, 0) * 100)::numeric, 2) AS hit_ratio
FROM pg_stat_statements
ORDER BY shared_blks_hit + shared_blks_read DESC
LIMIT 10;

-- 产生最多临时文件的 SQL
SELECT query,
       calls,
       temp_blks_written
FROM pg_stat_statements
ORDER BY temp_blks_written DESC
LIMIT 10;
```

### 4.3 重置统计

```sql
-- 重置所有统计
SELECT pg_stat_statements_reset();

-- 重置特定查询（PG 14+）
SELECT pg_stat_statements_reset(userid, dbid, queryid);
```

### 4.4 性能分析工作流

```
1. 重置统计: SELECT pg_stat_statements_reset();
2. 运行业务负载
3. 查询 top SQL
4. EXPLAIN ANALYZE 分析慢查询
5. 优化（索引/SQL改写/配置调整）
6. 重新统计验证效果
```

## 5. 其他常用扩展

| 扩展            | 用途                                 |
| --------------- | ------------------------------------ |
| `pg_trgm`       | 模糊搜索、相似度匹配                 |
| `pgcrypto`      | 加密函数、UUID 生成                  |
| `hstore`        | 键值对存储                           |
| `ltree`         | 层级路径数据                         |
| `btree_gin`     | GIN 索引支持 btree 类型              |
| `intarray`      | 整数数组操作                         |
| `unaccent`      | 去除重音符号                         |
| `fuzzystrmatch` | 字符串相似度（Soundex、Levenshtein） |
| `pg_cron`       | 定时任务                             |
| `pg_repack`     | 在线清理膨胀                         |

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
| 扩展模块详解 | 043-ExtensionModuleDetailed | 本文自身 |
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
