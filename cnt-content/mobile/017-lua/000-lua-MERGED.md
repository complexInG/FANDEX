---
order: 10
title: lua 模块文档合集
module: 'lua'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：017-lua/001-ProgramStructureBasicSyntax.md ============ -->

# Lua 程序结构与基本语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 注释

**基本写法：单行注释**
`-- <comment>`
```lua
-- 单行注释
local x = 10
```

**基本写法：多行注释**
`--[[ <content> ]]`
```lua
-- 多行注释
local x = 10
```

**基本写法：多行注释带嵌套**
`--[==[ <content> ]==]`
```lua
--[==[
带等号的多行注释
可以嵌套 ]]
]==]
local x = 10
```

---

## 变量声明

**基本写法：local 局部变量**
`local <name> = <value>`
```lua
-- 声明局部变量
local x = 10
local name = "Lua"
```

**基本写法：多变量赋值**
`local <name1>, <name2> = <value1>, <value2>`
```lua
-- 多变量赋值
local a, b = 1, 2
```

**基本写法：全局变量**
`<name> = <value>`
```lua
-- 全局变量（无 local 关键字）
count = 0
```

**基本写法：多变量交换**
`<name1>, <name2> = <name2>, <name1>`
```lua
-- 变量交换
local a, b = 1, 2
a, b = b, a
```

**基本写法：默认值赋值**
`<name> = <name> or <default>`
```lua
-- 使用 or 提供默认值
local name = name or "default"
```

---

## 运算符

**基本写法：算术运算符**
`<a> <op> <b>`
```lua
-- 算术运算
local sum = 10 + 20
local diff = 20 - 10
local product = 10 * 2
local quotient = 10 / 3
local intDiv = 10 // 3
local modulo = 10 % 3
local power = 2 ^ 10
```

**基本写法：比较运算符**
`<a> <op> <b>`
```lua
-- 比较运算
local isEqual = (10 == 10)
local isNotEqual = (10 ~= 20)
local isLess = (10 < 20)
local isGreater = (20 > 10)
local isLessEqual = (10 <= 10)
local isGreaterEqual = (20 >= 20)
```

**基本写法：逻辑运算符**
`<a> <op> <b>`
```lua
-- 逻辑运算
local result1 = true and false
local result2 = true or false
local result3 = not true
```

**基本写法：字符串连接**
`<str1> .. <str2>`
```lua
-- 字符串连接
local greeting = "Hello" .. ", " .. "Lua"
```

**基本写法：长度运算符**
`#<string>`
```lua
-- 获取字符串长度
local length = #"Hello"
```

**基本写法：获取表长度**
`#<table>`
```lua
-- 获取表长度
local arr = {1, 2, 3, 4, 5}
local length = #arr
```

---

## 控制流

**基本写法：if 语句**
`if <cond> then <body> end`
```lua
-- if 语句
if x > 0 then
    print("正数")
end
```

**基本写法：if-else 语句**
`if <cond> then <body1> else <body2> end`
```lua
-- if-else 语句
if x > 0 then
    print("正数")
else
    print("非正数")
end
```

**基本写法：if-elseif-else 语句**
`if <cond1> then <body1> elseif <cond2> then <body2> else <body3> end`
```lua
-- if-elseif-else 语句
if x > 0 then
    print("正数")
elseif x < 0 then
    print("负数")
else
    print("零")
end
```

**基本写法：while 循环**
`while <cond> do <body> end`
```lua
-- while 循环
local i = 1
while i <= 5 do
    print(i)
    i = i + 1
end
```

**基本写法：repeat-until 循环**
`repeat <body> until <cond>`
```lua
-- repeat-until 循环（至少执行一次）
local i = 1
repeat
    print(i)
    i = i + 1
until i > 5
```

**基本写法：for 数值循环**
`for <var> = <start>, <stop>, <step> do <body> end`
```lua
-- for 数值循环
for i = 1, 10, 2 do
    print(i)
end
```

**基本写法：for 递减循环**
`for <var> = <start>, <stop>, -<step> do <body> end`
```lua
-- for 递减循环
for i = 10, 1, -1 do
    print(i)
end
```

**基本写法：for 泛型循环**
`for <var1>, <var2> in <expr> do <body> end`
```lua
-- for 泛型循环
local arr = {10, 20, 30}
for i, v in ipairs(arr) do
    print(i, v)
end
```

**基本写法：for 遍历表键值**
`for <key>, <value> in pairs(<table>) do <body> end`
```lua
-- 遍历表的键值对
local t = {name = "Lua", version = 5.4}
for k, v in pairs(t) do
    print(k, v)
end
```

**基本写法：break 跳出循环**
`break`
```lua
-- break 跳出循环
for i = 1, 10 do
    if i == 5 then break end
    print(i)
end
```

**基本写法：goto 跳转**
`goto <label>`
```lua
-- goto 跳转
for i = 1, 10 do
    if i == 5 then goto skip end
    print(i)
    ::skip::
end
```

---

## 作用域

**基本写法：local 块作用域**
`do local <name> = <value> <body> end`
```lua
-- do-end 块作用域
do
    local x = 10
    print(x)
end
```

**基本写法：local 函数作用域**
`local <name> = <value>`
```lua
-- local 变量仅在当前作用域有效
function test()
    local y = 20
    print(y)
end
```

---

## 多赋值与默认值

**基本写法：函数返回多值赋值**
`local <name1>, <name2> = <func>()`
```lua
-- 函数返回多值赋值
local function getCoords()
    return 10, 20
end
local x, y = getCoords()
```

**基本写法：调整返回值数量**
`local <name> = (<func>())`
```lua
-- 括号调整返回值为 1 个
local function multi()
    return 1, 2, 3
end
local x = (multi())
```

**基本写法：可变参数**
`local <name> = {<...>}`
```lua
-- 可变参数收集为表
local function sum(...)
    local args = {...}
    local total = 0
    for _, v in ipairs(args) do
        total = total + v
    end
    return total
end
```

**基本写法：select 获取可变参数**
`select(<n>, ...)`
```lua
-- select 获取可变参数
local function first(...)
    return select(1, ...)
end
```

**基本写法：select 获取参数数量**
`select("#", ...)`
```lua
-- 获取可变参数数量
local function count(...)
    return select("#", ...)
end
```

---

## 关键字与保留字

**基本写法：local 关键字**
`local <name>`
```lua
-- local 声明局部变量
local x = 10
```

**基本写法：nil 值**
`<name> = nil`
```lua
-- nil 表示空值
local x = nil
```

**基本写法：true/false 布尔值**
`local <name> = <bool>`
```lua
-- 布尔值
local isActive = true
local isDone = false
```

---

## 基本输入输出

**基本写法：print 输出**
`print(<value>)`
```lua
-- print 输出到标准输出
print("Hello, Lua")
```

**基本写法：io.write 输出**
`io.write(<value>)`
```lua
-- io.write 输出（不换行）
io.write("Hello, ")
io.write("Lua\n")
```

**基本写法：io.read 输入**
`io.read()`
```lua
-- io.read 读取输入
local input = io.read()
```

**基本写法：io.read 读取数字**
`io.read("*n")`
```lua
-- 读取数字
local num = io.read("*n")
```

---

## 类型检查

**基本写法：type 获取类型**
`type(<value>)`
```lua
-- type 获取值类型
print(type(10))
print(type("Hello"))
print(type(true))
print(type(nil))
print(type({}))
print(type(print))
```

**基本写法：类型判断**
`type(<value>) == "<type>"`
```lua
-- 判断值类型
local x = 10
if type(x) == "number" then
    print("是数字")
end
```

---

## 运算符优先级

**基本写法：指数运算优先级**
`<a> ^ <b>`
```lua
-- ^ 优先级最高
local result = 2 + 3 ^ 2
```

**基本写法：一元运算符**
`-<value>`
```lua
-- 一元负号
local x = -10
```

**基本写法：not 运算符**
`not <value>`
```lua
-- not 逻辑非
local result = not nil
```

**基本写法：and/or 短路求值**
`<a> and <b> or <c>`
```lua
-- and/or 短路求值（类似三元运算符）
local x = 10
local result = (x > 5) and "大" or "小"
```



<!-- ============ 文档分隔线：017-lua/002-FunctionAndClosure.md ============ -->

# Lua 函数与闭包速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数定义

**基本写法：基本函数**
`function <name>(<params>) <body> end`
```lua
-- 基本函数定义
function add(a, b)
    return a + b
end
```

**基本写法：local 函数**
`local function <name>(<params>) <body> end`
```lua
-- local 函数
local function greet(name)
    return "Hello, " .. name
end
```

**基本写法：匿名函数赋值**
`local <name> = function(<params>) <body> end`
```lua
-- 匿名函数赋值给变量
local multiply = function(a, b)
    return a * b
end
```

**基本写法：表达式函数**
`local <name> = function(<params>) <expr> end`
```lua
-- 简单表达式函数
local square = function(x) return x * x end
```

**基本写法：表字段函数**
`<table>.<name> = function(<params>) <body> end`
```lua
-- 表字段函数
local utils = {}
utils.add = function(a, b)
    return a + b
end
```

**基本写法：表方法简写**
`function <table>.<name>(<params>) <body> end`
```lua
-- 表方法简写
function utils.subtract(a, b)
    return a - b
end
```

---

## 函数参数

**基本写法：固定参数**
`function <name>(<param1>, <param2>) <body> end`
```lua
-- 固定参数函数
function divide(a, b)
    return a / b
end
```

**基本写法：默认参数**
`<param> = <param> or <default>`
```lua
-- 默认参数
function greet(name, greeting)
    greeting = greeting or "Hello"
    return greeting .. ", " .. name
end
```

**基本写法：可变参数**
`function <name>(...) <body> end`
```lua
-- 可变参数函数
function sum(...)
    local total = 0
    for _, v in ipairs({...}) do
        total = total + v
    end
    return total
end
```

**基本写法：固定与可变参数混合**
`function <name>(<param>, ...) <body> end`
```lua
-- 固定参数与可变参数混合
function printf(format, ...)
    return string.format(format, ...)
end
```

**基本写法：select 获取可变参数**
`select(<n>, ...)`
```lua
-- select 获取指定位置参数
function firstAndRest(...)
    local first = select(1, ...)
    local rest = {select(2, ...)}
    return first, rest
end
```

**基本写法：select 获取参数数量**
`select("#", ...)`
```lua
-- 获取参数数量
function count(...)
    return select("#", ...)
end
```

---

## 函数返回值

**基本写法：单返回值**
`function <name>(<params>) return <value> end`
```lua
-- 单返回值
function double(x)
    return x * 2
end
```

**基本写法：多返回值**
`function <name>(<params>) return <val1>, <val2> end`
```lua
-- 多返回值
function getCoords()
    return 10, 20
end
```

**基本写法：无返回值**
`function <name>(<params>) <body> end`
```lua
-- 无返回值
function printMsg(msg)
    print(msg)
end
```

**基本写法：条件返回**
`if <cond> then return <val1> else return <val2> end`
```lua
-- 条件返回
function max(a, b)
    if a > b then
        return a
    else
        return b
    end
end
```

**基本写法：提前返回**
`if <cond> then return end`
```lua
-- 提前返回
function process(data)
    if not data then return end
    print(data)
end
```

---

## 闭包

**基本写法：基本闭包**
`local function <name>() local <var> = <init> return function() <body> end end`
```lua
-- 基本闭包
local function counter()
    local count = 0
    return function()
        count = count + 1
        return count
    end
end
```

**基本写法：闭包捕获变量**
`local <var> = <init>; local <func> = function() <body using var> end`
```lua
-- 闭包捕获外部变量
local x = 10
local function getX()
    return x
end
```

**基本写法：闭包工厂**
`local function <factory>(<param>) return function() <body> end end`
```lua
-- 闭包工厂
local function makeAdder(n)
    return function(x)
        return x + n
    end
end
```

**基本写法：闭包状态保持**
`local function <name>() local <state> = <init> return function(<param>) <body> end end`
```lua
-- 闭包保持状态
local function makeBank()
    local balance = 0
    return function(amount)
        balance = balance + amount
        return balance
    end
end
```

**基本写法：闭包共享状态**
`local <func1>, <func2> = <factory>()`
```lua
-- 闭包共享状态
local function makePair()
    local shared = 0
    local function set(v) shared = v end
    local function get() return shared end
    return set, get
end
```

---

## 高阶函数

**基本写法：函数作为参数**
`function <name>(<func>, <params>) <body> end`
```lua
-- 函数作为参数
function apply(func, value)
    return func(value)
end
```

**基本写法：函数作为返回值**
`function <name>(<params>) return function() <body> end end`
```lua
-- 函数作为返回值
function makeGreeter(greeting)
    return function(name)
        return greeting .. ", " .. name
    end
end
```

**基本写法：map 映射函数**
`function <name>(<arr>, <func>) <body> end`
```lua
-- map 映射函数
function map(arr, func)
    local result = {}
    for i, v in ipairs(arr) do
        result[i] = func(v)
    end
    return result
end
```

**基本写法：filter 过滤函数**
`function <name>(<arr>, <func>) <body> end`
```lua
-- filter 过滤函数
function filter(arr, func)
    local result = {}
    for _, v in ipairs(arr) do
        if func(v) then
            result[#result + 1] = v
        end
    end
    return result
end
```

**基本写法：reduce 累积函数**
`function <name>(<arr>, <func>, <init>) <body> end`
```lua
-- reduce 累积函数
function reduce(arr, func, init)
    local acc = init
    for _, v in ipairs(arr) do
        acc = func(acc, v)
    end
    return acc
end
```

**基本写法：forEach 遍历函数**
`function <name>(<arr>, <func>) <body> end`
```lua
-- forEach 遍历函数
function forEach(arr, func)
    for i, v in ipairs(arr) do
        func(v, i)
    end
end
```

---

## 函数调用

**基本写法：基本调用**
`<name>(<args>)`
```lua
-- 基本函数调用
local result = add(1, 2)
```

**基本写法：方法调用**
`<obj>:<method>(<args>)`
```lua
-- 方法调用（自动传递 self）
local str = "Hello"
local upper = str:upper()
```

**基本写法：表方法调用**
`<table>.<method>(<table>, <args>)`
```lua
-- 表方法调用（显式传递 self）
local result = string.upper(str)
```

**基本写法：函数作为表字段调用**
`<table>.<func>(<args>)`
```lua
-- 表字段函数调用
local result = utils.add(1, 2)
```

**基本写法：可变参数调用**
`<name>(<unpack>)`
```lua
-- 解包表作为参数调用
local args = {1, 2, 3}
local result = sum(table.unpack(args))
```

---

## 递归

**基本写法：基本递归**
`local function <name>(<param>) if <base> then return <val> else return <name>(<expr>) end end`
```lua
-- 递归计算阶乘
local function factorial(n)
    if n <= 1 then
        return 1
    else
        return n * factorial(n - 1)
    end
end
```

**基本写法：尾递归**
`local function <name>(<param>, <acc>) if <base> then return <acc> else return <name>(<expr>, <expr>) end end`
```lua
-- 尾递归计算阶乘
local function factorialTail(n, acc)
    if n <= 1 then
        return acc
    else
        return factorialTail(n - 1, n * acc)
    end
end
```

**基本写法：递归遍历表**
`local function <name>(<table>) for <k>, <v> in pairs(<table>) do if type(<v>) == "table" then <name>(<v>) end end end`
```lua
-- 递归遍历嵌套表
local function deepPrint(t, indent)
    indent = indent or ""
    for k, v in pairs(t) do
        if type(v) == "table" then
            print(indent .. k .. ":")
            deepPrint(v, indent .. "  ")
        else
            print(indent .. k .. ": " .. tostring(v))
        end
    end
end
```

---

## 函数作用域

**基本写法：local 函数前向引用**
`local <name>; <name> = function(<params>) <body> end`
```lua
-- local 函数前向声明
local fibonacci
fibonacci = function(n)
    if n <= 1 then
        return n
    else
        return fibonacci(n - 1) + fibonacci(n - 2)
    end
end
```

**基本写法：嵌套函数**
`function <outer>() local function <inner>() <body> end <body> end`
```lua
-- 嵌套函数
function process(data)
    local function validate(d)
        return d ~= nil
    end
    if validate(data) then
        print("Valid")
    end
end
```

---

## 函数与 Table

**基本写法：函数存储在表中**
`local <table> = { <name1> = function(...) end, <name2> = function(...) end }`
```lua
-- 函数存储在表中
local operations = {
    add = function(a, b) return a + b end,
    subtract = function(a, b) return a - b end,
    multiply = function(a, b) return a * b end
}
```

**基本写法：表方法定义**
`function <table>.<name>(<self>, <params>) <body> end`
```lua
-- 表方法定义
local obj = {}
function obj.greet(self, name)
    return "Hello, " .. name
end
```

**基本写法：冒号语法定义方法**
`function <table>:<name>(<params>) <body> end`
```lua
-- 冒号语法定义方法（自动传递 self）
function obj:greet(name)
    return "Hello, " .. name
end
```

---

## 函数式编程

**基本写法：函数组合**
`local function <name>(<f>, <g>) return function(<x>) return <f>(<g>(<x>)) end end`
```lua
-- 函数组合
local function compose(f, g)
    return function(x)
        return f(g(x))
    end
end
```

**基本写法：柯里化**
`local function <name>(<a>) return function(<b>) return <expr> end end`
```lua
-- 柯里化
local function curryAdd(a)
    return function(b)
        return a + b
    end
end
```

**基本写法：偏应用**
`local function <name>(<func>, <a>) return function(<b>) return <func>(<a>, <b>) end end`
```lua
-- 偏应用
local function partial(func, a)
    return function(b)
        return func(a, b)
    end
end
```

**基本写法：记忆化**
`local <cache> = {}; local function <name>(<param>) if <cache>[<param>] then return <cache>[<param>] end <body> <cache>[<param>] = <result> return <result> end`
```lua
-- 记忆化函数
local memo = {}
local function fibonacci(n)
    if memo[n] then return memo[n] end
    if n <= 1 then return n end
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]
end
```



<!-- ============ 文档分隔线：017-lua/003-OOP.md ============ -->

# Lua 面向对象编程速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类定义

**基本写法：类定义**
`local <Class> = {}; <Class>.__index = <Class>; <Class>.<method> = function(<self>, <params>) <body> end`
```lua
-- 类定义
local Animal = {}
Animal.__index = Animal
function Animal.new(name)
    local self = setmetatable({}, Animal)
    self.name = name
    return self
end
function Animal:speak()
    return "Some sound"
end
```

**基本写法：构造函数**
`function <Class>.new(<params>) local <self> = setmetatable({}, <Class>); <body>; return <self> end`
```lua
-- 构造函数
function Animal.new(name, age)
    local self = setmetatable({}, Animal)
    self.name = name
    self.age = age
    return self
end
```

**基本写法：实例方法**
`function <Class>:<method>(<params>) <body> end`
```lua
-- 实例方法（使用冒号语法）
function Animal:getName()
    return self.name
end
```

**基本写法：点号语法定义方法**
`function <Class>.<method>(<self>, <params>) <body> end`
```lua
-- 点号语法定义方法（显式 self）
function Animal.getName(self)
    return self.name
end
```

**基本写法：实例创建**
`local <instance> = <Class>.new(<args>)`
```lua
-- 创建实例
local dog = Animal.new("Buddy")
print(dog:speak())
```

---

## 继承

**基本写法：单继承**
`local <SubClass> = setmetatable({}, {__index = <BaseClass>}); <SubClass>.__index = <SubClass>`
```lua
-- 单继承
local Dog = setmetatable({}, {__index = Animal})
Dog.__index = Dog
function Dog.new(name, breed)
    local self = Animal.new(name)
    setmetatable(self, Dog)
    self.breed = breed
    return self
end
```

**基本写法：重写父类方法**
`function <SubClass>:<method>(<params>) <body> end`
```lua
-- 重写父类方法
function Dog:speak()
    return "Woof"
end
```

**基本写法：调用父类方法**
`<BaseClass>.<method>(<self>, <params>)`
```lua
-- 调用父类方法
function Dog:getInfo()
    local info = Animal.getName(self)
    return info .. " (" .. self.breed .. ")"
end
```

**基本写法：多级继承**
`setmetatable(<child>, {__index = <parent>}); setmetatable(<parent>, {__index = <grandparent>})`
```lua
-- 多级继承
local Puppy = setmetatable({}, {__index = Dog})
Puppy.__index = Puppy
function Puppy.new(name, breed)
    local self = Dog.new(name, breed)
    setmetatable(self, Puppy)
    return self
end
```

---

## 多重继承

**换行写法：多重继承**
`local <mt> = { __index = function(<t>, <k>) for _, <parent> in ipairs(<parents>) do if <parent>[<k>] then return <parent>[<k>] end end end }`
```lua
-- 多重继承
local function createClass(...)
    local parents = {...}
    local child = {}
    setmetatable(child, {
        __index = function(t, k)
            for _, parent in ipairs(parents) do
                if parent[k] then
                    return parent[k]
                end
            end
        end
    })
    child.__index = child
    return child
end
```

---

## 封装

**基本写法：私有字段**
`local <private> = <value>; function <Class>:<method>() return <private> end`
```lua
-- 私有字段（闭包实现）
local function createCounter()
    local count = 0
    return {
        increment = function() count = count + 1 end,
        getValue = function() return count end
    }
end
```

