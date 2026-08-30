---
order: 210
title: 特征值与特征向量计算
module: 'linear-algebra'
category: 数学
difficulty: intermediate
description: 特征值与特征向量的定义，特征方程与特征多项式，特征值与特征向量的计算步骤与方法（含重根情形），代数重数与几何重数，含 0 基础类比。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'linear-algebra/020-GramSchmidtOrthogonalization'
  - 'linear-algebra/022-EigenvalueProperties'
  - 'linear-algebra/023-MatrixDiagonalization'
prerequisites:
  - 'linear-algebra/001-DeterminantDefinitionAndGeometry'
---


## 0. 从一个生活场景说起：拉伸一张橡皮筋网格

在纸上画一张方格网，然后用双手把它均匀拉伸（比如横向拉长一倍）。你会发现：大多数格线都"变方向"了——原来的斜线拉伸后方向更平。但有两类格线很特殊：**横向的线只变长不变方向，纵向的线也不转向**。

矩阵作用在向量上，就像这次拉伸：大多数向量经过 $A$ 后方向和长度都变了，但总有少数"特殊方向"（如横向、纵向）在变换后**方向不变、只按某个倍数伸缩**。这些特殊方向就是**特征向量**，对应的伸缩倍数就是**特征值**。

本篇是"计算驱动"的实战篇，核心就三个问题：

1. 怎么求特征值？（解特征方程）
2. 怎么求特征向量？（解齐次方程组）
3. 特征值重了怎么办？（重根的处理）

掌握了这三步流水线，后面的性质篇、对角化篇就都顺了。

## 1. 特征值与特征向量的定义

### 1.1 定义（先看公式再解释）

设 $A$ 是 $n$ 阶方阵，若存在**数** $\lambda$ 和**非零向量** $\boldsymbol{x}$，使得：

$$A\boldsymbol{x} = \lambda\boldsymbol{x}$$

则称 $\lambda$ 为 $A$ 的**特征值**，$\boldsymbol{x}$ 为 $A$ 的属于特征值 $\lambda$ 的**特征向量**。

三个容易踩的细节（也是定义的本质）：

- **$\boldsymbol{x}$ 必须非零**。若允许 $\boldsymbol{x} = \mathbf{0}$，则 $A\mathbf{0} = \lambda\mathbf{0}$ 对任何 $\lambda$ 恒成立，特征值就失去意义了。
- 特征向量是"方向"不是"固定向量"：若 $\boldsymbol{x}$ 是特征向量，则 $k\boldsymbol{x}$（$k \neq 0$）也是同一个特征值的特征向量。
- 一个特征值通常对应**多个**线性无关的特征向量（它们构成一个子空间，见 1.3）。

### 1.2 等价表述（把方程改写成能算的形式）

$$A\boldsymbol{x} = \lambda\boldsymbol{x} \iff (A - \lambda I)\boldsymbol{x} = \mathbf{0}$$

$\boldsymbol{x} \neq \mathbf{0}$ 是 $(A - \lambda I)\boldsymbol{x} = \mathbf{0}$ 的非零解。由齐次方程组有非零解的充要条件（系数矩阵不满秩）：

$$|A - \lambda I| = 0$$

这一步是本篇的关键转化：**求特征值 = 解一个含参数 $\lambda$ 的行列式方程**。

### 1.3 特征空间

属于特征值 $\lambda$ 的所有特征向量加上零向量，构成一个子空间，称为 $\lambda$ 的**特征空间**：

$$V_\lambda = \{\boldsymbol{x} \mid A\boldsymbol{x} = \lambda\boldsymbol{x}\} = N(A - \lambda I)$$

特征空间的维数（即 $(A - \lambda I)\boldsymbol{x} = \mathbf{0}$ 基础解系所含向量个数）称为 $\lambda$ 的**几何重数**：

$$\dim(V_\lambda) = n - r(A - \lambda I)$$

## 2. 特征方程与特征多项式

### 2.1 特征方程与特征多项式

$$|A - \lambda I| = 0 \quad \text{称为特征方程}$$

$$f(\lambda) = |A - \lambda I| \quad \text{称为特征多项式}$$

特征多项式是关于 $\lambda$ 的 $n$ 次多项式。展开后：

$$f(\lambda) = |\lambda I - A| = \lambda^n - (\text{tr}A)\lambda^{n-1} + \cdots + (-1)^n|A|$$

其中：

- $\lambda^{n-1}$ 的系数为 $-\text{tr}(A) = -(a_{11} + a_{22} + \cdots + a_{nn})$；
- 常数项为 $(-1)^n|A|$。

这两个系数在"性质篇"会变成两个大杀器（迹 = 特征值之和，行列式 = 特征值之积），这里先认识它们。

### 2.2 一个实用技巧：$\lambda I - A$ 还是 $A - \lambda I$？

