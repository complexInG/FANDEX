---
order: 10
title: angular 模块文档合集
module: 'angular'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-30'
related: []
prerequisites: []
---

<!-- ============================================================ angular/001-AngularOverview ============================================================ -->

## 0. 五分钟创建第一个应用（先读这里）

> 学习目标：用 Angular CLI 创建项目，理解组件三件套（模板、类、样式）。

```bash
npm i -g @angular/cli
ng new my-app --style css --ssr false
cd my-app
ng serve
```

**讲解：**

1. `ng new` 创建项目并自动安装依赖；`--ssr false` 先关闭服务端渲染，入门更简单。
2. `ng serve` 启动开发服务器（默认 `http://localhost:4200`），改代码自动热更新。
3. 页面内容来自 `src/app/app.component.html`，打开改一行文字即可看到效果。

## 1. Angular 是什么

Angular 是 Google 维护的企业级前端框架，2016 年发布（Angular 2，与 AngularJS 完全不同）。它提供完整解决方案：组件、模板、依赖注入、路由、表单、HTTP、测试，团队无需拼装多个库。

### 1.1 版本现状（2026-08）

- Angular 22 为当前稳定版（2026-06 发布）：Signal Forms 与异步响应式 API 转正，新项目默认 zoneless（无 Zone.js）。
- 新项目由 `ng new` 自动生成：standalone 组件 + Signal + zoneless 是当前推荐形态。
- 学习建议：先掌握组件与模板，再学信号（Signals）、路由、表单、依赖注入。

## 2. 组件三件套

```typescript
// src/app/app.component.ts
import { Component } from "@angular/core"

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"]
})
export class AppComponent {
  title = "我的 Angular 应用"
}
```

```html
<!-- src/app/app.component.html -->
<main>
  <h1>{{ title }}</h1>
  <p>Angular 22 快速上手</p>
</main>
```

**讲解：**

1. `@Component` 装饰器把类变成组件：`selector` 是组件标签名，`templateUrl` 指向 HTML 模板，`styleUrls` 指向样式。
2. 模板里的 `{{ title }}` 是插值表达式：输出类的 `title` 属性。
3. 一个组件 = 类（数据与逻辑）+ 模板（HTML）+ 样式（CSS），三者按约定放同一目录。

## 3. 组件树与独立组件

```typescript
// src/app/app.component.ts（片段）
import { Component } from "@angular/core"
import { HeaderComponent } from "./header/header.component"

@Component({
  selector: "app-root",
  imports: [HeaderComponent],   // standalone 组件显式声明依赖
  templateUrl: "./app.component.html"
})
export class AppComponent {}
```

```html
<app-header />
<main>页面主体</main>
```

**讲解：**

1. Angular 17+ 的 standalone 组件在 `imports` 数组里显式声明要用的其他组件，不再需要 NgModule 包装。
2. 模板里用 `<app-header />` 标签渲染子组件——应用是一棵组件树，根组件在 `main.ts` 里启动。
3. 组件通信：属性输入（input）从父到子，输出事件（output）从子到父，下一章详解。

## 4. 动手试试

1. 修改 `app.component.html`，加一个 `<input>` 与按钮，把输入内容用 `{{ }}` 显示出来。
2. 用 `ng generate component header` 生成头部组件，在根组件中引入并渲染。
3. 运行 `ng serve`，打开浏览器 DevTools 确认无控制台错误。

## 5. 一句话记住

> Angular = 组件树 + 模板绑定 + 依赖注入；22 版新项目默认 standalone、Signal、无 Zone.js，用 `ng new` 起步即可。

<!-- ============================================================ angular/002-QuickStartComponentTemplate ============================================================ -->

## 0. 一句话理解

> Angular 模板 = HTML + 绑定：`{{ }}` 输出、`[属性]` 输入、`(事件)` 输出，`@if/@for` 做条件与循环。

## 1. 属性绑定

```typescript
export class AppComponent {
  imageUrl = "https://angular.dev/assets/images/favicon.svg"
  isDisabled = true
}
```

```html
<img [src]="imageUrl" alt="Angular 图标" />
<button [disabled]="isDisabled">不可点</button>
```

**讲解：**