**基本写法：私有方法**
`local function <private>(<self>) <body> end`
```lua
-- 私有方法
local function validateName(name)
    return type(name) == "string" and #name > 0
end
function Animal.new(name)
    if not validateName(name) then
        error("Invalid name")
    end
    local self = setmetatable({}, Animal)
    self.name = name
    return self
end
```

---

## 多态

**基本写法：多态调用**
`function <SubClass>:<method>() <body> end`
```lua
-- 多态调用
local Cat = setmetatable({}, {__index = Animal})
Cat.__index = Cat
function Cat:speak()
    return "Meow"
end
local animals = {
    Dog.new("Buddy"),
    Cat.new("Whiskers")
}
for _, animal in ipairs(animals) do
    print(animal:speak())
end
```

---

## 类属性

**基本写法：类静态属性**
`<Class>.<prop> = <value>`
```lua
-- 类静态属性
Animal.count = 0
function Animal.new(name)
    Animal.count = Animal.count + 1
    local self = setmetatable({}, Animal)
    self.name = name
    return self
end
```

**基本写法：类静态方法**
`function <Class>.<method>(<params>) <body> end`
```lua
-- 类静态方法
function Animal.getCount()
    return Animal.count
end
```

**基本写法：访问类静态成员**
`<Class>.<member>`
```lua
-- 访问类静态成员
print(Animal.getCount())
```

---

## 元表与 OOP

**基本写法：__index 实现继承**
`<Class>.__index = <Class>`
```lua
-- __index 实现类方法查找
local Person = {}
Person.__index = Person
function Person.new(name)
    return setmetatable({name = name}, Person)
end
function Person:greet()
    return "Hello, " .. self.name
end
```

**基本写法：__tostring 自定义输出**
`<Class>.__tostring = function(<self>) <body> end`
```lua
-- __tostring 自定义字符串表示
Person.__tostring = function(self)
    return "Person(" .. self.name .. ")"
end
local p = Person.new("Alice")
print(tostring(p))
```

**基本写法：__eq 自定义相等**
`<Class>.__eq = function(<a>, <b>) <body> end`
```lua
-- __eq 自定义相等比较
Person.__eq = function(a, b)
    return a.name == b.name
end
```

---

## 对象创建模式

**基本写法：工厂函数**
`local function <factory>(<params>) return setmetatable({<fields>}, <Class>) end`
```lua
-- 工厂函数创建对象
local function createPoint(x, y)
    return setmetatable({x = x, y = y}, Point)
end
```

**基本写法：Builder 模式**
`local <Builder> = {}; function <Builder>:<method>(<param>) <body>; return <self> end`
```lua
-- Builder 模式
local StringBuilder = {}
StringBuilder.__index = StringBuilder
function StringBuilder.new()
    return setmetatable({parts = {}}, StringBuilder)
end
function StringBuilder:append(s)
    self.parts[#self.parts + 1] = s
    return self
end
function StringBuilder:build()
    return table.concat(self.parts)
end
```

---

## Mixin 模式

**基本写法：Mixin 组合**
`for <k>, <v> in pairs(<mixin>) do <target>[<k>] = <v> end`
```lua
-- Mixin 组合
local Serializable = {
    serialize = function(self)
        local parts = {}
        for k, v in pairs(self) do
            parts[#parts + 1] = k .. "=" .. tostring(v)
        end
        return "{" .. table.concat(parts, ", ") .. "}"
    end
}
local function applyMixin(target, mixin)
    for k, v in pairs(mixin) do
        target[k] = v
    end
end
```

---

## 接口模拟

**基本写法：接口模拟**
`local <Interface> = { <method1> = function() error("...") end, <method2> = function() error("...") end }`
```lua
-- 接口模拟（抽象方法）
local Drawable = {
    draw = function(self) error("Not implemented") end,
    getArea = function(self) error("Not implemented") end
}
local Circle = setmetatable({}, {__index = Drawable})
Circle.__index = Circle
function Circle.new(radius)
    return setmetatable({radius = radius}, Circle)
end
function Circle:draw()
    return "Drawing circle"
end
```

---

## 对象生命周期

**基本写法：构造函数**
`function <Class>.new(<params>) <body> end`
```lua
-- 构造函数
function Animal.new(name)
    local self = setmetatable({}, Animal)
    self.name = name
    self.createdAt = os.time()
    return self
end
```

**基本写法：析构函数模拟**
`function <Class>:destroy() <body> end`
```lua
-- 析构函数模拟
function Animal:destroy()
    self.destroyed = true
end
```

**基本写法：__gc 元方法**
`<Class>.__gc = function(<self>) <body> end`
```lua
-- __gc 元方法（Lua 5.2+）
Person.__gc = function(self)
    print("Person " .. self.name .. " is being garbage collected")
end
```

---

## OOP 实战

**换行写法：完整类定义**
`local <Class> = {}; <Class>.__index = <Class>; <Class>.<new> = function(<params>) <body> end; <Class>:<method1> = function() <body> end; <Class>:<method2> = function() <body> end`
```lua
-- 完整类定义
local Stack = {}
Stack.__index = Stack
function Stack.new()
    return setmetatable({items = {}, size = 0}, Stack)
end
function Stack:push(item)
    self.size = self.size + 1
    self.items[self.size] = item
end
function Stack:pop()
    if self.size == 0 then return nil end
    local item = self.items[self.size]
    self.items[self.size] = nil
    self.size = self.size - 1
    return item
end
function Stack:peek()
    return self.items[self.size]
end
function Stack:isEmpty()
    return self.size == 0
end
```

**基本写法：单例模式**
`local <Singleton> = {}; local <instance> = nil; function <Singleton>.getInstance() if not <instance> then <instance> = <create> end return <instance> end`
```lua
-- 单例模式
local Database = {}
local instance = nil
function Database.getInstance()
    if not instance then
        instance = setmetatable({}, Database)
        instance.connected = false
    end
    return instance
end
```



<!-- ============ 文档分隔线：017-lua/004-ModulePackage.md ============ -->

# Lua 模块与包速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 模块定义

**基本写法：模块定义**
`local <module> = {}; return <module>`
```lua
-- 定义模块
local M = {}
function M.greet(name)
    return "Hello, " .. name
end
return M
```

**基本写法：模块返回表**
`local <module> = { <members> }; return <module>`
```lua
-- 模块返回包含函数的表
local M = {
    add = function(a, b) return a + b end,
    subtract = function(a, b) return a - b end
}
return M
```

**换行写法：多函数模块**
`local <module> = {}; function <module>.<name1>() <body> end; function <module>.<name2>() <body> end; return <module>`
```lua
-- 多函数模块定义
local M = {}
function M.add(a, b)
    return a + b
end
function M.subtract(a, b)
    return a - b
end
function M.multiply(a, b)
    return a * b
end
return M
```

---

## 模块加载

**基本写法：require 加载模块**
`local <module> = require("<module>")`
```lua
-- 加载模块
local math = require("math")
local utils = require("utils")
```

**基本写法：require 带路径**
`require("<path>.<module>")`
```lua
-- 加载子目录中的模块
local parser = require("lib.parser")
local config = require("app.config")
```

**基本写法：require 缓存**
`local <module> = require("<module>")`
```lua
-- require 会缓存模块，多次调用只加载一次
local mod1 = require("utils")
local mod2 = require("utils")
print(mod1 == mod2)
```

**基本写法：package.loaded 清除缓存**
`package.loaded["<module>"] = nil`
```lua
-- 清除模块缓存，强制重新加载
package.loaded["utils"] = nil
local utils = require("utils")
```

---

## 模块路径

**基本写法：package.path 查看搜索路径**
`print(package.path)`
```lua
-- 查看 Lua 模块搜索路径
print(package.path)
```

**基本写法：package.cpath 查看 C 模块路径**
`print(package.cpath)`
```lua
-- 查看 C 模块搜索路径
print(package.cpath)
```

**基本写法：添加搜索路径**
`package.path = package.path .. ";<path>?.lua"`
```lua
-- 添加自定义搜索路径
package.path = package.path .. ";./lib/?.lua"
```

**基本写法：package.searchpath 搜索文件**
`package.searchpath("<module>", <path>)`
```lua
-- 搜索模块文件路径
local path = package.searchpath("utils", package.path)
```

---

## 模块导出

**基本写法：导出函数**
`<module>.<name> = function(<params>) <body> end`
```lua
-- 导出模块函数
local M = {}
M.greet = function(name)
    return "Hello, " .. name
end
return M
```

**基本写法：导出变量**
`<module>.<name> = <value>`
```lua
-- 导出模块变量
local M = {}
M.version = "1.0.0"
M.author = "Lua"
return M
```

**基本写法：导出表**
`<module>.<name> = { <members> }`
```lua
-- 导出子表
local M = {}
M.config = {
    host = "localhost",
    port = 8080
}
return M
```

**基本写法：local 与导出结合**
`local function <private>() <body> end; <module>.<public> = function() <body> end`
```lua
-- 私有函数与公开函数
local M = {}
local function privateHelper(x)
    return x * 2
end
function M.process(x)
    return privateHelper(x) + 1
end
return M
```

---

## 模块模式

**基本写法：模块单例模式**
`local <module> = {}; <module>.instance = nil; function <module>.get() <body> end; return <module>`
```lua
-- 模块单例模式
local M = {}
local instance = nil
function M.getInstance()
    if not instance then
        instance = M._create()
    end
    return instance
end
function M._create()
    return { data = {} }
end
return M
```

**基本写法：模块工厂模式**
`local <module> = {}; function <module>.create(<params>) <body> end; return <module>`
```lua
-- 模块工厂模式
local M = {}
function M.create(name, age)
    return {
        name = name,
        age = age,
        greet = function(self)
            return "Hi, I'm " .. self.name
        end
    }
end
return M
```

---

## 模块依赖

**基本写法：模块间依赖**
`local <dep> = require("<dep>"); local <module> = {}; <body>; return <module>`
```lua
-- 模块依赖其他模块
local logger = require("logger")
local M = {}
function M.process(data)
    logger.info("Processing data")
    return data
end
return M
```

**基本写法：循环依赖处理**
`local <module> = {}; function <module>.<method>() local <dep> = require("<dep>"); <body> end; return <module>`
```lua
-- 延迟加载解决循环依赖
local M = {}
function M.process()
    local dep = require("dep")
    return dep.doSomething()
end
return M
```

---

## package 模块

**基本写法：package.loaded 已加载模块**
`package.loaded["<module>"]`
```lua
-- 检查模块是否已加载
if package.loaded["utils"] then
    print("utils 已加载")
end
```

**基本写法：package.preload 预加载**
`package.preload["<module>"] = function(<name>) <body> end`
```lua
-- 预加载模块
package.preload["mymodule"] = function(name)
    return { greet = function() return "Hello" end }
end
```

**基本写法：package.seeall**
`setmetatable(<module>, {__index = _G})`
```lua
-- 模块访问全局环境
local M = {}
setmetatable(M, {__index = _G})
return M
```

---

## 模块加载器

**基本写法：自定义加载器**
`table.insert(package.loaders, <function>)`
```lua
-- 自定义模块加载器
table.insert(package.loaders or package.searchers, function(name)
    return function()
        return { custom = true }
    end
end)
```

**基本写法：package.loaders 查看加载器**
`for <i>, <loader> in ipairs(package.loaders or package.searchers) do <body> end`
```lua
-- 查看所有加载器
local loaders = package.loaders or package.searchers
for i, loader in ipairs(loaders) do
    print(i, loader)
end
```

---

## C 模块

**基本写法：加载 C 模块**
`local <module> = require("<cmodule>")`
```lua
-- 加载 C 扩展模块
local cjson = require("cjson")
local socket = require("socket")
```

**基本写法：package.loadlib 加载动态库**
`package.loadlib("<path>", "<func>")`
```lua
-- 加载动态链接库
local f = package.loadlib("./libtest.so", "luaopen_test")
if f then
    local module = f()
end
```

---

## 模块组织

**基本写法：命名空间式模块**
`local <ns> = {}; <ns>.<sub> = require("<ns>.<sub>"); return <ns>`
```lua
-- 命名空间式模块组织
local app = {}
app.config = require("app.config")
app.utils = require("app.utils")
app.models = require("app.models")
return app
```

**换行写法：多子模块组织**
`local <ns> = { <sub1> = require(...), <sub2> = require(...), <sub3> = require(...) }; return <ns>`
```lua
-- 多子模块组织
local myapp = {
    config = require("myapp.config"),
    database = require("myapp.database"),
    router = require("myapp.router"),
    middleware = require("myapp.middleware")
}
return myapp
```

---

## 模块初始化

**基本写法：模块初始化函数**
`function <module>.init(<params>) <body> end`
```lua
-- 模块初始化函数
local M = {}
function M.init(config)
    M.config = config
    M.initialized = true
end
return M
```

**基本写法：模块自动初始化**
`local <module> = {}; <body>; return <module>`
```lua
-- 模块加载时自动初始化
local M = {}
M.version = "1.0.0"
M.loaded = os.time()
function M.getInfo()
    return "Version: " .. M.version
end
return M
```

---

## 模块重载

**基本写法：模块重载**
`package.loaded["<module>"] = nil; local <module> = require("<module>")`
```lua
-- 模块重载
package.loaded["utils"] = nil
local utils = require("utils")
```

**基本写法：模块重载函数**
`local function <name>(<module>) package.loaded[<module>] = nil; return require(<module>) end`
```lua
-- 模块重载函数
local function reloadModule(name)
    package.loaded[name] = nil
    return require(name)
end
```



<!-- ============ 文档分隔线：017-lua/005-DataTypeTableDetailed.md ============ -->

# Lua 数据类型与 Table 详解速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本数据类型

**基本写法：nil 空值**
`local <name> = nil`
```lua
-- nil 表示空值
local x = nil
```

**基本写法：boolean 布尔值**
`local <name> = <bool>`
```lua
-- 布尔值
local isActive = true
local isDone = false
```

**基本写法：number 数字**
`local <name> = <number>`
```lua
-- 数字类型（整数和浮点数）
local intVal = 42
local floatVal = 3.14
local sciVal = 1e10
local hexVal = 0xFF
```

**基本写法：string 字符串**
`local <name> = "<text>"`
```lua
-- 字符串
local name = "Lua"
local path = 'C:\\Users'
```

**基本写法：多行字符串**
`local <name> = [[<content>]]`
```lua
-- 多行字符串
local text = [[
第一行
第二行
]]
```

**基本写法：function 函数**
`local <name> = function(<params>) <body> end`
```lua
-- 函数类型
local greet = function(name)
    return "Hello, " .. name
end
```

**基本写法：table 表**
`local <name> = {}`
```lua
-- 表类型
local emptyTable = {}
local arr = {1, 2, 3}
local map = {key = "value"}
```

---

## Table 创建

**基本写法：空表**
`local <name> = {}`
```lua
-- 创建空表
local t = {}
```

**单行写法：数组式表**
`local <name> = {<val1>, <val2>, <val3>}`
```lua
-- 创建数组式表
local arr = {10, 20, 30, 40, 50}
```

**单行写法：字典式表**
`local <name> = {<key1> = <val1>, <key2> = <val2>}`
```lua
-- 创建字典式表
local person = {name = "Alice", age = 25}
```

**换行写法：多字段字典式表**
`local <name> = { <key1> = <val1>, <key2> = <val2>, <key3> = <val3> }`
```lua
-- 换行声明多字段表
local config = {
    host = "localhost",
    port = 8080,
    timeout = 5000,
    debug = true
}
```

**单行写法：混合式表**
`local <name> = {<val1>, <key> = <val2>}`
```lua
-- 混合数组与字典
local mixed = {10, 20, name = "Alice", age = 25}
```

**基本写法：嵌套表**
`local <name> = {<key> = {<subkey> = <val>}}`
```lua
-- 嵌套表
local user = {
    profile = {
        name = "Alice",
        age = 25
    }
}
```

---

## Table 访问

**基本写法：点号访问**
`<table>.<key>`
```lua
-- 点号访问表字段
local person = {name = "Alice", age = 25}
print(person.name)
print(person.age)
```

**基本写法：方括号访问**
`<table>["<key>"]`
```lua
-- 方括号访问表字段
print(person["name"])
```

**基本写法：数组索引访问**
`<table>[<index>]`
```lua
-- 数组索引访问（从 1 开始）
local arr = {10, 20, 30}
print(arr[1])
print(arr[2])
```

**基本写法：动态键访问**
`<table>[<variable>]`
```lua
-- 动态键访问
local key = "name"
print(person[key])
```

**基本写法：嵌套表访问**
`<table>.<key1>.<key2>`
```lua
-- 嵌套表访问
local user = {profile = {name = "Alice"}}
print(user.profile.name)
```

---

## Table 修改

**基本写法：添加字段**
`<table>.<newKey> = <value>`
```lua
-- 添加新字段
local person = {}
person.name = "Alice"
person.age = 25
```

**基本写法：修改字段**
`<table>.<key> = <newValue>`
```lua
-- 修改字段值
person.name = "Bob"
```

**基本写法：删除字段**
`<table>.<key> = nil`
```lua
-- 删除字段
person.age = nil
```

**基本写法：数组添加元素**
`<table>[#<table> + 1] = <value>`
```lua
-- 数组末尾添加元素
local arr = {1, 2, 3}
arr[#arr + 1] = 4
```

---

## Table 遍历

**基本写法：ipairs 遍历数组**
`for <i>, <v> in ipairs(<table>) do <body> end`
```lua
-- ipairs 遍历数组部分
local arr = {"a", "b", "c"}
for i, v in ipairs(arr) do
    print(i, v)
end
```

**基本写法：pairs 遍历表**
`for <k>, <v> in pairs(<table>) do <body> end`
```lua
-- pairs 遍历所有键值对
local t = {name = "Alice", age = 25}
for k, v in pairs(t) do
    print(k, v)
end
```

**基本写法：数值遍历数组**
`for <i> = 1, #<table> do <body> end`
```lua
-- 数值遍历数组
local arr = {10, 20, 30}
for i = 1, #arr do
    print(arr[i])
end
```

**基本写法：next 遍历表**
`local <k>, <v> = next(<table>, <prevKey>)`
```lua
-- next 遍历表
local t = {a = 1, b = 2}
local k, v = next(t, nil)
while k do
    print(k, v)
    k, v = next(t, k)
end
```

---

## Table 长度

**基本写法：# 获取长度**
`#<table>`
```lua
-- # 获取数组长度
local arr = {1, 2, 3, 4, 5}
print(#arr)
```

**基本写法：table.getn 获取长度**
`table.getn(<table>)`
```lua
-- table.getn 获取长度（Lua 5.1）
print(table.getn(arr))
```

**基本写法：计算表字段数量**
`local <count> = 0; for _ in pairs(<table>) do <count> = <count> + 1 end`
```lua
-- 计算表字段数量
local t = {a = 1, b = 2, c = 3}
local count = 0
for _ in pairs(t) do
    count = count + 1
end
print(count)
```

---

## Table 操作函数

**基本写法：table.insert 末尾插入**
`table.insert(<table>, <value>)`
```lua
-- 末尾插入元素
local arr = {1, 2, 3}
table.insert(arr, 4)
```

**基本写法：table.insert 指定位置插入**
`table.insert(<table>, <pos>, <value>)`
```lua
-- 指定位置插入元素
table.insert(arr, 1, 0)
```

**基本写法：table.remove 末尾移除**
`table.remove(<table>)`
```lua
-- 移除末尾元素
local removed = table.remove(arr)
```

**基本写法：table.remove 指定位置移除**
`table.remove(<table>, <pos>)`
```lua
-- 移除指定位置元素
local removed = table.remove(arr, 1)
```

**基本写法：table.sort 排序**
`table.sort(<table>)`
```lua
-- 升序排序
local nums = {5, 3, 1, 4, 2}
table.sort(nums)
```

**基本写法：table.sort 自定义排序**
`table.sort(<table>, <comparator>)`
```lua
-- 自定义比较函数排序
table.sort(nums, function(a, b)
    return a > b
end)
```

**基本写法：table.concat 连接**
`table.concat(<table>, <separator>)`
```lua
-- 连接数组为字符串
local arr = {"a", "b", "c"}
local result = table.concat(arr, ", ")
```

**基本写法：table.concat 指定范围连接**
`table.concat(<table>, <separator>, <start>, <end>)`
```lua
-- 指定范围连接
local result = table.concat(arr, ", ", 2, 3)
```

**基本写法：table.unpack 解包**
`table.unpack(<table>)`
```lua
-- 解包表为多个值
local arr = {10, 20, 30}
local a, b, c = table.unpack(arr)
```

**基本写法：table.unpack 部分解包**
`table.unpack(<table>, <start>, <end>)`
```lua
-- 部分解包
local a, b = table.unpack(arr, 1, 2)
```

---

## Table 复制

**基本写法：浅拷贝**
`local <newTable> = {}; for <k>, <v> in pairs(<table>) do <newTable>[<k>] = <v> end`
```lua
-- 浅拷贝表
local function shallowCopy(t)
    local copy = {}
    for k, v in pairs(t) do
        copy[k] = v
    end
    return copy
end
```

**换行写法：深拷贝**
`local function <name>(<table>) <body with recursion> end`
```lua
-- 深拷贝表
local function deepCopy(t)
    local copy = {}
    for k, v in pairs(t) do
        if type(v) == "table" then
            copy[k] = deepCopy(v)
        else
            copy[k] = v
        end
    end
    return copy
end
```

---

## Table 合并

**基本写法：合并两个表**
`for <k>, <v> in pairs(<source>) do <target>[<k>] = <v> end`
```lua
-- 合并两个表
local function merge(target, source)
    for k, v in pairs(source) do
        target[k] = v
    end
    return target
end
```

