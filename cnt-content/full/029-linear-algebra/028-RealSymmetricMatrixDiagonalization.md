---
order: 53
title: 实对称矩阵的对角化
module: 'linear-algebra'
category: 'comp-sci'
difficulty: advanced
description: 实对称矩阵的性质（特征值为实数、不同特征值特征向量正交），谱定理，正交对角化步骤与应用（二次型、PCA），含 0 基础类比、完整例题、常见错误对策与实战练习。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/特征值性质'
  - 'linear-algebra/矩阵对角化'
  - 'linear-algebra/特征值典型例题'
  - 'linear-algebra/二次型的标准形'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 0. 从一个生活场景说起：为什么"对称"的东西总是更好

仔细观察一座对称的建筑（比如天安门城楼、故宫的布局）：左右两半互为镜像，结构稳、受力均衡、看起来也舒服。工程师还发现，对称结构在数学上"脾气"最好——需要求解的方程往往更简单、更稳定。

**实对称矩阵**（满足 $A^T = A$ 的实矩阵）就是矩阵世界里的"对称建筑"。它拥有一般矩阵梦寐以求的三条"优雅性质"：

1. 特征值全是**实数**（不会出现复数，工程上可直接使用）；
2. 不同特征值的特征向量自动**正交**（省去很多正交化工作）；
3. **一定可以对角化**，而且可以用**正交矩阵** $Q$（$Q^{-1} = Q^T$）来对角化——求逆变成转置，成本为零。

本篇是"定理驱动"篇：先证明三条性质（定理），再给出谱定理（总纲），最后走一遍正交对角化的完整流程。它是二次型标准化、主成分分析（PCA）等应用的数学地基。

## 1. 实对称矩阵的三条基本性质（三条定理）

### 定理1：实对称矩阵的特征值都是实数

**证明**：设 $A\boldsymbol{x} = \lambda\boldsymbol{x}$（$\boldsymbol{x} \neq \mathbf{0}$，允许复数）。对两边取共轭转置，利用 $A$ 是实对称矩阵（$\overline{A} = A$，$A^T = A$）：

$$\bar{\boldsymbol{x}}^T A\boldsymbol{x} = \lambda \bar{\boldsymbol{x}}^T\boldsymbol{x}$$

另一方面，由 $A\boldsymbol{x} = \lambda\boldsymbol{x}$ 及 $A = A^T$：

$$\bar{\boldsymbol{x}}^T A\boldsymbol{x} = (A\bar{\boldsymbol{x}})^T\boldsymbol{x} = \bar{\lambda}\bar{\boldsymbol{x}}^T\boldsymbol{x}$$

两式相减：$(\lambda - \bar{\lambda})\bar{\boldsymbol{x}}^T\boldsymbol{x} = 0$。因 $\bar{\boldsymbol{x}}^T\boldsymbol{x} = \sum|\boldsymbol{x}_i|^2 > 0$，故 $\lambda = \bar{\lambda}$，$\lambda$ 为实数。证毕。

**工程意义**：实对称矩阵的特征值可以直接排序、比较大小（如 PCA 中的"方差贡献率"排序），不会出现复数特征值的尴尬。

### 定理2：实对称矩阵属于不同特征值的特征向量正交

**证明**：设 $A\boldsymbol{x}_1 = \lambda_1\boldsymbol{x}_1$，$A\boldsymbol{x}_2 = \lambda_2\boldsymbol{x}_2$，$\lambda_1 \neq \lambda_2$。计算：

$$\lambda_1(\boldsymbol{x}_1, \boldsymbol{x}_2) = (A\boldsymbol{x}_1)^T\boldsymbol{x}_2 = \boldsymbol{x}_1^T A^T\boldsymbol{x}_2 = \boldsymbol{x}_1^T A\boldsymbol{x}_2 = \lambda_2(\boldsymbol{x}_1, \boldsymbol{x}_2)$$

