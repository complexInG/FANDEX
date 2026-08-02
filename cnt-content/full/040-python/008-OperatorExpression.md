---
order: 80
title: 运算符与表达式
module: 'python'
category: 后端技术
difficulty: intermediate
description: 算术、比较、逻辑、位运算与运算符优先级。
author: Anonymous
updated: '2026-08-01'
related:
  - 'python/067-BasicDataType'
  - 'python/007-ListComprehensionAdvanced'
  - 'python/010-Metaclass'
  - 'python/004-PythonDescriptorProtocol'
prerequisites: []
---

## 1. 运算符分类 (Operator Categories)

### 1.1 算术运算符 (Arithmetic)

算术运算符用于执行基本的数学运算：

| 运算符 | 描述             | 示例 (a=10, b=3)   |
| ------ | ---------------- | ------------------ |
| `+`    | 加法             | `a + b = 13`       |
| `-`    | 减法             | `a - b = 7`        |
| `*`    | 乘法             | `a * b = 30`       |
| `/`    | 除法             | `a / b = 3.333...` |
| `//`   | 整除（向下取整） | `a // b = 3`       |
| `%`    | 取模（求余数）   | `a % b = 1`        |
| `**`   | 幂运算           | `a ** b = 1000`    |

#### 1.1.1 算术运算符示例

```python
 # 基本算术运算
 a = 10
 b = 3
 print(f"a + b = {a + b}") # 13
 print(f"a - b = {a - b}") # 7
 print(f"a * b = {a * b}") # 30
 print(f"a / b = {a / b}") # 3.3333333333333335
 print(f"a // b = {a // b}") # 3
 print(f"a % b = {a % b}") # 1
 print(f"a ** b = {a ** b}") # 1000
 # 负数运算
 c = -5
 print(f"-c = {-c}") # 5
 # 浮点数运算
 d = 3.14
 e = 2.71
 print(f"d + e = {d + e}") # 5.85
 print(f"d * e = {d * e}") # 8.5094
 # 混合类型运算
 f = 5
 g = 2.5
 print(f"f + g = {f + g}") # 7.5（结果为浮点数）
```

#### 1.1.2 算术运算符的特殊用法

```python
 # 字符串拼接
 first_name = "Alice"
 last_name = "Smith"
 full_name = first_name + " " + last_name
 print(full_name) # "Alice Smith"
 # 字符串重复
 print("Hello" * 3) # "HelloHelloHello"
 # 列表拼接
 list1 = [1, 2, 3]
 list2 = [4, 5, 6]
 combined = list1 + list2
 print(combined) # [1, 2, 3, 4, 5, 6]
 # 列表重复
 print([0] * 5) # [0, 0, 0, 0, 0]
```

### 1.2 比较运算符 (Relational)

比较运算符用于比较两个值的关系，返回布尔值 ``或 `False`：

| 运算符 | 描述     | 示例              |
| ------ | -------- | ----------------- |
| `==`   | 等于     | `5 == 5` →``      |
| `!=`   | 不等于   | `5 != 3` → ``     |
| `>`    | 大于     | `5 > 3` →``       |
| `<`    | 小于     | `5 < 3` → `False` |
| `>=`   | 大于等于 | `5 >= 5` → ``     |
| `<=`   | 小于等于 | `5 <= 3`→`False`  |

#### 1.2.1 比较运算符示例

```python
 # 基本比较
 x = 10
 y = 5
 print(f"x == y: {x == y}") # False
 print(f"x != y: {x != y}") #
 print(f"x > y: {x > y}") #
 print(f"x < y: {x < y}") # False
 print(f"x >= y: {x >= y}") #
 print(f"x <= y: {x <= y}") # False
 # 字符串比较（按字典序）
 s1 = "apple"
 s2 = "banana"
 print(f"s1 < s2: {s1 < s2}") # True（"apple" 在字典序中小于 "banana"）
 # 列表比较（按元素顺序）
 lst1 = [1, 2, 3]
 lst2 = [1, 2, 4]
 print(f"lst1 < lst2: {lst1 < lst2}") # True（第三个元素 3 < 4）
 # 链式比较
 age = 25
 print(f"18 <= age <= 65: {18 <= age <= 65}") #
```

