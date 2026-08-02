---
order: 52
title: 中心极限定理
module: 'probability-statistics'
category: 'comp-sci'
difficulty: advanced
description: 列维-林德伯格中心极限定理、棣莫弗-拉普拉斯中心极限定理、连续性修正与应用条件。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/切比雪夫不等式'
  - 'probability-statistics/大数定律'
  - 'probability-statistics/大数定律与中心极限定理典型例题'
  - 'probability-statistics/随机样本'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 0. 从一个生活场景说起：为什么"灯泡寿命"都像正态分布？

单个灯泡的寿命分布其实很"怪"：有的几百小时就坏，有的能用几年，明显右偏。但如果你统计**一个仓库里 1000 只灯泡的总寿命**，或者**1000 只灯泡的平均寿命**，你会发现它们的分布意外地接近正态的钟形曲线。

更神奇的是：不管单个变量服从什么分布（均匀、指数、偏态、离散……），只要它们独立且样本量够大，**和与均值都近似服从正态分布**。这就是中心极限定理（Central Limit Theorem，CLT）——正态分布统治统计世界的根本原因。

本文采用"**近似驱动**"的叙事结构：核心问题是"什么时候可以把复杂分布当正态算"。先建立直觉，再给列维-林德伯格 CLT（独立同分布情形）与棣莫弗-拉普拉斯 CLT（二项分布情形），重点讲透应用条件（$np \ge 5$、$n(1-p) \ge 5$）与连续性修正，最后给出完整例题。

## 1. 直观理解：大数定律 vs 中心极限定理

- **大数定律**（上一篇）：$\bar{X}_n$ **收敛到哪**——样本均值收敛于 $\mu$（一个点）；
- **中心极限定理**（本篇）：$\bar{X}_n$ **怎么波动**——围绕 $\mu$ 的波动幅度服从正态分布（一个形状）。

中心极限定理是大数定律的"精细版"：大数定律只知道"越来越接近 $\mu$"，CLT 还告诉我们"接近的程度服从什么分布"，从而可以**计算具体概率**。

### 例题 0（直觉建立）

掷 1 枚骰子，点数分布是均匀的（每个点数 $\dfrac{1}{6}$）；掷 2 枚骰子，点数之和呈三角分布（和为 7 概率最大）；掷 3 枚、4 枚……点数之和的分布越来越像钟形曲线。抛 100 枚骰子，点数之和几乎就是正态分布。

这个"叠加 → 正态"的过程，就是 CLT 的直觉来源：**大量独立随机因素相加，个体差异被"平均化"，整体呈现正态**。

## 2. 列维-林德伯格中心极限定理

### 2.1 定理

设 $X_1, X_2, \cdots$ 为独立同分布的随机变量序列，$E(X_i) = \mu$，$D(X_i) = \sigma^2 > 0$，则对任意实数 $x$：

$$\lim_{n \to \infty} P\left(\frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}} \leq x\right) = \Phi(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x} e^{-t^2/2} \, dt$$

即标准化变量 $\dfrac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$（依分布收敛）。

### 2.2 等价表述（实用版）

当 $n$ 充分大时：

$$\sum_{i=1}^n X_i \overset{\text{近似}}{\sim} N(n\mu, n\sigma^2), \qquad \bar{X}_n \overset{\text{近似}}{\sim} N\left(\mu, \frac{\sigma^2}{n}\right)$$

也就是：**和的近似正态**、**均值的近似正态**，参数由"和/均值的期望与方差"决定。做题时只需三步：算期望、算方差、标准化查表。

### 2.3 证明思路（特征函数）

设 $X_i$ 的特征函数为 $\varphi(t)$，标准化变量 $Y_i = \dfrac{X_i - \mu}{\sigma}$ 的特征函数为

$$\varphi_Y(t) = e^{-i\mu t/\sigma}\varphi(t/\sigma)$$

$S_n = \dfrac{\sum X_i - n\mu}{\sigma\sqrt{n}}$ 的特征函数为

$$\varphi_{S_n}(t) = \left[\varphi_Y\left(\frac{t}{\sqrt{n}}\right)\right]^n$$

由 $\varphi_Y(t) = 1 - \dfrac{t^2}{2} + o(t^2)$（$t \to 0$）：

$$\varphi_{S_n}(t) = \left[1 - \frac{t^2}{2n} + o\left(\frac{1}{n}\right)\right]^n \to e^{-t^2/2}$$

而 $e^{-t^2/2}$ 正是 $N(0,1)$ 的特征函数，由连续性定理得证。**特征函数法**是概率论中证明极限定理的通用武器。

## 3. 棣莫弗-拉普拉斯中心极限定理

