---
order: 490
title: pg_dump 与 pg_restore 语法速查手册
module: 021-postgresql
category: '021-postgresql'
difficulty: beginner
description: pg_dump 与 pg_restore 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## pg_dump 基本备份

**基本写法：备份单个数据库**
`pg_dump -U <用户名> -d <数据库名> -f <输出文件>`

```bash
# 备份 mydb 数据库到文件
pg_dump -U postgres -d mydb -f mydb_backup.sql
```

**基本写法：自定义压缩格式备份**
`pg_dump -U <用户名> -Fc -d <数据库名> -f <输出文件>.dump`

```bash
# 使用自定义压缩格式（支持选择性恢复，推荐）
pg_dump -U postgres -Fc -d mydb -f mydb.dump
```

**基本写法：目录格式备份（支持并行）**
`pg_dump -U <用户名> -Fd -d <数据库名> -f <输出目录>`

```bash
# 目录格式（每个表一个文件，支持并行恢复）
pg_dump -U postgres -Fd -d mydb -f mydb_dir/
```

**基本写法：并行备份**
`pg_dump -U <用户名> -Fd -j <并行数> -d <数据库名> -f <输出目录>`

```bash
# 4 个并行进程加速备份
pg_dump -U postgres -Fd -j 4 -d mydb -f mydb_dir/
```

---

## 选择性备份

**基本写法：仅备份指定表**
`pg_dump -U <用户名> -d <库名> -t <表名> [-t <表2>] -f <输出文件>`

```bash
# 仅备份 users 和 orders 表
pg_dump -U postgres -d mydb -t users -t orders -f tables_backup.sql
```

**基本写法：排除指定表**
`pg_dump -U <用户名> -d <库名> -T <表名> -f <输出文件>`

```bash
# 备份除 logs 表外的所有表
pg_dump -U postgres -d mydb -T logs -f mydb_no_logs.sql
```

**基本写法：仅备份数据/仅结构**
`pg_dump -U <用户名> -d <库名> --data-only -f <输出文件>`

```bash
# 仅备份数据（不含结构）
pg_dump -U postgres -d mydb --data-only -f mydb_data.sql
# 仅备份结构（不含数据）
pg_dump -U postgres -d mydb --schema-only -f mydb_schema.sql
```

---

## 全库与模式备份

**基本写法：备份所有数据库**
`pg_dumpall -U <用户名> -f <输出文件>`

```bash
# 备份所有数据库（含角色与表空间定义）
pg_dumpall -U postgres -f all_db_backup.sql
# 仅备份全局对象（角色、表空间）
pg_dumpall -U postgres --globals-only -f globals.sql
```

**基本写法：备份指定模式**
`pg_dump -U <用户名> -d <库名> -n <模式名> -f <输出文件>`

```bash
# 仅备份 business 模式
pg_dump -U postgres -d mydb -n business -f business_schema.sql
```

---

## pg_restore 恢复

**基本写法：从自定义格式恢复**
`pg_restore -U <用户名> -d <数据库名> <备份文件>.dump`

```bash
# 恢复自定义格式备份到指定数据库
pg_restore -U postgres -d mydb mydb.dump
```

**基本写法：从 SQL 文本恢复**
`psql -U <用户名> -d <数据库名> -f <备份文件>.sql`

```bash
# 恢复纯文本 SQL 备份
psql -U postgres -d mydb -f mydb_backup.sql
```

**基本写法：并行恢复**
`pg_restore -U <用户名> -d <库名> -j <并行数> <备份文件>.dump`

```bash
# 4 个并行进程加速恢复
pg_restore -U postgres -d mydb -j 4 mydb.dump
```

**基本写法：仅恢复结构/数据**
`pg_restore -U <用户名> -d <库名> --schema-only <备份文件>.dump`

```bash
# 仅恢复结构
pg_restore -U postgres -d mydb --schema-only mydb.dump
# 仅恢复数据
pg_restore -U postgres -d mydb --data-only mydb.dump
```

---

## 增量备份（17 新特性）

**基本写法：pg_basebackup 增量备份**
`pg_basebackup -U <用户名> -D <目录> -Fp -Xs -P --incremental <基础备份manifest路径>`

```bash
# PostgreSQL 17 増量基础备份
pg_basebackup -U postgres -D /backup/incr -Fp -Xs -P -c fast
```

**基本写法：pg_combinebackup 合并备份**
`pg_combinebackup <基础备份目录> <增量备份目录> -o <合并输出目录>`

```bash
# PostgreSQL 17 合并基础与增量备份
pg_combinebackup /backup/base /backup/incr -o /backup/combined
```

---

## 选项速查

**基本写法：连接选项**
`pg_dump -h <主机> -p <端口> -U <用户> -d <数据库>`

```bash
# 远程数据库备份
pg_dump -h 192.168.1.100 -p 5432 -U admin -d mydb -f remote.sql
```

**基本写法：压缩级别**
`pg_dump -U <用户> -Fc -Z <级别> -d <库名> -f <输出文件>`

```bash
# 指定压缩级别 0-9（9 最高压缩率）
pg_dump -U postgres -Fc -Z 6 -d mydb -f mydb.dump
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
| pg_dump 与 pg_restore 语法速查手册 | 049-PgDumpRestore | 本文自身 |
| 数组类型操作 语法速查手册 | 050-ArrayType | 本文的并列主题 |
| 模式（Schema）管理 语法速查手册 | 051-SchemaManagement | 本文的并列主题 |
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
