---
order: 64
title: 'git-stash'
module: git
category: 'Git Basics'
difficulty: intermediate
description: 'git stash详解：暂存工作进度、多栈管理与典型应用场景。'
author: fanquanpp
updated: '2026-08-01'
related:
  - git/变基操作
  - git/摘取提交
  - git/远程跟踪分支
  - 'git/Git-Flow与GitHub-Flow'
prerequisites:
  - git/语法速查
---

# git stash 暂存命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. stash 概述

### 1.1 什么是 stash

`git stash` 将工作区和暂存区的修改**临时保存**到栈中，恢复工作区到干净状态。

```mermaid
flowchart TD
    W[工作区 有修改] -->|git stash| C[工作区 干净]
    W --> S[stash 栈<br/>stash@{2} / stash@{1} / stash@{0} 最新]
```

## 2. 基本用法

### 2.1 创建 stash

```bash
# 保存所有已跟踪文件的修改
git stash

# 保存时添加消息
git stash push -m "WIP: feature auth"

# 包含未跟踪的文件
git stash -u
git stash --include-untracked

# 包含被忽略的文件
git stash -a
git stash --all

# 只暂存部分文件
git stash push -p          # 交互式选择
git stash push file.txt    # 指定文件
```

### 2.2 查看 stash

```bash
# 查看所有 stash
git stash list
# stash@{0}: On main: WIP: feature auth
# stash@{1}: WIP on main: abc1234 fix: bug

# 查看 stash 内容
git stash show             # 最新 stash 的摘要
git stash show -p          # 最新 stash 的差异
git stash show stash@{1}   # 指定 stash 的摘要
git stash show -p stash@{1}
```

### 2.3 恢复 stash

```bash
# 恢复并删除 stash
git stash pop              # 恢复最新的 stash
git stash pop stash@{1}    # 恢复指定 stash

# 恢复但保留 stash
git stash apply            # 恢复最新的 stash
git stash apply stash@{1}  # 恢复指定 stash

# 恢复暂存区状态
git stash apply --index    # 同时恢复暂存区
```

### 2.4 删除 stash

```bash
# 删除指定 stash
git stash drop stash@{1}

# 删除所有 stash
git stash clear
```

## 3. 高级用法

### 3.1 从 stash 创建分支

```bash
# 基于 stash 创建新分支
git stash branch feature-from-stash stash@{0}
# 1. 创建新分支
# 2. 恢复 stash 内容
# 3. 删除 stash
```

### 3.2 部分暂存

```bash
# 交互式选择暂存内容
git stash push -p
# Stash this hunk [y,n,q,a,d,/,s,e,?]?
```

### 3.3 查看 stash 中的文件

```bash
# 查看 stash 中某个文件的内容
git show stash@{0}:src/index.js

# 比较 stash 和当前工作区
git diff stash@{0}
```

## 4. 典型场景

### 4.1 紧急修复

```bash
# 正在开发功能，需要紧急修复 Bug
git stash -m "WIP: feature"
git checkout main
git checkout -b hotfix/bug-123
# ... 修复 Bug ...
git commit -m "fix: resolve bug 123"
git checkout feature
git stash pop
```

### 4.2 切换分支

```bash
# 需要切换分支但不想提交半成品
git stash
git checkout other-branch
# ... 完成其他工作 ...
git checkout feature
git stash pop
```

### 4.3 多任务并行

```bash
# 多个 WIP 进度
git stash push -m "feature A"
# ... 工作 ...
git stash push -m "feature B"

# 查看所有进度
git stash list

# 恢复特定进度
git stash apply stash@{1}
```

## 5. 注意事项

- `git stash pop` 如果有冲突，stash 不会被删除
- stash 是**本地**的，不会推送到远程
- 默认不保存未跟踪文件，需加 `-u`
- 长期不用的 stash 应及时清理
## 基础暂存

**基本用法:暂存当前改动**
`git stash [push]`

```bash
# 暂存已跟踪文件的改动(含暂存区与工作区)
git stash

# 添加描述信息
git stash push -m "WIP: 登录功能未完成"

# 仅暂存已暂存内容
git stash --keep-index
```

---

**基本用法:暂存含未跟踪文件**
`git stash -u`

```bash
# 包含未跟踪文件(untracked)
git stash -u

# 包含忽略文件
git stash -a
```

---

## 查看与恢复

**基本用法:查看暂存列表**
`git stash list`

```bash
# 列出所有 stash
git stash list

# 查看某个 stash 的内容差异
git stash show stash@{0}

# 查看完整差异
git stash show -p stash@{1}
```

---

**基本用法:恢复暂存**
`git stash pop [stash@{N}]`

```bash
# 恢复最近 stash 并删除
git stash pop

# 恢复指定 stash 并删除
git stash pop stash@{2}

# 恢复但保留 stash
git stash apply stash@{0}
```

---

## 管理暂存

**基本用法:删除暂存**
`git stash drop <stash@{N}>`

```bash
# 删除指定 stash
git stash drop stash@{1}

# 清空所有 stash
git stash clear
```

---

**基本用法:从 stash 创建分支**
`git stash branch <分支名> [stash@{N}]`

```bash
# 基于 stash 创建并切换分支
git stash branch hotfix-branch stash@{0}
```

---

## 局部暂存

**基本用法:交互式暂存**
`git stash -p`

```bash
# 逐块选择暂存内容
git stash -p
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
| git-stash | 021-GitStash | 本文自身 |
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
| git-format-patch | 032-GitFormatPatch | 本文的并列主题 |
| git-grep | 033-GitGrep | 本文的并列主题 |
| git-worktree | 034-GitWorktree | 本文的并列主题 |
| git-gc | 035-GitGc | 本文的并列主题 |
| Git-Flow与GitHub-Flow对比 | 036-GitFlowGitHubFlowComparison | 本文的并列主题 |
| 交互式rebase | 037-InteractiveRebase | 本文的并列主题 |
| git-revert与reset对比 | 038-GitRevertResetComparison | 本文的并列主题 |
| Code-Review流程与最佳实践 | 039-CodeReviewBestPractice | 本文的并列主题 |
