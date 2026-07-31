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
