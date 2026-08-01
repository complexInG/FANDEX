---
order: 56
title: 全文索引
module: mysql
category: MySQL
difficulty: intermediate
description: 'MySQL全文索引：FULLTEXT索引创建、自然语言模式、布尔模式、n-gram解析器与中文分词'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/联合索引与最左前缀原则
  - mysql/索引下推
  - mysql/前缀索引
  - mysql/索引提示与强制索引
prerequisites:
  - mysql/语法速查
---
## 1. 全文索引概述

MySQL 全文索引（FULLTEXT Index）支持对文本内容进行全文检索，InnoDB 和 MyISAM 均支持。

## 2. 创建全文索引

```sql
-- 创建表时定义
CREATE TABLE articles (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    title   VARCHAR(200),
    content TEXT,
    FULLTEXT INDEX ft_title_content (title, content)
) ENGINE = InnoDB;

-- 在已有表上创建
ALTER TABLE articles ADD FULLTEXT INDEX ft_content (content);

-- 使用 n-gram 解析器（支持中文）
ALTER TABLE articles ADD FULLTEXT INDEX ft_content (content)
    WITH PARSER ngram;
```

## 3. 搜索模式

### 3.1 自然语言模式

```sql
-- 默认模式，按相关性排序
SELECT * FROM articles
WHERE MATCH(title, content) AGAINST('数据库 索引');

-- 获取相关性分数
SELECT *, MATCH(title, content) AGAINST('数据库 索引') AS score
FROM articles
WHERE MATCH(title, content) AGAINST('数据库 索引')
ORDER BY score DESC;
```

### 3.2 布尔模式

```sql
-- 支持操作符
SELECT * FROM articles
WHERE MATCH(title, content) AGAINST('+MySQL -索引' IN BOOLEAN MODE);

-- 操作符说明：
-- +  必须包含
-- -  必须不包含
-- 无  可选，包含则提高相关性
-- >  提高权重
-- <  降低权重
-- *  通配符（前缀匹配）
-- "  短语匹配
-- () 分组
-- ~  取反（降低相关性）

-- 短语匹配
SELECT * FROM articles
WHERE MATCH(content) AGAINST('"MySQL索引优化"' IN BOOLEAN MODE);

-- 前缀匹配
SELECT * FROM articles
WHERE MATCH(content) AGAINST('数据*' IN BOOLEAN MODE);
```

### 3.3 查询扩展模式

```sql
-- 两阶段搜索：先搜关键词，再用结果中的词扩展搜索
SELECT * FROM articles
WHERE MATCH(content) AGAINST('数据库' WITH QUERY EXPANSION);
```

## 4. n-gram 解析器

```sql
-- 中文分词支持
-- ngram_token_size = 2（默认，双字分词）

CREATE TABLE chinese_articles (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    title   VARCHAR(200),
    content TEXT,
    FULLTEXT INDEX ft_content (content) WITH PARSER ngram
) ENGINE = InnoDB;

-- 搜索中文
SELECT * FROM chinese_articles
WHERE MATCH(content) AGAINST('数据库' IN NATURAL LANGUAGE MODE);
```

## 5. 限制与注意事项

```sql
-- 最小词长度：innodb_ft_min_token_size = 3（默认）
-- ngram 时由 ngram_token_size 决定

-- 全文索引不支持前缀索引
-- 全文索引列不支持排序
-- 全文索引不支持 % 通配符
-- 建议在数据导入完成后再创建全文索引
```
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

## 参考文献

MySQL 官方文档：https://dev.mysql.com/doc/
MySQL 8.0 参考手册：https://dev.mysql.com/doc/refman/8.0/en/
High Performance MySQL（O'Reilly）：https://www.oreilly.com/library/view/high-performance-mysql/
Percona 博客：https://www.percona.com/blog/

## 延伸阅读

MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 高级课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 InnoDB 日志与崩溃恢复

redo log 记录物理页修改（WAL：先写日志再写数据页），崩溃后重放恢复；环形文件组 + checkpoint 推进。
undo log 记录事务前镜像，支持回滚与 MVCC 版本链；purge 线程清理。
两阶段提交：redo prepare -> binlog -> redo commit，保证两份日志一致，主从不丢数据。
刷盘策略：innodb_flush_log_at_trx_commit=1 最安全（每次提交 fsync），2 每秒刷。