### 1.3 逻辑运算符 (Logical)

逻辑运算符用于组合多个布尔表达式：

| 运算符 | 描述   | 短路特性                       | 示例                   |
| ------ | ------ | ------------------------------ | ---------------------- |
| `and`  | 逻辑与 | 如果左侧为 `False`，右侧不执行 | ` and False` → `False` |
| `or`   | 逻辑或 | 如果左侧为 ``，右侧不执行      | ` or False` → ``       |
| `not`  | 逻辑非 | 取反布尔值                     | `not ` → `False`       |

#### 1.3.1 逻辑运算符示例

```python
 # 基本逻辑运算
 a =
 b = False
 print(f"a and b: {a and b}") # False
 print(f"a or b: {a or b}") #
 print(f"not a: {not a}") # False
 print(f"not b: {not b}") #
 # 短路特性
 # and: 左侧为 False 时，右侧不执行
 def func():
  print("Function executed")
  return
 print(f"False and func(): {False and func()}") # 输出: False（func 未执行）
 print(f" and func(): { and func()}") # 输出: Function executed
  #
 # or: 左侧为  时，右侧不执行
 print(f" or func(): { or func()}") # 输出: True（func 未执行）
 print(f"False or func(): {False or func()}") # 输出: Function executed
  #
 # 实际应用
 age = 20
 is_student =
 if age >= 18 and is_student:
  print("Eligible for student discount")
 # 非布尔值的逻辑运算
 # 0, None, "", [], {}, set() 等被视为 False
 print(f"0 and 5: {0 and 5}") # 0（False）
 print(f"5 and 10: {5 and 10}") # 10（最后一个真值）
 print(f"0 or 5: {0 or 5}") # 5（第一个真值）
 print(f"5 or 10: {5 or 10}") # 5（第一个真值）
 print(f"not 0: {not 0}") #
 print(f"not 'hello': {not 'hello'}") # False
```

### 1.4 位运算符 (Bitwise)

位运算符用于对整数的二进制位进行操作：

| 运算符 | 描述     | 示例 (a=6 (0110), b=3 (0011)) |
| ------ | -------- | ----------------------------- |
| `&`    | 按位与   | `a & b = 2 (0010)`            |
| `      | `        | 按位或                        | `a  | b = 7 (0111)` |
| `^`    | 按位异或 | `a ^ b = 5 (0101)`            |
| `~`    | 按位取反 | `~a = -7 (补码表示)`          |
| `<<`   | 左移     | `a << 1 = 12 (1100)`          |
| `>>`   | 右移     | `a >> 1 = 3 (0011)`           |

#### 1.4.1 位运算符示例

```python
 # 位运算符示例
 a = 6 # 二进制: 0110
 b = 3 # 二进制: 0011
 print(f"a = {a} (0b{bin(a)[2:]})")
 print(f"b = {b} (0b{bin(b)[2:]})")
 print(f"a & b = {a & b} (0b{bin(a & b)[2:]})") # 2 (0010)
 print(f"a | b = {a | b} (0b{bin(a | b)[2:]})") # 7 (0111)
 print(f"a ^ b = {a ^ b} (0b{bin(a ^ b)[2:]})") # 5 (0101)
 print(f"~a = {~a} (0b{bin(~a)[2:]})") # -7
 print(f"a << 1 = {a << 1} (0b{bin(a << 1)[2:]})") # 12 (1100)
 print(f"a >> 1 = {a >> 1} (0b{bin(a >> 1)[2:]})") # 3 (0011)
 # 应用：检查奇偶数
 num = 7
 if num & 1:
  print(f"{num} 是奇数")
 else:
  print(f"{num} 是偶数")
 # 应用：交换两个数（不使用临时变量）
 x = 10
 y = 20
 print(f"交换前: x={x}, y={y}")
 x ^= y
 y ^= x
 x ^= y
 print(f"交换后: x={x}, y={y}")
```

