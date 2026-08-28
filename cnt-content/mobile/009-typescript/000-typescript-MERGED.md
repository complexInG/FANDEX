---
order: 10
title: typescript 模块文档合集
module: 'typescript'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：009-typescript/001-GenericConstraintDefault.md ============ -->

# 泛型约束与默认值

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 泛型约束基础

**换行写法：使用 extends 约束泛型**
`interface <接口> { <属性>: <类型> }`
`function <函数><<T> extends <接口>>(<参数>: <T>): <返回类型> { <语句> }`

```typescript
// 泛型约束（限制类型必须包含指定属性）
interface HasLength {
    length: number
}

function log_length<T extends HasLength>(value: T): void {
    console.log(value.length)
}
```

---

**基本写法：使用约束泛型**
`<函数>(<值>)`

```typescript
// 使用约束泛型函数
log_length("hello")  // string 有 length 属性
log_length([1, 2, 3])  // array 有 length 属性
```

---

## keyof 约束

**基本写法：使用 keyof 约束泛型**
`function <函数><<T>, <K> extends keyof <T>>(<参数>: <T>, <键>: <K>): <返回类型> { <语句> }`

```typescript
// 使用 keyof 约束泛型
function get_property<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key]
}
```

---

**基本写法：使用 keyof 约束泛型函数**
`<函数>(<对象>, "<属性>")`

```typescript
// 使用 keyof 约束泛型函数
let user = { name: "Alice", age: 30 }
let name = get_property(user, "name")
```

---

## 类型参数约束

**换行写法：类型参数之间约束**
`function <函数><<T>, <U> extends keyof <T>>(<参数>: <T>): <返回类型> { <语句> }`

```typescript
// 类型参数之间约束（U 必须是 T 的键）
function get_keys<T, U extends keyof T>(obj: T): U[] {
    return Object.keys(obj) as U[]
}
```

---

**基本写法：约束为特定类型**
`function <函数><<T> extends <类型>>(<参数>: <T>): <返回类型> { <语句> }`

```typescript
// 约束泛型为特定类型
function sum<T extends number>(a: T, b: T): number {
    return a + b
}
```

---

## 泛型默认类型

**基本写法：泛型默认类型**
`function <函数><<T> = <默认类型>>(<参数>: <T>): <返回类型> { <语句> }`

```typescript
// 泛型默认类型
function create_array<T = string>(length: number, value: T): T[] {
    return Array(length).fill(value)
}
```

---

**换行写法：多泛型默认类型**
`function <函数><`
`    <T> = <默认类型1>,`
`    <U> = <默认类型2>,`
`>(<参数1>: <T>, <参数2>: <U>): <返回类型> { <语句> }`

```typescript
// 多泛型默认类型
function create_pair<
    T = string,
    U = number,
>(first: T, second: U): [T, U] {
    return [first, second]
}
```

---

**基本写法：使用默认类型**
`<函数>(<值>)`

```typescript
// 使用默认类型（不指定类型参数）
let arr = create_array(3, "hello")  // T 默认为 string
```

---

**基本写法：覆盖默认类型**
`<函数><<新类型>>(<值>)`

```typescript
// 覆盖默认类型
let arr = create_array<number>(3, 42)
```

---

## 泛型接口默认类型

**换行写法：泛型接口默认类型**
`interface <接口名><<T> = <默认类型>> {`
`    <属性>: <T>`
`}`

```typescript
// 泛型接口默认类型
interface Container<T = string> {
    value: T
}
```

---

**基本写法：使用默认类型的泛型接口**
`let <变量>: <接口名> = { <属性>: <值> }`

```typescript
// 使用默认类型的泛型接口
let container: Container = { value: "hello" }  // T 默认为 string
```

---

## 泛型类默认类型

**换行写法：泛型类默认类型**
`class <类名><<T> = <默认类型>> {`
`    private <属性>: <T>[]`
`}`

```typescript
// 泛型类默认类型
class Stack<T = string> {
    private items: T[] = []

    push(item: T): void {
        this.items.push(item)
    }
}
```

---

**基本写法：使用默认类型的泛型类**
`let <变量> = new <类名>()`

```typescript
// 使用默认类型的泛型类
let stack = new Stack()  // T 默认为 string
```

---

## 条件类型约束

**基本写法：条件类型约束**
`type <类型> = <T> extends <条件> ? <真类型> : <假类型>`

```typescript
// 条件类型约束
type IsString<T> = T extends string ? true : false
```

---

**基本写法：使用条件类型约束**
`type <别名> = <类型函数><<参数类型>>`

```typescript
// 使用条件类型约束
type A = IsString<string>  // true
type B = IsString<number>  // false
```

---

## infer 推断

**换行写法：使用 infer 推断类型**
`type <类型> = <T> extends (<参数>: infer <U>) => any ? <U> : never`

```typescript
// 使用 infer 推断函数参数类型
type GetParameter<T> = T extends (arg: infer U) => any ? U : never
```

---

**基本写法：使用 infer 推断返回类型**
`type <类型> = <T> extends (...args: any[]) => infer <R> ? <R> : never`

```typescript
// 使用 infer 推断函数返回类型
type GetReturnType<T> = T extends (...args: any[]) => infer R ? R : never
```

---

**基本写法：使用 infer 推断数组元素类型**
`type <类型> = <T> extends (infer <U>)[] ? <U> : never`

```typescript
// 使用 infer 推断数组元素类型
type GetArrayElement<T> = T extends (infer U)[] ? U : never
```

---

**基本写法：使用 infer 推断 Promise 类型**
`type <类型> = <T> extends Promise<infer <U>> ? <U> : <T>`

```typescript
// 使用 infer 推断 Promise 的类型
type UnwrapPromise<T> = T extends Promise<infer U> ? U : T
```

---

## 多重约束

**换行写法：多重约束泛型**
`function <函数><<T> extends <接口1> & <接口2>>(<参数>: <T>): <返回类型> { <语句> }`

```typescript
// 多重约束泛型（必须同时满足多个约束）
interface HasLength {
    length: number
}

interface HasName {
    name: string
}

function process<T extends HasLength & HasName>(value: T): void {
    console.log(value.length, value.name)
}
```

---

## 泛型约束与类

**换行写法：泛型类约束**
`class <类名><<T> extends <接口>> {`
`    private <属性>: <T>`
`}`

```typescript
// 泛型类约束
interface Comparable {
    compare(other: any): number
}

class SortedList<T extends Comparable> {
    private items: T[] = []

    add(item: T): void {
        this.items.push(item)
        this.items.sort((a, b) => a.compare(b))
    }
}
```

---

## 泛型约束与构造函数

**换行写法：约束为构造函数**
`function <函数><<T>>(<类>: new (...args: any[]) => <T>): <T> { <语句> }`

```typescript
// 约束泛型为构造函数
function create_instance<T>(constructor: new (...args: any[]) => T): T {
    return new constructor()
}
```

---

**换行写法：使用 new 约束**
`interface <接口> { new (...args: any[]): <类型> }`
`function <函数><<T>>(<类>: <接口>): <T> { <语句> }`

```typescript
// 使用 new 约束泛型
interface Constructor<T> {
    new (...args: any[]): T
}

function factory<T>(ctor: Constructor<T>): T {
    return new ctor()
}
```

---

## 泛型与映射类型

**换行写法：泛型映射类型**
`type <类型><<T>> = {`
`    [P in keyof T]: <新类型>`
`}`

```typescript
// 泛型映射类型
type Stringify<T> = {
    [P in keyof T]: string
}
```

---

**换行写法：使用泛型映射类型**
`type <别名> = <类型><<接口>>`

```typescript
// 使用泛型映射类型
interface User {
    name: string
    age: number
}

type StringUser = Stringify<User>  // { name: string, age: string }
```

---

## 泛型与工具类型

**基本写法：使用 Partial 工具类型**
`type <别名> = Partial<<接口>>`

```typescript
// 使用 Partial 使所有属性可选
type PartialUser = Partial<User>
```

---

**基本写法：使用 Required 工具类型**
`type <别名> = Required<<接口>>`

```typescript
// 使用 Required 使所有属性必填
type RequiredUser = Required<User>
```

---

**基本写法：使用 Readonly 工具类型**
`type <别名> = Readonly<<接口>>`

```typescript
// 使用 Readonly 使所有属性只读
type ReadonlyUser = Readonly<User>
```

---

**基本写法：使用 Pick 工具类型**
`type <别名> = Pick<<接口>, "<属性1>" | "<属性2>">`

```typescript
// 使用 Pick 选取部分属性
type UserBasic = Pick<User, "name" | "age">
```

---

**基本写法：使用 Omit 工具类型**
`type <别名> = Omit<<接口>, "<属性>">`

```typescript
// 使用 Omit 排除部分属性
type UserWithoutAge = Omit<User, "age">
```

---

**基本写法：使用 Record 工具类型**
`type <别名> = Record<<键类型>, <值类型>>`

```typescript
// 使用 Record 创建键值对类型
type UserMap = Record<string, User>
```

---

## 泛型与条件类型组合

**换行写法：条件类型与泛型组合**
`type <类型><<T>> = <T> extends <条件> ? <真类型> : <假类型>`

```typescript
// 条件类型与泛型组合
type NonNullable<T> = T extends null | undefined ? never : T
```

---

**换行写法：分布式条件类型**
`type <类型><<T>> = <T> extends <条件> ? <真类型> : <假类型>`

```typescript
// 分布式条件类型（对联合类型逐个判断）
type ToArray<T> = T extends any ? T[] : never
```

---

**基本写法：使用分布式条件类型**
`type <别名> = <类型><<联合类型>>`

```typescript
// 使用分布式条件类型
type Result = ToArray<string | number>  // string[] | number[]
```

---

## 泛型与 infer 组合

**换行写法：使用 infer 提取类型**
`type <类型> = <T> extends Promise<infer <U>> ? <U> : <T>`

```typescript
// 使用 infer 提取 Promise 的类型
type Awaited<T> = T extends Promise<infer U> ? U : T
```

---

**换行写法：递归条件类型**
`type <类型> = <T> extends Promise<infer <U>> ? <类型><<U>> : <T>`

```typescript
// 递归条件类型（处理嵌套 Promise）
type DeepAwaited<T> = T extends Promise<infer U> ? DeepAwaited<U> : T
```

---

## 泛型约束最佳实践

**换行写法：约束泛型为特定结构**
`interface <接口> { <属性>: <类型> }`
`function <函数><<T> extends <接口>>(<参数>: <T>): <返回类型> { <语句> }`

```typescript
// 约束泛型为特定结构
interface Identifiable {
    id: string | number
}

function find_item<T extends Identifiable>(items: T[], id: string | number): T | undefined {
    return items.find(item => item.id === id)
}
```

---

**换行写法：使用泛型约束实现工厂模式**
`interface <接口> { create(): <类型> }`
`function <函数><<T>>(<工厂>: <接口>): <T> { <语句> }`

```typescript
// 使用泛型约束实现工厂模式
interface Factory<T> {
    create(): T
}

function create_instance<T>(factory: Factory<T>): T {
    return factory.create()
}
```



<!-- ============ 文档分隔线：009-typescript/002-FunctionGeneric.md ============ -->

# 函数与泛型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数声明

**基本写法：函数声明**
`function <函数名>(<参数>: <类型>): <返回类型> { <语句> }`

```typescript
// 函数声明
function add(a: number, b: number): number {
    return a + b
}
```

---

**基本写法：函数表达式**
`const <函数名> = function(<参数>: <类型>): <返回类型> { <语句> }`

```typescript
// 函数表达式
const add = function(a: number, b: number): number {
    return a + b
}
```

---

**基本写法：箭头函数**
`const <函数名> = (<参数>: <类型>): <返回类型> => <表达式>`

```typescript
// 箭头函数
const add = (a: number, b: number): number => a + b
```

---

## 函数类型

**基本写法：使用 type 定义函数类型**
`type <函数类型> = (<参数>: <类型>) => <返回类型>`

```typescript
// 使用 type 定义函数类型
type MathFunc = (a: number, b: number) => number
```

---

**换行写法：使用 interface 定义函数类型**
`interface <函数类型> {`
`    (<参数>: <类型>): <返回类型>`
`}`

```typescript
// 使用 interface 定义函数类型
interface MathFunc {
    (a: number, b: number): number
}
```

---

**基本写法：使用函数类型**
`let <变量>: <函数类型> = (<参数>) => <表达式>`

```typescript
// 使用函数类型注解
let add: MathFunc = (a, b) => a + b
```

---

## 可选参数

**基本写法：可选参数**
`function <函数>(<参数1>: <类型>, <参数2>?: <类型>): <返回类型> { <语句> }`

```typescript
// 可选参数（必须放在必选参数后）
function greet(name: string, greeting?: string): string {
    return `${greeting || "Hello"}, ${name}`
}
```

---

## 默认参数

**基本写法：默认参数**
`function <函数>(<参数>: <类型> = <默认值>): <返回类型> { <语句> }`

```typescript
// 默认参数值
function greet(name: string = "World"): string {
    return `Hello, ${name}`
}
```

---

## 剩余参数

**基本写法：剩余参数**
`function <函数>(...<参数>: <类型>[]): <返回类型> { <语句> }`

```typescript
// 剩余参数
function sum(...numbers: number[]): number {
    return numbers.reduce((a, b) => a + b, 0)
}
```

---

## 函数重载

**换行写法：函数重载签名**
`function <函数>(<参数>: <类型1>): <返回类型1>`
`function <函数>(<参数>: <类型2>): <返回类型2>`
`function <函数>(<参数>: <类型>): <返回类型> { <语句> }`

```typescript
// 函数重载
function process(data: number): string
function process(data: string): number
function process(data: number | string): string | number {
    if (typeof data === "number") {
        return String(data)
    }
    return data.length
}
```

---

## 泛型函数

**基本写法：定义泛型函数**
`function <函数><<类型参数>>(<参数>: <类型参数>): <类型参数> { <语句> }`

```typescript
// 定义泛型函数
function identity<T>(value: T): T {
    return value
}
```

---

**基本写法：使用泛型函数**
`<函数><<类型>>(<值>)`

```typescript
// 使用泛型函数（显式指定类型）
let result = identity<string>("hello")
```

---

**基本写法：类型推断泛型**
`<函数>(<值>)`

```typescript
// 使用泛型函数（自动推断类型）
let result = identity("hello")  // T 推断为 string
```

---

## 多类型参数泛型

**单行写法：多类型参数泛型函数**
`function <函数><<T>, <U>>(<参数1>: <T>, <参数2>: <U>): [<T>, <U>] { <语句> }`

```typescript
// 多类型参数泛型函数
function pair<T, U>(first: T, second: U): [T, U] {
    return [first, second]
}
```

---

**换行写法：多类型参数泛型函数**
`function <函数><`
`    <T>,`
`    <U>,`
`>(<参数1>: <T>, <参数2>: <U>): [<T>, <U>] { <语句> }`

```typescript
// 多类型参数泛型函数（换行书写）
function pair<
    T,
    U,
>(first: T, second: U): [T, U] {
    return [first, second]
}
```

---

## 泛型接口

**换行写法：定义泛型接口**
`interface <接口名><<T>> {`
`    <属性>: <T>`
`}`

```typescript
// 定义泛型接口
interface Container<T> {
    value: T
}
```

---

**基本写法：使用泛型接口**
`let <变量>: <接口名><<类型>> = { <属性>: <值> }`

```typescript
// 使用泛型接口
let container: Container<string> = { value: "hello" }
```

---

## 泛型类

**换行写法：定义泛型类**
`class <类名><<T>> {`
`    private <属性>: <T>[]`
`    <方法>(<参数>: <T>): void { <语句> }`
`}`

```typescript
// 定义泛型类
class Stack<T> {
    private items: T[] = []

    push(item: T): void {
        this.items.push(item)
    }

    pop(): T | undefined {
        return this.items.pop()
    }
}
```

---

**基本写法：使用泛型类**
`let <变量> = new <类名><<类型>>()`

```typescript
// 使用泛型类
let stack = new Stack<number>()
stack.push(1)
```

---

## 泛型约束

**换行写法：使用 extends 约束泛型**
`interface <接口> { <属性>: <类型> }`
`function <函数><<T> extends <接口>>(<参数>: <T>): <返回类型> { <语句> }`

```typescript
// 泛型约束（限制类型必须包含指定属性）
interface HasLength {
    length: number
}

function log_length<T extends HasLength>(value: T): void {
    console.log(value.length)
}
```

---

**基本写法：使用 keyof 约束泛型**
`function <函数><<T>, <K> extends keyof <T>>(<参数>: <T>, <键>: <K>): <返回类型> { <语句> }`

```typescript
// 使用 keyof 约束泛型
function get_property<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key]
}
```

---

## 泛型默认类型

**基本写法：泛型默认类型**
`function <函数><<T> = <默认类型>>(<参数>: <T>): <返回类型> { <语句> }`

```typescript
// 泛型默认类型
function create_array<T = string>(length: number, value: T): T[] {
    return Array(length).fill(value)
}
```

---

**换行写法：多泛型默认类型**
`function <函数><`
`    <T> = <默认类型1>,`
`    <U> = <默认类型2>,`
`>(<参数1>: <T>, <参数2>: <U>): <返回类型> { <语句> }`

```typescript
// 多泛型默认类型
function create_pair<
    T = string,
    U = number,
>(first: T, second: U): [T, U] {
    return [first, second]
}
```

---

## 泛型工具类型

**基本写法：使用 Partial 工具类型**
`type <别名> = Partial<<接口>>`

```typescript
// 使用 Partial 使所有属性可选
interface User {
    name: string
    age: number
}

type PartialUser = Partial<User>
```

---

**基本写法：使用 Readonly 工具类型**
`type <别名> = Readonly<<接口>>`

```typescript
// 使用 Readonly 使所有属性只读
type ReadonlyUser = Readonly<User>
```

---

**基本写法：使用 Pick 工具类型**
`type <别名> = Pick<<接口>, "<属性1>" | "<属性2>">`

```typescript
// 使用 Pick 选取部分属性
type UserBasic = Pick<User, "name" | "age">
```

---

**基本写法：使用 Record 工具类型**
`type <别名> = Record<<键类型>, <值类型>>`

```typescript
// 使用 Record 创建键值对类型
type UserMap = Record<string, User>
```

---

## 泛型与数组

**基本写法：泛型数组函数**
`function <函数><<T>>(<参数>: <T>[]): <T> { <语句> }`

```typescript
// 泛型数组函数
function first<T>(items: T[]): T {
    return items[0]
}
```

---

**基本写法：泛型数组方法**
`function <函数><<T>>(<参数>: <T>[], <函数>: (<项>: <T>) => boolean): <T>[] { <语句> }`

```typescript
// 泛型数组方法
function filter<T>(items: T[], predicate: (item: T) => boolean): T[] {
    return items.filter(predicate)
}
```

---

## this 类型

**换行写法：使用 this 类型**
`class <类名> {`
`    <方法>(<参数>: <类型>): this { return this }`
`}`

```typescript
// 使用 this 类型实现链式调用
class Calculator {
    private value = 0

    add(n: number): this {
        this.value += n
        return this
    }

    multiply(n: number): this {
        this.value *= n
        return this
    }
}
```

---

## 高阶函数

**基本写法：高阶函数**
`function <函数>(<函数参数>: (<参数>: <类型>) => <返回类型>): <返回类型> { <语句> }`

```typescript
// 高阶函数（函数作为参数）
function apply(func: (x: number) => number, value: number): number {
    return func(value)
}
```

---

**基本写法：返回函数的函数**
`function <函数>(<参数>): (<参数>: <类型>) => <返回类型> { return <函数> }`

```typescript
// 返回函数的函数
function create_multiplier(factor: number): (x: number) => number {
    return (x: number) => x * factor
}
```

---

## 泛型与 Promise

**换行写法：泛型 Promise 函数**
`async function <函数><<T>>(): Promise<<T>> { return <值> }`

```typescript
// 泛型 Promise 函数
async function fetch_data<T>(url: string): Promise<T> {
    const response = await fetch(url)
    return response.json()
}
```

---

**基本写法：使用泛型 Promise**
`let <变量>: Promise<<类型>> = <函数>()`

```typescript
// 使用泛型 Promise
let data: Promise<User> = fetch_data<User>("/api/user")
```

---

## 条件类型与泛型

**基本写法：条件类型**
`type <类型> = <T> extends <条件> ? <真类型> : <假类型>`

```typescript
// 条件类型
type IsString<T> = T extends string ? true : false
```

---

**基本写法：使用条件类型**
`type <别名> = <类型函数><<参数类型>>`

```typescript
// 使用条件类型
type A = IsString<string>  // true
type B = IsString<number>  // false
```

---

## 泛型与类方法

**换行写法：泛型类方法**
`class <类名><<T>> {`
`    <方法><<U>>(<参数>: <U>): <返回类型> { <语句> }`
`}`

```typescript
// 泛型类方法
class DataProcessor<T> {
    private data: T[] = []

    add(item: T): void {
        this.data.push(item)
    }

    transform<U>(fn: (item: T) => U): U[] {
        return this.data.map(fn)
    }
}
```

---

## 函数类型推断

**基本写法：从函数推断返回类型**
`type <别名> = ReturnType<typeof <函数>>`

```typescript
// 从函数推断返回类型
function get_user() {
    return { name: "Alice", age: 30 }
}

type User = ReturnType<typeof get_user>
```

---

**基本写法：从函数推断参数类型**
`type <别名> = Parameters<typeof <函数>>`

```typescript
// 从函数推断参数类型
function greet(name: string, age: number): void {}

type GreetParams = Parameters<typeof greet>  // [string, number]
```

---

## 泛型与映射类型

**换行写法：泛型映射类型**
`type <类型><<T>> = {`
`    [P in keyof T]: <新类型>`
`}`

```typescript
// 泛型映射类型
type Stringify<T> = {
    [P in keyof T]: string
}
```

---

**换行写法：使用泛型映射类型**
`type <别名> = <类型><<接口>>`

```typescript
// 使用泛型映射类型
interface User {
    name: string
    age: number
}

type StringUser = Stringify<User>  // { name: string, age: string }
```

---

## TypeScript 5.x 新特性

**基本写法：TypeScript 5.0 装饰器**
`function <decorator>(<target>, <context>) { }`

```typescript
// 定义符合 Stage 3 标准的装饰器函数
function log(target, context) {
    console.log(`装饰: ${context.name}`)
}
```

---

**基本写法：TypeScript 5.0 const 类型参数**
`<const T>`

```typescript
// 使用 const 类型参数锁定传入数组的字面量类型
function first_of<T extends readonly unknown[]>(arr: const T): T[0] {
    return arr[0]
}
const v = first_of([1, 2, 3] as const)  // 类型为字面量 1
```

---

**基本写法：TypeScript 5.1 函数返回类型分离声明**
`function <函数名>(<参数>): <返回类型> { return <表达式> }`

```typescript
// 返回类型与函数体解耦检查，便于提前捕获类型错误
function build_user(id: number): User {
    return { id, name: "Tom" }
}
```

---

**基本写法：TypeScript 5.2 using 资源管理**
`using <resource> = <表达式>`

```typescript
// 使用 using 声明在作用域结束时自动释放资源
function process() {
    using resource = get_resource()
    // 函数结束时自动调用 resource[Symbol.dispose]()
}
```

---

**基本写法：TypeScript 5.4 NoInfer 工具类型**
`NoInfer<T>`

```typescript
// 使用 NoInfer 阻止类型参数的逆向推断
function create_pair<T>(first: T, second: NoInfer<T>): [T, T] {
    return [first, second]
}
```

---

**基本写法：TypeScript 5.5 推断类型谓词**
`(<param>) => <param> is <类型>`

```typescript
// 自动推断类型谓词，无需显式标注 is 类型守卫
const is_string = (x: unknown) => typeof x === "string"
// 推断为 (x: unknown) => x is string
```

---

**基本写法：TypeScript 5.6 不允许真值比较**
`if (<cond> === true)`

```typescript
// 启用 --strictBooleanExpressions 后必须显式比较布尔值
function process(value?: boolean) {
    if (value === true) {
        console.log("值为 true")
    }
}
```

---

**基本写法：TypeScript 5.7 默认导入解析约束**
`import <名称> from "<模块>"`

```typescript
// 5.7 默认使用 bundler 解析模式，类型导入需显式标注 type 修饰符
import type { User } from "./types"
import { UserService } from "./service"
```

---

**基本写法：TypeScript 5.8 --erasableSyntaxOnly 选项**
`// tsconfig.json 中设置 "erasableSyntaxOnly": true`

```typescript
// 启用后仅允许类型层面的可擦除语法，禁止 enum 和 namespace 等运行时构造
type Status = "active" | "inactive"
// 以下写法将被禁止：
// enum Status { Active, Inactive }
```



<!-- ============ 文档分隔线：009-typescript/003-BasicTypeSystem.md ============ -->

# 基础类型系统

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 原始类型

**基本写法：布尔类型**
`let <变量>: boolean = <值>`

```typescript
// 布尔类型
let is_active: boolean = true
```

---

**基本写法：数字类型**
`let <变量>: number = <值>`

```typescript
// 数字类型
let count: number = 42
```

---

**基本写法：字符串类型**
`let <变量>: string = <值>`

```typescript
// 字符串类型
let name: string = "Alice"
```

---

**基本写法：空值类型**
`let <变量>: void = undefined`

```typescript
// void 类型（通常用于函数返回值）
let unused: void = undefined
```

---

**基本写法：null 类型**
`let <变量>: null = null`

```typescript
// null 类型
let empty: null = null
```

---

**基本写法：undefined 类型**
`let <变量>: undefined = undefined`

```typescript
// undefined 类型
let not_defined: undefined = undefined
```

---

**基本写法：symbol 类型**
`let <变量>: symbol = Symbol(<描述>)`

```typescript
// symbol 类型
let unique_id: symbol = Symbol("id")
```

---

**基本写法：bigint 类型**
`let <变量>: bigint = <大整数>n`

```typescript
// bigint 类型
let large_number: bigint = 9007199254740991n
```

---

## 数组类型

**基本写法：使用类型加方括号**
`let <变量>: <类型>[] = [<值>]`

```typescript
// 数字数组
let numbers: number[] = [1, 2, 3]
```

---

**基本写法：使用泛型数组**
`let <变量>: Array<<类型>> = [<值>]`

```typescript
// 使用泛型语法的字符串数组
let names: Array<string> = ["Alice", "Bob"]
```

---

**换行写法：多行数组定义**
`let <变量>: <类型>[] = [`
`    <值1>,`
`    <值2>,`
`]`

```typescript
// 多行数组定义
let users: string[] = [
    "Alice",
    "Bob",
    "Charlie",
]
```

---

## 元组类型

**单行写法：定义元组**
`let <变量>: [<类型1>, <类型2>] = [<值1>, <值2>]`

```typescript
// 元组类型（固定长度和类型的数组）
let person: [string, number] = ["Alice", 30]
```

---

**换行写法：多元素元组**
`let <变量>: [`
`    <类型1>,`
`    <类型2>,`
`    <类型3>,`
`] = [<值1>, <值2>, <值3>]`

```typescript
// 多元素元组定义
let record: [
    string,
    number,
    boolean,
] = ["Alice", 30, true]
```

---

## 枚举类型

**换行写法：数字枚举**
`enum <枚举名> {`
`    <成员1>,`
`    <成员2>,`
`}`

```typescript
// 数字枚举
enum Direction {
    Up,
    Down,
    Left,
    Right,
}
```

---

**换行写法：字符串枚举**
`enum <枚举名> {`
`    <成员1> = "<值1>",`
`    <成员2> = "<值2>",`
`}`

```typescript
// 字符串枚举
enum Color {
    Red = "RED",
    Green = "GREEN",
    Blue = "BLUE",
}
```

---

**基本写法：访问枚举成员**
`<枚举名>.<成员>`

```typescript
// 访问枚举成员
let direction: Direction = Direction.Up
```

---

## any 类型

**基本写法：使用 any 类型**
`let <变量>: any = <值>`

```typescript
// any 类型（允许任意类型赋值）
let data: any = "hello"
data = 123
```

---

## unknown 类型

**基本写法：使用 unknown 类型**
`let <变量>: unknown = <值>`

```typescript
// unknown 类型（安全的 any，使用前必须类型检查）
let value: unknown = "hello"
if (typeof value === "string") {
    console.log(value.toUpperCase())
}
```

---

## never 类型

**基本写法：使用 never 类型**
`function <函数>(): never { <语句> }`

```typescript
// never 类型（表示永不返回的函数）
function error(message: string): never {
    throw new Error(message)
}
```

---

**基本写法：无限循环返回 never**
`function <函数>(): never { while(true) {} }`

```typescript
// 无限循环返回 never
function infinite_loop(): never {
    while (true) {}
}
```

---

## object 类型

**基本写法：使用 object 类型**
`let <变量>: object = <对象>`

```typescript
// object 类型（表示非原始类型）
let obj: object = { name: "Alice" }
```

---

## 类型断言

**基本写法：使用尖括号断言**
`<<类型>><表达式>`

```typescript
// 尖括号语法类型断言
let value: any = "hello"
let length: number = (<string>value).length
```

---

**基本写法：使用 as 断言**
`<表达式> as <类型>`

```typescript
// as 语法类型断言
let value: any = "hello"
let length: number = (value as string).length
```

---

## 联合类型

**基本写法：联合类型**
`let <变量>: <类型1> | <类型2> = <值>`

```typescript
// 联合类型（可以是多种类型之一）
let id: string | number = 123
id = "ABC"
```

---

## 交叉类型

**基本写法：交叉类型**
`type <类型> = <类型1> & <类型2>`

```typescript
// 交叉类型（组合多个类型）
type Person = { name: string }
type Employee = { employee_id: number }
type Staff = Person & Employee
```

---

## 字面量类型

**基本写法：字符串字面量类型**
`let <变量>: "<值>" = "<值>"`

```typescript
// 字符串字面量类型
let direction: "left" = "left"
```

