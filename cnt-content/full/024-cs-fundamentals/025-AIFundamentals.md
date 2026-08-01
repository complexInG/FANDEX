---
order: 68
title: 人工智能基础
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: intermediate
description: 人工智能基础：搜索算法、知识表示、机器学习、神经网络与深度学习
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/网络安全'
  - 'cs-fundamentals/多媒体技术'
  - 'cs-fundamentals/计算机图形学'
  - 'cs-fundamentals/设计模式'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 人工智能概述

### 1.1 AI 发展历程

| 阶段     | 年代        | 核心思想         |
| -------- | ----------- | ---------------- |
| 符号主义 | 1950s-1980s | 基于逻辑推理     |
| 连接主义 | 1980s-1990s | 神经网络         |
| 统计学习 | 2000s-2010s | 机器学习         |
| 深度学习 | 2012-       | 深层神经网络     |
| 大模型   | 2020-       | Transformer、LLM |

### 1.2 AI 分类

| 类型   | 定义     | 示例               |
| ------ | -------- | ------------------ |
| 弱AI   | 特定任务 | 图像识别、语音助手 |
| 强AI   | 通用智能 | 尚未实现           |
| 超级AI | 超越人类 | 理论概念           |

## 2. 搜索算法

### 2.1 无信息搜索

| 算法 | 完备性 | 最优性     | 时间                 | 空间                 |
| ---- | ------ | ---------- | -------------------- | -------------------- |
| BFS  | 是     | 是(等代价) | $O(b^d)$             | $O(b^d)$             |
| DFS  | 否     | 否         | $O(b^m)$             | $O(bm)$              |
| UCS  | 是     | 是         | $O(b^{C*/\epsilon})$ | $O(b^{C*/\epsilon})$ |
| IDS  | 是     | 是(等代价) | $O(b^d)$             | $O(bd)$              |

$b$：分支因子，$d$：解深度，$m$：最大深度

### 2.2 启发式搜索

**A\* 算法**：

$$f(n) = g(n) + h(n)$$

- $g(n)$：从起点到 $n$ 的实际代价
- $h(n)$：从 $n$ 到目标的启发式估计

**最优性条件**：$h(n)$ 是可采纳的（不高估实际代价）。

**A\* 的效率**：

$$\text{有效分支因子} = b^* : N = 1 + b^* + (b^*)^2 + ...$$

### 2.3 对抗搜索

**Minimax 算法**：

$$V(s) = \begin{cases} \text{utility}(s) & \text{终止状态} \\ \max_{a}V(\text{result}(s,a)) & \text{MAX 节点} \\ \min_{a}V(\text{result}(s,a)) & \text{MIN 节点} \end{cases}$$

**Alpha-Beta 剪枝**：

- $\alpha$：MAX 节点当前最优值
- $\beta$：MIN 节点当前最优值
- 剪枝条件：$\alpha \geq \beta$

最佳情况下搜索节点数：$O(b^{d/2})$

## 3. 知识表示与推理

### 3.1 一阶谓词逻辑

**基本元素**：

- 常量：John, 5
- 变量：$x$, $y$
- 谓词：$Likes(x, y)$
- 函数：$Father(John)$
- 量词：$\forall$, $\exists$

**推理规则**：

- 假言推理（Modus Ponens）：$P, P \to Q \vdash Q$
- 全称实例化：$\forall x P(x) \vdash P(a)$
- 存在实例化：$\exists x P(x) \vdash P(c)$

### 3.2 语义网络

用图结构表示概念间的关系：

```
[鸟] --is-a--> [动物]
[企鹅] --is-a--> [鸟]
[企鹅] --cannot--> [飞]
```

### 3.3 本体论

使用 OWL（Web Ontology Language）定义概念层次和关系：

- 类（Class）
- 属性（Property）
- 个体（Individual）
- 公理（Axiom）

## 4. 机器学习

### 4.1 学习范式

| 范式       | 训练数据        | 目标       |
| ---------- | --------------- | ---------- |
| 监督学习   | 标注数据        | 预测标签   |
| 无监督学习 | 无标注数据      | 发现结构   |
| 半监督学习 | 部分+大量无标注 | 预测标签   |
| 强化学习   | 环境反馈        | 最大化奖励 |
| 自监督学习 | 自生成标签      | 学习表示   |

### 4.2 线性回归

$$\hat{y} = \mathbf{w}^T \mathbf{x} + b$$

**损失函数（MSE）**：

$$L = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

**正规方程**：

$$\mathbf{w}^* = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

### 4.3 逻辑回归

$$P(y=1|\mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x} + b) = \frac{1}{1+e^{-(\mathbf{w}^T\mathbf{x}+b)}}$$

**交叉熵损失**：

$$L = -\frac{1}{n}\sum_{i=1}^{n}[y_i\log\hat{y}_i + (1-y_i)\log(1-\hat{y}_i)]$$

