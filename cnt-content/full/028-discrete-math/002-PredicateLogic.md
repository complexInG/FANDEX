---
order: 20
title: 谓词逻辑
module: 'discrete-math'
category: 数学
difficulty: intermediate
description: 量词、谓词公式、等值演算、前束范式、推理理论、一阶逻辑形式化。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'discrete-math/001-PropositionalLogic'
  - 'discrete-math/003-SetAndRelation'
  - 'discrete-math/004-FunctionAndNumber'
prerequisites:
  - 'discrete-math/001-PropositionalLogic'
---


## 1. 从"命题逻辑的局限"说起

### 1.1 一个说不清的问题

在命题逻辑中，我们只能处理"原子命题"——不能再分解的陈述句。比如：

- $p$：苏格拉底是人
- $q$：苏格拉底会死

如果我们知道"所有人都会死"，怎么表达"**所有**人都会死"？命题逻辑做不到——它没有"所有""存在"这种**量词**。

再看一个经典三段论：

- 大前提：所有人都会死
- 小前提：苏格拉底是人
- 结论：苏格拉底会死

用命题逻辑，我们只能把三句话当作三个独立命题，**无法体现"所有人"这个量词的结构**，也无法证明这个推理是有效的。

**谓词逻辑（Predicate Logic，一阶逻辑）就是命题逻辑的"升级版"**：它引入"谓词"（描述性质/关系）和"量词"（描述所有/存在），从而能够表达和证明更复杂的推理。

### 1.2 谓词逻辑能做什么

| 命题逻辑 | 谓词逻辑 |
| :--- | :--- |
| "苏格拉底会死" | "所有人都会死"（量化） |
| "x 是质数"（x 具体取值） | "对任意整数 x，x 是质数或合数" |
| 无法表达"所有/存在" | 用 $\forall$ / $\exists$ 表达 |

## 2. 谓词与量词

### 2.1 谓词

**谓词**表示个体的性质或个体间的关系：

- 一元谓词 $P(x)$：$x$ 具有性质 $P$（如"x 是质数"）
- 二元谓词 $P(x, y)$：$x$ 和 $y$ 具有关系 $P$（如"x 大于 y"）
- $n$ 元谓词 $P(x_1, x_2, \ldots, x_n)$

**论域（个体域）**：个体变元的取值范围。如"x 是质数"的论域是正整数集。

### 2.2 量词

| 量词 | 符号 | 含义 | 例子 |
| :--- | :--- | :--- | :--- |
| 全称量词 | $\forall$ | 对所有 | $\forall x\,P(x)$：所有 x 满足 P |
| 存在量词 | $\exists$ | 存在 | $\exists x\,P(x)$：存在 x 满足 P |

**生活理解**：

- "**所有**同学都通过了考试" → $\forall x\,P(x)$
- "**有的**同学通过了考试" → $\exists x\,P(x)$

### 2.3 量词与联结词的关系

在**有限论域** $D = \{a_1, a_2, \ldots, a_n\}$ 上：

$$\forall x\,P(x) \Leftrightarrow P(a_1) \land P(a_2) \land \cdots \land P(a_n)$$

$$\exists x\,P(x) \Leftrightarrow P(a_1) \lor P(a_2) \lor \cdots \lor P(a_n)$$

**直觉**："所有"就像"逐个都满足"（且），"存在"就像"至少一个满足"（或）。

### 2.4 量词的否定（重点）

$$\neg\forall x\,P(x) \Leftrightarrow \exists x\,\neg P(x)$$
$$\neg\exists x\,P(x) \Leftrightarrow \forall x\,\neg P(x)$$

**理解**：

- "不是所有同学都通过" = "存在同学没通过"
- "不存在外星人" = "所有东西都不是外星人"

**例**：$\neg\forall x(P(x) \to Q(x)) \Leftrightarrow \exists x\,(P(x) \land \neg Q(x))$（"不是所有人都…" = "存在一个人…但不…"）

## 3. 谓词公式

### 3.1 项与公式

**项**的递归定义：

1. 个体常量和个体变元是项
2. 若 $f$ 是 $n$ 元函数符号，$t_1, \ldots, t_n$ 是项，则 $f(t_1, \ldots, t_n)$ 是项

