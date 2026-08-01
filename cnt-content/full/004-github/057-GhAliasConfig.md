---
order: 570
title: gh alias 与 config 命令速查手册
module: github

category: '004-github'
difficulty: beginner
description: gh alias 与 config 命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 别名管理

**基本用法:设置命令别名**
`gh alias set <别名> <展开>`

```bash
# 为 pr checkout 设置别名
gh alias set co "pr checkout"

# 设置 shell 别名(支持管道与变量)
gh alias set recent "run list --limit 5" --shell

# 列出全部别名
gh alias list

# 删除别名
gh alias delete co

# 从 YAML 文件导入别名
gh alias import aliases.yml --clobber
```

---

## 配置项

**基本用法:读取配置**
`gh config get <键>`

```bash
# 查看默认编辑器
gh config get editor

# 查看 git 协议
gh config get git_protocol

# 列出所有配置
gh config list
```

---

**基本用法:修改配置**
`gh config set <键> <值>`

```bash
# 设置编辑器
gh config set editor "code --wait"

# 设置 SSH 协议
gh config set git_protocol ssh

# 设置分页器关闭
gh config set pager ""

# 设置为指定主机
gh config set editor vim --host github.com
```

---

## 补全与状态

**基本用法:Shell 自动补全**
`gh completion -s <shell>`

```bash
# 生成 bash 补全脚本
gh completion -s bash > ~/.gh-completion.bash

# PowerShell 补全
gh completion -s powershell | Out-String | Invoke-Expression

# zsh 补全
gh completion -s zsh > "${fpath[1]}/_gh"
```

---

**基本用法:查看账户状态**
`gh status`

```bash
# 查看当前账户在所有仓库的工作概览
gh status
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
