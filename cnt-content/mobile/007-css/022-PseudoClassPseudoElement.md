# CSS 伪类与伪元素速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 链接与交互伪类

**基本写法：:link 未访问链接**
`a:link { }`
```css
/* 未访问链接样式 */
a:link {
  color: blue;
}
```

---

**基本写法：:visited 已访问链接**
`a:visited { }`
```css
/* 已访问链接样式 */
a:visited {
  color: purple;
}
```

---

**基本写法：:hover 悬停**
`<选择器>:hover { }`
```css
/* 鼠标悬停样式 */
.button:hover {
  background: #2980b9;
}
```

---

**基本写法：:active 激活**
`<选择器>:active { }`
```css
/* 鼠标按下样式 */
.button:active {
  transform: scale(0.95);
}
```

---

**基本写法：:focus 获得焦点**
`<选择器>:focus { }`
```css
/* 获得焦点样式 */
input:focus {
  border-color: #3498db;
  outline: none;
}
```

---

**基本写法：:focus-visible 键盘焦点**
`<选择器>:focus-visible { }`
```css
/* 仅键盘聚焦时显示焦点框 */
input:focus-visible {
  outline: 2px solid #3498db;
}
```

---

**基本写法：:focus-within 子元素聚焦**
`<选择器>:focus-within { }`
```css
/* 子元素获得焦点时父元素样式 */
.form:focus-within {
  border-color: #3498db;
}
```

---

## 表单伪类

**基本写法：:checked 选中状态**
`input:checked { }`
```css
/* 复选框选中样式 */
input:checked + label {
  color: #27ae60;
}
```

---

**基本写法：:disabled 禁用**
`input:disabled { }`
```css
/* 禁用输入框样式 */
input:disabled {
  background: #f0f0f0;
  cursor: not-allowed;
}
```

---

**基本写法：:enabled 可用**
`input:enabled { }`
```css
/* 可用输入框样式 */
input:enabled {
  background: white;
}
```

---

**基本写法：:required 必填**
`input:required { }`
```css
/* 必填字段样式 */
input:required {
  border-left: 3px solid #e74c3c;
}
```

---

**基本写法：:valid 有效**
`input:valid { }`
```css
/* 校验通过样式 */
input:valid {
  border-color: #27ae60;
}
```

---

**基本写法：:invalid 无效**
`input:invalid { }`
```css
/* 校验失败样式 */
input:invalid {
  border-color: #e74c3c;
}
```

---

**基本写法：:placeholder-shown 占位显示**
`input:placeholder-shown { }`
```css
/* 输入框为空显示占位符时 */
input:placeholder-shown {
  background: #fafafa;
}
```

---

**基本写法：:read-only 只读**
`input:read-only { }`
```css
/* 只读输入框样式 */
input:read-only {
  background: #f5f5f5;
}
```

---

## 结构伪类

**基本写法：:first-child 第一个子元素**
`<选择器>:first-child { }`
```css
/* 第一个列表项样式 */
li:first-child {
  font-weight: bold;
}
```

---

**基本写法：:last-child 最后一个子元素**
`<选择器>:last-child { }`
```css
/* 最后一个列表项样式 */
li:last-child {
  border-bottom: none;
}
```

---

**基本写法：:only-child 唯一子元素**
`<选择器>:only-child { }`
```css
/* 父元素唯一子元素样式 */
.icon:only-child {
  margin: 0 auto;
}
```

---

**基本写法：:first-of-type 同类型首个**
`<选择器>:first-of-type { }`
```css
/* 第一个段落样式 */
p:first-of-type {
  font-size: 1.2em;
}
```

---

**基本写法：:last-of-type 同类型末个**
`<选择器>:last-of-type { }`
```css
/* 最后一个段落样式 */
p:last-of-type {
  margin-bottom: 0;
}
```

---

**基本写法：:nth-child 第 N 个子元素**
`<选择器>:nth-child(<n>) { }`
```css
/* 第 2 个子元素 */
li:nth-child(2) {
  color: red;
}
```

---

**基本写法：:nth-child 奇偶**
`<选择器>:nth-child(odd | even) { }`
```css
/* 隔行变色 */
tr:nth-child(even) {
  background: #f9f9f9;
}
```

---

**基本写法：:nth-child 公式**
`<选择器>:nth-child(<公式>) { }`
```css
/* 每 3 个元素选第 1 个 */
li:nth-child(3n+1) {
  color: blue;
}
```

---

**基本写法：:nth-last-child 倒数第 N 个**
`<选择器>:nth-last-child(<n>) { }`
```css
/* 倒数第 2 个子元素 */
li:nth-last-child(2) {
  color: green;
}
```

---

**基本写法：:nth-of-type 同类型第 N 个**
`<选择器>:nth-of-type(<n>) { }`
```css
/* 第 2 个段落 */
p:nth-of-type(2) {
  color: red;
}
```

---

**基本写法：:empty 空元素**
`<选择器>:empty { }`
```css
/* 空段落隐藏 */
p:empty {
  display: none;
}
```

---

**基本写法：:root 根元素**
`:root { }`
```css
/* 定义全局 CSS 变量 */
:root {
  --primary: #3498db;
}
```

