---
order: 73
title: 正态总体参数的区间估计
module: 'probability-statistics'
category: 'comp-sci'
difficulty: advanced
description: 正态总体均值、方差的区间估计公式（σ已知、σ未知、方差区间），以"体检指标正常范围"类比串联全部公式。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/估计量的评选标准'
  - 'probability-statistics/区间估计'
  - 'probability-statistics/参数估计典型例题'
  - 'probability-statistics/假设检验基本概念'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 0. 体检指标的正常范围是怎么定的

体检报告上每个指标旁边都有一栏"参考范围"，比如空腹血糖 3.9-6.1 mmol/L。这个范围是怎么来的？本质是：**把大量健康人的血糖数据收集起来，算出均值和波动，然后给出一个"95% 的人都会落在其中"的区间**——这就是区间估计！

体检报告的逻辑链条：

- 想知道"我的血糖是否正常" → 需要知道健康人血糖的**参考区间**；
- 参考区间怎么算？→ 用抽样样本的 $\bar{x}$ 和 $s$，套**区间估计公式**；
- 不同指标用不同公式 → 看"指标（$\mu$ 还是 $\sigma^2$）"和"已知条件（$\sigma$ 已知/未知）"。

本文用**公式驱动**的方式，把正态总体参数区间估计的"公式全家桶"一次性列全，并为每条公式配"适用条件 + 推导思路 + 数值例题"。本文是全模块的"公式字典"，做题时随查随用。

## 1. 单正态总体均值的区间估计

设 $X_1, X_2, \cdots, X_n \sim N(\mu, \sigma^2)$，置信水平 $1 - \alpha$。

### 1.1 σ 已知：Z 区间

**枢轴量**：

$$Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$

**置信区间**：

$$\left(\bar{X} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \quad \bar{X} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right)$$

**区间宽度**：$2z_{\alpha/2}\dfrac{\sigma}{\sqrt{n}}$——与 $\sigma$ 成正比、与 $\sqrt{n}$ 成反比。

**推导思路**：由 $P\left(-z_{\alpha/2} < \dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}} < z_{\alpha/2}\right) = 1 - \alpha$，对 $\mu$ 反解即得。这一行是所有公式的"模板"。

### 1.2 σ 未知：t 区间

**枢轴量**：

$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$$

**置信区间**：

$$\left(\bar{X} - t_{\alpha/2}(n-1)\frac{S}{\sqrt{n}}, \quad \bar{X} + t_{\alpha/2}(n-1)\frac{S}{\sqrt{n}}\right)$$

**要点**：自由度是 $n-1$；因为 $t$ 分布尾部更厚，相同置信水平下 $t_{\alpha/2}(n-1) > z_{\alpha/2}$，所以 $\sigma$ 未知时区间更宽——这"多出的宽度"是为"不知道 $\sigma$"付出的代价。

### 1.3 完整例题（σ 未知）

**例题**：从某批零件中抽取 9 件，测得长度（mm）为：21.1, 21.3, 21.4, 21.5, 21.3, 21.7, 21.4, 21.3, 21.6。设零件长度服从正态分布，求总体均值 $\mu$ 的 $95\%$ 置信区间。

**解**：$n = 9$，$\sigma$ 未知，用 $t$ 区间。

$$\bar{x} = \frac{21.1 + 21.3 + 21.4 + 21.5 + 21.3 + 21.7 + 21.4 + 21.3 + 21.6}{9} = \frac{192.6}{9} = 21.4$$

$$\sum x_i^2 = 21.1^2 + 21.3^2 \times 3 + 21.4^2 \times 2 + 21.5^2 + 21.7^2 + 21.6^2 = 445.21 + 1362.27 + 915.92 + 462.25 + 470.89 + 466.56 = 4123.10$$

$$S^2 = \frac{1}{8}(4123.10 - 9 \times 21.4^2) = \frac{1}{8}(4123.10 - 4121.64) = \frac{1.46}{8} = 0.1825, \quad S \approx 0.427$$

查表 $t_{0.025}(8) = 2.306$，区间为：

$$\left(21.4 - 2.306 \times \frac{0.427}{3}, \quad 21.4 + 2.306 \times \frac{0.427}{3}\right) = (21.072, 21.728)$$

**解读**：95% 的把握认为零件平均长度在 21.072 到 21.728 mm 之间。

## 2. 单正态总体方差的区间估计

### 2.1 公式

**枢轴量**：

$$\chi^2 = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$$

**置信区间**（注意 $\chi^2$ 不对称，上下分位数不同）：

