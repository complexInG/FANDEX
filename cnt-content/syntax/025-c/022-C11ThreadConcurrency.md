# C11 线程并发

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 线程创建

**基本写法：创建线程**
`thrd_create(&<线程>, <函数>, <参数>);`
```c
// 启动新线程执行函数
thrd_t t;
thrd_create(&t, worker, arg);
```

---

**基本写法：线程函数签名**
`int <函数名>(void* <参数>);`
```c
// 线程入口函数返回 int
int worker(void* arg) {
    return 0;
}
```

---

**基本写法：等待线程结束**
`thrd_join(<线程>, [&<结果>]);`
```c
// 阻塞等待线程完成
int result;
thrd_join(t, &result);
```

---

**基本写法：分离线程**
`thrd_detach(<线程>);`
```c
// 线程独立运行
thrd_detach(t);
```

---

**基本写法：当前线程让出**
`thrd_yield();`
```c
// 主动让出 CPU
thrd_yield();
```

---

**基本写法：线程休眠**
`thrd_sleep(&<时长>, NULL);`
```c
// 休眠指定时长
struct timespec ts = {2, 0};
thrd_sleep(&ts, NULL);
```

---

**基本写法：获取当前线程**
`thrd_current();`
```c
// 获取当前线程标识
thrd_t self = thrd_current();
```

---

## 互斥锁

**基本写法：创建互斥锁**
`mtx_t <变量>; mtx_init(&<变量>, mtx_plain);`
```c
// 初始化普通互斥锁
mtx_t m;
mtx_init(&m, mtx_plain);
```

---

**基本写法：加锁解锁**
`mtx_lock(&<锁>);` `mtx_unlock(&<锁>);`
```c
// 临界区保护
mtx_lock(&m);
// 临界区
mtx_unlock(&m);
```

---

**基本写法：尝试加锁**
`mtx_trylock(&<锁>);`
```c
// 非阻塞加锁
if (mtx_trylock(&m) == thrd_success) { }
```

---

**基本写法：定时加锁**
`mtx_timedlock(&<锁>, &<超时>);`
```c
// 限时等待加锁
struct timespec ts;
mtx_timedlock(&m, &ts);
```

---

**基本写法：销毁互斥锁**
`mtx_destroy(&<锁>);`
```c
// 释放互斥锁资源
mtx_destroy(&m);
```

---

**基本写法：递归互斥锁**
`mtx_init(&<锁>, mtx_recursive);`
```c
// 同一线程可多次加锁
mtx_init(&m, mtx_recursive);
```

---

## 条件变量

**基本写法：创建条件变量**
`cnd_t <变量>; cnd_init(&<变量>);`
```c
// 初始化条件变量
cnd_t cv;
cnd_init(&cv);
```

---

**基本写法：等待条件**
`cnd_wait(&<cv>, &<锁>);`
```c
// 释放锁并等待唤醒
mtx_lock(&m);
while (!ready) cnd_wait(&cv, &m);
mtx_unlock(&m);
```

---

**基本写法：通知一个**
`cnd_signal(&<cv>);`
```c
// 唤醒一个等待线程
cnd_signal(&cv);
```

---

**基本写法：通知所有**
`cnd_broadcast(&<cv>);`
```c
// 唤醒所有等待线程
cnd_broadcast(&cv);
```

---

**基本写法：销毁条件变量**
`cnd_destroy(&<cv>);`
```c
// 释放条件变量资源
cnd_destroy(&cv);
```

---

## 线程局部存储

**基本写法：线程局部变量**
`_Thread_local <类型> <变量>;`
```c
// 每个线程独立副本
_Thread_local int tid = 0;
```

---

**基本写法：使用 TSS**
`tss_t <键>; tss_create(&<键>, NULL); tss_set(<键>, <指针>);`
```c
// 线程特定存储
tss_t key;
tss_create(&key, NULL);
tss_set(key, ptr);
void* p = tss_get(key);
```

---

## 一次性初始化

**基本写法：call_once**
`once_flag <标志> = ONCE_FLAG_INIT; call_once(&<标志>, <函数>);`
```c
// 保证函数只执行一次
once_flag flag = ONCE_FLAG_INIT;
call_once(&flag, init_func);
```

---

## 信号量 C23

**基本写法：创建信号量**
`#include <semaphore.h>` `sem_t <变量>; sem_init(&<变量>, 0, <初始>);`
```c
// 计数信号量
sem_t sem;
sem_init(&sem, 0, 3);
```

---

**基本写法：等待与释放**
`sem_wait(&<sem>);` `sem_post(&<sem>);`
```c
// P 操作与 V 操作
sem_wait(&sem);
// 临界区
sem_post(&sem);
```
