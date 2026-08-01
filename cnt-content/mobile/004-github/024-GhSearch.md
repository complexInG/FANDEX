# gh search 搜索命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 搜索仓库

**基本用法:搜索仓库**
`gh search repos <查询>`

```bash
# 按关键词搜索仓库
gh search repos "react ui"

# 按语言与 star 数过滤
gh search repos --language=typescript --stars=">1000"

# 按主题过滤
gh search repos --topic=vue --limit 10

# 在指定组织中搜索
gh search repos --owner=microsoft --visibility=public
```

---

## 搜索 Issue 与 PR

**基本用法:搜索 issue**
`gh search issues <查询>`

```bash
# 搜索 open 状态的 bug
gh search issues "memory leak" --state=open --label=bug

# 搜索分配给自己的 issue
gh search issues --assignee=@me

# 搜索某仓库的 issue
gh search issues --repo=owner/repo "crash"
```

---

**基本用法:搜索 PR**
`gh search prs <查询>`

```bash
# 搜索已合并的 PR
gh search prs --merged --author=@me

# 搜索需要审查的 PR
gh search prs --review-requested=@me --open
```

---

## 搜索代码

**基本用法:搜索代码**
`gh search code <查询>`

```bash
# 在所有公开仓库搜索代码
gh search code "useState useEffect"

# 限定仓库与文件名
gh search code "TODO" --repo=owner/repo --filename=*.py

# 限定组织
gh search code "config" --org=myorg --language=go
```

---

## 搜索提交

**基本用法:搜索提交**
`gh search commits <查询>`

```bash
# 搜索提交信息
gh search commits "fix memory leak" --repo=owner/repo

# 按作者搜索
gh search commits --author=zhangsan
```

---

## 通用选项

**基本用法:控制输出**
`gh search <类型> --<选项>`

```bash
# 排序方式
gh search repos react --sort=stars --order=desc

# 输出 JSON
gh search repos react --json fullName,stargazersCount

# 在浏览器中打开搜索结果
gh search repos react --web
```

---