---
order: 72
title: 级联复制
module: postgresql
category: PostgreSQL
difficulty: intermediate
description: PostgreSQL级联复制：备库作为上游、多层级联架构与配置
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/FDW外部数据包装器
  - postgresql/流复制
  - postgresql/物理复制槽
  - postgresql/逻辑解码与输出插件
prerequisites:
  - postgresql/概述与安装配置
---

## 概述

级联复制（Cascading Replication）是 PostgreSQL 流复制的扩展能力，允许备库作为上游，将接收到的 WAL 数据继续转发给其他备库。这种架构可以有效减少主库的复制负载，特别是在需要多个备库的场景下。级联复制广泛应用于跨数据中心部署、读写分离和报表分流等场景，是构建高可用和大规模读取架构的重要手段。

## 基础概念

**级联备库（Cascading Standby）**：既是主库的下游（接收 WAL），又是其他备库的上游（转发 WAL）。级联备库必须启用 hot_standby 参数。

**WAL 发送进程**：主库和级联备库都会启动 wal_sender 进程来发送 WAL。级联备库的 max_wal_senders 参数决定了它能向多少个下游备库转发。

**复制拓扑**：级联复制形成树状拓扑结构。主库是根节点，级联备库是中间节点，叶子备库是末端节点。每一级只从其上游接收 WAL。

**流复制协议**：级联备库使用与主库相同的流复制协议向下游发送 WAL，下游备库的配置方式与直连主库基本相同。

## 快速上手

### 基本架构

```
主库 (Primary)
  |
  +-- 级联备库1 (Cascade Standby 1)
  |     |
  |     +-- 备库2 (Standby 2)
  |     +-- 备库3 (Standby 3)
  |
  +-- 级联备库4 (Cascade Standby 4)
        |
        +-- 备库5 (Standby 5)
```

### 级联备库配置

```ini
# 级联备库的 postgresql.conf
# 启用热备份（允许只读查询）
hot_standby = on

# 允许向下游发送 WAL
max_wal_senders = 10

# WAL 保留大小
wal_keep_size = '1GB'

# 监听所有地址（允许下游备库连接）
listen_addresses = '*'
```

```ini
# 级联备库的 pg_hba.conf
# 允许下游备库的复制连接
# TYPE  DATABASE  USER        ADDRESS         METHOD
host    replication  replicator  192.168.2.0/24  md5
```

### 下游备库配置

```ini
# 下游备库的 postgresql.conf
# primary_conninfo 指向级联备库而非主库
primary_conninfo = 'host=cascade-standby-1 port=5432 user=replicator password=secret'

# 可选：指定复制槽
primary_slot_name = 'standby2'

# 启用热备份
hot_standby = on
```

## 详细用法

### 多层级联架构

```
主库 (Primary) - 数据中心A
  |
  +-- 同城级联备库 (Cascade DC-A)
  |     |
  |     +-- 同城只读备库1
  |     +-- 同城只读备库2
  |
  +-- 异地级联备库 (Cascade DC-B)
        |
        +-- 异地只读备库1
        +-- 异地只读备库2
```

```ini
# 主库配置
# postgresql.conf
wal_level = replica
max_wal_senders = 10
wal_keep_size = '2GB'

# pg_hba.conf
host  replication  replicator  10.0.1.0/24  md5  # 同城级联
host  replication  replicator  10.0.2.0/24  md5  # 异地级联
```

```ini
# 同城级联备库配置
# postgresql.conf
hot_standby = on
max_wal_senders = 5
primary_conninfo = 'host=primary port=5432 user=replicator password=secret'
primary_slot_name = 'cascade_dc_a'

# pg_hba.conf
host  replication  replicator  10.0.1.0/24  md5
```

```ini
# 异地级联备库配置
# postgresql.conf
hot_standby = on
max_wal_senders = 5
primary_conninfo = 'host=primary port=5432 user=replicator password=secret'
primary_slot_name = 'cascade_dc_b'

# pg_hba.conf
host  replication  replicator  10.0.2.0/24  md5
```

