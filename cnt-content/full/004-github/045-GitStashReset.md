---
order: 450
title: GitHub 暂存与回退
module: 004-github
category: '004-github'
difficulty: beginner
description: GitHub 暂存与回退 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 暂存改动

**基本写法：暂存当前改动**
`git stash`
```bash
# 暂存工作区和暂存区的改动
git stash
```

---

**基本写法：暂存并添加说明**
`git stash push -m "<说明>"`
```bash
# 暂存改动并附上描述信息
git stash push -m "登录功能开发中"
```

---

**基本写法：包含未跟踪文件**
`git stash -u`
```bash
# 暂存改动同时包含未跟踪文件
git stash -u
```

---

**基本写法：包含所有文件**
`git stash -a`
```bash
# 暂存所有改动（含忽略文件）
git stash -a
```

---

**基本写法：保留暂存区**
`git stash --keep-index`
```bash
# 暂存改动但保留暂存区内容
git stash --keep-index
```

---

## 查看暂存

**基本写法：查看暂存列表**
`git stash list`
```bash
# 列出所有暂存的改动
git stash list
```

---

**基本写法：查看暂存详情**
`git stash show stash@{<索引>}`
```bash
# 查看指定暂存的改动摘要
git stash show stash@{0}
```

---

**基本写法：查看暂存差异详情**
`git stash show -p stash@{<索引>}`
```bash
# 查看指定暂存的完整差异
git stash show -p stash@{0}
```

---

**基本写法：查看最近暂存详情**
`git stash show`
```bash
# 查看最近一次暂存的改动摘要
git stash show
```

---

## 恢复暂存

**基本写法：恢复最近暂存**
`git stash pop`
```bash
# 恢复最近暂存并删除该暂存记录
git stash pop
```

---

**基本写法：恢复指定暂存**
`git stash pop stash@{<索引>}`
```bash
# 恢复指定索引的暂存
git stash pop stash@{1}
```

---

**基本写法：恢复但不删除暂存**
`git stash apply`
```bash
# 恢复最近暂存但保留暂存记录
git stash apply
```

---

**基本写法：恢复指定暂存不删除**
`git stash apply stash@{<索引>}`
```bash
# 恢复指定暂存但保留记录
git stash apply stash@{1}
```

---

## 删除暂存

**基本写法：删除指定暂存**
`git stash drop stash@{<索引>}`
```bash
# 删除指定索引的暂存记录
git stash drop stash@{0}
```

---

**基本写法：清空所有暂存**
`git stash clear`
```bash
# 删除所有暂存记录
git stash clear
```

---

**基本写法：从暂存创建分支**
`git stash branch <分支名> stash@{<索引>}`
```bash
# 基于暂存创建新分支并恢复改动
git stash branch feature/recovery stash@{0}
```

---

## 撤销工作区改动

**基本写法：撤销工作区修改**
`git restore <文件>`
```bash
# 恢复文件到上次提交的状态
git restore index.js
```

---

**基本写法：checkout 撤销修改**
`git checkout -- <文件>`
```bash
# 旧写法撤销工作区修改
git checkout -- index.js
```

---

**基本写法：撤销所有修改**
`git restore .`
```bash
# 撤销当前目录所有改动
git restore .
```

---

**基本写法：取消暂存**
`git restore --staged <文件>`
```bash
# 将文件从暂存区移回工作区
git restore --staged index.js
```

---

**基本写法：取消所有暂存**
`git restore --staged .`
```bash
# 将所有文件从暂存区移回工作区
git restore --staged .
```

---

## 回退提交

**基本写法：软回退（保留改动）**
`git reset --soft HEAD~1`
```bash
# 撤销上次提交保留改动在暂存区
git reset --soft HEAD~1
```

---

**基本写法：混合回退（默认）**
`git reset --mixed HEAD~1`
```bash
# 撤销上次提交保留改动在工作区
git reset --mixed HEAD~1
```

---

**基本写法：硬回退（丢弃改动）**
`git reset --hard HEAD~1`
```bash
# 撤销上次提交并丢弃所有改动
git reset --hard HEAD~1
```

---

**基本写法：回退到指定提交**
`git reset --hard <提交ID>`
```bash
# 强制回退到指定提交
git reset --hard abc1234
```

---

**基本写法：回退单个文件**
`git reset HEAD~1 <文件>`
```bash
# 仅回退指定文件到上次提交状态
git reset HEAD~1 src/index.js
```

---

**基本写法：回退到远程分支状态**
`git reset --hard origin/<分支名>`
```bash
# 重置本地分支到远程分支状态
git reset --hard origin/main
```

---

## 反向提交

**基本写法：创建反向提交**
`git revert <提交ID>`
```bash
# 创建一个新提交撤销指定提交的改动
git revert abc1234
```

---

**基本写法：反向提交不自动提交**
`git revert -n <提交ID>`
```bash
# 反向提交但不自动创建提交
git revert -n abc1234
```

---

**基本写法：反向多个提交**
`git revert <提交1>..<提交2>`
```bash
# 反向指定范围内的提交
git revert abc1234..def5678
```

---

**基本写法：反向最近提交**
`git revert HEAD`
```bash
# 撤销最近一次提交
git revert HEAD
```

---

## 清理未跟踪文件

**基本写法：查看将被清理的文件**
`git clean -n`
```bash
# 预览将被删除的未跟踪文件
git clean -n
```

---

**基本写法：删除未跟踪文件**
`git clean -f`
```bash
# 强制删除未跟踪的文件
git clean -f
```

---

**基本写法：删除未跟踪目录**
`git clean -fd`
```bash
# 删除未跟踪的文件和目录
git clean -fd
```

---

**基本写法：包含忽略文件清理**
`git clean -fdx`
```bash
# 删除所有未跟踪文件含忽略文件
git clean -fdx
```

---

**基本写法：交互式清理**
`git clean -i`
```bash
# 交互式选择要删除的文件
git clean -i
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
| GitHub 历史与日志 | 044-GitHistoryLog | 本文的并列主题 |
| GitHub 暂存与回退 | 045-GitStashReset | 本文自身 |
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
