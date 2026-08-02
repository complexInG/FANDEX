---
order: 60
title: 矩阵运算
module: 'linear-algebra'
category: 数学
difficulty: beginner
description: '从"表格数据运算"的直觉出发，讲解矩阵的加法、数乘、乘法（含不满足交换律与消去律的辨析）、转置与对称矩阵、方阵的幂与多项式、矩阵的迹。'
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/005-CramersRule'
  - 'linear-algebra/008-InverseMatrix'
  - 'linear-algebra/009-ElementaryTransformationAndMatrix'
prerequisites: []
---


## 0. 生活类比：表格数据的运算

想象你负责统计一家连锁店的月度销售：一张 Excel 表格，行是各门店，列是各品类。你想做的所有操作，几乎都能在矩阵运算里找到对应：

- 汇总两个月的销售额 → **矩阵加法**（对应位置相加）；
- 价格统一上调 10% → **矩阵数乘**（每个格子乘 1.1）；
- 已知"门店 × 单价"和"单价 × 数量"，求总销售额 → **矩阵乘法**（行乘列、求和）；
- 把"行是门店"翻转为"列是门店"（方便纵向对比）→ **矩阵转置**。

这个类比揭示了矩阵的本质：**矩阵是一张"数表"，运算是表与表之间的批量化操作**。上一模块你学了"行列式"（一个数），现在进入"矩阵"（一张表）的世界。两者最关键的区分：行列式算出来是一个**数**，矩阵本身是**表**；只有方阵才有行列式，而矩阵运算对任意长方形数表都成立。

同济版《线性代数》第 2 章"矩阵及其运算"正是从"线性方程组和矩阵"讲起，把方程组写成 $Ax = b$ 的紧凑形式，然后用矩阵运算整体处理。本文按"运算"主线组织：加、乘、转置、幂、迹，逐一定义、给示例、辨误区。

## 1. 矩阵是什么

### 1.1 定义

由 $m \times n$ 个数 $a_{ij}$ 排成的 $m$ 行 $n$ 列数表称为 **$m \times n$ 矩阵**，记作：

$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix} = (a_{ij})_{m \times n}$$

当 $m = n$ 时称为**方阵**，此时可以讨论行列式 $|A|$。

### 1.2 常用特殊矩阵

| 名称 | 定义 | 记号 |
| --- | --- | --- |
| 零矩阵 | 所有元素为零 | $O$ |
| 单位矩阵 | 主对角线为 1，其余为 0 的方阵 | $I$（或 $E$） |
| 对角矩阵 | 非主对角线元素全为零的方阵 | $\text{diag}(d_1, \ldots, d_n)$ |
| 数量矩阵 | $kI$（$k$ 为常数） | $kI$ |
| 上（下）三角矩阵 | 主对角线以下（上）全为零 | — |

单位矩阵 $I$ 是矩阵世界的"1"：$AI = IA = A$。

## 2. 矩阵加法与数乘

### 2.1 加法：对应位置相加

设 $A = (a_{ij})_{m \times n}$，$B = (b_{ij})_{m \times n}$，则：

$$A + B = (a_{ij} + b_{ij})_{m \times n}$$

**前提**：必须是**同型矩阵**（行数、列数分别相同）才能相加。

**运算律**：交换律 $A + B = B + A$；结合律 $(A + B) + C = A + (B + C)$；零矩阵 $A + O = A$；负矩阵 $A + (-A) = O$。

### 2.2 数乘：每个元素乘同一个数

设 $k$ 为常数，则 $kA = (ka_{ij})_{m \times n}$。

**运算律**：$k(A + B) = kA + kB$；$(k + l)A = kA + lA$；$(kl)A = k(lA)$；$1 \cdot A = A$。

**例 1**：设 $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$，$B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$，求 $2A + 3B$。

**解**：对应位置运算：

$$2A + 3B = \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} + \begin{pmatrix} 0 & 3 \\ 3 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 7 \\ 9 & 8 \end{pmatrix}$$

## 3. 矩阵乘法：行乘列，对位求和

### 3.1 定义

设 $A = (a_{ik})_{m \times s}$，$B = (b_{kj})_{s \times n}$，则乘积 $C = AB = (c_{ij})_{m \times n}$，其中：

