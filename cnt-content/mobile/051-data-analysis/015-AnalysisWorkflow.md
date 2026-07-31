# 数据分析 分析工作流

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数据加载

**基本写法：从 CSV 加载**
`pd.read_csv(<文件路径>)`

```python
# 加载 CSV 文件
df = pd.read_csv("data.csv")
```

---

**基本写法：指定编码加载**
`pd.read_csv(<文件路径>, encoding=<编码>)`

```python
# 指定编码加载 CSV
df = pd.read_csv("data.csv", encoding="utf-8")
```

---

**基本写法：加载时指定列类型**
`pd.read_csv(<文件路径>, dtype={ <列名>: <类型> })`

```python
# 指定列类型加载
df = pd.read_csv("data.csv", dtype={"id": str, "age": int})
```

---

**基本写法：加载时解析日期**
`pd.read_csv(<文件路径>, parse_dates=[<日期列>])`

```python
# 加载时解析日期列
df = pd.read_csv("data.csv", parse_dates=["date"])
```

---

**基本写法：从多个文件加载**
`pd.concat([pd.read_csv(f) for f in <文件列表>])`

```python
# 合并多个 CSV 文件
import glob
files = glob.glob("data_*.csv")
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
```

---

## 数据概览

**基本写法：查看前几行**
`<DataFrame>.head(<行数>)`

```python
# 查看前 5 行
df.head()
# 查看前 10 行
df.head(10)
```

---

**基本写法：查看数据信息**
`<DataFrame>.info()`

```python
# 查看 DataFrame 基本信息（列名、类型、非空值数）
df.info()
```

---

**基本写法：查看描述性统计**
`<DataFrame>.describe()`

```python
# 查看数值列的描述性统计
df.describe()
```

---

**基本写法：包含所有列的统计**
`<DataFrame>.describe(include="all")`

```python
# 查看所有列的统计信息
df.describe(include="all")
```

---

**基本写法：查看数据形状**
`<DataFrame>.shape`

```python
# 查看数据形状（行数，列数）
print(df.shape)
```

---

**基本写法：查看列名**
`<DataFrame>.columns`

```python
# 查看所有列名
print(df.columns.tolist())
```

---

## 数据清洗

**基本写法：查看缺失值**
`<DataFrame>.isna().sum()`

```python
# 查看每列缺失值数量
print(df.isna().sum())
```

---

**基本写法：删除缺失值**
`<DataFrame>.dropna(subset=[<列名>])`

```python
# 删除指定列的缺失值
df_clean = df.dropna(subset=["age", "salary"])
```

---

**基本写法：填充缺失值**
`<DataFrame>.fillna(<填充值>)`

```python
# 填充缺失值
df["age"] = df["age"].fillna(df["age"].mean())
df["city"] = df["city"].fillna("未知")
```

---

**基本写法：删除重复行**
`<DataFrame>.drop_duplicates()`

```python
# 删除重复行
df = df.drop_duplicates()
```

---

**基本写法：按列删除重复**
`<DataFrame>.drop_duplicates(subset=[<列名>])`

```python
# 按指定列删除重复
df = df.drop_duplicates(subset=["id"])
```

---

**基本写法：重命名列**
`<DataFrame>.rename(columns={ <旧名>: <新名> })`

```python
# 重命名列
df = df.rename(columns={"old_name": "new_name"})
```

---

**基本写法：修改列类型**
`<DataFrame>[<列名>].astype(<类型>)`

```python
# 修改列的数据类型
df["price"] = df["price"].astype(float)
df["id"] = df["id"].astype(str)
```

---

## 数据筛选

**基本写法：条件筛选**
`<DataFrame>[<条件>]`

```python
# 条件筛选
adults = df[df["age"] >= 18]
```

---

**基本写法：多条件筛选**
`<DataFrame>[(<条件1>) & (<条件2>)]`

```python
# 多条件筛选
result = df[(df["age"] >= 18) & (df["city"] == "北京")]
```

---

**基本写法：使用 query 方法**
`<DataFrame>.query(<查询表达式>)`

```python
# 使用 query 方法筛选
result = df.query("age >= 18 and city == '北京'")
```

---

**基本写法：使用 isin 筛选**
`<DataFrame>[<列名>].isin([<值列表>])`

```python
# 多值筛选
result = df[df["city"].isin(["北京", "上海", "广州"])]
```

---

**基本写法：选择列**
`<DataFrame>[[<列1>, <列2>]]`

```python
# 选择指定列
subset = df[["name", "age", "salary"]]
```

---

## 数据转换

**基本写法：应用函数**
`<DataFrame>[<列名>].apply(<函数>)`

```python
# 对列应用函数
df["age_group"] = df["age"].apply(lambda x: "成年" if x >= 18 else "未成年")
```

---