移项得 $(\lambda_1 - \lambda_2)(\boldsymbol{x}_1, \boldsymbol{x}_2) = 0$。因 $\lambda_1 \neq \lambda_2$，$(\boldsymbol{x}_1, \boldsymbol{x}_2) = 0$，即正交。证毕。

**对比**：对一般矩阵，不同特征值的特征向量只保证**线性无关**；实对称矩阵则升级为**正交**——这是"对称"带来的额外红利。

### 定理3：实对称矩阵一定可对角化（几何重数 = 代数重数）

比一般矩阵更强：一般矩阵要逐个检查几何重数是否等于代数重数，实对称矩阵**无条件成立**。因此实对称矩阵的特征向量总能凑齐 $n$ 个线性无关的，且经施密特正交化后还能凑齐 $n$ 个标准正交的。

## 2. 谱定理（本篇总纲）

**谱定理（Spectral Theorem）**：设 $A$ 为 $n$ 阶实对称矩阵，则存在正交矩阵 $Q$，使得：

$$Q^{-1}AQ = Q^TAQ = \Lambda = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$$

即实对称矩阵一定可以**正交对角化**。等价地：

$$A = Q\Lambda Q^T = \lambda_1\boldsymbol{q}_1\boldsymbol{q}_1^T + \lambda_2\boldsymbol{q}_2\boldsymbol{q}_2^T + \cdots + \lambda_n\boldsymbol{q}_n\boldsymbol{q}_n^T$$

其中 $\boldsymbol{q}_i$ 是 $Q$ 的第 $i$ 列（标准正交特征向量）。最后这个展开式称为 $A$ 的**谱分解**——它把 $A$ 表示成 $n$ 个秩 1 矩阵的加权和，每个"谱项" $\lambda_i\boldsymbol{q}_i\boldsymbol{q}_i^T$ 对应一个特征方向。谱分解是 PCA、低秩近似、量子力学中"可观测量的谱"的理论源头。

**谱定理的直观总结**：实对称矩阵 $A$ 可以被"旋转坐标轴"（乘正交矩阵 $Q$）变成对角形 $\Lambda$，旋转不改变几何（正交变换保长度保角度），所以"对称结构"在任何坐标系下都保持优雅。

## 3. 正交对角化的步骤

### 3.1 步骤（与一般对角化的区别只在第 4 步）

1. 求出 $A$ 的所有特征值；
2. 对每个特征值，求对应的特征向量（基础解系）；
3. 不同特征值的特征向量已自动正交（定理2）；
4. 同一特征值的特征向量用**施密特正交化**处理（022-023 篇的工具）；
5. 将所有特征向量**单位化**；
6. 以标准正交特征向量为列构造正交矩阵 $Q$，$Q^TAQ = \Lambda$。

注意第 4、5 步的顺序：先正交化再单位化（施密特正交化本身含单位化，可合并执行）。

### 3.2 完整示例1（无重根，最简情形）

将 $A = \begin{pmatrix} 2 & -2 \\ -2 & 5 \end{pmatrix}$ 正交对角化。

**步骤1**：特征多项式：

$$|A - \lambda I| = (2-\lambda)(5-\lambda) - 4 = \lambda^2 - 7\lambda + 6 = (\lambda-1)(\lambda-6)$$

特征值 $\lambda_1 = 1$，$\lambda_2 = 6$。

**步骤2**：求特征向量。

$\lambda_1 = 1$：$(A - I)\boldsymbol{x} = 0$：$\begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}\boldsymbol{x} = 0 \Rightarrow x_1 = 2x_2$，取 $\boldsymbol{x}_1 = (2, 1)^T$。

$\lambda_2 = 6$：$(A - 6I)\boldsymbol{x} = 0$：$\begin{pmatrix} -4 & -2 \\ -2 & -1 \end{pmatrix}\boldsymbol{x} = 0 \Rightarrow x_1 = -\frac{1}{2}x_2$，取 $\boldsymbol{x}_2 = (1, -2)^T$。

