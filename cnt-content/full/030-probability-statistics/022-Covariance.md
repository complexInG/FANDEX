---
order: 42
title: 协方差
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 协方差的定义、性质、计算方法与协方差矩阵。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/数学期望'
  - 'probability-statistics/方差与标准差'
  - 'probability-statistics/相关系数'
  - 'probability-statistics/矩与协方差矩阵'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 协方差的定义

### 1.1 定义

设 $X$ 和 $Y$ 是两个随机变量，若 $E[X - E(X)][Y - E(Y)]$ 存在，则称

$$\text{Cov}(X, Y) = E[X - E(X)][Y - E(Y)]$$

为 $X$ 与 $Y$ 的**协方差**。

### 1.2 协方差的计算公式

$$\text{Cov}(X, Y) = E(XY) - E(X)E(Y)$$

**证明**：

$$\text{Cov}(X, Y) = E[X - E(X)][Y - E(Y)] = E[XY - XE(Y) - YE(X) + E(X)E(Y)]$$

$$= E(XY) - E(X)E(Y) - E(Y)E(X) + E(X)E(Y) = E(XY) - E(X)E(Y)$$

### 1.3 协方差的直观意义

协方差衡量了两个随机变量的**线性相关程度**：

- $\text{Cov}(X, Y) > 0$：$X$ 与 $Y$ 正相关（$X$ 增大时 $Y$ 倾向于增大）
- $\text{Cov}(X, Y) < 0$：$X$ 与 $Y$ 负相关（$X$ 增大时 $Y$ 倾向于减小）
- $\text{Cov}(X, Y) = 0$：$X$ 与 $Y$ 不相关（无线性关系）

## 2. 协方差的性质

### 2.1 基本性质

1. **对称性**：$\text{Cov}(X, Y) = \text{Cov}(Y, X)$

2. **自身协方差**：$\text{Cov}(X, X) = D(X)$

3. **常数**：$\text{Cov}(X, C) = 0$（$C$ 为常数）

4. **线性性**：

$$\text{Cov}(aX, bY) = ab \cdot \text{Cov}(X, Y)$$

$$\text{Cov}(X_1 + X_2, Y) = \text{Cov}(X_1, Y) + \text{Cov}(X_2, Y)$$

5. **更一般的双线性性**：

$$\text{Cov}\left(\sum_{i=1}^m a_i X_i, \sum_{j=1}^n b_j Y_j\right) = \sum_{i=1}^m \sum_{j=1}^n a_i b_j \text{Cov}(X_i, Y_j)$$

6. **方差与协方差的关系**：

$$D(X \pm Y) = D(X) + D(Y) \pm 2\text{Cov}(X, Y)$$

$$D\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n D(X_i) + 2\sum_{i < j} \text{Cov}(X_i, X_j)$$

7. **独立性推论**：若 $X$ 与 $Y$ 独立，则 $\text{Cov}(X, Y) = 0$

   > 注意：反之不成立，$\text{Cov}(X, Y) = 0$ 不能推出 $X$ 与 $Y$ 独立。

### 2.2 协方差的界

$$|\text{Cov}(X, Y)| \leq \sqrt{D(X) \cdot D(Y)}$$

这由柯西-施瓦茨不等式直接得到。

## 3. 协方差的计算

### 3.1 离散型

$$\text{Cov}(X, Y) = \sum_{i=1}^{\infty} \sum_{j=1}^{\infty} [x_i - E(X)][y_j - E(Y)] p_{ij}$$

或

$$\text{Cov}(X, Y) = \sum_{i=1}^{\infty} \sum_{j=1}^{\infty} x_i y_j p_{ij} - E(X)E(Y)$$

### 3.2 连续型

$$\text{Cov}(X, Y) = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} [x - E(X)][y - E(Y)] f(x, y) \, dx \, dy$$

或

$$\text{Cov}(X, Y) = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} xy f(x, y) \, dx \, dy - E(X)E(Y)$$

### 3.3 计算示例

**例题**：设 $(X, Y)$ 的联合密度为

$$f(x, y) = \begin{cases} 2, & 0 < y < x < 1 \\ 0, & \text{其他} \end{cases}$$

求 $\text{Cov}(X, Y)$。

**解**：

$$E(X) = \int_0^1 \int_0^x 2x \, dy \, dx = \int_0^1 2x^2 \, dx = \frac{2}{3}$$

$$E(Y) = \int_0^1 \int_y^1 2y \, dx \, dy = \int_0^1 2y(1-y) \, dy = \frac{1}{3}$$

$$E(XY) = \int_0^1 \int_0^x 2xy \, dy \, dx = \int_0^1 2x \cdot \frac{x^2}{2} \, dx = \int_0^1 x^3 \, dx = \frac{1}{4}$$

$$\text{Cov}(X, Y) = E(XY) - E(X)E(Y) = \frac{1}{4} - \frac{2}{3} \times \frac{1}{3} = \frac{1}{4} - \frac{2}{9} = \frac{1}{36}$$

## 4. 不相关与独立

### 4.1 不相关的定义

若 $\text{Cov}(X, Y) = 0$，即 $E(XY) = E(X)E(Y)$，则称 $X$ 与 $Y$ **不相关**。

### 4.2 不相关与独立的关系

- 独立 $\Rightarrow$ 不相关
- 不相关 $\not\Rightarrow$ 独立

### 4.3 不相关但非独立的例子

设 $X \sim U(-1, 1)$，$Y = X^2$，则

$$E(X) = 0, \quad E(XY) = E(X^3) = 0$$

$$\text{Cov}(X, Y) = E(XY) - E(X)E(Y) = 0 - 0 = 0$$

$X$ 与 $Y$ 不相关，但 $Y = X^2$，显然 $X$ 与 $Y$ 不独立。

### 4.4 特殊情况：二维正态分布

对于 $(X, Y) \sim N(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$：

$$X \text{ 与 } Y \text{ 不相关} \iff X \text{ 与 } Y \text{ 独立} \iff \rho = 0$$

这是二维正态分布的特殊性质，一般分布不具备。

## 5. 协方差的应用

### 5.1 投资组合风险

$$D(wX + (1-w)Y) = w^2 D(X) + (1-w)^2 D(Y) + 2w(1-w)\text{Cov}(X, Y)$$

当 $\text{Cov}(X, Y) < 0$ 时，可以通过分散投资降低风险。

### 5.2 回归分析

协方差是回归分析的基础，最小二乘回归系数为

$$\beta = \frac{\text{Cov}(X, Y)}{D(X)}$$

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
| 协方差 | 022-Covariance | 本文自身 |
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
