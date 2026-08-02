---
order: 70
title: 点估计
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 矩估计法与极大似然估计法的原理与计算，两种点估计方法的对比与选择。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/正态总体的抽样分布'
  - 'probability-statistics/抽样分布典型例题'
  - 'probability-statistics/估计量的评选标准'
  - 'probability-statistics/区间估计'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 0. 用样本"尝汤"猜总体的配方

你去一家饭馆喝汤，想知道汤里盐放了多少克（总体参数 $\theta$）。当然不能把整锅汤端走化验，只能**舀一勺尝尝**（抽取样本）。尝完你判断："这锅汤大概放了 3 克盐。"——这就是**点估计**：用一个数值去猜未知参数。

但"猜"也有不同的思路：

- **思路 A（矩估计）**：你尝了几口，凭"咸淡平均水平"推断。平均口感对应盐的期望，把样本平均当作总体平均，反推盐量。
- **思路 B（极大似然估计）**：你回想"这锅汤最像放了 3 克盐做的"——即让"喝到这勺汤"这件事**最有可能发生**的配方，就是最佳猜测。

两种思路各有千秋。本文用**对比驱动**的方式，把矩估计与极大似然估计放在同一张"擂台"上：先讲各自原理，再讲操作步骤，用同一批例题对比结果，最后总结各自的优缺点与适用场景。

## 1. 点估计的基本概念

### 1.1 定义

设总体 $X$ 的分布函数 $F(x; \theta)$ 中含有未知参数 $\theta$（可以是向量），$X_1, X_2, \cdots, X_n$ 为样本。构造统计量 $\hat{\theta} = \hat{\theta}(X_1, X_2, \cdots, X_n)$ 来估计 $\theta$，称 $\hat{\theta}$ 为 $\theta$ 的**点估计量**（或**估计量**）。

把样本观测值代入后得到的数值 $\hat{\theta}(x_1, x_2, \cdots, x_n)$ 称为 **估计值**。

> 区分两个词：**估计量**是样本的（随机）函数，**估计值**是代入具体数据后的数。考试里问"求估计量"要写式子，问"求估计值"要代数字。

### 1.2 点估计要解决的两个问题

1. **如何构造估计量？**（方法问题）——本文的主角：矩估计法、极大似然估计法。
2. **如何评价估计量的好坏？**（准则问题）——下一篇《估计量的评选标准》的主角。

## 2. 矩估计法（思路 A："尝平均水平"）

### 2.1 基本思想

"替换原理"：由大数定律，样本矩依概率收敛于总体矩。既然如此，就用**样本矩去替换总体矩**，列出方程反解未知参数。

### 2.2 操作步骤

设总体 $X$ 有 $k$ 个未知参数 $\theta_1, \theta_2, \cdots, \theta_k$：

1. **算总体矩**：求出总体 $X$ 的前 $k$ 阶原点矩 $\mu_1, \mu_2, \cdots, \mu_k$，写成 $\theta_1, \cdots, \theta_k$ 的函数；
2. **列方程**：令样本矩等于总体矩（$j = 1, 2, \cdots, k$）：

$$A_j = \mu_j(\theta_1, \theta_2, \cdots, \theta_k), \quad A_j = \frac{1}{n}\sum_{i=1}^n X_i^j$$

3. **解方程**：解出 $\hat{\theta}_1, \hat{\theta}_2, \cdots, \hat{\theta}_k$。

**实用技巧**：有时用一阶矩（均值）和二阶中心矩（方差）比用二阶原点矩更方便，因为 $D(X) = E(X^2) - [E(X)]^2$，解方程更简单。

### 2.3 矩估计的两个完整例题

**例题 1**：设 $X \sim U(a, b)$，$a, b$ 未知，求 $a, b$ 的矩估计。

**解**：

先算总体矩：

$$\mu_1 = E(X) = \frac{a+b}{2}, \quad \mu_2 = E(X^2) = D(X) + [E(X)]^2 = \frac{(b-a)^2}{12} + \left(\frac{a+b}{2}\right)^2$$

令样本矩等于总体矩（用方差形式更方便）：

$$\bar{X} = \frac{a+b}{2}, \quad \frac{n-1}{n}S^2 = \frac{(b-a)^2}{12}$$

解方程组。由第一式 $a + b = 2\bar{X}$，由第二式 $b - a = \sqrt{12 \cdot \dfrac{n-1}{n}S^2}$，解得：

$$\hat{a} = \bar{X} - \sqrt{3 \cdot \frac{n-1}{n}S^2}, \quad \hat{b} = \bar{X} + \sqrt{3 \cdot \frac{n-1}{n}S^2}$$

