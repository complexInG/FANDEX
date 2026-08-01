---
order: 20
tags:
  - cpp
difficulty: beginner
title: 'C++ 基础语法'
module: cpp
category: 'C++ Basics'
description: 'C++ 基本语法、注释、标识符与关键字。'
author: Anonymous
related:
  - cpp/概述与现代标准
  - cpp/类型系统
  - cpp/引用
prerequisites: []
updated: '2026-08-01'
---

# 基础语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 数据类型 (Data Types)

C++ 具有丰富的类型系统，分为基本类型和复合类型。

### 1.1 基本数据类型

| 类型                 | 描述                   | 大小 (字节) | 示例                                             |
| :------------------- | :--------------------- | :---------- | :----------------------------------------------- |
| **整数类型**         |                        |             |                                                  |
| `char`               | 字符                   | 1           | `char c = 'A';`                                  |
| `unsigned char`      | 无符号字符             | 1           | `unsigned char uc = 255;`                        |
| `short`              | 短整数                 | 2           | `short s = 32767;`                               |
| `unsigned short`     | 无符号短整数           | 2           | `unsigned short us = 65535;`                     |
| `int`                | 整数                   | 4           | `int x = 10;`                                    |
| `unsigned int`       | 无符号整数             | 4           | `unsigned int ux = 4294967295;`                  |
| `long`               | 长整数                 | 4 或 8      | `long l = 1000000;`                              |
| `unsigned long`      | 无符号长整数           | 4 或 8      | `unsigned long ul = 1000000;`                    |
| `long long`          | 长长整数 (C++11)       | 8           | `long long ll = 10000000000;`                    |
| `unsigned long long` | 无符号长长整数 (C++11) | 8           | `unsigned long long ull = 18446744073709551615;` |
| **浮点类型**         |                        |             |                                                  |
| `float`              | 单精度浮点数           | 4           | `float f = 3.14f;`                               |
| `double`             | 双精度浮点数           | 8           | `double d = 3.1415926535;`                       |
| `long double`        | 长双精度浮点数         | 8 或 16     | `long double ld = 3.14159265358979323846;`       |
| **布尔类型**         |                        |             |                                                  |
| `bool`               | 布尔值                 | 1           | `bool is_valid = true;`                          |
| **空类型**           |                        |             |                                                  |
| `void`               | 无类型                 | -           | 用于函数返回或通用指针                           |

### 1.2 复合数据类型

| 类型       | 描述               | 示例                                            |
| :--------- | :----------------- | :---------------------------------------------- |
| **数组**   | 相同类型元素的集合 | `int arr[5] = {1, 2, 3, 4, 5};`                 |
| **字符串** | 字符序列           | `std::string s = "Hello C++";`                  |
| **指针**   | 存储内存地址       | `int* p = &x;`                                  |
| **引用**   | 变量的别名         | `int& ref = x;`                                 |
| **结构体** | 不同类型成员的集合 | `struct Person { std::string name; int age; };` |
| **联合体** | 共用内存的不同类型 | `union Data { int i; float f; char c; };`       |
| **枚举**   | 命名常量集合       | `enum Color { RED, GREEN, BLUE };`              |
| **类**     | 面向对象的类型     | `class MyClass { /* ... */ };`                  |

### 1.3 类型修饰符

| 修饰符      | 描述                 | 示例                                                                         |
| :---------- | :------------------- | :--------------------------------------------------------------------------- |
| `signed`    | 有符号类型 (默认)    | `signed int x = -10;`                                                        |
| `unsigned`  | 无符号类型           | `unsigned int y = 10;`                                                       |
| `short`     | 短类型               | `short s = 100;`                                                             |
| `long`      | 长类型               | `long l = 1000000;`                                                          |
| `const`     | 常量类型             | `const int MAX = 100;`                                                       |
| `volatile`  | 易变类型             | `volatile int flag = 0;`                                                     |
| `constexpr` | 编译期常量 (C++11)   | `constexpr int factorial(int n) { return n <= 1 ? 1 : n * factorial(n-1); }` |
| `auto`      | 自动类型推断 (C++11) | `auto i = 10;`                                                               |
| `decltype`  | 类型推导 (C++11)     | `decltype(i) j = 20;`                                                        |

### 1.4 类型转换

#### 1.4.1 隐式类型转换

```cpp
 int i = 10;
 double d = i; // 隐式转换：int -> double
 char c = 'A';
 i = c; // 隐式转换：char -> int
```

#### 1.4.2 显式类型转换

```cpp
 // C 风格转换
 double d = 3.14;
 int i = (int)d; // 截断小数部分
 // C++ 风格转换
 // static_cast: 静态类型转换
 i = static_cast<int>(d);
 // dynamic_cast: 动态类型转换（用于多态）
 Base* base = new Derived();
 Derived* derived = dynamic_cast<Derived*>(base);
 // const_cast: 移除 const 修饰
 const int& const_ref = i;
 int& ref = const_cast<int&>(const_ref);
 // reinterpret_cast: 重新解释类型
 int* p = &i;
 long addr = reinterpret_cast<long>(p);
```

