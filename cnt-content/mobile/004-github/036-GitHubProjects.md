# GitHub Projects 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 项目管理

**基本用法:创建项目**
`gh project create`

```bash
# 创建组织级项目
gh project create --owner myorg --title "Q3 Roadmap" --format json

# 创建用户级项目
gh project create --owner @me --title "Personal Tasks"
```

---

**基本用法:查看项目**
`gh project view <编号>`

```bash
# 查看项目详情(按编号)
gh project view 1 --owner myorg

# 列出项目
gh project list --owner myorg

# 在浏览器中打开
gh project view 1 --owner myorg --web
```

---

**基本用法:编辑与关闭**
`gh project edit <编号>`

```bash
# 修改项目标题
gh project edit 1 --owner myorg --title "New Title"

# 关闭项目
gh project close 1 --owner myorg

# 重新打开
gh project reopen 1 --owner myorg

# 删除项目
gh project delete 1 --owner myorg
```

---

## 字段管理

**基本用法:添加字段**
`gh project field-create`

```bash
# 创建单选字段
gh project field-create 1 --owner myorg --name "Priority" --data-type SINGLE_SELECT --options "P0,P1,P2"

# 创建文本字段
gh project field-create 1 --owner myorg --name "Notes" --data-type TEXT

# 列出字段
gh project field-list 1 --owner myorg
```

---

## 添加项目条目

**基本用法:添加 issue/pr 到项目**
`gh project item-add <项目号>`

```bash
# 把 issue 加入项目
gh project item-add 1 --owner myorg --url https://github.com/owner/repo/issues/42

# 查看 items
gh project item-list 1 --owner myorg

# 修改字段值
gh project item-edit --id <item-id> --field-id <field-id> --project-id <project-id> --text "done"

# 从项目移除
gh project item-delete <item-id> --project-id <project-id>
```

---

## 通过 API 操作

**基本用法:GraphQL 操作项目**
`gh api graphql`

```bash
# 查询项目信息
gh api graphql -f query='
query {
  user(login: "username") {
    projectV2(number: 1) {
      title
      items(first: 10) {
        nodes { id content { ... on Issue { title } } }
      }
    }
  }
}'
```

---