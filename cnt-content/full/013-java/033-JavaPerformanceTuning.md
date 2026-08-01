---
order: 76
title: Java性能调优
module: java
category: Java
difficulty: advanced
description: Java应用性能优化
author: fanquanpp
updated: '2026-08-01'
related:
  - java/Java与Docker
  - java/Java与GraphQL
  - java/Java与AI
  - java/Java与安全
prerequisites:
  - java/概述与开发环境
---

## 概述

Java 性能调优是在应用满足功能需求之后，通过分析瓶颈、调整参数、优化代码来提升响应速度和吞吐量的过程。性能问题通常不会在开发阶段暴露，而是在高并发、大数据量的生产环境中才显现。因此，掌握性能调优的方法论比记住具体的参数更重要。

性能调优不是盲目修改配置，而是"先测量，再优化"。你需要先确定瓶颈在哪里（CPU、内存、IO、锁竞争），然后针对性地优化，最后验证优化效果。没有测量数据的调优只是猜测。

## 基础概念

### 性能指标

衡量 Java 应用性能的几个核心指标：

- **响应时间**：单个请求从发出到返回的时间，通常关注 P99（99% 的请求在多少时间内完成）
- **吞吐量**：单位时间内处理的请求数量，通常用 QPS（每秒查询数）衡量
- **GC 停顿**：垃圾回收导致的应用暂停时间，直接影响响应时间的稳定性
- **内存使用**：堆内存的占用情况和分配速率，影响 GC 频率

### 性能瓶颈的常见来源

- **CPU 密集**：计算量过大，算法效率低
- **内存分配过快**：短生命周期对象太多，GC 压力大
- **IO 阻塞**：数据库查询慢、网络延迟高、磁盘读写慢
- **锁竞争**：多线程争抢同一把锁，导致线程等待
- **连接池不足**：数据库连接或 HTTP 连接不够用，请求排队

### 调优的一般流程

1. 建立基准：用压测工具测量当前性能
2. 监控分析：用工具找到瓶颈所在
3. 提出假设：根据分析结果猜测原因
4. 实施优化：修改代码或配置
5. 验证效果：再次压测，对比数据
6. 重复以上步骤

## 快速上手

### 使用 JFR 记录性能数据

Java Flight Recorder（JFR）是 JDK 内置的性能分析工具，对应用影响极小（通常低于 2%），适合在生产环境使用：

```bash
# 启动应用时开启 JFR
java -XX:StartFlightRecording=duration=60s,filename=app.jfr -jar myapp.jar

# 或者在运行中的应用上动态开启
jcmd <pid> JFR.start duration=60s filename=app.jfr
```

使用 JDK Mission Control（JMC）打开 app.jfr 文件，可以查看 CPU 热点、内存分配、GC 事件、线程阻塞等信息。

### 使用 async-profiler 分析 CPU 热点

async-profiler 是一个低开销的 CPU 和内存分析工具，能准确找到最耗时的方法：

```bash
# 分析 CPU 使用情况，持续 30 秒
java -jar async-profiler.jar -d 30 -f cpu.html <pid>

# 分析内存分配
java -jar async-profiler.jar -d 30 -e alloc -f alloc.html <pid>
```

生成的 HTML 文件包含火焰图，直观展示哪些方法占用了最多 CPU 时间。

## 详细用法

### 1. JVM 内存调优

JVM 内存分为堆（Heap）和非堆（Non-heap）。堆用于存储对象实例，非堆包括方法区（元空间）、线程栈、直接内存等。

```bash
# 基本内存参数
java -Xms2g -Xmx2g \        # 初始堆大小和最大堆大小设为相同，避免动态扩容
     -XX:MetaspaceSize=256m \ # 元空间初始大小
     -XX:MaxMetaspaceSize=256m \ # 元空间最大大小
     -jar myapp.jar
```

为什么要把 -Xms 和 -Xmx 设为相同？因为堆从较小值扩展到较大值时需要 Full GC，这个过程会暂停应用。设为相同值可以避免这种动态调整带来的停顿。

### 2. 垃圾回收器选择

JDK 8 默认使用 Parallel GC，JDK 9+ 默认使用 G1 GC。不同场景适合不同的 GC：

```bash
# G1 GC：适合大多数服务端应用，平衡吞吐量和延迟
java -XX:+UseG1GC \
     -XX:MaxGCPauseMillis=200 \ # 目标最大停顿时间 200ms
     -XX:G1HeapRegionSize=8m \   # Region 大小
     -jar myapp.jar

# ZGC：适合需要极低延迟的应用（JDK 15+ 生产可用）
java -XX:+UseZGC \
     -XX:MaxGCPauseMillis=10 \  # 目标最大停顿时间 10ms
     -Xmx4g \
     -jar myapp.jar

# Parallel GC：适合批处理任务，追求最大吞吐量
java -XX:+UseParallelGC \
     -XX:ParallelGCThreads=4 \  # GC 线程数
     -jar myapp.jar
```

