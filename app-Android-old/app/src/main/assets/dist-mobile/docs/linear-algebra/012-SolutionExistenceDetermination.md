## 0. 一张决策图，回答全部问题

拿到一个线性方程组 $Ax = b$，先别急着消元求解。考试和工程里最常见的任务是：**先判断解的情况**。好消息是，判断只需要两个数——系数矩阵的秩 $r(A)$ 和增广矩阵的秩 $r(A \mid b)$。

<svg viewBox="0 0 860 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" role="img" aria-label="线性方程组解况判定决策图">
  <defs>
    <marker id="arrow-d" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#777"/></marker>
  </defs>
  <rect x="285" y="12" width="290" height="52" rx="10" fill="#2c3e50"/>
  <text x="430" y="34" text-anchor="middle" font-size="15" font-weight="bold" fill="#fff">Ax = b（m 个方程，n 个未知数）</text>
  <text x="430" y="53" text-anchor="middle" font-size="13" fill="#dbe6f2">第 1 步：增广矩阵 (A | b) 化行阶梯形，数出两个秩</text>
  <line x1="430" y1="64" x2="430" y2="95" stroke="#777" stroke-width="2" marker-end="url(#arrow-d)"/>
  <rect x="270" y="98" width="320" height="52" rx="10" fill="#fdf3e7" stroke="#b0702a" stroke-width="1.5"/>
  <text x="430" y="120" text-anchor="middle" font-size="15" font-weight="bold" fill="#2c3e50">r(A) 与 r(A | b) 相等吗？</text>
  <text x="430" y="139" text-anchor="middle" font-size="13" fill="#555">相等 ⟺ b 落在 A 的列空间里（有解）</text>
  <line x1="270" y1="124" x2="145" y2="124" stroke="#a33" stroke-width="2" marker-end="url(#arrow-d)"/>
  <text x="205" y="112" text-anchor="middle" font-size="13" fill="#a33">不相等</text>
  <line x1="590" y1="124" x2="700" y2="124" stroke="#3d8b5b" stroke-width="2" marker-end="url(#arrow-d)"/>
  <text x="648" y="112" text-anchor="middle" font-size="13" fill="#3d8b5b">相等，记公共值 r</text>
  <rect x="20" y="100" width="170" height="48" rx="10" fill="#fbeaea" stroke="#a33" stroke-width="1.5"/>
  <text x="105" y="122" text-anchor="middle" font-size="15" font-weight="bold" fill="#8b2f2f">无解</text>
  <text x="105" y="140" text-anchor="middle" font-size="12" fill="#8b2f2f">出现矛盾行 0 = c ≠ 0</text>
  <line x1="700" y1="150" x2="700" y2="180" stroke="#777" stroke-width="2" marker-end="url(#arrow-d)"/>
  <rect x="560" y="184" width="280" height="48" rx="10" fill="#eaf7ee" stroke="#3d8b5b" stroke-width="1.5"/>
  <text x="700" y="205" text-anchor="middle" font-size="14" font-weight="bold" fill="#2c3e50">r = n ?</text>
  <text x="700" y="223" text-anchor="middle" font-size="12" fill="#555">秩是否等于未知数个数</text>
  <line x1="560" y1="208" x2="400" y2="208" stroke="#a33" stroke-width="2" marker-end="url(#arrow-d)"/>
  <text x="478" y="196" text-anchor="middle" font-size="13" fill="#a33">否（r &lt; n）</text>
  <line x1="840" y1="208" x2="840" y2="240" stroke="#777" stroke-width="2" marker-end="url(#arrow-d)"/>
  <text x="860" y="200" text-anchor="middle" font-size="13" fill="#3d8b5b">是</text>
  <rect x="220" y="186" width="180" height="52" rx="10" fill="#fdf3e7" stroke="#b0702a" stroke-width="1.5"/>
  <text x="310" y="208" text-anchor="middle" font-size="14" font-weight="bold" fill="#2c3e50">无穷多解</text>
  <text x="310" y="227" text-anchor="middle" font-size="12" fill="#555">自由变量 n − r 个</text>
  <rect x="680" y="244" width="160" height="44" rx="10" fill="#eaf7ee" stroke="#3d8b5b" stroke-width="1.5"/>
  <text x="760" y="264" text-anchor="middle" font-size="14" font-weight="bold" fill="#2c3e50">唯一解</text>
  <text x="760" y="281" text-anchor="middle" font-size="12" fill="#555">x = A⁻¹b（方阵时）</text>