**步骤3**：不同特征值自动正交（可验证 $(2, 1) \cdot (1, -2) = 0$）。

**步骤4-5**：单位化：

$$\boldsymbol{q}_1 = \frac{1}{\sqrt{5}}(2, 1)^T, \quad \boldsymbol{q}_2 = \frac{1}{\sqrt{5}}(1, -2)^T$$

**步骤6**：

$$Q = \frac{1}{\sqrt{5}}\begin{pmatrix} 2 & 1 \\ 1 & -2 \end{pmatrix}, \quad \Lambda = \begin{pmatrix} 1 & 0 \\ 0 & 6 \end{pmatrix}$$

**验证**：$Q^TQ = \frac{1}{5}\begin{pmatrix} 4+1 & 2-2 \\ 2-2 & 1+4 \end{pmatrix} = I$（$Q$ 确为正交矩阵），且 $Q^TAQ = \Lambda$。

### 3.3 完整示例2（有重根，需正交化）

将 $A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$ 正交对角化。

**步骤1**：特征多项式（可利用"各行和相等"的技巧：每行和都是 4，故 $\lambda = 4$ 是特征值）：

$$|A - \lambda I| = (4-\lambda)(1-\lambda)^2$$

$\lambda_1 = 4$（单根），$\lambda_2 = 1$（二重根）。

**步骤2**：$\lambda_1 = 4$：$(A - 4I)\boldsymbol{x} = 0$，解得 $\boldsymbol{x}_1 = (1, 1, 1)^T$。

$\lambda_2 = 1$：$(A - I)\boldsymbol{x} = 0$，即 $x_1 + x_2 + x_3 = 0$，基础解系：

$$\boldsymbol{\alpha}_1 = (-1, 1, 0)^T, \quad \boldsymbol{\alpha}_2 = (-1, 0, 1)^T$$

**步骤3**：$\boldsymbol{x}_1$ 与 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2$ 已正交（不同特征值），但 $\boldsymbol{\alpha}_1$ 与 $\boldsymbol{\alpha}_2$ 同属 $\lambda = 1$，不一定正交（$(-1)(-1) + 0 + 0 = 1 \neq 0$），需施密特正交化。

**步骤4**：对 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2$ 施密特正交化：

$\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1 = (-1, 1, 0)^T$。

$(\boldsymbol{\alpha}_2, \boldsymbol{\beta}_1) = 1$，$(\boldsymbol{\beta}_1, \boldsymbol{\beta}_1) = 2$：

$$\boldsymbol{\beta}_2 = (-1, 0, 1)^T - \frac{1}{2}(-1, 1, 0)^T = \left(-\frac{1}{2}, -\frac{1}{2}, 1\right)^T$$

**步骤5**：单位化：

$$\boldsymbol{q}_1 = \frac{1}{\sqrt{3}}(1, 1, 1)^T, \quad \boldsymbol{q}_2 = \frac{1}{\sqrt{2}}(-1, 1, 0)^T, \quad \boldsymbol{q}_3 = \frac{1}{\sqrt{6}}(-1, -1, 2)^T$$

**步骤6**：

$$Q = \begin{pmatrix} \frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & 0 & \frac{2}{\sqrt{6}} \end{pmatrix}, \quad \Lambda = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

**验证**：$\boldsymbol{q}_2 \cdot \boldsymbol{q}_3 = \frac{1}{\sqrt{12}}(1 - 1 + 0) = 0$，三列两两正交且单位长，$Q^TAQ = \Lambda$。

## 4. 正交对角化的应用

### 4.1 二次型的标准化

实对称矩阵的正交对角化等价于用**正交变换**把二次型 $f = \boldsymbol{x}^TA\boldsymbol{x}$ 化为标准形（只含平方项）。这是 030 篇"二次型的标准形"的直接前置。

### 4.2 矩阵函数的计算

