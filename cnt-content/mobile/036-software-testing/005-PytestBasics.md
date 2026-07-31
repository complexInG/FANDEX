# pytest 基础

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## pytest 命令行

**基本写法：运行测试**
`pytest [<选项>] [<路径>]`

```bash
# pytest 常用命令
pytest                          # 运行所有测试
pytest test_file.py             # 运行指定文件
pytest -v                       # 详细输出
pytest -s                       # 显示 print 输出
pytest -k "表达式"              # 按表达式筛选
pytest -x                       # 失败立即停止
pytest --maxfail=2              # 失败 N 次停止
pytest --tb=short               # 简短回溯
```

---

## 测试函数定义

**基本写法：以 test_ 开头定义测试**
`def test_<名称>(): <断言>`

```python
# 定义测试函数，函数名须以 test_ 开头
def test_add():
    assert 1 + 1 == 2
```

---

## assert 断言

**基本写法：使用原生 assert**
`assert <表达式>[, <消息>]`

```python
# pytest 使用原生 assert 语句
def test_equal():
    assert 2 + 3 == 5
    assert "hello" in "hello world"
    assert [1, 2] == [1, 2]
```

---

## 测试类

**换行写法：使用类组织测试**
`class Test<名称>:`
`    def test_<方法>(self): <断言>`

```python
# 测试类名须以 Test 开头，不能有 __init__
class TestCalculator:
    def test_add(self):
        assert self.add(1, 2) == 3

    def add(self, a, b):
        return a + b
```

---

## 异常断言

**基本写法：断言抛出异常**
`with pytest.raises(<异常类型>[, match=<正则>]): <调用>`

```python
# 断言代码抛出指定异常
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error():
    with pytest.raises(ValueError, match="invalid"):
        int("abc")
```

---

## 警告断言

**基本写法：断言产生警告**
`with pytest.warns(<警告类型>[, match=<正则>]): <调用>`

```python
# 断言产生警告
import warnings

def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("test", UserWarning)
```

---

## fixture 注入

**基本写法：使用 fixture 注入依赖**
`def test_<名称>(<fixture名>): <语句>`

```python
# 通过参数名注入 fixture
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6
```

---

## conftest.py 共享 fixture

**基本写法：在 conftest.py 中定义共享 fixture**
`# conftest.py`
`@pytest.fixture`
`def <fixture名>(): <返回值>`

```python
# conftest.py 文件中的 fixture 自动被同目录及子目录测试发现
import pytest

@pytest.fixture
def db_connection():
    conn = create_conn()
    yield conn
    conn.close()
```

---

## 跳过测试

**基本写法：跳过测试用例**
`@pytest.mark.skip(reason="<原因>")`
`@pytest.mark.skipif(<条件>, reason="<原因>")`

```python
# 跳过或条件跳过测试
import pytest

@pytest.mark.skip(reason="未实现")
def test_future():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="不支持 Windows")
def test_unix_only():
    pass
```

---

## 标记预期失败

**基本写法：标记测试预期失败**
`@pytest.mark.xfail([reason="<原因>"][, raises=<异常>])`

```python
# 标记预期失败的测试
@pytest.mark.xfail(reason="已知 bug")
def test_known_bug():
    assert buggy_func() == 1
```

---

## 自定义标记

**基本写法：自定义标记并筛选**
`@pytest.mark.<标记名>`
`pytest -m <标记名>`

```python
# 自定义标记并按标记筛选
import pytest

@pytest.mark.slow
def test_large_dataset():
    pass

# 运行: pytest -m slow
```

---

## 测试输出捕获

**基本写法：访问捕获的输出**
`capsys.readouterr().out`
`capsys.readouterr().err`

```python
# 捕获 stdout/stderr
def test_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert "hello" in captured.out
```

---

## 临时目录

**基本写法：使用临时目录 fixture**
`def test_<名称>(tmp_path): <语句>`
`def test_<名称>(tmp_path_factory): <语句>`

```python
# 使用 tmp_path 创建临时目录
def test_file_write(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("content")
    assert file.read_text() == "content"
```

---

## 退出码

**基本写法：pytest 退出码含义**
`0 全部通过 | 1 部分失败 | 2 中断 | 5 无测试`

```bash
# pytest 退出码: 0 通过, 1 失败, 2 中断, 3 内部错误, 4 命令行错误, 5 无测试
pytest; echo $?
```
