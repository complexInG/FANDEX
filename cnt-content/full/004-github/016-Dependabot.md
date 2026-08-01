---
order: 59
title: Dependabot
module: github
category: GitHub
difficulty: intermediate
description: Dependabot详解：依赖项自动更新、版本升级与配置最佳实践。
author: fanquanpp
updated: '2026-08-01'
related:
  - github/社区讨论
  - github/AI编程助手
  - 'github/Issues模板-标签与里程碑'
  - github/密钥扫描
prerequisites:
  - github/GitHub概述
---

## 1. Dependabot 概述

### 1.1 什么是 Dependabot

Dependabot 是 GitHub 内置的**依赖管理机器人**，自动检测和更新项目依赖。

### 1.2 两种更新类型

| 类型                 | 触发条件     | 说明            |
| :------------------- | :----------- | :-------------- |
| **Security Updates** | 发现安全漏洞 | 自动创建修复 PR |
| **Version Updates**  | 定期检查     | 保持依赖最新    |

## 2. 配置文件

### 2.1 基本配置

```yaml
# .github/dependabot.yml
version: 2
updates:
  # npm 依赖
  - package-ecosystem: 'npm'
    directory: '/'
    schedule:
      interval: 'weekly'
      day: 'monday'
      time: '09:00'
      timezone: 'Asia/Shanghai'

  # Python 依赖
  - package-ecosystem: 'pip'
    directory: '/backend'
    schedule:
      interval: 'monthly'

  # GitHub Actions
  - package-ecosystem: 'github-actions'
    directory: '/'
    schedule:
      interval: 'weekly'
```

### 2.2 完整配置

```yaml
version: 2
updates:
  - package-ecosystem: 'npm'
    directory: '/'
    schedule:
      interval: 'weekly'
    open-pull-requests-limit: 5
    reviewers:
      - 'dev-team'
    assignees:
      - 'tech-lead'
    labels:
      - 'dependencies'
      - 'automated'
    commit-message:
      prefix: 'chore'
      prefix-development: 'chore'
      include: 'scope'
    ignore:
      - dependency-name: 'express'
        versions: ['>=5.0.0']
      - dependency-name: 'lodash'
    allow:
      - dependency-type: 'production'
    rebase-strategy: 'auto'
    target-branch: 'develop'
    vendor: false
```

## 3. 支持的生态系统

| 生态系统           | 配置值           | 锁定文件            |
| :----------------- | :--------------- | :------------------ |
| **npm**            | `npm`            | `package-lock.json` |
| **yarn**           | `npm`            | `yarn.lock`         |
| **pip**            | `pip`            | `requirements.txt`  |
| **Maven**          | `maven`          | `pom.xml`           |
| **Gradle**         | `gradle`         | `build.gradle`      |
| **Go**             | `gomod`          | `go.sum`            |
| **Cargo**          | `cargo`          | `Cargo.lock`        |
| **NuGet**          | `nuget`          | `*.csproj`          |
| **GitHub Actions** | `github-actions` | 工作流文件          |
| **Docker**         | `docker`         | `Dockerfile`        |

## 4. 版本更新策略

### 4.1 更新频率

| 频率       | 配置值     | 适用场景 |
| :--------- | :--------- | :------- |
| **每天**   | `daily`    | 活跃开发 |
| **每周**   | `weekly`   | 推荐     |
| **每两周** | `biweekly` | 稳定项目 |
| **每月**   | `monthly`  | 维护模式 |

### 4.2 控制更新范围

```yaml
# 只更新生产依赖
allow:
  - dependency-type: 'production'

# 只更新指定依赖
allow:
  - dependency-name: 'express'
  - dependency-name: 'lodash'

# 忽略大版本升级
ignore:
  - dependency-name: 'webpack'
    versions: ['>=5.0.0']
```

## 5. 自动合并

### 5.1 GitHub Actions 自动合并

```yaml
# .github/workflows/auto-merge.yml
name: Auto Merge Dependabot
on: pull_request

permissions:
  pull-requests: write
  contents: write

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    if: ${{ github.actor == 'dependabot[bot]' }}
    steps:
      - name: Enable auto-merge
        run: gh pr merge --auto --merge "$PR_URL"
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 5.2 条件自动合并

```yaml
# 只自动合并补丁版本
- name: Check and auto-merge
  run: |
    if [[ "$(gh pr view --json labels -q '.labels[].name')" == *"dependencies"* ]]; then
      gh pr merge --auto --squash "$PR_URL"
    fi
```

## 6. 最佳实践

- 提交锁定文件，让 Dependabot 精确解析依赖
- 设置 `open-pull-requests-limit` 避免过多 PR
- 使用 `ignore` 控制大版本升级
- 为 Dependabot PR 设置自动 CI 测试
- 定期审查和合并 Dependabot PR

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
