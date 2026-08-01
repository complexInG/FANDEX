---
order: 92
title: 导数与微分典型例题
module: calculus
category: 'comp-sci'
difficulty: intermediate
description: 导数与微分15道典型例题：求导法则、隐函数求导、参数方程求导、高阶导数等核心题型。
author: fanquanpp
updated: '2026-08-01'
related:
  - calculus/无穷级数与常微分方程
  - calculus/函数与极限典型例题
  - calculus/微分中值定理典型例题
  - calculus/不定积分典型例题
prerequisites:
  - calculus/函数与极限
---

## 1. 复合函数求导

**例1**：求 $y = \ln(\sin\sqrt{x})$ 的导数。

**解**：由链式法则：

$$y' = \frac{1}{\sin\sqrt{x}} \cdot \cos\sqrt{x} \cdot \frac{1}{2\sqrt{x}} = \frac{\cot\sqrt{x}}{2\sqrt{x}}$$

---

**例2**：求 $y = e^{\arctan\frac{1}{x}}$ 的导数。

**解**：

$$y' = e^{\arctan\frac{1}{x}} \cdot \frac{1}{1+\frac{1}{x^2}} \cdot \left(-\frac{1}{x^2}\right) = e^{\arctan\frac{1}{x}} \cdot \frac{x^2}{1+x^2} \cdot \left(-\frac{1}{x^2}\right) = -\frac{e^{\arctan\frac{1}{x}}}{1+x^2}$$

## 2. 隐函数求导

**例3**：设 $x^2 + y^2 = 25$，求 $\frac{dy}{dx}$ 和 $\frac{d^2y}{dx^2}$。

**解**：两边对 $x$ 求导：

$$2x + 2y\frac{dy}{dx} = 0 \Rightarrow \frac{dy}{dx} = -\frac{x}{y}$$

再求二阶导：

$$\frac{d^2y}{dx^2} = -\frac{y - x\frac{dy}{dx}}{y^2} = -\frac{y - x \cdot (-\frac{x}{y})}{y^2} = -\frac{y^2 + x^2}{y^3} = -\frac{25}{y^3}$$

---

**例4**：设 $y = 1 + x e^y$，求 $y'$ 和 $y''$。

**解**：两边对 $x$ 求导：

$$y' = e^y + x e^y y' \Rightarrow y'(1 - xe^y) = e^y \Rightarrow y' = \frac{e^y}{1-xe^y} = \frac{e^y}{2-y}$$

（因为 $xe^y = y - 1$）

$$y'' = \frac{e^y y'(2-y) - e^y(-y')}{(2-y)^2} = \frac{e^y y'(2-y+1)}{(2-y)^2} = \frac{e^y y'(3-y)}{(2-y)^2}$$

代入 $y' = \frac{e^y}{2-y}$：

$$y'' = \frac{e^{2y}(3-y)}{(2-y)^3}$$

## 3. 参数方程求导

**例5**：设 $\begin{cases} x = t - \sin t \\ y = 1 - \cos t \end{cases}$，求 $\frac{d^2y}{dx^2}$。

**解**：

$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{\sin t}{1 - \cos t}$$

$$\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{\sin t}{1-\cos t}\right) \cdot \frac{1}{dx/dt} = \frac{\cos t(1-\cos t) - \sin t \cdot \sin t}{(1-\cos t)^2} \cdot \frac{1}{1-\cos t}$$

$$= \frac{\cos t - \cos^2 t - \sin^2 t}{(1-\cos t)^3} = \frac{\cos t - 1}{(1-\cos t)^3} = \frac{-1}{(1-\cos t)^2}$$

## 4. 对数求导法

**例6**：求 $y = x^{\sin x}$ 的导数。

**解**：取对数 $\ln y = \sin x \cdot \ln x$