## 2. 控制流 (Control Flow)

### 2.1 条件判断

#### 2.1.1 if 语句

```cpp
 // 基本 if 语句
 int score = 85;
 if (score >= 90) {
  std::cout << "优秀" << std::endl;
 }
  std::cout << "良好" << std::endl;
 }
  std::cout << "及格" << std::endl;
 }
  std::cout << "不及格" << std::endl;
 }
 // 嵌套 if 语句
 int x = 10, y = 20;
 if (x > 0) {
  if (y > 0) {
  std::cout << "x 和 y 都是正数" << std::endl;
  } else {
  std::cout << "x 是正数，y 不是正数" << std::endl;
  }
 }
 // 使用逻辑运算符
 int a = 5, b = 10, c = 15;
 if (a > 0 && b > 0 && c > 0) {
  std::cout << "所有数都是正数" << std::endl;
 }
 if (a > 10 || b > 10 || c > 10) {
  std::cout << "至少有一个数大于 10" << std::endl;
 }
```

#### 2.1.2 switch 语句

```cpp
 // 基本 switch 语句
 int day = 3;
 switch (day) {
  case 1:
  std::cout << "星期一" << std::endl;
  break;
  case 2:
  std::cout << "星期二" << std::endl;
  break;
  case 3:
  std::cout << "星期三" << std::endl;
  break;
  case 4:
  std::cout << "星期四" << std::endl;
  break;
  case 5:
  std::cout << "星期五" << std::endl;
  break;
  case 6:
  case 7:
  std::cout << "周末" << std::endl;
  break;
  default:
  std::cout << "无效的日期" << std::endl;
  break;
 }
 // 使用枚举的 switch 语句
 enum Color { RED, GREEN, BLUE };
 Color color = GREEN;
 switch (color) {
  case RED:
  std::cout << "红色" << std::endl;
  break;
  case GREEN:
  std::cout << "绿色" << std::endl;
  break;
  case BLUE:
  std::cout << "蓝色" << std::endl;
  break;
  default:
  std::cout << "未知颜色" << std::endl;
  break;
 }
 // 使用枚举类的 switch 语句 (C++11)
 enum class Direction { UP, DOWN, LEFT, RIGHT };
 Direction dir = Direction::UP;
 switch (dir) {
  case Direction::UP:
  std::cout << "向上" << std::endl;
  break;
  case Direction::DOWN:
  std::cout << "向下" << std::endl;
  break;
  case Direction::LEFT:
  std::cout << "向左" << std::endl;
  break;
  case Direction::RIGHT:
  std::cout << "向右" << std::endl;
  break;
 }
```

### 2.2 循环结构

#### 2.2.1 for 循环

```cpp
 // 传统 for 循环
 for (int i = 0; i < 10; ++i) {
  std::cout << i << " ";
 }
 std::cout << std::endl;
 // 循环变量作用域控制
 {
  for (int i = 0; i < 5; ++i) {
  std::cout << i << " ";
  }
  // i 在这里不可见
 }
 // 多变量 for 循环
 for (int i = 0, j = 10; i < 5 && j > 5; ++i, --j) {
  std::cout << "i: " << i << ", j: " << j << std::endl;
 }
 // 范围 for 循环 (C++11)
 std::vector<int> numbers = {1, 2, 3, 4, 5};
 for (int num : numbers) {
  std::cout << num << " ";
 }
 std::cout << std::endl;
 // 使用 auto 的范围 for 循环 (C++11)
 for (auto num : numbers) {
  std::cout << num << " ";
 }
 std::cout << std::endl;
 // 使用 const 引用的范围 for 循环（避免复制）
 for (const auto& num : numbers) {
  std::cout << num << " ";
 }
 std::cout << std::endl;
 // 使用引用的范围 for 循环（可以修改元素）
 for (auto& num : numbers) {
  num *= 2; // 每个元素都乘以 2
 }
 // 遍历数组
 int arr[] = {10, 20, 30, 40, 50};
 for (int x : arr) {
  std::cout << x << " ";
 }
 std::cout << std::endl;
```

#### 2.2.2 while 循环

```cpp
 // 基本 while 循环
 int i = 0;
 while (i < 10) {
  std::cout << i << " ";
  ++i;
 }
 std::cout << std::endl;
 // 无限循环（需要内部 break）
 i = 0;
 while (true) {
  std::cout << i << " ";
  ++i;
  if (i >= 10) {
  break;
  }
 }
 std::cout << std::endl;
 // 基于条件的 while 循环
 std::string input;
 while (true) {
  std::cout << "输入 'quit' 退出: ";
  std::cin >> input;
  if (input == "quit") {
  break;
  }
  std::cout << "你输入了: " << input << std::endl;
 }
```

#### 2.2.3 do-while 循环

```cpp
 // 基本 do-while 循环
 int i = 0;
 do {
  std::cout << i << " ";
  ++i;
 }
 std::cout << std::endl;
 // 至少执行一次的情况
 std::string password;
 do {
  std::cout << "请输入密码: ";
  std::cin >> password;
 }
 std::cout << "密码正确！" << std::endl;
```

