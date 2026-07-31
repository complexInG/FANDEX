# Pandas Series

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Series

**基本写法：创建 Series 对象**
`pd.Series(<数据>[, index=<索引>][, name=<名称>])`

```python
# 从列表、字典、数组创建 Series
import pandas as pd

s = pd.Series([1, 2, 3, 4])
s = pd.Series([1, 2, 3], index=["a", "b", "c"])
s = pd.Series({"a": 1, "b": 2, "c": 3})
s = pd.Series([1, 2, 3], name="values")
```

---

## 访问元素

**基本写法：通过标签或位置访问**
`<series>[<标签>]` | `<series>.loc[<标签>]` | `<series>.iloc[<位置>]`

```python
# Series 元素访问
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s["a"])        # 10
print(s.loc["b"])    # 20
print(s.iloc[0])     # 10
print(s[["a", "c"]]) # 多个标签
```

---

## 切片

**基本写法：Series 切片**
`<series>[<start>:<stop>]`
`<series>.loc[<start>:<stop>]`

```python
# Series 切片
s = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(s[1:3])        # 位置切片，不含 3
print(s.loc["a":"c"])  # 标签切片，包含 c
```

---

## 布尔索引

**基本写法：条件筛选**
`<series>[<布尔条件>]`

```python
# 布尔条件筛选
s = pd.Series([1, 2, 3, 4, 5])
print(s[s > 2])              # 3, 4, 5
print(s[(s > 1) & (s < 5)]) # 2, 3, 4
print(s[s.isin([2, 4])])    # 2, 4
```

---

## 基本属性

**基本写法：访问 Series 属性**
`<series>.index` | `<series>.values` | `<series>.dtype` | `<series>.name`

```python
# Series 基本属性
s = pd.Series([1, 2, 3], index=["a", "b", "c"], name="nums")
print(s.index)   # Index(['a', 'b', 'c'])
print(s.values)  # [1 2 3]
print(s.dtype)   # int64
print(s.name)    # nums
print(s.shape)   # (3,)
```

---

## 统计方法

**基本写法：Series 统计**
`<series>.<方法>()`

```python
# Series 常用统计方法
s = pd.Series([1, 2, 3, 4, 5])
print(s.sum())     # 15
print(s.mean())    # 3.0
print(s.median())  # 3.0
print(s.std())     # 标准差
print(s.min())     # 1
print(s.max())     # 5
print(s.count())   # 5
print(s.describe())  # 汇总统计
```

---

## 唯一值与计数

**基本写法：唯一值与值计数**
`<series>.unique()`
`<series>.value_counts()`

```python
# 唯一值与值计数
s = pd.Series(["a", "b", "a", "c", "b", "a"])
print(s.unique())           # ['a', 'b', 'c']
print(s.value_counts())     # a:3, b:2, c:1
print(s.nunique())          # 3
```

---

## 缺失值处理

**基本写法：处理缺失值**
`<series>.isna()` | `<series>.fillna(<值>)` | `<series>.dropna()`

```python
# Series 缺失值处理
s = pd.Series([1, None, 3, np.nan, 5])
print(s.isna())            # [False, True, False, True, False]
print(s.fillna(0))         # 用 0 填充
print(s.dropna())          # 删除缺失值
print(s.fillna(s.mean()))  # 用均值填充
```

---

## apply 应用函数

**基本写法：应用自定义函数**
`<series>.apply(<函数>)`

```python
# Series 应用函数
s = pd.Series([1, 2, 3, 4])
print(s.apply(lambda x: x ** 2))      # 平方
print(s.apply(lambda x: f"值:{x}"))    # 转字符串
print(s.map({1: "一", 2: "二"}))       # 字典映射
```

---

## 排序

**基本写法：Series 排序**
`<series>.sort_values([ascending=<布尔>])`
`<series>.sort_index()`

```python
# Series 排序
s = pd.Series([3, 1, 4, 1, 5], index=["b", "a", "d", "c", "e"])
print(s.sort_values())              # 按值升序
print(s.sort_values(ascending=False))  # 降序
print(s.sort_index())               # 按索引排序
```

---

## 字符串方法

**基本写法：Series 字符串操作**
`<series>.str.<方法>()`

```python
# Series 字符串向量化操作
s = pd.Series(["Hello", "World", "Python"])
print(s.str.lower())          # 小写
print(s.str.upper())          # 大写
print(s.str.len())            # 长度
print(s.str.contains("o"))    # 是否包含
print(s.str.replace("o", "0"))  # 替换
```

---

## 类型转换

**基本写法：转换 Series 类型**
`<series>.astype(<类型>)`

```python
# Series 类型转换
s = pd.Series(["1", "2", "3"])
print(s.astype(int))
print(s.astype(float))
s_date = pd.Series(["2024-01-01"]).astype("datetime64[ns]")
```

---

## 运算

**基本写法：Series 算术运算**
`<series> <op> <series或标量>`

```python
# Series 算术运算与对齐
s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s1 + s2)   # 按索引对齐相加
print(s1 * 2)
print(s1.add(s2, fill_value=0))  # 填充后相加
```

---

## 重索引

**基本写法：重新索引 Series**
`<series>.reindex(<新索引>)`

```python
# Series 重新索引
s = pd.Series([1, 2, 3], index=["a", "b", "c"])
new_s = s.reindex(["a", "b", "c", "d"], fill_value=0)
print(new_s)
```
