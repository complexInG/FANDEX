# git log 高级用法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 格式化输出

**基本用法:简洁历史**
`git log --oneline`

```bash
# 每个提交一行显示
git log --oneline

# 限制显示条数
git log --oneline -10
```

---

**基本用法:图形化分支**
`git log --graph`

```bash
# 图形化展示分支合并历史
git log --oneline --graph --all

# 带装饰标签
git log --oneline --graph --decorate
```

---

**基本用法:自定义格式**
`git log --pretty=format:"<格式>"`

```bash
# 自定义字段:哈希 作者 时间 说明
git log --pretty=format:"%h - %an, %ar : %s"

# 完整格式
git log --pretty=format:"%C(yellow)%h%Creset %C(green)%ad%Creset %s" --date=short
```

---

## 过滤条件

**基本用法:按作者筛选**
`git log --author="<名称>"`

```bash
# 按作者过滤
git log --author="zhangsan"

# 按提交说明搜索
git log --grep="fix"
```

---

**基本用法:按时间筛选**
`git log --since=<时间>`

```bash
# 最近 7 天
git log --since="7 days ago"

# 指定日期之后
git log --since="2026-01-01" --until="2026-06-30"

# 按相对时间
git log --since="2 weeks ago" --until="yesterday"
```

---

**基本用法:按文件筛选**
`git log <路径>`

```bash
# 查看某文件的提交历史
git log -- src/auth/login.js

# 显示每次提交改动的统计
git log --stat -- src/

# 显示每次提交的具体差异
git log -p -- package.json
```

---

## 范围与对比

**基本用法:查看分支差异**
`git log <分支1>..<分支2>`

```bash
# 查看 feature 比 main 多的提交
git log main..feature

# 查看两个分支各自独有的提交
git log --left-right main...feature
```

---

**基本用法:查看指定行变更**
`git log -L <起始,结束>:<文件>`

```bash
# 追踪文件中 10-20 行的变更历史
git log -L 10,20:src/utils.js
```

---

## 统计输出

**基本用法:简明统计**
`git log --stat`

```bash
# 显示文件改动统计
git log --stat

# 仅显示数字统计
git log --numstat

# 短统计格式
git log --shortstat
```

---