---
order: 100
title: 分块矩阵
module: 'linear-algebra'
category: 数学
difficulty: intermediate
description: 分块矩阵的概念与分块原则，分块矩阵的运算（加法、乘法、转置），分块对角矩阵的性质，分块矩阵的求逆与行列式，Schur 补与典型例题。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'linear-algebra/008-ElementaryTransformationAndMatrix'
  - 'linear-algebra/009-MatrixRank'
  - 'linear-algebra/011-GaussianElimination'
prerequisites: []
---


## 0. 从"大表格分区管理"说起

假设你是一家连锁超市的运营主管，手上有全国 200 家门店、每个门店 50 个品类的月度销售报表。这张大表有 200 行、50 列，直接整体管理既难读又难算。你自然会把它按"华东 / 华北 / 华南"分区，或者按"生鲜 / 日用 / 电器"分区：每个分区是一个小表格，整体报表就是"小表格组成的表格"。

矩阵也一样。一个 $100 \times 100$ 的大矩阵，如果内部天然存在"零块""单位块""重复块"等结构，把它们看作整体、当作新的元素来运算，往往比逐元素计算省力得多。这就是**分块矩阵（block matrix）**的出发点：**先分区，再以子块为元素做运算**。

分块不是把问题变复杂，而是"把大表格分成小板块管理"——这是本文（也是同济版《线性代数》第 2 章 §5"矩阵分块法"）要讲的核心思想。

## 1. 分块矩阵的概念

### 1.1 定义

用若干条横线和竖线将矩阵 $A$ 分成若干小块，每一小块称为 $A$ 的一个**子矩阵（子块）**。以子矩阵为元素的矩阵，称为 $A$ 的一个**分块矩阵**。

例如把 $4 \times 4$ 矩阵按下图方式切成 2 行 2 列共 4 块：

$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix} = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}$$

其中 $A_{11} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$ 等四个子块。分块方式不是唯一的：同一矩阵可以按不同的行列切分方式得到不同的分块结构，如何切取决于**运算需要与结构利用**。

### 1.2 分块的原则

分块必须保证后续运算"有意义"，这是分块唯一的原则：

- **分块加法**：两个矩阵的分块方式必须相同，且对应子块同型（行数、列数分别相等）；
- **分块乘法**：左矩阵 $A$ 的**列分法**必须与右矩阵 $B$ 的**行分法**完全一致（这是子块乘法的"内层维度匹配"要求）。

类比到门店报表：要合并两张报表，必须按同样的分区方式切；要让"分区的销售矩阵"乘"单品的价格向量"，分区的口径必须对齐。

## 2. 分块矩阵的运算

### 2.1 分块加法与数乘

设 $A$、$B$ 同型且分块方式相同：

$$A + B = \begin{pmatrix} A_{11} + B_{11} & A_{12} + B_{12} \\ A_{21} + B_{21} & A_{22} + B_{22} \end{pmatrix}, \qquad kA = \begin{pmatrix} kA_{11} & kA_{12} \\ kA_{21} & kA_{22} \end{pmatrix}$$

分块加法和数乘与普通矩阵完全类似，只是"元素"换成了子块。

### 2.2 分块乘法

设 $A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}$，$B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix}$，且 $A$ 的列分法与 $B$ 的行分法一致，则：

$$AB = \begin{pmatrix} A_{11}B_{11} + A_{12}B_{21} & A_{11}B_{12} + A_{12}B_{22} \\ A_{21}B_{11} + A_{22}B_{21} & A_{21}B_{12} + A_{22}B_{22} \end{pmatrix}$$

它和普通 2 阶矩阵乘法的"行乘列"模式一模一样。**唯一的注意点**：子矩阵乘法不满足交换律，$A_{ij}B_{jk}$ 绝不允许写成 $B_{jk}A_{ij}$，书写顺序必须严格保持。

### 2.3 分块转置

$$\begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}^{T} = \begin{pmatrix} A_{11}^{T} & A_{21}^{T} \\ A_{12}^{T} & A_{22}^{T} \end{pmatrix}$$

分块转置有"双重转置"：先按分块位置整体转置（行列互换），**每个子块内部还要再转置一次**。这是新手最容易漏掉的一步。

### 2.4 一个完整的算例

**例 1**（分块乘法验证）：设

$$A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 0 & 0 & 4 \end{pmatrix} = \begin{pmatrix} I_2 & C \\ O & 4 \end{pmatrix}, \qquad C = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$$

求 $A^2$。

**解**：利用分块乘法：

