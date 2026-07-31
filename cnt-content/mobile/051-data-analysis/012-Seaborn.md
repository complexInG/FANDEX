# 数据分析 Seaborn 可视化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础设置

**基本写法：导入 Seaborn**
`import seaborn as sns`

```python
# 导入 seaborn 并设置主题
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
```

---

**基本写法：设置主题**
`sns.set_theme(style=<主题>)`

```python
# 设置主题（darkgrid, whitegrid, dark, white, ticks）
sns.set_theme(style="darkgrid")
```

---

**基本写法：设置调色板**
`sns.set_palette(<调色板名>)`

```python
# 设置调色板
sns.set_palette("husl")
```

---

**基本写法：查看调色板**
`sns.color_palette(<调色板名>)`

```python
# 查看调色板
palette = sns.color_palette("deep")
sns.palplot(palette)
```

---

## 关系图

**基本写法：绘制散点图**
`sns.scatterplot(data=<数据>, x=<x列>, y=<y列>)`

```python
# 绘制散点图
sns.scatterplot(data=df, x="height", y="weight")
plt.show()
```

---

**基本写法：按类别着色**
`sns.scatterplot(data=<数据>, x=<x列>, y=<y列>, hue=<分类列>)`

```python
# 按类别着色
sns.scatterplot(data=df, x="height", y="weight", hue="gender")
```

---

**基本写法：绘制折线图**
`sns.lineplot(data=<数据>, x=<x列>, y=<y列>)`

```python
# 绘制折线图
sns.lineplot(data=df, x="month", y="sales")
```

---

**基本写法：多变量关系图**
`sns.relplot(data=<数据>, x=<x列>, y=<y列>, kind=<图表类型>)`

```python
# 绘制多变量关系图
sns.relplot(data=df, x="height", y="weight", kind="scatter", col="gender")
```

---

## 分布图

**基本写法：绘制直方图**
`sns.histplot(data=<数据>, x=<列>, bins=<分箱数>)`

```python
# 绘制直方图
sns.histplot(data=df, x="age", bins=20)
```

---

**基本写法：绘制核密度估计图**
`sns.kdeplot(data=<数据>, x=<列>)`

```python
# 绘制核密度估计图
sns.kdeplot(data=df, x="salary")
```

---

**基本写法：绘制经验累积分布函数**
`sns.ecdfplot(data=<数据>, x=<列>)`

```python
# 绘制 ECDF 图
sns.ecdfplot(data=df, x="score")
```

---

**基本写法：绘制分布-散点组合图**
`sns.rugplot(data=<数据>, x=<列>)`

```python
# 绘制 rugplot（在轴上显示数据点）
sns.rugplot(data=df, x="age")
```

---

**基本写法：组合分布图**
`sns.displot(data=<数据>, x=<列>, kind=<图表类型>)`

```python
# 组合直方图和 KDE
sns.displot(data=df, x="salary", kind="kde", rug=True)
```

---

## 分类图

**基本写法：绘制箱线图**
`sns.boxplot(data=<数据>, x=<分类列>, y=<数值列>)`

```python
# 绘制箱线图
sns.boxplot(data=df, x="city", y="salary")
```

---

**基本写法：绘制小提琴图**
`sns.violinplot(data=<数据>, x=<分类列>, y=<数值列>)`

```python
# 绘制小提琴图
sns.violinplot(data=df, x="gender", y="height")
```

---

**基本写法：绘制条形图**
`sns.barplot(data=<数据>, x=<分类列>, y=<数值列>)`

```python
# 绘制条形图（默认显示均值和置信区间）
sns.barplot(data=df, x="city", y="sales")
```

---

**基本写法：绘制计数图**
`sns.countplot(data=<数据>, x=<分类列>)`

```python
# 绘制计数图（统计每个类别的数量）
sns.countplot(data=df, x="gender")
```

---

**基本写法：绘制点图**
`sns.pointplot(data=<数据>, x=<分类列>, y=<数值列>)`

```python
# 绘制点图（显示均值和置信区间）
sns.pointplot(data=df, x="month", y="sales")
```

---

**基本写法：绘制蜂群图**
`sns.swarmplot(data=<数据>, x=<分类列>, y=<数值列>)`

```python
# 绘制蜂群图（不重叠的散点图）
sns.swarmplot(data=df, x="city", y="salary")
```

---

## 回归图

**基本写法：绘制线性回归图**
`sns.regplot(data=<数据>, x=<x列>, y=<y列>)`

```python
# 绘制线性回归图（含拟合线和置信区间）
sns.regplot(data=df, x="experience", y="salary")
```

---

**基本写法：绘制多变量回归图**
`sns.lmplot(data=<数据>, x=<x列>, y=<y列>, hue=<分类列>)`

```python
# 按类别绘制回归图
sns.lmplot(data=df, x="experience", y="salary", hue="education")
```

---

**基本写法：绘制残差图**
`sns.residplot(data=<数据>, x=<x列>, y=<y列>)`

```python
# 绘制残差图（检查回归模型的残差）
sns.residplot(data=df, x="experience", y="salary")
```

---

## 矩阵图

**基本写法：绘制热力图**
`sns.heatmap(<矩阵数据>, annot=<是否标注>)`

```python
# 绘制热力图
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
```

---

**基本写法：绘制聚类图**
`sns.clustermap(<矩阵数据>)`

```python
# 绘制带聚类的热力图
sns.clustermap(corr, annot=True)
```

---

## 多变量图

**基本写法：绘制成对关系图**
`sns.pairplot(data=<数据>, hue=<分类列>)`

```python
# 绘制成对关系图（散点图矩阵）
sns.pairplot(data=df, hue="species")
```

---

**基本写法：绘制联合分布图**
`sns.jointplot(data=<数据>, x=<x列>, y=<y列>, kind=<类型>)`

```python
# 绘制联合分布图
sns.jointplot(data=df, x="height", y="weight", kind="hex")
```

---

**基本写法：绘制多面板分类图**
`sns.catplot(data=<数据>, x=<分类列>, y=<数值列>, kind=<图表类型>)`

```python
# 绘制多面板分类图
sns.catplot(data=df, x="city", y="salary", kind="box", col="year")
```

---

## 样式定制

**基本写法：设置图表大小**
`sns.set_theme(rc={"figure.figsize": (<宽>, <高>)})`

```python
# 设置图表大小
sns.set_theme(rc={"figure.figsize": (10, 6)})
```

---

**基本写法：设置字体大小**
`sns.set_theme(font_scale=<缩放比例>)`

```python
# 设置字体大小
sns.set_theme(font_scale=1.2)
```

---

**基本写法：移除顶部和右侧轴线**
`sns.despine()`

```python
# 移除图表的顶部和右侧轴线
sns.boxplot(data=df, x="city", y="salary")
sns.despine()
```

---

**基本写法：保存图表**
`plt.savefig(<文件路径>, dpi=<分辨率>, bbox_inches="tight")`

```python
# 保存图表到文件
sns.scatterplot(data=df, x="height", y="weight")
plt.savefig("scatter.png", dpi=300, bbox_inches="tight")
```

---

## 数据加载

**基本写法：加载内置数据集**
`sns.load_dataset(<数据集名>)`

```python
# 加载 seaborn 内置数据集
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
```
