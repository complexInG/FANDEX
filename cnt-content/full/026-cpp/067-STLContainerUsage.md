---
order: 670
title: C++ STL 容器使用速查
module: 026-cpp
category: '026-cpp'
difficulty: beginner
description: C++ STL 容器使用速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# C++ STL 容器使用速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## vector

**基本写法：创建 vector**
`std::vector<<类型>> <变量>;`
```cpp
// 动态数组
std::vector<int> v;
```

---

**基本写法：初始化列表**
`std::vector<<类型>> <变量> = {<元素>...};`
```cpp
// 列表初始化
std::vector<int> v = {1, 2, 3};
```

---

**基本写法：尾部添加**
`<v>.push_back(<值>);`
```cpp
// 末尾追加元素
v.push_back(4);
```

---

**基本写法：原地构造**
`<v>.emplace_back(<参数>...);`
```cpp
// 原地构造避免临时对象
v.emplace_back(42, "name");
```

---

**基本写法：访问元素**
`<v>[<索引>]` 或 `<v>.at(<索引>)`
```cpp
// at 带边界检查
int x = v.at(0);
```

---

**基本写法：删除尾部**
`<v>.pop_back();`
```cpp
// 移除末尾元素
v.pop_back();
```

---

## deque

**基本写法：双端队列**
`std::deque<<类型>> <变量>;`
```cpp
// 支持头尾高效增删
std::deque<int> dq;
```

---

**基本写法：头部添加**
`<dq>.push_front(<值>);`
```cpp
// 头部插入
dq.push_front(1);
```

---

## list / forward_list

**基本写法：双向链表**
`std::list<<类型>> <变量>;`
```cpp
// 双向链表
std::list<int> lst;
```

---

**基本写法：单链表**
`std::forward_list<<类型>> <变量>;`
```cpp
// 单向链表节省内存
std::forward_list<int> fl;
```

---

**基本写法：链表插入**
`<lst>.insert(<迭代器>, <值>);`
```cpp
// 指定位置插入
auto it = lst.begin();
lst.insert(it, 10);
```

---

**基本写法：链表删除**
`<lst>.remove(<值>);`
```cpp
// 按值删除所有匹配
lst.remove(10);
```

---

## array

**基本写法：固定大小数组**
`std::array<<类型>, <大小>> <变量>;`
```cpp
// 编译期固定大小数组
std::array<int, 5> arr = {1, 2, 3, 4, 5};
```

---

**基本写法：获取大小**
`<arr>.size()`
```cpp
// 编译期已知大小
size_t n = arr.size();
```

---

## map / unordered_map

**基本写法：有序映射**
`std::map<<键>, <值>> <变量>;`
```cpp
// 按键有序的映射
std::map<std::string, int> m;
```

---

**基本写法：哈希映射**
`std::unordered_map<<键>, <值>> <变量>;`
```cpp
// 哈希表实现查找更快
std::unordered_map<std::string, int> um;
```

---

**基本写法：插入键值对**
`<m>[<键>] = <值>;`
```cpp
// 下标操作插入或更新
m["apple"] = 3;
```

---

**基本写法：插入**
`<m>.insert({<键>, <值>});`
```cpp
// 插入键值对
m.insert({"pear", 5});
```

---

**基本写法：查找**
`<m>.find(<键>);`
```cpp
// 返回迭代器
auto it = m.find("apple");
if (it != m.end()) { /* 找到 */ }
```

---

**基本写法：判断包含 C++20**
`<m>.contains(<键>);`
```cpp
// 返回布尔值
bool has = m.contains("apple");
```

---

**基本写法：删除**
`<m>.erase(<键>);`
```cpp
// 按键删除
m.erase("apple");
```

---

## set / unordered_set

**基本写法：有序集合**
`std::set<<类型>> <变量>;`
```cpp
// 自动排序去重
std::set<int> s;
```

---

**基本写法：哈希集合**
`std::unordered_set<<类型>> <变量>;`
```cpp
// 哈希实现去重集合
std::unordered_set<int> us;
```

---

**基本写法：插入元素**
`<s>.insert(<值>);`
```cpp
// 插入元素
s.insert(10);
```

---

## stack / queue

**基本写法：栈**
`std::stack<<类型>> <变量>;`
```cpp
// 后进先出
std::stack<int> st;
st.push(1);
st.top();
st.pop();
```

---

**基本写法：队列**
`std::queue<<类型>> <变量>;`
```cpp
// 先进先出
std::queue<int> q;
q.push(1);
q.front();
q.pop();
```

---

**基本写法：优先队列**
`std::priority_queue<<类型>> <变量>;`
```cpp
// 大顶堆默认
std::priority_queue<int> pq;
pq.push(3);
pq.top();   // 最大值
```

---

**基本写法：小顶堆**
`std::priority_queue<<类型>, std::vector<<类型>>, std::greater<>> <变量>;`
```cpp
// 最小元素在顶
std::priority_queue<int, std::vector<int>, std::greater<>> min_pq;
```

---

## 通用操作

**基本写法：获取大小**
`<容器>.size()`
```cpp
// 元素个数
size_t n = v.size();
```

---

**基本写法：判断空**
`<容器>.empty()`
```cpp
// 是否为空
bool e = v.empty();
```

---

**基本写法：清空**
`<容器>.clear()`
```cpp
// 清空所有元素
v.clear();
```

---

**基本写法：遍历**
`for (auto& <项> : <容器>) { }`
```cpp
// 范围 for 循环
for (auto& x : v) { x *= 2; }
```

---

**基本写法：迭代器**
`<容器>.begin()` / `<容器>.end()`
```cpp
// 起止迭代器
for (auto it = v.begin(); it != v.end(); ++it) { }
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
| C++ STL 容器使用速查 | 067-STLContainerUsage | 本文自身 |
| C++ 结构化绑定语法速查手册 | 068-StructuredBinding | 本文的并列主题 |
| C++ STL 迭代器 | 069-CppSTLIterator | 本文的并列主题 |
| C++ tuple 与 pair | 070-CppTuplePair | 本文的并列主题 |
| C++ variant / optional / any | 071-CppVariantOptionalAny | 本文的并列主题 |
| C++ CMake 构建命令 | 072-CMakeBuild | 本文的并列主题 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
