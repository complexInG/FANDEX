---
order: 78
title: 物理备份
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL物理备份：MySQL Enterprise Backup、Percona XtraBackup的原理、热备份与恢复流程'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/日志系统
  - mysql/逻辑备份
  - mysql/基于时间点恢复
  - mysql/主从复制
prerequisites:
  - mysql/语法速查
---

## 1. 物理备份概述

物理备份直接复制数据库文件（数据文件、日志文件），速度比逻辑备份快得多。

| 特性   | 物理备份       | 逻辑备份      |
| ------ | -------------- | ------------- |
| 速度   | 快             | 慢            |
| 粒度   | 整库/整表      | 可选表/行     |
| 可读性 | 二进制，不可读 | SQL文本，可读 |
| 跨平台 | 不可以         | 可以          |
| 工具   | XtraBackup/MEB | mysqldump     |

## 2. Percona XtraBackup

### 2.1 全量备份

```bash
# 全量热备份
xtrabackup --backup --target-dir=/backup/full -u root -p

# 准备备份（使备份一致）
xtrabackup --prepare --target-dir=/backup/full

# 恢复
xtrabackup --copy-back --target-dir=/backup/full
chown -R mysql:mysql /var/lib/mysql
systemctl start mysql
```

### 2.2 增量备份

```bash
# 增量备份基于全量
xtrabackup --backup --target-dir=/backup/inc1 \
    --incremental-basedir=/backup/full -u root -p

# 准备增量备份
xtrabackup --prepare --apply-log-only --target-dir=/backup/full
xtrabackup --prepare --target-dir=/backup/full --incremental-dir=/backup/inc1

# 恢复（同全量恢复）
xtrabackup --copy-back --target-dir=/backup/full
```

### 2.3 压缩备份

```bash
xtrabackup --backup --compress --target-dir=/backup/compressed -u root -p

# 解压
xtrabackup --decompress --target-dir=/backup/compressed
```

## 3. MySQL Enterprise Backup

```bash
# 全量备份
mysqlbackup --user=root --password --backup-dir=/backup/full backup

# 增量备份
mysqlbackup --user=root --password --backup-dir=/backup/inc1 \
    --incremental --incremental-base=dir:/backup/full backup

# 恢复
mysqlbackup --datadir=/var/lib/mysql --backup-dir=/backup/full copy-back
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
