---
order: 870
title: Java Arrays 工具类语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java Arrays 工具类语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 数组排序

**基本写法：排序**
`Arrays.sort(<数组>);`
```java
// 对数组进行自然排序
int[] a = {3, 1, 2};
Arrays.sort(a);
```

---

**基本写法：范围排序**
`Arrays.sort(<数组>, <起>, <止>);`
```java
// 只排序 [1, 3) 范围
Arrays.sort(a, 1, 3);
```

---

**基本写法：并行排序**
`Arrays.parallelSort(<数组>);`
```java
// 并行排序大数组
Arrays.parallelSort(a);
```

---

**基本写法：自定义比较器排序**
`Arrays.sort(<数组>, <比较器>);`
```java
// 对象数组自定义排序
String[] s = {"b", "a"};
Arrays.sort(s, Comparator.reverseOrder());
```

---

## 数组搜索

**基本写法：二分查找**
`Arrays.binarySearch(<数组>, <key>);`
```java
// 在已排序数组中查找
int idx = Arrays.binarySearch(a, 2);
```

---

**基本写法：范围查找**
`Arrays.binarySearch(<数组>, <起>, <止>, <key>);`
```java
// 在 [1, 3) 范围查找
int idx = Arrays.binarySearch(a, 1, 3, 2);
```

---

## 数组拷贝

**基本写法：拷贝**
`Arrays.copyOf(<数组>, <新长度>);`
```java
// 拷贝并指定新长度
int[] b = Arrays.copyOf(a, 5);
```

---

**基本写法：范围拷贝**
`Arrays.copyOfRange(<数组>, <起>, <止>);`
```java
// 拷贝 [1, 3) 范围
int[] c = Arrays.copyOfRange(a, 1, 3);
```

---

## 数组填充

**基本写法：填充**
`Arrays.fill(<数组>, <值>);`
```java
// 用值填充整个数组
Arrays.fill(a, 0);
```

---

**基本写法：范围填充**
`Arrays.fill(<数组>, <起>, <止>, <值>);`
```java
// 填充 [1, 3) 范围
Arrays.fill(a, 1, 3, 99);
```

---

## 数组比较与哈希

**基本写法：数组相等**
`Arrays.equals(<数组1>, <数组2>);`
```java
// 比较两个数组内容
boolean ok = Arrays.equals(a, b);
```

---

**基本写法：深度比较**
`Arrays.deepEquals(<数组1>, <数组2>);`
```java
// 多维数组深度比较
boolean ok = Arrays.deepEquals(m1, m2);
```

---

**基本写法：哈希码**
`Arrays.hashCode(<数组>);`
```java
// 计算数组哈希码
int h = Arrays.hashCode(a);
```

---

**基本写法：深度哈希**
`Arrays.deepHashCode(<数组>);`
```java
// 多维数组哈希码
int h = Arrays.deepHashCode(m);
```

---

## 数组转字符串

**基本写法：转字符串**
`Arrays.toString(<数组>);`
```java
// 一维数组转字符串
String s = Arrays.toString(a); // [1, 2, 3]
```

---

**基本写法：深度转字符串**
`Arrays.deepToString(<数组>);`
```java
// 多维数组转字符串
String s = Arrays.deepToString(matrix);
```

---

## 数组转流

**基本写法：转 Stream**
`Arrays.stream(<数组>);`
```java
// 数组转 Stream
IntStream s = Arrays.stream(new int[]{1, 2, 3});
```

---

**基本写法：范围流**
`Arrays.stream(<数组>, <起>, <止>);`
```java
// 取数组部分转 Stream
IntStream s = Arrays.stream(a, 1, 3);
```

---

## 数组转列表

**基本写法：转固定大小列表**
`Arrays.asList(<元素>...);`
```java
// 数组转 List（固定大小，不可增删）
List<String> list = Arrays.asList("a", "b");
```

---

**基本写法：转可变列表**
`new ArrayList<>(Arrays.asList(<元素>...));`
```java
// 包装为可变 List
List<String> list = new ArrayList<>(Arrays.asList("a", "b"));
```

---

## 数组创建

**基本写法：setAll 创建**
`Arrays.setAll(<数组>, <生成器>);`
```java
// 用函数初始化数组
int[] a = new int[5];
Arrays.setAll(a, i -> i * 2);
```

---

**基本写法：parallelSetAll**
`Arrays.parallelSetAll(<数组>, <生成器>);`
```java
// 并行初始化数组
Arrays.parallelSetAll(a, i -> i * i);
```

---

**基本写法：parallelPrefix**
`Arrays.parallelPrefix(<数组>, <BinaryOperator>);`
```java
// 并行前缀计算（累加）
Arrays.parallelPrefix(a, Integer::sum);
```

---

## 数组工具

**基本写法：获取数组长度**
`<数组>.length`
```java
// 数组长度属性
int n = a.length;
```

---

**基本写法：Array.newInstance**
`Array.newInstance(<类型>, <长度>);`
```java
// 反射创建数组
Object arr = Array.newInstance(int.class, 5);
```

---

**基本写法：获取元素**
`Array.get(<数组>, <索引>);`
```java
// 反射获取数组元素
Object e = Array.get(arr, 0);
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
