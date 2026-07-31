# C++ 异常与性能

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 异常开销

**基本写法：禁用异常**
`g++ -fno-exceptions <源文件>`
```bash
# 禁用异常以减小体积（嵌入式/游戏）
g++ -fno-exceptions main.cpp
# 影响：throw/catch 不可用，需用错误码
```

---

**基本写法：noexcept 优化**
`<函数> noexcept`
```cpp
// noexcept 标记不抛异常，编译器可优化
void swapValues(int& a, int& b) noexcept {
    int t = a; a = b; b = t;
}
// 条件 noexcept
template <typename T>
void mySwap(T& a, T& b) noexcept(noexcept(a.swap(b))) {
    a.swap(b);
}
```

---

## 异常性能特征

**基本写法：异常的开销**
`正常路径零开销，异常路径昂贵`
```cpp
// 现代编译器：零成本异常模型
// 正常执行路径几乎无开销（表驱动）
// 抛异常时：栈展开 + 查表，比错误码慢 10-100 倍
// 热点路径避免抛异常，用 expected/error_code
```

---

## 错误码与异常对比

**基本写法：错误码返回**
`std::pair<<值>, <错误>> <函数>()`
```cpp
// 轻量错误处理
std::pair<int, ErrorCode> parseInt(std::string_view s) {
    try { return {std::stoi(std::string(s)), ErrorCode::Ok}; }
    catch (...) { return {0, ErrorCode::ParseError}; }
}
```

---

**基本写法：std::expected（C++23）**
`std::expected<<值>, <错误>>`
```cpp
// C++23 推荐的错误处理
#include <expected>
std::expected<int, std::string> parse(std::string s) {
    if (s.empty()) return std::unexpected("empty");
    return std::stoi(s);
}
auto r = parse("42");
if (r) use(*r);
else handleError(r.error());
```

---

## 异常安全级别

**基本写法：基本异常安全**
`不泄漏资源，对象保持有效状态`
```cpp
// 基本保证：异常时资源不泄漏
void work() {
    auto p = std::make_unique<Resource>();
    riskyOp(); // 抛异常时 p 自动释放
    // 对象可能处于未指定但有效的状态
}
```

---

**基本写法：强异常安全**
`操作成功或回滚`
```cpp
// 强保证：copy-and-swap 惯用法
class Vector {
    int* data; size_t n;
public:
    void push_back(int x) {
        Vector copy = *this;     // 拷贝
        copy.grow(x);            // 修改副本
        swap(copy);              // 不抛交换
    }                            // 失败时原对象不变
};
```

---

**基本写法：nothrow 保证**
`<函数> noexcept`
```cpp
// 不抛保证：绝不抛异常
~Destructor() noexcept {
    // 析构函数默认 noexcept
    // 释放资源，不抛异常
}
```

---

## 性能测量

**基本写法：异常 vs 错误码基准**
`benchmark 对比`
```cpp
// 用 Google Benchmark 对比
#include <benchmark/benchmark.h>
static void BM_Exception(benchmark::State& s) {
    for (auto _ : s) {
        try { throw std::runtime_error("e"); }
        catch (...) {}
    }
}
BENCHMARK(BM_Exception);
static void BM_ErrorCode(benchmark::State& s) {
    for (auto _ : s) {
        auto e = errorCodePath();
        benchmark::DoNotOptimize(e);
    }
}
BENCHMARK(BM_ErrorCode);
```

---

## 异常使用建议

**基本写法：异常用于错误，非控制流**
`抛异常表示异常情况`
```cpp
// 推荐：异常用于真正的错误
File openFile(const std::string& path) {
    FILE* fp = fopen(path.c_str(), "r");
    if (!fp) throw std::runtime_error("cannot open");
    return File(fp);
}
// 不推荐：用异常做正常流程控制
// for (int i = 0; ; ++i) {
//     if (i >= n) throw EndException();
// }
```

---

**基本写法：catch 常引用**
`catch (const <异常类型>& e)`
```cpp
// 避免拷贝
try {
    risky();
} catch (const std::exception& e) { // const 引用
    std::cerr << e.what();
} catch (...) {
    // 兜底
    std::terminate(); // 或重新抛出
}
```

---

## 构造与析构

**基本写法：析构不抛异常**
`~<类>() noexcept`
```cpp
// 析构函数绝不抛异常（默认 noexcept）
struct Resource {
    ~Resource() noexcept {
        try { cleanup(); }
        catch (...) { /* 吞掉异常 */ }
    }
};
```

---

**基本写法：构造抛异常**
`构造函数抛异常，成员按声明逆序析构`
```cpp
// 构造中抛异常，已构造的成员会析构
struct Widget {
    Resource a;
    Resource b;
    Widget() : a() {
        throw std::runtime_error("init failed");
        // a 已构造，会析构
        // b 未构造，不析构
    }
};
```
