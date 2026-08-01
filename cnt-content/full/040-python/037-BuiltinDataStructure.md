---
order: 80
tags:
  - python
difficulty: intermediate
title: 内置数据结构
module: python
category: 'Python Basics'
description: 列表、元组、字典、集合的操作与性能特征。
author: Anonymous
related:
  - 'python/Python与CI-CD'
  - python/Python与性能优化
  - python/正则表达式
  - python/Python与设计模式
prerequisites:
  - python/语法速查
updated: '2026-08-01'
---
## 1. 列表 (List - `list`)

列表是Python中最常用的数据结构之一，它是一个有序、可变的序列，允许存储重复元素。

### 1.1 列表的创建

```python
 # 创建空列表
 empty_list = []
 empty_list = list()
 # 创建带有初始元素的列表
 numbers = [1, 2, 3, 4, 5]
 fruits = ["apple", "banana", "cherry"]
 mixed = [1, "apple", True, 3.14]
 # 使用列表推导式创建列表
 squares = [x ** 2 for x in range(10)]
 print(squares) # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 # 使用range创建列表
 numbers = list(range(1, 10, 2))
 print(numbers) # 输出: [1, 3, 5, 7, 9]
 # 复制列表
 original = [1, 2, 3]
 copy1 = original.copy()
 copy2 = list(original)
 copy3 = original[:] # 切片复制
```

### 1.2 列表的访问

```python
 fruits = ["apple", "banana", "cherry"]
 # 通过索引访问元素
 print(fruits[0]) # 输出: apple
 print(fruits[1]) # 输出: banana
 print(fruits[-1]) # 输出: cherry (负索引从末尾开始)
 # 切片操作
 print(fruits[1:3]) # 输出: ['banana', 'cherry'] (从索引1到2)
 print(fruits[:2]) # 输出: ['apple', 'banana'] (从开始到索引1)
 print(fruits[1:]) # 输出: ['banana', 'cherry'] (从索引1到结束)
 print(fruits[::-1]) # 输出: ['cherry', 'banana', 'apple'] (反转列表)
 # 检查元素是否存在
 print("apple" in fruits) # 输出:
 print("orange" in fruits) # 输出: False
 # 获取列表长度
 print(len(fruits)) # 输出: 3
```

### 1.3 列表的修改

```python
 fruits = ["apple", "banana", "cherry"]
 # 修改元素
 fruits[1] = "grape"
 print(fruits) # 输出: ['apple', 'grape', 'cherry']
 # 添加元素
 fruits.append("orange") # 在末尾添加
 print(fruits) # 输出: ['apple', 'grape', 'cherry', 'orange']
 fruits.insert(1, "pear") # 在指定位置插入
 print(fruits) # 输出: ['apple', 'pear', 'grape', 'cherry', 'orange']
 # 扩展列表
 more_fruits = ["mango", "kiwi"]
 fruits.extend(more_fruits) # 添加另一个列表的所有元素
 print(fruits) # 输出: ['apple', 'pear', 'grape', 'cherry', 'orange', 'mango', 'kiwi']
 # 删除元素
 fruits.remove("cherry") # 移除指定值的元素
 print(fruits) # 输出: ['apple', 'pear', 'grape', 'orange', 'mango', 'kiwi']
 popped = fruits.pop() # 移除并返回最后一个元素
 print(popped) # 输出: kiwi
 print(fruits) # 输出: ['apple', 'pear', 'grape', 'orange', 'mango']
 popped = fruits.pop(1) # 移除并返回指定位置的元素
 print(popped) # 输出: pear
 print(fruits) # 输出: ['apple', 'grape', 'orange', 'mango']
 # 清空列表
 fruits.clear()
 print(fruits) # 输出: []
```

### 1.4 列表的常用方法

