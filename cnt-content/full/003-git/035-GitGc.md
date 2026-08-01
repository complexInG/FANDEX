---
order: 77
title: 'git-gc'
module: git
category: 'Git Basics'
difficulty: intermediate
description: 'git gc垃圾回收详解：仓库清理、对象打包与性能优化。'
author: fanquanpp
updated: '2026-08-01'
related:
  - git/内容搜索
  - git/工作树管理
  - 'git/Git-Flow与GitHub-Flow对比'
  - git/交互式rebase
prerequisites:
  - git/语法速查
---

## 1. gc 概述

### 1.1 什么是 git gc

`git gc`（Garbage Collection）清理仓库中的**不可达对象**，打包松散对象，优化仓库性能。

### 1.2 gc 做什么

1. **打包松散对象**：将 `.git/objects/??/` 中的松散文件打包为 packfile
2. **删除不可达对象**：清理不再被任何引用指向的对象
3. **压缩 packfile**：合并多个 packfile 为一个
4. **清理 reflog**：移除过期的 reflog 条目

## 2. 基本用法

### 2.1 运行 gc

```bash
# 标准垃圾回收
git gc

# 激进模式（更彻底的压缩）
git gc --aggressive

# 自动模式（只在需要时运行）
git gc --auto

# 只打包不删除
git gc --no-prune

# 立即删除不可达对象
git gc --prune=now
```

### 2.2 查看仓库状态

```bash
# 查看对象数量
git count-objects -v
# count: 42           ← 松散对象数
# size: 128           ← 松散对象大小（KB）
# in-pack: 1234       ← 打包对象数
# packs: 2            ← packfile 数量
# size-pack: 4096     ← packfile 大小（KB）
# prune-packable: 0   ← 可清理的打包对象
# garbage: 0          ← 损坏的对象

# 查看仓库大小
du -sh .git
```

## 3. gc 触发时机

### 3.1 自动触发

Git 在以下操作后可能自动运行 `git gc --auto`：

- `git commit`
- `git merge`
- `git rebase`
- `git fetch`
- `git pull`

### 3.2 自动触发条件

```bash
# 默认配置
git config --get gc.auto
# 6700  ← 松散对象超过 6700 个时触发

git config --get gc.autoPackLimit
# 50   ← packfile 超过 50 个时触发
```

### 3.3 禁用自动 gc

```bash
# 禁用自动 gc
git config --global gc.auto 0

# 临时禁用
git -c gc.auto=0 commit -m "message"
```

## 4. 手动清理

### 4.1 清理 reflog

```bash
# 清理所有过期的 reflog
git reflog expire --expire=now --all

# 清理后运行 gc
git gc --prune=now
```

### 4.2 清理不可达分支

```bash
# 查看不可达的提交
git fsck --unreachable

# 清理
git gc --prune=now
```

### 4.3 重新打包

```bash
# 重新打包所有对象
git repack -a -d

# 只打包松散对象
git repack

# 增量打包
git repack -d -l
```

## 5. 性能优化

### 5.1 gc 策略配置

```bash
# 日常 gc（快速）
git gc

# 深度优化（慢但更彻底）
git gc --aggressive

# 差异：aggressive 会重新计算 delta 压缩
# 适合：大型仓库首次 gc 或重大变更后
```

### 5.2 推荐配置

```bash
# 定期运行 gc
git config --global gc.auto 256
git config --global gc.autopacklimit 20

# 优化 pack 窗口
git config --global pack.windowMemory 256m

# 优化 delta 压缩
git config --global pack.depth 50
git config --global pack.window 10
```

## 6. 常见问题

### 6.1 仓库体积过大

```bash
# 1. 清理 reflog
git reflog expire --expire=now --all

# 2. 运行 gc
git gc --prune=now --aggressive

# 3. 检查大文件
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '/^blob/ {print $3, $4}' | \
  sort -rn | head -20
```

### 6.2 清理历史中的大文件

```bash
# 使用 git filter-repo（推荐）
pip install git-filter-repo
git filter-repo --path large-file.bin --invert-paths

# 清理后
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

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
| git-format-patch | 032-GitFormatPatch | 本文的并列主题 |
| git-grep | 033-GitGrep | 本文的并列主题 |
| git-worktree | 034-GitWorktree | 本文的并列主题 |
| git-gc | 035-GitGc | 本文自身 |
| Git-Flow与GitHub-Flow对比 | 036-GitFlowGitHubFlowComparison | 本文的并列主题 |
| 交互式rebase | 037-InteractiveRebase | 本文的并列主题 |
| git-revert与reset对比 | 038-GitRevertResetComparison | 本文的并列主题 |
| Code-Review流程与最佳实践 | 039-CodeReviewBestPractice | 本文的并列主题 |
