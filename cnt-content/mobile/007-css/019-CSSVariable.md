# CSS 变量自定义属性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本定义与使用

**基本写法：定义自定义属性**
`--<属性名>: <值>;`
```css
/* 在 :root 定义全局变量 */
:root {
  --primary-color: #3498db;
  --font-size: 16px;
}
```

---

**基本写法：使用 var()**
`color: var(--<属性名>);`
```css
/* 引用自定义属性 */
.button {
  color: var(--primary-color);
  font-size: var(--font-size);
}
```

---

**基本写法：带默认值的 var()**
`var(--<属性名>, <默认值>);`
```css
/* 变量未定义时使用默认值 */
.text {
  color: var(--text-color, #333);
}
```

---

**基本写法：嵌套默认值**
`var(--<属性名>, var(--<其他属性>, <默认值>));`
```css
/* 多层回退默认值 */
.text {
  color: var(--theme-color, var(--default-color, black));
}
```

---

## 作用域

**基本写法：全局作用域**
`:root { --<属性名>: <值>; }`
```css
/* :root 定义的变量全局可用 */
:root {
  --spacing: 16px;
}
```

---

**基本写法：局部作用域**
`<选择器> { --<属性名>: <值>; }`
```css
/* 仅在 .card 内有效 */
.card {
  --padding: 24px;
  padding: var(--padding);
}
```

---

**基本写法：作用域覆盖**
`<子选择器> { --<属性名>: <新值>; }`
```css
/* 子作用域覆盖父作用域 */
.card {
  --text-color: black;
}
.card.dark {
  --text-color: white;
}
```

---

**基本写法：媒体查询作用域**
`@media (<条件>) { :root { --<属性名>: <值>; } }`
```css
/* 响应式调整变量值 */
:root {
  --font-size: 18px;
}
@media (max-width: 768px) {
  :root {
    --font-size: 16px;
  }
}
```

---

## 类型化自定义属性

**基本写法：@property 定义类型**
`@property --<属性名> { syntax: <类型>; inherits: <是否继承>; initial-value: <初始值>; }`
```css
/* 定义带类型的自定义属性 */
@property --angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}
```

---

**基本写法：颜色类型**
`@property --<属性名> { syntax: '<color>'; ... }`
```css
/* 颜色类型变量支持动画过渡 */
@property --theme-color {
  syntax: '<color>';
  inherits: true;
  initial-value: #3498db;
}
```

---

**基本写法：长度类型**
`@property --<属性名> { syntax: '<length>'; ... }`
```css
/* 长度类型变量 */
@property --spacing {
  syntax: '<length>';
  inherits: true;
  initial-value: 16px;
}
```

---

**基本写法：整数类型**
`@property --<属性名> { syntax: '<integer>'; ... }`
```css
/* 整数类型变量 */
@property --count {
  syntax: '<integer>';
  inherits: false;
  initial-value: 3;
}
```

---

## 常见用法

**基本写法：主题色系统**
`:root { --<语义名>: <值>; }`
```css
/* 设计令牌语义化命名 */
:root {
  --color-primary: #3498db;
  --color-secondary: #2ecc71;
  --color-danger: #e74c3c;
  --color-text: #333;
  --color-bg: #fff;
}
```

---

**基本写法：暗色主题**
`[data-theme="dark"] { --<属性名>: <值>; }`
```css
/* 通过 data 属性切换暗色主题 */
[data-theme="dark"] {
  --color-text: #fff;
  --color-bg: #1a1a1a;
  --color-primary: #5dade2;
}
```

---

**基本写法：prefers-color-scheme 暗色**
`@media (prefers-color-scheme: dark) { :root { --<属性名>: <值>; } }`
```css
/* 跟随系统暗色模式 */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #fff;
    --color-bg: #1a1a1a;
  }
}
```

---

**基本写法：spacing 比例系统**
`:root { --space-<级数>: <值>; }`
```css
/* 8px 间距比例系统 */
:root {
  --space-1: 0.5rem;
  --space-2: 1rem;
  --space-3: 1.5rem;
  --space-4: 2rem;
  --space-5: 3rem;
}
```

---

**基本写法：字体大小比例**
`:root { --text-<语义名>: <值>; }`
```css
/* 字体大小令牌 */
:root {
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
}
```

---

## 进阶用法

**基本写法：JavaScript 读写**
`element.style.setProperty('<属性名>', <值>);`
```css
/* JS 动态修改变量 */
/* document.documentElement.style.setProperty('--primary', '#ff0000'); */
:root {
  --primary: #3498db;
}
```

---

**基本写法：calc 中使用**
`calc(var(--<属性名>) * <系数>);`
```css
/* 变量参与计算 */
.box {
  width: calc(var(--base-width) * 2);
  padding: calc(var(--spacing) / 2);
}
```

---

**基本写法：变量组合**
`var(--<属性1>) var(--<属性2>);`
```css
/* 多变量组合成完整值 */
.box {
  margin: var(--spacing) var(--spacing-lg);
  border: var(--border-width) solid var(--border-color);
}
```

---

**基本写法：响应式字体**
`font-size: clamp(<最小>, var(--<变量>), <最大>);`
```css
/* 流式响应字体结合变量 */
:root {
  --font-scale: 2vw;
}
h1 {
  font-size: clamp(1.5rem, var(--font-scale) + 1rem, 3rem);
}
```

---

## light-dark() 函数（2024+）

**基本写法：light-dark 自动明暗**
`color: light-dark(<浅色>, <深色>);`
```css
/* 根据配色方案自动切换颜色 */
.text {
  color: light-dark(#333, #fff);
  background: light-dark(#fff, #1a1a1a);
}
```

---

**基本写法：配合 color-scheme**
`color-scheme: light dark;`
```css
/* 声明支持明暗两种配色 */
:root {
  color-scheme: light dark;
}
```

---

## color-mix() 混合颜色

**基本写法：color-mix 混合**
`color: color-mix(in <色彩空间>, <颜色1> <比例>, <颜色2>);`
```css
/* 混合两种颜色 */
.box {
  background: color-mix(in srgb, var(--primary) 50%, white);
}
```

---

**基本写法：基于变量的颜色变体**
`color: color-mix(in srgb, var(--color) <比例>, <其他色>);`
```css
/* 生成颜色的明暗变体 */
.button {
  background: var(--primary);
  border-color: color-mix(in srgb, var(--primary) 80%, black);
}
.button:hover {
  background: color-mix(in srgb, var(--primary) 80%, white);
}
```
