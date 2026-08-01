---
order: 93
title: 性能调优与安全
module: mysql
category: MySQL
difficulty: advanced
description: MySQL性能调优：缓冲池配置、慢查询分析、performance_schema、安全认证、角色管理、在线DDL与XA事务
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/复制与高可用
  - mysql/不可见索引
  - mysql/函数索引
  - mysql/存储过程与函数
prerequisites:
  - mysql/语法速查
---

## 1. 学习目标（Bloom 分类）

本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《性能调优与安全》，属于 MySQL 模块，读者可以根据自身阶段选择阅读深度。

记忆层面：能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。能够说出 MySQL 的核心概念、语法与常用对象。

理解层面：能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。能够解释 MySQL 的执行原理与优化机制。

应用层面：能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。能够编写正确、高效的 MySQL 语句与操作。

分析层面：能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。能够分析 MySQL 相关方案在性能与一致性上的权衡。

评价层面：能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。能够根据业务场景评价 MySQL 技术选型。

创造层面：能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。能够组合 MySQL 与其他技术设计数据架构。

通过本节学习，读者应当能够把《性能调优与安全》纳入自己的知识网络，并与 MySQL 模块的其他主题（InnoDB、索引、日志、主从、性能调优）建立关联。

## 2. 历史动机与发展脉络

《性能调优与安全》是 MySQL 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。

MySQL 于 1995 年由 MySQL AB 发布，2008 年被 Sun 收购，2010 年随 Sun 并入 Oracle；MariaDB 是社区分支。
MySQL 8.0（2018）重写优化器、引入窗口函数与 CTE、默认 utf8mb4、数据字典升级；MySQL 8.4 与 9.x 继续演进（Oracle 创新版 + LTS 双轨）。
InnoDB 是默认存储引擎：事务、行锁、MVCC、崩溃恢复（redo/undo）；MyISAM 仅存于历史场景。

回到本文主题：性能调优与安全 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。


## 3. 形式化定义与核心概念精讲

本节把《性能调优与安全》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。

InnoDB 架构：缓冲池（Buffer Pool）、日志缓冲、redo/undo 日志；脏页刷盘与 checkpoint 机制。
索引：B+ 树主键聚集索引、二级索引、覆盖索引；索引下推（ICP）与 MRR 优化。
事务与锁：两阶段锁、间隙锁/临键锁（可重复读防幻读）、MVCC 快照读；隔离级别。

### 3.1 原文章节逐一精讲

原文档把主题拆分为 18 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。

#### 原文精读（完整保留）

# 性能分析 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

#### 1. 缓冲池配置与优化

##### 1.1 Buffer Pool 大小规划

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

##### 1.2 Buffer Pool 预热与转储

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

##### 1.3 Buffer Pool 命中率监控

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

#### 2. 日志文件与刷新策略

##### 2.1 Redo Log 配置

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

##### 2.2 刷盘策略

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

#### 3. 慢查询日志分析

##### 3.1 慢查询日志配置

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

##### 3.2 mysqldumpslow 分析工具

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

##### 3.3 慢查询优化案例

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

#### 4. Performance Schema

##### 4.1 启用与配置

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

##### 4.2 语句分析

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

##### 4.3 等待事件分析

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

#### 5. Sys Schema

##### 5.1 Sys Schema 概述

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

##### 5.2 常用 Sys Schema 视图

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

#### 6. 索引优化提示

##### 6.1 USE INDEX / FORCE INDEX / IGNORE INDEX

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

##### 6.2 优化器开关

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

#### 7. 安全机制

##### 7.1 caching_sha2_password 认证

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

##### 7.2 角色管理

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

##### 7.3 密码策略与过期

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

##### 7.4 账户锁

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

##### 7.5 SSL 加密连接

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

##### 7.6 防火墙插件

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

#### 8. 在线 DDL

##### 8.1 在线 DDL 算法

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

##### 8.2 INSTANT DDL 支持的操作

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

#### 9. 生成列与降序索引

##### 9.1 生成列 (Generated Column)

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

##### 9.2 降序索引

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

#### 10. 原子 DDL

##### 10.1 原子 DDL 特性

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

#### 11. XA 分布式事务

##### 11.1 XA 事务基础

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

##### 11.2 跨库 XA 事务

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

