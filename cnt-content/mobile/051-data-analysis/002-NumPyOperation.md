# NumPy 数组操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 索引访问

**基本写法：访问数组元素**
`<arr>[<索引>]`
`<arr>[<行>, <列>]`

```python
# 一维与多维数组索引
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])      # 1
print(arr[-1])     # 5

matrix = np.array([[1, 2], [3, 4]])
print(matrix[0, 1])  # 2
```

---

## 切片操作

**基本写法：数组切片**
`<arr>[<start>:<stop>:<step>]`

```python
# 一维与二维数组切片
arr = np.arange(10)
print(arr[2:5])     # [2, 3, 4]
print(arr[:5])      # [0, 1, 2, 3, 4]
print(arr[::2])     # [0, 2, 4, 6, 8]

matrix = np.arange(12).reshape(3, 4)
print(matrix[0:2, 1:3])
```

---

## 花式索引

**基本写法：使用索引数组访问**
`<arr>[<索引数组>]`

```python
# 使用索引数组访问多个元素
arr = np.arange(10)
print(arr[[1, 3, 5]])  # [1, 3, 5]

matrix = np.arange(12).reshape(3, 4)
print(matrix[[0, 2]])  # 第 0 行与第 2 行
```

---

## 布尔索引

**基本写法：使用布尔数组筛选**
`<arr>[<布尔数组>]`

```python
# 布尔条件筛选
arr = np.arange(10)
print(arr[arr > 5])           # [6, 7, 8, 9]
print(arr[(arr > 2) & (arr < 7)])  # [3, 4, 5, 6]
print(arr[arr % 2 == 0])      # [0, 2, 4, 6, 8]
```

---

## np.where 条件筛选

**基本写法：条件返回索引或值**
`np.where(<条件>[, <x>, <y>])`

```python
# 条件筛选索引或值
arr = np.arange(10)
indices = np.where(arr > 5)        # 返回索引
result = np.where(arr > 5, arr, 0) # 满足取 arr，否则取 0
```

---

## 数学运算

**基本写法：数组数学运算**
`<arr> + <n>` | `<arr> * <n>` | `np.add(<a>, <b>)`

```python
# 数组与标量、数组与数组运算
arr = np.array([1, 2, 3])
print(arr + 10)         # [11, 12, 13]
print(arr * 2)          # [2, 4, 6]
print(np.add(arr, arr)) # [2, 4, 6]
```

---

## 统计函数

**基本写法：数组统计**
`<arr>.<方法>([axis=<轴>])`

```python
# 数组统计方法
arr = np.array([[1, 2], [3, 4]])
print(arr.sum())          # 10
print(arr.sum(axis=0))    # [4, 6] 按列求和
print(arr.mean())         # 2.5
print(arr.max())          # 4
print(arr.min())          # 1
print(arr.std())          # 标准差
```

---

## 矩阵运算

**基本写法：矩阵乘法与转置**
`<arr>.dot(<arr>)` | `<arr>.T` | `np.matmul(<a>, <b>)`

```python
# 矩阵乘法与转置
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = a.dot(b)        # 矩阵乘法
result = np.matmul(a, b) # 等价写法
transposed = a.T         # 转置
```

---

## np.concatenate 拼接

**基本写法：拼接数组**
`np.concatenate(<数组列表>[, axis=<轴>])`

```python
# 沿指定轴拼接数组
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate([a, b]))  # [1, 2, 3, 4]

m1 = np.array([[1, 2]])
m2 = np.array([[3, 4]])
print(np.vstack([m1, m2]))  # 垂直堆叠
print(np.hstack([m1, m2]))  # 水平堆叠
```

---

## np.split 分割

**基本写法：分割数组**
`np.split(<arr>, <份数>[, axis=<轴>])`
`np.hsplit(<arr>, <份数>)` | `np.vsplit(<arr>, <份数>)`

```python
# 分割数组
arr = np.arange(12)
parts = np.split(arr, 3)
print(parts)  # [array([0,1,2,3]), array([4,5,6,7]), array([8,9,10,11])]

matrix = np.arange(12).reshape(3, 4)
left, right = np.hsplit(matrix, 2)
```

---

## np.sort 排序

**基本写法：排序数组**
`np.sort(<arr>[, axis=<轴>])`
`<arr>.sort([axis=<轴>])`

```python
# 排序数组
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
sorted_arr = np.sort(arr)  # 返回新数组
arr.sort()                 # 原地排序
indices = np.argsort(arr)  # 返回排序后索引
```

---

## np.unique 唯一值

**基本写法：获取唯一值**
`np.unique(<arr>[, return_counts=<布尔>])`

```python
# 获取数组唯一值
arr = np.array([1, 2, 2, 3, 3, 3])
print(np.unique(arr))                              # [1, 2, 3]
values, counts = np.unique(arr, return_counts=True)
print(counts)  # [1, 2, 3]
```

---

## 广播机制

**基本写法：不同形状数组运算**
`<arr> <op> <不同形状arr>` (自动广播)

```python
# 广播机制自动扩展数组形状
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print(matrix + row)  # 每行加 row

col = np.array([[100], [200]])
print(matrix + col)  # 每列加 col
```

---

## np.apply_along_axis

**基本写法：沿轴应用函数**
`np.apply_along_axis(<函数>, <轴>, <arr>)`

```python
# 沿指定轴应用自定义函数
arr = np.array([[1, 2, 3], [4, 5, 6]])
result = np.apply_along_axis(np.sum, axis=1, arr=arr)
print(result)  # [6, 15]
```

---

## 线性代数

**基本写法：线性代数函数**
`np.linalg.<方法>(<arr>)`

```python
# NumPy 线性代数
import numpy as np

a = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(a))     # 逆矩阵
print(np.linalg.det(a))     # 行列式
eigvals, eigvecs = np.linalg.eig(a)  # 特征值与特征向量
```
