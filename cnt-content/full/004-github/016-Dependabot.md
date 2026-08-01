---
order: 59
title: Dependabot
module: github
category: GitHub
difficulty: intermediate
description: Dependabot详解：依赖项自动更新、版本升级与配置最佳实践。
author: fanquanpp
updated: '2026-08-01'
related:
  - github/社区讨论
  - github/AI编程助手
  - 'github/Issues模板-标签与里程碑'
  - github/密钥扫描
prerequisites:
  - github/GitHub概述
---

## 1. Dependabot 概述

### 1.1 什么是 Dependabot

Dependabot 是 GitHub 内置的**依赖管理机器人**，自动检测和更新项目依赖。

### 1.2 两种更新类型

| 类型                 | 触发条件     | 说明            |
| :------------------- | :----------- | :-------------- |
| **Security Updates** | 发现安全漏洞 | 自动创建修复 PR |
| **Version Updates**  | 定期检查     | 保持依赖最新    |

## 2. 配置文件

### 2.1 基本配置

```yaml
# .github/dependabot.yml
version: 2
updates:
  # npm 依赖
  - package-ecosystem: 'npm'
    directory: '/'
    schedule:
      interval: 'weekly'
      day: 'monday'
      time: '09:00'
      timezone: 'Asia/Shanghai'

  # Python 依赖
  - package-ecosystem: 'pip'
    directory: '/backend'
    schedule:
      interval: 'monthly'

  # GitHub Actions
  - package-ecosystem: 'github-actions'
    directory: '/'
    schedule:
      interval: 'weekly'
```

### 2.2 完整配置

```yaml
version: 2
updates:
  - package-ecosystem: 'npm'
    directory: '/'
    schedule:
      interval: 'weekly'
    open-pull-requests-limit: 5
    reviewers:
      - 'dev-team'
    assignees:
      - 'tech-lead'
    labels:
      - 'dependencies'
      - 'automated'
    commit-message:
      prefix: 'chore'
      prefix-development: 'chore'
      include: 'scope'
    ignore:
      - dependency-name: 'express'
        versions: ['>=5.0.0']
      - dependency-name: 'lodash'
    allow:
      - dependency-type: 'production'
    rebase-strategy: 'auto'
    target-branch: 'develop'
    vendor: false
```

## 3. 支持的生态系统

| 生态系统           | 配置值           | 锁定文件            |
| :----------------- | :--------------- | :------------------ |
| **npm**            | `npm`            | `package-lock.json` |
| **yarn**           | `npm`            | `yarn.lock`         |
| **pip**            | `pip`            | `requirements.txt`  |
| **Maven**          | `maven`          | `pom.xml`           |
| **Gradle**         | `gradle`         | `build.gradle`      |
| **Go**             | `gomod`          | `go.sum`            |
| **Cargo**          | `cargo`          | `Cargo.lock`        |
| **NuGet**          | `nuget`          | `*.csproj`          |
| **GitHub Actions** | `github-actions` | 工作流文件          |
| **Docker**         | `docker`         | `Dockerfile`        |

## 4. 版本更新策略

### 4.1 更新频率

| 频率       | 配置值     | 适用场景 |
| :--------- | :--------- | :------- |
| **每天**   | `daily`    | 活跃开发 |
| **每周**   | `weekly`   | 推荐     |
| **每两周** | `biweekly` | 稳定项目 |
| **每月**   | `monthly`  | 维护模式 |

### 4.2 控制更新范围

```yaml
# 只更新生产依赖
allow:
  - dependency-type: 'production'

# 只更新指定依赖
allow:
  - dependency-name: 'express'
  - dependency-name: 'lodash'

# 忽略大版本升级
ignore:
  - dependency-name: 'webpack'
    versions: ['>=5.0.0']
```

## 5. 自动合并

### 5.1 GitHub Actions 自动合并

```yaml
# .github/workflows/auto-merge.yml
name: Auto Merge Dependabot
on: pull_request

permissions:
  pull-requests: write
  contents: write

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    if: ${{ github.actor == 'dependabot[bot]' }}
    steps:
      - name: Enable auto-merge
        run: gh pr merge --auto --merge "$PR_URL"
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 5.2 条件自动合并

```yaml
# 只自动合并补丁版本
- name: Check and auto-merge
  run: |
    if [[ "$(gh pr view --json labels -q '.labels[].name')" == *"dependencies"* ]]; then
      gh pr merge --auto --squash "$PR_URL"
    fi
```

## 6. 最佳实践

- 提交锁定文件，让 Dependabot 精确解析依赖
- 设置 `open-pull-requests-limit` 避免过多 PR
- 使用 `ignore` 控制大版本升级
- 为 Dependabot PR 设置自动 CI 测试
- 定期审查和合并 Dependabot PR

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
| Dependabot | 016-Dependabot | 本文自身 |
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
