# Java Lock 与 Condition 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ReentrantLock 基础

**基本写法：创建可重入锁**
`ReentrantLock <变量> = new ReentrantLock();`
```java
// 创建非公平可重入锁
ReentrantLock lock = new ReentrantLock();
```

---

**基本写法：公平锁**
`new ReentrantLock(true);`
```java
// true 表示公平锁（按等待顺序获取）
ReentrantLock lock = new ReentrantLock(true);
```

---

**基本写法：try-finally 加锁**
`<lock>.lock(); <lock>.unlock();`
```java
// 标准加解锁模板
lock.lock();
try {
    // 临界区代码
} finally {
    lock.unlock();
}
```

---

## 非阻塞获取

**基本写法：tryLock 立即返回**
`<lock>.tryLock();`
```java
// 获取成功返回 true，失败立即返回 false
if (lock.tryLock()) {
    try {
        // 拿到锁
    } finally {
        lock.unlock();
    }
}
```

---

**基本写法：tryLock 超时**
`<lock>.tryLock(<超时>, <单位>);`
```java
// 最多等待指定时间
if (lock.tryLock(3, TimeUnit.SECONDS)) {
    try {
        // 拿到锁
    } finally {
        lock.unlock();
    }
}
```

---

**基本写法：可中断加锁**
`<lock>.lockInterruptibly();`
```java
// 等待锁时可以被 interrupt 打断
try {
    lock.lockInterruptibly();
    try {
        // 临界区
    } finally {
        lock.unlock();
    }
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
}
```

---

## Condition 等待通知

**基本写法：创建 Condition**
`<lock>.newCondition();`
```java
// 一个锁可绑定多个条件变量
ReentrantLock lock = new ReentrantLock();
Condition notEmpty = lock.newCondition();
Condition notFull  = lock.newCondition();
```

---

**基本写法：等待**
`<condition>.await();`
```java
// 释放锁并等待，唤醒后重新竞争锁
lock.lock();
try {
    while (queue.isEmpty()) {
        notEmpty.await();
    }
    // 取数据
} finally {
    lock.unlock();
}
```

---

**基本写法：唤醒一个**
`<condition>.signal();`
```java
// 唤醒一个等待在该条件上的线程
lock.lock();
try {
    queue.add(item);
    notEmpty.signal();
} finally {
    lock.unlock();
}
```

---

**基本写法：唤醒全部**
`<condition>.signalAll();`
```java
// 唤醒所有等待线程
notFull.signalAll();
```

---

**基本写法：超时等待**
`<condition>.await(<超时>, <单位>);`
```java
// 最多等待指定时间
boolean woken = notEmpty.await(1, TimeUnit.SECONDS);
```

---

**基本写法：不抛中断等待**
`<condition>.awaitUninterruptibly();`
```java
// 等待期间不响应中断
notEmpty.awaitUninterruptibly();
```

---

## ReadWriteLock

**基本写法：创建读写锁**
`ReentrantReadWriteLock <变量> = new ReentrantReadWriteLock();`
```java
// 读读共享，读写/写写互斥
ReentrantReadWriteLock rw = new ReentrantReadWriteLock();
```

---

**基本写法：读锁**
`<rw>.readLock().lock();`
```java
// 多个读线程可同时进入
rw.readLock().lock();
try {
    // 读取共享数据
} finally {
    rw.readLock().unlock();
}
```

---

**基本写法：写锁**
`<rw>.writeLock().lock();`
```java
// 写锁独占
rw.writeLock().lock();
try {
    // 修改共享数据
} finally {
    rw.writeLock().unlock();
}
```

---

## StampedLock

**基本写法：创建戳锁**
`StampedLock <变量> = new StampedLock();`
```java
// 高性能读写锁，附带戳（stamp）
StampedLock sl = new StampedLock();
```

---

**基本写法：乐观读**
`<sl>.tryOptimisticRead();`
```java
// 乐观读：不阻塞写线程
long stamp = sl.tryOptimisticRead();
double x = currentX;
if (!sl.validate(stamp)) {
    stamp = sl.readLock();
    try {
        x = currentX;
    } finally {
        sl.unlockRead(stamp);
    }
}
```

---

**基本写法：悲观读**
`<sl>.readLock();`
```java
// 悲观读锁
long stamp = sl.readLock();
try {
    return currentX;
} finally {
    sl.unlockRead(stamp);
}
```

---

**基本写法：写锁**
`<sl>.writeLock();`
```java
// 写锁
long stamp = sl.writeLock();
try {
    currentX = newX;
} finally {
    sl.unlockWrite(stamp);
}
```

---

## 锁状态查询

**基本写法：查询持有与等待**
`<lock>.getHoldCount();`
```java
// 当前线程持有次数
int hold = lock.getHoldCount();
// 等待队列长度
int queued = lock.getQueueLength();
```

---

**基本写法：判断当前线程是否持有**
`<lock>.isHeldByCurrentThread();`
```java
// 仅在持有时才能 unlock
if (lock.isHeldByCurrentThread()) {
    lock.unlock();
}
```
