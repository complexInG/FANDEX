---
order: 63
title: 正态总体的抽样分布
module: 'probability-statistics'
category: 'comp-sci'
difficulty: advanced
description: 单正态总体和双正态总体的抽样分布定理，统计推断的理论基础，逐条定理给出推导与直观理解。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/统计量'
  - 'probability-statistics/三大分布'
  - 'probability-statistics/抽样分布典型例题'
  - 'probability-statistics/点估计'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 0. 全班成绩分布抽样的启示

假设你是班主任，全班 50 人的数学成绩服从某个分布（总体），你随机抽取 10 名同学（样本）。你关心两件事：

1. **这 10 人的平均分**（样本均值 $\bar{X}$）和全班真实平均分（$\mu$）差多少？
2. **这 10 人的分数分散程度**（样本方差 $S^2$）能代表全班分散程度（$\sigma^2$）吗？

更关键的问题是：如果你反复抽 100 次，每次得到一个新的 $\bar{X}$，这 100 个 $\bar{X}$ 会呈现什么规律？这个规律——**统计量的分布**——就叫**抽样分布**。

本文采用**定理驱动**的写法：以四条核心定理为主线，每条定理先讲直观含义，再给出数学结论，最后推导证明。这是统计推断（估计与检验）的"发动机"，值得逐字吃透。

## 1. 单正态总体的抽样分布

### 1.1 基本设定

设 $X_1, X_2, \cdots, X_n$ 为来自正态总体 $N(\mu, \sigma^2)$ 的简单随机样本，$\bar{X}$ 为样本均值，$S^2$ 为样本方差。

**定理一（样本均值的分布）**：样本均值仍服从正态分布，且

$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

标准化后得到标准正态：

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$

**证明思路**（回顾概念）：

$$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$$

是 $X_1, \cdots, X_n$ 的线性组合。正态分布的线性组合仍服从正态分布（正态分布的可加性），因此只需算期望和方差：

$$E(\bar{X}) = \frac{1}{n}\sum_{i=1}^n E(X_i) = \mu$$

$$D(\bar{X}) = \frac{1}{n^2}\sum_{i=1}^n D(X_i) = \frac{\sigma^2}{n}$$

（独立性保证协方差项为零。）均值不变、方差缩小 $n$ 倍：**样本量越大，样本均值越稳定**。这就是为什么"抽样调查"能靠少量样本推测全体的底气所在。

**直观理解**：全班平均分的"抽样分布"比单个学生成绩的分布更集中，$n = 10$ 时标准差缩为原来的 $1/\sqrt{10} \approx 0.316$ 倍。

**定理二（样本方差的分布）**：

$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$$

**证明思路**（浙大概率论讲义的标准做法）：作正交变换，把 $\sum_{i=1}^n (X_i - \bar{X})^2$ 化为 $n-1$ 个独立标准正态平方和。直观版本：

$$\sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2$$

看似是 $n$ 个"标准化离差"的平方和，但 $\sum (X_i - \bar{X}) = 0$ 给出一个线性约束，独立成分只有 $n-1$ 个，所以自由度是 $n-1$。这正是"除以 $n-1$"在分布层面的体现。

**定理三（均值与方差独立）**：

$$\bar{X} \text{ 与 } S^2 \text{ 相互独立}$$

这是正态总体特有的重要性质，非正态总体一般不成立。直观上：$\bar{X}$ 描述"位置"，$S^2$ 描述"离散"，二者携带的信息互不重叠。证明依赖正交变换或协方差结构：$\text{Cov}(\bar{X}, X_i - \bar{X}) = \dfrac{\sigma^2}{n} - \dfrac{\sigma^2}{n} = 0$，而正态分布中不相关等价于独立。

**定理四（t 统计量的分布）**：当 $\sigma$ 未知时，用 $S$ 代替 $\sigma$：

$$\frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$$

**完整推导**（这是检验"是否真懂"的试金石）：

由定理一与定理二：

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1), \quad \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$$

由定理三，$\bar{X}$ 与 $S^2$ 独立，故分子与分母中的 $\chi^2$ 独立。对照 $t$ 分布定义 $T = \dfrac{Z}{\sqrt{Y/n}}$（$Z \sim N(0,1)$，$Y \sim \chi^2(n)$，独立）：

$$T = \frac{\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}}{\sqrt{\frac{(n-1)S^2}{\sigma^2} \big/ (n-1)}} = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$$

注意：$\sigma$ 在分子分母中约掉了——这正是把未知的 $\sigma$ "藏进" $S$ 之后仍能得到**精确分布**的原因，也是 $t$ 检验的核心。

