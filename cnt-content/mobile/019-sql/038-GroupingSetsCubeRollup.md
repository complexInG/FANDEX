# SQL GROUPING SETS / CUBE / ROLLUP 多维分组语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## GROUPING SETS 自定义分组

**基本写法：指定多个分组集**
`GROUP BY GROUPING SETS ((<列1>,<列2>), (<列1>), (<列2>), ())`
```sql
-- 一次性输出多种分组聚合结果，等价于多个 UNION ALL
SELECT
  COALESCE(region, '所有地区') AS region,
  COALESCE(product, '所有产品') AS product,
  SUM(amount) AS total
FROM sales
GROUP BY GROUPING SETS (
  (region, product),   -- 按地区+产品
  (region),            -- 仅按地区
  (product),           -- 仅按产品
  ()                   -- 总计
)
ORDER BY region, product;
```

---

**基本写法：单列分组集**
`GROUP BY GROUPING SETS ((<列1>), (<列2>))`
```sql
-- 对不同列分别分组聚合
SELECT dept, NULL AS job, COUNT(*) AS cnt FROM emp GROUP BY GROUPING SETS ((dept),(job));
-- 等价于
SELECT dept, NULL AS job, COUNT(*) FROM emp GROUP BY dept
UNION ALL
SELECT NULL, job, COUNT(*) FROM emp GROUP BY job;
```

---

## ROLLUP 层级汇总

**基本写法：ROLLUP 递减分组**
`GROUP BY ROLLUP (<列1>, <列2>, <列3>)`
```sql
-- ROLLUP(a,b,c) 等价于 GROUPING SETS ((a,b,c),(a,b),(a),())
-- 按列顺序从右到左递减，生成层级小计与总计
SELECT
  COALESCE(year, '总计') AS year,
  COALESCE(region, '小计') AS region,
  COALESCE(product, '-') AS product,
  SUM(amount) AS total
FROM sales
GROUP BY ROLLUP (year, region, product)
ORDER BY year, region, product;
-- 输出：(2024,East,A) (2024,East,小计) (2024,总计,-) (总计,小计,-)
```

---

**基本写法：ROLLUP 部分列**
`GROUP BY <列1>, ROLLUP(<列2>, <列3>)`
```sql
-- 不对第一列做汇总，仅对后续列 ROLLUP
SELECT dept, job, SUM(salary) AS total
FROM employees
GROUP BY dept, ROLLUP(job, level);
-- 等价于 GROUPING SETS ((dept,job,level),(dept,job),(dept))
```

---

## CUBE 全组合汇总

**基本写法：CUBE 全维度组合**
`GROUP BY CUBE (<列1>, <列2>, <列3>)`
```sql
-- CUBE(a,b,c) 生成 2^3=8 种分组：
-- (a,b,c)(a,b)(a,c)(b,c)(a)(b)(c)()
-- 适合多维交叉分析
SELECT
  COALESCE(year, '全部') AS yr,
  COALESCE(region, '全部') AS reg,
  COALESCE(product, '全部') AS prod,
  SUM(amount) AS total,
  COUNT(*) AS cnt
FROM sales
GROUP BY CUBE (year, region, product)
ORDER BY year, region, product;
```

---

**基本写法：CUBE 部分列**
`GROUP BY <列1>, CUBE(<列2>, <列3>)`
```sql
-- dept 固定分组，job 与 level 交叉
SELECT dept, job, level, SUM(salary)
FROM employees
GROUP BY dept, CUBE (job, level);
-- 4 种组合：(dept,job,level)(dept,job)(dept,level)(dept)
```

---

## GROUPING 函数识别小计行

**基本写法：GROUPING 标记**
`GROUPING(<列>) -- 返回 1 表示该列在此行被聚合（NULL 为汇总标记）`
```sql
-- 区分原始 NULL 与汇总产生的 NULL
SELECT
  year,
  region,
  SUM(amount) AS total,
  GROUPING(year) AS gy,       -- 1=年汇总行
  GROUPING(region) AS gr      -- 1=地区汇总行
FROM sales
GROUP BY ROLLUP(year, region);

-- 用 CASE 生成可读标签
SELECT
  CASE WHEN GROUPING(year)=1 THEN '年总计' ELSE year::text END AS yr,
  CASE WHEN GROUPING(region)=1 THEN '地区小计' ELSE region END AS reg,
  SUM(amount) AS total
FROM sales
GROUP BY ROLLUP(year, region);
```

---

**基本写法：GROUPING_ID 组合标记**
`GROUPING_ID(<列1>, <列2>, ...)`
```sql
-- 返回位掩码，标识当前行对应哪个分组集
SELECT year, region, product,
  GROUPING_ID(year, region, product) AS gid,
  SUM(amount) AS total
FROM sales
GROUP BY ROLLUP(year, region, product);
-- gid=0: 明细 (year,region,product)
-- gid=1: year+region 小计（product 被 rollup）
-- gid=3: year 小计
-- gid=7: 总计
```

---

## 三者对比

**基本写法：对比总结**
`GROUP BY <ROLLUP|CUBE|GROUPING SETS> (...)`
```sql
-- ROLLUP(a,b): 3 组 = (a,b)(a)()
-- CUBE(a,b):   4 组 = (a,b)(a)(b)()
-- GROUPING SETS((a,b),(a),(b),()): 等价于 CUBE(a,b)

-- ROLLUP 适合层级维度（年>月>日）
-- CUBE 适合独立维度交叉分析
-- GROUPING SETS 适合自定义任意分组组合
```

---

## MySQL 兼容写法

**基本写法：MySQL 8.0+ 支持**
`GROUP BY <列> WITH ROLLUP`
```sql
-- MySQL 8.0 之前用 WITH ROLLUP，不支持 CUBE/GROUPING SETS
SELECT year, region, SUM(amount) AS total
FROM sales
GROUP BY year, region WITH ROLLUP;

-- MySQL 8.0+ 完整支持 GROUPING SETS/CUBE/ROLLUP
SELECT year, region, SUM(amount)
FROM sales
GROUP BY ROLLUP(year, region);
```
