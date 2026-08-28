---
order: 10
title: deno 模块文档合集
module: 'deno'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
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
