---
order: 10
title: deno 模块文档合集
module: 'deno'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-29'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：050-deno/001-DenoOverview.md ============ -->

## 0. 两分钟运行第一个脚本（先读这里）

> 学习目标：安装 Deno 并运行一个 TypeScript 脚本，感受"无需配置文件"的开发体验。

```bash
# Windows（PowerShell）
irm https://deno.land/install.ps1 | iex

# 或通过包管理器
winget install DenoLand.Deno
```

```typescript
// hello.ts
const name = Deno.args[0] ?? "世界"
console.log(`你好，${name}！`)
```

```bash
deno run hello.ts 小明
```

**讲解：**

1. `Deno.args` 是命令行参数数组，`?? "世界"` 在未传参时给默认值。
2. 不需要 `package.json`、不需要 `tsconfig.json`、不需要先编译——`deno run` 直接执行 TypeScript。
3. 输出 `你好，小明！`，第一个 Deno 程序完成。

## 1. Deno 是什么

Deno 是 Node.js 创始人 Ryan Dahl 于 2020 年发布的 JavaScript/TypeScript 运行时，由 Rust 编写。它的设计目标是修复 Node.js 的历史问题：

- 默认安全：脚本不能随意读文件、写网络，必须显式授权；
- 原生 TypeScript：不需要 ts-node、webpack；
- 去中心化依赖：直接用 URL 导入，或使用 JSR/npm 包；
- 内置工具链：格式化、测试、代码检查、打包全部内置。

### 1.1 版本现状（2026-08）

- Deno 2.7+ 为当前稳定版（2.7 于 2026-02 发布，引入 Temporal API、Windows ARM 支持与 npm overrides）。
- 2.x 兼容 npm 包与 Node.js 项目（`node:` 前缀导入），迁移成本已大幅降低。
- 配套平台：Deno Deploy 提供边缘部署、KV 存储与 Cron 定时任务。

## 2. 内置工具链

```bash
deno fmt            # 格式化代码
deno lint           # 代码检查
deno test           # 运行测试
deno compile hello.ts  # 编译成单个可执行文件
```

**讲解：**

1. `deno fmt` 与 `deno lint` 对标 Prettier/ESLint，零配置即用。
2. `deno test` 自动发现 `*_test.ts` 文件并运行，内置断言库。
3. `deno compile` 把脚本连同运行时打包成单文件可执行程序，适合分发 CLI 工具。

## 3. 与 Node.js 的对比

| 维度 | Node.js | Deno |
| --- | --- | --- |
| 类型支持 | 需 tsx/ts-node | 原生 TypeScript |
| 模块 | npm + CommonJS/ESM | URL/JSR/npm，标准 ESM |
| 权限 | 默认全开 | 默认全关，按需授权 |
| 配置 | package.json + 一堆工具 | 零配置起步 |
| 生态 | 全球最大 | 兼容 npm，原生生态快速增长 |

## 4. 动手试试

1. 修改 `hello.ts`，用 `Deno.readTextFile` 读取同目录的一个 txt 文件，运行后观察权限提示。
2. 运行 `deno fmt hello.ts` 看看格式化效果。
3. 用 `deno compile hello.ts` 生成可执行文件并运行它。

## 5. 一句话记住

> Deno = 原生 TypeScript + 默认安全的现代运行时；一个命令跑脚本，一条权限规则保护系统。

<!-- ============ 文档分隔线：050-deno/002-DenoQuickStart.md ============ -->

## 0. 一句话理解

> Deno 的依赖就是"网址或包名"：import 写在文件顶部，首次运行时自动下载缓存；测试就是 `Deno.test`，与业务代码放一起。

## 1. 导入第三方模块

```typescript
// 从 npm 导入（Deno 2.x 起推荐写法，带版本号）
import { Hono } from "npm:hono@4"

// 从 JSR 导入（Deno 官方包仓库）
import { camelCase } from "jsr:@std/text@1"

// 从 URL 直接导入（经典 Deno 风格）
import { serve } from "https://deno.land/std@0.224.0/http/server.ts"
```

**讲解：**

