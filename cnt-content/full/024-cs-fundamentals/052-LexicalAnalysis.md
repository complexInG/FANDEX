---
order: 119
title: 词法分析
module: 'cs-fundamentals'
category: 'comp-sci'
difficulty: intermediate
description: '编译器词法分析：正则表达式、NFA、DFA 与 Token 识别。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/ARP协议与ARP欺骗'
  - 'cs-fundamentals/BGP路由协议'
  - 'cs-fundamentals/语法分析'
  - 'cs-fundamentals/语义分析'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 词法分析概述

### 1.1 Token 定义

Token 定义是词法分析的重要组成部分。本节详细介绍Token 定义的核心概念、工作原理和实际应用。

**关键要点**：

- Token 定义的定义与核心原理
- Token 定义的实现方式与技术细节
- Token 定义在实际场景中的应用与最佳实践
- Token 定义的常见问题与解决方案

Token 定义在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 词法分析器接口

词法分析器接口是词法分析的重要组成部分。本节详细介绍词法分析器接口的核心概念、工作原理和实际应用。

**关键要点**：

- 词法分析器接口的定义与核心原理
- 词法分析器接口的实现方式与技术细节
- 词法分析器接口在实际场景中的应用与最佳实践
- 词法分析器接口的常见问题与解决方案

词法分析器接口在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 正则表达式

### 2.1 正则语法

正则语法是词法分析的重要组成部分。本节详细介绍正则语法的核心概念、工作原理和实际应用。

**关键要点**：

- 正则语法的定义与核心原理
- 正则语法的实现方式与技术细节
- 正则语法在实际场景中的应用与最佳实践
- 正则语法的常见问题与解决方案

正则语法在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 正则到 NFA（Thompson 构造）

正则到 NFA（Thompson 构造）是词法分析的重要组成部分。本节详细介绍正则到 NFA（Thompson 构造）的核心概念、工作原理和实际应用。

**关键要点**：

- 正则到 NFA（Thompson 构造）的定义与核心原理
- 正则到 NFA（Thompson 构造）的实现方式与技术细节
- 正则到 NFA（Thompson 构造）在实际场景中的应用与最佳实践
- 正则到 NFA（Thompson 构造）的常见问题与解决方案

正则到 NFA（Thompson 构造）在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. NFA 到 DFA

### 3.1 子集构造法

子集构造法是词法分析的重要组成部分。本节详细介绍子集构造法的核心概念、工作原理和实际应用。

**关键要点**：

- 子集构造法的定义与核心原理
- 子集构造法的实现方式与技术细节
- 子集构造法在实际场景中的应用与最佳实践
- 子集构造法的常见问题与解决方案

子集构造法在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 DFA 最小化

DFA 最小化是词法分析的重要组成部分。本节详细介绍DFA 最小化的核心概念、工作原理和实际应用。

**关键要点**：

- DFA 最小化的定义与核心原理
- DFA 最小化的实现方式与技术细节
- DFA 最小化在实际场景中的应用与最佳实践
- DFA 最小化的常见问题与解决方案

DFA 最小化在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 实现

### 4.1 状态转移表

状态转移表是词法分析的重要组成部分。本节详细介绍状态转移表的核心概念、工作原理和实际应用。

**关键要点**：

- 状态转移表的定义与核心原理
- 状态转移表的实现方式与技术细节
- 状态转移表在实际场景中的应用与最佳实践
- 状态转移表的常见问题与解决方案

状态转移表在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 Lex/Flex 工具

Lex/Flex 工具是词法分析的重要组成部分。本节详细介绍Lex/Flex 工具的核心概念、工作原理和实际应用。

**关键要点**：

- Lex/Flex 工具的定义与核心原理
- Lex/Flex 工具的实现方式与技术细节
- Lex/Flex 工具在实际场景中的应用与最佳实践
- Lex/Flex 工具的常见问题与解决方案

Lex/Flex 工具在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 参考文献

CSAPP（深入理解计算机系统）：https://csapp.cs.cmu.edu/
算法导论（CLRS）：https://mitpress.mit.edu/9780262046305/
MIT OpenCourseWare 6.006：https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
Teach Yourself CS：https://teachyourselfcs.com/

## 延伸阅读

数据结构与算法，见 023-algorithm 模块。
操作系统概念，见 024-cs-fundamentals 模块相关文档。
计算机体系结构，见 001-getting-started 模块相关文档。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供计算机基础课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 大 O 分析与复杂度推导

渐进符号：O（上界）、Ω（下界）、Θ（紧界）；常数与低阶项忽略。
常见阶：O(1)、O(log n)、O(n)、O(n log n)、O(n²)、O(2ⁿ)；识别主循环与递归式。
主定理：T(n)=aT(n/b)+f(n) 的三种情形。
实践：先估规模与时限，再选算法与数据结构。

### 13.2 缓存与局部性

