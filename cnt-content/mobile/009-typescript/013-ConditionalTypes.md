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
