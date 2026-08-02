---
order: 230
title: 矩阵对角化
module: 'linear-algebra'
category: 数学
difficulty: intermediate
description: 相似矩阵的定义与性质，矩阵可对角化的条件与判别，对角化的完整步骤（P⁻¹AP=Λ）与应用（矩阵幂、矩阵多项式、微分方程组），含 0 基础类比。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/025-EigenvalueAndEigenvectorCalculation'
  - 'linear-algebra/026-EigenvalueProperties'
  - 'linear-algebra/028-RealSymmetricMatrixDiagonalization'
prerequisites:
  - 'linear-algebra/001-DeterminantDefinitionAndGeometry'
---


## 0. 从一个生活场景说起：换个坐标系，复杂问题变简单

拍一张摆在斜桌上的圆形披萨，照片里它是个"椭圆"——透视把圆压扁了。但如果把相机转到正上方（换个观察坐标系），它又变回正圆。**同一个物体，在不同坐标系下"长相"差别很大，选对坐标系能让它简单得惊人**。

矩阵对角化做的正是这件事：$A$ 是一个复杂的线性变换（像"斜着看"），我们找到一个合适的坐标系（由特征向量张成），在这个坐标系里 $A$ 只做"沿各坐标轴分别伸缩"——也就是一个**对角矩阵**。对角矩阵的好处一目了然：求幂、求指数、解方程组都变成逐分量的标量运算。

本篇是"过程驱动"篇，完整走一遍对角化流程：

1. 什么矩阵能对角化？（判别条件）
2. 怎么把 $P$ 和 $\Lambda$ 找出来？（四步流程）
3. 对角化能干什么？（三大应用）

## 1. 相似矩阵：同一个变换的两张"证件照"

### 1.1 定义

设 $A, B$ 为 $n$ 阶方阵，若存在可逆矩阵 $P$，使得：

$$B = P^{-1}AP$$

则称 $A$ 与 $B$ **相似**，记作 $A \sim B$。

几何理解：$A$ 和 $B$ 描述的是**同一个线性变换在两个不同基下的矩阵**。$P$ 的列就是"新旧基之间的过渡矩阵"——这正好接上了 021 篇的坐标变换：$x_{\text{新}} = P^{-1}x_{\text{旧}}$。

### 1.2 相似关系的三条基本性质

1. **自反性**：$A \sim A$（取 $P = I$）；
2. **对称性**：$A \sim B \Rightarrow B \sim A$（取 $P^{-1}$）；
3. **传递性**：$A \sim B$，$B \sim C \Rightarrow A \sim C$。

### 1.3 相似矩阵的共同性质（"证件照"共享的信息）

若 $A \sim B$，则：

1. $|A| = |B|$；
2. $\text{tr}(A) = \text{tr}(B)$；
3. $r(A) = r(B)$；
4. $A$ 和 $B$ 有相同的特征值（含重数）；
5. 特征多项式相同：$|A - \lambda I| = |B - \lambda I|$；
6. $A$ 可逆 $\iff$ $B$ 可逆；
7. $A^k \sim B^k$；$f(A) \sim f(B)$（$f$ 为多项式）。

**重要提醒**：这些性质都是相似的**必要条件**，**不是充分条件**——两个矩阵特征值相同，不一定相似。

**反例**：$A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$，$B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$。两者特征值都是 $1, 1$，但 $A = I$ 与任何矩阵相似当且仅当它就是 $I$，故 $A \not\sim B$（$B$ 连特征向量都配不齐，更不可能与 $I$ 相似）。

## 2. 矩阵可对角化的条件

### 2.1 定义

若 $A$ 相似于对角矩阵，即存在可逆矩阵 $P$ 使得 $P^{-1}AP = \Lambda$（$\Lambda$ 为对角矩阵），则称 $A$ **可对角化**。

### 2.2 可对角化的等价条件（三条判定）

以下条件等价：

