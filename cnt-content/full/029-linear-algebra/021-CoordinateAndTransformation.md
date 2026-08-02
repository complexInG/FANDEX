---
order: 42
title: 坐标与坐标变换
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 向量在基下的坐标，基变换与过渡矩阵，坐标变换公式，不同基下坐标的关系，含 0 基础类比、完整例题、常见错误对策与实战练习。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/线性相关性'
  - 'linear-algebra/基与维数'
  - 'linear-algebra/内积与正交性'
  - 'linear-algebra/施密特正交化'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 0. 从一个生活场景说起：同一座城市，不同的地图坐标

假设你手里有三张地图：一张是世界地图，一张是中国地图，一张是北京城市地图。同一个天安门广场，在三张地图上都能找到，但它在每张地图上的"坐标"（格网编号）完全不同——这是因为三张地图的**坐标系（基准线）不一样**。

向量空间里也是这样：同一个向量 $\boldsymbol{\alpha}$，在不同基（可以理解为不同的"坐标轴框架"）下，写出来的坐标数字是完全不同的。本篇的核心问题就是：

1. 给定一组基，怎么求出向量的坐标？
2. 换一组基，坐标怎么跟着变？
3. 变过去之后，还能不能"换算"回来？

把这三个问题搞清楚，你就掌握了线性代数里非常实用的一件工具：**坐标变换**。后面学特征值、对角化（换坐标系把矩阵变简单）都要用到它。

## 1. 向量的坐标

### 1.1 坐标的定义（先直观理解）

在平面上，我们说向量 $\boldsymbol{\alpha} = (3, 2)$，默认的潜台词是：$\boldsymbol{\alpha} = 3 \times \text{东向单位向量} + 2 \times \text{北向单位向量}$。这里的"东"和"北"就是一组**基**。

更一般地，设 $\boldsymbol{\varepsilon}_1, \boldsymbol{\varepsilon}_2, \ldots, \boldsymbol{\varepsilon}_n$ 是 $n$ 维向量空间 $V$ 的一组基，对于任意 $\boldsymbol{\alpha} \in V$，存在唯一的一组数 $x_1, x_2, \ldots, x_n$，使得：

$$\boldsymbol{\alpha} = x_1\boldsymbol{\varepsilon}_1 + x_2\boldsymbol{\varepsilon}_2 + \cdots + x_n\boldsymbol{\varepsilon}_n$$

称 $(x_1, x_2, \ldots, x_n)^T$ 为 $\boldsymbol{\alpha}$ 在基 $\boldsymbol{\varepsilon}_1, \ldots, \boldsymbol{\varepsilon}_n$ 下的**坐标**。

直观理解：坐标就是"按这组基的分量各取多少"。坐标的每一个分量 $x_i$，本质上是一个"系数"——它告诉我们把第 $i$ 个基向量放大 $x_i$ 倍后拼起来，就能得到 $\boldsymbol{\alpha}$。

### 1.2 坐标的唯一性（为什么基要线性无关）

坐标之所以"唯一"，依赖的是基的**线性无关性**。假设存在两组坐标 $x$ 与 $y$ 都表示同一个 $\boldsymbol{\alpha}$，则：

$$\sum_{i=1}^{n}(x_i - y_i)\boldsymbol{\varepsilon}_i = \mathbf{0}$$

由基线性无关，只能 $x_i = y_i$（$i = 1, \ldots, n$）。所以同一向量在**同一组基**下的坐标是唯一的；但同一个向量在**不同基**下的坐标不同（这一点正是本篇第 3 节的主题）。

### 1.3 自然基下的坐标（最舒服的坐标系）

在自然基 $\boldsymbol{e}_1 = (1, 0, \ldots, 0)^T, \ldots, \boldsymbol{e}_n = (0, \ldots, 0, 1)^T$ 下，向量 $\boldsymbol{\alpha} = (a_1, a_2, \ldots, a_n)^T$ 的坐标就是 $(a_1, a_2, \ldots, a_n)^T$ 本身。这是因为：

