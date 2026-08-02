---
order: 25
title: 矩阵典型例题
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 矩阵运算、逆矩阵、秩、伴随矩阵、分块矩阵等典型例题集锦，按"考点案例"组织，涵盖计算题与证明题，附常见错误与实战练习。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/矩阵的秩'
  - 'linear-algebra/分块矩阵'
  - 'linear-algebra/高斯消元法'
  - 'linear-algebra/解的存在性判定'
prerequisites: []
---

## 0. 从"考前综合训练场"说起

学完矩阵的运算、逆矩阵、初等变换、秩与分块矩阵（007-011 篇）之后，你手里已经攒了一堆"工具"。但工具会用了不等于能解题——就像考驾照前，单练过起步、侧方停车、直角转弯，还需要在综合训练场把动作串起来。矩阵的典型例题就是这座"综合训练场"：**一道题里可能同时用到幂的规律、逆的求法、秩的不等式和分块技巧**。

本文按"案例"组织，每一类案例对应一组高频考点，先讲清"这类题考什么、用什么工具"，再给出完整例题与推导。读完你会得到一张矩阵题型的"战术地图"。

## 1. 考点全景图：矩阵知识树

先总览矩阵章节的题型地图（这也是同济版《线性代数》第 2 章与第 3 章习题的常见分布）：

| 案例类别 | 核心考点 | 常用工具 |
| --- | --- | --- |
| 矩阵运算与幂 | $A^n$ 的计算 | 拆分 $A = I + B$、$A = \boldsymbol{\alpha}\boldsymbol{\beta}^T$、分块对角 |
| 逆矩阵 | 可逆性证明、求逆 | $AB = I$、伴随矩阵、初等变换 |
| 矩阵的秩 | 秩的等式与不等式 | 秩的定义、Sylvester 不等式、$r(AB) \le \min(r(A), r(B))$ |
| 伴随矩阵 | 伴随的秩与行列式 | $AA^* = |A|I$、$|A^*| = |A|^{n-1}$ |
| 矩阵方程 | 解 $AX = B$ 等 | 先化简合并、再判可逆、左乘右乘逆 |
| 综合证明 | 可逆性 + 秩的混合题 | 配凑 $(A - I)(B - I) = I$ 等恒等式 |

下面逐类展开。

## 2. 案例一：矩阵运算与高次幂

### 例 1

设 $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$，求 $A^n$。

**分析**：直接连乘 $n$ 次太慢。观察 $A = I + B$，其中 $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$。因为 $B^2 = O$，二项式展开后只有两项非零。

**解**：$A^n = (I + B)^n = I + nB + \binom{n}{2}B^2 + \cdots = I + nB$（$B^2 = O$，更高次项全为零）：

$$A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$$

**思路提炼**：当 $A = I + N$ 且 $N$ 是幂零矩阵（某次幂为零）时，二项式定理自动截断，这是求高次幂的核心套路。

### 例 2

设 $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 1 \end{pmatrix}$，求 $A^n - 2A^{n-1}$（$n \geq 2$）。

**解**：先算 $A^2 = \begin{pmatrix} 2 & 0 & 2 \\ 0 & 4 & 0 \\ 2 & 0 & 2 \end{pmatrix} = 2A$。于是对任意 $n \ge 2$：

$$A^n = A^{n-2}A^2 = A^{n-2} \cdot 2A = 2A^{n-1}$$

所以 $A^n - 2A^{n-1} = O$。这里的关键是**先发现 $A^2 = 2A$ 这个"循环关系"**，把高次幂化归为低次幂。

### 例 3（外积结构的幂）

设 $\boldsymbol{\alpha} = (1, 2, 3)^T$，$\boldsymbol{\beta} = (1, 1, 1)^T$，$A = \boldsymbol{\alpha}\boldsymbol{\beta}^T$，求 $A^n$。

**解**：$A = \boldsymbol{\alpha}\boldsymbol{\beta}^T = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \\ 3 & 3 & 3 \end{pmatrix}$。利用矩阵乘法结合律：

$$A^2 = \boldsymbol{\alpha}\boldsymbol{\beta}^T\boldsymbol{\alpha}\boldsymbol{\beta}^T = \boldsymbol{\alpha}(\boldsymbol{\beta}^T\boldsymbol{\alpha})\boldsymbol{\beta}^T$$

而 $\boldsymbol{\beta}^T\boldsymbol{\alpha} = 1 + 2 + 3 = 6$ 是一个**数**，可以提到前面：

$$A^2 = 6\boldsymbol{\alpha}\boldsymbol{\beta}^T = 6A, \qquad A^n = 6^{n-1}A$$

**思路提炼**：$\boldsymbol{\alpha}\boldsymbol{\beta}^T$ 这种"列乘行"矩阵的幂，核心是抓中间那个内积数 $\boldsymbol{\beta}^T\boldsymbol{\alpha}$。

