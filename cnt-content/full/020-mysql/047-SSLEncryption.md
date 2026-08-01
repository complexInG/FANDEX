---
order: 88
title: 'SSL-TLS加密'
module: mysql
category: MySQL
difficulty: intermediate
description: 'MySQL SSL/TLS加密连接：证书配置、强制加密、客户端验证与安全最佳实践'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/分库分表中间件
  - mysql/账户与权限管理
  - mysql/防火墙插件
  - mysql/InnoDB体系架构
prerequisites:
  - mysql/语法速查
---

## 1. SSL/TLS 概述

MySQL 支持SSL/TLS加密客户端与服务器之间的通信，防止数据在传输中被窃听。

## 2. 配置SSL

### 2.1 自动配置

```sql
-- MySQL 8.0 默认自动生成SSL证书
-- 查看SSL状态
SHOW VARIABLES LIKE '%ssl%';
-- have_ssl = YES
```

### 2.2 手动配置

```ini
[mysqld]
ssl-ca = /etc/mysql/ssl/ca.pem
ssl-cert = /etc/mysql/ssl/server-cert.pem
ssl-key = /etc/mysql/ssl/server-key.pem
require_secure_transport = ON  -- 强制加密连接
```

## 3. 强制加密连接

```sql
-- 创建必须使用SSL的用户
CREATE USER 'secure_user'@'%' IDENTIFIED BY 'password'
REQUIRE SSL;

-- 创建需要客户端证书的用户
CREATE USER 'cert_user'@'%' IDENTIFIED BY 'password'
REQUIRE X509;

-- 修改现有用户
ALTER USER 'app_user'@'%' REQUIRE SSL;
```

## 4. 客户端连接

```bash
# 使用SSL连接
mysql -u secure_user -p --ssl-mode=REQUIRED

# 使用客户端证书
mysql -u cert_user -p \
    --ssl-ca=/etc/mysql/ssl/ca.pem \
    --ssl-cert=/etc/mysql/ssl/client-cert.pem \
    --ssl-key=/etc/mysql/ssl/client-key.pem

# 验证SSL连接
mysql> \s
-- SSL: Cipher in use is TLS_AES_256_GCM_SHA384
```

## 5. 验证SSL连接

```sql
-- 查看当前连接是否加密
SELECT * FROM performance_schema.session_status
WHERE VARIABLE_NAME = 'Ssl_cipher';

-- 查看所有连接的SSL状态
SELECT sbt.thread_id, sbt.ssl_cipher, sbt.user, sbt.host
FROM performance_schema.threads t
JOIN performance_schema.session_connect_attrs sca
    ON t.processlist_id = sca.processlist_id
WHERE sca.attr_name = 'ssl_cipher';
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
