# Java 多线程基础

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建线程

**基本写法：继承 Thread**
`class <类> extends Thread { public void run() {} }`
```java
// 继承 Thread 创建线程
class MyThread extends Thread {
    public void run() { System.out.println("running"); }
}
new MyThread().start();
```

---

**基本写法：实现 Runnable**
`new Thread(<Runnable>).start();`
```java
// 实现 Runnable 接口
new Thread(() -> System.out.println("running")).start();
```

---

**基本写法：实现 Callable**
`class <类> implements Callable<<类型>> { public <类型> call() {} }`
```java
// 带返回值的任务
Callable<Integer> task = () -> 42;
Future<Integer> f = Executors.newSingleThreadExecutor().submit(task);
```

---

## 线程基本操作

**基本写法：启动线程**
`<thread>.start();`
```java
// 启动线程执行 run
thread.start();
```

---

**基本写法：等待线程结束**
`<thread>.join();`
```java
// 阻塞当前线程直到目标结束
thread.join();
```

---

**基本写法：超时等待**
`<thread>.join(<毫秒>);`
```java
// 最多等待 1000 毫秒
thread.join(1000);
```

---

**基本写法：休眠**
`Thread.sleep(<毫秒>);`
```java
// 当前线程休眠 500 毫秒
Thread.sleep(500);
```

---

**基本写法：让出 CPU**
`Thread.yield();`
```java
// 提示调度器让出 CPU
Thread.yield();
```

---

## 线程状态

**基本写法：获取状态**
`<thread>.getState();`
```java
// 获取线程状态枚举
Thread.State s = thread.getState();
```

---

**基本写法：判断存活**
`<thread>.isAlive();`
```java
// 判断线程是否存活
boolean alive = thread.isAlive();
```

---

**基本写法：判断中断**
`<thread>.isInterrupted();`
```java
// 判断线程是否被中断
boolean i = thread.isInterrupted();
```

---

## 中断机制

**基本写法：请求中断**
`<thread>.interrupt();`
```java
// 设置线程中断标志
thread.interrupt();
```

---

**基本写法：检测中断并清除标志**
`Thread.interrupted();`
```java
// 静态方法检测并清除当前线程中断
boolean i = Thread.interrupted();
```

---

**基本写法：响应中断**
`if (Thread.currentThread().isInterrupted()) break;`
```java
// 循环中检测中断
while (!Thread.currentThread().isInterrupted()) {
    doWork();
}
```

---

## synchronized 同步

**基本写法：同步方法**
`public synchronized <返回> <方法>() {}`
```java
// 整个方法同步
public synchronized void inc() { count++; }
```

---

**基本写法：同步代码块**
`synchronized (<对象>) { }`
```java
// 同步代码块减少锁范围
synchronized (this) { count++; }
```

---

**基本写法：同步静态方法**
`public static synchronized <返回> <方法>() {}`
```java
// 静态方法锁 Class 对象
public static synchronized void inc() { total++; }
```

---

**基本写法：同步任意锁对象**
`private final Object <锁> = new Object();`
```java
// 使用私有锁对象
private final Object lock = new Object();
synchronized (lock) { count++; }
```

---

## volatile 关键字

**基本写法：声明 volatile 字段**
`private volatile <类型> <字段>;`
```java
// 保证可见性但不保证原子性
private volatile boolean running = true;
```

---

## wait / notify

**基本写法：等待**
`<对象>.wait();`
```java
// 释放锁并等待通知
synchronized (lock) {
    while (!ready) lock.wait();
}
```

---

**基本写法：通知一个**
`<对象>.notify();`
```java
// 唤醒一个等待线程
synchronized (lock) {
    ready = true;
    lock.notify();
}
```

---

**基本写法：通知所有**
`<对象>.notifyAll();`
```java
// 唤醒所有等待线程
synchronized (lock) {
    lock.notifyAll();
}
```

---

**基本写法：超时等待**
`<对象>.wait(<毫秒>);`
```java
// 最多等待 1000 毫秒
lock.wait(1000);
```

---

## 线程优先级

**基本写法：设置优先级**
`<thread>.setPriority(<级别>);`
```java
// 设置线程优先级 1-10
thread.setPriority(Thread.MAX_PRIORITY);
```

---

**基本写法：守护线程**
`<thread>.setDaemon(true);`
```java
// 设置为守护线程（主线程退出即结束）
thread.setDaemon(true);
thread.start();
```

---

## 线程异常处理

**基本写法：设置未捕获异常处理器**
`<thread>.setUncaughtExceptionHandler(<处理器>);`
```java
// 设置线程异常处理器
thread.setUncaughtExceptionHandler((t, e) -> {
    System.out.println(t.getName() + " " + e);
});
```

---

**基本写法：全局默认处理器**
`Thread.setDefaultUncaughtExceptionHandler(<处理器>);`
```java
// 设置全局默认异常处理器
Thread.setDefaultUncaughtExceptionHandler((t, e) -> log.error(e));
```

---

## 线程工厂

**基本写法：自定义线程工厂**
`new ThreadFactory() { public Thread newThread(Runnable r) {} }`
```java
// 自定义线程创建
ThreadFactory factory = r -> {
    Thread t = new Thread(r);
    t.setName("worker-" + t.getId());
    t.setDaemon(true);
    return t;
};
```

---

## 线程局部变量（简化版）

**基本写法：使用 ThreadLocal**
`ThreadLocal.<类型>withInitial(() -> <值>);`
```java
// 线程私有计数器
ThreadLocal<Integer> tl = ThreadLocal.withInitial(() -> 0);
```

---

## Thread 类静态方法

**基本写法：获取当前线程**
`Thread.currentThread();`
```java
// 获取当前执行线程
Thread t = Thread.currentThread();
```

---

**基本写法：获取所有栈帧**
`Thread.getAllStackTraces();`
```java
// 获取所有活动线程的栈帧
Map<Thread, StackTraceElement[]> m = Thread.getAllStackTraces();
```

---

**基本写法：onSpinWait 提示**
`Thread.onSpinWait();`
```java
// Java 9+ 自旋等待提示优化
while (!ready) Thread.onSpinWait();
```
