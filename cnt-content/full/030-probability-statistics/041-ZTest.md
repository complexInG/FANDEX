---
order: 81
title: Z检验
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 单总体均值Z检验、双总体均值差Z检验的原理与应用。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/参数估计典型例题'
  - 'probability-statistics/假设检验基本概念'
  - 'probability-statistics/t检验'
  - 'probability-statistics/卡方检验'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 单总体均值的 Z 检验

### 1.1 适用条件

- 总体服从正态分布 $N(\mu, \sigma^2)$，$\sigma$ 已知
- 或总体分布未知，但大样本（$n \geq 30$），由中心极限定理近似

### 1.2 检验步骤

**假设**：

- 双侧：$H_0: \mu = \mu_0$，$H_1: \mu \neq \mu_0$
- 右侧：$H_0: \mu \leq \mu_0$，$H_1: \mu > \mu_0$
- 左侧：$H_0: \mu \geq \mu_0$，$H_1: \mu < \mu_0$

**检验统计量**：

$$Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}$$

在 $H_0$ 成立时，$Z \sim N(0, 1)$。

**拒绝域**：

| 检验类型 | 拒绝域                 |
| -------- | ---------------------- |
| 双侧     | $\|Z\| > z_{\alpha/2}$ |
| 右侧     | $Z > z_\alpha$         |
| 左侧     | $Z < -z_\alpha$        |

### 1.3 示例

**例题**：某工厂生产的灯泡寿命服从正态分布 $N(\mu, 100)$，标准规定平均寿命不低于 1000 小时。现抽取 25 只灯泡，测得平均寿命 $\bar{x} = 995$ 小时。在 $\alpha = 0.05$ 下检验灯泡寿命是否达标。

**解**：

$H_0: \mu \geq 1000$，$H_1: \mu < 1000$

$$Z = \frac{995 - 1000}{10/5} = \frac{-5}{2} = -2.5$$

$z_{0.05} = 1.645$，拒绝域 $Z < -1.645$。

$Z = -2.5 < -1.645$，拒绝 $H_0$，认为灯泡寿命不达标。

## 2. 双总体均值差的 Z 检验

### 2.1 适用条件

- 两个正态总体 $N(\mu_1, \sigma_1^2)$ 和 $N(\mu_2, \sigma_2^2)$，$\sigma_1, \sigma_2$ 已知
- 或大样本近似

### 2.2 检验步骤

**假设**：

- 双侧：$H_0: \mu_1 - \mu_2 = d_0$，$H_1: \mu_1 - \mu_2 \neq d_0$
- 右侧：$H_0: \mu_1 - \mu_2 \leq d_0$，$H_1: \mu_1 - \mu_2 > d_0$
- 左侧：$H_0: \mu_1 - \mu_2 \geq d_0$，$H_1: \mu_1 - \mu_2 < d_0$

（通常 $d_0 = 0$）

**检验统计量**：

$$Z = \frac{(\bar{X} - \bar{Y}) - d_0}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$$

在 $H_0$ 成立时，$Z \sim N(0, 1)$。

**拒绝域**：与单总体类似。

### 2.3 示例

**例题**：甲乙两台机床加工同一种零件，直径分别服从 $N(\mu_1, 0.04)$ 和 $N(\mu_2, 0.09)$。从甲机床抽取 6 件，$\bar{x} = 14.95$；从乙机床抽取 9 件，$\bar{y} = 15.02$。在 $\alpha = 0.05$ 下检验两机床加工精度是否有显著差异。

**解**：

$H_0: \mu_1 = \mu_2$，$H_1: \mu_1 \neq \mu_2$

$$Z = \frac{14.95 - 15.02}{\sqrt{\frac{0.04}{6} + \frac{0.09}{9}}} = \frac{-0.07}{\sqrt{0.00667 + 0.01}} = \frac{-0.07}{0.129} = -0.543$$

$z_{0.025} = 1.96$，$|Z| = 0.543 < 1.96$，不拒绝 $H_0$。

认为两机床加工精度无显著差异。

## 3. 大样本比例的 Z 检验

### 3.1 单总体比例

设 $X \sim B(n, p)$，$\hat{p} = X/n$。

$$H_0: p = p_0, \quad H_1: p \neq p_0$$

$$Z = \frac{\hat{p} - p_0}{\sqrt{p_0(1-p_0)/n}}$$

当 $n$ 较大时，$Z$ 近似 $N(0, 1)$。

### 3.2 双总体比例差

$$H_0: p_1 = p_2, \quad H_1: p_1 \neq p_2$$

$$Z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$$

其中 $\hat{p} = \dfrac{X_1 + X_2}{n_1 + n_2}$ 为合并比例。

### 3.3 示例

**例题**：某产品原不合格率为 5%，采用新工艺后抽查 200 件，发现 6 件不合格。在 $\alpha = 0.05$ 下检验新工艺是否降低了不合格率。

**解**：

$H_0: p \geq 0.05$，$H_1: p < 0.05$

$$\hat{p} = \frac{6}{200} = 0.03$$

$$Z = \frac{0.03 - 0.05}{\sqrt{0.05 \times 0.95/200}} = \frac{-0.02}{0.01541} = -1.298$$

$-z_{0.05} = -1.645$，$Z = -1.298 > -1.645$，不拒绝 $H_0$。

不能认为新工艺显著降低了不合格率。

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
| 参数估计典型例题 | 039-ParameterEstimationExamples | 本文的并列主题 |
| 假设检验基本概念 | 040-HypothesisTestingBasics | 本文的并列主题 |
| Z检验 | 041-ZTest | 本文自身 |
| t检验 | 042-TTest | 本文的并列主题 |
| 卡方检验 | 043-ChiSquareTest | 本文的并列主题 |
| F检验 | 044-FTest | 本文的并列主题 |
| 假设检验典型例题 | 045-HypothesisTestingExamples | 本文的并列主题 |
