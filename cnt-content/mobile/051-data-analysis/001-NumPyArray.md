# NumPy 数组创建

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## np.array 创建数组

**基本写法：从列表创建数组**
`np.array(<列表>[, dtype=<类型>])`

```python
# 从列表创建 NumPy 数组
import numpy as np

arr = np.array([1, 2, 3])
arr = np.array([1, 2, 3], dtype=np.float64)
matrix = np.array([[1, 2], [3, 4]])
```

---

## np.zeros 创建零数组

**基本写法：创建全零数组**
`np.zeros(<形状>[, dtype=<类型>])`

```python
# 创建全零数组
zeros_1d = np.zeros(5)
zeros_2d = np.zeros((3, 4))
zeros_int = np.zeros((2, 2), dtype=np.int32)
```

---

## np.ones 创建全一数组

**基本写法：创建全一数组**
`np.ones(<形状>[, dtype=<类型>])`

```python
# 创建全一数组
ones_1d = np.ones(5)
ones_2d = np.ones((3, 4))
ones_float = np.ones((2, 2), dtype=np.float32)
```

---

## np.full 创建指定值数组

**基本写法：创建填充指定值的数组**
`np.full(<形状>, <值>[, dtype=<类型>])`

```python
# 创建填充指定值的数组
arr = np.full((3, 3), 7)
arr = np.full((2, 2), np.nan)
```

---

## np.eye 单位矩阵

**基本写法：创建单位矩阵**
`np.eye(<n>[, M=<列数>][, k=<对角偏移>][, dtype=<类型>])`

```python
# 创建单位矩阵
identity = np.eye(3)
rectangular = np.eye(3, 4)
offset = np.eye(3, k=1)
```

---

## np.arange 范围数组

**基本写法：创建等差数列数组**
`np.arange([<start>,] <stop>[, <step>][, dtype=<类型>])`

```python
# 创建等差数列数组
arr = np.arange(10)
arr = np.arange(1, 10)
arr = np.arange(0, 10, 2)
arr = np.arange(0, 1, 0.1)
```

---

## np.linspace 等间隔数组

**基本写法：创建线性等分数组**
`np.linspace(<start>, <stop>[, num=<个数>][, endpoint=<布尔>])`

```python
# 创建线性等间隔数组
arr = np.linspace(0, 10, num=5)
arr = np.linspace(0, 1, num=11, endpoint=True)
arr = np.linspace(0, 10, num=5, endpoint=False)
```

---

## np.logspace 对数等分

**基本写法：创建对数等间隔数组**
`np.logspace(<start>, <stop>[, num=<个数>][, base=<底数>])`

```python
# 创建对数等间隔数组
arr = np.logspace(0, 2, num=3)  # 10^0, 10^1, 10^2
arr = np.logspace(0, 3, num=4, base=2)
```

---

## np.random 随机数组

**基本写法：创建随机数组**
`np.random.rand(<形状>)`
`np.random.randn(<形状>)`
`np.random.randint(<low>, <high>, <形状>)`

```python
# 创建随机数组
uniform = np.random.rand(3, 3)              # [0,1) 均匀分布
normal = np.random.randn(3, 3)              # 标准正态分布
integers = np.random.randint(0, 10, size=5)  # [0,10) 随机整数
```

---

## Generator 新式随机

**基本写法：使用新式随机生成器**
`rng = np.random.default_rng(<seed>)`
`rng.<方法>(<参数>)`

```python
# NumPy 2.x 推荐使用新式随机生成器
rng = np.random.default_rng(42)
arr = rng.random((3, 3))
arr = rng.standard_normal((3, 3))
arr = rng.integers(0, 10, size=5)
```

---

## np.empty 未初始化数组

**基本写法：创建未初始化数组**
`np.empty(<形状>[, dtype=<类型>])`

```python
# 创建未初始化数组（值随机，性能最佳）
arr = np.empty((3, 3))
arr = np.empty_like(existing_array)
```

---

## 数组属性

**基本写法：访问数组属性**
`<arr>.shape` | `<arr>.ndim` | `<arr>.size` | `<arr>.dtype`

```python
# 访问数组基本属性
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)   # (2, 3)
print(arr.ndim)    # 2
print(arr.size)    # 6
print(arr.dtype)   # int64
```

---

## np.reshape 形状变换

**基本写法：改变数组形状**
`<arr>.reshape(<形状>)`
`np.reshape(<arr>, <形状>)`

```python
# 改变数组形状
arr = np.arange(12)
matrix = arr.reshape(3, 4)
row_vector = arr.reshape(1, -1)
col_vector = arr.reshape(-1, 1)
```

---

## np.copy 复制数组

**基本写法：复制数组**
`<arr>.copy()`
`np.copy(<arr>)`

```python
# 深拷贝数组
arr = np.array([1, 2, 3])
copy_arr = arr.copy()
copy_arr[0] = 99
print(arr[0])  # 1，原数组不变
```

---

## astype 类型转换

**基本写法：转换数组数据类型**
`<arr>.astype(<新类型>)`

```python
# 转换数组数据类型
arr = np.array([1.5, 2.7, 3.2])
int_arr = arr.astype(np.int32)  # 截断小数部分
str_arr = arr.astype(str)
```
