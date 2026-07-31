# Python urllib 标准库

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## urllib.request 请求

**基本写法：urlopen 打开 URL**
`urllib.request.urlopen(<URL>)`
```python
# 打开 URL 并读取
from urllib.request import urlopen

with urlopen("https://www.python.org") as resp:
    print(resp.read()[:100])
```

**基本写法：带超时**
`urlopen(<URL>, timeout=<秒>)`
```python
# 设置超时
with urlopen("https://www.python.org", timeout=10) as resp:
    print(resp.status)
```

**基本写法：Request 自定义请求**
`urllib.request.Request(<URL>, data=<数据>, headers=<头>)`
```python
# 自定义请求对象
from urllib.request import Request, urlopen

req = Request(
    "https://httpbin.org/post",
    data=b"key=value",
    headers={"User-Agent": "MyClient/1.0"},
    method="POST",
)
with urlopen(req) as resp:
    print(resp.read().decode()[:100])
```

**基本写法：携带 User-Agent**
`req.add_header(<键>, <值>)`
```python
# 添加请求头
req = Request("https://www.python.org")
req.add_header("User-Agent", "MyClient/1.0")
with urlopen(req) as resp:
    print(resp.status)
```

---

## urllib.parse URL 解析

**基本写法：urlparse 拆分 URL**
`urllib.parse.urlparse(<URL>)`
```python
# 拆分 URL 各部分
from urllib.parse import urlparse

r = urlparse("https://user:pass@host.com:8080/path?q=1#frag")
print(r.scheme, r.netloc, r.path, r.query, r.fragment)
```

**基本写法：urlunparse 组合**
`urllib.parse.urlunparse(<六元组>)`
```python
# 组合 URL
parts = ("https", "host.com", "/path", "", "q=1", "")
print(urlunparse(parts))
```

**基本写法：urljoin 拼接**
`urllib.parse.urljoin(<基础>, <相对>)`
```python
# 拼接基础与相对 URL
print(urljoin("https://host.com/a/b/", "../c"))
# https://host.com/a/c
```

**基本写法：urlencode 编码查询**
`urllib.parse.urlencode(<字典>)`
```python
# 字典转查询字符串
from urllib.parse import urlencode

print(urlencode({"name": "Alice", "age": 18}))
# name=Alice&age=18
```

**基本写法：urlencode 多值**
`urlencode(<字典>, doseq=True)`
```python
# 多值参数
print(urlencode({"tag": ["a", "b"]}, doseq=True))
# tag=a&tag=b
```

**基本写法：parse_qs 解析查询**
`urllib.parse.parse_qs(<查询串>)`
```python
# 解析查询字符串为字典
from urllib.parse import parse_qs

print(parse_qs("name=Alice&tag=a&tag=b"))
# {"name": ["Alice"], "tag": ["a", "b"]}
```

**基本写法：parse_qsl 列表形式**
`urllib.parse.parse_qsl(<查询串>)`
```python
# 解析为键值对列表
print(parse_qsl("name=Alice&age=18"))
# [("name", "Alice"), ("age", "18")]
```

**基本写法：quote URL 编码**
`urllib.parse.quote(<字符串>)`
```python
# 编码特殊字符
from urllib.parse import quote

print(quote("hello world&test"))
# hello%20world%26test
```

**基本写法：quote_plus 空格转加号**
`urllib.parse.quote_plus(<字符串>)`
```python
# 空格编码为 +
print(quote_plus("hello world"))
# hello+world
```

**基本写法：unquote 解码**
`urllib.parse.unquote(<字符串>)`
```python
# 解码 URL 编码
from urllib.parse import unquote

print(unquote("hello%20world"))
# hello world
```

**基本写法：urlsplit**
`urllib.parse.urlsplit(<URL>)`
```python
# 拆分为五元组（不拆 params）
r = urlsplit("https://host.com/path?q=1")
print(r)
```

---

## urllib.error 异常

**基本写法：URLError**
`except urllib.error.URLError:`
```python
# 捕获 URL 错误
from urllib.error import URLError, HTTPError

try:
    urlopen("https://invalid.invalid")
except URLError as e:
    print("URL 错误:", e.reason)
```

**基本写法：HTTPError**
`except urllib.error.HTTPError:`
```python
# 捕获 HTTP 错误（含状态码）
try:
    urlopen("https://httpbin.org/status/404")
except HTTPError as e:
    print(e.code, e.reason)
```

---

## urllib.request 高级

**基本写法：BaseHandler 与 Opener**
`urllib.request.build_opener(<处理器>)`
```python
# 自定义 opener
from urllib.request import build_opener, HTTPCookieProcessor, HTTPHandler

opener = build_opener(HTTPCookieProcessor(), HTTPHandler())
resp = opener.open("https://www.python.org")
```

**基本写法：HTTPBasicAuthHandler 认证**
`urllib.request.HTTPPasswordMgrWithDefaultRealm()`
```python
# HTTP 基本认证
import urllib.request

pwd_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwd_mgr.add_password(None, "https://host.com", "user", "pass")
auth = urllib.request.HTTPBasicAuthHandler(pwd_mgr)
opener = urllib.request.build_opener(auth)
resp = opener.open("https://host.com/protected")
```

**基本写法：ProxyHandler 代理**
`urllib.request.ProxyHandler(<代理字典>)`
```python
# 设置代理
proxy = urllib.request.ProxyHandler({"http": "http://proxy:8080"})
opener = urllib.request.build_opener(proxy)
```

**基本写法：HTTPCookieProcessor Cookie**
`http.cookiejar.CookieJar()`
```python
# 自动管理 Cookie
import http.cookiejar

jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
resp = opener.open("https://httpbin.org/cookies/set?name=Alice")
```

---

## 下载文件

**基本写法：urlretrieve 下载**
`urllib.request.urlretrieve(<URL>, <文件路径>)`
```python
# 下载到本地文件
from urllib.request import urlretrieve

filename, headers = urlretrieve("https://www.python.org/static/img/python-logo.png", "logo.png")
print(filename)
```
