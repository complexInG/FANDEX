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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| GitHub 概述 | 001-GitHubOverview | 本文的前置基础 |
| 账户注册与双因素认证（2FA） | 002-AccountRegister2FA2FA | 本文的并列主题 |
| 仓库创建、克隆、归档、删除 | 003-RepositoryCreateCloneArchiveDelete | 本文的并列主题 |
| SSH 与 HTTPS 远程配置 | 004-SSHHTTPS | 本文的并列主题 |
| 协作开发规范 | 005-CollaborationDevelopmentStandard | 本文的并列主题 |
| README文件 | 006-READMEFile | 本文的并列主题 |
| 分支模型与分支保护规则 | 007-BranchModelBranchRule | 本文的并列主题 |
| Gitignore配置 | 008-GitignoreConfig | 本文的并列主题 |
| 开源许可证选择 | 009-OpenSourceLicense | 本文的并列主题 |
| 依赖安全选项 | 010-DependencySecurityOptions | 本文的安全延伸 |
| Fork工作流 | 011-ForkWorkflow | 本文的并列主题 |
| Projects看板 | 012-ProjectsBoard | 本文的并列主题 |
| Wikis | 013-Wikis | 本文的并列主题 |
| Discussions | 014-Discussions | 本文的并列主题 |
| GitHub-Copilot | 015-GitHubCopilot | 本文的并列主题 |
| Dependabot | 016-Dependabot | 本文的并列主题 |
| Issues 模板、标签与里程碑 | 017-IssuesTemplateTagMilestone | 本文的并列主题 |
| 密钥扫描 | 018-SecretScanning | 本文的并列主题 |
| CodeQL代码扫描 | 019-CodeQLCodeScanning | 本文的并列主题 |
| GitHub-CLI | 020-GitHubCLI | 本文自身 |
| REST与GraphQL-API | 021-RESTGraphQLAPI | 本文的并列主题 |
| Webhooks | 022-Webhooks | 本文的并列主题 |
| GitHub-Packages | 023-GitHubPackages | 本文的并列主题 |
| Codespaces | 024-Codespaces | 本文的并列主题 |
| CODEOWNERS | 025-CODEOWNERS | 本文的并列主题 |
| 社区健康文件 | 026-CommunityHealthFile | 本文的并列主题 |
| Pull Request 完整协作流程 | 027-PullRequestCompleteCollaborationFlow | 本文的并列主题 |
| GitHub Pages 多站点方案 | 028-GitHubPagesMultiSolution | 本文的并列主题 |
| GitHub Actions 与 CI/CD | 029-GitHubActionsCICD | 本文的并列主题 |
| Actions触发器 | 030-ActionsTrigger | 本文的并列主题 |
| 常见问题排查 | 031-FAQTroubleshoot | 本文的并列主题 |
| Actions矩阵构建 | 032-ActionsMatrixBuild | 本文的并列主题 |
| Actions缓存依赖 | 033-ActionsCacheDependency | 本文的并列主题 |
| Actions自托管运行器 | 034-ActionsSelfHostedRunner | 本文的并列主题 |
| Actions制品传递 | 035-ActionsArtifact | 本文的并列主题 |
| Actions环境部署 | 036-ActionsEnvironmentDeploy | 本文的前置基础 |
| GitHub 仓库初始化 | 037-GitRepoInit | 本文的并列主题 |
| GitHub 提交与推送 | 038-GitCommitPush | 本文的并列主题 |
| GitHub 拉取与获取 | 039-GitPullFetch | 本文的并列主题 |
| GitHub 合并与变基 | 040-GitMergeRebase | 本文的并列主题 |
| GitHub 冲突解决 | 041-GitConflictResolve | 本文的并列主题 |
| GitHub 标签管理 | 042-GitTagManage | 本文的并列主题 |
| GitHub 远程仓库管理 | 043-GitRemoteManage | 本文的并列主题 |
| GitHub 历史与日志 | 044-GitHistoryLog | 本文的并列主题 |
| GitHub 暂存与回退 | 045-GitStashReset | 本文的并列主题 |
| GitHub CLI 认证配置 | 046-GhCliAuth | 本文的并列主题 |
| GitHub CLI PR 管理 | 047-GhPrManage | 本文的并列主题 |
| GitHub CLI Issue 管理 | 048-GhIssueManage | 本文的并列主题 |
| GitHub CLI 仓库管理 | 049-GhRepoManage | 本文的并列主题 |
| gh release 发布命令速查手册 | 050-GhRelease | 本文的并列主题 |
| gh workflow 工作流命令速查手册 | 051-GhWorkflow | 本文的并列主题 |
| gh gist 代码片段命令速查手册 | 052-GhGist | 本文的并列主题 |
| gh extension 扩展命令速查手册 | 053-GhExtension | 本文的并列主题 |
| gh api 调用命令速查手册 | 054-GhApi | 本文的并列主题 |
| gh search 搜索命令速查手册 | 055-GhSearch | 本文的并列主题 |
| gh label 与 alias/config 命令速查手册 | 056-GhLabel | 本文的并列主题 |
| gh alias 与 config 命令速查手册 | 057-GhAliasConfig | 本文的并列主题 |
