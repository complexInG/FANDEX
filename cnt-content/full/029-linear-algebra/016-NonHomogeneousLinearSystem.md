---
order: 33
title: 非齐次线性方程组
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 非齐次线性方程组的解的性质与结构，特解与导出组通解的关系，非齐次方程组通解的求法，特解选取的灵活性。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/解的存在性判定'
  - 'linear-algebra/齐次线性方程组'
  - 'linear-algebra/解的结构'
  - 'linear-algebra/线性方程组典型例题'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 0. 从"搬家"说起

搬家到一个新城市，通常分两步：第一步，先找一个**落脚点**（租好房子、定好坐标）；第二步，再慢慢安排家具摆放的**自由度**（这面墙放沙发、那面墙放书架，有多少种摆法）。房子的位置是"一个点"，摆法却是一个"空间"。

非齐次方程组 $Ax = b$ 的解，正是这种"落脚点 + 自由度"的组合。数学上叫：**一个特解 + 导出组的通解**。

- **特解 $\boldsymbol{\eta}^*$**：随便找一组满足方程的解——"落脚点"，决定了解集的位置；
- **导出组 $Ax = 0$ 的通解**：齐次方程组的全部解——"摆法的自由度"，决定了解集的形状与方向。

只要知道"落脚点"在哪儿、"摆法"有哪些，整个解集就完全确定了。本文按"结构驱动"的路线，先讲清这两部分各自的性质，再给出组装通解的完整流程（对应同济版《线性代数》第 4 章 §5）。

## 1. 基本概念

**定义**：非齐次线性方程组指 $Ax = b$ 且 $b \neq 0$。与它对应的齐次方程组 $Ax = 0$ 称为原方程组的**导出组**。

回顾 014 篇的判定结论：$Ax = b$ 有解 $\Longleftrightarrow r(A) = r(A \mid b)$。本文假设**方程组已经判定有解**，研究解集的结构。

## 2. 解的两条核心性质

**性质 1（解之差是齐次解）**：若 $\boldsymbol{\eta}_1, \boldsymbol{\eta}_2$ 都是 $Ax = b$ 的解，则 $\boldsymbol{\eta}_1 - \boldsymbol{\eta}_2$ 是导出组 $Ax = 0$ 的解。

**证明**：$A(\boldsymbol{\eta}_1 - \boldsymbol{\eta}_2) = A\boldsymbol{\eta}_1 - A\boldsymbol{\eta}_2 = b - b = 0$。

**性质 2（特解加齐次解仍是解）**：若 $\boldsymbol{\eta}$ 是 $Ax = b$ 的解，$\boldsymbol{\xi}$ 是 $Ax = 0$ 的解，则 $\boldsymbol{\eta} + \boldsymbol{\xi}$ 也是 $Ax = b$ 的解。

**证明**：$A(\boldsymbol{\eta} + \boldsymbol{\xi}) = A\boldsymbol{\eta} + A\boldsymbol{\xi} = b + 0 = b$。

这两条性质配合 015 篇的"齐次解集是子空间"，立刻推出：**非齐次方程组的解集 = 特解 + 齐次解空间**（一个平移后的子空间，即仿射子空间）。

**注意**：$Ax = b$ 的解集**不是**向量空间（不包含零向量，除非 $b = 0$）；但它是齐次解空间的"平移拷贝"，形状完全相同。

## 3. 解的结构定理

**定理（非齐次方程组通解公式）**：设 $Ax = b$ 有解，$\boldsymbol{\eta}^*$ 是它的一个特解，$\boldsymbol{\xi}_1, \boldsymbol{\xi}_2, \ldots, \boldsymbol{\xi}_{n-r}$ 是导出组 $Ax = 0$ 的基础解系（$r = r(A)$），则 $Ax = b$ 的**通解**为：

$$x = \boldsymbol{\eta}^* + k_1\boldsymbol{\xi}_1 + k_2\boldsymbol{\xi}_2 + \cdots + k_{n-r}\boldsymbol{\xi}_{n-r}, \qquad k_i \in \mathbb{R}$$

**为什么是"且仅是"这个形状**：

- *是解*：由性质 2，$\boldsymbol{\eta}^*$ 加任何齐次解都是解；
- *只有这些*：任意解 $x$ 与 $\boldsymbol{\eta}^*$ 之差 $x - \boldsymbol{\eta}^*$ 由性质 1 是齐次解，而齐次解都能写成基础解系的线性组合，所以 $x = \boldsymbol{\eta}^* + \sum k_i\boldsymbol{\xi}_i$。