如何选择？如果应用对延迟敏感（如 Web 服务），选 G1 或 ZGC；如果应用是批处理任务（如数据分析），选 Parallel GC。

### 3. 字符串优化

字符串拼接是 Java 中最常见的性能陷阱之一：

```java
// 错误：循环中使用 + 拼接字符串，每次都创建新对象
String result = "";
for (String item : items) {
    result += item;  // 每次循环都创建一个新的 String 对象
}

// 正确：使用 StringBuilder
StringBuilder sb = new StringBuilder();
for (String item : items) {
    sb.append(item);  // 在内部缓冲区追加，不创建新对象
}
String result = sb.toString();

// 更好：如果只是拼接已知数量的字符串，直接用 + 即可
// 编译器会自动优化为 StringBuilder
String greeting = "Hello, " + name + "!";  // 这没问题
```

### 4. 集合优化

选择合适的集合类型和初始容量可以减少扩容开销：

```java
import java.util.ArrayList;
import java.util.HashMap;

// 指定初始容量，避免扩容
// ArrayList 每次扩容会增加 50%，涉及数组拷贝
List<String> list = new ArrayList<>(1000);  // 如果知道大概有多少元素

// HashMap 默认容量 16，负载因子 0.75，超过容量*负载因子就扩容
// 扩容需要重新计算所有键的哈希位置，代价很高
Map<String, String> map = new HashMap<>(1024);  // 预分配足够容量

// 使用基本类型集合避免自动装箱
// 错误：大量 Integer 对象的创建和销毁
Map<Integer, String> map = new HashMap<>();  // int 会被装箱为 Integer

// 如果使用第三方库，可以用 Trove 或 Eclipse Collections 的基本类型集合
// TIntObjectMap<String> map = new TIntObjectHashMap<>();
```

### 5. 线程池优化

线程池的大小直接影响并发性能。线程太少会浪费 CPU，太多会导致上下文切换开销：

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;

// CPU 密集型任务：线程数 = CPU 核心数 + 1
int cpuCores = Runtime.getRuntime().availableProcessors();
ExecutorService cpuPool = Executors.newFixedThreadPool(cpuCores + 1);

// IO 密集型任务：线程数 = CPU 核心数 * 2（或更多）
ExecutorService ioPool = Executors.newFixedThreadPool(cpuCores * 2);

// 自定义线程池（更灵活）
ThreadPoolExecutor customPool = new ThreadPoolExecutor(
    4,                                  // 核心线程数
    8,                                  // 最大线程数
    60, TimeUnit.SECONDS,               // 空闲线程存活时间
    new LinkedBlockingQueue<>(1000),    // 任务队列容量
    new ThreadPoolExecutor.CallerRunsPolicy()  // 队列满时由调用线程执行
);
```

### 6. 数据库访问优化

数据库访问通常是 Java 应用最大的性能瓶颈：

```java
import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.PreparedStatement;

// 使用连接池，不要每次创建新连接
// HikariCP 是性能最好的连接池
// spring.datasource.hikari.maximum-pool-size=20

// 使用 PreparedStatement 防止 SQL 注入，同时可以利用查询缓存
String sql = "SELECT * FROM users WHERE id = ?";
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setLong(1, userId);
    // 执行查询...
}

// 批量操作代替循环单条操作
String insertSql = "INSERT INTO orders (user_id, amount) VALUES (?, ?)";
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement(insertSql)) {
    for (Order order : orders) {
        ps.setLong(1, order.getUserId());
        ps.setBigDecimal(2, order.getAmount());
        ps.addBatch();  // 添加到批次
    }
    ps.executeBatch();  // 一次性执行所有插入
}
```

### 7. 缓存优化

缓存是减少重复计算和数据库访问的最有效手段：

```java
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.TimeUnit;

// 简单的本地缓存
public class LocalCache<V> {
    private final ConcurrentHashMap<String, CacheEntry<V>> cache = new ConcurrentHashMap<>();
    private final long ttlMillis;  // 缓存过期时间

    public LocalCache(long ttlMillis) {
        this.ttlMillis = ttlMillis;
    }

    public V get(String key) {
        CacheEntry<V> entry = cache.get(key);
        if (entry != null && !entry.isExpired()) {
            return entry.value;
        }
        return null;
    }

    public void put(String key, V value) {
        cache.put(key, new CacheEntry<>(value, System.currentTimeMillis() + ttlMillis));
    }

    private static class CacheEntry<V> {
        final V value;
        final long expireTime;