### 2.3 跳转语句

#### 2.3.1 break 语句

```cpp
 // 在 for 循环中使用 break
 for (int i = 0; i < 10; ++i) {
  if (i == 5) {
  break; // 跳出循环
  }
  std::cout << i << " ";
 }
 // 输出: 0 1 2 3 4
 // 在 while 循环中使用 break
 int j = 0;
 while (j < 10) {
  if (j == 5) {
  break;
  }
  std::cout << j << " ";
  ++j;
 }
 // 在 switch 语句中使用 break
 int value = 2;
 switch (value) {
  case 1:
  std::cout << "值为 1" << std::endl;
  break;
  case 2:
  std::cout << "值为 2" << std::endl;
  break; // 没有这个 break 会继续执行下一个 case
  case 3:
  std::cout << "值为 3" << std::endl;
  break;
 }
```

#### 2.3.2 continue 语句

```cpp
 // 在 for 循环中使用 continue
 for (int i = 0; i < 10; ++i) {
  if (i % 2 == 0) {
  continue; // 跳过当前迭代
  }
  std::cout << i << " ";
 }
 // 输出: 1 3 5 7 9
 // 在 while 循环中使用 continue
 int j = 0;
 while (j < 10) {
  ++j;
  if (j % 2 == 0) {
  continue;
  }
  std::cout << j << " ";
 }
 // 在范围 for 循环中使用 continue
 std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
 for (auto num : nums) {
  if (num % 3 == 0) {
  continue;
  }
  std::cout << num << " ";
 }
```

#### 2.3.3 return 语句

```cpp
 // 基本 return 语句
 int add(int a, int b) {
  return a + b; // 返回值并结束函数
 }
 // 提前返回
 bool is_even(int n) {
  if (n % 2 == 0) {
  return true; // 提前返回
  }
  return false;
 }
 // 返回引用
 int& get_largest(int& a, int& b) {
  if (a > b) {
  return a;
  }
  return b;
 }
 // 返回空
 void print_hello() {
  std::cout << "Hello!" << std::endl;
  return; // 可选
 }
 int main() {
  int result = add(5, 3);
  std::cout << "5 + 3 = " << result << std::endl;
  int x = 10, y = 20;
  int& largest = get_largest(x, y);
  largest = 100; // 修改返回的引用
  std::cout << "x: " << x << ", y: " << y << std::endl;
  return 0; // 结束主函数
 }
```

#### 2.3.4 goto 语句（不推荐使用）

```cpp
 // 基本 goto 语句
 int main() {
  int i = 0;
 loop:
  std::cout << i << " ";
  ++i;
  if (i < 10) {
  goto loop; // 跳转到标签处
  }
  return 0;
 }
 // 使用 goto 跳出多层循环
 void nested_loops() {
  for (int i = 0; i < 10; ++i) {
  for (int j = 0; j < 10; ++j) {
  if (i * j > 20) {
  goto exit_loops; // 跳出所有循环
  }
  std::cout << "i: " << i << ", j: " << j << std::endl;
  }
  }
 exit_loops:
  std::cout << "跳出循环" << std::endl;
 }
 // 使用 goto 进行错误处理
 bool process_data() {
  // 模拟错误
  bool error = true;
  if (error) {
  goto error_handler;
  }
  // 正常处理
  return true;
 error_handler:
  std::cout << "处理错误" << std::endl;
  return false;
 }
```

## 3. 输入输出 (I/O)

### 3.1 标准输入输出

#### 3.1.1 输出

```cpp
 #include <iostream>
 int main() {
  // 基本输出
  std::cout << "Hello, C++!" << std::endl;
  // 多个值输出
  int x = 10;
  double y = 3.14;
  std::cout << "x = " << x << ", y = " << y << std::endl;
  // 使用 endl 换行并刷新缓冲区
  std::cout << "Line 1" << std::endl;
  std::cout << "Line 2" << std::endl;
  // 使用 \n 仅换行
  std::cout << "Line 1\nLine 2" << std::endl;
  // 输出布尔值
  bool flag = true;
  std::cout << "Flag: " << flag << std::endl; // 输出 1
  std::cout << std::boolalpha << "Flag: " << flag << std::endl; // 输出
  // 输出字符和字符串
  char c = 'A';
  std::string s = "Hello";
  std::cout << "Character: " << c << std::endl;
  std::cout << "String: " << s << std::endl;
  return 0;
 }
```

#### 3.1.2 输入

