---
order: 43
title: 内积与正交性
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: 内积的定义与性质，向量的长度与距离，正交向量与正交向量组，正交补空间与正交投影，含 0 基础类比、完整例题、常见错误对策与实战练习。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/基与维数'
  - 'linear-algebra/坐标与坐标变换'
  - 'linear-algebra/施密特正交化'
  - 'linear-algebra/向量空间典型例题'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 0. 从一个生活场景说起：没有尺子，怎么量长度和夹角？

装修师傅想确认两面墙是不是垂直（成 90° 角），但他的直角尺丢了，只剩一把直尺。他能做到吗？能。方法是在墙角两边各量出长度，再用勾股定理反推：如果两边墙上的两点距离满足 $a^2 + b^2 = c^2$，那么这两面墙就垂直。

这个故事告诉我们：**"垂直"（正交）和"长度"、"夹角"这些几何概念，本质上都能用"测量"来定义**。在向量空间里，这个"测量工具"就是**内积**。它是一把通用尺子：有了内积，我们可以给任意向量量长度（范数）、量夹角、判断正交（垂直），还能做"投影"——把一个向量拆成"平行分量 + 垂直分量"。

本篇完全围绕"度量"展开：定义内积 → 导出长度与夹角 → 定义正交 → 研究正交补与投影。它是后面施密特正交化、实对称矩阵正交对角化的基础。

## 1. 内积（那把尺子）

### 1.1 内积的定义（从点积说起）

在中学物理里，力做功 $W = F \cdot s$（力乘以位移再乘夹角余弦），这个"点乘"就是内积的雏形。对 $\mathbb{R}^n$ 中的向量，我们把点积推广为**标准内积**：

设 $\boldsymbol{\alpha} = (a_1, a_2, \ldots, a_n)^T$，$\boldsymbol{\beta} = (b_1, b_2, \ldots, b_n)^T$，定义：

$$(\boldsymbol{\alpha}, \boldsymbol{\beta}) = \boldsymbol{\alpha}^T\boldsymbol{\beta} = a_1b_1 + a_2b_2 + \cdots + a_nb_n = \sum_{i=1}^{n} a_ib_i$$

直观理解：内积是"逐分量相乘再求和"。它把一个数值对（两个向量）映射成一个数。内积为 0 意味着"两个方向完全没有同向分量"，这正是正交的含义。

### 1.2 内积的性质（尺子要好用，得满足四条规矩）

一个合理的"测量工具"必须满足以下性质（在更抽象的线性空间中，满足这四条的任何二元函数都可称为内积）：

1. **对称性**：$(\boldsymbol{\alpha}, \boldsymbol{\beta}) = (\boldsymbol{\beta}, \boldsymbol{\alpha})$
2. **线性性**：$(k_1\boldsymbol{\alpha}_1 + k_2\boldsymbol{\alpha}_2, \boldsymbol{\beta}) = k_1(\boldsymbol{\alpha}_1, \boldsymbol{\beta}) + k_2(\boldsymbol{\alpha}_2, \boldsymbol{\beta})$（对第一变元线性）
3. **正定性**：$(\boldsymbol{\alpha}, \boldsymbol{\alpha}) \geq 0$，等号成立当且仅当 $\boldsymbol{\alpha} = \mathbf{0}$

正定性保证了"长度平方非负"且"只有零向量长度为零"，这是所有几何结论的地基。

### 1.3 加权内积（一般内积）

标准内积把所有分量一视同仁。有时我们希望"某些方向分量更重要"，可以用 $n$ 阶**正定矩阵** $A$ 定义加权内积：

$$(\boldsymbol{\alpha}, \boldsymbol{\beta})_A = \boldsymbol{\alpha}^T A \boldsymbol{\beta}$$

（$A$ 正定保证正定性成立。）加权内积在机器学习、数据拟合中很常见（例如带权最小二乘）。

### 1.4 Cauchy-Schwarz 不等式（内积最重要的不等式）

$$|(\boldsymbol{\alpha}, \boldsymbol{\beta})| \leq \|\boldsymbol{\alpha}\| \cdot \|\boldsymbol{\beta}\|$$

等号成立当且仅当 $\boldsymbol{\alpha}$ 与 $\boldsymbol{\beta}$ 线性相关。

