---
order: 53
title: 大数定律与中心极限定理典型例题
module: 'probability-statistics'
category: 'comp-sci'
difficulty: intermediate
description: 大数定律与中心极限定理部分的典型例题精选，涵盖切比雪夫不等式、频率估计、正态近似计算等应用。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/大数定律'
  - 'probability-statistics/中心极限定理'
  - 'probability-statistics/随机样本'
  - 'probability-statistics/统计量'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 0. 从一个生活场景说起：三个典型的"应用现场"

假设你在三家单位分别遇到三个问题：

1. **质检车间**：只知道次品率的期望和方差，想在抽检前划一条"合格范围"——用**切比雪夫不等式**；
2. **市场调研**：用 1 万份问卷的样本均值估计总体均值，想知道这个估计靠不靠谱——用**大数定律**；
3. **保险公司**：1 万人投保，要算"赔付总额超预算"的概率——用**中心极限定理**。

三个问题对应三大定理的三种典型用途：**划界限（不等式）、证收敛（LLN）、算概率（CLT）**。本文是"**应用驱动**"的综合例题篇：按工具分组编排例题，每题给出完整步骤与要点，帮助你建立"看到什么条件、就用什么定理"的自动反应。

## 1. 工具一：切比雪夫不等式（划界限）

### 例题 1（估计区间概率）

设 $E(X) = 1$，$D(X) = 0.04$，利用切比雪夫不等式估计 $P(0.6 < X < 1.4)$。

**解**：区间关于 $E(X) = 1$ 对称，半宽 $\varepsilon = 0.4$。

$$P(0.6 < X < 1.4) = P(|X - 1| < 0.4) \geq 1 - \frac{D(X)}{\varepsilon^2} = 1 - \frac{0.04}{0.16} = 0.75$$

**要点**：使用前提是区间以 $\mu$ 为中心；若区间不对称，先判断是否包含中心，再选择使用双边或单边形式。

### 例题 2（样本均值精度）

设 $X_1, X_2, \cdots, X_{100}$ 独立同分布，$E(X_i) = 5$，$D(X_i) = 1$，估计 $P(4.7 < \bar{X} < 5.3)$。

**解**：$E(\bar{X}) = 5$，$D(\bar{X}) = \dfrac{1}{100} = 0.01$，半宽 $\varepsilon = 0.3$。

$$P(4.7 < \bar{X} < 5.3) = P(|\bar{X} - 5| < 0.3) \geq 1 - \frac{0.01}{0.09} = \frac{8}{9} \approx 0.889$$

**对比**：用中心极限定理算得的精确近似约 0.997，切比雪夫给出的 0.889 是保守下界——**切比雪夫适合"不知道分布"时的兜底保证**。

### 例题 3（单边事件的上界）

设 $X \sim P(5)$，利用切比雪夫不等式估计 $P(X \geq 10)$。

**解**：$E(X) = 5$，$D(X) = 5$。单边事件含于双边事件：

$$P(X \geq 10) = P(X - 5 \geq 5) \leq P(|X - 5| \geq 5) \leq \frac{5}{25} = 0.2$$

**要点**：切比雪夫给的是上界，真实值约 0.032，0.2 明显偏保守——这正是"分布无关"的代价。

## 2. 工具二：大数定律（证收敛）

### 例题 4（函数平均的极限）

设 $X_1, X_2, \cdots$ 独立同分布，$E(X_i) = \mu$，$D(X_i) = \sigma^2$，证明 $\dfrac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{P} \mu^2 + \sigma^2$。

**证明**：设 $Y_i = X_i^2$，则 $Y_i$ 独立同分布，且

$$E(Y_i) = E(X_i^2) = D(X_i) + [E(X_i)]^2 = \sigma^2 + \mu^2$$

由辛钦大数定律：

$$\frac{1}{n}\sum_{i=1}^n Y_i = \frac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{P} \sigma^2 + \mu^2$$

**要点**：证明"随机变量函数的平均收敛"只有一条路——构造 $Y_i = g(X_i)$，验证 $E(Y_i)$ 存在，套辛钦大数定律。

