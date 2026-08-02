---
order: 44
title: 矩与协方差矩阵
module: 'probability-statistics'
category: 'comp-sci'
difficulty: advanced
description: 原点矩、中心矩、混合矩的定义、偏度与峰度、协方差矩阵与相关矩阵、多元正态分布。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'probability-statistics/协方差'
  - 'probability-statistics/相关系数'
  - 'probability-statistics/数字特征典型例题'
  - 'probability-statistics/切比雪夫不等式'
prerequisites:
  - 'probability-statistics/样本空间与事件'
---

## 0. 从一个生活场景说起：一张表格装下一个班的"统计档案"

班主任想全面掌握一个班级的情况，不会只看平均分。他的"档案表"至少有三层信息：

1. **每一科的均分**（各科平均水平）——每个科目的期望；
2. **每一科的分差**（各科波动大小）——每个科目的方差；
3. **科目之间的联动**（语文好的学生数学是否也好）——两两协方差。

当变量从 1 个变成 $n$ 个，单独写"期望、方差、协方差"就太啰嗦了。数学家把第 1、2 层放进一个"均值向量"，把第 2、3 层放进一张 $n \times n$ 的表格——**协方差矩阵**。矩阵的每个位置都有明确含义：对角线上是各变量自己的方差，对角线外是两两协方差。

本文采用"**矩阵驱动**"的叙事结构：先讲"矩"（数字特征的统一框架：一阶矩是期望、二阶中心矩是方差），再用矩的语言引出偏度、峰度，最后把协方差推广成矩阵，并介绍多元正态分布。

## 1. 矩：数字特征的"统一框架"

"期望、方差、协方差"看似三个概念，其实都是"矩"的特例。矩把数字特征组织成一张整齐的表格，就像给随机变量建档案。

### 1.1 原点矩

设 $X$ 为随机变量，$k$ 为正整数，若 $E(X^k)$ 存在，则称

$$\mu_k = E(X^k)$$

为 $X$ 的 **$k$ 阶原点矩**。特别地，一阶原点矩 $\mu_1 = E(X)$ 就是数学期望。

### 1.2 中心矩

设 $X$ 为随机变量，$k$ 为正整数，若 $E[X - E(X)]^k$ 存在，则称

$$\nu_k = E\left[X - E(X)\right]^k$$

为 $X$ 的 **$k$ 阶中心矩**。特别地：

- 一阶中心矩 $\nu_1 = 0$（偏差的期望恒为 0）；
- 二阶中心矩 $\nu_2 = D(X)$（方差就是二阶中心矩）。

### 1.3 原点矩与中心矩的换算

由二项展开：

$$\nu_k = E[X - E(X)]^k = \sum_{j=0}^{k} \binom{k}{j} (-1)^{k-j} \mu_j \mu_1^{k-j}$$

常用结果（记 $\mu = \mu_1$）：

$$\nu_2 = \mu_2 - \mu^2 = E(X^2) - [E(X)]^2 = D(X)$$

$$\nu_3 = \mu_3 - 3\mu_2\mu + 2\mu^3$$

$$\nu_4 = \mu_4 - 4\mu_3\mu + 6\mu_2\mu^2 - 3\mu^4$$

### 1.4 混合矩

设 $X$、$Y$ 为随机变量，$k, l$ 为非负整数，若 $E(X^k Y^l)$ 存在，则称 $\mu_{k,l} = E(X^k Y^l)$ 为 $X$ 与 $Y$ 的 **$k + l$ 阶混合原点矩**；称

$$\nu_{k,l} = E[X - E(X)]^k [Y - E(Y)]^l$$

为**混合中心矩**。特别地，$\nu_{1,1} = \text{Cov}(X, Y)$——协方差就是 $(1,1)$ 阶混合中心矩。

> 档案观：原点矩记录"取值本身"的分布信息，中心矩记录"偏离均值"的分布信息，混合矩记录"跨变量联动"的信息——三者合起来构成完整的数字特征体系。

## 2. 偏度与峰度：分布"形状"的档案

期望和方差只刻画位置与散布，无法区分"左偏还是右偏"、"尖峰还是扁平"。偏度与峰度用三阶、四阶中心矩补上这一课。

### 2.1 偏度

$$\gamma_1 = \frac{\nu_3}{\nu_2^{3/2}} = \frac{E[X - E(X)]^3}{[D(X)]^{3/2}}$$

偏度度量分布的**不对称性**：

- $\gamma_1 > 0$：右偏（正偏），右侧尾部较长；
- $\gamma_1 < 0$：左偏（负偏），左侧尾部较长；
- $\gamma_1 = 0$：对称分布（正态分布偏度为 0）。

