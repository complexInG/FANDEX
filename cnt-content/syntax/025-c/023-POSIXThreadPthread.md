# C POSIX 线程 pthread

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 线程创建

**基本写法：创建线程**
`pthread_create(&<线程>, [NULL], <函数>, <参数>);`
```c
// 创建新线程
pthread_t tid;
pthread_create(&tid, NULL, worker, arg);
```

---

**基本写法：线程函数签名**
`void* <函数名>(void* <参数>);`
```c
// 线程入口函数返回 void 指针
void* worker(void* arg) {
    return NULL;
}
```

---

**基本写法：等待线程**
`pthread_join(<线程>, [&<返回值>]);`
```c
// 阻塞等待线程结束
void* ret;
pthread_join(tid, &ret);
```

---

**基本写法：分离线程**
`pthread_detach(<线程>);`
```c
// 分离线程自动回收资源
pthread_detach(tid);
```

---

**基本写法：获取自身 ID**
`pthread_self();`
```c
// 当前线程 ID
pthread_t self = pthread_self();
```

---

**基本写法：比较线程 ID**
`pthread_equal(<t1>, <t2>);`
```c
// 比较两个线程是否相同
if (pthread_equal(t1, t2)) { }
```

---

**基本写法：线程退出**
`pthread_exit([<返回值>]);`
```c
// 退出当前线程
pthread_exit(NULL);
```

---

## 互斥锁

**基本写法：静态初始化**
`pthread_mutex_t <变量> = PTHREAD_MUTEX_INITIALIZER;`
```c
// 静态初始化互斥锁
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
```

---

**基本写法：动态初始化**
`pthread_mutex_init(&<锁>, [NULL]);`
```c
// 运行时初始化
pthread_mutex_init(&m, NULL);
```

---

**基本写法：加锁解锁**
`pthread_mutex_lock(&<锁>);` `pthread_mutex_unlock(&<锁>);`
```c
// 临界区保护
pthread_mutex_lock(&m);
// 临界区
pthread_mutex_unlock(&m);
```

---

**基本写法：尝试加锁**
`pthread_mutex_trylock(&<锁>);`
```c
// 非阻塞加锁
if (pthread_mutex_trylock(&m) == 0) { }
```

---

**基本写法：销毁互斥锁**
`pthread_mutex_destroy(&<锁>);`
```c
// 释放资源
pthread_mutex_destroy(&m);
```

---

## 条件变量

**基本写法：静态初始化条件变量**
`pthread_cond_t <变量> = PTHREAD_COND_INITIALIZER;`
```c
// 静态初始化
pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
```

---

**基本写法：等待条件**
`pthread_cond_wait(&<cv>, &<锁>);`
```c
// 释放锁等待唤醒
pthread_mutex_lock(&m);
while (!ready) pthread_cond_wait(&cv, &m);
pthread_mutex_unlock(&m);
```

---

**基本写法：超时等待**
`pthread_cond_timedwait(&<cv>, &<锁>, &<超时>);`
```c
// 限时等待
struct timespec ts;
pthread_cond_timedwait(&cv, &m, &ts);
```

---

**基本写法：通知一个**
`pthread_cond_signal(&<cv>);`
```c
// 唤醒一个线程
pthread_cond_signal(&cv);
```

---

**基本写法：通知所有**
`pthread_cond_broadcast(&<cv>);`
```c
// 唤醒所有线程
pthread_cond_broadcast(&cv);
```

---

## 读写锁

**基本写法：创建读写锁**
`pthread_rwlock_t <变量> = PTHREAD_RWLOCK_INITIALIZER;`
```c
// 读写锁支持多读单写
pthread_rwlock_t rw = PTHREAD_RWLOCK_INITIALIZER;
```

---

**基本写法：读锁**
`pthread_rwlock_rdlock(&<锁>);`
```c
// 共享读
pthread_rwlock_rdlock(&rw);
```

---

**基本写法：写锁**
`pthread_rwlock_wrlock(&<锁>);`
```c
// 独占写
pthread_rwlock_wrlock(&rw);
```

---

## 信号量

**基本写法：创建信号量**
`sem_t <变量>; sem_init(&<变量>, 0, <初始>);`
```c
// 初始化信号量
sem_t sem;
sem_init(&sem, 0, 1);
```

---

**基本写法：等待与释放**
`sem_wait(&<sem>);` `sem_post(&<sem>);`
```c
// P 与 V 操作
sem_wait(&sem);
// 临界区
sem_post(&sem);
```

---

**基本写法：销毁信号量**
`sem_destroy(&<sem>);`
```c
// 释放信号量资源
sem_destroy(&sem);
```

---

## 线程属性

**基本写法：设置分离状态**
`pthread_attr_setdetachstate(&<属性>, PTHREAD_CREATE_DETACHED);`
```c
// 创建即分离的线程
pthread_attr_t attr;
pthread_attr_init(&attr);
pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
pthread_create(&tid, &attr, worker, NULL);
```

---

**基本写法：编译链接**
`gcc -pthread <文件>.c -o <输出>`
```c
// 链接 pthread 库
gcc -pthread main.c -o main
```
