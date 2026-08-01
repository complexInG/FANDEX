---
order: 69
title: 计算机图形学
module: 'cs-fundamentals'
category: 'Computer Science'
difficulty: intermediate
description: 计算机图形学：图形变换、光栅化、光照模型、着色与渲染管线
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cs-fundamentals/多媒体技术'
  - 'cs-fundamentals/人工智能基础'
  - 'cs-fundamentals/设计模式'
  - 'cs-fundamentals/软件体系结构'
prerequisites:
  - 'cs-fundamentals/计算机科学概述'
---

## 1. 图形学基础

### 1.1 坐标系统

| 坐标系   | 说明         |
| -------- | ------------ |
| 模型空间 | 物体局部坐标 |
| 世界空间 | 全局坐标     |
| 观察空间 | 相机坐标     |
| 裁剪空间 | 投影后坐标   |
| 屏幕空间 | 像素坐标     |

### 1.2 变换矩阵

**平移**：

$$T = \begin{pmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

**缩放**：

$$S = \begin{pmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

**旋转（绕 Z 轴）**：

$$R_z = \begin{pmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

### 1.3 MVP 变换

$$\mathbf{p}_{clip} = M_{projection} \times M_{view} \times M_{model} \times \mathbf{p}_{local}$$

## 2. 投影

### 2.1 透视投影

近大远小，符合人眼视觉：

$$M_{persp} = \begin{pmatrix} \frac{2n}{r-l} & 0 & \frac{r+l}{r-l} & 0 \\ 0 & \frac{2n}{t-b} & \frac{t+b}{t-b} & 0 \\ 0 & 0 & -\frac{f+n}{f-n} & -\frac{2fn}{f-n} \\ 0 & 0 & -1 & 0 \end{pmatrix}$$

其中 $n$ 为近裁剪面距离，$f$ 为远裁剪面距离。

### 2.2 正交投影

平行投影，无近大远小：

$$M_{ortho} = \begin{pmatrix} \frac{2}{r-l} & 0 & 0 & -\frac{r+l}{r-l} \\ 0 & \frac{2}{t-b} & 0 & -\frac{t+b}{t-b} \\ 0 & 0 & \frac{2}{n-f} & -\frac{n+f}{n-f} \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

## 3. 光栅化

### 3.1 三角形光栅化

将三角形覆盖的像素标记为"内部"。

**判断点在三角形内**：

使用叉积判断：

$$\vec{v}_0 \times \vec{v}_1 > 0 \wedge \vec{v}_1 \times \vec{v}_2 > 0 \wedge \vec{v}_2 \times \vec{v}_0 > 0$$

### 3.2 重心坐标

三角形内任意点 $P$ 可表示为：

$$P = \alpha A + \beta B + \gamma C$$

$$\alpha + \beta + \gamma = 1, \quad \alpha, \beta, \gamma \geq 0$$

$$\alpha = \frac{S_{PBC}}{S_{ABC}}, \quad \beta = \frac{S_{PCA}}{S_{ABC}}, \quad \gamma = \frac{S_{PAB}}{S_{ABC}}$$

### 3.3 Z-Buffer 算法

维护深度缓冲区，解决遮挡问题：

```
for each triangle:
    for each pixel in triangle:
        if z < zbuffer[x][y]:
            zbuffer[x][y] = z
            framebuffer[x][y] = color
```

时间复杂度：$O(n)$（$n$ 为三角形数 × 每个三角形的像素数）

空间复杂度：$O(W \times H)$（帧缓冲 + 深度缓冲）

## 4. 光照模型

### 4.1 Phong 光照模型

$$I = I_a \cdot k_a + I_d \cdot k_d (\mathbf{N} \cdot \mathbf{L}) + I_s \cdot k_s (\mathbf{R} \cdot \mathbf{V})^n$$

| 分量                                              | 含义         | 说明       |
| ------------------------------------------------- | ------------ | ---------- |
| 环境光 $I_a k_a$                                  | 全局光照     | 常量       |
| 漫反射 $I_d k_d(\mathbf{N} \cdot \mathbf{L})$     | Lambert 反射 | 与视角无关 |
| 镜面反射 $I_s k_s(\mathbf{R} \cdot \mathbf{V})^n$ | 高光         | 与视角有关 |

**Blinn-Phong 改进**：用半程向量 $\mathbf{H} = \frac{\mathbf{L}+\mathbf{V}}{\|\mathbf{L}+\mathbf{V}\|}$ 替代 $\mathbf{R}$：

$$I_{specular} = k_s (\mathbf{N} \cdot \mathbf{H})^n$$

### 4.2 着色频率

| 着色方式     | 计算位置 | 效果     |
| ------------ | -------- | -------- |
| Flat 着色    | 每个面   | 面片感强 |
| Gouraud 着色 | 每个顶点 | 较平滑   |
| Phong 着色   | 每个像素 | 最平滑   |

## 5. 纹理映射

### 5.1 纹理坐标

将2D纹理映射到3D表面：

$$(u, v) \in [0, 1] \times [0, 1]$$

### 5.2 纹理过滤

| 方法   | 质量           | 性能 |
| ------ | -------------- | ---- |
| 最近邻 | 差（锯齿）     | 最快 |
| 双线性 | 好             | 中等 |
| 三线性 | 最好（Mipmap） | 较慢 |

**Mipmap**：预计算多级纹理，根据像素与纹理的距离选择级别：

$$\text{级别} = \log_2\left(\max\left(\frac{du}{dx}, \frac{dv}{dx}, \frac{du}{dy}, \frac{dv}{dy}\right)\right)$$

### 5.3 法线贴图

用纹理存储法线方向，模拟表面细节而不增加几何复杂度：

$$\mathbf{N}' = \text{normalize}(T \cdot \mathbf{n}_t)$$

其中 $T$ 为切线空间变换矩阵，$\mathbf{n}_t$ 为纹理中的法线。

## 6. 渲染管线

### 6.1 图形渲染管线

```
顶点数据 → 顶点着色器 → 图元装配 → 几何着色器 → 光栅化 → 片段着色器 → 混合 → 帧缓冲
```

| 阶段       | 可编程 | 功能           |
| ---------- | ------ | -------------- |
| 顶点着色器 | 是     | MVP 变换       |
| 图元装配   | 否     | 组装图元       |
| 几何着色器 | 是     | 生成/修改图元  |
| 光栅化     | 否     | 生成片段       |
| 片段着色器 | 是     | 着色、纹理     |
| 混合       | 否     | 深度测试、混合 |

### 6.2 光线追踪

从相机发射光线，与场景求交：

```
for each pixel:
    ray = generate_ray(pixel)
    hit = trace_ray(ray, scene)
    color = shade(hit)
```

**递归光线追踪**：在交点处继续发射反射/折射光线。

**加速结构**：

| 结构    | 构建时间     | 查询时间    |
| ------- | ------------ | ----------- |
| BVH     | $O(n\log n)$ | $O(\log n)$ |
| KD-Tree | $O(n\log n)$ | $O(\log n)$ |
| 八叉树  | $O(n)$       | $O(\log n)$ |

### 6.3 路径追踪

蒙特卡洛方法求解渲染方程：

$$L_o(p, \omega_o) = L_e(p, \omega_o) + \int_{\Omega^+} f_r(p, \omega_i, \omega_o) L_i(p, \omega_i) (\mathbf{n} \cdot \omega_i) d\omega_i$$

通过采样估计积分：

$$L_o \approx L_e + \frac{1}{N}\sum_{i=1}^{N}\frac{f_r L_i (\mathbf{n} \cdot \omega_i)}{p(\omega_i)}$$

收敛速度：$O(1/\sqrt{N})$

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
| 计算机图形学 | 026-ComputerShape | 本文自身 |
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
