---
order: 10
title: nestjs 模块文档合集
module: 'nestjs'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-30'
related: []
prerequisites: []
---

<!-- ============================================================ nestjs/001-NestJSOverview ============================================================ -->

## 0. 五分钟创建第一个接口（先读这里）

> 学习目标：跑起一个 NestJS 应用，并理解"模块-控制器-服务"三层结构。

```bash
npm i -g @nestjs/cli
nest new todo-api --package-manager pnpm
cd todo-api
npm run start:dev
```

**讲解：**

1. `@nestjs/cli` 是官方脚手架；`nest new` 会生成一个完整的 TypeScript 项目并安装依赖。
2. `start:dev` 以监听模式启动，默认端口 3000，改代码自动重启。
3. 浏览器打开 `http://localhost:3000` 会看到 `Hello World!`——它来自 `app.controller.ts`。

## 1. NestJS 是什么

NestJS 是一个用 TypeScript 编写的 Node.js 服务端框架，2017 年发布。它借鉴了 Angular 的架构思想（模块化、依赖注入、装饰器），把 Express/Fastify 的底层能力包装成一套**结构规范**，让团队代码风格统一、易于测试和维护。

### 1.1 核心设计：三件套

| 角色 | 文件名示例 | 职责 |
| --- | --- | --- |
| 模块 Module | `app.module.ts` | 组织边界，声明谁属于谁 |
| 控制器 Controller | `app.controller.ts` | 接收 HTTP 请求，路由分发 |
| 服务 Service | `app.service.ts` | 业务逻辑与数据访问 |

请求流向：**HTTP 请求 → 控制器（校验参数）→ 服务（处理业务）→ 数据库 → 响应**。

### 1.2 版本现状（2026-08）

- NestJS 11.x 为当前稳定版（11.1.x）；v12 计划 2026 年 Q3 发布，将全面迁移到 ESM，并默认使用 Vitest、oxlint、Rspack 等现代工具链。
- 新项目直接用 CLI 创建即可，CLI 会安装当前稳定版。

## 2. 认识项目骨架

```text
todo-api/
  src/
    main.ts               # 入口：创建应用并监听端口
    app.module.ts         # 根模块
    app.controller.ts     # 根控制器（Hello World）
    app.service.ts        # 根服务
  test/                   # 单元测试与 e2e 测试
  nest-cli.json
  tsconfig.json
```

```typescript
// src/main.ts
import { NestFactory } from "@nestjs/core"
import { AppModule } from "./app.module"

async function bootstrap() {
  const app = await NestFactory.create(AppModule)
  await app.listen(3000)
}
bootstrap()
```

**讲解：**

1. `NestFactory.create(AppModule)` 从根模块构建整个应用：Nest 会扫描模块里的装饰器元数据，自动组装依赖。
2. `app.listen(3000)` 启动 HTTP 服务；生产环境端口从环境变量读取（如 `process.env.PORT`）。
3. `bootstrap()` 是异步函数，顶层调用即可，这是 Nest 项目的固定入口写法。

## 3. 动手试试

1. 修改 `app.controller.ts` 的 `getHello()` 返回你自己的名字，刷新页面确认生效。
2. 用 `nest g controller hello` 生成一个 `hello` 控制器，访问自动生成的路由。
3. 阅读 `app.module.ts`，找到 `controllers` 与 `providers` 数组，理解模块如何声明依赖。

## 4. 一句话记住

> NestJS = TypeScript + 模块化 + 依赖注入：控制器管请求、服务管业务、模块管组装，三个文件构成一个功能单元。

<!-- ============================================================ nestjs/002-ModuleControllerService ============================================================ -->

## 0. 一句话理解

> 一个功能单元 = 模块（组装）+ 控制器（接请求）+ 服务（写逻辑）+ DTO（定义入参）；控制器只负责"翻译 HTTP"，业务全部下沉到服务。

## 1. 生成功能模块

```bash
nest g module todos
nest g controller todos
nest g service todos
```

**讲解：**

1. `nest g` 是生成器命令，会自动创建文件并把类注册到对应模块。
2. 三条命令分别生成 `todos.module.ts`、`todos.controller.ts`、`todos.service.ts`，目录 `src/todos/`。
3. 生成后 `app.module.ts` 的 `imports` 会自动加入 `TodosModule`。

## 2. DTO：定义请求体

```typescript
// src/todos/dto/create-todo.dto.ts
export class CreateTodoDto {
  title: string
  done?: boolean
}
```

**讲解：**

1. DTO（Data Transfer Object）是"请求长什么样"的类型描述，控制器用它接收并校验参数。
2. `title` 必填、`done` 可选（`?`），先声明类型，下一章再用装饰器做真正的运行时校验。
3. 类（class）比接口（interface）更适合 DTO：编译后仍存在，能配合装饰器做校验与文档生成。

## 3. Service：业务逻辑

```typescript
// src/todos/todos.service.ts
import { Injectable } from "@nestjs/common"
import { CreateTodoDto } from "./dto/create-todo.dto"

export interface Todo {
  id: number
  title: string
  done: boolean
}

@Injectable()
export class TodosService {
  private todos: Todo[] = []
  private nextId = 1

  create(dto: CreateTodoDto): Todo {
    const todo: Todo = {
      id: this.nextId++,
      title: dto.title,
      done: dto.done ?? false
    }
    this.todos.push(todo)
    return todo
  }

  findAll(): Todo[] {
    return this.todos
  }

  remove(id: number): void {
    this.todos = this.todos.filter((t) => t.id !== id)
  }
}
```

**讲解：**

1. `@Injectable()` 装饰器标记该类可以被依赖注入：Nest 会在需要时自动创建单例实例。
2. `private todos: Todo[]` 是内存存储，重启即清空；真实项目在这里换成数据库访问。
3. `dto.done ?? false`：空值合并运算符，`undefined` 时取默认值 `false`。
4. `remove` 用 `filter` 生成新数组再赋值，这是不可变更新风格，避免残留已删除项。

## 4. Controller：接收请求

```typescript
// src/todos/todos.controller.ts
import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  ParseIntPipe,
  Post
} from "@nestjs/common"
import { TodosService } from "./todos.service"
import { CreateTodoDto } from "./dto/create-todo.dto"

@Controller("todos")
export class TodosController {
  constructor(private readonly todosService: TodosService) {}

  @Post()
  create(@Body() dto: CreateTodoDto) {
    return this.todosService.create(dto)
  }

  @Get()
  findAll() {
    return this.todosService.findAll()
  }

  @Delete(":id")
  remove(@Param("id", ParseIntPipe) id: number) {
    this.todosService.remove(id)
  }
}
```

**讲解：**

1. `@Controller("todos")` 声明路由前缀：`POST /todos`、`GET /todos`、`DELETE /todos/1`。
2. 构造器参数 `private readonly todosService: TodosService` 就是依赖注入：Nest 自动把服务实例传进来，不需要手动 new。
3. `@Body()` 取出请求体并交给 DTO；`@Param("id", ParseIntPipe)` 取出路径参数并自动转成数字，转失败返回 400。
4. 控制器里只有一行调用——业务逻辑全部在服务里，这是分层最重要的目的：控制器可测、服务可测、互不纠缠。

## 5. 手动接线：Module

```typescript
// src/todos/todos.module.ts
import { Module } from "@nestjs/common"
import { TodosController } from "./todos.controller"
import { TodosService } from "./todos.service"

@Module({
  controllers: [TodosController],
  providers: [TodosService]
})
export class TodosModule {}
```

**讲解：**

1. `controllers` 数组声明本模块对外提供哪些路由。
2. `providers` 数组声明本模块可注入的服务；Nest 会解析 `TodosController` 构造函数里的依赖并自动注入。
3. 若其他模块也要用 `TodosService`，需要在 `providers` 里保留并加到 `exports` 数组。

## 6. 动手试试

1. 用 `curl` 测试接口：`curl -X POST http://localhost:3000/todos -H "Content-Type: application/json" -d '{"title":"学 NestJS"}'`，再 `curl http://localhost:3000/todos`。
2. 给 Todo 增加 `priority` 字段（DTO、Service、接口三处同步修改）。
3. 新增 `PATCH /todos/:id` 接口，把 `done` 置为 true（服务里加 `toggle` 方法）。

## 7. 一句话记住

> 控制器用装饰器声明路由、服务用类封装业务、模块把它们组装起来；依赖注入让"谁来实例化"这件事交给框架。

<!-- ============================================================ nestjs/003-ValidationPipes ============================================================ -->

