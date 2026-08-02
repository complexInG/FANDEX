---
order: 44
title: 施密特正交化
module: 'linear-algebra'
category: 'comp-sci'
difficulty: intermediate
description: Gram-Schmidt 正交化的算法步骤（投影-减去），正交矩阵的定义与性质，正交对角化基础，含 0 基础类比。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'linear-algebra/坐标与坐标变换'
  - 'linear-algebra/内积与正交性'
  - 'linear-algebra/特征值与特征向量计算'
prerequisites:
  - 'linear-algebra/行列式定义与几何意义'
---

## 0. 从一个生活场景说起：把歪斜的坐标轴掰正

你买了个书架，组装时发现每层隔板都"歪"了——相邻隔板之间既不平行也不垂直，整个架子摇摇晃晃。怎么修？装修师傅的做法是：先固定第一块板，然后以它为基准，把第二块板中"和第一块板重叠（平行）的部分"刨掉，只保留"与第一块板垂直的方向"，这样第二块板就和第一块板垂直了；第三块板同理，把"与第一、二块板重叠的部分"都刨掉……

这个"**留下垂直的部分、刨掉平行（投影）的部分**"的工序，就是本篇的主角——**施密特正交化（Gram-Schmidt 过程）**。它把一组"歪七扭八"的线性无关向量，一步步改造成一组两两垂直（正交）的向量，再拉成单位长度，就得到一组标准正交基。

为什么值得做这件事？上一篇文章提到：标准正交基下求坐标只需做内积，不用解方程组；本篇的算法就是"制造"标准正交基的流水线。它还是 QR 分解、最小二乘法、实对称矩阵正交对角化的共同地基。

## 1. 预备知识：投影公式（算法的"刨刀"）

正交化的每一步都要用到同一个工具：**向量在另一向量方向上的投影**。

设 $\boldsymbol{\alpha}$ 向非零向量 $\boldsymbol{\beta}$ 的方向投影，投影向量为：

$$\text{proj}_{\boldsymbol{\beta}} \boldsymbol{\alpha} = \frac{(\boldsymbol{\alpha}, \boldsymbol{\beta})}{(\boldsymbol{\beta}, \boldsymbol{\beta})}\boldsymbol{\beta}$$

理解：系数 $\dfrac{(\boldsymbol{\alpha}, \boldsymbol{\beta})}{(\boldsymbol{\beta}, \boldsymbol{\beta})}$ 是一个数（标量），它决定了"$\boldsymbol{\alpha}$ 在 $\boldsymbol{\beta}$ 方向上的分量有多大"，再乘上 $\boldsymbol{\beta}$ 本身，就得到投影向量。

关键性质（几何直觉）：**$\boldsymbol{\alpha}$ 减去它在 $\boldsymbol{\beta}$ 上的投影，所得向量与 $\boldsymbol{\beta}$ 正交**。验证一下：

$$\left(\boldsymbol{\alpha} - \frac{(\boldsymbol{\alpha}, \boldsymbol{\beta})}{(\boldsymbol{\beta}, \boldsymbol{\beta})}\boldsymbol{\beta}, \boldsymbol{\beta}\right) = (\boldsymbol{\alpha}, \boldsymbol{\beta}) - \frac{(\boldsymbol{\alpha}, \boldsymbol{\beta})}{(\boldsymbol{\beta}, \boldsymbol{\beta})}(\boldsymbol{\beta}, \boldsymbol{\beta}) = 0$$

这就是"投影-减去"的核心：**减去投影 = 留下垂直分量**。

## 2. 施密特正交化算法

### 2.1 问题提出

给定一组线性无关的向量 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \ldots, \boldsymbol{\alpha}_s$，如何构造一组与之等价的正交向量组 $\boldsymbol{\beta}_1, \boldsymbol{\beta}_2, \ldots, \boldsymbol{\beta}_s$？"等价"是指张成的子空间逐层相同：

