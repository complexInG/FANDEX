# Pandas 时间序列

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 时间戳创建

**基本写法：创建时间戳**
`pd.Timestamp(<值>)`
`pd.to_datetime(<序列>)`

```python
# 创建时间戳
import pandas as pd

ts = pd.Timestamp("2024-01-15")
ts = pd.Timestamp("2024-01-15 10:30:00")
dates = pd.to_datetime(["2024-01-01", "2024-02-01", "2024-03-01"])
```

---

## date_range 时间序列

**基本写法：生成时间范围**
`pd.date_range(<start>, <end>[, periods=<个数>][, freq=<频率>])`

```python
# 生成时间序列
dates = pd.date_range("2024-01-01", "2024-01-10")
dates = pd.date_range("2024-01-01", periods=10)
dates = pd.date_range("2024-01-01", periods=5, freq="D")   # 日
dates = pd.date_range("2024-01-01", periods=5, freq="W")   # 周
dates = pd.date_range("2024-01-01", periods=12, freq="ME")  # 月末
dates = pd.date_range("2024-01-01", periods=4, freq="YE")   # 年末
```

---

## 时间索引

**基本写法：将时间设为索引**
`<df>.set_index(<时间列>)`

```python
# 时间作为索引便于时间序列分析
df = pd.DataFrame({"date": ["2024-01-01", "2024-01-02"], "value": [1, 2]})
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
```

---

## 时间切片

**基本写法：按时间范围切片**
`<df>["<开始>":"<结束>"]`

```python
# 时间索引支持字符串切片
df = df.set_index("date")
result = df["2024-01-01":"2024-01-15"]
result = df["2024-01":]  # 2024 年 1 月起
result = df.loc["2024-01-01":"2024-01-10"]
```

---

## resample 重采样

**基本写法：时间重采样聚合**
`<df>.resample(<频率>).<聚合方法>()`

```python
# 时间重采样聚合
df.resample("D").mean()    # 按日
df.resample("W").sum()     # 按周
df.resample("ME").max()    # 按月末
df.resample("YE").mean()   # 按年

# Pandas 2.x 频率别名: D 日, W 周, ME 月末, YE 年末, h 时, min 分
```

---

## asfreq 指定频率

**基本写法：转换频率不聚合**
`<df>.asfreq(<频率>[, fill_value=<值>])`

```python
# 转换为指定频率，缺失补 NaN 或指定值
df.asfreq("D")
df.asfreq("D", fill_value=0)
df.asfreq("h", method="ffill")  # 前向填充
```

---

## shift 偏移

**基本写法：移动数据**
`<df>.shift(<周期>[, freq=<频率>])`

```python
# 数据偏移
df["prev"] = df["value"].shift(1)   # 向下移动 1 行
df["next"] = df["value"].shift(-1)  # 向上移动 1 行
df.shift(periods=1, freq="D")       # 按时间偏移
```

---

## 滚动窗口

**基本写法：滚动窗口计算**
`<df>.rolling(<窗口>).<方法>()`

```python
# 滚动窗口统计
df["rolling_mean"] = df["value"].rolling(window=7).mean()
df["rolling_std"] = df["value"].rolling(window=7).std()
df["rolling_max"] = df["value"].rolling(window=7, min_periods=1).max()
```

---

## 累计窗口

**基本写法：累计窗口计算**
`<df>.expanding().<方法>()`

```python
# 累计窗口统计
df["cum_mean"] = df["value"].expanding().mean()
df["cum_max"] = df["value"].expanding().max()
df["cum_sum"] = df["value"].expanding().sum()
```

---

## 时间属性

**基本写法：访问时间属性**
`<df>.index.<属性>`

```python
# DatetimeIndex 时间属性
df.index.year
df.index.month
df.index.day
df.index.hour
df.index.weekday        # 0=周一
df.index.day_name()     # 星期名
df.index.month_name()   # 月份名
df.index.quarter        # 季度
```

---

## dt 访问器

**基本写法：Series.dt 访问时间属性**
`<series>.dt.<属性>`

```python
# Series.dt 访问器
s = pd.Series(pd.date_range("2024-01-01", periods=5))
print(s.dt.year)
print(s.dt.month)
print(s.dt.day)
print(s.dt.weekday)
print(s.dt.day_name())
```

---

## 时区处理

**基本写法：时区本地化与转换**
`<df>.tz_localize(<时区>)`
`<df>.tz_convert(<时区>)`

```python
# 时区处理
ts = pd.Timestamp("2024-01-01 10:00")
ts = ts.tz_localize("Asia/Shanghai")
ts = ts.tz_convert("UTC")
ts = ts.tz_convert("US/Eastern")
```

---

## 时间差

**基本写法：时间差计算**
`pd.Timedelta(<值>)`
`<df>.diff()`

```python
# 时间差计算
delta = pd.Timedelta("1 day")
delta = pd.Timedelta(days=1, hours=6)

df["diff"] = df["value"].diff()      # 与前一行差值
df["pct_change"] = df["value"].pct_change()  # 变化率
```

---

## period 时期

**基本写法：时期与时间戳互转**
`pd.Period(<值>[, freq=<频率>])`
`<df>.to_period(<频率>)`

```python
# 时期 Period 处理
p = pd.Period("2024-01", freq="M")
p = pd.Period("2024", freq="Y")

df.index = df.index.to_period("M")   # 时间戳转月时期
df.index = df.index.to_timestamp()   # 时期转时间戳
```