### 例题 5（构造法求极限）

设 $X_1, X_2, \cdots$ 独立同分布，$X_i \sim U(0, 1)$，证明 $\dfrac{1}{n}\sum_{i=1}^n X_i(1 - X_i) \xrightarrow{P} \dfrac{1}{6}$。

**证明**：设 $Y_i = X_i(1 - X_i)$：

$$E(Y_i) = E(X_i) - E(X_i^2) = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$

由辛钦大数定律，$\dfrac{1}{n}\sum_{i=1}^n Y_i \xrightarrow{P} \dfrac{1}{6}$。

### 例题 6（频率估计的样本量）

某事件 $A$ 每次试验发生概率为 $p$，独立重复试验 $n$ 次，用频率 $\dfrac{n_A}{n}$ 估计 $p$。要使 $P\left(\left|\dfrac{n_A}{n} - p\right| < 0.01\right) \geq 0.95$，$n$ 至少为多少？

**解**：$E\left(\dfrac{n_A}{n}\right) = p$，$D\left(\dfrac{n_A}{n}\right) = \dfrac{p(1-p)}{n}$。由切比雪夫不等式：

$$P\left(\left|\frac{n_A}{n} - p\right| < 0.01\right) \geq 1 - \frac{p(1-p)}{n \times 10^{-4}}$$

$p(1-p) \leq \dfrac{1}{4}$（$p = 0.5$ 时最大），故

$$1 - \frac{1}{4n \times 10^{-4}} \geq 0.95 \quad \Longrightarrow \quad n \geq \frac{1}{4 \times 10^{-4} \times 0.05} = 50000$$

**要点**：$p$ 未知时用 $p(1-p) \le \dfrac{1}{4}$ 放大，得到与 $p$ 无关的保守样本量。注意：这个 50000 是切比雪夫路线给出的；若用 CLT 路线只需约 9600（见练习 4）。

## 3. 工具三：中心极限定理（算概率）

### 例题 7（二项分布的正态近似）

某厂产品次品率 0.03，任取 1000 件，求次品数在 20 到 40 之间的概率。

**解**：设 $X$ 为次品数，$X \sim B(1000, 0.03)$。$E(X) = 30$，$D(X) = 1000 \times 0.03 \times 0.97 = 29.1$。

条件检查：$np = 30 \ge 5$，$n(1-p) = 970 \ge 5$，可用正态近似（区间端点离均值较远，修正与否差别小，此处直接用）：

$$P(20 \leq X \leq 40) \approx \Phi\left(\frac{40 - 30}{\sqrt{29.1}}\right) - \Phi\left(\frac{20 - 30}{\sqrt{29.1}}\right) = 2\Phi(1.854) - 1 \approx 0.9364$$

### 例题 8（指数分布之和）

设 $X_1, \cdots, X_{50}$ 独立同分布，$X_i \sim \text{Exp}(2)$，求 $P\left(\sum_{i=1}^{50} X_i > 30\right)$。

**解**：$E(X_i) = \dfrac{1}{2} = 0.5$，$D(X_i) = \dfrac{1}{4} = 0.25$。

$$E(S) = 25, \qquad D(S) = 50 \times 0.25 = 12.5$$

$$P(S > 30) \approx 1 - \Phi\left(\frac{30 - 25}{\sqrt{12.5}}\right) = 1 - \Phi(1.414) \approx 1 - 0.9214 = 0.0786$$

**要点**：指数分布和的正态近似，直接套 $\sum X_i \sim N(n\mu, n\sigma^2)$，无需任何修正（连续型）。

### 例题 9（样本均值近似）

设 $X_1, \cdots, X_{36}$ 独立同分布，$X_i \sim U(0, 10)$，求 $P(\bar{X} > 5.5)$。

**解**：$E(X_i) = 5$，$D(X_i) = \dfrac{(10)^2}{12} = \dfrac{25}{3}$。

