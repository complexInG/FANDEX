---
order: 10
title: 行列式定义与几何意义
module: 'linear-algebra'
category: 'comp-sci'
difficulty: beginner
description: 二阶行列式、三阶行列式、n阶行列式的定义，行列式的几何意义——有向面积与有向体积，排列与逆序数。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/行列式基本性质'
  - 'linear-algebra/行列式按行列展开'
prerequisites: []
---
## 0. 零基础入门（从零开始）

### 0.1 零基础起点

本模块讲解线性代数，零基础可学，需要高中数学基础（会解二元一次方程组即可）。
先建立直觉：线性代数研究的对象是“向量”（一组数，如坐标 (x, y)）和“矩阵”（一张数表，如 3x3 的数表）。矩阵可以理解为对向量做变换的“机器”：输入一个向量，输出变换后的向量。

### 0.2 第一个线性代数对象：行列式与线性方程组

```text
二元一次方程组：
  2x + 3y = 8
   x +  y = 3

写成矩阵形式：
  [2 3] [x]   [8]
  [1 1] [y] = [3]

系数行列式：
  |2 3|
  |1 1|  = 2*1 - 3*1 = -1   （不等于 0，说明方程组有唯一解）
```

方程组里的未知数系数排成一张表就是矩阵，等号右边的常数排成向量，整个方程组可以紧凑地写成“矩阵乘向量 = 向量”。
行列式是由方阵计算出的一个数，2x2 行列式的算法是主对角线乘积减副对角线乘积：2*1 - 3*1 = -1。
行列式是否等于 0 有几何含义：不等于 0 表示变换可逆、方程组有唯一解；等于 0 表示信息被压缩（无解或无穷多解）。
解这个方程组得到 x=1, y=2，你可以代入验证。
后续的矩阵乘法、逆矩阵、特征值都是在回答同一个问题：变换如何作用、能否还原、本质方向是什么。

## 1. 二阶行列式

### 1.1 定义

设有一个 $2 \times 2$ 的数表：

$$\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$$

其**二阶行列式**定义为：

$$\begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}$$

### 1.2 计算方法——对角线法则

二阶行列式的计算遵循**对角线法则**（沙路法则）：

- **主对角线**（左上到右下）：$a_{11}a_{22}$，取正号
- **副对角线**（右上到左下）：$a_{12}a_{21}$，取负号

$$\begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}$$

**示例**：

$$\begin{vmatrix} 3 & 1 \\ 2 & 4 \end{vmatrix} = 3 \times 4 - 1 \times 2 = 12 - 2 = 10$$

### 1.3 二元线性方程组的行列式解法

对于方程组：

$$\begin{cases} a_{11}x_1 + a_{12}x_2 = b_1 \\ a_{21}x_1 + a_{22}x_2 = b_2 \end{cases}$$

令 $D = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix}$，$D_1 = \begin{vmatrix} b_1 & a_{12} \\ b_2 & a_{22} \end{vmatrix}$，$D_2 = \begin{vmatrix} a_{11} & b_1 \\ a_{21} & b_2 \end{vmatrix}$

当 $D \neq 0$ 时，$x_1 = \dfrac{D_1}{D}$，$x_2 = \dfrac{D_2}{D}$。

## 2. 三阶行列式

### 2.1 定义

设有一个 $3 \times 3$ 的数表：

$$\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$$

其**三阶行列式**定义为：

$$\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{12}a_{21}a_{33} - a_{11}a_{23}a_{32}$$

### 2.2 对角线法则

三阶行列式的对角线法则：

- **三条主对角线方向**（取正号）：
  - $a_{11}a_{22}a_{33}$
  - $a_{12}a_{23}a_{31}$
  - $a_{13}a_{21}a_{32}$

- **三条副对角线方向**（取负号）：
  - $a_{13}a_{22}a_{31}$
  - $a_{12}a_{21}a_{33}$
  - $a_{11}a_{23}a_{32}$

**示例**：

$$\begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 0 \end{vmatrix} = 1 \times 5 \times 0 + 2 \times 6 \times 7 + 3 \times 4 \times 8 - 3 \times 5 \times 7 - 2 \times 4 \times 0 - 1 \times 6 \times 8$$

$$= 0 + 84 + 96 - 105 - 0 - 48 = 27$$

## 3. 排列与逆序数

### 3.1 排列

由 $1, 2, \ldots, n$ 组成的一个有序数组称为一个 **$n$ 阶排列**。$n$ 阶排列共有 $n!$ 个。

### 3.2 逆序与逆序数

在一个排列 $p_1 p_2 \cdots p_n$ 中，若 $i < j$ 但 $p_i > p_j$，则称 $(p_i, p_j)$ 构成一个**逆序**。

排列中逆序的总数称为该排列的**逆序数**，记作 $\tau(p_1 p_2 \cdots p_n)$。

**逆序数的计算方法**：对排列中每个元素，数其后面比它小的元素个数，然后求和。

**示例**：计算 $\tau(42513)$

- $4$ 后面比 $4$ 小的有 $2, 1, 3$，共 $3$ 个
- $2$ 后面比 $2$ 小的有 $1$，共 $1$ 个
- $5$ 后面比 $5$ 小的有 $1, 3$，共 $2$ 个
- $1$ 后面没有比 $1$ 小的，共 $0$ 个
- $3$ 后面没有，共 $0$ 个

