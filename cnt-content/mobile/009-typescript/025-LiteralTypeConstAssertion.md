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