## 0. 一句话理解

> 管道（Pipe）在请求进入控制器前做"安检"：类型不对、字段缺失、格式错误，全部在门口拦截；异常过滤器负责把错误翻译成统一的 JSON 响应。

## 1. 安装校验依赖

```bash
npm i class-validator class-transformer
```

**讲解：**

1. `class-validator` 提供 `@IsString()`、`@IsInt()` 等声明式校验规则。
2. `class-transformer` 负责把普通请求对象转换成 DTO 类实例，校验规则才能真正生效。

## 2. 给 DTO 加校验规则

```typescript
// src/todos/dto/create-todo.dto.ts
import { IsBoolean, IsOptional, IsString, MaxLength, MinLength } from "class-validator"

export class CreateTodoDto {
  @IsString()
  @MinLength(1, { message: "标题不能为空" })
  @MaxLength(100, { message: "标题最长 100 字" })
  title: string

  @IsOptional()
  @IsBoolean()
  done?: boolean
}
```

**讲解：**

1. 装饰器从上到下依次校验：先确认是字符串，再检查长度。
2. `message` 自定义错误文案；不写则返回英文默认消息。
3. `@IsOptional()` 表示字段可以缺省，缺省时跳过其余校验。

## 3. 全局启用 ValidationPipe

```typescript
// src/main.ts
import { NestFactory } from "@nestjs/core"
import { ValidationPipe } from "@nestjs/common"
import { AppModule } from "./app.module"

async function bootstrap() {
  const app = await NestFactory.create(AppModule)
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      transform: true
    })
  )
  await app.listen(3000)
}
bootstrap()
```

**讲解：**

1. `whitelist: true`：自动删除 DTO 里没有声明属性的多余字段，防止"额外字段注入"。
2. `forbidNonWhitelisted: true`：出现多余字段直接报 400，适合严格接口。
3. `transform: true`：把请求对象转换成 DTO 实例，路径参数 `"1"` 也会按 DTO 类型转成数字。

## 4. 验证效果

```bash
# 缺 title：返回 400 与错误消息
curl -X POST http://localhost:3000/todos -H "Content-Type: application/json" -d '{}'

# 多余字段：返回 400
curl -X POST http://localhost:3000/todos -H "Content-Type: application/json" -d '{"title":"x","hack":1}'
```

**讲解：**

1. 第一句返回 `{ message: ["标题不能为空"], error: "Bad Request", statusCode: 400 }`，客户端可直接展示错误数组。
2. 第二句返回 `property hack should not exist`，把注入风险挡在业务逻辑之外。
3. 校验失败发生在管道层，服务方法根本不会被调用——这是"纵深防御"的第一道门。

## 5. 异常过滤器：统一错误格式

```typescript
// src/common/filters/http-exception.filter.ts
import {
  ArgumentsHost,
  Catch,
  ExceptionFilter,
  HttpException
} from "@nestjs/common"
import { Response } from "express"

@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp()
    const response = ctx.getResponse<Response>()
    const status = exception.getStatus()
    const body = exception.getResponse()

    response.status(status).json({
      code: status,
      message: typeof body === "string" ? body : (body as any).message,
      timestamp: new Date().toISOString()
    })
  }
}
```

**讲解：**

1. `@Catch(HttpException)` 声明这个过滤器只处理 HTTP 异常，其他异常继续走默认流程。
2. `host.switchToHttp()` 拿到底层请求/响应对象，`getResponse()` 是 Express 的 response。
3. 最终统一输出 `{ code, message, timestamp }` 结构，前端只需要解析一种错误格式。
4. 在 `main.ts` 用 `app.useGlobalFilters(new HttpExceptionFilter())` 注册为全局过滤器。

## 6. 动手试试

1. 给 `title` 加 `@Matches(/^[a-zA-Z0-9 ]+$/)` 规则，验证中文标题被拒绝。
2. 新建一个 `NotFoundException` 场景：查询不存在的 id 时抛 `new NotFoundException("待办不存在")`，确认响应格式。
3. 把过滤器注册为全局，测试校验失败的响应是否也走统一格式。

## 7. 一句话记住

> 校验交给管道、错误交给过滤器：入口越严格，业务代码越干净；全局统一错误结构，前端对接成本最低。

<!-- ============================================================ nestjs/004-DatabaseIntegration ============================================================ -->

## 0. 一句话理解

> 数据库接入 = 环境变量管连接串 + ORM 管模型与查询 + 模块管注入；NestJS 里 Prisma 是最主流的组合。

## 1. 安装与初始化

```bash
npm i @prisma/client prisma @nestjs/config
npx prisma init --datasource-provider postgresql
```

**讲解：**

1. `@prisma/client` 是运行时客户端，`prisma` 是命令行工具，`@nestjs/config` 提供环境变量读取。
2. `prisma init` 生成 `prisma/schema.prisma` 与 `.env`（含 `DATABASE_URL`）。
3. 本地开发用 Docker 起 PostgreSQL：`docker run -d --name pg-dev -p 5432:5432 -e POSTGRES_PASSWORD=dev123 postgres:18`。

## 2. 定义模型

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model Todo {
  id        Int      @id @default(autoincrement())
  title     String   @db.VarChar(100)
  done      Boolean  @default(false)
  createdAt DateTime @default(now())
}
```

**讲解：**

1. `@id @default(autoincrement())` 声明自增主键，对应 SQL 的 `PRIMARY KEY AUTO_INCREMENT`。
2. `@db.VarChar(100)` 指定数据库列类型，与 DTO 的 `MaxLength(100)` 形成双保险。
3. `@default(now())` 让数据库填默认创建时间，应用层不用管。

```bash
npx prisma migrate dev --name init
```

**讲解：**

1. `migrate dev` 根据 schema 生成 SQL 迁移并执行，同时重新生成 Prisma Client。
2. 生产环境用 `prisma migrate deploy` 执行已提交的迁移文件，保证多环境结构一致。
3. 每次修改 schema 后都要重新跑迁移，否则 Prisma Client 类型不更新。

## 3. 模块注入 PrismaService

```typescript
// src/prisma/prisma.service.ts
import { Injectable, OnModuleDestroy, OnModuleInit } from "@nestjs/common"
import { PrismaClient } from "@prisma/client"

@Injectable()
export class PrismaService
  extends PrismaClient
  implements OnModuleInit, OnModuleDestroy
{
  async onModuleInit() {
    await this.$connect()
  }

  async onModuleDestroy() {
    await this.$disconnect()
  }
}
```

**讲解：**

1. `PrismaService` 继承 `PrismaClient`，让应用里所有服务共用同一个数据库连接池。
2. `OnModuleInit/OnModuleDestroy` 生命周期钩子：应用启动时连接、关闭时断开，避免连接泄漏。
3. 把 `PrismaService` 放进模块的 `providers + exports`，其他模块 `imports` 后即可注入。

## 4. Service 使用 Prisma

```typescript
// src/todos/todos.service.ts
import { Injectable } from "@nestjs/common"
import { PrismaService } from "../prisma/prisma.service"
import { CreateTodoDto } from "./dto/create-todo.dto"

@Injectable()
export class TodosService {
  constructor(private readonly prisma: PrismaService) {}

  create(dto: CreateTodoDto) {
    return this.prisma.todo.create({
      data: { title: dto.title, done: dto.done ?? false }
    })
  }

  findAll() {
    return this.prisma.todo.findMany({ orderBy: { createdAt: "desc" } })
  }

  remove(id: number) {
    return this.prisma.todo.delete({ where: { id } })
  }
}
```

**讲解：**

1. `this.prisma.todo.create({ data: {...} })` 对应 `INSERT`，返回完整的新记录。
2. `findMany({ orderBy })` 对应带排序的 `SELECT`；Prisma 查询对象有完整类型提示，字段拼错在编译期就报错。
3. `delete` 对应 `DELETE`，`where: { id }` 里的 id 必须是唯一键；删除不存在记录会抛异常，可捕获后转成 404。
4. 之前的 `nextId` 与数组存储全部删除——业务代码只关心"做什么"，不关心 SQL 细节。

## 5. 动手试试

1. 给 Todo 加 `priority` 字段（枚举 Int），重新迁移，验证类型提示自动更新。
2. 把 `remove` 改成软删除：加 `deletedAt DateTime?` 字段，查询时过滤 `deletedAt: null`。
3. 在 `TodosModule` 里 `imports: [PrismaModule]`，确认 `PrismaService` 可注入。

## 6. 一句话记住

> Prisma 把数据库变成类型安全的模型：`create/findMany/update/delete` 就是增删改查，连接生命周期交给 PrismaService 统一管理。

<!-- ============================================================ nestjs/005-Testing ============================================================ -->

## 0. 一句话理解

> 单元测试只测"一个类"（服务），把数据库换成假的；端到端测试启动整个应用，用真实 HTTP 请求验证"从路由到响应"的完整链路。

## 1. 服务单元测试

```typescript
// src/todos/todos.service.spec.ts
import { Test } from "@nestjs/testing"
import { TodosService } from "./todos.service"
import { PrismaService } from "../prisma/prisma.service"

