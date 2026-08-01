---
order: 56
title: 'git-log详解'
module: git
category: 'Git Basics'
difficulty: intermediate
description: 'git log多种格式与过滤选项：自定义输出、搜索过滤与可视化。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'git/git-diff与暂存区操作'
  - 'git/git-restore与文件操作'
  - git/引用日志
  - git/代码追溯
prerequisites:
  - git/语法速查
---
## 1. git log 基础

### 1.1 基本用法

```bash
git log                       # 查看完整日志
git log -5                    # 最近5条
git log --oneline             # 单行格式
git log --oneline -10         # 最近10条，单行格式
```

### 1.2 输出格式

```bash
# 默认格式
git log
# commit 9a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t
# Author: Zhang San <zhang@example.com>
# Date:   Sat Jun 14 10:00:00 2026 +0800
#
#     feat: add user authentication

# 单行格式
git log --oneline
# 9a1b2c3 feat: add user authentication

# 简短格式
git log --abbrev-commit
```

## 2. 自定义输出格式

### 2.1 预定义格式

```bash
# 单行
git log --oneline

# 紧凑
git log --oneline --graph --decorate

# 详细
git log --format=full

# 完整
git log --format=fuller

# 邮箱格式
git log --format=email

# 原始格式
git log --format=raw
```

### 2.2 自定义格式字符串

```bash
# 常用占位符
git log --format="%h - %an, %ar : %s"
# 9a1b2c3 - Zhang San, 2 hours ago : feat: add user auth

# 占位符参考
```

| 占位符 | 说明                 | 示例                |
| :----- | :------------------- | :------------------ |
| `%H`   | 完整哈希             | `9a1b2c3d4e5f...`   |
| `%h`   | 短哈希               | `9a1b2c3`           |
| `%T`   | 完整 tree 哈希       | —                   |
| `%t`   | 短 tree 哈希         | —                   |
| `%an`  | 作者名               | `Zhang San`         |
| `%ae`  | 作者邮箱             | `zhang@example.com` |
| `%ad`  | 作者日期             | —                   |
| `%ar`  | 作者相对日期         | `2 hours ago`       |
| `%cn`  | 提交者名             | —                   |
| `%s`   | 提交消息首行         | `feat: add auth`    |
| `%b`   | 提交消息正文         | —                   |
| `%d`   | 引用装饰             | `(HEAD -> main)`    |
| `%f`   | 消息的文件名安全版本 | —                   |

### 2.3 实用格式

```bash
# 美观的单行格式
git log --format="%C(yellow)%h%C(reset) %C(green)(%ar)%C(reset) %s %C(blue)<%an>%C(reset)"

# 图表格式
git log --oneline --graph --all --decorate

# 变更统计
git log --stat

# 每次提交的差异
git log -p

# 每次提交的差异（仅文件名）
git log --name-only

# 每次提交的差异（文件名+状态）
git log --name-status
```

## 3. 过滤选项

### 3.1 按数量

```bash
git log -5                    # 最近5条
git log -1                   # 最近1条
```

### 3.2 按日期

```bash
git log --since="2026-01-01"         # 2026年1月1日以来
git log --after="2026-01-01"         # 同上
git log --until="2026-06-14"         # 2026年6月14日之前
git log --before="2026-06-14"        # 同上
git log --since="2 weeks ago"        # 最近2周
git log --since="3 days ago"         # 最近3天
git log --after="yesterday"          # 昨天
```

### 3.3 按作者

```bash
git log --author="Zhang San"         # 按作者名
git log --author="zhang@example.com" # 按邮箱
git log --author="zhang"             # 模糊匹配
```

### 3.4 按提交消息

```bash
git log --grep="feat"                # 消息包含 "feat"
git log --grep="fix\|bug"            # 正则匹配
git log --grep="auth" -i             # 忽略大小写
git log --all-match --grep="feat" --grep="auth"  # 同时匹配
```

### 3.5 按文件

