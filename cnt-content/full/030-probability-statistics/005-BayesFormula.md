---
order: 14
title: 贝叶斯公式
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 全概率公式、贝叶斯公式的推导与应用、先验概率与后验概率。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/几何概型'
  - 'probability-statistics/条件概率'
  - 'probability-statistics/事件的独立性'
  - 'probability-statistics/概率基础典型例题'
prerequisites: []
---

## 1. 全概率公式

### 1.1 样本空间的分割

设 $\Omega$ 为样本空间，$B_1, B_2, \cdots, B_n$ 为一组事件，若满足：

1. $B_i B_j = \varnothing$（$i \neq j$），即两两互斥
2. $\bigcup_{i=1}^{n} B_i = \Omega$
3. $P(B_i) > 0$（$i = 1, 2, \cdots, n$）

则称 $B_1, B_2, \cdots, B_n$ 为样本空间 $\Omega$ 的一个**分割**（或**完备事件组**）。

### 1.2 全概率公式

设 $B_1, B_2, \cdots, B_n$ 为样本空间 $\Omega$ 的一个分割，则对任意事件 $A$，有

$$P(A) = \sum_{i=1}^{n} P(B_i) P(A \mid B_i)$$

**证明**：

$$A = A\Omega = A\left(\bigcup_{i=1}^{n} B_i\right) = \bigcup_{i=1}^{n} AB_i$$

由于 $B_1, B_2, \cdots, B_n$ 两两互斥，故 $AB_1, AB_2, \cdots, AB_n$ 也两两互斥，由概率的有限可加性：

$$P(A) = \sum_{i=1}^{n} P(AB_i) = \sum_{i=1}^{n} P(B_i) P(A \mid B_i)$$

### 1.3 全概率公式的直观理解

全概率公式的核心思想是**化整为零**：将复杂事件 $A$ 的概率分解为在各种"原因" $B_i$ 下条件概率的加权平均，权重即为各"原因"的概率 $P(B_i)$。

### 1.4 全概率公式的应用

**例题**：某工厂有甲、乙、丙三条生产线生产同一种产品，产量分别占总产量的 25%、35%、40%，且各条生产线的次品率分别为 5%、4%、2%。现从总产品中任取一件，求取到次品的概率。

**解**：设 $A$ 为"取到次品"，$B_1, B_2, B_3$ 分别为"取到甲、乙、丙生产线的产品"，则

$$P(A) = P(B_1)P(A \mid B_1) + P(B_2)P(A \mid B_2) + P(B_3)P(A \mid B_3)$$

$$= 0.25 \times 0.05 + 0.35 \times 0.04 + 0.40 \times 0.02 = 0.0125 + 0.014 + 0.008 = 0.0345$$

## 2. 贝叶斯公式

### 2.1 贝叶斯公式的表述

设 $B_1, B_2, \cdots, B_n$ 为样本空间 $\Omega$ 的一个分割，$A$ 为任意事件且 $P(A) > 0$，则

$$P(B_k \mid A) = \frac{P(B_k) P(A \mid B_k)}{\sum_{i=1}^{n} P(B_i) P(A \mid B_i)}, \quad k = 1, 2, \cdots, n$$

**证明**：由条件概率定义和乘法公式：

$$P(B_k \mid A) = \frac{P(B_k A)}{P(A)} = \frac{P(B_k) P(A \mid B_k)}{P(A)}$$

分母用全概率公式展开即得。

### 2.2 贝叶斯公式的直观理解

贝叶斯公式体现了**由果溯因**的思想：

- $P(B_k)$：**先验概率**——在观察到结果 $A$ 之前，原因 $B_k$ 的概率
- $P(A \mid B_k)$：**似然函数**——在原因 $B_k$ 下，结果 $A$ 出现的概率
- $P(B_k \mid A)$：**后验概率**——观察到结果 $A$ 之后，原因 $B_k$ 的概率

贝叶斯公式描述了从先验概率到后验概率的**更新过程**：

$$\text{后验概率} = \frac{\text{先验概率} \times \text{似然函数}}{\text{全概率（归一化常数）}}$$

### 2.3 两个事件的贝叶斯公式

当 $n = 2$ 时，$B$ 和 $\bar{B}$ 构成 $\Omega$ 的分割：

