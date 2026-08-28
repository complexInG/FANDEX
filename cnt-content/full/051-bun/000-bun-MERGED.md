---
order: 10
title: bun 模块文档合集
module: 'bun'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：051-bun/001-BunOverview.md ============ -->


## 0. 两分钟运行第一个脚本（先读这里）

> 学习目标：安装 Bun 并运行 TypeScript，体验"启动快到感觉不到"。

```bash
# Windows（PowerShell）
powershell -c "irm bun.sh/install.ps1 | iex"
```

```typescript
// hello.ts
const start = performance.now()
console.log("你好，Bun！")
console.log(`启动耗时：${(performance.now() - start).toFixed(1)}ms`)
```

```bash
bun hello.ts
```

**讲解：**

1. `bun hello.ts` 直接执行 TypeScript，无需安装 ts-node 或先编译。
2. `performance.now()` 返回毫秒时间戳，前后相减得到运行耗时——Bun 的冷启动通常在十几毫秒内。
3. 同样代码用 `node hello.js` 对比，能直观感受到运行时差异。

## 1. Bun 是什么

Bun 是一个由 Zig 编写的 JavaScript/TypeScript 运行时与工具链，2022 年发布，目标是"一个工具替代 Node.js + npm + webpack + jest"：

- 运行时：兼容 Node.js API，比 Node 冷启动更快；
- 包管理器：`bun install` 比 npm/pnpm 快数倍，可直接读取 npm 包；
- 打包器：内置打包与压缩（对标 webpack/esbuild）；
- 测试器：内置 Jest 风格测试框架；
- 运行器：`bunx` 对标 `npx`。

### 1.1 版本现状（2026-08）

- Bun 1.3.x 为当前稳定版（1.3.14，2026-05）；1.3 引入零配置前端开发、统一 SQL API、内置 Redis 客户端。
- 兼容性：Node.js 项目大多可直接用 `bun run` 启动；Windows 支持已成熟。

## 2. 与 Node.js 对比

| 维度 | Node.js | Bun |
| --- | --- | --- |
| 语言 | C++ | Zig |
| 冷启动 | 较慢 | 极快 |
| 包管理 | npm/pnpm/yarn | bun（也兼容 npm 仓库） |
| 测试 | 需额外安装 Jest/Vitest | 内置 |
| 打包 | 需 webpack/Vite | 内置 |
| 兼容性 | 标准 | 兼容 Node API，少数边缘差异 |

## 3. 内置命令速览

```bash
bun run script.ts   # 运行脚本（兼容 package.json scripts）
bun install         # 安装依赖
bun add hono        # 添加依赖
bun test            # 运行测试
bun build ./src/index.ts --outdir dist  # 打包
bunx cowsay "hi"    # 临时执行 npm 包
```

**讲解：**

1. `bun run` 既能跑 TS 文件，也能跑 `package.json` 里的 scripts（如 `bun run dev`）。
2. `bun add` 与 npm 的 `npm install 包` 等价，生成的还是 `package.json` + 锁文件。
3. `bun build` 把入口文件连同依赖打包成浏览器可用或服务器可用的产物。

## 4. 动手试试

1. 用 `bun init` 初始化一个项目，观察生成的 `package.json` 与 `index.ts`。
2. 写一个斐波那契计算脚本，分别用 `node` 与 `bun` 运行 10 次，记录平均耗时。
3. 用 `bunx` 运行一个 npm CLI 工具（如 `bunx tsc --version`）。

## 5. 一句话记住

> Bun 把运行时、包管理、打包、测试装进一个二进制：`bun run` 一条命令，快是它的名片。



<!-- ============ 文档分隔线：051-bun/002-BunQuickStart.md ============ -->


## 0. 一句话理解

> Bun 的项目还是 `package.json` + `node_modules` 那套（生态兼容），只是执行更快、命令更短、测试内置。

## 1. 初始化项目

```bash
bun init -y
```

**讲解：**

1. `bun init` 生成 `package.json`、`index.ts`、`tsconfig.json` 与 `.gitignore`。
2. `-y` 跳过交互提问；生成的 `index.ts` 里有一个可运行的 `server` 示例。
3. 对比 `npm init`：多出了开箱即用的 TypeScript 配置，无需再装 `typescript` 与 `ts-node`。

## 2. 管理依赖

```bash
bun add hono
bun add -d @types/bun
bun remove hono
```

**讲解：**

1. `bun add` 安装运行时依赖，`-d` 安装开发依赖，`bun remove` 卸载。
2. 锁文件是 `bun.lock`（也兼容 `bun.lockb`），提交 git 保证环境一致。
3. 安装速度快的原理：并行下载 + 全局内容寻址缓存，同一版本只存一份。

## 3. 内置测试框架

```typescript
// math.ts
export function factorial(n: number): number {
  if (n < 0) throw new Error("负数没有阶乘")
  let result = 1
  for (let i = 2; i <= n; i++) result *= i
  return result
}
```

```typescript
// math.test.ts
import { describe, expect, test } from "bun:test"
import { factorial } from "./math"

describe("factorial", () => {
  test("0 的阶乘是 1", () => {
    expect(factorial(0)).toBe(1)
  })

  test("5 的阶乘是 120", () => {
    expect(factorial(5)).toBe(120)
  })

  test("负数抛错", () => {
    expect(() => factorial(-1)).toThrow("负数")
  })
})
```

```bash
bun test
```

**讲解：**

1. `bun:test` 提供与 Jest 几乎相同的 API：`describe/test/expect`。
2. 测试文件命名 `*.test.ts` 会被自动发现，不需要配置文件。
3. 三个用例分别覆盖：边界（0）、正常（5）、异常（负数）——这是测试设计的标准三分法。
4. `bun test` 默认并发运行测试文件，整体速度远快于 Jest。