$$\text{span}\{\boldsymbol{\beta}_1, \ldots, \boldsymbol{\beta}_k\} = \text{span}\{\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_k\}, \quad k = 1, \ldots, s$$

### 2.2 算法步骤（两步一组，逐个处理）

**第 1 步**：第一个向量原样保留。

$$\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1$$

**第 2 步**：从 $\boldsymbol{\alpha}_2$ 中减去其在 $\boldsymbol{\beta}_1$ 上的投影（刨掉与 $\boldsymbol{\beta}_1$ 平行的部分）。

$$\boldsymbol{\beta}_2 = \boldsymbol{\alpha}_2 - \frac{(\boldsymbol{\alpha}_2, \boldsymbol{\beta}_1)}{(\boldsymbol{\beta}_1, \boldsymbol{\beta}_1)}\boldsymbol{\beta}_1$$

**第 3 步**：从 $\boldsymbol{\alpha}_3$ 中减去其在 $\boldsymbol{\beta}_1$ 和 $\boldsymbol{\beta}_2$ 上的两个投影（刨掉与 $\boldsymbol{\beta}_1$、$\boldsymbol{\beta}_2$ 平行的部分）。

$$\boldsymbol{\beta}_3 = \boldsymbol{\alpha}_3 - \frac{(\boldsymbol{\alpha}_3, \boldsymbol{\beta}_1)}{(\boldsymbol{\beta}_1, \boldsymbol{\beta}_1)}\boldsymbol{\beta}_1 - \frac{(\boldsymbol{\alpha}_3, \boldsymbol{\beta}_2)}{(\boldsymbol{\beta}_2, \boldsymbol{\beta}_2)}\boldsymbol{\beta}_2$$

**一般地**（第 $k$ 步）：

$$\boldsymbol{\beta}_k = \boldsymbol{\alpha}_k - \sum_{j=1}^{k-1} \frac{(\boldsymbol{\alpha}_k, \boldsymbol{\beta}_j)}{(\boldsymbol{\beta}_j, \boldsymbol{\beta}_j)}\boldsymbol{\beta}_j, \quad k = 2, 3, \ldots, s$$

### 2.3 几何理解（为什么这样能行）

每一步的本质是：

$$\boldsymbol{\beta}_k = \boldsymbol{\alpha}_k - \text{proj}_{\text{span}(\boldsymbol{\beta}_1, \ldots, \boldsymbol{\beta}_{k-1})} \boldsymbol{\alpha}_k$$

即：$\boldsymbol{\beta}_k$ 等于 $\boldsymbol{\alpha}_k$ 减去它在前 $k-1$ 个已正交向量张成的子空间上的投影，剩下的就是"与前 $k-1$ 个方向都垂直"的余量。由于 $\boldsymbol{\alpha}_k$ 与 $\boldsymbol{\beta}_1, \ldots, \boldsymbol{\beta}_{k-1}$ 线性无关（原向量组线性无关），这个余量一定非零。逐层推进，最终得到 $s$ 个两两正交的非零向量。

注意：**必须按顺序处理**。第 $k$ 步只减前 $k-1$ 个投影，绝不能回头减后面的，否则会破坏已完成的步骤。

### 2.4 单位化（把长度拉成 1）

正交化只保证"垂直"，要得到**标准正交**向量组，还要把每个向量单位化：

$$\boldsymbol{e}_k = \frac{\boldsymbol{\beta}_k}{\|\boldsymbol{\beta}_k\|}, \quad k = 1, \ldots, s$$

单位化不改变方向，只把长度缩放到 1。至此，$\boldsymbol{e}_1, \ldots, \boldsymbol{e}_s$ 就是与原向量组等价的标准正交向量组。

### 2.5 完整示例（教科书经典题）

设 $\boldsymbol{\alpha}_1 = (1, 1, 0)^T$，$\boldsymbol{\alpha}_2 = (1, 0, 1)^T$，$\boldsymbol{\alpha}_3 = (0, 1, 1)^T$，用施密特正交化求标准正交组。

**步骤1**：$\boldsymbol{\beta}_1 = \boldsymbol{\alpha}_1 = (1, 1, 0)^T$。

