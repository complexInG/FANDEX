---
order: 44
title: 施密特正交化
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 'Gram-Schmidt正交化方法与步骤，正交矩阵的定义与性质，正交对角化基础。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/坐标与坐标变换'
  - 'linear-algebra/内积与正交性'
  - 'linear-algebra/向量空间典型例题'
  - 'linear-algebra/特征值与特征向量计算'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 1. 施密特正交化方法

### 1.1 问题提出

给定一组线性无关的向量 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \ldots, \boldsymbol{\alpha}_s$，如何构造一组与之等价的正交向量组 $\boldsymbol{\beta}_1, \boldsymbol{\beta}_2, \ldots, \boldsymbol{\beta}_s$？

### 1.2 正交化公式

**Gram-Schmidt 正交化**步骤如下：

$$\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1$$

$$\boldsymbol{\beta}_2 = \boldsymbol{\alpha}_2 - \frac{(\boldsymbol{\alpha}_2, \boldsymbol{\beta}_1)}{(\boldsymbol{\beta}_1, \boldsymbol{\beta}_1)}\boldsymbol{\beta}_1$$

$$\boldsymbol{\beta}_3 = \boldsymbol{\alpha}_3 - \frac{(\boldsymbol{\alpha}_3, \boldsymbol{\beta}_1)}{(\boldsymbol{\beta}_1, \boldsymbol{\beta}_1)}\boldsymbol{\beta}_1 - \frac{(\boldsymbol{\alpha}_3, \boldsymbol{\beta}_2)}{(\boldsymbol{\beta}_2, \boldsymbol{\beta}_2)}\boldsymbol{\beta}_2$$

一般地：

$$\boldsymbol{\beta}_k = \boldsymbol{\alpha}_k - \sum_{j=1}^{k-1} \frac{(\boldsymbol{\alpha}_k, \boldsymbol{\beta}_j)}{(\boldsymbol{\beta}_j, \boldsymbol{\beta}_j)}\boldsymbol{\beta}_j, \quad k = 2, 3, \ldots, s$$

### 1.3 几何理解

每一步中，$\boldsymbol{\beta}_k$ 是 $\boldsymbol{\alpha}_k$ 减去其在已正交化向量 $\boldsymbol{\beta}_1, \ldots, \boldsymbol{\beta}_{k-1}$ 上的投影：

$$\boldsymbol{\beta}_k = \boldsymbol{\alpha}_k - \text{proj}_{\text{span}(\boldsymbol{\beta}_1, \ldots, \boldsymbol{\beta}_{k-1})} \boldsymbol{\alpha}_k$$

### 1.4 单位化

正交化后，将每个向量单位化：

$$\boldsymbol{e}_k = \frac{\boldsymbol{\beta}_k}{\|\boldsymbol{\beta}_k\|}$$

得到标准正交向量组 $\boldsymbol{e}_1, \boldsymbol{e}_2, \ldots, \boldsymbol{e}_s$。

### 1.5 完整示例

设 $\boldsymbol{\alpha}_1 = (1, 1, 0)^T$，$\boldsymbol{\alpha}_2 = (1, 0, 1)^T$，$\boldsymbol{\alpha}_3 = (0, 1, 1)^T$，用施密特正交化求标准正交组。

**步骤1**：$\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1 = (1, 1, 0)^T$

**步骤2**：

$$\boldsymbol{\beta}_2 = \boldsymbol{\alpha}_2 - \frac{(\boldsymbol{\alpha}_2, \boldsymbol{\beta}_1)}{(\boldsymbol{\beta}_1, \boldsymbol{\beta}_1)}\boldsymbol{\beta}_1 = (1, 0, 1)^T - \frac{1}{2}(1, 1, 0)^T = \left(\frac{1}{2}, -\frac{1}{2}, 1\right)^T$$

**步骤3**：

$$(\boldsymbol{\alpha}_3, \boldsymbol{\beta}_1) = 1, \quad (\boldsymbol{\alpha}_3, \boldsymbol{\beta}_2) = -\frac{1}{2} + 1 = \frac{1}{2}$$

$$(\boldsymbol{\beta}_2, \boldsymbol{\beta}_2) = \frac{1}{4} + \frac{1}{4} + 1 = \frac{3}{2}$$

$$\boldsymbol{\beta}_3 = (0, 1, 1)^T - \frac{1}{2}(1, 1, 0)^T - \frac{1/2}{3/2}\left(\frac{1}{2}, -\frac{1}{2}, 1\right)^T$$