---

**基本写法：数字字面量类型**
`let <变量>: <数字> = <数字>`

```typescript
// 数字字面量类型
let dice: 6 = 6
```

---

## let 与 const

**基本写法：使用 let 声明变量**
`let <变量>: <类型> = <值>`

```typescript
// 使用 let 声明可变变量
let count: number = 0
count = 1
```

---

**基本写法：使用 const 声明常量**
`const <变量>: <类型> = <值>`

```typescript
// 使用 const 声明不可变常量
const PI: number = 3.14159
```

---

## 类型推断

**基本写法：自动类型推断**
`let <变量> = <值>`

```typescript
// 自动推断变量类型
let name = "Alice"  // 推断为 string
let count = 42      // 推断为 number
```

---

## 解构赋值类型

**基本写法：数组解构类型**
`let [<变量1>, <变量2>]: <类型>[] = <数组>`

```typescript
// 数组解构赋值
let [first, second]: number[] = [1, 2]
```

---

**基本写法：对象解构类型**
`let { <属性1>, <属性2> }: { <属性1>: <类型1>, <属性2>: <类型2> } = <对象>`

```typescript
// 对象解构赋值
let { name, age }: { name: string, age: number } = { name: "Alice", age: 30 }
```

---

## 函数类型

**基本写法：函数参数类型**
`function <函数名>(<参数>: <类型>): <返回类型> { <语句> }`

```typescript
// 函数参数和返回值类型注解
function add(a: number, b: number): number {
    return a + b
}
```

---

**基本写法：箭头函数类型**
`const <函数名> = (<参数>: <类型>): <返回类型> => <表达式>`

```typescript
// 箭头函数类型注解
const greet = (name: string): string => `Hello, ${name}`
```

---

**基本写法：可选参数**
`function <函数名>(<参数1>: <类型>, <参数2>?: <类型>): <返回类型> { <语句> }`

```typescript
// 可选参数（使用 ? 标记）
function greet(name: string, greeting?: string): string {
    return `${greeting || "Hello"}, ${name}`
}
```

---

**基本写法：默认参数**
`function <函数名>(<参数>: <类型> = <默认值>): <返回类型> { <语句> }`

```typescript
// 默认参数值
function greet(name: string = "World"): string {
    return `Hello, ${name}`
}
```

---

**基本写法：剩余参数**
`function <函数名>(...<参数>: <类型>[]): <返回类型> { <语句> }`

```typescript
// 剩余参数
function sum(...numbers: number[]): number {
    return numbers.reduce((a, b) => a + b, 0)
}
```

---

## 类型别名

**基本写法：定义类型别名**
`type <别名> = <类型>`

```typescript
// 定义类型别名
type ID = string | number
```

---

## 可空类型

**基本写法：可空类型**
`let <变量>: <类型> | null = <值>`

```typescript
// 可空类型（值为指定类型或 null）
let name: string | null = "Alice"
name = null
```

---

## 可选链

**基本写法：使用可选链**
`<对象>?.<属性>`

```typescript
// 可选链操作符
let user: { name?: string } = {}
let name: string | undefined = user?.name
```

---

## 空值合并

**基本写法：使用空值合并**
`<值> ?? <默认值>`

```typescript
// 空值合并运算符
let name: string | null = null
let display_name: string = name ?? "Anonymous"
```



<!-- ============ 文档分隔线：009-typescript/004-InterfaceTypeAlias.md ============ -->

# 接口与类型别名

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 接口定义

**换行写法：定义基本接口**
`interface <接口名> {`
`    <属性1>: <类型1>`
`    <属性2>: <类型2>`
`}`

```typescript
// 定义基本接口
interface User {
    name: string
    age: number
}
```

---

**基本写法：使用接口**
`let <变量>: <接口名> = { <属性>: <值> }`

```typescript
// 使用接口定义对象
let user: User = { name: "Alice", age: 30 }
```

---

## 可选属性

**换行写法：接口可选属性**
`interface <接口名> {`
`    <属性1>: <类型1>`
`    <属性2>?: <类型2>`
`}`

```typescript
// 接口可选属性（使用 ? 标记）
interface User {
    name: string
    age?: number
}
```

---

## 只读属性

**换行写法：接口只读属性**
`interface <接口名> {`
`    readonly <属性>: <类型>`
`}`

```typescript
// 接口只读属性
interface User {
    readonly id: number
    name: string
}
```

---

## 接口继承

**基本写法：单继承**
`interface <子接口> extends <父接口> { <属性>: <类型> }`

```typescript
// 接口单继承
interface Animal {
    name: string
}

interface Dog extends Animal {
    breed: string
}
```

---

**基本写法：多继承**
`interface <子接口> extends <父接口1>, <父接口2> { <属性>: <类型> }`

```typescript
// 接口多继承
interface Flyable {
    fly(): void
}

interface Swimmable {
    swim(): void
}

interface Duck extends Flyable, Swimmable {
    name: string
}
```

---

## 函数类型接口

**换行写法：定义函数类型接口**
`interface <接口名> {`
`    (<参数>: <类型>): <返回类型>`
`}`

```typescript
// 定义函数类型接口
interface SearchFunc {
    (source: string, sub: string): boolean
}
```

---

**基本写法：使用函数类型接口**
`let <变量>: <接口名> = (<参数>) => <表达式>`

```typescript
// 使用函数类型接口
let search: SearchFunc = (src, sub) => src.includes(sub)
```

---

## 可索引类型接口

**换行写法：字符串索引签名**
`interface <接口名> {`
`    [key: string]: <类型>`
`}`

```typescript
// 字符串索引签名
interface StringArray {
    [index: string]: string
}
```

---

**换行写法：数字索引签名**
`interface <接口名> {`
`    [index: number]: <类型>`
`}`

```typescript
// 数字索引签名
interface NumberArray {
    [index: number]: string
}
```

---

## 类类型接口

**换行写法：类实现接口**
`interface <接口名> {`
`    <方法>(<参数>): <返回类型>`
`}`
`class <类名> implements <接口名> { <语句> }`

```typescript
// 类实现接口
interface Clock {
    current_time: Date
    set_time(d: Date): void
}

class DigitalClock implements Clock {
    current_time = new Date()
    set_time(d: Date) {
        this.current_time = d
    }
}
```

---

## 类型别名

**基本写法：定义类型别名**
`type <别名> = <类型>`

```typescript
// 定义类型别名
type Name = string
type Age = number
```

---

**换行写法：对象类型别名**
`type <别名> = {`
`    <属性1>: <类型1>`
`    <属性2>: <类型2>`
`}`

```typescript
// 对象类型别名
type User = {
    name: string
    age: number
}
```

---

**基本写法：联合类型别名**
`type <别名> = <类型1> | <类型2>`

```typescript
// 联合类型别名
type ID = string | number
```

---

**基本写法：交叉类型别名**
`type <别名> = <类型1> & <类型2>`

```typescript
// 交叉类型别名
type Person = { name: string }
type Employee = { id: number }
type Staff = Person & Employee
```

---

## 接口与类型别名对比

**换行写法：接口扩展**
`interface <接口名> extends <父接口> { <属性>: <类型> }`

```typescript
// 接口扩展（使用 extends）
interface Animal {
    name: string
}

interface Dog extends Animal {
    breed: string
}
```

---

**基本写法：类型别名交叉**
`type <别名> = <类型1> & <类型2>`

```typescript
// 类型别名交叉（使用 &）
type Animal = { name: string }
type Dog = Animal & { breed: string }
```

---

## 函数类型

**基本写法：使用 type 定义函数类型**
`type <函数类型> = (<参数>: <类型>) => <返回类型>`

```typescript
// 使用 type 定义函数类型
type Callback = (data: string) => void
```

---

**基本写法：使用 interface 定义函数类型**
`interface <函数类型> { (<参数>: <类型>): <返回类型> }`

```typescript
// 使用 interface 定义函数类型
interface Callback {
    (data: string): void
}
```

---

## 合并接口

**换行写法：接口声明合并**
`interface <接口名> { <属性1>: <类型1> }`
`interface <接口名> { <属性2>: <类型2> }`

```typescript
// 接口声明合并（同名接口自动合并）
interface Box {
    width: number
}

interface Box {
    height: number
}
```

---

## 描述对象

**换行写法：描述复杂对象**
`interface <接口名> {`
`    <属性>: <类型>`
`    <嵌套对象>: {`
`        <子属性>: <类型>`
`    }`
`}`

```typescript
// 描述复杂嵌套对象
interface User {
    name: string
    address: {
        street: string
        city: string
    }
}
```

---

## 数组类型接口

**换行写法：描述对象数组**
`interface <接口名> {`
`    <属性>: <类型>`
`}`
`let <变量>: <接口名>[] = [<对象>]`

```typescript
// 描述对象数组
interface Product {
    name: string
    price: number
}

let products: Product[] = [
    { name: "Apple", price: 1.5 },
    { name: "Banana", price: 0.5 },
]
```

---

## readonly 与 Readonly

**基本写法：使用 readonly 修饰符**
`interface <接口名> { readonly <属性>: <类型> }`

```typescript
// 使用 readonly 修饰符
interface Point {
    readonly x: number
    readonly y: number
}
```

---

**基本写法：使用 Readonly 工具类型**
`type <别名> = Readonly<<接口>>`

```typescript
// 使用 Readonly 工具类型
type ReadonlyUser = Readonly<User>
```

---

## Partial 与 Required

**基本写法：使用 Partial 工具类型**
`type <别名> = Partial<<接口>>`

```typescript
// 使用 Partial 使所有属性可选
type PartialUser = Partial<User>
```

---

**基本写法：使用 Required 工具类型**
`type <别名> = Required<<接口>>`

```typescript
// 使用 Required 使所有属性必填
type RequiredUser = Required<User>
```

---

## Pick 与 Omit

**基本写法：使用 Pick 工具类型**
`type <别名> = Pick<<接口>, "<属性1>" | "<属性2>">`

```typescript
// 使用 Pick 选取部分属性
type UserBasic = Pick<User, "name" | "age">
```

---

**基本写法：使用 Omit 工具类型**
`type <别名> = Omit<<接口>, "<属性>">`

```typescript
// 使用 Omit 排除部分属性
type UserWithoutAge = Omit<User, "age">
```

---

## Record 类型

**基本写法：使用 Record 工具类型**
`type <别名> = Record<<键类型>, <值类型>>`

```typescript
// 使用 Record 创建键值对类型
type UserMap = Record<string, User>
```

---

## 函数参数类型

**换行写法：描述函数参数对象**
`interface <参数接口> {`
`    <属性1>: <类型1>`
`    <属性2>: <类型2>`
`}`
`function <函数>(<参数>: <参数接口>): <返回类型> { <语句> }`

```typescript
// 描述函数参数对象
interface Config {
    host: string
    port: number
    timeout?: number
}

function connect(config: Config): void {
    console.log(`${config.host}:${config.port}`)
}
```

---

## 可调用接口

**换行写法：可调用对象接口**
`interface <接口名> {`
`    (<参数>: <类型>): <返回类型>`
`    <属性>: <类型>`
`}`

```typescript
// 可调用对象接口（既是函数又有属性）
interface Counter {
    (start: number): void
    count: number
}
```

---

## 构造器类型

**换行写法：构造器接口**
`interface <接口名> {`
`    new (<参数>: <类型>): <对象类型>`
`}`

```typescript
// 构造器接口
interface ClockConstructor {
    new (hour: number, minute: number): ClockInterface
}

interface ClockInterface {
    tick(): void
}
```



<!-- ============ 文档分隔线：009-typescript/005-TypeGuardCustomGuard.md ============ -->

# 类型守卫与自定义守卫

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## typeof 类型守卫

**基本写法：使用 typeof 收窄类型**
`if (typeof <变量> === "<类型>") { <语句> }`

```typescript
// 使用 typeof 类型守卫
function process(value: string | number): void {
    if (typeof value === "string") {
        console.log(value.toUpperCase())
    } else {
        console.log(value.toFixed(2))
    }
}
```

---

**基本写法：typeof 检查多种类型**
`if (typeof <变量> === "<类型1>" || typeof <变量> === "<类型2>") { <语句> }`

```typescript
// typeof 检查多种类型
function process(value: string | number | boolean): void {
    if (typeof value === "string" || typeof value === "number") {
        console.log(value.toString())
    } else {
        console.log(value)
    }
}
```

---

## instanceof 类型守卫

**基本写法：使用 instanceof 收窄类型**
`if (<变量> instanceof <类>) { <语句> }`

```typescript
// 使用 instanceof 类型守卫
class Dog {
    bark(): void {}
}

class Cat {
    meow(): void {}
}

function speak(animal: Dog | Cat): void {
    if (animal instanceof Dog) {
        animal.bark()
    } else {
        animal.meow()
    }
}
```

---

**基本写法：instanceof 检查多个类**
`if (<变量> instanceof <类1> || <变量> instanceof <类2>) { <语句> }`

```typescript
// instanceof 检查多个类
function process(obj: Dog | Cat | Bird): void {
    if (obj instanceof Dog || obj instanceof Cat) {
        console.log("哺乳动物")
    } else {
        console.log("鸟类")
    }
}
```

---

## in 类型守卫

**基本写法：使用 in 收窄类型**
`if ("<属性>" in <对象>) { <语句> }`

```typescript
// 使用 in 操作符类型守卫
function process(obj: { a: string } | { b: number }): void {
    if ("a" in obj) {
        console.log(obj.a)
    } else {
        console.log(obj.b)
    }
}
```

---

**基本写法：in 检查多个属性**
`if ("<属性1>" in <对象> && "<属性2>" in <对象>) { <语句> }`

```typescript
// in 检查多个属性
function process(obj: { a?: string } | { b?: number }): void {
    if ("a" in obj && "b" in obj) {
        console.log("同时具有 a 和 b")
    }
}
```

---

## 可辨识联合类型守卫

**换行写法：可辨识联合类型**
`type <类型> =`
`    | { kind: "<标识1>", <属性1>: <类型1> }`
`    | { kind: "<标识2>", <属性2>: <类型2> }`

```typescript
// 可辨识联合类型
type Shape =
    | { kind: "circle", radius: number }
    | { kind: "square", size: number }
```

---

**基本写法：使用可辨识属性收窄类型**
`if (<变量>.kind === "<标识>") { <语句> }`

```typescript
// 使用可辨识属性类型守卫
function area(shape: Shape): number {
    if (shape.kind === "circle") {
        return Math.PI * shape.radius ** 2
    } else {
        return shape.size ** 2
    }
}
```

---

**换行写法：使用 switch 收窄类型**
`switch (<变量>.kind) {`
`    case "<标识1>": return <处理1>`
`    case "<标识2>": return <处理2>`
`}`

```typescript
// 使用 switch 收窄类型
function area(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2
        case "square":
            return shape.size ** 2
    }
}
```

---

## 自定义类型守卫

**换行写法：定义自定义类型守卫**
`function <函数>(<参数>: <类型>): <参数> is <目标类型> {`
`    return <条件>`
`}`

```typescript
// 定义自定义类型守卫
function is_string(value: any): value is string {
    return typeof value === "string"
}
```

---

**基本写法：使用自定义类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用自定义类型守卫
let value: any = "hello"
if (is_string(value)) {
    console.log(value.toUpperCase())  // value 被收窄为 string
}
```

---

## 数组类型守卫

**换行写法：数组类型守卫**
`function <函数>(<参数>: any): <参数> is <类型>[] {`
`    return Array.isArray(<参数>) && <参数>.every(item => <检查>)`
`}`

```typescript
// 数组类型守卫
function is_string_array(value: any): value is string[] {
    return Array.isArray(value) && value.every(item => typeof item === "string")
}
```

---

**基本写法：使用数组类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用数组类型守卫
let value: any = ["a", "b", "c"]
if (is_string_array(value)) {
    value.forEach(item => console.log(item.toUpperCase()))
}
```

---

## 对象类型守卫

**换行写法：对象类型守卫**
`function <函数>(<参数>: any): <参数> is <接口> {`
`    return <参数> !== null && typeof <参数> === "object" && "<属性>" in <参数>`
`}`

```typescript
// 对象类型守卫
interface User {
    name: string
    age: number
}

function is_user(value: any): value is User {
    return value !== null
        && typeof value === "object"
        && "name" in value
        && "age" in value
}
```

---

**基本写法：使用对象类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用对象类型守卫
let value: any = { name: "Alice", age: 30 }
if (is_user(value)) {
    console.log(value.name)
}
```

---

## null 与 undefined 守卫

**基本写法：检查 null**
`if (<变量> !== null) { <语句> }`

```typescript
// 检查 null 后安全使用
function process(name: string | null): void {
    if (name !== null) {
        console.log(name.toUpperCase())
    }
}
```

---

**基本写法：检查 undefined**
`if (<变量> !== undefined) { <语句> }`

```typescript
// 检查 undefined 后安全使用
function process(value: string | undefined): void {
    if (value !== undefined) {
        console.log(value.toUpperCase())
    }
}
```

---

**基本写法：同时检查 null 和 undefined**
`if (<变量> != null) { <语句> }`

```typescript
// 同时检查 null 和 undefined
function process(value: string | null | undefined): void {
    if (value != null) {
        console.log(value.toUpperCase())
    }
}
```

---

## 类型断言守卫

**基本写法：使用 as 断言类型**
`<值> as <类型>`

```typescript
// 使用 as 类型断言
let value: any = "hello"
let length: number = (value as string).length
```

---

**基本写法：使用非空断言**
`<值>!`

```typescript
// 使用非空断言操作符
let value: string | null = "hello"
let length: number = value!.length
```

---

## 类型守卫与联合类型

**换行写法：联合类型守卫**
`function <函数>(<参数>: <类型1> | <类型2>): void {`
`    if (typeof <参数> === "<类型1>") { <处理1> }`
`    else { <处理2> }`
`}`

```typescript
// 联合类型守卫
function process(value: string | number): void {
    if (typeof value === "string") {
        console.log(value.toUpperCase())
    } else {
        console.log(value.toFixed(2))
    }
}
```

---

## 类型守卫与数组

**换行写法：数组元素类型守卫**
`function <函数>(<参数>: any[]): <参数> is <类型>[] {`
`    return <参数>.every(item => <检查>)`
`}`

```typescript
// 数组元素类型守卫
function is_number_array(value: any[]): value is number[] {
    return value.every(item => typeof item === "number")
}
```

---

**基本写法：使用数组元素守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用数组元素守卫
let value: any[] = [1, 2, 3]
if (is_number_array(value)) {
    let sum: number = value.reduce((a, b) => a + b, 0)
}
```

---

## 类型守卫与函数

**换行写法：函数类型守卫**
`function <函数>(<参数>: any): <参数> is (<值>: any) => <返回类型> {`
`    return typeof <参数> === "function"`
`}`

```typescript
// 函数类型守卫
function is_function(value: any): value is Function {
    return typeof value === "function"
}
```

---

**基本写法：使用函数类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用函数类型守卫
let value: any = () => "hello"
if (is_function(value)) {
    console.log(value())
}
```

---

## 类型守卫与 Promise

**换行写法：Promise 类型守卫**
`function <函数>(<参数>: any): <参数> is Promise<<类型>> {`
`    return <参数> instanceof Promise`
`}`

```typescript
// Promise 类型守卫
function is_promise<T>(value: any): value is Promise<T> {
    return value instanceof Promise
}
```

---

**基本写法：使用 Promise 类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用 Promise 类型守卫
let value: any = Promise.resolve("hello")
if (is_promise<string>(value)) {
    value.then(v => console.log(v.toUpperCase()))
}
```

---

## 类型守卫与 Error

**换行写法：Error 类型守卫**
`function <函数>(<参数>: any): <参数> is Error {`
`    return <参数> instanceof Error`
`}`

```typescript
// Error 类型守卫
function is_error(value: any): value is Error {
    return value instanceof Error
}
```

---

**基本写法：使用 Error 类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用 Error 类型守卫
try {
    // 可能抛出异常的代码
} catch (error) {
    if (is_error(error)) {
        console.log(error.message)
    } else {
        console.log(String(error))
    }
}
```

---

## 类型守卫与 Date

**换行写法：Date 类型守卫**
`function <函数>(<参数>: any): <参数> is Date {`
`    return <参数> instanceof Date`
`}`

```typescript
// Date 类型守卫
function is_date(value: any): value is Date {
    return value instanceof Date
}
```

---

**基本写法：使用 Date 类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用 Date 类型守卫
let value: any = new Date()
if (is_date(value)) {
    console.log(value.getFullYear())
}
```

---

## 类型守卫与类

**换行写法：类实例类型守卫**
`function <函数>(<参数>: any): <参数> is <类名> {`
`    return <参数> instanceof <类名>`
`}`

```typescript
// 类实例类型守卫
class User {
    constructor(public name: string) {}
}

function is_user(value: any): value is User {
    return value instanceof User
}
```

---

**基本写法：使用类实例类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用类实例类型守卫
let value: any = new User("Alice")
if (is_user(value)) {
    console.log(value.name)
}
```

---

## 类型守卫与可辨识联合

**换行写法：可辨识联合类型守卫**
`function <函数>(<参数>: <类型>): <参数> is { kind: "<标识>", <属性>: <类型> } {`
`    return <参数>.kind === "<标识>"`
`}`

```typescript
// 可辨识联合类型守卫
type Shape =
    | { kind: "circle", radius: number }
    | { kind: "square", size: number }

function is_circle(shape: Shape): shape is { kind: "circle", radius: number } {
    return shape.kind === "circle"
}
```

---

**基本写法：使用可辨识联合类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用可辨识联合类型守卫
let shape: Shape = { kind: "circle", radius: 5 }
if (is_circle(shape)) {
    console.log(shape.radius)
}
```

---

## 类型守卫与穷尽检查

**换行写法：使用 never 进行穷尽检查**
`function <函数>(<参数>: <类型>): <返回类型> {`
`    switch (<参数>.kind) {`
`        case "<标识1>": return <处理1>`
`        case "<标识2>": return <处理2>`
`        default: const _exhaustive: never = <参数> return _exhaustive`
`    }`
`}`

```typescript
// 使用 never 进行穷尽检查
function area(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2
        case "square":
            return shape.size ** 2
        default:
            const _exhaustive: never = shape
            return _exhaustive
    }
}
```

---

## 类型守卫与可选属性

**换行写法：可选属性类型守卫**
`function <函数>(<参数>: any): <参数> is { <属性>: <类型> } {`
`    return "<属性>" in <参数>`
`}`

```typescript
// 可选属性类型守卫
interface User {
    name: string
    age?: number
}

function has_age(user: User): user is { name: string, age: number } {
    return "age" in user && user.age !== undefined
}
```

---

**基本写法：使用可选属性类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用可选属性类型守卫
let user: User = { name: "Alice", age: 30 }
if (has_age(user)) {
    console.log(user.age)
}
```

---

## 类型守卫与字面量类型

**换行写法：字面量类型守卫**
`function <函数>(<参数>: string): <参数> is "<值>" {`
`    return <参数> === "<值>"`
`}`

```typescript
// 字面量类型守卫
function is_hello(value: string): value is "hello" {
    return value === "hello"
}
```

---

**基本写法：使用字面量类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用字面量类型守卫
let value: string = "hello"
if (is_hello(value)) {
    console.log(value)  // value 被收窄为 "hello"
}
```

---

## 类型守卫与联合类型数组

**换行写法：联合类型数组守卫**
`function <函数>(<参数>: (<类型1> | <类型2>)[]): <参数> is <类型1>[] {`
`    return <参数>.every(item => <检查>)`
`}`

```typescript
// 联合类型数组守卫
function is_all_strings(value: (string | number)[]): value is string[] {
    return value.every(item => typeof item === "string")
}
```

---

**基本写法：使用联合类型数组守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用联合类型数组守卫
let value: (string | number)[] = ["a", "b", "c"]
if (is_all_strings(value)) {
    value.forEach(item => console.log(item.toUpperCase()))
}
```

---

## 类型守卫与类型谓词

**换行写法：复杂类型谓词**
`function <函数>(<参数>: unknown): <参数> is { <属性1>: <类型1>, <属性2>: <类型2> } {`
`    if (typeof <参数> !== "object" || <参数> === null) return false`
`    return "<属性1>" in <参数> && "<属性2>" in <参数>`
`}`

```typescript
// 复杂类型谓词
interface User {
    name: string
    age: number
}

function is_user(value: unknown): value is User {
    if (typeof value !== "object" || value === null) {
        return false
    }
    return "name" in value && "age" in value
}
```

---

## 类型守卫与 assert

**换行写法：使用 assert 函数**
`function <函数>(<参数>: unknown): asserts <参数> is <类型> {`
`    if (!<检查>) throw new Error(<消息>)`
`}`

```typescript
// 使用 assert 函数
function assert_string(value: unknown): asserts value is string {
    if (typeof value !== "string") {
        throw new Error("Expected string")
    }
}
```

---

**基本写法：使用 assert 函数**
`<函数>(<值>)`

```typescript
// 使用 assert 函数
let value: unknown = "hello"
assert_string(value)
console.log(value.toUpperCase())  // value 被收窄为 string
```

---

**换行写法：assert 函数检查非 null**
`function <函数>(<参数>: unknown): asserts <参数> is NonNullable<typeof <参数>> {`
`    if (<参数> === null || <参数> === undefined) throw new Error(<消息>)`
`}`

```typescript
// assert 函数检查非 null
function assert_non_null<T>(value: T): asserts value is NonNullable<T> {
    if (value === null || value === undefined) {
        throw new Error("Value is null or undefined")
    }
}
```

---

**基本写法：使用 assert 非 null**
`<函数>(<值>)`

```typescript
// 使用 assert 非 null
let value: string | null = "hello"
assert_non_null(value)
console.log(value.toUpperCase())  // value 被收窄为 string
```



<!-- ============ 文档分隔线：009-typescript/006-ClassDecorator.md ============ -->

# 类与装饰器

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类定义

**换行写法：定义基本类**
`class <类名> {`
`    <属性>: <类型>`
`    <方法>(<参数>): <返回类型> { <语句> }`
`}`

```typescript
// 定义基本类
class User {
    name: string
    age: number

    greet(): string {
        return `Hello, ${this.name}`
    }
}
```

---

**基本写法：创建类实例**
`let <变量> = new <类名>(<参数>)`

```typescript
// 创建类实例
let user = new User()
```

---

## 构造函数

**换行写法：定义构造函数**
`class <类名> {`
`    constructor(<参数>: <类型>) { <语句> }`
`}`

```typescript
// 定义构造函数
class User {
    name: string

    constructor(name: string) {
        this.name = name
    }
}
```

---

**基本写法：构造函数参数简写**
`class <类名> {`
`    constructor(public <属性>: <类型>) {}`
`}`

```typescript
// 构造函数参数简写（自动创建属性）
class User {
    constructor(public name: string, public age: number) {}
}
```

---

## 属性修饰符

**换行写法：public 公有属性**
`class <类名> {`
`    public <属性>: <类型>`
`}`

```typescript
// public 公有属性（默认）
class User {
    public name: string = "Alice"
}
```

---

**换行写法：private 私有属性**
`class <类名> {`
`    private <属性>: <类型>`
`}`

```typescript
// private 私有属性
class User {
    private age: number = 30
}
```

---

**换行写法：protected 受保护属性**
`class <类名> {`
`    protected <属性>: <类型>`
`}`

```typescript
// protected 受保护属性
class User {
    protected id: number = 1
}
```

---

**换行写法：readonly 只读属性**
`class <类名> {`
`    readonly <属性>: <类型>`
`}`

```typescript
// readonly 只读属性
class User {
    readonly id: number

    constructor(id: number) {
        this.id = id
    }
}
```

---

**换行写法：static 静态属性**
`class <类名> {`
`    static <属性>: <类型>`
`}`

```typescript
// static 静态属性
class User {
    static count: number = 0
}
```

---

**基本写法：访问静态属性**
`<类名>.<静态属性>`

```typescript
// 访问静态属性
console.log(User.count)
```

---

## 方法

**换行写法：定义实例方法**
`class <类名> {`
`    <方法>(<参数>: <类型>): <返回类型> { <语句> }`
`}`

```typescript
// 定义实例方法
class User {
    greet(name: string): string {
        return `Hello, ${name}`
    }
}
```

---

**换行写法：定义静态方法**
`class <类名> {`
`    static <方法>(<参数>: <类型>): <返回类型> { <语句> }`
`}`

```typescript
// 定义静态方法
class User {
    static create(name: string): User {
        return new User(name)
    }
}
```

---

**换行写法：定义 getter**
`class <类名> {`
`    get <属性>(): <类型> { <语句> }`
`}`

```typescript
// 定义 getter
class User {
    private _name: string = ""

    get name(): string {
        return this._name
    }
}
```

---

**换行写法：定义 setter**
`class <类名> {`
`    set <属性>(<值>: <类型>) { <语句> }`
`}`

```typescript
// 定义 setter
class User {
    private _name: string = ""

    set name(value: string) {
        this._name = value
    }
}
```

---

## 继承

**换行写法：类继承**
`class <子类> extends <父类> {`
`    constructor(<参数>) { super(<参数>) }`
`}`

```typescript
// 类继承
class Animal {
    constructor(public name: string) {}
}

class Dog extends Animal {
    constructor(name: string, public breed: string) {
        super(name)
    }
}
```

---

**换行写法：方法重写**
`class <子类> extends <父类> {`
`    <方法>(<参数>): <返回类型> { <新语句> }`
`}`

```typescript
// 方法重写
class Animal {
    speak(): string {
        return "sound"
    }
}

class Dog extends Animal {
    speak(): string {
        return "Woof!"
    }
}
```

---

**基本写法：调用父类方法**
`super.<方法>(<参数>)`

```typescript
// 调用父类方法
class Dog extends Animal {
    speak(): string {
        return `${super.speak()} - Woof!`
    }
}
```

---

## 抽象类

**换行写法：定义抽象类**
`abstract class <类名> {`
`    abstract <方法>(<参数>): <返回类型>`
`}`

```typescript
// 定义抽象类
abstract class Animal {
    abstract speak(): string

