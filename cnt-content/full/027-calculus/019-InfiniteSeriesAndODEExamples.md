---
order: 99
title: 无穷级数与常微分方程典型例题
module: calculus
category: 'comp-sci'
difficulty: intermediate
description: 无穷级数与常微分方程15道典型例题：级数审敛、幂级数展开、傅里叶级数、微分方程求解等核心题型。
author: fanquanpp
updated: '2026-08-01'
related:
  - calculus/重积分典型例题
  - calculus/曲线积分与曲面积分典型例题
prerequisites:
  - calculus/函数与极限
---

## 1. 常数项级数审敛

**例1**：判断 $\sum_{n=1}^{\infty} \frac{n}{2^n}$ 的收敛性。

**解**：比值审敛法：

$$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = \lim_{n \to \infty} \frac{n+1}{2^{n+1}} \cdot \frac{2^n}{n} = \lim_{n \to \infty} \frac{n+1}{2n} = \frac{1}{2} < 1$$

级数收敛。

---

**例2**：判断 $\sum_{n=1}^{\infty} \frac{1}{n\sqrt[n]{n}}$ 的收敛性。

**解**：$\sqrt[n]{n} \to 1$（$n \to \infty$），故 $\frac{1}{n\sqrt[n]{n}} \sim \frac{1}{n}$

与调和级数比较：$\lim_{n \to \infty} \frac{1/(n\sqrt[n]{n})}{1/n} = \lim_{n \to \infty} \frac{1}{\sqrt[n]{n}} = 1$

调和级数发散，故原级数发散。

---

**例3**：判断 $\sum_{n=1}^{\infty} (-1)^n \frac{\ln n}{n}$ 的收敛性（条件收敛还是绝对收敛）。

**解**：

**绝对值级数**：$\sum \frac{\ln n}{n}$，因 $\frac{\ln n}{n} > \frac{1}{n}$（$n \geq 3$），发散。

**原级数**：莱布尼茨审敛法。

- $a_n = \frac{\ln n}{n}$，令 $f(x) = \frac{\ln x}{x}$，$f'(x) = \frac{1-\ln x}{x^2} < 0$（$x > e$），故 $a_n$ 递减（$n \geq 3$）
- $\lim_{n \to \infty} \frac{\ln n}{n} = 0$

由莱布尼茨审敛法，级数收敛。但非绝对收敛，故**条件收敛**。

## 2. 幂级数

**例4**：求 $\sum_{n=1}^{\infty} \frac{x^n}{n \cdot 3^n}$ 的收敛域。

**解**：

$$R = \lim_{n \to \infty} \frac{a_n}{a_{n+1}} = \lim_{n \to \infty} \frac{(n+1) \cdot 3^{n+1}}{n \cdot 3^n} = 3$$

端点 $x = 3$：$\sum \frac{1}{n}$ 发散

端点 $x = -3$：$\sum \frac{(-1)^n}{n}$ 收敛（莱布尼茨）

收敛域 $[-3, 3)$

---

**例5**：求 $\sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}$ 的和函数。

**解**：

$$\sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!} = x + \frac{x^3}{3!} + \frac{x^5}{5!} + \cdots = \sinh x = \frac{e^x - e^{-x}}{2}$$

---

**例6**：求 $\sum_{n=1}^{\infty} nx^n$ 的和函数（$|x| < 1$）。

**解**：设 $S(x) = \sum_{n=1}^{\infty} nx^n = x\sum_{n=1}^{\infty} nx^{n-1}$

已知 $\sum_{n=0}^{\infty} x^n = \frac{1}{1-x}$，两边求导：

$$\sum_{n=1}^{\infty} nx^{n-1} = \frac{1}{(1-x)^2}$$

$$S(x) = \frac{x}{(1-x)^2}$$

## 3. 函数展开为幂级数

**例7**：将 $f(x) = \frac{1}{x^2-3x+2}$ 展开为 $x$ 的幂级数。

**解**：

$$f(x) = \frac{1}{(x-1)(x-2)} = \frac{1}{x-2} - \frac{1}{x-1} = \frac{1}{1-x} - \frac{1}{2}\cdot\frac{1}{1-\frac{x}{2}}$$

$$= \sum_{n=0}^{\infty} x^n - \frac{1}{2}\sum_{n=0}^{\infty}\frac{x^n}{2^n} = \sum_{n=0}^{\infty}\left(1-\frac{1}{2^{n+1}}\right)x^n$$

收敛域 $|x| < 1$

---

**例8**：将 $f(x) = \arctan x$ 展开为麦克劳林级数。

**解**：$f'(x) = \frac{1}{1+x^2} = \sum_{n=0}^{\infty} (-1)^n x^{2n}$（$|x| < 1$）