**几何图景**：齐次解空间是过原点的一个 $n - r$ 维平面/直线；非齐次解集就是把它平移 $\boldsymbol{\eta}^*$ 之后的那个平面/直线——方向、维数一模一样，只是不再过原点。

## 4. 通解求法（七步流程）

1. 对增广矩阵 $(A \mid b)$ 做初等行变换，化为**行最简形**；
2. 比较 $r(A)$ 与 $r(A \mid b)$，判定是否有解（无解则停止）；
3. 写出同解方程组（把主变量用自由变量表示）；
4. 确定主变量与自由变量；
5. 令自由变量全取 0，求出**一个特解** $\boldsymbol{\eta}^*$；
6. 令自由变量逐个取 1、其余取 0（同 015 篇），求出导出组的**基础解系** $\boldsymbol{\xi}_1, \ldots, \boldsymbol{\xi}_{n-r}$；
7. 组装通解：$x = \boldsymbol{\eta}^* + \sum k_i\boldsymbol{\xi}_i$。

**例 1**：求方程组

$$\begin{cases} x_1 + x_2 - x_3 + 2x_4 = 3 \\ 2x_1 + x_2 - 3x_3 + 4x_4 = 5 \\ x_1 - x_3 + 2x_4 = 2 \end{cases}$$

的通解。

**步骤 1-2：化行最简形并判定**

$$(A \mid b) = \begin{pmatrix} 1 & 1 & -1 & 2 & 3 \\ 2 & 1 & -3 & 4 & 5 \\ 1 & 0 & -1 & 2 & 2 \end{pmatrix} \xrightarrow{r_2 - 2r_1, \; r_3 - r_1} \begin{pmatrix} 1 & 1 & -1 & 2 & 3 \\ 0 & -1 & -1 & 0 & -1 \\ 0 & -1 & 0 & 0 & -1 \end{pmatrix}$$

$$\xrightarrow{r_3 - r_2} \begin{pmatrix} 1 & 1 & -1 & 2 & 3 \\ 0 & -1 & -1 & 0 & -1 \\ 0 & 0 & 1 & 0 & 0 \end{pmatrix} \xrightarrow{-r_2} \begin{pmatrix} 1 & 1 & -1 & 2 & 3 \\ 0 & 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 & 0 \end{pmatrix}$$

$$\xrightarrow{r_2 - r_3, \; r_1 + r_3} \begin{pmatrix} 1 & 1 & 0 & 2 & 3 \\ 0 & 1 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 & 0 \end{pmatrix} \xrightarrow{r_1 - r_2} \begin{pmatrix} 1 & 0 & 0 & 2 & 2 \\ 0 & 1 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 & 0 \end{pmatrix}$$

$r(A) = r(A \mid b) = 3 < 4$，有无穷多解。

**步骤 3-4：写同解方程组、定变量**

$$\begin{cases} x_1 + 2x_4 = 2 \\ x_2 = 1 \\ x_3 = 0 \end{cases}$$

主变量 $x_1, x_2, x_3$，自由变量 $x_4$。

**步骤 5：求特解**（令 $x_4 = 0$）：

$$\boldsymbol{\eta}^* = (2, 1, 0, 0)^T$$

**步骤 6：求导出组基础解系**（令 $x_4 = 1$，由 $x_1 + 2x_4 = 0$ 得 $x_1 = -2$）：

$$\boldsymbol{\xi} = (-2, 0, 0, 1)^T$$

**步骤 7：组装通解**

$$x = (2, 1, 0, 0)^T + k(-2, 0, 0, 1)^T, \qquad k \in \mathbb{R}$$

**验证**：取 $k = 1$，$x = (0, 1, 0, 1)^T$ 代入第一个方程：$0 + 1 - 0 + 2 = 3$，正确。

## 5. 特解选取的灵活性

**例 2（换一种特解取法）**：沿用例 1，这次令 $x_4 = 1$ 求特解。

由 $x_1 + 2x_4 = 2$ 得 $x_1 = 0$，故 $\boldsymbol{\eta}' = (0, 1, 0, 1)^T$。通解写成：

$$x = (0, 1, 0, 1)^T + k(-2, 0, 0, 1)^T$$

与例 1 的通解**等价**吗？是的：取 $k = 1$，$(0,1,0,1)^T + 1 \cdot (-2,0,0,1)^T = (-2, 1, 0, 2)^T$，在例 1 的通解中取 $k = 1$ 得到 $(2,1,0,0)^T + (-2,0,0,1)^T = (0,1,0,1)^T$，两者描述的是同一条直线（解集相同）。