1. `[src]="imageUrl"` 是属性绑定：把类的属性值传给 DOM 属性；不加方括号的 `src="imageUrl"` 是字面字符串。
2. `[disabled]` 绑定布尔值，`true` 时按钮禁用。
3. 需要同时拼多个 class 时用 `[class.active]="condition"` 或 `[ngClass]="对象"`。

## 2. 事件绑定

```typescript
export class AppComponent {
  count = 0

  add() {
    this.count += 1
  }

  onInput(event: Event) {
    const value = (event.target as HTMLInputElement).value
    console.log("输入了：", value)
  }
}
```

```html
<p>点击次数：{{ count }}</p>
<button (click)="add()">加一</button>
<input (input)="onInput($event)" placeholder="输入点什么" />
```

**讲解：**

1. `(click)="add()"` 是事件绑定：点击按钮时调用组件方法。
2. `$event` 是事件对象，`onInput($event)` 把原生事件传给方法。
3. 注意方法里必须写 `this.count += 1`——Angular 类的属性访问都要通过 `this`。

## 3. @if 与 @for 控制流

```typescript
export class AppComponent {
  loggedIn = false
  todos = ["学模板", "学信号", "学路由"]
}
```

```html
@if (loggedIn) {
  <p>欢迎回来</p>
} @else {
  <button (click)="loggedIn = true">登录</button>
}

<ul>
  @for (todo of todos; track todo) {
    <li>{{ todo }}</li>
  } @empty {
    <li>暂无待办</li>
  }
</ul>
```

**讲解：**

1. `@if/@else` 是 Angular 17+ 的新控制流语法，取代旧版 `*ngIf`，性能更好、可读性更强。
2. `@for` 遍历数组，`track todo` 提供稳定标识（类似 React 的 key），列表重排时复用 DOM。
3. `@empty` 是数组为空时显示的分支，不需要再写一个 `@if`。

## 4. 表单输入与双向绑定

```html
<input
  [value]="keyword"
  (input)="keyword = $any($event.target).value"
/>
<p>搜索：{{ keyword }}</p>
```

```typescript
export class AppComponent {
  keyword = ""
}
```

**讲解：**

1. 属性绑定 + 事件绑定组合就是"受控输入"：输入事件把值写回组件属性。
2. 模板里直接给组件属性赋值是合法的（`keyword = ...`），Angular 会自动触发变更检测。
3. 进阶写法是 `[(ngModel)]`（需要 FormsModule）或 Angular 22 的 Signal Forms，下一章介绍。

## 5. 动手试试

1. 做一个待办列表：输入框 + 添加按钮，用 `@for` 渲染，点条目删除。
2. 用 `[class.done]="todo.done"` 给已完成条目加删除线样式。
3. 用 `@empty` 分支显示"暂无待办"。

## 6. 一句话记住

> 模板就是"类属性与页面之间的接线板"：`[属性]` 进、`(事件)` 出、`@if/@for` 控制结构。

<!-- ============================================================ angular/003-SignalsInputsOutputs ============================================================ -->

## 0. 一句话理解

> 信号（Signal）是 Angular 的"响应式状态单元"：`signal()` 存值、`computed()` 派生、`effect()` 监听；组件通信用 `input/output/model` 三个函数。

## 1. signal 与 computed

```typescript
import { Component, computed, signal } from "@angular/core"

@Component({
  selector: "app-price",
  template: `
    <p>单价：{{ price() }}</p>
    <p>数量：{{ qty() }}</p>
    <p>合计：{{ total() }}</p>
    <button (click)="qty.set(qty() + 1)">加一</button>
  `
})
export class PriceComponent {
  price = signal(100)
  qty = signal(2)
  total = computed(() => this.price() * this.qty())
}
```

**讲解：**

1. `signal(100)` 创建信号，读取必须调用 `price()`，更新用 `.set(新值)` 或 `.update(旧值 => 新值)`。
2. `computed(() => ...)` 创建派生信号：内部读取 `price()` 与 `qty()`，任一变化时自动重算。
3. 模板里直接调用 `total()`，Angular 只重渲染依赖变化的节点，这是信号性能优势的来源。

## 2. 副作用 effect

