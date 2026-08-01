---
order: 60
tags:
  - python
difficulty: intermediate
title: 控制流
module: python
category: 'Python Basics'
description: 条件判断、循环结构与推导式。
author: Anonymous
related:
  - python/Python与Django
  - python/Python与SQLAlchemy
  - python/Python与Celery
  - python/Python与Docker
prerequisites:
  - python/语法速查
updated: '2026-08-01'
---
## 1. 条件分支 (Selection)

条件分支用于根据不同的条件执行不同的代码块。

### 1.1 `if-elif-else` 语句

`if-elif-else` 语句是最基本的条件分支结构：

```python
 # 基本用法
 x = 7
 if x > 10:
  print("Greater than 10")
 elif x < 5:
  print("Less than 5")
 else:
  print("Between 5 and 10")
 # 多个 elif 条件
 temperature = 25
 if temperature < 0:
  print("Freezing")
 elif 0 <= temperature < 10:
  print("Cold")
 elif 10 <= temperature < 20:
  print("Mild")
 elif 20 <= temperature < 30:
  print("Warm")
 else:
  print("Hot")
 # 嵌套 if 语句
 a = 10
 b = 5
 if a > b:
  print("a is greater than b")
  if a > 20:
  print("a is also greater than 20")
  else:
  print("a is not greater than 20")
 else:
  print("a is not greater than b")
```

### 1.2 三元表达式 (Ternary Expression)

三元表达式是一种简洁的条件表达式，用于在一行代码中实现简单的条件判断：

```python
 # 基本用法
 score = 75
 result = "Pass" if score >= 60 else "Fail"
 print(result) # 输出: Pass
 # 嵌套三元表达式
 temperature = 15
 status = "Hot" if temperature > 30 else "Warm" if temperature > 20 else "Mild" if temperature > 10 else "Cold"
 print(status) # 输出: Mild
 # 与函数结合
 def get_grade(score):
  return "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
 print(get_grade(85)) # 输出: B
 # 用于列表推导式
 numbers = [1, 2, 3, 4, 5]
 even_odd = ["even" if num % 2 == 0 else "odd" for num in numbers]
 print(even_odd) # 输出: ['odd', 'even', 'odd', 'even', 'odd']
```

### 1.3 `match-case` 语句 (Python 3.10+)

`match-case` 语句（模式匹配）是 Python 3.10 引入的新特性，类似于其他语言的 `switch-case`，但功能更强大：

```python
 # 基本用法
 status = 404
 match status:
  case 200:
  print("OK")
  case 404:
  print("Not Found")
  case 500:
  print("Internal Server Error")
  case _:
  print("Unknown Status")
 # 匹配不同类型
 value = "hello"
 match value:
  case int(x):
  print(f"Integer: {x}")
  case str(x):
  print(f"String: {x}")
  case list(x):
  print(f"List: {x}")
  case _:
  print("Other type")
 # 匹配序列
 point = (1, 2)
 match point:
  case (0, 0):
  print("Origin")
  case (x, 0):
  print(f"On x-axis: {x}")
  case (0, y):
  print(f"On y-axis: {y}")
  case (x, y):
  print(f"Point: ({x}, {y})")
 # 匹配字典
 person = {"name": "Alice", "age": 30}
 match person:
  case {"name": name, "age": age}:
  print(f"Name: {name}, Age: {age}")
  case {"name": name}:
  print(f"Name: {name}, Age unknown")
  case _:
  print("Invalid person data")
 # 匹配类实例
 class Point:
  def __init__(self, x, y):
  self.x = x
  self.y = y
 p = Point(3, 4)
 match p:
  case Point(x=0, y=0):
  print("Origin")
  case Point(x=x, y=0):
  print(f"On x-axis: {x}")
  case Point(x=0, y=y):
  print(f"On y-axis: {y}")
  case Point(x=x, y=y):
  print(f"Point: ({x}, {y})")
 # 组合模式匹配
 command = "quit"
 match command:
  case "help" | "h" | "?":
  print("Show help")
  case "quit" | "q" | "exit":
  print("Exit program")
  case _:
  print("Unknown command")
```