```cpp
 #include <iostream>
 #include <string>
 int main() {
  // 输入整数
  int x;
  std::cout << "Enter an integer: ";
  std::cin >> x;
  std::cout << "You entered: " << x << std::endl;
  // 输入浮点数
  double y;
  std::cout << "Enter a double: ";
  std::cin >> y;
  std::cout << "You entered: " << y << std::endl;
  // 输入布尔值
  bool flag;
  std::cout << "Enter a boolean (0 or 1): ";
  std::cin >> flag;
  std::cout << "You entered: " << std::boolalpha << flag << std::endl;
  // 输入字符
  char c;
  std::cout << "Enter a character: ";
  std::cin >> c;
  std::cout << "You entered: " << c << std::endl;
  // 输入字符串（遇到空格停止）
  std::string name;
  std::cout << "Enter your name: ";
  std::cin >> name;
  std::cout << "Hello, " << name << "!" << std::endl;
  // 输入一行字符串
  std::string line;
  std::cout << "Enter a line: ";
  std::cin.ignore(); // 忽略之前的换行符
  std::getline(std::cin, line);
  std::cout << "You entered: " << line << std::endl;
  // 输入多个值
  int a, b;
  std::cout << "Enter two integers: ";
  std::cin >> a >> b;
  std::cout << "You entered: " << a << " and " << b << std::endl;
  return 0;
 }
```

#### 3.1.3 输入验证

```cpp
 #include <iostream>
 #include <limits>
 int main() {
  int age;
  // 验证输入是否为整数
  while (true) {
  std::cout << "Enter your age: ";
  if (std::cin >> age) {
  // 输入成功
  break;
  } else {
  // 输入失败，清除错误状态
  std::cin.clear();
  // 忽略无效输入
  std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
  std::cout << "Invalid input. Please enter a number." << std::endl;
  }
  }
  std::cout << "Your age is: " << age << std::endl;
  return 0;
 }
```

### 3.2 格式化输出

```cpp
 #include <iostream>
 #include <iomanip>
 int main() {
  // 设置输出宽度
  std::cout << std::setw(10) << "Name" << std::setw(10) << "Age" << std::endl;
  std::cout << std::setw(10) << "Alice" << std::setw(10) << 25 << std::endl;
  std::cout << std::setw(10) << "Bob" << std::setw(10) << 30 << std::endl;
  // 设置填充字符
  std::cout << std::setw(10) << std::setfill('*') << "Hello" << std::endl;
  // 设置精度
  double pi = 3.1415926535;
  std::cout << "Pi: " << std::setprecision(5) << pi << std::endl;
  // 固定精度
  std::cout << "Pi (fixed): " << std::fixed << std::setprecision(2) << pi << std::endl;
  // 科学计数法
  double large_num = 123456789.123456;
  std::cout << "Large number: " << std::scientific << large_num << std::endl;
  // 十六进制输出
  int x = 255;
  std::cout << "Hex: " << std::hex << x << std::endl;
  std::cout << "Hex (uppercase): " << std::hex << std::uppercase << x << std::endl;
  // 八进制输出
  std::cout << "Octal: " << std::oct << x << std::endl;
  // 重置为十进制
  std::cout << "Decimal: " << std::dec << x << std::endl;
  // 显示正负号
  int positive = 10;
  int negative = -10;
  std::cout << "Positive: " << std::showpos << positive << std::endl;
  std::cout << "Negative: " << negative << std::endl;
  std::cout << std::noshowpos; // 关闭显示正负号
  // 显示前导零
  int num = 42;
  std::cout << "With leading zeros: " << std::setw(5) << std::setfill('0') << num << std::endl;
  return 0;
 }
```

### 3.3 文件输入输出

```cpp
 #include <iostream>
 #include <fstream>
 #include <string>
 int main() {
  // 写入文件
  std::ofstream outfile("example.txt");
  if (outfile.is_open()) {
  outfile << "Hello, File!" << std::endl;
  outfile << "This is a test." << std::endl;
  outfile << "Number: " << 42 << std::endl;
  outfile.close();
  std::cout << "File written successfully." << std::endl;
  } else {
  std::cerr << "Unable to open file for writing." << std::endl;
  }
  // 读取文件
  std::ifstream infile("example.txt");
  if (infile.is_open()) {
  std::string line;
  std::cout << "File contents:" << std::endl;
  while (std::getline(infile, line)) {
  std::cout << line << std::endl;
  }
  infile.close();
  } else {
  std::cerr << "Unable to open file for reading." << std::endl;
  }
  return 0;
 }
```

### 3.4 字符串流

```cpp
 #include <iostream>
 #include <sstream>
 #include <string>
 int main() {
  // 输出字符串流
  std::stringstream ss;
  ss << "Name: " << "Alice" << ", Age: " << 25 << ", Score: " << 95.5;
  std::string result = ss.str();
  std::cout << "String stream result: " << result << std::endl;
  // 输入字符串流
  std::string data = "10 3.14 Hello";
  std::stringstream input_ss(data);
  int i;
  double d;
  std::string s;
  input_ss >> i >> d >> s;
  std::cout << "Parsed values: " << i << ", " << d << ", " << s << std::endl;
  // 格式化数字为字符串
  std::stringstream format_ss;
  format_ss << std::fixed << std::setprecision(2) << 3.14159;
  std::string pi_str = format_ss.str();
  std::cout << "Formatted pi: " << pi_str << std::endl;
  return 0;
 }
```

## 4. 命名空间 (Namespace)

### 4.1 命名空间的定义