$$c_{ij} = \sum_{k=1}^{s} a_{ik}b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{is}b_{sj}$$

**维度匹配规则**：$A$ 的**列数**必须等于 $B$ 的**行数**（都是 $s$）才能相乘；结果的形状是"$A$ 的行数 $\times$ $B$ 的列数"。

$$\underbrace{(m \times s)}_{A} \cdot \underbrace{(s \times n)}_{B} = \underbrace{(m \times n)}_{C}$$

**例 2**：设 $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$，$B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$，求 $AB$ 与 $BA$。

**解**：

$$AB = \begin{pmatrix} 1 \times 5 + 2 \times 7 & 1 \times 6 + 2 \times 8 \\ 3 \times 5 + 4 \times 7 & 3 \times 6 + 4 \times 8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

$$BA = \begin{pmatrix} 5 \times 1 + 6 \times 3 & 5 \times 2 + 6 \times 4 \\ 7 \times 1 + 8 \times 3 & 7 \times 2 + 8 \times 4 \end{pmatrix} = \begin{pmatrix} 23 & 34 \\ 31 & 46 \end{pmatrix}$$

$AB \neq BA$——这是矩阵乘法与普通乘法最根本的差异。

### 3.2 运算律（成立的）

1. **结合律**：$(AB)C = A(BC)$；
2. **分配律**：$A(B + C) = AB + AC$，$(A + B)C = AC + BC$；
3. **数乘结合**：$k(AB) = (kA)B = A(kB)$；
4. **单位矩阵**：$AI = IA = A$。

### 3.3 不成立的运算律（必考陷阱）

**陷阱一：交换律不成立** $AB \neq BA$（一般情况下）。

- $AB$ 有意义时 $BA$ 可能没意义（维度不匹配）；
- 即使都有意义，可能不同型；
- 即使同型，值也常不相等（如例 2）。

**陷阱二：消去律不成立**。$AB = AC$ 且 $A \neq O$，不能推出 $B = C$；$AB = O$ 也不能推出 $A = O$ 或 $B = O$。

**例 3**（零因子）：设 $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$，$B = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$，则：

$$AB = \begin{pmatrix} 1 \times 1 + 1 \times (-1) & 1 \times (-1) + 1 \times 1 \\ 1 \times 1 + 1 \times (-1) & 1 \times (-1) + 1 \times 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = O$$

但 $A \neq O$ 且 $B \neq O$。**两个非零矩阵相乘可能得到零矩阵**，这是"数"的世界里永远不会发生的事。

## 4. 矩阵的转置

### 4.1 定义

把 $A$ 的行与列互换得到 $A^T$：$(A^T)_{ij} = a_{ji}$。

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix} \Rightarrow A^T = \begin{pmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \end{pmatrix}$$

### 4.2 运算律

1. $(A^T)^T = A$；
2. $(A + B)^T = A^T + B^T$；
3. $(kA)^T = kA^T$；
4. $(AB)^T = B^TA^T$——**注意顺序反转**（"穿衣脱衣"法则：先穿的外套最后脱，先乘的矩阵最后转置）。

### 4.3 对称矩阵与反对称矩阵

- **对称矩阵**：$A^T = A$（$a_{ij} = a_{ji}$）；
- **反对称矩阵**：$A^T = -A$（$a_{ij} = -a_{ji}$，主对角线必为零）。

**两个重要结论**：

1. 任意方阵可拆成对称与反对称部分之和：$A = \dfrac{A + A^T}{2} + \dfrac{A - A^T}{2}$；
2. $AA^T$ 与 $A^TA$ 恒为对称矩阵（验证：$(AA^T)^T = (A^T)^TA^T = AA^T$）。

**例 4**：验证 $(AB)^T = B^TA^T$。设 $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$，$B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$。

**解**：$AB = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$，$(AB)^T = \begin{pmatrix} 19 & 43 \\ 22 & 50 \end{pmatrix}$；

$$B^TA^T = \begin{pmatrix} 5 & 7 \\ 6 & 8 \end{pmatrix}\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} = \begin{pmatrix} 19 & 43 \\ 22 & 50 \end{pmatrix}$$

两边相等，验证通过。

## 5. 方阵的幂与多项式