$$P\left(\chi^2_{1-\alpha/2}(n-1) < \frac{(n-1)S^2}{\sigma^2} < \chi^2_{\alpha/2}(n-1)\right) = 1 - \alpha$$

$\sigma^2$ 的置信区间：

$$\left(\frac{(n-1)S^2}{\chi^2_{\alpha/2}(n-1)}, \quad \frac{(n-1)S^2}{\chi^2_{1-\alpha/2}(n-1)}\right)$$

$\sigma$ 的置信区间（开方即可）：

$$\left(\sqrt{\frac{(n-1)S^2}{\chi^2_{\alpha/2}(n-1)}}, \quad \sqrt{\frac{(n-1)S^2}{\chi^2_{1-\alpha/2}(n-1)}}\right)$$

**记忆诀窍**：不等式两边取倒数后不等号反向——"大分位点在分母、给出下限；小分位点在分母、给出上限"（因为 $\chi^2_{1-\alpha/2} < \chi^2_{\alpha/2}$，除以小分位点得大上限，除以大分位点得小下限）。

### 2.2 完整例题

**例题**：设 $n = 16$，$s^2 = 4$，求 $\sigma^2$ 的 $95\%$ 置信区间。

**解**：查表 $\chi^2_{0.025}(15) = 27.488$，$\chi^2_{0.975}(15) = 6.262$。

$$\left(\frac{15 \times 4}{27.488}, \quad \frac{15 \times 4}{6.262}\right) = (2.183, 9.583)$$

**解读**：95% 的把握认为总体方差在 2.183 到 9.583 之间。注意区间不对称——这是 $\chi^2$ 分布右偏的直接体现。

## 3. 双正态总体均值差的区间估计

设 $X_1, \cdots, X_{n_1} \sim N(\mu_1, \sigma_1^2)$，$Y_1, \cdots, Y_{n_2} \sim N(\mu_2, \sigma_2^2)$，两样本独立。

### 3.1 σ₁² 和 σ₂² 已知：Z 区间

$$\left((\bar{X} - \bar{Y}) - z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}, \quad (\bar{X} - \bar{Y}) + z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}\right)$$

### 3.2 σ₁² = σ₂² = σ² 未知：t 区间

$$\left((\bar{X} - \bar{Y}) - t_{\alpha/2}(n_1+n_2-2)S_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}, \quad (\bar{X} - \bar{Y}) + t_{\alpha/2}(n_1+n_2-2)S_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}\right)$$

其中联合方差

$$S_w^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1 + n_2 - 2}$$

自由度 $n_1 + n_2 - 2$。这是"两个总体均值是否有差异"问题（如两种工艺对比）的核心公式。

### 3.3 σ₁² ≠ σ₂² 且未知：大样本近似

当 $n_1, n_2$ 都较大时，由中心极限定理可用近似区间：

$$\left((\bar{X} - \bar{Y}) - z_{\alpha/2}\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}, \quad (\bar{X} - \bar{Y}) + z_{\alpha/2}\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}\right)$$

## 4. 双正态总体方差比的区间估计

### 4.1 公式

**枢轴量**：

$$F = \frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim F(n_1-1, n_2-1)$$

$\dfrac{\sigma_1^2}{\sigma_2^2}$ 的置信区间：

$$\left(\frac{S_1^2}{S_2^2} \cdot \frac{1}{F_{\alpha/2}(n_1-1, n_2-1)}, \quad \frac{S_1^2}{S_2^2} \cdot F_{\alpha/2}(n_2-1, n_1-1)\right)$$

**要点**：上限用了 $F_{\alpha/2}(n_2-1, n_1-1)$（自由度颠倒）——这来自 $F$ 分布的倒数关系 $F_{1-\alpha}(n_1, n_2) = \dfrac{1}{F_\alpha(n_2, n_1)}$。

## 5. 非正态总体的近似区间估计

### 5.1 大样本均值近似区间

当总体分布未知、$n$ 较大时，由中心极限定理：

$$\frac{\bar{X} - \mu}{S/\sqrt{n}} \overset{\text{近似}}{\sim} N(0, 1)$$

$\mu$ 的近似置信区间：

$$\left(\bar{X} - z_{\alpha/2}\frac{S}{\sqrt{n}}, \quad \bar{X} + z_{\alpha/2}\frac{S}{\sqrt{n}}\right)$$

### 5.2 比例的区间估计（(0-1) 分布）

设 $X \sim B(n, p)$，$\hat{p} = X/n$，当 $n$ 较大时（一般要求 $n\hat{p} \geq 5$ 且 $n(1-\hat{p}) \geq 5$）：

