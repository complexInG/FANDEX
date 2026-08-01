---
order: 54
title: 存储系统
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: advanced
description: 存储系统深度：Cache优化、虚拟存储、TLB、内存管理与存储一致性
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/数据表示与运算'
  - 'cs-fundamentals/指令流水线'
  - 'cs-fundamentals/总线与接口'
  - 'cs-fundamentals/并行计算'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 存储层次原理

### 1.1 局部性原理

**时间局部性**：最近访问的数据很可能在不久后再次被访问。

**空间局部性**：最近访问数据附近的数据很可能即将被访问。

局部性是存储层次有效性的理论基础。

### 1.2 存储层次设计目标

$$\text{目标：以最低成本获得接近最快存储的访问速度}$$

$$t_{effective} = \sum_{i=1}^{n} h_i \times t_i$$

其中 $h_i$ 为第 $i$ 层的命中率，$t_i$ 为第 $i$ 层的访问时间。

## 2. Cache 优化技术

### 2.1 降低缺失率

**更大块大小**：利用空间局部性，但块过大会增加缺失代价。

**更大 Cache 容量**：直接降低缺失率，但增加命中时间和功耗。

**更高相联度**：降低冲突缺失，但增加命中时间。

| 相联度    | 强制缺失 | 容量缺失 | 冲突缺失 | 命中时间 |
| --------- | -------- | -------- | -------- | -------- |
| 直接映射  | 不变     | 不变     | 最多     | 最短     |
| 2路组相联 | 不变     | 不变     | 较少     | 略长     |
| 4路组相联 | 不变     | 不变     | 很少     | 较长     |
| 全相联    | 不变     | 不变     | 无       | 最长     |

**3C 模型**：

$$\text{缺失率} = \text{强制缺失} + \text{容量缺失} + \text{冲突缺失}$$

### 2.2 降低缺失代价

**多级 Cache**：

$$t_{miss} = t_{L2\_hit} + (1-h_{L2}) \times t_{L2\_miss}$$

**关键字优先（Critical Word First）**：缺失时优先加载所需字，其余部分后台加载。

**读缺失优先于写**：写缓冲可能导致读缺失读到过时数据。

### 2.3 降低命中时间

**小而简单的 Cache**：L1 Cache 保持小容量、低相联度。

**流水线化 Cache 访问**：将 Cache 访问拆分为多个流水线级。

**路预测**：预测可能命中的路，只访问该路。

### 2.4 Cache 替换策略

**LRU（最近最少使用）**：替换最久未访问的行。

- 2路：1 bit 计数器
- 4路：需要更复杂的计数器
- 相联度高时开销大

**伪 LRU（PLRU）**：近似 LRU，用树形结构记录访问信息。

**随机替换**：简单，在某些情况下性能接近 LRU。

### 2.5 Cache 预取

**硬件预取**：

- 顺序预取：检测到顺序访问模式时预取下一行
- 跨步预取：检测固定跨步访问模式

**软件预取**：

```c
// 使用预取指令
__builtin_prefetch(addr, rw, locality);
```

预取有效性条件：

$$t_{prefetch} < t_{miss} \quad \text{且} \quad \text{预取准确率足够高}$$

## 3. 虚拟存储

### 3.1 虚拟地址与物理地址

虚拟地址空间由 CPU 生成，物理地址空间对应实际内存：

$$\text{物理地址} = f(\text{虚拟地址}, \text{页表})$$

32 位系统：虚拟地址空间 4GB
64 位系统：虚拟地址空间 $2^{48}$ 或 $2^{57}$（实际实现）

### 3.2 页式存储

**页表映射**：

$$\text{物理页号} = \text{页表}[\text{虚拟页号}]$$

$$\text{物理地址} = \text{物理页号} \times \text{页大小} + \text{页内偏移}$$

**页表项（PTE）结构**：

```mermaid
flowchart LR
    V[有效位] --- RW[读写位] --- U[用户位] --- D[脏位] --- A[访问位] --- P[物理页号]
```

### 3.3 多级页表

32 位地址，4KB 页，4B PTE：

- 单级页表：$2^{20}$ 项 × 4B = 4MB（每个进程）
- 二级页表：仅映射已使用的虚拟地址范围

64 位系统通常使用四级页表：

```
虚拟地址：[PGD索引 | PUD索引 | PMD索引 | PTE索引 | 偏移]
```

Linux 的四级页表：PGD → PUD → PMD → PTE → 物理页

### 3.4 反置页表

按物理页号索引而非虚拟页号：

$$\text{哈希表}[\text{虚拟页号} \oplus \text{PID}] \to \text{物理页号}$$

优势：页表大小与物理内存成正比，与虚拟地址空间无关。

## 4. TLB

### 4.1 TLB 原理

TLB（Translation Lookaside Buffer）是页表的高速缓存：

