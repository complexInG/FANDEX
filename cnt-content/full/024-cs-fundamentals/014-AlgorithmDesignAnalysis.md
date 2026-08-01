---
order: 58
title: 算法设计与分析
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: advanced
description: 算法设计与分析：分治、贪心、动态规划、回溯、分支限界与NP理论
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/并行计算'
  - 'cs-fundamentals/分布式系统'
  - 'cs-fundamentals/形式语言与自动机'
  - 'cs-fundamentals/信息安全基础'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 算法分析基础

### 1.1 渐近记号

**大O记号**：上界

$$f(n) = O(g(n)) \iff \exists c > 0, n_0 > 0, \forall n \geq n_0: f(n) \leq c \cdot g(n)$$

**Ω记号**：下界

$$f(n) = \Omega(g(n)) \iff \exists c > 0, n_0 > 0, \forall n \geq n_0: f(n) \geq c \cdot g(n)$$

**Θ记号**：紧界

$$f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \wedge f(n) = \Omega(g(n))$$

### 1.2 常见复杂度类

| 复杂度        | 名称     | 示例       |
| ------------- | -------- | ---------- |
| $O(1)$        | 常数     | 哈希表查找 |
| $O(\log n)$   | 对数     | 二分查找   |
| $O(n)$        | 线性     | 遍历数组   |
| $O(n \log n)$ | 线性对数 | 归并排序   |
| $O(n^2)$      | 平方     | 冒泡排序   |
| $O(2^n)$      | 指数     | 子集枚举   |
| $O(n!)$       | 阶乘     | 全排列     |

### 1.3 递推关系求解

**主定理（Master Theorem）**：

$$T(n) = aT(n/b) + f(n)$$

| 情况 | 条件                                     | 结果                                       |
| ---- | ---------------------------------------- | ------------------------------------------ |
| 1    | $f(n) = O(n^{\log_b a - \epsilon})$      | $T(n) = \Theta(n^{\log_b a})$              |
| 2    | $f(n) = \Theta(n^{\log_b a} \log^k n)$   | $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$ |
| 3    | $f(n) = \Omega(n^{\log_b a + \epsilon})$ | $T(n) = \Theta(f(n))$                      |

## 2. 分治法

### 2.1 基本思想

将问题分解为若干子问题，递归求解后合并：

```
Divide: 将问题分解为子问题
Conquer: 递归求解子问题
Combine: 合并子问题的解
```

### 2.2 经典分治算法

**归并排序**：

$$T(n) = 2T(n/2) + O(n) = O(n \log n)$$

**快速排序**：

- 平均：$O(n \log n)$
- 最坏：$O(n^2)$（已排序输入 + 固定主元选择）
- 随机化后期望：$O(n \log n)$

**最近点对**：

$$T(n) = 2T(n/2) + O(n) = O(n \log n)$$

**Strassen 矩阵乘法**：

$$T(n) = 7T(n/2) + O(n^2) = O(n^{\log_2 7}) \approx O(n^{2.807})$$

## 3. 贪心算法

### 3.1 贪心选择性质

局部最优选择能导致全局最优解。

### 3.2 经典贪心算法

**活动选择问题**：选择最多不重叠活动。

策略：按结束时间排序，贪心选择最早结束的活动。

**Huffman 编码**：

- 构建最优前缀码
- 每次合并频率最低的两个节点
- 时间复杂度：$O(n \log n)$

**最小生成树**：

Kruskal 算法：按边权排序，用并查集判断是否形成环。$O(E \log E)$

Prim 算法：从任一顶点出发，每次选最短边扩展。$O(E \log V)$（优先队列）

**Dijkstra 最短路径**：

$$T = O((V + E) \log V)$$

限制：不能有负权边。

### 3.3 贪心正确性证明

**交换论证法**：

1. 假设存在最优解 $O$ 与贪心解 $G$ 不同
2. 找到第一个不同的选择
3. 证明将 $O$ 的选择替换为 $G$ 的选择不会变差
4. 反复替换，最终 $O$ 变为 $G$

## 4. 动态规划

### 4.1 基本要素

**最优子结构**：问题的最优解包含子问题的最优解。

**重叠子问题**：递归求解中大量子问题被重复计算。

### 4.2 设计步骤

1. 定义子问题（状态）
2. 建立状态转移方程
3. 确定计算顺序（拓扑序）
4. 确定边界条件
5. 可选：空间优化

### 4.3 经典动态规划问题

**0-1 背包**：

