---
order: 300
title: 估计量的评选标准
module: 'probability-statistics'
category: 数学
difficulty: intermediate
description: '无偏性、有效性、一致性（相合性）的定义与判定，从"评委打分"类比理解估计量优劣评价体系。'
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/035-PointEstimation'
  - 'probability-statistics/037-IntervalEstimation'
  - 'probability-statistics/038-NormalPopulationParameterIntervalEstimation'
prerequisites:
  - 'probability-statistics/001-SampleSpaceAndEvent'
---


## 0. 评委打分，选谁当"最佳估计"？

综艺节目选秀，选手（估计量）一个个上台表演。评委（统计学家）手里有三张打分卡：

1. **无偏性卡**：你表演的平均水平是否接近真实实力？——估计量的**期望**是否等于真值。
2. **有效性卡**：你每次表演的发挥是否稳定？——估计量的**方差**是否够小。
3. **相合性卡**：给你更多次表演机会（更大样本），你是否越来越接近真实实力？——样本量增大时是否收敛到真值。

三位评委各有侧重：无偏性看"不偏不倚"，有效性看"稳定发挥"，相合性看"越练越准"。**一个优秀的估计量，应该同时通过这三关。**

本文用**评价驱动**的方式展开：把"如何评选估计量"作为主线，逐一介绍三大标准——定义、判定方法、典型例子，最后用均方误差（MSE）把三条标准统一起来。

## 1. 无偏性：不偏不倚，平均水平等于真值

### 1.1 定义

设 $\hat{\theta}$ 是参数 $\theta$ 的估计量，若对一切 $\theta \in \Theta$，有

$$E(\hat{\theta}) = \theta$$

则称 $\hat{\theta}$ 是 $\theta$ 的**无偏估计量**（或**无偏估计**）。

若 $E(\hat{\theta}) \neq \theta$，则称 $\hat{\theta}$ 是 $\theta$ 的**有偏估计**，差值 $E(\hat{\theta}) - \theta$ 称为**偏差**。

**直观理解**：把估计量反复使用无数次（每次换一批样本），平均下来正好打在靶心，没有系统性偏移。就像老练的射箭手，虽然每箭有散布，但平均落点就是靶心。

### 1.2 渐近无偏性

若 $\lim_{n \to \infty} E(\hat{\theta}_n) = \theta$，则称 $\hat{\theta}_n$ 是 $\theta$ 的**渐近无偏估计**。样本量越大，偏差越趋近于零。

### 1.3 常见估计的无偏性盘点

| 估计量 | 估计对象 | 无偏性 | 说明 |
| --- | --- | --- | --- |
| $\bar{X}$ | $\mu$ | 无偏 | $E(\bar{X}) = \mu$ |
| $S^2 = \frac{1}{n-1}\sum (X_i-\bar X)^2$ | $\sigma^2$ | 无偏 | $E(S^2) = \sigma^2$ |
| $B_2 = \frac{1}{n}\sum (X_i-\bar X)^2$ | $\sigma^2$ | 有偏（渐近无偏） | $E(B_2) = \frac{n-1}{n}\sigma^2$ |
| $A_k = \frac{1}{n}\sum X_i^k$ | $\mu_k = E(X^k)$ | 无偏 | $E(A_k) = \mu_k$ |
| MLE 的 $\hat{\sigma}^2$ | $\sigma^2$ | 有偏（渐近无偏） | $E(\hat{\sigma}^2) = \frac{n-1}{n}\sigma^2$ |

### 1.4 无偏性不唯一

同一个参数可以有无穷多个无偏估计。例如，$\bar{X}$ 是 $\mu$ 的无偏估计，单独取第一个样本 $X_1$ 也是 $\mu$ 的无偏估计（$E(X_1) = \mu$）。甚至 $0.3X_1 + 0.7\bar{X}$ 也是无偏的。

无偏性只保证了"平均正确"，没有保证"单个估计离真值近"。所以还需要第二个标准。

## 2. 有效性：同样无偏，方差越小越优

### 2.1 定义

