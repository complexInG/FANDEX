---
order: 33
title: 随机变量的独立性
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 二维随机变量独立性的定义、判定方法、独立性的性质与应用。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/边缘分布'
  - 'probability-statistics/条件分布'
  - 'probability-statistics/和的分布与极值分布'
  - 'probability-statistics/多维随机变量典型例题'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 随机变量独立性的定义

### 1.1 定义

设 $(X, Y)$ 是二维随机变量，若对任意实数 $x, y$，都有

$$F(x, y) = F_X(x) \cdot F_Y(y)$$

即

$$P(X \leq x, Y \leq y) = P(X \leq x) \cdot P(Y \leq y)$$

则称随机变量 $X$ 与 $Y$ **相互独立**。

### 1.2 等价定义

**离散型**：$X$ 与 $Y$ 独立 $\iff$ 对所有 $i, j$，

$$P(X = x_i, Y = y_j) = P(X = x_i) \cdot P(Y = y_j)$$

即 $p_{ij} = p_{i\cdot} \cdot p_{\cdot j}$

**连续型**：$X$ 与 $Y$ 独立 $\iff$ 在 $f(x, y)$ 的连续点处，

$$f(x, y) = f_X(x) \cdot f_Y(y)$$

## 2. 独立性的判定方法

### 2.1 定义法

直接验证联合分布等于边缘分布的乘积。

### 2.2 分解法

若联合密度 $f(x, y)$ 可以分解为

$$f(x, y) = g(x) \cdot h(y)$$

其中 $g(x)$ 只与 $x$ 有关，$h(y)$ 只与 $y$ 有关，且 $f(x, y)$ 的非零区域为矩形（即 $x$ 和 $y$ 的取值范围互不依赖），则 $X$ 与 $Y$ 独立。

> **注意**：非零区域必须是矩形区域，否则即使密度可分解，也不独立。

### 2.3 判定步骤

1. 求出联合分布（分布律或密度）
2. 求出边缘分布
3. 检验联合分布是否等于边缘分布的乘积

## 3. 独立性的重要性质

### 3.1 独立变量的函数

若 $X$ 与 $Y$ 独立，则 $g(X)$ 与 $h(Y)$ 也独立，其中 $g$ 和 $h$ 为连续函数。

### 3.2 独立变量的概率

若 $X$ 与 $Y$ 独立，则对任意 Borel 集 $A, B$，

$$P(X \in A, Y \in B) = P(X \in A) \cdot P(Y \in B)$$

### 3.3 独立变量的期望

若 $X$ 与 $Y$ 独立且期望存在，则

$$E(XY) = E(X) \cdot E(Y)$$

### 3.4 独立变量的方差

若 $X$ 与 $Y$ 独立且方差存在，则

$$D(X + Y) = D(X) + D(Y)$$

$$D(X - Y) = D(X) + D(Y)$$

## 4. 独立性判定的典型例题

### 例题1

设 $(X, Y)$ 的联合密度为

$$f(x, y) = \begin{cases} 4xy, & 0 < x < 1, 0 < y < 1 \\ 0, & \text{其他} \end{cases}$$

判断 $X$ 与 $Y$ 是否独立。

**解**：

$$f_X(x) = \int_0^1 4xy \, dy = 2x, \quad 0 < x < 1$$

$$f_Y(y) = \int_0^1 4xy \, dx = 2y, \quad 0 < y < 1$$

$$f_X(x) \cdot f_Y(y) = 4xy = f(x, y) \quad \checkmark$$

且非零区域为矩形，故 $X$ 与 $Y$ 独立。

### 例题2

设 $(X, Y)$ 的联合密度为

$$f(x, y) = \begin{cases} 2, & 0 < x < y < 1 \\ 0, & \text{其他} \end{cases}$$

判断 $X$ 与 $Y$ 是否独立。

**解**：非零区域为三角形 $\{(x, y) : 0 < x < y < 1\}$，不是矩形，故 $X$ 与 $Y$ 不独立。

也可以验证：

$$f_X(x) = 2(1 - x), \quad f_Y(y) = 2y$$

$$f_X(x) \cdot f_Y(y) = 4y(1 - x) \neq 2 = f(x, y)$$

### 例题3

设 $(X, Y) \sim N(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$，证明 $X$ 与 $Y$ 独立 $\iff$ $\rho = 0$。

**证明**：

当 $\rho = 0$ 时，联合密度为

$$f(x, y) = \frac{1}{2\pi\sigma_1\sigma_2} \exp\left\{-\frac{(x-\mu_1)^2}{2\sigma_1^2} - \frac{(y-\mu_2)^2}{2\sigma_2^2}\right\} = f_X(x) \cdot f_Y(y)$$

故 $X$ 与 $Y$ 独立。

当 $X$ 与 $Y$ 独立时，$f(x, y) = f_X(x) \cdot f_Y(y)$，比较联合密度公式可得 $\rho = 0$。

## 5. 多个随机变量的独立性

### 5.1 定义

设 $X_1, X_2, \cdots, X_n$ 是 $n$ 个随机变量，若对任意实数 $x_1, x_2, \cdots, x_n$，有

$$F(x_1, x_2, \cdots, x_n) = F_{X_1}(x_1) \cdot F_{X_2}(x_2) \cdots F_{X_n}(x_n)$$

则称 $X_1, X_2, \cdots, X_n$ **相互独立**。

### 5.2 独立随机变量和的性质

若 $X_1, X_2, \cdots, X_n$ 相互独立，则

1. $D\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n D(X_i)$

2. $D\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 D(X_i)$

3. 独立正态变量的线性组合仍为正态变量

### 5.3 独立与两两独立

- 相互独立 $\Rightarrow$ 两两独立
- 两两独立 $\not\Rightarrow$ 相互独立

这与事件的独立性类似。

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
| 随机变量的独立性 | 017-RandomVariableIndependence | 本文自身 |
| 和的分布与极值分布 | 018-SumDistributionAndExtremeValueDistribution | 本文的并列主题 |
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
