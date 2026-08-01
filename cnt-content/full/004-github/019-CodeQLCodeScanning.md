---
order: 61
title: CodeQL代码扫描
module: github
category: GitHub
difficulty: intermediate
description: 'GitHub CodeQL代码扫描：静态分析、查询编写与安全漏洞检测。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'github/Issues模板-标签与里程碑'
  - github/密钥扫描
  - github/命令行工具
  - 'github/REST与GraphQL-API'
prerequisites:
  - github/GitHub概述
---

## 1. CodeQL 概述

### 1.1 什么是 CodeQL

CodeQL 是 GitHub 的**静态代码分析引擎**，通过将代码转换为数据库并运行查询来发现安全漏洞和代码缺陷。

### 1.2 工作原理

```
源代码 → CodeQL 数据库 → 运行查询 → 发现问题
```

## 2. 配置代码扫描

### 2.1 使用默认配置

```yaml
# .github/workflows/codeql.yml
name: CodeQL
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * 1' # 每周一

jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3
```

### 2.2 支持的语言

| 语言                      | 分析类型    |
| :------------------------ | :---------- |
| **JavaScript/TypeScript** | 安全 + 质量 |
| **Python**                | 安全 + 质量 |
| **Java**                  | 安全 + 质量 |
| **C/C++**                 | 安全 + 质量 |
| **C#**                    | 安全 + 质量 |
| **Go**                    | 安全 + 质量 |
| **Ruby**                  | 安全        |
| **Swift**                 | 安全        |
| **Kotlin**                | 安全        |

### 2.3 自定义配置

```yaml
# .github/codeql/codeql-config.yml
name: Custom CodeQL Config
paths:
  - src
  - lib
paths-ignore:
  - '**/test/**'
  - '**/tests/**'
queries:
  - uses: security-and-quality
  - uses: ./custom-queries
```

## 3. 查看扫描结果

### 3.1 Security 选项卡

仓库 → Security → Code scanning alerts

### 3.2 告警级别

| 级别        | 说明           |
| :---------- | :------------- |
| **Error**   | 确定的安全漏洞 |
| **Warning** | 潜在的安全问题 |
| **Note**    | 建议性改进     |

### 3.3 常见检测

- SQL 注入
- XSS（跨站脚本）
- 路径遍历
- 不安全的反序列化
- 硬编码凭证
- 不安全的随机数

## 4. 自定义查询

### 4.1 CodeQL 查询语法

```ql
/**
 * @name SQL injection
 * @description Detects SQL injection vulnerabilities
 * @kind path-problem
 * @security-severity 9.0
 */

import python

from Call call, StrConst sql
where
  call.getFunc().hasName("execute") and
  sql = call.getArg(0) and
  exists(Call format |
    format.getFunc().hasName("format") and
    format = sql.getAChild*()
  )
select call, "Potential SQL injection"
```

### 4.2 查询套件

```yaml
# codeql-suite.yml
name: Custom Query Suite
queries:
  - uses: security-and-quality
  - uses: ./custom-queries/sql-injection.ql
```

## 5. 最佳实践

- 在 PR 中运行代码扫描，及早发现问题
- 定期运行全量扫描（schedule）
- 关注高严重性告警
- 将误报标记为已忽略并说明原因
- 结合其他安全工具（Dependabot、密钥扫描）

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
| CodeQL代码扫描 | 019-CodeQLCodeScanning | 本文自身 |
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
