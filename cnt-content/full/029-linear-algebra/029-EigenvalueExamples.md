---
order: 54
title: 特征值典型例题
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 用实际应用（马尔可夫链、人口迁移、斐波那契数列、振动、微分方程组）巩固特征值知识，涵盖计算题、对角化判定、正交对角化、抽象矩阵特征值等题型，含 0 基础类比、完整例题、常见错误对策与实战练习。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/矩阵对角化'
  - 'linear-algebra/实对称矩阵的对角化'
  - 'linear-algebra/二次型的标准形'
  - 'linear-algebra/二次型的规范形'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 0. 从一个生活场景说起：能"看见未来"的数学

一家手机厂商想知道：按现在的换机习惯，五年后自己的市场份额是多少？一座城市想知道：按现在的迁移率，城市和乡村人口比例最终会停在什么水平？物理系学生想知道：弹簧振子的振动频率由什么决定？

这些问题的共同结构是：**状态每步按同一规则更新**——$x_{k+1} = Ax_k$。连乘 $n$ 次，未来状态就是 $A^nx_0$。而 $A^n$ 一旦对角化就变得透明：$A^n = P\Lambda^nP^{-1}$，未来完全由**特征值的幂**控制。

这就是本篇的主题——"应用驱动"：把前面学过的特征值、对角化、实对称矩阵知识，投放到真实场景里。你会看到：

- 马尔可夫链中，特征值 1 决定**稳态**（长期趋势）；
- 斐波那契数列中，特征值 $(1 \pm \sqrt{5})/2$ 就是通项公式的底数；
- 振动问题中，特征值（的平方根）就是**固有频率**。

学完本篇，特征值不再是"抽象的 $\lambda$"，而是"能预测未来的常数"。

## 1. 应用一：离散动力系统与斐波那契数列（差分方程）

### 1.1 模型：$x_{k+1} = Ax_k$

若第 $k$ 步状态为 $x_k$，每步按 $x_{k+1} = Ax_k$ 更新，则：

$$x_k = A^kx_0$$

若 $A = P\Lambda P^{-1}$（$P$ 的列是特征向量 $v_1, \ldots, v_n$），把 $x_0$ 按特征向量展开 $x_0 = c_1v_1 + \cdots + c_nv_n$，则：

$$x_k = c_1\lambda_1^kv_1 + c_2\lambda_2^kv_2 + \cdots + c_n\lambda_n^kv_n$$

**长期行为一目了然**：$|\lambda_i| < 1$ 的分量衰减至零，$|\lambda_i| > 1$ 的分量爆炸增长，$|\lambda_i| = 1$ 的分量保持不变——这就是"特征值控制未来"的精确含义。

### 1.2 例1（斐波那契数列通项，同济教材经典衍生题）

斐波那契数列 $F_0 = 0$，$F_1 = 1$，$F_{n+2} = F_{n+1} + F_n$。求通项公式。

**第一步，化矩阵**。令 $x_k = \begin{pmatrix} F_{k+1} \\ F_k \end{pmatrix}$，则：

$$x_{k+1} = \begin{pmatrix} F_{k+2} \\ F_{k+1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} F_{k+1} \\ F_k \end{pmatrix} = A x_k, \quad A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}, \quad x_0 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

**第二步，对角化**。$|\lambda I - A| = \lambda^2 - \lambda - 1 = 0$，特征值：

$$\lambda_1 = \frac{1 + \sqrt{5}}{2}, \quad \lambda_2 = \frac{1 - \sqrt{5}}{2}$$

（注意：这就是"黄金比例" $\varphi$ 与 $-\varphi^{-1}$。）特征向量：$v_1 = (\lambda_1, 1)^T$，$v_2 = (\lambda_2, 1)^T$。

**第三步，展开初值**。$x_0 = c_1v_1 + c_2v_2$，解 $\begin{pmatrix} 1 \\ 0 \end{pmatrix} = c_1\begin{pmatrix} \lambda_1 \\ 1 \end{pmatrix} + c_2\begin{pmatrix} \lambda_2 \\ 1 \end{pmatrix}$，得 $c_1 = \dfrac{1}{\sqrt{5}}$，$c_2 = -\dfrac{1}{\sqrt{5}}$。

