---
order: 63
title: MERGE语句增强
module: postgresql
category: PostgreSQL
difficulty: advanced
description: 'PostgreSQL MERGE语句增强：UPSERT、RETURNING与条件操作'
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/分区裁剪与分区连接
  - postgresql/高级SQL
  - postgresql/JSON表格函数
  - postgresql/全文检索
prerequisites:
  - postgresql/概述与安装配置
---

## 1. MERGE 语法

```sql
MERGE INTO target_table t
USING source_table s
ON t.key = s.key
WHEN MATCHED THEN
    UPDATE SET col = s.col
WHEN NOT MATCHED THEN
    INSERT (key, col) VALUES (s.key, s.col);
```

## 2. 条件操作

```sql
MERGE INTO employees e
USING new_employees n
ON e.id = n.id
WHEN MATCHED AND e.salary < n.salary THEN
    UPDATE SET salary = n.salary, updated_at = NOW()
WHEN MATCHED AND e.salary >= n.salary THEN
    DO NOTHING
WHEN NOT MATCHED THEN
    INSERT (id, name, salary) VALUES (n.id, n.name, n.salary);
```

## 3. RETURNING

```sql
-- MERGE with RETURNING
MERGE INTO employees e
USING (SELECT * FROM staging) s
ON e.id = s.id
WHEN MATCHED THEN
    UPDATE SET salary = s.salary
WHEN NOT MATCHED THEN
    INSERT (id, name, salary) VALUES (s.id, s.name, s.salary)
RETURNING
    merge_action() AS action,
    id, name, salary;
-- action: 'INSERT' 或 'UPDATE'
```

## 4. UPSERT 替代

```sql
-- 简单 UPSERT 仍可用 INSERT ON CONFLICT
INSERT INTO employees (id, name, salary)
VALUES (1, 'Alice', 50000)
ON CONFLICT (id) DO UPDATE SET salary = EXCLUDED.salary;
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
