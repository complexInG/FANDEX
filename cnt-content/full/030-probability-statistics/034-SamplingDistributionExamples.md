---
order: 64
title: 抽样分布典型例题
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 抽样分布部分的典型例题精选，涵盖统计量、三大分布、正态总体抽样分布。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/三大分布'
  - 'probability-statistics/正态总体的抽样分布'
  - 'probability-statistics/点估计'
  - 'probability-statistics/估计量的评选标准'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 统计量

### 例题1

设 $X_1, X_2, \cdots, X_n$ 为来自总体 $X$ 的样本，$E(X) = \mu$，$D(X) = \sigma^2$，求 $E(\bar{X})$，$D(\bar{X})$ 和 $E(S^2)$。

**解**：

$$E(\bar{X}) = \mu, \quad D(\bar{X}) = \frac{\sigma^2}{n}, \quad E(S^2) = \sigma^2$$

### 例题2

设 $X_1, X_2, \cdots, X_7$ 为来自 $N(0, 1)$ 的样本，求 $E(\bar{X}^2)$ 和 $D(\bar{X}^2)$。

**解**：$\bar{X} \sim N(0, 1/7)$，$\dfrac{\bar{X}}{1/\sqrt{7}} = \sqrt{7}\bar{X} \sim N(0, 1)$。

$$7\bar{X}^2 \sim \chi^2(1)$$

$$E(\bar{X}^2) = D(\bar{X}) + [E(\bar{X})]^2 = \frac{1}{7}$$

$$D(\bar{X}^2) = D\left(\frac{\chi^2(1)}{7}\right) = \frac{2}{49}$$

### 例题3

设 $X_1, X_2, \cdots, X_n$ 为来自 $N(\mu, \sigma^2)$ 的样本，$\bar{X}$ 和 $S^2$ 分别为样本均值和样本方差，求 $E(\bar{X}^2)$。

**解**：

$$E(\bar{X}^2) = D(\bar{X}) + [E(\bar{X})]^2 = \frac{\sigma^2}{n} + \mu^2$$

## 2. χ² 分布

### 例题4

设 $X_1, X_2, \cdots, X_6$ 为来自 $N(0, 4)$ 的样本，求 $a$ 使得 $P\left(\sum_{i=1}^6 X_i^2 > a\right) = 0.05$。

**解**：$\dfrac{X_i}{2} \sim N(0, 1)$，$\sum_{i=1}^6 \dfrac{X_i^2}{4} = \dfrac{1}{4}\sum_{i=1}^6 X_i^2 \sim \chi^2(6)$。

$$P\left(\sum_{i=1}^6 X_i^2 > a\right) = P\left(\frac{1}{4}\sum_{i=1}^6 X_i^2 > \frac{a}{4}\right) = 0.05$$

$$\frac{a}{4} = \chi^2_{0.05}(6) = 12.592$$

$$a = 50.368$$

### 例题5

设 $X_1, X_2, \cdots, X_{10}$ 为来自 $N(\mu, \sigma^2)$ 的样本，求 $P\left(\dfrac{S^2}{\sigma^2} > 2\right)$。

**解**：$\dfrac{9S^2}{\sigma^2} \sim \chi^2(9)$。

$$P\left(\frac{S^2}{\sigma^2} > 2\right) = P\left(\frac{9S^2}{\sigma^2} > 18\right)$$

查 $\chi^2$ 分布表，$\chi^2_{0.05}(9) = 16.919$，$\chi^2_{0.025}(9) = 19.023$。

$P(\chi^2(9) > 18) \approx 0.035$。

## 3. t 分布

### 例题6

设 $X_1, X_2, \cdots, X_9$ 为来自 $N(\mu, 4)$ 的样本，求 $P(|\bar{X} - \mu| < 1)$。

**解**：$\sigma = 2$ 已知，$\dfrac{\bar{X} - \mu}{2/3} \sim N(0, 1)$。

$$P(|\bar{X} - \mu| < 1) = P\left(\left|\frac{\bar{X} - \mu}{2/3}\right| < 1.5\right) = 2\Phi(1.5) - 1 = 2 \times 0.9332 - 1 = 0.8664$$

### 例题7

设 $X_1, X_2, \cdots, X_{16}$ 为来自 $N(\mu, \sigma^2)$ 的样本（$\sigma$ 未知），求 $P(|\bar{X} - \mu| < 0.5S)$。

**解**：$T = \dfrac{\bar{X} - \mu}{S/4} \sim t(15)$。

$$P(|\bar{X} - \mu| < 0.5S) = P\left(\left|\frac{\bar{X} - \mu}{S/4}\right| < 2\right) = P(|T| < 2)$$

查 $t$ 分布表，$t_{0.025}(15) = 2.131$，$t_{0.05}(15) = 1.753$。

$P(|T| < 2) \approx 2 \times 0.965 - 1 = 0.93$（近似值）。

### 例题8

设 $X_1, X_2, X_3, X_4$ 为来自 $N(0, 1)$ 的样本，求 $a$ 和 $b$ 使得 $Y = a(X_1 - X_2)^2 + b(X_3 + X_4)^2 \sim \chi^2(2)$。

**解**：$X_1 - X_2 \sim N(0, 2)$，$\dfrac{X_1 - X_2}{\sqrt{2}} \sim N(0, 1)$，$(X_1 - X_2)^2/2 \sim \chi^2(1)$。

$X_3 + X_4 \sim N(0, 2)$，$(X_3 + X_4)^2/2 \sim \chi^2(1)$。

两者独立，故 $Y = \dfrac{(X_1 - X_2)^2}{2} + \dfrac{(X_3 + X_4)^2}{2} \sim \chi^2(2)$。

$a = b = \dfrac{1}{2}$。

