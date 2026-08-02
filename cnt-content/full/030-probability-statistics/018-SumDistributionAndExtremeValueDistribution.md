---
order: 34
title: 和的分布与极值分布
module: 'probability-statistics'
category: 'comp-sci'
difficulty: advanced
description: 随机变量和的分布（离散卷积、连续卷积公式）、差与商的分布、最大值与最小值分布、系统可靠性应用。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/条件分布'
  - 'probability-statistics/随机变量的独立性'
  - 'probability-statistics/多维随机变量典型例题'
  - 'probability-statistics/数学期望'
prerequisites:
  - 'probability-statistics/样本空间与事件'
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

### 1.2 例题 1（离散卷积）

设 $X$ 与 $Y$ 独立，$X \sim B(1, p)$，$Y \sim B(1, p)$，求 $Z = X + Y$ 的分布律。

**解**：$X, Y$ 各取 $0$ 或 $1$，故 $Z$ 取 $0, 1, 2$。

$$P(Z = 0) = P(X=0)P(Y=0) = (1-p)^2$$

$$P(Z = 1) = P(X=0)P(Y=1) + P(X=1)P(Y=0) = 2p(1-p)$$

$$P(Z = 2) = P(X=1)P(Y=1) = p^2$$

验证：$(1-p)^2 + 2p(1-p) + p^2 = 1$。这正是 $B(2, p)$ 的分布律——两个独立伯努利变量之和服从二项分布，这是二项分布"可加性"的雏形。

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

### 2.3 例题 2（两个均匀分布之和，分段积分）

设 $X \sim U(0,1)$，$Y \sim U(0,1)$，$X$ 与 $Y$ 独立，求 $Z = X + Y$ 的密度。

**解**：被积函数非零需同时满足 $0 < x < 1$ 与 $0 < z - x < 1$，即 $0 < x < 1$ 且 $z - 1 < x < z$。按 $z$ 分段：

当 $0 < z < 1$：$x$ 从 $0$ 到 $z$，$f_Z(z) = \displaystyle\int_0^z 1 \cdot 1 \, dx = z$；

当 $1 \le z < 2$：$x$ 从 $z-1$ 到 $1$，$f_Z(z) = \displaystyle\int_{z-1}^1 dx = 2 - z$。

$$f_Z(z) = \begin{cases} z, & 0 < z < 1 \\ 2 - z, & 1 \le z < 2 \\ 0, & \text{其他} \end{cases}$$

这是著名的"三角分布"，两个均匀分布之和的密度呈等腰三角形，它是中心极限定理最直观的入门案例（见《中心极限定理》）。

## 3. 和的分布：重要结论（可加性）

下面几条"可加性"结论必须熟记，它们能省去大量卷积计算：

1. **正态可加性**：$X \sim N(\mu_1, \sigma_1^2)$、$Y \sim N(\mu_2, \sigma_2^2)$ 独立 $\Rightarrow$ $X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$；
   推广：$X_1, \cdots, X_n$ 独立，$X_i \sim N(\mu_i, \sigma_i^2)$，则 $\displaystyle\sum_{i=1}^n a_i X_i \sim N\left(\sum a_i \mu_i, \sum a_i^2 \sigma_i^2\right)$；
2. **泊松可加性**：$X \sim P(\lambda_1)$、$Y \sim P(\lambda_2)$ 独立 $\Rightarrow$ $X + Y \sim P(\lambda_1 + \lambda_2)$；
3. **二项可加性**：$X \sim B(n_1, p)$、$Y \sim B(n_2, p)$ 独立（$p$ 相同）$\Rightarrow$ $X + Y \sim B(n_1 + n_2, p)$。

### 例题 3（泊松可加性的证明）

设 $X \sim P(\lambda_1)$，$Y \sim P(\lambda_2)$ 独立，证明 $Z = X + Y \sim P(\lambda_1 + \lambda_2)$。

**证明**：$Z$ 取非负整数 $k$，用离散卷积：

$$P(Z = k) = \sum_{i=0}^{k} \frac{\lambda_1^i e^{-\lambda_1}}{i!} \cdot \frac{\lambda_2^{k-i} e^{-\lambda_2}}{(k-i)!} = \frac{e^{-(\lambda_1+\lambda_2)}}{k!} \sum_{i=0}^k \binom{k}{i} \lambda_1^i \lambda_2^{k-i}$$

由二项式定理，求和等于 $(\lambda_1 + \lambda_2)^k$，故

$$P(Z = k) = \frac{(\lambda_1 + \lambda_2)^k e^{-(\lambda_1+\lambda_2)}}{k!}, \qquad k = 0, 1, 2, \cdots$$

即 $Z \sim P(\lambda_1 + \lambda_2)$。实际意义：两个独立客服座席的来电数之和仍是泊松分布，参数相加。

