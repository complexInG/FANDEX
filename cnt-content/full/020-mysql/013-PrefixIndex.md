---
order: 57
title: 前缀索引
module: mysql
category: MySQL
difficulty: intermediate
description: MySQL前缀索引：长字符串列的索引优化、选择性计算、适用场景与限制
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/索引下推
  - mysql/全文索引
  - mysql/索引提示与强制索引
  - mysql/索引统计信息与直方图
prerequisites:
  - mysql/语法速查
---

## 1. 前缀索引概述

前缀索引对字符串列的前 N 个字符建立索引，减少索引存储空间和维护开销。

```sql
-- 创建前缀索引
CREATE INDEX idx_email_prefix ON users(email(10));
CREATE INDEX idx_url_prefix ON web_pages(url(50));
```

## 2. 选择性计算

### 2.1 计算完整列选择性

```sql
-- 完整列的选择性
SELECT COUNT(DISTINCT email) / COUNT(*) AS selectivity FROM users;
-- 如 0.95
```

### 2.2 计算前缀选择性

```sql
-- 不同前缀长度的选择性
SELECT
    COUNT(DISTINCT LEFT(email, 5)) / COUNT(*) AS s5,
    COUNT(DISTINCT LEFT(email, 10)) / COUNT(*) AS s10,
    COUNT(DISTINCT LEFT(email, 15)) / COUNT(*) AS s15,
    COUNT(DISTINCT LEFT(email, 20)) / COUNT(*) AS s20
FROM users;

-- 选择使选择性接近完整列选择性的最小前缀长度
-- 如 s10 = 0.94 接近 0.95，选择前缀长度 10
```

## 3. 限制

```sql
-- 前缀索引不支持覆盖索引
-- 无法在 ORDER BY / GROUP BY 中使用
-- 无法用于等值比较的覆盖扫描

-- 示例：前缀索引无法覆盖
SELECT email FROM users WHERE email LIKE 'test%';
-- 即使 email(10) 索引包含前10个字符，也需要回表获取完整 email
```

## 4. 适用场景

```sql
-- 1. 长字符串列（URL、邮箱、路径）
CREATE INDEX idx_url_prefix ON pages(url(50));

-- 2. 空间敏感场景
-- 前缀索引占用空间远小于完整列索引

-- 3. 不需要覆盖索引的查询
SELECT id, name FROM users WHERE email LIKE 'test@%';
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
