# JavaScript Proxy 与 Reflect

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Proxy 基础

**基本写法：创建 Proxy**
`new Proxy(<目标对象>, <处理器>)`
```javascript
// Proxy 代理目标对象拦截操作
let proxy = new Proxy({}, { get(t, k) { return k in t ? t[k] : 42; } });
```

---

**基本写法：get 拦截**
`new Proxy(<目标>, { get(<target>, <prop>) { } })`
```javascript
// 拦截属性读取
let proxy = new Proxy(obj, {
    get(target, prop) {
        console.log(`read ${String(prop)}`);
        return Reflect.get(target, prop);
    }
});
```

---

**基本写法：set 拦截**
`new Proxy(<目标>, { set(<target>, <prop>, <value>) { } })`
```javascript
// 拦截属性设置做校验
let proxy = new Proxy(obj, {
    set(target, prop, value) {
        if (prop === "age" && value < 0) throw new Error("invalid");
        return Reflect.set(target, prop, value);
    }
});
```

---

**基本写法：has 拦截**
`new Proxy(<目标>, { has(<target>, <prop>) { } })`
```javascript
// 拦截 in 操作符
let proxy = new Proxy(obj, {
    has(target, prop) {
        return prop.startsWith("_") ? false : Reflect.has(target, prop);
    }
});
```

---

**基本写法：deleteProperty 拦截**
`new Proxy(<目标>, { deleteProperty(<target>, <prop>) { } })`
```javascript
// 拦截 delete 操作
let proxy = new Proxy(obj, {
    deleteProperty(target, prop) {
        console.log(`delete ${String(prop)}`);
        return Reflect.deleteProperty(target, prop);
    }
});
```

---

## 函数拦截

**基本写法：apply 拦截**
`new Proxy(<函数>, { apply(<target>, <thisArg>, <args>) { } })`
```javascript
// 拦截函数调用
let fn = new Proxy(function (x) { return x; }, {
    apply(target, thisArg, args) {
        return Reflect.apply(target, thisArg, args) * 2;
    }
});
fn(5);  // 10
```

---

**基本写法：construct 拦截**
`new Proxy(<构造器>, { construct(<target>, <args>) { } })`
```javascript
// 拦截 new 调用
let Klass = new Proxy(function () {}, {
    construct(target, args) {
        return Reflect.construct(target, args);
    }
});
new Klass();
```

---

## Reflect 静态方法

**基本写法：Reflect.get**
`Reflect.get(<目标>, <属性>, [<this>])`
```javascript
// 等同 target[key] 但可指定 this
let val = Reflect.get(obj, "name");
```

---

**基本写法：Reflect.set**
`Reflect.set(<目标>, <属性>, <值>, [<this>])`
```javascript
// 等同赋值返回布尔表示成功
let ok = Reflect.set(obj, "name", "Tom");
```

---

**基本写法：Reflect.has**
`Reflect.has(<目标>, <属性>)`
```javascript
// 等同 in 操作符
let exists = Reflect.has(obj, "name");
```

---

**基本写法：Reflect.ownKeys**
`Reflect.ownKeys(<目标>)`
```javascript
// 返回所有自有键含 Symbol
let keys = Reflect.ownKeys(obj);
```

---

**基本写法：Reflect.deleteProperty**
`Reflect.deleteProperty(<目标>, <属性>)`
```javascript
// 等同 delete 返回布尔
let ok = Reflect.deleteProperty(obj, "name");
```

---

**基本写法：Reflect.construct**
`Reflect.construct(<构造器>, <参数列表>)`
```javascript
// 等同 new 但可指定原型
let instance = Reflect.construct(Klass, [1, 2]);
```

---

**基本写法：Reflect.apply**
`Reflect.apply(<函数>, <this>, <参数列表>)`
```javascript
// 函数调用替代 fn.apply
let result = Reflect.apply(fn, thisArg, [1, 2]);
```

---

## 常见陷阱

**基本写法：响应式对象**
`new Proxy(<目标>, { get, set })`
```javascript
// 简易响应式系统
function reactive(obj) {
    return new Proxy(obj, {
        get(target, key, receiver) {
            track(target, key);
            return Reflect.get(target, key, receiver);
        },
        set(target, key, value, receiver) {
            const result = Reflect.set(target, key, value, receiver);
            trigger(target, key);
            return result;
        }
    });
}
```

