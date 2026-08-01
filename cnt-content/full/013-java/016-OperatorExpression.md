---
order: 60
tags:
  - java
difficulty: intermediate
title: 运算符与表达式
module: java
category: 'Java Basics'
description: 算术、关系、逻辑、位运算及运算符优先级。
author: Anonymous
related:
  - java/JavaIO与NIO
  - java/Java新特性
  - java/Spring基础
  - java/SpringBoot进阶
prerequisites:
  - java/概述与开发环境
updated: '2026-08-01'
---

# Java 运算符与表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 运算符分类

### 1.1 算术运算符

算术运算符用于执行基本的数学运算，包括加法、减法、乘法、除法和取模等。

| 运算符         | 描述         | 示例 (a=10, b=3) | 结果           |
| -------------- | ------------ | ---------------- | -------------- |
| `+`            | 加法         | `a + b`          | 13             |
| `-`            | 减法         | `a - b`          | 7              |
| `*`            | 乘法         | `a * b`          | 30             |
| `/`            | 除法         | `a / b`          | 3 (整数除法)   |
| `%`            | 取模（取余） | `a % b`          | 1              |
| `++`           | 自增         | `a++` (先用后加) | 10 (a 变为 11) |
| `++`           | 自增         | `++a` (先加后用) | 11 (a 变为 11) |
| `--`           | 自减         | `b--` (先用后减) | 3 (b 变为 2)   |
| `--`           | 自减         | `--b` (先减后用) | 2 (b 变为 2)   |
| **特殊用法**： |

- `+` 运算符还可以用于字符串拼接：`"Hello" + "World"` 结果为 `"HelloWorld"`
- 当 `+` 运算符两边有一个是字符串时，会将另一个操作数转换为字符串进行拼接
  **示例**：

```java
 // 基本算术运算
 int a = 10;
 int b = 3;
 System.out.println("a + b = " + (a + b)); // 13
 System.out.println("a - b = " + (a - b)); // 7
 System.out.println("a * b = " + (a * b)); // 30
 System.out.println("a / b = " + (a / b)); // 3 (整数除法)
 System.out.println("a % b = " + (a % b)); // 1
 // 自增和自减
 int c = 5;
 System.out.println("c++ = " + c++); // 5 (先用后加)
 System.out.println("c = " + c); // 6
 System.out.println("++c = " + ++c); // 7 (先加后用)
 // 字符串拼接
 String str1 = "Hello";
 String str2 = "World";
 System.out.println(str1 + " " + str2); // "Hello World"
 System.out.println("The answer is: " + 42); // "The answer is: 42"
```

### 1.2 关系运算符

关系运算符用于比较两个值的大小关系，结果为 `boolean` 类型（``或`false`）。

| 运算符     | 描述     | 示例 (a=10, b=3) | 结果  |
| ---------- | -------- | ---------------- | ----- |
| `==`       | 等于     | `a == b`         | false |
| `!=`       | 不等于   | `a != b`         |       |
| `>`        | 大于     | `a > b`          |       |
| `<`        | 小于     | `a < b`          | false |
| `>=`       | 大于等于 | `a >= b`         |       |
| `<=`       | 小于等于 | `a <= b`         | false |
| **注意**： |

- 对于引用类型，`==` 比较的是对象的引用（内存地址），而不是对象的内容。要比较对象的内容，应使用 `equals()` 方法。
  **示例**：

```java
 // 基本类型比较
 int a = 10;
 int b = 3;
 System.out.println("a == b: " + (a == b)); // false
 System.out.println("a != b: " + (a != b)); //
 System.out.println("a > b: " + (a > b)); //
 System.out.println("a < b: " + (a < b)); // false
 System.out.println("a >= b: " + (a >= b)); //
 System.out.println("a <= b: " + (a <= b)); // false
 // 引用类型比较
 String s1 = "Hello";
 String s2 = "Hello";
 String s3 = new String("Hello");
 System.out.println("s1 == s2: " + (s1 == s2)); //  (字符串常量池)
 System.out.println("s1 == s3: " + (s1 == s3)); // false (不同对象)
 System.out.println("s1.equals(s3): " + s1.equals(s3)); //  (内容相同)
```

### 1.3 逻辑运算符

逻辑运算符用于连接布尔表达式，结果为 `boolean` 类型。

| 运算符         | 描述             | 短路特性                       | 示例 (a=true, b=false)   | 结果                           |
| -------------- | ---------------- | ------------------------------ | ------------------------ | ------------------------------ |
| `&&`           | 短路与           | 有（第一个为假则不计算第二个） | `a && b`                 | false                          |
| `              |                  | `                              | 短路或                   | 有（第一个为真则不计算第二个） | `a  |     | b`  |     |
| `!`            | 逻辑非           | 无                             | `!a`                     | false                          |
| `&`            | 逻辑与（无短路） | 无（总是计算两个操作数）       | `a & b`                  | false                          |
| `              | `                | 逻辑或（无短路）               | 无（总是计算两个操作数） | `a                             | b`  |     |
| `^`            | 逻辑异或         | 无                             | `a ^ b`                  |                                |
| **短路特性**： |

