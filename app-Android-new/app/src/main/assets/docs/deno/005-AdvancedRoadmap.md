---
order: 50
title: 进阶学习路线图
module: 'deno'
category: 后端技术
difficulty: intermediate
description: 承上启下：从已掌握的运行时与权限模型出发，给出通往精通的进阶路线、每站核心 API 与学习自检清单。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'deno/004-DenoWebFrameworkDeploy'
  - 'typescript/002-TypeScriptOverviewEnvSetup'
prerequisites:
  - 'deno/004-DenoWebFrameworkDeploy'
---

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
