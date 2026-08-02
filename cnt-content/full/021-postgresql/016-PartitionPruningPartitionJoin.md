---
order: 61
title: 分区裁剪与分区连接
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL分区裁剪与分区连接：运行时裁剪、分区智能连接与性能优化
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/查询优化
  - postgresql/分区表
  - postgresql/高级SQL
  - postgresql/MERGE语句增强
prerequisites:
  - postgresql/概述与安装配置
---

## 1. 分区裁剪

### 1.1 计划时裁剪

```sql
-- WHERE 条件常量在计划时已知
EXPLAIN SELECT * FROM orders WHERE order_date = '2026-05-15';
-- 只扫描 orders_2026_q2
```

### 1.2 运行时裁剪

```sql
-- 参数化查询在执行时裁剪
PREPARE get_orders(DATE) AS
    SELECT * FROM orders WHERE order_date = $1;
EXPLAIN EXECUTE get_orders('2026-05-15');
-- Append
--   Subplans Removed: 3  -- 运行时裁剪了3个分区
```

## 2. 分区连接（Partitionwise Join）

```sql
-- 当两表都是分区表且分区策略匹配时
-- PostgreSQL 可以逐分区连接

SET enable_partitionwise_join = ON;

EXPLAIN SELECT * FROM orders o JOIN order_items oi ON o.id = oi.order_id;
-- 每对对应分区单独连接
-- 减少内存使用和计算量
```

## 3. 分区聚合

```sql
SET enable_partitionwise_aggregate = ON;

-- 逐分区聚合后合并
SELECT order_date, SUM(amount) FROM orders GROUP BY order_date;
-- 每个分区先聚合，然后合并结果
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
