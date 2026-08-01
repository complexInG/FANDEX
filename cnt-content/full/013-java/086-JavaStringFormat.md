---
order: 860
title: Java String.format/printf/MessageFormat 语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java String.format/printf/MessageFormat 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## String.format

**基本写法：格式化字符串**
`String.format(<格式>, <参数>...);`
```java
// 格式化字符串
String s = String.format("name=%s, age=%d", "Tom", 18);
```

---

**基本写法：带 Locale**
`String.format(<Locale>, <格式>, <参数>...);`
```java
// 指定地区
String s = String.format(Locale.US, "%,.2f", 1234567.89);
```

---

## 常用格式说明符

**基本写法：字符串**
`%s`
```java
// 字符串占位符
String s = String.format("hello %s", "world");
```

---

**基本写法：整数**
`%d`
```java
// 十进制整数
String s = String.format("count=%d", 42);
```

---

**基本写法：浮点**
`%.2f`
```java
// 保留两位小数
String s = String.format("%.2f", 3.14159);
```

---

**基本写法：十六进制**
`%x`
```java
// 十六进制小写
String s = String.format("%x", 255); // ff
```

---

**基本写法：八进制**
`%o`
```java
// 八进制
String s = String.format("%o", 8); // 10
```

---

**基本写法：字符**
`%c`
```java
// 字符
String s = String.format("%c", 65); // A
```

---

**基本写法：布尔**
`%b`
```java
// 布尔
String s = String.format("%b", true);
```

---

## 宽度与对齐

**基本写法：指定宽度**
`%<宽度>d`
```java
// 最小宽度 5
String s = String.format("%5d", 42); // "   42"
```

---

**基本写法：左对齐**
`%-<宽度>d`
```java
// 左对齐宽度 5
String s = String.format("%-5d|", 42); // "42   |"
```

---

**基本写法：零填充**
`%0<宽度>d`
```java
// 用 0 填充
String s = String.format("%05d", 42); // "00042"
```

---

**基本写法：千分位**
`%,d`
```java
// 千分位分隔符
String s = String.format("%,d", 1234567); // 1,234,567
```

---

**基本写法：正负号**
`%+d`
```java
// 显示正负号
String s = String.format("%+d", 42); // +42
```

---

## 参数索引

**基本写法：指定参数位置**
`%<索引>$<格式>`
```java
// 使用第 1 个参数
String s = String.format("%1$s = %1$s", "hello");
```

---

**基本写法：重复使用参数**
`%<索引>$<格式>`
```java
// 复用同一参数
String s = String.format("%1$s has %2$d items, %1$s is ok", "Tom", 5);
```

---

## System.out.printf

**基本写法：直接输出**
`System.out.printf(<格式>, <参数>...);`
```java
// 格式化打印到标准输出
System.out.printf("name=%s, age=%d%n", "Tom", 18);
```

---

## 换行符

**基本写法：平台无关换行**
`%n`
```java
// 平台无关的换行符
String s = String.format("line1%nline2");
```

---

**基本写法：System.lineSeparator**
`System.lineSeparator();`
```java
// 获取系统换行符
String nl = System.lineSeparator();
```

---

## MessageFormat

**基本写法：消息格式化**
`MessageFormat.format(<模板>, <参数>...);`
```java
// 使用 MessageFormat
String s = MessageFormat.format("At {0,time} on {0,date}, {1} sent", new Date(), "Tom");
```

---

**基本写法：占位符索引**
`{<索引>}`
```java
// 占位符格式 {索引,类型,样式}
String s = MessageFormat.format("{0} + {1} = {2}", 1, 2, 3);
```

---

**基本写法：数字格式**
`{<索引>,number,<样式>}`
```java
// 数字格式化
String s = MessageFormat.format("{0,number,#.##}", 3.14159);
```

---

**基本写法：选择格式**
`{<索引>,choice,<选项>}`
```java
// 选择性文本
String s = MessageFormat.format("{0,choice,0#no items|1#one item|1<many items}", 5);
```

---

## Formatter 类

**基本写法：使用 Formatter**
`new Formatter().format(<格式>, <参数>).toString();`
```java
// Formatter 流式格式化
String s = new Formatter().format("x=%d, y=%d", 1, 2).toString();
```

---

**基本写法：输出到 StringBuilder**
`new Formatter(<StringBuilder>).format(<格式>, <参数>);`
```java
// 把格式化结果追加到 StringBuilder
StringBuilder sb = new StringBuilder();
new Formatter(sb).format("value=%d%n", 42);
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
