---
order: 680
title: C++ 结构化绑定语法速查手册
module: 'cpp'
category: 计算机科学
difficulty: beginner
description: C++ 结构化绑定语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## 基础语法

**基本写法：绑定数组**
`auto [<标识1>, <标识2>, ...] = <数组对象>;`
```cpp
// 按位置绑定数组元素
int arr[3] = {1, 2, 3};
auto [a, b, c] = arr;  // a=1, b=2, c=3
```

---

**基本写法：绑定 pair / tuple**
`auto [<标识1>, <标识2>, ...] = <tuple 类对象>;`
```cpp
// 解包 pair 与 tuple
std::pair<int, std::string> p{42, "Tom"};
auto [id, name] = p;  // id=42, name="Tom"

std::tuple t{1, 2.5, "hi"};
auto [x, y, z] = t;
```

---

**基本写法：绑定结构体公有成员**
`auto [<标识1>, <标识2>, ...] = <结构体对象>;`
```cpp
// 按声明顺序绑定公有非静态成员
struct Point { int x; int y; };
Point pt{10, 20};
auto [px, py] = pt;  // px=10, py=20
```

---

## 值类别修饰

**基本写法：值拷贝绑定**
`auto [<...>] = <对象>;`
```cpp
// 拷贝一份，原对象不受影响
auto [a, b] = make_pair(1, 2);
```

---

**基本写法：引用绑定**
`auto& [<...>] = <对象>;`
```cpp
// 绑定为左值引用，可修改原对象
std::pair<int, int> p{1, 2};
auto& [a, b] = p;
a = 100;  // p.first 变为 100
```

---

**基本写法：常量引用绑定**
`const auto& [<...>] = <对象>;`
```cpp
// 只读引用，避免拷贝
const auto& [a, b] = some_big_pair;
```

---

**基本写法：右值引用绑定**
`auto&& [<...>] = <对象>;`
```cpp
// 转发引用，保留值类别
auto&& [a, b] = std::make_pair(1, 2);
```

---

## 范围 for 与解构

**基本写法：遍历 map**
`for (const auto& [<键>, <值>] : <map>) { ... }`
```cpp
// 直接解构 map 元素
std::map<std::string, int> m{{"a", 1}, {"b", 2}};
for (const auto& [key, val] : m) {
    std::cout << key << "=" << val << "\n";
}
```

---

**基本写法：遍历 vector of pair**
`for (auto& [<a>, <b>] : <容器>) { ... }`
```cpp
// 解构容器中的 pair 元素
std::vector<std::pair<int, int>> v{{1, 2}, {3, 4}};
for (auto& [first, second] : v) {
    second += 10;
}
```

---

## 函数返回值解构

**基本写法：解构函数返回的 tuple**
`auto [<...>] = <函数调用>();`
```cpp
// 一次返回多值并解构
auto divide(int a, int b) {
    return std::tuple{a / b, a % b};
}
auto [quot, rem] = divide(17, 5);  // quot=3, rem=2
```

---

## C++20 扩展

**基本写法：位域绑定（C++20）**
`auto [<标识>] = <含位域的结构体>;`
```cpp
// C++20 支持位字段绑定（取值为副本）
struct Flags { unsigned a : 3; unsigned b : 5; };
Flags f{1, 2};
auto [x, y] = f;  // x=1, y=2（位域绑定为副本）
```

---

**基本写法：结构化绑定作 lambda 捕获（C++20）**
`[<...>]<lambda>`
```cpp
// C++20 允许结构化绑定变量被 lambda 捕获
std::pair p{1, 2};
auto [a, b] = p;
auto f = [=] { return a + b; };
```

---

## 限定符组合

**基本写法：带 cv 限定与推导**
`<cv> auto [<...>] = <对象>;`
```cpp
// 限定符写在 auto 前
const auto [a, b] = std::make_pair(1, 2);  // a, b 为 const
```

---

**基本写法：decltype(auto) 绑定**
`decltype(auto) [<...>] = <对象>;`
```cpp
// 保留表达式精确值类别
decltype(auto) [a, b] = p;
```

---

## 注意事项速查

**基本写法：标识符数量必须匹配**
`auto [<n 个标识>] = <含 n 个成员的对象>;`
```cpp
// 数量不匹配会编译错误
std::tuple t{1, 2, 3};
auto [a, b] = t;      // 错误：数量不符
auto [a, b, c] = t;   // 正确
```

## 延伸阅读
C++ 模板深入，见 026-cpp/062-CppTemplate 文档。
STL 容器与算法，见 026-cpp 模块 STL 文档。
并发与原子，见 026-cpp 模块并发文档。
Rust 内存安全对比，见 053-rust 模块（若已加入）。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 RAII 与所有权设计

所有权是资源生命周期的归属：栈对象归作用域，unique_ptr 归唯一持有者，shared_ptr 共享所有权，weak_ptr 观察不持有。
传参选择：只读用 const&，需要拷贝用值，转移所有权用 unique_ptr 值传递或 move。
返回选择：返回值（RVO/移动）优先；需要多态返回 unique_ptr<Base>。
容器元素生命周期：容器持有元素值或智能指针；避免裸指针悬垂。

### 13.2 constexpr 与编译期编程

constexpr 变量与函数在编译期求值，消除运行时开销；consteval（C++20）强制编译期求值。
编译期字符串处理、配置表、哈希可在 constexpr 中实现，配合 static_assert 验证。
模板元编程（如 std::tuple 操作）与 constexpr 互补：前者变换类型，后者计算值。
工程建议：优先 constexpr 函数而非模板递归；编译期逻辑保持可测试（运行时同样可调用）。
