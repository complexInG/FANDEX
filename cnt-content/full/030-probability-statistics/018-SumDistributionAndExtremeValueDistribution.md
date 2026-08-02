---
order: 160
title: 和的分布与极值分布
module: 'probability-statistics'
category: 数学
difficulty: advanced
description: 随机变量和的分布（离散卷积、连续卷积公式）、差与商的分布、最大值与最小值分布、系统可靠性应用。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/016-ConditionalDistribution'
  - 'probability-statistics/017-RandomVariableIndependence'
  - 'probability-statistics/020-MathematicalExpectation'
prerequisites:
  - 'probability-statistics/001-SampleSpaceAndEvent'
---


## 0. 从一个生活场景说起：合股开店，利润相加、取最值

你和朋友合股开一家奶茶店，你的那份月利润是 $X$ 万元，朋友的月利润是 $Y$ 万元。店铺总利润是 $X + Y$——你想知道"总利润怎么分布"；如果店里有 5 个独立经营的窗口，你关心"最赚钱的窗口赚了多少（$\max$）"或者"最差窗口赔了多少（$\min$）"。

这就是本篇的主题：**已知 $X$、$Y$（或一组变量）的分布，计算它们"运算之后"的新变量的分布**。我们把这类问题统称为随机变量函数的分布，核心武器是"卷积"（加法）与"次序统计"（取最值）。

本文采用"**运算驱动**"的叙事结构：按照运算类型逐一攻克——加法（卷积）→ 减法 → 除法 → 取最大/最小，每个运算配定义、公式、例题，最后落地到系统可靠性的实际应用。

## 1. 和的分布：离散型卷积

### 1.1 思路

设 $X$、$Y$ 为独立离散型随机变量，$Z = X + Y$。事件 $\{Z = z\}$ 可以拆成"互不相交"的若干子事件：

$$\{Z = z\} = \bigcup_{i} \{X = x_i,\ Y = z - x_i\}$$

由独立性，各子事件概率为 $P(X = x_i) P(Y = z - x_i)$，再相加：

$$P(Z = z_k) = \sum_{x_i + y_j = z_k} P(X = x_i) P(Y = y_j) = \sum_i P(X = x_i) P(Y = z_k - x_i)$$

这就是**离散卷积**。可以形象地理解为：把 $X$ 的分布律与 $Y$ 的分布律"错位相乘再求和"。

## 2. 和的分布：连续型卷积公式

### 2.1 卷积公式

设 $X$、$Y$ 为独立连续型随机变量，密度分别为 $f_X(x)$、$f_Y(y)$，则 $Z = X + Y$ 的密度为

$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(z - x) \, dx = \int_{-\infty}^{+\infty} f_X(z - y) f_Y(y) \, dy$$

记作 $f_Z = f_X * f_Y$。

### 2.2 公式推导（分布函数法）

$$F_Z(z) = P(X + Y \leq z) = \iint_{x + y \leq z} f_X(x) f_Y(y) \, dx \, dy$$

先对 $y$ 积分，再换元 $u = x + y$（此时 $y = u - x$，$dy = du$）：

$$F_Z(z) = \int_{-\infty}^{+\infty} f_X(x) \left[\int_{-\infty}^{z-x} f_Y(y) \, dy\right] dx = \int_{-\infty}^{+\infty} f_X(x) F_Y(z - x) \, dx$$

对 $z$ 求导（对积分求导，把导数放入内层）：

$$f_Z(z) = \frac{d}{dz} F_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(z - x) \, dx$$

## 3. 和的分布：重要结论（可加性）

下面几条"可加性"结论必须熟记，它们能省去大量卷积计算：

1. **正态可加性**：$X \sim N(\mu_1, \sigma_1^2)$、$Y \sim N(\mu_2, \sigma_2^2)$ 独立 $\Rightarrow$ $X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$；
   推广：$X_1, \cdots, X_n$ 独立，$X_i \sim N(\mu_i, \sigma_i^2)$，则 $\displaystyle\sum_{i=1}^n a_i X_i \sim N\left(\sum a_i \mu_i, \sum a_i^2 \sigma_i^2\right)$；
2. **泊松可加性**：$X \sim P(\lambda_1)$、$Y \sim P(\lambda_2)$ 独立 $\Rightarrow$ $X + Y \sim P(\lambda_1 + \lambda_2)$；
3. **二项可加性**：$X \sim B(n_1, p)$、$Y \sim B(n_2, p)$ 独立（$p$ 相同）$\Rightarrow$ $X + Y \sim B(n_1 + n_2, p)$。

## 4. 差的分布与商的分布

### 4.1 差的分布

若 $X$、$Y$ 独立，$Z = X - Y$，则

$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(x - z) \, dx = \int_{-\infty}^{+\infty} f_X(y + z) f_Y(y) \, dy$$

本质上与卷积同源，只是把 $Y$ 换成 $-Y$。

### 4.2 商的分布

