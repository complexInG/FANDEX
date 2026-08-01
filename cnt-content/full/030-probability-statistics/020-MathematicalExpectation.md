---
order: 40
title: 数学期望
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 数学期望的定义、性质、随机变量函数的期望、条件期望。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/和的分布与极值分布'
  - 'probability-statistics/多维随机变量典型例题'
  - 'probability-statistics/方差与标准差'
  - 'probability-statistics/协方差'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 数学期望的定义

### 1.1 离散型随机变量的期望

设离散型随机变量 $X$ 的分布律为 $P(X = x_k) = p_k$（$k = 1, 2, \cdots$），若级数 $\sum_{k=1}^{\infty} |x_k| p_k$ 收敛，则称

$$E(X) = \sum_{k=1}^{\infty} x_k p_k$$

为 $X$ 的**数学期望**（简称**期望**或**均值**）。

> **注意**：要求级数绝对收敛。若 $\sum |x_k| p_k = +\infty$，则称 $X$ 的期望不存在。

### 1.2 连续型随机变量的期望

设连续型随机变量 $X$ 的密度函数为 $f(x)$，若积分 $\int_{-\infty}^{+\infty} |x| f(x) \, dx$ 收敛，则称

$$E(X) = \int_{-\infty}^{+\infty} x f(x) \, dx$$

为 $X$ 的**数学期望**。

### 1.3 期望的直观意义

数学期望是随机变量取值的"加权平均"，权重为各取值的概率。它反映了随机变量取值的**中心位置**。

## 2. 随机变量函数的期望

### 2.1 一维随机变量函数的期望

**离散型**：设 $Y = g(X)$，则

$$E(Y) = E[g(X)] = \sum_{k=1}^{\infty} g(x_k) p_k$$

**连续型**：设 $Y = g(X)$，则

$$E(Y) = E[g(X)] = \int_{-\infty}^{+\infty} g(x) f(x) \, dx$$

> **重要**：不需要先求 $Y$ 的分布，可以直接用 $X$ 的分布计算 $E[g(X)]$。

### 2.2 二维随机变量函数的期望

**离散型**：

$$E[g(X, Y)] = \sum_{i=1}^{\infty} \sum_{j=1}^{\infty} g(x_i, y_j) p_{ij}$$

**连续型**：

$$E[g(X, Y)] = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} g(x, y) f(x, y) \, dx \, dy$$

## 3. 数学期望的性质

### 3.1 基本性质

1. **常数性质**：$E(C) = C$（$C$ 为常数）

2. **线性性质**：$E(aX + b) = aE(X) + b$

3. **可加性**：$E(X + Y) = E(X) + E(Y)$（无论 $X, Y$ 是否独立）

4. **乘法性质**：若 $X$ 与 $Y$ 独立，则 $E(XY) = E(X) \cdot E(Y)$

   > 注意：反之不成立，即 $E(XY) = E(X)E(Y)$ 不能推出 $X$ 与 $Y$ 独立。

5. **推广**：$E\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i E(X_i)$

### 3.2 性质的应用

**例题**：设 $X \sim B(n, p)$，利用性质求 $E(X)$。

**解**：$X$ 可表示为 $n$ 个独立 0-1 变量之和：$X = X_1 + X_2 + \cdots + X_n$，其中 $X_i \sim B(1, p)$，$E(X_i) = p$。

$$E(X) = E(X_1) + E(X_2) + \cdots + E(X_n) = np$$

## 4. 常用分布的期望

| 分布                  | 期望                 |
| --------------------- | -------------------- |
| $B(1, p)$             | $p$                  |
| $B(n, p)$             | $np$                 |
| $P(\lambda)$          | $\lambda$            |
| $G(p)$                | $\dfrac{1}{p}$       |
| $U(a, b)$             | $\dfrac{a+b}{2}$     |
| $\text{Exp}(\lambda)$ | $\dfrac{1}{\lambda}$ |
| $N(\mu, \sigma^2)$    | $\mu$                |

## 5. 条件期望

### 5.1 定义

**离散型**：在 $Y = y_j$ 条件下 $X$ 的条件期望为

$$E(X \mid Y = y_j) = \sum_{i=1}^{\infty} x_i P(X = x_i \mid Y = y_j)$$

**连续型**：在 $Y = y$ 条件下 $X$ 的条件期望为

$$E(X \mid Y = y) = \int_{-\infty}^{+\infty} x f_{X \mid Y}(x \mid y) \, dx$$

### 5.2 全期望公式

$$E(X) = E[E(X \mid Y)]$$

即

$$E(X) = \begin{cases} \sum_{j} E(X \mid Y = y_j) P(Y = y_j), & \text{离散型} \\ \int_{-\infty}^{+\infty} E(X \mid Y = y) f_Y(y) \, dy, & \text{连续型} \end{cases}$$

### 5.3 全期望公式的应用

**例题**：某商店每天的顾客数 $N \sim P(50)$，每位顾客的消费金额 $X_i \sim \text{Exp}(0.01)$（独立同分布），且 $N$ 与 $\{X_i\}$ 独立。求商店每天的总营业额期望。

**解**：设总营业额 $S = \sum_{i=1}^N X_i$。

$$E(S) = E[E(S \mid N)] = E[N \cdot E(X_1)] = E(N) \cdot E(X_1) = 50 \times 100 = 5000$$

## 6. 期望不存在的例子

### 6.1 柯西分布

设 $X$ 的密度为 $f(x) = \dfrac{1}{\pi(1 + x^2)}$，则

$$E(|X|) = \int_{-\infty}^{+\infty} \frac{|x|}{\pi(1+x^2)} \, dx = \frac{2}{\pi} \int_0^{+\infty} \frac{x}{1+x^2} \, dx = +\infty$$

故柯西分布的期望不存在。

### 6.2 期望存在但高阶矩不存在

设 $X$ 的密度为 $f(x) = \dfrac{2}{x^3}$（$x > 1$），则

$$E(X) = \int_1^{+\infty} x \cdot \frac{2}{x^3} \, dx = 2\int_1^{+\infty} \frac{1}{x^2} \, dx = 2$$

但 $E(X^2) = \int_1^{+\infty} x^2 \cdot \frac{2}{x^3} \, dx = 2\int_1^{+\infty} \frac{1}{x} \, dx = +\infty$，二阶矩不存在。

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
| 数学期望 | 020-MathematicalExpectation | 本文自身 |
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
