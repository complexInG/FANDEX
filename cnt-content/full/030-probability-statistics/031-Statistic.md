---
order: 61
title: 统计量
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 统计量的定义、样本均值、样本方差、样本矩及常用统计量。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/大数定律与中心极限定理典型例题'
  - 'probability-statistics/随机样本'
  - 'probability-statistics/三大分布'
  - 'probability-statistics/正态总体的抽样分布'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 统计量的定义

### 1.1 定义

设 $X_1, X_2, \cdots, X_n$ 为来自总体 $X$ 的样本，$g(X_1, X_2, \cdots, X_n)$ 是一个 $n$ 元函数，若 $g$ 中不包含任何未知参数，则称 $g(X_1, X_2, \cdots, X_n)$ 为一个**统计量**。

### 1.2 统计量的特点

1. 统计量是样本的函数，不含未知参数
2. 统计量是随机变量
3. 统计量的分布称为**抽样分布**

### 1.3 为什么要求不含未知参数

统计量是用于推断未知参数的，如果统计量本身含有未知参数，就无法从样本数据中计算出统计量的值，也就无法进行推断。

## 2. 样本均值

### 2.1 定义

$$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$$

称为**样本均值**。

### 2.2 样本均值的性质

设 $E(X) = \mu$，$D(X) = \sigma^2$，则：

1. $E(\bar{X}) = \mu$（无偏性）

2. $D(\bar{X}) = \dfrac{\sigma^2}{n}$

3. 由中心极限定理，当 $n$ 较大时，$\bar{X}$ 近似服从 $N\left(\mu, \dfrac{\sigma^2}{n}\right)$

4. 若总体 $X \sim N(\mu, \sigma^2)$，则 $\bar{X} \sim N\left(\mu, \dfrac{\sigma^2}{n}\right)$（精确分布）

### 2.3 样本均值的计算

**未分组数据**：$\bar{x} = \dfrac{1}{n}\sum_{i=1}^n x_i$

**分组数据**：$\bar{x} = \dfrac{\sum_{j=1}^k f_j x_j}{\sum_{j=1}^k f_j}$

其中 $f_j$ 为第 $j$ 组的频数，$x_j$ 为第 $j$ 组的组中值。

## 3. 样本方差

### 3.1 定义

$$S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$$

称为**样本方差**（无偏版本）。

$$S = \sqrt{S^2} = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2}$$

称为**样本标准差**。

### 3.2 为什么除以 $n-1$ 而不是 $n$

$$E(S^2) = E\left[\frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2\right] = \sigma^2$$

除以 $n-1$ 使得 $S^2$ 是 $\sigma^2$ 的**无偏估计**。

若除以 $n$，则 $E\left[\dfrac{1}{n}\sum_{i=1}^n (X_i - \bar{X})^2\right] = \dfrac{n-1}{n}\sigma^2 < \sigma^2$，是有偏的。

### 3.3 样本方差的计算公式

$$S^2 = \frac{1}{n-1}\left(\sum_{i=1}^n X_i^2 - n\bar{X}^2\right) = \frac{n\sum X_i^2 - (\sum X_i)^2}{n(n-1)}$$

### 3.4 样本方差的性质

设 $E(X) = \mu$，$D(X) = \sigma^2$，则：

1. $E(S^2) = \sigma^2$（无偏性）

2. 当总体 $X \sim N(\mu, \sigma^2)$ 时，$\dfrac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$

3. $\bar{X}$ 与 $S^2$ 独立（正态总体时）

## 4. 样本矩

### 4.1 样本 $k$ 阶原点矩

$$A_k = \frac{1}{n}\sum_{i=1}^n X_i^k, \quad k = 1, 2, \cdots$$

特别地，$A_1 = \bar{X}$。

### 4.2 样本 $k$ 阶中心矩

$$B_k = \frac{1}{n}\sum_{i=1}^n (X_i - \bar{X})^k, \quad k = 2, 3, \cdots$$

注意：$B_2 = \dfrac{n-1}{n}S^2$。

### 4.3 样本矩与总体矩的关系

由大数定律，当 $n \to \infty$ 时：

$$A_k \xrightarrow{P} E(X^k) = \mu_k$$

$$B_k \xrightarrow{P} E[X - E(X)]^k = \nu_k$$

## 5. 其他常用统计量

### 5.1 样本极差

$$R = X_{(n)} - X_{(1)} = \max(X_i) - \min(X_i)$$

### 5.2 样本中位数

$$M_e = \begin{cases} X_{\left(\frac{n+1}{2}\right)}, & n \text{ 为奇数} \\ \frac{1}{2}\left[X_{\left(\frac{n}{2}\right)} + X_{\left(\frac{n}{2}+1\right)}\right], & n \text{ 为偶数} \end{cases}$$

### 5.3 样本 $p$ 分位数

$$m_p = \begin{cases} X_{([np]+1)}, & np \text{ 不是整数} \\ \frac{1}{2}(X_{(np)} + X_{(np+1)}), & np \text{ 是整数} \end{cases}$$

### 5.4 变异系数

$$CV = \frac{S}{\bar{X}}$$

### 5.5 偏度与峰度

**样本偏度**：

$$g_1 = \frac{B_3}{B_2^{3/2}}$$

**样本峰度**：

$$g_2 = \frac{B_4}{B_2^2} - 3$$

## 6. 次序统计量

### 6.1 定义

设 $X_1, X_2, \cdots, X_n$ 为样本，将其按从小到大排列为

$$X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}$$

则 $X_{(k)}$ 称为第 $k$ 个**次序统计量**。

### 6.2 次序统计量的分布

设总体 $X$ 的分布函数为 $F(x)$，密度函数为 $f(x)$，则

$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!}[F(x)]^{k-1}[1-F(x)]^{n-k}f(x)$$

特别地：

$$f_{X_{(1)}}(x) = n[1-F(x)]^{n-1}f(x)$$

$$f_{X_{(n)}}(x) = n[F(x)]^{n-1}f(x)$$

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
| 大数定律 | 027-LawOfLargeNumbers | 本文的并列主题 |
| 中心极限定理 | 028-CentralLimitTheorem | 本文的并列主题 |
| 大数定律与中心极限定理典型例题 | 029-LLNAndCLTExamples | 本文的并列主题 |
| 随机样本 | 030-RandomSample | 本文的并列主题 |
| 统计量 | 031-Statistic | 本文自身 |
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
