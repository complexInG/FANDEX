---
order: 10
title: bun 模块文档合集
module: 'bun'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-29'
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

<!-- ============ 文档分隔线：051-bun/004-AdvancedRoadmap.md ============ -->

## 0. 你现在在哪里（先读这里）

> 学习目标：对照进阶路线，明确接下来三站要学什么、为什么按这个顺序学、每站学到什么程度算过关。

前三篇文档带你完成了 Bun 的入门闭环：认识这个"全家桶"运行时（001）、
用 bun init/add/test 跑起项目（002）、用内置服务器与 SQL 写出可运行的后端（003）。
到这里，你已经能用 Bun 完成从脚本到服务的完整开发。

本篇是通往精通阶段的路线图：把剩余的核心能力拆成三站。每一站给出
"要解决的问题 → 核心 API 清单 → 最小示例 → 常见陷阱 → 过关自检"，
后续版本会把每一站展开为独立文档（编号紧接本篇）。

## 1. 进阶路线总览

| 站点 | 主题 | 解决的问题 | 核心能力 |
| --- | --- | --- | --- |
| 第四站 | 包管理与工作区 | 依赖怎么管：安装、锁文件与 monorepo | bun install、bun.lock、workspaces |
| 第五站 | 内置测试与基准 | 质量怎么保：零配置的测试体系 | bun test、mock、覆盖率、基准 |
| 第六站 | WebSocket 与前端开发服务器 | 实时与一体化：从后端到全栈 | Bun.serve websocket、routes、HTML imports |

三站的关系：第四站让项目"装得快、装得稳"，第五站让代码"改得起"，
第六站把能力从后端扩展到实时通信与前端一体化。按顺序学，收获最大。

## 2. 第四站：包管理与工作区

Bun 的包管理器以快著称，这一站要建立可复现的依赖管理习惯。

### 2.1 为什么快

| 环节 | npm | bun install |
| --- | --- | --- |
| 下载 | 串行为主，包级缓存 | 全局二进制缓存 + 并行下载 |
| 解压 | 每项目解压全量文件 | 硬链接复用全局缓存 |
| 实现 | JavaScript | 原生（Zig）实现 |

**讲解：** 快不是魔法，而是"全局缓存 + 硬链接 + 原生实现"三件事。
理解了这一点，就能解释为什么 `bun install` 在 CI 冷启动时收益最大。

### 2.2 锁文件与 CI

```bash
# bun.lock 是文本格式：可评审、可合并，告别二进制锁文件冲突
git add bun.lock

# CI 中锁死依赖，杜绝"本地能装，流水线装了新版本"
bun install --frozen-lockfile
```

### 2.3 workspaces 最小 monorepo

```json
// 根 package.json
{
  "name": "my-monorepo",
  "workspaces": ["packages/*"]
}
```

```json
// packages/web/package.json —— 用 workspace:* 引用本地包
{
  "name": "web",
  "dependencies": {
    "@my/shared": "workspace:*"
  }
}
```

**讲解：** `bun install` 会把 `packages/shared` 链接进 `packages/web` 的
node_modules；`bun run --filter '<name>' <script>` 可以按包名执行脚本。
这就是"多包一仓"的最小骨架，pnpm workspace 的用户可以无缝理解。

### 2.4 生命周期脚本安全

Bun 默认不执行依赖包的 `postinstall` 等生命周期脚本——这是供应链安全的关键设计。
需要执行脚本的原生包（如 esbuild、sharp）要显式加进白名单：

```json
{
  "trustedDependencies": ["esbuild", "sharp"]
}
```

### 2.5 常见陷阱

- 忘记提交 bun.lock：队友与 CI 各装各的版本。
- 用 npm 的思维频繁 `bun pm cache clean`：全局缓存正是速度来源，清它等于自废武功。
- 白名单一开一大片：`trustedDependencies` 应保持最小集合。

### 2.6 过关自检

1. 能说出 bun install 快的三个来源。
2. CI 里会配合 bun.lock 使用 `--frozen-lockfile`。
3. 手工搭过一个两个包的 workspace 并互相引用。

## 3. 第五站：内置测试与基准

`bun test` 让测试零配置起步。

### 3.1 测试骨架

```ts
// math.test.ts —— 命名约定：*.test.ts 会被 bun test 自动发现
import { describe, it, expect } from "bun:test";
import { add } from "./math";

describe("add", () => {
  it("两数相加", () => {
    expect(add(1, 2)).toBe(3);
  });

  it("异步也没问题", async () => {
    expect(await Promise.resolve(42)).toBe(42);
  });
});
```

**讲解：** API 与 Jest 高度兼容（describe/it/expect/matcher 大表通用），
存量 Jest 项目基本"换个命令就能跑"。差异集中在模块 mock 上：
Bun 用 `mock.module()`，迁移时重点核对。

### 3.2 mock 三件套