---

**基本写法：私有属性保护**
`new Proxy(<目标>, { get, has })`
```javascript
// 禁止访问下划线开头属性
let proxy = new Proxy(obj, {
    get(target, prop) {
        if (prop[0] === "_") throw new Error("private");
        return Reflect.get(target, prop);
    }
});
```

---

**基本写法：默认值**
`new Proxy(<目标>, { get })`
```javascript
// 属性不存在时返回默认值
let proxy = new Proxy({}, {
    get(target, prop) {
        return prop in target ? target[prop] : "default";
    }
});
```

---

**基本写法：缓存代理**
`new Proxy(<函数>, { apply })`
```javascript
// 缓存函数结果
function memoize(fn) {
    let cache = new Map();
    return new Proxy(fn, {
        apply(target, thisArg, args) {
            let key = JSON.stringify(args);
            if (!cache.has(key)) cache.set(key, Reflect.apply(target, thisArg, args));
            return cache.get(key);
        }
    });
}
```

---

**基本写法：属性验证**
`new Proxy(<目标>, { set })`
```javascript
// 设置属性时做类型校验
let proxy = new Proxy({}, {
    set(target, prop, value) {
        if (prop === "age" && typeof value !== "number") return false;
        return Reflect.set(target, prop, value);
    }
});
```

---

**基本写法：日志代理**
`new Proxy(<目标>, { get, set })`
```javascript
// 记录属性访问与修改
let proxy = new Proxy(obj, {
    get(target, prop) {
        console.log(`get ${String(prop)}`);
        return Reflect.get(target, prop);
    },
    set(target, prop, value) {
        console.log(`set ${String(prop)} = ${value}`);
        return Reflect.set(target, prop, value);
    }
});
```

---

## receiver 参数

**基本写法：receiver 保持 this 指向**
`Reflect.get(<target>, <prop>, <receiver>)`
```javascript
// receiver 保证 getter 中的 this 正确
let proxy = new Proxy(obj, {
    get(target, prop, receiver) {
        return Reflect.get(target, prop, receiver);
    }
});
```

---

## 可撤销 Proxy

**基本写法：revoke 撤销**
`Proxy.revocable(<目标>, <处理器>)`
```javascript
// 创建可撤销代理
let { proxy, revoke } = Proxy.revocable(obj, {
    get(t, k) { return Reflect.get(t, k); }
});
revoke();  // 之后访问 proxy 抛出 TypeError
```

---

## 数组代理

**基本写法：数组索引拦截**
`new Proxy(<数组>, { get, set })`
```javascript
// 拦截数组读写触发更新
let arr = new Proxy([1, 2, 3], {
    set(target, prop, value, receiver) {
        if (!isNaN(prop)) console.log(`set index ${prop}`);
        return Reflect.set(target, prop, value, receiver);
    }
});
arr[0] = 99;
```

---

## 实用模式

**基本写法：观察者模式**
`function <observable>(<对象>, <回调>)`
```javascript
// 监听对象所有修改
function observable(obj, callback) {
    return new Proxy(obj, {
        set(target, prop, value, receiver) {
            const old = target[prop];
            const result = Reflect.set(target, prop, value, receiver);
            if (old !== value) callback(prop, value, old);
            return result;
        }
    });
}
```

---

**基本写法：单例代理**
`new Proxy(<构造器>, { construct })`
```javascript
// 限制只能创建一个实例
let Singleton = new Proxy(class {}, {
    construct(target, args) {
        if (!instance) instance = Reflect.construct(target, args);
        return instance;
    }
});
```

---

## Proxy 限制

**基本写法：不可代理的对象**
`new Proxy(<目标>, <处理器>)`
```javascript
// 一些内置对象不可代理如 Map 的内部槽
let proxy = new Proxy(new Map(), {});
proxy.set("a", 1);  // 抛出 TypeError
```

---

**基本写法：兼容性处理**
`Object.defineProperty(<对象>, <属性>, <描述>)`
```javascript
// Proxy 不支持时退回 defineProperty
function defineReactive(obj, key, val) {
    Object.defineProperty(obj, key, {
        get() { return val; },
        set(newVal) { val = newVal; }
    });
}
```
