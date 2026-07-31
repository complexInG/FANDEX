# 数据分析 数据重塑

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数据透视

**基本写法：创建透视表**
`<DataFrame>.pivot(index=<行索引>, columns=<列索引>, values=<值>)`

```python
# 创建透视表
pivoted = df.pivot(index="date", columns="city", values="sales")
```

---

**基本写法：使用 pivot_table 聚合**
`<DataFrame>.pivot_table(index=<行索引>, columns=<列索引>, values=<值>, aggfunc=<聚合函数>)`

```python
# 使用 pivot_table 进行聚合（默认求均值）
pivoted = df.pivot_table(index="city", columns="year", values="sales", aggfunc="sum")
```

---

**基本写法：多值透视**
`<DataFrame>.pivot_table(index=<行索引>, columns=<列索引>, values=[<列1>, <列2>])`

```python
# 多值透视表
pivoted = df.pivot_table(index="city", columns="year", values=["sales", "profit"])
```

---

**基本写法：添加边际汇总**
`<DataFrame>.pivot_table(index=<行索引>, columns=<列索引>, values=<值>, margins=True)`

```python
# 添加行和列的汇总
pivoted = df.pivot_table(index="city", columns="year", values="sales", margins=True)
```

---

**基本写法：填充缺失值**
`<DataFrame>.pivot_table(..., fill_value=<填充值>)`

```python
# 透视表填充缺失值
pivoted = df.pivot_table(index="city", columns="year", values="sales", fill_value=0)
```

---

## 逆透视

**基本写法：宽表转长表**
`<DataFrame>.melt(id_vars=<标识列>, value_vars=<值列>)`

```python
# 宽表转长表
melted = df.melt(id_vars=["city"], value_vars=["2023", "2024"])
```

---

**基本写法：自定义列名**
`<DataFrame>.melt(id_vars=<标识列>, var_name=<变量名>, value_name=<值名>)`

```python
# 自定义变量列和值列名称
melted = df.melt(id_vars=["city"], var_name="year", value_name="sales")
```

---

**基本写法：使用 wide_to_long**
`pd.wide_to_long(<DataFrame>, stubnames=<前缀>, i=<索引列>, j=<后缀列>)`

```python
# 宽表转长表（适用于列名有规律的情况）
long_df = pd.wide_to_long(df, stubnames="sales", i="city", j="year", sep="_")
```

---

## 堆叠与解堆叠

**基本写法：堆叠数据**
`<DataFrame>.stack()`

```python
# 堆叠（列转为行）
stacked = df.stack()
```

---

**基本写法：解堆叠数据**
`<DataFrame>.unstack()`

```python
# 解堆叠（行转为列）
unstacked = stacked.unstack()
```

---

**基本写法：指定层级解堆叠**
`<DataFrame>.unstack(level=<层级>)`

```python
# 指定层级解堆叠
unstacked = df.unstack(level=0)
```

---

**基本写法：填充解堆叠缺失值**
`<DataFrame>.unstack(fill_value=<填充值>)`

```python
# 解堆叠并填充缺失值
unstacked = df.unstack(fill_value=0)
```

---

## 交叉表

**基本写法：创建交叉表**
`pd.crosstab(<行数据>, <列数据>)`

```python
# 创建交叉表（计算频数）
cross = pd.crosstab(df["city"], df["category"])
```

---

**基本写法：带聚合值的交叉表**
`pd.crosstab(<行数据>, <列数据>, values=<值>, aggfunc=<聚合函数>)`

```python
# 带聚合值的交叉表
cross = pd.crosstab(df["city"], df["category"], values=df["sales"], aggfunc="sum")
```

---

**基本写法：添加边际汇总**
`pd.crosstab(<行数据>, <列数据>, margins=True)`

```python
# 交叉表添加汇总
cross = pd.crosstab(df["city"], df["category"], margins=True)
```

---

**基本写法：归一化交叉表**
`pd.crosstab(<行数据>, <列数据>, normalize=<归一化方式>)`

```python
# 按行归一化（百分比）
cross = pd.crosstab(df["city"], df["category"], normalize="index")
```

---

## 虚拟变量

**基本写法：生成虚拟变量**
`pd.get_dummies(<DataFrame>, columns=<列名>)`

```python
# 将分类变量转为虚拟变量
df_dummies = pd.get_dummies(df, columns=["city"])
```

---

**基本写法：去除一个类别**
`pd.get_dummies(<DataFrame>, columns=<列名>, drop_first=True)`

```python
# 去除第一个类别（避免多重共线性）
df_dummies = pd.get_dummies(df, columns=["city"], drop_first=True)
```

---

**基本写法：指定前缀**
`pd.get_dummies(<DataFrame>, columns=<列名>, prefix=<前缀>)`

```python
# 自定义虚拟变量列名前缀
df_dummies = pd.get_dummies(df, columns=["city"], prefix="c")
```

---

## 分箱

**基本写法：等宽分箱**
`pd.cut(<Series>, bins=<分箱数>)`

```python
# 等宽分箱
df["age_group"] = pd.cut(df["age"], bins=5)
```

---

**基本写法：自定义分箱边界**
`pd.cut(<Series>, bins=[<边界1>, <边界2>, ...])`

```python
# 自定义分箱边界
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 35, 60, 100])
```

---

**基本写法：自定义标签**
`pd.cut(<Series>, bins=<分箱数>, labels=[<标签1>, ...])`

```python
# 自定义分箱标签
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 35, 60, 100], 
                          labels=["未成年", "青年", "中年", "老年"])
```

---

**基本写法：等频分箱**
`pd.qcut(<Series>, q=<分箱数>)`

```python
# 等频分箱（每箱样本数大致相等）
df["score_group"] = pd.qcut(df["score"], q=4)
```

---

**基本写法：自定义分位数**
`pd.qcut(<Series>, q=[<分位数1>, ...])`

```python
# 自定义分位数分箱
df["score_group"] = pd.qcut(df["score"], q=[0, 0.25, 0.5, 0.75, 1])
```

---

## 排名与排序

**基本写法：数据排名**
`<DataFrame>.rank(method=<方法>)`

```python
# 数据排名（平均排名）
df["rank"] = df["sales"].rank()
```

---

**基本写法：指定排名方法**
`<DataFrame>.rank(method=<方法>)`

```python
# 不同排名方法
df["rank"] = df["sales"].rank(method="min")    # 最小排名
df["rank"] = df["sales"].rank(method="max")    # 最大排名
df["rank"] = df["sales"].rank(method="dense")  # 稠密排名
```

---

**基本写法：按多列排序**
`<DataFrame>.sort_values(by=[<列1>, <列2>])`

```python
# 按多列排序
df_sorted = df.sort_values(by=["city", "sales"], ascending=[True, False])
```

---

## 数据转置

**基本写法：转置 DataFrame**
`<DataFrame>.T`

```python
# 转置 DataFrame
df_transposed = df.T
```

---

**基本写法：使用 transpose 方法**
`<DataFrame>.transpose()`

```python
# 转置 DataFrame
df_transposed = df.transpose()
```

---

## 实战应用

**换行写法：透视表转长表**
`melted = pivoted.reset_index().melt(id_vars="city")`

```python
# 透视表转长表
pivoted = df.pivot_table(index="city", columns="year", values="sales")
melted = pivoted.reset_index().melt(id_vars="city", var_name="year", value_name="sales")
```

---

**换行写法：多级索引重塑**
`df = df.unstack().reset_index()`

```python
# 多级索引重塑为普通 DataFrame
df_grouped = df.groupby(["city", "year"])["sales"].sum()
df_flat = df_grouped.unstack().reset_index()
```
