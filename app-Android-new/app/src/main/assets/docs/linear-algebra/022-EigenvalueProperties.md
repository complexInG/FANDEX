---
order: 220
title: 特征值性质
module: 'linear-algebra'
category: 数学
difficulty: intermediate
description: 特征值的基本性质，迹与特征值的关系，行列式与特征值的关系，矩阵运算的特征值，Cayley-Hamilton 定理，含 0 基础类比。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'linear-algebra/021-EigenvalueAndEigenvectorCalculation'
  - 'linear-algebra/023-MatrixDiagonalization'
  - 'linear-algebra/024-RealSymmetricMatrixDiagonalization'
prerequisites:
  - 'linear-algebra/001-DeterminantDefinitionAndGeometry'
---


## 0. 从一个生活场景说起：矩阵的"身份证"

每张身份证都印着姓名、身份证号等信息，但有些信息是"冗余校验"用的：比如身份证号的最后一位校验码，可以从前面 17 位算出来，用来快速发现抄写错误。**矩阵的特征值集合，就是矩阵的"身份证号"**——而本篇要讲的迹（主对角线和）与行列式，则是两个"校验信息"：它们不需要算特征值就能从矩阵本身直接读出，却精确等于特征值的"和"与"积"。

这两个校验关系威力极大：

- 已知特征值，立刻得到 $\text{tr}(A)$ 和 $|A|$（不用展开行列式）；
- 已知 $\text{tr}(A)$ 和 $|A|$，可以反查特征值的计算是否有错；
- 已知部分特征值，可以推理缺失特征值。

本篇是"性质驱动"篇：把特征值的各种性质系统整理，配上证明与例题。核心信条是：**凡是能不用解特征方程就推出的特征值信息，都不要去硬解方程**。

## 1. 特征值的基本性质

### 1.1 迹与特征值（和的关系）

$$\text{tr}(A) = \lambda_1 + \lambda_2 + \cdots + \lambda_n$$

矩阵的**迹**（主对角线元素之和）等于所有特征值之和（计入代数重数）。

**来源**：特征多项式 $f(\lambda) = \lambda^n - (\text{tr}A)\lambda^{n-1} + \cdots$ 中 $\lambda^{n-1}$ 的系数是 $-\text{tr}(A)$；而 $f(\lambda) = \prod(\lambda - \lambda_i)$ 中 $\lambda^{n-1}$ 的系数是 $-\sum\lambda_i$。对比系数即得。

### 1.2 行列式与特征值（积的关系）

$$|A| = \lambda_1 \lambda_2 \cdots \lambda_n$$

矩阵的行列式等于所有特征值之积（计入代数重数）。由 $f(\lambda)$ 的常数项 $(-1)^n|A| = (-1)^n\lambda_1\cdots\lambda_n$ 对比即得。

### 1.3 可逆性与特征值

$$A \text{ 可逆} \iff A \text{ 的特征值全不为零}$$

由 $|A| = \prod\lambda_i \neq 0$ 直接得到。这条性质非常常用：判断可逆不必求逆矩阵或算秩，看特征值有没有零即可。

### 1.4 特征值的个数

$n$ 阶方阵在复数域上恰好有 $n$ 个特征值（计入代数重数）。这是代数基本定理的推论：$n$ 次特征多项式在复数范围内恰有 $n$ 个根（计重数）。

## 2. 矩阵运算的特征值（"操作合法"清单）

### 2.1 基本运算表（同特征向量的"换汤不换药"）

设 $A\boldsymbol{x} = \lambda\boldsymbol{x}$（$\boldsymbol{x} \neq \mathbf{0}$），则下列运算的特征值与特征向量如下：