- `&&`：如果第一个操作数为 `false`，则第二个操作数不会被计算
- `||`：如果第一个操作数为 ``，则第二个操作数不会被计算
  **示例**：

```java
 // 短路与
 int x = 5;
 b boolean result1 = (x > 10) && (x++ > 0);
 System.out.println("result1: " + result1); // false
 System.out.println("x: " + x); // 5 (x++ 未执行)
 // 短路或
 int y = 5;
 b boolean result2 = (y < 10) || (y++ > 0);
 System.out.println("result2: " + result2); //
 System.out.println("y: " + y); // 5 (y++ 未执行)
 // 逻辑非
 boolean flag = true;
 System.out.println("!flag: " + !flag); // false
 // 逻辑异或
 boolean a = true;
 b boolean b = false;
 System.out.println("a ^ b: " + (a ^ b)); //
```

### 1.4 位运算符

位运算符用于对二进制位进行操作，适用于整数类型（`byte`, `short`, `int`, `long`）。

| 运算符     | 描述           | 示例 (a=6, b=3) | 二进制                 | 结果 |
| ---------- | -------------- | --------------- | ---------------------- | ---- |
| `&`        | 按位与         | `a & b`         | `110 & 011 = 010`      | 2    |
| `          | `              | 按位或          | `a                     | b`   | `110 | 011 = 111` | 7   |
| `^`        | 按位异或       | `a ^ b`         | `110 ^ 011 = 101`      | 5    |
| `~`        | 按位取反       | `~a`            | `~00000110 = 11111001` | -7   |
| `<<`       | 左移           | `a << 1`        | `110 << 1 = 1100`      | 12   |
| `>>`       | 右移（带符号） | `a >> 1`        | `110 >> 1 = 011`       | 3    |
| `>>>`      | 右移（无符号） | `a >>> 1`       | `110 >>> 1 = 011`      | 3    |
| **说明**： |

- `<<`：左移 n 位，相当于乘以 2 的 n 次方
- `>>`：右移 n 位，相当于除以 2 的 n 次方（带符号）
- `>>>`：无符号右移，高位补 0
  **示例**：

```java
 int a = 6; // 二进制: 110
 int b = 3; // 二进制: 011
 System.out.println("a & b = " + (a & b)); // 2 (010)
 System.out.println("a | b = " + (a | b)); // 7 (111)
 System.out.println("a ^ b = " + (a ^ b)); // 5 (101)
 System.out.println("~a = " + (~a)); // -7
 System.out.println("a << 1 = " + (a << 1)); // 12 (1100)
 System.out.println("a >> 1 = " + (a >> 1)); // 3 (011)
 System.out.println("a >>> 1 = " + (a >>> 1)); // 3 (011)
 // 负数的位运算
 int c = -6; // 二进制补码: 11111111111111111111111111111010
 System.out.println("c >> 1 = " + (c >> 1)); // -3 (带符号右移)
 System.out.println("c >>> 1 = " + (c >>> 1)); // 2147483645 (无符号右移)
```

### 1.5 赋值运算符

赋值运算符用于给变量赋值，包括简单赋值和复合赋值。

| 运算符     | 描述           | 示例       | 等价于        |
| ---------- | -------------- | ---------- | ------------- |
| `=`        | 简单赋值       | `a = 10`   | `a = 10`      |
| `+=`       | 加法赋值       | `a += 5`   | `a = a + 5`   |
| `-=`       | 减法赋值       | `a -= 5`   | `a = a - 5`   |
| `*=`       | 乘法赋值       | `a *= 5`   | `a = a * 5`   |
| `/=`       | 除法赋值       | `a /= 5`   | `a = a / 5`   |
| `%=`       | 取模赋值       | `a %= 5`   | `a = a % 5`   |
| `<<=`      | 左移赋值       | `a <<= 2`  | `a = a << 2`  |
| `>>=`      | 右移赋值       | `a >>= 2`  | `a = a >> 2`  |
| `>>>=`     | 无符号右移赋值 | `a >>>= 2` | `a = a >>> 2` |
| `&=`       | 按位与赋值     | `a &= 5`   | `a = a & 5`   |
| `          | =`             | 按位或赋值 | `a            | = 5` | `a = a | 5`  |
| `^=`       | 按位异或赋值   | `a ^= 5`   | `a = a ^ 5`   |
| **示例**： |

```java
 int a = 10;
 // 简单赋值
 a = 20;
 System.out.println("a = " + a); // 20
 // 复合赋值
 a += 5; // 等价于 a = a + 5
 System.out.println("a += 5: " + a); // 25
 a -= 3; // 等价于 a = a - 3
 System.out.println("a -= 3: " + a); // 22
 a *= 2; // 等价于 a = a * 2
 System.out.println("a *= 2: " + a); // 44
 a /= 4; // 等价于 a = a / 4
 System.out.println("a /= 4: " + a); // 11
 a %= 3; // 等价于 a = a % 3
 System.out.println("a %= 3: " + a); // 2
```

