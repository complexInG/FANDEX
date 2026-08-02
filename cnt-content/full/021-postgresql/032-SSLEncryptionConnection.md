---
order: 320
title: SSL-TLS加密连接
module: 'postgresql'
category: 数据库
difficulty: intermediate
description: PostgreSQL SSL/TLS加密连接：证书配置、强制加密、客户端证书验证
author: fanquanpp
updated: '2026-08-01'
related:
  - 'postgresql/030-IncrementalBackup'
  - 'postgresql/031-SubscribePublish'
  - 'postgresql/033-RoleBasedPermissionManagement'
  - 'postgresql/034-RowLevelSecurity'
prerequisites:
  - 'postgresql/001-OverviewInstallConfig'
---


## 1. 配置SSL

```ini
# postgresql.conf
ssl = on
ssl_ca_file = '/etc/postgresql/root.crt'
ssl_cert_file = '/etc/postgresql/server.crt'
ssl_key_file = '/etc/postgresql/server.key'
```

## 2. 强制SSL

```ini
# pg_hba.conf
hostssl all all 0.0.0.0/0 md5       -- 只允许SSL连接
hostnossl all all 0.0.0.0/0 reject   -- 拒绝非SSL连接
```

## 3. 客户端证书验证

```ini
# pg_hba.conf
hostssl all all 0.0.0.0/0 cert       -- 要求客户端证书
```

```bash
# 客户端连接
psql "host=server dbname=mydb user=alice sslmode=verify-full sslcert=client.crt sslkey=client.key sslrootcert=root.crt"
```

## 4. sslmode 选项

| 模式        | 验证级别                |
| ----------- | ----------------------- |
| disable     | 不使用SSL               |
| allow       | 优先非SSL，失败再SSL    |
| prefer      | 优先SSL，失败再非SSL    |
| require     | 必须SSL，不验证证书     |
| verify-ca   | 必须SSL，验证CA         |
| verify-full | 必须SSL，验证CA和主机名 |

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
