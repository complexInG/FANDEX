# C++ 多线程并发速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建线程

**基本写法：thread 创建**
`std::thread <变量>(<函数>, [<参数>...]);`
```cpp
// 创建并启动线程
std::thread t([]() { std::cout << "Hello"; });
```

---

**基本写法：带参数线程**
`std::thread <变量>(<函数>, <参数1>, <参数2>);`
```cpp
// 传递参数
std::thread t([](int x) { std::cout << x; }, 42);
```

---

**基本写法：join 等待线程**
`<thread>.join();`
```cpp
// 等待线程完成
t.join();
```

---

**基本写法：detach 分离线程**
`<thread>.detach();`
```cpp
// 分离线程在后台运行
t.detach();
```

---

## 互斥锁

**基本写法：mutex 加锁解锁**
`std::mutex <变量>;`
```cpp
// 手动加锁解锁
std::mutex mtx;
mtx.lock();
// 临界区
mtx.unlock();
```

---

**基本写法：lock_guard 自动锁**
`std::lock_guard<<类型>> <变量>(<mutex>);`
```cpp
// RAII 自动管理锁
std::lock_guard<std::mutex> lock(mtx);
// 临界区
```

---

**基本写法：unique_lock 灵活锁**
`std::unique_lock<<类型>> <变量>(<mutex>);`
```cpp
// 可手动解锁的灵活锁
std::unique_lock<std::mutex> lock(mtx);
lock.unlock();
// 后续操作
lock.lock();
```

---

**基本写法：scoped_lock 多锁同时**
`std::scoped_lock <变量>(<mutex1>, <mutex2>);`
```cpp
// 同时锁住多个 mutex（避免死锁）
std::scoped_lock lock(mtx1, mtx2);
```

---

## 条件变量

**基本写法：等待通知**
`<cv>.wait(<unique_lock>, <谓词>);`
```cpp
// 等待条件成立
std::condition_variable cv;
std::unique_lock<std::mutex> lock(mtx);
cv.wait(lock, [] { return ready; });
```

---

**基本写法：通知一个**
`<cv>.notify_one();`
```cpp
// 通知一个等待线程
cv.notify_one();
```

---

**基本写法：通知所有**
`<cv>.notify_all();`
```cpp
// 通知所有等待线程
cv.notify_all();
```

---

## 异步与 Future

**基本写法：async 异步执行**
`std::async(<策略>, <函数>, [<参数>...]);`
```cpp
// 异步执行任务
auto future = std::async(std::launch::async, []() { return 42; });
int result = future.get();
```

---

**基本写法：promise 承诺**
`std::promise<<类型>> <变量>;`
```cpp
// 设置异步结果
std::promise<int> p;
p.set_value(42);
// 在另一线程获取
int value = p.get_future().get();
```

---

**基本写法：packaged_task 打包任务**
`std::packaged_task<<函数签名>> <变量>(<函数>);`
```cpp
// 打包任务获取 future
std::packaged_task<int()> task([]() { return 42; });
auto future = task.get_future();
std::thread t(std::move(task));
t.join();
```

---

## 原子操作

**基本写法：atomic 原子变量**
`std::atomic<<类型>> <变量>;`
```cpp
// 原子计数器
std::atomic<int> counter{0};
counter++;
counter.fetch_add(1);
```

---

**基本写法：load 读取**
`<atomic>.load();`
```cpp
// 读取原子值
int value = counter.load();
```

---

**基本写法：store 存储**
`<atomic>.store(<值>);`
```cpp
// 存储原子值
counter.store(100);
```

---

**基本写法：compare_exchange 比较交换**
`<atomic>.compare_exchange_strong(<期望值>, <新值>);`
```cpp
// CAS 操作
int expected = 10;
bool changed = counter.compare_exchange_strong(expected, 20);
```

---

## 线程安全容器

**基本写法：call_once 单次调用**
`std::call_once(<flag>, <函数>, [<参数>...]);`
```cpp
// 保证函数只执行一次
std::once_flag flag;
std::call_once(flag, []() { initialize(); });
```

---

## 线程信息

**基本写法：获取线程 ID**
`std::this_thread::get_id();`
```cpp
// 获取当前线程 ID
auto id = std::this_thread::get_id();
```

---

**基本写法：线程休眠**
`std::this_thread::sleep_for(<时长>);`
```cpp
// 休眠 1 秒
std::this_thread::sleep_for(std::chrono::seconds(1));
```

---

**基本写法：让出 CPU**
`std::this_thread::yield();`
```cpp
// 让出当前时间片
std::this_thread::yield();
```