| 矩阵 | 特征值 | 特征向量 |
| --- | --- | --- |
| $kA$ | $k\lambda$ | $\boldsymbol{x}$ |
| $A + kI$ | $\lambda + k$ | $\boldsymbol{x}$ |
| $A^k$（$k \geq 1$） | $\lambda^k$ | $\boldsymbol{x}$ |
| $A^{-1}$（$A$ 可逆时） | $\lambda^{-1}$ | $\boldsymbol{x}$ |
| $A^*$（$\lambda \neq 0$ 时） | $\dfrac{|A|}{\lambda}$ | $\boldsymbol{x}$ |
| $f(A)$（$f$ 为多项式） | $f(\lambda)$ | $\boldsymbol{x}$ |
| $A^T$ | $\lambda$ | 不一定是 $\boldsymbol{x}$ |
| $P^{-1}AP$（相似变换） | $\lambda$ | $P^{-1}\boldsymbol{x}$ |

### 2.2 证明（选两条关键的）

**$A^k$**：由 $A\boldsymbol{x} = \lambda\boldsymbol{x}$ 两边左乘 $A$：$A^2\boldsymbol{x} = A(\lambda\boldsymbol{x}) = \lambda^2\boldsymbol{x}$，归纳得 $A^k\boldsymbol{x} = \lambda^k\boldsymbol{x}$。

**$A^{-1}$**：$A\boldsymbol{x} = \lambda\boldsymbol{x}$ 两边左乘 $A^{-1}$ 得 $\boldsymbol{x} = \lambda A^{-1}\boldsymbol{x}$，因 $\lambda \neq 0$（$A$ 可逆），$A^{-1}\boldsymbol{x} = \lambda^{-1}\boldsymbol{x}$。

**$A^*$**：由 $A^* = |A|A^{-1}$，$A^*\boldsymbol{x} = |A|A^{-1}\boldsymbol{x} = \dfrac{|A|}{\lambda}\boldsymbol{x}$。

**$f(A)$**：$f(A)\boldsymbol{x} = (a_mA^m + \cdots + a_1A + a_0I)\boldsymbol{x} = (a_m\lambda^m + \cdots + a_1\lambda + a_0)\boldsymbol{x} = f(\lambda)\boldsymbol{x}$。

### 2.3 两个"不成立"的坑（必考易错）

1. **$A + B$ 的特征值 ≠ $A$ 的特征值 + $B$ 的特征值**；
2. **$AB$ 的特征值 ≠ $A$ 的特征值 × $B$ 的特征值**。

这两条是"特征向量不同"导致的：$A$ 与 $B$ 的特征向量一般不同，无法对同一向量同时展开。只有在特殊情形（如 $AB = BA$ 且可同时对角化）才可能成立。**遇到此类题必须回到定义或整体处理，不可拆开**。

另外注意：$A^T$ 与 $A$ 有**相同**的特征值（特征多项式相同），但特征向量一般不同。

## 3. 特征值的估计（不用解方程也能知道大概位置）

### 3.1 Gershgorin 圆盘定理

$A = (a_{ij})_{n \times n}$ 的每个特征值都位于以下 $n$ 个圆盘之一中：

$$D_i = \{z \in \mathbb{C} \mid |z - a_{ii}| \leq R_i\}, \quad R_i = \sum_{j \neq i} |a_{ij}|$$

其中 $R_i$ 是第 $i$ 行去掉主对角元后的绝对值之和。这条定理在数值计算中用于快速定位特征值、判断稳定性（如控制系统极点位置）。

### 3.2 Rayleigh 商（实对称矩阵的特征值界）

对实对称矩阵 $A$，任意非零向量 $\boldsymbol{x}$ 满足：

$$\lambda_{\min} \leq \frac{\boldsymbol{x}^TA\boldsymbol{x}}{\boldsymbol{x}^T\boldsymbol{x}} \leq \lambda_{\max}$$

中间的比值称为 **Rayleigh 商**。它给出了特征值的上下界，也是机器学习中谱聚类、拉普拉斯特征映射的理论基础。

## 4. 特征多项式的性质

### 4.1 Cayley-Hamilton 定理（矩阵满足自己的特征方程）