describe("TodosService", () => {
  let service: TodosService
  const prisma = {
    todo: {
      create: jest.fn(),
      findMany: jest.fn(),
      delete: jest.fn()
    }
  }

  beforeEach(async () => {
    const moduleRef = await Test.createTestingModule({
      providers: [
        TodosService,
        { provide: PrismaService, useValue: prisma }
      ]
    }).compile()

    service = moduleRef.get(TodosService)
  })

  it("创建待办时调用 prisma.todo.create", async () => {
    prisma.todo.create.mockResolvedValue({
      id: 1,
      title: "测试",
      done: false
    })

    const result = await service.create({ title: "测试" })

    expect(prisma.todo.create).toHaveBeenCalledWith({
      data: { title: "测试", done: false }
    })
    expect(result.id).toBe(1)
  })
})
```

**讲解：**

1. `Test.createTestingModule` 用测试模块替代真实应用，只加载被测服务。
2. `{ provide: PrismaService, useValue: prisma }` 是"替身注入"：用 `jest.fn()` 假对象替换数据库，测试不碰真实数据库。
3. `mockResolvedValue` 设置假返回；`toHaveBeenCalledWith` 断言调用参数，防止服务悄悄改错了入参。
4. 单元测试的关键：只测 `TodosService` 自己的逻辑，数据库行为由 `expect` 调用参数来约束。

## 2. 控制器单元测试

```typescript
// src/todos/todos.controller.spec.ts
import { Test } from "@nestjs/testing"
import { TodosController } from "./todos.controller"
import { TodosService } from "./todos.service"

describe("TodosController", () => {
  let controller: TodosController

  beforeEach(async () => {
    const moduleRef = await Test.createTestingModule({
      controllers: [TodosController],
      providers: [
        {
          provide: TodosService,
          useValue: { create: jest.fn(), findAll: jest.fn(), remove: jest.fn() }
        }
      ]
    }).compile()

    controller = moduleRef.get(TodosController)
  })

  it("findAll 返回服务结果", async () => {
    jest
      .spyOn(controller as any, "todosService")
      .mockReturnValue({ findAll: () => [] })

    // 更常见做法：先拿到 service 替身再断言
    const service = moduleRef.get(TodosService)
    service.findAll = jest.fn().mockResolvedValue([])
    await expect(controller.findAll()).resolves.toEqual([])
  })
})
```

**讲解：**

1. 控制器测试同样注入替身服务，验证"路由方法把参数正确传给服务"。
2. `useValue` 里的三个方法都是 `jest.fn()`，未被调用的方法不会影响测试。
3. 注意：真实测试里应通过 `moduleRef.get(TodosService)` 拿到替身再设置返回值，不要在私有属性上做手脚。

## 3. 端到端测试

```typescript
// test/todos.e2e-spec.ts
import { Test } from "@nestjs/testing"
import { INestApplication, ValidationPipe } from "@nestjs/common"
import request from "supertest"
import { AppModule } from "../src/app.module"

describe("Todos (e2e)", () => {
  let app: INestApplication

  beforeAll(async () => {
    const moduleRef = await Test.createTestingModule({
      imports: [AppModule]
    }).compile()

    app = moduleRef.createNestApplication()
    app.useGlobalPipes(new ValidationPipe({ whitelist: true }))
    await app.init()
  })

  afterAll(async () => {
    await app.close()
  })

  it("POST /todos 创建并返回 201", async () => {
    const res = await request(app.getHttpServer())
      .post("/todos")
      .send({ title: "写测试" })
      .expect(201)

    expect(res.body.title).toBe("写测试")
  })

  it("校验失败返回 400", async () => {
    await request(app.getHttpServer())
      .post("/todos")
      .send({})
      .expect(400)
  })
})
```

**讲解：**

1. e2e 测试加载 `AppModule` 完整应用，`app.init()` 后通过 `app.getHttpServer()` 接收真实 HTTP 请求。
2. `supertest` 的 `.expect(201)` 断言状态码，`.send({...})` 发送请求体——与真实客户端行为一致。
3. `beforeAll/afterAll` 启动与关闭应用；测试间共享状态时注意用 `beforeEach` 清理数据。
4. e2e 测试可以连真实测试数据库，也可以注入内存实现；连真实库时每个用例后要清理数据，避免用例互相污染。

## 4. 测试策略建议

| 层级 | 覆盖内容 | 速度 | 数量 |
| --- | --- | --- | --- |
| 单元测试 | 服务、工具函数、管道逻辑 | 毫秒级 | 多 |
| 控制器测试 | 参数传递、状态码 | 毫秒级 | 中 |
| e2e 测试 | 完整链路、校验、数据库 | 秒级 | 少 |

## 5. 动手试试

1. 为 `TodosService.remove` 写单元测试：删除不存在记录时，Prisma 抛错被转换成 404。
2. 为 `POST /todos` 补充 e2e 用例：发送 101 个字符的标题，断言 400。
3. 运行 `npm test` 与 `npm run test:e2e`，把两个失败用例修到全绿。

## 6. 一句话记住

> 单元测试用替身隔离依赖、测逻辑；e2e 测试起真应用、走真 HTTP；两者配合，重构时才有底气。

<!-- ============================================================ nestjs/006-GuardsAndLifecycle ============================================================ -->

## 0. 请求生命周期（先读这里）

> 学习目标：看懂一个请求从进入 NestJS 到返回响应要穿过哪些组件、各自负责什么；会用 CanActivate 编写鉴权守卫，用 @SetMetadata 与 Reflector 实现声明式角色控制；理解方法级、控制器级、全局三种绑定作用域的差异。

一个请求会依次穿过 7 层组件，每层只做一类事：

| 顺序 | 组件 | 核心接口 | 典型职责 |
| --- | --- | --- | --- |
| 1 | 中间件 Middleware | NestMiddleware | 通用预处理：CORS、body 解析、请求日志 |
| 2 | 守卫 Guard | CanActivate | 决定请求能否继续：登录态、角色、限流 |
| 3 | 拦截器（前半） | NestInterceptor | 计时起点、请求改写 |
| 4 | 管道 Pipe | PipeTransform | 参数转换与校验（见第 3 篇） |
| 5 | 处理器 Handler | Controller + Service | 真正的业务逻辑 |
| 6 | 拦截器（后半） | RxJS 操作符 | 响应映射、统一包装 |
| 7 | 异常过滤器 | ExceptionFilter | 兜底所有未捕获异常 |

```mermaid
flowchart LR
  A[Middleware] --> B[Guard]
  B -->|拒绝| F[Exception Filter]
  B -->|放行| C[Interceptor 前]
  C --> D[Pipe]
  D --> E[Handler]
  E --> G[Interceptor 后]
  G --> H[响应]
  E -->|抛异常| F
```

先记住三个结论：守卫在管道与处理器之前，鉴权失败时校验和业务都不会执行；拦截器横跨前后两半，天然适合"环绕通知"式的逻辑；任何一层抛出的异常，最终都汇入异常过滤器。拦截器与异常过滤器是下一篇的主角，本章先把管线起点（守卫）吃透。

## 1. 第一个守卫：CanActivate

守卫返回 `true` 放行、`false` 拒绝（默认 403）。先做一个登录守卫：

```typescript
// src/common/guards/auth.guard.ts
import {
  CanActivate,
  ExecutionContext,
  Injectable,
  UnauthorizedException
} from "@nestjs/common"

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest()
    const token = request.headers["authorization"]
    if (!token) {
      // 未携带凭证直接 401，业务代码完全无感
      throw new UnauthorizedException("请先登录")
    }
    // 真实项目在这里校验 JWT，并把解析出的用户挂到 request 上
    request.user = { id: 1, name: "itian", roles: ["admin"] }
    return true
  }
}
```

**讲解：**

1. `ExecutionContext` 是"请求上下文 + 反射信息"的组合体：`switchToHttp()` 拿到底层请求/响应对象，`getHandler()` 与 `getClass()` 用来区分当前是哪个方法、哪个控制器。
2. 守卫里抛异常与返回 `false` 都是拒绝，但抛 `UnauthorizedException`、`ForbiddenException` 能带明确的状态码与文案，前端好区分"没登录"和"没权限"。
3. `request.user` 是守卫写给下游的"公共上下文"：管道、处理器、拦截器都能读到，第 4 节的参数装饰器会优雅地消费它。
4. 守卫是 DI 容器的正式成员，可以注入 `ConfigService`、`JwtService` 等任意 Provider，这是守卫优于"控制器里手写 if 判断"的根本原因。

## 2. 声明式角色控制：@SetMetadata 与 Reflector

"哪些接口要什么角色"不该硬编码在守卫里，用元数据声明、由守卫读取：

```typescript
// src/common/decorators/roles.decorator.ts
import { SetMetadata } from "@nestjs/common"

