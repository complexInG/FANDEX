# Python collections 模块

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Counter 计数器

**基本写法：创建计数器**
`Counter(<可迭代对象>)`
```python
# 统计元素出现次数
from collections import Counter
c = Counter("abracadabra")
print(c)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

**基本写法：获取元素计数**
`<计数器>[<元素>]`
```python
# 获取指定元素的计数
c = Counter(["a", "b", "a"])
print(c["a"])  # 2
```

**基本写法：获取前 N 个高频元素**
`<计数器>.most_common([n])`
```python
# 返回计数最多的 n 个元素
c = Counter("abracadabra")
print(c.most_common(2))  # [('a', 5), ('b', 2)]
```

**基本写法：计数器加法**
`<计数器1> + <计数器2>`
```python
# 合并计数
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)  # Counter({'a': 4, 'b': 3})
```

**基本写法：计数器减法**
`<计数器1> - <计数器2>`
```python
# 计数相减（结果保留正数）
c1 = Counter(a=5, b=2)
c2 = Counter(a=1, b=4)
print(c1 - c2)  # Counter({'a': 4})
```

**基本写法：获取所有元素**
`<计数器>.elements()`
```python
# 返回所有元素的迭代器
c = Counter(a=2, b=3)
print(list(c.elements()))  # ['a', 'a', 'b', 'b', 'b']
```

**基本写法：更新计数**
`<计数器>.update(<可迭代对象>)`
```python
# 增加元素计数
c = Counter(a=1)
c.update("aab")
print(c)  # Counter({'a': 3, 'b': 1})
```

---

## defaultdict 默认字典

**基本写法：创建默认字典**
`defaultdict(<工厂函数>)`
```python
# 键不存在时自动创建默认值
from collections import defaultdict
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
print(d["a"])  # [1, 2]
```

**基本写法：int 默认值**
`defaultdict(int)`
```python
# 默认值为 0
counts = defaultdict(int)
for word in words:
    counts[word] += 1
```

**基本写法：set 默认值**
`defaultdict(set)`
```python
# 默认值为空集合
groups = defaultdict(set)
groups["fruit"].add("apple")
groups["fruit"].add("banana")
```

**基本写法：自定义默认值**
`defaultdict(lambda: <默认值>)`
```python
# 自定义默认值
d = defaultdict(lambda: "N/A")
print(d["missing"])  # N/A
```

---

## namedtuple 命名元组

**基本写法：创建命名元组**
`namedtuple("<类名>", [<字段1>, <字段2>])`
```python
# 创建具名元组类型
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)  # 1 2
```

**基本写法：字段名为字符串**
`namedtuple("<类名>", "<字段1> <字段2>")`
```python
# 空格分隔的字段名
Point = namedtuple("Point", "x y")
p = Point(3, 4)
```

**基本写法：通过键创建**
`<类型>._make(<可迭代对象>)`
```python
# 从可迭代对象创建
data = [10, 20]
p = Point._make(data)
```

**基本写法：转换为字典**
`<实例>._asdict()`
```python
# 转为字典
p = Point(1, 2)
d = p._asdict()
print(d)  # {'x': 1, 'y': 2}
```

**基本写法：替换字段值**
`<实例>._replace(<字段>=<新值>)`
```python
# 返回替换指定字段后的新实例
p = Point(1, 2)
p2 = p._replace(x=10)
print(p2)  # Point(x=10, y=2)
```

**基本写法：默认值字段**
`namedtuple("<类名>", <字段>, defaults=[<默认值>])`
```python
# 从右往左设置默认值
Point = namedtuple("Point", ["x", "y", "z"], defaults=[0])
p = Point(1, 2)  # z 默认为 0
```

---

## OrderedDict 有序字典

**基本写法：创建有序字典**
`OrderedDict([<键值对列表>])`
```python
# 保持插入顺序的字典（Python 3.7+ 普通 dict 也保序）
from collections import OrderedDict
od = OrderedDict([("a", 1), ("b", 2)])
```

**基本写法：移到末尾**
`<有序字典>.move_to_end(<键>)`
```python
# 将指定键移到末尾
od = OrderedDict(a=1, b=2, c=3)
od.move_to_end("a")
print(list(od.keys()))  # ['b', 'c', 'a']
```

**基本写法：弹出首尾**
`<有序字典>.popitem(last=<布尔>)`
```python
# 弹出首部或尾部元素
od = OrderedDict(a=1, b=2)
key, val = od.popitem(last=False)  # 弹出 a
```

---

## deque 双端队列

**基本写法：创建双端队列**
`deque([<可迭代对象>], [maxlen=<最大长度>])`
```python
# 创建双端队列
from collections import deque
dq = deque([1, 2, 3], maxlen=5)
```

**基本写法：左端添加**
`<队列>.appendleft(<元素>)`
```python
# 在左端添加元素
dq = deque([1, 2])
dq.appendleft(0)  # deque([0, 1, 2])
```

**基本写法：右端添加**
`<队列>.append(<元素>)`
```python
# 在右端添加元素
dq = deque([1, 2])
dq.append(3)  # deque([1, 2, 3])
```

**基本写法：左端弹出**
`<队列>.popleft()`
```python
# 从左端弹出元素
dq = deque([1, 2, 3])
x = dq.popleft()  # 1
```

**基本写法：批量扩展**
`<队列>.extendleft(<可迭代对象>)`
```python
# 左端批量添加
dq = deque([1])
dq.extendleft([2, 3])  # deque([3, 2, 1])
```

**基本写法：旋转**
`<队列>.rotate(<步数>)`
```python
# 向右旋转 n 步（负数向左）
dq = deque([1, 2, 3, 4])
dq.rotate(1)  # deque([4, 1, 2, 3])
```

---

## ChainMap 链式映射

**基本写法：创建链式映射**
`ChainMap(<字典1>, <字典2>)`
```python
# 合并多个字典按顺序查找
from collections import ChainMap
defaults = {"color": "red", "size": 10}
user = {"color": "blue"}
config = ChainMap(user, defaults)
print(config["color"])  # blue
print(config["size"])   # 10
```

**基本写法：添加新映射**
`<链式映射>.new_child(<字典>)`
```python
# 在链首添加新字典
config = ChainMap(user, defaults)
new_config = config.new_child({"size": 20})
print(new_config["size"])  # 20
```

---

## UserDict 自定义字典

**换行写法：继承 UserDict**
`class <类名>(UserDict):`
`    def __setitem__(self, key, value): <语句>`

```python
# 继承 UserDict 自定义字典行为
from collections import UserDict
class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    def __getitem__(self, key):
        return super().__getitem__(key.lower())
```
