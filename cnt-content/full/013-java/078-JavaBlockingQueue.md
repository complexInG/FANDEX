---
order: 780
title: Java 阻塞队列 BlockingQueue 语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java 阻塞队列 BlockingQueue 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## ArrayBlockingQueue 有界数组队列

**基本写法：创建有界队列**
`new ArrayBlockingQueue<<类型>>(<容量>);`
```java
// 创建容量 100 的有界阻塞队列
ArrayBlockingQueue<String> q = new ArrayBlockingQueue<>(100);
```

---

**基本写法：公平队列**
`new ArrayBlockingQueue<<类型>>(<容量>, true);`
```java
// 使用公平锁的队列
ArrayBlockingQueue<String> q = new ArrayBlockingQueue<>(100, true);
```

---

## LinkedBlockingQueue 链式队列

**基本写法：创建链式队列**
`new LinkedBlockingQueue<<类型>>();`
```java
// 创建默认容量 Integer.MAX_VALUE 的链式队列
LinkedBlockingQueue<String> q = new LinkedBlockingQueue<>();
```

---

**基本写法：指定容量**
`new LinkedBlockingQueue<<类型>>(<容量>);`
```java
// 创建容量 1000 的链式队列
LinkedBlockingQueue<String> q = new LinkedBlockingQueue<>(1000);
```

---

## SynchronousQueue 同步队列

**基本写法：创建同步队列**
`new SynchronousQueue<<类型>>();`
```java
// 每个 put 必须等待一个 take
SynchronousQueue<String> q = new SynchronousQueue<>();
```

---

## PriorityBlockingQueue 优先级队列

**基本写法：创建优先级队列**
`new PriorityBlockingQueue<<类型>>();`
```java
// 自然顺序的优先级队列
PriorityBlockingQueue<Integer> q = new PriorityBlockingQueue<>();
```

---

**基本写法：带比较器**
`new PriorityBlockingQueue<<类型>>(<初始容量>, <比较器>);`
```java
// 自定义比较器
PriorityBlockingQueue<String> q = new PriorityBlockingQueue<>(11, Comparator.reverseOrder());
```

---

## DelayQueue 延迟队列

**基本写法：创建延迟队列**
`new DelayQueue<<类型>>();`
```java
// 元素必须实现 Delayed 接口
DelayQueue<DelayedTask> q = new DelayQueue<>();
```

---

## 通用操作

**基本写法：阻塞入队**
`<queue>.put(<元素>);`
```java
// 队列满时阻塞
q.put("item");
```

---

**基本写法：阻塞出队**
`<queue>.take();`
```java
// 队列空时阻塞
String item = q.take();
```

---

**基本写法：offer 超时入队**
`<queue>.offer(<元素>, <超时>, <单位>);`
```java
// 最多等待 5 秒
boolean ok = q.offer("item", 5, TimeUnit.SECONDS);
```

---

**基本写法：poll 超时出队**
`<queue>.poll(<超时>, <单位>);`
```java
// 最多等待 5 秒取元素
String item = q.poll(5, TimeUnit.SECONDS);
```

---

**基本写法：剩余容量**
`<queue>.remainingCapacity();`
```java
// 查询剩余容量
int cap = q.remainingCapacity();
```

---

## 生产者消费者示例

**基本写法：阻塞队列用作通道**
```java
BlockingQueue<String> queue = new LinkedBlockingQueue<>(10);
// 生产者
new Thread(() -> { for (int i = 0; i < 5; i++) queue.put("p" + i); }).start();
// 消费者
new Thread(() -> { for (int i = 0; i < 5; i++) System.out.println(queue.take()); }).start();
```

---

## 延伸阅读
Java 并发与 JUC，见 013-java 模块并发文档。
JVM 内存与 GC 调优，见 013-java 模块 JVM 文档。
Spring Boot 微服务与 Kubernetes，见 013-java/041-JavaKubernetes 文档。
数据库访问（JDBC/JPA），见 019-sql 模块相关文档。
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
