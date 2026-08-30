## 开篇思想实验：四个向量，能不能压缩成两个？

假设你的程序里存了四个向量：

$$\boldsymbol{\alpha}_1 = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix},\quad
\boldsymbol{\alpha}_2 = \begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix},\quad
\boldsymbol{\alpha}_3 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix},\quad
\boldsymbol{\alpha}_4 = \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}$$

直接存要存 12 个数。但仔细一看：

$$\boldsymbol{\alpha}_2 = 2\boldsymbol{\alpha}_1, \qquad \boldsymbol{\alpha}_4 = \boldsymbol{\alpha}_1 - \boldsymbol{\alpha}_3$$

第二个向量只是第一个的复制放大，第四个向量只是第一、三个的"加减组合"。也就是说，**真正不可互相替代的只有 $\boldsymbol{\alpha}_1$ 和 $\boldsymbol{\alpha}_3$ 两个**。只要存下这两个，另外两个随时能算出来：

$$\boldsymbol{\alpha}_2 = 2\boldsymbol{\alpha}_1, \qquad \boldsymbol{\alpha}_4 = \boldsymbol{\alpha}_1 - \boldsymbol{\alpha}_3$$

存储量从 12 个数压缩到 6 个数。这个"最少需要几个向量"的答案，就是本篇的**维数（dimension）**；被保留下来的那组"骨架"向量，就是**基（basis）**；寻找骨架的过程，就是求**极大线性无关组**。

> 本篇与 019 篇（线性相关性）的分工：019 回答"一组向量是否冗余、谁冗余"；本篇回答"冗余去掉后剩几个、剩下的是不是空间的地基、换一套地基坐标怎么变"。

下面先通过一个完整例子把全部概念串一遍，再逐层展开定义、性质和操作流程。

## 1. 一镜到底：用同一个例子走完全程

继续用上面的四个向量。把它们按列排成矩阵：

