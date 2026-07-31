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