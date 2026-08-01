---
order: 680
title: C++ 结构化绑定语法速查手册
module: 026-cpp
category: '026-cpp'
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

## 参考文献

cppreference C++ 文档：https://zh.cppreference.com/w/cpp
C++ 核心指南：https://isocpp.github.io/CppCoreGuidelines/
C++ 标准草案（WG21）：https://isocpp.org/std/the-standard
CMake 官方文档：https://cmake.org/documentation/
Compiler Explorer：https://godbolt.org/

## 延伸阅读

C++ 模板深入，见 026-cpp/062-CppTemplate 文档。
STL 容器与算法，见 026-cpp 模块 STL 文档。
并发与原子，见 026-cpp 模块并发文档。
Rust 内存安全对比，见 053-rust 模块（若已加入）。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 C++ 课程。

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| C++ 概述与现代标准 | 001-CppOverviewAndModernStandard | 本文的前置基础 |
| C++ 基础语法 | 002-CppBasicSyntax | 本文的前置基础 |
| C++ 类型系统 | 003-CppTypeSystem | 本文的并列主题 |
| C++ 引用 | 004-CppReference | 本文的并列主题 |
| 右值引用与移动语义 | 005-RvalueReferenceMoveSemantics | 本文的并列主题 |
| C++ 指针 | 006-PointersCppreferenceCom | 本文的并列主题 |
| 智能指针详解 | 007-N4089DeletingSafeBoolInFavorOfExplicitBool | 本文的并列主题 |
| Lambda表达式 | 008-LambdaExpression | 本文的并列主题 |
| 模板元编程 | 009-ATourOfC3rdEditionOnlineExcerpts | 本文的并列主题 |
| C++20范围 | 010-Cpp20Range | 本文的并列主题 |
| C++20模块 | 011-Cpp20Module | 本文的并列主题 |
| 设计模式与C++ | 012-DesignPatternCpp | 本文的并列主题 |
| RAII与资源管理 | 013-RAIIResourceManagement | 本文的并列主题 |
| 运算符重载 | 014-OperatorOverloading | 本文的并列主题 |
| C++ 面向对象基础 | 015-COOPBasics | 本文的前置基础 |
| C++ STL 算法详解 | 016-CSTL | 本文的并列主题 |
| 字符串处理 | 017-StringProcessing | 本文的并列主题 |
| 文件IO与文件系统 | 018-FileIOFileSystem | 本文的并列主题 |
| 异常安全 | 019-ExceptionSecurity | 本文的安全延伸 |
| 多线程与并发 | 020-MultithreadingConcurrency | 本文的并列主题 |
| 类型特征与SFINAE | 021-TypeTraitsSFINAE | 本文的并列主题 |
| 变参模板 | 022-VariadicTemplate | 本文的并列主题 |
| constexpr与编译期计算 | 023-ConstexprCompileTime | 本文的并列主题 |
| 命名空间与链接 | 024-NamespaceLinkage | 本文的并列主题 |
| C++网络编程 | 025-CppNetworkProgramming | 本文的并列主题 |
| C++ 面向对象进阶 | 026-COOPAdvanced | 本文的并列主题 |
| C++内存模型 | 027-CppMemoryModel | 本文的并列主题 |
| C++图形编程 | 028-CppGraphicsProgramming | 本文的并列主题 |
| C++工具链 | 029-CppToolchain | 本文的并列主题 |
| C++正则表达式 | 030-CppRegex | 本文的并列主题 |
| C++与Python交互 | 031-CppPythonInteraction | 本文的并列主题 |
| C++测试框架 | 032-CppTestFramework | 本文的并列主题 |
| C++与Rust对比 | 033-CppRustComparison | 本文的并列主题 |
| C++23与C++26新特性 | 034-Cpp23Cpp26NewFeatures | 本文的并列主题 |
| C++性能优化 | 035-CppPerformance | 本文的性能延伸 |
| C++序列化 | 036-CppSerialization | 本文的并列主题 |
| C++游戏开发 | 037-CppGameDev | 本文的并列主题 |
| C++嵌入式开发 | 038-CppEmbedded | 本文的并列主题 |
| C++ 内存管理 | 039-CppMemoryManagement | 本文的并列主题 |
| C++代码规范 | 040-CppCodeStyle | 本文的并列主题 |
| C++与WebAssembly | 041-CppWebAssembly | 本文的并列主题 |
| C++反射与元编程 | 042-CppReflectionMetaprogramming | 本文的并列主题 |
| C++数学库 | 043-CppMathLibrary | 本文的并列主题 |
| 智能指针 | 044-SmartPointer | 本文的并列主题 |
| C++ 日期时间 | 045-CppDateTime | 本文的并列主题 |
| C++格式化输出 | 046-CppFormatOutput | 本文的并列主题 |
| C++26 与最新标准 | 047-Cpp26AndLatestStandard | 本文的并列主题 |
| C++ STL 容器与迭代器 | 048-CSTL | 本文的并列主题 |
| 并发编程 | 049-ConcurrentProgramming | 本文的并列主题 |
| RAII资源管理 | 050-CCoreGuidelinesResourceManagement | 本文的并列主题 |
| C++ STL 算法与函数对象 | 051-CSTLAlgorithmAndFunctionObject | 本文的并列主题 |
| 移动语义详解 | 052-MoveSemanticsDetailed | 本文的并列主题 |
| 完美转发与引用折叠 | 053-PerfectForwardingReferenceCollapse | 本文的并列主题 |
| 虚函数表与多态内存布局 | 054-VTablePolymorphismMemoryLayout | 本文的并列主题 |
| 智能指针循环引用 | 055-SmartPointerCircularReference | 本文的并列主题 |
| Lambda捕获详解 | 056-LambdaCaptureDetailed | 本文的并列主题 |
| 类型萃取与SFINAE | 057-TypeExtractionSFINAE | 本文的并列主题 |
| 可变参数模板与折叠表达式 | 058-VariadicTemplateFoldExpression | 本文的并列主题 |
| C++20协程 | 059-Cpp20Coroutine | 本文的并列主题 |
| C++20概念 | 060-Cpp20Concept | 本文的并列主题 |
| C++23新特性 | 061-Cpp23NewFeatures | 本文的并列主题 |
| C++ 模板 | 062-CppTemplate | 本文的并列主题 |
| 内存序与无锁编程 | 063-MemoryOrderLockFree | 本文的并列主题 |
| C++ 异常处理与性能优化 | 064-CppExceptionAndPerformance | 本文的性能延伸 |
| C++ 调试与性能分析 | 065-CDebugPerformanceAnalysis | 本文的性能延伸 |
| C++ 项目实战 | 066-CppProjectPractice | 本文的综合应用 |
| C++ STL 容器使用速查 | 067-STLContainerUsage | 本文的并列主题 |
| C++ 结构化绑定语法速查手册 | 068-StructuredBinding | 本文自身 |
| C++ STL 迭代器 | 069-CppSTLIterator | 本文的并列主题 |
| C++ tuple 与 pair | 070-CppTuplePair | 本文的并列主题 |
| C++ variant / optional / any | 071-CppVariantOptionalAny | 本文的并列主题 |
| C++ CMake 构建命令 | 072-CMakeBuild | 本文的并列主题 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
