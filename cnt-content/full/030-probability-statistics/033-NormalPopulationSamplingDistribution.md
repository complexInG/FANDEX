---
order: 63
title: 正态总体的抽样分布
module: 'probability-statistics'
category: 'comp-sci'
difficulty: advanced
description: 单正态总体和双正态总体的抽样分布定理，统计推断的理论基础。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/统计量'
  - 'probability-statistics/三大分布'
  - 'probability-statistics/抽样分布典型例题'
  - 'probability-statistics/点估计'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 单正态总体的抽样分布

### 1.1 基本设定

设 $X_1, X_2, \cdots, X_n$ 为来自正态总体 $N(\mu, \sigma^2)$ 的简单随机样本，$\bar{X}$ 为样本均值，$S^2$ 为样本方差。

### 1.2 样本均值的分布

$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

标准化：

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$

### 1.3 样本方差的分布

$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$$

### 1.4 样本均值与样本方差的独立性

**定理**：$\bar{X}$ 与 $S^2$ 相互独立。

这是正态总体特有的重要性质，非正态总体一般不具备。

### 1.5 t 统计量的分布

$$\frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$$

**推导**：

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1), \quad \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$$

由 $\bar{X}$ 与 $S^2$ 独立：

$$T = \frac{\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}}{\sqrt{\frac{(n-1)S^2}{\sigma^2} / (n-1)}} = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$$

### 1.6 单正态总体抽样分布汇总

| 统计量                                   | 分布          | 条件          |
| ---------------------------------------- | ------------- | ------------- |
| $\dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}}$ | $N(0, 1)$     | $\sigma$ 已知 |
| $\dfrac{(n-1)S^2}{\sigma^2}$             | $\chi^2(n-1)$ | —             |
| $\dfrac{\bar{X} - \mu}{S/\sqrt{n}}$      | $t(n-1)$      | $\sigma$ 未知 |

## 2. 双正态总体的抽样分布

### 2.1 基本设定

设 $X_1, X_2, \cdots, X_{n_1}$ 为来自 $N(\mu_1, \sigma_1^2)$ 的样本，$Y_1, Y_2, \cdots, Y_{n_2}$ 为来自 $N(\mu_2, \sigma_2^2)$ 的样本，两样本独立。

### 2.2 均值差的分布

**$\sigma_1^2, \sigma_2^2$ 已知**：

$$\frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N(0, 1)$$

**$\sigma_1^2 = \sigma_2^2 = \sigma^2$ 未知**：

$$\frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{S_w\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 - 2)$$

其中

$$S_w^2 = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}$$

为**联合方差**（**合并方差**）。

### 2.3 方差比的分布

$$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim F(n_1 - 1, n_2 - 1)$$

特别地，当 $\sigma_1^2 = \sigma_2^2$ 时：

$$\frac{S_1^2}{S_2^2} \sim F(n_1 - 1, n_2 - 1)$$

### 2.4 双正态总体抽样分布汇总

| 统计量                                                                          | 分布             | 条件                          |
| ------------------------------------------------------------------------------- | ---------------- | ----------------------------- |
| $\dfrac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}}$ | $N(0,1)$         | $\sigma_1^2, \sigma_2^2$ 已知 |
| $\dfrac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{S_w\sqrt{1/n_1+1/n_2}}$                | $t(n_1+n_2-2)$   | $\sigma_1^2=\sigma_2^2$ 未知  |
| $\dfrac{S_1^2/S_2^2}{\sigma_1^2/\sigma_2^2}$                                    | $F(n_1-1,n_2-1)$ | —                             |

## 3. 抽样分布的应用

### 3.1 参数估计

抽样分布是构造置信区间的基础：

- $\sigma$ 已知时，用 $Z$ 统计量构造均值的置信区间
- $\sigma$ 未知时，用 $t$ 统计量构造均值的置信区间
- 用 $\chi^2$ 统计量构造方差的置信区间
- 用 $F$ 统计量构造方差比的置信区间

### 3.2 假设检验

抽样分布是确定拒绝域的基础：

- $Z$ 检验：$\sigma$ 已知时的均值检验
- $t$ 检验：$\sigma$ 未知时的均值检验
- $\chi^2$ 检验：方差检验
- $F$ 检验：方差齐性检验

### 3.3 示例

**例题**：设 $X_1, \cdots, X_{16}$ 为来自 $N(\mu, 4)$ 的样本，求 $P(|\bar{X} - \mu| < 0.5)$。

**解**：$\bar{X} \sim N(\mu, 1/4)$，$\dfrac{\bar{X} - \mu}{1/2} \sim N(0, 1)$。

$$P(|\bar{X} - \mu| < 0.5) = P\left(\left|\frac{\bar{X} - \mu}{0.5}\right| < 1\right) = 2\Phi(1) - 1 = 0.6826$$

**例题**：设 $X_1, \cdots, X_{10}$ 为来自 $N(0, \sigma^2)$ 的样本，求 $E(S^2)$ 和 $D(S^2)$。

**解**：$\dfrac{9S^2}{\sigma^2} \sim \chi^2(9)$。

$$E\left(\frac{9S^2}{\sigma^2}\right) = 9 \implies E(S^2) = \sigma^2$$

$$D\left(\frac{9S^2}{\sigma^2}\right) = 18 \implies D(S^2) = \frac{18\sigma^4}{81} = \frac{2\sigma^4}{9}$$

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
| 统计量 | 031-Statistic | 本文的并列主题 |
| 三大分布 | 032-ThreeMajorDistributions | 本文的并列主题 |
| 正态总体的抽样分布 | 033-NormalPopulationSamplingDistribution | 本文自身 |
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