$$A = Q\Lambda Q^T \Rightarrow f(A) = Qf(\Lambda)Q^T$$

例如 $e^A = Qe^{\Lambda}Q^T$，$\sqrt{A} = Q\sqrt{\Lambda}Q^T$（正定时）。比一般对角化更省：$Q^{-1} = Q^T$ 无需求逆。

### 4.3 正定矩阵与极分解

谱分解给出判断正定性的快速通道：$A$ 正定 $\iff$ 特征值全为正。矩阵极分解 $A = QS$（$Q$ 正交、$S$ 半正定）也建立在谱分解之上。

### 4.4 主成分分析（PCA）

PCA 的核心是对协方差矩阵（实对称矩阵）做正交对角化：

- 特征值 $\lambda_i$ = 各主成分方向上的方差（贡献率 $= \lambda_i / \sum\lambda_j$）；
- 特征向量 $\boldsymbol{q}_i$ = 主成分方向（新坐标轴）。

由于特征值可排序、特征向量标准正交，PCA 的"取前 $k$ 个主成分降维"就是取谱分解的前 $k$ 大谱项——这就是"对称性"在数据科学中的直接红利。

## 5. 典型例题

### 例1（三阶实对称矩阵反求矩阵）

设 $A$ 为 3 阶实对称矩阵，$r(A) = 2$，$A^2 + 2A = O$，求 $A$ 的特征值。

**解**：设 $\lambda$ 为特征值，由 $A^2 + 2A = O$ 得 $\lambda^2 + 2\lambda = 0$，$\lambda = 0$ 或 $\lambda = -2$。

$A$ 是实对称矩阵，必可对角化，秩等于非零特征值个数（对角形中非零对角元个数）。$r(A) = 2$ 说明有两个非零特征值，故特征值为 $0, -2, -2$。

**方法总结**：实对称矩阵的"秩 = 非零特征值个数"这一性质（由可对角化保证）在抽象题中极其好用——一般矩阵并不满足（例如 $A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ 秩 1 但特征值 $1, 0$，非零特征值个数也是 1，但"可对角化"是前提；不可对角化时该结论失效）。

### 例2（正交矩阵与对称矩阵交叉题）

设 $A$ 为 $n$ 阶实对称矩阵，$A^2 = I$，$r(A + I) = r$，求 $|A - 2I|$。

**解**：$A^2 = I$ 推特征值 $\lambda = \pm 1$。$A + I$ 的特征值为 $\lambda + 1$：$2$（对应 $\lambda = 1$）和 $0$（对应 $\lambda = -1$）。$r(A + I) = $ 非零特征值个数 $= r$（$A + I$ 也是实对称矩阵，可对角化），故 $A$ 有 $r$ 个特征值 $1$，$n - r$ 个特征值 $-1$。

$A - 2I$ 的特征值为 $1 - 2 = -1$（$r$ 个）与 $-1 - 2 = -3$（$n - r$ 个），故：

$$|A - 2I| = (-1)^r \cdot (-3)^{n-r}$$

### 例3（秩 1 对称矩阵的特征分解）

设 $\boldsymbol{\alpha}$ 为非零 $n$ 维实向量，$A = \boldsymbol{\alpha}\boldsymbol{\alpha}^T$（秩 1 实对称矩阵），求 $A$ 的特征值，并写出它的谱分解。

**解**：$A\boldsymbol{\alpha} = \boldsymbol{\alpha}(\boldsymbol{\alpha}^T\boldsymbol{\alpha}) = \|\boldsymbol{\alpha}\|^2\boldsymbol{\alpha}$，故 $\lambda_1 = \|\boldsymbol{\alpha}\|^2$ 是特征值，$\boldsymbol{\alpha}$ 是对应特征向量。对任意 $\boldsymbol{x} \perp \boldsymbol{\alpha}$：$A\boldsymbol{x} = \boldsymbol{\alpha}(\boldsymbol{\alpha}^T\boldsymbol{x}) = 0$，故 $0$ 是 $n-1$ 重特征值（特征子空间是 $\boldsymbol{\alpha}^\perp$，维数 $n-1$）。

