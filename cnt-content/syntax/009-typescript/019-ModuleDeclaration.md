# TypeScript 模块声明

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 模块基础

**基本写法：导出**
`export <声明>`
```typescript
// 导出变量函数类型等
export const name = "Tom"
export function greet() {}
export type User = { name: string }
```

---

**基本写法：默认导出**
`export default <声明>`
```typescript
// 每个模块只能有一个默认导出
export default class User {}
```

---

**基本写法：命名导入**
`import { <名称>, <名称> } from "<模块>"`
```typescript
// 按名导入多个
import { name, greet } from "./user"
```

---

**基本写法：默认导入**
`import <名称> from "<模块>"`
```typescript
// 导入默认导出
import User from "./User"
```

---

**基本写法：别名导入**
`import { <名称> as <别名> } from "<模块>"`
```typescript
// 重命名导入避免冲突
import { name as userName } from "./user"
```

---

**基本写法：命名空间导入**
`import * as <名称> from "<模块>"`
```typescript
// 整体导入为一个对象
import * as utils from "./utils"
utils.format()
```

---

## 模块声明

**基本写法：声明模块**
`declare module "<模块名>"`
```typescript
// 为 JS 模块补类型声明
declare module "my-lib" {
    export function greet(name: string): string
    export const version: string
}
```

---

**基本写法：通配符模块声明**
`declare module "*<后缀>"`
```typescript
// 处理非 JS 资源导入
declare module "*.css" {
    const content: string
    export default content
}
declare module "*.png" {
    const src: string
    export default src
}
```

---

**基本写法：声明全局变量**
`declare const <变量>: <类型>`
```typescript
// 声明全局变量类型
declare const VERSION: string
declare const __DEV__: boolean
```

---

**基本写法：声明全局函数**
`declare function <名称>(<参数>): <返回类型>`
```typescript
// 声明全局函数
declare function $(selector: string): HTMLElement
```

---

## namespace 命名空间

**基本写法：定义命名空间**
`namespace <名称> { }`
```typescript
// 命名空间组织相关类型
namespace App {
    export function init() {}
    export const version = "1.0"
}
App.init()
```

---

**基本写法：嵌套命名空间**
`namespace <外层>.<内层> { }`
```typescript
// 命名空间嵌套
namespace App.Config {
    export const port = 3000
}
App.Config.port
```

---

**基本写法：命名空间与模块结合**
`export namespace <名称> { }`
```typescript
// 模块中导出命名空间
export namespace Utils {
    export function format(s: string) { return s.trim() }
}
```

---

## 声明合并

**基本写法：同名接口合并**
`interface <名称> { }`
```typescript
// 同名接口自动合并
interface User { name: string }
interface User { age: number }
const u: User = { name: "T", age: 18 }
```

---

**基本写法：同名命名空间合并**
`namespace <名称> { }`
```typescript
// 命名空间自动合并
namespace App { export const a = 1 }
namespace App { export const b = 2 }
App.a; App.b
```

---

**基本写法：函数与接口合并**
`function <函数>(); interface <函数> { }`
```typescript
// 函数声明可与接口合并添加属性
function greet(name: string): string
namespace greet {
    export const version = "1.0"
}
greet.version
```

---

## 全局声明

**基本写法：global 声明**
`declare global { }`
```typescript
// 在模块中扩展全局
declare global {
    interface Window { myApp: any }
}
window.myApp = {}
```

---

**基本写法：扩展全局接口**
`declare global { interface <名称> { } }`
```typescript
// 扩展内置全局接口
declare global {
    interface Array<T> { last(): T | undefined }
}
Array.prototype.last = function () { return this[this.length - 1] }
```

---

## 模块扩展

**基本写法：扩展模块声明**
`declare module "<模块>" { interface <名称> { } }`
```typescript
// 扩展已存在模块的类型
declare module "express" {
    interface Request { user?: User }
}
```

---

**基本写法：扩展 Express 类型**
`declare module "express" { interface Request { } }`
```typescript
// 给 Express Request 添加属性
declare module "express-serve-static-core" {
    interface Request { userId: string }
}
```

---

## ambient 声明