1. $A$ 可对角化；
2. $A$ 有 $n$ 个线性无关的特征向量；
3. 每个特征值的几何重数等于代数重数（$m_g(\lambda_i) = m_a(\lambda_i)$，对所有 $i$）。

直觉理解：对角化就是"把 $n$ 个特征向量拿来当坐标轴"。坐标轴必须线性无关（$P$ 可逆），所以需要 $n$ 个无关特征向量；重根如果"配不齐"（几何重数 < 代数重数），就凑不齐 $n$ 个。

### 2.3 充分条件（免检通道）

1. $A$ 有 $n$ 个**互不相同**的特征值 $\Rightarrow$ $A$ 可对角化（由"不同特征值特征向量无关"+ 个数恰好 $n$ 得证）；
2. $A$ 为实对称矩阵 $\Rightarrow$ $A$ 可对角化（且可正交对角化，见 028 篇）。

### 2.4 不可对角化的典型

若某个特征值的几何重数小于代数重数，则 $A$ 不可对角化。

**示例**：$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$。特征值 $\lambda = 1$（二重），$A - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，$r(A - I) = 1$，几何重数 $= 2 - 1 = 1 < 2$。特征向量只有 $k(1, 0)^T$ 一个方向，配不齐两个无关特征向量，$A$ 不可对角化。

## 3. 对角化的步骤（四步流程）

### 3.1 步骤

1. **求特征值**：解 $|\lambda I - A| = 0$，得 $\lambda_1, \ldots, \lambda_n$（计重数）；
2. **求特征向量**：对每个 $\lambda_i$ 解 $(\lambda_i I - A)\boldsymbol{x} = 0$，取基础解系；
3. **判配齐**：检查无关特征向量总数是否达到 $n$（即每个重根的几何重数 = 代数重数）；不满足则停止（不可对角化）；
4. **拼装**：以 $n$ 个特征向量为列构造 $P$，对应特征值按列序排成对角矩阵 $\Lambda$，则：

$$P^{-1}AP = \Lambda$$

**对应关系**：$P$ 的第 $i$ 列是 $\boldsymbol{x}_i$，则 $\Lambda$ 的第 $i$ 个对角元是 $\boldsymbol{x}_i$ 对应的特征值 $\lambda_i$。**顺序必须一一对应**——这是最易错的一步。

### 3.2 完整示例（同济教材经典题）

将 $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}$ 对角化。

**步骤1**：特征多项式（见 025 篇 3.3）：

$$|\lambda I - A| = \lambda^3 - 6\lambda^2 + 11\lambda - 6 = (\lambda - 1)(\lambda - 2)(\lambda - 3)$$

特征值 $\lambda_1 = 1$，$\lambda_2 = 2$，$\lambda_3 = 3$（互异，必可对角化）。

**步骤2**：逐个求特征向量。

$\lambda_1 = 1$：$(I - A)\boldsymbol{x} = 0$，行变换：

$$\begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ -6 & 11 & -5 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}$$

得 $\boldsymbol{x}_1 = (1, 1, 1)^T$。

$\lambda_2 = 2$：$(2I - A)\boldsymbol{x} = 0$：

$$\begin{pmatrix} 2 & -1 & 0 \\ 0 & 2 & -1 \\ -6 & 11 & -4 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & -1/4 \\ 0 & 1 & -1/2 \\ 0 & 0 & 0 \end{pmatrix}$$

得 $\boldsymbol{x}_2 = (1, 2, 4)^T$。

$\lambda_3 = 3$：$(3I - A)\boldsymbol{x} = 0$：

$$\begin{pmatrix} 3 & -1 & 0 \\ 0 & 3 & -1 \\ -6 & 11 & -3 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & -1/9 \\ 0 & 1 & -1/3 \\ 0 & 0 & 0 \end{pmatrix}$$

得 $\boldsymbol{x}_3 = (1, 3, 9)^T$。

