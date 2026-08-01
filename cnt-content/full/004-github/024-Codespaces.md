---
order: 66
title: Codespaces
module: github
category: GitHub
difficulty: intermediate
description: 'GitHub Codespaces详解：云端开发环境配置、预构建与使用。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/Web钩子
  - github/包管理服务
  - github/代码所有者
  - github/社区健康文件
prerequisites:
  - github/GitHub概述
---

# gh codespace 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. Codespaces 概述

### 1.1 什么是 Codespaces

GitHub Codespaces 是**云端开发环境**，在浏览器或 VS Code 中提供完整的开发环境，无需本地配置。

### 1.2 优势

| 优势       | 说明             |
| :--------- | :--------------- |
| **零配置** | 一键启动开发环境 |
| **一致性** | 团队使用相同环境 |
| **可复现** | 环境定义在代码中 |
| **弹性**   | 按需使用计算资源 |

### 1.3 免费额度

| 账户类型 | 每月核心小时 | 存储空间 |
| :------- | :----------- | :------- |
| **Free** | 120 核心小时 | 15 GB    |
| **Pro**  | 180 核心小时 | 20 GB    |
| **Team** | 按需付费     | 按需付费 |

## 2. 配置开发环境

### 2.1 devcontainer.json

```json
// .devcontainer/devcontainer.json
{
  "name": "My Dev Environment",
  "image": "mcr.microsoft.com/devcontainers/javascript-node:20",
  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "forwardPorts": [3000, 5173],
  "postCreateCommand": "npm install",
  "customizations": {
    "vscode": {
      "extensions": ["dbaeumer.vscode-eslint", "esbenp.prettier-vscode", "vue.volar"],
      "settings": {
        "editor.formatOnSave": true
      }
    }
  }
}
```

### 2.2 Dockerfile 方式

```dockerfile
# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/javascript-node:20

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y postgresql-client

COPY . /workspace
WORKDIR /workspace
RUN npm ci
```

```json
{
  "name": "Custom Environment",
  "build": {
    "dockerfile": "Dockerfile"
  }
}
```

### 2.3 docker-compose 方式

```yaml
# .devcontainer/docker-compose.yml
version: '3.8'
services:
  app:
    build:
      context: ..
      dockerfile: .devcontainer/Dockerfile
    volumes:
      - ..:/workspace
    command: sleep infinity
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: devpassword
    ports:
      - '5432:5432'
```

## 3. 使用 Codespaces

### 3.1 创建 Codespace

```bash
# 通过 GitHub CLI
gh codespace create -r user/repo -b main

# 通过浏览器
# 仓库 → Code → Codespaces → Create codespace
```

### 3.2 管理 Codespaces

```bash
# 列出
gh codespace list

# 连接
gh codespace ssh

# 删除
gh codespace delete

# 查看端口
gh codespace ports
```

### 3.3 机器类型

| 类型        | 核心 | 内存  | 存储  |
| :---------- | :--- | :---- | :---- |
| **2-core**  | 2    | 4 GB  | 32 GB |
| **4-core**  | 4    | 8 GB  | 32 GB |
| **8-core**  | 8    | 16 GB | 32 GB |
| **16-core** | 16   | 32 GB | 32 GB |
| **32-core** | 32   | 64 GB | 32 GB |

## 4. 预构建

### 4.1 配置预构建

1. 仓库 Settings → Codespaces → Prebuilds
2. 选择分支和区域
3. 配置触发条件

### 4.2 预构建工作流

```yaml
# .github/workflows/codespace-prebuild.yml
name: Codespace Prebuild
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'

jobs:
  prebuild:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codespaces-prebuild@v1
        with:
          regions: euWest2, usEast1
```

## 5. 最佳实践

- 使用 `.devcontainer` 定义环境
- 利用预构建加速启动
- 及时删除不用的 Codespaces
- 使用 dotfiles 统一个人配置
- 将敏感信息存储在 Codespace Secrets 中
## 创建与列出

**基本用法:创建 codespace**
`gh codespace create`

```bash
# 交互式创建
gh codespace create

# 指定仓库与分支
gh codespace create --repo owner/repo --branch dev

# 指定机器规格
gh codespace create --machine basicLinux32gb
```

---

**基本用法:列出 codespace**
`gh codespace list`

```bash
# 列出所有 codespace
gh codespace list
```

---

## 连接与操作

**基本用法:SSH 连接**
`gh codespace ssh`

```bash
# 通过 SSH 连接到 codespace
gh codespace ssh -c <codespace名>

# 在 VS Code 中打开
gh codespace code
```

---

**基本用法:查看日志**
`gh codespace logs`

```bash
# 实时查看创建日志
gh codespace logs -c <codespace名>
```

---

**基本用法:查看详情**
`gh codespace view`

```bash
# 查看 codespace 详情
gh codespace view -c <codespace名>
```

---

## 管理生命周期

**基本用法:停止 codespace**
`gh codespace stop`

```bash
# 停止运行中的 codespace
gh codespace stop -c <codespace名>
```

---

**基本用法:重建 codespace**
`gh codespace rebuild`

```bash
# 重建(应用 devcontainer 改动)
gh codespace rebuild -c <codespace名>
```

---

**基本用法:删除 codespace**
`gh codespace delete`

```bash
# 删除指定 codespace
gh codespace delete -c <codespace名> --force

# 删除所有已停止的 codespace
gh codespace delete --days 7
```

---

## 端口管理

**基本用法:查看端口转发**
`gh codespace ports`

```bash
# 列出转发端口
gh codespace ports -c <codespace名>

# 设置端口可见性
gh codespace ports visibility 3000:public -c <codespace名>
```

---

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
| Codespaces | 024-Codespaces | 本文自身 |
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