设 $A$ 的特征多项式为 $f(\lambda) = |\lambda I - A|$，则：

$$f(A) = O$$

即"矩阵代入自己的特征多项式得到零矩阵"。这条定理的威力：**任何高次幂都能化成次数不超过 $n-1$ 的多项式**，大幅简化计算。

**示例**：设 $A^3 - 2A^2 + A - I = O$，求 $A^4$。

由 $f(A) = O$ 反解：$A^3 = 2A^2 - A + I$，两边左乘 $A$：

$$A^4 = A \cdot A^3 = A(2A^2 - A + I) = 2A^3 - A^2 + A$$

代入 $A^3$ 的表达式：

$$A^4 = 2(2A^2 - A + I) - A^2 + A = 3A^2 - A + 2I$$

这样 $A^4$ 就被化成了 $A^2, A, I$ 的组合。

### 4.2 特征多项式的系数（牛顿公式的雏形）

$$f(\lambda) = \lambda^n - c_1\lambda^{n-1} + c_2\lambda^{n-2} - \cdots + (-1)^n c_n$$

其中：

- $c_1 = \text{tr}(A) = \lambda_1 + \cdots + \lambda_n$；
- $c_2 = \sum_{i<j}\lambda_i\lambda_j$（所有二阶主子式之和）；
- $c_n = |A| = \lambda_1\lambda_2\cdots\lambda_n$。

一般地，$c_k$ 等于所有 $k$ 阶主子式之和。这条规律在"已知部分特征值推其余"的问题中非常有用。

### 例1（特征值综合计算）

设 $A$ 为三阶方阵，特征值为 $1, 2, 3$，求 $|A^* + 3A^{-1} - 2I|$。

**解**：$A$ 的特征值为 $1, 2, 3$，故 $|A| = 1 \times 2 \times 3 = 6$。

- $A^*$ 的特征值：$\dfrac{|A|}{\lambda}$，即 $6, 3, 2$；
- $A^{-1}$ 的特征值：$\dfrac{1}{\lambda}$，即 $1, \dfrac{1}{2}, \dfrac{1}{3}$；
- 于是 $A^* + 3A^{-1} - 2I$ 的特征值（三个矩阵共享同一特征向量，可叠加）：

$$6 + 3 \times 1 - 2 = 7, \quad 3 + 3 \times \frac{1}{2} - 2 = \frac{5}{2}, \quad 2 + 3 \times \frac{1}{3} - 2 = 1$$

由"行列式 = 特征值之积"：

$$|A^* + 3A^{-1} - 2I| = 7 \times \frac{5}{2} \times 1 = \frac{35}{2}$$

**方法总结**：题目要算"$f(A)$ 的行列式"，标准套路是——先求 $A$ 的特征值 $\lambda_i$，再算 $f(\lambda_i)$，最后连乘。全程不需要知道 $A$ 本身。

### 例2（正交矩阵的特征值）

设 $A$ 为 $n$ 阶实矩阵，$A^TA = I$，$|A| < 0$，求 $A$ 的一个特征值。

**解**：$A^TA = I$ 说明 $A$ 是正交矩阵，故 $|A| = \pm 1$；由 $|A| < 0$ 得 $|A| = -1$。

$|A| = \lambda_1\lambda_2\cdots\lambda_n = -1$。又正交矩阵的特征值满足 $|\lambda_i| = 1$，且实矩阵的复特征值成共轭对出现、共轭对乘积 $|\lambda|^2 = 1 > 0$。要让总乘积为负，必须存在奇数个实特征值取 $-1$。故 $A$ 至少有一个特征值为 $-1$。

### 例3（幂等矩阵的特征值）

设 $A^2 = A$（幂等矩阵），证明 $A$ 的特征值只能是 $0$ 或 $1$。

