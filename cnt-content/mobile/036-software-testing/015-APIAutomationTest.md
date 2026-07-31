# API 自动化测试

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## requests 基础请求

**基本写法：发送 HTTP 请求**
`import requests`
`requests.<method>(<url>, **<kwargs>)`

```python
# requests 发送各类 HTTP 请求
import requests

r = requests.get("https://api.example.com/users")
r = requests.post("https://api.example.com/users", json={"name": "Alice"})
r = requests.put(url, json=data)
r = requests.delete(url)
```

---

## 响应对象

**基本写法：访问响应内容**
`<response>.status_code`
`<response>.json()`
`<response>.text`
`<response>.headers`

```python
# 访问 HTTP 响应
r = requests.get("https://api.example.com/users")
assert r.status_code == 200
data = r.json()
content = r.text
headers = r.headers
```

---

## 请求参数

**基本写法：传递查询参数与请求体**
`requests.get(<url>, params=<字典>)`
`requests.post(<url>, json=<字典>|data=<字典>)`

```python
# 查询参数与请求体
params = {"page": 1, "size": 10}
r = requests.get(url, params=params)

payload = {"name": "Alice", "age": 30}
r = requests.post(url, json=payload)
r = requests.post(url, data=payload)
```

---

## 请求头与认证

**基本写法：设置请求头与认证**
`requests.get(<url>, headers=<字典>, auth=(<user>, <pass>))`

```python
# 自定义请求头与 Basic 认证
headers = {"Authorization": "Bearer token", "Content-Type": "application/json"}
r = requests.get(url, headers=headers)
r = requests.get(url, auth=("user", "pass"))
```

---

## pytest 集成 API 测试

**换行写法：pytest 测试 API**
`def test_<名称>():`
`    r = requests.<method>(<url>)`
`    assert r.status_code == <期望>`

```python
# pytest 测试 API 接口
import requests

def test_get_users():
    r = requests.get("https://api.example.com/users")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_create_user():
    r = requests.post(url, json={"name": "Alice"})
    assert r.status_code == 201
    assert r.json()["name"] == "Alice"
```

---

## TestClient FastAPI 测试

**换行写法：FastAPI 测试客户端**
`from fastapi.testclient import TestClient`
`client = TestClient(<app>)`
`response = client.<method>("<路径>")`

```python
# FastAPI 内置测试客户端
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello"}
```

---

## responses 模拟 HTTP

**换行写法：使用 responses 拦截请求**
`@responses.activate`
`def test_<名称>():`
`    responses.add(responses.GET, <url>, json=<数据>, status=<状态码>)`

```python
# responses 库模拟 HTTP 响应
import responses
import requests

@responses.activate
def test_mock_api():
    responses.add(
        responses.GET,
        "https://api.example.com/users",
        json={"id": 1},
        status=200,
    )
    r = requests.get("https://api.example.com/users")
    assert r.json() == {"id": 1}
```

---

## httpx 异步测试

**换行写法：httpx 异步客户端**
`async with httpx.AsyncClient() as client:`
`    response = await client.<method>(<url>)`

```python
# httpx 异步 API 测试
import httpx
import pytest

@pytest.mark.asyncio
async def test_async_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/users")
        assert response.status_code == 200
```

---

## JSON Schema 验证

**换行写法：验证响应结构**
`from jsonschema import validate`
`validate(instance=<数据>, schema=<schema>)`

```python
# 验证 JSON 响应符合 schema
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
    },
    "required": ["id", "name"],
}

def test_response_schema():
    data = response.json()
    validate(instance=data, schema=schema)
```

---

## 参数化 API 测试

**换行写法：参数化测试多个接口**
`@pytest.mark.parametrize("<参数>", [<数据>])`
`def test_<名称>(<参数>): <调用与断言>`

```python
# 参数化测试多个用例
import pytest
import requests

@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
])
def test_get_user(user_id, expected_name):
    r = requests.get(f"https://api.example.com/users/{user_id}")
    assert r.json()["name"] == expected_name
```

---

## 会话管理

**换行写法：使用 Session 保持会话**
`s = requests.Session()`
`s.headers.update(<头>)`
`r = s.<method>(<url>)`

```python
# Session 保持 Cookie 与连接
s = requests.Session()
s.headers.update({"Authorization": "Bearer token"})

r = s.post(url, json={"name": "Alice"})
r = s.get(url)  # 复用会话
s.close()
```

---

## 超时与重试

**基本写法：设置超时与自动重试**
`requests.<method>(<url>, timeout=<秒>)`
`from requests.adapters import HTTPAdapter`
`s.mount("<前缀>", HTTPAdapter(max_retries=<n>))`

```python
# 超时设置与自动重试
import requests
from requests.adapters import HTTPAdapter

r = requests.get(url, timeout=5)

s = requests.Session()
adapter = HTTPAdapter(max_retries=3)
s.mount("https://", adapter)
```

---

## pytest-httpserver 本地服务器

**换行写法：启动本地 HTTP 服务器**
`with HTTPServer() as httpserver:`
`    httpserver.expect_request("<路径>").respond_with_json(<数据>)`
`    requests.get(httpserver.url_for("<路径>"))`

```python
# pytest-httpserver 启动本地 Mock 服务器
from pytest_httpserver import HTTPServer
import requests

def test_local_server():
    with HTTPServer() as httpserver:
        httpserver.expect_request("/api").respond_with_json({"ok": True})
        r = requests.get(httpserver.url_for("/api"))
        assert r.json() == {"ok": True}
```