1. `npm:hono@4` 前缀表示"从 npm 拿包"，Deno 会解析其依赖树并缓存，不需要 `npm install`。
2. `jsr:@std/text` 是 Deno 官方标准库在 JSR 上的发布名，`@1` 表示主版本。
3. URL 导入是 Deno 1.x 的标志性写法，新项目建议优先 npm/JSR，并锁定版本号。

## 2. 标准库常用模块

```typescript
// format_date.ts
import { format } from "jsr:@std/datetime@0.225"

const now = new Date()
console.log(format(now, "yyyy-MM-dd HH:mm:ss"))
```

```typescript
// csv.ts：解析 CSV 并计算总和
import { parse } from "jsr:@std/csv@1"

const csvText = `name,score\n小明,90\n小红,85`
const rows = parse(csvText, { skipFirstRow: true })

let total = 0
for (const row of rows) {
  total += Number(row.score)
}
console.log("平均分：", total / rows.length)
```

**讲解：**

1. `@std/datetime` 的 `format` 用 `yyyy/MM/dd` 占位符格式化日期，`@std/csv` 的 `parse` 一行把 CSV 变成对象数组。
2. `skipFirstRow: true` 把第一行当作表头，`row.score` 直接按列名取值。
3. `Number(row.score)` 把字符串转数字；标准库覆盖了文件、路径、颜色、日志、测试等常用能力。

## 3. 内置测试框架

```typescript
// avg_test.ts
import { assertEquals } from "jsr:@std/assert@1"

export function average(scores: number[]): number {
  if (scores.length === 0) return 0
  return scores.reduce((a, b) => a + b, 0) / scores.length
}

Deno.test("average 计算平均值", () => {
  assertEquals(average([90, 85, 95]), 90)
})

Deno.test("average 空数组返回 0", () => {
  assertEquals(average([]), 0)
})
```

```bash
deno test
```

**讲解：**

1. `Deno.test("名字", 函数)` 定义一个测试用例，`assertEquals` 断言两个值相等。
2. 测试文件与业务代码同目录，文件名带 `_test.ts` 后缀即可被自动发现。
3. 空数组返回 0 的用例专门保护边界条件——写测试的入门标准就是"正常情况 + 边界情况"。

## 4. 项目配置文件（可选）

```json
// deno.json
{
  "tasks": {
    "dev": "deno run --watch main.ts",
    "test": "deno test"
  },
  "imports": {
    "@std/assert": "jsr:@std/assert@1"
  }
}
```

**讲解：**

1. `tasks` 相当于 npm scripts：`deno task dev` 运行开发任务，`--watch` 自动重启。
2. `imports` 是 import map：把 `@std/assert` 映射到具体版本，代码里写 `import { assertEquals } from "@std/assert"` 更干净。
3. deno.json 是可选文件，没有它 Deno 也能跑，但项目复杂后建议加上。

## 5. 动手试试

1. 写一个 `median`（中位数）函数，包含奇数长度与偶数长度两个测试用例。
2. 用 `@std/csv` 解析一份 10 行成绩单，输出及格率（>=60 的占比）。
3. 把 `average` 重构为从 CSV 读取分数再计算，运行 `deno test` 确认测试仍通过。

## 6. 一句话记住

> Deno 的开发节奏是"写文件 → import 带版本的包 → deno test/run"，工具链内置、测试内置，配置按需增加。

<!-- ============ 文档分隔线：050-deno/003-DenoPermissionsSecurity.md ============ -->

## 0. 一句话理解

> Deno 的默认状态是"什么都不能做"：读文件、写网络都要在运行命令里显式授权；权限最小化是 Deno 最重要的安全特性。

## 1. 权限报错体验

```typescript
// read_file.ts
const content = await Deno.readTextFile("secret.txt")
console.log(content)
```

```bash
deno run read_file.ts
```

**讲解：**

1. 直接运行会报错：`PermissionDenied: Requires read access to "secret.txt"`。
2. 这是"默认拒绝"的设计：即使脚本被恶意第三方依赖控制，它也无法悄悄读取你的文件。
3. 相比 Node.js 默认全开，Deno 把"要不要给权限"变成了每次运行时的显式决定。

## 2. 授权参数

```bash
# 只允许读当前目录
deno run --allow-read=. read_file.ts

# 只允许访问指定域名
deno run --allow-net=api.example.com fetch_data.ts

# 允许读写文件与网络（生产环境按需最小化，不要图省事用 --allow-all）
deno run --allow-read --allow-write --allow-net app.ts
```