$$\frac{\hat{p} - p}{\sqrt{\hat{p}(1-\hat{p})/n}} \overset{\text{近似}}{\sim} N(0, 1)$$

$p$ 的近似置信区间：

$$\left(\hat{p} - z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}, \quad \hat{p} + z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\right)$$

**完整例题**：调查 400 名用户，其中 120 人偏好某产品。求该产品偏好比例 $p$ 的 $95\%$ 近似置信区间。

**解**：$\hat{p} = 120/400 = 0.3$，$z_{0.025} = 1.96$。

$$\sqrt{\frac{0.3 \times 0.7}{400}} = \sqrt{0.000525} \approx 0.0229$$

$$0.3 \pm 1.96 \times 0.0229 = 0.3 \pm 0.0449$$

即 $(0.255, 0.345)$：95% 的把握认为偏好比例在 25.5% 到 34.5% 之间。

## 6. 公式全家桶汇总表

| 待估参数 | 条件 | 枢轴量 | 置信区间 | 自由度/分位数 |
| --- | --- | --- | --- | --- |
| $\mu$ | $\sigma$ 已知 | $Z = \dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}}$ | $\bar{X} \pm z_{\alpha/2}\dfrac{\sigma}{\sqrt{n}}$ | $z_{\alpha/2}$ |
| $\mu$ | $\sigma$ 未知 | $T = \dfrac{\bar{X} - \mu}{S/\sqrt{n}}$ | $\bar{X} \pm t_{\alpha/2}(n-1)\dfrac{S}{\sqrt{n}}$ | $n-1$ |
| $\sigma^2$ | — | $\chi^2 = \dfrac{(n-1)S^2}{\sigma^2}$ | $\left(\dfrac{(n-1)S^2}{\chi^2_{\alpha/2}}, \dfrac{(n-1)S^2}{\chi^2_{1-\alpha/2}}\right)$ | $n-1$ |
| $\mu_1 - \mu_2$ | $\sigma_1^2, \sigma_2^2$ 已知 | $Z$ | $(\bar{X}-\bar{Y}) \pm z_{\alpha/2}\sqrt{\dfrac{\sigma_1^2}{n_1}+\dfrac{\sigma_2^2}{n_2}}$ | $z_{\alpha/2}$ |
| $\mu_1 - \mu_2$ | $\sigma_1^2 = \sigma_2^2$ 未知 | $T$ | $(\bar{X}-\bar{Y}) \pm t_{\alpha/2}S_w\sqrt{\dfrac{1}{n_1}+\dfrac{1}{n_2}}$ | $n_1+n_2-2$ |
| $\dfrac{\sigma_1^2}{\sigma_2^2}$ | — | $F = \dfrac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}$ | $\left(\dfrac{S_1^2/S_2^2}{F_{\alpha/2}(n_1-1,n_2-1)}, \dfrac{S_1^2}{S_2^2}F_{\alpha/2}(n_2-1,n_1-1)\right)$ | $(n_1-1, n_2-1)$ |
| $p$ | 大样本 | $Z$（近似） | $\hat{p} \pm z_{\alpha/2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$ | 近似 |

**选题口诀**："均值看 $\sigma$，方差看 $\chi^2$，差值看 $t$，比值看 $F$。"

## 7. 常见错误与对策

| 错误类型 | 错误示例 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 条件误判 | $\sigma$ 未知用 $z_{\alpha/2}$ 公式 | 没看题给条件 | 题给 $\sigma$ 或可直接求 $\sigma$ 的用 $Z$；只给 $s$ 的用 $t$ |
| 方差区间分位点写反 | $\sigma^2$ 区间写成 $\left(\frac{·}{\chi^2_{1-\alpha/2}}, \frac{·}{\chi^2_{\alpha/2}}\right)$ | 不等式取倒数忘变号 | 记住"除以大分位点得下限、除以小分位点得上限"：$\left(\frac{(n-1)S^2}{\chi^2_{\alpha/2}}, \frac{(n-1)S^2}{\chi^2_{1-\alpha/2}}\right)$ |
| 联合方差算错 | $S_w^2$ 用 $n_1 + n_2$ 做分母 | 忘记自由度 | $S_w^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$ |
| F 区间自由度错 | 上限也用 $F_{\alpha/2}(n_1-1, n_2-1)$ | 没用到倒数关系 | 上限用 $F_{\alpha/2}(n_2-1, n_1-1)$，自由度颠倒 |
| 比例区间条件不满足 | $n\hat{p}$ 很小时强行用正态近似 | 忽略近似条件 | 先检查 $n\hat{p} \geq 5$ 且 $n(1-\hat{p}) \geq 5$，不满足则需更大样本或用精确方法 |
| 大样本误用精确分布 | 非正态总体小样本用 $Z$ | 混淆"近似"与"精确" | 非正态总体必须 $n$ 大（经验值 $\geq 30$）才可近似；小样本需知道具体分布或转非参数方法 |

## 8. 实战练习

**练习 1（σ 已知）**：设 $X_1, \cdots, X_{25} \sim N(\mu, 4)$，$\bar{x} = 14.5$，求 $\mu$ 的 $95\%$ 置信区间。

**提示**：$\sigma = 2$，$z_{0.025} = 1.96$。

**参考答案要点**：$14.5 \pm 1.96 \times \dfrac{2}{5} = (13.716, 15.284)$。

**练习 2（σ 未知）**：设 $X_1, \cdots, X_{16} \sim N(\mu, \sigma^2)$，$\bar{x} = 10$，$s = 3$，求 $\mu$ 的 $95\%$ 置信区间。

**提示**：$t_{0.025}(15) = 2.131$。

**参考答案要点**：$10 \pm 2.131 \times \dfrac{3}{4} = (8.402, 11.598)$。

**练习 3（方差区间）**：设 $X_1, \cdots, X_{10} \sim N(\mu, \sigma^2)$，$s^2 = 6.42$，求 $\sigma^2$ 的 $95\%$ 置信区间。

**提示**：$\chi^2_{0.025}(9) = 19.023$，$\chi^2_{0.975}(9) = 2.700$。

**参考答案要点**：$\left(\dfrac{9 \times 6.42}{19.023}, \dfrac{9 \times 6.42}{2.700}\right) = (3.037, 21.400)$。

**练习 4（均值差）**：甲工艺抽 10 件、乙工艺抽 8 件，$\bar{x} = 50.1$，$\bar{y} = 49.8$，$s_1^2 = 0.04$，$s_2^2 = 0.03$，设两总体方差相等且未知，求 $\mu_1 - \mu_2$ 的 $95\%$ 置信区间。

**提示**：$S_w^2 = \dfrac{9 \times 0.04 + 7 \times 0.03}{16} = 0.0356$，$t_{0.025}(16) = 2.120$。

**参考答案要点**：$0.3 \pm 2.120\sqrt{0.0356 \times \left(\dfrac{1}{10} + \dfrac{1}{8}\right)} = 0.3 \pm 0.189$，即 $(0.111, 0.489)$。

**练习 5（样本量规划 + 比例）**：某产品合格率的 $95\%$ 置信区间要求宽度不超过 0.1，至少需要多大的样本量？（用最保守的 $\hat{p}(1-\hat{p}) \leq 1/4$）

**提示**：宽度 $2z_{0.025}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}} \leq 0.1$，$\hat{p}(1-\hat{p})$ 最大为 $1/4$。