### 1.2 单正态总体抽样分布汇总

| 统计量 | 分布 | 条件 |
| --- | --- | --- |
| $\dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}}$ | $N(0, 1)$ | $\sigma$ 已知 |
| $\dfrac{(n-1)S^2}{\sigma^2}$ | $\chi^2(n-1)$ | — |
| $\dfrac{\bar{X} - \mu}{S/\sqrt{n}}$ | $t(n-1)$ | $\sigma$ 未知 |

**使用口诀**：均值找 $Z$ 或 $t$（看 $\sigma$ 知不知），方差找 $\chi^2$。

## 2. 双正态总体的抽样分布

### 2.1 基本设定

设 $X_1, X_2, \cdots, X_{n_1}$ 为来自 $N(\mu_1, \sigma_1^2)$ 的样本，$Y_1, Y_2, \cdots, Y_{n_2}$ 为来自 $N(\mu_2, \sigma_2^2)$ 的样本，两样本独立。

**定理五（均值差的分布，$\sigma_1^2, \sigma_2^2$ 已知）**：

$$\frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N(0, 1)$$

**证明思路**：$\bar{X} - \bar{Y}$ 是两个正态变量的差，仍服从正态分布：

$$E(\bar{X} - \bar{Y}) = \mu_1 - \mu_2, \quad D(\bar{X} - \bar{Y}) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$$

（两样本独立，方差相加。）

**定理六（均值差的分布，$\sigma_1^2 = \sigma_2^2 = \sigma^2$ 未知）**：

$$\frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{S_w\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 - 2)$$

其中 $S_w^2$ 为**联合方差**（合并方差）：

$$S_w^2 = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}$$

**证明思路**：当 $\sigma_1^2 = \sigma_2^2 = \sigma^2$ 时，

$$\frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{\sigma\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim N(0, 1)$$

且

$$\frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{\sigma^2} \sim \chi^2(n_1 + n_2 - 2)$$

（两个独立 $\chi^2$ 相加，自由度相加。）联合方差 $S_w^2$ 就是"把两组的平方和加总后除以总自由度"——它是 $\sigma^2$ 的无偏估计，且两个样本一起用、信息更充分。再由 $\bar{X} - \bar{Y}$ 与 $S_w^2$ 独立（这是 $\bar{X}_1$ 与 $S_1^2$、$\bar{X}_2$ 与 $S_2^2$ 独立性的推广），套 $t$ 分布定义即得。

**定理七（方差比的分布）**：

$$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim F(n_1 - 1, n_2 - 1)$$

特别地，当 $\sigma_1^2 = \sigma_2^2$ 时：

$$\frac{S_1^2}{S_2^2} \sim F(n_1 - 1, n_2 - 1)$$

**证明思路**：$\dfrac{(n_1-1)S_1^2}{\sigma_1^2} \sim \chi^2(n_1-1)$，$\dfrac{(n_2-1)S_2^2}{\sigma_2^2} \sim \chi^2(n_2-1)$，两样本独立。整理：

$$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} = \frac{\frac{(n_1-1)S_1^2}{\sigma_1^2}/(n_1-1)}{\frac{(n_2-1)S_2^2}{\sigma_2^2}/(n_2-1)} \sim F(n_1-1, n_2-1)$$

**直观理解**：比较两台机床谁更稳定，看样本方差之比。若 $\sigma_1^2 = \sigma_2^2$，比值应接近 1，偏离 1 太远就怀疑"稳定性有差异"——这就是后续 $F$ 检验的思想。

### 2.2 双正态总体抽样分布汇总

| 统计量 | 分布 | 条件 |
| --- | --- | --- |
| $\dfrac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}}$ | $N(0,1)$ | $\sigma_1^2, \sigma_2^2$ 已知 |
| $\dfrac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{S_w\sqrt{1/n_1+1/n_2}}$ | $t(n_1+n_2-2)$ | $\sigma_1^2=\sigma_2^2$ 未知 |
| $\dfrac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}$ | $F(n_1-1,n_2-1)$ | — |

## 3. 抽样分布定理的应用地图

### 3.1 参数估计

抽样分布是构造置信区间的原料：

- $\sigma$ 已知：用 $Z$ 统计量构造均值的置信区间（038 篇 1.1 节）
- $\sigma$ 未知：用 $t$ 统计量构造均值的置信区间（038 篇 1.2 节）
- 用 $\chi^2$ 统计量构造方差的置信区间（038 篇 2 节）
- 用 $F$ 统计量构造方差比的置信区间（038 篇 4 节）

### 3.2 假设检验

抽样分布是确定拒绝域的基础：

