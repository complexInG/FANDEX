---
order: 10
tags:
  - typescript
difficulty: beginner
title: 'TypeScript 概述与环境配置'
module: typescript
category: 'TS Advanced'
description: 'TypeScript 发展历程、与 JavaScript 的关系与开发环境搭建。'
author: Anonymous
related:
  - typescript/语法速查
  - typescript/基础类型系统
  - typescript/接口与类型别名
prerequisites: []
updated: '2026-08-01'
---
## 1. TypeScript 概述 (Overview)

TypeScript 是 JavaScript 的一个**超集**，由微软开发，于 2012 年首次发布。它在 JavaScript 的基础上增加了**静态类型系统**和其他高级特性，最终通过编译器转换为纯 JavaScript 代码运行。TypeScript 的设计目标是帮助开发者构建大型、复杂的应用程序，提供更好的开发体验和代码质量。

### 1.1 核心价值 (Core Value)

| 价值                | 描述                                             | 优势                               |
| :------------------ | :----------------------------------------------- | :--------------------------------- |
| **类型安全**        | 在开发阶段发现潜在错误 (如拼写错误、类型不匹配)  | 减少运行时错误，提高代码可靠性     |
| **更好的 IDE 支持** | 自动补全、重构更精准，提供更好的代码导航         | 提高开发效率，减少编码错误         |
| **增强可读性**      | 类型注解使代码更加自文档化                       | 便于团队协作和代码维护             |
| **支持最新语法**    | 提前使用尚未在所有浏览器实现的 ECMAScript 新特性 | 保持代码现代化，无需等待浏览器支持 |
| **渐进式 adoption** | 可以与 JavaScript 代码无缝集成                   | 便于现有项目逐步迁移到 TypeScript  |
| **大型项目支持**    | 提供模块化、命名空间等特性                       | 适合构建和维护大型应用程序         |

### 1.2 TypeScript 与 JavaScript 的关系

TypeScript 是 JavaScript 的超集，这意味着：

- **所有 JavaScript 代码都是有效的 TypeScript 代码**
- TypeScript 增加了额外的特性，如类型注解、接口、泛型等
- TypeScript 代码最终会被编译为 JavaScript 代码运行
- TypeScript 可以与 JavaScript 代码和库无缝集成

### 1.4 应用场景

TypeScript 适用于以下场景：

- **大型应用程序**：需要类型安全和更好的代码组织
- **团队开发**：需要清晰的代码结构和类型约束
- **前端框架**：React、Vue、Angular 等框架的类型定义
- **Node.js 后端**：提供类型安全的服务器端代码
- **库和工具**：提供类型定义，改善开发者体验

## 2. 环境配置 (Environment Setup)

### 2.1 安装 TypeScript

#### 2.1.1 全局安装

```bash
 # 全局安装 TypeScript 编译器
 npm install -g typescript
 # 验证安装
 tsc --version
```

#### 2.1.2 项目本地安装

```bash
 # 在项目中本地安装 TypeScript
 npm install --save-dev typescript
 # 验证安装
 npx tsc --version
```

### 2.2 初始化 TypeScript 项目

#### 2.2.1 生成 tsconfig.json

```bash
 # 生成默认的 tsconfig.json 文件
 tsc --init
 # 或使用 npm init 初始化项目后添加 TypeScript
 npm init -y
 npm install --save-dev typescript
 npx tsc --init
```

#### 2.2.2 基本项目结构

```mermaid
flowchart TD
    T0["my-project/"]
    T1["tsconfig.json # TypeScript 配置文件"]
    T2["package.json # 项目配置文件"]
    T3["src/ # 源码目录"]
    T4["index.ts # 主入口文件"]
    T5["dist/ # 编译输出目录"]
    T6["index.js # 编译后的 JavaScript 文件"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T4 --> T5
    T5 --> T6
```

### 2.3 编译与运行

#### 2.3.1 基本编译

```bash
 # 编译单个文件
 tsc src/index.ts
 # 编译整个项目 (使用 tsconfig.json)
 tsc
 # 监视模式编译 (文件变化时自动重新编译)
 tsc --watch
```

#### 2.3.2 使用 ts-node 直接运行

```bash
 # 安装 ts-node
 npm install --save-dev ts-node
 # 直接运行 TypeScript 文件
 npx ts-node src/index.ts
 # 监视模式运行
 npx ts-node --watch src/index.ts
```

#### 2.3.3 使用构建工具