**基本写法：数组合并**
`for <i>, <v> in ipairs(<source>) do <target>[#<target> + 1] = <v> end`
```lua
-- 合并两个数组
local function mergeArrays(target, source)
    for i, v in ipairs(source) do
        target[#target + 1] = v
    end
    return target
end
```

---

## Table 作为数组

**基本写法：创建数组**
`local <name> = {<val1>, <val2>, <val3>}`
```lua
-- 创建数组
local colors = {"red", "green", "blue"}
```

**基本写法：数组遍历**
`for <i>, <v> in ipairs(<array>) do <body> end`
```lua
-- 遍历数组
for i, color in ipairs(colors) do
    print(i, color)
end
```

**基本写法：数组查找**
`for <i>, <v> in ipairs(<array>) do if <v> == <target> then return <i> end end`
```lua
-- 查找元素索引
local function indexOf(arr, target)
    for i, v in ipairs(arr) do
        if v == target then return i end
    end
    return nil
end
```

**基本写法：数组过滤**
`local <result> = {}; for <i>, <v> in ipairs(<array>) do if <cond> then <result>[#<result> + 1] = <v> end end`
```lua
-- 过滤数组元素
local function filter(arr, predicate)
    local result = {}
    for i, v in ipairs(arr) do
        if predicate(v) then
            result[#result + 1] = v
        end
    end
    return result
end
```

**基本写法：数组映射**
`local <result> = {}; for <i>, <v> in ipairs(<array>) do <result>[<i>] = <transform> end`
```lua
-- 映射数组元素
local function map(arr, transform)
    local result = {}
    for i, v in ipairs(arr) do
        result[i] = transform(v)
    end
    return result
end
```

---

## Table 作为集合

**基本写法：创建集合**
`local <set> = {<key1> = true, <key2> = true}`
```lua
-- 创建集合
local fruits = {apple = true, banana = true, cherry = true}
```

**基本写法：集合添加元素**
`<set>[<key>] = true`
```lua
-- 添加集合元素
fruits.orange = true
```

**基本写法：集合移除元素**
`<set>[<key>] = nil`
```lua
-- 移除集合元素
fruits.banana = nil
```

**基本写法：集合包含检查**
`if <set>[<key>] then <body> end`
```lua
-- 检查集合包含
if fruits.apple then
    print("包含 apple")
end
```

---

## Table 作为队列

**基本写法：队列入队**
`table.insert(<queue>, <value>)`
```lua
-- 队列入队
local queue = {}
table.insert(queue, "task1")
```

**基本写法：队列出队**
`table.remove(<queue>, 1)`
```lua
-- 队列出队
local task = table.remove(queue, 1)
```

---

## 弱引用表

**基本写法：弱引用键表**
`setmetatable({}, {__mode = "k"})`
```lua
-- 弱引用键表
local weakKeys = setmetatable({}, {__mode = "k"})
```

**基本写法：弱引用值表**
`setmetatable({}, {__mode = "v"})`
```lua
-- 弱引用值表
local weakValues = setmetatable({}, {__mode = "v"})
```

**基本写法：弱引用键值表**
`setmetatable({}, {__mode = "kv"})`
```lua
-- 弱引用键值表
local weakKV = setmetatable({}, {__mode = "kv"})
```



<!-- ============ 文档分隔线：017-lua/006-CoroutineAsync.md ============ -->

# Lua 协程与异步速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 协程创建

**基本写法：coroutine.create 创建协程**
`coroutine.create(<function>)`
```lua
-- 创建协程
local co = coroutine.create(function()
    print("协程开始")
    coroutine.yield()
    print("协程恢复")
end)
```

**基本写法：coroutine.wrap 创建协程**
`coroutine.wrap(<function>)`
```lua
-- 创建协程（返回函数）
local co = coroutine.wrap(function()
    print("协程开始")
    coroutine.yield()
    print("协程恢复")
end)
```

---

## 协程控制

**基本写法：coroutine.resume 恢复协程**
`coroutine.resume(<coroutine>)`
```lua
-- 恢复协程执行
local co = coroutine.create(function()
    print("Hello")
    coroutine.yield()
    print("World")
end)
coroutine.resume(co)
coroutine.resume(co)
```

**基本写法：coroutine.yield 挂起协程**
`coroutine.yield(<value>)`
```lua
-- 挂起协程并返回值
local co = coroutine.create(function()
    coroutine.yield("第一个值")
    coroutine.yield("第二个值")
end)
local _, v1 = coroutine.resume(co)
local _, v2 = coroutine.resume(co)
```

**基本写法：coroutine.status 获取状态**
`coroutine.status(<coroutine>)`
```lua
-- 获取协程状态
local co = coroutine.create(function()
    coroutine.yield()
end)
print(coroutine.status(co))
coroutine.resume(co)
print(coroutine.status(co))
```

**基本写法：coroutine.wrap 调用**
`<wrapped>()`
```lua
-- wrap 创建的协程直接调用
local co = coroutine.wrap(function()
    coroutine.yield("A")
    coroutine.yield("B")
end)
print(co())
print(co())
```

---

## 协程通信

**基本写法：resume 传递参数**
`coroutine.resume(<coroutine>, <value>)`
```lua
-- resume 传递参数给 yield
local co = coroutine.create(function(a)
    local b = coroutine.yield(a + 1)
    return b + 1
end)
print(coroutine.resume(co, 10))
print(coroutine.resume(co, 20))
```

**基本写法：yield 返回多值**
`coroutine.yield(<val1>, <val2>)`
```lua
-- yield 返回多个值
local co = coroutine.create(function()
    coroutine.yield(1, 2, 3)
end)
local _, a, b, c = coroutine.resume(co)
```

**基本写法：resume 返回状态**
`local <ok>, <value> = coroutine.resume(<coroutine>)`
```lua
-- resume 返回成功状态和值
local co = coroutine.create(function()
    return "完成"
end)
local ok, result = coroutine.resume(co)
```

---

## 协程状态

**基本写法：suspended 挂起状态**
`coroutine.status(<coroutine>) == "suspended"`
```lua
-- 检查协程是否挂起
local co = coroutine.create(function()
    coroutine.yield()
end)
if coroutine.status(co) == "suspended" then
    coroutine.resume(co)
end
```

**基本写法：running 运行状态**
`coroutine.status(<coroutine>) == "running"`
```lua
-- 检查协程是否运行
local co = coroutine.create(function()
    if coroutine.status(co) == "running" then
        print("正在运行")
    end
end)
coroutine.resume(co)
```

**基本写法：dead 结束状态**
`coroutine.status(<coroutine>) == "dead"`
```lua
-- 检查协程是否结束
local co = coroutine.create(function()
    print("执行完毕")
end)
coroutine.resume(co)
if coroutine.status(co) == "dead" then
    print("协程已结束")
end
```

**基本写法：coroutine.running 获取当前协程**
`coroutine.running()`
```lua
-- 获取当前运行的协程
local co = coroutine.create(function()
    local current = coroutine.running()
    print(current == co)
end)
coroutine.resume(co)
```

---

## 生成器模式

**基本写法：生成器函数**
`local function <generator>(<params>) return coroutine.wrap(function() <body with yield> end) end`
```lua
-- 生成器函数
local function range(start, stop, step)
    step = step or 1
    return coroutine.wrap(function()
        for i = start, stop, step do
            coroutine.yield(i)
        end
    end)
end
```

**基本写法：生成器遍历**
`for <value> in <generator>(<args>) do <body> end`
```lua
-- 遍历生成器
for v in range(1, 5) do
    print(v)
end
```

**基本写法：无限生成器**
`local function <generator>() return coroutine.wrap(function() while true do coroutine.yield(<value>) end end) end`
```lua
-- 无限生成器
local function counter()
    local i = 0
    return coroutine.wrap(function()
        while true do
            i = i + 1
            coroutine.yield(i)
        end
    end)
end
```

---

## 协程迭代器

**基本写法：协程作为迭代器**
`local function <iterator>(<collection>) return coroutine.wrap(function() for <k>, <v> in pairs(<collection>) do coroutine.yield(<k>, <v>) end end) end`
```lua
-- 协程作为迭代器
local function pairsByValue(t)
    local sorted = {}
    for k, v in pairs(t) do
        sorted[#sorted + 1] = {k = k, v = v}
    end
    table.sort(sorted, function(a, b) return a.v < b.v end)
    return coroutine.wrap(function()
        for _, item in ipairs(sorted) do
            coroutine.yield(item.k, item.v)
        end
    end)
end
```

**基本写法：协程遍历树**
`local function <traverse>(<tree>) return coroutine.wrap(function() <recursive yield> end) end`
```lua
-- 协程遍历树结构
local function traverse(node)
    return coroutine.wrap(function()
        if node then
            for _, child in ipairs(node.children or {}) do
                for k, v in traverse(child) do
                    coroutine.yield(k, v)
                end
            end
            coroutine.yield(node.value)
        end
    end)
end
```

---

## 异步模拟

**基本写法：异步任务模拟**
`local function <asyncTask>(<params>) <coroutine with yield> end`
```lua
-- 异步任务模拟
local function asyncTask(name, duration)
    return coroutine.create(function()
        print(name .. " 开始")
        coroutine.yield()
        print(name .. " 完成")
    end)
end
```

**基本写法：任务调度器**
`local function <scheduler>(<tasks>) <body> end`
```lua
-- 简单任务调度器
local function scheduler(tasks)
    while true do
        local allDead = true
        for _, co in ipairs(tasks) do
            if coroutine.status(co) ~= "dead" then
                allDead = false
                coroutine.resume(co)
            end
        end
        if allDead then break end
    end
end
```

**基本写法：并行执行**
`local function <parallel>(<funcs>) <body> end`
```lua
-- 并行执行多个函数
local function parallel(funcs)
    local coroutines = {}
    for i, func in ipairs(funcs) do
        coroutines[i] = coroutine.create(func)
    end
    while true do
        local allDead = true
        for _, co in ipairs(coroutines) do
            if coroutine.status(co) ~= "dead" then
                allDead = false
                coroutine.resume(co)
            end
        end
        if allDead then break end
    end
end
```

---

## 协程错误处理

**基本写法：resume 错误捕获**
`local <ok>, <err> = coroutine.resume(<coroutine>)`
```lua
-- resume 捕获协程错误
local co = coroutine.create(function()
    error("协程错误")
end)
local ok, err = coroutine.resume(co)
if not ok then
    print("错误: " .. err)
end
```

**基本写法：协程内 pcall**
`pcall(function() <body> end)`
```lua
-- 协程内使用 pcall
local co = coroutine.create(function()
    local ok, err = pcall(function()
        error("处理错误")
    end)
    if not ok then
        print("捕获: " .. err)
    end
end)
coroutine.resume(co)
```

---

## 协程实战

**基本写法：生产者消费者**
`local function <producer>() <coroutine> end; local function <consumer>(<producer>) <body> end`
```lua
-- 生产者消费者模式
local function producer()
    for i = 1, 5 do
        coroutine.yield("产品" .. i)
    end
end
local function consume(producer)
    local co = coroutine.create(producer)
    while coroutine.status(co) ~= "dead" do
        local ok, product = coroutine.resume(co)
        if product then
            print("消费: " .. product)
        end
    end
end
```

**基本写法：管道**
`local function <pipe>(<source>, <filter>) <body> end`
```lua
-- 协程管道
local function pipe(source, filter)
    return coroutine.wrap(function()
        for value in source do
            local filtered = filter(value)
            if filtered then
                coroutine.yield(filtered)
            end
        end
    end)
end
```

**基本写法：超时控制**
`local function <withTimeout>(<func>, <timeout>) <body> end`
```lua
-- 协程超时控制
local function withTimeout(func, timeout)
    local co = coroutine.create(func)
    local start = os.time()
    while true do
        local ok, result = coroutine.resume(co)
        if coroutine.status(co) == "dead" then
            return result
        end
        if os.time() - start > timeout then
            return nil, "timeout"
        end
    end
end
```

---

## 协程与迭代器

**基本写法：协程生成迭代器**
`local function <iter>(<collection>) return coroutine.wrap(function() <body> end) end`
```lua
-- 协程生成迭代器
local function iter(t)
    return coroutine.wrap(function()
        for i, v in ipairs(t) do
            coroutine.yield(i, v)
        end
    end)
end
```

**基本写法：使用协程迭代器**
`for <k>, <v> in <iter>(<collection>) do <body> end`
```lua
-- 使用协程迭代器
local arr = {10, 20, 30}
for i, v in iter(arr) do
    print(i, v)
end
```



<!-- ============ 文档分隔线：017-lua/007-MetatableMetamethodDetailed.md ============ -->

# Lua 元表与元方法详解速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 元表基础

**基本写法：setmetatable 设置元表**
`setmetatable(<table>, <metatable>)`
```lua
-- 设置元表
local t = {}
local mt = {}
setmetatable(t, mt)
```

**基本写法：getmetatable 获取元表**
`getmetatable(<table>)`
```lua
-- 获取元表
local mt = getmetatable(t)
```

**基本写法：链式设置元表**
`local <table> = setmetatable({}, <metatable>)`
```lua
-- 创建表并设置元表
local obj = setmetatable({}, {
    __index = function(t, k)
        return "default"
    end
})
```

---

## 算术元方法

**基本写法：__add 加法**
`<metatable>.__add = function(<a>, <b>) <body> end`
```lua
-- 自定义加法运算
local mt = {}
mt.__add = function(a, b)
    return {value = a.value + b.value}
end
local v1 = setmetatable({value = 10}, mt)
local v2 = setmetatable({value = 20}, mt)
local result = v1 + v2
```

**基本写法：__sub 减法**
`<metatable>.__sub = function(<a>, <b>) <body> end`
```lua
-- 自定义减法运算
mt.__sub = function(a, b)
    return {value = a.value - b.value}
end
```

**基本写法：__mul 乘法**
`<metatable>.__mul = function(<a>, <b>) <body> end`
```lua
-- 自定义乘法运算
mt.__mul = function(a, b)
    return {value = a.value * b.value}
end
```

**基本写法：__div 除法**
`<metatable>.__div = function(<a>, <b>) <body> end`
```lua
-- 自定义除法运算
mt.__div = function(a, b)
    return {value = a.value / b.value}
end
```

**基本写法：__mod 取模**
`<metatable>.__mod = function(<a>, <b>) <body> end`
```lua
-- 自定义取模运算
mt.__mod = function(a, b)
    return {value = a.value % b.value}
end
```

**基本写法：__pow 幂运算**
`<metatable>.__pow = function(<a>, <b>) <body> end`
```lua
-- 自定义幂运算
mt.__pow = function(a, b)
    return {value = a.value ^ b.value}
end
```

**基本写法：__unm 一元负号**
`<metatable>.__unm = function(<a>) <body> end`
```lua
-- 自定义一元负号
mt.__unm = function(a)
    return {value = -a.value}
end
```

---

## 关系元方法

**基本写法：__eq 相等**
`<metatable>.__eq = function(<a>, <b>) <body> end`
```lua
-- 自定义相等比较
mt.__eq = function(a, b)
    return a.value == b.value
end
```

**基本写法：__lt 小于**
`<metatable>.__lt = function(<a>, <b>) <body> end`
```lua
-- 自定义小于比较
mt.__lt = function(a, b)
    return a.value < b.value
end
```

**基本写法：__le 小于等于**
`<metatable>.__le = function(<a>, <b>) <body> end`
```lua
-- 自定义小于等于比较
mt.__le = function(a, b)
    return a.value <= b.value
end
```

---

## 字符串元方法

**基本写法：__concat 连接**
`<metatable>.__concat = function(<a>, <b>) <body> end`
```lua
-- 自定义字符串连接
mt.__concat = function(a, b)
    return tostring(a.value) .. tostring(b.value)
end
```

**基本写法：__tostring 转字符串**
`<metatable>.__tostring = function(<a>) <body> end`
```lua
-- 自定义转字符串
mt.__tostring = function(a)
    return "Value(" .. a.value .. ")"
end
```

---

## 索引元方法

**基本写法：__index 表查找**
`<metatable>.__index = <table>`
```lua
-- __index 为表（继承）
local base = {greet = function() return "Hello" end}
local mt = {__index = base}
local obj = setmetatable({}, mt)
print(obj.greet())
```

**基本写法：__index 函数查找**
`<metatable>.__index = function(<table>, <key>) <body> end`
```lua
-- __index 为函数
local mt = {
    __index = function(t, key)
        return "Key not found: " .. key
    end
}
local obj = setmetatable({}, mt)
print(obj.missing)
```

**基本写法：__newindex 新索引**
`<metatable>.__newindex = <table>`
```lua
-- __newindex 为表（重定向）
local storage = {}
local mt = {__newindex = storage}
local obj = setmetatable({}, mt)
obj.x = 10
print(storage.x)
```

**基本写法：__newindex 函数拦截**
`<metatable>.__newindex = function(<table>, <key>, <value>) <body> end`
```lua
-- __newindex 为函数（拦截赋值）
local mt = {
    __newindex = function(t, key, value)
        if type(value) == "number" then
            rawset(t, key, value)
        end
    end
}
local obj = setmetatable({}, mt)
obj.x = 10
obj.y = "hello"
```

**基本写法：rawget 绕过元方法**
`rawget(<table>, <key>)`
```lua
-- rawget 绕过 __index
local obj = setmetatable({}, {__index = function() return "default" end})
print(rawget(obj, "x"))
```

**基本写法：rawset 绕过元方法**
`rawset(<table>, <key>, <value>)`
```lua
-- rawset 绕过 __newindex
local obj = setmetatable({}, {__newindex = function() end})
rawset(obj, "x", 10)
```

---

## 调用元方法

**基本写法：__call 可调用对象**
`<metatable>.__call = function(<self>, <params>) <body> end`
```lua
-- __call 使表可像函数一样调用
local mt = {
    __call = function(self, x)
        return x * self.factor
    end
}
local multiplier = setmetatable({factor = 2}, mt)
print(multiplier(5))
```

---

## 长度元方法

**基本写法：__len 长度**
`<metatable>.__len = function(<self>) <body> end`
```lua
-- __len 自定义长度运算
local mt = {
    __len = function(self)
        local count = 0
        for _ in pairs(self.data) do
            count = count + 1
        end
        return count
    end
}
local obj = setmetatable({data = {a = 1, b = 2}}, mt)
print(#obj)
```

---

## 迭代元方法

**基本写法：__pairs 自定义遍历**
`<metatable>.__pairs = function(<self>) <body> end`
```lua
-- __pairs 自定义 pairs 遍历
local mt = {
    __pairs = function(self)
        return coroutine.wrap(function()
            for k, v in pairs(self.data) do
                coroutine.yield(k, v)
            end
        end)
    end
}
local obj = setmetatable({data = {a = 1, b = 2}}, mt)
for k, v in pairs(obj) do
    print(k, v)
end
```

**基本写法：__ipairs 自定义数组遍历**
`<metatable>.__ipairs = function(<self>) <body> end`
```lua
-- __ipairs 自定义 ipairs 遍历
local mt = {
    __ipairs = function(self)
        return coroutine.wrap(function()
            for i, v in ipairs(self.items) do
                coroutine.yield(i, v)
            end
        end)
    end
}
local obj = setmetatable({items = {10, 20, 30}}, mt)
for i, v in ipairs(obj) do
    print(i, v)
end
```

---

## 类型元方法

**基本写法：__type 类型判断**
`<metatable>.__type = "<type>"`
```lua
-- __type 自定义类型（需要库支持）
local mt = {__type = "Vector"}
local v = setmetatable({x = 1, y = 2}, mt)
```

---

## 元表保护

**基本写法：__metatable 保护元表**
`<metatable>.__metatable = "<value>"`
```lua
-- __metatable 保护元表不被修改
local mt = {__index = {}, __metatable = "protected"}
local obj = setmetatable({}, mt)
print(getmetatable(obj))
```

---

## 元表组合

**换行写法：多元方法元表**
`local <mt> = { __index = <...>, __newindex = <...>, __add = <...>, __tostring = <...> }`
```lua
-- 组合多个元方法
local mt = {
    __index = function(t, k) return nil end,
    __newindex = function(t, k, v) rawset(t, k, v) end,
    __add = function(a, b) return setmetatable({}, getmetatable(a)) end,
    __tostring = function(a) return "Object" end
}
local obj = setmetatable({}, mt)
```

---

## 元表继承

**基本写法：元表链式继承**
`setmetatable(<child>, {__index = <parent>})`
```lua
-- 元表链式继承
local animal = {sound = "Some sound"}
local dog = setmetatable({}, {__index = animal})
print(dog.sound)
```

**基本写法：多级继承**
`setmetatable(<child>, {__index = <parent>}); setmetatable(<parent>, {__index = <grandparent>})`
```lua
-- 多级继承
local creature = {alive = true}
local animal = setmetatable({sound = "Some sound"}, {__index = creature})
local dog = setmetatable({breed = "Lab"}, {__index = animal})
print(dog.alive)
print(dog.sound)
```

---

## 元表实战

**基本写法：向量运算**
`local <mt> = { __add = <...>, __sub = <...>, __tostring = <...> }`
```lua
-- 向量运算元表
local Vector = {}
Vector.__index = Vector
Vector.__add = function(a, b)
    return Vector.new(a.x + b.x, a.y + b.y)
end
Vector.__tostring = function(v)
    return "(" .. v.x .. ", " .. v.y .. ")"
end
function Vector.new(x, y)
    return setmetatable({x = x, y = y}, Vector)
end
```

