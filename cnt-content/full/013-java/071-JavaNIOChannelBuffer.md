---
order: 710
title: Java NIO 通道与缓冲区
module: 'java'
category: 后端技术
difficulty: beginner
description: Java NIO 通道与缓冲区 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## Buffer 创建

**基本写法：创建字节缓冲区**
`ByteBuffer.allocate(<容量>);`
```java
// 分配堆内字节缓冲区
ByteBuffer buf = ByteBuffer.allocate(1024);
```

---

**基本写法：创建直接缓冲区**
`ByteBuffer.allocateDirect(<容量>);`
```java
// 分配堆外直接缓冲区（减少拷贝）
ByteBuffer direct = ByteBuffer.allocateDirect(1024);
```

---

**基本写法：包装数组**
`ByteBuffer.wrap(<字节数组>);`
```java
// 包装现有数组为 Buffer
ByteBuffer buf = ByteBuffer.wrap(new byte[]{1, 2, 3});
```

---

## Buffer 读写操作

**基本写法：写入数据**
`<buffer>.put(<值>);`
```java
// 向缓冲区写入字节
buf.put((byte) 65);
```

---

**基本写法：读取数据**
`<buffer>.get();`
```java
// 从缓冲区读取字节
byte b = buf.get();
```

---

**基本写法：切换为读模式**
`<buffer>.flip();`
```java
// 写完后翻转为读模式
buf.flip();
```

---

**基本写法：重置位置**
`<buffer>.rewind();`
```java
// 重置 position 以便重新读
buf.rewind();
```

---

**基本写法：清空缓冲区**
`<buffer>.clear();`
```java
// 清空缓冲区准备再次写入
buf.clear();
```

---

**基本写法：压缩缓冲区**
`<buffer>.compact();`
```java
// 压缩未读数据到头部
buf.compact();
```

---

## Buffer 状态属性

**基本写法：获取容量**
`<buffer>.capacity();`
```java
// 获取缓冲区容量
int cap = buf.capacity();
```

---

**基本写法：获取位置**
`<buffer>.position();`
```java
// 获取当前位置
int pos = buf.position();
```

---

**基本写法：获取限制**
`<buffer>.limit();`
```java
// 获取限制位置
int limit = buf.limit();
```

---

**基本写法：获取剩余量**
`<buffer>.remaining();`
```java
// 获取剩余可读元素数量
int rem = buf.remaining();
```

---

## FileChannel 文件通道

**基本写法：从文件获取通道**
`FileChannel.open(<路径>, <打开选项>...);`
```java
// 打开文件通道
FileChannel ch = FileChannel.open(Path.of("a.txt"), StandardOpenOption.READ);
```

---

**基本写法：通道读入缓冲区**
`<channel>.read(<buffer>);`
```java
// 从通道读取到 Buffer
int n = ch.read(buf);
```

---

**基本写法：缓冲区写入通道**
`<channel>.write(<buffer>);`
```java
// 将 Buffer 数据写入通道
ch.write(buf);
```

---

**基本写法：传输文件**
`<channel>.transferTo(<位置>, <数量>, <目标通道>);`
```java
// 零拷贝传输文件内容
src.transferTo(0, src.size(), dst);
```

---

## Scatter / Gather

**基本写法：分散读**
`<channel>.read(<buffer数组>);`
```java
// 一次读入多个 Buffer
ByteBuffer[] bufs = {header, body};
channel.read(bufs);
```

---

**基本写法：聚集写**
`<channel>.write(<buffer数组>);`
```java
// 多个 Buffer 一次写出
ByteBuffer[] bufs = {header, body};
channel.write(bufs);
```

---

## Selector 选择器

**基本写法：创建选择器**
`Selector.open();`
```java
// 打开选择器
Selector selector = Selector.open();
```

---

**基本写法：注册通道到选择器**
`<channel>.register(<selector>, <就绪事件>);`
```java
// 注册通道为可读事件
channel.configureBlocking(false);
channel.register(selector, SelectionKey.OP_READ);
```

---

**基本写法：选择就绪通道**
`<selector>.select();`
```java
// 阻塞直到有就绪通道
int ready = selector.select();
```

---

**基本写法：获取就绪键**
`<selector>.selectedKeys();`
```java
// 获取就绪的 SelectionKey 集合
Set<SelectionKey> keys = selector.selectedKeys();
```

---

## Charset 字符编码

**基本写法：编码字符串到字节**
`<charset>.encode(<字符串>);`
```java
// 使用 UTF-8 编码
ByteBuffer b = StandardCharsets.UTF_8.encode("hello");
```

---

**基本写法：解码字节到字符串**
`<charset>.decode(<buffer>);`
```java
// 使用 UTF-8 解码
String s = StandardCharsets.UTF_8.decode(buf).toString();
```

---

## Path 路径操作

**基本写法：创建路径**
`Path.of("<路径>");`
```java
// 创建 Path 对象
Path p = Path.of("a", "b", "c.txt");
```

---

**基本写法：读取文件所有字节**
`Files.readAllBytes(<路径>);`
```java
// 一次性读取小文件全部字节
byte[] all = Files.readAllBytes(Path.of("a.txt"));
```

---

**基本写法：写入文件**
`Files.write(<路径>, <字节数组>);`
```java
// 写入字节数组到文件
Files.write(Path.of("out.txt"), bytes);
```

---

**基本写法：按行读取**
`Files.readAllLines(<路径>);`
```java
// 按行读取文件
List<String> lines = Files.readAllLines(Path.of("a.txt"));
```

---

## 异步文件通道

**基本写法：打开异步文件通道**
`AsynchronousFileChannel.open(<路径>, <选项>...);`
```java
// 打开异步文件通道
AsynchronousFileChannel ch = AsynchronousFileChannel.open(
    Path.of("a.txt"), StandardOpenOption.READ);
```

---

**基本写法：异步读取**
`<channel>.read(<buffer>, <位置>, <附件>, <完成处理器>);`
```java
// 异步读取并回调
ch.read(buf, 0, null, new CompletionHandler<Integer, Object>() {
    public void completed(Integer n, Object att) { }
    public void failed(Throwable e, Object att) { }
});
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
