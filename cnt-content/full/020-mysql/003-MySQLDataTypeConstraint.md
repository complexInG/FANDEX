---
order: 30
tags:
  - mysql
  - database
difficulty: beginner
title: 'MySQL 数据类型与约束'
module: mysql
category: 'MySQL Basics'
description: 数值、字符串、日期类型及主键、外键、唯一约束。
author: Anonymous
related:
  - mysql/概述与数据库设计
  - mysql/环境搭建
  - mysql/SQL数据定义与高级对象
  - mysql/MyISAM存储引擎
prerequisites: []
updated: '2026-08-01'
---
## 1. 数据类型选择原则 (Selection Principles)

核心目标：

- 正确表达业务含义（语义清晰）
- 保证数据完整性（约束与校验）
- 兼顾性能与存储成本（索引友好、空间可控）
  实践要点：
- 能用更小的类型就不用更大类型（但不要牺牲语义）
- 经常参与过滤/排序/Join 的列优先选择“可索引且稳定”的类型
- 避免把结构化字段塞进一个字符串里（除非确实是原始文本）

## 2. 数值类型 (Numeric)

### 2.1 整数

常用：`TINYINT`、`INT`、`BIGINT`
实践建议：

- 业务自增主键常用 `BIGINT`（预留增长空间）
- 状态枚举常用 `TINYINT`（配合业务层枚举）
- 需要非负时用 `UNSIGNED`

### 2.2 定点与浮点

- 金额优先用 `DECIMAL(p, s)`，避免浮点误差
- 测量数据/近似值可用 `DOUBLE`

## 3. 字符串类型 (String)

### 3.1 `CHAR` vs `VARCHAR`

- `CHAR(n)`：定长，适合长度固定的值（如国家码、短编码），更新更稳定
- `VARCHAR(n)`：变长，适合长度变化较大的值（如昵称、标题）
  实践建议：
- `VARCHAR` 不是越大越好，过大的上限会影响行格式与索引策略
- 经常参与索引的长文本字段慎用 `VARCHAR(1024+)`

### 3.2 `TEXT` 家族

用于长文本（文章内容、描述）。注意：

- `TEXT` 列通常不适合直接做常规索引（需要前缀索引或全文索引）
- `TEXT` 列会影响行存储与读取代价

## 4. 日期与时间 (Date & Time)

常用：`DATE`、`DATETIME`、`TIMESTAMP`

- `DATETIME`：范围大，存储不依赖时区转换（更“客观”）
- `TIMESTAMP`：存储与时区有关（读取/写入可能发生转换），范围较小
  实践建议：
- 业务“发生时间”通常用 `DATETIME`，统一用 UTC 或在应用层明确时区策略
- 保存“仅日期”用 `DATE`，避免在应用层反复截断

## 5. JSON 类型 (JSON)

MySQL 的 `JSON` 适合存放：

- 结构频繁变化的扩展字段
- 不适合拆表但需要一定结构的配置项
  注意：
- JSON 查询需要函数/生成列配合索引，否则易慢
- 不要用 JSON 替代关键业务字段（关键字段应拆列以便约束、索引与统计）

## 6. 字符集与排序规则 (Charset & Collation)

实践建议：

- 统一使用 `utf8mb4`
- 明确排序规则（collation），避免跨表/跨库比较时发生隐式转换

## 7. 约束 (Constraints)

### 7.1 `NOT NULL`

优先用 `NOT NULL` 来表达“必填”。配合默认值要谨慎，确保默认值也符合业务语义。

### 7.2 `DEFAULT`

示例：

```sql
 created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
```

注意：不要用默认值掩盖业务层输入缺失，应区分“未知/未填”与“默认”。

### 7.3 `UNIQUE`

用于业务唯一性约束（如手机号、邮箱、业务单号）。
实践建议：

- 唯一约束应该从业务语义出发，而不是“为了查得快”
- 可组合唯一：例如 `(tenant_id, email)`

### 7.4 `PRIMARY KEY`

通常建议：

- 使用单列自增或雪花 ID 作为主键
- 避免使用可变业务字段（例如手机号）作为主键

### 7.5 `FOREIGN KEY`

MySQL 支持外键，但很多互联网业务会选择在应用层维护约束，原因包括：

- 高并发下跨表约束可能放大锁冲突
- 分库分表/异构存储下外键不可用
  是否使用外键取决于：
- 业务规模与一致性要求
- 团队治理与数据质量策略

## 8. 建表示例 (Example)

```sql
 CREATE TABLE user_account (
  id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  status TINYINT NOT NULL DEFAULT 1,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uk_email (email)
 )
```

---

## 数值类型

**单行写法：定义 BIGINT 自增主键**
`<列名> BIGINT [UNSIGNED] [NOT NULL] [PRIMARY KEY] [AUTO_INCREMENT]`
```sql
-- 定义 BIGINT 无符号自增主键
id BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT;
```

**单行写法：定义 TINYINT 状态枚举**
`<列名> TINYINT [UNSIGNED] [NOT NULL] [DEFAULT <默认值>]`
```sql
-- 定义 TINYINT 状态字段并设置默认值
status TINYINT NOT NULL DEFAULT 1;
```

**单行写法：定义 DECIMAL 金额字段**
`<列名> DECIMAL(<精度>, <小数位数>) [DEFAULT <默认值>]`
```sql
-- 定义金额字段避免浮点误差
balance DECIMAL(10, 2) DEFAULT 0.00;
```

**单行写法：定义 DOUBLE 浮点字段**
`<列名> <FLOAT|DOUBLE> [(<精度>, <小数位数>)]`
```sql
-- 定义测量数据浮点字段
temperature DOUBLE;
```

---

