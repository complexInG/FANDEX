---
order: 50
title: 数字逻辑
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: intermediate
description: 数字逻辑基础：布尔代数、逻辑门、组合逻辑、时序逻辑与有限状态机
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/操作系统'
  - 'cs-fundamentals/计算机网络'
  - 'cs-fundamentals/离散数学'
  - 'cs-fundamentals/计算机组成原理'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 布尔代数基础

布尔代数是数字逻辑的数学基础，由 George Boole 于 1854 年提出，变量取值仅为 0 和 1。

### 1.1 基本运算

| 运算         | 符号                   | 真值表                           | 说明    |
| ------------ | ---------------------- | -------------------------------- | ------- |
| 与（AND）    | $A \cdot B$            | 0·0=0, 0·1=0, 1·0=0, 1·1=1       | 全1则1  |
| 或（OR）     | $A + B$                | 0+0=0, 0+1=1, 1+0=1, 1+1=1       | 有1则1  |
| 非（NOT）    | $\overline{A}$         | $\overline{0}=1, \overline{1}=0$ | 取反    |
| 异或（XOR）  | $A \oplus B$           | 0⊕0=0, 0⊕1=1, 1⊕0=1, 1⊕1=0       | 不同为1 |
| 与非（NAND） | $\overline{A \cdot B}$ | 与的非                           | 万能门  |
| 或非（NOR）  | $\overline{A + B}$     | 或的非                           | 万能门  |

### 1.2 布尔代数定律

**基本定律**：

- 交换律：$A + B = B + A$，$A \cdot B = B \cdot A$
- 结合律：$(A + B) + C = A + (B + C)$
- 分配律：$A \cdot (B + C) = A \cdot B + A \cdot C$
- 同一律：$A + 0 = A$，$A \cdot 1 = A$
- 补元律：$A + \overline{A} = 1$，$A \cdot \overline{A} = 0$

**德摩根定律（De Morgan's Law）**：

$$\overline{A \cdot B} = \overline{A} + \overline{B}$$

$$\overline{A + B} = \overline{A} \cdot \overline{B}$$

**吸收律**：

$$A + A \cdot B = A$$

$$A \cdot (A + B) = A$$

### 1.3 布尔函数化简

**卡诺图（Karnaugh Map）**：用于4变量以内的布尔函数化简。

2变量卡诺图：

```
        B=0  B=1
  A=0 |  m0 | m1 |
  A=1 |  m2 | m3 |
```

**奎因-麦克拉斯基法（Quine-McCluskey）**：适用于任意变量数的系统化化简方法。

## 2. 逻辑门电路

### 2.1 基本逻辑门

| 逻辑门 | 逻辑符号 | 布尔表达式                  | 国际符号 |
| ------ | -------- | --------------------------- | -------- |
| AND    | &        | $Y = A \cdot B$             | 与门     |
| OR     | ≥1       | $Y = A + B$                 | 或门     |
| NOT    | 1        | $Y = \overline{A}$          | 非门     |
| NAND   | &        | $Y = \overline{A \cdot B}$  | 与非门   |
| NOR    | ≥1       | $Y = \overline{A + B}$      | 或非门   |
| XOR    | =1       | $Y = A \oplus B$            | 异或门   |
| XNOR   | =1       | $Y = \overline{A \oplus B}$ | 同或门   |

### 2.2 万能门

NAND 和 NOR 门被称为万能门，因为仅用一种即可实现所有逻辑功能：

**用 NAND 实现 NOT**：

$$\overline{A} = \overline{A \cdot A}$$

**用 NAND 实现 AND**：

$$A \cdot B = \overline{\overline{A \cdot B}}$$

**用 NAND 实现 OR**：

$$A + B = \overline{\overline{A} \cdot \overline{B}}$$

### 2.3 传输延迟

逻辑门的输出不是瞬时变化的，存在传播延迟：

$$t_{pd} = \max(t_{pLH}, t_{pHL})$$

其中 $t_{pLH}$ 为低→高延迟，$t_{pHL}$ 为高→低延迟。

## 3. 组合逻辑电路

组合逻辑电路的输出仅取决于当前输入，无记忆功能。

### 3.1 编码器与译码器

**编码器**：将 $2^n$ 条输入线编码为 $n$ 位二进制输出。

**优先编码器**：允许多个输入同时有效，优先级最高的输入被编码。

**译码器**：将 $n$ 位二进制输入译码为 $2^n$ 条输出线中的一条。

```
3-8 译码器：
  输入：A2, A1, A0
  输出：Y0~Y7（仅一个为有效）
```

### 3.2 多路选择器（MUX）

从 $2^n$ 条输入中选择一条输出：

$$Y = \sum_{i=0}^{2^n-1} D_i \cdot m_i$$

其中 $m_i$ 为选择变量对应的最小项。

**用 MUX 实现任意逻辑函数**：$n$ 变量函数可用 $2^{n-1}$ 选 1 的 MUX 实现。

### 3.3 加法器

**半加器**：