$$= (0, 1, 1)^T - \left(\frac{1}{2}, \frac{1}{2}, 0\right)^T - \left(\frac{1}{6}, -\frac{1}{6}, \frac{1}{3}\right)^T = \left(-\frac{2}{3}, \frac{2}{3}, \frac{2}{3}\right)^T$$

**步骤4**：单位化

$$\|\boldsymbol{\beta}_1\| = \sqrt{2}, \quad \|\boldsymbol{\beta}_2\| = \sqrt{3/2}, \quad \|\boldsymbol{\beta}_3\| = \frac{2\sqrt{3}}{3}$$

$$\boldsymbol{e}_1 = \frac{1}{\sqrt{2}}(1, 1, 0)^T, \quad \boldsymbol{e}_2 = \frac{1}{\sqrt{6}}(1, -1, 2)^T, \quad \boldsymbol{e}_3 = \frac{1}{\sqrt{3}}(-1, 1, 1)^T$$

## 2. 正交矩阵

### 2.1 定义

$n$ 阶实方阵 $A$ 称为**正交矩阵**，若：

$$A^TA = I \quad \text{或} \quad A^{-1} = A^T$$

### 2.2 等价条件

以下条件等价：

1. $A$ 是正交矩阵
2. $A^TA = I$
3. $AA^T = I$
4. $A^{-1} = A^T$
5. $A$ 的列向量构成 $\mathbb{R}^n$ 的标准正交基
6. $A$ 的行向量构成 $\mathbb{R}^n$ 的标准正交基

### 2.3 正交矩阵的性质

1. $|A| = \pm 1$
2. $A^{-1}$ 也是正交矩阵
3. $A^T$ 也是正交矩阵
4. 两个正交矩阵的乘积仍是正交矩阵
5. 正交变换保持内积：$(A\boldsymbol{\alpha}, A\boldsymbol{\beta}) = (\boldsymbol{\alpha}, \boldsymbol{\beta})$
6. 正交变换保持长度：$\|A\boldsymbol{\alpha}\| = \|\boldsymbol{\alpha}\|$
7. 正交变换保持距离和角度

### 2.4 正交变换的几何意义

正交矩阵表示的线性变换是**刚体运动**（旋转或旋转加反射）：

- $|A| = 1$：旋转
- $|A| = -1$：旋转加反射（镜像）

### 2.5 常见正交矩阵

**二维旋转矩阵**：

$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

**置换矩阵**：每行每列恰好有一个1，其余为0。

## 3. 正交矩阵的构造

### 3.1 由标准正交基构造

将 $n$ 个 $n$ 维标准正交向量按列排列即得正交矩阵。

### 3.2 由施密特正交化构造

对任意可逆矩阵 $A$ 的列向量进行施密特正交化，得到正交矩阵 $Q$，且 $A = QR$（QR分解）。

## 4. 施密特正交化的应用

### 4.1 构造标准正交基

将向量空间的任意一组基正交化，得到标准正交基。

### 4.2 QR 分解

任意 $m \times n$ 矩阵（$m \geq n$，列满秩）可分解为 $A = QR$，其中 $Q$ 是 $m \times n$ 的列正交矩阵，$R$ 是 $n \times n$ 的上三角矩阵。

### 4.3 最小二乘法

求超定方程组 $Ax \approx b$ 的最小二乘解，等价于求解正规方程 $A^TAx = A^Tb$。利用 QR 分解可以简化计算。

### 4.4 实对称矩阵的正交对角化

对实对称矩阵的不同特征值对应的特征向量，自动正交；同一特征值对应的特征向量需要用施密特正交化。

## 5. 典型例题

### 例1

验证 $A = \begin{pmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & 0 & -\frac{2}{\sqrt{6}} \end{pmatrix}$ 是正交矩阵。

**解**：验证 $A^TA = I$：

$A^TA$ 的 $(1,1)$ 元素 $= \frac{1}{3} + \frac{1}{3} + \frac{1}{3} = 1$

$A^TA$ 的 $(1,2)$ 元素 $= \frac{1}{\sqrt{6}} - \frac{1}{\sqrt{6}} + 0 = 0$

（其余类似验证）

### 例2

设 $A$ 为正交矩阵，$|A| = -1$，证明 $|A + I| = 0$。

**证明**：

$|A + I| = |A + AA^T| = |A(I + A^T)| = |A| \cdot |I + A^T|$

$= -|I + A^T| = -|(I + A)^T| = -|I + A| = -|A + I|$

故 $2|A + I| = 0$，$|A + I| = 0$。

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
| 施密特正交化 | 023-GramSchmidtOrthogonalization | 本文自身 |
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
