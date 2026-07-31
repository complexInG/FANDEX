# CSS 容器查询语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 建立容器上下文

**基本写法：声明查询容器**
`container-type: <size|inline-size|normal>;`
```css
/* 设置元素为查询容器 */
.sidebar { container-type: inline-size; }
.card-wrap { container-type: size; }
/* size：可查宽高；inline-size：仅查行向（最常用）；normal：非尺寸容器 */
```

---

**基本写法：命名容器**
`container-name: <名称>;`
```css
/* 给容器命名以便精确查询 */
.layout { container-type: inline-size; container-name: layout; }
.sidebar { container-type: inline-size; container-name: sidebar; }
```

---

**基本写法：容器简写**
`container: <名称> / <类型>;`
```css
/* 一次声明名称与类型 */
.layout { container: layout / inline-size; }
.anon { container: inline-size; }   /* 仅类型，匿名容器 */
```

---

## 容器查询

**基本写法：基本查询**
`@container (<条件>) { ... }`
```css
/* 查询最近的祖先容器 */
.card-wrap { container-type: inline-size; }
@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

---

**基本写法：命名容器查询**
`@container <名称> (<条件>) { ... }`
```css
/* 指定查询某个命名容器 */
.sidebar { container-type: inline-size; container-name: sidebar; }
@container sidebar (min-width: 300px) {
  .menu { display: flex; }
}
```

---

**基本写法：范围查询**
`@container (<min-width>) and (<max-width>)`
```css
/* 多条件组合 */
@container (min-width: 400px) and (max-width: 800px) {
  .card { padding: 20px; }
}
```

---

**基本写法：方向查询**
`@container (orientation: <landscape|portrait>)`
```css
/* 按容器方向应用样式 */
@container (orientation: landscape) {
  .media { flex-direction: row; }
}
```

---

**基本写法：高度查询**
`@container (<min-height>)`
```css
/* 需要 container-type: size 才能查 block 方向 */
.hero { container-type: size; }
@container (min-height: 500px) {
  .hero-title { font-size: 4rem; }
}
```

---

## 容器查询单位

**基本写法：容器相对单位**
`<值><cqw|cqh|cqi|cqb|cqmin|cqmax>`
```css
/* 单位速查 */
/* cqw    容器宽度的 1%        */
/* cqh    容器高度的 1%        */
/* cqi    容器内联尺寸的 1%    */
/* cqb    容器块尺寸的 1%      */
/* cqmin  cqi 与 cqb 较小者    */
/* cqmax  cqi 与 cqb 较大者    */
.title { font-size: clamp(1rem, 5cqi, 3rem); }
.gap { margin: 2cqi; }
```

---

## 样式查询

**基本写法：按自定义属性查询**
`@container style(<属性>: <值>)`
```css
/* 根据容器自定义属性应用样式 */
.theme { container-type: normal; container-name: theme; --theme: dark; }
@container theme style(--theme: dark) {
  .card { background: #222; color: #eee; }
}
```

---

**基本写法：按计算样式查询**
`@container style(<属性>: <值>)`
```css
/* 查询容器计算后的样式值 */
.card-wrap { container-name: card; }
@container card style(font-size: 1.5rem) {
  .title { font-weight: 700; }
}
```

---

## 逻辑组合

**基本写法：and / or / not**
`@container (<条件>) and (<条件>) { ... }`
```css
/* 多条件逻辑 */
@container (min-width: 400px) and (orientation: landscape) {
  .card { display: grid; grid-template-columns: 2fr 1fr; }
}

@container (max-width: 200px) or (orientation: portrait) {
  .card { flex-direction: column; }
}

@container not (min-width: 400px) {
  .card { font-size: 0.9rem; }
}
```

---

## 媒体查询与容器查询对比

**基本写法：视口 vs 容器**
```css
/* 媒体查询：基于视口 */
@media (min-width: 768px) {
  .card { flex-direction: row; }
}

/* 容器查询：基于父容器，组件更可复用 */
.card-wrap { container-type: inline-size; }
@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

---

## 注意事项速查

**基本写法：size 容器需显式高度**
`container-type: size;`
```css
/* size 类型不能从子元素推导高度，否则高度坍缩 */
.hero {
  container-type: size;
  height: 100vh;   /* 必须显式设置高度 */
}
```

---

**基本写法：容器查询后代选择器**
```css
/* @container 内的规则作用于容器后代 */
.card-wrap { container-type: inline-size; }
@container (min-width: 400px) {
  .card .title { font-size: 1.5rem; }
  .card .body { padding: 16px; }
}
```