---

## 否定与匹配伪类

**基本写法：:not 否定**
`<选择器>:not(<排除选择器>) { }`
```css
/* 非特殊按钮的样式 */
.button:not(.special) {
  background: gray;
}
```

---

**基本写法：:not 多条件否定**
`<选择器>:not(<选择器1>, <选择器2>) { }`
```css
/* 排除多个选择器 */
input:not(:disabled, [type="hidden"]) {
  border: 1px solid #ccc;
}
```

---

**基本写法：:is 匹配任一**
`<选择器>:is(<选择器1>, <选择器2>) { }`
```css
/* 匹配多个标题级别 */
:is(h1, h2, h3) {
  color: #333;
}
```

---

**基本写法：:where 匹配任一（零优先级）**
`<选择器>:where(<选择器1>, <选择器2>) { }`
```css
/* 零优先级匹配便于覆盖 */
:where(.card) .title {
  font-size: 1.2em;
}
```

---

## 状态伪类

**基本写法：:target 目标锚点**
`<选择器>:target { }`
```css
/* 锚点目标高亮 */
.section:target {
  background: #fffacd;
}
```

---

**基本写法：:default 默认选项**
`input:default { }`
```css
/* 默认选中的单选按钮 */
input:default {
  box-shadow: 0 0 0 2px #3498db;
}
```

---

**基本写法：:indeterminate 不确定状态**
`input:indeterminate { }`
```css
/* 不确定状态复选框 */
input:indeterminate {
  background: gray;
}
```

---

## 伪元素

**基本写法：::before 前置内容**
`<选择器>::before { content: <内容>; }`
```css
/* 添加前置图标 */
.link::before {
  content: "→ ";
}
```

---

**基本写法：::after 后置内容**
`<选择器>::after { content: <内容>; }`
```css
/* 添加后置内容 */
.required::after {
  content: " *";
  color: red;
}
```

---

**基本写法：::first-letter 首字母**
`<选择器>::first-letter { }`
```css
/* 段落首字母放大 */
p::first-letter {
  font-size: 2em;
  float: left;
}
```

---

**基本写法：::first-line 首行**
`<选择器>::first-line { }`
```css
/* 段落首行样式 */
p::first-line {
  font-weight: bold;
}
```

---

**基本写法：::selection 选中文本**
`::selection { }`
```css
/* 选中文本样式 */
::selection {
  background: #3498db;
  color: white;
}
```

---

**基本写法：::placeholder 占位符**
`input::placeholder { }`
```css
/* 占位符文本样式 */
input::placeholder {
  color: #999;
}
```

---

**基本写法：::marker 列表标记**
`li::marker { }`
```css
/* 列表项标记样式 */
li::marker {
  color: #3498db;
  font-weight: bold;
}
```

---

**基本写法：::file-selector-button 文件按钮**
`input[type=file]::file-selector-button { }`
```css
/* 文件选择按钮样式 */
input[type=file]::file-selector-button {
  background: #3498db;
  color: white;
  border: none;
  padding: 6px 12px;
}
```

---

## 现代 CSS 伪类（2024+）

**基本写法：:has 父级选择**
`<选择器>:has(<子选择器>) { }`
```css
/* 包含图片的卡片样式 */
.card:has(img) {
  padding: 0;
}
```

---

**基本写法：:has 否定形式**
`<选择器>:not(:has(<子选择器>)) { }`
```css
/* 不包含错误的表单 */
.form:not(:has(.error)) {
  border-color: #27ae60;
}
```

---

**基本写法：:has 多条件**
`<选择器>:has(<选择器1>, <选择器2>) { }`
```css
/* 包含图片或视频的容器 */
.container:has(img, video) {
  aspect-ratio: 16 / 9;
}
```

---

**基本写法：:defined 自定义元素已定义**
`<选择器>:defined { }`
```css
/* 自定义元素定义后显示 */
custom-element:not(:defined) {
  display: none;
}
```

---

**基本写法：:modal 模态框**
`<选择器>:modal { }`
```css
/* 原生模态框样式 */
dialog:modal {
  border: none;
  border-radius: 8px;
}
```

---

**基本写法：:fullscreen 全屏**
`<选择器>:fullscreen { }`
```css
/* 全屏元素样式 */
.video:fullscreen {
  width: 100vw;
  height: 100vh;
}
```

---

**基本写法：:picture-in-picture 画中画**
`<选择器>:picture-in-picture { }`
```css
/* 画中画视频样式 */
video:picture-in-picture {
  border: 2px solid #3498db;
}
```

---

**基本写法：:playing 播放中**
`<选择器>:playing { }`
```css
/* 视频播放时样式 */
video:playing {
  filter: brightness(1.1);
}
```

---

## @scope 作用域（2024+）

**基本写法：@scope 限定作用域**
`@scope (<选择器>) { <规则> }`
```css
/* 限定样式作用范围 */
@scope (.card) {
  .title {
    color: red;
  }
}
```

---

**基本写法：@scope 范围限定**
`@scope (<起>) to (<止>) { }`
```css
/* 限定到 .start 到 .end 之间 */
@scope (.start) to (.end) {
  p {
    color: blue;
  }
}
```
