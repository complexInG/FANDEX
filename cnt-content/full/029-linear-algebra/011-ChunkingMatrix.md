---
order: 24
title: 分块矩阵
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 分块矩阵的概念与运算，分块矩阵的乘法，分块对角矩阵，分块矩阵的求逆，分块矩阵的行列式。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/初等变换与初等矩阵'
  - 'linear-algebra/矩阵的秩'
  - 'linear-algebra/矩阵典型例题'
  - 'linear-algebra/高斯消元法'
prerequisites: []
---

## 1. 分块矩阵的概念

### 1.1 定义

用若干条横线和竖线将矩阵分成若干小块，每个小块称为**子矩阵**（子块），以子矩阵为元素的矩阵称为**分块矩阵**。

$$A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}$$

其中 $A_{11}, A_{12}, A_{21}, A_{22}$ 为子矩阵。

### 1.2 分块的原则

分块时须保证运算有意义：

- **加法**：对应子块必须同型
- **乘法**：左矩阵的列分法必须与右矩阵的行分法一致

## 2. 分块矩阵的运算

### 2.1 分块加法

设 $A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}$，$B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix}$（同型分块），则：

$$A + B = \begin{pmatrix} A_{11} + B_{11} & A_{12} + B_{12} \\ A_{21} + B_{21} & A_{22} + B_{22} \end{pmatrix}$$

### 2.2 分块数乘

$$kA = \begin{pmatrix} kA_{11} & kA_{12} \\ kA_{21} & kA_{22} \end{pmatrix}$$

### 2.3 分块乘法

设 $A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}$，$B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix}$，且分块方式使乘法有意义，则：

$$AB = \begin{pmatrix} A_{11}B_{11} + A_{12}B_{21} & A_{11}B_{12} + A_{12}B_{22} \\ A_{21}B_{11} + A_{22}B_{21} & A_{21}B_{12} + A_{22}B_{22} \end{pmatrix}$$

**关键**：子矩阵相乘时顺序不能交换，即 $A_{ij}B_{jk}$ 不能写成 $B_{jk}A_{ij}$。

### 2.4 分块转置

$$\begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}^T = \begin{pmatrix} A_{11}^T & A_{21}^T \\ A_{12}^T & A_{22}^T \end{pmatrix}$$

**注意**：分块转置不仅将子块的位置转置，每个子块本身也要转置。

## 3. 分块对角矩阵

### 3.1 定义

形如 $\begin{pmatrix} A_1 & & \\ & A_2 & \\ & & \ddots & \\ & & & A_s \end{pmatrix}$ 的分块矩阵称为**分块对角矩阵**，记作 $\text{diag}(A_1, A_2, \ldots, A_s)$。

### 3.2 性质

1. **行列式**：$|A| = |A_1| \cdot |A_2| \cdots |A_s|$

2. **乘法**：$\text{diag}(A_1, \ldots, A_s) \cdot \text{diag}(B_1, \ldots, B_s) = \text{diag}(A_1B_1, \ldots, A_sB_s)$

3. **幂**：$[\text{diag}(A_1, \ldots, A_s)]^k = \text{diag}(A_1^k, \ldots, A_s^k)$

4. **逆**：若每个 $A_i$ 可逆，则：

$$\text{diag}(A_1, \ldots, A_s)^{-1} = \text{diag}(A_1^{-1}, \ldots, A_s^{-1})$$

5. **秩**：$r(A) = r(A_1) + r(A_2) + \cdots + r(A_s)$

## 4. 分块矩阵的求逆

### 4.1 分块对角矩阵的逆

$$\begin{pmatrix} A & O \\ O & B \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} & O \\ O & B^{-1} \end{pmatrix}$$

### 4.2 分块上三角矩阵的逆

$$\begin{pmatrix} A & C \\ O & B \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} & -A^{-1}CB^{-1} \\ O & B^{-1} \end{pmatrix}$$

**验证**：

