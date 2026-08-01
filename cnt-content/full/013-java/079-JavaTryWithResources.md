---
order: 790
title: Java try-with-resources 与异常链语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Java try-with-resources 与异常链语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## try-with-resources

**基本写法：自动关闭资源**
```java
try (<资源声明>) { <语句> }
```
```java
// 自动关闭实现了 AutoCloseable 的资源
try (FileInputStream in = new FileInputStream("a.txt")) {
    int b = in.read();
}
```

---

**基本写法：多个资源**
```java
try (<资源1>; <资源2>) { <语句> }
```
```java
// 多个资源用分号分隔，关闭顺序与声明相反
try (FileInputStream in = new FileInputStream("in.txt");
     FileOutputStream out = new FileOutputStream("out.txt")) {
    out.write(in.readAllBytes());
}
```

---

**基本写法：引用外部变量**
```java
<AutoCloseable 变量> = ...;
try (<变量>) { <语句> }
```
```java
// Java 9+ 支持使用 effectively final 的外部资源
BufferedReader r = Files.newBufferedReader(Path.of("a.txt"));
try (r) {
    System.out.println(r.readLine());
}
```

---

## 异常捕获

**基本写法：多异常捕获**
```java
try { <语句> } catch (<类型1> | <类型2> <变量>) { <处理> }
```
```java
// 一个 catch 块处理多种异常
try {
    Files.readAllBytes(Path.of("a.txt"));
} catch (IOException | SecurityException e) {
    log.error(e);
}
```

---

**基本写法：异常重新抛出**
```java
catch (<类型> <变量>) { throw <变量>; }
```
```java
// 处理后再抛出
try { risky(); }
catch (IOException e) { log.error(e); throw e; }
```

---

## 异常链

**基本写法：包装异常**
`throw new <异常>(<消息>, <原因>);`
```java
// 把底层异常包装成业务异常
try {
    Files.readString(Path.of("a.txt"));
} catch (IOException e) {
    throw new BusinessException("读取配置失败", e);
}
```

---

**基本写法：获取根因**
`<throwable>.getCause();`
```java
// 获取异常的根本原因
Throwable root = e.getCause();
```

---

**基本写法：添加受抑制异常**
`<throwable>.addSuppressed(<异常>);`
```java
// 主异常抛出后关闭资源时的异常被抑制
try (Resource r = new Resource()) {
    throw new IOException("main");
} catch (IOException e) {
    for (Throwable s : e.getSuppressed()) {
        System.out.println(s);
    }
}
```

---

## finally 块

**基本写法：finally 执行清理**
```java
try { <语句> } catch (<类型> <变量>) { <处理> } finally { <清理> }
```
```java
// finally 块无论是否抛异常都会执行
try {
    return risky();
} finally {
    cleanup();
}
```

---

## StackWalker 栈遍历

**基本写法：遍历调用栈**
`StackWalker.getInstance().forEach(<消费者>);`
```java
// 打印调用栈
StackWalker.getInstance().forEach(f -> System.out.println(f.getClassName() + "#" + f.getMethodName()));
```

---

**基本写法：获取调用者**
`StackWalker.getInstance().walk(<函数>);`
```java
// 获取直接调用者的栈帧
StackTraceElement caller = StackWalker.getInstance()
    .walk(s -> s.skip(1).findFirst())
    .map(StackWalker.StackFrame::toStackTraceElement)
    .orElse(null);
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
