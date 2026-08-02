---
order: 40
title: 线性相关性
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 线性组合与线性表示，线性相关与线性无关的定义、判定与性质，向量组的等价，从"冗余"直觉到行列式与秩的严格判定。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/解的结构'
  - 'linear-algebra/线性方程组典型例题'
  - 'linear-algebra/基与维数'
  - 'linear-algebra/坐标与坐标变换'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 0. 从"团队是否冗余"说起

项目组里如果有人能完全替代另一个人——两个人干的是同一件事，那这个团队就有**冗余**：裁掉一个，项目的产出能力不变。反过来，如果每个成员都有不可替代的独特贡献，团队就是**精简**的。

"向量组是否线性相关"问的正是这件事：**这组向量里，有没有"多余"的向量——可以被其他向量"拼"出来？** 比如平面里两个共线的向量 $(1, 2)$ 和 $(2, 4)$：第二个是第一个的 2 倍，纯属冗余；而 $(1, 0)$ 和 $(0, 1)$ 各管一个方向，谁也不能替代谁。

别小看这个直觉，它是整个线性代数大厦的地基：

- 解空间的"骨架"（基础解系）要求线性无关——冗余的"柱子"不能撑起空间；
- 矩阵的秩 = 列向量组中"非冗余"向量的个数；
- 基的定义 = "生成 + 无关"（一个不多、一个不少）。

本文按"概念驱动"的路线，从"冗余"直觉出发，给出线性相关 / 无关的精确定义、判定工具与核心性质（对应同济版《线性代数》第 4 章 §2"向量组的线性相关性"）。

## 1. 前置概念：线性组合与线性表示

**线性组合**：设 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \ldots, \boldsymbol{\alpha}_s$ 是一组向量，$k_1, k_2, \ldots, k_s$ 是一组数，则

$$k_1\boldsymbol{\alpha}_1 + k_2\boldsymbol{\alpha}_2 + \cdots + k_s\boldsymbol{\alpha}_s$$

称为它们的**线性组合**。"线性"指只允许两种操作：**数乘**（伸缩）与**相加**（叠加），不允许平方、开方、乘除向量等操作。

**线性表示**：若向量 $\boldsymbol{\beta}$ 可以写成

$$\boldsymbol{\beta} = k_1\boldsymbol{\alpha}_1 + k_2\boldsymbol{\alpha}_2 + \cdots + k_s\boldsymbol{\alpha}_s$$

则称 $\boldsymbol{\beta}$ 可由 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ **线性表示**（即 $\boldsymbol{\beta}$ 能被这些向量"拼"出来）。

**与方程组挂钩**：$\boldsymbol{\beta}$ 能否被线性表示，等价于方程组 $x_1\boldsymbol{\alpha}_1 + \cdots + x_s\boldsymbol{\alpha}_s = \boldsymbol{\beta}$ 是否有解，即 $r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s) = r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s, \boldsymbol{\beta})$。这又把向量组理论与 014 篇的秩判定连在了一起。

**基本性质**：零向量可由任何向量组表示（全取系数 0）；每个向量可由自身所在组表示；线性表示具有传递性（$\boldsymbol{\alpha}$ 可由 $\boldsymbol{\beta}$ 组表示、每个 $\boldsymbol{\beta}$ 可由 $\boldsymbol{\gamma}$ 组表示，则 $\boldsymbol{\alpha}$ 可由 $\boldsymbol{\gamma}$ 组表示）。

## 2. 线性相关与线性无关：把"冗余"说精确

### 2.1 从直觉到定义

团队冗余的精确说法是：**存在一个成员能由其他成员替代**。对应到向量：

**定义（线性相关）**：存在**不全为零**的数 $k_1, k_2, \ldots, k_s$，使得

$$k_1\boldsymbol{\alpha}_1 + k_2\boldsymbol{\alpha}_2 + \cdots + k_s\boldsymbol{\alpha}_s = \mathbf{0}$$

则称 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ **线性相关**。

**定义（线性无关）**：若上式**只有**在 $k_1 = k_2 = \cdots = k_s = 0$ 时才成立，则称它们**线性无关**。