### 1.5 成员运算符 (Membership)

成员运算符用于检查一个值是否存在于序列或集合中：

| 运算符   | 描述                 | 示例                     |
| -------- | -------------------- | ------------------------ |
| `in`     | 检查值是否在序列中   | `3 in [1, 2, 3]` → ``    |
| `not in` | 检查值是否不在序列中 | `4 not in [1, 2, 3]` →`` |

#### 1.5.1 成员运算符示例

```python
 # 字符串
 text = "Hello, World!"
 print(f"'H' in text: {'H' in text}") #
 print(f"'z' in text: {'z' in text}") # False
 print(f"'World' in text: {'World' in text}") #
 # 列表
 numbers = [1, 2, 3, 4, 5]
 print(f"3 in numbers: {3 in numbers}") #
 print(f"6 in numbers: {6 in numbers}") # False
 # 元组
 coordinates = (10, 20, 30)
 print(f"10 in coordinates: {10 in coordinates}") #
 # 集合
 fruits = {"apple", "banana", "orange"}
 print(f"'apple' in fruits: {'apple' in fruits}") #
 # 字典（检查键）
 person = {"name": "Alice", "age": 30}
 print(f"'name' in person: {'name' in person}") #
 print(f"'Alice' in person: {'Alice' in person}") # False（检查的是键）
 print(f"'Alice' in person.values(): {'Alice' in person.values()}") #
```

### 1.6 身份运算符 (Identity)

身份运算符用于比较两个对象的内存地址：

| 运算符                          | 描述                           | 示例         |
| ------------------------------- | ------------------------------ | ------------ |
| `is`                            | 检查两个对象是否为同一个对象   | `a is b`     |
| `is not`                        | 检查两个对象是否不是同一个对象 | `a is not b` |
| **注意**: `is` 与 `==` 的区别： |

- `is` 比较的是对象的身份（内存地址）
- `==` 比较的是对象的值

#### 1.6.1 身份运算符示例

```python
 # 身份运算符示例
 a = [1, 2, 3]
 b = a # b 指向同一个对象
 c = [1, 2, 3] # c 是一个新对象
 print(f"a is b: {a is b}") # True（指向同一个对象）
 print(f"a == b: {a == b}") # True（值相同）
 print(f"a is c: {a is c}") # False（不同对象）
 print(f"a == c: {a == c}") # True（值相同）
 # 小整数池
 x = 100
 y = 100
 print(f"x is y: {x is y}") # True（小整数被缓存）
 x = 1000
 y = 1000
 print(f"x is y: {x is y}") # False（大整数不被缓存）
 # None 的比较
 value = None
 print(f"value is None: {value is None}") # True（推荐方式）
 print(f"value == None: {value == None}") # True（不推荐）
 # 布尔值
 p =
 q =
 print(f"p is q: {p is q}") # True（布尔值被缓存）
```

## 2. 海象运算符 (Walrus Operator - `:=`)

Python 3.8 引入的海象运算符允许在表达式内部进行赋值，简化代码结构。

### 2.1 基本用法

```python
 # 基本用法
 items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
 # 传统方式
 n = len(items)
 if n > 10:
  print(f"Total items: {n}")
 # 使用海象运算符
 if (n := len(items)) > 10:
  print(f"Total items: {n}")
 # 在循环中使用
 while (line := input("Enter a line (or 'quit' to exit): ")) != "quit":
  print(f"You entered: {line}")
 # 在列表推导式中使用
 values = [1, 2, 3, 4, 5]
 squared = [x*x for x in values if (x := x*2) > 5]
 print(squared) # [16, 25]（x 先被乘以 2，然后检查是否大于 5）
```

### 2.2 应用场景

```python
 # 读取文件时使用
 with open("example.txt", "r") as f:
  while (line := f.readline()):
  print(line.strip())
 # 正则表达式匹配
 import re
 text = "Contact: john@example.com"
 if match := re.search(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", text):
  print(f"Found email: {match.group(1)}")
 # 复杂条件判断
 user = {"name": "Alice", "age": 30, "active": True}
 if (name := user.get("name")) and (age := user.get("age")) > 18:
  print(f"Welcome, {name}! You are {age} years old.")
```