## 2. 循环结构 (Iteration)

循环结构用于重复执行代码块，Python 提供了 `for` 循环和 `while` 循环两种主要的循环结构。

### 2.1 `for` 循环

`for` 循环用于遍历序列（如列表、元组、字符串等）或其他可迭代对象：

#### 2.1.1 基本用法

```python
 # 遍历列表
 fruits = ["apple", "banana", "cherry"]
 for fruit in fruits:
  print(fruit)
 # 遍历字符串
 text = "Hello"
 for char in text:
  print(char)
 # 遍历元组
 tuple_data = (1, 2, 3, 4, 5)
 for num in tuple_data:
  print(num)
 # 遍历字典
 person = {"name": "Alice", "age": 30, "city": "New York"}
 # 遍历键
 for key in person:
  print(key)
 # 遍历值
 for value in person.values():
  print(value)
 # 遍历键值对
 for key, value in person.items():
  print(f"{key}: {value}")
```

#### 2.1.2 使用 `range()` 函数

`range()` 函数用于生成一个数值序列，常用于 `for` 循环：

```python
 # 基本用法
 for i in range(5):
  print(i) # 输出: 0, 1, 2, 3, 4
 # 指定起始值和结束值
 for i in range(2, 7):
  print(i) # 输出: 2, 3, 4, 5, 6
 # 指定步长
 for i in range(0, 10, 2):
  print(i) # 输出: 0, 2, 4, 6, 8
 # 倒序
 for i in range(5, 0, -1):
  print(i) # 输出: 5, 4, 3, 2, 1
 # 遍历列表的索引
 fruits = ["apple", "banana", "cherry"]
 for i in range(len(fruits)):
  print(f"Index {i}: {fruits[i]}")
```

#### 2.1.3 使用 `enumerate()` 函数

`enumerate()` 函数用于同时获取索引和值：

```python
 # 基本用法
 fruits = ["apple", "banana", "cherry"]
 for index, fruit in enumerate(fruits):
  print(f"Index {index}: {fruit}")
 # 指定起始索引
 for index, fruit in enumerate(fruits, start=1):
  print(f"Position {index}: {fruit}")
 # 用于字符串
 text = "Hello"
 for index, char in enumerate(text):
  print(f"Character at {index}: {char}")
```

#### 2.1.4 使用 `zip()` 函数

`zip()` 函数用于同时遍历多个序列：

```python
 # 基本用法
 names = ["Alice", "Bob", "Charlie"]
 ages = [30, 25, 35]
 cities = ["New York", "London", "Paris"]
 for name, age, city in zip(names, ages, cities):
  print(f"{name} is {age} years old from {city}")
 # 处理不同长度的序列
 short_list = [1, 2, 3]
 long_list = [10, 20, 30, 40, 50]
 for a, b in zip(short_list, long_list):
  print(f"{a} - {b}") # 只遍历到最短序列的长度
 # 使用 zip(*) 解压缩
 pairs = [(1, 10), (2, 20), (3, 30)]
 a, b = zip(*pairs)
 print(a) # 输出: (1, 2, 3)
 print(b) # 输出: (10, 20, 30)
```

### 2.2 `while` 循环

`while` 循环用于在条件为真时重复执行代码块：

```python
 # 基本用法
 count = 0
 while count < 5:
  print(count)
  count += 1
 # 计算累加和
 sum = 0
 number = 1
 while number <= 10:
  sum += number
  number += 1
 print(f"Sum: {sum}") # 输出: 55
 # 无限循环（需要 break 退出）
 while True:
  user_input = input("Enter 'quit' to exit: ")
  if user_input == "quit":
  break
  print(f"You entered: {user_input}")
 # 使用 else 子句
 try_count = 0
 max_tries = 3
 while try_count < max_tries:
  print(f"Try {try_count + 1}")
  try_count += 1
 else:
  print("Maximum tries reached")
```

### 2.3 循环控制语句

循环控制语句用于控制循环的执行流程：

#### 2.3.1 `break` 语句

`break` 语句用于立即退出当前循环：

