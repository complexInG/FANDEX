---
order: 30
tags:
  - github
difficulty: intermediate
title: 'SSH 与 HTTPS 远程配置'
module: github
category: 'GitHub Basics'
description: 'SSH 与 HTTPS 远程配置对比、公钥配置、HTTPS+PAT 配置指南。'
author: Anonymous
related:
  - github/账户注册与双因素认证(2FA)
  - 'github/仓库创建-克隆-归档-删除'
  - github/协作开发规范
  - github/README文件
prerequisites: []
updated: '2026-08-01'
---

## 1. 背景

与远程 **GitHub 仓库（repository）** 通信是日常开发中不可或缺的操作，主要有两种认证方式：

- **SSH（Secure Shell）**：使用非对称密钥对进行认证
- **HTTPS**：使用 **PAT（个人访问令牌）** 作为密码替代
  选择哪种方式取决于多种因素，如团队规范、网络环境、安全性要求等。本指南将详细介绍两种方式的配置和使用方法。

## 2. 原理对比

| 特性       | SSH                        | HTTPS                  |
| ---------- | -------------------------- | ---------------------- |
| 认证方式   | 非对称密钥对（公钥/私钥）  | 用户名 + PAT           |
| 端口       | 22                         | 443                    |
| 安全性     | 高（私钥本地存储）         | 中（PAT 需要妥善保管） |
| 网络兼容性 | 可能被防火墙阻止           | 几乎所有网络都支持     |
| 配置复杂度 | 稍高（需要生成和管理密钥） | 简单（只需生成 PAT）   |
| 适用场景   | 高频推送、多设备开发       | 偶尔操作、受限网络环境 |

## 3. SSH：生成密钥与配置

### 3.1 生成 SSH 密钥

#### 3.1.1 使用 Ed25519 算法（推荐）

```bash
 # Windows 系统
 ssh-keygen -t ed25519 -C "you@example.com" -f "%USERPROFILE%\.ssh\id_ed25519_github" -N ""
 # macOS/Linux 系统
 ssh-keygen -t ed25519 -C "you@example.com" -f "~/.ssh/id_ed25519_github" -N ""
 # 参数说明：
 # -t ed25519：使用 Ed25519 算法，更安全且密钥文件更小
 # -C "you@example.com"：添加注释，通常使用邮箱
 # -f：指定密钥文件路径和名称
 # -N ""：设置空密码短语，生产环境建议设置密码短语
```

#### 3.1.2 使用 RSA 算法（兼容性更好）

```bash
 # Windows 系统
 ssh-keygen -t rsa -b 4096 -C "you@example.com" -f "%USERPROFILE%\.ssh\id_rsa_github" -N ""
 # macOS/Linux 系统
 ssh-keygen -t rsa -b 4096 -C "you@example.com" -f "~/.ssh/id_rsa_github" -N ""
 # 参数说明：
 # -t rsa：使用 RSA 算法
 # -b 4096：密钥长度为 4096 位
```

### 3.2 查看和复制公钥

```bash
 # Windows 系统
 type %USERPROFILE%\.ssh\id_ed25519_github.pub
 # macOS/Linux 系统
 cat ~/.ssh/id_ed25519_github.pub
 # 复制输出的公钥内容，包括 ssh-ed25519 前缀和邮箱后缀
```

### 3.3 在 GitHub 上添加公钥

1. 登录 GitHub，点击头像 → Settings → SSH and GPG keys
2. 点击 "New SSH key" 按钮
3. 在 "Title" 字段中输入密钥名称（如 "My Laptop"）
4. 在 "Key" 字段中粘贴复制的公钥内容
5. 点击 "Add SSH key" 按钮完成添加
   **截图占位**：`[图 02-1] SSH 公钥已添加列表`

### 3.4 测试 SSH 连接

```bash
 # 测试默认 GitHub 连接
 ssh -T git@github.com
 # 测试指定密钥文件的连接
 ssh -i "%USERPROFILE%\.ssh\id_ed25519_github" -T git@github.com # Windows
 ssh -i "~/.ssh/id_ed25519_github" -T git@github.com # macOS/Linux
 # 首次连接会提示验证主机指纹，确认后输入 yes
 # 成功时显示：Hi username! You've successfully authenticated...
```

