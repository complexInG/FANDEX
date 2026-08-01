---
order: 32
title: 条件分布
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 条件分布律、条件概率密度的定义与计算、条件分布的应用。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/联合分布'
  - 'probability-statistics/边缘分布'
  - 'probability-statistics/随机变量的独立性'
  - 'probability-statistics/和的分布与极值分布'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 离散型随机变量的条件分布

### 1.1 条件分布律

设 $(X, Y)$ 是二维离散型随机变量，联合分布律为 $P(X = x_i, Y = y_j) = p_{ij}$，边缘分布律为 $p_{i\cdot}$ 和 $p_{\cdot j}$。

若 $P(Y = y_j) > 0$，则在 $Y = y_j$ 条件下 $X$ 的**条件分布律**为

$$P(X = x_i \mid Y = y_j) = \frac{P(X = x_i, Y = y_j)}{P(Y = y_j)} = \frac{p_{ij}}{p_{\cdot j}}, \quad i = 1, 2, \cdots$$

类似地，若 $P(X = x_i) > 0$，则在 $X = x_i$ 条件下 $Y$ 的**条件分布律**为

$$P(Y = y_j \mid X = x_i) = \frac{p_{ij}}{p_{i\cdot}}, \quad j = 1, 2, \cdots$$

### 1.2 条件分布律的性质

1. **非负性**：$P(X = x_i \mid Y = y_j) \geq 0$
2. **规范性**：$\displaystyle\sum_{i=1}^{\infty} P(X = x_i \mid Y = y_j) = 1$

### 1.3 示例

设 $(X, Y)$ 的联合分布律为：

| $X \backslash Y$ |        0        |        1        |
| :--------------: | :-------------: | :-------------: |
|        0         | $\dfrac{1}{10}$ | $\dfrac{3}{10}$ |
|        1         | $\dfrac{3}{10}$ | $\dfrac{3}{10}$ |

求 $X = 0$ 条件下 $Y$ 的条件分布律。

**解**：$P(X = 0) = \dfrac{1}{10} + \dfrac{3}{10} = \dfrac{2}{5}$

$$P(Y = 0 \mid X = 0) = \frac{P(X = 0, Y = 0)}{P(X = 0)} = \frac{1/10}{2/5} = \frac{1}{4}$$

$$P(Y = 1 \mid X = 0) = \frac{P(X = 0, Y = 1)}{P(X = 0)} = \frac{3/10}{2/5} = \frac{3}{4}$$

## 2. 连续型随机变量的条件分布

### 2.1 条件概率密度

设 $(X, Y)$ 是二维连续型随机变量，联合密度为 $f(x, y)$，边缘密度为 $f_X(x)$ 和 $f_Y(y)$。

若 $f_Y(y) > 0$，则在 $Y = y$ 条件下 $X$ 的**条件概率密度**为

$$f_{X \mid Y}(x \mid y) = \frac{f(x, y)}{f_Y(y)}$$

类似地，若 $f_X(x) > 0$，则在 $X = x$ 条件下 $Y$ 的**条件概率密度**为

$$f_{Y \mid X}(y \mid x) = \frac{f(x, y)}{f_X(x)}$$

### 2.2 条件分布函数

在 $Y = y$ 条件下 $X$ 的**条件分布函数**为

$$F_{X \mid Y}(x \mid y) = \int_{-\infty}^{x} f_{X \mid Y}(u \mid y) \, du = \frac{\int_{-\infty}^{x} f(u, y) \, du}{f_Y(y)}$$

### 2.3 条件概率密度的性质

1. **非负性**：$f_{X \mid Y}(x \mid y) \geq 0$
2. **规范性**：$\displaystyle\int_{-\infty}^{+\infty} f_{X \mid Y}(x \mid y) \, dx = 1$
3. **乘法公式**：$f(x, y) = f_X(x) \cdot f_{Y \mid X}(y \mid x) = f_Y(y) \cdot f_{X \mid Y}(x \mid y)$

### 2.4 示例

**例题**：设 $(X, Y)$ 的联合密度为

$$f(x, y) = \begin{cases} 3x, & 0 < x < 1, 0 < y < x \\ 0, & \text{其他} \end{cases}$$

求条件概率密度 $f_{Y \mid X}(y \mid x)$ 和 $f_{X \mid Y}(x \mid y)$。

**解**：

$$f_X(x) = \int_0^x 3x \, dy = 3x^2, \quad 0 < x < 1$$

$$f_Y(y) = \int_y^1 3x \, dx = \frac{3(1 - y^2)}{2}, \quad 0 < y < 1$$

$$f_{Y \mid X}(y \mid x) = \frac{f(x, y)}{f_X(x)} = \frac{3x}{3x^2} = \frac{1}{x}, \quad 0 < y < x$$

即在 $X = x$ 条件下，$Y \sim U(0, x)$。

$$f_{X \mid Y}(x \mid y) = \frac{f(x, y)}{f_Y(y)} = \frac{3x}{\frac{3(1 - y^2)}{2}} = \frac{2x}{1 - y^2}, \quad y < x < 1$$

## 3. 条件分布与独立性

### 3.1 独立性的等价条件

$X$ 与 $Y$ 独立等价于条件分布等于无条件分布：

- 离散型：$P(X = x_i \mid Y = y_j) = P(X = x_i)$ 对所有 $i, j$ 成立
- 连续型：$f_{X \mid Y}(x \mid y) = f_X(x)$ 对所有 $x, y$ 成立

### 3.2 条件分布的信息量

条件分布 $f_{X \mid Y}(x \mid y)$ 与边缘分布 $f_X(x)$ 的差异反映了 $Y$ 对 $X$ 的影响程度。两者越接近，说明 $Y$ 对 $X$ 的影响越小。

## 4. 条件分布的应用

### 4.1 贝叶斯推断

条件分布是贝叶斯推断的核心：

$$f_{X \mid Y}(x \mid y) = \frac{f_Y(y \mid x) f_X(x)}{f_Y(y)} \propto f_Y(y \mid x) f_X(x)$$

即**后验 $\propto$ 似然 $\times$ 先验**。

### 4.2 条件期望

条件分布可以定义条件期望：

$$E(X \mid Y = y) = \int_{-\infty}^{+\infty} x f_{X \mid Y}(x \mid y) \, dx$$

这是回归分析的理论基础。

### 4.3 全概率公式的密度形式

$$f_X(x) = \int_{-\infty}^{+\infty} f_{X \mid Y}(x \mid y) f_Y(y) \, dy$$

这是全概率公式在连续型情形的推广。

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
| 条件分布 | 016-ConditionalDistribution | 本文自身 |
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
