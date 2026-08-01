---
order: 21
title: 连续型随机变量
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 连续型随机变量的定义与概率密度、均匀分布、指数分布、正态分布及其应用。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/概率基础典型例题'
  - 'probability-statistics/离散型随机变量'
  - 'probability-statistics/分布函数'
  - 'probability-statistics/常用分布'
prerequisites: []
---

## 1. 连续型随机变量的概念

### 1.1 概率密度函数

设 $F(x)$ 为随机变量 $X$ 的分布函数，若存在非负可积函数 $f(x)$，使得对任意实数 $x$，有

$$F(x) = \int_{-\infty}^{x} f(t) \, dt$$

则称 $X$ 为**连续型随机变量**，$f(x)$ 为 $X$ 的**概率密度函数**（简称**密度函数**或**密度**）。

### 1.2 概率密度函数的性质

1. **非负性**：$f(x) \geq 0$
2. **规范性**：$\displaystyle\int_{-\infty}^{+\infty} f(x) \, dx = 1$
3. **概率计算**：$P(a < X \leq b) = \displaystyle\int_a^b f(x) \, dx$
4. **单点概率为零**：$P(X = x_0) = 0$（对任意 $x_0$）
5. **在连续点处**：$F'(x) = f(x)$

### 1.3 连续型随机变量的特点

- 取任一确定值的概率为零
- $P(a < X < b) = P(a \leq X < b) = P(a < X \leq b) = P(a \leq X \leq b)$
- 分布函数 $F(x)$ 是连续函数

## 2. 均匀分布

### 2.1 定义

若随机变量 $X$ 的概率密度为

$$f(x) = \begin{cases} \dfrac{1}{b-a}, & a \leq x \leq b \\ 0, & \text{其他} \end{cases}$$

则称 $X$ 在区间 $[a, b]$ 上服从**均匀分布**，记作 $X \sim U(a, b)$。

### 2.2 分布函数

$$F(x) = \begin{cases} 0, & x < a \\ \dfrac{x - a}{b - a}, & a \leq x < b \\ 1, & x \geq b \end{cases}$$

### 2.3 性质

1. **期望与方差**：$E(X) = \dfrac{a + b}{2}$，$D(X) = \dfrac{(b-a)^2}{12}$

2. **等可能性**：$X$ 落在 $[a, b]$ 中任意等长度的子区间内的概率相等

3. **线性变换**：若 $X \sim U(a, b)$，则 $Y = \dfrac{X - a}{b - a} \sim U(0, 1)$

### 2.4 应用

均匀分布常用于：

- 随机数的生成（计算机中的伪随机数）
- 舍入误差的建模
- 缺乏先验信息时的初始假设

## 3. 指数分布

### 3.1 定义

若随机变量 $X$ 的概率密度为

$$f(x) = \begin{cases} \lambda e^{-\lambda x}, & x > 0 \\ 0, & x \leq 0 \end{cases}$$

其中 $\lambda > 0$ 为常数，则称 $X$ 服从参数为 $\lambda$ 的**指数分布**，记作 $X \sim \text{Exp}(\lambda)$。

### 3.2 分布函数

$$F(x) = \begin{cases} 1 - e^{-\lambda x}, & x > 0 \\ 0, & x \leq 0 \end{cases}$$

### 3.3 性质

1. **期望与方差**：$E(X) = \dfrac{1}{\lambda}$，$D(X) = \dfrac{1}{\lambda^2}$

2. **无记忆性**：对任意 $s, t > 0$，

$$P(X > s + t \mid X > s) = P(X > t)$$

**证明**：