- $Z$ 检验：$\sigma$ 已知时的均值检验（041 篇）
- $t$ 检验：$\sigma$ 未知时的均值检验（042 篇）
- $\chi^2$ 检验：方差检验（043 篇）
- $F$ 检验：方差齐性检验（044 篇）

## 4. 完整例题

### 例题 1：正态总体均值的概率计算

设 $X_1, \cdots, X_{16}$ 为来自 $N(\mu, 4)$ 的样本，求 $P(|\bar{X} - \mu| < 0.5)$。

**解**：

由定理一，$\bar{X} \sim N\left(\mu, \dfrac{4}{16}\right) = N\left(\mu, \dfrac{1}{4}\right)$，故 $\dfrac{\bar{X} - \mu}{1/2} \sim N(0, 1)$。

$$P(|\bar{X} - \mu| < 0.5) = P\left(\left|\frac{\bar{X} - \mu}{0.5}\right| < 1\right) = 2\Phi(1) - 1 = 2 \times 0.8413 - 1 = 0.6826$$

**解读**：均值在 0.5 个单位的"误差圈"内的概率约 68.3%，这正是"$1\sigma$ 区间"规律在样本均值上的体现——只不过这里的 $\sigma$ 被压缩成了 $\sigma/\sqrt{n} = 0.5$。

### 例题 2：正态总体样本方差的期望与方差

设 $X_1, \cdots, X_{10}$ 为来自 $N(0, \sigma^2)$ 的样本，求 $E(S^2)$ 和 $D(S^2)$。

**解**：

由定理二，$\dfrac{9S^2}{\sigma^2} \sim \chi^2(9)$。由 $\chi^2$ 分布性质 $E(\chi^2(n)) = n$、$D(\chi^2(n)) = 2n$：

$$E\left(\frac{9S^2}{\sigma^2}\right) = 9 \implies E(S^2) = \sigma^2$$

$$D\left(\frac{9S^2}{\sigma^2}\right) = 18 \implies D(S^2) = \frac{18\sigma^4}{81} = \frac{2\sigma^4}{9}$$

**解读**：$E(S^2) = \sigma^2$ 再次验证无偏性；$D(S^2) = \dfrac{2\sigma^4}{9}$ 表明样本量越大，样本方差的波动越小。

### 例题 3：t 统计量的构造（$\sigma$ 未知）

设 $X_1, \cdots, X_9$ 为来自 $N(\mu, \sigma^2)$ 的样本（$\sigma$ 未知），求 $P(|\bar{X} - \mu| < S)$。

**解**：

由定理四，$T = \dfrac{\bar{X} - \mu}{S/\sqrt{9}} = \dfrac{3(\bar{X} - \mu)}{S} \sim t(8)$。

$$P(|\bar{X} - \mu| < S) = P\left(\left|\frac{3(\bar{X} - \mu)}{S}\right| < 3\right) = P(|T| < 3)$$

查 $t$ 分布表：$t_{0.01}(8) = 2.896$，$t_{0.005}(8) = 3.355$。因为 $2.896 < 3 < 3.355$：

$$P(|T| < 3) = 1 - 2P(T > 3) \approx 1 - 2 \times 0.0075 = 0.985$$

（更精确地，$P(T > 3) \approx 0.008$，$P(|T| < 3) \approx 0.984$。）

## 5. 常见错误与对策

| 错误类型 | 错误示例 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 乱用 $\sigma$ 条件 | $\sigma$ 未知还用 $Z$ 统计量 | 混淆定理一与定理四的使用前提 | 判断条件：$\sigma$ 已知用 $Z$，$\sigma$ 未知用 $t$，这是唯一判据 |
| 自由度计算错 | 双总体 $t$ 检验自由度写成 $n_1 + n_2$ | 忘掉"联合方差消耗 2 个自由度" | 自由度是 $n_1 + n_2 - 2$（各减 1 后相加） |
| 方差比方向错 | $\dfrac{S_1^2}{\sigma_1^2}$ 的分布写成 $F(n_2-1, n_1-1)$ | 分子分母自由度对应错位 | 第一自由度始终对应分子样本（$n_1 - 1$），第二对应分母（$n_2 - 1$） |
| 忽略独立性 | 认为 $\bar{X}$ 与 $S^2$ 一定独立 | 把正态总体特有性质推广到任意总体 | 独立性定理只对正态总体成立；非正态总体需大样本近似 |
| 均值差方差相加 | 认为 $D(\bar{X} - \bar{Y}) = \frac{\sigma_1^2}{n_1} - \frac{\sigma_2^2}{n_2}$ | 方差没有"减法" | 独立变量之差的方差是**相加**：$D(\bar{X} - \bar{Y}) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$ |
| 分位点用错 | 查 $t$ 表用 $\alpha$ 而非 $\alpha/2$（双侧时） | 混淆单侧与双侧尾部面积 | 双侧概率区间 $P(|T| < c) = 1-\alpha$ 对应 $c = t_{\alpha/2}(n-1)$ |

