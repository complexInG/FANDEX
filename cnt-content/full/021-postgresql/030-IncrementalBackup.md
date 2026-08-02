---
order: 300
title: 增量备份
module: 'postgresql'
category: 数据库
difficulty: advanced
description: PostgreSQL增量备份：pg_basebackup、pg_receivewal、归档WAL与PITR
author: fanquanpp
updated: '2026-08-01'
related:
  - 'postgresql/028-PhysicalReplicationSlot'
  - 'postgresql/029-LogicalDecodingOutputPlugin'
  - 'postgresql/031-SubscribePublish'
  - 'postgresql/032-SSLEncryptionConnection'
prerequisites:
  - 'postgresql/001-OverviewInstallConfig'
---


## 1. pg_basebackup

```bash
# 全量基础备份
pg_basebackup -h localhost -U replicator -D /backup/full -Fp -Xs -P -R

# 压缩备份
pg_basebackup -h localhost -U replicator -D /backup/full -Ft -z -P

# 选项：
# -Fp: plain格式（目录）
# -Ft: tar格式
# -Xs: 流式传输WAL
# -P: 显示进度
# -R: 创建standby.signal
# -z: gzip压缩
```

## 2. WAL 归档

```ini
# postgresql.conf
wal_level = replica
archive_mode = ON
archive_command = 'cp %p /archive/%f'
```

```sql
-- 查看归档状态
SELECT * FROM pg_stat_archiver;
```

## 3. pg_receivewal

```bash
# 持续接收WAL到本地
pg_receivewal -h localhost -U replicator -D /archive/wal --synchronous

# 压缩接收
pg_receivewal -h localhost -U replicator -D /archive/wal -Z 6
```

## 4. PITR 恢复

```bash
# 1. 恢复基础备份
cp -r /backup/full/* /var/lib/postgresql/data/

# 2. 配置恢复目标
cat >> /var/lib/postgresql/data/postgresql.auto.conf << EOF
restore_command = 'cp /archive/%f %p'
recovery_target_time = '2026-06-14 10:00:00'
recovery_target_action = 'promote'
EOF

# 3. 创建恢复标记
touch /var/lib/postgresql/data/recovery.signal

# 4. 启动PostgreSQL
systemctl start postgresql
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