**基本写法：只读表**
`local <mt> = { __index = <table>, __newindex = function() error("...") end }`
```lua
-- 只读表实现
local function readOnly(t)
    local mt = {
        __index = t,
        __newindex = function(t, k, v)
            error("attempt to update a read-only table", 2)
        end
    }
    return setmetatable({}, mt)
end
```

**基本写法：默认值表**
`local <mt> = { __index = function() return <default> end }`
```lua
-- 默认值表
local function defaultTable(default)
    return setmetatable({}, {
        __index = function(t, k)
            return default
        end
    })
end
```



<!-- ============ 文档分隔线：017-lua/008-StringPatternMatching.md ============ -->

# Lua 字符串模式匹配速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 字符串基础

**基本写法：字符串长度**
`#<string>`
```lua
-- 获取字符串长度
local len = #"Hello, Lua"
```

**基本写法：string.len 获取长度**
`string.len(<string>)`
```lua
-- string.len 获取长度
local len = string.len("Hello")
```

**基本写法：字符串连接**
`<str1> .. <str2>`
```lua
-- 字符串连接
local result = "Hello" .. ", " .. "Lua"
```

**基本写法：字符串重复**
`string.rep(<string>, <n>)`
```lua
-- 字符串重复
local repeated = string.rep("ab", 3)
```

---

## 大小写转换

**基本写法：转大写**
`string.upper(<string>)`
```lua
-- 转大写
local upper = string.upper("Hello")
```

**基本写法：转小写**
`string.lower(<string>)`
```lua
-- 转小写
local lower = string.lower("Hello")
```

**基本写法：方法调用转大写**
`<string>:upper()`
```lua
-- 方法调用转大写
local upper = ("Hello"):upper()
```

---

## 子字符串

**基本写法：string.sub 截取**
`string.sub(<string>, <start>, <end>)`
```lua
-- 截取子字符串
local sub = string.sub("Hello, Lua", 1, 5)
```

**基本写法：从末尾截取**
`string.sub(<string>, -<n>)`
```lua
-- 从末尾截取
local sub = string.sub("Hello, Lua", -3)
```

**基本写法：截取中间部分**
`string.sub(<string>, <start>, -<n>)`
```lua
-- 截取中间部分
local sub = string.sub("Hello, Lua", 2, -2)
```

---

## 查找与匹配

**基本写法：string.find 查找**
`string.find(<string>, <pattern>)`
```lua
-- 查找字符串
local start, endPos = string.find("Hello, Lua", "Lua")
```

**基本写法：string.find 带起始位置**
`string.find(<string>, <pattern>, <init>)`
```lua
-- 从指定位置开始查找
local start, endPos = string.find("Hello, Lua", "l", 4)
```

**基本写法：string.find 模式匹配**
`string.find(<string>, "<pattern>")`
```lua
-- 模式匹配查找
local start, endPos = string.find("Hello 123", "%d+")
```

**基本写法：string.find 捕获**
`string.find(<string>, "(<pattern>)")`
```lua
-- 捕获匹配内容
local start, endPos, capture = string.find("Hello, Lua", "(Lua)")
```

**基本写法：string.match 匹配**
`string.match(<string>, <pattern>)`
```lua
-- 匹配字符串
local result = string.match("Hello 123", "%d+")
```

**基本写法：string.match 捕获**
`string.match(<string>, "(<pattern>)")`
```lua
-- 捕获匹配内容
local result = string.match("Hello, Lua", "(%w+), (%w+)")
```

---

## 替换

**基本写法：string.gsub 替换**
`string.gsub(<string>, <pattern>, <replacement>)`
```lua
-- 替换字符串
local result, count = string.gsub("Hello, Lua", "Lua", "World")
```

**基本写法：string.gsub 限制替换次数**
`string.gsub(<string>, <pattern>, <replacement>, <n>)`
```lua
-- 限制替换次数
local result = string.gsub("aaa", "a", "b", 2)
```

**基本写法：string.gsub 捕获替换**
`string.gsub(<string>, "(<pattern>)", <replacement>)`
```lua
-- 使用捕获替换
local result = string.gsub("Hello, Lua", "(%w+)", "[%1]")
```

**基本写法：string.gsub 函数替换**
`string.gsub(<string>, <pattern>, <function>)`
```lua
-- 使用函数替换
local result = string.gsub("Hello 123", "%d+", function(s)
    return tonumber(s) * 2
end)
```

---

## 分割与拆分

**基本写法：字符串分割**
`local function <name>(<str>, <sep>) <body> end`
```lua
-- 字符串分割
local function split(str, sep)
    local result = {}
    for part in string.gmatch(str, "[^" .. sep .. "]+") do
        result[#result + 1] = part
    end
    return result
end
```

**基本写法：string.gmatch 遍历匹配**
`for <match> in string.gmatch(<string>, <pattern>) do <body> end`
```lua
-- gmatch 遍历所有匹配
for word in string.gmatch("Hello, World, Lua", "%w+") do
    print(word)
end
```

**基本写法：string.gmatch 捕获遍历**
`for <cap1>, <cap2> in string.gmatch(<string>, <pattern>) do <body> end`
```lua
-- gmatch 捕获遍历
for key, value in string.gmatch("a=1, b=2, c=3", "(%w+)=(%w+)") do
    print(key, value)
end
```

---

## 格式化

**基本写法：string.format 格式化**
`string.format(<format>, <args>)`
```lua
-- 字符串格式化
local result = string.format("Name: %s, Age: %d", "Alice", 25)
```

**基本写法：格式化数字**
`string.format("<format>", <number>)`
```lua
-- 格式化数字
local result = string.format("%.2f", 3.14159)
```

**基本写法：格式化补齐**
`string.format("<format>", <string>)`
```lua
-- 字符串补齐
local result = string.format("%10s", "Lua")
```

**基本写法：格式化十六进制**
`string.format("<format>", <number>)`
```lua
-- 格式化为十六进制
local result = string.format("%x", 255)
```

---

## 模式字符类

**基本写法：%a 字母**
`string.match(<string>, "%a+")`
```lua
-- 匹配字母
local result = string.match("Hello123", "%a+")
```

**基本写法：%d 数字**
`string.match(<string>, "%d+")`
```lua
-- 匹配数字
local result = string.match("Hello123", "%d+")
```

**基本写法：%w 字母数字**
`string.match(<string>, "%w+")`
```lua
-- 匹配字母数字
local result = string.match("Hello_123", "%w+")
```

**基本写法：%s 空白**
`string.match(<string>, "%s+")`
```lua
-- 匹配空白字符
local result = string.match("Hello World", "%s+")
```

**基本写法：%p 标点**
`string.match(<string>, "%p")`
```lua
-- 匹配标点符号
local result = string.match("Hello, World", "%p")
```

**基本写法：%l 小写字母**
`string.match(<string>, "%l+")`
```lua
-- 匹配小写字母
local result = string.match("HelloWorld", "%l+")
```

**基本写法：%u 大写字母**
`string.match(<string>, "%u+")`
```lua
-- 匹配大写字母
local result = string.match("HelloWorld", "%u+")
```

**基本写法：大写字符类取反**
`string.match(<string>, "%D+")`
```lua
-- %D 匹配非数字
local result = string.match("abc123", "%D+")
```

---

## 模式锚点

**基本写法：^ 开头锚定**
`string.match(<string>, "^<pattern>")`
```lua
-- 匹配字符串开头
local result = string.match("Hello World", "^%w+")
```

**基本写法：$ 结尾锚定**
`string.match(<string>, "<pattern>$")`
```lua
-- 匹配字符串结尾
local result = string.match("Hello World", "%w+$")
```

---

## 模式量词

**基本写法：* 零次或多次**
`string.match(<string>, "<pattern>*")`
```lua
-- 匹配零次或多次
local result = string.match("aaa", "a*")
```

**基本写法：+ 一次或多次**
`string.match(<string>, "<pattern>+")`
```lua
-- 匹配一次或多次
local result = string.match("aaa", "a+")
```

**基本写法：- 零次或多次（最小匹配）**
`string.match(<string>, "<pattern>-")`
```lua
-- 最小匹配
local result = string.match("<a><b>", "<.->")
```

**基本写法：? 零次或一次**
`string.match(<string>, "<pattern>?")`
```lua
-- 匹配零次或一次
local result = string.match("color", "colou?r")
```

---

## 字符集

**基本写法：字符集**
`string.match(<string>, "[<chars>]")`
```lua
-- 匹配字符集中的任意字符
local result = string.match("Hello", "[aeiou]")
```

**基本写法：字符范围**
`string.match(<string>, "[<start>-<end>]")`
```lua
-- 匹配字符范围
local result = string.match("Hello", "[a-z]")
```

**基本写法：取反字符集**
`string.match(<string>, "[^<chars>]")`
```lua
-- 匹配不在字符集中的字符
local result = string.match("Hello", "[^aeiou]")
```

---

## 捕获

**基本写法：基本捕获**
`string.match(<string>, "(<pattern>)")`
```lua
-- 捕获匹配内容
local result = string.match("Hello, Lua", "(%w+)")
```

**基本写法：多捕获**
`string.match(<string>, "(<p1>) (<p2>)")`
```lua
-- 多个捕获
local a, b = string.match("key=value", "(%w+)=(%w+)")
```

**基本写法：捕获引用**
`string.gsub(<string>, "(<pattern>)", "%<n>")`
```lua
-- 引用捕获内容
local result = string.gsub("Hello, Lua", "(%w+)", "[%1]")
```

**基本写法：位置捕获**
`string.find(<string>, "()<pattern>()")`
```lua
-- 捕获位置
local start, _, pos = string.find("Hello", "()l")
```

---

## 字符编码

**基本写法：string.byte 获取字节**
`string.byte(<string>, <pos>)`
```lua
-- 获取字符的字节值
local code = string.byte("A")
```

**基本写法：string.char 转字符**
`string.char(<code>)`
```lua
-- 字节值转字符
local char = string.char(65)
```

**基本写法：多字节转换**
`string.char(<code1>, <code2>)`
```lua
-- 多个字节值转字符串
local str = string.char(72, 105)
```

---

## 实用函数

**基本写法：trim 去除空白**
`local function <name>(<str>) <body> end`
```lua
-- 去除首尾空白
local function trim(s)
    return s:match("^%s*(.-)%s*$")
end
```

**基本写法：startsWith 检查前缀**
`string.sub(<str>, 1, #<prefix>) == <prefix>`
```lua
-- 检查字符串前缀
local function startsWith(str, prefix)
    return string.sub(str, 1, #prefix) == prefix
end
```

**基本写法：endsWith 检查后缀**
`string.sub(<str>, -#<suffix>) == <suffix>`
```lua
-- 检查字符串后缀
local function endsWith(str, suffix)
    return string.sub(str, -#suffix) == suffix
end
```

**基本写法：contains 检查包含**
`string.find(<str>, <substr>, 1, true) ~= nil`
```lua
-- 检查字符串包含（纯文本查找）
local function contains(str, substr)
    return string.find(str, substr, 1, true) ~= nil
end
```

**基本写法：reverse 反转字符串**
`string.reverse(<string>)`
```lua
-- 反转字符串
local reversed = string.reverse("Hello")
```

**基本写法：padLeft 左补齐**
`string.rep(<pad>, <n>) .. <str>`
```lua
-- 左侧补齐
local function padLeft(str, len, pad)
    pad = pad or " "
    local padding = string.rep(pad, len - #str)
    return padding .. str
end
```



<!-- ============ 文档分隔线：017-lua/009-LuaErrorHandling.md ============ -->

# Lua 错误处理速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## error 函数

**基本写法：error 抛出错误**
`error("<message>")`
```lua
-- 抛出错误
error("发生错误")
```

**基本写法：error 带错误级别**
`error("<message>", <level>)`
```lua
-- 指定错误级别（1=调用位置，2=调用者的调用位置）
error("参数错误", 2)
```

**基本写法：error 抛出表**
`error({code = <code>, message = "<msg>"})`
```lua
-- 抛出表作为错误对象
error({code = 404, message = "Not Found"})
```

---

## pcall 错误捕获

**基本写法：pcall 保护调用**
`pcall(<function>, <args>)`
```lua
-- pcall 保护调用函数
local ok, result = pcall(function()
    return 10 / 0
end)
if not ok then
    print("错误: " .. result)
end
```

**基本写法：pcall 带参数**
`pcall(<function>, <arg1>, <arg2>)`
```lua
-- pcall 传递参数给函数
local function divide(a, b)
    if b == 0 then error("除零错误") end
    return a / b
end
local ok, result = pcall(divide, 10, 0)
```

**基本写法：pcall 多返回值**
`local <ok>, <r1>, <r2> = pcall(<function>, <args>)`
```lua
-- pcall 捕获多返回值
local function getCoords()
    return 10, 20
end
local ok, x, y = pcall(getCoords)
```

**基本写法：pcall 错误处理**
`if not <ok> then <body> end`
```lua
-- pcall 错误处理
local ok, err = pcall(function()
    error("处理失败")
end)
if not ok then
    print("捕获错误: " .. err)
end
```

---

## xpcall 错误捕获

**基本写法：xpcall 带错误处理函数**
`xpcall(<function>, <handler>)`
```lua
-- xpcall 带错误处理函数
local function errorHandler(err)
    print("错误: " .. err)
    return "处理后"
end
local ok, result = xpcall(function()
    error("发生错误")
end, errorHandler)
```

**基本写法：xpcall 带参数**
`xpcall(<function>, <handler>, <arg>)`
```lua
-- xpcall 传递参数给函数
local function process(data)
    if not data then error("数据为空") end
    return data
end
local ok, result = xpcall(process, errorHandler, "Hello")
```

**基本写法：xpcall 多参数**
`xpcall(<function>, <handler>, <arg1>, <arg2>)`
```lua
-- xpcall 传递多个参数
local function add(a, b)
    if type(a) ~= "number" then error("参数类型错误") end
    return a + b
end
local ok, result = xpcall(add, errorHandler, 10, 20)
```

---

## assert 断言

**基本写法：assert 基本断言**
`assert(<condition>)`
```lua
-- assert 断言条件为真
assert(x > 0)
```

**基本写法：assert 带错误消息**
`assert(<condition>, "<message>")`
```lua
-- assert 带自定义错误消息
assert(x > 0, "x 必须大于 0")
```

**基本写法：assert 检查返回值**
`local <result> = assert(<func>(<args>))`
```lua
-- assert 检查函数返回值
local file = assert(io.open("test.txt", "r"))
```

**基本写法：assert 带格式化消息**
`assert(<condition>, string.format("<format>", <args>))`
```lua
-- assert 带格式化错误消息
assert(age >= 18, string.format("年龄 %d 不满足要求", age))
```

---

## 错误对象

**基本写法：错误对象表**
`error({code = <code>, message = "<msg>"})`
```lua
-- 错误对象表
local function createError(code, message)
    return {code = code, message = message}
end
error(createError(500, "服务器错误"))
```

**基本写法：错误对象处理**
`if type(<err>) == "table" then <body> end`
```lua
-- 处理错误对象
local ok, err = pcall(function()
    error({code = 404, message = "Not Found"})
end)
if not ok and type(err) == "table" then
    print("错误码: " .. err.code)
    print("错误信息: " .. err.message)
end
```

---

## 错误传播

**基本写法：函数内错误传播**
`if <cond> then error("<msg>") end`
```lua
-- 函数内检查并抛出错误
local function process(data)
    if not data then
        error("数据不能为空")
    end
    return data.value
end
```

**基本写法：嵌套错误捕获**
`local <ok>, <err> = pcall(function() <body with nested pcall> end)`
```lua
-- 嵌套错误捕获
local function outerFunc()
    local ok, err = pcall(function()
        error("内部错误")
    end)
    if not ok then
        error("外部错误: " .. err)
    end
end
local ok, err = pcall(outerFunc)
```

---

## finally 模拟

**基本写法：finally 模拟**
`local <ok>, <err> = pcall(<function>); <cleanup>; if not <ok> then error(<err>) end`
```lua
-- 模拟 finally 清理
local function withCleanup(func, cleanup)
    local ok, err = pcall(func)
    cleanup()
    if not ok then
        error(err)
    end
end
```

**基本写法：资源清理**
`local <ok>, <err> = pcall(<function>); <resource>:close(); if not <ok> then error(<err>) end`
```lua
-- 资源清理模式
local function processFile(filename)
    local file = io.open(filename, "r")
    if not file then error("无法打开文件") end
    local ok, err = pcall(function()
        return file:read("*a")
    end)
    file:close()
    if not ok then error(err) end
end
```

---

## 错误处理模式

**基本写法：返回错误模式**
`local function <name>(<params>) if <cond> then return nil, "<error>" end return <result> end`
```lua
-- 返回 nil 和错误信息
local function divide(a, b)
    if b == 0 then
        return nil, "除零错误"
    end
    return a / b
end
local result, err = divide(10, 0)
```

**基本写法：错误码模式**
`local function <name>(<params>) if <cond> then return false, <code> end return true, <result> end`
```lua
-- 返回成功状态和错误码
local function validate(data)
    if not data then
        return false, 1
    end
    if #data == 0 then
        return false, 2
    end
    return true, data
end
```

**基本写法：Result 模式**
`local function <name>(<params>) return {ok = <bool>, value = <value>, err = <err>} end`
```lua
-- Result 对象模式
local function safeDivide(a, b)
    if b == 0 then
        return {ok = false, err = "除零错误"}
    end
    return {ok = true, value = a / b}
end
```

---

## 错误日志

**基本写法：错误日志记录**
`local function <logError>(<err>) <body> end`
```lua
-- 错误日志记录函数
local function logError(err)
    local log = io.open("error.log", "a")
    if log then
        log:write(os.date("%Y-%m-%d %H:%M:%S") .. " - " .. tostring(err) .. "\n")
        log:close()
    end
end
```

**基本写法：pcall 与日志结合**
`local <ok>, <err> = pcall(<function>); if not <ok> then <logError>(<err>) end`
```lua
-- pcall 与日志结合
local ok, err = pcall(function()
    error("处理失败")
end)
if not ok then
    logError(err)
end
```

---

## debug 追踪

**基本写法：debug.traceback 获取堆栈**
`debug.traceback("<message>")`
```lua
-- 获取错误堆栈追踪
local function funcA()
    error("错误发生")
end
local function funcB()
    funcA()
end
local ok, err = pcall(funcB)
print(debug.traceback(err))
```

**基本写法：xpcall 中获取堆栈**
`xpcall(<function>, function(<err>) return debug.traceback(<err>) end)`
```lua
-- xpcall 中获取堆栈追踪
local ok, err = xpcall(function()
    error("错误")
end, function(err)
    return debug.traceback(err, 2)
end)
```

**基本写法：debug.getinfo 获取函数信息**
`debug.getinfo(<function>)`
```lua
-- 获取函数信息
local function testFunc() end
local info = debug.getinfo(testFunc)
print(info.name, info.source, info.linedefined)
```

---

## 错误处理实战

**基本写法：安全调用**
`local function <safeCall>(<func>, <args>) <body> end`
```lua
-- 安全调用函数
local function safeCall(func, ...)
    local ok, result = pcall(func, ...)
    if not ok then
        print("调用失败: " .. tostring(result))
        return nil
    end
    return result
end
```

**基本写法：重试机制**
`local function <retry>(<func>, <times>) <body> end`
```lua
-- 重试机制
local function retry(func, times)
    local ok, err
    for i = 1, times do
        ok, err = pcall(func)
        if ok then return err end
    end
    return nil, err
end
```

**基本写法：错误链**
`local function <chain>(<funcs>) <body> end`
```lua
-- 错误链处理
local function chain(funcs)
    for _, func in ipairs(funcs) do
        local ok, err = pcall(func)
        if not ok then
            return nil, err
        end
    end
    return true
end
```



<!-- ============ 文档分隔线：017-lua/010-LuaIterator.md ============ -->

# Lua 迭代器速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 泛型 for 迭代器

**基本写法：for-in 迭代器**
`for <var> in <iterator> do <body> end`
```lua
-- 泛型 for 迭代器
for value in iter({1, 2, 3}) do
    print(value)
end
```

**基本写法：for-in 多变量迭代器**
`for <var1>, <var2> in <iterator> do <body> end`
```lua
-- 多变量迭代器
for key, value in pairs({a = 1, b = 2}) do
    print(key, value)
end
```

**基本写法：for-in 带状态迭代器**
`for <var> in <iterator>, <state>, <init> do <body> end`
```lua
-- 带状态和初始值的迭代器
for value in function(t, i) i = i + 1; return t[i] end, {10, 20, 30}, 0 do
    print(value)
end
```

---

## 内置迭代器

**基本写法：ipairs 数组迭代器**
`ipairs(<table>)`
```lua
-- ipairs 遍历数组部分
local arr = {"a", "b", "c"}
for i, v in ipairs(arr) do
    print(i, v)
end
```

**基本写法：pairs 表迭代器**
`pairs(<table>)`
```lua
-- pairs 遍历表所有键值对
local t = {name = "Alice", age = 25}
for k, v in pairs(t) do
    print(k, v)
end
```

**基本写法：string.gmatch 字符串迭代器**
`string.gmatch(<string>, <pattern>)`
```lua
-- gmatch 遍历字符串匹配
for word in string.gmatch("Hello World Lua", "%w+") do
    print(word)
end
```

**基本写法：io.lines 文件行迭代器**
`io.lines(<filename>)`
```lua
-- io.lines 遍历文件行
for line in io.lines("test.txt") do
    print(line)
end
```

