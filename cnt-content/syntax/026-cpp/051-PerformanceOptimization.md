# C++ 性能优化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 编译优化

**基本写法：优化级别**
`g++ -O<级别> <源文件>`
```bash
# 优化级别选择
g++ -O0 main.cpp    # 调试用
g++ -O2 main.cpp    # 发布推荐
g++ -O3 main.cpp    # 激进优化
g++ -Ofast main.cpp # O3 + 快速数学
g++ -Os main.cpp    # 优化体积
```

---

**基本写法：链接时优化 LTO**
`g++ -flto <源文件>`
```bash
# 跨文件优化
g++ -O2 -flto main.cpp utils.cpp -o app
# CMake 中
set(CMAKE_INTERPROCEDURAL_OPTIMIZATION TRUE)
```

---

**基本写法：目标架构优化**
`g++ -march=<架构>`
```bash
# 针对特定 CPU 架构
g++ -march=native main.cpp   # 当前 CPU
g++ -march=x86-64-v3 main.cpp # AVX2 等
```

---

## 内存优化

**基本写法：避免伪共享**
`alignas(<缓存行>) <变量>`
```cpp
// 缓存行对齐
struct alignas(64) Counter {
    std::atomic<int> value{0};
    // 防止多线程伪共享
};
```

---

**基本写法：内存池**
`<类型>* pool = new <类型>[<数量>];`
```cpp
// 批量分配减少碎片
struct Pool {
    std::vector<std::unique_ptr<Object>> storage;
    Object* acquire() {
        storage.push_back(std::make_unique<Object>());
        return storage.back().get();
    }
};
```

---

**基本写法：小对象优化**
`struct <字符串> { char buf[<n>]; };`
```cpp
// SSO 短字符串优化（std::string 已内置）
// 自定义小对象存储
struct ShortStr {
    static constexpr size_t SSO = 15;
    union { char buf[SSO+1]; char* ptr; };
    // 短串内联，长串堆分配
};
```

---

## 算法优化

**基本写法：reserve 预分配**
`<容器>.reserve(<容量>)`
```cpp
// 预分配避免多次扩容
std::vector<int> v;
v.reserve(1000);     // 预留容量
for (int i = 0; i < 1000; ++i) v.push_back(i);
```

---

**基本写法：emplace 原位构造**
`<容器>.emplace_back(<参数>...)`
```cpp
// 原位构造避免临时对象
std::vector<std::string> v;
v.emplace_back(10, 'x');    // 直接构造，无临时对象
// v.push_back(std::string(10, 'x')); // 先构造临时再移动
```

---

**基本写法：连续内存容器**
`std::vector` 优于 `std::list`
```cpp
// 缓存友好性：连续内存更快
std::vector<int> v(1000);    // 缓存友好
// std::list<int> l(1000);   // 节点分散，慢
// 遍历性能：vector >> list
```

---

## 移动语义

**基本写法：std::move 转移所有权**
`<目标> = std::move(<源>)`
```cpp
// 避免深拷贝
std::vector<int> big(1000000, 42);
std::vector<int> dst = std::move(big); // 移动，O(1)
// big 现在为空
```

---

**基本写法：返回值优化 RVO**
`return <临时对象>;`
```cpp
// 编译器自动消除拷贝
std::vector<int> makeVec() {
    return std::vector<int>(1000, 1); // RVO/NRVO
}
auto v = makeVec(); // 无拷贝
```

---

## 并发优化

**基本写法：无锁数据结构**
`std::atomic<<类型>>`
```cpp
// 原子操作避免锁
std::atomic<int> counter{0};
counter.fetch_add(1, std::memory_order_relaxed); // 无锁自增
```

---

**基本写法：避免锁竞争**
`thread_local <变量>`
```cpp
// 线程局部变量避免锁
thread_local std::vector<int> localBuf;
// 每线程独立缓冲，最后合并
localBuf.push_back(x);
```

---

## 内联与热点

**基本写法：内联函数**
`inline <返回> <函数>(<参数>)`
```cpp
// 建议内联（编译器决定）
inline int square(int x) { return x * x; }
// 强制内联（部分编译器）
__attribute__((always_inline)) inline int cube(int x) { return x*x*x; }
```

---

**基本写法：likely/unlikely 提示**
`[[likely]]` `[[unlikely]]`
```cpp
// C++20 分支预测提示
if (cache_hit) [[likely]] {
    return cache_value;
} else [[unlikely]] {
    return compute();
}
```

---

## 测量与分析

**基本写法：chrono 计时**
`std::chrono::high_resolution_clock`
```cpp
#include <chrono>
auto t1 = std::chrono::high_resolution_clock::now();
// 待测代码
work();
auto t2 = std::chrono::high_resolution_clock::now();
auto us = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();
```

---

**基本写法：perf 分析**
`perf record ./app`
```bash
# 采样分析
perf record -g ./app        # 带调用栈
perf report                 # 查看报告
perf top                    # 实时热点
perf stat ./app             # 统计信息
```
