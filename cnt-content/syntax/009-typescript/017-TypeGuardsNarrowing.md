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
