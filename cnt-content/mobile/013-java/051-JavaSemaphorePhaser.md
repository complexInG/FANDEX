# Java Semaphore 信号量语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Semaphore 信号量

**基本写法：创建信号量**
`new Semaphore(<许可数>);`
```java
// 创建 3 个许可的信号量
Semaphore sem = new Semaphore(3);
```

---

**基本写法：公平信号量**
`new Semaphore(<许可数>, true);`
```java
// 使用公平模式获取许可
Semaphore sem = new Semaphore(3, true);
```

---

**基本写法：获取许可**
`<sem>.acquire();`
```java
// 阻塞获取一个许可
sem.acquire();
```

---

**基本写法：获取多个许可**
`<sem>.acquire(<数量>);`
```java
// 一次获取多个许可
sem.acquire(2);
```

---

**基本写法：释放许可**
`<sem>.release();`
```java
// 释放一个许可
sem.release();
```

---

**基本写法：尝试获取**
`<sem>.tryAcquire();`
```java
// 尝试获取，不阻塞
boolean got = sem.tryAcquire();
```

---

**基本写法：超时获取**
`<sem>.tryAcquire(<超时>, <单位>);`
```java
// 最多等待 5 秒获取许可
boolean ok = sem.tryAcquire(5, TimeUnit.SECONDS);
```

---

**基本写法：剩余许可**
`<sem>.availablePermits();`
```java
// 查询当前可用许可数
int rest = sem.availablePermits();
```

---

## Semaphore 限流示例

**基本写法：用作限流器**
```java
// 限制同时访问的线程数
class RateLimiter {
    private final Semaphore sem;
    public RateLimiter(int max) { sem = new Semaphore(max); }
    public void run(Runnable task) throws InterruptedException {
        sem.acquire();
        try { task.run(); } finally { sem.release(); }
    }
}
```

---