**例题 2**：设 $X \sim B(N, p)$，$N$ 已知，$p$ 未知，求 $p$ 的矩估计。

**解**：$E(X) = Np$。令 $Np = \bar{X}$，解得：

$$\hat{p} = \frac{\bar{X}}{N}$$

（例如抛一枚硬币 $N = 100$ 次，正面出现 $\sum x_i = 55$ 次，则 $\hat{p} = 55/100 = 0.55$。）

## 3. 极大似然估计法（思路 B："猜最像的配方"）

### 3.1 基本思想

"似然"就是"像的程度"。对于已经发生的样本观测值 $x_1, \cdots, x_n$，不同的参数 $\theta$ 会让这组数据"出现的概率（密度）"不同。**选择使该观测值出现概率最大的参数作为估计值**——因为如果 $\theta$ 真是它，看到这组数据的概率才最高，"最合理"。

### 3.2 似然函数

设总体 $X$ 的密度函数（或分布律）为 $f(x; \theta)$，$\theta \in \Theta$，则样本的**似然函数**为（由独立性，联合密度等于乘积）：

$$L(\theta) = L(x_1, x_2, \cdots, x_n; \theta) = \prod_{i=1}^n f(x_i; \theta)$$

### 3.3 极大似然估计（MLE）

若存在 $\hat{\theta} = \hat{\theta}(x_1, \cdots, x_n)$ 使得

$$L(\hat{\theta}) = \max_{\theta \in \Theta} L(\theta)$$

则称 $\hat{\theta}$ 为 $\theta$ 的**极大似然估计**（MLE）。注意：这里把 $x_i$ 视为已观测的常数，$\theta$ 视为变量——视角与"似然函数当密度函数"刚好相反。

### 3.4 对数似然函数：化乘积为求和

$\ln L$ 是 $L$ 的单调递增函数，两者在同一点取最大值。连乘求导很痛苦，连加求导很舒服，所以通常对**对数似然函数**求极值：

$$\ln L(\theta) = \sum_{i=1}^n \ln f(x_i; \theta)$$

### 3.5 求 MLE 的标准流程

1. 写出似然函数 $L(\theta) = \prod f(x_i; \theta)$；
2. 取对数得 $\ln L(\theta)$；
3. 对 $\theta$ 求导，令导数为零，得**似然方程**；

$$\frac{\partial \ln L}{\partial \theta} = 0$$

4. 解方程得 $\hat{\theta}$。若似然方程无解或边界取极值（如均匀分布），直接看 $L$ 的单调性确定最大值点。

### 3.6 极大似然估计的两个完整例题

**例题 3**：设 $X \sim N(\mu, \sigma^2)$，$\mu, \sigma^2$ 均未知，求 $\mu$ 和 $\sigma^2$ 的 MLE。

**解**：

似然函数：

$$L(\mu, \sigma^2) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x_i - \mu)^2}{2\sigma^2}} = (2\pi)^{-n/2} (\sigma^2)^{-n/2} e^{-\frac{1}{2\sigma^2}\sum (x_i - \mu)^2}$$

对数似然：

$$\ln L = -\frac{n}{2}\ln(2\pi) - \frac{n}{2}\ln\sigma^2 - \frac{1}{2\sigma^2}\sum (x_i - \mu)^2$$

对 $\mu$ 求偏导并令其为零：

$$\frac{\partial \ln L}{\partial \mu} = \frac{1}{\sigma^2}\sum (x_i - \mu) = 0 \implies \hat{\mu} = \bar{x}$$

对 $\sigma^2$ 求偏导并令其为零（把 $\mu$ 换成 $\bar{x}$ 后）：

$$\frac{\partial \ln L}{\partial \sigma^2} = -\frac{n}{2\sigma^2} + \frac{1}{2\sigma^4}\sum (x_i - \bar{x})^2 = 0 \implies \hat{\sigma}^2 = \frac{1}{n}\sum (x_i - \bar{x})^2 = \frac{n-1}{n}S^2$$

**对比点**：$\hat{\sigma}^2 = \dfrac{n-1}{n}S^2$ **不是**无偏估计（下一篇会讲）。这说明"MLE 的估计不一定无偏"，小样本时需修正。

**例题 4**：设 $X \sim U(0, \theta)$，$\theta$ 未知，求 $\theta$ 的 MLE。

**解**：

