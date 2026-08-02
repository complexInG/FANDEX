---
order: 350
title: Lua io 库语法速查手册
module: 'lua'
category: 后端技术
difficulty: beginner
description: Lua io 库语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## 标准输入输出

**基本写法：读取标准输入**
`io.read([<格式>])`
```lua
-- 默认读取一行
local line = io.read()           -- 读一行字符串
local n = io.read("*n")          -- 读一个数字
local all = io.read("*a")        -- 读全部内容（Lua 5.3+）
local char = io.read(1)          -- 读 1 个字符
local block = io.read(1024)      -- 读 1024 字节
```

---

**基本写法：写入标准输出**
`io.write(<参数>...)`
```lua
-- 写入标准输出，不自动换行
io.write("hello", " ", "world", "\n")
io.write(string.format("count=%d\n", 42))
```

---

**基本写法：标准读行迭代器**
`io.lines([<文件名>])`
```lua
-- 不传文件名：迭代标准输入
for line in io.lines() do
    print(line)
end

-- 传文件名：迭代文件后自动关闭
for line in io.lines("data.txt") do
    print(line)
end
```

---

## 默认输入输出流

**基本写法：设置默认输入流**
`io.input([<文件或句柄>])`
```lua
-- 设置默认输入文件，后续 io.read 从该文件读
io.input("input.txt")         -- 打开文件作为默认输入
local f = io.open("x.txt", "r")
io.input(f)                   -- 设置句柄为默认输入
io.input():read("*l")         -- 当前默认输入流
```

---

**基本写法：设置默认输出流**
`io.output([<文件或句柄>])`
```lua
-- 设置默认输出文件，后续 io.write 写入该文件
io.output("log.txt")
io.write("日志内容\n")
```

---

## 文件打开与关闭

**基本写法：打开文件**
`io.open(<文件名> [, <模式>])`
```lua
-- 返回文件句柄，失败返回 nil 加错误信息
local f, err = io.open("data.txt", "r")
if not f then error(err) end

-- 模式速查
-- "r"  只读（默认）   "w"  覆盖写   "a"  追加写
-- "r+" 读写           "w+" 覆盖读写  "a+" 追加读写
-- "rb" 二进制只读     "wb" 二进制写  "ab" 二进制追加
```

---

**基本写法：关闭文件**
`<f>:close()` 或 `io.close([<f>])`
```lua
-- 关闭文件句柄
f:close()
io.close(f)             -- 等价写法
io.close()              -- 关闭默认输出流
```

---

## 句柄读写方法

**基本写法：按行读取**
`<f>:read([<格式>...])`
```lua
-- 常用格式
f:read("*l")     -- 读一行（默认，不含换行符）
f:read("*L")     -- 读一行（含换行符，Lua 5.2+）
f:read("*n")     -- 读一个数字
f:read("*a")     -- 读全部剩余内容
f:read(5)        -- 读 5 个字符
f:read("*n", "*l")  -- 一次读多个
```

---

**基本写法：写入文件**
`<f>:write(<参数>...)`
```lua
-- 写入字符串或数字
f:write("name=", name, "\n")
f:write(42, " ", 3.14, "\n")
```

---

**基本写法：按行迭代**
`<f>:lines()`
```lua
-- 返回迭代器，遍历结束后自动关闭句柄
for line in f:lines() do
    print(line)
end
```

---

## 文件指针

**基本写法：定位文件指针**
`<f>:seek([<whence>] [, <偏移>])`
```lua
-- 设置或获取文件位置
f:seek("set", 0)      -- 从文件头偏移 0（回到开头）
f:seek("cur", 10)     -- 从当前位置后移 10 字节
f:seek("end", -5)     -- 从末尾前移 5 字节
local pos = f:seek()  -- 不带参返回当前位置
```

---

**基本写法：刷新缓冲区**
`<f>:flush()` 或 `io.flush()`
```lua
-- 把缓冲数据写入磁盘
f:flush()
io.flush()           -- 刷新默认输出流
```

---

**基本写法：设置缓冲模式**
`<f>:setvbuf(<模式> [, <大小>])`
```lua
-- 缓冲模式
f:setvbuf("no")       -- 无缓冲
f:setvbuf("line")     -- 行缓冲（默认终端）
f:setvbuf("full", 4096)  -- 全缓冲，缓冲区 4KB
```

---

## 其他常用

**基本写法：获取文件句柄类型**
`io.type(<对象>)`
```lua
-- 判断对象是否为文件句柄
io.type(f)        -- "file"   打开的句柄
io.type(closed_f) -- "closed file"  已关闭
io.type(42)       -- nil  非句柄
```

---

**基本写法：弹出管道执行命令**
`io.popen(<命令> [, <模式>])`
```lua
-- 执行命令并返回管道句柄（读其输出或写其输入）
local h = io.popen("ls -la", "r")
local output = h:read("*a")
h:close()

local w = io.popen("cat > out.txt", "w")
w:write("写入管道\n")
w:close()
```

---

## 注意事项速查

**基本写法：二进制模式与换行**
`io.open(<文件>, "rb")`
```lua
-- Windows 下文本模式会做 \r\n 转换
-- 处理二进制数据必须用 b 模式
local f = io.open("img.png", "rb")
local data = f:read("*a")
f:close()
```
