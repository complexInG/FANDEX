---
order: 740
title: Java Executor 与 ForkJoin
module: 013-java
category: '013-java'
difficulty: beginner
description: Java Executor 与 ForkJoin 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## ExecutorService 创建

**基本写法：固定线程池**
`Executors.newFixedThreadPool(<线程数>);`
```java
// 创建固定大小线程池
ExecutorService pool = Executors.newFixedThreadPool(4);
```

---

**基本写法：缓存线程池**
`Executors.newCachedThreadPool();`
```java
// 按需创建线程的缓存池
ExecutorService pool = Executors.newCachedThreadPool();
```

---

**基本写法：单线程池**
`Executors.newSingleThreadExecutor();`
```java
// 单线程顺序执行
ExecutorService pool = Executors.newSingleThreadExecutor();
```

---

**基本写法：定时任务线程池**
`Executors.newScheduledThreadPool(<线程数>);`
```java
// 支持定时和周期任务的线程池
ScheduledExecutorService pool = Executors.newScheduledThreadPool(2);
```

---

**基本写法：虚拟线程池（Java 21+）**
`Executors.newVirtualThreadPerTaskExecutor();`
```java
// 每任务一虚拟线程的执行器
ExecutorService pool = Executors.newVirtualThreadPerTaskExecutor();
```

---

## 自定义 ThreadPoolExecutor

**基本写法：自定义线程池**
`new ThreadPoolExecutor(<核心>, <最大>, <空闲时长>, <单位>, <队列>);`
```java
// 自定义线程池参数
ThreadPoolExecutor pool = new ThreadPoolExecutor(
    2, 4, 60L, TimeUnit.SECONDS, new LinkedBlockingQueue<>(100));
```

---

**基本写法：自定义线程工厂**
`new ThreadPoolExecutor(<参数>, <队列>, <线程工厂>);`
```java
// 设置命名线程工厂便于排查
ThreadPoolExecutor pool = new ThreadPoolExecutor(
    2, 4, 60L, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(),
    new ThreadFactoryBuilder().setNameFormat("worker-%d").build());
```

---

**基本写法：自定义拒绝策略**
`new ThreadPoolExecutor(<参数>, <队列>, <工厂>, <拒绝策略>);`
```java
// 队列满时由调用线程执行
ThreadPoolExecutor pool = new ThreadPoolExecutor(
    2, 4, 60L, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(10),
    new ThreadPoolExecutor.CallerRunsPolicy());
```

---

## 提交任务

**基本写法：提交 Runnable**
`<pool>.submit(<Runnable>);`
```java
// 提交无返回值任务
Future<?> f = pool.submit(() -> doWork());
```

---

**基本写法：提交 Callable**
`<pool>.submit(<Callable>);`
```java
// 提交有返回值任务
Future<Integer> f = pool.submit(() -> compute());
```

---

**基本写法：批量提交**
`<pool>.invokeAll(<任务集合>);`
```java
// 批量提交并等待全部完成
List<Future<Integer>> futures = pool.invokeAll(tasks);
```

---

**基本写法：任一完成返回**
`<pool>.invokeAny(<任务集合>);`
```java
// 任一任务完成即返回结果
Integer r = pool.invokeAny(tasks);
```

---

## Future 操作

**基本写法：获取结果**
`<future>.get();`
```java
// 阻塞等待结果
Integer r = future.get();
```

---

**基本写法：超时获取**
`<future>.get(<超时>, <单位>);`
```java
// 最多等待 1 秒
Integer r = future.get(1, TimeUnit.SECONDS);
```

---

**基本写法：取消任务**
`<future>.cancel(<是否中断>);`
```java
// 中断运行中的任务
future.cancel(true);
```

---

**基本写法：判断完成**
`<future>.isDone();`
```java
// 判断任务是否完成
boolean done = future.isDone();
```

---

## 关闭线程池

