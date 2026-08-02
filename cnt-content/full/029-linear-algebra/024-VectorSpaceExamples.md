---
order: 45
title: 向量空间典型例题
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 用多项式空间、函数空间、矩阵空间等一组实例巩固向量空间概念，涵盖线性相关性判定、秩的计算、正交化、基与维数等题型，含 0 基础类比、完整例题、常见错误对策与实战练习。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/内积与正交性'
  - 'linear-algebra/施密特正交化'
  - 'linear-algebra/特征值与特征向量计算'
  - 'linear-algebra/特征值性质'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 0. 从一个生活场景说起：同样的拼插规则，不同的积木

乐高积木的玩法大家都懂：无论积木是红色、蓝色、是方砖还是长条，只要"拼插规则"一致，就能拼出各种结构。数学里的**向量空间**也是这样：元素（向量）可以是数字数组、可以是多项式、可以是矩阵、甚至可以是函数——长得完全不一样，但只要满足同样的运算规则（加法、数乘、封闭性），它们就都是"向量"，共享同一套理论。

本篇是"案例驱动"的综合篇：前面 019-023 篇讲了线性相关、基、坐标、内积、正交化，现在用一组跨越不同"积木类型"的实例，把这些概念串起来。你会看到：判断多项式线性相关和判断数组线性相关，用的竟是同一套方法——这恰恰是抽象（向量空间理论）的力量所在。

## 1. 案例总览：四类"积木"空间

| 空间 | 元素 | 加法 | 数乘 | 典型维数 |
| --- | --- | --- | --- | --- |
| $\mathbb{R}^n$ | $n$ 维实数组 | 逐分量相加 | 逐分量乘数 | $n$ |
| 多项式空间 $P_n$ | 次数 $\leq n$ 的多项式 | 多项式相加 | 多项式乘数 | $n+1$ |
| 矩阵空间 $M_{m \times n}$ | $m \times n$ 矩阵 | 矩阵相加 | 矩阵数乘 | $mn$ |
| 函数空间 | 某区间上的函数 | 函数相加 | 函数乘数 | 无穷（或依约束而定） |

核心规则（任何空间都要验证的三条）：**加法封闭、数乘封闭、加法满足结合律与交换律**。满足这些，集合就是向量空间。下面逐个用案例巩固。

## 2. 案例1：$\mathbb{R}^n$ 中的线性相关性

### 例1（含参数的相关性判定）

设 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 线性无关，判断 $k$ 为何值时，$\boldsymbol{\alpha}_2 - \boldsymbol{\alpha}_1$，$k\boldsymbol{\alpha}_3 - \boldsymbol{\alpha}_2$，$\boldsymbol{\alpha}_1 - \boldsymbol{\alpha}_3$ 线性相关。

**解**：设组合为零向量：

$$x_1(\boldsymbol{\alpha}_2 - \boldsymbol{\alpha}_1) + x_2(k\boldsymbol{\alpha}_3 - \boldsymbol{\alpha}_2) + x_3(\boldsymbol{\alpha}_1 - \boldsymbol{\alpha}_3) = 0$$

按 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 整理系数：

$$(-x_1 + x_3)\boldsymbol{\alpha}_1 + (x_1 - x_2)\boldsymbol{\alpha}_2 + (kx_2 - x_3)\boldsymbol{\alpha}_3 = 0$$

由 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 线性无关，各系数必须同时为零：

$$\begin{cases} -x_1 + x_3 = 0 \\ x_1 - x_2 = 0 \\ kx_2 - x_3 = 0 \end{cases}$$

新向量组线性相关 $\iff$ 该齐次方程组有非零解 $\iff$ 系数行列式为零：

$$\begin{vmatrix} -1 & 0 & 1 \\ 1 & -1 & 0 \\ 0 & k & -1 \end{vmatrix} = 1 - k$$

故 $k = 1$ 时行列式为零，新向量组线性相关；$k \neq 1$ 时线性无关。

**方法总结**：判断"组合后的向量组"的相关性，套路是——把组合展开，按原向量合并，利用"原向量组线性无关"把问题转化为齐次方程组的非零解问题。

