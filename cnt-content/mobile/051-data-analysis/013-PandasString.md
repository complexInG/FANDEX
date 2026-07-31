# 数据分析 Pandas 字符串

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 字符串访问器

**基本写法：访问字符串方法**
`<Series>.str.<方法名>`

```python
# 通过 .str 访问器使用字符串方法
s = pd.Series(["apple", "banana", "cherry"])
print(s.str.upper())
```

---

## 大小写转换

**基本写法：转换为大写**
`<Series>.str.upper()`

```python
# 转换为大写
s.str.upper()
```

---

**基本写法：转换为小写**
`<Series>.str.lower()`

```python
# 转换为小写
s.str.lower()
```

---

**基本写法：首字母大写**
`<Series>.str.capitalize()`

```python
# 首字母大写
s.str.capitalize()
```

---

**基本写法：标题格式**
`<Series>.str.title()`

```python
# 转换为标题格式（每个单词首字母大写）
s.str.title()
```

---

**基本写法：大小写互换**
`<Series>.str.swapcase()`

```python
# 大小写互换
s.str.swapcase()
```

---

## 字符串查找

**基本写法：查找子字符串**
`<Series>.str.contains(<模式>, na=<缺失值处理>)`

```python
# 判断是否包含子字符串
s.str.contains("an", na=False)
```

---

**基本写法：查找开头**
`<Series>.str.startswith(<前缀>)`

```python
# 判断是否以指定前缀开头
s.str.startswith("ap")
```

---

**基本写法：查找结尾**
`<Series>.str.endswith(<后缀>)`

```python
# 判断是否以指定后缀结尾
s.str.endswith("e")
```

---

**基本写法：查找位置**
`<Series>.str.find(<子字符串>)`

```python
# 查找子字符串位置（找不到返回 -1）
s.str.find("a")
```

---

**基本写法：匹配正则表达式**
`<Series>.str.match(<正则模式>)`

```python
# 匹配正则表达式（从头开始）
s.str.match(r"^a")
```

---

**基本写法：全字符串匹配**
`<Series>.str.fullmatch(<正则模式>)`

```python
# 完整匹配正则表达式
s.str.fullmatch(r"\w+")
```

---

## 字符串替换与分割

**基本写法：替换子字符串**
`<Series>.str.replace(<旧字符串>, <新字符串>)`

```python
# 替换子字符串
s.str.replace("a", "A")
```

---

**基本写法：使用正则替换**
`<Series>.str.replace(<正则模式>, <新字符串>, regex=True)`

```python
# 使用正则表达式替换
s.str.replace(r"\d+", "NUM", regex=True)
```

---

**基本写法：分割字符串**
`<Series>.str.split(<分隔符>)`

```python
# 分割字符串
s.str.split(",")
```

---

**基本写法：分割并展开为列**
`<Series>.str.split(<分隔符>, expand=True)`

```python
# 分割字符串并展开为多列
s.str.split(",", expand=True)
```

---

**基本写法：限制分割次数**
`<Series>.str.split(<分隔符>, n=<次数>)`

```python
# 限制分割次数
s.str.split(",", n=1)
```

---

**基本写法：按行分割**
`<Series>.str.partition(<分隔符>)`

```python
# 按分隔符分割为三部分（前、分隔符、后）
s.str.partition("-")
```

---

**基本写法：从右侧分割**
`<Series>.str.rpartition(<分隔符>)`

```python
# 从右侧开始分割
s.str.rpartition("-")
```

---

## 字符串提取

**基本写法：提取匹配组**
`<Series>.str.extract(<正则模式>)`

```python
# 提取正则匹配的分组
s.str.extract(r"(\d+)-(\w+)")
```

---

**基本写法：提取所有匹配**
`<Series>.str.extractall(<正则模式>)`

```python
# 提取所有匹配项
s.str.extractall(r"(\d+)")
```

---

**基本写法：使用命名分组**
`<Series>.str.extract(<正则模式>)`

```python
# 使用命名分组提取
s.str.extract(r"(?P<year>\d{4})-(?P<month>\d{2})")
```

---

## 字符串长度与计数