$$dp[i][w] = \max(dp[i-1][w], dp[i-1][w-w_i] + v_i)$$

时间：$O(nW)$，空间可优化至 $O(W)$。

**最长公共子序列（LCS）**：

$$dp[i][j] = \begin{cases} dp[i-1][j-1] + 1 & \text{if } s_1[i] = s_2[j] \\ \max(dp[i-1][j], dp[i][j-1]) & \text{otherwise} \end{cases}$$

**编辑距离**：

$$dp[i][j] = \min \begin{cases} dp[i-1][j] + 1 & \text{删除} \\ dp[i][j-1] + 1 & \text{插入} \\ dp[i-1][j-1] + \text{cost} & \text{替换} \end{cases}$$

**矩阵链乘法**：

$$dp[i][j] = \min_{i \leq k < j} \{dp[i][k] + dp[k+1][j] + p_{i-1} \cdot p_k \cdot p_j\}$$

### 4.4 状态空间优化

**滚动数组**：当状态转移只依赖前一行/列时，只保留两行。

**单调队列优化**：滑动窗口最大值问题。

**斜率优化**：决策单调性问题时，用凸包维护候选决策。

## 5. 回溯法

### 5.1 基本框架

```python
def backtrack(state, choices):
    if is_solution(state):
        record(state)
        return
    for choice in choices:
        if is_valid(state, choice):
            make_choice(state, choice)
            backtrack(state, next_choices)
            undo_choice(state, choice)
```

### 5.2 剪枝策略

**约束剪枝**：不满足约束条件时提前返回。

**限界剪枝**：当前解不可能优于已知最优解时返回。

### 5.3 经典回溯问题

**N皇后**：在 $n \times n$ 棋盘放置 $n$ 个互不攻击的皇后。

**子集和**：从集合中选取子集使和等于目标值。

**图着色**：用最少的颜色给图的顶点着色，相邻顶点颜色不同。

## 6. 分支限界法

### 6.1 与回溯法的区别

| 特性     | 回溯法    | 分支限界法        |
| -------- | --------- | ----------------- |
| 搜索方式 | 深度优先  | 广度优先/最佳优先 |
| 数据结构 | 栈        | 优先队列          |
| 目标     | 找所有解  | 找最优解          |
| 剪枝     | 约束+限界 | 限界为主          |

### 6.2 优先队列式分支限界

使用优先队列按限界值排序，优先扩展最有希望的节点。

**0-1 背包的分支限界**：

- 上界估计：剩余物品按单位价值贪心装入
- 每次取出上界最大的节点扩展

## 7. NP 理论

### 7.1 复杂度类

| 类    | 定义             | 示例           |
| ----- | ---------------- | -------------- |
| P     | 多项式时间可解   | 排序、最短路径 |
| NP    | 多项式时间可验证 | TSP、SAT       |
| NPC   | NP中最难的问题   | 3-SAT、Clique  |
| co-NP | NP的补           | 不可满足性     |

### 7.2 NP 完全性

**归约**：$A \leq_p B$ 表示问题 A 可在多项式时间内归约到问题 B。

**NP 完全问题**：

- 属于 NP
- 所有 NP 问题可归约到它

**Cook-Levin 定理**：SAT 是 NP 完全的。

### 7.3 常见 NP 完全问题

| 问题           | 描述                 |
| -------------- | -------------------- |
| SAT            | 布尔公式可满足性     |
| 3-SAT          | 3-CNF 公式可满足性   |
| Clique         | 图中是否存在 k-团    |
| Vertex Cover   | 最小顶点覆盖         |
| TSP            | 旅行商问题           |
| Subset Sum     | 子集和问题           |
| Knapsack       | 0-1 背包（弱NP完全） |
| Graph Coloring | 图着色问题           |

### 7.4 近似算法

对于 NP 难问题，寻找近似解：

**近似比**：

$$\rho = \max\left(\frac{\text{近似解}}{\text{最优解}}, \frac{\text{最优解}}{\text{近似解}}\right)$$

| 问题              | 近似比       | 算法         |
| ----------------- | ------------ | ------------ |
| 顶点覆盖          | 2            | 贪心匹配     |
| TSP（三角不等式） | 2            | MST + 匹配   |
| TSP（三角不等式） | 1.5          | Christofides |
| 背包              | $1+\epsilon$ | FPTAS        |
| 一般 TSP          | 无常数比     | 除非 P=NP    |

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
| 算法设计与分析 | 014-AlgorithmDesignAnalysis | 本文自身 |
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
