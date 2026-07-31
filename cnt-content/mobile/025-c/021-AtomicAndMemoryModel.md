# C 原子操作与内存模型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 原子类型

**基本写法：声明原子变量**
`_Atomic(<类型>) <变量>;`
```c
// 声明原子整型
_Atomic(int) counter = 0;
```

---

**基本写法：原子类型简写**
`_Atomic <类型> <变量>;`
```c
// 简写形式
_Atomic int counter = 0;
```

---

**基本写法：原子标志**
`atomic_flag <变量> = ATOMIC_FLAG_INIT;`
```c
// 最轻量的原子类型
atomic_flag lock = ATOMIC_FLAG_INIT;
```

---

## 原子操作

**基本写法：原子加载**
`atomic_load(&<变量>);`
```c
// 原子读取值
int v = atomic_load(&counter);
```

---

**基本写法：原子存储**
`atomic_store(&<变量>, <值>);`
```c
// 原子写入值
atomic_store(&counter, 10);
```

---

**基本写法：原子交换**
`atomic_exchange(&<变量>, <值>);`
```c
// 替换并返回旧值
int old = atomic_exchange(&counter, 5);
```

---

**基本写法：原子比较交换**
`atomic_compare_exchange_strong(&<变量>, &<期望>, <新值>);`
```c
// CAS 操作成功返回 true
int expected = 0;
bool ok = atomic_compare_exchange_strong(&counter, &expected, 1);
```

---

**基本写法：弱版本 CAS**
`atomic_compare_exchange_weak(&<变量>, &<期望>, <新值>);`
```c
// 可能伪失败适合循环中
while (!atomic_compare_exchange_weak(&counter, &expected, expected + 1));
```

---

**基本写法：原子加法**
`atomic_fetch_add(&<变量>, <值>);`
```c
// 原子加并返回旧值
int prev = atomic_fetch_add(&counter, 1);
```

---

**基本写法：原子减法**
`atomic_fetch_sub(&<变量>, <值>);`
```c
// 原子减并返回旧值
int prev = atomic_fetch_sub(&counter, 1);
```

---

**基本写法：原子按位与**
`atomic_fetch_and(&<变量>, <值>);`
```c
// 原子按位与
int prev = atomic_fetch_and(&flags, 0xFF);
```

---

**基本写法：原子按位或**
`atomic_fetch_or(&<变量>, <值>);`
```c
// 原子按位或
int prev = atomic_fetch_or(&flags, 0x10);
```

---

## 自旋锁示例

**基本写法：自旋锁加锁**
`while (atomic_flag_test_and_set(&<锁>)) {}`
```c
// 使用 atomic_flag 实现自旋锁
while (atomic_flag_test_and_set(&lock)) {
    // 等待
}
```

---

**基本写法：自旋锁解锁**
`atomic_flag_clear(&<锁>);`
```c
// 释放自旋锁
atomic_flag_clear(&lock);
```

---

## 内存顺序

**基本写法：顺序一致**
`memory_order_seq_cst`
```c
// 最严格的全局顺序
atomic_store(&v, 1, memory_order_seq_cst);
```

---

**基本写法：获取语义**
`memory_order_acquire`
```c
// 加载时防止后续读重排
int v = atomic_load(&flag, memory_order_acquire);
```

---

**基本写法：释放语义**
`memory_order_release`
```c
// 存储时防止前面写重排
atomic_store(&flag, 1, memory_order_release);
```

---

**基本写法：宽松语义**
`memory_order_relaxed`
```c
// 仅原子无顺序约束
atomic_fetch_add(&counter, 1, memory_order_relaxed);
```

---

**基本写法：带内存顺序的 CAS**
`atomic_compare_exchange_strong_explicit(&<变量>, &<期望>, <新值>, <成功序>, <失败序>);`
```c
// 显式指定内存顺序
atomic_compare_exchange_strong_explicit(
    &v, &expected, newval,
    memory_order_acq_rel, memory_order_acquire);
```

---

## 栅栏

**基本写法：线程栅栏**
`atomic_thread_fence(<内存序>);`
```c
// 显式内存屏障
atomic_thread_fence(memory_order_release);
```

---

**基本写法：信号栅栏**
`atomic_signal_fence(<内存序>);`
```c
// 信号处理函数内屏障
atomic_signal_fence(memory_order_acquire);
```

---

## 同步关系

**基本写法：发布订阅模式**
`store(release)` ↔ `load(acquire)`
```c
// 线程间建立先行关系
// 线程 A
data = 42;
atomic_store(&flag, 1, memory_order_release);
// 线程 B
while (!atomic_load(&flag, memory_order_acquire));
// 此处能看到 data == 42
```

---

## 常用查询

**基本写法：是否锁自由**
`atomic_is_lock_free(&<变量>);`
```c
// 查询是否无锁实现
bool free = atomic_is_lock_free(&counter);
```

---

**基本写法：原子大小**
`_Atomic(<类型>)` 大小通常与原类型相同
```c
// 原子类型大小
size_t sz = sizeof(_Atomic(int));
```
