---
order: 55
title: 'git-restore与文件操作'
module: git
category: 'Git Basics'
difficulty: intermediate
description: 'git restore、rm、mv、clean等文件操作命令的详细用法与安全实践。'
author: fanquanpp
updated: '2026-08-01'
related:
  - git/三棵树
  - 'git/git-diff与暂存区操作'
  - 'git/git-log详解'
  - git/引用日志
prerequisites:
  - git/语法速查
---

## 1. git restore

### 1.1 概述

`git restore` 是 Git 2.23 引入的命令，用于**恢复工作区或暂存区的文件**，替代了 `git checkout` 的部分功能。

### 1.2 基本用法

```bash
# 恢复工作区文件（从暂存区）
git restore file.txt

# 恢复工作区文件（从指定提交）
git restore --source=HEAD~3 file.txt
git restore -s main file.txt

# 取消暂存（从仓库恢复到暂存区）
git restore --staged file.txt

# 同时恢复工作区和暂存区
git restore --staged --worktree file.txt
git restore -SW file.txt
```

### 1.3 restore vs checkout

| 操作           | `git restore`                | `git checkout`                |
| :------------- | :--------------------------- | :---------------------------- |
| 恢复工作区文件 | `git restore file`           | `git checkout -- file`        |
| 取消暂存       | `git restore --staged file`  | `git reset HEAD file`         |
| 切换分支       |                              | `git checkout branch`         |
| 恢复到指定提交 | `git restore -s commit file` | `git checkout commit -- file` |

## 2. git rm

### 2.1 基本用法

```bash
# 删除文件（工作区 + 暂存区）
git rm file.txt

# 只从暂存区删除（保留工作区文件）
git rm --cached file.txt

# 递归删除目录
git rm -r directory/

# 强制删除（忽略修改检查）
git rm -f file.txt

# 使用 glob 模式
git rm '*.log'
git rm 'src/**/*.test.js'
```

### 2.2 常见场景

```bash
# 从版本控制中移除但保留本地文件
git rm --cached .env          # 移除敏感文件
git rm --cached -r node_modules/  # 移除不应跟踪的目录

# 删除已删除的文件（已手动删除文件后）
git rm $(git ls-files --deleted)
```

## 3. git mv

### 3.1 基本用法

```bash
# 重命名文件
git mv old-name.txt new-name.txt

# 移动文件
git mv src/file.txt docs/file.txt

# 移动并重命名
git mv src/old.js lib/new.js
```

### 3.2 git mv 的本质

`git mv` 等价于以下三步操作：

```bash
mv old-name.txt new-name.txt    # 1. 文件系统重命名
git rm old-name.txt             # 2. Git 删除旧文件
git add new-name.txt            # 3. Git 添加新文件
```

Git 会自动检测重命名（通过内容相似度），不需要特殊操作。

### 3.3 重命名检测

```bash
# 查看重命名历史
git log --follow file.txt

# diff 时显示重命名
git diff -M                    # 检测重命名
git log --stat -M              # 日志中显示重命名
```

## 4. git clean

### 4.1 基本用法

```bash
# 查看将被删除的文件（干运行）
git clean -n

# 删除未跟踪的文件
git clean -f

# 删除未跟踪的文件和目录
git clean -fd

# 删除被忽略的文件
git clean -fX

# 删除未跟踪和被忽略的文件
git clean -fx

# 交互式删除
git clean -i
```

### 4.2 选项说明

| 选项 | 说明                         |
| :--- | :--------------------------- |
| `-n` | 干运行，只显示将被删除的文件 |
| `-f` | 强制删除                     |
| `-d` | 包含目录                     |
| `-X` | 只删除被忽略的文件           |
| `-x` | 删除未跟踪和被忽略的文件     |
| `-i` | 交互式确认                   |

### 4.3 常见场景

```bash
# 清理构建产物
git clean -fdx dist/

# 恢复到干净状态
git clean -fd && git reset --hard

# 只清理被忽略的文件
git clean -fX
```

## 5. 安全实践

### 5.1 防止数据丢失

```bash
# 在 clean 之前先查看
git clean -nfd                # 查看将被删除的内容

# 在 reset 之前先暂存
git stash                     # 保存当前修改
git reset --hard HEAD~3       # 重置
git stash pop                 # 恢复修改

# 使用 reflog 恢复误删的提交
git reflog                    # 查看操作历史
git reset --hard HEAD@{5}     # 恢复到指定操作
```

### 5.2 危险操作清单

| 命令                        | 风险等级 | 数据可恢复性                 |
| :-------------------------- | :------- | :--------------------------- |
| `git restore file`          | 低       | 暂存区或仓库有副本           |
| `git restore --staged file` | 低       | 仓库有副本                   |
| `git rm file`               | 中       | 提交历史中有                 |
| `git rm --cached file`      | 低       | 工作区保留                   |
| `git clean -f`              | **高**   | 未跟踪文件永久删除           |
| `git reset --hard`          | **高**   | reflog 可能恢复              |
| `git clean -fdx`            | **极高** | 所有未跟踪和忽略文件永久删除 |

### 5.3 保护措施

```bash
# 设置 clean 需要二次确认
git config --global clean.requireForce true

# 使用 .gitignore 防止重要文件被误删
echo "important-data/" >> .gitignore
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
| git-restore与文件操作 | 011-GitRestoreFileOperation | 本文自身 |
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
| git-gc | 035-GitGc | 本文的并列主题 |
| Git-Flow与GitHub-Flow对比 | 036-GitFlowGitHubFlowComparison | 本文的并列主题 |
| 交互式rebase | 037-InteractiveRebase | 本文的并列主题 |
| git-revert与reset对比 | 038-GitRevertResetComparison | 本文的并列主题 |
| Code-Review流程与最佳实践 | 039-CodeReviewBestPractice | 本文的并列主题 |
