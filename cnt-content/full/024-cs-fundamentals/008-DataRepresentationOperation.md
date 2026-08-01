---
order: 52
title: 数据表示与运算
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: intermediate
description: 数据表示与运算：数值编码、浮点标准、定点运算、溢出检测与校验码
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/离散数学'
  - 'cs-fundamentals/计算机组成原理'
  - 'cs-fundamentals/指令流水线'
  - 'cs-fundamentals/存储系统'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 数值编码

### 1.1 原码

最高位为符号位（0正1负），其余位为绝对值：

$$[X]_{\text{原}} = \begin{cases} X & 0 \leq X < 2^{n-1} \\ 2^{n-1} + |X| & -2^{n-1} < X \leq 0 \end{cases}$$

8 位原码范围：$-127 \sim +127$，0 有两种表示（+0 和 -0）。

### 1.2 反码

正数与原码相同，负数符号位为1，数值位按位取反：

$$[X]_{\text{反}} = \begin{cases} X & X \geq 0 \\ 2^n - 1 + X & X < 0 \end{cases}$$

### 1.3 补码

计算机中最常用的整数表示法：

$$[X]_{\text{补}} = \begin{cases} X & X \geq 0 \\ 2^n + X & X < 0 \end{cases}$$

**关键性质**：

- 补码 = 反码 + 1（负数）
- 0 的补码唯一
- $n$ 位补码范围：$-2^{n-1} \sim 2^{n-1}-1$
- 补码加减法统一为加法

**快速求补码**：从最低位到第一个1保持不变，其余位取反。

### 1.4 移码

补码的符号位取反，用于浮点数的阶码表示：

$$[X]_{\text{移}} = 2^{n-1} + X$$

移码保持了数值的大小顺序，便于比较大小。

## 2. 定点运算

### 2.1 补码加法

$$[X+Y]_{\text{补}} = [X]_{\text{补}} + [Y]_{\text{补}}$$

符号位参与运算，进位自然丢弃。

### 2.2 补码减法

$$[X-Y]_{\text{补}} = [X]_{\text{补}} + [-Y]_{\text{补}}$$

其中 $[-Y]_{\text{补}}$ 为 $[Y]_{\text{补}}$ 的各位取反加1。

### 2.3 溢出检测

**单符号位法**：

$$V = A_s \oplus B_s \oplus S_s$$

- $V = 0$：无溢出
- $V = 1$：溢出

**双符号位法（变形补码）**：

- $S_{s1}S_{s2} = 00$：结果为正，无溢出
- $S_{s1}S_{s2} = 01$：正溢出
- $S_{s1}S_{s2} = 10$：负溢出
- $S_{s1}S_{s2} = 11$：结果为负，无溢出

### 2.4 定点乘法

**原码一位乘法**：

- 符号位单独处理：$P_s = A_s \oplus B_s$
- 数值部分：被乘数加或不加（根据乘数位），然后右移

**补码一位乘法（Booth 算法）**：

根据乘数末两位的差值决定操作：

| $Y_i$ | $Y_{i-1}$ | 操作                            |
| ----- | --------- | ------------------------------- |
| 0     | 0         | 右移一位                        |
| 0     | 1         | 加 $[X]_{\text{补}}$，右移一位  |
| 1     | 0         | 加 $[-X]_{\text{补}}$，右移一位 |
| 1     | 1         | 右移一位                        |

## 3. 浮点数表示

### 3.1 IEEE 754 标准

浮点数格式：

$$(-1)^S \times 1.M \times 2^{E-\text{bias}}$$

| 参数       | 单精度（32位）          | 双精度（64位）            |
| ---------- | ----------------------- | ------------------------- |
| 符号位 S   | 1 位                    | 1 位                      |
| 阶码 E     | 8 位                    | 11 位                     |
| 尾数 M     | 23 位                   | 52 位                     |
| 偏置值     | 127                     | 1023                      |
| 阶码范围   | 1~254                   | 1~2046                    |
| 规格化范围 | $2^{-126} \sim 2^{127}$ | $2^{-1022} \sim 2^{1023}$ |

### 3.2 特殊值