```typescript
import { Component, effect, signal } from "@angular/core"

@Component({
  selector: "app-log",
  template: `<input [value]="keyword()" (input)="onInput($event)" />`
})
export class LogComponent {
  keyword = signal("")

  constructor() {
    effect(() => {
      console.log("搜索词变化：", this.keyword())
    })
  }

  onInput(event: Event) {
    this.keyword.set((event.target as HTMLInputElement).value)
  }
}
```

**讲解：**

1. `effect` 在组件创建时执行一次，之后每当内部读取的信号变化就重新执行。
2. 适用场景：日志上报、localStorage 同步、与第三方非响应式库对接。
3. 不要在 `effect` 里直接修改其他信号，容易造成循环依赖；写入类操作应放在事件处理器里。

## 3. input 与 output：父子通信

```typescript
// src/app/todo-item/todo-item.component.ts
import { Component, input, output } from "@angular/core"

export interface Todo {
  id: number
  title: string
  done: boolean
}

@Component({
  selector: "app-todo-item",
  template: `
    <li>
      <input type="checkbox" [checked]="todo().done" (change)="onToggle()" />
      {{ todo().title }}
      <button (click)="onRemove()">删除</button>
    </li>
  `
})
export class TodoItemComponent {
  todo = input.required<Todo>()
  toggle = output()
  remove = output()

  onToggle() {
    this.toggle.emit()
  }

  onRemove() {
    this.remove.emit()
  }
}
```

**讲解：**

1. `input.required<Todo>()` 声明必填输入属性，父组件通过 `[todo]="..."` 传入。
2. `output()` 声明事件，子组件用 `this.toggle.emit()` 通知父组件。
3. 模板里调用 `todo().done` 读输入信号；`input.required` 保证使用方不传时编译报错。

## 4. 父组件用法

```typescript
@Component({
  selector: "app-list",
  imports: [TodoItemComponent],
  template: `
    @for (item of todos(); track item.id) {
      <app-todo-item
        [todo]="item"
        (toggle)="onToggle(item.id)"
        (remove)="onRemove(item.id)"
      />
    }
  `
})
export class ListComponent {
  todos = signal<Todo[]>([
    { id: 1, title: "学信号", done: false },
    { id: 2, title: "学路由", done: false }
  ])

  onToggle(id: number) {
    this.todos.update((list) =>
      list.map((t) => (t.id === id ? { ...t, done: !t.done } : t))
    )
  }

  onRemove(id: number) {
    this.todos.update((list) => list.filter((t) => t.id !== id))
  }
}
```

**讲解：**

1. `(toggle)="onToggle(item.id)"` 监听子组件事件，事件名与子组件的 `output()` 名一致。
2. `todos.update((list) => list.map(...))` 用不可变更新替换数组，返回新数组触发视图刷新。
3. 数据流保持单向：子组件不直接改父组件数据，只发事件。

## 5. 动手试试

1. 给 Todo 增加 `model<boolean>()` 双向绑定复选框（Angular 17.2+ 的 `model` 信号）。
2. 用 `computed` 派生"未完成数量"并显示在标题。
3. 把添加待办的输入框做成独立组件，通过 `output` 把新标题传给父组件。

## 6. 一句话记住

> 信号管状态（signal/computed/effect），`input/output/model` 管通信；数据单向流动，父组件是唯一改数据的入口。

<!-- ============================================================ angular/004-DependencyInjectionServices ============================================================ -->

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

<!-- ============================================================ angular/005-RoutingForms ============================================================ -->

## 0. 一句话理解

> 路由 = 把 URL 映射到组件：`RouterOutlet` 是页面出口，`provideRouter` 声明映射；响应式表单 = 用 FormGroup/FormControl 描述表单结构并校验。

## 1. 配置路由

```typescript
// src/app/app.config.ts（片段）
import { provideRouter, withComponentInputBinding } from "@angular/router"
import { routes } from "./app.routes"

export const appConfig = {
  providers: [provideRouter(routes, withComponentInputBinding())]
}
```

```typescript
// src/app/app.routes.ts
import { Routes } from "@angular/router"

export const routes: Routes = [
  { path: "", redirectTo: "/todos", pathMatch: "full" },
  {
    path: "todos",
    loadComponent: () =>
      import("./todos/todos.component").then((m) => m.TodosComponent)
  },
  { path: "**", redirectTo: "/todos" }
]
```

**讲解：**

