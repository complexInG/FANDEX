---
order: 250
title: FDW外部数据包装器
module: 'postgresql'
category: 数据库
difficulty: advanced
description: PostgreSQL FDW外部数据包装器：跨数据库查询、postgres_fdw、文件FDW与数据联邦
author: fanquanpp
updated: '2026-08-01'
related:
  - 'postgresql/023-TriggerEventTrigger'
  - 'postgresql/024-ExtensionModule'
  - 'postgresql/026-StreamingReplication'
  - 'postgresql/027-CascadingReplication'
prerequisites:
  - 'postgresql/001-OverviewInstallConfig'
---


## 1. FDW 概述

外部数据包装器（Foreign Data Wrapper，FDW）允许 PostgreSQL 访问外部数据源，像查询本地表一样查询远程数据。

## 2. postgres_fdw

```sql
-- 安装扩展
CREATE EXTENSION postgres_fdw;

-- 创建外部服务器
CREATE SERVER remote_db
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host 'remote-host', dbname 'remotedb', port '5432');

-- 创建用户映射
CREATE USER MAPPING FOR current_user
SERVER remote_db
OPTIONS (user 'remote_user', password 'password');

-- 导入外部表
IMPORT FOREIGN SCHEMA public
LIMIT TO (employees, departments)
FROM SERVER remote_db INTO public;

-- 或手动创建
CREATE FOREIGN TABLE remote_employees (
    id INTEGER,
    name VARCHAR(100),
    salary NUMERIC
) SERVER remote_db
OPTIONS (schema_name 'public', table_name 'employees');

-- 查询外部表
SELECT * FROM remote_employees WHERE salary > 50000;
```

## 3. 文件 FDW

```sql
CREATE EXTENSION file_fdw;

CREATE SERVER csv_server
FOREIGN DATA WRAPPER file_fdw;

CREATE FOREIGN TABLE csv_data (
    id INTEGER,
    name VARCHAR(100),
    value NUMERIC
) SERVER csv_server
OPTIONS (filename '/data/export.csv', format 'csv', header 'true');
```

## 4. 下推优化

```sql
-- postgres_fdw 支持 WHERE 条件下推
-- 远程数据库执行过滤，减少数据传输

-- 启用下推
ALTER SERVER remote_db OPTIONS (ADD fetch_size '10000');

-- 查看下推情况
EXPLAIN VERBOSE
SELECT * FROM remote_employees WHERE salary > 50000;
-- Remote SQL: SELECT id, name, salary FROM public.employees WHERE ((salary > 5000.0))
```

## 延伸阅读
PostgreSQL 窗口函数，见 021-postgresql 模块文档。
PostgreSQL 递归查询，见 021-postgresql 模块相关文档。
SQL 基础，见 019-sql 模块。
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
