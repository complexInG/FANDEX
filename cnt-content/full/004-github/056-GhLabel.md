---
order: 560
title: gh label 与 alias/config 命令速查手册
module: github

category: '004-github'
difficulty: beginner
description: gh label 与 alias/config 命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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
