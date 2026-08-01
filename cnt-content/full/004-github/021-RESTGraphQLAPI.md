---
order: 63
title: 'REST与GraphQL-API'
module: github
category: GitHub
difficulty: advanced
description: 'GitHub API详解：REST API与GraphQL API的使用、认证与速率限制。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/CodeQL代码扫描
  - github/命令行工具
  - github/Web钩子
  - github/包管理服务
prerequisites:
  - github/GitHub概述
---

## 1. GitHub API 概述

### 1.1 两种 API

| 特性         | REST API         | GraphQL API              |
| :----------- | :--------------- | :----------------------- |
| **端点**     | 多个固定端点     | 单一端点                 |
| **数据获取** | 固定结构         | 按需获取                 |
| **请求次数** | 可能需要多次     | 通常一次                 |
| **版本**     | v3               | v4                       |
| **基础 URL** | `api.github.com` | `api.github.com/graphql` |

## 2. 认证

### 2.1 Token 类型

| Token                                    | 用途       | 权限       |
| :--------------------------------------- | :--------- | :--------- |
| **Personal Access Token (Classic)**      | 个人使用   | 全部权限   |
| **Personal Access Token (Fine-grained)** | 个人使用   | 细粒度权限 |
| **GitHub App Token**                     | 应用集成   | 按需授权   |
| **OAuth App Token**                      | 第三方应用 | 用户授权   |

### 2.2 创建 Token

1. Settings → Developer settings → Personal access tokens
2. 选择权限范围
3. 生成并保存 Token

### 2.3 使用 Token

```bash
# REST API
curl -H "Authorization: token ghp_xxxxx" \
  https://api.github.com/user

# GraphQL API
curl -H "Authorization: bearer ghp_xxxxx" \
  -X POST -d '{"query": "{ viewer { login } }"}' \
  https://api.github.com/graphql

# 使用 gh CLI
gh api user
```

## 3. REST API

### 3.1 常用端点

| 操作       | 方法 | 端点                           |
| :--------- | :--- | :----------------------------- |
| 获取用户   | GET  | `/user`                        |
| 列出仓库   | GET  | `/user/repos`                  |
| 获取仓库   | GET  | `/repos/{owner}/{repo}`        |
| 列出 Issue | GET  | `/repos/{owner}/{repo}/issues` |
| 创建 Issue | POST | `/repos/{owner}/{repo}/issues` |
| 列出 PR    | GET  | `/repos/{owner}/{repo}/pulls`  |
| 创建 PR    | POST | `/repos/{owner}/{repo}/pulls`  |

### 3.2 示例

```bash
# 列出仓库
curl -H "Authorization: token ghp_xxxxx" \
  "https://api.github.com/user/repos?per_page=10&sort=updated"

# 创建 Issue
curl -X POST \
  -H "Authorization: token ghp_xxxxx" \
  -H "Content-Type: application/json" \
  -d '{"title":"Bug report","body":"Description","labels":["bug"]}' \
  https://api.github.com/repos/user/repo/issues

# 使用 gh CLI（推荐）
gh api repos/user/repo/issues \
  -f title="Bug report" \
  -f body="Description"
```

## 4. GraphQL API

### 4.1 基本查询

```graphql
query {
  viewer {
    login
    repositories(first: 10, orderBy: { field: UPDATED_AT, direction: DESC }) {
      nodes {
        name
        description
        stargazerCount
      }
    }
  }
}
```

### 4.2 变更操作

```graphql
mutation {
  createIssue(input: { repositoryId: "REPO_ID", title: "Bug report", body: "Description" }) {
    issue {
      number
      url
    }
  }
}
```

### 4.3 使用 gh CLI

```bash
gh api graphql -f query='
  query {
    viewer {
      login
      repositories(first: 5) {
        nodes { name }
      }
    }
  }
'
```

## 5. 速率限制

### 5.1 限制规则

| API         | 认证用户      | 未认证     |
| :---------- | :------------ | :--------- |
| **REST**    | 5,000 次/小时 | 60 次/小时 |
| **GraphQL** | 5,000 点/小时 | —          |

### 5.2 检查剩余配额

```bash
# REST API
curl -I https://api.github.com/user
# X-RateLimit-Limit: 5000
# X-RateLimit-Remaining: 4999
# X-RateLimit-Reset: 1718342400

# GraphQL
gh api graphql -f query='{ rateLimit { remaining resetAt } }'
```

### 5.3 避免触发限制

- 使用条件请求（ETag / If-Modified-Since）
- 缓存 API 响应
- 使用 GraphQL 减少请求次数
- 使用 Webhooks 替代轮询

## 6. Webhooks vs API 轮询

| 方式             | 优势       | 劣势       |
| :--------------- | :--------- | :--------- |
| **Webhooks**     | 实时、高效 | 需要服务器 |
| **API 轮询**     | 简单       | 浪费配额   |
| **GraphQL 订阅** | 实时       | 实验性     |

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
| REST与GraphQL-API | 021-RESTGraphQLAPI | 本文自身 |
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
