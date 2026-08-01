---
order: 74
title: 'git-format-patch'
module: git
category: 'Git Basics'
difficulty: intermediate
description: 'git format-patch详解：生成补丁文件、邮件工作流与离线协作。'
author: fanquanpp
updated: '2026-08-01'
related:
  - git/子模块管理
  - git/稀疏检出
  - git/内容搜索
  - git/工作树管理
prerequisites:
  - git/语法速查
---

# git add/restore/checkout 工作区命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. format-patch 概述

### 1.1 什么是 format-patch

`git format-patch` 将提交转换为**标准的电子邮件补丁格式**，适合通过邮件或文件交换代码变更。

### 1.2 补丁格式

```
From abc1234 Mon Sep 17 00:00:00 2001
From: Zhang San <zhang@example.com>
Date: Sat, 14 Jun 2026 10:00:00 +0800
Subject: [PATCH] feat: add authentication

---
 src/auth.ts | 20 ++++++++++++++++++++
 1 file changed, 20 insertions(+)

diff --git a/src/auth.ts b/src/auth.ts
...
```

## 2. 基本用法

### 2.1 生成补丁

```bash
# 最近1个提交的补丁
git format-patch -1

# 最近3个提交的补丁
git format-patch -3

# 指定范围
git format-patch HEAD~3..HEAD
git format-patch abc1234..def5678

# 指定输出目录
git format-patch -3 -o /tmp/patches/
```

### 2.2 应用补丁

```bash
# 应用补丁（保留提交信息）
git am < 0001-feat-add-auth.patch

# 应用多个补丁
git am /tmp/patches/*.patch

# 检查补丁是否能应用
git apply --check 0001-feat-add-auth.patch

# 只应用变更不提交
git apply 0001-feat-add-auth.patch
```

### 2.3 处理冲突

```bash
git am /tmp/patches/*.patch
# Applying: feat: add auth
# error: patch failed: ...

# 解决冲突
vim conflicted-file.js
git add .
git am --continue

# 跳过当前补丁
git am --skip

# 放弃
git am --abort
```

## 3. 高级用法

### 3.1 生成单个文件

```bash
# 所有补丁合并为一个文件
git format-patch -3 --stdout > all-patches.patch

# 应用
git am < all-patches.patch
```

### 3.2 指定范围

```bash
# 某分支独有的提交
git format-patch main..feature

# 两个标签之间
git format-patch v1.0.0..v1.1.0
```

### 3.3 添加前缀

```bash
git format-patch -3 --subject-prefix="PATCH v2"
# [PATCH v2 1/3] feat: add auth
```

## 4. 离线协作场景

```bash
# 开发者 A：生成补丁
git format-patch -1 -o /tmp/patches/
# 通过 U盘/邮件 发送给开发者 B

# 开发者 B：应用补丁
git am < /tmp/patches/0001-feat-add-auth.patch
```

## 5. 与 git diff 的区别

| 特性         | format-patch | diff        |
| :----------- | :----------- | :---------- |
| **格式**     | 邮箱格式     | 纯差异      |
| **提交信息** | 保留         | 不保留      |
| **作者信息** | 保留         | 不保留      |
| **应用方式** | `git am`     | `git apply` |
| **适用场景** | 邮件协作     | 临时补丁    |
## 暂存文件

**基本用法:暂存改动**
`git add <路径>`

```bash
# 暂存单个文件
git add src/main.py

# 暂存整个目录
git add src/

# 暂存所有改动
git add .

# 暂存已跟踪文件(不含未跟踪)
git add -u
```

---

**基本用法:交互式暂存**
`git add -p`

```bash
# 逐块选择暂存(支持 y/n/s/e/q)
git add -p

# 交互模式主菜单
git add -i
```

---

**基本用法:按补丁暂存**
`git add --patch <文件>`

```bash
# 对指定文件逐块暂存
git add --patch src/utils.js
```

---

## 恢复工作区文件

**基本用法:丢弃工作区改动**
`git restore <文件>`

```bash
# 丢弃工作区改动(恢复到暂存区状态)
git restore src/main.py

# 恢复到指定提交的版本
git restore --source=HEAD~3 src/config.js

# 从暂存区取消暂存
git restore --staged src/main.py
```

---

**基本用法:用 checkout 恢复文件**
`git checkout -- <文件>`

```bash
# 旧写法:丢弃工作区改动
git checkout -- src/main.py

# 恢复指定提交的文件
git checkout a1b2c3d -- README.md
```

---

## 暂存区管理

**基本用法:取消暂存**
`git restore --staged <文件>`

```bash
# 把已暂存的文件移出暂存区
git restore --staged src/main.py

# 取消所有暂存
git restore --staged .
```

---

**基本用法:重置暂存区与工作区**
`git reset [选项] <提交>`

