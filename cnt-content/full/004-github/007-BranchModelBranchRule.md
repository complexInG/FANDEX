---
order: 50
tags:
  - github
difficulty: intermediate
title: 分支模型与分支保护规则
module: github
category: 'GitHub Basics'
description: 分支模型设计、保护规则配置与强制策略。
author: fanquanpp
updated: '2026-08-01'
related:
  - github/协作开发规范
  - github/README文件
  - github/Gitignore配置
  - github/开源许可证选择
prerequisites:
  - github/GitHub概述
---

# GitHub 分支管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 2. 分支模型详解

### 2.1 Git Flow 分支模型

Git Flow 是一种较为复杂的分支模型，适合有明确发布周期的软件项目。

#### 2.1.1 核心分支

- **main/master**：生产环境分支，存放稳定的已发布代码
- **develop**：开发集成分支，存放最新的开发代码
- **feature/**\*：功能分支，从 develop 分支创建，完成后合并回 develop
- **release/**\*：发布分支，从 develop 分支创建，用于预发布准备
- **hotfix/**\*：热修复分支，从 main/master 分支创建，用于紧急修复生产问题

#### 2.1.2 Git Flow 工作流程

1. 从 develop 分支创建 feature 分支
2. 在 feature 分支上进行开发
3. 完成开发后，将 feature 分支合并回 develop
4. 当 develop 分支积累了足够的功能，创建 release 分支
5. 在 release 分支上进行测试和修复
6. 完成后，将 release 分支合并回 main/master 和 develop
7. 如有生产问题，从 main/master 创建 hotfix 分支
8. 修复完成后，将 hotfix 分支合并回 main/master 和 develop

### 2.2 GitHub Flow 分支模型

GitHub Flow 是一种简化的分支模型，适合持续交付和 Web 服务项目。

#### 2.2.1 核心分支

- **main**：默认分支，始终保持可部署状态
- **feature 分支**：从 main 分支创建，用于开发新功能或修复问题

#### 2.2.2 GitHub Flow 工作流程

1. 从 main 分支创建 feature 分支
2. 在 feature 分支上进行开发
3. 提交代码并推送到远程仓库
4. 打开 Pull Request 进行代码审查
5. 通过审查后，将 feature 分支合并回 main
6. 合并后立即部署到生产环境

### 2.3 分支模型对比

| 特性     | Git Flow                                      | GitHub Flow         |
| -------- | --------------------------------------------- | ------------------- |
| 分支数量 | 多（main, develop, feature, release, hotfix） | 少（main, feature） |
| 适合项目 | 有明确发布周期的软件                          | 持续交付的 Web 服务 |
| 学习成本 | 高                                            | 低                  |
| 部署频率 | 较低                                          | 较高                |
| 复杂度   | 复杂                                          | 简单                |

## 3. GitHub 分支保护规则配置

### 3.1 配置路径

路径：**Settings → Branches → Branch protection rules → Add rule**

### 3.2 详细配置选项

#### 3.2.1 基本设置

- **Branch name pattern**：分支名称模式，如 `main`、`release/*` 等
- **Protect matching branches**：启用分支保护

#### 3.2.2 合并规则

- **Require a pull request before merging**：禁止直接推送，强制通过 PR 合并
- **Require approvals**：设置最少审查人数，可选择是否需要 CODEOWNERS 批准
- **Dismiss stale pull request approvals when new commits are pushed**：当有新提交时，撤销之前的批准
- **Require review from Code Owners**：要求代码所有者审查
- **Restrict who can dismiss pull request reviews**：限制谁可以撤销 PR 审查

#### 3.2.3 状态检查

- **Require status checks to pass before merging**：要求状态检查通过才能合并
- **Require branches to be up to date before merging**：要求分支在合并前与基础分支同步
- **Status checks that are required**：选择需要通过的状态检查

#### 3.2.4 分支操作限制

- **Restrict who can push to matching branches**：限制谁可以向匹配的分支推送
- **Allow force pushes**：是否允许强制推送
- **Allow deletions**：是否允许删除分支
- **Include administrators**：是否对管理员同样生效

### 3.3 配置示例

#### 3.3.1 生产分支（main/master）配置

- \[支持] Require a pull request before merging
- \[支持] Require approvals (2 人)
- \[支持] Require status checks to pass before merging
- \[支持] Require branches to be up to date before merging
- \[支持] Include administrators
- \[不支持] Allow force pushes
- \[不支持] Allow deletions

#### 3.3.2 开发分支（develop）配置

- \[支持] Require a pull request before merging
- \[支持] Require approvals (1 人)
- \[支持] Require status checks to pass before merging
- \[支持] Require branches to be up to date before merging
- \[支持] Include administrators
- \[不支持] Allow force pushes
- \[不支持] Allow deletions

#### 3.3.3 功能分支（feature/\*）配置

- \[不支持] Require a pull request before merging
- \[不支持] Require approvals
- \[不支持] Require status checks to pass before merging
- \[不支持] Include administrators
- \[支持] Allow force pushes
- \[支持] Allow deletions

## 4. CODEOWNERS 配置

### 4.1 CODEOWNERS 文件位置

CODEOWNERS 文件可以放在以下位置：

- 仓库根目录：`.github/CODEOWNERS`
- 仓库根目录：`CODEOWNERS`
- `docs/` 目录：`docs/CODEOWNERS`

### 4.2 CODEOWNERS 语法

```gitignore
 # 语法：模式 @团队或用户
 # 整个仓库的所有者
 *
 # 特定目录的所有者
 /
 /
 # 特定文件类型的所有者
 *
 *
 # 特定文件的所有者
 README.md @maintainer # README.md 文件变更需要 maintainer 审查
```

### 4.3 CODEOWNERS 匹配规则

- 匹配顺序：从上到下，找到第一个匹配的规则即生效
- 更具体的模式优先于更通用的模式
- 以 `#` 开头的行是注释
- 空行被忽略

## 5. 分支操作实战

### 5.1 GitHub Flow 分支操作

```bash
 # 1. 确保本地 main 分支是最新的
 git checkout main
 git pull origin main
 # 2. 创建并切换到 feature 分支
 git checkout -b feature/add-login
 # 3. 进行开发并提交代码
 git add .
 git commit -m "Add login functionality"
 # 4. 推送到远程仓库（首次推送）
 git push -u origin feature/add-login
 # 5. 后续推送
 git push
 # 6. 完成开发后，在 GitHub 上打开 PR
 # 7. 通过审查后，合并 PR
 # 8. 清理本地分支
 git checkout main
 git pull origin main
 git branch -d feature/add-login
```

### 5.2 Git Flow 分支操作

```bash
 # 1. 从 develop 分支创建 feature 分支
 git checkout develop
 git pull origin develop
 git checkout -b feature/add-login
 # 2. 开发完成后，合并回 develop
 git checkout develop
 git merge feature/add-login
 # 3. 创建 release 分支
 git checkout -b release/v1.0.0
 # 4. 完成发布准备后，合并到 main 和 develop
 git checkout main
 git merge release/v1.0.0
 git tag v1.0.0
 git checkout develop
 git merge release/v1.0.0
 # 5. 处理热修复
 git checkout main
 git checkout -b hotfix/security-patch
 git checkout main
 git merge hotfix/security-patch
 git tag v1.0.1
 git checkout develop
 git merge hotfix/security-patch
```

## 6. 常见问题与解决方案

### 6.1 状态检查问题

#### 6.1.1 状态检查名称错误

- **问题**：Actions job 改名后，保护规则里的旧名称不生效，导致 PR 永远等不到「绿灯」
- **解决方案**：

1.  在 GitHub 上查看最新的状态检查名称
2.  更新分支保护规则中的状态检查名称
3.  重新运行 CI 检查

#### 6.1.2 状态检查超时

- **问题**：CI 检查超时，导致 PR 无法合并
- **解决方案**：

1.  检查 CI 配置，优化构建时间
2.  增加 CI 超时时间
3.  考虑将大型测试拆分为多个任务

### 6.2 分支操作问题

#### 6.2.1 强制推送被禁止

- **问题**：尝试强制推送时收到错误
- **解决方案**：

1.  对于保护的分支，避免使用强制推送
2.  如果确实需要，联系仓库管理员临时允许强制推送
3.  考虑使用 `git push --force-with-lease` 代替 `git push --force`

#### 6.2.2 分支合并冲突

- **问题**：PR 合并时出现冲突
- **解决方案**：

1.  在本地解决冲突：

```bash
 git checkout feature-branch
 git pull origin main
 # 解决冲突
 git add .
 git commit -m "Resolve merge conflicts"
 git push
```

2.  使用 GitHub 网页界面解决冲突

### 6.3 权限问题

#### 6.3.1 无法推送至保护分支

- **问题**：收到「You are not allowed to push code to this branch」错误
- **解决方案**：

1.  确认是否有推送权限
2.  对于保护的分支，使用 PR 流程而不是直接推送
3.  联系仓库管理员调整权限

#### 6.3.2 无法批准自己的 PR

- **问题**：GitHub 不允许作者批准自己的 PR
- **解决方案**：

1.  邀请团队成员审查 PR
2.  确保 CODEOWNERS 配置正确

## 7. 最佳实践

### 7.1 分支命名规范

- **feature 分支**：`feature/功能描述`，如 `feature/add-login`
- **bugfix 分支**：`bugfix/问题描述`，如 `bugfix/fix-login-error`
- **hotfix 分支**：`hotfix/问题描述`，如 `hotfix/security-patch`
- **release 分支**：`release/版本号`，如 `release/v1.0.0`

### 7.2 合并策略

- **默认分支**：选择一种合并策略并保持一致
- **Squash merge**：将多个提交压缩为一个，保持历史简洁
- **Merge commit**：保留所有提交历史
- **Rebase and merge**：将提交重新基于目标分支，创建线性历史

### 7.3 分支保护策略

- **生产分支（main/master）**：最严格的保护，要求多人审查和所有状态检查通过
- **开发分支（develop）**：中等保护，要求至少一人审查和状态检查通过
- **功能分支（feature/\*）**：最少保护，允许开发者自由操作

### 7.4 CI/CD 集成

- **状态检查**：配置必要的 CI 检查，如代码质量、单元测试、构建等
- **部署流水线**：设置自动化部署流程，确保合并到 main 分支后自动部署
- **环境隔离**：使用不同的环境（开发、测试、生产）进行部署

### 7.5 团队协作

- **CODEOWNERS**：为不同模块设置明确的代码所有者
- **PR 模板**：使用 PR 模板，确保 PR 包含必要的信息
- **分支清理**：定期清理已合并的分支，保持仓库整洁
- **文档**：记录分支模型和工作流程，确保团队成员理解并遵循

## 8. 实际应用案例

### 8.1 大型开源项目

#### 8.1.1 案例描述

- **项目**：一个大型前端框架
- **分支模型**：Git Flow
- **保护规则**：
- `main` 分支：要求 2 人审查，所有 CI 检查通过
- `develop` 分支：要求 1 人审查，所有 CI 检查通过
- `release/*` 分支：要求 2 人审查，所有 CI 检查通过

#### 8.1.2 工作流程

1. 贡献者从 `develop` 分支创建 feature 分支
2. 完成开发后，打开 PR 到 `develop` 分支
3. 经过审查和 CI 检查后，合并到 `develop`
4. 当准备发布时，从 `develop` 创建 `release/*` 分支
5. 在 `release/*` 分支上进行测试和修复
6. 完成后，合并到 `main` 和 `develop`
7. 如有紧急问题，从 `main` 创建 hotfix 分支

### 8.2 中小型团队项目

#### 8.2.1 案例描述

- **项目**：一个 Web 应用
- **分支模型**：GitHub Flow
- **保护规则**：
- `main` 分支：要求 1 人审查，所有 CI 检查通过

#### 8.2.2 工作流程

1. 开发者从 `main` 分支创建 feature 分支
2. 完成开发后，打开 PR 到 `main` 分支
3. 经过审查和 CI 检查后，合并到 `main`
4. 合并后自动部署到生产环境

## 9. 延伸阅读

- [GitHub Flow 指南](https://docs.github.com/en/get-started/using-github/github-flow) <!-- nofollow -->
- [Git Flow 工作流](https://nvie.com/posts/a-successful-git-branching-model/) <!-- nofollow -->
- [GitHub 分支保护规则文档](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches) <!-- nofollow -->
- [CODEOWNERS 文档](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) <!-- nofollow -->

## 创建分支

**基本写法：创建新分支**
`git branch <分支名>`
```bash
# 创建新分支但不切换
git branch feature/login
```

---

**基本写法：创建并切换分支**
`git switch -c <分支名>`
```bash
# 创建新分支并立即切换
git switch -c feature/login
```

---

**基本写法：checkout 方式创建并切换**
`git checkout -b <分支名>`
```bash
# 旧写法创建并切换分支
git checkout -b feature/login
```

---

**基本写法：从指定提交创建分支**
`git switch -c <分支名> <提交ID>`
```bash
# 从指定提交点创建新分支
git switch -c hotfix abc1234
```

---

**基本写法：从远程分支创建**
`git switch -c <本地分支> origin/<远程分支>`
```bash
# 基于远程分支创建本地分支
git switch -c feature origin/feature
```

---

**基本写法：创建追踪远程分支**
`git switch --track origin/<远程分支>`
```bash
# 创建并追踪同名远程分支
git switch --track origin/feature
```

---

## 查看分支

**基本写法：查看本地分支**
`git branch`
```bash
# 列出所有本地分支
git branch
```

---

**基本写法：查看所有分支**
`git branch -a`
```bash
# 列出本地和远程所有分支
git branch -a
```

---

**基本写法：查看远程分支**
`git branch -r`
```bash
# 仅列出远程分支
git branch -r
```

---

**基本写法：查看分支追踪信息**
`git branch -vv`
```bash
# 查看分支追踪关系和最新提交
git branch -vv
```

---

**基本写法：按最新提交排序**
`git branch --sort=-committerdate`
```bash
# 按最近提交时间排序分支
git branch --sort=-committerdate
```

---

**基本写法：查看已合并分支**
`git branch --merged`
```bash
# 查看已合并到当前分支的分支
git branch --merged
```

---

**基本写法：查看未合并分支**
`git branch --no-merged`
```bash
# 查看未合并到当前分支的分支
git branch --no-merged
```

---

## 切换分支

**基本写法：切换到指定分支**
`git switch <分支名>`
```bash
# 切换到指定分支（推荐写法）
git switch main
```

---

**基本写法：checkout 切换分支**
`git checkout <分支名>`
```bash
# 旧写法切换分支
git checkout main
```

---

**基本写法：切换到上一个分支**
`git switch -`
```bash
# 快速切换到上次所在的分支
git switch -
```

---

**基本写法：checkout 切换上一分支**
`git checkout -`
```bash
# 旧写法切换到上一个分支
git checkout -
```

---

**基本写法：切换到远程分支**
`git switch <远程分支名>`
```bash
# 自动追踪同名远程分支并切换
git switch origin/feature
```

---

## 删除分支

**基本写法：删除已合并分支**
`git branch -d <分支名>`
```bash
# 删除已合并的本地分支
git branch -d feature/login
```

---

**基本写法：强制删除分支**
`git branch -D <分支名>`
```bash
# 强制删除未合并的分支
git branch -D feature/abandoned
```

---

**基本写法：删除远程分支**
`git push origin --delete <分支名>`
```bash
# 删除远程仓库的分支
git push origin --delete old-feature
```

---

**基本写法：删除远程分支（替代方式）**
`git push origin :<分支名>`
```bash
# 通过推送空分支删除远程分支
git push origin :old-feature
```

---

## 重命名分支

**基本写法：重命名当前分支**
`git branch -m <新名>`
```bash
# 重命名当前所在分支
git branch -m main
```

---

**基本写法：重命名指定分支**
`git branch -m <旧名> <新名>`
```bash
# 重命名指定分支
git branch -m old-name new-name
```

---

**基本写法：重命名远程分支**
`git push origin :<旧名> <新名>`
```bash
# 删除旧远程分支并推送新名分支
git push origin :old-feature new-feature
```

---

**基本写法：设置新上游**
`git branch -u origin/<新名>`
```bash
# 为重命名后的分支设置新的追踪关系
git branch -u origin/new-feature
```

---

## 分支关联管理

**基本写法：设置上游分支**
`git branch --set-upstream-to=origin/<分支名>`
```bash
# 为当前分支设置远程追踪
git branch --set-upstream-to=origin/main
```

---

**基本写法：设置上游（短写法）**
`git branch -u origin/<分支名>`
```bash
# 设置当前分支的远程追踪
git branch -u origin/main
```

---

**基本写法：取消上游关联**
`git branch --unset-upstream`
```bash
# 移除当前分支的远程追踪关系
git branch --unset-upstream
```

---

**基本写法：查看所有分支的追踪关系**
`git branch -vv`
```bash
# 显示各分支的远程追踪状态
git branch -vv
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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| GitHub 概述 | 001-GitHubOverview | 本文的前置基础 |
| 账户注册与双因素认证（2FA） | 002-AccountRegister2FA2FA | 本文的并列主题 |
| 仓库创建、克隆、归档、删除 | 003-RepositoryCreateCloneArchiveDelete | 本文的并列主题 |
| SSH 与 HTTPS 远程配置 | 004-SSHHTTPS | 本文的并列主题 |
| 协作开发规范 | 005-CollaborationDevelopmentStandard | 本文的并列主题 |
| README文件 | 006-READMEFile | 本文的并列主题 |
| 分支模型与分支保护规则 | 007-BranchModelBranchRule | 本文自身 |
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
