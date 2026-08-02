---
order: 760
title: 启动 REPL 交互环境
module: java

category: '013-java'
difficulty: beginner
description: 启动 REPL 交互环境 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

﻿# Java jshell 与 jpackage 命令速查手册

---

## jshell 启动

**基本写法：进入交互**
`jshell`
```bash
# 启动 REPL 交互环境
jshell
```

---

**基本写法：指定版本进入**
`jshell --execution <模式>`
```bash
# 本地执行模式
jshell --execution local
```

---

**基本写法：执行片段**
`jshell -e "<代码>"`
```bash
# 直接执行单段代码
jshell -e "System.out.println(\"hi\");"
```

---

## jshell 会话控制

**基本写法：加载文件**
`/open <文件路径>`
```java
// 在 jshell 内加载脚本文件
/open snippet.java
```

---

**基本写法：保存片段**
`/save <文件路径>`
```java
// 保存当前会话片段到文件
/save session.java
```

---

**基本写法：列出片段**
`/list`
```java
// 列出已输入的代码片段（带编号）
/list
// 仅列出有效片段
/list -all
```

---

**基本写法：查看变量**
`/vars`
```java
// 列出已定义的变量及值
/vars
```

---

**基本写法：查看方法**
`/methods`
```java
// 列出已定义的方法
/methods
```

---

**基本写法：查看类型**
`/types`
```java
// 列出已定义的类与接口
/types
```

---

**基本写法：查看导入**
`/imports`
```java
// 列出已导入的包
/imports
```

---

**基本写法：编辑片段**
`/edit <片段编号>`
```java
// 用外部编辑器编辑片段
/edit 1
```

---

**基本写法：重置会话**
`/reset`
```java
// 清空所有片段，重新开始
/reset
```

---

**基本写法：退出**
`/exit`
```java
// 退出 jshell
/exit
```

---

## jshell 设置

**基本写法：设置反馈模式**
`/set feedback <模式>`
```java
// concise / normal / silent / verbose
/set feedback verbose
```

---

**基本写法：添加导入**
`import <包名>;`
```java
// 直接输入 import 语句即可
import java.util.stream.*;
```

---

**基本写法：执行外部命令**
`/!<shell 命令>`
```java
// 在 jshell 中执行系统命令
/! javac -version
```

---

**基本写法：设置类路径**
`jshell --class-path <路径>`
```bash
# 启动时指定类路径
jshell --class-path "lib/*;bin"
```

---

## jpackage 基础

**基本写法：构建 Windows 安装包**
`jpackage --name <名称> --input <输入> --main-jar <主jar>`
```bash
# 打包成 Windows 安装程序（msi/exe）
jpackage --name MyApp --input target --main-jar app.jar
```

---

**基本写法：指定主类**
`jpackage --name <名称> --module <模块>/<主类>`
```bash
# 模块化应用打包
jpackage --name MyApp --module com.example.app/com.example.app.Main
```

---

**基本写法：指定运行时镜像**
`jpackage --runtime-image <镜像目录>`
```bash
# 使用自定义 JRE
jpackage --name MyApp --input target --main-jar app.jar --runtime-image myjre
```

---

## jpackage 平台选项

**基本写法：Windows 安装器类型**
`jpackage --win-msi`
```bash
# 生成 MSI 安装包
jpackage --name MyApp --input target --main-jar app.jar --win-msi
```

---

**基本写法：Windows 快捷方式**
`jpackage --win-shortcut --win-menu`
```bash
# 创建桌面快捷方式与开始菜单项
jpackage --name MyApp --input target --main-jar app.jar --win-shortcut --win-menu
```

---

**基本写法：macOS dmg**
`jpackage --type dmg --name <名称>`
```bash
# 生成 macOS dmg 镜像
jpackage --type dmg --name MyApp --module com.example.app/com.example.app.Main
```

---

**基本写法：macOS 应用图标**
`jpackage --icon <icns 文件>`
```bash
# 指定应用图标
jpackage --name MyApp --input target --main-jar app.jar --icon icon.icns
```

---

**基本写法：Linux deb/rpm**
`jpackage --type <deb|rpm>`
```bash
# 生成 Linux 安装包
jpackage --type deb --name myapp --input target --main-jar app.jar
```

---

## jpackage 应用配置

**基本写法：设置版本与供应商**
`jpackage --app-version <版本> --vendor <供应商>`
```bash
# 应用版本与供应商
jpackage --name MyApp --input target --main-jar app.jar \
    --app-version 1.0.0 --vendor "Acme Inc"
```

---

**基本写法：传入 JVM 参数**
`jpackage --java-options "<参数>"`
```bash
# 启动时传入 JVM 参数
jpackage --name MyApp --input target --main-jar app.jar \
    --java-options "-Xmx512m -Dfile.encoding=UTF-8"
```

---

**基本写法：应用参数**
`jpackage --arguments "<参数>"`
```bash
# 启动应用时传入的命令行参数
jpackage --name MyApp --input target --main-jar app.jar \
    --arguments "--mode=prod"
```

---

**基本写法：关联文件类型**
`jpackage --file-associations <属性文件>`
```bash
# 关联文件扩展名
jpackage --name MyApp --input target --main-jar app.jar \
    --file-associations app.properties
```

---

**基本写法：添加资源**
`jpackage --resource-dir <目录>`
```bash
# 指定图标与许可文件目录
jpackage --name MyApp --input target --main-jar app.jar \
    --resource-dir res
```

---

**基本写法：临时目录与详细输出**
`jpackage --temp <目录> --verbose`
```bash
# 指定临时目录并输出详细信息
jpackage --name MyApp --input target --main-jar app.jar \
    --temp build/tmp --verbose
```

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
