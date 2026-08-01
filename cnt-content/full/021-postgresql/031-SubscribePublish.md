---
order: 76
title: 订阅与发布
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL逻辑复制：发布与订阅、选择性复制、冲突处理与监控
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/逻辑解码与输出插件
  - postgresql/增量备份
  - 'postgresql/SSL-TLS加密连接'
  - postgresql/基于角色的权限管理
prerequisites:
  - postgresql/概述与安装配置
---

## 1. 逻辑复制概述

逻辑复制基于发布/订阅模型，在表级别复制数据变更。

## 2. 发布端配置

```sql
-- 创建发布
CREATE PUBLICATION my_pub FOR TABLE employees, departments;

-- 发布所有表
CREATE PUBLICATION all_tables FOR ALL TABLES;

-- 发布特定模式
CREATE PUBLICATION schema_pub FOR TABLES IN SCHEMA public;

-- 查看发布
SELECT * FROM pg_publication;
SELECT * FROM pg_publication_tables;
```

## 3. 订阅端配置

```sql
-- 创建订阅
CREATE SUBSCRIPTION my_sub
CONNECTION 'host=publisher-host dbname=mydb user=replicator password=password'
PUBLICATION my_pub;

-- 查看订阅
SELECT * FROM pg_subscription;
SELECT * FROM pg_stat_subscription;
```

## 4. 冲突处理

```sql
-- 逻辑复制冲突时，订阅端会停止
-- 查看冲突
SELECT * FROM pg_stat_subscription;

-- 解决方案1：跳过冲突事务
ALTER SUBSCRIPTION my_sub SKIP (lsn = '0/12345678');

-- 解决方案2：手动修复数据后重启
-- 修复冲突数据
ALTER SUBSCRIPTION my_sub DISABLE;
-- 修复后重新启用
ALTER SUBSCRIPTION my_sub ENABLE;
```

## 5. 监控

```sql
-- 发布端
SELECT * FROM pg_stat_replication;

-- 订阅端
SELECT subname, pid, received_lsn, latest_end_lsn,
       latest_end_time
FROM pg_stat_subscription;
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