export const ROLES_KEY = "roles"
// @Roles("admin") 会把 ["admin"] 写进路由元数据
export const Roles = (...roles: string[]) => SetMetadata(ROLES_KEY, roles)
```

```typescript
// src/common/guards/roles.guard.ts
import {
  CanActivate,
  ExecutionContext,
  ForbiddenException,
  Injectable
} from "@nestjs/common"
import { Reflector } from "@nestjs/core"
import { ROLES_KEY } from "../decorators/roles.decorator"

@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private readonly reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    // 依次查"方法上"与"类上"的元数据，方法级覆盖类级
    const required = this.reflector.getAllAndOverride<string[]>(ROLES_KEY, [
      context.getHandler(),
      context.getClass()
    ])
    if (!required?.length) return true // 未标注角色的接口不限制
    const { user } = context.switchToHttp().getRequest()
    const ok = required.some((role) => user?.roles?.includes(role))
    if (!ok) throw new ForbiddenException("权限不足")
    return true
  }
}
```

控制器里两个守卫一起挂：

```typescript
// src/todos/todos.controller.ts（节选）
@Controller("todos")
@UseGuards(AuthGuard) // 类级：整个控制器都要求登录
export class TodosController {
  @Post()
  @UseGuards(RolesGuard) // 方法级：登录之外还要求角色
  @Roles("admin")
  create(@Body() dto: CreateTodoDto) {
    return this.todosService.create(dto)
  }
}
```

**讲解：**

1. `@SetMetadata(key, value)` 把任意数据附着在路由上，本质是给方法打了个标签；`Reflector` 是读取标签的官方工具。
2. `getAllAndOverride` 按数组顺序查找、命中即返回，形成"方法覆盖类"的语义；想把两处角色合并判断则改用 `getAllAndMerge`。
3. 规则写在路由上（声明）、逻辑收敛在守卫里（执行），新增接口只需要一行 `@Roles(...)`——这就是声明式鉴权的价值。
4. 进阶：Nest 新版提供 `Reflector.createDecorator<string[]>()` 创建类型安全的装饰器，用法以官方文档为准。

## 3. 绑定作用域：方法、控制器与全局

| 方式 | 写法 | 依赖注入 | 适用场景 |
| --- | --- | --- | --- |
| 方法级 | 方法上 `@UseGuards(X)` | 传类引用时支持 | 单个接口的特殊规则 |
| 控制器级 | 类上 `@UseGuards(X)` | 传类引用时支持 | 整组接口统一约束 |
| 全局（推荐） | `{ provide: APP_GUARD, useClass }` | 支持 | 鉴权等全站逻辑 |
| 全局（实例） | `app.useGlobalGuards(new X())` | 不支持 | main.ts 里快速试验 |

全局注册推荐走模块 Provider：

```typescript
// src/app.module.ts（节选）
import { APP_GUARD } from "@nestjs/core"

@Module({
  providers: [
    { provide: APP_GUARD, useClass: AuthGuard }, // 先注册先执行
    { provide: APP_GUARD, useClass: RolesGuard }
  ]
})
export class AppModule {}
```

**讲解：**

1. 传类引用（而非 new 出来的实例）时，Nest 会在所属模块作用域内实例化，构造器依赖正常注入；`useGlobalGuards(new X())` 脱离模块上下文，只适合零依赖组件。
2. 同一个 `APP_GUARD` token 写多个即注册多个全局守卫，执行顺序就是书写顺序：AuthGuard 先登录校验，RolesGuard 后判角色。
3. 全局守卫对每一个路由生效（包括不存在的路由），因此 RolesGuard 里"没有元数据就放行"的判断必不可少。

## 4. 自定义参数装饰器：消费守卫的产出

守卫把用户挂到 `request.user` 之后，用参数装饰器在控制器里优雅取出：

```typescript
// src/common/decorators/current-user.decorator.ts
import { createParamDecorator, ExecutionContext } from "@nestjs/common"

export const CurrentUser = createParamDecorator(
  (data: string | undefined, ctx: ExecutionContext) => {
    const request = ctx.switchToHttp().getRequest()
    const user = request.user
    // @CurrentUser("id") 取单字段；@CurrentUser() 取整个用户对象
    return data ? user?.[data] : user
  }
)
```

```typescript
@Get("me")
me(@CurrentUser() user: AuthUser, @CurrentUser("name") name: string) {
  return { user, name }
}
```

**讲解：**

1. 工厂函数第一个参数就是使用处传入的值：`@CurrentUser("id")` 传入 `"id"`，配合可选参数实现"取整 / 取字段"两种用法。
2. 参数装饰器在管道之后求值，但它依赖的数据（`request.user`）由守卫提前写入——管线各层围绕同一个 request 对象协作，分工明确。

## 5. 小结与延伸

- 请求生命周期七层：Middleware、Guard、Interceptor（前）、Pipe、Handler、Interceptor（后）、Exception Filter，各层只做一类事。
- 守卫答"能不能进"：`CanActivate` + `ExecutionContext` 判断，`@SetMetadata`/`Reflector` 做声明式角色控制。
- 全站性守卫用 `APP_GUARD` token 注册在 `AppModule`，支持 DI 且顺序可控。
- 延伸：真实项目鉴权用 `@nestjs/passport` + `@nestjs/jwt`（Strategy 模式对接守卫）；限流用 `@nestjs/throttler`（同样基于守卫实现）。

<!-- ============================================================ nestjs/007-InterceptorsAndFilters ============================================================ -->

## 0. 环绕逻辑与错误兜底（先读这里）

> 学习目标：用 NestInterceptor 实现耗时日志与统一响应壳，掌握 RxJS 的 map、tap、catchError 在拦截器中的分工；定义业务异常并编写全量异常过滤器；用实验验证整条管线的执行顺序。

上一篇的管线表里，守卫负责"能不能进"，而"进出来什么"（拦截器）与"出错怎么办"（异常过滤器）是本章主角。拦截器横跨处理前后两半，异常过滤器兜底所有未捕获异常，两者共同决定接口的最终输出形态。

## 1. 拦截器：日志与耗时统计

拦截器是函数式思维：`next.handle()` 返回响应流（RxJS Observable），写在 `handle()` 之前的逻辑是"前半"，用操作符加工返回流的是"后半"。

```typescript
// src/common/interceptors/logging.interceptor.ts
import {
  CallHandler,
  ExecutionContext,
  Injectable,
  NestInterceptor
} from "@nestjs/common"
import { Observable, tap } from "rxjs"

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const req = context.switchToHttp().getRequest()
    const start = Date.now()
    console.log(`--> ${req.method} ${req.url}`)
    return next.handle().pipe(
      // tap 只做旁路观察不改数据；处理器成功返回后才打印耗时
      tap(() => console.log(`<-- ${req.method} ${req.url} ${Date.now() - start}ms`))
    )
  }
}
```

**讲解：**

1. `intercept` 返回什么流，Nest 就以什么作为响应：不调用 `next.handle()` 相当于短路（配合缓存、熔断场景）。
2. `tap` 用于副作用（日志、埋点），`map` 用于改数据，混用会让"谁改了返回值"难以追踪。
3. 拦截器与守卫一样支持方法级 `@UseInterceptors(X)`、控制器级与全局三种绑定，粒度记忆可以完全复用。

## 2. 拦截器：统一响应壳与错误转换

```typescript
// src/common/interceptors/transform.interceptor.ts
import {
  CallHandler,
  ExecutionContext,
  Injectable,
  NestInterceptor
} from "@nestjs/common"
import { map, Observable } from "rxjs"

export interface ApiResponse<T> {
  code: number
  data: T
  timestamp: string
}

