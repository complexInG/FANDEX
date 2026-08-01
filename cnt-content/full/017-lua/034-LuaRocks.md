---
order: 340
title: Lua LuaRocks 包管理
module: 017-lua
category: '017-lua'
difficulty: beginner
description: Lua LuaRocks 包管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

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
| Lua LuaRocks 包管理 | 034-LuaRocks | 本文自身 |
| Lua io 库语法速查手册 | 035-IoLibrary | 本文的并列主题 |
| Lua math 库语法速查手册 | 036-MathLibrary | 本文的并列主题 |
| Lua os 库语法速查手册 | 037-OsLibrary | 本文的并列主题 |
