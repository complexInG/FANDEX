---
order: 700
title: C++ tuple 与 pair
module: 'cpp'
category: 计算机科学
difficulty: beginner
description: C++ tuple 与 pair 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## pair 基本用法

**基本写法：构造 pair**
`std::pair<<类型1>, <类型2>> <变量>(<值1>, <值2>);`
```cpp
// 存储两个可能不同类型的值
std::pair<int, std::string> p(1, "hello");
```

---

**基本写法：make_pair**
`std::make_pair(<值1>, <值2>)`
```cpp
// 自动推导元素类型
auto p = std::make_pair(42, 3.14);
```

---

**基本写法：访问成员**
`<pair>.first` / `<pair>.second`
```cpp
// 直接访问两个元素
std::cout << p.first << " " << p.second;
```

---

**基本写法：结构化绑定解包**
`auto [a, b] = <pair>;`
```cpp
// C++17 一次性解包两个成员
auto [id, name] = p;
```

---

**基本写法：pair 比较**
`<lhs> < <rhs>`
```cpp
// 字典序比较，先比 first 再比 second
bool before = (std::make_pair(1, 2) < std::make_pair(1, 3));
```

---

## tuple 基本用法

**基本写法：构造 tuple**
`std::tuple<<类型>...> <变量>(<值>...);`
```cpp
// 任意数量、任意类型的元素组合
std::tuple<int, double, std::string> t(1, 2.0, "x");
```

---

**基本写法：make_tuple**
`std::make_tuple(<值>...)`
```cpp
// 自动推导各元素类型
auto t = std::make_tuple(1, 2.0, "x");
```

---

**基本写法：按索引取值**
`std::get<<索引>>(<tuple>)`
```cpp
// 编译期固定索引取出元素
std::cout << std::get<0>(t); // 1
std::cout << std::get<std::string>(t); // 也可按类型取，需唯一
```

---

**基本写法：结构化绑定解包**
`auto [a, b, c] = <tuple>;`
```cpp
// C++17 一次性解包全部元素
auto [i, d, s] = t;
```

---

**基本写法：元素个数**
`std::tuple_size<<tuple类型>>::value`
```cpp
// 编译期获取元素数量
constexpr auto n = std::tuple_size<decltype(t)>::value;
```

---

**基本写法：元素类型**
`std::tuple_element<<索引>, <tuple类型>>::type`
```cpp
// 编译期获取指定位置元素类型
using T = std::tuple_element<0, decltype(t)>::type; // int
```

---

## tuple 操作

**基本写法：tie 绑定变量**
`std::tie(<引用1>, <引用2>...)`
```cpp
// 将变量以引用方式打包，常用于接收多返回值
int a, b;
std::tie(a, b) = std::make_pair(1, 2);
```

---

**基本写法：tie 忽略某位**
`std::tie(<变量>, std::ignore)`
```cpp
// 用 std::ignore 跳过不需要的位置
int id;
std::tie(id, std::ignore) = some_pair_func();
```

---

**基本写法：拼接多个 tuple**
`std::tuple_cat(<tuple1>, <tuple2>...)`
```cpp
// 将多个 tuple 连成一个更大的 tuple
auto t1 = std::make_tuple(1);
auto t2 = std::make_tuple(2.0, "x");
auto big = std::tuple_cat(t1, t2); // tuple<int, double, const char*>
```

---

**基本写法：函数调用解包**
`std::apply(<函数>, <tuple>)`
```cpp
// 将 tuple 元素作为参数调用函数
int add(int a, int b) { return a + b; }
auto args = std::make_tuple(3, 4);
int r = std::apply(add, args); // 7
```

---

**基本写法：构造时元素类型转换**
`std::make_from_tuple<<类型>>(<tuple>)`
```cpp
// 用 tuple 元素构造指定类型对象
struct Point { int x, y; };
auto args = std::make_tuple(1, 2);
Point p = std::make_from_tuple<Point>(args);
```

---

## pair/tuple 与容器

**基本写法：map 元素即为 pair**
`std::map<...>::value_type` 为 `std::pair<const Key, T>`
```cpp
// 遍历时元素就是 pair
for (const auto& kv : mymap) {
    std::cout << kv.first << ":" << kv.second;
}
```

---

**基本写法：返回多值**
`return std::make_tuple(<值>...);`
```cpp
// 用 tuple 一次返回多个值，配合 tie 或结构化绑定接收
std::tuple<bool, int> divmod(int a, int b) {
    return {b != 0, b ? a / b : 0};
}
```

---

## C++23/26 增强

**基本写法：tuple-like 协议**
`std::tuple_size` / `std::tuple_element` 适配更多类型
```cpp
// C++23 起 array/pair 等均满足 tuple-like 概念
// 可直接用于结构化绑定与 apply
```

---

**基本写法：pair-like 访问**
`std::get<<索引>>(<pair>)`
```cpp
// C++23 起对 pair 也可用 get<0>/<1> 访问，与 tuple 接口一致
std::cout << std::get<0>(p);
```

---

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
