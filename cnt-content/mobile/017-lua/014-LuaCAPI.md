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