```cpp
 // 定义命名空间
 namespace MyNamespace {
  int add(int a, int b) {
  return a + b;
  }
  namespace Nested {
  int multiply(int a, int b) {
  return a * b;
  }
  }
 }
 int main() {
  // 使用命名空间
  int result1 = MyNamespace::add(5, 3);
  int result2 = MyNamespace::Nested::multiply(5, 3);
  std::cout << "5 + 3 = " << result1 << std::endl;
  std::cout << "5 * 3 = " << result2 << std::endl;
  return 0;
 }
```

### 4.2 using 声明

```cpp
 #include <iostream>
 // 使用命名空间中的特定成员
 using std::cout;
 using std::endl;
 int main() {
  cout << "Hello, C++!" << endl;
  return 0;
 }
```

### 4.3 using 指令

```cpp
 #include <iostream>
 // 使用整个命名空间
 using namespace std;
 int main() {
  cout << "Hello, C++!" << endl;
  return 0;
 }
```

### 4.4 命名空间别名

```cpp
 #include <iostream>
 namespace long_namespace_name {
  void func() {
  std::cout << "Function in long namespace" << std::endl;
  }
 }
 // 命名空间别名
 namespace lnn = long_namespace_name;
 int main() {
  lnn::func();
  return 0;
 }
```

## 5. 作用域 (Scope)

### 5.1 块作用域

```cpp
 int main() {
  // 全局作用域
  int global_var = 10;
  if (true) {
  // 块作用域
  int local_var = 20;
  std::cout << "local_var: " << local_var << std::endl;
  std::cout << "global_var: " << global_var << std::endl;
  }
  // 这里无法访问 local_var
  std::cout << "global_var: " << global_var << std::endl;
  return 0;
 }
```

### 5.2 函数作用域

```cpp
 void func() {
  // 函数作用域
  int func_var = 100;
  std::cout << "func_var: " << func_var << std::endl;
 }
 int main() {
  // 这里无法访问 func_var
  func();
  return 0;
 }
```

### 5.3 类作用域

```cpp
 class MyClass {
 public:
  int public_var; // 类作用域
 private:
  int private_var; // 类作用域
 }
 int main() {
  MyClass obj;
  obj.public_var = 10; // 可以访问
  // obj.private_var = 20; // 无法访问，private 成员
  return 0;
 }
```

### 5.4 命名空间作用域

```cpp
 namespace MyNS {
  int ns_var = 1000; // 命名空间作用域
 }
 int main() {
  std::cout << MyNS::ns_var << std::endl;
  return 0;
 }
```

---

## 头文件包含

**系统头文件写法：包含系统头文件**
`#include <<header>>`
```cpp
// 包含输入输出流头文件
#include <iostream>
```

---

**用户头文件写法：包含自定义头文件**
`#include "<header>"`
```cpp
// 包含当前目录下的头文件
#include "myheader.h"
```

---

## 命名空间

**基本写法：使用命名空间**
`using namespace <name>;`
```cpp
// 使用标准命名空间
using namespace std;
```

---

**作用域写法：使用命名空间中的特定成员**
`using <namespace>::<member>;`
```cpp
// 使用 std::cout
using std::cout;
```

---

**限定写法：使用完整限定名**
`<namespace>::<member>`
```cpp
// 使用完整限定名
std::cout << "Hello" << std::endl;
```

---

**定义写法：自定义命名空间**
`namespace <name> { ... }`
```cpp
// 定义命名空间
namespace MyMath {
    int add(int a, int b) { return a + b; }
}
```

---

## 输入输出

**输出写法：标准输出**
`std::cout << <value>;`
```cpp
// 输出字符串到标准输出
std::cout << "Hello C++";
```

---

**换行写法：输出并换行**
`std::cout << <value> << std::endl;`
```cpp
// 输出并换行
std::cout << "Hello" << std::endl;
```

---

**输入写法：标准输入**
`std::cin >> <variable>;`
```cpp
// 从标准输入读取
int age;
std::cin >> age;
```

---

**多值输入写法：连续读取多个值**
`std::cin >> <var1> >> <var2>;`
```cpp
// 连续读取多个值
int a, b;
std::cin >> a >> b;
```

---

## main 函数

**无参写法：无参数主函数**
`int main() { ... return 0; }`
```cpp
// 无参数形式的 main 函数
int main() {
    std::cout << "Hello" << std::endl;
    return 0;
}
```

---

**带参写法：命令行参数主函数**
`int main(int argc, char *argv[]) { ... }`
```cpp
// argc 为参数个数，argv 为参数字符串数组
int main(int argc, char *argv[]) {
    for (int i = 0; i < argc; i++) {
        std::cout << argv[i] << std::endl;
    }
    return 0;
}
```

---

## 变量声明与初始化

**基本写法：变量声明与初始化**
`<type> <var_name> = <value>;`
```cpp
// 声明并初始化变量
int x = 10;
```

---

**直接初始化写法：构造函数式初始化**
`<type> <var_name>(<value>);`
```cpp
// 直接初始化
int x(10);
```

---

**列表初始化写法：C++11 列表初始化**
`<type> <var_name>{<value>};`
```cpp
// 列表初始化
int x{10};
```

---

