---
order: 79
title: 基于时间点恢复
module: mysql
category: MySQL
difficulty: advanced
description: MySQL基于时间点恢复PITR：全量恢复+binlog重放、时间点定位与误操作恢复
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/逻辑备份
  - mysql/物理备份
  - mysql/主从复制
  - mysql/进阶查询与多表操作
prerequisites:
  - mysql/语法速查
---

## 1. PITR 概述

基于时间点恢复（Point-In-Time Recovery，PITR）将数据库恢复到任意时间点，通过全量备份 + binlog 重放实现。

## 2. 恢复流程

```
1. 恢复全量备份
2. 找到误操作的时间点
3. 重放 binlog 到误操作之前
4. 跳过误操作
5. 继续重放后续 binlog
```

## 3. 操作步骤

### 3.1 恢复全量备份

```bash
# 停止 MySQL
systemctl stop mysql

# 恢复全量备份
xtrabackup --copy-back --target-dir=/backup/full
chown -R mysql:mysql /var/lib/mysql

# 启动 MySQL
systemctl start mysql
```

### 3.2 定位误操作时间

```bash
# 查看 binlog 事件
mysqlbinlog --base64-output=DECODE-ROWS -v mysql-bin.000123 | grep -A5 "DROP TABLE"

# 查看事件时间
mysqlbinlog --start-datetime="2026-06-14 10:00:00" \
            --stop-datetime="2026-06-14 12:00:00" \
            mysql-bin.000123 | head -100
```

### 3.3 重放 binlog

```bash
# 重放到误操作之前
mysqlbinlog --start-datetime="2026-06-14 10:00:00" \
            --stop-datetime="2026-06-14 10:59:59" \
            mysql-bin.000123 | mysql -u root -p

# 跳过误操作，继续重放
mysqlbinlog --start-datetime="2026-06-14 11:01:00" \
            mysql-bin.000123 | mysql -u root -p
```

## 4. 按位置恢复

```bash
# 查看事件位置
mysqlbinlog mysql-bin.000123 | grep -n "DROP TABLE"

# 按位置恢复
mysqlbinlog --start-position=154 --stop-position=1024 \
            mysql-bin.000123 | mysql -u root -p

# 跳过误操作后继续
mysqlbinlog --start-position=2048 \
            mysql-bin.000123 | mysql -u root -p
```

## 5. 最佳实践

```sql
-- 1. 定期全量备份
-- 2. 确保 binlog 开启且完整
-- 3. sync_binlog = 1 确保不丢失 binlog
-- 4. 保留足够长时间的 binlog
-- 5. 测试恢复流程
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
