---
order: 66
title: 'GROUP-BY与ORDER-BY优化'
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL GROUP BY与ORDER BY优化：松散索引扫描、紧凑索引扫描、临时表与filesort优化'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/子查询优化
  - mysql/派生表优化
  - mysql/JOIN算法
  - mysql/事务隔离级别底层实现
prerequisites:
  - mysql/语法速查
---

## 1. GROUP BY 优化

### 1.1 使用索引避免临时表

```sql
-- 索引 (dept_id, name)
-- GROUP BY 可以利用索引排序
SELECT dept_id, COUNT(*) FROM employees GROUP BY dept_id;
-- Extra: Using index

-- 无索引时需要临时表
-- Extra: Using temporary; Using filesort
```

### 1.2 松散索引扫描（Loose Index Scan）

```sql
-- 适用于：GROUP BY 列有索引，且 MIN/MAX 聚合
-- 索引 (dept_id, salary)
SELECT dept_id, MIN(salary) FROM employees GROUP BY dept_id;
-- Extra: Using index for group-by

-- 松散索引扫描跳过索引中不需要的条目
-- 只读取每个 dept_id 的第一条（MIN）或最后一条（MAX）
```

### 1.3 紧凑索引扫描

```sql
-- 索引 (dept_id, name)
-- WHERE 条件和 GROUP BY 一起使用索引
SELECT dept_id, COUNT(*) FROM employees
WHERE dept_id > 5
GROUP BY dept_id;
-- 扫描索引的 dept_id > 5 部分
```

## 2. ORDER BY 优化

### 2.1 使用索引排序

```sql
-- 索引 (dept_id, salary)
-- ORDER BY 与索引顺序一致
SELECT * FROM employees WHERE dept_id = 5 ORDER BY salary;
-- Extra: Using index condition（无需 filesort）

-- ORDER BY 与索引顺序不一致
SELECT * FROM employees ORDER BY salary;
-- Extra: Using filesort
```

### 2.2 filesort 算法

| 算法     | 说明                                   |
| -------- | -------------------------------------- |
| 双路排序 | 读取行指针和排序列，排序后回表获取数据 |
| 单路排序 | 读取所有需要的列到内存，排序后直接输出 |

```sql
-- 控制 filesort 缓冲区
SET max_length_for_sort_data = 4096;  -- 超过此值使用双路排序
SET sort_buffer_size = 262144;        -- 排序缓冲区大小
```

## 3. GROUP BY + ORDER BY 组合优化

```sql
-- 索引 (dept_id, created_at)
-- GROUP BY + ORDER BY 使用同一索引
SELECT dept_id, COUNT(*) AS cnt
FROM orders
GROUP BY dept_id
ORDER BY dept_id;
-- Extra: Using index

-- GROUP BY 和 ORDER BY 列不同
SELECT dept_id, COUNT(*) AS cnt
FROM orders
GROUP BY dept_id
ORDER BY cnt DESC;
-- Extra: Using temporary; Using filesort
-- 需要临时表 + 额外排序
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
