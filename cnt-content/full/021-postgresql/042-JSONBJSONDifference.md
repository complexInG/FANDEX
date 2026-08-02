---
order: 420
title: JSONB与JSON差异
module: 'postgresql'
category: 数据库
difficulty: intermediate
description: PostgreSQL JSONB 与 JSON 类型对比：存储格式、查询性能、索引策略、GIN 索引与 JSON 路径表达式。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'postgresql/040-ParallelQuery'
  - 'postgresql/041-LogicalPhysicalReplicationCompare'
  - 'postgresql/043-ExtensionModuleDetailed'
prerequisites:
  - 'postgresql/001-OverviewInstallConfig'
---


## 1. JSON 与 JSONB 对比

### 1.1 核心差异

| 维度      | JSON           | JSONB            |
| --------- | -------------- | ---------------- |
| 存储格式  | 原始文本       | 二进制（分解后） |
| 插入速度  | 快（直接存储） | 慢（需解析转换） |
| 查询速度  | 慢（每次解析） | 快（已分解）     |
| 空格/顺序 | 保留           | 不保留           |
| 重复键    | 保留           | 保留最后一个     |
| 索引支持  | 无             | GIN 索引         |
| 操作符    | 有限           | 丰富             |
| 推荐度    | 仅归档         | 日常使用         |

### 1.2 存储差异示例

```sql
-- JSON: 保留原始格式（空格、键顺序）
SELECT '{"name": "Alice", "age": 30}'::json;
-- {"name": "Alice", "age": 30}

-- JSONB: 重新格式化（去空格、键排序）
SELECT '{"name": "Alice", "age": 30}'::jsonb;
-- {"age": 30, "name": "Alice"}

-- 重复键处理
SELECT '{"a": 1, "a": 2}'::json;   -- {"a": 1, "a": 2}
SELECT '{"a": 1, "a": 2}'::jsonb;  -- {"a": 2}
```

## 2. JSONB 操作符

### 2.1 提取操作符

```sql
-- -> 获取 JSON 对象字段（返回 JSON 类型）
SELECT '{"a":1,"b":2}'::jsonb -> 'a';      -- 1
SELECT '[1,2,3]'::jsonb -> 1;              -- 2

-- ->> 获取 JSON 对象字段（返回文本）
SELECT '{"a":1,"b":2}'::jsonb ->> 'a';     -- "1" (text)
SELECT '{"a":"hello"}'::jsonb ->> 'a';     -- "hello" (text)

-- #> 按路径获取（返回 JSON）
SELECT '{"a":{"b":1}}'::jsonb #> '{a,b}';  -- 1

-- #>> 按路径获取（返回文本）
SELECT '{"a":{"b":1}}'::jsonb #>> '{a,b}'; -- "1"
```

### 2.2 包含操作符

```sql
-- @> 包含（左侧是否包含右侧）
SELECT '{"a":1,"b":2}'::jsonb @> '{"a":1}'::jsonb;    -- true
SELECT '{"a":1,"b":2}'::jsonb @> '{"a":2}'::jsonb;    -- false

-- <@ 被包含
SELECT '{"a":1}'::jsonb <@ '{"a":1,"b":2}'::jsonb;    -- true

-- ? 键是否存在
SELECT '{"a":1}'::jsonb ? 'a';                         -- true

-- ?| 任一键是否存在
SELECT '{"a":1}'::jsonb ?| array['a','c'];             -- true

-- ?& 所有键是否都存在
SELECT '{"a":1}'::jsonb ?& array['a','c'];             -- false
```

### 2.3 修改操作符

```sql
-- || 合并（右侧覆盖左侧同键）
SELECT '{"a":1,"b":2}'::jsonb || '{"b":3,"c":4}'::jsonb;
-- {"a":1,"b":3,"c":4}

-- - 删除键
SELECT '{"a":1,"b":2}'::jsonb - 'a';     -- {"b":2}
SELECT '{"a":1,"b":2}'::jsonb - 'b';     -- {"a":1}

-- - 删除数组元素
SELECT '["a","b","c"]'::jsonb - 1;       -- ["a","c"]

-- #- 按路径删除
SELECT '{"a":{"b":1,"c":2}}'::jsonb #- '{a,b}';
-- {"a":{"c":2}}
```

## 3. JSONB 函数

### 3.1 创建与转换

