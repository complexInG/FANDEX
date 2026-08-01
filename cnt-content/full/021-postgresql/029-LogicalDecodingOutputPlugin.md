---
order: 74
title: 逻辑解码与输出插件
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL逻辑解码与输出插件：逻辑复制基础、pgoutput、wal2json与CDC
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/级联复制
  - postgresql/物理复制槽
  - postgresql/增量备份
  - postgresql/订阅与发布
prerequisites:
  - postgresql/概述与安装配置
---

## 1. 逻辑解码概述

逻辑解码将 WAL 日志解析为逻辑变更事件（INSERT/UPDATE/DELETE），是逻辑复制和 CDC 的基础。

## 2. 逻辑复制槽

```sql
-- 创建逻辑复制槽
SELECT pg_create_logical_replication_slot('my_slot', 'pgoutput');

-- 查看逻辑槽
SELECT slot_name, slot_type, database, plugin
FROM pg_replication_slots WHERE slot_type = 'logical';

-- 删除
SELECT pg_drop_replication_slot('my_slot');
```

## 3. 输出插件

### 3.1 pgoutput（内置）

```sql
-- PostgreSQL 内置的逻辑解码输出插件
-- 用于逻辑复制的发布/订阅
SELECT pg_create_logical_replication_slot('pgoutput_slot', 'pgoutput');
```

### 3.2 wal2json

```sql
CREATE EXTENSION wal2json;

SELECT pg_create_logical_replication_slot('json_slot', 'wal2json');

-- 消费变更
SELECT data FROM pg_logical_slot_peek_changes('json_slot', NULL, NULL);
-- 输出 JSON 格式的变更事件
```

## 4. CDC 应用

```sql
-- 使用逻辑解码实现变更数据捕获
-- 1. 创建逻辑槽
-- 2. 定期消费变更事件
-- 3. 将变更发送到消息队列（Kafka等）

-- 消费并推进位置
SELECT data FROM pg_logical_slot_get_changes('json_slot', NULL, NULL);

-- 只查看不推进
SELECT data FROM pg_logical_slot_peek_changes('json_slot', NULL, NULL);
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