直觉：三阶中心矩对"大偏差"非常敏感，若右侧偏离均值更远更频繁，立方后正贡献压过负贡献，偏度为正。

### 2.2 峰度

$$\gamma_2 = \frac{\nu_4}{\nu_2^2} - 3 = \frac{E[X - E(X)]^4}{[D(X)]^2} - 3$$

峰度度量分布的**尖峰程度**（以正态分布为基准，正态的四阶中心矩 $\nu_4 = 3\sigma^4$，故 $\gamma_2 = 0$）：

- $\gamma_2 > 0$：尖峰分布（比正态更尖、尾部更厚，如 $t$ 分布）；
- $\gamma_2 < 0$：平坦分布（比正态更平、尾部更薄，如均匀分布）；
- $\gamma_2 = 0$：与正态相同。

### 2.3 例题 1（用矩算偏度）

设 $X \sim B(1, p)$（$p = \dfrac{1}{2}$），计算偏度。

**解**：$X$ 取 0、1 各 $\dfrac{1}{2}$。$E(X) = \dfrac{1}{2}$。

$$\nu_3 = E[X - E(X)]^3 = \left(0 - \frac{1}{2}\right)^3 \cdot \frac{1}{2} + \left(1 - \frac{1}{2}\right)^3 \cdot \frac{1}{2} = -\frac{1}{16} + \frac{1}{16} = 0$$

$$\gamma_1 = 0$$

分布关于 $\dfrac{1}{2}$ 对称，偏度为 0，与直觉一致。

## 3. 协方差矩阵：把联动装进一张表

### 3.1 定义

设 $n$ 维随机向量 $\mathbf{X} = (X_1, X_2, \cdots, X_n)^T$，令

$$c_{ij} = \text{Cov}(X_i, X_j) = E[X_i - E(X_i)][X_j - E(X_j)], \qquad i, j = 1, \cdots, n$$

则矩阵

$$\mathbf{C} = (c_{ij})_{n \times n} = \begin{pmatrix} c_{11} & c_{12} & \cdots & c_{1n} \\ c_{21} & c_{22} & \cdots & c_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ c_{n1} & c_{n2} & \cdots & c_{nn} \end{pmatrix}$$

称为 $\mathbf{X}$ 的**协方差矩阵**。

读法：对角线 $c_{ii} = D(X_i)$ 是各变量的方差；非对角线 $c_{ij}$ 是 $X_i$ 与 $X_j$ 的协方差。**整张表对称**：$c_{ij} = c_{ji}$。

### 3.2 紧凑写法

令均值向量 $\boldsymbol{\mu} = E(\mathbf{X}) = (E(X_1), \cdots, E(X_n))^T$，则

$$\mathbf{C} = E\left[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T\right]$$

注意 $(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T$ 是 $n \times n$ 外积矩阵，逐元素取期望即得 $\mathbf{C}$。

### 3.3 例题 2（二元协方差矩阵）

设 $D(X) = 4$，$D(Y) = 9$，$\text{Cov}(X, Y) = -3$，写出 $(X, Y)$ 的协方差矩阵。

**解**：

$$\mathbf{C} = \begin{pmatrix} D(X) & \text{Cov}(X, Y) \\ \text{Cov}(Y, X) & D(Y) \end{pmatrix} = \begin{pmatrix} 4 & -3 \\ -3 & 9 \end{pmatrix}$$

## 4. 协方差矩阵的性质

1. **对称性**：$\mathbf{C}^T = \mathbf{C}$（因为 $c_{ij} = c_{ji}$）；
2. **半正定性**：对任意 $n$ 维向量 $\mathbf{a}$，$\mathbf{a}^T \mathbf{C} \mathbf{a} \geq 0$。

**证明**：

$$\mathbf{a}^T \mathbf{C} \mathbf{a} = \mathbf{a}^T E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T] \mathbf{a} = E\left[\mathbf{a}^T(\mathbf{X} - \boldsymbol{\mu})\right]^2 \geq 0$$

中间是"某个随机变量的平方"，期望非负。半正定性是协方差矩阵最重要的结构性质，它保证了二次型 $\mathbf{a}^T\mathbf{C}\mathbf{a} \geq 0$（即组合方差非负）。

3. **对角线**：$c_{ii} = D(X_i) \geq 0$；
4. **线性变换**：若 $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$（$\mathbf{A}$ 为矩阵，$\mathbf{b}$ 为向量），则

$$\mathbf{C}_Y = \mathbf{A} \mathbf{C}_X \mathbf{A}^T$$

