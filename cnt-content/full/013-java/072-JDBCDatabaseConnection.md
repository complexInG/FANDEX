---
order: 720
title: Java JDBC 数据库连接
module: 013-java
category: '013-java'
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

## 参考文献

Oracle Java 官方文档：https://docs.oracle.com/en/java/
OpenJDK 项目：https://openjdk.org/
Java 语言规范：https://docs.oracle.com/javase/specs/
Spring 官方文档：https://spring.io/projects/spring-boot
Baeldung 教程站：https://www.baeldung.com/
Maven 官方文档：https://maven.apache.org/guides/

## 延伸阅读

Java 并发与 JUC，见 013-java 模块并发文档。
JVM 内存与 GC 调优，见 013-java 模块 JVM 文档。
Spring Boot 微服务与 Kubernetes，见 013-java/041-JavaKubernetes 文档。
数据库访问（JDBC/JPA），见 019-sql 模块相关文档。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Java 全栈课程；尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Java 进阶课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 Java 集合框架源码级分析

HashMap 在 Java 8+ 由数组 + 链表 + 红黑树组成：哈希桶冲突超过 8 且容量不小于 64 时树化；扩容按 2 的幂进行，通过 `(n-1) & hash` 定位桶。
ConcurrentHashMap 采用 CAS + synchronized 锁桶（Java 8 实现），读操作无锁；与 HashTable 的全表锁相比并发度大幅提升。
ArrayList 扩容 1.5 倍并复制数组；LinkedList 每个节点有前后指针；LinkedList 的随机访问是 O(n)，顺序插入删除是 O(1)。
PriorityQueue 是小顶堆结构，offer/poll 为 O(log n)；TreeMap/TreeSet 基于红黑树，key 有序。
工程建议：按操作特征选型——随机访问用 ArrayList，频繁头尾操作用 ArrayDeque，排序键用 TreeMap，高并发用 ConcurrentHashMap。

### 13.2 JVM 垃圾回收与调优

分代假说：大多数对象朝生夕灭。新生代（Eden + Survivor）采用复制算法，老年代采用标记-整理或并发标记；GC Roots 可达性分析决定存活对象。
G1 把堆划分为 Region，跟踪每个 Region 的回收价值，优先回收收益最高的区域；ZGC 使用染色指针与读屏障实现亚毫秒级暂停。
调优参数：-Xms/-Xmx 设置堆，-XX:MaxMetaspaceSize 限制元空间，-XX:MaxGCPauseMillis 设置 G1 目标停顿。
调优流程：先用 GC 日志与 JFR 观察，再调整堆与 GC 策略；避免盲目复制网上参数。容器环境注意 -XX:MaxRAMPercentage。

### 13.3 虚拟线程与高并发编程