1. `Routes` 数组声明 URL 与组件的映射：`path` 是路径，`redirectTo` 重定向，`**` 是兜底 404。
2. `loadComponent: () => import(...)` 实现懒加载：该路由被访问时才下载对应组件代码，首屏更快。
3. `withComponentInputBinding()` 让路由参数自动绑定到组件 input（如 `[id]` 对应 `id = input()`）。

## 2. 路由出口与导航

```html
<!-- src/app/app.component.html -->
<nav>
  <a routerLink="/todos" routerLinkActive="active">待办</a>
  <a routerLink="/about">关于</a>
</nav>
<router-outlet />
```

**讲解：**

1. `<router-outlet />` 是页面出口：当前路由对应的组件渲染在这里。
2. `routerLink` 是声明式导航，`routerLinkActive="active"` 在当前路由匹配时自动加类名。
3. 编程式跳转在组件里 `inject(Router).navigate(["/todos"])`。

## 3. 路由守卫

```typescript
// src/app/guards/auth.guard.ts
import { inject } from "@angular/core"
import { CanActivateFn, Router } from "@angular/router"

export const authGuard: CanActivateFn = () => {
  const router = inject(Router)
  const loggedIn = localStorage.getItem("token") !== null

  if (!loggedIn) {
    router.navigate(["/login"])
    return false
  }
  return true
}
```

```typescript
// 路由配置中挂载守卫
{
  path: "todos",
  canActivate: [authGuard],
  loadComponent: () => import("./todos/todos.component").then((m) => m.TodosComponent)
}
```

**讲解：**

1. `CanActivateFn` 是函数式守卫：返回 `true` 放行，`false` 拦截并跳转登录页。
2. 真实项目用 AuthService 判断登录态，而不是直接读 localStorage。
3. 守卫适合"未登录拦截"，数据级权限应在 API 服务端校验，不能只靠前端。

## 4. 响应式表单

```typescript
import { Component, inject } from "@angular/core"
import { FormBuilder, ReactiveFormsModule, Validators } from "@angular/forms"

@Component({
  selector: "app-create-todo",
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="submit()">
      <input formControlName="title" placeholder="待办标题" />
      @if (form.controls.title.invalid && form.controls.title.touched) {
        <p class="error">标题必填，最长 100 字</p>
      }
      <button [disabled]="form.invalid">保存</button>
    </form>
  `
})
export class CreateTodoComponent {
  private fb = inject(FormBuilder)

  form = this.fb.group({
    title: ["", [Validators.required, Validators.maxLength(100)]]
  })

  submit() {
    if (this.form.invalid) return
    console.log("提交：", this.form.value.title)
  }
}
```

**讲解：**

1. `FormBuilder.group` 定义表单结构，`Validators.required/maxLength` 声明校验规则。
2. `formControlName="title"` 把输入框与表单控件绑定；`formGroup` 绑定整个表单。
3. `form.controls.title.invalid && touched` 在用户碰过且无效时才显示错误，避免一进页面就报红。
4. `[disabled]="form.invalid"` 让无效表单不可提交；`ngSubmit` 在提交时调用 `submit()`。

## 5. 动手试试

1. 新增 `/login` 页面与 `loginForm`（用户名 + 密码必填），提交后写一个假 token 并跳转 `/todos`。
2. 给 `title` 增加"不能与已有待办重复"的自定义校验器（`Validators` 之外写一个返回 `{ duplicate: true }` 的函数）。
3. 用 `input.required<string>()` 接收路由参数 id，加载对应待办详情。

## 6. 一句话记住

> `provideRouter + RouterOutlet + routerLink` 三件套搞定导航；表单用 FormBuilder 声明结构，校验不过就禁用提交。

<!-- ============================================================ angular/006-AdvancedRoadmap ============================================================ -->

## 0. 你现在在哪里（先读这里）

> 学习目标：对照进阶路线，明确接下来三站要学什么、为什么按这个顺序学、每站学到什么程度算过关。

前五篇文档带你完成了 Angular 的入门闭环：认识框架与工具链（001）、
组件与模板（002）、Signals 信号体系（003）、依赖注入与服务（004）、
路由与表单（005）。到这里，你已经能搭出一个多页面、有表单、有服务层的
Angular 应用骨架。

本篇是通往精通阶段的路线图：把剩余的核心能力拆成三站。每一站给出
"要解决的问题 → 核心 API 清单 → 最小示例 → 常见陷阱 → 过关自检"，
后续版本会把每一站展开为独立文档（编号紧接本篇）。

## 1. 进阶路线总览

| 站点 | 主题 | 解决的问题 | 核心能力 |
| --- | --- | --- | --- |
| 第六站 | 指令与管道 | 模板怎么复用：行为复用与数据格式化 | 属性/结构指令、@if/@for、自定义管道 |
| 第七站 | HttpClient 与状态管理 | 数据怎么流：接口调用与信号化状态 | 拦截器、resource、computed、toSignal |
| 第八站 | 测试与 SSR 水合 | 质量与首屏：自动化测试与服务端渲染 | TestBed、@angular/ssr、水合 |

三站的关系：第六站解决"模板层的复用"，第七站解决"数据层的组织"，
第八站解决"交付质量"。顺序不可跳：指令与管道是模板写法的基础，
状态管理依赖信号（003 已学），SSR 则建立在完整应用之上。

## 2. 第六站：指令与管道

Angular 的模板复用分两条路：指令复用"行为"，管道复用"格式化"。

### 2.1 指令三分法

| 类型 | 装饰器 | 作用 | 例 |
| --- | --- | --- | --- |
| 组件 | @Component | 带模板的指令 | 页面、卡片 |
| 属性指令 | @Directive | 改变元素外观或行为 | 高亮、tooltip |
| 结构指令 | @Directive | 增删 DOM 改变布局 | *ngIf 的替代者 |

### 2.2 属性指令最小示例

```ts
@Directive({ selector: "[appHighlight]" })
export class HighlightDirective {
  // host 绑定：把宿主元素的颜色绑定到信号
  color = signal("transparent");
  host = { "[style.backgroundColor]": "color()" };

