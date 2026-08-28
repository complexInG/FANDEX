---
order: 30
title: Angular 信号与组件通信
module: 'angular'
category: 前端技术
difficulty: intermediate
description: signal/computed/effect 响应式状态、input/output/model 组件通信，Angular 22 推荐的响应式写法。
author: fanquanpp
updated: '2026-08-03'
related:
  - 'angular/002-QuickStartComponentTemplate'
  - 'angular/004-DependencyInjectionServices'
prerequisites:
  - 'angular/002-QuickStartComponentTemplate'
---

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
