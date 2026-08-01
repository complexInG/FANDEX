---
order: 1
title: 命题逻辑
module: 'discrete-math'
category: 离散数学
difficulty: beginner
description: 命题与联结词、真值表、等值演算、范式（主析取/主合取）、推理理论、自然推理系统。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'discrete-math/谓词逻辑'
  - 'discrete-math/集合与关系'
prerequisites: []
---
## 0. 零基础入门（从零开始）

### 0.1 零基础起点

本模块讲解离散数学（逻辑、集合、图论），零基础可学，不需要编程经验。它研究的是“可数的、分立的”数学对象，是计算机科学最直接的数学基础。
先理解为什么要学：程序里的 if 条件就是逻辑学中的“命题与蕴含”，数据库的表就是集合与关系，地图导航就是图论——离散数学是把生活直觉变成严谨推理的工具。

### 0.2 第一个逻辑概念：命题与真值表

```text
命题：可以判断真假的陈述句。
  P = "今天下雨"
  Q = "我带伞"

蕴含：如果 P 则 Q（记作 P -> Q）

真值表（列出所有可能情况）：
  P     Q     P->Q
  真    真     真
  真    假     假
  假    真     真
  假    假     真
```

命题必须是“可判断真假”的陈述句："今天下雨"是命题，"你好吗"不是。
蕴含（P -> Q）表示“如果 P 成立，那么 Q 也成立”。唯一为假的情况是“P 真但 Q 假”——即承诺被打破。
当 P 为假时，P -> Q 恒为真：这就是逻辑学中著名的“假前提蕴含一切”，初学者最容易困惑，务必对照真值表理解。
把真值表翻译成程序就是 if (P) then Q：程序判断 P 是否为真，再决定是否执行 Q。
掌握命题与真值表后，后续的集合、关系、图论都建立在同样的“定义 + 表格穷举”方法上。

### 0.3 学习路径

完成上面的第一步后，按以下顺序继续学习：

- 002-集合论：子集、并集、交集与集合运算。
- 003-关系：等价关系、偏序与函数。
- 004-图论：图、路径、树与连通性。

## 1. 命题与联结词

### 1.1 命题

**命题**是可以判断真假的陈述句。真值唯一确定，非真即假。

- **原子命题**：不能再分解的命题，用 $p, q, r, \ldots$ 表示
- **复合命题**：由原子命题通过联结词组合而成

### 1.2 逻辑联结词

| 联结词 | 符号                  | 名称 | 读法               |
| ------ | --------------------- | ---- | ------------------ |
| 否定   | $\neg p$              | 否定 | "非 $p$"           |
| 合取   | $p \land q$           | 合取 | "$p$ 与 $q$"       |
| 析取   | $p \lor q$            | 析取 | "$p$ 或 $q$"       |
| 蕴含   | $p \to q$             | 蕴含 | "若 $p$ 则 $q$"    |
| 等价   | $p \leftrightarrow q$ | 等价 | "$p$ 当且仅当 $q$" |

### 1.3 真值表

| $p$ | $q$ | $\neg p$ | $p \land q$ | $p \lor q$ | $p \to q$ | $p \leftrightarrow q$ |
| --- | --- | -------- | ----------- | ---------- | --------- | --------------------- |
| T   | T   | F        | T           | T          | T         | T                     |
| T   | F   | F        | F           | T          | F         | F                     |
| F   | T   | T        | F           | T          | T         | F                     |
| F   | F   | T        | F           | F          | T         | T                     |

**蕴含的理解**：$p \to q$ 仅在 $p$ 为真而 $q$ 为假时为假。$p$ 为假时 $p \to q$ 恒为真（空虚真）。

### 1.4 联结词的优先级

$$\neg > \land > \lor > \to > \leftrightarrow$$

## 2. 真值表与命题公式

### 2.1 命题公式

由命题变元、联结词和括号按规则组成的符号串。

**合式公式（wff）的递归定义**：

1. 命题变元是合式公式
2. 若 $A$ 是合式公式，则 $\neg A$ 是合式公式
3. 若 $A$, $B$ 是合式公式，则 $(A \land B)$, $(A \lor B)$, $(A \to B)$, $(A \leftrightarrow B)$ 是合式公式
4. 有限次使用 1-3 得到的是合式公式

### 2.2 真值函数

$n$ 个命题变元可构成 $2^{2^n}$ 个不同的真值函数。

- 1 个变元：4 个真值函数
- 2 个变元：16 个真值函数

### 2.3 公式分类

- **永真式（重言式）**：所有赋值下均为真，如 $p \lor \neg p$
- **永假式（矛盾式）**：所有赋值下均为假，如 $p \land \neg p$
- **可满足式**：存在赋值使其为真

