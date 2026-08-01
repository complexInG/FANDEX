---
order: 53
title: 实对称矩阵的对角化
module: 'linear-algebra'
category: 'comp-sci'
difficulty: advanced
description: 实对称矩阵的性质，实对称矩阵的正交对角化，谱定理，正交对角化的步骤。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/特征值性质'
  - 'linear-algebra/矩阵对角化'
  - 'linear-algebra/特征值典型例题'
  - 'linear-algebra/二次型的标准形'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 1. 实对称矩阵的性质

### 1.1 基本性质

**定理1**：实对称矩阵的特征值都是实数。

**证明**：设 $A\boldsymbol{x} = \lambda\boldsymbol{x}$（$\boldsymbol{x} \neq 0$），则：

$$\bar{\boldsymbol{x}}^T A\boldsymbol{x} = \lambda \bar{\boldsymbol{x}}^T\boldsymbol{x}$$

$$\bar{\boldsymbol{x}}^T A\boldsymbol{x} = (A\bar{\boldsymbol{x}})^T\boldsymbol{x} = \bar{\lambda}\bar{\boldsymbol{x}}^T\boldsymbol{x}$$

故 $(\lambda - \bar{\lambda})\bar{\boldsymbol{x}}^T\boldsymbol{x} = 0$。因 $\bar{\boldsymbol{x}}^T\boldsymbol{x} > 0$，$\lambda = \bar{\lambda}$，$\lambda$ 为实数。

**定理2**：实对称矩阵属于不同特征值的特征向量正交。

**证明**：设 $A\boldsymbol{x}_1 = \lambda_1\boldsymbol{x}_1$，$A\boldsymbol{x}_2 = \lambda_2\boldsymbol{x}_2$，$\lambda_1 \neq \lambda_2$。

$$\lambda_1(\boldsymbol{x}_1, \boldsymbol{x}_2) = (A\boldsymbol{x}_1, \boldsymbol{x}_2) = (A\boldsymbol{x}_1)^T\boldsymbol{x}_2 = \boldsymbol{x}_1^T A^T\boldsymbol{x}_2 = \boldsymbol{x}_1^T A\boldsymbol{x}_2 = \lambda_2(\boldsymbol{x}_1, \boldsymbol{x}_2)$$

$(\lambda_1 - \lambda_2)(\boldsymbol{x}_1, \boldsymbol{x}_2) = 0$，因 $\lambda_1 \neq \lambda_2$，$(\boldsymbol{x}_1, \boldsymbol{x}_2) = 0$。

**定理3**：实对称矩阵一定可对角化（几何重数 = 代数重数）。

### 1.2 谱定理

**谱定理**（Spectral Theorem）：设 $A$ 为 $n$ 阶实对称矩阵，则存在正交矩阵 $Q$，使得：

$$Q^{-1}AQ = Q^TAQ = \Lambda = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$$

即实对称矩阵一定可以**正交对角化**。

等价表述：$A = Q\Lambda Q^T = \lambda_1\boldsymbol{q}_1\boldsymbol{q}_1^T + \lambda_2\boldsymbol{q}_2\boldsymbol{q}_2^T + \cdots + \lambda_n\boldsymbol{q}_n\boldsymbol{q}_n^T$

这称为 $A$ 的**谱分解**。

## 2. 正交对角化的步骤

### 2.1 步骤

1. 求出 $A$ 的所有特征值
2. 对每个特征值，求对应的特征向量
3. 对属于不同特征值的特征向量，它们已经正交
4. 对属于同一特征值的特征向量，用施密特正交化
5. 将所有特征向量单位化
6. 以标准正交特征向量为列构造正交矩阵 $Q$

### 2.2 完整示例

将 $A = \begin{pmatrix} 2 & -2 \\ -2 & 5 \end{pmatrix}$ 正交对角化。

**步骤1**：特征多项式

$$|A - \lambda I| = (2-\lambda)(5-\lambda) - 4 = \lambda^2 - 7\lambda + 6 = (\lambda-1)(\lambda-6)$$

特征值 $\lambda_1 = 1$，$\lambda_2 = 6$。

**步骤2**：

$\lambda_1 = 1$：$(A - I)\boldsymbol{x} = 0$

$$\begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}\boldsymbol{x} = 0 \Rightarrow x_1 = 2x_2$$