## 4. scripts 与任务

```json
// package.json
{
  "name": "demo",
  "type": "module",
  "scripts": {
    "dev": "bun --watch index.ts",
    "start": "bun index.ts",
    "test": "bun test",
    "build": "bun build ./index.ts --outdir dist --target bun"
  }
}
```

**讲解：**

1. `bun --watch index.ts` 监听文件变化自动重启，相当于 Node 生态的 nodemon。
2. `bun build --target bun` 打出专门给 Bun 运行的产物，还可以用 `--target browser` 或 `--target node`。
3. `type: "module"` 让项目默认使用 ESM 语法。

## 5. 动手试试

1. 给 `factorial` 加 `1 的阶乘` 测试并运行 `bun test`。
2. 用 `bun add` 安装 `zod`，写一个校验邮箱的小函数与对应测试。
3. 用 `bun build` 打包，观察产物文件与体积。

## 6. 一句话记住

> Bun 不改变 Node 的项目形态，只把安装、运行、测试、打包四件事变快变短；测试从第一天就写，成本几乎为零。



<!-- ============ 文档分隔线：051-bun/003-BunBuiltinServerSQL.md ============ -->


## 0. 一句话理解

> Bun 把服务器、SQL、Redis 客户端都"内置"了：`Bun.serve` 起服务、`Bun.sql` 查数据库，少装一半依赖。

## 1. Bun.serve：HTTP 服务器

```typescript
// server.ts
const server = Bun.serve({
  port: 3000,
  async fetch(request) {
    const url = new URL(request.url)

    if (url.pathname === "/" ) {
      return new Response("你好，Bun!")
    }

    if (url.pathname === "/api/time") {
      return Response.json({ time: new Date().toISOString() })
    }

    return new Response("Not Found", { status: 404 })
  }
})

console.log(`服务已启动: http://localhost:${server.port}`)
```

**讲解：**

1. `Bun.serve({ fetch })` 使用 Web 标准 Request/Response，无需 Express 依赖。
2. `new URL(request.url)` 解析路径，按 `url.pathname` 分发路由。
3. `Response.json(...)` 是 Web 标准便捷方法，自动设置 `Content-Type: application/json`。
4. 最后一行兜底返回 404，避免未知路径静默返回 200。

## 2. Bun.sql：内置 SQLite

```typescript
// db.ts
import { Database } from "bun:sqlite"

const db = new Database("app.db")

db.run(`
  CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER DEFAULT 0
  )
`)

// 插入
const insert = db.query("INSERT INTO todos (title) VALUES (?) RETURNING *")
const created = insert.get("学 Bun SQL")

// 查询
const all = db.query("SELECT * FROM todos ORDER BY id DESC").all()

console.log("创建:", created)
console.log("全部:", all)
```

**讲解：**

1. `bun:sqlite` 是内置 SQLite 驱动，`new Database("app.db")` 打开（没有则创建）数据库文件。
2. `db.run` 执行建表等无返回语句；`db.query(...)` 预编译 SQL，`?` 是参数占位符，防止 SQL 注入。
3. `insert.get(...)` 执行插入并返回第一行（`RETURNING *` 返回新记录），`.all()` 返回所有行。
4. 参数化查询是铁律：永远不要用字符串拼接拼 SQL。

## 3. 组合：带数据库的 API

```typescript
// api.ts
import { Database } from "bun:sqlite"

const db = new Database("app.db")

db.run(`
  CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER DEFAULT 0
  )
`)

Bun.serve({
  port: 3000,
  async fetch(request) {
    const url = new URL(request.url)

    if (request.method === "POST" && url.pathname === "/todos") {
      const body = await request.json()
      const result = db
        .query("INSERT INTO todos (title) VALUES (?) RETURNING *")
        .get(body.title)
      return Response.json(result, { status: 201 })
    }

    if (request.method === "GET" && url.pathname === "/todos") {
      const rows = db.query("SELECT * FROM todos").all()
      return Response.json(rows)
    }

    return new Response("Not Found", { status: 404 })
  }
})
```

**讲解：**

1. 请求方法 + 路径组合成路由：`POST /todos` 创建，`GET /todos` 列表。
2. `await request.json()` 解析请求体，然后参数化插入数据库。
3. 这 40 行代码就是一个可运行的待办 API：无框架、无 ORM、无额外依赖。
4. 进阶：多表关联、迁移、连接池等场景再引入 Prisma/Drizzle 等 ORM，简单场景内置 SQLite 足够。

## 4. 内置 Redis 客户端

```typescript
import { Redis } from "bun"

const redis = new Redis("redis://localhost:6379")

await redis.set("counter", 1)
await redis.incr("counter")
const value = await redis.get("counter")

console.log(value) // "2"
```

**讲解：**

1. Bun 1.3+ 内置 Redis 客户端（`bun` 模块导出），无需安装 `ioredis` 等第三方包。
2. API 风格与 ioredis 高度一致：`set/get/incr` 都是 Promise，可用 `await`。
3. 内存缓存、分布式锁、限流等场景可直接使用；连接串支持 Redis 标准 URL。

## 5. 动手试试

1. 给待办 API 增加 `DELETE /todos/:id`（解析路径参数并 `db.run("DELETE ...")`）。
2. 用 `bun:sqlite` 做一个"点击计数"页面：每次访问 `/counter` 把数字加 1 并返回。
3. 启动本地 Redis（Docker），用内置客户端写入并读取一个字符串。

## 6. 一句话记住

> Bun.serve 起服务、bun:sqlite 存数据、内置 Redis 做缓存——小项目一个运行时全搞定，SQL 永远用参数占位符。
