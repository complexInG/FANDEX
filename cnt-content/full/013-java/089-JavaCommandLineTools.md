---
order: 890
title: Java 命令行工具 javac/java/jar/jshell/jpackage 语法速查手册
module: 'java'
category: 后端技术
difficulty: beginner
description: Java 命令行工具 javac/java/jar/jshell/jpackage 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## javac 编译

**基本写法：编译源文件**
`javac <源文件>.java`
```bash
# 编译单个源文件
javac Main.java
```

---

**基本写法：指定输出目录**
`javac -d <输出目录> <源文件>`
```bash
# 编译并输出到 bin 目录
javac -d bin src/Main.java
```

---

**基本写法：指定 classpath**
`javac -cp <路径> <源文件>`
```bash
# 编译时引用外部依赖
javac -cp "lib/*" -d bin src/Main.java
```

---

**基本写法：指定源版本与目标版本**
`javac --source <版本> --target <版本> <源文件>`
```bash
# 用 Java 21 语法编译为 21 字节码
javac --release 21 -d bin src/Main.java
```

---

**基本写法：启用预览特性**
`javac --enable-preview --release <版本> <源文件>`
```bash
# 启用 Java 23 预览特性
javac --enable-preview --release 23 src/Main.java
```

---

## java 运行

**基本写法：运行主类**
`java -cp <路径> <主类>`
```bash
# 运行编译后的类
java -cp bin com.example.Main
```

---

**基本写法：运行 jar**
`java -jar <文件>.jar`
```bash
# 运行可执行 jar
java -jar app.jar
```

---

**基本写法：传递程序参数**
`java -cp <路径> <主类> <参数>...`
```bash
# 传递命令行参数
java -cp bin Main arg1 arg2
```

---

**基本写法：设置 JVM 属性**
`java -D<名>=<值> -cp <路径> <主类>`
```bash
# 设置系统属性
java -Dconfig=prod -cp bin Main
```

---

**基本写法：设置堆内存**
`java -Xmx<大小> -Xms<大小> -cp <路径> <主类>`
```bash
# 设置最大堆 2G 初始堆 512M
java -Xmx2g -Xms512m -cp bin Main
```

---

## jar 打包

**基本写法：创建 jar**
`jar cf <文件>.jar -C <目录> .`
```bash
# 把 bin 目录打包成 app.jar
jar cf app.jar -C bin .
```

---

**基本写法：创建可执行 jar**
`jar cfe <文件>.jar <主类> -C <目录> .`
```bash
# 指定主类打成可执行 jar
jar cfe app.jar com.example.Main -C bin .
```

---

**基本写法：查看 jar 内容**
`jar tf <文件>.jar`
```bash
# 列出 jar 中的条目
jar tf app.jar
```

---

**基本写法：解压 jar**
`jar xf <文件>.jar`
```bash
# 解压到当前目录
jar xf app.jar
```

---

## jshell 交互式 REPL

**基本写法：启动 jshell**
`jshell`
```bash
# 启动 Java 交互式环境
jshell
```

---

**基本写法：执行片段**
`jshell -e "<表达式>"`
```bash
# 直接执行表达式
jshell -e "System.out.println(1+2)"
```

---

**基本写法：加载文件**
`/open <文件>`
```bash
# 在 jshell 中加载源文件
/open Main.java
```

---

## jpackage 打包

**基本写法：打包应用**
`jpackage --input <目录> --name <名称> --main-jar <文件> --main-class <类>`
```bash
# 打包成原生安装包
jpackage --input bin --name MyApp --main-jar app.jar --main-class com.example.Main
```

---

**基本写法：指定类型**
`jpackage --type <类型> --input <目录> --name <名称>`
```bash
# 指定输出类型 msi/exe/dmg/rpm/deb
jpackage --type msi --input bin --name MyApp --main-jar app.jar
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