**原子公式**：$P(t_1, \ldots, t_n)$，其中 $P$ 是谓词符号，$t_i$ 是项。

**合式公式**：由原子公式通过联结词和量词递归构造。

### 3.2 自由变元与约束变元

- **约束变元**：出现在量词作用范围内的变元，如 $\forall x\,P(x)$ 中的 $x$
- **自由变元**：不受量词约束的变元，如 $P(x) \land \forall y\,Q(y)$ 中的 $x$

**闭公式**：不含自由变元的公式（真值确定，可判断真假）。

### 3.3 量词的辖域

$\forall x\,P(x) \land Q(x)$ 中 $\forall x$ 的辖域仅为 $P(x)$，$Q(x)$ 中的 $x$ 是**自由**的——这是最容易混淆的点！

### 3.4 约束变元换名

可将约束变元换名为不出现在公式中的其他变元：

$$\forall x\,P(x, y) \Leftrightarrow \forall z\,P(z, y)$$

（换名时不能与自由变元冲突）

## 4. 等值演算

### 4.1 量词德摩根律

$$\neg\forall x\,A \Leftrightarrow \exists x\,\neg A, \quad \neg\exists x\,A \Leftrightarrow \forall x\,\neg A$$

### 4.2 量词分配律

$$\forall x(A \land B) \Leftrightarrow \forall x\,A \land \forall x\,B$$
$$\exists x(A \lor B) \Leftrightarrow \exists x\,A \lor \exists x\,B$$

**注意（易错）**：

$$\forall x(A \lor B) \not\Leftrightarrow \forall x\,A \lor \forall x\,B$$
$$\exists x(A \land B) \not\Leftrightarrow \exists x\,A \land \exists x\,B$$

**理解**："所有同学是男生或女生" ≠ "所有同学是男生 或 所有同学是女生"（显然错误）。

### 4.3 量词与蕴含（带条件）

当 $x$ 不在 $B$ 中自由出现时：

$$\forall x\,A \to B \Leftrightarrow \exists x(A \to B)$$
$$\exists x\,A \to B \Leftrightarrow \forall x(A \to B)$$

（直观理解：条件式中的"全称变存在、存在变全称"）

### 4.4 量词的顺序（重要）

**同种量词可交换**：

$$\forall x\,\forall y\,P(x,y) \Leftrightarrow \forall y\,\forall x\,P(x,y)$$
$$\exists x\,\exists y\,P(x,y) \Leftrightarrow \exists y\,\exists x\,P(x,y)$$

**不同量词不可交换**：

$$\forall x\,\exists y\,P(x,y) \not\Leftrightarrow \exists y\,\forall x\,P(x,y)$$

**经典例子**：

- $\forall x\,\exists y\,(x + y = 0)$：**真**——对每个 $x$，都能找到 $y = -x$ 使 $x+y=0$
- $\exists y\,\forall x\,(x + y = 0)$：**假**——不存在一个固定的 $y$ 对**所有** $x$ 都满足

**直觉**："每个人都有人爱"（真）≠ "有一个人被所有人爱"（可能假）。

## 5. 前束范式

### 5.1 定义

**前束范式**：所有量词都在公式最前面的等值形式，形如

$$Q_1 x_1\,Q_2 x_2 \cdots Q_n x_n\,B$$

其中 $Q_i \in \{\forall, \exists\}$，$B$ 为不含量词的公式（**母式**）。

### 5.2 求前束范式的步骤

1. 消去 $\to$ 和 $\leftrightarrow$
2. 将 $\neg$ 内移至原子公式前
3. 约束变元换名（使不同量词使用不同变元名）
4. 将量词前移

**例**：求 $\neg\forall x\,P(x) \to \exists x\,Q(x)$ 的前束范式。

> 1. $\neg\forall x\,P(x) \to \exists x\,Q(x) \Leftrightarrow \forall x\,P(x) \lor \exists x\,Q(x)$
> 2. 换名：$\forall x\,P(x) \lor \exists y\,Q(y)$
> 3. 量词前移：$\forall x\exists y\,(P(x) \lor Q(y))$

### 5.3 Skolem 范式（消去存在量词）

将前束范式中的存在量词用 **Skolem 函数**消去：

- $\exists x$ 前面有 $\forall y_1, \ldots, \forall y_k$：用 $f(y_1, \ldots, y_k)$ 替换 $x$
- $\exists x$ 前面无全称量词：用常量 $c$ 替换 $x$

