---
order: 43
title: 相关系数
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 相关系数的定义、性质、判定与意义，相关系数与独立性的关系。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/方差与标准差'
  - 'probability-statistics/协方差'
  - 'probability-statistics/矩与协方差矩阵'
  - 'probability-statistics/数字特征典型例题'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 相关系数的定义

### 1.1 定义

设 $X$ 和 $Y$ 是两个随机变量，且 $D(X) > 0$，$D(Y) > 0$，则称

$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sqrt{D(X)} \cdot \sqrt{D(Y)}} = \frac{E[X - E(X)][Y - E(Y)]}{\sqrt{D(X)} \cdot \sqrt{D(Y)}}$$

为 $X$ 与 $Y$ 的**相关系数**（或**皮尔逊相关系数**）。

### 1.2 标准化变量的协方差

$$\rho_{XY} = \text{Cov}\left(X^*, Y^*\right)$$

其中 $X^* = \dfrac{X - E(X)}{\sqrt{D(X)}}$，$Y^* = \dfrac{Y - E(Y)}{\sqrt{D(Y)}}$ 为标准化变量。

相关系数就是标准化变量的协方差。

## 2. 相关系数的性质

### 2.1 基本性质

1. **有界性**：$|\rho_{XY}| \leq 1$

2. **对称性**：$\rho_{XY} = \rho_{YX}$

3. **线性变换不变性**：$\rho_{aX+b, cY+d} = \text{sgn}(ac) \cdot \rho_{XY}$

   特别地，$\rho_{aX, aY} = \rho_{XY}$（$a > 0$）

4. **$|\rho| = 1$ 的条件**：$|\rho_{XY}| = 1 \iff$ 存在常数 $a, b$（$a \neq 0$），使得 $P(Y = aX + b) = 1$
   - $\rho = 1$：$a > 0$（完全正相关）
   - $\rho = -1$：$a < 0$（完全负相关）

5. **$\rho = 0$ 的条件**：$\rho_{XY} = 0 \iff \text{Cov}(X, Y) = 0 \iff E(XY) = E(X)E(Y)$

### 2.2 有界性的证明

由柯西-施瓦茨不等式：

$$[E(XY)]^2 \leq E(X^2) \cdot E(Y^2)$$

令 $U = X - E(X)$，$V = Y - E(Y)$，则

$$[\text{Cov}(X, Y)]^2 = [E(UV)]^2 \leq E(U^2) \cdot E(V^2) = D(X) \cdot D(Y)$$

$$\rho_{XY}^2 = \frac{[\text{Cov}(X, Y)]^2}{D(X) \cdot D(Y)} \leq 1$$

### 2.3 $|\rho| = 1$ 的证明

$|\rho_{XY}| = 1 \iff [E(UV)]^2 = E(U^2) E(V^2) \iff$ 存在常数 $a$，使得 $P(V = aU) = 1$

即 $P(Y - E(Y) = a[X - E(X)]) = 1$，亦即 $P(Y = aX + b) = 1$，其中 $b = E(Y) - aE(X)$。

## 3. 相关系数的意义

### 3.1 线性相关程度

相关系数衡量的是两个随机变量之间的**线性相关程度**：

| $\rho$ 的范围   | 含义                 |
| --------------- | -------------------- |
| $\rho = 1$      | 完全正线性相关       |
| $0 < \rho < 1$  | 正线性相关           |
| $\rho = 0$      | 不相关（无线性关系） |
| $-1 < \rho < 0$ | 负线性相关           |
| $\rho = -1$     | 完全负线性相关       |

### 3.2 相关系数与因果关系

**重要**：相关不等于因果。$\rho \neq 0$ 只说明 $X$ 与 $Y$ 存在线性关系，不能说明因果关系。

### 3.3 相关系数的局限

1. 只衡量线性关系，不反映非线性关系
2. 对异常值敏感
3. $\rho = 0$ 不意味着 $X$ 与 $Y$ 没有关系，只是没有线性关系

## 4. 相关系数与独立性

### 4.1 关系

- 独立 $\Rightarrow$ 不相关（$\rho = 0$）
- 不相关 $\not\Rightarrow$ 独立
- 二维正态：不相关 $\iff$ 独立

### 4.2 不相关但不独立的例子

**例1**：设 $\Theta \sim U(0, 2\pi)$，$X = \cos\Theta$，$Y = \sin\Theta$。

$$E(X) = E(\cos\Theta) = 0, \quad E(Y) = E(\sin\Theta) = 0$$

$$E(XY) = E(\cos\Theta \sin\Theta) = \frac{1}{2}E(\sin 2\Theta) = 0$$

$$\text{Cov}(X, Y) = 0, \quad \rho = 0$$

但 $X^2 + Y^2 = 1$，$X$ 与 $Y$ 显然不独立。

**例2**：设 $X \sim N(0, 1)$，$Y = X^2$。

$$E(XY) = E(X^3) = 0 = E(X)E(Y) = 0$$

$\rho = 0$，但 $Y$ 完全由 $X$ 决定。

## 5. 相关系数的计算

### 5.1 计算步骤

1. 计算 $E(X)$，$E(Y)$
2. 计算 $E(XY)$
3. 计算 $\text{Cov}(X, Y) = E(XY) - E(X)E(Y)$
4. 计算 $D(X)$，$D(Y)$
5. 计算 $\rho_{XY} = \dfrac{\text{Cov}(X, Y)}{\sqrt{D(X)D(Y)}}$

### 5.2 示例

**例题**：设 $(X, Y)$ 的联合分布律为：

| $X \backslash Y$ |       0        |       1        |
| :--------------: | :------------: | :------------: |
|        0         | $\dfrac{1}{4}$ | $\dfrac{1}{4}$ |
|        1         | $\dfrac{1}{4}$ | $\dfrac{1}{4}$ |

求 $\rho_{XY}$。

**解**：

$E(X) = \dfrac{1}{2}$，$E(Y) = \dfrac{1}{2}$

$E(XY) = 0 \times 0 \times \dfrac{1}{4} + 0 \times 1 \times \dfrac{1}{4} + 1 \times 0 \times \dfrac{1}{4} + 1 \times 1 \times \dfrac{1}{4} = \dfrac{1}{4}$

$\text{Cov}(X, Y) = \dfrac{1}{4} - \dfrac{1}{2} \times \dfrac{1}{2} = 0$

$\rho_{XY} = 0$

$X$ 与 $Y$ 不相关。实际上可以验证 $X$ 与 $Y$ 独立。

## 6. 其他相关系数

### 6.1 秩相关系数（斯皮尔曼）

对数据的秩（排名）计算相关系数，适用于非线性单调关系。

### 6.2 肯德尔秩相关系数

基于一致对和不一致对的数量，适用于序数数据。

### 6.3 点双列相关

用于一个连续变量和一个二分类变量之间的相关。

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
| 相关系数 | 023-CorrelationCoefficient | 本文自身 |
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
