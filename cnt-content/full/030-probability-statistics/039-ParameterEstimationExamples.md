---
order: 74
title: 参数估计典型例题
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 参数估计部分的典型例题精选，涵盖矩估计、极大似然估计、估计量评价、区间估计。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/区间估计'
  - 'probability-statistics/正态总体参数的区间估计'
  - 'probability-statistics/假设检验基本概念'
  - 'probability-statistics/Z检验'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 矩估计

### 例题1

设总体 $X$ 的密度为 $f(x) = \begin{cases} (\theta + 1)x^\theta, & 0 < x < 1 \\ 0, & \text{其他} \end{cases}$（$\theta > -1$），求 $\theta$ 的矩估计。

**解**：

$$E(X) = \int_0^1 x(\theta+1)x^\theta \, dx = (\theta+1)\int_0^1 x^{\theta+1} \, dx = \frac{\theta+1}{\theta+2}$$

令 $E(X) = \bar{X}$：

$$\frac{\theta+1}{\theta+2} = \bar{X} \implies \hat{\theta} = \frac{2\bar{X} - 1}{1 - \bar{X}}$$

### 例题2

设总体 $X \sim P(\lambda)$，求 $\lambda$ 的矩估计。

**解**：$E(X) = \lambda = \bar{X}$，故 $\hat{\lambda} = \bar{X}$。

### 例题3

设总体 $X$ 的密度为 $f(x) = \begin{cases} \dfrac{1}{\theta}e^{-x/\theta}, & x > 0 \\ 0, & x \leq 0 \end{cases}$，求 $\theta$ 的矩估计。

**解**：$E(X) = \theta$，故 $\hat{\theta} = \bar{X}$。

## 2. 极大似然估计

### 例题4

设总体 $X \sim P(\lambda)$，求 $\lambda$ 的 MLE。

**解**：

$$L(\lambda) = \prod_{i=1}^n \frac{\lambda^{x_i}e^{-\lambda}}{x_i!} = \frac{\lambda^{\sum x_i}e^{-n\lambda}}{\prod x_i!}$$

$$\ln L = \sum x_i \ln\lambda - n\lambda - \sum \ln(x_i!)$$

$$\frac{d\ln L}{d\lambda} = \frac{\sum x_i}{\lambda} - n = 0 \implies \hat{\lambda} = \bar{X}$$

### 例题5

设总体 $X \sim U(a, b)$，求 $a$ 和 $b$ 的 MLE。

**解**：

$$L(a, b) = \begin{cases} \dfrac{1}{(b-a)^n}, & a < x_i < b, i = 1, \cdots, n \\ 0, & \text{其他} \end{cases}$$

$L$ 是 $(b-a)^{-n}$，要使 $L$ 最大，需 $b - a$ 最小。

约束条件：$a \leq x_{(1)}$，$b \geq x_{(n)}$。

故 $\hat{a} = x_{(1)}$，$\hat{b} = x_{(n)}$。

### 例题6

设总体 $X$ 的密度为 $f(x) = \begin{cases} \theta x^{\theta-1}, & 0 < x < 1 \\ 0, & \text{其他} \end{cases}$（$\theta > 0$），求 $\theta$ 的 MLE。

**解**：

$$L(\theta) = \prod_{i=1}^n \theta x_i^{\theta-1} = \theta^n \left(\prod x_i\right)^{\theta-1}$$

$$\ln L = n\ln\theta + (\theta-1)\sum\ln x_i$$

$$\frac{d\ln L}{d\theta} = \frac{n}{\theta} + \sum\ln x_i = 0 \implies \hat{\theta} = -\frac{n}{\sum\ln x_i}$$

## 3. 估计量的评选

### 例题7

设 $X_1, \cdots, X_n \sim N(\mu, \sigma^2)$，证明 $S^2$ 是 $\sigma^2$ 的无偏估计。

**证明**：$\dfrac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$，$E[\chi^2(n-1)] = n-1$。

$$E(S^2) = E\left[\frac{\sigma^2}{n-1} \cdot \frac{(n-1)S^2}{\sigma^2}\right] = \frac{\sigma^2}{n-1} \cdot (n-1) = \sigma^2$$

### 例题8

设 $X_1, \cdots, X_n \sim U(0, \theta)$，$\hat{\theta}_1 = 2\bar{X}$，$\hat{\theta}_2 = X_{(n)}$，判断它们是否为 $\theta$ 的无偏估计。

**解**：

$$E(\hat{\theta}_1) = 2E(\bar{X}) = 2 \cdot \frac{\theta}{2} = \theta \quad \text{（无偏）}$$

$$f_{X_{(n)}}(x) = \frac{n}{\theta^n}x^{n-1}, \quad 0 < x < \theta$$

$$E(\hat{\theta}_2) = \int_0^\theta x \cdot \frac{n}{\theta^n}x^{n-1} \, dx = \frac{n}{n+1}\theta \neq \theta \quad \text{（有偏）}$$

修正：$\hat{\theta}_3 = \dfrac{n+1}{n}X_{(n)}$ 是无偏的。

### 例题9

比较 $\hat{\theta}_1 = 2\bar{X}$ 和 $\hat{\theta}_3 = \dfrac{n+1}{n}X_{(n)}$ 的有效性。