```python
 numbers = [3, 1, 4, 1, 5, 9, 2, 6]
 # 排序
 numbers.sort()
 print(numbers) # 输出: [1, 1, 2, 3, 4, 5, 6, 9]
 # 反向排序
 numbers.sort(reverse=True)
 print(numbers) # 输出: [9, 6, 5, 4, 3, 2, 1, 1]
 # 反转列表
 numbers.reverse()
 print(numbers) # 输出: [1, 1, 2, 3, 4, 5, 6, 9]
 # 统计元素出现次数
 print(numbers.count(1)) # 输出: 2
 # 查找元素索引
 print(numbers.index(5)) # 输出: 5
 # 列表拼接
 list1 = [1, 2, 3]
 list2 = [4, 5, 6]
 combined = list1 + list2
 print(combined) # 输出: [1, 2, 3, 4, 5, 6]
 # 列表重复
 repeated = [1, 2] * 3
 print(repeated) # 输出: [1, 2, 1, 2, 1, 2]
```

### 1.5 列表的性能特点

- **实现**: 基于动态数组
- **访问**: O(1)（通过索引）
- **插入/删除**:
- 末尾: O(1)
- 中间: O(n)（需要移动元素）
- **查找**: O(n)（线性搜索）

## 2. 元组 (Tuple - `tuple`)

元组是一个有序、不可变的序列，允许存储重复元素。

### 2.1 元组的创建

```python
 # 创建元组
 empty_tuple = ()
 empty_tuple = tuple()
 # 创建带有初始元素的元组
 numbers = (1, 2, 3, 4, 5)
 fruits = ("apple", "banana", "cherry")
 mixed = (1, "apple", True, 3.14)
 # 注意: 单个元素的元组需要加逗号
 single_element = (1,)
 print(type(single_element)) # 输出: <class 'tuple'>
 # 不带括号的元组
 implicit_tuple = 1, 2, 3
 print(type(implicit_tuple)) # 输出: <class 'tuple'>
 # 从其他序列创建元组
 list_to_tuple = tuple([1, 2, 3])
 print(list_to_tuple) # 输出: (1, 2, 3)
 string_to_tuple = tuple("hello")
 print(string_to_tuple) # 输出: ('h', 'e', 'l', 'l', 'o')
```

### 2.2 元组的访问

```python
 fruits = ("apple", "banana", "cherry")
 # 通过索引访问元素
 print(fruits[0]) # 输出: apple
 print(fruits[1]) # 输出: banana
 print(fruits[-1]) # 输出: cherry
 # 切片操作
 print(fruits[1:3]) # 输出: ('banana', 'cherry')
 print(fruits[:2]) # 输出: ('apple', 'banana')
 print(fruits[1:]) # 输出: ('banana', 'cherry')
 print(fruits[::-1]) # 输出: ('cherry', 'banana', 'apple')
 # 检查元素是否存在
 print("apple" in fruits) # 输出:
 # 获取元组长度
 print(len(fruits)) # 输出: 3
 # 元组的不可变性
 # fruits[1] = "grape" # 错误: 'tuple' object does not support item assignment
```

### 2.3 元组的解包

```python
 # 基本解包
 coordinates = (10, 20, 30)
 x, y, z = coordinates
 print(x, y, z) # 输出: 10 20 30
 # 部分解包
 numbers = (1, 2, 3, 4, 5)
 first, *middle, last = numbers
 print(first) # 输出: 1
 print(middle) # 输出: [2, 3, 4]
 print(last) # 输出: 5
 # 交换变量
 a, b = 1, 2
 a, b = b, a
 print(a, b) # 输出: 2 1
 # 函数返回多个值
 def get_user():
  return "Alice", 30, "New York"
 name, age, city = get_user()
 print(name, age, city) # 输出: Alice 30 New York
```

### 2.4 元组的常用方法

```python
 numbers = (3, 1, 4, 1, 5, 9)
 # 统计元素出现次数
 print(numbers.count(1)) # 输出: 2
 # 查找元素索引
 print(numbers.index(5)) # 输出: 4
 # 元组拼接
 tuple1 = (1, 2, 3)
 tuple2 = (4, 5, 6)
 combined = tuple1 + tuple2
 print(combined) # 输出: (1, 2, 3, 4, 5, 6)
 # 元组重复
 repeated = (1, 2) * 3
 print(repeated) # 输出: (1, 2, 1, 2, 1, 2)
```