### 13.2 执行计划与优化器

EXPLAIN 关键列：type（const/ref/range/index/ALL）、key、rows、Extra（Using index/Using filesort）。
优化器基于统计信息选计划；analyze table 更新统计；hint（FORCE INDEX）谨慎使用。
排序与分组：filesort 优化为索引序；避免临时表。
慢查询治理流程：慢日志 -> 计划分析 -> 索引/改写 -> 验证。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| MySQL 概述与数据库设计 | 001-MySQLOverviewDatabaseDesign | 本文的前置基础 |
| MySQL 环境搭建 | 002-MySQLEnvSetup | 本文的前置基础 |
| MySQL 数据类型与约束 | 003-MySQLDataTypeConstraint | 本文的并列主题 |
| SQL 数据定义与高级对象 | 004-SQLDataDefinitionAdvanced | 本文的并列主题 |
| MyISAM存储引擎 | 005-MyISAMStorageEngine | 本文的并列主题 |
| SQL 数据操作与查询 | 006-SQLDataOperationQuery | 本文的并列主题 |
| Memory存储引擎 | 007-MemoryStorageEngine | 本文的并列主题 |
| NDB-Cluster | 008-NDBCluster | 本文的并列主题 |
| 聚簇索引与二级索引 | 009-ClusteredIndexSecondaryIndex | 本文的并列主题 |
| 联合索引与最左前缀原则 | 010-CompositeIndexLeftmostPrefixPrinciple | 本文的并列主题 |
| 索引下推 | 011-IndexConditionPushdown | 本文的并列主题 |
| 全文索引 | 012-FullTextIndex | 本文自身 |
| 前缀索引 | 013-PrefixIndex | 本文的并列主题 |
| 索引提示与强制索引 | 014-IndexHintForceIndex | 本文的并列主题 |
| 索引统计信息与直方图 | 015-IndexStatsHistogram | 本文的并列主题 |
| SQL 函数与高级查询 | 016-SQLFunctionAndAdvancedQuery | 本文的并列主题 |
| 索引失效场景 | 017-IndexFailureScene | 本文的并列主题 |
| EXPLAIN输出详解 | 018-EXPLAINDetailed | 本文的并列主题 |
| 慢查询日志 | 019-SlowQueryLog | 本文的并列主题 |
| 优化器追踪 | 020-OptimizerTrace | 本文的性能延伸 |
| 子查询优化 | 021-SubqueryOptimization | 本文的性能延伸 |
| 派生表优化 | 022-DerivedTableOptimization | 本文的性能延伸 |
| GROUP-BY与ORDER-BY优化 | 023-GroupByOrderByOptimization | 本文的性能延伸 |
| JOIN算法 | 024-JOINAlgorithm | 本文的并列主题 |
| 事务隔离级别底层实现 | 025-TransactionIsolationImplementation | 本文的并列主题 |
| MVCC原理 | 026-MVCCPrinciple | 本文的原理深化 |
| 多表联查详解 | 027-MultiTableJoinDetailed | 本文的并列主题 |
| 锁分类 | 028-LockClassification | 本文的并列主题 |
| 死锁检测与处理 | 029-DeadlockDetectionHandling | 本文的并列主题 |
| 分布式事务 | 030-DistributedTransaction | 本文的并列主题 |
| 二进制日志 | 031-Binlog | 本文的并列主题 |
| 重做日志 | 032-RedoLog | 本文的并列主题 |
| 撤销日志 | 033-UndoLog | 本文的并列主题 |
| 日志系统 | 034-LogSystem | 本文的并列主题 |
| 逻辑备份 | 035-LogicalBackup | 本文的并列主题 |
| 物理备份 | 036-PhysicalBackup | 本文的并列主题 |
| 基于时间点恢复 | 037-PITR | 本文的并列主题 |
| 主从复制 | 038-Replication | 本文的并列主题 |
| 进阶查询与多表操作 | 039-AdvancedQueryMultiTableOperation | 本文的并列主题 |
| GTID | 040-GTID | 本文的并列主题 |
| 并行复制 | 041-ParallelReplication | 本文的并列主题 |
| 组复制 | 042-GroupReplication | 本文的并列主题 |
| InnoDB-Cluster | 043-InnoDBCluster | 本文的并列主题 |
| 分区表 | 044-PartitionedTable | 本文的并列主题 |
| 分库分表中间件 | 045-ShardingMiddleware | 本文的并列主题 |
| 账户与权限管理 | 046-AccountPermissionManagement | 本文的安全延伸 |
| SSL-TLS加密 | 047-SSLEncryption | 本文的安全延伸 |
| 防火墙插件 | 048-FirewallPlugin | 本文的并列主题 |
| InnoDB体系架构 | 049-InnoDBSystemArchitecture | 本文的原理深化 |
| 数据加密 | 050-DataEncryption | 本文的安全延伸 |
| MySQL 索引与执行计划 | 051-MySQLIndexExecutionPlan | 本文的并列主题 |
| MySQL9新特性与并行查询 | 052-MySQL9NewFeaturesParallelQuery | 本文的并列主题 |
| VECTOR向量类型 | 053-VectorType | 本文的并列主题 |
| JSON模式验证与聚合函数 | 054-JSONSchemaValidationAggregate | 本文的并列主题 |
| 复制与高可用 | 055-ReplicationHA | 本文的并列主题 |
| 不可见索引 | 056-InvisibleIndex | 本文的并列主题 |
| 性能调优与安全 | 057-PerformanceTuningSecurity | 本文的性能延伸 |
| 函数索引 | 058-FunctionalIndex | 本文的并列主题 |
| 存储过程与函数 | 059-StoredProcedureAndFunction | 本文的并列主题 |
| MVCC快照读与当前读 | 060-MVCCSnapshotCurrentRead | 本文的并列主题 |
| 索引原理与性能优化 | 061-IndexPrinciplePerformanceOptimization | 本文的性能延伸 |
| 触发器与事件 | 062-TriggerEvent | 本文的并列主题 |
| Redo与Undo与Binlog写入时机 | 063-RedoUndoBinlogWriteTiming | 本文的并列主题 |
| 两阶段提交 | 064-TwoPhaseCommit | 本文的并列主题 |
| 间隙锁与临键锁解决幻读 | 065-GapLockNextKeyLockSolutionPhantomRead | 本文的并列主题 |
| 主从复制延迟原因与解决 | 066-ReplicationDelayCauseSolution | 本文的并列主题 |
| 分库分表策略 | 067-ShardingStrategy | 本文的并列主题 |
| JSON类型与JSON-TABLE | 068-JSONTypeJSONTable | 本文的并列主题 |
| 事务与锁机制 | 069-TransactionLockMechanism | 本文的原理深化 |
| MySQL 配置与运维 | 070-MySQLConfigOps | 本文的并列主题 |
| MySQL 快速查阅 | 071-MySQLQuickLookup | 本文的并列主题 |
| MySQL 控制器与应用 | 072-MySQLControlApplication | 本文的并列主题 |
| SQL 注入基础与检测 | 073-SQLInjectionBasicsDetection | 本文的前置基础 |
| SQL 注入攻击类型与实战 | 074-SQLInjectionAttackTypePractice | 本文的综合应用 |
| SQL 注入防御策略 | 075-SQLInjectionDefenseStrategy | 本文的并列主题 |
| MySQL 项目示例：电商数据库设计 | 076-MySQLProjectExampleDatabaseDesign | 本文的综合应用 |
| MySQL 理论知识点 | 077-MySQLTheoryKnowledge | 本文的并列主题 |
| MySQL DDL 数据定义 | 078-DDL | 本文的并列主题 |
| MySQL DML 数据操作 | 079-DML | 本文的并列主题 |
| MySQL DQL 查询速查 | 080-DQL | 本文的并列主题 |
| MySQL 索引管理 | 081-IndexManagement | 本文的并列主题 |
| MySQL 用户与权限管理 | 082-UserPermission | 本文的安全延伸 |
| MySQL CLI 命令 | 083-CLI | 本文的并列主题 |
| mysqladmin 管理命令 语法速查手册 | 084-Mysqladmin | 本文的并列主题 |
| 视图 语法速查手册 | 085-View | 本文的并列主题 |
| 事件调度器 语法速查手册 | 086-EventScheduler | 本文的并列主题 |
| 字符集与排序规则 语法速查手册 | 087-CharsetCollation | 本文的并列主题 |