**讲解：**

1. `--allow-read=.` 的 `=.` 表示只读当前目录，比无参数的全盘读取安全得多。
2. `--allow-net=域名` 限制网络请求只到指定主机，防止脚本外联未知服务器。
3. 权限可以叠加；`-A`（`--allow-all`）适合本地临时调试，生产环境禁止使用。

## 3. 敏感信息：密钥不进代码

```bash
# Windows PowerShell 设置环境变量
$env:DB_PASSWORD = "s3cr3t"

# 运行时显式授权读取环境变量
deno run --allow-env=DB_PASSWORD app.ts
```

```typescript
// app.ts
const password = Deno.env.get("DB_PASSWORD")
if (!password) {
  throw new Error("缺少 DB_PASSWORD 环境变量")
}
```

**讲解：**

1. `Deno.env.get` 读取环境变量，密钥放在环境变量或密钥管理服务（如 Vercel/云厂商 Secret Manager）里，绝不写进代码与 git。
2. `--allow-env=DB_PASSWORD` 只放行这一个变量，其他环境变量脚本读不到。
3. `if (!password) throw` 是"fail fast"：缺少必需配置时立即失败，而不是带着空密码运行。

## 4. 依赖供应链安全

```bash
deno install
deno check --all
deno audit
```

**讲解：**

1. `deno install` 根据 import 生成锁文件（deno.lock），锁定每个依赖的精确版本与校验和，后续安装一致复现。
2. `deno check --all` 对全项目做类型检查，错误在 CI 里暴露而不是运行时。
3. `deno audit` 扫描依赖漏洞（Deno 2.1+ 提供），类似 `npm audit`，应纳入 CI 流程。

## 5. 生产环境安全清单

- 用最小权限运行：只给 `--allow-net=你的域名`、`--allow-env=必需变量`；
- 容器内以非 root 用户运行，避免容器逃逸后获得 root；
- 密钥放 Secret Manager，轮换机制 + 审计日志；
- 依赖锁文件提交 git，CI 里跑 `deno audit` 与 `deno check`；
- 不信任任何第三方模块的权限请求：权限永远由你的 `deno run` 命令决定。

## 6. 动手试试

1. 写一个脚本读取系统临时目录（`Deno.env.get("TEMP")`），分别用 `--allow-env` 与不带参数运行，观察差异。
2. 用 `--allow-net=example.com` 访问 `https://example.com` 成功、再访问 `https://httpbin.org` 失败。
3. 在项目里启用 deno.lock（`deno install`），查看锁文件内容。

## 7. 一句话记住

> 权限按需给：`--allow-read=.` 只读当前目录、`--allow-net=域名` 只连指定主机；密钥走环境变量，锁文件保供应链。

<!-- ============ 文档分隔线：050-deno/004-DenoWebFrameworkDeploy.md ============ -->

## 0. 一句话理解

> 用 Hono 写路由、用 Deno KV 存数据、部署到 Deno Deploy——三样都是"边缘原生"，一个项目从零到上线不需要自建服务器。

## 1. Hono 第一个 API

```typescript
// main.ts
import { Hono } from "npm:hono@4"

const app = new Hono()

app.get("/", (c) => c.text("你好，Deno!"))

app.get("/hello/:name", (c) => {
  const name = c.req.param("name")
  return c.json({ message: `你好，${name}` })
})

Deno.serve(app.fetch)
```

```bash
deno run --allow-net main.ts
```

**讲解：**

1. `new Hono()` 创建应用，`app.get("/", 处理函数)` 注册路由；`c` 是上下文对象，`c.text/c.json` 返回响应。
2. `c.req.param("name")` 读取路径参数，`/hello/小明` 会返回 JSON 消息。
3. `Deno.serve(app.fetch)` 把 Hono 应用挂到 Deno 内置 HTTP 服务器上，不需要 Express 或额外依赖。

## 2. 接入 Deno KV

