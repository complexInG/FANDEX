# Lua 调试库与排错

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 错误抛出

**基本写法：抛出错误**
`error("<消息>" [, <层级>])`
```lua
-- 抛出错误中断执行
error("参数不能为空")
```

---

**基本写法：带层级的错误**
`error("<消息>", <层级>)`
```lua
-- 层级 1 指向 error 调用处，2 指向调用者
error("调用方出错", 2)  -- 错误指向调用此函数的地方
```

---

**基本写法：抛出非字符串**
`error(<表>)`
```lua
-- 抛出任意值作为错误对象
error({ code = 500, msg = "服务器错误" })
```

---

**基本写法：assert 断言**
`assert(<条件> [, "<消息>"])`
```lua
-- 条件为 nil/false 时抛错
assert(x ~= nil, "x 不能为 nil")
local f = assert(io.open("data.txt", "r"))
```

---

## 错误捕获

**基本写法：pcall 保护调用**
`local <ok>, <结果> = pcall(<函数>, <参数>...)`
```lua
-- 捕获错误不中断程序
local ok, result = pcall(function(a, b)
    return a / b
end, 10, 0)
if not ok then print("出错:", result) end
```

---

**基本写法：pcall 调用已有函数**
`pcall(<函数>, <参数>...)`
```lua
-- 直接传函数与参数
local ok, val = pcall(tonumber, "abc")
if not ok then print("转换失败") end
```

---

**基本写法：xpcall 带处理函数**
`xpcall(<函数>, <错误处理>, <参数>...)`
```lua
-- 错误发生时调用处理函数获取栈信息
local ok, result = xpcall(function()
    return risky()
end, function(err)
    return debug.traceback("错误: " .. tostring(err), 2)
end)
```

---

**基本写法：pcall vs xpcall**
`-- pcall 仅返回错误，xpcall 可获取栈回溯`
```lua
-- pcall：错误对象不含调用栈
-- xpcall：错误处理器可在栈展开前抓取 traceback
```

---

## traceback 栈回溯

**基本写法：获取调用栈**
`debug.traceback(["<消息>" [, <层级>]])`
```lua
-- 返回当前调用栈字符串
local trace = debug.traceback("出错了", 2)
print(trace)
```

---

**基本写法：异常中获取栈**
`xpcall(<函数>, function(<err>) return debug.traceback(<err>, 2) end)`
```lua
-- 在错误处理函数中抓栈
local ok, err = xpcall(function()
    error("test")
end, function(e)
    return debug.traceback(e, 2)
end)
print(err)
```

---

## 调试信息

**基本写法：获取函数信息**
`debug.getinfo(<函数或层级> [, "<选项>"])`
```lua
-- 返回包含函数信息的表
local info = debug.getinfo(1, "Slu")
print(info.source)  -- 源文件
print(info.currentline)  -- 当前行
print(info.what)   -- "Lua"/"C"/"main"
```

---

**基本写法：info 选项速查**
`"<选项字符>"`
```lua
-- "S" 源信息    source short_src what linedefined lastlinedefined
-- "l" 当前行    currentline
-- "u" 上值信息  nups nparams isvararg
-- "n" 名称      name namewhat
-- "f" 函数本身  func
-- "L" 活动行    activelines
```

---

**基本写法：获取局部变量**
`debug.getlocal(<层级>, <序号>)`
```lua
-- 获取指定栈层的局部变量
local name, value = debug.getlocal(1, 1)
while name do
    print(name, value)
    name, value = debug.getlocal(1, 1 + 0)
    break
end
```

---

**基本写法：遍历所有局部变量**
`for <i> = 1, math.huge do end`
```lua
-- 遍历某层所有局部变量
local i = 1
while true do
    local name, value = debug.getlocal(2, i)
    if not name then break end
    print(name, value)
    i = i + 1
end
```

---

**基本写法：设置局部变量**
`debug.setlocal(<层级>, <序号>, <值>)`
```lua
-- 修改局部变量的值
debug.setlocal(1, 1, "new value")
```

---