  constructor(private el: ElementRef) {}
  @HostListener("mouseenter") enter() { this.color.set("#39C5BB"); }
  @HostListener("mouseleave") leave() { this.color.set("transparent"); }
}
```

```html
<p appHighlight>鼠标移过来试试</p>
```

### 2.3 结构指令的原理

```ts
@Directive({ selector: "[appUnless]" })
export class UnlessDirective {
  private tpl = inject(TemplateRef);
  private vcr = inject(ViewContainerRef);

  @Input() set appUnless(cond: boolean) {
    if (!cond) this.vcr.createEmbeddedView(this.tpl);   // 条件成立才渲染
    else this.vcr.clear();
  }
}
```

**讲解：** 结构指令的本质是"拿到模板 + 手动决定挂不挂"——
理解了 TemplateRef/ViewContainerRef，`@if` 的新控制流语法就不再神秘。

### 2.4 新控制流与管道

- 控制流：`@if (cond) {...} @for (item of list; track item.id) {...}` 已是
  Angular 17+ 的推荐写法，`track` 决定列表 diff 的效率（对照 *ngIf/*ngFor 迁移）。
- 管道：内置 date/currency/number/json 等速查；自定义管道实现
  `transform()`；默认纯管道（输入引用不变则不重算），非纯管道要慎用。

### 2.5 常见陷阱

- @for 忘写 track 或用 index 当 track：列表更新错乱或性能差。
- 在模板里调用方法做过滤排序（每次变更检测都执行），应改用 computed 或管道。
- 非纯管道里做重计算，拖垮整个变更检测。

### 2.6 过关自检

1. 能写一个属性指令和一个结构指令。
2. 新控制流 @if/@for 的 track 规则能说清楚。
3. 能解释"管道 vs 方法调用 vs computed"的性能取舍。

## 3. 第七站：HttpClient 与状态管理

这一站把"接口数据"变成"界面状态"，全程信号化。

### 3.1 拦截器：统一关注点

```ts
// 认证拦截器：函数式写法，自动附加 token
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).token();
  const authReq = token
    ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
    : req;
  return next(authReq);
};

// app.config.ts
provideHttpClient(withInterceptors([authInterceptor]))
```

### 3.2 resource：把请求变成三态信号

```ts
@Component({ /* ... */ })
export class UserList {
  private http = inject(HttpClient);
  keyword = signal("");

  users = resource({
    request: this.keyword,                       // 信号变化自动重新请求
    loader: ({ request }) =>
      this.http.get<User[]>(`/api/users?q=${request}`),
  });

