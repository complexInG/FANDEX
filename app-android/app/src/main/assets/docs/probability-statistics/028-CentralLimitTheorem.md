---
order: 240
title: 中心极限定理
module: 'probability-statistics'
category: 数学
difficulty: advanced
description: 列维-林德伯格中心极限定理、棣莫弗-拉普拉斯中心极限定理、连续性修正与应用条件。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/026-ChebyshevInequality'
  - 'probability-statistics/027-LawOfLargeNumbers'
  - 'probability-statistics/030-RandomSample'
prerequisites:
  - 'probability-statistics/001-SampleSpaceAndEvent'
---


## 0. 从一个生活场景说起：为什么"灯泡寿命"都像正态分布？

单个灯泡的寿命分布其实很"怪"：有的几百小时就坏，有的能用几年，明显右偏。但如果你统计**一个仓库里 1000 只灯泡的总寿命**，或者**1000 只灯泡的平均寿命**，你会发现它们的分布意外地接近正态的钟形曲线。

更神奇的是：不管单个变量服从什么分布（均匀、指数、偏态、离散……），只要它们独立且样本量够大，**和与均值都近似服从正态分布**。这就是中心极限定理（Central Limit Theorem，CLT）——正态分布统治统计世界的根本原因。

本文采用"**近似驱动**"的叙事结构：核心问题是"什么时候可以把复杂分布当正态算"。先建立直觉，再给列维-林德伯格 CLT（独立同分布情形）与棣莫弗-拉普拉斯 CLT（二项分布情形），重点讲透应用条件（$np \ge 5$、$n(1-p) \ge 5$）与连续性修正，最后给出完整例题。

## 1. 直观理解：大数定律 vs 中心极限定理

- **大数定律**（上一篇）：$\bar{X}_n$ **收敛到哪**——样本均值收敛于 $\mu$（一个点）；
- **中心极限定理**（本篇）：$\bar{X}_n$ **怎么波动**——围绕 $\mu$ 的波动幅度服从正态分布（一个形状）。

中心极限定理是大数定律的"精细版"：大数定律只知道"越来越接近 $\mu$"，CLT 还告诉我们"接近的程度服从什么分布"，从而可以**计算具体概率**。

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

## 5. 中心极限定理的应用

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

## 9. 一句话记忆

中心极限定理回答"怎么波动"：独立同分布变量的和（均值）在 $n$ 大时近似正态——$\sum X_i \sim N(n\mu, n\sigma^2)$、$\bar{X} \sim N(\mu, \sigma^2/n)$；二项分布近似正态要满足 $np \ge 5$ 与 $n(1-p) \ge 5$，并记得用 $\pm 0.5$ 连续性修正。