**要点**：特解不唯一——把自由变量取成任何数都行。考试中"令自由变量全为零"是最省事的默认选择，但遇到自由变量多的情况，也可以选让主变量更好算的取值。

## 6. 抽象非齐次方程组例题

**例 3**：设 $A$ 为 $4 \times 5$ 矩阵，$r(A) = 3$，$\boldsymbol{\eta}_1, \boldsymbol{\eta}_2, \boldsymbol{\eta}_3$ 是 $Ax = b$ 的三个线性无关的解，求 $Ax = b$ 的通解。

**解**：$r(A) = 3$，$n = 5$，导出组基础解系含 $5 - 3 = 2$ 个向量。

由性质 1，$\boldsymbol{\eta}_2 - \boldsymbol{\eta}_1$ 与 $\boldsymbol{\eta}_3 - \boldsymbol{\eta}_1$ 都是导出组的解。证明它们线性无关：设 $k_1(\boldsymbol{\eta}_2 - \boldsymbol{\eta}_1) + k_2(\boldsymbol{\eta}_3 - \boldsymbol{\eta}_1) = 0$，即

$$-k_1\boldsymbol{\eta}_1 - k_2\boldsymbol{\eta}_1 + k_1\boldsymbol{\eta}_2 + k_2\boldsymbol{\eta}_3 = 0$$

由 $\boldsymbol{\eta}_1, \boldsymbol{\eta}_2, \boldsymbol{\eta}_3$ 线性无关，得 $k_1 = k_2 = 0$。故 $\boldsymbol{\eta}_2 - \boldsymbol{\eta}_1$、$\boldsymbol{\eta}_3 - \boldsymbol{\eta}_1$ 是导出组的 2 个线性无关解，个数恰为 $n - r = 2$，构成基础解系。

**通解**：$x = \boldsymbol{\eta}_1 + k_1(\boldsymbol{\eta}_2 - \boldsymbol{\eta}_1) + k_2(\boldsymbol{\eta}_3 - \boldsymbol{\eta}_1)$。

**例 4**：设 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 是 $Ax = b$ 的解，$\boldsymbol{\beta}_1, \boldsymbol{\beta}_2$ 是导出组 $Ax = 0$ 的基础解系，写出 $Ax = b$ 的通解。

**解**：取特解 $\boldsymbol{\alpha}_1$，导出组通解为 $k_1\boldsymbol{\beta}_1 + k_2\boldsymbol{\beta}_2$，故：

$$x = \boldsymbol{\alpha}_1 + k_1\boldsymbol{\beta}_1 + k_2\boldsymbol{\beta}_2$$

**易错点**：$\boldsymbol{\alpha}_1 + \boldsymbol{\alpha}_2$ **不是** $Ax = b$ 的解（$A(\boldsymbol{\alpha}_1 + \boldsymbol{\alpha}_2) = 2b \neq b$）；而 $\dfrac{\boldsymbol{\alpha}_1 + \boldsymbol{\alpha}_2}{2}$ 是解。这是"解的和是 $2b$ 的解"这一性质最容易翻车的地方。

## 7. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 通解写成 $k_1\boldsymbol{\xi}_1 + k_2\boldsymbol{\xi}_2$ 忘了加特解 | 结构残缺 | 把非齐次当齐次 | 非齐次通解 = 特解 + 导出组通解，特解不能丢 |
| 认为 $\boldsymbol{\eta}_1 + \boldsymbol{\eta}_2$ 是 $Ax = b$ 的解 | 性质误用 | 解之和满足 $A(x_1+x_2) = 2b$ | 只有 $\frac{\boldsymbol{\eta}_1+\boldsymbol{\eta}_2}{2}$ 或 $\boldsymbol{\eta}_1 + \boldsymbol{\xi}$ 才是解 |
| 不判 $r(A) = r(A \mid b)$ 直接求通解 | 流程遗漏 | 无解时不存在特解 | 先判定有解再求通解（见 014 篇） |
| 特解与基础解系混在一起算 | 分工不清 | 主变量值里掺入自由变量 | 特解：自由变量全取 0；基础解系：自由变量逐个取 1 |
| 基础解系个数算成 $n - r(A \mid b)$ | 公式误用 | 导出组的自由变量取决于 $A$ 而非增广矩阵 | 基础解系个数 = $n - r(A)$ |
| 用 $x = \boldsymbol{\eta}^* + \sum k_i\boldsymbol{\xi}_i$ 却不检查 $\boldsymbol{\xi}_i$ 是否确实是齐次解 | 验证缺失 | 回代错误未被发现 | 取 $k_i$ 特殊值回代原方程验证 |

