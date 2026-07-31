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
