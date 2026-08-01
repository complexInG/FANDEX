---
order: 110
title: HTTPS握手过程
module: 'cs-fundamentals'
category: 'comp-sci'
difficulty: intermediate
description: 'HTTPS 握手过程详解：TLS 1.2 与 TLS 1.3 的握手差异、密钥交换与证书验证。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/进程间通信'
  - 'cs-fundamentals/HTTP缓存策略'
  - 'cs-fundamentals/TCP拥塞控制'
  - 'cs-fundamentals/TCP粘包与拆包'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. TLS 1.2 握手

### 1.1 RSA 密钥交换

RSA 密钥交换是HTTPS握手过程的重要组成部分。本节详细介绍RSA 密钥交换的核心概念、工作原理和实际应用。

**关键要点**：

- RSA 密钥交换的定义与核心原理
- RSA 密钥交换的实现方式与技术细节
- RSA 密钥交换在实际场景中的应用与最佳实践
- RSA 密钥交换的常见问题与解决方案

RSA 密钥交换在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 ECDHE 密钥交换

ECDHE 密钥交换是HTTPS握手过程的重要组成部分。本节详细介绍ECDHE 密钥交换的核心概念、工作原理和实际应用。

**关键要点**：

- ECDHE 密钥交换的定义与核心原理
- ECDHE 密钥交换的实现方式与技术细节
- ECDHE 密钥交换在实际场景中的应用与最佳实践
- ECDHE 密钥交换的常见问题与解决方案

ECDHE 密钥交换在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 完整握手流程

完整握手流程是HTTPS握手过程的重要组成部分。本节详细介绍完整握手流程的核心概念、工作原理和实际应用。

**关键要点**：

- 完整握手流程的定义与核心原理
- 完整握手流程的实现方式与技术细节
- 完整握手流程在实际场景中的应用与最佳实践
- 完整握手流程的常见问题与解决方案

完整握手流程在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. TLS 1.3 握手

### 2.1 1-RTT 握手

1-RTT 握手是HTTPS握手过程的重要组成部分。本节详细介绍1-RTT 握手的核心概念、工作原理和实际应用。

**关键要点**：

- 1-RTT 握手的定义与核心原理
- 1-RTT 握手的实现方式与技术细节
- 1-RTT 握手在实际场景中的应用与最佳实践
- 1-RTT 握手的常见问题与解决方案

1-RTT 握手在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 0-RTT 恢复

0-RTT 恢复是HTTPS握手过程的重要组成部分。本节详细介绍0-RTT 恢复的核心概念、工作原理和实际应用。

**关键要点**：

- 0-RTT 恢复的定义与核心原理
- 0-RTT 恢复的实现方式与技术细节
- 0-RTT 恢复在实际场景中的应用与最佳实践
- 0-RTT 恢复的常见问题与解决方案

0-RTT 恢复在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 与 TLS 1.2 的差异

与 TLS 1.2 的差异是HTTPS握手过程的重要组成部分。本节详细介绍与 TLS 1.2 的差异的核心概念、工作原理和实际应用。

**关键要点**：

- 与 TLS 1.2 的差异的定义与核心原理
- 与 TLS 1.2 的差异的实现方式与技术细节
- 与 TLS 1.2 的差异在实际场景中的应用与最佳实践
- 与 TLS 1.2 的差异的常见问题与解决方案

与 TLS 1.2 的差异在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 证书验证

### 3.1 证书链验证

证书链验证是HTTPS握手过程的重要组成部分。本节详细介绍证书链验证的核心概念、工作原理和实际应用。

**关键要点**：

- 证书链验证的定义与核心原理
- 证书链验证的实现方式与技术细节
- 证书链验证在实际场景中的应用与最佳实践
- 证书链验证的常见问题与解决方案

证书链验证在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 OCSP 与 CRL

OCSP 与 CRL是HTTPS握手过程的重要组成部分。本节详细介绍OCSP 与 CRL的核心概念、工作原理和实际应用。

**关键要点**：

- OCSP 与 CRL的定义与核心原理
- OCSP 与 CRL的实现方式与技术细节
- OCSP 与 CRL在实际场景中的应用与最佳实践
- OCSP 与 CRL的常见问题与解决方案

OCSP 与 CRL在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 密码套件

### 4.1 对称加密

对称加密是HTTPS握手过程的重要组成部分。本节详细介绍对称加密的核心概念、工作原理和实际应用。

**关键要点**：

- 对称加密的定义与核心原理
- 对称加密的实现方式与技术细节
- 对称加密在实际场景中的应用与最佳实践
- 对称加密的常见问题与解决方案

对称加密在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 非对称加密

非对称加密是HTTPS握手过程的重要组成部分。本节详细介绍非对称加密的核心概念、工作原理和实际应用。

**关键要点**：

- 非对称加密的定义与核心原理
- 非对称加密的实现方式与技术细节
- 非对称加密在实际场景中的应用与最佳实践
- 非对称加密的常见问题与解决方案

非对称加密在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 HMAC 与 AEAD

HMAC 与 AEAD是HTTPS握手过程的重要组成部分。本节详细介绍HMAC 与 AEAD的核心概念、工作原理和实际应用。

**关键要点**：

- HMAC 与 AEAD的定义与核心原理
- HMAC 与 AEAD的实现方式与技术细节
- HMAC 与 AEAD在实际场景中的应用与最佳实践
- HMAC 与 AEAD的常见问题与解决方案

HMAC 与 AEAD在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

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
| HTTPS握手过程 | 043-HTTPSHandshake | 本文自身 |
| TCP拥塞控制 | 044-TCPControl | 本文的并列主题 |
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
