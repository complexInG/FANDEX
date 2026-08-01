---
order: 72
title: 区间估计
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 置信区间的概念、构造方法、单侧置信区间。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/点估计'
  - 'probability-statistics/估计量的评选标准'
  - 'probability-statistics/正态总体参数的区间估计'
  - 'probability-statistics/参数估计典型例题'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 置信区间的概念

### 1.1 定义

设 $\theta$ 为总体分布的未知参数，$X_1, X_2, \cdots, X_n$ 为样本。若存在统计量 $\underline{\theta} = \underline{\theta}(X_1, \cdots, X_n)$ 和 $\overline{\theta} = \overline{\theta}(X_1, \cdots, X_n)$，使得对给定的 $\alpha \in (0, 1)$，

$$P(\underline{\theta} < \theta < \overline{\theta}) = 1 - \alpha$$

则称随机区间 $(\underline{\theta}, \overline{\theta})$ 为 $\theta$ 的**置信水平**为 $1 - \alpha$ 的**置信区间**，$\underline{\theta}$ 和 $\overline{\theta}$ 分别称为**置信下限**和**置信上限**，$1 - \alpha$ 称为**置信水平**（或**置信度**）。

### 1.2 置信水平的含义

$P(\underline{\theta} < \theta < \overline{\theta}) = 1 - \alpha$ 的含义是：反复抽样多次，每个样本确定一个区间，在这些区间中包含 $\theta$ 真值的比例约为 $1 - \alpha$。

> **注意**：参数 $\theta$ 是固定但未知的常数，区间 $(\underline{\theta}, \overline{\theta})$ 是随机的。

### 1.3 置信水平与精度的关系

- 置信水平 $1 - \alpha$ 越大，区间越宽，精度越低
- 置信水平 $1 - \alpha$ 越小，区间越窄，精度越高
- 在置信水平一定时，增大样本量可以缩小区间宽度

## 2. 置信区间的构造方法

### 2.1 枢轴量法

构造置信区间的基本方法是**枢轴量法**：

1. 找一个包含 $\theta$ 和样本的函数 $G(X_1, \cdots, X_n; \theta)$，其分布已知且不依赖于 $\theta$，称为**枢轴量**
2. 对给定的 $\alpha$，找常数 $a, b$ 使得 $P(a < G < b) = 1 - \alpha$
3. 由 $a < G < b$ 解出 $\underline{\theta} < \theta < \overline{\theta}$

### 2.2 枢轴量的选择

枢轴量通常基于抽样分布：

| 参数       | 条件          | 枢轴量                                   | 分布          |
| ---------- | ------------- | ---------------------------------------- | ------------- |
| $\mu$      | $\sigma$ 已知 | $\dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}}$ | $N(0,1)$      |
| $\mu$      | $\sigma$ 未知 | $\dfrac{\bar{X} - \mu}{S/\sqrt{n}}$      | $t(n-1)$      |
| $\sigma^2$ | $\mu$ 未知    | $\dfrac{(n-1)S^2}{\sigma^2}$             | $\chi^2(n-1)$ |

## 3. 单侧置信区间

### 3.1 定义

若 $P(\theta > \underline{\theta}) = 1 - \alpha$，则 $(\underline{\theta}, +\infty)$ 为 $\theta$ 的**单侧置信区间**，$\underline{\theta}$ 为**单侧置信下限**。

若 $P(\theta < \overline{\theta}) = 1 - \alpha$，则 $(-\infty, \overline{\theta})$ 为 $\theta$ 的**单侧置信区间**，$\overline{\theta}$ 为**单侧置信上限**。

### 3.2 单侧与双侧的关系

双侧置信水平 $1 - \alpha$ 的置信区间对应单侧置信水平 $1 - \alpha/2$。

例如，$\mu$ 的 $95\%$ 双侧置信区间使用 $z_{0.025} = 1.96$，而 $97.5\%$ 单侧置信上限使用 $z_{0.025} = 1.96$。

## 4. 置信区间的评价

### 4.1 精确置信区间

基于精确抽样分布构造的置信区间，其置信水平恰好等于 $1 - \alpha$。

### 4.2 近似置信区间

基于渐近分布（如中心极限定理）构造的置信区间，其置信水平近似等于 $1 - \alpha$。

### 4.3 置信区间的宽度

置信区间的宽度 $\overline{\theta} - \underline{\theta}$ 反映了估计的精度。在置信水平相同的条件下，宽度越小越好。

## 5. 置信区间的常见误解

1. **误解**：$\theta$ 有 $1 - \alpha$ 的概率落在置信区间内

   **正解**：参数 $\theta$ 是常数，不是随机变量。随机的是区间，不是参数

2. **误解**：$95\%$ 置信区间意味着 $\theta$ 落在该区间内的概率是 $0.95$

   **正解**：如果重复抽样 100 次，大约有 95 个区间包含 $\theta$

3. **误解**：置信水平越高越好

   **正解**：置信水平越高，区间越宽，精度越低。需要在置信水平和精度之间权衡

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
| 区间估计 | 037-IntervalEstimation | 本文自身 |
| 正态总体参数的区间估计 | 038-NormalPopulationParameterIntervalEstimation | 本文的并列主题 |
| 参数估计典型例题 | 039-ParameterEstimationExamples | 本文的并列主题 |
| 假设检验基本概念 | 040-HypothesisTestingBasics | 本文的并列主题 |
| Z检验 | 041-ZTest | 本文的并列主题 |
| t检验 | 042-TTest | 本文的并列主题 |
| 卡方检验 | 043-ChiSquareTest | 本文的并列主题 |
| F检验 | 044-FTest | 本文的并列主题 |
| 假设检验典型例题 | 045-HypothesisTestingExamples | 本文的并列主题 |
