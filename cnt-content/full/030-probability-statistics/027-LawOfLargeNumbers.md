---
order: 51
title: 大数定律
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 切比雪夫大数定律、伯努利大数定律、辛钦大数定律及其应用。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/数字特征典型例题'
  - 'probability-statistics/切比雪夫不等式'
  - 'probability-statistics/中心极限定理'
  - 'probability-statistics/大数定律与中心极限定理典型例题'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 大数定律的直观理解

大数定律表明：大量独立重复试验中，事件发生的**频率**稳定于其**概率**，随机变量的**算术平均**稳定于其**期望**。

这是概率论的理论基础，也是统计推断的依据。

## 2. 切比雪夫大数定律

### 2.1 定理

设 $X_1, X_2, \cdots$ 为相互独立的随机变量序列，若 $E(X_i) = \mu_i$，$D(X_i) = \sigma_i^2$ 都存在，且方差一致有界，即存在 $C > 0$ 使得 $\sigma_i^2 \leq C$（$i = 1, 2, \cdots$），则对任意 $\varepsilon > 0$，

$$\lim_{n \to \infty} P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i - \frac{1}{n}\sum_{i=1}^n \mu_i\right| < \varepsilon\right) = 1$$

### 2.2 证明

设 $\bar{X}_n = \dfrac{1}{n}\sum_{i=1}^n X_i$，则

$$E(\bar{X}_n) = \frac{1}{n}\sum_{i=1}^n \mu_i, \quad D(\bar{X}_n) = \frac{1}{n^2}\sum_{i=1}^n \sigma_i^2 \leq \frac{C}{n}$$

由切比雪夫不等式：

$$P(|\bar{X}_n - E(\bar{X}_n)| \geq \varepsilon) \leq \frac{D(\bar{X}_n)}{\varepsilon^2} \leq \frac{C}{n\varepsilon^2} \to 0 \quad (n \to \infty)$$

### 2.3 特殊情形

若 $X_1, X_2, \cdots$ 独立同分布，$E(X_i) = \mu$，$D(X_i) = \sigma^2$，则

$$\lim_{n \to \infty} P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i - \mu\right| < \varepsilon\right) = 1$$

即 $\bar{X}_n \xrightarrow{P} \mu$。

## 3. 伯努利大数定律

### 3.1 定理

设 $n_A$ 为 $n$ 次独立试验中事件 $A$ 发生的次数，$p$ 为每次试验中 $A$ 发生的概率，则对任意 $\varepsilon > 0$，

$$\lim_{n \to \infty} P\left(\left|\frac{n_A}{n} - p\right| < \varepsilon\right) = 1$$

### 3.2 证明

设 $X_i$ 为第 $i$ 次试验中 $A$ 是否发生的指示变量，则 $n_A = \sum_{i=1}^n X_i$，$X_i \sim B(1, p)$。

由切比雪夫大数定律（独立同分布情形）即得。

### 3.3 意义

伯努利大数定律表明：**频率稳定于概率**。这是用频率估计概率的理论依据。

## 4. 辛钦大数定律

### 4.1 定理

设 $X_1, X_2, \cdots$ 为独立同分布的随机变量序列，若 $E(X_i) = \mu$ 存在，则对任意 $\varepsilon > 0$，

$$\lim_{n \to \infty} P\left(\left|\frac{1}{n}\sum_{i=1}^n X_i - \mu\right| < \varepsilon\right) = 1$$

### 4.2 与切比雪夫大数定律的区别

- 切比雪夫大数定律要求方差存在且一致有界
- 辛钦大数定律只要求期望存在，不要求方差存在
- 辛钦大数定律要求独立同分布

### 4.3 辛钦大数定律的证明思路

利用特征函数的方法：设 $X_i$ 的特征函数为 $\varphi(t)$，则 $\bar{X}_n$ 的特征函数为

$$\varphi_{\bar{X}_n}(t) = \left[\varphi\left(\frac{t}{n}\right)\right]^n$$

由于 $\varphi(t) = 1 + i\mu t + o(t)$（$t \to 0$），故

$$\varphi_{\bar{X}_n}(t) = \left[1 + \frac{i\mu t}{n} + o\left(\frac{1}{n}\right)\right]^n \to e^{i\mu t}$$

而 $e^{i\mu t}$ 是常数 $\mu$ 的特征函数，由特征函数的连续性定理，$\bar{X}_n \xrightarrow{P} \mu$。

## 5. 收敛性的概念

### 5.1 依概率收敛

设 $X_1, X_2, \cdots$ 为随机变量序列，$X$ 为随机变量，若对任意 $\varepsilon > 0$，

$$\lim_{n \to \infty} P(|X_n - X| < \varepsilon) = 1$$

则称 $X_n$ **依概率收敛**于 $X$，记作 $X_n \xrightarrow{P} X$。

### 5.2 几乎必然收敛

若 $P\left(\lim_{n \to \infty} X_n = X\right) = 1$，则称 $X_n$ **几乎必然收敛**于 $X$，记作 $X_n \xrightarrow{a.s.} X$。

### 5.3 收敛的关系

