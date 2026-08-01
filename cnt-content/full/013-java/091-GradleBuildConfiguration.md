---
order: 910
title: Gradle build.gradle 配置语法速查手册
module: java

category: '013-java'
difficulty: beginner
description: Gradle build.gradle 配置语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 插件应用

**基本写法：应用插件**
```groovy
plugins {
  id '<插件ID>' version '<版本>'
}
```
```groovy
// 应用 Java 与应用插件
plugins {
    id 'java'
    id 'application'
}
```

---

**基本写法：应用 Kotlin 插件**
```groovy
plugins {
  id 'org.jetbrains.kotlin.jvm' version '<版本>'
}
```
```groovy
// Kotlin JVM 插件
plugins {
    id 'org.jetbrains.kotlin.jvm' version '2.0.0'
}
```

---

## 仓库配置

**基本写法：配置仓库**
```groovy
repositories {
  mavenCentral()
  maven { url '<地址>' }
}
```
```groovy
// 配置依赖来源仓库
repositories {
    mavenCentral()
    maven { url 'https://maven.aliyun.com/repository/public' }
}
```

---

## 依赖配置

**基本写法：添加依赖**
```groovy
dependencies {
  implementation '<组>:<构件>:<版本>'
}
```
```groovy
// 添加各类依赖
dependencies {
    implementation 'com.google.guava:guava:33.0.0-jre'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.0'
    compileOnly 'org.projectlombok:lombok:1.18.32'
    runtimeOnly 'org.postgresql:postgresql:42.7.3'
}
```

---

**基本写法：平台依赖 BOM**
```groovy
implementation platform('<组>:<构件>:<版本>')
```
```groovy
// 使用 Spring Boot BOM 管理版本
dependencies {
    implementation platform('org.springframework.boot:spring-boot-dependencies:3.3.0')
    implementation 'org.springframework.boot:spring-boot-starter-web'
}
```

---

## Java 配置

**基本写法：配置 Java 版本**
```groovy
java {
  sourceCompatibility = JavaVersion.VERSION_21
  targetCompatibility = JavaVersion.VERSION_21
}
```
```groovy
// 设定 Java 21
java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}
```

---

**基本写法：工具链配置**
```groovy
java {
  toolchain {
    languageVersion = JavaLanguageVersion.of(21)
  }
}
```
```groovy
// 使用指定版本 JDK 编译
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}
```

---

## 任务配置

**基本写法：自定义任务**
```groovy
tasks.register('<名称>') {
  doLast { <动作> }
}
```
```groovy
// 定义自定义任务
tasks.register('hello') {
    doLast {
        println 'Hello Gradle'
    }
}
```

---

**基本写法：任务依赖**
`<任务>.dependsOn <其他任务>`
```groovy
// 让 build 依赖 hello
tasks.named('build') {
    dependsOn 'hello'
}
```

---

## 应用配置

**基本写法：指定主类**
```groovy
application {
  mainClass = '<全限定类名>'
}
```
```groovy
// 配置可运行应用主类
application {
    mainClass = 'com.example.Main'
}
```

---

## 测试配置

**基本写法：使用 JUnit 5**
```groovy
test {
  useJUnitPlatform()
}
```
```groovy
// 启用 JUnit 5 平台
test {
    useJUnitPlatform()
    testLogging {
        events 'passed', 'skipped', 'failed'
    }
}
```

---

## 版本与项目信息

**基本写法：项目元信息**
```groovy
group = '<组ID>'
version = '<版本>'
```
```groovy
// 设置项目坐标
group = 'com.example'
version = '1.0.0'
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