**为什么等价于"冗余"**：若存在不全为零的系数使组合为零，比如 $k_1 \neq 0$，则

$$\boldsymbol{\alpha}_1 = -\frac{k_2}{k_1}\boldsymbol{\alpha}_2 - \cdots - \frac{k_s}{k_1}\boldsymbol{\alpha}_s$$

即 $\boldsymbol{\alpha}_1$ 可由其余向量拼出——确实有"冗余成员"。反过来也成立。

### 2.2 三个立刻可用的直觉结论

1. **单个向量**：$\boldsymbol{\alpha}$ 线性相关 $\Longleftrightarrow \boldsymbol{\alpha} = \mathbf{0}$（非零向量单个必无关）；
2. **两个向量**：$\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2$ 线性相关 $\Longleftrightarrow$ 它们**成比例**（共线）；
3. **含零向量**：任何含 $\mathbf{0}$ 的向量组必线性相关（零向量"谁都能替代它"）。

## 3. 判定方法：三条路线

**方法一：定义法（万能的）**

设 $k_1\boldsymbol{\alpha}_1 + \cdots + k_s\boldsymbol{\alpha}_s = 0$，把它看作关于 $k_1, \ldots, k_s$ 的齐次方程组，判断是否有非零解：

- 有非零解 $\Rightarrow$ 线性相关；
- 只有零解 $\Rightarrow$ 线性无关。

**方法二：行列式法（$s = n$ 时最快捷）**

若 $s$ 个 $s$ 维向量 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$，构造方阵 $A = (\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s)$：

- $|A| \neq 0$ $\Rightarrow$ 线性无关；
- $|A| = 0$ $\Rightarrow$ 线性相关。

**方法三：秩法（最通用的）**

构造矩阵 $A = (\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s)$（按列排）：

- $r(A) = s$ $\Rightarrow$ 线性无关（秩等于向量个数，说明没有冗余列）；
- $r(A) < s$ $\Rightarrow$ 线性相关（秩小于个数，说明有冗余列）。

**关键结论**：$n$ 维空间中，任意 $n + 1$ 个向量必线性相关（人比"方向"多，必有冗余）；当 $s > n$ 时秩法自动给出答案。

## 4. 核心性质

**性质 1（部分与整体）**：

- 部分组线性相关 $\Rightarrow$ 整体组线性相关（团队里两人重复，整个团队必然冗余）；
- 整体组线性无关 $\Rightarrow$ 任意部分组线性无关（团队精简，任何子集都精简）。

**性质 2（扩充与缩短分量）**：线性无关的向量组**添加分量**（加长）后仍线性无关；线性相关的向量组**删去分量**（缩短）后仍线性相关。直觉：冗余关系在"去掉坐标"后依然存在。

**性质 3（替换定理）**：若 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ 线性无关，且每个 $\boldsymbol{\alpha}_i$ 都可由 $\boldsymbol{\beta}_1, \ldots, \boldsymbol{\beta}_t$ 线性表示，则 $s \le t$。推论：两个等价的线性无关向量组所含向量个数相同。

**性质 4（含零向量的组、含相同向量的组）**：必线性相关。

**性质 5（$\boldsymbol{\beta}$ 表示的唯一性）**：若 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ 线性无关，且 $\boldsymbol{\beta}$ 可由它们表示，则**表示方式唯一**（系数唯一确定）。这正是"坐标"概念存在的前提（详见 020-021 篇）。

## 5. 例题

**例 1（观察法）**：判断 $\boldsymbol{\alpha}_1 = (1, 2, 3)^T$，$\boldsymbol{\alpha}_2 = (2, 4, 6)^T$，$\boldsymbol{\alpha}_3 = (1, 1, 1)^T$ 的线性相关性。

**解**：$\boldsymbol{\alpha}_2 = 2\boldsymbol{\alpha}_1$，两向量成比例，故 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2$ 线性相关；由性质 1（部分相关则整体相关），$\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 线性相关。

