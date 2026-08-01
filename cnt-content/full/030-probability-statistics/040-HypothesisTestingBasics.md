---
order: 80
title: 假设检验基本概念
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 假设检验的基本概念：原假设、备择假设、显著性水平、两类错误、检验步骤。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/正态总体参数的区间估计'
  - 'probability-statistics/参数估计典型例题'
  - 'probability-statistics/Z检验'
  - 'probability-statistics/t检验'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 假设检验的基本思想

### 1.1 统计假设

**统计假设**是关于总体分布中未知参数或分布形式的陈述。

- **参数假设**：关于参数的假设，如 $H: \mu = \mu_0$
- **非参数假设**：关于分布形式的假设，如 $H: X \sim N(\mu, \sigma^2)$

### 1.2 原假设与备择假设

- **原假设**（零假设）$H_0$：需要检验的假设，通常表示"没有效果"、"没有差异"
- **备择假设**（对立假设）$H_1$（或 $H_A$）：与原假设对立的假设

三种形式：

| 检验类型 | $H_0$            | $H_1$            |
| -------- | ---------------- | ---------------- |
| 双侧检验 | $\mu = \mu_0$    | $\mu \neq \mu_0$ |
| 右侧检验 | $\mu \leq \mu_0$ | $\mu > \mu_0$    |
| 左侧检验 | $\mu \geq \mu_0$ | $\mu < \mu_0$    |

### 1.3 假设检验的逻辑

假设检验采用**反证法**的思想：

1. 假设 $H_0$ 成立
2. 在 $H_0$ 下，推导样本应满足的结论
3. 若样本观测值与结论矛盾（小概率事件发生），则拒绝 $H_0$
4. 若不矛盾，则不能拒绝 $H_0$（但不等于接受 $H_0$）

## 2. 两类错误

### 2.1 定义

|              | $H_0$ 为真             | $H_0$ 为假             |
| ------------ | ---------------------- | ---------------------- |
| 拒绝 $H_0$   | **第一类错误**（弃真） | 正确决策               |
| 不拒绝 $H_0$ | 正确决策               | **第二类错误**（取伪） |

- **第一类错误**（弃真错误）：$H_0$ 为真时拒绝 $H_0$，概率为 $\alpha$
- **第二类错误**（取伪错误）：$H_0$ 为假时不拒绝 $H_0$，概率为 $\beta$

### 2.2 显著性水平

$$\alpha = P(\text{拒绝 } H_0 \mid H_0 \text{ 为真})$$

$\alpha$ 称为**显著性水平**，通常取 $\alpha = 0.05$ 或 $\alpha = 0.01$。

### 2.3 两类错误的关系

- 在样本量固定时，减小 $\alpha$ 会增大 $\beta$，反之亦然
- 同时减小 $\alpha$ 和 $\beta$ 的唯一方法是增大样本量
- Neyman-Pearson 原则：在控制 $\alpha$ 的条件下，使 $\beta$ 尽可能小

### 2.4 检验的功效

$$1 - \beta = P(\text{拒绝 } H_0 \mid H_1 \text{ 为真})$$

称为检验的**功效**（或**势函数**）。功效越大，检验越好。

## 3. 检验统计量与拒绝域

### 3.1 检验统计量

用于检验假设的统计量称为**检验统计量**，通常选择在 $H_0$ 下分布已知的枢轴量。

### 3.2 拒绝域

使 $H_0$ 被拒绝的检验统计量的取值范围称为**拒绝域**（或**临界域**），记作 $W$。

- 双侧检验：$W = \{|T| > c\}$
- 右侧检验：$W = \{T > c\}$
- 左侧检验：$W = \{T < c\}$

### 3.3 临界值

拒绝域的边界值称为**临界值**，由显著性水平 $\alpha$ 和检验统计量的分布确定。

## 4. P 值

### 4.1 定义

**P 值**是在 $H_0$ 成立的条件下，检验统计量取到观测值及更极端值的概率。

$$\text{P 值} = P(\text{检验统计量} \geq \text{观测值} \mid H_0)$$

### 4.2 P 值的判断

- 若 $\text{P 值} \leq \alpha$，拒绝 $H_0$
- 若 $\text{P 值} > \alpha$，不拒绝 $H_0$

### 4.3 P 值的意义

P 值越小，反对 $H_0$ 的证据越强：

- $P < 0.01$：非常显著
- $0.01 \leq P < 0.05$：显著
- $0.05 \leq P < 0.10$：边缘显著
- $P \geq 0.10$：不显著

## 5. 假设检验的步骤

1. **提出假设**：根据问题建立 $H_0$ 和 $H_1$
2. **选择检验统计量**：确定在 $H_0$ 下分布已知的统计量
3. **确定显著性水平**：通常取 $\alpha = 0.05$
4. **计算检验统计量的值**：由样本数据计算
5. **确定拒绝域**：由 $\alpha$ 和统计量的分布确定
6. **做出决策**：比较统计量的值与临界值，或比较 P 值与 $\alpha$
7. **得出结论**：在问题背景下解释检验结果

## 6. 假设检验的注意事项

### 6.1 统计显著 vs 实际显著

统计显著性只说明结果不太可能由偶然因素产生，不代表实际意义大。效应量（effect size）也是重要的。

### 6.2 不能拒绝 ≠ 接受

"不能拒绝 $H_0$"不等于"接受 $H_0$"。只能说当前证据不足以拒绝 $H_0$。

### 6.3 多重检验

同时进行多个检验时，犯第一类错误的概率会增大，需要进行校正（如 Bonferroni 校正）。

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
| 假设检验基本概念 | 040-HypothesisTestingBasics | 本文自身 |
| Z检验 | 041-ZTest | 本文的并列主题 |
| t检验 | 042-TTest | 本文的并列主题 |
| 卡方检验 | 043-ChiSquareTest | 本文的并列主题 |
| F检验 | 044-FTest | 本文的并列主题 |
| 假设检验典型例题 | 045-HypothesisTestingExamples | 本文的并列主题 |