这条公式是"方差 $D(aX) = a^2D(X)$"的矩阵版：系数从平方变成"左乘 $\mathbf{A}$ 右乘 $\mathbf{A}^T$"。

### 例题 3（线性变换验证）

已知 $\mathbf{C}_X = \begin{pmatrix} 4 & -3 \\ -3 & 9 \end{pmatrix}$，$\mathbf{Y} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}\mathbf{X}$，求 $\mathbf{C}_Y$。

**解**：

$$\mathbf{C}_Y = \mathbf{A}\mathbf{C}_X\mathbf{A}^T = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 4 & -3 \\ -3 & 9 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 8 & -6 \\ -9 & 27 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 16 & -18 \\ -18 & 81 \end{pmatrix}$$

验证：$D(2X_1) = 4 \times 4 = 16$，$D(3X_2) = 9 \times 9 = 81$，$\text{Cov}(2X_1, 3X_2) = 6 \times (-3) = -18$，全部吻合。

## 5. 相关矩阵：标准化后的协方差矩阵

把协方差矩阵"标准化"（除以各自标准差的乘积），得到**相关矩阵**：

$$\mathbf{R} = (\rho_{ij})_{n \times n}, \qquad \rho_{ij} = \frac{c_{ij}}{\sqrt{c_{ii} c_{jj}}}$$

矩阵写法：

$$\mathbf{R} = \mathbf{D}^{-1/2} \mathbf{C} \mathbf{D}^{-1/2}, \qquad \mathbf{D} = \text{diag}(c_{11}, c_{22}, \cdots, c_{nn})$$

相关矩阵的对角线全为 1，非对角线是两两相关系数，取值在 $[-1, 1]$。相比协方差矩阵，相关矩阵无量纲，适合横向比较不同尺度的变量（例如"身高-体重-肺活量"三个不同单位的指标）。

## 6. 多元正态分布

### 6.1 定义

设 $\mathbf{X} = (X_1, \cdots, X_n)^T$ 服从 $n$ 维正态分布 $\mathbf{X} \sim N_n(\boldsymbol{\mu}, \boldsymbol{\Sigma})$，其密度为

$$f(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\boldsymbol{\Sigma}|^{1/2}} \exp\left\{-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right\}$$

其中 $\boldsymbol{\mu}$ 为均值向量，$\boldsymbol{\Sigma}$ 为协方差矩阵（正定，故 $|\boldsymbol{\Sigma}| > 0$）。

### 6.2 四大性质

1. **边缘分布仍是正态**：$\mathbf{X}$ 的任意子向量的边缘分布仍为正态；
2. **线性变换封闭**：$\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b} \sim N(\mathbf{A}\boldsymbol{\mu} + \mathbf{b},\ \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^T)$；
3. **独立与不相关等价**：$X_i$ 与 $X_j$ 独立 $\iff$ $\text{Cov}(X_i, X_j) = 0$——正态分布的特权；
4. **条件分布仍是正态**：给定部分分量的条件下，其余分量的条件分布仍为正态（这是高斯过程、卡尔曼滤波的数学根基）。

### 6.3 例题 4（二元正态）

二元正态分布的参数为

$$\boldsymbol{\mu} = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} \sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}$$

求行列式 $|\boldsymbol{\Sigma}|$ 与 $\rho$ 的解释。

**解**：

$$|\boldsymbol{\Sigma}| = \sigma_1^2\sigma_2^2 - \rho^2\sigma_1^2\sigma_2^2 = \sigma_1^2\sigma_2^2(1 - \rho^2)$$

由于 $\boldsymbol{\Sigma}$ 正定，$1 - \rho^2 > 0$，即 $|\rho| < 1$——从矩阵正定性再一次看到相关系数的有界性。$\rho$ 就是 $X_1$ 与 $X_2$ 的相关系数，控制椭圆等高线的"倾斜程度"。

