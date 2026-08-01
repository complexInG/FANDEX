---
order: 44
title: 矩与协方差矩阵
module: 'probability-statistics'
category: 'comp-sci'
difficulty: advanced
description: 原点矩、中心矩、协方差矩阵的定义与性质、多元正态分布。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/协方差'
  - 'probability-statistics/相关系数'
  - 'probability-statistics/数字特征典型例题'
  - 'probability-statistics/切比雪夫不等式'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 矩的概念

### 1.1 原点矩

设 $X$ 为随机变量，$k$ 为正整数，若 $E(X^k)$ 存在，则称

$$\mu_k = E(X^k)$$

为 $X$ 的 **$k$ 阶原点矩**。

特别地，一阶原点矩 $\mu_1 = E(X)$ 即为数学期望。

### 1.2 中心矩

设 $X$ 为随机变量，$k$ 为正整数，若 $E[X - E(X)]^k$ 存在，则称

$$\nu_k = E[X - E(X)]^k$$

为 $X$ 的 **$k$ 阶中心矩**。

特别地：

- 一阶中心矩 $\nu_1 = 0$
- 二阶中心矩 $\nu_2 = D(X)$（方差）

### 1.3 原点矩与中心矩的关系

由二项展开：

$$\nu_k = E[X - E(X)]^k = \sum_{j=0}^{k} \binom{k}{j} (-1)^{k-j} \mu_j \mu_1^{k-j}$$

常用关系：

$$\nu_2 = \mu_2 - \mu_1^2 = E(X^2) - [E(X)]^2 = D(X)$$

$$\nu_3 = \mu_3 - 3\mu_2\mu_1 + 2\mu_1^3$$

$$\nu_4 = \mu_4 - 4\mu_3\mu_1 + 6\mu_2\mu_1^2 - 3\mu_1^4$$

### 1.4 混合矩

设 $X, Y$ 为随机变量，$k, l$ 为非负整数，若 $E(X^k Y^l)$ 存在，则称

$$\mu_{k,l} = E(X^k Y^l)$$

为 $X$ 与 $Y$ 的 **$k + l$ 阶混合原点矩**。

类似地，**混合中心矩**为

$$\nu_{k,l} = E[X - E(X)]^k [Y - E(Y)]^l$$

特别地，$\nu_{1,1} = \text{Cov}(X, Y)$。

## 2. 偏度与峰度

### 2.1 偏度

$$\gamma_1 = \frac{\nu_3}{\nu_2^{3/2}} = \frac{E[X - E(X)]^3}{[D(X)]^{3/2}}$$

偏度衡量分布的**不对称性**：

- $\gamma_1 > 0$：右偏（正偏），分布右侧尾部较长
- $\gamma_1 < 0$：左偏（负偏），分布左侧尾部较长
- $\gamma_1 = 0$：对称分布

正态分布的偏度为 0。

### 2.2 峰度

$$\gamma_2 = \frac{\nu_4}{\nu_2^2} - 3 = \frac{E[X - E(X)]^4}{[D(X)]^2} - 3$$

峰度衡量分布的**尖峰程度**（相对于正态分布）：

- $\gamma_2 > 0$：尖峰分布（比正态分布更尖）
- $\gamma_2 < 0$：平坦分布（比正态分布更平）
- $\gamma_2 = 0$：与正态分布相同

正态分布的峰度为 0（因为 $\dfrac{\nu_4}{\nu_2^2} = 3$）。

## 3. 协方差矩阵

### 3.1 定义

设 $n$ 维随机变量 $\mathbf{X} = (X_1, X_2, \cdots, X_n)^T$，令

$$c_{ij} = \text{Cov}(X_i, X_j) = E[X_i - E(X_i)][X_j - E(X_j)], \quad i, j = 1, 2, \cdots, n$$

则矩阵

$$\mathbf{C} = (c_{ij})_{n \times n} = \begin{pmatrix} c_{11} & c_{12} & \cdots & c_{1n} \\ c_{21} & c_{22} & \cdots & c_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ c_{n1} & c_{n2} & \cdots & c_{nn} \end{pmatrix}$$

称为 $\mathbf{X}$ 的**协方差矩阵**。

### 3.2 协方差矩阵的表示

$$\mathbf{C} = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T]$$

其中 $\boldsymbol{\mu} = E(\mathbf{X}) = (E(X_1), E(X_2), \cdots, E(X_n))^T$。

### 3.3 协方差矩阵的性质

1. **对称性**：$\mathbf{C}^T = \mathbf{C}$（因为 $c_{ij} = c_{ji}$）

2. **半正定性**：对任意 $n$ 维向量 $\mathbf{a}$，

$$\mathbf{a}^T \mathbf{C} \mathbf{a} \geq 0$$

**证明**：

$$\mathbf{a}^T \mathbf{C} \mathbf{a} = \mathbf{a}^T E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T] \mathbf{a} = E[\mathbf{a}^T(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T \mathbf{a}] = E[(\mathbf{a}^T(\mathbf{X} - \boldsymbol{\mu}))^2] \geq 0$$

3. **对角线元素**：$c_{ii} = D(X_i)$

4. **线性变换**：若 $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$，则

$$\mathbf{C}_Y = \mathbf{A}\mathbf{C}_X \mathbf{A}^T$$

## 4. 相关矩阵

### 4.1 定义

$$\mathbf{R} = (\rho_{ij})_{n \times n}$$

其中 $\rho_{ij} = \dfrac{c_{ij}}{\sqrt{c_{ii} c_{jj}}}$ 为 $X_i$ 与 $X_j$ 的相关系数。

### 4.2 与协方差矩阵的关系

$$\mathbf{R} = \mathbf{D}^{-1/2} \mathbf{C} \mathbf{D}^{-1/2}$$

其中 $\mathbf{D} = \text{diag}(c_{11}, c_{22}, \cdots, c_{nn})$。

## 5. 多元正态分布

### 5.1 定义

设 $\mathbf{X} = (X_1, X_2, \cdots, X_n)^T$ 服从 $n$ 维正态分布，$\mathbf{X} \sim N_n(\boldsymbol{\mu}, \boldsymbol{\Sigma})$，其密度函数为

$$f(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\boldsymbol{\Sigma}|^{1/2}} \exp\left\{-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right\}$$

其中 $\boldsymbol{\mu}$ 为均值向量，$\boldsymbol{\Sigma}$ 为协方差矩阵（正定）。

### 5.2 多元正态分布的性质

1. **边缘分布**：$\mathbf{X}$ 的任意子向量的边缘分布仍为正态分布

2. **线性变换**：若 $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$，则 $\mathbf{Y} \sim N(\mathbf{A}\boldsymbol{\mu} + \mathbf{b}, \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^T)$

3. **独立与不相关等价**：$X_i$ 与 $X_j$ 独立 $\iff$ $\text{Cov}(X_i, X_j) = 0$

4. **条件分布**：给定部分分量的条件下，其余分量的条件分布仍为正态分布

### 5.3 二元正态分布

$$\boldsymbol{\mu} = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \quad \boldsymbol{\Sigma} = \begin{pmatrix} \sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}$$

$$|\boldsymbol{\Sigma}| = \sigma_1^2\sigma_2^2(1 - \rho^2)$$

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
| 矩与协方差矩阵 | 024-MomentAndCovarianceMatrix | 本文自身 |
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