**步骤3**：三个特征值互异，特征向量线性无关（也可直接由"不同特征值特征向量无关"保证）。

**步骤4**：拼装：

$$P = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 4 & 9 \end{pmatrix}, \quad \Lambda = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$

验证 $P^{-1}AP = \Lambda$（或验证 $AP = P\Lambda$，后者不用求逆更简单：$AP$ 的列 $= A\boldsymbol{x}_i = \lambda_i\boldsymbol{x}_i$，$P\Lambda$ 的列也 $= \lambda_i\boldsymbol{x}_i$，两边逐列相等）。

## 4. 对角化的应用

### 4.1 求矩阵的幂（最重要的应用）

若 $A = P\Lambda P^{-1}$，则：

$$A^k = P\Lambda^k P^{-1}$$

对角矩阵的幂就是对角线元素各自乘方，计算量从"矩阵连乘"降为"标量乘方"。

**示例**：设 $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$，求 $A^{10}$。

$A$ 的特征值为 $1, 3$，特征向量 $(1, -1)^T, (1, 1)^T$（025 篇示例1），故：

$$P = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}, \quad \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}, \quad P^{-1} = \frac{1}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$$

$$A^{10} = P\Lambda^{10}P^{-1} = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & 3^{10} \end{pmatrix}\frac{1}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1 + 3^{10} & -1 + 3^{10} \\ -1 + 3^{10} & 1 + 3^{10} \end{pmatrix}$$

### 4.2 求矩阵多项式

同理 $f(A) = Pf(\Lambda)P^{-1}$，其中 $f(\Lambda)$ 是对角元逐项代入 $f$。

### 4.3 解线性微分方程组

一阶线性常微分方程组 $\dfrac{d\boldsymbol{x}}{dt} = A\boldsymbol{x}$ 的解为 $\boldsymbol{x}(t) = e^{At}\boldsymbol{x}(0)$。若 $A = P\Lambda P^{-1}$：

$$e^{At} = Pe^{\Lambda t}P^{-1}$$

$e^{\Lambda t}$ 是对角元取 $e^{\lambda_i t}$ 的对角矩阵——微分方程组因此化为 $n$ 个独立的标量方程。这是控制系统、振动分析、人口动力学的标准解法（029 篇会展开应用）。

### 例1（重根但仍可对角化）

设 $A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$，判断 $A$ 是否可对角化；若可以，给出 $P$ 与 $\Lambda$。

**解**：特征值 $\lambda_1 = 1$（二重），$\lambda_2 = 2$。

对 $\lambda_1 = 1$：$A - I = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix}$，$r(A - I) = 1$，几何重数 $= 3 - 1 = 2 = $ 代数重数，合格。

对 $\lambda_2 = 2$：$A - 2I = \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$，$r = 2$，几何重数 $= 3 - 2 = 1 = $ 代数重数，合格。

$A$ 可对角化。特征向量：$\lambda_1 = 1$ 对应 $(1, 0, 0)^T$ 与 $(0, 1, 0)^T$；$\lambda_2 = 2$ 对应 $(0, 1, 1)^T$。取：

$$P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}, \quad \Lambda = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$

**注意**：重根 $\lambda = 1$ 的两个特征向量 $(1,0,0)^T$ 与 $(0,1,0)^T$ 恰好正交，但这不是必须的——对角化只要求线性无关，不要求正交（正交化是 028 篇实对称矩阵的事）。

### 例2（相似矩阵的特征值）

设 $A \sim B$，$A$ 的特征值为 $1, 2, 3$，求 $B^{-1}$ 的特征值。

**解**：$A \sim B$ 推得特征值相同，故 $B$ 的特征值为 $1, 2, 3$。由"逆矩阵的特征值是倒数的性质"，$B^{-1}$ 的特征值为 $1, \dfrac{1}{2}, \dfrac{1}{3}$。

### 例3（用对角化求序列递推）