  // 模板里用 users.value() / users.isLoading() / users.error()
}
```

**讲解：** resource 把 loading/value/error 三态装进一个信号资源，
配合 computed 派生筛选视图，组件不再手写"请求 → 存结果 → 翻状态"的样板。

### 3.3 服务化状态与 RxJS 桥接

- 领域状态收进 service：`signal` 存数据、`computed` 派生视图模型、
  方法内做变更，组件只读不写。
- 既有 RxJS 代码用 `toSignal()` 接入信号世界，反向用 `toObservable()`；
  两者并存期注意订阅生命周期。

### 3.4 常见陷阱

- 拦截器里做重业务逻辑（它只该管横切关注点）。
- effect 里再改被它依赖的信号，造成循环触发。
- toSignal 在非注入上下文调用报错（要传 injectionContext 或在构造器里）。

### 3.5 过关自检

1. 会写函数式拦截器处理 token 与 401。
2. 会用 resource/rxResource 表达"请求即状态"。
3. 能把一个"满地手写状态同步"的组件重构成 signal + computed。

## 4. 第八站：测试与 SSR 水合

交付质量的两大支柱。

### 4.1 组件测试骨架

```ts
describe("CounterComponent", () => {
  it("点击加一", async () => {
    await TestBed.compileComponents();          // 准备
    const fixture = TestBed.createComponent(Counter);
    fixture.componentInstance.count.set(1);     // 执行
    await fixture.whenStable();
    expect(fixture.componentInstance.count()).toBe(2);   // 断言
  });
});
```

服务测试用 `provideHttpClientTesting` 把后端换成 mock，专测服务逻辑。

### 4.2 SSR 与水合

```bash
ng add @angular/ssr        # 一条命令接入服务端渲染
```

```ts
// app.config.ts —— 客户端水合：接管服务端 HTML 而非重绘
provideClientHydration(),
```

**讲解：** SSR 让首屏由服务端直出 HTML（快 + 利于 SEO），
水合让客户端"接上"这份 HTML 继续交互。水合错误的根源是
"服务端与客户端渲染出不同结果"——渲染路径里别直接碰 window/localStorage，
需要浏览器的逻辑放 afterNextRender。

### 4.3 常见陷阱

- 测试里没有 await fixture.whenStable 就断言，时序失败。
- SSR 下使用 window/document 直接访问导致服务器报错。
- 服务端与客户端渲染不一致（如依赖 Date.now 的随机内容），水合告警。

### 4.4 过关自检

1. 能为核心组件写 AAA 结构的测试并接入 CI。
2. 能解释 SSR 渲染流程与水合的关系。
3. 知道三类水合错误的典型成因与规避手段。

## 5. 学习建议

1. 顺序学，不跳站：第六站的模板 idioms 会在第七、八站反复出现。
2. 每站一个产出：给现有应用加"权限高亮"指令、把列表页改造成 resource + computed、
   为核心组件写测试并开启 SSR。
3. 版本跟进：Angular 半年一个大版本，升级走官方 update guide；
   zoneless 持续推进，新项目留意实验选项。

## 小结与延伸

- 进阶三站：模板复用 → 数据与状态 → 质量与首屏，对应从"会搭"到"能交付"的跨越。
- 每一站的展开文档将陆续补充在本模块中，编号紧接本篇（007 起）。
- 官方资源：angular.dev（新文档站）、angular.dev/guide/signals、
  angular.dev/guide/ssr。

<!-- ============================================================ angular/007-DirectivesPipes ============================================================ -->

# 指令与管道

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- 指令三分法
- 属性指令与 host 绑定
- 结构指令原理与 TemplateRef
- @if/@for 控制流与 track
- 自定义管道与纯/非纯

<!-- ============================================================ angular/008-HttpClientStateManagement ============================================================ -->

# HttpClient 与状态管理

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- 函数式拦截器与鉴权
- resource/rxResource 三态资源
- computed 视图模型
- 服务化状态
- toSignal/toObservable 桥接

<!-- ============================================================ angular/009-TestingSSRHydration ============================================================ -->

# 测试与 SSR 水合

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- TestBed 组件测试
- HttpClientTesting 服务测试
- @angular/ssr 接入
- provideClientHydration
- 水合错误规避
