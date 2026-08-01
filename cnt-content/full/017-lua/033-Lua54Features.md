---
order: 330
title: Lua 5.4 新特性
module: lua

category: '017-lua'
difficulty: beginner
description: Lua 5.4 新特性 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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