## 3. 等值演算

### 3.1 等值定义

若 $A \leftrightarrow B$ 为重言式，则称 $A$ 与 $B$ **等值**，记作 $A \Leftrightarrow B$ 或 $A = B$。

### 3.2 基本等值式

**双重否定律**：$\neg\neg p \Leftrightarrow p$

**幂等律**：$p \land p \Leftrightarrow p$，$p \lor p \Leftrightarrow p$

**交换律**：$p \land q \Leftrightarrow q \land p$，$p \lor q \Leftrightarrow q \lor p$

**结合律**：$(p \land q) \land r \Leftrightarrow p \land (q \land r)$，$(p \lor q) \lor r \Leftrightarrow p \lor (q \lor r)$

**分配律**：

- $p \land (q \lor r) \Leftrightarrow (p \land q) \lor (p \land r)$
- $p \lor (q \land r) \Leftrightarrow (p \lor q) \land (p \lor r)$

**德摩根律**：

- $\neg(p \land q) \Leftrightarrow \neg p \lor \neg q$
- $\neg(p \lor q) \Leftrightarrow \neg p \land \neg q$

**吸收律**：$p \land (p \lor q) \Leftrightarrow p$，$p \lor (p \land q) \Leftrightarrow p$

**蕴含等值式**：$p \to q \Leftrightarrow \neg p \lor q$

**逆否律**：$p \to q \Leftrightarrow \neg q \to \neg p$

**假言易位**：$p \to q \Leftrightarrow \neg q \to \neg p$

**等价等值式**：$p \leftrightarrow q \Leftrightarrow (p \to q) \land (q \to p)$

**归谬律**：$(p \to q) \land (p \to \neg q) \Leftrightarrow \neg p$

**例**：证明 $p \to (q \to r) \Leftrightarrow (p \land q) \to r$。

> $p \to (q \to r) \Leftrightarrow \neg p \lor (\neg q \lor r) \Leftrightarrow (\neg p \lor \neg q) \lor r \Leftrightarrow \neg(p \land q) \lor r \Leftrightarrow (p \land q) \to r$

## 4. 范式

### 4.1 析取范式与合取范式

**析取范式（DNF）**：形如 $A_1 \lor A_2 \lor \cdots \lor A_n$，其中每个 $A_i$ 为合取式（文字的合取）。

**合取范式（CNF）**：形如 $A_1 \land A_2 \land \cdots \land A_n$，其中每个 $A_i$ 为析取式（文字的析取）。

**文字**：命题变元或其否定，如 $p$，$\neg q$。

### 4.2 主析取范式

**极小项**：$n$ 个变元的合取式，每个变元以肯定或否定形式出现且仅出现一次。

$n$ 个变元有 $2^n$ 个极小项，第 $i$ 个极小项 $m_i$ 对应使公式为真的第 $i$ 组赋值。

**主析取范式**：极小项的析取。每个公式的主析取范式唯一。

**求法**：

1. 消去 $\to$ 和 $\leftrightarrow$
2. 用德摩根律将 $\neg$ 内移
3. 用分配律化为析取范式
4. 补齐缺失变元，合并相同极小项

**例**：求 $p \to q$ 的主析取范式。

> $p \to q \Leftrightarrow \neg p \lor q \Leftrightarrow (\neg p \land (q \lor \neg q)) \lor ((p \lor \neg p) \land q)$
> $\Leftrightarrow (\neg p \land q) \lor (\neg p \land \neg q) \lor (p \land q)$
> $\Leftrightarrow m_0 \lor m_1 \lor m_3$

### 4.3 主合取范式

**极大项**：$n$ 个变元的析取式，每个变元以肯定或否定形式出现且仅出现一次。

**主合取范式**：极大项的合取。每个公式的主合取范式唯一。

**关系**：主析取范式中的极小项编号与主合取范式中的极大项编号互补。

**例**：若主析取范式为 $m_1 \lor m_3$，则主合取范式为 $M_0 \land M_2$。

## 5. 推理理论

### 5.1 有效推理

若前提 $A_1, A_2, \ldots, A_n$ 为真时结论 $B$ 必为真，即 $(A_1 \land A_2 \land \cdots \land A_n) \to B$ 为重言式，则称推理**有效**，记作 $A_1, A_2, \ldots, A_n \vdash B$。

### 5.2 推理规则

**假言推理（MP）**：$p \to q$，$p \vdash q$

**假言三段论**：$p \to q$，$q \to r \vdash p \to r$

**析取三段论**：$p \lor q$，$\neg p \vdash q$

