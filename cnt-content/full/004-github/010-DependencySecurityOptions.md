---
order: 53
title: 依赖安全选项
module: github
category: GitHub
difficulty: intermediate
description: 'GitHub依赖安全功能：Dependabot alerts、安全更新与依赖审查。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/Gitignore配置
  - github/开源许可证选择
  - github/Fork工作流
  - github/Projects看板
prerequisites:
  - github/GitHub概述
---

## 1. 依赖安全概述

### 1.1 为什么关注依赖安全

现代项目平均使用数百个依赖，其中任何一个都可能存在安全漏洞。GitHub 提供多种工具帮助管理依赖安全。

### 1.2 GitHub 安全功能矩阵

| 功能                            | 免费版 | 说明        |
| :------------------------------ | :----- | :---------- |
| **Dependabot Alerts**           |        | 漏洞告警    |
| **Dependabot Security Updates** |        | 自动修复    |
| **Dependabot Version Updates**  |        | 版本更新    |
| **Dependency Review**           |        | PR 依赖审查 |
| **Dependency Graph**            |        | 依赖图谱    |

## 2. Dependabot Alerts

### 2.1 工作原理

```
仓库代码 → GitHub 扫描依赖清单 → 匹配漏洞数据库 → 生成告警
```

### 2.2 支持的依赖清单

| 生态系统   | 文件                                |
| :--------- | :---------------------------------- |
| **npm**    | `package.json`、`package-lock.json` |
| **pip**    | `requirements.txt`、`Pipfile.lock`  |
| **Maven**  | `pom.xml`                           |
| **Gradle** | `build.gradle`                      |
| **Go**     | `go.mod`、`go.sum`                  |
| **Cargo**  | `Cargo.toml`、`Cargo.lock`          |
| **NuGet**  | `*.csproj`、`packages.config`       |

### 2.3 配置告警

1. 仓库 Settings → Code security and analysis
2. 启用 Dependabot alerts
3. 可选：启用自动安全更新

## 3. Dependabot Security Updates

### 3.1 自动修复

当发现漏洞时，Dependabot 自动创建 PR 修复：

```markdown
# Dependabot 创建的 PR

## Security Update: lodash

Bumps lodash from 4.17.15 to 4.17.21 to fix:

- CVE-2021-23337: Command injection
- CVE-2020-28500: ReDoS vulnerability

## CVSS Score: 7.2 (High)
```

### 3.2 配置

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: 'npm'
    directory: '/'
    schedule:
      interval: 'weekly'
    open-pull-requests-limit: 10
    reviewers:
      - 'security-team'
    labels:
      - 'security'
      - 'dependencies'
```

## 4. Dependency Review

### 4.1 PR 中的依赖审查

在 PR 中自动检查新增依赖的安全性：

```yaml
# .github/workflows/dependency-review.yml
name: Dependency Review
on: [pull_request]

permissions:
  contents: read

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
        with:
          fail-on-severity: moderate
          deny-licenses: GPL-3.0, AGPL-3.0
```

### 4.2 审查内容

- 新增依赖的已知漏洞
- 许可证合规性
- 依赖变更的影响范围

## 5. 依赖图谱

### 5.1 查看依赖图谱

仓库 → Insights → Dependency graph

### 5.2 依赖图谱信息

- 直接依赖和传递依赖
- 每个依赖的版本
- 已知漏洞标记
- 依赖关系树

## 6. 最佳实践

- 始终提交锁定文件（`package-lock.json`、`yarn.lock`）
- 启用 Dependabot alerts 和 security updates
- 在 CI 中集成依赖审查
- 定期更新依赖版本
- 审查 Dependabot 创建的 PR 后再合并

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
| 依赖安全选项 | 010-DependencySecurityOptions | 本文自身 |
| Fork工作流 | 011-ForkWorkflow | 本文的并列主题 |
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
