# TypeScript tsconfig 配置速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 配置文件基础

**基本写法：tsconfig.json 结构**
`{ "compilerOptions": { }, "include": [], "exclude": [] }`
```json
// 项目根目录的 TS 配置文件
{
    "compilerOptions": {
        "target": "ES2022",
        "module": "ESNext"
    },
    "include": ["src"],
    "exclude": ["node_modules"]
}
```

---

**基本写法：extends 继承**
`{ "extends": "<基础配置>" }`
```json
// 继承基础配置再覆盖
{
    "extends": "./tsconfig.base.json",
    "compilerOptions": { "strict": true }
}
```

---

## target 编译目标

**基本写法：target 选项**
`"target": "ES2022"`
```json
// 指定编译目标 JS 版本
// ES3 ES5 ES6 ES2015-ES2023 ESNext
{
    "compilerOptions": { "target": "ES2022" }
}
```

---

**基本写法：lib 指定类型库**
`"lib": ["ES2022", "DOM"]`
```json
// 指定可用的类型库
{
    "compilerOptions": {
        "lib": ["ES2022", "DOM", "DOM.Iterable"]
    }
}
```

---

## module 模块系统

**基本写法：module 选项**
`"module": "ESNext"`
```json
// 指定模块系统
// CommonJS ESNext AMD UMD Node16
{
    "compilerOptions": { "module": "ESNext" }
}
```

---

**基本写法：moduleResolution 解析策略**
`"moduleResolution": "bundler"`
```json
// 模块解析策略
// node classic bundler node16 nodenext
{
    "compilerOptions": { "moduleResolution": "bundler" }
}
```

---

**基本写法：Node 项目配置**
`"module": "Node16"`
```json
// Node 项目推荐配置
{
    "compilerOptions": {
        "module": "Node16",
        "moduleResolution": "Node16"
    }
}
```

---

## 严格模式

**基本写法：strict 总开关**
`"strict": true`
```json
// 开启所有严格检查
{
    "compilerOptions": { "strict": true }
}
```

---

**基本写法：noImplicitAny**
`"noImplicitAny": true`
```json
// 禁止隐式 any
function fn(x) {}  // 报错
```

---

**基本写法：strictNullChecks**
`"strictNullChecks": true`
```json
// 严格区分 null undefined
let s: string = null  // 报错
```

---

**基本写法：strictFunctionTypes**
`"strictFunctionTypes": true`
```json
// 严格函数类型检查
```

---

**基本写法：noUnusedLocals**
`"noUnusedLocals": true`
```json
// 未使用的局部变量报错
const a = 1  // 报错如果未使用
```

---

**基本写法：noUnusedParameters**
`"noUnusedParameters": true`
```json
// 未使用的参数报错
function fn(a, b) { return a }  // b 报错
```

---

**基本写法：noImplicitReturns**
`"noImplicitReturns": true`
```json
// 函数所有分支必须返回
function fn(x: boolean) {
    if (x) return 1  // 报错缺少 else 分支
}
```

---

**基本写法：noFallthroughCasesInSwitch**
`"noFallthroughCasesInSwitch": true`
```json
// switch case 不允许穿透
switch (x) {
    case 1: doA();  // 报错需 break
    case 2: doB();
}
```

---

## 路径映射

**基本写法：baseUrl 与 paths**
`"paths": { "<别名>": ["<路径>"] }`
```json
// 配置路径别名
{
    "compilerOptions": {
        "baseUrl": ".",
        "paths": {
            "@/*": ["src/*"],
            "@components/*": ["src/components/*"]
        }
    }
}
```

---

**基本写法：rootDirs 多根目录**
`"rootDirs": ["<目录1>", "<目录2>"]`
```json
// 虚拟目录组合
{
    "compilerOptions": {
        "rootDirs": ["src", "generated"]
    }
}
```

---

**基本写法：rootDir 与 outDir**
`"rootDir": "src"` | `"outDir": "dist"`
```json
// 指定源码根与输出目录
{
    "compilerOptions": {
        "rootDir": "src",
        "outDir": "dist"
    }
}
```

---

## 类型解析

**基本写法：typeRoots**
`"typeRoots": ["<路径>"]`
```json
// 指定 @types 目录
{
    "compilerOptions": {
        "typeRoots": ["./node_modules/@types", "./types"]
    }
}
```

---

**基本写法：types 显式指定**
`"types": ["node", "jest"]`
```json
// 仅包含指定类型包
{
    "compilerOptions": { "types": ["node", "jest"] }
}
```

---

**基本写法：skipLibCheck**
`"skipLibCheck": true`
```json
// 跳过声明文件检查提升速度
{
    "compilerOptions": { "skipLibCheck": true }
}
```

---

## 输出格式

**基本写法：sourceMap**
`"sourceMap": true`
```json
// 生成 source map 文件
{
    "compilerOptions": { "sourceMap": true }
}
```

---

**基本写法：declaration**
`"declaration": true`
```json
// 生成 .d.ts 声明文件
{
    "compilerOptions": { "declaration": true }
}
```

---

**基本写法：declarationMap**
`"declarationMap": true`
```json
// 生成声明文件的 source map
{
    "compilerOptions": { "declarationMap": true }
}
```

---

**基本写法：removeComments**
`"removeComments": true`
```json
// 输出移除注释
{
    "compilerOptions": { "removeComments": true }
}
```

---