## 7. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 把协方差矩阵对角线写成 $E(X_i^2)$ | 公式误用 | 忘记对角线是方差而非二阶原点矩 | 对角线 $c_{ii} = D(X_i) = E(X_i^2) - [E(X_i)]^2$ |
| 认为协方差矩阵一定可逆 | 概念错误 | 混淆"对称"与"正定" | 协方差矩阵对称半正定；只有正定时才可逆（$|\boldsymbol{\Sigma}| > 0$） |
| 线性变换直接写 $\mathbf{C}_Y = \mathbf{A}^2\mathbf{C}_X$ | 公式误用 | 把一维公式平方照搬 | 矩阵公式是 $\mathbf{C}_Y = \mathbf{A}\mathbf{C}_X\mathbf{A}^T$（左乘 $\mathbf{A}$、右乘转置） |
| 混用偏度与峰度符号含义 | 概念混淆 | 记不清正负对应的形状 | 偏度看左右尾巴长短（对称为 0）；峰度看尖平（正态为基准 0，$t$ 分布为正） |
| 忘记 $\nu_1 = 0$ 与 $\nu_2 = D(X)$ | 概念错误 | 矩的编号与含义对不上 | 中心矩从"偏离均值"出发：$\nu_1 = 0$ 恒成立，$\nu_2$ 就是方差 |
| 认为一般分布也满足"不相关即独立" | 以偏概全 | 把正态性质外推 | 该性质只对（多元）正态分布成立；其他分布用 $Y = X^2$ 类反例 |

## 8. 实战练习

### 练习 1（矩的计算）

设 $X \sim U(0, 1)$，求一阶、二阶、三阶原点矩。

**提示**：$E(X^k) = \int_0^1 x^k dx$。

**参考答案要点**：$\mu_1 = \dfrac{1}{2}$，$\mu_2 = \dfrac{1}{3}$，$\mu_3 = \dfrac{1}{4}$。

### 练习 2（偏度计算）

设 $X$ 的分布律为 $P(X=-1)=0.5$，$P(X=1)=0.5$，求偏度 $\gamma_1$。

**提示**：分布对称。

**参考答案要点**：$E(X)=0$，$\nu_3 = (-1)^3 \times 0.5 + 1^3 \times 0.5 = 0$，$\gamma_1 = 0$。

### 练习 3（协方差矩阵）

设 $D(X_1) = 1$，$D(X_2) = 4$，$D(X_3) = 9$，且 $\text{Cov}(X_i, X_j) = 0$（$i \neq j$），写出协方差矩阵。

**提示**：独立（不相关）时非对角线为 0。

**参考答案要点**：$\mathbf{C} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 9 \end{pmatrix}$（对角矩阵）。

### 练习 4（线性变换）

设 $\mathbf{C}_X = \begin{pmatrix} 1 & 0.5 \\ 0.5 & 2 \end{pmatrix}$，$\mathbf{Y} = \begin{pmatrix} 2X_1 + X_2 \\ X_1 - X_2 \end{pmatrix}$，求 $\mathbf{C}_Y$。

**提示**：$\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$，用 $\mathbf{C}_Y = \mathbf{A}\mathbf{C}_X\mathbf{A}^T$。

**参考答案要点**：$\mathbf{A}\mathbf{C}_X = \begin{pmatrix} 2.5 & 3 \\ 0.5 & -1.5 \end{pmatrix}$，$\mathbf{C}_Y = \mathbf{A}\mathbf{C}_X\mathbf{A}^T = \begin{pmatrix} 2.5 & 3 \\ 0.5 & -1.5 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 8 & -0.5 \\ -0.5 & 2 \end{pmatrix}$。

### 练习 5（概念辨析）

判断：（1）协方差矩阵一定是对称矩阵；（2）$\nu_4/\nu_2^2 = 3$ 是正态分布的标志；（3）任意分布中"不相关 $\iff$ 独立"。

**提示**：对照性质逐条检查。

**参考答案要点**：（1）对，$c_{ij} = c_{ji}$；（2）对，这正是峰度 $\gamma_2 = 0$ 的定义来源；（3）错，仅多元正态分布成立。

## 9. 一句话记忆

矩是数字特征的"档案表"（$\mu_1$ 期望、$\nu_2$ 方差、$\nu_{1,1}$ 协方差），偏度峰度看形状；协方差矩阵 $\mathbf{C} = E[(\mathbf{X}-\boldsymbol{\mu})(\mathbf{X}-\boldsymbol{\mu})^T]$ 对称半正定，对角线方差、非对角协方差，线性变换满足 $\mathbf{C}_Y = \mathbf{A}\mathbf{C}_X\mathbf{A}^T$。

## 参考文献

- 盛骤, 谢式千, 潘承毅. 概率论与数理统计（第六版）[M]. 高等教育出版社, 2026. 第四章"随机变量的数字特征"§4 协方差矩阵与多元正态分布、§5 其他数字特征. https://www.hep.com.cn/book/show/3b2dd87a-7531-4610-97e6-071eb302d813
- 相关系数、矩与协方差矩阵讲义. http://wulisu.cn/pdf/2026/Lec-14-slides.pdf
- 数字特征讲义（期望、方差、协方差、相关系数、原点矩与中心矩、偏度峰度）. https://blog.csdn.net/apr15/article/details/105748887

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