$$\boldsymbol{\alpha} = a_1\boldsymbol{e}_1 + a_2\boldsymbol{e}_2 + \cdots + a_n\boldsymbol{e}_n$$

自然基下"向量就是坐标"，这也是大家平时最习惯的写法。而一旦换到别的基，坐标就会"面目全非"，这正是坐标变换要解决的问题。

### 1.4 坐标的求法（把基拼成矩阵）

设基矩阵 $E = (\boldsymbol{\varepsilon}_1, \boldsymbol{\varepsilon}_2, \ldots, \boldsymbol{\varepsilon}_n)$（把基向量按列排成的矩阵），则坐标 $x$ 满足：

$$\boldsymbol{\alpha} = Ex \quad \Rightarrow \quad x = E^{-1}\boldsymbol{\alpha}$$

注意：$E$ 的列是基向量，基线性无关 $\Rightarrow |E| \neq 0 \Rightarrow E$ 可逆，所以 $x = E^{-1}\boldsymbol{\alpha}$ 总是能算出来。

**示例**：设 $\boldsymbol{\varepsilon}_1 = (1, 1)^T$，$\boldsymbol{\varepsilon}_2 = (1, -1)^T$，求 $\boldsymbol{\alpha} = (3, 1)^T$ 在此基下的坐标。

第一步，拼基矩阵并求逆：

$$E = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad E^{-1} = \frac{1}{-2}\begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix}$$

第二步，左乘求坐标：

$$x = E^{-1}\boldsymbol{\alpha} = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{pmatrix}\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$

第三步，检验（这一步非常重要，能发现低级错误）：

$$\boldsymbol{\alpha} = 2\boldsymbol{\varepsilon}_1 + 1\boldsymbol{\varepsilon}_2 = 2(1, 1)^T + (1, -1)^T = (3, 1)^T \quad \checkmark$$

## 2. 基变换与过渡矩阵

### 2.1 什么是基变换

前面说了"同一向量在不同基下坐标不同"，现在反过来问：**基变了，怎么用公式描述这种变化？** 设 $\boldsymbol{\varepsilon}_1, \ldots, \boldsymbol{\varepsilon}_n$（旧基）和 $\boldsymbol{\eta}_1, \ldots, \boldsymbol{\eta}_n$（新基）是 $V$ 的两组基。新基的每个向量都可以用旧基线性表示（因为旧基是基，能表示空间里所有向量）：

$$\begin{cases} \boldsymbol{\eta}_1 = p_{11}\boldsymbol{\varepsilon}_1 + p_{21}\boldsymbol{\varepsilon}_2 + \cdots + p_{n1}\boldsymbol{\varepsilon}_n \\ \boldsymbol{\eta}_2 = p_{12}\boldsymbol{\varepsilon}_1 + p_{22}\boldsymbol{\varepsilon}_2 + \cdots + p_{n2}\boldsymbol{\varepsilon}_n \\ \cdots \\ \boldsymbol{\eta}_n = p_{1n}\boldsymbol{\varepsilon}_1 + p_{2n}\boldsymbol{\varepsilon}_2 + \cdots + p_{nn}\boldsymbol{\varepsilon}_n \end{cases}$$

写成矩阵形式（注意列是"新基向量在旧基下的坐标"）：

$$(\boldsymbol{\eta}_1, \boldsymbol{\eta}_2, \ldots, \boldsymbol{\eta}_n) = (\boldsymbol{\varepsilon}_1, \boldsymbol{\varepsilon}_2, \ldots, \boldsymbol{\varepsilon}_n)P$$

$P = (p_{ij})_{n \times n}$ 称为由旧基到新基的**过渡矩阵**。

### 2.2 过渡矩阵的性质

