---
order: 93
title: 微分中值定理典型例题
module: calculus
category: 'comp-sci'
difficulty: intermediate
description: 微分中值定理15道典型例题：罗尔定理、拉格朗日中值定理、柯西中值定理、泰勒公式等核心题型。
author: fanquanpp
updated: '2026-08-01'
related:
  - calculus/函数与极限典型例题
  - calculus/导数与微分典型例题
  - calculus/不定积分典型例题
  - calculus/定积分与应用典型例题
prerequisites:
  - calculus/函数与极限
---

## 1. 罗尔定理应用

**例1**：证明方程 $x^3 - 3x + 1 = 0$ 在 $(0,1)$ 内有且仅有一个实根。

**证明**：

**存在性**：$f(0) = 1 > 0$，$f(1) = -1 < 0$，由零点定理，$\exists \xi \in (0,1)$ 使 $f(\xi) = 0$。

**唯一性**：若有两个根 $\xi_1 < \xi_2$，则 $f(\xi_1) = f(\xi_2) = 0$，由罗尔定理 $\exists c \in (\xi_1, \xi_2)$ 使 $f'(c) = 0$。但 $f'(x) = 3x^2 - 3 = 3(x^2-1)$，在 $(0,1)$ 内 $f'(x) < 0$，矛盾。

---

**例2**：设 $f(x)$ 在 $[0,1]$ 连续、$(0,1)$ 可导，且 $f(0) = f(1) = 0$，$f\left(\frac{1}{2}\right) = 1$。证明：$\exists \xi \in (0,1)$ 使 $f'(\xi) = 1$。

**证明**：令 $g(x) = f(x) - x$，则 $g(0) = 0$，$g(1) = -1$，$g\left(\frac{1}{2}\right) = \frac{1}{2}$。

由 $g\left(\frac{1}{2}\right) = \frac{1}{2} > 0$ 和 $g(1) = -1 < 0$，由零点定理 $\exists c \in \left(\frac{1}{2}, 1\right)$ 使 $g(c) = 0$。

又 $g(0) = 0$，由罗尔定理 $\exists \xi \in (0, c)$ 使 $g'(\xi) = 0$，即 $f'(\xi) - 1 = 0$，$f'(\xi) = 1$。

## 2. 拉格朗日中值定理

**例3**：证明：当 $x > 0$ 时，$\frac{x}{1+x} < \ln(1+x) < x$。

**证明**：设 $f(t) = \ln(1+t)$，在 $[0, x]$ 上用拉格朗日中值定理：

$$\frac{\ln(1+x) - \ln 1}{x - 0} = \frac{1}{1+\xi}, \quad \xi \in (0, x)$$

因为 $0 < \xi < x$，所以 $\frac{1}{1+x} < \frac{1}{1+\xi} < 1$，即：

$$\frac{1}{1+x} < \frac{\ln(1+x)}{x} < 1$$

$$\frac{x}{1+x} < \ln(1+x) < x$$

---

**例4**：设 $f(x)$ 在 $[a,b]$ 连续、$(a,b)$ 可导，证明：$\exists \xi \in (a,b)$ 使 $f(b) - f(a) = \xi f'(\xi) \ln\frac{b}{a}$。

**证明**：令 $g(x) = \ln x$，对 $f(x)$ 和 $g(x)$ 用柯西中值定理：

$$\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(\xi)}{g'(\xi)} = \frac{f'(\xi)}{1/\xi} = \xi f'(\xi)$$

$$f(b) - f(a) = \xi f'(\xi) \cdot (\ln b - \ln a) = \xi f'(\xi) \ln\frac{b}{a}$$

## 3. 柯西中值定理

**例5**：设 $f(x)$ 在 $[a,b]$ 连续、$(a,b)$ 可导（$a > 0$），证明：$\exists \xi \in (a,b)$ 使 $2\xi[f(b)-f(a)] = (b^2-a^2)f'(\xi)$。

