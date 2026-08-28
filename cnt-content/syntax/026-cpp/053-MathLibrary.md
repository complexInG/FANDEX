# C++ 数学库

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## <cmath> 标准数学

**基本写法：常用数学函数**
`std::<函数>(<参数>)`
```cpp
#include <cmath>
// 基础函数
double y = std::sqrt(2.0);      // 平方根
double p = std::pow(2, 10);     // 2^10 = 1024
double e = std::exp(1.0);       // e^1
double l = std::log(10.0);      // 自然对数
double l2 = std::log2(8.0);     // log2(8) = 3
double l10 = std::log10(100.0); // log10(100) = 2
```

---

**基本写法：三角函数**
`std::sin / cos / tan`
```cpp
// 三角函数（弧度制）
double s = std::sin(3.14159 / 2); // 1.0
double c = std::cos(0);           // 1.0
double t = std::tan(0.785);       // tan(45°)
// 反三角
double as = std::asin(1.0);       // π/2
// 双曲
double h = std::sinh(1.0);
```

---

**基本写法：取整与绝对值**
`std::floor / ceil / round / abs`
```cpp
// 取整函数
double f = std::floor(3.7);   // 3.0 向下
double c = std::ceil(3.2);    // 4.0 向上
double r = std::round(3.5);   // 4.0 四舍五入
double tr = std::trunc(3.9);  // 3.0 截断
// 绝对值
int ai = std::abs(-5);        // 5
double ad = std::fabs(-3.14); // 3.14
```

---

**基本写法：特殊函数**
`std::erf / tgamma / lgamma`
```cpp
// 特殊数学函数
double e = std::erf(1.0);         // 误差函数
double g = std::tgamma(5.0);      // Γ(5) = 24
double lg = std::lgamma(5.0);     // ln(Γ(5))
double b = std::beta(2.0, 3.0);   // 贝塔函数（C++17）
```

---

## <numeric> 数值算法

**基本写法：累加**
`std::accumulate(<起始>, <结束>, <初值>)`
```cpp
#include <numeric>
std::vector<int> v = {1, 2, 3, 4, 5};
int sum = std::accumulate(v.begin(), v.end(), 0); // 15
// 自定义操作（累积乘积）
int prod = std::accumulate(v.begin(), v.end(), 1, std::multiplies<>{}); // 120
```

---

**基本写法：部分和**
`std::partial_sum(<起始>, <结束>, <输出>)`
```cpp
// 前缀和
std::vector<int> v = {1, 2, 3, 4};
std::vector<int> result(4);
std::partial_sum(v.begin(), v.end(), result.begin());
// result = {1, 3, 6, 10}
```

---

**基本写法：相邻差**
`std::adjacent_difference(<起始>, <结束>, <输出>)`
```cpp
// 相邻元素差
std::vector<int> v = {1, 3, 6, 10};
std::vector<int> result(4);
std::adjacent_difference(v.begin(), v.end(), result.begin());
// result = {1, 2, 3, 4}
```

---

**基本写法：内积**
`std::inner_product(<起始1>, <结束1>, <起始2>, <初值>)`
```cpp
// 向量内积
std::vector<int> a = {1, 2, 3};
std::vector<int> b = {4, 5, 6};
int dot = std::inner_product(a.begin(), a.end(), b.begin(), 0); // 1*4+2*5+3*6 = 32
```

---

**基本写法：GCD/LCM（C++17）**
`std::gcd(<a>, <b>)` `std::lcm(<a>, <b>)`
```cpp
#include <numeric>
int g = std::gcd(12, 18); // 6
int l = std::lcm(4, 6);    // 12
```

---

## <random> 随机数

**基本写法：随机数引擎**
`std::mt19937 <引擎>(<种子>);`
```cpp
#include <random>
// Mersenne Twister 引擎
std::random_device rd;
std::mt19937 gen(rd()); // 用硬件随机种子
// 或固定种子
std::mt19937 gen(42);
```

---

**基本写法：分布**
`std::uniform_int_distribution<<类型>> <分布>(<min>, <max>)`
```cpp
// 均匀分布
std::uniform_int_distribution<int> dist(1, 100);
int r = dist(gen); // 1-100 随机整数
std::uniform_real_distribution<double> rdist(0.0, 1.0);
double d = rdist(gen); // [0,1) 随机浮点
```

---

**基本写法：正态分布**
`std::normal_distribution<<类型>> <分布>(<均值>, <方差>)`
```cpp
// 正态分布
std::normal_distribution<double> ndist(0.0, 1.0); // 均值 0，标准差 1
double v = ndist(gen);
```

---

## <complex> 复数

**基本写法：复数**
`std::complex<<类型>> <变量>(<实部>, <虚部>)`
```cpp
#include <complex>
std::complex<double> c(3.0, 4.0); // 3 + 4i
double real = c.real();   // 3.0
double imag = c.imag();   // 4.0
double mag = std::abs(c); // 5.0 模长
double arg = std::arg(c); // 幅角
auto conj = std::conj(c); // 共轭复数
```

---

## 数学常量（C++20）

**基本写法：数学常量**
`std::numbers::<常量>`
```cpp
#include <numbers>
double pi = std::numbers::pi;          // 3.14159...
double e = std::numbers::e;            // 2.71828...
double sqrt2 = std::numbers::sqrt2;    // 1.41421...
double ln2 = std::numbers::ln2;        // 0.69314...
double phi = std::numbers::phi;        // 黄金比例
```