#### Webpack

```bash
 # 安装依赖
 npm install --save-dev webpack webpack-cli ts-loader
 # webpack.config.js
 module.exports = {
  entry: './src/index.ts',
  module: {
  rules: [
  {
  test: /\.tsx?$/,
  use: 'ts-loader',
  exclude: /node_modules/
  }
  ]
  },
  resolve: {
  extensions: ['.tsx', '.ts', '.js']
  },
  output: {
  filename: 'bundle.js',
  path: path.resolve(__dirname, 'dist')
  }
 }
```

#### Vite

```bash
 # 创建 Vite + TypeScript 项目
 npm create vite@latest my-project -- --template react-ts
 # 或使用 Vue + TypeScript
 npm create vite@latest my-project -- --template vue-ts
```

## 3. `tsconfig.json` 核心配置

`tsconfig.json` 是 TypeScript 项目的配置文件，用于指定编译选项和项目设置。

### 3.1 基本配置示例

```json
 {
  "compilerOptions": {
  "target": "ES2020",
  "module": "commonjs",
  "moduleResolution": "node",
  "lib": ["ES2020", "DOM"],
  "strict": true,
  "esModuleInterop": true,
  "skipLibCheck": true,
  "forceConsistentCasingInFileNames": true,
  "outDir": "./dist",
  "rootDir": "./src",
  "sourceMap": true,
  "declaration": true,
  "declarationMap": true,
  "removeComments": false,
  "noEmitOnError":
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
 }
```

### 3.2 核心配置选项

| 选项                                 | 描述                      | 默认值                         | 推荐值                                |
| :----------------------------------- | :------------------------ | :----------------------------- | :------------------------------------ |
| **target**                           | 编译后的 JavaScript 版本  | ES3                            | ES2020 或更高                         |
| **module**                           | 模块化规范                | commonjs                       | commonjs (Node.js) 或 esnext (浏览器) |
| **moduleResolution**                 | 模块解析策略              | node                           | node                                  |
| **lib**                              | 包含的库文件              | 取决于 target                  | ["ES2020", "DOM"]                     |
| **strict**                           | 开启所有严格类型检查      | false                          |                                       |
| **esModuleInterop**                  | 启用 ES 模块互操作性      | false                          |                                       |
| **skipLibCheck**                     | 跳过库文件的类型检查      | false                          |                                       |
| **forceConsistentCasingInFileNames** | 强制文件名大小写一致      | false                          |                                       |
| **outDir**                           | 编译输出目录              | 与源文件同目录                 | "./dist"                              |
| **rootDir**                          | 源码根目录                | 包含所有输入文件的最长公共路径 | "./src"                               |
| **sourceMap**                        | 生成 source map 文件      | false                          | (开发环境)                            |
| **declaration**                      | 生成 .d.ts 类型声明文件   | false                          | (库开发)                              |
| **declarationMap**                   | 为声明文件生成 source map | false                          | (库开发)                              |
| **removeComments**                   | 移除注释                  | false                          | false (保留注释)                      |
| **noEmitOnError**                    | 有错误时不生成输出        | false                          |                                       |

### 3.3 严格模式选项

| 选项                             | 描述                             | 启用条件          |
| :------------------------------- | :------------------------------- | :---------------- |
| **strictNullChecks**             | 严格的 null 和 undefined 检查    | strict:           |
| **strictFunctionTypes**          | 严格的函数类型检查               | strict:           |
| **strictBindCallApply**          | 严格的 bind, call, apply 检查    | strict:           |
| **strictPropertyInitialization** | 严格的属性初始化检查             | strict:           |
| **noImplicitAny**                | 禁止隐式 any 类型                | strict:           |
| **noImplicitThis**               | 禁止隐式 this                    | strict:           |
| **useUnknownInCatchVariables**   | 在 catch 变量中使用 unknown 类型 | strict: (TS 4.0+) |

### 3.4 高级配置选项

