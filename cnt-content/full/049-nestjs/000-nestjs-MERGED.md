---
order: 10
title: nestjs 模块文档合集
module: 'nestjs'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：049-nestjs/001-NestJSOverview.md ============ -->


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



<!-- ============ 文档分隔线：049-nestjs/002-ModuleControllerService.md ============ -->


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



<!-- ============ 文档分隔线：049-nestjs/003-ValidationPipes.md ============ -->


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



<!-- ============ 文档分隔线：049-nestjs/004-DatabaseIntegration.md ============ -->


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



<!-- ============ 文档分隔线：049-nestjs/005-Testing.md ============ -->


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
