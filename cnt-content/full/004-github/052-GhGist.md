---
order: 520
title: gh gist 代码片段命令速查手册
module: github

category: '004-github'
difficulty: beginner
description: gh gist 代码片段命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 创建 Gist

**基本用法:创建公开 gist**
`gh gist create <文件>`

```bash
# 从文件创建公开 gist
gh gist create snippet.js

# 创建私密 gist(不可搜索但仍可访问)
gh gist create snippet.js --secret

# 从标准输入创建
echo "console.log(1)" | gh gist create -f script.js

# 添加描述
gh gist create note.md --desc "配置笔记"
```

---

## 查看 Gist

**基本用法:列出 gist**
`gh gist list`

```bash
# 列出自己的 gist
gh gist list

# 限制条数
gh gist list --limit 20
```

---

**基本用法:查看 gist 内容**
`gh gist view <ID>`

```bash
# 查看 gist 内容
gh gist view abc123

# 查看原始内容
gh gist view abc123 --raw

# 在浏览器打开
gh gist view abc123 --web
```

---

## 编辑与克隆

**基本用法:编辑 gist**
`gh gist edit <ID>`

```bash
# 编辑 gist 内容
gh gist edit abc123

# 用指定文件替换
gh gist edit abc123 new_content.js
```

---

**基本用法:克隆 gist**
`gh gist clone <ID>`

```bash
# 把 gist 克隆为本地仓库
gh gist clone abc123 my-snippet
```

---

## 删除与重命名

**基本用法:删除 gist**
`gh gist delete <ID>`

```bash
# 删除 gist
gh gist delete abc123 --yes
```

---

**基本用法:重命名文件**
`gh gist rename <ID> <旧名> <新名>`

```bash
# 重命名 gist 中的文件
gh gist rename abc123 old.js new.js
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
