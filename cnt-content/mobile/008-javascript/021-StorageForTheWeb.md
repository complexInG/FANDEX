# JavaScript Web 存储 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## localStorage

**基本写法：setItem 存储**
`localStorage.setItem(<键>, <值>)`
```javascript
// 存储字符串值
localStorage.setItem("user", "Tom");
```

---

**基本写法：getItem 读取**
`localStorage.getItem(<键>)`
```javascript
// 读取存储的值不存在返回 null
let user = localStorage.getItem("user");
```

---

**基本写法：removeItem 删除**
`localStorage.removeItem(<键>)`
```javascript
// 删除指定键
localStorage.removeItem("user");
```

---

**基本写法：clear 清空**
`localStorage.clear()`
```javascript
// 清空当前域所有存储
localStorage.clear();
```

---

**基本写法：遍历键**
`localStorage.length` | `localStorage.key(<索引>)`
```javascript
// 遍历所有存储项
for (let i = 0; i < localStorage.length; i++) {
    let key = localStorage.key(i);
}
```

---

**基本写法：存储对象**
`localStorage.setItem(<键>, JSON.stringify(<对象>))`
```javascript
// 对象需序列化为字符串存储
localStorage.setItem("user", JSON.stringify({ name: "Tom" }));
```

---

**基本写法：读取对象**
`JSON.parse(localStorage.getItem(<键>))`
```javascript
// 读取后反序列化注意 null 处理
let user = JSON.parse(localStorage.getItem("user") || "null");
```

---

## sessionStorage

**基本写法：会话级存储**
`sessionStorage.setItem(<键>, <值>)`
```javascript
// 标签页关闭后清除
sessionStorage.setItem("token", "abc");
```

---

**基本写法：API 与 localStorage 一致**
`sessionStorage.getItem(<键>)`
```javascript
// API 完全相同生命周期不同
let token = sessionStorage.getItem("token");
```

---

## 存储事件

**基本写法：跨标签页通信**
`window.addEventListener("storage", <回调>)`
```javascript
// 同源其他标签页 storage 变化触发
window.addEventListener("storage", e => {
    console.log(e.key, e.newValue);
});
```

---

**基本写法：事件对象**
`{ key, newValue, oldValue, url }`
```javascript
// storage 事件包含变更详情
window.addEventListener("storage", e => {
    if (e.key === "cart") updateCart(e.newValue);
});
```

---

## IndexedDB 基础

**基本写法：打开数据库**
`indexedDB.open(<名称>, [<版本>])`
```javascript
// 打开或创建数据库返回请求
let req = indexedDB.open("myDB", 1);
```

---

**基本写法：监听事件**
`<请求>.onsuccess = <回调>` | `<请求>.onupgradeneeded = <回调>`
```javascript
// 升级时创建对象仓库
let req = indexedDB.open("myDB", 1);
req.onupgradeneeded = e => {
    let db = e.target.result;
    db.createObjectStore("users", { keyPath: "id" });
};
req.onsuccess = e => { let db = e.target.result; };
```

---

**基本写法：创建仓库与索引**
`<db>.createObjectStore(<名称>, { keyPath: <键> })`
```javascript
// 在 upgrade 时创建仓库
let store = db.createObjectStore("users", { keyPath: "id" });
store.createIndex("name", "name", { unique: false });
```

---

## IndexedDB 事务

**基本写法：开启事务**
`<db>.transaction(<仓库名>, <模式>)`
```javascript
// 事务读写数据
let tx = db.transaction("users", "readwrite");
let store = tx.objectStore("users");
```

---

**基本写法：添加数据**
`<store>.add(<对象>)`
```javascript
// 添加记录
let tx = db.transaction("users", "readwrite");
tx.objectStore("users").add({ id: 1, name: "Tom" });
```

---

**基本写法：读取数据**
`<store>.get(<键>)`
```javascript
// 按键读取
let req = db.transaction("users").objectStore("users").get(1);
req.onsuccess = e => console.log(e.target.result);
```

---

**基本写法：修改数据**
`<store>.put(<对象>)`
```javascript
// put 存在则更新不存在则添加
tx.objectStore("users").put({ id: 1, name: "Jerry" });
```

---

**基本写法：删除数据**
`<store>.delete(<键>)`
```javascript
// 按键删除记录
tx.objectStore("users").delete(1);
```

---

**基本写法：清空仓库**
`<store>.clear()`
```javascript
// 清空整个仓库
tx.objectStore("users").clear();
```

---

## IndexedDB 游标