### 1.6 三元运算符

三元运算符是 Java 中唯一的三目运算符，用于根据条件表达式的值选择执行两个表达式中的一个。
**语法**：`条件表达式 ? 表达式1 : 表达式2`
**说明**：

- 如果条件表达式为 ``，则执行表达式1并返回其结果
- 如果条件表达式为 `false`，则执行表达式2并返回其结果
  **示例**：

```java
 // 基本用法
 int a = 10;
 int b = 20;
 int max = (a > b) ? a : b;
 System.out.println("Max: " + max); // 20
 // 嵌套使用
 int x = 5;
 int y = 10;
 int z = 15;
 int largest = (x > y) ? ((x > z) ? x : z) : ((y > z) ? y : z);
 System.out.println("Largest: " + largest); // 15
 // 用于赋值
 String result = (a > b) ? "a is larger" : "b is larger";
 System.out.println(result); // "b is larger"
```

## 2. 表达式

### 2.1 表达式的概念

表达式是由运算符和操作数组成的代码片段，用于计算一个值。表达式可以是简单的（如 `5 + 3`），也可以是复杂的（如 `(a + b) * c / d`）。

### 2.2 表达式的类型

根据表达式的结果类型，表达式可以分为以下几类：

1. **算术表达式**：结果为数值类型，如 `a + b`, `x * y`
2. **关系表达式**：结果为布尔类型，如 `a > b`, `x == y`
3. **逻辑表达式**：结果为布尔类型，如 `a && b`, `x || y`
4. **位表达式**：结果为整数类型，如 `a & b`, `x << y`
5. **赋值表达式**：结果为赋值后变量的值，如 `a = 5`, `x += 3`
6. **三元表达式**：结果为表达式1或表达式2的值，如 `(a > b) ? a : b`

### 2.3 表达式的求值

表达式的求值顺序取决于运算符的优先级和结合性。
**结合性**：当多个运算符具有相同优先级时，表达式的求值顺序（从左到右或从右到左）。

| 运算符     | 结合性   |
| ---------- | -------- |
| 算术运算符 | 从左到右 |
| 关系运算符 | 从左到右 |
| 逻辑运算符 | 从左到右 |
| 赋值运算符 | 从右到左 |
| 三元运算符 | 从右到左 |
| **示例**： |

```java
 // 结合性示例
 int a = 10;
 int b = 5;
 int c = 3;
 // 算术运算符：从左到右
 int result1 = a + b * c; // 等价于 a + (b * c) = 10 + 15 = 25
 System.out.println("result1: " + result1);
 // 赋值运算符：从右到左
 int x, y;
 x = y = 5; // 等价于 x = (y = 5)
 System.out.println("x: " + x + ", y: " + y); // x: 5, y: 5
 // 三元运算符：从右到左
 int a = 10;
 int b = 20;
 int c = 30;
 int result2 = a > b ? a : b > c ? b : c;
 // 等价于 a > b ? a : (b > c ? b : c)
 System.out.println("result2: " + result2); // 30
```

## 3. 运算符优先级

运算符优先级决定了表达式中不同运算符的执行顺序。优先级高的运算符先执行，优先级低的运算符后执行。

| 优先级     | 运算符                                                      | 结合性   |
| ---------- | ----------------------------------------------------------- | -------- |
| 1          | `()` `[]` `.`                                               | 从左到右 |
| 2          | `!` `~` `++` `--` `+` (一元) `-` (一元)                     | 从右到左 |
| 3          | `*` `/` `%`                                                 | 从左到右 |
| 4          | `+` (二元) `-` (二元)                                       | 从左到右 |
| 5          | `<<` `>>` `>>>`                                             | 从左到右 |
| 6          | `<` `<=` `>` `>=` `instanceof`                              | 从左到右 |
| 7          | `==` `!=`                                                   | 从左到右 |
| 8          | `&`                                                         | 从左到右 |
| 9          | `^`                                                         | 从左到右 |
| 10         | `                                                           | `        | 从左到右 |
| 11         | `&&`                                                        | 从左到右 |
| 12         | `                                                           |          | `        | 从左到右 |
| 13         | `? :`                                                       | 从右到左 |
| 14         | `=` `+=` `-=` `*=` `/=` `%=` `<<=` `>>=` `>>>=` `&=` `^=` ` | =`       | 从右到左 |
| **示例**： |

