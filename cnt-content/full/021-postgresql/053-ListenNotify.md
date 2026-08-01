---
order: 530
title: LISTEN/NOTIFY 监听通知 语法速查手册
module: postgresql

category: '021-postgresql'
difficulty: beginner
description: LISTEN/NOTIFY 监听通知 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## NOTIFY 发送通知

**基本写法：发送通知**
`NOTIFY <通道名>[, '<载荷>'];`

```sql
-- 发送通道通知（无载荷）
NOTIFY user_update;
-- 发送带载荷的通知（载荷必须是字符串）
NOTIFY order_event, '{"order_id":1001,"action":"created"}';
```

**基本写法：pg_notify 函数发送通知**
`SELECT pg_notify('<通道名>', '<载荷>');`

```sql
-- 使用函数形式发送（载荷支持任意字符串）
SELECT pg_notify('task_queue', '{"task":"send_email","to":"user@example.com"}');
```

**基本写法：事务提交时触发通知**
`NOTIFY <通道> -- 在事务中`

```sql
-- 通知在事务提交时才真正发送（事务回滚则不发）
BEGIN;
UPDATE orders SET status = 'paid' WHERE id = 1001;
NOTIFY order_event, '{"order_id":1001,"status":"paid"}';
COMMIT;
```

---

## LISTEN 监听通道

**基本写法：监听通道**
`LISTEN <通道名>;`

```sql
-- 当前会话开始监听指定通道
LISTEN order_event;
-- 监听后该通道的通知会被异步推送到此会话
```

**基本写法：取消监听**
`UNLISTEN <通道名>;`

```sql
-- 停止监听指定通道
UNLISTEN order_event;
-- 停止所有通道监听
UNLISTEN *;
```

---

## 接收通知

**基本写法：psql 接收通知**
`LISTEN <通道>;`

```sql
-- 在 psql 中监听后，通知会自动显示
LISTEN order_event;
-- 当其他会话执行 NOTIFY 时，本会话显示:
-- Asynchronous notification "order_event" with payload "..." received from server process PID xxx.
```

**基本写法：应用轮询接收**
`SELECT 1; -- 触发通知接收`

```sql
-- 驱动通常需执行任意查询才能拉取排队中的通知
-- libpq 使用 PQnotifies 获取通知
-- JDBC 使用 PGNotification 接口
LISTEN order_event;
-- 定期执行轻量查询拉取通知
SELECT pg_notification_queue_usage();  -- 查看队列使用率
```

**基本写法：查看监听状态**
`SELECT * FROM pg_listening_channels();`

```sql
-- 查看当前会话监听的所有通道
SELECT pg_listening_channels();
-- 查看所有会话的监听（需超级用户）
SELECT pid, channel FROM pg_stat_activity
WHERE query LIKE 'LISTEN%';
```

---

## 实战模式

**基本写法：触发器配合 NOTIFY**
`CREATE TRIGGER ... AFTER ... DO NOTIFY <通道>, '<载荷>';`

```sql
-- 表变更时自动通知（监听方据载荷处理）
CREATE OR REPLACE FUNCTION notify_order_change()
RETURNS trigger AS $$
BEGIN
  PERFORM pg_notify('order_event',
    json_build_object('id', NEW.id, 'action', TG_OP)::text);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_order_notify
AFTER INSERT OR UPDATE OR DELETE ON orders
FOR EACH ROW EXECUTE FUNCTION notify_order_change();
```

**基本写法：队列模式（任务分发）**
`NOTIFY <通道>, '<任务JSON>'`

```sql
-- 生产者插入任务并通知
INSERT INTO task_queue (task_type, payload)
VALUES ('email', '{"to":"u@e.com"}');
NOTIFY task_available;
-- 消费者监听并拉取处理
LISTEN task_available;
-- 收到通知后查询并锁定任务
SELECT id, payload FROM task_queue
WHERE status = 'pending'
FOR UPDATE SKIP LOCKED LIMIT 1;
```

---

## 注意事项

**基本写法：载荷大小限制**
`NOTIFY <通道>, '<载荷>' -- 载荷不超过 8000 字节`

```sql
-- 载荷字符串需小于 8000 字节
-- 大数据建议只传 ID，监听方再查表
NOTIFY large_change, '{"id": 1001}';  -- 仅传 ID
-- 监听方接收后再查表
-- SELECT * FROM changes WHERE id = 1001;
```

**基本写法：查看通知队列使用率**
`SELECT pg_notification_queue_usage();`

```sql
-- 查看通知队列使用率（0-1，超过 0.5 需注意消费速度）
SELECT pg_notification_queue_usage();
```

**基本写法：清理堆积通知**
`UNLISTEN <通道>; LISTEN <通道>;`

```sql
-- 重新监听可清空当前会话已排队但未消费的通知
UNLISTEN order_event;
LISTEN order_event;
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
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文自身 |