这个不等式是内积理论的"心脏"：它保证夹角余弦 $\cos\theta = \dfrac{(\boldsymbol{\alpha}, \boldsymbol{\beta})}{\|\boldsymbol{\alpha}\|\|\boldsymbol{\beta}\|}$ 的取值一定在 $[-1, 1]$ 之间——否则"夹角"就没有意义了。

**例0（验证 Cauchy-Schwarz 不等式）**：设 $\boldsymbol{\alpha} = (1, 2, 2)^T$，$\boldsymbol{\beta} = (2, 1, 0)^T$。

左端：$|(\boldsymbol{\alpha}, \boldsymbol{\beta})| = |1 \cdot 2 + 2 \cdot 1 + 2 \cdot 0| = 4$。

右端：$\|\boldsymbol{\alpha}\| = \sqrt{1 + 4 + 4} = 3$，$\|\boldsymbol{\beta}\| = \sqrt{4 + 1 + 0} = \sqrt{5}$，乘积 $= 3\sqrt{5} \approx 6.71$。

$4 \leq 6.71$，成立。

## 2. 向量的长度与距离

### 2.1 长度（范数）：内积开方

有了内积，长度就顺理成章：**向量与自身内积的平方根**。

$$\|\boldsymbol{\alpha}\| = \sqrt{(\boldsymbol{\alpha}, \boldsymbol{\alpha})} = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}$$

这恰好就是中学的距离公式（勾股定理的 $n$ 维推广）。

### 2.2 长度的三条性质

1. **非负性**：$\|\boldsymbol{\alpha}\| \geq 0$，等号成立当且仅当 $\boldsymbol{\alpha} = \mathbf{0}$
2. **齐次性**：$\|k\boldsymbol{\alpha}\| = |k| \cdot \|\boldsymbol{\alpha}\|$
3. **三角不等式**：$\|\boldsymbol{\alpha} + \boldsymbol{\beta}\| \leq \|\boldsymbol{\alpha}\| + \|\boldsymbol{\beta}\|$（"两边之和大于第三边"）

### 2.3 单位向量与单位化

长度为 $1$ 的向量称为**单位向量**。对任意非零向量 $\boldsymbol{\alpha}$：

$$\frac{\boldsymbol{\alpha}}{\|\boldsymbol{\alpha}\|}$$

是与 $\boldsymbol{\alpha}$ 同方向的单位向量，这个操作叫**单位化**（归一化）。它的几何意义：只保留方向，把长度缩放到 1。

### 2.4 距离：差的长度

两个向量 $\boldsymbol{\alpha}$ 和 $\boldsymbol{\beta}$ 之间的**距离**定义为它们之差的长度：

$$d(\boldsymbol{\alpha}, \boldsymbol{\beta}) = \|\boldsymbol{\alpha} - \boldsymbol{\beta}\|$$

直观理解：把 $\boldsymbol{\beta}$ 平移到起点与 $\boldsymbol{\alpha}$ 重合，差向量 $\boldsymbol{\alpha} - \boldsymbol{\beta}$ 的箭头正好从 $\boldsymbol{\beta}$ 终点指向 $\boldsymbol{\alpha}$ 终点，其长度就是两点距离。

### 2.5 夹角：用余弦反推

两个非零向量 $\boldsymbol{\alpha}$ 和 $\boldsymbol{\beta}$ 的**夹角** $\theta$ 由下式定义：

$$\cos\theta = \frac{(\boldsymbol{\alpha}, \boldsymbol{\beta})}{\|\boldsymbol{\alpha}\| \cdot \|\boldsymbol{\beta}\|}$$

Cauchy-Schwarz 不等式保证了 $\cos\theta \in [-1, 1]$，从而 $\theta \in [0, \pi]$ 有定义。特别地：

- $\cos\theta = 1$：同方向；
- $\cos\theta = 0$：垂直（正交）；
- $\cos\theta = -1$：反方向。

## 3. 正交向量与正交向量组

### 3.1 正交的定义

若 $(\boldsymbol{\alpha}, \boldsymbol{\beta}) = 0$，则称 $\boldsymbol{\alpha}$ 与 $\boldsymbol{\beta}$ **正交**，记作 $\boldsymbol{\alpha} \perp \boldsymbol{\beta}$。

