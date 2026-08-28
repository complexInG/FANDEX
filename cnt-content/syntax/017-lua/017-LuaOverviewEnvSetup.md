# Lua 概览与环境配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 命令行运行

**基本写法：执行脚本**
`lua <脚本>`
```bash
// 运行指定 Lua 脚本
lua hello.lua
```

---

**基本写法：执行字符串**
`lua -e "<代码>"`
```bash
// 直接执行一段 Lua 代码
lua -e "print('hello')"
```

---

**基本写法：交互模式**
`lua -i`
```bash
// 进入交互式 REPL
lua -i
```

---

**基本写法：加载后进入交互**
`lua -i <脚本>`
```bash
// 先执行脚本再进入交互
lua -i init.lua
```

---

**基本写法：传递参数**
`lua <脚本> <参数1> <参数2>`
```bash
// 命令行参数在 arg 表中
lua app.lua --port 8080
```

---

**基本写法：获取脚本名与参数**
`arg[0] | arg[1]`
```lua
-- arg[0] 是脚本名，arg[1] 起为参数
print(arg[0])  -- 脚本路径
print(arg[1])  -- 第一个参数
print(#arg)    -- 参数个数
```

---

**基本写法：检查选项**
`lua -v`
```bash
// 输出 Lua 版本
lua -v
```

---

## 解释器 luac

**基本写法：编译为字节码**
`luac -o <输出> <脚本>`
```bash
// 预编译为字节码文件
luac -o out.luac hello.lua
```

---

**基本写法：列出字节码**
`luac -l <脚本>`
```bash
// 反汇编显示字节码清单
luac -l hello.lua
```

---

**基本写法：运行字节码**
`lua <字节码文件>`
```bash
// 直接运行预编译文件
lua out.luac
```

---

**基本写法：合并多个文件**
`luac -o <输出> <文件1> <文件2>`
```bash
// 多个源文件打包为一个字节码
luac -o app.luac a.lua b.lua c.lua
```

---

## 环境变量与版本

**基本写法：获取 Lua 版本**
`_VERSION`
```lua
-- 全局变量返回版本字符串
print(_VERSION)  -- Lua 5.4
```

---

**基本写法：获取版本号**
`tonumber((_VERSION:gsub("Lua ", "")))`
```lua
-- 提取数字版本用于判断
local ver = tonumber((_VERSION:gsub("Lua ", "")))
if ver >= 5.4 then print("支持 const/close") end
```

---

**基本写法：设置 LUA_PATH**
`export LUA_PATH="<路径>"`
```bash
// 设置模块搜索路径（bash）
export LUA_PATH="./?.lua;./?/init.lua"
```

---

**基本写法：设置 LUA_CPATH**
`export LUA_CPATH="<路径>"`
```bash
// 设置 C 模块搜索路径
export LUA_CPATH="./?.so;./?.dll"
```

---

**基本写法：查看默认路径**
`package.path | package.cpath`
```lua
-- 查看 Lua 模块与 C 模块搜索路径
print(package.path)
print(package.cpath)
```

---

## 注释

**基本写法：单行注释**
`-- <注释内容>`
```lua
-- 这是一行注释
local x = 10
```

---

**基本写法：多行注释**
`--[[ <内容> ]]`
```lua
--[[
多行注释内容
可以跨多行
]]
```

---

**基本写法：可切换注释**
`--[=[ <内容> ]=]`
```lua
-- 用等号数量控制层级
--[==[
这仍然是注释
]==]
-- 加一个 - 即可启用代码
---[[ print("生效") --]]
```

---

## 命名规范

**基本写法：标识符规则**
`<字母|下划线> <字母数字下划线>*`
```lua
-- 由字母、数字、下划线组成，不能以数字开头
local user_name = "Alice"
local _private = 1
local MAX_SIZE = 100  -- 常量习惯全大写
```

---

**基本写法：避免保留字**
`-- 不能用 and/or/if/local/function 等`
```lua
-- 保留字不能作标识符
-- local function = 1  -- 错误
-- local if = 2         -- 错误
```

---

**基本写法：约定命名**
`<小写蛇形> | <驼峰> | <全大写>`
```lua
-- 常见命名约定
local user_count = 0      -- 蛇形：变量函数
local function calcScore() end  -- 驼峰：方法
local MAX_RETRIES = 3     -- 全大写：常量
local _internal_state = {} -- 前置下划线：私有
```

---

## 基本数据类型

**基本写法：查看类型**
`type(<值>)`
```lua
-- 返回类型名字符串
print(type(42))        -- number
print(type("hi"))      -- string
print(type(nil))       -- nil
print(type({}))        -- table
```

---

**基本写法：八种基本类型**
`nil | boolean | number | string | function | table | thread | userdata`
```lua
-- Lua 的八种基本类型
local a = nil            -- 空
local b = true           -- 布尔
local c = 3.14           -- 数字
local d = "text"         -- 字符串
local e = print          -- 函数
local f = {}             -- 表
local g = coroutine.create(function() end) -- thread 协程
-- userdata 由 C API 创建
```