## 字符串类型

**单行写法：定义 CHAR 定长字符串**
`<列名> CHAR(<长度>) [NOT NULL]`
```sql
-- 定义国家码定长字段
country_code CHAR(2) NOT NULL;
```

**单行写法：定义 VARCHAR 变长字符串**
`<列名> VARCHAR(<最大长度>) [NOT NULL]`
```sql
-- 定义用户名变长字段
username VARCHAR(50) NOT NULL;
```

**单行写法：定义 TEXT 长文本**
`<列名> <TINYTEXT|TEXT|MEDIUMTEXT|LONGTEXT>`
```sql
-- 定义文章内容长文本字段
content TEXT;
```

---

## 日期与时间类型

**单行写法：定义 DATE 日期字段**
`<列名> DATE`
```sql
-- 定义仅保存日期的字段
birthday DATE;
```

**单行写法：定义 DATETIME 日期时间字段**
`<列名> DATETIME [NOT NULL] [DEFAULT CURRENT_TIMESTAMP]`
```sql
-- 定义业务发生时间字段
created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;
```

**单行写法：定义 TIMESTAMP 自动更新字段**
`<列名> TIMESTAMP [DEFAULT CURRENT_TIMESTAMP] [ON UPDATE CURRENT_TIMESTAMP]`
```sql
-- 定义更新时间自动维护字段
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
```

---

## JSON 类型

**单行写法：定义 JSON 列**
`<列名> JSON`
```sql
-- 定义 JSON 扩展字段
profile JSON;
```

**换行写法：建表时包含 JSON 列**
`CREATE TABLE <表名> (<列定义>, <JSON 列名> JSON)`
```sql
-- 创建包含 JSON 字段的用户表
CREATE TABLE users (
  id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
  profile JSON
);
```

---

## 字符集与排序规则

**换行写法：创建数据库时指定字符集**
`CREATE DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>`
```sql
-- 创建数据库并指定 utf8mb4 字符集
CREATE DATABASE mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

---

## 约束

**单行写法：非空约束**
`<列名> <类型> NOT NULL`
```sql
-- 定义必填字段
email VARCHAR(255) NOT NULL;
```

**单行写法：默认值约束**
`<列名> <类型> DEFAULT <默认值>`
```sql
-- 定义状态字段默认值为 1
status TINYINT NOT NULL DEFAULT 1;
```

**单行写法：默认值为当前时间**
`<列名> <时间类型> DEFAULT CURRENT_TIMESTAMP`
```sql
-- 定义创建时间默认值为当前时间
created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;
```

**单行写法：单列唯一约束**
`UNIQUE [KEY <索引名>] (<列名>)`
```sql
-- 定义邮箱单列唯一约束
UNIQUE KEY uk_email (email);
```

**单行写法：组合唯一约束**
`UNIQUE [KEY <索引名>] (<列名1>, <列名2>[, ...])`
```sql
-- 定义租户与邮箱组合唯一约束
UNIQUE KEY uk_tenant_email (tenant_id, email);
```

**单行写法：单列主键约束**
`<列名> <类型> PRIMARY KEY`
```sql
-- 定义单列主键
id BIGINT UNSIGNED NOT NULL PRIMARY KEY;
```

**单行写法：复合主键约束**
`PRIMARY KEY (<列名1>, <列名2>[, ...])`
```sql
-- 定义复合主键
PRIMARY KEY (tenant_id, user_id);
```

**换行写法：外键约束**
`FOREIGN KEY (<列名>) REFERENCES <父表>(<父列>) [ON DELETE <行为>] [ON UPDATE <行为>]`
```sql
-- 定义外键关联并设置级联行为
FOREIGN KEY (user_id) REFERENCES users(id)
  ON DELETE RESTRICT
  ON UPDATE CASCADE;
```

**单行写法：检查约束（非负）**
`CHECK (<条件表达式>)`
```sql
-- 定义金额必须非负的检查约束
CHECK (total_amount >= 0);
```

**单行写法：检查约束（枚举值）**
`CHECK (<列名> IN (<值1>, <值2>[, ...]))`
```sql
-- 定义状态值限定检查约束
CHECK (status IN (1, 2, 3, 4, 5));
```

**单行写法：自增约束**
`<列名> <整数类型> AUTO_INCREMENT`
```sql
-- 定义自增主键
id INT PRIMARY KEY AUTO_INCREMENT;
```

---

## 建表示例

**换行写法：完整建表语句**
`CREATE TABLE <表名> (<列定义>[, <约束定义>...])`
```sql
-- 创建用户账户表并包含唯一约束
CREATE TABLE user_account (
  id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  status TINYINT NOT NULL DEFAULT 1,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uk_email (email)
);
```

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
| MySQL 数据类型与约束 | 003-MySQLDataTypeConstraint | 本文自身 |
| SQL 数据定义与高级对象 | 004-SQLDataDefinitionAdvanced | 本文的并列主题 |
| MyISAM存储引擎 | 005-MyISAMStorageEngine | 本文的并列主题 |
| SQL 数据操作与查询 | 006-SQLDataOperationQuery | 本文的并列主题 |
| Memory存储引擎 | 007-MemoryStorageEngine | 本文的并列主题 |
| NDB-Cluster | 008-NDBCluster | 本文的并列主题 |
| 聚簇索引与二级索引 | 009-ClusteredIndexSecondaryIndex | 本文的并列主题 |
| 联合索引与最左前缀原则 | 010-CompositeIndexLeftmostPrefixPrinciple | 本文的并列主题 |
| 索引下推 | 011-IndexConditionPushdown | 本文的并列主题 |
| 全文索引 | 012-FullTextIndex | 本文的并列主题 |
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
