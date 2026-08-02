---
order: 50
title: 切比雪夫不等式
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 切比雪夫不等式的表述、推导（马尔可夫不等式）、应用（估计概率、确定样本量）、推广与局限性。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/矩与协方差矩阵'
  - 'probability-statistics/大数定律'
  - 'probability-statistics/中心极限定理'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 0. 从一个生活场景说起：即使不知道规则，也能划出"安全范围"

学校要评估一门考试的成绩稳定性，但新来的老师既不知道分数服从什么分布（正态？偏态？），手里只有两个数：平均分 70，标准差 5。他能对"分数落在 60 到 80 之间的人数比例"给出任何承诺吗？

能！切比雪夫不等式（Chebyshev's Inequality）就是这样的"安全网"：**只要知道期望和方差，不需要知道分布的细节，就能对"取值落在均值附近"的概率给出保证**。它不追求精确，只给出一个保守但绝对可靠的界限——好比保险公司不知道每位客户的赔付细节，但能保证"赔付总额落在某个范围内"。

本文采用"**不等式驱动**"的叙事结构：先讲它要回答什么问题，再从马尔可夫不等式一步步推出切比雪夫不等式，然后演示三大应用（估计概率、确定样本量、证明相合性），最后讨论它的保守性与推广。

## 1. 切比雪夫不等式：定理表述

### 1.1 定理

设随机变量 $X$ 的期望 $E(X) = \mu$ 和方差 $D(X) = \sigma^2$ 都存在，则对任意 $\varepsilon > 0$，有

$$P(|X - \mu| \geq \varepsilon) \leq \frac{\sigma^2}{\varepsilon^2}$$

等价形式（常用）：

$$P(|X - \mu| < \varepsilon) \geq 1 - \frac{\sigma^2}{\varepsilon^2}$$

### 1.2 标准差形式

令 $\varepsilon = k\sigma$（$k > 0$），则

$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$$

这条形式更好记：**"偏离均值至少 $k$ 个标准差的概率不超过 $1/k^2$"**。例如：

- $P(|X - \mu| \geq 2\sigma) \leq \dfrac{1}{4}$：落在 2 个标准差之外的概率至多 25%；
- $P(|X - \mu| \geq 3\sigma) \leq \dfrac{1}{9}$：落在 3 个标准差之外的概率至多约 11%。

对比正态分布：$P(|X - \mu| \geq 2\sigma) \approx 0.0455$，$P(|X - \mu| \geq 3\sigma) \approx 0.0027$——切比雪夫的界**松得多**，因为它对任何分布都成立（详情见"局限性"一节）。

## 2. 推导：从马尔可夫不等式出发

### 2.1 马尔可夫不等式

设 $Y$ 是非负随机变量（$P(Y \geq 0) = 1$），$E(Y)$ 存在，则对任意 $a > 0$：

$$P(Y \geq a) \leq \frac{E(Y)}{a}$$

**证明（离散型直觉）**：若 $Y \geq a$，则 $\dfrac{Y}{a} \geq 1$；更一般地恒有 $Y \geq a \cdot \mathbf{1}_{\{Y \geq a\}}$。两边取期望：

$$E(Y) \geq a \cdot P(Y \geq a) \quad \Longrightarrow \quad P(Y \geq a) \leq \frac{E(Y)}{a}$$

### 2.2 切比雪夫不等式的推导

令 $Y = (X - \mu)^2 \geq 0$，$a = \varepsilon^2 > 0$，对 $Y$ 应用马尔可夫不等式：

$$P\left((X - \mu)^2 \geq \varepsilon^2\right) \leq \frac{E[(X - \mu)^2]}{\varepsilon^2} = \frac{D(X)}{\varepsilon^2}$$

而事件 $\{(X - \mu)^2 \geq \varepsilon^2\}$ 与 $\{|X - \mu| \geq \varepsilon\}$ 等价，故

$$P(|X - \mu| \geq \varepsilon) \leq \frac{\sigma^2}{\varepsilon^2}$$