**附加律**：$p \vdash p \lor q$

**化简律**：$p \land q \vdash p$

**合取律**：$p$，$q \vdash p \land q$

**拒取式**：$p \to q$，$\neg q \vdash \neg p$

**构造性二难**：$p \to q$，$r \to s$，$p \lor r \vdash q \lor s$

### 5.3 证明方法

**直接证明法**：从前提出发，逐步推出结论。

**反证法（归谬法）**：将结论否定加入前提，推出矛盾。

**例**：前提：$p \to q$，$q \to r$，$p$。结论：$r$。

> 1. $p \to q$（前提）
> 2. $p$（前提）
> 3. $q$（MP，1, 2）
> 4. $q \to r$（前提）
> 5. $r$（MP，3, 4）

**例**：前提：$p \to q$，$\neg q$。结论：$\neg p$。

> 反证法：假设 $\neg\neg p$（即 $p$）。
>
> 1. $p$（假设）
> 2. $p \to q$（前提）
> 3. $q$（MP，1, 2）
> 4. $\neg q$（前提）
> 5. $q \land \neg q$（矛盾！）
>    故 $\neg p$ 成立。

## 6. 自然推理系统

### 6.1 系统组成

自然推理系统由推理规则组成，无需公理。常用系统 $\mathbf{F}$：

**引入规则**：

- $\land$I（合取引入）：从 $A$, $B$ 推出 $A \land B$
- $\lor$I（析取引入）：从 $A$ 推出 $A \lor B$
- $\to$I（蕴含引入）：假设 $A$ 推出 $B$，则 $A \to B$
- $\neg$I（否定引入）：假设 $A$ 推出矛盾，则 $\neg A$

**消去规则**：

- $\land$E（合取消去）：从 $A \land B$ 推出 $A$ 或 $B$
- $\lor$E（析取消去）：从 $A \lor B$，$A \to C$，$B \to C$ 推出 $C$
- $\to$E（蕴含消去）：即 MP，从 $A \to B$ 和 $A$ 推出 $B$
- $\neg$E（否定消去）：从 $A$ 和 $\neg A$ 推出矛盾

### 6.2 证明示例

**证明**：$p \to q, p \lor r, \neg r \vdash q$

> 1. $p \lor r$（前提）
> 2. $\neg r$（前提）
> 3. $p$（析取三段论，1, 2）
> 4. $p \to q$（前提）
> 5. $q$（MP，3, 4）

### 6.3 消解原理

**消解规则**：从 $A \lor C$ 和 $\neg A \lor B$ 推出 $C \lor B$。

**消解证明**：

1. 将前提和结论的否定化为合取范式
2. 反复应用消解规则
3. 若推出空子句 $\square$，则原推理有效

**例**：前提 $p \to q$，$p$，结论 $q$。

> $p \to q$ 化为 $\neg p \lor q$，$\neg q$（结论的否定）。
> 消解 $\neg p \lor q$ 与 $\neg q$：得 $\neg p$。
> 消解 $\neg p$ 与 $p$：得 $\square$（空子句）。证毕。

## 参考文献

MIT 6.042J：https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/
Khan Academy 离散数学：https://www.khanacademy.org/computing/computer-science
Discrete Mathematics and Its Applications（Rosen）：https://www.mheducation.com/

## 延伸阅读

离散数学基础，见 028-discrete-math 模块文档。
算法与图论，见 023-algorithm 模块。
逻辑与数据库关系，见 019-sql 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供离散数学课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 数学归纳法

基础情形 -> 归纳假设 -> 归纳步骤；变体：强归纳、结构归纳。
典型证明：求和公式、树性质、算法正确性。
循环不变量：归纳法在程序中的对应。
常见错误：假设过强/基础遗漏。

### 13.2 图论基础定理

握手引理：所有顶点度数之和为边数两倍。
树的等价定义：连通无环、n-1 条边、任意两点唯一路径。
欧拉回路条件：连通且所有顶点度数为偶。
四色定理与平面图（了解层面）。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 命题逻辑 | 001-PropositionalLogic | 本文自身 |
| 谓词逻辑 | 002-PredicateLogic | 本文的并列主题 |
| 集合与关系 | 003-SetAndRelation | 本文的并列主题 |
| 函数与基数 | 004-FunctionAndNumber | 本文的并列主题 |
| 图论基础 | 005-GraphTheoryBasics | 本文的前置基础 |
| 图论进阶 | 006-GraphTheoryAdvanced | 本文的并列主题 |
| 代数系统 | 007-AlgebraicSystem | 本文的并列主题 |
| 组合数学 | 008-Combinatorics | 本文的并列主题 |