**第四步，读答案**。$x_k$ 的第二个分量就是 $F_k$：

$$F_k = \frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^k - \left(\frac{1-\sqrt{5}}{2}\right)^k\right]$$

**检验**：$k = 2$ 时 $F_2 = \frac{1}{\sqrt{5}}(\varphi^2 - (-\varphi^{-1})^2) = 1$，与定义一致。

**方法总结**：二阶线性递推 $\Rightarrow$ 化为一阶矩阵递推 $\Rightarrow$ 对角化 $\Rightarrow$ 通项公式。特征值 $\lambda_1 > 1$ 控制增长速度，$\lambda_2$ 模小于 1，贡献衰减。

## 2. 应用二：马尔可夫链与人口迁移（稳态分析）

### 2.1 马尔可夫矩阵的两条性质（MIT 18.06 标准表述）

一个**马尔可夫矩阵**（列随机矩阵）$A$ 满足：

1. 所有元素非负：$a_{ij} \geq 0$；
2. 每列元素之和为 1（列和为 1）。

直观含义：$a_{ij}$ 表示"从状态 $j$ 流向状态 $i$ 的比例"，列和为 1 保证总量守恒（总人数不变、总概率为 1）。

**两条关键结论**（由性质直接推出，不用解方程）：

- $1$ 一定是马尔可夫矩阵的特征值（因为 $\begin{pmatrix} 1 & \cdots & 1 \end{pmatrix}A = \begin{pmatrix} 1 & \cdots & 1 \end{pmatrix}$，转置后 $(A^T - I)\begin{pmatrix} 1 \\ \vdots \\ 1 \end{pmatrix} = 0$，故 $A^T$ 有特征值 1，$A$ 也有特征值 1）；
- 对正则马尔可夫矩阵（某次幂全为正），其余特征值的模都小于 1。

**稳态（steady state）**：反复迭代 $x_k = A^kx_0$，当其余特征值的幂衰减到零，只剩下特征值 1 的分量：

$$x_\infty = c_1v_1 \quad（v_1 \text{ 是特征值 1 的特征向量}）$$

即：**稳态 = 特征值 1 的特征向量方向（归一化）**，与初值 $x_0$ 无关。稳态满足 $Av = v$。

### 2.2 例2（两城市人口迁移）

某国居民只在城市 $C$ 与乡村 $R$ 之间迁移。每年：城市居民有 20% 迁往乡村，乡村居民有 30% 迁往城市。初始比例为城市 60%、乡村 40%。求长期（10 年后及稳态）的城市人口比例。

**第一步，建矩阵**。状态向量 $x_k = \begin{pmatrix} \text{城市占比} \\ \text{乡村占比} \end{pmatrix}$，迁移矩阵（列随机）：

$$A = \begin{pmatrix} 0.8 & 0.3 \\ 0.2 & 0.7 \end{pmatrix}$$

（第 1 列：城市居民 80% 留在城市、20% 去乡村；第 2 列：乡村居民 30% 去城市、70% 留乡村。每列和为 1。）

**第二步，求特征值**：

$$|\lambda I - A| = (\lambda - 0.8)(\lambda - 0.7) - 0.06 = \lambda^2 - 1.5\lambda + 0.5 = (\lambda - 1)(\lambda - 0.5)$$

特征值 $\lambda_1 = 1$（正是马尔可夫矩阵必有特征值），$\lambda_2 = 0.5$。

**第三步，求特征向量**：

$\lambda_1 = 1$：$(I - A)v_1 = 0$：$\begin{pmatrix} 0.2 & -0.3 \\ -0.2 & 0.3 \end{pmatrix}v_1 = 0 \Rightarrow 2x_1 = 3x_2$，取 $v_1 = (3, 2)^T$。

$\lambda_2 = 0.5$：$(0.5I - A)v_2 = 0$：$\begin{pmatrix} -0.3 & -0.3 \\ -0.2 & -0.2 \end{pmatrix}v_2 = 0 \Rightarrow x_1 + x_2 = 0$，取 $v_2 = (1, -1)^T$。