| 阶码 E | 尾数 M | 含义       |
| ------ | ------ | ---------- |
| 全0    | 全0    | ±0         |
| 全0    | 非零   | 非规格化数 |
| 全1    | 全0    | ±∞         |
| 全1    | 非零   | NaN        |

### 3.3 非规格化数

当阶码全0、尾数非零时，表示非规格化数：

$$(-1)^S \times 0.M \times 2^{1-\text{bias}}$$

非规格化数填补了0和最小规格化数之间的间隙，实现**渐进下溢**。

### 3.4 浮点精度

单精度有效位数约 7 位十进制，双精度约 15~16 位十进制。

**机器 epsilon**：

$$\epsilon_{\text{single}} = 2^{-23} \approx 1.19 \times 10^{-7}$$

$$\epsilon_{\text{double}} = 2^{-52} \approx 2.22 \times 10^{-16}$$

## 4. 浮点运算

### 4.1 浮点加减法

1. **对阶**：小阶向大阶看齐，尾数右移
2. **尾数加减**：对阶后的尾数相加减
3. **规格化**：左规或右规使尾数满足 $1.M$ 格式
4. **舍入**：按舍入模式处理超出位
5. **溢出判断**：检查阶码是否溢出

### 4.2 舍入模式

| 模式     | 说明                           |
| -------- | ------------------------------ |
| 就近舍入 | 舍入到最接近的可表示值（默认） |
| 向0舍入  | 截断                           |
| 向+∞舍入 | 向上取整                       |
| 向-∞舍入 | 向下取整                       |

就近舍入的"银行家舍入"规则：当恰好在中间时，舍入到偶数。

### 4.3 浮点乘除法

**乘法**：

$$(-1)^{S_1 \oplus S_2} \times (1.M_1 \times 1.M_2) \times 2^{(E_1+E_2-\text{bias})}$$

**除法**：

$$(-1)^{S_1 \oplus S_2} \times (1.M_1 \div 1.M_2) \times 2^{(E_1-E_2+\text{bias})}$$

## 5. 校验码

### 5.1 奇偶校验

在数据位后添加1位校验位，使1的个数为奇数（奇校验）或偶数（偶校验）。

- 只能检测奇数个错误
- 不能纠正错误
- 检错率：$1 - 2^{-n}$（对于 $n$ 位数据）

### 5.2 海明码（Hamming Code）

在数据位之间插入 $r$ 个校验位，满足：

$$2^r \geq m + r + 1$$

其中 $m$ 为数据位数，$r$ 为校验位数。

**校验位位置**：放在 $2^i$ 的位置（第1、2、4、8...位）。

**编码步骤**：

1. 确定校验位数 $r$
2. 将数据位填入非 $2^i$ 位置
3. 每个校验位覆盖其位置二进制表示中对应位为1的所有位
4. 计算各校验位的值

**纠错能力**：SEC-DED（单纠错双检错）

### 5.3 CRC 循环冗余校验

将数据视为多项式，用生成多项式除取余数作为校验码。

**编码过程**：

1. 数据 $M(x)$ 左移 $r$ 位（$r$ 为生成多项式阶数）
2. 用生成多项式 $G(x)$ 模2除法取余数 $R(x)$
3. 发送 $M(x) \cdot x^r + R(x)$

**检错能力**：

- 所有单比特错误
- 所有双比特错误（生成多项式包含 $(x+1)$ 因子时）
- 所有奇数个比特错误
- 所有长度 $\leq r$ 的突发错误

### 5.4 校验码对比

| 校验码   | 冗余位                      | 检错能力 | 纠错能力         | 应用        |
| -------- | --------------------------- | -------- | ---------------- | ----------- |
| 奇偶校验 | 1位                         | 奇数个错 | 无               | 内存ECC基础 |
| 海明码   | $\lceil\log_2(m+r+1)\rceil$ | 2位错    | 1位错            | ECC内存     |
| CRC      | $r$位                       | 突发错误 | 无（可配合重传） | 网络通信    |

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
| 数据表示与运算 | 008-DataRepresentationOperation | 本文自身 |
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