@Injectable()
export class TransformInterceptor<T>
  implements NestInterceptor<T, ApiResponse<T>>
{
  intercept(
    context: ExecutionContext,
    next: CallHandler<T>
  ): Observable<ApiResponse<T>> {
    return next.handle().pipe(
      // map 把每个处理器的返回值包上统一外壳
      map((data) => ({ code: 0, data, timestamp: new Date().toISOString() }))
    )
  }
}
```

错误分支同样在流上处理，`catchError` 可以在异常进入过滤器之前先做一次转换：

```typescript
// 追加到 transform.interceptor.ts 的 pipe 中
import { catchError, throwError } from "rxjs"
import { HttpException, InternalServerErrorException } from "@nestjs/common"

return next.handle().pipe(
  catchError((err) => {
    // HttpException 原样放行给过滤器；未知异常统一转成 500
    if (err instanceof HttpException) return throwError(() => err)
    return throwError(() => new InternalServerErrorException("服务内部错误"))
  })
)
```

**讲解：**

1. 统一响应壳与第 3 篇的统一错误结构是一对：成功走 `TransformInterceptor`，失败走 `ExceptionFilter`，前端只需要解析两种固定格式。
2. `catchError` 不是必须的：不处理时异常沿管线继续向后传，最终由异常过滤器接收；在这里先转换，适合"把第三方库的私有错误类型翻译成 HTTP 语义"。
3. RxJS 的 `Observable` 是惰性流，不订阅就不执行，Nest 负责订阅，你只管在管道里加工。
4. 全局注册方式与守卫一致：`{ provide: APP_INTERCEPTOR, useClass: TransformInterceptor }`，先注册的先执行。

## 3. 业务异常与全量异常过滤器

第 3 篇写过只处理 `HttpException` 的局部过滤器；进阶做法是定义业务异常 + 一个全量兜底过滤器：

```typescript
// src/common/exceptions/business.exception.ts
import { HttpException, HttpStatus } from "@nestjs/common"

// 业务异常：携带业务错误码，HTTP 状态固定 422
export class BusinessException extends HttpException {
  constructor(
    message: string,
    private readonly bizCode: number
  ) {
    super(message, HttpStatus.UNPROCESSABLE_ENTITY)
  }

  getBizCode(): number {
    return this.bizCode
  }
}
```

```typescript
// src/common/filters/all-exceptions.filter.ts
import {
  ArgumentsHost,
  Catch,
  ExceptionFilter,
  HttpException,
  HttpStatus
} from "@nestjs/common"
import { Response } from "express"

@Catch() // 不带参数 = 捕获所有类型的异常
export class AllExceptionsFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost) {
    const res = host.switchToHttp().getResponse<Response>()

    if (exception instanceof HttpException) {
      const status = exception.getStatus()
      const body = exception.getResponse()
      return res.status(status).json({
        code: status,
        message:
          typeof body === "string" ? body : ((body as any).message ?? "请求失败")
      })
    }
    // 未知异常：完整堆栈只留在服务端，不泄露给客户端
    console.error(exception)
    return res.status(HttpStatus.INTERNAL_SERVER_ERROR).json({
      code: 500,
      message: "服务内部错误"
    })
  }
}
```

全局注册推荐走模块 Provider，这样过滤器内部也能依赖注入：

```typescript
// src/app.module.ts（节选）
import { APP_FILTER } from "@nestjs/core"

providers: [{ provide: APP_FILTER, useClass: AllExceptionsFilter }]
```

**讲解：**

1. `exception: unknown` 的类型签名是刻意设计：强制你显式处理"不是 HttpException 的情况"，而不是假设一切皆 Http。
2. `@Catch(HttpException)` 的局部过滤器与 `@Catch()` 全量过滤器可以共存，Nest 会挑最匹配的过滤器执行，全量兜底只负责"漏网之鱼"。
3. 服务类里 `throw new BusinessException("余额不足", 40001)`，客户端拿到 422 与业务码，比直接抛 Error 更有契约感。
4. 未知异常日志务必打在服务端（含堆栈），客户端只收到笼统的 500——这是安全与排障的平衡点。

## 4. 执行顺序验证实验

给同一接口挂上全部组件，每个组件打一行日志：

```typescript
// 临时实验：probe.guard.ts / probe.interceptor.ts / probe.filter.ts
// 各自 console.log 标识自身，全部注册后请求 POST /todos 观察输出
```

```bash
# 请求 POST /todos（body 合法），控制台输出顺序：
# [guard] AuthGuard
# [guard] RolesGuard
# [interceptor] 前半
# [pipe] ValidationPipe 校验通过
# [handler] TodosController.create
# [interceptor] 后半

# 把 body 改成非法数据再请求：
# [guard]、[interceptor] 前半、[pipe] 校验失败、[filter] 兜底
# —— handler 与拦截器后半消失，管道失败直接跳到过滤器
```

**讲解：**

1. 成功路径按上一篇的七层表严格递进；异常路径中，守卫抛异常时拦截器与管道都不会执行，处理器抛异常时拦截器的 `catchError` 先收到、过滤器最后兜底。
2. 把这套实验写进学习笔记：将来排查"过滤器没生效""拦截器跑了两次"类问题时，按时序逐层断点即可定位。

## 5. 小结与延伸

- 拦截器答"进出来什么"：`tap` 做副作用、`map` 做响应变换、`catchError` 做错误转换。
- 异常过滤器答"出错怎么办"：`BusinessException` 携带业务码，`@Catch()` 全量兜底统一错误结构。
- 全局组件用 `APP_GUARD` / `APP_INTERCEPTOR` / `APP_FILTER` 注册，支持 DI 且顺序可控。
- 延伸：`@nestjs/terminus` 健康检查与超时控制 `TimeoutInterceptor` 见官方 Interceptors 章节；RxJS 学习重点先掌握 tap、map、catchError 三个操作符即可覆盖八成场景。

<!-- ============================================================ nestjs/008-ConfigEnvValidation ============================================================ -->

## 0. 配置为什么值得单独一章（先读这里）

> 学习目标：用 @nestjs/config 建立"命名空间配置文件 + 全局注入"的配置体系；用 zod 在应用启动时校验全部环境变量（fail fast）；通过 z.infer 与继承获得类型安全的 ConfigService；掌握 .env 多环境分层与生产密钥管理约定。

配置翻车三连：本地跑得好好的，上线才发现 `DATABASE_URL` 拼错；`PORT` 读出来是字符串 `"3000"`，与 `3000` 严格比较永远为 false；密钥被同事提交进了 git。本章一次性解决这三类问题：

| 问题 | 本章方案 | 小节 |
| --- | --- | --- |
| 配置散落、拼错 key 无提示 | registerAs 命名空间 | 2 |
| 坏配置到运行时才爆炸 | validate 函数 + zod，启动即失败 | 3 |
| 读取结果全是 any | z.infer + TypedConfigService | 4 |
| 密钥入库、环境混淆 | .env 分层与 .env.example 约定 | 5-6 |

## 1. 安装与 ConfigModule.forRoot

```bash
npm i @nestjs/config zod
```

第 4 篇已经在用 `@nestjs/config` 读取 `DATABASE_URL`，现在把完整体系搭起来：

```typescript
// src/app.module.ts
import { Module } from "@nestjs/common"
import { ConfigModule } from "@nestjs/config"
import { validate } from "./config/env.validation"

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true, // 全局模块：业务模块无需重复 imports
      envFilePath: [".env.local", ".env"], // 数组靠前的优先，命中即停
      validate // 启动即校验，失败直接拒绝启动
    })
  ]
})
export class AppModule {}
```

**讲解：**

1. `isGlobal: true` 让 `ConfigService` 在全应用可注入，等价于每个模块都 imports 一遍 `ConfigModule`，省去重复接线。
2. `envFilePath` 是数组时按顺序取第一个存在的文件，实现".env.local 本机覆盖 .env 团队默认"的约定。
3. `ignoreEnvFile: true` 用于生产：完全忽略 .env 文件，只认平台注入的真实环境变量（容器与 K8s 场景标配），第 6 节展开。

## 2. 自定义配置文件：registerAs 命名空间

散落的 `process.env.xxx` 是隐形全局变量；`registerAs` 把配置按域分组、以 Provider 形式注册：

```typescript
// src/config/app.config.ts
import { registerAs } from "@nestjs/config"

export default registerAs("app", () => ({
  name: process.env.APP_NAME ?? "fandex-api",
  port: Number(process.env.PORT ?? 3000)
}))
```

```typescript
// src/config/db.config.ts
import { registerAs } from "@nestjs/config"

