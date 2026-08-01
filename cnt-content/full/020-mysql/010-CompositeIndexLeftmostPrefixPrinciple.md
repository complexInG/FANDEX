---
order: 54
title: 联合索引与最左前缀原则
module: mysql
category: MySQL
difficulty: advanced
description: MySQL联合索引与最左前缀原则：索引结构、匹配规则、跳列场景与索引设计策略
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/NDB集群
  - mysql/聚簇索引与二级索引
  - mysql/索引下推
  - mysql/全文索引
prerequisites:
  - mysql/语法速查
---

## 1. 联合索引结构

联合索引（复合索引）是在多个列上创建的索引，按照定义列的顺序在 B+树中排序。

```sql
-- 创建联合索引
CREATE INDEX idx_abc ON table_name(a, b, c);

-- B+树排序规则：
-- 先按 a 排序，a 相同按 b 排序，b 相同按 c 排序
-- 索引项：(1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2,1)
```

## 2. 最左前缀原则

### 2.1 匹配规则

联合索引 `(a, b, c)` 可以支持以下查询模式：

| WHERE 条件                | 使用索引 | 说明         |
| ------------------------- | -------- | ------------ |
| a = 1                     | a        | 最左列       |
| a = 1 AND b = 2           | a, b     | 最左两列     |
| a = 1 AND b = 2 AND c = 3 | a, b, c  | 全部列       |
| b = 2                     |          | 跳过最左列   |
| c = 3                     |          | 跳过最左列   |
| b = 2 AND c = 3           |          | 跳过最左列   |
| a = 1 AND c = 3           | a        | 跳过中间列 b |

### 2.2 范围查询中断

```sql
-- 索引 (a, b, c)

-- 范围查询后的列无法使用索引
WHERE a > 1 AND b = 2       -- 只用 a，b 无法用索引
WHERE a = 1 AND b > 2 AND c = 3  -- 用 a, b，c 无法用索引
WHERE a = 1 AND b = 2 AND c > 3  -- 用 a, b, c 全部

-- 等值条件在前，范围条件在后
-- 索引设计时应将范围查询列放在最后
```

### 2.3 ORDER BY 与最左前缀

```sql
-- 索引 (a, b, c)

-- ORDER BY 可以利用索引避免 filesort
WHERE a = 1 ORDER BY b              --  使用索引排序
WHERE a = 1 ORDER BY b, c           --  使用索引排序
WHERE a = 1 ORDER BY c              --  跳过 b，需要 filesort
WHERE a = 1 AND b = 2 ORDER BY c    --  使用索引排序
ORDER BY a, b, c                    --  使用索引排序
ORDER BY b, c                       --  跳过 a
ORDER BY a DESC, b DESC, c DESC     --  降序也可用索引
ORDER BY a ASC, b DESC              --  排序方向不一致
```

## 3. 索引设计策略

### 3.1 列顺序原则

```sql
-- 原则1：等值条件列在前，范围条件列在后
-- 查询：WHERE status = 'active' AND created_at > '2026-01-01'
CREATE INDEX idx_status_created ON orders(status, created_at);

-- 原则2：高选择性列在前
-- 查询：WHERE city = '北京' AND gender = 'M'
-- city 选择性 > gender 选择性
CREATE INDEX idx_city_gender ON users(city, gender);

-- 原则3：考虑排序需求
-- 查询：WHERE dept_id = 5 ORDER BY salary DESC
CREATE INDEX idx_dept_salary ON employees(dept_id, salary DESC);
```

### 3.2 冗余索引检测

```sql
-- 索引 (a, b) 已经覆盖了 (a) 的功能
-- (a) 是冗余索引
CREATE INDEX idx_a ON table_name(a);       -- 冗余
CREATE INDEX idx_ab ON table_name(a, b);   -- 包含 a 的查询也能用

-- 但 (a, b) 不能替代 (b)
CREATE INDEX idx_b ON table_name(b);       -- 非冗余

-- 查看冗余索引
SELECT * FROM sys.schema_redundant_indexes;
```

### 3.3 联合索引 vs 多个单列索引

```sql
-- 场景：WHERE a = 1 AND b = 2

-- 方案1：联合索引（推荐）
CREATE INDEX idx_ab ON table_name(a, b);
-- 一次索引查找，效率高

-- 方案2：两个单列索引
CREATE INDEX idx_a ON table_name(a);
CREATE INDEX idx_b ON table_name(b);
-- 优化器可能使用 index_merge，效率不如联合索引
-- 且无法用于排序
```

## 参考文献

MySQL 官方文档：https://dev.mysql.com/doc/
MySQL 8.0 参考手册：https://dev.mysql.com/doc/refman/8.0/en/
High Performance MySQL（O'Reilly）：https://www.oreilly.com/library/view/high-performance-mysql/
Percona 博客：https://www.percona.com/blog/

## 延伸阅读

MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 高级课程。

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
