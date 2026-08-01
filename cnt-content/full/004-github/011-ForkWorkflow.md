---
order: 54
title: Fork工作流
module: github
category: GitHub
difficulty: intermediate
description: 'GitHub Fork工作流详解：开源贡献流程、同步策略与最佳实践。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/开源许可证选择
  - github/依赖安全选项
  - github/Projects看板
  - github/知识库
prerequisites:
  - github/GitHub概述
---

## 1. Fork 工作流概述

### 1.1 什么是 Fork

Fork 是在 GitHub 上创建仓库的**个人副本**，可以在副本中自由修改，不影响原始仓库。

```
原始仓库 (upstream)
    ↑ fork
个人仓库 (origin)
    ↑ clone
本地仓库
```

### 1.2 Fork vs Branch

| 特性      | Fork               | Branch       |
| :-------- | :----------------- | :----------- |
| **权限**  | 无需原始仓库权限   | 需要写权限   |
| **位置**  | 独立的 GitHub 仓库 | 同一仓库内   |
| **适用**  | 开源贡献           | 团队内部开发 |
| **CI/CD** | 各自独立           | 共享         |

## 2. 完整 Fork 工作流

### 2.1 一次性设置

```bash
# 1. 在 GitHub 上 Fork 仓库

# 2. 克隆你的 Fork
git clone https://github.com/YOUR_USERNAME/project.git
cd project

# 3. 添加上游仓库
git remote add upstream https://github.com/ORIGINAL_OWNER/project.git

# 4. 验证远程仓库
git remote -v
# origin    https://github.com/YOUR_USERNAME/project.git (fetch)
# origin    https://github.com/YOUR_USERNAME/project.git (push)
# upstream  https://github.com/ORIGINAL_OWNER/project.git (fetch)
# upstream  https://github.com/ORIGINAL_OWNER/project.git (push)
```

### 2.2 贡献流程

```bash
# 1. 同步上游
git fetch upstream
git checkout main
git merge upstream/main

# 2. 创建功能分支
git checkout -b feature/my-contribution

# 3. 开发并提交
git add .
git commit -m "feat: add new feature"

# 4. 推送到你的 Fork
git push origin feature/my-contribution

# 5. 在 GitHub 上创建 Pull Request
# 从你的 Fork → 原始仓库

# 6. 等待审查和合并
```

### 2.3 保持 Fork 同步

```bash
# 方法一：命令行
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# 方法二：GitHub 界面
# Fork 页面 → "Sync fork" 按钮

# 方法三：GitHub API
gh api repos/YOUR_USERNAME/project/merge-upstream \
  -f branch=main
```

## 3. 常见场景

### 3.1 解决冲突

```bash
# PR 有冲突
git fetch upstream
git checkout feature/my-contribution
git rebase upstream/main
# 解决冲突
git add .
git rebase --continue
git push origin feature/my-contribution --force-with-lease
```

### 3.2 多个 PR 并行

```bash
# 每个功能一个分支
git checkout main
git checkout -b feature/A
# ... 开发 ...

git checkout main
git checkout -b feature/B
# ... 开发 ...

# 分别推送和创建 PR
```

### 3.3 追踪上游变更

```bash
# 查看上游的变更
git fetch upstream
git log upstream/main --oneline -10

# 查看差异
git diff main..upstream/main
```

## 4. 最佳实践

- 始终从最新的上游创建分支
- 每个功能/修复一个分支
- PR 描述清晰，关联 Issue
- 遵循项目的贡献指南
- 定期同步 Fork

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
| Fork工作流 | 011-ForkWorkflow | 本文自身 |
| Projects看板 | 012-ProjectsBoard | 本文的并列主题 |
| Wikis | 013-Wikis | 本文的并列主题 |
| Discussions | 014-Discussions | 本文的并列主题 |
| GitHub-Copilot | 015-GitHubCopilot | 本文的并列主题 |
| Dependabot | 016-Dependabot | 本文的并列主题 |
| Issues 模板、标签与里程碑 | 017-IssuesTemplateTagMilestone | 本文的并列主题 |
| 密钥扫描 | 018-SecretScanning | 本文的并列主题 |
| CodeQL代码扫描 | 019-CodeQLCodeScanning | 本文的并列主题 |
| GitHub-CLI | 020-GitHubCLI | 本文的并列主题 |
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
