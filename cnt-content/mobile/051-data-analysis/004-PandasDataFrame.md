# Pandas DataFrame

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 DataFrame

**基本写法：创建 DataFrame**
`pd.DataFrame(<数据>[, index=<索引>][, columns=<列>])`

```python
# 从字典、列表、数组创建 DataFrame
import pandas as pd

df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4}])
```

---

## 访问列

**基本写法：访问 DataFrame 列**
`<df>[<列名>]` | `<df>.<列名>` | `<df>[[<列1>, <列2>]]`

```python
# 访问 DataFrame 列
df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
print(df["name"])
print(df.name)
print(df[["name", "age"]])
```

---

## loc 标签访问

**基本写法：按标签访问行与列**
`<df>.loc[<行标签>, <列标签>]`

```python
# loc 按标签访问
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]}, index=["x", "y"])
print(df.loc["x"])            # 访问行
print(df.loc["x", "a"])       # 访问元素
print(df.loc[:, "a"])         # 所有行单列
print(df.loc[df["a"] > 1])    # 布尔条件
```

---

## iloc 位置访问

**基本写法：按位置访问行与列**
`<df>.iloc[<行位置>, <列位置>]`

```python
# iloc 按整数位置访问
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(df.iloc[0])        # 第一行
print(df.iloc[0, 1])     # 第一行第二列
print(df.iloc[0:2])      # 前两行
print(df.iloc[:, 0])     # 所有行第一列
```

---

## 添加列

**基本写法：添加新列**
`<df>[<新列名>] = <值或Series>`

```python
# 添加新列
df = pd.DataFrame({"a": [1, 2, 3]})
df["b"] = [4, 5, 6]
df["c"] = 10               # 广播标量
df["sum"] = df["a"] + df["b"]
df["label"] = df["a"].apply(lambda x: "大" if x > 1 else "小")
```

---

## 删除列与行

**基本写法：删除行或列**
`<df>.drop(<标签>[, axis=<轴>][, inplace=<布尔>])`

```python
# 删除行或列
df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
df_new = df.drop("c", axis=1)     # 删除列
df_new = df.drop(columns=["c"])   # 删除列
df_new = df.drop(0)               # 删除行
df.drop("c", axis=1, inplace=True)  # 原地删除
```

---

## 筛选行

**基本写法：按条件筛选行**
`<df>[<布尔条件>]`
`<df>.query("<表达式>")`

```python
# 按条件筛选行
df = pd.DataFrame({"name": ["A", "B", "C"], "age": [30, 25, 35]})
print(df[df["age"] > 25])
print(df[(df["age"] > 20) & (df["age"] < 35)])
print(df.query("age > 25"))
print(df.query("age > 20 and age < 35"))
```

---

## 排序

**基本写法：DataFrame 排序**
`<df>.sort_values(<列>[, ascending=<布尔>])`
`<df>.sort_index()`

```python
# DataFrame 排序
df = pd.DataFrame({"a": [3, 1, 2], "b": [6, 4, 5]})
print(df.sort_values("a"))                  # 按 a 升序
print(df.sort_values("a", ascending=False)) # 降序
print(df.sort_values(["a", "b"]))           # 多列排序
print(df.sort_index(ascending=False))       # 按索引排序
```

---

## 基本属性

**基本写法：访问 DataFrame 属性**
`<df>.shape` | `<df>.columns` | `<df>.index` | `<df>.dtypes`

```python
# DataFrame 基本属性
df = pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})
print(df.shape)    # (2, 2)
print(df.columns)  # Index(['a', 'b'])
print(df.index)    # RangeIndex(0, 2)
print(df.dtypes)   # a:int64, b:object
print(df.size)     # 4
```

---

## info 与 describe

**基本写法：查看 DataFrame 概况**
`<df>.info()`
`<df>.describe()`

```python
# DataFrame 概况信息
df.info()           # 结构信息
df.describe()       # 数值列统计
df.describe(include="all")  # 包含所有列
df.head()           # 前 5 行
df.tail(3)          # 后 3 行
df.sample(n=2)      # 随机 2 行
```

---

## 重命名列

**基本写法：重命名列名**
`<df>.rename(columns=<字典>)`
`<df>.columns = <列表>`

```python
# 重命名列
df = pd.DataFrame({"old_name": [1, 2]})
df = df.rename(columns={"old_name": "new_name"})
df.columns = ["a", "b"]
df = df.rename(str.upper, axis=1)  # 列名转大写
```

---

## 去重

**基本写法：去除重复行**
`<df>.drop_duplicates([subset=<列>])`
`<df>.duplicated()`

```python
# 去除重复行
df = pd.DataFrame({"a": [1, 1, 2], "b": [3, 3, 4]})
df_unique = df.drop_duplicates()
df_unique = df.drop_duplicates(subset=["a"])
print(df.duplicated())  # 布尔标记重复行
```

---

## apply 应用函数

**基本写法：沿轴应用函数**
`<df>.apply(<函数>[, axis=<轴>])`

```python
# DataFrame 应用函数
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(df.apply(sum))                    # 按列求和
print(df.apply(sum, axis=1))            # 按行求和
print(df["a"].apply(lambda x: x ** 2))  # 单列应用
print(df.applymap(lambda x: x * 2))     # 每个元素应用
```

---

## 重设索引

**基本写法：重设索引**
`<df>.reset_index([drop=<布尔>])`
`<df>.set_index(<列>)`

```python
# 重设索引
df = pd.DataFrame({"a": [1, 2]}, index=["x", "y"])
df = df.reset_index()           # 索引变列
df = df.reset_index(drop=True)  # 丢弃原索引
df = df.set_index("a")          # 设置某列为索引
```