##### 11.3 XA 事务恢复

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

##### 11.4 XA 事务注意事项

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

#### 12. 综合调优检查清单

##### 12.1 服务器级别调优

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

##### 12.2 查询级别调优

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
#### EXPLAIN 执行计划

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

#### EXPLAIN 关键列

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

#### SHOW PROFILE

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

#### 慢查询日志

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

#### Performance Schema

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

#### 优化器追踪

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

---

### 3.2 概念关系图

下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：

```mermaid
flowchart LR
    A["性能调优与安全"] --> B["核心概念"]
    B --> C["原理机制"]
    B --> D["代码实践"]
    C --> E["工程应用"]
    D --> E
```

图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。

## 4. 理论推导与原理解析

本节深入《性能调优与安全》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。

InnoDB 架构：缓冲池（Buffer Pool）、日志缓冲、redo/undo 日志；脏页刷盘与 checkpoint 机制。
索引：B+ 树主键聚集索引、二级索引、覆盖索引；索引下推（ICP）与 MRR 优化。
事务与锁：两阶段锁、间隙锁/临键锁（可重复读防幻读）、MVCC 快照读；隔离级别。
复制：binlog 逻辑复制（statement/row/mixed），主从异步、半同步与组复制。

需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。

## 5. 代码示例与逐行讲解

本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。

### 5.1 示例：1.1 Buffer Pool 大小规划

该示例来自原文《1.1 Buffer Pool 大小规划》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.2 示例：1.2 Buffer Pool 预热与转储

该示例来自原文《1.2 Buffer Pool 预热与转储》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.3 示例：1.3 Buffer Pool 命中率监控

该示例来自原文《1.3 Buffer Pool 命中率监控》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 21 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.4 示例：2.1 Redo Log 配置

该示例来自原文《2.1 Redo Log 配置》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，包含 1 类关键结构（ALTER）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.5 示例：2.2 刷盘策略

该示例来自原文《2.2 刷盘策略》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.6 示例：3.1 慢查询日志配置

该示例来自原文《3.1 慢查询日志配置》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.7 示例：3.2 mysqldumpslow 分析工具

该示例来自原文《3.2 mysqldumpslow 分析工具》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 15 行有效代码，包含 1 类关键结构（SELECT）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.8 示例：3.3 慢查询优化案例

该示例来自原文《3.3 慢查询优化案例》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 23 行有效代码，包含 3 类关键结构（SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.9 示例：4.1 启用与配置

该示例来自原文《4.1 启用与配置》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.10 示例：4.2 语句分析

该示例来自原文《4.2 语句分析》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 22 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.11 示例：4.3 等待事件分析

该示例来自原文《4.3 等待事件分析》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 20 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.12 示例：5.1 Sys Schema 概述

该示例来自原文《5.1 Sys Schema 概述》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.13 示例：5.2 常用 Sys Schema 视图

该示例来自原文《5.2 常用 Sys Schema 视图》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 20 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.14 示例：6.1 USE INDEX / FORCE INDEX / IGNORE INDEX

该示例来自原文《6.1 USE INDEX / FORCE INDEX / IGNORE INDEX》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.15 示例：6.2 优化器开关

该示例来自原文《6.2 优化器开关》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.16 示例：7.1 caching_sha2_password 认证

该示例来自原文《7.1 caching_sha2_password 认证》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 4 类关键结构（SELECT、CREATE、ALTER、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.17 示例：7.2 角色管理

该示例来自原文《7.2 角色管理》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 25 行有效代码，包含 5 类关键结构（SELECT、INSERT、CREATE、ALTER、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.18 示例：7.3 密码策略与过期

该示例来自原文《7.3 密码策略与过期》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 19 行有效代码，包含 2 类关键结构（CREATE、ALTER）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.19 示例：7.4 账户锁

该示例来自原文《7.4 账户锁》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 15 行有效代码，包含 4 类关键结构（SELECT、CREATE、ALTER、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.20 示例：7.5 SSL 加密连接

该示例来自原文《7.5 SSL 加密连接》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 17 行有效代码，包含 4 类关键结构（SELECT、CREATE、ALTER、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.21 示例：7.6 防火墙插件

该示例来自原文《7.6 防火墙插件》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 15 行有效代码，包含 3 类关键结构（SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.22 示例：8.1 在线 DDL 算法