### 2.5 元组的应用场景

- **作为字典的键**（因为元组不可变）
- **函数返回多个值**
- **保护数据不被修改**
- **性能优化**（元组比列表更节省内存，访问速度更快）

## 3. 字典 (Dictionary - `dict`)

字典是一种映射类型，存储键值对，Python 3.7+ 保证插入顺序。

### 3.1 字典的创建

```python
 # 创建空字典
 empty_dict = {}
 empty_dict = dict()
 # 创建带有初始键值对的字典
 person = {"name": "Alice", "age": 30, "city": "New York"}
 # 使用dict()构造函数
 person = dict(name="Alice", age=30, city="New York")
 # 从键值对列表创建
 items = [("name", "Alice"), ("age", 30), ("city", "New York")]
 person = dict(items)
 # 从两个列表创建（键和值）
 keys = ["name", "age", "city"]
 values = ["Alice", 30, "New York"]
 person = dict(zip(keys, values))
 # 字典推导式
 squares = {x: x**2 for x in range(5)}
 print(squares) # 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 3.2 字典的访问

```python
 person = {"name": "Alice", "age": 30, "city": "New York"}
 # 通过键访问值
 print(person["name"]) # 输出: Alice
 print(person["age"]) # 输出: 30
 # 使用get()方法访问（更安全）
 print(person.get("name")) # 输出: Alice
 print(person.get("country", "Unknown")) # 输出: Unknown（键不存在时返回默认值）
 # 检查键是否存在
 print("name" in person) # 输出:
 print("country" in person) # 输出: False
 # 获取所有键
 print(person.keys()) # 输出: dict_keys(['name', 'age', 'city'])
 # 获取所有值
 print(person.values()) # 输出: dict_values(['Alice', 30, 'New York'])
 # 获取所有键值对
 print(person.items()) # 输出: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
```

### 3.3 字典的修改

```python
 person = {"name": "Alice", "age": 30, "city": "New York"}
 # 添加或修改键值对
 person["country"] = "USA" # 添加新键值对
 print(person) # 输出: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
 person["age"] = 31 # 修改现有值
 print(person) # 输出: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
 # 使用update()方法更新
 person.update({"city": "Boston", "job": "Engineer"})
 print(person) # 输出: {'name': 'Alice', 'age': 31, 'city': 'Boston', 'country': 'USA', 'job': 'Engineer'}
 # 删除键值对
 removed_value = person.pop("country") # 移除并返回值
 print(removed_value) # 输出: USA
 print(person) # 输出: {'name': 'Alice', 'age': 31, 'city': 'Boston', 'job': 'Engineer'}
 # 删除最后一个键值对（Python 3.7+）
 last_item = person.popitem()
 print(last_item) # 输出: ('job', 'Engineer')
 print(person) # 输出: {'name': 'Alice', 'age': 31, 'city': 'Boston'}
 # 清空字典
 person.clear()
 print(person) # 输出: {}
```

### 3.4 字典的遍历

```python
 person = {"name": "Alice", "age": 30, "city": "New York"}
 # 遍历键
 for key in person:
  print(key)
 # 遍历键（显式）
 for key in person.keys():
  print(key)
 # 遍历值
 for value in person.values():
  print(value)
 # 遍历键值对
 for key, value in person.items():
  print(f"{key}: {value}")
```

### 3.5 字典的性能特点

- **实现**: 基于哈希表
- **访问**: O(1)（平均情况）
- **插入/删除**: O(1)（平均情况）
- **查找**: O(1)（平均情况）
- **键的要求**: 必须是不可变类型（如字符串、数字、元组）

## 4. 集合 (Set - `set`)

集合是一个无序、不重复的元素集合。

### 4.1 集合的创建

```python
 # 创建空集合
 empty_set = set() # 注意: {} 创建的是空字典
 # 创建带有初始元素的集合
 numbers = {1, 2, 3, 4, 5}
 fruits = {"apple", "banana", "cherry"}
 # 从其他序列创建集合
 list_to_set = set([1, 2, 3, 3, 4, 5])
 print(list_to_set) # 输出: {1, 2, 3, 4, 5}（自动去重）
 string_to_set = set("hello")
 print(string_to_set) # 输出: {'h', 'e', 'l', 'o'}（自动去重）
 # 集合推导式
 squares = {x**2 for x in range(5)}
 print(squares) # 输出: {0, 1, 4, 9, 16}
