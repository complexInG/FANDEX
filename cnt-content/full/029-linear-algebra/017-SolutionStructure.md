---
order: 34
title: 解的结构
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 线性方程组解的结构理论，通解、特解与基础解系的关系，解空间的维数与结构，解集的几何描述。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/齐次线性方程组'
  - 'linear-algebra/非齐次线性方程组'
  - 'linear-algebra/线性方程组典型例题'
  - 'linear-algebra/线性相关性'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 1. 解的结构总览

### 1.1 齐次方程组的解结构

$Ax = 0$ 的解集 $S_0$ 构成向量空间（零空间），其结构为：

$$S_0 = \{k_1\boldsymbol{\xi}_1 + k_2\boldsymbol{\xi}_2 + \cdots + k_t\boldsymbol{\xi}_t \mid k_i \in \mathbb{R}\}$$

其中 $\boldsymbol{\xi}_1, \ldots, \boldsymbol{\xi}_t$ 是基础解系，$t = n - r(A)$。

### 1.2 非齐次方程组的解结构

$Ax = b$ 的解集 $S$ 是仿射子空间：

$$S = \boldsymbol{\eta}^* + S_0 = \{\boldsymbol{\eta}^* + \boldsymbol{\xi} \mid \boldsymbol{\xi} \in S_0\}$$

其中 $\boldsymbol{\eta}^*$ 是 $Ax = b$ 的特解，$S_0$ 是导出组 $Ax = 0$ 的解空间。

## 2. 通解、特解与基础解系的关系

### 2.1 核心关系图

```
Ax = b 的通解 = 特解 + 导出组的通解
     x    =  η*  +  k₁ξ₁ + k₂ξ₂ + ... + kₜξₜ
```

### 2.2 各部分的作用

| 概念                                                      | 作用                 | 唯一性               |
| --------------------------------------------------------- | -------------------- | -------------------- |
| 特解 $\boldsymbol{\eta}^*$                                | 确定解集的"位置"     | 不唯一，任意特解均可 |
| 基础解系 $\boldsymbol{\xi}_1, \ldots, \boldsymbol{\xi}_t$ | 确定解集的"形状"     | 不唯一，但等价       |
| 自由参数 $k_1, \ldots, k_t$                               | 参数化解集中的每个解 | 依赖于基础解系的选取 |

### 2.3 特解的选取对通解的影响

设 $\boldsymbol{\eta}_1^*$ 和 $\boldsymbol{\eta}_2^*$ 是 $Ax = b$ 的两个不同特解，则：

$$\boldsymbol{\eta}_2^* = \boldsymbol{\eta}_1^* + \boldsymbol{\xi}_0$$

其中 $\boldsymbol{\xi}_0 \in S_0$。两个通解表达式等价：

$$\boldsymbol{\eta}_2^* + \sum k_i\boldsymbol{\xi}_i = \boldsymbol{\eta}_1^* + \boldsymbol{\xi}_0 + \sum k_i\boldsymbol{\xi}_i$$

由于 $\boldsymbol{\xi}_0$ 可由基础解系表示，故两个通解描述的是同一个解集。

## 3. 解空间的维数

### 3.1 维数公式

$$\dim(S_0) = n - r(A)$$

### 3.2 秩-零度定理

$$r(A) + \dim(N(A)) = n$$

这是线性代数中最基本的维数关系之一。

### 3.3 推广

对于 $m \times n$ 矩阵 $A$：

$$\dim(\text{Row}(A)) + \dim(N(A)) = n$$

$$\dim(\text{Col}(A)) + \dim(N(A^T)) = m$$

## 4. 解集的几何描述

### 4.1 齐次方程组

$Ax = 0$ 的解集是 $\mathbb{R}^n$ 中过原点的 $t$ 维子空间（$t = n - r(A)$）。

- $t = 0$：解集为单点 $\{0\}$
- $t = 1$：解集为过原点的直线
- $t = 2$：解集为过原点的平面
- $t = n$：解集为整个 $\mathbb{R}^n$（$A = O$ 时）

### 4.2 非齐次方程组

$Ax = b$ 的解集是 $\mathbb{R}^n$ 中的 $t$ 维仿射子空间（平移后的子空间）。

- $t = 0$：解集为单点（唯一解）
- $t = 1$：解集为不过原点的直线
- $t = 2$：解集为不过原点的平面

### 4.3 示例