若 $X$、$Y$ 为独立连续型随机变量，$Z = \dfrac{X}{Y}$，则

$$f_Z(z) = \int_{-\infty}^{+\infty} |y| \, f_X(zy) f_Y(y) \, dy$$

**推导思路**：分布函数法。

$$F_Z(z) = P\left(\frac{X}{Y} \leq z\right) = \iint_{x/y \leq z} f_X(x) f_Y(y) \, dx \, dy$$

注意 $y > 0$ 与 $y < 0$ 时不等式方向相反，要分两半积分（$x \le zy$ 与 $x \ge zy$）：

$$= \int_0^{+\infty} F_X(zy) f_Y(y) \, dy + \int_{-\infty}^0 [1 - F_X(zy)] f_Y(y) \, dy$$

对 $z$ 求导即得商的密度公式。|y| 的出现正是分段带来的雅可比因子。

> 经典结论：$X \sim N(0,1)$、$Y \sim N(0,1)$ 独立时，$Z = X/Y$ 服从柯西分布（密度为 $\dfrac{1}{\pi(1+z^2)}$，期望不存在）。

## 5. 最大值分布：$M = \max(X_1, \cdots, X_n)$

### 5.1 分布函数

"最大值不超过 $x$"等价于"每个变量都不超过 $x$"，利用独立性：

$$F_M(x) = P(M \leq x) = P(X_1 \leq x,\ \cdots,\ X_n \leq x) = \prod_{i=1}^n F_i(x)$$

独立同分布时（共同分布函数 $F(x)$）：

$$F_M(x) = [F(x)]^n$$

### 5.2 密度函数

独立同分布、密度为 $f(x)$ 时，对 $F_M$ 求导：

$$f_M(x) = n\,[F(x)]^{n-1} f(x)$$

## 6. 最小值分布：$N = \min(X_1, \cdots, X_n)$

### 6.1 分布函数

"最小值大于 $x$"等价于"每个变量都大于 $x$"，故

$$F_N(x) = 1 - P(N > x) = 1 - \prod_{i=1}^n P(X_i > x) = 1 - \prod_{i=1}^n [1 - F_i(x)]$$

独立同分布时：

$$F_N(x) = 1 - [1 - F(x)]^n$$

### 6.2 密度函数

$$f_N(x) = n\,[1 - F(x)]^{n-1} f(x)$$

## 7. 应用：系统可靠性

把元件寿命建模为独立随机变量：

- **串联系统**：任一元件失效则系统失效，系统寿命 $T = \min(T_1, \cdots, T_n)$；
- **并联系统**：全部元件失效系统才失效，系统寿命 $T = \max(T_1, \cdots, T_n)$。

## 8. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 卷积积分上下限直接写 $-\infty$ 到 $+\infty$ 不讨论分段 | 支撑集遗漏 | 未把 $f_X(x) f_Y(z-x)$ 的非零区域投影到 $x$ 轴 | 先解不等式组（如 $0<x<1$ 与 $0<z-x<1$），按 $z$ 分段定限 |
| 忘记卷积要求 $X$ 与 $Y$ 独立 | 前提遗漏 | 卷积公式本质是 $f(x,y) = f_X(x)f_Y(y)$ 的叠加 | 用卷积前先确认独立性；不独立时改用 $\int f(x, z-x) dx$ 形式 |
| 最大值分布写成 $F_M(x) = 1 - [F(x)]^n$ | 公式记反 | 把最大与最小公式混淆 | 记忆法：$M \le x$ 是"交"（全都不超过），$N > x$ 也是"交"（全都超过）；最大值用 $[F(x)]^n$，最小值用 $1-[1-F(x)]^n$ |
| 商的分布忘了乘 $|y|$ | 因子遗漏 | 变量替换的雅可比因子被跳过 | 记住 $f_Z(z)=\int|y|f_X(zy)f_Y(y)dy$，$|y|$ 不能丢 |
| 两个独立指数分布之和直接用 $f_Z = \lambda^2 z e^{-\lambda z}$ | 公式误用 | 只对 $\lambda_1=\lambda_2$ 成立 | 参数不同时用卷积逐项算；参数相同才属于 $\Gamma(2, \lambda)$ |
| 混淆"两个变量之和"与"$n$ 个变量均值"的分布 | 概念混淆 | 忽略了正态可加性的参数规则 | 和：$N(n\mu, n\sigma^2)$；均值 $\bar{X}$：$N(\mu, \sigma^2/n)$ |

## 10. 一句话记忆

"加"用卷积：$f_{X+Y} = f_X * f_Y$（离散求和、连续积分，独立才可分离）；"取最值"用分布函数：最大值 $F_M = \prod F_i$、最小值 $F_N = 1 - \prod(1-F_i)$——运算驱动，一题一型，先定支撑、再套公式。

## 延伸阅读
概率统计基础，见 030-probability-statistics 模块文档。
数据分析应用，见 051-data-analysis 模块。
机器学习概率视角，见 042-machine-learning 模块（AI 模块仅供了解）。