```java
 // 优先级示例
 int a = 10;
 int b = 5;
 int c = 3;
 int d = 2;
 // 运算顺序：先乘除后加减
 int result1 = a + b * c - d;
 // 等价于 a + (b * c) - d = 10 + 15 - 2 = 23
 System.out.println("result1: " + result1);
 // 运算顺序：先括号内，后括号外
 int result2 = (a + b) * (c - d);
 // 等价于 (10 + 5) * (3 - 2) = 15 * 1 = 15
 System.out.println("result2: " + result2);
 // 运算顺序：先关系运算，后逻辑运算
 boolean result3 = a > b && c < d;
 // 等价于 (a > b) && (c < d) =  && false = false
 System.out.println("result3: " + result3);
```

## 4. 常见陷阱与最佳实践

### 4.1 浮点精度问题

**问题**：由于浮点数的存储方式（IEEE 754 标准），某些十进制小数无法精确表示，导致计算结果出现误差。
**示例**：

```java
 double a = 0.1;
 double b = 0.2;
 double c = a + b;
 System.out.println(c); // 输出 0.30000000000000004，而不是 0.3
```

**解决方案**：

- 使用 `BigDecimal` 类进行精确计算
- 对于货币等需要精确计算的场景，应使用 `BigDecimal`
  **示例**：

```java
 import java.math.BigDecimal;
 BigDecimal a = new BigDecimal("0.1");
 BigDecimal b = new BigDecimal("0.2");
 BigDecimal c = a.add(b);
 System.out.println(c); // 输出 0.3
```

### 4.2 整数溢出问题

**问题**：当整数运算的结果超出其类型的取值范围时，会发生溢出，导致结果不正确。
**示例**：

```java
 int max = Integer.MAX_VALUE; // 2147483647
 int result = max + 1;
 System.out.println(result); // 输出 -2147483648，发生溢出
```

**解决方案**：

- 使用更大范围的整数类型（如 `long`）
- 在运算前检查是否会发生溢出
- 使用 `Math.addExact()` 等方法，在溢出时抛出异常
  **示例**：

```java
 long max = Integer.MAX_VALUE;
 long result = max + 1;
 System.out.println(result); // 输出 2147483648，正确
 // 使用 Math.addExact()
 try {
  int result2 = Math.addExact(Integer.MAX_VALUE, 1);
 }
  System.out.println("发生溢出: " + e.getMessage());
 }
```

### 4.3 字符串拼接的性能问题

**问题**：使用 `+` 运算符进行大量字符串拼接时，会创建多个临时字符串对象，影响性能。
**解决方案**：

- 对于少量字符串拼接，使用 `+` 运算符是可以接受的
- 对于大量字符串拼接，应使用 `StringBuilder` 或 `StringBuffer`
  **示例**：

```java
 // 性能较差的方式
 String result = "";
 for (int i = 0; i < 1000; i++) {
  result += " " + i;
 }
 // 性能较好的方式
 StringBuilder sb = new StringBuilder();
 for (int i = 0; i < 1000; i++) {
  sb.append(" ").append(i);
 }
 String result = sb.toString();
```

### 4.4 短路运算符的使用

**最佳实践**：

- 当第二个操作数可能会导致异常或有副作用时，应使用短路运算符 (`&&`, `||`)
- 当需要确保两个操作数都被计算时，应使用非短路运算符 (`&`, `|`)
  **示例**：

```java
 // 安全的空检查
 String str = null;
 if (str != null && str.length() > 0) {
  // 只有当 str 不为 null 时，才会计算 str.length()
  System.out.println("String length: " + str.length());
 }
 // 确保两个条件都被检查
 boolean condition1 = checkCondition1();
 boolean condition2 = checkCondition2();
 if (condition1 & condition2) {
  // 无论 condition1 是什么，都会执行 checkCondition2()
  System.out.println("Both conditions are ");
 }
```

### 4.5 位运算符的应用

**位运算符的常见应用**：

- 位掩码：用于表示一组布尔标志
- 位操作：用于高效的数学运算
- 加密和哈希算法：使用位运算进行数据变换
  **示例**：

```java
 // 位掩码示例
 int FLAG_READ = 1 << 0; // 0b0001
 int FLAG_WRITE = 1 << 1; // 0b0010
 int FLAG_EXECUTE = 1 << 2; // 0b0100
 int permissions = FLAG_READ | FLAG_WRITE; // 0b0011
 // 检查权限
 if ((permissions & FLAG_READ) != 0) {
  System.out.println("Read permission granted");
 }
 // 高效的乘除运算
 int a = 10;
 int multiplyBy2 = a << 1; // 等价于 a * 2
 int divideBy2 = a >> 1; // 等价于 a / 2
 System.out.println("Multiply by 2: " + multiplyBy2); // 20
 System.out.println("Divide by 2: " + divideBy2); // 5
```

## 5. 实际应用示例

### 5.1 示例 1：计算BMI指数