## 3. 案例二：逆矩阵

### 例 4

设 $A^3 = 2I$，证明 $B = A^2 - A + I$ 可逆，并求 $B^{-1}$。

**解**：可逆性的本质是"找逆元"，即构造 $C$ 使 $BC = I$。由 $A^3 = 2I$ 得 $A^3 + I = 3I$，左边因式分解：

$$(A + I)(A^2 - A + I) = 3I$$

所以 $B \cdot \dfrac{A + I}{3} = I$，故 $B$ 可逆且：

$$B^{-1} = \frac{A + I}{3}$$

**思路提炼**：见到"多项式等于常数乘单位阵"（如 $A^3 = 2I$），优先尝试**因式分解配凑**出目标矩阵的倍数等于 $I$。这是证明可逆最常用的代数技巧。

### 例 5

设 $A, B$ 为 $n$ 阶方阵，$A + B = AB$，证明 $A - I$ 可逆。

**解**：把条件改写成"乘积 = 单位阵"的形式：

$$AB - A - B = O \Rightarrow AB - A - B + I = I \Rightarrow (A - I)(B - I) = I$$

由逆矩阵的定义，$A - I$ 可逆且 $(A - I)^{-1} = B - I$。

**思路提炼**：条件是加法的等式，目标是乘法的等式，中间的桥梁是"加 $I$ 再因式分解"。记住恒等式：$AB - A - B + I = (A - I)(B - I)$。

## 4. 案例三：矩阵的秩

### 例 6

设 $A$ 为 $n$ 阶方阵，$A^2 = A$（幂等矩阵），证明 $r(A) + r(I - A) = n$。

**证明**：这类题用"秩的双向夹逼"。

- 一方面：$A(I - A) = A - A^2 = O$，由"$AB = O \Rightarrow r(A) + r(B) \le n$"，得 $r(A) + r(I - A) \le n$；
- 另一方面：$A + (I - A) = I$，由"$r(P + Q) \le r(P) + r(Q)$"取 $P = A, Q = I - A$，得 $n = r(I) \le r(A) + r(I - A)$。

两边夹住，故 $r(A) + r(I - A) = n$。

**思路提炼**："$AB = O$"与"$P + Q = I$"是秩等式的两个标准出发点，前者给出上界、后者给出下界。

### 例 7

设 $A$ 为 $m \times n$ 矩阵，$B$ 为 $n \times s$ 矩阵，$AB = O$，证明 $r(A) + r(B) \le n$。

**证明**：$AB = O$ 说明 $B$ 的每一列 $b_j$ 都满足 $Ab_j = 0$，即 $B$ 的列空间是 $A$ 的零空间 $N(A)$ 的子空间。于是：

$$r(B) = \dim(\mathrm{Col}(B)) \le \dim(N(A)) = n - r(A)$$

移项即得 $r(A) + r(B) \le n$。

**思路提炼**：$AB = O$ 的本质是"$B$ 的列落在 $A$ 的零空间里"，用维数语言一句话就证完。这个结论（又称 Sylvester 秩不等式的特例）在考研中出场率极高。

### 例 8

设 $A$ 为 $n$ 阶方阵（$n \geq 2$），$A^* \neq O$，若 $Ax = 0$ 有非零解，求 $r(A^*)$。

**解**：$Ax = 0$ 有非零解 $\Rightarrow |A| = 0 \Rightarrow r(A) \le n-1$。又 $A^* \neq O$ 说明 $A$ 至少存在一个 $n-1$ 阶非零子式，即 $r(A) \ge n-1$。故 $r(A) = n-1$。

由伴随矩阵秩的结论（同济版教材习题结论：$r(A) = n-1$ 时 $r(A^*) = 1$），得 $r(A^*) = 1$。

## 5. 案例四：伴随矩阵

### 例 9

设 $A$ 为三阶可逆矩阵，$|A| = 3$，求 $\left|2(A^*)^{-1}\right|$。

**解**：由 $(A^*)^{-1} = \dfrac{A}{|A|} = \dfrac{A}{3}$，再结合"数乘行列式"（$n$ 阶矩阵乘数 $k$，行列式乘 $k^n$）：

$$\left|2(A^*)^{-1}\right| = \left|\frac{2A}{3}\right| = \left(\frac{2}{3}\right)^3 |A| = \frac{8}{27} \times 3 = \frac{8}{9}$$

**易错提醒**：计算 $\left|\frac{2}{3}A\right|$ 时，系数要取 $3$ 次方（矩阵是三阶的），而不是直接乘 $\frac{2}{3}$。

### 例 10

设 $A$ 为 $n$ 阶方阵，$|A| = a \neq 0$，求 $\left|(A^*)^*\right|$。

