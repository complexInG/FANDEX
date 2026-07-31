# gh label 与 alias/config 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 标签管理

**基本用法:列出标签**
`gh label list`

```bash
# 列出仓库标签
gh label list

# 按名称搜索
gh label list --search bug
```

---

**基本用法:创建标签**
`gh label create <名称>`

```bash
# 创建带颜色与描述的标签
gh label create "type:bug" --color "D73A4A" --description "Bug 问题"

# 从已有仓库复制所有标签
gh label clone owner/template-repo
```

---

**基本用法:编辑与删除**
`gh label edit <名称>`

```bash
# 修改标签颜色
gh label edit bug --color "B60205"

# 重命名标签
gh label edit bug --new-name "type:bug"

# 删除标签
gh label delete "type:bug" --yes
```

---

## 命令别名

**基本用法:设置别名**
`gh alias set <别名> <命令>`

```bash
# 创建常用命令别名
gh alias set co "pr checkout"

# 创建带 shell 的别名
gh alias set vp "pr view --web" --shell

# 列出所有别名
gh alias list

# 删除别名
gh alias delete co
```

---

## 配置管理

**基本用法:查看配置**
`gh config list`

```bash
# 列出所有配置
gh config list

# 查看单项配置
gh config get editor
```

---

**基本用法:设置配置**
`gh config set <键> <值>`

```bash
# 设置默认编辑器
gh config set editor "code --wait"

# 设置默认 Git 协议
gh config set git_protocol ssh

# 设置默认分页器
gh config set pager less
```

---

**基本用法:清理缓存**
`gh config clear-cache`

```bash
# 清除 CLI 缓存
gh config clear-cache
```

---