    eat(): void {
        console.log("eating")
    }
}
```

---

**换行写法：实现抽象类**
`class <子类> extends <抽象类> {`
`    <方法>(<参数>): <返回类型> { <语句> }`
`}`

```typescript
// 实现抽象类
class Dog extends Animal {
    speak(): string {
        return "Woof!"
    }
}
```

---

## 接口实现

**换行写法：类实现接口**
`interface <接口> { <方法>(<参数>): <返回类型> }`
`class <类名> implements <接口> { <语句> }`

```typescript
// 类实现接口
interface Comparable {
    compare(other: any): number
}

class Number implements Comparable {
    constructor(public value: number) {}

    compare(other: Number): number {
        return this.value - other.value
    }
}
```

---

## 泛型类

**换行写法：定义泛型类**
`class <类名><<T>> {`
`    private <属性>: <T>[]`
`    <方法>(<参数>: <T>): void { <语句> }`
`}`

```typescript
// 定义泛型类
class Stack<T> {
    private items: T[] = []

    push(item: T): void {
        this.items.push(item)
    }

    pop(): T | undefined {
        return this.items.pop()
    }
}
```

---

**基本写法：使用泛型类**
`let <变量> = new <类名><<类型>>()`

```typescript
// 使用泛型类
let stack = new Stack<number>()
stack.push(1)
```

---

## 装饰器

**换行写法：类装饰器**
`function <装饰器>(<构造函数>: { new (...args: any[]): any }) { <语句> }`
`@<装饰器>`
`class <类名> { <语句> }`

```typescript
// 类装饰器
function logged<T extends { new (...args: any[]): any }>(constructor: T) {
    return class extends constructor {
        created_at = new Date()
    }
}

@logged
class User {
    constructor(public name: string) {}
}
```

---

**换行写法：方法装饰器**
`function <装饰器>(<目标>, <键>, <描述符>) { <语句> }`
`class <类名> {`
`    @<装饰器>`
`    <方法>(<参数>) { <语句> }`
`}`

```typescript
// 方法装饰器
function log(target: any, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value
    descriptor.value = function(...args: any[]) {
        console.log(`调用 ${key}`)
        return original.apply(this, args)
    }
}

class User {
    @log
    greet(name: string): string {
        return `Hello, ${name}`
    }
}
```

---

**换行写法：属性装饰器**
`function <装饰器>(<目标>, <键>) { <语句> }`
`class <类名> {`
`    @<装饰器>`
`    <属性>: <类型>`
`}`

```typescript
// 属性装饰器
function required(target: any, key: string) {
    console.log(`${key} 是必填的`)
}

class User {
    @required
    name: string = ""
}
```

---

**换行写法：参数装饰器**
`function <装饰器>(<目标>, <键>, <参数索引>) { <语句> }`
`class <类名> {`
`    <方法>(@<装饰器> <参数>: <类型>) { <语句> }`
`}`

```typescript
// 参数装饰器
function log_param(target: any, key: string, index: number) {
    console.log(`参数 ${index} of ${key}`)
}

class User {
    greet(@log_param name: string): string {
        return `Hello, ${name}`
    }
}
```

---

## 装饰器工厂

**换行写法：装饰器工厂**
`function <装饰器>(<参数>): <装饰器> {`
`    return function(<目标>) { <语句> }`
`}`

```typescript
// 装饰器工厂
function repeat(times: number) {
    return function(target: any, key: string, descriptor: PropertyDescriptor) {
        const original = descriptor.value
        descriptor.value = function(...args: any[]) {
            for (let i = 0; i < times; i++) {
                original.apply(this, args)
            }
        }
    }
}

class User {
    @repeat(3)
    greet(): void {
        console.log("Hello")
    }
}
```

---

## 访问器

**换行写法：使用 getter 和 setter**
`class <类名> {`
`    private _<属性>: <类型>`
`    get <属性>(): <类型> { return this._<属性> }`
`    set <属性>(<值>: <类型>) { this._<属性> = <值> }`
`}`

```typescript
// 使用 getter 和 setter 实现属性访问控制
class User {
    private _age: number = 0

    get age(): number {
        return this._age
    }

    set age(value: number) {
        if (value < 0 || value > 150) {
            throw new Error("Invalid age")
        }
        this._age = value
    }
}
```

---

## 静态块

**换行写法：静态初始化块**
`class <类名> {`
`    static <属性>: <类型>`
`    static { <语句> }`
`}`

```typescript
// 静态初始化块
class Config {
    static settings: Record<string, string>