```sql
-- jsonb_build_object
SELECT jsonb_build_object('name', 'Alice', 'age', 30);
-- {"name":"Alice","age":30}

-- jsonb_build_array
SELECT jsonb_build_array(1, 'hello', null, true);
-- [1, "hello", null, true]

-- jsonb_object 从键值对数组创建
SELECT jsonb_object('{a,b,c}', '{1,2,3}');
-- {"a":"1","b":"2","c":"3"}

-- 行转 JSON
SELECT to_jsonb(row(1, 'Alice'));
-- {"f1":1,"f2":"Alice"}

-- 聚合为 JSON 数组
SELECT jsonb_agg(name) FROM users;
-- ["Alice","Bob","Charlie"]

-- 聚合为 JSON 对象
SELECT jsonb_object_agg(name, age) FROM users;
-- {"Alice":30,"Bob":25}
```

### 3.2 查询与处理

```sql
-- jsonb_array_elements 展开数组
SELECT jsonb_array_elements('[1,2,3]'::jsonb);
-- 1, 2, 3 (每行一个)

-- jsonb_each 展开对象
SELECT * FROM jsonb_each('{"a":1,"b":2}'::jsonb);
-- key | value
-- a   | 1
-- b   | 2

-- jsonb_each_text 展开对象（文本值）
SELECT * FROM jsonb_each_text('{"a":1,"b":"hello"}'::jsonb);

-- jsonb_typeof 获取类型
SELECT jsonb_typeof('"hello"'::jsonb);    -- string
SELECT jsonb_typeof('123'::jsonb);        -- number
SELECT jsonb_typeof('true'::jsonb);       -- boolean
SELECT jsonb_typeof('null'::jsonb);       -- null
SELECT jsonb_typeof('[]'::jsonb);         -- array
SELECT jsonb_typeof('{}'::jsonb);         -- object

-- jsonb_pretty 格式化
SELECT jsonb_pretty('{"a":1,"b":[2,3]}'::jsonb);
-- {
--     "a": 1,
--     "b": [
--         2,
--         3
--     ]
-- }
```

## 4. JSON 路径表达式（SQL/JSON Path）

### 4.1 基本语法（PostgreSQL 12+）

```sql
-- jsonb_path_query: 返回所有匹配
SELECT jsonb_path_query(
    '{"a": [1,2,3], "b": [4,5,6]}'::jsonb,
    '$.*[*]'
);
-- 1, 2, 3, 4, 5, 6

-- jsonb_path_query_first: 返回第一个匹配
SELECT jsonb_path_query_first(
    '{"a": 1, "b": 2}'::jsonb,
    '$.b'
);
-- 2

-- jsonb_path_exists: 是否存在匹配
SELECT jsonb_path_exists(
    '{"a": 1}'::jsonb,
    '$.b'
);
-- false
```

### 4.2 过滤表达式

```sql
-- ?() 过滤条件
SELECT jsonb_path_query(
    '[{"name":"iPhone","price":7999},
      {"name":"AirPods","price":1299},
      {"name":"MacBook","price":12999}]'::jsonb,
    '$[*] ? (@.price > 5000)'
);
-- {"name":"iPhone","price":7999}
-- {"name":"MacBook","price":12999}

-- .** 递归通配
SELECT jsonb_path_query(
    '{"a":{"b":{"c":1}},"d":2}'::jsonb,
    '$.**.c'
);
-- 1
```

## 5. JSONB 索引

### 5.1 GIN 索引

```sql
-- 默认 GIN 索引（支持 @>, ?, ?|, ?& 操作符）
CREATE INDEX idx_products_attrs ON products USING gin (attrs);

-- 查询走索引
SELECT * FROM products WHERE attrs @> '{"color": "red"}';

-- jsonb_path_ops GIN 索引（仅支持 @>，更小更快）
CREATE INDEX idx_products_attrs_path ON products USING gin (attrs jsonb_path_ops);
```

### 5.2 btree 索引（排序比较）

```sql
-- JSONB 支持 btree 排序
CREATE INDEX idx_data ON events USING btree (data);

-- 排序查询
SELECT * FROM events ORDER BY data;
```

### 5.3 表达式索引

```sql
-- 为特定字段建索引
CREATE INDEX idx_user_name ON users ((data->>'name'));
CREATE INDEX idx_user_age ON users (((data->>'age')::int));

-- 查询走索引
SELECT * FROM users WHERE data->>'name' = 'Alice';
SELECT * FROM users WHERE (data->>'age')::int > 25;
```

### 5.4 索引选择策略

| 查询模式         | 推荐索引             |
| ---------------- | -------------------- |
| `@>` 包含查询    | GIN (jsonb_path_ops) |
| `?` 键存在       | GIN (默认)           |
| `->>` 提取后比较 | btree 表达式索引     |
| JSON Path 查询   | GIN (默认)           |
| 排序             | btree                |

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
