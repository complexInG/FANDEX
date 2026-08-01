---
order: 520
title: TypeScript tsc 编译命令速查
module: typescript

category: '009-typescript'
difficulty: beginner
description: TypeScript tsc 编译命令速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 基础编译

**基本写法：编译文件**
`tsc <文件.ts> [选项]`
```bash
# 编译为同名 js
tsc main.ts
tsc src/*.ts
```

---

**基本写法：编译并输出**
`tsc <文件> --outFile <输出>`
```bash
# 合并输出单文件
tsc a.ts b.ts --outFile bundle.js
# 指定输出目录
tsc src/*.ts --outDir dist
```

---

## 项目与配置

**基本写法：按 tsconfig 编译**
`tsc -p <路径>`
```bash
# 使用指定配置文件
tsc -p tsconfig.json
tsc -p ./packages/core
```

---

**基本写法：生成配置文件**
`tsc --init`
```bash
# 生成默认 tsconfig.json
tsc --init
# 仅生成目标为特定版本
tsc --init --target ES2022 --module NodeNext
```

---

## 类型检查模式

**基本写法：只检查不输出**
`tsc --noEmit`
```bash
# CI 常用，仅做类型检查
tsc --noEmit
tsc -p . --noEmit
```

---

**基本写法：监听变更**
`tsc -w`
```bash
# 增量监听重编译
tsc -w
tsc -p . --watch --preserveWatchOutput
```

---

## 模块与目标

**基本写法：指定模块系统**
`tsc --module <值>`
```bash
# ES 模块 / CommonJS / NodeNext 等
tsc --module ES2022
tsc --module NodeNext
tsc --module CommonJS
```

---

**基本写法：指定目标版本**
`tsc --target <值>`
```bash
# 编译降级目标
tsc --target ES2020
tsc --target ESNext
```

---

**基本写法：模块解析策略**
`tsc --moduleResolution <值>`
```bash
# Node10 / NodeNext / Bundler / Classic
tsc --moduleResolution Bundler
tsc --moduleResolution NodeNext
```

---

## 严格模式

**基本写法：开启全部严格**
`tsc --strict`
```bash
# 等价于一组严格选项
tsc --strict
```

---

**基本写法：单项严格选项**
`tsc --<选项>`
```bash
# 各项严格检查
tsc --noImplicitAny
tsc --strictNullChecks
tsc --strictFunctionTypes
tsc --strictBindCallApply
tsc --strictPropertyInitialization
tsc --noImplicitThis
tsc --alwaysStrict
tsc --useUnknownInCatchVariables
```

---

## 路径与导出

**基本写法：基础路径映射**
`tsconfig: "baseUrl": ".", "paths": { "@/*": ["src/*"] }`
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@core/*": ["packages/core/*"]
    }
  }
}
```

---

**基本写法：声明文件输出**
`tsc --declaration`
```bash
# 生成 .d.ts 类型声明
tsc --declaration
tsc --declaration --emitDeclarationOnly
tsc --declarationDir types
```

---

## 常用输出控制

**基本写法：sourceMap 与导出**
`tsc --<选项>`
```bash
# 生成 source map
tsc --sourceMap
# 仅生成类型不生成 js
tsc --emitDeclarationOnly
# 不生成注释
tsc --removeComments
# 保留 import 断言
tsc --verbatimModuleSyntax
```

---

## JSX 与库

**基本写法：JSX 支持**
`tsc --jsx <值>`
```bash
# react / react-jsx / preserve / react-native
tsc --jsx react-jsx
```

---

**基本写法：引入 lib**
`tsconfig: "lib": ["<库>"]`
```json
{
  "compilerOptions": {
    "lib": ["ES2022", "DOM", "DOM.Iterable"]
  }
}
```

---

## 增量构建

**基本写法：增量编译**
`tsc --incremental`
```bash
# 缓存到 .tsbuildinfo 加速
tsc --incremental
tsc --incremental --tsBuildInfoFile ./.cache/info
```

---

## 命令行诊断

**基本写法：显示版本与原因**
`tsc --version` | `tsc --explainFiles`
```bash
tsc -v                       # 版本
tsc --listFiles              # 列出所有参与编译文件
tsc --explainFiles           # 解释为何包含某文件
tsc --showConfig             # 展开继承后的最终配置
```

---

## 监听与项目引用

**基本写法：项目引用**
`tsconfig: "references": [{ "path": "./shared" }]`
```json
{
  "references": [{ "path": "./packages/shared" }]
}
```

---

**基本写法：构建引用项目**
`tsc -b [--dry]`
```bash
# 增量构建依赖项目
tsc -b
tsc -b --dry       # 模拟不写盘
tsc -b --clean     # 清理构建产物
tsc -b --force     # 强制全量构建
```

---

## 参考文献

TypeScript 官方文档：https://www.typescriptlang.org/docs/
TS 手册中文版：https://www.typescriptlang.org/zh/docs/handbook/
TypeScript 发布计划：https://github.com/microsoft/TypeScript/wiki/Roadmap
tsconfig 参考：https://www.typescriptlang.org/tsconfig/
Type Challenges：https://github.com/type-challenges/type-challenges

## 延伸阅读

TS 基础类型与接口，见 009-typescript 模块文档。
TS 泛型与工具类型，见 009-typescript 模块进阶文档。
React + TS 组件类型，见 011-react 模块。
Vue3 + TS 组合式 API，见 010-vue3 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 TypeScript 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 条件类型与类型体操

条件类型 T extends U ? X : Y 在类型层做分支；infer 提取类型片段（ReturnType、Parameters 的底层实现）。
映射类型 { [K in keyof T]: T[K] } 变换对象结构；key remapping（as）过滤键。
模板字面量类型 `${K}Id` 组合字符串类型，配合推断实现精确匹配。
工程建议：类型体操控制在团队可读范围，复杂类型用注释解释意图。

### 13.2 声明文件与模块解析

.d.ts 声明 JS 库类型：declare module、declare global、export =；@types 包集中管理社区类型。
moduleResolution：node16/nodenext 遵循 ESM/CJS 规则；bundler 模式适配 Vite。
三斜线指令（/// reference）用于旧式依赖声明；现代代码用 import。
发布库时生成 .d.ts 并测试（arethetypeswrong）。
