---
order: 22
title: 分布函数
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 分布函数的定义、性质、离散型与连续型随机变量的分布函数。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/离散型随机变量'
  - 'probability-statistics/连续型随机变量'
  - 'probability-statistics/常用分布'
  - 'probability-statistics/随机变量函数的分布'
prerequisites: []
---

## 1. 分布函数的定义

### 1.1 定义

设 $X$ 是一个随机变量，$x$ 是任意实数，函数

$$F(x) = P(X \leq x)$$

称为 $X$ 的**分布函数**（或**累积分布函数**，Cumulative Distribution Function，CDF）。

分布函数完整地描述了随机变量的概率分布规律。

### 1.2 分布函数的意义

分布函数 $F(x)$ 表示随机变量 $X$ 取值不超过 $x$ 的概率。对于任意实数 $x_1 < x_2$：

$$P(x_1 < X \leq x_2) = F(x_2) - F(x_1)$$

因此，知道了分布函数，就能计算 $X$ 落在任意区间内的概率。

## 2. 分布函数的性质

### 2.1 基本性质

1. **单调不减**：若 $x_1 < x_2$，则 $F(x_1) \leq F(x_2)$

2. **有界性**：$0 \leq F(x) \leq 1$

3. **边界值**：

$$F(-\infty) = \lim_{x \to -\infty} F(x) = 0, \quad F(+\infty) = \lim_{x \to +\infty} F(x) = 1$$

4. **右连续**：$F(x^+) = F(x)$，即 $\lim_{t \to x^+} F(t) = F(x)$

### 2.2 由分布函数计算概率

1. $P(X \leq x) = F(x)$

2. $P(X > x) = 1 - F(x)$

3. $P(x_1 < X \leq x_2) = F(x_2) - F(x_1)$

4. $P(X = x) = F(x) - F(x^-)$（$F(x^-)$ 为 $F$ 在 $x$ 处的左极限）

5. $P(X < x) = F(x^-)$

6. $P(x_1 \leq X \leq x_2) = F(x_2) - F(x_1^-)$

7. $P(x_1 < X < x_2) = F(x_2^-) - F(x_1)$

### 2.3 分布函数与概率的对应

分布函数的**跳跃点**对应离散型随机变量的取值点，**跳跃高度**等于该点的概率：

$$P(X = x_0) = F(x_0) - F(x_0^-)$$

- 若 $F$ 在 $x_0$ 处连续，则 $P(X = x_0) = 0$
- 若 $F$ 在 $x_0$ 处有跳跃，则 $P(X = x_0) > 0$

## 3. 离散型随机变量的分布函数

### 3.1 构造方法

设离散型随机变量 $X$ 的分布律为 $P(X = x_k) = p_k$（$k = 1, 2, \cdots$），则

$$F(x) = \sum_{x_k \leq x} p_k$$

### 3.2 特征

离散型随机变量的分布函数是**阶梯函数**：

- 在每个取值点 $x_k$ 处有跳跃，跳跃高度为 $p_k$
- 在相邻取值点之间为常数

### 3.3 示例

设 $X$ 的分布律为：

| $X$ | 0   | 1   | 2   |
| --- | --- | --- | --- |
| $P$ | 0.3 | 0.5 | 0.2 |

则分布函数为：

$$F(x) = \begin{cases} 0, & x < 0 \\ 0.3, & 0 \leq x < 1 \\ 0.8, & 1 \leq x < 2 \\ 1, & x \geq 2 \end{cases}$$

## 4. 连续型随机变量的分布函数

### 4.1 与密度函数的关系

若 $X$ 为连续型随机变量，密度函数为 $f(x)$，则

$$F(x) = \int_{-\infty}^{x} f(t) \, dt$$

且在 $f(x)$ 的连续点处

$$F'(x) = f(x)$$

### 4.2 特征

连续型随机变量的分布函数是**连续函数**，且在密度函数连续处可导。

### 4.3 示例

设 $X \sim U(0, 1)$，则

$$F(x) = \begin{cases} 0, & x < 0 \\ x, & 0 \leq x < 1 \\ 1, & x \geq 1 \end{cases}$$

## 5. 分布函数的判定

### 5.1 判定准则

一个函数 $F(x)$ 是某个随机变量的分布函数，当且仅当满足以下条件：

1. 单调不减
2. $F(-\infty) = 0$，$F(+\infty) = 1$
3. 右连续

### 5.2 常见错误

- 左连续而非右连续的函数不是分布函数
- 不满足单调性的函数不是分布函数
- 极限不为 0 和 1 的函数不是分布函数

## 6. 分布函数的应用

### 6.1 比较随机变量

若 $F_X(x) \geq F_Y(x)$ 对所有 $x$ 成立，则 $X$ **随机小于** $Y$，即 $X$ 倾向于取更小的值。

### 6.2 分位数

设 $F(x)$ 为随机变量 $X$ 的分布函数，对于 $0 < p < 1$，满足

$$F(x_p) = p$$

的 $x_p$ 称为 $X$ 的 **$p$ 分位数**（或**下侧 $p$ 分位数**）。

特别地：

- $x_{0.5}$：中位数
- $x_{0.25}$：下四分位数
- $x_{0.75}$：上四分位数

### 6.3 逆变换法生成随机数

若 $U \sim U(0, 1)$，则 $X = F^{-1}(U)$ 的分布函数为 $F(x)$。

这是利用均匀随机数生成任意分布随机数的基本方法。

**证明**：

$$P(X \leq x) = P(F^{-1}(U) \leq x) = P(U \leq F(x)) = F(x)$$

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
| 分布函数 | 010-DistributionFunction | 本文自身 |
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