谱分解：设 $\boldsymbol{q}_1 = \dfrac{\boldsymbol{\alpha}}{\|\boldsymbol{\alpha}\|}$，则：

$$A = \|\boldsymbol{\alpha}\|^2 \boldsymbol{q}_1\boldsymbol{q}_1^T + 0 \cdot (\cdots) = \boldsymbol{\alpha}\boldsymbol{\alpha}^T$$

这正是"秩 1 对称矩阵的谱分解只有一项非零"——投影矩阵的原型。

## 6. 常见错误与对策

| 常见错误 | 错误类型 | 原因 | 纠正方法 |
| --- | --- | --- | --- |
| 忘记验证 $Q$ 是正交矩阵（$Q^TQ = I$） | 流程缺失 | 只做对角化不做正交化 | 每列必须两两正交且单位长；做完用 $Q^TQ$ 抽查 |
| 同一特征值的特征向量不施密特正交化就拼进 $Q$ | 算法遗漏 | 误以为"实对称 = 所有特征向量自动正交" | 自动正交只对**不同**特征值成立；同特征值的向量要施密特正交化 |
| 先单位化再正交化（顺序颠倒） | 算法顺序错误 | 混淆流程 | 先正交化（减投影），后单位化（除以模长） |
| 把"实对称必可对角化"推广到"任何矩阵必可对角化" | 概念混淆 | 混淆定理适用范围 | 一般矩阵要对每个重根检查 $m_g = m_a$；实对称矩阵才是无条件对角化 |
| 用"秩 = 非零特征值个数"处理不可对角化矩阵 | 前提条件忽略 | 忘记该结论依赖可对角化 | 先确认矩阵可对角化（实对称/特征值互异）再使用 |
| $Q^TAQ$ 中把 $Q^T$ 写成 $Q^{-1}$ 后不再处理 | 计算规范问题 | 忘记 $Q^{-1} = Q^T$ 的便利 | 验证时直接用 $Q^TAQ$，不必算 $Q^{-1}$ |

## 7. 实战练习

### 练习1（基础：二阶正交对角化）

将 $A = \begin{pmatrix} 1 & -2 \\ -2 & 1 \end{pmatrix}$ 正交对角化。

**提示**：特征多项式 $(1-\lambda)^2 - 4$；两个特征值互异，特征向量自动正交，只需单位化。

**参考答案要点**：$\lambda_1 = 3$，$\lambda_2 = -1$；$\boldsymbol{q}_1 = \frac{1}{\sqrt{2}}(1, -1)^T$，$\boldsymbol{q}_2 = \frac{1}{\sqrt{2}}(1, 1)^T$；$Q = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$，$\Lambda = \begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix}$。

### 练习2（进阶：三阶重根正交对角化）