两种写法都能用（差一个 $(-1)^n$ 因子，根相同）。$|\lambda I - A|$ 的优点是最高次项系数为 $+1$，展开不易出错，推荐习惯用它。

## 3. 特征值与特征向量的计算步骤（核心流水线）

### 3.1 三步法

1. **求特征值**：计算特征多项式 $f(\lambda) = |\lambda I - A|$，解特征方程 $f(\lambda) = 0$，得到全部特征值（计入重数）；
2. **求特征向量**：对每个特征值 $\lambda_i$，解齐次方程组 $(\lambda_i I - A)\boldsymbol{x} = \mathbf{0}$（或 $(A - \lambda_i I)\boldsymbol{x} = \mathbf{0}$），求出基础解系；
3. **写答案**：特征向量的完整集合 = 基础解系的所有非零线性组合。

### 3.2 示例1（二阶矩阵，无重根）

求 $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ 的特征值与特征向量。

**步骤1**：

$$|A - \lambda I| = \begin{vmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{vmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda-1)(\lambda-3)$$

特征值 $\lambda_1 = 1$，$\lambda_2 = 3$。

**步骤2**：

对 $\lambda_1 = 1$：解 $(A - I)\boldsymbol{x} = 0$：

$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\boldsymbol{x} = 0 \Rightarrow x_1 + x_2 = 0$$

基础解系 $\boldsymbol{x}_1 = (1, -1)^T$，属于 $\lambda_1 = 1$ 的全部特征向量为 $k_1(1, -1)^T$（$k_1 \neq 0$）。

对 $\lambda_2 = 3$：解 $(A - 3I)\boldsymbol{x} = 0$：

$$\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}\boldsymbol{x} = 0 \Rightarrow x_1 - x_2 = 0$$

基础解系 $\boldsymbol{x}_2 = (1, 1)^T$，全部特征向量为 $k_2(1, 1)^T$（$k_2 \neq 0$）。

**步骤3（检验，必做）**：

$$A\boldsymbol{x}_1 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix} = 1 \cdot \boldsymbol{x}_1 \quad \checkmark \quad A\boldsymbol{x}_2 = \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3\boldsymbol{x}_2 \quad \checkmark$$

### 3.3 示例2（三阶矩阵）

求 $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 6 & -11 & 6 \end{pmatrix}$ 的特征值。

**解**：

$$|A - \lambda I| = \begin{vmatrix} -\lambda & 1 & 0 \\ 0 & -\lambda & 1 \\ 6 & -11 & 6-\lambda \end{vmatrix} = -\lambda^3 + 6\lambda^2 - 11\lambda + 6 = -(\lambda - 1)(\lambda - 2)(\lambda - 3)$$

特征值为 $\lambda_1 = 1$，$\lambda_2 = 2$，$\lambda_3 = 3$（三个互不相同的实根）。

**检验**：$\text{tr}(A) = 0 + 0 + 6 = 6 = 1 + 2 + 3$；$|A| = 6 = 1 \times 2 \times 3$。两条性质同时满足，计算可信。

（这个矩阵的特征向量与完整对角化见 027 篇例1。）

### 3.4 示例3（重根情形，同济教材经典题）