## 8. 实战练习

**练习 1（基础）**：求 $\begin{cases} x_1 + 2x_2 = 3 \\ 2x_1 + 4x_2 = 6 \end{cases}$ 的通解。

- **提示**：先判定（两个方程相同），再按"特解 + 导出组通解"写。
- **参考答案要点**：特解 $(3, 0)^T$，导出组基础解系 $(-2, 1)^T$，通解 $x = (3,0)^T + k(-2,1)^T$。

**练习 2（进阶）**：求 $\begin{cases} x_1 + x_2 + x_3 = 1 \\ 2x_1 + 2x_2 + 2x_3 = 2 \\ 3x_1 + 3x_2 + 3x_3 = 3 \end{cases}$ 的通解。

- **提示**：三个方程本质相同，$r(A) = r(A \mid b) = 1$。
- **参考答案要点**：$x_1 + x_2 + x_3 = 1$，特解 $(1,0,0)^T$，基础解系 $(-1,1,0)^T$, $(-1,0,1)^T$，通解 $x = (1,0,0)^T + k_1(-1,1,0)^T + k_2(-1,0,1)^T$。

**练习 3（进阶）**：设 $A$ 为 $3 \times 4$ 矩阵，$r(A) = 2$，$\boldsymbol{\eta}_1 = (1, 1, 1, 1)^T$、$\boldsymbol{\eta}_2 = (2, 1, 0, 1)^T$ 都是 $Ax = b$ 的解，求 $Ax = b$ 的通解。

- **提示**：$\boldsymbol{\eta}_2 - \boldsymbol{\eta}_1$ 是导出组的非零解，且 $n - r(A) = 2$，还缺一个基础解系向量——题目信息不足？检查条件。
- **参考答案要点**：$\boldsymbol{\xi} = \boldsymbol{\eta}_2 - \boldsymbol{\eta}_1 = (1, 0, -1, 0)^T$ 是导出组解；基础解系应有 $4 - 2 = 2$ 个向量，仅知两个特解无法确定第二个，通解至少为 $x = \boldsymbol{\eta}_1 + k_1\boldsymbol{\xi} + k_2\boldsymbol{\xi}_2$（$\boldsymbol{\xi}_2$ 需另行求出）。

**练习 4（综合）**：设 $A$ 为 $n$ 阶方阵，$Ax = b$ 有唯一解，问 $Ax = 0$ 有多少解？若 $Ax = b$ 有无穷多解呢？

- **提示**：唯一解时 $r(A) = n$。
- **参考答案要点**：$Ax = b$ 唯一解 $\Rightarrow r(A) = n \Rightarrow Ax = 0$ 只有零解；$Ax = b$ 有无穷多解 $\Rightarrow r(A) < n \Rightarrow Ax = 0$ 也有无穷多解。

**练习 5（综合）**：证明：$Ax = b$ 的任意解可写成 $x = \boldsymbol{\eta}^* + \boldsymbol{\xi}$，其中 $\boldsymbol{\eta}^*$ 是固定特解，$\boldsymbol{\xi}$ 跑遍导出组解空间。

- **提示**：分别证"包含"与"包含于"，用性质 1、2。
- **参考答案要点**：由性质 2，$\boldsymbol{\eta}^* + \boldsymbol{\xi}$ 全是解；任取解 $x$，由性质 1，$x - \boldsymbol{\eta}^* \in N(A)$，故 $x = \boldsymbol{\eta}^* + (x - \boldsymbol{\eta}^*)$，两集合相等。

## 9. 一句话记忆

> **非齐次方程组 $Ax = b$ 的解集 = 一个特解（落脚点）+ 导出组 $Ax = 0$ 的解空间（自由度）——先找"一个位置"，再叠加"全部方向"，解的结构一目了然。**

## 参考文献

- 同济大学数学科学学院. 工程数学 线性代数（第七版）[M]. 北京: 高等教育出版社, 2023. （第 4 章 §5 线性方程组的解的结构）https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=630508ea938b7cc2960ef14b
- MIT 18.06 Linear Algebra（Strang）: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Interactive Linear Algebra（Georgia Tech）: https://textbooks.math.gatech.edu/ila/

## 延伸阅读

- 有解判定的秩条件，见 029-linear-algebra 模块 014 篇。
- 导出组的基础解系求法，见 029-linear-algebra 模块 015 篇。
- 解的结构定理的系统证明与推广（解空间的仿射几何），见 029-linear-algebra 模块 017 篇。
- 大量非齐次方程组综合题（含参数、抽象条件），见 029-linear-algebra 模块 018 篇。
