# C++ 代码风格

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 命名规范

**基本写法：命名约定**
`<作用域> <命名风格>`
```cpp
// 常见命名风格
int localVar;          // 局部变量：小驼峰或下划线
int g_counter;         // 全局变量：g_ 前缀
constexpr int MAX_SIZE = 100; // 常量：全大写下划线
class HttpClient {};   // 类名：大驼峰
struct Point {};       // 结构体：大驼峰
void fetchData();      // 函数：小驼峰或下划线
int m_count;           // 成员变量：m_ 前缀
int m_data;            // 或 _data 前缀
```

---

**基本写法：Google 风格**
`<类型> <命名>`
```cpp
// Google C++ 风格
class MyClass {
public:
    void DoWork();        // 公开方法：大驼峰
private:
    int counter_;         // 成员变量：下划线后缀
};
enum class Color { kRed, kGreen }; // 枚举值 k 前缀
constexpr int kBufferSize = 1024;  // 常量 k 前缀
```

---

**基本写法：STL/标准库风格**
`<小写下划线>`
```cpp
// 标准库风格
class string_view {};
template <typename T> class unique_ptr {};
int some_value = 0;
void make_unique();
```

---

## 头文件

**基本写法：头文件保护**
`#pragma once`
```cpp
// 现代 C++ 推荐用 #pragma once
#pragma once
class Widget {};

// 传统 include guard
#ifndef MY_HEADER_H
#define MY_HEADER_H
class Widget {};
#endif
```

---

**基本写法：include 顺序**
`<标准库> → <第三方> → <项目>`
```cpp
// 推荐顺序
#include <vector>           // 1. C++ 标准库
#include <string>

#include <fmt/format.h>     // 2. 第三方库

#include "myproject/widget.h" // 3. 项目头文件
```

---

## const 与 constexpr

**基本写法：const 修饰**
`const <类型> <变量>` 或 `<类型> const <变量>`
```cpp
// const 正确性
const int max = 100;        // 不可变变量
const int* p1;              // 指向 const 的指针
int* const p2 = &x;         // const 指针
const int& ref = x;         // const 引用
void print() const;         // const 成员函数
```

---

**基本写法：constexpr 编译期**
`constexpr <返回> <函数>()`
```cpp
// 编译期常量与函数
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}
constexpr int x = factorial(5); // 120，编译期计算
```

---

## 现代类型推导

**基本写法：auto 与 decltype**
`auto <变量> = <表达式>;`
```cpp
// 类型推导
auto i = 42;                // int
auto& ref = obj;            // 引用
const auto& cref = obj;     // const 引用
auto ptr = std::make_unique<int>(5); // unique_ptr<int>

decltype(auto) x = expr;    // 保持表达式类型
decltype(obj.member) m;     // 成员类型
```

---

**基本写法：函数返回类型推导**
`auto <函数>() -> <返回类型>`
```cpp
// 尾随返回类型
auto divide(double a, double b) -> double {
    return a / b;
}
// C++14 直接 auto
auto add(int a, int b) { return a + b; }
```

---

## 资源管理

**基本写法：智能指针优先**
`std::unique_ptr` / `std::shared_ptr`
```cpp
// 避免裸 new/delete
std::unique_ptr<Widget> w = std::make_unique<Widget>();
std::shared_ptr<Widget> s = std::make_shared<Widget>();
// 函数参数传引用或指针
void process(const Widget& w);  // 输入参数用 const 引用
void update(Widget& w);          // 输出参数用引用
```

---

**基本写法：RAII 守卫**
`std::lock_guard` `std::unique_lock`
```cpp
// RAII 管理锁
std::mutex m;
{
    std::lock_guard<std::mutex> lk(m);
    // 临界区
} // 自动解锁
```

---

## 异常与错误处理

**基本写法：异常安全**
`try { } catch (const <异常>& e) {}`
```cpp
// 异常处理
try {
    riskyOperation();
} catch (const std::runtime_error& e) {
    std::cerr << e.what();
} catch (...) {
    // 捕获所有异常
}
// noexcept 标记不抛异常
void swap(T& a, T& b) noexcept;
```

---

## 格式化工具

**基本写法：clang-format 配置**
`.clang-format`
```yaml
# clang-format 配置文件示例
BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 100
BreakBeforeBraces: Attach
AllowShortFunctionsOnASingleLine: Empty
```

---

**基本写法：现代格式化输出**
`std::format` / `std::print`
```cpp
// C++20 std::format
#include <format>
std::string s = std::format("x={}, y={}", x, y);

// C++23 std::print
#include <print>
std::println("result = {}", result);
```