$\tau(42513) = 3 + 1 + 2 + 0 + 0 = 6$

### 3.3 奇排列与偶排列

- 逆序数为**奇数**的排列称为**奇排列**
- 逆序数为**偶数**的排列称为**偶排列**

**对换**：交换排列中两个元素的位置。一次对换改变排列的奇偶性。

## 4. n阶行列式

### 4.1 定义

$n$ 阶行列式定义为：

$$\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{vmatrix} = \sum_{p_1 p_2 \cdots p_n} (-1)^{\tau(p_1 p_2 \cdots p_n)} a_{1p_1} a_{2p_2} \cdots a_{np_n}$$

其中求和取遍所有 $n$ 阶排列 $p_1 p_2 \cdots p_n$，共有 $n!$ 项。

### 4.2 等价定义（列标排列）

行列式也可以按列标排列定义：

$$|A| = \sum_{q_1 q_2 \cdots q_n} (-1)^{\tau(q_1 q_2 \cdots q_n)} a_{q_1 1} a_{q_2 2} \cdots a_{q_n n}$$

### 4.3 行列式定义的要点

1. 行列式是 $n!$ 项的代数和
2. 每项是取自不同行不同列的 $n$ 个元素的乘积
3. 每项的符号由行标排列和列标排列的逆序数共同决定
4. 当行标按自然序排列时，符号由列标排列的逆序数决定

**示例**：用定义计算四阶行列式中含 $a_{12}a_{23}a_{34}a_{41}$ 的项的符号。

行标排列为 $(1,2,3,4)$，列标排列为 $(2,3,4,1)$。

$\tau(2341) = 0 + 0 + 0 + 3 = 3$（奇数），故该项取负号：$-a_{12}a_{23}a_{34}a_{41}$。

## 5. 行列式的几何意义

### 5.1 二阶行列式的几何意义

二阶行列式 $\begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix}$ 的绝对值等于由列向量 $\boldsymbol{\alpha}_1 = (a_{11}, a_{21})^T$ 和 $\boldsymbol{\alpha}_2 = (a_{12}, a_{22})^T$ 张成的平行四边形的**面积**。

$$S = |a_{11}a_{22} - a_{12}a_{21}|$$

行列式的正负号表示两个列向量的**定向**：

- 行列式 $> 0$：$\boldsymbol{\alpha}_1$ 到 $\boldsymbol{\alpha}_2$ 为逆时针方向
- 行列式 $< 0$：$\boldsymbol{\alpha}_1$ 到 $\boldsymbol{\alpha}_2$ 为顺时针方向
- 行列式 $= 0$：两向量共线，面积为零

### 5.2 三阶行列式的几何意义

三阶行列式的绝对值等于由三个列向量张成的平行六面体的**体积**。

$$V = \left| \begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} \right|$$

行列式的正负号反映了三个向量的**手性**（右手系或左手系）。

### 5.3 n阶行列式的几何意义

$n$ 阶行列式的绝对值等于由 $n$ 个 $n$ 维列向量张成的**平行多面体的体积**。

行列式为零意味着这些向量线性相关，张成的"体积"为零，即所有向量落在一个低于 $n$ 维的超平面上。

### 5.4 行列式与线性变换

设 $T: \mathbb{R}^n \to \mathbb{R}^n$ 是由矩阵 $A$ 表示的线性变换，则：

$$\text{Vol}(T(\Omega)) = |\det(A)| \cdot \text{Vol}(\Omega)$$

即行列式的绝对值是线性变换的**体积伸缩因子**。

- $|\det(A)| > 1$：变换放大体积
- $|\det(A)| < 1$：变换缩小体积
- $|\det(A)| = 0$：变换将空间压缩到低维
- $\det(A) < 0$：变换改变了定向（如镜像反射）

## 6. 特殊行列式

### 6.1 对角行列式

$$\begin{vmatrix} a_{11} & 0 & \cdots & 0 \\ 0 & a_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_{nn} \end{vmatrix} = a_{11}a_{22} \cdots a_{nn} = \prod_{i=1}^{n} a_{ii}$$

### 6.2 上三角行列式

$$\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ 0 & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_{nn} \end{vmatrix} = a_{11}a_{22} \cdots a_{nn}$$

### 6.3 副对角线行列式

$$\begin{vmatrix} 0 & \cdots & 0 & a_{1n} \\ 0 & \cdots & a_{2,n-1} & 0 \\ \vdots & \iddots & \vdots & \vdots \\ a_{n1} & \cdots & 0 & 0 \end{vmatrix} = (-1)^{\frac{n(n-1)}{2}} a_{1n}a_{2,n-1} \cdots a_{n1}$$

当 $n = 2$ 时，符号为 $(-1)^1 = -1$；当 $n = 3$ 时，符号为 $(-1)^3 = -1$；当 $n = 4$ 时，符号为 $(-1)^6 = 1$。

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
| 行列式定义与几何意义 | 001-DeterminantDefinitionAndGeometry | 本文自身 |
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
