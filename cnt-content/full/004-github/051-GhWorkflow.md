---
order: 510
title: gh workflow 工作流命令速查手册
module: github

category: '004-github'
difficulty: beginner
description: gh workflow 工作流命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 查看工作流

**基本用法:列出工作流**
`gh workflow list`

```bash
# 列出所有工作流
gh workflow list

# 查看某工作流详情
gh workflow view deploy.yml

# 在浏览器中打开
gh workflow view deploy.yml --web
```

---

## 手动触发

**基本用法:触发工作流**
`gh workflow run <工作流>`

```bash
# 手动触发工作流
gh workflow run deploy.yml

# 指定分支触发
gh workflow run deploy.yml --ref feature

# 传入参数
gh workflow run deploy.yml -f environment=production -f version=1.2.3

# 从 JSON 文件读取参数
gh workflow run deploy.yml --raw-field config=@config.json
```

---

## 启用与禁用

**基本用法:启用工作流**
`gh workflow enable <工作流>`

```bash
# 启用被禁用的工作流
gh workflow enable deploy.yml
```

---

**基本用法:禁用工作流**
`gh workflow disable <工作流>`

```bash
# 临时禁用工作流
gh workflow disable deploy.yml
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
