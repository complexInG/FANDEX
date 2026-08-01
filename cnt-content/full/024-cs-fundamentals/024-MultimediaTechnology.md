---
order: 67
title: 多媒体技术
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: intermediate
description: 多媒体技术：音频编码、图像压缩、视频编码、流媒体与多媒体网络
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/计算机网络进阶'
  - 'cs-fundamentals/网络安全'
  - 'cs-fundamentals/人工智能基础'
  - 'cs-fundamentals/计算机图形学'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 音频编码

### 1.1 音频基础

- **采样率**：每秒采样次数（CD：44.1kHz）
- **量化位数**：每个采样的精度（CD：16位）
- **声道数**：单声道/立体声

**Nyquist 定理**：采样率必须大于信号最高频率的2倍：

$$f_s \geq 2 \times f_{max}$$

CD 音质数据率：

$$44100 \times 16 \times 2 = 1411.2 \text{ kbps}$$

### 1.2 音频编码算法

| 编码器 | 类型     | 比特率       | 质量    |
| ------ | -------- | ------------ | ------- |
| PCM    | 无损     | 1411 kbps    | 原始    |
| FLAC   | 无损压缩 | ~700 kbps    | 原始    |
| MP3    | 有损     | 128~320 kbps | 好      |
| AAC    | 有损     | 96~256 kbps  | 优于MP3 |
| Opus   | 有损     | 6~510 kbps   | 最优    |

### 1.3 感知编码

利用人耳的掩蔽效应：

- **频域掩蔽**：强信号掩盖附近的弱信号
- **时域掩蔽**：强信号前后一定时间内的弱信号不可感知

$$\text{压缩比} = \frac{\text{原始比特率}}{\text{编码比特率}}$$

## 2. 图像压缩

### 2.1 色彩空间

**RGB**：红绿蓝三原色，用于显示。

**YCbCr**：亮度+色度，用于压缩：

$$Y = 0.299R + 0.587G + 0.114B$$

$$Cb = 0.564(B - Y)$$

$$Cr = 0.713(R - Y)$$

人眼对亮度更敏感，可对色度进行下采样（4:2:0）。

### 2.2 JPEG 编码

1. **颜色转换**：RGB → YCbCr
2. **色度下采样**：4:2:0
3. **分块 DCT**：8×8 块离散余弦变换
4. **量化**：除以量化表，取整（信息损失主要来源）
5. **熵编码**：Zigzag 扫描 + Huffman 编码

**DCT 变换**：

$$F(u,v) = \frac{1}{4}C(u)C(v)\sum_{x=0}^{7}\sum_{y=0}^{7}f(x,y)\cos\frac{(2x+1)u\pi}{16}\cos\frac{(2y+1)v\pi}{16}$$

量化步长越大，压缩比越高，质量越低。

### 2.3 现代图像格式

| 格式    | 压缩方式   | 特点                   |
| ------- | ---------- | ---------------------- |
| JPEG    | DCT + 量化 | 有损，兼容性好         |
| PNG     | DEFLATE    | 无损，支持透明         |
| WebP    | VP8/VP8L   | 有损/无损，比JPEG小30% |
| AVIF    | AV1        | 有损/无损，比JPEG小50% |
| JPEG XL | 多种       | 有损/无损，向后兼容    |

## 3. 视频编码

### 3.1 视频编码原理

视频压缩利用三种冗余：

- **空间冗余**：帧内像素的相关性
- **时间冗余**：帧间像素的相关性
- **统计冗余**：符号出现的概率不均匀

### 3.2 帧类型

| 帧类型        | 说明     | 压缩率 |
| ------------- | -------- | ------ |
| I帧（关键帧） | 独立编码 | 低     |
| P帧（预测帧） | 前向预测 | 中     |
| B帧（双向帧） | 双向预测 | 高     |

**GOP（Group of Pictures）**：

