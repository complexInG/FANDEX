---
order: 440
title: GitHub 历史与日志
module: github

category: '004-github'
difficulty: beginner
description: GitHub 历史与日志 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 提交历史查看

**基本写法：查看完整历史**
`git log`
```bash
# 查看完整提交历史
git log
```

---

**基本写法：单行简洁显示**
`git log --oneline`
```bash
# 每条提交一行显示
git log --oneline
```

---

**基本写法：图形化分支显示**
`git log --graph`
```bash
# 图形化显示分支合并历史
git log --graph
```

---

**基本写法：完整图形化显示**
`git log --oneline --graph --all`
```bash
# 图形化显示所有分支的简洁历史
git log --oneline --graph --all
```

---

**基本写法：查看最近 N 条提交**
`git log -<数量>`
```bash
# 查看最近 10 条提交
git log -10
```

---

**基本写法：查看指定数量并单行**
`git log -<数量> --oneline`
```bash
# 单行查看最近 5 条提交
git log -5 --oneline
```

---

## 历史筛选

**基本写法：按作者筛选**
`git log --author="<作者>"`
```bash
# 查看指定作者的提交
git log --author="zhangsan"
```

---

**基本写法：按提交信息搜索**
`git log --grep="<关键词>"`
```bash
# 搜索提交信息含关键词的提交
git log --grep="登录"
```

---

**基本写法：按日期筛选**
`git log --since="<开始日期>" --until="<结束日期>"`
```bash
# 查看指定日期范围的提交
git log --since="2026-01-01" --until="2026-07-31"
```

---

**基本写法：相对日期筛选**
`git log --since="<时间>"`
```bash
# 查看最近 2 周的提交
git log --since="2 weeks ago"
```

---

**基本写法：按文件筛选**
`git log -- <文件路径>`
```bash
# 查看指定文件的提交历史
git log -- src/index.js
```

---

**基本写法：按代码变更搜索**
`git log -S "<代码片段>"`
```bash
# 搜索添加或删除指定代码的提交
git log -S "console.log"
```

---

**基本写法：按正则搜索代码**
`git log -G "<正则表达式>"`
```bash
# 使用正则搜索代码变更
git log -G "function\s+login"
```

---

## 差异查看

**基本写法：查看工作区差异**
`git diff`
```bash
# 查看工作区与暂存区的差异
git diff
```

---

**基本写法：查看暂存区差异**
`git diff --staged`
```bash
# 查看暂存区与上次提交的差异
git diff --staged
```

---

**基本写法：查看所有改动**
`git diff HEAD`
```bash
# 查看工作区与上次提交的所有差异
git diff HEAD
```

---

**基本写法：查看指定文件差异**
`git diff <文件>`
```bash
# 查看指定文件的改动
git diff src/index.js
```

---

**基本写法：比较两个提交**
`git diff <提交1> <提交2>`
```bash
# 查看两个提交之间的差异
git diff abc1234 def5678
```

---

**基本写法：比较两个分支**
`git diff <分支1>..<分支2>`
```bash
# 查看两个分支之间的差异
git diff main..feature
```

---

**基本写法：三点差异比较**
`git diff <分支1>...<分支2>`
```bash
# 查看分支2 相对共同祖先的差异
git diff main...feature
```

---

**基本写法：仅查看文件名**
`git diff --name-only`
```bash
# 仅列出有改动的文件名
git diff --name-only
```

---

**基本写法：查看改动统计**
`git diff --stat`
```bash
# 显示文件改动行数统计
git diff --stat
```

---

## 文件历史分析

**基本写法：查看文件改动历史**
`git log -p <文件>`
```bash
# 查看文件的每次改动内容
git log -p src/index.js
```

---

**基本写法：查看文件改动（含重命名）**
`git log --follow -p <文件>`
```bash
# 跟踪文件重命名前的历史
git log --follow -p src/index.js
```

---

**基本写法：查看每行最后修改者**
`git blame <文件>`
```bash
# 显示文件每行最后的修改者
git blame src/index.js
```

---

**基本写法：查看指定行范围的 blame**
`git blame -L <起始>,<结束> <文件>`
```bash
# 查看 10 到 20 行的最后修改者
git blame -L 10,20 src/index.js
```

---

**基本写法：查看 blame 忽略空格**
`git blame -w <文件>`
```bash
# blame 时忽略空格改动
git blame -w src/index.js
```

---

## 提交详情

**基本写法：查看指定提交**
`git show <提交ID>`
```bash
# 查看指定提交的详情和改动
git show abc1234
```

---

**基本写法：查看提交的文件列表**
`git show --stat <提交ID>`
```bash
# 查看提交修改的文件列表
git show --stat abc1234
```

---

**基本写法：查看提交的指定文件**
`git show <提交ID>:<文件路径>`
```bash
# 查看指定提交中某文件的内容
git show abc1234:src/index.js
```

---

**基本写法：查看最近提交**
`git show HEAD`
```bash
# 查看最近一次提交的详情
git show HEAD
```

---

**基本写法：查看上一次提交**
`git show HEAD~1`
```bash
# 查看倒数第二次提交
git show HEAD~1
```

---

## 引用日志

**基本写法：查看引用日志**
`git reflog`
```bash
# 查看 HEAD 的变更历史
git reflog
```

---

**基本写法：查看指定分支引用日志**
`git reflog <分支名>`
```bash
# 查看指定分支的引用日志
git reflog feature
```

---

**基本写法：查看所有引用日志**
`git reflog --all`
```bash
# 查看所有引用的变更历史
git reflog --all
```

---

**基本写法：恢复到引用日志的提交**
`git reset --hard <引用日志ID>`
```bash
# 重置到引用日志记录的某个状态
git reset --hard HEAD@{2}
```

---

**基本写法：查看引用日志的相对引用**
`git show HEAD@{<n>}`
```bash
# 查看引用日志中第 n 个状态
git show HEAD@{3}
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
| GitHub 冲突解决 | 041-GitConflictResolve | 本文的并列主题 |
| GitHub 标签管理 | 042-GitTagManage | 本文的并列主题 |
| GitHub 远程仓库管理 | 043-GitRemoteManage | 本文的并列主题 |
| GitHub 历史与日志 | 044-GitHistoryLog | 本文自身 |
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