求 $A = \begin{pmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1 \end{pmatrix}$ 的特征值与特征向量。

**步骤1**：

$$|A - \lambda I| = \begin{vmatrix} 1-\lambda & 2 & 2 \\ 2 & 1-\lambda & 2 \\ 2 & 2 & 1-\lambda \end{vmatrix} = (5-\lambda)(-1-\lambda)^2$$

特征值 $\lambda_1 = 5$（单根），$\lambda_2 = -1$（二重根）。

**步骤2**：

对 $\lambda_1 = 5$：$(A - 5I)\boldsymbol{x} = 0$，由行变换得 $x_1 = x_2 = x_3$，基础解系 $\boldsymbol{x}_1 = (1, 1, 1)^T$。

对 $\lambda_2 = -1$：$(A + I)\boldsymbol{x} = 0$，即 $2x_1 + 2x_2 + 2x_3 = 0$，$x_1 + x_2 + x_3 = 0$。基础解系含 2 个向量：

$$\boldsymbol{x}_2 = (-1, 1, 0)^T, \quad \boldsymbol{x}_3 = (-1, 0, 1)^T$$

**注意**：$\lambda_2 = -1$ 的代数重数是 2，这里基础解系恰好有 2 个向量（几何重数 = 2），这种情况"重根也能配齐特征向量"，是可对角化的关键信号。若几何重数 < 代数重数（如 $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$），则配不齐，后续对角化会失败。

## 4. 代数重数与几何重数

### 4.1 定义

- **代数重数** $m_a(\lambda_i)$：$\lambda_i$ 作为特征方程根的重复次数；
- **几何重数** $m_g(\lambda_i)$：$\lambda_i$ 的特征空间维数，$m_g(\lambda_i) = n - r(A - \lambda_i I)$。

### 4.2 关系（判定对角化的重要工具）

$$1 \leq m_g(\lambda_i) \leq m_a(\lambda_i)$$

几何重数不超过代数重数。两者相等的特征值叫"完好的"，不等则意味着"缺特征向量"。

**示例**：$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$。特征值 $\lambda = 1$（二重根），代数重数 2；$A - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，$r(A - I) = 1$，几何重数 $= 2 - 1 = 1 < 2$。特征向量只有一个方向 $k(1, 0)^T$，配不齐两个无关特征向量——这是"不可对角化"的典型代表。

## 5. 特征向量的性质

### 5.1 基本性质

1. 特征向量必须非零；
2. 若 $\boldsymbol{x}$ 属于 $\lambda$，则 $k\boldsymbol{x}$（$k \neq 0$）也属于 $\lambda$；
3. 属于同一特征值的特征向量的非零线性组合，仍是该特征值的特征向量；
4. 属于**不同**特征值的特征向量线性无关。

### 5.2 核心定理（不同特征值的特征向量线性无关）

**定理**：设 $\lambda_1, \lambda_2, \ldots, \lambda_s$ 是 $A$ 的互不相同的特征值，$\boldsymbol{x}_i$ 是属于 $\lambda_i$ 的特征向量，则 $\boldsymbol{x}_1, \ldots, \boldsymbol{x}_s$ 线性无关。

**证明思路**（反证 + 归纳）：设 $k_1\boldsymbol{x}_1 + \cdots + k_s\boldsymbol{x}_s = 0$，两边左乘 $A$ 得 $\sum k_i\lambda_i\boldsymbol{x}_i = 0$；再乘 $\lambda_s$ 得 $\sum k_i\lambda_s\boldsymbol{x}_i = 0$，两式相减消去最后一项，对 $s-1$ 个向量归纳即可。

**推广**：属于不同特征值的各组线性无关特征向量，合在一起仍线性无关。

## 6. 特殊矩阵的特征值（秒杀结论）

| 矩阵类型 | 特征值结论 |
| --- | --- |
| 上（下）三角矩阵 | 特征值就是主对角线元素 |
| 对角矩阵 $\text{diag}(d_1, \ldots, d_n)$ | 特征值就是 $d_1, \ldots, d_n$ |
| 幂零矩阵（$A^k = O$） | 特征值全为 0 |
| 正交矩阵 | 特征值满足 $|\lambda| = 1$ |
| 幂等矩阵（$A^2 = A$） | 特征值只能是 0 或 1 |
| 对合矩阵（$A^2 = I$） | 特征值只能是 $\pm 1$ |

这些结论在考试与工程中经常直接使用，可以省去整套计算。

## 7. 常见错误与对策

| 常见错误 | 错误类型 | 原因 | 纠正方法 |
| --- | --- | --- | --- |
| 特征向量写成零向量 | 概念理解错误 | 忽略 $\boldsymbol{x} \neq \mathbf{0}$ 要求 | 基础解系取非零解；答案用"$k$ 乘基础解系，$k \neq 0$"表示 |
| 特征多项式展开丢符号（尤其三阶） | 计算错误 | $|A - \lambda I|$ 与 $|\lambda I - A|$ 混用 | 统一用 $|\lambda I - A|$（最高次系数 +1）；算完用 $\text{tr}$ 和 $|A|$ 复核 |
| 解 $(A - \lambda I)\boldsymbol{x} = 0$ 时把方程方向弄反 | 计算规范问题 | 代 $\lambda$ 时符号出错 | 先写 $(A - \lambda I)$ 再代入；特征值 $\lambda$ 只减主对角线 |
| 重根只写一个特征向量 | 流程缺失 | 漏算重根的完整基础解系 | 代数重数 $m$ 的特征值要解出 $m$ 个（或尽可能多）无关解向量 |
| 忘记检验 $A\boldsymbol{x} = \lambda\boldsymbol{x}$ | 流程缺失 | 只信计算 | 每题至少验一个特征向量，代入即知对错 |
| 用 $\text{tr}$ 和 $|A|$ 反推特征值时重根计数错 | 概念混淆 | 不知道计重数 | $n$ 阶矩阵恰有 $n$ 个特征值（计入代数重数），迹与行列式按重数累加 |

## 9. 一句话记忆

**特征值解特征方程 $|\lambda I - A| = 0$，特征向量解齐次方程组 $(\lambda I - A)\boldsymbol{x} = \mathbf{0}$；先算特征值（可用迹与行列式复核），再对每个特征值求基础解系，重根要数清重数。**
