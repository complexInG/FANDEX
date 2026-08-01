---
order: 25
title: 随机变量典型例题
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 随机变量部分的典型例题精选，涵盖离散型与连续型随机变量、分布函数、常用分布、随机变量函数的分布。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/常用分布'
  - 'probability-statistics/随机变量函数的分布'
  - 'probability-statistics/联合分布'
  - 'probability-statistics/边缘分布'
prerequisites: []
---

## 1. 离散型随机变量

### 例题1

某射手每次射击命中目标的概率为 0.8，连续射击直到命中为止。求射击次数 $X$ 的分布律及 $P(X \leq 3)$。

**解**：$X$ 服从几何分布 $G(0.8)$。

$$P(X = k) = 0.2^{k-1} \times 0.8, \quad k = 1, 2, 3, \cdots$$

$$P(X \leq 3) = P(X = 1) + P(X = 2) + P(X = 3) = 0.8 + 0.16 + 0.032 = 0.992$$

### 例题2

设某电话交换台每分钟接到的呼叫次数 $X$ 服从参数 $\lambda = 3$ 的泊松分布，求：

（1）一分钟内恰好接到 5 次呼叫的概率；

（2）一分钟内接到呼叫次数不超过 2 次的概率。

**解**：$X \sim P(3)$。

（1）$P(X = 5) = \dfrac{3^5 e^{-3}}{5!} = \dfrac{243 \times 0.0498}{120} \approx 0.1008$

（2）$P(X \leq 2) = P(X = 0) + P(X = 1) + P(X = 2) = e^{-3}(1 + 3 + 4.5) = 8.5e^{-3} \approx 0.4232$

### 例题3

一批产品共 100 件，其中 10 件次品。从中任取 5 件，求取到次品数 $X$ 的分布律。

**解**：$X \sim H(100, 10, 5)$。

$$P(X = k) = \frac{\binom{10}{k}\binom{90}{5-k}}{\binom{100}{5}}, \quad k = 0, 1, 2, 3, 4, 5$$

## 2. 连续型随机变量

### 例题4

设随机变量 $X$ 的密度函数为

$$f(x) = \begin{cases} Ax^2, & 0 \leq x \leq 1 \\ 0, & \text{其他} \end{cases}$$

求：（1）常数 $A$；（2）$P(0.2 < X < 0.5)$；（3）$X$ 的分布函数。

**解**：

（1）由规范性 $\displaystyle\int_{-\infty}^{+\infty} f(x) dx = 1$：

$$\int_0^1 Ax^2 \, dx = A \cdot \frac{1}{3} = 1 \implies A = 3$$

（2）$P(0.2 < X < 0.5) = \displaystyle\int_{0.2}^{0.5} 3x^2 \, dx = [x^3]_{0.2}^{0.5} = 0.125 - 0.008 = 0.117$

（3）当 $x < 0$ 时，$F(x) = 0$；

当 $0 \leq x < 1$ 时，$F(x) = \displaystyle\int_0^x 3t^2 \, dt = x^3$；

当 $x \geq 1$ 时，$F(x) = 1$。

$$F(x) = \begin{cases} 0, & x < 0 \\ x^3, & 0 \leq x < 1 \\ 1, & x \geq 1 \end{cases}$$

### 例题5

设 $X \sim N(2, 9)$，求：

（1）$P(X < 5)$；（2）$P(-4 < X < 8)$；（3）$P(|X| > 4)$。

**解**：$\mu = 2$，$\sigma = 3$。

（1）$P(X < 5) = \Phi\left(\dfrac{5-2}{3}\right) = \Phi(1) = 0.8413$

（2）$P(-4 < X < 8) = \Phi\left(\dfrac{8-2}{3}\right) - \Phi\left(\dfrac{-4-2}{3}\right) = \Phi(2) - \Phi(-2) = 2\Phi(2) - 1 = 2 \times 0.9772 - 1 = 0.9544$

（3）$P(|X| > 4) = P(X > 4) + P(X < -4)$

$= 1 - \Phi\left(\dfrac{4-2}{3}\right) + \Phi\left(\dfrac{-4-2}{3}\right) = 1 - \Phi(0.667) + \Phi(-2) = 1 - 0.7476 + 0.0228 = 0.2752$

## 3. 分布函数

### 例题6

设随机变量 $X$ 的分布函数为

$$F(x) = \begin{cases} 0, & x < 0 \\ Ax + B, & 0 \leq x < 1 \\ 1, & x \geq 1 \end{cases}$$

求常数 $A, B$ 及 $P(0.3 < X < 0.7)$。

**解**：由 $F(0) = 0$ 得 $B = 0$；由 $F(1^-) = 1$ 得 $A = 1$。

$$P(0.3 < X < 0.7) = F(0.7) - F(0.3) = 0.7 - 0.3 = 0.4$$

### 例题7

设随机变量 $X$ 的分布函数为

$$F(x) = \begin{cases} 0, & x < -1 \\ 0.2, & -1 \leq x < 0 \\ 0.7, & 0 \leq x < 1 \\ 1, & x \geq 1 \end{cases}$$

求 $X$ 的分布律。

**解**：$X$ 为离散型随机变量，取值为 $-1, 0, 1$。

$$P(X = -1) = F(-1) - F(-1^-) = 0.2 - 0 = 0.2$$

$$P(X = 0) = F(0) - F(0^-) = 0.7 - 0.2 = 0.5$$

$$P(X = 1) = F(1) - F(1^-) = 1 - 0.7 = 0.3$$

## 4. 常用分布

