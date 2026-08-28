---
order: 40
title: Angular 依赖注入与 HTTP 服务
module: 'angular'
category: 前端技术
difficulty: intermediate
description: inject() 函数、providedIn 作用域、HttpClient 请求与错误处理，把 API 调用收进可测试服务。
author: fanquanpp
updated: '2026-08-03'
related:
  - 'angular/003-SignalsInputsOutputs'
  - 'angular/005-RoutingForms'
prerequisites:
  - 'angular/003-SignalsInputsOutputs'
---

## 0. 一句话理解

> 依赖注入（DI）就是"要用什么服务，声明一下，框架给你实例"：`inject()` 一行代码拿到 HttpClient，服务类统一封装 API。

## 1. 创建服务

```bash
ng generate service data/todo
```

```typescript
// src/app/data/todo.service.ts
import { HttpClient } from "@angular/common/http"
import { Injectable, inject } from "@angular/core"

export interface Todo {
  id: number
  title: string
  done: boolean
}

@Injectable({ providedIn: "root" })
export class TodoService {
  private http = inject(HttpClient)
  private baseUrl = "https://jsonplaceholder.typicode.com/todos"

  list() {
    return this.http.get<Todo[]>(this.baseUrl)
  }

  create(title: string) {
    return this.http.post<Todo>(this.baseUrl, { title, done: false })
  }
}
```

**讲解：**

1. `@Injectable({ providedIn: "root" })` 声明服务是全局单例：任何组件注入的都是同一个实例。
2. `inject(HttpClient)` 是函数式注入（Angular 14+），替代旧版构造器注入。
3. `http.get<Todo[]>` 的泛型让响应自动获得类型：返回的是 Observable，组件订阅后得到 `Todo[]`。

## 2. 组件中使用服务

```typescript
import { Component, inject, signal } from "@angular/core"
import { TodoService, Todo } from "../data/todo.service"
import { firstValueFrom } from "rxjs"

@Component({
  selector: "app-todo-list",
  template: `
    @for (todo of todos(); track todo.id) {
      <p>{{ todo.id }}. {{ todo.title }}</p>
    }
  `
})
export class TodoListComponent {
  private todoService = inject(TodoService)
  todos = signal<Todo[]>([])

  constructor() {
    this.load()
  }

  async load() {
    const list = await firstValueFrom(this.todoService.list())
    this.todos.set(list)
  }
}
```

**讲解：**

1. `inject(TodoService)` 在字段初始化处注入服务，组件里直接用 `this.todoService`。
2. `firstValueFrom()` 把 Observable 转成 Promise，配合 `async/await` 更符合现代习惯。
3. 拿到结果后 `todos.set(list)` 更新信号，模板自动刷新。

## 3. 错误处理

```typescript
import { catchError, throwError } from "rxjs"

list() {
  return this.http.get<Todo[]>(this.baseUrl).pipe(
    catchError((error) => {
      console.error("加载待办失败：", error)
      return throwError(() => new Error("服务暂不可用，请稍后重试"))
    })
  )
}
```

**讲解：**

1. `.pipe(catchError(...))` 拦截 HTTP 错误流，统一记录日志并转换为用户可读的错误。
2. `throwError(() => new Error(...))` 重新抛出错误，调用方可以在 `try/catch` 里处理。
3. 生产项目通常再封装一层 `ApiService`：统一处理 401 跳登录、429 重试、错误消息格式化。

## 4. 服务单例与测试

```typescript
// todo.service.spec.ts
import { TestBed } from "@angular/core/testing"
import { HttpClientTestingModule, HttpTestingController } from "@angular/common/http/testing"
import { TodoService } from "./todo.service"

describe("TodoService", () => {
  let service: TodoService
  let httpMock: HttpTestingController

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    })
    service = TestBed.inject(TodoService)
    httpMock = TestBed.inject(HttpTestingController)
  })

  it("list 返回待办数组", async () => {
    const promise = firstValueFrom(service.list())
    const req = httpMock.expectOne("https://jsonplaceholder.typicode.com/todos")
    req.flush([{ id: 1, title: "测试", done: false }])
    const data = await promise
    expect(data.length).toBe(1)
  })
})
```

**讲解：**

1. `HttpClientTestingModule` 提供假的 HTTP 后端，测试不会发出真实网络请求。
2. `httpMock.expectOne(url)` 断言"恰好发了一次该请求"，`req.flush(假数据)` 返回模拟响应。
3. 用 `TestBed.inject` 拿到被测服务与假后端，这是 Angular 官方推荐的测试模式。

## 5. 动手试试

1. 给 `TodoService` 增加 `update(id, done)` 与 `remove(id)` 方法并接入组件。
2. 在组件里加载时显示"加载中"，失败时显示错误信息。
3. 写一个 `list` 的单元测试：断言请求 URL 与 HTTP 方法（`req.request.method === "GET"`）。

## 6. 一句话记住

> API 调用全部收进 `@Injectable` 服务，组件用 `inject()` 取用；Observable 配 `firstValueFrom` 最省心，测试用 `HttpTestingController` 拦截请求。
