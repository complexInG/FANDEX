# React 可访问性 Accessibility

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 语义化 HTML

**基本写法：使用语义化标签**
`<<语义标签> >`
```tsx
// 提升屏幕阅读器体验
<header><nav>导航</nav></header>
<main><article>正文</article></main>
<footer>页脚</footer>
```

---

**基本写法：button 与 a 区分**
`<button onClick={<处理>}>`
```tsx
// 行为触发用 button 跳转用 a
<button onClick={save}>保存</button>
<a href="/about">关于</a>
```

---

## aria-label 标签

**基本写法：为图标按钮添加标签**
`<button aria-label="<描述>">`
```tsx
// 无文字按钮需可访问名称
<button aria-label="关闭" onClick={close}><IconX /></button>
```

---

## aria-labelledby 引用

**基本写法：用 ID 关联标题**
`<div aria-labelledby="<标题id>">`
```tsx
// 区域由标题描述
<div aria-labelledby="title">
  <h2 id="title">用户信息</h2>
</div>
```

---

## aria-describedby 描述

**基本写法：补充详细描述**
`<input aria-describedby="<提示id>" />`
```tsx
// 输入框补充说明
<input aria-describedby="pwd-tip" type="password" />
<p id="pwd-tip">至少 8 位含数字字母</p>
```

---

## 表单可访问性

**基本写法：label 关联 input**
`<label htmlFor="<id>"> <input id="<id>" />`
```tsx
// 点击 label 聚焦 input
<label htmlFor="email">邮箱</label>
<input id="email" type="email" />
```

---

**基本写法：label 包裹 input**
`<label> <文本> <input /> </label>`
```tsx
// 隐式关联
<label>用户名 <input type="text" /></label>
```

---

**基本写法：必填字段**
`<input required aria-required="true" />`
```tsx
// 标记必填字段
<input required aria-required="true" />
```

---

**基本写法：错误提示**
`<input aria-invalid="true" aria-describedby="<错误id>" />`
```tsx
// 字段错误状态
<input aria-invalid="true" aria-describedby="err" />
<p id="err" role="alert">邮箱格式错误</p>
```

---

## 图像可访问性

**基本写法：img 必须有 alt**
`<img src="<路径>" alt="<描述>" />`
```tsx
// 装饰性图片用空 alt
<img src="/bg.jpg" alt="" />
<img src="/logo.png" alt="公司标志" />
```

---

**基本写法：role 处理装饰图**
`<img alt="" role="presentation" />`
```tsx
// 屏幕阅读器跳过
<img src="/deco.png" alt="" role="presentation" />
```

---

## 键盘导航

**基本写法：保证 tab 顺序合理**
`<button>自然 tab 顺序</button>`
```tsx
// DOM 顺序即 tab 顺序
<div>
  <button>1</button>
  <button>2</button>
</div>
```

---

**基本写法：tabindex 控制焦点**
`<div tabIndex={0}>可聚焦</div>`
```tsx
// tabindex 0 表示可聚焦 tabindex -1 表示仅 JS 可聚焦
<div tabIndex={0}>自定义可聚焦区域</div>
```

---

**基本写法：处理 Enter 与 Space**
`onKeyDown={(e) => { if (e.key === 'Enter') <处理>; }}`
```tsx
// 自定义按钮需处理键盘事件
<div role="button" tabIndex={0} onKeyDown={e => {
  if (e.key === 'Enter' || e.key === ' ') activate();
}}>
```

---

## 焦点管理

**基本写法：弹窗打开聚焦**
`useEffect(() => <ref>.current.focus(), [])`
```tsx
// 模态框打开自动聚焦
useEffect(() => inputRef.current.focus(), []);
```

---

**基本写法：focus trap 焦点陷阱**
`onKeyDown={(e) => { if (e.key === 'Tab') <限制>; }}`
```tsx
// 弹窗内循环焦点
function trapFocus(e, container) {
  if (e.key !== 'Tab') return;
  // 限制在容器内
}
```

---

**基本写法：关闭后恢复焦点**
`const <lastFocused> = document.activeElement;`
```tsx
// 关闭弹窗后焦点回到触发按钮
const trigger = document.activeElement;
// 关闭时 trigger.focus()
```

---

## 隐藏内容

**基本写法：仅视觉隐藏保留可访问**
`className="sr-only"`
```tsx
// 屏幕阅读器可见视觉隐藏
<span className="sr-only">附加说明</span>
```

---

**基本写法：aria-hidden 隐藏装饰**
`<div aria-hidden="true">`
```tsx
// 装饰元素对辅助技术隐藏
<div aria-hidden="true"><Decoration /></div>
```

---

## role 角色

**基本写法：自定义组件标注角色**
`<div role="<角色>">`
```tsx
// 自定义下拉框标注 listbox
<div role="listbox">
  <div role="option" aria-selected="true">选项</div>
</div>
```

---

**基本写法：dialog 角色**
`<div role="dialog" aria-modal="true">`
```tsx
// 模态框角色
<div role="dialog" aria-modal="true">
  <h2>标题</h2>
</div>
```

---

## 动态通知 aria-live

**基本写法：实时区域播报变化**
`<div aria-live="polite">`
```tsx
// 异步提示礼貌播报
<div aria-live="polite">{message}</div>
```

---

**基本写法：assertive 紧急播报**
`<div aria-live="assertive" role="alert">`
```tsx
// 错误立即播报
<div role="alert" aria-live="assertive">{error}</div>
```

---

## 跳过导航链接

**基本写法：skip to main content**
`<a href="#<主内容id>" className="skip-link">跳到主内容</a>`
```tsx
// 键盘用户快速跳过导航
<a href="#main" className="skip-link">跳到主内容</a>
<main id="main">...</main>
```

---

## 颜色对比度

**基本写法：保证文字与背景对比度**
`color: <深色>; background: <浅色>;`
```tsx
// WCAG AA 标准对比度 4.5:1
<span style={{ color: '#333', background: '#fff' }}>文本</span>
```

---

## 焦点可见样式

**基本写法：保留 outline 焦点环**
`<button>默认 outline 可见</button>`
```tsx
// 不要移除 outline 提供替代方案
button:focus-visible { outline: 2px solid blue; }
```

---

## 表格可访问性

**基本写法：使用 th 与 scope**
`<th scope="col">`
```tsx
// 表头关联单元格
<table>
  <tr><th scope="col">姓名</th><th scope="col">年龄</th></tr>
  <tr><td>张三</td><td>20</td></tr>
</table>
```

---

## 动画与运动

**基本写法：尊重 prefers-reduced-motion**
`const <reduce> = matchMedia('(prefers-reduced-motion: reduce)').matches`
```tsx
// 用户偏好减少动画
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reduce) animate();
```

---

## ESLint 可访问性插件

**基本写法：安装 eslint-plugin-jsx-a11y**
`npm install -D eslint-plugin-jsx-a11y`
```bash
# 静态检测可访问性问题
npm install -D eslint-plugin-jsx-a11y
```

---

**基本写法：配置规则**
`plugins: ['jsx-a11y']`
```json
// .eslintrc
{
  "plugins": ["jsx-a11y"],
  "extends": ["plugin:jsx-a11y/recommended"]
}
```

---

## 测试可访问性

**基本写法：使用 jest-axe 检测**
`expect(await axe(<容器>)).toHaveNoViolations()`
```tsx
// 自动化无障碍测试
import { axe } from 'jest-axe';
const results = await axe(container);
expect(results).toHaveNoViolations();
```