### 例2（抽象矩阵与线性无关）

设 $A$ 为 $n$ 阶方阵，$\boldsymbol{\alpha}$ 为 $n$ 维非零列向量，$\boldsymbol{\alpha}, A\boldsymbol{\alpha}, A^2\boldsymbol{\alpha}$ 线性无关，且 $A^3\boldsymbol{\alpha} = 3A\boldsymbol{\alpha} - 2A^2\boldsymbol{\alpha}$，求 $|A + I|$。

**解**：由 $A^3\boldsymbol{\alpha} = 3A\boldsymbol{\alpha} - 2A^2\boldsymbol{\alpha}$ 移项得 $(A^3 + 2A^2 - 3A)\boldsymbol{\alpha} = 0$，即 $A(A^2 + 2A - 3I)\boldsymbol{\alpha} = 0$，因式分解得 $A(A + 3I)(A - I)\boldsymbol{\alpha} = 0$。

以 $\boldsymbol{\alpha}, A\boldsymbol{\alpha}, A^2\boldsymbol{\alpha}$ 为基，考察 $A$ 在这组基下的作用：

$$A\boldsymbol{\alpha} = 0\cdot\boldsymbol{\alpha} + 1\cdot A\boldsymbol{\alpha} + 0\cdot A^2\boldsymbol{\alpha}, \quad A(A\boldsymbol{\alpha}) = A^2\boldsymbol{\alpha}, \quad A(A^2\boldsymbol{\alpha}) = A^3\boldsymbol{\alpha} = 3A\boldsymbol{\alpha} - 2A^2\boldsymbol{\alpha}$$

故 $A$ 在基 $\boldsymbol{\alpha}, A\boldsymbol{\alpha}, A^2\boldsymbol{\alpha}$ 下的表示矩阵为：

$$B = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 3 \\ 0 & 1 & -2 \end{pmatrix}$$

于是 $|A + I| = |B + I| = \begin{vmatrix} 1 & 0 & 0 \\ 1 & 1 & 3 \\ 0 & 1 & -1 \end{vmatrix} = -4$。

**方法总结**：当题干出现"$\boldsymbol{\alpha}, A\boldsymbol{\alpha}, A^2\boldsymbol{\alpha}$ 线性无关"时，通常提示要以这组向量为基，把抽象的 $A$ 翻译成具体矩阵再计算。

## 3. 案例2：多项式空间（新视角）

### 例3（多项式线性无关性）

判断 $1$，$x$，$x^2$，$x^3$ 在多项式空间 $P_3$ 中是否线性无关；再判断 $1$，$x - 1$，$(x-1)^2$ 是否线性无关。

**解**：

(1) 设 $k_0 + k_1x + k_2x^2 + k_3x^3 = 0$（对所有 $x$ 成立）。一个非零三次多项式至多有 3 个根，不可能恒为零，故 $k_0 = k_1 = k_2 = k_3 = 0$，线性无关。

(2) 设 $c_1 + c_2(x-1) + c_3(x-1)^2 = 0$，展开整理：

$$(c_1 - c_2 + c_3) + (c_2 - 2c_3)x + c_3x^2 = 0$$

由 (1) 的结论，$c_3 = 0$，$c_2 - 2c_3 = c_2 = 0$，$c_1 - c_2 + c_3 = c_1 = 0$，线性无关。

**方法总结**：多项式的线性无关性归结为"各项系数全为零"。多项式空间 $P_n$ 的维数是 $n+1$，自然基是 $1, x, x^2, \ldots, x^n$。

### 例4（多项式空间的基与坐标）

证明 $1$，$x-1$，$(x-1)^2$ 构成 $P_2$ 的一组基，并求多项式 $p(x) = x^2 + 2x + 3$ 在该基下的坐标。

**解**：$P_2$ 维数为 3，上例已证 $1, x-1, (x-1)^2$ 线性无关，故构成基。设：

