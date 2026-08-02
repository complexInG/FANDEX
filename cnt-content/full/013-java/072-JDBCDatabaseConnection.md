---
order: 720
title: Java JDBC 数据库连接
module: 'java'
category: 后端技术
difficulty: beginner
description: Java JDBC 数据库连接 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## 建立连接

**基本写法：DriverManager 获取连接**
`DriverManager.getConnection("<url>", "<用户>", "<密码>");`
```java
// 建立数据库连接
Connection conn = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/db", "root", "pwd");
```

---

**基本写法：使用 Properties**
`DriverManager.getConnection(<url>, <properties>);`
```java
// 通过 Properties 传参
Properties p = new Properties();
p.setProperty("user", "root");
p.setProperty("password", "pwd");
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/db", p);
```

---

## Statement 执行 SQL

**基本写法：创建 Statement**
`<connection>.createStatement();`
```java
// 创建静态 SQL 执行器
Statement st = conn.createStatement();
```

---

**基本写法：执行查询**
`<statement>.executeQuery("<sql>");`
```java
// 执行查询并返回结果集
ResultSet rs = st.executeQuery("SELECT * FROM user");
```

---

**基本写法：执行更新**
`<statement>.executeUpdate("<sql>");`
```java
// 执行 INSERT/UPDATE/DELETE
int rows = st.executeUpdate("DELETE FROM user WHERE id=1");
```

---

## PreparedStatement 参数化

**基本写法：创建预编译语句**
`<connection>.prepareStatement("<sql>");`
```java
// 预编译防 SQL 注入
PreparedStatement ps = conn.prepareStatement(
    "SELECT * FROM user WHERE id = ?");
```

---

**基本写法：设置参数**
`<ps>.setInt(<位置>, <值>);`
```java
// 按位置设置整型参数
ps.setInt(1, 100);
```

---

**基本写法：设置字符串参数**
`<ps>.setString(<位置>, <值>);`
```java
// 按位置设置字符串参数
ps.setString(1, "Alice");
```

---

**基本写法：执行预编译查询**
`<ps>.executeQuery();`
```java
// 执行预编译查询
ResultSet rs = ps.executeQuery();
```

---

**基本写法：执行预编译更新**
`<ps>.executeUpdate();`
```java
// 执行预编译更新
int rows = ps.executeUpdate();
```

---

## ResultSet 遍历

**基本写法：遍历结果集**
`while (<rs>.next()) { <rs>.getX("<列>"); }`
```java
// 按列名读取结果
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
}
```

---

**基本写法：按索引取值**
`<rs>.getInt(<位置>);`
```java
// 按列位置取值
int id = rs.getInt(1);
```

---

**基本写法：可滚动结果集**
`<connection>.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);`
```java
// 创建可前后滚动的结果集
Statement st = conn.createStatement(
    ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);
```

---

**基本写法：跳转到指定行**
`<rs>.absolute(<行号>);`
```java
// 移动到绝对行
rs.absolute(5);
```

---

## 事务管理

**基本写法：关闭自动提交**
`<connection>.setAutoCommit(false);`
```java
// 开启手动事务
conn.setAutoCommit(false);
```

---

**基本写法：提交事务**
`<connection>.commit();`
```java
// 提交当前事务
conn.commit();
```

---

**基本写法：回滚事务**
`<connection>.rollback();`
```java
// 回滚当前事务
conn.rollback();
```

---

**基本写法：设置保存点**
`<connection>.setSavepoint();`
```java
// 设置保存点
Savepoint sp = conn.setSavepoint();
```

---

**基本写法：回滚到保存点**
`<connection>.rollback(<savepoint>);`
```java
// 回滚到指定保存点
conn.rollback(sp);
```

---

## 批处理

**基本写法：添加批处理**
`<ps>.addBatch();`
```java
// 添加到批处理
ps.setInt(1, 1); ps.addBatch();
ps.setInt(1, 2); ps.addBatch();
```

---

**基本写法：执行批处理**
`<ps>.executeBatch();`
```java
// 执行批量操作
int[] counts = ps.executeBatch();
```

---

**基本写法：清空批处理**
`<ps>.clearBatch();`
```java
// 清空批处理队列
ps.clearBatch();
```

---

## 获取自增主键

**基本写法：返回生成键**
`<connection>.prepareStatement(<sql>, Statement.RETURN_GENERATED_KEYS);`
```java
// 执行后获取自增主键
PreparedStatement ps = conn.prepareStatement(
    "INSERT INTO user(name) VALUES(?)", Statement.RETURN_GENERATED_KEYS);
ps.setString(1, "Alice");
ps.executeUpdate();
ResultSet keys = ps.getGeneratedKeys();
if (keys.next()) { long id = keys.getLong(1); }
```

---

## 连接池

**基本写法：HikariCP 配置**
`new HikariConfig(); new HikariDataSource(<config>);`
```java
// 配置 HikariCP 连接池
HikariConfig cfg = new HikariConfig();
cfg.setJdbcUrl("jdbc:mysql://localhost/db");
cfg.setUsername("root");
cfg.setPassword("pwd");
cfg.setMaximumPoolSize(10);
HikariDataSource ds = new HikariDataSource(cfg);
Connection conn = ds.getConnection();
```

---

## try-with-resources 自动关闭

**基本写法：自动关闭资源**
`try (Connection c = ...; PreparedStatement p = ...) { }`
```java
// 自动关闭连接、语句、结果集
try (Connection c = ds.getConnection();
     PreparedStatement p = c.prepareStatement(sql)) {
    try (ResultSet rs = p.executeQuery()) {
        while (rs.next()) { }
    }
}
```

---

## 元数据查询

**基本写法：获取表元数据**
`<connection>.getMetaData().getTables(null, null, "<表名>", null);`
```java
// 查询数据库表信息
ResultSet rs = conn.getMetaData().getTables(null, null, "user", null);
```

---

**基本写法：获取结果集元数据**
`<rs>.getMetaData().getColumnCount();`
```java
// 获取列数及列名
ResultSetMetaData md = rs.getMetaData();
int n = md.getColumnCount();
String name = md.getColumnName(1);
```

---

## DataSource 与 JNDI

**基本写法：从 JNDI 获取 DataSource**
`InitialContext.doLookup("java:comp/env/jdbc/db");`
```java
// 通过 JNDI 查找数据源
DataSource ds = InitialContext.doLookup("java:comp/env/jdbc/db");
Connection conn = ds.getConnection();
```
