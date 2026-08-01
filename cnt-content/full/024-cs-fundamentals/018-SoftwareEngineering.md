---
order: 61
title: 软件工程
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: intermediate
description: 软件工程：需求分析、设计模式、敏捷开发、测试策略与项目管理
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/信息安全基础'
  - 'cs-fundamentals/编译原理'
  - 'cs-fundamentals/数据库系统原理'
  - 'cs-fundamentals/编译原理进阶'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 软件工程概述

### 1.1 软件危机

1968年 NATO 会议提出"软件危机"概念：

- 软件项目经常超时、超预算
- 软件质量低劣、维护困难
- 缺乏系统化的开发方法

### 1.2 软件生命周期

```
需求分析 → 系统设计 → 详细设计 → 编码实现 → 测试 → 部署 → 维护
```

### 1.3 软件过程模型

| 模型     | 特点               | 适用场景       |
| -------- | ------------------ | -------------- |
| 瀑布模型 | 线性顺序，文档驱动 | 需求明确的项目 |
| 增量模型 | 分批交付，逐步完善 | 大型项目       |
| 螺旋模型 | 风险驱动，迭代     | 高风险项目     |
| 喷泉模型 | 面向对象，迭代     | OO项目         |
| 敏捷模型 | 快速迭代，拥抱变化 | 需求变化频繁   |

## 2. 需求工程

### 2.1 需求分类

- **功能需求**：系统应该做什么
- **非功能需求**：系统应该做到什么程度
  - 性能需求：响应时间、吞吐量
  - 安全需求：认证、授权、加密
  - 可靠性需求：MTBF、MTTR
  - 可用性需求：并发用户数

### 2.2 需求获取方法

| 方法 | 优点     | 缺点           |
| ---- | -------- | -------------- |
| 访谈 | 深入了解 | 耗时           |
| 问卷 | 覆盖面广 | 深度不足       |
| 观察 | 真实场景 | 受霍桑效应影响 |
| 原型 | 直观验证 | 可能偏离实际   |

### 2.3 用例建模

用例图要素：

- 参与者（Actor）：与系统交互的外部实体
- 用例（Use Case）：系统提供的功能
- 关系：包含（include）、扩展（extend）、泛化（generalization）

### 2.4 需求规格说明

SRS（Software Requirements Specification）应满足：

- 完整性：覆盖所有需求
- 一致性：需求之间不矛盾
- 可验证性：每条需求可测试
- 可追踪性：需求可追溯到来源

## 3. 软件设计

### 3.1 设计原则（SOLID）

| 原则            | 含义                       |
| --------------- | -------------------------- |
| 单一职责（SRP） | 一个类只有一个变化原因     |
| 开闭原则（OCP） | 对扩展开放，对修改关闭     |
| 里氏替换（LSP） | 子类可替换父类             |
| 接口隔离（ISP） | 客户端不应依赖不需要的接口 |
| 依赖反转（DIP） | 依赖抽象而非具体实现       |

### 3.2 设计模式分类

**创建型模式**：

| 模式                         | 意图                   |
| ---------------------------- | ---------------------- |
| 单例（Singleton）            | 确保类只有一个实例     |
| 工厂方法（Factory Method）   | 由子类决定创建哪个对象 |
| 抽象工厂（Abstract Factory） | 创建一族相关对象       |
| 建造者（Builder）            | 分步骤构建复杂对象     |
| 原型（Prototype）            | 通过克隆创建对象       |

**结构型模式**：

| 模式                | 意图             |
| ------------------- | ---------------- |
| 适配器（Adapter）   | 接口转换         |
| 桥接（Bridge）      | 分离抽象与实现   |
| 组合（Composite）   | 树形结构统一处理 |
| 装饰器（Decorator） | 动态添加职责     |
| 外观（Facade）      | 简化子系统接口   |
| 代理（Proxy）       | 控制对象访问     |

**行为型模式**：

| 模式                        | 意图           |
| --------------------------- | -------------- |
| 观察者（Observer）          | 一对多依赖通知 |
| 策略（Strategy）            | 算法族可互换   |
| 模板方法（Template Method） | 定义算法骨架   |
| 命令（Command）             | 请求参数化     |
| 迭代器（Iterator）          | 顺序访问集合   |
| 状态（State）               | 状态驱动行为   |

### 3.3 架构模式