### 例题 4（指数分布之和）

设 $X \sim \text{Exp}(\lambda_1)$，$Y \sim \text{Exp}(\lambda_2)$ 独立（$\lambda_1 \neq \lambda_2$），求 $Z = X + Y$ 的密度。

**解**：$z > 0$ 时 $x$ 从 $0$ 到 $z$：

$$f_Z(z) = \int_0^z \lambda_1 e^{-\lambda_1 x} \cdot \lambda_2 e^{-\lambda_2(z-x)} \, dx = \lambda_1 \lambda_2 e^{-\lambda_2 z} \int_0^z e^{(\lambda_2 - \lambda_1)x} \, dx$$

$$= \frac{\lambda_1 \lambda_2}{\lambda_2 - \lambda_1} \left(e^{-\lambda_1 z} - e^{-\lambda_2 z}\right), \quad z > 0$$

当 $\lambda_1 = \lambda_2 = \lambda$ 时，$Z \sim \Gamma(2, \lambda)$，即两个独立同参数指数分布之和服从伽马分布（爱朗分布）。

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

### 5.3 例题 5（均匀分布的最大值）

设 $X_1, X_2, \cdots, X_n$ 独立同分布，$X_i \sim U(0, 1)$，求 $M = \max(X_1, \cdots, X_n)$ 的分布函数与密度。

**解**：$F(x) = x$（$0 < x < 1$），故

$$F_M(x) = x^n, \qquad f_M(x) = nx^{n-1}, \quad 0 < x < 1$$

直观意义：$n$ 个随机点中最大的那个倾向于靠近 1，密度在 $x = 1$ 附近最大（$n > 1$ 时 $nx^{n-1}$ 单调递增）。

## 6. 最小值分布：$N = \min(X_1, \cdots, X_n)$

### 6.1 分布函数

"最小值大于 $x$"等价于"每个变量都大于 $x$"，故

$$F_N(x) = 1 - P(N > x) = 1 - \prod_{i=1}^n P(X_i > x) = 1 - \prod_{i=1}^n [1 - F_i(x)]$$

独立同分布时：

$$F_N(x) = 1 - [1 - F(x)]^n$$

### 6.2 密度函数

$$f_N(x) = n\,[1 - F(x)]^{n-1} f(x)$$

### 6.3 例题 6（指数分布的最小值）

设 $X_1, \cdots, X_n$ 独立同分布，$X_i \sim \text{Exp}(\lambda)$，求 $N = \min(X_1, \cdots, X_n)$ 的分布。

**解**：$F(x) = 1 - e^{-\lambda x}$（$x > 0$），故

$$F_N(x) = 1 - \left[e^{-\lambda x}\right]^n = 1 - e^{-n\lambda x}, \quad x > 0$$

即 $N \sim \text{Exp}(n\lambda)$！**指数分布对取最小值封闭**（参数变为 $n\lambda$，平均寿命缩短为 $1/(n\lambda)$）。这解释了"多个独立电子元件串联时系统寿命按元件个数成倍缩短"的现象。

## 7. 应用：系统可靠性

把元件寿命建模为独立随机变量：

- **串联系统**：任一元件失效则系统失效，系统寿命 $T = \min(T_1, \cdots, T_n)$；
- **并联系统**：全部元件失效系统才失效，系统寿命 $T = \max(T_1, \cdots, T_n)$。

### 例题 7（并联系统可靠性）

系统由 5 个独立工作的元件并联组成，每个元件寿命 $T_i \sim \text{Exp}(0.1)$（单位：小时），求系统寿命超过 20 小时的概率。

**解**：并联系统寿命 $T = \max(T_1, \cdots, T_5)$。

$$P(T > 20) = 1 - P(T \le 20) = 1 - \left[P(T_1 \le 20)\right]^5$$

$$P(T_1 \le 20) = 1 - e^{-0.1 \times 20} = 1 - e^{-2} \approx 0.8647$$

$$P(T > 20) = 1 - 0.8647^5 \approx 1 - 0.4833 = 0.5167$$

单个元件寿命超过 20 小时的概率仅约 13.5%，而 5 元件并联后系统超过 20 小时的概率提高到约 51.7%——这就是冗余设计（备份）的价值。

