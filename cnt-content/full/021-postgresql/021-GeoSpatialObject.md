---
order: 66
title: 地理空间对象
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL地理空间对象：PostGIS扩展、几何类型、空间索引与空间查询
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/JSON表格函数
  - postgresql/全文检索
  - postgresql/存储过程与函数
  - postgresql/触发器与事件触发器
prerequisites:
  - postgresql/概述与安装配置
---

## 1. PostGIS 概述

PostGIS 是 PostgreSQL 的空间数据库扩展，支持 OGC 简单要素规范。

```sql
-- 安装扩展
CREATE EXTENSION postgis;

-- 查看版本
SELECT PostGIS_Version();
```

## 2. 几何类型

```sql
-- 点
SELECT ST_MakePoint(116.3975, 39.9087);

-- 线
SELECT ST_MakeLine(ST_MakePoint(0,0), ST_MakePoint(1,1));

-- 多边形
SELECT ST_MakePolygon(ST_MakeLine(ARRAY[
    ST_MakePoint(0,0), ST_MakePoint(1,0),
    ST_MakePoint(1,1), ST_MakePoint(0,0)
]));

-- 创建空间列
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    geom GEOMETRY(Point, 4326)
);
```

## 3. 空间索引

```sql
-- GiST 空间索引
CREATE INDEX idx_locations_geom ON locations USING GIST (geom);

-- SP-GiST 索引
CREATE INDEX idx_locations_geom_spgist ON locations USING SPGIST (geom);
```

## 4. 空间查询

```sql
-- 距离查询
SELECT name, ST_Distance(geom::geography,
    ST_SetSRID(ST_MakePoint(116.4, 39.9), 4326)::geography) AS dist
FROM locations
ORDER BY dist LIMIT 10;

-- 范围查询
SELECT * FROM locations
WHERE ST_DWithin(geom::geography,
    ST_SetSRID(ST_MakePoint(116.4, 39.9), 4326)::geography, 3000);

-- 包含查询
SELECT * FROM regions
WHERE ST_Contains(boundary, ST_MakePoint(116.4, 39.9));

-- 相交查询
SELECT * FROM parcels
WHERE ST_Intersects(geom, ST_MakeEnvelope(116.3, 39.8, 116.5, 40.0, 4326));
```

## 5. 坐标系转换

```sql
-- WGS84 (4326) → Web Mercator (3857)
SELECT ST_Transform(geom, 3857) FROM locations;

-- 计算面积（需要投影坐标系）
SELECT ST_Area(ST_Transform(geom, 32650)) AS area_sqm FROM parcels;
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
