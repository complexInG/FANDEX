# JavaScript 深浅拷贝方法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 浅拷贝

**基本写法：Object.assign**
`Object.assign({}, <源对象>)`
```javascript
// 浅拷贝一级属性嵌套仍引用
let copy = Object.assign({}, obj);
```

---

**基本写法：展开运算符**
`{ ...<对象> }`
```javascript
// 对象展开为浅拷贝
let copy = { ...obj };
```

---

**基本写法：数组展开**
`[ ...<数组> ]`
```javascript
// 数组展开为浅拷贝
let copy = [...arr];
```

---

**基本写法：slice 浅拷贝数组**
`<数组>.slice()`
```javascript
// slice 无参返回新数组
let copy = arr.slice();
```

---

**基本写法：concat 浅拷贝数组**
`<数组>.concat()`
```javascript
// concat 无参返回新数组
let copy = arr.concat();
```

---

**基本写法：Array.from**
`Array.from(<数组>)`
```javascript
// 从可迭代对象创建新数组
let copy = Array.from(arr);
```

---

## JSON 深拷贝

**基本写法：JSON 序列化**
`JSON.parse(JSON.stringify(<对象>))`
```javascript
// 简单深拷贝但无法处理函数 undefined 循环引用
let deep = JSON.parse(JSON.stringify(obj));
```

---

**基本写法：JSON 限制**
`JSON.parse(JSON.stringify(<含 Date 对象>))`
```javascript
// Date 会变成字符串 Map Set 丢失
let obj = { d: new Date() };
let copy = JSON.parse(JSON.stringify(obj));  // d 变为字符串
```

---

## 递归深拷贝

**基本写法：基础递归深拷贝**
`function <深拷贝>(<对象>) { }`
```javascript
// 递归处理对象和数组
function deepClone(obj) {
    if (obj === null || typeof obj !== "object") return obj;
    if (Array.isArray(obj)) return obj.map(deepClone);
    let copy = {};
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) copy[key] = deepClone(obj[key]);
    }
    return copy;
}
```

---

**基本写法：处理 Date RegExp**
`function <深拷贝>(<对象>) { }`
```javascript
// 处理特殊对象类型
function deepClone(obj) {
    if (obj instanceof Date) return new Date(obj);
    if (obj instanceof RegExp) return new RegExp(obj);
    if (obj === null || typeof obj !== "object") return obj;
    let copy = Array.isArray(obj) ? [] : {};
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) copy[key] = deepClone(obj[key]);
    }
    return copy;
}
```

---

## 循环引用处理

**基本写法：使用 WeakMap 解决循环引用**
`function <深拷贝>(<对象>, <hash>) { }`
```javascript
// WeakMap 记录已拷贝对象避免重复
function deepClone(obj, hash = new WeakMap()) {
    if (obj === null || typeof obj !== "object") return obj;
    if (hash.has(obj)) return hash.get(obj);
    let copy = Array.isArray(obj) ? [] : {};
    hash.set(obj, copy);
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) copy[key] = deepClone(obj[key], hash);
    }
    return copy;
}
```

---

## Map Set 拷贝

**基本写法：拷贝 Map**
`new Map(<源 Map>)`
```javascript
// Map 浅拷贝
let copy = new Map(map);
```

---

**基本写法：深拷贝 Map**
`function <深拷贝Map>(<源>) { }`
```javascript
// 递归拷贝 Map 值
function deepCloneMap(map, hash = new WeakMap()) {
    if (hash.has(map)) return hash.get(map);
    let copy = new Map();
    hash.set(map, copy);
    for (let [k, v] of map) copy.set(deepClone(k, hash), deepClone(v, hash));
    return copy;
}
```

---

**基本写法：拷贝 Set**
`new Set(<源 Set>)`
```javascript
// Set 浅拷贝
let copy = new Set(set);
```

---

## structuredClone

**基本写法：structuredClone**
`structuredClone(<对象>)`
```javascript
// 原生深拷贝支持循环引用 Date Map Set
let deep = structuredClone(obj);
```

---

**基本写法：transfer 转移**
`structuredClone(<对象>, { transfer: [<可转移对象>] })`
```javascript
// 转移 ArrayBuffer 提升性能源对象失效
let buf = new ArrayBuffer(8);
let copy = structuredClone(buf, { transfer: [buf] });
```

---

**基本写法：structuredClone 限制**
`structuredClone(<含函数对象>)`
```javascript
// 不支持函数 DOM 节点抛出异常
let obj = { fn: () => {} };
structuredClone(obj);  // 抛出 DataCloneError
```

---

## 特殊对象拷贝

**基本写法：拷贝 RegExp**
`new RegExp(<源>)`
```javascript
// 复制正则对象
let copy = new RegExp(regex);
```

---

**基本写法：拷贝 Date**
`new Date(<源>)`
```javascript
// 复制日期对象
let copy = new Date(date);
```

---

**基本写法：拷贝 Error**
`new <Error类型>(<源>.message)`
```javascript
// 复制错误对象
let copy = new Error(err.message);
```

---

## 自定义类拷贝

**基本写法：通过构造器重建**
`new <类>(<源对象>)`
```javascript
// 调用构造器重新创建实例
class Point {
    constructor(x, y) { this.x = x; this.y = y; }
    clone() { return new Point(this.x, this.y); }
}
```

---

## 性能对比

**基本写法：浅拷贝性能最优**
`{ ...<对象> }`
```javascript
// 浅拷贝最快但只复制一层
let copy = { ...obj };
```

---

**基本写法：structuredClone 平衡**
`structuredClone(<对象>)`
```javascript
// 原生 API 性能优于递归实现
let copy = structuredClone(obj);
```

---

**基本写法：JSON 适合纯数据**
`JSON.parse(JSON.stringify(<对象>))`
```javascript
// 纯数据场景 JSON 最快
let copy = JSON.parse(JSON.stringify(data));
```

---

## 实用工具函数

**基本写法：通用深拷贝工具**
`function <deepClone>(<对象>) { }`
```javascript
// 综合处理各种类型的深拷贝
function deepClone(obj, hash = new WeakMap()) {
    if (obj === null || typeof obj !== "object") return obj;
    if (obj instanceof Date) return new Date(obj);
    if (obj instanceof RegExp) return new RegExp(obj);
    if (obj instanceof Map) {
        let copy = new Map(); hash.set(obj, copy);
        for (let [k, v] of obj) copy.set(deepClone(k, hash), deepClone(v, hash));
        return copy;
    }
    if (obj instanceof Set) {
        let copy = new Set(); hash.set(obj, copy);
        for (let v of obj) copy.add(deepClone(v, hash));
        return copy;
    }
    if (hash.has(obj)) return hash.get(obj);
    let copy = Array.isArray(obj) ? [] : {};
    hash.set(obj, copy);
    for (let key of Reflect.ownKeys(obj)) copy[key] = deepClone(obj[key], hash);
    return copy;
}
```

---

## 引用关系

**基本写法：浅拷贝引用关系**
`let <副本> = { ...<对象> }`
```javascript
// 嵌套对象仍共享引用
let obj = { nested: { a: 1 } };
let copy = { ...obj };
copy.nested.a = 2;  // obj.nested.a 也变为 2
```

---

**基本写法：深拷贝独立**
`let <副本> = structuredClone(<对象>)`
```javascript
// 深拷贝完全独立互不影响
let obj = { nested: { a: 1 } };
let copy = structuredClone(obj);
copy.nested.a = 2;  // obj.nested.a 仍为 1
```
