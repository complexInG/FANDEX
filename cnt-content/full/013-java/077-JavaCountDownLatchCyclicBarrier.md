---
order: 770
title: Java 同步器 CountDownLatch/CyclicBarrier/Phaser 语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java 同步器 CountDownLatch/CyclicBarrier/Phaser 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## CountDownLatch 一次性倒数

**基本写法：创建倒数器**
`new CountDownLatch(<计数>);`
```java
// 创建计数为 3 的倒数器
CountDownLatch latch = new CountDownLatch(3);
```

---

**基本写法：计数减一**
`<latch>.countDown();`
```java
// 计数减 1
latch.countDown();
```

---

**基本写法：等待计数归零**
`<latch>.await();`
```java
// 阻塞直到计数归零
latch.await();
```

---

**基本写法：超时等待**
`<latch>.await(<超时>, <单位>);`
```java
// 最多等待 5 秒
boolean ok = latch.await(5, TimeUnit.SECONDS);
```

---

**基本写法：获取剩余计数**
`<latch>.getCount();`
```java
// 查询当前剩余计数
long rest = latch.getCount();
```

---

## CyclicBarrier 可循环屏障

**基本写法：创建屏障**
`new CyclicBarrier(< parties >);`
```java
// 创建 3 个线程同步的屏障
CyclicBarrier barrier = new CyclicBarrier(3);
```

---

**基本写法：带动作的屏障**
`new CyclicBarrier(< parties >, <Runnable>);`
```java
// 所有线程到达后执行的动作
CyclicBarrier b = new CyclicBarrier(3, () -> System.out.println("all arrived"));
```

---

**基本写法：等待**
`<barrier>.await();`
```java
// 等待其他线程到达
barrier.await();
```

---

**基本写法：超时等待**
`<barrier>.await(<超时>, <单位>);`
```java
// 最多等待 10 秒
int idx = barrier.await(10, TimeUnit.SECONDS);
```

---

**基本写法：重置屏障**
`<barrier>.reset();`
```java
// 重置屏障以便复用
barrier.reset();
```

---

## Phaser 阶段同步器

**基本写法：创建 Phaser**
`new Phaser(< parties >);`
```java
// 创建包含 3 个参与者的 Phaser
Phaser phaser = new Phaser(3);
```

---

**基本写法：注册参与者**
`<phaser>.register();`
```java
// 动态注册一个参与者
phaser.register();
```

---

**基本写法：到达并等待**
`<phaser>.arriveAndAwaitAdvance();`
```java
// 到达当前阶段并等待其他人
int phase = phaser.arriveAndAwaitAdvance();
```

---

**基本写法：到达并注销**
`<phaser>.arriveAndDeregister();`
```java
// 到达并从后续阶段注销自己
phaser.arriveAndDeregister();
```

---

**基本写法：获取当前阶段**
`<phaser>.getPhase();`
```java
// 查询当前阶段编号
int phase = phaser.getPhase();
```

---

## Exchanger 交换器

**基本写法：创建交换器**
`new Exchanger<<类型>>();`
```java
// 创建字符串交换器
Exchanger<String> ex = new Exchanger<>();
```

---

**基本写法：交换数据**
`<exchanger>.exchange(<数据>);`
```java
// 与另一线程交换数据并返回对方的数据
String other = ex.exchange("mine");
```

---

**基本写法：超时交换**
`<exchanger>.exchange(<数据>, <超时>, <单位>);`
```java
// 最多等待 5 秒
String other = ex.exchange("mine", 5, TimeUnit.SECONDS);
```

---

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
