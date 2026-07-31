# C++ 内存模型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 原子类型

**基本写法：声明原子变量**
`std::atomic<<类型>> <变量>;`
```cpp
// 原子整型变量
std::atomic<int> counter{0};
```

---

**基本写法：原子加载**
`<变量>.load([<内存序>]);`
```cpp
// 原子读取值
int v = counter.load(std::memory_order_acquire);
```

---

**基本写法：原子存储**
`<变量>.store(<值>, [<内存序>]);`
```cpp
// 原子写入值
counter.store(10, std::memory_order_release);
```

---

**基本写法：原子交换**
`<变量>.exchange(<值>, [<内存序>]);`
```cpp
// 原子替换并返回旧值
int old = counter.exchange(5);
```

---

## CAS 操作

**基本写法：比较并交换**
`<变量>.compare_exchange_strong(<期望>, <新值>, [<内存序>]);`
```cpp
// 强版本 CAS，失败时更新期望值
int expected = 0;
bool ok = counter.compare_exchange_strong(expected, 1);
```

---

**基本写法：弱版本 CAS**
`<变量>.compare_exchange_weak(<期望>, <新值>);`
```cpp
// 可能伪失败，适合循环中
while (!counter.compare_exchange_weak(expected, expected + 1));
```

---

**基本写法：fetch_add 原子加法**
`<变量>.fetch_add(<值>, [<内存序>]);`
```cpp
// 原子加并返回旧值
int prev = counter.fetch_add(1);
```

---

**基本写法：fetch_sub 原子减法**
`<变量>.fetch_sub(<值>, [<内存序>]);`
```cpp
// 原子减并返回旧值
int prev = counter.fetch_sub(1);
```

---

## 内存序

**基本写法：顺序一致性**
`std::memory_order_seq_cst`
```cpp
// 最强保证，全局总序
counter.store(1, std::memory_order_seq_cst);
```

---

**基本写法：获取语义**
`std::memory_order_acquire`
```cpp
// 加载时保证后续读不重排到此之前
v = counter.load(std::memory_order_acquire);
```

---

**基本写法：释放语义**
`std::memory_order_release`
```cpp
// 存储时保证之前写不重排到此之后
counter.store(1, std::memory_order_release);
```

---

**基本写法：宽松语义**
`std::memory_order_relaxed`
```cpp
// 仅保证原子性无顺序约束
counter.fetch_add(1, std::memory_order_relaxed);
```

---

## fence 屏障

**基本写法：释放屏障**
`std::atomic_thread_fence(std::memory_order_release);`
```cpp
// 显式内存屏障防止写重排
std::atomic_thread_fence(std::memory_order_release);
data = 42;
ready.store(true);
```

---

**基本写法：获取屏障**
`std::atomic_thread_fence(std::memory_order_acquire);`
```cpp
// 显式内存屏障防止读重排
std::atomic_thread_fence(std::memory_order_acquire);
int v = data;
```

---

## 自旋锁示例

**基本写法：使用原子实现自旋锁**
`while (<锁>.test_and_set(std::memory_order_acquire)) {}`
```cpp
// 原子标志位自旋等待
std::atomic_flag lock = ATOMIC_FLAG_INIT;
while (lock.test_and_set(std::memory_order_acquire)) {}
// 临界区
lock.clear(std::memory_order_release);
```

---

**基本写法：等待与通知**
`<变量>.wait(<旧值>);` `<变量>.notify_one();`
```cpp
// C++20 原子等待通知
counter.wait(0);          // 阻塞直到值变化
counter.store(1);
counter.notify_one();     // 唤醒一个等待者
```