**几何意义**：夹角为 $90°$（或其中一个是零向量）。注意：零向量与任何向量都正交（因为内积恒为 0）。

### 3.2 正交的三条性质

1. 零向量与任何向量正交；
2. $\boldsymbol{\alpha} \perp \boldsymbol{\beta} \iff \|\boldsymbol{\alpha} + \boldsymbol{\beta}\|^2 = \|\boldsymbol{\alpha}\|^2 + \|\boldsymbol{\beta}\|^2$（这就是勾股定理：两正交向量和的平方 = 平方和）；
3. 若 $\boldsymbol{\alpha} \perp \boldsymbol{\beta}_1$ 且 $\boldsymbol{\alpha} \perp \boldsymbol{\beta}_2$，则 $\boldsymbol{\alpha} \perp (k_1\boldsymbol{\beta}_1 + k_2\boldsymbol{\beta}_2)$（与一组向量都正交，则与它们的任意线性组合也正交——这是"正交补"的定义基础）。

### 3.3 正交向量组

若向量组 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ 中任意两个向量都正交（$(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_j) = 0$，$i \neq j$），则称为**正交向量组**。

**定理**：不含零向量的正交向量组一定线性无关。

**证明**：设 $k_1\boldsymbol{\alpha}_1 + \cdots + k_s\boldsymbol{\alpha}_s = 0$，两边与 $\boldsymbol{\alpha}_i$ 做内积：

$$k_i(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_i) = 0$$

因 $\boldsymbol{\alpha}_i \neq \mathbf{0}$，$(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_i) > 0$，故 $k_i = 0$（$i = 1, \ldots, s$），线性无关。证毕。

这条定理是正交性最重要的价值：**正交自动保证无关**，省去了判断相关性的麻烦。

### 3.4 标准正交向量组

若正交向量组中每个向量都是单位向量，则称为**标准正交向量组**（规范正交组）：

$$(\boldsymbol{\alpha}_i, \boldsymbol{\alpha}_j) = \delta_{ij} = \begin{cases} 1, & i = j \\ 0, & i \neq j \end{cases}$$

**标准正交基**：若 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_n$ 是 $n$ 维空间的标准正交基，则任意向量 $\boldsymbol{\beta}$ 的坐标有"免费"公式——直接用内积就能读出坐标：

$$x_i = (\boldsymbol{\beta}, \boldsymbol{\alpha}_i), \quad \boldsymbol{\beta} = \sum_{i=1}^{n} (\boldsymbol{\beta}, \boldsymbol{\alpha}_i)\boldsymbol{\alpha}_i$$

对比普通基下要解方程组 $x = E^{-1}\boldsymbol{\beta}$，标准正交基下只需逐分量做内积，计算量大大下降。这是所有后续"正交化"工作的动机。

## 4. 正交补空间与正交投影

### 4.1 正交补的定义

设 $W$ 是 $\mathbb{R}^n$ 的子空间，所有与 $W$ 中每个向量都正交的向量构成的集合称为 $W$ 的**正交补**，记作 $W^\perp$：

$$W^\perp = \{\boldsymbol{\alpha} \in \mathbb{R}^n \mid (\boldsymbol{\alpha}, \boldsymbol{\beta}) = 0, \forall \boldsymbol{\beta} \in W\}$$

直观理解：$W$ 是一个"平面"，$W^\perp$ 就是所有与该平面垂直的方向构成的"直线"。

### 4.2 正交补的性质

1. $W^\perp$ 也是子空间；
2. $W \cap W^\perp = \{\mathbf{0}\}$；
3. $\dim(W) + \dim(W^\perp) = n$；
4. $(W^\perp)^\perp = W$；
5. $\mathbb{R}^n = W \oplus W^\perp$（正交直和分解：空间里任一向量可唯一拆成"W 内分量 + 与 W 正交的分量"）。

### 4.3 与矩阵的关系（秩-零度定理的内积版本）

- $N(A) = (\text{Row}(A))^\perp$（零空间是行空间的正交补）
- $N(A^T) = (\text{Col}(A))^\perp$（左零空间是列空间的正交补）

这两条把线性方程组理论与几何正交性打通，是最小二乘法等应用的基石。

### 4.4 正交投影：把向量"拍"到子空间上

向量 $\boldsymbol{\alpha}$ 在子空间 $W$ 上的**正交投影** $\text{proj}_W \boldsymbol{\alpha}$ 满足：

