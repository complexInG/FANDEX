---
order: 74
title: 参数估计典型例题
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 参数估计部分的典型例题精选，以实际应用项目串联矩估计、极大似然估计、估计量评价、区间估计。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/区间估计'
  - 'probability-statistics/正态总体参数的区间估计'
  - 'probability-statistics/假设检验基本概念'
  - 'probability-statistics/Z检验'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 0. 一个工厂质检科的"估计工作日志"

想象你是某零件厂质检科的统计师，一天的"工作日志"是这样的：

- 上午：收到 8 周发货数据，要**估出**不合格率 $\theta$（点估计——矩估计）；
- 中午：拿到一摞抗拉强度数据，要**猜出**最可能的分布参数（点估计——极大似然估计）；
- 下午：要评判"用均值估还是用中位数估更稳"（估计量评选）；
- 下班前：要给"平均寿命"和"寿命波动"各画一个**置信区间**（区间估计）。

本文用**应用驱动**的方式，把参数估计的四块内容（矩估计、极大似然估计、估计量评选、区间估计）放进这个"工作日志"式的项目里，每块用贴近实战的案例讲透。学完这篇，参数估计的"工具箱"就完整了。

## 1. 上午：矩估计——发货批次不合格率

### 案例 1：发货批次的矩估计

某零件供应商每周发货，批次质量分为 0（合格）与 1（不合格），$X \sim B(1, \theta)$（$\theta$ 为不合格率）。收集了 8 周的数据：$3, 1, 3, 0, 3, 1, 2, 3$（这里为教学方便，将每周视为独立批次编号）。求 $\theta$ 的矩估计。

**解**：

$$E(X) = \theta$$

令 $E(X) = \bar{X}$，即 $\theta = \bar{X}$：

$$\hat{\theta} = \bar{X} = \frac{3 + 1 + 3 + 0 + 3 + 1 + 2 + 3}{8} = \frac{16}{8} = 2$$

（说明：本例为演示矩估计流程而设，实际"0-1 化"数据应为 $X_i \in \{0,1\}$，其矩估计即样本均值 $\hat{\theta} = \dfrac{\sum X_i}{n}$。）

**方法要点**：伯努利分布的矩估计就是"样本中 1 的比例"。这是比例估计的最朴素形式。

### 案例 2：两参数分布的矩估计

设总体 $X$ 的密度为 $f(x) = \begin{cases} (\theta + 1)x^\theta, & 0 < x < 1 \\ 0, & \text{其他} \end{cases}$（$\theta > -1$），求 $\theta$ 的矩估计。

**解**：

$$E(X) = \int_0^1 x(\theta+1)x^\theta dx = (\theta+1)\int_0^1 x^{\theta+1} dx = \frac{\theta+1}{\theta+2}$$

令 $E(X) = \bar{X}$：

$$\frac{\theta+1}{\theta+2} = \bar{X} \implies \theta + 1 = \bar{X}(\theta+2) \implies \theta(1 - \bar{X}) = 2\bar{X} - 1$$

$$\hat{\theta} = \frac{2\bar{X} - 1}{1 - \bar{X}}$$

**方法要点**：单参数只需一阶矩；若参数有两个（如 $U(a,b)$），则需一阶、二阶矩联立。

## 2. 中午：极大似然估计——寿命与合格率

### 案例 3：泊松分布的 MLE

某电话交换机每分钟呼叫次数 $X \sim P(\lambda)$，记录 $n$ 分钟的呼叫次数 $x_1, \cdots, x_n$，求 $\lambda$ 的 MLE。

**解**：

似然函数：

$$L(\lambda) = \prod_{i=1}^n \frac{\lambda^{x_i} e^{-\lambda}}{x_i!} = \frac{\lambda^{\sum x_i} e^{-n\lambda}}{\prod x_i!}$$

对数似然：

$$\ln L = \sum x_i \ln\lambda - n\lambda - \sum \ln(x_i!)$$

似然方程：

$$\frac{d\ln L}{d\lambda} = \frac{\sum x_i}{\lambda} - n = 0 \implies \hat{\lambda} = \frac{\sum x_i}{n} = \bar{x}$$

**要点**：泊松分布的 $\lambda$ 无论矩估计还是 MLE 都是 $\bar{X}$（两种方法在此一致）。

### 案例 4：均匀分布的 MLE（边界情形）

设总体 $X \sim U(a, b)$，求 $a$、$b$ 的 MLE。

