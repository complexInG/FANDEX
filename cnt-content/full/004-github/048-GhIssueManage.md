---
order: 480
title: GitHub CLI Issue 管理
module: 004-github
category: '004-github'
difficulty: beginner
description: GitHub CLI Issue 管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# GitHub CLI Issue 管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Issue

**基本写法：交互式创建 Issue**
`gh issue create`
```bash
# 通过交互式提示创建 Issue
gh issue create
```

---

**基本写法：指定标题和正文**
`gh issue create --title "<标题>" --body "<正文>"`
```bash
# 直接指定 Issue 标题和描述
gh issue create --title "Bug: 登录页面报错" --body "点击登录按钮无响应"
```

---

**基本写法：从文件读取正文**
`gh issue create --title "<标题>" --body-file <文件>`
```bash
# 从文件读取 Issue 正文内容
gh issue create --title "性能优化" --body-file issue-template.md
```

---

**基本写法：指定指派人**
`gh issue create --assignee <用户>`
```bash
# 创建 Issue 并指派处理人
gh issue create --title "修复 bug" --assignee @me
```

---

**基本写法：添加标签**
`gh issue create --label "<标签>"`
```bash
# 创建 Issue 并添加标签
gh issue create --title "新功能" --label "enhancement"
```

---

**基本写法：指定里程碑**
`gh issue create --milestone "<里程碑>"`
```bash
# 创建 Issue 并关联里程碑
gh issue create --title "任务" --milestone "v1.0"
```

---

**基本写法：在浏览器中创建**
`gh issue create --web`
```bash
# 打开浏览器创建 Issue
gh issue create --web
```

---

## 查看 Issue

**基本写法：列出当前仓库 Issue**
`gh issue list`
```bash
# 列出当前仓库的 Issue
gh issue list
```

---

**基本写法：列出指定状态**
`gh issue list --state <状态>`
```bash
# 列出指定状态的 Issue
gh issue list --state open
```

---

**基本写法：列出已关闭 Issue**
`gh issue list --state closed`
```bash
# 列出已关闭的 Issue
gh issue list --state closed
```

---

**基本写法：查看指派给自己的 Issue**
`gh issue list --assignee @me`
```bash
# 列出指派给自己的 Issue
gh issue list --assignee @me
```

---

**基本写法：查看自己创建的 Issue**
`gh issue list --author @me`
```bash
# 列出自己创建的 Issue
gh issue list --author @me
```

---

**基本写法：按标签筛选**
`gh issue list --label "<标签>"`
```bash
# 按标签筛选 Issue
gh issue list --label "bug"
```

---

**基本写法：限制返回数量**
`gh issue list --limit <数量>`
```bash
# 限制返回的 Issue 数量
gh issue list --limit 30
```

---

**基本写法：查看 Issue 详情**
`gh issue view <编号>`
```bash
# 查看指定 Issue 的详细信息
gh issue view 42
```

---

**基本写法：在浏览器中查看**
`gh issue view <编号> --web`
```bash
# 在浏览器中打开 Issue 页面
gh issue view 42 --web
```

---

**基本写法：查看 Issue 评论**
`gh issue view <编号> --comments`
```bash
# 查看 Issue 及其评论内容
gh issue view 42 --comments
```

---

## Issue 评论

**基本写法：添加评论**
`gh issue comment <编号> --body "<评论>"`
```bash
# 在 Issue 中添加评论
gh issue comment 42 --body "已复现此问题"
```

---

**基本写法：从文件读取评论**
`gh issue comment <编号> --body-file <文件>`
```bash
# 从文件读取评论内容
gh issue comment 42 --body-file comment.md
```

---

**基本写法：编辑评论**
`gh api repos/<owner>/<repo>/issues/comments/<评论ID> -X PATCH -f body="<新内容>"`
```bash
# 通过 API 编辑指定评论
gh api repos/owner/repo/issues/comments/123 -X PATCH -f body="更新后的评论"
```

---

**基本写法：删除评论**
`gh api repos/<owner>/<repo>/issues/comments/<评论ID> -X DELETE`
```bash
# 通过 API 删除指定评论
gh api repos/owner/repo/issues/comments/123 -X DELETE
```

---

## Issue 状态管理

**基本写法：关闭 Issue**
`gh issue close <编号>`
```bash
# 关闭指定 Issue
gh issue close 42
```

---

**基本写法：关闭并添加评论**
`gh issue close <编号> --comment "<评论>"`
```bash
# 关闭 Issue 并附带说明
gh issue close 42 --comment "已在 v1.2 修复"
```

---

**基本写法：关闭并指定原因**
`gh issue close <编号> --reason <原因>`
```bash
# 关闭 Issue 并指定关闭原因
gh issue close 42 --reason "not planned"
```

