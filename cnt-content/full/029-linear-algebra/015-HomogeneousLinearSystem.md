---
order: 32
title: 齐次线性方程组
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 齐次线性方程组的性质，基础解系的概念与求法，解空间的维数定理，齐次方程组的通解。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/高斯消元法'
  - 'linear-algebra/解的存在性判定'
  - 'linear-algebra/非齐次线性方程组'
  - 'linear-algebra/解的结构'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 1. 齐次线性方程组的基本性质

### 1.1 定义

齐次线性方程组的形式为 $Ax = 0$，即：

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = 0 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = 0 \\ \cdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = 0 \end{cases}$$

### 1.2 基本性质

1. **零解**：$x = 0$ 一定是齐次方程组的解
2. **解的线性组合**：若 $x_1, x_2$ 是 $Ax = 0$ 的解，则 $k_1x_1 + k_2x_2$ 也是解（$k_1, k_2$ 为任意常数）
3. **解集构成向量空间**：$Ax = 0$ 的全体解构成 $\mathbb{R}^n$ 的一个子空间，称为**解空间**或**零空间** $N(A)$

### 1.3 非零解的存在条件

$$Ax = 0 \text{ 有非零解} \iff r(A) < n$$

特别地，当 $m < n$ 时，$Ax = 0$ 一定有非零解。

## 2. 基础解系

### 2.1 定义

齐次方程组 $Ax = 0$ 的解向量 $\boldsymbol{\xi}_1, \boldsymbol{\xi}_2, \ldots, \boldsymbol{\xi}_t$ 称为**基础解系**，若：

1. $\boldsymbol{\xi}_1, \boldsymbol{\xi}_2, \ldots, \boldsymbol{\xi}_t$ 线性无关
2. $Ax = 0$ 的任意解都可以由 $\boldsymbol{\xi}_1, \boldsymbol{\xi}_2, \ldots, \boldsymbol{\xi}_t$ 线性表示

基础解系就是解空间的一组**基**。

### 2.2 基础解系所含向量的个数

$$t = n - r(A)$$

即基础解系所含向量的个数等于未知量的个数减去系数矩阵的秩。

### 2.3 维数定理

$$\dim(N(A)) = n - r(A)$$

解空间的维数等于自由变量的个数。

## 3. 基础解系的求法

### 3.1 步骤

1. 将系数矩阵 $A$ 化为行最简形
2. 确定主变量（主元对应的未知量）和自由变量（非主元对应的未知量）
3. 令自由变量依次取 $(1,0,\ldots,0)^T$，$(0,1,\ldots,0)^T$，...，$(0,0,\ldots,1)^T$
4. 回代求出主变量的值，得到基础解系

### 3.2 示例

求 $Ax = 0$ 的基础解系，其中 $A = \begin{pmatrix} 1 & 2 & 3 & 1 \\ 2 & 4 & 6 & 2 \\ 1 & 2 & 1 & 1 \end{pmatrix}$

**步骤1**：化行最简形

$$A \xrightarrow{r_2 - 2r_1, r_3 - r_1} \begin{pmatrix} 1 & 2 & 3 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & -2 & 0 \end{pmatrix} \xrightarrow{r_2 \leftrightarrow r_3} \begin{pmatrix} 1 & 2 & 3 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

$$\xrightarrow{-\frac{1}{2}r_2} \begin{pmatrix} 1 & 2 & 3 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \xrightarrow{r_1 - 3r_2} \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

**步骤2**：$r(A) = 2$，主变量为 $x_1, x_3$，自由变量为 $x_2, x_4$。

**步骤3**：基础解系含 $4 - 2 = 2$ 个向量。

令 $(x_2, x_4) = (1, 0)$：$x_3 = 0$，$x_1 = -2$，得 $\boldsymbol{\xi}_1 = (-2, 1, 0, 0)^T$

令 $(x_2, x_4) = (0, 1)$：$x_3 = 0$，$x_1 = -1$，得 $\boldsymbol{\xi}_2 = (-1, 0, 0, 1)^T$