Java 21 的虚拟线程（Virtual Threads）由 JVM 调度，占用内存远小于平台线程，支持百万级并发任务；适合 I/O 密集场景。
使用 Executors.newVirtualThreadPerTaskExecutor() 创建线程池；阻塞 I/O 时虚拟线程自动让出载体线程。
注意：synchronized 块内阻塞会固定载体线程；尽量使用 ReentrantLock 或避免在锁内阻塞。
虚拟线程不是万能：CPU 密集任务仍受核心数限制；线程本地变量（ThreadLocal）在虚拟线程下成本更高。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Java 概述与开发环境 | 001-JavaOverviewDevEnv | 本文的前置基础 |
| 快速入门 | 002-QuickStart | 本文的前置基础 |
| 程序结构与基本语法 | 003-ProgramStructureBasicSyntax | 本文的并列主题 |
| 数据类型与类型转换 | 004-DataTypeConversion | 本文的并列主题 |
| 变量与常量 | 005-VariableConstant | 本文的并列主题 |
| 枚举与注解 | 006-JavaAnnotationsTutorial | 本文的并列主题 |
| 泛型进阶 | 007-JavaGenericsTutorial | 本文的并列主题 |
| 并发编程基础 | 008-ConcurrencyBasics | 本文的前置基础 |
| JUC并发包 | 009-JUCConcurrency | 本文的并列主题 |
| JVM类加载机制 | 010-JVMClassLoadingMechanism | 本文的原理深化 |
| JVM垃圾回收 | 011-JVMGC | 本文的并列主题 |
| Java反射 | 012-JavaReflection | 本文的并列主题 |
| Java序列化 | 013-JavaSerialization | 本文的并列主题 |
| JavaIO与NIO | 014-JavaIONIO | 本文的并列主题 |
| Java新特性 | 015-JavaNewFeatures | 本文的并列主题 |
| 运算符与表达式 | 016-OperatorExpression | 本文的并列主题 |
| Spring 基础：IoC 容器、AOP、Bean 生命周期与企业级开发核心 | 017-SpringBasicsIoCAOPBeanLifecycle | 本文的前置基础 |
| SpringBoot进阶 | 018-SpringBootAdvanced | 本文的并列主题 |
| SpringBoot安全 | 019-SpringBootSecurity | 本文的安全延伸 |
| SpringBoot数据访问 | 020-SpringBootDataAccess | 本文的并列主题 |
| Java设计模式 | 021-JavaDesignPattern | 本文的并列主题 |
| Java函数式编程 | 022-JavaFunctionalProgramming | 本文的并列主题 |
| Java网络编程 | 023-JavaNetworkProgramming | 本文的并列主题 |
| Java日志系统 | 024-JavaLogSystem | 本文的并列主题 |
| Java单元测试 | 025-JavaUnitTest | 本文的并列主题 |
| Java构建工具 | 026-JavaBuildTool | 本文的并列主题 |
| 控制流 | 027-ControlFlow | 本文的并列主题 |
| Java与微服务 | 028-JavaMicroservice | 本文的并列主题 |
| Java与消息队列 | 029-JavaMessageQueue | 本文的并列主题 |
| Java与Redis | 030-JavaRedis | 本文的并列主题 |
| Java与Docker | 031-JavaDocker | 本文的并列主题 |
| Java与GraphQL | 032-JavaGraphQL | 本文的并列主题 |
| Java性能调优 | 033-JavaPerformanceTuning | 本文的性能延伸 |
| Java与AI | 034-JavaAI | 本文的并列主题 |
| Java与安全 | 035-JavaSecurity | 本文的安全延伸 |
| Java与WebAssembly | 036-JavaWebAssembly | 本文的并列主题 |
| Java与响应式编程 | 037-JavaReactiveProgramming | 本文的并列主题 |
| 方法详解 | 038-MethodDetailed | 本文的并列主题 |
| Java与虚拟线程 | 039-JavaVirtualThread | 本文的并列主题 |
| Java与GraalVM | 040-JavaGraalVM | 本文的并列主题 |
| Java与Kubernetes | 041-JavaKubernetes | 本文的并列主题 |
| Java记录类 | 042-JavaRecordClass | 本文的并列主题 |
| Java文本块 | 043-JavaTextBlock | 本文的并列主题 |
| Java模块系统 | 044-JavaModuleSystem | 本文的并列主题 |
| Java与数据库连接 | 045-JavaDatabaseConnection | 本文的并列主题 |
| Java 新特性与生态 | 046-JavaNewFeaturesEcosystem | 本文的并列主题 |
| 数组详解 | 047-ArrayDetailed | 本文的并列主题 |
| JVM调优 | 048-JVMtuning | 本文的性能延伸 |
| 集合框架详解 | 049-CollectionFrameworkDetailed | 本文的并列主题 |
| 并发编程详解 | 050-ConcurrencyDetailed | 本文的并列主题 |
| CompletableFuture异步编排 | 051-CompletableFutureAsync | 本文的并列主题 |
| ThreadLocal内存泄漏 | 052-ThreadLocalMemoryLeak | 本文的并列主题 |
| 反射与动态代理 | 053-ReflectionDynamicProxy | 本文的并列主题 |
| 注解处理器 | 054-AnnotationProcessor | 本文的并列主题 |
| 分代ZGC详解 | 055-GenerationalZGCDetailed | 本文的并列主题 |
| 面向对象编程 | 056-OOP | 本文的并列主题 |
| 抽象类与接口 | 057-AbstractClassInterface | 本文的并列主题 |
| 异常处理机制 | 058-ExceptionHandlingMechanism | 本文的原理深化 |
| 泛型详解 | 059-GenericDetailed | 本文的并列主题 |
| I/O 流与文件操作 | 060-IOStreamFileOperation | 本文的并列主题 |
| 多线程基础 | 061-MultithreadingBasics | 本文的前置基础 |
| JVM 内存模型 | 062-JVMMemoryModel | 本文的并列主题 |
| Lambda与函数式编程 | 063-LambdaFunctionalProgramming | 本文的并列主题 |
| Stream API | 064-StreamAPI | 本文的并列主题 |
| Spring Boot 学习笔记 | 065-SpringBootNotes | 本文的并列主题 |
| 网络编程 | 066-NetworkProgramming | 本文的并列主题 |
| Spring Cloud 微服务开发 | 067-SpringCloudMicroserviceDevelopment | 本文的并列主题 |
| Java Swing 图形界面 | 068-JavaSwingGUI | 本文的并列主题 |
| Java 项目示例：图书管理系统 | 069-JavaProjectExampleLibrarySystem | 本文的综合应用 |
| Java 理论知识点：JVM 原理、类加载机制与内存管理 | 070-JavaTheoryJVMClassLoadingMemory | 本文的原理深化 |
| Java NIO 通道与缓冲区 | 071-JavaNIOChannelBuffer | 本文的并列主题 |
| Java JDBC 数据库连接 | 072-JDBCDatabaseConnection | 本文自身 |
| Java Optional 类 | 073-JavaOptionalClass | 本文的并列主题 |
| Java Executor 与 ForkJoin | 074-ExecutorForkJoinPool | 本文的并列主题 |
| Java Path 与 Files 语法速查手册 | 075-JavaPathFiles | 本文的并列主题 |
| 启动 REPL 交互环境 | 076-JavaJshellJpackage | 本文的前置基础 |
| Java 同步器 CountDownLatch/CyclicBarrier/Phaser 语法速查手册 | 077-JavaCountDownLatchCyclicBarrier | 本文的并列主题 |
| Java 阻塞队列 BlockingQueue 语法速查手册 | 078-JavaBlockingQueue | 本文的并列主题 |
| Java try-with-resources 与异常链语法速查手册 | 079-JavaTryWithResources | 本文的并列主题 |
| Java HttpClient 与 WebSocket 语法速查手册 | 080-JavaHttpClientWebSocket | 本文的并列主题 |
| Java 时间格式化 DateTimeFormatter/ZoneId 语法速查手册 | 081-JavaTimeFormatting | 本文的并列主题 |
| Java 类型擦除与桥接方法语法速查手册 | 082-JavaTypeErasure | 本文的并列主题 |
| Java 枚举进阶 EnumSet/EnumMap/枚举单例语法速查手册 | 083-JavaEnumAdvanced | 本文的并列主题 |
| Java Iterator/Iterable/Spliterator 语法速查手册 | 084-JavaIteratorIterable | 本文的并列主题 |
| Java Comparator/Comparable 语法速查手册 | 085-JavaComparatorComparable | 本文的并列主题 |
| Java String.format/printf/MessageFormat 语法速查手册 | 086-JavaStringFormat | 本文的并列主题 |
| Java Arrays 工具类语法速查手册 | 087-JavaArraysUtility | 本文的并列主题 |
| Java Objects 工具类语法速查手册 | 088-JavaObjectsUtility | 本文的并列主题 |
| Java 命令行工具 javac/java/jar/jshell/jpackage 语法速查手册 | 089-JavaCommandLineTools | 本文的并列主题 |
| Maven pom.xml 配置语法速查手册 | 090-MavenPomConfiguration | 本文的并列主题 |
| Gradle build.gradle 配置语法速查手册 | 091-GradleBuildConfiguration | 本文的并列主题 |