**auto 写法：自动类型推导**
`auto <var_name> = <value>;`
```cpp
// 编译器自动推导类型
auto x = 10;
```

---

**decltype 写法：推导表达式类型**
`decltype(<expression>) <var_name>;`
```cpp
// 推导表达式的类型
int a = 10;
decltype(a) b = 20;
```

---

**const 写法：常量声明**
`const <type> <var_name> = <value>;`
```cpp
// 声明常量
const int MAX_SIZE = 100;
```

---

**constexpr 写法：编译期常量**
`constexpr <type> <var_name> = <value>;`
```cpp
// 编译期常量
constexpr int SIZE = 10;
```

---

## 注释

**单行写法：单行注释**
`// <注释内容>`
```cpp
// 这是一个单行注释
int x = 10;
```

---

**多行写法：多行注释**
`/* <注释内容> */`
```cpp
/*
 * 这是一个多行注释
 * 可以跨越多行
 */
int y = 20;
```

---

## 引用

**基本写法：左值引用**
`<type>& <ref_name> = <var>;`
```cpp
// 引用是变量的别名
int x = 10;
int& ref = x;
```

---

**常量引用写法：const 引用**
`const <type>& <ref_name> = <value>;`
```cpp
// 常量引用，不能通过引用修改值
const int& ref = 10;
```

---

**右值引用写法：C++11 右值引用**
`<type>&& <ref_name> = <value>;`
```cpp
// 右值引用，绑定到临时值
int&& rref = 10;
```

---

## 指针

**基本写法：指针声明与初始化**
`<type>* <ptr_name> = &<var>;`
```cpp
// ptr 指向 x 的地址
int x = 10;
int* ptr = &x;
```

---

**空指针写法：C++11 nullptr**
`<type>* <ptr_name> = nullptr;`
```cpp
// 初始化为空指针
int* ptr = nullptr;
```

---

**智能指针写法：unique_ptr**
`std::unique_ptr<<type>> <ptr> = std::make_unique<<type>>(<args>);`
```cpp
#include <memory>
// 独占所有权的智能指针
std::unique_ptr<int> p = std::make_unique<int>(10);
```

---

**智能指针写法：shared_ptr**
`std::shared_ptr<<type>> <ptr> = std::make_shared<<type>>(<args>);`
```cpp
#include <memory>
// 共享所有权的智能指针
std::shared_ptr<int> p = std::make_shared<int>(10);
```

---

## 类型转换

**static_cast 写法：静态类型转换**
`static_cast<<target_type>>(<expression>)`
```cpp
// 静态类型转换
double pi = 3.14;
int rounded = static_cast<int>(pi);
```

---

**dynamic_cast 写法：动态类型转换**
`dynamic_cast<<target_type>>(<expression>)`
```cpp
// 动态类型转换（用于多态类型）
Base* base = new Derived();
Derived* derived = dynamic_cast<Derived*>(base);
```

---

**const_cast 写法：常量转换**
`const_cast<<target_type>>(<expression>)`
```cpp
// 添加或移除 const
const int* cp = &x;
int* p = const_cast<int*>(cp);
```

---

**reinterpret_cast 写法：重解释转换**
`reinterpret_cast<<target_type>>(<expression>)`
```cpp
// 重解释类型转换
long addr = reinterpret_cast<long>(ptr);
```

---

## 异常处理

**基本写法：try-catch**
`try { ... } catch (<type> <e>) { ... }`
```cpp
// 异常处理
try {
    throw std::runtime_error("Error");
} catch (const std::exception& e) {
    std::cerr << e.what() << std::endl;
}
```

---

**抛出写法：抛出异常**
`throw <expression>;`
```cpp
// 抛出异常
throw std::runtime_error("Something went wrong");
```

---

**多 catch 写法：捕获多种异常**
`try { ... } catch (<type1> <e>) { ... } catch (<type2> <e>) { ... }`
```cpp
// 捕获多种异常
try {
    // 可能抛出不同异常的代码
} catch (const std::runtime_error& e) {
    std::cerr << e.what() << std::endl;
} catch (const std::logic_error& e) {
    std::cerr << e.what() << std::endl;
}
```

---

## 编译命令

**单文件写法：编译单个源文件**
`g++ <source.cpp> -o <output>`
```bash
# 编译 hello.cpp 生成可执行文件 hello
g++ hello.cpp -o hello
```

---

**标准写法：指定 C++ 标准**
`g++ -std=c++17 <source.cpp> -o <output>`
```bash
# 使用 C++17 标准编译
g++ -std=c++17 hello.cpp -o hello
```

---

## C++23/26 新特性

**基本写法：C++23 std::print**
`std::print("<格式>", <参数>);`
```cpp
// 格式化输出到 stdout，支持 {} 占位符
#include <print>
std::print("Hello, {}! Value = {}\n", "World", 42);
// 输出：Hello, World! Value = 42
```

**基本写法：C++23 std::println**
`std::println("<格式>", <参数>);`
```cpp
// 自动换行的格式化输出
#include <print>
std::println("Sum of {} and {} is {}", 3, 5, 8);
// 输出：Sum of 3 and 5 is 8（自动换行）
```

