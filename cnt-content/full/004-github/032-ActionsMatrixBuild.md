---
order: 101
title: Actions矩阵构建
module: github
category: toolchain
difficulty: advanced
description: 'GitHub Actions矩阵策略详解：多操作系统、多版本、多配置的并行构建。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/Actions触发器
  - github/常见问题排查
  - github/Actions缓存依赖
  - github/Actions自托管运行器
prerequisites:
  - github/GitHub概述
---

# GitHub Actions 矩阵策略速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 矩阵策略基础

### 1.1 基本概念

矩阵策略（Matrix Strategy）允许你通过变量组合创建多个并行 Job，一次配置即可在多种环境下测试。

```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node-version: [18, 20, 22]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm test
```

上述配置会生成 $3 \times 3 = 9$ 个并行 Job。

### 1.2 矩阵变量类型

| 类型   | 示例                          | 说明           |
| ------ | ----------------------------- | -------------- |
| 字符串 | `os: [ubuntu-latest]`         | 最常用         |
| 数字   | `node-version: [18, 20]`      | 自动转为字符串 |
| 布尔值 | `experimental: [true, false]` | 自动转为字符串 |
| 对象   | `include: [{...}]`            | 复杂配置       |

## 2. 矩阵组合

### 2.1 笛卡尔积

默认行为是所有变量的笛卡尔积：

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest] # 2 个值
    python: ['3.10', '3.11', '3.12'] # 3 个值
# 结果: 2 × 3 = 6 个 Job
```

### 2.2 include — 添加额外组合

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    python: ['3.11', '3.12']
    include:
      - os: macos-latest
        python: '3.12'
        experimental: true
      - os: ubuntu-latest
        python: '3.13-dev'
        experimental: true
# 基础: 2 × 2 = 4 + 2 = 6 个 Job
```

`include` 中的条目：

- 如果匹配已有组合，则**追加变量**
- 如果不匹配，则**新增一个 Job**

### 2.3 exclude — 排除组合

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    python: ['3.10', '3.11', '3.12']
    exclude:
      - os: windows-latest
        python: '3.10' # 不在 Windows + Python 3.10 上测试
      - os: ubuntu-latest
        python: '3.10' # 不在 Ubuntu + Python 3.10 上测试
# 结果: 6 - 2 = 4 个 Job
```

### 2.4 include 与 exclude 的执行顺序

```
1. 先计算笛卡尔积
2. 应用 exclude 排除组合
3. 应用 include 添加组合
```

## 3. 实战配置

### 3.1 多语言项目

```yaml
jobs:
  build:
    strategy:
      fail-fast: false
      matrix:
        include:
          - language: typescript
            build: npm run build
            test: npm test
          - language: python
            build: pip install -e .
            test: pytest
          - language: go
            build: go build ./...
            test: go test ./...
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: ${{ matrix.build }}
      - name: Test
        run: ${{ matrix.test }}
```

### 3.2 浏览器兼容性测试

```yaml
jobs:
  e2e:
    strategy:
      fail-fast: false
      matrix:
        browser: [chromium, firefox, webkit]
        shard: [1/4, 2/4, 3/4, 4/4]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx playwright test --project=${{ matrix.browser }} --shard=${{ matrix.shard }}
```

### 3.3 容器镜像构建

```yaml
jobs:
  docker:
    strategy:
      matrix:
        platform: [linux/amd64, linux/arm64]
    runs-on: ubuntu-latest
    steps:
      - uses: docker/setup-qemu-action@v3
      - uses: docker/setup-buildx-action@v3
      - uses: docker/build-push-action@v5
        with:
          platforms: ${{ matrix.platform }}
          push: true
          tags: myapp:latest-${{ matrix.platform == 'linux/amd64' && 'amd64' || 'arm64' }}
```

## 4. fail-fast 与并发控制

### 4.1 fail-fast

```yaml
strategy:
  fail-fast: true # 默认值，任一 Job 失败则取消其他 Job
  # fail-fast: false  # 所有 Job 都执行完毕
```

建议在 CI 场景设为 `false`，以便收集所有环境的失败信息。

### 4.2 max-parallel

```yaml
strategy:
  max-parallel: 4 # 最多同时运行 4 个 Job
  matrix:
    os: [ubuntu, macos, windows]
    node: [18, 20, 22]
# 9 个 Job，但最多 4 个并行
```

### 4.3 Job 级别并发

```yaml
concurrency:
  group: ci-${{ github.ref }}-${{ matrix.os }}-${{ matrix.node-version }}
  cancel-in-progress: true
