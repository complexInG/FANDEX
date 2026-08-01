---
order: 130
tags:
  - mysql
  - database
difficulty: intermediate
title: 'MySQL 快速查阅'
module: mysql
category: 'MySQL Reference'
description: '常用 SQL 语句、函数与配置参数速查。'
author: Anonymous
related:
  - mysql/事务与锁机制
  - mysql/配置与运维
  - mysql/控制器与应用
  - mysql/SQL注入基础与检测
prerequisites:
  - mysql/语法速查
updated: '2026-08-01'
---

## 1. 学习目标（Bloom 分类）

本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《MySQL 快速查阅》，属于 MySQL 模块，读者可以根据自身阶段选择阅读深度。

记忆层面：能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。能够说出 MySQL 的核心概念、语法与常用对象。

理解层面：能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。能够解释 MySQL 的执行原理与优化机制。

应用层面：能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。能够编写正确、高效的 MySQL 语句与操作。

分析层面：能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。能够分析 MySQL 相关方案在性能与一致性上的权衡。

评价层面：能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。能够根据业务场景评价 MySQL 技术选型。

创造层面：能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。能够组合 MySQL 与其他技术设计数据架构。

通过本节学习，读者应当能够把《MySQL 快速查阅》纳入自己的知识网络，并与 MySQL 模块的其他主题（InnoDB、索引、日志、主从、性能调优）建立关联。

## 2. 历史动机与发展脉络

《MySQL 快速查阅》是 MySQL 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。

MySQL 于 1995 年由 MySQL AB 发布，2008 年被 Sun 收购，2010 年随 Sun 并入 Oracle；MariaDB 是社区分支。
MySQL 8.0（2018）重写优化器、引入窗口函数与 CTE、默认 utf8mb4、数据字典升级；MySQL 8.4 与 9.x 继续演进（Oracle 创新版 + LTS 双轨）。
InnoDB 是默认存储引擎：事务、行锁、MVCC、崩溃恢复（redo/undo）；MyISAM 仅存于历史场景。

回到本文主题：MySQL 快速查阅 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。


## 3. 形式化定义与核心概念精讲

本节把《MySQL 快速查阅》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。

InnoDB 架构：缓冲池（Buffer Pool）、日志缓冲、redo/undo 日志；脏页刷盘与 checkpoint 机制。
索引：B+ 树主键聚集索引、二级索引、覆盖索引；索引下推（ICP）与 MRR 优化。
事务与锁：两阶段锁、间隙锁/临键锁（可重复读防幻读）、MVCC 快照读；隔离级别。

### 3.1 原文章节逐一精讲

原文档把主题拆分为 11 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。

#### 原文精读（完整保留）


#### 1. 数据库操作

##### 创建数据库

```sql
 CREATE DATABASE dbname;
 CREATE DATABASE IF NOT EXISTS dbname;
```

##### 创建数据库（指定字符集）

```sql
 CREATE DATABASE dbname
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
 -
 CREATE DATABASE ecommerce
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

##### 修改数据库字符集

```sql
 ALTER DATABASE dbname
  CHARACTER SET gbk
  COLLATE gbk_chinese_ci;
```

##### 查看数据库

```sql
 SHOW DATABASES;
 SHOW CREATE DATABASE dbname;
 -
 SELECT table_schema AS '数据库',
  SUM(data_length + index_length) / 1024 / 1024 AS '大小(MB)'
 from information_schema.tables
 GROUP BY table_schema;
```

##### 使用数据库

```sql
 use dbname;
```

##### 删除数据库

```sql
 DROP DATABASE dbname;
 DROP DATABASE IF EXISTS dbname;
```

---

#### 2. 表操作

##### 创建表

```sql
 CREATE TABLE tablename (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  age INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 )
 -
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

##### 查看表

```sql
 SHOW TABLES;
 DESC tablename;
 SHOW COLUMNS FROM tablename;
 SHOW CREATE TABLE tablename;
 -
 SELECT table_name AS '表名',
  data_length / 1024 / 1024 AS '数据大小(MB)',
  index_length / 1024 / 1024 AS '索引大小(MB)'
 from information_schema.tables
 WHERE table_schema = DATABASE();
```

##### 修改表结构

```sql
 -
 ALTER TABLE tablename ADD COLUMN colname type;
 ALTER TABLE tablename ADD COLUMN colname type AFTER another_col;
 -
 ALTER TABLE tablename MODIFY COLUMN colname new_type;
 ALTER TABLE tablename CHANGE COLUMN oldname newname new_type;
 -
 ALTER TABLE tablename DROP COLUMN colname;
 -
 ALTER TABLE oldname RENAME TO newname;
 -
 ALTER TABLE users ADD COLUMN phone VARCHAR(20) AFTER email;
 ALTER TABLE users MODIFY COLUMN age SMALLINT UNSIGNED;
 ALTER TABLE users CHANGE COLUMN phone mobile VARCHAR(20);
 ALTER TABLE users DROP COLUMN age;
```

