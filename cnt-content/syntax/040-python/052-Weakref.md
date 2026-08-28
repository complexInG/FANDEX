# Python weakref 弱引用

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 弱引用基础

**基本写法：创建弱引用**
`weakref.ref(<对象>)`
```python
# 创建弱引用
import weakref

class Obj:
    pass

obj = Obj()
r = weakref.ref(obj)
print(r())        # 引用对象
print(r() is obj) # True
```

**基本写法：访问引用对象**
`r()`
```python
# 调用弱引用获取对象
obj_ref = r()
if obj_ref is not None:
    print("对象存在")
else:
    print("对象已回收")
```

**基本写法：对象回收后**
`del <对象>`
```python
# 删除强引用后弱引用返回 None
del obj
print(r())  # None
```

---

## WeakValueDictionary

**基本写法：值弱引用字典**
`weakref.WeakValueDictionary()`
```python
# 字典值为弱引用，对象可被回收
d = weakref.WeakValueDictionary()
o = Obj()
d["key"] = o
print(d["key"] is o)  # True
del o
print("key" in d)     # False，对象回收后自动移除
```

---

## WeakKeyDictionary

**基本写法：键弱引用字典**
`weakref.WeakKeyDictionary()`
```python
# 字典键为弱引用
d = weakref.WeakKeyDictionary()
o = Obj()
d[o] = "value"
print(d.get(o))  # value
del o
print(len(d))    # 0
```

---

## WeakSet

**基本写法：弱引用集合**
`weakref.WeakSet()`
```python
# 集合中元素为弱引用
s = weakref.WeakSet()
o = Obj()
s.add(o)
print(o in s)  # True
del o
print(len(s))  # 0
```

---

## finalize 终结回调

**基本写法：注册终结回调**
`weakref.finalize(<对象>, <函数>, *<参数>)`
```python
# 对象回收时调用回调
def cleanup(name):
    print(f"{name} 被回收")

o = Obj()
f = weakref.finalize(o, cleanup, "myobj")
del o  # 打印 "myobj 被回收"
```

**基本写法：取消终结**
`f.detach()`
```python
# 取消终结器
f = weakref.finalize(o, cleanup, "myobj")
f.detach()  # 取消回调
```

**基本写法：检查是否存活**
`f.alive`
```python
# 检查终结器是否仍存活
print(f.alive)
```

---

## WeakMethod 方法弱引用

**基本写法：方法弱引用**
`weakref.WeakMethod(<绑定方法>)`
```python
# 对绑定方法创建弱引用
class Service:
    def run(self):
        pass

s = Service()
m = weakref.WeakMethod(s.run)
print(m() is s.run)
```

---

## proxy 代理

**基本写法：创建代理**
`weakref.proxy(<对象>)`
```python
# 代理对象自动解引用
obj = Obj()
p = weakref.proxy(obj)
print(p is obj)  # False，但行为像 obj
del obj
# 访问 p 现在会抛出 ReferenceError
```

**基本写法：代理回调**
`weakref.proxy(<对象>, <回调>)`
```python
# 代理对象回收时回调
def on_unref(ref):
    print("代理对象被回收")

p = weakref.proxy(obj, on_unref)
```

---

## 支持弱引用的对象

**基本写法：检查是否支持弱引用**
`weakref.ref(<对象>)`
```python
# 内置类型如 list/dict 不支持弱引用
try:
    weakref.ref([1, 2, 3])
except TypeError as e:
    print(e)
```

**基本写法：子类化获得支持**
`class <类>(dict): __slots__ = ("__weakref__",)`
```python
# 通过 __slots__ 让对象支持弱引用
class MyDict(dict):
    __slots__ = ("__weakref__",)
```

---

## 应用场景

**基本写法：缓存弱引用**
`WeakValueDictionary`
```python
# 缓存大对象，不阻止回收
class Cache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get(self, key, factory):
        obj = self._cache.get(key)
        if obj is None:
            obj = factory()
            self._cache[key] = obj
        return obj
```

**基本写法：观察者模式弱引用**
`WeakSet`
```python
# 观察者列表使用弱引用，避免内存泄漏
class Subject:
    def __init__(self):
        self._observers = weakref.WeakSet()
    def subscribe(self, obs):
        self._observers.add(obs)
    def notify(self, msg):
        for obs in self._observers:
            obs.update(msg)
```

---

## getweakrefcount

**基本写法：统计弱引用数**
`weakref.getweakrefcount(<对象>)`
```python
# 返回指向对象的弱引用数
print(weakref.getweakrefcount(obj))
```

**基本写法：获取所有弱引用**
`weakref.getweakrefs(<对象>)`
```python
# 返回所有弱引用列表
print(weakref.getweakrefs(obj))
```