$$P(B \mid A) = \frac{P(B) P(A \mid B)}{P(B) P(A \mid B) + P(\bar{B}) P(A \mid \bar{B})}$$

## 3. 贝叶斯公式的典型应用

### 3.1 医学检验问题

**问题**：某种疾病的患病率为 0.1%，现有一种检测方法，其灵敏度为 99%（即患者中 99% 检测为阳性），特异度为 95%（即非患者中 95% 检测为阴性）。现某人检测为阳性，求其确实患病的概率。

**解**：设 $D$ 为"患病"，$\bar{D}$ 为"未患病"，$+$ 为"检测阳性"。

已知：$P(D) = 0.001$，$P(+ \mid D) = 0.99$，$P(- \mid \bar{D}) = 0.95$

$$P(D \mid +) = \frac{P(D) P(+ \mid D)}{P(D) P(+ \mid D) + P(\bar{D}) P(+ \mid \bar{D})}$$

$$= \frac{0.001 \times 0.99}{0.001 \times 0.99 + 0.999 \times 0.05} = \frac{0.00099}{0.00099 + 0.04995} = \frac{0.00099}{0.05094} \approx 0.0194$$

虽然检测方法的灵敏度和特异度都很高，但由于患病率极低，阳性结果中真正患病的概率仅约 1.94%。

### 3.2 信号检测问题

**问题**：在通信系统中，发送端以概率 0.6 发送信号 0，以概率 0.4 发送信号 1。由于信道噪声，发送 0 时接收为 1 的概率为 0.2，发送 1 时接收为 0 的概率为 0.1。若接收端收到信号 1，求发送端确实发送了 1 的概率。

**解**：设 $S_0, S_1$ 分别表示发送 0 和 1，$R_0, R_1$ 分别表示接收 0 和 1。

$$P(S_1 \mid R_1) = \frac{P(S_1) P(R_1 \mid S_1)}{P(S_0) P(R_1 \mid S_0) + P(S_1) P(R_1 \mid S_1)}$$

$$= \frac{0.4 \times 0.9}{0.6 \times 0.2 + 0.4 \times 0.9} = \frac{0.36}{0.12 + 0.36} = \frac{0.36}{0.48} = 0.75$$

### 3.3 产品来源追溯

**问题**：某商店从甲、乙两厂采购同种商品，甲厂占 60%，乙厂占 40%。甲厂次品率为 2%，乙厂次品率为 1%。现发现一件次品，求该次品来自甲厂的概率。

**解**：

$$P(\text{甲} \mid \text{次品}) = \frac{0.6 \times 0.02}{0.6 \times 0.02 + 0.4 \times 0.01} = \frac{0.012}{0.012 + 0.004} = \frac{0.012}{0.016} = 0.75$$

## 4. 贝叶斯公式的推广

### 4.1 序贯贝叶斯更新

若连续获得多个观察结果 $A_1, A_2, \cdots, A_m$，则后验概率可以序贯更新：

$$P(B_k \mid A_1 A_2 \cdots A_m) = \frac{P(B_k) P(A_1 A_2 \cdots A_m \mid B_k)}{\sum_{i=1}^{n} P(B_i) P(A_1 A_2 \cdots A_m \mid B_i)}$$

若 $A_1, A_2, \cdots, A_m$ 在给定 $B_k$ 的条件下条件独立，则

$$P(A_1 A_2 \cdots A_m \mid B_k) = \prod_{j=1}^{m} P(A_j \mid B_k)$$

### 4.2 贝叶斯公式与决策论

贝叶斯公式是贝叶斯决策论的基础。在统计决策中，选择使后验期望损失最小的行动。

### 4.3 贝叶斯学派与频率学派

- **频率学派**：概率是长期频率的极限，参数是固定但未知的常数
- **贝叶斯学派**：概率是主观信念的度量，参数是随机变量，有先验分布

贝叶斯公式是贝叶斯统计推断的核心工具，它将先验信息与样本信息结合，得到后验分布。

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
| 贝叶斯公式 | 005-BayesFormula | 本文自身 |
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
| Z检验 | 041-ZTest | 本文的并列主题 |
| t检验 | 042-TTest | 本文的并列主题 |
| 卡方检验 | 043-ChiSquareTest | 本文的并列主题 |
| F检验 | 044-FTest | 本文的并列主题 |
| 假设检验典型例题 | 045-HypothesisTestingExamples | 本文的并列主题 |
