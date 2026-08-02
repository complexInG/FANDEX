---
order: 900
title: Maven pom.xml 配置语法速查手册
module: 'java'
category: 后端技术
difficulty: beginner
description: Maven pom.xml 配置语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## 项目坐标

**基本写法：定义项目坐标**
```xml
<groupId><组ID></groupId>
<artifactId><构件ID></artifactId>
<version><版本></version>
```
```xml
<!-- 项目唯一标识 -->
<groupId>com.example</groupId>
<artifactId>my-app</artifactId>
<version>1.0.0</version>
```

---

**基本写法：定义打包类型**
`<packaging><类型></packaging>`
```xml
<!-- jar/war/pom/ear -->
<packaging>jar</packaging>
```

---

## 属性定义

**基本写法：定义属性**
```xml
<properties>
  <属性名>属性值</属性名>
</properties>
```
```xml
<!-- 集中管理版本号 -->
<properties>
  <maven.compiler.release>21</maven.compiler.release>
  <junit.version>5.10.0</junit.version>
</properties>
```

---

## 依赖配置

**基本写法：添加依赖**
```xml
<dependency>
  <groupId><组ID></groupId>
  <artifactId><构件ID></artifactId>
  <version><版本></version>
</dependency>
```
```xml
<!-- 引入 JUnit 5 -->
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter</artifactId>
  <version>${junit.version}</version>
  <scope>test</scope>
</dependency>
```

---

**基本写法：依赖范围**
`<scope><范围></scope>`
```xml
<!-- compile/provided/runtime/test/system -->
<scope>test</scope>
```

---

**基本写法：排除传递依赖**
```xml
<exclusions>
  <exclusion>
    <groupId><组ID></groupId>
    <artifactId><构件ID></artifactId>
  </exclusion>
</exclusions>
```
```xml
<!-- 排除不想要的传递依赖 -->
<exclusions>
  <exclusion>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
  </exclusion>
</exclusions>
```

---

## 构建配置

**基本写法：指定输出目录**
```xml
<build>
  <finalName><名称></finalName>
  <sourceDirectory><目录></sourceDirectory>
</build>
```
```xml
<!-- 自定义构建产物名 -->
<build>
  <finalName>my-app</finalName>
</build>
```

---

**基本写法：配置插件**
```xml
<plugin>
  <groupId><组ID></groupId>
  <artifactId><构件ID></artifactId>
  <version><版本></version>
  <configuration>...</configuration>
</plugin>
```
```xml
<!-- 配置编译插件 -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.13.0</version>
  <configuration>
    <release>21</release>
  </configuration>
</plugin>
```

---

**基本写法：插件执行目标**
```xml
<executions>
  <execution>
    <phase><阶段></phase>
    <goals><goal><目标></goal></goals>
  </execution>
</executions>
```
```xml
<!-- 绑定插件到生命周期阶段 -->
<executions>
  <execution>
    <phase>package</phase>
    <goals>
      <goal>shade</goal>
    </goals>
  </execution>
</executions>
```

---

## 仓库配置

**基本写法：配置仓库**
```xml
<repositories>
  <repository>
    <id><ID></id>
    <url><地址></url>
  </repository>
</repositories>
```
```xml
<!-- 添加阿里云镜像仓库 -->
<repositories>
  <repository>
    <id>aliyun</id>
    <url>https://maven.aliyun.com/repository/public</url>
  </repository>
</repositories>
```

---

## 多模块聚合

**基本写法：聚合子模块**
```xml
<modules>
  <module><模块名></module>
</modules>
```
```xml
<!-- 聚合多个子模块 -->
<modules>
  <module>core</module>
  <module>web</module>
  <module>service</module>
</modules>
```

---

## dependencyManagement

**基本写法：统一版本管理**
```xml
<dependencyManagement>
  <dependencies>
    <dependency>...</dependency>
  </dependencies>
</dependencyManagement>
```
```xml
<!-- 父 pom 中统一定义版本 -->
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-dependencies</artifactId>
      <version>3.3.0</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
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
