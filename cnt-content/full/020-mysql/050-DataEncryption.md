---
order: 90
title: 数据加密
module: mysql
category: MySQL
difficulty: advanced
description: MySQL数据加密：透明数据加密TDE、密钥管理、加密表空间与静态数据保护
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/防火墙插件
  - mysql/InnoDB体系架构
  - mysql/索引与执行计划
  - mysql/MySQL9新特性与并行查询
prerequisites:
  - mysql/语法速查
---

## 1. 透明数据加密（TDE）

### 1.1 概述

InnoDB 透明数据加密（Transparent Data Encryption）在存储层自动加密数据，对应用透明。

### 1.2 配置

```ini
[mysqld]
early-plugin-load = keyring_file.so
keyring_file_data = /var/lib/mysql-keyring/keyring
```

```sql
-- 安装 keyring 插件
INSTALL PLUGIN keyring_file SONAME 'keyring_file.so';

-- 查看插件状态
SELECT PLUGIN_NAME, PLUGIN_STATUS FROM information_schema.PLUGINS
WHERE PLUGIN_NAME LIKE 'keyring%';
```

## 2. 加密表空间

```sql
-- 创建加密表
CREATE TABLE sensitive_data (
    id BIGINT PRIMARY KEY,
    ssn VARCHAR(20),
    credit_card VARCHAR(20)
) ENCRYPTION = 'Y';

-- 加密现有表
ALTER TABLE sensitive_data ENCRYPTION = 'Y';

-- 加密通用表空间
CREATE TABLESPACE encrypted_ts ADD DATAFILE 'encrypted_ts.ibd' ENCRYPTION = 'Y';
```

## 3. 加密 redo log 和 undo log

```sql
-- 加密 redo log
SET GLOBAL innodb_redo_log_encrypt = ON;

-- 加密 undo log
SET GLOBAL innodb_undo_log_encrypt = ON;
```

## 4. 密钥轮换

```sql
-- 轮换主密钥
ALTER INSTANCE ROTATE INNODB MASTER KEY;

-- 建议定期轮换（如每季度）
```

## 5. 密钥管理

```sql
-- keyring_file：文件存储（开发环境）
-- keyring_encrypted_file：加密文件存储
-- keyring_okv：Oracle Key Vault
-- keyring_aws：AWS KMS

-- 生产环境推荐使用外部密钥管理服务
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
