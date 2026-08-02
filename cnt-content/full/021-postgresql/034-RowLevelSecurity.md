---
order: 340
title: 行级安全策略
module: 'postgresql'
category: 数据库
difficulty: advanced
description: PostgreSQL行级安全策略RLS：策略定义、角色策略、WITH CHECK与多租户隔离
author: fanquanpp
updated: '2026-08-01'
related:
  - 'postgresql/032-SSLEncryptionConnection'
  - 'postgresql/033-RoleBasedPermissionManagement'
  - 'postgresql/035-DataEncryptionStorage'
  - 'postgresql/036-AuditLog'
prerequisites:
  - 'postgresql/001-OverviewInstallConfig'
---


## 1. RLS 概述

行级安全策略（Row-Level Security，RLS）控制用户可以访问哪些行。

## 2. 启用RLS

```sql
-- 启用表级RLS
ALTER TABLE employees ENABLE ROW LEVEL SECURITY;

-- 表所有者默认不受RLS限制
-- 强制所有者也受RLS限制
ALTER TABLE employees FORCE ROW LEVEL SECURITY;
```

## 3. 创建策略

```sql
-- 用户只能看到自己部门的员工
CREATE POLICY dept_isolation ON employees
    USING (dept_id = current_user_dept());

-- 只读策略
CREATE POLICY read_own_dept ON employees
    FOR SELECT USING (dept_id = current_user_dept());

-- 插入策略
CREATE POLICY insert_own_dept ON employees
    FOR INSERT WITH CHECK (dept_id = current_user_dept());

-- 更新策略
CREATE POLICY update_own_dept ON employees
    FOR UPDATE USING (dept_id = current_user_dept())
    WITH CHECK (dept_id = current_user_dept());

-- 删除策略
CREATE POLICY delete_own_dept ON employees
    FOR DELETE USING (dept_id = current_user_dept());
```

## 4. 多租户隔离

```sql
-- 租户隔离
CREATE POLICY tenant_isolation ON orders
    USING (tenant_id = current_setting('app.tenant_id')::INTEGER);

-- 设置租户ID
SET app.tenant_id = '42';
SELECT * FROM orders;  -- 只能看到 tenant_id=42 的订单
```

## 5. 策略管理

```sql
-- 查看策略
SELECT * FROM pg_policies WHERE tablename = 'employees';

-- 删除策略
DROP POLICY dept_isolation ON employees;

-- 禁用RLS
ALTER TABLE employees DISABLE ROW LEVEL SECURITY;
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