##### 删除表

```sql
 DROP TABLE tablename;
 DROP TABLE IF EXISTS tablename;
```

##### 清空表

```sql
 TRUNCATE TABLE tablename;
```

##### 复制表

```sql
 -
 CREATE TABLE newtable LIKE oldtable;
 -
 CREATE TABLE newtable AS SELECT * FROM oldtable;
 -
 CREATE TABLE active_users AS SELECT * FROM users WHERE status = 1;
```

---

#### 3. 数据类型

##### 字符型

- CHAR(n) - 定长字符串，最多255字符
- VARCHAR(n) - 变长字符串，最多65535字符
- TEXT - 长文本，最多65535字符
- MEDIUMTEXT - 中等文本，最多16MB
- LONGTEXT - 超长文本，最多4GB
- ENUM - 枚举类型
- SET - 集合类型
- BLOB - 二进制大对象

##### 数值型

- TINYINT - 微整数 (-128~127)
- SMALLINT - 小整数 (-32768~32767)
- MEDIUMINT - 中等整数
- INT - 整数 (-21亿~21亿)
- BIGINT - 大整数
- FLOAT - 单精度浮点
- DOUBLE - 双精度浮点
- DECIMAL(M,D) - 定点数

##### 日期时间型

- DATE - 日期 (YYYY-MM-DD)
- TIME - 时间 (HH:MM:SS)
- DATETIME - 日期时间
- TIMESTAMP - 时间戳
- YEAR - 年份

---

#### 4. 约束类型

##### 常用约束

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

##### 外键约束选项

```sql
 forEIGN KEY (col) REFERENCES parent_table(col)
  ON DELETE CASCADE -- 级联删除
  ON UPDATE CASCADE -- 级联更新
  ON DELETE SET NULL -- 删除时设为NULL
  ON DELETE RESTRICT -- 限制删除
```

---

#### 5. 数据操作

##### 插入数据

```sql
 -
 inSERT INTO table(col1, col2) VALUES(val1, val2);
 -
 inSERT INTO table(col1, col2) VALUES
  (v1, v2),
  (v3, v4),
  (v5, v6);
 -
 inSERT INTO table(cols) VALUES(vals)
 ON DUPLICATE KEY UPDATE col = new_val;
 -
 replace INTO table(cols) VALUES(vals);
 -
 inSERT INTO users(username, email, password)
 VALUES ('zhangsan', 'zhang@example.com', '123456');
 -
 inSERT INTO users(username, email, password) VALUES
  ('lisi', 'li@example.com', '654321'),
  ('wangwu', 'wang@example.com', 'abc123'),
  ('zhaoliu', 'zhao@example.com', 'xyz789');
 -
 inSERT INTO users(id, username, email)
 VALUES (1, 'zhangsan_new', 'zhang_new@example.com')
 ON DUPLICATE KEY UPDATE username = VALUES(username), email = VALUES(email);
```

##### 更新数据

```sql
 UPDATE table SET col = val WHERE condition;
 UPDATE table SET col1 = val1, col2 = val2 WHERE condition;
 -
 UPDATE users SET status = 0 WHERE id = 1;
 -
 UPDATE users SET status = 1 WHERE created_at > '2024-01-01';
 -
 UPDATE orders o
 JOIN users u ON o.user_id = u.id
 SET o.user_name = u.username
 WHERE o.user_name IS NULL;
```

##### 删除数据

```sql
 delete FROM table WHERE condition; -- 按条件删除
 delete FROM table; -- 删除所有行
 TRUNCATE TABLE table; -- 清空表（重置自增ID）
 -
 delete FROM users WHERE id = 1;
 -
 delete FROM logs WHERE created_at < '2024-01-01';
 -
 delete o FROM orders o
 JOIN users u ON o.user_id = u.id
 WHERE u.status = 0;
```

---

#### 6. 数据查询

##### 基础查询

```sql
 SELECT * FROM table;
 SELECT col1, col2 FROM table;
 SELECT col1 AS alias FROM table;
 SELECT DISTINCT col FROM table;
 -
 SELECT id, username, email FROM users WHERE status = 1;
 -
 SELECT COUNT(*) AS user_count FROM users;
```

##### 条件查询