---

## 自定义迭代器

**基本写法：闭包迭代器**
`local function <iterator>(<collection>) return function() <body with yield> end end`
```lua
-- 闭包迭代器
local function range(start, stop, step)
    step = step or 1
    local i = start - step
    return function()
        i = i + step
        if i <= stop then
            return i
        end
    end
end
```

**基本写法：使用闭包迭代器**
`for <var> in <iterator>(<args>) do <body> end`
```lua
-- 使用闭包迭代器
for i in range(1, 5) do
    print(i)
end
```

**基本写法：状态迭代器**
`local function <iterator>(<state>, <control>) <body> end`
```lua
-- 无状态迭代器
local function iter(t, i)
    i = i + 1
    local v = t[i]
    if v then
        return i, v
    end
end
```

**基本写法：使用状态迭代器**
`for <k>, <v> in <iterator>, <collection>, 0 do <body> end`
```lua
-- 使用无状态迭代器
local arr = {10, 20, 30}
for i, v in iter, arr, 0 do
    print(i, v)
end
```

---

## 协程迭代器

**基本写法：协程迭代器**
`local function <iterator>(<collection>) return coroutine.wrap(function() <body with yield> end) end`
```lua
-- 协程迭代器
local function iter(t)
    return coroutine.wrap(function()
        for i, v in ipairs(t) do
            coroutine.yield(i, v)
        end
    end)
end
```

**基本写法：使用协程迭代器**
`for <k>, <v> in <iterator>(<collection>) do <body> end`
```lua
-- 使用协程迭代器
local arr = {10, 20, 30}
for i, v in iter(arr) do
    print(i, v)
end
```

**基本写法：协程生成器迭代器**
`local function <generator>(<params>) return coroutine.wrap(function() <body> end) end`
```lua
-- 协程生成器迭代器
local function fibonacci(n)
    return coroutine.wrap(function()
        local a, b = 0, 1
        for i = 1, n do
            coroutine.yield(a)
            a, b = b, a + b
        end
    end)
end
```

---

## 数组迭代器

**基本写法：数组遍历迭代器**
`local function <iter>(<array>) return function() <body> end end`
```lua
-- 数组遍历迭代器
local function elements(arr)
    local i = 0
    return function()
        i = i + 1
        return arr[i]
    end
end
```

**基本写法：反向遍历迭代器**
`local function <reverseIter>(<array>) return function() <body> end end`
```lua
-- 反向遍历迭代器
local function reverse(arr)
    local i = #arr + 1
    return function()
        i = i - 1
        if i >= 1 then
            return arr[i]
        end
    end
end
```

**基本写法：带步长迭代器**
`local function <stepIter>(<array>, <step>) return function() <body> end end`
```lua
-- 带步长迭代器
local function stepIter(arr, step)
    local i = 1 - step
    return function()
        i = i + step
        if i <= #arr then
            return arr[i]
        end
    end
end
```

---

## 表迭代器

**基本写法：按键排序迭代器**
`local function <sortedPairs>(<table>) return function() <body> end end`
```lua
-- 按键排序遍历
local function sortedPairs(t)
    local keys = {}
    for k in pairs(t) do
        keys[#keys + 1] = k
    end
    table.sort(keys)
    local i = 0
    return function()
        i = i + 1
        local k = keys[i]
        if k then
            return k, t[k]
        end
    end
end
```

**基本写法：按值排序迭代器**
`local function <sortedByValue>(<table>) return function() <body> end end`
```lua
-- 按值排序遍历
local function sortedByValue(t)
    local items = {}
    for k, v in pairs(t) do
        items[#items + 1] = {k = k, v = v}
    end
    table.sort(items, function(a, b) return a.v < b.v end)
    local i = 0
    return function()
        i = i + 1
        local item = items[i]
        if item then
            return item.k, item.v
        end
    end
end
```

**基本写法：过滤迭代器**
`local function <filterIter>(<table>, <predicate>) return function() <body> end end`
```lua
-- 过滤迭代器
local function filterPairs(t, predicate)
    local co = coroutine.wrap(function()
        for k, v in pairs(t) do
            if predicate(k, v) then
                coroutine.yield(k, v)
            end
        end
    end)
    return co
end
```

---

## 无限迭代器

**基本写法：无限计数器**
`local function <counter>() return function() <body> end end`
```lua
-- 无限计数器
local function counter()
    local i = 0
    return function()
        i = i + 1
        return i
    end
end
```

**基本写法：循环迭代器**
`local function <cycle>(<array>) return function() <body> end end`
```lua
-- 循环迭代器
local function cycle(arr)
    local i = 0
    return function()
        i = i % #arr + 1
        return arr[i]
    end
end
```

**基本写法：使用 take 限制**
`local function <take>(<iterator>, <n>) return function() <body> end end`
```lua
-- take 限制迭代次数
local function take(iter, n)
    local count = 0
    return function()
        count = count + 1
        if count <= n then
            return iter()
        end
    end
end
```

---

## 迭代器组合

**基本写法：map 迭代器**
`local function <mapIter>(<iterator>, <func>) return function() <body> end end`
```lua
-- map 迭代器转换
local function mapIter(iter, func)
    return function()
        local value = iter()
        if value then
            return func(value)
        end
    end
end
```

**基本写法：filter 迭代器**
`local function <filterIter>(<iterator>, <predicate>) return function() <body> end end`
```lua
-- filter 迭代器过滤
local function filterIter(iter, predicate)
    return function()
        while true do
            local value = iter()
            if value == nil then return end
            if predicate(value) then
                return value
            end
        end
    end
end
```

**基本写法：chain 迭代器**
`local function <chain>(<iter1>, <iter2>) return function() <body> end end`
```lua
-- chain 链式迭代器
local function chain(iter1, iter2)
    return function()
        local value = iter1()
        if value then
            return value
        end
        return iter2()
    end
end
```

**基本写法：zip 迭代器**
`local function <zip>(<iter1>, <iter2>) return function() <body> end end`
```lua
-- zip 合并迭代器
local function zip(iter1, iter2)
    return function()
        local v1 = iter1()
        local v2 = iter2()
        if v1 and v2 then
            return v1, v2
        end
    end
end
```

---

## 迭代器工具函数

**基本写法：collect 收集为表**
`local function <collect>(<iterator>) <body> end`
```lua
-- 收集迭代器结果为表
local function collect(iter)
    local result = {}
    for value in iter do
        result[#result + 1] = value
    end
    return result
end
```

**基本写法：reduce 累积**
`local function <reduce>(<iterator>, <func>, <init>) <body> end`
```lua
-- reduce 累积迭代器结果
local function reduce(iter, func, init)
    local acc = init
    for value in iter do
        acc = func(acc, value)
    end
    return acc
end
```

**基本写法：forEach 遍历**
`local function <forEach>(<iterator>, <func>) <body> end`
```lua
-- forEach 遍历迭代器
local function forEach(iter, func)
    for value in iter do
        func(value)
    end
end
```

**基本写法：count 计数**
`local function <count>(<iterator>) <body> end`
```lua
-- count 计数迭代器元素
local function count(iter)
    local n = 0
    for _ in iter do
        n = n + 1
    end
    return n
end
```

---

## 迭代器实战

**基本写法：文件行迭代器**
`local function <lines>(<filename>) return function() <body> end end`
```lua
-- 文件行迭代器
local function lines(filename)
    local file = io.open(filename, "r")
    if not file then return nil end
    return function()
        local line = file:read("*l")
        if not line then
            file:close()
        end
        return line
    end
end
```

**基本写法：树遍历迭代器**
`local function <traverse>(<tree>) return coroutine.wrap(function() <body> end) end`
```lua
-- 树遍历迭代器
local function traverse(node)
    return coroutine.wrap(function()
        if node then
            coroutine.yield(node.value)
            for _, child in ipairs(node.children or {}) do
                for v in traverse(child) do
                    coroutine.yield(v)
                end
            end
        end
    end)
end
```

**基本写法：分块迭代器**
`local function <chunks>(<array>, <size>) return function() <body> end end`
```lua
-- 分块迭代器
local function chunks(arr, size)
    local i = 0
    return function()
        i = i + 1
        local start = (i - 1) * size + 1
        if start <= #arr then
            local chunk = {}
            for j = start, math.min(start + size - 1, #arr) do
                chunk[#chunk + 1] = arr[j]
            end
            return chunk
        end
    end
end
```



<!-- ============ 文档分隔线：017-lua/011-LuaStandardLibrary.md ============ -->

# Lua 标准库与协程速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## string 库

**基本写法：string.format 格式化**
`string.format("<格式串>", <参数>...)`
```lua
-- 格式化字符串
local s = string.format("Value: %d, Name: %s", 42, "Alice")
```

---

**基本写法：string.find 查找**
`string.find(<字符串>, "<模式>" [, <起始>])`
```lua
-- 查找子串
local start, finish = string.find("hello world", "world")
```

---

**基本写法：string.gsub 替换**
`string.gsub(<字符串>, "<模式>", "<替换>")`
```lua
-- 全局替换
local result = string.gsub("hello", "l", "L")
-- 返回 "heLLo"
```

---

**基本写法：string.match 匹配**
`string.match(<字符串>, "<模式>")`
```lua
-- 匹配数字
local num = string.match("abc 123", "%d+")
```

---

**基本写法：string.gmatch 迭代匹配**
`string.gmatch(<字符串>, "<模式>")`
```lua
-- 迭代所有匹配
for word in string.gmatch("one two three", "%a+") do
    print(word)
end
```

---

**基本写法：string.sub 子串**
`string.sub(<字符串>, <起始> [, <结束>])`
```lua
-- 截取子串
local s = string.sub("hello", 2, 4)  -- "ell"
```

---

**基本写法：string.rep 重复**
`string.rep(<字符串>, <次数>)`
```lua
-- 重复字符串
local s = string.rep("ab", 3)  -- "ababab"
```

---

## table 库

**基本写法：table.insert 插入**
`table.insert(<表>, [<位置>,] <值>)`
```lua
-- 末尾插入
table.insert(t, "item")
-- 指定位置插入
table.insert(t, 1, "first")
```

---

**基本写法：table.remove 移除**
`table.remove(<表> [, <位置>])`
```lua
-- 移除并返回末尾元素
local item = table.remove(t)
-- 移除指定位置
local item = table.remove(t, 1)
```

---

**基本写法：table.concat 拼接**
`table.concat(<表> [, <分隔符> [, <起始> [, <结束>]]])`
```lua
-- 数组拼接为字符串
local s = table.concat({"a", "b", "c"}, ", ")
```

---

**基本写法：table.sort 排序**
`table.sort(<表> [, <比较函数>])`
```lua
-- 升序排序
table.sort(t)
-- 自定义比较
table.sort(t, function(a, b) return a > b end)
```

---

**基本写法：table.unpack 展开**
`table.unpack(<表> [, <起始> [, <结束>]])`
```lua
-- 表展开为多返回值
local a, b, c = table.unpack({1, 2, 3})
```

---

## math 库

**基本写法：math.floor 向下取整**
`math.floor(<数值>)`
```lua
-- 向下取整
local n = math.floor(3.7)  -- 3
```

---

**基本写法：math.ceil 向上取整**
`math.ceil(<数值>)`
```lua
-- 向上取整
local n = math.ceil(3.2)  -- 4
```

---

**基本写法：math.random 随机数**
`math.random([<最小> [, <最大>]])`
```lua
-- 0 到 1 之间小数
local r = math.random()
-- 1 到 100 整数
local n = math.random(1, 100)
```

---

**基本写法：math.randomseed 设置种子**
`math.randomseed(<种子>)`
```lua
-- 设置随机种子
math.randomseed(os.time())
```

---

**基本写法：math.max/min 极值**
`math.max(<值1>, <值2>, ...)`
```lua
-- 最大值
local max = math.max(1, 5, 3)
-- 最小值
local min = math.min(1, 5, 3)
```

---

## io 库

**基本写法：io.open 打开文件**
`io.open("<路径>", "<模式>")`
```lua
-- 打开文件读取
local f = io.open("data.txt", "r")
-- 模式: r 读, w 写, a 追加, b 二进制
```

---

**基本写法：file:read 读取**
`<file>:read("<格式>")`
```lua
-- 读取一行
local line = f:read("*l")
-- 读取全部
local content = f:read("*a")
```

---

**基本写法：file:write 写入**
`<file>:write(<字符串>)`
```lua
-- 写入数据
f:write("Hello\n")
```

---

**基本写法：io.close 关闭**
`<file>:close()`
```lua
-- 关闭文件
f:close()
```

---

**基本写法：io.lines 行迭代器**
`io.lines("<路径>")`
```lua
-- 遍历文件每行
for line in io.lines("data.txt") do
    print(line)
end
```

---

## os 库

**基本写法：os.time 当前时间**
`os.time([<表>])`
```lua
-- 获取当前时间戳
local t = os.time()
```

---

**基本写法：os.date 格式化时间**
`os.date("<格式>" [, <时间>])`
```lua
-- 格式化日期
local date = os.date("%Y-%m-%d %H:%M:%S")
```

---

**基本写法：os.execute 执行命令**
`os.execute("<命令>")`
```lua
-- 执行系统命令
os.execute("mkdir newdir")
```

---

**基本写法：os.getenv 环境变量**
`os.getenv("<变量名>")`
```lua
-- 读取环境变量
local path = os.getenv("PATH")
```

---

## 协程库

**基本写法：coroutine.create 创建**
`coroutine.create(<函数>)`
```lua
-- 创建协程
local co = coroutine.create(function()
    print("Hello")
end)
```

---

**基本写法：coroutine.resume 恢复**
`coroutine.resume(<协程> [, <参数>...])`
```lua
-- 启动或恢复协程
coroutine.resume(co)
```

---

**基本写法：coroutine.yield 挂起**
`coroutine.yield(<值>)`
```lua
-- 挂起协程并返回值
coroutine.create(function()
    coroutine.yield(1)
    coroutine.yield(2)
end)
```

---

**基本写法：coroutine.status 状态**
`coroutine.status(<协程>)`
```lua
-- 获取协程状态
local status = coroutine.status(co)
-- 状态: suspended, running, dead, normal
```

---

**基本写法：coroutine.wrap 包装**
`coroutine.wrap(<函数>)`
```lua
-- 返回可直接调用的函数
local f = coroutine.wrap(function()
    coroutine.yield(1)
    coroutine.yield(2)
end)
print(f())  -- 1
print(f())  -- 2
```



<!-- ============ 文档分隔线：017-lua/012-FileIO.md ============ -->

# Lua 文件 IO 进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：017-lua/013-Lua54Features.md ============ -->

# Lua 5.4 新特性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## const 常量变量

**基本写法：声明常量**
`local <变量> <const> = <值>`
```lua
-- 声明后不可重新赋值
local PI <const> = 3.14159
```

---

**基本写法：const 变量重新赋值报错**
`-- 编译时错误`
```lua
local x <const> = 10
-- x = 20  -- 错误：attempt to assign to const variable 'x'
```

---

**基本写法：const 表内容可改**
`<常量表>[<键>] = <值>`
```lua
-- const 仅限制变量绑定，不限制表内容
local t <const> = {}
t[1] = 1            -- 合法
table.insert(t, 2)  -- 合法
-- t = {}  -- 非法，不能重新赋值变量本身
```

---

**基本写法：const 与函数参数**
`function f(<参数> <const>)`
```lua
-- 参数也可标记为 const
local function process(data <const>)
    -- data 不能在函数内被重新赋值
    return #data
end
```

---

## close 自动关闭变量

**基本写法：声明 close 变量**
`local <变量> <close> = <带__close的值>`
```lua
-- 离开作用域自动调用 __close
local f <close> = io.open("data.txt", "r")
local content = f:read("*a")
-- 离开作用域自动关闭文件
```

---

**基本写法：自定义 close 对象**
`local <变量> <close> = setmetatable({}, { __close = <函数> })`
```lua
-- 自定义资源清理逻辑
local res <close> = setmetatable({}, {
    __close = function(self)
        print("资源已释放")
    end
})
```

---

**基本写法：close 反向调用**
`-- 多个 close 变量按声明逆序释放`
```lua
-- 先声明的后关闭，类似 C++ RAII
do
    local a <close> = make_res("a")
    local b <close> = make_res("b")
end -- 先调用 b 的 __close，再调用 a 的 __close
```

---

**基本写法：close 与异常**
`-- 即使出错也会调用 __close`
```lua
-- 保护调用中 close 仍会触发
local function risky()
    local f <close> = io.open("x.txt", "r")
    error("运行出错")  -- __close 仍会被调用
end
pcall(risky)
```

---

**基本写法：close 错误捕获**
`__close = function(self, <err>)`
```lua
-- __close 第二参数接收错误对象
local obj <close> = setmetatable({}, {
    __close = function(self, err)
        if err then print("因异常关闭:", err) end
    end
})
```

---

## 分代垃圾回收

**基本写法：切换分代模式**
`collectgarbage("generational")`
```lua
-- 启用分代 GC，适合短生命周期对象多的程序
collectgarbage("generational")
```

---

**基本写法：切回增量模式**
`collectgarbage("incremental")`
```lua
-- 切换为传统增量 GC
collectgarbage("incremental")
```

---

**基本写法：强制 minor GC**
`collectgarbage("collect", 0, 0)`
```lua
-- 仅做次代回收，速度快
collectgarbage("collect", 0, 0)
```

---

**基本写法：设置分代参数**
`collectgarbage("setpause", <值>)`
```lua
-- 控制分代 GC 节奏
collectgarbage("setpause", 100)   -- 暂停率
collectgarbage("setstepmul", 200) -- 步进倍率
```

---

**基本写法：查看内存占用**
`collectgarbage("count")`
```lua
-- 返回当前内存（单位 KB）
local kb = collectgarbage("count")
```

---

**基本写法：查看 GC 是否运行**
`collectgarbage("isrunning")`
```lua
-- 返回布尔值表示 GC 是否在运行
local running = collectgarbage("isrunning")
```

---

## warn 警告函数

**基本写法：输出警告**
`warn("<消息>")`
```lua
-- 输出到 stderr 的警告
warn("配置项缺失，使用默认值")
```

---

**基本写法：多参数警告**
`warn("<前缀>", <参数>...)`
```lua
-- 第一参数为消息前缀
warn("@myapp", "用户不存在:", userId)
```

---

**基本写法：关闭警告**
`warn("@off")`
```lua
-- 临时关闭警告输出
warn("@off")
warn("这不会显示")
warn("@on")  -- 重新开启
```

---

**基本写法：自定义警告处理器**
`warn("@on", <函数>)`
```lua
-- 自定义警告处理（5.4 特性）
local handler = function(msg) print("[WARN]", msg) end
-- 通过 C API lua_setwarnf 注册自定义处理
```

---

## coroutine.close

**基本写法：关闭协程**
`coroutine.close(<协程>)`
```lua
-- 5.4 新增，关闭挂起的协程
local co = coroutine.create(function() coroutine.yield() end)
coroutine.resume(co)
coroutine.close(co)  -- 标记为死亡并清理
```

---

**基本写法：close 协程返回状态**
`local <ok>, <err> = coroutine.close(<协程>)`
```lua
-- 返回是否成功关闭
local ok, err = coroutine.close(co)
```

---

## 整数 for 循环新语义

**基本写法：整数 for 循环**
`for <i> = <起>, <止> [, <步>] do end`
```lua
-- 5.4 修正溢出与方向判定
for i = 1, 10 do print(i) end
for i = 10, 1, -1 do print(i) end
```

---

**基本写法：避免浮点误差**
`-- 5.4 整数循环更精确`
```lua
-- 旧版浮点循环可能有误差，5.4 整数版本更可靠
for i = 1, 100 do
    -- i 始终为整数
end
```

---

## 数学库改进

**基本写法：新随机数实现**
`math.random([<最小> [, <最大>]])`
```lua
-- 5.4 使用更高质量的随机数算法
local n = math.random(1, 100)
```

---

**基本写法：随机数生成器对象**
`math.randomseed(<种子>)`
```lua
-- 5.4 使用更稳健的播种
math.randomseed(os.time())
```

---

## 字符串与格式

**基本写法：format 新增 %p**
`string.format("%p", <userdata>)`
```lua
-- 输出指针地址
local s = string.format("%p", some_userdata)
```

---

**基本写法：gmatch 可选 init**
`string.gmatch(<串>, "<模式>" [, <起始>])`
```lua
-- 5.4 支持从指定位置开始匹配
for m in string.gmatch(s, "%w+", 5) do
    print(m)
end
```

---

**基本写法：数字到字符串强制转换移除**
`tonumber(<字符串>)`
```lua
-- 5.4 字符串到数字的隐式转换更严格
-- 字符串运算不再自动转数字
local n = tonumber("123")  -- 显式转换
-- "10" + 5  在 5.4 中需显式转
```

---

## userdata 多用户值

**基本写法：多用户值 userdata**
`-- 通过 C API lua_setiuservalue`
```lua
-- 5.4 userdata 可关联多个用户值
-- 旧版仅支持一个 uservalue
```

---

## utf8 库增强

**基本写法：支持更大码点**
`utf8.char(<码点>)`
```lua
-- 5.4 支持到 2^31 的码点
local s = utf8.char(0x1F600)  -- 笑脸 emoji
```

---

**基本写法：遍历 UTF-8 字符**
`for <码点>, <位置> in utf8.codes(<串>) do end`
```lua
-- 按码点遍历字符串
for p, pos in utf8.codes("中文") do
    print(p, pos)
end
```

---

