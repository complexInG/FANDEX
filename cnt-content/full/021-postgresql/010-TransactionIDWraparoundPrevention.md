---
order: 100
title: 事务ID回卷预防
module: 'postgresql'
category: 数据库
difficulty: advanced
description: PostgreSQL事务ID回卷预防：XID机制、FREEZE、autovacuum_freeze_max_age与紧急处理
author: fanquanpp
updated: '2026-08-01'
related:
  - 'postgresql/008-DeadlockDetectionHandling'
  - 'postgresql/009-VACUUMMechanism'
  - 'postgresql/011-IndexType'
  - 'postgresql/012-CoveringIndexPartialIndex'
prerequisites:
  - 'postgresql/001-OverviewInstallConfig'
---


## 1. 事务ID机制

PostgreSQL 事务ID（XID）是 32 位无符号整数，范围 $0 \sim 2^{31}-1$（约21亿）。

$$
\text{XID 空间} = [0, 2^{31}) \approx 2.1 \times 10^9
$$

## 2. 回卷问题

当 XID 达到最大值后回卷到 0，导致旧事务看起来像是未来事务，数据变得不可见。

```
XID 顺序：... → 2^31-2 → 2^31-1 → 0 → 1 → 2 → ...
                                    ↑ 回卷点
```

## 3. FREEZE 机制

```sql
-- VACUUM FREEZE 将旧行的 xmin 标记为 FrozenTransactionId
-- 冻结后的行对所有事务可见，不再依赖 XID 比较

-- 手动冻结
VACUUM FREEZE employees;

-- 自动冻结阈值
ALTER SYSTEM SET autovacuum_freeze_max_age = 200000000;  -- 2亿
-- 当 age(relfrozenxid) 超过此值，autovacuum 自动 FREEZE
```

## 4. 紧急处理

```sql
-- 查看接近回卷的数据库
SELECT datname, age(datfrozenxid) AS xid_age
FROM pg_database
ORDER BY xid_age DESC;

-- 如果 age 接近 autovacuum_freeze_max_age，需要紧急 VACUUM FREEZE
VACUUM FREEZE;

-- 最坏情况：数据库进入只读模式
-- 必须执行 VACUUM FREEZE 恢复
```

## 5. 监控

```sql
-- 查看各表的 XID 年龄
SELECT relname, age(relfrozenxid) AS xid_age,
       pg_size_pretty(pg_total_relation_size(oid)) AS size
FROM pg_class
WHERE relkind IN ('r', 'm')
ORDER BY xid_age DESC;

-- 设置告警
-- 当 age(relfrozenxid) > autovacuum_freeze_max_age * 0.8 时告警
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
