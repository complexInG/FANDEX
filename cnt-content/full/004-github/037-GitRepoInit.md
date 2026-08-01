---
order: 370
title: GitHub 仓库初始化
module: github

category: '004-github'
difficulty: beginner
description: GitHub 仓库初始化 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 本地仓库初始化

**基本写法：初始化新仓库**
`git init`
```bash
# 在当前目录初始化 Git 仓库
git init
```

---

**基本写法：指定目录初始化**
`git init <目录名>`
```bash
# 在指定目录创建新仓库
git init myproject
```

---

**基本写法：初始化裸仓库**
`git init --bare`
```bash
# 创建不带工作区的裸仓库（用于服务器）
git init --bare
```

---

**基本写法：指定默认分支名初始化**
`git init -b <分支名>`
```bash
# 初始化时指定默认分支为 main
git init -b main
```

---

## 克隆远程仓库

**基本写法：克隆仓库**
`git clone <仓库URL>`
```bash
# 克隆远程仓库到本地
git clone https://github.com/user/repo.git
```

---

**基本写法：克隆到指定目录**
`git clone <仓库URL> <目录名>`
```bash
# 克隆仓库并指定本地目录名
git clone https://github.com/user/repo.git myapp
```

---

**基本写法：克隆指定分支**
`git clone -b <分支名> <仓库URL>`
```bash
# 仅克隆指定分支
git clone -b develop https://github.com/user/repo.git
```

---

**基本写法：浅克隆**
`git clone --depth 1 <仓库URL>`
```bash
# 仅克隆最近一次提交（适合大仓库）
git clone --depth 1 https://github.com/user/repo.git
```

---

**基本写法：克隆指定数量的提交**
`git clone --depth <数量> <仓库URL>`
```bash
# 克隆最近 5 次提交历史
git clone --depth 5 https://github.com/user/repo.git
```

---

**基本写法：SSH 方式克隆**
`git clone git@github.com:<用户名>/<仓库>.git`
```bash
# 通过 SSH 协议克隆（需配置 SSH 密钥）
git clone git@github.com:user/repo.git
```

---

## 仓库状态查看

**基本写法：查看仓库状态**
`git status`
```bash
# 查看工作区和暂存区状态
git status
```

---

**基本写法：简洁状态显示**
`git status -s`
```bash
# 以简短格式显示状态
git status -s
```

---

**基本写法：查看详细差异**
`git status -v`
```bash
# 显示状态并附带差异内容
git status -v
```

---

**基本写法：查看指定目录状态**
`git status <路径>`
```bash
# 仅查看指定目录的状态
git status src/
```

---

## 文件添加到暂存区

**基本写法：添加单个文件**
`git add <文件>`
```bash
# 将指定文件加入暂存区
git add index.js
```

---

**基本写法：添加所有改动**
`git add .`
```bash
# 添加当前目录所有改动到暂存区
git add .
```

---

**基本写法：添加所有修改和删除**
`git add -u`
```bash
# 添加已跟踪文件的修改和删除（不含新文件）
git add -u
```

---

**基本写法：添加所有变化**
`git add -A`
```bash
# 添加所有变化（含新增、修改、删除）
git add -A
```

---

**基本写法：交互式添加**
`git add -p`
```bash
# 交互式选择文件的部分改动加入暂存区
git add -p
```

---

**基本写法：添加指定目录**
`git add <目录>/`
```bash
# 将整个目录的改动加入暂存区
git add src/components/
```

---

## 文件移除与移动

**基本写法：移除文件**
`git rm <文件>`
```bash
# 从工作区和暂存区移除文件
git rm oldfile.txt
```

---

**基本写法：仅从暂存区移除**
`git rm --cached <文件>`
```bash
# 从暂存区移除但保留本地文件
git rm --cached .env
```

---

**基本写法：递归移除目录**
`git rm -r <目录>`
```bash
# 递归移除整个目录
git rm -r olddir/
```

---

**基本写法：重命名文件**
`git mv <旧名> <新名>`
```bash
# 重命名文件并记录到暂存区
git mv old.txt new.txt
```

---

**基本写法：移动文件到目录**
`git mv <文件> <目录>/`
```bash
# 将文件移动到指定目录
git mv file.txt src/
```

---

**基本写法：取消暂存文件**
`git restore --staged <文件>`
```bash
# 将文件从暂存区移回工作区
git restore --staged index.js
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
