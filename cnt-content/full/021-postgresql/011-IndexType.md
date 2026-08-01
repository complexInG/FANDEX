---
order: 55
title: 索引类型
module: postgresql
category: PostgreSQL
difficulty: advanced
description: 'PostgreSQL索引类型：B-tree、Hash、GiST、GIN、SP-GiST、BRIN的原理与适用场景'
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/VACUUM机制
  - postgresql/事务ID回卷预防
  - postgresql/覆盖索引与部分索引
  - postgresql/KNN向量索引
prerequisites:
  - postgresql/概述与安装配置
---
## 1. 索引类型总览

| 类型    | 适用场景           | 特点               |
| ------- | ------------------ | ------------------ |
| B-tree  | 等值、范围、排序   | 默认，最通用       |
| Hash    | 等值查找           | 简单，不支持范围   |
| GiST    | 空间、范围、全文   | 可扩展的通用框架   |
| GIN     | 数组、全文、JSONB  | 倒排索引           |
| SP-GiST | 电话、路由、四叉树 | 非平衡磁盘数据结构 |
| BRIN    | 大表、有序数据     | 块级索引，极小     |

## 2. B-tree 索引

```sql
-- 默认索引类型
CREATE INDEX idx_employees_name ON employees(name);

-- 支持的操作符：=, >, <, >=, <=, BETWEEN, IN, LIKE 'prefix%'
-- 支持排序：ORDER BY
-- 支持唯一约束
```

## 3. Hash 索引

```sql
CREATE INDEX idx_users_email_hash ON users USING HASH (email);

-- 只支持等值查找（=）
-- 不支持范围、排序
-- PostgreSQL 10+ 后 Hash 索引可靠，但 B-tree 通常更好
```

## 4. GiST 索引

```sql
-- 空间索引（PostGIS）
CREATE INDEX idx_locations_geom ON locations USING GIST (geom);

-- 范围类型
CREATE INDEX idx_reservations_period ON reservations USING GIST (period);

-- 全文检索（较慢，GIN 更常用）
CREATE INDEX idx_articles_fts ON articles USING GIST (to_tsvector('english', content));
```

## 5. GIN 索引

```sql
-- 全文检索（推荐）
CREATE INDEX idx_articles_fts ON articles USING GIN (to_tsvector('english', content));

-- JSONB 索引
CREATE INDEX idx_data_jsonb ON api_logs USING GIN (payload);
CREATE INDEX idx_data_jsonb_path ON api_logs USING GIN (payload jsonb_path_ops);

-- 数组索引
CREATE INDEX idx_tags ON posts USING GIN (tags);

-- GIN 特点：写入慢（需更新倒排列表），查询快
-- 可使用 fastupdate 延迟更新
CREATE INDEX idx_tags ON posts USING GIN (tags) WITH (fastupdate = on);
```

## 6. SP-GiST 索引

```sql
-- 适合非平衡数据结构
-- 电话号码前缀
CREATE INDEX idx_phones ON contacts USING SPGST (phone prefix_range_ops);

-- 路由表
CREATE INDEX idx_routes ON routing USING SPGST (prefix);
```

## 7. BRIN 索引

```sql
-- 块范围索引：记录每个数据块范围的摘要
-- 极小（通常几MB），适合大表有序数据

CREATE INDEX idx_logs_created ON logs USING BRIN (created_at)
    WITH (pages_per_range = 32);

-- 适合：时间序列数据、按插入顺序的表
-- 不适合：随机分布的数据
```
## B-Tree 索引

**单行写法：创建单列 B-Tree 索引**
`CREATE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为用户名列创建 B-Tree 索引
CREATE INDEX idx_username ON users(username);
```

**单行写法：创建复合 B-Tree 索引**
`CREATE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 为用户名和状态列创建复合索引
CREATE INDEX idx_name_status ON users(username, status);
```

**单行写法：创建唯一 B-Tree 索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为邮箱列创建唯一索引
CREATE UNIQUE INDEX idx_email ON users(email);
```

---

## Hash 索引

**单行写法：创建 Hash 索引**
`CREATE INDEX <索引名> ON <表名> USING HASH (<列名>)`
```sql
-- 为用户 ID 创建 Hash 索引
CREATE INDEX idx_user_id_hash ON users USING HASH (user_id);
```

---

## GiST 索引

**单行写法：创建 GiST 索引**
`CREATE INDEX <索引名> ON <表名> USING GIST (<列名>)`
```sql
-- 为地理位置列创建 GiST 索引
CREATE INDEX idx_location ON places USING GIST (location);
```

**单行写法：创建 GiST 范围索引**
`CREATE INDEX <索引名> ON <表名> USING GIST (<范围列>)`
```sql
-- 为时间范围列创建 GiST 索引
CREATE INDEX idx_time_range ON schedules USING GIST (time_range);
```

---

## GIN 索引

**单行写法：创建 GIN 索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (<列名>)`
```sql
-- 为 JSONB 列创建 GIN 索引
CREATE INDEX idx_tags ON articles USING GIN (tags);
```