**例**：$\forall x\exists y\,P(x,y)$ 的 Skolem 化：用 $f(x)$ 替换 $y$，得 $\forall x\,P(x, f(x))$。

（Skolem 化是"消解原理"和自动定理证明的基础）

## 6. 推理理论

### 6.1 四条推理规则

| 规则 | 形式 | 直觉 |
| :--- | :--- | :--- |
| 全称量词消去（UI） | $\forall x\,A(x) \vdash A(c)$ | 所有满足 → 任意一个满足 |
| 全称量词引入（UG） | $A(c)$（$c$ 任意）$\vdash \forall x\,A(x)$ | 任意的都满足 → 所有满足 |
| 存在量词消去（EI） | $\exists x\,A(x) \vdash A(c)$（$c$ 特定） | 存在满足 → 给它起个名 |
| 存在量词引入（EG） | $A(c) \vdash \exists x\,A(x)$ | 有一个满足 → 存在满足 |

### 6.2 推理注意事项（易错）

- **EI 必须在 UI 之前使用**
- EI 引入的常量不能在其他前提中出现
- UG 要求变元是任意的

**例**：前提 $\forall x(P(x) \to Q(x))$，$\exists x\,P(x)$。结论 $\exists x\,Q(x)$。

> 1. $\exists x\,P(x)$（前提）
> 2. $P(a)$（EI，1）
> 3. $\forall x(P(x) \to Q(x))$（前提）
> 4. $P(a) \to Q(a)$（UI，3）
> 5. $Q(a)$（MP，2, 4）
> 6. $\exists x\,Q(x)$（EG，5）

## 7. 一阶逻辑形式化：把自然语言翻译成公式

### 7.1 形式化三步

1. 确定论域（个体范围）
2. 定义谓词（性质/关系）
3. 将自然语言翻译为谓词公式

**例**："所有实数都大于或等于某个整数"。

> 论域：实数集 $\mathbb{R}$
> 谓词：$G(x,y)$ 表示 $x \geq y$，$Z(x)$ 表示 $x$ 是整数
> $$\forall x\,\exists y\,(Z(y) \land G(x,y))$$

### 7.2 常见形式化模式（重点）

| 自然语言 | 形式化 |
| :--- | :--- |
| 所有 $A$ 都是 $B$ | $\forall x(A(x) \to B(x))$ |
| 有些 $A$ 是 $B$ | $\exists x(A(x) \land B(x))$ |
| 没有 $A$ 是 $B$ | $\forall x(A(x) \to \neg B(x))$ |
| 并非所有 $A$ 都是 $B$ | $\exists x(A(x) \land \neg B(x))$ |

**易错点**："所有 $A$ 都是 $B$" 必须形式化为 $\forall x(A(x) \to B(x))$，**不能**写成 $\forall x(A(x) \land B(x))$——后者要求"论域中所有元素既是 A 又是 B"，含义完全不同。

**记忆技巧**：

- "所有 A 是 B"：A → B（A 推出 B，只约束 A 的元素）
- "有些 A 是 B"：A ∧ B（存在一个既是 A 又是 B 的）

### 7.3 嵌套量词的理解

$$\forall x\,\exists y\,L(x,y)$$："每个人都爱某个人"（对每个人，都存在一个被他爱的人）

$$\exists y\,\forall x\,L(x,y)$$："有一个人被所有人爱"（存在一个人，所有人都爱他）

**两者的逻辑强度不同**：后者比前者强（后者蕴含前者，反之不成立）。

## 8. 常见误区

**误区一："所有 A 是 B" 用 $\land$ 连接。** → 必须用 $\to$。$\forall x(A(x) \land B(x))$ 会要求论域里全是 A。

**误区二：量词顺序可以随便换。** → $\forall\exists$ 和 $\exists\forall$ 含义完全不同（"每个人有人爱" vs "有个人被所有人爱"）。

**误区三：EI 在 UI 之后用。** → 顺序必须反过来：先 EI 再 UI，否则引入的常量可能是"假的特定个体"。

**误区四：$\forall x(A \lor B)$ 可以拆开。** → 全称对"或"、存在对"且"都不能拆分（见 4.2 节）。