时间局部性：近期访问的数据再访问；空间局部性：邻近数据一起访问。
缓存行：64 字节粒度；数组遍历比链表友好。
伪共享：多线程改同一缓存行不同变量，缓存乒乓。
优化手段：数据结构重排、分块（blocking）、无锁队列。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 计算机科学概述 | 001-ComputerOverview | 本文的前置基础 |
| 计算机体系结构 | 002-ComputerArchitecture | 本文的并列主题 |
| 操作系统 | 003-OperatingSystem | 本文的并列主题 |
| 计算机网络 | 004-ComputerNetwork | 本文的并列主题 |
| 数字逻辑 | 005-DigitalLogic | 本文的并列主题 |
| 离散数学 | 006-DiscreteMathematics | 本文的并列主题 |
| 计算机组成原理 | 007-ComputerPrinciple | 本文的原理深化 |
| 数据表示与运算 | 008-DataRepresentationOperation | 本文的并列主题 |
| 指令流水线 | 009-DirectivePipeline | 本文的并列主题 |
| 存储系统 | 010-StorageSystem | 本文的并列主题 |
| 总线与接口 | 011-BusAndInterface | 本文的并列主题 |
| 并行计算 | 012-ParallelCalculate | 本文的并列主题 |
| 分布式系统 | 013-DistributedSystem | 本文的并列主题 |
| 算法设计与分析 | 014-AlgorithmDesignAnalysis | 本文的并列主题 |
| 形式语言与自动机 | 015-FormalLanguageAndAutomata | 本文的并列主题 |
| 信息安全基础 | 016-InformationSecurityBasics | 本文的前置基础 |
| 编译原理 | 017-CompilePrinciple | 本文的原理深化 |
| 软件工程 | 018-SoftwareEngineering | 本文的并列主题 |
| 数据库系统原理 | 019-DatabaseSystemPrinciple | 本文的原理深化 |
| 编译原理进阶 | 020-CompilePrincipleAdvanced | 本文的原理深化 |
| 操作系统进阶 | 021-OperatingSystemAdvanced | 本文的并列主题 |
| 计算机网络进阶 | 022-ComputerNetworkAdvanced | 本文的并列主题 |
| 网络安全 | 023-NetworkSecurity | 本文的安全延伸 |
| 多媒体技术 | 024-MultimediaTechnology | 本文的并列主题 |
| 人工智能基础 | 025-AIFundamentals | 本文的前置基础 |
| 计算机图形学 | 026-ComputerShape | 本文的并列主题 |
| 设计模式 | 027-DesignPattern | 本文的并列主题 |
| 软件体系结构 | 028-SoftwareSystemStructure | 本文的并列主题 |
| 人机交互 | 029-HCI | 本文的并列主题 |
| 编程语言理论 | 030-ProgrammingLanguageTheory | 本文的并列主题 |
| 网络协议深度 | 031-NetworkProtocolDeep | 本文的并列主题 |
| 编译与运行时 | 032-CompileAndRuntime | 本文的并列主题 |
| 进程PCB与线程TCB | 033-PCBThreadTCB | 本文的并列主题 |
| 中断与系统调用 | 034-InterruptAndSystemCall | 本文的并列主题 |
| 用户态与内核态切换 | 035-UserModeKernelModeSwitch | 本文的并列主题 |
| 内存分段与分页 | 036-MemorySegmentationAndPaging | 本文的并列主题 |
| 页面置换算法 | 037-PageReplacementAlgorithm | 本文的并列主题 |
| 文件系统inode | 038-FileSystemInode | 本文的并列主题 |
| 磁盘调度 | 039-DiskScheduling | 本文的并列主题 |
| 零拷贝 | 040-ZeroCopy | 本文的并列主题 |
| 进程间通信 | 041-IPC | 本文的并列主题 |
| HTTP缓存策略 | 042-HTTPCacheStrategy | 本文的并列主题 |
| HTTPS握手过程 | 043-HTTPSHandshake | 本文的并列主题 |
| TCP拥塞控制 | 044-TCPControl | 本文的并列主题 |
| TCP粘包与拆包 | 045-TCP | 本文的并列主题 |
| DNS解析流程 | 046-DNSFlow | 本文的并列主题 |
| CDN原理 | 047-CDNPrinciple | 本文的原理深化 |
| WebSocket帧格式 | 048-WebSocketFrameFormat | 本文的并列主题 |
| QUIC协议 | 049-QUIC | 本文的并列主题 |
| ARP协议与ARP欺骗 | 050-ARPARP | 本文的并列主题 |
| BGP路由协议 | 051-BGPRoute | 本文的并列主题 |
| 词法分析 | 052-LexicalAnalysis | 本文自身 |
| 语法分析 | 053-GrammarAnalysis | 本文的并列主题 |
| 语义分析 | 054-SemanticAnalysis | 本文的并列主题 |
| 中间代码 | 055-IntermediateCode | 本文的并列主题 |
| 代码优化 | 056-CodeOptimization | 本文的性能延伸 |
| 目标代码生成 | 057-TargetCodeGeneration | 本文的并列主题 |
