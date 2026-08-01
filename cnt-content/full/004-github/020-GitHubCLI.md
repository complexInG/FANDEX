---
order: 62
title: 'GitHub-CLI'
module: github
category: GitHub
difficulty: intermediate
description: 'GitHub CLI（gh）详解：命令行操作仓库、PR、Issue与Actions。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/密钥扫描
  - github/CodeQL代码扫描
  - 'github/REST与GraphQL-API'
  - github/Web钩子
prerequisites:
  - github/GitHub概述
---

## 1. GitHub CLI 概述

### 1.1 什么是 gh

GitHub CLI（`gh`）是 GitHub 官方命令行工具，在终端中直接操作 GitHub 功能。

### 1.2 安装

```bash
# macOS
brew install gh

# Linux
sudo apt install gh

# Windows
winget install GitHub.cli

# 验证
gh --version
```

### 1.3 认证

```bash
gh auth login
# 选择 GitHub.com
# 选择认证方式（浏览器 / Token）
gh auth status
```

## 2. 仓库操作

```bash
# 创建仓库
gh repo create my-project --public --clone
gh repo create my-project --private

# 克隆仓库
gh repo clone user/repo

# 查看仓库信息
gh repo view user/repo

# Fork 仓库
gh repo fork user/repo --clone

# 列出仓库
gh repo list
gh repo list --limit 50
gh repo list user --language TypeScript
```

## 3. Pull Request

```bash
# 创建 PR
gh pr create --title "feat: add auth" --body "描述内容"
gh pr create --fill    # 使用 commit 信息自动填充

# 查看 PR
gh pr list
gh pr list --state open
gh pr view 123

# 检出 PR
gh pr checkout 123

# 审查 PR
gh pr review 123 --approve
gh pr review 123 --request-changes -b "需要修改"

# 合并 PR
gh pr merge 123 --merge
gh pr merge 123 --squash
gh pr merge 123 --rebase
```

## 4. Issue

```bash
# 创建 Issue
gh issue create --title "Bug: login fails" --body "描述"
gh issue create --title "Bug" --body-file bug-template.md

# 查看 Issue
gh issue list
gh issue list --label bug
gh issue view 123

# 关闭 Issue
gh issue close 123

# 重新打开
gh issue reopen 123
```

## 5. Actions

```bash
# 查看 Workflows
gh workflow list

# 触发 Workflow
gh workflow run ci.yml
gh workflow run ci.yml --ref feature-branch

# 查看 Run
gh run list
gh run view 123456
gh run watch       # 实时监控

# 查看 Logs
gh run view 123456 --log
gh run view 123456 --log-failed
```

## 6. 其他命令

```bash
# Gist
gh gist create file.txt
gh gist list

# Release
gh release create v1.0.0 --title "v1.0.0" --notes "Release notes"
gh release list
gh release download v1.0.0

# API 调用
gh api repos/user/repo/issues
gh api graphql -f query='{ viewer { login } }'

# 扩展
gh extension install github/gh-copilot
gh extension list
```

## 7. 别名配置

```bash
# 设置别名
gh alias set pc 'pr create --fill'
gh alias set pm 'pr merge --squash'
gh alias set il 'issue list'

# 使用别名
gh pc    # 等价于 gh pr create --fill
```

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
