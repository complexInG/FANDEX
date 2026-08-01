---
order: 66
title: 网络安全
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: intermediate
description: 网络安全：网络攻击与防御、防火墙、入侵检测、VPN与安全协议
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/操作系统进阶'
  - 'cs-fundamentals/计算机网络进阶'
  - 'cs-fundamentals/多媒体技术'
  - 'cs-fundamentals/人工智能基础'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 网络安全概述

### 1.1 安全威胁分类

| 威胁     | 说明             | 示例       |
| -------- | ---------------- | ---------- |
| 窃听     | 截获通信内容     | 网络嗅探   |
| 篡改     | 修改通信内容     | 中间人攻击 |
| 伪造     | 假冒身份发送消息 | IP 欺骗    |
| 拒绝服务 | 使服务不可用     | DDoS       |
| 重放     | 重复发送有效消息 | 重放攻击   |

### 1.2 安全服务

- **机密性**：数据加密
- **完整性**：消息认证码/数字签名
- **认证**：身份验证
- **访问控制**：权限管理
- **不可否认**：数字签名

## 2. 网络攻击技术

### 2.1 DDoS 攻击

**攻击类型**：

| 类型       | 目标层 | 方法                    |
| ---------- | ------ | ----------------------- |
| SYN Flood  | 传输层 | 大量半开连接耗尽资源    |
| UDP Flood  | 传输层 | 大量 UDP 包消耗带宽     |
| HTTP Flood | 应用层 | 大量 HTTP 请求          |
| DNS 放大   | 应用层 | 利用 DNS 服务器放大流量 |

**SYN Flood 原理**：

攻击者发送大量 SYN 包但不完成三次握手，服务器维护大量半开连接：

$$\text{半开连接数} \to \text{连接表满} \to \text{拒绝合法连接}$$

**防御**：

- SYN Cookie：不在连接表中保存半开连接
- 限速：限制每秒 SYN 数
- 黑洞路由：过滤攻击流量

### 2.2 中间人攻击（MITM）

攻击者截获并可能修改双方通信：

```
Alice ←→ 攻击者 ←→ Bob
  (以为在和Bob)  (以为在和Alice)
```

**防御**：TLS、证书固定、端到端加密。

### 2.3 DNS 欺骗

篡改 DNS 响应，将域名解析到恶意 IP。

**防御**：DNSSEC、DNS over HTTPS (DoH)、DNS over TLS (DoT)。

### 2.4 ARP 欺骗

发送伪造的 ARP 响应，将目标 IP 绑定到攻击者 MAC。

**防御**：静态 ARP 绑定、ARP 监控、端口安全。

## 3. 防火墙

### 3.1 防火墙类型

| 类型         | 工作层        | 特点                     |
| ------------ | ------------- | ------------------------ |
| 包过滤       | 网络层        | 基于 IP/端口过滤，速度快 |
| 状态检测     | 网络层+传输层 | 跟踪连接状态             |
| 应用层网关   | 应用层        | 深度包检测，速度慢       |
| 下一代防火墙 | 多层          | 集成 IPS、AV 等功能      |

### 3.2 包过滤规则

```
规则  源IP          目的IP        协议  源端口  目的端口  动作
1     192.168.1.*   10.0.0.1     TCP   *       80      允许
2     *             10.0.0.1     TCP   *       22      拒绝
3     *             *            *     *       *       拒绝
```

规则按顺序匹配，第一个匹配的规则决定动作。

### 3.3 网络地址转换（NAT）

NAT 隐藏内部网络结构，提供一定安全性：

- **静态 NAT**：一对一映射
- **动态 NAT**：地址池映射
- **NAPT/PAT**：端口多路复用

## 4. 入侵检测与防御

### 4.1 入侵检测系统（IDS）

| 类型 | 方法         | 优点     | 缺点             |
| ---- | ------------ | -------- | ---------------- |
| NIDS | 网络流量分析 | 覆盖面广 | 无法检测加密流量 |
| HIDS | 主机日志分析 | 检测精确 | 覆盖面窄         |

### 4.2 检测方法

**误用检测（签名匹配）**：

- 维护已知攻击特征库
- 准确率高，但无法检测未知攻击
- 类似杀毒软件

**异常检测（行为分析）**：

- 建立正常行为基线
- 偏离基线的行为视为异常
- 可检测未知攻击，但误报率高

### 4.3 入侵防御系统（IPS）

IPS 在 IDS 基础上增加了主动阻断能力：

- 内联部署（IDS 通常旁路部署）
- 检测到攻击时自动阻断
- 风险：误报可能导致合法流量被阻断

## 5. VPN 技术

### 5.1 VPN 类型

| 类型           | 说明       | 适用场景     |
| -------------- | ---------- | ------------ |
| 远程访问 VPN   | 单用户连接 | 远程办公     |
| 站点到站点 VPN | 网络间连接 | 分支机构互联 |
| SSL VPN        | 基于 Web   | 无需客户端   |

### 5.2 IPsec

IPsec 提供 IP 层的安全服务：

**AH（认证头）**：提供完整性和认证，不加密。

**ESP（封装安全载荷）**：提供加密、完整性和认证。

**两种模式**：

| 模式     | 保护范围       | 开销 |
| -------- | -------------- | ---- |
| 传输模式 | 仅载荷         | 小   |
| 隧道模式 | 整个原始 IP 包 | 大   |

**IKE（密钥交换）**：

- IKE Phase 1：建立 ISAKMP SA（主模式/积极模式）
- IKE Phase 2：建立 IPsec SA（快速模式）

### 5.3 WireGuard

现代 VPN 协议，特点：

- 代码量小（~4000 行）
- 使用现代密码学（ChaCha20、Poly1305、Curve25519）
- 快速握手（1-RTT）
- 无需手动管理 SA

## 6. 安全协议

### 6.1 TLS 1.3

TLS 1.3 简化了握手流程：

```
Client → Server: ClientHello + Key Share
Server → Client: ServerHello + Key Share + Certificate + Finished
Client → Server: Finished
```

1-RTT 握手（TLS 1.2 需要 2-RTT）。

0-RTT 模式：使用预共享密钥（PSK），但有重放攻击风险。

### 6.2 SSH

安全远程登录协议：

- 传输层协议：密钥交换、加密、MAC
- 认证协议：公钥认证、密码认证
- 连接协议：多路复用、端口转发

### 6.3 802.1X

网络接入认证：

```
客户端(Supplicant) ←EAPOL→ 认证器(Authenticator) ←RADIUS→ 认证服务器
```

## 7. 零信任安全

### 7.1 零信任原则

- **永不信任，始终验证**
- 最小权限原则
- 微分段
- 持续验证

### 7.2 零信任架构

```
用户/设备 → 零信任代理 → 策略决策点(PDP) → 策略执行点(PEP) → 资源
```

核心组件：

- **PEP**：策略执行点，拦截所有请求
- **PDP**：策略决策点，基于上下文评估访问权限
- **信任评估**：持续评估用户、设备、环境的风险

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
| 网络安全 | 023-NetworkSecurity | 本文自身 |
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
