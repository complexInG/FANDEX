---
order: 69
title: 'git-revert'
module: git
category: 'Git Basics'
difficulty: intermediate
description: 'git revert详解：安全撤销提交、生成反向提交与多人协作场景。'
author: fanquanpp
updated: '2026-08-01'
related:
  - git/修改提交
  - git/重置与回退
  - git/Git原理与对象模型
  - git/标签管理
prerequisites:
  - git/语法速查
---
## 1. revert 概述

### 1.1 什么是 revert

`git revert` 创建一个**新的反向提交**来撤销指定提交的变更，不修改历史。

```
原始: A---B---C---D (HEAD)
revert D: A---B---C---D---D' (HEAD)
                         ↑ D' 是 D 的反向操作
```

### 1.2 revert vs reset

| 特性       | revert              | reset                |
| :--------- | :------------------ | :------------------- |
| **历史**   | 新增提交，保留历史  | 删除提交，改写历史   |
| **安全性** | 安全，不影响他人    | 危险，影响已拉取的人 |
| **已推送** | 可安全使用          | 需要 force push      |
| **粒度**   | 按提交撤销          | 按范围重置           |
| **可逆性** | 容易（再次 revert） | 需要 reflog          |

## 2. 基本用法

### 2.1 撤销单个提交

```bash
git revert abc1234
# 打开编辑器编辑 revert 消息
```

### 2.2 不自动提交

```bash
git revert -n abc1234
# 变更放入暂存区，不自动提交
# 可以修改后再提交
```

### 2.3 撤销多个提交

```bash
# 撤销连续的多个提交
git revert abc1234..def5678

# 撤销多个不连续的提交
git revert abc1234 def5678 ghi9012
```

### 2.4 修改 revert 消息

```bash
git revert -m "revert: 回退认证功能" abc1234
```

## 3. 合并提交的 revert

### 3.1 指定父提交

合并提交有多个父提交，revert 时需要指定保留哪个：

```bash
# 查看合并提交的父提交
git cat-file -p abc1234
# parent def5678  ← 第一个父提交（主分支）
# parent ghi9012  ← 第二个父提交（合并分支）

# revert 保留第一个父提交（撤销合并分支的变更）
git revert -m 1 abc1234

# revert 保留第二个父提交（撤销主分支的变更）
git revert -m 2 abc1234
```

### 3.2 重新合并

revert 合并提交后，如果需要重新合并，需要先 revert 那个 revert 提交：

```bash
# 1. revert 合并提交
git revert -m 1 merge-commit

# 2. 后续需要重新合并
git revert revert-commit    # revert 那个 revert
git merge feature           # 重新合并
```

## 4. 冲突处理

### 4.1 revert 冲突

如果 revert 的提交之后有相关修改，可能产生冲突：

```bash
git revert abc1234
# CONFLICT: ...

# 解决冲突
vim conflicted-file.js
git add .
git revert --continue

# 或放弃
git revert --abort
```

## 5. 实际场景

### 5.1 回退已推送的功能

```bash
# 发现功能有严重 Bug，需要回退
git revert abc1234
git push origin main
```

### 5.2 回退发布

```bash
# 回退整个发布
git revert v1.0.0..v1.1.0
git push origin main
```

### 5.3 安全地撤销错误提交

```bash
# 错误提交已推送
git revert wrong-commit
# 在 revert 提交中说明原因
git commit -m "revert: 回退错误提交，原因：..."
```
## revert 基本用法

**基本写法：撤销单个提交**
`git revert <提交哈希>`
```bash
# 撤销 abc1234 提交
git revert abc1234;
```

**基本写法：不自动提交**
`git revert -n <提交哈希>`
```bash
# 撤销 abc1234 但不自动提交
git revert -n abc1234;
```

**基本写法：撤销连续多个提交**
`git revert <起始哈希>..<结束哈希>`
```bash
# 撤销 abc1234 到 def5678 之间的提交
git revert abc1234..def5678;
```

**单行写法：撤销多个不连续提交**
`git revert <哈希1> <哈希2> <哈希3>`
```bash
# 撤销多个不连续的提交
git revert abc1234 def5678 ghi9012;
```

