---
order: 740
title: Java Executor 与 ForkJoin
module: java

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