```java
 import java.util.Scanner;
 public class BMICalculator {
  public static void main(String[] args) {
  Scanner sc = new Scanner(System.in);
  System.out.print("请输入体重（公斤）: ");
  double weight = sc.nextDouble();
  System.out.print("请输入身高（米）: ");
  double height = sc.nextDouble();
  // 计算BMI
  double bmi = weight / (height * height);
  // 判断BMI等级
  String level;
  if (bmi < 18.5) {
  level = "偏瘦";
  } else if (bmi < 24) {
  level = "正常";
  } else if (bmi < 28) {
  level = "偏胖";
  } else {
  level = "肥胖";
  }
  System.out.println("您的BMI指数: " + bmi);
  System.out.println("体重等级: " + level);
  sc.close();
  }
 }
```

### 5.2 示例 2：判断闰年

```java
 import java.util.Scanner;
 public class LeapYearChecker {
  public static void main(String[] args) {
  Scanner sc = new Scanner(System.in);
  System.out.print("请输入年份: ");
  int year = sc.nextInt();
  // 判断闰年
  boolean isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
  if (isLeapYear) {
  System.out.println(year + " 是闰年");
  } else {
  System.out.println(year + " 不是闰年");
  }
  sc.close();
  }
 }
```

### 5.3 示例 3：使用位运算实现权限管理

```java
 public class PermissionManager {
  // 权限标志
  public static final int PERMISSION_READ = 1 << 0; // 0b0001
  public static final int PERMISSION_WRITE = 1 << 1; // 0b0010
  public static final int PERMISSION_EXECUTE = 1 << 2; // 0b0100
  public static final int PERMISSION_DELETE = 1 << 3; // 0b1000
  public static void main(String[] args) {
  // 分配权限
  int userPermissions = PERMISSION_READ | PERMISSION_WRITE;
  // 检查权限
  System.out.println("Read permission: " + hasPermission(userPermissions, PERMISSION_READ));
  System.out.println("Write permission: " + hasPermission(userPermissions, PERMISSION_WRITE));
  System.out.println("Execute permission: " + hasPermission(userPermissions, PERMISSION_EXECUTE));
  System.out.println("Delete permission: " + hasPermission(userPermissions, PERMISSION_DELETE));
  // 添加权限
  userPermissions |= PERMISSION_EXECUTE;
  System.out.println("\nAfter adding execute permission:");
  System.out.println("Execute permission: " + hasPermission(userPermissions, PERMISSION_EXECUTE));
  // 移除权限
  userPermissions &= ~PERMISSION_WRITE;
  System.out.println("\nAfter removing write permission:");
  System.out.println("Write permission: " + hasPermission(userPermissions, PERMISSION_WRITE));
  }
  public static boolean hasPermission(int permissions, int permission) {
  return (permissions & permission) != 0;
  }
 }
```

---

## 算术运算符

**基本写法：加法运算**
`<操作数1> + <操作数2>`
```java
// 两个整数相加
int sum = 10 + 3;
```

---

**基本写法：减法运算**
`<操作数1> - <操作数2>`
```java
// 两个整数相减
int diff = 10 - 3;
```

---

**基本写法：乘法运算**
`<操作数1> * <操作数2>`
```java
// 两个整数相乘
int product = 10 * 3;
```

---

**基本写法：除法运算**
`<操作数1> / <操作数2>`
```java
// 两个整数相除取整
int quotient = 10 / 3;
```

---

**基本写法：取模运算**
`<操作数1> % <操作数2>`
```java
// 取余数
int remainder = 10 % 3;
```

---

## 自增自减

**基本写法：后置自增**
`<变量>++`
```java
// 先使用后加 1
int a = 5;
int b = a++;
```

---

**基本写法：前置自增**
`++<变量>`
```java
// 先加 1 后使用
int a = 5;
int b = ++a;
```

---

**基本写法：后置自减**
`<变量>--`
```java
// 先使用后减 1
int a = 5;
int b = a--;
```

---

**基本写法：前置自减**
`--<变量>`
```java
// 先减 1 后使用
int a = 5;
int b = --a;
```

---

## 字符串拼接

**基本写法：字符串拼接**
`<字符串> + <其他类型>`
```java
// 字符串与字符串拼接
String result = "Hello" + " " + "World";
```

---

**基本写法：字符串与数字拼接**
`<字符串> + <数字>`
```java
// 字符串与数字拼接
String result = "The answer is: " + 42;
```

---

## 关系运算符

**基本写法：等于比较**
`<操作数1> == <操作数2>`
```java
// 比较两个值是否相等
boolean result = (10 == 3);
```

---

**基本写法：不等于比较**
`<操作数1> != <操作数2>`
```java
// 比较两个值是否不相等
boolean result = (10 != 3);
```

---

**基本写法：大于比较**
`<操作数1> > <操作数2>`
```java
// 比较左边是否大于右边
boolean result = (10 > 3);
```

---

**基本写法：小于比较**
`<操作数1> < <操作数2>`
```java
// 比较左边是否小于右边
boolean result = (10 < 3);
```

---

**基本写法：大于等于比较**
`<操作数1> >= <操作数2>`
```java
// 比较左边是否大于等于右边
boolean result = (10 >= 3);
```

---

