---
order: 320
title: Lua 文件 IO 进阶
module: 'lua'
category: 后端技术
difficulty: beginner
description: Lua 文件 IO 进阶 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## 文件打开与模式

**基本写法：以追加模式打开**
`local <f> = io.open("<路径>", "a")`
```lua
-- 追加写入，文件不存在则创建
local f = io.open("log.txt", "a")
```

---

**基本写法：二进制模式打开**
`local <f> = io.open("<路径>", "rb")`
```lua
-- 二进制读取，Windows 下避免换行转换
local f = io.open("data.bin", "rb")
```

---

**基本写法：读写模式打开**
`local <f> = io.open("<路径>", "r+")`
```lua
-- 读写共用同一文件句柄
local f = io.open("data.txt", "r+")
```

---

**基本写法：模式速查**
`<模式字符>`
```lua
-- r  读（默认）
-- w  覆盖写
-- a  追加写
-- r+ 读写不新建
-- w+ 读写覆盖
-- a+ 读写追加
-- b 附加二进制标记：rb wb a+b
```

---

## 写入操作

**基本写法：格式化写入**
`<f>:write(string.format(<格式>, <参数>))`
```lua
-- 写入格式化数据
local f = io.open("data.txt", "w")
f:write(string.format("count=%d\n", 100))
f:close()
```

---

**基本写法：写入多行**
`<f>:write(<串1>, <串2>, ...)`
```lua
-- 一次写入多个字符串
f:write("line1\n", "line2\n", "line3\n")
```

---

**基本写法：刷新缓冲**
`<f>:flush()`
```lua
-- 立即把缓冲写入磁盘
f:write("data")
f:flush()
```

---

## 读取操作

**基本写法：读取数字格式**
`<f>:read("<格式>")`
```lua
-- 按格式读取
local n = f:read("*n")  -- 读取一个数字
local s = f:read("*a")  -- 读取全部内容
local l = f:read("*l")  -- 读取一行（不含换行）
```

---

**基本写法：读取固定字节数**
`<f>:read(<数量>)`
```lua
-- 读取指定字节数
local chunk = f:read(1024)
```

---

**基本写法：read 多格式混合**
`<f>:read(<格式1>, <格式2>, ...)`
```lua
-- 一次读取多个字段
local name, age = f:read("*l", "*n")
```

---

**基本写法：格式速查**
`<read 格式>`
```lua
-- "*a"  读取全部
-- "*l"  读取一行（5.3 前默认）
-- "*L"  读取一行含换行（5.3+）
-- "*n"  读取数字
-- 数字  读取指定字节数
```

---

## 文件指针定位

**基本写法：移动指针 seek**
`<f>:seek("<模式>" [, <偏移>])`
```lua
-- 移动读写位置
f:seek("set", 0)   -- 移到开头
f:seek("end")      -- 移到末尾
f:seek("cur", 10)  -- 当前位置后移 10 字节
```

---

**基本写法：获取当前指针**
`local <pos> = <f>:seek()`
```lua
-- 不带参数返回当前位置
local pos = f:seek()
```

---

**基本写法：获取文件大小**
`local <size> = <f>:seek("end")`
```lua
-- 移到末尾即得到文件大小
local size = f:seek("end")
f:seek("set", 0)  -- 复位
```

---

## 默认输入输出

**基本写法：重定向标准输入**
`io.input(<文件>)`
```lua
-- 设置默认输入文件
local f = io.open("in.txt", "r")
io.input(f)
local line = io.read()  -- 读取自 in.txt
```

---

**基本写法：重定向标准输出**
`io.output(<文件>)`
```lua
-- 设置默认输出文件
local f = io.open("out.txt", "w")
io.output(f)
io.write("输出到文件而非控制台\n")
```

---

**基本写法：标准输入读取**
`io.read()`
```lua
-- 从默认输入读取
local line = io.read()
```

---

**基本写法：标准输出写入**
`io.write(<串>)`
```lua
-- 写入默认输出，不带换行
io.write("hello", " ", "world")
```

---

## 行迭代

**基本写法：逐行处理大文件**
`for <line> in io.lines("<路径>") do end`
```lua
-- 惰性逐行读取，内存占用低
for line in io.lines("big.log") do
    if line:find("ERROR") then print(line) end
end
```

---

**基本写法：带行号迭代**
`for <n>, <line> in <迭代> do end`
```lua
-- 自定义带行号迭代
local i = 0
for line in io.lines("file.txt") do
    i = i + 1
    print(i, line)
end
```

---

