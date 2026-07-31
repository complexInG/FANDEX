# GitHub Flavored Markdown 扩展

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 删除线

**基本写法：删除线**
`~~<文本>~~`
```markdown
# 双波浪线表示删除线
~~废弃内容~~
```

---

**基本写法：删除线与粗体组合`
`**~~<文本>~~**`
```markdown
# 删除线加粗组合
**~~重要废弃~~**
```

---

## 任务列表

**基本写法：任务列表`
`- [ ] <项>`
```markdown
# GFM 支持可勾选任务列表
- [x] 完成功能
- [ ] 修复 bug
```

---

**基本写法：任务列表嵌套`
`  - [ ] <子项>`
```markdown
# 嵌套任务列表
- [ ] 主任务
  - [x] 子任务一
  - [ ] 子任务二
```

---

## 表格扩展

**基本写法：GFM 表格`
`| <列1> | <列2> |`
`| --- | --- |`
```markdown
# GFM 表格语法
| 名称 | 版本 |
| --- | --- |
| Node | 20 |
| Git | 2.47 |
```

---

**基本写法：表格对齐`
`| :--- | :---: | ---: |`
```markdown
# 用冒号控制列对齐
| 左对齐 | 居中 | 右对齐 |
| :--- | :---: | ---: |
| a | b | c |
```

---

**基本写法：表格内行内代码`
`| \`<代码>\` |`
```markdown
# 表格单元格内可使用行内代码
| 命令 | 说明 |
| --- | --- |
| `git status` | 查看状态 |
```

---

## 自动链接

**基本写法：URL 自动链接`
`<https://example.com>`
```markdown
# 尖括号包裹 URL 转为链接
<https://github.com>
```

---

**基本写法：邮箱自动链接`
`<user@example.com>`
```markdown
# 邮箱地址自动转为 mailto 链接
<alice@example.com>
```

---

**基本写法：裸 URL 自动识别`
`https://example.com`
```markdown
# GFM 自动将裸 URL 转为链接
访问 https://github.com 了解更多
```

---

## 围栏代码块

**基本写法：围栏代码块`
` ```<语言> `
```markdown
# GFM 支持围栏代码块语法
```python
print("hi")
```
```

---

**基本写法：语法高亮`
` ```<语言> `
```markdown
# 指定语言启用语法高亮
```javascript
console.log("hi")
```
```

---

## 引用折行

**基本写法：引用内多段`
`> <段落1>`
`>`
`> <段落2>`
```markdown
# 引用内用空引用行分隔段落
> 第一段
>
> 第二段
```

---

**基本写法：引用嵌套`
`> > <内容>`
```markdown
# 多层引用嵌套
> 外层引用
> > 内层引用
```

---

## 列表扩展

**基本写法：列表内嵌套段落`
`1.  <项>`
`    <续行>`
```markdown
# 列表项内容跨行需缩进
1.  第一项

    续行说明

2.  第二项
```

---

**基本写法：列表内代码块`
`1.  <项>`
`        <代码>`
```markdown
# 列表内代码需 8 空格缩进
1. 示例：

        print("hi")
```

---

## 列表前后空行

**基本写法：列表前空行`
`<段落>`
`(空行)`
`- <项>`
```markdown
# 列表前建议留空行
这是段落。

- 列表项一
- 列表项二
```

---

## 链接引用

**基本写法：定义链接引用`
`[<标识>]: <URL>`
```markdown
# 文档末尾定义链接引用
[GitHub]: https://github.com
```

---

**基本写法：使用链接引用`
`[<文本>][<标识>]`
```markdown
# 引用预定义的链接
访问 [GitHub][GitHub] 仓库
```

---

**基本写法：链接引用带标题`
`[<标识>]: <URL> "<标题>"`
```markdown
# 链接引用追加 title 属性
[Google]: https://google.com "搜索引擎"
```

---

## 禁用与转义

**基本写法：转义星号`
`\*<文本>\*`
```markdown
# 反斜杠转义避免被解析为强调
这里不是 *斜体* 而是 \*字面星号\*
```

---

**基本写法：转义反引号`
`\`<文本>\``
```markdown
# 反斜杠转义反引号
显示 \`code\` 字面文本
```

---