```python
 # 在 for 循环中使用
 fruits = ["apple", "banana", "cherry", "date"]
 target = "cherry"
 for fruit in fruits:
  if fruit == target:
  print(f"Found {target}!")
  break
  print(f"Checking {fruit}")
 # 在 while 循环中使用
 number = 0
 while number < 10:
  print(number)
  if number == 5:
  break
  number += 1
```

#### 2.3.2 `continue` 语句

`continue` 语句用于跳过本次循环，进入下一次迭代：

```python
 # 跳过偶数
 for i in range(10):
  if i % 2 == 0:
  continue
  print(i) # 输出: 1, 3, 5, 7, 9
 # 跳过空字符串
 words = ["hello", "", "world", "", "python"]
 for word in words:
  if not word:
  continue
  print(word)
```

#### 2.3.3 `pass` 语句

`pass` 语句是一个空语句，用于占位：

```python
 # 作为占位符
 for i in range(5):
  pass # 什么都不做，只是占位
 # 在条件语句中
 if x > 10:
  pass # 暂时不实现，留作以后补充
 else:
  print("x is not greater than 10")
 # 在函数定义中
 def future_function():
  pass # 暂时不实现
```

### 2.4 `for-else` 和 `while-else` 语句

Python 的循环结构支持 `else` 子句，当循环正常执行结束（没有被 `break` 中断）时，会执行 `else` 代码块：

```python
 # for-else
 fruits = ["apple", "banana", "cherry"]
 target = "date"
 for fruit in fruits:
  if fruit == target:
  print(f"Found {target}!")
  break
 else:
  print(f"{target} not found")
 # while-else
 number = 0
 target = 5
 while number < 10:
  if number == target:
  print(f"Found {target}!")
  break
  number += 1
 else:
  print(f"{target} not found in 0-9")
 # 应用：查找素数
 def is_prime(n):
  if n <= 1:
  return False
  for i in range(2, int(n**0.5) + 1):
  if n % i == 0:
  return False
  else:
  return
 print(is_prime(17)) # 输出:
 print(is_prime(18)) # 输出: False
```

## 3. 异常处理 (Exception Handling)

异常处理用于捕获和处理程序运行时的错误：

```python
 # 基本用法
 try:
  result = 10 / 0
 except ZeroDivisionError:
  print("Cannot divide by zero")
 # 捕获多种异常
 try:
  number = int(input("Enter a number: "))
  result = 10 / number
 except ValueError:
  print("Invalid input, please enter a number")
 except ZeroDivisionError:
  print("Cannot divide by zero")
 # 捕获所有异常
 try:
  # 可能引发异常的代码
  pass
 except Exception as e:
  print(f"An error occurred: {e}")
 # else 子句：当没有异常时执行
 try:
  result = 10 / 2
 except ZeroDivisionError:
  print("Cannot divide by zero")
 else:
  print(f"Result: {result}")
 # finally 子句：无论是否有异常都执行
 try:
  file = open("example.txt", "r")
  content = file.read()
 except FileNotFoundError:
  print("File not found")
 finally:
  if 'file' in locals():
  file.close()
  print("File closed")
 # 使用 with 语句（自动管理资源）
 try:
  with open("example.txt", "r") as file:
  content = file.read()
  print(content)
 except FileNotFoundError:
  print("File not found")
 # 文件会自动关闭
```

## 4. 控制流的最佳实践

### 4.1 条件分支最佳实践

- **保持条件简洁**: 避免过于复杂的条件表达式
- **使用括号**: 当条件复杂时，使用括号提高可读性
- **避免嵌套过深**: 尽量减少 `if` 语句的嵌套层级
- **使用 `match-case`**: 对于多条件判断，优先使用 `match-case`（Python 3.10+）
- **使用常量**: 将魔法数字定义为常量，提高代码可读性

### 4.2 循环最佳实践