**基本写法：优雅关闭**
`<pool>.shutdown();`
```java
// 不再接受新任务，等待已提交任务完成
pool.shutdown();
```

---

**基本写法：立即关闭**
`<pool>.shutdownNow();`
```java
// 尝试中断所有任务并返回未执行任务
List<Runnable> notRun = pool.shutdownNow();
```

---

**基本写法：等待终止**
`<pool>.awaitTermination(<超时>, <单位>);`
```java
// 等待关闭完成最多 60 秒
pool.awaitTermination(60, TimeUnit.SECONDS);
```

---

**基本写法：try-with-resources 关闭**
`try (ExecutorService pool = ...) { }`
```java
// Java 19+ 自动关闭执行器
try (ExecutorService pool = Executors.newVirtualThreadPerTaskExecutor()) {
    pool.submit(() -> doWork());
}
```

---

## ScheduledExecutorService 定时任务

**基本写法：延迟执行**
`<pool>.schedule(<任务>, <延迟>, <单位>);`
```java
// 延迟 5 秒后执行一次
pool.schedule(() -> doWork(), 5, TimeUnit.SECONDS);
```

---

**基本写法：固定速率周期**
`<pool>.scheduleAtFixedRate(<任务>, <初始延迟>, <周期>, <单位>);`
```java
// 每 10 秒执行一次
pool.scheduleAtFixedRate(() -> doWork(), 0, 10, TimeUnit.SECONDS);
```

---

**基本写法：固定延迟周期**
`<pool>.scheduleWithFixedDelay(<任务>, <初始延迟>, <间隔>, <单位>);`
```java
// 上次结束后 10 秒再执行
pool.scheduleWithFixedDelay(() -> doWork(), 0, 10, TimeUnit.SECONDS);
```

---

## ForkJoinPool

**基本写法：创建 ForkJoinPool**
`new ForkJoinPool(<并行度>);`
```java
// 创建并行度为 CPU 核数的 ForkJoinPool
ForkJoinPool pool = new ForkJoinPool(Runtime.getRuntime().availableProcessors());
```

---

**基本写法：提交 RecursiveTask**
`<pool>.invoke(<任务>);`
```java
// 提交有返回值的分治任务
Integer r = pool.invoke(new SumTask(0, 1000));
```

---

**基本写法：提交 RecursiveAction**
`<pool>.execute(<任务>);`
```java
// 提交无返回值的分治任务
pool.execute(new PrintTask(0, 100));
```

---

## RecursiveTask 分治

**基本写法：继承 RecursiveTask**
`class <类> extends RecursiveTask<<返回类型>> { protected <类型> compute() {} }`
```java
// 分治任务带返回值
class SumTask extends RecursiveTask<Integer> {
    private final int start, end;
    protected Integer compute() {
        if (end - start < 100) return start + end;
        SumTask left = new SumTask(start, (start + end) / 2);
        SumTask right = new SumTask((start + end) / 2 + 1, end);
        left.fork();
        return right.compute() + left.join();
    }
}
```

---

**基本写法：fork 异步执行**
`<task>.fork();`
```java
// 异步提交子任务
left.fork();
```

---

**基本写法：join 等待结果**
`<task>.join();`
```java
// 阻塞等待子任务结果
int r = left.join();
```

---

## 并行流底层

**基本写法：并行流使用 ForkJoinPool**
`<集合>.parallelStream().<操作>`
```java
// 并行流默认使用公共 ForkJoinPool
list.parallelStream().mapToInt(Integer::intValue).sum();
```

---

## CompletionService

**基本写法：按完成顺序获取**
`new ExecutorCompletionService<<类型>>(<pool>);`
```java
// 按完成顺序获取结果
CompletionService<Integer> cs = new ExecutorCompletionService<>(pool);
cs.submit(() -> compute());
Future<Integer> f = cs.take();
Integer r = f.get();
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
| Java Executor 与 ForkJoin | 074-ExecutorForkJoinPool | 本文自身 |
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
