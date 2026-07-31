# Java 虚拟线程 API 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建虚拟线程

**基本写法：快速启动虚拟线程**
`Thread.startVirtualThread(<Runnable>)`
```java
// 创建并立即启动一个虚拟线程（Java 21+）
Thread vt = Thread.startVirtualThread(() -> {
    System.out.println("运行于: " + Thread.currentThread());
});
vt.join();
```

---

**基本写法：使用 Builder 创建**
`Thread.ofVirtual().start(<Runnable>)`
```java
// 通过 Builder 创建并启动
Thread vt = Thread.ofVirtual().start(() -> {
    doWork();
});
```

---

**基本写法：创建未启动的虚拟线程**
`Thread.ofVirtual().unstarted(<Runnable>)`
```java
// 先创建 Thread 引用，后续手动 start
Thread vt = Thread.ofVirtual().name("worker-1").unstarted(() -> doWork());
vt.start();
```

---

**基本写法：命名虚拟线程**
`Thread.ofVirtual().name(<名称>).start(...)`
```java
// 指定线程名称便于排查
Thread vt = Thread.ofVirtual()
    .name("db-worker")
    .start(() -> queryDatabase());
```

---

**基本写法：命名前缀 + 计数**
`Thread.ofVirtual().name(<前缀>, <起始>).start(...)`
```java
// 名称形如 worker-0、worker-1、worker-2...
Thread vt = Thread.ofVirtual()
    .name("worker-", 0)
    .start(() -> doWork());
```

---

**基本写法：设置未捕获异常处理器**
`Thread.ofVirtual().uncaughtExceptionHandler(<handler>).start(...)`
```java
// 虚拟线程异常未捕获时回调
Thread vt = Thread.ofVirtual()
    .uncaughtExceptionHandler((t, e) ->
        System.err.println(t.getName() + " 异常: " + e.getMessage()))
    .start(() -> { throw new RuntimeException("boom"); });
```

---

## 虚拟线程执行器

**基本写法：每任务一虚拟线程的执行器**
`Executors.newVirtualThreadPerTaskExecutor()`
```java
// 适用于提交大量任务，每个任务一个虚拟线程
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> doWork());
    executor.submit(() -> doWork());
}
```

---

**基本写法：批量提交任务**
`<executor>.submit(<task>)`
```java
// 提交大量任务，每个任务在独立虚拟线程上运行
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    List<Future<String>> futures = new ArrayList<>();
    for (int i = 0; i < 10_000; i++) {
        final int id = i;
        futures.add(executor.submit(() -> "result-" + id));
    }
    for (Future<String> f : futures) {
        System.out.println(f.get());
    }
}
```

---

**基本写法：执行器作为 ThreadFactory**
`Thread.ofVirtual().factory()`
```java
// 获取虚拟线程工厂，供自定义执行器使用
ThreadFactory factory = Thread.ofVirtual().name("vt-", 0).factory();
ExecutorService executor = Executors.newThreadPerTaskExecutor(factory);
```

---

## 判断线程类型

**基本写法：判断是否为虚拟线程**
`<thread>.isVirtual()`
```java
// 返回 true 表示当前为虚拟线程
boolean isVirtual = Thread.currentThread().isVirtual();
```

---

**基本写法：判断任意线程**
`Thread.ofVirtual().start(...).isVirtual()`
```java
// 用于日志或调试时区分线程类型
Thread vt = Thread.startVirtualThread(() -> { });
System.out.println("isVirtual: " + vt.isVirtual());
```

---

## 平台线程对比

**基本写法：创建平台线程**
`Thread.ofPlatform().start(<Runnable>)`
```java
// 传统 OS 线程，1:1 映射到内核线程
Thread pt = Thread.ofPlatform().name("platform-1").start(() -> doWork());
```

---

**基本写法：Builder 平台线程属性配置**
`Thread.ofPlatform().name(...).priority(...).start(...)`
```java
// 平台线程支持更丰富的属性设置
Thread pt = Thread.ofPlatform()
    .name("io-thread")
    .priority(Thread.MAX_PRIORITY)
    .start(() -> doWork());
```

---

## 阻塞操作

**基本写法：虚拟线程中的阻塞调用**
`Thread.sleep(<duration>)`
```java
// 阻塞时虚拟线程会让出载体线程，不浪费 OS 线程
Thread.startVirtualThread(() -> {
    Thread.sleep(Duration.ofSeconds(1));
});
```

---

**基本写法：阻塞 IO 操作**
`<channel>.read(...)` / `<socket>.connect(...)`
```java
// 网络 IO 阻塞时自动让出载体线程
Thread.startVirtualThread(() -> {
    try (Socket socket = new Socket("example.com", 80)) {
        socket.getInputStream().readAllBytes();
    }
});
```

---

## 等待与协调

