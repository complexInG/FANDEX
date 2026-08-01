---
order: 41
title: 基与维数
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 极大线性无关组的概念与求法，向量组的秩，向量空间的基与维数，基变换与坐标变换。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/线性方程组典型例题'
  - 'linear-algebra/线性相关性'
  - 'linear-algebra/坐标与坐标变换'
  - 'linear-algebra/内积与正交性'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 1. 极大线性无关组

### 1.1 定义

设 $S$ 是向量组 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \ldots, \boldsymbol{\alpha}_s$ 的一个部分组，若满足：

1. $S$ 线性无关
2. $S$ 中添加原向量组的任何一个向量后都线性相关

则称 $S$ 为向量组 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \ldots, \boldsymbol{\alpha}_s$ 的一个**极大线性无关组**。

### 1.2 等价定义

极大线性无关组是向量组中满足以下条件的部分组：

1. 线性无关
2. 原向量组中每个向量都可由它线性表示

即极大线性无关组与原向量组等价。

### 1.3 性质

1. 极大线性无关组不唯一，但所含向量个数唯一
2. 任意两个极大线性无关组等价
3. 线性无关向量组的极大线性无关组就是它本身

### 1.4 求法

**初等行变换法**：

1. 将向量按列排成矩阵 $A = (\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \ldots, \boldsymbol{\alpha}_s)$
2. 对 $A$ 施行初等行变换，化为行阶梯形
3. 行阶梯形中主元所在的列对应的原向量构成极大线性无关组

**示例**：求 $\boldsymbol{\alpha}_1 = (1, 2, 3)^T$，$\boldsymbol{\alpha}_2 = (2, 4, 6)^T$，$\boldsymbol{\alpha}_3 = (1, 1, 1)^T$，$\boldsymbol{\alpha}_4 = (0, 1, 2)^T$ 的极大线性无关组。

$$A = \begin{pmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 1 & 1 \\ 3 & 6 & 1 & 2 \end{pmatrix} \xrightarrow{r_2-2r_1, r_3-3r_1} \begin{pmatrix} 1 & 2 & 1 & 0 \\ 0 & 0 & -1 & 1 \\ 0 & 0 & -2 & 2 \end{pmatrix}$$

$$\xrightarrow{r_3-2r_2} \begin{pmatrix} 1 & 2 & 1 & 0 \\ 0 & 0 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

主元在第1、3列，故 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_3$ 是一个极大线性无关组。

## 2. 向量组的秩

### 2.1 定义

向量组的**秩**等于其极大线性无关组所含向量的个数。

### 2.2 矩阵的秩与向量组的秩

矩阵 $A$ 的秩 = $A$ 的行向量组的秩 = $A$ 的列向量组的秩

### 2.3 性质

1. $r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s) \leq \min(s, n)$（$n$ 为向量维数）
2. $r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s) = s \iff \boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ 线性无关
3. 若向量组 (I) 可由 (II) 线性表示，则 $r(\text{I}) \leq r(\text{II})$
4. 等价的向量组秩相同

### 2.4 秩与线性表示

设 $\boldsymbol{\beta}$ 可由 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ 线性表示，则：

$$r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s, \boldsymbol{\beta}) = r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s)$$

反之亦然。

## 3. 向量空间的基与维数

### 3.1 向量空间的定义

设 $V$ 是 $\mathbb{R}^n$ 的非空子集，若满足：

1. 对加法封闭：$\boldsymbol{\alpha}, \boldsymbol{\beta} \in V \Rightarrow \boldsymbol{\alpha} + \boldsymbol{\beta} \in V$
2. 对数乘封闭：$\boldsymbol{\alpha} \in V, k \in \mathbb{R} \Rightarrow k\boldsymbol{\alpha} \in V$

则称 $V$ 为**向量空间**（$\mathbb{R}^n$ 的子空间）。

### 3.2 基的定义