```

## 5. 动态矩阵

### 5.1 使用 JSON 生成矩阵

```yaml
jobs:
  setup:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run: |
          echo "matrix={\"include\":$(ls packages/ | jq -R -s -c 'split("\n") | map(select(length > 0)) | map({"package": .})')}" >> $GITHUB_OUTPUT

  test:
    needs: setup
    strategy:
      matrix: ${{ fromJson(needs.setup.outputs.matrix) }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "Testing ${{ matrix.package }}"
```

### 5.2 基于文件变更的动态矩阵

```yaml
jobs:
  detect:
    runs-on: ubuntu-latest
    outputs:
      services: ${{ steps.filter.outputs.changes }}
    steps:
      - uses: actions/checkout@v4
      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            auth: src/auth/**
            user: src/user/**
            order: src/order/**

  test:
    needs: detect
    if: needs.detect.outputs.services != '[]'
    strategy:
      matrix:
        service: ${{ fromJson(needs.detect.outputs.services) }}
    runs-on: ubuntu-latest
    steps:
      - run: npm test --workspace=src/${{ matrix.service }}
```

## 6. 矩阵中的条件逻辑

### 6.1 条件步骤

```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - name: Linux only
        if: runner.os == 'Linux'
        run: sudo apt-get update

      - name: macOS only
        if: runner.os == 'macOS'
        run: brew update
```

### 6.2 环境变量差异化

```yaml
strategy:
  matrix:
    include:
      - os: ubuntu-latest
        env: { CC: gcc, CXX: g++ }
      - os: macos-latest
        env: { CC: clang, CXX: clang++ }
      - os: windows-latest
        env: { CC: cl, CXX: cl }
```

## 7. 最佳实践

### 7.1 矩阵规模控制

```
推荐矩阵大小: ≤ 20 个 Job
超过 20 个: 考虑拆分工作流或使用动态矩阵
超过 50 个: 必须使用动态矩阵 + 路径过滤
```

### 7.2 资源优化

```yaml
# 快速测试先跑，慢速测试后跑
jobs:
  quick-test:
    strategy:
      matrix:
        node: [22] # 仅最新版本
    runs-on: ubuntu-latest
    steps:
      - run: npm test

  full-test:
    needs: quick-test # 快速测试通过后再跑完整矩阵
    strategy:
      matrix:
        node: [18, 20, 22]
        os: [ubuntu-latest, macos-latest, windows-latest]
```

### 7.3 调试技巧

```yaml
# 查看矩阵展开结果
- name: Debug matrix
  run: echo "${{ toJson(matrix) }}"
```
## 基础矩阵

**基本用法:定义矩阵**
`strategy.matrix`

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [16, 18, 20]
        os: [ubuntu-latest, macos-latest, windows-latest]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

---

## 矩阵组合与排除

**基本用法:排除特定组合**
`strategy.matrix.exclude`

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [18, 20]
    exclude:
      # 跳过 Windows + Node18
      - os: windows-latest
        node: 18
```

---

**基本用法:额外包含组合**
`strategy.matrix.include`

```yaml
strategy:
  matrix:
    node: [18, 20]
    include:
      # 给 node 20 额外加一个变量
      - node: 20
        experimental: true
      # 追加一个完全独立的组合
      - node: 22
        os: ubuntu-latest
```

---

## 失败策略

**基本用法:控制失败行为**
`strategy:`

```yaml
strategy:
  fail-fast: false      # 一个失败不取消其他
  max-parallel: 4       # 最大并行数
  matrix:
    node: [16, 18, 20]
```

---

## 动态矩阵

**基本用法:从 JSON 输出动态生成**
`strategy.matrix: ${{ fromJSON(...) }}`

```yaml
jobs:
  dynamic:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run: echo "matrix=[\"a\",\"b\",\"c\"]" >> $GITHUB_OUTPUT

  use:
    needs: dynamic
    runs-on: ubuntu-latest
    strategy:
      matrix:
        target: ${{ fromJSON(needs.dynamic.outputs.matrix) }}
    steps:
      - run: echo ${{ matrix.target }}
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
| Codespaces | 024-Codespaces | 本文的并列主题 |
| CODEOWNERS | 025-CODEOWNERS | 本文的并列主题 |
| 社区健康文件 | 026-CommunityHealthFile | 本文的并列主题 |
| Pull Request 完整协作流程 | 027-PullRequestCompleteCollaborationFlow | 本文的并列主题 |
| GitHub Pages 多站点方案 | 028-GitHubPagesMultiSolution | 本文的并列主题 |
| GitHub Actions 与 CI/CD | 029-GitHubActionsCICD | 本文的并列主题 |
| Actions触发器 | 030-ActionsTrigger | 本文的并列主题 |
| 常见问题排查 | 031-FAQTroubleshoot | 本文的并列主题 |
| Actions矩阵构建 | 032-ActionsMatrixBuild | 本文自身 |
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
