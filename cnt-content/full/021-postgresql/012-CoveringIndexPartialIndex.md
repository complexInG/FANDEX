---
order: 56
title: 覆盖索引与部分索引
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL覆盖索引、部分索引、表达式索引：INCLUDE子句、条件索引与优化策略
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/事务ID回卷预防
  - postgresql/索引类型
  - postgresql/KNN向量索引
  - postgresql/查询优化
prerequisites:
  - postgresql/概述与安装配置
---

## 1. 覆盖索引（INCLUDE）

```sql
-- INCLUDE 子句将额外列存储在索引叶子节点
-- 不参与排序，但可用于覆盖查询
CREATE INDEX idx_employees_dept_cover
ON employees(dept_id) INCLUDE (name, salary);

-- 覆盖查询：不需要回表
SELECT name, salary FROM employees WHERE dept_id = 5;
-- Index Only Scan
```

## 2. 部分索引（Partial Index）

```sql
-- 只索引满足条件的行
CREATE INDEX idx_active_orders
ON orders(created_at) WHERE status = 'active';

-- 每个用户只有一个活跃订阅
CREATE UNIQUE INDEX uk_active_subscription
ON subscriptions(user_id) WHERE status = 'active';

-- 查询必须匹配索引条件
SELECT * FROM orders WHERE status = 'active' AND created_at > '2026-01-01';
-- 使用 idx_active_orders
```

## 3. 表达式索引

```sql
-- 对表达式结果创建索引
CREATE INDEX idx_users_email_lower ON users(LOWER(email));

-- 查询必须使用相同的表达式
SELECT * FROM users WHERE LOWER(email) = 'test@example.com';
-- 使用索引

-- 日期提取
CREATE INDEX idx_orders_month ON orders(EXTRACT(MONTH FROM created_at));
```

## 4. 唯一索引与 NULL

```sql
-- PostgreSQL 唯一索引允许多个 NULL
CREATE UNIQUE INDEX uk_users_email ON users(email);
-- email = NULL 的行可以有多条

-- 部分唯一索引：排除 NULL
CREATE UNIQUE INDEX uk_users_email_notnull ON users(email) WHERE email IS NOT NULL;
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
