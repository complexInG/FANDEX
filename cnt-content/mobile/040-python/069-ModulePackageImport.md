# Python 模块包导入

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本导入

**基本写法：导入模块**
`import <模块名>`
```python
# 导入整个模块，通过模块名访问成员
import os
path = os.getcwd()
```

---

**基本写法：导入特定成员**
`from <模块> import <名称>`
```python
# 仅导入需要的函数或类
from pathlib import Path
p = Path(".")
```

---

**基本写法：导入并设置别名**
`import <模块> as <别名>`
```python
# 用别名简化长模块名
import numpy as np
arr = np.array([1, 2, 3])
```

---

**基本写法：导入多个成员**
`from <模块> import <名称1>, <名称2>`
```python
# 一次导入多个符号
from collections import deque, defaultdict
```

---

**基本写法：导入全部公开成员**
`from <模块> import *`
```python
# 导入 __all__ 列出的名称，无 __all__ 则导入所有非下划线开头名称
# 不推荐在生产代码使用，易造成命名冲突
```

---

## 包与 __init__.py

**基本写法：定义包**
`<目录>/__init__.py`
```python
# 含 __init__.py 的目录即为包（Python 3.3+ 普通目录也支持命名空间包）
# mypackage/__init__.py
__all__ = ["core", "utils"]
```

---

**基本写法：包内模块导入**
`from <包> import <模块>`
```python
# mypackage/core.py 中定义函数
# 外部调用
from mypackage import core
core.run()
```

---

## __all__ 公开接口

**基本写法：声明公开名称**
`__all__ = [<名称列表>]`
```python
# 模块顶部声明，控制 from module import * 的导出范围
# utils.py
__all__ = ["helper", "format_text"]

def helper():
    pass

def _internal():
    # 以 _ 开头默认为私有，不会被 import * 导入
    pass
```

---

## 相对导入

**基本写法：当前包内导入**
`from . import <模块>`
```python
# 一个点表示当前包目录
# mypackage/core.py
from . import utils
```

---

**基本写法：上级包导入**
`from .. import <模块>`
```python
# 两个点表示上一级包
# mypackage/sub/child.py
from .. import core
```

---

**基本写法：指定相对层级**
`from .<模块> import <名称>`
```python
# 从当前包的指定模块导入
# mypackage/core.py
from .utils import format_text
```

---

## sys.path 路径管理

**基本写法：查看搜索路径**
`sys.path`
```python
import sys
# 列出模块搜索路径，首项常为当前脚本目录
print(sys.path)
```

---

**基本写法：临时添加搜索路径**
`sys.path.append(<路径>)`
```python
import sys
# 运行时动态加入目录，重启后失效
sys.path.append("/home/user/libs")
import mylib
```

---

**基本写法：插入到路径最前**
`sys.path.insert(0, <路径>)`
```python
import sys
# 0 表示最高优先级
sys.path.insert(0, "/opt/custom")
```

---

## importlib 动态导入

**基本写法：按字符串导入模块**
`importlib.import_module(<模块名>)`
```python
import importlib
# 运行时根据字符串动态加载模块
mod = importlib.import_module("json")
print(mod.dumps({"a": 1}))
```

---

**基本写法：导入子模块**
`importlib.import_module("<包>.<模块>")`
```python
import importlib
# 动态加载包内子模块
core = importlib.import_module("mypackage.core")
```

---

**基本写法：按名称获取函数**
`getattr(<模块>, <名称>)`
```python
import importlib
mod = importlib.import_module("collections")
# 再用 getattr 取出具体成员
Deque = getattr(mod, "deque")
```

---

## 模块属性

**基本写法：模块名**
`__name__`
```python
# 模块自身为 "__main__"，被导入时为模块全名
if __name__ == "__main__":
    main()
```

---

**基本写法：模块文件路径**
`__file__`
```python
# 获取模块所在文件路径
print(__file__)
```

---

**基本写法：模块文档字符串**
`__doc__`
```python
"""模块顶部文档字符串。"""
# 通过 __doc__ 访问
print(__doc__)
```

---

**基本写法：包路径**
`__path__`
```python
# 仅包拥有 __path__，表示包目录列表
# 子模块导入时会基于 __path__ 查找
```

---

## 模块缓存

**基本写法：查看已加载模块**
`sys.modules`
```python
import sys
# 字典缓存所有已导入模块，键为模块全名
print("json" in sys.modules)
```

---

**基本写法：重载模块**
`importlib.reload(<模块>)`
```python
import importlib, mymod
# 开发期修改源码后重新加载
importlib.reload(mymod)
```

---

## 条件与延迟导入

**基本写法：函数内导入**
`def <函数>(): import <模块>`
```python
# 延迟到调用时导入，常用于避免循环依赖或加速启动
def parse(path):
    import json
    with open(path) as f:
        return json.load(f)
```

---

**基本写法：try 容错导入**
`try: import <模块>`
```python
# 优先使用 C 加速版本，失败回退纯 Python
try:
    import cjson as json
except ImportError:
    import json
```

---