$$E(\bar{X}) = 5, \qquad D(\bar{X}) = \frac{25/3}{36} = \frac{25}{108}$$

$$P(\bar{X} > 5.5) \approx 1 - \Phi\left(\frac{5.5 - 5}{\sqrt{25/108}}\right) = 1 - \Phi(1.039) \approx 1 - 0.8506 = 0.1494$$

### 例题 10（保险赔付：经典应用题）

某保险公司有 10000 人投保，每人每年交保费 12 元，每人出险概率 0.006，出险时赔付 1000 元。求保险公司亏本的概率。

**解**：设 $X$ 为出险人数，$X \sim B(10000, 0.006)$。

保险公司收入 $= 10000 \times 12 = 120000$ 元，赔付 $= 1000X$ 元。亏本条件：$1000X > 120000$，即 $X > 120$。

$$E(X) = 60, \qquad D(X) = 10000 \times 0.006 \times 0.994 = 59.64$$

$$P(X > 120) \approx 1 - \Phi\left(\frac{120 - 60}{\sqrt{59.64}}\right) = 1 - \Phi(7.77) \approx 0$$

**结论**：亏本概率几乎为 0——保费定价的数学保障。**要点**：先列"亏本不等式"，再标准化查表；当标准化值超过 4-5 个标准差时概率已经微乎其微。

### 例题 11（反解样本量）

设 $X_1, \cdots, X_n$ 独立同分布，$E(X_i) = 0$，$D(X_i) = 1$，求 $n$ 使 $P\left(\left|\sum_{i=1}^n X_i\right| < 10\right) \geq 0.9$。

**解**：$\sum_{i=1}^n X_i$ 近似服从 $N(0, n)$。

$$P\left(\left|\sum X_i\right| < 10\right) = P\left(\frac{|\sum X_i|}{\sqrt{n}} < \frac{10}{\sqrt{n}}\right) \approx 2\Phi\left(\frac{10}{\sqrt{n}}\right) - 1 \geq 0.9$$

$$\Phi\left(\frac{10}{\sqrt{n}}\right) \geq 0.95 \quad \Longrightarrow \quad \frac{10}{\sqrt{n}} \geq 1.645 \quad \Longrightarrow \quad n \leq \left(\frac{10}{1.645}\right)^2 \approx 36.9$$

取 $n \leq 36$。**注意**：$n$ 越大，$\sum X_i$ 的波动（$\sqrt{n}$）越大，区间 $(-10, 10)$ 反而更难覆盖——所以这里是 $n$ 的**上界**，与直觉相反，务必小心。

### 例题 12（产品重量装箱）

设 $X_i$ 表示第 $i$ 个产品重量（克），$E(X_i) = 50$，$D(X_i) = 25$。一箱装 100 个，求一箱重量超过 5025 克的概率。

**解**：$S = \sum_{i=1}^{100} X_i$，$E(S) = 5000$，$D(S) = 2500$，$\sigma_S = 50$。

$$P(S > 5025) \approx 1 - \Phi\left(\frac{5025 - 5000}{50}\right) = 1 - \Phi(0.5) = 1 - 0.6915 = 0.3085$$

## 4. 综合提高题

### 例题 13（依概率收敛的运算性质）

证明：若 $X_n \xrightarrow{P} X$，$Y_n \xrightarrow{P} Y$，则 $X_n + Y_n \xrightarrow{P} X + Y$。

**证明**：对任意 $\varepsilon > 0$，利用三角不等式：

$$\{|(X_n + Y_n) - (X + Y)| \geq \varepsilon\} \subseteq \left\{|X_n - X| \geq \frac{\varepsilon}{2}\right\} \cup \left\{|Y_n - Y| \geq \frac{\varepsilon}{2}\right\}$$

$$P(|(X_n+Y_n) - (X+Y)| \geq \varepsilon) \leq P\left(|X_n - X| \geq \frac{\varepsilon}{2}\right) + P\left(|Y_n - Y| \geq \frac{\varepsilon}{2}\right) \to 0$$

