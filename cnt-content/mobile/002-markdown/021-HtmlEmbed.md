# Markdown HTML 内嵌

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础 HTML 嵌入

**基本写法：行内 HTML 标签`
`<tag> <内容> </tag>`
```markdown
# 直接在 markdown 中写 HTML 标签
这是一个 <strong>加粗</strong> 的文本
```

---

**基本写法：块级 HTML 标签`
`<div> <内容> </div>`
```markdown
# 块级 HTML 标签独占一行
<div>
这是 div 包裹的内容
</div>
```

---

**基本写法：HTML 标签嵌套`
`<div><p> <内容> </p></div>`
```markdown
# HTML 标签可嵌套使用
<div>
<p>段落一</p>
<p>段落二</p>
</div>
```

---

## 文本格式化

**基本写法：HTML 加粗`
`<strong> <文本> </strong>`
```markdown
# 用 strong 标签加粗
<strong>重要内容</strong>
```

---

**基本写法：HTML 斜体`
`<em> <文本> </em>`
```markdown
# 用 em 标签表示斜体
<em>强调文本</em>
```

---

**基本写法：HTML 下划线`
`<u> <文本> </u>`
```markdown
# 用 u 标签添加下划线
<u>带下划线的文本</u>
```

---

**基本写法：HTML 删除线`
`<del> <文本> </del>` 或 `<s> <文本> </s>`
```markdown
# 用 del 或 s 标签表示删除线
<del>已废弃</del>
<s>已失效</s>
```

---

**基本写法：HTML 高亮`
`<mark> <文本> </mark>`
```markdown
# 用 mark 标签高亮文本
<mark>关键信息</mark>
```

---

## 颜色与样式

**基本写法：行内颜色`
`<span style="color:<颜色>"> <文本> </span>`
```markdown
# 用 span 加 style 设置颜色
<span style="color:red">红色文本</span>
```

---

**基本写法：背景色`
`<span style="background-color:<颜色>"> <文本> </span>`
```markdown
# 设置文本背景色
<span style="background-color:yellow">黄色背景</span>
```

---

**基本写法：字号`
`<span style="font-size:<大小>"> <文本> </span>`
```markdown
# 修改字体大小
<span style="font-size:20px">大字号</span>
```

---

**基本写法：组合样式`
`<span style="color:<颜色>;font-weight:bold"> <文本> </span>`
```markdown
# 多个样式属性组合
<span style="color:blue;font-weight:bold">蓝色加粗</span>
```

---

## 换行与对齐

**基本写法：强制换行`
`<br>`
```markdown
# 用 br 标签强制换行
第一行<br>第二行
```

---

**基本写法：水平线`
`<hr>`
```markdown
# 用 hr 标签画水平分隔线
内容一
<hr>
内容二
```

---

**基本写法：文本居中`
`<div align="center"> <内容> </div>`
```markdown
# 用 align 属性居中文本
<div align="center">
居中显示
</div>
```

---

**基本写法：右对齐`
`<div align="right"> <内容> </div>`
```markdown
# 文本右对齐
<div align="right">
右对齐文本
</div>
```

---

## 锚点与链接

**基本写法：定义锚点`
`<a id="<锚点>"></a>`
```markdown
# 用 a 标签定义锚点
<a id="section-1"></a>
## 章节一
```

---

**基本写法：HTML 链接`
`<a href="<URL>"> <文本> </a>`
```markdown
# 用 a 标签创建链接
<a href="https://example.com">访问示例</a>
```

---

**基本写法：新窗口打开链接`
`<a href="<URL>" target="_blank"> <文本> </a>`
```markdown
# target="_blank" 在新标签页打开
<a href="https://example.com" target="_blank">新窗口打开</a>
```

---

## 图片扩展

**基本写法：HTML 图片`
`<img src="<URL>" alt="<描述>">`
```markdown
# 用 img 标签插入图片
<img src="logo.png" alt="Logo">
```

---

**基本写法：指定图片尺寸`
`<img src="<URL>" width="<宽>" height="<高>">`
```markdown
# 设置图片宽高
<img src="logo.png" width="200" height="100">
```

---

**基本写法：图片样式`
`<img src="<URL>" style="border:1px solid">`
```markdown
# 给图片添加样式
<img src="logo.png" style="border:1px solid #ccc">
```

---

**基本写法：图片居中`
`<div align="center"><img src="<URL>"></div>`
```markdown
# 用 div 居中图片
<div align="center">
<img src="logo.png">
</div>
```

---

## 折叠内容

**基本写法：折叠区块`
`<details><summary><标题></summary><内容></details>`
```markdown
# 用 details 实现折叠
<details>
<summary>点击展开详情</summary>

这里是折叠的内容

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

**基本写法：嵌套折叠`
`<details><summary><外层>`
`<details><summary><内层>...`
```markdown
# 折叠区块可嵌套
<details>
<summary>外层</summary>
<details>
<summary>内层</summary>
内容
</details>
</details>
```

---

## 提示框

