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
