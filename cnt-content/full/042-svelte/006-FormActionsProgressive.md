---
order: 60
title: Form Actions 与渐进增强
module: 'svelte'
category: 前端技术
difficulty: intermediate
description: 不写一行 fetch 也能完成增删改：SvelteKit 的表单哲学。
author: fanquanpp
updated: '2026-08-28'
related:
  - 'svelte/003-ReactivityRunes'
prerequisites:
  - 'svelte/002-SvelteKitQuickStart'
---

## 0. 什么是渐进增强（先读这里）

> 学习目标：读完本文，你能用 actions 在服务端处理表单提交；区分 default 与具名
> action；理解 `form` 属性如何回填结果、`use:enhance` 如何把整页刷新升级为无刷新
> 交互；会用 fail(400) 与 redirect(303) 表达服务端结论；能落地"服务端唯一真相"的
> 校验模式，并把权限检查写在 action 内部；最后能判断何时该用 action、何时该用
> API 端点。

Form Actions 是 SvelteKit 的核心哲学：`<form>` 是原生 HTML 元素，不依赖 JavaScript
就能工作，框架在其上叠加增强。业务代码只写在服务端 action 里，客户端一行 `fetch`
都不用写。

## 1. 最小可用：default action

```svelte
<!-- src/routes/feedback/+page.svelte -->
<form method="POST">
  <!-- input 的 name 是服务端取值的键 -->
  <textarea name="message" rows="4" required></textarea>
  <button type="submit">提交反馈</button>
</form>
```

```ts
// src/routes/feedback/+page.server.ts
import type { Actions } from "./$types"

export const actions: Actions = {
  default: async ({ request }) => {
    const data = await request.formData() // 解析出的 FormData
    const message = String(data.get("message") ?? "")
    await saveFeedback(message) // 落库、发通知等副作用都写在服务端
    return { success: true } // 返回值会交给页面的 form 属性
  }
}
```

**讲解：**

1. `export const actions` 只能出现在 `+page.server.ts`（或 `+layout.server.ts`）中，
   这意味着处理函数永远运行在服务器，表单里没有任何业务逻辑可被窥探。
2. `<form method="POST">` 不写 `action` 属性时，提交目标就是当前路由的 default
   action——这就是"表单即接口"。
3. `request.formData()` 返回标准 `FormData`；`data.get()` 结果类型是
   `FormDataEntryValue | null`，用 `String(... ?? "")` 归一成字符串最稳妥。

## 2. 具名 action：一个页面多个动作

```svelte
<!-- src/routes/todos/+page.svelte -->
<form method="POST" action="?/create">
  <!-- action="?/名字" 指向同名 action -->
  <input name="title" placeholder="新待办" required />
  <button type="submit">创建</button>
</form>

{#each data.todos as todo (todo.id)}
  <li>
    {todo.title}
    <!-- 按钮级覆盖：同一表单内不同按钮触发不同 action -->
    <button type="submit" formaction="?/delete" name="id" value={todo.id}>
      删除
    </button>
  </li>
{/each}
```

```ts
// src/routes/todos/+page.server.ts
import type { Actions } from "./$types"

export const actions: Actions = {
  create: async ({ request }) => {
    const data = await request.formData()
    await db.todo.create({ data: { title: String(data.get("title")) } })
    return { ok: true }
  },
  delete: async ({ request }) => {
    const data = await request.formData()
    await db.todo.delete({ where: { id: String(data.get("id")) } })
    return { ok: true }
  }
}
```

| 表单写法 | 命中的 action |
| --- | --- |
| `<form method="POST">`（不写 action） | `default` |
| `<form method="POST" action="?/create">` | `create` |
| `<button formaction="?/delete">` | `delete`（覆盖表单级 action） |
| `<button formaction>` 带自身 `name/value` | 该按钮的值随提交一起发送 |

**讲解：**

1. `?/create` 的 `?` 表示"当前路由"，整体读作"当前页面的 create action"。
2. 一个页面承载整组增删改，是 actions 与 REST 风格 API 最大的体验差异：不必为每个
   动作单开一个端点文件。

## 3. form 属性与 use:enhance

action 的返回值去哪了？它成为页面的 `form` 属性；而 `use:enhance` 决定这次提交是
"整页刷新"还是"无刷新更新"。

```svelte
<!-- src/routes/subscribe/+page.svelte -->
<script lang="ts">
  import { enhance } from "$app/forms"
  import type { PageProps } from "./$types"

  let { form }: PageProps = $props() // action 返回值 / fail 数据都从这里来
</script>

<form method="POST" use:enhance>
  <!-- 加 use:enhance 即启用无刷新提交 -->
  <input name="email" type="email" required />
  <button type="submit">订阅</button>
</form>

{#if form?.errors}
  <!-- fail 返回的数据 -->
  <p role="alert">{form.errors.email}</p>
{:else if form?.success}
  <p>订阅成功，请查收邮件</p>
{/if}
```

