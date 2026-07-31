# Matplotlib 可视化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础绘图

**基本写法：绘制折线图**
`plt.plot(<x>, <y>[, <格式>])`

```python
# 折线图基础
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()
```

---

## 图表标题与标签

**基本写法：设置标题与轴标签**
`plt.title(<标题>)`
`plt.xlabel(<标签>)`
`plt.ylabel(<标签>)`

```python
# 设置标题与轴标签
plt.plot(x, y)
plt.title("销售趋势")
plt.xlabel("月份")
plt.ylabel("销售额")
plt.show()
```

---

## 散点图

**基本写法：绘制散点图**
`plt.scatter(<x>, <y>[, c=<颜色>][, s=<大小>])`

```python
# 散点图
plt.scatter(x, y, c="red", s=50, alpha=0.5)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("散点图")
plt.show()
```

---

## 柱状图

**基本写法：绘制柱状图**
`plt.bar(<x>, <height>[, width=<宽>])`
`plt.barh(<y>, <width>)`

```python
# 柱状图与水平柱状图
plt.bar(["A", "B", "C"], [10, 20, 15])
plt.barh(["A", "B", "C"], [10, 20, 15])
```

---

## 直方图

**基本写法：绘制直方图**
`plt.hist(<数据>[, bins=<箱数>])`

```python
# 直方图查看分布
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30, color="steelblue", edgecolor="black")
plt.xlabel("值")
plt.ylabel("频数")
plt.show()
```

---

## 饼图

**基本写法：绘制饼图**
`plt.pie(<数据>[, labels=<标签>][, autopct=<格式>])`

```python
# 饼图
sizes = [30, 40, 20, 10]
labels = ["A", "B", "C", "D"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.axis("equal")
plt.show()
```

---

## 子图

**换行写法：创建子图**
`fig, axes = plt.subplots(<行数>, <列数>)`
`axes[<i>].plot(<x>, <y>)`

```python
# 多子图布局
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(["A", "B"], [1, 2])
axes[1, 1].hist(data)
plt.tight_layout()
plt.show()
```

---

## add_axes 自定义位置

**基本写法：自定义坐标轴位置**
`fig.add_axes([<left>, <bottom>, <width>, <height>])`

```python
# 自定义子图位置
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.2, 0.5, 0.3, 0.3])
ax1.plot(x, y)
ax2.plot(y, x)
```

---

## 图例

**基本写法：添加图例**
`plt.legend([<标签列表>])`
`plt.plot(<x>, <y>, label="<标签>")`

```python
# 图例
plt.plot(x, y1, label="系列1")
plt.plot(x, y2, label="系列2")
plt.legend(loc="upper left")
plt.legend(loc="best")
```

---

## 样式设置

**基本写法：线条样式**
`plt.plot(<x>, <y>, color=<颜色>, linestyle=<线型>, marker=<标记>)`

```python
# 线条样式
plt.plot(x, y, color="red", linestyle="--", marker="o", linewidth=2, markersize=8)
plt.plot(x, y, "r--o")  # 简写: 颜色+线型+标记
```

---

## 坐标轴范围

**基本写法：设置坐标轴范围**
`plt.xlim(<下>, <上>)`
`plt.ylim(<下>, <上>)`

```python
# 坐标轴范围
plt.plot(x, y)
plt.xlim(0, 10)
plt.ylim(0, 20)
plt.axis([0, 10, 0, 20])  # 同时设置
```

---

## 网格与刻度

**基本写法：网格与刻度**
`plt.grid(<布尔>)`
`plt.xticks(<位置>[, <标签>])`

```python
# 网格与刻度
plt.plot(x, y)
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks([1, 2, 3], ["一", "二", "三"])
plt.yticks([0, 5, 10], ["低", "中", "高"])
```

---

## 保存图片

**基本写法：保存图表到文件**
`plt.savefig(<路径>[, dpi=<分辨率>][, format=<格式>])`

```python
# 保存图表
plt.plot(x, y)
plt.savefig("chart.png", dpi=300, bbox_inches="tight")
plt.savefig("chart.pdf", format="pdf")
plt.savefig("chart.svg", format="svg")
```

---

## Pandas 集成绘图

**基本写法：DataFrame 直接绘图**
`<df>.plot([kind=<类型>])`

```python
# Pandas 内置 Matplotlib 绑定
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df.plot()                      # 折线图
df.plot(kind="bar")            # 柱状图
df.plot(kind="hist")           # 直方图
df.plot(kind="scatter", x="A", y="B")  # 散点图
df.plot(kind="box")            # 箱线图
```

---

## 中文字体

**换行写法：配置中文字体**
`plt.rcParams["font.sans-serif"] = ["<字体名>"]`
`plt.rcParams["axes.unicode_minus"] = False`

```python
# 解决中文显示问题
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号

plt.title("中文标题")
plt.show()
```
