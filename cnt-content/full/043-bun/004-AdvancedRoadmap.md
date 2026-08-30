---
order: 40
title: 进阶学习路线图
module: 'bun'
category: 后端技术
difficulty: beginner
description: 承上启下：从已掌握的运行时与内置服务器出发，给出通往精通的进阶路线、每站核心 API 与学习自检清单。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'bun/003-BunBuiltinServerSQL'
  - 'javascript/002-JavaScriptOverviewRuntimeEnv'
prerequisites:
  - 'bun/003-BunBuiltinServerSQL'
---

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