$$p(x) = a_1 + a_2(x-1) + a_3(x-1)^2 = a_3x^2 + (a_2 - 2a_3)x + (a_1 - a_2 + a_3)$$

对比系数：$a_3 = 1$，$a_2 - 2 = 2 \Rightarrow a_2 = 4$，$a_1 - 4 + 1 = 3 \Rightarrow a_1 = 6$。

坐标为 $(6, 4, 1)^T$。检验：$6 + 4(x-1) + (x-1)^2 = x^2 + 2x + 3$。正确。

## 4. 案例3：矩阵空间（新视角）

### 例5（矩阵空间的基与维数）

求 $2 \times 2$ 对称矩阵全体 $S = \{A \mid A^T = A\}$ 的一组基与维数。

**解**：设 $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$（对称性要求 $a_{12} = a_{21}$），任意元素形如：

$$A = a\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + b\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + c\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

三个"标准件"矩阵线性无关（每个只有一个独立参数），且张成整个 $S$，故 $\dim S = 3$，基可取上述三个矩阵。

**方法总结**：找矩阵空间的基，先写出通式（带自由参数），每个自由参数对应一个基元素。

### 例6（向量组的秩）

设 $\boldsymbol{\alpha}_1 = (1, 2, -1)^T$，$\boldsymbol{\alpha}_2 = (2, 4, \lambda)^T$，$\boldsymbol{\alpha}_3 = (1, \lambda, 1)^T$，求 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 的秩。

**解**：拼成矩阵 $A$ 做初等行变换：

$$A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & \lambda \\ -1 & \lambda & 1 \end{pmatrix} \xrightarrow{r_2-2r_1, \ r_3+r_1} \begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & \lambda-2 \\ 0 & \lambda+2 & 2 \end{pmatrix}$$

分情况讨论：

- $\lambda \neq 2$ 且 $\lambda \neq -2$：存在非零二阶子式，$r(A) = 3$；
- $\lambda = 2$：$\begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ 0 & 4 & 2 \end{pmatrix}$，$r(A) = 2$；
- $\lambda = -2$：$\begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & -4 \\ 0 & 0 & 2 \end{pmatrix}$，$r(A) = 2$。

**方法总结**：含参数的向量组秩问题，统一套路是"行变换 + 按参数分类讨论"，分类的分界点就是使某主元为零的参数值。

## 5. 案例4：解空间（零空间）

### 例7（零空间的基和维数）

求矩阵 $A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 6 & 8 \\ 1 & 1 & 1 & 1 \end{pmatrix}$ 的零空间 $N(A)$ 的基和维数。

**解**：行变换化行最简形：

$$A \to \begin{pmatrix} 1 & 2 & 3 & 4 \\ 0 & 0 & 0 & 0 \\ 0 & -1 & -2 & -3 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & -1 & -2 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

$r(A) = 2$，由秩-零度定理：$\dim(N(A)) = 4 - 2 = 2$。

同解方程组：$\begin{cases} x_1 = x_3 + 2x_4 \\ x_2 = -2x_3 - 3x_4 \end{cases}$。令自由变量 $x_3, x_4$ 取基础解系：

$$\boldsymbol{\xi}_1 = (1, -2, 1, 0)^T, \quad \boldsymbol{\xi}_2 = (2, -3, 0, 1)^T$$

$\boldsymbol{\xi}_1, \boldsymbol{\xi}_2$ 就是 $N(A)$ 的一组基。

### 例8（超平面子空间）

设 $V = \{(x_1, x_2, x_3)^T \mid x_1 + x_2 + x_3 = 0\}$，求 $V$ 的基和维数。

**解**：$V$ 是 $Ax = 0$ 的解空间，其中 $A = (1, 1, 1)$。$r(A) = 1$，$\dim(V) = 3 - 1 = 2$。

基础解系：$\boldsymbol{\xi}_1 = (-1, 1, 0)^T$，$\boldsymbol{\xi}_2 = (-1, 0, 1)^T$，即 $V$ 的一组基。