$$P(X > s + t \mid X > s) = \frac{P(X > s + t)}{P(X > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t)$$

指数分布是唯一具有无记忆性的连续型分布。

3. **与泊松过程的关系**：若事件的发生服从参数为 $\lambda$ 的泊松过程，则相邻两个事件的时间间隔服从 $\text{Exp}(\lambda)$。

### 3.4 应用

- 电子元件的寿命
- 等待时间（如顾客到达的间隔时间）
- 电话通话时间
- 放射性衰变时间

## 4. 正态分布

### 4.1 定义

若随机变量 $X$ 的概率密度为

$$f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \quad -\infty < x < +\infty$$

其中 $\mu$ 和 $\sigma > 0$ 为常数，则称 $X$ 服从参数为 $\mu, \sigma^2$ 的**正态分布**（**高斯分布**），记作 $X \sim N(\mu, \sigma^2)$。

### 4.2 正态分布的密度函数特征

1. **对称性**：$f(x)$ 关于 $x = \mu$ 对称
2. **最大值**：$f(\mu) = \dfrac{1}{\sqrt{2\pi}\sigma}$
3. **拐点**：$x = \mu \pm \sigma$ 处有拐点
4. **渐近线**：$x$ 轴为水平渐近线
5. $\mu$ 决定曲线的**位置**，$\sigma$ 决定曲线的**形状**（$\sigma$ 越大曲线越矮胖，$\sigma$ 越小曲线越瘦高）

### 4.3 标准正态分布

当 $\mu = 0, \sigma = 1$ 时，$X \sim N(0, 1)$ 称为**标准正态分布**，其密度函数和分布函数分别记为

$$\varphi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}, \quad \Phi(x) = \int_{-\infty}^{x} \varphi(t) \, dt$$

**标准正态分布的性质**：

1. $\Phi(-x) = 1 - \Phi(x)$
2. $\Phi(0) = 0.5$
3. $P(|X| \leq a) = 2\Phi(a) - 1$

### 4.4 标准化

若 $X \sim N(\mu, \sigma^2)$，则 $Z = \dfrac{X - \mu}{\sigma} \sim N(0, 1)$。

因此

$$P(a < X < b) = P\left(\frac{a - \mu}{\sigma} < Z < \frac{b - \mu}{\sigma}\right) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$$

### 4.5 正态分布的 $3\sigma$ 法则

$$P(\mu - \sigma < X < \mu + \sigma) \approx 0.6827$$

$$P(\mu - 2\sigma < X < \mu + 2\sigma) \approx 0.9545$$

$$P(\mu - 3\sigma < X < \mu + 3\sigma) \approx 0.9973$$

即正态随机变量几乎全部落在 $(\mu - 3\sigma, \mu + 3\sigma)$ 之内。

### 4.6 正态分布的性质

1. **期望与方差**：$E(X) = \mu$，$D(X) = \sigma^2$

2. **线性变换**：若 $X \sim N(\mu, \sigma^2)$，则 $aX + b \sim N(a\mu + b, a^2\sigma^2)$

3. **可加性**：若 $X \sim N(\mu_1, \sigma_1^2)$，$Y \sim N(\mu_2, \sigma_2^2)$，且 $X$ 与 $Y$ 独立，则

$$X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$$

4. **更一般地**：独立正态随机变量的线性组合仍为正态随机变量

### 4.7 正态分布的应用

正态分布是概率论中最重要的分布，其重要性源于：

- **中心极限定理**：大量独立同分布随机变量之和近似服从正态分布
- **误差理论**：测量误差通常服从正态分布
- **自然界**：许多自然现象近似服从正态分布（身高、考试成绩等）

### 4.8 正态分布计算示例

**例题**：设 $X \sim N(3, 4)$，求 $P(2 < X < 5)$。

**解**：$\mu = 3$，$\sigma = 2$。

$$P(2 < X < 5) = \Phi\left(\frac{5-3}{2}\right) - \Phi\left(\frac{2-3}{2}\right) = \Phi(1) - \Phi(-0.5)$$

$$= \Phi(1) - (1 - \Phi(0.5)) = 0.8413 - (1 - 0.6915) = 0.8413 - 0.3085 = 0.5328$$

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
| 连续型随机变量 | 009-ContinuousRandomVariable | 本文自身 |
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
| Z检验 | 041-ZTest | 本文的并列主题 |
| t检验 | 042-TTest | 本文的并列主题 |
| 卡方检验 | 043-ChiSquareTest | 本文的并列主题 |
| F检验 | 044-FTest | 本文的并列主题 |
| 假设检验典型例题 | 045-HypothesisTestingExamples | 本文的并列主题 |