### 级联复制与复制槽

```sql
-- 在主库上为级联备库创建复制槽
SELECT pg_create_physical_replication_slot('cascade_dc_a');
SELECT pg_create_physical_replication_slot('cascade_dc_b');

-- 在级联备库上为下游备库创建复制槽
-- 注意：级联备库也需要创建复制槽
SELECT pg_create_physical_replication_slot('standby_ro_1');
SELECT pg_create_physical_replication_slot('standby_ro_2');

-- 查看主库的复制状态
SELECT
    pid,
    usename,
    application_name,
    client_addr,
    state,
    sent_lsn,
    write_lsn,
    flush_lsn,
    replay_lsn
FROM pg_stat_replication;

-- 查看级联备库的复制状态
-- 级联备库上也能看到下游备库的连接
SELECT pid, application_name, client_addr, state, sync_state
FROM pg_stat_replication;
```

### 同步复制与级联

```ini
# 主库配置同步复制
# postgresql.conf
synchronous_standby_names = 'FIRST 1 (cascade_dc_a, cascade_dc_b)'

# 注意：同步复制只适用于直连主库的备库
# 下游备库（通过级联备库连接）不参与同步投票
```

```sql
-- 查看同步状态
SELECT
    pid,
    application_name,
    sync_state,
    sync_priority
FROM pg_stat_replication;

-- sync_state 值：
-- 'sync'    : 同步备库
-- 'async'   : 异步备库
-- 'quorum'  : 法定人数备库
-- 'potential': 潜在同步备库
```

## 常见场景

### 报表分流架构

```
主库 (OLTP 读写)
  |
  +-- 级联备库 (报表专用)
        |
        +-- 报表只读备库1 (BI查询)
        +-- 报表只读备库2 (实时分析)
```

```ini
# 报表级联备库配置
# postgresql.conf
hot_standby = on
max_wal_senders = 5
max_standby_streaming_delay = '30s'  # 允许查询与恢复冲突时延迟
wal_receiver_status_interval = '10s'

# 优化报表查询性能
shared_buffers = '4GB'
work_mem = '256MB'
effective_cache_size = '12GB'
```

```sql
-- 应用层路由：将报表查询导向级联备库
-- 使用连接池（如 PgBouncer）实现读写分离

-- 检查备库是否已追上主库
SELECT
    now() - pg_last_xact_replay_timestamp() AS replication_lag;

-- 如果延迟过大，可以拒绝报表查询
SELECT CASE
    WHEN now() - pg_last_xact_replay_timestamp() > interval '5 seconds'
    THEN false
    ELSE true
END AS is_up_to_date;
```

### 灾备切换

```bash
# 当主库故障时，级联备库可以提升为新主库
# 下游备库需要重新指向新主库

# 步骤1：提升级联备库为新主库
pg_ctl -D /data promote

# 步骤2：下游备库修改 primary_conninfo
# 指向新的主库地址

# 步骤3：重启下游备库
pg_ctl -D /data restart

# 或者使用 pg_rewind 回溯
# 如果下游备库已经与旧主库产生了分歧
```

### 延迟备库

```ini
# 延迟备库配置：故意延迟应用 WAL
# 用于恢复误删除数据

# postgresql.conf
# 延迟 1 小时应用 WAL
recovery_min_apply_delay = '1h'

primary_conninfo = 'host=cascade-standby port=5432 user=replicator password=secret'
```

```sql
-- 延迟备库的使用场景
-- 如果在主库上误删除了数据，延迟备库仍然保留着删除前的数据

-- 查看延迟备库的当前时间点
SELECT pg_last_xact_replay_timestamp();

-- 从延迟备库导出误删除的数据
COPY (SELECT * FROM important_table WHERE id IN (...))
TO '/tmp/recovery_data.csv' WITH CSV HEADER;

-- 然后在主库上恢复数据
```

