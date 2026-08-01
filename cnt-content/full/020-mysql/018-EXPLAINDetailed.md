---
order: 61
title: EXPLAIN输出详解
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL EXPLAIN输出详解：type、key、rows、filtered、Extra字段的含义与性能诊断'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/SQL函数与高级查询
  - mysql/索引失效场景
  - mysql/慢查询日志
  - mysql/优化器追踪
prerequisites:
  - mysql/语法速查
---

## 1. EXPLAIN 输出列

| 列            | 含义                 |
| ------------- | -------------------- |
| id            | SELECT 标识符        |
| select_type   | 查询类型             |
| table         | 访问的表             |
| partitions    | 匹配的分区           |
| **type**      | 访问类型（最重要）   |
| possible_keys | 可能使用的索引       |
| **key**       | 实际使用的索引       |
| key_len       | 使用的索引长度       |
| ref           | 与索引比较的列或常量 |
| **rows**      | 估算扫描行数         |
| **filtered**  | 过滤比例             |
| **Extra**     | 额外信息             |

## 2. type 详解

从最优到最差：

| type            | 说明                          | 示例                        |
| --------------- | ----------------------------- | --------------------------- |
| system          | 表中只有一行                  | `WHERE id = 1`（单行表）    |
| const           | 主键/唯一索引等值查询         | `WHERE id = 1`              |
| eq_ref          | JOIN 中主键/唯一索引等值      | `JOIN ON a.id = b.id`       |
| ref             | 非唯一索引等值查询            | `WHERE dept_id = 5`         |
| fulltext        | 全文索引                      | `MATCH ... AGAINST`         |
| ref_or_null     | 类似 ref，额外搜索 NULL       | `WHERE dept_id = 5 OR NULL` |
| index_merge     | 索引合并                      | `WHERE a=1 OR b=2`          |
| unique_subquery | IN 子查询优化为唯一索引查找   | `WHERE id IN (SELECT ...)`  |
| index_subquery  | IN 子查询优化为非唯一索引查找 | `WHERE dept_id IN (...)`    |
| range           | 范围扫描                      | `WHERE id > 100`            |
| index           | 全索引扫描                    | `ORDER BY id`（无WHERE）    |
| ALL             | 全表扫描                      | 无索引条件                  |

## 3. key 与 key_len

```sql
-- key：实际使用的索引名
-- key = NULL：未使用索引

-- key_len：使用的索引字节数
-- 可判断联合索引使用了几个列

-- 索引 (dept_id INT, name VARCHAR(50))
-- dept_id: 4字节 + 1字节(NULL标志) = 5
-- name: 50*3(utf8mb4) + 2(变长) + 1(NULL) = 153

-- key_len = 5：只用了 dept_id
-- key_len = 158：用了 dept_id + name
```

## 4. rows 与 filtered

```sql
-- rows：估算扫描行数
-- filtered：过滤比例（0.00-100.00）
-- 实际返回行 ≈ rows × filtered / 100

-- 示例：rows=1000, filtered=10.00
-- 实际返回约 100 行
```

## 5. Extra 详解

| Extra 值                          | 含义                                |
| --------------------------------- | ----------------------------------- |
| Using index                       | 覆盖索引，无需回表                  |
| Using where                       | Server 层过滤                       |
| Using index condition             | 索引下推（ICP）                     |
| Using temporary                   | 使用临时表                          |
| Using filesort                    | 额外排序（非索引排序）              |
| Using join buffer                 | 使用连接缓冲区（Block Nested Loop） |
| Using MRR                         | 多范围读优化                        |
| Using index for group-by          | 索引用于 GROUP BY                   |
| Using where with pushed condition | 索引条件下推                        |
| Impossible WHERE                  | WHERE 不可能为真                    |
| Select tables optimized away      | 优化为常量（如 MIN/MAX 使用索引）   |

## 6. EXPLAIN ANALYZE

```sql
-- MySQL 8.0.18+：实际执行并返回真实数据
EXPLAIN ANALYZE
SELECT * FROM employees WHERE dept_id = 5;

-- 输出包含：
-- actual time：实际执行时间
-- actual rows：实际返回行数
-- loops：执行次数
-- 估算值 vs 实际值对比
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
