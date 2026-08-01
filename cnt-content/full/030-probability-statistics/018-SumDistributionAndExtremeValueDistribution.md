---
order: 34
title: 和的分布与极值分布
module: 'probability-statistics'
category: 'comp-sci'
difficulty: advanced
description: 随机变量和的分布（卷积公式）、最大值与最小值分布、商的分布。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/条件分布'
  - 'probability-statistics/随机变量的独立性'
  - 'probability-statistics/多维随机变量典型例题'
  - 'probability-statistics/数学期望'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 随机变量和的分布

### 1.1 离散型情形

设 $X$ 和 $Y$ 为独立离散型随机变量，分布律分别为 $P(X = x_i)$ 和 $P(Y = y_j)$，则 $Z = X + Y$ 的分布律为

$$P(Z = z_k) = \sum_{x_i + y_j = z_k} P(X = x_i) P(Y = y_j) = \sum_i P(X = x_i) P(Y = z_k - x_i)$$

### 1.2 连续型情形——卷积公式

设 $X$ 和 $Y$ 为独立连续型随机变量，密度函数分别为 $f_X(x)$ 和 $f_Y(y)$，则 $Z = X + Y$ 的密度函数为

$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(z - x) \, dx = \int_{-\infty}^{+\infty} f_X(z - y) f_Y(y) \, dy$$

这称为**卷积公式**，记作 $f_Z = f_X * f_Y$。

### 1.3 卷积公式的推导

$$F_Z(z) = P(X + Y \leq z) = \iint_{x + y \leq z} f_X(x) f_Y(y) \, dx \, dy = \int_{-\infty}^{+\infty} f_X(x) \left[\int_{-\infty}^{z-x} f_Y(y) \, dy\right] dx$$

$$= \int_{-\infty}^{+\infty} f_X(x) F_Y(z - x) \, dx$$

$$f_Z(z) = \frac{d}{dz} F_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(z - x) \, dx$$

### 1.4 卷积公式的应用

**例题**：设 $X \sim N(\mu_1, \sigma_1^2)$，$Y \sim N(\mu_2, \sigma_2^2)$，且 $X$ 与 $Y$ 独立，求 $Z = X + Y$ 的分布。

**解**：利用卷积公式可以证明 $Z \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$。

更一般地，若 $X_1, X_2, \cdots, X_n$ 相互独立，$X_i \sim N(\mu_i, \sigma_i^2)$，则

$$\sum_{i=1}^n a_i X_i \sim N\left(\sum_{i=1}^n a_i \mu_i, \sum_{i=1}^n a_i^2 \sigma_i^2\right)$$

**例题**：设 $X \sim \text{Exp}(\lambda_1)$，$Y \sim \text{Exp}(\lambda_2)$，且 $X$ 与 $Y$ 独立（$\lambda_1 \neq \lambda_2$），求 $Z = X + Y$ 的密度。

**解**：

$$f_Z(z) = \int_0^z \lambda_1 e^{-\lambda_1 x} \cdot \lambda_2 e^{-\lambda_2(z-x)} \, dx = \lambda_1 \lambda_2 e^{-\lambda_2 z} \int_0^z e^{(\lambda_2 - \lambda_1)x} \, dx$$

$$= \lambda_1 \lambda_2 e^{-\lambda_2 z} \cdot \frac{e^{(\lambda_2 - \lambda_1)z} - 1}{\lambda_2 - \lambda_1} = \frac{\lambda_1 \lambda_2}{\lambda_2 - \lambda_1}(e^{-\lambda_1 z} - e^{-\lambda_2 z}), \quad z > 0$$

当 $\lambda_1 = \lambda_2 = \lambda$ 时，$Z \sim \Gamma(2, \lambda)$。

## 2. 随机变量差的分布

设 $X$ 和 $Y$ 独立，$Z = X - Y$，则

