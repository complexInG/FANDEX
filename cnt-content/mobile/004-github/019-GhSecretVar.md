# gh secret 与变量命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 仓库密钥

**基本用法:设置 Actions 密钥**
`gh secret set <名称>`

```bash
# 交互式输入密钥值
gh secret set DATABASE_URL

# 从字符串设置
gh secret set API_KEY --body "sk-12345"

# 从文件读取
gh secret set DEPLOY_KEY < ~/.ssh/id_rsa

# 从环境变量读取
gh secret set TOKEN --body "$MY_TOKEN"
```

---

**基本用法:列出与删除密钥**
`gh secret list`

```bash
# 列出所有密钥(不显示值)
gh secret list

# 删除密钥
gh secret delete API_KEY
```

---

## 组织与环境密钥

**基本用法:设置组织级密钥**
`gh secret set <名称> --org <组织>`

```bash
# 设置组织密钥
gh secret set DEPLOY_TOKEN --org myorg

# 指定可见仓库
gh secret set TOKEN --org myorg --repos "repo1,repo2"

# 设置环境密钥
gh secret set DB_PASS --env production
```

---

## Codespaces 密钥

**基本用法:Codespaces 密钥**
`gh codespace secret set <名称>`

```bash
# 设置 Codespaces 用户密钥
gh codespace secret set API_KEY --body "sk-xxx"

# 设置组织 Codespaces 密钥
gh codespace secret set TOKEN --org myorg
```

---

## 变量管理

**基本用法:设置 Actions 变量**
`gh variable set <名称>`

```bash
# 设置变量(变量值可见,适合非敏感数据)
gh variable set NODE_ENV --body "production"

# 从文件设置
gh variable set CONFIG < config.json

# 列出变量
gh variable list

# 查看变量值
gh variable get NODE_ENV

# 删除变量
gh variable delete NODE_ENV
```

---