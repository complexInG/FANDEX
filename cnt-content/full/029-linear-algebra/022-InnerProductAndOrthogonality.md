---
order: 43
title: 内积与正交性
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 内积的定义与性质，向量的长度与距离，正交向量与正交向量组，正交补空间。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/基与维数'
  - 'linear-algebra/坐标与坐标变换'
  - 'linear-algebra/施密特正交化'
  - 'linear-algebra/向量空间典型例题'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 1. 内积

### 1.1 定义

设 $\boldsymbol{\alpha} = (a_1, a_2, \ldots, a_n)^T$，$\boldsymbol{\beta} = (b_1, b_2, \ldots, b_n)^T$ 是 $\mathbb{R}^n$ 中的向量，它们的**内积**（标准内积）定义为：

$$(\boldsymbol{\alpha}, \boldsymbol{\beta}) = \boldsymbol{\alpha}^T\boldsymbol{\beta} = a_1b_1 + a_2b_2 + \cdots + a_nb_n = \sum_{i=1}^{n} a_ib_i$$

### 1.2 内积的性质

1. **对称性**：$(\boldsymbol{\alpha}, \boldsymbol{\beta}) = (\boldsymbol{\beta}, \boldsymbol{\alpha})$
2. **线性性**：$(k_1\boldsymbol{\alpha}_1 + k_2\boldsymbol{\alpha}_2, \boldsymbol{\beta}) = k_1(\boldsymbol{\alpha}_1, \boldsymbol{\beta}) + k_2(\boldsymbol{\alpha}_2, \boldsymbol{\beta})$
3. **正定性**：$(\boldsymbol{\alpha}, \boldsymbol{\alpha}) \geq 0$，等号成立当且仅当 $\boldsymbol{\alpha} = \mathbf{0}$

### 1.3 一般内积

更一般地，设 $A$ 为 $n$ 阶正定矩阵，可以定义加权内积：

$$(\boldsymbol{\alpha}, \boldsymbol{\beta})_A = \boldsymbol{\alpha}^T A \boldsymbol{\beta}$$

### 1.4 Cauchy-Schwarz 不等式

$$|(\boldsymbol{\alpha}, \boldsymbol{\beta})| \leq \|\boldsymbol{\alpha}\| \cdot \|\boldsymbol{\beta}\|$$

等号成立当且仅当 $\boldsymbol{\alpha}$ 与 $\boldsymbol{\beta}$ 线性相关。

## 2. 向量的长度与距离

### 2.1 长度（范数）

向量 $\boldsymbol{\alpha}$ 的**长度**（或**范数**）定义为：

$$\|\boldsymbol{\alpha}\| = \sqrt{(\boldsymbol{\alpha}, \boldsymbol{\alpha})} = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}$$

### 2.2 长度的性质

1. **非负性**：$\|\boldsymbol{\alpha}\| \geq 0$，等号成立当且仅当 $\boldsymbol{\alpha} = \mathbf{0}$
2. **齐次性**：$\|k\boldsymbol{\alpha}\| = |k| \cdot \|\boldsymbol{\alpha}\|$
3. **三角不等式**：$\|\boldsymbol{\alpha} + \boldsymbol{\beta}\| \leq \|\boldsymbol{\alpha}\| + \|\boldsymbol{\beta}\|$

### 2.3 单位向量

长度为 $1$ 的向量称为**单位向量**。对非零向量 $\boldsymbol{\alpha}$，$\dfrac{\boldsymbol{\alpha}}{\|\boldsymbol{\alpha}\|}$ 是与 $\boldsymbol{\alpha}$ 同方向的单位向量，称为 $\boldsymbol{\alpha}$ 的**单位化**。

### 2.4 距离

两个向量 $\boldsymbol{\alpha}$ 和 $\boldsymbol{\beta}$ 之间的**距离**定义为：

$$d(\boldsymbol{\alpha}, \boldsymbol{\beta}) = \|\boldsymbol{\alpha} - \boldsymbol{\beta}\|$$

### 2.5 夹角

两个非零向量 $\boldsymbol{\alpha}$ 和 $\boldsymbol{\beta}$ 的**夹角** $\theta$ 满足：

$$\cos\theta = \frac{(\boldsymbol{\alpha}, \boldsymbol{\beta})}{\|\boldsymbol{\alpha}\| \cdot \|\boldsymbol{\beta}\|}$$

