# Pandas 数据清洗

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 缺失值检测

**基本写法：检测缺失值**
`<df>.isna()` | `<df>.isnull()` | `<df>.notna()`

```python
# 检测缺失值
import pandas as pd
import numpy as np

df = pd.DataFrame({"a": [1, None, 3], "b": ["x", np.nan, "z"]})
print(df.isna())           # 布尔矩阵
print(df.isna().sum())     # 每列缺失数
print(df.isna().any())     # 哪些列有缺失
```

---

## 删除缺失值

**基本写法：删除含缺失的行或列**
`<df>.dropna([axis=<轴>][, how=<方式>][, subset=<列>])`

```python
# 删除缺失值
df.dropna()                          # 删除任何缺失的行
df.dropna(axis=1)                    # 删除任何缺失的列
df.dropna(how="all")                 # 全部缺失才删
df.dropna(subset=["a", "b"])         # 只看指定列
df.dropna(thresh=2)                  # 至少 2 个非缺失保留
```

---

## 填充缺失值

**基本写法：填充缺失值**
`<df>.fillna(<值>)`

```python
# 填充缺失值
df.fillna(0)                         # 用 0 填充
df.fillna({"a": 0, "b": "未知"})       # 不同列不同填充值
df.fillna(method="ffill")            # 前向填充
df.fillna(method="bfill")            # 后向填充
df.fillna(df.mean())                 # 用均值填充
df["a"].interpolate()                # 线性插值
```

---

## 重复值处理

**基本写法：检测与删除重复值**
`<df>.duplicated([subset=<列>])`
`<df>.drop_duplicates([subset=<列>])`

```python
# 重复值处理
df.duplicated()                      # 标记重复行
df.duplicated(subset=["a"])          # 指定列判断重复
df.drop_duplicates()                 # 删除重复行
df.drop_duplicates(subset=["a"], keep="last")  # 保留最后一条
```

---

## 类型转换

**基本写法：转换数据类型**
`<df>.astype(<类型>)`
`<df>.convert_dtypes()`

```python
# 类型转换
df["price"] = df["price"].astype(float)
df["count"] = df["count"].astype(int)
df = df.convert_dtypes()             # 自动推断最佳类型
df["date"] = pd.to_datetime(df["date"])
```

---

## 字符串清洗

**基本写法：字符串清洗方法**
`<series>.str.<方法>()`

```python
# 字符串向量化清洗
s = pd.Series(["  hello  ", "WORLD", "foo,bar"])
print(s.str.strip())              # 去除首尾空格
print(s.str.lower())             # 转小写
print(s.str.upper())             # 转大写
print(s.str.replace(",", " "))   # 替换
print(s.str.split(","))          # 分割
print(s.str.contains("o"))       # 包含判断
```

---

## replace 替换

**基本写法：替换值**
`<df>.replace(<旧>, <新>)`

```python
# 替换指定值
df.replace("N/A", np.nan)
df.replace({"a": {"old": "new"}})   # 指定列替换
df.replace([1, 2, 3], 0)            # 多值替换为同值
df.replace({"yes": True, "no": False})  # 字典映射
```

---

## 异常值检测

**基本写法：基于分位数检测异常值**
`<df>.quantile(<分位>)`

```python
# 基于 IQR 检测异常值
Q1 = df["value"].quantile(0.25)
Q3 = df["value"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df_clean = df[(df["value"] >= lower) & (df["value"] <= upper)]
```

---

## 异常值替换

**基本写法：用边界值替换异常值**
`<df>.clip(<下界>, <上界>)`

```python
# 截断异常值到边界
df["value"] = df["value"].clip(lower=0, upper=100)
df["value"] = df["value"].clip(lower=df["value"].quantile(0.01))
```

---

## apply 自定义清洗

**换行写法：应用自定义清洗函数**
`<df>[<列>] = <df>[<列>].apply(<函数>)`

```python
# 自定义清洗逻辑
def clean_phone(phone):
    return "".join(c for c in str(phone) if c.isdigit())

df["phone"] = df["phone"].apply(clean_phone)
df["email"] = df["email"].str.lower().str.strip()
```

---

## 分类数据

**基本写法：转换为分类类型**
`<series>.astype("category")`

```python
# 分类类型节省内存
df["grade"] = df["grade"].astype("category")
df["grade"] = pd.Categorical(df["grade"], categories=["低", "中", "高"], ordered=True)
print(df["grade"].cat.categories)
```

---

## 列拆分

**换行写法：拆分列为多列**
`<df>[<新列>] = <df>[<列>].str.split(<分隔符>, expand=True)`

```python
# 拆分列
df[["first", "last"]] = df["name"].str.split(" ", expand=True)
df["date_parts"] = df["date"].str.split("-")
```

---

## 列合并

**基本写法：合并多列**
`<df>[<新列>] = <df>[<列1>].astype(str) + <分隔符> + <df>[<列2>].astype(str)`

```python
# 合并多列为字符串
df["full_name"] = df["first"] + " " + df["last"]
df["datetime"] = df["date"] + " " + df["time"]
```

---

## 内存优化

**基本写法：优化内存使用**
`<df>.info(memory_usage="deep")`
`<df>.astype(<类型>)`

```python
# 内存优化
df.info(memory_usage="deep")
df["id"] = df["id"].astype("int32")        # int64 转 int32
df["cat"] = df["cat"].astype("category")   # 字符串转分类
df = df.infer_objects()                     # 自动推断类型
```
