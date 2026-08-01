---
order: 104
title: Pandas时间序列
module: 'data-analysis'
category: data
difficulty: intermediate
description: 'Pandas 时间序列：resample、rolling、shift、diff 与时区处理。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'data-analysis/特征工程'
  - 'data-analysis/Pandas分组聚合'
  - 'data-analysis/NumPy广播机制'
  - 'data-analysis/Matplotlib子图布局'
prerequisites:
  - 'data-analysis/数据分析概述'
---
## 1. 时间索引

### 1.1 DatetimeIndex

DatetimeIndex是Pandas时间序列的重要组成部分。本节详细介绍DatetimeIndex的核心概念、工作原理和实际应用。

**关键要点**：

- DatetimeIndex的定义与核心原理
- DatetimeIndex的实现方式与技术细节
- DatetimeIndex在实际场景中的应用与最佳实践
- DatetimeIndex的常见问题与解决方案

DatetimeIndex在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 PeriodIndex

PeriodIndex是Pandas时间序列的重要组成部分。本节详细介绍PeriodIndex的核心概念、工作原理和实际应用。

**关键要点**：

- PeriodIndex的定义与核心原理
- PeriodIndex的实现方式与技术细节
- PeriodIndex在实际场景中的应用与最佳实践
- PeriodIndex的常见问题与解决方案

PeriodIndex在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 重采样

### 2.1 resample 降采样

resample 降采样是Pandas时间序列的重要组成部分。本节详细介绍resample 降采样的核心概念、工作原理和实际应用。

**关键要点**：

- resample 降采样的定义与核心原理
- resample 降采样的实现方式与技术细节
- resample 降采样在实际场景中的应用与最佳实践
- resample 降采样的常见问题与解决方案

resample 降采样在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 resample 升采样

resample 升采样是Pandas时间序列的重要组成部分。本节详细介绍resample 升采样的核心概念、工作原理和实际应用。

**关键要点**：

- resample 升采样的定义与核心原理
- resample 升采样的实现方式与技术细节
- resample 升采样在实际场景中的应用与最佳实践
- resample 升采样的常见问题与解决方案

resample 升采样在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 OHLC 重采样

OHLC 重采样是Pandas时间序列的重要组成部分。本节详细介绍OHLC 重采样的核心概念、工作原理和实际应用。

**关键要点**：

- OHLC 重采样的定义与核心原理
- OHLC 重采样的实现方式与技术细节
- OHLC 重采样在实际场景中的应用与最佳实践
- OHLC 重采样的常见问题与解决方案

OHLC 重采样在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 滑动窗口

### 3.1 rolling 窗口

rolling 窗口是Pandas时间序列的重要组成部分。本节详细介绍rolling 窗口的核心概念、工作原理和实际应用。

**关键要点**：

- rolling 窗口的定义与核心原理
- rolling 窗口的实现方式与技术细节
- rolling 窗口在实际场景中的应用与最佳实践
- rolling 窗口的常见问题与解决方案

rolling 窗口在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 expanding 窗口

expanding 窗口是Pandas时间序列的重要组成部分。本节详细介绍expanding 窗口的核心概念、工作原理和实际应用。

**关键要点**：

- expanding 窗口的定义与核心原理
- expanding 窗口的实现方式与技术细节
- expanding 窗口在实际场景中的应用与最佳实践
- expanding 窗口的常见问题与解决方案

expanding 窗口在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 ewm 指数加权

ewm 指数加权是Pandas时间序列的重要组成部分。本节详细介绍ewm 指数加权的核心概念、工作原理和实际应用。

**关键要点**：

- ewm 指数加权的定义与核心原理
- ewm 指数加权的实现方式与技术细节
- ewm 指数加权在实际场景中的应用与最佳实践
- ewm 指数加权的常见问题与解决方案

ewm 指数加权在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 时序操作

### 4.1 shift/lag

shift/lag是Pandas时间序列的重要组成部分。本节详细介绍shift/lag的核心概念、工作原理和实际应用。

**关键要点**：

- shift/lag的定义与核心原理
- shift/lag的实现方式与技术细节
- shift/lag在实际场景中的应用与最佳实践
- shift/lag的常见问题与解决方案

