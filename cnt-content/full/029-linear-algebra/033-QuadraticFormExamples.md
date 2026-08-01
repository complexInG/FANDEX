---
order: 63
title: 二次型典型例题
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 二次型典型例题集锦，涵盖标准形与规范形、正定性判定、合同判定、含参数二次型等题型。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'linear-algebra/二次型的规范形'
  - 'linear-algebra/正定二次型'
  - 'linear-algebra/LU分解'
  - 'linear-algebra/QR分解'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 1. 化标准形与规范形

### 例1

用配方法将 $f = x_1^2 - 2x_2^2 + x_3^2 + 2x_1x_2 + 4x_1x_3 + 2x_2x_3$ 化为标准形和规范形。

**解**：

$f = (x_1 + x_2 + 2x_3)^2 - x_2^2 - 4x_3^2 - 4x_2x_3 - 2x_2^2 + x_3^2 + 2x_2x_3$

$= (x_1 + x_2 + 2x_3)^2 - 3x_2^2 - 2x_2x_3 - 3x_3^2$

$= (x_1 + x_2 + 2x_3)^2 - 3(x_2 + \frac{1}{3}x_3)^2 + \frac{1}{3}x_3^2 - 3x_3^2$

$= (x_1 + x_2 + 2x_3)^2 - 3(x_2 + \frac{1}{3}x_3)^2 - \frac{8}{3}x_3^2$

标准形：$f = y_1^2 - 3y_2^2 - \frac{8}{3}y_3^2$

规范形：$f = z_1^2 - z_2^2 - z_3^2$

正惯性指数 $p = 1$，负惯性指数 $q = 2$。

### 例2

用正交变换将 $f = 2x_1^2 + 5x_2^2 + 5x_3^2 + 4x_1x_2 - 4x_1x_3 - 8x_2x_3$ 化为标准形。

**解**：

$$A = \begin{pmatrix} 2 & 2 & -2 \\ 2 & 5 & -4 \\ -2 & -4 & 5 \end{pmatrix}$$

$$|A - \lambda I| = \begin{vmatrix} 2-\lambda & 2 & -2 \\ 2 & 5-\lambda & -4 \\ -2 & -4 & 5-\lambda \end{vmatrix} = (10-\lambda)(1-\lambda)^2$$

$\lambda_1 = 10$，$\lambda_2 = \lambda_3 = 1$

标准形：$f = 10y_1^2 + y_2^2 + y_3^2$

## 2. 正定性判定

### 例3

判断 $f = x_1^2 + 4x_2^2 + x_3^2 + 2tx_1x_2 + 2x_1x_3 + 6x_2x_3$ 的正定性。

**解**：

$$A = \begin{pmatrix} 1 & t & 1 \\ t & 4 & 3 \\ 1 & 3 & 1 \end{pmatrix}$$

$\Delta_1 = 1 > 0$

$\Delta_2 = 4 - t^2 > 0 \Rightarrow |t| < 2$

$\Delta_3 = |A| = 1(4-9) - t(t-3) + 1(3t-4) = -5 - t^2 + 3t + 3t - 4 = -t^2 + 6t - 9 = -(t-3)^2$

$\Delta_3 = -(t-3)^2 \leq 0$，等号在 $t = 3$ 时成立。

但 $t = 3$ 时 $\Delta_2 = 4 - 9 = -5 < 0$，不满足。

故对任何 $t$，$f$ 都不是正定的。

### 例4

设 $A$ 为 $n$ 阶正定矩阵，$B$ 为 $n$ 阶半正定矩阵，证明 $A + B$ 正定。

**证明**：对任意 $\boldsymbol{x} \neq 0$：

$\boldsymbol{x}^T(A+B)\boldsymbol{x} = \boldsymbol{x}^TA\boldsymbol{x} + \boldsymbol{x}^TB\boldsymbol{x}$

$A$ 正定：$\boldsymbol{x}^TA\boldsymbol{x} > 0$

$B$ 半正定：$\boldsymbol{x}^TB\boldsymbol{x} \geq 0$

故 $\boldsymbol{x}^T(A+B)\boldsymbol{x} > 0$，$A + B$ 正定。

## 3. 合同判定

### 例5

判断 $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ 与 $B = \begin{pmatrix} -1 & 2 \\ 2 & -1 \end{pmatrix}$ 是否合同。

**解**：$A$ 的特征值为 $3, -1$，$p = 1, q = 1$。

$B$ 的特征值为 $1, -3$，$p = 1, q = 1$。

$p$ 和 $q$ 相同，故 $A$ 与 $B$ 合同。

### 例6

设 $A$ 为三阶实对称矩阵，$r(A) = 2$，$f = \boldsymbol{x}^TA\boldsymbol{x}$ 的规范形为 $y_1^2 - y_2^2$，求 $A$ 的特征值。

**解**：规范形为 $y_1^2 - y_2^2$，正惯性指数 $p = 1$，负惯性指数 $q = 1$，秩 $r = 2$。

$A$ 的特征值为 $\lambda_1 > 0$，$\lambda_2 < 0$，$\lambda_3 = 0$。

具体值无法确定，但符号为正、负、零。

## 4. 含参数二次型

### 例7

