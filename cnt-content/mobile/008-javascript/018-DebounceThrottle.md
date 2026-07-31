# JavaScript 防抖节流实现

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 防抖 debounce

**基本写法：防抖基本实现**
`function <防抖>(<函数>, <等待时间>) { }`
```javascript
// 防抖在停止触发后等待时间才执行
function debounce(fn, wait) {
    let timer;
    return function (...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), wait);
    };
}
```

---

**基本写法：立即执行防抖**
`function <防抖>(<函数>, <等待时间>, { leading: true })`
```javascript
// 首次触发立即执行后续等待
function debounce(fn, wait) {
    let timer, called = false;
    return function (...args) {
        if (!called) { fn.apply(this, args); called = true; }
        clearTimeout(timer);
        timer = setTimeout(() => called = false, wait);
    };
}
```

---

**基本写法：带 cancel 取消**
`<防抖函数>.cancel()`
```javascript
// 取消未执行的防抖调用
function debounce(fn, wait) {
    let timer;
    const debounced = (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), wait);
    };
    debounced.cancel = () => clearTimeout(timer);
    return debounced;
}
```

---

**基本写法：带 flush 立即执行**
`<防抖函数>.flush()`
```javascript
// 立即执行挂起的调用
function debounce(fn, wait) {
    let timer, lastArgs;
    const debounced = (...args) => {
        lastArgs = args;
        clearTimeout(timer);
        timer = setTimeout(() => fn(...lastArgs), wait);
    };
    debounced.flush = () => { clearTimeout(timer); if (lastArgs) fn(...lastArgs); };
    return debounced;
}
```

---

## 节流 throttle

**基本写法：节流定时器实现**
`function <节流>(<函数>, <等待时间>) { }`
```javascript
// 节流在间隔时间内最多执行一次
function throttle(fn, wait) {
    let timer = null;
    return function (...args) {
        if (timer) return;
        timer = setTimeout(() => { fn.apply(this, args); timer = null; }, wait);
    };
}
```

---

**基本写法：节流时间戳实现**
`function <节流>(<函数>, <等待时间>) { }`
```javascript
// 基于时间戳首次立即执行
function throttle(fn, wait) {
    let last = 0;
    return function (...args) {
        const now = Date.now();
        if (now - last >= wait) { fn.apply(this, args); last = now; }
    };
}
```

---

**基本写法：节流首次与尾调用**
`function <节流>(<函数>, <等待时间>) { }`
```javascript
// 首次立即执行并保留最后一次调用
function throttle(fn, wait) {
    let last = 0, timer, lastArgs;
    return function (...args) {
        const now = Date.now();
        const remaining = wait - (now - last);
        if (remaining <= 0) {
            clearTimeout(timer); timer = null;
            fn.apply(this, args); last = now;
        } else if (!timer) {
            lastArgs = args;
            timer = setTimeout(() => {
                fn.apply(this, lastArgs); last = Date.now(); timer = null;
            }, remaining);
        }
    };
}
```

---

**基本写法：节流带 cancel**
`<节流函数>.cancel()`
```javascript
// 取消节流并重置状态
function throttle(fn, wait) {
    let timer = null;
    const throttled = (...args) => {
        if (timer) return;
        timer = setTimeout(() => { fn(...args); timer = null; }, wait);
    };
    throttled.cancel = () => { clearTimeout(timer); timer = null; };
    return throttled;
}
```

---

## 应用场景

**基本写法：搜索输入防抖**
`<输入框>.addEventListener("input", <防抖>(<回调>, <等待>))`
```javascript
// 输入搜索时减少请求频率
input.addEventListener("input", debounce(e => {
    search(e.target.value);
}, 300));
```

---

**基本写法：窗口 resize 节流**
`window.addEventListener("resize", <节流>(<回调>, <等待>))`
```javascript
// 窗口尺寸变化时节流计算
window.addEventListener("resize", throttle(() => {
    layout();
}, 200));
```

---

**基本写法：滚动事件节流**
`window.addEventListener("scroll", <节流>(<回调>, <等待>))`
```javascript
// 滚动监听懒加载或吸顶
window.addEventListener("scroll", throttle(() => {
    checkInView();
}, 100));
```

---

**基本写法：按钮点击防抖**
`<按钮>.addEventListener("click", <防抖>(<回调>, <等待>))`
```javascript
// 防止按钮多次点击重复提交
btn.addEventListener("click", debounce(submit, 500));
```

---

**基本写法：拖拽节流**
`<元素>.addEventListener("mousemove", <节流>(<回调>, <等待>))`
```javascript
// 拖拽时降低 mousemove 触发频率
el.addEventListener("mousemove", throttle(update, 16));
```

---

## requestAnimationFrame 节流

**基本写法：rAF 节流**
`function <rAF节流>(<回调>) { }`
```javascript
// 基于刷新率节流适合动画场景
function rafThrottle(fn) {
    let locked = false;
    return function (...args) {
        if (locked) return;
        locked = true;
        requestAnimationFrame(() => { fn.apply(this, args); locked = false; });
    };
}
```

---

## 对象方法上下文

**基本写法：对象方法防抖**
`<对象>.<方法> = <防抖>(function () { }, <等待>)`
```javascript
// 保持 this 指向对象本身
const obj = {
    value: 1,
    log: debounce(function () { console.log(this.value); }, 300)
};
```

---

## 高级模式

**基本写法：返回 Promise 防抖**
`function <防抖异步>(<异步函数>, <等待>) { }`
```javascript
// 防抖并返回 Promise 支持异步
function debounceAsync(fn, wait) {
    let timer, rejectPrev;
    return (...args) => {
        clearTimeout(timer);
        if (rejectPrev) rejectPrev("cancelled");
        return new Promise((resolve, reject) => {
            rejectPrev = reject;
            timer = setTimeout(() => fn(...args).then(resolve, reject), wait);
        });
    };
}
```

---

**基本写法：组合防抖与节流**
`<节流>(<防抖>(<函数>, <短等待>), <长等待>)`
```javascript
// 既限制频率又保证停止后触发
const handler = throttle(debounce(save, 100), 1000);
```

---

## 实用工具

**基本写法：lodash 风格防抖**
`import { debounce } from "<lodash>"`
```javascript
// lodash 提供完整防抖实现
import { debounce } from "lodash";
const fn = debounce(search, 300, { leading: false, trailing: true });
```

---

**基本写法：lodash 风格节流**
`import { throttle } from "<lodash>"`
```javascript
// lodash 提供完整节流实现
import { throttle } from "lodash";
const fn = throttle(scroll, 100, { leading: true, trailing: true });
```

---

## 取消与挂起

**基本写法：组件卸载时取消**
`<防抖函数>.cancel()`
```javascript
// 防止组件卸载后回调执行
const handler = debounce(fetch, 300);
onUnmounted(() => handler.cancel());
```

---

**基本写法：Vue 中使用防抖**
`const <方法> = <防抖>(<回调>, <等待>)`
```javascript
// Vue 组合式 API 中防抖
import { onUnmounted } from "vue";
const search = debounce(q => fetch(q), 300);
onUnmounted(() => search.cancel());
```