1. 过渡矩阵 $P$ 一定**可逆**（因为两组基都是基，基矩阵都可逆）；
2. $P^{-1}$ 是由新基到旧基的过渡矩阵；
3. $|P| \neq 0$。

一个帮助记忆的要点：过渡矩阵的第 $j$ 列，就是第 $j$ 个**新基向量**在**旧基**下的坐标。

### 2.3 过渡矩阵的求法

设旧基矩阵为 $E = (\boldsymbol{\varepsilon}_1, \ldots, \boldsymbol{\varepsilon}_n)$，新基矩阵为 $F = (\boldsymbol{\eta}_1, \ldots, \boldsymbol{\eta}_n)$，则由基变换公式 $F = EP$ 得：

$$F = EP \quad \Rightarrow \quad P = E^{-1}F$$

**示例**：设旧基 $\boldsymbol{\varepsilon}_1 = (1, 0)^T$，$\boldsymbol{\varepsilon}_2 = (0, 1)^T$（自然基），新基 $\boldsymbol{\eta}_1 = (1, 1)^T$，$\boldsymbol{\eta}_2 = (1, -1)^T$，求过渡矩阵。

$$P = E^{-1}F = I^{-1}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

本例因为旧基是自然基，$E = I$，过渡矩阵恰好等于新基矩阵本身。

## 3. 坐标变换公式（本篇核心）

### 3.1 定理

设 $\boldsymbol{\alpha}$ 在旧基下的坐标为 $x = (x_1, \ldots, x_n)^T$，在新基下的坐标为 $y = (y_1, \ldots, y_n)^T$，由旧基到新基的过渡矩阵为 $P$，则：

$$x = Py \quad \text{或} \quad y = P^{-1}x$$

### 3.2 推导（为什么方向是"反着"的）

同一个向量 $\boldsymbol{\alpha}$ 用两组基表示应当相等：

$$\boldsymbol{\alpha} = Ex = Fy = (EP)y = E(Py)$$

因为 $E$ 可逆，两边左乘 $E^{-1}$，得到 $x = Py$。注意：过渡矩阵 $P$ 描述的是"旧基 → 新基"（$F = EP$），但坐标变换是 $x = Py$（旧坐标 $=$ $P$ 乘新坐标），**方向相反**。

记忆口诀：**基变正向，坐标变逆向。**

直觉解释：新基向量本身"更大/更偏"时，同一向量在新基下的坐标数字就会"更小"，所以坐标的变换方向与基的变换方向正好相反。类比：尺子变长一格（基变大），同一物体量出的数值（坐标）就变小。

### 3.3 注意点

- 公式里 $P$ 是"旧到新"的过渡矩阵，若题目给的是"新到旧"的过渡矩阵 $Q$，则坐标公式要换成 $x = Q^{-1}y$，务必看清题干。
- 常考题型：已知 $E, F$ 两组基 + 一个向量 $\boldsymbol{\alpha}$，先求 $P = E^{-1}F$，再代 $y = P^{-1}x$，两步合一。

## 4. 典型例题

### 例1（求过渡矩阵）

设 $\boldsymbol{\varepsilon}_1 = (1, 0, 0)^T$，$\boldsymbol{\varepsilon}_2 = (1, 1, 0)^T$，$\boldsymbol{\varepsilon}_3 = (1, 1, 1)^T$，$\boldsymbol{\eta}_1 = (1, 0, 1)^T$，$\boldsymbol{\eta}_2 = (0, 1, 0)^T$，$\boldsymbol{\eta}_3 = (0, 0, 1)^T$，求由 $\boldsymbol{\varepsilon}_1, \boldsymbol{\varepsilon}_2, \boldsymbol{\varepsilon}_3$ 到 $\boldsymbol{\eta}_1, \boldsymbol{\eta}_2, \boldsymbol{\eta}_3$ 的过渡矩阵。

**解**：

拼基矩阵：

