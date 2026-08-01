# Markdown 代码块高级用法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础围栏代码块

**基本写法：基础代码块**
` ``` `
`<代码>`
` ``` `
````markdown
# 用三个反引号包裹代码
```
plain text
```
````

---

**基本写法：指定语言高亮**
` ```<语言> `
`<代码>`
` ``` `
````markdown
# 围栏后紧跟语言名
```python
print("hello")
```
````

---

**基本写法：用波浪号围栏**
`~~~<语言>`
`<代码>`
`~~~`
````markdown
# 波浪号同样可作为围栏
~~~javascript
console.log("hi")
~~~
````

---

## 嵌套代码块

**基本写法：四反引号外层围栏**
` ```` `
` ``` `
`<代码>`
` ``` `
` ```` `
`````markdown
# 外层用更多反引号实现嵌套
````markdown
```python
print("hello")
```
````
`````

---

**基本写法：五反引号围栏**
` ````` `
`<内部内容>`
` ````` `
``````markdown
# 多层嵌套用更多反引号
`````markdown
````javascript
```js
nested code
```
````
`````
``````

---

## 行高亮

**基本写法：高亮单行**
` ```<语言>{<行号>} `
````markdown
# 高亮第 2 行
```javascript{2}
function hello() {
  console.log("hi");
  return true;
}
```
````

---

**基本写法：高亮多行**
` ```<语言>{<行1>,<行2>} `
````markdown
# 同时高亮多行
```python{1,3}
import os
import sys
print(sys.path)
```
````

---

**基本写法：高亮行范围**
` ```<语言>{<起>-<止>} `
````markdown
# 高亮 2 到 4 行
```javascript{2-4}
function a() {}
function b() {}
function c() {}
function d() {}
```
````

---

**基本写法：组合行号与范围**
` ```<语言>{<行1>,<起>-<止>} `
````markdown
# 同时高亮单行与范围
```python{1,3-5}
import os
import sys
def main():
    print("hi")
    return
```
````

---

**基本写法：相对行高亮**
` ```<语言>{<行号>}` 配合标注 `
````markdown
# Vue/Docusaurus 等支持相对行高亮
```javascript{2}{lines: true}
const a = 1;
const b = 2;
const c = 3;
```
````

---

## 行号显示

**基本写法：开启行号**
` ```<语言> showLineNumbers `
````markdown
# Docusaurus 等支持显式行号
```javascript showLineNumbers
const a = 1;
const b = 2;
```
````

---

**基本写法：从指定行开始**
` ```<语言> showLineNumbers{<起始>} `
````markdown
# 行号从指定数字开始
```javascript showLineNumbers{10}
const a = 1;
const b = 2;
```
````

---

**基本写法：全局开启行号**
` ```<语言>{行号} `
````markdown
# 部分渲染器默认显示行号
```python
print("默认带行号")
```
````

---

## 代码块标题

**基本写法：Docusaurus 标题**
` ```<语言> title="<文件名>" `
````markdown
# 用 title 属性标注文件名
```javascript title="src/index.js"
export default function () {
  return null;
}
```
````

---

**基本写法：标题加行高亮**
` ```<语言> title="<文件名>" {<行>} `
````markdown
# 同时指定标题与高亮
```python title="utils.py" {3}
def add(a, b):
    return a + b
```
````

---

**基本写法：Vue 标题语法**
` ```<语言>[vue] `
````markdown
# VuePress 风格的标题写法
```javascript[utils.js]
export const add = (a, b) => a + b
```
````

---

## 代码折叠

**基本写法：Docusaurus 折叠**
` ```<语言> showLineNumbers collapse `
````markdown
# 折叠长代码块
```javascript {1-2} collapse
function longFunc() {
  // 多行实现
}
```
````

---

**基本写法：MkDocs 折叠**
` ```<语言> linenums="<起始>" hl_lines="<行>" `
````markdown
# MkDocs 风格的折叠与高亮
```python linenums="1" hl_lines="2"
import os
import sys
```
````

---

## 复制按钮

**基本写法：Docusaurus 复制按钮**
` ```<语言> `
````markdown
# 默认提供复制按钮
```javascript
const x = 1;
```
````

---

## 代码组

**基本写法：Docusaurus 代码组**
` <CodeBlock language="<语言>"> `
````markdown
# 多语言切换代码组
```jsx
export default function App() {
  return <div />;
}
```

```tsx
export default function App(): JSX.Element {
  return <div />;
}
```
````

---

**基本写法：MkDocs 选项卡**
` === "tab1"`
`     ```<语言>`
`     <代码>`
`     ````
````markdown
# MkDocs Material 多语言选项卡
=== "JavaScript"

    ```js
    console.log("hi")
    ```

=== "Python"

    ```python
    print("hi")
    ```
````

---

## 代码块内特殊字符

**基本写法：转义反引号**
` ``` `
`包含 ` 反引号`
` ``` `
````markdown
# 围栏内反引号无需转义
```
这个符号是 ` 反引号
```
````

---

**基本写法：包含围栏字符**
` ```` `
` ``` `
`内部用三个反引号`
` ``` `
` ```` `
````markdown
# 外层用更多反引号包裹
````markdown
```python
print("nested")
```
````
````

---

## Diff 高亮

**基本写法：diff 语言高亮**
` ```diff `
`+ <新增>`
`- <删除>`
````markdown
# 用 diff 标记增删行
```diff
- const old = "v1";
+ const new = "v2";
```
````

---

**基本写法：行内 diff 标记**
` ```<语言> diff `
````markdown
# 部分渲染器支持 diff 与语言组合
```javascript diff
- const a = 1;
+ const a = 2;
```
````

---

## 注释与行内标注

**基本写法：代码内注释**
` ```<语言> `
`<代码> // <注释>`
````markdown
# 代码块内正常写注释
```javascript
function add(a, b) { // 求和函数
  return a + b;
}
```
````

---

**基本写法：高亮注释标记**
` ```<语言> {<行>}`
````markdown
# 通过行高亮突出注释行
```python {2}
def main():
    # 这里是关键步骤
    return True
```
````

---

## 行内代码

**基本写法：行内代码**
`` `<代码> ``
```markdown
# 单反引号包裹行内代码
使用 `print()` 函数
```

---

**基本写法：行内代码含反引号`
`` `` ` `` ``
```markdown
# 用双反引号包裹含反引号的内容
输出 ` 反引号符号
```

---

**基本写法：多反引号行内代码`
`` `` `<代码>` `` ``
```markdown
# 双反引号实现含反引号的行内代码
`` `print()` ``
```

---

## 代码块缩进式

**基本写法：缩进式代码块`
`    <代码>`
```markdown
# 4 空格缩进表示代码块
    indented code
    second line
```

---

**基本写法：缩进式与列表混合`
`1. 列表项`
`       <代码>`
```markdown
# 列表内代码需 8 空格缩进
1.  示例代码：

        print("hi")
```

---

## 注意事项

**基本写法：语言名称小写**
` ```<语言小写> `
````markdown
# 语言名建议用小写
```python
# 正确写法
```
````

---

**基本写法：围栏前后空行`
`<段落>`
` ```<语言> `
`<代码>`
` ``` `
```markdown
# 围栏代码块前后建议留空行
这是段落。

```python
print("hi")
```
```

---

**基本写法：避免解析错误`
` ```<语言> `
`无尾随空格`
` ``` `
````markdown
# 围栏后不要加多余空格
```python
print("hi")
```
````
