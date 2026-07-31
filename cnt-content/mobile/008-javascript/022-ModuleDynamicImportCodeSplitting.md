# JavaScript 动态 import 与代码分割

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 静态 import 回顾

**基本写法：静态导入**
`import <名称> from "<模块>"`
```javascript
// 静态导入在编译期分析打包到主 bundle
import lodash from "lodash";
```

---

**基本写法：命名导入**
`import { <名称>, <名称> } from "<模块>"`
```javascript
// 按需导入命名导出
import { debounce, throttle } from "lodash-es";
```

---

## 动态 import

**基本写法：动态 import 返回 Promise**
`import("<模块>")`
```javascript
// 运行时加载模块返回 Promise
import("./module.js").then(mod => {
    mod.doSomething();
});
```

---

**基本写法：await 动态 import**
`const <模块> = await import("<模块>")`
```javascript
// 配合 async await 使用
async function loadFeature() {
    const mod = await import("./feature.js");
    mod.run();
}
```

---

**基本写法：按需加载组件**
`const <组件> = React.lazy(() => import("<路径>"))`
```javascript
// React 路由或组件按需加载
const Page = React.lazy(() => import("./Page"));
```

---

**基本写法：Vue 异步组件**
`() => import("<路径>")`
```javascript
// Vue 异步组件工厂函数
const Page = () => import("./Page.vue");
```

---

## 条件加载

**基本写法：按条件加载**
`if (<条件>) import("<模块>")`
```javascript
// 满足条件才加载减少初始体积
if (typeof IntersectionObserver === "undefined") {
    await import("intersection-observer");
}
```

---

**基本写法：特性检测加载**
`if (!<特性>) import("<polyfill>")`
```javascript
// 按需加载 polyfill
if (!Array.prototype.flat) {
    await import("core-js/modules/es.array.flat");
}
```

---

**基本写法：环境判断**
`if (<环境>) import("<模块>")`
```javascript
// 开发环境加载调试工具
if (process.env.NODE_ENV === "development") {
    const { inspect } = await import("./inspect");
    inspect();
}
```

---

## 事件触发加载

**基本写法：点击后加载**
`<元素>.addEventListener("click", async () => await import("<模块>"))`
```javascript
// 用户点击时才加载模块
btn.addEventListener("click", async () => {
    const { editor } = await import("./editor");
    editor.show();
});
```

---

**基本写法：路由切换加载**
`{ path: "<路径>", component: () => import("<文件>") }`
```javascript
// Vue Router 懒加载路由
const routes = [
    { path: "/about", component: () => import("./About.vue") }
];
```

---

## Webpack 魔法注释

**基本写法：指定 chunk 名称**
`import(/* webpackChunkName: "<名称>" */ "<模块>")`
```javascript
// 自定义 chunk 名称便于识别
import(/* webpackChunkName: "editor" */ "./editor");
```

---

**基本写法：预加载 prefetch**
`import(/* webpackPrefetch: true */ "<模块>")`
```javascript
// 空闲时预加载提升后续体验
import(/* webpackPrefetch: true */ "./next-page");
```

---

**基本写法：预加载 preload**
`import(/* webpackPreload: true */ "<模块>")`
```javascript
// 与父 chunk 并行加载优先级高
import(/* webpackPreload: true */ "./critical");
```

---

**基本写法：组合魔法注释**
`import(/* webpackChunkName: "<n>", webpackPrefetch: true */ "<模块>")`
```javascript
// 多个魔法注释组合使用
import(/* webpackChunkName: "chart", webpackPrefetch: true */ "./chart");
```

---

## Vite Rollup 分割

**基本写法：Vite 自动分割**
`import("<模块>")`
```javascript
// Vite 自动分割动态 import
const mod = await import("./heavy");
```

---

**基本写法：manualChunks 配置**
`build.rollupOptions.output.manualChunks`
```javascript
// 手动配置 chunk 分割
export default {
    build: {
        rollupOptions: {
            output: {
                manualChunks: {
                    vendor: ["react", "react-dom"],
                    utils: ["lodash-es"]
                }
            }
        }
    }
};
```

---

## 加载状态处理

**基本写法：加载中提示**
`<Suspense fallback={<Loading />}>`
```javascript
// React Suspense 配合 lazy 显示加载
const Page = React.lazy(() => import("./Page"));
<Suspense fallback={<Loading />}><Page /></Suspense>;
```

---

**基本写法：错误处理**
`import("<模块>").catch(<回调>)`
```javascript
// 捕获加载失败错误
import("./module").catch(err => {
    console.error("load failed", err);
});
```

---

**基本写法：加载超时**
`Promise.race([import("<模块>"), <超时Promise>])`
```javascript
// 控制加载超时
Promise.race([
    import("./module"),
    new Promise((_, rej) => setTimeout(() => rej("timeout"), 5000))
]);
```

---

**基本写法：重试机制**
`async function <loadWithRetry>(<模块>, <次数>)`
```javascript
// 加载失败自动重试
async function loadWithRetry(path, times = 3) {
    for (let i = 0; i < times; i++) {
        try { return await import(path); }
        catch (e) { if (i === times - 1) throw e; }
    }
}
```

---

## import.meta

**基本写法：获取模块 URL**
`import.meta.url`
```javascript
// 获取当前模块 URL
let url = new URL("./data.json", import.meta.url);
```

---

**基本写法：Vite 环境变量**
`import.meta.env`
```javascript
// Vite 注入的环境变量
if (import.meta.env.DEV) console.log("dev mode");
```

---

**基本写法：动态资源路径**
`new URL("<资源>", import.meta.url)`
```javascript
// 动态计算资源路径
let img = new URL("./assets/logo.png", import.meta.url).href;
```

---

## 命名导出处理

**基本写法：解构动态导入**
`const { <名称> } = await import("<模块>")`
```javascript
// 直接解构命名导出
const { debounce } = await import("lodash-es");
```

---

**基本写法：默认导出**
`const <模块> = (await import("<模块>")).default`
```javascript
// 访问 default 属性
const lodash = (await import("lodash")).default;
```

---

## 实用模式

**基本写法：路由懒加载工厂**
`function <lazy>(<路径>) { return () => import(<路径>); }`
```javascript
// 统一路由懒加载工厂
function lazy(path) {
    return () => import(/* webpackChunkName: "[request]" */ path);
}
```

---

**基本写法：模块缓存复用**
`const <缓存> = new Map(); async function <load>(<名称>)`
```javascript
// 复用已加载模块避免重复
const cache = new Map();
async function load(name) {
    if (!cache.has(name)) cache.set(name, await import(`./mods/${name}`));
    return cache.get(name);
}
```

---

**基本写法：插件系统**
`async function <loadPlugin>(<名称>)`
```javascript
// 动态加载插件
async function loadPlugin(name) {
    const plugin = await import(`./plugins/${name}.js`);
    plugin.install(app);
}
```

---

## 性能优化

**基本写法：首屏关键资源**
`import("<首屏模块>")`
```javascript
// 首屏代码打包主 bundle 非首屏动态加载
const Home = lazy(() => import("./Home"));
```

---

**基本写法：vendor 分割**
`manualChunks: { vendor: <依赖数组> }`
```javascript
// 第三方库单独打包长期缓存
manualChunks: { react: ["react", "react-dom"] }
```

---

**基本写法：资源预取**
`<link rel="prefetch" href="<资源>">`
```javascript
// 提示浏览器空闲时预取
let link = document.createElement("link");
link.rel = "prefetch";
link.href = "/chunk.js";
document.head.appendChild(link);
```