**推导的巧妙之处**：把"绝对值"问题平方成"非负变量"问题，就能套用马尔可夫不等式；而 $E[(X-\mu)^2]$ 正是方差。整个证明只需三行，却揭示了"期望 → 方差 → 概率界限"的完整链条。

## 3. 应用一：不知道分布时估计概率

## 4. 应用二：确定样本量

## 5. 应用三：证明估计的相合性

## 6. 推广：马尔可夫、单边、多维形式

### 6.1 马尔可夫不等式（再回顾）

$$P(X \geq \varepsilon) \leq \frac{E(X)}{\varepsilon}, \qquad X \geq 0$$

### 6.2 单边切比雪夫不等式

设 $E(X) = \mu$，$D(X) = \sigma^2$，则对任意 $a > 0$：

$$P(X - \mu \geq a) \leq \frac{\sigma^2}{\sigma^2 + a^2}$$

单边形式只关心"右侧偏差"，比双边形式更精细（上界分母多了 $a^2$）。

### 6.3 多维切比雪夫不等式

设 $\mathbf{X}$ 为 $n$ 维随机向量，$E(\mathbf{X}) = \boldsymbol{\mu}$，协方差矩阵为 $\boldsymbol{\Sigma}$（正定），则对任意 $\varepsilon > 0$：

$$P\left((\mathbf{X} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{X} - \boldsymbol{\mu}) \geq \varepsilon\right) \leq \frac{n}{\varepsilon}$$

这是切比雪夫不等式在高维的推广，用马氏距离 $\sqrt{(\mathbf{X}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{X}-\boldsymbol{\mu})}$ 衡量偏离（马氏距离的异常检测应用即源于此）。

## 7. 局限性：切比雪夫的"保守"

### 7.1 界偏松

切比雪夫不等式不依赖分布，代价是界限很保守。

### 7.2 什么时候该用它

- 分布未知或难以计算，只需要**粗粒度保证**时；
- 证明理论结果（大数定律、相合性）时——此时精确概率不重要，重要的是"上界能趋于 0"；
- 分布已知时，应改用精确计算或中心极限定理（更紧的近似）。

## 8. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 把 $\sigma^2$ 当成 $\sigma$ 代入分子 | 公式误用 | 记错不等式形式 | $P(|X-\mu| \ge \varepsilon) \le \dfrac{\sigma^2}{\varepsilon^2}$，分子是**方差**；标准差形式用 $\dfrac{1}{k^2}$ |
| 用切比雪夫算精确概率 | 概念错误 | 忘记它只给上界/下界 | 它给出的是"至少/至多"的保证；分布已知时直接用分布函数 |
| 把 $\varepsilon$ 换成 $k\sigma$ 后忘掉 $\dfrac{1}{k^2}$ | 换算错误 | 变量替换不熟练 | 若 $\varepsilon = k\sigma$，则 $\sigma^2/\varepsilon^2 = 1/k^2$ |
| 对 $P(X \ge \varepsilon)$ 直接用双边公式 | 形式误用 | 单边事件 ≠ 双边事件 | 单边事件是其子集：$P(X-\mu \ge a) \le P(|X-\mu| \ge a)$，或改用单边切比雪夫 |
| 忘记要求 $\sigma^2$ 存在 | 前提遗漏 | 方差不存在时公式无意义 | 使用前确认 $D(X)$ 存在；柯西分布连期望都不存在，不适用 |
| 认为切比雪夫界可以替代正态计算 | 过度使用 | 忽略保守性 | 分布已知优先精确计算或 CLT；切比雪夫用于"未知分布 + 粗保证"或理论证明 |

## 10. 一句话记忆

切比雪夫不等式是"不知道分布也敢打包票"的安全网：$P(|X - \mu| \geq \varepsilon) \leq \dfrac{\sigma^2}{\varepsilon^2}$（或 $P(|X-\mu| \geq k\sigma) \leq \dfrac{1}{k^2}$），由马尔可夫不等式平方一步推出，用"期望+方差"为概率划出保守但可靠的界限。

## 延伸阅读
概率统计基础，见 030-probability-statistics 模块文档。
数据分析应用，见 051-data-analysis 模块。
机器学习概率视角，见 042-machine-learning 模块（AI 模块仅供了解）。
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
