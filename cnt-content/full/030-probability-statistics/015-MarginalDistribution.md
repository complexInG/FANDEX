---
order: 31
title: 边缘分布
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 边缘分布函数、边缘分布律、边缘概率密度的定义与计算。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/随机变量典型例题'
  - 'probability-statistics/联合分布'
  - 'probability-statistics/条件分布'
  - 'probability-statistics/随机变量的独立性'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 边缘分布函数

### 1.1 定义

设 $(X, Y)$ 的联合分布函数为 $F(x, y)$，则

$$F_X(x) = P(X \leq x) = P(X \leq x, Y < +\infty) = F(x, +\infty) = \lim_{y \to +\infty} F(x, y)$$

$$F_Y(y) = P(Y \leq y) = P(X < +\infty, Y \leq y) = F(+\infty, y) = \lim_{x \to +\infty} F(x, y)$$

分别称为 $(X, Y)$ 关于 $X$ 和关于 $Y$ 的**边缘分布函数**。

### 1.2 边缘分布与联合分布的关系

- 联合分布 $\Rightarrow$ 边缘分布（唯一确定）
- 边缘分布 $\not\Rightarrow$ 联合分布（不唯一确定）

不同的联合分布可以有相同的边缘分布。

## 2. 离散型随机变量的边缘分布

### 2.1 边缘分布律

设 $(X, Y)$ 的联合分布律为 $P(X = x_i, Y = y_j) = p_{ij}$，则

$$P(X = x_i) = \sum_{j=1}^{\infty} p_{ij} = p_{i\cdot}, \quad i = 1, 2, \cdots$$

$$P(Y = y_j) = \sum_{i=1}^{\infty} p_{ij} = p_{\cdot j}, \quad j = 1, 2, \cdots$$

分别称为关于 $X$ 和关于 $Y$ 的**边缘分布律**。

### 2.2 计算方法

在联合分布律表中：

- $X$ 的边缘分布律：将每行求和，写在表的右边
- $Y$ 的边缘分布律：将每列求和，写在表的下边

### 2.3 示例

设 $(X, Y)$ 的联合分布律为：

| $X \backslash Y$ |       1        |       2        |        3        |  $p_{i\cdot}$  |
| :--------------: | :------------: | :------------: | :-------------: | :------------: |
|        1         | $\dfrac{1}{6}$ | $\dfrac{1}{9}$ | $\dfrac{1}{18}$ | $\dfrac{1}{3}$ |
|        2         | $\dfrac{1}{3}$ | $\dfrac{2}{9}$ | $\dfrac{1}{9}$  | $\dfrac{2}{3}$ |
|  $p_{\cdot j}$   | $\dfrac{1}{2}$ | $\dfrac{1}{3}$ | $\dfrac{1}{6}$  |       1        |

$X$ 的边缘分布律：

| $X$ | 1              | 2              |
| --- | -------------- | -------------- |
| $P$ | $\dfrac{1}{3}$ | $\dfrac{2}{3}$ |

$Y$ 的边缘分布律：

| $Y$ | 1              | 2              | 3              |
| --- | -------------- | -------------- | -------------- |
| $P$ | $\dfrac{1}{2}$ | $\dfrac{1}{3}$ | $\dfrac{1}{6}$ |

## 3. 连续型随机变量的边缘分布

### 3.1 边缘概率密度

设 $(X, Y)$ 的联合概率密度为 $f(x, y)$，则

$$f_X(x) = \int_{-\infty}^{+\infty} f(x, y) \, dy$$

$$f_Y(y) = \int_{-\infty}^{+\infty} f(x, y) \, dx$$

分别称为关于 $X$ 和关于 $Y$ 的**边缘概率密度**。

### 3.2 计算要点

1. 确定联合密度 $f(x, y)$ 的非零区域
2. 对 $y$ 积分求 $f_X(x)$ 时，注意 $y$ 的积分范围可能依赖于 $x$
3. 对 $x$ 积分求 $f_Y(y)$ 时，注意 $x$ 的积分范围可能依赖于 $y$

### 3.3 示例

**例题**：设 $(X, Y)$ 的联合密度为

$$f(x, y) = \begin{cases} 2, & 0 < x < y < 1 \\ 0, & \text{其他} \end{cases}$$

求边缘概率密度 $f_X(x)$ 和 $f_Y(y)$。

**解**：

$$f_X(x) = \int_{-\infty}^{+\infty} f(x, y) \, dy = \int_x^1 2 \, dy = 2(1 - x), \quad 0 < x < 1$$

$$f_Y(y) = \int_{-\infty}^{+\infty} f(x, y) \, dx = \int_0^y 2 \, dx = 2y, \quad 0 < y < 1$$

### 3.4 二维正态分布的边缘分布

设 $(X, Y) \sim N(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$，则

$$X \sim N(\mu_1, \sigma_1^2), \quad Y \sim N(\mu_2, \sigma_2^2)$$

边缘分布与参数 $\rho$ 无关，说明不同的联合分布（不同的 $\rho$）可以有相同的边缘分布。

## 4. 边缘分布与联合分布的关系

### 4.1 联合分布确定边缘分布

由联合分布可以唯一确定边缘分布，这是显然的。

### 4.2 边缘分布不能确定联合分布

**反例**：设 $(X, Y)$ 的联合密度为

$$f_1(x, y) = \begin{cases} 4xy, & 0 < x < 1, 0 < y < 1 \\ 0, & \text{其他} \end{cases}$$

$$f_2(x, y) = \begin{cases} 8xy, & 0 < x < y < 1 \\ 0, & \text{其他} \end{cases}$$

可以验证两者关于 $X$ 的边缘密度不同，但如果构造更精巧的例子，可以使得两个不同的联合分布具有相同的边缘分布。

### 4.3 独立时的特殊情况

当 $X$ 与 $Y$ 独立时，联合分布由边缘分布唯一确定：

$$f(x, y) = f_X(x) \cdot f_Y(y)$$

$$P(X = x_i, Y = y_j) = P(X = x_i) \cdot P(Y = y_j)$$

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
| 边缘分布 | 015-MarginalDistribution | 本文自身 |
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