**证明**：设 $A\boldsymbol{x} = \lambda\boldsymbol{x}$，则 $A^2\boldsymbol{x} = A(\lambda\boldsymbol{x}) = \lambda^2\boldsymbol{x}$。又 $A^2 = A$，所以 $\lambda^2\boldsymbol{x} = \lambda\boldsymbol{x}$，$(\lambda^2 - \lambda)\boldsymbol{x} = 0$。因 $\boldsymbol{x} \neq \mathbf{0}$，$\lambda^2 - \lambda = 0$，$\lambda = 0$ 或 $1$。

**推广思路**：凡是给"矩阵方程"（如 $A^2 = A$、$A^2 = I$、$A^k = O$），一律先对特征向量作用，把矩阵方程变成特征值的代数方程——这是抽象矩阵特征值题的标准解法。

### 例4（判断对角化可能性的陷阱题）

设 $A$ 为 $n$ 阶方阵，$\boldsymbol{\alpha}$ 为 $n$ 维非零列向量，$A\boldsymbol{\alpha} = 2\boldsymbol{\alpha}$，$A^2\boldsymbol{\alpha} = 4\boldsymbol{\alpha}$，判断 $A$ 是否可对角化。

**解**：$A\boldsymbol{\alpha} = 2\boldsymbol{\alpha}$ 说明 $2$ 是特征值、$\boldsymbol{\alpha}$ 是特征向量。而 $A^2\boldsymbol{\alpha} = 4\boldsymbol{\alpha} = 2^2\boldsymbol{\alpha}$ 只是 $A\boldsymbol{\alpha} = 2\boldsymbol{\alpha}$ 的**必然推论**（$A^2\boldsymbol{\alpha} = A(2\boldsymbol{\alpha}) = 2A\boldsymbol{\alpha} = 4\boldsymbol{\alpha}$），没有提供新信息。仅凭一个特征值和一条特征向量，**无法判断** $A$ 是否可对角化（还需要知道全部特征值的几何重数与代数重数）。这题提醒我们：不要被题干"信息轰炸"迷惑，先过滤冗余条件。

## 6. 常见错误与对策

| 常见错误 | 错误类型 | 原因 | 纠正方法 |
| --- | --- | --- | --- |
| 把 $A + B$ 的特征值当成"特征值相加" | 概念理解错误 | 忽略特征向量不同的前提 | 特征值运算表只对"同一矩阵的函数"成立；$A+B$ 需整体处理 |
| 把 $AB$ 的特征值当成"特征值相乘" | 概念理解错误 | 与 $A^k$ 的性质混淆 | $AB$ 与 $BA$ 才有相同特征值（可逆情形）；乘法不可拆 |
| 用 $\text{tr}$、$|A|$ 反推特征值时忽略重数 | 计算规范问题 | 把"恰好 n 个特征值（计重数）"忘记 | 重根要重复计数；$n$ 阶矩阵的特征值和/积对应 $n$ 个值（计重数） |
| $A^*$ 的特征值公式用错（忘记 $\lambda \neq 0$ 前提） | 条件遗漏 | 只记公式不记适用范围 | $A^*$ 公式 $\dfrac{|A|}{\lambda}$ 要求 $A$ 可逆（$\lambda \neq 0$）；不可逆时另行处理 |
| 已知 $A$ 不可逆就断言"特征值全是 0" | 逻辑错误 | 混淆"存在 0 特征值"与"全是 0" | $A$ 不可逆 $\iff$ 至少一个特征值为 0（$|A| = \prod\lambda_i = 0$） |
| 例 4 类题被冗余条件带偏 | 策略失误 | 没过滤重复信息 | 先问"哪个条件给了新信息"；推论性条件不要重复使用 |

## 8. 一句话记忆

**特征值的"校验码"：$\text{tr}(A)$ 是特征值之和，$|A|$ 是特征值之积；同一矩阵的函数（$kA$、$A^k$、$A^{-1}$、$A^*$、$f(A)$）特征值跟着函数变，但 $A+B$、$AB$ 不可拆；矩阵方程给特征值出"代数方程"，Cayley-Hamilton 让高次幂降维。**