## 3. 赋值运算符 (Assignment Operators)

赋值运算符用于将值赋给变量，包括复合赋值运算符：

| 运算符 | 描述         | 示例                     |
| ------ | ------------ | ------------------------ |
| `=`    | 简单赋值     | `x = 5`                  |
| `+=`   | 加法赋值     | `x += 3` → `x = x + 3`   |
| `-=`   | 减法赋值     | `x -= 3` → `x = x - 3`   |
| `*=`   | 乘法赋值     | `x *= 3` → `x = x * 3`   |
| `/=`   | 除法赋值     | `x /= 3` → `x = x / 3`   |
| `//=`  | 整除赋值     | `x //= 3` → `x = x // 3` |
| `%=`   | 取模赋值     | `x %= 3` → `x = x % 3`   |
| `**=`  | 幂运算赋值   | `x **= 3` → `x = x ** 3` |
| `&=`   | 按位与赋值   | `x &= 3` → `x = x & 3`   |
| `      | =`           | 按位或赋值               | `x  | = 3`→`x = x | 3`  |
| `^=`   | 按位异或赋值 | `x ^= 3` → `x = x ^ 3`   |
| `<<=`  | 左移赋值     | `x <<= 1` → `x = x << 1` |
| `>>=`  | 右移赋值     | `x >>= 1` → `x = x >> 1` |

### 3.1 赋值运算符示例

```python
 # 赋值运算符示例
 x = 10
 print(f"初始 x = {x}")
 x += 5 # x = x + 5
 print(f"x += 5 → x = {x}") # 15
 x -= 3 # x = x - 3
 print(f"x -= 3 → x = {x}") # 12
 x *= 2 # x = x * 2
 print(f"x *= 2 → x = {x}") # 24
 x /= 4 # x = x / 4
 print(f"x /= 4 → x = {x}") # 6.0
 x //= 2 # x = x // 2
 print(f"x //= 2 → x = {x}") # 3.0
 x %= 2 # x = x % 2
 print(f"x %= 2 → x = {x}") # 1.0
 x **= 3 # x = x ** 3
 print(f"x **= 3 → x = {x}") # 1.0
 # 位运算赋值
 y = 6 # 0110
 print(f"初始 y = {y} (0b{bin(y)[2:]})")
 y <<= 1 # y = y << 1
 print(f"y <<= 1 → y = {y} (0b{bin(y)[2:]})") # 12 (1100)
 y >>= 1 # y = y >> 1
 print(f"y >>= 1 → y = {y} (0b{bin(y)[2:]})") # 6 (0110)
 y &= 3 # y = y & 3
 print(f"y &= 3 → y = {y} (0b{bin(y)[2:]})") # 2 (0010)
```

## 4. 运算符优先级 (Precedence)

运算符优先级决定了表达式中运算的执行顺序，优先级高的运算符先执行：

| 优先级 | 运算符                                                           | 描述                     |
| ------ | ---------------------------------------------------------------- | ------------------------ |
| 1      | `()`                                                             | 括号（最高优先级）       |
| 2      | `**`                                                             | 幂运算                   |
| 3      | `~`                                                              | 按位取反                 |
| 4      | `*`, `/`, `//`, `%`                                              | 乘除、整除、取模         |
| 5      | `+`, `-`                                                         | 加减                     |
| 6      | `<<`, `>>`                                                       | 位移运算                 |
| 7      | `&`                                                              | 按位与                   |
| 8      | `^`                                                              | 按位异或                 |
| 9      | `                                                                | `                        | 按位或 |
| 10     | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | 比较运算符               |
| 11     | `not`                                                            | 逻辑非                   |
| 12     | `and`                                                            | 逻辑与                   |
| 13     | `or`                                                             | 逻辑或                   |
| 14     | `=`                                                              | 赋值运算符（最低优先级） |

