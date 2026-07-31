# pytest 参数化与插件

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## @pytest.mark.parametrize

**换行写法：参数化测试函数**
`@pytest.mark.parametrize("<参数名>", [<值1>, <值2>])`
`def test_<名称>(<参数名>): <断言>`

```python
# 单参数数据驱动测试
import pytest

@pytest.mark.parametrize("number", [2, 4, 6])
def test_even(number):
    assert number % 2 == 0
```

---

## 多参数参数化

**换行写法：多参数参数化**
`@pytest.mark.parametrize("<a>,<b>,<expected>", [(<v1>,<v2>,<v3>), ...])`

```python
# 多参数数据驱动测试
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (0, 0, 0), (-1, 1, 0)],
)
def test_add(a, b, expected):
    assert a + b == expected
```

---

## 参数化 ids

**换行写法：自定义测试 id**
`@pytest.mark.parametrize("<参数>", [<值>], ids=[<id1>, <id2>])`

```python
# 自定义测试 id 便于报告识别
@pytest.mark.parametrize(
    "input,expected",
    [("2+4", 6), ("3*5", 15)],
    ids=["add", "multiply"],
)
def test_eval(input, expected):
    assert eval(input) == expected
```

---

## pytest.param 标记

**基本写法：为参数化用例添加标记**
`pytest.param(<值>, marks=<标记>, id="<标识>")`

```python
# 为单个参数化用例添加 xfail 等标记
@pytest.mark.parametrize(
    "x",
    [1, pytest.param(0, marks=pytest.mark.xfail, id="zero")],
)
def test_divide(x):
    assert 10 / x > 0
```

---

## 堆叠参数化

**换行写法：堆叠多个 parametrize 形成笛卡尔积**
`@pytest.mark.parametrize("<a>", [<值>])`
`@pytest.mark.parametrize("<b>", [<值>])`
`def test_<名称>(a, b): <断言>`

```python
# 多个 parametrize 装饰器形成笛卡尔积
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 20])
def test_cartesian(x, y):
    assert (x, y) in [(1,10),(1,20),(2,10),(2,20)]
```

---

## pytest-cov 覆盖率

**基本写法：生成覆盖率报告**
`pytest --cov=<模块> [--cov-report=<格式>]`

```bash
# 使用 pytest-cov 生成覆盖率报告
pytest --cov=src --cov-report=term-missing
pytest --cov=src --cov-report=html
pytest --cov=src --cov-branch --cov-fail-under=80
```

---

## pytest-mock 插件

**基本写法：使用 mocker fixture**
`def test_<名称>(mocker): <mocker.patch(...)>`

```python
# pytest-mock 提供 mocker fixture
def test_api(mocker):
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.return_value = {"id": 1}
    assert fetch().get("id") == 1
```

---

## mocker.patch

**基本写法：patch 对象方法**
`mocker.patch("<模块>.<方法>", return_value=<值>)`

```python
# patch 模块方法返回指定值
def test_fetch(mocker):
    mocker.patch("module.fetch_data", return_value="mocked")
    assert process() == "mocked"
```

---

## mocker.spy

**基本写法：监视函数调用**
`spy = mocker.spy(<对象>, "<方法>")`

```python
# spy 保留原实现并记录调用
def test_spy(mocker):
    obj = Calculator()
    spy = mocker.spy(obj, "add")
    obj.add(1, 2)
    spy.assert_called_once_with(1, 2)
```

---

## pytest-asyncio 异步测试

**基本写法：测试异步函数**
`@pytest.mark.asyncio`
`async def test_<名称>(): await <异步调用>`

```python
# pytest-asyncio 支持异步测试
import pytest

@pytest.mark.asyncio
async def test_async():
    result = await async_func()
    assert result == "ok"
```

---

## pytest-xdist 并行

**基本写法：并行运行测试**
`pytest -n <进程数|auto>`

```bash
# 使用 pytest-xdist 并行执行测试
pytest -n auto              # 自动选择进程数
pytest -n 4                 # 4 个进程
pytest -n auto --dist=loadfile  # 按文件分配
```

---

## pytest-timeout 超时

**基本写法：设置测试超时**
`@pytest.mark.timeout(<秒>)`
`pytest --timeout=<秒>`

```python
# 设置单个测试超时
@pytest.mark.timeout(5)
def test_slow():
    long_running_task()

# 全局超时: pytest --timeout=10
```

---

## pytest-repeat 重复测试

**基本写法：重复运行测试**
`@pytest.mark.repeat(<次数>)`

```python
# 重复运行测试用例
import pytest

@pytest.mark.repeat(100)
def test_flaky():
    assert random.random() > 0.01
```

---

## 自定义插件

**换行写法：编写 pytest 插件钩子**
`def pytest_<钩子名>(<参数>): <逻辑>`

```python
# 在 conftest.py 中定义钩子函数
def pytest_runtest_setup(item):
    # 每个测试运行前调用
    print(f"\n运行: {item.nodeid}")

def pytest_collection_modifyitems(items):
    # 修改收集到的测试项
    items.reverse()
```