export default registerAs("db", () => ({
  url: process.env.DATABASE_URL,
  maxPool: Number(process.env.DB_POOL_MAX ?? 10)
}))
```

```typescript
// src/config/config.module.ts —— 集中注册所有命名空间
import { Module } from "@nestjs/common"
import { ConfigModule } from "@nestjs/config"
import appConfig from "./app.config"
import dbConfig from "./db.config"

@Module({
  imports: [
    ConfigModule.forFeature(appConfig),
    ConfigModule.forFeature(dbConfig)
  ],
  exports: [ConfigModule]
})
export class AppConfigModule {}
```

```typescript
// 任意服务中按命名空间读取
constructor(private readonly config: ConfigService) {}

get appInfo() {
  return {
    name: this.config.get("app.name"),
    port: this.config.get("app.port")
  }
}
```

**讲解：**

1. `registerAs(key, factory)` 返回带 key 的 Provider 工厂，`forFeature` 把它注册进模块；工厂延迟求值，测试里可先改环境变量再实例化。
2. 读取时点是"命名空间.字段"，如 `app.port`；但拼错 key 不报错、只会返回 `undefined`——这正是第 4 节要类型化的原因。

## 3. 启动即校验：zod schema + validate（fail fast）

核心思想：把 `process.env` 当作"不可信的外部输入"，启动时用 zod 解析一遍，错一个变量就拒绝启动，并一次性列出所有问题：

```typescript
// src/config/env.validation.ts
import { z } from "zod"

// schema 即文档：需要哪些变量、什么类型、什么默认值，一目了然
const envSchema = z.object({
  NODE_ENV: z.enum(["development", "test", "production"]).default("development"),
  PORT: z.coerce.number().int().min(1).max(65535).default(3000),
  DATABASE_URL: z.string().url("必须是合法的连接串"),
  JWT_SECRET: z.string().min(32, "至少 32 位，防暴力破解")
})

// 由 schema 反推出 TS 类型，第 4 节直接复用
export type Env = z.infer<typeof envSchema>

export function validate(config: Record<string, unknown>): Env {
  const result = envSchema.safeParse(config)
  if (!result.success) {
    const detail = result.error.issues
      .map((i) => `  - ${i.path.join(".")}: ${i.message}`)
      .join("\n")
    throw new Error(`环境变量校验失败，请对照 .env.example 检查：\n${detail}`)
  }
  return result.data // 校验通过后的强类型对象，PORT 已是 number
}
```

运行效果：

```bash
# 缺 JWT_SECRET 且 DATABASE_URL 格式错误时，启动直接失败
Error: 环境变量校验失败，请对照 .env.example 检查：
  - DATABASE_URL: 必须是合法的连接串
  - JWT_SECRET: 至少 32 位，防暴力破解
```

**讲解：**

1. `z.coerce.number()` 一步完成"字符串转数字 + 校验"，修掉 `"3000" === 3000` 的经典 bug。
2. `safeParse` 不抛异常，方便把所有 issue 汇总成一次报错；用 `parse` 遇到第一个错误就中断，排查体验差。
3. 返回的 `result.data` 会成为 ConfigModule 内部的配置源：`get("PORT")` 拿到的是转换后的 number。
4. NestJS 12 原生支持 Standard Schema（zod、valibot、arktype 等实现的统一校验接口），schema 可直接交给框架消费，写法更简洁，细节以官方文档为准；本节的 validate 函数写法在 NestJS 11 与 12 上都可用。

## 4. 类型安全读取：infer 出来的 ConfigService

`get("app.port")` 返回 any、字符串 key 拼错无提示——用继承补一层强类型门面：

```typescript
// src/config/typed-config.service.ts
import { Injectable } from "@nestjs/common"
import { ConfigService } from "@nestjs/config"
import type { Env } from "./env.validation"

@Injectable()
export class TypedConfigService extends ConfigService<Env, true> {
  // 每个变量一个 getter：调用方拿到精确类型，无需记忆字符串 key
  get port(): number {
    return this.get("PORT", { infer: true })!
  }

  get databaseUrl(): string {
    return this.get("DATABASE_URL", { infer: true })!
  }

  get jwtSecret(): string {
    return this.get("JWT_SECRET", { infer: true })!
  }
}
```

```typescript
// src/app.module.ts providers 中注册
providers: [TypedConfigService]

// 业务代码里注入 TypedConfigService
constructor(private readonly cfg: TypedConfigService) {}
```

**讲解：**

1. `ConfigService<Env, true>` 的第二个泛型开启 infer 模式：`this.get("PORT", { infer: true })` 直接返回 number 而不是 any。
2. `Env` 来自 `z.infer`，schema 改了类型自动跟着变，配置文件与 TS 类型永远同步，这正是 TypeScript 泛型推导的价值。
3. getter 门面的额外收益：全局搜索使用点即可评估改动影响，重命名重构才敢下手；`!` 非空断言是安全的，因为启动校验已保证字段存在。

## 5. .env 多环境与 .env.example 约定

| 文件 | 是否提交 git | 用途 |
| --- | --- | --- |
| .env.example | 提交 | 变量清单 + 示例值，新人克隆后照着填 |
| .env | 不提交 | 本地团队默认环境 |
| .env.local | 不提交 | 本机个人覆盖（真实密钥），优先级最高 |
| 平台注入 | 无文件 | 生产环境由容器、K8s、云平台注入 |

```bash
# .gitignore 追加
.env
.env.local
```

```bash
# .env.example
# 应用
APP_NAME=fandex-api
PORT=3000
# 数据库
DATABASE_URL=postgresql://postgres:dev123@localhost:5432/fandex
# 认证密钥（生成命令见下）
JWT_SECRET=replace-me-with-32-bytes-random-string!!
```

```bash
# 生成强随机密钥
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

**讲解：**

1. `envFilePath: [".env.local", ".env"]` 保证本地覆盖优先；每人一个 `.env.local`，互不踩脚，团队默认值沉淀在 `.env`。
2. `.env.example` 是"配置的接口文档"，配合第 3 节的启动校验形成闭环：缺什么、错什么，启动时全部告诉你。

## 6. 生产配置要点

1. 密钥不入库：`JWT_SECRET`、数据库密码等只存在于密钥管理系统或平台注入；git 历史无法靠删除提交挽回，一旦泄露必须轮换密钥。
2. 生产环境关闭 env 文件读取，只认平台注入：

```typescript
// src/app.module.ts（节选）
ConfigModule.forRoot({
  isGlobal: true,
  ignoreEnvFile: process.env.NODE_ENV === "production", // 生产只认真实环境变量
  validate
})
```

3. 最小权限与凭证分离：数据库账号、对象存储凭证分开发放，一份泄露不至于全盘失守。
4. 敏感配置不进日志：拦截器、过滤器里打印配置前先做掩码（如只保留后 4 位）；校验失败报错只含字段名，不含值。
5. 配置变更要有记录：平台注入的变量随部署清单（docker-compose、Helm values、CI 变量组）进版本库，形成"配置即代码"，可审计、可回滚。

## 7. 小结与延伸

- 配置体系三板斧：命名空间（registerAs）管组织、zod 校验管正确性、类型化门面管开发体验。
- fail fast 是配置校验的灵魂：坏配置撑不过启动那一秒，比运行时偶发 500 便宜得多。
- 环境分层口诀：example 进库、local 覆盖、生产注入、密钥轮换。
- 延伸：validate 函数也可用 class-validator + `plainToInstance` 或 Joi 实现，思路相同；NestJS 12 的 Standard Schema 集成与 Configuration 自定义 getter 的进阶写法，以官方文档为准。

<!-- ============================================================ nestjs/009-CachingAndQueues ============================================================ -->

## 0. 什么时候需要它们（先读这里）

> 学习目标：判断应用何时需要缓存与队列；会用 CacheModule 与自定义拦截器做响应缓存，理解 TTL 与 key 设计；会用 @nestjs/bullmq 落地异步任务：注册队列、入队、消费、重试退避与延迟任务。

单机 CRUD 撑不到生产规模，本章对症下药：

| 症状 | 药方 | 本章小节 |
| --- | --- | --- |
| 同一列表每秒被查几十次，数据库 CPU 居高 | 响应缓存 | 1 |
| 导出报表、发邮件拖慢接口响应 | BullMQ 队列 | 2-3 |
| 多个应用重复实现同一套逻辑 | 微服务（见下一篇） | - |