```

### 4.2 集合的操作

```python
 fruits = {"apple", "banana", "cherry"}
 # 添加元素
 fruits.add("orange")
 print(fruits) # 输出: {'apple', 'banana', 'cherry', 'orange'}
 # 添加多个元素
 fruits.update(["mango", "kiwi"])
 print(fruits) # 输出: {'apple', 'banana', 'cherry', 'orange', 'mango', 'kiwi'}
 # 删除元素
 fruits.remove("cherry") # 如果元素不存在会抛出错误
 print(fruits) # 输出: {'apple', 'banana', 'orange', 'mango', 'kiwi'}
 fruits.discard("grape") # 如果元素不存在不会抛出错误
 print(fruits) # 输出: {'apple', 'banana', 'orange', 'mango', 'kiwi'}
 # 移除并返回任意元素
 popped = fruits.pop()
 print(popped) # 输出: 任意元素，如 'apple'
 print(fruits) # 输出: 剩余元素
 # 清空集合
 fruits.clear()
 print(fruits) # 输出: set()
```

### 4.3 集合运算

```python
 set1 = {1, 2, 3, 4, 5}
 set2 = {4, 5, 6, 7, 8}
 # 并集
 union = set1 | set2
 print(union) # 输出: {1, 2, 3, 4, 5, 6, 7, 8}
 print(set1.union(set2)) # 同上
 # 交集
 intersection = set1 & set2
 print(intersection) # 输出: {4, 5}
 print(set1.intersection(set2)) # 同上
 # 差集
 difference = set1 - set2
 print(difference) # 输出: {1, 2, 3}
 print(set1.difference(set2)) # 同上
 # 对称差集（并集减去交集）
 symmetric_difference = set1 ^ set2
 print(symmetric_difference) # 输出: {1, 2, 3, 6, 7, 8}
 print(set1.symmetric_difference(set2)) # 同上
 # 子集检查
 set3 = {1, 2, 3}
 print(set3.issubset(set1)) # 输出:
 # 超集检查
 print(set1.issuperset(set3)) # 输出:
 # 不相交检查
 set4 = {6, 7, 8}
 print(set1.isdisjoint(set4)) # 输出:
```

### 4.4 集合的性能特点

- **实现**: 基于哈希表
- **查找**: O(1)（平均情况）
- **插入/删除**: O(1)（平均情况）
- **元素要求**: 必须是不可变类型

## 5. 数据结构对比

| 类型    | 有序  | 可变 | 重复     | 性能 (查找) | 适用场景                             |
| ------- | ----- | ---- | -------- | ----------- | ------------------------------------ |
| `list`  | Yes   | Yes  | Yes      | $O(n)$      | 需要有序且可能修改的数据             |
| `tuple` | Yes   | No   | Yes      | $O(n)$      | 需要有序且不可修改的数据，作为字典键 |
| `dict`  | Yes\* | Yes  | No (Key) | $O(1)$      | 需要键值对映射，快速查找             |
| `set`   | No    | Yes  | No       | $O(1)$      | 需要去重，集合运算                   |

- Python 3.7+ 保证字典的插入顺序

## 6. 数据结构的最佳实践

### 6.1 列表的最佳实践

- **使用列表推导式**：简洁高效地创建列表
- **避免频繁在列表开头插入**：这会导致 O(n) 的时间复杂度
- **使用 `append()` 而不是 `+`**：`append()` 是 O(1)，而 `+` 是 O(n)
- **使用 `in` 检查元素**：虽然是 O(n)，但对于小列表是可接受的
- **排序前考虑是否需要**：排序是 O(n log n) 操作

### 6.2 元组的最佳实践

- **使用元组存储相关数据**：如坐标、日期等
- **作为函数返回值**：方便多值返回
- **作为字典键**：因为元组不可变
- **使用拆包简化代码**：提高可读性
- **注意单元素元组的语法**：需要加逗号 `(1,)`

### 6.3 字典的最佳实践

- **使用 `get()` 方法**：避免键不存在的错误
- **使用字典推导式**：简洁高效地创建字典
- **遍历键值对使用 `items()`**：比分别遍历键和值更高效
- **使用 `defaultdict`**：处理不存在的键（来自 `collections` 模块）
- **使用 `OrderedDict`**：需要保持插入顺序的旧版本 Python（3.7+ 已不需要）

### 6.4 集合的最佳实践

- **用于去重**：快速去除重复元素
- **用于集合运算**：交集、并集、差集等
- **用于快速成员检查**：比列表的 `in` 操作更快
- **注意集合是无序的**：不要依赖元素顺序
- **元素必须是不可变的**：不能包含列表、字典等可变类型

### 6.5 性能考虑

- **小数据集**：选择最符合语义的数据结构
- **大数据集**：考虑查找、插入、删除的性能
- **内存使用**：元组比列表更节省内存
- **操作频率**：根据最频繁的操作选择合适的数据结构

## 7. 高级数据结构

Python 标准库中还提供了一些高级数据结构：

### 7.1 有序字典 (`OrderedDict`)

```python
 from collections import OrderedDict
 # 在 Python 3.7+ 中，普通字典已经保持插入顺序
 # 但 OrderedDict 提供了额外的方法
 od = OrderedDict()
 od['a'] = 1
 od['b'] = 2
 od['c'] = 3
 print(list(od.keys())) # 输出: ['a', 'b', 'c']
 # 移动元素到末尾
 od.move_to_end('a')
 print(list(od.keys())) # 输出: ['b', 'c', 'a']
```

### 7.2 默认字典 (`defaultdict`)

```python
 from collections import defaultdict
 # 自动为不存在的键提供默认值
 d = defaultdict(int) # 默认值为 0
 d['a'] += 1
 d['b'] += 1
 print(d) # 输出: defaultdict(<class 'int'>, {'a': 1, 'b': 1})
 # 使用列表作为默认值
 d = defaultdict(list)
 d['a'].append(1)
 d['a'].append(2)
 d['b'].append(3)
 print(d) # 输出: defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})
```

### 7.3 计数器 (`Counter`)

```python
 from collections import Counter
 # 统计元素出现次数
 c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
 print(c) # 输出: Counter({'a': 3, 'b': 2, 'c': 1})
 # 访问次数
 print(c['a']) # 输出: 3
 # 获取最常见的元素
 print(c.most_common(2)) # 输出: [('a', 3), ('b', 2)]
```

### 7.4 双端队列 (`deque`)

```python
 from collections import deque
 # 双端队列，支持高效的两端操作
 dq = deque([1, 2, 3])
 # 从右侧添加
 dq.append(4)
 print(dq) # 输出: deque([1, 2, 3, 4])
 # 从左侧添加
 dq.appendleft(0)
 print(dq) # 输出: deque([0, 1, 2, 3, 4])
 # 从右侧移除
 print(dq.pop()) # 输出: 4
 print(dq) # 输出: deque([0, 1, 2, 3])
 # 从左侧移除
 print(dq.popleft()) # 输出: 0
 print(dq) # 输出: deque([1, 2, 3])
