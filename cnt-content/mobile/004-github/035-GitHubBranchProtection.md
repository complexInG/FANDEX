# GitHub 分支保护命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 通过 API 配置保护规则

**基本用法:设置分支保护**
`gh api repos/<owner>/<repo>/branches/<分支>/protection -X PUT`

```bash
# 要求 PR 评审再合并
gh api repos/owner/repo/branches/main/protection -X PUT \
  --input - <<'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["CI / build"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "dismiss_stale_reviews": true
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
```

---

**基本用法:查看保护规则**
`gh api repos/<owner>/<repo>/branches/<分支>/protection`

```bash
# 查看主分支的保护配置
gh api repos/owner/repo/branches/main/protection

# 查看是否受保护
gh api repos/owner/repo/branches/main --jq '.protected'
```

---

**基本用法:删除保护规则**
`gh api repos/<owner>/<repo>/branches/<分支>/protection -X DELETE`

```bash
# 取消分支保护
gh api repos/owner/repo/branches/main/protection -X DELETE
```

---

## 规则集(推荐方式)

**基本用法:创建规则集**
`gh api repos/<owner>/<repo>/rulesets -X POST`

```bash
# 创建针对 main 分支的规则集
gh api repos/owner/repo/rulesets -X POST --input - <<'EOF'
{
  "name": "main-protection",
  "target": "branch",
  "source_type": "Repository",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "exclude": [],
      "include": ["~DEFAULT_BRANCH"]
    }
  },
  "rules": [
    { "type": "required_status_checks", "parameters": { "required_status_checks": [] } },
    { "type": "required_pull_request_reviews", "parameters": { "required_approving_review_count": 1 } }
  ]
}
EOF
```

---

**基本用法:查看规则集**
`gh api repos/<owner>/<repo>/rulesets`

```bash
# 列出所有规则集
gh api repos/owner/repo/rulesets

# 查看某规则集详情
gh api repos/owner/repo/rulesets/123
```

---

## 常用保护项

**基本用法:通过 gh repo edit 设置**
`gh repo edit <仓库>`

```bash
# 启用合并时自动删除分支
gh repo edit owner/repo --enable-merge-commit
gh api repos/owner/repo -X PATCH -F delete_branch_on_merge=true

# 启用线性历史(仅 fast-forward / squash)
gh repo edit owner/repo --enable-squash-merge
gh repo edit owner/repo --disable-merge-commit
```

---