</svg>

**读图三步**：第一问"有没有解"看两个秩是否相等；第二问"解是否唯一"看秩是否等于 $n$。两张判断各只需要一次比较。

## 1. 三个必须先弄懂的小概念

### 1.1 解只有三种可能

线性方程组的解集只有三种形状：

| 情况 | 含义 | 几何形象 |
| --- | --- | --- |
| 无解 | 没有任何 $(x_1,\ldots,x_n)$ 满足全部方程 | 两条直线平行不交 |
| 唯一解 | 恰好一组解 | 两条直线交于一点 |
| 无穷多解 | 解由自由参数描述 | 两条直线完全重合 |

为什么不可能"恰好两组解"？因为解集是"平的"：如果 $\boldsymbol{x}^*$ 和 $\boldsymbol{y}^*$ 都是解，那么它们的加权平均 $t\boldsymbol{x}^* + (1-t)\boldsymbol{y}^*$ 也是解（代入验证即可）。有两个解，就自动有整条连线上的无穷多个解。

### 1.2 两个矩阵

- **系数矩阵** $A$（$m \times n$）：只装未知数的系数；
- **增广矩阵** $(A \mid b)$（$m \times (n+1)$）：系数右边再添一列常数项。

### 1.3 秩在说什么

秩 = 消元后非零行数 = 有效约束的个数。$r(A)$ 是"方程里真正独立的约束数"，$r(A \mid b)$ 是"把常数项也算进去后真正独立的行数"。

直觉先行：**如果常数项 $b$ 给方程组带来了新的独立约束，说明 $b$ 和系数列"对不上"，方程组无解**。用秩的语言说，就是 $r(A \mid b) > r(A)$。

## 2. 核心定理：Rouché–Capelli 定理

### 2.1 定理（这是全篇唯一必须背的结论）

设 $Ax = b$ 是 $m$ 个方程、$n$ 个未知数的线性方程组，$r = r(A)$。则：

$$\begin{cases} r(A) < r(A \mid b) & \Longrightarrow \text{无解} \\[4pt] r(A) = r(A \mid b) = n & \Longrightarrow \text{唯一解} \\[4pt] r(A) = r(A \mid b) = r < n & \Longrightarrow \text{无穷多解，自由变量 } n - r \text{ 个} \end{cases}$$

也就是说，**有解当且仅当 $r(A) = r(A \mid b)$**；有解时，**唯一当且仅当 $r(A) = n$**。

### 2.2 定理名字的小知识

这个定理在英文教材里叫 **Rouché–Capelli 定理**（以法国数学家 Eugène Rouché 和意大利数学家 Alfredo Capelli 命名），在东欧、俄语传统教材里也叫 **Kronecker–Capelli 定理**。中文教材通常不出现人名，直接叫**线性方程组有解的判定定理**或"秩判定定理"。考试写"由秩判定定理"即可，看到不同名字不要慌，说的是同一件事。

### 2.3 为什么成立：列空间视角

把 $Ax = b$ 展开成列向量的组合：

$$x_1\boldsymbol{\alpha}_1 + x_2\boldsymbol{\alpha}_2 + \cdots + x_n\boldsymbol{\alpha}_n = b$$

有解，就是问 $b$ 能不能写成 $A$ 的列向量的线性组合，即 $b$ 是否落在**列空间** $\mathrm{Col}(A)$ 里。而 $r(A \mid b)$ 恰好是 $\mathrm{Col}(A)$ 加上 $b$ 后撑开的维数：

$$b \in \mathrm{Col}(A) \iff \dim\,\mathrm{Col}(A\mid b) = \dim\,\mathrm{Col}(A) \iff r(A\mid b) = r(A)$$

至于"表示是否唯一"，取决于列向量是否线性无关，即 $r(A)$ 是否等于列数 $n$。

