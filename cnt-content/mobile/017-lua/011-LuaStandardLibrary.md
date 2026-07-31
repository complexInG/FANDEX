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