**步骤2**：算投影系数并减去：

$$(\boldsymbol{\alpha}_2, \boldsymbol{\beta}_1) = 1 + 0 + 0 = 1, \quad (\boldsymbol{\beta}_1, \boldsymbol{\beta}_1) = 1 + 1 + 0 = 2$$

$$\boldsymbol{\beta}_2 = (1, 0, 1)^T - \frac{1}{2}(1, 1, 0)^T = \left(\frac{1}{2}, -\frac{1}{2}, 1\right)^T$$

**步骤3**：对 $\boldsymbol{\alpha}_3$ 减去两个投影：

$$(\boldsymbol{\alpha}_3, \boldsymbol{\beta}_1) = 0 + 1 + 0 = 1, \quad (\boldsymbol{\alpha}_3, \boldsymbol{\beta}_2) = 0 + \left(-\frac{1}{2}\right) + 1 = \frac{1}{2}, \quad (\boldsymbol{\beta}_2, \boldsymbol{\beta}_2) = \frac{1}{4} + \frac{1}{4} + 1 = \frac{3}{2}$$

$$\boldsymbol{\beta}_3 = (0, 1, 1)^T - \frac{1}{2}(1, 1, 0)^T - \frac{1/2}{3/2}\left(\frac{1}{2}, -\frac{1}{2}, 1\right)^T$$

$$= (0, 1, 1)^T - \left(\frac{1}{2}, \frac{1}{2}, 0\right)^T - \left(\frac{1}{6}, -\frac{1}{6}, \frac{1}{3}\right)^T = \left(-\frac{2}{3}, \frac{2}{3}, \frac{2}{3}\right)^T$$

**步骤4**：单位化。

$$\|\boldsymbol{\beta}_1\| = \sqrt{2}, \quad \|\boldsymbol{\beta}_2\| = \sqrt{3/2}, \quad \|\boldsymbol{\beta}_3\| = \sqrt{4/9 + 4/9 + 4/9} = \frac{2\sqrt{3}}{3}$$

$$\boldsymbol{e}_1 = \frac{1}{\sqrt{2}}(1, 1, 0)^T, \quad \boldsymbol{e}_2 = \frac{1}{\sqrt{6}}(1, -1, 2)^T, \quad \boldsymbol{e}_3 = \frac{1}{\sqrt{3}}(-1, 1, 1)^T$$

**检验**（正交性自查，必做）：$(\boldsymbol{e}_1, \boldsymbol{e}_2) = \frac{1}{\sqrt{12}}(1 - 1 + 0) = 0$；$(\boldsymbol{e}_1, \boldsymbol{e}_3) = \frac{1}{\sqrt{6}}(-1 + 1 + 0) = 0$；$(\boldsymbol{e}_2, \boldsymbol{e}_3) = \frac{1}{\sqrt{18}}(-1 - 1 + 2) = 0$。全部通过。

## 3. 正交矩阵（正交化的"成品包装"）

### 3.1 定义

把 $n$ 个 $n$ 维标准正交向量按列排成矩阵 $A$，就得到**正交矩阵**：

$$A^TA = I \quad \text{或} \quad A^{-1} = A^T$$

正交矩阵的逆就是它的转置——求逆的成本瞬间降为零，这是它最大的实用价值。

### 3.2 等价条件（六条判定）

以下条件等价：

1. $A$ 是正交矩阵；
2. $A^TA = I$；
3. $AA^T = I$；
4. $A^{-1} = A^T$；
5. $A$ 的列向量构成 $\mathbb{R}^n$ 的标准正交基；
6. $A$ 的行向量构成 $\mathbb{R}^n$ 的标准正交基。

注意第 5、6 条：只要列（或行）向量两两正交且长度都为 1，矩阵必是正交矩阵。

### 3.3 正交矩阵的性质