## 3. 正交向量

### 3.1 定义

若 $(\boldsymbol{\alpha}, \boldsymbol{\beta}) = 0$，则称 $\boldsymbol{\alpha}$ 与 $\boldsymbol{\beta}$ **正交**，记作 $\boldsymbol{\alpha} \perp \boldsymbol{\beta}$。

**几何意义**：两个向量正交意味着它们的夹角为 $90°$。

### 3.2 正交的性质

1. 零向量与任何向量正交
2. $\boldsymbol{\alpha} \perp \boldsymbol{\beta} \iff \|\boldsymbol{\alpha} + \boldsymbol{\beta}\|^2 = \|\boldsymbol{\alpha}\|^2 + \|\boldsymbol{\beta}\|^2$（勾股定理）
3. 若 $\boldsymbol{\alpha} \perp \boldsymbol{\beta}_1$ 且 $\boldsymbol{\alpha} \perp \boldsymbol{\beta}_2$，则 $\boldsymbol{\alpha} \perp (k_1\boldsymbol{\beta}_1 + k_2\boldsymbol{\beta}_2)$

### 3.3 正交向量组

若向量组 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \ldots, \boldsymbol{\alpha}_s$ 中任意两个向量都正交（即 $(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_j) = 0$，$i \neq j$），则称为**正交向量组**。

### 3.4 正交向量组的重要性质

**定理**：不含零向量的正交向量组一定线性无关。

**证明**：设 $k_1\boldsymbol{\alpha}_1 + k_2\boldsymbol{\alpha}_2 + \cdots + k_s\boldsymbol{\alpha}_s = 0$，两边与 $\boldsymbol{\alpha}_i$ 做内积：

$$k_i(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_i) = 0$$

因 $\boldsymbol{\alpha}_i \neq 0$，$(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_i) > 0$，故 $k_i = 0$。

### 3.5 标准正交向量组

若正交向量组中每个向量都是单位向量，则称为**标准正交向量组**（或规范正交组），即：

$$(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_j) = \delta_{ij} = \begin{cases} 1, & i = j \\ 0, & i \neq j \end{cases}$$

**标准正交基**：若 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_n$ 是 $n$ 维向量空间的标准正交基，则任意向量 $\boldsymbol{\beta}$ 的坐标为：

$$x_i = (\boldsymbol{\beta}, \boldsymbol{\alpha}_i)$$

即 $\boldsymbol{\beta} = \sum_{i=1}^{n} (\boldsymbol{\beta}, \boldsymbol{\alpha}_i)\boldsymbol{\alpha}_i$。

## 4. 正交补空间

### 4.1 定义

设 $W$ 是 $\mathbb{R}^n$ 的子空间，所有与 $W$ 中每个向量都正交的向量构成的集合称为 $W$ 的**正交补**，记作 $W^\perp$：

$$W^\perp = \{\boldsymbol{\alpha} \in \mathbb{R}^n \mid (\boldsymbol{\alpha}, \boldsymbol{\beta}) = 0, \forall \boldsymbol{\beta} \in W\}$$

### 4.2 性质

1. $W^\perp$ 也是子空间
2. $W \cap W^\perp = \{\mathbf{0}\}$
3. $\dim(W) + \dim(W^\perp) = n$
4. $(W^\perp)^\perp = W$
5. $\mathbb{R}^n = W \oplus W^\perp$（正交直和分解）

### 4.3 与矩阵的关系

- $N(A) = (\text{Row}(A))^\perp$
- $N(A^T) = (\text{Col}(A))^\perp$

### 4.4 正交投影

向量 $\boldsymbol{\alpha}$ 在子空间 $W$ 上的**正交投影** $\text{proj}_W \boldsymbol{\alpha}$ 满足：

$$\boldsymbol{\alpha} = \text{proj}_W \boldsymbol{\alpha} + \boldsymbol{\alpha}_\perp$$

其中 $\boldsymbol{\alpha}_\perp \in W^\perp$。

若 $W$ 的一组标准正交基为 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_r$，则：

$$\text{proj}_W \boldsymbol{\alpha} = \sum_{i=1}^{r} (\boldsymbol{\alpha}, \boldsymbol{e}_i)\boldsymbol{e}_i$$

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
| 内积与正交性 | 022-InnerProductAndOrthogonality | 本文自身 |
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
