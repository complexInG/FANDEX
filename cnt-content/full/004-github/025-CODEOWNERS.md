---
order: 67
title: CODEOWNERS
module: github
category: GitHub
difficulty: intermediate
description: CODEOWNERS文件详解：代码所有权、自动审查与权限管理。
author: fanquanpp
updated: '2026-08-01'
related:
  - github/包管理服务
  - github/在线开发环境
  - github/社区健康文件
  - github/PullRequest完整协作流程
prerequisites:
  - github/GitHub概述
---

## 1. CODEOWNERS 概述

### 1.1 什么是 CODEOWNERS

`CODEOWNERS` 文件定义了仓库中**文件和目录的所有者**，当相关文件被修改时自动请求所有者审查。

### 1.2 核心功能

- PR 中自动添加审查者
- 保护关键代码的变更质量
- 明确代码维护责任

## 2. 文件格式

### 2.1 基本语法

```gitignore
# CODEOWNERS 文件

# 默认所有者
*       @org/default-team

# 按目录分配
/src/auth/    @org/auth-team
/src/api/     @org/api-team @org/backend-team

# 按文件类型分配
*.js          @org/frontend-team
*.py          @org/backend-team

# 按文件名分配
Dockerfile    @org/devops-team
Makefile      @org/devops-team

# 精确匹配
/docs/README.md  @org/docs-team
```

### 2.2 规则优先级

- 后面的规则优先级更高
- 更具体的路径优先级更高
- 每个匹配的规则都会添加审查者

```gitignore
# 所有 JS 文件
*.js          @org/frontend-team

# 但 auth 目录的 JS 文件由安全团队审查
/src/auth/*.js  @org/security-team @org/frontend-team
```

## 3. 文件位置

`CODEOWNERS` 可以放在以下位置（按优先级）：

1. `CODEOWNERS`（根目录）
2. `docs/CODEOWNERS`
3. `.github/CODEOWNERS`

推荐放在 `.github/CODEOWNERS`。

## 4. 所有者类型

| 类型     | 语法               | 说明        |
| :------- | :----------------- | :---------- |
| **用户** | `@username`        | 单个用户    |
| **团队** | `@org/team-name`   | GitHub 团队 |
| **邮箱** | `user@example.com` | 邮箱地址    |

## 5. 分支保护集成

### 5.1 要求审查

1. 仓库 Settings → Branches → Branch protection rules
2. 勾选 "Require a pull request before merging"
3. 勾选 "Require review from Code Owners"

### 5.2 效果

- CODEOWNERS 中的审查者必须批准后才能合并
- 即使其他审查者已批准，代码所有者的批准仍然必须

## 6. 实际示例

```gitignore
# .github/CODEOWNERS

# 默认
*                                              @myorg/core-team

# 前端
/src/components/                               @myorg/frontend-team
/src/styles/                                   @myorg/frontend-team
*.vue                                          @myorg/frontend-team
*.css                                          @myorg/frontend-team

# 后端
/src/api/                                      @myorg/backend-team
/src/services/                                 @myorg/backend-team
*.py                                           @myorg/backend-team

# 安全
/src/auth/                                     @myorg/security-team
.env.example                                   @myorg/security-team

# DevOps
Dockerfile                                     @myorg/devops-team
.github/workflows/                             @myorg/devops-team
docker-compose*.yml                            @myorg/devops-team

# 文档
/docs/                                         @myorg/docs-team
README.md                                      @myorg/docs-team
```

## 7. 最佳实践

- 保持团队和文件映射的合理性
- 避免单个人作为所有者（使用团队）
- 定期更新 CODEOWNERS 反映组织变化
- 与分支保护规则配合使用
- 在 PR 模板中提醒审查者

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
| GitHub-CLI | 020-GitHubCLI | 本文的并列主题 |
| REST与GraphQL-API | 021-RESTGraphQLAPI | 本文的并列主题 |
| Webhooks | 022-Webhooks | 本文的并列主题 |
| GitHub-Packages | 023-GitHubPackages | 本文的并列主题 |
| Codespaces | 024-Codespaces | 本文的并列主题 |
| CODEOWNERS | 025-CODEOWNERS | 本文自身 |
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