$$A = (\boldsymbol{\alpha}_1\ \boldsymbol{\alpha}_2\ \boldsymbol{\alpha}_3\ \boldsymbol{\alpha}_4) = \begin{pmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 1 & 1 \\ 3 & 6 & 1 & 2 \end{pmatrix}$$

**第一步，化行阶梯形（初等行变换）：**

$$A \xrightarrow{r_2-2r_1,\ r_3-3r_1} \begin{pmatrix} 1 & 2 & 1 & 0 \\ 0 & 0 & -1 & 1 \\ 0 & 0 & -2 & 2 \end{pmatrix} \xrightarrow{r_3-2r_2} \begin{pmatrix} 1 & 2 & 1 & 0 \\ 0 & 0 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

**第二步，数主元（每行第一个非零元素）：** 主元在第 1 列和第 3 列。

**第三步，读结论：**

| 概念 | 本例答案 | 含义 |
| --- | --- | --- |
| 极大线性无关组 | $\{\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_3\}$ | 主元所在列对应的原向量 |
| 向量组的秩 | $2$ | 极大无关组所含向量个数 |
| 生成子空间 | $\mathrm{span}(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\boldsymbol{\alpha}_3,\boldsymbol{\alpha}_4)$ | 所有线性组合构成的集合 |
| 该子空间的基 | $\{\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_3\}$ | 能生成全部、又线性无关 |
| 该子空间的维数 | $\dim = 2$ | 基里向量的个数 |

一个例子同时产出五个概念，说明它们本来就是同一件事的不同侧面：**"去掉冗余之后剩下多少"就是维数，"剩下的是哪几个"就是基**。

接下来的小节逐个展开。全文的 SVG 路线图放在第 2 节末尾，建议学完第 6 节后再回来看一遍。

## 2. 极大线性无关组：去掉冗余的"骨架"

### 2.1 为什么先讲它

019 篇已经讲过：向量组线性相关，意味着其中至少有一个向量能由其余向量线性表示。那么自然的问题就是：**能不能从一组向量里挑出一个"既无冗余、又能代表全部"的子集？** 这个子集就是极大线性无关组。

### 2.2 定义（两个条件，缺一不可）

设 $S = \{\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s\}$ 是一个向量组，它的部分组 $S_0$ 称为 $S$ 的**极大线性无关组**，如果：

1. **自身无关**：$S_0$ 线性无关；
2. **不能再加**：把 $S$ 中任何一个未被选中的向量加入 $S_0$，得到的组立刻线性相关。

条件 2 换个说法更常用：**$S$ 中每个向量都能由 $S_0$ 线性表示**。两个说法等价，因为"加一个向量 $\boldsymbol{\beta}$ 后线性相关"与"$\boldsymbol{\beta}$ 能被 $S_0$ 表示"是同一件事（这是 019 篇的核心结论）。

### 2.3 容易误解的"极大"

"极大"不是"个数最多"，而是"**已经无法再容纳新成员**"。就像"坐满的车厢"不等于"全站最大的车厢"。

由此得到三个立刻可用的性质：

1. **不唯一**：$\{\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_3\}$ 是上面例子的极大无关组，$\{\boldsymbol{\alpha}_2, \boldsymbol{\alpha}_4\}$ 也可以（$\boldsymbol{\alpha}_2 = 2\boldsymbol{\alpha}_1$ 与 $\boldsymbol{\alpha}_4 = \boldsymbol{\alpha}_1 - \boldsymbol{\alpha}_3$ 显然无关，且能表示其余向量）。
2. **个数唯一**：所有极大无关组含同样多的向量。这是后面"秩""维数"定义合法的根基。
3. **等价**：任意两个极大无关组可以互相线性表示（等价向量组）。

### 2.4 求法：化阶梯形，看主元列

标准流程（这也是 010 篇求秩的同一套操作）：

1. 把向量**按列**排成矩阵 $A$；
2. 对 $A$ 只做**初等行变换**，化为行阶梯形；
3. **主元所在的列**对应的**原矩阵中的列向量**，构成一个极大线性无关组。

为什么行变换不破坏列之间的关系？因为初等行变换只是对方程组做等价变形，列向量之间的线性表示关系保持不变（行变换相当于左乘可逆矩阵 $P$，而 $P(\alpha_1,\ldots,\alpha_s)$ 的列之间成立的关系与原来完全一致）。这一点在 009、010 篇有严格说明，这里先记住操作即可。

> 注意：选出来的是**原向量**，不是行阶梯形里的向量。行阶梯形只是用来"找位置"的。

## 3. 向量组的秩：骨架的"大小"

### 3.1 定义

向量组 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ 的**秩**定义为它的极大线性无关组所含向量的个数，记作 $r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s)$。

因为"个数唯一"，这个定义不会产生歧义。秩回答的问题是：**这组向量撑开的空间有几维？**

### 3.2 矩阵的秩与向量组的秩，其实是同一个数

关键定理：矩阵 $A$ 的秩 = $A$ 的**行向量组**的秩 = $A$ 的**列向量组**的秩。

这个结论并不显然：行和列明明是两种不同的排法，为什么"有效个数"一样？直观解释是：行阶梯形中非零行数既等于行秩，也等于主元列数即列秩（010 篇有详细论证）。工程上你不需要在乎按行还是按列，算一次阶梯形全部搞定。

### 3.3 四条常用性质（复习时直接背）

设两个向量组的秩分别为 $r_1, r_2$：

1. $r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s) \leq \min(s, n)$，其中 $n$ 是向量的维数；
2. $r = s \iff$ 向量组线性无关；
3. 若向量组 (I) 能由 (II) 线性表示，则 $r(\text{I}) \leq r(\text{II})$（表示别人的组至少不比别人"小"）；
4. 等价向量组秩相等（性质 3 两边各用一次）。

### 3.4 秩与线性表示：一个高频判定

设 $\boldsymbol{\beta}$ 能由 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ 线性表示，则：

$$r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s, \boldsymbol{\beta}) = r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s)$$

反过来也成立：**把 $\boldsymbol{\beta}$ 并进向量组后秩不变 $\iff$ $\boldsymbol{\beta}$ 能被原组表示**。

直觉：$\boldsymbol{\beta}$ 是"已有信息的组合"，并进来不产生新维度，所以秩不变；若 $\boldsymbol{\beta}$ 带来新方向，秩就变大。

## 4. 概念图：从向量组到维数

