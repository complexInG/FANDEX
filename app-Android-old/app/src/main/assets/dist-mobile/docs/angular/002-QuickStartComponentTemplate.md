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