- **选择合适的循环类型**: 对于已知次数的循环使用 `for`，对于未知次数的循环使用 `while`
- **使用 `enumerate()`**: 当需要索引和值时，使用 `enumerate()` 函数
- **使用 `zip()`**: 当需要同时遍历多个序列时，使用 `zip()` 函数
- **避免无限循环**: 确保循环有明确的退出条件
- **使用 `for-else`**: 当需要检查循环是否正常完成时，使用 `for-else` 结构

### 4.3 异常处理最佳实践

- **捕获具体异常**: 尽量捕获具体的异常类型，而不是所有异常
- **保持 `try` 块简洁**: 只在 `try` 块中放置可能引发异常的代码
- **使用 `with` 语句**: 对于需要资源管理的操作，使用 `with` 语句
- **记录异常**: 对于重要的异常，使用日志记录而不是简单打印
- **避免过度使用异常**: 不要将异常用于正常的控制流

### 4.4 代码风格

- **缩进**: 使用 4 个空格进行缩进
- **空行**: 在不同的代码块之间使用空行分隔
- **注释**: 为复杂的条件和循环添加注释
- **命名**: 使用有意义的变量和函数名
- **长度**: 保持每行代码长度不超过 79 个字符

---

## if 条件语句

**基本写法：基本 if 语句**
`if <条件>: <语句>`

```python
# 基本 if 语句
if x > 0:
    print("正数")
```

---

**基本写法：if-else 语句**
`if <条件>: <语句1> else: <语句2>`

```python
# if-else 语句
if age >= 18:
    print("成年")
else:
    print("未成年")
```

---

**基本写法：if-elif-else 语句**
`if <条件1>: <语句1> elif <条件2>: <语句2> else: <语句3>`

```python
# if-elif-else 语句
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

---

**换行写法：多条件 if 语句**
`if (<条件1> and`
`    <条件2>):`
`    <语句>`

```python
# 多条件 if 语句（换行书写）
if (age >= 18 and
    age <= 65 and
    has_id):
    print("符合条件")
```

---

## 三元条件表达式

**单行写法：三元条件表达式**
`<值1> if <条件> else <值2>`

```python
# 三元条件表达式
status = "成年" if age >= 18 else "未成年"
```

---

## match-case 语句

**基本写法：match-case 基本用法**
`match <对象>: case <模式>: <语句>`

```python
# match-case 基本用法
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")
```

---

**基本写法：match-case 字面量模式**
`match <对象>: case <字面量>: <语句>`

```python
# match-case 字面量模式匹配
match color:
    case "red":
        print("红色")
    case "green":
        print("绿色")
    case "blue":
        print("蓝色")
```

---

**基本写法：match-case 变量绑定**
`match <对象>: case <变量>: <语句>`

```python
# match-case 变量绑定模式
match point:
    case (0, 0):
        print("原点")
    case (0, y):
        print(f"y 轴上，y={y}")
    case (x, 0):
        print(f"x 轴上，x={x}")
    case (x, y):
        print(f"点 ({x}, {y})")
```

---

**基本写法：match-case 类模式匹配**
`match <对象>: case <类名>(<属性>): <语句>`

```python
# match-case 类模式匹配
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

match point:
    case Point(x=0, y=0):
        print("原点")
    case Point(x=x, y=0):
        print(f"x 轴上，x={x}")
    case Point(x=0, y=y):
        print(f"y 轴上，y={y}")
    case Point(x=x, y=y):
        print(f"点 ({x}, {y})")
```

---

**基本写法：match-case 序列模式**
`match <序列>: case [<元素1>, <元素2>]: <语句>`

```python
# match-case 序列模式匹配
match command:
    case [action]:
        print(f"单个命令: {action}")
    case [action, obj]:
        print(f"命令: {action} {obj}")
    case [action, *args]:
        print(f"命令: {action}，参数: {args}")
```

---

**基本写法：match-case 映射模式**
`match <字典>: case {"<键>": <值>}: <语句>`

```python
# match-case 映射模式匹配
match config:
    case {"host": str(host), "port": int(port)}:
        print(f"连接 {host}:{port}")
    case {"socket": str(path)}:
        print(f"Unix socket: {path}")