**几何含义**：$V$ 是过原点的平面（法向量 $(1,1,1)$），维数 2，与 $\mathbb{R}^3$ 中的"普通平面"同构。

### 例9（n 个无关向量必为基）

证明 $\mathbb{R}^n$ 中任意 $n$ 个线性无关的向量构成 $\mathbb{R}^n$ 的一组基。

**证明**：设 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_n$ 线性无关。对任意 $\boldsymbol{\beta} \in \mathbb{R}^n$，$\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_n, \boldsymbol{\beta}$ 是 $n+1$ 个 $n$ 维向量，必线性相关。故存在不全为零的 $k_1, \ldots, k_n, k_{n+1}$ 使：

$$k_1\boldsymbol{\alpha}_1 + \cdots + k_n\boldsymbol{\alpha}_n + k_{n+1}\boldsymbol{\beta} = 0$$

若 $k_{n+1} = 0$，则 $k_1\boldsymbol{\alpha}_1 + \cdots + k_n\boldsymbol{\alpha}_n = 0$，由 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_n$ 线性无关得 $k_1 = \cdots = k_n = 0$，与"不全为零"矛盾。故 $k_{n+1} \neq 0$，$\boldsymbol{\beta}$ 可由 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_n$ 线性表示。既然任意向量都能被它们表示，它们就是基。

## 6. 案例5：正交化与正交矩阵（综合）

### 例10（正交化综合）

对 $\boldsymbol{\alpha}_1 = (1, 1, 1)^T$，$\boldsymbol{\alpha}_2 = (1, 0, 1)^T$，$\boldsymbol{\alpha}_3 = (0, 1, 1)^T$ 进行施密特正交化并单位化。

**解**：

$\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1 = (1, 1, 1)^T$。

$\boldsymbol{\beta}_2 = \boldsymbol{\alpha}_2 - \frac{(\boldsymbol{\alpha}_2, \boldsymbol{\beta}_1)}{(\boldsymbol{\beta}_1, \boldsymbol{\beta}_1)}\boldsymbol{\beta}_1 = (1, 0, 1)^T - \frac{2}{3}(1, 1, 1)^T = \left(\frac{1}{3}, -\frac{2}{3}, \frac{1}{3}\right)^T$。

$\boldsymbol{\beta}_3$：先算系数 $(\boldsymbol{\alpha}_3, \boldsymbol{\beta}_1) = 2$，$(\boldsymbol{\alpha}_3, \boldsymbol{\beta}_2) = -\frac{2}{3} + \frac{1}{3} = -\frac{1}{3}$，$(\boldsymbol{\beta}_2, \boldsymbol{\beta}_2) = \frac{1}{9} + \frac{4}{9} + \frac{1}{9} = \frac{2}{3}$，则：

$$\boldsymbol{\beta}_3 = (0, 1, 1)^T - \frac{2}{3}(1, 1, 1)^T - \frac{-1/3}{2/3}\left(\frac{1}{3}, -\frac{2}{3}, \frac{1}{3}\right)^T = \left(-\frac{1}{2}, 0, \frac{1}{2}\right)^T$$

单位化：

$$\boldsymbol{e}_1 = \frac{1}{\sqrt{3}}(1, 1, 1)^T, \quad \boldsymbol{e}_2 = \frac{1}{\sqrt{6}}(1, -2, 1)^T, \quad \boldsymbol{e}_3 = \frac{1}{\sqrt{2}}(-1, 0, 1)^T$$

### 例11（正交矩阵 + 行列式）

设 $A$ 为 $n$ 阶正交矩阵，$|A| = 1$，$n$ 为奇数，证明 $|A - I| = 0$。

**证明**：利用 $A^T = A^{-1}$：

$$|A - I| = |A - AA^T| = |A(I - A^T)| = |A| \cdot |I - A^T| = |I - A^T|$$

而 $|I - A^T| = |(I - A)^T| = |I - A| = |-(A - I)| = (-1)^n|A - I| = -|A - I|$（$n$ 为奇数）。

故 $|A - I| = -|A - I|$，即 $2|A - I| = 0$，$|A - I| = 0$。