**基本写法：等待虚拟线程结束**
`<thread>.join()`
```java
// 等待虚拟线程执行完成
Thread vt = Thread.startVirtualThread(() -> doWork());
vt.join();
```

---

**基本写法：带超时的等待**
`<thread>.join(<超时>)`
```java
// 最多等待 5 秒
Thread vt = Thread.startVirtualThread(() -> doWork());
if (!vt.join(Duration.ofSeconds(5))) {
    System.out.println("任务超时");
}
```

---

**基本写法：使用 CountDownLatch 协调**
`new CountDownLatch(<n>)`
```java
// 多虚拟线程同步点
CountDownLatch latch = new CountDownLatch(3);
for (int i = 0; i < 3; i++) {
    Thread.startVirtualThread(() -> {
        try { doWork(); } finally { latch.countDown(); }
    });
}
latch.await();
```

---

## 虚拟线程与锁

**基本写法：使用 ReentrantLock 推荐替代 synchronized**
`ReentrantLock`
```java
// synchronized 会 pin 虚拟线程，ReentrantLock 更友好
ReentrantLock lock = new ReentrantLock();
Thread.startVirtualThread(() -> {
    lock.lock();
    try { doWork(); } finally { lock.unlock(); }
});
```

---

**基本写法：避免在 synchronized 中阻塞**
`synchronized (<锁>) { <阻塞调用> }`
```java
// 不推荐：阻塞会 pin 住载体线程
synchronized (lock) {
    Thread.sleep(1000); // 应改用 ReentrantLock
}
```

---

## 结构化并发（Java 21 预览）

**基本写法：结构化任务作用域**
`StructuredTaskScope.open()`
```java
// 父子任务生命周期绑定（预览特性）
try (var scope = StructuredTaskScope.open()) {
    Subtask<String> user = scope.fork(() -> fetchUser());
    Subtask<Order> order = scope.fork(() -> fetchOrder());
    scope.join();
    System.out.println(user.get() + " " + order.get());
}
```

---

**基本写法：关闭策略 ShutdownOnFailure**
`new StructuredTaskScope.ShutdownOnFailure()`
```java
// 任一失败则取消所有任务
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Subtask<String> a = scope.fork(() -> queryA());
    Subtask<String> b = scope.fork(() -> queryB());
    scope.join();
    scope.throwIfFailed();
    System.out.println(a.get() + " " + b.get());
}
```

---

## 作用域值（Java 21 预览）

**基本写法：定义 ScopedValue**
`private static final ScopedValue<String> USER = ScopedValue.newInstance()`
```java
// 替代 ThreadLocal 的不可变线程局部值
static final ScopedValue<String> USER = ScopedValue.newInstance();
ScopedValue.where(USER, "Alice").run(() -> {
    System.out.println(USER.get());
});
```

---

## 虚拟线程适用场景

**基本写法：IO 密集型任务**
`Thread.startVirtualThread(() -> { <IO 调用> })`
```java
// 适用于网络请求、数据库查询、文件读写等阻塞场景
Thread.startVirtualThread(() -> httpClient.send(request, BodyHandlers.ofString()));
```

---

**基本写法：CPU 密集型任务不推荐**
`Thread.ofPlatform().start(...)`
```java
// CPU 密集型任务应使用平台线程或 ForkJoinPool
Thread.ofPlatform().start(() -> heavyCompute());
```

---

## Spring Boot 启用虚拟线程

**基本写法：开启虚拟线程支持**
`spring.threads.virtual.enabled: true`
```java
// application.yml 启用虚拟线程处理请求
spring:
  threads:
    virtual:
      enabled: true
```

---

**基本写法：自定义 Tomcat 协议处理器**
`protocolHandler`
```java
// 底层机制：Tomcat 使用虚拟线程处理每个请求
// 配置 enabled=true 后，请求处理将运行在虚拟线程上
```

---

## 调试与观测

**基本写法：线程转储**
`jcmd <pid> Thread.dump_to_file -format=json <file>`
```java
// 输出包含虚拟线程的线程转储
// jcmd <pid> Thread.dump_to_file -format=json dump.json
```

---

**基本写法：检测 pinning**
`-Djdk.tracePinnedThreads=full`
```java
// JVM 启动参数检测被 pin 住的虚拟线程
// java -Djdk.tracePinnedThreads=full -jar app.jar
```

---

## 注意事项

**基本写法：不要池化虚拟线程**
`Thread.startVirtualThread(<task>)`
```java
// 虚拟线程用完即弃，无需复用，无池化必要
Thread.startVirtualThread(() -> doWork());
```

---

**基本写法：避免大量使用 ThreadLocal**
`ThreadLocal.withInitial(...)`
```java
// 百万虚拟线程会复制 ThreadLocal，内存开销大
// 推荐改用 ScopedValue（预览特性）
```