该示例来自原文《8.1 在线 DDL 算法》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，包含 1 类关键结构（ALTER）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.23 示例：8.2 INSTANT DDL 支持的操作

该示例来自原文《8.2 INSTANT DDL 支持的操作》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 18 行有效代码，包含 3 类关键结构（SELECT、ALTER、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.24 示例：9.1 生成列 (Generated Column)

该示例来自原文《9.1 生成列 (Generated Column)》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 27 行有效代码，包含 3 类关键结构（SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.25 示例：9.2 降序索引

该示例来自原文《9.2 降序索引》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 27 行有效代码，包含 3 类关键结构（SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.26 示例：10.1 原子 DDL 特性

该示例来自原文《10.1 原子 DDL 特性》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 17 行有效代码，包含 4 类关键结构（SELECT、CREATE、ALTER、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.27 示例：11.1 XA 事务基础

该示例来自原文《11.1 XA 事务基础》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.28 示例：11.2 跨库 XA 事务

该示例来自原文《11.2 跨库 XA 事务》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 17 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.29 示例：11.3 XA 事务恢复

该示例来自原文《11.3 XA 事务恢复》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 15 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.30 示例：11.4 XA 事务注意事项

该示例来自原文《11.4 XA 事务注意事项》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.31 示例：12.1 服务器级别调优

该示例来自原文《12.1 服务器级别调优》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 18 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.32 示例：12.2 查询级别调优

该示例来自原文《12.2 查询级别调优》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 16 行有效代码，包含 3 类关键结构（SELECT、ALTER、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.33 示例：EXPLAIN 执行计划

该示例来自原文《EXPLAIN 执行计划》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查看查询执行计划
EXPLAIN SELECT * FROM users WHERE age > 18;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.34 示例：EXPLAIN 执行计划

该示例来自原文《EXPLAIN 执行计划》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- MySQL 8.0+ 树形输出，显示 join 顺序与成本
EXPLAIN FORMAT=TREE
SELECT u.user_name, o.amount
FROM users u JOIN orders o ON u.id = o.user_id;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.35 示例：EXPLAIN 执行计划

该示例来自原文《EXPLAIN 执行计划》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- MySQL 8.0.18+ 实际执行并统计耗时（注意会真实执行 DML）
EXPLAIN ANALYZE
SELECT COUNT(*) FROM orders WHERE create_time > '2024-01-01';
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.36 示例：EXPLAIN 执行计划

该示例来自原文《EXPLAIN 执行计划》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查看 INSERT/UPDATE/DELETE 执行计划
EXPLAIN UPDATE users SET status = 0 WHERE last_login < NOW() - INTERVAL 90 DAY;
EXPLAIN DELETE FROM logs WHERE created_at < '2023-01-01';
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，包含 2 类关键结构（INSERT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.37 示例：EXPLAIN 关键列

该示例来自原文《EXPLAIN 关键列》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- type 取值从优到差：system > const > eq_ref > ref > range > index > ALL
-- const: 主键或唯一索引等值查询
EXPLAIN SELECT * FROM users WHERE id = 100;
-- range: 索引范围扫描
EXPLAIN SELECT * FROM orders WHERE id BETWEEN 1 AND 100;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.38 示例：EXPLAIN 关键列

该示例来自原文《EXPLAIN 关键列》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- Using index: 覆盖索引，无需回表（最优）
EXPLAIN SELECT id, name FROM users WHERE name = '张三';
-- Using filesort: 额外排序（需优化）
EXPLAIN SELECT * FROM users ORDER BY age;
-- Using temporary: 使用临时表（需优化）
EXPLAIN SELECT DISTINCT dept FROM users;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.39 示例：SHOW PROFILE

该示例来自原文《SHOW PROFILE》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 启用查询性能分析
SET profiling = 1;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.40 示例：SHOW PROFILE

该示例来自原文《SHOW PROFILE》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查看最近执行的查询及 Query_ID
SHOW PROFILES;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.41 示例：SHOW PROFILE

该示例来自原文《SHOW PROFILE》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查看指定查询各阶段耗时
SHOW PROFILE CPU FOR QUERY 1;
-- 查看所有资源使用
SHOW PROFILE ALL FOR QUERY 1;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.42 示例：慢查询日志