**基本写法：C++23 if consteval**
`if consteval { }`
```cpp
// 编译期分支判断：仅在常量求值上下文中执行
constexpr int compute(int x) {
    if consteval {
        return x * 2;  // 编译期执行
    } else {
        return x + 1;  // 运行期执行
    }
}
```

**基本写法：C++23 多维下标运算符**
`operator[](size_t x, size_t y)`
```cpp
// 支持多维下标访问，简化矩阵类设计
class Matrix {
    int data[3][3];
public:
    // 多参数 operator[]
    int& operator[](size_t i, size_t j) {
        return data[i][j];
    }
};
Matrix m;
m[1, 2] = 42;  // 直接多维访问
```

**基本写法：C++23 static call operator**
`static operator()(<参数>) { }`
```cpp
// 静态调用运算符：无需实例即可调用
class Calculator {
public:
    static int operator()(int a, int b) {
        return a + b;
    }
};
// 直接通过类型名调用
int result = Calculator()(3, 4);  // 返回 7
```

**基本写法：C++26 = delete 原因**
`= delete("reason");`
```cpp
// = delete 支持说明删除原因
class NonCopyable {
public:
    NonCopyable() = default;
    // 禁用拷贝构造并说明原因
    NonCopyable(const NonCopyable&) = delete("该类不允许拷贝构造");
    NonCopyable& operator=(const NonCopyable&) = delete("该类不允许拷贝赋值");
};
```

**基本写法：C++26 pack indexing**
`typename...<T>[N]`
```cpp
// 模板参数包索引：直接访问参数包中第 N 个类型
template <typename... Ts>
using First = Ts...[0];  // 取参数包第一个类型
template <typename... Ts>
using Last = Ts...[sizeof...(Ts) - 1];  // 取参数包最后一个类型
// 使用
First<int, double, char> a = 10;   // a 为 int
Last<int, double, char> b = 3.14;  // b 为 double
```

**基本写法：C++26 hazard pointer**
`std::hazard_pointer<<T>>`
```cpp
// 危险指针：用于无锁数据结构的安全内存回收
#include <hazard_pointer>
// 获取危险指针
std::hazard_pointer hp = std::make_hazard_pointer();
// 保护对象指针，防止被回收
hp.protect(ptr);
// 操作受保护对象
if (hp.get() != nullptr) {
    hp.get()->do_something();
}
// 离开作用域自动释放保护
```

**基本写法：C++26 RCU(Read-Copy-Update)**
`std::rcu<<T>>`
```cpp
// RCU：读多写少场景的无锁同步原语
#include <rcu>
// 读端：在 RCU 域中安全访问共享数据
std::rcu_reader reader;
auto* p = shared_ptr.load();
if (p) p->read_data();
// 写端：复制更新后原子替换，并延迟回收旧数据
auto* new_data = new Data(*p);
new_data->update();
shared_ptr.store(new_data);
std::rcu_retire(p);  // 等待所有读者退出后回收
```

## 参考文献



cppreference C++ 文档：https://zh.cppreference.com/w/cpp
C++ 核心指南：https://isocpp.github.io/CppCoreGuidelines/
C++ 标准草案（WG21）：https://isocpp.org/std/the-standard
CMake 官方文档：https://cmake.org/documentation/
Compiler Explorer：https://godbolt.org/

## 延伸阅读