**要点**：依概率收敛对加法封闭，证明套路是"三角不等式 + 事件并的概率界"。

### 例题 14（均值区间概率）

设 $X_1, X_2, \cdots$ 独立同分布，$E(X_i) = 3$，$D(X_i) = 4$，求 $P(2.8 < \bar{X}_{100} < 3.2)$ 的近似值。

**解**：$\bar{X} \sim N\left(3, \dfrac{4}{100}\right) = N(3, 0.04)$，$\sigma_{\bar{X}} = 0.2$。

$$P(2.8 < \bar{X} < 3.2) \approx \Phi(1) - \Phi(-1) = 2\Phi(1) - 1 = 2 \times 0.8413 - 1 = 0.6826$$

### 例题 15（均匀分布之和）

设 $X_1, X_2, \cdots$ 独立同分布，$X_i \sim U(-1, 1)$，求 $P\left(\sum_{i=1}^{48} X_i > 4\right)$ 的近似值。

**解**：$E(X_i) = 0$，$D(X_i) = \dfrac{(1-(-1))^2}{12} = \dfrac{1}{3}$。

$$E(S) = 0, \qquad D(S) = 48 \times \frac{1}{3} = 16$$

$$P(S > 4) \approx 1 - \Phi\left(\frac{4 - 0}{4}\right) = 1 - \Phi(1) = 1 - 0.8413 = 0.1587$$

## 5. 工具选择速查表

| 题目特征 | 用哪个工具 | 关键动作 |
| --- | --- | --- |
| 只给 $E$、$D$，要概率的上下界 | 切比雪夫不等式 | $P(|X-\mu| \ge \varepsilon) \le \dfrac{\sigma^2}{\varepsilon^2}$ |
| "证明 $\dfrac{1}{n}\sum g(X_i)$ 收敛" | 辛钦大数定律 | 求 $E[g(X_1)]$，直接套定理 |
| 频率估计概率的样本量 | 切比雪夫 + $p(1-p) \le \dfrac{1}{4}$ | 放大到与 $p$ 无关 |
| "二项分布 $B(n,p)$ 的区间概率" | 棣莫弗-拉普拉斯 CLT | 检查 $np \ge 5$、$n(1-p) \ge 5$；离散区间补 $\pm 0.5$ |
| "独立同分布和/均值的概率" | 列维-林德伯格 CLT | $\sum X_i \sim N(n\mu, n\sigma^2)$ 或 $\bar{X} \sim N(\mu, \sigma^2/n)$ |
| "证明依概率收敛的运算" | 依概率收敛定义 | 三角不等式 + 事件并 |

## 6. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 二项近似忘了检查 $np \ge 5$、$n(1-p) \ge 5$ | 前提遗漏 | 分布过偏时近似失真 | 先检查再近似；不满足改泊松近似 |
| 二项区间概率忘记 $\pm 0.5$ 修正 | 方法遗漏 | 离散连续台阶差 | $P(a \le X \le b) \approx P(a-0.5 \le Y \le b+0.5)$，$Y \sim N(np, npq)$ |
| 例题 11 中把 $n \le 36$ 写成 $n \ge 36$ | 方向错误 | 忽略"$n$ 大则波动大" | 先判断 $n$ 增大使目标概率增大还是减小，再定不等号方向 |
| 把"频率"与"次数"混用 | 单位错误 | 忘记除以 $n$ | 频率 $\dfrac{n_A}{n}$ 的方差是 $\dfrac{p(1-p)}{n}$，次数 $n_A$ 的方差是 $np(1-p)$ |
| 保险题里把收入当随机变量 | 建模错误 | 收入是确定常数 | 收入 $= 120000$ 是常数，只有赔付 $1000X$ 随机；亏本 = 确定值 < 随机值 |
| 用切比雪夫上界当精确概率 | 概念混淆 | 上界 ≠ 真值 | 切比雪夫给"至多/至少"；要精确值用 CLT 或分布函数 |

## 7. 实战练习

### 练习 1（切比雪夫）

设 $E(X) = 2$，$D(X) = 0.09$，估计 $P(1.4 < X < 2.6)$。