## 注意事项

- **复制延迟叠加**：级联复制中，每一级都会增加复制延迟。下游备库的数据落后于主库的时间等于所有上游的延迟之和。对延迟敏感的应用应直连主库。
- **max_wal_senders 配置**：级联备库需要为下游备库预留足够的 wal_sender 进程。如果下游备库数量超过 max_wal_senders，新的连接将被拒绝。
- **网络带宽**：级联备库需要同时接收和发送 WAL，网络带宽需求较高。在跨数据中心部署时，确保网络带宽充足。
- **故障切换复杂性**：级联架构的故障切换比单层复制更复杂。需要考虑级联备库提升后下游备库的重新指向问题。
- **监控覆盖**：每一级都需要监控复制状态和延迟。只监控主库的 pg_stat_replication 无法发现下游的问题。

## 进阶用法

### 自动化故障切换

```yaml
# Patroni 级联复制配置
# patroni.yml - 级联备库配置
scope: postgres-cluster
name: cascade-standby-1

restapi:
  listen: 0.0.0.0:8008

postgresql:
  data_dir: /var/lib/postgresql/data
  parameters:
    hot_standby: 'on'
    max_wal_senders: 10
    wal_keep_size: '1GB'

  # 级联复制配置
  replication:
    # 指定上游节点
    follow: primary

# 下游备库配置
# patroni.yml - 下游备库
scope: postgres-cluster
name: standby-2

postgresql:
  data_dir: /var/lib/postgresql/data
  parameters:
    hot_standby: 'on'

  replication:
    # 指向级联备库
    follow: cascade-standby-1
```

### 级联复制监控脚本

```sql
-- 创建级联复制监控视图
CREATE OR REPLACE VIEW v_cascade_replication_status AS
WITH upstream AS (
    SELECT
        pid,
        application_name,
        client_addr,
        state,
        sent_lsn,
        replay_lsn,
        pg_wal_lsn_diff(sent_lsn, replay_lsn) AS replay_lag_bytes,
        sync_state
    FROM pg_stat_replication
),
local_status AS (
    SELECT
        pg_is_in_recovery() AS is_standby,
        pg_last_xact_replay_timestamp() AS last_replay,
        now() - pg_last_xact_replay_timestamp() AS replication_delay
)
SELECT
    (SELECT is_standby FROM local_status) AS is_standby,
    (SELECT replication_delay FROM local_status) AS local_delay,
    u.application_name AS downstream_name,
    u.client_addr AS downstream_addr,
    u.state AS downstream_state,
    pg_size_pretty(u.replay_lag_bytes) AS downstream_lag,
    u.sync_state
FROM upstream u;

-- 查询级联复制状态
SELECT * FROM v_cascade_replication_status;
```

### 多活数据中心架构

```
数据中心A                    数据中心B
主库A (读写)                 主库B (读写)
  |                            |
  +-- 级联备库A1              +-- 级联备库B1
  |     |                      |     |
  |     +-- 只读备库A2        |     +-- 只读备库B2
  |                            |
  +--- 双向逻辑复制 -----------+
       (双向数据同步)
```

```sql
-- 双活架构中，级联复制用于本地读取分流
-- 逻辑复制用于跨数据中心的数据同步

-- 数据中心A的级联备库配置
-- postgresql.conf
hot_standby = on
max_wal_senders = 10
primary_conninfo = 'host=primary-a port=5432 user=replicator'

-- 同时配置逻辑复制发布
CREATE PUBLICATION data_center_a FOR TABLE shared_table1, shared_table2;

-- 数据中心B订阅
CREATE SUBSCRIPTION data_center_b_sub
CONNECTION 'host=primary-b port=5432 user=replicator'
PUBLICATION data_center_b;
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
| 级联复制 | 027-CascadingReplication | 本文自身 |
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