**第四步，展开初值并迭代**。$x_0 = \begin{pmatrix} 0.6 \\ 0.4 \end{pmatrix}$，设 $x_0 = c_1(3, 2)^T + c_2(1, -1)^T$，解得 $c_1 = 0.2$，$c_2 = 0$（恰好无 $\lambda_2$ 分量，但一般情况要保留）。

于是：

$$x_k = 0.2 \cdot 1^k \cdot (3, 2)^T + 0 \cdot (0.5)^k(1, -1)^T = (0.6, 0.4)^T$$

（本例初值恰好已在稳态，故比例不变。为看到"收敛"，把初值换成 $x_0 = (1, 0)^T$ 重算：$c_1 = 0.4$，$c_2 = -0.2$，得 $x_k = 0.4(3,2)^T - 0.2(0.5)^k(1,-1)^T$。10 年后：$0.4 \times 3 - 0.2 \times (0.5)^{10} \approx 1.1998$，城市占比约 60%。）**稳态**：$x_\infty = 0.4(3, 2)^T$ 归一化得城市 60%、乡村 40%。

**检验**：$Av_1 = (0.8 \times 3 + 0.3 \times 2, 0.2 \times 3 + 0.7 \times 2)^T = (3, 2)^T = v_1$，稳态方程 $Av = v$ 成立。

**工程结论**：无论初始城市人口比例如何，长期都会收敛到 60%（稳态由特征值 1 的特征向量唯一决定）。这正是马尔可夫链在人口学、市场占有率预测、PageRank 中的标准用法。

## 3. 应用三：振动与微分方程组（特征值 = 固有频率）

### 3.1 模型

弹簧-质量系统（两个质量块相连）的运动方程为 $\dfrac{d^2\boldsymbol{x}}{dt^2} = -K\boldsymbol{x}$。令 $\boldsymbol{y} = \dfrac{d\boldsymbol{x}}{dt}$ 可化为 $\dfrac{d}{dt}\begin{pmatrix} \boldsymbol{x} \\ \boldsymbol{y} \end{pmatrix} = \begin{pmatrix} O & I \\ -K & O \end{pmatrix}\begin{pmatrix} \boldsymbol{x} \\ \boldsymbol{y} \end{pmatrix}$。特征值的虚部（的绝对值）就是系统的**固有频率**——特征值进入物理学的入口。

### 3.2 例3（一阶微分方程组求解）

解微分方程组 $\begin{cases} \dot{x}_1 = 2x_1 + x_2 \\ \dot{x}_2 = x_1 + 2x_2 \end{cases}$。

**第一步，矩阵化**：$\dot{\boldsymbol{x}} = A\boldsymbol{x}$，$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$。

**第二步，对角化**：特征值 $1, 3$，特征向量 $(1, -1)^T, (1, 1)^T$，$A = P\Lambda P^{-1}$。

**第三步，利用 $e^{At}$**：解为 $\boldsymbol{x}(t) = e^{At}\boldsymbol{x}(0) = Pe^{\Lambda t}P^{-1}\boldsymbol{x}(0)$，其中 $e^{\Lambda t} = \begin{pmatrix} e^{t} & 0 \\ 0 & e^{3t} \end{pmatrix}$。

**第四步，写出显式解**：设初值 $(x_1(0), x_2(0)) = (c_1, c_2)$：

$$x_1(t) = \frac{c_1+c_2}{2}e^{3t} + \frac{c_1-c_2}{2}e^{t}, \quad x_2(t) = \frac{c_1+c_2}{2}e^{3t} - \frac{c_1-c_2}{2}e^{t}$$

**检验**：$t = 0$ 时还原初值；代入原方程验证 $\dot{x}_1 = 2x_1 + x_2$ 成立。特征值 $1, 3 > 0$ 说明系统不稳定（指数增长）——若特征值为纯虚数，则对应振荡（如弹簧系统）。

## 4. 应用四：抽象矩阵综合题（把"应用"收回到理论）

应用场景练熟了，再回到纯代数综合题——这些题考的正是前面所有工具的整合。

### 例4（幂等矩阵 + 秩）

设 $A^2 = A$（幂等矩阵），$r(A) = r$，求 $A$ 的特征值，并说明 $A$ 可对角化。

