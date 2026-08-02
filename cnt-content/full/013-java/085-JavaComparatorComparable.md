---
order: 850
title: Java Comparator/Comparable 语法速查手册
module: 'java'
category: 后端技术
difficulty: beginner
description: Java Comparator/Comparable 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## Comparable 自然排序

**基本写法：实现 Comparable**
```java
public class <类> implements Comparable<<类>> {
  public int compareTo(<类> other) { ... }
}
```
```java
// 定义自然排序
public class Person implements Comparable<Person> {
    private int age;
    public int compareTo(Person other) {
        return Integer.compare(this.age, other.age);
    }
}
```

---

## Comparator 比较器

**基本写法：创建比较器**
`Comparator.<comparing方法>(<keyExtractor>);`
```java
// 按属性创建比较器
Comparator<Person> byAge = Comparator.comparingInt(Person::getAge);
```

---

**基本写法：链式比较**
`<comparator>.thenComparing(<keyExtractor>);`
```java
// 主排序字段相等时用次排序字段
Comparator<Person> c = Comparator
    .comparing(Person::getDept)
    .thenComparingInt(Person::getAge);
```

---

**基本写法：反向**
`<comparator>.reversed();`
```java
// 反转排序
Comparator<Person> desc = byAge.reversed();
```

---

**基本写法：nulls 优先**
`Comparator.nullsFirst(<比较器>);`
```java
// null 排在最前
Comparator<String> c = Comparator.nullsFirst(Comparator.naturalOrder());
```

---

**基本写法：nulls 最后**
`Comparator.nullsLast(<比较器>);`
```java
// null 排在最后
Comparator<String> c = Comparator.nullsLast(Comparator.naturalOrder());
```

---

**基本写法：自然顺序**
`Comparator.naturalOrder();`
```java
// 使用元素自然顺序
Comparator<String> c = Comparator.naturalOrder();
```

---

**基本写法：反向自然顺序**
`Comparator.reverseOrder();`
```java
// 反向自然顺序
Comparator<String> c = Comparator.reverseOrder();
```

---

## 排序使用

**基本写法：集合排序**
`<list>.sort(<比较器>);`
```java
// 用比较器排序
list.sort(Comparator.comparing(Person::getName));
```

---

**基本写法：Stream 排序**
`<stream>.sorted(<比较器>);`
```java
// 流排序
list.stream().sorted(Comparator.comparingInt(Person::getAge).reversed());
```

---

**基本写法：求最大最小**
`<stream>.max(<比较器>);`
```java
// 用比较器求最大值
Optional<Person> oldest = list.stream().max(Comparator.comparingInt(Person::getAge));
```

---

## 基本类型比较

**基本写法：Integer 比较**
`Integer.compare(<a>, <b>);`
```java
// 比较两个 int 返回 -1/0/1
int r = Integer.compare(1, 2);
```

---

**基本写法：比较静态方法**
`<包装类>.compare(<a>, <b>);`
```java
// Long/Double 等都有 compare
int r = Double.compare(1.0, 2.0);
```

---

**基本写法：Objects.compare**
`Objects.compare(<a>, <b>, <比较器>);`
```java
// 工具方法
int r = Objects.compare("a", "b", Comparator.naturalOrder());
```

---

## 自定义比较器

**基本写法：lambda 比较**
`Comparator<<类型>> <变量> = (a, b) -> <表达式>;`
```java
// 用 lambda 自定义比较逻辑
Comparator<String> byLen = (a, b) -> Integer.compare(a.length(), b.length());
```

---

**基本写法：comparingDouble**
`Comparator.comparingDouble(<keyExtractor>);`
```java
// 按 double 属性比较
Comparator<Product> byPrice = Comparator.comparingDouble(Product::getPrice);
```

---

**基本写法：comparingLong**
`Comparator.comparingLong(<keyExtractor>);`
```java
// 按 long 属性比较
Comparator<Event> byTime = Comparator.comparingLong(Event::getTimestamp);
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
