---
order: 720
title: C++ CMake 构建命令
module: cpp

category: '026-cpp'
difficulty: beginner
description: C++ CMake 构建命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## CMake 基础

**基本写法：最小 CMakeLists.txt**
`cmake_minimum_required(VERSION <版本>)`
```cmake
# CMake 项目配置文件
cmake_minimum_required(VERSION 3.15)
project(MyApp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(app main.cpp)
```

---

**基本写法：命令行生成构建**
`cmake -S <源目录> -B <构建目录>`
```bash
# 配置生成构建文件
cmake -S . -B build
# -S 源目录（含 CMakeLists.txt）
# -B 构建目录（生成文件位置）
```

---

**基本写法：指定生成器**
`cmake -G <生成器> -S . -B build`
```bash
# 指定构建系统
cmake -G "Unix Makefiles" -S . -B build   # Linux/macOS make
cmake -G Ninja -S . -B build              # Ninja（更快）
cmake -G "Visual Studio 17 2022" -S . -B build # MSVC
```

---

**基本写法：编译构建**
`cmake --build <构建目录>`
```bash
# 执行编译
cmake --build build
# 指定并行数
cmake --build build -j 8
# 指定配置（Debug/Release）
cmake --build build --config Release
```

---

## 目标与源文件

**基本写法：添加可执行文件**
`add_executable(<名称> <源文件>...)`
```cmake
# 定义可执行目标
add_executable(app main.cpp utils.cpp io.cpp)
```

---

**基本写法：添加静态库**
`add_library(<名称> STATIC <源文件>...)`
```cmake
# 静态库
add_library(mylib STATIC utils.cpp io.cpp)
```

---

**基本写法：添加动态库**
`add_library(<名称> SHARED <源文件>...)`
```cmake
# 动态库
add_library(mylib SHARED utils.cpp io.cpp)
# 头文件库（interface）
add_library(mylib INTERFACE)
```

---

**基本写法：链接库**
`target_link_libraries(<目标> <库>...)`
```cmake
# 链接依赖库
target_link_libraries(app PRIVATE mylib)
target_link_libraries(app PRIVATE pthread)
# PRIVATE   仅当前目标使用
# PUBLIC    当前目标及依赖者使用
# INTERFACE 仅依赖者使用
```

---

**基本写法：包含目录**
`target_include_directories(<目标> <可见性> <路径>...)`
```cmake
# 头文件搜索路径
target_include_directories(app PRIVATE include)
target_include_directories(app PUBLIC
    ${CMAKE_SOURCE_DIR}/include
)
```

---

## 编译选项

**基本写法：设置编译选项**
`target_compile_options(<目标> <可见性> <选项>...)`
```cmake
# 添加编译选项
target_compile_options(app PRIVATE -Wall -Wextra -Werror)
# 条件添加
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(app PRIVATE -O2 -pipe)
endif()
```

---

**基本写法：设置 C++ 标准**
`set(CMAKE_CXX_STANDARD <版本>)`
```cmake
# 全局设置标准
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF) # 禁用编译器扩展
# 或针对单个目标
set_property(TARGET app PROPERTY CXX_STANDARD 20)
```

---

**基本写法：编译定义**
`target_compile_definitions(<目标> <可见性> <定义>...)`
```cmake
# 预处理宏定义
target_compile_definitions(app PRIVATE DEBUG=1)
target_compile_definitions(app PUBLIC VERSION="1.0.0")
```

---

## 构建类型

**基本写法：构建类型**
`set(CMAKE_BUILD_TYPE <类型>)`
```cmake
# 构建类型：Debug/Release/RelWithDebInfo/MinSizeRel
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()
# 命令行指定
# cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
```

---

**基本写法：类型专属选项**
`set(CMAKE_CXX_FLAGS_<类型> <选项>)`
```cmake
# 各类型编译选项
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0 -DDEBUG")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "-O2 -g")
```

---

## 查找与使用依赖

**基本写法：find_package 查找包**
`find_package(<包名> [版本] [REQUIRED])`
```cmake
# 查找已安装的包
find_package(Threads REQUIRED)
find_package(OpenCV 4.5 REQUIRED)
find_package(fmt CONFIG REQUIRED)
```

---

**基本写法：使用 find_package 结果**
`<包>::<目标>`
```cmake
# 链接找到的库目标
target_link_libraries(app PRIVATE Threads::Threads)
target_link_libraries(app PRIVATE fmt::fmt)
target_link_libraries(app PRIVATE ${OpenCV_LIBS})
```

---

**基本写法：查找系统库**
`find_library(<变量> <库名>)`
```cmake
# 查找系统库
find_library(MATH_LIB m)
target_link_libraries(app PRIVATE ${MATH_LIB})
```

---

## 子目录与安装

**基本写法：添加子目录**
`add_subdirectory(<目录>)`
```cmake
# 包含子项目的 CMakeLists.txt
add_subdirectory(src)
add_subdirectory(lib/mylib)
```

---

**基本写法：安装规则**
`install(TARGETS <目标> DESTINATION <目录>)`
```cmake
# 安装目标
install(TARGETS app DESTINATION bin)
install(TARGETS mylib DESTINATION lib)
install(DIRECTORY include/ DESTINATION include)
```

---

## 变量与条件

**基本写法：设置变量**
`set(<变量> <值>)`
```cmake
# 变量赋值
set(SOURCES main.cpp utils.cpp)
set(MY_VERSION 1.0.0)
# 使用变量
add_executable(app ${SOURCES})
```

---

**基本写法：条件判断**
`if(<条件>) ... elseif() ... else() ... endif()`
```cmake
# 条件分支
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_definitions(app PRIVATE DEBUG=1)
elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
    target_compile_definitions(app PRIVATE NDEBUG=1)
endif()
```

---

## 实用命令

**基本写法：打印消息**
`message(<模式> <消息>)`
```cmake
# 输出消息
message(STATUS "配置开始")
message(WARNING "自定义警告")
message(FATAL_ERROR "致命错误，停止配置")
```

---

**基本写法：列出源文件**
`file(GLOB <变量> <模式>)`
```cmake
# 通配符收集源文件
file(GLOB SOURCES src/*.cpp)
file(GLOB_RECURSE SOURCES src/*.cpp) # 递归
add_executable(app ${SOURCES})
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
| C++ CMake 构建命令 | 072-CMakeBuild | 本文自身 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