$$E = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}, \quad F = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$$

先求 $E^{-1}$（对 $(E \mid I)$ 做行变换，或直接用上三角矩阵求逆公式）：

$$E^{-1} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}$$

再算 $P = E^{-1}F$：

$$P = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 1 & -1 \\ 1 & 0 & 1 \end{pmatrix}$$

**验证**：$P$ 的第 1 列 $(1, -1, 1)^T$ 应当满足 $\boldsymbol{\eta}_1 = 1\boldsymbol{\varepsilon}_1 - 1\boldsymbol{\varepsilon}_2 + 1\boldsymbol{\varepsilon}_3 = (1,0,0)^T - (1,1,0)^T + (1,1,1)^T = (1,0,1)^T$，与 $\boldsymbol{\eta}_1$ 一致。验证通过。

### 例2（已知过渡矩阵求新坐标）

设 $\boldsymbol{\alpha}$ 在基 $\boldsymbol{\varepsilon}_1, \boldsymbol{\varepsilon}_2, \boldsymbol{\varepsilon}_3$ 下的坐标为 $(1, 2, 3)^T$，过渡矩阵 $P = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$，求 $\boldsymbol{\alpha}$ 在新基下的坐标。

**解**：由坐标变换公式 $y = P^{-1}x$。先求 $P^{-1}$：

$$P^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 1 & -1 & 1 \end{pmatrix}$$

代入：

$$y = \begin{pmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 1 & -1 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}$$

即 $\boldsymbol{\alpha}$ 在新基下的坐标为 $(1, 1, 2)^T$。

**检验**：$Py = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = x$，符合 $x = Py$。验证通过。

### 例3（判断是否构成基并求坐标）

设 $\boldsymbol{\alpha}_1 = (1, 0, 1)^T$，$\boldsymbol{\alpha}_2 = (1, 1, 0)^T$，$\boldsymbol{\alpha}_3 = (0, 1, 1)^T$，证明它们是 $\mathbb{R}^3$ 的一组基，并求 $\boldsymbol{\beta} = (2, 3, 4)^T$ 在此基下的坐标。

**解**：

第一步，验证线性无关（基的充要条件）：

$$|A| = \begin{vmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{vmatrix} = 1 + 1 = 2 \neq 0$$

故 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 线性无关，构成 $\mathbb{R}^3$ 的一组基（$n$ 个 $n$ 维线性无关向量必是基）。

第二步，用公式 $x = A^{-1}\boldsymbol{\beta}$ 求坐标：

$$A^{-1} = \frac{1}{2}\begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}$$

$$x = \frac{1}{2}\begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 3 \\ 1 \\ 5 \end{pmatrix} = \begin{pmatrix} 3/2 \\ 1/2 \\ 5/2 \end{pmatrix}$$

第三步，检验：

$$\frac{3}{2}\boldsymbol{\alpha}_1 + \frac{1}{2}\boldsymbol{\alpha}_2 + \frac{5}{2}\boldsymbol{\alpha}_3 = \frac{1}{2}\big(3(1,0,1) + (1,1,0) + 5(0,1,1)\big) = \frac{1}{2}(4, 6, 8) = (2, 3, 4) \quad \checkmark$$

## 5. 常见错误与对策