```sql
 -
 SELECT * FROM table WHERE col = value;
 SELECT * FROM table WHERE col > value;
 SELECT * FROM table WHERE col != value;
 -
 SELECT * FROM table WHERE col1 = v1 AND col2 = v2;
 SELECT * FROM table WHERE col1 = v1 OR col2 = v2;
 SELECT * FROM table WHERE NOT col = value;
 -
 SELECT * FROM table WHERE col BETWEEN val1 AND val2;
 SELECT * FROM table WHERE col IN (val1, val2, val3);
 -
 SELECT * FROM table WHERE col LIKE '%pattern%';
 SELECT * FROM table WHERE col LIKE 'pattern%';
 SELECT * FROM table WHERE col LIKE '_pattern';
 -
 SELECT * FROM table WHERE col IS NULL;
 SELECT * FROM table WHERE col IS NOT NULL;
 -
 SELECT * FROM users WHERE age BETWEEN 18 AND 30;
 -
 SELECT * FROM users WHERE city IN ('北京', '上海', '广州');
 -
 SELECT * FROM users WHERE username LIKE '%zhang%';
 -
 SELECT * FROM users WHERE phone IS NULL;
```

##### 排序与分页

```sql
 -
 SELECT * FROM table ORDER BY col ASC;
 SELECT * FROM table ORDER BY col DESC;
 SELECT * FROM table ORDER BY col1 ASC, col2 DESC;
 -
 SELECT * FROM table LIMIT 10;
 SELECT * FROM table LIMIT 10 OFFSET 20;
 SELECT * FROM table LIMIT 20, 10;
 -
 SELECT * FROM users ORDER BY created_at DESC;
 -
 SELECT * FROM users ORDER BY created_at DESC LIMIT 20, 10;
```

##### 分组查询

```sql
 -
 SELECT col, COUNT(*) FROM table GROUP BY col;
 -
 SELECT col, AVG(price) FROM table
 GROUP BY col
 HAVING AVG(price) > 100;
 -
 SELECT city, COUNT(*) AS user_count
 from users
 GROUP BY city
 ORDER BY user_count DESC;
 -
 SELECT DATE_FORMAT(created_at, '%Y-%m') AS month,
  COUNT(*) AS register_count
 from users
 GROUP BY month
 ORDER BY month;
 -
 SELECT user_id, SUM(amount) AS total_amount
 from orders
 GROUP BY user_id
 HAVING total_amount > 1000;
```

##### 聚合函数

```sql
 SELECT
  COUNT(*) AS total, -- 统计行数
  SUM(price) AS sum, -- 求和
  AVG(price) AS avg, -- 平均值
  MAX(price) AS max, -- 最大值
  MIN(price) AS min -- 最小值
 from table;
 -
 SELECT
  COUNT(*) AS order_count,
  SUM(amount) AS total_amount,
  AVG(amount) AS avg_amount,
  MAX(amount) AS max_amount,
  MIN(amount) AS min_amount
 from orders
 WHERE created_at BETWEEN '2024-01-01' AND '2024-01-31';
```

##### 多表连接

```sql
 -
 SELECT * FROM a INNER JOIN b ON a.id = b.id;
 -
 SELECT * FROM a LEFT JOIN b ON a.id = b.id;
 -
 SELECT * FROM a RIGHT JOIN b ON a.id = b.id;
 -
 SELECT * FROM a LEFT JOIN b ON a.id = b.id
 UNION
 SELECT * FROM a RIGHT JOIN b ON a.id = b.id;
 -
 SELECT e1.name, e2.name AS manager
 from employees e1
 JOIN employees e2 ON e1.manager_id = e2.id;
 -
 SELECT o.id, o.amount, o.created_at,
  u.username, u.email
 from orders o
 JOIN users u ON o.user_id = u.id
 WHERE o.created_at > '2024-01-01';
 -
 SELECT u.username, COUNT(o.id) AS order_count
 from users u
 LEFT JOIN orders o ON u.id = o.user_id
 GROUP BY u.id;
```

---

#### 7. 索引操作

##### 创建索引

```sql
 -
 CREATE INDEX idx_name ON table(col);
 -
 CREATE UNIQUE INDEX idx_name ON table(col);
 -
 CREATE INDEX idx_name ON table(col1, col2);
 -
 ALTER TABLE table ADD FULLTEXT INDEX ft_idx(col);
 -
 CREATE INDEX idx_users_email ON users(email);
 CREATE INDEX idx_users_status ON users(status);
 CREATE INDEX idx_users_created_at ON users(created_at);
 CREATE UNIQUE INDEX idx_users_username ON users(username);
 -
 CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);
```

##### 查看索引

```sql
 SHOW INDEX FROM table;
 -
 SELECT index_name, column_name
 from information_schema.statistics
 WHERE table_schema = DATABASE() AND table_name = 'users';
```

##### 删除索引

```sql
 DROP INDEX idx_name ON table;
 -
 DROP INDEX idx_users_email ON users;
```

---

#### 8. 用户与权限

##### 用户管理

