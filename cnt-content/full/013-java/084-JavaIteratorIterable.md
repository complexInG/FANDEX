---
order: 840
title: Java Iterator/Iterable/Spliterator 语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java Iterator/Iterable/Spliterator 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Iterator 接口

**基本写法：获取迭代器**
`<collection>.iterator();`
```java
// 从集合获取迭代器
Iterator<String> it = list.iterator();
```

---

**基本写法：遍历**
```java
while (<it>.hasNext()) { <类型> <变量> = <it>.next(); }
```
```java
// 经典迭代器遍历
while (it.hasNext()) {
    String s = it.next();
    System.out.println(s);
}
```

---

**基本写法：移除元素**
`<it>.remove();`
```java
// 移除最近 next() 返回的元素
it.remove();
```

---

**基本写法：forEachRemaining**
`<it>.forEachRemaining(<消费者>);`
```java
// 用 lambda 处理剩余元素
it.forEachRemaining(System.out::println);
```

---

## Iterable 接口

**基本写法：实现 Iterable**
```java
public class <类> implements Iterable<<类型>> {
  public Iterator<<类型>> iterator() { ... }
}
```
```java
// 自定义可迭代集合
public class MyList implements Iterable<String> {
    public Iterator<String> iterator() { return list.iterator(); }
}
```

---

**基本写法：增强 for 循环**
```java
for (<类型> <变量> : <iterable>) { }
```
```java
// 任何 Iterable 都可用增强 for
for (String s : myList) {
    System.out.println(s);
}
```

---

**基本写法：默认 forEach**
`<iterable>.forEach(<消费者>);`
```java
// Iterable 接口的默认方法
list.forEach(System.out::println);
```

---

**基本写法：spliterator**
`<iterable>.spliterator();`
```java
// 获取可分割迭代器
Spliterator<String> sp = list.spliterator();
```

---

## Spliterator 可分割迭代器

**基本写法：tryAdvance 单个处理**
`<sp>.tryAdvance(<消费者>);`
```java
// 处理一个元素返回是否还有
boolean has = sp.tryAdvance(System.out::println);
```

---

**基本写法：forEachRemaining**
`<sp>.forEachRemaining(<消费者>);`
```java
// 处理所有剩余元素
sp.forEachRemaining(System.out::println);
```

---

**基本写法：尝试分割**
`<sp>.trySplit();`
```java
// 把迭代器一分为二用于并行
Spliterator<String> other = sp.trySplit();
```

---

**基本写法：估算大小**
`<sp>.estimateSize();`
```java
// 估算剩余元素数量
long n = sp.estimateSize();
```

---

**基本写法：特征**
`<sp>.characteristics();`
```java
// 返回特征位
int chars = sp.characteristics();
boolean sorted = sp.hasCharacteristics(Spliterator.SORTED);
```

---

## StreamSupport 转 Stream

**基本写法：Spliterator 转 Stream**
`StreamSupport.stream(<spliterator>, <并行>);`
```java
// 把 Spliterator 转为 Stream
Stream<String> s = StreamSupport.stream(sp, false);
```

---

**基本写法：从迭代器创建流**
`StreamSupport.stream(Spliterators.spliteratorUnknownSize(<it>, 0), false);`
```java
// Iterator 转 Stream
Stream<String> s = StreamSupport.stream(
    Spliterators.spliteratorUnknownSize(it, 0), false);
```

---

## 自定义 Iterator

**基本写法：实现 Iterator**
```java
public class <类> implements Iterator<<类型>> {
  public boolean hasNext() { ... }
  public <类型> next() { ... }
}
```
```java
// 自定义迭代器
public class RangeIt implements Iterator<Integer> {
    private int cur, end;
    public RangeIt(int s, int e) { cur = s; end = e; }
    public boolean hasNext() { return cur < end; }
    public Integer next() { return cur++; }
}
```

---

## ListIterator 双向迭代

**基本写法：获取 ListIterator**
`<list>.listIterator();`
```java
// 获取双向迭代器
ListIterator<String> li = list.listIterator();
```

---

**基本写法：向前遍历**
`<li>.hasPrevious(); <li>.previous();`
```java
// 反向遍历
while (li.hasPrevious()) {
    String s = li.previous();
}
```

---

**基本写法：set 修改**
`<li>.set(<值>);`
```java
// 修改最近 next/previous 返回的元素
li.set("new");
```

---

**基本写法：add 插入**
`<li>.add(<值>);`
```java
// 在当前位置插入元素
li.add("inserted");
```

---

**基本写法：nextIndex/previousIndex**
`<li>.nextIndex();`
```java
// 返回下一个元素索引
int i = li.nextIndex();
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