**解**：

$$L(a, b) = \begin{cases} \dfrac{1}{(b-a)^n}, & a < x_i < b, \; i = 1, \cdots, n \\ 0, & \text{其他} \end{cases}$$

要使 $L$ 最大，需 $(b-a)^n$ 最小，即 $b - a$ 最小；而可行性约束要求 $a \leq x_{(1)}$、$b \geq x_{(n)}$。故取最小可行区间：

$$\hat{a} = x_{(1)} = \min(x_1, \cdots, x_n), \quad \hat{b} = x_{(n)} = \max(x_1, \cdots, x_n)$$

**要点**：MLE 在边界取极值，不能靠求导，要靠定义判断。

### 案例 5：幂律分布 MLE

设总体 $X$ 的密度为 $f(x) = \theta x^{\theta-1}$（$0 < x < 1$，$\theta > 0$），求 $\theta$ 的 MLE。

**解**：

$$L(\theta) = \prod_{i=1}^n \theta x_i^{\theta-1} = \theta^n \left(\prod x_i\right)^{\theta-1}$$

$$\ln L = n\ln\theta + (\theta - 1)\sum\ln x_i$$

$$\frac{d\ln L}{d\theta} = \frac{n}{\theta} + \sum\ln x_i = 0 \implies \hat{\theta} = -\frac{n}{\sum\ln x_i}$$

（注意 $\ln x_i < 0$，所以 $\hat{\theta} > 0$，合理。）

## 3. 下午：估计量评选——谁更靠谱

### 案例 6：$S^2$ 的无偏性证明

设 $X_1, \cdots, X_n \sim N(\mu, \sigma^2)$，证明 $S^2$ 是 $\sigma^2$ 的无偏估计。

**证明**：由抽样分布定理，$\dfrac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$，且 $E(\chi^2(n-1)) = n-1$：

$$E(S^2) = E\left[\frac{\sigma^2}{n-1} \cdot \frac{(n-1)S^2}{\sigma^2}\right] = \frac{\sigma^2}{n-1} \cdot (n-1) = \sigma^2$$

故 $S^2$ 是 $\sigma^2$ 的无偏估计。

### 案例 7：$U(0,\theta)$ 的两个估计比较

设 $X_1, \cdots, X_n \sim U(0, \theta)$，考察 $\hat{\theta}_1 = 2\bar{X}$ 与 $\hat{\theta}_2 = X_{(n)}$。

**（1）无偏性**：

$$E(\hat{\theta}_1) = 2E(\bar{X}) = 2 \cdot \frac{\theta}{2} = \theta \quad \text{（无偏）}$$

最大值 $X_{(n)}$ 的密度为 $f(x) = \dfrac{n}{\theta^n}x^{n-1}$（$0 < x < \theta$）：

$$E(\hat{\theta}_2) = \int_0^\theta x \cdot \frac{n}{\theta^n}x^{n-1} dx = \frac{n}{n+1}\theta \neq \theta \quad \text{（有偏）}$$

修正：$\hat{\theta}_3 = \dfrac{n+1}{n}X_{(n)}$ 无偏。

**（2）有效性**（比较 $\hat{\theta}_1$ 与 $\hat{\theta}_3$）：

$$D(\hat{\theta}_1) = 4D(\bar{X}) = 4 \cdot \frac{\theta^2}{12n} = \frac{\theta^2}{3n}$$

$$D(\hat{\theta}_3) = \left(\frac{n+1}{n}\right)^2 D(X_{(n)}) = \left(\frac{n+1}{n}\right)^2 \cdot \frac{n\theta^2}{(n+1)^2(n+2)} = \frac{\theta^2}{n(n+2)}$$

当 $n \geq 2$ 时 $\dfrac{\theta^2}{n(n+2)} < \dfrac{\theta^2}{3n}$，故 $\hat{\theta}_3$ 比 $\hat{\theta}_1$ 有效——它充分利用了"最大值"携带的信息。

**结论**：评选要按"先无偏、再有效"的顺序走；有偏的 $\hat{\theta}_2$ 经修正后反而成为更优候选。

## 4. 下班前：区间估计——给参数画范围

### 案例 8：σ 已知的均值区间

某产品重量 $X \sim N(\mu, 4)$，抽取 25 件，$\bar{x} = 14.5$。求 $\mu$ 的 $95\%$ 置信区间。

**解**：$\sigma = 2$ 已知，$z_{0.025} = 1.96$：