**证明**：令 $g(x) = x^2$，对 $f(x)$ 和 $g(x)$ 用柯西中值定理：

$$\frac{f(b)-f(a)}{b^2-a^2} = \frac{f'(\xi)}{2\xi}$$

$$2\xi[f(b)-f(a)] = (b^2-a^2)f'(\xi)$$

---

**例6**：设 $f(x)$ 在 $[0,+\infty)$ 可导，$f(0) = 0$，且 $0 \leq f'(x) \leq \frac{1}{2}$，证明：$\lim_{x \to +\infty} \frac{f(x)}{x^2} = 0$。

**证明**：由拉格朗日中值定理，$f(x) = f(x) - f(0) = f'(\xi) \cdot x$，其中 $\xi \in (0, x)$。

$$0 \leq f(x) \leq \frac{1}{2}x$$

$$0 \leq \frac{f(x)}{x^2} \leq \frac{1}{2x}$$

由夹逼准则，$\lim_{x \to +\infty} \frac{f(x)}{x^2} = 0$。

## 4. 泰勒公式应用

**例7**：求 $\lim_{x \to 0} \frac{e^x - 1 - x - \frac{x^2}{2}}{x^3}$。

**解**：$e^x$ 的三阶麦克劳林展开：

$$e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + o(x^3)$$

$$\lim_{x \to 0} \frac{\frac{x^3}{6} + o(x^3)}{x^3} = \frac{1}{6}$$

---

**例8**：设 $f(x)$ 在 $x=0$ 的某邻域内二阶可导，$\lim_{x \to 0} \frac{f(x) - x}{x^2} = 1$，求 $f(0)$，$f'(0)$，$f''(0)$。

**解**：泰勒展开 $f(x) = f(0) + f'(0)x + \frac{f''(0)}{2}x^2 + o(x^2)$

$$\frac{f(x)-x}{x^2} = \frac{f(0) + (f'(0)-1)x + \frac{f''(0)}{2}x^2 + o(x^2)}{x^2}$$

极限为 1，要求：

- $f(0) = 0$
- $f'(0) - 1 = 0 \Rightarrow f'(0) = 1$
- $\frac{f''(0)}{2} = 1 \Rightarrow f''(0) = 2$

## 5. 证明题综合

**例9**：设 $f(x)$ 在 $[0,1]$ 二阶可导，$f(0) = f(1) = 0$，$\min_{[0,1]} f(x) = -1$。证明：$\exists \xi \in (0,1)$ 使 $f''(\xi) \geq 8$。

**证明**：设 $f(x)$ 在 $x = c \in (0,1)$ 取最小值 $-1$，则 $f'(c) = 0$。

在 $[0, c]$ 上用泰勒公式（在 $c$ 处展开）：

$$f(0) = f(c) + f'(c)(0-c) + \frac{f''(\xi_1)}{2}(0-c)^2$$

$$0 = -1 + 0 + \frac{f''(\xi_1)}{2}c^2 \Rightarrow f''(\xi_1) = \frac{2}{c^2}$$

在 $[c, 1]$ 上同理：

$$0 = -1 + \frac{f''(\xi_2)}{2}(1-c)^2 \Rightarrow f''(\xi_2) = \frac{2}{(1-c)^2}$$

取 $\xi = \xi_1$ 或 $\xi_2$：

若 $c \leq \frac{1}{2}$，则 $f''(\xi_1) = \frac{2}{c^2} \geq \frac{2}{(1/2)^2} = 8$

若 $c > \frac{1}{2}$，则 $f''(\xi_2) = \frac{2}{(1-c)^2} \geq \frac{2}{(1/2)^2} = 8$

---

**例10**：设 $f(x)$ 在 $[a,b]$ 连续、$(a,b)$ 可导，$f(a) = f(b) = 0$，证明：$\exists \xi \in (a,b)$ 使 $f(\xi) + f'(\xi) = 0$。

**证明**：令 $F(x) = e^x f(x)$，则 $F(a) = F(b) = 0$。

$F(x)$ 在 $[a,b]$ 满足罗尔定理条件，故 $\exists \xi \in (a,b)$ 使 $F'(\xi) = 0$：

$$e^\xi f(\xi) + e^\xi f'(\xi) = 0 \Rightarrow f(\xi) + f'(\xi) = 0$$

---

**例11**：设 $f(x)$ 在 $[0,1]$ 连续、$(0,1)$ 可导，$f(0) = 0$，$f(1) = 1$。证明：$\exists \xi_1, \xi_2 \in (0,1)$ 使 $\frac{1}{f'(\xi_1)} + \frac{1}{f'(\xi_2)} = 2$。

**证明**：由介值定理，$\exists c \in (0,1)$ 使 $f(c) = \frac{1}{2}$。

在 $[0, c]$ 上用拉格朗日中值定理：$f'(\xi_1) = \frac{f(c)-f(0)}{c-0} = \frac{1}{2c}$

在 $[c, 1]$ 上用拉格朗日中值定理：$f'(\xi_2) = \frac{f(1)-f(c)}{1-c} = \frac{1}{2(1-c)}$

$$\frac{1}{f'(\xi_1)} + \frac{1}{f'(\xi_2)} = 2c + 2(1-c) = 2$$

## 6. 函数单调性与极值

**例12**：求 $f(x) = x^3 - 3x^2 + 4$ 的单调区间和极值。

**解**：$f'(x) = 3x^2 - 6x = 3x(x-2)$

| 区间    | $(-\infty, 0)$ | $(0, 2)$ | $(2, +\infty)$ |
| ------- | -------------- | -------- | -------------- |
| $f'(x)$ | $+$            | $-$      | $+$            |
| $f(x)$  | 递增           | 递减     | 递增           |

$x = 0$：极大值 $f(0) = 4$

$x = 2$：极小值 $f(2) = 0$

---

**例13**：证明：$x > 0$ 时 $e^x > 1 + x + \frac{x^2}{2}$。

**证明**：令 $f(x) = e^x - 1 - x - \frac{x^2}{2}$

$f(0) = 0$，$f'(x) = e^x - 1 - x$，$f'(0) = 0$

$f''(x) = e^x - 1$，当 $x > 0$ 时 $f''(x) > 0$

所以 $f'(x)$ 在 $x > 0$ 递增，$f'(x) > f'(0) = 0$

所以 $f(x)$ 在 $x > 0$ 递增，$f(x) > f(0) = 0$，即 $e^x > 1 + x + \frac{x^2}{2}$。

## 7. 凹凸性与拐点

**例14**：求 $f(x) = x^4 - 4x^3 + 6x^2 - 4x + 1$ 的凹凸区间和拐点。

**解**：$f'(x) = 4x^3 - 12x^2 + 12x - 4 = 4(x-1)^3$

$f''(x) = 12(x-1)^2$

$f''(x) \geq 0$ 对所有 $x$ 成立，且仅在 $x=1$ 处 $f''(x) = 0$。

但 $f''(x)$ 在 $x=1$ 两侧不变号，故 $x=1$ 不是拐点。

$f(x)$ 在 $(-\infty, +\infty)$ 上都是凹的，无拐点。

---

**例15**：设 $f(x)$ 在 $[a,b]$ 上二阶可导，$f'(a) = f'(b) = 0$，证明：$\exists \xi \in (a,b)$ 使 $|f''(\xi)| \geq \frac{4}{(b-a)^2}|f(b)-f(a)|$。

**证明**：设 $c = \frac{a+b}{2}$，在 $[a, c]$ 上对 $f(x)$ 在 $x=a$ 处泰勒展开：

$$f(c) = f(a) + f'(a)(c-a) + \frac{f''(\xi_1)}{2}(c-a)^2 = f(a) + \frac{f''(\xi_1)}{2}\left(\frac{b-a}{2}\right)^2$$

同理在 $[c, b]$ 上：

$$f(c) = f(b) + \frac{f''(\xi_2)}{2}\left(\frac{b-a}{2}\right)^2$$

两式相减：

$$f(b) - f(a) = \frac{(b-a)^2}{8}[f''(\xi_1) - f''(\xi_2)]$$

$$|f(b)-f(a)| \leq \frac{(b-a)^2}{8}[|f''(\xi_1)| + |f''(\xi_2)|] \leq \frac{(b-a)^2}{8} \cdot 2\max\{|f''(\xi_1)|, |f''(\xi_2)|\}$$

取 $\xi$ 为 $\xi_1$ 或 $\xi_2$ 中 $|f''|$ 较大者，即得 $|f''(\xi)| \geq \frac{4}{(b-a)^2}|f(b)-f(a)|$。

## 参考文献

Khan Academy 微积分：https://zh.khanacademy.org/math/calculus-1
3Blue1Brown 微积分的本质：https://www.3blue1brown.com/topics/calculus
MIT 18.01：https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/
Desmos：https://www.desmos.com/

## 延伸阅读

微积分基础，见 027-calculus 模块文档。
线性代数（梯度与向量），见 029-linear-algebra 模块。
概率统计（积分应用），见 030-probability-statistics 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供数学课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 极限与连续性严格化

ε-δ 定义：对任意 ε 存在 δ；用于证明连续性。
夹逼定理、单调有界收敛、洛必达法则（0/0 与 ∞/∞）。
连续函数性质：介值定理、极值定理。
理解严格化帮助甄别直觉误区（如瞬时速度）。

### 13.2 微积分基本定理

第一形式：变上限积分求导回到被积函数。
第二形式：定积分 = 原函数差。
推论：面积、累积量、期望的积分表达。
应用：FTC 是数值积分与微分方程求解的理论基础。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 函数与极限 | 001-FunctionAndLimit | 本文的并列主题 |
| 导数与微分 | 002-PhilosophiaeNaturalisPrincipiaMathematica | 本文的并列主题 |
| 微分中值定理 | 003-AMeanValueTheorem | 本文的并列主题 |
| 不定积分 | 004-IndefiniteIntegral | 本文的并列主题 |
| 定积分与应用 | 005-DefiniteIntegralAndApplication | 本文的并列主题 |
| 多元函数微分 | 006-MultivariateFunctionDifferential | 本文的并列主题 |
| 重积分 | 007-MultipleIntegral | 本文的并列主题 |
| 曲线积分与曲面积分 | 008-CurveAndSurfaceIntegral | 本文的并列主题 |
| 公式速查表 | 009-FormulaQuickReference | 本文的并列主题 |
| 无穷级数与常微分方程 | 010-InfiniteSeriesAndODE | 本文的并列主题 |
| 函数与极限典型例题 | 011-FunctionAndLimitExamples | 本文的并列主题 |
| 导数与微分典型例题 | 012-DerivativeAndDifferentialExamples | 本文的并列主题 |
| 微分中值定理典型例题 | 013-DifferentialMeanValueTheoremExamples | 本文自身 |
| 不定积分典型例题 | 014-IndefiniteIntegralExamples | 本文的并列主题 |
| 定积分与应用典型例题 | 015-DefiniteIntegralApplicationExamples | 本文的并列主题 |
| 多元函数微分典型例题 | 016-MultivariateFunctionDifferentialExamples | 本文的并列主题 |
| 重积分典型例题 | 017-MultipleIntegralExamples | 本文的并列主题 |
| 曲线积分与曲面积分典型例题 | 018-CurveAndSurfaceIntegralExamples | 本文的并列主题 |
| 无穷级数与常微分方程典型例题 | 019-InfiniteSeriesAndODEExamples | 本文的并列主题 |