**解**：

$$D(\hat{\theta}_1) = 4D(\bar{X}) = 4 \cdot \frac{\theta^2}{12n} = \frac{\theta^2}{3n}$$

$$D(\hat{\theta}_3) = \left(\frac{n+1}{n}\right)^2 D(X_{(n)}) = \left(\frac{n+1}{n}\right)^2 \cdot \frac{n\theta^2}{(n+1)^2(n+2)} = \frac{\theta^2}{n(n+2)}$$

当 $n \geq 2$ 时，$\dfrac{\theta^2}{n(n+2)} < \dfrac{\theta^2}{3n}$，故 $\hat{\theta}_3$ 更有效。

## 4. 区间估计

### 例题10

设 $X_1, \cdots, X_{25} \sim N(\mu, 4)$，$\bar{x} = 14.5$，求 $\mu$ 的 $95\%$ 置信区间。

**解**：$\sigma = 2$ 已知，$z_{0.025} = 1.96$。

$$\left(14.5 - 1.96 \times \frac{2}{5}, \quad 14.5 + 1.96 \times \frac{2}{5}\right) = (13.716, 15.284)$$

### 例题11

设 $X_1, \cdots, X_{16} \sim N(\mu, \sigma^2)$，$\bar{x} = 10$，$s = 3$，求 $\mu$ 的 $95\%$ 置信区间。

**解**：$\sigma$ 未知，$t_{0.025}(15) = 2.131$。

$$\left(10 - 2.131 \times \frac{3}{4}, \quad 10 + 2.131 \times \frac{3}{4}\right) = (8.402, 11.598)$$

### 例题12

设 $X_1, \cdots, X_{10} \sim N(\mu, \sigma^2)$，$s^2 = 6.42$，求 $\sigma^2$ 的 $95\%$ 置信区间。

**解**：$\chi^2_{0.025}(9) = 19.023$，$\chi^2_{0.975}(9) = 2.700$。

$$\left(\frac{9 \times 6.42}{19.023}, \quad \frac{9 \times 6.42}{2.700}\right) = (3.037, 21.400)$$

### 例题13

某产品合格率的 $95\%$ 置信区间要求宽度不超过 0.1，至少需要多大的样本量？

**解**：置信区间宽度为 $2z_{\alpha/2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}} \leq 0.1$。

$\hat{p}(1-\hat{p}) \leq 0.25$，$z_{0.025} = 1.96$。

$$2 \times 1.96 \times \sqrt{\frac{0.25}{n}} \leq 0.1 \implies n \geq \frac{4 \times 1.96^2 \times 0.25}{0.01} = 384.16$$

取 $n = 385$。

### 例题14

设甲乙两种工艺生产的产品重量分别为 $X \sim N(\mu_1, \sigma^2)$ 和 $Y \sim N(\mu_2, \sigma^2)$，分别抽取 10 件和 8 件，$\bar{x} = 50.1$，$\bar{y} = 49.8$，$s_1^2 = 0.04$，$s_2^2 = 0.03$，求 $\mu_1 - \mu_2$ 的 $95\%$ 置信区间。

**解**：$\sigma_1^2 = \sigma_2^2$ 未知。

$$S_w^2 = \frac{9 \times 0.04 + 7 \times 0.03}{16} = 0.0356$$

$$t_{0.025}(16) = 2.120$$

$$\left(0.3 - 2.120\sqrt{0.0356\left(\frac{1}{10}+\frac{1}{8}\right)}, \quad 0.3 + 2.120\sqrt{0.0356\left(\frac{1}{10}+\frac{1}{8}\right)}\right)$$

$$= (0.3 - 0.189, 0.3 + 0.189) = (0.111, 0.489)$$

### 例题15

设 $X_1, \cdots, X_n \sim N(\mu, \sigma^2)$，求 $\mu$ 的 $95\%$ 单侧置信下限。

**解**：

$$P\left(\frac{\bar{X} - \mu}{S/\sqrt{n}} < t_{0.05}(n-1)\right) = 0.95$$

$$\mu > \bar{X} - t_{0.05}(n-1)\frac{S}{\sqrt{n}}$$

单侧置信下限为 $\bar{X} - t_{0.05}(n-1)\dfrac{S}{\sqrt{n}}$。

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
| 抽样分布典型例题 | 034-SamplingDistributionExamples | 本文的并列主题 |
| 点估计 | 035-PointEstimation | 本文的并列主题 |
| 估计量的评选标准 | 036-EstimatorSelectionCriteria | 本文的并列主题 |
| 区间估计 | 037-IntervalEstimation | 本文的并列主题 |
| 正态总体参数的区间估计 | 038-NormalPopulationParameterIntervalEstimation | 本文的并列主题 |
| 参数估计典型例题 | 039-ParameterEstimationExamples | 本文自身 |
| 假设检验基本概念 | 040-HypothesisTestingBasics | 本文的并列主题 |
| Z检验 | 041-ZTest | 本文的并列主题 |
| t检验 | 042-TTest | 本文的并列主题 |
| 卡方检验 | 043-ChiSquareTest | 本文的并列主题 |
| F检验 | 044-FTest | 本文的并列主题 |
| 假设检验典型例题 | 045-HypothesisTestingExamples | 本文的并列主题 |