```mermaid
flowchart LR
    I[I] B1[B] B2[B] P1[P] B3[B] B4[B] P2[P] B5[B] B6[B] I2[I]
    I --- B1 --- B2 --- P1 --- B3 --- B4 --- P2 --- B5 --- B6 --- I2
```

I 帧为 GOP 起始，新 GOP 从下一个 I 帧开始

### 3.3 运动估计

在参考帧中搜索最匹配的块：

$$\text{SAD} = \sum_{i,j}|C(i,j) - R(i+dx, j+dy)|$$

运动矢量 $(dx, dy)$ 使 SAD 最小。

搜索算法：

| 算法     | 搜索点数     | 质量 |
| -------- | ------------ | ---- |
| 全搜索   | $(2p+1)^2$   | 最优 |
| 三步搜索 | $1+9+9+9=28$ | 良好 |
| 菱形搜索 | ~20          | 良好 |

### 3.4 编码标准演进

| 标准       | 年份 | 压缩效率     | 特点     |
| ---------- | ---- | ------------ | -------- |
| H.264/AVC  | 2003 | 基准         | 广泛兼容 |
| H.265/HEVC | 2013 | ~50%提升     | 4K/8K    |
| AV1        | 2018 | ~30%优于HEVC | 开源免费 |
| H.266/VVC  | 2020 | ~50%优于HEVC | 最新标准 |

### 3.5 码率控制

**CBR（恒定比特率）**：码率恒定，质量波动。

**VBR（可变比特率）**：质量恒定，码率波动。

**ABR（平均比特率）**：目标平均码率，允许波动。

**CQ/VBR with cap**：质量优先，设置码率上限。

## 4. 流媒体技术

### 4.1 流媒体协议

| 协议   | 类型   | 延迟   | 适用场景  |
| ------ | ------ | ------ | --------- |
| RTMP   | 推流   | 1~3s   | 直播推流  |
| HLS    | 拉流   | 10~30s | 点播/直播 |
| DASH   | 拉流   | 10~30s | 点播/直播 |
| WebRTC | P2P    | <1s    | 实时通信  |
| SRT    | 推拉流 | 1~3s   | 远程制作  |

### 4.2 HLS 工作流程

```
1. 编码器生成不同质量的分段（.ts）
2. 生成播放列表（.m3u8）
3. 客户端下载播放列表
4. 根据带宽选择质量级别
5. 下载并播放分段
```

**自适应码率（ABR）**：

$$\text{选择质量} = f(\text{当前带宽}, \text{缓冲区状态}, \text{历史吞吐量})$$

### 4.3 低延迟直播

**LL-HLS**：HLS 的低延迟扩展，支持部分分段传输。

**WebRTC**：

- ICE（交互式连接建立）：NAT 穿越
- DTLS：安全传输
- SRTP：安全实时传输
- SCTP：数据通道

## 5. 多媒体网络

### 5.1 QoS 需求

| 媒体类型 | 带宽      | 延迟   | 抖动   | 丢包   |
| -------- | --------- | ------ | ------ | ------ |
| 语音     | 8~64 kbps | <150ms | <30ms  | <1%    |
| 视频     | 1~20 Mbps | <200ms | <50ms  | <0.1%  |
| 流媒体   | 2~25 Mbps | <5s    | 不敏感 | 不敏感 |

### 5.2 RTP/RTCP

**RTP（实时传输协议）**：

- 承载媒体数据
- 包含时间戳、序列号、载荷类型
- 通常基于 UDP

**RTCP（RTP 控制协议）**：

- 传输统计信息
- 发送者报告（SR）
- 接收者报告（RR）
- 用于自适应码率调整

### 5.3 FEC 与重传

**前向纠错（FEC）**：添加冗余数据，无需反馈。

$$\text{FEC 开销} = \frac{\text{冗余包数}}{\text{总包数}}$$

**自动重传（ARQ）**：请求重传丢失的包，增加延迟。

混合方案：对延迟敏感的用 FEC，对延迟不敏感的用 ARQ。

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
| 多媒体技术 | 024-MultimediaTechnology | 本文自身 |
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