### 例题8

某元件的寿命 $X$（小时）服从参数 $\lambda = 0.001$ 的指数分布。求：

（1）元件寿命超过 1000 小时的概率；

（2）已知元件已使用了 500 小时，再使用 1000 小时的概率。

**解**：$X \sim \text{Exp}(0.001)$。

（1）$P(X > 1000) = e^{-0.001 \times 1000} = e^{-1} \approx 0.3679$

（2）由无记忆性：

$$P(X > 500 + 1000 \mid X > 500) = P(X > 1000) = e^{-1} \approx 0.3679$$

### 例题9

设 $X \sim B(n, p)$，且 $E(X) = 12$，$D(X) = 8$，求 $n$ 和 $p$。

**解**：

$$E(X) = np = 12, \quad D(X) = np(1-p) = 8$$

$$1 - p = \frac{8}{12} = \frac{2}{3} \implies p = \frac{1}{3}$$

$$n = \frac{12}{1/3} = 36$$

## 5. 随机变量函数的分布

### 例题10

设 $X \sim U(0, 1)$，求 $Y = -2\ln X$ 的分布。

**解**：当 $y > 0$ 时：

$$F_Y(y) = P(-2\ln X \leq y) = P(\ln X \geq -y/2) = P(X \geq e^{-y/2}) = 1 - e^{-y/2}$$

$$f_Y(y) = \frac{1}{2}e^{-y/2}, \quad y > 0$$

即 $Y \sim \text{Exp}(1/2)$，也即 $Y \sim \chi^2(2)$。

### 例题11

设 $X \sim U(-1, 2)$，求 $Y = X^2$ 的密度函数。

**解**：$Y$ 的取值范围为 $[0, 4)$。

当 $0 \leq y < 1$ 时：

$$F_Y(y) = P(X^2 \leq y) = P(-\sqrt{y} \leq X \leq \sqrt{y}) = \int_{-\sqrt{y}}^{\sqrt{y}} \frac{1}{3} dx = \frac{2\sqrt{y}}{3}$$

$$f_Y(y) = \frac{1}{3\sqrt{y}}$$

当 $1 \leq y < 4$ 时：

$$F_Y(y) = P(X^2 \leq y) = P(-\sqrt{y} \leq X \leq \sqrt{y})$$

由于 $X \in [-1, 2]$，所以 $-\sqrt{y} \leq X$ 等价于 $X \geq -1$（因为 $\sqrt{y} \geq 1$），

$$F_Y(y) = P(-1 \leq X \leq \sqrt{y}) = \frac{\sqrt{y} + 1}{3}$$

$$f_Y(y) = \frac{1}{6\sqrt{y}}$$

综上：

$$f_Y(y) = \begin{cases} \dfrac{1}{3\sqrt{y}}, & 0 < y < 1 \\ \dfrac{1}{6\sqrt{y}}, & 1 \leq y < 4 \\ 0, & \text{其他} \end{cases}$$

### 例题12

设 $X \sim N(0, 1)$，求 $Y = e^X$ 的密度函数。

**解**：$y = e^x$ 严格单调递增，$x = \ln y$，$x' = \dfrac{1}{y}$。

$$f_Y(y) = f_X(\ln y) \cdot \frac{1}{y} = \frac{1}{y} \cdot \frac{1}{\sqrt{2\pi}} e^{-\frac{(\ln y)^2}{2}}, \quad y > 0$$

这是**对数正态分布**的密度函数。

## 综合题知识点讲解

### 例题13

设随机变量 $X$ 的密度函数为 $f(x) = \dfrac{1}{2}e^{-|x|}$（$-\infty < x < +\infty$），求 $Y = |X|$ 的密度函数。

**解**：当 $y > 0$ 时：

$$F_Y(y) = P(|X| \leq y) = P(-y \leq X \leq y) = \int_{-y}^{y} \frac{1}{2}e^{-|x|} dx = 2\int_0^y \frac{1}{2}e^{-x} dx = 1 - e^{-y}$$

$$f_Y(y) = e^{-y}, \quad y > 0$$

即 $Y \sim \text{Exp}(1)$。

### 例题14

设 $X \sim U(0, \pi)$，求 $Y = \sin X$ 的密度函数。

**解**：$Y$ 的取值范围为 $[0, 1]$。

当 $0 < y < 1$ 时，$\sin x \leq y$ 在 $[0, \pi]$ 上的解为 $x \in [0, \arcsin y] \cup [\pi - \arcsin y, \pi]$。

$$F_Y(y) = P(\sin X \leq y) = \frac{\arcsin y + \arcsin y}{\pi} = \frac{2\arcsin y}{\pi}$$

$$f_Y(y) = \frac{2}{\pi\sqrt{1 - y^2}}, \quad 0 < y < 1$$

### 例题15

证明：若 $X \sim N(\mu, \sigma^2)$，则 $Y = \dfrac{X - \mu}{\sigma} \sim N(0, 1)$。

**证明**：$y = \dfrac{x - \mu}{\sigma}$ 严格单调递增，$x = \sigma y + \mu$，$\dfrac{dx}{dy} = \sigma$。

$$f_Y(y) = f_X(\sigma y + \mu) \cdot \sigma = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(\sigma y + \mu - \mu)^2}{2\sigma^2}} \cdot \sigma = \frac{1}{\sqrt{2\pi}} e^{-\frac{y^2}{2}} = \varphi(y)$$

故 $Y \sim N(0, 1)$。

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
| 随机变量典型例题 | 013-RandomVariableExamples | 本文自身 |
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
