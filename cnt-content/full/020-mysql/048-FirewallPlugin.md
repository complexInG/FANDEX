---
order: 89
title: 防火墙插件
module: mysql
category: MySQL
difficulty: intermediate
description: MySQL企业防火墙插件：SQL白名单、学习模式、拦截模式与SQL注入防护
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/账户与权限管理
  - 'mysql/SSL-TLS加密'
  - mysql/InnoDB体系架构
  - mysql/数据加密
prerequisites:
  - mysql/语法速查
---

## 1. MySQL 企业防火墙

MySQL Enterprise Firewall 记录正常SQL模式，拦截异常SQL，防止SQL注入。

## 2. 安装与配置

```sql
-- 安装防火墙插件
INSTALL PLUGIN mysql_firewall SONAME 'mysql_firewall.so';
INSTALL PLUGIN mysql_firewall_users SONAME 'mysql_firewall.so';
INSTALL PLUGIN mysql_firewall_whitelist SONAME 'mysql_firewall.so';

-- 创建防火墙用户
CREATE USER 'fw_user'@'%';
CALL mysql.sp_set_firewall_mode('fw_user@%', 'RECORDING');
```

## 3. 三种模式

| 模式       | 说明                       |
| ---------- | -------------------------- |
| RECORDING  | 记录SQL模式，建立白名单    |
| PROTECTING | 允许白名单SQL，拦截异常SQL |
| DETECTING  | 允许所有SQL，记录异常SQL   |

```sql
-- 学习模式：记录正常SQL
CALL mysql.sp_set_firewall_mode('fw_user@%', 'RECORDING');
-- 执行正常业务SQL...

-- 切换到保护模式
CALL mysql.sp_set_firewall_mode('fw_user@%', 'PROTECTING');

-- 检测模式（不拦截，只记录）
CALL mysql.sp_set_firewall_mode('fw_user@%', 'DETECTING');
```

## 4. 查看防火墙状态

```sql
-- 查看用户防火墙模式
SELECT * FROM mysql.firewall_users;

-- 查看白名单规则
SELECT * FROM mysql.firewall_whitelist;

-- 查看拦截统计
SELECT * FROM performance_schema.firewall_status;
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
