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
