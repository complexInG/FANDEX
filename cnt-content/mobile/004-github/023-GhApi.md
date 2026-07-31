# gh api 调用命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 基础请求

**基本用法:GET 请求**
`gh api <端点>`

```bash
# 获取仓库信息
gh api repos/owner/repo

# 获取当前用户
gh api user

# 列出仓库的 issue
gh api repos/owner/repo/issues
```

---

## 指定方法与字段

**基本用法:POST 请求**
`gh api <端点> --method POST`

```bash
# 创建 issue
gh api repos/owner/repo/issues \
  --method POST \
  -f title="Bug 报告" \
  -f body="详细描述问题"

# 创建仓库
gh api user/repos --method POST -f name=new-repo -f private=true
```

---

**基本用法:传递参数**
`gh api <端点> -f <键>=<值>`

```bash
# 字符串字段(-f)
gh api repos/owner/repo/comments -f body="评论内容"

# 类型化字段(-F,支持数字/布尔/null)
gh api repos/owner/repo/issues -F milestone=12

# 从文件读取字段值
gh api user/repos -f name=@repo-name.txt
```

---

## 输出处理

**基本用法:jq 过滤输出**
`gh api <端点> --jq <表达式>`

```bash
# 仅提取仓库名称
gh api user/repos --jq '.[].full_name'

# 提取并统计
gh api repos/owner/repo/issues --jq 'length'
```

---

**基本用法:分页获取**
`gh api <端点> --paginate`

```bash
# 自动获取所有分页结果
gh api repos/owner/repo/issues --paginate --jq '.[].title'
```

---

## 高级用法

**基本用法:查看请求详情**
`gh api <端点> --include`

```bash
# 包含响应头与状态码
gh api user --include

# 显示完整请求与响应(调试)
gh api user --verbose
```

---

**基本用法:发送原始请求体**
`gh api <端点> --input <文件>`

```bash
# 从文件读取 JSON 请求体
gh api repos/owner/repo/labels --input labels.json
```

---