**基本写法：遍历数据**
`<store>.openCursor()`
```javascript
// 使用游标遍历所有记录
let req = db.transaction("users").objectStore("users").openCursor();
req.onsuccess = e => {
    let cursor = e.target.result;
    if (cursor) { console.log(cursor.value); cursor.continue(); }
};
```

---

**基本写法：使用索引查询**
`<store>.index(<索引名>).get(<值>)`
```javascript
// 通过索引查询
let req = store.index("name").get("Tom");
```

---

## Promise 封装

**基本写法：Promise 封装 IndexedDB**
`function <open>(<名称>, <版本>, <升级回调>) { }`
```javascript
// 将请求 API 转为 Promise
function openDB(name, version, upgrade) {
    return new Promise((resolve, reject) => {
        let req = indexedDB.open(name, version);
        req.onupgradeneeded = e => upgrade(e.target.result);
        req.onsuccess = e => resolve(e.target.result);
        req.onerror = e => reject(e.target.error);
    });
}
```

---

**基本写法：async await 操作**
`await <封装的请求>`
```javascript
// 配合 async await 优雅操作
async function getUser(db, id) {
    return new Promise((resolve, reject) => {
        let req = db.transaction("users").objectStore("users").get(id);
        req.onsuccess = () => resolve(req.result);
        req.onerror = () => reject(req.error);
    });
}
```

---

## Cookie

**基本写法：写入 Cookie**
`document.cookie = "<键>=<值>; [expires=<日期>]; [path=<路径>]"`
```javascript
// 设置 cookie 默认会话级
document.cookie = "user=Tom; max-age=3600; path=/";
```

---

**基本写法：读取 Cookie**
`document.cookie`
```javascript
// 读取返回所有 cookie 字符串
let cookies = document.cookie;
```

---

**基本写法：删除 Cookie**
`document.cookie = "<键>=; expires=<过去时间>"`
```javascript
// 设置过期时间为过去删除
document.cookie = "user=; expires=Thu, 01 Jan 1970 00:00:00 GMT";
```

---

## Cache API

**基本写法：打开缓存**
`caches.open(<名称>)`
```javascript
// 用于 Service Worker 缓存
caches.open("v1").then(cache => {});
```

---

**基本写法：缓存请求**
`<cache>.put(<请求>, <响应>)`
```javascript
// 缓存 fetch 响应
caches.open("v1").then(cache => {
    fetch("/api").then(res => cache.put("/api", res.clone()));
});
```

---

**基本写法：读取缓存**
`<cache>.match(<请求>)`
```javascript
// 从缓存匹配请求
caches.open("v1").then(cache => cache.match("/api"))
    .then(res => {});
```

---

## 存储容量

**基本写法：查询存储估算**
`navigator.storage.estimate()`
```javascript
// 查询当前使用量与配额
navigator.storage.estimate().then(est => {
    console.log(est.usage, est.quota);
});
```

---

**基本写法：请求持久化存储**
`navigator.storage.persist()`
```javascript
// 请求持久化避免被自动清除
navigator.storage.persist().then(persisted => {});
```

---

## 工具函数

**基本写法：JSON 存储封装**
`const <storage> = { get, set, remove }`
```javascript
// 封装 localStorage JSON 操作
const storage = {
    get(key, def = null) {
        let val = localStorage.getItem(key);
        return val ? JSON.parse(val) : def;
    },
    set(key, value) { localStorage.setItem(key, JSON.stringify(value)); },
    remove(key) { localStorage.removeItem(key); }
};
```

---

**基本写法：带过期时间存储**
`<storage>.set(<键>, <值>, <过期毫秒>)`
```javascript
// 数据自动过期
const storage = {
    set(key, value, ttl) {
        localStorage.setItem(key, JSON.stringify({
            value, expire: Date.now() + ttl
        }));
    },
    get(key) {
        let data = JSON.parse(localStorage.getItem(key) || "null");
        if (!data) return null;
        if (data.expire < Date.now()) { localStorage.removeItem(key); return null; }
        return data.value;
    }
};
```

---

## 存储选择

**基本写法：选型对比**
| 存储 | 容量 | 同步 | 生命周期 |
|------|------|------|----------|
| localStorage | 5-10MB | 同步 | 永久 |
| sessionStorage | 5-10MB | 同步 | 会话 |
| IndexedDB | 数百MB+ | 异步 | 永久 |
| Cookie | 4KB | 同步 | 可配置 |
```javascript
// 小数据用 localStorage 大数据用 IndexedDB
```