```ts
import { test, expect, mock } from "bun:test";

// 函数 mock：记录调用与返回值
const fetchName = mock(() => "洛天依");

// 模块 mock：替换整个依赖模块
mock.module("./config", () => ({ API_URL: "http://test.local" }));

// 计时器 mock：不真等 3 秒
test("重试逻辑", () => {
  // 配合 fake timers 控制时间流逝（以官方文档为准）
});
```

### 3.3 覆盖率与基准

```bash
bun test --coverage            # 覆盖率报告
bun test --update-snapshots    # 快照更新
```

基准测试也是内置能力（细节以官方文档为准），写法仍是"定义用例、
对比实现"，适合给"两个 JSON 解析方案谁快"这类问题一个数字答案。

### 3.4 常见陷阱

- 从 `bun:test` 之外导入 test API（如混入 vitest 的 import），运行时直接报错。
- Jest 的 `jest.mock` 提升（hoisting）行为与 `mock.module` 不同，迁移时逐个验证。
- 快照测试滥用：把易变的大对象做快照，每次都 `--update`，快照形同虚设。

### 3.5 过关自检

1. 零配置给一个现有模块补上测试并跑绿。
2. 能说出 Jest 与 bun test 在模块 mock 上的差异。
3. CI 里有一条 `bun test` 步骤（oven-sh/setup-bun 安装）。

## 4. 第六站：WebSocket 与前端开发服务器

Bun.serve 原生集成 WebSocket 与前端开发能力，一个进程跑实时全栈。

### 4.1 最小聊天室

```ts
// server.ts
Bun.serve({
  port: 3000,
  routes: {                       // Bun 1.3 的路由表：路径直接映射
    "/": () => new Response(Bun.file("./chat.html")),
  },
  websocket: {                    // 原生 WebSocket 处理器
    open(ws) { ws.subscribe("chat"); },
    message(ws, msg) {
      ws.publish("chat", `说: ${msg}`);   // 频道广播
    },
    close(ws) { ws.unsubscribe("chat"); },
  },
  fetch(req, server) {
    if (server.upgrade(req)) return;      // 升级为 WebSocket
    return new Response("预期 WebSocket 连接");
  },
});
```

**讲解：** `subscribe/publish` 是内置的频道广播：不需要自己维护连接列表、
不需要引入 ws 库。`routes` 让"路径 → 响应"一行一条，通配符兜底动态路径。

### 4.2 前端开发服务器与打包

Bun 1.3 起内置前端开发服务器：HTML 即入口（HTML imports，
`<script src="./app.ts">` 直接写 TypeScript）、静态资源自动处理、
保存即热重载；上线用 `Bun.build`（或 `bun build` 命令）产出打包产物。
细节以官方文档为准。

### 4.3 常见陷阱

- 忘记在 fetch 里调用 `server.upgrade(req)`，WebSocket 永远握不上手。
- publish 前没有 subscribe：消息静默丢失，排查时先确认 open 里订阅了频道。
- 生产环境把 WebSocket 直接暴露公网：建议前置 Nginx 做终止与限流。

### 4.4 过关自检

1. 能写出 20 行以内的可广播聊天室。
2. 能解释 upgrade 与 subscribe/publish 的关系。
3. 用 routes 组织过多页面/接口并用热重载开发过前端页面。

## 5. 学习建议

1. 顺序学，不跳站：第四站的锁文件与 workspaces 是后续所有项目的地基。
2. 每站一个小产出：迁移一个现有仓库到 bun install、给 003 的服务补测试、
   部署一个 WebSocket 聊天室，比通读文档有效得多。
3. 版本跟进：Bun 迭代很快，依赖 bun.lock 锁定版本，升级前跑一遍测试。

## 小结与延伸

- 进阶三站：依赖管理 → 测试与基准 → 实时与一体化，对应从"能用"到"能交付"的跨越。
- 每一站的展开文档将陆续补充在本模块中，编号紧接本篇（005 起）。
- 官方资源：bun.sh/docs（运行时与 API）、bun.sh/blog（版本发布说明）。

<!-- ============ 文档分隔线：051-bun/005-BunPackageManagerWorkspaces.md ============ -->

# 包管理与工作区

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- 安装速度来源与 npm/pnpm 对比
- bun.lock 与 --frozen-lockfile
- workspaces 最小 monorepo
- 生命周期脚本安全策略
- bun pm 常用命令

<!-- ============ 文档分隔线：051-bun/006-BunTestBench.md ============ -->

# 内置测试与基准

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- bun test 骨架与 matcher
- Jest 兼容与迁移差异
- mock 三件套
- 快照与覆盖率
- CI 接入

<!-- ============ 文档分隔线：051-bun/007-BunWebSocketFrontendDev.md ============ -->

# WebSocket 与前端开发服务器

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- websocket 处理器与频道广播
- 最小聊天室实战
- routes 路由表与 cookies()
- HTML imports 与热重载
- 生产部署建议