$$S = A \oplus B, \quad C = A \cdot B$$

**全加器**：

$$S = A \oplus B \oplus C_{in}$$

$$C_{out} = A \cdot B + C_{in} \cdot (A \oplus B)$$

**行波进位加法器（RCA）**：$n$ 位加法器延迟为 $O(n)$。

**超前进位加法器（CLA）**：

生成函数：$G_i = A_i \cdot B_i$

传播函数：$P_i = A_i \oplus B_i$

$$C_{i+1} = G_i + P_i \cdot C_i$$

延迟为 $O(1)$（理想情况），但硬件复杂度随位数增加而急剧增大。

### 3.4 比较器

判断两个数的大小关系：

$$A > B, \quad A = B, \quad A < B$$

$n$ 位比较器从最高位开始逐位比较。

## 4. 时序逻辑电路

时序逻辑电路的输出不仅取决于当前输入，还与电路的历史状态有关。

### 4.1 锁存器与触发器

**SR 锁存器**：

| S   | R   | Q(n+1) | 说明 |
| --- | --- | ------ | ---- |
| 0   | 0   | Q(n)   | 保持 |
| 0   | 1   | 0      | 复位 |
| 1   | 0   | 1      | 置位 |
| 1   | 1   | ×      | 禁止 |

**D 触发器**：最常用的触发器，在时钟上升沿采样 D 输入：

$$Q(n+1) = D$$

**JK 触发器**：

| J   | K   | Q(n+1)            | 说明 |
| --- | --- | ----------------- | ---- |
| 0   | 0   | Q(n)              | 保持 |
| 0   | 1   | 0                 | 复位 |
| 1   | 0   | 1                 | 置位 |
| 1   | 1   | $\overline{Q(n)}$ | 翻转 |

**T 触发器**：

$$Q(n+1) = T \oplus Q(n)$$

### 4.2 寄存器与移位寄存器

- **寄存器**：由 $n$ 个 D 触发器组成，存储 $n$ 位数据
- **移位寄存器**：支持左移、右移操作
- **通用移位寄存器**：支持并行加载、左移、右移、保持

### 4.3 计数器

**同步计数器**：所有触发器共用同一时钟。

**异步计数器**：触发器时钟来自前一级输出，存在延迟累积。

**模 $N$ 计数器**：计数范围为 $0$ 到 $N-1$。

$n$ 位二进制计数器的模为 $2^n$。

## 5. 有限状态机（FSM）

### 5.1 Moore 型状态机

输出仅取决于当前状态：

$$\text{输出} = f(\text{当前状态})$$

### 5.2 Mealy 型状态机

输出取决于当前状态和当前输入：

$$\text{输出} = f(\text{当前状态}, \text{当前输入})$$

### 5.3 状态机设计步骤

1. 根据问题描述确定输入、输出和状态
2. 绘制状态转换图
3. 状态化简（消除等价状态）
4. 状态编码（二进制编码、独热编码等）
5. 求状态方程和输出方程
6. 画逻辑电路图

### 5.4 示例：序列检测器

检测输入序列中的 "101"：

```
状态定义：
  S0: 初始状态
  S1: 检测到 1
  S2: 检测到 10
  S3: 检测到 101（输出=1）

状态转换表：
  S0 --1--> S1  S0 --0--> S0
  S1 --0--> S2  S1 --1--> S1
  S2 --1--> S3  S2 --0--> S0
  S3 --1--> S1  S3 --0--> S2
```

## 6. 存储器结构

### 6.1 存储器分类

| 类型   | 特点         | 应用         |
| ------ | ------------ | ------------ |
| ROM    | 只读，非易失 | 固件、查找表 |
| PROM   | 一次可编程   | 小批量定制   |
| EPROM  | 紫外线可擦除 | 开发调试     |
| EEPROM | 电可擦除     | 配置参数     |
| Flash  | 块擦除       | SSD、U盘     |
| SRAM   | 静态，快速   | CPU缓存      |
| DRAM   | 动态，需刷新 | 主内存       |

### 6.2 存储器容量扩展

- **位扩展**：增加数据位宽（并联芯片）
- **字扩展**：增加地址空间（译码器选择芯片）
- **字位同时扩展**：两者结合

### 6.3 存储器访问时间

$$\text{访问时间} = t_{AA} \text{（地址到输出有效）}$$

$$\text{周期时间} \geq \text{访问时间} + \text{预充电时间}$$

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
| 数字逻辑 | 005-DigitalLogic | 本文自身 |
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
| 词法分析 | 052-LexicalAnalysis | 本文的并列主题 |
| 语法分析 | 053-GrammarAnalysis | 本文的并列主题 |
| 语义分析 | 054-SemanticAnalysis | 本文的并列主题 |
| 中间代码 | 055-IntermediateCode | 本文的并列主题 |
| 代码优化 | 056-CodeOptimization | 本文的性能延伸 |
| 目标代码生成 | 057-TargetCodeGeneration | 本文的并列主题 |
