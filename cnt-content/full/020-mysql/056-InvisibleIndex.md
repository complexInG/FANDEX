---
order: 93
title: 不可见索引
module: mysql
category: MySQL
difficulty: intermediate
description: MySQL不可见索引：索引可见性控制、优化器忽略、安全删除索引与灰度验证
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/JSON模式验证与聚合函数
  - mysql/复制与高可用
  - mysql/性能调优与安全
  - mysql/函数索引
prerequisites:
  - mysql/语法速查
---

## 1. 不可见索引概述

不可见索引（Invisible Index）对优化器不可见，但仍然被维护（INSERT/UPDATE/DELETE 仍更新索引）。

## 2. 语法

```sql
-- 创建不可见索引
CREATE INDEX idx_name ON employees(name) INVISIBLE;

-- 修改索引可见性
ALTER TABLE employees ALTER INDEX idx_name INVISIBLE;
ALTER TABLE employees ALTER INDEX idx_name VISIBLE;

-- 查看索引可见性
SELECT index_name, is_visible
FROM information_schema.statistics
WHERE table_name = 'employees';
```

## 3. 使用场景

### 3.1 安全删除索引

```sql
-- 步骤1：将索引设为不可见
ALTER TABLE employees ALTER INDEX idx_old INVISIBLE;

-- 步骤2：观察一段时间，确认无性能问题
-- 如果出现问题，快速恢复
ALTER TABLE employees ALTER INDEX idx_old VISIBLE;

-- 步骤3：确认安全后删除
DROP INDEX idx_old ON employees;
```

### 3.2 灰度测试新索引

```sql
-- 创建不可见的新索引
CREATE INDEX idx_new ON employees(dept_id, salary) INVISIBLE;

-- 特定会话测试
SET SESSION optimizer_switch = 'use_invisible_indexes=on';
EXPLAIN SELECT * FROM employees WHERE dept_id = 5 ORDER BY salary;
-- 可以使用新索引

-- 其他会话不受影响
```

## 4. 注意事项

```sql
-- 不可见索引仍被维护，写入开销不变
-- 主键索引不能设为不可见
-- UNIQUE 约束索引设为不可见后，约束仍然生效
```

## 延伸阅读
MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 InnoDB 日志与崩溃恢复

redo log 记录物理页修改（WAL：先写日志再写数据页），崩溃后重放恢复；环形文件组 + checkpoint 推进。
undo log 记录事务前镜像，支持回滚与 MVCC 版本链；purge 线程清理。
两阶段提交：redo prepare -> binlog -> redo commit，保证两份日志一致，主从不丢数据。
刷盘策略：innodb_flush_log_at_trx_commit=1 最安全（每次提交 fsync），2 每秒刷。

### 13.2 执行计划与优化器

EXPLAIN 关键列：type（const/ref/range/index/ALL）、key、rows、Extra（Using index/Using filesort）。
优化器基于统计信息选计划；analyze table 更新统计；hint（FORCE INDEX）谨慎使用。
排序与分组：filesort 优化为索引序；避免临时表。
慢查询治理流程：慢日志 -> 计划分析 -> 索引/改写 -> 验证。