**单行写法：创建 JSONB 路径 GIN 索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (<列名> jsonb_path_ops)`
```sql
-- 为 JSONB 列创建路径操作符 GIN 索引
CREATE INDEX idx_profile ON users USING GIN (profile jsonb_path_ops);
```

**单行写法：创建数组 GIN 索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (<数组列>)`
```sql
-- 为数组列创建 GIN 索引
CREATE INDEX idx_tags_array ON posts USING GIN (tags);
```

---

## BRIN 索引

**单行写法：创建 BRIN 索引**
`CREATE INDEX <索引名> ON <表名> USING BRIN (<列名>)`
```sql
-- 为时间戳列创建 BRIN 索引
CREATE INDEX idx_created ON logs USING BRIN (created_at);
```

**单行写法：指定 BRIN 块大小**
`CREATE INDEX <索引名> ON <表名> USING BRIN (<列名>) WITH (pages_per_range = <数量>)`
```sql
-- 指定 BRIN 块范围大小
CREATE INDEX idx_created ON logs USING BRIN (created_at) WITH (pages_per_range = 128);
```

---

## 部分索引

**换行写法：创建部分索引**
`CREATE INDEX <索引名> ON <表名>(<列名>) WHERE <条件>`
```sql
-- 仅为活跃用户创建索引
CREATE INDEX idx_active_users ON users(username) WHERE status = 1;
```

---

## 表达式索引

**换行写法：创建表达式索引**
`CREATE INDEX <索引名> ON <表名>(<表达式>)`
```sql
-- 为小写邮箱创建表达式索引
CREATE INDEX idx_email_lower ON users(LOWER(email));
```

**换行写法：创建函数表达式索引**
`CREATE INDEX <索引名> ON <表名>(<函数>(<列名>))`
```sql
-- 为日期提取创建表达式索引
CREATE INDEX idx_created_date ON orders(DATE(created_at));
```

---

## 索引管理

**单行写法：查看表索引**
`SELECT <列名> FROM pg_indexes WHERE <条件>`
```sql
-- 查看表的索引信息
SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'users';
```

**单行写法：查看索引大小**
`SELECT pg_size_pretty(pg_relation_size('<索引名>'))`
```sql
-- 查看索引占用空间
SELECT pg_size_pretty(pg_relation_size('idx_username'));
```

**单行写法：删除索引**
`DROP INDEX [IF EXISTS] <索引名>`
```sql
-- 删除索引
DROP INDEX IF EXISTS idx_username;
```

**单行写法：CONCURRENTLY 创建索引**
`CREATE INDEX CONCURRENTLY <索引名> ON <表名>(<列名>)`
```sql
-- 并发创建索引不阻塞写入
CREATE INDEX CONCURRENTLY idx_email ON users(email);
```

**单行写法：CONCURRENTLY 删除索引**
`DROP INDEX CONCURRENTLY <索引名>`
```sql
-- 并发删除索引不阻塞写入
DROP INDEX CONCURRENTLY idx_email;
```

**单行写法：重建索引**
`REINDEX INDEX <索引名>`
```sql
-- 重建索引
REINDEX INDEX idx_username;
```

**单行写法：重建表所有索引**
`REINDEX TABLE <表名>`
```sql
-- 重建表的所有索引
REINDEX TABLE users;
```

**单行写法：查看索引使用情况**
`SELECT <列名> FROM pg_stat_user_indexes WHERE <条件>`
```sql
-- 查看索引使用统计
SELECT indexrelname, idx_scan, idx_tup_read
FROM pg_stat_user_indexes
WHERE relname = 'users';
```

## 参考文献

PostgreSQL 官方文档：https://www.postgresql.org/docs/
PostgreSQL 中文文档：https://www.postgresql.org/docs/current/index.html
PGXN 扩展仓库：https://pgxn.org/
PostGIS：https://postgis.net/
pgvector：https://github.com/pgvector/pgvector

## 延伸阅读

PostgreSQL 窗口函数，见 021-postgresql 模块文档。
PostgreSQL 递归查询，见 021-postgresql 模块相关文档。
SQL 基础，见 019-sql 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 PostgreSQL 课程。

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
