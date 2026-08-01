---
order: 62
title: 慢查询日志
module: mysql
category: MySQL
difficulty: intermediate
description: 'MySQL慢查询日志：配置、分析工具mysqldumpslow、pt-query-digest与慢查询优化流程'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/索引失效场景
  - mysql/EXPLAIN输出详解
  - mysql/优化器追踪
  - mysql/子查询优化
prerequisites:
  - mysql/语法速查
---

## 1. 慢查询日志配置

```sql
-- 查看慢查询日志状态
SHOW VARIABLES LIKE 'slow_query%';
SHOW VARIABLES LIKE 'long_query_time';

-- 开启慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- 超过1秒记录
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';

-- 记录未使用索引的查询
SET GLOBAL log_queries_not_using_indexes = ON;

-- 每分钟限制记录条数（防止日志膨胀）
SET GLOBAL log_throttle_queries_not_using_indexes = 60;
```

## 2. 日志格式

```
# Time: 2026-06-14T10:30:00.123456+08:00
# User@Host: app_user[app_user] @ web-server [192.168.1.100]
# Query_time: 5.123456  Lock_time: 0.000123  Rows_sent: 100  Rows_examined: 1000000
SET timestamp=1718334600;
SELECT * FROM orders WHERE YEAR(created_at) = 2026;
```

## 3. 分析工具

### 3.1 mysqldumpslow

```bash
# 按查询时间排序，显示前10条
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log

# 按查询次数排序
mysqldumpslow -s c -t 10 /var/log/mysql/slow.log

# 选项：
# -s t: 按查询时间排序
# -s c: 按查询次数排序
# -s l: 按锁定时间排序
# -s r: 按返回记录数排序
# -t N: 显示前N条
```

### 3.2 pt-query-digest

```bash
# 分析慢查询日志
pt-query-digest /var/log/mysql/slow.log

# 分析特定时间段的查询
pt-query-digest --since '2026-06-14 00:00:00' --until '2026-06-14 23:59:59' /var/log/mysql/slow.log

# 输出报告包含：
# - 总体统计
# - 查询指纹和排名
# - 每个查询的详细统计
# - EXPLAIN 示例
```

## 4. 优化流程

```
1. 识别慢查询 → 慢查询日志
2. 分析执行计划 → EXPLAIN
3. 定位瓶颈 → 全表扫描、filesort、临时表
4. 优化方案 → 添加索引、改写查询、调整参数
5. 验证效果 → EXPLAIN ANALYZE
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
