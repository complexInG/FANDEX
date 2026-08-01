---
order: 500
title: 数组类型操作 语法速查手册
module: 021-postgresql
category: '021-postgresql'
difficulty: beginner
description: 数组类型操作 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 数组定义与构造

**基本写法：建表定义数组列**
`<列名> <元素类型>[]`

```sql
-- 定义整型数组和文本数组列
CREATE TABLE projects (
  id SERIAL PRIMARY KEY,
  tags TEXT[],
  member_ids BIGINT[],
  scores INTEGER[]
);
```

**基本写法：数组字面量构造**
`ARRAY[<值1>, <值2>, ...]` 或 `'{<值1>,<值2>,...}'`

```sql
-- 使用 ARRAY 构造器（推荐）
INSERT INTO projects (tags) VALUES (ARRAY['java','spring','web']);
-- 使用字符串字面量
INSERT INTO projects (tags) VALUES ('{java,spring,web}');
```

**基本写法：从子查询构造数组**
`ARRAY(SELECT <列> FROM <表> WHERE <条件>)`

```sql
-- 将查询结果转为数组
SELECT id, ARRAY(SELECT name FROM users WHERE dept_id = 1) AS dept_members;
```

**基本写法：多维数组**
`<元素类型>[][]`

```sql
-- 二维数组
CREATE TABLE matrix (data INTEGER[][]);
INSERT INTO matrix VALUES (ARRAY[[1,2],[3,4]]);
```

---

## 数组访问

**基本写法：按下标访问元素**
`<数组列>[<下标>]`

```sql
-- PostgreSQL 数组下标从 1 开始
SELECT tags[1] AS first_tag FROM projects WHERE id = 1;
SELECT member_ids[1:3] AS first_three FROM projects WHERE id = 1;  -- 切片
```

**基本写法：获取数组长度**
`array_length(<数组列>, <维度>)`

```sql
-- 获取第一维长度
SELECT array_length(tags, 1) AS tag_count FROM projects;
-- 获取多维数组各维长度
SELECT array_length(data, 1), array_length(data, 2) FROM matrix;
```

**基本写法：数组展开为行**
`unnest(<数组列>)`

```sql
-- 将数组展开为多行（常用于关联查询）
SELECT id, unnest(tags) AS tag FROM projects;
-- 多数组同步展开
SELECT id, tag, score
FROM projects
CROSS JOIN unnest(tags, scores) AS t(tag, score);
```

---

## 数组包含与匹配

**基本写法：包含元素判断**
`<值> = ANY(<数组>)` / `<数组> @> <数组>`

```sql
-- 是否包含任一等于该值的元素
SELECT * FROM projects WHERE 'java' = ANY(tags);
-- 是否包含指定子集（@> 包含）
SELECT * FROM projects WHERE tags @> ARRAY['java','spring'];
-- 是否被包含（<@）
SELECT * FROM projects WHERE ARRAY['java'] <@ tags;
```

**基本写法：重叠判断**
`<数组> && <数组>`

```sql
-- 两个数组是否有公共元素（存在交集）
SELECT * FROM projects WHERE tags && ARRAY['java','python'];
```

**基本写法：查找元素位置**
`array_position(<数组>, <值>)`

```sql
-- 返回元素首次出现的下标（从 1 开始）
SELECT array_position(tags, 'spring') FROM projects WHERE id = 1;
-- 所有出现位置
SELECT array_positions(tags, 'java') FROM projects;
```

---

## 数组修改

**基本写法：连接数组**
`<数组1> || <数组2>`

```sql
-- 数组连接
SELECT ARRAY[1,2] || ARRAY[3,4] AS result;  -- {1,2,3,4}
-- 追加元素
SELECT tags || 'new_tag' FROM projects WHERE id = 1;
```

**基本写法：追加元素**
`array_append(<数组>, <值>)`

```sql
-- 在末尾追加元素
UPDATE projects SET tags = array_append(tags, 'microservice') WHERE id = 1;
```

**基本写法：删除元素**
`array_remove(<数组>, <值>)`

```sql
-- 删除所有匹配元素
UPDATE projects SET tags = array_remove(tags, 'deprecated') WHERE id = 1;
```

**基本写法：替换元素**
`array_replace(<数组>, <旧值>, <新值>)`

```sql
-- 替换所有匹配元素
UPDATE projects SET tags = array_replace(tags, 'old', 'new') WHERE id = 1;
```

**基本写法：数组去重**
`ARRAY(SELECT DISTINCT unnest(<数组>))`

```sql
-- 数组去重
SELECT id, ARRAY(SELECT DISTINCT unnest(tags)) AS unique_tags FROM projects;
```

---

## 数组函数

**基本写法：数组转字符串**
`array_to_string(<数组>, <分隔符> [, <NULL替代>])`

```sql
-- 拼接为逗号分隔字符串
SELECT array_to_string(tags, ', ') AS tag_str FROM projects;
-- NULL 用占位符替代
SELECT array_to_string(scores, ',', 'N/A') FROM projects;
```

**基本写法：字符串转数组**
`string_to_array(<字符串>, <分隔符>)`

```sql
-- 按分隔符拆分为数组
SELECT string_to_array('a,b,c', ',') AS arr;  -- {a,b,c}
```

**基本写法：数组聚合**
`array_agg(<列>)`

```sql
-- 将分组内的值聚合为数组
SELECT dept_id, array_agg(user_name) AS members
FROM users GROUP BY dept_id;
```