```sql
 -
 CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
 CREATE USER 'username'@'%' IDENTIFIED BY 'password'; -- 允许远程
 -
 ALTER USER 'username'@'localhost' IDENTIFIED BY 'new_password';
 -
 DROP USER 'username'@'localhost';
 -
 SELECT user, host FROM mysql.user;
 -
 CREATE USER 'readonly'@'%' IDENTIFIED BY 'read123';
 -
 CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin123';
```

##### 权限管理

```sql
 -
 GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'localhost';
 GRANT SELECT, INSERT, UPDATE ON dbname.table TO 'username'@'localhost';
 -
 REVOKE ALL PRIVILEGES ON dbname.* FROM 'username'@'localhost';
 -
 SHOW GRANTS FOR 'username'@'localhost';
 -
 FLUSH PRIVILEGES;
 -
 GRANT SELECT ON ecommerce.* TO 'readonly'@'%';
 -
 GRANT SELECT, INSERT, UPDATE, DELETE ON ecommerce.* TO 'appuser'@'%';
 -
 GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
```

##### 常用权限

- ALL PRIVILEGES - 所有权限
- SELECT, INSERT, UPDATE, DELETE - 基本操作
- CREATE, DROP - 创建/删除
- GRANT OPTION - 授权权限
- ALTER - 修改表结构
- INDEX - 创建索引

---

#### 9. 事务管理

##### 基本操作

```sql
 -
 START TRANSACTION;
 -
 BEGIN;
 -
 commit;
 -
 ROLLBACK;
 -
 SAVEPOINT savepoint_name;
 -
 ROLLBACK TO SAVEPOINT savepoint_name;
 -
 BEGIN;
 UPDATE accounts SET balance = balance - 100 WHERE id = 1;
 UPDATE accounts SET balance = balance + 100 WHERE id = 2;
 commit;
 -
 BEGIN;
 inSERT INTO orders (...) VALUES (...);
 SAVEPOINT order_saved;
 inSERT INTO order_items (...) VALUES (...);
 if error THEN
  ROLLBACK TO order_saved;
 END IF;
 commit;
```

##### 隔离级别

```sql
 -
 SELECT @@transaction_isolation;
 -
 SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
 SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

##### 隔离级别说明

- READ UNCOMMITTED - 最低级别，可能读取未提交数据
- READ COMMITTED - 读取已提交数据
- REPEATABLE READ - 可重复读（MySQL默认）
- SERIALIZABLE - 最高级别，串行执行

---

#### 10. 常用函数

##### 字符串函数

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
 -
 SELECT CONCAT(last_name, ' ', first_name) AS full_name FROM users;
 -
 SELECT SUBSTRING(email, INSTR(email, '@') + 1) AS domain FROM users;
 -
 SELECT LOWER(CONCAT(SUBSTRING(first_name, 1, 1), last_name)) AS username FROM users;
```

##### 日期函数

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
 -
 SELECT * FROM users WHERE DATE_FORMAT(created_at, '%Y-%m') = DATE_FORMAT(NOW(), '%Y-%m');
 -
 SELECT TIMESTAMPDIFF(YEAR, birthday, CURDATE()) AS age FROM users;
 -
 SELECT DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AS monday;
```

##### 数值函数

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
 -
 SELECT ROUND(AVG(rating), 1) AS avg_rating FROM products;
 -
 SELECT FLOOR(RAND() * 9000 + 1000) AS captcha;
 -
 SELECT price * 0.8 AS discounted_price FROM products;
```

##### 条件函数

```sql
 if(age >= 18, '成人', '未成年') -- 条件判断
 ifNULL(email, '未填写') -- NULL替换
 NULLIF(a, b) -- 相等返回NULL
 case
  WHEN score >= 90 THEN '优秀'
  WHEN score >= 60 THEN '及格'
  ELSE '不及格'
 END -- 多条件判断
 -
 SELECT id, username, IF(status = 1, '活跃', '禁用') AS status_text FROM users;
 -
 SELECT
  username,
  CASE
  WHEN points >= 1000 THEN 'VIP'
  WHEN points >= 500 THEN '高级会员'
  ELSE '普通会员'
  END AS level
 from users;
 -
 SELECT name, IFNULL(phone, '未填写') AS phone FROM customers;
```

---

#### 附录：常用命令

##### 服务器管理

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

##### 备份与恢复

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

##### 查看系统信息

```sql
 SELECT VERSION(); -- 版本
 SELECT USER(); -- 当前用户
 SELECT DATABASE(); -- 当前数据库
 SHOW STATUS; -- 服务器状态
 SHOW VARIABLES; -- 配置变量
 SHOW PROCESSLIST; -- 进程列表
 SHOW VARIABLES LIKE 'slow_query%'; -- 慢查询状态
```

---



### 3.2 概念关系图

下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：