### 3.1 定理

设 $X \sim B(n, p)$（$0 < p < 1$），则对任意实数 $x$：

$$\lim_{n \to \infty} P\left(\frac{X - np}{\sqrt{np(1-p)}} \leq x\right) = \Phi(x)$$

即当 $n$ 较大时，$X \overset{\text{近似}}{\sim} N(np, np(1-p))$。

### 3.2 与列维-林德伯格定理的关系

$X = \sum_{i=1}^n X_i$，$X_i \sim B(1, p)$ 独立同分布，$E(X_i) = p$，$D(X_i) = p(1-p)$——直接代入列维-林德伯格定理即得。所以棣莫弗-拉普拉斯定理是 CLT 在二项分布上的特例。

### 3.3 应用条件（必须满足）

$$np \geq 5 \quad \text{且} \quad n(1-p) \geq 5$$

经验法则：期望的"成功数"与"失败数"都不少于 5，二项分布的直方图才足够对称、可用正态近似。若 $n$ 很大但 $p$ 很小（稀有事件，如 $np \le 10$），应改用**泊松近似**（泊松定理），而不是正态近似。

## 4. 连续性修正：离散到连续的"桥"

二项分布是离散的（只取整数），正态分布是连续的。直接近似会让 $P(X = k)$ 这种"单点概率"失真，因此需要**连续性修正**：把整数 $k$ 看成区间 $\left(k - \dfrac{1}{2},\ k + \dfrac{1}{2}\right)$。

$$P(X = k) \approx \Phi\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right)$$

$$P(X \leq k) \approx \Phi\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$$

$$P(X \geq k) \approx 1 - \Phi\left(\frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right)$$

记忆口诀：**"≤ 加 0.5，≥ 减 0.5"**（左端点向右挪、右端点向左挪，把离散点"包"进区间）。

### 例题 1（含连续性修正）

设 $X \sim B(100, 0.5)$，用正态近似计算 $P(X = 50)$ 与 $P(X \le 50)$。

**解**：$np = 50$，$\sqrt{np(1-p)} = 5$，条件 $np \ge 5$ 与 $n(1-p) \ge 5$ 满足。

$$P(X = 50) \approx \Phi\left(\frac{50.5 - 50}{5}\right) - \Phi\left(\frac{49.5 - 50}{5}\right) = \Phi(0.1) - \Phi(-0.1) = 2\Phi(0.1) - 1 \approx 0.0797$$

$$P(X \le 50) \approx \Phi\left(\frac{50.5 - 50}{5}\right) = \Phi(0.1) \approx 0.5398$$

## 5. 中心极限定理的应用

### 例题 2（供电设计问题）

某车间有 200 台独立工作的机床，每台机床开工概率 0.6，开工时耗电 1 千瓦。问供电所至少要供应多少千瓦，才能以 99.9% 的概率保证不因供电不足而停产？

**解**：设 $X$ 为同时开工的机床数，$X \sim B(200, 0.6)$。

$$E(X) = 120, \qquad D(X) = 200 \times 0.6 \times 0.4 = 48$$

设供电 $k$ 千瓦，要求 $P(X \leq k) \geq 0.999$。由棣莫弗-拉普拉斯定理：

$$P(X \le k) \approx \Phi\left(\frac{k - 120}{\sqrt{48}}\right) \geq 0.999$$

查表得 $\Phi(3.09) = 0.999$，故

$$\frac{k - 120}{\sqrt{48}} \geq 3.09 \quad \Longrightarrow \quad k \geq 120 + 3.09\sqrt{48} \approx 120 + 21.4 = 141.4$$

取整数 $k = 142$ 千瓦。**步骤讲解**：① 识别 $X \sim B(n,p)$；② 算 $E$、$D$；③ 反解分位数；④ 向上取整（物理量不能"四舍五入"）。

### 例题 3（样本均值的近似分布）

设总体 $X$ 的均值 $\mu = 50$，方差 $\sigma^2 = 25$，从中抽取容量 $n = 100$ 的样本，求 $P(49 < \bar{X} < 51)$。

**解**：由 CLT，$\bar{X}$ 近似服从 $N\left(50, \dfrac{25}{100}\right) = N(50, 0.25)$，标准差 $\sqrt{0.25} = 0.5$。

$$P(49 < \bar{X} < 51) = \Phi\left(\frac{51 - 50}{0.5}\right) - \Phi\left(\frac{49 - 50}{0.5}\right) = \Phi(2) - \Phi(-2) = 2\Phi(2) - 1 \approx 0.9544$$

**注意**：这里 $\bar{X}$ 本身是连续型的近似（总体分布未知也无妨），不需要连续性修正；修正只针对离散型（如二项分布）的近似。