| 选项                       | 描述                       | 用途                           |
| :------------------------- | :------------------------- | :----------------------------- |
| **baseUrl**                | 模块解析的基础目录         | 简化模块导入路径               |
| **paths**                  | 模块路径映射               | 自定义模块解析路径             |
| **allowJs**                | 允许编译 JavaScript 文件   | 混合 TypeScript 和 JavaScript  |
| **checkJs**                | 检查 JavaScript 文件的类型 | 对 JavaScript 文件进行类型检查 |
| **jsx**                    | JSX 处理模式               | React 或其他 JSX 框架          |
| **experimentalDecorators** | 启用装饰器                 | 使用装饰器特性                 |
| **emitDecoratorMetadata**  | 生成装饰器元数据           | 配合装饰器使用                 |
| **resolveJsonModule**      | 允许导入 JSON 文件         | 直接导入 JSON 数据             |
| **isolatedModules**        | 每个文件作为独立模块编译   | 与 Babel 等工具配合            |

### 3.5 配置示例

#### 3.5.1 浏览器项目配置

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "esnext",
    "moduleResolution": "node",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "sourceMap": true,
    "jsx": "react-jsx"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

#### 3.5.2 Node.js 项目配置

```json
 {
  "compilerOptions": {
  "target": "ES2020",
  "module": "commonjs",
  "moduleResolution": "node",
  "lib": ["ES2020"],
  "strict": true,
  "esModuleInterop": true,
  "skipLibCheck": true,
  "forceConsistentCasingInFileNames": true,
  "outDir": "./dist",
  "rootDir": "./src",
  "sourceMap": true,
  "declaration":
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
 }
```

## 4. 工具链与生态系统

### 4.1 开发工具

| 工具              | 描述                     | 用途                 |
| :---------------- | :----------------------- | :------------------- |
| **tsc**           | TypeScript 编译器        | 编译 TypeScript 代码 |
| **ts-node**       | 直接运行 TypeScript 文件 | 开发和调试           |
| **tslint/eslint** | TypeScript 代码检查工具  | 代码质量检查         |
| **prettier**      | 代码格式化工具           | 保持代码风格一致     |
| **jest**          | 测试框架                 | 单元测试             |
| **webpack**       | 模块打包工具             | 前端项目构建         |
| **vite**          | 现代前端构建工具         | 快速开发和构建       |
| **rollup**        | 模块打包工具             | 库构建               |

### 4.2 类型定义

| 类型定义                | 描述                   | 安装方式                                                                            |
| :---------------------- | :--------------------- | :---------------------------------------------------------------------------------- |
| **@types/node**         | Node.js 类型定义       | `npm install --save-dev @types/node`                                                |
| **@types/react**        | React 类型定义         | `npm install --save-dev @types/react`                                               |
| **@types/react-dom**    | React DOM 类型定义     | `npm install --save-dev @types/react-dom`                                           |
| **@types/jest**         | Jest 类型定义          | `npm install --save-dev @types/jest`                                                |
| \*_@typescript-eslint/_ | ESLint TypeScript 插件 | `npm install --save-dev @typescript-eslint/eslint-plugin @typescript-eslint/parser` |

### 4.3 IDE 支持

推荐的 IDE 和编辑器：
| IDE/编辑器 | 特点 | 推荐插件 |
| :--- | :--- | :--- |
| **Visual Studio Code** | 官方推荐，内置 TypeScript 支持 | TypeScript Hero, ESLint, Prettier |
| **WebStorm** | 强大的 IDE，内置 TypeScript 支持 | ESLint, Prettier |
| **Sublime Text** | 轻量级编辑器 | TypeScript, SublimeLinter |
| **Atom** | 开源编辑器 | atom-typescript |

## 5. 最佳实践

### 5.1 项目结构

```mermaid
flowchart TD
    T0["my-project/"]
    T1["tsconfig.json # TypeScript 配置"]
    T2["package.json # 项目配置"]
    T3[".eslintrc.json # ESLint 配置"]
    T4[".prettierrc # Prettier 配置"]
    T5["src/ # 源码目录"]
    T6["index.ts # 主入口"]
    T7["components/ # 组件"]
    T8["utils/ # 工具函数"]
    T9["types/ # 类型定义"]
    T10["interfaces/ # 接口定义"]
    T11["dist/ # 编译输出"]
    T12["tests/ # 测试文件"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T0 --> T5
    T10 --> T11
    T10 --> T12
```

### 5.2 类型定义最佳实践

- **使用接口定义对象结构**：清晰描述对象的形状
- **使用类型别名**：为复杂类型创建有意义的名称
- **避免使用 any 类型**：尽量使用具体类型或联合类型
- **使用泛型**：提高代码复用性和类型安全性
- **使用枚举**：为一组相关常量提供有意义的名称
- **使用命名空间**：组织相关类型和功能

### 5.3 代码风格

