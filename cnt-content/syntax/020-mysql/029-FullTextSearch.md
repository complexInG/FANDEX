# 全文搜索 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 全文索引创建

**基本写法：建表时创建全文索引**
`CREATE TABLE <表名> (... FULLTEXT KEY <索引名>(<列1>[, <列2>...])) [WITH PARSER <解析器>];`

```sql
-- 创建带中文全文索引的文章表（需 ngram 解析器支持中文）
CREATE TABLE articles (
  id BIGINT PRIMARY KEY,
  title VARCHAR(200),
  body TEXT,
  FULLTEXT KEY ft_title_body (title, body) WITH PARSER ngram
) ENGINE = InnoDB;
```

**基本写法：为已有表添加全文索引**
`CREATE FULLTEXT INDEX <索引名> ON <表名>(<列>[, <列>...]) [WITH PARSER <解析器>];`

```sql
-- 为 body 列添加全文索引
CREATE FULLTEXT INDEX ft_body ON articles(body) WITH PARSER ngram;
```

**基本写法：ALTER 添加全文索引**
`ALTER TABLE <表名> ADD FULLTEXT INDEX <索引名>(<列>[, <列>...]) [WITH PARSER <解析器>];`

```sql
-- 通过 ALTER 添加复合全文索引
ALTER TABLE articles
ADD FULLTEXT INDEX ft_title_body (title, body) WITH PARSER ngram;
```

---

## 全文搜索查询

**基本写法：MATCH ... AGAINST 自然语言搜索**
`SELECT ... WHERE MATCH(<列>) AGAINST('<关键词>')`

```sql
-- 自然语言模式搜索（默认）
SELECT id, title, MATCH(title, body) AGAINST('数据库') AS relevance
FROM articles
WHERE MATCH(title, body) AGAINST('数据库')
ORDER BY relevance DESC;
```

**基本写法：布尔模式搜索**
`SELECT ... WHERE MATCH(<列>) AGAINST('<表达式>' IN BOOLEAN MODE)`

```sql
-- 布尔模式：+必须包含，-排除，*通配
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST('+MySQL -Oracle' IN BOOLEAN MODE);
-- 包含任意一个词
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST('MySQL PostgreSQL' IN BOOLEAN MODE);
-- 前缀匹配
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST('data*' IN BOOLEAN MODE);
```

**基本写法：查询扩展模式**
`SELECT ... WHERE MATCH(<列>) AGAINST('<关键词>' WITH QUERY EXPANSION)`

```sql
-- 查询扩展：自动扩展相关词进行二次搜索（召回率高但精度低）
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST('database' WITH QUERY EXPANSION);
```

---

## ngram 中文解析器

**基本写法：ngram 分词配置**
`SET GLOBAL ngram_token_size = <数值>;`

```sql
-- 查看 ngram 分词长度（默认 2，需在配置文件设置）
SHOW VARIABLES LIKE 'ngram_token_size';
```

**基本写法：配置文件设置 ngram**
`ngram_token_size = 2`

```ini
# my.cnf 中设置 ngram 分词长度（重启生效）
[mysqld]
ngram_token_size = 2
```

**基本写法：ngram 布尔搜索中文**
`SELECT ... WHERE MATCH(<列>) AGAINST('<中文词>' IN BOOLEAN MODE)`

```sql
-- ngram 模式下中文搜索（"数据库"会被切分为"数据""据库"）
SELECT id, title FROM articles
WHERE MATCH(title, body) AGAINST('+数据 +据库' IN BOOLEAN MODE);
```

---

## 索引维护

**基本写法：查看全文索引**
`SHOW INDEX FROM <表名> WHERE Index_type = 'FULLTEXT';`

```sql
-- 查看表的全文索引
SHOW INDEX FROM articles WHERE Index_type = 'FULLTEXT';
```

**基本写法：删除全文索引**
`ALTER TABLE <表名> DROP INDEX <索引名>;`

```sql
-- 删除全文索引
ALTER TABLE articles DROP INDEX ft_title_body;
-- 或使用 DROP INDEX
DROP INDEX ft_body ON articles;
```

**基本写法：重建全文索引**
`ALTER TABLE <表名> DROP INDEX <索引名>, ADD FULLTEXT INDEX <索引名>(<列>) WITH PARSER <解析器>;`

```sql
-- 重建全文索引（数据变更后统计信息更新）
ALTER TABLE articles
DROP INDEX ft_body,
ADD FULLTEXT INDEX ft_body (body) WITH PARSER ngram;
```

---

## 布尔模式运算符

**基本写法：运算符速查**
`AGAINST('<+包含> <-排除> <可选> "<短语>" <前缀>*' IN BOOLEAN MODE)`

```sql
-- + 包含该词
MATCH(body) AGAINST('+MySQL' IN BOOLEAN MODE)
-- - 排除该词
MATCH(body) AGAINST('-Oracle' IN BOOLEAN MODE)
-- 无符号：该词可选，相关性更高
MATCH(body) AGAINST('MySQL 性能' IN BOOLEAN MODE)
-- "短语"：完整匹配短语
MATCH(body) AGAINST('"full text search"' IN BOOLEAN MODE)
-- * 前缀通配（必须 3 字符以上）
MATCH(body) AGAINST('opti*' IN BOOLEAN MODE)
-- () 分组
MATCH(body) AGAINST('+MySQL +(优化 调优)' IN BOOLEAN MODE)
-- ~ 词之间距离（接近度）
MATCH(body) AGAINST('MySQL~性能' IN BOOLEAN MODE)
```

**基本写法：相关性排序**
`SELECT MATCH(<列>) AGAINST('<词>') AS <相关度> FROM <表> ORDER BY <相关度> DESC`

```sql
-- 返回相关性分数并排序
SELECT
  id,
  title,
  MATCH(title, body) AGAINST('数据库 优化') AS score
FROM articles
WHERE MATCH(title, body) AGAINST('数据库 优化' IN BOOLEAN MODE)
ORDER BY score DESC
LIMIT 20;
```

---