# Pandas 合并连接

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## merge 基础合并

**基本写法：数据库式连接**
`pd.merge(<left>, <right>[, how=<方式>][, on=<列>])`

```python
# 两表按列合并
import pandas as pd

left = pd.DataFrame({"id": [1, 2, 3], "name": ["A", "B", "C"]})
right = pd.DataFrame({"id": [1, 2, 4], "age": [20, 30, 40]})

result = pd.merge(left, right, on="id")
```

---

## merge how 连接方式

**基本写法：指定连接方式**
`pd.merge(<left>, <right>, how="<inner|left|right|outer|cross>")`

```python
# 不同连接方式
pd.merge(left, right, on="id", how="inner")  # 内连接
pd.merge(left, right, on="id", how="left")   # 左连接
pd.merge(left, right, on="id", how="right")  # 右连接
pd.merge(left, right, on="id", how="outer")  # 全外连接
pd.merge(left, right, how="cross")           # 笛卡尔积
```

---

## 不同列名合并

**基本写法：左右表列名不同**
`pd.merge(<left>, <right>, left_on=<左列>, right_on=<右列>)`

```python
# 左右表连接列名不同
left = pd.DataFrame({"uid": [1, 2]})
right = pd.DataFrame({"id": [1, 2]})
pd.merge(left, right, left_on="uid", right_on="id")
```

---

## 索引合并

**基本写法：按索引合并**
`pd.merge(<left>, <right>, left_index=<布尔>, right_index=<布尔>)`

```python
# 按索引合并
left = pd.DataFrame({"a": [1, 2]}, index=["x", "y"])
right = pd.DataFrame({"b": [3, 4]}, index=["x", "y"])
pd.merge(left, right, left_index=True, right_index=True)
```

---

## merge suffixes

**基本写法：处理重名列**
`pd.merge(<left>, <right>, on=<列>, suffixes=(<左后缀>, <右后缀>))`

```python
# 重名列添加后缀
left = pd.DataFrame({"id": [1], "value": [10]})
right = pd.DataFrame({"id": [1], "value": [20]})
pd.merge(left, right, on="id", suffixes=("_left", "_right"))
```

---

## merge validate

**基本写法：验证关系类型**
`pd.merge(<left>, <right>, on=<列>, validate="<关系>")`

```python
# 验证合并关系
pd.merge(left, right, on="id", validate="one_to_one")     # 一对一
pd.merge(left, right, on="id", validate="one_to_many")    # 一对多
pd.merge(left, right, on="id", validate="many_to_one")    # 多对一
pd.merge(left, right, on="id", validate="many_to_many")   # 多对多
```

---

## concat 拼接

**基本写法：沿轴拼接**
`pd.concat(<对象列表>[, axis=<轴>][, ignore_index=<布尔>])`

```python
# 沿行或列拼接
df1 = pd.DataFrame({"a": [1, 2]})
df2 = pd.DataFrame({"a": [3, 4]})

pd.concat([df1, df2])                          # 纵向拼接
pd.concat([df1, df2], ignore_index=True)       # 重新索引
pd.concat([df1, df2], axis=1)                  # 横向拼接
```

---

## concat join

**基本写法：拼接时处理不同列**
`pd.concat(<列表>, join="<inner|outer>")`

```python
# 拼接时保留共有列或全部列
df1 = pd.DataFrame({"a": [1], "b": [2]})
df2 = pd.DataFrame({"b": [3], "c": [4]})
pd.concat([df1, df2], join="inner")  # 只保留共有列 b
pd.concat([df1, df2], join="outer")  # 保留所有列，缺失补 NaN
```

---

## join 索引连接

**基本写法：按索引连接**
`<df>.join(<other>[, how=<方式>])`

```python
# DataFrame.join 默认按索引连接
left = pd.DataFrame({"a": [1, 2]}, index=["x", "y"])
right = pd.DataFrame({"b": [3, 4]}, index=["x", "y"])
left.join(right)
left.join(right, how="left")
```

---

## combine_first 合并

**基本写法：用另一表填补缺失**
`<df1>.combine_first(<df2>)`

```python
# 用 df2 填补 df1 的缺失值
df1 = pd.DataFrame({"a": [1, None, 3]})
df2 = pd.DataFrame({"a": [10, 20, 30]})
result = df1.combine_first(df2)
```

---

## append 追加（已废弃）

**基本写法：追加行（推荐用 concat）**
`pd.concat([<df1>, <df2>])`

```python
# Pandas 2.x 推荐用 concat 替代 append
result = pd.concat([df1, df2], ignore_index=True)
```

---

## 指定合并键 validate

**换行写法：检查合并键唯一性**
`<left>.drop_duplicates(subset=<列>)`
`pd.merge(<left>, <right>, on=<列>, validate="one_to_one")`

```python
# 合并前确保键唯一
left_unique = left.drop_duplicates(subset="id")
pd.merge(left_unique, right, on="id", validate="one_to_one")
```

---

## indicator 标记来源

**基本写法：标记每行来源**
`pd.merge(<left>, <right>, on=<列>, indicator=<布尔|列名>)`

```python
# indicator 列标记数据来源
result = pd.merge(left, right, on="id", indicator=True)
print(result["_merge"])
# left_only: 仅左表, both: 两表都有, right_only: 仅右表
```

---

## 多键合并

**基本写法：按多个列合并**
`pd.merge(<left>, <right>, on=[<列1>, <列2>])`

```python
# 多列联合作为合并键
pd.merge(df1, df2, on=["city", "date"])
pd.merge(df1, df2, left_on=["k1", "k2"], right_on=["k1", "k2"])
```