$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(x - z) \, dx = \int_{-\infty}^{+\infty} f_X(y + z) f_Y(y) \, dy$$

## 3. 随机变量商的分布

### 3.1 商的密度公式

设 $X$ 和 $Y$ 为独立连续型随机变量，$Z = \dfrac{X}{Y}$，则

$$f_Z(z) = \int_{-\infty}^{+\infty} |y| f_X(zy) f_Y(y) \, dy$$

### 3.2 推导

$$F_Z(z) = P\left(\frac{X}{Y} \leq z\right) = \iint_{x/y \leq z} f_X(x) f_Y(y) \, dx \, dy$$

$$= \int_0^{+\infty} F_X(zy) f_Y(y) \, dy + \int_{-\infty}^0 [1 - F_X(zy)] f_Y(y) \, dy$$

对 $z$ 求导即得商的密度公式。

## 4. 最大值分布

### 4.1 公式

设 $X_1, X_2, \cdots, X_n$ 相互独立，分布函数分别为 $F_1, F_2, \cdots, F_n$，则 $M = \max(X_1, X_2, \cdots, X_n)$ 的分布函数为

$$F_M(x) = P(M \leq x) = P(X_1 \leq x, X_2 \leq x, \cdots, X_n \leq x) = \prod_{i=1}^n F_i(x)$$

若 $X_1, X_2, \cdots, X_n$ 独立同分布，分布函数为 $F(x)$，则

$$F_M(x) = [F(x)]^n$$

### 4.2 密度函数

若 $X_1, X_2, \cdots, X_n$ 独立同分布，密度为 $f(x)$，则

$$f_M(x) = n[F(x)]^{n-1} f(x)$$

## 5. 最小值分布

### 5.1 公式

设 $X_1, X_2, \cdots, X_n$ 相互独立，分布函数分别为 $F_1, F_2, \cdots, F_n$，则 $N = \min(X_1, X_2, \cdots, X_n)$ 的分布函数为

$$F_N(x) = 1 - P(N > x) = 1 - \prod_{i=1}^n P(X_i > x) = 1 - \prod_{i=1}^n [1 - F_i(x)]$$

若 $X_1, X_2, \cdots, X_n$ 独立同分布，分布函数为 $F(x)$，则

$$F_N(x) = 1 - [1 - F(x)]^n$$

### 5.2 密度函数

若 $X_1, X_2, \cdots, X_n$ 独立同分布，密度为 $f(x)$，则

$$f_N(x) = n[1 - F(x)]^{n-1} f(x)$$

## 6. 极值分布的应用

### 6.1 系统可靠性

**串联系统**：$n$ 个元件串联，系统寿命 $T = \min(T_1, T_2, \cdots, T_n)$

**并联系统**：$n$ 个元件并联，系统寿命 $T = \max(T_1, T_2, \cdots, T_n)$

### 6.2 指数分布的极值

设 $X_1, X_2, \cdots, X_n$ 独立同分布，$X_i \sim \text{Exp}(\lambda)$，则

$$F_{\min}(x) = 1 - e^{-n\lambda x}, \quad x > 0$$

即 $\min(X_1, \cdots, X_n) \sim \text{Exp}(n\lambda)$。

### 6.3 均匀分布的极值

设 $X_1, X_2, \cdots, X_n$ 独立同分布，$X_i \sim U(0, 1)$，则

$$f_{\max}(x) = nx^{n-1}, \quad 0 < x < 1$$

$$f_{\min}(x) = n(1-x)^{n-1}, \quad 0 < x < 1$$

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
| 和的分布与极值分布 | 018-SumDistributionAndExtremeValueDistribution | 本文自身 |
| 多维随机变量典型例题 | 019-MultivariateRandomVariableExamples | 本文的并列主题 |
| 数学期望 | 020-MathematicalExpectation | 本文的并列主题 |
| 方差与标准差 | 021-VarianceAndStandardDeviation | 本文的并列主题 |
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
