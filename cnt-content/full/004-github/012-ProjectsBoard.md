---
order: 55
title: Projects看板
module: github
category: GitHub
difficulty: intermediate
description: 'GitHub Projects看板：项目管理、自动化工作流与视图配置。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/依赖安全选项
  - github/Fork工作流
  - github/知识库
  - github/社区讨论
prerequisites:
  - github/GitHub概述
---

## 1. Projects 概述

### 1.1 什么是 GitHub Projects

GitHub Projects 是内置的**项目管理工具**，支持看板视图、表格视图和路线图，可以关联 Issue、PR 和草稿。

### 1.2 Projects V2 特性

| 特性           | 说明                         |
| :------------- | :--------------------------- |
| **多视图**     | 看板、表格、路线图           |
| **自定义字段** | 文本、数字、日期、单选、迭代 |
| **自动化**     | 状态变更自动移动卡片         |
| **过滤器**     | 按字段筛选和分组             |
| **跨仓库**     | 聚合多个仓库的 Issue         |

## 2. 创建项目

### 2.1 创建组织项目

1. 组织页面 → Projects → New project
2. 选择模板（Board / Table / Roadmap）
3. 添加仓库和团队

### 2.2 创建仓库项目

1. 仓库 → Projects → New project
2. 自动关联当前仓库

## 3. 自定义字段

### 3.1 字段类型

| 类型              | 说明     | 示例               |
| :---------------- | :------- | :----------------- |
| **Text**          | 自由文本 | 备注、描述         |
| **Number**        | 数字     | 优先级、故事点     |
| **Date**          | 日期     | 截止日期           |
| **Single select** | 单选     | 状态、类型         |
| **Iteration**     | 迭代周期 | Sprint 1、Sprint 2 |

### 3.2 推荐字段配置

```
Status: Backlog → Todo → In Progress → In Review → Done
Priority:  Critical →  High →  Medium →  Low
Type:  Bug →  Feature →  Chore →  Docs
Sprint: Sprint 1, Sprint 2, Sprint 3...
Estimate: 1, 2, 3, 5, 8, 13
```

## 4. 自动化工作流

### 4.1 内置自动化

| 触发条件   | 自动操作                  |
| :--------- | :------------------------ |
| Issue 创建 | 添加到项目，状态设为 Todo |
| PR 创建    | 状态设为 In Review        |
| PR 合并    | 状态设为 Done             |
| Issue 关闭 | 状态设为 Done             |

### 4.2 GitHub Actions 自动化

```yaml
# .github/workflows/project-automation.yml
name: Project Automation
on:
  issues:
    types: [opened, labeled]
  pull_request:
    types: [opened]

jobs:
  add-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v1.0.2
        with:
          project-url: https://github.com/orgs/myorg/projects/1
          github-token: ${{ secrets.PROJECT_TOKEN }}
          labeled: bug, feature
```

### 4.3 GraphQL 自动化

```graphql
mutation {
  addProjectV2ItemById(input: { projectId: "PROJECT_ID", contentId: "ISSUE_ID" }) {
    item {
      id
    }
  }
}
```

## 5. 视图配置

### 5.1 看板视图

按状态分列的拖拽式看板：

```
| Backlog | Todo | In Progress | In Review | Done |
|---------|------|-------------|-----------|------|
| Issue#5 | #3   | #1          | #2        | #4   |
| Issue#8 | #6   |             |           | #7   |
```

### 5.2 表格视图

类似电子表格，支持排序、筛选和分组：

```
| Title | Status | Priority | Sprint | Assignee |
|-------|--------|----------|--------|----------|
| Auth  | Done   | High     | S1     | Alice    |
| API   | Active | Medium   | S2     | Bob      |
```

### 5.3 路线图视图

按时间线展示项目进度，适合展示里程碑。

## 6. Insights 与报告

### 6.1 项目统计

- 完成率
- 燃尽图
- 按标签/类型分布
- 按成员工作量

### 6.2 导出数据

```bash
# 使用 GitHub CLI 导出
gh project item-list 1 --owner myorg --format json > project.json
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
| Projects看板 | 012-ProjectsBoard | 本文自身 |
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