```mermaid
flowchart LR
    A["MySQL 快速查阅"] --> B["核心概念"]
    B --> C["原理机制"]
    B --> D["代码实践"]
    C --> E["工程应用"]
    D --> E
```

图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。

## 4. 理论推导与原理解析

本节深入《MySQL 快速查阅》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。

InnoDB 架构：缓冲池（Buffer Pool）、日志缓冲、redo/undo 日志；脏页刷盘与 checkpoint 机制。
索引：B+ 树主键聚集索引、二级索引、覆盖索引；索引下推（ICP）与 MRR 优化。
事务与锁：两阶段锁、间隙锁/临键锁（可重复读防幻读）、MVCC 快照读；隔离级别。
复制：binlog 逻辑复制（statement/row/mixed），主从异步、半同步与组复制。

需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。

## 5. 代码示例与逐行讲解

本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。

### 5.1 示例：创建数据库

该示例来自原文《创建数据库》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 CREATE DATABASE dbname;
 CREATE DATABASE IF NOT EXISTS dbname;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，包含 1 类关键结构（CREATE）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.2 示例：创建数据库（指定字符集）

该示例来自原文《创建数据库（指定字符集）》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 CREATE DATABASE dbname
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
 -
 CREATE DATABASE ecommerce
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 1 类关键结构（CREATE）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.3 示例：修改数据库字符集

该示例来自原文《修改数据库字符集》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 ALTER DATABASE dbname
  CHARACTER SET gbk
  COLLATE gbk_chinese_ci;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，包含 1 类关键结构（ALTER）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.4 示例：查看数据库

该示例来自原文《查看数据库》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 SHOW DATABASES;
 SHOW CREATE DATABASE dbname;
 -
 SELECT table_schema AS '数据库',
  SUM(data_length + index_length) / 1024 / 1024 AS '大小(MB)'
 from information_schema.tables
 GROUP BY table_schema;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 3 类关键结构（from、SELECT、CREATE）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.5 示例：使用数据库

该示例来自原文《使用数据库》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 use dbname;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 1 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.6 示例：删除数据库

该示例来自原文《删除数据库》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 DROP DATABASE dbname;
 DROP DATABASE IF EXISTS dbname;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.7 示例：创建表

该示例来自原文《创建表》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 CREATE TABLE tablename (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  age INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 )
 -
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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 17 行有效代码，包含 1 类关键结构（CREATE）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.8 示例：查看表

该示例来自原文《查看表》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 SHOW TABLES;
 DESC tablename;
 SHOW COLUMNS FROM tablename;
 SHOW CREATE TABLE tablename;
 -
 SELECT table_name AS '表名',
  data_length / 1024 / 1024 AS '数据大小(MB)',
  index_length / 1024 / 1024 AS '索引大小(MB)'
 from information_schema.tables
 WHERE table_schema = DATABASE();
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 4 类关键结构（from、SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.9 示例：修改表结构

该示例来自原文《修改表结构》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 ALTER TABLE tablename ADD COLUMN colname type;
 ALTER TABLE tablename ADD COLUMN colname type AFTER another_col;
 -
 ALTER TABLE tablename MODIFY COLUMN colname new_type;
 ALTER TABLE tablename CHANGE COLUMN oldname newname new_type;
 -
 ALTER TABLE tablename DROP COLUMN colname;
 -
 ALTER TABLE oldname RENAME TO newname;
 -
 ALTER TABLE users ADD COLUMN phone VARCHAR(20) AFTER email;
 ALTER TABLE users MODIFY COLUMN age SMALLINT UNSIGNED;
 ALTER TABLE users CHANGE COLUMN phone mobile VARCHAR(20);
 ALTER TABLE users DROP COLUMN age;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 15 行有效代码，包含 1 类关键结构（ALTER）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.10 示例：删除表

该示例来自原文《删除表》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 DROP TABLE tablename;
 DROP TABLE IF EXISTS tablename;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.11 示例：清空表

该示例来自原文《清空表》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 TRUNCATE TABLE tablename;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 1 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.12 示例：复制表

该示例来自原文《复制表》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 CREATE TABLE newtable LIKE oldtable;
 -
 CREATE TABLE newtable AS SELECT * FROM oldtable;
 -
 CREATE TABLE active_users AS SELECT * FROM users WHERE status = 1;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，包含 3 类关键结构（SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.13 示例：常用约束

该示例来自原文《常用约束》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 1 类关键结构（CREATE）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.14 示例：外键约束选项

该示例来自原文《外键约束选项》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 forEIGN KEY (col) REFERENCES parent_table(col)
  ON DELETE CASCADE -- 级联删除
  ON UPDATE CASCADE -- 级联更新
  ON DELETE SET NULL -- 删除时设为NULL
  ON DELETE RESTRICT -- 限制删除
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.15 示例：插入数据

