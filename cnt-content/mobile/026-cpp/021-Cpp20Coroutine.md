# C++20 协程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 协程关键字

**基本写法：暂停等待异步操作**
`co_await <表达式>;`
```cpp
// 暂停协程直到异步操作完成
co_await std::suspend_always{};
```

---

**基本写法：产出值并暂停**
`co_yield <表达式>;`
```cpp
// 产出当前值后暂停执行
co_yield 42;
```

---

**基本写法：结束协程并返回值**
`co_return <表达式>;`
```cpp
// 结束协程并返回最终值
co_return 100;
```

---

## Promise 类型

**基本写法：定义 promise_type**
`struct promise_type { <方法> };`
```cpp
// 协程控制中枢必须实现的接口
struct promise_type {
    Task get_return_object();
    std::suspend_never initial_suspend() noexcept;
    std::suspend_never final_suspend() noexcept;
    void return_void();
    void unhandled_exception();
};
```

---

**基本写法：初始与最终挂起策略**
`<返回类型> initial_suspend();`
```cpp
// 协程开始时立即挂起
std::suspend_always initial_suspend() noexcept { return {}; }
```

---

**基本写法：处理返回值**
`void return_value(<类型> <值>);`
```cpp
// 接收 co_return 的值
void return_value(int v) { result = v; }
```

---

**基本写法：处理 yield 值**
`std::suspend_always yield_value(<类型> <值>);`
```cpp
// 接收 co_yield 产出的值
std::suspend_always yield_value(int v) {
    current = v;
    return {};
}
```

---

**基本写法：异常处理**
`void unhandled_exception();`
```cpp
// 捕获协程内部未处理异常
void unhandled_exception() { std::terminate(); }
```

---

## 协程句柄

**基本写法：从 promise 获取句柄**
`std::coroutine_handle<<promise类型>>::from_promise(<promise>);`
```cpp
// 通过 promise 对象构造协程句柄
auto h = std::coroutine_handle<promise_type>::from_promise(p);
```

---

**基本写法：恢复执行**
`<handle>.resume();`
```cpp
// 恢复挂起的协程
h.resume();
```

---

**基本写法：判断是否完成**
`<handle>.done();`
```cpp
// 检查协程是否已执行完毕
bool finished = h.done();
```

---

**基本写法：销毁协程帧**
`<handle>.destroy();`
```cpp
// 手动销毁协程状态释放资源
h.destroy();
```

---

## Awaitable 接口

**基本写法：自定义 awaitable**
`struct <名称> { bool await_ready(); void await_suspend(<handle>); <类型> await_resume(); };`
```cpp
// 实现三个方法构成可等待对象
struct MyAwaiter {
    bool await_ready() { return false; }
    void await_suspend(std::coroutine_handle<> h) { h.resume(); }
    int await_resume() { return 42; }
};
```

---

## 内置挂起器

**基本写法：总是挂起**
`std::suspend_always{}`
```cpp
// 总是暂停协程的 awaitable
co_await std::suspend_always{};
```

---

**基本写法：从不挂起**
`std::suspend_never{}`
```cpp
// 从不暂停协程的 awaitable
co_await std::suspend_never{};
```

---

## 生成器示例

**基本写法：协程生成器返回类型**
`struct <名称> { struct promise_type { ... }; };`
```cpp
// 简易生成器框架
struct Generator {
    struct promise_type {
        int current;
        Generator get_return_object() {
            return Generator{std::coroutine_handle<promise_type>::from_promise(*this)};
        }
        std::suspend_always initial_suspend() { return {}; }
        std::suspend_always final_suspend() noexcept { return {}; }
        std::suspend_always yield_value(int v) { current = v; return {}; }
        void return_void() {}
        void unhandled_exception() { std::terminate(); }
    };
    std::coroutine_handle<promise_type> h;
};
```

---

**基本写法：使用生成器产出序列**
`Generator <函数名>() { while (...) co_yield <值>; }`
```cpp
// 产出自然数序列的协程
Generator counter() {
    int i = 0;
    while (true) {
        co_yield i++;
    }
}
```