**基本写法：小于等于比较**
`<操作数1> <= <操作数2>`
```java
// 比较左边是否小于等于右边
boolean result = (10 <= 3);
```

---

**基本写法：引用类型内容比较**
`<对象1>.equals(<对象2>)`
```java
// 比较两个字符串内容是否相同
String s1 = "Hello";
String s2 = new String("Hello");
boolean result = s1.equals(s2);
```

---

## 逻辑运算符

**基本写法：短路与**
`<布尔表达式1> && <布尔表达式2>`
```java
// 第一个为 false 则不计算第二个
boolean result = (x > 10) && (x++ > 0);
```

---

**基本写法：短路或**
`<布尔表达式1> || <布尔表达式2>`
```java
// 第一个为 true 则不计算第二个
boolean result = (y < 10) || (y++ > 0);
```

---

**基本写法：逻辑非**
`!<布尔表达式>`
```java
// 对布尔值取反
boolean result = !flag;
```

---

**基本写法：逻辑异或**
`<布尔表达式1> ^ <布尔表达式2>`
```java
// 相同为 false 不同为 true
boolean result = true ^ false;
```

---

## 位运算符

**基本写法：按位与**
`<操作数1> & <操作数2>`
```java
// 二进制位与运算
int result = 6 & 3;
```

---

**基本写法：按位或**
`<操作数1> | <操作数2>`
```java
// 二进制位或运算
int result = 6 | 3;
```

---

**基本写法：按位异或**
`<操作数1> ^ <操作数2>`
```java
// 二进制位异或运算
int result = 6 ^ 3;
```

---

**基本写法：按位取反**
`~<操作数>`
```java
// 二进制位取反
int result = ~6;
```

---

**基本写法：左移**
`<操作数> << <位数>`
```java
// 二进制位左移相当于乘以 2
int result = 6 << 1;
```

---

**基本写法：右移**
`<操作数> >> <位数>`
```java
// 二进制位右移相当于除以 2
int result = 6 >> 1;
```

---

**基本写法：无符号右移**
`<操作数> >>> <位数>`
```java
// 高位补 0 的右移
int result = -6 >>> 1;
```

---

## 赋值运算符

**基本写法：简单赋值**
`<变量> = <值>`
```java
// 给变量赋值
int a = 10;
```

---

**基本写法：加法复合赋值**
`<变量> += <值>`
```java
// 等价于 a = a + 5
int a = 10;
a += 5;
```

---

**基本写法：减法复合赋值**
`<变量> -= <值>`
```java
// 等价于 a = a - 3
int a = 10;
a -= 3;
```

---

**基本写法：乘法复合赋值**
`<变量> *= <值>`
```java
// 等价于 a = a * 2
int a = 10;
a *= 2;
```

---

**基本写法：除法复合赋值**
`<变量> /= <值>`
```java
// 等价于 a = a / 4
int a = 10;
a /= 4;
```

---

**基本写法：取模复合赋值**
`<变量> %= <值>`
```java
// 等价于 a = a % 3
int a = 10;
a %= 3;
```

---

## 三元运算符

**基本写法：三元运算符**
`<条件表达式> ? <表达式1> : <表达式2>`
```java
// 根据条件选择值
int max = (a > b) ? a : b;
```

---

**基本写法：三元运算符赋值字符串**
`<条件> ? "<字符串1>" : "<字符串2>"`
```java
// 根据条件选择字符串
String result = (a > b) ? "a is larger" : "b is larger";
```

---

## 运算符优先级

**基本写法：使用括号明确顺序**
`(<表达式>)`
```java
// 使用括号改变运算顺序
int result = (a + b) * (c - d);
```

---

## 整数溢出处理

**基本写法：溢出检查加法**
`Math.addExact(<a>, <b>)`
```java
// 溢出时抛出 ArithmeticException
int result = Math.addExact(Integer.MAX_VALUE, 1);
```

---

**基本写法：使用更大类型**
`long <变量名> = <int变量> + <值>;`
```java
// 使用 long 类型避免溢出
long max = Integer.MAX_VALUE;
long result = max + 1;
```

---

## 字符串拼接性能

**基本写法：创建 StringBuilder**
`StringBuilder <变量名> = new StringBuilder();`
```java
// 创建 StringBuilder 对象
StringBuilder sb = new StringBuilder();
```

---

**基本写法：StringBuilder 追加**
`<StringBuilder>.append(<内容>)`
```java
// 追加内容到 StringBuilder
sb.append("Hello").append(" ").append("World");
```

---

**基本写法：转换为字符串**
`<StringBuilder>.toString()`
```java
// 将 StringBuilder 转换为字符串
String result = sb.toString();
```

---

## 位运算应用

**基本写法：位掩码定义**
`int <标志> = 1 << <位数>;`
```java
// 定义权限标志位
int FLAG_READ = 1 << 0;
```

---