共同点：两者都打破了"请求-响应同步完成"的假设，需要为失败重试、数据一致性支付额外复杂度。先确认真的需要，再引入。

## 1. 响应缓存：CacheModule 与拦截器

```bash
npm i @nestjs/cache-manager cache-manager
```

```typescript
// src/app.module.ts
import { CacheModule } from "@nestjs/cache-manager"

@Module({
  imports: [
    CacheModule.register({
      ttl: 60_000 // 默认过期时间 60 秒（毫秒）；默认内存存储
    })
  ]
})
export class AppModule {}
```

注入 `Cache` 手动缓存 Todo 列表，写操作后主动失效：

```typescript
// src/todos/todos.service.ts
import { Inject, Injectable } from "@nestjs/common"
import { CACHE_MANAGER, Cache } from "@nestjs/cache-manager"
import { PrismaService } from "../prisma/prisma.service"
import { CreateTodoDto } from "./dto/create-todo.dto"

@Injectable()
export class TodosService {
  constructor(
    private readonly prisma: PrismaService,
    @Inject(CACHE_MANAGER) private readonly cache: Cache
  ) {}

  async findAll() {
    const cached = await this.cache.get("todos:all")
    if (cached) return cached // 命中：不再查库
    const todos = await this.prisma.todo.findMany({
      orderBy: { createdAt: "desc" }
    })
    await this.cache.set("todos:all", todos, 60_000)
    return todos
  }

  async create(dto: CreateTodoDto) {
    const todo = await this.prisma.todo.create({ data: { title: dto.title } })
    await this.cache.del("todos:all") // 写后删 key，避免脏读
    return todo
  }
}
```

key 必须把所有影响结果的参数编码进去：

| key 示例 | 含义 |
| --- | --- |
| `todos:all` | 全量列表 |
| `todos:page:1:size:20` | 分页列表，页码与页大小进 key |
| `todos:user:42` | 按用户隔离的数据，用户 id 进 key |

再给一个按路由自动缓存的拦截器，写法沿用守卫与拦截器一篇的 `NestInterceptor` 模式：

```typescript
// src/common/interceptors/http-cache.interceptor.ts
import {
  CallHandler,
  ExecutionContext,
  Injectable,
  NestInterceptor
} from "@nestjs/common"
import { CACHE_MANAGER, Cache } from "@nestjs/cache-manager"
import { Observable, of, tap } from "rxjs"

@Injectable()
export class HttpCacheInterceptor implements NestInterceptor {
  constructor(@Inject(CACHE_MANAGER) private readonly cache: Cache) {}

  async intercept(
    context: ExecutionContext,
    next: CallHandler
  ): Promise<Observable<any>> {
    const req = context.switchToHttp().getRequest()
    if (req.method !== "GET") return next.handle() // 只缓存 GET

    const key = `http:${req.originalUrl}` // 路径 + 查询串天然构成 key
    const cached = await this.cache.get(key)
    if (cached) return of(cached) // 命中：直接回放缓存

    return next.handle().pipe(
      tap((data) => this.cache.set(key, data, 30_000)) // 写缓存不阻塞响应
    )
  }
}

// 控制器按需挂载
@UseInterceptors(HttpCacheInterceptor)
@Get()
findAll() {
  return this.todosService.findAll()
}
```

**讲解：**

1. 默认内存存储重启即失、多实例不共享；生产换 Redis 存储（@nestjs/cache-manager 配合 Keyv 系适配器），各版本配置差异以官方文档为准。
2. 两种方案选一即可：拦截器按 URL 全自动化，手动方案能精确控制 key 与失效时机；有分页、按人隔离等复杂 key 时推荐手动。
3. 失效策略从简：写操作直接删 key（cache-aside 模式），比"顺手更新缓存"更不容易出错。

## 2. BullMQ 队列：注册、生产者与消费者

```bash
npm i @nestjs/bullmq bullmq ioredis
```

```typescript
// src/app.module.ts
import { BullModule } from "@nestjs/bullmq"

@Module({
  imports: [
    BullModule.forRoot({
      connection: { host: "localhost", port: 6379 } // Redis 连接全局复用
    }),
    BullModule.registerQueue({ name: "email" }) // 队列名即契约
  ]
})
export class AppModule {}
```

生产者：接口只负责入队，立即返回 202：

```typescript
// src/email/email.service.ts
import { Inject, Injectable } from "@nestjs/common"
import { InjectQueue } from "@nestjs/bullmq"
import { Queue } from "bullmq"

export interface EmailJob {
  to: string
  subject: string
  body: string
}

@Injectable()
export class EmailService {
  constructor(
    @InjectQueue("email") private readonly emailQueue: Queue<EmailJob>
  ) {}

  async sendWelcome(to: string) {
    await this.emailQueue.add(
      "welcome", // 任务名
      { to, subject: "欢迎注册", body: "..." },
      {
        attempts: 5, // 最多尝试 5 次
        backoff: { type: "exponential", delay: 3000 }, // 间隔 3s、6s、12s、24s、48s
        removeOnComplete: 100, // 完成记录最多保留 100 条，防 Redis 膨胀
        removeOnFail: 1000
      }
    )
  }
}
```

消费者：

```typescript
// src/email/email.processor.ts
import { Logger } from "@nestjs/common"
import { Processor, WorkerHost } from "@nestjs/bullmq"
import { Job } from "bullmq"
import { EmailJob } from "./email.service"

@Processor("email", { concurrency: 5 }) // 同时处理 5 个任务
export class EmailProcessor extends WorkerHost {
  private readonly logger = new Logger(EmailProcessor.name)

  async process(job: Job<EmailJob>): Promise<void> {
    this.logger.log(`任务 ${job.id} 第 ${job.attemptsMade + 1} 次尝试`)
    await mailer.send(job.data) // 抛异常 = 本轮失败，BullMQ 按策略重试
  }
}

// EmailModule 的 providers 中注册 EmailProcessor
```

**讲解：**

1. 队列的价值：把"慢且可能失败"的操作移出请求-响应周期，接口耗时从 3 秒降到 20 毫秒，失败还能自动重试。
2. `attempts + backoff` 是可靠性下限：瞬时故障（网络抖动、下游限流）靠指数退避自愈；反复失败最终进入 failed 集合，留给人处理。
3. `job.data` 必须可 JSON 序列化：只传 id 等引用，消费者自己查库取最新数据，避免把大对象塞进 Redis。

## 3. 延迟任务与消费可靠性

```typescript
// 24 小时后发送回访邮件
await this.emailQueue.add(
  "follow-up",
  { to, subject: "使用得怎么样？" },
  { delay: 24 * 60 * 60 * 1000 }
)
```

任务状态机：

| 状态 | 含义 | 去向 |
| --- | --- | --- |
| waiting | 排队中 | active |
| active | 消费中 | completed / failed（重试回 waiting） |
| delayed | 等待触发时间 | 到期转 waiting |
| failed | 重试次数耗尽 | 人工介入 |

```typescript
// 队列事件监听：失败告警的最简实现
this.emailQueue.on("failed", (job, err) => {
  this.logger.error(`任务 ${job?.id} 失败：${err.message}`)
})
```

**讲解：**

1. delay 任务先进入 delayed 集合，到期自动转 waiting；状态存在 Redis，应用重启不丢任务。
2. 重试由"消费者抛异常"触发；对参数错误等重试无意义的失败，抛 `UnrecoverableError` 可跳过剩余重试。
3. 幂等是消费前提：重试意味着任务可能已执行过一半，写库操作用唯一键约束兜底，避免重复发货类事故。
4. 单元测试建议：直接测试 Processor 的 `process` 方法（传入伪造 Job），队列行为本身交给集成环境验证，与测试一篇的分层思路一致。

## 4. 小结与延伸

- 缓存救读压力：TTL 控制新鲜度、key 编码全部查询参数、写后删 key（cache-aside）。
- 队列救写延迟：`forRoot` 连接、`registerQueue` 声明、`add` 入队、`@Processor` 消费；重试退避保瞬时故障，幂等保最终一致。
- 两者都引入新的失败模式：先量化症状（QPS、耗时、失败率），再决定引入。
- 延伸：Bull Board 面板可视化队列积压；缓存穿透与雪崩的应对（空值缓存、随机 TTL）；微服务与健康检查见下一篇。

<!-- ============================================================ nestjs/010-MicroservicesAndHealth ============================================================ -->

## 0. 从单应用到多应用（先读这里）