### 4.1 优先级示例

```python
 # 优先级示例
 # 1. 括号优先
 print((2 + 3) * 4) # 20（先计算括号内的加法）
 # 2. 幂运算优先
 print(2 ** 3 * 4) # 32（先计算 2**3 = 8，再乘以 4）
 print(2 ** (3 * 4)) # 4096（括号改变优先级）
 # 3. 乘除优先于加减
 print(10 + 5 * 2) # 20（先计算 5*2 = 10，再加 10）
 print((10 + 5) * 2) # 30（括号改变优先级）
 # 4. 逻辑运算符优先级
 print( or False and False) # True（and 优先于 or）
 print(( or False) and False) # False（括号改变优先级）
 # 5. 比较运算符与逻辑运算符
 print(5 > 3 and 2 < 4) # True（比较运算符优先于 and）
 print(5 > (3 and 2) < 4) # True（括号改变优先级）
```

## 5. 表达式 (Expressions)

表达式是由变量、常量、运算符和函数调用组成的代码片段，它会被计算并返回一个值。

### 5.1 基本表达式

```python
 # 算术表达式
 result = 10 + 5 * 2 # 20
 # 比较表达式
 is_greater = 10 > 5 #
 # 逻辑表达式
 is_valid =  and not False #
 # 成员表达式
 is_present = 3 in [1, 2, 3] #
 # 身份表达式
 is_same = (a is b) # 取决于 a 和 b 是否指向同一对象
```

### 5.2 复杂表达式

```python
 # 复杂表达式
 a = 10
 b = 5
 c = 3
 # 混合运算符
 result = (a + b) * c / 2 # 22.5
 # 条件表达式（三元运算符）
 status = "Adult" if a >= 18 else "Minor"
 # 嵌套表达式
 result = ((a + b) * c) ** 2 # 225
 # 函数调用表达式
 result = len("Hello") + sum([1, 2, 3]) # 5 + 6 = 11
```

### 5.3 表达式求值

Python 表达式的求值遵循运算符优先级和结合性规则：

- **结合性**: 大多数运算符从左到右结合，除了幂运算符（从右到左）

```python
 # 结合性示例
 print(10 - 5 - 3) # 2（从左到右：(10-5)-3）
 print(2 ** 3 ** 2) # 512（从右到左：2**(3**2)）
 print(10 / 5 * 2) # 4.0（从左到右：(10/5)*2）
```

## 6. 最佳实践

### 6.1 运算符使用

- **括号使用**: 当表达式复杂时，使用括号提高可读性，即使括号不是必需的
- **短路特性**: 利用 `and` 和 `or` 的短路特性优化代码
- **身份比较**: 对于 `None`、``、`False`等单例对象，使用`is` 进行比较
- **成员检查**: 使用 `in` 运算符检查成员关系，它比手动遍历更高效

### 6.2 表达式编写

- **可读性**: 保持表达式简洁明了，避免过于复杂的单行表达式
- **格式化**: 对于长表达式，适当换行和缩进以提高可读性
- **优先级**: 了解运算符优先级，避免因优先级问题导致的错误
- **类型一致性**: 确保表达式中的操作数类型兼容

### 6.3 性能考虑

- **短路评估**: 利用逻辑运算符的短路特性减少不必要的计算
- **位运算**: 在处理位级操作时，位运算符比算术运算符更高效
- **成员检查**: 在大型集合中，`in` 运算符对 `set` 和 `dict` 的检查比 `list` 和 `tuple` 更快

---

## 算术运算符

**基本写法：加法运算**
`<操作数1> + <操作数2>`

```python
# 加法运算
result = 10 + 5
```

---

**基本写法：减法运算**
`<操作数1> - <操作数2>`

```python
# 减法运算
result = 10 - 5
```

---

**基本写法：乘法运算**
`<操作数1> * <操作数2>`

```python
# 乘法运算
result = 10 * 5
```

---

**基本写法：除法运算**
`<操作数1> / <操作数2>`

