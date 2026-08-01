---
order: 24
title: 随机变量函数的分布
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 随机变量函数的分布求解方法：分布函数法、公式法、离散型随机变量函数的分布。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'probability-statistics/分布函数'
  - 'probability-statistics/常用分布'
  - 'probability-statistics/随机变量典型例题'
  - 'probability-statistics/联合分布'
prerequisites: []
---

## 1. 问题的提出

设 $X$ 是一个随机变量，其分布已知，$g(x)$ 是一个连续函数，如何求 $Y = g(X)$ 的分布？

这是概率论中的基本问题之一，主要有以下几种方法。

## 2. 分布函数法

### 2.1 基本思路

分布函数法是求随机变量函数分布的最基本方法，步骤如下：

1. 写出 $Y$ 的分布函数 $F_Y(y) = P(Y \leq y) = P(g(X) \leq y)$
2. 将不等式 $g(X) \leq y$ 转化为关于 $X$ 的不等式
3. 利用 $X$ 的分布求出 $F_Y(y)$
4. 对 $F_Y(y)$ 求导得到 $f_Y(y)$（连续型）

### 2.2 单调函数的情形

若 $g(x)$ 严格单调且可导，则 $Y = g(X)$ 的密度函数为：

$$f_Y(y) = \begin{cases} f_X(g^{-1}(y)) \cdot |(g^{-1}(y))'|, & y \in g \text{ 的值域} \\ 0, & \text{其他} \end{cases}$$

**推导**：设 $g$ 严格单调递增，则

$$F_Y(y) = P(g(X) \leq y) = P(X \leq g^{-1}(y)) = F_X(g^{-1}(y))$$

$$f_Y(y) = F_Y'(y) = f_X(g^{-1}(y)) \cdot (g^{-1}(y))'$$

若 $g$ 严格单调递减，则

$$F_Y(y) = P(g(X) \leq y) = P(X \geq g^{-1}(y)) = 1 - F_X(g^{-1}(y))$$

$$f_Y(y) = f_X(g^{-1}(y)) \cdot |(g^{-1}(y))'|$$

### 2.3 示例

**例题**：设 $X \sim N(0, 1)$，求 $Y = X^2$ 的分布。

**解**：

当 $y \leq 0$ 时，$F_Y(y) = 0$。

当 $y > 0$ 时：

$$F_Y(y) = P(X^2 \leq y) = P(-\sqrt{y} \leq X \leq \sqrt{y}) = \Phi(\sqrt{y}) - \Phi(-\sqrt{y}) = 2\Phi(\sqrt{y}) - 1$$

$$f_Y(y) = F_Y'(y) = 2\varphi(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} = \frac{1}{\sqrt{y}} \cdot \frac{1}{\sqrt{2\pi}} e^{-y/2} = \frac{1}{\sqrt{2\pi y}} e^{-y/2}$$

即 $Y \sim \chi^2(1)$。

## 3. 公式法

### 3.1 适用条件

当 $g(x)$ 严格单调且可导时，可直接使用公式：

$$f_Y(y) = f_X(h(y)) \cdot |h'(y)|$$

其中 $h(y) = g^{-1}(y)$ 是 $g$ 的反函数。

### 3.2 常见变换

**线性变换**：$Y = aX + b$（$a \neq 0$）

$$f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y - b}{a}\right)$$

特别地，若 $X \sim N(\mu, \sigma^2)$，则 $Y = aX + b \sim N(a\mu + b, a^2\sigma^2)$。

**幂变换**：$Y = X^2$（$X > 0$）

$$f_Y(y) = \frac{1}{2\sqrt{y}} f_X(\sqrt{y}), \quad y > 0$$

**指数变换**：$Y = e^X$

$$f_Y(y) = \frac{1}{y} f_X(\ln y), \quad y > 0$$

**对数变换**：$Y = \ln X$（$X > 0$）

