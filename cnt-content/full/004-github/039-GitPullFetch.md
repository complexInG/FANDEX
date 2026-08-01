---
order: 390
title: GitHub 拉取与获取
module: 004-github
category: '004-github'
difficulty: beginner
description: GitHub 拉取与获取 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# GitHub 拉取与获取

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 拉取远程更新

**基本写法：拉取并合并**
`git pull`
```bash
# 拉取远程更新并合并到当前分支
git pull
```

---

**基本写法：拉取指定远程分支**
`git pull origin <分支名>`
```bash
# 拉取指定远程分支并合并
git pull origin main
```

---

**基本写法：拉取并变基**
`git pull --rebase`
```bash
# 拉取远程更新并使用 rebase 方式合并
git pull --rebase
```

---

**基本写法：拉取指定远程和分支并变基**
`git pull --rebase origin <分支名>`
```bash
# 拉取指定分支并使用 rebase
git pull --rebase origin main
```

---

**基本写法：允许不相关历史合并**
`git pull --allow-unrelated-histories`
```bash
# 合并不相关的历史（如初始化仓库后首次合并）
git pull origin main --allow-unrelated-histories
```

---

**基本写法：仅拉取不自动合并**
`git pull --no-commit`
```bash
# 拉取更新但不自动创建合并提交
git pull --no-commit
```

---

## 获取远程信息

**基本写法：获取所有远程更新**
`git fetch`
```bash
# 获取远程所有分支的更新（不合并）
git fetch
```

---

**基本写法：获取指定远程**
`git fetch origin`
```bash
# 获取 origin 远程的更新
git fetch origin
```

---

**基本写法：获取指定分支**
`git fetch origin <分支名>`
```bash
# 获取指定远程分支的更新
git fetch origin main
```

---

**基本写法：获取所有远程**
`git fetch --all`
```bash
# 获取所有远程仓库的更新
git fetch --all
```

---

**基本写法：获取并清理已删除分支**
`git fetch --prune`
```bash
# 获取更新并清理远程已删除的分支引用
git fetch --prune
```

---

**基本写法：获取指定标签**
`git fetch origin <标签名>`
```bash
# 获取远程指定的标签
git fetch origin v1.0.0
```

---

**基本写法：获取所有标签**
`git fetch --tags`
```bash
# 获取远程所有标签
git fetch --tags
```

---

## 远程分支操作

**基本写法：查看远程分支**
`git branch -r`
```bash
# 列出所有远程分支
git branch -r
```

---

**基本写法：查看所有分支**
`git branch -a`
```bash
# 列出本地和远程所有分支
git branch -a
```

---

**基本写法：查看分支详细信息**
`git branch -vv`
```bash
# 查看分支及其追踪关系和最新提交
git branch -vv
```

---

**基本写法：从远程分支创建本地分支**
`git switch -c <本地分支> origin/<远程分支>`
```bash
# 基于远程分支创建本地分支并切换
git switch -c feature origin/feature
```

---

**基本写法：直接跟踪远程分支**
`git switch <分支名>`
```bash
# 自动追踪同名远程分支
git switch feature
```

---

## 拉取冲突处理

**基本写法：中止合并**
`git merge --abort`
```bash
# 取消正在进行的合并操作
git merge --abort
```

---

**基本写法：中止变基**
`git rebase --abort`
```bash
# 取消正在进行的变基操作
git rebase --abort
```

---

**基本写法：继续合并**
`git merge --continue`
```bash
# 解决冲突后继续合并
git merge --continue
```

---

**基本写法：继续变基**
`git rebase --continue`
```bash
# 解决冲突后继续变基
git rebase --continue
```

---

**基本写法：跳过当前变基提交**
`git rebase --skip`
```bash
# 跳过当前冲突的提交继续变基
git rebase --skip
```

---

## 远程信息查看

**基本写法：查看远程仓库详情**
`git remote show origin`
```bash
# 显示 origin 远程仓库的详细信息
git remote show origin
```

---

**基本写法：查看远程分支列表**
`git ls-remote origin`
```bash
# 列出远程仓库的所有引用
git ls-remote origin
```

---

**基本写法：查看远程 HEAD 分支**
`git remote show origin | grep "HEAD branch"`
```bash
# 查看远程默认分支名
git remote show origin | grep "HEAD branch"
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
| GitHub 拉取与获取 | 039-GitPullFetch | 本文自身 |
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
