---
order: 710
title: C++ variant / optional / any
module: 026-cpp
category: '026-cpp'
difficulty: beginner
description: C++ variant / optional / any 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# C++ variant / optional / any

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## std::optional 可选值

**基本写法：构造 optional**
`std::optional<<类型>> <变量>;`
```cpp
// 表示可能存在也可能不存在的值，避免用裸指针或特殊值
std::optional<int> find_id(const std::string& name);
std::optional<int> oid = find_id("x");
```

---

**基本写法：构造有值**
`std::optional<<类型>>(<值>)`
```cpp
// 直接用值构造
std::optional<int> o(42);
auto o2 = std::make_optional(3.14); // 自动推导类型
```

---

**基本写法：判空**
`<optional>.has_value()`
```cpp
// 判断是否持有值
if (oid.has_value()) { std::cout << *oid; }
```

---

**基本写法：解引用取值**
`*<optional>` / `<optional>.value()`
```cpp
// value() 在空时抛 std::bad_optional_access，* 不检查
int a = *oid;
int b = oid.value();
```

---

**基本写法：取值或默认**
`<optional>.value_or(<默认值>)`
```cpp
// 为空时返回默认值
int id = oid.value_or(-1);
```

---

**基本写法：置空**
`<optional>.reset()` / `<optional> = std::nullopt`
```cpp
// 清空当前值
oid.reset();
oid = std::nullopt;
```

---

**基本写法：值存在时执行**
`<optional>.and_then(<函数>)`
```cpp
// C++23：值存在则应用函数返回新 optional，否则返回空
auto name = oid.and_then([](int i){ return std::optional<std::string>(std::to_string(i)); });
```

---

## std::variant 多值容器

**基本写法：定义 variant**
`std::variant<<类型>...> <变量>;`
```cpp
// 类型安全的联合体，同一时刻持有其一候选类型
std::variant<int, double, std::string> v;
```

---

**基本写法：赋值**
`<variant> = <值>;`
```cpp
// 赋值后自动记录当前活跃类型
v = 42;          // 当前为 int
v = std::string("hi"); // 切换为 string
```

---

**基本写法：按索引取值**
`std::get<<索引>>(<variant>)`
```cpp
// 编译期按位置取出，类型不符抛 std::bad_variant_access
int i = std::get<0>(v);
```

---

**基本写法：按类型取值**
`std::get<<类型>>(<variant>)`
```cpp
// 按类型取出，需该类型当前活跃
std::string s = std::get<std::string>(v);
```

---

**基本写法：安全取指针**
`std::get_if<<类型>>(&<variant>)`
```cpp
// 类型匹配返回指针，否则返回 nullptr，不抛异常
if (auto p = std::get_if<int>(&v)) { std::cout << *p; }
```

---

**基本写法：查询当前索引**
`<variant>.index()`
```cpp
// 返回当前活跃类型的索引
std::size_t idx = v.index();
```

---

**基本写法：判断是否持有某类型**
`std::holds_alternative<<类型>>(<variant>)`
```cpp
// 编译期类型查询
if (std::holds_alternative<int>(v)) { /* int 活跃 */ }
```

---

**基本写法：访问者模式**
`std::visit(<访问者>, <variant>)`
```cpp
// 对活跃类型分派到访问者的对应 operator()
auto printer = [](auto&& x) { std::cout << x; };
std::visit(printer, v);
```

---

**基本写法：多 variant 访问**
`std::visit(<访问者>, <variant1>, <variant2>)`
```cpp
// 同时对多个 variant 分派，访问者接收每种组合
auto add = [](auto a, auto b) { return a + b; };
auto r = std::visit(add, v1, v2);
```

---

**基本写法：空状态标记类型**
`std::variant<std::monostate, <其他类型>...>`
```cpp
// monostate 作为默认首类型，使 variant 默认构造不抛异常
std::variant<std::monostate, int, double> v2;
```

---

**基本写法：泛型 lambda 访问**
`std::visit([](auto&& x){...}, <variant>)`
```cpp
// 用泛型 lambda 统一处理，按活跃类型实例化
std::visit([](auto&& x){ std::cout << x << "\n"; }, v);
```

---

**基本写法：overload 访问者**
`struct { auto operator()(<类型>) {...} ... }`
```cpp
// 手写结构体重载每类型，或用辅助模板组合多个 lambda
struct Visitor {
    void operator()(int i) { std::cout << "int:" << i; }
    void operator()(const std::string& s) { std::cout << "str:" << s; }
};
std::visit(Visitor{}, v);
```

---

## std::any 任意类型

**基本写法：构造 any**
`std::any <变量>;`
```cpp
// 持有任意可复制构造类型的值
std::any a;
```

---

**基本写法：赋值**
`std::any <变量> = <值>;`
```cpp
// 用任意类型赋值，类型信息被记录
a = 42;
a = std::string("hi"); // 后赋值覆盖前值
```

---

**基本写法：判空**
`<any>.has_value()`
```cpp
// 判断是否持有值
if (!a.has_value()) { /* 空 */ }
```

---

**基本写法：取类型信息**
`<any>.type()`
```cpp
// 返回 const std::type_info&，需 <typeinfo>
if (a.type() == typeid(int)) { /* 当前持有 int */ }
```

---

**基本写法：取值**
`std::any_cast<<类型>>(<any>)`
```cpp
// 类型匹配返回值，不匹配抛 std::bad_any_cast
int i = std::any_cast<int>(a);
```

---

**基本写法：安全取指针**
`std::any_cast<<类型>>(&<any>)`
```cpp
// 返回指针，类型不符返回 nullptr
if (auto p = std::any_cast<int>(&a)) { std::cout << *p; }
```

---

**基本写法：置空**
`<any>.reset()` / `<any> = std::nullopt` 不适用
```cpp
// any 用 reset 清空
a.reset();
```

---

## 选型对比

**基本写法：何时用哪个**
`optional` / `variant` / `any`
```cpp
// optional：可能无值或单类型缺失值
// variant：有限已知类型集合中选一（编译期类型安全）
// any：完全未知类型、运行期动态类型（牺牲类型安全）
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
| C++ STL 迭代器 | 069-CppSTLIterator | 本文的并列主题 |
| C++ tuple 与 pair | 070-CppTuplePair | 本文的并列主题 |
| C++ variant / optional / any | 071-CppVariantOptionalAny | 本文自身 |
| C++ CMake 构建命令 | 072-CMakeBuild | 本文的并列主题 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