该示例来自原文《插入数据》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 inSERT INTO table(col1, col2) VALUES(val1, val2);
 -
 inSERT INTO table(col1, col2) VALUES
  (v1, v2),
  (v3, v4),
  (v5, v6);
 -
 inSERT INTO table(cols) VALUES(vals)
 ON DUPLICATE KEY UPDATE col = new_val;
 -
 replace INTO table(cols) VALUES(vals);
 -
 inSERT INTO users(username, email, password)
 VALUES ('zhangsan', 'zhang@example.com', '123456');
 -
 inSERT INTO users(username, email, password) VALUES
  ('lisi', 'li@example.com', '654321'),
  ('wangwu', 'wang@example.com', 'abc123'),
  ('zhaoliu', 'zhao@example.com', 'xyz789');
 -
 inSERT INTO users(id, username, email)
 VALUES (1, 'zhangsan_new', 'zhang_new@example.com')
 ON DUPLICATE KEY UPDATE username = VALUES(username), email = VALUES(email);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 24 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.16 示例：更新数据

该示例来自原文《更新数据》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 UPDATE table SET col = val WHERE condition;
 UPDATE table SET col1 = val1, col2 = val2 WHERE condition;
 -
 UPDATE users SET status = 0 WHERE id = 1;
 -
 UPDATE users SET status = 1 WHERE created_at > '2024-01-01';
 -
 UPDATE orders o
 JOIN users u ON o.user_id = u.id
 SET o.user_name = u.username
 WHERE o.user_name IS NULL;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.17 示例：删除数据

该示例来自原文《删除数据》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 delete FROM table WHERE condition; -- 按条件删除
 delete FROM table; -- 删除所有行
 TRUNCATE TABLE table; -- 清空表（重置自增ID）
 -
 delete FROM users WHERE id = 1;
 -
 delete FROM logs WHERE created_at < '2024-01-01';
 -
 delete o FROM orders o
 JOIN users u ON o.user_id = u.id
 WHERE u.status = 0;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，包含 1 类关键结构（FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.18 示例：基础查询

该示例来自原文《基础查询》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 SELECT * FROM table;
 SELECT col1, col2 FROM table;
 SELECT col1 AS alias FROM table;
 SELECT DISTINCT col FROM table;
 -
 SELECT id, username, email FROM users WHERE status = 1;
 -
 SELECT COUNT(*) AS user_count FROM users;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.19 示例：条件查询

该示例来自原文《条件查询》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 SELECT * FROM table WHERE col = value;
 SELECT * FROM table WHERE col > value;
 SELECT * FROM table WHERE col != value;
 -
 SELECT * FROM table WHERE col1 = v1 AND col2 = v2;
 SELECT * FROM table WHERE col1 = v1 OR col2 = v2;
 SELECT * FROM table WHERE NOT col = value;
 -
 SELECT * FROM table WHERE col BETWEEN val1 AND val2;
 SELECT * FROM table WHERE col IN (val1, val2, val3);
 -
 SELECT * FROM table WHERE col LIKE '%pattern%';
 SELECT * FROM table WHERE col LIKE 'pattern%';
 SELECT * FROM table WHERE col LIKE '_pattern';
 -
 SELECT * FROM table WHERE col IS NULL;
 SELECT * FROM table WHERE col IS NOT NULL;
 -
 SELECT * FROM users WHERE age BETWEEN 18 AND 30;
 -
 SELECT * FROM users WHERE city IN ('北京', '上海', '广州');
 -
 SELECT * FROM users WHERE username LIKE '%zhang%';
 -
 SELECT * FROM users WHERE phone IS NULL;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 26 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.20 示例：排序与分页

该示例来自原文《排序与分页》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 SELECT * FROM table ORDER BY col ASC;
 SELECT * FROM table ORDER BY col DESC;
 SELECT * FROM table ORDER BY col1 ASC, col2 DESC;
 -
 SELECT * FROM table LIMIT 10;
 SELECT * FROM table LIMIT 10 OFFSET 20;
 SELECT * FROM table LIMIT 20, 10;
 -
 SELECT * FROM users ORDER BY created_at DESC;
 -
 SELECT * FROM users ORDER BY created_at DESC LIMIT 20, 10;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.21 示例：分组查询

该示例来自原文《分组查询》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 SELECT col, COUNT(*) FROM table GROUP BY col;
 -
 SELECT col, AVG(price) FROM table
 GROUP BY col
 HAVING AVG(price) > 100;
 -
 SELECT city, COUNT(*) AS user_count
 from users
 GROUP BY city
 ORDER BY user_count DESC;
 -
 SELECT DATE_FORMAT(created_at, '%Y-%m') AS month,
  COUNT(*) AS register_count
 from users
 GROUP BY month
 ORDER BY month;
 -
 SELECT user_id, SUM(amount) AS total_amount
 from orders
 GROUP BY user_id
 HAVING total_amount > 1000;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 22 行有效代码，包含 3 类关键结构（from、SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.22 示例：聚合函数