**基本写法：位掩码组合**
`<标志1> | <标志2>`
```java
// 组合多个权限标志
int permissions = FLAG_READ | FLAG_WRITE;
```

---

**基本写法：检查位掩码**
`(<组合标志> & <单个标志>) != 0`
```java
// 检查是否包含某权限
boolean hasRead = (permissions & FLAG_READ) != 0;
```

## 参考文献



Oracle Java 官方文档：https://docs.oracle.com/en/java/
OpenJDK 项目：https://openjdk.org/
Java 语言规范：https://docs.oracle.com/javase/specs/
Spring 官方文档：https://spring.io/projects/spring-boot
Baeldung 教程站：https://www.baeldung.com/
Maven 官方文档：https://maven.apache.org/guides/

## 延伸阅读



Java 并发与 JUC，见 013-java 模块并发文档。
JVM 内存与 GC 调优，见 013-java 模块 JVM 文档。
Spring Boot 微服务与 Kubernetes，见 013-java/041-JavaKubernetes 文档。
数据库访问（JDBC/JPA），见 019-sql 模块相关文档。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Java 全栈课程；尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Java 进阶课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Java 概述与开发环境 | 001-JavaOverviewDevEnv | 本文的前置基础 |
| 快速入门 | 002-QuickStart | 本文的前置基础 |
| 程序结构与基本语法 | 003-ProgramStructureBasicSyntax | 本文的并列主题 |
| 数据类型与类型转换 | 004-DataTypeConversion | 本文的并列主题 |
| 变量与常量 | 005-VariableConstant | 本文的并列主题 |
| 枚举与注解 | 006-JavaAnnotationsTutorial | 本文的并列主题 |
| 泛型进阶 | 007-JavaGenericsTutorial | 本文的并列主题 |
| 并发编程基础 | 008-ConcurrencyBasics | 本文的前置基础 |
| JUC并发包 | 009-JUCConcurrency | 本文的并列主题 |
| JVM类加载机制 | 010-JVMClassLoadingMechanism | 本文的原理深化 |
| JVM垃圾回收 | 011-JVMGC | 本文的并列主题 |
| Java反射 | 012-JavaReflection | 本文的并列主题 |
| Java序列化 | 013-JavaSerialization | 本文的并列主题 |
| JavaIO与NIO | 014-JavaIONIO | 本文的并列主题 |
| Java新特性 | 015-JavaNewFeatures | 本文的并列主题 |
| 运算符与表达式 | 016-OperatorExpression | 本文自身 |
| Spring 基础：IoC 容器、AOP、Bean 生命周期与企业级开发核心 | 017-SpringBasicsIoCAOPBeanLifecycle | 本文的前置基础 |
| SpringBoot进阶 | 018-SpringBootAdvanced | 本文的并列主题 |
| SpringBoot安全 | 019-SpringBootSecurity | 本文的安全延伸 |
| SpringBoot数据访问 | 020-SpringBootDataAccess | 本文的并列主题 |
| Java设计模式 | 021-JavaDesignPattern | 本文的并列主题 |
| Java函数式编程 | 022-JavaFunctionalProgramming | 本文的并列主题 |
| Java网络编程 | 023-JavaNetworkProgramming | 本文的并列主题 |
| Java日志系统 | 024-JavaLogSystem | 本文的并列主题 |
| Java单元测试 | 025-JavaUnitTest | 本文的并列主题 |
| Java构建工具 | 026-JavaBuildTool | 本文的并列主题 |
| 控制流 | 027-ControlFlow | 本文的并列主题 |
| Java与微服务 | 028-JavaMicroservice | 本文的并列主题 |
| Java与消息队列 | 029-JavaMessageQueue | 本文的并列主题 |
| Java与Redis | 030-JavaRedis | 本文的并列主题 |
| Java与Docker | 031-JavaDocker | 本文的并列主题 |
| Java与GraphQL | 032-JavaGraphQL | 本文的并列主题 |
| Java性能调优 | 033-JavaPerformanceTuning | 本文的性能延伸 |
| Java与AI | 034-JavaAI | 本文的并列主题 |
| Java与安全 | 035-JavaSecurity | 本文的安全延伸 |
| Java与WebAssembly | 036-JavaWebAssembly | 本文的并列主题 |
| Java与响应式编程 | 037-JavaReactiveProgramming | 本文的并列主题 |
| 方法详解 | 038-MethodDetailed | 本文的并列主题 |
| Java与虚拟线程 | 039-JavaVirtualThread | 本文的并列主题 |
| Java与GraalVM | 040-JavaGraalVM | 本文的并列主题 |
| Java与Kubernetes | 041-JavaKubernetes | 本文的并列主题 |
| Java记录类 | 042-JavaRecordClass | 本文的并列主题 |
| Java文本块 | 043-JavaTextBlock | 本文的并列主题 |
| Java模块系统 | 044-JavaModuleSystem | 本文的并列主题 |
| Java与数据库连接 | 045-JavaDatabaseConnection | 本文的并列主题 |
| Java 新特性与生态 | 046-JavaNewFeaturesEcosystem | 本文的并列主题 |
| 数组详解 | 047-ArrayDetailed | 本文的并列主题 |
| JVM调优 | 048-JVMtuning | 本文的性能延伸 |
| 集合框架详解 | 049-CollectionFrameworkDetailed | 本文的并列主题 |
| 并发编程详解 | 050-ConcurrencyDetailed | 本文的并列主题 |
| CompletableFuture异步编排 | 051-CompletableFutureAsync | 本文的并列主题 |
| ThreadLocal内存泄漏 | 052-ThreadLocalMemoryLeak | 本文的并列主题 |
| 反射与动态代理 | 053-ReflectionDynamicProxy | 本文的并列主题 |
| 注解处理器 | 054-AnnotationProcessor | 本文的并列主题 |
| 分代ZGC详解 | 055-GenerationalZGCDetailed | 本文的并列主题 |
| 面向对象编程 | 056-OOP | 本文的并列主题 |
| 抽象类与接口 | 057-AbstractClassInterface | 本文的并列主题 |
| 异常处理机制 | 058-ExceptionHandlingMechanism | 本文的原理深化 |
| 泛型详解 | 059-GenericDetailed | 本文的并列主题 |
| I/O 流与文件操作 | 060-IOStreamFileOperation | 本文的并列主题 |
| 多线程基础 | 061-MultithreadingBasics | 本文的前置基础 |
| JVM 内存模型 | 062-JVMMemoryModel | 本文的并列主题 |
| Lambda与函数式编程 | 063-LambdaFunctionalProgramming | 本文的并列主题 |
| Stream API | 064-StreamAPI | 本文的并列主题 |
| Spring Boot 学习笔记 | 065-SpringBootNotes | 本文的并列主题 |
| 网络编程 | 066-NetworkProgramming | 本文的并列主题 |
| Spring Cloud 微服务开发 | 067-SpringCloudMicroserviceDevelopment | 本文的并列主题 |
| Java Swing 图形界面 | 068-JavaSwingGUI | 本文的并列主题 |
| Java 项目示例：图书管理系统 | 069-JavaProjectExampleLibrarySystem | 本文的综合应用 |
| Java 理论知识点：JVM 原理、类加载机制与内存管理 | 070-JavaTheoryJVMClassLoadingMemory | 本文的原理深化 |
| Java NIO 通道与缓冲区 | 071-JavaNIOChannelBuffer | 本文的并列主题 |
| Java JDBC 数据库连接 | 072-JDBCDatabaseConnection | 本文的并列主题 |
| Java Optional 类 | 073-JavaOptionalClass | 本文的并列主题 |
| Java Executor 与 ForkJoin | 074-ExecutorForkJoinPool | 本文的并列主题 |
| Java Path 与 Files 语法速查手册 | 075-JavaPathFiles | 本文的并列主题 |
| 启动 REPL 交互环境 | 076-JavaJshellJpackage | 本文的前置基础 |
| Java 同步器 CountDownLatch/CyclicBarrier/Phaser 语法速查手册 | 077-JavaCountDownLatchCyclicBarrier | 本文的并列主题 |
| Java 阻塞队列 BlockingQueue 语法速查手册 | 078-JavaBlockingQueue | 本文的并列主题 |
| Java try-with-resources 与异常链语法速查手册 | 079-JavaTryWithResources | 本文的并列主题 |
| Java HttpClient 与 WebSocket 语法速查手册 | 080-JavaHttpClientWebSocket | 本文的并列主题 |
| Java 时间格式化 DateTimeFormatter/ZoneId 语法速查手册 | 081-JavaTimeFormatting | 本文的并列主题 |
| Java 类型擦除与桥接方法语法速查手册 | 082-JavaTypeErasure | 本文的并列主题 |
| Java 枚举进阶 EnumSet/EnumMap/枚举单例语法速查手册 | 083-JavaEnumAdvanced | 本文的并列主题 |
| Java Iterator/Iterable/Spliterator 语法速查手册 | 084-JavaIteratorIterable | 本文的并列主题 |
| Java Comparator/Comparable 语法速查手册 | 085-JavaComparatorComparable | 本文的并列主题 |
| Java String.format/printf/MessageFormat 语法速查手册 | 086-JavaStringFormat | 本文的并列主题 |
| Java Arrays 工具类语法速查手册 | 087-JavaArraysUtility | 本文的并列主题 |
| Java Objects 工具类语法速查手册 | 088-JavaObjectsUtility | 本文的并列主题 |
| Java 命令行工具 javac/java/jar/jshell/jpackage 语法速查手册 | 089-JavaCommandLineTools | 本文的并列主题 |
| Maven pom.xml 配置语法速查手册 | 090-MavenPomConfiguration | 本文的并列主题 |
| Gradle build.gradle 配置语法速查手册 | 091-GradleBuildConfiguration | 本文的并列主题 |
