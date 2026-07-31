# Pandas 分组聚合

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## groupby 基础

**基本写法：按列分组**
`<df>.groupby(<列>[, as_index=<布尔>])`

```python
# 按列分组
import pandas as pd

df = pd.DataFrame({
    "city": ["北京", "上海", "北京", "上海"],
    "sales": [100, 200, 150, 250],
})
grouped = df.groupby("city")
print(grouped["sales"].mean())
```

---

## 聚合函数

**基本写法：对分组应用聚合**
`<df>.groupby(<列>).<聚合方法>()`

```python
# 分组聚合方法
df.groupby("city")["sales"].sum()     # 求和
df.groupby("city")["sales"].mean()    # 均值
df.groupby("city")["sales"].count()   # 计数
df.groupby("city")["sales"].max()     # 最大值
df.groupby("city")["sales"].min()     # 最小值
df.groupby("city")["sales"].median()  # 中位数
df.groupby("city")["sales"].std()     # 标准差
```

---

## agg 多聚合

**基本写法：一次应用多个聚合**
`<df>.groupby(<列>).agg([<方法1>, <方法2>])`

```python
# 对同一列应用多个聚合
df.groupby("city")["sales"].agg(["mean", "sum", "count"])
df.groupby("city")["sales"].agg([np.mean, np.max])
```

---

## agg 字典指定

**换行写法：不同列应用不同聚合**
`<df>.groupby(<列>).agg({<列1>: [<方法>], <列2>: [<方法>]})`

```python
# 不同列应用不同聚合函数
df.groupby("city").agg({
    "sales": ["mean", "sum"],
    "quantity": "max",
    "price": "median",
})
```

---

## agg 命名聚合

**换行写法：为聚合结果命名**
`<df>.groupby(<列>).agg(<新名>=(<列>, <方法>))`

```python
# Pandas 2.x 命名聚合
df.groupby("city").agg(
    avg_sales=("sales", "mean"),
    total_sales=("sales", "sum"),
    max_qty=("quantity", "max"),
)
```

---

## 自定义聚合函数

**基本写法：应用自定义函数**
`<df>.groupby(<列>).agg(<函数>)`

```python
# 自定义聚合函数
df.groupby("city")["sales"].agg(lambda x: x.max() - x.min())

def range_func(x):
    return x.max() - x.min()

df.groupby("city")["sales"].agg(range_func)
```

---

## 多列分组

**基本写法：按多列分组**
`<df>.groupby([<列1>, <列2>])`

```python
# 多列分组形成层次索引
df.groupby(["city", "category"])["sales"].sum()
df.groupby(["city", "category"]).agg({"sales": "mean", "qty": "sum"})
```

---

## transform 变换

**基本写法：分组变换保持原形状**
`<df>.groupby(<列>)[<列>].transform(<方法>)`

```python
# transform 返回与原 DataFrame 等长的结果
df["sales_mean"] = df.groupby("city")["sales"].transform("mean")
df["sales_norm"] = df.groupby("city")["sales"].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

---

## filter 过滤分组

**基本写法：按条件过滤整个分组**
`<df>.groupby(<列>).filter(<函数>)`

```python
# 过滤满足条件的分组
df.groupby("city").filter(lambda g: g["sales"].sum() > 200)
df.groupby("city").filter(lambda g: len(g) > 1)
```

---

## apply 通用应用

**基本写法：分组应用任意函数**
`<df>.groupby(<列>).apply(<函数>)`

```python
# 分组应用任意函数
def top_n(g, n=2):
    return g.nlargest(n, "sales")

df.groupby("city").apply(top_n, n=2)
df.groupby("city").apply(lambda g: g.head(1))
```

---

## 分组迭代

**基本写法：遍历各分组**
`for <名>, <组> in <df>.groupby(<列>):`

```python
# 遍历各分组
for name, group in df.groupby("city"):
    print(f"城市: {name}")
    print(group)

# 多列分组遍历
for (city, cat), group in df.groupby(["city", "category"]):
    print(city, cat, len(group))
```

---

## 分组信息

**基本写法：访问分组元信息**
`<grouped>.groups` | `<grouped>.ngroups` | `<grouped>.get_group(<名>)`

```python
# 分组元信息
grouped = df.groupby("city")
print(grouped.groups)         # 各组索引
print(grouped.ngroups)        # 分组数量
print(grouped.get_group("北京"))  # 获取指定分组
print(grouped.size())         # 各组大小
```

---

## as_index 参数

**基本写法：分组列是否作为索引**
`<df>.groupby(<列>, as_index=<布尔>)`

```python
# as_index=False 保留分组列为普通列
df.groupby("city", as_index=False)["sales"].sum()
# 等价 SQL: SELECT city, SUM(sales) FROM df GROUP BY city
```

---

## 窗口函数 rolling

**基本写法：滚动窗口计算**
`<df>.rolling(<窗口大小>).<方法>()`

```python
# 滚动窗口计算
df["rolling_mean"] = df["sales"].rolling(window=3).mean()
df["rolling_sum"] = df["sales"].rolling(window=3, min_periods=1).sum()
```

---

## 窗口函数 expanding

**基本写法：扩展窗口计算**
`<df>.expanding(<min_periods>).<方法>()`

```python
# 累计扩展窗口计算
df["cum_mean"] = df["sales"].expanding().mean()
df["cum_sum"] = df["sales"].expanding(min_periods=2).sum()
```