**解**：设 $A\boldsymbol{x} = \lambda\boldsymbol{x}$，由 $A^2 = A$ 得 $\lambda^2 = \lambda$，$\lambda = 0$ 或 $1$。

$\text{tr}(A) = $ 特征值之和 $= 1$ 的个数。又幂等矩阵满足 $\text{tr}(A) = r(A)$（可对角化，对角形中 1 的个数 = 秩），故 $A$ 有 $r$ 个特征值 $1$ 和 $n - r$ 个特征值 $0$。

幂等矩阵 $A^2 = A$ 必可对角化：对每个特征向量，$(A - \lambda I)\boldsymbol{x} = 0$ 的解空间维数恰等于代数重数（可由 $A$ 的最小多项式无重根或几何论证得到）。

### 例5（秩 1 矩阵的特征值）

设 $\boldsymbol{\alpha}, \boldsymbol{\beta}$ 为 $n$ 维非零列向量，$A = \boldsymbol{\alpha}\boldsymbol{\beta}^T$，$\boldsymbol{\beta}^T\boldsymbol{\alpha} = k$，求 $A$ 的特征值与特征向量，并讨论可对角化性。

**解**：$A\boldsymbol{\alpha} = \boldsymbol{\alpha}(\boldsymbol{\beta}^T\boldsymbol{\alpha}) = k\boldsymbol{\alpha}$，故 $k$ 是特征值，$\boldsymbol{\alpha}$ 是对应特征向量。

对任意满足 $\boldsymbol{\beta}^T\boldsymbol{x} = 0$ 的 $\boldsymbol{x}$：$A\boldsymbol{x} = \boldsymbol{\alpha}(\boldsymbol{\beta}^T\boldsymbol{x}) = 0$，故 $0$ 是特征值，特征子空间是 $\boldsymbol{\beta}^\perp$（维数 $n-1$，因为 $\boldsymbol{\beta} \neq 0$）。$0$ 的代数重数为 $n - 1$（$r(A) = 1$，行列式非零特征值只有 $k$）。

- 当 $k \neq 0$ 时：特征值 $k$（单）与 $0$（$n-1$ 重），几何重数 $= n - r(A) = n - 1 = $ 代数重数，$A$ 可对角化；
- 当 $k = 0$ 时：全部特征值为 0 但 $A \neq O$，几何重数 $n - 1 < n$，不可对角化（除非 $n = 1$）。

### 例6（正交矩阵的特征值存在性）

设 $A$ 为 $n$ 阶正交矩阵，证明：若 $|A| = 1$ 且 $n$ 为奇数，则 $1$ 是 $A$ 的特征值；若 $|A| = -1$，则 $-1$ 是 $A$ 的特征值。

**证明**：利用"凑 $AA^T$"技巧。

**$|A| = 1$，$n$ 为奇数**：

$$|A - I| = |A - AA^T| = |A(I - A^T)| = |A| \cdot |I - A^T| = |(I - A)^T| = |I - A| = (-1)^n|A - I| = -|A - I|$$

（$|I - A| = |-(A - I)| = (-1)^n|A - I|$，$n$ 为奇数。）故 $2|A - I| = 0$，$|A - I| = 0$，$1$ 是特征值。

**$|A| = -1$**：

$$|A + I| = |A + AA^T| = |A(I + A^T)| = |A| \cdot |I + A^T| = -|I + A| = -|A + I|$$

故 $|A + I| = 0$，$-1$ 是特征值。

**几何解读**：奇数维空间中的"保向旋转"（$|A| = 1$）必然绕某条轴旋转，轴上向量不动——这条轴就是特征值 1 的方向。

## 5. 典型计算题（速度训练）

### 例7

