---
order: 730
title: Java Optional 类
module: 'java'
category: 后端技术
difficulty: beginner
description: Java Optional 类 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## 创建 Optional

**基本写法：创建非空 Optional**
`Optional.of(<值>);`
```java
// 包装非空值，为 null 抛 NPE
Optional<String> o = Optional.of("hello");
```

---

**基本写法：创建可空 Optional**
`Optional.ofNullable(<值>);`
```java
// 包装可能为 null 的值
Optional<String> o = Optional.ofNullable(getName());
```

---

**基本写法：创建空 Optional**
`Optional.empty();`
```java
// 创建空 Optional
Optional<String> empty = Optional.empty();
```

---

## 判断与获取

**基本写法：判断是否存在**
`<optional>.isPresent();`
```java
// 判断是否有值
boolean has = o.isPresent();
```

---

**基本写法：判断为空**
`<optional>.isEmpty();`
```java
// Java 11+ 判断是否为空
boolean empty = o.isEmpty();
```

---

**基本写法：获取值**
`<optional>.get();`
```java
// 获取值（为空抛 NoSuchElementException）
String v = o.get();
```

---

**基本写法：存在则执行**
`<optional>.ifPresent(<消费者>);`
```java
// 值存在时执行消费
o.ifPresent(System.out::println);
```

---

## 默认值

**基本写法：默认值**
`<optional>.orElse(<默认值>);`
```java
// 为空返回默认值
String v = o.orElse("default");
```

---

**基本写法：默认值惰性求值**
`<optional>.orElseGet(() -> <计算>);`
```java
// 为空时惰性计算默认值
String v = o.orElseGet(() -> fetchDefault());
```

---

**基本写法：为空抛异常**
`<optional>.orElseThrow();`
```java
// 为空抛 NoSuchElementException
String v = o.orElseThrow();
```

---

**基本写法：抛自定义异常**
`<optional>.orElseThrow(() -> new <异常>());`
```java
// 为空抛自定义异常
String v = o.orElseThrow(() -> new RuntimeException("no value"));
```

---

## 链式操作

**基本写法：map 转换**
`<optional>.map(<函数>);`
```java
// 值存在则转换
Optional<Integer> len = o.map(String::length);
```

---

**基本写法：flatMap 嵌套扁平化**
`<optional>.flatMap(<函数>);`
```java
// 处理返回 Optional 的函数
Optional<String> r = o.flatMap(this::findEmail);
```

---

**基本写法：filter 过滤**
`<optional>.filter(<条件>);`
```java
// 不满足条件则返回空
Optional<String> r = o.filter(s -> s.length() > 3);
```

---

## 提供备选 Optional

**基本写法：备选 Optional**
`<optional>.or(() -> <其他 Optional>);`
```java
// 为空则返回另一个 Optional
Optional<String> r = o.or(() -> Optional.of("backup"));
```

---

## 流式消费

**基本写法：存在则执行 else 执行**
`<optional>.ifPresentOrElse(<消费者>, <运行>);`
```java
// 存在执行 A 否则执行 B
o.ifPresentOrElse(
    v -> System.out.println(v),
    () -> System.out.println("empty")
);
```

---

## Optional 与 Stream

**基本写法：转 Stream**
`<optional>.stream();`
```java
// 转 Stream 便于链式处理
Stream<String> s = o.stream();
```

---

**基本写法：过滤空 Optional**
`<list>.stream().flatMap(Optional::stream)`
```java
// 过滤掉集合中的空 Optional
List<String> r = list.stream()
    .map(this::find)
    .flatMap(Optional::stream)
    .toList();
```

---

## 原始类型 Optional

**基本写法：OptionalInt**
`OptionalInt.of(<值>);`
```java
// int 专用 Optional
OptionalInt oi = OptionalInt.of(42);
```

---

**基本写法：OptionalDouble**
`OptionalDouble.of(<值>);`
```java
// double 专用 Optional
OptionalDouble od = OptionalDouble.of(3.14);
```

---

**基本写法：OptionalLong**
`OptionalLong.of(<值>);`
```java
// long 专用 Optional
OptionalLong ol = OptionalLong.of(100L);
```

---

## 实用模式

**基本写法：方法返回 Optional**
`public Optional<<类型>> <方法>() { return Optional.ofNullable(<值>); }`
```java
// 方法返回 Optional 表达可能为空
public Optional<User> findById(long id) {
    return Optional.ofNullable(map.get(id));
}
```

---

**基本写法：链式调用避免 null**
`opt.map(<取值>).map(<再取>).orElse(<默认>);`
```java
// 链式调用避免 NPE
String city = optUser.map(User::getAddr).map(Addr::getCity).orElse("unknown");
```

---

## equals 比较

**基本写法：安全比较**
`<optional>.equals(<其他 Optional>);`
```java
// 比较两个 Optional 的值
boolean same = o1.equals(o2);
```

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
