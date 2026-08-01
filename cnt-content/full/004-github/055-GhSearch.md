---
order: 550
title: gh search 搜索命令速查手册
module: github

category: '004-github'
difficulty: beginner
description: gh search 搜索命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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