该示例来自原文《聚合函数》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 SELECT
  COUNT(*) AS total, -- 统计行数
  SUM(price) AS sum, -- 求和
  AVG(price) AS avg, -- 平均值
  MAX(price) AS max, -- 最大值
  MIN(price) AS min -- 最小值
 from table;
 -
 SELECT
  COUNT(*) AS order_count,
  SUM(amount) AS total_amount,
  AVG(amount) AS avg_amount,
  MAX(amount) AS max_amount,
  MIN(amount) AS min_amount
 from orders
 WHERE created_at BETWEEN '2024-01-01' AND '2024-01-31';
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 16 行有效代码，包含 2 类关键结构（from、SELECT）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.23 示例：多表连接

该示例来自原文《多表连接》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 SELECT * FROM a INNER JOIN b ON a.id = b.id;
 -
 SELECT * FROM a LEFT JOIN b ON a.id = b.id;
 -
 SELECT * FROM a RIGHT JOIN b ON a.id = b.id;
 -
 SELECT * FROM a LEFT JOIN b ON a.id = b.id
 UNION
 SELECT * FROM a RIGHT JOIN b ON a.id = b.id;
 -
 SELECT e1.name, e2.name AS manager
 from employees e1
 JOIN employees e2 ON e1.manager_id = e2.id;
 -
 SELECT o.id, o.amount, o.created_at,
  u.username, u.email
 from orders o
 JOIN users u ON o.user_id = u.id
 WHERE o.created_at > '2024-01-01';
 -
 SELECT u.username, COUNT(o.id) AS order_count
 from users u
 LEFT JOIN orders o ON u.id = o.user_id
 GROUP BY u.id;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 25 行有效代码，包含 3 类关键结构（from、SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.24 示例：创建索引

该示例来自原文《创建索引》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 CREATE INDEX idx_name ON table(col);
 -
 CREATE UNIQUE INDEX idx_name ON table(col);
 -
 CREATE INDEX idx_name ON table(col1, col2);
 -
 ALTER TABLE table ADD FULLTEXT INDEX ft_idx(col);
 -
 CREATE INDEX idx_users_email ON users(email);
 CREATE INDEX idx_users_status ON users(status);
 CREATE INDEX idx_users_created_at ON users(created_at);
 CREATE UNIQUE INDEX idx_users_username ON users(username);
 -
 CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 15 行有效代码，包含 2 类关键结构（CREATE、ALTER）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.25 示例：查看索引

该示例来自原文《查看索引》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 SHOW INDEX FROM table;
 -
 SELECT index_name, column_name
 from information_schema.statistics
 WHERE table_schema = DATABASE() AND table_name = 'users';
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 3 类关键结构（from、SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.26 示例：删除索引

该示例来自原文《删除索引》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 DROP INDEX idx_name ON table;
 -
 DROP INDEX idx_users_email ON users;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.27 示例：用户管理

该示例来自原文《用户管理》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
 CREATE USER 'username'@'%' IDENTIFIED BY 'password'; -- 允许远程
 -
 ALTER USER 'username'@'localhost' IDENTIFIED BY 'new_password';
 -
 DROP USER 'username'@'localhost';
 -
 SELECT user, host FROM mysql.user;
 -
 CREATE USER 'readonly'@'%' IDENTIFIED BY 'read123';
 -
 CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin123';
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 4 类关键结构（SELECT、CREATE、ALTER、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.28 示例：权限管理

该示例来自原文《权限管理》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'localhost';
 GRANT SELECT, INSERT, UPDATE ON dbname.table TO 'username'@'localhost';
 -
 REVOKE ALL PRIVILEGES ON dbname.* FROM 'username'@'localhost';
 -
 SHOW GRANTS FOR 'username'@'localhost';
 -
 FLUSH PRIVILEGES;
 -
 GRANT SELECT ON ecommerce.* TO 'readonly'@'%';
 -
 GRANT SELECT, INSERT, UPDATE, DELETE ON ecommerce.* TO 'appuser'@'%';
 -
 GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 15 行有效代码，包含 3 类关键结构（SELECT、INSERT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.29 示例：基本操作