```

---

## 延伸阅读

- [Pandas](data-analysis/pandas)
## 列表

**基本写法：创建列表**
`[<元素1>, <元素2>, <元素3>]`

```python
# 创建列表
fruits = ["apple", "banana", "cherry"]
```

---

**基本写法：创建空列表**
`[]`

```python
# 创建空列表
empty_list = []
```

---

**基本写法：使用 list() 创建列表**
`list(<可迭代对象>)`

```python
# 使用 list() 创建列表
numbers = list(range(5))
```

---

**基本写法：访问列表元素**
`<列表>[<索引>]`

```python
# 访问列表元素
print(fruits[0])
```

---

**基本写法：负索引访问**
`<列表>[-<索引>]`

```python
# 使用负索引访问（从末尾开始）
print(fruits[-1])
```

---

**基本写法：列表切片**
`<列表>[<start>:<stop>:<step>]`

```python
# 列表切片
print(fruits[0:2])
```

---

**基本写法：修改列表元素**
`<列表>[<索引>] = <新值>`

```python
# 修改列表元素
fruits[0] = "orange"
```

---

## 列表方法

**基本写法：追加元素**
`<列表>.append(<元素>)`

```python
# 追加元素到列表末尾
fruits.append("grape")
```

---

**基本写法：插入元素**
`<列表>.insert(<索引>, <元素>)`

```python
# 在指定位置插入元素
fruits.insert(1, "kiwi")
```

---

**基本写法：扩展列表**
`<列表>.extend(<可迭代对象>)`

```python
# 使用另一个列表扩展当前列表
fruits.extend(["mango", "pear"])
```

---

**基本写法：删除指定元素**
`<列表>.remove(<元素>)`

```python
# 删除列表中第一个匹配的元素
fruits.remove("banana")
```

---

**基本写法：弹出元素**
`<列表>.pop([<索引>])`

```python
# 弹出指定位置的元素（默认末尾）
last = fruits.pop()
```

---

**基本写法：清空列表**
`<列表>.clear()`

```python
# 清空列表
fruits.clear()
```

---

**基本写法：查找元素索引**
`<列表>.index(<元素>)`

```python
# 查找元素的索引位置
index = fruits.index("cherry")
```

---

**基本写法：统计元素出现次数**
`<列表>.count(<元素>)`

```python
# 统计元素出现次数
count = fruits.count("apple")
```

---

**基本写法：排序列表**
`<列表>.sort()`

```python
# 原地排序列表
fruits.sort()
```

---

**基本写法：指定排序规则**
`<列表>.sort(key=<函数>, reverse=<布尔值>)`

```python
# 按字符串长度排序
fruits.sort(key=len, reverse=True)
```

---

**基本写法：反转列表**
`<列表>.reverse()`

```python
# 原地反转列表
fruits.reverse()
```

---

**基本写法：复制列表**
`<列表>.copy()`

```python
# 复制列表
fruits_copy = fruits.copy()
```

---

## 元组

**基本写法：创建元组**
`(<元素1>, <元素2>, <元素3>)`

```python
# 创建元组
point = (3, 4)
```

---

**基本写法：创建单元素元组**
`(<元素>,)`

```python
# 创建单元素元组（注意逗号）
single = (42,)
```

---

**基本写法：创建空元组**
`()`

```python
# 创建空元组
empty_tuple = ()
```

---

**基本写法：使用 tuple() 创建元组**
`tuple(<可迭代对象>)`

```python
# 使用 tuple() 创建元组
numbers = tuple([1, 2, 3])
```

---

**基本写法：访问元组元素**
`<元组>[<索引>]`

```python
# 访问元组元素
print(point[0])
```

---

**基本写法：元组解包**
`<变量1>, <变量2> = <元组>`

```python
# 元组解包
x, y = point
```

---

**基本写法：使用星号解包**
`<变量1>, *<变量2> = <元组>`

```python
# 使用星号收集剩余值
first, *rest = (1, 2, 3, 4, 5)
```

---

**基本写法：命名元组**
`namedtuple(<类名>, [<字段1>, <字段2>])`

```python
# 创建命名元组
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)
```

---

## 字典

**基本写法：创建字典**
`{<键1>: <值1>, <键2>: <值2>}`

```python
# 创建字典
person = {"name": "Alice", "age": 30}
```

---

**基本写法：创建空字典**
`{}`

```python
# 创建空字典
empty_dict = {}
```

---

**基本写法：使用 dict() 创建字典**
`dict(<键1>=<值1>, <键2>=<值2>)`

```python
# 使用 dict() 创建字典
person = dict(name="Alice", age=30)
```

---

**基本写法：使用键值对序列创建字典**
`dict([(<键>, <值>), (<键>, <值>)])`

```python
# 使用键值对序列创建字典
person = dict([("name", "Alice"), ("age", 30)])
```

---

**基本写法：访问字典值**
`<字典>[<键>]`

```python
# 通过键访问值
print(person["name"])
```

---

**基本写法：使用 get() 安全访问**
`<字典>.get(<键>, <默认值>)`

```python
# 使用 get() 安全访问，键不存在时返回默认值
print(person.get("email", "N/A"))
```

---

**基本写法：修改或添加键值对**
`<字典>[<键>] = <值>`

```python
# 修改或添加键值对
person["email"] = "alice@example.com"
```

---

**基本写法：删除键值对**
`del <字典>[<键>]`

```python
# 删除指定键值对
del person["age"]
```

---

## 字典方法

**基本写法：获取所有键**
`<字典>.keys()`

```python
# 获取字典的所有键
print(person.keys())
```

---

**基本写法：获取所有值**
`<字典>.values()`

```python
# 获取字典的所有值
print(person.values())
```

---

**基本写法：获取所有键值对**
`<字典>.items()`

```python
# 获取字典的所有键值对
print(person.items())
```

---

**基本写法：弹出键值对**
`<字典>.pop(<键>, <默认值>)`

```python
# 弹出指定键的值
age = person.pop("age", None)
```

---

**基本写法：弹出最后一个键值对**
`<字典>.popitem()`

```python
# 弹出最后一个键值对
key, value = person.popitem()
```

---

**基本写法：更新字典**
`<字典>.update(<其他字典>)`

```python
# 使用另一个字典更新当前字典
person.update({"age": 31, "city": "New York"})
```

---

**基本写法：设置默认值**
`<字典>.setdefault(<键>, <默认值>)`

```python
# 设置键的默认值（键不存在时设置）
person.setdefault("country", "USA")
```

---

**基本写法：清空字典**
`<字典>.clear()`

```python
# 清空字典
person.clear()
```

---

**基本写法：复制字典**
`<字典>.copy()`

```python
# 复制字典
person_copy = person.copy()
```

---

## 字典推导式

**基本写法：基本字典推导式**
`{<键表达式>: <值表达式> for <变量> in <可迭代对象>}`

```python
# 基本字典推导式
squares = {x: x ** 2 for x in range(5)}
```

---

**基本写法：带条件的字典推导式**
`{<键表达式>: <值表达式> for <变量> in <可迭代对象> if <条件>}`

```python
# 带条件的字典推导式
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
```

---

## 集合

**基本写法：创建集合**
`{<元素1>, <元素2>, <元素3>}`

```python
# 创建集合
fruits = {"apple", "banana", "cherry"}
```

---

**基本写法：创建空集合**
`set()`

```python
# 创建空集合（注意：{} 创建的是空字典）
empty_set = set()
```

---

**基本写法：使用 set() 创建集合**
`set(<可迭代对象>)`

```python
# 使用 set() 从列表创建集合
numbers = set([1, 2, 3, 2, 1])
```

---

## 集合方法

**基本写法：添加元素**
`<集合>.add(<元素>)`

```python
# 添加元素到集合
fruits.add("orange")
```

---

**基本写法：删除元素**
`<集合>.remove(<元素>)`

```python
# 删除元素（元素不存在时抛出异常）
fruits.remove("banana")
```

---

**基本写法：安全删除元素**
`<集合>.discard(<元素>)`

```python
# 安全删除元素（元素不存在时不抛出异常）
fruits.discard("banana")
```

---

**基本写法：弹出元素**
`<集合>.pop()`

```python
# 弹出集合中的任意元素
element = fruits.pop()
```

---

**基本写法：清空集合**
`<集合>.clear()`

```python
# 清空集合
fruits.clear()
```

---

## 集合运算

**基本写法：并集运算**
`<集合1> | <集合2>`

```python
# 集合并集
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2
```

---

**基本写法：交集运算**
`<集合1> & <集合2>`

```python
# 集合交集
intersection = set1 & set2
```

---

**基本写法：差集运算**
`<集合1> - <集合2>`

```python
# 集合差集
difference = set1 - set2
```

---

**基本写法：对称差集运算**
`<集合1> ^ <集合2>`

```python
# 集合对称差集
symmetric_diff = set1 ^ set2
```

---

**基本写法：使用 union() 方法**
`<集合>.union(<其他集合>)`

```python
# 使用 union() 方法求并集
union = set1.union(set2)
```

---

**基本写法：使用 intersection() 方法**
`<集合>.intersection(<其他集合>)`

```python
# 使用 intersection() 方法求交集
intersection = set1.intersection(set2)
```

---

**基本写法：使用 difference() 方法**
`<集合>.difference(<其他集合>)`

```python
# 使用 difference() 方法求差集
difference = set1.difference(set2)
```

---

**基本写法：子集判断**
`<集合1>.issubset(<集合2>)`

```python
# 判断是否为子集
is_subset = {1, 2}.issubset({1, 2, 3})
```

---

**基本写法：超集判断**
`<集合1>.issuperset(<集合2>)`

```python
# 判断是否为超集
is_superset = {1, 2, 3}.issuperset({1, 2})
```

---

**基本写法：不相交判断**
`<集合1>.isdisjoint(<集合2>)`

```python
# 判断两个集合是否不相交
is_disjoint = {1, 2}.isdisjoint({3, 4})
```

---

## 集合推导式

**基本写法：基本集合推导式**
`{<表达式> for <变量> in <可迭代对象>}`

```python
# 基本集合推导式
squares = {x ** 2 for x in range(5)}
```

---

**基本写法：带条件的集合推导式**
`{<表达式> for <变量> in <可迭代对象> if <条件>}`

```python
# 带条件的集合推导式
even_squares = {x ** 2 for x in range(10) if x % 2 == 0}
```

---

## collections 模块

**基本写法：使用 Counter 计数**
`Counter(<可迭代对象>)`

```python
# 使用 Counter 统计元素出现次数
from collections import Counter
word_count = Counter("hello world")
```

---

**基本写法：使用 defaultdict**
`defaultdict(<默认工厂>)`

```python
# 使用 defaultdict 设置默认值
from collections import defaultdict
word_list = defaultdict(list)
word_list["fruits"].append("apple")
```

---

**基本写法：使用 OrderedDict**
`OrderedDict([(<键>, <值>), (<键>, <值>)])`

```python
# 使用 OrderedDict 保持插入顺序
from collections import OrderedDict
ordered = OrderedDict([("a", 1), ("b", 2)])
```

---

**基本写法：使用 deque 双端队列**
`deque(<可迭代对象>)`

```python
# 使用 deque 创建双端队列
from collections import deque
queue = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)
```

---

**基本写法：deque 弹出左侧元素**
`<deque>.popleft()`

```python
# 从左侧弹出元素
first = queue.popleft()
```

---

## 冻结集合

**基本写法：创建冻结集合**
`frozenset(<可迭代对象>)`

```python
# 创建不可变的冻结集合
frozen = frozenset([1, 2, 3])
```

---

## 数据结构嵌套

**换行写法：嵌套字典列表**
`[`
`    {<键1>: <值1>, <键2>: <值2>},`
`    {<键1>: <值1>, <键2>: <值2>},`
`]`

```python
# 嵌套字典列表
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
]
```

---

**换行写法：嵌套字典字典**
`{`
`    <键1>: {<子键1>: <值1>},`
`    <键2>: {<子键2>: <值2>},`
`}`

```python
# 嵌套字典字典
matrix = {
    "row1": {"col1": 1, "col2": 2},
    "row2": {"col1": 3, "col2": 4},
}
```

---

## 参考文献

Python 官方文档：https://docs.python.org/zh-cn/3/
PEP 8 样式指南：https://peps.python.org/pep-0008/
Python 之禅（PEP 20）：https://peps.python.org/pep-0020/
Python 类型注解指南（PEP 484）：https://peps.python.org/pep-0484/
Python 打包用户指南：https://packaging.python.org/
Real Python 教程站：https://realpython.com/

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
| 控制流 | 018-ControlFlow | 本文的并列主题 |
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
| 内置数据结构 | 037-BuiltinDataStructure | 本文自身 |
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
