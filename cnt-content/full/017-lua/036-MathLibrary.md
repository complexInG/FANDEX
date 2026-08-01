---
order: 360
title: Lua math 库语法速查手册
module: 017-lua
category: '017-lua'
difficulty: beginner
description: Lua math 库语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

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

## 参考文献



Lua 官方文档：https://www.lua.org/docs.html
Lua 5.4 参考手册：https://www.lua.org/manual/5.4/
LuaJIT：https://luajit.org/
OpenResty 文档：https://openresty.org/cn/
Redis EVAL 文档：https://redis.io/docs/latest/develop/programming/

## 延伸阅读



Lua 与 Redis 脚本，见 022-redis 模块相关文档。
Lua 与 OpenResty 网关，见 031-devops 模块相关文档。
游戏开发与脚本扩展，见 017-lua 模块文档。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Lua 课程。

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Lua 概述与环境配置 | 001-LuaOverviewEnvSetup | 本文的前置基础 |
| 程序结构与基本语法 | 002-ProgramStructureBasicSyntax | 本文的并列主题 |
| 数据类型与 Table 详解 | 003-DataTypeTableDetailed | 本文的并列主题 |
| 函数与闭包 | 004-FunctionAndClosure | 本文的并列主题 |
| 元表与面向对象编程 | 005-MetatableOOP | 本文的并列主题 |
| 表与元表进阶 | 006-TableMetatableAdvanced | 本文的并列主题 |
| 面向对象编程 | 007-OOP | 本文的并列主题 |
| 协程详解 | 008-CoroutineDetailed | 本文的并列主题 |
| 环境与模块 | 009-EnvironmentModule | 本文的前置基础 |
| 字符串模式匹配 | 010-StringPatternMatching | 本文的并列主题 |
| Lua 与 C 交互 | 011-LuaC | 本文的并列主题 |
| LuaJIT | 012-LuaJIT | 本文的并列主题 |
| Lua与Love2D | 013-LuaLove2D | 本文的并列主题 |
| Lua与Neovim | 014-LuaNeovim | 本文的并列主题 |
| Lua与Redis脚本 | 015-LuaRedisScript | 本文的并列主题 |
| Lua与Nginx | 016-LuaNginx | 本文的并列主题 |
| 模块与包 | 017-ModulePackage | 本文的并列主题 |
| Lua错误处理 | 018-LuaErrorHandling | 本文的并列主题 |
| Lua迭代器 | 019-LuaIterator | 本文的并列主题 |
| Lua与World of Warcraft | 020-LuaWorldOfWarcraft | 本文的并列主题 |
| Lua性能优化 | 021-LuaPerformance | 本文的性能延伸 |
| Lua调试技巧 | 022-LuaDebug | 本文的并列主题 |
| 协程与异步 | 023-CoroutineAsync | 本文的并列主题 |
| 标准库详解 | 024-StandardLibraryDetailed | 本文的并列主题 |
| 元表与元方法详解 | 025-MetatableMetamethodDetailed | 本文的并列主题 |
| 协程非抢占式调度 | 026-CoroutineNonPreemptiveScheduling | 本文的并列主题 |
| 弱表 | 027-WeakTable | 本文的并列主题 |
| 环境与全局变量管理 | 028-EnvironmentGlobalVariable | 本文的前置基础 |
| C-API栈操作 | 029-CAPIStackOperation | 本文的并列主题 |
| 用户数据 | 030-UserData | 本文的并列主题 |
| 模块加载 | 031-ModuleLoading | 本文的并列主题 |
| Lua 文件 IO 进阶 | 032-FileIO | 本文的并列主题 |
| Lua 5.4 新特性 | 033-Lua54Features | 本文的并列主题 |
| Lua LuaRocks 包管理 | 034-LuaRocks | 本文的并列主题 |
| Lua io 库语法速查手册 | 035-IoLibrary | 本文的并列主题 |
| Lua math 库语法速查手册 | 036-MathLibrary | 本文自身 |
| Lua os 库语法速查手册 | 037-OsLibrary | 本文的并列主题 |