**解**：先用公式 $|A^*| = |A|^{n-1} = a^{n-1}$，再用 $(A^*)^* = |A^*|(A^*)^{-1}$：

$$(A^*)^* = a^{n-1} \cdot \frac{A}{|A|} = a^{n-2}A$$

两边取行列式：

$$\left|(A^*)^*\right| = (a^{n-2})^n \cdot |A| = a^{n(n-2)} \cdot a = a^{n^2 - 2n + 1} = a^{(n-1)^2}$$

**思路提炼**：伴随矩阵的两条"元公式"是 $(A^*)^{-1} = \frac{A}{|A|}$ 与 $|A^*| = |A|^{n-1}$，绝大多数伴随题由它们推演。

## 6. 案例五：矩阵方程

### 例 11

设 $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 2 & 0 \\ -1 & 0 & 1 \end{pmatrix}$，$AX + I = A^2 + X$，求 $X$。

**解**：先合并同类项：$AX - X = A^2 - I$，即 $(A - I)X = (A - I)(A + I)$。注意不能想当然地消去 $A - I$，必须先判断其可逆性。

$$A - I = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{pmatrix}, \qquad |A - I| = 0$$

$A - I$ 不可逆，所以不能直接约去。但我们可以验证：$X = A + I$ 代入原方程确实成立（此时 $A^2 - I$ 的每一列都在 $A - I$ 的列空间中，方程有解且解不唯一）。这类题的正确姿势是：**能消就消，不能消就逐列解方程组或直接验证候选解**。

### 例 12

设 $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$，$B = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$，解矩阵方程 $AXB = C$，其中 $C = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$。

**解**：两边同时左乘 $A^{-1}$、右乘 $B^{-1}$，得 $X = A^{-1}CB^{-1}$。逐步计算：

$$A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}, \qquad B^{-1} = \frac{1}{-2}\begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix}$$

$$A^{-1}C = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} -2 & -2 \\ 7 & 8 \end{pmatrix}$$

$$X = \begin{pmatrix} -2 & -2 \\ 7 & 8 \end{pmatrix}\begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -2 & 3 \end{pmatrix}$$

**思路提炼**：解矩阵方程记住口诀："**左乘左除、右乘右除**"——$X$ 在 $A$ 的右边就右乘 $A^{-1}$，在 $A$ 的左边就左乘 $A^{-1}$，顺序绝不能搞反（$AX = B \Rightarrow X = A^{-1}B$，而不是 $BA^{-1}$）。

## 7. 案例六：综合证明题

### 例 13

设 $A$ 为 $n$ 阶实对称矩阵，$A^2 = O$，证明 $A = O$。

**证明**：实对称即 $A^T = A$，故 $A^2 = O$ 可写成 $A^TA = O$。取 $(A^TA)$ 的对角线元素：

$$(A^TA)_{jj} = \sum_{i=1}^{n} a_{ij}^2 = 0$$

每一项都是平方和，故 $a_{ij} = 0$ 对一切 $i, j$ 成立，即 $A = O$。

**思路提炼**："实对称 + 平方和 = 0 推出矩阵为零"是线性代数里的经典桥段，本质是内积 $\langle A_j, A_j\rangle = 0$。

### 例 14

设 $A$ 为 $n$ 阶方阵，$A^2 - 2A - 3I = O$，证明 $r(A + I) + r(A - 3I) = n$。

**证明**：$A^2 - 2A - 3I = (A + I)(A - 3I) = O$，由例 7 的结论，$r(A + I) + r(A - 3I) \le n$。

又 $(A + I) - (A - 3I) = 4I$，由 $r(P + Q) \le r(P) + r(Q)$ 反推：

$$n = r(4I) = r((A+I) - (A-3I)) \le r(A+I) + r(A-3I)$$

两边夹逼得 $r(A + I) + r(A - 3I) = n$。

### 例 15

设 $A, B, C$ 为 $n$ 阶方阵，$ABC = O$，证明 $r(A) + r(B) + r(C) \le 2n$。

**证明**：先对 $AB$ 与 $C$ 用例 7 的结论：$(AB)C = O$ 推出 $r(AB) + r(C) \le n$。

再用 Sylvester 不等式：$r(AB) \ge r(A) + r(B) - n$。两式合并：

$$r(A) + r(B) - n + r(C) \le n \Rightarrow r(A) + r(B) + r(C) \le 2n$$

**思路提炼**：三矩阵乘积为零，两两配对用"$r(PQ) + r(R) \le n$"，再用 Sylvester 不等式补回中间项，是标准的"降维打击"套路。

