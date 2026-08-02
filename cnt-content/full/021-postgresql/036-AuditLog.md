---
order: 81
title: 审计日志
module: postgresql
category: PostgreSQL
difficulty: intermediate
description: PostgreSQL审计日志：pgAudit扩展、日志配置、审计策略与合规要求
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/行级安全策略
  - postgresql/数据加密存储
  - postgresql/序列与自增列
  - postgresql/生成列
prerequisites:
  - postgresql/概述与安装配置
---

## 1. pgAudit 扩展

```sql
CREATE EXTENSION pgaudit;
```

```ini
# postgresql.conf
shared_preload_libraries = 'pgaudit'

# 审计级别
pgaudit.log = 'all'           -- 所有操作
pgaudit.log = 'read,write'    -- 读写操作
pgaudit.log = 'ddl'           -- DDL操作
pgaudit.log = 'role'          -- 角色操作

# 审计日志格式
pgaudit.log_line_prefix = '%t [%p]: '
pgaudit.log_relation = on     -- 记录表名
```

## 2. 审计日志示例

```
2026-06-14 10:30:00 UTC [12345]: LOG:  AUDIT: SESSION,1,1,WRITE,INSERT,,,
    INSERT INTO employees (name, salary) VALUES ('Alice', 50000);,<none>
2026-06-14 10:30:01 UTC [12345]: LOG:  AUDIT: SESSION,1,2,READ,SELECT,,,
    SELECT * FROM employees WHERE dept_id = 5;,<none>
```

## 3. 对象级审计

```sql
-- 审计特定表
ALTER TABLE employees SET (pgaudit.log = 'read,write');

-- 审计特定角色
ALTER ROLE admin SET pgaudit.log = 'all';
```

## 4. 原生日志审计

```ini
# 不使用pgAudit时的替代方案
log_statement = 'all'          -- 记录所有SQL
log_statement = 'ddl'          -- 只记录DDL
log_statement = 'mod'          -- 记录DML+DDL
log_min_duration_statement = 0 -- 记录所有语句及执行时间
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