| 对比项 | 不加 use:enhance | 加 use:enhance |
| --- | --- | --- |
| 提交方式 | 浏览器原生 POST，整页刷新 | 框架用 fetch 提交，原地更新 |
| 结果传达 | 服务端重新渲染页面并注入 form | 直接更新 form 属性 |
| 无 JS 环境 | 正常工作（这就是渐进增强的底线） | 自动退回原生行为 |
| load 重跑 | 页面重新执行 | 成功时 invalidateAll 重跑 load |

`use:enhance` 对不同响应的默认行为：

| 响应类型 | 默认处理 |
| --- | --- |
| success | invalidateAll 刷新所有 load，更新 form，重置表单 |
| failure | 只更新 form（保留用户输入，不清空） |
| redirect | 自动 goto 到目标地址 |
| error | 交给 `+error.svelte` 渲染 |

**讲解：**

1. `form` 属性在页面初次进入时是 `undefined`，提交后才有值；读取时全部用可选链。
2. 即使不做任何自定义，`use:enhance` 也值得加：不刷新、自动更新 form、成功后刷新
   数据，三件事零代码完成。

## 4. fail(400) 与 redirect(303)：服务端的两种答复

```ts
// src/routes/login/+page.server.ts
import { fail, redirect } from "@sveltejs/kit"
import type { Actions } from "./$types"

export const actions: Actions = {
  default: async ({ request, cookies }) => {
    const data = await request.formData()
    const email = String(data.get("email") ?? "")
    const password = String(data.get("password") ?? "")

    const user = await verifyUser(email, password)
    if (!user) {
      // fail：带状态码与数据"返回"页面，form 属性可拿到 errors 与 values
      return fail(400, {
        errors: { password: "邮箱或密码错误" },
        values: { email } // 回填用户已输入的部分，避免重打
      })
    }

    cookies.set("session", await createSession(user.id), {
      path: "/",
      httpOnly: true // 会话 Cookie 必须防脚本读取
    })
    redirect(303, "/dashboard") // redirect 是"抛出"式，之后的代码不会执行
  }
}
```

```svelte
<!-- 登录表单：value 绑定回填值 -->
<input name="email" value={form?.values?.email ?? ""} />
{#if form?.errors?.password}
  <p role="alert">{form.errors.password}</p>
{/if}
```

**讲解：**

1. `fail` 与 `redirect` 都从 `@sveltejs/kit` 导入；`fail` 用 `return`，`redirect` 是
   直接调用抛出（SvelteKit 2 无需 `throw` 前缀）。
2. POST 成功后重定向用 `303`：浏览器收到后会改用 GET 请求目标页，避免"刷新重复
   提交"，这就是经典的 PRG（Post/Redirect/Get）模式。
3. `fail` 的第二个参数就是交给 `form` 的数据；约定 `errors` 放错误、`values` 放回填
   值，页面渲染就有稳定契约。

## 5. 自定义 use:enhance：pending 态与取消

默认增强之外，常见需求是"提交中禁用按钮"与"提交前拦截"。自定义回调即可。

```svelte
<!-- src/routes/todos/+page.svelte -->
<script lang="ts">
  import { enhance } from "$app/forms"

  let submitting = $state(false) // pending 态用 runes 维护
</script>

<form
  method="POST"
  action="?/create"
  use:enhance={({ formElement, formData, cancel }) => {
    // 提交前回调：可拿到表单元素、formData，并能取消本次提交
    if (String(formData.get("title") ?? "").trim() === "") {
      cancel() // 阻止请求发出，表单恢复原状
      return
    }
    submitting = true
    // 返回的函数在响应到达后执行：可拿到 result 与 update
    return async ({ result, update }) => {
      submitting = false
      if (result.type === "failure") {
        console.log("服务端校验未通过", result.data) // 可自定义提示
      }
      await update({ reset: false }) // 默认成功后清空表单，这里保留输入
    }
  }}
>
  <input name="title" />
  <button type="submit" disabled={submitting}>
    {submitting ? "提交中……" : "添加"}
  </button>
</form>
```

**讲解：**

1. 提交前回调参数：`formElement`（DOM 表单）、`formData`（待发送数据）、
   `cancel`（取消函数）；不返回函数则走默认处理。
2. 响应回调参数：`result`（服务端结果对象，含 `type` 与 `data`）、`update`（等价于
   "执行默认行为"，可传 `{ reset: false }` 控制是否清空表单）。
3. 想完全接管就不调用 `update`，自行处理 `result`；一般场景
   `update({ reset: false })` 已够用。

## 6. 校验：服务端是唯一真相（zod）