$$L(\theta) = \begin{cases} \dfrac{1}{\theta^n}, & 0 < x_i < \theta, \; i = 1, \cdots, n \\ 0, & \text{其他} \end{cases}$$

注意：$L$ 的定义域约束了 $\theta$ 必须 $\geq x_{(n)} = \max(x_1, \cdots, x_n)$。在 $\theta \geq x_{(n)}$ 的范围内，$L(\theta) = \theta^{-n}$ 关于 $\theta$ **严格递减**，所以 $\theta$ 越小 $L$ 越大，但最小只能到 $x_{(n)}$：

$$\hat{\theta} = x_{(n)} = \max(x_1, \cdots, x_n)$$

**对比点**：这个例子"求导不灵、单调性灵"——MLE 有时要用定义直接判断，不能用套路。

## 4. 两种方法的对比擂台

| 对比维度 | 矩估计（MM） | 极大似然估计（MLE） |
| --- | --- | --- |
| 核心思想 | 样本矩替换总体矩，解方程 | 让样本观测值出现概率最大 |
| 计算难度 | 简单，只需算矩、解方程组 | 较复杂，需写似然函数、求导 |
| 理论基础 | 大数定律（替换原理） | 概率最大原则 |
| 小样本表现 | 一般，方差往往较大 | 一般更优，但不保证无偏 |
| 大样本性质 | 相合，但渐近效率可能不足 | 相合、渐近正态、渐近有效 |
| 不变性 | 无（$g(\hat{\theta}_{MM})$ 一般不是 $g(\theta)$ 的矩估计） | 有（$g(\hat{\theta}_{MLE})$ 是 $g(\theta)$ 的 MLE） |
| 典型缺陷 | 可能不唯一；对分布形状不敏感 | 需知道分布形式；有时无解析解 |
| 适用场景 | 快速估算、分布形式模糊时 | 分布已知、追求估计精度时 |

### 4.1 不变性（MLE 的独门绝技）

**定理（MLE 的不变性）**：若 $\hat{\theta}$ 是 $\theta$ 的 MLE，$g$ 是连续函数，则 $g(\hat{\theta})$ 是 $g(\theta)$ 的 MLE。

例如 $\hat{\sigma} = \sqrt{\hat{\sigma}^2}$ 是标准差 $\sigma$ 的 MLE——求完 $\sigma^2$ 的 MLE 直接开方即可，无需重新推导。

### 4.2 MLE 的渐近性质

在一定正则条件下：

- **相合性**：$\hat{\theta}_n \xrightarrow{P} \theta$；
- **渐近正态性**：$\hat{\theta}_n$ 近似服从 $N\left(\theta, \dfrac{1}{nI(\theta)}\right)$，其中 $I(\theta)$ 为 Fisher 信息量（见下一篇）。

这两条性质使 MLE 在大样本下几乎是最优的，也是它在现代统计与机器学习中地位显赫的原因（如逻辑回归、神经网络的极大似然训练）。

## 5. 常见错误与对策

| 错误类型 | 错误示例 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 混淆估计量与估计值 | 求出的 $\hat{\theta}$ 写成数字而非式子 | 没区分随机函数与观测值 | 题目问"估计量"写含 $X_i$ 的式子，问"估计值"才代入数据 |
| 矩方程个数不够 | 两个参数只列一阶矩方程 | 未知参数个数 = 方程个数 | $k$ 个参数需列 $k$ 个方程，常用前 $k$ 阶原点矩 |
| 似然函数忽略定义域 | $U(0, \theta)$ 中 $\theta < x_{(n)}$ 也代入 | 忘了密度非零区域依赖 $\theta$ | 先写出密度非零的条件，MLE 候选必须在可行域内 |
| 盲目求导 | 均匀分布用似然方程求 $\theta$ | 极大点在边界，不在驻点 | 先看 $L(\theta)$ 单调性：$U(0,\theta)$ 中 $L$ 递减，最大点在 $\theta = x_{(n)}$ |
| 忘记取对数 | 对乘积形式直接求导 | 连乘求导繁琐易错 | 取对数化为求和再求导；对数与 $L$ 同点取极值 |
| 混淆 $\hat{\sigma}^2$ 与 $S^2$ | 把 MLE 的 $\hat{\sigma}^2$ 当无偏 | 不知 $\hat{\sigma}^2 = \frac{n-1}{n}S^2$ 有偏 | 记住：MLE 给 $\frac{1}{n}\sum(X_i-\bar X)^2$，无偏修正是 $S^2$；方差估计的"无偏版"是 $S^2$ |

## 6. 实战练习