**步骤4**：基础解系为 $\boldsymbol{\xi}_1 = (-2, 1, 0, 0)^T$，$\boldsymbol{\xi}_2 = (-1, 0, 0, 1)^T$。

### 3.3 通解

$$x = k_1\boldsymbol{\xi}_1 + k_2\boldsymbol{\xi}_2 \quad (k_1, k_2 \text{ 为任意常数})$$

## 4. 基础解系的性质

### 4.1 唯一性

基础解系不唯一，但任意两个基础解系所含向量个数相同，且它们等价（可以互相线性表示）。

### 4.2 判定基础解系的方法

设 $\boldsymbol{\xi}_1, \boldsymbol{\xi}_2, \ldots, \boldsymbol{\xi}_t$ 都是 $Ax = 0$ 的解，则它们构成基础解系当且仅当：

1. 它们线性无关
2. $t = n - r(A)$

**注意**：条件2可以用"它们线性无关"替代"它们线性无关且 $t = n - r(A)$"——只要验证线性无关且个数正确即可。

### 4.3 基础解系的线性变换

若 $\boldsymbol{\xi}_1, \ldots, \boldsymbol{\xi}_t$ 是基础解系，$C$ 为 $t$ 阶可逆矩阵，则 $(\boldsymbol{\xi}_1, \ldots, \boldsymbol{\xi}_t)C$ 的列向量也是基础解系。

## 5. 解空间的结构

### 5.1 解空间的维数

$$\dim(N(A)) = n - r(A)$$

### 5.2 解空间与列空间的关系

$$\mathbb{R}^n = \text{Row}(A) \oplus N(A)$$

行空间与零空间互为正交补（在标准内积下）。

### 5.3 解空间的基变换

设 $B_1 = \{\boldsymbol{\xi}_1, \ldots, \boldsymbol{\xi}_t\}$ 和 $B_2 = \{\boldsymbol{\eta}_1, \ldots, \boldsymbol{\eta}_t\}$ 是两组基础解系，则存在可逆矩阵 $P$ 使得：

$$(\boldsymbol{\eta}_1, \ldots, \boldsymbol{\eta}_t) = (\boldsymbol{\xi}_1, \ldots, \boldsymbol{\xi}_t)P$$

## 6. 典型例题

### 例1

设 $A$ 为 $m \times n$ 矩阵，$r(A) = r$，证明 $Ax = 0$ 的基础解系含 $n - r$ 个向量。

**证明**：将 $A$ 化为行最简形，有 $r$ 个主元，$n - r$ 个自由变量。每个自由变量对应一个解向量，共 $n - r$ 个，它们线性无关且任意解可由它们表示。

### 例2

设 $A$ 为 $n$ 阶方阵，$|A| = 0$，$A_{11} \neq 0$（$A_{11}$ 为 $a_{11}$ 的代数余子式），求 $Ax = 0$ 的通解。

**解**：$|A| = 0$ 且 $A_{11} \neq 0$，故 $r(A) = n - 1$，基础解系含 $1$ 个向量。

由 $AA^* = |A|I = O$，$A^*$ 的第一列 $(A_{11}, A_{21}, \ldots, A_{n1})^T$ 是 $Ax = 0$ 的解。

又 $A_{11} \neq 0$，故该解非零，可作为基础解系。

通解：$x = k(A_{11}, A_{21}, \ldots, A_{n1})^T$（$k$ 为任意常数）。

### 例3

设 $A$ 为 $n$ 阶方阵，$A^2 = A$，$r(A) = r$，求 $Ax = 0$ 的基础解系所含向量的个数。

**解**：$Ax = 0$ 的基础解系含 $n - r(A) = n - r$ 个向量。

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
| 齐次线性方程组 | 015-HomogeneousLinearSystem | 本文自身 |
| 非齐次线性方程组 | 016-NonHomogeneousLinearSystem | 本文的并列主题 |
| 解的结构 | 017-SolutionStructure | 本文的并列主题 |
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
