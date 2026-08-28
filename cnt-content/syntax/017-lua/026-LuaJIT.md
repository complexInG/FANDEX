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