```bash
# 仅重置暂存区,保留工作区改动
git reset HEAD src/

# 软重置(保留改动到暂存区)
git reset --soft HEAD~1

# 混合重置(默认,保留改动到工作区)
git reset --mixed HEAD~1
```

---

## 参考文献



Git 官方文档：https://git-scm.com/doc
Pro Git 中文版：https://git-scm.com/book/zh/v2
Git 参考手册：https://git-scm.com/docs
Conventional Commits：https://www.conventionalcommits.org/zh-hans/

## 延伸阅读



Git 基础操作与分支，见 003-git 模块文档。
GitHub 协作与 PR，见 004-github 模块。
CI/CD 自动化，见 031-devops 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Git 课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 Git 对象模型与内部机制

git add 创建 blob 与 tree，git commit 创建 commit 对象，引用（HEAD/分支）指向 commit。
packfile 压缩对象；gc 清理悬空对象；fsck 校验完整性。
reflog 记录引用变动，是误操作恢复的最后防线。
理解对象模型后可解释 cherry-pick、rebase 与 reset 的底层行为。

### 13.2 合并策略与冲突解决

三路合并：base/ours/theirs 对比；rerere 记录重复冲突解决方案。
冲突标记：<<<<<<< 与 >>>>>>> 之间手工合并，保持语义正确后重新 add。
merge --no-ff 保留合并提交；squash 合并压缩 PR 历史。
策略选择：特性分支多 commit 用 squash/merge；持续集成用 rebase 保持线性。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Git 基础概念与核心特点 | 001-Git | 本文的前置基础 |
| Git 环境配置与初始化 | 002-GitEnvConfigInit | 本文的前置基础 |
| Git 基本操作 | 003-GitBasicOperation | 本文的并列主题 |
| Git 分支管理 | 004-GitBranchManagement | 本文的并列主题 |
| Git 远程仓库操作 | 005-GitRemoteRepoOperation | 本文的并列主题 |
| 分布式版本控制原理 | 006-DistributedVCSPrinciple | 本文的原理深化 |
| 对象模型 | 007-ObjectModel | 本文的并列主题 |
| SHA-1哈希完整性校验 | 008-SHA1IntegrityCheck | 本文的并列主题 |
| 三棵树 | 009-ThreeTrees | 本文的并列主题 |
| git-diff与暂存区操作 | 010-GitDiffStagingOperation | 本文的并列主题 |
| git-restore与文件操作 | 011-GitRestoreFileOperation | 本文的并列主题 |
| git-log详解 | 012-GitLogDetailed | 本文的并列主题 |
| git-reflog | 013-GitReflog | 本文的并列主题 |
| git-blame | 014-GitBlame | 本文的并列主题 |
| HEAD指针与分支本质 | 015-HEADPointerBranchEssence | 本文的并列主题 |
| Git 钩子与 Git LFS | 016-GitHookGitLFS | 本文的并列主题 |
| 合并冲突解决 | 017-MergeConflictResolution | 本文的并列主题 |
| git-mergetool | 018-GitMergetool | 本文的并列主题 |
| git-rebase | 019-GitRebase | 本文的并列主题 |
| git-cherry-pick | 020-GitCherryPick | 本文的并列主题 |
| git-stash | 021-GitStash | 本文的并列主题 |
| 远程跟踪分支 | 022-RemoteTrackingBranch | 本文的并列主题 |
| Git-Flow与GitHub-Flow | 023-GitFlowGitHubFlow | 本文的并列主题 |
| git-commit-amend | 024-GitCommitAmend | 本文的并列主题 |
| git-reset | 025-GitReset | 本文的并列主题 |
| git-revert | 026-GitRevert | 本文的并列主题 |
| Git 原理与对象模型 | 027-GitPrincipleObjectModel | 本文的原理深化 |
| 标签管理 | 028-TagManagement | 本文的并列主题 |
| git-bisect | 029-GitBisect | 本文的并列主题 |
| git-submodule | 030-GitSubmodule | 本文的并列主题 |
| sparse-checkout | 031-SparseCheckout | 本文的并列主题 |
| git-format-patch | 032-GitFormatPatch | 本文自身 |
| git-grep | 033-GitGrep | 本文的并列主题 |
| git-worktree | 034-GitWorktree | 本文的并列主题 |
| git-gc | 035-GitGc | 本文的并列主题 |
| Git-Flow与GitHub-Flow对比 | 036-GitFlowGitHubFlowComparison | 本文的并列主题 |
| 交互式rebase | 037-InteractiveRebase | 本文的并列主题 |
| git-revert与reset对比 | 038-GitRevertResetComparison | 本文的并列主题 |
| Code-Review流程与最佳实践 | 039-CodeReviewBestPractice | 本文的并列主题 |