1. $|A| = \pm 1$；
2. $A^{-1}$ 也是正交矩阵；
3. $A^T$ 也是正交矩阵；
4. 两个正交矩阵的乘积仍是正交矩阵；
5. 正交变换保持内积：$(A\boldsymbol{\alpha}, A\boldsymbol{\beta}) = (\boldsymbol{\alpha}, \boldsymbol{\beta})$；
6. 正交变换保持长度：$\|A\boldsymbol{\alpha}\| = \|\boldsymbol{\alpha}\|$；
7. 正交变换保持距离和角度。

### 3.4 几何意义与常见例子

正交矩阵对应的线性变换是**刚体运动**（旋转，或旋转加反射）：$|A| = 1$ 是旋转，$|A| = -1$ 是旋转加镜像。它不拉伸、不压缩、不歪曲，只转动或翻面。

**二维旋转矩阵**（最经典的正交矩阵）：

$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

**置换矩阵**：每行每列恰好有一个 1、其余为 0（例如 $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$），也是正交矩阵。

## 4. 施密特正交化的应用

### 4.1 构造标准正交基

把向量空间的任意一组基按算法改造，即得标准正交基——这是全篇的出发点。

### 4.2 QR 分解（算法顺带的"赠品"）

任意 $m \times n$ 矩阵（$m \geq n$，列满秩）可分解为 $A = QR$，其中 $Q$ 的列是 $A$ 的列向量施密特正交化（含单位化）的结果，$R$ 是 $n \times n$ 上三角矩阵。QR 分解是数值稳定的求解与最小二乘工具。

### 4.3 最小二乘法

超定方程组 $Ax \approx b$ 的最小二乘解等价于求解正规方程 $A^TAx = A^Tb$。用 QR 分解可避免求 $A^TA$（数值上更稳）：

$$x = R^{-1}Q^Tb$$

### 4.4 实对称矩阵的正交对角化

对实对称矩阵：不同特征值对应的特征向量自动正交；同一特征值对应的多个特征向量则需要用施密特正交化"掰正"。这是下一篇 028 的核心流程。

### 例1（验证正交矩阵）

