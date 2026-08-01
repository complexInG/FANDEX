---
order: 530
title: gh extension 扩展命令速查手册
module: github

category: '004-github'
difficulty: beginner
description: gh extension 扩展命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 安装扩展

**基本用法:安装扩展**
`gh extension install <仓库>`

```bash
# 安装社区扩展
gh extension install dlvhdr/gh-dash

# 安装特定版本
gh extension install dlvhdr/gh-dash --pin v2.0.0
```

---

**基本用法:搜索扩展**
`gh extension search <关键词>`

```bash
# 搜索相关扩展
gh extension search notify
```

---

## 管理扩展

**基本用法:列出扩展**
`gh extension list`

```bash
# 查看已安装扩展
gh extension list
```

---

**基本用法:升级扩展**
`gh extension upgrade`

```bash
# 升级所有扩展
gh extension upgrade --all

# 升级指定扩展
gh extension upgrade gh-dash
```

---

**基本用法:移除扩展**
`gh extension remove <名称>`

```bash
# 卸载扩展
gh extension remove gh-dash
```

---

## 创建扩展

**基本用法:创建扩展脚手架**
`gh extension create <名称>`

```bash
# 创建新扩展(含脚手架)
gh extension create my-ext

# 创建预编译扩展(Go)
gh extension create my-ext --precompiled=go
```

---

**基本用法:本地开发扩展**
`gh extension install <路径>`

```bash
# 以本地目录方式安装用于开发
gh extension install .
```

---

## 浏览扩展

**基本用法:在浏览器打开**
`gh extension browse <名称>`

```bash
# 打开扩展仓库主页
gh extension browse gh-dash
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