设数列 $u_n$ 满足 $\begin{pmatrix} u_{n+1} \\ v_{n+1} \end{pmatrix} = A\begin{pmatrix} u_n \\ v_n \end{pmatrix}$，$A = \begin{pmatrix} 0.5 & 0.25 \\ 0.5 & 0.75 \end{pmatrix}$，初始 $(u_0, v_0)^T = (1, 0)^T$，求 $\begin{pmatrix} u_n \\ v_n \end{pmatrix}$ 的通项。

**解**：这是 $x_{n+1} = Ax_n$，解为 $x_n = A^nx_0$。先对角化 $A$：

$|\lambda I - A| = (\lambda - 0.5)(\lambda - 0.75) - 0.125 = \lambda^2 - 1.25\lambda + 0.25 = (\lambda - 1)(\lambda - 0.25)$。

特征值 $1$ 与 $0.25$，特征向量分别 $(1, 2)^T$ 与 $(1, -1)^T$。故：

$$A^n = P\begin{pmatrix} 1 & 0 \\ 0 & (0.25)^n \end{pmatrix}P^{-1}, \quad P = \begin{pmatrix} 1 & 1 \\ 2 & -1 \end{pmatrix}$$

$$x_n = P\begin{pmatrix} 1 & 0 \\ 0 & (0.25)^n \end{pmatrix}P^{-1}\begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

计算 $P^{-1}x_0 = \frac{1}{-3}\begin{pmatrix} -1 & -1 \\ -2 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1/3 \\ 2/3 \end{pmatrix}$，则：

$$u_n = \frac{1}{3} + \frac{2}{3}(0.25)^n, \quad v_n = \frac{2}{3} - \frac{2}{3}(0.25)^n$$

**检验**：$n \to \infty$ 时 $u_n \to 1/3$，$v_n \to 2/3$——这正是"特征值 1 对应的特征向量方向上的稳态"，为 029 篇的马尔可夫链应用埋下伏笔。

## 6. 常见错误与对策

| 常见错误 | 错误类型 | 原因 | 纠正方法 |
| --- | --- | --- | --- |
| $P$ 的列与 $\Lambda$ 的对角元顺序错位 | 计算规范问题 | 拼装时忘记一一对应 | 写 $AP = P\Lambda$ 逐列验证：$A\boldsymbol{x}_i = \lambda_i\boldsymbol{x}_i$ 必须逐列成立 |
| 认为"特征值相同就相似" | 逻辑错误 | 把必要条件当充分条件 | 相似 ⇒ 同特征值，但反过来不对（反例：$I$ 与 $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$） |
| 重根只求出一个特征向量就宣称可对角化 | 流程缺失 | 没数清几何重数 | 逐特征值检查 $m_g(\lambda_i) = n - r(A - \lambda_i I)$ 是否等于 $m_a(\lambda_i)$ |
| 用 $P^{-1}AP$ 验证时算错 $P^{-1}$ | 计算错误 | 逆矩阵不熟练 | 改用更稳的 $AP = P\Lambda$ 逐列验证，无需算逆 |
| 对角化后直接写 $A^k$ 的对角元为 $\lambda_i^k$ 而忘掉 $P$ | 概念理解错误 | 把"$A$ 相似于 $\Lambda$"当成"$A = \Lambda$" | 牢记 $A^k = P\Lambda^kP^{-1}$，只有 $A$ 本身就是对角矩阵时 $A^k$ 才等于 $\Lambda^k$ |
| 特征向量选了零向量或选了成比例的向量凑数 | 概念理解错误 | 误把"线性相关组"当"基" | $P$ 的列必须线性无关；重根的基础解系向量之间也要无关 |

## 8. 一句话记忆

**对角化 = 找 $n$ 个线性无关的特征向量当新坐标轴：$P$ 是特征向量拼成的坐标变换，$\Lambda$ 是特征值拼成的伸缩表，$P^{-1}AP = \Lambda$；重根的几何重数必须等于代数重数，否则配不齐。**
