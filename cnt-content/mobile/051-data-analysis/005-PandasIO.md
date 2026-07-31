# Pandas 数据读写

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## read_csv 读取 CSV

**基本写法：读取 CSV 文件**
`pd.read_csv(<路径>[, sep=<分隔符>][, header=<行>][, index_col=<列>])`

```python
# 读取 CSV 文件
import pandas as pd

df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", sep=",", encoding="utf-8")
df = pd.read_csv("data.csv", header=0, index_col=0)
df = pd.read_csv("data.csv", usecols=["name", "age"])
df = pd.read_csv("data.csv", nrows=100)  # 只读前 100 行
```

---

## to_csv 写入 CSV

**基本写法：写入 CSV 文件**
`<df>.to_csv(<路径>[, index=<布尔>][, encoding=<编码>])`

```python
# 写入 CSV 文件
df.to_csv("output.csv")
df.to_csv("output.csv", index=False)         # 不写入索引
df.to_csv("output.csv", encoding="utf-8-sig")  # Excel 兼容编码
df.to_csv("output.csv", columns=["a", "b"])    # 指定列
```

---

## read_excel 读取 Excel

**基本写法：读取 Excel 文件**
`pd.read_excel(<路径>[, sheet_name=<表名>][, header=<行>])`

```python
# 读取 Excel 文件（需 openpyxl 引擎）
df = pd.read_excel("data.xlsx")
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
df = pd.read_excel("data.xlsx", sheet_name=None)  # 读取所有表，返回字典
df = pd.read_excel("data.xlsx", header=0, usecols="A:C")
```

---

## to_excel 写入 Excel

**基本写法：写入 Excel 文件**
`<df>.to_excel(<路径>[, sheet_name=<表名>][, index=<布尔>])`

```python
# 写入 Excel 文件
df.to_excel("output.xlsx", index=False)
df.to_excel("output.xlsx", sheet_name="数据")

# 写入多个表
with pd.ExcelWriter("multi.xlsx") as writer:
    df1.to_excel(writer, sheet_name="表1")
    df2.to_excel(writer, sheet_name="表2")
```

---

## read_json 读取 JSON

**基本写法：读取 JSON 文件**
`pd.read_json(<路径>[, orient=<格式>][, lines=<布尔>])`

```python
# 读取 JSON 文件
df = pd.read_json("data.json")
df = pd.read_json("data.json", orient="records")
df = pd.read_json("data.jsonl", lines=True)  # JSON Lines 格式
```

---

## to_json 写入 JSON

**基本写法：写入 JSON 文件**
`<df>.to_json(<路径>[, orient=<格式>][, lines=<布尔>])`

```python
# 写入 JSON 文件
df.to_json("output.json")
df.to_json("output.json", orient="records", force_ascii=False)
df.to_json("output.jsonl", orient="records", lines=True)
```

---

## read_sql 读取数据库

**换行写法：从 SQL 数据库读取**
`from sqlalchemy import create_engine`
`engine = create_engine("<连接串>")`
`df = pd.read_sql("<SQL或表名>", engine)`

```python
# 从 SQL 数据库读取
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.db")
df = pd.read_sql("SELECT * FROM users", engine)
df = pd.read_sql_table("users", engine)
df = pd.read_sql_query("SELECT * FROM users WHERE age > 18", engine)
```

---

## to_sql 写入数据库

**基本写法：写入 SQL 数据库**
`<df>.to_sql(<表名>, <engine>[, if_exists=<策略>][, index=<布尔>])`

```python
# 写入 SQL 数据库
df.to_sql("users", engine, if_exists="replace")
df.to_sql("users", engine, if_exists="append", index=False)
# if_exists: fail(默认) | replace | append
```

---

## read_html 读取网页表格

**基本写法：从 HTML 读取表格**
`pd.read_html(<URL或路径>)`

```python
# 从网页读取表格，返回 DataFrame 列表
tables = pd.read_html("https://example.com/table.html")
df = tables[0]
```

---

## read_parquet 读取 Parquet

**基本写法：读取 Parquet 文件**
`pd.read_parquet(<路径>)`

```python
# 读取 Parquet 列式存储格式
df = pd.read_parquet("data.parquet")
df = pd.read_parquet("data.parquet", columns=["a", "b"])
```

---

## to_parquet 写入 Parquet

**基本写法：写入 Parquet 文件**
`<df>.to_parquet(<路径>[, compression=<压缩>])`

```python
# 写入 Parquet 文件
df.to_parquet("output.parquet")
df.to_parquet("output.parquet", compression="gzip")
```

---

## read_pickle 读取 Pickle

**基本写法：读取 Pickle 文件**
`pd.read_pickle(<路径>)`

```python
# 读取 Pickle 序列化文件
df = pd.read_pickle("data.pkl")
```

---

## to_pickle 写入 Pickle

**基本写法：写入 Pickle 文件**
`<df>.to_pickle(<路径>)`

```python
# 写入 Pickle 序列化文件
df.to_pickle("output.pkl")
```

---

## clipboard 剪贴板

**基本写法：读写剪贴板**
`pd.read_clipboard()`
`<df>.to_clipboard([index=<布尔>])`

```python
# 从剪贴板读取表格数据
df = pd.read_clipboard()
df.to_clipboard(index=False)
```

---

## 读写 HDF5

**基本写法：读写 HDF5 文件**
`pd.read_hdf(<路径>, <键>)`
`<df>.to_hdf(<路径>, <键>)`

```python
# 读写 HDF5 格式（适合大数据集）
df = pd.read_hdf("data.h5", key="table")
df.to_hdf("output.h5", key="table", mode="w")
```
