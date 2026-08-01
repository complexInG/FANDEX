---
order: 50
title: 特征值与特征向量计算
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 特征值与特征向量的定义，特征方程与特征多项式，特征值与特征向量的计算步骤与方法。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/施密特正交化'
  - 'linear-algebra/向量空间典型例题'
  - 'linear-algebra/特征值性质'
  - 'linear-algebra/矩阵对角化'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 1. 特征值与特征向量的定义

### 1.1 定义

设 $A$ 是 $n$ 阶方阵，若存在数 $\lambda$ 和非零向量 $\boldsymbol{x}$，使得：

$$A\boldsymbol{x} = \lambda\boldsymbol{x}$$

则称 $\lambda$ 为 $A$ 的**特征值**，$\boldsymbol{x}$ 为 $A$ 的属于特征值 $\lambda$ 的**特征向量**。

### 1.2 等价表述

$$A\boldsymbol{x} = \lambda\boldsymbol{x} \iff (A - \lambda I)\boldsymbol{x} = \mathbf{0}$$

$\boldsymbol{x} \neq \mathbf{0}$ 是 $(A - \lambda I)\boldsymbol{x} = \mathbf{0}$ 的非零解，故：

$$|A - \lambda I| = 0$$

### 1.3 特征空间

属于特征值 $\lambda$ 的所有特征向量加上零向量构成的集合称为 $\lambda$ 的**特征空间**：

$$V_\lambda = \{\boldsymbol{x} \mid A\boldsymbol{x} = \lambda\boldsymbol{x}\} = N(A - \lambda I)$$

特征空间的维数称为 $\lambda$ 的**几何重数**，即 $\dim(V_\lambda) = n - r(A - \lambda I)$。

## 2. 特征方程与特征多项式

### 2.1 特征方程

$$|A - \lambda I| = 0$$

称为 $A$ 的**特征方程**。

### 2.2 特征多项式

$$f(\lambda) = |A - \lambda I|$$

称为 $A$ 的**特征多项式**，它是关于 $\lambda$ 的 $n$ 次多项式。

$$f(\lambda) = (-1)^n\lambda^n + (-1)^{n-1}(\text{tr}A)\lambda^{n-1} + \cdots + |A|$$

### 2.3 特征多项式的展开

对于 $n$ 阶矩阵 $A$：

$$f(\lambda) = |\lambda I - A| = \lambda^n - (\text{tr}A)\lambda^{n-1} + \cdots + (-1)^n|A|$$

其中：

- $\lambda^{n-1}$ 的系数为 $-\text{tr}(A) = -(a_{11} + a_{22} + \cdots + a_{nn})$
- 常数项为 $(-1)^n|A|$

## 3. 特征值与特征向量的计算步骤

### 3.1 计算步骤

1. 计算特征多项式 $f(\lambda) = |A - \lambda I|$
2. 解特征方程 $|A - \lambda I| = 0$，求出所有特征值 $\lambda_1, \lambda_2, \ldots, \lambda_n$
3. 对每个特征值 $\lambda_i$，解齐次方程组 $(A - \lambda_i I)\boldsymbol{x} = \mathbf{0}$，求出基础解系，即为属于 $\lambda_i$ 的线性无关的特征向量

### 3.2 示例

求 $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ 的特征值与特征向量。

**步骤1**：特征多项式

$$|A - \lambda I| = \begin{vmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{vmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda-1)(\lambda-3)$$

**步骤2**：特征值为 $\lambda_1 = 1$，$\lambda_2 = 3$。

**步骤3**：

对 $\lambda_1 = 1$：$(A - I)\boldsymbol{x} = 0$

$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\boldsymbol{x} = 0 \Rightarrow x_1 + x_2 = 0$$

特征向量 $\boldsymbol{x}_1 = (1, -1)^T$（或其非零倍数）。

对 $\lambda_2 = 3$：$(A - 3I)\boldsymbol{x} = 0$

$$\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}\boldsymbol{x} = 0 \Rightarrow x_1 - x_2 = 0$$

特征向量 $\boldsymbol{x}_2 = (1, 1)^T$（或其非零倍数）。

### 3.3 三阶矩阵示例

求 $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}$ 的特征值。

$$|A - \lambda I| = \begin{vmatrix} -\lambda & 1 & 0 \\ 0 & -\lambda & 1 \\ 6 & -11 & 6-\lambda \end{vmatrix} = -\lambda[\lambda(\lambda-6) + 11] + 1 \cdot (0 - 6)$$

$$= -\lambda^3 + 6\lambda^2 - 11\lambda + 6 = -(\lambda - 1)(\lambda - 2)(\lambda - 3)$$

特征值为 $\lambda_1 = 1$，$\lambda_2 = 2$，$\lambda_3 = 3$。

## 4. 代数重数与几何重数

### 4.1 代数重数

特征值 $\lambda_i$ 作为特征方程根的重数称为 $\lambda_i$ 的**代数重数** $m_a(\lambda_i)$。

### 4.2 几何重数

$\lambda_i$ 的特征空间的维数称为 $\lambda_i$ 的**几何重数** $m_g(\lambda_i)$：

$$m_g(\lambda_i) = n - r(A - \lambda_i I)$$

### 4.3 关系

$$1 \leq m_g(\lambda_i) \leq m_a(\lambda_i)$$

几何重数不超过代数重数。

**示例**：$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$

特征值 $\lambda = 1$（二重根），代数重数为 $2$。

$A - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，$r(A - I) = 1$，几何重数 $= 2 - 1 = 1$。

## 5. 特征向量的性质

### 5.1 基本性质

1. 特征向量是非零向量
2. 若 $\boldsymbol{x}$ 是属于 $\lambda$ 的特征向量，则 $k\boldsymbol{x}$（$k \neq 0$）也是属于 $\lambda$ 的特征向量
3. 属于同一特征值的特征向量的线性组合（非零）仍是该特征值的特征向量
4. 属于不同特征值的特征向量线性无关

### 5.2 不同特征值的特征向量

**定理**：设 $\lambda_1, \lambda_2, \ldots, \lambda_s$ 是 $A$ 的互不相同的特征值，$\boldsymbol{x}_i$ 是属于 $\lambda_i$ 的特征向量，则 $\boldsymbol{x}_1, \boldsymbol{x}_2, \ldots, \boldsymbol{x}_s$ 线性无关。

**推广**：属于不同特征值的各组线性无关的特征向量合在一起仍线性无关。

## 6. 特殊矩阵的特征值

### 6.1 三角矩阵

上（下）三角矩阵的特征值就是主对角线上的元素。

### 6.2 对角矩阵

对角矩阵 $\text{diag}(d_1, d_2, \ldots, d_n)$ 的特征值就是 $d_1, d_2, \ldots, d_n$。

### 6.3 幂零矩阵

若 $A^k = O$（$k \geq 1$），则 $A$ 的特征值全为零。

### 6.4 正交矩阵

正交矩阵的特征值 $\lambda$ 满足 $|\lambda| = 1$。

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
| 特征值与特征向量计算 | 025-EigenvalueAndEigenvectorCalculation | 本文自身 |
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