- **使用 PascalCase**：命名类、接口、类型别名
- **使用 camelCase**：命名函数、变量、属性
- **使用 UPPER_SNAKE_CASE**：命名常量
- **使用下划线前缀**：命名私有成员
- **使用 JSDoc 注释**：为类型和函数添加文档

### 5.4 性能优化

- **使用类型断言**：在确知类型时使用，避免不必要的类型检查
- **使用 const 断言**：为字面量类型提供更精确的类型
- **使用类型守卫**：在运行时检查类型
- **避免过度泛型**：只在必要时使用泛型
- **使用模块导入**：避免全局命名空间污染

## 6. 实际应用示例

### 6.1 基本 TypeScript 示例

```typescript
 // src/index.ts
 // 类型定义
 interface User {
  id: number;
  name: string;
  email: string;
  age?: number; // 可选属性
 }
 // 函数定义
 function greet(user: User): string {
  return `Hello, ${user.name}!`;
 }
 // 类定义
 class UserService {
  private users: User[] = [];
  addUser(user: User): void {
  this.users.push(user);
  }
  getUserById(id: number): User | undefined {
  return this.users.find(user => user.id === id);
  }
  getAllUsers(): User[] {
  return this.users;
  }
 }
 // 使用示例
 const userService = new UserService();
 userService.addUser({
  id: 1,
  name: "John Doe",
  email: "john@example.com",
  age: 30
 }
 userService.addUser({
  id: 2,
  name: "Jane Smith",
  email: "jane@example.com"
 }
 const user = userService.getUserById(1);
 if (user) {
  console.log(greet(user));
 }
 console.log(userService.getAllUsers());
```

### 6.2 编译与运行

```bash
 # 编译
 tsc
 # 运行
 node dist/index.js
 # 或直接运行
 npx ts-node src/index.ts
```

### 6.3 与 JavaScript 集成

```typescript
// src/index.ts
// 导入 JavaScript 模块
import { calculateTotal } from './utils.js';
// 类型定义
interface Order {
  id: number;
  items: {
    name: string;
    price: number;
    quantity: number;
  }[];
}
// 使用 JavaScript 函数
const order: Order = {
  id: 1,
  items: [
    { name: 'Item 1', price: 10, quantity: 2 },
    { name: 'Item 2', price: 15, quantity: 1 },
  ],
};
const total = calculateTotal(order.items);
console.log(`Order total: $${total}`);
```

```javascript
// src/utils.js
// JavaScript 函数
export function calculateTotal(items) {
  return items.reduce((total, item) => {
    return total + item.price * item.quantity;
  }, 0);
}
```

## 7. 常见问题与解决方案

### 7.1 编译错误

| 错误                                        | 原因           | 解决方案                                 |
| :------------------------------------------ | :------------- | :--------------------------------------- |
| **Type 'X' is not assignable to type 'Y'**  | 类型不匹配     | 检查变量类型，确保类型一致               |
| **Property 'X' does not exist on type 'Y'** | 属性不存在     | 检查对象结构，确保属性存在或使用可选属性 |
| **Cannot find name 'X'**                    | 变量未定义     | 检查变量是否已声明，或添加类型定义       |
| **Module 'X' has no exported member 'Y'**   | 模块导出不存在 | 检查模块导出，确保导出名称正确           |
| **Cannot find module 'X'**                  | 模块未找到     | 检查模块路径，确保模块已安装             |

### 7.2 类型定义问题

| 问题             | 原因                 | 解决方案                            |
| :--------------- | :------------------- | :---------------------------------- |
| **缺少类型定义** | 第三方库没有类型定义 | 安装 @types/ 包或创建自定义类型定义 |
| **类型冲突**     | 多个类型定义冲突     | 检查类型定义文件，解决冲突          |
| **类型过于严格** | 类型定义过于严格     | 使用类型断言或调整类型定义          |
| **类型不完整**   | 类型定义不完整       | 扩展类型定义或使用接口继承          |

### 7.3 性能问题

| 问题           | 原因               | 解决方案                                 |
| :------------- | :----------------- | :--------------------------------------- |
| **编译速度慢** | 项目过大或配置不当 | 优化 tsconfig.json，使用增量编译         |
| **类型检查慢** | 复杂类型或循环依赖 | 简化类型定义，避免循环依赖               |
| **运行时性能** | 编译输出效率低     | 优化 TypeScript 代码，使用适当的编译选项 |

### 7.4 工具链问题