**基本写法：警告框`
`<div class="alert alert-warning"><内容></div>`
```markdown
# 用 div 加 class 实现提示框
<div class="alert alert-warning">
<strong>警告</strong> 注意此风险
</div>
```

---

**基本写法：调用框`
`<blockquote class="warning"><内容></blockquote>`
```markdown
# 用 blockquote 加 class 实现引用框
<blockquote class="warning">
警告内容
</blockquote>
```

---

## 表格扩展

**基本写法：HTML 表格`
`<table><tr><td> <内容> </td></tr></table>`
```markdown
# 用 HTML 实现更复杂的表格
<table>
<tr>
<th>姓名</th>
<th>年龄</th>
</tr>
<tr>
<td>张三</td>
<td>25</td>
</tr>
</table>
```

---

**基本写法：合并单元格`
`<td colspan="<列数>"> <内容> </td>`
```markdown
# 用 colspan 与 rowspan 合并单元格
<table>
<tr>
<td colspan="2">合并两列</td>
</tr>
<tr>
<td>单元格</td>
<td>单元格</td>
</tr>
</table>
```

---

## 视频与媒体

**基本写法：嵌入视频`
`<video src="<URL>" controls></video>`
```markdown
# 用 video 标签嵌入视频
<video src="demo.mp4" controls width="400"></video>
```

---

**基本写法：嵌入音频`
`<audio src="<URL>" controls></audio>`
```markdown
# 用 audio 标签嵌入音频
<audio src="song.mp3" controls></audio>
```

---

**基本写法：嵌入 iframe`
`<iframe src="<URL>"></iframe>`
```markdown
# 用 iframe 嵌入网页
<iframe src="https://example.com" width="600" height="400"></iframe>
```

---

## 注释

**基本写法：HTML 注释`
`<!-- <注释内容> -->`
```markdown
# 用 HTML 注释隐藏内容
<!-- 这是注释不会渲染 -->
```

---

**基本写法：多行注释`
`<!--`
`<多行内容>`
`-->`
```markdown
# 多行注释
<!--
多行
注释内容
-->
```

---

## 键盘按键样式

**基本写法：键盘按键`
`<kbd> <按键> </kbd>`
```markdown
# 用 kbd 标签表示键盘按键
按 <kbd>Ctrl</kbd> + <kbd>C</kbd> 复制
```

---

## 上下标

**基本写法：下标`
`<sub> <内容> </sub>`
```markdown
# 用 sub 标签实现下标
H<sub>2</sub>O
```

---

**基本写法：上标`
`<sup> <内容> </sup>`
```markdown
# 用 sup 标签实现上标
x<sup>2</sup> + y<sup>2</sup>
```

---

## 内联样式

**基本写法：用 style 属性`
`<元素 style="<CSS>">`
```markdown
# 行内 style 属性指定样式
<p style="color:green;font-size:18px">绿色大字</p>
```

---

**基本写法：用 class 属性`
`<元素 class="<类名>">`
```markdown
# 用 class 关联外部 CSS
<div class="highlight">高亮内容</div>
```

---

## 渲染器支持差异

**基本写法：GitHub 支持的 HTML`
`<a> <img> <details> <kbd> 等`
```markdown
# GitHub 支持部分安全 HTML 标签
# 禁用 script、style 标签
```

---

**基本写法：GitLab HTML 过滤`
`允许大部分 HTML 标签`
```markdown
# GitLab 允许更多 HTML 标签与属性
# 包括 style 属性
```

---

**基本写法：Obsidian 完整支持`
`支持所有 HTML 标签与样式`
```markdown
# Obsidian 渲染时保留 HTML 原样
# 支持完整样式属性
```

---

## 注意事项

**基本写法：块级 HTML 前后空行`
`<段落>`
`<div> <内容> </div>`
`<段落>`
```markdown
# 块级 HTML 前后建议留空行
段落

<div>HTML 块</div>

段落
```

---

**基本写法：避免 script 标签`
`多数平台禁用 script`
```markdown
# 多数平台出于安全过滤 script 标签
# 不要依赖 JavaScript 实现
```

---

**基本写法：HTML 与 Markdown 混用`
`<div>`
`<Markdown 内容>`
`</div>`
```markdown
# HTML 块内 Markdown 可能不解析
# 建议复杂格式统一用 HTML 或 Markdown
```

---

## 实战场景

**基本写法：文档头部居中标题`
`<div align="center"><h1> <标题> </h1></div>`
```markdown
# 居中显示项目标题
<div align="center">
<h1>项目名称</h1>
<p>项目简介</p>
</div>
```

---

**基本写法：徽章组合`
`<img src="<徽章URL>">`
```markdown
# 用 img 标签展示多个状态徽章
<img src="https://img.shields.io/badge/build-passing-green">
<img src="https://img.shields.io/badge/version-1.0-blue">
```

---

**基本写法：警告区块`
`<div class="warning"><内容></div>`
```markdown
# 突出显示重要警告
<div class="warning">
<strong>重要</strong> 此功能已弃用
</div>
```
