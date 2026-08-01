---
order: 540
title: gh api 调用命令速查手册
module: github

category: '004-github'
difficulty: beginner
description: gh api 调用命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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

## 参考文献

GitHub 文档：https://docs.github.com/zh
GitHub Actions 文档：https://docs.github.com/zh/actions
GitHub REST API：https://docs.github.com/zh/rest
GitHub GraphQL API：https://docs.github.com/zh/graphql

## 延伸阅读

GitHub Actions CI/CD，见 004-github 模块 Actions 文档。
Git 协作基础，见 003-git 模块。
DevOps 自动化，见 031-devops 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 GitHub 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 GitHub Actions 深入

事件驱动：push、pull_request、schedule、workflow_dispatch；on 支持过滤路径与分支。
上下文：github（事件数据）、env、secrets、needs（任务依赖）；表达式与函数。
安全：第三方 action 固定 SHA；权限默认最小；OIDC 换取云凭证。
缓存与性能：actions/cache、并发控制、矩阵并行。

### 13.2 开源协作治理

CONTRIBUTING 定义贡献路径；Issue 标签（good first issue）引导新手。
维护者时间管理：合并队列、自动化 triage、定期发布。
社区健康：行为准则执行、讨论区沉淀、感谢贡献。
安全披露：SECURITY.md + 私密漏洞报告流程。
