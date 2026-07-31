# 分区表 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## RANGE 分区

**基本写法：RANGE 分区建表**
`CREATE TABLE <表名> (...) PARTITION BY RANGE (<表达式>) (PARTITION <分区名> VALUES LESS THAN (<值>), ...)`

```sql
-- 按年份范围分区
CREATE TABLE orders (
  id BIGINT PRIMARY KEY,
  order_date DATE,
  amount DECIMAL(10,2)
)
PARTITION BY RANGE (YEAR(order_date)) (
  PARTITION p2022 VALUES LESS THAN (2023),
  PARTITION p2023 VALUES LESS THAN (2024),
  PARTITION p2024 VALUES LESS THAN (2025),
  PARTITION pmax VALUES LESS THAN MAXVALUE
);
```

**基本写法：RANGE COLUMNS 多列分区**
`PARTITION BY RANGE COLUMNS(<列1>, <列2>) (PARTITION <名> VALUES LESS THAN (<值1>, <值2>), ...)`

```sql
-- 按多列组合范围分区
CREATE TABLE sales (
  id BIGINT,
  region VARCHAR(20),
  sale_date DATE
)
PARTITION BY RANGE COLUMNS(region, sale_date) (
  PARTITION p_east_2024 VALUES LESS THAN ('EAST', '2025-01-01'),
  PARTITION p_west_2024 VALUES LESS THAN ('WEST', '2025-01-01'),
  PARTITION p_other VALUES LESS THAN (MAXVALUE, MAXVALUE)
);
```

---

## LIST 分区

**基本写法：LIST 分区建表**
`CREATE TABLE <表名> (...) PARTITION BY LIST (<表达式>) (PARTITION <分区名> VALUES IN (<值列表>), ...)`

```sql
-- 按地区枚举分区
CREATE TABLE customers (
  id BIGINT PRIMARY KEY,
  region_code INT
)
PARTITION BY LIST (region_code) (
  PARTITION p_north VALUES IN (1, 2, 3),
  PARTITION p_south VALUES IN (4, 5, 6),
  PARTITION p_east VALUES IN (7, 8),
  PARTITION p_west VALUES IN (9, 10)
);
```

**基本写法：LIST COLUMNS 多列分区**
`PARTITION BY LIST COLUMNS(<列>) (PARTITION <名> VALUES IN (<值列表>), ...)`

```sql
-- 按字符串列分区
CREATE TABLE users (
  id BIGINT,
  country VARCHAR(10)
)
PARTITION BY LIST COLUMNS(country) (
  PARTITION p_cn VALUES IN ('CN', 'HK', 'TW'),
  PARTITION p_us VALUES IN ('US', 'CA'),
  PARTITION p_other VALUES IN ('UK', 'FR', 'DE')
);
```

---

## HASH 与 KEY 分区

**基本写法：HASH 分区**
`CREATE TABLE <表名> (...) PARTITION BY HASH(<表达式>) PARTITIONS <分区数>;`

```sql
-- 按用户 ID 哈希分 8 个区
CREATE TABLE user_logs (
  id BIGINT,
  user_id BIGINT,
  log_text TEXT
)
PARTITION BY HASH(user_id)
PARTITIONS 8;
```

**基本写法：LINEAR HASH 分区**
`PARTITION BY LINEAR HASH(<表达式>) PARTITIONS <分区数>;`

```sql
-- 线性哈希，增删分区更快但分布可能不均
CREATE TABLE t_logs (id BIGINT)
PARTITION BY LINEAR HASH(id)
PARTITIONS 16;
```

**基本写法：KEY 分区**
`PARTITION BY KEY(<列>) PARTITIONS <分区数>;`

```sql
-- KEY 分区由 MySQL 内部哈希，类似主键哈希
CREATE TABLE user_events (
  id BIGINT PRIMARY KEY,
  event VARCHAR(50)
)
PARTITION BY KEY()
PARTITIONS 4;
```

---

## 分区管理

**基本写法：添加分区**
`ALTER TABLE <表名> ADD PARTITION (PARTITION <分区名> VALUES LESS THAN (<值>));`

```sql
-- 为 RANGE 分区表添加新分区
ALTER TABLE orders
ADD PARTITION (
  PARTITION p2025 VALUES LESS THAN (2026)
);
```

**基本写法：删除分区**
`ALTER TABLE <表名> DROP PARTITION <分区名>;`

```sql
-- 删除分区（连同数据一起删除）
ALTER TABLE orders DROP PARTITION p2022;
```

**基本写法：重组分区**
`ALTER TABLE <表名> REORGANIZE PARTITION <分区名> INTO (PARTITION <新分区> ...);`

```sql
-- 将 p2024 拆分为 p2024_h1 和 p2024_h2
ALTER TABLE orders
REORGANIZE PARTITION p2024 INTO (
  PARTITION p2024_h1 VALUES LESS THAN ('2024-07-01'),
  PARTITION p2024_h2 VALUES LESS THAN (2025)
);
```

**基本写法：合并分区**
`ALTER TABLE <表名> REORGANIZE PARTITION <分区1>, <分区2> INTO (PARTITION <新分区> ...);`

```sql
-- 合并两个相邻分区
ALTER TABLE orders
REORGANIZE PARTITION p2024_h1, p2024_h2 INTO (
  PARTITION p2024 VALUES LESS THAN (2025)
);
```

---

## 分区维护

**基本写法：查看分区信息**
`SELECT * FROM information_schema.PARTITIONS WHERE table_name = '<表名>';`

```sql
-- 查看表分区、行数、数据长度
SELECT partition_name, partition_method, table_rows, data_length
FROM information_schema.PARTITIONS
WHERE table_name = 'orders';
```

**基本写法：检查分区**
`ALTER TABLE <表名> CHECK PARTITION <分区名>;`

```sql
-- 检查指定分区数据完整性
ALTER TABLE orders CHECK PARTITION p2024;
```

**基本写法：重建分区**
`ALTER TABLE <表名> REBUILD PARTITION <分区名>;`

```sql
-- 重建分区回收碎片
ALTER TABLE orders REBUILD PARTITION p2023;
```

**基本写法：分析分区**
`ALTER TABLE <表名> ANALYZE PARTITION <分区名>;`

```sql
-- 重新收集分区统计信息
ALTER TABLE orders ANALYZE PARTITION p2024;
```

**基本写法：移除分区（保留数据）**
`ALTER TABLE <表名> REMOVE PARTITIONING;`

```sql
-- 移除分区结构但保留数据为普通表
ALTER TABLE orders REMOVE PARTITIONING;
```

---