---

**基本写法：数字子类型**
`math.type(<数字>)`
```lua
-- Lua 5.3+ 区分整数与浮点
print(math.type(10))    -- integer
print(math.type(10.0))  -- float
```

---

## 变量作用域

**基本写法：局部变量**
`local <变量> = <值>`
```lua
-- 局部变量仅在块内有效
local x = 10
do
    local x = 20  -- 块内独立变量
    print(x)      -- 20
end
print(x)          -- 10
```

---

**基本写法：多变量赋值**
`local <a>, <b> = <值1>, <值2>`
```lua
-- 一次声明多个变量
local x, y = 1, 2
local a, b, c = 10, 20
-- 数量不足时补 nil
```

---

**基本写法：交换变量**
`<a>, <b> = <b>, <a>`
```lua
-- 无需临时变量
local a, b = 1, 2
a, b = b, a
```

---

**基本写法：全局变量**
`<变量> = <值>`
```lua
-- 不加 local 即为全局变量
count = 0  -- 存入 _G.count
_G.name = "Alice"
```

---

## 运算符

**基本写法：算术运算**
`+ - * / // % ^`
```lua
-- 算术运算符
local sum = 1 + 2      -- 3
local div = 7 / 2      -- 3.5
local idiv = 7 // 2    -- 3 整除
local mod = 7 % 2      -- 1 取余
local pow = 2 ^ 10     -- 1024 幂
```

---

**基本写法：比较运算**
`== ~= < > <= >=`
```lua
-- 注意 ~= 是不等于
local eq = (1 == 1)
local ne = (1 ~= 2)
-- 不同类型比较永远不等
-- "10" < "9" 字符串按字典序
```

---

**基本写法：逻辑运算**
`and or not`
```lua
-- 短路求值，返回操作数而非布尔
local v = nil or "default"  -- "default"
local r = true and "yes"    -- "yes"
local n = not nil           -- true
```

---

**基本写法：默认值惯用法**
`<值> or <默认值>`
```lua
-- nil 时取默认值
local port = config.port or 8080
```

---

**基本写法：位运算（5.3+）**
`& | ~ << >>`
```lua
-- 整数位运算
local a = 0xF0 & 0x0F  -- 0
local b = 0xF0 | 0x0F  -- 255
local c = 1 << 4       -- 16
local d = ~0           -- -1 按位取反
```

---

**基本写法：字符串连接**
`<串1> .. <串2>`
```lua
-- 用 .. 连接字符串
local s = "Hello" .. ", " .. "world"
```

---

**基本写法：长度运算**
`#<字符串或表>`
```lua
-- 取字符串字节数或表序列长度
local len = #("hello")  -- 5
local n = #({ 1, 2, 3 }) -- 3
```

---

## 控制流

**基本写法：if 分支**
`if <条件> then <语句> elseif <条件> then <语句> else <语句> end`
```lua
-- 条件分支
if score >= 90 then
    grade = "A"
elseif score >= 60 then
    grade = "B"
else
    grade = "C"
end
```

---

**基本写法：while 循环**
`while <条件> do <语句> end`
```lua
-- 条件为真时反复执行
local i = 1
while i <= 10 do
    i = i + 1
end
```

---

**基本写法：repeat 循环**
`repeat <语句> until <条件>`
```lua
-- 先执行后判断，至少执行一次
local i = 1
repeat
    i = i + 1
until i > 10
```

---

**基本写法：数值 for**
`for <i> = <起>, <止> [, <步>] do <语句> end`
```lua
-- 数值遍历
for i = 1, 10 do print(i) end
for i = 10, 1, -1 do print(i) end
```

---

**基本写法：泛型 for**
`for <变量> in <迭代器> do <语句> end`
```lua
-- 用迭代器遍历
for k, v in pairs(t) do print(k, v) end
for i, v in ipairs(arr) do print(i, v) end
```

---

**基本写法：break 与 return**
`break | return [<值>]`
```lua
-- break 跳出循环，return 返回函数
for i = 1, 10 do
    if i == 5 then break end
end
local function f() return 42 end
```

---

**基本写法：goto 跳转（5.2+）**
`goto <标签> | ::<标签>::`
```lua
-- 配合标签实现跳转
for i = 1, 10 do
    if i == 5 then goto skip end
    ::skip::
end
```

---

## 安装与构建

**基本写法：源码编译**
`make <平台>`
```bash
// 从源码编译 Lua
make linux
make macosx
make mingw
```

---

**基本写法：指定安装路径**
`make install INSTALL_TOP=<路径>`
```bash
// 安装到自定义目录
make install INSTALL_TOP=/usr/local/lua
```

---

**基本写法：包管理器安装**
`apt install lua5.4 | brew install lua`
```bash
// 各平台包管理器安装
sudo apt install lua5.4      # Debian/Ubuntu
brew install lua             # macOS
choco install lua            # Windows
```
