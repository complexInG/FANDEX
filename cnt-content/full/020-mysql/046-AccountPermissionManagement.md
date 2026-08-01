---
order: 87
title: 账户与权限管理
module: mysql
category: MySQL
difficulty: intermediate
description: MySQL账户与权限管理：用户创建、权限授予、角色、密码策略与审计
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/分区表
  - mysql/分库分表中间件
  - 'mysql/SSL-TLS加密'
  - mysql/防火墙插件
prerequisites:
  - mysql/语法速查
---
## 1. 用户管理

```sql
-- 创建用户
CREATE USER 'app_user'@'%' IDENTIFIED BY 'StrongP@ss123';
CREATE USER 'readonly'@'10.0.%' IDENTIFIED BY 'password';

-- 修改密码
ALTER USER 'app_user'@'%' IDENTIFIED BY 'NewP@ss456';

-- 删除用户
DROP USER 'app_user'@'%';

-- 查看用户
SELECT user, host FROM mysql.user;
```

## 2. 权限管理

```sql
-- 授予权限
GRANT SELECT, INSERT ON mydb.* TO 'app_user'@'%';
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';

-- 撤销权限
REVOKE INSERT ON mydb.* FROM 'app_user'@'%';

-- 查看权限
SHOW GRANTS FOR 'app_user'@'%';
```

## 3. 角色（MySQL 8.0+）

```sql
-- 创建角色
CREATE ROLE 'app_read', 'app_write', 'app_admin';

-- 授予角色权限
GRANT SELECT ON mydb.* TO 'app_read';
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
GRANT ALL PRIVILEGES ON mydb.* TO 'app_admin';

-- 将角色分配给用户
GRANT 'app_read' TO 'reporting_user'@'%';
GRANT 'app_write' TO 'application_user'@'%';

-- 激活角色
SET DEFAULT ROLE ALL TO 'reporting_user'@'%';
```

## 4. 密码策略

```sql
-- MySQL 8.0 密码验证插件
INSTALL COMPONENT 'file://component_validate_password';
SET GLOBAL validate_password.policy = MEDIUM;
SET GLOBAL validate_password.length = 12;
SET GLOBAL validate_password.mixed_case_count = 1;
SET GLOBAL validate_password.number_count = 1;
SET GLOBAL validate_password.special_char_count = 1;

-- 密码过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE INTERVAL 90 DAY;
ALTER USER 'app_user'@'%' PASSWORD EXPIRE NEVER;
```

## 5. 连接安全

```sql
-- 限制最大连接数
ALTER USER 'app_user'@'%' WITH MAX_CONNECTIONS_PER_HOUR 100;

-- 限制查询数
ALTER USER 'app_user'@'%' WITH MAX_QUERIES_PER_HOUR 1000;

-- 锁定账户
ALTER USER 'app_user'@'%' ACCOUNT LOCK;
ALTER USER 'app_user'@'%' ACCOUNT UNLOCK;
```
## 用户管理

**单行写法：创建用户允许任意主机连接**
`CREATE USER '<用户名>'@'%' IDENTIFIED BY '<密码>'`
```sql
-- 创建允许任意主机连接的用户
CREATE USER 'app_user'@'%' IDENTIFIED BY 'StrongP@ss123';
```

**单行写法：创建用户限制来源 IP 段**
`CREATE USER '<用户名>'@'<IP 段>' IDENTIFIED BY '<密码>'`
```sql
-- 创建限制来源 IP 段的用户
CREATE USER 'readonly'@'10.0.%' IDENTIFIED BY 'password';
```

**单行写法：修改用户密码**
`ALTER USER '<用户名>'@'<主机>' IDENTIFIED BY '<新密码>'`
```sql
-- 修改用户密码
ALTER USER 'app_user'@'%' IDENTIFIED BY 'NewP@ss456';
```

**单行写法：删除用户**
`DROP USER '<用户名>'@'<主机>'`
```sql
-- 删除指定用户
DROP USER 'app_user'@'%';
```

**单行写法：查看所有用户**
`SELECT user, host FROM mysql.user`
```sql
-- 查看所有用户列表
SELECT user, host FROM mysql.user;
```

---

## 权限管理

**单行写法：授予查询和插入权限**
`GRANT <权限列表> ON <库>.<表> TO '<用户名>'@'<主机>'`
```sql
-- 授予查询和插入权限
GRANT SELECT, INSERT ON mydb.* TO 'app_user'@'%';
```

**单行写法：授予所有权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<用户名>'@'<主机>'`
```sql
-- 授予所有权限
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';
```

**单行写法：撤销权限**
`REVOKE <权限列表> ON <库>.<表> FROM '<用户名>'@'<主机>'`
```sql
-- 撤销插入权限
REVOKE INSERT ON mydb.* FROM 'app_user'@'%';
```

