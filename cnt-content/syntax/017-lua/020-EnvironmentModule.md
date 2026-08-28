# Lua 环境与模块

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## _ENV 环境（Lua 5.2+）

**基本写法：访问 _ENV**
`_ENV`
```lua
-- _ENV 是当前代码块的环境表
-- 所有全局变量访问实际是 _ENV 的字段
print(_ENV.print)  -- 与 print 相同
-- _ENV 本身不是全局变量，是语法上的 upvalue
```

---

**基本写法：修改环境**
`_ENV = <表>`
```lua
-- 切换当前代码块的环境
local env = { print = print, x = 10 }
_ENV = env
print(x)        -- 10（从 env 取）
-- print(_G)    -- 错误：_G 不在 env 中
```

---

**基本写法：load 指定环境**
`load(<代码>, [, <名字> [, <模式> [, <环境>]]])`
```lua
-- load 第五参数指定环境（Lua 5.2）
local code = "return x + 1"
local f = load(code, "chunk", "t", { x = 10, math = math })
print(f())  -- 11
-- Lua 5.1 用 setfenv 设置
```

---

## 沙箱环境

**基本写法：创建沙箱**
`local <env> = {}; <env>.<安全函数> = <原始>`
```lua
-- 构造受限环境执行不可信代码
local function sandbox(code)
    local env = {}
    -- 白名单暴露安全函数
    env.print = print
    env.math = math
    env.string = string
    env.table = table
    -- 执行
    local fn = load(code, "sandbox", "t", env)
    if fn then fn() end
end
sandbox("print(math.pi)")  -- 3.14159...
-- sandbox("os.execute('rm -rf /')")  -- 错误：os 不存在
```

---

**基本写法：_ENV 沙箱模式**
`local _ENV = <受限表>`
```lua
-- 直接在代码块内限制环境
local function run(code)
    local _ENV = { print = print }
    local f = load(code)
    setfenv(f, _ENV)  -- Lua 5.1
    f()
end
```

---

## 模块定义

**基本写法：module 函数（旧式）**
`module("<名>")`
```lua
-- Lua 5.1 旧式模块定义（已不推荐）
module("mymod")
function hello() print("hi") end
-- 调用：mymod.hello()
```

---

**基本写法：现代模块模式**
`local <模块> = {}; ... return <模块>`
```lua
-- 推荐的现代模块定义
local M = {}  -- 模块表

function M.greet(name)
    return "hello, " .. name
end

M.version = "1.0"

return M
-- 保存为 mymod.lua
-- 使用：local mymod = require("mymod")
```

---

**基本写法：模块元方法**
`setmetatable(<模块>, <元表>)`
```lua
-- 模块可调用（__call）
local M = setmetatable({}, {
    __call = function(self, x)
        return x * 2
    end
})
M(5)  -- 10，模块本身可调用
return M
```

---

## require 加载

**基本写法：require 基础**
`require("<模块名>")`
```lua
-- 加载模块（只执行一次）
local mod = require("mymod")
-- 多次 require 只加载一次
local mod2 = require("mymod")  -- 返回缓存
-- 返回值缓存于 package.loaded
```

---

**基本写法：package.loaded 缓存**
`package.loaded["<模块>"]`
```lua
-- 查看或清除模块缓存
print(package.loaded.mymod)  -- 模块表或 nil
package.loaded.mymod = nil   -- 清除缓存，下次重新加载
-- 强制重载
package.loaded.mymod = nil
require("mymod")
```

---

**基本写法：package.path 搜索路径**
`package.path`
```lua
-- 模块搜索路径
print(package.path)
-- 格式：./?.lua;./?/init.lua;/usr/share/lua/5.4/?.lua;...
-- 添加自定义路径
package.path = "./lib/?.lua;" .. package.path
local mymod = require("lib.utils")  -- 查找 ./lib/lib/utils.lua
```

---

**基本写法：package.cpath C 模块路径**
`package.cpath`
```lua
-- C 扩展模块搜索路径
print(package.cpath)
-- 添加路径
package.cpath = "./lib/?.so;" .. package.cpath
local cmod = require("cutils")  -- 查找 cutils.so
```

---

## package 搜索器

**基本写法：package.searchers**
`package.searchers`
```lua
-- 模块加载器列表（Lua 5.2+）
-- 依次尝试每个搜索器
for i, searcher in ipairs(package.searchers) do
    print(i, searcher)
end
-- 1. package.preload 预加载
-- 2. package.path Lua 文件
-- 3. package.cpath C 库
-- 4. 内置加载器
```

---

**基本写法：package.preload 预加载**
`package.preload["<名>"] = <函数>`
```lua
-- 预注册模块加载函数
package.preload.mymod = function()
    local M = {}
    function M.hello() return "hi" end
    return M
end
local m = require("mymod")  -- 调用 preload 函数
```

---

## 模块重载

**基本写法：热重载**
`package.loaded[<名>] = nil; require(<名>)`
```lua
-- 开发时热重载模块
function reloadModule(name)
    package.loaded[name] = nil
    return require(name)
end
-- 注意：已引用旧模块的代码不会更新
```

---

## 子模块

**基本写法：点号子模块**
`require("<父>.<子>")`
```lua
-- 点号表示目录层级
local utils = require("myapp.utils")
-- 搜索 myapp/utils.lua 或 myapp/utils/init.lua
-- 返回的模块表可以挂到父模块
local myapp = require("myapp")
myapp.utils = utils
```