## 4. F 分布

### 例题9

设 $X_1, \cdots, X_8$ 和 $Y_1, \cdots, Y_{10}$ 分别来自 $N(\mu_1, \sigma^2)$ 和 $N(\mu_2, \sigma^2)$，求 $P(S_1^2 > 2S_2^2)$。

**解**：$\dfrac{S_1^2}{S_2^2} \sim F(7, 9)$。

$$P(S_1^2 > 2S_2^2) = P\left(\frac{S_1^2}{S_2^2} > 2\right) = P(F(7, 9) > 2)$$

查 $F$ 分布表，$F_{0.10}(7, 9) = 2.51$，$F_{0.25}(7, 9) = 1.57$。

$P(F(7, 9) > 2) \approx 0.15$（近似值）。

### 例题10

设 $X_1, \cdots, X_5$ 和 $Y_1, \cdots, Y_6$ 分别来自 $N(0, \sigma_1^2)$ 和 $N(0, \sigma_2^2)$，求 $\dfrac{\sum X_i^2 / 5\sigma_1^2}{\sum Y_i^2 / 6\sigma_2^2}$ 的分布。

**解**：$\dfrac{\sum_{i=1}^5 X_i^2}{\sigma_1^2} \sim \chi^2(5)$，$\dfrac{\sum_{j=1}^6 Y_j^2}{\sigma_2^2} \sim \chi^2(6)$。

$$\frac{\sum X_i^2 / 5\sigma_1^2}{\sum Y_i^2 / 6\sigma_2^2} = \frac{\chi^2(5)/5}{\chi^2(6)/6} \sim F(5, 6)$$

## 综合题知识点讲解

### 例题11

设 $X_1, \cdots, X_{25}$ 为来自 $N(3, 100)$ 的样本，求 $P(0 < \bar{X} - 3 < 6)$ 和 $P(S^2 > 62.5)$。

**解**：

（1）$\bar{X} \sim N(3, 4)$，$\dfrac{\bar{X} - 3}{2} \sim N(0, 1)$。

$$P(0 < \bar{X} - 3 < 6) = P(0 < Z < 3) = \Phi(3) - \Phi(0) = 0.9987 - 0.5 = 0.4987$$

（2）$\dfrac{24S^2}{100} \sim \chi^2(24)$。

$$P(S^2 > 62.5) = P\left(\frac{24S^2}{100} > 15\right)$$

$\chi^2_{0.90}(24) = 15.659$，故 $P(\chi^2(24) > 15) \approx 0.92$。

### 例题12

设 $X_1, \cdots, X_n$ 为来自 $N(\mu, \sigma^2)$ 的样本，证明 $\bar{X}$ 与 $X_i - \bar{X}$ 不相关。

**证明**：

$$\text{Cov}(\bar{X}, X_i - \bar{X}) = \text{Cov}(\bar{X}, X_i) - \text{Cov}(\bar{X}, \bar{X})$$

$$= \frac{\sigma^2}{n} - \frac{\sigma^2}{n} = 0$$

由于正态分布中不相关等价于独立，故 $\bar{X}$ 与 $X_i - \bar{X}$ 独立。

### 例题13

设 $X_1, \cdots, X_{10}$ 为来自 $N(\mu, \sigma^2)$ 的样本，$S^2$ 为样本方差，已知 $P(S^2 > \sigma^2) = 0.5$，求 $P(S^2 > 2\sigma^2)$。

**解**：$\dfrac{9S^2}{\sigma^2} \sim \chi^2(9)$。

$P(S^2 > \sigma^2) = P(\chi^2(9) > 9) = 0.5$（因为 $\chi^2$ 分布的中位数在自由度附近）。

$P(S^2 > 2\sigma^2) = P(\chi^2(9) > 18)$。

查表：$\chi^2_{0.05}(9) = 16.919$，$\chi^2_{0.025}(9) = 19.023$。

$P(\chi^2(9) > 18) \approx 0.035$。

### 例题14

设 $X_1, \cdots, X_6$ 为来自 $N(0, 1)$ 的样本，求 $Y = \dfrac{X_1 + X_2 + X_3}{\sqrt{X_4^2 + X_5^2 + X_6^2}}$ 的分布。

**解**：$X_1 + X_2 + X_3 \sim N(0, 3)$，$\dfrac{X_1 + X_2 + X_3}{\sqrt{3}} \sim N(0, 1)$。

$X_4^2 + X_5^2 + X_6^2 \sim \chi^2(3)$。

$$Y = \frac{(X_1 + X_2 + X_3)/\sqrt{3}}{\sqrt{(X_4^2 + X_5^2 + X_6^2)/3}} = \frac{N(0,1)}{\sqrt{\chi^2(3)/3}} \sim t(3)$$

### 例题15

设 $X_1, \cdots, X_{20}$ 为来自 $N(0, \sigma^2)$ 的样本，求 $a$ 和 $b$ 使得 $P\left(a < \sum_{i=1}^{20} X_i^2 < b\right) = 0.90$，且 $P\left(\sum_{i=1}^{20} X_i^2 < a\right) = P\left(\sum_{i=1}^{20} X_i^2 > b\right) = 0.05$。

**解**：$\dfrac{1}{\sigma^2}\sum_{i=1}^{20} X_i^2 \sim \chi^2(20)$。

$$a = \sigma^2 \chi^2_{0.95}(20) = \sigma^2 \times 10.851$$

$$b = \sigma^2 \chi^2_{0.05}(20) = \sigma^2 \times 31.410$$

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
| 正态总体的抽样分布 | 033-NormalPopulationSamplingDistribution | 本文的并列主题 |
| 抽样分布典型例题 | 034-SamplingDistributionExamples | 本文自身 |
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
