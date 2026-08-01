---
order: 730
title: C++ 调试命令
module: 026-cpp
category: '026-cpp'
difficulty: beginner
description: C++ 调试命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## gdb 基础

**基本写法：启动 gdb**
`gdb <可执行文件>`
```bash
# 启动调试器
gdb ./app
# 带参数运行
gdb --args ./app arg1 arg2
# 带核心转储
gdb ./app core.dump
```

---

**基本写法：运行程序**
`run [参数]` 或 `r`
```bash
gdb> run              # 开始运行
gdb> run arg1 arg2    # 带参数运行
gdb> start            # 在 main 处暂停
```

---

**基本写法：断点**
`break <位置>` 或 `b <位置>`
```bash
gdb> break main         # 函数处断点
gdb> break main.cpp:42  # 文件行号断点
gdb> break 42           # 当前行号断点
gdb> tbreak main        # 临时断点（触发一次后删除）
gdb> break if x == 5    # 条件断点
```

---

**基本写法：管理断点**
`delete/info/disable/enable <断点号>`
```bash
gdb> info breakpoints   # 列出所有断点
gdb> delete 2           # 删除 2 号断点
gdb> delete             # 删除所有断点
gdb> disable 1          # 禁用 1 号断点
gdb> enable 1           # 启用
gdb> ignore 1 5         # 忽略前 5 次触发
```

---

**基本写法：单步执行**
`step / next / finish`
```bash
gdb> step        # 单步进入函数（s）
gdb> next        # 单步不进入函数（n）
gdb> finish      # 运行到当前函数结束
gdb> continue    # 继续运行（c）
gdb> until 50    # 运行到第 50 行
```

---

**基本写法：查看变量**
`print <表达式>` 或 `p <表达式>`
```bash
gdb> print x          # 查看变量
gdb> print x = 10     # 修改变量值
gdb> print *arr@5     # 查看数组前 5 个元素
gdb> print myvec.size()
gdb> display x        # 每次停止自动显示
```

---

**基本写法：查看内存**
`x/<数量><格式><大小> <地址>`
```bash
# 检查内存
gdb> x/10xw 0xaddr    # 10 个 16 进制 4 字节
gdb> x/4cb &ch        # 4 个字符字节
# 格式：x 16进制 d 十进制 c 字符 s 字符串
# 大小：b 字节 h 半字 w 字 g 双字
```

---

**基本写法：查看栈**
`backtrace` 或 `bt`
```bash
gdb> backtrace        # 查看调用栈
gdb> bt full          # 带局部变量
gdb> frame 2          # 切换到第 2 帧
gdb> up / down        # 上一帧/下一帧
gdb> info locals      # 当前帧局部变量
gdb> info args        # 当前帧参数
```

---

**基本写法：监视点**
`watch <表达式>`
```bash
# 数据变化时暂停
gdb> watch x          # 写入时触发
gdb> rwatch x         # 读取时触发
gdb> awatch x         # 读写都触发
```

---

## gdb 进阶

**基本写法：线程调试**
`info threads / thread <号>`
```bash
gdb> info threads        # 列出所有线程
gdb> thread 2            # 切换到 2 号线程
gdb> thread apply all bt # 所有线程栈
gdb> set scheduler-locking on # 锁定其他线程
```

---

**基本写法：信号处理**
`handle <信号> <动作>`
```bash
gdb> handle SIGINT stop    # 收到信号暂停
gdb> handle SIGUSR1 nostop # 不暂停
gdb> handle SIGSEGV stop print # 暂停并打印
```

---

**基本写法：调试已运行进程**
`gdb -p <PID>`
```bash
# 附加到运行中的进程
gdb -p 12345
# 或在 gdb 内
gdb> attach 12345
gdb> detach  # 分离
```

---

**基本写法：核心转储**
`gcore <PID>` 或 `ulimit -c unlimited`
```bash
# 启用核心转储
ulimit -c unlimited
# 运行崩溃后生成 core 文件
gdb ./app core
```

---

## lldb 调试

**基本写法：启动 lldb**
`lldb <可执行文件>`
```bash
# lldb 命令与 gdb 类似但语法不同
lldb ./app
lldb -- ./app arg1 arg2
```

---

**基本写法：lldb 常用命令对照**
`breakpoint / step / next / continue / frame`
```bash
lldb> breakpoint set --name main       # 设断点（b main）
lldb> breakpoint set --file main.cpp --line 42
lldb> run                              # 运行
lldb> step                             # 单步进入
lldb> next                             # 单步不进入
lldb> continue                         # 继续
lldb> frame variable                   # 查看局部变量
lldb> thread backtrace                 # 调用栈
```

---

**基本写法：lldb 查看变量**
`frame variable` 或 `expression`
```bash
lldb> frame variable x       # 查看变量
lldb> expression x           # 查看表达式
lldb> expression x = 10      # 修改变量
lldb> p x                    # print 简写
```

---

## 调试技巧

**基本写法：编译时加调试信息**
`g++ -g -O0 <源文件>`
```bash
# 调试专用编译选项
g++ -g -O0 -Wall main.cpp -o app
# -g3      最详细调试信息
# -O0      不优化（避免变量被优化掉）
```

---

**基本写法：AddressSanitizer**
`g++ -fsanitize=address -g <源文件>`
```bash
# 内存错误检测
g++ -fsanitize=address -g main.cpp -o app
./app
# 检测：越界、释放后使用、双重释放等
# 组合多个消毒器
g++ -fsanitize=address,undefined -g main.cpp -o app
```

---

**基本写法：命令脚本**
`gdb -x <脚本文件> <程序>`
```bash
# 自动执行 gdb 命令
# script.gdb 内容：
# break main
# run
# bt
gdb -x script.gdb ./app
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
| C++ 调试命令 | 073-DebugCommand | 本文自身 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