```typescript
// kv_todo.ts
import { Hono } from "npm:hono@4"

const kv = await Deno.openKv()
const app = new Hono()

app.post("/todos", async (c) => {
  const { title } = await c.req.json()
  const id = crypto.randomUUID()
  await kv.set(["todos", id], { title, done: false })
  return c.json({ id, title, done: false }, 201)
})

app.get("/todos", async (c) => {
  const list = []
  for await (const entry of kv.list({ prefix: ["todos"] })) {
    list.push({ id: entry.key[1], ...entry.value })
  }
  return c.json(list)
})

Deno.serve(app.fetch)
```

**讲解：**

1. `Deno.openKv()` 打开内置键值存储（本地是 SQLite，云端是 Deno KV），零配置即可持久化。
2. `kv.set(["todos", id], 对象)` 以数组作为分层键，`kv.list({ prefix: ["todos"] })` 遍历该前缀下的所有记录。
3. `crypto.randomUUID()` 生成唯一 id；`for await` 异步遍历 KV 结果集。
4. KV 天然适合会话、配置、小型业务数据；复杂关系查询仍然选数据库（如 PostgreSQL）。

## 3. 测试与检查

```typescript
// main_test.ts
import { assertEquals } from "jsr:@std/assert@1"
import { average } from "./main.ts"

Deno.test("average 基本功能", () => {
  assertEquals(average([1, 2, 3]), 2)
})
```

```bash
deno check main.ts
deno test
```

**讲解：**

1. 测试与业务函数同文件导出，`deno test` 自动发现 `_test.ts`。
2. `deno check` 做全量类型检查，是 CI 里最便宜的一层保障。

## 4. 部署到 Deno Deploy

```bash
# 安装部署 CLI
deno install -gArf jsr:@deno/deployctl

# 登录并部署
deployctl deploy --project=my-deno-app main.ts
```

**讲解：**

1. `deployctl deploy` 把项目推送到 Deno Deploy 边缘网络，全球节点就近执行，无需配置服务器。
2. 每次部署会生成新的预览 URL，正式域名在控制台绑定。
3. 云端自动注入 `Deno.openKv()`、`Deno.cron` 等服务，本地与线上 API 一致，无环境差异。

## 5. 动手试试

1. 给待办 API 增加 `DELETE /todos/:id`（`kv.delete(["todos", id])`）。
2. 用 `Deno.cron("daily", "0 3 * * *", ...)` 写一个每天 3 点清理已完成待办的定时任务。
3. 把项目部署到 Deno Deploy，用浏览器访问线上接口。

## 6. 一句话记住

> Deno 的 Web 开发链路最短：Hono 写 API、KV 存数据、Deploy 一键上线，权限参数决定它能碰什么。

<!-- ============ 文档分隔线：050-deno/005-AdvancedRoadmap.md ============ -->

## 0. 你现在在哪里（先读这里）

> 学习目标：对照进阶路线，明确接下来三站要学什么、为什么按这个顺序学、每站学到什么程度算过关。

前四篇文档带你完成了 Deno 的入门闭环：认识运行时（001）、跑起第一个脚本（002）、
理解权限模型（003）、用 Web 框架部署了服务（004）。到这里，你已经能用 Deno
写出并运行一个正经的 TypeScript 服务。

本篇是通往精通阶段的路线图：把剩余的核心能力拆成三站。每一站给出
"要解决的问题 → 核心 API 清单 → 最小示例 → 常见陷阱 → 过关自检"，
后续版本会把每一站展开为独立文档（编号紧接本篇）。

## 1. 进阶路线总览

| 站点 | 主题 | 解决的问题 | 核心能力 |
| --- | --- | --- | --- |
| 第五站 | 标准库与 npm 兼容 | 依赖从哪来：jsr:@std、npm:、node: 三个生态怎么用 | imports 映射、lockfile、Node 项目迁移 |
| 第六站 | Deno KV 与队列 | 数据存哪：零配置强一致存储与消息队列 | openKv、原子事务、enqueue/listenQueue |
| 第七站 | 测试、基准与 CI | 质量怎么保：零依赖的测试与流水线 | deno test/bench、lint/fmt/check |

三站的关系：第五站解决"代码的原料"，第六站解决"状态的归宿"，
第七站解决"质量的地基"。按顺序学，每一站都会用到前一站的成果——
例如第六站的项目要用第五站的 imports 映射组织依赖，第七站的测试要覆盖第六站的 KV 逻辑。

