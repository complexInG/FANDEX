---
order: 68
title: 'git-reset'
module: git
category: 'Git Basics'
difficulty: advanced
description: 'git reset三种模式详解：soft、mixed、hard的区别与安全使用。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'git/Git-Flow与GitHub-Flow'
  - git/修改提交
  - git/撤销提交
  - git/Git原理与对象模型
prerequisites:
  - git/语法速查
---

## 1. reset 概述

### 1.1 什么是 reset

`git reset` 将当前分支的 HEAD 移动到指定位置，根据模式决定是否影响暂存区和工作区。

### 1.2 三种模式对比

| 模式               | HEAD | 暂存区 | 工作区 | 安全性 |
| :----------------- | :--- | :----- | :----- | :----- |
| **--soft**         | 移动 | 不变   | 不变   | 最安全 |
| **--mixed** (默认) | 移动 | 重置   | 不变   | 安全   |
| **--hard**         | 移动 | 重置   | 重置   | 危险   |

## 2. --soft 模式

### 2.1 效果

只移动 HEAD 指针，暂存区和工作区保持不变。

```
重置前: A---B---C---D (HEAD, main)
                    ↑ 暂存区和工作区

git reset --soft B

重置后: A---B---C---D (工作区和暂存区仍有 D 的内容)
        ↑ HEAD, main
```

### 2.2 使用场景

```bash
# 合并多个提交为一个
git reset --soft HEAD~3
git commit -m "feat: complete feature"

# 撤销提交但保留暂存
git reset --soft HEAD~1
# 修改后重新提交
```

## 3. --mixed 模式（默认）

### 3.1 效果

移动 HEAD 指针，重置暂存区，工作区保持不变。

```
重置前: A---B---C---D (HEAD, main)
                    ↑ 暂存区
                    ↑ 工作区

git reset --mixed B
# 或 git reset B

重置后: A---B (HEAD, main)
             ↑ 暂存区
        C和D的变更保留在工作区（未暂存状态）
```

### 3.2 使用场景

```bash
# 撤销提交，变更回到未暂存状态
git reset HEAD~1

# 取消暂存
git reset file.txt

# 重置到指定提交
git reset abc1234
```

## 4. --hard 模式

### 4.1 效果

移动 HEAD 指针，重置暂存区和工作区。**所有未提交的变更都会丢失！**

```
重置前: A---B---C---D (HEAD, main)
                    ↑ 暂存区
                    ↑ 工作区

git reset --hard B

重置后: A---B (HEAD, main)
             ↑ 暂存区
             ↑ 工作区
        C和D的变更全部丢失
```

### 4.2 使用场景

```bash
# 完全丢弃所有修改
git reset --hard HEAD

# 回到指定提交
git reset --hard abc1234

# 丢弃所有本地修改，同步远程
git fetch origin
git reset --hard origin/main
```

### 4.3 恢复 hard reset

```bash
# 通过 reflog 恢复
git reflog
# abc1234 HEAD@{0}: reset: moving to B
# def5678 HEAD@{1}: commit: D  ← reset 前的提交

git reset --hard def5678
```

## 5. 路径 reset

### 5.1 重置特定文件

```bash
# 将文件从暂存区移除（不改变工作区）
git reset file.txt

# 将文件恢复到指定提交的版本（放入暂存区）
git reset abc1234 -- file.txt
```

## 6. 安全实践

### 6.1 操作前检查

```bash
# 查看将要丢弃的内容
git stash                     # 先保存当前修改
git reset --hard HEAD~3       # 再执行 reset
git stash pop                 # 需要时恢复
```

### 6.2 使用 restore 替代

```bash
# Git 2.23+ 推荐使用 restore 替代 reset 的部分功能
git restore --staged file.txt  # 替代 git reset file.txt
git restore file.txt           # 替代 git checkout -- file.txt
```

## 延伸阅读
Git 基础操作与分支，见 003-git 模块文档。
GitHub 协作与 PR，见 004-github 模块。
CI/CD 自动化，见 031-devops 模块。
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
