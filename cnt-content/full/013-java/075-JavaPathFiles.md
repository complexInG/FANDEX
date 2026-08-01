---
order: 750
title: Java Path 与 Files 语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java Path 与 Files 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Path 创建

**基本写法：从字符串创建**
`Path.of(<路径字符串>);`
```java
// Java 11+，等价于 Paths.get
Path p = Path.of("C:\\data\\file.txt");
```

---

**基本写法：从多段创建**
`Path.of(<根>, <段1>, <段2>);`
```java
// 拼接路径段
Path p = Path.of("C:", "data", "sub", "file.txt");
```

---

**基本写法：Paths.get**
`Paths.get(<路径字符串>);`
```java
// NIO.2 传统方式
Path p = Paths.get("/var/log/app.log");
```

---

**基本写法：从 URI 创建**
`Paths.get(<URI>);`
```java
// 通过 URI 创建
Path p = Paths.get(URI.create("file:///C:/data/file.txt"));
```

---

## Path 操作

**基本写法：拼接路径**
`<Path>.resolve(<子路径>);`
```java
// 拼接子路径
Path dir = Path.of("C:\\data");
Path file = dir.resolve("file.txt");
```

---

**基本写法：相对化**
`<Path>.relativize(<目标>);`
```java
// 求相对路径
Path a = Path.of("C:\\data\\sub");
Path b = Path.of("C:\\data\\other\\f.txt");
Path r = a.relativize(b);
```

---

**基本写法：规范化**
`<Path>.normalize();`
```java
// 消除 . 和 ..
Path p = Path.of("C:\\data\\..\\file.txt").normalize();
```

---

**基本写法：转绝对路径**
`<Path>.toAbsolutePath();`
```java
// 转换为绝对路径
Path p = Path.of("file.txt").toAbsolutePath();
```

---

**基本写法：访问路径组件**
`<Path>.getFileName();`
```java
// 获取文件名、父路径、根
Path p = Path.of("C:\\data\\file.txt");
p.getFileName();   // file.txt
p.getParent();     // C:\data
p.getRoot();       // C:\
```

---

## Files 文件操作

**基本写法：判断存在**
`Files.exists(<Path>);`
```java
// 判断文件是否存在
boolean ok = Files.exists(Path.of("a.txt"));
```

---

**基本写法：创建文件**
`Files.createFile(<Path>);`
```java
// 创建空文件
Files.createFile(Path.of("new.txt"));
```

---

**基本写法：创建目录**
`Files.createDirectory(<Path>);`
```java
// 创建单层目录
Files.createDirectory(Path.of("C:\\newdir"));
```

---

**基本写法：递归创建目录**
`Files.createDirectories(<Path>);`
```java
// 创建多层目录
Files.createDirectories(Path.of("C:\\a\\b\\c"));
```

---

**基本写法：删除文件**
`Files.delete(<Path>);`
```java
// 删除，不存在则抛异常
Files.delete(Path.of("old.txt"));
```

---

**基本写法：删除不存在不报错**
`Files.deleteIfExists(<Path>);`
```java
// 不存在时返回 false
boolean deleted = Files.deleteIfExists(Path.of("old.txt"));
```

---

**基本写法：复制文件**
`Files.copy(<源>, <目标>);`
```java
// 复制文件
Files.copy(Path.of("a.txt"), Path.of("b.txt"));
```

---

**基本写法：覆盖复制**
`Files.copy(<源>, <目标>, StandardCopyOption.REPLACE_EXISTING);`
```java
// 覆盖已存在目标
Files.copy(Path.of("a.txt"), Path.of("b.txt"),
    StandardCopyOption.REPLACE_EXISTING);
```

---

**基本写法：移动/重命名**
`Files.move(<源>, <目标>);`
```java
// 移动或重命名
Files.move(Path.of("a.txt"), Path.of("dir/a.txt"));
```

---

## 文件读写

**基本写法：读全部字节**
`Files.readAllBytes(<Path>);`
```java
// 读取整个文件为字节数组
byte[] data = Files.readAllBytes(Path.of("a.dat"));
```

---

**基本写法：读全部行**
`Files.readAllLines(<Path>);`
```java
// 读取所有行
List<String> lines = Files.readAllLines(Path.of("a.txt"));
```

---

**基本写法：读字符串**
`Files.readString(<Path>);`
```java
// Java 11+，读取为字符串
String text = Files.readString(Path.of("a.txt"));
```

---

