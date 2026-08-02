---
order: 80
title: 数据加密存储
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL数据加密存储：pgcrypto扩展、加密函数、列级加密与密钥管理
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/基于角色的权限管理
  - postgresql/行级安全策略
  - postgresql/审计日志
  - postgresql/序列与自增列
prerequisites:
  - postgresql/概述与安装配置
---

## 1. pgcrypto 扩展

```sql
CREATE EXTENSION pgcrypto;
```

## 2. 哈希函数

```sql
-- MD5（不推荐用于安全场景）
SELECT md5('password');

-- SHA-256
SELECT encode(digest('password', 'sha256'), 'hex');

-- bcrypt（推荐用于密码存储）
SELECT crypt('password', gen_salt('bf'));
-- 验证
SELECT crypt('password', stored_hash) = stored_hash;
```

## 3. 加密函数

```sql
-- 对称加密（AES-256）
SELECT encrypt('secret data', 'my_key', 'aes');
SELECT decrypt(encrypt('secret data', 'my_key', 'aes'), 'my_key', 'aes');

-- pgp对称加密
SELECT pgp_sym_encrypt('secret data', 'my_password');
SELECT pgp_sym_decrypt(pgp_sym_encrypt('secret data', 'my_password'), 'my_password');

-- pgp公钥加密
SELECT pgp_pub_encrypt('secret data', dearmor(public_key));
SELECT pgp_pub_decrypt(encrypted_data, dearmor(private_key), 'passphrase');
```

## 4. 列级加密

```sql
-- 加密列
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    ssn BYTEA  -- 加密存储
);

-- 插入加密数据
INSERT INTO users (name, ssn) VALUES (
    'Alice',
    pgp_sym_encrypt('123-45-6789', 'encryption_key')
);

-- 查询解密
SELECT name, pgp_sym_decrypt(ssn, 'encryption_key') AS ssn
FROM users;
```

## 延伸阅读
PostgreSQL 窗口函数，见 021-postgresql 模块文档。
PostgreSQL 递归查询，见 021-postgresql 模块相关文档。
SQL 基础，见 019-sql 模块。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 MVCC 与 vacuum 机制

行头存储 xmin（创建事务）与 xmax（删除事务）；可见性由快照比较决定。
更新 = 插入新版本 + 旧版本标记；旧版本对旧事务可见，vacuum 回收不再可见的死元组。
事务 ID 回卷：约 21 亿事务后需要冻结；autovacuum 与 vacuum freeze 防止。
监控：SELECT n_dead_tup, last_autovacuum FROM pg_stat_user_tables。

### 13.2 逻辑复制与高可用

发布（publication）定义表集，订阅（subscription）在目标端应用变更；支持过滤与列子集。
流复制：主库 WAL 发送到备库，同步/异步模式；级联复制扩展拓扑。
Patroni 使用分布式共识（etcd）选主，故障自动切换，配合虚拟 IP。
切换演练与数据校验（pg_checksums）是可用性工程必备。