### 3.5 配置 ssh-agent 管理密钥

```bash
 # 启动 ssh-agent
 # Windows 系统
 Start-Service ssh-agent # PowerShell
 # 或
 ssh-agent cmd.exe # CMD
 # macOS/Linux 系统
 eval "$(ssh-agent -s)"
 # 添加私钥到 ssh-agent
 # Windows 系统
 ssh-add "%USERPROFILE%\.ssh\id_ed25519_github"
 # macOS/Linux 系统
 ssh-add ~/.ssh/id_ed25519_github
 # 查看已添加的密钥
 ssh-add -l
```

### 3.6 多账户配置：SSH config

```sshconfig
 # 文件路径：~/.ssh/config（Windows 同路径）
 # 个人 GitHub 账户
 Host github.com-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal
  IdentitiesOnly yes # 只使用指定的密钥
 # 工作 GitHub 账户
 Host github.com-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
  IdentitiesOnly yes
 # 配置说明：
 # Host：自定义主机别名
 # HostName：实际主机名
 # User：登录用户名，GitHub 固定为 git
 # IdentityFile：指定使用的私钥文件
 # IdentitiesOnly：只使用配置中指定的密钥
```

### 3.7 使用 SSH 克隆和推送

```bash
 # 使用默认 SSH 配置克隆
 git clone git@github.com:username/repository.git
 # 使用指定账户克隆
 git clone git@github.com-personal:username/personal-repo.git
 git clone git@github.com-work:company/work-repo.git
 # 推送代码
 cd repository
 git add .
 git commit -m "Update files"
 git push origin main
```

## 4. HTTPS：PAT 与凭据管理

### 4.1 生成个人访问令牌 (PAT)

#### 4.1.1 生成 Fine-grained token（推荐）

1. 登录 GitHub，点击头像 → Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. 点击 "Generate new token" 按钮
3. 填写以下信息：

- Token name：令牌名称（如 "My Laptop HTTPS"）
- Expiration：过期时间（建议 30-90 天）
- Repository access：选择访问权限（可选择特定仓库或所有仓库）
- Permissions：根据需要选择具体权限

4. 点击 "Generate token" 按钮
5. 复制生成的令牌，离开页面后将无法再次查看

#### 4.1.2 生成 Classic token

1. 登录 GitHub，点击头像 → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 点击 "Generate new token" → "Generate new token (classic)"
3. 填写以下信息：

- Note：令牌名称
- Expiration：过期时间
- Scopes：选择所需权限（如 `repo`、`gist` 等）

4. 点击 "Generate token" 按钮
5. 复制生成的令牌
   **截图占位**：`[图 02-2] Fine-grained token 权限勾选界面`

### 4.2 配置 Git 凭据管理

```bash
 # Windows 系统：使用 Git Credential Manager
 git config --global credential.helper manager
 # macOS 系统：使用 osxkeychain
 git config --global credential.helper osxkeychain
 # Linux 系统：使用 libsecret
 git config --global credential.helper libsecret
 # 验证配置
 git config --global --get credential.helper
```

### 4.3 使用 HTTPS 克隆和推送

```bash
 # 克隆仓库
 git clone https://github.com/username/repository.git
 # 首次推送时，系统会提示输入用户名和密码：
 # 用户名：GitHub 用户名
 # 密码：粘贴生成的 PAT
 # 查看远程配置
 git remote -v
 # 更改远程 URL 从 SSH 到 HTTPS
 git remote set-url origin https://github.com/username/repository.git
 # 更改远程 URL 从 HTTPS 到 SSH
 git remote set-url origin git@github.com:username/repository.git
```

### 4.4 管理 PAT

- **定期轮换**：设置合理的过期时间，到期前生成新令牌
- **最小权限**：只授予必要的权限范围
- **安全存储**：使用密码管理器存储 PAT，避免明文存储
- **撤销令牌**：当设备丢失或令牌泄露时，及时在 GitHub 上撤销

## 5. 常见问题与解决方案