## 警告与提示（GitHub 不支持原生）

**基本写法：用引用模拟提示`
`> **<类型>**: <内容>`
```markdown
# GitHub 用引用加粗体模拟提示框
> **Note**: 这是提示内容
> **Warning**: 这是警告内容
```

---

## 表情符号

**基本写法：emoji 短码`
`:<短码>:`
```markdown
# GFM 支持 emoji 短码
:smile: :rocket: :+1:
```

---

**基本写法：直接使用 emoji 字符`
`<emoji>`
```markdown
# 直接输入 Unicode emoji 字符
完成 享受
```

---

## 用户与 Issue 引用

**基本写法：提及用户`
`@<用户名>`
```markdown
# @ 后跟用户名提及他人
@octocat 请查看
```

---

**基本写法：引用 Issue 与 PR`
`#<编号>`
```markdown
# 自动链接到 issue 与 PR
修复 #123 的回归
关闭 PR #456
```

---

**基本写法：跨仓库引用`
`<用户>/<仓库>#<编号>`
```markdown
# 跨仓库引用 issue
相关 microsoft/vscode#12345
```

---

## 提交 SHA 引用

**基本写法：引用提交哈希`
`<40位哈希>`
```markdown
# 自动链接到提交记录
提交 08103b9f2b6e7fbed517a7e268e4e371d84a9a10 修复此问题
```

---

**基本写法：短 SHA 引用`
`<7位哈希>`
```markdown
# 7 位以上哈希自动识别
参见 abc1234
```

---

## 对比表格（diff）

**基本写法：diff 代码块`
` ```diff `
```markdown
# 用 diff 代码块展示差异
```diff
- old line
+ new line
```
```

---

## 折叠内容

**基本写法：用 HTML details 折叠`
`<details><summary><标题></summary><内容></details>`
```markdown
# GitHub 用 details 标签实现折叠
<details>
<summary>点击展开</summary>

这里是折叠内容

</details>
```

---

**基本写法：默认展开折叠`
`<details open>`
```markdown
# 用 open 属性默认展开
<details open>
<summary>默认展开</summary>
内容
</details>
```

---

## 图片扩展

**基本写法：指定图片宽高`
`<img src="<URL>" width="<宽>" height="<高>">`
```markdown
# 用 HTML img 标签指定尺寸
<img src="logo.png" width="200" height="100">
```

---

**基本写法：图片带链接`
`[![<alt>](<图片URL>)](<链接URL>)`
```markdown
# 图片外层包裹链接
[![Logo](logo.png)](https://example.com)
```

---

## 数学公式扩展

**基本写法：行内公式`
`$<公式>$`
```markdown
# GFM 2022 年起支持 LaTeX 公式
能量 $E = mc^2$
```

---

**基本写法：块级公式`
`$$<公式>$$`
```markdown
# 块级公式独占一行
$$
\int_0^1 x^2 dx = \frac{1}{3}
$$
```

---

## 锚点自动生成

**基本写法：标题锚点`
`## <标题>`
```markdown
# 标题自动生成小写横线锚点
## Quick Start
# 锚点 #quick-start
```

---

**基本写法：链接到锚点`
`[<文本>](#<锚点>)`
```markdown
# 链接到本文档某标题
[快速开始](#quick-start)
```

---

## 渲染器适配

**基本写法：GitHub 渲染规则`
`GFM 规范`
```markdown
# GitHub 遵循 GFM 规范
# 支持上述所有扩展语法
```

---

**基本写法：GitLab 扩展`
`GitLab Flavored Markdown`
```markdown
# GitLab 在 GFM 基础上扩展
# 支持数学公式、Mermaid 图表等
```

---

**基本写法：VS Code 预览`
`内置 Markdown 预览`
```markdown
# VS Code 支持大部分 GFM 语法
# 通过插件可扩展更多功能
```

---

## 注意事项

**基本写法：GFM 与 CommonMark 关系`
`GFM 是 CommonMark 的超集`
```markdown
# GFM 兼容 CommonMark 并扩展
# CommonMark 不支持的扩展可参考本文档
```

---

**基本写法：兼容性检查`
`在目标平台预览验证`
```markdown
# 不同平台支持程度不同
# 建议提交前在目标平台预览
```
