# JavaScript Symbol 与迭代协议语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Symbol 基础

**基本写法：创建唯一值**
`Symbol([<描述>])`
```javascript
// 每次创建独一无二，不可强制转换
const s1 = Symbol("id");
const s2 = Symbol("id");
s1 === s2; // false
s1.description; // "id"
```

---

**基本写法：作为对象键**
`{ [<symbol>]: <值> }`
```javascript
// Symbol 键不会被 for-in/Object.keys 枚举
const KEY = Symbol("hidden");
const obj = { [KEY]: "secret", name: "Tom" };
Object.keys(obj);          // ["name"]
Object.getOwnPropertySymbols(obj); // [Symbol(hidden)]
```

---

**基本写法：全局注册**
`Symbol.for(<键>)` | `Symbol.keyFor(<symbol>)`
```javascript
// 同键返回同一 Symbol
const a = Symbol.for("shared");
const b = Symbol.for("shared");
a === b;            // true
Symbol.keyFor(a);   // "shared"
```

---

## 内置 Symbol

**基本写法：常用内置 Symbol**
`Symbol.<wellKnown>`
```javascript
Symbol.iterator;       // 自定义迭代器
Symbol.asyncIterator;  // 自定义异步迭代器
Symbol.toPrimitive;    // 类型转换
Symbol.toStringTag;    // toString 标识
Symbol.hasInstance;    // instanceof 行为
```

---

## 迭代协议

**基本写法：iterable 协议**
`[Symbol.iterator]() { return <iterator> }`
```javascript
// 实现 Symbol.iterator 即可迭代
const range = {
  from: 1, to: 3,
  [Symbol.iterator]() {
    let cur = this.from;
    const last = this.to;
    return {
      next() {
        return cur <= last
          ? { value: cur++, done: false }
          : { value: undefined, done: true };
      }
    };
  }
};
[...range]; // [1, 2, 3]
```

---

**基本写法：iterator 协议**
`next() { return { value, done } }`
```javascript
// 迭代器对象须有 next 方法
const it = range[Symbol.iterator]();
it.next(); // { value: 1, done: false }
it.next(); // { value: 2, done: false }
it.next(); // { value: 3, done: false }
it.next(); // { value: undefined, done: true }
```

---

**基本写法：return 提前终止**
`return(<值>) { ... }`
```javascript
// for-of 提前 break/throw 时调用
return {
  next() { /* ... */ },
  return(v) { console.log("清理"); return { value: v, done: true }; }
};
```

---

## 生成器函数

**基本写法：声明生成器**
`function* <名>() { yield <值> }`
```javascript
// 生成器函数返回迭代器
function* gen() {
  yield 1;
  yield 2;
  yield 3;
}
const it = gen();
it.next(); // { value: 1, done: false }
[...gen()]; // [1, 2, 3]
```

---

**基本写法：yield 委托**
`yield* <可迭代>`
```javascript
// 委托给另一个可迭代对象
function* inner() { yield "a"; yield "b"; }
function* outer() { yield 1; yield* inner(); yield 2; }
[...outer()]; // [1, "a", "b", 2]
```

---

**基本写法：双向通信**
`<变量> = yield <值>`
```javascript
// next 参数回传到 yield
function* dialog() {
  const x = yield 1;
  console.log("收到", x); // 收到 hi
}
const it = dialog();
it.next();      // { value: 1 }
it.next("hi");  // 输出 收到 hi
```

---

**基本写法：生成器作迭代器**
`{ [Symbol.iterator]: function* () {} }`
```javascript
// 用生成器简化可迭代对象
const obj = {
  data: [10, 20, 30],
  *[Symbol.iterator]() {
    for (const v of this.data) yield v;
  }
};
[...obj]; // [10, 20, 30]
```

---

## 异步迭代

**基本写法：异步可迭代协议**
`[Symbol.asyncIterator]() { return { next() } }`
```javascript
// 异步迭代器返回 Promise
const src = {
  async *[Symbol.asyncIterator]() {
    yield 1;
    yield 2;
  }
};
for await (const v of src) console.log(v);
```

---

**基本写法：for await 遍历**
`for await (const <v> of <异步可迭代>) {}`
```javascript
// 消费异步迭代器
async function* lines() {
  yield "a"; yield "b";
}
for await (const line of lines()) {
  console.log(line);
}
```

---

## 默认可迭代对象

**基本写法：内置可迭代类型**
`for (const <v> of <可迭代>) {}`
```javascript
// Array Map Set String arguments NodeLists 均可迭代
for (const x of [1, 2]) {}
for (const [k, v] of new Map()) {}
for (const c of "abc") {}
```

---

## 解构与展开

**基本写法：展开可迭代**
`[...<可迭代>]`
```javascript
// 任何可迭代对象都能展开
const arr = [...new Set([1, 2]), ...range];
```

---