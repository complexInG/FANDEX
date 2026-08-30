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
