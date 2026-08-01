---
order: 71
title: 估计量的评选标准
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 无偏性、有效性、一致性（相合性）的定义与判定。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/抽样分布典型例题'
  - 'probability-statistics/点估计'
  - 'probability-statistics/区间估计'
  - 'probability-statistics/正态总体参数的区间估计'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 1. 无偏性

### 1.1 定义

设 $\hat{\theta}$ 是参数 $\theta$ 的估计量，若对一切 $\theta \in \Theta$，有

$$E(\hat{\theta}) = \theta$$

则称 $\hat{\theta}$ 是 $\theta$ 的**无偏估计量**（或**无偏估计**）。

若 $E(\hat{\theta}) \neq \theta$，则称 $\hat{\theta}$ 是 $\theta$ 的**有偏估计**，$E(\hat{\theta}) - \theta$ 称为**偏差**。

### 1.2 渐近无偏性

若 $\lim_{n \to \infty} E(\hat{\theta}_n) = \theta$，则称 $\hat{\theta}_n$ 是 $\theta$ 的**渐近无偏估计**。

### 1.3 常见估计的无偏性

**样本均值**：$E(\bar{X}) = \mu$，$\bar{X}$ 是 $\mu$ 的无偏估计。

**样本方差**：$E(S^2) = \sigma^2$，$S^2$ 是 $\sigma^2$ 的无偏估计。

**二阶中心矩**：$E(B_2) = E\left(\dfrac{1}{n}\sum(X_i - \bar{X})^2\right) = \dfrac{n-1}{n}\sigma^2$，$B_2$ 不是 $\sigma^2$ 的无偏估计，但渐近无偏。

### 1.4 无偏性的意义

无偏性意味着估计量在大量重复使用时，平均来说没有系统偏差。

### 1.5 无偏性不唯一

同一个参数可以有无穷多个无偏估计。例如，$\bar{X}$ 是 $\mu$ 的无偏估计，$X_1$ 也是 $\mu$ 的无偏估计。

## 2. 有效性

### 2.1 定义

设 $\hat{\theta}_1$ 和 $\hat{\theta}_2$ 都是 $\theta$ 的无偏估计，若对一切 $\theta \in \Theta$，有

$$D(\hat{\theta}_1) \leq D(\hat{\theta}_2)$$

且至少存在一个 $\theta$ 使不等号严格成立，则称 $\hat{\theta}_1$ 比 $\hat{\theta}_2$ **有效**。

### 2.2 最小方差无偏估计（MVUE）

若 $\hat{\theta}^*$ 是 $\theta$ 的无偏估计，且对 $\theta$ 的任何无偏估计 $\hat{\theta}$，都有

$$D(\hat{\theta}^*) \leq D(\hat{\theta})$$

则称 $\hat{\theta}^*$ 为 $\theta$ 的**最小方差无偏估计**（MVUE）。

### 2.3 克拉默-拉奥下界（C-R 下界）

设总体 $X$ 的密度函数为 $f(x; \theta)$，满足一定正则条件，则 $\theta$ 的任何无偏估计 $\hat{\theta}$ 的方差满足

$$D(\hat{\theta}) \geq \frac{1}{nI(\theta)}$$

其中

$$I(\theta) = E\left[\left(\frac{\partial \ln f(X; \theta)}{\partial \theta}\right)^2\right] = -E\left[\frac{\partial^2 \ln f(X; \theta)}{\partial \theta^2}\right]$$

称为 **Fisher 信息量**。

若某个无偏估计的方差达到 C-R 下界，则它一定是 MVUE。

### 2.4 示例

**例题**：设 $X_1, \cdots, X_n \sim N(\mu, \sigma^2)$，比较 $\bar{X}$ 和 $X_1$ 作为 $\mu$ 的估计的有效性。

**解**：两者都是 $\mu$ 的无偏估计。

$$D(\bar{X}) = \frac{\sigma^2}{n}, \quad D(X_1) = \sigma^2$$

当 $n > 1$ 时，$D(\bar{X}) < D(X_1)$，故 $\bar{X}$ 比 $X_1$ 有效。

## 3. 一致性（相合性）

### 3.1 定义

设 $\hat{\theta}_n$ 是参数 $\theta$ 的估计量，若对任意 $\varepsilon > 0$，

$$\lim_{n \to \infty} P(|\hat{\theta}_n - \theta| < \varepsilon) = 1$$

即 $\hat{\theta}_n \xrightarrow{P} \theta$，则称 $\hat{\theta}_n$ 是 $\theta$ 的**一致估计**（或**相合估计**）。

### 3.2 一致性的判定

**定理**：若 $\hat{\theta}_n$ 是 $\theta$ 的渐近无偏估计，且 $\lim_{n \to \infty} D(\hat{\theta}_n) = 0$，则 $\hat{\theta}_n$ 是 $\theta$ 的一致估计。

**证明**：由切比雪夫不等式，$P(|\hat{\theta}_n - E(\hat{\theta}_n)| \geq \varepsilon) \leq \dfrac{D(\hat{\theta}_n)}{\varepsilon^2} \to 0$。

再由 $E(\hat{\theta}_n) \to \theta$，可得 $\hat{\theta}_n \xrightarrow{P} \theta$。

### 3.3 常见估计的一致性

- $\bar{X}$ 是 $\mu$ 的一致估计（由大数定律）
- $S^2$ 是 $\sigma^2$ 的一致估计
- $A_k$ 是 $\mu_k$ 的一致估计

### 3.4 一致性的意义

一致性是最基本的要求：当样本量增大时，估计量应越来越接近真实参数。如果一个估计量不是一致的，则增大样本量也不能改善估计精度。

## 4. 三个标准的关系

### 4.1 优先级

1. **一致性**是最基本的要求（大样本性质）
2. **无偏性**是中等要求（消除系统偏差）
3. **有效性**是更高要求（在无偏估计中选最优）

### 4.2 三个标准的比较

| 标准   | 性质         | 样本量要求 |
| ------ | ------------ | ---------- |
| 无偏性 | 期望等于真值 | 有限样本   |
| 有效性 | 方差最小     | 有限样本   |
| 一致性 | 依概率收敛   | 大样本     |

### 4.3 均方误差

$$\text{MSE}(\hat{\theta}) = E(\hat{\theta} - \theta)^2 = D(\hat{\theta}) + [E(\hat{\theta}) - \theta]^2 = D(\hat{\theta}) + \text{偏差}^2$$

MSE 综合考虑了偏差和方差，是评价估计量的更全面指标。有时一个有偏估计的 MSE 可能比无偏估计更小（偏差-方差权衡）。

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