```bash
git log -- file.txt                  # 涉及指定文件的提交
git log -- src/                      # 涉及指定目录的提交
git log -p -- file.txt               # 显示文件差异
git log --follow file.txt            # 跟踪重命名
```

### 3.6 按引用范围

```bash
git log main..feature                # feature 有而 main 没有的提交
git log feature..main                # main 有而 feature 没有的提交
git log main...feature               # 两边独有的提交
git log --left-right main...feature  # 标注属于哪边
```

## 4. 图形化显示

### 4.1 内置图形

```bash
# ASCII 图形
git log --oneline --graph

# 带分支标签
git log --oneline --graph --decorate

# 所有分支
git log --oneline --graph --all

# 带日期和作者
git log --graph --format="%h %ad %an %s" --date=short
```

### 4.2 图形化工具

| 工具                  | 类型 | 特点                    |
| :-------------------- | :--- | :---------------------- |
| **gitk**              | 内置 | 基础图形界面            |
| **tig**               | 终端 | 终端中的交互式查看器    |
| **GitKraken**         | 桌面 | 专业 Git 客户端         |
| **SourceTree**        | 桌面 | 免费的 Atlassian 客户端 |
| **VS Code Git Graph** | 插件 | VS Code 内集成          |

## 5. 实用别名

```bash
[alias]
    lg = log --oneline --graph --decorate
    lga = log --oneline --graph --all --decorate
    ll = log --format="%C(yellow)%h%C(reset) %s %C(cyan)(%cr)%C(reset) %C(blue)<%an>%C(reset)"
    ls = log --stat
    lp = log -p
    lf = log --follow
    recent = log --since='2 weeks ago' --oneline
    who = shortlog -sn
```
## 格式化输出

**基本用法:简洁历史**
`git log --oneline`

```bash
# 每个提交一行显示
git log --oneline

# 限制显示条数
git log --oneline -10
```

---

**基本用法:图形化分支**
`git log --graph`

```bash
# 图形化展示分支合并历史
git log --oneline --graph --all

# 带装饰标签
git log --oneline --graph --decorate
```

---

**基本用法:自定义格式**
`git log --pretty=format:"<格式>"`

```bash
# 自定义字段:哈希 作者 时间 说明
git log --pretty=format:"%h - %an, %ar : %s"

# 完整格式
git log --pretty=format:"%C(yellow)%h%Creset %C(green)%ad%Creset %s" --date=short
```

---

## 过滤条件

**基本用法:按作者筛选**
`git log --author="<名称>"`

```bash
# 按作者过滤
git log --author="zhangsan"

# 按提交说明搜索
git log --grep="fix"
```

---

**基本用法:按时间筛选**
`git log --since=<时间>`

```bash
# 最近 7 天
git log --since="7 days ago"

# 指定日期之后
git log --since="2026-01-01" --until="2026-06-30"

# 按相对时间
git log --since="2 weeks ago" --until="yesterday"
```

---

**基本用法:按文件筛选**
`git log <路径>`

```bash
# 查看某文件的提交历史
git log -- src/auth/login.js

# 显示每次提交改动的统计
git log --stat -- src/

# 显示每次提交的具体差异
git log -p -- package.json
```

---

## 范围与对比

**基本用法:查看分支差异**
`git log <分支1>..<分支2>`

```bash
# 查看 feature 比 main 多的提交
git log main..feature

# 查看两个分支各自独有的提交
git log --left-right main...feature
```

---

**基本用法:查看指定行变更**
`git log -L <起始,结束>:<文件>`

```bash
# 追踪文件中 10-20 行的变更历史
git log -L 10,20:src/utils.js
```

---

## 统计输出

**基本用法:简明统计**
`git log --stat`

```bash
# 显示文件改动统计
git log --stat

# 仅显示数字统计
git log --numstat

# 短统计格式
git log --shortstat
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
| git-log详解 | 012-GitLogDetailed | 本文自身 |
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