## 2. 第五站：标准库与 npm 兼容

Deno 2.x 完全兼容 npm 生态，同时自带走 JSR 发布的官方标准库。
这一站要建立"选依赖"的判断力。

### 2.1 三种导入来源对比

| 来源 | 示例 | 适用场景 | 特点 |
| --- | --- | --- | --- |
| jsr:@std | `import { join } from "jsr:@std/path@1"` | 通用工具 | 官方维护、TypeScript 原生、类型即文档 |
| npm: | `import express from "npm:express@5"` | 复用 Node 生态 | 全量 npm 包可用 |
| node: | `import { readFile } from "node:fs/promises"` | 熟悉的内置模块 | 与 Node 行为一致 |

### 2.2 用 deno.json 集中管理依赖

```json
{
  "imports": {
    "@std/path": "jsr:@std/path@^1.0.0",
    "express": "npm:express@^5.0.0"
  }
}
```

```ts
// main.ts —— 代码里只写别名，版本集中在 deno.json
import { join } from "@std/path";
import express from "express";

const app = express();
app.get("/", (_req, res) => res.send("Hello Deno + Express"));
app.listen(3000, () => console.log("http://localhost:3000"));
```

**讲解：** `imports` 是依赖的"唯一真相"：升级版本只改一处；
配合 `deno.json` 生成 lockfile 后，CI 与本地的依赖完全一致。

### 2.3 常用标准库速览

| 包 | 用途 | 一句话记忆 |
| --- | --- | --- |
| @std/fs | ensureDir、walk、exists | 目录操作不用再手写递归 |
| @std/path | join、dirname、extname | 跨平台路径拼接 |
| @std/assert | assertEquals、assertRejects | 测试断言标配 |
| @std/cli | parseArgs、prompt | 命令行参数解析 |
| @std/yaml | parse、stringify | YAML 读写 |

### 2.4 常见陷阱

- 直接写完整 URL 导入（`import ... from "jsr:@std/path@1.0.6"）而不进 imports 映射：
  版本散落各处，升级是灾难。
- 忘记生成/提交 lockfile：CI 拉到新版本导致"本地好好的，线上挂了"。
- 把 npm 包的 CommonJS 默认导出当作命名导入用，报 `does not provide an export named`。

### 2.5 过关自检

1. 能说出三种导入来源各自的最佳使用场景。
2. 新依赖一律先加进 `deno.json` 的 imports 再在代码中引用。
3. 用 `deno install` 把一个现成 Node 项目跑起来过一次。

## 3. 第六站：Deno KV 与队列

Deno 内置强一致键值数据库与消息队列，不装任何东西就能用——
这一站解决"小服务不想背一个数据库"的场景。

### 3.1 基本读写

```ts
// kv.ts —— 打开（本地开发默认使用 SQLite 后端，零配置）
const kv = await Deno.openKv();

// 写入：key 是数组（天然支持前缀查询），value 是结构化克隆数据
await kv.set(["users", "u_1001"], { name: "洛天依", vip: true });

// 读取
const res = await kv.get(["users", "u_1001"]);
console.log(res.value); // { name: "洛天依", vip: true }

// 前缀列出所有用户
for await (const entry of kv.list({ prefix: ["users"] })) {
  console.log(entry.key, entry.value);
}
```

**讲解：** key 用数组而不是字符串，是为了支持 `list({ prefix })` ——
`["users"]` 一次取出全部用户，`["users", "u_1001", "orders"]` 取某用户的订单，
这是 KV 数据建模的核心手法（把"表"编码进 key 前缀）。

### 3.2 原子操作：乐观并发

```ts
// 库存扣减：check 保证不超卖，sum 原子自增
const res = await kv.atomic()
  .check({ key: ["stock", "sku_1"], versionstamp: current.versionstamp })
  .sum(["stock", "sku_1"], 1n)
  .commit();
if (!res.ok) console.log("有人先改了，重试");
```

**讲解：** `check` 校验版本戳（别人改过就失败），`sum/set` 是本次变更，
`commit` 让整组操作原子生效——这就是 KV 版的"事务"。

### 3.3 消息队列

```ts
// 投递任务：可以晚点做、但必须做的事
await kv.enqueue({ type: "send-mail", to: "fan@example.com" });

