---
order: 72
title: 编程语言理论
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: advanced
description: 编程语言理论：类型系统、Lambda演算、语义学与程序验证
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/软件体系结构'
  - 'cs-fundamentals/人机交互'
  - 'cs-fundamentals/网络协议深度'
  - 'cs-fundamentals/编译与运行时'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 类型系统

### 1.1 类型系统分类

| 维度         | 分类      | 说明               |
| ------------ | --------- | ------------------ |
| 类型检查时机 | 静态/动态 | 编译时/运行时      |
| 类型转换     | 强/弱     | 隐式转换的严格程度 |
| 类型推断     | 显式/隐式 | 是否需要声明类型   |

### 1.2 静态类型系统

**Hindley-Milner 类型推断**：

自动推断表达式的最一般类型：

$$\text{算法W}(\Gamma, e) = (S, \tau)$$

其中 $\Gamma$ 为类型环境，$S$ 为替换，$\tau$ 为类型。

**多态类型**：

$$id : \forall \alpha. \alpha \to \alpha$$

**Let 多态**：

```
let id = λx.x in (id 1, id true)  -- 合法
```

而：

```
(λid.(id 1, id true))(λx.x)  -- 不合法（ML中）
```

### 1.3 子类型

**子类型关系** $S <: T$ 表示 $S$ 类型的值可以用在期望 $T$ 类型的地方。

**函数子类型的协变与逆变**：

- 参数类型：逆变（contravariant）
- 返回类型：协变（covariant）

$$S_1 \to S_2 <: T_1 \to T_2 \iff T_1 <: S_1 \wedge S_2 <: T_2$$

**Liskov 替换原则（LSP）**：

若 $S <: T$，则 $T$ 类型的对象可被 $S$ 类型的对象替换，程序行为不变。

### 1.4 代数数据类型

**积类型（Product）**：

$$A \times B = \{(a, b) \mid a \in A, b \in B\}$$

**和类型（Sum）**：

$$A + B = \text{inl}(a) \mid \text{inr}(b)$$

**类型同构**：

| 类型表达式       | 等价于           |
| ---------------- | ---------------- |
| $A \times 1$     | $A$              |
| $A + 0$          | $A$              |
| $A \times B$     | $B \times A$     |
| $A + B$          | $B + A$          |
| $A^{B+C}$        | $A^B \times A^C$ |
| $(A \times B)^C$ | $A^C \times B^C$ |

## 2. Lambda 演算

### 2.1 无类型 Lambda 演算

**语法**：

$$e ::= x \mid \lambda x.e \mid e_1\ e_2$$

**β 归约**：

$$(\lambda x.e_1)\ e_2 \to e_1[x := e_2]$$

**α 转换**：

$$\lambda x.e \equiv_\alpha \lambda y.e[x := y]$$

**η 归约**：

$$\lambda x.(f\ x) \to_\eta f \quad (x \notin FV(f))$$

### 2.2 归约策略

| 策略     | 说明           | 特点           |
| -------- | -------------- | -------------- |
| 正则序   | 最左最外先归约 | 可能重复计算   |
| 应用序   | 最左最内先归约 | 可能不终止     |
| 惰性求值 | 仅在需要时归约 | 避免不必要计算 |
| 急切求值 | 参数先求值     | 实用           |

### 2.3 Church 编码

**Church 布尔值**：

$$\text{true} = \lambda t.\lambda f.t$$

$$\text{false} = \lambda t.\lambda f.f$$

**Church 数**：

$$0 = \lambda f.\lambda x.x$$

$$1 = \lambda f.\lambda x.f\ x$$

$$2 = \lambda f.\lambda x.f\ (f\ x)$$

$$n = \lambda f.\lambda x.f^n\ x$$

**后继**：

$$\text{succ} = \lambda n.\lambda f.\lambda x.f\ (n\ f\ x)$$

**加法**：

$$\text{plus} = \lambda m.\lambda n.\lambda f.\lambda x.m\ f\ (n\ f\ x)$$

### 2.4 Y 组合子

实现不动点，允许递归：

$$Y = \lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))$$

$$Y\ f = f\ (Y\ f)$$

### 2.5 简单类型 Lambda 演算（STLC）

**类型语法**：

$$\tau ::= B \mid \tau_1 \to \tau_2$$

**类型规则**：

$$\frac{x:\tau \in \Gamma}{\Gamma \vdash x : \tau} \text{ (Var)}$$

$$\frac{\Gamma, x:\tau_1 \vdash e : \tau_2}{\Gamma \vdash \lambda x:\tau_1.e : \tau_1 \to \tau_2} \text{ (Abs)}$$