$$\boldsymbol{\alpha} = \text{proj}_W \boldsymbol{\alpha} + \boldsymbol{\alpha}_\perp, \quad \boldsymbol{\alpha}_\perp \in W^\perp$$

直观理解：阳光垂直照向地面，物体影子的落点就是投影；"影子 + 竖直方向的分量"恰好还原物体本身。

若 $W$ 的一组标准正交基为 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_r$，则投影有简单公式：

$$\text{proj}_W \boldsymbol{\alpha} = \sum_{i=1}^{r} (\boldsymbol{\alpha}, \boldsymbol{e}_i)\boldsymbol{e}_i$$

即投影等于"$\boldsymbol{\alpha}$ 在各标准正交基方向上的分量之和"。

## 5. 典型例题

### 例1（求长度、夹角与正交性判断）

设 $\boldsymbol{\alpha} = (1, -1, 2)^T$，$\boldsymbol{\beta} = (2, 1, 0)^T$，$\boldsymbol{\gamma} = (1, 3, 1)^T$。

(1) 求 $\|\boldsymbol{\alpha}\|$ 与 $\|\boldsymbol{\beta}\|$；(2) 求 $\boldsymbol{\alpha}$ 与 $\boldsymbol{\beta}$ 的夹角余弦；(3) 判断 $\boldsymbol{\beta}$ 与 $\boldsymbol{\gamma}$ 是否正交。

**解**：

(1) $\|\boldsymbol{\alpha}\| = \sqrt{1 + 1 + 4} = \sqrt{6}$，$\|\boldsymbol{\beta}\| = \sqrt{4 + 1 + 0} = \sqrt{5}$。

(2) $(\boldsymbol{\alpha}, \boldsymbol{\beta}) = 2 - 1 + 0 = 1$，故：

$$\cos\theta = \frac{1}{\sqrt{6} \cdot \sqrt{5}} = \frac{1}{\sqrt{30}}$$

(3) $(\boldsymbol{\beta}, \boldsymbol{\gamma}) = 2 \cdot 1 + 1 \cdot 3 + 0 \cdot 1 = 5 \neq 0$，故 $\boldsymbol{\beta}$ 与 $\boldsymbol{\gamma}$ 不正交。

### 例2（标准正交基下求坐标）

设 $\boldsymbol{e}_1 = \frac{1}{\sqrt{2}}(1, 1, 0)^T$，$\boldsymbol{e}_2 = \frac{1}{\sqrt{2}}(1, -1, 0)^T$，$\boldsymbol{e}_3 = (0, 0, 1)^T$。验证它们是 $\mathbb{R}^3$ 的标准正交基，并求 $\boldsymbol{\beta} = (3, 1, 5)^T$ 在此基下的坐标。

**解**：

第一步，验证标准正交性：

$(\boldsymbol{e}_1, \boldsymbol{e}_2) = \frac{1}{2}(1 - 1 + 0) = 0$；$(\boldsymbol{e}_1, \boldsymbol{e}_3) = 0$；$(\boldsymbol{e}_2, \boldsymbol{e}_3) = 0$；且 $\|\boldsymbol{e}_1\| = \|\boldsymbol{e}_2\| = \|\boldsymbol{e}_3\| = 1$。故是标准正交基。

第二步，直接用内积求坐标：

$$x_1 = (\boldsymbol{\beta}, \boldsymbol{e}_1) = \frac{3 + 1}{\sqrt{2}} = 2\sqrt{2}, \quad x_2 = (\boldsymbol{\beta}, \boldsymbol{e}_2) = \frac{3 - 1}{\sqrt{2}} = \sqrt{2}, \quad x_3 = (\boldsymbol{\beta}, \boldsymbol{e}_3) = 5$$

第三步，检验：$2\sqrt{2}\boldsymbol{e}_1 + \sqrt{2}\boldsymbol{e}_2 + 5\boldsymbol{e}_3 = (2, 2, 0) + (1, -1, 0) + (0, 0, 5) = (3, 1, 5)$，验证通过。

### 例3（正交投影）

设 $W = \text{span}\{(1, 1, 0)^T\}$（一条直线），求 $\boldsymbol{\alpha} = (3, 1, 2)^T$ 在 $W$ 上的正交投影，并求 $\boldsymbol{\alpha}_\perp$。