该示例来自原文《慢查询日志》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查看慢查询日志开关与路径
SHOW VARIABLES LIKE 'slow_query_log%';
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.43 示例：慢查询日志

该示例来自原文《慢查询日志》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 临时开启慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- 超过 1 秒记录
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.44 示例：慢查询日志

该示例来自原文《慢查询日志》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```ini
# my.cnf 持久配置
[mysqld]
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 1
log_queries_not_using_indexes = 1
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.45 示例：慢查询日志

该示例来自原文《慢查询日志》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```bash
# 按总耗时排序取前 10 条
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log
# 按次数排序
mysqldumpslow -s c -t 10 /var/log/mysql/slow.log
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.46 示例：Performance Schema

该示例来自原文《Performance Schema》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查看可用的性能采集器
SELECT name, enabled, timed
FROM performance_schema.setup_instruments
WHERE name LIKE 'statement/%';
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.47 示例：Performance Schema

该示例来自原文《Performance Schema》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 启用语句采集
UPDATE performance_schema.setup_instruments
SET enabled = 'YES', timed = 'YES'
WHERE name LIKE 'statement/%';
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.48 示例：Performance Schema

该示例来自原文《Performance Schema》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查看执行最频繁的 SQL 模式
SELECT digest_text, count_star, avg_timer_wait/1000000000 AS avg_ms
FROM performance_schema.events_statements_summary_by_digest
ORDER BY count_star DESC LIMIT 10;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.49 示例：Performance Schema

该示例来自原文《Performance Schema》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查看最耗时的等待事件
SELECT event_name, count_star, sum_timer_wait/1000000000 AS sum_ms
FROM performance_schema.events_waits_summary_global_by_event_name
ORDER BY sum_timer_wait DESC LIMIT 10;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.50 示例：优化器追踪

该示例来自原文《优化器追踪》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 启用优化器追踪
SET optimizer_trace = 'enabled=on';
SET optimizer_trace_max_mem_size = 65536;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.51 示例：优化器追踪

该示例来自原文《优化器追踪》小节，用于演示性能调优与安全相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 执行查询后查看优化器决策过程
SELECT id FROM users WHERE email = 'test@example.com';
SELECT trace FROM information_schema.OPTIMIZER_TRACE\G
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。


综合以上示例，可以总结出本主题的代码实践要点：第一，先定义清晰的输入输出契约；第二，核心逻辑保持单一职责；第三，错误处理与边界条件不可省略；第四，命名与注释表达意图而非复述代码。

## 6. 对比分析

对比是理解《性能调优与安全》定位的最快路径。下面从多个维度与相邻方案进行对比。

MySQL 与 PostgreSQL：MySQL 简单易用、复制生态成熟；PostgreSQL 功能与扩展更强。
InnoDB 与 MyISAM：事务/行锁/崩溃恢复 vs 表锁/压缩；新表一律 InnoDB。
异步复制与组复制：异步简单、组复制强一致；按可用性需求选择。

对比的目的不是分出绝对优劣，而是建立选择依据：不同约束条件下，最优解不同。读者应把每个对比维度转化为决策检查清单。

## 7. 常见陷阱与最佳实践

本节整理该主题的高频错误与推荐做法。每个陷阱先描述现象，再解释原因，最后给出最佳实践。

### 7.1 最大连接数耗尽

连接池过小或慢查询占连接。调大连接池与优化 SQL。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，最大连接数耗尽 一般源于对 MySQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，最大连接数耗尽 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理最大连接数耗尽的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.2 索引失效

隐式转换、函数包裹、LIKE 前导通配。检查执行计划。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，索引失效 一般源于对 MySQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，索引失效 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理索引失效的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.3 大表 DDL 锁表

8.0 的 INSTANT/INPLACE 减少锁；仍评估窗口。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，大表 DDL 锁表 一般源于对 MySQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，大表 DDL 锁表 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理大表 DDL 锁表的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.4 缓冲池过小

命中率低全盘 IO。调 innodb_buffer_pool_size（约内存 60-70%）。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，缓冲池过小 一般源于对 MySQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，缓冲池过小 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理缓冲池过小的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.5 隐式提交