### 例12（构造正交矩阵）

设 $A$ 为三阶正交矩阵，$|A| = 1$，$\boldsymbol{\alpha} = (1, 0, 0)^T$，$A\boldsymbol{\alpha} = (0, 1, 0)^T$，求 $A$。

**解**：$A\boldsymbol{\alpha}$ 等于 $A$ 的第一列，故 $A$ 的第一列为 $(0, 1, 0)^T$。设：

$$A = \begin{pmatrix} 0 & a & d \\ 1 & b & e \\ 0 & c & f \end{pmatrix}$$

由 $A^TA = I$（列标准正交）得约束：第一列与第二列正交 $\Rightarrow b = 0$；第二列与第三列正交 $\Rightarrow ad + cf = 0$；第二列单位 $\Rightarrow a^2 + c^2 = 1$；第三列单位 $\Rightarrow d^2 + e^2 + f^2 = 1$；第一行单位 $\Rightarrow a^2 + d^2 = 1$。

由 $|A| = 1$ 按第一列展开：$|A| = -(af - cd) = -af + cd = 1$。

由 $a^2 + c^2 = 1$ 与 $a^2 + d^2 = 1$ 得 $c^2 = d^2$。令 $a = \cos\theta$，$c = \sin\theta$，结合 $ad + cf = 0$ 与 $|A| = 1$，可取 $d = -\sin\theta$，$f = \cos\theta$（另一组符号给出镜像解）。$e$ 由第三列单位确定：$\sin^2\theta + e^2 + \cos^2\theta = 1 \Rightarrow e = 0$。

$$A = \begin{pmatrix} 0 & \cos\theta & -\sin\theta \\ 1 & 0 & 0 \\ 0 & \sin\theta & \cos\theta \end{pmatrix}, \quad \theta \text{ 任意}$$

## 7. 常见错误与对策

| 常见错误 | 错误类型 | 原因 | 纠正方法 |
| --- | --- | --- | --- |
| 忘记 $P_n$ 维数是 $n+1$（不是 $n$） | 概念理解错误 | 多项式次数从 0 算起 | 次数 $\leq n$ 的多项式有 $n+1$ 个系数（含常数项），维数 $n+1$ |
| 判定多项式相关时只代一个 $x$ 值 | 方法错误 | 混淆"多项式函数恒零"与"在某点为零" | 多项式恒为零需所有系数为零；可对比系数或代入多个不同 $x$ 值 |
| 求子空间基时把自由参数个数当维数，漏掉约束 | 概念混淆 | 没先写出通式再数参数 | 先写通式（含自由参数），自由参数的个数才是维数 |
| 对 $N(A)$ 只算 $4 - r$ 不写基础解系 | 流程缺失 | 把维数当基 | 维数之外必须给出具体的线性无关解向量作为基 |
| 含参数题不分情况讨论就下结论 | 逻辑不严密 | 默认参数"一般位置" | 找出使主元为零的参数值，逐个分类；每类都要写出秩 |
| 把"$\boldsymbol{\alpha}, A\boldsymbol{\alpha}, A^2\boldsymbol{\alpha}$ 线性无关"当作多余条件 | 策略失误 | 没识别抽象矩阵题的信号 | 见到这类条件，考虑以它为基把 $A$ 具体化为矩阵 |

## 8. 实战练习

### 练习1（基础：矩阵空间维数）

求 $3 \times 3$ 上三角矩阵全体构成的向量空间的一组基与维数。

**提示**：上三角矩阵有 6 个独立位置（主对角线上方含对角线），每个位置对应一个"只有一个 1"的基矩阵。

**参考答案要点**：$\dim = 6$，基为 $E_{ij}$（$i \leq j$），共 6 个，其中 $E_{ij}$ 是第 $(i,j)$ 位置为 1、其余为 0 的矩阵。

### 练习2（进阶：多项式空间坐标）

求多项式 $p(x) = 2x^2 - 3x + 1$ 在基 $1, x+1, x^2$ 下的坐标。

