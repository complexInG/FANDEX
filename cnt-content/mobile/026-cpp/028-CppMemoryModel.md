# C++ 内存模型基础

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 内存顺序基础

**基本写法：顺序一致顺序**
`std::memory_order_seq_cst`
```cpp
// 默认最严格的全局一致顺序
a.store(1, std::memory_order_seq_cst);
```

---

**基本写法：获取释放顺序**
`std::memory_order_acquire` / `std::memory_order_release`
```cpp
// 配对使用建立同步关系
data.store(42, std::memory_order_release);
int v = data.load(std::memory_order_acquire);
```

---

**基本写法：宽松顺序**
`std::memory_order_relaxed`
```cpp
// 仅保证原子操作本身无竞争
counter.fetch_add(1, std::memory_order_relaxed);
```

---

**基本写法：消费顺序**
`std::memory_order_consume`
```cpp
// 依赖数据的获取顺序通常建议用 acquire 替代
int v = data.load(std::memory_order_consume);
```

---

## 同步关系

**基本写法：发布订阅模式**
`<写线程>.store(<值>, release); <读线程>.load(acquire);`
```cpp
// 线程间建立先行关系
// 线程 A
data = 42;
flag.store(true, std::memory_order_release);
// 线程 B
while (!flag.load(std::memory_order_acquire));
// 此处能看到 data == 42
```

---

**基本写法：栅栏建立同步**
`std::atomic_thread_fence(<内存序>);`
```cpp
// 显式屏障替代操作内存序
data = 42;
std::atomic_thread_fence(std::memory_order_release);
flag.store(true, std::memory_order_relaxed);
```

---

## happens-before 关系

**基本写法：序列先行**
`<语句1>; <语句2>;`
```cpp
// 同一线程内前者 sequenced-before 后者
int a = 1;
int b = a + 1;
```

---

**基本写法：同步建立先行**
`store(release) ↔ load(acquire)`
```cpp
// release 操作 happens-before 配对的 acquire
ready.store(true, std::memory_order_release);
```

---

## 数据竞争

**基本写法：避免数据竞争**
`std::atomic<<类型>> <变量>;`
```cpp
// 多线程访问共享变量需原子或加锁
std::atomic<int> counter{0};
```

---

**基本写法：mutex 保护共享数据**
`std::lock_guard<<锁类型>> <变量>(<锁>);`
```cpp
// 通过锁保证互斥访问
std::mutex m;
std::lock_guard<std::mutex> lk(m);
data.push_back(x);
```

---

## 可见性与顺序

**基本写法：一次性写入**
`std::call_once(<flag>, <函数>);`
```cpp
// 保证初始化只执行一次
std::once_flag flag;
std::call_once(flag, []{ obj = new Object; });
```

---

**基本写法：局部静态线程安全**
`static <类型> <变量>(<参数>);`
```cpp
// C++11 起局部静态初始化线程安全
static Widget& instance() {
    static Widget w;
    return w;
}
```

---

## volatile 关键字

**基本写法：禁止优化**
`volatile <类型> <变量>;`
```cpp
// 阻止编译器优化读写用于硬件寄存器
volatile int* reg = (volatile int*)0x4000;
```

---

**基本写法：注意 volatile 不保证原子性**
`volatile <类型> <变量>;  // 多线程下不安全`
```cpp
// volatile 仅禁优化不提供原子或顺序保证
volatile int v = 0;  // 多线程读写仍需锁或原子
```

---

## 顺序一致性与性能

**基本写法：选择适当内存序**
`load(acquire)` / `store(release)`
```cpp
// 性能优于 seq_cst 的常用配对
flag.load(std::memory_order_acquire);
flag.store(true, std::memory_order_release);
```

---

**基本写法：统计计数用宽松**
`fetch_add(<值>, relaxed)`
```cpp
// 无顺序要求场景使用最宽松顺序
counter.fetch_add(1, std::memory_order_relaxed);
```

---

## 信号量 C++20

**基本写法：创建信号量**
`std::counting_semaphore<<最大值>> <变量>(<初始值>);`
```cpp
// 计数信号量
std::counting_semaphore<10> sem(3);
```

---

**基本写法：获取与释放**
`<sem>.acquire();` `<sem>.release();`
```cpp
// P 操作与 V 操作
sem.acquire();   // 计数减 1
// 临界区
sem.release();   // 计数加 1
```

---

**基本写法：二元信号量**
`std::binary_semaphore <变量>(<初始值>);`
```cpp
// 等价于只有 0 和 1 的信号量
std::binary_semaphore sem(1);
```