### 2.4 齐次情形的推论

对 $Ax = 0$（常数项全零），$b = \boldsymbol{0}$ 永远在列空间里，所以**齐次方程组永远有解（至少零解）**。真正的问题是：

$$Ax = 0 \text{ 有非零解} \iff r(A) < n$$

这是后续 015 篇和特征值理论的基石。

## 3. 操作流水线：四步拿结论

**第 1 步** 写出增广矩阵 $(A \mid b)$；
**第 2 步** 只做初等行变换，化为行阶梯形；
**第 3 步** 数两个秩：系数部分非零行数 $r_1$，整个增广矩阵非零行数 $r_2$；
**第 4 步** 套决策图：先比 $r_1$ 与 $r_2$，再比 $r_1$ 与 $n$。

> 手算时最容易犯的错是只对系数矩阵消元。必须带着 $b$ 列一起消，否则 $r(A \mid b)$ 根本数不出来。

**例 1**：判断方程组

$$\begin{cases} x_1 + x_2 + x_3 = 1 \\ 2x_1 + 3x_2 + x_3 = 3 \\ x_1 + 2x_2 = 2 \end{cases}$$

的解的情况。

**解**：化增广矩阵：

$$(A \mid b) = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 2 & 3 & 1 & 3 \\ 1 & 2 & 0 & 2 \end{pmatrix} \xrightarrow{r_2-2r_1,\ r_3-r_1} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & -1 & 1 \\ 0 & 1 & -1 & 1 \end{pmatrix} \xrightarrow{r_3-r_2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

系数部分 2 个非零行，整个增广矩阵也是 2 个非零行，所以 $r(A) = r(A \mid b) = 2$。又 $n = 3$，$r = 2 < 3$，结论：**无穷多解，自由变量 1 个**。

（通解是一条直线：$x = (2,0,-1)^T + k(2,-1,1)^T$，见 016 篇的非齐次通解求法。）

**如果写成代码，核心逻辑只有几行：**

```python
def classify_solution(A, b):
    """返回 ('无解' | '唯一解' | '无穷多解', 自由变量个数)"""
    import numpy as np
    from numpy.linalg import matrix_rank
    r1 = matrix_rank(A)            # 系数矩阵的秩
    r2 = matrix_rank(np.column_stack((A, b)))  # 增广矩阵的秩
    n = A.shape[1]                 # 未知数个数
    if r1 < r2:
        return '无解', 0           # 矛盾约束
    if r1 == n:
        return '唯一解', 0         # 满秩，恰有 n 个独立约束
    return '无穷多解', n - r1      # 缺 n - r1 个约束，自由变量 n - r1 个
```

## 4. 方阵快捷通道：行列式分流

当方程个数等于未知数个数（$m = n$，$A$ 是方阵）时，可以先算 $|A|$ 分流：

- $|A| \neq 0$：$A$ 可逆，**对任意 $b$ 都有唯一解** $x = A^{-1}b$，不用再消元；
- $|A| = 0$：**不能下结论**，可能是无解也可能是无穷多解，必须回到秩判定。

$|A| = 0$ 时最常见的错误是直接说"无解"。反例：$x_1 + x_2 = 1$ 与 $2x_1 + 2x_2 = 2$ 这两个方程系数行列式为零，但显然有无穷多解。

## 5. 含参数方程组的"分类讨论模板"

含参数题（$\lambda$ 出现在系数里）是高频考点，套路固定，按模板走不会漏情况：

**模板四步：**

1. **算 $|A|$**（方阵时），把使 $|A| = 0$ 的参数值全部解出来；
2. **非临界值**：$|A| \neq 0$，直接回答"有唯一解"（可用克莱姆法则求，见 005 篇）；
3. **临界值逐个代入**：对每个使 $|A| = 0$ 的 $\lambda$，代入原增广矩阵化阶梯形，比较 $r(A)$ 与 $r(A \mid b)$；
4. **汇总成表**：按 $\lambda$ 的取值分段写出结论。

> 漏掉第 3 步是这类题丢分的头号原因：**临界值处不一定无解，往往是无穷多解**。

**例 2**：讨论方程组

$$\begin{cases} x_1 + x_2 + x_3 = 1 \\ x_1 + \lambda x_2 + x_3 = \lambda \\ x_1 + x_2 + \lambda x_3 = \lambda^2 \end{cases}$$

的解的情况。

**第 1 步**：

$$|A| = \begin{vmatrix} 1 & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{vmatrix} = \begin{vmatrix} 1 & 1 & 1 \\ 0 & \lambda-1 & 0 \\ 0 & 0 & \lambda-1 \end{vmatrix} = (\lambda-1)^2$$

临界值只有 $\lambda = 1$。

**第 2 步**：$\lambda \neq 1$ 时 $|A| \neq 0$，**有唯一解**。

**第 3 步**：$\lambda = 1$ 时代入，三个方程都变成 $x_1 + x_2 + x_3 = 1$，增广矩阵：

$$\begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

$r(A) = r(A \mid b) = 1 < 3$，**无穷多解，自由变量 2 个**。

**第 4 步汇总**：

| $\lambda$ 取值 | 结论 |
| --- | --- |
| $\lambda \neq 1$ | 唯一解 |
| $\lambda = 1$ | 无穷多解（2 个自由变量） |

## 6. 换个视角：列空间与几何

### 6.1 列空间视角（和 019 篇打通）

设 $A$ 的列向量为 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_n$：

- $b \in \mathrm{Col}(A)$ $\iff$ 有解；
- 表示唯一 $\iff$ 列向量线性无关（$r(A) = n$）$\iff$ 唯一解；
- 表示不唯一 $\iff$ 列向量线性相关 $\iff$ 无穷多解。

所以"解方程组"本质上就是"把 $b$ 拆成列向量的线性组合"。

### 6.2 几何视角

- 二元：每行是一条直线。交于一点 / 重合 / 平行不交，对应唯一解 / 无穷多解 / 无解；
- 三元：每行是一个平面。三面交于一点 / 交于一条线 / 无公共点；
- 一般：有解时解集是 $\mathbb{R}^n$ 中一个 $n - r$ 维的"平直子空间"（仿射子空间），无解时是空集。

注意"三元三个平面两两相交但无公共点"也能造成无解——所以几何直觉只用来辅助，最终判定永远以秩为准。

## 7. 常见错误与对策

| 错误示例 | 错误类型 | 原因分析 | 纠正方法 |
| --- | --- | --- | --- |
| 只看 $r(A)$ 就下结论 | 判定残缺 | 忘了比较增广矩阵 | 两个秩必须都数出来再比 |
| $m < n$ 就断言"有解" | 推论误用 | 混淆齐次/非齐次 | $m<n$ 只保证齐次有非零解；非齐次用秩判定 |
| $|A| = 0$ 断言"无解" | 结论过强 | 把"无唯一解"当"无解" | $|A|=0$ 后必须代入增广矩阵算秩 |
| 把 $n$ 当成方程个数 | 符号混淆 | $n$ 是未知数个数 | 记住"$r = n$ 才唯一"，$m$ 是行数 |
| 参数题只算 $|A| = 0$ 的根 | 讨论不全 | 没在临界值处继续判定 | 每个临界值代入增广矩阵，比较两秩 |
| 消元丢掉 $b$ 列 | 工具误用 | 只对系数矩阵消元 | 增广矩阵整体行变换，$b$ 列全程保留 |
| 认为"秩相等=唯一解" | 逻辑遗漏 | 漏掉 $=n$ 的第二条件 | 两步走：等号管有解，$=n$ 管唯一 |

## 9. 一页速查卡

```text
判定线性方程组 Ax = b 解况
----------------------------
① 增广矩阵 (A|b) 化行阶梯形
② 数 r₁ = r(A)，r₂ = r(A|b)
③ r₁ < r₂          → 无解
   r₁ = r₂ = n      → 唯一解
   r₁ = r₂ < n      → 无穷多解（自由变量 n − r₁）

方阵捷径：|A| ≠ 0 → 唯一解；|A| = 0 → 回到 ③
齐次特例：Ax = 0 有非零解 ⟺ r(A) < n
```
