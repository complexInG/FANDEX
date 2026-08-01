---
order: 75
title: 'git-grep'
module: git
category: 'Git Basics'
difficulty: intermediate
description: 'git grep详解：在Git仓库中高效搜索代码，比grep更快的搜索方式。'
author: fanquanpp
updated: '2026-08-01'
related:
  - git/稀疏检出
  - git/补丁与邮件工作流
  - git/工作树管理
  - git/垃圾回收
prerequisites:
  - git/语法速查
---

## 1. git grep 概述

### 1.1 什么是 git grep

`git grep` 在 Git 仓库的**跟踪文件**中搜索，不需要索引文件，比普通 grep 更快。

### 1.2 优势

| 特性         | git grep            | 普通 grep  |
| :----------- | :------------------ | :--------- |
| **搜索范围** | 只搜跟踪文件        | 所有文件   |
| **速度**     | 快                  | 较慢       |
| **忽略文件** | 自动忽略 .gitignore | 需手动排除 |
| **指定版本** |                     |            |
| **并行搜索** |                     | 需配置     |

## 2. 基本用法

### 2.1 搜索当前工作区

```bash
# 搜索关键词
git grep "TODO"
git grep "function auth"

# 显示行号
git grep -n "TODO"

# 只显示文件名
git grep -l "TODO"

# 统计匹配数
git grep -c "TODO"

# 忽略大小写
git grep -i "todo"
```

### 2.2 搜索指定版本

```bash
# 在指定提交中搜索
git grep "TODO" HEAD~3
git grep "TODO" v1.0.0
git grep "TODO" main

# 在两个版本间搜索
git grep "TODO" main..feature
```

### 2.3 搜索指定文件

```bash
# 只搜特定文件
git grep "TODO" -- '*.js'
git grep "TODO" -- 'src/'

# 排除文件
git grep "TODO" -- ':!*.test.js'
```

## 3. 高级用法

### 3.1 正则搜索

```bash
# 基本正则
git grep -E "TODO|FIXME|HACK"

# Perl 正则
git grep -P "function\s+\w+\(" -- '*.js'

# 匹配整个单词
git grep -w "auth"
```

### 3.2 上下文显示

```bash
# 显示匹配行前后各2行
git grep -C 2 "TODO"

# 只显示后续行
git grep -A 5 "function auth"

# 只显示前面行
git grep -B 2 "return"
```

### 3.3 搜索多个模式

```bash
# 匹配任一模式
git grep -e "TODO" -e "FIXME"

# 必须同时匹配
git grep -e "import" --and -e "from"
```

## 4. 实际场景

### 4.1 查找所有 TODO

```bash
git grep -n "TODO\|FIXME\|HACK" -- '*.ts' '*.js'
```

### 4.2 查找废弃 API 使用

```bash
git grep -n "oldMethod\|deprecatedAPI" -- 'src/'
```

### 4.3 查找安全敏感代码

```bash
git grep -n "eval(\|innerHTML\|dangerouslySetInnerHTML" -- '*.js' '*.jsx' '*.ts' '*.tsx'
```

### 4.4 比较版本间的变更

```bash
# 查找新增的 TODO
git diff HEAD~5..HEAD | git grep "^+.*TODO"
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
| git-grep | 033-GitGrep | 本文自身 |
| git-worktree | 034-GitWorktree | 本文的并列主题 |
| git-gc | 035-GitGc | 本文的并列主题 |
| Git-Flow与GitHub-Flow对比 | 036-GitFlowGitHubFlowComparison | 本文的并列主题 |
| 交互式rebase | 037-InteractiveRebase | 本文的并列主题 |
| git-revert与reset对比 | 038-GitRevertResetComparison | 本文的并列主题 |
| Code-Review流程与最佳实践 | 039-CodeReviewBestPractice | 本文的并列主题 |