    static {
        Config.settings = {
            host: "localhost",
            port: "8080",
        }
    }
}
```

---

## 私有字段

**换行写法：使用 # 私有字段**
`class <类名> {`
`    #<属性>: <类型>`
`}`

```typescript
// 使用 # 私有字段（ES2022+）
class User {
    #age: number

    constructor(age: number) {
        this.#age = age
    }

    get_age(): number {
        return this.#age
    }
}
```

---

## 类表达式

**基本写法：类表达式**
`const <变量> = class <类名> { <语句> }`

```typescript
// 类表达式
const User = class {
    constructor(public name: string) {}
}
```

---

## 抽象属性

**换行写法：抽象属性**
`abstract class <类名> {`
`    abstract <属性>: <类型>`
`}`

```typescript
// 抽象属性
abstract class Animal {
    abstract name: string

    abstract speak(): string
}
```

---

## 实现多个接口

**换行写法：实现多个接口**
`class <类名> implements <接口1>, <接口2> { <语句> }`

```typescript
// 实现多个接口
interface Comparable {
    compare(other: any): number
}

interface Serializable {
    serialize(): string
}

class User implements Comparable, Serializable {
    compare(other: User): number {
        return 0
    }

    serialize(): string {
        return "User"
    }
}
```

---

## this 类型

**换行写法：使用 this 类型**
`class <类名> {`
`    <方法>(<参数>: <类型>): this { return this }`
`}`

```typescript
// 使用 this 类型实现链式调用
class Calculator {
    private value = 0

    add(n: number): this {
        this.value += n
        return this
    }

    multiply(n: number): this {
        this.value *= n
        return this
    }
}
```

---

## 类与类型

**基本写法：类作为类型**
`let <变量>: <类名> = <实例>`

```typescript
// 类作为类型使用
class User {
    constructor(public name: string) {}
}

let user: User = new User("Alice")
```

---

**基本写法：使用 typeof 获取构造函数类型**
`type <别名> = typeof <类名>`

```typescript
// 获取类的构造函数类型
type UserConstructor = typeof User
```

---

## 类装饰器实战

**换行写法：使用类装饰器添加属性**
`function <装饰器><<T> extends { new (...args: any[]): any }>(<构造函数>: <T>) {`
`    return class extends <T> { <新属性> }`
`}`

```typescript
// 使用类装饰器添加属性
function timestamp<T extends { new (...args: any[]): any }>(constructor: T) {
    return class extends constructor {
        timestamp = Date.now()
    }
}

@timestamp
class User {
    constructor(public name: string) {}
}
```

---

## 方法装饰器实战

**换行写法：使用方法装饰器实现日志**
`function <装饰器>(<目标>, <键>, <描述符>) {`
`    const <原方法> = <描述符>.value`
`    <描述符>.value = function(...args) { <前置> return <原方法>.apply(this, args) }`
`}`

```typescript
// 使用方法装饰器实现日志
function log_execution(target: any, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value
    descriptor.value = function(...args: any[]) {
        console.log(`执行 ${key}，参数: ${args}`)
        const result = original.apply(this, args)
        console.log(`${key} 执行完成`)
        return result
    }
}

class Calculator {
    @log_execution
    add(a: number, b: number): number {
        return a + b
    }
}
```

---

## 属性装饰器实战

**换行写法：使用属性装饰器实现验证**
`function <装饰器>(<目标>, <键>) {`
`    let <值>: <类型>`
`    Object.defineProperty(<目标>, <键>, { get, set })`
`}`

```typescript
// 使用属性装饰器实现验证
function validate_age(target: any, key: string) {
    let value: number

    Object.defineProperty(target, key, {
        get() { return value },
        set(new_value: number) {
            if (new_value < 0 || new_value > 150) {
                throw new Error("Invalid age")
            }
            value = new_value
        }
    })
}

class User {
    @validate_age
    age: number = 0
}
```



<!-- ============ 文档分隔线：009-typescript/007-EnumAdvanced.md ============ -->

# 枚举进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数字枚举

**换行写法：定义数字枚举**
`enum <枚举名> {`
`    <成员1>,`
`    <成员2>,`
`}`

```typescript
// 定义数字枚举（自动从 0 开始递增）
enum Direction {
    Up,
    Down,
    Left,
    Right,
}
```

---

**换行写法：指定起始值的数字枚举**
`enum <枚举名> {`
`    <成员1> = <值>,`
`    <成员2>,`
`}`

```typescript
// 指定起始值的数字枚举
enum Direction {
    Up = 1,
    Down,
    Left,
    Right,
}
```

---

**换行写法：指定每个成员的值**
`enum <枚举名> {`
`    <成员1> = <值1>,`
`    <成员2> = <值2>,`
`}`

```typescript
// 指定每个成员的值
enum StatusCode {
    OK = 200,
    NotFound = 404,
    ServerError = 500,
}
```

---

**基本写法：访问数字枚举成员**
`<枚举名>.<成员>`

```typescript
// 访问数字枚举成员
let direction: Direction = Direction.Up
```

---

**基本写法：反向映射（数字枚举）**
`<枚举名>[<数字>]`

```typescript
// 数字枚举的反向映射
let name: string = Direction[0]  // "Up"
```

---

## 字符串枚举

**换行写法：定义字符串枚举**
`enum <枚举名> {`
`    <成员1> = "<值1>",`
`    <成员2> = "<值2>",`
`}`

```typescript
// 定义字符串枚举
enum Color {
    Red = "RED",
    Green = "GREEN",
    Blue = "BLUE",
}
```

---

**基本写法：访问字符串枚举成员**
`<枚举名>.<成员>`

```typescript
// 访问字符串枚举成员
let color: Color = Color.Red
```

---

**基本写法：获取字符串枚举的值**
`<枚举名>.<成员>`

```typescript
// 获取字符串枚举的值
let value: string = Color.Red  // "RED"
```

---

## 异构枚举

**换行写法：混合数字和字符串枚举**
`enum <枚举名> {`
`    <成员1> = <数字>,`
`    <成员2> = "<字符串>",`
`}`

```typescript
// 混合数字和字符串的异构枚举
enum Boolean {
    No = 0,
    Yes = "YES",
}
```

---

## 常量枚举

**换行写法：定义常量枚举**
`const enum <枚举名> {`
`    <成员1>,`
`    <成员2>,`
`}`

```typescript
// 定义常量枚举（编译时内联，不生成代码）
const enum Direction {
    Up,
    Down,
    Left,
    Right,
}
```

---

**基本写法：使用常量枚举**
`let <变量>: <枚举名> = <枚举名>.<成员>`

```typescript
// 使用常量枚举（编译时替换为具体值）
let direction: Direction = Direction.Up
```

---

## 枚举与联合类型

**换行写法：从枚举提取联合类型**
`type <类型> = \`${<枚举名>}\``

```typescript
// 从枚举提取字符串联合类型
enum Color {
    Red = "RED",
    Green = "GREEN",
    Blue = "BLUE",
}

type ColorValue = `${Color}`  // "RED" | "GREEN" | "BLUE"
```

---

**基本写法：枚举成员作为类型**
`type <类型> = <枚举名>.<成员>`

```typescript
// 枚举成员作为类型
type RedColor = Color.Red
```

---

## 枚举与映射类型

**换行写法：枚举键映射**
`type <类型> = {`
`    [P in <枚举名>]: <类型>`
`}`

```typescript
// 从枚举创建映射类型
enum Status {
    Active = "ACTIVE",
    Inactive = "INACTIVE",
}

type StatusMessages = {
    [P in Status]: string
}
```

---

**换行写法：枚举值映射**
`type <类型> = {`
`    [P in <枚举名>]: <类型>`
`}`

```typescript
// 从枚举创建值映射类型
type StatusConfig = {
    [P in Status]: {
        label: string
        color: string
    }
}
```

---

## 枚举与条件类型

**换行写法：枚举条件类型**
`type <类型> = <T> extends <枚举名> ? <真类型> : <假类型>`

```typescript
// 枚举条件类型
type IsColor<T> = T extends Color ? true : false
```

---

## 枚举方法

**换行写法：枚举与命名空间合并**
`enum <枚举名> { <成员> }`
`namespace <枚举名> {`
`    export function <方法>(<参数>): <返回类型> { <语句> }`
`}`

```typescript
// 枚举与命名空间合并（为枚举添加方法）
enum Color {
    Red = "RED",
    Green = "GREEN",
    Blue = "BLUE",
}

namespace Color {
    export function from_string(value: string): Color | undefined {
        switch (value) {
            case "RED": return Color.Red
            case "GREEN": return Color.Green
            case "BLUE": return Color.Blue
            default: return undefined
        }
    }
}
```

---

**基本写法：调用枚举方法**
`<枚举名>.<方法>(<参数>)`

```typescript
// 调用枚举方法
let color = Color.from_string("RED")
```

---

## 枚举与对象

**换行写法：使用对象替代枚举**
`const <对象> = {`
`    <成员1>: "<值1>",`
`    <成员2>: "<值2>",`
`} as const`

```typescript
// 使用对象替代枚举（使用 as const）
const Color = {
    Red: "RED",
    Green: "GREEN",
    Blue: "BLUE",
} as const
```

---

**基本写法：从对象提取类型**
`type <类型> = typeof <对象>[keyof typeof <对象>]`

```typescript
// 从对象提取联合类型
type ColorValue = typeof Color[keyof typeof Color]  // "RED" | "GREEN" | "BLUE"
```

---

## 枚举与 switch

**换行写法：枚举与 switch 语句**
`function <函数>(<参数>: <枚举名>): <返回类型> {`
`    switch (<参数>) {`
`        case <枚举名>.<成员1>: return <处理1>`
`        case <枚举名>.<成员2>: return <处理2>`
`    }`
`}`

```typescript
// 枚举与 switch 语句
function get_color_name(color: Color): string {
    switch (color) {
        case Color.Red:
            return "红色"
        case Color.Green:
            return "绿色"
        case Color.Blue:
            return "蓝色"
    }
}
```

---

## 枚举与穷尽检查

**换行写法：使用 never 进行穷尽检查**
`function <函数>(<参数>: <枚举名>): <返回类型> {`
`    switch (<参数>) {`
`        case <枚举名>.<成员1>: return <处理1>`
`        case <枚举名>.<成员2>: return <处理2>`
`        default: const _exhaustive: never = <参数> return _exhaustive`
`    }`
`}`

```typescript
// 使用 never 进行穷尽检查
function get_color_name(color: Color): string {
    switch (color) {
        case Color.Red:
            return "红色"
        case Color.Green:
            return "绿色"
        case Color.Blue:
            return "蓝色"
        default:
            const _exhaustive: never = color
            return _exhaustive
    }
}
```

---

## 枚举与 const 断言

**换行写法：使用 const 断言替代枚举**
`const <对象> = {`
`    <成员1>: <值1>,`
`    <成员2>: <值2>,`
`} as const`
`type <类型> = keyof typeof <对象>`

```typescript
// 使用 const 断言替代枚举
const Direction = {
    Up: "UP",
    Down: "DOWN",
    Left: "LEFT",
    Right: "RIGHT",
} as const

type Direction = keyof typeof Direction  // "Up" | "Down" | "Left" | "Right"
```

---

**基本写法：使用 const 断言对象**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用 const 断言对象
let direction: Direction = "Up"
```

---

## 枚举与映射

**换行写法：枚举值映射**
`const <映射>: Record<<枚举名>, <类型>> = {`
`    [<枚举名>.<成员1>]: <值1>,`
`    [<枚举名>.<成员2>]: <值2>,`
`}`

```typescript
// 枚举值映射
const ColorHex: Record<Color, string> = {
    [Color.Red]: "#FF0000",
    [Color.Green]: "#00FF00",
    [Color.Blue]: "#0000FF",
}
```

---

**基本写法：访问枚举映射**
`<映射>[<枚举名>.<成员>]`

```typescript
// 访问枚举映射
let hex: string = ColorHex[Color.Red]
```

---

## 枚举与类型守卫

**换行写法：枚举类型守卫**
`function <函数>(<参数>: any): <参数> is <枚举名> {`
`    return Object.values(<枚举名>).includes(<参数>)`
`}`

```typescript
// 枚举类型守卫
function is_color(value: any): value is Color {
    return Object.values(Color).includes(value)
}
```

---

**基本写法：使用枚举类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用枚举类型守卫
let value: any = "RED"
if (is_color(value)) {
    let color: Color = value
}
```

---

## 枚举与反向映射

**换行写法：字符串枚举反向映射**
`const <映射>: Record<string, <枚举名>> = {`
`    ["<值1>"]: <枚举名>.<成员1>,`
`    ["<值2>"]: <枚举名>.<成员2>,`
`}`

```typescript
// 字符串枚举反向映射
const ColorFromValue: Record<string, Color> = {
    ["RED"]: Color.Red,
    ["GREEN"]: Color.Green,
    ["BLUE"]: Color.Blue,
}
```

---

**基本写法：使用反向映射**
`let <变量>: <枚举名> = <映射>["<值>"]`

```typescript
// 使用反向映射
let color: Color = ColorFromValue["RED"]
```

---

## 枚举与迭代

**换行写法：迭代枚举值**
`for (const <值> of Object.values(<枚举名>)) { <语句> }`

```typescript
// 迭代枚举值
for (const color of Object.values(Color)) {
    console.log(color)
}
```

---

**换行写法：迭代枚举键值对**
`for (const [<键>, <值>] of Object.entries(<枚举名>)) { <语句> }`

```typescript
// 迭代枚举键值对
for (const [key, value] of Object.entries(Color)) {
    console.log(`${key}: ${value}`)
}
```

---

## 枚举与工具类型

**换行写法：获取枚举所有值**
`type <类型> = \`${<枚举名>}\``

```typescript
// 获取枚举所有值的联合类型
type ColorValues = `${Color}`  // "RED" | "GREEN" | "BLUE"
```

---

**换行写法：获取枚举所有键**
`type <类型> = keyof typeof <枚举名>`

```typescript
// 获取枚举所有键的联合类型
type ColorKeys = keyof typeof Color  // "Red" | "Green" | "Blue"
```

---

## 枚举与函数

**换行写法：枚举作为函数参数**
`function <函数>(<参数>: <枚举名>): <返回类型> { <语句> }`

```typescript
// 枚举作为函数参数
function get_color_code(color: Color): string {
    return color
}
```

---

**换行写法：枚举作为函数返回值**
`function <函数>(<参数>: <类型>): <枚举名> { <语句> }`

```typescript
// 枚举作为函数返回值
function parse_color(value: string): Color {
    switch (value) {
        case "RED": return Color.Red
        case "GREEN": return Color.Green
        case "BLUE": return Color.Blue
        default: throw new Error("Invalid color")
    }
}
```

---

## 枚举与接口

**换行写法：枚举与接口组合**
`interface <接口> {`
`    <属性>: <枚举名>`
`}`

```typescript
// 枚举与接口组合
interface User {
    name: string
    status: Status
}
```

---

**换行写法：枚举与类型别名**
`type <类型> = {`
`    <属性>: <枚举名>`
`}`

```typescript
// 枚举与类型别名组合
type Config = {
    color: Color
    direction: Direction
}
```



<!-- ============ 文档分隔线：009-typescript/008-TemplateLiteralType.md ============ -->

# 模板字面量类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本模板字面量类型

**基本写法：基本模板字面量类型**
`type <类型> = \`<前缀>\${<类型>}\``

```typescript
// 基本模板字面量类型
type Greeting = `hello ${string}`
```

---

**基本写法：使用模板字面量类型**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用模板字面量类型
let greeting: Greeting = "hello world"
```

---

## 联合类型模板字面量

**换行写法：联合类型模板字面量**
`type <类型> = \`<前缀>\${<类型1> | <类型2>}\``

```typescript
// 联合类型模板字面量
type Side = "left" | "right"
type Direction = `turn ${Side}`
```

---

**基本写法：使用联合类型模板字面量**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用联合类型模板字面量
let direction: Direction = "turn left"
```

---

## 多变量模板字面量

**换行写法：多变量模板字面量**
`type <类型> = \`\${<类型1>}_\${<类型2>}\``

```typescript
// 多变量模板字面量
type Border = `${"top" | "bottom"}-${"left" | "right"}`
```

---

**基本写法：使用多变量模板字面量**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用多变量模板字面量
let corner: Border = "top-left"
```

---

## 字符串操作类型

**基本写法：使用 Uppercase 转大写**
`type <类型> = Uppercase<<字符串类型>>`

```typescript
// 将字符串类型转为大写
type Upper = Uppercase<"hello">  // "HELLO"
```

---

**基本写法：使用 Lowercase 转小写**
`type <类型> = Lowercase<<字符串类型>>`

```typescript
// 将字符串类型转为小写
type Lower = Lowercase<"HELLO">  // "hello"
```

---

**基本写法：使用 Capitalize 首字母大写**
`type <类型> = Capitalize<<字符串类型>>`

```typescript
// 将字符串类型首字母大写
type Capitalized = Capitalize<"hello">  // "Hello"
```

---

**基本写法：使用 Uncapitalize 首字母小写**
`type <类型> = Uncapitalize<<字符串类型>>`

```typescript
// 将字符串类型首字母小写
type Uncapitalized = Uncapitalize<"Hello">  // "hello"
```

---

## 模板字面量与映射类型

**换行写法：使用模板字面量重映射键**
`type <类型><<T>> = {`
`    [P in keyof T as \`get_\${P & string}\`]: T[P]`
`}`

```typescript
// 使用模板字面量为键添加前缀
type Getters<T> = {
    [P in keyof T as `get_${P & string}`]: () => T[P]
}
```

---

**换行写法：使用 Capitalize 重映射键**
`type <类型><<T>> = {`
`    [P in keyof T as \`on\${Capitalize<P & string>}\`]: T[P]`
`}`

```typescript
// 使用 Capitalize 为键添加 on 前缀
type EventHandlers<T> = {
    [P in keyof T as `on${Capitalize<P & string>}`]: (value: T[P]) => void
}
```

---

## 模板字面量与 infer

**换行写法：使用 infer 推断模板字面量**
`type <类型> = <S> extends \`prefix_\${infer <T>}\` ? <T> : never`

```typescript
// 使用 infer 推断模板字面量中的类型
type RemovePrefix<S> = S extends `prefix_${infer T}` ? T : never
```

---

**换行写法：推断字符串前缀**
`type <类型> = <S> extends \`${infer <Prefix>}_suffix\` ? <Prefix> : never`

```typescript
// 推断字符串前缀
type GetPrefix<S> = S extends `${infer Prefix}_suffix` ? Prefix : never
```

---

**换行写法：推断字符串两部分**
`type <类型> = <S> extends \`${infer <First>}_\${infer <Second>}\` ? [<First>, <Second>] : never`

```typescript
// 推断字符串的两部分
type Split<S> = S extends `${infer First}_${infer Second}` ? [First, Second] : never
```

---

## 模板字面量实战

**换行写法：生成 getter 方法名**
`type <类型><<T>> = {`
`    [P in keyof T as \`get\${Capitalize<P & string>}\`]: () => T[P]`
`}`

```typescript
// 为所有属性生成 getter 方法名
type Getters<T> = {
    [P in keyof T as `get${Capitalize<P & string>}`]: () => T[P]
}
```

---

**换行写法：生成 setter 方法名**
`type <类型><<T>> = {`
`    [P in keyof T as \`set\${Capitalize<P & string>}\`]: (<值>: T[P]) => void`
`}`

```typescript
// 为所有属性生成 setter 方法名
type Setters<T> = {
    [P in keyof T as `set${Capitalize<P & string>}`]: (value: T[P]) => void
}
```

---

**换行写法：生成事件处理器**
`type <类型><<T>> = {`
`    [P in keyof T as \`on\${Capitalize<P & string>}\`]: (<值>: T[P]) => void`
`}`

```typescript
// 为所有属性生成事件处理器
type EventHandlers<T> = {
    [P in keyof T as `on${Capitalize<P & string>}`]: (value: T[P]) => void
}
```

---

## 模板字面量与联合类型

**换行写法：从联合类型生成字符串**
`type <类型> = \`\${<联合类型1>}_\${<联合类型2>}\``

```typescript
// 从联合类型生成所有组合
type Prefix = "get" | "set"
type Suffix = "Name" | "Age"
type MethodName = `${Prefix}${Suffix}`
```

---

**基本写法：使用联合类型模板字面量**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用联合类型模板字面量
let method: MethodName = "getName"
```

---

## 模板字面量与条件类型

**换行写法：条件类型与模板字面量**
`type <类型> = <S> extends \`\${infer <T>}\` ? <T> : never`

```typescript
// 条件类型与模板字面量组合
type ExtractString<S> = S extends `${infer T}` ? T : never
```

---

**换行写法：检查字符串前缀**
`type <类型> = <S> extends \`prefix_\${string}\` ? true : false`

```typescript
// 检查字符串是否有指定前缀
type HasPrefix<S> = S extends `prefix_${string}` ? true : false
```

---

## 模板字面量与 keyof

**换行写法：从对象键生成事件名**
`type <类型> = \`on\${Capitalize<keyof <接口> & string>}\``

```typescript
// 从对象键生成事件名
interface User {
    name: string
    age: number
}

type UserEvent = `on${Capitalize<keyof User & string>}`
```

---

**基本写法：使用 keyof 模板字面量**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用 keyof 模板字面量
let event: UserEvent = "onName"
```

---

## 模板字面量与递归

**换行写法：递归处理字符串**
`type <类型> = <S> extends \`${infer <First>}\${infer <Rest>}\` ? <处理> : <S>`

```typescript
// 递归处理字符串
type Reverse<S> = S extends `${infer First}${infer Rest}` ? `${Reverse<Rest>}${First}` : S
```

---

**换行写法：递归替换字符**
`type <类型> = <S> extends \`${infer <Before>}_\${infer <After>}\` ? <类型><\`${<Before>}-\${<After>}\`> : <S>`

```typescript
// 递归替换下划线为连字符
type Replace<S> = S extends `${infer Before}_${infer After}` ? Replace<`${Before}-${After}`> : S
```

---

## 模板字面量与类型推断

**换行写法：推断函数名**
`type <类型> = <F> extends \`\${infer <Prefix>}\${string}\` ? <Prefix> : never`

```typescript
// 推断函数名前缀
type GetPrefix<F> = F extends `${infer Prefix}${string}` ? Prefix : never
```

---

**换行写法：推断属性路径**
`type <类型> = <P> extends \`\${infer <First>}.\${infer <Rest>}\` ? <处理> : <P>`

```typescript
// 推断属性路径
type GetFirstPath<P> = P extends `${infer First}.${infer Rest}` ? First : P
```

---

## 模板字面量与对象

**换行写法：从对象生成配置类型**
`interface <接口> { <属性>: <类型> }`
`type <类型> = \`--\${<接口>["<属性>"]}\``

```typescript
// 从对象生成配置类型
interface Config {
    host: string
    port: number
}

type ConfigKey = `--${keyof Config}`
```

---

**基本写法：使用对象模板字面量**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用对象模板字面量
let key: ConfigKey = "--host"
```

---

## 模板字面量与枚举

**换行写法：从枚举生成字符串**
`enum <枚举> { <成员1>, <成员2> }`
`type <类型> = \`\${<枚举>}\``

```typescript
// 从枚举生成字符串类型
enum Status {
    Active = "ACTIVE",
    Inactive = "INACTIVE",
}

type StatusString = `${Status}`
```

---

**基本写法：使用枚举模板字面量**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用枚举模板字面量
let status: StatusString = "ACTIVE"
```

---

## 模板字面量与工具类型

**换行写法：实现 Join 工具类型**
`type <类型> = <T extends string[], <分隔符> extends string> =`
`    <T> extends [infer <First>, ...infer <Rest>]`
`    ? <Rest> extends [] ? <First> : \`\${<First>}\${<分隔符>}\${<类型><<Rest>, <分隔符>>}\``
`    : never`

```typescript
// 实现 Join 工具类型
type Join<T extends string[], D extends string> =
    T extends [infer First, ...infer Rest]
    ? Rest extends [] ? First : `${First & string}${D}${Join<Rest, D>}`
    : never
```

---

**换行写法：实现 Split 工具类型**
`type <类型> = <S extends string, <分隔符> extends string> =`
`    <S> extends \`${infer <First>}\${<分隔符>}\${infer <Rest>}\``
`    ? [<First>, ...<类型><<Rest>, <分隔符>>]`
`    : [<S>]`

```typescript
// 实现 Split 工具类型
type Split<S extends string, D extends string> =
    S extends `${infer First}${D}${infer Rest}`
    ? [First, ...Split<Rest, D>]
    : [S]
```

---

## 模板字面量与路径

**换行写法：生成属性路径**
`type <类型><<T>> = <T> extends object`
`    ? { [P in keyof T & string]: \`\${P}.\${<类型><T[P]>>}\` }[keyof T]`
`    : never`

```typescript
// 生成嵌套属性路径
type Path<T> = T extends object
    ? { [P in keyof T & string]: `${P}.${Path<T[P]>}` }[keyof T]
    : never
```

---

**换行写法：生成简单属性路径**
`type <类型><<T>> = <T> extends object`
`    ? { [P in keyof T & string]: P }[keyof T]`
`    : never`

```typescript
// 生成简单属性路径
type SimplePath<T> = T extends object
    ? { [P in keyof T & string]: P }[keyof T]
    : never
```

---

## 模板字面量与 CSS

**换行写法：生成 CSS 属性名**
`type <类型> = \`\${<属性>}-\${<值>}\``

```typescript
// 生成 CSS 属性名
type Property = "margin" | "padding"
type Side = "top" | "bottom" | "left" | "right"
type CSSProperty = `${Property}-${Side}`
```

---

**基本写法：使用 CSS 模板字面量**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用 CSS 模板字面量
let css: CSSProperty = "margin-top"
```

---

## 模板字面量与 API

**换行写法：生成 API 路径**
`type <类型> = \`/api/\${<路径>}\``

```typescript
// 生成 API 路径
type Endpoint = "users" | "posts" | "comments"
type APIPath = `/api/${Endpoint}`
```

---

**基本写法：使用 API 模板字面量**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用 API 模板字面量
let path: APIPath = "/api/users"
```



<!-- ============ 文档分隔线：009-typescript/009-IndexSignatureDynamicProperty.md ============ -->

# 索引签名与动态属性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 字符串索引签名

**换行写法：定义字符串索引签名**
`interface <接口名> {`
`    [key: string]: <类型>`
`}`

```typescript
// 字符串索引签名
interface StringArray {
    [index: string]: string
}
```

---

**基本写法：使用字符串索引签名**
`let <变量>: <接口名> = { <键>: <值> }`

```typescript
// 使用字符串索引签名
let colors: StringArray = {
    red: "#FF0000",
    green: "#00FF00",
}
```

---

**基本写法：通过索引访问**
`<对象>[<键>]`

```typescript
// 通过字符串索引访问
let color: string = colors["red"]
```

---

## 数字索引签名

**换行写法：定义数字索引签名**
`interface <接口名> {`
`    [index: number]: <类型>`
`}`

```typescript
// 数字索引签名
interface NumberArray {
    [index: number]: string
}
```

---

**基本写法：使用数字索引签名**
`let <变量>: <接口名> = [<值>]`

```typescript
// 使用数字索引签名
let names: NumberArray = ["Alice", "Bob", "Charlie"]
```

---

**基本写法：通过数字索引访问**
`<对象>[<索引>]`

```typescript
// 通过数字索引访问
let name: string = names[0]
```

---

## 混合索引签名

**换行写法：混合字符串和数字索引签名**
`interface <接口名> {`
`    [key: string]: <类型>`
`    [key: number]: <类型>`
`}`

```typescript
// 混合字符串和数字索引签名
interface MixedArray {
    [index: string]: string
    [index: number]: string
}
```

---

**基本写法：使用混合索引签名**
`let <变量>: <接口名> = [<值>]`

```typescript
// 使用混合索引签名
let mixed: MixedArray = ["Alice", "Bob"]
```

---

## 索引签名与已知属性

**换行写法：索引签名与已知属性共存**
`interface <接口名> {`
`    <属性>: <类型>`
`    [key: string]: <类型>`
`}`

```typescript
// 索引签名与已知属性共存（已知属性类型必须兼容索引签名类型）
interface User {
    name: string
    age: number
    [key: string]: string | number
}
```

---

**基本写法：使用带已知属性的索引签名**
`let <变量>: <接口名> = { <属性>: <值>, <动态键>: <值> }`

```typescript
// 使用带已知属性的索引签名
let user: User = {
    name: "Alice",
    age: 30,
    email: "alice@example.com",
}
```

---

## 索引签名与 readonly

**换行写法：只读索引签名**
`interface <接口名> {`
`    readonly [key: string]: <类型>`
`}`

```typescript
// 只读索引签名
interface ReadonlyConfig {
    readonly [key: string]: string
}
```

---

**基本写法：使用只读索引签名**
`let <变量>: <接口名> = { <键>: <值> }`

```typescript
// 使用只读索引签名
let config: ReadonlyConfig = {
    host: "localhost",
    port: "8080",
}
```

---

## Record 工具类型

**基本写法：使用 Record 创建索引类型**
`type <类型> = Record<<键类型>, <值类型>>`

```typescript
// 使用 Record 创建索引类型
type ColorMap = Record<string, string>
```

---

**基本写法：使用 Record 类型**
`let <变量>: <类型> = { <键>: <值> }`

```typescript
// 使用 Record 类型
let colors: ColorMap = {
    red: "#FF0000",
    green: "#00FF00",
}
```

---

**换行写法：Record 与字面量键类型**
`type <类型> = Record<<"<键1>" | "<键2>", <值类型>>`

```typescript
// Record 与字面量键类型
type UserProperties = Record<"name" | "age", string>
```

---

**基本写法：使用字面量键 Record**
`let <变量>: <类型> = { <键>: <值> }`

```typescript
// 使用字面量键 Record
let props: UserProperties = {
    name: "Alice",
    age: "30",
}
```

---

## 动态属性访问

**基本写法：使用方括号访问动态属性**
`<对象>[<变量>]`

```typescript
// 使用方括号访问动态属性
let key: string = "name"
let user: Record<string, any> = { name: "Alice" }
let value: any = user[key]
```

---

**基本写法：使用变量作为键**
`let <变量> = <对象>[<键变量>]`

```typescript
// 使用变量作为键访问属性
let property: string = "age"
let user: Record<string, number> = { age: 30 }
let age: number = user[property]
```

---

## 索引签名与类型推断

**换行写法：索引签名类型推断**
`function <函数>(<参数>: <接口>): <返回类型> {`
`    return <参数>[<键>]`
`}`

```typescript
// 索引签名类型推断
function get_property(obj: Record<string, number>, key: string): number {
    return obj[key]
}
```

---

**基本写法：使用索引签名函数**
`let <变量> = <函数>(<对象>, "<键>")`

```typescript
// 使用索引签名函数
let user: Record<string, number> = { age: 30, score: 95 }
let age: number = get_property(user, "age")
```

---

## 索引签名与映射类型

**换行写法：索引签名与映射类型**
`type <类型><<T>> = {`
`    [P in keyof T]: <类型>`
`}`

```typescript
// 索引签名与映射类型
type Stringify<T> = {
    [P in keyof T]: string
}
```

---

**基本写法：使用映射类型**
`type <别名> = <类型><<接口>>`

```typescript
// 使用映射类型
interface User {
    name: string
    age: number
}

type StringUser = Stringify<User>
```

---

## 索引签名与 Partial

**基本写法：使用 Partial 使索引签名可选**
`type <别名> = Partial<<接口>>`

```typescript
// 使用 Partial 使索引签名可选
interface Config {
    host: string
    port: number
}

type PartialConfig = Partial<Config>
```

---

**基本写法：使用 Partial 索引签名**
`let <变量>: <别名> = { <属性>: <值> }`

```typescript
// 使用 Partial 索引签名
let config: PartialConfig = {
    host: "localhost",
}
```

---

## 索引签名与 Pick

**基本写法：使用 Pick 选取部分属性**
`type <别名> = Pick<<接口>, "<属性1>" | "<属性2>">`

```typescript
// 使用 Pick 选取部分属性
interface User {
    name: string
    age: number
    email: string
}

type UserBasic = Pick<User, "name" | "age">
```

---

**基本写法：使用 Pick 类型**
`let <变量>: <别名> = { <属性>: <值> }`

```typescript
// 使用 Pick 类型
let user: UserBasic = {
    name: "Alice",
    age: 30,
}
```

---

## 索引签名与 Omit

**基本写法：使用 Omit 排除属性**
`type <别名> = Omit<<接口>, "<属性>">`

```typescript
// 使用 Omit 排除属性
type UserWithoutAge = Omit<User, "age">
```

---

**基本写法：使用 Omit 类型**
`let <变量>: <别名> = { <属性>: <值> }`

```typescript
// 使用 Omit 类型
let user: UserWithoutAge = {
    name: "Alice",
    email: "alice@example.com",
}
```

---

## 索引签名与 keyof

**基本写法：使用 keyof 获取键类型**
`type <类型> = keyof <接口>`

```typescript
// 使用 keyof 获取键类型
interface User {
    name: string
    age: number
}

type UserKey = keyof User  // "name" | "age"
```

---

**基本写法：使用 keyof 约束**
`function <函数><<K> extends keyof <接口>>(<参数>: <接口>, <键>: <K>): <返回类型> { <语句> }`

```typescript
// 使用 keyof 约束函数参数
function get_property<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key]
}
```

---

**基本写法：使用 keyof 约束函数**
`let <变量> = <函数>(<对象>, "<属性>")`

```typescript
// 使用 keyof 约束函数
let user: User = { name: "Alice", age: 30 }
let name: string = get_property(user, "name")
```

---

## 索引签名与 in 操作符

**基本写法：使用 in 检查属性存在**
`if ("<属性>" in <对象>) { <语句> }`

```typescript
// 使用 in 检查属性是否存在
let user: Record<string, any> = { name: "Alice" }
if ("name" in user) {
    console.log(user.name)
}
```

---

**基本写法：使用 in 检查动态属性**
`if (<键变量> in <对象>) { <语句> }`

```typescript
// 使用 in 检查动态属性
let key: string = "age"
let user: Record<string, any> = { name: "Alice" }
if (key in user) {
    console.log(user[key])
}
```

---

## 索引签名与 delete

**基本写法：使用 delete 删除属性**
`delete <对象>[<键>]`

```typescript
// 使用 delete 删除属性
let user: Record<string, any> = { name: "Alice", age: 30 }
delete user["age"]
```

---

**基本写法：使用 delete 删除动态属性**
`delete <对象>[<键变量>]`

```typescript
// 使用 delete 删除动态属性
let key: string = "email"
let user: Record<string, any> = { name: "Alice", email: "alice@example.com" }
delete user[key]
```

---

## 索引签名与遍历

**换行写法：遍历索引签名对象**
`for (const <键> in <对象>) { <语句> }`

```typescript
// 遍历索引签名对象
let user: Record<string, string> = { name: "Alice", email: "alice@example.com" }
for (const key in user) {
    console.log(`${key}: ${user[key]}`)
}
```

---

**换行写法：使用 Object.keys 遍历**
`for (const <键> of Object.keys(<对象>)) { <语句> }`

```typescript
// 使用 Object.keys 遍历
let user: Record<string, string> = { name: "Alice", email: "alice@example.com" }
for (const key of Object.keys(user)) {
    console.log(`${key}: ${user[key]}`)
}
```

---

**换行写法：使用 Object.entries 遍历**
`for (const [<键>, <值>] of Object.entries(<对象>)) { <语句> }`

```typescript
// 使用 Object.entries 遍历
let user: Record<string, string> = { name: "Alice", email: "alice@example.com" }
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`)
}
```

---

## 索引签名与 Object 方法

**基本写法：使用 Object.keys 获取键**
`Object.keys(<对象>)`

```typescript
// 使用 Object.keys 获取所有键
let user: Record<string, string> = { name: "Alice", email: "alice@example.com" }
let keys: string[] = Object.keys(user)
```

---

**基本写法：使用 Object.values 获取值**
`Object.values(<对象>)`

```typescript
// 使用 Object.values 获取所有值
let user: Record<string, string> = { name: "Alice", email: "alice@example.com" }
let values: string[] = Object.values(user)
```

---

**基本写法：使用 Object.entries 获取键值对**
`Object.entries(<对象>)`

```typescript
// 使用 Object.entries 获取所有键值对
let user: Record<string, string> = { name: "Alice", email: "alice@example.com" }
let entries: [string, string][] = Object.entries(user)
```

---

## 索引签名与扩展运算符

**基本写法：使用扩展运算符合并对象**
`{ ...<对象1>, ...<对象2> }`

```typescript
// 使用扩展运算符合并对象
let defaults: Record<string, any> = { host: "localhost", port: 8080 }
let overrides: Record<string, any> = { port: 3000 }
let config = { ...defaults, ...overrides }
```

---

**基本写法：使用扩展运算符复制对象**
`let <变量> = { ...<对象> }`

```typescript
// 使用扩展运算符复制对象
let original: Record<string, any> = { name: "Alice", age: 30 }
let copy = { ...original }
```

---

## 索引签名与可选属性

**换行写法：索引签名与可选属性**
`interface <接口名> {`
`    <属性>?: <类型>`
`    [key: string]: <类型> | undefined`
`}`

```typescript
// 索引签名与可选属性
interface Config {
    host?: string
    port?: number
    [key: string]: string | number | undefined
}
```

---

**基本写法：使用可选属性索引签名**
`let <变量>: <接口名> = { <属性>: <值> }`

```typescript
// 使用可选属性索引签名
let config: Config = {
    host: "localhost",
    custom_setting: "value",
}
```

---

## 索引签名与类型守卫

**换行写法：索引签名与类型守卫**
`function <函数>(<参数>: Record<string, unknown>): <参数> is Record<string, <类型>> {`
`    return <检查>`
`}`

```typescript
// 索引签名与类型守卫
function is_string_record(value: Record<string, unknown>): value is Record<string, string> {
    return Object.values(value).every(v => typeof v === "string")
}
```

---

**基本写法：使用索引签名类型守卫**
`if (<函数>(<值>)) { <语句> }`

```typescript
// 使用索引签名类型守卫
let data: Record<string, unknown> = { name: "Alice", city: "NYC" }
if (is_string_record(data)) {
    Object.values(data).forEach(v => console.log(v.toUpperCase()))
}
```

---

## 索引签名与 Map

**换行写法：使用 Map 替代索引签名**
`let <变量>: Map<<键类型>, <值类型>> = new Map()`

```typescript
// 使用 Map 替代索引签名
let user_map: Map<string, string> = new Map()
user_map.set("name", "Alice")
user_map.set("email", "alice@example.com")
```

---

**基本写法：访问 Map**
`<Map>.get(<键>)`

```typescript
// 访问 Map
let name: string | undefined = user_map.get("name")
```

---

**换行写法：遍历 Map**
`for (const [<键>, <值>] of <Map>) { <语句> }`

```typescript
// 遍历 Map
for (const [key, value] of user_map) {
    console.log(`${key}: ${value}`)
}
```

---

## 索引签名与 WeakMap

**换行写法：使用 WeakMap**
`let <变量>: WeakMap<<对象类型>, <值类型>> = new WeakMap()`

```typescript
// 使用 WeakMap（键必须是对象）
let metadata: WeakMap<object, string> = new WeakMap()
let user = { name: "Alice" }
metadata.set(user, "admin")
```

---

**基本写法：访问 WeakMap**
`<WeakMap>.get(<对象>)`

```typescript
// 访问 WeakMap
let role: string | undefined = metadata.get(user)
```

---

## 索引签名与动态键

**换行写法：使用计算属性名**
`let <变量>: <接口> = {`
`    [<表达式>]: <值>,`
`}`

```typescript
// 使用计算属性名
let key: string = "dynamic_key"
let obj: Record<string, string> = {
    [key]: "value",
}
```

---

**基本写法：使用模板字面量作为键**
`let <变量>: <接口> = { [\`prefix_\${<变量>}\`]: <值> }`

```typescript
// 使用模板字面量作为键
let prefix: string = "user"
let obj: Record<string, string> = {
    [`${prefix}_name`]: "Alice",
}
```

---

## 索引签名与 JSON

**基本写法：使用 JSON.parse 解析**
`JSON.parse(<字符串>) as <接口>`

```typescript
// 使用 JSON.parse 解析为索引签名类型
let json: string = '{"name": "Alice", "age": 30}'
let user: Record<string, any> = JSON.parse(json)
```

---

**基本写法：使用 JSON.stringify 序列化**
`JSON.stringify(<对象>)`

```typescript
// 使用 JSON.stringify 序列化索引签名对象
let user: Record<string, any> = { name: "Alice", age: 30 }
let json: string = JSON.stringify(user)
```

---

## 索引签名与 Proxy

**换行写法：使用 Proxy 拦截属性访问**
`let <变量> = new Proxy(<目标>, {`
`    get(<目标>, <键>) { return <值> }`
`    set(<目标>, <键>, <值>) { return <布尔值> }`
`})`

```typescript
// 使用 Proxy 拦截属性访问
let handler: ProxyHandler<Record<string, any>> = {
    get(target, key: string) {
        return key in target ? target[key] : "not found"
    },
    set(target, key: string, value) {
        target[key] = value
        return true
    }
}

let user: Record<string, any> = new Proxy({}, handler)
```



<!-- ============ 文档分隔线：009-typescript/010-ConditionalTypeInfer.md ============ -->

# 条件类型与infer

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本条件类型

**基本写法：基本条件类型**
`type <类型> = <T> extends <条件> ? <真类型> : <假类型>`

```typescript
// 基本条件类型
type IsString<T> = T extends string ? true : false
```

---

**基本写法：使用条件类型**
`type <别名> = <类型函数><<参数类型>>`

```typescript
// 使用条件类型
type A = IsString<string>  // true
type B = IsString<number>  // false
```

---

## 分布式条件类型

**基本写法：分布式条件类型**
`type <类型><<T>> = <T> extends <条件> ? <真类型> : <假类型>`

```typescript
// 分布式条件类型（对联合类型逐个判断）
type ToArray<T> = T extends any ? T[] : never
```

---

**基本写法：使用分布式条件类型**
`type <别名> = <类型><<联合类型>>`

```typescript
// 使用分布式条件类型
type Result = ToArray<string | number>  // string[] | number[]
```

---

**基本写法：阻止分布式条件类型**
`type <类型><<T>> = [<T>] extends [<条件>] ? <真类型> : <假类型>`

```typescript
// 阻止分布式条件类型（使用方括号包裹）
type ToArrayAll<T> = [T] extends [any] ? T[] : never
```

---

## infer 基础

**基本写法：使用 infer 推断类型**
`type <类型> = <T> extends (<参数>: infer <U>) => any ? <U> : never`

```typescript
// 使用 infer 推断函数参数类型
type GetParameter<T> = T extends (arg: infer U) => any ? U : never
```

---

**基本写法：使用 infer 推断返回类型**
`type <类型> = <T> extends (...args: any[]) => infer <R> ? <R> : never`

```typescript
// 使用 infer 推断函数返回类型
type GetReturnType<T> = T extends (...args: any[]) => infer R ? R : never
```

---

**基本写法：使用 infer 推断数组元素类型**
`type <类型> = <T> extends (infer <U>)[] ? <U> : never`

```typescript
// 使用 infer 推断数组元素类型
type GetArrayElement<T> = T extends (infer U)[] ? U : never
```

---

**基本写法：使用 infer 推断 Promise 类型**
`type <类型> = <T> extends Promise<infer <U>> ? <U> : <T>`

```typescript
// 使用 infer 推断 Promise 的类型
type UnwrapPromise<T> = T extends Promise<infer U> ? U : T
```

---

## infer 推断元组

**基本写法：推断元组第一个元素**
`type <类型> = <T> extends [infer <First>, ...any[]] ? <First> : never`

```typescript
// 推断元组第一个元素类型
type GetFirst<T extends any[]> = T extends [infer First, ...any[]] ? First : never
```

---

**基本写法：推断元组最后一个元素**
`type <类型> = <T> extends [...any[], infer <Last>] ? <Last> : never`

```typescript
// 推断元组最后一个元素类型
type GetLast<T extends any[]> = T extends [...any[], infer Last] ? Last : never
```

---

**换行写法：推断元组所有元素**
`type <类型> = <T> extends [infer <First>, ...infer <Rest>]`
`    ? [<First>, ...<类型><<Rest>>]`
`    : []`

```typescript
// 递归推断元组所有元素类型
type ToTuple<T extends any[]> = T extends [infer First, ...infer Rest]
    ? [First, ...ToTuple<Rest>]
    : []
```

---

## infer 推断对象

**基本写法：推断对象属性类型**
`type <类型> = <T> extends { <属性>: infer <U> } ? <U> : never`

```typescript
// 推断对象属性的类型
type GetPropertyType<T> = T extends { value: infer U } ? U : never
```

---

**换行写法：推断构造函数实例类型**
`type <类型> = <T> extends new (...args: any[]) => infer <Instance> ? <Instance> : never`

```typescript
// 推断构造函数的实例类型
type GetInstance<T> = T extends new (...args: any[]) => infer Instance ? Instance : never
```

---

## 条件类型组合

**换行写法：嵌套条件类型**
`type <类型> =`
`    <T> extends string ? <处理1> :`
`    <T> extends number ? <处理2> :`
`    <处理3>`

```typescript
// 嵌套条件类型
type TypeName<T> =
    T extends string ? "string" :
    T extends number ? "number" :
    T extends boolean ? "boolean" :
    "other"
```

---

**基本写法：使用嵌套条件类型**
`type <别名> = <类型函数><<参数类型>>`

```typescript
// 使用嵌套条件类型
type Name1 = TypeName<string>  // "string"
type Name2 = TypeName<number>  // "number"
```

---

## 条件类型与联合类型

**基本写法：条件类型过滤联合类型**
`type <类型> = <T> extends <条件> ? <T> : never`

```typescript
// 条件类型过滤联合类型
type ExtractString<T> = T extends string ? T : never
```

---

**基本写法：使用条件类型过滤**
`type <别名> = <类型函数><<联合类型>>`

```typescript
// 使用条件类型过滤联合类型
type Result = ExtractString<string | number | boolean>  // string
```

---

## Exclude 与 Extract

**基本写法：使用 Exclude 排除类型**
`type <别名> = Exclude<<联合类型>, <排除类型>>`

```typescript
// 使用 Exclude 排除特定类型
type T = Exclude<string | number | boolean, boolean>
```

---

**基本写法：使用 Extract 提取类型**
`type <别名> = Extract<<联合类型>, <匹配类型>>`

```typescript
// 使用 Extract 提取符合条件的类型
type T = Extract<string | number | boolean, string | number>
```

---

## NonNullable

**基本写法：使用 NonNullable 排除 null**
`type <别名> = NonNullable<<类型>>`

```typescript
// 使用 NonNullable 排除 null 和 undefined
type T = NonNullable<string | null | undefined>
```

---

## ReturnType 与 Parameters

**基本写法：使用 ReturnType 获取返回类型**
`type <别名> = ReturnType<typeof <函数>>`

```typescript
// 从函数推断返回类型
function get_user() {
    return { name: "Alice", age: 30 }
}

type User = ReturnType<typeof get_user>
```

---

**基本写法：使用 Parameters 获取参数类型**
`type <别名> = Parameters<typeof <函数>>`

```typescript
// 从函数推断参数类型
function greet(name: string, age: number): void {}

type GreetParams = Parameters<typeof greet>  // [string, number]
```

---

**基本写法：使用 ConstructorParameters 获取构造函数参数**
`type <别名> = ConstructorParameters<typeof <类>>`

```typescript
// 从类推断构造函数参数类型
class User {
    constructor(public name: string, public age: number) {}
}

type UserParams = ConstructorParameters<typeof User>
```

---

**基本写法：使用 InstanceType 获取实例类型**
`type <别名> = InstanceType<typeof <类>>`

```typescript
// 从类推断实例类型
type UserInstance = InstanceType<typeof User>
```

---

## 条件类型与映射类型

**换行写法：条件类型与映射类型组合**
`type <类型><<T>> = {`
`    [P in keyof T]: T[P] extends <条件> ? <真类型> : <假类型>`
`}`

```typescript
// 条件类型与映射类型组合
type StringifyStrings<T> = {
    [P in keyof T]: T[P] extends string ? string : never
}
```

---

## 递归条件类型

**换行写法：递归条件类型**
`type <类型> = <T> extends Promise<infer <U>> ? <类型><<U>> : <T>`

```typescript
// 递归条件类型（处理嵌套 Promise）
type DeepAwaited<T> = T extends Promise<infer U> ? DeepAwaited<U> : T
```

---

**换行写法：递归展平元组**
`type <类型> = <T> extends [infer <First>, ...infer <Rest>]`
`    ? <First> extends any[] ? [...<类型><<First>>, ...<类型><<Rest>>]`
`    : [<First>, ...<类型><<Rest>>]`
`    : []`

```typescript
// 递归展平嵌套元组
type Flatten<T extends any[]> = T extends [infer First, ...infer Rest]
    ? First extends any[] ? [...Flatten<First>, ...Flatten<Rest>]
    : [First, ...Flatten<Rest>]
    : []
```

---

## 条件类型推断函数重载

**换行写法：推断重载函数返回类型**
`type <类型> = <T> extends (...args: any[]) => infer <R> ? <R> : never`

```typescript
// 推断重载函数的返回类型（取最后一个重载）
type GetOverloadReturn<T> = T extends (...args: any[]) => infer R ? R : never
```

---

## infer 与模板字面量

**换行写法：使用 infer 推断模板字面量**
`type <类型> = <S> extends \`prefix_\${infer <T>}\` ? <T> : never`

```typescript
// 使用 infer 推断模板字面量中的类型
type RemovePrefix<S> = S extends `prefix_${infer T}` ? T : never
```

---

**换行写法：推断字符串前缀**
`type <类型> = <S> extends \`${infer <Prefix>}_suffix\` ? <Prefix> : never`

```typescript
// 推断字符串前缀
type GetPrefix<S> = S extends `${infer Prefix}_suffix` ? Prefix : never
```

---

## 条件类型实战

**换行写法：实现 DeepPartial**
`type <类型><<T>> = {`
`    [P in keyof T]?: T[P] extends object ? <类型><T[P]> : T[P]`
`}`

```typescript
// 实现深度可选类型
type DeepPartial<T> = {
    [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P]
}
```

---

**换行写法：实现 DeepReadonly**
`type <类型><<T>> = {`
`    readonly [P in keyof T]: T[P] extends object ? <类型><T[P]> : T[P]`
`}`

```typescript
// 实现深度只读类型
type DeepReadonly<T> = {
    readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P]
}
```

---

**换行写法：实现 Mutable**
`type <类型><<T>> = {`
`    -readonly [P in keyof T]: T[P]`
`}`

```typescript
// 移除只读修饰符
type Mutable<T> = {
    -readonly [P in keyof T]: T[P]
}
```

---

## 条件类型与 never

**基本写法：使用 never 过滤**
`type <类型> = <T> extends <条件> ? <T> : never`

```typescript
// 使用 never 过滤不符合条件的类型
type FilterString<T> = T extends string ? T : never
```

---

**基本写法：使用 never 过滤联合类型**
`type <别名> = <类型函数><<联合类型>>`

```typescript
// 使用 never 过滤联合类型
type Result = FilterString<string | number | boolean>  // string
```

---

## 条件类型与函数推断

**换行写法：推断异步函数返回类型**
`type <类型> = <T> extends (...args: any[]) => Promise<infer <R>> ? <R> : never`

```typescript
// 推断异步函数的返回类型
type AsyncReturnType<T> = T extends (...args: any[]) => Promise<infer R> ? R : never
```

---

**换行写法：推断函数第一个参数类型**
`type <类型> = <T> extends (<参数>: infer <P>, ...args: any[]) => any ? <P> : never`

```typescript
// 推断函数第一个参数类型
type FirstParameter<T> = T extends (first: infer P, ...args: any[]) => any ? P : never
```



<!-- ============ 文档分隔线：009-typescript/011-MappedTypeKeyRemap.md ============ -->

# 映射类型与键重映射

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本映射类型

**换行写法：基本映射类型**
`type <类型><<T>> = {`
`    [P in keyof T]: T[P]`
`}`

```typescript
// 基本映射类型（复制类型）
type Copy<T> = {
    [P in keyof T]: T[P]
}
```

---

**换行写法：使用映射类型**
`type <别名> = <类型><<接口>>`

```typescript
// 使用映射类型
interface User {
    name: string
    age: number
}

type UserCopy = Copy<User>
```

---

## 修改属性类型

**换行写法：映射类型修改属性类型**
`type <类型><<T>> = {`
`    [P in keyof T]: <新类型>`
`}`

```typescript
// 映射类型将所有属性改为 string
type Stringify<T> = {
    [P in keyof T]: string
}
```

---

**换行写法：映射类型将属性改为可选**
`type <类型><<T>> = {`
`    [P in keyof T]?: T[P]`
`}`

```typescript
// 映射类型将所有属性改为可选
type MyPartial<T> = {
    [P in keyof T]?: T[P]
}
```

---

**换行写法：映射类型将属性改为只读**
`type <类型><<T>> = {`
`    readonly [P in keyof T]: T[P]`
`}`

```typescript
// 映射类型将所有属性改为只读
type MyReadonly<T> = {
    readonly [P in keyof T]: T[P]
}
```

---

## 移除修饰符

**换行写法：移除只读修饰符**
`type <类型><<T>> = {`
`    -readonly [P in keyof T]: T[P]`
`}`

```typescript
// 移除只读修饰符
type Mutable<T> = {
    -readonly [P in keyof T]: T[P]
}
```

---

**换行写法：移除可选修饰符**
`type <类型><<T>> = {`
`    [P in keyof T]-?: T[P]`
`}`

```typescript
// 移除可选修饰符
type Required<T> = {
    [P in keyof T]-?: T[P]
}
```

---

## 键重映射 as

**换行写法：使用 as 重映射键**
`type <类型><<T>> = {`
`    [P in keyof T as <新键>]: T[P]`
`}`

```typescript
// 使用 as 重映射键（将键转为大写）
type GetKeys<T> = {
    [P in keyof T as Uppercase<string & P>]: T[P]
}
```

---

**换行写法：使用 as 添加前缀**
`type <类型><<T>> = {`
`    [P in keyof T as \`get_\${P & string}\`]: T[P]`
`}`

```typescript
// 使用 as 为键添加前缀
type Getters<T> = {
    [P in keyof T as `get_${P & string}`]: () => T[P]
}
```

---

**换行写法：使用 as 过滤键**
`type <类型><<T>> = {`
`    [P in keyof T as <条件> extends <真> ? <P> : never]: T[P]`
`}`

```typescript
// 使用 as 过滤键（只保留 string 类型的键）
type StringKeys<T> = {
    [P in keyof T as P extends string ? P : never]: T[P]
}
```

---

## 映射类型与条件类型

**换行写法：映射类型与条件类型组合**
`type <类型><<T>> = {`
`    [P in keyof T]: T[P] extends <条件> ? <真类型> : <假类型>`
`}`

```typescript
// 映射类型与条件类型组合
type StringifyStrings<T> = {
    [P in keyof T]: T[P] extends string ? string : never
}
```

---

## 内置工具类型

**基本写法：使用 Partial 工具类型**
`type <别名> = Partial<<接口>>`

```typescript
// 使用 Partial 使所有属性可选
type PartialUser = Partial<User>
```

---

**基本写法：使用 Required 工具类型**
`type <别名> = Required<<接口>>`

```typescript
// 使用 Required 使所有属性必填
type RequiredUser = Required<User>
```

---

**基本写法：使用 Readonly 工具类型**
`type <别名> = Readonly<<接口>>`

```typescript
// 使用 Readonly 使所有属性只读
type ReadonlyUser = Readonly<User>
```

---

**基本写法：使用 Pick 工具类型**
`type <别名> = Pick<<接口>, "<属性1>" | "<属性2>">`

```typescript
// 使用 Pick 选取部分属性
type UserBasic = Pick<User, "name" | "age">
```

---

**基本写法：使用 Omit 工具类型**
`type <别名> = Omit<<接口>, "<属性>">`

```typescript
// 使用 Omit 排除部分属性
type UserWithoutAge = Omit<User, "age">
```

---

**基本写法：使用 Record 工具类型**
`type <别名> = Record<<键类型>, <值类型>>`

```typescript
// 使用 Record 创建键值对类型
type UserMap = Record<string, User>
```

---

## 自定义映射类型

**换行写法：实现 DeepPartial**
`type <类型><<T>> = {`
`    [P in keyof T]?: T[P] extends object ? <类型><T[P]> : T[P]`
`}`

```typescript
// 实现深度可选类型
type DeepPartial<T> = {
    [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P]
}
```

---

**换行写法：实现 DeepReadonly**
`type <类型><<T>> = {`
`    readonly [P in keyof T]: T[P] extends object ? <类型><T[P]> : T[P]`
`}`

```typescript
// 实现深度只读类型
type DeepReadonly<T> = {
    readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P]
}
```

---

**换行写法：实现 Mutable**
`type <类型><<T>> = {`
`    -readonly [P in keyof T]: T[P]`
`}`

```typescript
// 移除只读修饰符
type Mutable<T> = {
    -readonly [P in keyof T]: T[P]
}
```

---

**换行写法：实现 Getters**
`type <类型><<T>> = {`
`    [P in keyof T as \`get_\${P & string}\`]: () => T[P]`
`}`

```typescript
// 为所有属性生成 getter 方法
type Getters<T> = {
    [P in keyof T as `get_${P & string}`]: () => T[P]
}
```

---

**换行写法：实现 Setters**
`type <类型><<T>> = {`
`    [P in keyof T as \`set_\${P & string}\`]: (<值>: T[P]) => void`
`}`

```typescript
// 为所有属性生成 setter 方法
type Setters<T> = {
    [P in keyof T as `set_${P & string}`]: (value: T[P]) => void
}
```

---

## 映射类型与联合类型

**换行写法：从联合类型创建映射类型**
`type <类型> = {`
`    [P in <联合类型>]: <类型>`
`}`

```typescript
// 从联合类型创建映射类型
type Events = "click" | "hover" | "focus"

type EventHandlers = {
    [P in Events]: (event: string) => void
}
```

---

**换行写法：从枚举创建映射类型**
`type <类型> = {`
`    [P in <枚举>]: <类型>`
`}`

```typescript
// 从枚举创建映射类型
enum Status {
    Idle = "IDLE",
    Loading = "LOADING",
}

type StatusMessages = {
    [P in Status]: string
}
```

---

## 键重映射实战

**换行写法：将键转为大写**
`type <类型><<T>> = {`
`    [P in keyof T as Uppercase<P & string>]: T[P]`
`}`

```typescript
// 将所有键转为大写
type UppercaseKeys<T> = {
    [P in keyof T as Uppercase<P & string>]: T[P]
}
```

---

**换行写法：将键转为小写**
`type <类型><<T>> = {`
`    [P in keyof T as Lowercase<P & string>]: T[P]`
`}`

```typescript
// 将所有键转为小写
type LowercaseKeys<T> = {
    [P in keyof T as Lowercase<P & string>]: T[P]
}
```

---

**换行写法：过滤特定类型的键**
`type <类型><<T>> = {`
`    [P in keyof T as T[P] extends <条件> ? <P> : never]: T[P]`
`}`

```typescript
// 只保留 string 类型的属性
type StringProperties<T> = {
    [P in keyof T as T[P] extends string ? P : never]: T[P]
}
```

---

**换行写法：过滤函数类型的键**
`type <类型><<T>> = {`
`    [P in keyof T as T[P] extends Function ? <P> : never]: T[P]`
`}`

```typescript
// 只保留函数类型的属性
type Methods<T> = {
    [P in keyof T as T[P] extends Function ? P : never]: T[P]
}
```

---

## 映射类型与模板字面量

**换行写法：使用模板字面量重映射键**
`type <类型><<T>> = {`
`    [P in keyof T as \`on\${Capitalize<P & string>}\`]: T[P]`
`}`

```typescript
// 使用模板字面量为键添加 on 前缀
type EventHandlers<T> = {
    [P in keyof T as `on${Capitalize<P & string>}`]: (value: T[P]) => void
}
```

---

## 同态映射类型

**换行写法：同态映射类型**
`type <类型><<T>> = {`
`    [P in keyof T]: T[P]`
`}`

```typescript
// 同态映射类型（保留修饰符）
type Homomorphic<T> = {
    [P in keyof T]: T[P]
}
```

---

## 非同态映射类型

**换行写法：非同态映射类型**
`type <类型> = {`
`    [P in <联合类型>]: <类型>`
`}`

```typescript
// 非同态映射类型（不保留修饰符）
type NonHomomorphic = {
    [P in "a" | "b" | "c"]: string
}
```

---

## 映射类型与 keyof

**换行写法：使用 keyof 过滤键**
`type <类型><<T>, <K>> = {`
`    [P in keyof T as P extends <K> ? <P> : never]: T[P]`
`}`

```typescript
// 使用 keyof 过滤键
type PickByType<T, U> = {
    [P in keyof T as T[P] extends U ? P : never]: T[P]
}
```

---

**换行写法：使用 PickByType**
`type <别名> = <类型><<接口>, <类型>>`

```typescript
// 使用 PickByType 过滤特定类型的属性
interface User {
    name: string
    age: number
    email: string
}

type StringProps = PickByType<User, string>  // { name: string, email: string }
```

---

## 映射类型与 never

**换行写法：使用 never 过滤属性**
`type <类型><<T>> = {`
`    [P in keyof T as <条件> ? <P> : never]: T[P]`
`}`

```typescript
// 使用 never 过滤属性
type RemoveMethods<T> = {
    [P in keyof T as T[P] extends Function ? never : P]: T[P]
}
```

---

## 映射类型与递归

**换行写法：递归映射类型**
`type <类型><<T>> = {`
`    [P in keyof T]: T[P] extends object ? <类型><T[P]> : T[P]`
`}`

```typescript
// 递归映射类型
type DeepCopy<T> = {
    [P in keyof T]: T[P] extends object ? DeepCopy<T[P]> : T[P]
}
```

---

## 映射类型与可选链

**换行写法：处理可选属性**
`type <类型><<T>> = {`
`    [P in keyof T]-?: T[P]`
`}`

```typescript
// 移除可选修饰符
type NonNullable<T> = {
    [P in keyof T]-?: T[P]
}
```

---

## 映射类型与联合类型键

**换行写法：从联合类型创建对象**
`type <类型> = {`
`    [P in <联合类型>]: <类型>`
`}`

```typescript
// 从联合类型创建对象类型
type Direction = "up" | "down" | "left" | "right"

type DirectionValues = {
    [P in Direction]: number
}
```

---

**换行写法：从字面量联合类型创建映射**
`type <类型> = {`
`    [P in "<值1>" | "<值2>"]: <类型>`
`}`

```typescript
// 从字面量联合类型创建映射类型
type Config = {
    [P in "host" | "port" | "timeout"]: string
}
```



<!-- ============ 文档分隔线：009-typescript/012-LocalTypeInference.md ============ -->

# 字面量类型与联合类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 字符串字面量类型

**基本写法：定义字符串字面量类型**
`let <变量>: "<值>" = "<值>"`

```typescript
// 字符串字面量类型
let direction: "left" = "left"
```

---

**换行写法：联合字符串字面量类型**
`type <类型> = "<值1>" | "<值2>" | "<值3>"`

```typescript
// 联合字符串字面量类型
type Direction = "left" | "right" | "up" | "down"
```

---

**基本写法：使用字符串字面量类型**
`let <变量>: <类型> = "<值>"`

```typescript
// 使用字符串字面量类型
let move: Direction = "left"
```

---

## 数字字面量类型

**基本写法：定义数字字面量类型**
`let <变量>: <数字> = <数字>`

```typescript
// 数字字面量类型
let dice: 6 = 6
```

---

**换行写法：联合数字字面量类型**
`type <类型> = <数字1> | <数字2> | <数字3>`

```typescript
// 联合数字字面量类型
type DiceValue = 1 | 2 | 3 | 4 | 5 | 6
```

---

## 布尔字面量类型

**基本写法：定义布尔字面量类型**
`let <变量>: true = true`

```typescript
// 布尔字面量类型
let is_true: true = true
```

---

## 联合类型

**基本写法：基本联合类型**
`let <变量>: <类型1> | <类型2> = <值>`

```typescript
// 基本联合类型
let id: string | number = 123
id = "ABC"
```

---

**换行写法：多类型联合**
`type <类型> =`
`    | <类型1>`
`    | <类型2>`
`    | <类型3>`

```typescript
// 多类型联合（换行书写）
type Result =
    | string
    | number
    | boolean
```

---

**基本写法：联合类型与 null**
`let <变量>: <类型> | null = <值>`

```typescript
// 联合类型与 null
let name: string | null = "Alice"
name = null
```

---

**基本写法：联合类型与 undefined**
`let <变量>: <类型> | undefined = <值>`

```typescript
// 联合类型与 undefined
let value: string | undefined = undefined
```

---

## 可辨识联合

**换行写法：可辨识联合类型**
`type <类型> =`
`    | { kind: "<标识1>", <属性1>: <类型1> }`
`    | { kind: "<标识2>", <属性2>: <类型2> }`

```typescript
// 可辨识联合类型
type Shape =
    | { kind: "circle", radius: number }
    | { kind: "square", size: number }
    | { kind: "rectangle", width: number, height: number }
```

---

**换行写法：使用可辨识联合**
`function <函数>(<参数>: <类型>): <返回类型> {`
`    switch (<参数>.kind) {`
`        case "<标识1>": return <处理1>`
`        case "<标识2>": return <处理2>`
`    }`
`}`

```typescript
// 使用可辨识联合（通过 kind 属性区分）
function area(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2
        case "square":
            return shape.size ** 2
        case "rectangle":
            return shape.width * shape.height
    }
}
```

---

## 接口可辨识联合

**换行写法：接口形式可辨识联合**
`interface <接口1> { kind: "<标识1>", <属性>: <类型> }`
`interface <接口2> { kind: "<标识2>", <属性>: <类型> }`
`type <类型> = <接口1> | <接口2>`

```typescript
// 接口形式可辨识联合
interface Circle {
    kind: "circle"
    radius: number
}

interface Square {
    kind: "square"
    size: number
}

type Shape = Circle | Square
```

---

## 类型收窄

**基本写法：使用 typeof 收窄**
`if (typeof <变量> === "<类型>") { <语句> }`

```typescript
// 使用 typeof 类型收窄
function process(value: string | number): void {
    if (typeof value === "string") {
        console.log(value.toUpperCase())
    } else {
        console.log(value.toFixed(2))
    }
}
```

---

**基本写法：使用 instanceof 收窄**
`if (<变量> instanceof <类>) { <语句> }`

```typescript
// 使用 instanceof 类型收窄
class Dog {
    bark(): void {}
}

class Cat {
    meow(): void {}
}

function speak(animal: Dog | Cat): void {
    if (animal instanceof Dog) {
        animal.bark()
    } else {
        animal.meow()
    }
}
```

---

**基本写法：使用 in 收窄**
`if ("<属性>" in <对象>) { <语句> }`

```typescript
// 使用 in 操作符类型收窄
function process(obj: { a: string } | { b: number }): void {
    if ("a" in obj) {
        console.log(obj.a)
    } else {
        console.log(obj.b)
    }
}
```

---

**基本写法：使用可辨识属性收窄**
`if (<变量>.kind === "<标识>") { <语句> }`

```typescript
// 使用可辨识属性类型收窄
function area(shape: Shape): number {
    if (shape.kind === "circle") {
        return Math.PI * shape.radius ** 2
    } else {
        return shape.size ** 2
    }
}
```

---

## 联合类型函数

**基本写法：联合类型作为函数参数**
`function <函数>(<参数>: <类型1> | <类型2>): <返回类型> { <语句> }`

```typescript
// 联合类型作为函数参数
function format(value: string | number): string {
    return String(value)
}
```

---

**基本写法：联合类型作为返回值**
`function <函数>(<参数>): <类型1> | <类型2> { <语句> }`

```typescript
// 联合类型作为返回值
function get_id(): string | number {
    return Math.random() > 0.5 ? "ABC" : 123
}
```

---

## 联合类型数组

**基本写法：联合类型数组**
`let <变量>: (<类型1> | <类型2>)[] = [<值>]`

```typescript
// 联合类型数组
let mixed: (string | number)[] = [1, "two", 3, "four"]
```

---

## null 与 undefined 处理

**基本写法：检查 null**
`if (<变量> !== null) { <语句> }`

```typescript
// 检查 null 后安全使用
function process(name: string | null): void {
    if (name !== null) {
        console.log(name.toUpperCase())
    }
}
```

---

**基本写法：检查 undefined**
`if (<变量> !== undefined) { <语句> }`

```typescript
// 检查 undefined 后安全使用
function process(value: string | undefined): void {
    if (value !== undefined) {
        console.log(value.toUpperCase())
    }
}
```

---

**基本写法：同时检查 null 和 undefined**
`if (<变量> != null) { <语句> }`

```typescript
// 同时检查 null 和 undefined
function process(value: string | null | undefined): void {
    if (value != null) {
        console.log(value.toUpperCase())
    }
}
```

---

## 空值合并运算符

**基本写法：使用空值合并提供默认值**
`<值> ?? <默认值>`

```typescript
// 使用空值合并提供默认值
let name: string | null = null
let display_name: string = name ?? "Anonymous"
```

---

## 可选链与联合类型

**基本写法：可选链处理 null/undefined**
`<对象>?.<属性>`

```typescript
// 可选链处理可能为 null/undefined 的属性
interface User {
    profile?: {
        name: string
    }
}

let user: User = {}
let name: string | undefined = user?.profile?.name
```

---

## 字面量类型推断

**基本写法：const 推断字面量类型**
`const <变量> = <值>`

```typescript
// const 推断为字面量类型
const direction = "left"  // 类型为 "left"
```

---

**基本写法：let 推断宽泛类型**
`let <变量> = <值>`

```typescript
// let 推断为宽泛类型
let direction = "left"  // 类型为 string
```

---

## as const 断言

**基本写法：使用 as const 断言**
`const <变量> = <值> as const`

```typescript
// 使用 as const 断言为字面量类型
const direction = "left" as const  // 类型为 "left"
```

---

**换行写法：对象 as const**
`const <变量> = {`
`    <属性1>: <值1>,`
`    <属性2>: <值2>,`
`} as const`

```typescript
// 对象使用 as const 斿言为只读字面量类型
const config = {
    host: "localhost",
    port: 8080,
} as const
```

---

**基本写法：数组 as const**
`const <变量> = [<值1>, <值2>] as const`

```typescript
// 数组使用 as const 断言为只读元组
const colors = ["red", "green", "blue"] as const
```

---

## 模板字面量类型

**基本写法：基本模板字面量类型**
`type <类型> = \`<前缀>\${<类型>}\``

```typescript
// 基本模板字面量类型
type Greeting = `hello ${string}`
```

---

**换行写法：联合类型模板字面量**
`type <类型> = \`<前缀>\${<类型1> | <类型2>}\``

```typescript
// 联合类型模板字面量
type Side = "left" | "right"
type Direction = `turn ${Side}`
```

---

## 穷尽检查

**换行写法：使用 never 进行穷尽检查**
`function <函数>(<参数>: <类型>): <返回类型> {`
`    switch (<参数>.kind) {`
`        case "<标识1>": return <处理1>`
`        case "<标识2>": return <处理2>`
`        default: const _exhaustive: never = <参数> return _exhaustive`
`    }`
`}`

```typescript
// 使用 never 进行穷尽检查
function area(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2
        case "square":
            return shape.size ** 2
        default:
            const _exhaustive: never = shape
            return _exhaustive
    }
}
```

---

## 联合类型工具

**基本写法：使用 Extract 提取类型**
`type <别名> = Extract<<联合类型>, <匹配类型>>`

```typescript
// 使用 Extract 提取符合条件的类型
type T = Extract<string | number | boolean, string | number>
```

---

**基本写法：使用 Exclude 排除类型**
`type <别名> = Exclude<<联合类型>, <排除类型>>`

```typescript
// 使用 Exclude 排除特定类型
type T = Exclude<string | number | boolean, boolean>
```

---

**基本写法：使用 NonNullable 排除 null**
`type <别名> = NonNullable<<类型>>`

```typescript
// 使用 NonNullable 排除 null 和 undefined
type T = NonNullable<string | null | undefined>
```

---

## 联合类型与数组

**基本写法：映射联合类型**
`type <别名> = <类型>[keyof <类型>]`

```typescript
// 从类型提取值的联合类型
type Config = {
    host: string
    port: number
}

type ConfigValue = Config[keyof Config]  // string | number
```

---

## 字面量类型应用

**换行写法：使用字面量类型定义事件**
`type <事件类型> = "click" | "hover" | "focus"`
`function <函数>(<事件>: <事件类型>): void { <语句> }`

```typescript
// 使用字面量类型定义事件处理器
type EventName = "click" | "hover" | "focus"

function handle_event(event: EventName): void {
    console.log(`处理事件: ${event}`)
}
```

---

**换行写法：使用字面量类型定义状态**
`type <状态类型> = "idle" | "loading" | "success" | "error"`

```typescript
// 使用字面量类型定义状态机
type Status = "idle" | "loading" | "success" | "error"

function get_status_message(status: Status): string {
    switch (status) {
        case "idle":
            return "等待中"
        case "loading":
            return "加载中"
        case "success":
            return "成功"
        case "error":
            return "错误"
    }
}
```



<!-- ============ 文档分隔线：009-typescript/013-ConditionalTypes.md ============ -->

# TypeScript 条件类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 条件类型基础

**基本写法：条件类型语法**
`type <类型> = <T> extends <条件> ? <真类型> : <假类型>`
```typescript
// 根据条件选择类型
type IsString<T> = T extends string ? true : false
```

---

**基本写法：使用条件类型**
`type <别名> = <类型函数><<参数>>`
```typescript
// 通过条件类型得到结果
type A = IsString<"hi">  // true
type B = IsString<42>     // false
```

---

**基本写法：嵌套条件类型**
`type <类型> = <T> extends <条件1> ? <T1> : <T> extends <条件2> ? <T2> : <T3>`
```typescript
// 多分支条件判断
type TypeName<T> =
    T extends string ? "string" :
    T extends number ? "number" :
    T extends boolean ? "boolean" :
    "other"
```

---

## 分布式条件类型

**基本写法：分布式条件类型**
`type <类型><<T>> = <T> extends <条件> ? <真> : <假>`
```typescript
// 联合类型会分发判断
type ToArray<T> = T extends any ? T[] : never
type R = ToArray<string | number>  // string[] | number[]
```

---

**基本写法：阻止分布式**
`type <类型><<T>> = [<T>] extends [<条件>] ? <真> : <假>`
```typescript
// 使用方括号包裹阻止分发
type ToArrayAll<T> = [T] extends [any] ? T[] : never
type R = ToArrayAll<string | number>  // (string | number)[]
```

---

**基本写法：never 在分布式中的行为**
`type <类型><<T>> = <T> extends <条件> ? <真> : <假>`
```typescript
// never 在分布式条件中返回 never
type R = ToArray<never>  // never
```

---

## infer 推断

**基本写法：推断函数参数**
`type <类型> = <T> extends (<参数>: infer <U>) => any ? <U> : never`
```typescript
// 提取函数参数类型
type GetParam<T> = T extends (arg: infer U) => any ? U : never
```

---

**基本写法：推断返回类型**
`type <类型> = <T> extends (...args: any[]) => infer <R> ? <R> : never`
```typescript
// 提取函数返回类型
type GetReturn<T> = T extends (...args: any[]) => infer R ? R : never
```

---

**基本写法：推断数组元素**
`type <类型> = <T> extends (infer <U>)[] ? <U> : never`
```typescript
// 提取数组元素类型
type ItemOf<T> = T extends (infer U)[] ? U : never
type R = ItemOf<string[]>  // string
```

---

**基本写法：推断 Promise 值**
`type <类型> = <T> extends Promise<infer <U>> ? <U> : <T>`
```typescript
// 解包 Promise 类型
type Unwrap<T> = T extends Promise<infer U> ? U : T
type R = Unwrap<Promise<number>>  // number
```

---

**基本写法：推断对象属性**
`type <类型> = <T> extends { <属性>: infer <U> } ? <U> : never`
```typescript
// 提取对象属性类型
type PropType<T> = T extends { name: infer U } ? U : never
```

---

**基本写法：多 infer 同位置**
`type <类型> = <T> extends [<U>, <U>] ? <U> : never`
```typescript
// 多个 infer 同名推断为联合
type First<T> = T extends [infer U, ...any[]] ? U : never
```

---

## infer 与元组

**基本写法：提取元组首项**
`type <类型> = <T> extends [infer <首>, ...any[]] ? <首> : never`
```typescript
// 提取元组第一个元素类型
type Head<T extends any[]> = T extends [infer H, ...any[]] ? H : never
```

---

**基本写法：提取元组尾项**
`type <类型> = <T> extends [...any[], infer <尾>] ? <尾> : never`
```typescript
// 提取元组最后一个元素类型
type Tail<T extends any[]> = T extends [...any[], infer L] ? L : never
```

---

**基本写法：推断剩余元素**
`type <类型> = <T> extends [infer <首>, ...infer <Rest>] ? <Rest> : []`
```typescript
// 提取除首元素外的剩余元组
type DropFirst<T extends any[]> = T extends [infer _, ...infer R] ? R : []
```

---

## 条件类型约束

**基本写法：带 extends 约束的 infer**
`<T> extends <类型> & { <属性>: infer <U> }`
```typescript
// 约束 infer 推断的类型
type GetProp<T, K extends string> = T extends { [P in K]: infer U } ? U : never
```

---

**基本写法：条件与映射结合**
`type <类型> = { [K in keyof <T>]: <T>[K] extends <条件> ? <真> : <假> }`
```typescript
// 映射类型中应用条件
type StringValues<T> = {
    [K in keyof T]: T[K] extends string ? T[K] : never
}
```

---

## 实用工具类型

**基本写法：Exclude**
`type <结果> = Exclude<<联合>, <排除>>`
```typescript
// 从联合类型中排除
type T = Exclude<"a" | "b" | "c", "a">  // "b" | "c"
```

---

**基本写法：Extract**
`type <结果> = Extract<<联合>, <提取>>`
```typescript
// 从联合类型中提取
type T = Extract<string | number | boolean, string | number>  // string | number
```

---

**基本写法：NonNullable**
`type <结果> = NonNullable<<T>>`
```typescript
// 排除 null 和 undefined
type T = NonNullable<string | null>  // string
```

---

**基本写法：ReturnType**
`type <结果> = ReturnType<<函数类型>>`
```typescript
// 获取函数返回类型
type R = ReturnType<() => string>  // string
```

---

**基本写法：Parameters**
`type <结果> = Parameters<<函数类型>>`
```typescript
// 获取函数参数元组类型
type P = Parameters<(a: number, b: string) => void>  // [number, string]
```

---

**基本写法：Awaited**
`type <结果> = Awaited<<Promise>>`
```typescript
// 递归解包 Promise
type R = Awaited<Promise<Promise<number>>>  // number
```

---

**基本写法：ConstructorParameters**
`type <结果> = ConstructorParameters<<构造器类型>>`
```typescript
// 获取构造函数参数
type P = ConstructorParameters<ErrorConstructor>
```

---

**基本写法：InstanceType**
`type <结果> = InstanceType<<构造器类型>>`
```typescript
// 获取构造器实例类型
type I = InstanceType<typeof Error>
```

---

## 条件类型分配

**基本写法：基于条件过滤**
`type <类型><<T>> = <T> extends <条件> ? <T> : never`
```typescript
// 过滤联合类型保留符合条件的
type OnlyStrings<T> = T extends string ? T : never
type R = OnlyStrings<"a" | 1 | "b">  // "a" | "b"
```

---

**基本写法：Diff 类型**
`type <Diff><<T>, <U>> = <T> extends <U> ? never : <T>`
```typescript
// 计算类型差异
type Diff<T, U> = T extends U ? never : T
type R = Diff<"a" | "b" | "c", "a">  // "b" | "c"
```

---

## 高级应用

**基本写法：递归条件类型**
`type <类型> = <T> extends Promise<infer <U>> ? <类型><<U>> : <T>`
```typescript
// 递归解包嵌套 Promise
type DeepUnwrap<T> = T extends Promise<infer U> ? DeepUnwrap<U> : T
```

---

**基本写法：函数重载推断**
`type <类型> = <T> extends { (...args: infer <A>): any; (...args: any[]): infer <R> } ? [<A>, <R>] : never`
```typescript
// 提取重载函数最后一个签名
type OverloadInfo<T> =
    T extends {
        (...args: infer A): any;
        (...args: any[]): infer R;
    } ? [A, R] : never
```

---

**基本写法：判断是否为数组**
`type <类型> = <T> extends any[] ? true : false`
```typescript
// 判断类型是否为数组
type IsArray<T> = T extends any[] ? true : false
type A = IsArray<number[]>  // true
type B = IsArray<number>    // false
```

---

**基本写法：判断两个类型相等**
`type <类型> = [<T>] extends [<U>] ? [<U>] extends [<T>] ? true : false : false`
```typescript
// 双向 extends 判断类型相等
type Equal<T, U> = [T] extends [U] ? ([U] extends [T] ? true : false) : false
```

---

## 实用模式

**基本写法：联合类型转交叉**
`type <类型> = <T> = <T> extends any ? (<参数>: <T>) => void : never`
```typescript
// 利用函数参数逆变转交叉
type UnionToIntersection<U> =
    (U extends any ? (x: U) => void : never) extends (x: infer I) => void ? I : never
```

---

**基本写法：提取对象可选键**
`type <类型> = { [K in keyof <T>]-?: {} extends Pick<<T>, <K>> ? <K> : never }[keyof <T>]`
```typescript
// 提取对象中可选属性的键
type OptionalKeys<T> = {
    [K in keyof T]-?: {} extends Pick<T, K> ? K : never
}[keyof T]
```

---

**基本写法：提取必填键**
`type <类型> = { [K in keyof <T>]-?: {} extends Pick<<T>, <K>> ? never : <K> }[keyof <T>]`
```typescript
// 提取对象中必填属性的键
type RequiredKeys<T> = {
    [K in keyof T]-?: {} extends Pick<T, K> ? never : K
}[keyof T]
```

---

## 注意事项

**基本写法：条件类型延迟求值**
`type <类型> = <T> extends <未知> ? <真> : <假>`
```typescript
// 当 T 未确定时条件类型延迟求值
type Foo<T> = T extends string ? "yes" : "no"
declare const t: Foo<X>  // X 未解析前 Foo 也不解析
```

---

**基本写法：never 的特殊行为**
`type <类型> = never extends <任何> ? <真> : <假>`
```typescript
// never extends 任何类型都为真
type R = never extends string ? "yes" : "no"  // "yes"
```



<!-- ============ 文档分隔线：009-typescript/014-MappedTypes.md ============ -->

# TypeScript 映射类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 映射类型基础

**基本写法：映射类型语法**
`type <类型> = { [K in keyof <T>]: <新类型> }`
```typescript
// 遍历键名重新定义类型
type Stringify<T> = { [K in keyof T]: string }
```

---

**基本写法：保持原类型**
`type <类型> = { [K in keyof <T>]: <T>[K] }`
```typescript
// 同态映射保持修饰符
type Copy<T> = { [K in keyof T]: T[K] }
```

---

**基本写法：将所有属性转为只读**
`type <类型> = { readonly [K in keyof <T>]: <T>[K] }`
```typescript
// 添加 readonly 修饰符
type Readonly<T> = { readonly [K in keyof T]: T[K] }
```

---

**基本写法：将所有属性变为可选**
`type <类型> = { [K in keyof <T>]?: <T>[K] }`
```typescript
// 添加 ? 修饰符
type Partial<T> = { [K in keyof T]?: T[K] }
```

---

## 修饰符操作

**基本写法：移除 readonly**
`type <类型> = { -readonly [K in keyof <T>]: <T>[K] }`
```typescript
// 使用 - 移除 readonly 修饰符
type Mutable<T> = { -readonly [K in keyof T]: T[K] }
```

---

**基本写法：移除可选**
`type <类型> = { [K in keyof <T>]-?: <T>[K] }`
```typescript
// 使用 - 移除 ? 修饰符
type Required<T> = { [K in keyof T]-?: T[K] }
```

---

**基本写法：同时添加修饰符**
`type <类型> = { readonly [K in keyof <T>]?: <T>[K] }`
```typescript
// 同时添加 readonly 与 ?
type Freeze<T> = { readonly [K in keyof T]?: T[K] }
```

---

## 键重映射

**基本写法：as 重映射键名**
`type <类型> = { [K in keyof <T> as <新键>]: <T>[K] }`
```typescript
// 使用 as 重命名键
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]
}
```

---

**基本写法：过滤键**
`type <类型> = { [K in keyof <T> as <条件> ? <K> : never]: <T>[K] }`
```typescript
// 通过条件返回 never 过滤键
type StringValuesOnly<T> = {
    [K in keyof T as T[K] extends string ? K : never]: T[K]
}
```

---

**基本写法：模板字面量重映射**
`type <类型> = { [K in keyof <T> as `<前缀>${<K>}`]: <T>[K] }`
```typescript
// 使用模板字面量生成新键名
type Prefix<T, P extends string> = {
    [K in keyof T as `${P}${Capitalize<string & K>}`]: T[K]
}
```

---

## 联合类型映射

**基本写法：基于联合类型映射**
`type <类型> = { [K in <联合类型>]: <类型> }`
```typescript
// 直接对联合类型映射
type Flags = "a" | "b" | "c"
type FlagMap = { [K in Flags]: boolean }
```

---

**基本写法：从数组生成映射**
`type <类型> = { [K in <数组>[number]]: <类型> }`
```typescript
// 数组元素作为键
const keys = ["a", "b", "c"] as const
type Map = { [K in typeof keys[number]]: string }
```

---

## 实用工具类型

**基本写法：Pick**
`type <结果> = Pick<<T>, <键联合>>`
```typescript
// 选取指定属性
type R = Pick<User, "id" | "name">
```

---

**基本写法：Omit**
`type <结果> = Omit<<T>, <键联合>>`
```typescript
// 移除指定属性
type R = Omit<User, "password">
```

---

**基本写法：Record**
`type <结果> = Record<<键>, <值>>`
```typescript
// 构造键值对类型
type R = Record<"a" | "b", number>
```

---

**基本写法：自定义 Pick**
`type <类型> = { [K in keyof <T> as <K> extends <键> ? <K> : never]: <T>[K] }`
```typescript
// 通过 as 实现自定义 Pick
type MyPick<T, K extends keyof T> = {
    [P in keyof T as P extends K ? P : never]: T[P]
}
```

---

**基本写法：自定义 Omit**
`type <类型> = { [K in keyof <T> as <K> extends <排除> ? never : <K>]: <T>[K> }`
```typescript
// 通过 as 实现自定义 Omit
type MyOmit<T, K extends keyof T> = {
    [P in keyof T as P extends K ? never : P]: T[P]
}
```

---

## 属性过滤

**基本写法：按值类型过滤**
`type <类型> = { [K in keyof <T> as <T>[K] extends <条件> ? <K> : never]: <T>[K] }`
```typescript
// 仅保留函数类型的属性
type Functions<T> = {
    [K in keyof T as T[K] extends Function ? K : never]: T[K]
}
```

---

**基本写法：按值类型转换**
`type <类型> = { [K in keyof <T>]: <T>[K] extends <条件> ? <新类型> : <T>[K] }`
```typescript
// 将字符串属性转为数字
type StringToNumber<T> = {
    [K in keyof T]: T[K] extends string ? number : T[K]
}
```

---

## 同态与非同态

**基本写法：同态映射**
`type <类型> = { [K in keyof <T>]: <T>[K> }`
```typescript
// 同态映射保留原属性修饰符
type Homomorphic<T> = { [K in keyof T]: T[K] }
```

---

**基本写法：非同态映射**
`type <类型> = { [K in <联合>]: <类型> }`
```typescript
// 非同态映射不保留修饰符
type NonHomomorphic = { [K in "a" | "b"]: string }
```

---

## 高级模式

**基本写法：条件映射**
`type <类型> = <T> extends <条件> ? { [K in keyof <T>]: <新> } : <T>`
```typescript
// 根据条件决定是否映射
type MaybeStringify<T> =
    T extends object ? { [K in keyof T]: string } : T
```

---

**基本写法：递归映射**
`type <类型> = { [K in keyof <T>]: <T>[K> extends object ? <类型><<T>[K>> : <T>[K> }`
```typescript
// 深度 readonly
type DeepReadonly<T> = {
    [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K]
}
```

---

**基本写法：深度 Partial**
`type <类型> = { [K in keyof <T>]?: <T>[K> extends object ? <类型><<T>[K>> : <T>[K> }`
```typescript
// 所有层级可选
type DeepPartial<T> = {
    [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K]
}
```

---

**基本写法：深度 Mutable**
`type <类型> = { -readonly [K in keyof <T>]: <T>[K> extends object ? <类型><<T>[K>> : <T>[K> }`
```typescript
// 移除所有层级 readonly
type DeepMutable<T> = {
    -readonly [K in keyof T]: T[K] extends object ? DeepMutable<T[K]> : T[K]
}
```

---

## 键名转换

**基本写法：键名大写**
`type <类型> = { [K in keyof <T> as Uppercase<string & <K>>]: <T>[K> }`
```typescript
// 所有键名转为大写
type UpperKeys<T> = {
    [K in keyof T as Uppercase<string & K>]: T[K]
}
```

---

**基本写法：键名小写**
`type <类型> = { [K in keyof <T> as Lowercase<string & <K>>]: <T>[K> }`
```typescript
// 所有键名转为小写
type LowerKeys<T> = {
    [K in keyof T as Lowercase<string & K>]: T[K]
}
```

---

**基本写法：添加前缀**
`type <类型> = { [K in keyof <T> as `<前缀>${string & <K>}`]: <T>[K> }`
```typescript
// 给所有键添加前缀
type WithPrefix<T, P extends string> = {
    [K in keyof T as `${P}${string & K}`]: T[K]
}
```

---

**基本写法：移除前缀**
`type <类型> = { [K in keyof <T> as <K> extends `<前缀>${infer <R>}` ? <R> : <K>]: <T>[K> }`
```typescript
// 移除指定前缀
type RemovePrefix<T, P extends string> = {
    [K in keyof T as K extends `${P}${infer R}` ? R : K]: T[K]
}
```

---

## 实用模式

**基本写法：getter setter 类型**
`type <类型> = { [K in keyof <T> as `get${Capitalize<string & <K>>}`]: () => <T>[K> }`
```typescript
// 生成 getter 方法类型
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]
}
```

---

**基本写法：setter 类型**
`type <类型> = { [K in keyof <T> as `set${Capitalize<string & <K>>}`]: (<值>: <T>[K>) => void }`
```typescript
// 生成 setter 方法类型
type Setters<T> = {
    [K in keyof T as `set${Capitalize<string & K>}`]: (v: T[K]) => void
}
```

---

**基本写法：事件处理器映射**
`type <类型> = { [K in keyof <T> as `on${Capitalize<string & <K>>}`]: (<事件>: <T>[K>) => void }`
```typescript
// 生成事件处理函数类型
type Handlers<T> = {
    [K in keyof T as `on${Capitalize<string & K>}`]: (e: T[K]) => void
}
```

---

## 修饰符组合

**基本写法：可选转必填同时移除 readonly**
`type <类型> = { -readonly [K in keyof <T>]-?: <T>[K> }`
```typescript
// 组合移除两个修饰符
type Writable<T> = { -readonly [K in keyof T]-?: T[K] }
```

---

**基本写法：互斥属性**
`type <类型> = { [K in keyof <T>]: <T>[K> } & { [K in keyof <T>]?: never }`
```typescript
// 让对象的多个属性互斥只能选一个
type XOR<T> = { [K in keyof T]: T[K] } & { [K in keyof T]?: never }
```



<!-- ============ 文档分隔线：009-typescript/015-TemplateLiteralTypes.md ============ -->

# TypeScript 模板字面量类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础语法

**基本写法：模板字面量类型**
`type <类型> = `<前缀>${<类型>}``
```typescript
// 用反引号定义字符串类型
type Greeting = `hello ${string}`
```

---

**基本写法：固定字符串拼接**
`type <类型> = `<前缀>${<字面量联合>}``
```typescript
// 与字面量联合类型组合
type Side = "left" | "right"
type SideProperty = `padding-${Side}`  // "padding-left" | "padding-right"
```

---

**基本写法：多变量拼接**
`type <类型> = `${<变量1>}-${<变量2>}``
```typescript
// 多个变量拼接
type EventType = "click" | "hover"
type Handler = `on${Capitalize<EventType>}`
```

---

## 内置字符转换类型

**基本写法：Uppercase**
`type <结果> = Uppercase<<字符串类型>>`
```typescript
// 转为大写
type T = Uppercase<"hello">  // "HELLO"
```

---

**基本写法：Lowercase**
`type <结果> = Lowercase<<字符串类型>>`
```typescript
// 转为小写
type T = Lowercase<"HELLO">  // "hello"
```

---

**基本写法：Capitalize**
`type <结果> = Capitalize<<字符串类型>>`
```typescript
// 首字母大写
type T = Capitalize<"hello">  // "Hello"
```

---

**基本写法：Uncapitalize**
`type <结果> = Uncapitalize<<字符串类型>>`
```typescript
// 首字母小写
type T = Uncapitalize<"Hello">  // "hello"
```

---

## 字符串解析

**基本写法：infer 提取前缀**
`type <类型> = <S> extends `${infer <Head>}${string}` ? <Head> : never`
```typescript
// 提取字符串前缀
type GetPrefix<S extends string> = S extends `${infer H}${string}` ? H : never
```

---

**基本写法：infer 提取后缀**
`type <类型> = <S> extends `${string}${infer <Tail>}` ? <Tail> : never`
```typescript
// 提取字符串后缀
type GetSuffix<S extends string> = S extends `${string}${infer T}` ? T : never
```

---

**基本写法：分割字符串**
`type <类型> = <S> extends `${infer <Head>}${<分隔符>}${infer <Tail>}` ? [<Head>, ...<类型><<Tail>>] : []`
```typescript
// 按分隔符分割字符串为元组
type Split<S extends string, D extends string> =
    S extends `${infer Head}${D}${infer Tail}` ? [Head, ...Split<Tail, D>] : [S]
```

---

**基本写法：解析路径段**
`type <类型> = <S> extends `${infer <Seg>}/${infer <Rest>}` ? [<Seg>, ...<类型><<Rest>>] : [<S>]`
```typescript
// 解析路径为段元组
type PathSegments<S extends string> =
    S extends `${infer Seg}/${infer Rest}` ? [Seg, ...PathSegments<Rest>] : [S]
```

---

## 实用工具类型

**基本写法：getter 名称**
`type <类型> = `get${Capitalize<<K>>}``
```typescript
// 生成 getter 方法名
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]
}
```

---

**基本写法：setter 名称**
`type <类型> = `set${Capitalize<<K>>}``
```typescript
// 生成 setter 方法名
type Setters<T> = {
    [K in keyof T as `set${Capitalize<string & K>}`]: (v: T[K]) => void
}
```

---

**基本写法：事件处理器名称**
`type <类型> = `on${Capitalize<<K>>}``
```typescript
// 生成 onXxx 事件处理器
type Handlers<T> = {
    [K in string & keyof T as `on${Capitalize<K>}`]: (e: T[K]) => void
}
```

---

**基本写法：CSS 属性**
`type <类型> = `${<属性>}-${<值>}``
```typescript
// 生成 CSS 属性字符串
type CSSProperty = `${string}-${string}`
```

---

## 路由类型

**基本写法：动态路由提取**
`type <类型> = <P> extends `${string}/:${infer <Param>}` ? <Param> : never`
```typescript
// 提取路由参数名
type GetRouteParam<P extends string> =
    P extends `${string}/:${infer Param}` ? Param : never
```

---

**基本写法：提取所有路由参数**
`type <类型> = <P> extends `${infer <Start>}:${infer <Param>}/${infer <Rest>}` ? <Param> | <类型><<Rest>> : <P> extends `${infer <Start>}:${infer <Param>}` ? <Param> : never`
```typescript
// 提取所有路由参数
type RouteParams<P extends string> =
    P extends `${infer _}:${infer Param}/${infer Rest}`
        ? Param | RouteParams<`/${Rest}`>
        : P extends `${infer _}:${infer Param}` ? Param : never
```

---

**基本写法：路由参数对象**
`type <类型> = { [K in <类型><<P>>]: string }`
```typescript
// 路由参数转为对象类型
type Params<P extends string> = { [K in RouteParams<P>]: string }
type R = Params<"/user/:id/post/:postId">  // { id: string; postId: string }
```

---

## 字符串拼接

**基本写法：联合展开**
`type <类型> = `${<联合1>}-${<联合2>}``
```typescript
// 联合类型会自动展开
type T = `${"a" | "b"}-${"x" | "y"}`  // "a-x" | "a-y" | "b-x" | "b-y"
```

---

**基本写法：与 number 拼接**
`type <类型> = `${<string>}-${number}``
```typescript
// number 类型在模板中转为字符串
type T = `id-${number}`
```

---

**基本写法：与 boolean 拼接**
`type <类型> = `${<boolean>}``
```typescript
// boolean 展开为 true | false
type T = `${boolean}`  // "true" | "false"
```

---

## 字符串操作

**基本写法：字符串替换**
`type <类型> = <S> extends `${infer <L>}${<From>}${infer <R>}` ? `${<L>}${<To>}${<类型><<R>>}` : <S>`
```typescript
// 替换所有匹配子串
type ReplaceAll<S extends string, From extends string, To extends string> =
    S extends `${infer L}${From}${infer R}` ? `${L}${To}${ReplaceAll<R, From, To>}` : S
```

---

**基本写法：去除空白**
`type <类型> = <S> extends ` ${infer <R>}` ? <类型><<R>> : <S> extends `${infer <L>} ` ? <类型><<L>> : <S>`
```typescript
// 递归去除两端空白
type Trim<S extends string> =
    S extends ` ${infer R}` ? Trim<R> :
    S extends `${infer L} ` ? Trim<L> : S
```

---

**基本写法：字符串反转**
`type <类型> = <S> extends `${infer <First>}${infer <Rest>}` ? `${<类型><<Rest>>}${<First>}` : <S>`
```typescript
// 递归反转字符串
type Reverse<S extends string> =
    S extends `${infer First}${infer Rest}` ? `${Reverse<Rest>}${First}` : S
```

---

## 实用模式

**基本写法：环境变量类型**
`type <类型> = `VITE_${string}``
```typescript
// 限制环境变量键名格式
type EnvKey = `VITE_${string}`
```

---

**基本写法：HTTP 方法路径**
`type <类型> = `${<方法>} ${<路径>}``
```typescript
// API 路由描述类型
type Route = `${"GET" | "POST"} ${string}`
```

---

**基本写法：CSS 类名组合**
`type <类型> = `${<前缀>}__${<元素>}``
```typescript
// BEM 命名规范类型
type BEM<B extends string, E extends string, M extends string> =
    `${B}__${E}--${M}`
```

---

**基本写法：枚举键转值**
`type <类型> = `${<联合>}``
```typescript
// 枚举值类型推导
type Status = "pending" | "success" | "error"
type StatusMessage = `${Status} message`
```

---

## 类型安全事件

**基本写法：事件总线**
`type <类型> = `on${Capitalize<<K>>}``
```typescript
// 强类型事件总线
type EventMap = { click: string; hover: number }
type EventName = `on${Capitalize<string & keyof EventMap>}`
// "onClick" | "onHover"
```

---

**基本写法：表单字段验证**
`type <类型> = `${<字段>}Error` | `${<字段>}Valid``
```typescript
// 表单状态类型
type FormField = "name" | "email"
type FormState = `${FormField}Error` | `${FormField}Valid`
```

---

## 高级应用

**基本写法：组合多个工具**
`type <类型> = `set${Capitalize<<K>>}``
```typescript
// 多工具组合生成 setter
type Setters<T> = {
    [K in keyof T as `set${Capitalize<string & K>}`]: (v: T[K]) => void
}
```

---

**基本写法：嵌套路径访问**
`type <类型> = <T> extends object ? { [K in keyof <T>]: <K> | `${<K>}.${<类型><<T>[K]>>}` }[keyof <T>] : never`
```typescript
// 生成深层属性路径如 "a.b.c"
type Path<T> =
    T extends object
        ? { [K in keyof T & string]: K | `${K}.${Path<T[K]>}` }[keyof T & string]
        : never
```

---

**基本写法：版本号类型**
`type <类型> = `${number}.${number}.${number}``
```typescript
// semver 版本号格式
type Version = `${number}.${number}.${number}`
const v: Version = "1.0.0"
```

---

## 注意事项

**基本写法：模板字面量限制**
`type <类型> = `${string & <K>}``
```typescript
// 键名需 string 交集转换
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]
}
```

---

**基本写法：递归深度限制**
`type <类型> = <S> extends ... ? ... : <S>`
```typescript
// 递归模板字面量需注意深度
type Deep<S extends string> = S extends `${infer H}${infer R}` ? Deep<R> : S
```



<!-- ============ 文档分隔线：009-typescript/016-UtilityTypes.md ============ -->

# TypeScript 工具类型速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Partial 与 Required

**基本写法：Partial 所有可选**
`type <结果> = Partial<<T>>`
```typescript
// 所有属性变为可选
type R = Partial<User>
```

---

**基本写法：Required 所有必填**
`type <结果> = Required<<T>>`
```typescript
// 所有属性变为必填
type R = Required<User>
```

---

**基本写法：自定义 Partial**
`type <类型> = { [K in keyof <T>]?: <T>[K] }`
```typescript
// 手动实现 Partial
type MyPartial<T> = { [K in keyof T]?: T[K] }
```

---

## Readonly 与 Mutable

**基本写法：Readonly 只读**
`type <结果> = Readonly<<T>>`
```typescript
// 所有属性变为只读
type R = Readonly<User>
```

---

**基本写法：自定义 Readonly**
`type <类型> = { readonly [K in keyof <T>]: <T>[K] }`
```typescript
// 手动实现 Readonly
type MyReadonly<T> = { readonly [K in keyof T]: T[K] }
```

---

**基本写法：Mutable 移除只读**
`type <类型> = { -readonly [K in keyof <T>]: <T>[K] }`
```typescript
// 移除所有 readonly 修饰符
type Mutable<T> = { -readonly [K in keyof T]: T[K] }
```

---

## Record

**基本写法：Record 键值对**
`type <结果> = Record<<键>, <值>>`
```typescript
// 构造键值对类型
type R = Record<"a" | "b", number>
```

---

**基本写法：自定义 Record**
`type <类型> = { [K in <键>]: <值> }`
```typescript
// 手动实现 Record
type MyRecord<K extends keyof any, V> = { [P in K]: V }
```

---

**基本写法：枚举映射**
`type <结果> = Record<<枚举>, <值>>`
```typescript
// 用枚举作为键
enum Status { Active, Inactive }
type StatusMap = Record<Status, string>
```

---

## Pick 与 Omit

**基本写法：Pick 选取**
`type <结果> = Pick<<T>, <键联合>>`
```typescript
// 选取指定属性
type R = Pick<User, "id" | "name">
```

---

**基本写法：自定义 Pick**
`type <类型> = { [K in <键>]: <T>[K] }`
```typescript
// 手动实现 Pick
type MyPick<T, K extends keyof T> = { [P in K]: T[P] }
```

---

**基本写法：Omit 排除**
`type <结果> = Omit<<T>, <键联合>>`
```typescript
// 排除指定属性
type R = Omit<User, "password">
```

---

**基本写法：自定义 Omit**
`type <类型> = <T> extends any ? { [K in keyof <T> as <K> extends <排除> ? never : <K>]: <T>[K] } : never`
```typescript
// 手动实现 Omit
type MyOmit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>
```

---

## Exclude 与 Extract

**基本写法：Exclude 排除**
`type <结果> = Exclude<<联合>, <排除>>`
```typescript
// 从联合类型排除
type R = Exclude<"a" | "b" | "c", "a">  // "b" | "c"
```

---

**基本写法：Extract 提取**
`type <结果> = Extract<<联合>, <提取>>`
```typescript
// 从联合类型提取
type R = Extract<string | number | boolean, string | number>
```

---

**基本写法：NonNullable 排除空值**
`type <结果> = NonNullable<<T>>`
```typescript
// 排除 null 与 undefined
type R = NonNullable<string | null | undefined>  // string
```

---

## 函数相关

**基本写法：ReturnType 返回类型**
`type <结果> = ReturnType<<函数>>`
```typescript
// 获取函数返回类型
type R = ReturnType<() => string>  // string
```

---

**基本写法：Parameters 参数元组**
`type <结果> = Parameters<<函数>>`
```typescript
// 获取函数参数元组
type P = Parameters<(a: number, b: string) => void>  // [number, string]
```

---

**基本写法：ConstructorParameters 构造参数**
`type <结果> = ConstructorParameters<<构造器>>`
```typescript
// 获取构造器参数元组
type P = ConstructorParameters<ErrorConstructor>
```

---

**基本写法：InstanceType 实例类型**
`type <结果> = InstanceType<<构造器>>`
```typescript
// 获取构造器实例类型
type I = InstanceType<typeof Error>
```

---

**基本写法：Awaited 解包 Promise**
`type <结果> = Awaited<<Promise>>`
```typescript
// 递归解包 Promise
type R = Awaited<Promise<Promise<number>>>  // number
```

---

## keyof 与 typeof

**基本写法：keyof 键联合**
`type <结果> = keyof <T>`
```typescript
// 获取所有键的联合类型
type K = keyof User
```

---

**基本写法：typeof 值类型**
`type <结果> = typeof <值>`
```typescript
// 获取变量类型
const config = { port: 3000 }
type Config = typeof config
```

---

**基本写法：typeof 枚举值**
`type <结果> = typeof <枚举>[keyof typeof <枚举>]`
```typescript
// 获取枚举值类型
enum Color { Red, Green }
type ColorValue = typeof Color[keyof typeof Color]  // Color.Red | Color.Green
```

---

## 索引访问

**基本写法：索引类型访问**
`type <结果> = <T>[<键>]`
```typescript
// 通过键访问属性类型
type NameType = User["name"]
```

---

**基本写法：数组元素类型**
`type <结果> = <数组>[number]`
```typescript
// 获取数组元素类型
type Item = typeof arr[number]
```

---

**基本写法：函数返回值类型**
`type <结果> = ReturnType<typeof <函数>>`
```typescript
// 推导函数返回值类型
type Data = ReturnType<typeof fetchUser>
```

---

## 联合与交叉

**基本写法：联合类型**
`type <结果> = <类型1> | <类型2>`
```typescript
// 或关系
type StringOrNumber = string | number
```

---

**基本写法：交叉类型**
`type <结果> = <类型1> & <类型2>`
```typescript
// 与关系合并
type User = Person & { age: number }
```

---

**基本写法：互斥联合**
`type <类型> = { <键>: <值1> } | { <键>: <值2> }`
```typescript
// 可辨识联合
type Result = { ok: true; data: string } | { ok: false; error: Error }
```

---

## 类型断言

**基本写法：as 断言**
`<值> as <类型>`
```typescript
// 显式断言类型
let s = value as string
```

---

**基本写法：const 断言**
`<值> as const`
```typescript
// 字面量化断言
const arr = [1, 2] as const  // readonly [1, 2]
```

---

**基本写法：satisfies**
`<值> satisfies <类型>`
```typescript
// 类型检查但保留推导类型
const cfg = { port: 3000 } satisfies Config
```

---

## 实用组合

**基本写法：可选与只读组合**
`type <结果> = Readonly<Partial<<T>>>`
```typescript
// 只读可选组合
type R = Readonly<Partial<User>>
```

---

**基本写法：Pick 与 Readonly**
`type <结果> = Readonly<Pick<<T>, <键>>>`
```typescript
// 选取部分只读
type R = Readonly<Pick<User, "id">>
```

---

**基本写法：Omit 与 Partial**
`type <结果> = Partial<Omit<<T>, <键>>>`
```typescript
// 排除部分后可选
type R = Partial<Omit<User, "id">>
```

---

**基本写法：Record 与 Partial**
`type <结果> = Record<<键>, Partial<<T>>>`
```typescript
// 值为部分对象
type R = Record<string, Partial<User>>
```

---

## 高级工具

**基本写法：深度 Partial**
`type <类型> = { [K in keyof <T>]?: <T>[K] extends object ? <类型><<T>[K]> : <T>[K] }`
```typescript
// 所有层级可选
type DeepPartial<T> = {
    [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K]
}
```

---

**基本写法：深度 Readonly**
`type <类型> = { readonly [K in keyof <T>]: <T>[K] extends object ? <类型><<T>[K]> : <T>[K] }`
```typescript
// 所有层级只读
type DeepReadonly<T> = {
    readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K]
}
```

---

**基本写法：永不类型**
`type <结果> = never`
```typescript
// 永不出现的类型用于穷尽检查
type Never = never
```

---

**基本写法：unknown 类型**
`type <结果> = unknown`
```typescript
// 任意值需类型检查后使用
type Any = unknown
```

---

## 路径类型

**基本写法：获取对象深层类型**
`type <结果> = <T>[<键>]`
```typescript
// 通过路径访问深层类型
type UserName = User["profile"]["name"]
```

---

**基本写法：可选链类型**
`type <结果> = <T>[<键>] | undefined`
```typescript
// 处理可选属性
type MaybeName = User["profile"]?.["name"]
```

---

## 类型谓词

**基本写法：自定义类型守卫**
`function <函数>(<参数>: <T>): <参数> is <类型>`
```typescript
// 自定义类型谓词
function isString(v: unknown): v is string {
    return typeof v === "string"
}
```

---

**基本写法：断言函数**
`function <函数>(<参数>: <T>): asserts <参数> is <类型>`
```typescript
// 断言函数失败抛错
function assertDefined<T>(v: T | undefined): asserts v is T {
    if (v === undefined) throw new Error("undefined")
}
```

---

## 类型实用模式

**基本写法：可选属性变必填**
`type <结果> = Required<Pick<<T>, <键>>>`
```typescript
// 将部分可选变必填
type R = Required<Pick<User, "id">>
```

---

**基本写法：联合转交叉**
`type <类型> = (<U> extends any ? (<参数>: <U>) => void : never) extends (<参数>: infer <I>) => void ? <I> : never`
```typescript
// 联合类型转交叉类型
type UnionToIntersection<U> =
    (U extends any ? (x: U) => void : never) extends (x: infer I) => void ? I : never
```

---

**基本写法：获取可选键**
`type <类型> = { [K in keyof <T>]-?: {} extends Pick<<T>, <K>> ? <K> : never }[keyof <T>]`
```typescript
// 提取对象中可选属性的键
type OptionalKeys<T> = {
    [K in keyof T]-?: {} extends Pick<T, K> ? K : never
}[keyof T]
```

---

**基本写法：获取必填键**
`type <类型> = { [K in keyof <T>]-?: {} extends Pick<<T>, <K>> ? never : <K> }[keyof <T>]`
```typescript
// 提取对象中必填属性的键
type RequiredKeys<T> = {
    [K in keyof T]-?: {} extends Pick<T, K> ? never : K
}[keyof T]
```



<!-- ============ 文档分隔线：009-typescript/017-TypeGuardsNarrowing.md ============ -->

# TypeScript 类型守卫与收窄

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## typeof 守卫

**基本写法：typeof 守卫**
`typeof <变量> === <类型字符串>`
```typescript
// 通过 typeof 收窄基本类型
function fn(x: string | number) {
    if (typeof x === "string") x.toUpperCase();
    else x.toFixed(2);
}
```

---

**基本写法：typeof 联合类型**
`typeof <变量> !== <类型字符串>`
```typescript
// 反向判断收窄
function fn(x: string | number) {
    if (typeof x !== "string") x.toFixed();  // x: number
}
```

---

**基本写法：typeof 支持类型**
`typeof <变量> === "string" | "number" | "boolean" | "bigint" | "symbol" | "undefined" | "object" | "function"`
```typescript
// typeof 仅支持这些字符串
typeof "a"  // "string"
typeof 1    // "number"
typeof {}   // "object"
```

---

## instanceof 守卫

**基本写法：instanceof 守卫**
`<变量> instanceof <类>`
```typescript
// 通过 instanceof 收窄类实例
function fn(e: Error | Date) {
    if (e instanceof Error) e.message;
    else e.getTime();
}
```

---

**基本写法：instanceof 数组**
`<变量> instanceof Array`
```typescript
// 判断是否为数组
function fn(x: string | string[]) {
    if (x instanceof Array) x.length;
    else x.toUpperCase();
}
```

---

**基本写法：instanceof 自定义类**
`<变量> extends <类>`
```typescript
// 自定义类的类型收窄
class Cat { meow(): void {} }
class Dog { bark(): void {} }
function speak(animal: Cat | Dog) {
    if (animal instanceof Cat) animal.meow();
    else animal.bark();
}
```

---

## in 守卫

**基本写法：in 守卫**
`<属性> in <对象>`
```typescript
// 通过属性存在判断收窄
function fn(x: { a: string } | { b: number }) {
    if ("a" in x) x.a;
    else x.b;
}
```

---

**基本写法：in 与可辨识联合**
`<属性> in <对象>`
```typescript
// 可辨识联合收窄
type Shape = Circle | Square
interface Circle { kind: "circle"; radius: number }
interface Square { kind: "square"; size: number }
function area(s: Shape) {
    if ("radius" in s) return Math.PI * s.radius ** 2;
    return s.size ** 2;
}
```

---

**基本写法：可选属性判断**
`<属性> in <对象>`
```typescript
// 判断可选属性是否存在
function fn(x: { name: string; age?: number }) {
    if ("age" in x) x.age.toFixed();
}
```

---

## 可辨识联合

**基本写法：字面量类型辨识**
`type <类型> = { kind: <字面量> } | { kind: <字面量> }`
```typescript
// 通过字面量属性辨识
type Result =
    | { status: "success"; data: string }
    | { status: "error"; error: Error }
```

---

**基本写法：switch 收窄**
`switch (<变量>.<辨识属性>)`
```typescript
// switch 分支自动收窄
function handle(r: Result) {
    switch (r.status) {
        case "success": return r.data;
        case "error": return r.error.message;
    }
}
```

---

**基本写法：穷尽检查**
`assertNever(<变量>: never)`
```typescript
// 漏处理分支会编译错误
function assertNever(x: never): never {
    throw new Error(`unexpected: ${x}`);
}
function handle(r: Result) {
    switch (r.status) {
        case "success": return r.data;
        case "error": return r.error.message;
        default: return assertNever(r);
    }
}
```

---

## 自定义类型守卫

**基本写法：is 谓词**
`function <函数>(<参数>: <T>): <参数> is <类型>`
```typescript
// 自定义类型守卫
function isString(v: unknown): v is string {
    return typeof v === "string"
}
if (isString(v)) v.toUpperCase();
```

---

**基本写法：对象类型守卫**
`function <函数>(<参数>: any): <参数> is <类型>`
```typescript
// 判断对象结构
function isUser(v: any): v is { name: string; age: number } {
    return v && typeof v.name === "string" && typeof v.age === "number"
}
```

---

**基本写法：数组类型守卫**
`function <函数>(<参数>: any): <参数> is <类型>[]`
```typescript
// 判断是否为某类型数组
function isStringArray(v: any): v is string[] {
    return Array.isArray(v) && v.every(i => typeof i === "string")
}
```

---

**基本写法：联合类型守卫**
`function <函数>(<参数>: <联合>): <参数> is <类型>`
```typescript
// 收窄联合类型
type Animal = Cat | Dog
function isCat(a: Animal): a is Cat {
    return a instanceof Cat
}
```

---

## asserts 断言

**基本写法：asserts 断言函数**
`function <函数>(<参数>: <T>): asserts <参数> is <类型>`
```typescript
// 断言失败抛错成功则收窄
function assertString(v: unknown): asserts v is string {
    if (typeof v !== "string") throw new Error("not string")
}
assertString(v); v.toUpperCase();
```

---

**基本写法：asserts 非空断言**
`function <函数>(<参数>: <T> | null | undefined): asserts <参数> is <类型>`
```typescript
// 断言非空
function assertDefined<T>(v: T | undefined): asserts v is T {
    if (v === undefined) throw new Error("undefined")
}
```

---

**基本写法：asserts 永真**
`function <函数>(<条件>: any): asserts <条件>`
```typescript
// 断言条件为真
function assert(condition: any): asserts condition {
    if (!condition) throw new Error("assertion failed")
}
assert(x > 0);  // 之后 x 推断为 truthy
```

---

## 控制流收窄

**基本写法：if 收窄**
`if (<条件>) { }`
```typescript
// if 分支内自动收窄
function fn(x: string | null) {
    if (x !== null) x.toUpperCase();  // x: string
}
```

---

**基本写法：三元表达式收窄**
`<条件> ? <真分支> : <假分支>`
```typescript
// 三元分支分别收窄
function fn(x: string | number) {
    return typeof x === "string" ? x.length : x.toFixed()
}
```

---

**基本写法：逻辑与短路**
`<条件> && <使用>`
```typescript
// && 短路收窄
function fn(x: string | null) {
    x && x.toUpperCase();  // x: string
}
```

---

**基本写法：逻辑或默认值**
`<变量> ?? <默认>`
```typescript
// ?? 移除 null undefined
function fn(x: string | null) {
    let s = x ?? "default";  // s: string
}
```

---

## 数组收窄

**基本写法：filter 收窄**
`<数组>.filter(<守卫>)`
```typescript
// filter 配合守卫收窄
function isString(v: any): v is string { return typeof v === "string" }
const arr: (string | number)[] = ["a", 1];
const strs = arr.filter(isString);  // string[]
```

---

**基本写法：filter 内联守卫**
`<数组>.filter((<项>): <项> is <类型> => <条件>)`
```typescript
// 内联守卫函数
const strs = arr.filter((x): x is string => typeof x === "string")
```

---

**基本写法：find 收窄**
`<数组>.find(<守卫>)`
```typescript
// find 后守卫
const item = arr.find(isString)
if (item) item.toUpperCase()
```

---

## 解构收窄

**基本写法：解构类型守卫**
`const { <属性> } = <对象>`
```typescript
// 解构后类型守卫仍有效
function fn(x: { a: string } | { b: number }) {
    if ("a" in x) {
        const { a } = x;  // a: string
    }
}
```

---

## 交叉类型收窄

**基本写法：交叉类型守卫**
`<变量> is <类型1> & <类型2>`
```typescript
// 守卫返回交叉类型
function isCatDog(a: Cat | Dog): a is Cat & Dog {
    return a instanceof Cat && a instanceof Dog
}
```

---

## 常见陷阱

**基本写法：typeof null**
`typeof <变量> === "object"`
```typescript
// typeof null 为 object 需额外判断
function fn(x: object | null) {
    if (x && typeof x === "object") {}
}
```

---

**基本写法：数组 typeof**
`typeof <数组>`
```typescript
// 数组的 typeof 是 object 需用 Array.isArray
typeof []  // "object"
Array.isArray([])  // true
```

---

**基本写法：truthy 陷阱**
`if (<变量>)`
```typescript
// truthy 会过滤掉 0 与 空字符串
function fn(x: string | number | null) {
    if (x) {}  // x: string | number 但 0 与 "" 被排除
}
```

---

## 实用模式

**基本写法：可选链收窄**
`<对象>?.<属性>`
```typescript
// 可选链自动处理 null undefined
function fn(x?: { name: string }) {
    return x?.name  // string | undefined
}
```

---

**基本写法：空值合并**
`<变量> ?? <默认>`
```typescript
// 仅 null undefined 触发默认值
function fn(x?: string) {
    const s = x ?? "default"
}
```

---

**基本写法：类型守卫组合**
`<守卫1>(<变量>) && <守卫2>(<变量>)`
```typescript
// 多守卫组合判断
function isStringAndNonEmpty(v: unknown): v is string {
    return typeof v === "string" && v.length > 0
}
```

---

**基本写法：断言函数复用**
`function <断言>(<值>): asserts <值> is <类型>`
```typescript
// 复用断言函数
function assertNonNull<T>(v: T | null | undefined): asserts v is T {
    if (v == null) throw new Error("null")
}
assertNonNull(user); user.name;
```

---

## 类型守卫与映射

**基本写法：守卫返回 Promise**
`async function <函数>(<参数>): <参数> is <类型>`
```typescript
// 注意异步函数不能直接用 is 谓词
// 需通过 await 后再用同步守卫
async function fn(x: unknown) {
    await Promise.resolve()
    if (typeof x === "string") x.toUpperCase()
}
```

---

**基本写法：穷尽检查工具**
`function <assertNever>(<变量>: never): never`
```typescript
// 编译期保证穷尽所有分支
function assertNever(x: never): never {
    throw new Error(`Unhandled: ${JSON.stringify(x)}`)
}
```



<!-- ============ 文档分隔线：009-typescript/018-Decorators.md ============ -->

# TypeScript 装饰器

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 装饰器基础

**基本写法：类装饰器**
`function <装饰器>(<target>: <构造器>) { }`
```typescript
// 类装饰器接收构造器返回新构造器
function Log<T extends new (...args: any[]) => any>(target: T): T {
    return class extends target { }
}
@Log class Foo {}
```

---

**基本写法：方法装饰器**
`function <装饰器>(<target>, <key>, <descriptor>) { }`
```typescript
// 方法装饰器接收原型 方法名 描述符
function Log(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    desc.value = function (...args: any[]) {
        console.log(`call ${key}`)
        return orig.apply(this, args)
    }
}
```

---

**基本写法：属性装饰器**
`function <装饰器>(<target>, <key>) { }`
```typescript
// 属性装饰器接收原型 与 属性名
function Meta(target: any, key: string) {
    Object.defineProperty(target, key, { value: null })
}
```

---

**基本写法：参数装饰器**
`function <装饰器>(<target>, <key>, <index>) { }`
```typescript
// 参数装饰器接收原型 方法名 参数索引
function Required(target: any, key: string, index: number) {
    console.log(`param ${index} of ${key}`)
}
```

---

## 方法装饰器实战

**基本写法：日志装饰器**
`function <Log>(<target>, <key>, <descriptor>)`
```typescript
// 记录方法调用
function Log(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    desc.value = function (...args: any[]) {
        console.log(`${key} called with`, args)
        return orig.apply(this, args)
    }
}
class Service { @Log greet(name: string) { return `hi ${name}` } }
```

---

**基本写法：性能测量装饰器**
`function <Measure>(<target>, <key>, <descriptor>)`
```typescript
// 测量方法执行时间
function Measure(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    desc.value = function (...args: any[]) {
        const start = performance.now()
        const result = orig.apply(this, args)
        console.log(`${key} took ${performance.now() - start}ms`)
        return result
    }
}
```

---

**基本写法：错误捕获装饰器**
`function <Catch>(<target>, <key>, <descriptor>)`
```typescript
// 统一捕获方法异常
function Catch(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    desc.value = async function (...args: any[]) {
        try { return await orig.apply(this, args) }
        catch (e) { console.error(`${key} error`, e) }
    }
}
```

---

## 类装饰器实战

**基本写法：单例装饰器**
`function <Singleton><<T>>(<target>: <T>)`
```typescript
// 强制类为单例
function Singleton<T extends new (...args: any[]) => any>(target: T): T {
    let instance: InstanceType<T>
    return class extends target {
        constructor(...args: any[]) {
            if (instance) return instance
            super(...args)
            instance = this as any
        }
    }
}
@Singleton class Config {}
```

---

**基本写法：混入装饰器**
`function <Mixin>(...<bases>): <类装饰器>`
```typescript
// 混入多个类的方法
function Mixin(...bases: any[]) {
    return function (target: any) {
        bases.forEach(base => {
            Object.getOwnPropertyNames(base.prototype).forEach(name => {
                target.prototype[name] = base.prototype[name]
            })
        })
    }
}
```

---

**基本写法：标签元数据**
`function <Tag>(<名称>: string): <类装饰器>`
```typescript
// 给类附加元数据
function Tag(name: string) {
    return function <T extends new (...args: any[]) => any>(target: T): T {
        (target as any).tag = name
        return target
    }
}
@Tag("service") class Service {}
```

---

## 属性装饰器实战

**基本写法：默认值装饰器**
`function <Default>(<值>): <属性装饰器>`
```typescript
// 为属性设置默认值
function Default(value: any) {
    return function (target: any, key: string) {
        target[key] = value
    }
}
class Config { @Default(8080) port: number }
```

---

**基本写法：只读属性装饰器**
`function <ReadOnly>(<target>, <key>)`
```typescript
// 让属性只读
function ReadOnly(target: any, key: string) {
    Object.defineProperty(target, key, { writable: false })
}
```

---

## 装饰器工厂

**基本写法：装饰器工厂**
`function <装饰器>(<配置>): <装饰器>`
```typescript
// 工厂返回实际装饰器
function Log(prefix: string) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        desc.value = function (...args: any[]) {
            console.log(`${prefix}: ${key}`)
            return orig.apply(this, args)
        }
    }
}
class S { @Log("APP") run() {} }
```

---

**基本写法：多装饰器组合**
`@<A> @<B> @<C> <声明>`
```typescript
// 多装饰器从下往上执行
function A(target: any, key: string) { console.log("A") }
function B(target: any, key: string) { console.log("B") }
class S { @A @B method() {} }  // B A
```

---

## 元数据反射

**基本写法：emitDecoratorMetadata**
`import "reflect-metadata"`
```typescript
// 需要 tsconfig 开启 emitDecoratorMetadata
import "reflect-metadata"
function Meta(target: any, key: string) {
    const type = Reflect.getMetadata("design:type", target, key)
    console.log(type)  // String
}
class S { @Meta name: string = "" }
```

---

**基本写法：自定义元数据**
`Reflect.defineMetadata(<键>, <值>, <目标>)`
```typescript
// 存储自定义元数据
function Role(role: string) {
    return function (target: any, key: string) {
        Reflect.defineMetadata("role", role, target, key)
    }
}
```

---

**基本写法：读取元数据**
`Reflect.getMetadata(<键>, <目标>)`
```typescript
// 读取存储的元数据
function getRole(target: any, key: string) {
    return Reflect.getMetadata("role", target, key)
}
```

---

## 参数装饰器实战

**基本写法：必填参数装饰器**
`function <Required>(<target>, <key>, <index>)`
```typescript
// 标记参数必填
const required: Set<number> = new Set()
function Required(target: any, key: string, index: number) {
    required.add(index)
}
class S { greet(@Required name: string) {} }
```

---

**基本写法：参数注入**
`function <Inject>(<token>): <参数装饰器>`
```typescript
// 依赖注入标记
function Inject(token: string) {
    return function (target: any, key: string, index: number) {
        Reflect.defineMetadata("inject", token, target, key)
    }
}
class S { constructor(@Inject("DB") db: any) {} }
```

---

## 访问器装饰器

**基本写法：getter setter 装饰器**
`function <装饰器>(<target>, <key>, <descriptor>)`
```typescript
// 装饰访问器属性
function Log(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.get
    desc.get = function () {
        const v = orig?.call(this)
        console.log(`get ${key}`)
        return v
    }
}
class S { private _v = 1; @Log get v() { return this._v } }
```

---

## 5.0 新版装饰器

**基本写法：Stage 3 装饰器**
`function <装饰器>(<target>, <context>) { }`
```typescript
// TS 5.0 标准 TC39 装饰器
function log(target: any, context: ClassMethodDecoratorContext) {
    return function (this: any, ...args: any[]) {
        console.log(`call ${String(context.name)}`)
        return target.apply(this, args)
    }
}
class S { @log run() {} }
```

---

**基本写法：新版类装饰器**
`function <装饰器>(<target>, <context>): <新类>`
```typescript
// TC39 类装饰器
function tag(target: any, context: ClassDecoratorContext) {
    return class extends target {
        tag = context.name
    }
}
@tag class S {}
```

---

**基本写法：新版自动访问器**
`accessor <字段>`
```typescript
// TS 5.0 自动访问器
class S {
    accessor count = 0  // 自动生成 getter setter
}
```

---

## 实用模式

**基本写法：缓存装饰器**
`function <Memoize>(<target>, <key>, <descriptor>)`
```typescript
// 缓存方法结果
function Memoize(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    const cache = new Map()
    desc.value = function (...args: any[]) {
        const k = JSON.stringify(args)
        if (!cache.has(k)) cache.set(k, orig.apply(this, args))
        return cache.get(k)
    }
}
```

---

**基本写法：防抖装饰器**
`function <Debounce>(<等待>): <方法装饰器>`
```typescript
// 方法防抖
function Debounce(wait: number) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        let timer: any
        desc.value = function (...args: any[]) {
            clearTimeout(timer)
            timer = setTimeout(() => orig.apply(this, args), wait)
        }
    }
}
```

---

**基本写法：节流装饰器**
`function <Throttle>(<等待>): <方法装饰器>`
```typescript
// 方法节流
function Throttle(wait: number) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        let last = 0
        desc.value = function (...args: any[]) {
            const now = Date.now()
            if (now - last >= wait) { last = now; return orig.apply(this, args) }
        }
    }
}
```

---

**基本写法：权限校验装饰器**
`function <Auth>(<角色>): <方法装饰器>`
```typescript
// 校验调用权限
function Auth(role: string) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        desc.value = function (...args: any[]) {
            if (currentUser.role !== role) throw new Error("forbidden")
            return orig.apply(this, args)
        }
    }
}
class Admin { @Auth("admin") delete() {} }
```

---

**基本写法：重试装饰器**
`function <Retry>(<次数>): <方法装饰器>`
```typescript
// 异步方法重试
function Retry(times: number) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        desc.value = async function (...args: any[]) {
            for (let i = 0; i < times; i++) {
                try { return await orig.apply(this, args) }
                catch (e) { if (i === times - 1) throw e }
            }
        }
    }
}
```

---

## tsconfig 配置

**基本写法：开启装饰器**
`"experimentalDecorators": true`
```json
// tsconfig.json 开启装饰器支持
{
    "compilerOptions": {
        "experimentalDecorators": true,
        "emitDecoratorMetadata": true
    }
}
```



<!-- ============ 文档分隔线：009-typescript/019-ModuleDeclaration.md ============ -->

# TypeScript 模块声明

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 模块基础

**基本写法：导出**
`export <声明>`
```typescript
// 导出变量函数类型等
export const name = "Tom"
export function greet() {}
export type User = { name: string }
```

---

**基本写法：默认导出**
`export default <声明>`
```typescript
// 每个模块只能有一个默认导出
export default class User {}
```

---

**基本写法：命名导入**
`import { <名称>, <名称> } from "<模块>"`
```typescript
// 按名导入多个
import { name, greet } from "./user"
```

---

**基本写法：默认导入**
`import <名称> from "<模块>"`
```typescript
// 导入默认导出
import User from "./User"
```

---

**基本写法：别名导入**
`import { <名称> as <别名> } from "<模块>"`
```typescript
// 重命名导入避免冲突
import { name as userName } from "./user"
```

---

**基本写法：命名空间导入**
`import * as <名称> from "<模块>"`
```typescript
// 整体导入为一个对象
import * as utils from "./utils"
utils.format()
```

---

## 模块声明

**基本写法：声明模块**
`declare module "<模块名>"`
```typescript
// 为 JS 模块补类型声明
declare module "my-lib" {
    export function greet(name: string): string
    export const version: string
}
```

---

**基本写法：通配符模块声明**
`declare module "*<后缀>"`
```typescript
// 处理非 JS 资源导入
declare module "*.css" {
    const content: string
    export default content
}
declare module "*.png" {
    const src: string
    export default src
}
```

---

**基本写法：声明全局变量**
`declare const <变量>: <类型>`
```typescript
// 声明全局变量类型
declare const VERSION: string
declare const __DEV__: boolean
```

---

**基本写法：声明全局函数**
`declare function <名称>(<参数>): <返回类型>`
```typescript
// 声明全局函数
declare function $(selector: string): HTMLElement
```

---

## namespace 命名空间

**基本写法：定义命名空间**
`namespace <名称> { }`
```typescript
// 命名空间组织相关类型
namespace App {
    export function init() {}
    export const version = "1.0"
}
App.init()
```

---

**基本写法：嵌套命名空间**
`namespace <外层>.<内层> { }`
```typescript
// 命名空间嵌套
namespace App.Config {
    export const port = 3000
}
App.Config.port
```

---

**基本写法：命名空间与模块结合**
`export namespace <名称> { }`
```typescript
// 模块中导出命名空间
export namespace Utils {
    export function format(s: string) { return s.trim() }
}
```

---

## 声明合并

**基本写法：同名接口合并**
`interface <名称> { }`
```typescript
// 同名接口自动合并
interface User { name: string }
interface User { age: number }
const u: User = { name: "T", age: 18 }
```

---

**基本写法：同名命名空间合并**
`namespace <名称> { }`
```typescript
// 命名空间自动合并
namespace App { export const a = 1 }
namespace App { export const b = 2 }
App.a; App.b
```

---

**基本写法：函数与接口合并**
`function <函数>(); interface <函数> { }`
```typescript
// 函数声明可与接口合并添加属性
function greet(name: string): string
namespace greet {
    export const version = "1.0"
}
greet.version
```

---

## 全局声明

**基本写法：global 声明**
`declare global { }`
```typescript
// 在模块中扩展全局
declare global {
    interface Window { myApp: any }
}
window.myApp = {}
```

---

**基本写法：扩展全局接口**
`declare global { interface <名称> { } }`
```typescript
// 扩展内置全局接口
declare global {
    interface Array<T> { last(): T | undefined }
}
Array.prototype.last = function () { return this[this.length - 1] }
```

---

## 模块扩展

**基本写法：扩展模块声明**
`declare module "<模块>" { interface <名称> { } }`
```typescript
// 扩展已存在模块的类型
declare module "express" {
    interface Request { user?: User }
}
```

---

**基本写法：扩展 Express 类型**
`declare module "express" { interface Request { } }`
```typescript
// 给 Express Request 添加属性
declare module "express-serve-static-core" {
    interface Request { userId: string }
}
```

---

## ambient 声明

**基本写法：声明文件**
`<文件>.d.ts`
```typescript
// 声明文件仅类型不产生代码
// types.d.ts
declare module "lib" {
    export function fn(): void
}
```

---

**基本写法：声明类型别名**
`declare type <名称> = <类型>`
```typescript
// 全局类型别名声明
declare type ID = string | number
```

---

**基本写法：声明枚举**
`declare enum <名称> { }`
```typescript
// 声明外部枚举
declare enum Color { Red, Green, Blue }
```

---

## 三斜线指令

**基本写法：引用类型声明**
`/// <reference types="<包>" />`
```typescript
// 引入 @types 包
/// <reference types="node" />
```

---

**基本写法：引用路径**
`/// <reference path="<文件>" />`
```typescript
// 引入指定声明文件
/// <reference path="./types.d.ts" />
```

---

**基本写法：引用库**
`/// <reference lib="<库>" />`
```typescript
// 引入内置 lib
/// <reference lib="es2017" />
```

---

## 类型与值导入

**基本写法：import type**
`import type { <类型> } from "<模块>"`
```typescript
// 仅导入类型编译时移除
import type { User } from "./types"
```

---

**基本写法：内联 type 限定**
`import { type <类型>, <值> } from "<模块>"`
```typescript
// 混合导入时标记类型
import { type User, getUser } from "./user"
```

---

**基本写法：export type**
`export type { <类型> }`
```typescript
// 仅导出类型
export type { User } from "./types"
```

---

## CommonJS 互操作

**基本写法：导入 CommonJS 模块**
`import <名称> = require("<模块>")`
```typescript
// CommonJS 模块导入
import fs = require("fs")
```

---

**基本写法：导出 CommonJS**
`export = <对象>`
```typescript
// CommonJS 风格导出
class User {}
export = User
```

---

**基本写法：esModuleInterop**
`import <名称> from "<CommonJS模块>"`
```typescript
// 开启 esModuleInterop 后默认导入
import fs from "fs"
```

---

## 动态导入

**基本写法：动态 import 类型**
`const <模块> = await import("<模块>")`
```typescript
// 动态导入类型为 Promise<typeof import>
const mod = await import("./user")
mod.greet()
```

---

**基本写法：动态导入类型**
`type <类型> = typeof import("<模块>")`
```typescript
// 推导模块类型
type UserModule = typeof import("./user")
```

---

## 实用模式

**基本写法：barrel 导出**
`export * from "<模块>"`
```typescript
// index.ts 汇总导出
export * from "./user"
export * from "./post"
export * from "./comment"
```

---

**基本写法：选择性 barrel**
`export { <名称>, <名称> } from "<模块>"`
```typescript
// 选择性重新导出
export { User, getUser } from "./user"
export type { UserProps } from "./user"
```

---

**基本写法：声明 JSON 模块**
`declare module "*.json"`
```typescript
// 允许 import JSON
declare module "*.json" {
    const value: any
    export default value
}
```

---

**基本写法：环境变量类型**
`interface ImportMetaEnv { }`
```typescript
// Vite 环境变量类型
interface ImportMetaEnv {
    readonly VITE_API: string
}
interface ImportMeta {
    readonly env: ImportMetaEnv
}
```

---

## 模块解析

**基本写法：node 解析策略**
`"moduleResolution": "node"`
```typescript
// tsconfig 配置 node 经典解析
// 查找 node_modules 文件扩展名
```

---

**基本写法：bundler 解析策略**
`"moduleResolution": "bundler"`
```typescript
// TS 5.0+ 适配打包工具的解析
// 支持 package.json exports 字段
```

---

**基本写法：paths 路径映射**
`"paths": { "<别名>": ["<路径>"] }`
```typescript
// tsconfig 配置路径别名
{
    "compilerOptions": {
        "baseUrl": ".",
        "paths": { "@/*": ["src/*"] }
    }
}
```

---

## 注意事项

**基本写法：模块与脚本区分**
`export <声明>` 或 `import <名称>`
```typescript
// 含 import export 的是模块
// 否则是脚本全局可见
```

---

**基本写法：isolatedModules**
`"isolatedModules": true`
```typescript
// 单文件转译模式约束
// 要求类型导入显式标注
export type { User }
```



<!-- ============ 文档分隔线：009-typescript/020-TsConfigReference.md ============ -->

# TypeScript tsconfig 配置速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 配置文件基础

**基本写法：tsconfig.json 结构**
`{ "compilerOptions": { }, "include": [], "exclude": [] }`
```json
// 项目根目录的 TS 配置文件
{
    "compilerOptions": {
        "target": "ES2022",
        "module": "ESNext"
    },
    "include": ["src"],
    "exclude": ["node_modules"]
}
```

---

**基本写法：extends 继承**
`{ "extends": "<基础配置>" }`
```json
// 继承基础配置再覆盖
{
    "extends": "./tsconfig.base.json",
    "compilerOptions": { "strict": true }
}
```

---

## target 编译目标

**基本写法：target 选项**
`"target": "ES2022"`
```json
// 指定编译目标 JS 版本
// ES3 ES5 ES6 ES2015-ES2023 ESNext
{
    "compilerOptions": { "target": "ES2022" }
}
```

---

**基本写法：lib 指定类型库**
`"lib": ["ES2022", "DOM"]`
```json
// 指定可用的类型库
{
    "compilerOptions": {
        "lib": ["ES2022", "DOM", "DOM.Iterable"]
    }
}
```

---

## module 模块系统

**基本写法：module 选项**
`"module": "ESNext"`
```json
// 指定模块系统
// CommonJS ESNext AMD UMD Node16
{
    "compilerOptions": { "module": "ESNext" }
}
```

---

**基本写法：moduleResolution 解析策略**
`"moduleResolution": "bundler"`
```json
// 模块解析策略
// node classic bundler node16 nodenext
{
    "compilerOptions": { "moduleResolution": "bundler" }
}
```

---

**基本写法：Node 项目配置**
`"module": "Node16"`
```json
// Node 项目推荐配置
{
    "compilerOptions": {
        "module": "Node16",
        "moduleResolution": "Node16"
    }
}
```

---

## 严格模式

**基本写法：strict 总开关**
`"strict": true`
```json
// 开启所有严格检查
{
    "compilerOptions": { "strict": true }
}
```

---

**基本写法：noImplicitAny**
`"noImplicitAny": true`
```json
// 禁止隐式 any
function fn(x) {}  // 报错
```

---

**基本写法：strictNullChecks**
`"strictNullChecks": true`
```json
// 严格区分 null undefined
let s: string = null  // 报错
```

---

**基本写法：strictFunctionTypes**
`"strictFunctionTypes": true`
```json
// 严格函数类型检查
```

---

**基本写法：noUnusedLocals**
`"noUnusedLocals": true`
```json
// 未使用的局部变量报错
const a = 1  // 报错如果未使用
```

---

**基本写法：noUnusedParameters**
`"noUnusedParameters": true`
```json
// 未使用的参数报错
function fn(a, b) { return a }  // b 报错
```

---

**基本写法：noImplicitReturns**
`"noImplicitReturns": true`
```json
// 函数所有分支必须返回
function fn(x: boolean) {
    if (x) return 1  // 报错缺少 else 分支
}
```

---

**基本写法：noFallthroughCasesInSwitch**
`"noFallthroughCasesInSwitch": true`
```json
// switch case 不允许穿透
switch (x) {
    case 1: doA();  // 报错需 break
    case 2: doB();
}
```

---

## 路径映射

**基本写法：baseUrl 与 paths**
`"paths": { "<别名>": ["<路径>"] }`
```json
// 配置路径别名
{
    "compilerOptions": {
        "baseUrl": ".",
        "paths": {
            "@/*": ["src/*"],
            "@components/*": ["src/components/*"]
        }
    }
}
```

---

**基本写法：rootDirs 多根目录**
`"rootDirs": ["<目录1>", "<目录2>"]`
```json
// 虚拟目录组合
{
    "compilerOptions": {
        "rootDirs": ["src", "generated"]
    }
}
```

---

**基本写法：rootDir 与 outDir**
`"rootDir": "src"` | `"outDir": "dist"`
```json
// 指定源码根与输出目录
{
    "compilerOptions": {
        "rootDir": "src",
        "outDir": "dist"
    }
}
```

---

## 类型解析

**基本写法：typeRoots**
`"typeRoots": ["<路径>"]`
```json
// 指定 @types 目录
{
    "compilerOptions": {
        "typeRoots": ["./node_modules/@types", "./types"]
    }
}
```

---

**基本写法：types 显式指定**
`"types": ["node", "jest"]`
```json
// 仅包含指定类型包
{
    "compilerOptions": { "types": ["node", "jest"] }
}
```

---

**基本写法：skipLibCheck**
`"skipLibCheck": true`
```json
// 跳过声明文件检查提升速度
{
    "compilerOptions": { "skipLibCheck": true }
}
```

---

## 输出格式

**基本写法：sourceMap**
`"sourceMap": true`
```json
// 生成 source map 文件
{
    "compilerOptions": { "sourceMap": true }
}
```

---

**基本写法：declaration**
`"declaration": true`
```json
// 生成 .d.ts 声明文件
{
    "compilerOptions": { "declaration": true }
}
```

---

**基本写法：declarationMap**
`"declarationMap": true`
```json
// 生成声明文件的 source map
{
    "compilerOptions": { "declarationMap": true }
}
```

---

**基本写法：removeComments**
`"removeComments": true`
```json
// 输出移除注释
{
    "compilerOptions": { "removeComments": true }
}
```

---

**基本写法：noEmit**
`"noEmit": true`
```json
// 仅类型检查不输出文件
{
    "compilerOptions": { "noEmit": true }
}
```

---

## JSX 配置

**基本写法：jsx 选项**
`"jsx": "react-jsx"`
```json
// JSX 处理模式
// preserve react react-native react-jsx
{
    "compilerOptions": { "jsx": "react-jsx" }
}
```

---

**基本写法：jsxImportSource**
`"jsxImportSource": "<包>"`
```json
// 指定 JSX 工厂导入源
{
    "compilerOptions": {
        "jsx": "react-jsx",
        "jsxImportSource": "preact"
    }
}
```

---

## 装饰器配置

**基本写法：开启装饰器**
`"experimentalDecorators": true`
```json
// 启用实验性装饰器
{
    "compilerOptions": {
        "experimentalDecorators": true,
        "emitDecoratorMetadata": true
    }
}
```

---

## 互操作

**基本写法：esModuleInterop**
`"esModuleInterop": true`
```json
// 允许默认导入 CommonJS 模块
import fs from "fs"  // 需要 esModuleInterop
```

---

**基本写法：allowSyntheticDefaultImports**
`"allowSyntheticDefaultImports": true`
```json
// 允许从无默认导出的模块默认导入仅类型
```

---

**基本写法：allowJs**
`"allowJs": true`
```json
// 允许编译 JS 文件
{
    "compilerOptions": { "allowJs": true }
}
```

---

**基本写法：checkJs**
`"checkJs": true`
```json
// 检查 JS 文件类型错误
{
    "compilerOptions": { "checkJs": true }
}
```

---

## 项目引用

**基本写法：references**
`"references": [{ "path": "<项目>" }]`
```json
// 项目引用用于 monorepo
{
    "references": [
        { "path": "./packages/shared" },
        { "path": "./packages/app" }
    ]
}
```

---

**基本写法：composite**
`"composite": true`
```json
// 项目引用必须开启
{
    "compilerOptions": {
        "composite": true,
        "declaration": true
    }
}
```

---

**基本写法：incremental**
`"incremental": true`
```json
// 增量编译提升速度
{
    "compilerOptions": {
        "incremental": true,
        "tsBuildInfoFile": ".tsbuildinfo"
    }
}
```

---

## 监听与构建

**基本写法：tsc --watch**
`tsc --watch`
```bash
# 监听文件变化自动编译
tsc -w
```

---

**基本写法：tsc --build**
`tsc --build`
```bash
# 构建项目引用
tsc -b
```

---

**基本写法：tsc --noEmit**
`tsc --noEmit`
```bash
# 仅类型检查不输出
tsc --noEmit
```

---

## 现代项目配置

**基本写法：Vite React 模板**
`{ "compilerOptions": { } }`
```json
// Vite + React 项目推荐配置
{
    "compilerOptions": {
        "target": "ES2020",
        "useDefineForClassFields": true,
        "lib": ["ES2020", "DOM", "DOM.Iterable"],
        "module": "ESNext",
        "moduleResolution": "bundler",
        "jsx": "react-jsx",
        "strict": true,
        "noEmit": true,
        "isolatedModules": true,
        "skipLibCheck": true
    },
    "include": ["src"]
}
```

---

**基本写法：Node 项目配置**
`{ "compilerOptions": { } }`
```json
// Node.js 后端项目推荐配置
{
    "compilerOptions": {
        "target": "ES2022",
        "module": "Node16",
        "moduleResolution": "Node16",
        "outDir": "dist",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "types": ["node"]
    },
    "include": ["src"]
}
```

---

**基本写法：库开发配置**
`{ "compilerOptions": { } }`
```json
// npm 包开发推荐配置
{
    "compilerOptions": {
        "target": "ES2020",
        "module": "ESNext",
        "moduleResolution": "bundler",
        "declaration": true,
        "declarationMap": true,
        "sourceMap": true,
        "outDir": "dist",
        "strict": true,
        "skipLibCheck": true
    },
    "include": ["src"],
    "exclude": ["node_modules", "dist"]
}
```

---

## 实用配置

**基本写法：resolveJsonModule**
`"resolveJsonModule": true`
```json
// 允许导入 JSON 文件
import pkg from "./package.json"
```

---

**基本写法：isolatedModules**
`"isolatedModules": true`
```json
// 单文件转译约束
// 类型导入必须显式 export type
```

---

**基本写法：useDefineForClassFields**
`"useDefineForClassFields": true`
```json
// 使用 ES 标准 class 字段语义
class A { x = 1 }  // 使用 defineProperty
```

---

**基本写法：forceConsistentCasingInFileNames**
`"forceConsistentCasingInFileNames": true`
```json
// 强制文件名大小写一致
```

---

## 编译诊断

**基本写法：diagnostics**
`tsc --diagnostics`
```bash
# 输出编译诊断信息
tsc --diagnostics --extendedDiagnostics
```

---

**基本写法：listFiles**
`tsc --listFiles`
```bash
# 列出所有编译文件
tsc --listFiles
```

---

**基本写法：explainFiles**
`tsc --explainFiles`
```bash
# 解释文件为何被包含
tsc --explainFiles
```

---

## 常用脚本

**基本写法：package.json scripts**
`{ "scripts": { } }`
```json
// package.json 常用 TS 脚本
{
    "scripts": {
        "build": "tsc",
        "dev": "tsc --watch",
        "typecheck": "tsc --noEmit",
        "clean": "rm -rf dist"
    }
}
```



<!-- ============ 文档分隔线：009-typescript/021-UnionIntersectionType.md ============ -->

# TypeScript 联合类型与交叉类型语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 联合类型基础

**基本写法：联合类型**
`type <名> = <A> | <B>`
```typescript
// 变量可取多种类型之一
type ID = string | number;
function find(id: ID) {}
find(1);
find("a");
```

---

**基本写法：字面量联合**
`type <名> = "<值1>" | "<值2>"`
```typescript
// 限定具体取值
type Status = "idle" | "loading" | "success" | "error";
let s: Status = "loading";
```

---

## 联合类型 narrowing

**基本写法：typeof 收窄**
`typeof <值> === "<类型>"`
```typescript
// 联合类型按类型分支
function pad(v: string | number) {
  if (typeof v === "number") return " ".repeat(v);
  return v;
}
```

---

**基本写法：in 操作符收窄**
`"<键>" in <值>`
```typescript
// 按属性是否存在分支
type Cat = { meow: () => void };
type Dog = { bark: () => void };
function speak(a: Cat | Dog) {
  if ("meow" in a) a.meow();
  else a.bark();
}
```

---

**基本写法：判别联合**
`{ kind: "<字面量>", ... }`
```typescript
// 用公共字面量字段区分
type Shape =
  | { kind: "circle"; r: number }
  | { kind: "square"; s: number };
function area(x: Shape) {
  switch (x.kind) {
    case "circle": return Math.PI * x.r ** 2;
    case "square": return x.s ** 2;
  }
}
```

---

## 交叉类型

**基本写法：交叉类型合并**
`type <名> = <A> & <B>`
```typescript
// 同时具备多个类型全部属性
type WithId = { id: number };
type WithName = { name: string };
type User = WithId & WithName;
const u: User = { id: 1, name: "Tom" };
```

---

**基本写法：与接口交叉**
`<A> & <B>`
```typescript
// 接口可参与交叉
interface A { a: string }
type AB = A & { b: number };
```

---

## 同名属性处理

**基本写法：同名字段冲突**
`{ a: <T1> } & { a: <T2> }`
```typescript
// 同名字段类型合并为联合
type T = { a: string } & { a: number };
// 等价 a: string & number（即 never，几乎不可赋值）
```

---

**基本写法：字面量同名字段**
`{ kind: "x" } & { kind: "y" }`
```typescript
// 不冲突字面量合并为联合
type K = { kind: "a" } & { value: number };
// kind 为 "a"，value 为 number
```

---

## 可辨识联合模式

**基本写法：完整判别联合**
`type <名> = <成员1> | <成员2> | ...`
```typescript
// 标准判别联合 + 穷尽检查
type Event =
  | { type: "click"; x: number; y: number }
  | { type: "scroll"; top: number };
function handle(e: Event) {
  switch (e.type) {
    case "click": return e.x + e.y;
    case "scroll": return e.top;
    default:
      const _: never = e; // 穷尽检查
      return _;
  }
}
```

---

## 联合分布

**基本写法：联合在条件类型中分布**
`<T> extends <U> ? <X> : <Y>`
```typescript
// 裸类型参数自动分发到联合成员
type ToArray<T> = T extends unknown ? T[] : never;
type R = ToArray<string | number>; // string[] | number[]
```

---

**基本写法：阻止分布**
`[<T>] extends [<U>] ? <X> : <Y>`
```typescript
// 用元组包裹阻止分发
type ToArrayAll<T> = [T] extends [unknown] ? T[] : never;
type R = ToArrayAll<string | number>; // (string | number)[]
```

---

## 工具：联合转交叉

**基本写法：联合转交叉**
`UnionToIntersection<<U>>`
```typescript
// 利用函数参数逆变特性
type UnionToIntersection<U> =
  (U extends unknown ? (x: U) => void : never) extends (x: infer I) => void
    ? I : never;
type R = UnionToIntersection<{ a: 1 } | { b: 2 }>; // { a: 1 } & { b: 2 }
```

---

## 联合成员提取

**基本写法：Extract 提取**
`type <R> = Extract<<T>, <U>>`
```typescript
// 从联合中提取符合 U 的成员
type T = "a" | "b" | "c";
type AB = Extract<T, "a" | "b">; // "a" | "b"
```

---

**基本写法：Exclude 排除**
`type <R> = Exclude<<T>, <U>>`
```typescript
// 从联合中排除符合 U 的成员
type T = "a" | "b" | "c";
type C = Exclude<T, "a" | "b">; // "c"
```

---

**基本写法：NonNullable 排空**
`type <R> = NonNullable<<T>>`
```typescript
// 排除 null 与 undefined
type T = string | null | undefined;
type S = NonNullable<T>; // string
```

---



<!-- ============ 文档分隔线：009-typescript/022-TscCompilerCommands.md ============ -->

# TypeScript tsc 编译命令速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础编译

**基本写法：编译文件**
`tsc <文件.ts> [选项]`
```bash
# 编译为同名 js
tsc main.ts
tsc src/*.ts
```

---

**基本写法：编译并输出**
`tsc <文件> --outFile <输出>`
```bash
# 合并输出单文件
tsc a.ts b.ts --outFile bundle.js
# 指定输出目录
tsc src/*.ts --outDir dist
```

---

## 项目与配置

**基本写法：按 tsconfig 编译**
`tsc -p <路径>`
```bash
# 使用指定配置文件
tsc -p tsconfig.json
tsc -p ./packages/core
```

---

**基本写法：生成配置文件**
`tsc --init`
```bash
# 生成默认 tsconfig.json
tsc --init
# 仅生成目标为特定版本
tsc --init --target ES2022 --module NodeNext
```

---

## 类型检查模式

**基本写法：只检查不输出**
`tsc --noEmit`
```bash
# CI 常用，仅做类型检查
tsc --noEmit
tsc -p . --noEmit
```

---

**基本写法：监听变更**
`tsc -w`
```bash
# 增量监听重编译
tsc -w
tsc -p . --watch --preserveWatchOutput
```

---

## 模块与目标

**基本写法：指定模块系统**
`tsc --module <值>`
```bash
# ES 模块 / CommonJS / NodeNext 等
tsc --module ES2022
tsc --module NodeNext
tsc --module CommonJS
```

---

**基本写法：指定目标版本**
`tsc --target <值>`
```bash
# 编译降级目标
tsc --target ES2020
tsc --target ESNext
```

---

**基本写法：模块解析策略**
`tsc --moduleResolution <值>`
```bash
# Node10 / NodeNext / Bundler / Classic
tsc --moduleResolution Bundler
tsc --moduleResolution NodeNext
```

---

## 严格模式

**基本写法：开启全部严格**
`tsc --strict`
```bash
# 等价于一组严格选项
tsc --strict
```

---

**基本写法：单项严格选项**
`tsc --<选项>`
```bash
# 各项严格检查
tsc --noImplicitAny
tsc --strictNullChecks
tsc --strictFunctionTypes
tsc --strictBindCallApply
tsc --strictPropertyInitialization
tsc --noImplicitThis
tsc --alwaysStrict
tsc --useUnknownInCatchVariables
```

---

## 路径与导出

**基本写法：基础路径映射**
`tsconfig: "baseUrl": ".", "paths": { "@/*": ["src/*"] }`
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@core/*": ["packages/core/*"]
    }
  }
}
```

---

**基本写法：声明文件输出**
`tsc --declaration`
```bash
# 生成 .d.ts 类型声明
tsc --declaration
tsc --declaration --emitDeclarationOnly
tsc --declarationDir types
```

---

## 常用输出控制

**基本写法：sourceMap 与导出**
`tsc --<选项>`
```bash
# 生成 source map
tsc --sourceMap
# 仅生成类型不生成 js
tsc --emitDeclarationOnly
# 不生成注释
tsc --removeComments
# 保留 import 断言
tsc --verbatimModuleSyntax
```

---

## JSX 与库

**基本写法：JSX 支持**
`tsc --jsx <值>`
```bash
# react / react-jsx / preserve / react-native
tsc --jsx react-jsx
```

---

**基本写法：引入 lib**
`tsconfig: "lib": ["<库>"]`
```json
{
  "compilerOptions": {
    "lib": ["ES2022", "DOM", "DOM.Iterable"]
  }
}
```

---

## 增量构建

**基本写法：增量编译**
`tsc --incremental`
```bash
# 缓存到 .tsbuildinfo 加速
tsc --incremental
tsc --incremental --tsBuildInfoFile ./.cache/info
```

---

## 命令行诊断

**基本写法：显示版本与原因**
`tsc --version` | `tsc --explainFiles`
```bash
tsc -v                       # 版本
tsc --listFiles              # 列出所有参与编译文件
tsc --explainFiles           # 解释为何包含某文件
tsc --showConfig             # 展开继承后的最终配置
```

---

## 监听与项目引用

**基本写法：项目引用**
`tsconfig: "references": [{ "path": "./shared" }]`
```json
{
  "references": [{ "path": "./packages/shared" }]
}
```

---

**基本写法：构建引用项目**
`tsc -b [--dry]`
```bash
# 增量构建依赖项目
tsc -b
tsc -b --dry       # 模拟不写盘
tsc -b --clean     # 清理构建产物
tsc -b --force     # 强制全量构建
```

---



<!-- ============ 文档分隔线：009-typescript/023-RecursiveTypeInfer.md ============ -->

# TypeScript 递归类型与 infer 语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## infer 基础

**基本写法：infer 提取类型**
`<T> extends <模式> ? infer <X> : <never>`
```typescript
// 从函数返回类型提取
type Return<T> = T extends (...args: never[]) => infer R ? R : never;
type R = Return<() => string>; // string
```

---

**基本写法：提取函数参数**
`infer <Args>`
```typescript
// 提取参数元组
type Params<T> = T extends (...args: infer P) => unknown ? P : never;
type P = Params<(a: number, b: string) => void>; // [number, string]
```

---

**基本写法：提取数组元素**
`infer <E>`
```typescript
// 提取元组/数组元素类型
type Item<T> = T extends (infer E)[] ? E : never;
type A = Item<string[]>;       // string
type B = Item<[1, 2, 3]>;      // 1 | 2 | 3
```

---

## 多 infer 与约束

**基本写法：多个 infer**
`<T> extends <模式1> extends <模式2> ? infer <X> : never`
```typescript
// 嵌套条件约束
type First<T> = T extends [infer F, ...unknown[]] ? F : never;
type F = First<[1, 2, 3]>; // 1
```

---

**基本写法：infer 约束（TS 4.7+）**
`infer <X> extends <约束>`
```typescript
// 限定推断类型范围
type FirstString<T> =
  T extends [infer F extends string, ...unknown[]] ? F : never;
type S = FirstString<["a", 2]>; // "a"
```

---

## 递归类型基础

**基本写法：自引用递归**
`type <名> = <终止> | { <字段>: <名> }`
```typescript
// 递归定义树形结构
type Tree = number | { children: Tree[] };
const t: Tree = { children: [1, { children: [2] }] };
```

---

**基本写法：深度只读**
`type <名> = <T> extends object ? { readonly [K in keyof <T>]: <名> } : <T>`
```typescript
// 递归遍历所有层级
type DeepReadonly<T> =
  T extends object ? { readonly [K in keyof T]: DeepReadonly<T[K]> } : T;
type R = DeepReadonly<{ a: { b: 1 } }>; // { readonly a: { readonly b: 1 } }
```

---

## 元组递归操作

**基本写法：反转元组**
`<T> extends [infer <H>, ...infer <R>] ? <递归> : []`
```typescript
// 递归反转元组类型
type Reverse<T extends unknown[]> =
  T extends [infer H, ...infer R] ? [...Reverse<R>, H] : [];
type R = Reverse<[1, 2, 3]>; // [3, 2, 1]
```

---

**基本写法：拼接元组**
`[...<A>, ...<B>]`
```typescript
// 利用展开拼接
type Concat<A extends unknown[], B extends unknown[]> = [...A, ...B];
type R = Concat<[1], [2, 3]>; // [1, 2, 3]
```

---

**基本写法：元组转对象**
`<T> extends [infer <K>, ...infer <R>] ? { ... } : {}`
```typescript
// 递归构造键值对象
type PairToObj<T extends unknown[]> =
  T extends [infer K extends string, infer V, ...infer R]
    ? { [P in K]: V } & PairToObj<R>
    : {};
```

---

## 字符串递归

**基本写法：字符串拆分**
`<S> extends `${infer <Head>}${infer <Rest>}``
```typescript
// 逐字符递归
type Split<S extends string> =
  S extends `${infer H}${infer R}` ? [H, ...Split<R>] : [];
type R = Split<"abc">; // ["a", "b", "c"]
```

---

**基本写法：联合字符**
`type <R> = <递归>`
```typescript
// 字符串转字符联合
type Chars<S extends string> =
  S extends `${infer H}${infer R}` ? H | Chars<R> : never;
type R = Chars<"abc">; // "a" | "b" | "c"
```

---

## 递归深度限制

**基本写法：递归层级计数**
`<T, N extends number>`
```typescript
// 用元组长度计数器限制递归深度，避免无限递归
type Depth<T extends unknown[]> = T["length"];
type Repeat<S extends string, N extends number, A extends string[] = []> =
  A["length"] extends N ? "" : `${S}${Repeat<S, N, [S, ...A]>}`;
type R = Repeat<"ab", 3>; // "ababab"
```

---

## infer 在 Promise

**基本写法：递归解包 Promise**
`<T> extends Promise<infer <U>> ? <递归> : <T>`
```typescript
// 提取深层 Promise 值类型
type Unwrap<T> = T extends Promise<infer U> ? Unwrap<U> : T;
type R = Unwrap<Promise<Promise<number>>>; // number
```

---

## 递归实例：DeepPartial

**基本写法：深度可选**
`type DeepPartial<<T>> = ...`
```typescript
// 所有层级属性可选
type DeepPartial<T> =
  T extends object ? { [K in keyof T]?: DeepPartial<T[K]> } : T;
type R = DeepPartial<{ a: { b: number } }>; // { a?: { b?: number } }
```

---

## 递归实例：Paths

**基本写法：对象路径联合**
`<T> extends object ? ...`
```typescript
// 生成对象所有路径字符串联合
type Paths<T, P extends string = ""> =
  T extends object
    ? { [K in keyof T & string]:
        Paths<T[K], `${P}${P extends "" ? "" : "."}${K}`> }[keyof T & string] | P
    : P;
type R = Paths<{ a: { b: number } }>; // "a" | "a.b"
```

---

## 尾递归优化

**基本写法：尾递归形式**
`<递归> extends <终止> ? <结果> : <递归(缩小)>`
```typescript
// TS 4.5+ 对尾递归类型优化，避免栈溢出
// 写法：递归调用作为最后操作且不包裹展开
type Join<S extends string[], D extends string> =
  S extends [] ? ""
  : S extends [infer H extends string] ? H
  : S extends [infer H extends string, ...infer R extends string[]]
    ? `${H}${D}${Join<R, D>}` : never;
```

---



<!-- ============ 文档分隔线：009-typescript/024-TypeScript5NewFeatures.md ============ -->

# TypeScript 5.x 新特性语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 5.0 const 类型参数

**基本写法：const 泛型参数**
`function <名><const T extends <约束>>(<参数>: T)`
```typescript
// 推断字面量类型而非放宽
function pickFirst<const T>(arr: readonly T[]): T {
  return arr[0];
}
const r = pickFirst(["red", "green"]); // "red" | "green"
```

---

**基本写法：const 配合元组**
`<const T extends readonly string[]>`
```typescript
// 保留元组字面量
function define<const T extends readonly string[]>(routes: T): T {
  return routes;
}
const c = define(["/home", "/about"]); // readonly ["/home", "/about"]
```

---

## 5.0 satisfies 操作符

**基本写法：satisfies 校验不放宽**
`const <变量> = <值> satisfies <类型>`
```typescript
// 校验符合类型，保留具体字面量推断
const palette = {
  red: "#f00",
  green: [0, 255, 0],
} satisfies Record<string, string | number[]>;
palette.red;   // string（具体）
palette.green; // number[]
```

---

**基本写法：satisfies 与 as 区别**
`<值> satisfies <类型>`
```typescript
// as 断言可能撒谎，satisfies 强制校验
const m = { a: 1 } satisfies Record<"a", number>;
// const m = { a: 1 } satisfies Record<"a", string>; // 报错
```

---

## 5.0 新版装饰器

**基本写法：标准装饰器**
`@<装饰器> <类成员>`
```typescript
// 符合 TC39 Stage 3，无需 experimentalDecorators
function log(target: Function, ctx: ClassMethodDecoratorContext) {
  return function (this: unknown, ...args: unknown[]) {
    console.log(ctx.name, args);
    return target.apply(this, args);
  };
}
class S { @log greet() { return "hi"; } }
```

---

## 5.2 using 声明

**基本写法：同步资源管理**
`using <变量> = <带 Symbol.dispose>`
```typescript
// 离开作用域自动释放
function read() {
  using f = openFile("./a.txt");
  // 作用域结束调用 [Symbol.dispose]
}
```

---

**基本写法：异步资源管理**
`await using <变量> = <带 Symbol.asyncDispose>`
```typescript
// 异步自动清理
async function run() {
  await using conn = await db.connect();
  // 自动 await [Symbol.asyncDispose]
}
```

---

## 5.3 switch(true) 收窄

**基本写法：switch(true) 类型收窄**
`switch (true) { case <条件>: ... }`
```typescript
// 每个 case 体内自动收窄
function desc(v: unknown) {
  switch (true) {
    case typeof v === "string": return v.toUpperCase();
    case typeof v === "number": return v.toFixed(2);
    default: return "unknown";
  }
}
```

---

## 5.4 NoInfer 工具类型

**基本写法：阻止推断**
`NoInfer<<T>>`
```typescript
// 不从该位置推断 T，仅校验
function withDefault<T>(v: T | undefined, fb: NoInfer<T>): T {
  return v ?? fb;
}
const r = withDefault("hi", "x"); // T = string
// withDefault("hi", 42); // 报错：number 不能赋给 string
```

---

## 5.4 闭包保留收窄

**基本写法：闭包内保留 narrowing**
`const <fn> = () => <使用收窄变量>`
```typescript
// 5.4 修复闭包内类型丢失
function fn(v: string | null) {
  if (v === null) return;
  const cb = () => v.toUpperCase(); // v 已收窄为 string
  return cb();
}
```

---

## 5.5 推断类型谓词

**基本写法：自动推断 is**
`function <f>(<x>): <TypePredicate>`
```typescript
// 返回布尔值自动推断为类型谓词
const isString = (x: unknown) => typeof x === "string";
const arr = [1, "a"].filter(isString); // string[]
```

---

## 5.6 离散联合与迭代器

**基本写法：离散联合类型**
`type <名> = { ... } | { ... }`
```typescript
// 成员间无公共字段时更严格检查
type A = { kind: "a"; x: number };
type B = { kind: "b"; y: string };
type U = A | B;
```

---

**基本写法：Iterator Helpers 类型**
`<iterator>.map(<fn>).filter(<fn>)`
```typescript
// 内置 Iterator 类型支持链式
function* gen() { yield 1; yield 2; }
const r = gen().map(x => x * 2).filter(x => x > 2).toArray(); // [4]
```

---

## 5.9 import defer 与 node20

**基本写法：延迟导入**
`import defer * as <名> from "<模块>"`
```typescript
// 首次使用时才求值
import defer * as lib from "./heavy";
// 用到 lib 时才执行模块
export function use() { return lib.foo(); }
```

---

**基本写法：node20 模块解析**
`"moduleResolution": "node20"`
```json
{
  "compilerOptions": {
    "module": "node20",
    "moduleResolution": "node20"
  }
}
```

---

## 装饰器上下文

**基本写法：装饰器上下文对象**
`<ctx>: ClassMethodDecoratorContext`
```typescript
// 上下文提供 name/kind/addInitializer 等
function bound(target: Function, ctx: ClassMethodDecoratorContext) {
  ctx.addInitializer(function (this: unknown) {
    (this as Record<string, unknown>)[ctx.name as string] =
      target.bind(this);
  });
}
```

---

## satisfies + const 组合

**基本写法：校验且保留字面量**
`<值> satisfies <类型>` + `function f<const T>`
```typescript
// 配置对象校验且保留字面量联合
function config<const T extends Record<string, string>>(c: T): T { return c; }
const c = config({
  home: "/",
  api: "/api",
} satisfies Record<string, string>);
c.home; // "/" 字面量
```

---



<!-- ============ 文档分隔线：009-typescript/025-LiteralTypeConstAssertion.md ============ -->

# TypeScript 字面量类型与 const 断言语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 字符串字面量类型

**基本写法：字符串字面量**
`type <名> = "<值>"`
```typescript
// 限定具体字符串
type Direction = "left" | "right" | "up" | "down";
function move(d: Direction) {}
move("left");
```

---

## 数字字面量类型

**基本写法：数字字面量**
`type <名> = <数字>`
```typescript
// 限定具体数字
type Dice = 1 | 2 | 3 | 4 | 5 | 6;
type Byte = 0 | 1;
```

---

## 布尔字面量类型

**基本写法：布尔字面量**
`type <名> = true | false`
```typescript
// 严格布尔取值
type True = true;
const t: true = true;
```

---

## 字面量推断放宽

**基本写法：let 推断放宽**
`let <变量> = "<值>"`
```typescript
// let 推断为基础类型
const c = "hi";   // "hi" 字面量
let v = "hi";     // string（放宽）
```

---

**基本写法：对象属性放宽**
`const <obj> = { <键>: <字面量> }`
```typescript
// 对象属性推断为基础类型
const cfg = { mode: "dev" }; // { mode: string }
cfg.mode; // string
```

---

## const 断言

**基本写法：as const 全对象断言**
`const <变量> = <对象> as const`
```typescript
// 全部属性转 readonly 字面量
const cfg = { mode: "dev", port: 3000 } as const;
// { readonly mode: "dev"; readonly port: 3000 }
cfg.mode; // "dev"
```

---

**基本写法：数组 as const 转元组**
`const <变量> = [<项>] as const`
```typescript
// 数组推断为只读元组
const arr = ["a", 1, true] as const;
// readonly ["a", 1, true]
arr[0]; // "a"
```

---

**基本写法：表达式 as const**
`"<值>" as const`
```typescript
// 单值断言为字面量
const x = "hi" as const; // "hi"
const y = [1, 2] as const; // readonly [1, 2]
```

---

## const 与枚举对比

**基本写法：as const 替代枚举**
`const <枚举> as const`
```typescript
// 联合字面量比枚举更利于 tree-shaking
const Color = { Red: "red", Green: "green" } as const;
type Color = typeof Color[keyof typeof Color]; // "red" | "green"
```

---

**基本写法：提取字面量联合**
`type <R> = typeof <对象>[keyof typeof <对象>]`
```typescript
// 从常量对象提取联合
const Status = { Idle: 0, Running: 1 } as const;
type Status = typeof Status[keyof typeof Status]; // 0 | 1
```

---

## 模板字面量类型

**基本写法：模板字面量类型**
`type <名> = `${<前缀>}${<变量>}``
```typescript
// 拼接字面量类型
type Greeting = `hello ${string}`;
const g: Greeting = "hello world";
```

---

**基本写法：联合展开**
`type <R> = `${<联合>}-${<联合>}``
```typescript
// 联合自动笛卡尔积
type Side = "top" | "bottom";
type Style = `${Side}-px`;
// "top-px" | "bottom-px"
```

---

## 字面量与映射

**基本写法：键转字面量**
`type <R> = keyof typeof <对象>`
```typescript
// 取字面量键联合
const api = { getUser: 1, setUser: 2 } as const;
type Api = keyof typeof api; // "getUser" | "setUser"
```

---

**基本写法：大写小写工具**
`Uppercase<<S>>` | `Lowercase<<S>>` | `Capitalize<<S>>` | `Uncapitalize<<S>>`
```typescript
// 内置字符串大小写工具
type U = Uppercase<"abc">;    // "ABC"
type L = Lowercase<"ABC">;    // "abc"
type C = Capitalize<"abc">;   // "Abc"
```

---

## 单值字面量断言

**基本写法：as 字面量断言**
`<值> as "<字面量>"`
```typescript
// 强制断言为字面量（需可兼容）
let v: string = "a";
const a = v as "a"; // "a"
```

---

## const 断言的限制

**基本写法：as const 不可用于已声明类型**
`let <变量>: <类型> = <值> as const`
```typescript
// as const 不能覆盖显式注解
const a: string = "hi" as const; // 仍是 string
// 对象展开保留 readonly
const o = { a: 1 } as const;
// o.a = 2; // 报错：只读
```

---

## 字面量与函数返回

**基本写法：函数返回字面量**
`function <f>(): <字面量>`
```typescript
// 显式返回字面量类型
function mode(): "dev" | "prod" { return "dev"; }
const m = mode(); // "dev" | "prod"
```

---

## 唯一字面量 brand 模式

**基本写法：brand 唯一字面量**
`type <名> = string & { readonly __brand: "<唯一>" }`
```typescript
// 用字面量做名义类型
type UserId = string & { readonly __brand: "UserId" };
function mk(s: string): UserId { return s as UserId; }
function find(id: UserId) {}
find(mk("u1"));
// find("u1"); // 报错：缺少 brand
```

---