## 8. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 解 $AX = B$ 写成 $X = BA^{-1}$ | 左右顺序颠倒 | 矩阵乘法不交换，逆必须"贴"在 $X$ 所在的一侧 | 口诀：左乘左除、右乘右除 |
| $\left|\frac{2}{3}A\right| = \frac{2}{3}|A|$ | 数乘行列式算错 | 忘记 $n$ 阶矩阵数乘要取 $n$ 次方 | $\|kA\| = k^n\|A\|$ |
| 见到 $A^2 = 2A$ 直接说 $A = 2I$ 或 $A = O$ | 消去律误用 | 矩阵没有消去律，$A$ 可能不可逆 | 改写为 $A(A - 2I) = O$，用秩或方程组分析 |
| 判断可逆只看 $A \neq O$ | 概念混淆 | 非零矩阵未必可逆（如 $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$） | 用 $|A| \neq 0$ 或 $r(A) = n$ 判定 |
| 伴随题中 $(A^*)^* = A$ | 公式张冠李戴 | 该式仅当 $n = 2$ 时成立 | 用 $(A^*)^* = |A|^{n-2}A$（$n \ge 2$） |
| 幂的计算里 $(\boldsymbol{\alpha}\boldsymbol{\beta}^T)^n = \boldsymbol{\alpha}^n(\boldsymbol{\beta}^T)^n$ | 结合律误用 | 列向量乘行向量是矩阵，$\boldsymbol{\alpha}^n$ 无定义 | 抓内积：$(\boldsymbol{\alpha}\boldsymbol{\beta}^T)^n = (\boldsymbol{\beta}^T\boldsymbol{\alpha})^{n-1}\boldsymbol{\alpha}\boldsymbol{\beta}^T$ |

## 9. 实战练习

**练习 1（基础）**：设 $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$，求 $A^{100}$。

- **提示**：$A = I + 2B$，$B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，$B^2 = O$。
- **参考答案要点**：$A^{100} = I + 100 \cdot 2B = \begin{pmatrix} 1 & 200 \\ 0 & 1 \end{pmatrix}$。

**练习 2（进阶）**：设 $A$ 为 3 阶矩阵，$|A| = 2$，求 $|3A^*|$。

- **提示**：$|A^*| = |A|^{n-1}$，再配合数乘行列式。
- **参考答案要点**：$|3A^*| = 3^3 \cdot |A^*| = 27 \times 2^2 = 108$。

**练习 3（进阶）**：设 $A^2 + A + I = O$，证明 $A$ 可逆，并求 $A^{-1}$。

- **提示**：把条件改写成 $A(A + I) = -I$。
- **参考答案要点**：$A \cdot (-(A + I)) = I$，故 $A^{-1} = -A - I$。

**练习 4（综合）**：设 $A, B$ 为 $n$ 阶方阵，$AB = A + B$，证明 $AB = BA$。

- **提示**：由 $AB - A - B = O$ 配凑 $(A - I)(B - I) = I$，从而 $B - I = (A - I)^{-1}$，两边与 $(A - I)$ 可交换。
- **参考答案要点**：$(A - I)(B - I) = I$ 给出 $(B - I)(A - I) = I$，展开得 $BA = AB$。

**练习 5（综合）**：设 $A$ 为 $n$ 阶方阵，$A^2 = A$，$r(A) = r$。问 $Ax = 0$ 的解空间维数是多少？$(I - A)x = 0$ 呢？

- **提示**：直接用秩-零度定理：解空间维数 $= n - r(\cdot)$。
- **参考答案要点**：$\dim N(A) = n - r$；由例 6 知 $r(I - A) = n - r$，故 $\dim N(I - A) = r$。两者互为对方的列空间维数，体现幂等矩阵的分解结构。

## 10. 一句话记忆

> **矩阵题型的战术地图：求幂靠拆分（幂零块、外积、分块对角），证可逆靠配凑恒等式，算秩靠"乘积为零"与"和为 $I$"的双向夹逼，解矩阵方程牢记"左乘左除、右乘右除"。**

## 参考文献

- 同济大学数学科学学院. 工程数学 线性代数（第七版）[M]. 北京: 高等教育出版社, 2023. （第 2、3 章习题）https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=630508ea938b7cc2960ef14b
- 同济大学数学科学学院. 线性代数附册 学习辅导与习题全解（同济·第七版）[M]. 北京: 高等教育出版社, 2023. https://xuanshu.hep.com.cn/
- MIT 18.06 Linear Algebra（Strang）: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/

## 延伸阅读

- 矩阵运算、逆矩阵、初等变换与秩的概念，见 029-linear-algebra 模块 007-010 篇。
- 分块矩阵与分块求幂技巧，见 029-linear-algebra 模块 011 篇。
- 方程组的解与秩的关系，见 029-linear-algebra 模块 013-017 篇。
- 特征值与矩阵幂的结合应用（如 $A^n$ 的对角化求法），见 029-linear-algebra 模块 025-027 篇。