| 常见错误 | 错误类型 | 原因 | 纠正方法 |
| --- | --- | --- | --- |
| 坐标变换方向搞反（把 $y = P^{-1}x$ 写成 $y = Px$） | 概念理解错误 | 混淆"基变换方向"与"坐标变换方向" | 记住口诀"基变正向，坐标变逆向"，并养成代入检验的习惯 |
| 过渡矩阵列写错（把新基向量按行排） | 概念理解错误 | 忘记"过渡矩阵第 $j$ 列 = 第 $j$ 个新基向量在旧基下的坐标" | 过渡矩阵永远是 $P = E^{-1}F$，$E$ 是旧基，$F$ 是新基 |
| 求坐标时忘记验证基的线性无关性就直接 $E^{-1}$ | 计算规范问题 | 默认给的向量组一定是基 | 先用行列式（或秩）确认 $|E| \neq 0$ 再求逆 |
| 求 $E^{-1}$ 时犯计算错误 | 计算错误 | 伴随矩阵法或行变换法不熟练 | 算完后用 $E^{-1}E = I$ 复核；或直接代入 $x = E^{-1}\boldsymbol{\alpha}$ 反解验证 |
| 把向量坐标与基向量的坐标混为一谈 | 概念混淆 | 没分清"谁的坐标" | 明确对象：$\boldsymbol{\alpha}$ 的坐标 = 它按基展开的组合系数 |
| 求坐标后不做还原检验 | 流程缺失 | 只求结果不求验证 | 算完坐标后用 $\sum x_i\boldsymbol{\varepsilon}_i$ 还原原向量，能快速发现错误 |

## 6. 实战练习

### 练习1（基础：求坐标）

设 $\boldsymbol{\varepsilon}_1 = (1, 2)^T$，$\boldsymbol{\varepsilon}_2 = (2, 1)^T$，求向量 $\boldsymbol{\alpha} = (4, 5)^T$ 在此基下的坐标。

**提示**：设 $\boldsymbol{\alpha} = x_1\boldsymbol{\varepsilon}_1 + x_2\boldsymbol{\varepsilon}_2$，解二元一次方程组，或直接用 $x = E^{-1}\boldsymbol{\alpha}$。

**参考答案要点**：$E = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$，$E^{-1} = -\frac{1}{3}\begin{pmatrix} 1 & -2 \\ -2 & 1 \end{pmatrix}$，$x = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$。检验：$2(1,2) + (2,1) = (4, 5)$。

### 练习2（进阶：过渡矩阵与坐标变换）

设 $\boldsymbol{\varepsilon}_1, \boldsymbol{\varepsilon}_2$ 为 $\mathbb{R}^2$ 的一组基，新基满足 $\boldsymbol{\eta}_1 = \boldsymbol{\varepsilon}_1 + \boldsymbol{\varepsilon}_2$，$\boldsymbol{\eta}_2 = \boldsymbol{\varepsilon}_1 - \boldsymbol{\varepsilon}_2$。若 $\boldsymbol{\alpha}$ 在新基下的坐标为 $(1, -1)^T$，求 $\boldsymbol{\alpha}$ 在旧基下的坐标。

**提示**：过渡矩阵 $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$（列是 $\boldsymbol{\eta}$ 在 $\boldsymbol{\varepsilon}$ 下的坐标），用 $x = Py$。

**参考答案要点**：$x = Py = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 0 \\ 2 \end{pmatrix}$。

### 练习3（进阶：含参数判断基）

问 $k$ 取何值时，$\boldsymbol{\alpha}_1 = (1, k, 0)^T$，$\boldsymbol{\alpha}_2 = (k, 1, 0)^T$，$\boldsymbol{\alpha}_3 = (0, 0, 1)^T$ 构成 $\mathbb{R}^3$ 的一组基？

**提示**：三个三维向量构成基 $\iff$ 行列式非零；先对前两行做初等变换化简行列式。

**参考答案要点**：$|A| = \begin{vmatrix} 1 & k & 0 \\ k & 1 & 0 \\ 0 & 0 & 1 \end{vmatrix} = 1 - k^2$，故 $k \neq \pm 1$ 时构成基；$k = \pm 1$ 时秩降为 2。

### 练习4（综合：两步变换）