设 $\hat{\theta}_1$ 和 $\hat{\theta}_2$ 都是 $\theta$ 的无偏估计，若对一切 $\theta \in \Theta$，有

$$D(\hat{\theta}_1) \leq D(\hat{\theta}_2)$$

且至少存在一个 $\theta$ 使不等号严格成立，则称 $\hat{\theta}_1$ 比 $\hat{\theta}_2$ **有效**。

**直观理解**：两位选手都"平均准"，但一位每次发挥波动小、一位忽高忽低。当然选波动小的——方差越小，单次估计落在真值附近的概率越高。

### 2.2 最小方差无偏估计（MVUE）

若 $\hat{\theta}^*$ 是 $\theta$ 的无偏估计，且对 $\theta$ 的任何无偏估计 $\hat{\theta}$，都有

$$D(\hat{\theta}^*) \leq D(\hat{\theta})$$

则称 $\hat{\theta}^*$ 为 $\theta$ 的**最小方差无偏估计**（MVUE）。这是"无偏 + 有效"的完美结合，是评选体系中的"冠军"。

### 2.4 克拉默-拉奥下界（C-R 下界）：有效性的"天花板"

设总体 $X$ 的密度函数为 $f(x; \theta)$，满足一定正则条件，则 $\theta$ 的任何无偏估计 $\hat{\theta}$ 的方差满足

$$D(\hat{\theta}) \geq \frac{1}{nI(\theta)}$$

其中

$$I(\theta) = E\left[\left(\frac{\partial \ln f(X; \theta)}{\partial \theta}\right)^2\right] = -E\left[\frac{\partial^2 \ln f(X; \theta)}{\partial \theta^2}\right]$$

称为 **Fisher 信息量**（刻画了分布"含有多少关于 $\theta$ 的信息"）。

若某个无偏估计的方差恰好达到 C-R 下界，则它一定是 MVUE（且称为**有效估计**）。例如正态总体 $N(\mu, \sigma^2)$ 中，$\bar{X}$ 的方差 $\sigma^2/n$ 恰好等于下界 $1/(nI(\mu)) = \sigma^2/n$，所以 $\bar{X}$ 是 $\mu$ 的有效估计。

## 3. 相合性（一致性）：越练越准

### 3.1 定义

设 $\hat{\theta}_n$ 是参数 $\theta$ 的估计量（下标 $n$ 表示样本量），若对任意 $\varepsilon > 0$，

$$\lim_{n \to \infty} P(|\hat{\theta}_n - \theta| < \varepsilon) = 1$$

即 $\hat{\theta}_n \xrightarrow{P} \theta$（依概率收敛），则称 $\hat{\theta}_n$ 是 $\theta$ 的**一致估计**（或**相合估计**）。

**直观理解**：无论允许误差 $\varepsilon$ 多小，只要样本足够大，估计量几乎必然落在 $\theta$ 的 $\varepsilon$ 邻域内。"样本量越大越接近真相"，这是估计量的底线要求——一个不相合的估计量，加大样本毫无意义。

### 3.2 相合性的判定定理

**定理**：若 $\hat{\theta}_n$ 是 $\theta$ 的渐近无偏估计，且 $\lim_{n \to \infty} D(\hat{\theta}_n) = 0$，则 $\hat{\theta}_n$ 是 $\theta$ 的一致估计。

**证明**（用到切比雪夫不等式）：对任意 $\varepsilon > 0$，

$$P(|\hat{\theta}_n - E(\hat{\theta}_n)| \geq \varepsilon) \leq \frac{D(\hat{\theta}_n)}{\varepsilon^2} \to 0$$

即 $\hat{\theta}_n - E(\hat{\theta}_n) \xrightarrow{P} 0$；又 $E(\hat{\theta}_n) \to \theta$，合起来得到 $\hat{\theta}_n \xrightarrow{P} \theta$。

> 这条定理非常实用：**证明相合性的通用套路 = 验证渐近无偏 + 验证方差趋于 0**。

### 3.3 常见估计的相合性