**基本写法：获取字符串长度**
`<Series>.str.len()`

```python
# 获取每个字符串的长度
s.str.len()
```

---

**基本写法：统计子字符串出现次数**
`<Series>.str.count(<子字符串>)`

```python
# 统计子字符串出现次数
s.str.count("a")
```

---

## 字符串修剪

**基本写法：去除两端空白**
`<Series>.str.strip()`

```python
# 去除字符串两端的空白字符
s.str.strip()
```

---

**基本写法：去除左侧空白**
`<Series>.str.lstrip()`

```python
# 去除字符串左侧的空白字符
s.str.lstrip()
```

---

**基本写法：去除右侧空白**
`<Series>.str.rstrip()`

```python
# 去除字符串右侧的空白字符
s.str.rstrip()
```

---

**基本写法：去除指定字符**
`<Series>.str.strip(<字符集>)`

```python
# 去除指定字符
s.str.strip("0123456789")
```

---

## 字符串填充

**基本写法：左侧填充**
`<Series>.str.pad(<宽度>, side="left", fillchar=<填充字符>)`

```python
# 左侧填充
s.str.pad(5, side="left", fillchar="0")
```

---

**基本写法：居中填充**
`<Series>.str.center(<宽度>, fillchar=<填充字符>)`

```python
# 居中填充
s.str.center(10, fillchar="-")
```

---

**基本写法：零填充**
`<Series>.str.zfill(<宽度>)`

```python
# 左侧填充零
s.str.zfill(5)
```

---

## 字符串切片

**基本写法：字符串切片**
`<Series>.str[<start>:<stop>]`

```python
# 字符串切片
s.str[0:3]
```

---

**基本写法：字符索引访问**
`<Series>.str[<索引>]`

```python
# 获取指定位置的字符
s.str[0]
```

---

## 字符串连接

**基本写法：连接字符串**
`<Series>.str.cat(<其他Series>)`

```python
# 连接两个 Series
s.str.cat(other_series, sep="-")
```

---

**基本写法：连接为单个字符串**
`<Series>.str.cat(sep=<分隔符>)`

```python
# 将整个 Series 连接为一个字符串
s.str.cat(sep=", ")
```

---

**基本写法：逐元素连接**
`<Series>.str.cat(<列表>, sep=<分隔符>)`

```python
# 逐元素连接多个 Series
s.str.cat([s2, s3], sep="-")
```

---

## 字符串判断

**基本写法：判断是否为数字**
`<Series>.str.isnumeric()`

```python
# 判断字符串是否全为数字
s.str.isnumeric()
```

---

**基本写法：判断是否为字母**
`<Series>.str.isalpha()`

```python
# 判断字符串是否全为字母
s.str.isalpha()
```

---

**基本写法：判断是否为字母数字**
`<Series>.str.isalnum()`

```python
# 判断字符串是否全为字母或数字
s.str.isalnum()
```

---

**基本写法：判断是否为空白**
`<Series>.str.isspace()`

```python
# 判断字符串是否全为空白字符
s.str.isspace()
```

---

## 字符串重复

**基本写法：重复字符串**
`<Series>.str.repeat(<次数>)`

```python
# 重复每个字符串
s.str.repeat(3)
```

---

## 编码转换

**基本写法：编码为字节**
`<Series>.str.encode(<编码>)`

```python
# 编码为字节
s.str.encode("utf-8")
```

---

**基本写法：解码字节**
`<Series>.str.decode(<编码>)`

```python
# 解码字节为字符串
s.str.decode("utf-8")
```

---

## 实战应用

**换行写法：提取邮箱域名**
`df["domain"] = df["email"].str.extract(r"@(.+)$")`

```python
# 从邮箱地址中提取域名
df["domain"] = df["email"].str.extract(r"@(.+)$")
```

---

**换行写法：标准化手机号**
`df["phone"] = df["phone"].str.replace(r"\D", "", regex=True)`

```python
# 标准化手机号格式（只保留数字）
df["phone"] = df["phone"].str.replace(r"\D", "", regex=True)
df["phone"] = df["phone"].str.zfill(11)
```