**基本写法：写字符串**
`Files.writeString(<Path>, <内容>);`
```java
// Java 11+，写入字符串
Files.writeString(Path.of("a.txt"), "hello");
```

---

**基本写法：写行集合**
`Files.write(<Path>, <Iterable>);`
```java
// 写入多行
Files.write(Path.of("a.txt"), List.of("a", "b", "c"));
```

---

**基本写法：追加写入**
`Files.writeString(<Path>, <内容>, StandardOpenOption.APPEND);`
```java
// 追加到文件末尾
Files.writeString(Path.of("a.txt"), "more",
    StandardOpenOption.APPEND);
```

---

## 流式读写

**基本写法：行流**
`Files.lines(<Path>);`
```java
// 按行流式读取，需 try-with-resources
try (Stream<String> s = Files.lines(Path.of("big.log"))) {
    s.filter(l -> l.contains("ERROR")).forEach(System.out::println);
}
```

---

**基本写法：列出目录**
`Files.list(<Path>);`
```java
// 列出直接子项
try (Stream<Path> s = Files.list(Path.of("C:\\data"))) {
    s.forEach(System.out::println);
}
```

---

**基本写法：遍历目录树**
`Files.walk(<Path>, <深度>);`
```java
// 深度遍历
try (Stream<Path> s = Files.walk(Path.of("C:\\data"), 3)) {
    s.filter(Files::isRegularFile).forEach(System.out::println);
}
```

---

**基本写法：按 glob 查找**
`Files.find(<Path>, <深度>, <匹配器>);`
```java
// 按条件查找
try (Stream<Path> s = Files.find(Path.of("C:\\data"), 5,
        (p, a) -> p.toString().endsWith(".log"))) {
    s.forEach(System.out::println);
}
```

---

## 文件属性

**基本写法：基本属性**
`Files.size(<Path>);`
```java
// 文件大小（字节）
long size = Files.size(Path.of("a.txt"));
```

---

**基本写法：判断类型**
`Files.isDirectory(<Path>);`
```java
// 判断目录/文件/符号链接
boolean dir = Files.isDirectory(Path.of("C:\\data"));
boolean reg = Files.isRegularFile(Path.of("a.txt"));
boolean lnk = Files.isSymbolicLink(Path.of("link"));
```

---

**基本写法：读取属性对象**
`Files.readAttributes(<Path>, <属性类>);`
```java
// 一次性读取基本属性
BasicFileAttributes attrs = Files.readAttributes(
    Path.of("a.txt"), BasicFileAttributes.class);
attrs.size();
attrs.lastModifiedTime();
```

---

**基本写法：创建符号链接**
`Files.createSymbolicLink(<链接>, <目标>);`
```java
// 创建符号链接
Files.createSymbolicLink(Path.of("link.txt"), Path.of("a.txt"));
```

---

## PathMatcher 路径匹配

**基本写法：创建匹配器**
`FileSystems.getDefault().getPathMatcher("<语法>:<模式>");`
```java
// 创建 glob 路径匹配器
PathMatcher m = FileSystems.getDefault().getPathMatcher("glob:**/*.java");
// 也可使用 regex 语法
PathMatcher r = FileSystems.getDefault().getPathMatcher("regex:.*\\.java$");
```

---

**基本写法：匹配路径**
`<matcher>.matches(<Path>);`
```java
// 判断路径是否匹配
boolean ok = m.matches(Path.of("src/Main.java"));
```

---

**基本写法：glob 语法要点**
```java
// **   匹配任意层级目录
// *    匹配任意字符（不含目录分隔符）
// ?    匹配单个字符
// {}   逗号分隔的多个选项
PathMatcher m = FileSystems.getDefault().getPathMatcher("glob:*.{java,txt}");
```

---

## FileVisitor 递归

**基本写法：递归遍历回调**
`Files.walkFileTree(<Path>, <Visitor>);`
```java
// 自定义递归访问
Files.walkFileTree(Path.of("C:\\data"), new SimpleFileVisitor<>() {
    @Override public FileVisitResult visitFile(Path f, BasicFileAttributes a) {
        System.out.println(f);
        return FileVisitResult.CONTINUE;
    }
});
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
| Java JDBC 数据库连接 | 072-JDBCDatabaseConnection | 本文的并列主题 |
| Java Optional 类 | 073-JavaOptionalClass | 本文的并列主题 |
| Java Executor 与 ForkJoin | 074-ExecutorForkJoinPool | 本文的并列主题 |
| Java Path 与 Files 语法速查手册 | 075-JavaPathFiles | 本文自身 |
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