### 例题 4（测量误差问题）

测量某物理量，每次测量的误差服从 $(-1, 1)$ 上的均匀分布。求 100 次测量的算术平均值与真值之差的绝对值小于 0.1 的概率。

**解**：设 $X_i$ 为第 $i$ 次测量误差，$X_i \sim U(-1, 1)$，$E(X_i) = 0$，$D(X_i) = \dfrac{1}{3}$。

由 CLT，$\bar{X}$ 近似服从 $N\left(0, \dfrac{1/3}{100}\right) = N\left(0, \dfrac{1}{300}\right)$，标准差 $\sqrt{\dfrac{1}{300}} \approx 0.0577$。

$$P(|\bar{X}| < 0.1) \approx 2\Phi\left(\frac{0.1}{\sqrt{1/300}}\right) - 1 = 2\Phi(\sqrt{3}) - 1 \approx 2 \times 0.9582 - 1 = 0.9164$$

**要点**：均匀分布是最"不正态"的分布之一，但 100 次平均后近似正态已经非常好——这正是"均值检验"（如 $Z$ 检验）的理论基础（见《Z 检验》）。

## 6. 中心极限定理的推广

### 6.1 李雅普诺夫中心极限定理

设 $X_1, X_2, \cdots$ 相互独立（**不必同分布**），$E(X_i) = \mu_i$，$D(X_i) = \sigma_i^2$，记 $B_n^2 = \sum_{i=1}^n \sigma_i^2$。若存在 $\delta > 0$ 使

$$\lim_{n \to \infty} \frac{1}{B_n^{2+\delta}} \sum_{i=1}^n E|X_i - \mu_i|^{2+\delta} = 0$$

则

$$\frac{\sum_{i=1}^n X_i - \sum_{i=1}^n \mu_i}{B_n} \xrightarrow{d} N(0, 1)$$

直觉：各变量的"扰动"都不太极端（$2+\delta$ 阶矩可控），总扰动 $\sum X_i$ 依然近似正态。这保证了现实世界中"不同分布的独立因素之和"也能用正态近似（例如不同客户的理赔金额之和）。

### 6.2 应用条件小结

| 情形 | 适用定理 | 条件 |
| --- | --- | --- |
| 独立同分布之和/均值 | 列维-林德伯格 CLT | $n$ 较大（一般 $n \ge 30$ 经验值） |
| 二项分布 $B(n,p)$ | 棣莫弗-拉普拉斯 CLT | $np \ge 5$ 且 $n(1-p) \ge 5$ |
| 稀有事件二项分布 | 泊松定理（泊松近似） | $n$ 大、$p$ 小（$np$ 适中，如 $np \le 10$） |
| 独立不同分布之和 | 李雅普诺夫 CLT | 李雅普诺夫条件 |

## 7. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 忽略 $np \ge 5$ 与 $n(1-p) \ge 5$ 直接近似 | 前提遗漏 | 二项分布过偏时正态近似失真严重 | 先检查条件；不满足时改用泊松近似或精确计算 |
| 二项近似忘记连续性修正（$\pm 0.5$） | 方法遗漏 | 离散与连续的"台阶差"被忽略 | 单点、$\le k$、$\ge k$ 都要挪 0.5："≤ 加 0.5，≥ 减 0.5" |
| 把"和的方差"写成 $\sigma^2$ 而不是 $n\sigma^2$ | 公式误用 | 忘记求和放大方差 | $\sum X_i \sim N(n\mu, n\sigma^2)$；$\bar{X} \sim N(\mu, \sigma^2/n)$ |
| 用 $N(\mu, \sigma^2)$ 近似 $\bar{X}$ | 公式误用 | 混淆总体分布与均值分布 | 近似对象是 $\bar{X}$：$N(\mu, \sigma^2/n)$，不是总体的 $N(\mu, \sigma^2)$ |
| 对连续型变量也做连续性修正 | 过度修正 | 修正只针对离散型 | $\pm 0.5$ 只用于二项、泊松等离散分布的近似 |
| $n$ 很小就硬套 CLT | 前提忽视 | $n$ 过小近似误差大 | 经验上 $n \ge 30$ 才放心；更保守时用 $n \ge 50$ 或精确方法 |

## 8. 实战练习

### 练习 1（和分布的近似）

设 $X_1, \cdots, X_{50}$ 独立同分布，$X_i \sim \text{Exp}(2)$，求 $P\left(\sum_{i=1}^{50} X_i > 30\right)$ 的近似值。

**提示**：$E(X_i) = 0.5$，$D(X_i) = 0.25$；和服从 $N(25, 12.5)$。

