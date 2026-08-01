---
order: 12
title: 行列式按行列展开
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 余子式与代数余子式的定义，行列式按行（列）展开定理，代数余子式的性质，展开定理的应用。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/行列式定义与几何意义'
  - 'linear-algebra/行列式基本性质'
  - 'linear-algebra/行列式计算方法'
  - 'linear-algebra/克莱姆法则'
prerequisites: []
---

## 1. 余子式与代数余子式

### 1.1 余子式

在 $n$ 阶行列式 $|A|$ 中，划去元素 $a_{ij}$ 所在的第 $i$ 行和第 $j$ 列后，剩下的元素按原顺序构成的 $n-1$ 阶行列式，称为 $a_{ij}$ 的**余子式**，记作 $M_{ij}$。

$$M_{ij} = \begin{vmatrix} a_{11} & \cdots & a_{1,j-1} & a_{1,j+1} & \cdots & a_{1n} \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{i-1,1} & \cdots & a_{i-1,j-1} & a_{i-1,j+1} & \cdots & a_{i-1,n} \\ a_{i+1,1} & \cdots & a_{i+1,j-1} & a_{i+1,j+1} & \cdots & a_{i+1,n} \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{n1} & \cdots & a_{n,j-1} & a_{n,j+1} & \cdots & a_{nn} \end{vmatrix}$$

### 1.2 代数余子式

$a_{ij}$ 的**代数余子式**定义为：

$$A_{ij} = (-1)^{i+j} M_{ij}$$

符号规律：$(-1)^{i+j}$ 的符号可以用"棋盘法则"记忆——从 $(1,1)$ 位置开始，正负交替：

$$\begin{pmatrix} + & - & + & \cdots \\ - & + & - & \cdots \\ + & - & + & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

**示例**：设 $|A| = \begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix}$，求 $A_{23}$。

$$M_{23} = \begin{vmatrix} 1 & 2 \\ 7 & 8 \end{vmatrix} = 8 - 14 = -6$$

$$A_{23} = (-1)^{2+3} M_{23} = (-1)^5 \times (-6) = 6$$

## 2. 行列式按行（列）展开定理

### 2.1 展开定理

**定理**：行列式等于它的任意一行（列）的各元素与其对应的代数余子式的乘积之和。

**按第 $i$ 行展开**：

$$|A| = a_{i1}A_{i1} + a_{i2}A_{i2} + \cdots + a_{in}A_{in} = \sum_{j=1}^{n} a_{ij}A_{ij}$$

**按第 $j$ 列展开**：

$$|A| = a_{1j}A_{1j} + a_{2j}A_{2j} + \cdots + a_{nj}A_{nj} = \sum_{i=1}^{n} a_{ij}A_{ij}$$

### 2.2 展开定理的证明思路

以三阶行列式按第一行展开为例：

$$\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = a_{11} \begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} - a_{12} \begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} + a_{13} \begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}$$

$$= a_{11}A_{11} + a_{12}A_{12} + a_{13}A_{13}$$

### 2.3 展开定理的意义

展开定理将 $n$ 阶行列式的计算降为 $n-1$ 阶行列式的计算，实现了**降阶**。当某行（列）有较多零元素时，展开特别方便。

## 3. 代数余子式的重要性质

### 3.1 异行（列）代数余子式乘积之和为零

**定理**：行列式某一行（列）的元素与另一行（列）对应元素的代数余子式乘积之和为零。

$$a_{i1}A_{j1} + a_{i2}A_{j2} + \cdots + a_{in}A_{jn} = 0 \quad (i \neq j)$$

$$a_{1i}A_{1j} + a_{2i}A_{2j} + \cdots + a_{ni}A_{nj} = 0 \quad (i \neq j)$$

**证明思路**：$a_{i1}A_{j1} + a_{i2}A_{j2} + \cdots + a_{in}A_{jn}$ 相当于将行列式第 $j$ 行替换为第 $i$ 行后按第 $j$ 行展开，此时行列式有两行相同，值为零。