```ts
// src/routes/signup/+page.server.ts
import { fail } from "@sveltejs/kit"
import { z } from "zod"
import type { Actions } from "./$types"

// Schema 一处定义：服务端校验 + 类型推导共用
const signupSchema = z.object({
  email: z.string().email("邮箱格式不正确"),
  password: z.string().min(8, "密码至少 8 位"),
  nickname: z.string().min(2, "昵称至少 2 个字符").max(20, "昵称过长")
})

export const actions: Actions = {
  default: async ({ request }) => {
    const raw = Object.fromEntries(await request.formData())
    const parsed = signupSchema.safeParse(raw)

    if (!parsed.success) {
      // 把字段错误整理成 { 字段名: 提示 } 的结构
      const errors: Record<string, string> = {}
      for (const issue of parsed.error.issues) {
        const key = String(issue.path[0])
        errors[key] ??= issue.message // 同一字段只保留第一条
      }
      return fail(400, { errors, values: raw })
    }

    await createUser(parsed.data) // parsed.data 已是校验过的强类型数据
    return { success: true }
  }
}
```

**讲解：**

1. 原则：HTML 的 `required`、`type="email"` 只是体验优化；绕过浏览器的任何请求
   （curl、脚本）都必须被服务端 Schema 拦截，所以服务端校验不可省略。
2. `safeParse` 不抛异常，返回 `{ success, data }` 或 `{ success, error }`；业务层
   只消费 `parsed.data`，天然获得类型收窄。
3. zod 不同大版本的 API 略有差异（如错误结构），以所用版本文档为准；校验失败统一
   `fail(400, { errors, values })`，页面端就有一套稳定的渲染契约。

## 7. 权限检查与 actions 对比 API 端点

```ts
// src/routes/posts/[id]/+page.server.ts
import { fail, redirect } from "@sveltejs/kit"
import type { Actions } from "./$types"

export const actions: Actions = {
  delete: async ({ locals, params }) => {
    // 鉴权紧贴业务入口：locals 由 hooks 注入（见第 5 篇第 6 节）
    if (!locals.user) return fail(401, { message: "请先登录" })

    const post = await db.post.findUnique({ where: { id: params.id } })
    if (!post) return fail(404, { message: "文章不存在" })
    if (post.authorId !== locals.user.id) {
      return fail(403, { message: "只能删除自己的文章" }) // 授权校验不可省略
    }

    await db.post.delete({ where: { id: params.id } })
    redirect(303, "/posts")
  }
}
```

| 维度 | Form Actions | `+server.ts` API 端点 |
| --- | --- | --- |
| 调用方 | 本站 `<form>`（人） | 任意 HTTP 客户端（程序） |
| 返回形式 | 数据 / fail / redirect 混用 | 纯 `Response` 对象 |
| 无 JS 可用 | 天然支持，可整页降级 | 不适用 |
| 页面联动 | 自动更新 form、刷新 load | 需要自己写状态同步 |
| CSRF | 默认受 SvelteKit 跨站 POST 保护 | 同样受保护 |
| 典型场景 | 页面内增删改、登录注册 | 公开 API、Webhook、多端共用接口 |

**讲解：**

1. 权限检查必须写在 action 内部，而不是只靠隐藏按钮——前端隐藏只是体验，服务端
   校验才是安全。
2. 经验法则：为"这个页面"服务就用 actions，为"多个客户端"服务才开 `+server.ts`；
   两者可以共存于同一目录。
3. SvelteKit 默认拒绝跨站 POST 提交（CSRF 保护基于 Origin 头），部署在反代后面时
   注意正确转发协议与主机头（以官方文档为准）。

## 小结与延伸

> 表单提交的完整链路：`<form method="POST">` 命中 action，服务端校验后
> `return fail` 回填错误、`redirect(303)` 跳转成功；`use:enhance` 把这条链路升级成
> 无刷新交互，而没有 JS 时一切照常。

1. actions 是"表单即接口"：`default` 与具名 action 覆盖一个页面的全部写操作。
2. `form` 属性是服务端与页面之间的回传通道，`errors`/`values` 是常用契约。
3. `fail(400)` 失败回填、`redirect(303)` 成功跳转，两种答复覆盖绝大多数场景。
4. 校验只认服务端 Schema；权限检查写在 action 里，不信任任何前端状态。
5. actions 面向页面，`+server.ts` 面向程序，按调用方选型而不是按习惯。

**动手试试：**

1. 把第 4 节的登录页跑起来，故意输错密码，观察 form 回填与地址栏变化；再删掉
   `use:enhance` 对比整页刷新的行为。
2. 给待办页面加"切换完成状态"的具名 action，按钮用 `formaction` 触发。
3. 在 action 里打印 `locals.user`，未登录时直接 `fail(401)`，验证 hooks 与 actions
   的配合。

**延伸阅读：** SvelteKit 官方文档的 Form actions 与 Progressive enhancement 两章；
本模块第 5 篇的 hooks 一节是本文权限检查的前置知识。
