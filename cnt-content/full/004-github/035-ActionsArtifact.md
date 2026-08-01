---
order: 104
title: Actions制品传递
module: github
category: toolchain
difficulty: intermediate
description: 'GitHub Actions制品（Artifacts）详解：跨Job传递构建产物、上传下载与生命周期管理。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/Actions缓存依赖
  - github/Actions自托管运行器
  - github/Actions环境部署
prerequisites:
  - github/GitHub概述
---

## 1. 制品概述

### 1.1 什么是制品

制品（Artifacts）是工作流运行过程中产生的文件，如构建产物、测试报告、日志等。制品允许在 Job 之间传递数据，或在工作流完成后下载查看。

```mermaid
flowchart LR
    JA[Job A 构建<br/>编译代码<br/>上传制品] -->|制品| JB[Job B 测试<br/>下载制品 运行测试<br/>上传报告] -->|报告| JC[Job C 部署<br/>下载制品 部署]
```

### 1.2 制品限制

| 限制项             | 值                  |
| ------------------ | ------------------- |
| 单个制品大小       | 最大 2 GB（压缩后） |
| 单个工作流制品总数 | 最大 10 个          |
| 仓库总制品大小     | 最大 80 GB          |
| 保留时间           | 默认 90 天          |

## 2. actions/upload-artifact 与 download-artifact

### 2.1 上传制品

```yaml
- name: Upload build artifacts
  uses: actions/upload-artifact@v4
  with:
    name: dist-files # 制品名称（在同一工作流中唯一）
    path: | # 要上传的路径
      dist/
      package.json
    retention-days: 5 # 保留天数（默认 90）
    compression-level: 6 # 压缩级别 0-9（默认 6）
    if-no-files-found: error # 无文件时的行为: error|warn|ignore
```

### 2.2 下载制品

```yaml
- name: Download build artifacts
  uses: actions/download-artifact@v4
  with:
    name: dist-files # 指定制品名称
    path: dist/ # 下载到指定目录
```

下载所有制品：

```yaml
- name: Download all artifacts
  uses: actions/download-artifact@v4
  # 不指定 name，下载所有制品
```

### 2.3 v4 版本变更

`actions/upload-artifact@v4` 和 `actions/download-artifact@v4` 的关键变更：

| 变更项       | v3           | v4                   |
| ------------ | ------------ | -------------------- |
| 制品名称冲突 | 自动覆盖     | 报错，必须唯一       |
| 跨工作流下载 | 默认可下载   | 需指定 `run-id`      |
| 上传合并     | 同名自动合并 | 不再自动合并         |
| 性能         | -            | 显著提升（增量上传） |

## 3. 跨 Job 传递

### 3.1 同工作流内传递

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          path: dist/
      - run: npm test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          path: dist/
      - run: npm run deploy
```

### 3.2 多制品传递

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          npm run build:web
          npm run build:mobile
      - uses: actions/upload-artifact@v4
        with:
          name: web-build
          path: dist/web/
      - uses: actions/upload-artifact@v4
        with:
          name: mobile-build
          path: dist/mobile/

  test-web:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: web-build

  test-mobile:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: mobile-build
```

### 3.3 矩阵构建中的制品

```yaml
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build-${{ matrix.os }} # 名称包含矩阵变量
          path: dist/
```

## 4. 跨工作流传递

### 4.1 使用 download-artifact 下载其他工作流的制品

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          run-id: ${{ github.event.workflow_run.id }} # 指定工作流运行 ID
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

### 4.2 使用 workflow_run 触发器

```yaml
# deploy.yml
on:
  workflow_run:
    workflows: ['Build']
    types: [completed]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          run-id: ${{ github.event.workflow_run.id }}
```

## 5. 典型应用场景

### 5.1 测试报告

```yaml
- name: Run tests
  run: npm test -- --reporter=json --output=test-results.json

- name: Upload test results
  if: always() # 即使测试失败也上传
  uses: actions/upload-artifact@v4
  with:
    name: test-results
    path: test-results.json
    retention-days: 7
```

### 5.2 代码覆盖率

```yaml
- name: Generate coverage
  run: npm run coverage

- name: Upload coverage report
  uses: actions/upload-artifact@v4
  with:
    name: coverage-report
    path: coverage/
    retention-days: 14
```

### 5.3 构建产物分发

```yaml
- name: Build all platforms
  run: npm run build:all

- name: Upload Linux binary
  uses: actions/upload-artifact@v4
  with:
    name: app-linux
    path: dist/app-linux

- name: Upload macOS binary
  uses: actions/upload-artifact@v4
  with:
    name: app-macos
    path: dist/app-macos

- name: Upload Windows binary
  uses: actions/upload-artifact@v4
  with:
    name: app-windows
    path: dist/app-windows
```

### 5.4 调试快照

```yaml
- name: Upload debug snapshot
  if: failure() # 仅在失败时上传
  uses: actions/upload-artifact@v4
  with:
    name: debug-snapshot-${{ github.run_id }}
    path: |
      logs/
      screenshots/
      cypress/videos/
    retention-days: 3
```

## 6. 制品管理

### 6.1 清理策略

```yaml
# 设置短保留期以节省空间
- uses: actions/upload-artifact@v4
  with:
    name: temp-build
    path: dist/
    retention-days: 1 # 1 天后自动删除
```

### 6.2 手动删除

```bash
# 使用 GitHub CLI 删除制品
gh api repos/OWNER/REPO/actions/artifacts \
  --jq '.artifacts[] | select(.name == "temp-build") | .id' | \
  xargs -I {} gh api repos/OWNER/REPO/actions/artifacts/{} --method DELETE
```

### 6.3 制品大小优化

```yaml
# 排除不必要的文件
- uses: actions/upload-artifact@v4
  with:
    name: build
    path: |
      dist/
      !dist/**/*.map    # 排除 source map
    compression-level: 9 # 最高压缩
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
| Actions制品传递 | 035-ActionsArtifact | 本文自身 |
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