> 学习目标：理解 NestJS 微服务"同一套代码换传输层"的设计；会用 @MessagePattern 与 @EventPattern 编写消息处理器，用 ClientProxy 发起调用；为应用接入 @nestjs/terminus 健康检查；了解 NestJS 12 的 ESM 与 Standard Schema 变化。

上一篇解决了单应用的读压力（缓存）与慢操作（队列），当问题变成"多个应用重复实现同一套逻辑"时，才轮到微服务。拆分顺序有讲究：先在同一仓库里拆清模块边界、用队列通信，边界稳定后再拆进程——传输层可插拔正是 NestJS 的底气。

## 1. 微服务传输层概览

```bash
npm i @nestjs/microservices
```

```typescript
// src/main.ts —— 服务端：HTTP 与微服务可共存
const app = await NestFactory.create(AppModule)
app.connectMicroservice({ transport: Transport.TCP, options: { port: 3001 } })
await app.startAllMicroservices()
await app.listen(3000) // HTTP 路由照常工作
```

```typescript
// src/todos/todos.controller.ts —— 消息处理器
@MessagePattern({ cmd: "todos.list" }) // 请求-响应：有返回值
list() {
  return this.todosService.findAll()
}

@EventPattern("todo.created") // 事件：发后即忘，不等待返回
onTodoCreated(data: { title: string }) {
  this.logger.log(`待办创建：${data.title}`)
}
```

传输层选型：

| 传输层 | 模式 | 优势 | 适用场景 |
| --- | --- | --- | --- |
| TCP | 请求-响应 | 零外部依赖 | 单机联调、起步 |
| Redis | 发布订阅 | 轻量、上手快 | 中小规模任务分发 |
| NATS | 请求-响应/发布订阅 | 极轻、低延迟 | 服务发现与内部总线 |
| Kafka | 持久化日志订阅 | 高吞吐、可回放 | 事件流、审计、日志管道 |
| gRPC | 请求-响应 | 强类型契约、跨语言 | 多语言团队、低延迟调用 |
| RabbitMQ | 发布订阅 | AMQP 成熟、路由强 | 复杂任务路由 |

**讲解：**

1. `@MessagePattern` 对应 RPC（有响应），`@EventPattern` 对应事件（无响应），语义与消息队列的两种交互一一对应。
2. pattern 可以是字符串也可以是 JSON 对象（如 `{ cmd: "todos.list" }`），对象式便于按域组织、避免命名冲突。
3. 换传输层只改 `connectMicroservice` 的配置与客户端注入，业务代码不动——这就是传输层可插拔。
4. 事件处理器内部抛异常不会通知发布方（事件本来就是发后即忘），可靠性依赖消费端重试与死信处理。
5. 一个进程可以 `connectMicroservice` 多个传输层（TCP 加 Kafka），`startAllMicroservices()` 会把它们全部启动，适合过渡期的双轨运行。

## 2. 客户端调用：ClientProxy

```typescript
// src/app.module.ts —— 注册指向 todos 服务的客户端
import { ClientsModule, Transport } from "@nestjs/microservices"

@Module({
  imports: [
    ClientsModule.register([
      {
        name: "TODOS_CLIENT", // 注入令牌
        transport: Transport.TCP,
        options: { host: "localhost", port: 3001 }
      }
    ])
  ]
})
export class AppModule {}
```

```typescript
// src/report/report.service.ts —— 另一个应用里发起调用
import { Inject, Injectable } from "@nestjs/common"
import { ClientProxy } from "@nestjs/microservices"
import { firstValueFrom, timeout, catchError, throwError } from "rxjs"

@Injectable()
export class ReportService {
  constructor(
    @Inject("TODOS_CLIENT") private readonly client: ClientProxy
  ) {}

  async countTodos() {
    return firstValueFrom(
      this.client.send({ cmd: "todos.list" }, {}).pipe(
        timeout(5000), // 远程调用必须设超时，防止无限等待
        catchError((err) =>
          throwError(() => new Error(`调用 todos 服务失败：${err.message}`))
        )
      )
    )
  }

  notifyTodoCreated(todo: { title: string }) {
    // emit 发布事件，不等待响应，返回的 Observable 无需订阅即已发送
    this.client.emit("todo.created", todo)
  }
}
```

**讲解：**

1. `send` 请求-响应、`emit` 发后即忘，与 `@MessagePattern` / `@EventPattern` 成对出现。
2. `send` 返回的是 Observable：可以 `timeout`、`retry`、`catchError`，远程调用按"必然失败"设计，超时与降级是标配。
3. `ClientsModule.register` 的 `name` 就是注入令牌；每个微服务模块也可以在自己的模块里 `ClientsModule.registerAsync` 按需注册。

## 3. 健康检查：@nestjs/terminus

```bash
npm i @nestjs/terminus
```

```typescript
// src/health/health.controller.ts
import { Controller, Get } from "@nestjs/common"
import {
  HealthCheck,
  HealthCheckService,
  MemoryHealthIndicator
} from "@nestjs/terminus"
import { PrismaService } from "../prisma/prisma.service"

@Controller("health")
export class HealthController {
  constructor(
    private readonly health: HealthCheckService,
    private readonly memory: MemoryHealthIndicator,
    private readonly prisma: PrismaService
  ) {}

  @Get()
  @HealthCheck()
  check() {
    return this.health.check([
      // 堆内存超过 512MB 视为不健康
      () => this.memory.checkHeap("memory_heap", 512 * 1024 * 1024),
      // 自定义指示器：跑一条最轻的 SQL 确认数据库连接可用
      async () => {
        await this.prisma.$queryRaw`SELECT 1`
        return { database: { status: "up" } }
      }
    ])
  }
}
```

**讲解：**

1. 响应形如 `{ status: "ok", info: { memory_heap: {...}, database: {...} } }`；任一指示器失败则整体 `status: "error"` 并返回 503。
2. 用途直接：K8s 的 liveness/readiness 探针指向 `GET /health`，负载均衡按它摘除不健康实例，发布流水线用它做前置检查。
3. 健康检查要"轻"：只验证关键依赖的连通性（一条 `SELECT 1` 即可），不要在探针里做重查询，否则探针本身会拖垮服务。
4. 自定义指示器在 NestJS 11 起推荐基于 `HealthIndicatorService` 编写，与 Prisma、TypeORM 的现成指示器用法以官方文档为准。

## 4. NestJS 12：ESM 与 Standard Schema

2026 年的版本事实：

| 事项 | 现状 |
| --- | --- |
| 框架版本 | NestJS 12 已发布（ESM-ready、原生支持 Standard Schema），11 仍被广泛使用 |
| 运行时 | 推荐 Node.js 22 LTS |
| 语言 | TypeScript 5.x |
| ESM | 核心包提供 ESM 导出，存量 CJS 项目可渐进迁移 |
| Standard Schema | ValidationPipe 等可直接消费 zod、valibot、arktype 等实现 |

**讲解：**

1. ESM-ready 指包同时提供 CJS 与 ESM 双导出：新项目可直接用 ESM；存量项目不要在业务高峰期顺带做 ESM 改造，单独排期。
2. Standard Schema 是校验库的统一接口标准：配合《配置与环境变量校验》一篇的 zod schema，配置校验与 DTO 校验可以共享同一套 schema；团队已在用 class-validator 的不必急于更换。
3. 升级策略：按官方迁移指引（Migrations to v12）在 CI 里先行验证，重点核对 RxJS、cache-manager、bullmq 等外围包的版本配套；细节以官方文档为准。

## 5. 动手试试

1. 把 `connectMicroservice` 的 `Transport.TCP` 换成 `Transport.REDIS`，服务端与客户端同步修改，用 `redis-cli MONITOR` 观察 payload 的收发。
2. 制造故障演练：停掉 todos 服务再调用 `countTodos`，验证 `timeout + catchError` 的降级输出，确认接口不再无限等待。
3. 用 Docker 起一个 Redis 供缓存与队列共用，把 `GET /health` 配进负载均衡探针，观察任一依赖宕机后返回的 `status: "error"` 结构。

## 6. 小结与延伸

- 微服务先拆模块边界再拆进程；`@MessagePattern` 管 RPC、`@EventPattern` 管事件，传输层可插拔。
- 远程调用三件套：超时、降级、幂等，缺一不可。
- 健康检查是上生产前的最后一道自检：探针要轻、指标要真、对接 K8s 或负载均衡。
- 延伸：混合应用（HTTP + 微服务共存）的官方示例；gRPC proto 文件与 Nest 的结合；NATS 的队列组实现负载均衡消费。
