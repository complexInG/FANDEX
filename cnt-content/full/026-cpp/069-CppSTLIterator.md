---
order: 690
title: C++ STL 迭代器
module: cpp

category: '026-cpp'
difficulty: beginner
description: C++ STL 迭代器 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 迭代器类别

**基本写法：输入迭代器**
`std::input_iterator<T>`
```cpp
// 只读、单遍递增，如 istream_iterator
std::istream_iterator<int> it(std::cin), end;
while (it != end) { std::cout << *it++; }
```

---

**基本写法：前向迭代器**
`std::forward_iterator<T>`
```cpp
// 只读或多遍递增，如 forward_list 的迭代器
std::forward_list<int> l{1, 2, 3};
for (auto it = l.begin(); it != l.end(); ++it) { *it += 1; }
```

---

**基本写法：双向迭代器**
`std::bidirectional_iterator<T>`
```cpp
// 支持递减，如 list/set/map 的迭代器
std::list<int> l{1, 2, 3};
auto it = l.end(); --it; // 指向 3
```

---

**基本写法：随机访问迭代器**
`std::random_access_iterator<T>`
```cpp
// 支持 + n / - n 与下标，如 vector/deque/array
std::vector<int> v{10, 20, 30};
auto it = v.begin() + 2; // 指向 30
```

---

**基本写法：连续迭代器（C++20）**
`std::contiguous_iterator<T>`
```cpp
// 元素连续存储，最强保证，如 vector/array
int* p = v.data(); // 等价裸指针访问
```

---

## 容器迭代器

**基本写法：begin/end**
`<容器>.begin()` / `<容器>.end()`
```cpp
// 返回首元素与尾后位置迭代器
std::vector<int> v{1, 2, 3};
for (auto it = v.begin(); it != v.end(); ++it) { std::cout << *it; }
```

---

**基本写法：只读迭代器**
`<容器>.cbegin()` / `<容器>.cend()`
```cpp
// const 版本，元素不可修改
for (auto it = v.cbegin(); it != v.cend(); ++it) { /* *it = 0; 错误 */ }
```

---

**基本写法：反向迭代器**
`<容器>.rbegin()` / `<容器>.rend()`
```cpp
// 反向遍历，rbegin 指向末元素
for (auto it = v.rbegin(); it != v.rend(); ++it) { std::cout << *it; }
```

---

**基本写法：自由函数版本**
`std::begin(<容器>)` / `std::end(<容器>)`
```cpp
// 适配原生数组与容器
int arr[] = {1, 2, 3};
auto total = std::accumulate(std::begin(arr), std::end(arr), 0);
```

---

## 迭代器辅助函数

**基本写法：距离**
`std::distance(<首>, <尾>)`
```cpp
// 计算两个迭代器间距离
auto n = std::distance(v.begin(), v.end()); // 元素个数
```

---

**基本写法：前进**
`std::advance(<迭代器>, <步数>)`
```cpp
// 原地移动迭代器，负数需双向或随机访问
auto it = v.begin();
std::advance(it, 2); // 指向第 3 个元素
```

---

**基本写法：移动到下一位置**
`std::next(<迭代器> [, <步数>])`
```cpp
// 返回前进后的副本，不修改原迭代器
auto it = std::next(v.begin()); // 指向第 2 个元素
auto it2 = std::next(v.begin(), 2);
```

---

**基本写法：移动到上一位置**
`std::prev(<迭代器> [, <步数>])`
```cpp
// 返回后退后的副本，需双向迭代器
auto it = std::prev(v.end()); // 指向末元素
```

---

## 插入迭代器

**基本写法：尾插迭代器**
`std::back_inserter(<容器>)`
```cpp
// 每次赋值调用 push_back
std::vector<int> dst;
std::copy(v.begin(), v.end(), std::back_inserter(dst));
```

---

**基本写法：头插迭代器**
`std::front_inserter(<容器>)`
```cpp
// 每次赋值调用 push_front，需有该接口
std::list<int> dst;
std::copy(v.begin(), v.end(), std::front_inserter(dst));
```

---

**基本写法：任意位置插入迭代器**
`std::inserter(<容器>, <位置>)`
```cpp
// 在指定位置前插入
auto it = std::inserter(dst, dst.begin());
```

---

**基本写法：移动迭代器**
`std::make_move_iterator(<迭代器>)`
```cpp
// 将解引用转为右值引用，触发移动
std::vector<std::string> v2(std::make_move_iterator(v.begin()),
                           std::make_move_iterator(v.end()));
```

---

## 流迭代器

**基本写法：输入流迭代器**
`std::istream_iterator<T>(<流>)`
```cpp
// 从输入流读取 T 序列
std::vector<int> v2((std::istream_iterator<int>(std::cin)),
                    std::istream_iterator<int>());
```

---

**基本写法：输出流迭代器**
`std::ostream_iterator<T>(<流> [, <分隔串>])`
```cpp
// 将元素写入输出流
std::copy(v.begin(), v.end(),
          std::ostream_iterator<int>(std::cout, ", "));
```

---

## C++20 哨兵与范围

**基本写法：哨兵判断结束**
`<范围>.end()` 可与迭代器不同类型
```cpp
// C++20 允许 end() 返回哨兵类型，如 read_until_eof 的结束判断
// 算法用 == 比较迭代器与哨兵
```

---

**基本写法：ranges 迭代器**
`std::ranges::begin(<范围>)`
```cpp
// 范式库的迭代器接口，返回第一元素
auto it = std::ranges::begin(v);
auto end = std::ranges::end(v);
```

---

**基本写法：view 迭代**
`for (auto&& <x> : <视图>)`
```cpp
// 视图是惰性迭代的轻量范围
auto even = v | std::views::filter([](int x){ return x % 2 == 0; });
for (int x : even) { std::cout << x; }
```

---

## 自定义迭代器

**基本写法：迭代器特征别名**
`std::iterator_traits<<迭代器类型>>`
```cpp
// 提取 value_type/difference_type/pointer/reference
using traits = std::iterator_traits<std::vector<int>::iterator>;
traits::value_type n = 0;
```

---

**基本写法：C++20 概念约束迭代器**
`std::input_iterator<I>`
```cpp
#include <iterator>
// 用 concept 约束模板迭代器类型
template <std::input_iterator It>
auto sum(It first, It last) {
    return std::accumulate(first, last, 0);
}
```

---

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
| C++ STL 迭代器 | 069-CppSTLIterator | 本文自身 |
| C++ tuple 与 pair | 070-CppTuplePair | 本文的并列主题 |
| C++ variant / optional / any | 071-CppVariantOptionalAny | 本文的并列主题 |
| C++ CMake 构建命令 | 072-CMakeBuild | 本文的并列主题 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