## 8. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 卷积积分上下限直接写 $-\infty$ 到 $+\infty$ 不讨论分段 | 支撑集遗漏 | 未把 $f_X(x) f_Y(z-x)$ 的非零区域投影到 $x$ 轴 | 先解不等式组（如 $0<x<1$ 与 $0<z-x<1$），按 $z$ 分段定限 |
| 忘记卷积要求 $X$ 与 $Y$ 独立 | 前提遗漏 | 卷积公式本质是 $f(x,y) = f_X(x)f_Y(y)$ 的叠加 | 用卷积前先确认独立性；不独立时改用 $\int f(x, z-x) dx$ 形式 |
| 最大值分布写成 $F_M(x) = 1 - [F(x)]^n$ | 公式记反 | 把最大与最小公式混淆 | 记忆法：$M \le x$ 是"交"（全都不超过），$N > x$ 也是"交"（全都超过）；最大值用 $[F(x)]^n$，最小值用 $1-[1-F(x)]^n$ |
| 商的分布忘了乘 $|y|$ | 因子遗漏 | 变量替换的雅可比因子被跳过 | 记住 $f_Z(z)=\int|y|f_X(zy)f_Y(y)dy$，$|y|$ 不能丢 |
| 两个独立指数分布之和直接用 $f_Z = \lambda^2 z e^{-\lambda z}$ | 公式误用 | 只对 $\lambda_1=\lambda_2$ 成立 | 参数不同时用卷积逐项算；参数相同才属于 $\Gamma(2, \lambda)$ |
| 混淆"两个变量之和"与"$n$ 个变量均值"的分布 | 概念混淆 | 忽略了正态可加性的参数规则 | 和：$N(n\mu, n\sigma^2)$；均值 $\bar{X}$：$N(\mu, \sigma^2/n)$ |

## 9. 实战练习

### 练习 1（离散卷积）

设 $X \sim P(3)$，$Y \sim P(2)$，$X$ 与 $Y$ 独立，求 $P(X + Y = 3)$。

**提示**：利用泊松可加性 $Z = X + Y \sim P(5)$。

**参考答案要点**：$P(Z=3) = \dfrac{5^3 e^{-5}}{3!} \approx 0.1404$。

### 练习 2（连续卷积，分段）

设 $X \sim U(0, 2)$，$Y \sim U(0, 2)$ 独立，求 $Z = X + Y$ 的密度。

**提示**：按 $0<z<2$ 与 $2 \le z < 4$ 分段。

**参考答案要点**：$0<z<2$ 时 $f_Z(z)=\dfrac{z}{4}$；$2\le z<4$ 时 $f_Z(z)=\dfrac{4-z}{4}$；其他为 0。

### 练习 3（最大值分布）

设 $X_1, X_2, X_3$ 独立同分布，$X_i \sim U(0, \theta)$，求 $M = \max(X_1, X_2, X_3)$ 的密度函数，并求 $P(M \ge 0.8\theta)$。

**提示**：先写 $F_M(x) = \left(\dfrac{x}{\theta}\right)^3$。

**参考答案要点**：$f_M(x) = \dfrac{3x^2}{\theta^3}$（$0<x<\theta$）；$P(M \ge 0.8\theta) = 1 - F_M(0.8\theta) = 1 - 0.512 = 0.488$。

### 练习 4（最小值分布）

设系统由 4 个独立元件串联组成，每个元件寿命 $T_i \sim \text{Exp}(0.05)$，求系统平均寿命。

**提示**：串联系统寿命为最小值，指数分布对最小值封闭。

**参考答案要点**：$\min(T_1,\cdots,T_4) \sim \text{Exp}(0.2)$，平均寿命 $E = \dfrac{1}{0.2} = 5$（小时）；单个元件平均寿命为 20 小时，串联后缩短为 5 小时。

### 练习 5（综合）

设 $X$、$Y$ 独立，$X \sim N(1, 4)$，$Y \sim N(2, 9)$，求 $Z = 2X - 3Y + 1$ 的分布。

**提示**：用正态线性组合结论。

**参考答案要点**：$Z \sim N(2\times1 - 3\times2 + 1,\ 4\times4 + 9\times9) = N(-3, 97)$。

## 10. 一句话记忆

"加"用卷积：$f_{X+Y} = f_X * f_Y$（离散求和、连续积分，独立才可分离）；"取最值"用分布函数：最大值 $F_M = \prod F_i$、最小值 $F_N = 1 - \prod(1-F_i)$——运算驱动，一题一型，先定支撑、再套公式。

## 参考文献

- 盛骤, 谢式千, 潘承毅. 概率论与数理统计（第六版）[M]. 高等教育出版社, 2026. 第三章"多维随机变量及其分布"§5 两个随机变量的函数的分布. https://www.hep.com.cn/book/show/3b2dd87a-7531-4610-97e6-071eb302d813
- 和的分布与差的分布（卷积公式）. https://kb.kmath.cn/kbase/detail.aspx?id=2554
- 概率论复习笔记——卷积公式（含 $Z=X+Y$、$Z=X/Y$、$M=\max\{X,Y\}$ 例题）. https://blog.csdn.net/jyfan0806/article/details/84729422

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
