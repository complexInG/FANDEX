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