| 模式     | 特点             | 适用场景   |
| -------- | ---------------- | ---------- |
| 分层架构 | 关注点分离       | 企业应用   |
| MVC      | 模型-视图-控制器 | Web应用    |
| 微服务   | 独立部署、松耦合 | 大型系统   |
| 事件驱动 | 异步消息通信     | 实时系统   |
| CQRS     | 读写分离         | 高并发系统 |

## 4. 敏捷开发

### 4.1 敏捷宣言

- **个体和互动** 高于 流程和工具
- **工作的软件** 高于 详尽的文档
- **客户合作** 高于 合同谈判
- **响应变化** 高于 遵循计划

### 4.2 Scrum 框架

| 角色             | 职责             |
| ---------------- | ---------------- |
| Product Owner    | 管理产品待办列表 |
| Scrum Master     | 促进 Scrum 实践  |
| Development Team | 自组织开发       |

| 事件       | 时长  | 目的           |
| ---------- | ----- | -------------- |
| Sprint     | 1~4周 | 迭代开发       |
| Sprint计划 | 4h    | 确定Sprint目标 |
| 每日站会   | 15min | 同步进展       |
| Sprint评审 | 4h    | 展示成果       |
| Sprint回顾 | 3h    | 持续改进       |

### 4.3 看板方法

- 可视化工作流
- 限制在制品（WIP）
- 管理流动
- 显式化策略
- 实施反馈环

### 4.4 极限编程（XP）

| 实践         | 说明             |
| ------------ | ---------------- |
| 结对编程     | 两人一台电脑     |
| 测试驱动开发 | 先写测试再写代码 |
| 持续集成     | 频繁集成到主干   |
| 重构         | 改善代码结构     |
| 简单设计     | 只实现当前需要   |

## 5. 软件测试

### 5.1 测试层次

| 层次     | 目标           | 方法     |
| -------- | -------------- | -------- |
| 单元测试 | 验证模块功能   | 白盒测试 |
| 集成测试 | 验证模块间接口 | 灰盒测试 |
| 系统测试 | 验证系统功能   | 黑盒测试 |
| 验收测试 | 验证用户需求   | 黑盒测试 |

### 5.2 白盒测试

**语句覆盖**：每条语句至少执行一次。

**分支覆盖**：每个分支至少执行一次。

**路径覆盖**：每条路径至少执行一次。

**条件覆盖**：每个条件的真假至少各取一次。

覆盖强度：路径 > 分支 > 语句

### 5.3 黑盒测试

**等价类划分**：将输入分为有效和无效等价类。

**边界值分析**：测试边界附近的值。

**因果图**：分析输入条件之间的逻辑关系。

**正交实验法**：减少测试用例数量。

### 5.4 测试金字塔

```
        /  E2E测试  \        少量，慢
       /  集成测试    \      适量
      /   单元测试      \    大量，快
```

### 5.5 度量指标

$$\text{缺陷密度} = \frac{\text{缺陷数}}{\text{代码行数（KLOC）}}$$

$$\text{测试覆盖率} = \frac{\text{已覆盖项}}{\text{总项}} \times 100\%$$

$$\text{MTBF} = \frac{\text{总运行时间}}{\text{故障次数}}$$

## 6. 软件度量

### 6.1 面向规模度量

$$\text{生产率} = \frac{\text{KLOC}}{\text{人月}}$$

$$\text{质量} = \frac{\text{缺陷数}}{\text{KLOC}}$$

### 6.2 面向对象度量（CK度量集）

| 度量 | 含义             |
| ---- | ---------------- |
| WMC  | 类的方法权重总和 |
| DIT  | 继承深度         |
| NOC  | 子类数量         |
| CBO  | 耦合度           |
| RFC  | 方法调用数       |
| LCOM | 方法内聚度       |

### 6.3 功能点分析

$$\text{FP} = \text{UFP} \times \text{VAF}$$

其中 UFP 为未调整功能点，VAF 为价值调整因子。

## 7. 软件维护

### 7.1 维护类型

| 类型       | 占比    | 说明         |
| ---------- | ------- | ------------ |
| 完善性维护 | 50%~66% | 增强功能     |
| 适应性维护 | 18%~25% | 适应环境变化 |
| 纠错性维护 | 17%~21% | 修复缺陷     |
| 预防性维护 | 4%      | 提高可维护性 |

### 7.2 技术债务

技术债务是选择快速方案而非更好方案所产生的额外工作：

$$\text{技术债务成本} = \text{当前妥协成本} + \text{未来修复成本}$$

管理策略：定期重构、代码审查、自动化测试。

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
| 软件工程 | 018-SoftwareEngineering | 本文自身 |
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