## resetthread

**基本写法：重置线程**
`lua_resetthread(<线程>)`
```lua
-- C API 重置协程以便复用
-- 对应 Lua 层 coroutine 的底层支持
```

---

## 调试信息增强

**基本写法：函数参数调试信息**
`debug.getinfo(<函数>, "u")`
```lua
-- 5.4 增加参数与返回值调试信息
local info = debug.getinfo(f, "u")
print(info.nparams)  -- 参数个数
print(info.isvararg) -- 是否可变参数
```

---

## 兼容性迁移

**基本写法：检查 Lua 版本**
`_VERSION`
```lua
-- 返回当前 Lua 版本字符串
print(_VERSION)  -- Lua 5.4
```

---

**基本写法：版本兼容判断**
`tonumber((_VERSION:gsub("Lua ", "")))`
```lua
-- 提取版本号用于特性判断
local ver = tonumber((_VERSION:gsub("Lua ", "")))
if ver >= 5.4 then
    -- 使用 const/close 等新特性
end
```



<!-- ============ 文档分隔线：017-lua/014-LuaCAPI.md ============ -->

# Lua C API 基础

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 栈操作基础

**基本写法：压入数字**
`lua_pushnumber(<L>, <数值>);`
```c
// 压入一个数字到栈顶
lua_pushnumber(L, 3.14);
```

---

**基本写法：压入整数**
`lua_pushinteger(<L>, <整数>);`
```c
// 压入整数类型
lua_pushinteger(L, 42);
```

---

**基本写法：压入字符串**
`lua_pushstring(<L>, "<字符串>");`
```c
// 压入 C 字符串（以\0结尾）
lua_pushstring(L, "hello");
```

---

**基本写法：压入字面字符串**
`lua_pushliteral(<L>, "<字符串>");`
```c
// 字面量优化版本
lua_pushliteral(L, "literal text");
```

---

**基本写法：压入 nil**
`lua_pushnil(<L>);`
```c
// 压入 nil 值
lua_pushnil(L);
```

---

**基本写法：压入布尔**
`lua_pushboolean(<L>, <0或1>);`
```c
// 0 表示 false，非 0 表示 true
lua_pushboolean(L, 1);
```

---

**基本写法：获取栈顶索引**
`int <top> = lua_gettop(<L>);`
```c
// 返回栈中元素个数
int n = lua_gettop(L);
```

---

**基本写法：设置栈大小**
`lua_settop(<L>, <索引>);`
```c
// 设置栈顶位置，负数表示距顶偏移
lua_settop(L, 0);  // 清空栈
```

---

**基本写法：弹出元素**
`lua_pop(<L>, <数量>);`
```c
// 弹出指定数量的元素
lua_pop(L, 2);
```

---

## 栈读取

**基本写法：转数字**
`lua_Number <n> = lua_tonumber(<L>, <索引>);`
```c
// 把栈中元素转为浮点数
lua_Number x = lua_tonumber(L, 1);
```

---

**基本写法：转整数**
`lua_Integer <n> = lua_tointeger(<L>, <索引>);`
```c
// 转为整数，非整数返回 0
lua_Integer n = lua_tointeger(L, -1);
```

---

**基本写法：转字符串**
`size_t <len>; const char* <s> = lua_tolstring(<L>, <索引>, &<len>);`
```c
// 转字符串并返回长度
size_t len;
const char* s = lua_tolstring(L, 1, &len);
```

---

**基本写法：检查并转字符串**
`const char* <s> = luaL_checkstring(<L>, <参数序号>);`
```c
// 类型不符抛出错误
const char* name = luaL_checkstring(L, 1);
```

---

**基本写法：检查并转整数**
`lua_Integer <n> = luaL_checkinteger(<L>, <参数序号>);`
```c
// 必须为整数否则报错
lua_Integer n = luaL_checkinteger(L, 2);
```

---

**基本写法：判断类型**
`int <type> = lua_type(<L>, <索引>);`
```c
// 返回 LUA_TNUMBER、LUA_TSTRING 等
int t = lua_type(L, 1);
if (t == LUA_TSTRING) { }
```

---

**基本写法：判断特定类型**
`lua_isnumber(<L>, <索引>);`
```c
// 判断是否可转为数字
if (lua_isnumber(L, 1)) { }
```

---

## 表操作

**基本写法：创建空表**
`lua_newtable(<L>);`
```c
// 在栈顶创建空表
lua_newtable(L);
```

---

**基本写法：设置表字段（字符串键）**
`lua_setfield(<L>, <表索引>, "<键>");`
```c
// 弹出栈顶值并设置到表
lua_pushstring(L, "Alice");
lua_setfield(L, -2, "name");  // 表在 -2
```

---

**基本写法：获取表字段**
`lua_getfield(<L>, <表索引>, "<键>");`
```c
// 把表字段值压入栈顶
lua_getfield(L, -1, "name");
```

---

**基本写法：原始设置**
`lua_rawset(<L>, <表索引>);`
```c
// 不触发 __newindex 元方法
lua_pushstring(L, "key");
lua_pushinteger(L, 100);
lua_rawset(L, -3);
```

---

**基本写法：原始获取**
`lua_rawget(<L>, <表索引>);`
```c
// 不触发 __index 元方法
lua_pushstring(L, "key");
lua_rawget(L, -2);
```

---

**基本写法：数组式设置**
`lua_rawseti(<L>, <表索引>, <整数键>);`
```c
// 设置 t[i] = 栈顶值
lua_pushinteger(L, 10);
lua_rawseti(L, -2, 1);  // t[1] = 10
```

---

**基本写法：数组式获取**
`lua_rawgeti(<L>, <表索引>, <整数键>);`
```c
// 把 t[i] 压入栈顶
lua_rawgeti(L, -1, 1);
```

---

## 函数调用

**基本写法：注册 C 函数**
`lua_register(<L>, "<函数名>", <C函数>);`
```c
// 把 C 函数注册为全局函数
lua_register(L, "add", l_add);
```

---

**基本写法：C 函数签名**
`static int <函数名>(lua_State* <L>) { }`
```c
// C 函数必须返回返回值个数
static int l_add(lua_State* L) {
    int a = luaL_checkinteger(L, 1);
    int b = luaL_checkinteger(L, 2);
    lua_pushinteger(L, a + b);
    return 1;  // 一个返回值
}
```

---

**基本写法：调用 Lua 函数**
`lua_call(<L>, <参数个数>, <返回个数>);`
```c
// 调用栈顶函数，无错误处理
lua_getglobal(L, "print");
lua_pushstring(L, "hi");
lua_call(L, 1, 0);  // 1 参数 0 返回
```

---

**基本写法：保护调用**
`int <ok> = lua_pcall(<L>, <参数>, <返回>, <错误处理>);`
```c
// 调用失败返回 LUA_ERRRUN，不抛出
lua_getglobal(L, "func");
if (lua_pcall(L, 0, 0, 0) != LUA_OK) {
    const char* err = lua_tostring(L, -1);
}
```

---

## 错误处理

**基本写法：抛出错误**
`luaL_error(<L>, "<格式>", <参数>);`
```c
// 抛出错误并返回栈
luaL_error(L, "参数错误: %d", arg);
```

---

**基本写法：参数检查**
`luaL_argcheck(<L>, <条件>, <参数序号>, "<消息>");`
```c
// 条件不满足抛出错误
luaL_argcheck(L, n > 0, 1, "必须为正数");
```

---

**基本写法：参数类型检查**
`luaL_checktype(<L>, <参数序号>, <类型>);`
```c
// 检查参数类型
luaL_checktype(L, 1, LUA_TTABLE);
```

---

**基本写法：设置 panic 函数**
`lua_atpanic(<L>, <函数>);`
```c
// 设置未捕获错误时的处理
lua_atpanic(L, my_panic);
```

---

## 模块注册

**基本写法：注册函数列表**
`luaL_Reg <数组>[] = { { "<名>", <函数> }, { NULL, NULL } };`
```c
// 定义模块函数表
static const luaL_Reg mylib[] = {
    { "add", l_add },
    { "sub", l_sub },
    { NULL, NULL }  // 哨兵结尾
};
```

---

**基本写法：创建库**
`luaL_newlib(<L>, <函数表>);`
```c
// 创建包含函数的新表
luaL_newlib(L, mylib);
return 1;
```

---

**基本写法：模块入口**
`int luaopen_<模块名>(lua_State* <L>) { }`
```c
// require 时调用的入口函数
int luaopen_mylib(lua_State* L) {
    luaL_newlib(L, mylib);
    return 1;
}
```

---

## 元表操作

**基本写法：创建元表**
`luaL_newmetatable(<L>, "<名称>");`
```c
// 创建并注册命名元表
luaL_newmetatable(L, "MyType");
```

---

**基本写法：获取元表**
`lua_getmetatable(<L>, <索引>);`
```c
// 获取栈中值的元表
if (lua_getmetatable(L, 1)) { }
```

---

**基本写法：设置元表**
`lua_setmetatable(<L>, <索引>);`
```c
// 把栈顶元表设给指定值
lua_setmetatable(L, -2);
```

---

## userdata 用户数据

**基本写法：创建 userdata**
`void* <p> = lua_newuserdata(<L>, <大小>);`
```c
// 分配用户数据并压栈
Point* p = lua_newuserdata(L, sizeof(Point));
```

---

**基本写法：检查 userdata**
`void* <p> = luaL_checkudata(<L>, <参数序号>, "<元表名>");`
```c
// 检查并返回 userdata 指针
Point* p = luaL_checkudata(L, 1, "MyPoint");
```

---

## 状态与线程

**基本写法：创建新状态**
`lua_State* <L> = luaL_newstate();`
```c
// 创建独立的 Lua 状态
lua_State* L = luaL_newstate();
```

---

**基本写法：关闭状态**
`lua_close(<L>);`
```c
// 释放所有资源
lua_close(L);
```

---

**基本写法：加载标准库**
`luaL_openlibs(<L>);`
```c
// 加载所有标准库
luaL_openlibs(L);
```

---

**基本写法：加载并执行文件**
`luaL_dofile(<L>, "<路径>");`
```c
// 加载并运行 Lua 文件
if (luaL_dofile(L, "script.lua") != LUA_OK) {
    fprintf(stderr, "%s\n", lua_tostring(L, -1));
}
```

---

**基本写法：加载字符串**
`luaL_dostring(<L>, "<代码>");`
```c
// 加载并执行 Lua 代码字符串
luaL_dostring(L, "print('hello')");
```

---

## 全局变量

**基本写法：获取全局变量**
`lua_getglobal(<L>, "<名称>");`
```c
// 把全局变量压栈
lua_getglobal(L, "print");
```

---

**基本写法：设置全局变量**
`lua_setglobal(<L>, "<名称>");`
```c
// 弹出栈顶并设为全局变量
lua_pushinteger(L, 100);
lua_setglobal(L, "count");
```

---

## 栈保护与恢复

**基本写法：记录栈底**
`int <base> = lua_gettop(<L>);`
```c
// 记录调用前栈位置
int base = lua_gettop(L);
```

---

**基本写法：恢复栈**
`lua_settop(<L>, <base>);`
```c
// 还原到记录的位置
lua_settop(L, base);
```

---

**基本写法：复制栈元素**
`lua_pushvalue(<L>, <索引>);`
```c
// 把指定位置值复制到栈顶
lua_pushvalue(L, 1);  // 复制第一个参数
```

---

**基本写法：移除栈元素**
`lua_remove(<L>, <索引>);`
```c
// 移除指定位置元素并下移
lua_remove(L, 1);
```

---

**基本写法：插入到位置**
`lua_insert(<L>, <索引>);`
```c
// 把栈顶移到指定位置
lua_insert(L, 1);
```



<!-- ============ 文档分隔线：017-lua/015-Love2D.md ============ -->

# Lua Love2D 常用命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 命令行

**基本写法：运行游戏**
`love <目录>`
```bash
// 运行指定目录的 Love2D 游戏
love /path/to/game
```

---

**基本写法：打包 love 文件**
`zip -r game.love .`
```bash
// 把游戏目录打包为 .love 文件
zip -r game.love *.lua assets
```

---

**基本写法：生成可执行文件**
`cat love.exe game.love > game.exe`
```bash
// Windows 下合并为单可执行文件
cat love.exe game.love > game.exe
```

---

**基本写法：查看版本**
`love --version`
```bash
// 输出 Love2D 版本号
love --version
```

---

**基本写法：启用控制台**
`love <目录> --console`
```bash
// Windows 启动时附加控制台窗口
love game --console
```

---

## 项目结构

**基本写法：main.lua 入口**
`function love.load() end`
```lua
-- 游戏启动时调用一次
function love.load()
    love.graphics.setBackgroundColor(0.2, 0.2, 0.2)
end
```

---

**基本写法：主回调**
`function love.<回调>() end`
```lua
-- Love2D 内置主回调
-- love.load()      加载时
-- love.update(dt)  每帧更新
-- love.draw()      每帧绘制
-- love.keypressed(key) 按键
-- love.mousemoved(x,y) 鼠标移动
```

---

## 窗口配置

**基本写法：设置窗口**
`love.window.setMode(<宽>, <高>, <设置>)`
```lua
-- 设置窗口大小与属性
love.window.setMode(800, 600, {
    fullscreen = false,
    resizable = true,
    vsync = true
})
```

---

**基本写法：设置标题**
`love.window.setTitle("<标题>")`
```lua
-- 设置窗口标题
love.window.setTitle("My Game")
```

---

**基本写法：获取尺寸**
`local <w>, <h> = love.graphics.getDimensions()`
```lua
-- 获取窗口客户区尺寸
local w, h = love.graphics.getDimensions()
```

---

## 图形绘制

**基本写法：设置颜色**
`love.graphics.setColor(<r>, <g>, <b> [, <a>])`
```lua
-- 设置后续绘制颜色（0-1）
love.graphics.setColor(1, 0, 0)  -- 红色
```

---

**基本写法：绘制矩形**
`love.graphics.rectangle("<模式>", <x>, <y>, <宽>, <高>)`
```lua
-- mode 为 fill 或 line
love.graphics.rectangle("fill", 100, 100, 80, 60)
```

---

**基本写法：绘制圆形**
`love.graphics.circle("<模式>", <x>, <y>, <半径>)`
```lua
-- 绘制填充圆
love.graphics.circle("fill", 200, 200, 30)
```

---

**基本写法：绘制线段**
`love.graphics.line(<x1>, <y1>, <x2>, <y2>)`
```lua
-- 连接多点的线段
love.graphics.line(0, 0, 100, 100)
```

---

**基本写法：绘制文本**
`love.graphics.print("<文本>", <x> [, <y>])`
```lua
-- 在指定位置绘制文本
love.graphics.print("Score: 0", 10, 10)
```

---

**基本写法：设置字体**
`love.graphics.setFont(<字体>)`
```lua
-- 设置当前字体
local font = love.graphics.newFont(20)
love.graphics.setFont(font)
```

---

**基本写法：清屏**
`love.graphics.clear(<r>, <g>, <b>)`
```lua
-- 用指定颜色清空画布
love.graphics.clear(0, 0, 0)
```

---

## 图像与资源

**基本写法：加载图像**
`local <img> = love.graphics.newImage("<路径>")`
```lua
-- 加载图片资源
local img = love.graphics.newImage("assets/player.png")
```

---

**基本写法：绘制图像**
`love.graphics.draw(<图像>, <x>, <y> [, <旋转>])`
```lua
-- 在指定位置绘制图像
love.graphics.draw(img, 100, 100)
```

---

**基本写法：加载字体**
`local <font> = love.graphics.newFont("<路径>", <大小>)`
```lua
-- 加载 TTF 字体文件
local font = love.graphics.newFont("font.ttf", 24)
```

---

**基本写法：加载音频**
`local <snd> = love.audio.newSource("<路径>", <类型>)`
```lua
-- 加载音效或音乐
local bgm = love.audio.newSource("bgm.ogg", "stream")
local sfx = love.audio.newSource("hit.wav", "static")
```

---

## 输入处理

**基本写法：按键回调**
`function love.keypressed(<键>) end`
```lua
-- 按键按下时触发
function love.keypressed(key)
    if key == "escape" then love.event.quit() end
end
```

---

**基本写法：按键状态查询**
`love.keyboard.isDown(<键>)`
```lua
-- 查询按键是否持续按下
if love.keyboard.isDown("right") then
    player.x = player.x + 200 * dt
end
```

---

**基本写法：鼠标按下**
`function love.mousepressed(<x>, <y>, <按钮>) end`
```lua
-- 鼠标按键按下回调
function love.mousepressed(x, y, button)
    if button == 1 then print("左键点击", x, y) end
end
```

---

**基本写法：查询鼠标位置**
`local <x>, <y> = love.mouse.getPosition()`
```lua
-- 获取当前鼠标坐标
local x, y = love.mouse.getPosition()
```

---

## 更新循环

**基本写法：update 回调**
`function love.update(<dt>) end`
```lua
-- 每帧调用，dt 是距上一帧秒数
function love.update(dt)
    player.x = player.x + speed * dt
end
```

---

**基本写法：基于时间的移动**
`<位置> = <位置> + <速度> * <dt>`
```lua
-- 用 dt 保证不同帧率下速度一致
player.x = player.x + 200 * dt
```

---

**基本写法：定时器**
`local <计时> = 0`
```lua
-- 用 dt 累积实现计时
local timer = 0
function love.update(dt)
    timer = timer + dt
    if timer >= 2 then
        timer = 0
        -- 每 2 秒触发一次
    end
end
```

---

## 绘制回调

**基本写法：draw 回调**
`function love.draw() end`
```lua
-- 每帧绘制内容
function love.draw()
    love.graphics.print("Hello Love2D", 100, 100)
end
```

---

**基本写法：批量绘制**
`love.graphics.rectangle(...)`
```lua
-- 在 draw 中批量调用绘制
function love.draw()
    for _, e in ipairs(enemies) do
        love.graphics.circle("fill", e.x, e.y, e.r)
    end
end
```

---

## 数学与随机

**基本写法：Love2D 随机数**
`love.math.random([<最小> [, <最大>]])`
```lua
-- 使用 Love2D 的随机数（独立于 math.random）
local n = love.math.random(1, 100)
```

---

**基本写法：设置随机种子**
`love.math.setRandomSeed(<种子>)`
```lua
-- 设置随机种子保证可复现
love.math.setRandomSeed(os.time())
```

---

**基本写法：角度与弧度**
`math.rad(<角度>) | math.deg(<弧度>)`
```lua
-- Love2D 三角函数用弧度
local rad = math.rad(90)
local sin = math.sin(rad)
```

---

## 音频播放

**基本写法：播放音效**
`<source>:play()`
```lua
-- 播放音效源
local sfx = love.audio.newSource("hit.wav", "static")
sfx:play()
```

---

**基本写法：循环播放背景音乐**
`<source>:setLooping(true)`
```lua
-- 设置循环播放
local bgm = love.audio.newSource("bgm.ogg", "stream")
bgm:setLooping(true)
bgm:play()
```

---

**基本写法：设置音量**
`<source>:setVolume(<0-1>)`
```lua
-- 设置音量
bgm:setVolume(0.5)
```

---

**基本写法：停止播放**
`<source>:stop()`
```lua
-- 停止播放并回到开头
bgm:stop()
```

---

## 画布与变换

**基本写法：创建画布**
`local <canvas> = love.graphics.newCanvas(<宽>, <高>)`
```lua
-- 离屏渲染画布
local canvas = love.graphics.newCanvas(800, 600)
```

---

**基本写法：渲染到画布**
`love.graphics.setCanvas(<canvas>)`
```lua
-- 切换渲染目标到画布
love.graphics.setCanvas(canvas)
love.graphics.circle("fill", 100, 100, 50)
love.graphics.setCanvas()  -- 恢复主屏
```

---

**基本写法：坐标变换**
`love.graphics.push() | love.graphics.pop()`
```lua
-- 保存与恢复变换状态
love.graphics.push()
love.graphics.translate(100, 100)
love.graphics.rotate(math.rad(45))
love.graphics.draw(img, 0, 0)
love.graphics.pop()
```

---

## 文件系统

**基本写法：读取文件**
`local <内容> = love.filesystem.read("<路径>")`
```lua
-- 在保存目录与源中读取
local content = love.filesystem.read("config.txt")
```

---

**基本写法：写入文件**
`love.filesystem.write("<路径>", <内容>)`
```lua
-- 写入到保存目录
love.filesystem.write("save.txt", "progress=5")
```

---

**基本写法：追加写入**
`love.filesystem.append("<路径>", <内容>)`
```lua
-- 追加内容到文件
love.filesystem.append("log.txt", "new line\n")
```

---

**基本写法：列举目录**
`local <文件表> = love.filesystem.getDirectoryItems("<目录>")`
```lua
-- 列出目录下所有文件
local files = love.filesystem.getDirectoryItems("levels")
for _, f in ipairs(files) do
    print(f)
end
```

---

## 状态管理

**基本写法：游戏状态切换**
`love.event.quit("restart")`
```lua
-- 重启游戏
love.event.quit("restart")
```

---

**基本写法：退出游戏**
`love.event.quit()`
```lua
-- 退出应用
love.event.quit()
```

---

**基本写法：获取帧率**
`love.timer.getFPS()`
```lua
-- 获取当前帧率
local fps = love.timer.getFPS()
love.graphics.print("FPS: " .. fps, 10, 10)
```

---

## 配置 conf.lua