// 消费任务：失败会自动重试
kv.listenQueue(async (msg) => {
  if (msg.type === "send-mail") await sendMail(msg.to);
});
```

### 3.4 常见陷阱

- 把 KV 当关系库用：需要多表 JOIN、复杂聚合时直接上 Postgres，不要硬建模。
- 忘记 value 是"结构化克隆"存储：函数、Symbol 这类无法克隆的值会报错。
- 本地与 Deno Deploy 的 KV 行为差异（配额、备份）部署前要查官方文档。

### 3.5 过关自检

1. 能用 key 前缀设计出"用户—订单"两级数据模型。
2. 能解释 check/sum/commit 如何防止超卖。
3. 能写一个"失败自动重试"的队列消费者。

## 4. 第七站：测试、基准与 CI

Deno 把质量工具内置进运行时，零配置即可使用。

### 4.1 测试骨架

```ts
// calc_test.ts —— 命名约定：*.test.ts 会被 deno test 自动发现
import { assertEquals, assertRejects } from "@std/assert";
import { add, loadConfig } from "./calc.ts";

Deno.test("add 两数相加", () => {
  assertEquals(add(1, 2), 3);
});

Deno.test("loadConfig 文件缺失时拒绝", async () => {
  await assertRejects(() => loadConfig("./not-exist.json"));
});

Deno.test("受限权限下运行", { permissions: { read: true } }, () => {
  // 只授予 read 权限验证代码在最小权限下可用
});
```

### 4.2 流水线三件套

| 命令 | 作用 | CI 用法 |
| --- | --- | --- |
| deno fmt | 统一格式 | `deno fmt --check` |
| deno lint | 静态检查 | `deno lint` |
| deno check | 类型检查 | `deno check main.ts` |

```yaml
# .github/workflows/ci.yml 最小流水线
name: ci
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: denoland/setup-deno@v2
        with:
          deno-version: v2.x
      - run: deno fmt --check
      - run: deno lint
      - run: deno test -A
```

### 4.3 常见陷阱

- 测试文件里 `import { test } from "bun:test"` 之类的串台导入（各运行时测试 API 不同）。
- 异步测试忘记 await，测试永远绿。
- CI 里不开 `--frozen` 类参数，依赖漂移。

### 4.4 过关自检

1. 能为零依赖项目写出"断言 + 受限权限"的测试。
2. 能解释 fmt/lint/check 各自拦截什么问题。
3. 有一条从 push 到测试通过的绿色流水线。

## 5. 学习建议

1. 顺序学，不跳站：第五站的 imports 映射是第六、七站脚本的组织基础。
2. 每一站做一个可运行的小项目：KV 购物车、带测试的 CLI 工具，比读三遍文档有效。
3. 版本跟进：Deno 每 12 周一个稳定版，LTS 模式已结束（2.5 是最后一个），
   建议跟随稳定版并在项目中锁定版本（lockfile + deno.json）。

## 小结与延伸

- 进阶三站：依赖管理 → 数据与队列 → 测试与 CI，对应从"能写"到"能上线"的跨越。
- 每一站的展开文档将陆续补充在本模块中，编号紧接本篇（006 起）。
- 官方资源：docs.deno.com（运行时）、jsr.io（标准库）、deno.com/deploy（部署）。

<!-- ============ 文档分隔线：050-deno/006-DenoStdLibNpmCompatibility.md ============ -->

# 标准库与 npm 兼容

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- 三种导入来源对比与选型
- deno.json imports 映射与 lockfile
- 常用标准库实操
- 从 Node 项目迁移的最短路径

<!-- ============ 文档分隔线：050-deno/007-DenoKVQueues.md ============ -->

# Deno KV 与队列

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- openKv 基本读写与 key 前缀建模
- 原子操作与乐观并发
- kv.watch 实时监听
- enqueue/listenQueue 与失败重试
- 适用边界与 Postgres 对比

<!-- ============ 文档分隔线：050-deno/008-DenoTestingBenchCI.md ============ -->

# 测试、基准与 CI

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- deno test 组织与 @std/assert 断言
- 异步与权限受限测试
- deno bench 基准
- fmt/lint/check 与 GitHub Actions