$$\arctan x = \int_0^x \frac{dt}{1+t^2} = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{2n+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots$$

## 4. 傅里叶级数

**例9**：将 $f(x) = x$（$-\pi < x < \pi$）展开为傅里叶级数。

**解**：$f(x)$ 为奇函数，$a_n = 0$

$$b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\sin nx\, dx = \frac{2}{\pi}\int_0^{\pi} x\sin nx\, dx = \frac{2}{\pi}\left[-\frac{x\cos nx}{n} + \frac{\sin nx}{n^2}\right]_0^{\pi}$$

$$= \frac{2}{\pi} \cdot \frac{(-1)^{n+1}\pi}{n} = \frac{2(-1)^{n+1}}{n}$$

$$x = 2\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}\sin nx = 2\left(\sin x - \frac{\sin 2x}{2} + \frac{\sin 3x}{3} - \cdots\right)$$

---

**例10**：利用傅里叶级数求 $\sum_{n=1}^{\infty} \frac{1}{n^2}$ 的值。

**解**：将 $f(x) = x^2$（$-\pi \leq x \leq \pi$）展开：

$$x^2 = \frac{\pi^2}{3} + 4\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2}\cos nx$$

令 $x = \pi$：

$$\pi^2 = \frac{\pi^2}{3} + 4\sum_{n=1}^{\infty} \frac{1}{n^2}$$

$$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$$

## 5. 一阶微分方程

**例11**：求 $y' - \frac{2}{x+1}y = (x+1)^3$ 的通解。

**解**：一阶线性方程，$P(x) = -\frac{2}{x+1}$，$Q(x) = (x+1)^3$

$$y = e^{\int \frac{2}{x+1}dx}\left[\int (x+1)^3 e^{-\int\frac{2}{x+1}dx}dx + C\right]$$

$$= (x+1)^2\left[\int (x+1)^3 \cdot \frac{1}{(x+1)^2}dx + C\right] = (x+1)^2\left[\frac{(x+1)^2}{2} + C\right]$$

$$= \frac{(x+1)^4}{2} + C(x+1)^2$$

---

**例12**：求 $y' = \frac{y}{x} + \tan\frac{y}{x}$ 的通解。

**解**：齐次方程，令 $u = \frac{y}{x}$，$y = xu$，$y' = u + xu'$

$$u + xu' = u + \tan u \Rightarrow xu' = \tan u$$

$$\int \frac{du}{\tan u} = \int \frac{dx}{x} \Rightarrow \ln|\sin u| = \ln|x| + C_1$$

$$\sin\frac{y}{x} = Cx$$

## 6. 二阶常系数线性方程

**例13**：求 $y'' - 4y' + 3y = 0$ 的通解。

**解**：特征方程 $r^2 - 4r + 3 = 0$，$r_1 = 1$，$r_2 = 3$

$$y = C_1 e^x + C_2 e^{3x}$$

---

**例14**：求 $y'' + 4y' + 4y = e^{-2x}$ 的通解。

**解**：特征方程 $r^2 + 4r + 4 = 0$，$r = -2$（二重根）

齐次通解：$Y = (C_1 + C_2 x)e^{-2x}$

特解：设 $y^* = Ax^2 e^{-2x}$

$y^{*'} = (2Ax - 2Ax^2)e^{-2x}$，$y^{*''} = (2A - 8Ax + 4Ax^2)e^{-2x}$

代入方程：$2Ae^{-2x} = e^{-2x}$，$A = \frac{1}{2}$

$$y = (C_1 + C_2 x)e^{-2x} + \frac{x^2}{2}e^{-2x}$$

## 综合题知识点讲解

**例15**：设 $f(x)$ 具有二阶连续导数，$f(0) = 0$，$f'(0) = 1$，且

$$[x^2y + f(xy)]dx + [f(xy) + y^2]dy = 0$$

为全微分方程，求 $f(x)$ 及其通解。

**解**：全微分条件 $\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$：

$$x^2 + f'(xy) \cdot x = f'(xy) \cdot y + 0$$

$$x^2 + xf'(xy) = yf'(xy)$$

令 $t = xy$，则 $x^2 = (y-x)f'(t)$，这要求 $f'(t)$ 与 $t = xy$ 有关而与 $x, y$ 分离，只有 $x = y$ 时成立。

重新分析：$\frac{\partial P}{\partial y} = x^2 + xf'(xy)$，$\frac{\partial Q}{\partial x} = yf'(xy)$

$$x^2 + xf'(xy) = yf'(xy) \Rightarrow x^2 = (y-x)f'(xy)$$

令 $u = xy$，取 $y = 1$：$x^2 = (1-x)f'(x)$

$f'(x) = \frac{x^2}{1-x} = -x - 1 + \frac{1}{1-x}$

$f(x) = -\frac{x^2}{2} - x - \ln|1-x| + C$

由 $f(0) = 0$：$C = 0$

$f'(0) = 0 \neq 1$，矛盾。需重新审视。

修正：取 $x = 1$：$1 = (y-1)f'(y)$，$f'(y) = \frac{1}{y-1}$

$f(y) = \ln|y-1| + C$，$f(0) = \ln 1 + C = 0$，$C = 0$

$f'(0) = -1 \neq 1$，仍有矛盾。此题条件需调整，但核心方法为：利用全微分条件建立微分方程，再求解。

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