$$\frac{y'}{y} = \cos x \cdot \ln x + \sin x \cdot \frac{1}{x}$$

$$y' = x^{\sin x}\left(\cos x \cdot \ln x + \frac{\sin x}{x}\right)$$

---

**例7**：求 $y = \sqrt[3]{\frac{(x-1)(x-2)}{(x-3)(x-4)}}$ 的导数。

**解**：取对数：

$$\ln|y| = \frac{1}{3}[\ln|x-1| + \ln|x-2| - \ln|x-3| - \ln|x-4|]$$

$$\frac{y'}{y} = \frac{1}{3}\left[\frac{1}{x-1} + \frac{1}{x-2} - \frac{1}{x-3} - \frac{1}{x-4}\right]$$

$$y' = \frac{y}{3}\left[\frac{1}{x-1} + \frac{1}{x-2} - \frac{1}{x-3} - \frac{1}{x-4}\right]$$

## 5. 高阶导数

**例8**：求 $y = \frac{1}{x^2 - 3x + 2}$ 的 $n$ 阶导数。

**解**：部分分式分解：

$$y = \frac{1}{(x-1)(x-2)} = \frac{1}{x-2} - \frac{1}{x-1}$$

$$y^{(n)} = \left(\frac{1}{x-2}\right)^{(n)} - \left(\frac{1}{x-1}\right)^{(n)} = \frac{(-1)^n n!}{(x-2)^{n+1}} - \frac{(-1)^n n!}{(x-1)^{n+1}}$$

$$= (-1)^n n!\left[\frac{1}{(x-2)^{n+1}} - \frac{1}{(x-1)^{n+1}}\right]$$

---

**例9**：求 $y = x^2 e^{2x}$ 的 $n$ 阶导数。

**解**：利用莱布尼茨公式，设 $u = x^2$，$v = e^{2x}$：

$$u' = 2x, \quad u'' = 2, \quad u^{(k)} = 0 \ (k \geq 3)$$

$$v^{(k)} = 2^k e^{2x}$$

$$y^{(n)} = \sum_{k=0}^{n}\binom{n}{k}u^{(n-k)}v^{(k)} = x^2 \cdot 2^n e^{2x} + n \cdot 2x \cdot 2^{n-1}e^{2x} + \frac{n(n-1)}{2} \cdot 2 \cdot 2^{n-2}e^{2x}$$

$$= 2^{n-2}e^{2x}\left[4x^2 + 4nx + n(n-1)\right]$$

## 6. 微分的计算与应用

**例10**：求 $y = \arctan\frac{1+x}{1-x}$ 的微分 $dy$。

**解**：

$$y' = \frac{1}{1+\left(\frac{1+x}{1-x}\right)^2} \cdot \frac{(1-x)+(1+x)}{(1-x)^2} = \frac{(1-x)^2}{(1-x)^2+(1+x)^2} \cdot \frac{2}{(1-x)^2}$$

$$= \frac{2}{(1-x)^2+(1+x)^2} = \frac{2}{2+2x^2} = \frac{1}{1+x^2}$$

$$dy = \frac{dx}{1+x^2}$$

---

**例11**：利用微分近似计算 $\sqrt[3]{8.02}$。

**解**：设 $f(x) = \sqrt[3]{x}$，$x_0 = 8$，$\Delta x = 0.02$

$$f(x_0 + \Delta x) \approx f(x_0) + f'(x_0)\Delta x$$

$$f'(x) = \frac{1}{3}x^{-2/3}, \quad f'(8) = \frac{1}{3} \cdot \frac{1}{4} = \frac{1}{12}$$

$$\sqrt[3]{8.02} \approx 2 + \frac{1}{12} \times 0.02 = 2 + \frac{0.02}{12} \approx 2.00167$$

## 综合题知识点讲解

**例12**：设 $f(x) = \begin{cases} x^2 & x \leq 1 \\ ax + b & x > 1 \end{cases}$，确定 $a, b$ 使 $f(x)$ 在 $x=1$ 处可导。

**解**：可导必连续，先求连续条件：

$$\lim_{x \to 1^-} f(x) = 1, \quad \lim_{x \to 1^+} f(x) = a + b$$

连续：$a + b = 1$

再求可导条件：

$$f'_-(1) = \lim_{x \to 1^-} \frac{x^2 - 1}{x-1} = 2$$

$$f'_+(1) = \lim_{x \to 1^+} \frac{ax+b-1}{x-1} = a$$

可导：$a = 2$，代入 $b = 1 - a = -1$。

---

**例13**：设 $f(x)$ 在 $x = a$ 处可导，求 $\lim_{h \to 0} \frac{f(a+ph) - f(a-qh)}{h}$（$p, q > 0$）。

**解**：

$$\frac{f(a+ph) - f(a-qh)}{h} = p \cdot \frac{f(a+ph) - f(a)}{ph} + q \cdot \frac{f(a) - f(a-qh)}{qh}$$

$$= p \cdot f'(a) + q \cdot f'(a) = (p+q)f'(a)$$

---

**例14**：设 $y = f(\ln x)$，其中 $f$ 二阶可导，求 $y''$。

**解**：

$$y' = f'(\ln x) \cdot \frac{1}{x}$$

$$y'' = f''(\ln x) \cdot \frac{1}{x^2} + f'(\ln x) \cdot \left(-\frac{1}{x^2}\right) = \frac{f''(\ln x) - f'(\ln x)}{x^2}$$

---

**例15**：证明：双曲线 $xy = c^2$ 上任一点处的切线与两坐标轴围成的三角形面积为常数。

**证明**：设切点为 $(x_0, y_0)$，其中 $x_0 y_0 = c^2$。

由 $y = \frac{c^2}{x}$，$y' = -\frac{c^2}{x^2}$，切线斜率 $k = -\frac{c^2}{x_0^2}$。

切线方程：$y - y_0 = -\frac{c^2}{x_0^2}(x - x_0)$

令 $y = 0$：$x$ 截距 $= x_0 + \frac{y_0 x_0^2}{c^2} = x_0 + \frac{c^2 \cdot x_0}{c^2} = 2x_0$

令 $x = 0$：$y$ 截距 $= y_0 + \frac{c^2}{x_0} = y_0 + y_0 = 2y_0$

面积 $= \frac{1}{2} \cdot 2x_0 \cdot 2y_0 = 2x_0 y_0 = 2c^2$（常数）。

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