$$f_Y(y) = e^y f_X(e^y)$$

### 3.3 公式法的局限性

当 $g(x)$ 不单调时，公式法不能直接使用，需要用分布函数法分段处理。

## 4. 非单调函数的处理

### 4.1 分段单调

若 $g(x)$ 在若干区间上分别单调，则在每个单调区间上分别使用公式法，然后求和。

**例题**：设 $X \sim N(0, 1)$，求 $Y = |X|$ 的分布。

**解**：$y = |x|$ 在 $(-\infty, 0)$ 上单调递减，在 $(0, +\infty)$ 上单调递增。

当 $y > 0$ 时：

$$F_Y(y) = P(|X| \leq y) = P(-y \leq X \leq y) = \Phi(y) - \Phi(-y) = 2\Phi(y) - 1$$

$$f_Y(y) = 2\varphi(y) = \frac{2}{\sqrt{2\pi}} e^{-y^2/2}, \quad y > 0$$

### 4.2 一般方法

对于一般的 $g(x)$：

1. 对每个 $y$，求出 $\{x : g(x) \leq y\}$ 的范围
2. 利用 $X$ 的分布计算 $P(g(X) \leq y)$
3. 对 $F_Y(y)$ 求导

## 5. 离散型随机变量函数的分布

### 5.1 方法

设 $X$ 为离散型随机变量，分布律为 $P(X = x_k) = p_k$，$Y = g(X)$。

1. 列出 $Y$ 的所有可能取值 $y_1, y_2, \cdots$
2. 对每个 $y_j$，计算 $P(Y = y_j) = \sum_{g(x_k) = y_j} p_k$

### 5.2 示例

**例题**：设 $X$ 的分布律为：

| $X$ | $-1$  | $0$   | $1$   | $2$   |
| --- | ----- | ----- | ----- | ----- |
| $P$ | $0.2$ | $0.3$ | $0.1$ | $0.4$ |

求 $Y = X^2$ 的分布律。

**解**：$Y$ 的可能取值为 $0, 1, 4$。

$$P(Y = 0) = P(X = 0) = 0.3$$

$$P(Y = 1) = P(X = -1) + P(X = 1) = 0.2 + 0.1 = 0.3$$

$$P(Y = 4) = P(X = 2) = 0.4$$

| $Y$ | $0$   | $1$   | $4$   |
| --- | ----- | ----- | ----- |
| $P$ | $0.3$ | $0.3$ | $0.4$ |

## 6. 常见变换总结

### 6.1 正态分布的变换

| 变换                          | $X$ 的分布         | $Y$ 的分布                 |
| ----------------------------- | ------------------ | -------------------------- |
| $Y = aX + b$                  | $N(\mu, \sigma^2)$ | $N(a\mu + b, a^2\sigma^2)$ |
| $Y = X^2$                     | $N(0, 1)$          | $\chi^2(1)$                |
| $Y = \dfrac{X - \mu}{\sigma}$ | $N(\mu, \sigma^2)$ | $N(0, 1)$                  |
| $Y = e^X$                     | $N(\mu, \sigma^2)$ | 对数正态分布               |

### 6.2 均匀分布的变换

| 变换            | $X$ 的分布 | $Y$ 的分布      |
| --------------- | ---------- | --------------- |
| $Y = aX + b$    | $U(0, 1)$  | $U(b, a + b)$   |
| $Y = -\ln X$    | $U(0, 1)$  | $\text{Exp}(1)$ |
| $Y = F^{-1}(X)$ | $U(0, 1)$  | $F$             |

### 6.3 指数分布的变换

| 变换            | $X$ 的分布            | $Y$ 的分布      |
| --------------- | --------------------- | --------------- |
| $Y = \lambda X$ | $\text{Exp}(\lambda)$ | $\text{Exp}(1)$ |
| $Y = e^X$       | $\text{Exp}(\lambda)$ | 帕累托分布      |

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