DDL 隐式提交事务。事务内避免 DDL。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，隐式提交 一般源于对 MySQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，隐式提交 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理隐式提交的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.6 utf8 与 utf8mb4

utf8 非完整 UTF-8，emoji 报错。统一 utf8mb4。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，utf8 与 utf8mb4 一般源于对 MySQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，utf8 与 utf8mb4 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理utf8 与 utf8mb4的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.7 主从延迟

大事务与长查询放大延迟。拆事务、并行复制。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，主从延迟 一般源于对 MySQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，主从延迟 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理主从延迟的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.8 备份缺失

无备份无法恢复。binlog + 定期全备并演练恢复。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，备份缺失 一般源于对 MySQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，备份缺失 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理备份缺失的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.0 最佳实践总览

1. 表与字段：主键自增或有序 UUID；金额 decimal；时间戳统一。
2. 索引：高频查询建覆盖索引；写密集控制索引数量。
3. 配置：字符集 utf8mb4、排序规则 utf8mb4_0900_ai_ci（8.0）。
4. 安全：最小权限账号、SSL 连接、敏感字段加密。

把这些最佳实践固化为团队规范与代码评审检查项，是避免同类问题反复出现的关键。

## 8. 工程实践

本节把《性能调优与安全》放入真实工程场景，给出可复用的模式与组织方法。

架构：主从读写分离、分库分表（ShardingSphere）、Proxy（ProxySQL）；容量规划。
运维：Percona Toolkit 巡检、慢日志分析（pt-query-digest）、备份（Xtrabackup）。
监控：QPS、连接、复制延迟、InnoDB 状态（SHOW ENGINE INNODB STATUS）。

### 8.1 工程实践的原则拆解

以上工程实践可以归纳为四条原则。第一，配置与代码分离：MySQL 项目中环境差异应通过配置注入，而不是散落在代码分支中；这保证同一份代码可以在开发、测试、生产环境一致运行。

第二，接口稳定优先：对外接口（函数签名、协议、数据格式）一旦被消费方依赖，变更成本极高；设计时应预留扩展点并保持向后兼容。

第三，可观测性内置：日志、指标与追踪应该在功能开发时同步设计，而不是故障发生后补救；没有观测手段的模块等于黑盒。

第四，变更可回滚：任何发布都应有对应的回滚方案；数据库迁移、配置变更与代码发布一样需要版本管理与逆向路径。

### 8.2 实践落地的检查清单

- [ ] 架构：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 运维：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 监控：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。

工程实践的共性原则：配置与代码分离、接口稳定优先、可观测性内置、变更可回滚。这些原则适用于本主题的所有实现。

## 9. 案例研究

本节通过一个完整案例把《性能调优与安全》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。

需求：电商订单库优化：订单查询从 2 秒降到 50ms。
方案：复合索引（user_id, status, created_at）、覆盖查询列、分页键集化。
要点：EXPLAIN 前后对比；慢日志验证；避免 SELECT *。
验证：压测 P95 延迟、索引使用率、无全表扫描。

### 9.1 案例的扩展讨论

把案例中的方案放大到真实规模，需要额外考虑三个问题：

第一，规模：当数据量或并发量上升一个数量级时，原方案中的数据结构、缓存策略与任务调度是否仍然成立？通常需要引入分层与异步。

第二，团队：多人协作时，模块边界、接口契约与代码所有权必须明确；案例中的实现应拆分为可独立测试的单元，并配合文档说明设计意图。

第三，演进：上线后的需求变化不可避免；方案设计时应预留扩展点（配置化、插件化、事件化），并定期用真实指标验证假设。


案例研究的学习方法：先独立阅读需求，尝试在脑中形成方案，再对照实现与讲解，最后思考“如果约束变化（数据量、并发、团队规模），方案应如何调整”。

## 10. 知识要点总结与深入讲解

本节以讲解形式汇总全文要点，替代传统的习题与自测，读者不需要答题，只需跟随解释建立完整的认知框架。

关于《性能调优与安全》的核心结论：

MySQL 的性能核心是 InnoDB 的缓冲池与索引设计。
日志（redo/undo/binlog）理解是故障恢复与复制的基础。
工程化：字符集、连接池、备份、监控四件套。

原文档各小节的要点回顾：