```

---

**基本写法：match-case 守卫条件**
`match <对象>: case <模式> if <条件>: <语句>`

```python
# match-case 守卫条件
match number:
    case n if n < 0:
        print("负数")
    case 0:
        print("零")
    case n if n > 0:
        print("正数")
```

---

**基本写法：match-case 或模式**
`match <对象>: case <模式1> | <模式2>: <语句>`

```python
# match-case 或模式匹配
match status:
    case 200 | 201:
        print("成功")
    case 400 | 404:
        print("客户端错误")
    case 500 | 502:
        print("服务器错误")
```

---

## while 循环

**基本写法：while 循环**
`while <条件>: <语句>`

```python
# while 循环
count = 0
while count < 5:
    print(count)
    count += 1
```

---

**基本写法：while-else 语句**
`while <条件>: <语句> else: <语句>`

```python
# while-else 语句（循环正常结束执行 else）
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("循环结束")
```

---

**基本写法：break 跳出循环**
`while <条件>: break`

```python
# 使用 break 跳出循环
while True:
    user_input = input("输入 quit 退出: ")
    if user_input == "quit":
        break
    print(f"你输入了: {user_input}")
```

---

**基本写法：continue 跳过本次迭代**
`while <条件>: continue`

```python
# 使用 continue 跳过本次迭代
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
```

---

## for 循环

**基本写法：遍历可迭代对象**
`for <变量> in <可迭代对象>: <语句>`

```python
# 遍历列表
for item in [1, 2, 3]:
    print(item)
```

---

**基本写法：遍历字符串**
`for <字符> in <字符串>: <语句>`

```python
# 遍历字符串
for char in "Hello":
    print(char)
```

---

**基本写法：遍历字典**
`for <键>, <值> in <字典>.items(): <语句>`

```python
# 遍历字典的键值对
for key, value in {"a": 1, "b": 2}.items():
    print(f"{key}: {value}")
```

---

**基本写法：遍历字典键**
`for <键> in <字典>: <语句>`

```python
# 遍历字典的键
for key in {"a": 1, "b": 2}:
    print(key)
```

---

**基本写法：遍历字典值**
`for <值> in <字典>.values(): <语句>`

```python
# 遍历字典的值
for value in {"a": 1, "b": 2}.values():
    print(value)
```

---

**基本写法：使用 range() 生成序列**
`for <变量> in range(<stop>): <语句>`

```python
# 使用 range() 遍历数字序列
for i in range(5):
    print(i)
```

---

**基本写法：使用 range() 指定起止**
`for <变量> in range(<start>, <stop>): <语句>`

```python
# 使用 range() 指定起始和结束
for i in range(1, 6):
    print(i)
```

---

**基本写法：使用 range() 指定步长**
`for <变量> in range(<start>, <stop>, <step>): <语句>`

```python
# 使用 range() 指定步长
for i in range(0, 10, 2):
    print(i)
```

---

**基本写法：使用 enumerate() 获取索引**
`for <索引>, <值> in enumerate(<可迭代对象>): <语句>`

```python
# 使用 enumerate() 获取索引和值
for index, value in enumerate(["a", "b", "c"]):
    print(f"{index}: {value}")
```

---

**基本写法：enumerate() 指定起始索引**
`for <索引>, <值> in enumerate(<可迭代对象>, start=<n>): <语句>`

```python
# 使用 enumerate() 指定起始索引
for index, value in enumerate(["a", "b", "c"], start=1):
    print(f"{index}: {value}")
```

---

**基本写法：使用 zip() 并行遍历**
`for <变量1>, <变量2> in zip(<可迭代对象1>, <可迭代对象2>): <语句>`

```python
# 使用 zip() 并行遍历多个可迭代对象
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

---

**基本写法：for-else 语句**
`for <变量> in <可迭代对象>: <语句> else: <语句>`

```python
# for-else 语句（循环正常结束执行 else）
for item in [1, 2, 3]:
    print(item)
else:
    print("循环结束")
```

---

**基本写法：嵌套循环**
`for <变量1> in <可迭代对象1>: for <变量2> in <可迭代对象2>: <语句>`