<svg viewBox="0 0 880 210" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" role="img" aria-label="从向量组到维数的概念递进图">
  <defs>
    <marker id="arrow-a" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#888"/></marker>
  </defs>
  <rect x="10" y="55" width="170" height="100" rx="10" fill="#eef3fb" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="95" y="85" text-anchor="middle" font-size="15" font-weight="bold" fill="#2c3e50">向量组</text>
  <text x="95" y="107" text-anchor="middle" font-size="13" fill="#333">含冗余，个数任意</text>
  <text x="95" y="127" text-anchor="middle" font-size="13" fill="#333">例：4 个向量</text>
  <text x="95" y="146" text-anchor="middle" font-size="13" fill="#666">秩 = 极大无关组个数</text>
  <line x1="180" y1="105" x2="235" y2="105" stroke="#888" stroke-width="2" marker-end="url(#arrow-a)"/>
  <rect x="240" y="55" width="185" height="100" rx="10" fill="#eaf7ee" stroke="#3d8b5b" stroke-width="1.5"/>
  <text x="332" y="85" text-anchor="middle" font-size="15" font-weight="bold" fill="#2c3e50">极大线性无关组</text>
  <text x="332" y="107" text-anchor="middle" font-size="13" fill="#333">自身无关 + 能表示全部</text>
  <text x="332" y="127" text-anchor="middle" font-size="13" fill="#333">不唯一，个数唯一</text>
  <text x="332" y="146" text-anchor="middle" font-size="13" fill="#666">例：{α₁, α₃}</text>
  <line x1="425" y1="105" x2="480" y2="105" stroke="#888" stroke-width="2" marker-end="url(#arrow-a)"/>
  <rect x="485" y="55" width="175" height="100" rx="10" fill="#fdf3e7" stroke="#b0702a" stroke-width="1.5"/>
  <text x="572" y="85" text-anchor="middle" font-size="15" font-weight="bold" fill="#2c3e50">基</text>
  <text x="572" y="107" text-anchor="middle" font-size="13" fill="#333">向量空间的骨架</text>
  <text x="572" y="127" text-anchor="middle" font-size="13" fill="#333">无关 + 张成整个空间</text>
  <text x="572" y="146" text-anchor="middle" font-size="13" fill="#666">同一空间基含相同个数</text>
  <line x1="660" y1="105" x2="715" y2="105" stroke="#888" stroke-width="2" marker-end="url(#arrow-a)"/>
  <rect x="720" y="55" width="150" height="100" rx="10" fill="#f6eefb" stroke="#7b4fa6" stroke-width="1.5"/>
  <text x="795" y="85" text-anchor="middle" font-size="15" font-weight="bold" fill="#2c3e50">维数</text>
  <text x="795" y="107" text-anchor="middle" font-size="13" fill="#333">基中向量的个数</text>
  <text x="795" y="127" text-anchor="middle" font-size="13" fill="#333">例：dim = 2</text>
  <text x="795" y="146" text-anchor="middle" font-size="13" fill="#666">最小信息量的度量</text>
  <text x="440" y="30" text-anchor="middle" font-size="14" fill="#555">去冗余：取极大无关组</text>
  <text x="440" y="192" text-anchor="middle" font-size="13" fill="#555">关键一步：向量按列排成矩阵，化行阶梯形，主元列即骨架</text>
</svg>

**读图方法**：从左到右是"抽离"的过程——先去掉冗余（极大无关组），再把它放到整个空间里看（基），最后数个数（维数）。从右往左是"还原"的过程——知道基和维数，就知道整个空间长什么样。

## 5. 向量空间与子空间：先分清"房子"和"房间"

### 5.1 向量空间的严格定义

一个非空集合 $V$，如果定义了**加法**和**数乘**两种运算，并且满足下面八条规则，就称为**向量空间（线性空间）**（数域这里取实数 $\mathbb{R}$）：

