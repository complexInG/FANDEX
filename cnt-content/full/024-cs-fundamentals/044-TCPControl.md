---
order: 111
title: TCP拥塞控制
module: 'cs-fundamentals'
category: 'comp-sci'
difficulty: intermediate
description: 'TCP 拥塞控制：慢启动、拥塞避免、快速重传、快速恢复算法与 BBR。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/HTTP缓存策略'
  - 'cs-fundamentals/HTTPS握手过程'
  - 'cs-fundamentals/TCP粘包与拆包'
  - 'cs-fundamentals/DNS解析流程'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 拥塞控制基础

### 1.1 拥塞窗口 cwnd

拥塞窗口 cwnd是TCP拥塞控制的重要组成部分。本节详细介绍拥塞窗口 cwnd的核心概念、工作原理和实际应用。

**关键要点**：

- 拥塞窗口 cwnd的定义与核心原理
- 拥塞窗口 cwnd的实现方式与技术细节
- 拥塞窗口 cwnd在实际场景中的应用与最佳实践
- 拥塞窗口 cwnd的常见问题与解决方案

拥塞窗口 cwnd在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 慢启动阈值 ssthresh

慢启动阈值 ssthresh是TCP拥塞控制的重要组成部分。本节详细介绍慢启动阈值 ssthresh的核心概念、工作原理和实际应用。

**关键要点**：

- 慢启动阈值 ssthresh的定义与核心原理
- 慢启动阈值 ssthresh的实现方式与技术细节
- 慢启动阈值 ssthresh在实际场景中的应用与最佳实践
- 慢启动阈值 ssthresh的常见问题与解决方案

慢启动阈值 ssthresh在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 四大算法

### 2.1 慢启动

慢启动是TCP拥塞控制的重要组成部分。本节详细介绍慢启动的核心概念、工作原理和实际应用。

**关键要点**：

- 慢启动的定义与核心原理
- 慢启动的实现方式与技术细节
- 慢启动在实际场景中的应用与最佳实践
- 慢启动的常见问题与解决方案

慢启动在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 拥塞避免

拥塞避免是TCP拥塞控制的重要组成部分。本节详细介绍拥塞避免的核心概念、工作原理和实际应用。

**关键要点**：

- 拥塞避免的定义与核心原理
- 拥塞避免的实现方式与技术细节
- 拥塞避免在实际场景中的应用与最佳实践
- 拥塞避免的常见问题与解决方案

拥塞避免在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 快速重传

快速重传是TCP拥塞控制的重要组成部分。本节详细介绍快速重传的核心概念、工作原理和实际应用。

**关键要点**：

- 快速重传的定义与核心原理
- 快速重传的实现方式与技术细节
- 快速重传在实际场景中的应用与最佳实践
- 快速重传的常见问题与解决方案

快速重传在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.4 快速恢复

快速恢复是TCP拥塞控制的重要组成部分。本节详细介绍快速恢复的核心概念、工作原理和实际应用。

**关键要点**：

- 快速恢复的定义与核心原理
- 快速恢复的实现方式与技术细节
- 快速恢复在实际场景中的应用与最佳实践
- 快速恢复的常见问题与解决方案

快速恢复在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 拥塞控制变体

### 3.1 Reno / Cubic

Reno / Cubic是TCP拥塞控制的重要组成部分。本节详细介绍Reno / Cubic的核心概念、工作原理和实际应用。

**关键要点**：

- Reno / Cubic的定义与核心原理
- Reno / Cubic的实现方式与技术细节
- Reno / Cubic在实际场景中的应用与最佳实践
- Reno / Cubic的常见问题与解决方案

Reno / Cubic在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 BBR 算法

BBR 算法是TCP拥塞控制的重要组成部分。本节详细介绍BBR 算法的核心概念、工作原理和实际应用。

**关键要点**：

- BBR 算法的定义与核心原理
- BBR 算法的实现方式与技术细节
- BBR 算法在实际场景中的应用与最佳实践
- BBR 算法的常见问题与解决方案

BBR 算法在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 流量控制 vs 拥塞控制

### 4.1 滑动窗口

滑动窗口是TCP拥塞控制的重要组成部分。本节详细介绍滑动窗口的核心概念、工作原理和实际应用。

**关键要点**：

- 滑动窗口的定义与核心原理
- 滑动窗口的实现方式与技术细节
- 滑动窗口在实际场景中的应用与最佳实践
- 滑动窗口的常见问题与解决方案

滑动窗口在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 区别与联系

区别与联系是TCP拥塞控制的重要组成部分。本节详细介绍区别与联系的核心概念、工作原理和实际应用。

**关键要点**：

- 区别与联系的定义与核心原理
- 区别与联系的实现方式与技术细节
- 区别与联系在实际场景中的应用与最佳实践
- 区别与联系的常见问题与解决方案

区别与联系在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

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
| TCP拥塞控制 | 044-TCPControl | 本文自身 |
| TCP粘包与拆包 | 045-TCP | 本文的并列主题 |
| DNS解析流程 | 046-DNSFlow | 本文的并列主题 |
| CDN原理 | 047-CDNPrinciple | 本文的原理深化 |
| WebSocket帧格式 | 048-WebSocketFrameFormat | 本文的并列主题 |
| QUIC协议 | 049-QUIC | 本文的并列主题 |
| ARP协议与ARP欺骗 | 050-ARPARP | 本文的并列主题 |
| BGP路由协议 | 051-BGPRoute | 本文的并列主题 |
| 词法分析 | 052-LexicalAnalysis | 本文的并列主题 |
| 语法分析 | 053-GrammarAnalysis | 本文的并列主题 |
| 语义分析 | 054-SemanticAnalysis | 本文的并列主题 |
| 中间代码 | 055-IntermediateCode | 本文的并列主题 |
| 代码优化 | 056-CodeOptimization | 本文的性能延伸 |
| 目标代码生成 | 057-TargetCodeGeneration | 本文的并列主题 |