几乎必然收敛 $\Rightarrow$ 依概率收敛，反之不成立。

大数定律中的收敛是**依概率收敛**（弱大数定律）或**几乎必然收敛**（强大数定律）。

## 6. 大数定律的应用

### 6.1 蒙特卡洛方法

设 $E(g(X)) = I$，由辛钦大数定律：

$$\frac{1}{n}\sum_{i=1}^n g(X_i) \xrightarrow{P} I$$

其中 $X_1, X_2, \cdots$ 独立同分布。这就是蒙特卡洛积分的原理。

### 6.2 经验分布函数

设 $F_n(x) = \dfrac{1}{n}\sum_{i=1}^n I(X_i \leq x)$ 为经验分布函数，由伯努利大数定律：

$$F_n(x) \xrightarrow{P} F(x)$$

### 6.3 统计推断的基础

大数定律保证了样本均值是总体均值的一致估计，这是参数估计的理论基础。

## 参考文献

Khan Academy 统计：https://zh.khanacademy.org/math/statistics-probability
Seeing Theory：https://seeing-theory.brown.edu/
OpenIntro Statistics：https://www.openintro.org/book/os/
StatQuest（B站/YouTube）：https://www.youtube.com/@statquest

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 样本空间与事件 | 001-SampleSpaceAndEvent | 本文的并列主题 |
| 古典概型 | 002-ClassicalProbability | 本文的并列主题 |
| 几何概型 | 003-GeometricProbability | 本文的并列主题 |
| 条件概率 | 004-ConditionalProbability | 本文的并列主题 |
| 贝叶斯公式 | 005-BayesFormula | 本文的并列主题 |
| 事件的独立性 | 006-EventIndependence | 本文的并列主题 |
| 概率基础典型例题 | 007-ProbabilityBasicsExamples | 本文的前置基础 |
| 离散型随机变量 | 008-DiscreteRandomVariable | 本文的并列主题 |
| 连续型随机变量 | 009-ContinuousRandomVariable | 本文的并列主题 |
| 分布函数 | 010-DistributionFunction | 本文的并列主题 |
| 常用分布 | 011-CommonDistributions | 本文的并列主题 |
| 随机变量函数的分布 | 012-DistributionOfRandomVariableFunction | 本文的并列主题 |
| 随机变量典型例题 | 013-RandomVariableExamples | 本文的并列主题 |
| 联合分布 | 014-JointDistribution | 本文的并列主题 |
| 边缘分布 | 015-MarginalDistribution | 本文的并列主题 |
| 条件分布 | 016-ConditionalDistribution | 本文的并列主题 |
| 随机变量的独立性 | 017-RandomVariableIndependence | 本文的并列主题 |
| 和的分布与极值分布 | 018-SumDistributionAndExtremeValueDistribution | 本文的并列主题 |
| 多维随机变量典型例题 | 019-MultivariateRandomVariableExamples | 本文的并列主题 |
| 数学期望 | 020-MathematicalExpectation | 本文的并列主题 |
| 方差与标准差 | 021-VarianceAndStandardDeviation | 本文的并列主题 |
| 协方差 | 022-Covariance | 本文的并列主题 |
| 相关系数 | 023-CorrelationCoefficient | 本文的并列主题 |
| 矩与协方差矩阵 | 024-MomentAndCovarianceMatrix | 本文的并列主题 |
| 数字特征典型例题 | 025-NumericalCharacteristicsExamples | 本文的并列主题 |
| 切比雪夫不等式 | 026-ChebyshevInequality | 本文的并列主题 |
| 大数定律 | 027-LawOfLargeNumbers | 本文自身 |
| 中心极限定理 | 028-CentralLimitTheorem | 本文的并列主题 |
| 大数定律与中心极限定理典型例题 | 029-LLNAndCLTExamples | 本文的并列主题 |
| 随机样本 | 030-RandomSample | 本文的并列主题 |
| 统计量 | 031-Statistic | 本文的并列主题 |
| 三大分布 | 032-ThreeMajorDistributions | 本文的并列主题 |
| 正态总体的抽样分布 | 033-NormalPopulationSamplingDistribution | 本文的并列主题 |
| 抽样分布典型例题 | 034-SamplingDistributionExamples | 本文的并列主题 |
| 点估计 | 035-PointEstimation | 本文的并列主题 |
| 估计量的评选标准 | 036-EstimatorSelectionCriteria | 本文的并列主题 |
| 区间估计 | 037-IntervalEstimation | 本文的并列主题 |
| 正态总体参数的区间估计 | 038-NormalPopulationParameterIntervalEstimation | 本文的并列主题 |
| 参数估计典型例题 | 039-ParameterEstimationExamples | 本文的并列主题 |
| 假设检验基本概念 | 040-HypothesisTestingBasics | 本文的并列主题 |
| Z检验 | 041-ZTest | 本文的并列主题 |
| t检验 | 042-TTest | 本文的并列主题 |
| 卡方检验 | 043-ChiSquareTest | 本文的并列主题 |
| F检验 | 044-FTest | 本文的并列主题 |
| 假设检验典型例题 | 045-HypothesisTestingExamples | 本文的并列主题 |