| 类别 | 规则 |
| --- | --- |
| 加法 | 交换律 $\boldsymbol{\alpha}+\boldsymbol{\beta}=\boldsymbol{\beta}+\boldsymbol{\alpha}$；结合律 $(\boldsymbol{\alpha}+\boldsymbol{\beta})+\boldsymbol{\gamma}=\boldsymbol{\alpha}+(\boldsymbol{\beta}+\boldsymbol{\gamma})$ |
| 加法 | 存在零向量 $\boldsymbol{0}$ 使 $\boldsymbol{\alpha}+\boldsymbol{0}=\boldsymbol{\alpha}$；每个 $\boldsymbol{\alpha}$ 有负向量 $-\boldsymbol{\alpha}$ |
| 数乘 | $1\cdot\boldsymbol{\alpha}=\boldsymbol{\alpha}$；$(kl)\boldsymbol{\alpha}=k(l\boldsymbol{\alpha})$ |
| 混合 | $(k+l)\boldsymbol{\alpha}=k\boldsymbol{\alpha}+l\boldsymbol{\alpha}$；$k(\boldsymbol{\alpha}+\boldsymbol{\beta})=k\boldsymbol{\alpha}+k\boldsymbol{\beta}$ |

八条公理看起来繁琐，但 $\mathbb{R}^n$ 的普通向量加法和数乘天然满足它们。**零基础读者第一遍只需要记住两条**：向量空间里可以自由地做"加法"和"按比例缩放"，而且结果不离开这个空间。

### 5.2 子空间：封闭性就够了

实际题目里遇到的往往是"大空间里的一个小集合"，比如 $\mathbb{R}^3$ 中过原点的平面。判定它是不是子空间，**不需要验证八条公理**，只需要验证三条：

设 $W$ 是向量空间 $V$ 的非空子集，若：

1. $\boldsymbol{0} \in W$（或至少 $W$ 非空）；
2. **加法封闭**：$\boldsymbol{\alpha}, \boldsymbol{\beta} \in W \Rightarrow \boldsymbol{\alpha}+\boldsymbol{\beta} \in W$；
3. **数乘封闭**：$\boldsymbol{\alpha} \in W,\ k \in \mathbb{R} \Rightarrow k\boldsymbol{\alpha} \in W$。

则 $W$ 是 $V$ 的**子空间**。

为什么三条就够？因为加法交换律、结合律等公理是"继承"自大空间 $V$ 的，只要小集合对运算封闭，结果不会跑出去，其余公理自动成立。

> 常见教材差异提醒：同济《线性代数》把 $\mathbb{R}^n$ 的子空间直接称为"向量空间"（第 4 章 §2），到第 6 章才引入一般线性空间的八条公理。做题时"向量空间""子空间""线性空间"指的是同一套封闭性思想，不要被叫法绕晕。

**最容易错的判定**：过原点的直线/平面是子空间；**不过原点的直线/平面不是子空间**（因为不包含 $\boldsymbol{0}$，数乘也封闭不了）。

### 5.3 常见向量空间速查表

| 空间 | 一组基 | 维数 |
| --- | --- | --- |
| $\mathbb{R}^n$ | 标准基 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_n$ | $n$ |
| $Ax=0$ 的解空间（零空间 $N(A)$） | 基础解系 | $n - r(A)$ |
| 列空间 $\mathrm{Col}(A)$ | $A$ 的列向量组的极大无关组 | $r(A)$ |
| 行空间 $\mathrm{Row}(A)$ | 行向量组的极大无关组 | $r(A)$ |
| $\{ \boldsymbol{0} \}$ | 空集（没有基） | $0$ |
| 次数不超过 $n$ 的多项式空间 $P_n$ | $1, x, x^2, \ldots, x^n$ | $n+1$ |
| 所有 $m \times n$ 矩阵构成的空间 | 每个位置一个"单元素矩阵" | $mn$ |

最后两行说明：**向量空间里的"向量"可以是多项式、矩阵，不一定是箭头**。这是第 6 章"线性空间与线性变换"的伏笔，也是后续 024 篇《向量空间典型例题》的素材。

## 6. 基与维数：空间的"骨架"和"刻度"

### 6.1 定义

设 $V$ 是向量空间，$V$ 中的向量组 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_r$ 称为 $V$ 的一组**基**，如果：

1. $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_r$ 线性无关；
2. $V$ 中每个向量都能由它们线性表示（即 $\mathrm{span}(\boldsymbol{e}_1, \ldots, \boldsymbol{e}_r) = V$）。

$V$ 的**维数**定义为基中向量的个数，记作 $\dim V$。