$\begin{cases} x + y + z = 1 \end{cases}$

$r(A) = 1$，$n = 3$，$\dim(S_0) = 2$。

解集是 $\mathbb{R}^3$ 中不过原点的平面 $x + y + z = 1$。

特解：$(1, 0, 0)^T$，基础解系：$(-1, 1, 0)^T$，$(-1, 0, 1)^T$。

## 5. 解的结构与矩阵分解

### 5.1 与 SVD 的关系

设 $A = U\Sigma V^T$ 为 $A$ 的奇异值分解，则：

- $N(A) = \text{span}\{v_{r+1}, \ldots, v_n\}$（$V$ 的后 $n-r$ 列）
- $\text{Col}(A) = \text{span}\{u_1, \ldots, u_r\}$（$U$ 的前 $r$ 列）

### 5.2 与特征值的关系

若 $A$ 可对角化为 $A = P\Lambda P^{-1}$，则：

- $N(A)$ 由对应零特征值的特征向量张成
- $Ax = b$ 的解可通过对角化后求解

## 6. 解的稳定性

### 6.1 条件数

矩阵 $A$ 的**条件数**定义为：

$$\kappa(A) = \|A\| \cdot \|A^{-1}\|$$

条件数衡量了 $Ax = b$ 的解对 $b$ 的扰动的敏感程度。

- $\kappa(A) \approx 1$：良态问题，解稳定
- $\kappa(A) \gg 1$：病态问题，解不稳定

### 6.2 扰动分析

若 $b$ 有扰动 $\delta b$，则解的扰动 $\delta x$ 满足：

$$\frac{\|\delta x\|}{\|x\|} \leq \kappa(A) \cdot \frac{\|\delta b\|}{\|b\|}$$

## 7. 典型例题

### 例1

设 $A$ 为 $3 \times 4$ 矩阵，$\boldsymbol{\eta}_1 = (1, 0, 1, 0)^T$，$\boldsymbol{\eta}_2 = (0, 1, 0, 1)^T$ 是 $Ax = 0$ 的基础解系，$\boldsymbol{\eta}^* = (1, 1, 1, 1)^T$ 是 $Ax = b$ 的特解，求 $Ax = b$ 的通解。

**解**：通解 $x = \boldsymbol{\eta}^* + k_1\boldsymbol{\eta}_1 + k_2\boldsymbol{\eta}_2$

$$x = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} + k_1\begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} + k_2\begin{pmatrix} 0 \\ 1 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 + k_1 \\ 1 + k_2 \\ 1 + k_1 \\ 1 + k_2 \end{pmatrix}$$

### 例2

设 $A$ 为 $m \times n$ 矩阵，$r(A) = r$，证明 $Ax = b$ 的任意 $n - r + 1$ 个解线性相关。

**证明**：设 $\boldsymbol{\eta}_0$ 为特解，$\boldsymbol{\eta}_i = \boldsymbol{\eta}_0 + \boldsymbol{\xi}_i$（$i = 1, \ldots, n-r$），其中 $\boldsymbol{\xi}_i$ 是基础解系。

考虑 $n - r + 1$ 个解 $\boldsymbol{\eta}_0, \boldsymbol{\eta}_1, \ldots, \boldsymbol{\eta}_{n-r}$：

$$k_0\boldsymbol{\eta}_0 + k_1\boldsymbol{\eta}_1 + \cdots + k_{n-r}\boldsymbol{\eta}_{n-r} = 0$$

$$(k_0 + k_1 + \cdots + k_{n-r})\boldsymbol{\eta}_0 + k_1\boldsymbol{\xi}_1 + \cdots + k_{n-r}\boldsymbol{\xi}_{n-r} = 0$$

取 $k_0 = 1, k_1 = k_2 = \cdots = k_{n-r} = -\dfrac{1}{n-r}$，则 $k_0 + \sum k_i = 0$，且 $\sum k_i\boldsymbol{\xi}_i$ 是 $Ax = 0$ 的解。

但需要更仔细的分析。实际上，$n - r + 1$ 个解向量 $\boldsymbol{\eta}_0, \boldsymbol{\eta}_1, \ldots, \boldsymbol{\eta}_{n-r}$ 在 $n$ 维空间中，它们位于一个 $n - r$ 维仿射子空间上，故必线性相关。

## 参考文献