---

**基本写法：重新打开 Issue**
`gh issue reopen <编号>`
```bash
# 重新打开已关闭的 Issue
gh issue reopen 42
```

---

## 编辑 Issue

**基本写法：修改标题**
`gh issue edit <编号> --title "<新标题>"`
```bash
# 修改 Issue 标题
gh issue edit 42 --title "Bug: 登录页面 500 错误"
```

---

**基本写法：修改正文**
`gh issue edit <编号> --body "<新正文>"`
```bash
# 修改 Issue 正文内容
gh issue edit 42 --body "更新后的描述"
```

---

**基本写法：添加标签**
`gh issue edit <编号> --add-label "<标签>"`
```bash
# 为 Issue 添加标签
gh issue edit 42 --add-label "优先级高"
```

---

**基本写法：移除标签**
`gh issue edit <编号> --remove-label "<标签>"`
```bash
# 移除 Issue 的标签
gh issue edit 42 --remove-label "优先级高"
```

---

**基本写法：添加指派人**
`gh issue edit <编号> --add-assignee <用户>`
```bash
# 为 Issue 添加处理人
gh issue edit 42 --add-assignee alice
```

---

**基本写法：移除指派人**
`gh issue edit <编号> --remove-assignee <用户>`
```bash
# 移除 Issue 的处理人
gh issue edit 42 --remove-assignee alice
```

---

## 批量操作

**基本写法：批量关闭 Issue**
`gh issue list --label "<标签>" --json number --jq ".[].number" | xargs -I {} gh issue close {}`
```bash
# 批量关闭指定标签的 Issue
gh issue list --label "wontfix" --json number --jq ".[].number" | xargs -I {} gh issue close {}
```

---

**基本写法：批量添加标签**
`gh issue list --state open --json number --jq ".[].number" | xargs -I {} gh issue edit {} --add-label "需要审查"`
```bash
# 为所有打开的 Issue 添加标签
gh issue list --state open --json number --jq ".[].number" | xargs -I {} gh issue edit {} --add-label "需要审查"
```

---

## Issue 传输与开发

**基本写法：将 Issue 转为分支开发**
`gh issue develop <编号>`
```bash
# 基于 Issue 创建开发分支
gh issue develop 42
```

---

**基本写法：指定分支名开发**
`gh issue develop <编号> -b <分支名>`
```bash
# 为 Issue 创建指定名称的分支
gh issue develop 42 -b fix/login-error
```

---

**基本写法：查看 Issue 关联的 PR**
`gh issue view <编号> --json trackedIssues`
```bash
# 查看 Issue 关联的追踪问题
gh issue view 42 --json trackedIssues
```

---

## JSON 输出

**基本写法：输出 JSON 格式**
`gh issue list --json <字段>`
```bash
# 以 JSON 格式输出指定字段
gh issue list --json number,title,state
```

---

**基本写法：使用 jq 过滤**
`gh issue list --json number,title | jq ".[] | select(.title | contains(\"bug\"))"`
```bash
# 使用 jq 过滤标题含 bug 的 Issue
gh issue list --json number,title | jq ".[] | select(.title | contains(\"bug\"))"
```

---

**基本写法：使用模板输出**
`gh issue list --template "<模板>"`
```bash
# 使用 Go 模板自定义输出格式
gh issue list --template "{{range .}}#{{.number}} {{.title}}{{end}}"
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
| GitHub 暂存与回退 | 045-GitStashReset | 本文的并列主题 |
| GitHub CLI 认证配置 | 046-GhCliAuth | 本文的并列主题 |
| GitHub CLI PR 管理 | 047-GhPrManage | 本文的并列主题 |
| GitHub CLI Issue 管理 | 048-GhIssueManage | 本文自身 |
| GitHub CLI 仓库管理 | 049-GhRepoManage | 本文的并列主题 |
| gh release 发布命令速查手册 | 050-GhRelease | 本文的并列主题 |
| gh workflow 工作流命令速查手册 | 051-GhWorkflow | 本文的并列主题 |
| gh gist 代码片段命令速查手册 | 052-GhGist | 本文的并列主题 |
| gh extension 扩展命令速查手册 | 053-GhExtension | 本文的并列主题 |
| gh api 调用命令速查手册 | 054-GhApi | 本文的并列主题 |
| gh search 搜索命令速查手册 | 055-GhSearch | 本文的并列主题 |
| gh label 与 alias/config 命令速查手册 | 056-GhLabel | 本文的并列主题 |
| gh alias 与 config 命令速查手册 | 057-GhAliasConfig | 本文的并列主题 |