### 5.1 幂的定义

$A^k = \underbrace{A \cdot A \cdots A}_{k \text{ 个}}$，规定 $A^0 = I$。运算律：$A^k A^l = A^{k+l}$，$(A^k)^l = A^{kl}$。

**注意**：$(AB)^k \neq A^kB^k$（一般情况），原因还是交换律不成立。

### 5.2 求幂技巧：拆成"I + 幂零矩阵"

**例 5**：设 $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$，求 $A^n$。

**解**：把 $A$ 拆成 $I + B$，其中 $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$。计算 $B^2 = O$（幂零矩阵）。因为 $IB = BI$（$I$ 与任何矩阵可交换），可用二项式展开：

$$A^n = (I + B)^n = I + nB + \binom{n}{2}B^2 + \cdots = I + nB = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$$

**思路点拨**：$B^2 = O$ 使二项式展开"在第 2 项后截断"，这是处理幂零扰动的标准手法。

### 5.3 矩阵多项式

设 $f(x) = a_m x^m + \cdots + a_1 x + a_0$，则 $f(A) = a_m A^m + \cdots + a_1 A + a_0 I$。

**性质**：若 $A\boldsymbol{\alpha} = \lambda\boldsymbol{\alpha}$（$\lambda$ 为特征值），则 $f(A)\boldsymbol{\alpha} = f(\lambda)\boldsymbol{\alpha}$——矩阵多项式把特征值"代入"多项式，这是 025 文档的伏笔。

## 6. 矩阵的迹

### 6.1 定义

$n$ 阶方阵 $A = (a_{ij})$ 的**迹**为主对角线元素之和：

$$\text{tr}(A) = \sum_{i=1}^{n} a_{ii}$$

### 6.2 性质

1. $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$；
2. $\text{tr}(kA) = k\,\text{tr}(A)$；
3. $\text{tr}(A^T) = \text{tr}(A)$；
4. $\text{tr}(AB) = \text{tr}(BA)$（$A$ 为 $m \times n$，$B$ 为 $n \times m$——注意此时 $AB$ 是 $m$ 阶、$BA$ 是 $n$ 阶，但迹相等！）；
5. $\text{tr}(A) = \lambda_1 + \lambda_2 + \cdots + \lambda_n$（特征值之和）。

迹在深度学习中有直接应用：神经网络损失函数中常用 $\text{tr}(A^T B)$ 表示矩阵内积（Frobenius 内积），优化理论里到处可见。

## 7. 常见错误与对策

| 常见错误 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 两个维度不匹配的矩阵强行相乘 | 维度错误 | 没检查"前列 = 后行" | 相乘前先写维度：$(m\times s)(s\times n)$ 才合法 |
| 默认 $AB = BA$ | 交换律误用 | 把数的乘法习惯带进来 | 做乘法后随手验证：$AB$ 与 $BA$ 未必相等 |
| 由 $AB = O$ 推出 $A = O$ 或 $B = O$ | 消去律误用 | 不知"零因子"存在 | 记住例 3：非零矩阵乘积可能为零 |
| 由 $AB = AC$ 推出 $B = C$ | 消去律误用 | 数的世界里的"约分"习惯 | 矩阵乘法没有消去律；$A$ 可逆时才可"约"（见 008） |
| 转置乘积忘了反序：$(AB)^T$ 写成 $A^TB^T$ | 公式错误 | 顺序记忆混乱 | 记"穿衣脱衣"：后穿（先乘的）的先脱（先转置） |
| 把 $|AB|$ 与 $AB$ 混用 | 概念混淆 | 没区分矩阵与行列式 | $AB$ 是矩阵，$|AB| = |A||B|$ 是数（只对方阵） |

## 9. 一句话记忆

矩阵运算是"表"的批量化操作：**加法对位相加、数乘逐格放大、乘法行乘列求和、转置行列互换**——而"交换律与消去律双双失效"是它与普通数运算的最大分水岭。

### 延伸阅读

- 矩阵乘法的几何解释（线性变换的复合），见 001 行列式的几何意义部分与 024 向量空间示例。
- 转置与行列式的关系 $|A^T| = |A|$，见 002 行列式基本性质。
- 有了乘法，什么时候能"除"？见 008 逆矩阵。
