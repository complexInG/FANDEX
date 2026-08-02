---
order: 880
title: Java Objects 工具类语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java Objects 工具类语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 非空检查

**基本写法：要求非空**
`Objects.requireNonNull(<对象>);`
```java
// 为 null 抛 NullPointerException
Objects.requireNonNull(name);
```

---

**基本写法：带消息的非空检查**
`Objects.requireNonNull(<对象>, <消息>);`
```java
// 抛出带消息的 NPE
Objects.requireNonNull(name, "name 不能为空");
```

---

**基本写法：带 Supplier 消息**
`Objects.requireNonNull(<对象>, <Supplier>);`
```java
// 延迟构造消息
Objects.requireNonNull(name, () -> "字段 " + fieldName + " 不能为空");
```

---

**基本写法：requireNonNullElse**
`Objects.requireNonNullElse(<对象>, <默认值>);`
```java
// Java 9+ 为 null 返回默认值
String v = Objects.requireNonNullElse(name, "default");
```

---

**基本写法：requireNonNullElseGet**
`Objects.requireNonNullElseGet(<对象>, <Supplier>);`
```java
// 为 null 时用 Supplier 生成默认值
String v = Objects.requireNonNullElseGet(name, () -> fetchDefault());
```

---

## 相等与哈希

**基本写法：判等**
`Objects.equals(<a>, <b>);`
```java
// 安全的 equals，避免 NPE
boolean ok = Objects.equals(a, b);
```

---

**基本写法：深度判等**
`Objects.deepEquals(<a>, <b>);`
```java
// 数组深度比较
boolean ok = Objects.deepEquals(arr1, arr2);
```

---

**基本写法：哈希码**
`Objects.hash(<字段>...);`
```java
// 多字段组合哈希码
@Override public int hashCode() {
    return Objects.hash(name, age);
}
```

---

**基本写法：单值哈希**
`Objects.hashCode(<对象>);`
```java
// 单个对象的哈希码
int h = Objects.hashCode(name);
```

---

## 字符串表示

**基本写法：toString**
`Objects.toString(<对象>);`
```java
// 调用 toString，null 返回 "null"
String s = Objects.toString(obj);
```

---

**基本写法：带默认值 toString**
`Objects.toString(<对象>, <默认值>);`
```java
// 为 null 返回默认值
String s = Objects.toString(obj, "N/A");
```

---

**基本写法：toIdentityString**
`Objects.toIdentityString(<对象>);`
```java
// 返回类名@哈希码形式
String s = Objects.toIdentityString(obj);
```

---

## 比较操作

**基本写法：比较**
`Objects.compare(<a>, <b>, <比较器>);`
```java
// 用比较器比较两个对象
int r = Objects.compare("a", "b", Comparator.naturalOrder());
```

---

## 索引检查

**基本写法：检查索引**
`Objects.checkIndex(<索引>, <长度>);`
```java
// 检查索引在 [0, length) 范围
int i = Objects.checkIndex(5, 10);
```

---

**基本写法：检查范围**
`Objects.checkFromToIndex(<起>, <止>, <长度>);`
```java
// 检查 [from, to) 在 [0, length) 范围
Objects.checkFromToIndex(2, 5, 10);
```

---

**基本写法：检查起始长度**
`Objects.checkFromIndexSize(<起>, <大小>, <长度>);`
```java
// 检查 [from, from+size) 在 [0, length) 范围
Objects.checkFromIndexSize(2, 3, 10);
```

---

## 数组相关

**基本写法：数组相等**
`Objects.equals(<数组1>, <数组2>);`
```java
// 用 Objects.equals 比较数组引用
boolean same = Objects.equals(arr1, arr2);
```

---

## 验证工具

**基本写法：校验后返回值**
`<表达式> == null ? <默认> : <对象>`
```java
// 配合 requireNonNullElse 使用
String v = Objects.requireNonNullElseElseGet(name, () -> "");
```

---

## 防御性拷贝

**基本写法：复制不可变**
```java
// 通过不可变工厂方法
List<String> imm = List.copyOf(mutableList);
```
```java
// Java 10+ 拷贝为不可变集合
List<String> safe = List.copyOf(original);
Set<String> safeSet = Set.copyOf(original);
Map<String, Integer> safeMap = Map.copyOf(original);
```

---

## 通用工具

**基本写法：获取类名**
`<对象>.getClass().getName();`
```java
// 获取运行时类名
String name = obj.getClass().getName();
```

---

**基本写法：instanceof 模式匹配**
`<对象> instanceof <类型> <变量>`
```java
// Java 16+ 模式匹配
if (obj instanceof String s) {
    System.out.println(s.length());
}
```

---

## 防御性编程

**基本写法：参数校验组合**
```java
public void set(String name, int age) {
    this.name = Objects.requireNonNull(name);
    if (Objects.checkIndex(age, 151) != age) throw new IllegalArgumentException();
}
```
```java
// 综合使用 Objects 进行参数校验
public User(String name, int age) {
    this.name = Objects.requireNonNull(name, "name");
    this.age = age >= 0 && age <= 150 ? age : -1;
}
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