设 $\boldsymbol{\alpha}$ 在基 $\boldsymbol{\varepsilon}_1, \boldsymbol{\varepsilon}_2$ 下的坐标为 $(3, 4)^T$，先从 $\boldsymbol{\varepsilon}$ 到 $\boldsymbol{\eta}$ 的过渡矩阵为 $P_1 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$，再从 $\boldsymbol{\eta}$ 到 $\boldsymbol{\zeta}$ 的过渡矩阵为 $P_2 = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$。求 $\boldsymbol{\alpha}$ 在 $\boldsymbol{\zeta}$ 基下的坐标。

**提示**：两步合成一步，由 $\boldsymbol{\varepsilon}$ 到 $\boldsymbol{\zeta}$ 的过渡矩阵是 $P_1P_2$（注意顺序：$(\boldsymbol{\zeta}) = (\boldsymbol{\varepsilon})P_1P_2$），坐标用逆矩阵。

**参考答案要点**：$P_1P_2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$，$z = (P_1P_2)^{-1}x = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} -1 \\ 5 \end{pmatrix}$。

### 练习5（挑战：三维完整流程）

设 $\boldsymbol{\varepsilon}_1 = (1, 1, 0)^T$，$\boldsymbol{\varepsilon}_2 = (1, 0, 1)^T$，$\boldsymbol{\varepsilon}_3 = (0, 1, 1)^T$，$\boldsymbol{\eta}_1 = (1, 0, 0)^T$，$\boldsymbol{\eta}_2 = (0, 1, 0)^T$，$\boldsymbol{\eta}_3 = (0, 0, 1)^T$。求由 $\boldsymbol{\varepsilon}$ 到 $\boldsymbol{\eta}$ 的过渡矩阵，并求 $\boldsymbol{\beta} = (1, 2, 3)^T$ 在 $\boldsymbol{\varepsilon}$ 基下的坐标。

**提示**：此处旧基是 $\boldsymbol{\varepsilon}$，新基 $\boldsymbol{\eta}$ 是自然基；$P = E^{-1}F = E^{-1}$；注意坐标公式中 $x$（旧基坐标）$= Py$。

**参考答案要点**：$E = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$，$|E| = -2 \neq 0$。$P = E^{-1} = \frac{1}{2}\begin{pmatrix} 1 & 1 & -1 \\ 1 & -1 & 1 \\ -1 & 1 & 1 \end{pmatrix}$。$\boldsymbol{\beta}$ 在 $\boldsymbol{\varepsilon}$ 基下的坐标为 $P\boldsymbol{\beta} = \frac{1}{2}(1+2-3, 1-2+3, -1+2+3)^T = (0, 1, 2)^T$。检验：$0\boldsymbol{\varepsilon}_1 + 1\boldsymbol{\varepsilon}_2 + 2\boldsymbol{\varepsilon}_3 = (1, 2, 3)^T$。

## 7. 一句话记忆

**同一向量在不同基下坐标不同，坐标按"基的逆方向"变换：基变用 $P$，坐标变用 $P^{-1}$——基变正向，坐标变逆向。**

## 参考链接与延伸阅读

- 同济大学数学科学学院《工程数学 线性代数（第七版）》，高等教育出版社，第 6 章 §3 基变换与坐标变换（权威教材，概念表述与例题来源）：https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=630508ea938b7cc2960ef14b
- MIT 18.06 Linear Algebra（Gilbert Strang，第 5 讲转置、置换与向量空间；坐标与基变换相关内容）：https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Interactive Linear Algebra（Georgia Tech，§4.6 基与基变换）：https://textbooks.math.gatech.edu/ila/
- 3Blue1Brown 线性代数的本质（基变换与坐标变换的可视化）：https://www.3blue1brown.com/topics/linear-algebra
- NumPy 文档（`numpy.linalg.inv`、`numpy.linalg.solve` 可验证坐标计算）：https://numpy.org/doc/stable/

延伸阅读：线性相关性、基与维数（前置知识）；内积与正交性、施密特正交化（后续内容，将自然基推广为标准正交基）；矩阵对角化（本篇坐标变换思想在特征值部分的深化应用）。
