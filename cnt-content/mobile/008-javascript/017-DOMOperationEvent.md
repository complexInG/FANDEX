# JavaScript DOM 操作与事件 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 节点获取

**基本写法：getElementById**
`document.getElementById(<id>)`
```javascript
// 通过 ID 获取单个元素
let el = document.getElementById("app");
```

---

**基本写法：querySelector**
`document.querySelector(<选择器>)`
```javascript
// 通过 CSS 选择器获取首个匹配元素
let el = document.querySelector(".item");
```

---

**基本写法：querySelectorAll**
`document.querySelectorAll(<选择器>)`
```javascript
// 获取所有匹配元素返回 NodeList
let els = document.querySelectorAll(".item");
```

---

## 节点创建

**基本写法：createElement**
`document.createElement(<标签名>)`
```javascript
// 创建元素节点
let div = document.createElement("div");
```

---

**基本写法：createTextNode**
`document.createTextNode(<文本>)`
```javascript
// 创建文本节点
let text = document.createTextNode("hello");
```

---

**基本写法：DocumentFragment 批量插入**
`document.createDocumentFragment()`
```javascript
// 使用片段批量插入减少重排
let frag = document.createDocumentFragment();
items.forEach(item => {
    let li = document.createElement("li");
    li.textContent = item;
    frag.appendChild(li);
});
list.appendChild(frag);
```

---

## 节点插入与删除

**基本写法：appendChild**
`<父节点>.appendChild(<节点>)`
```javascript
// 在末尾追加子节点
document.body.appendChild(div);
```

---

**基本写法：insertBefore**
`<父节点>.insertBefore(<新节点>, <参考节点>)`
```javascript
// 在参考节点前插入
parent.insertBefore(newNode, refNode);
```

---

**基本写法：removeChild**
`<父节点>.removeChild(<节点>)`
```javascript
// 移除子节点
parent.removeChild(child);
```

---

**基本写法：replaceChild**
`<父节点>.replaceChild(<新节点>, <旧节点>)`
```javascript
// 替换子节点
parent.replaceChild(newNode, oldNode);
```

---

## 现代节点 API

**基本写法：append**
`<父节点>.append(<节点或文本>)`
```javascript
// 追加多个节点或文本字符串
parent.append(node1, "text", node2);
```

---

**基本写法：prepend**
`<父节点>.prepend(<节点或文本>)`
```javascript
// 在开头插入
parent.prepend(newNode);
```

---

**基本写法：before 与 after**
`<节点>.before(<节点>)`
```javascript
// 在节点前或后插入兄弟节点
el.before(newNode);
el.after(anotherNode);
```

---

**基本写法：remove**
`<节点>.remove()`
```javascript
// 节点自移除
el.remove();
```

---

**基本写法：replaceWith**
`<节点>.replaceWith(<新节点>)`
```javascript
// 节点自替换
oldEl.replaceWith(newEl);
```

---

## 属性操作

**基本写法：getAttribute setAttribute**
`<元素>.setAttribute(<名称>, <值>)`
```javascript
// 读写 HTML 属性
el.setAttribute("data-id", "1");
let id = el.getAttribute("data-id");
```

---

**基本写法：dataset 自定义属性**
`<元素>.dataset.<名称>`
```javascript
// 读写 data-* 自定义属性
el.dataset.userId = "42";
let id = el.dataset.userId;
```

---

**基本写法：hasAttribute removeAttribute**
`<元素>.removeAttribute(<名称>)`
```javascript
// 检查与移除属性
el.hasAttribute("disabled");
el.removeAttribute("disabled");
```

---

## classList 操作

**基本写法：add remove**
`<元素>.classList.add(<类名>)`
```javascript
// 添加移除类名
el.classList.add("active");
el.classList.remove("hidden");
```

---

**基本写法：toggle**
`<元素>.classList.toggle(<类名>)`
```javascript
// 切换类名存在则移除否则添加
el.classList.toggle("open");
```

---

**基本写法：contains**
`<元素>.classList.contains(<类名>)`
```javascript
// 判断是否包含类名
if (el.classList.contains("active")) {}
```

---

## 样式操作

**基本写法：内联样式**
`<元素>.style.<属性> = <值>`
```javascript
// 读写内联样式需用驼峰命名
el.style.backgroundColor = "#fff";
```

---

**基本写法：getComputedStyle**
`window.getComputedStyle(<元素>)`
```javascript
// 获取最终计算样式
let style = window.getComputedStyle(el);
let color = style.color;
```

---

**基本写法：cssText 批量设置**
`<元素>.style.cssText = "<样式字符串>"`
```javascript
// 批量设置内联样式
el.style.cssText = "color:red;font-size:14px;";
```

---

## 事件绑定

**基本写法：addEventListener**
`<元素>.addEventListener(<事件>, <回调>, [<选项>])`
```javascript
// 添加事件监听器
el.addEventListener("click", e => {});
```

