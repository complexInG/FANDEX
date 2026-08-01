---
order: 830
title: Java 枚举进阶 EnumSet/EnumMap/枚举单例语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java 枚举进阶 EnumSet/EnumMap/枚举单例语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 枚举定义

**基本写法：简单枚举**
```java
public enum <名称> { <常量1>, <常量2> }
```
```java
// 定义枚举类型
public enum Color { RED, GREEN, BLUE }
```

---

**基本写法：带字段枚举**
```java
public enum <名称> {
  <常量>(<参数>);
  private final <类型> <字段>;
  <名称>(<类型> <参数>) { this.<字段> = <参数>; }
}
```
```java
// 枚举带属性与方法
public enum Planet {
    EARTH(6371), MARS(3390);
    private final int radius;
    Planet(int r) { this.radius = r; }
    public int getRadius() { return radius; }
}
```

---

**基本写法：带抽象方法**
```java
public enum <名称> {
  <常量> { @Override public <返回> <方法>() { } };
  public abstract <返回> <方法>();
}
```
```java
// 每个常量实现自己的行为
public enum Op {
    PLUS { public int apply(int a, int b) { return a + b; } },
    MINUS { public int apply(int a, int b) { return a - b; } };
    public abstract int apply(int a, int b);
}
```

---

## 枚举方法

**基本写法：获取所有常量**
`<枚举>.values();`
```java
// 返回所有枚举常量数组
Color[] all = Color.values();
```

---

**基本写法：按名获取**
`<枚举>.valueOf(<名称>);`
```java
// 按字符串名获取常量
Color c = Color.valueOf("RED");
```

---

**基本写法：序号**
`<常量>.ordinal();`
```java
// 返回常量声明序号（从 0 开始）
int idx = Color.RED.ordinal();
```

---

**基本写法：比较**
`<常量>.compareTo(<其他>);`
```java
// 按 ordinal 比较
int r = Color.RED.compareTo(Color.BLUE);
```

---

**基本写法：名称**
`<常量>.name();`
```java
// 返回常量名字符串
String n = Color.RED.name();
```

---

## EnumSet 枚举集合

**基本写法：所有常量集合**
`EnumSet.allOf(<枚举类>.class);`
```java
// 创建包含全部常量的集合
EnumSet<Color> all = EnumSet.allOf(Color.class);
```

---

**基本写法：指定常量集合**
`EnumSet.of(<常量>...);`
```java
// 创建包含部分常量的集合
EnumSet<Color> warm = EnumSet.of(Color.RED);
```

---

**基本写法：补集**
`EnumSet.complementOf(<EnumSet>);`
```java
// 返回传入集合的补集
EnumSet<Color> rest = EnumSet.complementOf(warm);
```

---

**基本写法：范围**
`EnumSet.range(<起>, <止>);`
```java
// 创建常量区间集合
EnumSet<Color> r = EnumSet.range(Color.RED, Color.BLUE);
```

---

## EnumMap 枚举映射

**基本写法：创建 EnumMap**
`new EnumMap<<枚举>, <值>>(<枚举类>.class);`
```java
// 键为枚举的高效 Map
EnumMap<Color, String> names = new EnumMap<>(Color.class);
names.put(Color.RED, "红色");
```

---

## 枚举实现接口

**基本写法：枚举实现接口**
```java
public interface <接口> { <方法签名>; }
public enum <名称> implements <接口> { ... }
```
```java
// 枚举实现接口统一行为
public interface Operation { int apply(int a, int b); }
public enum BasicOp implements Operation {
    PLUS { public int apply(int a, int b) { return a + b; } }
}
```

---

## 枚举单例

**基本写法：枚举单例模式**
```java
public enum <名称> {
  INSTANCE;
  public void <方法>() { }
}
```
```java
// 线程安全的单例实现
public enum AppConfig {
    INSTANCE;
    private final Map<String, String> cfg = new HashMap<>();
    public String get(String k) { return cfg.get(k); }
}
// 使用：AppConfig.INSTANCE.get("key")
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
