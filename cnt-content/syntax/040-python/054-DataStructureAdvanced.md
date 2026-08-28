# Python 数据结构进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## deque 双端队列

**基本写法：创建 deque**
`collections.deque(<可迭代>, maxlen=<最大长度>)`
```python
# 创建双端队列
from collections import deque

d = deque([1, 2, 3])
d_bounded = deque(maxlen=5)  # 固定长度，溢出自动丢弃
```

**基本写法：两端追加**
`d.append(<值>)` | `d.appendleft(<值>)`
```python
# 右侧与左侧追加
d.append(4)
d.appendleft(0)
```

**基本写法：两端弹出**
`d.pop()` | `d.popleft()`
```python
# 两端弹出元素
print(d.pop())       # 4
print(d.popleft())   # 0
```

**基本写法：extend 批量追加**
`d.extend(<可迭代>)` | `d.extendleft(<可迭代>)`
```python
# 批量追加
d.extend([5, 6])
d.extendleft([-1, -2])  # 注意左侧追加顺序反转
```

**基本写法：rotate 旋转**
`d.rotate(<步数>)`
```python
# 正数右旋，负数左旋
d = deque([1, 2, 3, 4, 5])
d.rotate(2)   # deque([4, 5, 1, 2, 3])
d.rotate(-1)  # deque([5, 1, 2, 3, 4])
```

**基本写法：固定长度滑动窗口**
`deque(maxlen=<大小>)`
```python
# 自动维护滑动窗口
window = deque(maxlen=3)
for i in range(5):
    window.append(i)
    print(window)  # 最后只剩 [2, 3, 4]
```

---

## heapq 堆队列

**基本写法：创建堆**
`heapq.heapify(<列表>)`
```python
# 原地转换为最小堆
import heapq

data = [3, 1, 4, 1, 5, 9]
heapq.heapify(data)
print(data[0])  # 1（最小值）
```

**基本写法：压入元素**
`heapq.heappush(<堆>, <值>)`
```python
# 维持堆性质压入
heapq.heappush(data, 0)
```

**基本写法：弹出最小**
`heapq.heappop(<堆>)`
```python
# 弹出堆顶最小值
print(heapq.heappop(data))
```

**基本写法：push 后 pop**
`heapq.heappushpop(<堆>, <值>)`
```python
# 压入后立即弹出，比分别调用更高效
print(heapq.heappushpop(data, 2))
```

**基本写法：pop 后 Push**
`heapq.heapreplace(<堆>, <值>)`
```python
# 先弹出再压入
print(heapq.heapreplace(data, 6))
```

**基本写法：nsmallest 取最小 N**
`heapq.nsmallest(<n>, <可迭代>, key=<函数>)`
```python
# 取最小的 N 个元素
print(heapq.nsmallest(3, [5, 1, 8, 2, 9]))
```

**基本写法：nlargest 取最大 N**
`heapq.nlargest(<n>, <可迭代>, key=<函数>)`
```python
# 取最大的 N 个元素
print(heapq.nlargest(3, [5, 1, 8, 2, 9]))
```

**基本写法：最大堆**
`heapq` 配合负值
```python
# Python heapq 只支持最小堆，用负值模拟最大堆
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
print(-heapq.heappop(max_heap))  # 5
```

**基本写法：合并有序序列**
`heapq.merge(*<有序可迭代>)`
```python
# 合并多个有序序列
a = [1, 3, 5]
b = [2, 4, 6]
print(list(heapq.merge(a, b)))
```

**基本写法：自定义优先级**
`heapq` 配合元组
```python
# 元组比较实现优先队列
pq = []
heapq.heappush(pq, (1, "low"))
heapq.heappush(pq, (0, "high"))
print(heapq.heappop(pq))  # (0, "high")
```

---

## OrderedDict 有序字典

**基本写法：创建 OrderedDict**
`collections.OrderedDict()`
```python
# 有序字典（3.7+ 普通 dict 也保持插入顺序）
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
```

**基本写法：move_to_end 移动到末尾**
`od.move_to_end(<键>, last=<bool>)`
```python
# 移动元素到末尾或开头
od.move_to_end("a")           # 移到末尾
od.move_to_end("a", last=False)  # 移到开头
```

**基本写法：popitem 弹出**
`od.popitem(last=<bool>)`
```python
# 弹出末尾或开头元素
print(od.popitem())           # 弹出末尾
print(od.popitem(last=False)) # 弹出开头
```

**基本写法：按插入顺序迭代**
`for <键>, <值> in od.items():`
```python
# 迭代有序字典
for k, v in od.items():
    print(k, v)
```

**基本写法：LRU 缓存**
`OrderedDict` 实现 LRU
```python
# LRU 缓存实现
class LRU:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

---

## ChainMap 链式字典

**基本写法：创建 ChainMap**
`collections.ChainMap(*<字典>)`
```python
# 链接多个字典，按顺序查找
from collections import ChainMap

defaults = {"host": "localhost", "port": 8080}
override = {"port": 9000}
config = ChainMap(override, defaults)
print(config["host"], config["port"])  # localhost 9000
```

**基本写法：新增映射**
`cm.new_child(<字典>)`
```python
# 添加新字典到链首
cm = config.new_child({"host": "remote"})
print(cm["host"])  # remote
```

**基本写法：parents 父链**
`cm.parents`
```python
# 返回除第一个之外的所有映射
print(config.parents)
```

**基本写法：写入只影响首映射**
`cm[<键>] = <值>`
```python
# 赋值只修改第一个字典
config["host"] = "changed"
print(override)  # {"port": 9000, "host": "changed"}
```

---

## UserDict 自定义字典

**基本写法：继承 UserDict**
`class <类>(collections.UserDict):`
```python
# UserDict 比继承 dict 更易自定义
import collections

class CaseInsensitiveDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    def __getitem__(self, key):
        return super().__getitem__(key.lower())
```
