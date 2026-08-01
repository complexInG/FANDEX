---
order: 540
title: Node.js 与 TypeScript 工程化
module: typescript
category: '009-typescript'
difficulty: intermediate
description: 一份开箱即用的 Node.js + TypeScript 工程骨架：目录结构、tsconfig 双配置、开发与构建脚本、常见坑位。
author: fanquanpp
created: '2026-08-02'
updated: '2026-08-02'
related:
  - 'typescript/039-TypeScriptEngineeringConfig'
  - 'typescript/048-TsconfigStrictMode'
prerequisites:
  - 'typescript/001-TypeScriptOverviewEnvSetup'
quiz:
  - type: choice
    question: Node 端开发与构建为什么要用两套 tsconfig？
    options:
      - 因为编译器有 bug
      - 开发要快（不产出文件），构建要严格（产出 dist）
      - 因为 Node 不认识 tsconfig
      - 两套配置可以完全一样
    answer: 1
    explanation: tsconfig.base 共享编译选项，tsconfig.dev 用 noEmit 提速，tsconfig.build 产出 dist。
  - type: fill
    question: Node 的 ESM 模式下，tsconfig 的 module 通常设置为____。
    answer: NodeNext
    hint: NodeNext 让 Node 按文件扩展名区分 ESM/CJS。
references:
  - type: documentation
    authors:
      - Node.js Contributors
    year: 2026
    title: Node.js 模块：ESM 与 CJS
    venue: nodejs.org
    url: https://nodejs.org/api/esm.html
    accessedDate: '2026-08-02'
  - type: documentation
    authors:
      - TypeScript Team
    year: 2026
    title: TypeScript 模块解析：NodeNext
    venue: typescriptlang.org
    url: https://www.typescriptlang.org/docs/handbook/modules/reference.html
    accessedDate: '2026-08-02'
etymology:
  - term: 工程化
    english: Engineering Setup
    origin: 把"能跑"的脚本升级为"可维护、可测试、可部署"的项目结构，强调工程而非手艺。
estimatedReadingTime: 7
lastReviewed: '2026-08-02'
reviewer: fanquanpp
---

## 一句话理解

Node.js + TypeScript 工程化 = 一套固定目录 + 两套 tsconfig + 三个脚本命令，
让开发（快速热跑）、构建（产出干净 dist）、部署（只带 dist）各司其职。

## 目录结构

```text
my-service/
├── src/                 # 源码（TS）
│   ├── index.ts         # 入口
│   ├── config.ts
│   └── routes/
├── dist/                # 构建产物（JS，部署用）
├── test/                # 测试
├── package.json
├── tsconfig.base.json
├── tsconfig.dev.json
└── tsconfig.build.json
```

## tsconfig：一个基础 + 两个场景

```json
// tsconfig.base.json：共享编译选项
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "outDir": "dist",
    "rootDir": "src",
    "sourceMap": true,
    "declaration": true,
    "skipLibCheck": true
  },
  "include": ["src"]
}
```

```json
// tsconfig.dev.json：开发期只做类型检查，不产出文件
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "noEmit": true
  }
}
```

```json
// tsconfig.build.json：构建期产出 dist
{
  "extends": "./tsconfig.base.json"
}
```

## 三个脚本命令

```json
{
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc -p tsconfig.build.json",
    "start": "node dist/index.js",
    "typecheck": "tsc -p tsconfig.dev.json"
  }
}
```

```typescript
// src/index.ts：最小示例
import { createServer } from 'node:http';

const port = Number(process.env.PORT ?? 3000);

createServer((req, res) => {
  res.writeHead(200, { 'content-type': 'text/plain; charset=utf-8' });
  res.end('hello');
}).listen(port, () => {
  console.log(`listening on ${port}`);
});
```

开发用 `pnpm dev`（tsx 直接跑 TS），提交前 `pnpm typecheck`，
发布时 `pnpm build && pnpm start`。

## 常见误区

| 误区 | 真相 |
| --- | --- |
| 生产环境直接跑 ts-node/tsx | 部署应使用构建后的 JS，避免运行时依赖 TS 编译 |
| module 随意设成 CommonJS | ESM 项目应使用 NodeNext，让 Node 正确解析 `.js` 导入 |
| 导入写 `./config` 不写扩展名 | NodeNext 下 ESM 要求显式 `.js`（TS 源文件里写 `./config.js`） |
| dist 里混入测试文件 | `rootDir: src` + include 只编译 src，测试放 test/ 不参与构建 |

## 小结

这套骨架的核心是"开发快、构建干净、类型严格"：
`tsx` 负责开发体验，`tsc` 负责产物质量，双 tsconfig 让两件事互不干扰。
继续深化可看 [tsconfig 严格模式](/FANDEX/typescript/048-TsconfigStrictMode/) 与
[编译与性能优化](/FANDEX/typescript/043-TypeScriptCompilePerformanceOptimization/)。
