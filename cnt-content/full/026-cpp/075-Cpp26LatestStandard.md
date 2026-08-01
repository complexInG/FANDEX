---
order: 750
title: C++26 最新标准
module: 026-cpp
category: '026-cpp'
difficulty: beginner
description: C++26 最新标准 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# C++26 最新标准

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## C++26 概览

**基本写法：编译启用 C++26**
`g++ -std=c++26 <源文件>` 或 `g++ -std=c++2c`
```bash
# C++26 仍在制定中（部分特性可能调整）
g++ -std=c++2c -fconcepts main.cpp
clang++ -std=c++2c main.cpp
# 特性宏查看
g++ -std=c++2c -dM -E -x c++ /dev/null | grep cpp_
```

---

## Contracts 契约（进行中）

**基本写法：契约断言**
`[[assert: <条件>]];`
```cpp
// C++26 契约（提案中）
int divide(int a, int b) {
    [[assert: b != 0]];          // 断言前置条件
    return a / b;
}
// 前置/后置条件（语法可能调整）
int compute(int x)
    [[pre: x > 0]]               // 前置条件
    [[post r: r > 0]]            // 后置条件
{
    return x * 2;
}
```

---

## 静态反射（进行中）

**基本写法：反射元信息**
`^^<类型>` `std::meta::info`
```cpp
// C++26 反射提案（语法可能变化）
#include <meta>
struct Point { int x; int y; };

// 获取类型信息
constexpr auto info = ^^Point;
// 遍历成员
template_for (auto member : info.members) {
    std::cout << member.name;
}
// 反射特性仍在演进，具体语法以最终标准为准
```

---

## Senders/Receivers（进行中）

**基本写法：执行模型**
`std::execution`
```cpp
// C++26 异步执行框架（P2300 提案）
#include <execution>
using namespace std::execution;
// 发送器链
auto work = just(42)
    | then([](int x){ return x * 2; })
    | then([](int x){ std::cout << x; });
sync_wait(std::move(work));
```

---

## 已确认特性

**基本写法：= delete 理由**
`= delete("<理由>")`
```cpp
// C++26 标注删除原因
struct NonCopyable {
    NonCopyable(const NonCopyable&) = delete("不可拷贝");
    NonCopyable& operator=(const NonCopyable&) = delete("不可拷贝");
};
```

---

**基本写法：静态索引 operator[]**
`<返回> operator[](size_t, size_t) static`
```cpp
// 静态下标运算符
struct Matrix {
    static constexpr int data[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
    // 静态上下标
    static constexpr int at(size_t i, size_t j) { return data[i][j]; }
};
int v = Matrix::at(1, 2); // 6
```

---

**基本写法：包索引**
`<包>...[<索引>]`
```cpp
// C++26 访问变参包中特定元素
template <typename... Ts>
auto first(Ts... args) {
    return args...[0]; // 访问第一个参数
}
int x = first(1, 2, 3); // 1
```

---

**基本写法：用户自定义占位符**
`_` 作为忽略变量
```cpp
// C++26 标准化下划线占位符
auto [x, _, z] = std::tuple(1, 2, 3);
// _ 不需要使用，避免未使用警告
auto [a, _unused, b] = someTriple();
```

---

## 测试支持增强

**基本写法：constexpr 更多支持**
`constexpr` 可用于更多场景
```cpp
// C++26 扩展 constexpr 能力
constexpr void printAtCompile() {
    // 编译期输出（提案中）
}
// 更多标准库函数变为 constexpr
constexpr double v = std::sin(0.0); // 编译期计算
```

---

## 字符串改进

**基本写法：string read_until**
`<字符串>.read_until(<谓词>)`
```cpp
// C++26 字符串处理增强（提案）
std::string s = "hello world";
// 字符串搜索与分割增强
auto pos = s.find("world");
```

---

## 警告与现状

**基本写法：特性宏检查**
`#ifdef __cpp_<特性>`
```cpp
// 编译期检测 C++26 特性支持
#ifdef __cpp_static_call_operator
    // 静态调用运算符
#endif

#ifdef __cpp_pack_indexing
    // 包索引
    auto x = args...[0];
#endif
// 注意：C++26 特性仍在演进，使用前请查询编译器支持情况
```

---

## 编译器支持

**基本写法：查看支持情况**
`g++ -std=c++2c -dM -E -x c++ /dev/null`
```bash
# GCC / Clang 对 C++26 的部分支持
# GCC 14+ 部分特性
# Clang 18+ 部分特性
# 特性仍在开发，建议关注最新编译器版本
g++ -std=c++2c -dM -E -x c++ /dev/null | sort | grep cpp_
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
| C++ 结构化绑定语法速查手册 | 068-StructuredBinding | 本文的并列主题 |
| C++ STL 迭代器 | 069-CppSTLIterator | 本文的并列主题 |
| C++ tuple 与 pair | 070-CppTuplePair | 本文的并列主题 |
| C++ variant / optional / any | 071-CppVariantOptionalAny | 本文的并列主题 |
| C++ CMake 构建命令 | 072-CMakeBuild | 本文的并列主题 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文自身 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