**基本写法：声明文件**
`<文件>.d.ts`
```typescript
// 声明文件仅类型不产生代码
// types.d.ts
declare module "lib" {
    export function fn(): void
}
```

---

**基本写法：声明类型别名**
`declare type <名称> = <类型>`
```typescript
// 全局类型别名声明
declare type ID = string | number
```

---

**基本写法：声明枚举**
`declare enum <名称> { }`
```typescript
// 声明外部枚举
declare enum Color { Red, Green, Blue }
```

---

## 三斜线指令

**基本写法：引用类型声明**
`/// <reference types="<包>" />`
```typescript
// 引入 @types 包
/// <reference types="node" />
```

---

**基本写法：引用路径**
`/// <reference path="<文件>" />`
```typescript
// 引入指定声明文件
/// <reference path="./types.d.ts" />
```

---

**基本写法：引用库**
`/// <reference lib="<库>" />`
```typescript
// 引入内置 lib
/// <reference lib="es2017" />
```

---

## 类型与值导入

**基本写法：import type**
`import type { <类型> } from "<模块>"`
```typescript
// 仅导入类型编译时移除
import type { User } from "./types"
```

---

**基本写法：内联 type 限定**
`import { type <类型>, <值> } from "<模块>"`
```typescript
// 混合导入时标记类型
import { type User, getUser } from "./user"
```

---

**基本写法：export type**
`export type { <类型> }`
```typescript
// 仅导出类型
export type { User } from "./types"
```

---

## CommonJS 互操作

**基本写法：导入 CommonJS 模块**
`import <名称> = require("<模块>")`
```typescript
// CommonJS 模块导入
import fs = require("fs")
```

---

**基本写法：导出 CommonJS**
`export = <对象>`
```typescript
// CommonJS 风格导出
class User {}
export = User
```

---

**基本写法：esModuleInterop**
`import <名称> from "<CommonJS模块>"`
```typescript
// 开启 esModuleInterop 后默认导入
import fs from "fs"
```

---

## 动态导入

**基本写法：动态 import 类型**
`const <模块> = await import("<模块>")`
```typescript
// 动态导入类型为 Promise<typeof import>
const mod = await import("./user")
mod.greet()
```

---

**基本写法：动态导入类型**
`type <类型> = typeof import("<模块>")`
```typescript
// 推导模块类型
type UserModule = typeof import("./user")
```

---

## 实用模式

**基本写法：barrel 导出**
`export * from "<模块>"`
```typescript
// index.ts 汇总导出
export * from "./user"
export * from "./post"
export * from "./comment"
```

---

**基本写法：选择性 barrel**
`export { <名称>, <名称> } from "<模块>"`
```typescript
// 选择性重新导出
export { User, getUser } from "./user"
export type { UserProps } from "./user"
```

---

**基本写法：声明 JSON 模块**
`declare module "*.json"`
```typescript
// 允许 import JSON
declare module "*.json" {
    const value: any
    export default value
}
```

---

**基本写法：环境变量类型**
`interface ImportMetaEnv { }`
```typescript
// Vite 环境变量类型
interface ImportMetaEnv {
    readonly VITE_API: string
}
interface ImportMeta {
    readonly env: ImportMetaEnv
}
```

---

## 模块解析

**基本写法：node 解析策略**
`"moduleResolution": "node"`
```typescript
// tsconfig 配置 node 经典解析
// 查找 node_modules 文件扩展名
```

---

**基本写法：bundler 解析策略**
`"moduleResolution": "bundler"`
```typescript
// TS 5.0+ 适配打包工具的解析
// 支持 package.json exports 字段
```

---

**基本写法：paths 路径映射**
`"paths": { "<别名>": ["<路径>"] }`
```typescript
// tsconfig 配置路径别名
{
    "compilerOptions": {
        "baseUrl": ".",
        "paths": { "@/*": ["src/*"] }
    }
}
```

---

## 注意事项

**基本写法：模块与脚本区分**
`export <声明>` 或 `import <名称>`
```typescript
// 含 import export 的是模块
// 否则是脚本全局可见
```

---

**基本写法：isolatedModules**
`"isolatedModules": true`
```typescript
// 单文件转译模式约束
// 要求类型导入显式标注
export type { User }
```
