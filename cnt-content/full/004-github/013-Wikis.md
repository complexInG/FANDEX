---
order: 56
title: Wikis
module: github
category: GitHub
difficulty: beginner
description: 'GitHub Wikis详解：项目文档管理、编辑与协作。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/Fork工作流
  - github/Projects看板
  - github/社区讨论
  - github/AI编程助手
prerequisites:
  - github/GitHub概述
---

## 1. Wikis 概述

### 1.1 什么是 GitHub Wikis

GitHub Wikis 是仓库内置的**文档系统**，适合存放项目文档、教程和设计文档。

### 1.2 Wiki vs README

| 特性     | README     | Wiki             |
| :------- | :--------- | :--------------- |
| **位置** | 仓库根目录 | 独立的 Wiki 区域 |
| **内容** | 项目概览   | 详细文档         |
| **编辑** | 提交代码   | 独立编辑         |
| **结构** | 单文件     | 多页面           |
| **权限** | 同仓库权限 | 可独立配置       |

## 2. 启用和配置

### 2.1 启用 Wiki

1. 仓库 Settings → Features → Wikis → 勾选
2. 访问 `https://github.com/user/repo/wiki`

### 2.2 权限设置

| 选项                   | 说明           |
| :--------------------- | :------------- |
| **Public**             | 所有人可编辑   |
| **Collaborators only** | 仅协作者可编辑 |

## 3. 创建和编辑页面

### 3.1 创建首页

访问 Wiki 页面，点击 "Create the first page"

### 3.2 添加新页面

1. Wiki → New Page
2. 输入标题和内容
3. 选择编辑模式（Markdown 推荐）

### 3.3 侧边栏

创建 `_Sidebar.md` 文件自定义导航：

```markdown
**文档导航**

- [[首页]]
- [[安装指南]]
- [[API 文档]]
  - [[认证 API]]
  - [[用户 API]]
- [[常见问题]]
```

### 3.4 页脚

创建 `_Footer.md` 文件：

```markdown
---

文档最后更新于 2026-06-14
如有问题请提交 [Issue](../../issues)
```

## 4. 本地编辑 Wiki

### 4.1 克隆 Wiki

```bash
# Wiki 是独立的 Git 仓库
git clone https://github.com/user/repo.wiki.git

# 目录结构
repo.wiki/
├── Home.md           ← 首页
├── _Sidebar.md       ← 侧边栏
├── _Footer.md        ← 页脚
├── Installation.md   ← 自定义页面
└── API-Reference.md  ← 自定义页面
```

### 4.2 本地编辑并推送

```bash
cd repo.wiki
vim API-Reference.md
git add .
git commit -m "docs: update API reference"
git push origin master
```

## 5. 最佳实践

- 首页作为目录，链接到其他页面
- 使用 `_Sidebar.md` 统一导航
- 文档与代码变更同步更新
- 使用 Wiki 记录设计决策和架构
- 长文档拆分为多个页面

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