### 4.4 支持向量机（SVM）

**最大间隔**：

$$\max_{\mathbf{w},b} \frac{2}{\|\mathbf{w}\|} \quad \text{s.t.} \quad y_i(\mathbf{w}^T\mathbf{x}_i+b) \geq 1$$

**核技巧**：

$$K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T\phi(\mathbf{x}_j)$$

常用核函数：

| 核函数   | 公式                                             |
| -------- | ------------------------------------------------ |
| 线性核   | $K = \mathbf{x}_i^T\mathbf{x}_j$                 |
| 多项式核 | $K = (\mathbf{x}_i^T\mathbf{x}_j + c)^d$         |
| RBF核    | $K = e^{-\gamma\|\mathbf{x}_i-\mathbf{x}_j\|^2}$ |

### 4.5 模型评估

| 指标    | 公式                              |
| ------- | --------------------------------- |
| 准确率  | $\frac{TP+TN}{TP+TN+FP+FN}$       |
| 精确率  | $\frac{TP}{TP+FP}$                |
| 召回率  | $\frac{TP}{TP+FN}$                |
| F1      | $2 \times \frac{P \times R}{P+R}$ |
| AUC-ROC | ROC曲线下面积                     |

**偏差-方差权衡**：

$$\text{泛化误差} = \text{偏差}^2 + \text{方差} + \text{噪声}$$

## 5. 神经网络

### 5.1 多层感知机（MLP）

$$\mathbf{h} = \sigma(\mathbf{W}_1\mathbf{x} + \mathbf{b}_1)$$

$$\mathbf{y} = \mathbf{W}_2\mathbf{h} + \mathbf{b}_2$$

**反向传播**：

$$\frac{\partial L}{\partial \mathbf{W}} = \frac{\partial L}{\partial \mathbf{y}} \cdot \frac{\partial \mathbf{y}}{\partial \mathbf{h}} \cdot \frac{\partial \mathbf{h}}{\partial \mathbf{W}}$$

### 5.2 常用激活函数

| 函数       | 公式                | 特点               |
| ---------- | ------------------- | ------------------ |
| ReLU       | $\max(0, x)$        | 计算快，有死亡问题 |
| Leaky ReLU | $\max(\alpha x, x)$ | 缓解死亡           |
| GELU       | $x\Phi(x)$          | Transformer 常用   |
| Swish      | $x\sigma(\beta x)$  | 平滑               |

### 5.3 优化算法

| 算法     | 更新规则                                           |
| -------- | -------------------------------------------------- |
| SGD      | $\theta = \theta - \eta \nabla L$                  |
| Momentum | $v = \beta v + \nabla L, \theta = \theta - \eta v$ |
| Adam     | 结合 Momentum 和 RMSProp                           |

**Adam 更新规则**：

$$m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t$$

$$v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$$

$$\theta_t = \theta_{t-1} - \frac{\eta}{\sqrt{\hat{v}_t}+\epsilon}\hat{m}_t$$

### 5.4 正则化技术

| 技术       | 方法                      | 防止           |
| ---------- | ------------------------- | -------------- |
| Dropout    | 随机丢弃神经元            | 过拟合         |
| L2 正则    | $\lambda\|\mathbf{w}\|^2$ | 过拟合         |
| Batch Norm | 归一化层输入              | 内部协变量偏移 |
| 数据增强   | 扩充训练数据              | 过拟合         |
| 早停       | 验证集性能下降时停止      | 过拟合         |

## 6. 深度学习

### 6.1 CNN（卷积神经网络）

核心操作：

- 卷积：提取局部特征
- 池化：降维，增强平移不变性
- 全连接：分类决策

经典架构：

| 网络         | 年份 | 创新          |
| ------------ | ---- | ------------- |
| LeNet        | 1998 | 开创性 CNN    |
| AlexNet      | 2012 | ReLU、Dropout |
| VGG          | 2014 | 小卷积核堆叠  |
| ResNet       | 2015 | 残差连接      |
| EfficientNet | 2019 | 复合缩放      |

**残差连接**：

$$\mathbf{y} = F(\mathbf{x}) + \mathbf{x}$$

解决深层网络的梯度消失问题。

### 6.2 Transformer

**自注意力机制**：

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

**多头注意力**：

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O$$

$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

### 6.3 大语言模型（LLM）

基于 Transformer Decoder 的生成式模型：

- GPT 系列：自回归生成
- BERT：双向编码
- LLaMA：开源大模型

**缩放定律**：

$$L(N) \approx \left(\frac{N_c}{N}\right)^{\alpha}$$

模型性能随参数量 $N$、数据量 $D$、计算量 $C$ 的增加而可预测地提升。

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
| 人工智能基础 | 025-AIFundamentals | 本文自身 |
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