**参考答案要点**：$P(S > 30) \approx 1 - \Phi\left(\dfrac{30 - 25}{\sqrt{12.5}}\right) = 1 - \Phi(1.414) \approx 0.0786$。

### 练习 2（均值分布的近似）

设 $X_1, \cdots, X_{36}$ 独立同分布，$X_i \sim U(0, 10)$，求 $P(\bar{X} > 5.5)$。

**提示**：$E(X_i) = 5$，$D(X_i) = \dfrac{25}{3}$；$\bar{X} \sim N\left(5, \dfrac{25}{108}\right)$。

**参考答案要点**：$P(\bar{X} > 5.5) \approx 1 - \Phi\left(\dfrac{5.5-5}{\sqrt{25/108}}\right) = 1 - \Phi(1.039) \approx 0.1494$。

### 练习 3（二项近似 + 修正）

设 $X \sim B(400, 0.2)$，求 $P(70 \le X \le 90)$ 的近似值。

**提示**：$np = 80$，$\sqrt{np(1-p)} = 8$；两端都修正：$P(69.5 \le X \le 90.5)$。

**参考答案要点**：$P = \Phi\left(\dfrac{90.5-80}{8}\right) - \Phi\left(\dfrac{69.5-80}{8}\right) = \Phi(1.3125) - \Phi(-1.3125) \approx 2 \times 0.9052 - 1 = 0.8104$。

### 练习 4（反解分位数）

一箱装 100 个产品，每个重量 $E(X_i) = 50$ 克，$D(X_i) = 25$。求一箱重量超过 5025 克的概率。

**提示**：$S \sim N(5000, 2500)$。

**参考答案要点**：$P(S > 5025) \approx 1 - \Phi\left(\dfrac{25}{50}\right) = 1 - \Phi(0.5) \approx 0.3085$。

### 练习 5（综合：区分用哪个定理）

设 $X_1, \cdots, X_n$ 独立同分布，$E(X_i) = 0$，$D(X_i) = 1$。用 CLT 求 $n$，使得 $P\left(\left|\sum_{i=1}^n X_i\right| < 10\right) \geq 0.9$。

**提示**：$\sum X_i \sim N(0, n)$；$P = 2\Phi\left(\dfrac{10}{\sqrt{n}}\right) - 1 \ge 0.9$。

**参考答案要点**：$\Phi\left(\dfrac{10}{\sqrt{n}}\right) \ge 0.95 \Rightarrow \dfrac{10}{\sqrt{n}} \ge 1.645 \Rightarrow n \le 36.96$，取 $n \le 36$。

## 9. 一句话记忆

中心极限定理回答"怎么波动"：独立同分布变量的和（均值）在 $n$ 大时近似正态——$\sum X_i \sim N(n\mu, n\sigma^2)$、$\bar{X} \sim N(\mu, \sigma^2/n)$；二项分布近似正态要满足 $np \ge 5$ 与 $n(1-p) \ge 5$，并记得用 $\pm 0.5$ 连续性修正。

## 参考文献

- 盛骤, 谢式千, 潘承毅. 概率论与数理统计（第六版）[M]. 高等教育出版社, 2026. 第五章"大数定律及中心极限定理"§2 中心极限定理. https://www.hep.com.cn/book/show/3b2dd87a-7531-4610-97e6-071eb302d813
- Normal Approximation: Binomial Guide, Formulas & Continuity Correction（$np \ge 5$ 条件与 $\pm 0.5$ 修正）. https://statisticsfundamentals.com/normal-distribution/normal-approximation/
- 二项分布的泊松估计与中心极限定理估计（含棣莫弗-拉普拉斯定理与泊松近似的适用场景对比）. https://kb.kmath.cn/kbase/detail.aspx?id=2870

## 延伸阅读

概率统计基础，见 030-probability-statistics 模块文档。
数据分析应用，见 051-data-analysis 模块。
机器学习概率视角，见 042-machine-learning 模块（AI 模块仅供了解）。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供概率统计课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 贝叶斯推断

贝叶斯公式：后验 ∝ 似然 × 先验；先验的选择影响结果。
共轭先验：后验同族（Beta-二项、Gamma-泊松），解析计算。
马尔可夫链蒙特卡洛（MCMC）：复杂后验数值采样。
应用：垃圾过滤、推荐、A/B 分层模型。

### 13.2 假设检验框架

零假设与备择假设、显著性水平、两类错误（α/β）、功效。
流程：假设 -> 检验统计量 -> p 值 -> 决策；注意前提条件。
常见检验：t、卡方、F、正态性检验。
现代实践：置信区间替代纯 p 值，注册分析计划防 p-hacking。
