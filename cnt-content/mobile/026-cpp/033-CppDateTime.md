# C++ 日期时间库

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## duration 时长

**基本写法：定义时长**
`std::chrono::duration<<类型>, <比率>> <变量>(<值>);`
```cpp
// 表示 5 秒
std::chrono::duration<int> sec(5);
```

---

**基本写法：预定义时长类型**
`std::chrono::seconds` / `std::chrono::milliseconds`
```cpp
// 使用标准时长别名
std::chrono::seconds s(10);
std::chrono::milliseconds ms(100);
```

---

**基本写法：时长运算**
`<时长1> + <时长2>`
```cpp
// 时长相加
auto total = std::chrono::seconds(5) + std::chrono::milliseconds(500);
```

---

**基本写法：时长转换**
`std::chrono::duration_cast<<目标类型>>(<时长>);`
```cpp
// 秒转毫秒
auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(sec);
```

---

**基本写法：获取计数值**
`<时长>.count()`
```cpp
// 取出底层计数
long n = ms.count();
```

---

## time_point 时间点

**基本写法：获取当前时间**
`std::chrono::system_clock::now();`
```cpp
// 系统时钟当前时间点
auto now = std::chrono::system_clock::now();
```

---

**基本写法：稳态时钟**
`std::chrono::steady_clock::now();`
```cpp
// 单调递增时钟用于计时
auto start = std::chrono::steady_clock::now();
```

---

**基本写法：高精度时钟**
`std::chrono::high_resolution_clock::now();`
```cpp
// 最高精度时钟
auto t = std::chrono::high_resolution_clock::now();
```

---

**基本写法：计算时间差**
`<结束> - <开始>`
```cpp
// 两个时间点相减得到时长
auto diff = end - start;
```

---

**基本写法：时间点加时长**
`<时间点> + <时长>`
```cpp
// 时间点偏移
auto later = now + std::chrono::hours(1);
```

---

## time_t 转换

**基本写法：转 time_t**
`std::chrono::system_clock::to_time_t(<时间点>);`
```cpp
// 转为 C 风格 time_t
std::time_t t = std::chrono::system_clock::to_time_t(now);
```

---

**基本写法：从 time_t 转**
`std::chrono::system_clock::from_time_t(<t>);`
```cpp
// time_t 转回时间点
auto tp = std::chrono::system_clock::from_time_t(t);
```

---

**基本写法：格式化时间**
`std::ctime(&<t>);`
```cpp
// 转为可读字符串
std::string s = std::ctime(&t);
```

---

## year_month_day C++20

**基本写法：构造日期**
`std::chrono::year(<年>)/<月>/<日>`
```cpp
// C++20 日历日期
auto date = std::chrono::year(2026)/7/31;
```

---

**基本写法：获取年月日**
`<date>.year()` / `.month()` / `.day()`
```cpp
// 取出日期各部分
auto y = date.year();
auto m = date.month();
```

---

**基本写法：从时间点转日期**
`std::chrono::year_month_day{std::chrono::floor<std::chrono::days>(<tp>)};`
```cpp
// 时间点转日历日期
auto days = std::chrono::floor<std::chrono::days>(now);
auto ymd = std::chrono::year_month_day{days};
```

---

## 时钟相关

**基本写法：clock 字符串格式 C++23**
`std::format("{:%Y-%m-%d}", <时间点>);`
```cpp
// 格式化日历
auto s = std::format("{:%Y-%m-%d %H:%M:%S}", now);
```

---

**基本写法：休眠**
`std::this_thread::sleep_for(<时长>);`
```cpp
// 线程休眠指定时长
std::this_thread::sleep_for(std::chrono::seconds(2));
```

---

**基本写法：休眠到时间点**
`std::this_thread::sleep_until(<时间点>);`
```cpp
// 休眠到指定时间点
std::this_thread::sleep_until(now + std::chrono::hours(1));
```

---

## 计时器示例

**基本写法：测量耗时**
`auto <开始> = steady_clock::now(); <任务>; auto <耗时> = steady_clock::now() - <开始>;`
```cpp
// 测量代码执行耗时
auto start = std::chrono::steady_clock::now();
do_work();
auto elapsed = std::chrono::steady_clock::now() - start;
auto us = std::chrono::duration_cast<std::chrono::microseconds>(elapsed);
```

---

## C 风格 time

**基本写法：获取时间戳**
`std::time(nullptr);`
```cpp
// 当前时间戳秒数
std::time_t t = std::time(nullptr);
```

---

**基本写法：分解时间**
`std::localtime(&<t>);`
```cpp
// 转为本地时间结构
std::tm* tm = std::localtime(&t);
```

---

**基本写法：格式化分解时间**
`std::strftime(<缓冲>, <大小>, <格式>, <tm>);`
```cpp
// 自定义格式输出
char buf[64];
std::strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S", tm);
```