把基和极大无关组对比：极大无关组是"**一个向量组内部**"的骨架；基是"**整个空间**"的骨架。生成子空间时两者合流：

$$\dim\big(\mathrm{span}(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s)\big) = r(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s)$$

即：**一组向量张成的空间的维数，恰好等于这组向量的秩**。开篇例子里 $\dim = 2$ 就是这么来的。

### 6.2 维数为什么是"良定义"的

凭什么保证任何基都含同样多的向量？这是线性代数的**交换定理（Steinitz Exchange Lemma）**的推论：

> 设 $V$ 是有限维向量空间，$\dim V = r$。则 $V$ 中任何线性无关组所含向量个数不超过 $r$；任何能生成 $V$ 的向量组所含向量个数不少于 $r$。

证明思路（零基础也能看懂版）：假设无关组 $L$ 比基 $B$ 多一个向量。因为 $B$ 能生成 $L$ 中的每个向量，$L$ 的某个向量可以"换掉" $B$ 中的一个向量而仍然生成全空间；不断替换，最后 $L$ 就"长"进了基的内部，与 $L$ 的无关性矛盾。严谨版见参考链接中的教材。

由交换定理立刻得到三个高频结论：

1. **$n$ 维空间中 $n$ 个线性无关的向量必为基**（个数已到上限，不可能再少）；
2. $n$ 维空间中 $n$ 个向量若线性相关，则必不能生成全空间；
3. 若 $\dim V = n$，则 $V$ 中任意 $n$ 个线性无关向量都能互相充当基，它们之间只差一个可逆的过渡矩阵。

### 6.3 生成子空间

由 $\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s$ 的所有线性组合构成的集合：

$$\mathrm{span}(\boldsymbol{\alpha}_1, \ldots, \boldsymbol{\alpha}_s) = \left\{ k_1\boldsymbol{\alpha}_1 + \cdots + k_s\boldsymbol{\alpha}_s \mid k_i \in \mathbb{R} \right\}$$

它一定是子空间（自己验证：加法、数乘封闭）。它的基就是这组向量的极大线性无关组。

## 7. 基变换与坐标变换：换一套"度量衡"

### 7.1 坐标：用基来"读数"

设 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_r$ 是 $V$ 的一组基。由基的定义，$V$ 中任何向量 $\boldsymbol{\alpha}$ 都能唯一地写成：

$$\boldsymbol{\alpha} = x_1\boldsymbol{e}_1 + x_2\boldsymbol{e}_2 + \cdots + x_r\boldsymbol{e}_r$$

$(x_1, x_2, \ldots, x_r)^T$ 称为 $\boldsymbol{\alpha}$ 在这组基下的**坐标**。

坐标的**唯一性**是基的线性无关性给的：如果两组坐标都能表示 $\boldsymbol{\alpha}$，相减得到 $\sum (x_i - y_i)\boldsymbol{e}_i = \boldsymbol{0}$，线性无关逼迫每个 $x_i = y_i$。所以"读数"不会产生歧义。

### 7.2 过渡矩阵：旧基与新基之间的"翻译器"

设 $\boldsymbol{e}_1, \ldots, \boldsymbol{e}_n$ 和 $\boldsymbol{f}_1, \ldots, \boldsymbol{f}_n$ 是 $V$ 的两组基。既然 $\boldsymbol{f}_j$ 也是 $V$ 中的向量，它就能用旧基表示：

$$\boldsymbol{f}_j = p_{1j}\boldsymbol{e}_1 + p_{2j}\boldsymbol{e}_2 + \cdots + p_{nj}\boldsymbol{e}_n$$

把系数按列排成矩阵：

$$\big(\boldsymbol{f}_1\ \boldsymbol{f}_2\ \cdots\ \boldsymbol{f}_n\big) = \big(\boldsymbol{e}_1\ \boldsymbol{e}_2\ \cdots\ \boldsymbol{e}_n\big)\, P$$

$P$ 称为由旧基 $\{\boldsymbol{e}_j\}$ 到新基 $\{\boldsymbol{f}_j\}$ 的**过渡矩阵**。两组基互相能表示，所以 $P$ 一定可逆。

**求法**：若两组基都是 $\mathbb{R}^n$ 中的具体向量，把基向量按列拼成矩阵 $E$ 和 $F$，则关系式就是 $F = E P$，解得：

