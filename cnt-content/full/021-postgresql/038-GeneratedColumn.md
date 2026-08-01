---
order: 83
title: 生成列
module: postgresql
category: PostgreSQL
difficulty: intermediate
description: PostgreSQL生成列：STORED生成列、VIRTUAL生成列、表达式计算与索引支持
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/审计日志
  - postgresql/序列与自增列
  - postgresql/可更新视图
  - postgresql/并行查询
prerequisites:
  - postgresql/概述与安装配置
---

## 1. 生成列概述

生成列（Generated Column）的值由表达式自动计算，不能手动插入或更新。

## 2. STORED 生成列

```sql
-- 值存储在磁盘上
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    price NUMERIC(10,2),
    tax_rate NUMERIC(5,4) DEFAULT 0.13,
    total_price NUMERIC(10,2) GENERATED ALWAYS AS (price * (1 + tax_rate)) STORED
);

-- 插入时自动计算 total_price
INSERT INTO products (price) VALUES (100);
-- total_price = 100 * 1.13 = 113.00
```

## 3. 表达式限制

```sql
-- 生成列表达式必须是不可变的（IMMUTABLE）
-- 不能使用：随机函数、当前时间、子查询、其他表的列

-- 正确
full_name VARCHAR(200) GENERATED ALWAYS AS (first_name || ' ' || last_name) STORED

-- 错误
created_year INT GENERATED ALWAYS AS (EXTRACT(YEAR FROM created_at)) STORED
-- EXTRACT 不是 IMMUTABLE（依赖时区设置）

-- 修正：使用确定性表达式
created_year INT GENERATED ALWAYS AS (EXTRACT(YEAR FROM created_at::timestamp)) STORED
```

## 4. 索引支持

```sql
-- 可以在生成列上创建索引
CREATE INDEX idx_products_total ON products(total_price);

-- 用于函数索引的替代
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    data JSONB,
    status VARCHAR(20) GENERATED ALWAYS AS (data->>'status') STORED
);
CREATE INDEX idx_orders_status ON orders(status);
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