求 $A = \begin{pmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1 \end{pmatrix}$ 的特征值与特征向量。

**解**（利用"各行和相等"技巧）：每行和为 5，故 $\lambda = 5$ 是特征值，$(1, 1, 1)^T$ 是对应特征向量。由 $\text{tr}(A) = 3 = 5 + \lambda_2 + \lambda_3$ 得 $\lambda_2 + \lambda_3 = -2$；又 $|A| = (5-\lambda)(-1-\lambda)^2$ 展开得 $\lambda_2 = \lambda_3 = -1$。特征值 $5, -1, -1$。$\lambda = -1$ 的特征向量满足 $x_1 + x_2 + x_3 = 0$，取 $(-1, 1, 0)^T$ 与 $(-1, 0, 1)^T$。

### 例8

设 $A$ 为三阶实对称矩阵，$r(A) = 2$，$A^2 + 2A = O$，求 $A$ 的特征值及 $|A + I|$。

**解**：特征值满足 $\lambda^2 + 2\lambda = 0$，$\lambda = 0$ 或 $-2$。$A$ 实对称可对角化，$r(A) = 2$ 推非零特征值 2 个，故特征值 $0, -2, -2$。

$$|A + I| = (0 + 1)(-2 + 1)(-2 + 1) = 1$$

## 6. 常见错误与对策

| 常见错误 | 错误类型 | 原因 | 纠正方法 |
| --- | --- | --- | --- |
| 马尔可夫矩阵写成"行和为 1"（方向搞反） | 概念理解错误 | 混淆列随机与行随机 | 列和 = 1 保证总量守恒；$a_{ij}$ 是"从 $j$ 到 $i$"的比例 |
| 稳态直接取 $x_0$ 或忘记归一化特征向量 | 概念理解错误 | 把"稳态"当"初值" | 稳态 = 特征值 1 的特征向量（归一化为概率向量）；与初值无关 |
| 差分/递推题不会化成矩阵形式 | 方法缺失 | 没掌握 $x_{k+1} = Ax_k$ 建模 | 二阶递推 $F_{n+2} = aF_{n+1} + bF_n$ 用 $x_k = (F_{k+1}, F_k)^T$ 化矩阵 |
| 振动/微分方程题忘记 $e^{At} = Pe^{\Lambda t}P^{-1}$ | 公式遗忘 | 与 $A^k$ 形式混淆 | 矩阵指数与矩阵幂同构：$\Lambda$ 换 $e^{\lambda t}$ 即可 |
| 秩 1 矩阵 $A = \boldsymbol{\alpha}\boldsymbol{\beta}^T$ 的特征值只写 $k$ 和"0 重数算错" | 计算规范问题 | 忽略 $0$ 的代数重数为 $n-1$ | $r(A) = 1$ 推 $0$ 至少 $n-1$ 重；另一个特征值用 $\text{tr} = \boldsymbol{\beta}^T\boldsymbol{\alpha}$ 核对 |
| 马尔可夫链直接手算 $A^n$ 而非用特征值 | 方法低效 | 没体会到对角化的威力 | $A^n$ 用对角化；稳态只看特征值 1 的特征向量，其他特征值幂衰减 |
| 判断 $A$ 可对角化时漏掉 $k = 0$ 的秩 1 特例 | 条件遗漏 | 只看"特征值互异"不看重根 | 逐情形讨论：重根必须检查几何重数是否等于代数重数 |

## 7. 实战练习

### 练习1（基础：特征值计算）

求 $A = \begin{pmatrix} 3 & -1 \\ -1 & 3 \end{pmatrix}$ 的特征值与特征向量。

**提示**：$|\lambda I - A| = (\lambda - 3)^2 - 1$；特征向量用 $x_1 \pm x_2$ 关系写出。

**参考答案要点**：$\lambda_1 = 2$：$\boldsymbol{x}_1 = (1, 1)^T$；$\lambda_2 = 4$：$\boldsymbol{x}_2 = (1, -1)^T$。检验：$A(1,1)^T = (2, 2)^T$。

### 练习2（进阶：马尔可夫链稳态）

某市场有 A、B 两个品牌。每月：用 A 的顾客有 70% 继续用 A、30% 换 B；用 B 的顾客有 40% 换 A、60% 继续用 B。求长期市场份额。

**提示**：迁移矩阵 $M = \begin{pmatrix} 0.7 & 0.4 \\ 0.3 & 0.6 \end{pmatrix}$（列和为 1）；求特征值 1 的特征向量并归一化。

**参考答案要点**：特征值 $1$ 与 $0.3$。$(I - M)v = 0$：$\begin{pmatrix} 0.3 & -0.4 \\ -0.3 & 0.4 \end{pmatrix}v = 0 \Rightarrow 3x_1 = 4x_2$，$v = (4, 3)^T$，归一化得 A 占 $\frac{4}{7} \approx 57.1\%$，B 占 $\frac{3}{7} \approx 42.9\%$。

### 练习3（进阶：斐波那契式递推）

数列 $a_{n+2} = 2a_{n+1} + 3a_n$，$a_0 = 0$，$a_1 = 1$，求通项。

**提示**：$A = \begin{pmatrix} 2 & 3 \\ 1 & 0 \end{pmatrix}$，特征值解 $\lambda^2 - 2\lambda - 3 = 0$。

**参考答案要点**：$\lambda_1 = 3$，$\lambda_2 = -1$。$a_n = \frac{1}{4}(3^n - (-1)^n)$。检验：$a_2 = \frac{1}{4}(9 - 1) = 2 = 2 \times 1 + 3 \times 0$。

### 练习4（综合：抽象矩阵）

设 $A$ 为三阶矩阵，特征值为 $1, -1, 2$，求 $|A^2 + A - 2I|$。

**提示**：$A^2 + A - 2I$ 的特征值为 $\lambda^2 + \lambda - 2$；行列式 = 特征值之积。

**参考答案要点**：$\lambda = 1$：$0$；$\lambda = -1$：$-2$；$\lambda = 2$：$4$。$|A^2 + A - 2I| = 0 \times (-2) \times 4 = 0$。

### 练习5（挑战：振动频率）

某弹簧系统运动方程为 $\dfrac{d^2\boldsymbol{x}}{dt^2} = \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix}\boldsymbol{x}$。求系统的固有频率。