**基本写法：获取上值**
`debug.getupvalue(<函数>, <序号>)`
```lua
-- 获取闭包的上值
local name, value = debug.getupvalue(func, 1)
```

---

**基本写法：设置上值**
`debug.setupvalue(<函数>, <序号>, <值>)`
```lua
-- 修改闭包的上值
debug.setupvalue(func, 1, newvalue)
```

---

## 调试钩子

**基本写法：设置钩子**
`debug.sethook(<函数>, "<事件>" [, <行数>])`
```lua
-- 设置调试钩子，事件：c call l r
debug.sethook(function(event)
    print("事件:", event, debug.getinfo(2).currentline)
end, "cr")  -- c 函数调用 r 返回
```

---

**基本写法：行计数钩子**
`debug.sethook(<函数>, "l", <行数间隔>)`
```lua
-- 每隔 N 行触发一次
debug.sethook(function()
    print("执行到:", debug.getinfo(2).currentline)
end, "l", 100)
```

---

**基本写法：获取当前钩子**
`debug.gethook()`
```lua
-- 返回当前钩子函数、事件与计数
local hook, mask, count = debug.gethook()
```

---

**基本写法：移除钩子**
`debug.sethook()`
```lua
-- 传 nil 取消钩子
debug.sethook()
```

---

## 注册表操作

**基本写法：访问注册表**
`debug.getregistry()`
```lua
-- 返回 Lua 注册表（全局共享表）
local reg = debug.getregistry()
-- reg[1] 等存放 C 侧引用的对象
```

---

## 元表调试

**基本写法：获取元表**
`debug.getmetatable(<值>)`
```lua
-- 获取值的元表（绕过 __metatable 保护）
local mt = debug.getmetatable(obj)
```

---

**基本写法：设置元表**
`debug.setmetatable(<值>, <元表>)`
```lua
-- 强制设置元表（绕过 __metatable 保护）
debug.setmetatable(obj, newmt)
```

---

## 调试实用函数

**基本写法：类型判断增强**
`<函数>.what = debug.getinfo(<函数>).what`
```lua
-- 判断函数来源是 Lua 还是 C
local info = debug.getinfo(somefunc, "S")
if info.what == "C" then
    print("C 函数")
elseif info.what == "Lua" then
    print("Lua 函数")
end
```

---

**基本写法：打印调用栈**
`local function <名>() end`
```lua
-- 自定义栈打印工具
local function print_stack()
    local level = 2
    while true do
        local info = debug.getinfo(level, "Sl")
        if not info then break end
        print(string.format("%s:%d", info.short_src, info.currentline))
        level = level + 1
    end
end
```

---

## 调试器基础

**基本写法：简单断点实现**
`debug.sethook(<函数>, "l")`
```lua
-- 用行钩子实现断点
local breakpoints = { ["/path/file.lua"] = { [10] = true } }
debug.sethook(function(_, line)
    local info = debug.getinfo(2, "S")
    if breakpoints[info.short_src] and breakpoints[info.short_src][line] then
        print("命中断点:", info.short_src, line)
        debug.debug()  -- 进入交互调试
    end
end, "l")
```

---

**基本写法：交互调试提示**
`debug.debug()`
```lua
-- 进入内置交互调试器，输入 cont 退出
debug.debug()
```

---

## 常见排错模式

**基本写法：封装安全调用**
`local function <名>(<函数>, ...)`
```lua
-- 统一错误处理封装
local function safe_call(fn, ...)
    local ok, result = pcall(fn, ...)
    if not ok then
        print("[ERROR]", result)
        return nil
    end
    return result
end
```

---

**基本写法：资源清理保护**
`pcall(function() end) + finally`
```lua
-- 模拟 try-finally
local function try_finally(body, cleanup)
    local ok, err = pcall(body)
    cleanup()
    if not ok then error(err) end
end
```

---

**基本写法：可选参数校验**
`assert(type(<参数>) == "<类型>", "<消息>")`
```lua
-- 参数类型检查
local function add(a, b)
    assert(type(a) == "number", "a 必须为数字")
    assert(type(b) == "number", "b 必须为数字")
    return a + b
end
```
