---
order: 820
title: Java 类型擦除与桥接方法语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java 类型擦除与桥接方法语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 类型擦除规则

**基本写法：擦除为上界**
```java
// 源码：List<T>  字节码：List<Object>
// 源码：List<T extends Number>  字节码：List<Number>
```
```java
// 编译后泛型类型参数被擦除
public class Box<T> {
    private T value;
    // 字节码中 value 类型为 Object
}
```

---

**基本写法：擦除影响**
```java
// 运行时无法获取泛型类型参数
if (list instanceof List<String>) { } // 编译错误
```
```java
// 不能 new 泛型类型
T t = new T(); // 编译错误
```

---

## 反射获取泛型

**基本写法：获取字段泛型**
`<field>.getGenericType();`
```java
// 通过反射获取字段的参数化类型
Field f = Box.class.getDeclaredField("value");
Type t = f.getGenericType();
if (t instanceof ParameterizedType pt) {
    Type[] args = pt.getActualTypeArguments();
}
```

---

**基本写法：获取方法返回泛型**
`<method>.getGenericReturnType();`
```java
// 获取方法的泛型返回类型
Method m = clazz.getMethod("getList");
Type rt = m.getGenericReturnType();
```

---

**基本写法：TypeToken 模式**
```java
// 通过子类保留泛型信息
Type type = new TypeToken<List<String>>() {}.getType();
```
```java
// Gson 等库常用此模式
Type type = new TypeToken<Map<String, List<Integer>>>() {}.getType();
```

---

## 桥接方法

**基本写法：桥接方法生成**
```java
// 子类覆盖泛型方法时编译器生成桥接方法
class StringBox extends Box<String> {
    @Override public void set(String v) { super.set(v); }
    // 编译器生成：public void set(Object v) { set((String) v); }
}
```
```java
// 桥接方法保证多态正确
Box<String> b = new StringBox();
b.set("hi"); // 实际调用桥接方法
```

---

**基本写法：识别桥接方法**
`<method>.isBridge();`
```java
// 反射判断是否桥接方法
for (Method m : StringBox.class.getMethods()) {
    if (m.isBridge()) System.out.println(m);
}
```

---

## 泛型数组

**基本写法：泛型数组限制**
```java
// 不能直接创建泛型数组
List<String>[] arr = new List<String>[10]; // 编译错误
```
```java
// 通过原始类型或 Array.newInstance 创建
List<?>[] arr = new List<?>[10];
```

---

**基本写法：Array.newInstance**
`Array.newInstance(<类型>, <长度>);`
```java
// 反射创建泛型数组
T[] arr = (T[]) Array.newInstance(componentType, 10);
```

---

## 可重写类型参数

**基本写法：保留泛型信息的类**
```java
// 通过 Class 对象保留类型
public class TypedBox<T> {
    private final Class<T> type;
    public TypedBox(Class<T> type) { this.type = type; }
    public T cast(Object o) { return type.cast(o); }
}
```
```java
// 运行时仍可使用类型
TypedBox<String> b = new TypedBox<>(String.class);
String s = b.cast("hello");
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