**提示**：设 $p = a_1 + a_2(x+1) + a_3x^2$，按 $x$ 的幂合并同类项后对比系数。

**参考答案要点**：$(a_1 + a_2) + a_2x + a_3x^2 = 1 - 3x + 2x^2$，得 $a_3 = 2$，$a_2 = -3$，$a_1 = 4$，坐标为 $(4, -3, 2)^T$。

### 练习3（进阶：含参数秩）

设 $\boldsymbol{\alpha}_1 = (1, \lambda, 1)^T$，$\boldsymbol{\alpha}_2 = (\lambda, 1, 0)^T$，$\boldsymbol{\alpha}_3 = (1, 0, 0)^T$，讨论 $\lambda$ 取何值时它们线性相关、线性无关。

**提示**：三阶行列式为零时线性相关；先做列交换或行变换化简。

**参考答案要点**：$|A| = \begin{vmatrix} 1 & \lambda & 1 \\ \lambda & 1 & 0 \\ 1 & 0 & 0 \end{vmatrix} = -\lambda^2 + 1 = 1 - \lambda^2$。$\lambda = \pm 1$ 时线性相关（秩 2），否则线性无关（秩 3）。

### 练习4（综合：解空间）

求齐次方程组 $\begin{cases} x_1 + 2x_2 - x_3 + x_4 = 0 \\ 2x_1 + 4x_2 + x_3 - x_4 = 0 \end{cases}$ 的解空间的基与维数。

**提示**：系数矩阵是 $2 \times 4$，秩至多 2；行变换化行最简形后令自由变量取基础解系。

**参考答案要点**：$r = 2$，$\dim = 4 - 2 = 2$。基础解系可取 $\boldsymbol{\xi}_1 = (-2, 1, 0, 0)^T$，$\boldsymbol{\xi}_2 = (0, 0, -2, 1)^T$（由行最简形 $x_1 = -2x_2$，$x_3 = -2x_4$ 得）。

### 练习5（挑战：函数空间相关性）

判断函数 $f_1(t) = 1$，$f_2(t) = t$，$f_3(t) = t^2$ 在函数空间（全体实系数多项式）中是否线性相关；若相关，找出非平凡组合关系。

**提示**：设 $k_1 + k_2t + k_3t^2 = 0$ 对所有 $t$ 成立；或用 Wronskian 行列式判定。

**参考答案要点**：线性无关。设 $k_1 + k_2t + k_3t^2 = 0$，取 $t = 0$ 得 $k_1 = 0$；求导取 $t = 0$ 得 $k_2 = 0$；再求导得 $k_3 = 0$。故无非平凡组合关系。

## 9. 一句话记忆

**向量空间的核心是"运算规则"而非"元素长相"：多项式、矩阵、函数只要满足加法与数乘封闭就都是向量，线性相关、基、维数、正交化这些工具对它们一律通用。**

## 参考链接与延伸阅读

- 同济大学数学科学学院《工程数学 线性代数（第七版）》，高等教育出版社，第 4 章 §4 向量空间、第 5 章 §1 内积与正交性（向量空间与正交化例题来源）：https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=630508ea938b7cc2960ef14b
- LibreTexts Linear Algebra（向量空间的例子：多项式、矩阵、函数空间）：https://math.libretexts.org/Bookshelves/Linear_Algebra/Linear_Algebra_with_Applications_(Nicholson)/05%3A_Vector_Space_R_%E2%84%9D
- MIT 18.06 Linear Algebra（Strang 第 6 讲列空间与零空间，第 9 讲线性无关、基与维数）：https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Interactive Linear Algebra（Georgia Tech，§3.2 零空间与列空间，§3.5 子空间与基）：https://textbooks.math.gatech.edu/ila/
- 3Blue1Brown 线性代数的本质（抽象向量空间的直观解释）：https://www.3blue1brown.com/topics/linear-algebra

延伸阅读：线性相关性、基与维数（前置知识）；内积与正交性、施密特正交化（正交化工具）；特征值与特征向量计算（向量空间理论在"空间变形"问题中的应用）。
