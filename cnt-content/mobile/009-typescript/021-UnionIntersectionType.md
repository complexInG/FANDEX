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