C++ 模板深入，见 026-cpp/062-CppTemplate 文档。
STL 容器与算法，见 026-cpp 模块 STL 文档。
并发与原子，见 026-cpp 模块并发文档。
Rust 内存安全对比，见 053-rust 模块（若已加入）。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 C++ 课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| C++ 概述与现代标准 | 001-CppOverviewAndModernStandard | 本文的前置基础 |
| C++ 基础语法 | 002-CppBasicSyntax | 本文自身 |
| C++ 类型系统 | 003-CppTypeSystem | 本文的并列主题 |
| C++ 引用 | 004-CppReference | 本文的并列主题 |
| 右值引用与移动语义 | 005-RvalueReferenceMoveSemantics | 本文的并列主题 |
| C++ 指针 | 006-PointersCppreferenceCom | 本文的并列主题 |
| 智能指针详解 | 007-N4089DeletingSafeBoolInFavorOfExplicitBool | 本文的并列主题 |
| Lambda表达式 | 008-LambdaExpression | 本文的并列主题 |
| 模板元编程 | 009-ATourOfC3rdEditionOnlineExcerpts | 本文的并列主题 |
| C++20范围 | 010-Cpp20Range | 本文的并列主题 |
| C++20模块 | 011-Cpp20Module | 本文的并列主题 |
| 设计模式与C++ | 012-DesignPatternCpp | 本文的并列主题 |
| RAII与资源管理 | 013-RAIIResourceManagement | 本文的并列主题 |
| 运算符重载 | 014-OperatorOverloading | 本文的并列主题 |
| C++ 面向对象基础 | 015-COOPBasics | 本文的前置基础 |
| C++ STL 算法详解 | 016-CSTL | 本文的并列主题 |
| 字符串处理 | 017-StringProcessing | 本文的并列主题 |
| 文件IO与文件系统 | 018-FileIOFileSystem | 本文的并列主题 |
| 异常安全 | 019-ExceptionSecurity | 本文的安全延伸 |
| 多线程与并发 | 020-MultithreadingConcurrency | 本文的并列主题 |
| 类型特征与SFINAE | 021-TypeTraitsSFINAE | 本文的并列主题 |
| 变参模板 | 022-VariadicTemplate | 本文的并列主题 |
| constexpr与编译期计算 | 023-ConstexprCompileTime | 本文的并列主题 |
| 命名空间与链接 | 024-NamespaceLinkage | 本文的并列主题 |
| C++网络编程 | 025-CppNetworkProgramming | 本文的并列主题 |
| C++ 面向对象进阶 | 026-COOPAdvanced | 本文的并列主题 |
| C++内存模型 | 027-CppMemoryModel | 本文的并列主题 |
| C++图形编程 | 028-CppGraphicsProgramming | 本文的并列主题 |
| C++工具链 | 029-CppToolchain | 本文的并列主题 |
| C++正则表达式 | 030-CppRegex | 本文的并列主题 |
| C++与Python交互 | 031-CppPythonInteraction | 本文的并列主题 |
| C++测试框架 | 032-CppTestFramework | 本文的并列主题 |
| C++与Rust对比 | 033-CppRustComparison | 本文的并列主题 |
| C++23与C++26新特性 | 034-Cpp23Cpp26NewFeatures | 本文的并列主题 |
| C++性能优化 | 035-CppPerformance | 本文的性能延伸 |
| C++序列化 | 036-CppSerialization | 本文的并列主题 |
| C++游戏开发 | 037-CppGameDev | 本文的并列主题 |
| C++嵌入式开发 | 038-CppEmbedded | 本文的并列主题 |
| C++ 内存管理 | 039-CppMemoryManagement | 本文的并列主题 |
| C++代码规范 | 040-CppCodeStyle | 本文的并列主题 |
| C++与WebAssembly | 041-CppWebAssembly | 本文的并列主题 |
| C++反射与元编程 | 042-CppReflectionMetaprogramming | 本文的并列主题 |
| C++数学库 | 043-CppMathLibrary | 本文的并列主题 |
| 智能指针 | 044-SmartPointer | 本文的并列主题 |
| C++ 日期时间 | 045-CppDateTime | 本文的并列主题 |
| C++格式化输出 | 046-CppFormatOutput | 本文的并列主题 |
| C++26 与最新标准 | 047-Cpp26AndLatestStandard | 本文的并列主题 |
| C++ STL 容器与迭代器 | 048-CSTL | 本文的并列主题 |
| 并发编程 | 049-ConcurrentProgramming | 本文的并列主题 |
| RAII资源管理 | 050-CCoreGuidelinesResourceManagement | 本文的并列主题 |
| C++ STL 算法与函数对象 | 051-CSTLAlgorithmAndFunctionObject | 本文的并列主题 |
| 移动语义详解 | 052-MoveSemanticsDetailed | 本文的并列主题 |
| 完美转发与引用折叠 | 053-PerfectForwardingReferenceCollapse | 本文的并列主题 |
| 虚函数表与多态内存布局 | 054-VTablePolymorphismMemoryLayout | 本文的并列主题 |
| 智能指针循环引用 | 055-SmartPointerCircularReference | 本文的并列主题 |
| Lambda捕获详解 | 056-LambdaCaptureDetailed | 本文的并列主题 |
| 类型萃取与SFINAE | 057-TypeExtractionSFINAE | 本文的并列主题 |
| 可变参数模板与折叠表达式 | 058-VariadicTemplateFoldExpression | 本文的并列主题 |
| C++20协程 | 059-Cpp20Coroutine | 本文的并列主题 |
| C++20概念 | 060-Cpp20Concept | 本文的并列主题 |
| C++23新特性 | 061-Cpp23NewFeatures | 本文的并列主题 |
| C++ 模板 | 062-CppTemplate | 本文的并列主题 |
| 内存序与无锁编程 | 063-MemoryOrderLockFree | 本文的并列主题 |
| C++ 异常处理与性能优化 | 064-CppExceptionAndPerformance | 本文的性能延伸 |
| C++ 调试与性能分析 | 065-CDebugPerformanceAnalysis | 本文的性能延伸 |
| C++ 项目实战 | 066-CppProjectPractice | 本文的综合应用 |
| C++ STL 容器使用速查 | 067-STLContainerUsage | 本文的并列主题 |
| C++ 结构化绑定语法速查手册 | 068-StructuredBinding | 本文的并列主题 |
| C++ STL 迭代器 | 069-CppSTLIterator | 本文的并列主题 |
| C++ tuple 与 pair | 070-CppTuplePair | 本文的并列主题 |
| C++ variant / optional / any | 071-CppVariantOptionalAny | 本文的并列主题 |
| C++ CMake 构建命令 | 072-CMakeBuild | 本文的并列主题 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