**基本写法：数组与集合运算**
`array_cat / array_intersect / array_union`

```sql
-- 数组并集
SELECT ARRAY(SELECT unnest(ARRAY[1,2,3]) UNION SELECT unnest(ARRAY[3,4,5]));
-- 数组交集
SELECT ARRAY(SELECT unnest(ARRAY[1,2,3]) INTERSECT SELECT unnest(ARRAY[2,3,4]));
```

---

## 数组索引

**基本写法：创建 GIN 索引加速数组查询**
`CREATE INDEX <索引名> ON <表名> USING GIN (<数组列>);`

```sql
-- 为数组列建 GIN 索引（支持 @>、&& 等操作符）
CREATE INDEX idx_projects_tags ON projects USING GIN (tags);
-- 使用索引加速包含查询
SELECT * FROM projects WHERE tags @> ARRAY['java'];
```

---

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与安装配置 | 001-OverviewInstallConfig | 本文的前置基础 |
| 事务与并发控制 | 002-TransactionConcurrencyControl | 本文的并列主题 |
| 索引与查询优化 | 003-IndexQueryOptimization | 本文的性能延伸 |
| 高级SQL与扩展 | 004-AdvancedSQLExtension | 本文的并列主题 |
| 复制与高可用 | 005-ReplicationHA | 本文的并列主题 |
| 体系架构 | 006-SystemArchitecture | 本文的原理深化 |
| 锁机制 | 007-LockMechanism | 本文的原理深化 |
| 死锁检测与处理 | 008-DeadlockDetectionHandling | 本文的并列主题 |
| VACUUM机制 | 009-VACUUMMechanism | 本文的原理深化 |
| 事务ID回卷预防 | 010-TransactionIDWraparoundPrevention | 本文的并列主题 |
| 索引类型 | 011-IndexType | 本文的并列主题 |
| 覆盖索引与部分索引 | 012-CoveringIndexPartialIndex | 本文的并列主题 |
| KNN向量索引 | 013-KNNVectorIndex | 本文的并列主题 |
| 查询优化 | 014-QueryOptimization | 本文的性能延伸 |
| 分区表 | 015-PartitionedTable | 本文的并列主题 |
| 分区裁剪与分区连接 | 016-PartitionPruningPartitionJoin | 本文的并列主题 |
| 高级SQL | 017-AdvancedSQL | 本文的并列主题 |
| MERGE语句增强 | 018-MERGEStatementEnhancement | 本文的并列主题 |
| JSON-TABLE | 019-JSONTABLE | 本文的并列主题 |
| 全文检索 | 020-FullTextSearch | 本文的并列主题 |
| 地理空间对象 | 021-GeoSpatialObject | 本文的并列主题 |
| 存储过程与函数 | 022-StoredProcedureAndFunction | 本文的并列主题 |
| 触发器与事件触发器 | 023-TriggerEventTrigger | 本文的并列主题 |
| 扩展模块 | 024-ExtensionModule | 本文的并列主题 |
| FDW外部数据包装器 | 025-FDWFDW | 本文的并列主题 |
| 流复制 | 026-StreamingReplication | 本文的并列主题 |
| 级联复制 | 027-CascadingReplication | 本文的并列主题 |
| 物理复制槽 | 028-PhysicalReplicationSlot | 本文的并列主题 |
| 逻辑解码与输出插件 | 029-LogicalDecodingOutputPlugin | 本文的并列主题 |
| 增量备份 | 030-IncrementalBackup | 本文的并列主题 |
| 订阅与发布 | 031-SubscribePublish | 本文的并列主题 |
| SSL-TLS加密连接 | 032-SSLEncryptionConnection | 本文的安全延伸 |
| 基于角色的权限管理 | 033-RoleBasedPermissionManagement | 本文的安全延伸 |
| 行级安全策略 | 034-RowLevelSecurity | 本文的安全延伸 |
| 数据加密存储 | 035-DataEncryptionStorage | 本文的安全延伸 |
| 审计日志 | 036-AuditLog | 本文的并列主题 |
| 序列与自增列 | 037-SequenceAutoIncrement | 本文的并列主题 |
| 生成列 | 038-GeneratedColumn | 本文的并列主题 |
| 可更新视图 | 039-UpdatableView | 本文的并列主题 |
| 并行查询 | 040-ParallelQuery | 本文的并列主题 |
| 逻辑复制与物理复制对比 | 041-LogicalPhysicalReplicationCompare | 本文的并列主题 |
| JSONB与JSON差异 | 042-JSONBJSONDifference | 本文的并列主题 |
| 扩展模块详解 | 043-ExtensionModuleDetailed | 本文的并列主题 |
| PostgreSQL DDL 数据定义 | 044-DDL | 本文的并列主题 |
| PostgreSQL DML 数据操作 | 045-DML | 本文的并列主题 |
| PostgreSQL 窗口函数 | 046-WindowFunction | 本文的并列主题 |
| PostgreSQL CTE 递归查询 | 047-CTE | 本文的并列主题 |
| PostgreSQL psql CLI 命令 | 048-PsqlCLI | 本文的并列主题 |
| pg_dump 与 pg_restore 语法速查手册 | 049-PgDumpRestore | 本文的并列主题 |
| 数组类型操作 语法速查手册 | 050-ArrayType | 本文自身 |
| 模式（Schema）管理 语法速查手册 | 051-SchemaManagement | 本文的并列主题 |
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