验证 $A = \begin{pmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & 0 & -\frac{2}{\sqrt{6}} \end{pmatrix}$ 是正交矩阵。

**解**：按"列向量是标准正交组"判定。三列的列内积：

$(1,1)$ 元素：$\frac{1}{3} + \frac{1}{3} + \frac{1}{3} = 1$（第 1 列单位长）。

$(1,2)$ 元素：$\frac{1}{\sqrt{3}\sqrt{2}} - \frac{1}{\sqrt{3}\sqrt{2}} + 0 = 0$（第 1、2 列正交）。

$(2,2)$ 元素：$\frac{1}{2} + \frac{1}{2} + 0 = 1$；$(3,3)$ 元素：$\frac{1}{6} + \frac{1}{6} + \frac{4}{6} = 1$。

$(1,3)$ 元素：$\frac{1}{\sqrt{18}} + \frac{1}{\sqrt{18}} - \frac{2}{\sqrt{18}} = 0$；$(2,3)$ 元素：$\frac{1}{\sqrt{12}} - \frac{1}{\sqrt{12}} + 0 = 0$。

所有列两两正交、长度均为 1，故 $A$ 是正交矩阵，$A^TA = I$。

### 例2（正交矩阵行列式的应用）

设 $A$ 为正交矩阵，$|A| = -1$，证明 $|A + I| = 0$。

**证明**：利用 $A^TA = I$ 和 $A^T = A^{-1}$ 做"凑恒等变换"：

$$|A + I| = |A + AA^T| = |A(I + A^T)| = |A| \cdot |I + A^T| = -|I + A^T|$$

而 $|I + A^T| = |(I + A)^T| = |I + A| = |A + I|$，代入得：

$$|A + I| = -|A + I| \Rightarrow 2|A + I| = 0 \Rightarrow |A + I| = 0$$

几何含义：$|A| = -1$ 的正交变换是"旋转 + 镜像"，$A + I$ 奇异说明存在非零向量 $\boldsymbol{x}$ 使 $A\boldsymbol{x} = -\boldsymbol{x}$（$-1$ 是特征值），即反射轴上总有不动方向。

### 例3（用算法处理含参数向量）

对 $\boldsymbol{\alpha}_1 = (1, 0, 1)^T$，$\boldsymbol{\alpha}_2 = (0, 1, 1)^T$ 做施密特正交化并单位化（二维子空间 $\subset \mathbb{R}^3$）。

**解**：$\boldsymbol{\beta}_1 = (1, 0, 1)^T$。$(\boldsymbol{\alpha}_2, \boldsymbol{\beta}_1) = 1$，$(\boldsymbol{\beta}_1, \boldsymbol{\beta}_1) = 2$。

$$\boldsymbol{\beta}_2 = (0, 1, 1)^T - \frac{1}{2}(1, 0, 1)^T = \left(-\frac{1}{2}, 1, \frac{1}{2}\right)^T$$

单位化：$\|\boldsymbol{\beta}_1\| = \sqrt{2}$，$\|\boldsymbol{\beta}_2\| = \sqrt{\frac{1}{4} + 1 + \frac{1}{4}} = \frac{\sqrt{6}}{2}$。

$$\boldsymbol{e}_1 = \frac{1}{\sqrt{2}}(1, 0, 1)^T, \quad \boldsymbol{e}_2 = \frac{1}{\sqrt{6}}(-1, 2, 1)^T$$

**检验**：$(\boldsymbol{e}_1, \boldsymbol{e}_2) = \frac{1}{\sqrt{12}}(-1 + 0 + 1) = 0$。通过。

## 6. 常见错误与对策

| 常见错误 | 错误类型 | 原因 | 纠正方法 |
| --- | --- | --- | --- |
| 公式中的系数 $\dfrac{(\boldsymbol{\alpha}_k, \boldsymbol{\beta}_j)}{(\boldsymbol{\beta}_j, \boldsymbol{\beta}_j)}$ 分母写成 $(\boldsymbol{\alpha}_j, \boldsymbol{\alpha}_j)$ | 公式记忆错误 | 混淆投影公式的分子分母 | 分母永远是"被投影方向"的自内积 $(\boldsymbol{\beta}_j, \boldsymbol{\beta}_j)$ |
| 对 $\boldsymbol{\alpha}_k$ 减去"自己已算出的 $\boldsymbol{\beta}_k$ 的投影" | 算法顺序错误 | 没理解逐层推进 | 第 $k$ 步只减 $\boldsymbol{\beta}_1$ 到 $\boldsymbol{\beta}_{k-1}$ 的投影，不含 $\boldsymbol{\beta}_k$ 本身 |
| 忘记单位化就声称得到"标准正交组" | 流程缺失 | 把正交化当终点 | 正交化后必须逐向量除以模长，才算标准正交 |
| 正交化结果不做内积验证 | 流程缺失 | 迷信计算 | 算完后抽查 $(\boldsymbol{\beta}_i, \boldsymbol{\beta}_j) = 0$（$i \neq j$），一步验证全错 |
| 直接用正交化处理"线性相关"的向量组 | 前提条件忽略 | 没检查线性无关性 | 施密特正交化只对线性无关组有效；相关组中会出现 $\boldsymbol{\beta}_k = 0$ |
| 把"正交矩阵"与"对称矩阵"混淆 | 概念混淆 | 对矩阵分类不清晰 | 正交矩阵 $A^TA = I$（列标准正交）；对称矩阵 $A^T = A$（沿对角线对称） |

## 8. 一句话记忆

**施密特正交化就是"逐个减去前面方向的投影"：$\boldsymbol{\beta}_k = \boldsymbol{\alpha}_k - \sum_{j<k}\dfrac{(\boldsymbol{\alpha}_k, \boldsymbol{\beta}_j)}{(\boldsymbol{\beta}_j, \boldsymbol{\beta}_j)}\boldsymbol{\beta}_j$，刨掉平行分量留下垂直分量，最后统一单位化。**