$$\left(14.5 - 1.96 \times \frac{2}{5}, \quad 14.5 + 1.96 \times \frac{2}{5}\right) = (13.716, 15.284)$$

### 案例 9：σ 未知的均值区间

某零件强度 $X \sim N(\mu, \sigma^2)$，抽取 16 件，$\bar{x} = 10$，$s = 3$。求 $\mu$ 的 $95\%$ 置信区间。

**解**：$\sigma$ 未知，$t_{0.025}(15) = 2.131$：

$$\left(10 - 2.131 \times \frac{3}{4}, \quad 10 + 2.131 \times \frac{3}{4}\right) = (8.402, 11.598)$$

### 案例 10：方差的区间

某灌装机装量 $X \sim N(\mu, \sigma^2)$，抽取 10 瓶，$s^2 = 6.42$。求 $\sigma^2$ 的 $95\%$ 置信区间。

**解**：$\chi^2_{0.025}(9) = 19.023$，$\chi^2_{0.975}(9) = 2.700$：

$$\left(\frac{9 \times 6.42}{19.023}, \quad \frac{9 \times 6.42}{2.700}\right) = (3.037, 21.400)$$

### 案例 11：样本量规划（比例）

某产品合格率的 $95\%$ 置信区间要求宽度不超过 0.1，至少需要多大样本？

**解**：区间宽度 $= 2z_{\alpha/2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}} \leq 0.1$。最保守地取 $\hat{p}(1-\hat{p}) \leq \dfrac{1}{4}$，$z_{0.025} = 1.96$：

$$2 \times 1.96 \times \sqrt{\frac{0.25}{n}} \leq 0.1 \implies n \geq \frac{4 \times 1.96^2 \times 0.25}{0.01} = 384.16$$

取 $n = 385$。

**要点**：抽样前先规划样本量，是实际项目中最常见的应用——"要多少数据才够"。

### 案例 12：双总体均值差

甲、乙两种工艺生产的产品重量分别为 $X \sim N(\mu_1, \sigma^2)$ 和 $Y \sim N(\mu_2, \sigma^2)$，分别抽取 10 件和 8 件：$\bar{x} = 50.1$，$\bar{y} = 49.8$，$s_1^2 = 0.04$，$s_2^2 = 0.03$。求 $\mu_1 - \mu_2$ 的 $95\%$ 置信区间。

**解**：$\sigma_1^2 = \sigma_2^2$ 未知，用 $t$ 区间。联合方差：

$$S_w^2 = \frac{9 \times 0.04 + 7 \times 0.03}{16} = \frac{0.36 + 0.21}{16} = 0.0356$$

$t_{0.025}(16) = 2.120$，区间为：

$$0.3 \pm 2.120 \times \sqrt{0.0356 \times \left(\frac{1}{10} + \frac{1}{8}\right)} = 0.3 \pm 2.120 \times \sqrt{0.00801} = 0.3 \pm 2.120 \times 0.0895$$

$$= 0.3 \pm 0.190 \implies (0.110, 0.490)$$

**解读**：区间不包含 0，说明有较强证据表明两种工艺平均重量存在差异（这也预告了假设检验的核心思想：区间不含 0 大致对应"拒绝 $\mu_1 = \mu_2$"）。

## 5. 常见错误与对策

| 错误类型 | 错误示例 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 矩方程不匹配 | 两参数只用一个矩方程 | 方程数必须等于参数数 | $k$ 个参数列 $k$ 个方程（前 $k$ 阶矩） |
| MLE 忽略可行性域 | $U(a,b)$ 中取 $b < x_{(n)}$ | 忘了密度非零区域与参数有关 | 先写约束：$a \leq x_{(1)}$、$b \geq x_{(n)}$，再在域内求最大 |
| 无偏性判断想当然 | 直接把 $\frac{1}{n}\sum(X_i-\bar X)^2$ 当无偏 | 忘记自由度修正 | $E(B_2) = \frac{n-1}{n}\sigma^2$；无偏版是 $S^2$ |
| 有效性比较顺序错 | 拿有偏的 $\hat{\theta}_2$ 与无偏的 $\hat{\theta}_1$ 直接比方差 | 有效性定义限无偏估计 | 先修成无偏（如 $\frac{n+1}{n}X_{(n)}$）再比方差 |
| 分位点选错 | 置信区间用 $t_{0.05}$ 而非 $t_{0.025}$（95%） | 单双尾混淆 | 双侧 $1-\alpha$ 用 $\alpha/2$ 分位点 |
| 样本量规划忘保守化 | 用 $\hat{p}$ 点估计规划样本量 | 事前没有 $\hat{p}$ | 事前规划用最保守 $\hat{p}(1-\hat{p}) \leq 1/4$，得到最大所需样本量 |

