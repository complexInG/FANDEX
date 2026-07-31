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