该示例来自原文《基本操作》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 START TRANSACTION;
 -
 BEGIN;
 -
 commit;
 -
 ROLLBACK;
 -
 SAVEPOINT savepoint_name;
 -
 ROLLBACK TO SAVEPOINT savepoint_name;
 -
 BEGIN;
 UPDATE accounts SET balance = balance - 100 WHERE id = 1;
 UPDATE accounts SET balance = balance + 100 WHERE id = 2;
 commit;
 -
 BEGIN;
 inSERT INTO orders (...) VALUES (...);
 SAVEPOINT order_saved;
 inSERT INTO order_items (...) VALUES (...);
 if error THEN
  ROLLBACK TO order_saved;
 END IF;
 commit;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 26 行有效代码，包含 1 类关键结构（if）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.30 示例：隔离级别

该示例来自原文《隔离级别》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 -
 SELECT @@transaction_isolation;
 -
 SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
 SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 1 类关键结构（SELECT）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.31 示例：字符串函数

该示例来自原文《字符串函数》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

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
 -
 SELECT CONCAT(last_name, ' ', first_name) AS full_name FROM users;
 -
 SELECT SUBSTRING(email, INSTR(email, '@') + 1) AS domain FROM users;
 -
 SELECT LOWER(CONCAT(SUBSTRING(first_name, 1, 1), last_name)) AS username FROM users;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 17 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.32 示例：日期函数

该示例来自原文《日期函数》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

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
 -
 SELECT * FROM users WHERE DATE_FORMAT(created_at, '%Y-%m') = DATE_FORMAT(NOW(), '%Y-%m');
 -
 SELECT TIMESTAMPDIFF(YEAR, birthday, CURDATE()) AS age FROM users;
 -
 SELECT DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AS monday;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 20 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.33 示例：数值函数

该示例来自原文《数值函数》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

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
 -
 SELECT ROUND(AVG(rating), 1) AS avg_rating FROM products;
 -
 SELECT FLOOR(RAND() * 9000 + 1000) AS captcha;
 -
 SELECT price * 0.8 AS discounted_price FROM products;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 16 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.34 示例：条件函数

该示例来自原文《条件函数》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 if(age >= 18, '成人', '未成年') -- 条件判断
 ifNULL(email, '未填写') -- NULL替换
 NULLIF(a, b) -- 相等返回NULL
 case
  WHEN score >= 90 THEN '优秀'
  WHEN score >= 60 THEN '及格'
  ELSE '不及格'
 END -- 多条件判断
 -
 SELECT id, username, IF(status = 1, '活跃', '禁用') AS status_text FROM users;
 -
 SELECT
  username,
  CASE
  WHEN points >= 1000 THEN 'VIP'
  WHEN points >= 500 THEN '高级会员'
  ELSE '普通会员'
  END AS level
 from users;
 -
 SELECT name, IFNULL(phone, '未填写') AS phone FROM customers;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 21 行有效代码，包含 3 类关键结构（from、SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.35 示例：服务器管理

该示例来自原文《服务器管理》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.36 示例：备份与恢复

该示例来自原文《备份与恢复》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.37 示例：查看系统信息

该示例来自原文《查看系统信息》小节，用于演示MySQL 快速查阅相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
 SELECT VERSION(); -- 版本
 SELECT USER(); -- 当前用户
 SELECT DATABASE(); -- 当前数据库
 SHOW STATUS; -- 服务器状态
 SHOW VARIABLES; -- 配置变量
 SHOW PROCESSLIST; -- 进程列表
 SHOW VARIABLES LIKE 'slow_query%'; -- 慢查询状态
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 1 类关键结构（SELECT）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。


综合以上示例，可以总结出本主题的代码实践要点：第一，先定义清晰的输入输出契约；第二，核心逻辑保持单一职责；第三，错误处理与边界条件不可省略；第四，命名与注释表达意图而非复述代码。

## 6. 对比分析

对比是理解《MySQL 快速查阅》定位的最快路径。下面从多个维度与相邻方案进行对比。

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

本节把《MySQL 快速查阅》放入真实工程场景，给出可复用的模式与组织方法。

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

本节通过一个完整案例把《MySQL 快速查阅》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。

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

关于《MySQL 快速查阅》的核心结论：

MySQL 的性能核心是 InnoDB 的缓冲池与索引设计。
日志（redo/undo/binlog）理解是故障恢复与复制的基础。
工程化：字符集、连接池、备份、监控四件套。

原文档各小节的要点回顾：

- 1. 数据库操作：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 2. 表操作：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 3. 数据类型：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 4. 约束类型：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 5. 数据操作：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 6. 数据查询：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 7. 索引操作：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 8. 用户与权限：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 9. 事务管理：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 10. 常用函数：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 附录：常用命令：该小节围绕MySQL 快速查阅展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。

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

本文属于 MySQL 模块。为了把《MySQL 快速查阅》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。

```mermaid
flowchart LR
    A["MySQL 快速查阅"]
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
| MySQL 快速查阅 | 071-MySQLQuickLookup | 本文自身 |
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

下表整理《MySQL 快速查阅》及 MySQL 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。

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