$$\begin{pmatrix} A & C \\ O & B \end{pmatrix}\begin{pmatrix} A^{-1} & -A^{-1}CB^{-1} \\ O & B^{-1} \end{pmatrix} = \begin{pmatrix} I & -CB^{-1} + CB^{-1} \\ O & I \end{pmatrix} = I$$

### 4.3 分块下三角矩阵的逆

$$\begin{pmatrix} A & O \\ C & B \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} & O \\ -B^{-1}CA^{-1} & B^{-1} \end{pmatrix}$$

### 4.4 一般分块矩阵的逆

对于 $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$，当 $A$ 可逆时，利用分块消元法：

$$\begin{pmatrix} I & O \\ -CA^{-1} & I \end{pmatrix}\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} A & B \\ O & D - CA^{-1}B \end{pmatrix}$$

令 $S = D - CA^{-1}B$（**Schur 补**），若 $S$ 可逆，则：

$$\begin{pmatrix} A & B \\ C & D \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} + A^{-1}BS^{-1}CA^{-1} & -A^{-1}BS^{-1} \\ -S^{-1}CA^{-1} & S^{-1} \end{pmatrix}$$

## 5. 分块矩阵的行列式

### 5.1 分块对角矩阵

$$\begin{vmatrix} A & O \\ O & B \end{vmatrix} = |A| \cdot |B|$$

### 5.2 分块三角矩阵

$$\begin{vmatrix} A & C \\ O & B \end{vmatrix} = |A| \cdot |B|$$

$$\begin{vmatrix} A & O \\ C & B \end{vmatrix} = |A| \cdot |B|$$

### 5.3 一般分块矩阵

当 $A$ 可逆时：

$$\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |A| \cdot |D - CA^{-1}B|$$

当 $D$ 可逆时：

$$\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |D| \cdot |A - BD^{-1}C|$$

### 5.4 特殊情形

当 $A$ 与 $C$ 可交换（$AC = CA$）时：

$$\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |AD - CB|$$

当 $B$ 与 $C$ 可交换（$BC = CB$）时：

$$\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |DA - CB|$$

## 6. 分块矩阵的应用

### 6.1 矩阵乘法的简化

对于具有分块结构的矩阵，分块乘法可以大大简化计算。

### 6.2 线性方程组的分块表示

$Ax = b$ 可写为分块形式：

$$\begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}$$

### 6.3 典型例题

**例**：设 $A$ 为 $m$ 阶可逆矩阵，$D$ 为 $n$ 阶可逆矩阵，证明 $\begin{pmatrix} A & B \\ O & D \end{pmatrix}$ 可逆并求其逆。

**解**：

$$\begin{vmatrix} A & B \\ O & D \end{vmatrix} = |A| \cdot |D| \neq 0$$

故该矩阵可逆。设逆为 $\begin{pmatrix} X & Y \\ Z & W \end{pmatrix}$，则：

$$\begin{pmatrix} A & B \\ O & D \end{pmatrix}\begin{pmatrix} X & Y \\ Z & W \end{pmatrix} = \begin{pmatrix} I_m & O \\ O & I_n \end{pmatrix}$$

由 $AX + BZ = I_m$，$AY + BW = O$，$DZ = O$，$DW = I_n$：

$Z = O$，$W = D^{-1}$，$X = A^{-1}$，$Y = -A^{-1}BD^{-1}$

$$\begin{pmatrix} A & B \\ O & D \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} & -A^{-1}BD^{-1} \\ O & D^{-1} \end{pmatrix}$$

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
| 分块矩阵 | 011-ChunkingMatrix | 本文自身 |
| 矩阵典型例题 | 012-MatrixExamples | 本文的并列主题 |
| 高斯消元法 | 013-GaussianElimination | 本文的并列主题 |
| 解的存在性判定 | 014-SolutionExistenceDetermination | 本文的并列主题 |
| 齐次线性方程组 | 015-HomogeneousLinearSystem | 本文的并列主题 |
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
