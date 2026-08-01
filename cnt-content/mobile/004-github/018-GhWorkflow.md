# gh workflow 工作流命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 查看工作流

**基本用法:列出工作流**
`gh workflow list`

```bash
# 列出所有工作流
gh workflow list

# 查看某工作流详情
gh workflow view deploy.yml

# 在浏览器中打开
gh workflow view deploy.yml --web
```

---

## 手动触发

**基本用法:触发工作流**
`gh workflow run <工作流>`

```bash
# 手动触发工作流
gh workflow run deploy.yml

# 指定分支触发
gh workflow run deploy.yml --ref feature

# 传入参数
gh workflow run deploy.yml -f environment=production -f version=1.2.3

# 从 JSON 文件读取参数
gh workflow run deploy.yml --raw-field config=@config.json
```

---

## 启用与禁用

**基本用法:启用工作流**
`gh workflow enable <工作流>`

```bash
# 启用被禁用的工作流
gh workflow enable deploy.yml
```

---

**基本用法:禁用工作流**
`gh workflow disable <工作流>`

```bash
# 临时禁用工作流
gh workflow disable deploy.yml
```

---