| 问题                 | 原因     | 解决方案                              |
| :------------------- | :------- | :------------------------------------ |
| **与 Babel 集成**    | 配置冲突 | 使用 @babel/preset-typescript         |
| **与 Webpack 集成**  | 配置不当 | 正确配置 ts-loader 或 babel-loader    |
| **与 ESLint 集成**   | 规则冲突 | 使用 @typescript-eslint/eslint-plugin |
| **与 Prettier 集成** | 格式冲突 | 配置 Prettier 与 ESLint 配合          |

### 8.2 书籍

- **《TypeScript 实战》** - 梁宵
- **《深入理解 TypeScript》** - Basarat Ali Syed
- **《TypeScript 编程》** - Boris Cherny
- **《TypeScript 权威指南》** - 张容铭

### 8.3 在线教程

- **TypeScript 官方教程**: [https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html)
- **MDN TypeScript 教程**: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/TypeScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/TypeScript)
- **TypeScript Deep Dive**: [https://basarat.gitbook.io/typescript/](https://basarat.gitbook.io/typescript/)
- **freeCodeCamp TypeScript 教程**: [https://www.freecodecamp.org/learn/typescript/](https://www.freecodecamp.org/learn/typescript/)

### 8.4 社区与论坛

- **TypeScript 社区**: [https://github.com/microsoft/TypeScript/discussions](https://github.com/microsoft/TypeScript/discussions)
- **Stack Overflow TypeScript**: [https://stackoverflow.com/questions/tagged/typescript](https://stackoverflow.com/questions/tagged/typescript)
- **Reddit r/typescript**: [https://www.reddit.com/r/typescript/](https://www.reddit.com/r/typescript/)
- **TypeScript 中文社区**: [https://www.typescriptlang.cn/](https://www.typescriptlang.cn/)

## 9. 总结

TypeScript 是一种强大的编程语言，它通过添加静态类型系统和其他高级特性，使 JavaScript 开发更加安全、高效和可维护。通过正确配置环境、使用最佳实践和利用丰富的工具链，开发者可以充分发挥 TypeScript 的优势，构建高质量的应用程序。

### 9.1 关键要点

- **类型安全**: TypeScript 的核心价值在于提供静态类型检查，减少运行时错误
- **渐进式 adoption**: 可以与 JavaScript 无缝集成，便于现有项目逐步迁移
- **强大的工具链**: 丰富的工具和 IDE 支持，提高开发效率
- **现代语言特性**: 支持最新的 ECMAScript 特性，保持代码现代化
- **大型项目支持**: 适合构建和维护大型应用程序

### 9.2 学习建议

- **从基础开始**: 学习 TypeScript 的基本类型和语法
- **实践项目**: 通过实际项目练习 TypeScript
- **阅读文档**: 参考官方文档和最佳实践
- **参与社区**: 加入 TypeScript 社区，学习和分享经验
- **持续学习**: 关注 TypeScript 的更新和新特性
  TypeScript 已经成为现代前端和 Node.js 开发的重要工具，掌握 TypeScript 可以帮助开发者构建更加可靠、可维护的应用程序，提高开发效率和代码质量。

## 延伸阅读

- [JavaScript](javascript/overview)
- [Vue3](vue3/overview)

---

## 5.0 const 类型参数

**基本写法：const 泛型参数**
`function <名><const T extends <约束>>(<参数>: T)`
```typescript
// 推断字面量类型而非放宽
function pickFirst<const T>(arr: readonly T[]): T {
  return arr[0];
}
const r = pickFirst(["red", "green"]); // "red" | "green"
```

---

**基本写法：const 配合元组**
`<const T extends readonly string[]>`
```typescript
// 保留元组字面量
function define<const T extends readonly string[]>(routes: T): T {
  return routes;
}
const c = define(["/home", "/about"]); // readonly ["/home", "/about"]
```

---

## 5.0 satisfies 操作符

**基本写法：satisfies 校验不放宽**
`const <变量> = <值> satisfies <类型>`
```typescript
// 校验符合类型，保留具体字面量推断
const palette = {
  red: "#f00",
  green: [0, 255, 0],
} satisfies Record<string, string | number[]>;
palette.red;   // string（具体）
palette.green; // number[]
```

---

**基本写法：satisfies 与 as 区别**
`<值> satisfies <类型>`
```typescript
// as 断言可能撒谎，satisfies 强制校验
const m = { a: 1 } satisfies Record<"a", number>;
// const m = { a: 1 } satisfies Record<"a", string>; // 报错
```

---

## 5.0 新版装饰器

**基本写法：标准装饰器**
`@<装饰器> <类成员>`
```typescript
// 符合 TC39 Stage 3，无需 experimentalDecorators
function log(target: Function, ctx: ClassMethodDecoratorContext) {
  return function (this: unknown, ...args: unknown[]) {
    console.log(ctx.name, args);
    return target.apply(this, args);
  };
}
class S { @log greet() { return "hi"; } }
```

---

## 5.2 using 声明

**基本写法：同步资源管理**
`using <变量> = <带 Symbol.dispose>`
```typescript
// 离开作用域自动释放
function read() {
  using f = openFile("./a.txt");
  // 作用域结束调用 [Symbol.dispose]
}
```

---

**基本写法：异步资源管理**
`await using <变量> = <带 Symbol.asyncDispose>`
```typescript
// 异步自动清理
async function run() {
  await using conn = await db.connect();
  // 自动 await [Symbol.asyncDispose]
}
```

---

## 5.3 switch(true) 收窄

**基本写法：switch(true) 类型收窄**
`switch (true) { case <条件>: ... }`
```typescript
// 每个 case 体内自动收窄
function desc(v: unknown) {
  switch (true) {
    case typeof v === "string": return v.toUpperCase();
    case typeof v === "number": return v.toFixed(2);
    default: return "unknown";
  }
}
```

---

## 5.4 NoInfer 工具类型

**基本写法：阻止推断**
`NoInfer<<T>>`
```typescript
// 不从该位置推断 T，仅校验
function withDefault<T>(v: T | undefined, fb: NoInfer<T>): T {
  return v ?? fb;
}
const r = withDefault("hi", "x"); // T = string
// withDefault("hi", 42); // 报错：number 不能赋给 string
```

---

## 5.4 闭包保留收窄

**基本写法：闭包内保留 narrowing**
`const <fn> = () => <使用收窄变量>`
```typescript
// 5.4 修复闭包内类型丢失
function fn(v: string | null) {
  if (v === null) return;
  const cb = () => v.toUpperCase(); // v 已收窄为 string
  return cb();
}
```

---

## 5.5 推断类型谓词

**基本写法：自动推断 is**
`function <f>(<x>): <TypePredicate>`
```typescript
// 返回布尔值自动推断为类型谓词
const isString = (x: unknown) => typeof x === "string";
const arr = [1, "a"].filter(isString); // string[]
```

---

## 5.6 离散联合与迭代器

**基本写法：离散联合类型**
`type <名> = { ... } | { ... }`
```typescript
// 成员间无公共字段时更严格检查
type A = { kind: "a"; x: number };
type B = { kind: "b"; y: string };
type U = A | B;
```

---

**基本写法：Iterator Helpers 类型**
`<iterator>.map(<fn>).filter(<fn>)`
```typescript
// 内置 Iterator 类型支持链式
function* gen() { yield 1; yield 2; }
const r = gen().map(x => x * 2).filter(x => x > 2).toArray(); // [4]
```

---

## 5.9 import defer 与 node20

**基本写法：延迟导入**
`import defer * as <名> from "<模块>"`
```typescript
// 首次使用时才求值
import defer * as lib from "./heavy";
// 用到 lib 时才执行模块
export function use() { return lib.foo(); }
```

---

**基本写法：node20 模块解析**
`"moduleResolution": "node20"`
```json
{
  "compilerOptions": {
    "module": "node20",
    "moduleResolution": "node20"
  }
}
```

---

## 装饰器上下文

**基本写法：装饰器上下文对象**
`<ctx>: ClassMethodDecoratorContext`
```typescript
// 上下文提供 name/kind/addInitializer 等
function bound(target: Function, ctx: ClassMethodDecoratorContext) {
  ctx.addInitializer(function (this: unknown) {
    (this as Record<string, unknown>)[ctx.name as string] =
      target.bind(this);
  });
}
```

---

## satisfies + const 组合

**基本写法：校验且保留字面量**
`<值> satisfies <类型>` + `function f<const T>`
```typescript
// 配置对象校验且保留字面量联合
function config<const T extends Record<string, string>>(c: T): T { return c; }
const c = config({
  home: "/",
  api: "/api",
} satisfies Record<string, string>);
c.home; // "/" 字面量
```

---