shift/lag在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 diff 百分比变化

diff 百分比变化是Pandas时间序列的重要组成部分。本节详细介绍diff 百分比变化的核心概念、工作原理和实际应用。

**关键要点**：

- diff 百分比变化的定义与核心原理
- diff 百分比变化的实现方式与技术细节
- diff 百分比变化在实际场景中的应用与最佳实践
- diff 百分比变化的常见问题与解决方案

diff 百分比变化在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 时区处理

时区处理是Pandas时间序列的重要组成部分。本节详细介绍时区处理的核心概念、工作原理和实际应用。

**关键要点**：

- 时区处理的定义与核心原理
- 时区处理的实现方式与技术细节
- 时区处理在实际场景中的应用与最佳实践
- 时区处理的常见问题与解决方案

时区处理在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
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

## 参考文献

Pandas 文档：https://pandas.pydata.org/docs/
NumPy 文档：https://numpy.org/doc/stable/
Matplotlib：https://matplotlib.org/
Kaggle Learn：https://www.kaggle.com/learn

## 延伸阅读

数据分析工具，见 051-data-analysis 模块文档。
概率统计基础，见 030-probability-statistics 模块。
SQL 取数，见 019-sql 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供数据分析课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 数据清洗实战

缺失：删除（比例低）或填充（均值/中位数/前向）；记录填充策略。
异常：业务规则优先，统计方法（z-score/IQR）辅助；异常分“错误”与“真实极端”。
类型与格式：日期解析、单位统一、文本标准化。
验证：清洗前后分布对比，抽样人工核对。

### 13.2 可视化叙事

图型选型：时间趋势折线、类别比较柱状、分布直方/箱线、关系散点、地理地图。
设计：标签完整、颜色语义化（红=风险）、避免 3D 与双坐标滥用。
叙事结构：背景 -> 发现 -> 结论 -> 建议。
工具：Matplotlib/Plotly/ECharts；报告用 Quarto/Jupyter。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 数据分析概述 | 001-DataAnalysisOverview | 本文的前置基础 |
| NumPy 数组操作、线性代数与随机数 | 002-NumPy | 本文的并列主题 |
| Pandas -- DataFrame/Series、数据清洗、合并重塑 | 003-PandasDataFrameSeriesDataCleaningMerge | 本文的并列主题 |
| Matplotlib -- 折线图、柱状图、散点图与子图 | 004-Matplotlib | 本文的并列主题 |
| Seaborn -- 统计可视化、热力图与分布图 | 005-Seaborn | 本文的并列主题 |
| 统计学 -- 描述统计、推断统计与假设检验 | 006-StatisticsDescriptiveInferentialHypothesisTesting | 本文的并列主题 |
| 数据清洗 -- 缺失值、异常值与数据类型转换 | 007-DataCleaningMissingOutlierTypeConversion | 本文的并列主题 |
| 实战案例 -- 电商用户行为分析 | 008-EcommerceUserBehaviorAnalysis | 本文的综合应用 |
| 数据分析进阶与实战 | 009-DataAnalysisAdvancedPractice | 本文的综合应用 |
| 数据分析全流程 | 010-DataAnalysisWorkflow | 本文的并列主题 |
| 数据清洗详解 | 011-DataCleaningDetailed | 本文的并列主题 |
| 特征工程 | 012-FeatureEngineering | 本文的并列主题 |
| Pandas分组聚合 | 013-PandasGroupAggregate | 本文的并列主题 |
| Pandas时间序列 | 014-PandasTimeSequence | 本文自身 |
| NumPy广播机制 | 015-NumPyMechanism | 本文的原理深化 |
| Matplotlib子图布局 | 016-MatplotlibSubGraph | 本文的并列主题 |
| Seaborn统计图表 | 017-SeabornStatsGraphTable | 本文的并列主题 |
| 假设检验详解 | 018-HypothesisTestingDetailed | 本文的并列主题 |
| 相关性分析 | 019-CorrelationAnalysis | 本文的并列主题 |
| 回归分析 | 020-RegressionAnalysis | 本文的并列主题 |
| 商业智能 | 021-BusinessIntelligence | 本文的并列主题 |
| 自动化报表 | 022-AutomationTable | 本文的并列主题 |