设 $f = x_1^2 + x_2^2 + x_3^2 + 2\lambda x_1x_2 + 2x_1x_3 + 2\mu x_2x_3$，当 $\lambda, \mu$ 满足什么条件时，$f$ 正定？

**解**：

$$A = \begin{pmatrix} 1 & \lambda & 1 \\ \lambda & 1 & \mu \\ 1 & \mu & 1 \end{pmatrix}$$

$\Delta_1 = 1 > 0$

$\Delta_2 = 1 - \lambda^2 > 0 \Rightarrow |\lambda| < 1$

$\Delta_3 = |A| = 1(1 - \mu^2) - \lambda(\lambda - \mu) + 1(\lambda\mu - 1) = 1 - \mu^2 - \lambda^2 + \lambda\mu + \lambda\mu - 1 = 2\lambda\mu - \lambda^2 - \mu^2 = -(\lambda - \mu)^2$

$\Delta_3 > 0 \Rightarrow -(\lambda - \mu)^2 > 0$，不可能！

故 $f$ 不可能正定（除非 $\lambda = \mu$ 且 $\Delta_3 = 0$，此时半正定）。

实际上，$|A| = -(\lambda - \mu)^2 \leq 0$，$f$ 不可能正定。

### 例8

设二次型 $f(x_1, x_2, x_3) = (1 - a)x_1^2 + (1 - a)x_2^2 + 2x_3^2 + 2(1 + a)x_1x_2$ 的秩为 2，求 $a$ 及正惯性指数。

**解**：

$$A = \begin{pmatrix} 1-a & 1+a & 0 \\ 1+a & 1-a & 0 \\ 0 & 0 & 2 \end{pmatrix}$$

$|A| = 2[(1-a)^2 - (1+a)^2] = 2[(1-2a+a^2) - (1+2a+a^2)] = 2 \cdot (-4a) = -8a$

$r(A) = 2 \Rightarrow |A| = 0 \Rightarrow a = 0$

当 $a = 0$ 时：$A = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$

$r(A) = 2$

特征值：$\begin{vmatrix} 1-\lambda & 1 & 0 \\ 1 & 1-\lambda & 0 \\ 0 & 0 & 2-\lambda \end{vmatrix} = (2-\lambda)[(1-\lambda)^2 - 1] = (2-\lambda)\lambda(\lambda - 2) = -\lambda(2-\lambda)^2$

$\lambda_1 = 0$，$\lambda_2 = 2$（二重）

正惯性指数 $p = 2$。

## 5. 综合证明题

### 例9

设 $A$ 为 $n$ 阶实对称矩阵，证明 $A$ 正定 $\iff$ 存在可逆矩阵 $B$ 使得 $A = B^TB$。

**证明**：

$\Rightarrow$：$A$ 正定，合同于 $I$，存在可逆 $C$ 使得 $C^TAC = I$，$A = (C^{-1})^TC^{-1}$，取 $B = C^{-1}$。

$\Leftarrow$：$A = B^TB$，$\boldsymbol{x}^TA\boldsymbol{x} = \boldsymbol{x}^TB^TB\boldsymbol{x} = \|B\boldsymbol{x}\|^2 \geq 0$。$B$ 可逆，$\boldsymbol{x} \neq 0 \Rightarrow B\boldsymbol{x} \neq 0 \Rightarrow \|B\boldsymbol{x}\|^2 > 0$。$A$ 正定。

### 例10

设 $A$ 为 $n$ 阶正定矩阵，$\boldsymbol{x}^TA\boldsymbol{x} = 1$ 表示 $\mathbb{R}^n$ 中的椭球面，证明该椭球面的体积为 $V = \dfrac{\omega_n}{\sqrt{|A|}}$，其中 $\omega_n$ 是单位球的体积。

**证明**：$A = Q\Lambda Q^T$，令 $\boldsymbol{x} = Q\Lambda^{-1/2}\boldsymbol{y}$，则 $\boldsymbol{x}^TA\boldsymbol{x} = \boldsymbol{y}^T\boldsymbol{y} = 1$。

变换的雅可比行列式为 $|Q\Lambda^{-1/2}| = |\Lambda|^{-1/2} = |A|^{-1/2}$。

$V = \omega_n \cdot |A|^{-1/2} = \dfrac{\omega_n}{\sqrt{|A|}}$。

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
| 实对称矩阵的对角化 | 028-RealSymmetricMatrixDiagonalization | 本文的并列主题 |
| 特征值典型例题 | 029-EigenvalueExamples | 本文的并列主题 |
| 二次型的标准形 | 030-QuadraticFormStandardForm | 本文的并列主题 |
| 二次型的规范形 | 031-QuadraticFormCanonicalForm | 本文的并列主题 |
| 正定二次型 | 032-PositiveDefiniteQuadraticForm | 本文的并列主题 |
| 二次型典型例题 | 033-QuadraticFormExamples | 本文自身 |
| LU分解 | 034-LU | 本文的并列主题 |
| QR分解 | 035-QR | 本文的并列主题 |
| 奇异值分解SVD | 036-SVD | 本文的并列主题 |
| 矩阵分解应用 | 037-MatrixDecompositionApplication | 本文的并列主题 |