## 6. 实战练习

**练习 1（单总体均值）**：设 $X_1, \cdots, X_{25}$ 为来自 $N(\mu, \sigma^2)$ 的样本，$\sigma = 2$，求 $P(|\bar{X} - \mu| < 0.4)$。

**提示**：$\dfrac{\bar{X} - \mu}{2/5} \sim N(0,1)$。

**参考答案要点**：$P(|Z| < 1) = 2\Phi(1) - 1 = 0.6826$。

**练习 2（单总体方差）**：设 $X_1, \cdots, X_{20}$ 为来自 $N(\mu, \sigma^2)$ 的样本，求 $P\left(\dfrac{19S^2}{\sigma^2} \leq 30.144\right)$ 的近似值。

**提示**：$\dfrac{19S^2}{\sigma^2} \sim \chi^2(19)$，查 $\chi^2$ 表上分位数。

**参考答案要点**：$\chi^2_{0.05}(19) = 30.144$，故 $P(\chi^2(19) \leq 30.144) = 0.95$。

**练习 3（双总体均值差）**：$X_1, \cdots, X_{n_1} \sim N(\mu_1, \sigma^2)$ 与 $Y_1, \cdots, Y_{n_2} \sim N(\mu_2, \sigma^2)$ 独立，写出 $\bar{X} - \bar{Y}$ 的分布。

**提示**：用定理五的特例（$\sigma_1^2 = \sigma_2^2 = \sigma^2$ 已知）。

**参考答案要点**：$\bar{X} - \bar{Y} \sim N\left(\mu_1 - \mu_2, \sigma^2\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)\right)$。

**练习 4（双总体方差比）**：设 $n_1 = 9$，$n_2 = 11$，$\sigma_1^2 = \sigma_2^2$，求 $c$ 使 $P\left(\dfrac{S_1^2}{S_2^2} > c\right) = 0.05$。

**提示**：$\dfrac{S_1^2}{S_2^2} \sim F(8, 10)$。

**参考答案要点**：$c = F_{0.05}(8, 10) = 3.07$（查 F 分布表）。

**练习 5（综合）**：设 $X_1, \cdots, X_n \sim N(\mu, \sigma^2)$，证明 $\dfrac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$（写出完整推导过程）。

**提示**：三个定理按顺序组合：定理一给 $Z$，定理二给 $\chi^2$，定理三给独立性。

**参考答案要点**：$Z = \dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)$，$Y = \dfrac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$，$Z$ 与 $Y$ 独立（由 $\bar{X}$ 与 $S^2$ 独立），则 $\dfrac{Z}{\sqrt{Y/(n-1)}} = \dfrac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$。

## 7. 一句话记忆

**正态总体的抽样分布四定理：$\bar{X}$ 是正态（方差缩 $n$ 倍），$\frac{(n-1)S^2}{\sigma^2}$ 是 $\chi^2(n-1)$，$\bar{X}$ 与 $S^2$ 独立，于是 $\sigma$ 已知用 $Z$、$\sigma$ 未知用 $t$、比方差用 $F$。**

## 参考文献

- 盛骤、谢式千、潘承毅，《概率论与数理统计》（浙大版第四版），高等教育出版社：第六章第三节"正态总体的抽样分布"。
- 浙江大学概率论与数理统计 MOOC 第 42 讲（单个正态总体的抽样分布，定理一至定理四的证明）：https://cloud.moezx.cc/Document/mooc/%E6%B5%99%E5%A4%A7%E6%A6%82%E7%8E%87%E8%AE%BA/
- University of Chicago STAT 244 Lecture 13（样本均值与样本方差的分布）：https://statistics.uchicago.edu/~yibi/teaching/stat244/L13.pdf
- Khan Academy 统计与概率：https://zh.khanacademy.org/math/statistics-probability
- OpenIntro Statistics：https://www.openintro.org/book/os/

## 延伸阅读

- 统计量与样本方差无偏性的概念基础，见《统计量》。
- $\chi^2$、$t$、$F$ 分布的定义与性质，见《三大分布》。
- 抽样分布定理的查表与计算练习，见《抽样分布典型例题》。
- 利用抽样分布做区间估计与假设检验，见 035-045 文档。