- $\bar{X}$ 是 $\mu$ 的一致估计（由大数定律直接得到）；
- $S^2$ 是 $\sigma^2$ 的一致估计（$E(S^2) = \sigma^2$ 且 $D(S^2) \to 0$）；
- $A_k$ 是 $\mu_k$ 的一致估计（大数定律推广）；
- MLE 在一定正则条件下相合（上一篇已提）。

## 4. 三个标准的统一：均方误差（MSE）

### 4.1 定义

三个标准各管一面，能否用一个指标统一？答案是**均方误差**：

$$\text{MSE}(\hat{\theta}) = E(\hat{\theta} - \theta)^2 = D(\hat{\theta}) + [E(\hat{\theta}) - \theta]^2 = \text{方差} + \text{偏差}^2$$

MSE 把"方差"和"偏差"打包成一个数：偏差大了不行（不准），方差大了也不行（不稳）。

### 4.2 偏差-方差权衡

有时一个有偏估计的 MSE 反而比无偏估计更小。经典例子：岭回归（Ridge Regression）牺牲一点无偏性，大幅缩小方差，使 MSE 整体下降；上一篇文章中 $U(0,\theta)$ 的 MLE $\hat{\theta} = X_{(n)}$ 有偏，但方差小、MSE 通常优于无偏修正 $\dfrac{n+1}{n}X_{(n)}$。

**结论**：评选不是"唯无偏论"，要综合看 MSE。机器学习中"偏差-方差权衡"（bias-variance tradeoff）正是这一思想的直接应用。

### 4.3 三个标准的定位比较

| 标准 | 关注点 | 性质表述 | 样本量要求 | 优先级 |
| --- | --- | --- | --- | --- |
| 无偏性 | 平均水平是否等于真值 | $E(\hat{\theta}) = \theta$ | 有限样本 | 中等 |
| 有效性 | 无偏估计中方差是否最小 | $D(\hat{\theta})$ 最小 | 有限样本 | 最高（同无偏时） |
| 相合性 | 样本增大是否收敛于真值 | $\hat{\theta}_n \xrightarrow{P} \theta$ | 大样本 | 最基本（底线） |
| MSE | 偏差与方差的综合 | $\text{MSE} = D + \text{偏差}^2$ | 任意 | 综合指标 |

**实际使用顺序**：先用相合性淘汰"越学越差"的估计量，再在无偏的候选里比有效性，若不得不有偏，则看 MSE 谁更小。

## 5. 常见错误与对策

| 错误类型 | 错误示例 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 混淆"无偏"与"单个准" | 认为无偏估计一定单次接近真值 | 无偏是"平均"概念，不是"每次"概念 | 无偏只保证 $E(\hat{\theta}) = \theta$，单次误差由方差决定 |
| 比较有效性忘前提 | 直接比两个有偏估计的方差 | 有效性定义限定在"无偏估计之间" | 先验证两个估计都无偏，再比方差 |
| 相合性证明无章法 | 不知道从哪下手 | 不知道判定定理 | 套路：渐近无偏 + 方差 $\to 0$，再用切比雪夫不等式 |
| 误判 $B_2$ 无偏 | 把 $\frac{1}{n}\sum (X_i-\bar X)^2$ 当 $\sigma^2$ 的无偏估计 | 忘记自由度修正 | $E(B_2) = \frac{n-1}{n}\sigma^2$，无偏版是 $S^2$ |
| 忽略 C-R 下界条件 | 任意分布都套 C-R 下界 | 正则条件不满足（如均匀分布） | 均匀分布等"定义域依赖 $\theta$"的分布没有常规 C-R 下界，不能套用 |
| MSE 计算错误 | 忘记展开式 | 把 MSE 当方差 | $\text{MSE} = D(\hat{\theta}) + [\text{偏差}]^2$，偏差为零时才退化为方差 |

## 7. 一句话记忆

**评选估计量看三关：无偏性（平均打中靶心）、有效性（无偏者中方差最小）、相合性（样本越大越准），三关可统一成均方误差 MSE = 方差 + 偏差平方。**