```python
# 除法运算（返回浮点数）
result = 10 / 3
```

---

**基本写法：整除运算**
`<操作数1> // <操作数2>`

```python
# 整除运算（向下取整）
result = 10 // 3
```

---

**基本写法：取模运算**
`<操作数1> % <操作数2>`

```python
# 取模运算（求余数）
result = 10 % 3
```

---

**基本写法：幂运算**
`<操作数1> ** <操作数2>`

```python
# 幂运算
result = 2 ** 3
```

---

**基本写法：负号运算**
`-<操作数>`

```python
# 负号运算
result = -10
```

---

**基本写法：正号运算**
`+<操作数>`

```python
# 正号运算
result = +10
```

---

## 复合赋值运算符

**基本写法：加法赋值**
`<变量> += <值>`

```python
# 加法赋值运算
x = 10
x += 5
```

---

**基本写法：减法赋值**
`<变量> -= <值>`

```python
# 减法赋值运算
x = 10
x -= 5
```

---

**基本写法：乘法赋值**
`<变量> *= <值>`

```python
# 乘法赋值运算
x = 10
x *= 5
```

---

**基本写法：除法赋值**
`<变量> /= <值>`

```python
# 除法赋值运算
x = 10
x /= 5
```

---

**基本写法：整除赋值**
`<变量> //= <值>`

```python
# 整除赋值运算
x = 10
x //= 3
```

---

**基本写法：取模赋值**
`<变量> %= <值>`

```python
# 取模赋值运算
x = 10
x %= 3
```

---

**基本写法：幂运算赋值**
`<变量> **= <值>`

```python
# 幂运算赋值
x = 2
x **= 3
```

---

## 比较运算符

**基本写法：等于比较**
`<操作数1> == <操作数2>`

```python
# 等于比较
result = (5 == 5)
```

---

**基本写法：不等于比较**
`<操作数1> != <操作数2>`

```python
# 不等于比较
result = (5 != 3)
```

---

**基本写法：大于比较**
`<操作数1> > <操作数2>`

```python
# 大于比较
result = (5 > 3)
```

---

**基本写法：小于比较**
`<操作数1> < <操作数2>`

```python
# 小于比较
result = (5 < 10)
```

---

**基本写法：大于等于比较**
`<操作数1> >= <操作数2>`

```python
# 大于等于比较
result = (5 >= 5)
```

---

**基本写法：小于等于比较**
`<操作数1> <= <操作数2>`

```python
# 小于等于比较
result = (5 <= 10)
```

---

## 链式比较

**基本写法：链式比较运算**
`<值1> < <值2> < <值3>`

```python
# 链式比较（等价于 1 < 2 and 2 < 3）
result = 1 < 2 < 3
```

---

## 逻辑运算符

**基本写法：逻辑与运算**
`<表达式1> and <表达式2>`

```python
# 逻辑与运算
result = True and False
```

---

**基本写法：逻辑或运算**
`<表达式1> or <表达式2>`

```python
# 逻辑或运算
result = True or False
```

---

**基本写法：逻辑非运算**
`not <表达式>`

```python
# 逻辑非运算
result = not True
```

---

## 短路求值

**基本写法：and 短路返回**
`<表达式1> and <表达式2>`

```python
# and 短路求值，第一个为 False 时返回第一个值
result = False and expensive_operation()
```

---

**基本写法：or 短路返回**
`<表达式1> or <表达式2>`

```python
# or 短路求值，第一个为 True 时返回第一个值
result = True or expensive_operation()
```

---

## 身份运算符

**基本写法：is 身份比较**
`<对象1> is <对象2>`

```python
# is 身份比较（判断是否为同一对象）
a = [1, 2, 3]
b = a
result = (a is b)
```

---

**基本写法：is not 身份比较**
`<对象1> is not <对象2>`

```python
# is not 身份比较
a = [1, 2, 3]
b = [1, 2, 3]
result = (a is not b)
```

---

**基本写法：使用 is 检查 None**
`<变量> is None`

```python
# 使用 is 检查 None
x = None
result = (x is None)
```

