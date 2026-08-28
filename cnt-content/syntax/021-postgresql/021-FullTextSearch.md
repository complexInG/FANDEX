# 全文搜索 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## tsvector 与 tsquery

**基本写法：创建 tsvector 文档**
`to_tsvector([<配置>,] <文本>)`

```sql
-- 将文本转换为标准化词素（分词、去停用词、词干化）
SELECT to_tsvector('english', 'The quick brown fox jumps');
-- 输出: 'brown':3 'fox':4 'jump':5 'quick':2
-- 中文需 zhparser 扩展
SELECT to_tsvector('chinese', '数据库性能优化');
```

**基本写法：创建 tsquery 查询**
`to_tsquery([<配置>,] <查询表达式>)` / `plainto_tsquery(<文本>)`

```sql
-- to_tsquery 支持运算符 & | ! <->（与/或/非/相邻）
SELECT to_tsquery('english', 'quick & brown');
-- plainto_tsquery 自动处理（不支持运算符，全部 AND）
SELECT plainto_tsquery('english', 'quick brown fox');
-- phraseto_tsquery 短语匹配（词序敏感）
SELECT phraseto_tsquery('english', 'quick brown fox');
-- websearch_to_tsquery 类似搜索引擎语法
SELECT websearch_to_tsquery('english', 'quick OR brown -slow');
```

**基本写法：手动构造 tsvector**
`'<词1>:<位置> <词2>:<位置>'::tsvector`

```sql
-- 手动指定词与位置
SELECT '数据库:1 性能:2 优化:3'::tsvector;
-- 含权重（A 最高，D 默认）
SELECT setweight('数据库:1 性能:2'::tsvector, 'A');
```

---

## 搜索查询

**基本写法：全文匹配**
`WHERE to_tsvector(<列>) @@ to_tsquery(<查询>)`

```sql
-- 使用 @@ 操作符匹配
SELECT id, title
FROM articles
WHERE to_tsvector(title) @@ to_tsquery('database & performance');
```

**基本写法：返回相关性排序**
`ts_rank(<tsvector>, <tsquery>)`

```sql
-- 按相关性分数排序
SELECT id, title,
  ts_rank(to_tsvector(title), to_tsquery('database')) AS rank
FROM articles
WHERE to_tsvector(title) @@ to_tsquery('database')
ORDER BY rank DESC;
-- ts_rank_cd 考虑词距（覆盖密度）
SELECT id, ts_rank_cd(to_tsvector(body), query) FROM articles;
```

**基本写法：高亮显示**
`ts_headline([<配置>,] <原文>, <tsquery> [, <选项>])`

```sql
-- 返回带高亮标记的摘要
SELECT ts_headline('english', body, to_tsquery('database & performance'),
  'StartSel=<b>, StopSel=</b>, MaxWords=35, MinWords=15')
FROM articles
WHERE to_tsvector(body) @@ to_tsquery('database & performance');
```

---

## GIN 索引

**基本写法：创建 GIN 全文索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (to_tsvector(<配置>, <列>));`

```sql
-- 为表达式创建 GIN 索引加速全文搜索
CREATE INDEX idx_articles_body_fts
ON articles USING GIN (to_tsvector('english', body));
```

**基本写法：生成列加速索引**
`<列> tsvector GENERATED ALWAYS AS (to_tsvector(...)) STORED`

```sql
-- 使用生成列避免重复计算
CREATE TABLE articles (
  id SERIAL PRIMARY KEY,
  title TEXT,
  body TEXT,
  body_tsv tsvector GENERATED ALWAYS AS (to_tsvector('english', body)) STORED
);
-- 为生成列建索引
CREATE INDEX idx_articles_body_tsv ON articles USING GIN (body_tsv);
-- 直接查询生成列
SELECT * FROM articles WHERE body_tsv @@ to_tsquery('database');
```

---

## 搜索配置

**基本写法：查看搜索配置**
`SELECT * FROM pg_ts_config;`

```sql
-- 查看可用的文本搜索配置
SELECT cfgname FROM pg_ts_config;
-- 默认配置（通常为 simple 或 english）
SHOW default_text_search_config;
-- 设置默认配置
SET default_text_search_config = 'english';
```

**基本写法：中文搜索配置**
`CREATE TEXT SEARCH CONFIGURATION <配置名> (...)`

```sql
-- 使用 zhparser 扩展配置中文搜索
CREATE EXTENSION IF NOT EXISTS zhparser;
CREATE TEXT SEARCH CONFIGURATION chinese (PARSER = zhparser);
ALTER TEXT SEARCH CONFIGURATION chinese
  ADD MAPPING FOR n,v,a,i,e,l WITH simple;
-- 使用配置
SELECT to_tsvector('chinese', '数据库性能优化');
```

---

## 复合搜索

**基本写法：多列加权搜索**
`setweight(to_tsvector(<列1>), 'A') || setweight(to_tsvector(<列2>), 'B')`

```sql
-- 标题权重 A（最高），正文权重 D（默认）
SELECT id,
  setweight(to_tsvector(title), 'A') ||
  setweight(to_tsvector(body), 'D') AS document
FROM articles;
-- 加权相关性排序（标题匹配分数更高）
SELECT id, title,
  ts_rank(setweight(to_tsvector(title), 'A') ||
          setweight(to_tsvector(body), 'D'),
          to_tsquery('database')) AS rank
FROM articles
WHERE to_tsvector(title) || to_tsvector(body) @@ to_tsquery('database')
ORDER BY rank DESC;
```

**基本写法：词组相邻搜索**
`phraseto_tsquery(<配置>, '<短语>')` 或 `<词1> <-> <词2>`

```sql
-- 精确短语匹配（词序相邻）
SELECT * FROM articles
WHERE to_tsvector(body) @@ phraseto_tsquery('database performance');
-- 指定相邻距离
SELECT * FROM articles
WHERE to_tsvector(body) @@ to_tsquery('database <3> performance');
```

---

## 字典与停用词

**基本写法：查看字典**
`SELECT * FROM pg_ts_dict;`

```sql
-- 查看可用字典
SELECT dictname, dictinit FROM pg_ts_dict;
```

**基本写法：自定义停用词**
`CREATE TEXT SEARCH DICTIONARY <名称> (TEMPLATE = pg_catalog.simple, STOPWORDS = <停用词集>);`

```sql
-- 创建自定义停用词字典
CREATE TEXT SEARCH DICTIONARY my_simple (
  TEMPLATE = pg_catalog.simple,
  STOPWORDS = my_stopwords
);
```

---