**提示**：令 $\boldsymbol{x} = \boldsymbol{v}e^{i\omega t}$，代入得 $-\omega^2\boldsymbol{v} = K\boldsymbol{v}$，即 $K$ 的特征值是 $-\omega^2$；先求 $K = \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix}$ 的特征值。

**参考答案要点**：$|\lambda I - K| = (\lambda + 2)^2 - 1 = (\lambda + 1)(\lambda + 3)$，$K$ 的特征值为 $-1, -3$。故 $\omega^2 = 1, 3$，固有频率 $\omega = 1, \sqrt{3}$（两个模态分别沿 $(1,1)^T$ 与 $(1,-1)^T$ 方向振动）。

## 8. 一句话记忆

**特征值就是"未来的系数"：$x_k = A^kx_0 = \sum c_i\lambda_i^kv_i$——$|\lambda_i| < 1$ 的衰减、$> 1$ 的增长、$= 1$ 的定住（马尔可夫稳态、斐波那契通项、振动频率全是它的化身）。**

## 参考链接与延伸阅读

- 同济大学数学科学学院《工程数学 线性代数（第七版）》，高等教育出版社，第 5 章 §2-§4（特征值计算、相似矩阵、对称矩阵对角化的权威例题）：https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=630508ea938b7cc2960ef14b
- MIT 18.06 Linear Algebra（Strang 第 24 讲马尔可夫矩阵：两性质、特征值 1、稳态特征向量；第 23 讲微分方程与 $e^{At}$）：https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- LibreTexts Linear Algebra（4.3.4 马尔可夫链：两状态模型的特征值与特征空间推导）：https://math.libretexts.org/Courses/University_of_California_Irvine/Linear_Algebra_(Math_3A_UCI)/04%3A_Vector_Spaces/4.03%3A_Examples_and_Applications/4.3.04%3A_Markov_Chains
- 动态系统与马尔可夫链讲义（离散动力系统 $x_{k+1} = Ax_k$、Perron-Frobenius 定理的应用）：https://wanghemath.github.io/Book-AdvancedLinearAlgebraAI/chapters/chapter-09-dynamical-systems-markov-chains-perron-frobenius.html
- 3Blue1Brown 线性代数的本质（特征向量在重复矩阵乘法中的意义）：https://www.3blue1brown.com/topics/linear-algebra

延伸阅读：矩阵对角化（本篇所有应用的工具）；特征值性质（迹、行列式与特征值的关系）；实对称矩阵的对角化（振动与 PCA 的数学基础）；二次型的标准形（特征值在几何与优化中的应用）。