3Blue1Brown 线性代数的本质：https://www.3blue1brown.com/topics/linear-algebra
MIT 18.06：https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
NumPy 文档：https://numpy.org/doc/stable/
Interactive Linear Algebra：https://textbooks.math.gatech.edu/ila/

## 延伸阅读

线性代数基础，见 029-linear-algebra 模块文档。
微积分与优化，见 027-calculus 模块。
数据分析（PCA/矩阵），见 051-data-analysis 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供线性代数课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 矩阵分解体系

LU：消元分解，解方程组；QR：正交化，稳定最小二乘。
特征分解：对称矩阵可正交对角化；主成分分析基础。
SVD：A=UΣVᵀ，任意矩阵；低秩近似与压缩。
选择：一般求解 LU/QR，分析用 SVD/特征分解。

### 13.2 线性变换的几何

矩阵乘法 = 基向量的新位置；行列式 = 面积/体积缩放因子。
特征向量：变换中方向不变只伸缩的方向。
秩：变换后空间的维数（塌缩程度）。
应用：理解梯度、雅可比、神经网络层。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 行列式定义与几何意义 | 001-DeterminantDefinitionAndGeometry | 本文的并列主题 |
| 行列式基本性质 | 002-DeterminantBasicProperties | 本文的并列主题 |
| 行列式按行列展开 | 003-DeterminantRowColumnExpansion | 本文的并列主题 |
| 行列式计算方法 | 004-DeterminantCalculationMethods | 本文的并列主题 |
| 克莱姆法则 | 005-CramersRule | 本文的并列主题 |
| 行列式典型例题 | 006-DeterminantExamples | 本文的并列主题 |
| 矩阵运算 | 007-MatrixOperation | 本文的并列主题 |
| 逆矩阵 | 008-InverseMatrix | 本文的并列主题 |
| 初等变换与初等矩阵 | 009-ElementaryTransformationAndMatrix | 本文的并列主题 |
| 矩阵的秩 | 010-MatrixRank | 本文的并列主题 |
| 分块矩阵 | 011-ChunkingMatrix | 本文的并列主题 |
| 矩阵典型例题 | 012-MatrixExamples | 本文的并列主题 |
| 高斯消元法 | 013-GaussianElimination | 本文的并列主题 |
| 解的存在性判定 | 014-SolutionExistenceDetermination | 本文的并列主题 |
| 齐次线性方程组 | 015-HomogeneousLinearSystem | 本文的并列主题 |
| 非齐次线性方程组 | 016-NonHomogeneousLinearSystem | 本文的并列主题 |
| 解的结构 | 017-SolutionStructure | 本文自身 |
| 线性方程组典型例题 | 018-LinearSystemOfEquationsExamples | 本文的并列主题 |
| 线性相关性 | 019-LinearDependence | 本文的并列主题 |
| 基与维数 | 020-BasisAndDimension | 本文的并列主题 |
| 坐标与坐标变换 | 021-CoordinateAndTransformation | 本文的并列主题 |
| 内积与正交性 | 022-InnerProductAndOrthogonality | 本文的并列主题 |
| 施密特正交化 | 023-GramSchmidtOrthogonalization | 本文的并列主题 |
| 向量空间典型例题 | 024-VectorSpaceExamples | 本文的并列主题 |
| 特征值与特征向量计算 | 025-EigenvalueAndEigenvectorCalculation | 本文的并列主题 |
| 特征值性质 | 026-EigenvalueProperties | 本文的并列主题 |
| 矩阵对角化 | 027-MatrixDiagonalization | 本文的并列主题 |
| 实对称矩阵的对角化 | 028-RealSymmetricMatrixDiagonalization | 本文的并列主题 |
| 特征值典型例题 | 029-EigenvalueExamples | 本文的并列主题 |
| 二次型的标准形 | 030-QuadraticFormStandardForm | 本文的并列主题 |
| 二次型的规范形 | 031-QuadraticFormCanonicalForm | 本文的并列主题 |
| 正定二次型 | 032-PositiveDefiniteQuadraticForm | 本文的并列主题 |
| 二次型典型例题 | 033-QuadraticFormExamples | 本文的并列主题 |
| LU分解 | 034-LU | 本文的并列主题 |
| QR分解 | 035-QR | 本文的并列主题 |
| 奇异值分解SVD | 036-SVD | 本文的并列主题 |
| 矩阵分解应用 | 037-MatrixDecompositionApplication | 本文的并列主题 |