**参考答案要点**：$2 \times 1.96 \times \sqrt{\dfrac{0.25}{n}} \leq 0.1 \implies n \geq \dfrac{4 \times 1.96^2 \times 0.25}{0.01} = 384.16$，取 $n = 385$。

## 9. 一句话记忆

**正态总体的区间估计公式全家桶：均值配 $Z$（$\sigma$ 已知）或 $t$（$\sigma$ 未知）、方差配 $\chi^2$（除以大分位点得下限）、均值差配 $t$（联合方差、自由度 $n_1+n_2-2$）、方差比配 $F$（上限自由度颠倒）。**

## 参考文献

- 盛骤、谢式千、潘承毅，《概率论与数理统计》（浙大版第四版），高等教育出版社：第七章第三节、第四节"区间估计"全部公式。
- University of Oxford Statistics 讲义 Chapter 4（正态总体参数置信区间的构造与例子）：https://www.stats.ox.ac.uk/~reinert/stattheory/chapter407.pdf
- 浙江大学概率论与数理统计 MOOC 第 49-53 讲（区间估计公式推导与例题）：https://www.icourse163.org/course/ZJU-1001743002
- Khan Academy 统计与概率：https://zh.khanacademy.org/math/statistics-probability
- OpenIntro Statistics：https://www.openintro.org/book/os/

## 延伸阅读

- 置信区间的概念与枢轴量法，见《区间估计》。
- 估计量评价标准（为什么用 $n-1$、$t$ 而非 $Z$），见《估计量的评选标准》。
- 区间估计与点估计的混合应用，见《参数估计典型例题》。
- 区间估计与假设检验的"对偶关系"，见《假设检验基本概念》及后续检验各篇。