将 $A = \begin{pmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1 \end{pmatrix}$ 正交对角化。

**提示**：特征值 $5$（单）与 $-1$（二重，见 025 篇 3.4）；对 $\lambda = -1$ 的两个基础解系向量做施密特正交化再单位化。

**参考答案要点**：$\lambda = 5$：$\boldsymbol{q}_1 = \frac{1}{\sqrt{3}}(1, 1, 1)^T$；$\lambda = -1$：先取 $\boldsymbol{\alpha}_1 = (-1, 1, 0)^T$，$\boldsymbol{\alpha}_2 = (-1, 0, 1)^T$，正交化得 $\boldsymbol{q}_2 = \frac{1}{\sqrt{2}}(-1, 1, 0)^T$，$\boldsymbol{q}_3 = \frac{1}{\sqrt{6}}(-1, -1, 2)^T$。$Q^TAQ = \text{diag}(5, -1, -1)$。

### 练习3（进阶：证明对称矩阵正交可对角化条件）

证明：若 $A$ 可正交对角化（存在正交 $Q$ 使 $Q^TAQ$ 为对角矩阵），则 $A$ 必为对称矩阵。

**提示**：对 $A = Q\Lambda Q^T$ 两边取转置，利用 $(\Lambda)^T = \Lambda$。

**参考答案要点**：$A^T = (Q\Lambda Q^T)^T = (Q^T)^T\Lambda^T Q^T = Q\Lambda Q^T = A$，故 $A$ 对称。这说明"可正交对角化"与"实对称"互为充要条件。

### 练习4（综合：利用特征值反求矩阵）

设 $A$ 为 2 阶实对称矩阵，特征值为 $3$ 与 $-1$，且属于 $3$ 的特征向量为 $(1, 1)^T$，求 $A$。

**提示**：用谱分解 $A = 3\boldsymbol{q}_1\boldsymbol{q}_1^T + (-1)\boldsymbol{q}_2\boldsymbol{q}_2^T$，其中 $\boldsymbol{q}_2$ 与 $\boldsymbol{q}_1$ 正交。

**参考答案要点**：$\boldsymbol{q}_1 = \frac{1}{\sqrt{2}}(1, 1)^T$，$\boldsymbol{q}_2 = \frac{1}{\sqrt{2}}(1, -1)^T$。$A = 3 \cdot \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} - 1 \cdot \frac{1}{2}\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$。验证：$A(1,1)^T = (3, 3)^T$，$A(1,-1)^T = (-1, 1)^T$。

### 练习5（挑战：谱分解的应用）

设 $A$ 为 $n$ 阶实对称矩阵，证明 $A = O$ 当且仅当 $A$ 的所有特征值为 0。

**提示**：必要性显然；充分性用谱分解 $A = Q\Lambda Q^T$，$\Lambda = O$ 时 $A = Q \cdot O \cdot Q^T = O$。

**参考答案要点**：若 $\Lambda = O$，则 $A = QOQ^T = O$。反方向：$A = O$ 时特征值全为 0 显然。故等价。推论：实对称矩阵 $\text{tr}(A^k) = 0$（对所有 $k$）时必有 $A = O$（因为特征值全为 0 且可对角化）。

## 8. 一句话记忆

**实对称矩阵是"对称建筑"：特征值全是实数，不同特征值的特征向量自动正交，且必可正交对角化 $A = Q\Lambda Q^T$——同一特征值的向量用施密特正交化补正交，最后全部单位化拼成 $Q$。**

## 参考链接与延伸阅读

- 同济大学数学科学学院《工程数学 线性代数（第七版）》，高等教育出版社，第 5 章 §4 对称矩阵的对角化（三个引理与谱定理的权威表述）：https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=630508ea938b7cc2960ef14b
- 山东理工大学线性代数课件 §5.4 实对称矩阵的相似对角形（特征值为实数的完整证明）：https://etcnew.sdut.edu.cn/meol/common/script/preview/download_preview.jsp?fileid=2451101&resid=524131&lid=39469&preview=preview
- Purdue University《Linear Algebra and its Applications》（Lay 教材讲义，§7.1 对称矩阵的对角化与谱定理，含不同特征值特征向量正交的证明）：https://www.math.purdue.edu/~xu1121/Sec7.1
- MIT 18.06 Linear Algebra（Strang 第 24-25 讲对称矩阵与正定矩阵、谱分解）：https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- LibreTexts Linear Algebra（8.2 正交对角化与主轴定理）：https://math.libretexts.org/Bookshelves/Linear_Algebra/Linear_Algebra_with_Applications_(Nicholson)/08%3A_Orthogonality/8.02%3A_Orthogonal_Diagonalization

延伸阅读：矩阵对角化（一般情形，前置知识）；施密特正交化（本篇第 4 步的工具）；二次型的标准形（正交对角化的直接应用）；特征值典型例题（实对称矩阵综合题）。