| 问题                          | 原因                                                             | 解决方案                                                        |
| ----------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------- |
| Permission denied (publickey) | 公钥未添加到 GitHub、私钥未加载到 ssh-agent、SSH config 配置错误 | 检查公钥是否已添加、使用 ssh-add 加载私钥、检查 SSH config 配置 |
| Host key verification failed  | 主机指纹不匹配，可能是中间人攻击                                 | 确认 GitHub 官方指纹后再连接                                    |
| PAT 过期                      | Classic token 设置了有效期                                       | 生成新的 PAT 并更新凭据                                         |
| HTTPS 连接失败                | 网络问题、代理设置、企业 MITM                                    | 检查网络连接、配置代理、信任企业根证书                          |
| 多账户认证冲突                | 多个 SSH 密钥或 PAT 管理混乱                                     | 使用 SSH config 配置多账户、为不同账户使用不同 PAT              |

### 5.1 故障诊断脚本

```bash
 # 检查 SSH 配置
 ssh -v git@github.com # 详细输出 SSH 连接过程
 # 检查 Git 远程配置
 git remote -v
 # 检查 Git 凭据配置
 git config --list | grep credential
 # 测试 HTTPS 连接
 git ls-remote https://github.com/username/repository.git
 # 测试 SSH 连接
 git ls-remote git@github.com:username/repository.git
```

## 6. 最佳实践

### 6.1 SSH 最佳实践

- **使用 Ed25519 算法**：更安全且密钥文件更小
- **设置密码短语**：为私钥设置密码短语，增加安全性
- **合理命名密钥**：为不同用途的密钥使用明确的命名（如 id_ed25519_personal、id_ed25519_work）
- **权限设置**：
- Linux/macOS：`chmod 600 ~/.ssh/id_ed25519_*`
- Windows：使用 OpenSSH 默认权限
- **定期备份**：备份私钥文件到安全位置
- **使用 ssh-agent**：避免每次操作都输入密码短语

### 6.2 HTTPS 最佳实践

- **使用 Fine-grained token**：提供更精细的权限控制
- **设置合理过期时间**：建议 30-90 天
- **最小权限原则**：只授予必要的权限
- **使用凭据管理器**：避免每次操作都输入 PAT
- **定期轮换**：到期前生成新令牌
- **CI/CD 环境**：使用 GitHub Actions 提供的 `GITHUB_TOKEN`，不使用个人 PAT

### 6.3 团队协作最佳实践

- **统一认证方式**：团队内统一使用 SSH 或 HTTPS
- **文档化配置**：创建团队配置文档，包含认证方式和步骤
- **密钥管理**：建立密钥轮换和备份策略
- **安全审计**：定期检查已添加的 SSH 密钥和 PAT

## 7. 高级配置

### 7.1 使用 SSH 代理

```bash
 # 配置 SSH 通过代理连接
 # ~/.ssh/config
 Host github.com
  HostName github.com
  User git
  ProxyCommand nc -X 5 -x proxy.example.com:1080 %h %p
  IdentityFile ~/.ssh/id_ed25519_github
```

### 7.2 自动加载 SSH 密钥

```bash
 # Windows：在 PowerShell 配置文件中添加
 # ~/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1
 Start-Service ssh-agent
 ssh-add ~/.ssh/id_ed25519_github
 # macOS/Linux：在 ~/.bashrc 或 ~/.zshrc 中添加
 if [ -z "$SSH_AUTH_SOCK" ]; then
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519_github
 fi
```

### 7.3 多仓库配置示例

```bash
 # 个人仓库使用 SSH
 git remote set-url origin git@github.com-personal:username/personal-repo.git
 # 工作仓库使用 HTTPS
 git remote set-url origin https://github.com/company/work-repo.git
 # 检查配置
 git remote -v
```

## 延伸阅读

- [GitHub：SSH 密钥](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) <!-- nofollow -->
- [GitHub：创建个人访问令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) <!-- nofollow -->
- [GitHub：使用 SSH 代理](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding) <!-- nofollow -->
- [Git 官方文档：凭据存储](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) <!-- nofollow -->

## 参考文献

GitHub 文档：https://docs.github.com/zh
GitHub Actions 文档：https://docs.github.com/zh/actions
GitHub REST API：https://docs.github.com/zh/rest
GitHub GraphQL API：https://docs.github.com/zh/graphql

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
| SSH 与 HTTPS 远程配置 | 004-SSHHTTPS | 本文自身 |
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