$$A^2 = \begin{pmatrix} I_2 & C \\ O & 4 \end{pmatrix}\begin{pmatrix} I_2 & C \\ O & 4 \end{pmatrix} = \begin{pmatrix} I_2^2 + CO & I_2C + C \cdot 4 \\ OI_2 + 4O & OC + 16 \end{pmatrix} = \begin{pmatrix} I_2 & 5C \\ O & 16 \end{pmatrix}$$

于是 $A^2 = \begin{pmatrix} 1 & 0 & 10 \\ 0 & 1 & 15 \\ 0 & 0 & 16 \end{pmatrix}$。验证：直接逐元素算 $A^2$ 得到相同结果。这里 $I_2C + 4C = 5C$ 正是利用了单位块与常数块，整个计算只需 2 个"元素级"乘法。

## 3. 分块对角矩阵

### 3.1 定义

如果分块后，非对角位置全是零块：

$$A = \begin{pmatrix} A_1 & & & \\ & A_2 & & \\ & & \ddots & \\ & & & A_s \end{pmatrix}$$

则称 $A$ 为**分块对角矩阵**，记作 $A = \mathrm{diag}(A_1, A_2, \ldots, A_s)$。它像是把几个独立的小系统"放在一条对角线上互不干扰"。

### 3.2 性质

分块对角矩阵的运算可以"逐块独立进行"，这是它最大的价值：

1. **行列式**：$|A| = |A_1||A_2|\cdots|A_s|$
2. **乘法**：$\mathrm{diag}(A_1,\ldots,A_s)\,\mathrm{diag}(B_1,\ldots,B_s) = \mathrm{diag}(A_1B_1,\ldots,A_sB_s)$（要求对应子块可乘）
3. **幂**：$A^k = \mathrm{diag}(A_1^k,\ldots,A_s^k)$
4. **逆**：若每个 $A_i$ 可逆，则 $A^{-1} = \mathrm{diag}(A_1^{-1},\ldots,A_s^{-1})$
5. **秩**：$r(A) = r(A_1) + \cdots + r(A_s)$

### 3.3 例 2（利用分块求高次幂）

设 $A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix}$，求 $A^{10}$。

**解**：$A = \mathrm{diag}(2, 3, 1)$，由幂的性质：

$$A^{10} = \mathrm{diag}(2^{10}, 3^{10}, 1^{10}) = \begin{pmatrix} 1024 & 0 & 0 \\ 0 & 59049 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

若不用分块，需要做 10 次 $3 \times 3$ 矩阵乘法；用分块后每个子块（此时是数）独立求幂即可。这也是数值计算中"结构化矩阵"（如对角块系统）能被高效处理的原因。

## 4. 分块矩阵的求逆

### 4.1 分块对角与分块三角

分块对角：$\begin{pmatrix} A & O \\ O & B \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} & O \\ O & B^{-1} \end{pmatrix}$。

分块上三角：$\begin{pmatrix} A & C \\ O & B \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} & -A^{-1}CB^{-1} \\ O & B^{-1} \end{pmatrix}$，其中 $A, B$ 可逆。

**验证**（上三角情形）：

$$\begin{pmatrix} A & C \\ O & B \end{pmatrix}\begin{pmatrix} A^{-1} & -A^{-1}CB^{-1} \\ O & B^{-1} \end{pmatrix} = \begin{pmatrix} AA^{-1} & -AA^{-1}CB^{-1} + CB^{-1} \\ O & BB^{-1} \end{pmatrix} = \begin{pmatrix} I & -CB^{-1} + CB^{-1} \\ O & I \end{pmatrix} = I$$

类似地，分块下三角：$\begin{pmatrix} A & O \\ C & B \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} & O \\ -B^{-1}CA^{-1} & B^{-1} \end{pmatrix}$。

### 4.2 一般分块矩阵的逆与 Schur 补

对于 $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$，若 $A$ 可逆，先用"分块消元"把左下角消成零块：

$$\begin{pmatrix} I & O \\ -CA^{-1} & I \end{pmatrix}\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} A & B \\ O & D - CA^{-1}B \end{pmatrix}$$

称 $S = D - CA^{-1}B$ 为 $A$ 的 **Schur 补**。若 $S$ 也可逆，则：

$$\begin{pmatrix} A & B \\ C & D \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} + A^{-1}BS^{-1}CA^{-1} & -A^{-1}BS^{-1} \\ -S^{-1}CA^{-1} & S^{-1} \end{pmatrix}$$