**提示**：区间半宽 0.6。

**参考答案要点**：$P \ge 1 - \dfrac{0.09}{0.36} = 0.75$。

### 练习 2（大数定律）

设 $X_1, \cdots, X_n$ 独立同分布，$X_i \sim U(0, 1)$，求 $\dfrac{1}{n}\sum_{i=1}^n X_i^k$（$k$ 为正整数）的依概率极限。

**提示**：$E(X^k) = \dfrac{1}{k+1}$。

**参考答案要点**：$\dfrac{1}{n}\sum X_i^k \xrightarrow{P} \dfrac{1}{k+1}$。

### 练习 3（CLT 二项近似）

某次考试通过率 0.4，随机抽查 300 名学生，求通过人数在 100 到 140 之间的概率近似值。

**提示**：$X \sim B(300, 0.4)$；$np = 120$，$\sqrt{np(1-p)} = \sqrt{72} \approx 8.485$；用连续性修正 $P(99.5 \le X \le 140.5)$。

**参考答案要点**：$P = \Phi\left(\dfrac{140.5-120}{8.485}\right) - \Phi\left(\dfrac{99.5-120}{8.485}\right) = \Phi(2.416) - \Phi(-2.416) \approx 0.9843$。

### 练习 4（CLT 样本量对比）

用中心极限定理重做例题 6（要求 $P\left(\left|\dfrac{n_A}{n} - p\right| < 0.01\right) \ge 0.95$，$p = 0.5$ 已知），比较与切比雪夫路线的样本量差异。

**提示**：$\dfrac{n_A}{n} \sim N\left(p, \dfrac{p(1-p)}{n}\right)$；$2\Phi\left(\dfrac{0.01}{\sqrt{p(1-p)/n}}\right) - 1 \ge 0.95$。

**参考答案要点**：$p = 0.5$ 时标准差 $\sqrt{\dfrac{0.25}{n}} = \dfrac{0.5}{\sqrt{n}}$；$\dfrac{0.01}{0.5/\sqrt{n}} \ge 1.96 \Rightarrow \sqrt{n} \ge 98 \Rightarrow n \ge 9604$——约为切比雪夫路线（50000）的 $\dfrac{1}{5}$，这就是"用分布信息换效率"。

### 练习 5（综合）

一商场每天客流量 $X_i$ 独立同分布，$E(X_i) = 1000$ 人，$D(X_i) = 40000$。求 30 天总客流量超过 32000 人的概率近似值。

**提示**：$S \sim N(30000, 30 \times 40000)$。

**参考答案要点**：$E(S) = 30000$，$\sigma_S = \sqrt{1200000} \approx 1095.4$；$P(S > 32000) \approx 1 - \Phi\left(\dfrac{2000}{1095.4}\right) = 1 - \Phi(1.826) \approx 0.0339$。

## 8. 一句话记忆

三大工具各司其职：切比雪夫只凭"期望+方差"划保守界限（$P(|X-\mu| \ge \varepsilon) \le \dfrac{\sigma^2}{\varepsilon^2}$），大数定律保证"平均收敛到期望"（$p(1-p) \le \dfrac{1}{4}$ 处理未知 $p$），中心极限定理把和/均值近似成正态并给出精确概率（记得检查 $np$ 条件与 $\pm 0.5$ 修正）。

## 参考文献

- 盛骤, 谢式千, 潘承毅. 概率论与数理统计（第六版）[M]. 高等教育出版社, 2026. 第五章"大数定律及中心极限定理"习题五. https://www.hep.com.cn/book/show/3b2dd87a-7531-4610-97e6-071eb302d813
- 《概率论与数理统计》第五章"大数定律与中心极限定理"备考指南（三大定律对比与 Python 仿真）. https://blog.csdn.net/2402_84764726/article/details/159855304
- Normal Approximation: Binomial Guide（$np \ge 5$ 条件与连续性修正）. https://statisticsfundamentals.com/normal-distribution/normal-approximation/

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
