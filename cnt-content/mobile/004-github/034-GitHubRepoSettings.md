# GitHub 仓库设置命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 仓库信息

**基本用法:查看仓库设置**
`gh repo view <仓库>`

```bash
# 查看仓库详情
gh repo view owner/repo

# 以 JSON 输出
gh repo view owner/repo --json name,visibility,defaultBranchRef
```

---

**基本用法:修改仓库设置**
`gh repo edit <仓库>`

```bash
# 修改描述
gh repo edit owner/repo --description "项目描述"

# 修改主页地址
gh repo edit owner/repo --homepage "https://example.com"

# 切换可见性
gh repo edit owner/repo --visibility public
gh repo edit owner/repo --visibility internal

# 启用 issues 与 wiki
gh repo edit owner/repo --enable-issues --enable-wiki

# 关闭项目功能
gh repo edit owner/repo --enable-projects=false
```

---

## 仓库生命周期

**基本用法:归档仓库**
`gh repo archive <仓库>`

```bash
# 把仓库设为只读归档
gh repo archive owner/repo --yes
```

---

**基本用法:取消归档**
`gh repo unarchive <仓库>`

```bash
# 恢复归档仓库为可写
gh repo unarchive owner/repo --yes
```

---

**基本用法:删除仓库**
`gh repo delete <仓库>`

```bash
# 删除仓库(危险操作)
gh repo delete owner/repo --yes
```

---

## 仓库元数据

**基本用法:管理 topics**
`gh repo edit <仓库> --add-topic`

```bash
# 添加 topic 标签
gh repo edit owner/repo --add-topic vue --add-topic frontend

# 移除 topic
gh repo edit owner/repo --remove-topic legacy

# 清空 topics
gh repo edit owner/repo --clear-topics
```

---

## 部署密钥

**基本用法:添加部署密钥**
`gh repo deploy-key add <文件>`

```bash
# 添加只读部署密钥
gh repo deploy-key add ~/.ssh/deploy.pub -t "CI deploy key"

# 添加可写部署密钥
gh repo deploy-key add ~/.ssh/deploy.pub -t "write key" --allow-write

# 列出部署密钥
gh repo deploy-key list

# 删除密钥
gh repo deploy-key delete <key-id>
```

---

## 通过 API 操作

**基本用法:调用 API 修改设置**
`gh api repos/<owner>/<repo> -X PATCH`

```bash
# 修改默认分支
gh api repos/owner/repo -X PATCH -f default_branch=main

# 启用自动删除分支
gh api repos/owner/repo -X PATCH -F delete_branch_on_merge=true
```

---