Schur 补在数值线性代数（如高斯消元的分块版本、置信区间计算、条件分布）中反复出现，是"大矩阵问题分解为小矩阵问题"的核心工具。

## 5. 分块矩阵的行列式

- 分块对角 / 分块三角（$A$ 或 $B$ 为方阵且另一侧为 $O$）：

$$\begin{vmatrix} A & O \\ O & B \end{vmatrix} = |A||B|, \qquad \begin{vmatrix} A & C \\ O & B \end{vmatrix} = |A||B|$$

- 一般情形（$A$ 可逆时）：$\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |A| \cdot |D - CA^{-1}B|$

- 一般情形（$D$ 可逆时）：$\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |D| \cdot |A - BD^{-1}C|$

注意：只有分块对角 / 三角时行列式才能直接写成子块行列式之积；一般分块矩阵**不能**直接写成 $|A||D|$，必须借助 Schur 补。

**例 3**：设 $A$ 为 $m$ 阶可逆矩阵，$D$ 为 $n$ 阶可逆矩阵，$B$ 为 $m \times n$ 矩阵。证明 $\begin{pmatrix} A & B \\ O & D \end{pmatrix}$ 可逆，并求其逆。

**解**：$|A| \neq 0$，$|D| \neq 0$，由分块三角行列式公式 $\left|\begin{pmatrix} A & B \\ O & D \end{pmatrix}\right| = |A||D| \neq 0$，故矩阵可逆。

设其逆为 $\begin{pmatrix} X & Y \\ Z & W \end{pmatrix}$，则：

$$\begin{pmatrix} A & B \\ O & D \end{pmatrix}\begin{pmatrix} X & Y \\ Z & W \end{pmatrix} = \begin{pmatrix} I_m & O \\ O & I_n \end{pmatrix}$$

展开得：$DZ = O$，$DW = I_n$，故 $Z = O$，$W = D^{-1}$；再由 $AX + BZ = I_m$ 得 $X = A^{-1}$，由 $AY + BW = O$ 得 $AY = -BD^{-1}$，即 $Y = -A^{-1}BD^{-1}$。因此：

$$\begin{pmatrix} A & B \\ O & D \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} & -A^{-1}BD^{-1} \\ O & D^{-1} \end{pmatrix}$$

这与 4.1 节公式一致。本题是考研与竞赛中的高频题，核心是"设逆、列方程、解子块"三步。

## 6. 分块矩阵的应用

### 6.1 线性方程组的分块形式

$$Ax = b \quad \Longleftrightarrow \quad \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}$$

把未知量分组后，方程组按"块"进行消元，这在求解大规模稀疏方程组（如电网潮流、有限元方程）时是分治算法的数学基础。

### 6.2 块对角系统的高效求解

若 $A = \mathrm{diag}(A_1, A_2, \ldots, A_s)$ 且每个 $A_i$ 可逆，则方程 $Ax = b$ 的解为 $x_i = A_i^{-1}b_i$（$i = 1, \ldots, s$），一个大型问题被拆成 $s$ 个互不相关的子问题，可以并行求解。这正是"分块驱动"思想在工程中的落地：**结构即算法**。

## 7. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 分块乘法写成 $B_{jk}A_{ij}$ | 运算律误用 | 子矩阵乘法不满足交换律 | 严格保持"左乘"顺序，$A_{ij}B_{jk}$ 中 $A$ 必须在左 |
| 分块转置只换块位置、子块不转置 | 转置理解偏差 | 把子块当成数 | 先整体转置，再对每个子块转置 |
| 分块时 $A$ 的列分法与 $B$ 的行分法不一致 | 分块前提错误 | 忽略"内层维度匹配" | 切分前先约定：$A$ 每块的列数 = $B$ 每块的行数 |
| 把一般分块矩阵行列式写成 $|A_{11}||A_{22}|$ | 公式滥用 | 分块三角公式只适用于有一角为零块的情形 | 用 Schur 补公式：$|A||D - CA^{-1}B|$ |
| 分块对角求逆时直接写各块逆但漏了可逆条件 | 条件缺失 | 子块不可逆时整体公式不成立 | 先验证每个对角子块可逆 |
| 把零块、单位块当普通元素随便交换 | 结构误读 | 混淆"块"与"数" | 先展开成小块，验证再收拢 |

## 9. 一句话记忆

> **分块矩阵就是把"矩阵中的矩阵"当元素来运算——先按需切块，再逐块运算；分块对角矩阵的一切运算都可以逐块独立进行。**