$\boldsymbol{x}_1 = (2, 1)^T$

$\lambda_2 = 6$：$(A - 6I)\boldsymbol{x} = 0$

$$\begin{pmatrix} -4 & -2 \\ -2 & -1 \end{pmatrix}\boldsymbol{x} = 0 \Rightarrow x_1 = -\frac{1}{2}x_2$$

$\boldsymbol{x}_2 = (1, -2)^T$

**步骤3**：不同特征值的特征向量已正交：$(2, 1) \cdot (1, -2) = 2 - 2 = 0$

**步骤4**：单位化

$\boldsymbol{q}_1 = \frac{1}{\sqrt{5}}(2, 1)^T$，$\boldsymbol{q}_2 = \frac{1}{\sqrt{5}}(1, -2)^T$

**步骤5**：

$$Q = \frac{1}{\sqrt{5}}\begin{pmatrix} 2 & 1 \\ 1 & -2 \end{pmatrix}, \quad \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 6 \end{pmatrix}$$

验证：$Q^TAQ = \Lambda$

### 2.3 有重特征值的示例

将 $A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$ 正交对角化。

**步骤1**：

$$|A - \lambda I| = \begin{vmatrix} 2-\lambda & 1 & 1 \\ 1 & 2-\lambda & 1 \\ 1 & 1 & 2-\lambda \end{vmatrix} = (4-\lambda)(1-\lambda)^2$$

$\lambda_1 = 4$（单根），$\lambda_2 = 1$（二重根）。

**步骤2**：

$\lambda_1 = 4$：$\boldsymbol{x}_1 = (1, 1, 1)^T$

$\lambda_2 = 1$：$(A - I)\boldsymbol{x} = 0$，$x_1 + x_2 + x_3 = 0$

基础解系：$\boldsymbol{\alpha}_1 = (-1, 1, 0)^T$，$\boldsymbol{\alpha}_2 = (-1, 0, 1)^T$

**步骤3**：$\boldsymbol{x}_1$ 与 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2$ 已正交（不同特征值）。

**步骤4**：对 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2$ 施密特正交化：

$\boldsymbol{\beta}_1 = (-1, 1, 0)^T$

$\boldsymbol{\beta}_2 = (-1, 0, 1)^T - \frac{1}{2}(-1, 1, 0)^T = (-1/2, -1/2, 1)^T$

**步骤5**：单位化

$\boldsymbol{q}_1 = \frac{1}{\sqrt{3}}(1, 1, 1)^T$，$\boldsymbol{q}_2 = \frac{1}{\sqrt{2}}(-1, 1, 0)^T$，$\boldsymbol{q}_3 = \frac{1}{\sqrt{6}}(-1, -1, 2)^T$

$$Q = \begin{pmatrix} \frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & 0 & \frac{2}{\sqrt{6}} \end{pmatrix}$$

## 3. 正交对角化的应用

### 3.1 二次型的标准化

实对称矩阵的正交对角化等价于用正交变换将二次型化为标准形。

### 3.2 矩阵函数的计算

$A = Q\Lambda Q^T$，则 $f(A) = Qf(\Lambda)Q^T$。

### 3.3 矩阵的极分解

利用谱分解可以研究正定矩阵、半正定矩阵等。

### 3.4 主成分分析（PCA）

PCA 的核心是对协方差矩阵（实对称矩阵）进行正交对角化，特征值表示各主成分的方差，特征向量表示主成分方向。

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
| 实对称矩阵的对角化 | 028-RealSymmetricMatrixDiagonalization | 本文自身 |
| 特征值典型例题 | 029-EigenvalueExamples | 本文的并列主题 |
| 二次型的标准形 | 030-QuadraticFormStandardForm | 本文的并列主题 |
| 二次型的规范形 | 031-QuadraticFormCanonicalForm | 本文的并列主题 |
| 正定二次型 | 032-PositiveDefiniteQuadraticForm | 本文的并列主题 |
| 二次型典型例题 | 033-QuadraticFormExamples | 本文的并列主题 |
| LU分解 | 034-LU | 本文的并列主题 |
| QR分解 | 035-QR | 本文的并列主题 |
| 奇异值分解SVD | 036-SVD | 本文的并列主题 |
| 矩阵分解应用 | 037-MatrixDecompositionApplication | 本文的并列主题 |