**换行写法：撤销多个不连续提交**
`git revert <哈希1> <哈希2> <哈希3>`
```bash
# 换行书写多个提交
git revert abc1234 \
          def5678 \
          ghi9012;
```

**基本写法：指定 revert 消息**
`git revert -m "<消息>" <提交哈希>`
```bash
# 撤销 abc1234 并指定消息
git revert -m "revert: 回退认证功能" abc1234;
```

---

## 合并提交的 revert

**基本写法：查看合并提交的父提交**
`git cat-file -p <合并提交哈希>`
```bash
# 查看 abc1234 合并提交的父提交
git cat-file -p abc1234;
```

**基本写法：revert 保留第一个父提交**
`git revert -m 1 <合并提交哈希>`
```bash
# 撤销合并提交，保留主分支的变更
git revert -m 1 abc1234;
```

**基本写法：revert 保留第二个父提交**
`git revert -m 2 <合并提交哈希>`
```bash
# 撤销合并提交，保留合并分支的变更
git revert -m 2 abc1234;
```

---

## 重新合并已撤销的分支

**基本写法：revert 之前的 revert**
`git revert <revert提交哈希>`
```bash
# 恢复被撤销的合并
git revert revert-commit;
```

**基本写法：重新合并分支**
`git merge <分支名>`
```bash
# revert revert 后重新合并 feature 分支
git merge feature;
```

---

## revert 冲突处理

**基本写法：触发 revert 冲突**
`git revert <提交哈希>`
```bash
# 触发 revert 冲突
git revert abc1234;
```

**基本写法：添加解决后的文件**
`git add .`
```bash
# 添加解决冲突后的文件
git add .;
```

**基本写法：继续 revert 流程**
`git revert --continue`
```bash
# 继续 revert 流程
git revert --continue;
```

**基本写法：放弃 revert**
`git revert --abort`
```bash
# 放弃当前 revert 操作
git revert --abort;
```

---

## reset 撤销提交

**基本写法：软回退**
`git reset --soft HEAD~<n>`
```bash
# 撤销最近一次提交，修改保留在暂存区
git reset --soft HEAD~1;
```

**基本写法：混合回退**
`git reset --mixed HEAD~<n>`
```bash
# 撤销最近一次提交，修改保留在工作区
git reset --mixed HEAD~1;
```

**基本写法：硬回退**
`git reset --hard HEAD~<n>`
```bash
# 撤销最近一次提交并丢弃修改
git reset --hard HEAD~1;
```

---

## 撤销工作区修改

**基本写法：撤销单个文件修改**
`git checkout -- <file>`
```bash
# 撤销 src/index.js 的工作区修改
git checkout -- src/index.js;
```

**基本写法：使用 restore 撤销**
`git restore <file>`
```bash
# 撤销指定文件修改（Git 2.23+）
git restore src/index.js;
```

---

## 撤销暂存

**基本写法：取消暂存（保留修改）**
`git reset HEAD <file>`
```bash
# 将 src/index.js 移出暂存区
git reset HEAD src/index.js;
```

**基本写法：使用 restore 撤销暂存**
`git restore --staged <file>`
```bash
# 取消暂存但保留工作区修改（Git 2.23+）
git restore --staged src/index.js;
```

---

## 实际场景

**基本写法：回退已推送的功能**
`git revert <提交哈希>`
```bash
# 撤销已推送的 abc1234 提交
git revert abc1234;
```

**基本写法：推送撤销结果**
`git push <远程仓库名> <分支名>`
```bash
# 推送撤销结果到远程
git push origin main;
```

**基本写法：回退整个发布**
`git revert <起始标签>..<结束标签>`
```bash
# 回退 v1.0.0 到 v1.1.0 之间的所有提交
git revert v1.0.0..v1.1.0;
```

**基本写法：安全撤销错误提交**
`git revert <错误提交哈希>`
```bash
# 撤销错误提交
git revert wrong-commit;
```

**基本写法：补充撤销原因说明**
`git commit -m "<消息>"`
```bash
# 提交撤销原因说明
git commit -m "revert: 回退错误提交，原因：...";
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
