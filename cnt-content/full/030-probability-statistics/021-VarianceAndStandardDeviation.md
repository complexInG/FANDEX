---
order: 41
title: 方差与标准差
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 方差与标准差的定义、性质、常用分布的方差、切比雪夫不等式。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/多维随机变量典型例题'
  - 'probability-statistics/数学期望'
  - 'probability-statistics/协方差'
  - 'probability-statistics/相关系数'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 方差的定义

### 1.1 定义

设 $X$ 是随机变量，若 $E[X - E(X)]^2$ 存在，则称

$$D(X) = \text{Var}(X) = E[X - E(X)]^2$$

为 $X$ 的**方差**。

### 1.2 方差的计算公式

$$D(X) = E[X - E(X)]^2 = E(X^2) - [E(X)]^2$$

这是最常用的方差计算公式。

**推导**：

$$D(X) = E[X - E(X)]^2 = E[X^2 - 2XE(X) + E(X)^2] = E(X^2) - 2E(X) \cdot E(X) + E(X)^2 = E(X^2) - [E(X)]^2$$

### 1.3 离散型与连续型的计算

**离散型**：

$$D(X) = \sum_{k=1}^{\infty} [x_k - E(X)]^2 p_k = \sum_{k=1}^{\infty} x_k^2 p_k - [E(X)]^2$$

**连续型**：

$$D(X) = \int_{-\infty}^{+\infty} [x - E(X)]^2 f(x) \, dx = \int_{-\infty}^{+\infty} x^2 f(x) \, dx - [E(X)]^2$$

## 2. 标准差

### 2.1 定义

方差的算术平方根称为**标准差**（或**均方差**）：

$$\sigma(X) = \sqrt{D(X)}$$

### 2.2 标准差的意义

标准差与 $X$ 具有相同的量纲，更便于实际解释。它衡量了随机变量取值偏离均值的**平均程度**。

## 3. 方差的性质

### 3.1 基本性质

1. **非负性**：$D(X) \geq 0$，且 $D(X) = 0 \iff P(X = C) = 1$

2. **常数方差**：$D(C) = 0$

3. **线性变换**：$D(aX + b) = a^2 D(X)$

4. **独立可加性**：若 $X$ 与 $Y$ 独立，则 $D(X \pm Y) = D(X) + D(Y)$

5. **一般公式**：$D(X \pm Y) = D(X) + D(Y) \mp 2\text{Cov}(X, Y)$

6. **标准化**：若 $D(X) > 0$，则 $D\left(\dfrac{X - E(X)}{\sqrt{D(X)}}\right) = 1$

### 3.2 性质的证明

**性质3**：$D(aX + b) = E[(aX + b) - E(aX + b)]^2 = E[aX - aE(X)]^2 = a^2 E[X - E(X)]^2 = a^2 D(X)$

**性质4**：$D(X + Y) = E[(X+Y)^2] - [E(X+Y)]^2$

$= E(X^2) + 2E(XY) + E(Y^2) - [E(X)]^2 - 2E(X)E(Y) - [E(Y)]^2$

当 $X$ 与 $Y$ 独立时，$E(XY) = E(X)E(Y)$，故

$D(X + Y) = E(X^2) - [E(X)]^2 + E(Y^2) - [E(Y)]^2 = D(X) + D(Y)$

## 4. 常用分布的方差

### 4.1 方差推导示例

**二项分布** $B(n, p)$：

$X = X_1 + X_2 + \cdots + X_n$，$X_i$ 独立同分布，$X_i \sim B(1, p)$。

$D(X_i) = E(X_i^2) - [E(X_i)]^2 = p - p^2 = p(1-p)$

$D(X) = np(1-p)$

**泊松分布** $P(\lambda)$：

$E(X^2) = \sum_{k=0}^{\infty} k^2 \cdot \frac{\lambda^k e^{-\lambda}}{k!} = \lambda(\lambda + 1)$

$D(X) = E(X^2) - [E(X)]^2 = \lambda(\lambda + 1) - \lambda^2 = \lambda$

**均匀分布** $U(a, b)$：

$E(X^2) = \int_a^b \frac{x^2}{b-a} dx = \frac{a^2 + ab + b^2}{3}$

$D(X) = \frac{a^2 + ab + b^2}{3} - \left(\frac{a+b}{2}\right)^2 = \frac{(b-a)^2}{12}$

**指数分布** $\text{Exp}(\lambda)$：

$E(X^2) = \int_0^{+\infty} x^2 \lambda e^{-\lambda x} dx = \frac{2}{\lambda^2}$

$D(X) = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$

**正态分布** $N(\mu, \sigma^2)$：

$D(X) = \sigma^2$

### 4.2 常用分布的方差汇总

| 分布                  | 期望                 | 方差                   |
| --------------------- | -------------------- | ---------------------- |
| $B(1, p)$             | $p$                  | $p(1-p)$               |
| $B(n, p)$             | $np$                 | $np(1-p)$              |
| $P(\lambda)$          | $\lambda$            | $\lambda$              |
| $G(p)$                | $\dfrac{1}{p}$       | $\dfrac{1-p}{p^2}$     |
| $U(a, b)$             | $\dfrac{a+b}{2}$     | $\dfrac{(b-a)^2}{12}$  |
| $\text{Exp}(\lambda)$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ |
| $N(\mu, \sigma^2)$    | $\mu$                | $\sigma^2$             |

## 5. 变异系数

### 5.1 定义

$$C_V = \frac{\sqrt{D(X)}}{E(X)} = \frac{\sigma}{\mu}$$

称为**变异系数**（或**离散系数**）。

### 5.2 意义

变异系数消除了量纲和均值大小的影响，可以比较不同量纲或不同均值水平的随机变量的离散程度。

## 6. 方差的应用

### 6.1 风险度量

在金融中，方差常作为投资风险的度量。方差越大，收益的不确定性越高。

### 6.2 精度评估

在测量和统计中，方差反映了估计的精度。方差越小，估计越精确。

### 6.3 投资组合

设两种资产的收益率分别为 $X$ 和 $Y$，权重为 $w$ 和 $1-w$，则组合收益 $R = wX + (1-w)Y$ 的方差为

$$D(R) = w^2 D(X) + (1-w)^2 D(Y) + 2w(1-w)\text{Cov}(X, Y)$$

通过选择适当的权重，可以在给定期望收益下最小化方差（马科维茨投资组合理论）。

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
| 方差与标准差 | 021-VarianceAndStandardDeviation | 本文自身 |
| 协方差 | 022-Covariance | 本文的并列主题 |
| 相关系数 | 023-CorrelationCoefficient | 本文的并列主题 |
| 矩与协方差矩阵 | 024-MomentAndCovarianceMatrix | 本文的并列主题 |
| 数字特征典型例题 | 025-NumericalCharacteristicsExamples | 本文的并列主题 |
| 切比雪夫不等式 | 026-ChebyshevInequality | 本文的并列主题 |
| 大数定律 | 027-LawOfLargeNumbers | 本文的并列主题 |
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
