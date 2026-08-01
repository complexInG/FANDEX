---
order: 400
title: GitHub 合并与变基
module: 004-github
category: '004-github'
difficulty: beginner
description: GitHub 合并与变基 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# GitHub 合并与变基

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 合并分支

**基本写法：合并指定分支**
`git merge <分支名>`
```bash
# 将指定分支合并到当前分支
git merge feature/login
```

---

**基本写法：禁止快进合并**
`git merge --no-ff <分支名>`
```bash
# 强制创建合并提交保留分支历史
git merge --no-ff feature/login
```

---

**基本写法：仅快进合并**
`git merge --ff-only <分支名>`
```bash
# 仅在可快进时合并否则失败
git merge --ff-only feature/login
```

---

**基本写法：压缩合并**
`git merge --squash <分支名>`
```bash
# 将所有提交压缩为一个后合并
git merge --squash feature/login
```

---

**基本写法：合并并编辑提交信息**
`git merge -e <分支名>`
```bash
# 合并时打开编辑器编辑提交信息
git merge -e feature/login
```

---

**基本写法：合并指定提交**
`git cherry-pick <提交ID>`
```bash
# 将指定提交应用到当前分支
git cherry-pick abc1234
```

---

**基本写法：合并多个提交**
`git cherry-pick <提交1> <提交2>`
```bash
# 将多个提交应用到当前分支
git cherry-pick abc1234 def5678
```

---

## 变基操作

**基本写法：变基到指定分支**
`git rebase <目标分支>`
```bash
# 将当前分支变基到目标分支
git rebase main
```

---

**基本写法：交互式变基**
`git rebase -i HEAD~<数量>`
```bash
# 交互式整理最近 N 次提交
git rebase -i HEAD~5
```

---

**基本写法：交互式变基到指定提交**
`git rebase -i <提交ID>`
```bash
# 从指定提交开始交互式变基
git rebase -i abc1234
```

---

**基本写法：变基到远程分支**
`git rebase origin/<分支名>`
```bash
# 将当前分支变基到远程分支
git rebase origin/main
```

---

**基本写法：变基时保留空提交**
`git rebase --keep-empty <目标分支>`
```bash
# 变基时保留空提交
git rebase --keep-empty main
```

---

## 变基冲突处理

**基本写法：继续变基**
`git rebase --continue`
```bash
# 解决冲突后继续变基
git rebase --continue
```

---

**基本写法：跳过当前提交**
`git rebase --skip`
```bash
# 跳过当前冲突的提交
git rebase --skip
```

---

**基本写法：中止变基**
`git rebase --abort`
```bash
# 取消变基回到变基前状态
git rebase --abort
```

---

**基本写法：编辑待提交内容**
`git rebase --edit-todo`
```bash
# 编辑变基待办列表
git rebase --edit-todo
```

---

## 交互式变基操作

**基本写法：使用 pick 保留提交**
`pick <提交ID>`
```bash
# 在变基编辑器中使用保留该提交
pick abc1234 添加登录功能
```

---

**基本写法：使用 reword 修改信息**
`reword <提交ID>`
```bash
# 保留提交但修改提交信息
reword abc1234 修改提交说明
```

---

**基本写法：使用 squash 合并提交**
`squash <提交ID>`
```bash
# 将该提交合并到前一个提交
squash def5678 修复样式
```

---

**基本写法：使用 fixup 合并并丢弃信息**
`fixup <提交ID>`
```bash
# 合并到前一个提交并丢弃提交信息
fixup def5678 修复样式
```

---

**基本写法：使用 drop 删除提交**
`drop <提交ID>`
```bash
# 删除该提交
drop ghi9012 废弃的实验代码
```

---

**基本写法：使用 edit 暂停修改**
`edit <提交ID>`
```bash
# 在该提交处暂停以便修改内容
edit abc1234 添加登录功能
```

---

## 合并后清理

**基本写法：删除已合并的本地分支**
`git branch -d <分支名>`
```bash
# 合并完成后删除本地分支
git branch -d feature/login
```

---

**基本写法：删除已合并的远程分支**
`git push origin --delete <分支名>`
```bash
# 合并完成后删除远程分支
git push origin --delete feature/login
```

---

**基本写法：清理已删除的远程分支引用**
`git fetch --prune`
```bash
# 清理本地中已不存在的远程分支引用
git fetch --prune
```

---

**基本写法：查看可清理的分支**
`git branch --merged main`
```bash
# 查看已合并到 main 的分支
git branch --merged main
```

---

**基本写法：批量删除已合并分支**
`git branch --merged main | grep -v "main" | xargs git branch -d`
```bash
# 删除所有已合并到 main 的分支（保留 main）
git branch --merged main | grep -v "main" | xargs git branch -d
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
| GitHub 拉取与获取 | 039-GitPullFetch | 本文的并列主题 |
| GitHub 合并与变基 | 040-GitMergeRebase | 本文自身 |
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
