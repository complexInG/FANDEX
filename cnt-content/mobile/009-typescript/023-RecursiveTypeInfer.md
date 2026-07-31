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