```python
# 嵌套循环
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

---

## 循环控制语句

**基本写法：break 跳出 for 循环**
`for <变量> in <可迭代对象>: if <条件>: break`

```python
# 使用 break 跳出 for 循环
for item in [1, 2, 3, 4, 5]:
    if item == 3:
        break
    print(item)
```

---

**基本写法：continue 跳过 for 循环迭代**
`for <变量> in <可迭代对象>: if <条件>: continue`

```python
# 使用 continue 跳过 for 循环的本次迭代
for item in [1, 2, 3, 4, 5]:
    if item % 2 == 0:
        continue
    print(item)
```

---

**基本写法：pass 空语句**
`for <变量> in <可迭代对象>: pass`

```python
# 使用 pass 作为循环体占位符
for item in items:
    pass
```

---

## 无限循环

**基本写法：while True 无限循环**
`while True: <语句>`

```python
# while True 无限循环
while True:
    response = get_input()
    if response == "exit":
        break
    process(response)
```

---

## 循环中的 else 与 break

**基本写法：循环 break 不执行 else**
`for <变量> in <可迭代对象>: if <条件>: break else: <语句>`

```python
# 循环中 break 时不执行 else 块
for item in [1, 2, 3, 4, 5]:
    if item == 3:
        print("找到 3")
        break
else:
    print("未找到 3")