$$P = E^{-1}F$$

### 7.3 坐标变换公式：方向是"反直觉"的

设 $\boldsymbol{\alpha}$ 在旧基下的坐标为 $\boldsymbol{x}$，在新基下的坐标为 $\boldsymbol{y}$，则：

$$\boxed{\ \boldsymbol{x} = P\boldsymbol{y}\ \quad \Longleftrightarrow \quad \boldsymbol{y} = P^{-1}\boldsymbol{x}\ }$$

**为什么方向是反的**：$P$ 的作用对象是"新基向量如何用旧基表示"，所以旧坐标 = $P$ 乘新坐标。想理解：$\boldsymbol{f}_j$ 用旧基表示时，$\boldsymbol{f}_j$ 自己的"旧坐标"就是 $P$ 的第 $j$ 列；而同一个向量 $\boldsymbol{\alpha}$ 在新基下第 $j$ 个坐标 $y_j$ 表示"取 $y_j$ 份 $\boldsymbol{f}_j$"，换算回旧基自然要乘 $P$。

**防错口诀**："$P$ 写在旧坐标那边"——旧坐标 $\boldsymbol{x} = P\,\boldsymbol{y}$，永远让 $P$ 靠近旧基。

### 7.4 完整示例

设 $\boldsymbol{e}_1 = (1,0)^T$、$\boldsymbol{e}_2 = (0,1)^T$ 为旧基；$\boldsymbol{f}_1 = (1,1)^T$、$\boldsymbol{f}_2 = (1,-1)^T$ 为新基。

**第 1 步，求过渡矩阵**（旧基是标准基，$E = I$，所以 $P = F$）：

$$P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

**第 2 步，求新坐标**。向量 $\boldsymbol{\alpha} = (3,1)^T$ 在旧基下坐标 $\boldsymbol{x} = (3,1)^T$，则：

$$\boldsymbol{y} = P^{-1}\boldsymbol{x} = \frac{1}{-2}\begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \frac{1}{-2}\begin{pmatrix} -4 \\ -2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$

**第 3 步，验证**：

$$2\boldsymbol{f}_1 + 1\cdot\boldsymbol{f}_2 = 2\begin{pmatrix} 1 \\ 1 \end{pmatrix} + \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix} = \boldsymbol{\alpha}$$

读数正确。若换成 $\{\boldsymbol{f}_j\}$ 到 $\{\boldsymbol{e}_j\}$ 的过渡矩阵，则是 $P^{-1}$——**换方向就换逆**，这是最容易翻车的地方。

## 8. 高频混淆点自查表

| 易混说法 | 正确理解 | 常见后果 |
| --- | --- | --- |
| "向量空间 = 子空间" | 向量空间是完整公理体系；子空间是其中对运算封闭的非空子集（多数题目语境下等价） | 判定时漏查 $\boldsymbol{0} \in W$ |
| "极大无关组 = 个数最多的无关组" | 极大指"加不进新成员"，不同极大无关组个数相同但未必最多 | 误以为只能选主元列那一种 |
| "基 = 极大无关组" | 基是"整个空间"的骨架；极大无关组是"某个向量组"的骨架 | 把零空间的基当成列向量的极大无关组 |
| "坐标变换公式是 $\boldsymbol{y} = P\boldsymbol{x}$" | 旧坐标 $\boldsymbol{x} = P\boldsymbol{y}$，$P$ 由旧基表示新基 | 答案方向反了 |
| "维数 = 向量个数" | 维数 = 基的个数，不是生成组里所有向量的个数 | 把 4 个向量生成的 2 维空间算成 4 维 |
| "不过原点的平面也是子空间" | 子空间必须含 $\boldsymbol{0}$，不过原点的仿射平面不是 | 线性性被破坏 |
| "$A$ 的列空间基 = $A$ 本身的所有列" | 列空间的基是列向量组的极大无关组 | 冗余列被重复计入 |

## 10. 一句话记忆

> 基是"最小生成骨架"：线性无关 + 张成全部；维数是骨架的长度；极大线性无关组是"一个向量组内部的基"；换基时旧坐标 $= P\,$新坐标，$P$ 是"新基用旧基说话"的翻译器。
