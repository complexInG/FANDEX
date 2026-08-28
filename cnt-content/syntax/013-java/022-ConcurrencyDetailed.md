# Java 并发工具速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Lock 锁机制

**基本写法：使用 ReentrantLock**
`ReentrantLock <lock> = new ReentrantLock()`
```java
// 显式加锁与释放锁（必须在 finally 中释放）
ReentrantLock lock = new ReentrantLock();
lock.lock();
try {
    // 临界区代码
} finally {
    lock.unlock();
}
```

---

**基本写法：可中断锁获取**
`<lock>.lockInterruptibly()`
```java
// 等待锁过程中可被中断
lock.lockInterruptibly();
try {
    // 临界区代码
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
} finally {
    lock.unlock();
}
```

---

**基本写法：尝试获取锁**
`<lock>.tryLock(<超时>, <单位>)`
```java
// 尝试在 3 秒内获取锁，失败则跳过
if (lock.tryLock(3, TimeUnit.SECONDS)) {
    try {
        // 获取锁成功
    } finally {
        lock.unlock();
    }
}
```

---

**基本写法：读写锁**
`ReentrantReadWriteLock`
```java
// 读多写少场景提升并发度
ReentrantReadWriteLock rwLock = new ReentrantReadWriteLock();
rwLock.readLock().lock();
try { /* 读操作 */ } finally { rwLock.readLock().unlock(); }
rwLock.writeLock().lock();
try { /* 写操作 */ } finally { rwLock.writeLock().unlock(); }
```

---

**基本写法：Condition 条件变量**
`<lock>.newCondition()`
```java
// 配合 Lock 实现等待/通知
Condition notEmpty = lock.newCondition();
lock.lock();
try {
    while (queue.isEmpty()) {
        notEmpty.await();
    }
    // 消费元素
} finally {
    lock.unlock();
}
```

---

## CountDownLatch 倒计时门闩

**基本写法：等待 N 个线程完成**
`CountDownLatch <latch> = new CountDownLatch(<count>)`
```java
// 主线程等待所有工作线程完成
CountDownLatch latch = new CountDownLatch(3);
for (int i = 0; i < 3; i++) {
    new Thread(() -> {
        try { doWork(); } finally { latch.countDown(); }
    }).start();
}
latch.await();
```

---

**基本写法：带超时等待**
`<latch>.await(<超时>, <单位>)`
```java
// 最多等待 5 秒
boolean done = latch.await(5, TimeUnit.SECONDS);
if (!done) { /* 超时处理 */ }
```

---

**基本写法：递减计数**
`<latch>.countDown()`
```java
// 计数减 1，归零时唤醒 await 的线程
latch.countDown();
```

---

## CyclicBarrier 循环屏障

**基本写法：N 个线程到达屏障后统一放行**
`CyclicBarrier <barrier> = new CyclicBarrier(<count>)`
```java
// 3 个线程都到达后才继续执行
CyclicBarrier barrier = new CyclicBarrier(3);
new Thread(() -> {
    barrier.await(); // 等待其他线程
}).start();
```

---

**基本写法：屏障动作**
`new CyclicBarrier(<count>, <Runnable>)`
```java
// 所有线程到达后执行一次动作
CyclicBarrier barrier = new CyclicBarrier(3, () -> {
    System.out.println("所有线程到达屏障");
});
barrier.await();
```

---

## Semaphore 信号量

**基本写法：限流并发访问**
`Semaphore <sem> = new Semaphore(<许可数>)`
```java
// 同时只允许 5 个线程访问资源
Semaphore sem = new Semaphore(5);
sem.acquire();
try {
    // 访问受限资源
} finally {
    sem.release();
}
```

---

**基本写法：批量获取许可**
`<sem>.acquire(<数量>)`
```java
// 一次获取 3 个许可
sem.acquire(3);
try { /* 资源使用 */ } finally { sem.release(3); }
```

---

## ConcurrentHashMap

**基本写法：创建并发 Map**
`new ConcurrentHashMap<K, V>()`
```java
// 线程安全的 HashMap
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
map.put("a", 1);
```

---

**基本写法：原子更新**
`<map>.compute(<key>, <BiFunction>)`
```java
// 原子地更新指定 key 的值
map.compute("a", (k, v) -> v == null ? 1 : v + 1);
```

---

**基本写法：不存在时放入**
`<map>.putIfAbsent(<key>, <value>)`
```java
// 仅当 key 不存在时才放入
map.putIfAbsent("b", 100);
```

---

**基本写法：合并值**
`<map>.merge(<key>, <默认值>, <BiFunction>)`
```java
// 统计词频的惯用写法
map.merge(word, 1, Integer::sum);
```

---

**基本写法：原子替换**
`<map>.replace(<key>, <旧值>, <新值>)`
```java
// CAS 替换，旧值匹配才更新
boolean ok = map.replace("a", 1, 2);
```

---

## 原子类

**基本写法：原子整数**
`AtomicInteger <ai> = new AtomicInteger(<初始值>)`
```java
// 无锁线程安全的整数
AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();
int now = counter.get();
```

