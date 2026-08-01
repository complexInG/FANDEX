---
order: 30
title: 高斯消元法
module: 'linear-algebra'
category: 'comp-sci'
difficulty: beginner
description: 高斯消元法的基本步骤，行阶梯形与行最简形矩阵，消元过程与回代过程，主元选取策略。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/分块矩阵'
  - 'linear-algebra/矩阵典型例题'
  - 'linear-algebra/解的存在性判定'
  - 'linear-algebra/齐次线性方程组'
prerequisites: []
---

## 1. 高斯消元法概述

### 1.1 基本思想

高斯消元法（Gaussian Elimination）是求解线性方程组最基本的方法，通过初等行变换将增广矩阵化为行阶梯形或行最简形，从而求出方程组的解。

### 1.2 线性方程组的矩阵表示

线性方程组 $Ax = b$ 的增广矩阵为：

$$(A | b) = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \end{pmatrix}$$

对增广矩阵施行初等行变换，不改变方程组的解集。

## 2. 行阶梯形矩阵

### 2.1 定义

矩阵称为**行阶梯形**（Row Echelon Form, REF），若满足：

1. 零行（元素全为零的行）位于矩阵底部
2. 每个非零行的首非零元（主元）的列标严格递增
3. 主元下方的元素全为零

**示例**：

$$\begin{pmatrix} \boxed{2} & 3 & 1 & 4 \\ 0 & \boxed{1} & 2 & 5 \\ 0 & 0 & \boxed{3} & 6 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

其中 $\boxed{}$ 标记的是主元。

### 2.2 行最简形矩阵

行阶梯形进一步满足：

1. 每个主元为 $1$
2. 每个主元所在列的其他元素全为 $0$

称为**行最简形**（Reduced Row Echelon Form, RREF）。

**示例**：

$$\begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

## 3. 高斯消元法的步骤

### 3.1 前向消元（化为行阶梯形）

**步骤**：

1. 选取第一列中非零元素作为主元（若第一列全为零，则看第二列）
2. 若需要，交换行使主元位于第一行
3. 用主元消去其下方所有元素
4. 对右下角的子矩阵重复上述过程

**示例**：解方程组 $\begin{cases} x_1 + 2x_2 + x_3 = 2 \\ 2x_1 + 5x_2 + 3x_3 = 7 \\ x_1 + 3x_2 + 3x_3 = 5 \end{cases}$

增广矩阵：

$$\begin{pmatrix} 1 & 2 & 1 & 2 \\ 2 & 5 & 3 & 7 \\ 1 & 3 & 3 & 5 \end{pmatrix}$$

$$\xrightarrow{r_2 - 2r_1, r_3 - r_1} \begin{pmatrix} 1 & 2 & 1 & 2 \\ 0 & 1 & 1 & 3 \\ 0 & 1 & 2 & 3 \end{pmatrix}$$

$$\xrightarrow{r_3 - r_2} \begin{pmatrix} 1 & 2 & 1 & 2 \\ 0 & 1 & 1 & 3 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

### 3.2 回代过程

从最后一个非零行开始，逐步回代求出各未知量。

由行阶梯形：

$$\begin{cases} x_1 + 2x_2 + x_3 = 2 \\ x_2 + x_3 = 3 \\ x_3 = 0 \end{cases}$$

回代：$x_3 = 0$，$x_2 = 3 - 0 = 3$，$x_1 = 2 - 6 - 0 = -4$。

解为 $x_1 = -4, x_2 = 3, x_3 = 0$。

### 3.3 高斯-约当消元法（化为行最简形）

继续消元，将主元上方的元素也消为零：

$$\begin{pmatrix} 1 & 2 & 1 & 2 \\ 0 & 1 & 1 & 3 \\ 0 & 0 & 1 & 0 \end{pmatrix} \xrightarrow{r_2 - r_3, r_1 - r_3} \begin{pmatrix} 1 & 2 & 0 & 2 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & 0 \end{pmatrix} \xrightarrow{r_1 - 2r_2} \begin{pmatrix} 1 & 0 & 0 & -4 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

直接读出解：$x_1 = -4, x_2 = 3, x_3 = 0$。

## 4. 主元选取策略

### 4.1 部分主元选取

在每一步消元中，选取当前列中绝对值最大的元素作为主元，交换行使之到达主元位置。

**目的**：减少舍入误差的传播，提高数值稳定性。

### 4.2 全主元选取

在剩余子矩阵中选取绝对值最大的元素作为主元，可能需要同时交换行和列。

**优点**：数值稳定性最好。

**缺点**：计算量增大，且列交换需要记录未知量的顺序。

### 4.3 主元选取的重要性

不选主元时，若主元非常小，消元过程中会产生大数，导致严重的舍入误差。

**示例**：

$$\begin{cases} 0.001x_1 + x_2 = 1 \\ x_1 + x_2 = 2 \end{cases}$$

不选主元：$r_2 - 1000r_1$，会产生大系数，增大误差。

选主元：交换两行后消元，数值更稳定。

## 5. 高斯消元法的计算量

### 5.1 时间复杂度

- 前向消元：$O(n^3/3)$ 次乘除法
- 回代过程：$O(n^2/2)$ 次乘除法
- 总计：$O(n^3)$

### 5.2 与克莱姆法则的比较

| 方法       | 计算量          |
| ---------- | --------------- |
| 克莱姆法则 | $O(n \cdot n!)$ |
| 高斯消元法 | $O(n^3)$        |

高斯消元法远比克莱姆法则高效。

## 6. 高斯消元法的程序实现思路

### 6.1 伪代码

```
for k = 1 to n-1:
    // 选主元
    找到第k列中 |a_{ik}| 最大的行 i_max (i >= k)
    交换第k行和第i_max行
    // 消元
    for i = k+1 to m:
        factor = a_{ik} / a_{kk}
        for j = k to n+1:
            a_{ij} = a_{ij} - factor * a_{kj}
```

### 6.2 注意事项

1. 主元为零或接近零时需要特殊处理
2. 浮点运算中要注意数值稳定性
3. 稀疏矩阵可以使用特殊存储格式加速

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
| 高斯消元法 | 013-GaussianElimination | 本文自身 |
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
