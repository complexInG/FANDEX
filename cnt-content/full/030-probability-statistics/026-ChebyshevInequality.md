---
order: 50
title: 切比雪夫不等式
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 切比雪夫不等式的表述、证明、应用与推广。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/矩与协方差矩阵'
  - 'probability-statistics/数字特征典型例题'
  - 'probability-statistics/大数定律'
  - 'probability-statistics/中心极限定理'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 切比雪夫不等式

### 1.1 定理表述

设随机变量 $X$ 的期望 $E(X) = \mu$ 和方差 $D(X) = \sigma^2$ 都存在，则对任意 $\varepsilon > 0$，有

$$P(|X - \mu| \geq \varepsilon) \leq \frac{\sigma^2}{\varepsilon^2}$$

等价形式：

$$P(|X - \mu| < \varepsilon) \geq 1 - \frac{\sigma^2}{\varepsilon^2}$$

### 1.2 证明

**连续型情形**：

$$P(|X - \mu| \geq \varepsilon) = \int_{|x - \mu| \geq \varepsilon} f(x) \, dx$$

由于在积分区域上 $\dfrac{(x - \mu)^2}{\varepsilon^2} \geq 1$，故

$$\leq \int_{|x - \mu| \geq \varepsilon} \frac{(x - \mu)^2}{\varepsilon^2} f(x) \, dx \leq \frac{1}{\varepsilon^2} \int_{-\infty}^{+\infty} (x - \mu)^2 f(x) \, dx = \frac{\sigma^2}{\varepsilon^2}$$

**离散型情形**类似。

### 1.3 切比雪夫不等式的意义

1. **不需要知道分布**：只需知道期望和方差即可估计概率
2. **普适性**：适用于任何分布
3. **保守性**：给出的上界通常较宽松，实际概率可能远小于上界

## 2. 切比雪夫不等式的应用

### 2.1 估计概率

**例题**：设 $E(X) = 3$，$D(X) = 2$，估计 $P(|X - 3| \geq 4)$。

**解**：

$$P(|X - 3| \geq 4) \leq \frac{2}{16} = \frac{1}{8} = 0.125$$

### 2.2 确定样本量

**例题**：设 $X_1, X_2, \cdots, X_n$ 独立同分布，$E(X_i) = \mu$，$D(X_i) = \sigma^2$，要使 $P(|\bar{X} - \mu| < 0.5) \geq 0.95$，$n$ 至少为多少？

**解**：$E(\bar{X}) = \mu$，$D(\bar{X}) = \dfrac{\sigma^2}{n}$。

$$P(|\bar{X} - \mu| < 0.5) \geq 1 - \frac{\sigma^2/n}{0.25} = 1 - \frac{4\sigma^2}{n}$$

要求 $1 - \dfrac{4\sigma^2}{n} \geq 0.95$，即 $\dfrac{4\sigma^2}{n} \leq 0.05$，$n \geq 80\sigma^2$。

### 2.3 证明估计的相合性

设 $\hat{\theta}_n$ 是参数 $\theta$ 的估计量，若 $E(\hat{\theta}_n) = \theta$ 且 $D(\hat{\theta}_n) \to 0$（$n \to \infty$），则由切比雪夫不等式：

$$P(|\hat{\theta}_n - \theta| \geq \varepsilon) \leq \frac{D(\hat{\theta}_n)}{\varepsilon^2} \to 0$$

即 $\hat{\theta}_n$ 是 $\theta$ 的相合估计。

## 3. 切比雪夫不等式的推广

### 3.1 马尔可夫不等式

设 $X$ 是非负随机变量，$E(X)$ 存在，则对任意 $\varepsilon > 0$，

$$P(X \geq \varepsilon) \leq \frac{E(X)}{\varepsilon}$$

切比雪夫不等式是马尔可夫不等式的推论（令 $X = (Y - E(Y))^2$）。

### 3.2 单边切比雪夫不等式

设 $E(X) = \mu$，$D(X) = \sigma^2$，则对任意 $a > 0$，

$$P(X - \mu \geq a) \leq \frac{\sigma^2}{\sigma^2 + a^2}$$

### 3.3 多维切比雪夫不等式

设 $\mathbf{X}$ 为 $n$ 维随机向量，$E(\mathbf{X}) = \boldsymbol{\mu}$，协方差矩阵为 $\boldsymbol{\Sigma}$，则对任意 $\varepsilon > 0$，

$$P\left((\mathbf{X} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{X} - \boldsymbol{\mu}) \geq \varepsilon\right) \leq \frac{n}{\varepsilon}$$

## 4. 切比雪夫不等式的局限性

### 4.1 保守性

切比雪夫不等式给出的上界通常远大于实际概率。

**例题**：设 $X \sim N(0, 1)$，比较 $P(|X| \geq 2)$ 的实际值与切比雪夫上界。

**解**：

实际值：$P(|X| \geq 2) = 2(1 - \Phi(2)) \approx 2 \times 0.0228 = 0.0456$

切比雪夫上界：$P(|X| \geq 2) \leq \dfrac{1}{4} = 0.25$

上界比实际值大约 5.5 倍。

### 4.2 改进方向

- 当分布已知时，直接计算概率更精确
- 中心极限定理给出更好的渐近估计
- 对于特定分布族，有更精确的不等式

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
| 切比雪夫不等式 | 026-ChebyshevInequality | 本文自身 |
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