---

**基本写法：CAS 更新**
`<ai>.compareAndSet(<期望值>, <新值>)`
```java
// 期望值匹配才更新
boolean updated = counter.compareAndSet(0, 1);
```

---

**基本写法：累加器（高并发更优）**
`LongAdder <adder> = new LongAdder()`
```java
// 高并发计数性能优于 AtomicLong
LongAdder adder = new LongAdder();
adder.increment();
long sum = adder.sum();
```

---

**基本写法：原子引用**
`AtomicReference<T> <ref> = new AtomicReference<>(<初始值>)`
```java
// 引用类型的原子更新
AtomicReference<String> ref = new AtomicReference<>("init");
ref.compareAndSet("init", "updated");
```

---

**基本写法：字段原子更新器**
`AtomicIntegerFieldUpdater.newUpdater(<类>.class, "<字段名>")`
```java
// 对 volatile 字段进行原子更新
class Account {
    volatile int balance;
}
AtomicIntegerFieldUpdater<Account> u =
    AtomicIntegerFieldUpdater.newUpdater(Account.class, "balance");
u.incrementAndGet(account);
```

---

## 并发集合

**基本写法：阻塞队列**
`ArrayBlockingQueue<E> <q> = new ArrayBlockingQueue<>(<容量>)`
```java
// 生产者-消费者模式
ArrayBlockingQueue<String> q = new ArrayBlockingQueue<>(100);
q.put("task");          // 队列满则阻塞
String task = q.take(); // 队列空则阻塞
```

---

**基本写法：并发链表队列**
`ConcurrentLinkedQueue<E>`
```java
// 无界非阻塞队列（基于 CAS）
ConcurrentLinkedQueue<Integer> q = new ConcurrentLinkedQueue<>();
q.offer(1);
Integer head = q.poll();
```

---

**基本写法：并发跳表 Map**
`ConcurrentSkipListMap<K, V>`
```java
// 线程安全的有序 Map
ConcurrentSkipListMap<String, Integer> map = new ConcurrentSkipListMap<>();
map.put("b", 2);
map.put("a", 1);
```

---

## 线程池

**基本写法：固定大小线程池**
`Executors.newFixedThreadPool(<大小>)`
```java
// 固定线程数的线程池
ExecutorService pool = Executors.newFixedThreadPool(4);
pool.submit(() -> System.out.println("task"));
pool.shutdown();
```

---

**基本写法：自定义线程池**
`new ThreadPoolExecutor(...)`
```java
// 推荐方式，参数可控
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    2, 4, 60L, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(1000),
    Executors.defaultThreadFactory(),
    new ThreadPoolExecutor.CallerRunsPolicy()
);
```

---

**基本写法：定时任务线程池**
`Executors.newScheduledThreadPool(<大小>)`
```java
// 延迟或周期执行任务
ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(2);
scheduler.scheduleAtFixedRate(() -> doWork(), 0, 1, TimeUnit.SECONDS);
```

---

**基本写法：优雅关闭**
`<pool>.shutdown()` + `<pool>.awaitTermination(...)`
```java
// 优雅关闭线程池
pool.shutdown();
if (!pool.awaitTermination(60, TimeUnit.SECONDS)) {
    pool.shutdownNow();
}
```

---

## 同步工具

**基本写法：交换器**
`Exchanger<T>`
```java
// 两个线程交换数据
Exchanger<String> exchanger = new Exchanger<>();
String received = exchanger.exchange("data");
```

---

**基本写法：同步队列**
`SynchronousQueue<E>`
```java
// 无容量，put 必须等待 take
SynchronousQueue<String> q = new SynchronousQueue<>();
new Thread(() -> q.put("hello")).start();
String data = q.take();
```

---

## CompletableFuture 并发

**基本写法：异步执行任务**
`CompletableFuture.supplyAsync(<Supplier>)`
```java
// 异步执行有返回值的任务
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    return fetchData();
});
String result = future.get();
```

---

**基本写法：链式转换**
`<future>.thenApply(<Function>)`
```java
// 任务完成后转换结果
CompletableFuture<Integer> f = future.thenApply(String::length);
```

---

**基本写法：组合两个任务**
`<future1>.thenCombine(<future2>, <BiFunction>)`
```java
// 等两个任务都完成后合并结果
CompletableFuture<Integer> combined = f1.thenCombine(f2, (a, b) -> a + b);
```

---

**基本写法：等待全部完成**
`CompletableFuture.allOf(<future>...)`
```java
// 等待所有任务完成
CompletableFuture.allOf(f1, f2, f3).join();
```

---

## ThreadLocal

**基本写法：线程本地变量**
`ThreadLocal<T> <tl> = new ThreadLocal<>()`
```java
// 每个线程独立副本
ThreadLocal<SimpleDateFormat> tl =
    ThreadLocal.withInitial(() -> new SimpleDateFormat("yyyy-MM-dd"));
String date = tl.get().format(new Date());
tl.remove(); // 用完清理避免内存泄漏
```