---

## 成员运算符

**基本写法：in 成员判断**
`<元素> in <容器>`

```python
# in 成员判断
result = 3 in [1, 2, 3]
```

---

**基本写法：not in 成员判断**
`<元素> not in <容器>`

```python
# not in 成员判断
result = 4 not in [1, 2, 3]
```

---

**基本写法：字符串成员判断**
`<子串> in <字符串>`

```python
# 字符串子串判断
result = "World" in "Hello, World!"
```

---

**基本写法：字典键成员判断**
`<键> in <字典>`

```python
# 字典键成员判断
result = "name" in {"name": "Alice", "age": 30}
```

---

## 位运算符

**基本写法：按位与运算**
`<操作数1> & <操作数2>`

```python
# 按位与运算
result = 5 & 3
```

---

**基本写法：按位或运算**
`<操作数1> | <操作数2>`

```python
# 按位或运算
result = 5 | 3
```

---

**基本写法：按位异或运算**
`<操作数1> ^ <操作数2>`

```python
# 按位异或运算
result = 5 ^ 3
```

---

**基本写法：按位取反运算**
`~<操作数>`

```python
# 按位取反运算
result = ~5
```

---

**基本写法：左移运算**
`<操作数> << <位数>`

```python
# 左移运算
result = 5 << 2
```

---

**基本写法：右移运算**
`<操作数> >> <位数>`

```python
# 右移运算
result = 20 >> 2
```

---

## 三元条件运算符

**单行写法：三元条件表达式**
`<值1> if <条件> else <值2>`

```python
# 三元条件表达式
age = 20
status = "Adult" if age >= 18 else "Minor"
```

---

**单行写法：嵌套三元表达式**
`<值1> if <条件1> else (<值2> if <条件2> else <值3>)`

```python
# 嵌套三元表达式
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
```

---

## 运算符优先级

**基本写法：使用括号改变优先级**
`(<表达式>)`

```python
# 使用括号明确运算优先级
result = (2 + 3) * 4
```

---

## 海象运算符

**基本写法：赋值表达式**
`(<变量> := <值>)`

```python
# 海象运算符（赋值表达式）
if (n := len([1, 2, 3])) > 2:
    print(f"List has {n} elements")
```

---

**基本写法：在 while 循环中使用海象运算符**
`while (<变量> := <表达式>): <语句>`

```python
# 在 while 循环中使用海象运算符
while (line := input()) != "quit":
    print(line)
```

---

**基本写法：在列表推导式中使用海象运算符**
`[<变量> for <元素> in <可迭代对象> if (<变量> := <表达式>)]`

```python
# 在列表推导式中使用海象运算符
data = [1, 2, 3, 4, 5]
results = [y for x in data if (y := x * 2) > 4]
```

---

## 表达式求值

**基本写法：使用 eval() 求值**
`eval(<字符串表达式>)`

```python
# 使用 eval() 求值字符串表达式
result = eval("2 + 3 * 4")
```

---

## 运算符重载

**换行写法：通过魔术方法重载运算符**
`class <类名>:`
`    def __<运算符方法>__(self, <参数>): <语句>`

```python
# 通过 __add__ 方法重载加法运算符
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

---

**基本写法：重载等于运算符**
`def __eq__(self, other): <语句>`

```python
# 通过 __eq__ 方法重载等于运算符
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

---

**基本写法：重载小于运算符**
`def __lt__(self, other): <语句>`

```python
# 通过 __lt__ 方法重载小于运算符
class Student:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score
```

---

**基本写法：重载字符串表示**
`def __repr__(self): <语句>`

```python
# 通过 __repr__ 方法重载字符串表示
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name!r})"
```

---

**基本写法：重载长度运算**
`def __len__(self): <语句>`

```python
# 通过 __len__ 方法重载 len() 函数
class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
```

---

**基本写法：重载成员判断**
`def __contains__(self, item): <语句>`

```python
# 通过 __contains__ 方法重载 in 运算符
class Matrix:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return any(item in row for row in self.data)
```