**基本写法：从已打开文件迭代**
`<f>:lines()`
```lua
-- 从文件句柄逐行迭代
for line in f:lines() do
    print(line)
end
```

---

## 临时文件

**基本写法：创建临时文件**
`local <f> = io.tmpfile()`
```lua
-- 创建临时文件，关闭后自动删除
local tmp = io.tmpfile()
tmp:write("temp data")
tmp:seek("set", 0)
```

---

**基本写法：临时文件名**
`os.tmpname()`
```lua
-- 仅返回临时文件名，需自行打开
local name = os.tmpname()
local f = io.open(name, "w")
```

---

## 文件与目录管理

**基本写法：删除文件**
`os.remove("<路径>")`
```lua
-- 删除文件，返回是否成功
local ok, err = os.remove("temp.txt")
```

---

**基本写法：重命名移动**
`os.rename("<旧>", "<新>")`
```lua
-- 重命名或移动文件
local ok, err = os.rename("a.txt", "b.txt")
```

---

**基本写法：执行命令**
`os.execute("<命令>")`
```lua
-- 通过 shell 操作目录
os.execute("mkdir -p newdir")
os.execute("rmdir emptydir")
```

---

## 二进制读写

**基本写法：写入二进制数字**
`string.pack("<格式>", <值>)`
```lua
-- 5.3+ string.pack 打包二进制
local f = io.open("d.bin", "wb")
f:write(string.pack("i4", 12345))
f:close()
```

---

**基本写法：读取二进制数字**
`string.unpack("<格式>", <串>)`
```lua
-- 解包二进制数据
local f = io.open("d.bin", "rb")
local data = f:read("*a")
local n = string.unpack("i4", data)
f:close()
```

---

**基本写法：pack 格式速查**
`<pack 格式>`
```lua
-- i4  4 字节有符号整数
-- I4  4 字节无符号整数
-- f   单精度浮点
-- d   双精度浮点
-- <   小端序
-- >   大端序
-- =   原生字节序
```

---

## 完整文件读写模式

**基本写法：一次性读取整个文件**
`local <内容> = io.open("<路径>"):read("*a")`
```lua
-- 打开即读取并关闭（需注意释放）
local f = io.open("config.json", "r")
local content = f:read("*a")
f:close()
```

---

**基本写法：安全打开封装**
`local <内容> = read_all("<路径>")`
```lua
-- 自带错误处理的读取封装
local function read_all(path)
    local f, err = io.open(path, "r")
    if not f then return nil, err end
    local s = f:read("*a")
    f:close()
    return s
end
```

---

**基本写法：错误处理打开**
`local <f>, <err> = io.open("<路径>", "r")`
```lua
-- 检查是否打开成功
local f, err = io.open("data.txt", "r")
if not f then
    error("打开失败: " .. err)
end
```

---

## io 库与 with 风格封装

**基本写法：自动关闭封装**
`local function <名>(<路径>, <回调>)`
```lua
-- 模拟 with 语义确保关闭
local function with_file(path, mode, fn)
    local f = assert(io.open(path, mode))
    local ok, result = pcall(fn, f)
    f:close()
    if not ok then error(result) end
    return result
end
```

---

**基本写法：Lua 5.4 close 变量自动关闭**
`local <f> <close> = io.open(...)`
```lua
-- Lua 5.4 变量出作用域自动 close
do
    local f <close> = io.open("data.txt", "r")
    local content = f:read("*a")
end -- 离开块自动调用 __close
```

## 延伸阅读
Lua 与 Redis 脚本，见 022-redis 模块相关文档。
Lua 与 OpenResty 网关，见 031-devops 模块相关文档。
游戏开发与脚本扩展，见 017-lua 模块文档。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 元表与面向对象

用 table 模拟类：构造函数返回新表，__index 指向类表实现继承；冒号语法 self 绑定。
类继承链：子类 __index 指向父类实例/类表；方法查找沿链上行。
多态与组合：元方法 __call 让 table 可调用；__tostring 控制输出。
工程建议：对象体系保持浅继承，优先组合；性能敏感路径避免动态派发。

### 13.2 Lua C API 集成

宿主初始化 lua_State，注册 C 函数（lua_pushcfunction），调用 lua_pcall 执行脚本并处理错误。
值传递通过栈：lua_pushnumber/lua_tointeger 等；返回值按栈顺序返回。
用户数据（userdata）包装 C 对象，配合元表实现面向对象接口。
安全：限制可用库（require 白名单）、执行超时（debug.sethook）与内存上限。
