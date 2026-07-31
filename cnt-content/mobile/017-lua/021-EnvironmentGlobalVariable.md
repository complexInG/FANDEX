# Lua 环境与全局变量

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## _G 全局表

**基本写法：访问 _G**
`_G`
```lua
-- _G 是全局环境表
print(_G.print)       -- function
_G.x = 10             -- 等价于 x = 10
print(x)              -- 10
print(_G["x"])        -- 10
```

---

**基本写法：遍历全局变量**
`for k, v in pairs(_G) do ... end`
```lua
-- 遍历所有全局变量
for k, v in pairs(_G) do
    print(k, type(v))
end
-- 输出：print function, string table, math table 等
```

---

**基本写法：动态访问全局**
`_G[<变量名>]`
```lua
-- 按名称字符串访问全局
local name = "print"
_G[name]("hello")  -- 等价于 print("hello")
-- 动态设置
_G["myVar"] = 42
print(myVar)  -- 42
```

---

## _ENV 与 _G 的关系

**基本写法：5.1 _G vs 5.2+ _ENV**
`_G` / `_ENV`
```lua
-- Lua 5.1：_G 是真正的全局表
-- Lua 5.2+：_ENV 是当前环境（upvalue），_G 是 _ENV._G
-- 默认 _ENV == _G
print(_ENV == _G)  -- true（默认情况）
-- 修改 _ENV 后 _G 不可直接访问
local _ENV = {}
-- print(_G)  -- 错误：_G 不在新环境中
```

---

## 全局变量声明

**基本写法：隐式全局变量**
`<变量名> = <值>`
```lua
-- 未加 local 即为全局变量
x = 10           -- 全局
local y = 20     -- 局部
function f() end -- 全局函数
local function g() end  -- 局部函数（推荐）
```

---

**基本写法：global 关键字（Lua 5.5）**
`global <变量名>`
```lua
-- Lua 5.5 显式声明全局变量
global config
config = { debug = true }
-- 开启严格模式后必须先 global 声明
```

---

**基本写法：严格模式检测**
`<元表>.__index = <函数>`
```lua
-- 检测未声明的全局变量访问
setmetatable(_G, {
    __index = function(t, k)
        error("访问未定义的全局变量: " .. k, 2)
    end,
    __newindex = function(t, k, v)
        error("禁止创建全局变量: " .. k, 2)
    end
})
-- x = 10  -- 错误：禁止创建全局变量
```

---

## 局部变量优先

**基本写法：local 遮蔽全局**
`local <变量> = <值>`
```lua
-- 局部变量遮蔽同名全局
x = 10
local x = 20
print(x)  -- 20（局部优先）
-- 访问全局用 _G
print(_G.x)  -- 10
```

---

**基本写法：local 作用域**
`local <变量>; do local <变量> = <值> end`
```lua
-- 局部变量作用域限定
do
    local temp = compute()
    useTemp(temp)
end
-- temp 在此处不可访问，可被 GC
-- 减少全局污染
```

---

## 全局变量管理

**基本写法：导出 API**
`<模块>.<API> = <函数>`
```lua
-- 模块化导出而非全局
local M = {}
function M.api() return "public" end
-- 而非
-- function api() return "public" end  -- 全局污染
return M
```

---

**基本写法：清空全局**
`_G[<名>] = nil`
```lua
-- 删除全局变量
config = { ... }
-- 使用完毕
_G.config = nil
config = nil  -- 也可以
-- 注意：nil 后该变量变为 nil
```

---

## 全局表与性能

**基本写法：局部化全局**
`local <别名> = <全局>`
```lua
-- 频繁访问的全局变量局部化（性能优化）
local print = print      -- 缓存全局函数
local table_insert = table.insert
local string_format = string.format
-- 循环中使用局部别名更快
for i = 1, 1000 do
    print(i)  -- 局部查找，比全局快
end
```

---

## getfenv / setfenv（Lua 5.1）

**基本写法：获取函数环境**
`getfenv(<函数或层级>)`
```lua
-- Lua 5.1 专用
local env = getfenv(1)  -- 当前函数环境
print(env == _G)  -- true
```

---

**基本写法：设置函数环境**
`setfenv(<函数或层级>, <环境表>)`
```lua
-- Lua 5.1 设置环境
local env = { print = print, x = 10 }
local f = function() return x end
setfenv(f, env)
print(f())  -- 10
-- Lua 5.2+ 用 _ENV 替代
```

---

## 调试与环境

**基本写法：debug.getfenv**
`debug.getfenv(<函数或值>)`
```lua
-- 获取值的环境（兼容版本）
local env = debug.getfenv(func)
print(env)
```

---

**基本写法：debug.setfenv**
`debug.setfenv(<函数或值>, <环境>)`
```lua
-- 设置环境（兼容方式）
local newEnv = { print = print }
debug.setfenv(func, newEnv)
```