**解**：$W$ 由 $\boldsymbol{u} = (1, 1, 0)^T$ 张成。先单位化：$\boldsymbol{e}_1 = \frac{1}{\sqrt{2}}(1, 1, 0)^T$。

投影公式：

$$\text{proj}_W \boldsymbol{\alpha} = (\boldsymbol{\alpha}, \boldsymbol{e}_1)\boldsymbol{e}_1 = \frac{4}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}(1, 1, 0)^T = 2(1, 1, 0)^T = (2, 2, 0)^T$$

垂直分量：

$$\boldsymbol{\alpha}_\perp = \boldsymbol{\alpha} - \text{proj}_W \boldsymbol{\alpha} = (3, 1, 2)^T - (2, 2, 0)^T = (1, -1, 2)^T$$

**检验**：$(\boldsymbol{\alpha}_\perp, \boldsymbol{e}_1) = (1 - 1 + 0)/\sqrt{2} = 0$，确实正交。验证通过。

## 6. 常见错误与对策

| 常见错误 | 错误类型 | 原因 | 纠正方法 |
| --- | --- | --- | --- |
| 内积定义记成"逐分量相乘不求和"或"加绝对值和" | 概念理解错误 | 与逐分量乘法混淆 | 牢记内积 = $\sum a_ib_i$，可用 2 维例子 $(1,2)\cdot(3,4) = 11$ 自查 |
| 把"正交向量组"等同于"标准正交向量组" | 概念混淆 | 忽略单位化要求 | 正交只要求两两内积为 0；标准正交还要求每个向量长度为 1 |
| 用"线性无关"判断"正交"，或反之 | 逻辑关系错误 | 不清楚两者方向关系 | 记住：正交（非零）⇒ 无关，但无关 ⇏ 正交；正交是更强的条件 |
| 算夹角时忘记开方（直接用内积当分母） | 计算规范问题 | 把 $\|\boldsymbol{\alpha}\|$ 与 $\|\boldsymbol{\alpha}\|^2$ 混淆 | 分母一定是两个长度的乘积 $\|\boldsymbol{\alpha}\| \cdot \|\boldsymbol{\beta}\|$ |
| 标准正交基下仍解方程组求坐标 | 方法低效/错误 | 没利用内积公式 | 标准正交基下坐标就是 $(\boldsymbol{\beta}, \boldsymbol{e}_i)$，直接内积即可 |
| 求投影后不检验垂直分量 | 流程缺失 | 只算投影不算余量 | 投影与余量应满足 $\boldsymbol{\alpha}_\perp \perp W$，算完代入验证 |

## 7. 实战练习

### 练习1（基础：内积与长度）

设 $\boldsymbol{\alpha} = (2, -1, 3)^T$，$\boldsymbol{\beta} = (1, 4, -2)^T$。求 $(\boldsymbol{\alpha}, \boldsymbol{\beta})$、$\|\boldsymbol{\alpha}\|$、$\|\boldsymbol{\beta}\|$，并判断 $\boldsymbol{\alpha}$ 与 $\boldsymbol{\beta}$ 是否正交。

**提示**：直接套定义；正交当且仅当内积为 0。

**参考答案要点**：$(\boldsymbol{\alpha}, \boldsymbol{\beta}) = 2 - 4 - 6 = -8 \neq 0$，不正交；$\|\boldsymbol{\alpha}\| = \sqrt{14}$，$\|\boldsymbol{\beta}\| = \sqrt{21}$。

### 练习2（进阶：夹角）

求 $\boldsymbol{\alpha} = (1, 1, 0)^T$ 与 $\boldsymbol{\beta} = (1, -1, \sqrt{2})^T$ 的夹角 $\theta$。

**提示**：$\cos\theta = \dfrac{(\boldsymbol{\alpha}, \boldsymbol{\beta})}{\|\boldsymbol{\alpha}\|\|\boldsymbol{\beta}\|}$，注意向量分量含 $\sqrt{2}$，长度也要带根号算。

**参考答案要点**：$(\boldsymbol{\alpha}, \boldsymbol{\beta}) = 1 - 1 + 0 = 0$，故 $\theta = 90°$，两向量正交。

### 练习3（进阶：构造正交向量）

