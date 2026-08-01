---
order: 52
title: 矩阵对角化
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 相似矩阵的定义与性质，矩阵可对角化的条件与判别，对角化的步骤与方法。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/特征值与特征向量计算'
  - 'linear-algebra/特征值性质'
  - 'linear-algebra/实对称矩阵的对角化'
  - 'linear-algebra/特征值典型例题'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 1. 相似矩阵

### 1.1 定义

设 $A, B$ 为 $n$ 阶方阵，若存在可逆矩阵 $P$，使得：

$$B = P^{-1}AP$$

则称 $A$ 与 $B$ **相似**，记作 $A \sim B$。

### 1.2 相似关系的性质

1. **自反性**：$A \sim A$
2. **对称性**：$A \sim B \Rightarrow B \sim A$
3. **传递性**：$A \sim B, B \sim C \Rightarrow A \sim C$

### 1.3 相似矩阵的共同性质

若 $A \sim B$，则：

1. $|A| = |B|$
2. $\text{tr}(A) = \text{tr}(B)$
3. $r(A) = r(B)$
4. $A$ 和 $B$ 有相同的特征值（含重数）
5. $|A - \lambda I| = |B - \lambda I|$（特征多项式相同）
6. $A$ 可逆 $\iff$ $B$ 可逆
7. $A^k \sim B^k$
8. $f(A) \sim f(B)$（$f$ 为多项式）

### 1.4 相似的必要条件

以上性质都是相似的必要条件，但不是充分条件。两个矩阵有相同的特征值不一定相似。

**反例**：$A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$，$B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$

特征值都是 $1, 1$，但 $A$ 不相似于 $B$（$A = I$ 只与自身相似）。

## 2. 矩阵可对角化的条件

### 2.1 定义

若 $A$ 相似于对角矩阵，即存在可逆矩阵 $P$ 使得 $P^{-1}AP = \Lambda$（对角矩阵），则称 $A$ **可对角化**。

### 2.2 可对角化的等价条件

以下条件等价：

1. $A$ 可对角化
2. $A$ 有 $n$ 个线性无关的特征向量
3. 每个特征值的几何重数等于代数重数

### 2.3 充分条件

1. $A$ 有 $n$ 个互不相同的特征值 $\Rightarrow$ $A$ 可对角化
2. $A$ 为实对称矩阵 $\Rightarrow$ $A$ 可对角化（且可正交对角化）

### 2.4 不可对角化的情形

若某个特征值的几何重数小于代数重数，则 $A$ 不可对角化。

**示例**：$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$

特征值 $\lambda = 1$（二重），$A - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，$r(A - I) = 1$。

几何重数 $= 2 - 1 = 1 < 2 =$ 代数重数，故 $A$ 不可对角化。

## 3. 对角化的步骤

### 3.1 步骤

1. 求出 $A$ 的所有特征值 $\lambda_1, \lambda_2, \ldots, \lambda_n$
2. 对每个特征值 $\lambda_i$，求 $(A - \lambda_i I)\boldsymbol{x} = 0$ 的基础解系
3. 判断是否有 $n$ 个线性无关的特征向量
4. 若有，以这 $n$ 个特征向量为列构造 $P$，则 $P^{-1}AP = \Lambda$

### 3.2 完整示例

将 $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}$ 对角化。

**步骤1**：特征值 $\lambda_1 = 1$，$\lambda_2 = 2$，$\lambda_3 = 3$。

**步骤2**：

对 $\lambda_1 = 1$：$(A - I)\boldsymbol{x} = 0$

$$\begin{pmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \\ 6 & -11 & 5 \end{pmatrix} \to \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & -5 & 5 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}$$

$\boldsymbol{x}_1 = (1, 1, 1)^T$

对 $\lambda_2 = 2$：$(A - 2I)\boldsymbol{x} = 0$

$$\begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 1 \\ 6 & -11 & 4 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & -1/4 \\ 0 & 1 & -1/2 \\ 0 & 0 & 0 \end{pmatrix}$$

$\boldsymbol{x}_2 = (1, 2, 4)^T$

对 $\lambda_3 = 3$：$(A - 3I)\boldsymbol{x} = 0$

$$\begin{pmatrix} -3 & 1 & 0 \\ 0 & -3 & 1 \\ 6 & -11 & 3 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & -1/9 \\ 0 & 1 & -1/3 \\ 0 & 0 & 0 \end{pmatrix}$$

$\boldsymbol{x}_3 = (1, 3, 9)^T$

**步骤3**：三个特征值互不相同，特征向量线性无关。

**步骤4**：

$$P = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 4 & 9 \end{pmatrix}, \quad \Lambda = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$

$P^{-1}AP = \Lambda$

## 4. 对角化的应用

### 4.1 求矩阵的幂

若 $A = P\Lambda P^{-1}$，则 $A^k = P\Lambda^k P^{-1}$。

**示例**：设 $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$，求 $A^{10}$。

$A$ 的特征值为 $1, 3$，特征向量 $(1, -1)^T, (1, 1)^T$。

$$P = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}, \quad \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}$$

$$A^{10} = P\Lambda^{10}P^{-1} = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & 3^{10} \end{pmatrix}\frac{1}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$$

$$= \frac{1}{2}\begin{pmatrix} 1 + 3^{10} & -1 + 3^{10} \\ -1 + 3^{10} & 1 + 3^{10} \end{pmatrix}$$

### 4.2 求矩阵多项式

若 $A = P\Lambda P^{-1}$，则 $f(A) = Pf(\Lambda)P^{-1}$。

### 4.3 解微分方程组

$\dfrac{d\boldsymbol{x}}{dt} = A\boldsymbol{x}$ 的通解为 $\boldsymbol{x}(t) = e^{At}\boldsymbol{x}(0)$。

若 $A = P\Lambda P^{-1}$，则 $e^{At} = Pe^{\Lambda t}P^{-1}$。

## 5. 典型例题

### 例1

设 $A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$，判断 $A$ 是否可对角化。

**解**：特征值 $\lambda_1 = 1$（二重），$\lambda_2 = 2$。

对 $\lambda_1 = 1$：$A - I = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix}$，$r(A - I) = 1$，几何重数 $= 3 - 1 = 2 = $ 代数重数。

对 $\lambda_2 = 2$：$A - 2I = \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$，$r(A - 2I) = 2$，几何重数 $= 3 - 2 = 1 = $ 代数重数。

$A$ 可对角化。

### 例2

设 $A \sim B$，$A$ 的特征值为 $1, 2, 3$，求 $B^{-1}$ 的特征值。

**解**：$B$ 与 $A$ 有相同的特征值 $1, 2, 3$。$B^{-1}$ 的特征值为 $1, 1/2, 1/3$。

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
| 矩阵对角化 | 027-MatrixDiagonalization | 本文自身 |
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