**基本写法：配置窗口与模块**
`function love.conf(<t>) end`
```lua
-- 项目根目录 conf.lua 设置
function love.conf(t)
    t.window.width = 1024
    t.window.height = 768
    t.window.title = "My Game"
    t.modules.joystick = false  -- 禁用未用模块
end
```

---

**基本写法：设置版本兼容**
`t.version = "<版本>"`
```lua
-- 声明目标 Love2D 版本
function love.conf(t)
    t.version = "11.5"
end
```



<!-- ============ 文档分隔线：017-lua/016-LuaRocks.md ============ -->

# Lua LuaRocks 包管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础命令

**基本写法：查看版本**
`luarocks --version`
```bash
// 查看 LuaRocks 版本
luarocks --version
```

---

**基本写法：查看配置**
`luarocks config`
```bash
// 查看当前 LuaRocks 配置
luarocks config
```

---

**基本写法：查看帮助**
`luarocks help <命令>`
```bash
// 查看具体命令的帮助
luarocks help install
```

---

## 搜索与查询

**基本写法：搜索包**
`luarocks search <关键词>`
```bash
// 按名称搜索 LuaRocks 仓库
luarocks search lua-cjson
```

---

**基本写法：搜索结果过滤**
`luarocks search <关键词> --all`
```bash
// 包含所有版本与平台的结果
luarocks search lpeg --all
```

---

**基本写法：查看包详情**
`luarocks show <包名>`
```bash
// 查看已安装包的元信息
luarocks show lua-cjson
```

---

**基本写法：列出本地包**
`luarocks list [<包名>]`
```bash
// 列出已安装的所有 rock
luarocks list
```

---

## 安装与卸载

**基本写法：安装包**
`luarocks install <包名> [<版本>]`
```bash
// 安装最新版本的 rock
luarocks install lua-cjson
// 安装指定版本
luarocks install lua-cjson 2.1.0
```

---

**基本写法：从本地 rockspec 安装**
`luarocks install <rockspec文件>`
```bash
// 根据本地 rockspec 构建
luarocks install mylib-1.0-1.rockspec
```

---

**基本写法：安装到指定 Lua 版本**
`luarocks install <包> --lua-version=<版本>`
```bash
// 多版本 Lua 共存时指定目标
luarocks install lpeg --lua-version=5.3
```

---

**基本写法：安装到本地项目**
`luarocks install <包> --local`
```bash
// 安装到用户目录而非系统目录
luarocks install lua-cjson --local
```

---

**基本写法：仅下载不安装**
`luarocks download <包名> [<版本>]`
```bash
// 仅下载 rock 文件或 rockspec
luarocks download lua-cjson
```

---

**基本写法：卸载包**
`luarocks remove <包名> [<版本>]`
```bash
// 卸载已安装的 rock
luarocks remove lua-cjson
```

---

**基本写法：强制卸载**
`luarocks remove <包名> --force`
```bash
// 忽略依赖强制移除
luarocks remove lua-cjson --force
```

---

## 构建与打包

**基本写法：初始化 rockspec**
`luarocks init [<项目名>]`
```bash
// 在当前目录初始化 LuaRocks 项目
luarocks init mylib
```

---

**基本写法：编写 rockspec**
`-- rockspec 文件示例`
```lua
-- mylib-1.0-1.rockspec
package = "mylib"
version = "1.0-1"
source = { url = "git://github.com/user/mylib.git" }
description = {
    summary = "My Lua library",
    license = "MIT"
}
dependencies = {
    "lua >= 5.1"
}
build = {
    type = "builtin",
    modules = { mylib = "src/mylib.lua" }
}
```

---

**基本写法：构建 rock**
`luarocks build <rockspec>`
```bash
// 根据 rockspec 构建并安装
luarocks build mylib-1.0-1.rockspec
```

---

**基本写法：仅构建不安装**
`luarocks build <rockspec> --pack-binary-rock`
```bash
// 生成 .rock 文件便于分发
luarocks build mylib-1.0-1.rockspec --pack-binary-rock
```

---

**基本写法：make 本地构建**
`luarocks make [<rockspec>]`
```bash
// 在源码目录直接构建安装
luarocks make
```

---

## 依赖管理

**基本写法：查看依赖**
`luarocks deps <包名>`
```bash
// 查看包的所有依赖
luarocks deps lua-cjson
```

---

**基本写法：安装依赖**
`luarocks deps --install <rockspec>`
```bash
// 仅安装依赖不构建本身
luarocks deps --install mylib-1.0-1.rockspec
```

---

**基本写法：声明依赖**
`dependencies = { "<包> <约束>", ... }`
```lua
-- rockspec 中声明依赖
dependencies = {
    "lua >= 5.3, < 5.5",
    "lpeg >= 1.0",
    "lua-cjson"
}
```

---

## 服务器与仓库

**基本写法：指定服务器安装**
`luarocks install <包> --server=<服务器>`
```bash
// 从自定义 manifest 服务器安装
luarocks install mylib --server=http://rocks.moonscript.org
```

---

**基本写法：仅从本地安装**
`luarocks install <包> --only-server=<目录>`
```bash
// 只从本地目录搜索不联网
luarocks install mylib --only-server=./rocks
```

---

**基本写法：上传包**
`luarocks upload <rockspec> [--api-key=<密钥>]`
```bash
// 发布到 LuaRocks 官方仓库
luarocks upload mylib-1.0-1.rockspec --api-key=YOUR_KEY
```

---

**基本写法：添加自定义仓库**
`luarocks add <仓库URL>`
```bash
// 注册新的 rocks 服务器
luarocks config repositories.myrepo "http://example.com/rocks"
```

---

## 配置管理

**基本写法：查看配置项**
`luarocks config <键>`
```bash
// 查看具体配置值
luarocks config lua_version
luarocks config lua_dir
```

---

**基本写法：设置配置项**
`luarocks config <键> <值>`
```bash
// 修改配置
luarocks config lua_version 5.4
```

---

**基本写法：配置文件位置**
`~/.luarocks/config.lua`
```lua
-- 用户级配置文件
-- 可设置 servers、variables 等
variables = {
    LUA_INCDIR = "/usr/include/lua5.4",
    LUA_LIBDIR = "/usr/lib"
}
```

---

## 多版本共存

**基本写法：列出可用 Lua 版本**
`luarocks config lua_versions`
```bash
// 查看本机已配置的 Lua 版本
luarocks config lua_versions
```

---

**基本写法：切换 Lua 版本**
`luarocks config lua_version <版本>`
```bash
// 切换 LuaRocks 默认 Lua 版本
luarocks config lua_version 5.4
```

---

**基本写法：针对版本安装**
`luarocks --lua-version=<版本> install <包>`
```bash
// 临时为某 Lua 版本安装
luarocks --lua-version=5.1 install lpeg
```

---

## 本地项目树

**基本写法：创建项目本地树**
`luarocks init`
```bash
// 在项目目录创建 lua_modules 与 .luarocks
luarocks init
```

---

**基本写法：使用项目本地树**
`luarocks install <包> --tree=<目录>`
```bash
// 安装到指定目录树
luarocks install lua-cjson --tree=./lua_modules
```

---

**基本写法：设置包路径**
`package.path = "<目录>/?<包名>"`
```lua
-- 加载项目本地安装的模块
package.path = "./lua_modules/share/lua/5.4/?.lua;" .. package.path
package.cpath = "./lua_modules/lib/lua/5.4/?.so;" .. package.cpath
```

---

## 常见维护命令

**基本写法：检查可升级**
`luarocks list --outdated`
```bash
// 列出有新版本的已装包
luarocks list --outdated
```

---

**基本写法：升级包**
`luarocks install <包> --force`
```bash
// 强制重装为最新版本
luarocks install lua-cjson --force
```

---

**基本写法：文档查看**
`luarocks doc <包名>`
```bash
// 打开包的本地文档
luarocks doc lua-cjson
```

---

**基本写法：测试包**
`luarocks test [<rockspec>]`
```bash
// 运行 rockspec 中声明的测试
luarocks test mylib-1.0-1.rockspec
```

---

**基本写法：测试类型声明**
`test = { type = "<框架>" }`
```lua
-- rockspec 中声明测试
test = {
    type = "busted",
    script = "test/test_busted.lua"
}
```



<!-- ============ 文档分隔线：017-lua/017-LuaOverviewEnvSetup.md ============ -->

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



<!-- ============ 文档分隔线：017-lua/018-LuaDebug.md ============ -->

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



<!-- ============ 文档分隔线：017-lua/019-WeakTable.md ============ -->

# Lua 弱表与 GC

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 弱表基础

**基本写法：设置弱键表**
`setmetatable(<表>, { __mode = "k" })`
```lua
-- 键为弱引用，值被回收时键值对删除
local t = setmetatable({}, { __mode = "k" })
```

---

**基本写法：设置弱值表**
`setmetatable(<表>, { __mode = "v" })`
```lua
-- 值为弱引用，无其他引用时回收值
local t = setmetatable({}, { __mode = "v" })
```

---

**基本写法：键值都弱**
`setmetatable(<表>, { __mode = "kv" })`
```lua
-- 键和值都为弱引用
local cache = setmetatable({}, { __mode = "kv" })
```

---

**基本写法：__mode 字符速查**
`"k" | "v" | "kv"`
```lua
-- "k"  仅键弱引用
-- "v"  仅值弱引用
-- "kv" 键值均弱引用
-- 字符串与数字不受弱引用影响
```

---

## 弱表使用场景

**基本写法：对象属性缓存**
`<缓存表>[<对象>] = <属性>`
```lua
-- 用对象作键缓存属性，对象回收后自动清理
local props = setmetatable({}, { __mode = "k" })
props[obj] = { x = 1, y = 2 }
-- obj 无其他引用时该条目被回收
```

---

**基本写法：值缓存**
`<缓存表>[<键>] = <临时对象>`
```lua
-- 缓存大对象，无人引用时释放
local cache = setmetatable({}, { __mode = "v" })
cache["big"] = createBigObject()
```

---

**基本写法：临时关联表**
`setmetatable({}, { __mode = "k" })`
```lua
-- 不阻止键对象被回收的映射
local memo = setmetatable({}, { __mode = "k" })
local function memoize(obj)
    if memo[obj] then return memo[obj] end
    local r = compute(obj)
    memo[obj] = r
    return r
end
```

---

## GC 控制

**基本写法：手动触发 GC**
`collectgarbage("collect")`
```lua
-- 强制完整垃圾回收
collectgarbage("collect")
```

---

**基本写法：分步 GC**
`collectgarbage("step" [, <步长>])`
```lua
-- 执行一次增量 GC 步骤
collectgarbage("step", 100)
```

---

**基本写法：停止 GC**
`collectgarbage("stop")`
```lua
-- 暂停自动垃圾回收
collectgarbage("stop")
```

---

**基本写法：重启 GC**
`collectgarbage("restart")`
```lua
-- 恢复自动垃圾回收
collectgarbage("restart")
```

---

**基本写法：查看内存**
`collectgarbage("count")`
```lua
-- 返回当前内存使用（KB）
local kb = collectgarbage("count")
print(kb, "KB")
```

---

**基本写法：查看运行状态**
`collectgarbage("isrunning")`
```lua
-- 返回 GC 是否在运行
local running = collectgarbage("isrunning")
```

---

## 增量 GC 调参

**基本写法：设置暂停率**
`collectgarbage("setpause", <值>)`
```lua
-- 值为百分比，100 表示等待内存翻倍再回收
collectgarbage("setpause", 200)
```

---

**基本写法：设置步进倍率**
`collectgarbage("setstepmul", <值>)`
```lua
-- 步进速度相对内存分配的倍率
collectgarbage("setstepmul", 500)
```

---

## 分代 GC（5.4+）

**基本写法：启用分代模式**
`collectgarbage("generational")`
```lua
-- 切换到分代垃圾回收
collectgarbage("generational")
```

---

**基本写法：切回增量模式**
`collectgarbage("incremental")`
```lua
-- 切换回传统增量 GC
collectgarbage("incremental")
```

---

**基本写法：分代 minor 回收**
`collectgarbage("collect", 0, 0)`
```lua
-- 仅做次代回收，快速清理短生命周期对象
collectgarbage("collect", 0, 0)
```

---

## 析构元方法

**基本写法：定义 __gc**
`setmetatable(<表>, { __gc = <函数> })`
```lua
-- 对象被回收时调用
local obj = setmetatable({}, {
    __gc = function(self)
        print("对象被回收")
    end
})
```

---

**基本写法：__gc 触发时机**
`-- GC 决定，非确定性`
```lua
-- __gc 在对象被真正回收时触发
-- 时机不可预测，不要依赖其立即执行
obj = nil
collectgarbage("collect")  -- 此时可能触发
```

---

**基本写法：__close 确定性释放（5.4+）**
`local <变量> <close> = <带__close对象>`
```lua
-- 作用域结束立即调用，确定性释放
do
    local res <close> = setmetatable({}, {
        __close = function() print("立即释放") end
    })
end -- 离开块立即触发 __close
```

---

**基本写法：__gc 与 __close 区别**
`-- __gc 不确定 | __close 确定`
```lua
-- __gc：垃圾回收时触发，时机不确定
-- __close：变量作用域结束触发，确定且即时
-- 推荐用 __close 管理资源，__gc 仅作兜底
```

---

## 弱表与字符串

**基本写法：字符串不受弱引用影响**
`-- 字符串不会被弱表回收`
```lua
-- Lua 字符串是内部化的，不会被弱引用回收
local t = setmetatable({}, { __mode = "v" })
t["key"] = "some string"
-- 即使无其他引用，字符串也不会被回收
```

---

**基本写法：数字键也不回收**
`-- 数字与布尔同字符串`
```lua
-- 数字、布尔、字符串作为键值都不会触发弱表回收
-- 仅 table、function、userdata、thread 等引用类型可弱引用
```

---

## 验证弱表行为

**基本写法：验证键弱引用**
`<表>[<对象>] = 1; <对象> = nil; collectgarbage()`
```lua
-- 验证键被回收后条目消失
local t = setmetatable({}, { __mode = "k" })
local key = {}
t[key] = "data"
print(next(t))  -- 非空
key = nil
collectgarbage("collect")
print(next(t))  -- nil，条目已清理
```

---

**基本写法：验证值弱引用**
`<表>[1] = <对象>; <对象> = nil; collectgarbage()`
```lua
-- 验证值被回收后条目消失
local t = setmetatable({}, { __mode = "v" })
local obj = { name = "x" }
t[1] = obj
obj = nil
collectgarbage("collect")
print(t[1])  -- nil
```

---

## 缓存模式实战

**基本写法：受限大小缓存**
`<弱表> + <强引用队列>`
```lua
-- 弱表加快查，强队列保近期 N 个
local strong = {}
local weak = setmetatable({}, { __mode = "v" })
local MAX = 100
local function cache(key, val)
    weak[key] = val
    table.insert(strong, val)
    if #strong > MAX then table.remove(strong, 1) end
end
```

---

**基本写法：清除缓存**
`<表> = {} 或 for k in pairs(<表>) do <表>[k] = nil end`
```lua
-- 清空弱表缓存
for k in pairs(cache) do
    cache[k] = nil
end
-- 或直接重建
cache = setmetatable({}, { __mode = "kv" })
```

---

## 监控内存

**基本写法：内存基线对比**
`collectgarbage("count")`
```lua
-- 测量某操作前后的内存增量
collectgarbage("collect")
local before = collectgarbage("count")
do_something()
local after = collectgarbage("count")
print("增量:", after - before, "KB")
```

---

**基本写法：检测泄漏**
`<循环> + collectgarbage("count")`
```lua
-- 观察内存是否持续增长
for i = 1, 10000 do
    process()
end
collectgarbage("collect")
print("内存:", collectgarbage("count"), "KB")
```



<!-- ============ 文档分隔线：017-lua/020-EnvironmentModule.md ============ -->

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



<!-- ============ 文档分隔线：017-lua/021-EnvironmentGlobalVariable.md ============ -->

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



<!-- ============ 文档分隔线：017-lua/022-IoLibrary.md ============ -->

# Lua io 库语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：017-lua/023-LuaCliCommand.md ============ -->

# Lua / luac 命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## lua 解释器

**基本写法：交互式 REPL**
`lua`
```bash
# 进入交互式解释器
lua
# 输入 Lua 表达式或语句即时执行，Ctrl+D 退出
```

---

**基本写法：执行脚本文件**
`lua <脚本.lua> [参数...]`
```bash
# 执行 main.lua，后续参数传入 arg 表
lua main.lua
lua script.lua arg1 arg2
```

---

**基本写法：从标准输入执行**
`lua -` 或 `echo <代码> | lua`
```bash
# 从 stdin 读取脚本
echo 'print("hello")' | lua
lua -                # 等待 stdin 输入
```

---

**基本写法：执行字符串代码**
`lua -e "<代码>"`
```bash
# 直接执行一段 Lua 代码
lua -e 'print("Lua " .. _VERSION)'
lua -e 'for i=1,3 do print(i) end'
```

---

**基本写法：加载模块路径**
`lua -l <模块> [脚本]`
```bash
# 加载指定模块后再运行脚本
lua -l mylib -l utils main.lua
```

---

**基本写法：忽略环境变量 LUA_PATH / LUA_CPATH**
`lua -E [脚本]`
```bash
# 忽略 LUA_PATH / LUA_CPATH 等环境变量
lua -E main.lua
```

---

**基本写法：禁用 JIT（LuaJIT 专属）**
`luajit -j off <脚本>`
```bash
# LuaJIT 关闭 JIT 编译
luajit -j off script.lua
luajit -jv script.lua   # 显示 JIT 编译日志
```

---

## lua 命令行参数

**基本写法：解释器停止选项解析**
`lua -- <脚本>`
```bash
# -- 之后的内容不再作为选项
lua -- script.lua
```

---

**基本写法：传递给脚本的参数表**
`lua <脚本> <参数>`
```lua
-- 脚本中通过 arg 全局表访问
-- lua script.lua a b c
-- arg[0]  = "script.lua"  脚本名
-- arg[-1] = "lua"          解释器名
-- arg[1]  = "a"            第一个参数
-- arg[2]  = "b"
-- arg[3]  = "c"
-- arg[#arg] = 最后一个参数
print(arg[0], arg[1], arg[#arg])
```

---

## luac 编译器

**基本写法：编译为字节码**
`luac -o <输出> <源文件>`
```bash
# 编译 .lua 为字节码文件（默认 luac.out）
luac -o out.luac main.lua
luac main.lua util.lua        # 多文件合并为 luac.out
```

---

**基本写法：列出字节码**
`luac -l <源文件>`
```bash
# 打印函数 main 与字节码列表
luac -l main.lua
luac -l -l main.lua          # 重复 -l 显示更详细
```

---

**基本写法：仅做语法检查**
`luac -p <源文件>`
```bash
# 只解析不生成字节码，用于语法检查
luac -p main.lua
echo $?                      # 0 表示语法正确
```

---

**基本写法：显示版本信息**
`luac -v`
```bash
# 查看 luac 版本
luac -v
```

---

**基本写法：去除调试信息**
`luac -s -o <输出> <源>`
```bash
# 去除行号等调试信息减小体积
luac -s -o release.luac main.lua
```

---

**基本写法：指定输出格式版本**
`luac -W`（Lua 5.4 写入小端格式）
```bash
# Lua 5.4 字节码字节序
luac -W -o out.luac main.lua   # 小端字节序
```

---

## 加载与运行字节码

**基本写法：运行 luac 输出**
`lua <字节码文件>`
```bash
# 直接用 lua 运行字节码文件
lua out.luac
```

---

**基本写法：脚本内加载字节码**
`loadfile(<文件>)` / `load(<字符串>)`
```lua
-- 加载字节码或源码为函数
local chunk = loadfile("out.luac")
if chunk then chunk() end

-- 从字符串加载
local f = load("return 1 + 2")
print(f())   -- 3
```

---

**基本写法：dump 函数为字节码**
`string.dump(<函数> [, <strip>])`
```lua
-- 将 Lua 函数序列化为字节码字符串
local function add(a, b) return a + b end
local bytecode = string.dump(add)
local f = io.open("add.luac", "wb")
f:write(bytecode); f:close()
```

---

## 调试与诊断

**基本写法：错误追踪**
`lua -e "..."` 配合 `pcall`
```lua
-- pcall 捕获错误并打印栈
local ok, err = pcall(function()
    error("出错了")
end)
if not ok then print(err) end
```

---

**基本写法：LuaJIT 性能分析**
`luajit -jp <脚本>`
```bash
# LuaJIT 内置性能分析器
luajit -jp script.lua
luajit -jp=fl script.lua   # 按函数行统计
```

---

## 注意事项速查

**基本写法：字节码版本兼容性**
`luac -o <输出> <源>`
```bash
# 不同 Lua 版本字节码不兼容
# Lua 5.1 / 5.2 / 5.3 / 5.4 字节码互不通用
# 必须用目标版本对应的 luac 重新编译
luac5.4 -o main.luac main.lua
lua5.4 main.luac
```



<!-- ============ 文档分隔线：017-lua/024-MathLibrary.md ============ -->

# Lua math 库语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 常量

**基本写法：数学常量**
`math.<常量名>`
```lua
-- 内置数学常量
math.pi       -- 3.141592653589793
math.huge     -- 正无穷
math.maxinteger  -- 最大整型值（Lua 5.3+）
math.mininteger  -- 最小整型值（Lua 5.3+）
```

---

## 取整与绝对值

**基本写法：绝对值**
`math.abs(<x>)`
```lua
-- 返回绝对值
math.abs(-10)      -- 10
math.abs(-3.14)    -- 3.14
```