$$\frac{\Gamma \vdash e_1 : \tau_1 \to \tau_2 \quad \Gamma \vdash e_2 : \tau_1}{\Gamma \vdash e_1\ e_2 : \tau_2} \text{ (App)}$$

**类型安全 = 进展性 + 保持性**：

- 进展性：良类型的闭项要么是值，要么可以归约
- 保持性：归约保持类型不变

## 3. 操作语义

### 3.1 小步语义

定义单步归约关系 $\to$：

$$\frac{e_1 \to e_1'}{e_1\ e_2 \to e_1'\ e_2}$$

$$\frac{v_1\ e_2 \to v_1\ e_2'}{e_2 \to e_2'}$$

$$\frac{}{(\lambda x.e)\ v \to e[x := v]}$$

### 3.2 大步语义

定义求值关系 $\Downarrow$：

$$\frac{e_1 \Downarrow \lambda x.e \quad e_2 \Downarrow v_2 \quad e[x:=v_2] \Downarrow v}{e_1\ e_2 \Downarrow v}$$

### 3.3 小步 vs 大步

| 特性   | 小步语义 | 大步语义   |
| ------ | -------- | ---------- |
| 粒度   | 单步归约 | 直接到结果 |
| 非终止 | 可描述   | 无法描述   |
| 并发   | 适合     | 不适合     |
| 证明   | 归纳简单 | 可能更直观 |

## 4. 指称语义

### 4.1 基本思想

将程序映射到数学对象（域论中的元素）：

$$\llbracket e \rrbracket : \text{Env} \to \text{Value}$$

### 4.2 语义函数

$$\llbracket x \rrbracket \rho = \rho(x)$$

$$\llbracket \lambda x.e \rrbracket \rho = \lambda v.\llbracket e \rrbracket \rho[x \mapsto v]$$

$$\llbracket e_1\ e_2 \rrbracket \rho = (\llbracket e_1 \rrbracket \rho)(\llbracket e_2 \rrbracket \rho)$$

### 4.3 不动点语义

递归定义的语义通过域论中的最小不动点给出：

$$\llbracket \text{fix} \rrbracket = \text{lfp}(F) = \bigsqcup_{n=0}^{\infty} F^n(\bot)$$

## 5. 程序验证

### 5.1 Hoare 逻辑

**Hoare 三元组**：

$$\{P\}\ C\ \{Q\}$$

含义：若前置条件 $P$ 成立，执行命令 $C$ 后，后置条件 $Q$ 成立。

**推理规则**：

$$\frac{}{\{P\}\ \text{skip}\ \{P\}}$$

$$\frac{}{\{Q[x:=e]\}\ x := e\ \{Q\}}$$

$$\frac{\{P\}\ C_1\ \{R\} \quad \{R\}\ C_2\ \{Q\}}{\{P\}\ C_1;C_2\ \{Q\}}$$

$$\frac{\{P \wedge b\}\ C_1\ \{Q\} \quad \{P \wedge \neg b\}\ C_2\ \{Q\}}{\{P\}\ \text{if } b \text{ then } C_1 \text{ else } C_2\ \{Q\}}$$

$$\frac{\{P \wedge b\}\ C\ \{P\}}{\{P\}\ \text{while } b \text{ do } C\ \{P \wedge \neg b\}}$$

### 5.2 循环不变式

循环不变式 $I$ 必须满足：

1. **初始化**：循环开始前 $I$ 成立
2. **保持**：每次迭代后 $I$ 仍然成立
3. **终止**：循环结束时 $I \wedge \neg b$ 可推出 $Q$

### 5.3 最弱前置条件

$$\text{wp}(x := e, Q) = Q[x := e]$$

$$\text{wp}(C_1; C_2, Q) = \text{wp}(C_1, \text{wp}(C_2, Q))$$

$$\text{wp}(\text{if } b \text{ then } C_1 \text{ else } C_2, Q) = (b \Rightarrow \text{wp}(C_1, Q)) \wedge (\neg b \Rightarrow \text{wp}(C_2, Q))$$

### 5.4 类型系统与验证

类型系统是一种轻量级程序验证：

| 验证级别 | 方法     | 保证       |
| -------- | -------- | ---------- |
| 类型检查 | 编译器   | 类型安全   |
| 静态分析 | 分析工具 | 特定属性   |
| 程序证明 | 证明助手 | 完全正确性 |

**依赖类型**：类型可以依赖于值，允许在类型层面表达更精细的属性。

$$\text{Vec}(A, n) : \text{Type}$$

长度为 $n$ 的 $A$ 类型向量，类型检查器可验证列表操作的正确性。

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
| 编程语言理论 | 030-ProgrammingLanguageTheory | 本文自身 |
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
