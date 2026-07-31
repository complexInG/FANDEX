# JavaScript Web API 浏览器接口语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## fetch 请求

**基本写法：基础请求**
`fetch(<url>, [<选项>])`
```javascript
// 返回 Promise<Response>
const res = await fetch("/api/user");
const data = await res.json();
```

---

**基本写法：带请求配置**
`fetch(<url>, { method, headers, body })`
```javascript
// POST JSON
const res = await fetch("/api/user", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Tom" }),
});
```

---

**基本写法：错误与状态处理**
`<res>.ok` | `<res>.status`
```javascript
// fetch 仅在网络错误时 reject
if (!res.ok) throw new Error(`HTTP ${res.status}`);
```

---

**基本写法：中止请求**
`new AbortController()` | `signal: <signal>`
```javascript
// 超时或取消请求
const ctrl = new AbortController();
setTimeout(() => ctrl.abort(), 5000);
const res = await fetch("/api", { signal: ctrl.signal });
```

---

## 网络请求与流

**基本写法：读取响应流**
`<res>.body.getReader()`
```javascript
// 流式读取大响应
const reader = res.body.getReader();
while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  console.log(value); // Uint8Array 分块
}
```

---

## IntersectionObserver 可视区观察

**基本写法：观察元素可见性**
`new IntersectionObserver(<回调>, [<选项>])`
```javascript
// 元素进入/离开视口触发
const ob = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) console.log("可见", e.target);
  });
}, { threshold: 0.5 });
ob.observe(document.querySelector(".box"));
```

---

**基本写法：取消观察**
`<observer>.unobserve(<元素>)` | `<observer>.disconnect()`
```javascript
// 停止观察单个或全部
ob.unobserve(el);
ob.disconnect();
```

---

## MutationObserver DOM 变动

**基本写法：监听 DOM 变化**
`new MutationObserver(<回调>)`
```javascript
// 子节点/属性变化回调
const ob = new MutationObserver(muts => {
  muts.forEach(m => console.log(m.type, m.target));
});
ob.observe(document.body, {
  childList: true,     // 子节点变动
  subtree: true,       // 含后代
  attributes: true,    // 属性变动
  characterData: true, // 文本变动
});
```

---

## ResizeObserver 尺寸观察

**基本写法：监听元素尺寸**
`new ResizeObserver(<回调>)`
```javascript
// 元素尺寸变化回调
const ob = new ResizeObserver(entries => {
  entries.forEach(e => console.log(e.contentRect.width));
});
ob.observe(document.querySelector(".box"));
```

---

## LocalStorage 与 SessionStorage

**基本写法：存储读取**
`localStorage.setItem(<键>, <值>)`
```javascript
// 仅存字符串，对象需序列化
localStorage.setItem("user", JSON.stringify({ id: 1 }));
const user = JSON.parse(localStorage.getItem("user"));
localStorage.removeItem("user");
localStorage.clear();
```

---

**基本写法：sessionStorage 会话存储**
`sessionStorage.setItem(<键>, <值>)`
```javascript
// 标签页关闭即清除
sessionStorage.setItem("token", "abc");
sessionStorage.getItem("token");
```

---

## 定时器

**基本写法：延时与循环**
`setTimeout(<回调>, <毫秒>)` | `setInterval(<回调>, <毫秒>)`
```javascript
const t1 = setTimeout(() => {}, 1000);
const t2 = setInterval(() => {}, 1000);
clearTimeout(t1);
clearInterval(t2);
```

---

**基本写法：requestAnimationFrame**
`requestAnimationFrame(<回调>)`
```javascript
// 与刷新率同步的动画帧
let id = requestAnimationFrame(loop);
function loop(t) {
  // t 为高精度时间戳
  id = requestAnimationFrame(loop);
}
cancelAnimationFrame(id);
```

---

## URL 与 History

**基本写法：URL 解析**
`new URL(<url>, [<base>])`
```javascript
// 解析与拼接 URL
const u = new URL("/api", "https://a.com");
u.searchParams.set("q", "js");
u.toString(); // https://a.com/api?q=js
```

---

**基本写法：历史记录操作**
`history.pushState(<state>, <标题>, <url>)`
```javascript
// 不刷新页面改地址
history.pushState({ page: 1 }, "", "/page1");
history.replaceState({}, "", "/page2");
history.back();
window.onpopstate = e => console.log(e.state);
```

---

## Clipboard 剪贴板

**基本写法：读写剪贴板**
`navigator.clipboard.writeText(<文本>)`
```javascript
// 需 HTTPS 与用户手势
await navigator.clipboard.writeText("复制内容");
const text = await navigator.clipboard.readText();
```

---

## BroadcastChannel 跨页通信

**基本写法：同源页面广播**
`new BroadcastChannel(<频道名>)`
```javascript
// 同源多标签页通信
const ch = new BroadcastChannel("evt");
ch.postMessage({ hello: 1 });
ch.onmessage = e => console.log(e.data);
ch.close();
```

---