- 1. 缓冲池配置与优化：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 2. 日志文件与刷新策略：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 3. 慢查询日志分析：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 4. Performance Schema：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 5. Sys Schema：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 6. 索引优化提示：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 7. 安全机制：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 8. 在线 DDL：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 9. 生成列与降序索引：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 10. 原子 DDL：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 11. XA 分布式事务：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 12. 综合调优检查清单：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- EXPLAIN 执行计划：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- EXPLAIN 关键列：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- SHOW PROFILE：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 慢查询日志：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- Performance Schema：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 优化器追踪：该小节围绕性能调优与安全展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。

把以上要点与第 3-9 节的内容对照复习，即可完成对本文主题的闭环学习。

## 11. 参考文献


MySQL 官方文档：https://dev.mysql.com/doc/
MySQL 8.0 参考手册：https://dev.mysql.com/doc/refman/8.0/en/
High Performance MySQL（O'Reilly）：https://www.oreilly.com/library/view/high-performance-mysql/
Percona 博客：https://www.percona.com/blog/

## 12. 延伸阅读


MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 高级课程。

## 14. 模块知识图谱与学习路径

本文属于 MySQL 模块。为了把《性能调优与安全》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。

```mermaid
flowchart LR
    A["性能调优与安全"]
    N0["MySQL 概述与数据库设计"]
    N1["MySQL 环境搭建"]
    N0 --> N1
    N2["MySQL 数据类型与约束"]
    N1 --> N2
    N3["SQL 数据定义与高级对象"]
    N2 --> N3
    N4["MyISAM存储引擎"]
    N3 --> N4
    N5["SQL 数据操作与查询"]
    N4 --> N5
    N6["Memory存储引擎"]
    N5 --> N6
    N7["NDB-Cluster"]
    N6 --> N7
    N8["聚簇索引与二级索引"]
    N7 --> N8
    N9["联合索引与最左前缀原则"]
    N8 --> N9
    N10["索引下推"]
    N9 --> N10
    N11["全文索引"]
    N10 --> N11
    N12["前缀索引"]
    N11 --> N12
    N13["索引提示与强制索引"]
    N12 --> N13
```

上图为模块主题的推荐学习顺序示意图（仅展示前若干主题）。各主题之间存在三类关联：

第一，前置依赖关系：早期主题是后期主题的基础，例如环境与语法先行、进阶主题随后；

第二，横向并列关系：同一层级主题从不同角度覆盖模块能力，学习顺序可以按兴趣调整；

第三，工程组合关系：多个主题在真实项目中组合使用，例如配置、性能与安全主题往往出现在同一系统的不同层面。

### 14.1 模块主题速查表

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
| 性能调优与安全 | 057-PerformanceTuningSecurity | 本文自身 |
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

速查表的作用是让读者快速判断：哪些文档应在阅读本文前掌握（前置基础），哪些文档应在阅读本文后继续（延伸主题）。本模块的交叉引用体系即以此表为基础。

## 15. 术语表

下表整理《性能调优与安全》及 MySQL 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。

| 术语 | 释义 |
| --- | --- |
| InnoDB 架构 | 缓冲池（Buffer Pool）、日志缓冲、redo/undo 日志；脏页刷盘与 checkpoint 机制。 |
| 索引 | B+ 树主键聚集索引、二级索引、覆盖索引；索引下推（ICP）与 MRR 优化。 |
| 事务与锁 | 两阶段锁、间隙锁/临键锁（可重复读防幻读）、MVCC 快照读；隔离级别。 |
| 复制 | binlog 逻辑复制（statement/row/mixed），主从异步、半同步与组复制。 |
| 最大连接数耗尽（易错点） | 参见常见陷阱章节的详细讲解 |
| 索引失效（易错点） | 参见常见陷阱章节的详细讲解 |
| 大表 DDL 锁表（易错点） | 参见常见陷阱章节的详细讲解 |
| 缓冲池过小（易错点） | 参见常见陷阱章节的详细讲解 |
| 隐式提交（易错点） | 参见常见陷阱章节的详细讲解 |
| utf8 与 utf8mb4（易错点） | 参见常见陷阱章节的详细讲解 |

术语表与正文配合使用：先通读正文，遇到模糊术语回查本表；长期使用后术语会自然进入工作记忆。
