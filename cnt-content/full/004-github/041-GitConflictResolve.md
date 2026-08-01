---
order: 410
title: GitHub 冲突解决
module: 004-github
category: '004-github'
difficulty: beginner
description: GitHub 冲突解决 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 冲突识别

**基本写法：查看冲突文件**
`git status`
```bash
# 查看哪些文件存在合并冲突
git status
```

---

**基本写法：查看冲突详情**
`git diff --name-only --diff-filter=U`
```bash
# 仅列出有冲突的文件名
git diff --name-only --diff-filter=U
```

---

**基本写法：查看冲突内容**
`git diff`
```bash
# 查看冲突的具体内容
git diff
```

---

**基本写法：使用 mergetool**
`git mergetool`
```bash
# 启动图形化合并工具解决冲突
git mergetool
```

---

**基本写法：指定合并工具**
`git mergetool --tool=<工具名>`
```bash
# 使用指定的合并工具
git mergetool --tool=vimdiff
```

---

## 冲突标记处理

**基本写法：冲突标记说明**
`<<<<<<< HEAD`
```bash
# 冲突标记开始（当前分支内容）
# <<<<<<< HEAD
# 当前分支的代码
# =======
# 传入分支的代码
# >>>>>>> feature/login
```

---

**基本写法：保留当前分支版本**
`git checkout --ours <文件>`
```bash
# 冲突时保留当前分支的版本
git checkout --ours index.js
```

---

**基本写法：保留传入分支版本**
`git checkout --theirs <文件>`
```bash
# 冲突时保留传入分支的版本
git checkout --theirs index.js
```

---

**基本写法：使用 VS Code 解决冲突**
`code <冲突文件>`
```bash
# 用 VS Code 打开冲突文件图形化解决
code index.js
```

---

## 冲突解决流程

**基本写法：标记冲突已解决**
`git add <文件>`
```bash
# 编辑文件解决冲突后添加到暂存区
git add index.js
```

---

**基本写法：完成合并提交**
`git commit -m "<合并信息>"`
```bash
# 所有冲突解决后完成合并提交
git commit -m "merge: 合并 feature/login 分支"
```

---

**基本写法：使用默认合并信息**
`git commit --no-edit`
```bash
# 使用默认的合并提交信息
git commit --no-edit
```

---

**基本写法：继续变基**
`git rebase --continue`
```bash
# 变基冲突解决后继续
git rebase --continue
```

---

**基本写法：完成 cherry-pick**
`git cherry-pick --continue`
```bash
# cherry-pick 冲突解决后继续
git cherry-pick --continue
```

---

## 中止操作

**基本写法：中止合并**
`git merge --abort`
```bash
# 取消合并回到合并前状态
git merge --abort
```

---

**基本写法：中止变基**
`git rebase --abort`
```bash
# 取消变基回到变基前状态
git rebase --abort
```

---

**基本写法：中止 cherry-pick**
`git cherry-pick --abort`
```bash
# 取消 cherry-pick 操作
git cherry-pick --abort
```

---

**基本写法：重置到合并前状态**
`git reset --hard HEAD`
```bash
# 强制重置到当前 HEAD（丢弃所有改动）
git reset --hard HEAD
```

---

## 冲突预防

**基本写法：拉取前先暂存**
`git stash && git pull && git stash pop`
```bash
# 暂存当前改动后拉取再恢复
git stash && git pull && git stash pop
```

---

**基本写法：使用 rebase 拉取**
`git pull --rebase`
```bash
# 拉取时使用变基避免合并提交
git pull --rebase
```

---

**基本写法：定期同步主分支**
`git fetch origin && git rebase origin/main`
```bash
# 定期将当前分支变基到最新主分支
git fetch origin && git rebase origin/main
```

---

**基本写法：查看分支差异**
`git diff main...feature`
```bash
# 查看 feature 分支相对 main 的差异
git diff main...feature
```

---

**基本写法：查看分支分叉点**
`git merge-base <分支1> <分支2>`
```bash
# 查看两个分支的共同祖先提交
git merge-base main feature
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
| GitHub 合并与变基 | 040-GitMergeRebase | 本文的并列主题 |
| GitHub 冲突解决 | 041-GitConflictResolve | 本文自身 |
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
