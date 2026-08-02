---
order: 840
title: mysqladmin 管理命令 语法速查手册
module: mysql

category: '020-mysql'
difficulty: beginner
description: mysqladmin 管理命令 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 服务状态检查

**基本写法：检查服务器存活**
`mysqladmin -u <用户名> -p ping`

```bash
# 检测 MySQL 服务是否运行（返回 mysqld is alive）
mysqladmin -u root -p ping
```

**基本写法：查看服务器状态**
`mysqladmin -u <用户名> -p status`

```bash
# 查看连接数、运行时间等概览
mysqladmin -u root -p status
# 输出: Uptime: 3600  Threads: 5  Questions: 1234  Slow queries: 0  Opens: 100
```

**基本写法：查看扩展状态**
`mysqladmin -u <用户名> -p extended-status`

```bash
# 查看所有状态变量
mysqladmin -u root -p extended-status
# 查看特定状态变量
mysqladmin -u root -p extended-status | grep -i thread
```

**基本写法：查看版本信息**
`mysqladmin -u <用户名> -p version`

```bash
# 查看 MySQL 版本与协议信息
mysqladmin -u root -p version
```

---

## 进程与连接管理

**基本写法：查看进程列表**
`mysqladmin -u <用户名> -p processlist`

```bash
# 查看当前所有连接与执行的 SQL
mysqladmin -u root -p processlist
```

**基本写法：杀掉指定连接**
`mysqladmin -u <用户名> -p kill <连接ID> [<连接ID2> ...]`

```bash
# 终止指定会话（ID 来自 processlist）
mysqladmin -u root -p kill 1234 5678
```

**基本写法：杀掉某用户所有连接**
`mysqladmin -u <用户名> -p kill $(mysqladmin -u root -p processlist | grep <用户名> | awk '{print $2}')`

```bash
# 终止某用户的所有连接
mysqladmin -u root -p kill $(mysqladmin -u root -ppass processlist | grep appuser | awk '{print $2}')
```

---

## 服务控制

**基本写法：关闭服务器**
`mysqladmin -u <用户名> -p shutdown`

```bash
# 安全关闭 MySQL 服务
mysqladmin -u root -p shutdown
```

**基本写法：刷新权限**
`mysqladmin -u <用户名> -p flush-privileges`

```bash
# 重新加载授权表（8.4 需 FLUSH_PRIVILEGES 权限）
mysqladmin -u root -p flush-privileges
```

**基本写法：刷新日志**
`mysqladmin -u <用户名> -p flush-logs`

```bash
# 关闭并重新打开日志文件（轮转二进制日志）
mysqladmin -u root -p flush-logs
```

**基本写法：刷新主机缓存**
`mysqladmin -u <用户名> -p flush-hosts`

```bash
# 清空主机缓存（8.4 FLUSH HOSTS 已移除，等价于 TRUNCATE host_cache）
mysqladmin -u root -p flush-hosts
```

**基本写法：刷新表**
`mysqladmin -u <用户名> -p flush-tables`

```bash
# 关闭所有打开的表并刷新缓存
mysqladmin -u root -p flush-tables
```

**基本写法：刷新状态变量**
`mysqladmin -u <用户名> -p flush-status`

```bash
# 重置大多数状态变量为 0
mysqladmin -u root -p flush-status
```

---

## 密码与变量

**基本写法：修改用户密码**
`mysqladmin -u <用户名> -p password "<新密码>"`

```bash
# 修改当前用户密码
mysqladmin -u root -p password "NewStrongPass123!"
```

**基本写法：查看/设置变量**
`mysqladmin -u <用户名> -p variables`

```bash
# 查看所有系统变量
mysqladmin -u root -p variables
# 过滤查看字符集相关变量
mysqladmin -u root -p variables | grep -i character
```

**基本写法：动态设置变量**
`mysqladmin -u <用户名> -p variable-set "<变量名>=<值>"`

```bash
# 在线调整最大连接数
mysqladmin -u root -p variable-set max_connections=500
```

---

## 其他常用

**基本写法：重新加载授权表并刷新**
`mysqladmin -u <用户名> -p reload`

```bash
# 重新加载授权表（等同 flush-privileges）
mysqladmin -u root -p reload
```

**基本写法：刷新线程缓存**
`mysqladmin -u <用户名> -p flush-threads`

```bash
# 清空线程缓存
mysqladmin -u root -p flush-threads
```

**基本写法：刷新查询缓存（8.0 前可用）**
`mysqladmin -u <用户名> -p refresh`

```bash
# 刷新表并刷新日志
mysqladmin -u root -p refresh
```

---

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