```
虚拟地址 → TLB 查找 → 命中 → 物理地址
                  → 缺失 → 页表查找 → 填充 TLB → 物理地址
```

### 4.2 TLB 结构

典型 TLB 参数：

| 参数     | 典型值         |
| -------- | -------------- |
| TLB 项数 | 64~512         |
| 相联度   | 全相联或高相联 |
| 页大小   | 4KB~2MB        |
| 命中率   | >99%           |
| 命中时间 | 1 周期         |
| 缺失代价 | 20~100 周期    |

### 4.3 TLB 与 Cache 的交互

**物理索引物理标记（PIPT）**：

- Cache 使用物理地址索引和标记
- TLB 必须先完成翻译
- 命中时间较长

**虚拟索引物理标记（VIPT）**：

- Cache 索引使用虚拟地址低位（与物理地址相同）
- Cache 标记使用物理地址
- TLB 翻译和 Cache 索引可并行

$$\text{索引位数} \leq \log_2(\text{页大小}) - \log_2(\text{块大小})$$

### 4.4 超大页（Huge Pages）

标准 4KB 页导致 TLB 覆盖范围有限：

$$\text{TLB 覆盖} = \text{TLB 项数} \times \text{页大小}$$

64 项 × 4KB = 256KB，远不够大工作集。

**解决方案**：使用 2MB 或 1GB 大页。

$$64 \times 2\text{MB} = 128\text{MB}$$

Linux 透明大页（THP）自动将连续的 4KB 页合并为 2MB 大页。

## 5. 内存管理

### 5.1 页面置换算法

**最优置换（OPT）**：置换未来最久不被访问的页，理论最优但不可实现。

**FIFO**：置换最早进入内存的页，简单但性能差，存在 Belady 异常。

**LRU**：置换最近最久未访问的页，性能好但实现开销大。

**Clock 算法**：LRU 的近似实现，使用访问位和循环指针。

**改进型 Clock 算法**：同时考虑访问位和脏位：

| 优先级 | 访问位 | 脏位 | 说明           |
| ------ | ------ | ---- | -------------- |
| 1      | 0      | 0    | 最佳替换目标   |
| 2      | 0      | 1    | 未访问但已修改 |
| 3      | 1      | 0    | 已访问未修改   |
| 4      | 1      | 1    | 最差替换目标   |

### 5.2 工作集模型

进程的工作集 $W(t, \Delta)$ 是在时刻 $t$ 之前的 $\Delta$ 个时间单位内被访问的页面集合。

$$\text{工作集大小} = |W(t, \Delta)|$$

**抖动（Thrashing）**：当分配给进程的物理页数小于工作集大小时，频繁发生页面置换。

### 5.3 页面分配策略

- **全局置换**：所有进程共享物理页池，可从其他进程夺取页面
- **局部置换**：每个进程有固定数量的物理页

## 6. 存储一致性

### 6.1 Cache 一致性问题

多核系统中，每个核心有自己的私有 Cache，同一内存块可能在不同 Cache 中有不同副本。

### 6.2 监听协议（Snooping）

**MSI 协议**：

| 状态          | 说明                                  |
| ------------- | ------------------------------------- |
| M（Modified） | 仅本 Cache 有最新数据，与内存不一致   |
| S（Shared）   | 多个 Cache 可能有相同数据，与内存一致 |
| I（Invalid）  | 无效                                  |

**MESI 协议**（Intel 使用）：

| 状态           | 说明         |
| -------------- | ------------ |
| M（Modified）  | 已修改，独占 |
| E（Exclusive） | 未修改，独占 |
| S（Shared）    | 共享         |
| I（Invalid）   | 无效         |

E 状态优化：当只有一个 Cache 拥有该行且未修改时，无需总线广播即可写入。

**MOESI 协议**（AMD 使用）：增加 O（Owner）状态，允许共享脏行。

### 6.3 目录协议（Directory）

适用于大规模多核系统，用目录记录每个缓存行的共享信息：

$$\text{目录项} = \text{脏位} + \text{共享向量}[N]$$

其中 $N$ 为处理器数量。

**目录协议的扩展性**：

- 全映射目录：$O(N)$ 空间/行
- 有限目录：$O(\log N)$ 空间/行
- 链式目录：动态分配空间

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
| 存储系统 | 010-StorageSystem | 本文自身 |
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
| 词法分析 | 052-LexicalAnalysis | 本文的并列主题 |
| 语法分析 | 053-GrammarAnalysis | 本文的并列主题 |
| 语义分析 | 054-SemanticAnalysis | 本文的并列主题 |
| 中间代码 | 055-IntermediateCode | 本文的并列主题 |
| 代码优化 | 056-CodeOptimization | 本文的性能延伸 |
| 目标代码生成 | 057-TargetCodeGeneration | 本文的并列主题 |