**基本写法：noEmit**
`"noEmit": true`
```json
// 仅类型检查不输出文件
{
    "compilerOptions": { "noEmit": true }
}
```

---

## JSX 配置

**基本写法：jsx 选项**
`"jsx": "react-jsx"`
```json
// JSX 处理模式
// preserve react react-native react-jsx
{
    "compilerOptions": { "jsx": "react-jsx" }
}
```

---

**基本写法：jsxImportSource**
`"jsxImportSource": "<包>"`
```json
// 指定 JSX 工厂导入源
{
    "compilerOptions": {
        "jsx": "react-jsx",
        "jsxImportSource": "preact"
    }
}
```

---

## 装饰器配置

**基本写法：开启装饰器**
`"experimentalDecorators": true`
```json
// 启用实验性装饰器
{
    "compilerOptions": {
        "experimentalDecorators": true,
        "emitDecoratorMetadata": true
    }
}
```

---

## 互操作

**基本写法：esModuleInterop**
`"esModuleInterop": true`
```json
// 允许默认导入 CommonJS 模块
import fs from "fs"  // 需要 esModuleInterop
```

---

**基本写法：allowSyntheticDefaultImports**
`"allowSyntheticDefaultImports": true`
```json
// 允许从无默认导出的模块默认导入仅类型
```

---

**基本写法：allowJs**
`"allowJs": true`
```json
// 允许编译 JS 文件
{
    "compilerOptions": { "allowJs": true }
}
```

---

**基本写法：checkJs**
`"checkJs": true`
```json
// 检查 JS 文件类型错误
{
    "compilerOptions": { "checkJs": true }
}
```

---

## 项目引用

**基本写法：references**
`"references": [{ "path": "<项目>" }]`
```json
// 项目引用用于 monorepo
{
    "references": [
        { "path": "./packages/shared" },
        { "path": "./packages/app" }
    ]
}
```

---

**基本写法：composite**
`"composite": true`
```json
// 项目引用必须开启
{
    "compilerOptions": {
        "composite": true,
        "declaration": true
    }
}
```

---

**基本写法：incremental**
`"incremental": true`
```json
// 增量编译提升速度
{
    "compilerOptions": {
        "incremental": true,
        "tsBuildInfoFile": ".tsbuildinfo"
    }
}
```

---

## 监听与构建

**基本写法：tsc --watch**
`tsc --watch`
```bash
# 监听文件变化自动编译
tsc -w
```

---

**基本写法：tsc --build**
`tsc --build`
```bash
# 构建项目引用
tsc -b
```

---

**基本写法：tsc --noEmit**
`tsc --noEmit`
```bash
# 仅类型检查不输出
tsc --noEmit
```

---

## 现代项目配置

**基本写法：Vite React 模板**
`{ "compilerOptions": { } }`
```json
// Vite + React 项目推荐配置
{
    "compilerOptions": {
        "target": "ES2020",
        "useDefineForClassFields": true,
        "lib": ["ES2020", "DOM", "DOM.Iterable"],
        "module": "ESNext",
        "moduleResolution": "bundler",
        "jsx": "react-jsx",
        "strict": true,
        "noEmit": true,
        "isolatedModules": true,
        "skipLibCheck": true
    },
    "include": ["src"]
}
```

---

**基本写法：Node 项目配置**
`{ "compilerOptions": { } }`
```json
// Node.js 后端项目推荐配置
{
    "compilerOptions": {
        "target": "ES2022",
        "module": "Node16",
        "moduleResolution": "Node16",
        "outDir": "dist",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "types": ["node"]
    },
    "include": ["src"]
}
```

---

**基本写法：库开发配置**
`{ "compilerOptions": { } }`
```json
// npm 包开发推荐配置
{
    "compilerOptions": {
        "target": "ES2020",
        "module": "ESNext",
        "moduleResolution": "bundler",
        "declaration": true,
        "declarationMap": true,
        "sourceMap": true,
        "outDir": "dist",
        "strict": true,
        "skipLibCheck": true
    },
    "include": ["src"],
    "exclude": ["node_modules", "dist"]
}
```

---

## 实用配置

**基本写法：resolveJsonModule**
`"resolveJsonModule": true`
```json
// 允许导入 JSON 文件
import pkg from "./package.json"
```

---

**基本写法：isolatedModules**
`"isolatedModules": true`
```json
// 单文件转译约束
// 类型导入必须显式 export type
```

---

**基本写法：useDefineForClassFields**
`"useDefineForClassFields": true`
```json
// 使用 ES 标准 class 字段语义
class A { x = 1 }  // 使用 defineProperty
```

---

**基本写法：forceConsistentCasingInFileNames**
`"forceConsistentCasingInFileNames": true`
```json
// 强制文件名大小写一致
```

---

## 编译诊断

**基本写法：diagnostics**
`tsc --diagnostics`
```bash
# 输出编译诊断信息
tsc --diagnostics --extendedDiagnostics
```

---

**基本写法：listFiles**
`tsc --listFiles`
```bash
# 列出所有编译文件
tsc --listFiles
```

---

**基本写法：explainFiles**
`tsc --explainFiles`
```bash
# 解释文件为何被包含
tsc --explainFiles
```

---

## 常用脚本

**基本写法：package.json scripts**
`{ "scripts": { } }`
```json
// package.json 常用 TS 脚本
{
    "scripts": {
        "build": "tsc",
        "dev": "tsc --watch",
        "typecheck": "tsc --noEmit",
        "clean": "rm -rf dist"
    }
}
```
