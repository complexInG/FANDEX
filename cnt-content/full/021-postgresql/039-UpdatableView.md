---
order: 84
title: 可更新视图
module: postgresql
category: PostgreSQL
difficulty: intermediate
description: 'PostgreSQL可更新视图：自动可更新条件、INSTEAD OF触发器、WITH CHECK OPTION'
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/序列与自增列
  - postgresql/生成列
  - postgresql/并行查询
  - postgresql/逻辑复制与物理复制对比
prerequisites:
  - postgresql/概述与安装配置
---

## 1. 自动可更新视图

PostgreSQL 自动使简单视图可更新：

```sql
CREATE VIEW active_employees AS
SELECT id, name, salary, dept_id
FROM employees
WHERE status = 'active';

-- 可以直接 INSERT/UPDATE/DELETE
INSERT INTO active_employees (name, salary, dept_id)
VALUES ('Alice', 50000, 1);

UPDATE active_employees SET salary = 55000 WHERE name = 'Alice';

DELETE FROM active_employees WHERE name = 'Alice';
```

### 1.1 自动可更新条件

- 从单表选择
- 不包含聚合、窗口函数、GROUP BY、HAVING、DISTINCT
- 不包含 UNION/INTERSECT/EXCEPT
- SELECT 列直接引用表列（无表达式）

## 2. WITH CHECK OPTION

```sql
-- 确保通过视图插入/更新的行满足视图条件
CREATE VIEW active_employees AS
SELECT id, name, salary, dept_id
FROM employees
WHERE status = 'active'
WITH CHECK OPTION;

-- 以下操作会被拒绝
INSERT INTO active_employees (name, salary, dept_id, status)
VALUES ('Bob', 50000, 1, 'inactive');
-- ERROR: new row violates check option for view "active_employees"
```

## 3. INSTEAD OF 触发器

```sql
-- 复杂视图需要 INSTEAD OF 触发器
CREATE VIEW employee_details AS
SELECT e.id, e.name, e.salary, d.dept_name
FROM employees e JOIN departments d ON e.dept_id = d.id;

CREATE OR REPLACE FUNCTION update_employee_details()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE employees SET name = NEW.name, salary = NEW.salary
    WHERE id = NEW.id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_employee_details
INSTEAD OF UPDATE ON employee_details
FOR EACH ROW EXECUTE FUNCTION update_employee_details();
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
