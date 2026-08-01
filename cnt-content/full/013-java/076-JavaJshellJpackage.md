---
order: 760
title: 启动 REPL 交互环境
module: java

category: '013-java'
difficulty: beginner
description: 启动 REPL 交互环境 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

﻿# Java jshell 与 jpackage 命令速查手册

---

## jshell 启动

**基本写法：进入交互**
`jshell`
```bash
# 启动 REPL 交互环境
jshell
```

---

**基本写法：指定版本进入**
`jshell --execution <模式>`
```bash
# 本地执行模式
jshell --execution local
```

---

**基本写法：执行片段**
`jshell -e "<代码>"`
```bash
# 直接执行单段代码
jshell -e "System.out.println(\"hi\");"
```

---

## jshell 会话控制

**基本写法：加载文件**
`/open <文件路径>`
```java
// 在 jshell 内加载脚本文件
/open snippet.java
```

---

**基本写法：保存片段**
`/save <文件路径>`
```java
// 保存当前会话片段到文件
/save session.java
```

---

**基本写法：列出片段**
`/list`
```java
// 列出已输入的代码片段（带编号）
/list
// 仅列出有效片段
/list -all
```

---

**基本写法：查看变量**
`/vars`
```java
// 列出已定义的变量及值
/vars
```

---

**基本写法：查看方法**
`/methods`
```java
// 列出已定义的方法
/methods
```

---

**基本写法：查看类型**
`/types`
```java
// 列出已定义的类与接口
/types
```

---

**基本写法：查看导入**
`/imports`
```java
// 列出已导入的包
/imports
```

---

**基本写法：编辑片段**
`/edit <片段编号>`
```java
// 用外部编辑器编辑片段
/edit 1
```

---

**基本写法：重置会话**
`/reset`
```java
// 清空所有片段，重新开始
/reset
```

---

**基本写法：退出**
`/exit`
```java
// 退出 jshell
/exit
```

---

## jshell 设置

**基本写法：设置反馈模式**
`/set feedback <模式>`
```java
// concise / normal / silent / verbose
/set feedback verbose
```

---

**基本写法：添加导入**
`import <包名>;`
```java
// 直接输入 import 语句即可
import java.util.stream.*;
```

---

**基本写法：执行外部命令**
`/!<shell 命令>`
```java
// 在 jshell 中执行系统命令
/! javac -version
```

---

**基本写法：设置类路径**
`jshell --class-path <路径>`
```bash
# 启动时指定类路径
jshell --class-path "lib/*;bin"
```

---

## jpackage 基础

**基本写法：构建 Windows 安装包**
`jpackage --name <名称> --input <输入> --main-jar <主jar>`
```bash
# 打包成 Windows 安装程序（msi/exe）
jpackage --name MyApp --input target --main-jar app.jar
```

---

**基本写法：指定主类**
`jpackage --name <名称> --module <模块>/<主类>`
```bash
# 模块化应用打包
jpackage --name MyApp --module com.example.app/com.example.app.Main
```

---

**基本写法：指定运行时镜像**
`jpackage --runtime-image <镜像目录>`
```bash
# 使用自定义 JRE
jpackage --name MyApp --input target --main-jar app.jar --runtime-image myjre
```

---

## jpackage 平台选项

**基本写法：Windows 安装器类型**
`jpackage --win-msi`
```bash
# 生成 MSI 安装包
jpackage --name MyApp --input target --main-jar app.jar --win-msi
```

---

**基本写法：Windows 快捷方式**
`jpackage --win-shortcut --win-menu`
```bash
# 创建桌面快捷方式与开始菜单项
jpackage --name MyApp --input target --main-jar app.jar --win-shortcut --win-menu
```

---

**基本写法：macOS dmg**
`jpackage --type dmg --name <名称>`
```bash
# 生成 macOS dmg 镜像
jpackage --type dmg --name MyApp --module com.example.app/com.example.app.Main
```

---

**基本写法：macOS 应用图标**
`jpackage --icon <icns 文件>`
```bash
# 指定应用图标
jpackage --name MyApp --input target --main-jar app.jar --icon icon.icns
```

---

**基本写法：Linux deb/rpm**
`jpackage --type <deb|rpm>`
```bash
# 生成 Linux 安装包
jpackage --type deb --name myapp --input target --main-jar app.jar
```

---

## jpackage 应用配置

**基本写法：设置版本与供应商**
`jpackage --app-version <版本> --vendor <供应商>`
```bash
# 应用版本与供应商
jpackage --name MyApp --input target --main-jar app.jar \
    --app-version 1.0.0 --vendor "Acme Inc"
```

---

**基本写法：传入 JVM 参数**
`jpackage --java-options "<参数>"`
```bash
# 启动时传入 JVM 参数
jpackage --name MyApp --input target --main-jar app.jar \
    --java-options "-Xmx512m -Dfile.encoding=UTF-8"
```

---

**基本写法：应用参数**
`jpackage --arguments "<参数>"`
```bash
# 启动应用时传入的命令行参数
jpackage --name MyApp --input target --main-jar app.jar \
    --arguments "--mode=prod"
```

---

**基本写法：关联文件类型**
`jpackage --file-associations <属性文件>`
```bash
# 关联文件扩展名
jpackage --name MyApp --input target --main-jar app.jar \
    --file-associations app.properties
```

---

**基本写法：添加资源**
`jpackage --resource-dir <目录>`
```bash
# 指定图标与许可文件目录
jpackage --name MyApp --input target --main-jar app.jar \
    --resource-dir res
```

---

**基本写法：临时目录与详细输出**
`jpackage --temp <目录> --verbose`
```bash
# 指定临时目录并输出详细信息
jpackage --name MyApp --input target --main-jar app.jar \
    --temp build/tmp --verbose
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
| Java JDBC 数据库连接 | 072-JDBCDatabaseConnection | 本文的并列主题 |
| Java Optional 类 | 073-JavaOptionalClass | 本文的并列主题 |
| Java Executor 与 ForkJoin | 074-ExecutorForkJoinPool | 本文的并列主题 |
| Java Path 与 Files 语法速查手册 | 075-JavaPathFiles | 本文的并列主题 |
| 启动 REPL 交互环境 | 076-JavaJshellJpackage | 本文自身 |
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
