# SQL PIVOT / UNPIVOT 进阶语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## PIVOT 行转列

**基本写法：SQL Server / Oracle PIVOT**
`SELECT * FROM (<源查询>) AS <别名> PIVOT (<聚合>(<值列>) FOR <列> IN ([<值1>],[<值2>])) AS <别名>`
```sql
-- SQL Server / Oracle 原生 PIVOT
SELECT *
FROM (
  SELECT dept, month, amount FROM sales
) AS src
PIVOT (
  SUM(amount) FOR month IN (
    [Jan], [Feb], [Mar], [Apr], [May], [Jun]
  )
) AS pvt
ORDER BY dept;
-- 输出：dept | Jan | Feb | Mar | Apr | May | Jun
```

---

**基本写法：动态列名 PIVOT（动态 SQL）**
`EXEC('SELECT ... PIVOT ... IN (' + @cols + ')')`
```sql
-- SQL Server 动态生成列名
DECLARE @cols AS NVARCHAR(MAX);
SELECT @cols = STRING_AGG(QUOTENAME(month), ',')
  FROM (SELECT DISTINCT month FROM sales) t;

DECLARE @sql AS NVARCHAR(MAX) = '
SELECT * FROM (SELECT dept, month, amount FROM sales) src
PIVOT (SUM(amount) FOR month IN (' + @cols + ')) pvt';

EXEC sp_executesql @sql;
```

---

## CASE 表达式实现 PIVOT（通用）

**基本写法：CASE WHEN 交叉表**
`SUM(CASE WHEN <条件> THEN <值> ELSE 0 END) AS <列名>`
```sql
-- 所有数据库通用的行转列方案
SELECT
  dept,
  SUM(CASE WHEN month = 'Jan' THEN amount ELSE 0 END) AS Jan,
  SUM(CASE WHEN month = 'Feb' THEN amount ELSE 0 END) AS Feb,
  SUM(CASE WHEN month = 'Mar' THEN amount ELSE 0 END) AS Mar,
  SUM(amount) AS total
FROM sales
GROUP BY dept
ORDER BY dept;
```

---

**基本写法：FILTER 子句（PostgreSQL）**
`SUM(<值>) FILTER (WHERE <条件>) AS <列名>`
```sql
-- PostgreSQL 简洁写法
SELECT
  dept,
  SUM(amount) FILTER (WHERE month = 'Jan') AS Jan,
  SUM(amount) FILTER (WHERE month = 'Feb') AS Feb,
  SUM(amount) FILTER (WHERE month = 'Mar') AS Mar
FROM sales
GROUP BY dept;
```

---

## crosstab（PostgreSQL）

**基本写法：tablefunc 扩展**
`SELECT * FROM crosstab('<源查询>') AS <结果表结构>(<行键> <类型>, <列1> <类型>, ...)`
```sql
-- PostgreSQL tablefunc 扩展
CREATE EXTENSION IF NOT EXISTS tablefunc;

SELECT *
FROM crosstab(
  'SELECT dept, month, amount FROM sales ORDER BY 1,2'
) AS ct(
  dept text,
  Jan numeric, Feb numeric, Mar numeric,
  Apr numeric, May numeric, Jun numeric
);
```

---

## JSONB 实现动态 PIVOT（PostgreSQL）

**基本写法：jsonb_pivot 自定义聚合**
`SELECT <行键>, jsonb_object_agg(<列>, <值>) FROM <表> GROUP BY <行键>`
```sql
-- PostgreSQL 用 JSONB 动态生成列
SELECT
  dept,
  jsonb_object_agg(month, amount) AS 月份金额
FROM sales
GROUP BY dept;
-- 输出：dept | {"Jan":100, "Feb":200, "Mar":150}

-- 展开为行查看
SELECT dept, kv.key AS month, kv.value::numeric AS amount
FROM (
  SELECT dept, jsonb_object_agg(month, amount) AS data FROM sales GROUP BY dept
) t, jsonb_each_text(t.data) AS kv(key, value);
```

---

## UNPIVOT 列转行

**基本写法：SQL Server / Oracle UNPIVOT**
`SELECT * FROM <表> UNPIVOT (<值列> FOR <列名列> IN ([<列1>],[<列2>])) AS <别名>`
```sql
-- 列转行
SELECT dept, month, amount
FROM monthly_sales
UNPIVOT (
  amount FOR month IN ([Jan], [Feb], [Mar], [Apr], [May], [Jun])
) AS upvt;
-- 输入：dept | Jan | Feb | Mar ...
-- 输出：dept | Jan | 100 / dept | Feb | 200 ...
```

---

**基本写法：UNION ALL 通用列转行**
`SELECT <键>, '列名1' AS <列>, <列1> AS <值> UNION ALL ...`
```sql
-- 所有数据库通用
SELECT dept, 'Jan' AS month, Jan AS amount FROM monthly_sales WHERE Jan IS NOT NULL
UNION ALL
SELECT dept, 'Feb' AS month, Feb AS amount FROM monthly_sales WHERE Feb IS NOT NULL
UNION ALL
SELECT dept, 'Mar' AS month, Mar AS amount FROM monthly_sales WHERE Mar IS NOT NULL;
```

---

## VALUES 子句列转行

**基本写法：PostgreSQL/标准 VALUES**
`SELECT <键>, m.month, m.amount FROM <表> CROSS JOIN LATERAL (VALUES ...) AS m(...)`
```sql
-- PostgreSQL 用 LATERAL + VALUES
SELECT dept, m.month, m.amount
FROM monthly_sales ms
CROSS JOIN LATERAL (
  VALUES
    ('Jan', ms.Jan),
    ('Feb', ms.Feb),
    ('Mar', ms.Mar)
) AS m(month, amount)
WHERE m.amount IS NOT NULL;
```

---

## 实战：交叉报表

**基本写法：季度+产品交叉报表**
`SUM(CASE WHEN <产品> THEN <值> END) FILTER ...`
```sql
-- 年度产品季度销售交叉表
SELECT
  product,
  SUM(CASE WHEN quarter = 1 THEN amount ELSE 0 END) AS Q1,
  SUM(CASE WHEN quarter = 2 THEN amount ELSE 0 END) AS Q2,
  SUM(CASE WHEN quarter = 3 THEN amount ELSE 0 END) AS Q3,
  SUM(CASE WHEN quarter = 4 THEN amount ELSE 0 END) AS Q4,
  SUM(amount) AS 全年
FROM sales
WHERE year = 2024
GROUP BY product
ORDER BY product;

-- PostgreSQL FILTER 简写
SELECT product,
  SUM(amount) FILTER (WHERE quarter=1) AS Q1,
  SUM(amount) FILTER (WHERE quarter=2) AS Q2,
  SUM(amount) FILTER (WHERE quarter=3) AS Q3,
  SUM(amount) FILTER (WHERE quarter=4) AS Q4
FROM sales WHERE year = 2024 GROUP BY product;
```
