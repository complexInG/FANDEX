---
order: 800
title: Java HttpClient 与 WebSocket 语法速查手册
module: 'java'
category: 后端技术
difficulty: beginner
description: Java HttpClient 与 WebSocket 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## HttpClient 创建

**基本写法：创建客户端**
`HttpClient.newHttpClient();`
```java
// 创建默认 HTTP 客户端
HttpClient client = HttpClient.newHttpClient();
```

---

**基本写法：自定义客户端**
```java
HttpClient.newBuilder()
  .version(<版本>)
  .connectTimeout(<超时>)
  .build();
```
```java
// 配置 HTTP/2 与超时
HttpClient client = HttpClient.newBuilder()
    .version(HttpClient.Version.HTTP_2)
    .connectTimeout(Duration.ofSeconds(10))
    .build();
```

---

## HttpRequest 请求

**基本写法：构建 GET 请求**
```java
HttpRequest.newBuilder()
  .uri(URI.create(<URL>))
  .GET()
  .build();
```
```java
// 构建 GET 请求
HttpRequest req = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/users"))
    .GET()
    .build();
```

---

**基本写法：POST 请求体**
```java
HttpRequest.newBuilder()
  .uri(URI.create(<URL>))
  .POST(HttpRequest.BodyPublishers.ofString(<正文>))
  .build();
```
```java
// 发送 JSON POST 请求
HttpRequest req = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/users"))
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString("{\"name\":\"Tom\"}"))
    .build();
```

---

**基本写法：设置头**
`<builder>.header(<名称>, <值>);`
```java
// 添加请求头
builder.header("Authorization", "Bearer token");
```

---

**基本写法：设置超时**
`<builder>.timeout(<超时>);`
```java
// 请求级超时
builder.timeout(Duration.ofSeconds(5));
```

---

## 发送请求

**基本写法：同步发送**
`<client>.send(<请求>, <响应处理器>);`
```java
// 同步获取响应
HttpResponse<String> resp = client.send(req, HttpResponse.BodyHandlers.ofString());
int code = resp.statusCode();
String body = resp.body();
```

---

**基本写法：异步发送**
`<client>.sendAsync(<请求>, <处理器>);`
```java
// 异步获取响应
client.sendAsync(req, HttpResponse.BodyHandlers.ofString())
    .thenAccept(r -> System.out.println(r.body()));
```

---

**基本写法：响应处理器**
`HttpResponse.BodyHandlers.<类型>();`
```java
// 各种响应体处理器
HttpResponse.BodyHandlers.ofString();   // 字符串
HttpResponse.BodyHandlers.ofByteArray(); // 字节数组
HttpResponse.BodyHandlers.ofFile(Path.of("out.bin")); // 写入文件
HttpResponse.BodyHandlers.discarding();   // 丢弃
```

---

## WebSocket

**基本写法：创建 WebSocket**
```java
<client>.newWebSocketBuilder()
  .buildAsync(URI.create(<URL>), <监听器>)
  .join();
```
```java
// 连接 WebSocket
WebSocket ws = HttpClient.newHttpClient()
    .newWebSocketBuilder()
    .buildAsync(URI.create("wss://example.com/ws"), new WebSocket.Listener() {
        @Override public CompletionStage<?> onText(WebSocket ws, CharSequence data, boolean last) {
            System.out.println("recv: " + data);
            return null;
        }
    })
    .join();
```

---

**基本写法：发送消息**
`<ws>.sendText(<文本>, <是否最后>);`
```java
// 发送文本帧
ws.sendText("hello", true);
```

---

**基本写法：发送二进制**
`<ws>.sendBinary(<字节>, <是否最后>);`
```java
// 发送二进制帧
ws.sendBinary(ByteBuffer.wrap(new byte[]{1,2,3}), true);
```

---

**基本写法：关闭**
`<ws>.sendClose(<状态码>, <原因>);`
```java
// 发送关闭帧
ws.sendClose(WebSocket.NORMAL_CLOSURE, "bye");
```

---

## 传统 Socket

**基本写法：创建客户端**
`new Socket(<host>, <port>);`
```java
// 连接 TCP 服务端
try (Socket s = new Socket("example.com", 8080)) {
    OutputStream out = s.getOutputStream();
    out.write("hi\n".getBytes());
}
```

---

**基本写法：创建服务端**
`new ServerSocket(<端口>);`
```java
// 监听端口
try (ServerSocket ss = new ServerSocket(8080)) {
    Socket client = ss.accept();
    InputStream in = client.getInputStream();
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
