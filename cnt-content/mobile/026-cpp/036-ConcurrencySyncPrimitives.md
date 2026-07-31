# C++ 并发同步原语

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## thread 线程

**基本写法：创建线程**
`std::thread <变量>(<函数>, <参数>...);`
```cpp
// 启动新线程执行函数
std::thread t(worker, 42);
```

---

**基本写法：等待线程结束**
`<t>.join();`
```cpp
// 阻塞直到线程完成
t.join();
```

---

**基本写法：分离线程**
`<t>.detach();`
```cpp
// 线程独立运行不再管理
t.detach();
```

---

**基本写法：获取线程 ID**
`<t>.get_id()` 或 `std::this_thread::get_id()`
```cpp
// 获取线程标识
std::thread::id id = t.get_id();
```

---

**基本写法：硬件并发数**
`std::thread::hardware_concurrency();`
```cpp
// 返回 CPU 支持的并发线程数
unsigned n = std::thread::hardware_concurrency();
```

---

## mutex 互斥锁

**基本写法：创建互斥锁**
`std::mutex <变量>;`
```cpp
// 互斥锁对象
std::mutex m;
```

---

**基本写法：手动加锁解锁**
`<m>.lock();` `<m>.unlock();`
```cpp
// 显式加锁解锁
m.lock();
// 临界区
m.unlock();
```

---

**基本写法：递归锁**
`std::recursive_mutex <变量>;`
```cpp
// 同一线程可多次加锁
std::recursive_mutex rm;
```

---

**基本写法：定时锁**
`std::timed_mutex <变量>;`
```cpp
// 支持超时的互斥锁
std::timed_mutex tm;
```

---

**基本写法：尝试加锁**
`<m>.try_lock();`
```cpp
// 非阻塞加锁
if (m.try_lock()) { /* 成功 */ }
```

---

**基本写法：超时加锁**
`<m>.try_lock_for(<时长>);`
```cpp
// 限时等待加锁
if (tm.try_lock_for(std::chrono::seconds(1))) { }
```

---

## lock_guard / unique_lock

**基本写法：作用域锁**
`std::lock_guard<<锁类型>> <变量>(<锁>);`
```cpp
// RAII 自动加锁解锁
std::lock_guard<std::mutex> lk(m);
```

---

**基本写法：unique_lock 灵活锁**
`std::unique_lock<<锁类型>> <变量>(<锁>);`
```cpp
// 可延迟加锁或手动解锁
std::unique_lock<std::mutex> lk(m);
```

---

**基本写法：多锁同时加锁**
`std::lock(<锁1>, <锁2>);`
```cpp
// 一次性锁住多个互斥避免死锁
std::lock(m1, m2);
```

---

## condition_variable 条件变量

**基本写法：创建条件变量**
`std::condition_variable <变量>;`
```cpp
// 条件变量对象
std::condition_variable cv;
```

---

**基本写法：等待条件**
`<cv>.wait(<unique_lock>, [<谓词>]);`
```cpp
// 释放锁并等待唤醒
std::unique_lock<std::mutex> lk(m);
cv.wait(lk, []{ return ready; });
```

---

**基本写法：通知一个**
`<cv>.notify_one();`
```cpp
// 唤醒一个等待线程
cv.notify_one();
```

---

**基本写法：通知所有**
`<cv>.notify_all();`
```cpp
// 唤醒所有等待线程
cv.notify_all();
```

---

**基本写法：超时等待**
`<cv>.wait_for(<unique_lock>, <时长>, [<谓词>]);`
```cpp
// 限时等待
if (cv.wait_for(lk, std::chrono::seconds(2), []{ return ready; })) { }
```

---

## future / promise / async

**基本写法：异步任务**
`std::async(std::launch::async, <函数>, <参数>...);`
```cpp
// 异步执行并返回 future
auto fut = std::async(std::launch::async, compute, 42);
```

---

**基本写法：获取异步结果**
`<fut>.get();`
```cpp
// 阻塞等待并取回结果
int result = fut.get();
```

---

**基本写法：promise 设置值**
`std::promise<<类型>> <变量>; <变量>.set_value(<值>);`
```cpp
// 通过 promise 传递结果
std::promise<int> p;
p.set_value(100);
auto f = p.get_future();
```

---

**基本写法：打包任务**
`std::packaged_task<<签名>>(<函数>);`
```cpp
// 包装可调用对象为可获取结果的任务
std::packaged_task<int(int)> task(compute);
auto f = task.get_future();
task(42);
```

---

## shared_mutex 读写锁

**基本写法：共享互斥**
`std::shared_mutex <变量>;`
```cpp
// 读写锁支持多读单写
std::shared_mutex rw;
```

---

**基本写法：共享读锁**
`std::shared_lock<<锁类型>> <变量>(<锁>);`
```cpp
// 多线程可同时读
std::shared_lock<std::shared_mutex> rl(rw);
```

---

**基本写法：独占写锁**
`std::unique_lock<<锁类型>> <变量>(<锁>);`
```cpp
// 独占写
std::unique_lock<std::shared_mutex> wl(rw);
```

---

## barrier 屏障 C++20

**基本写法：创建屏障**
`std::barrier<<数量>>(<计数>);`
```cpp
// 多线程同步屏障
std::barrier b(4);
```

---

**基本写法：到达并等待**
`<b>.arrive_and_wait();`
```cpp
// 等待所有线程到达
b.arrive_and_wait();
```

---

## latch 闩锁 C++20

**基本写法：创建闩锁**
`std::latch <变量>(<计数>);`
```cpp
// 一次性倒计数同步
std::latch l(3);
```

---

**基本写法：计数减一**
`<l>.count_down();`
```cpp
// 计数减一
l.count_down();
```

---

**基本写法：等待计数归零**
`<l>.wait();`
```cpp
// 阻塞直到计数为零
l.wait();
```