---

**基本写法：removeEventListener**
`<元素>.removeEventListener(<事件>, <回调>)`
```javascript
// 移除事件监听需同一回调引用
el.removeEventListener("click", handler);
```

---

**基本写法：once 选项**
`<元素>.addEventListener(<事件>, <回调>, { once: true })`
```javascript
// once 表示只触发一次后自动移除
el.addEventListener("click", fn, { once: true });
```

---

**基本写法：capture 捕获阶段**
`<元素>.addEventListener(<事件>, <回调>, { capture: true })`
```javascript
// 在捕获阶段触发
el.addEventListener("click", fn, { capture: true });
```

---

**基本写法：passive 提升滚动性能**
`<元素>.addEventListener(<事件>, <回调>, { passive: true })`
```javascript
// passive 声明不调用 preventDefault 优化滚动
window.addEventListener("touchmove", fn, { passive: true });
```

---

## 事件对象

**基本写法：preventDefault**
`<事件>.preventDefault()`
```javascript
// 阻止默认行为如表单提交链接跳转
a.addEventListener("click", e => e.preventDefault());
```

---

**基本写法：stopPropagation**
`<事件>.stopPropagation()`
```javascript
// 阻止事件冒泡
el.addEventListener("click", e => e.stopPropagation());
```

---

**基本写法：stopImmediatePropagation**
`<事件>.stopImmediatePropagation()`
```javascript
// 阻止冒泡并阻止同元素其他监听器
el.addEventListener("click", e => e.stopImmediatePropagation());
```

---

## 事件委托

**基本写法：事件委托模式**
`<父节点>.addEventListener(<事件>, <回调>)`
```javascript
// 利用冒泡在父节点统一处理
list.addEventListener("click", e => {
    let item = e.target.closest(".item");
    if (item) handle(item);
});
```

---

**基本写法：closest 匹配祖先**
`<元素>.closest(<选择器>)`
```javascript
// 从当前元素向上查找匹配选择器的最近祖先
let card = e.target.closest(".card");
```

---

## 自定义事件

**基本写法：CustomEvent**
`new CustomEvent(<名称>, { detail: <数据> })`
```javascript
// 创建带数据的自定义事件
let evt = new CustomEvent("login", { detail: { user: "Tom" } });
el.dispatchEvent(evt);
```

---

**基本写法：dispatchEvent**
`<元素>.dispatchEvent(<事件>)`
```javascript
// 同步派发事件触发监听器
el.dispatchEvent(new Event("ready"));
```

---

## 遍历与查找

**基本写法：parentNode parentElement**
`<元素>.parentElement`
```javascript
// 获取父节点
let parent = el.parentElement;
```

---

**基本写法：children childNodes**
`<元素>.children`
```javascript
// children 返回元素集合 childNodes 含文本节点
let kids = el.children;
```

---

**基本写法：nextElementSibling**
`<元素>.nextElementSibling`
```javascript
// 获取下一个兄弟元素节点
let next = el.nextElementSibling;
```

---

## MutationObserver

**基本写法：观察 DOM 变化**
`new MutationObserver(<回调>)`
```javascript
// 监听子节点属性变化
let observer = new MutationObserver(muts => {});
observer.observe(el, { childList: true, subtree: true });
```

---

**基本写法：disconnect 断开**
`<observer>.disconnect()`
```javascript
// 停止观察
observer.disconnect();
```

---

## IntersectionObserver

**基本写法：可见性观察**
`new IntersectionObserver(<回调>, [<选项>])`
```javascript
// 监听元素进入视口用于懒加载
let io = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (e.isIntersecting) loadImage(e.target);
    });
});
io.observe(img);
```

---

**基本写法：rootMargin**
`new IntersectionObserver(<回调>, { rootMargin: "<边距>" })`
```javascript
// 提前预加载设置根边距
let io = new IntersectionObserver(fn, { rootMargin: "100px" });
```

---

## ResizeObserver

**基本写法：尺寸变化观察**
`new ResizeObserver(<回调>)`
```javascript
// 监听元素尺寸变化
let ro = new ResizeObserver(entries => {
    entries.forEach(e => console.log(e.contentRect.width));
});
ro.observe(el);
```

---

## 实用模式

**基本写法：事件委托结合 dataset**
`<父节点>.addEventListener(<事件>, <回调>)`
```javascript
// 通过 dataset 传递上下文数据
list.addEventListener("click", e => {
    let item = e.target.closest("[data-id]");
    if (item) console.log(item.dataset.id);
});
```

---

**基本写法：批量绑定事件**
`<元素列表>.forEach(<元素> => <元素>.addEventListener(<事件>, <回调>))`
```javascript
// 为多个元素绑定相同事件
document.querySelectorAll(".btn")
    .forEach(btn => btn.addEventListener("click", onClick));
```
