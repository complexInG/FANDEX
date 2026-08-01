---
order: 740
title: C++ 链接与符号
module: cpp

category: '026-cpp'
difficulty: beginner
description: C++ 链接与符号 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 链接基础

**基本写法：链接目标文件**
`g++ <对象文件>... -o <输出>`
```bash
# 链接多个目标文件
g++ main.o utils.o io.o -o app
# 链接时指定库
g++ main.o -L./lib -lutils -o app
```

---

**基本写法：静态链接**
`g++ <源文件> -static -o <输出>`
```bash
# 完全静态链接
g++ main.cpp -static -o app
# 静态库参与链接
g++ main.cpp libutils.a -o app
```

---

**基本写法：动态链接**
`g++ <源文件> -l<库> -o <输出>`
```bash
# 链接动态库
g++ main.cpp -lutils -o app
# 运行时需要找到 .so
LD_LIBRARY_PATH=/path/to/lib ./app
```

---

## 符号查看

**基本写法：nm 列出符号**
`nm <目标文件>`
```bash
# 列出目标文件符号
nm main.o
nm -C main.o          # C++ 符号 demangle
nm -D libutils.so     # 动态符号
# 符号类型：
# T  代码段（已定义函数）
# U  未定义（外部引用）
# D  已初始化数据
# B  未初始化数据
# W  弱符号
```

---

**基本写法：demangle C++ 符号**
`c++filt <符号>`
```bash
# 还原 C++ 修饰名
echo _ZN3foo3barEv | c++filt
# 输出 foo::bar()
nm main.o | c++filt
```

---

**基本写法：objdump 反汇编**
`objdump -d <文件>`
```bash
# 反汇编目标文件
objdump -d main.o
objdump -d -M intel main.o    # Intel 语法
objdump -t libutils.so        # 符号表
objdump -T libutils.so        # 动态符号
objdump -h main.o             # 段信息
```

---

**基本写法：readelf 查看 ELF**
`readelf -a <文件>`
```bash
# 查看 ELF 文件信息
readelf -h app           # ELF 头
readelf -S app           # 段表
readelf -s app           # 符号表
readelf -d app           # 动态段
readelf -l app           # 程序头
```

---

## 动态库依赖

**基本写法：ldd 查看依赖**
`ldd <可执行文件>`
```bash
# 查看动态库依赖
ldd ./app
# 输出示例：
# libutils.so => ./libutils.so
# libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
```

---

**基本写法：ldconfig 配置**
`ldconfig [<目录>]`
```bash
# 更新动态链接器缓存
sudo ldconfig
sudo ldconfig /opt/mylib
# 查看缓存
ldconfig -p | grep utils
```

---

**基本写法：RPATH/RUNPATH**
`g++ -Wl,-rpath,<路径> <源文件>`
```bash
# 嵌入运行时库搜索路径
g++ main.cpp -L./lib -lutils -Wl,-rpath,./lib -o app
# -Wl,-rpath,$ORIGIN  相对可执行文件位置
g++ main.cpp -L./lib -lutils -Wl,-rpath,\$ORIGIN -o app
```

---

## 链接错误排查

**基本写法：未定义引用**
`undefined reference to \`<符号>\``
```bash
# 常见链接错误
# 1. 检查库是否链接
g++ main.cpp -lutils  # 添加 -l
# 2. 检查库顺序（被依赖的放后面）
g++ main.cpp -lA -lB  # 若 A 依赖 B
# 3. 检查库路径
g++ main.cpp -L./lib -lutils
```

---

**基本写法：重复定义**
`multiple definition of \`<符号>\``
```bash
# 符号重复定义
# 1. 检查是否在头文件中定义了全局变量/函数
# 2. 使用 inline 或 static 限制作用域
# 3. 头文件中只声明，源文件中定义
```

---

## 弱符号与可见性

**基本写法：弱符号**
`__attribute__((weak)) <声明>`
```cpp
// 弱符号：可被强符号覆盖
__attribute__((weak)) void hook() {
    // 默认实现
}
// 其他目标文件定义同名强符号会覆盖此实现
```

---

**基本写法：符号可见性**
`__attribute__((visibility("<可见性>"))`
```cpp
// 控制符号在动态库中的可见性
__attribute__((visibility("default"))) void api_func();
__attribute__((visibility("hidden"))) void internal_func();
// 默认隐藏，显式导出
// 编译选项：-fvisibility=hidden
```

---

## 链接脚本与控制

**基本写法：链接脚本**
`ld -T <脚本文件> <对象文件>`
```bash
# 使用自定义链接脚本
ld -T linker.ld main.o -o app
```

---

**基本写法：Map 文件**
`g++ -Wl,-Map,<文件> <源文件>`
```bash
# 生成链接 map 文件（查看符号地址）
g++ main.cpp -Wl,-Map,app.map -o app
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
| C++ 链接与符号 | 074-LinkSymbol | 本文自身 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