### 3.2 综合公式

$$\sum_{k=1}^{n} a_{ik}A_{jk} = \begin{cases} |A|, & i = j \\ 0, & i \neq j \end{cases}$$

$$\sum_{k=1}^{n} a_{ki}A_{kj} = \begin{cases} |A|, & i = j \\ 0, & i \neq j \end{cases}$$

用克罗内克符号（Kronecker delta）表示：

$$\sum_{k=1}^{n} a_{ik}A_{jk} = |A| \cdot \delta_{ij}$$

## 4. 展开定理的应用

### 4.1 选择零元素多的行（列）展开

**示例**：计算 $\begin{vmatrix} 3 & 0 & 0 & 0 \\ 2 & 1 & 0 & 0 \\ 1 & 2 & 2 & 0 \\ 4 & 3 & 1 & 3 \end{vmatrix}$

按第一行展开：

$$= 3 \times \begin{vmatrix} 1 & 0 & 0 \\ 2 & 2 & 0 \\ 3 & 1 & 3 \end{vmatrix} = 3 \times 1 \times \begin{vmatrix} 2 & 0 \\ 1 & 3 \end{vmatrix} = 3 \times 1 \times 6 = 18$$

### 4.2 先化简再展开

**示例**：计算 $\begin{vmatrix} 1 & 2 & 3 \\ 1 & 3 & 5 \\ 2 & 5 & 8 \end{vmatrix}$

$$\xrightarrow{r_2 - r_1, r_3 - 2r_1} \begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{vmatrix} = 0$$

（第2行与第3行相同）

### 4.3 利用代数余子式求和

**示例**：设 $|A| = \begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix}$，求 $A_{11} + A_{12} + A_{13}$。

由展开定理：$1 \cdot A_{11} + 2 \cdot A_{12} + 3 \cdot A_{13} = |A|$

但我们需要的是 $A_{11} + A_{12} + A_{13}$，这相当于将第一行替换为 $(1,1,1)$ 后的行列式：

$$A_{11} + A_{12} + A_{13} = \begin{vmatrix} 1 & 1 & 1 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix} = \begin{vmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{vmatrix} = 0$$

### 4.4 求代数余子式的线性组合

**关键技巧**：$k_1 A_{i1} + k_2 A_{i2} + \cdots + k_n A_{in}$ 等于将第 $i$ 行替换为 $(k_1, k_2, \ldots, k_n)$ 后的行列式。

**示例**：设 $D = \begin{vmatrix} 2 & 1 & 3 \\ 1 & 2 & 1 \\ 3 & 1 & 2 \end{vmatrix}$，求 $2A_{21} + A_{22} + 3A_{23}$。

这等于将第二行替换为 $(2, 1, 3)$ 后的行列式：

$$\begin{vmatrix} 2 & 1 & 3 \\ 2 & 1 & 3 \\ 3 & 1 & 2 \end{vmatrix} = 0$$

（第1行与第2行相同）

## 5. 递推法与展开定理

对于具有递推结构的行列式，展开定理可以建立递推关系。

**示例**：计算 $n$ 阶行列式 $D_n = \begin{vmatrix} a & b & 0 & \cdots & 0 & 0 \\ c & a & b & \cdots & 0 & 0 \\ 0 & c & a & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & a & b \\ 0 & 0 & 0 & \cdots & c & a \end{vmatrix}$（三对角行列式）

按第一行展开：

$$D_n = a \cdot D_{n-1} - b \cdot c \cdot D_{n-2}$$

这是一个二阶线性递推关系，特征方程为 $t^2 - at + bc = 0$。

当 $a^2 - 4bc > 0$ 时，设特征根为 $t_1, t_2$，则 $D_n = C_1 t_1^n + C_2 t_2^n$。

当 $a^2 = 4bc$ 时，$D_n = (C_1 + C_2 n) t^n$，其中 $t = a/2$。

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
| 行列式按行列展开 | 003-DeterminantRowColumnExpansion | 本文自身 |
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