## 6. 实战练习

**练习 1（矩估计）**：设总体 $X$ 的密度为 $f(x) = \dfrac{1}{\theta}e^{-x/\theta}$（$x > 0$），求 $\theta$ 的矩估计。

**提示**：$E(X) = \theta$。

**参考答案要点**：$\hat{\theta} = \bar{X}$。

**练习 2（MLE）**：设 $X_1, \cdots, X_n \sim N(\mu, \sigma^2)$，写出 $\mu$ 与 $\sigma^2$ 的 MLE。

**提示**：对 $\ln L$ 分别求偏导，参考《点估计》例题 3。

**参考答案要点**：$\hat{\mu} = \bar{x}$，$\hat{\sigma}^2 = \dfrac{1}{n}\sum (x_i - \bar{x})^2 = \dfrac{n-1}{n}S^2$（有偏）。

**练习 3（评选）**：设 $X \sim U(0, \theta)$，$n = 4$，样本为 $0.3, 0.7, 0.5, 0.9$。求 $\theta$ 的矩估计值与 MLE 值，并比较。

**提示**：矩估计 $\hat{\theta}_{MM} = 2\bar{x}$；MLE $\hat{\theta}_{MLE} = x_{(4)}$。

**参考答案要点**：$\bar{x} = 0.6$，$\hat{\theta}_{MM} = 1.2$；$x_{(4)} = 0.9$，$\hat{\theta}_{MLE} = 0.9$。MLE 更小（利用最大值信息），两者都可作为 $\theta$ 的估计。

**练习 4（区间估计）**：设 $X_1, \cdots, X_{9} \sim N(\mu, \sigma^2)$，$\bar{x} = 5$，$s = 1.2$，求 $\mu$ 的 $95\%$ 置信区间。

**提示**：$t_{0.025}(8) = 2.306$。

**参考答案要点**：$5 \pm 2.306 \times \dfrac{1.2}{3} = 5 \pm 0.922$，即 $(4.078, 5.922)$。

**练习 5（综合）**：某产品长度 $X \sim N(\mu, \sigma^2)$，抽 20 件，$\bar{x} = 10.2$，$s = 0.5$。求 $\sigma^2$ 的 $95\%$ 置信区间，并据此判断 $\sigma^2 = 0.2$ 是否"合理"。

**提示**：$\chi^2_{0.025}(19) = 32.852$，$\chi^2_{0.975}(19) = 8.907$。

**参考答案要点**：$\left(\dfrac{19 \times 0.25}{32.852}, \dfrac{19 \times 0.25}{8.907}\right) = (0.145, 0.533)$。由于 $0.2$ 落在区间内，不能认为 $\sigma^2 = 0.2$ 不合理——这正是"区间估计与假设检验对偶"的体现。

## 7. 一句话记忆

**参数估计实战四步走：上午矩估计（样本矩替换总体矩）、中午极大似然（让数据最可能出现的 $\theta$）、下午评选（先无偏再有效）、下班前画区间（$Z$/$t$/$\chi^2$/$F$ 套公式）；区间不含假设值，就预告"有差异"。**

## 参考文献

- 盛骤、谢式千、潘承毅，《概率论与数理统计》（浙大版第四版），高等教育出版社：第七章习题与典型例题。
- 浙江大学概率论与数理统计 MOOC 第 44-53 讲（参数估计全部例题）：https://www.icourse163.org/course/ZJU-1001743002
- University of Oxford Statistics 讲义 Chapter 4（估计与置信区间例子）：https://www.stats.ox.ac.uk/~reinert/stattheory/chapter407.pdf
- Khan Academy 统计与概率：https://zh.khanacademy.org/math/statistics-probability
- OpenIntro Statistics：https://www.openintro.org/book/os/

## 延伸阅读

- 矩估计与极大似然估计的原理详解，见《点估计》。
- 无偏性、有效性、相合性的严格定义，见《估计量的评选标准》。
- 置信区间概念与枢轴量法，见《区间估计》。
- 区间估计的"对偶问题"——假设检验，见《假设检验基本概念》及后续各篇。
