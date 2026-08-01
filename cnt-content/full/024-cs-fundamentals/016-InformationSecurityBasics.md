---
order: 60
title: 信息安全基础
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: intermediate
description: 信息安全基础：密码学原理、对称加密、非对称加密、哈希函数与数字签名
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/算法设计与分析'
  - 'cs-fundamentals/形式语言与自动机'
  - 'cs-fundamentals/编译原理'
  - 'cs-fundamentals/软件工程'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 信息安全概述

### 1.1 CIA 三元组

| 属性                      | 说明                 | 威胁       |
| ------------------------- | -------------------- | ---------- |
| 机密性（Confidentiality） | 信息不被未授权访问   | 窃听、泄露 |
| 完整性（Integrity）       | 信息不被未授权修改   | 篡改、伪造 |
| 可用性（Availability）    | 信息可被授权用户访问 | DDoS、破坏 |

### 1.2 安全服务

- **认证**：验证身份
- **访问控制**：限制资源访问
- **数据机密性**：防止信息泄露
- **数据完整性**：检测篡改
- **不可否认**：防止抵赖

## 2. 对称加密

### 2.1 基本原理

加密和解密使用相同密钥：

$$E_K(M) = C, \quad D_K(C) = M$$

### 2.2 分组密码

**AES（Advanced Encryption Standard）**：

| 参数     | AES-128 | AES-192 | AES-256 |
| -------- | ------- | ------- | ------- |
| 密钥长度 | 128 位  | 192 位  | 256 位  |
| 轮数     | 10      | 12      | 14      |
| 分组大小 | 128 位  | 128 位  | 128 位  |

AES 操作：

1. SubBytes：S盒字节替换
2. ShiftRows：行移位
3. MixColumns：列混合
4. AddRoundKey：轮密钥加

**工作模式**：

| 模式 | 并行加密 | 并行解密 | 随机访问 | 错误传播 |
| ---- | -------- | -------- | -------- | -------- |
| ECB  | 是       | 是       | 是       | 1块      |
| CBC  | 否       | 是       | 否       | 2块      |
| CTR  | 是       | 是       | 是       | 1块      |
| GCM  | 是       | 是       | 是       | 1块      |

### 2.3 流密码

**ChaCha20**：Google 推荐的流密码，比 AES 在软件实现上更快。

$$\text{密钥流} = \text{ChaCha20\_Block}(Key, Counter, Nonce)$$

$$C_i = M_i \oplus \text{密钥流}_i$$

## 3. 非对称加密

### 3.1 基本原理

使用一对密钥：公钥加密，私钥解密。

$$E_{PK}(M) = C, \quad D_{SK}(C) = M$$

### 3.2 RSA

**密钥生成**：

1. 选择两个大素数 $p, q$
2. 计算 $n = pq$，$\phi(n) = (p-1)(q-1)$
3. 选择 $e$，满足 $1 < e < \phi(n)$，$\gcd(e, \phi(n)) = 1$
4. 计算 $d$，满足 $ed \equiv 1 \pmod{\phi(n)}$
5. 公钥 $(n, e)$，私钥 $(n, d)$

**加密**：$C = M^e \mod n$

**解密**：$M = C^d \mod n$

**正确性**：由 Euler 定理，$M^{ed} \equiv M \pmod{n}$

**安全性**：基于大整数分解困难性。推荐密钥长度 ≥ 2048 位。

### 3.3 椭圆曲线密码（ECC）

在有限域上的椭圆曲线上定义运算：

$$y^2 = x^3 + ax + b \pmod{p}$$

**ECDSA**：椭圆曲线数字签名算法。

**ECDH**：椭圆曲线 Diffie-Hellman 密钥交换。

**优势**：256 位 ECC ≈ 3072 位 RSA 的安全强度。

### 3.4 Diffie-Hellman 密钥交换

允许双方在不安全信道上协商共享密钥：

```
Alice: 选择私钥 a，计算 A = g^a mod p，发送 A
Bob:   选择私钥 b，计算 B = g^b mod p，发送 B
共享密钥: K = g^{ab} mod p
  Alice: K = B^a mod p
  Bob:   K = A^b mod p
```

安全性基于离散对数问题。

## 4. 哈希函数

### 4.1 性质

- **抗原象性**：给定 $h$，难以找到 $m$ 使得 $H(m) = h$
- **抗第二原象性**：给定 $m_1$，难以找到 $m_2 \neq m_1$ 使得 $H(m_1) = H(m_2)$
- **抗碰撞性**：难以找到 $m_1 \neq m_2$ 使得 $H(m_1) = H(m_2)$

### 4.2 常用哈希算法

| 算法    | 输出长度 | 状态   |
| ------- | -------- | ------ |
| MD5     | 128 位   | 已破解 |
| SHA-1   | 160 位   | 已破解 |
| SHA-256 | 256 位   | 安全   |
| SHA-3   | 可变     | 安全   |
| BLAKE3  | 可变     | 安全   |

### 4.3 SHA-256 结构

基于 Merkle-Damgård 结构：

1. 填充消息使其长度 $\equiv 448 \pmod{512}$
2. 附加原始长度（64位）
3. 以 512 位块处理
4. 每块进行 64 轮压缩

## 5. 数字签名

### 5.1 签名流程

```
签名：Sign(SK, M) = σ
验证：Verify(PK, M, σ) = True/False
```

通常先对消息哈希再签名：

$$\sigma = \text{Sign}(SK, H(M))$$

### 5.2 RSA 签名

$$\sigma = H(M)^d \mod n$$

$$\text{验证：} \sigma^e \mod n \stackrel{?}{=} H(M)$$

### 5.3 DSA 签名

1. 选择随机 $k$
2. $r = (g^k \mod p) \mod q$
3. $s = k^{-1}(H(M) + xr) \mod q$
4. 签名为 $(r, s)$

**注意**：$k$ 必须随机且不可重复，否则可推导出私钥。

## 6. 公钥基础设施（PKI）

### 6.1 数字证书

X.509 证书结构：

```
版本 | 序列号 | 签名算法 | 颁发者 | 有效期 | 主体 | 公钥 | 签名
```

### 6.2 证书链

```
根 CA → 中间 CA → 终端证书
```

验证时沿证书链逐级验证签名，直到信任的根 CA。

### 6.3 TLS/SSL

TLS 握手流程（简化）：

```
1. ClientHello: 支持的加密套件、随机数
2. ServerHello: 选定加密套件、证书、随机数
3. Client: 验证证书，生成预主密钥，用服务器公钥加密发送
4. 双方: 根据预主密钥和随机数生成会话密钥
5. 切换到对称加密通信
```

## 7. 密码分析

### 7.1 攻击类型

| 攻击类型     | 攻击者已知      |
| ------------ | --------------- |
| 唯密文攻击   | 仅密文          |
| 已知明文攻击 | 部分明文-密文对 |
| 选择明文攻击 | 可选择明文加密  |
| 选择密文攻击 | 可选择密文解密  |

### 7.2 生日攻击

利用生日悖论寻找哈希碰撞：

$$\text{碰撞概率} \approx 1 - e^{-n^2/(2 \cdot 2^m)}$$

其中 $m$ 为哈希输出位数，$n$ 为尝试次数。

找到碰撞所需的尝试次数约为 $2^{m/2}$，远小于暴力搜索的 $2^m$。

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
| 信息安全基础 | 016-InformationSecurityBasics | 本文自身 |
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