        CacheEntry(V value, long expireTime) {
            this.value = value;
            this.expireTime = expireTime;
        }

        boolean isExpired() {
            return System.currentTimeMillis() > expireTime;
        }
    }
}
```

## 常见场景

### 场景一：接口响应慢

排查接口响应慢的标准流程：

```bash
# 第一步：查看 GC 日志，排除 GC 停顿的影响
java -Xlog:gc*:file=gc.log -jar myapp.jar

# 第二步：用 async-profiler 找到 CPU 热点
java -jar async-profiler.jar -d 30 -f cpu.html <pid>

# 第三步：查看数据库慢查询日志
# 第四步：检查是否有锁竞争（JFR 的 Thread Blocking 事件）
```

### 场景二：内存泄漏

内存泄漏的表现是应用运行一段时间后越来越慢，最终 OOM：

```bash
# 第一步：用 jmap 导出堆转储
jmap -dump:live,format=b,file=heap.hprof <pid>

# 第二步：用 MAT（Memory Analyzer Tool）分析堆转储
# 查找占用内存最大的对象，追踪 GC Roots 引用链

# 第三步：常见内存泄漏原因
# - 静态集合不断添加元素但从不清理
# - 未关闭的资源（连接、流）
# - 监听器/回调未注销
# - ThreadLocal 未清理
```

### 场景三：高并发下的线程问题

```java
// 错误：使用 synchronized 导致所有线程串行执行
public synchronized User getUser(Long id) {
    return userRepository.findById(id);
}

// 正确：缩小锁的范围，或使用并发集合
private final ConcurrentHashMap<Long, User> cache = new ConcurrentHashMap<>();

public User getUser(Long id) {
    // 使用 ConcurrentHashMap 的原子操作
    return cache.computeIfAbsent(id, key -> userRepository.findById(key));
}
```

## 注意事项与常见错误

### 过早优化

不要在没有性能数据的情况下优化代码。先让代码正确运行，再根据实际瓶颈优化。Donald Knuth 说过："过早优化是万恶之源。"

### 忽略 GC 日志

生产环境一定要开启 GC 日志，否则无法排查 GC 相关的问题：

```bash
# JDK 9+ 的 GC 日志参数
java -Xlog:gc*:file=gc.log:time,uptime:filecount=5,filesize=10m -jar myapp.jar
```

### 盲目调大内存

堆内存不是越大越好。堆越大，Full GC 的停顿时间越长。如果应用只需要 2GB 内存，设置 8GB 反而可能导致更长的 GC 停顿。应该根据实际需要设置合理的堆大小。

### 忽略连接池配置

数据库连接池、HTTP 连接池的配置对性能影响很大。连接数太少会导致请求排队，太多会压垮数据库。一般建议数据库连接池大小为 CPU 核心数 \* 2 + 有效磁盘数。

## 进阶用法

### JIT 编译优化

JIT（Just-In-Time）编译器会将热点代码编译为本地机器码，大幅提升执行速度。了解 JIT 行为有助于理解某些性能现象：

```bash
# 查看 JIT 编译日志
java -XX:+PrintCompilation -jar myapp.jar

# 查看内联情况
java -XX:+PrintInlining -jar myapp.jar

# 禁用 JIT（用于对比测试）
java -Xint -jar myapp.jar  # 纯解释执行，速度会慢很多
```

### 使用 JMH 做微基准测试

JMH（Java Microbenchmark Harness）是 OpenJDK 提供的微基准测试框架，用于准确测量小段代码的性能：

```java
import org.openjdk.jmh.annotations.*;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)       // 测量平均执行时间
@OutputTimeUnit(TimeUnit.NANOSECONDS)  // 时间单位纳秒
@State(Scope.Thread)                   // 每个线程独立的状态
public class StringBenchmark {

    private String prefix = "Hello";
    private String name = "World";

    @Benchmark
    public String stringConcat() {
        return prefix + ", " + name + "!";
    }

    @Benchmark
    public String stringBuilder() {
        StringBuilder sb = new StringBuilder();
        sb.append(prefix).append(", ").append(name).append("!");
        return sb.toString();
    }
}
```

### 容器环境下的内存配置

在 Docker 容器中运行 Java 应用时，需要正确配置内存限制：

```bash
# JDK 10+ 会自动识别容器内存限制
# JDK 8u191+ 需要手动开启
java -XX:+UseContainerSupport \
     -XX:MaxRAMPercentage=75.0 \  # 使用容器内存的 75% 作为堆
     -jar myapp.jar
```

不要用 -Xmx 指定固定值，因为容器的内存限制可能变化。使用 -XX:MaxRAMPercentage 更灵活。

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
| Java性能调优 | 033-JavaPerformanceTuning | 本文自身 |
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