**例 2（定义法 / 行列式法）**：设 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 线性无关，$\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1 + \boldsymbol{\alpha}_2$，$\boldsymbol{\beta}_2 = \boldsymbol{\alpha}_2 + \boldsymbol{\alpha}_3$，$\boldsymbol{\beta}_3 = \boldsymbol{\alpha}_3 + \boldsymbol{\alpha}_1$，判断 $\boldsymbol{\beta}_1, \boldsymbol{\beta}_2, \boldsymbol{\beta}_3$ 的线性相关性。

**解**：设 $k_1\boldsymbol{\beta}_1 + k_2\boldsymbol{\beta}_2 + k_3\boldsymbol{\beta}_3 = 0$，展开并按 $\boldsymbol{\alpha}_i$ 合并：

$$(k_1 + k_3)\boldsymbol{\alpha}_1 + (k_1 + k_2)\boldsymbol{\alpha}_2 + (k_2 + k_3)\boldsymbol{\alpha}_3 = 0$$

由 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 线性无关，得齐次方程组：

$$\begin{cases} k_1 + k_3 = 0 \\ k_1 + k_2 = 0 \\ k_2 + k_3 = 0 \end{cases}$$

系数行列式 $\begin{vmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{vmatrix} = 2 \neq 0$，方程组只有零解 $k_1 = k_2 = k_3 = 0$。故 $\boldsymbol{\beta}_1, \boldsymbol{\beta}_2, \boldsymbol{\beta}_3$ **线性无关**。

**思路提炼**：把"组合为零"翻译成"以 $k$ 为未知数的方程组"，再用行列式/秩判断——这是抽象向量组题目的标准套路。

**例 3（对称的"翻车"例子）**：同上题条件，但取 $\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1 - \boldsymbol{\alpha}_2$，$\boldsymbol{\beta}_2 = \boldsymbol{\alpha}_2 - \boldsymbol{\alpha}_3$，$\boldsymbol{\beta}_3 = \boldsymbol{\alpha}_3 - \boldsymbol{\alpha}_1$。

**解**：直接相加：$\boldsymbol{\beta}_1 + \boldsymbol{\beta}_2 + \boldsymbol{\beta}_3 = (\boldsymbol{\alpha}_1 - \boldsymbol{\alpha}_2) + (\boldsymbol{\alpha}_2 - \boldsymbol{\alpha}_3) + (\boldsymbol{\alpha}_3 - \boldsymbol{\alpha}_1) = 0$。

存在不全为零的系数 $(1, 1, 1)$ 使组合为零，故**线性相关**。同样的结构，符号一变就从无关变相关——做此类题务必细心核对符号。

## 6. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 认为"向量组含非零向量就无关" | 概念误判 | 两个成比例的非零向量是相关的 | 用定义/行列式/秩判定，不能凭非零判断 |
| 把"线性表示存在"当"唯一" | 唯一性误用 | 表示唯一的前提是组线性无关 | $\boldsymbol{\beta}$ 表示唯一 $\Leftrightarrow$ 向量组无关 |
| 行列式法用于 $s \neq n$ 的向量组 | 方法误用 | 只有 $s$ 个 $s$ 维向量才能构方阵 | $s \neq n$ 时改用秩法 |
| 例 3 这类题漏看符号 | 粗心错误 | 加减号变换后关系变化 | 展开验证：先求和再判断 |
| 把"整体相关"当作"每个都冗余" | 推断过强 | 相关只保证至少一个可被替代 | 相关时可能有向量不可被其余表示，需具体判断 |
| 秩法把向量按行排导致结论错误 | 操作错误 | 按行排后列数变化，$r = s$ 判断失效 | 判定线性相关性必须把向量**按列**排成矩阵 |

## 7. 实战练习

**练习 1（基础）**：判断 $\boldsymbol{\alpha}_1 = (1, 1)^T$，$\boldsymbol{\alpha}_2 = (2, 3)^T$ 是否线性相关。

- **提示**：两个二维向量，算行列式。
- **参考答案要点**：$\begin{vmatrix} 1 & 2 \\ 1 & 3 \end{vmatrix} = 1 \neq 0$，线性无关。

**练习 2（基础）**：判断 $\boldsymbol{\alpha}_1 = (1, 2, 1)^T$，$\boldsymbol{\alpha}_2 = (2, 4, 2)^T$，$\boldsymbol{\alpha}_3 = (0, 1, 1)^T$。

- **提示**：观察 $\boldsymbol{\alpha}_2$ 与 $\boldsymbol{\alpha}_1$ 的关系。
- **参考答案要点**：$\boldsymbol{\alpha}_2 = 2\boldsymbol{\alpha}_1$，线性相关。

**练习 3（进阶）**：判断 $\boldsymbol{\alpha}_1 = (1, 1, 1)^T$，$\boldsymbol{\alpha}_2 = (1, 2, 3)^T$，$\boldsymbol{\alpha}_3 = (1, 4, 9)^T$ 的线性相关性。

- **提示**：算范德蒙德行列式。
- **参考答案要点**：$|A| = (2-1)(3-1)(3-2) = 2 \neq 0$，线性无关。

**练习 4（进阶）**：设 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 线性无关，问 $\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1$，$\boldsymbol{\beta}_2 = \boldsymbol{\alpha}_1 + \boldsymbol{\alpha}_2$，$\boldsymbol{\beta}_3 = \boldsymbol{\alpha}_1 + \boldsymbol{\alpha}_2 + \boldsymbol{\alpha}_3$ 是否线性无关。

- **提示**：写系数矩阵（表示矩阵）并算行列式；或用定义法。
- **参考答案要点**：$\begin{pmatrix} \boldsymbol{\beta}_1 & \boldsymbol{\beta}_2 & \boldsymbol{\beta}_3 \end{pmatrix} = \begin{pmatrix} \boldsymbol{\alpha}_1 & \boldsymbol{\alpha}_2 & \boldsymbol{\alpha}_3 \end{pmatrix}\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$，表示矩阵上三角且行列式为 1，可逆，故 $\boldsymbol{\beta}$ 组线性无关。

**练习 5（综合）**：设 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 线性无关，证明 $\boldsymbol{\alpha}_1 + \boldsymbol{\alpha}_2$，$\boldsymbol{\alpha}_2 + \boldsymbol{\alpha}_3$，$\boldsymbol{\alpha}_1 + 2\boldsymbol{\alpha}_2 + \boldsymbol{\alpha}_3$ 线性相关。

- **提示**：$\boldsymbol{\alpha}_1 + 2\boldsymbol{\alpha}_2 + \boldsymbol{\alpha}_3 = (\boldsymbol{\alpha}_1 + \boldsymbol{\alpha}_2) + (\boldsymbol{\alpha}_2 + \boldsymbol{\alpha}_3)$。
- **参考答案要点**：第三个向量恰为前两个之和，存在系数 $(-1, -1, 1)$ 使组合为零，线性相关。

## 8. 一句话记忆

> **线性相关 = 向量组里有"冗余成员"（能被其余向量拼出来）；判定三件套：定义法（看齐次方程组有无非零解）、行列式法（$s$ 个 $s$ 维向量看 $|A|$）、秩法（$r(A) < s$ 即相关）——向量的个数超过维度，必冗余。**

## 参考文献

- 同济大学数学科学学院. 工程数学 线性代数（第七版）[M]. 北京: 高等教育出版社, 2023. （第 4 章 §2 向量组的线性相关性）https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=630508ea938b7cc2960ef14b
- MIT 18.06 Linear Algebra（Strang）: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Interactive Linear Algebra（Georgia Tech）: https://textbooks.math.gatech.edu/ila/

## 延伸阅读

- 判定中用到的秩工具，见 029-linear-algebra 模块 010 篇。
- 线性相关性与方程组的联系（$Ax = 0$ 有非零解），见 029-linear-algebra 模块 014-015 篇。
- 极大无关组、向量组的秩、基与维数（"冗余"的精确定量），见 029-linear-algebra 模块 020 篇。
- 坐标的唯一性由无关性保证，见 029-linear-algebra 模块 021 篇。