向量空间 $V$ 中的向量组 $\boldsymbol{e}_1, \boldsymbol{e}_2, \ldots, \boldsymbol{e}_r$ 称为 $V$ 的一组**基**，若：

1. $\boldsymbol{e}_1, \boldsymbol{e}_2, \ldots, \boldsymbol{e}_r$ 线性无关
2. $V$ 中每个向量都可由 $\boldsymbol{e}_1, \boldsymbol{e}_2, \ldots, \boldsymbol{e}_r$ 线性表示

### 3.3 维数

向量空间 $V$ 的**维数** $\dim(V)$ 等于其基所含向量的个数。

### 3.4 常见向量空间

| 向量空间                  | 基                                           | 维数       |
| ------------------------- | -------------------------------------------- | ---------- |
| $\mathbb{R}^n$            | $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_n$ | $n$        |
| $N(A)$（零空间）          | 基础解系                                     | $n - r(A)$ |
| $\text{Col}(A)$（列空间） | $A$ 的列向量组的极大无关组                   | $r(A)$     |
| $\{0\}$                   | 无（空集）                                   | $0$        |

### 3.5 生成子空间

由向量 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ 的所有线性组合构成的集合称为由它们**生成**的子空间：

$$\text{span}(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s) = \{k_1\boldsymbol{\alpha}_1 + \cdots + k_s\boldsymbol{\alpha}_s \mid k_i \in \mathbb{R}\}$$

$\dim(\text{span}(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s)) = r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s)$

## 4. 基变换与坐标变换

### 4.1 向量的坐标

设 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_r$ 是向量空间 $V$ 的一组基，$\boldsymbol{\alpha} \in V$，则：

$$\boldsymbol{\alpha} = x_1\boldsymbol{e}_1 + x_2\boldsymbol{e}_2 + \cdots + x_r\boldsymbol{e}_r$$

$(x_1, x_2, \ldots, x_r)^T$ 称为 $\boldsymbol{\alpha}$ 在基 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_r$ 下的**坐标**。

### 4.2 过渡矩阵

设 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_n$ 和 $\boldsymbol{f}_1, \ldots, \boldsymbol{f}_n$ 是向量空间 $V$ 的两组基，且：

$$\begin{pmatrix} \boldsymbol{f}_1 & \boldsymbol{f}_2 & \cdots & \boldsymbol{f}_n \end{pmatrix} = \begin{pmatrix} \boldsymbol{e}_1 & \boldsymbol{e}_2 & \cdots & \boldsymbol{e}_n \end{pmatrix} P$$

则 $P$ 称为由基 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_n$ 到基 $\boldsymbol{f}_1, \ldots, \boldsymbol{f}_n$ 的**过渡矩阵**。

过渡矩阵 $P$ 一定是可逆的。

### 4.3 坐标变换公式

设 $\boldsymbol{\alpha}$ 在旧基下的坐标为 $x$，在新基下的坐标为 $y$，则：

$$x = Py \quad \text{或} \quad y = P^{-1}x$$

### 4.4 示例

设 $\boldsymbol{e}_1 = (1, 0)^T$，$\boldsymbol{e}_2 = (0, 1)^T$，$\boldsymbol{f}_1 = (1, 1)^T$，$\boldsymbol{f}_2 = (1, -1)^T$。

过渡矩阵：$\boldsymbol{f}_1 = \boldsymbol{e}_1 + \boldsymbol{e}_2$，$\boldsymbol{f}_2 = \boldsymbol{e}_1 - \boldsymbol{e}_2$

$$P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

$\boldsymbol{\alpha} = (3, 1)^T$ 在旧基下坐标为 $(3, 1)^T$，在新基下坐标为：

$$y = P^{-1}x = \frac{1}{-2}\begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$

验证：$2\boldsymbol{f}_1 + 1 \cdot \boldsymbol{f}_2 = 2(1,1)^T + (1,-1)^T = (3, 1)^T$

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
| 基与维数 | 020-BasisAndDimension | 本文自身 |
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