求一个与 $\boldsymbol{\alpha}_1 = (1, 1, 0)^T$ 和 $\boldsymbol{\alpha}_2 = (0, 1, 1)^T$ 都正交的单位向量。

**提示**：先找满足 $\begin{cases} x_1 + x_2 = 0 \\ x_2 + x_3 = 0 \end{cases}$ 的非零解，再单位化。

**参考答案要点**：由 $x_2 = -x_1$，$x_3 = -x_2 = x_1$，取 $(1, -1, 1)^T$，单位化得 $\frac{1}{\sqrt{3}}(1, -1, 1)^T$。

### 练习4（综合：正交补与投影）

设 $W = \text{span}\{(1, 2, -1)^T\}$。求 $W^\perp$ 的一组基，并把 $\boldsymbol{\beta} = (3, 1, 2)^T$ 分解为 $W$ 分量与 $W^\perp$ 分量之和。

**提示**：$W^\perp = \{(x,y,z) \mid x + 2y - z = 0\}$，是 2 维子空间，解方程组得基；投影用公式 $\text{proj}_W\boldsymbol{\beta} = \dfrac{(\boldsymbol{\beta},\boldsymbol{u})}{(\boldsymbol{u},\boldsymbol{u})}\boldsymbol{u}$。

**参考答案要点**：$W^\perp$ 基可取 $(-2, 1, 0)^T$ 与 $(1, 0, 1)^T$。$\text{proj}_W\boldsymbol{\beta} = \frac{3+2-2}{6}(1,2,-1)^T = \frac{1}{2}(1,2,-1)^T$，余量 $\boldsymbol{\beta}_\perp = (\frac{5}{2}, 0, \frac{5}{2})^T$。检验：$(\boldsymbol{\beta}_\perp, (1,2,-1)) = \frac{5}{2} + 0 - \frac{5}{2} = 0$。

### 练习5（挑战：内积不等式）

证明：对任意实数 $x_1, \ldots, x_n$，有 $\left(\sum_{i=1}^{n}x_i\right)^2 \leq n\sum_{i=1}^{n}x_i^2$，并指出等号成立条件。

**提示**：令 $\boldsymbol{\alpha} = (1, 1, \ldots, 1)^T$，$\boldsymbol{\beta} = (x_1, \ldots, x_n)^T$，用 Cauchy-Schwarz 不等式。

**参考答案要点**：$|(\boldsymbol{\alpha}, \boldsymbol{\beta})| \leq \|\boldsymbol{\alpha}\|\|\boldsymbol{\beta}\|$ 即 $|\sum x_i| \leq \sqrt{n}\sqrt{\sum x_i^2}$，平方即得。等号当且仅当 $\boldsymbol{\beta}$ 与 $\boldsymbol{\alpha}$ 线性相关，即 $x_1 = x_2 = \cdots = x_n$。

## 8. 一句话记忆

**内积是向量空间的"尺子"：长度是内积开方，夹角由内积定义，正交就是内积为零；非零正交组必线性无关，标准正交基下坐标只需做内积。**

## 参考链接与延伸阅读

- 同济大学数学科学学院《工程数学 线性代数（第七版）》，高等教育出版社，第 5 章 §1 向量的内积、长度及正交性（权威教材，概念与例题来源）：https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=630508ea938b7cc2960ef14b
- Purdue University《Linear Algebra and its Applications》（Lay 教材配套讲义，§6.1 内积、长度与正交性）：https://www.math.purdue.edu/~xu1121/Sec6.1
- LibreTexts Linear Algebra（正交集合与投影，含正交基坐标公式）：https://math.libretexts.org/Courses/Irvine_Valley_College/Math_26%3A_Introduction_to_Linear_Algebra/03%3A_Vector_Geometry/3.07%3A_Orthogonal_Sets
- MIT 18.06 Linear Algebra（Strang 第 14 讲正交向量与子空间）：https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Interactive Linear Algebra（Georgia Tech，§6.2 正交集合与正交基）：https://textbooks.math.gatech.edu/ila/

延伸阅读：基与维数、坐标与坐标变换（前置知识）；施密特正交化（把普通基改造成标准正交基的算法，即本篇的直接续篇）；向量空间典型例题（正交化综合练习）；实对称矩阵对角化（标准正交基在特征值问题中的应用）。
