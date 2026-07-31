# pytest Fixture

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## @pytest.fixture 定义

**换行写法：定义 fixture**
`@pytest.fixture([scope=<作用域>])`
`def <fixture名>(<依赖>): <返回值>`

```python
# 定义 fixture 供测试注入
import pytest

@pytest.fixture
def user():
    return {"name": "Alice", "age": 30}

def test_user_name(user):
    assert user["name"] == "Alice"
```

---

## scope 作用域

**基本写法：设置 fixture 作用域**
`@pytest.fixture(scope="<function|class|module|package|session>")`

```python
# fixture 作用域决定生命周期
@pytest.fixture(scope="function")  # 每个测试
@pytest.fixture(scope="class")     # 每个测试类
@pytest.fixture(scope="module")    # 每个测试模块
@pytest.fixture(scope="session")   # 整个测试会话
def db():
    return create_db()
```

---

## yield 清理

**换行写法：使用 yield 执行清理**
`@pytest.fixture`
`def <fixture名>():`
`    <setup>`
`    yield <值>`
`    <teardown>`

```python
# yield 之前的为 setup，之后的为 teardown
@pytest.fixture
def connection():
    conn = create_conn()
    yield conn
    conn.close()
```

---

## params 参数化 fixture

**换行写法：参数化 fixture**
`@pytest.fixture(params=[<值1>, <值2>])`
`def <fixture名>(request): return request.param`

```python
# 参数化 fixture 对每组参数运行一次
@pytest.fixture(params=["smtp.gmail.com", "mail.python.org"])
def server(request):
    return connect(request.param)

def test_server(server):
    assert server.is_connected()
```

---

## autouse 自动使用

**基本写法：fixture 自动应用**
`@pytest.fixture(autouse=True)`

```python
# autouse fixture 无需显式声明参数
@pytest.fixture(autouse=True)
def reset_state():
    db.reset()
    yield
    db.clear()
```

---

## fixture 依赖

**换行写法：fixture 依赖其他 fixture**
`@pytest.fixture`
`def <fixture名>(<其他fixture>): <语句>`

```python
# fixture 之间可以相互依赖
@pytest.fixture
def engine():
    return Engine()

@pytest.fixture
def car(engine):
    return Car(engine)
```

---

## pytest.param 标记参数

**基本写法：为参数化 fixture 添加标记**
`pytest.param(<值>, marks=<标记>, id="<标识>")`

```python
# 为单个参数添加标记与 id
@pytest.fixture(params=[
    pytest.param(1, id="one"),
    pytest.param(2, marks=pytest.mark.xfail, id="two"),
])
def num(request):
    return request.param
```

---

## conftest.py 共享 fixture

**基本写法：在 conftest.py 定义跨文件共享的 fixture**
`# conftest.py`
`@pytest.fixture(scope="<作用域>")`
`def <fixture名>(): <返回值>`

```python
# conftest.py 中的 fixture 自动被同目录及子目录发现
# 无需 import 即可使用
import pytest

@pytest.fixture(scope="session")
def api_client():
    return APIClient()
```

---

## usefixtures 装饰器

**基本写法：在类上应用 fixture**
`@pytest.mark.usefixtures("<fixture名>")`

```python
# 在测试类上应用 fixture
@pytest.mark.usefixtures("setup_db")
class TestDatabase:
    def test_query(self):
        assert db.query() is not None
```

---

## fixture 覆盖

**换行写法：在子目录覆盖 fixture**
`# tests/unit/conftest.py`
`@pytest.fixture`
`def <同名fixture>(): <新实现>`

```python
# 子目录 conftest.py 可覆盖父级同名 fixture
@pytest.fixture
def user():  # 覆盖上层 user fixture
    return {"name": "Bob"}
```

---

## request 上下文

**基本写法：通过 request 访问上下文**
`def <fixture>(request): <request.param|request.module>`

```python
# 通过 request 访问测试上下文信息
@pytest.fixture
def info(request):
    return {
        "module": request.module.__name__,
        "node": request.node.name,
    }
```

---

## 间接参数化

**换行写法：间接参数化 fixture**
`@pytest.mark.parametrize("<fixture名>", [<值>], indirect=True)`

```python
# indirect=True 将参数传给 fixture 而非测试函数
@pytest.fixture
def num(request):
    return request.param * 2

@pytest.mark.parametrize("num", [1, 2, 3], indirect=True)
def test_double(num):
    assert num in [2, 4, 6]
```

---

## fixture 工厂

**换行写法：fixture 返回工厂函数**
`@pytest.fixture`
`def <fixture名>():`
`    def factory(<参数>): <返回对象>`
`    return factory`

```python
# fixture 返回工厂函数创建动态对象
@pytest.fixture
def make_user():
    def factory(name, age):
        return {"name": name, "age": age}
    return factory

def test_user(make_user):
    user = make_user("Alice", 30)
    assert user["name"] == "Alice"
```