**基本写法：对整个 DataFrame 应用**
`<DataFrame>.applymap(<函数>)`

```python
# 对所有元素应用函数（Pandas 2.x 推荐使用 map）
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
```

---

**基本写法：使用 map 映射**
`<DataFrame>[<列名>].map(<映射字典>)`

```python
# 使用字典映射值
gender_map = {"M": "男", "F": "女"}
df["gender"] = df["gender"].map(gender_map)
```

---

**基本写法：使用 assign 创建新列**
`<DataFrame>.assign(<新列名>=<表达式>)`

```python
# 使用 assign 创建新列
df = df.assign(bmi=df["weight"] / (df["height"] / 100) ** 2)
```

---

## 分组聚合

**基本写法：分组聚合**
`<DataFrame>.groupby(<分组列>)[<值列>].<聚合函数>()`

```python
# 按城市分组计算平均薪资
result = df.groupby("city")["salary"].mean()
```

---

**基本写法：多列聚合**
`<DataFrame>.groupby(<分组列>).agg({ <列1>: <函数1>, <列2>: <函数2> })`

```python
# 多列不同聚合
result = df.groupby("city").agg({
    "salary": "mean",
    "age": "median",
    "id": "count"
})
```

---

**基本写法：多级聚合**
`<DataFrame>.groupby(<分组列>)[<值列>].agg([<函数1>, <函数2>])`

```python
# 多级聚合
result = df.groupby("city")["salary"].agg(["mean", "max", "min"])
```

---

**基本写法：重置索引**
`<DataFrame>.reset_index()`

```python
# 聚合后重置索引
result = df.groupby("city")["salary"].mean().reset_index()
```

---

## 数据合并

**基本写法：合并数据**
`pd.merge(<左表>, <右表>, on=<连接列>)`

```python
# 合并两个 DataFrame
result = pd.merge(df_employees, df_departments, on="dept_id")
```

---

**基本写法：拼接数据**
`pd.concat([<DataFrame1>, <DataFrame2>])`

```python
# 纵向拼接
result = pd.concat([df_jan, df_feb], ignore_index=True)
```

---

**基本写法：横向拼接**
`pd.concat([<DataFrame1>, <DataFrame2>], axis=1)`

```python
# 横向拼接
result = pd.concat([df_info, df_scores], axis=1)
```

---

## 数据导出

**基本写法：导出为 CSV**
`<DataFrame>.to_csv(<文件路径>, index=<是否写入索引>)`

```python
# 导出为 CSV（不写入索引）
df.to_csv("output.csv", index=False)
```

---

**基本写法：导出为 Excel**
`<DataFrame>.to_excel(<文件路径>, sheet_name=<工作表名>)`

```python
# 导出为 Excel
df.to_excel("output.xlsx", sheet_name="data", index=False)
```

---

**基本写法：导出为 JSON**
`<DataFrame>.to_json(<文件路径>, orient=<格式>)`

```python
# 导出为 JSON
df.to_json("output.json", orient="records", force_ascii=False)
```

---

**基本写法：导出为 Markdown**
`<DataFrame>.to_markdown()`

```python
# 导出为 Markdown 表格
print(df.to_markdown())
```

---

## 完整分析流程

**换行写法：完整数据分析流程**
`df = pd.read_csv(<文件>)`
`df = df.dropna().drop_duplicates()`
`result = df.groupby(<分组列>).agg({ <列>: <函数> })`
`result.to_csv(<输出文件>)`

```python
# 完整数据分析流程
df = pd.read_csv("sales.csv")
df = df.dropna(subset=["city", "sales"])
df = df.drop_duplicates()
df["month"] = pd.to_datetime(df["date"]).dt.month
result = df.groupby(["city", "month"])["sales"].sum().reset_index()
result.to_csv("monthly_sales.csv", index=False)
```

---

**换行写法：分组后排序取 Top N**
`result = df.groupby(<分组列>)[<值列>].sum().nlargest(<n>)`

```python
# 按城市分组计算总销售额并取前 5 名
top_cities = df.groupby("city")["sales"].sum().nlargest(5)
```

---

**换行写法：计算占比**
`df["percent"] = df["value"] / df["value"].sum() * 100`

```python
# 计算每个城市销售额占总销售额的百分比
df["sales_percent"] = df["sales"] / df["sales"].sum() * 100
```

---

**换行写法：累计计算**
`df["cumsum"] = df.groupby(<分组列>)[<值列>].cumsum()`

```python
# 计算每个城市的累计销售额
df["cumulative_sales"] = df.groupby("city")["sales"].cumsum()
```

---

**换行写法：同环比计算**
`df["pct_change"] = df.groupby(<分组列>)[<值列>].pct_change()`

```python
# 计算销售额的环比增长率
df["growth_rate"] = df.groupby("city")["sales"].pct_change()
```