**练习 1（矩估计入门）**：设总体 $X \sim P(\lambda)$（泊松分布），求 $\lambda$ 的矩估计。

**提示**：$E(X) = \lambda$，令 $E(X) = \bar{X}$。

**参考答案要点**：$\hat{\lambda} = \bar{X}$。

**练习 2（MLE 入门）**：设总体 $X \sim P(\lambda)$，求 $\lambda$ 的 MLE。

**提示**：$P(X = k) = \dfrac{\lambda^k e^{-\lambda}}{k!}$，写出似然函数后取对数。

**参考答案要点**：$L(\lambda) = \dfrac{\lambda^{\sum x_i} e^{-n\lambda}}{\prod x_i!}$，$\ln L = \sum x_i \ln\lambda - n\lambda - \sum \ln(x_i!)$，$\dfrac{d\ln L}{d\lambda} = \dfrac{\sum x_i}{\lambda} - n = 0$，得 $\hat{\lambda} = \bar{x}$。两种方法在此结果一致。

**练习 3（指数分布对比）**：设 $X$ 的密度为 $f(x) = \dfrac{1}{\theta}e^{-x/\theta}$（$x > 0$，$\theta > 0$），分别求 $\theta$ 的矩估计与 MLE。

**提示**：$E(X) = \theta$；似然函数 $L = \theta^{-n} e^{-\sum x_i/\theta}$。

**参考答案要点**：矩估计 $\hat{\theta} = \bar{X}$；MLE：$\ln L = -n\ln\theta - \dfrac{\sum x_i}{\theta}$，$\dfrac{d\ln L}{d\theta} = -\dfrac{n}{\theta} + \dfrac{\sum x_i}{\theta^2} = 0$，得 $\hat{\theta} = \bar{x}$。两者一致。

**练习 4（幂律分布 MLE）**：设 $X$ 的密度为 $f(x) = \theta x^{\theta-1}$（$0 < x < 1$，$\theta > 0$），求 $\theta$ 的 MLE。

**提示**：$\ln L = n\ln\theta + (\theta - 1)\sum \ln x_i$。

**参考答案要点**：$\dfrac{d\ln L}{d\theta} = \dfrac{n}{\theta} + \sum\ln x_i = 0$，$\hat{\theta} = -\dfrac{n}{\sum\ln x_i}$。

**练习 5（不变性应用）**：已知 $\hat{\sigma}^2 = \dfrac{1}{n}\sum (X_i - \bar{X})^2$ 是正态总体 $\sigma^2$ 的 MLE，求 $\sigma$ 的 MLE，并判断它是否为 $\sigma$ 的无偏估计（提示：用 $E(\chi^2(1))$ 相关性质或 Jensen 不等式直觉判断）。

**提示**：由不变性 $\hat{\sigma} = \sqrt{\hat{\sigma}^2}$；无偏性可借助 $\chi^2$ 分布计算 $E(\sqrt{\chi^2(n)})$。

**参考答案要点**：$\hat{\sigma} = \sqrt{\dfrac{1}{n}\sum (X_i - \bar{X})^2}$；它不是 $\sigma$ 的无偏估计（平方根运算会使期望略小于真值，属于"凸函数下的 Jensen 偏差"）。这也是"MLE 在小样本未必无偏"的又一个例子。

## 7. 一句话记忆

**点估计就是"尝汤猜配方"：矩估计靠"平均口感"反推（样本矩替换总体矩、解方程），极大似然估计靠"最像"反推（让观测数据出现概率最大的 $\theta$），两者各有所长，分布已知求精度选 MLE。**

## 参考文献

- 盛骤、谢式千、潘承毅，《概率论与数理统计》（浙大版第四版），高等教育出版社：第七章第一节"点估计"（矩估计法与极大似然估计法）。
- 浙江大学概率论与数理统计 MOOC 第 44-46 讲（点估计、矩估计、极大似然估计）：https://www.icourse163.org/course/ZJU-1001743002
- Khan Academy 统计与概率：https://zh.khanacademy.org/math/statistics-probability
- Seeing Theory（交互式可视化统计教材）：https://seeing-theory.brown.edu/
- OpenIntro Statistics：https://www.openintro.org/book/os/

## 延伸阅读

- 估计量的好坏如何评判（无偏性、有效性、相合性），见《估计量的评选标准》。
- 点估计只给一个数，如何给"一个范围"？见《区间估计》。
- 正态总体均值、方差的置信区间具体公式，见《正态总体参数的区间估计》。
- 点估计与区间估计的混合应用案例，见《参数估计典型例题》。