---

**基本写法：向上取整**
`math.ceil(<x>)`
```lua
-- 返回不小于 x 的最小整数
math.ceil(2.3)     -- 3
math.ceil(-1.5)    -- -1
```

---

**基本写法：向下取整**
`math.floor(<x>)`
```lua
-- 返回不大于 x 的最大整数
math.floor(2.7)    -- 2
math.floor(-1.5)   -- -2
```

---

**基本写法：向零取整**
`math.tointeger(<x>)` / `math.modf(<x>)`
```lua
-- modf 拆分整数与小数部分
local int, frac = math.modf(3.75)   -- int=3, frac=0.75

-- tointeger 当 x 为整数值时返回整数，否则返回 nil
math.tointeger(3.0)   -- 3
math.tointeger(3.5)   -- nil
```

---

## 最值

**基本写法：取最大值**
`math.max(<x>, <y>, ...)`
```lua
-- 多个值中的最大值
math.max(1, 5, 3)        -- 5
math.max(-1, -2, 0)      -- 0
```

---

**基本写法：取最小值**
`math.min(<x>, <y>, ...)`
```lua
-- 多个值中的最小值
math.min(1, 5, 3)        -- 1
math.min(10, 20, 0.5)    -- 0.5
```

---

## 幂与对数

**基本写法：平方根**
`math.sqrt(<x>)`
```lua
-- 返回算术平方根
math.sqrt(16)    -- 4.0
math.sqrt(2)     -- 1.4142135623731
```

---

**基本写法：幂运算**
`<x> ^ <y>` 或 `math.pow(<x>, <y>)`（5.2 已移除，用 ^）
```lua
-- 用 ^ 运算符求幂
2 ^ 10        -- 1024.0
8 ^ (1/3)     -- 2.0
```

---

**基本写法：自然对数与任意底对数**
`math.log(<x> [, <底>])`
```lua
-- 默认自然对数
math.log(2.71828)     -- 1.0
math.log(100, 10)     -- 2.0 任意底对数
math.exp(1)           -- 2.71828...  e 的幂
```

---

## 三角函数

**基本写法：三角函数**
`math.sin(<rad>)` / `math.cos(<rad>)` / `math.tan(<rad>)`
```lua
-- 参数为弧度
math.sin(0)              -- 0.0
math.cos(0)              -- 1.0
math.tan(math.pi / 4)    -- 1.0
```

---

**基本写法：反三角函数**
`math.asin(<x>)` / `math.acos(<x>)` / `math.atan(<y> [, <x>])`
```lua
-- 返回弧度
math.asin(1)           -- 1.5707963...  即 pi/2
math.acos(1)           -- 0.0
math.atan(1)           -- 0.7853981...  即 pi/4

-- Lua 5.3+ 双参数 atan2
math.atan(1, 1)        -- 0.7853981...
```

---

**基本写法：角度弧度互转**
`math.rad(<deg>)` / `math.deg(<rad>)`
```lua
-- 角度转弧度
math.rad(180)    -- 3.1415926535898
math.deg(math.pi)   -- 180.0
```

---

## 取模与符号

**基本写法：取模**
`math.fmod(<x>, <y>)` 或 `<x> % <y>`
```lua
-- fmod 结果符号同 x；% 结果符号同 y
math.fmod(-7, 3)    -- -1.0
-7 % 3              -- 2  (Lua % 运算符)
math.fmod(7, 0)     -- nan
```

---

**基本写法：取符号（Lua 5.4 新增）**
`math.ult(<m>, <n>)`
```lua
-- 无符号比较 m < n（按无符号整数解读）
math.ult(0xFFFFFFFF, 0)   -- false（前者作为无符号很大）
```

---

## 随机数

**基本写法：设置随机种子**
`math.randomseed(<seed>)`
```lua
-- 设置伪随机数种子
math.randomseed(os.time())
math.randomseed(1)             -- 固定种子可复现序列
math.randomseed(os.time(), os.clock())  -- Lua 5.4 支持双种子
```

---

**基本写法：生成随机数**
`math.random([<n> [, <m>]])`
```lua
-- 无参返回 [0,1) 浮点
math.random()        -- 0.3421...
-- 单参返回 [1, n] 整数
math.random(6)       -- 1 到 6 的整数
-- 双参返回 [n, m] 整数
math.random(10, 20)  -- 10 到 20 的整数
```

---

## 类型转换

**基本写法：整数浮点互转**
`math.tointeger(<x>)` / `math.type(<x>)`
```lua
-- Lua 5.3+ 区分整数与浮点
math.type(3)       -- "integer"
math.type(3.0)     -- "float"
math.type("a")     -- nil（非数字）

-- 整数值转 integer 子类型
math.tointeger(3.0)   -- 3
```

---

## 对数函数（Lua 5.4 新增）

**基本写法：整数对数**
`math.log(<x>, <底>)`
```lua
-- Lua 5.4 log 支持整数参数返回整数结果（当可整除时）
math.log(100, 10)   -- 2
math.log(8, 2)      -- 3
```

---

## 注意事项速查

**基本写法：三角函数参数为弧度**
`math.sin(math.rad(<角度>))`
```lua
-- 常见错误：直接传入角度
math.sin(30)             -- 0.5（错误：30 被当作弧度）
math.sin(math.rad(30))   -- 0.5（正确：先转为弧度）
```



<!-- ============ 文档分隔线：017-lua/025-OsLibrary.md ============ -->

# Lua os 库语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 时间获取

**基本写法：当前时间戳**
`os.time([<表>])`
```lua
-- 无参返回当前 UNIX 时间戳（秒）
local t = os.time()        -- 1700000000

-- 传入时间表返回对应时间戳
local stamp = os.time({
    year = 2024, month = 1, day = 1,
    hour = 0, min = 0, sec = 0,
})
```

---

**基本写法：本地时间表**
`os.date([<格式> [, <时间戳>]])`
```lua
-- 默认返回本地时间字符串
os.date()                  -- "01/15/24 12:00:00"

-- 格式化字符串
os.date("%Y-%m-%d %H:%M:%S")          -- "2024-01-15 12:00:00"
os.date("%Y-%m-%d", os.time())        -- 指定时间戳

-- 格式前加 *t 返回时间表
local t = os.date("*t")    -- {year=2024, month=1, day=15, hour=12, ...}
local utc = os.date("!*t") -- UTC 时间表
```

---

**基本写法：常用 date 格式符**
`os.date("<格式>")`
```lua
-- 常用格式符速查
-- %Y  四位年   %m  月(01-12)   %d  日(01-31)
-- %H  时(00-23) %M  分(00-59)  %S  秒(00-60)
-- %A  星期全名  %a  星期缩写   %B  月份全名 %b 月份缩写
-- %w  周几(0-6, 0=周日)  %j  年内第几天(001-366)
-- %p  AM/PM    %I  12 小时制
os.date("%Y年%m月%d日 %H:%M")   -- "2024年01月15日 12:00"
```

---

## 时间差

**基本写法：计算时间差**
`os.difftime(<t2>, <t1>)`
```lua
-- 返回 t2 - t1 的秒数
local t1 = os.time()
-- ... 执行耗时操作
local t2 = os.time()
local cost = os.difftime(t2, t1)   -- 等价于 t2 - t1
```

---

**基本写法：时间表字段**
`<表>.<字段>`
```lua
-- os.date("*t") 返回的表字段
local t = os.date("*t")
-- t.year     年
-- t.month    月 (1-12)
-- t.day      日 (1-31)
-- t.hour     时 (0-23)
-- t.min      分 (0-59)
-- t.sec      秒 (0-60)
-- t.wday     周几 (1-7, 1=周日)
-- t.yday     年内第几天 (1-366)
-- t.isdst    是否夏令时（布尔）
print(t.year, t.month, t.day)
```

---

## 时钟

**基本写法：程序运行时钟**
`os.clock()`
```lua
-- 返回程序使用的 CPU 时间（秒，浮点）
local start = os.clock()
for i = 1, 1e6 do end
print(string.format("耗时 %.3f 秒", os.clock() - start))
```

---

## 环境变量

**基本写法：读取环境变量**
`os.getenv(<名称>)`
```lua
-- 读取系统环境变量，不存在返回 nil
local path = os.getenv("PATH")
local home = os.getenv("HOME") or os.getenv("USERPROFILE")
```

---

## 执行系统命令

**基本写法：执行命令并获取状态**
`os.execute(<命令>)`
```lua
-- Lua 5.1 返回状态码
-- Lua 5.2+ 返回 true/nil, exit_type, status
local ok, reason, code = os.execute("ls -l")
if ok then print("成功，退出码 " .. code) end

-- 仅退出码
os.execute("mkdir -p build")
```

---

**基本写法：退出程序**
`os.exit([<代码> [, <关闭>]])`
```lua
-- 退出 Lua 解释器
os.exit()           -- 默认 0
os.exit(1)          -- 退出码 1
-- Lua 5.2+ 第二参数控制是否关闭 Lua 状态
os.exit(0, true)    -- 退出并关闭状态机
```

---

## 临时资源

**基本写法：临时文件名**
`os.tmpname()`
```lua
-- 返回一个可用临时文件名
local fname = os.tmpname()
local f = io.open(fname, "w")
f:write("tmp"); f:close()
os.remove(fname)
```

---

**基本写法：重命名文件**
`os.rename(<旧名>, <新名>)`
```lua
-- 重命名或移动文件，返回成功标志与错误信息
local ok, err = os.rename("a.txt", "b.txt")
if not ok then print(err) end
```

---

**基本写法：删除文件**
`os.remove(<文件名>)`
```lua
-- 删除文件（不能删目录），返回成功标志与错误
local ok, err = os.remove("temp.log")
if not ok then error(err) end
```

---

## locale 设置

**基本写法：设置区域**
`os.setlocale(<区域> [, <类别>])`
```lua
-- 设置数字、日期等本地化格式
os.setlocale("C")             -- 默认 C 区域
os.setlocale("zh_CN.UTF-8")   -- 中文
os.setlocale("fr_FR", "time") -- 仅设置时间相关
```

---

## 注意事项速查

**基本写法：os.time 字段范围**
`os.time(<表>)`
```lua
-- 时间表字段必须合法，否则返回 nil
-- month 必须 1-12，day 不能超过当月天数
-- hour 必须 0-23，min/sec 必须 0-59
os.time({year=2024, month=13, day=1})  -- nil（月份非法）
```



<!-- ============ 文档分隔线：017-lua/026-LuaJIT.md ============ -->

# Lua LuaJIT

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## LuaJIT 概览

**基本写法：检测 LuaJIT**
`jit.status()` `jit.version`
```lua
-- 检测是否运行在 LuaJIT
if jit then
    print(jit.version)  -- LuaJIT 2.1.x
    print(jit.os)       -- Linux/OSX/Windows
    print(jit.arch)     -- x64/x86/arm
end
```

---

**基本写法：JIT 状态控制**
`jit.on()` `jit.off()`
```lua
-- 开关 JIT 编译
jit.on()   -- 启用 JIT（默认）
jit.off()  -- 关闭，回退到解释器
-- 检查状态
print(jit.status())  -- true/false
```

---

**基本写法：函数级控制**
`jit.on(<函数>)` `jit.off(<函数>)`
```lua
-- 对特定函数开关 JIT
local function hotFunc() end
jit.off(hotFunc)  -- 此函数用解释器执行
jit.on(hotFunc)   -- 恢复 JIT
-- 全文件关闭
-- jit.off()
```

---

## FFI 外部函数接口

**基本写法：ffi.cdef 声明**
`ffi.cdef("<C 声明>")`
```lua
local ffi = require("ffi")
-- 声明 C 函数和类型
ffi.cdef[[
    int printf(const char *fmt, ...);
    typedef struct { int x, y; } Point;
    int *malloc(int size);
    void free(void *p);
]]
```

---

**基本写法：调用 C 函数**
`ffi.C.<函数>(<参数>)`
```lua
local ffi = require("ffi")
ffi.cdef("int printf(const char *fmt, ...);")
-- 直接调用 libc 函数
ffi.C.printf("hello %d\n", 42)
```

---

**基本写法：使用 C 库**
`ffi.load("<库名>")`
```lua
local ffi = require("ffi")
-- 加载动态库
local lib = ffi.load("mylib")  -- libmylib.so
ffi.cdef[[
    int add(int a, int b);
]]
print(lib.add(2, 3))  -- 5
```

---

**基本写法：C 类型与对象**
`ffi.new("<类型>", <值>)`
```lua
local ffi = require("ffi")
ffi.cdef("typedef struct { int x, y; } Point;")
-- 创建 C 对象
local p = ffi.new("Point", {10, 20})
print(p.x, p.y)  -- 10  20
-- 数组
local arr = ffi.new("int[10]")
arr[0] = 42
print(arr[0])  -- 42
```

---

**基本写法：ffi.cast 类型转换**
`ffi.cast("<类型>", <值>)`
```lua
local ffi = require("ffi")
-- 类型转换
local p = ffi.cast("void*", 0x1234)
local n = ffi.cast("intptr_t", p)
print(n)  -- 4660
```

---

**基本写法：ffi.string 转字符串**
`ffi.string(<C 字符串> [, <长度>])`
```lua
local ffi = require("ffi")
ffi.cdef("const char *getenv(const char *name);")
-- C 字符串转 Lua 字符串
local home = ffi.string(ffi.C.getenv("HOME"))
print(home)
```

---

## 性能优化

**基本写法：trace 编译**
`jit.dump` `jit.util`
```lua
-- 查看 JIT 编译的 trace
local opt = require("jit.opt")
opt.start("hotloop=10", "maxtrace=1000")
-- hotloop=10  循环 10 次后编译
-- 也可用命令行
-- luajit -jdump main.lua
```

---

**基本写法：jit.opt 优化选项**
`require("jit.opt").start(<选项>)`
```lua
-- 编译优化选项
local opt = require("jit.opt")
opt.start(
    "maxtrace=2000",     -- 最大 trace 数
    "maxrecord=4000",    -- 最大记录
    "maxirconst=10000",  -- 最大常量
    "maxsnap=500",       -- 最大快照
    "maxmcode=512",      -- 最大机器码 KB
    "hotloop=10",        -- 热点阈值
    "tryside=4"          -- 侧边尝试
)
```

---

## 扩展库

**基本写法：bit 位运算（5.1/5.2 兼容）**
`require("bit")`
```lua
-- LuaJIT 的 bit 库（Lua 5.3+ 有原生位运算）
local bit = require("bit")
local a = bit.band(0xF0, 0x0F)  -- 0
local b = bit.bor(0xF0, 0x0F)   -- 255
local c = bit.bxor(0xFF, 0x0F)  -- 240
local d = bit.lshift(1, 4)      -- 16
local e = bit.rshift(0xFF, 4)   -- 15
```

---

**基本写法：ffi.gc 设置终结器**
`ffi.gc(<对象>, <函数>)`
```lua
local ffi = require("ffi")
ffi.cdef("void free(void *p);")
-- 设置 GC 时的清理函数
local buf = ffi.C.malloc(1024)
ffi.gc(buf, function(p) ffi.C.free(p) end)
-- buf 被回收时自动调用 free
```

---

## 注意事项

**基本写法：ABI 与平台**
`ffi.abi("<属性>")`
```lua
-- 检测平台 ABI
print(ffi.abi("64bit"))  -- true（64 位系统）
print(ffi.abi("le"))     -- true（小端）
print(ffi.abi("win"))    -- true（Windows）
print(ffi.abi("gc64"))   -- LuaJIT 是否 gc64 模式
```

---

**基本写法：兼容性**
`jit.version_num`
```lua
-- 检查 LuaJIT 版本
if jit.version_num >= 20100 then
    -- LuaJIT 2.1+
end
-- 注意：LuaJIT 兼容 Lua 5.1 语法
-- 不支持 5.3+ 整数类型、原生位运算、<close> 等
```



<!-- ============ 文档分隔线：017-lua/027-LuaNeovim.md ============ -->

# Lua Neovim 配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 配置基础

**基本写法：init.lua 入口**
`~/.config/nvim/init.lua`
```lua
-- Neovim Lua 配置入口
-- 标准初始化
vim.g.mapleader = " "
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
```

---

**基本写法：vim.opt 选项设置**
`vim.opt.<选项> = <值>`
```lua
-- 设置 Neovim 选项
vim.opt.ignorecase = true       -- 忽略大小写
vim.opt.smartcase = true        -- 智能大小写
vim.opt.wrap = false            -- 不自动换行
vim.opt.scrolloff = 8           -- 光标保留 8 行
vim.opt.termguicolors = true    -- 24 位颜色
vim.opt.splitright = true       -- 垂直分割在右侧
vim.opt.splitbelow = true       -- 水平分割在下方
```

---

## vim 全局对象

**基本写法：vim.g 全局变量**
`vim.g.<变量> = <值>`
```lua
-- 设置 vim 全局变量
vim.g.mapleader = " "
vim.g.loaded_netrw = 1           -- 禁用 netrw
vim.g.netrw_banner = 0
-- 访问
print(vim.g.mapleader)
```

---

**基本写法：vim.b 缓冲区变量**
`vim.b[<缓冲区>].<变量>`
```lua
-- 缓冲区局部变量
vim.b.current_project = "myapp"
print(vim.b.current_project)
-- 当前缓冲区
vim.b[0].custom = true
```

---

**基本写法：vim.w 窗口变量**
`vim.w.<变量>`
```lua
-- 窗口局部变量
vim.w.is_focused = true
```

---

## 键映射

**基本写法：vim.keymap.set**
`vim.keymap.set(<模式>, <键>, <动作>, <选项>)`
```lua
-- 设置键映射
vim.keymap.set("n", "<leader>w", ":w<CR>", { desc = "保存" })
vim.keymap.set("n", "<leader>q", ":q<CR>", { desc = "退出" })
vim.keymap.set("i", "jk", "<ESC>", { desc = "返回普通模式" })
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv", { desc = "移动选中行下" })
-- 模式：n 普通 i 插入 v 可视 c 命令 t 终端
```

---

**基本写法：映射选项**
`{ buffer = <bufnr>, silent = true, ... }`
```lua
-- 映射选项
vim.keymap.set("n", "<leader>f", function()
    vim.lsp.buf.format()
end, {
    desc = "格式化",
    buffer = true,       -- 仅当前缓冲区
    silent = true,       -- 静默
    noremap = true,      -- 非递归
    expr = false,        -- 非表达式
})
```

---

## 命令与自动命令

**基本写法：vim.api.nvim_create_user_command**
`vim.api.nvim_create_user_command(<名>, <回调>, <选项>)`
```lua
-- 创建用户命令
vim.api.nvim_create_user_command("Hello", function(opts)
    print("Hello, " .. opts.args)
end, { nargs = "*", desc = "打招呼" })
-- :Hello world
```

---

**基本写法：自动命令组**
`vim.api.nvim_create_augroup(<名>, <选项>)`
```lua
-- 创建自动命令组
local group = vim.api.nvim_create_augroup("MyConfig", { clear = true })
vim.api.nvim_create_autocmd("TextYankPost", {
    group = group,
    callback = function()
        vim.highlight.on_yank()
    end,
})
vim.api.nvim_create_autocmd("BufWritePre", {
    group = group,
    pattern = "*.lua",
    callback = function()
        vim.lsp.buf.format()
    end,
})
```

---

## 插件管理

**基本写法：lazy.nvim**
`require("lazy").setup(<插件列表>)`
```lua
-- lazy.nvim 插件管理器
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
vim.opt.rtp:prepend(lazypath)
require("lazy").setup({
    { "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" },
    { "nvim-telescope/telescope.nvim", dependencies = { "nvim-lua/plenary.nvim" } },
    { "neovim/nvim-lspconfig" },
}, {
    install = { colorscheme = { "habamax" } },
    checker = { enabled = true },
})
```

---

**基本写法：插件配置**
`config = function() ... end`
```lua
-- 插件配置回调
{
    "nvim-telescope/telescope.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
        require("telescope").setup({})
        vim.keymap.set("n", "<leader>ff", require("telescope.builtin").find_files)
    end
}
```

---

## API 与函数

**基本写法：vim.fn 调用 vim 函数**
`vim.fn.<函数>(<参数>)`
```lua
-- 调用 vim 内置函数
local cwd = vim.fn.getcwd()
local expand = vim.fn.expand("%:p")
local line = vim.fn.line(".")
vim.fn.mkdir(vim.fn.stdpath("config") .. "/tmp", "p")
```

---

**基本写法：vim.cmd 执行命令**
`vim.cmd("<命令>")`
```lua
-- 执行 Ex 命令
vim.cmd("colorscheme habamax")
vim.cmd("set number")
-- 多行
vim.cmd([[
    augroup MyGroup
        autocmd!
    augroup END
]])
```

---

**基本写法：vim.notify 通知**
`vim.notify(<消息>, <级别>)`
```lua
-- 显示通知
vim.notify("Hello", vim.log.levels.INFO)
vim.notify("警告", vim.log.levels.WARN)
vim.notify("错误", vim.log.levels.ERROR)
```

---

## LSP 配置

**基本写法：lspconfig**
`require("lspconfig").<服务器>.setup(<配置>)`
```lua
-- 配置语言服务器
local lspconfig = require("lspconfig")
lspconfig.lua_ls.setup({
    settings = {
        Lua = {
            diagnostics = { globals = { "vim" } },
            workspace = { checkThirdParty = false },
        }
    }
})
lspconfig.clangd.setup({})
lspconfig.pyright.setup({})
```