**单行写法：查看用户权限**
`SHOW GRANTS FOR '<用户名>'@'<主机>'`
```sql
-- 查看用户权限
SHOW GRANTS FOR 'app_user'@'%';
```

**单行写法：刷新权限**
`FLUSH PRIVILEGES`
```sql
-- 刷新权限表
FLUSH PRIVILEGES;
```

---

## 角色管理

**单行写法：创建多个角色**
`CREATE ROLE '<角色名>'[, '<角色名>'...]`
```sql
-- 创建多个角色
CREATE ROLE 'app_read', 'app_write', 'app_admin';
```

**单行写法：授予只读角色权限**
`GRANT SELECT ON <库>.<表> TO '<角色名>'`
```sql
-- 授予只读角色权限
GRANT SELECT ON mydb.* TO 'app_read';
```

**单行写法：授予读写角色权限**
`GRANT SELECT, INSERT, UPDATE, DELETE ON <库>.<表> TO '<角色名>'`
```sql
-- 授予读写角色权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
```

**单行写法：授予管理员角色权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<角色名>'`
```sql
-- 授予管理员角色权限
GRANT ALL PRIVILEGES ON mydb.* TO 'app_admin';
```

**单行写法：将角色分配给用户**
`GRANT '<角色名>' TO '<用户名>'@'<主机>'`
```sql
-- 分配角色给用户
GRANT 'app_read' TO 'reporting_user'@'%';
```

**单行写法：设置用户默认角色**
`SET DEFAULT ROLE ALL TO '<用户名>'@'<主机>'`
```sql
-- 设置用户默认角色
SET DEFAULT ROLE ALL TO 'reporting_user'@'%';
```

**单行写法：撤销用户角色**
`REVOKE '<角色名>' FROM '<用户名>'@'<主机>'`
```sql
-- 撤销用户角色
REVOKE 'app_read' FROM 'reporting_user'@'%';
```

**单行写法：删除角色**
`DROP ROLE '<角色名>'[, '<角色名>'...]`
```sql
-- 删除多个角色
DROP ROLE 'app_read', 'app_write', 'app_admin';
```

---

## 密码策略

**单行写法：安装密码验证组件**
`INSTALL COMPONENT 'file://component_validate_password'`
```sql
-- 安装密码验证组件
INSTALL COMPONENT 'file://component_validate_password';
```

**单行写法：设置密码策略级别**
`SET GLOBAL validate_password.policy = <级别>`
```sql
-- 设置密码策略级别为 MEDIUM
SET GLOBAL validate_password.policy = MEDIUM;
```

**单行写法：设置密码最小长度**
`SET GLOBAL validate_password.length = <长度>`
```sql
-- 设置密码最小长度为 12
SET GLOBAL validate_password.length = 12;
```

**单行写法：设置大小写字母数量**
`SET GLOBAL validate_password.mixed_case_count = <数量>`
```sql
-- 设置密码大小写字母数量为 1
SET GLOBAL validate_password.mixed_case_count = 1;
```

**单行写法：设置数字数量**
`SET GLOBAL validate_password.number_count = <数量>`
```sql
-- 设置密码数字数量为 1
SET GLOBAL validate_password.number_count = 1;
```

**单行写法：设置特殊字符数量**
`SET GLOBAL validate_password.special_char_count = <数量>`
```sql
-- 设置密码特殊字符数量为 1
SET GLOBAL validate_password.special_char_count = 1;
```

**单行写法：密码定期过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE INTERVAL <天数> DAY`
```sql
-- 设置密码 90 天过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE INTERVAL 90 DAY;
```

**单行写法：密码永不过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE NEVER`
```sql
-- 设置密码永不过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE NEVER;
```

---

## 连接限制

**单行写法：限制每小时最大连接数**
`ALTER USER '<用户名>'@'<主机>' WITH MAX_CONNECTIONS_PER_HOUR <数量>`
```sql
-- 限制每小时最大连接数为 100
ALTER USER 'app_user'@'%' WITH MAX_CONNECTIONS_PER_HOUR 100;
```

**单行写法：限制每小时最大查询数**
`ALTER USER '<用户名>'@'<主机>' WITH MAX_QUERIES_PER_HOUR <数量>`
```sql
-- 限制每小时最大查询数为 1000
ALTER USER 'app_user'@'%' WITH MAX_QUERIES_PER_HOUR 1000;
```

**单行写法：锁定账户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT LOCK`
```sql
-- 锁定账户
ALTER USER 'app_user'@'%' ACCOUNT LOCK;
```

**单行写法：解锁账户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT UNLOCK`
```sql
-- 解锁账户
ALTER USER 'app_user'@'%' ACCOUNT UNLOCK;
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