```

---

## 迭代器与可迭代对象

**基本写法：使用 iter() 获取迭代器**
`iter(<可迭代对象>)`

```python
# 获取迭代器
my_iter = iter([1, 2, 3])
```

---

**基本写法：使用 next() 获取下一个值**
`next(<迭代器>)`

```python
# 获取迭代器的下一个值
print(next(my_iter))
```

---

**基本写法：next() 指定默认值**
`next(<迭代器>, <默认值>)`

```python
# 获取迭代器的下一个值，指定默认值
print(next(my_iter, None))
```

---

**换行写法：自定义迭代器类**
`class <类名>:`
`    def __iter__(self): <语句>`
`    def __next__(self): <语句>`

```python
# 自定义迭代器类
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
```

---

**换行写法：可迭代对象（仅实现 __iter__）**
`class <类名>:`
`    def __iter__(self): yield <值>`

```python
# 可迭代对象（使用 yield 实现）
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1
```

---

## 生成器表达式

**基本写法：生成器表达式**
`(<表达式> for <变量> in <可迭代对象>)`

```python
# 生成器表达式
squares = (x ** 2 for x in range(10))
print(next(squares))
```

---

**基本写法：带条件的生成器表达式**
`(<表达式> for <变量> in <可迭代对象> if <条件>)`

```python
# 带条件的生成器表达式
evens = (x for x in range(20) if x % 2 == 0)
print(list(evens))
```

---

## 参考文献

Python 官方文档：https://docs.python.org/zh-cn/3/
PEP 8 样式指南：https://peps.python.org/pep-0008/
Python 之禅（PEP 20）：https://peps.python.org/pep-0020/
Python 类型注解指南（PEP 484）：https://peps.python.org/pep-0484/
Python 打包用户指南：https://packaging.python.org/
Real Python 教程站：https://realpython.com/

## 延伸阅读

Python 数据类型与内置容器，见 040-python 模块的基础文档。
Python 异步编程（asyncio/FastAPI），见 040-python 模块的异步与 Web 文档。
Python 数据分析（NumPy/Pandas），见 051-data-analysis 模块。
Python 与数据库交互（SQLAlchemy），见 019-sql 模块相关文档。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Python 全栈课程；尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Python 后端课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Python 概述与环境配置 | 001-PythonOverviewEnvSetup | 本文的前置基础 |
| 程序结构与基本语法 | 002-ProgramStructureBasicSyntax | 本文的并列主题 |
| 变量与常量 | 003-VariableConstant | 本文的并列主题 |
| Python 描述符协议：属性访问的底层机制与工程实践 | 004-PythonDescriptorProtocol | 本文的原理深化 |
| Python 基础数据类型：从对象模型到工程实践的深度解析 | 005-PythonBasicsDataTypeObjectModelPracticeDeepAnalysis | 本文的前置基础 |
| 协程与asyncio | 006-CoroutineAsyncio | 本文的并列主题 |
| 列表推导式进阶 | 007-ListComprehensionAdvanced | 本文的并列主题 |
| 运算符与表达式 | 008-OperatorExpression | 本文的并列主题 |
| Python与虚拟环境 | 009-PythonVirtualEnv | 本文的前置基础 |
| 元类 | 010-Metaclass | 本文的并列主题 |
| Python与SQLAlchemy | 011-PythonSQLAlchemy | 本文的并列主题 |
| 多进程与多线程 | 012-MultiprocessingMultithreading | 本文的并列主题 |
| Python与FastAPI | 013-PythonFastAPI | 本文的并列主题 |
| Python与Django | 014-PythonDjango | 本文的并列主题 |
| 数据类与Pydantic | 015-DataClassPydantic | 本文的并列主题 |
| Python与Redis | 016-PythonRedis | 本文的并列主题 |
| Python 与 Celery：分布式任务队列的设计、实现与工程实践 | 017-PythonCeleryDistributedTaskQueue | 本文的并列主题 |
| 控制流 | 018-ControlFlow | 本文自身 |
| Python与Docker | 019-PythonDocker | 本文的并列主题 |
| Python与机器学习 | 020-PythonMachineLearning | 本文的并列主题 |
| Python与深度学习 | 021-PythonDeepLearning | 本文的并列主题 |
| Python与NLP | 022-PythonAndNLP | 本文的并列主题 |
| Python与计算机视觉 | 023-PythonComputerVision | 本文的并列主题 |
| Python与Web爬虫 | 024-WebScrapingWithPython | 本文的并列主题 |
| Python与自动化 | 025-PythonAutomationCookbook | 本文的并列主题 |
| 函数详解 | 026-FunctionDetailed | 本文的并列主题 |
| Python与日志 | 027-PythonLog | 本文的并列主题 |
| Python与加密 | 028-PythonAndCryptography | 本文的安全延伸 |
| Python与测试 | 029-PythonTest | 本文的并列主题 |
| Python 与配置管理：从环境变量到云原生动态配置的工程实践 | 030-Python | 本文的前置基础 |
| 装饰器 | 031-Decorator | 本文的并列主题 |
| Python与消息队列 | 032-PythonMessageQueue | 本文的并列主题 |
| Python与gRPC | 033-PythongRPC | 本文的并列主题 |
| Python与WebSocket | 034-PythonWebSocket | 本文的并列主题 |
| Python与CI-CD | 035-PythonCICD | 本文的并列主题 |
| Python与性能优化 | 036-PythonPerformance | 本文的性能延伸 |
| 内置数据结构 | 037-BuiltinDataStructure | 本文的并列主题 |
| 正则表达式 | 038-Regex | 本文的并列主题 |
| Python与CLI | 039-PythonCLI | 本文的并列主题 |
| Python与设计模式 | 040-PythonDesignPattern | 本文的并列主题 |
| Python与打包发布 | 041-ASurveyOfPythonPackagingPastPresentAndFuture | 本文的并列主题 |
| Python 与 Jupyter：交互式计算、数据分析与可复现研究 | 042-PythonJupyter | 本文的并列主题 |
| Python与GraphQL | 043-PythonGraphQL | 本文的并列主题 |
| Python与代码质量 | 044-PythonCodeQuality | 本文的并列主题 |
| 并发编程 | 045-ConcurrentProgramming | 本文的并列主题 |
| Python与数据库迁移 | 046-PythonDatabaseMigration | 本文的并列主题 |
| Python与OAuth2 | 047-PythonOAuth2 | 本文的并列主题 |
| Python与向量数据库 | 048-PythonVectorDatabase | 本文的并列主题 |
| Python 进阶与最新特性 | 049-PythonAdvancedLatestFeature | 本文的并列主题 |
| 推导式与生成器 | 050-ComprehensionGenerator | 本文的并列主题 |
| 模块、包与工程化 | 051-ModulePackageEngineering | 本文的并列主题 |
| 上下文管理器 | 052-ContextManager | 本文的并列主题 |
| 元类与单例模式 | 053-MetaclassSingleton | 本文的并列主题 |
| 异步编程详解 | 054-AsyncProgrammingDetailed | 本文的并列主题 |
| 弱引用 | 055-WeakReference | 本文的并列主题 |
| 打包与发布 | 056-PackagePublish | 本文的并列主题 |
| 描述符 | 057-Descriptor | 本文的并列主题 |
| 数据类与字段默认值 | 058-DataClassFieldDefault | 本文的并列主题 |
| 生成器与协程 | 059-GeneratorCoroutine | 本文的并列主题 |
| 类型注解与mypy | 060-TypeAnnotationMypy | 本文的并列主题 |
| 面向对象编程 | 061-OOP | 本文的并列主题 |
| 装饰器进阶 | 062-DecoratorAdvanced | 本文的并列主题 |
| 异常处理 | 063-ExceptionHandling | 本文的并列主题 |
| 文件 I/O 与上下文管理器 | 064-FileIOContextManager | 本文的并列主题 |
| Python 项目示例：网页爬虫与数据分析 | 065-PythonProjectExampleWebCrawlerDataAnalysis | 本文的综合应用 |
| Python 理论知识点 | 066-PythonTheoryKnowledge | 本文的并列主题 |
| 基础数据类型 | 067-BasicDataType | 本文的前置基础 |
| Python 面向对象基础 | 068-COOPBasics | 本文的前置基础 |
| Python 面向对象进阶 | 069-COOPAdvanced | 本文的并列主题 |
| Python pathlib 路径操作 | 070-Pathlib | 本文的并列主题 |
| Python itertools 迭代工具 | 071-Itertools | 本文的并列主题 |
| Python functools 函数工具 | 072-Functools | 本文的并列主题 |
| Python datetime 与 time | 073-DatetimeTime | 本文的并列主题 |
| Python 序列化 JSON/CSV/Pickle | 074-SerializationJsonCsvPickle | 本文的并列主题 |
| Python 网络编程 socket/http | 075-NetworkSocketHttp | 本文的并列主题 |
| Python sys/os 平台接口 | 076-SysOsPlatform | 本文的并列主题 |
| Python math/random/statistics | 077-MathRandomStatistics | 本文的并列主题 |
| Python subprocess 子进程 | 078-Subprocess | 本文的并列主题 |
| Python logging 日志配置 | 079-Logging | 本文的并列主题 |
| Python 测试 unittest/pytest | 080-UnittestPytest | 本文的并列主题 |
| Python 字符串格式化与方法 | 081-StringFormattingMethods | 本文的并列主题 |
| Python argparse 命令行参数解析 | 082-ArgparseCli | 本文的并列主题 |
| Python typing 进阶 | 083-TypingAdvanced | 本文的并列主题 |
| Python enum 枚举 | 084-Enum | 本文的并列主题 |
| Python hashlib 与 hmac | 085-HashlibHmac | 本文的并列主题 |
| Python ssl 安全套接字 | 086-SslCrypto | 本文的安全延伸 |
| Python http.client HTTP 客户端 | 087-HttpClient | 本文的并列主题 |
| Python sqlite3 数据库 | 088-Sqlite3 | 本文的并列主题 |
| Python zipfile 与 tarfile | 089-ZipfileTarfile | 本文的并列主题 |
| Python array 与 bisect | 090-ArrayBisect | 本文的并列主题 |
| Python 字符串与文本处理 | 091-StringText | 本文的并列主题 |
| Python decimal 与 fractions | 092-DecimalFractions | 本文的并列主题 |
| Python shutil 与 tempfile | 093-ShutilTempfile | 本文的并列主题 |
| Python gc inspect dis | 094-GcInspect | 本文的并列主题 |
| Python traceback 与 warnings | 095-TracebackWarnings | 本文的并列主题 |
| Python httpx 与 requests | 096-HttpxRequests | 本文的并列主题 |
| Python 性能分析与优化 | 097-ProfilingOptimization | 本文的性能延伸 |
