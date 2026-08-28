---
order: 10
title: git 模块文档合集
module: 'git'
category: 工具链
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：003-git/001-GitRebase.md ============ -->

# 变基操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本 rebase

**基本写法：标准变基**
`git rebase <基础分支>`
```bash
# 将 feature 分支变基到 main
git checkout feature;
git rebase main;
```

**基本写法：等价写法**
`git rebase <基础分支> <目标分支>`
```bash
# 等价于先 checkout feature 再 rebase main
git rebase main feature;
```

---

## 处理 rebase 冲突

**基本写法：触发 rebase**
`git rebase <基础分支>`
```bash
# rebase 过程中遇到冲突
git rebase main;
```

**基本写法：添加解决后的文件**
`git add .`
```bash
# 解决冲突后添加文件
git add .;
```

**基本写法：继续 rebase**
`git rebase --continue`
```bash
# 继续 rebase 流程
git rebase --continue;
```

**基本写法：跳过当前提交**
`git rebase --skip`
```bash
# 跳过当前冲突的提交
git rebase --skip;
```

**基本写法：放弃 rebase**
`git rebase --abort`
```bash
# 放弃整个 rebase 操作
git rebase --abort;
```

---

## 交互式 rebase

**基本写法：修改最近 N 个提交**
`git rebase -i HEAD~<n>`
```bash
# 修改最近 3 个提交
git rebase -i HEAD~3;
```

**基本写法：修改分叉点以来的提交**
`git rebase -i <基础分支>`
```bash
# 修改从 main 分叉以来的所有提交
git rebase -i main;
```

---

## 交互式 rebase 指令

**基本写法：指令格式**
`<指令> <提交哈希> <提交消息>`
```text
# 指令说明
# p, pick   使用提交
# r, reword 使用提交，修改消息
# e, edit   使用提交，暂停修改
# s, squash 合并到前一个提交
# f, fixup  合并到前一个提交，丢弃消息
# d, drop   丢弃提交
pick abc1234 feat: add authentication
pick def5678 fix: resolve login bug
```

**基本写法：修改提交消息**
`reword <提交哈希> <提交消息>`
```text
# 修改 abc1234 的提交消息
reword abc1234 feat: add authentication
pick def5678 fix: resolve login bug
```

**基本写法：合并提交**
`squash <提交哈希> <提交消息>`
```text
# 将 def5678 合并到 abc1234
pick abc1234 feat: add authentication
squash def5678 fix: resolve login bug
```

**基本写法：修改提交内容**
`edit <提交哈希> <提交消息>`
```text
# 标记 abc1234 为 edit 后保存退出
edit abc1234 feat: add authentication
pick def5678 fix: resolve login bug
```

**基本写法：修改暂停后的提交**
`git commit --amend`
```bash
# 修改提交内容
git commit --amend;
```

**基本写法：重新排序提交**
`pick <提交哈希> <提交消息>`
```text
# 调整提交顺序，def5678 在前
pick def5678 fix: resolve login bug
pick abc1234 feat: add authentication
```

**基本写法：删除提交**
`drop <提交哈希> <提交消息>`
```text
# 删除 def5678 提交
pick abc1234 feat: add authentication
drop def5678 fix: resolve login bug
```

---

## 高级 rebase

**基本写法：变基到指定提交**
`git rebase --onto <基础分支> <起始提交> <目标分支>`
```bash
# 将 abc1234..feature 范围的提交变基到 main 上
git rebase --onto main abc1234 feature;
```

**基本写法：自动 squash**
`git rebase -i --autosquash`
```bash
# 配合 git commit --fixup=abc1234 使用
git rebase -i --autosquash;
```

**基本写法：保留合并提交**
`git rebase -i --rebase-merges <基础分支>`
```bash
# 保留分支合并结构的交互式变基
git rebase -i --rebase-merges main;
```

---

## force push 安全方式

**基本写法：安全强制推送**
`git push --force-with-lease`
```bash
# 检查远程是否有新提交，有则拒绝推送
git push --force-with-lease;
```

---

## 实际场景

**基本写法：同步主分支更新**
`git rebase <远程仓库名>/<分支名>`
```bash
# 功能分支同步主分支更新
git checkout feature;
git fetch origin;
git rebase origin/main;
```

**基本写法：清理提交历史**
`git rebase -i HEAD~<n>`
```bash
# 合并最近 5 个提交
git rebase -i HEAD~5;
```

**基本写法：启动交互式 rebase 修复 Bug**
`git rebase -i HEAD~<n>`
```bash
# 启动交互式 rebase
git rebase -i HEAD~3;
```

**基本写法：修改提交**
`git commit --amend`
```bash
# 修复 Bug 后修改提交
git commit --amend;
```

**基本写法：继续 rebase**
`git rebase --continue`
```bash
# 继续 rebase 流程
git rebase --continue;
```



<!-- ============ 文档分隔线：003-git/002-TagManagement.md ============ -->

# 标签管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建轻量标签

**基本写法：在当前提交创建标签**
`git tag <标签名>`
```bash
# 在当前提交创建 v1.0.0 标签
git tag v1.0.0;
```

**基本写法：在指定提交创建标签**
`git tag <标签名> <提交哈希>`
```bash
# 在 abc1234 提交创建 v0.9.0 标签
git tag v0.9.0 abc1234;
```

---

## 创建附注标签

**基本写法：创建附注标签**
`git tag -a <标签名> -m "<标签消息>"`
```bash
# 创建附注标签 v1.0.0
git tag -a v1.0.0 -m "Release version 1.0.0";
```

**基本写法：在指定提交创建附注标签**
`git tag -a <标签名> <提交哈希> -m "<标签消息>"`
```bash
# 在 abc1234 提交创建附注标签 v0.9.0
git tag -a v0.9.0 abc1234 -m "Release version 0.9.0";
```

---

## 语义化版本

**基本写法：语义化版本格式**
`v<主版本号>.<次版本号>.<修订号>`
```text
# v1.2.3 含义
# 1 主版本号：不兼容的变更
# 2 次版本号：向后兼容的新功能
# 3 修订号：Bug 修复
v1.2.3
```

---

## 列出标签

**基本写法：列出所有标签**
`git tag`
```bash
# 列出所有标签
git tag;
```

**基本写法：按模式过滤标签**
`git tag -l "<模式>"`
```bash
# 列出 v1. 开头的标签
git tag -l "v1.*";
```

**基本写法：查看标签详情**
`git show <标签名>`
```bash
# 查看 v1.0.0 标签的详情
git show v1.0.0;
```

**基本写法：查看标签对象内容**
`git cat-file -p <标签名>`
```bash
# 查看 v1.0.0 标签对象内容
git cat-file -p v1.0.0;
```

---

## 查看标签指向的提交

**基本写法：获取标签指向的提交哈希**
`git rev-parse <标签名>`
```bash
# 获取 v1.0.0 指向的提交哈希
git rev-parse v1.0.0;
```

**基本写法：查看标签指向的提交日志**
`git log <标签名> -1`
```bash
# 查看 v1.0.0 标签指向的提交
git log v1.0.0 -1;
```

---

## 推送标签

**基本写法：推送单个标签**
`git push <远程仓库名> <标签名>`
```bash
# 推送 v1.0.0 标签到 origin
git push origin v1.0.0;
```

**基本写法：推送所有标签**
`git push <远程仓库名> --tags`
```bash
# 推送所有标签到 origin
git push origin --tags;
```

**基本写法：只推送附注标签**
`git push <远程仓库名> --follow-tags`
```bash
# 推送所有附注标签到 origin
git push origin --follow-tags;
```

---

## 删除标签

**基本写法：删除本地标签**
`git tag -d <标签名>`
```bash
# 删除本地 v1.0.0 标签
git tag -d v1.0.0;
```

**基本写法：删除远程标签**
`git push <远程仓库名> --delete <标签名>`
```bash
# 删除 origin 上的 v1.0.0 标签
git push origin --delete v1.0.0;
```

**基本写法：删除远程标签（refs 写法）**
`git push <远程仓库名> :refs/tags/<标签名>`
```bash
# 使用 refs 写法删除远程标签
git push origin :refs/tags/v1.0.0;
```

---

## 签名标签

**基本写法：创建 GPG 签名标签**
`git tag -s <标签名> -m "<标签消息>"`
```bash
# 创建 GPG 签名的 v1.0.0 标签
git tag -s v1.0.0 -m "Release v1.0.0";
```

**基本写法：验证签名标签**
`git tag -v <标签名>`
```bash
# 验证 v1.0.0 标签的签名
git tag -v v1.0.0;
```

---

## 配置 SSH 签名

**基本写法：配置 SSH 签名格式**
`git config --global gpg.format ssh`
```bash
# 配置使用 SSH 签名
git config --global gpg.format ssh;
```

**基本写法：配置签名密钥**
`git config --global user.signingkey <密钥路径>`
```bash
# 指定 ed25519 密钥作为签名密钥
git config --global user.signingkey ~/.ssh/id_ed25519.pub;
```

---

## 检出标签

**基本写法：检出到标签**
`git checkout <标签名>`
```bash
# 切换到 v1.0.0 标签对应的提交
git checkout v1.0.0;
```



<!-- ============ 文档分隔线：003-git/003-GitRevert.md ============ -->

# 撤销提交

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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



<!-- ============ 文档分隔线：003-git/004-GitWorktree.md ============ -->

# 工作树管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建工作树

**基本写法：基于现有分支创建**
`git worktree add <路径> <分支名>`
```bash
# 将 feature 分支检出到 ../project-feature
git worktree add ../project-feature feature;
```

**基本写法：基于新分支创建**
`git worktree add -b <新分支名> <路径> <基础分支>`
```bash
# 基于 main 创建 new-feature 分支并检出
git worktree add -b new-feature ../project-new-feature main;
```

**基本写法：创建分离 HEAD 工作树**
`git worktree add --detach <路径> <提交或标签>`
```bash
# 检出 v1.0.0 标签到 ../project-v1
git worktree add --detach ../project-v1 v1.0.0;
```

---

## 管理工作树

**基本写法：列出所有工作树**
`git worktree list`
```bash
# 列出所有工作树
git worktree list;
```

**基本写法：删除工作树**
`git worktree remove <路径>`
```bash
# 删除 ../project-feature 工作树
git worktree remove ../project-feature;
```

**基本写法：强制删除工作树**
`git worktree remove --force <路径>`
```bash
# 强制删除有修改的工作树
git worktree remove --force ../project-feature;
```

---

## 清理工作树

**基本写法：清理已删除目录的引用**
`git worktree prune`
```bash
# 清理已删除目录的工作树引用
git worktree prune;
```

**基本写法：预览清理**
`git worktree prune --dry-run`
```bash
# 查看将被清理的工作树
git worktree prune --dry-run;
```

---

## 紧急修复场景

**基本写法：创建紧急修复工作树**
`git worktree add -b <修复分支> <路径> <基础分支>`
```bash
# 创建紧急修复工作树
git worktree add ../hotfix -b hotfix/bug-123 main;
```

**基本写法：进入工作树**
`cd <路径>`
```bash
# 进入工作树
cd ../hotfix;
```

**基本写法：提交修复**
`git commit -m "<消息>"`
```bash
# 修复 Bug 并提交
git commit -m "fix: resolve bug 123";
```

**基本写法：推送修复**
`git push <远程仓库名> <分支名>`
```bash
# 推送修复
git push origin hotfix/bug-123;
```

**基本写法：返回主工作树**
`cd <路径>`
```bash
# 返回主工作树
cd ../project;
```

**基本写法：删除修复工作树**
`git worktree remove <路径>`
```bash
# 删除修复工作树
git worktree remove ../hotfix;
```

---

## 代码审查场景

**基本写法：检出 PR 到工作树**
`git worktree add -b <分支> <路径> <远程仓库名>/<远程分支名>`
```bash
# 检出同事的 PR 到独立工作树
git worktree add ../review-pr -b review origin/colleague/feature;
```

**基本写法：进入审查工作树**
`cd <路径>`
```bash
# 进入工作树
cd ../review-pr;
```

---

## 对比版本场景

**基本写法：创建对比工作树**
`git worktree add <路径> <标签或提交>`
```bash
# 检出 v1.0.0 到独立目录
git worktree add ../v1-compare v1.0.0;
```

**基本写法：对比两个版本**
`diff -r <目录1> <目录2>`
```bash
# 对比两个版本的代码
diff -r src/ ../v1-compare/src/;
```



<!-- ============ 文档分隔线：003-git/005-MergeConflictResolution.md ============ -->

# 合并冲突解决

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 冲突标记格式

**基本写法：冲突标记结构**
`<<<<<<< HEAD ... ======= ... >>>>>>> <分支名>`
```text
# 冲突标记格式
<<<<<<< HEAD
当前分支的内容
=======
合并分支的内容
>>>>>>> feature
```

---

## 冲突解决标准流程

**基本写法：尝试合并**
`git merge <分支名>`
```bash
# 合并 feature 分支到当前分支
git merge feature;
```

**基本写法：查看冲突文件**
`git status`
```bash
# 查看冲突状态
git status;
```

**基本写法：标记冲突已解决**
`git add <file>`
```bash
# 将解决冲突后的文件加入暂存区
git add src/index.js;
```

**基本写法：完成合并提交**
`git commit`
```bash
# 提交合并结果
git commit;
```

---

## 查看冲突详情

**基本写法：列出冲突文件**
`git diff --name-only --diff-filter=U`
```bash
# 列出所有冲突文件
git diff --name-only --diff-filter=U;
```

**基本写法：查看冲突内容**
`git diff`
```bash
# 查看冲突内容
git diff;
```

**基本写法：使用合并工具**
`git mergetool`
```bash
# 启动配置的合并工具
git mergetool;
```

---

## 选择一方版本

**基本写法：采用当前分支版本**
`git checkout --ours <file>`
```bash
# 采用当前分支版本的 src/config.js
git checkout --ours src/config.js;
```

**基本写法：采用合并分支版本**
`git checkout --theirs <file>`
```bash
# 采用合并分支版本的 src/styles.css
git checkout --theirs src/styles.css;
```

---

## 合并策略选项

**基本写法：合并双方修改**
`git merge -X union <分支名>`
```bash
# 使用 union 策略合并双方修改
git merge -X union feature;
```

**基本写法：冲突时采用当前分支**
`git merge -X ours <分支名>`
```bash
# 冲突时总是采用当前分支
git merge -X ours feature;
```

**基本写法：冲突时采用合并分支**
`git merge -X theirs <分支名>`
```bash
# 冲突时总是采用合并分支
git merge -X theirs feature;
```

---

## 放弃合并

**基本写法：放弃当前合并**
`git merge --abort`
```bash
# 放弃当前合并操作
git merge --abort;
```

**基本写法：硬重置放弃合并**
`git reset --hard HEAD`
```bash
# 强制回到合并前的 HEAD 状态
git reset --hard HEAD;
```

---

## 多文件冲突处理

**基本写法：批量采用 ours**
`git checkout --ours .`
```bash
# 批量采用当前分支版本
git checkout --ours .;
```

**基本写法：批量采用 theirs**
`git checkout --theirs .`
```bash
# 批量采用合并分支版本
git checkout --theirs .;
```

**基本写法：逐文件处理冲突**
`for file in $(git diff --name-only --diff-filter=U)`
```bash
# 遍历所有冲突文件逐个处理
for file in $(git diff --name-only --diff-filter=U); do
    echo "Conflict in: $file"
done
```

---

## 重命名冲突

**基本写法：查看重命名情况**
`git diff --name-status --diff-filter=R`
```bash
# 查看重命名的文件
git diff --name-status --diff-filter=R;
```

---

## 子模块冲突

**基本写法：查看子模块指向的提交**
`git ls-tree HEAD <子模块路径>`
```bash
# 查看子模块指向的提交
git ls-tree HEAD path/to/submodule;
```

**基本写法：进入子模块目录**
`cd <子模块路径>`
```bash
# 进入子模块目录
cd path/to/submodule;
```

**基本写法：切换到正确的提交**
`git checkout <提交哈希>`
```bash
# 切换到正确的提交
git checkout correct-commit;
```

**基本写法：返回主仓库**
`cd ..`
```bash
# 返回主仓库
cd ..;
```

**基本写法：添加子模块**
`git add <子模块路径>`
```bash
# 添加子模块
git add path/to/submodule;
```

---

## 预合并检查

**基本写法：测试合并（不提交）**
`git merge --no-commit --no-ff <分支名>`
```bash
# 测试合并但不提交
git merge --no-commit --no-ff feature;
```

**基本写法：检查冲突标记**
`git diff --check`
```bash
# 检查空白错误和冲突标记
git diff --check;
```

**基本写法：放弃测试合并**
`git merge --abort`
```bash
# 放弃测试合并
git merge --abort;
```



<!-- ============ 文档分隔线：003-git/006-GitSubmodule.md ============ -->

# 子模块管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 添加子模块

**基本写法：添加子模块**
`git submodule add <仓库地址> <路径>`
```bash
# 添加 shared-lib 作为子模块到 lib/shared
git submodule add https://github.com/user/shared-lib.git lib/shared;
```

**基本写法：提交子模块添加**
`git commit -m "<消息>"`
```bash
# 提交子模块添加
git commit -m "feat: add shared-lib submodule";
```

---

## 克隆含子模块的仓库

**基本写法：递归克隆**
`git clone --recurse-submodules <仓库地址>`
```bash
# 克隆并递归初始化所有子模块
git clone --recurse-submodules https://github.com/user/main-repo.git;
```

**基本写法：克隆主仓库**
`git clone <仓库地址>`
```bash
# 克隆主仓库
git clone https://github.com/user/main-repo.git;
```

**基本写法：初始化子模块**
`git submodule init`
```bash
# 初始化子模块
git submodule init;
```

**基本写法：更新子模块**
`git submodule update`
```bash
# 更新子模块
git submodule update;
```

**基本写法：一步到位初始化**
`git submodule update --init --recursive`
```bash
# 初始化并递归更新所有子模块
git submodule update --init --recursive;
```

---

## 更新子模块

**基本写法：更新到最新提交**
`git submodule update --remote`
```bash
# 更新所有子模块到远程最新提交
git submodule update --remote;
```

**基本写法：更新指定子模块**
`git submodule update --remote <路径>`
```bash
# 仅更新 lib/shared 子模块
git submodule update --remote lib/shared;
```

**基本写法：更新并合并**
`git submodule update --remote --merge`
```bash
# 更新所有子模块并合并
git submodule update --remote --merge;
```

---

## 删除子模块

**基本写法：取消注册子模块**
`git submodule deinit -f <路径>`
```bash
# 取消注册 lib/shared 子模块
git submodule deinit -f lib/shared;
```

**基本写法：删除子模块 Git 数据**
`rm -rf .git/modules/<路径>`
```bash
# 删除子模块的 Git 数据
rm -rf .git/modules/lib/shared;
```

**基本写法：从 Git 中移除子模块**
`git rm -f <路径>`
```bash
# 从 Git 中移除子模块
git rm -f lib/shared;
```

**基本写法：提交删除**
`git commit -m "<消息>"`
```bash
# 提交子模块删除
git commit -m "chore: remove shared-lib submodule";
```

---

## .gitmodules 配置文件

**基本写法：配置文件格式**
`[submodule "<名称>"]`
```ini
# .gitmodules 文件格式
[submodule "lib/shared"]
    path = lib/shared
    url = https://github.com/user/shared-lib.git
    branch = main
```

---

## 子模块分离 HEAD 处理

**基本写法：进入子模块目录**
`cd <子模块路径>`
```bash
# 进入子模块目录
cd lib/shared;
```

**基本写法：切换到分支**
`git checkout <分支名>`
```bash
# 切换到 main 分支
git checkout main;
```

**基本写法：拉取更新**
`git pull`
```bash
# 拉取更新
git pull;
```

**基本写法：返回主仓库**
`cd ../..`
```bash
# 返回主仓库
cd ../..;
```

**基本写法：添加子模块更新**
`git add <子模块路径>`
```bash
# 添加子模块更新
git add lib/shared;
```

**基本写法：提交更新**
`git commit -m "<消息>"`
```bash
# 提交子模块更新
git commit -m "chore: update submodule";
```

---

## 子模块脏状态处理

**基本写法：忽略子模块修改**
`git config submodule.<路径>.ignore dirty`
```bash
# 忽略 lib/shared 子模块的修改
git config submodule.lib/shared.ignore dirty;
```

**基本写法：强制更新子模块**
`git submodule update --force`
```bash
# 强制更新所有子模块
git submodule update --force;
```

---

## 子模块冲突

**基本写法：采用当前分支的子模块版本**
`git checkout --ours <子模块路径>`
```bash
# 采用当前分支的子模块版本
git checkout --ours lib/shared;
```

**基本写法：采用合并分支的子模块版本**
`git checkout --theirs <子模块路径>`
```bash
# 采用合并分支的子模块版本
git checkout --theirs lib/shared;
```

**基本写法：添加解决后的子模块**
`git add <子模块路径>`
```bash
# 添加解决后的子模块
git add lib/shared;
```

---

## git subtree 替代方案

**基本写法：添加 subtree**
`git subtree add --prefix=<路径> <仓库地址> <分支> --squash`
```bash
# 添加 shared-lib 到 lib/shared
git subtree add --prefix=lib/shared https://github.com/user/shared-lib.git main --squash;
```

**基本写法：更新 subtree**
`git subtree pull --prefix=<路径> <仓库地址> <分支> --squash`
```bash
# 更新 lib/shared 的 subtree
git subtree pull --prefix=lib/shared https://github.com/user/shared-lib.git main --squash;
```



<!-- ============ 文档分隔线：003-git/007-GitDiffStagingOperation.md ============ -->

# git-diff 与暂存区操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## diff 三种模式

**基本写法：工作区与暂存区差异**
`git diff`
```bash
# 查看工作区与暂存区的差异
git diff;
```

**基本写法：暂存区与最新提交差异**
`git diff --staged`
```bash
# 查看暂存区与 HEAD 的差异
git diff --staged;
```

**基本写法：工作区与指定提交差异**
`git diff <commit>`
```bash
# 查看工作区与 abc1234 提交的差异
git diff abc1234;
```

---

## 统计输出

**基本写法：统计差异**
`git diff --stat`
```bash
# 显示每个文件的增删行数统计
git diff --stat;
```

**基本写法：数字统计**
`git diff --numstat`
```bash
# 输出格式：新增行数 删除行数 文件名
git diff --numstat;
```

---

## 过滤选项

**基本写法：只看文件名**
`git diff --name-only`
```bash
# 列出所有变更的文件名
git diff --name-only;
```

**基本写法：只看文件名和状态**
`git diff --name-status`
```bash
# M 修改 / A 新增 / D 删除
git diff --name-status;
```

**基本写法：按目录路径过滤**
`git diff -- <路径>`
```bash
# 查看 src/ 目录的差异
git diff -- src/;
```

**基本写法：按文件类型过滤**
`git diff -- <模式>`
```bash
# 查看 JavaScript 文件的差异
git diff -- '*.js';
```

**基本写法：排除路径**
`git diff -- ':(exclude)<模式>'`
```bash
# 排除测试文件
git diff -- ':(exclude)*.test.js';
```

---

## 显示选项

**基本写法：增加上下文行数**
`git diff -U<行数>`
```bash
# 显示 5 行上下文（默认 3 行）
git diff -U5;
```

**基本写法：忽略空白**
`git diff -w`
```bash
# 忽略所有空白变化
git diff -w;
```

**基本写法：忽略行尾空白**
`git diff --ignore-space-at-eol`
```bash
# 只忽略行尾空白
git diff --ignore-space-at-eol;
```

**基本写法：词语级别差异**
`git diff --color-words`
```bash
# 词语级别的差异高亮
git diff --color-words;
```

**基本写法：词语差异标记**
`git diff --word-diff`
```bash
# 词语级别的差异标记
git diff --word-diff;
```

**基本写法：函数上下文**
`git diff -W`
```bash
# 显示完整函数的差异
git diff -W;
```

---

## 比较选项

**基本写法：比较两个分支**
`git diff <分支1>..<分支2>`
```bash
# 比较 main 与 feature 分支
git diff main..feature;
```

**基本写法：比较两个提交**
`git diff <提交1>..<提交2>`
```bash
# 比较 abc1234 与 def5678 提交
git diff abc1234..def5678;
```

**基本写法：比较分叉点以来的变化**
`git diff <基础分支>...<目标分支>`
```bash
# feature 相对于 main 的变更
git diff main...feature;
```

**基本写法：暂存区与 HEAD 差异**
`git diff --cached`
```bash
# 查看暂存区与 HEAD 的差异
git diff --cached;
```

---

## 比较特定文件

**基本写法：比较特定文件在不同提交间的差异**
`git diff <提交> -- <文件>`
```bash
# 查看 src/index.js 在最近 3 次提交的差异
git diff HEAD~3 -- src/index.js;
```

**基本写法：比较两个分支的特定文件**
`git diff <分支1> <分支2> -- <文件>`
```bash
# 比较 main 和 feature 分支的 package.json
git diff main feature -- package.json;
```

---

## 交互式 diff

**基本写法：使用 difftool**
`git difftool`
```bash
# 使用默认 diff 工具
git difftool;
```

**基本写法：指定 diff 工具**
`git difftool --tool=<工具名>`
```bash
# 使用 vimdiff 查看差异
git difftool --tool=vimdiff;
```

---

## 查看合并冲突差异

**基本写法：检查冲突标记**
`git diff --check`
```bash
# 检查冲突标记和空白错误
git diff --check;
```

**基本写法：合并冲突的三方差异**
`git diff HEAD...MERGE_HEAD`
```bash
# 查看合并冲突的三方差异
git diff HEAD...MERGE_HEAD;
```

---

## diff 算法

**基本写法：默认算法（Myers）**
`git diff`
```bash
# 使用默认 Myers 算法
git diff;
```

**基本写法：耐心算法**
`git diff --patience`
```bash
# 使用耐心算法，适合代码重构
git diff --patience;
```

**基本写法：直方图算法**
`git diff --histogram`
```bash
# 使用直方图算法，适合复杂变更
git diff --histogram;
```

---

## 重命名检测

**基本写法：检测文件重命名**
`git diff -M`
```bash
# 检测重命名（默认 50% 相似度）
git diff -M;
```

**基本写法：指定相似度阈值**
`git diff -M<百分比>`
```bash
# 90% 相似度阈值（更严格）
git diff -M90%;
```

**基本写法：检测文件复制**
`git diff -C`
```bash
# 检测文件复制
git diff -C;
```

**基本写法：同时检测重命名和复制**
`git diff -C -M`
```bash
# 同时检测重命名和复制
git diff -C -M;
```

---

## 实用别名

**基本写法：配置 diff 别名**
`git config --global alias.<别名> "<命令>"`
```bash
# 配置常用 diff 别名
git config --global alias.d "diff";
```

**基本写法：配置暂存区差异别名**
`git config --global alias.<别名> "<命令>"`
```bash
# 配置暂存区差异别名
git config --global alias.ds "diff --staged";
```

**基本写法：配置文件名差异别名**
`git config --global alias.<别名> "<命令>"`
```bash
# 配置文件名差异别名
git config --global alias.dn "diff --name-only";
```

**基本写法：配置词语差异别名**
`git config --global alias.<别名> "<命令>"`
```bash
# 配置词语差异别名
git config --global alias.dw "diff --color-words";
```

**基本写法：配置统计差异别名**
`git config --global alias.<别名> "<命令>"`
```bash
# 配置统计差异别名
git config --global alias.dst "diff --stat";
```



<!-- ============ 文档分隔线：003-git/008-GitBranchManagement.md ============ -->

# Git 分支管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 查看分支

**基本写法：查看本地分支**
`git branch`
```bash
# 列出本地所有分支
git branch;
```

**基本写法：查看远程分支**
`git branch -r`
```bash
# 列出所有远程分支
git branch -r;
```

**基本写法：查看所有分支**
`git branch -a`
```bash
# 列出本地和远程所有分支
git branch -a;
```

**基本写法：查看分支详情**
`git branch -v`
```bash
# 显示分支名、哈希、提交消息
git branch -v;
```

---

## 创建分支

**基本写法：创建新分支**
`git branch <分支名>`
```bash
# 创建 feature/login 分支
git branch feature/login;
```

---

## 切换分支

**基本写法：切换分支**
`git checkout <分支名>`
```bash
# 切换到 feature/login 分支
git checkout feature/login;
```

**基本写法：使用 switch 切换**
`git switch <分支名>`
```bash
# 切换到 develop 分支（Git 2.23+）
git switch develop;
```

---

## 创建并切换分支

**基本写法：创建并切换**
`git checkout -b <分支名>`
```bash
# 创建并切换到 feature/login 分支
git checkout -b feature/login;
```

**基本写法：使用 switch 创建并切换**
`git switch -c <分支名>`
```bash
# 创建并切换到 feature/payment 分支（Git 2.23+）
git switch -c feature/payment;
```

---

## 合并分支

**基本写法：合并到当前分支**
`git merge <分支名>`
```bash
# 将 feature/login 合并到当前分支
git merge feature/login;
```

**基本写法：快速合并（Fast-forward）**
`git merge <分支名>`
```bash
# 切换到 main 后合并 feature/login
git checkout main;
git merge feature/login;
```

**基本写法：三方合并（3-way merge）**
`git merge <分支名>`
```bash
# 切换到 main 后合并 feature/payment
git checkout main;
git merge feature/payment;
```

---

## 合并策略

**基本写法：优先对方分支修改**
`git merge --strategy-option theirs <分支名>`
```bash
# 冲突时优先使用对方分支的修改
git merge --strategy-option theirs feature/branch;
```

**基本写法：优先当前分支修改**
`git merge --strategy-option ours <分支名>`
```bash
# 冲突时优先使用当前分支的修改
git merge --strategy-option ours feature/branch;
```

**基本写法：递归策略**
`git merge --strategy recursive <分支名>`
```bash
# 显式指定递归策略
git merge --strategy recursive feature/branch;
```

**单行写法：章鱼策略合并多个分支**
`git merge --strategy octopus <分支1> <分支2> <分支3>`
```bash
# 同时合并多个分支
git merge --strategy octopus feature1 feature2 feature3;
```

**换行写法：章鱼策略合并多个分支**
`git merge --strategy octopus <分支1> <分支2> <分支3>`
```bash
# 换行书写多个分支
git merge --strategy octopus feature1 \
                          feature2 \
                          feature3;
```

---

## 删除分支

**基本写法：安全删除**
`git branch -d <分支名>`
```bash
# 删除已合并的 feature/login 分支
git branch -d feature/login;
```

**基本写法：强制删除**
`git branch -D <分支名>`
```bash
# 强制删除未合并的 feature/login 分支
git branch -D feature/login;
```

**基本写法：删除远程分支**
`git push <远程仓库名> --delete <分支名>`
```bash
# 删除 origin 上的 feature/login 分支
git push origin --delete feature/login;
```

---

## 重命名分支

**基本写法：重命名分支**
`git branch -m <旧分支名> <新分支名>`
```bash
# 将 feature/old 重命名为 feature/new
git branch -m feature/old feature/new;
```

---

## 设置上游分支

**基本写法：设置已有分支上游**
`git branch --set-upstream-to=<远程仓库名>/<远程分支名> <本地分支名>`
```bash
# 将本地 feature/login 关联到 origin/feature/login
git branch --set-upstream-to=origin/feature/login feature/login;
```

**基本写法：首次推送时设置上游**
`git push -u <远程仓库名> <本地分支名>`
```bash
# 推送 feature/login 并设置上游
git push -u origin feature/login;
```

---

## 分支命名规范

**基本写法：命名格式约定**
`<type>/<描述>`
```text
# 功能分支：feature/login
# 修复分支：bugfix/login-error
# 紧急修复：hotfix/security-patch
# 发布分支：release/v1.0.0
# 开发分支：develop
# 主分支：main / master
```

---

## GitFlow 工作流

**基本写法：初始化 GitFlow**
`git flow init`
```bash
# 初始化 GitFlow 工作流
git flow init;
```

**基本写法：创建功能分支**
`git flow feature start <功能名>`
```bash
# 创建功能分支
git flow feature start login;
```

**基本写法：完成功能分支**
`git flow feature finish <功能名>`
```bash
# 完成功能分支
git flow feature finish login;
```

**基本写法：创建发布分支**
`git flow release start <版本号>`
```bash
# 创建发布分支
git flow release start v1.0.0;
```

**基本写法：完成发布分支**
`git flow release finish <版本号>`
```bash
# 完成发布分支
git flow release finish v1.0.0;
```

**基本写法：创建热修复分支**
`git flow hotfix start <修复名>`
```bash
# 创建热修复分支
git flow hotfix start security-patch;
```

**基本写法：完成热修复分支**
`git flow hotfix finish <修复名>`
```bash
# 完成热修复分支
git flow hotfix finish security-patch;
```

---

## 解决分支冲突

**基本写法：查看冲突文件**
`git diff`
```bash
# 查看冲突详情
git diff;
```

**基本写法：冲突标记格式**
`<<<<<<< HEAD ... ======= ... >>>>>>> <分支名>`
```text
# 冲突标记格式
<<<<<<< HEAD
当前分支的内容
=======
要合并的分支的内容
>>>>>>> feature/login
```

**基本写法：标记冲突已解决**
`git add .`
```bash
# 将解决冲突后的文件加入暂存区
git add .;
```

**基本写法：完成合并提交**
`git commit`
```bash
# 提交合并结果
git commit;
```

**基本写法：放弃合并**
`git merge --abort`
```bash
# 放弃当前合并操作
git merge --abort;
```



<!-- ============ 文档分隔线：003-git/009-GitBasicOperation.md ============ -->

# Git 基本操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 状态查看

**基本写法：查看仓库状态**
`git status`
```bash
# 显示工作区、暂存区文件状态
git status;
```

**简略写法：短格式状态**
`git status -s`
```bash
# 输出 ?? 未追踪 / A 新增暂存 / M 修改 / D 删除
git status -s;
```

---

## 暂存操作

**基本写法：暂存单个文件**
`git add <file>`
```bash
# 暂存指定文件
git add src/index.js;
```

**基本写法：暂存所有变更**
`git add .`
```bash
# 暂存当前目录下所有文件
git add .;
```

**单行写法：暂存多个文件**
`git add <file1> <file2> <file3>`
```bash
# 一次性暂存多个文件
git add src/index.js src/utils.js src/config.js;
```

**换行写法：暂存多个文件**
`git add <file1> <file2> <file3>`
```bash
# 换行书写多个文件
git add src/index.js \
        src/utils.js \
        src/config.js;
```

**基本写法：暂存已追踪文件**
`git add -u`
```bash
# 暂存所有已追踪文件的修改（不含新文件）
git add -u;
```

**基本写法：交互式暂存**
`git add -p`
```bash
# 逐代码块确认是否暂存
git add -p;
```

---

## 提交操作

**基本写法：标准提交**
`git commit -m "<message>"`
```bash
# 提交暂存区内容并附带消息
git commit -m "feat: add login module";
```

**基本写法：跳过暂存提交**
`git commit -a -m "<message>"`
```bash
# 自动暂存已追踪文件并提交
git commit -a -m "fix: resolve crash";
```

**基本写法：修改最后一次提交**
`git commit --amend -m "<message>"`
```bash
# 修改最近一次提交消息
git commit --amend -m "feat: add login module v2";
```

---

## 提交信息规范

**基本写法：约定式提交格式**
`<type>: <subject>`
```text
# type 取值：feat / fix / docs / style / refactor / test / chore
feat: add user authentication
```

---

## 查看历史

**基本写法：查看完整历史**
`git log`
```bash
# 查看完整提交历史
git log;
```

**基本写法：简洁历史**
`git log --oneline`
```bash
# 每条提交一行显示
git log --oneline;
```

**基本写法：限制条数**
`git log -n <count>`
```bash
# 查看最近 5 次提交
git log -n 5;
```

**基本写法：图形化分支历史**
`git log --graph --oneline --all`
```bash
# 查看所有分支的合并图
git log --graph --oneline --all;
```

**基本写法：查看文件历史**
`git log <file>`
```bash
# 查看 src/index.js 的修改历史
git log src/index.js;
```

**基本写法：查看提交详情**
`git show <commit-hash>`
```bash
# 查看指定提交的详情
git show abc1234;
```

---

## 查看差异

**基本写法：工作区与暂存区差异**
`git diff`
```bash
# 查看未暂存的修改
git diff;
```

**基本写法：暂存区与上次提交差异**
`git diff --cached`
```bash
# 查看已暂存但未提交的修改
git diff --cached;
```

**基本写法：分支间差异**
`git diff <branch1>..<branch2>`
```bash
# 比较 main 与 feature 分支差异
git diff main..feature;
```

**基本写法：文件差异**
`git diff <file>`
```bash
# 查看 src/index.js 的修改
git diff src/index.js;
```

---

## 撤销工作区修改

**基本写法：撤销单个文件修改**
`git checkout -- <file>`
```bash
# 撤销 src/index.js 的工作区修改
git checkout -- src/index.js;
```

**基本写法：撤销所有文件修改**
`git checkout -- .`
```bash
# 撤销所有工作区修改
git checkout -- .;
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

## 撤销提交

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

**基本写法：安全撤销（revert）**
`git revert <commit-hash>`
```bash
# 创建反向提交撤销 abc1234
git revert abc1234;
```

**单行写法：撤销多个提交**
`git revert <hash1> <hash2>`
```bash
# 撤销多个不连续的提交
git revert abc1234 def5678;
```

---

## 远程仓库基础

**基本写法：添加远程仓库**
`git remote add <name> <url>`
```bash
# 添加名为 origin 的远程仓库
git remote add origin https://github.com/user/repo.git;
```

**基本写法：查看远程仓库**
`git remote -v`
```bash
# 显示远程仓库名称和地址
git remote -v;
```

**基本写法：修改远程仓库 URL**
`git remote set-url <name> <new-url>`
```bash
# 更新 origin 的 URL
git remote set-url origin https://github.com/user/new-repo.git;
```

**基本写法：删除远程仓库**
`git remote remove <name>`
```bash
# 删除名为 origin 的远程仓库
git remote remove origin;
```

---

## 推送与拉取

**基本写法：推送到远程**
`git push <remote> <branch>`
```bash
# 推送 main 分支到 origin
git push origin main;
```

**基本写法：拉取远程更新**
`git pull <remote> <branch>`
```bash
# 拉取 origin 的 main 分支并合并
git pull origin main;
```

**基本写法：获取远程更新（不合并）**
`git fetch <remote>`
```bash
# 获取 origin 的更新但不合并
git fetch origin;
```

---

## 暂存修改（stash）

**基本写法：暂存当前修改**
`git stash`
```bash
# 暂存当前所有修改
git stash;
```

**基本写法：恢复暂存修改**
`git stash pop`
```bash
# 恢复最近一次暂存的修改并删除该暂存
git stash pop;
```

**基本写法：查看暂存列表**
`git stash list`
```bash
# 查看所有暂存记录
git stash list;
```

---

## 选择性合并

**基本写法：挑选提交合并**
`git cherry-pick <commit-hash>`
```bash
# 将 abc1234 提交应用到当前分支
git cherry-pick abc1234;
```



<!-- ============ 文档分隔线：003-git/010-GitRemoteRepoOperation.md ============ -->

# Git 远程仓库操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 添加远程仓库

**基本写法：添加远程仓库**
`git remote add <远程仓库名> <仓库地址>`
```bash
# 添加名为 origin 的远程仓库
git remote add origin https://github.com/username/repository.git;
```

---

## 查看远程仓库信息

**基本写法：查看远程仓库列表**
`git remote -v`
```bash
# 列出所有远程仓库
git remote -v;
```

**基本写法：查看远程仓库详情**
`git remote show <远程仓库名>`
```bash
# 查看 origin 的详细信息
git remote show origin;
```

---

## 重命名远程仓库

**基本写法：重命名远程仓库**
`git remote rename <旧远程仓库名> <新远程仓库名>`
```bash
# 将 origin 重命名为 upstream
git remote rename origin upstream;
```

---

## 删除远程仓库

**基本写法：删除远程仓库**
`git remote remove <远程仓库名>`
```bash
# 删除名为 origin 的远程仓库
git remote remove origin;
```

---

## 更新远程仓库 URL

**基本写法：更新远程仓库 URL**
`git remote set-url <远程仓库名> <新仓库地址>`
```bash
# 更新 origin 的 URL
git remote set-url origin https://github.com/username/new-repository.git;
```

---

## 首次推送

**基本写法：首次推送并设置上游**
`git push -u <远程仓库名> <本地分支名>:<远程分支名>`
```bash
# 首次推送到 origin 的 main 分支并设置上游
git push -u origin main;
```

---

## 后续推送

**基本写法：简化推送**
`git push`
```bash
# 推送到默认上游分支
git push;
```

**基本写法：推送指定分支**
`git push <远程仓库名> <本地分支名>:<远程分支名>`
```bash
# 推送本地 feature 到远程 feature
git push origin feature:feature;
```

**基本写法：推送所有分支**
`git push --all <远程仓库名>`
```bash
# 推送所有分支到 origin
git push --all origin;
```

**基本写法：强制推送**
`git push -f <远程仓库名> <分支名>`
```bash
# 强制推送 main 分支
git push -f origin main;
```

---

## 拉取远程更改

**基本写法：拉取并合并**
`git pull`
```bash
# 拉取默认上游分支并合并
git pull;
```

**基本写法：拉取指定分支**
`git pull <远程仓库名> <远程分支名>:<本地分支名>`
```bash
# 拉取 origin 的 main 分支到本地 main
git pull origin main:main;
```

**基本写法：允许合并不相关历史**
`git pull --allow-unrelated-histories`
```bash
# 拉取并合并不相关历史
git pull --allow-unrelated-histories;
```

---

## 获取远程更改

**基本写法：获取所有更新**
`git fetch <远程仓库名>`
```bash
# 获取 origin 的所有更新
git fetch origin;
```

**基本写法：获取所有远程仓库更新**
`git fetch --all`
```bash
# 获取所有远程仓库的更新
git fetch --all;
```

**基本写法：查看获取的远程分支**
`git branch -r`
```bash
# 列出所有远程分支
git branch -r;
```

---

## 远程分支管理

**基本写法：从远程分支创建本地分支**
`git checkout -b <本地分支名> <远程仓库名>/<远程分支名>`
```bash
# 基于 origin/feature 创建本地 feature 分支
git checkout -b feature origin/feature;
```

**基本写法：跟踪远程分支**
`git branch --set-upstream-to=<远程仓库名>/<远程分支名> <本地分支名>`
```bash
# 将本地 main 跟踪 origin/main
git branch --set-upstream-to=origin/main main;
```

**基本写法：删除远程分支**
`git push <远程仓库名> --delete <分支名>`
```bash
# 删除 origin 上的 feature 分支
git push origin --delete feature;
```

---

## SSH 密钥配置

**基本写法：生成 ed25519 SSH 密钥**
`ssh-keygen -t <算法> -C "<注释>"`
```bash
# 生成 ed25519 算法的 SSH 密钥
ssh-keygen -t ed25519 -C "your_email@example.com";
```

**基本写法：生成 RSA SSH 密钥**
`ssh-keygen -t <算法> -b <位数> -C "<注释>"`
```bash
# 生成 RSA 算法的 SSH 密钥
ssh-keygen -t rsa -b 4096 -C "your_email@example.com";
```

**基本写法：查看 ed25519 SSH 公钥**
`cat ~/.ssh/<密钥文件>.pub`
```bash
# 查看 ed25519 公钥
cat ~/.ssh/id_ed25519.pub;
```

**基本写法：查看 RSA SSH 公钥**
`cat ~/.ssh/<密钥文件>.pub`
```bash
# 查看 RSA 公钥
cat ~/.ssh/id_rsa.pub;
```

**基本写法：测试 GitHub SSH 连接**
`ssh -T git@<域名>`
```bash
# 测试 GitHub 连接
ssh -T git@github.com;
```

**基本写法：测试 GitLab SSH 连接**
`ssh -T git@<域名>`
```bash
# 测试 GitLab 连接
ssh -T git@gitlab.com;
```

---

## 高级远程操作

**基本写法：推送特定提交**
`git push <远程仓库名> <提交哈希>:<远程分支名>`
```bash
# 将 abc1234 提交推送到 origin 的 main 分支
git push origin abc1234:main;
```

**基本写法：推送所有标签**
`git push --tags <远程仓库名>`
```bash
# 推送所有标签到 origin
git push --tags origin;
```

**基本写法：推送特定标签**
`git push <远程仓库名> <标签名>`
```bash
# 推送 v1.0.0 标签到 origin
git push origin v1.0.0;
```

**基本写法：同步远程分支（清理）**
`git fetch --prune <远程仓库名>`
```bash
# 同步 origin 并清理已删除的远程分支
git fetch --prune origin;
```

**基本写法：同步所有远程仓库并清理**
`git fetch --all --prune`
```bash
# 同步所有远程仓库并清理
git fetch --all --prune;
```

---

## 多远程仓库管理

**基本写法：添加主仓库**
`git remote add <名称> <地址>`
```bash
# 添加主仓库 origin
git remote add origin https://github.com/username/repository.git;
```

**基本写法：添加备份仓库**
`git remote add <名称> <地址>`
```bash
# 添加备份仓库 backup
git remote add backup https://gitee.com/username/repository.git;
```

**基本写法：推送到主仓库**
`git push <远程仓库名> <分支名>`
```bash
# 推送到主仓库 origin
git push origin main;
```

**基本写法：推送到备份仓库**
`git push <远程仓库名> <分支名>`
```bash
# 推送到备份仓库 backup
git push backup main;
```

**基本写法：从特定远程拉取**
`git pull <远程仓库名> <分支名>`
```bash
# 从备份仓库拉取 main 分支
git pull backup main;
```



<!-- ============ 文档分隔线：003-git/011-GitAdvancedWorkflow.md ============ -->

# Git 高级命令与工作流速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 配置管理

**基本写法：设置全局用户**
`git config --global user.name "<姓名>"`
```bash
# 配置用户名
git config --global user.name "Alice"
git config --global user.email "alice@example.com"
```

---

**基本写法：查看配置**
`git config --list`
```bash
# 查看所有配置
git config --list
# 查看特定配置
git config user.name
```

---

**基本写法：设置默认编辑器**
`git config --global core.editor "<命令>"`
```bash
# 设置 VS Code 为默认编辑器
git config --global core.editor "code --wait"
```

---

**基本写法：配置别名**
`git config --global alias.<别名> "<命令>"`
```bash
# 设置别名
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph"
```

---

## 暂存与恢复

**基本写法：stash 暂存修改**
`git stash [push -m "<消息>"]`
```bash
# 暂存当前修改
git stash
# 带消息暂存
git stash push -m "WIP: feature A"
```

---

**基本写法：查看暂存列表**
`git stash list`
```bash
# 列出所有暂存
git stash list
```

---

**基本写法：恢复暂存**
`git stash pop [<索引>]`
```bash
# 恢复最近暂存并删除
git stash pop
# 恢复指定暂存
git stash pop stash@{1}
```

---

**基本写法：应用暂存不删除**
`git stash apply [<索引>]`
```bash
# 应用最近暂存（保留暂存）
git stash apply
```

---

**基本写法：清除暂存**
`git stash drop [<索引>]`
```bash
# 删除最近暂存
git stash drop
# 删除所有暂存
git stash clear
```

---

## 提交修改

**基本写法：修改最近提交**
`git commit --amend [-m "<消息>"]`
```bash
# 修改最近提交的消息
git commit --amend -m "新消息"
# 将新改动加入最近提交
git add . && git commit --amend --no-edit
```

---

**基本写法：交互式添加**
`git add -p`
```bash
# 选择性添加改动块
git add -p
```

---

**基本写法：空提交**
`git commit --allow-empty -m "<消息>"`
```bash
# 创建空提交（触发 CI 等）
git commit --allow-empty -m "trigger deploy"
```

---

## 分支操作

**基本写法：查看分支**
`git branch [-a] [-v]`
```bash
# 查看本地分支
git branch
# 查看所有分支（含远程）
git branch -a
# 查看分支详细信息
git branch -vv
```

---

**基本写法：重命名分支**
`git branch -m [<旧名>] <新名>`
```bash
# 重命名当前分支
git branch -m new-name
# 重命名指定分支
git branch -m old-name new-name
```

---

**基本写法：删除分支**
`git branch -d <分支名>`
```bash
# 安全删除（已合并）
git branch -d feature
# 强制删除
git branch -D feature
```

---

**基本写法：追踪远程分支**
`git branch -u <远程>/<分支>`
```bash
# 设置上游分支
git branch -u origin/main
```

---

## 合并策略

**基本写法：合并分支**
`git merge <分支> [--no-ff]`
```bash
# 默认合并（可能 fast-forward）
git merge feature
# 强制创建合并提交
git merge --no-ff feature
```

---

**基本写法：变基**
`git rebase <目标分支>`
```bash
# 将当前分支变基到 main
git rebase main
```

---

**基本写法：交互式变基**
`git rebase -i <提交>`
```bash
# 压缩最近 3 次提交
git rebase -i HEAD~3
```

---

**基本写法：中止变基**
`git rebase --abort`
```bash
# 取消变基
git rebase --abort
```

---

**基本写法：解决冲突后继续**
`git rebase --continue`
```bash
# 解决冲突后继续变基
git add . && git rebase --continue
```

---

## 远程仓库

**基本写法：添加远程**
`git remote add <名称> <URL>`
```bash
# 添加远程仓库
git remote add origin https://github.com/user/repo.git
```

---

**基本写法：查看远程**
`git remote -v`
```bash
# 查看所有远程
git remote -v
```

---

**基本写法：修改远程 URL**
`git remote set-url <名称> <新URL>`
```bash
# 修改远程地址
git remote set-url origin git@github.com:user/repo.git
```

---

**基本写法：拉取与推送**
`git pull [<远程>] [<分支>]`
```bash
# 拉取并合并
git pull origin main
# 推送
git push origin main
# 推送并设置上游
git push -u origin feature
```

---

**基本写法：强制推送**
`git push --force-with-lease`
```bash
# 安全的强制推送（推荐）
git push --force-with-lease
```

---

## 历史查看

**基本写法：查看提交历史**
`git log [--oneline] [--graph] [-<数量>]`
```bash
# 单行显示历史
git log --oneline
# 图形化显示
git log --oneline --graph --all
# 查看最近 10 条
git log -10
```

---

**基本写法：查看文件历史**
`git log -p <文件>`
```bash
# 查看文件的变更历史
git log -p src/main.py
```

---

**基本写法：搜索提交**
`git log --grep="<关键词>"`
```bash
# 按消息搜索提交
git log --grep="fix"
```

---

**基本写法：查看作者提交**
`git log --author="<姓名>"`
```bash
# 按作者过滤
git log --author="Alice"
```

---

## 撤销与回退

**基本写法：撤销工作区修改**
`git checkout -- <文件>`
```bash
# 丢弃工作区修改
git checkout -- file.txt
```

---

**基本写法：取消暂存**
`git reset HEAD <文件>`
```bash
# 取消已暂存的文件
git reset HEAD file.txt
```

---

**基本写法：软回退**
`git reset --soft <提交>`
```bash
# 回退提交，保留改动在暂存区
git reset --soft HEAD~1
```

---

**基本写法：硬回退**
`git reset --hard <提交>`
```bash
# 完全回退（慎用）
git reset --hard HEAD~1
```

---

**基本写法：撤销提交**
`git revert <提交>`
```bash
# 创建反向提交
git revert abc123
```

---

## 标签管理

**基本写法：创建标签**
`git tag [-a] <标签名> [-m "<消息>"] [<提交>]`
```bash
# 创建轻量标签
git tag v1.0
# 创建附注标签
git tag -a v1.0 -m "Release 1.0"
```

---

**基本写法：推送标签**
`git push <远程> <标签>`
```bash
# 推送单个标签
git push origin v1.0
# 推送所有标签
git push origin --tags
```

---

**基本写法：删除标签**
`git tag -d <标签名>`
```bash
# 删除本地标签
git tag -d v1.0
# 删除远程标签
git push origin --delete v1.0
```

---

## 二分查找

**基本写法：git bisect**
`git bisect start`
```bash
# 启动二分查找
git bisect start
git bisect bad          # 标记当前为坏
git bisect good v1.0     # 标记 v1.0 为好
# 测试后标记
git bisect good  # 或 bad
# 完成查找
git bisect reset
```

---

## 樱桃挑选

**基本写法：cherry-pick**
`git cherry-pick <提交>`
```bash
# 选择性合并某个提交
git cherry-pick abc123
```

---

## 子模块

**基本写法：添加子模块**
`git submodule add <URL> [<路径>]`
```bash
# 添加子模块
git submodule add https://github.com/user/lib.git libs/lib
```

---

**基本写法：初始化子模块**
`git submodule update --init --recursive`
```bash
# 克隆后初始化子模块
git submodule update --init --recursive
```

---

## 工作树

**基本写法：添加工作树**
`git worktree add <路径> <分支>`
```bash
# 创建新工作树
git worktree add ../feature-work feature
```

---

**基本写法：列出工作树**
`git worktree list`
```bash
# 查看所有工作树
git worktree list
```

---

**基本写法：删除工作树**
`git worktree remove <路径>`
```bash
# 删除工作树
git worktree remove ../feature-work
```



<!-- ============ 文档分隔线：003-git/012-GitConfig.md ============ -->

# Git 配置管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 配置级别

**基本写法：设置仓库级配置（仅当前仓库）**
`git config <键> <值>`
```bash
# 设置当前仓库的用户名
git config user.name "Alice"
```

---

**基本写法：设置全局级配置（当前用户所有仓库）**
`git config --global <键> <值>`
```bash
# 设置全局用户邮箱
git config --global user.email "alice@example.com"
```

---

**基本写法：设置系统级配置（本机所有用户）**
`git config --system <键> <值>`
```bash
# 设置系统级默认分支名（需管理员权限）
git config --system init.defaultBranch main
```

---

**基本写法：查看某级别配置来源**
`git config --show-origin <键>`
```bash
# 显示配置项来自哪个文件
git config --show-origin user.name
```

---

## 查看配置

**基本写法：查看所有配置（合并后最终值）**
`git config --list`
```bash
# 列出所有生效配置
git config --list
```

---

**基本写法：查看指定级别配置**
`git config --list --<级别>`
```bash
# 仅查看全局级配置
git config --list --global
```

---

**基本写法：查看单个配置项**
`git config <键>`
```bash
# 查看当前用户名
git config user.name
```

---

**基本写法：查看配置类型**
`git config --type <类型> <键>`
```bash
# 以布尔类型读取配置
git config --type bool core.autocrlf
```

---

## 编辑配置文件

**基本写法：直接打开配置文件编辑**
`git config --<级别> --edit`
```bash
# 用默认编辑器打开全局配置
git config --global --edit
```

---

## 用户身份

**基本写法：配置提交身份**
`git config --global user.name "<姓名>"`
```bash
# 设置全局提交姓名
git config --global user.name "Alice Lee"
```

---

**基本写法：配置提交邮箱**
`git config --global user.email "<邮箱>"`
```bash
# 设置全局提交邮箱
git config --global user.email "alice@example.com"
```

---

**基本写法：按仓库单独配置身份**
`git config user.name "<姓名>"`
```bash
# 仅当前仓库使用工作账号
git config user.name "Alice Corp"
```

---

## 默认分支与初始化

**基本写法：设置 init 默认分支**
`git config --global init.defaultBranch <分支名>`
```bash
# 新仓库默认使用 main 分支
git config --global init.defaultBranch main
```

---

## 行尾处理

**基本写法：Windows 自动转 CRLF**
`git config --global core.autocrlf true`
```bash
# 检出转 CRLF，提交转 LF
git config --global core.autocrlf true
```

---

**基本写法：Linux/Mac 保留 LF**
`git config --global core.autocrlf input`
```bash
# 检出保留 LF，提交转 LF
git config --global core.autocrlf input
```

---

## 编辑器与工具

**基本写法：设置默认编辑器**
`git config --global core.editor "<命令>"`
```bash
# 使用 VS Code 作为默认编辑器
git config --global core.editor "code --wait"
```

---

**基本写法：设置默认合并工具**
`git config --global merge.tool <工具>`
```bash
# 配置 VS Code 为合并工具
git config --global merge.tool vscode
```

---

**基本写法：配置合并工具路径**
`git config --global mergetool.<工具>.cmd "<命令>"`
```bash
# 配置 vscode 合并工具调用命令
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
```

---

## 别名（alias）

**基本写法：设置命令别名**
`git config --global alias.<别名> "<命令>"`
```bash
# 用 co 代替 checkout
git config --global alias.co checkout
```

---

**基本写法：设置带参数别名**
`git config --global alias.<别名> "!<脚本>"`
```bash
# 用 ! 前缀执行外部命令
git config --global alias.lg "log --oneline --graph --all"
```

---

**基本写法：删除别名**
`git config --global --unset alias.<别名>`
```bash
# 移除 co 别名
git config --global --unset alias.co
```

---

## 拉取与推送行为

**基本写法：拉取时默认使用 rebase**
`git config --global pull.rebase true`
```bash
# pull 默认变基而非合并
git config --global pull.rebase true
```

---

**基本写法：拉取仅快进**
`git config --global pull.ff only`
```bash
# 仅允许快进拉取，否则失败
git config --global pull.ff only
```

---

**基本写法：推送默认模式**
`git config --global push.default <模式>`
```bash
# 只推送当前分支到同名上游
git config --global push.default simple
```

---

## 颜色与输出

**基本写法：开启颜色输出**
`git config --global color.ui auto`
```bash
# 终端自动启用颜色
git config --global color.ui auto
```

---

## 凭据缓存

**基本写法：开启凭据助手**
`git config --global credential.helper <助手>`
```bash
# 使用系统凭据管理器
git config --global credential.helper manager
```

---

**基本写法：临时内存缓存**
`git config --global credential.helper 'cache --timeout=<秒>'`
```bash
# 凭据缓存 1 小时
git config --global credential.helper 'cache --timeout=3600'
```

---

## 增删改配置项

**基本写法：新增或修改配置项**
`git config --<级别> <键> <值>`
```bash
# 修改全局 init 默认分支
git config --global init.defaultBranch main
```

---

**基本写法：删除配置项**
`git config --<级别> --unset <键>`
```bash
# 删除全局用户名配置
git config --global --unset user.name
```

---

**基本写法：删除多处同键配置**
`git config --<级别> --unset-all <键>`
```bash
# 删除所有同名配置项
git config --local --unset-all remote.origin.fetch
```

---

**基本写法：追加多值配置**
`git config --<级别> --add <键> <值>`
```bash
# 追加一条 fetch 规则
git config --local --add remote.origin.fetch '+refs/tags/*:refs/tags/*'
```

---

## 引用存储格式（Reftable）

**基本写法：查看引用存储格式**
`git config core.refStorage`
```bash
# 查看当前引用存储后端
git config core.refStorage
```

---

**基本写法：迁移到 reftable 后端**
`git refs migrate --ref-storage=reftable`
```bash
# 切换到 reftable 引用存储（适用于多分支大仓）
git refs migrate --ref-storage=reftable
```

---

## 文件路径与位置

**基本写法：查看各级别配置文件路径**
`git config --list --show-origin`
```bash
# 显示每条配置来源文件
git config --list --show-origin
```

---

**基本写法：仓库级配置文件位置**
`.git/config`
```bash
# 编辑当前仓库配置文件
git config --local --edit
```

---

**基本写法：全局配置文件位置**
`~/.gitconfig`
```bash
# 编辑用户级配置文件
git config --global --edit
```

---

**基本写法：系统级配置文件位置**
`/etc/gitconfig`
```bash
# 编辑系统级配置文件（需管理员权限）
git config --system --edit
```



<!-- ============ 文档分隔线：003-git/013-GitReflog.md ============ -->

# Git reflog 与恢复

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 查看 reflog

**基本写法：查看当前分支引用日志**
`git reflog [show]`
```bash
# 查看当前分支的引用日志
git reflog
```

---

**基本写法：查看指定分支引用日志**
`git reflog <分支名>`
```bash
# 查看 main 分支的引用日志
git reflog main
```

---

**基本写法：查看 HEAD 引用日志**
`git reflog show HEAD`
```bash
# 查看 HEAD 的所有移动记录
git reflog show HEAD
```

---

**基本写法：限定显示条数**
`git reflog -<数量>`
```bash
# 仅显示最近 5 条引用记录
git reflog -5
```

---

**基本写法：带日期过滤**
`git reflog --since="<时间>"`
```bash
# 仅显示最近 2 小时的记录
git reflog --since="2 hours ago"
```

---

## reflog 输出格式

**基本写法：自定义输出格式**
`git reflog --format="<格式>"`
```bash
# 自定义显示提交哈希与引用动作
git reflog --format="%h %gs"
```

---

**基本写法：显示时间戳**
`git reflog --date=iso`
```bash
# 以 ISO 格式显示日期
git reflog --date=iso
```

---

## 恢复丢失的提交

**基本写法：通过 reflog 哈希恢复提交**
`git reset --hard <reflog哈希>`
```bash
# 重置到 reflog 记录的某次提交
git reset --hard HEAD@{2}
```

---

**基本写法：通过 cherry-pick 恢复单个提交**
`git cherry-pick <reflog哈希>`
```bash
# 将丢失的提交重新应用
git cherry-pick 9a3b1c2
```

---

**基本写法：创建新分支保存丢失提交**
`git branch <分支名> <reflog哈希>`
```bash
# 用新分支指向丢失的提交
git branch recover-work HEAD@{3}
```

---

**基本写法：强制移动分支到 reflog 位置**
`git branch -f <分支名> <reflog哈希>`
```bash
# 将分支强制指向 reflog 记录
git branch -f feature HEAD@{1}
```

---

## 恢复误删分支

**基本写法：通过 reflog 重建被删分支**
`git branch <分支名> <reflog哈希>`
```bash
# 恢复已删除的 feature 分支
git branch feature feature@{2}
```

---

**基本写法：查看已删除分支的 reflog**
`git reflog show <已删除分支名>`
```bash
# 查看已删除分支历史位置
git reflog show deleted-branch
```

---

## 恢复误用 reset

**基本写法：撤销硬重置**
`git reset --hard HEAD@{1}`
```bash
# 回到 reset 之前的位置
git reset --hard HEAD@{1}
```

---

**基本写法：用 ORIG_HEAD 恢复**
`git reset --hard ORIG_HEAD`
```bash
# 使用上次操作前的 HEAD
git reset --hard ORIG_HEAD
```

---

## reflog 过期与管理

**基本写法：查看 reflog 子命令**
`git reflog --help`
```bash
# 查看 reflog 完整用法
git reflog --help
```

---

**基本写法：删除单条 reflog 记录**
`git reflog delete <引用>@{<序号>}`
```bash
# 删除指定 reflog 条目
git reflog delete HEAD@{5}
```

---

**基本写法：立即过期所有 reflog**
`git reflog expire --expire=now --all`
```bash
# 标记所有 reflog 条目为过期
git reflog expire --expire=now --all
```

---

**基本写法：按时间过期 reflog**
`git reflog expire --expire=<时间> --all`
```bash
# 90 天前的可达条目过期
git reflog expire --expire=90.days --all
```

---

**基本写法：过期不可达条目**
`git reflog expire --expire-unreachable=<时间> --all`
```bash
# 30 天前不可达的条目过期
git reflog expire --expire-unreachable=30.days --all
```

---

## 与 fsck 配合查找悬空对象

**基本写法：查找所有悬空提交**
`git fsck --lost-found`
```bash
# 查找未引用的对象并写入 .git/lost-found
git fsck --lost-found
```

---

**基本写法：查看悬空提交内容**
`git show <悬空提交哈希>`
```bash
# 查看悬空提交的变更
git show d1f2a3b
```

---

## 配置 reflog 保留时长

**基本写法：设置可达条目保留时间**
`git config --global gc.reflogExpire "<时间>"`
```bash
# 可达条目保留 90 天
git config --global gc.reflogExpire "90 days"
```

---

**基本写法：设置不可达条目保留时间**
`git config --global gc.reflogExpireUnreachable "<时间>"`
```bash
# 不可达条目保留 30 天
git config --global gc.reflogExpireUnreachable "30 days"
```

---

**基本写法：禁用某 ref 自动写 reflog**
`git config --global core.logAllRefUpdates false`
```bash
# 关闭自动记录引用更新
git config --global core.logAllRefUpdates false
```

---

## reflog 与 stash 协同

**基本写法：查看 stash 的 reflog**
`git reflog show stash`
```bash
# 查看 stash 栈所有变更
git reflog show stash
```

---

**基本写法：恢复误删的 stash**
`git stash apply <stash@{n}>`
```bash
# 通过 reflog 找回已 drop 的 stash
git stash apply stash@{2}
```



<!-- ============ 文档分隔线：003-git/014-GitBisect.md ============ -->

# Git bisect 二分查找

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 启动与基本流程

**基本写法：启动二分查找**
`git bisect start`
```bash
# 进入 bisect 模式
git bisect start
```

---

**基本写法：标记当前提交为坏**
`git bisect bad [<提交>]`
```bash
# 标记 HEAD 为有问题的提交
git bisect bad
```

---

**基本写法：标记已知的好提交**
`git bisect good <提交>`
```bash
# 指定一个正常的旧提交
git bisect good v1.0.0
```

---

**基本写法：一行启动并指定好坏**
`git bisect start <坏提交> <好提交>`
```bash
# 同时指定坏起点与好起点
git bisect start HEAD v1.0.0
```

---

## 标记测试结果

**基本写法：当前提交标记为好**
`git bisect good`
```bash
# 当前测试通过，继续二分
git bisect good
```

---

**基本写法：当前提交标记为坏**
`git bisect bad`
```bash
# 当前测试失败，继续二分
git bisect bad
```

---

**基本写法：跳过当前提交**
`git bisect skip`
```bash
# 跳过无法测试的提交
git bisect skip
```

---

## 查看状态

**基本写法：查看二分状态**
`git bisect status`
```bash
# 显示当前 bisect 进度
git bisect status
```

---

**基本写法：查看剩余待测提交**
`git bisect visualize`
```bash
# 用 git log 查看剩余范围
git bisect visualize
```

---

**基本写法：查看已测试提交日志**
`git bisect log`
```bash
# 输出 bisect 操作过程
git bisect log
```

---

## 自动化二分

**基本写法：自动二分测试**
`git bisect run <命令> [<参数>]`
```bash
# 用测试脚本自动定位首坏提交
git bisect run npm test
```

---

**基本写法：通过脚本退出码判定**
`git bisect run <脚本>`
```bash
# 125 表示跳过，0 好，1-124 坏
git bisect run ./scripts/check-bug.sh
```

---

**基本写法：编译并测试**
`git bisect run <命令1> && <命令2>`
```bash
# 先编译再测试
git bisect run sh -c 'make && make test'
```

---

## 范围控制

**基本写法：限定路径范围**
`git bisect start -- <路径>`
```bash
# 只二分指定路径下的变更
git bisect start -- src/auth
```

---

**基本写法：排除某些提交**
`git bisect skip <提交1> <提交2>`
```bash
# 跳过多条已知不可测提交
git bisect skip abc1234 def5678
```

---

## 结束与回退

**基本写法：结束二分查找**
`git bisect reset`
```bash
# 退出 bisect 模式回到原分支
git bisect reset
```

---

**基本写法：结束后切回指定分支**
`git bisect reset <分支>`
```bash
# 退出并切回 main 分支
git bisect reset main
```

---

## 恢复中断的二分

**基本写法：记录二分过程到文件**
`git bisect log > <文件>`
```bash
# 保存当前 bisect 状态
git bisect log > bisect.log
```

---

**基本写法：从文件恢复二分状态**
`git bisect replay <文件>`
```bash
# 重新执行记录的 bisect 步骤
git bisect replay bisect.log
```

---

## 查看引入问题的提交

**基本写法：定位首坏提交后查看**
`git show <提交>`
```bash
# 查看被 bisect 锁定的提交内容
git show HEAD
```

---

**基本写法：查看引入问题的差异**
`git diff <好提交> <坏提交>`
```bash
# 查看好坏提交之间的差异
git diff v1.0.0 HEAD
```



<!-- ============ 文档分隔线：003-git/015-GitCherryPick.md ============ -->

# Git cherry-pick

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：应用单个提交到当前分支**
`git cherry-pick <提交>`
```bash
# 将指定提交应用到当前分支
git cherry-pick abc1234
```

---

**基本写法：应用多个提交**
`git cherry-pick <提交1> <提交2>`
```bash
# 按顺序应用多个提交
git cherry-pick abc1234 def5678
```

---

**基本写法：应用提交范围**
`git cherry-pick <起点>..<终点>`
```bash
# 应用从起点之后到终点的提交（不含起点）
git cherry-pick v1.0.0..v1.1.0
```

---

**基本写法：应用包含起点的范围**
`git cherry-pick <起点>^..<终点>`
```bash
# 应用从起点到终点的所有提交
git cherry-pick v1.0.0^..v1.1.0
```

---

## 保留信息

**基本写法：保留原提交作者**
`git cherry-pick -x <提交>`
```bash
# 在提交信息中追加原提交哈希
git cherry-pick -x abc1234
```

---

**基本写法：保留原提交哈希引用**
`git cherry-pick --edit <提交>`
```bash
# 应用时打开编辑器修改提交信息
git cherry-pick --edit abc1234
```

---

**基本写法：使用原提交信息**
`git cherry-pick --no-commit <提交>`
```bash
# 应用变更但不立即提交
git cherry-pick --no-commit abc1234
```

---

**基本写法：自定义提交信息**
`git cherry-pick --signoff <提交>`
```bash
# 添加 Signed-off-by 签名
git cherry-pick --signoff abc1234
```

---

## 冲突处理

**基本写法：继续 cherry-pick**
`git cherry-pick --continue`
```bash
# 解决冲突后继续
git cherry-pick --continue
```

---

**基本写法：放弃当前 cherry-pick**
`git cherry-pick --abort`
```bash
# 取消并回到操作前状态
git cherry-pick --abort
```

---

**基本写法：跳过当前提交**
`git cherry-pick --skip`
```bash
# 跳过当前冲突提交继续下一个
git cherry-pick --skip
```

---

**基本写法：保留冲突标记的合并提交**
`git cherry-pick --keep-redundant-commits <提交>`
```bash
# 即使变更已被包含也保留提交
git cherry-pick --keep-redundant-commits abc1234
```

---

## 策略选项

**基本写法：指定合并策略**
`git cherry-pick -X <策略> <提交>`
```bash
# 使用 theirs 策略优先采用被应用提交
git cherry-pick -X theirs abc1234
```

---

**基本写法：使用 ours 策略**
`git cherry-pick -X ours <提交>`
```bash
# 冲突时优先保留当前分支内容
git cherry-pick -X ours abc1234
```

---

## 主分支回退场景

**基本写法：从 hotfix 分支拣选修复到 main**
`git cherry-pick <修复提交>`
```bash
# 切到 main 后应用 hotfix 提交
git cherry-pick hotfix-9a3b1c2
```

---

**基本写法：从 main 拣选到发布分支**
`git cherry-pick <提交>`
```bash
# 将 main 上的修复同步到 release 分支
git cherry-pick release-1.2.3
```

---

## 批量操作

**基本写法：批量拣选多分支提交**
`git cherry-pick <分支A>^..<分支B>`
```bash
# 拣选 A 到 B 范围内的所有提交
git cherry-pick feature^..release
```

---

**基本写法：从 git log 拣选**
`git cherry-pick $(git log --grep="<关键字>" --format=%H)`
```bash
# 拣选所有匹配关键字的提交
git cherry-pick $(git log --grep="fix:" --format=%H)
```

---

## 验证与查询

**基本写法：查看哪些提交尚未应用**
`git cherry -v <上游分支>`
```bash
# 显示尚未合并到上游的提交
git cherry -v main
```

---

**基本写法：显示带 + 或 - 的可拣选提交**
`git cherry <上游> <分支>`
```bash
# 列出指定分支相对上游的可拣选状态
git cherry main feature
```



<!-- ============ 文档分隔线：003-git/016-GitFilterRepo.md ============ -->

# Git filter-repo 与历史改写

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 准备工作

**基本写法：安装 git-filter-repo**
`pip install git-filter-repo`
```bash
# 通过 pip 安装官方推荐工具
pip install git-filter-repo
```

---

**基本写法：克隆待改写仓库**
`git clone --mirror <仓库URL> <目录>`
```bash
# 镜像克隆保留所有引用
git clone --mirror https://github.com/org/repo.git repo.git
```

---

**基本写法：创建备份分支**
`git branch backup-main main`
```bash
# 改写前备份当前分支
git branch backup-main main
```

---

## filter-repo 基本用法

**基本写法：分析仓库历史**
`git filter-repo --analyze`
```bash
# 生成历史分析报告到 .git/filter-repo
git filter-repo --analyze
```

---

**基本写法：移除某文件历史**
`git filter-repo --path <路径> --invert-paths`
```bash
# 从所有历史中移除 secrets.env
git filter-repo --path secrets.env --invert-paths
```

---

**基本写法：保留某路径并移除其他**
`git filter-repo --path <路径>`
```bash
# 只保留 src 目录历史
git filter-repo --path src/
```

---

**基本写法：移除整个目录**
`git filter-repo --path <目录>/ --invert-paths`
```bash
# 移除 vendor 目录的所有历史
git filter-repo --path vendor/ --invert-paths
```

---

## 改写作者信息

**基本写法：替换作者邮箱**
`git filter-repo --mailmap <mailmap文件>`
```bash
# 用 mailmap 文件统一作者信息
git filter-repo --mailmap mailmap.txt
```

---

**基本写法：直接替换提交者**
`git filter-repo --commit-callback '<脚本>'`
```bash
# 用回调函数批量改写提交者
git filter-repo --commit-callback 'commit.author_email = b"new@example.com"'
```

---

**基本写法：mailmap 文件格式**
`<新姓名> <新邮箱> <旧邮箱>`
```bash
# 在 mailmap.txt 中映射旧邮箱到新身份
Alice Lee <alice@example.com> <old@domain.com>
```

---

## 移除敏感信息

**基本写法：移除包含密码的文件**
`git filter-repo --path <文件> --invert-paths`
```bash
# 从历史中彻底删除配置文件
git filter-repo --path config/passwords.yml --invert-paths
```

---

**基本写法：按内容替换文本**
`git filter-repo --replace-text <替换文件>`
```bash
# 用替换规则批量清除敏感字符串
git filter-repo --replace-text replacements.txt
```

---

**基本写法：替换文件格式**
`<旧字符串>==><新字符串>`
```bash
# 在 replacements.txt 中定义替换规则
SECRET_KEY==>REDACTED
```

---

**基本写法：正则替换**
`regex:<正则>==><替换>`
```bash
# 用正则匹配并替换
regex:\b\d{16}\b==>****-****-****-****
```

---

## 重命名与移动

**基本写法：重命名目录**
`git filter-repo --path-rename <旧路径>:<新路径>`
```bash
# 将 src 重命名为 lib/src
git filter-repo --path-rename src/:lib/src/
```

---

**基本写法：合并多目录**
`git filter-repo --path-rename <旧1>:<新> --path-rename <旧2>:<新>`
```bash
# 合并两个目录到同一位置
git filter-repo --path-rename old-a/:src/ --path-rename old-b/:src/
```

---

## 分支与标签处理

**基本写法：仅改写指定分支**
`git filter-repo --refs <分支>`
```bash
# 仅改写 main 分支历史
git filter-repo --refs main
```

---

**基本写法：保留所有标签**
`git filter-repo --tags`
```bash
# 改写时同时更新所有标签
git filter-repo --tags
```

---

**基本写法：删除某标签**
`git filter-repo --refs <分支> --invert-paths --path <文件>`
```bash
# 删除 main 中某文件并保留其他引用
git filter-repo --refs main --invert-paths --path secret.env
```

---

## 提交信息改写

**基本写法：修改提交信息**
`git filter-repo --message-callback '<脚本>'`
```bash
# 用回调函数改写提交信息
git filter-repo --message-callback b"feat: " + message if message.startswith(b"add") else message'
```

---

**基本写法：移除特定关键字**
`git filter-repo --replace-message <替换文件>`
```bash
# 替换提交信息中的敏感词
git filter-repo --replace-message replacements.txt
```

---

## 推送与协作

**基本写法：强制推送改写后的历史**
`git push --force-with-lease origin <分支>`
```bash
# 安全地强制推送改写历史
git push --force-with-lease origin main
```

---

**基本写法：推送所有引用**
`git push --mirror origin`
```bash
# 推送所有分支与标签（镜像推送）
git push --mirror origin
```

---

**基本写法：通知协作者重新克隆**
`git push --force origin <分支>`
```bash
# 改写后强制推送，要求团队重新克隆
git push --force origin main
```

---

## filter-branch（不推荐但仍可用）

**基本写法：用 filter-branch 移除文件**
`git filter-branch --tree-filter 'rm -f <文件>' HEAD`
```bash
# 旧式逐提交删除文件（速度慢）
git filter-branch --tree-filter 'rm -f secrets.env' HEAD
```

---

**基本写法：改写作者**
`git filter-branch --env-filter '<脚本>' HEAD`
```bash
# 用环境过滤器改写作者信息
git filter-branch --env-filter 'export GIT_AUTHOR_EMAIL="new@example.com"' HEAD
```

---

**基本写法：清理 filter-branch 备份**
`git for-each-ref --format="%(refname)" refs/original/ | xargs -n 1 git update-ref -d`
```bash
# 删除 filter-branch 创建的备份引用
git for-each-ref --format="%(refname)" refs/original/ | xargs -n 1 git update-ref -d
```

---

## 验证与回收

**基本写法：验证改写结果**
`git log --all --pretty=format:"%H %an <%ae> %s"`
```bash
# 检查所有提交作者信息
git log --all --pretty=format:"%H %an <%ae> %s"
```

---

**基本写法：回收空间**
`git reflog expire --expire=now --all && git gc --prune=now`
```bash
# 清理悬空对象并立即回收
git reflog expire --expire=now --all && git gc --prune=now
```

---

**基本写法：检查悬空对象**
`git fsck --full --unreachable`
```bash
# 列出所有不可达对象
git fsck --full --unreachable
```



<!-- ============ 文档分隔线：003-git/017-GitArchive.md ============ -->

# Git archive 归档导出

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：导出 tar 归档**
`git archive --format=tar <提交> -o <文件>`
```bash
# 将 HEAD 导出为 tar 文件
git archive --format=tar HEAD -o project.tar
```

---

**基本写法：导出 zip 归档**
`git archive --format=zip <提交> -o <文件>`
```bash
# 将 HEAD 导出为 zip 文件
git archive --format=zip HEAD -o project.zip
```

---

**基本写法：根据扩展名自动识别格式**
`git archive <提交> -o <文件>`
```bash
# 通过 .tar.gz 扩展名自动选格式与压缩
git archive HEAD -o project.tar.gz
```

---

## 指定内容范围

**基本写法：导出指定路径**
`git archive <提交> <路径>`
```bash
# 仅导出 src 目录内容
git archive HEAD src/ -o src.tar
```

---

**基本写法：导出多个路径**
`git archive <提交> <路径1> <路径2>`
```bash
# 导出 src 与 docs 目录
git archive HEAD src/ docs/ -o bundle.tar
```

---

**基本写法：排除指定路径**
`git archive <提交> ':(exclude)<路径>'`
```bash
# 排除 tests 目录
git archive HEAD ':(exclude)tests/' -o release.tar
```

---

**基本写法：排除多个路径**
`git archive <提交> ':(exclude)<路径1>' ':(exclude)<路径2>'`
```bash
# 同时排除 tests 与 node_modules
git archive HEAD ':(exclude)tests/' ':(exclude)node_modules/' -o release.tar
```

---

## 添加前缀目录

**基本写法：导出时添加统一前缀**
`git archive --prefix=<前缀>/ <提交>`
```bash
# 所有文件前添加 project-v1.0/ 目录
git archive --prefix=project-v1.0/ HEAD -o release.tar.gz
```

---

**基本写法：路径级别前缀**
`git archive --prefix=<前缀> <提交> <路径>`
```bash
# 将 src 内容放到 release/src/ 下
git archive --prefix=release/ HEAD src/ -o bundle.tar
```

---

## 指定分支标签

**基本写法：导出指定标签版本**
`git archive <标签> -o <文件>`
```bash
# 导出 v1.2.0 标签版本
git archive v1.2.0 -o release-1.2.0.tar.gz
```

---

**基本写法：导出指定分支**
`git archive <分支> -o <文件>`
```bash
# 导出 release 分支内容
git archive release -o release.tar
```

---

**基本写法：导出某次提交**
`git archive <提交哈希> -o <文件>`
```bash
# 导出指定提交的快照
git archive abc1234 -o snapshot.tar
```

---

## 提交信息

**基本写法：将提交信息加入归档**
`git archive --format=tar <提交> | tar -O -xf - <文件>`
```bash
# 从归档中提取特定文件内容
git archive --format=tar HEAD | tar -O -xf - README.md
```

---

**基本写法：附加版本说明**
`git archive --add-file <文件> <提交>`
```bash
# 归档时追加本地文件
git archive --add-file VERSION.txt HEAD -o release.tar
```

---

## 压缩选项

**基本写法：指定压缩级别**
`git archive --format=tar.gz -<级别> <提交>`
```bash
# 使用最大压缩级别
git archive --format=tar.gz -9 HEAD -o release.tar.gz
```

---

**基本写法：输出到标准输出**
`git archive <提交>`
```bash
# 直接输出到 stdout 供管道使用
git archive HEAD | tar -x -C /tmp/release
```

---

## 远程仓库归档

**基本写法：从远程仓库归档**
`git archive --remote=<仓库URL> <分支>`
```bash
# 直接从远程仓库归档（需服务器支持）
git archive --remote=https://git.example.com/repo.git HEAD -o remote.tar
```

---

**基本写法：远程归档带前缀**
`git archive --remote=<URL> --prefix=<前缀>/ <分支>`
```bash
# 远程归档并添加前缀
git archive --remote=https://git.example.com/repo.git --prefix=repo/ main -o repo.tar
```

---

## 实用场景

**基本写法：导出干净的发布包**
`git archive --format=tar.gz --prefix=<项目>-<版本>/ <标签> -o <文件>`
```bash
# 制作标准源码发布包
git archive --format=tar.gz --prefix=myapp-1.0.0/ v1.0.0 -o myapp-1.0.0.tar.gz
```

---

**基本写法：导出并校验**
`git archive <提交> -o <文件> && sha256sum <文件>`
```bash
# 归档并生成校验和
git archive v1.0.0 -o release.tar.gz && sha256sum release.tar.gz
```

---

**基本写法：归档排除 git 元数据**
`git archive <提交> | tar -t`
```bash
# 列出归档内容验证
git archive HEAD | tar -t
```



<!-- ============ 文档分隔线：003-git/018-GitDescribe.md ============ -->

# Git describe 版本描述

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：描述当前提交**
`git describe`
```bash
# 显示当前 HEAD 距离最近标签的描述
git describe
```

---

**基本写法：描述指定提交**
`git describe <提交>`
```bash
# 描述指定分支最新提交
git describe main
```

---

**基本写法：描述指定标签**
`git describe <标签>`
```bash
# 描述 v1.0.0 标签
git describe v1.0.0
```

---

## 标签选择

**基本写法：仅使用带注释的标签**
`git describe --tags`
```bash
# 包含轻量标签与带注释标签
git describe --tags
```

---

**基本写法：包含所有引用**
`git describe --all`
```bash
# 使用所有引用（含分支）描述
git describe --all
```

---

**基本写法：仅匹配特定模式标签**
`git describe --match "<模式>"`
```bash
# 仅匹配 v 开头的版本标签
git describe --match "v*"
```

---

**基本写法：排除特定模式标签**
`git describe --exclude "<模式>"`
```bash
# 排除 alpha 与 beta 标签
git describe --exclude "*alpha*" --exclude "*beta*"
```

---

## 输出格式

**基本写法：仅显示最近标签**
`git describe --abbrev=0`
```bash
# 仅输出最近标签名，不显示提交距离
git describe --abbrev=0
```

---

**基本写法：指定哈希缩写长度**
`git describe --abbrev=<长度>`
```bash
# 输出 7 位提交哈希缩写
git describe --abbrev=7
```

---

**基本写法：始终输出长格式**
`git describe --long`
```bash
# 始终输出 标签-距离-哈希 完整格式
git describe --long
```

---

**基本写法：自定义输出格式**
`git describe --format="<格式>"`
```bash
# 自定义描述输出格式
git describe --format="%d-%h"
```

---

## 提交距离控制

**基本写法：限制标签查找深度**
`git describe --max-count=<数量>`
```bash
# 最多向前查找 100 个标签
git describe --max-count=100
```

---

**基本写法：按提交数量限制**
`git describe --candidates=<数量>`
```bash
# 仅在最近 5 个候选中查找标签
git describe --candidates=5
```

---

**基本写法：找不到标签时回退到哈希**
`git describe --always`
```bash
# 无标签时输出短哈希而非报错
git describe --always
```

---

## 与 dirty 状态结合

**基本写法：附加工作区状态**
`git describe --dirty`
```bash
# 工作区有改动时附加 -dirty
git describe --dirty
```

---

**基本写法：附加详细 dirty 标记**
`git describe --dirty --broken`
```bash
# 包含工作区改动与损坏对象标记
git describe --dirty --broken
```

---

**基本写法：自定义 dirty 标记**
`git describe --dirty-mark=<标记>`
```bash
# 自定义脏标记字符串
git describe --dirty-mark="-modified"
```

---

## 实用场景

**基本写法：生成版本号字符串**
`git describe --tags --always --dirty`
```bash
# 用于构建系统的版本号
git describe --tags --always --dirty
```

---

**基本写法：写入版本文件**
`git describe --tags > VERSION`
```bash
# 将版本描述写入文件供程序读取
git describe --tags > VERSION
```

---

**基本写法：组合提交信息**
`git describe --long --dirty --tags`
```bash
# 完整版本描述用于发布报告
git describe --long --dirty --tags
```

---

**基本写法：在 CI 中获取版本**
`git describe --tags --abbrev=0`
```bash
# 获取最近版本标签用于构建产物命名
git describe --tags --abbrev=0
```

---

## 多标签场景

**基本写法：优先匹配主版本**
`git describe --match "v[0-9]*" --match "release-*"`
```bash
# 同时匹配多种版本模式
git describe --match "v[0-9]*" --match "release-*"
```

---

**基本写法：忽略特定前缀标签**
`git describe --exclude "nightly-*"`
```bash
# 排除每日构建标签
git describe --exclude "nightly-*"
```



<!-- ============ 文档分隔线：003-git/019-GitShortlog.md ============ -->

# Git shortlog 提交摘要

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：查看提交者统计**
`git shortlog`
```bash
# 按作者分组显示提交数量
git shortlog
```

---

**基本写法：限定提交范围**
`git shortlog <提交范围>`
```bash
# 仅统计最近 30 天的提交
git shortlog --since="30 days"
```

---

**基本写法：统计指定分支**
`git shortlog <分支>`
```bash
# 统计 main 分支提交
git shortlog main
```

---

**基本写法：从某版本起统计**
`git shortlog <标签>..HEAD`
```bash
# 统计 v1.0.0 之后的所有提交
git shortlog v1.0.0..HEAD
```

---

## 输出格式

**基本写法：按数量排序**
`git shortlog -n`
```bash
# 提交数量多的作者排在前面
git shortlog -n
```

---

**基本写法：按作者排序**
`git shortlog -s`
```bash
# 仅显示提交数量与作者名
git shortlog -s
```

---

**基本写法：组合数量与姓名排序**
`git shortlog -s -n`
```bash
# 按提交数量降序显示摘要
git shortlog -s -n
```

---

**基本写法：显示完整提交信息**
`git shortlog -e`
```bash
# 同时显示作者邮箱
git shortlog -e
```

---

## 分组方式

**基本写法：按作者分组**
`git shortlog --group=author`
```bash
# 默认按作者名分组
git shortlog --group=author
```

---

**基本写法：按邮箱分组**
`git shortlog --group=email`
```bash
# 按邮箱分组避免同名不同人
git shortlog --group=email
```

---

**基本写法：按提交者分组**
`git shortlog --group=committer`
```bash
# 按提交者而非作者分组
git shortlog --group=committer
```

---

**基本写法：多分组聚合**
`git shortlog --group=author --group=email`
```bash
# 同时按作者与邮箱分组
git shortlog --group=author --group=email
```

---

## 格式化输出

**基本写法：自定义行格式**
`git shortlog --format="<格式>"`
```bash
# 自定义每条提交的显示格式
git shortlog --format="%h %s"
```

---

**基本写法：只显示提交主题**
`git shortlog -w`
```bash
# 包装长行输出更整齐
git shortlog -w
```

---

**基本写法：指定换行宽度**
`git shortlog -w<宽度>`
```bash
# 设置 80 列换行
git shortlog -w80
```

---

## 过滤范围

**基本写法：按时间过滤**
`git shortlog --since="<时间>" --until="<时间>"`
```bash
# 统计 2024 年的提交
git shortlog --since="2024-01-01" --until="2024-12-31"
```

---

**基本写法：按作者过滤**
`git shortlog --author="<关键字>"`
```bash
# 仅统计 Alice 的提交
git shortlog --author="Alice"
```

---

**基本写法：按提交信息过滤**
`git shortlog --grep="<关键字>"`
```bash
# 仅统计 fix 类提交
git shortlog --grep="^fix:"
```

---

**基本写法：按路径过滤**
`git shortlog -- <路径>`
```bash
# 仅统计 src 目录的提交
git shortlog -- src/
```

---

## 报告生成

**基本写法：生成发布说明**
`git shortlog -s -n <标签>..HEAD > CHANGELOG.txt`
```bash
# 生成自上版本以来的贡献者列表
git shortlog -s -n v1.0.0..HEAD > CHANGELOG.txt
```

---

**基本写法：Markdown 格式输出**
`git shortlog -s -n --format="* %s"`
```bash
# 输出 Markdown 列表格式的变更摘要
git shortlog --format="* %s" v1.0.0..HEAD
```

---

**基本写法：按作者生成详细日志**
`git shortlog -e -n v1.0.0..HEAD`
```bash
# 按作者分组生成发布日志
git shortlog -e -n v1.0.0..HEAD
```

---

## 统计行数（结合其他命令）

**基本写法：统计每个作者提交数**
`git shortlog -s -n --all`
```bash
# 全分支统计作者提交数
git shortlog -s -n --all
```

---

**基本写法：组合 numstat 统计行数**
`git log --author="<作者>" --numstat --pretty=tformat: | awk '{add+=$1; del+=$2} END {print add, del}'`
```bash
# 统计某作者新增与删除的行数
git log --author="Alice" --numstat --pretty=tformat: | awk '{add+=$1; del+=$2} END {print add, del}'
```

---

## 多仓库合并统计

**基本写法：跨仓库汇总贡献**
`git log --all --pretty=format:"%an" | sort | uniq -c | sort -nr`
```bash
# 用基础命令统计所有引用的作者
git log --all --pretty=format:"%an" | sort | uniq -c | sort -nr
```

---

**基本写法：导出报告供汇总**
`git shortlog -sne --all > contributors.txt`
```bash
# 导出全分支贡献者列表
git shortlog -sne --all > contributors.txt
```



<!-- ============ 文档分隔线：003-git/020-GitSubtree.md ============ -->

# Git subtree 子树管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 添加子树

**基本写法：添加远程仓库为子树**
`git subtree add --prefix=<路径> <仓库URL> <分支>`
```bash
# 将外部仓库添加到 lib/utils 目录
git subtree add --prefix=lib/utils https://github.com/org/utils.git main
```

---

**基本写法：指定子目录前缀**
`git subtree add --prefix=<路径> <仓库URL> <分支> --squash`
```bash
# 仅合并子树最新提交（压缩历史）
git subtree add --prefix=lib/utils https://github.com/org/utils.git main --squash
```

---

**基本写法：从本地路径添加子树**
`git subtree add --prefix=<路径> <本地路径> <分支>`
```bash
# 从本地仓库添加子树
git subtree add --prefix=lib/local ../local-repo main
```

---

## 拉取子树更新

**基本写法：拉取子树最新变更**
`git subtree pull --prefix=<路径> <仓库URL> <分支>`
```bash
# 拉取子树仓库 main 分支的更新
git subtree pull --prefix=lib/utils https://github.com/org/utils.git main
```

---

**基本写法：压缩方式拉取**
`git subtree pull --prefix=<路径> <仓库URL> <分支> --squash`
```bash
# 拉取并压缩为单次提交
git subtree pull --prefix=lib/utils https://github.com/org/utils.git main --squash
```

---

**基本写法：使用 rebase 方式拉取**
`git subtree pull --prefix=<路径> -X <策略> <仓库URL> <分支>`
```bash
# 拉取时优先采用子树内容
git subtree pull --prefix=lib/utils -X theirs https://github.com/org/utils.git main
```

---

## 推送子树变更

**基本写法：推送子树变更到上游**
`git subtree push --prefix=<路径> <仓库URL> <分支>`
```bash
# 推送子树变更回原仓库
git subtree push --prefix=lib/utils https://github.com/org/utils.git feature-update
```

---

**基本写法：拆分后推送**
`git subtree split --prefix=<路径> --branch <新分支>`
```bash
# 将子树拆分为独立分支
git subtree split --prefix=lib/utils --branch utils-sync
```

---

**基本写法：从拆分分支推送**
`git push <仓库URL> <本地分支>:<远程分支>`
```bash
# 推送拆分分支到远程
git push https://github.com/org/utils.git utils-sync:main
```

---

## 拆分历史

**基本写法：拆分子树为新分支**
`git subtree split --prefix=<路径> --branch <分支名>`
```bash
# 将 src 目录历史拆分到新分支
git subtree split --prefix=src --branch src-history
```

---

**基本写法：拆分到指定提交**
`git subtree split --prefix=<路径> --branch <分支> <提交>`
```bash
# 从指定提交开始拆分
git subtree split --prefix=src --branch src-history v1.0.0
```

---

**基本写法：拆分时重新生成历史**
`git subtree split --prefix=<路径> --rejoin`
```bash
# 拆分后标记主分支已同步
git subtree split --prefix=src --rejoin
```

---

## 合并策略

**基本写法：使用 subtree 合并策略**
`git merge -X subtree=<路径> <分支>`
```bash
# 用 subtree 策略合并子分支
git merge -X subtree=lib/utils utils-branch
```

---

**基本写法：以 ours 优先合并**
`git merge -X subtree=<路径> -X ours <分支>`
```bash
# 冲突时优先保留主仓库内容
git merge -X subtree=lib/utils -X ours utils-branch
```

---

## 初始化配置

**基本写法：为子树添加远程别名**
`git remote add <别名> <仓库URL>`
```bash
# 为子树来源仓库添加远程别名
git remote add utils https://github.com/org/utils.git
```

---

**基本写法：使用别名进行拉取**
`git subtree pull --prefix=<路径> <别名> <分支>`
```bash
# 通过别名简化拉取命令
git subtree pull --prefix=lib/utils utils main
```

---

**基本写法：使用别名进行推送**
`git subtree push --prefix=<路径> <别名> <分支>`
```bash
# 通过别名推送变更
git subtree push --prefix=lib/utils utils feature
```

---

## 与 submodule 对比

**基本写法：subtree 内容直接存放于主仓库**
`git subtree add --prefix=<路径> <URL> <分支>`
```bash
# 子目录文件直接属于主仓库历史
git subtree add --prefix=lib/utils https://github.com/org/utils.git main
```

---

**基本写法：submodule 仅存引用**
`git submodule add <URL> <路径>`
```bash
# submodule 仅记录子仓库引用（对比场景）
git submodule add https://github.com/org/utils.git lib/utils
```

---

## 常用查询

**基本写法：查看子树目录内容**
`git log --oneline --graph -- <路径>`
```bash
# 查看子树目录的所有提交
git log --oneline --graph -- lib/utils
```

---

**基本写法：查看子树来源**
`git remote -v`
```bash
# 查看配置的远程仓库别名
git remote -v
```

---

## 提交子树变更

**基本写法：在子树目录修改后提交**
`git commit -am "<消息>"`
```bash
# 修改 lib/utils 后直接在主仓库提交
git commit -am "update utils library"
```

---

**基本写法：仅提交子树目录**
`git commit -- <路径> -m "<消息>"`
```bash
# 仅提交子树目录变更
git commit -- lib/utils -m "feat: update utils"
```



<!-- ============ 文档分隔线：003-git/021-GitBlame.md ============ -->

# Git blame 与 annotate

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：查看文件每行最后修改者**
`git blame <文件>`
```bash
# 显示 src/main.py 每行的作者与提交
git blame src/main.py
```

---

**基本写法：限定行范围**
`git blame -L <起始>,<结束> <文件>`
```bash
# 仅查看第 10 到 30 行的归属
git blame -L 10,30 src/main.py
```

---

**基本写法：限定起始行到文件末尾**
`git blame -L <起始> <文件>`
```bash
# 从第 50 行到文件末尾
git blame -L 50 src/main.py
```

---

## 提交范围控制

**基本写法：从指定提交开始追溯**
`git blame <提交> -- <文件>`
```bash
# 从 v1.0.0 标签开始追溯
git blame v1.0.0 -- src/main.py
```

---

**基本写法：限定追溯范围**
`git blame <起点>..<终点> -- <文件>`
```bash
# 仅在指定提交范围内追溯
git blame v1.0.0..HEAD -- src/main.py
```

---

**基本写法：查看更早版本**
`git blame <提交>^ -- <文件>`
```bash
# 查看上一次提交时的归属
git blame HEAD^ -- src/main.py
```

---

## 输出格式

**基本写法：显示完整哈希**
`git blame -l <文件>`
```bash
# 显示 40 位完整提交哈希
git blame -l src/main.py
```

---

**基本写法：显示作者邮箱**
`git blame -e <文件>`
```bash
# 用邮箱代替作者姓名
git blame -e src/main.py
```

---

**基本写法：显示提交时间**
`git blame -t <文件>`
```bash
# 显示原始时间戳而非日期
git blame -t src/main.py
```

---

**基本写法：空提交敏感模式**
`git blame -w <文件>`
```bash
# 忽略空白变更的提交
git blame -w src/main.py
```

---

## 行追踪

**基本写法：追踪行移动**
`git blame -M <文件>`
```bash
# 检测同一文件内的行移动
git blame -M src/main.py
```

---

**基本写法：检测跨文件复制移动**
`git blame -C <文件>`
```bash
# 检测从其他文件复制的行
git blame -C src/main.py
```

---

**基本写法：全仓库范围检测复制**
`git blame -CCC <文件>`
```bash
# 在所有提交中检测复制来源
git blame -CCC src/main.py
```

---

**基本写法：指定移动检测阈值**
`git blame -M<数量> <文件>`
```bash
# 设置移动检测的最小字符数
git blame -M20 src/main.py
```

---

## 增量查看

**基本写法：限制每次显示行数**
`git blame --incremental <文件>`
```bash
# 增量输出便于程序解析
git blame --incremental src/main.py
```

---

**基本写法：显示边界提交**
`git blame --root <文件>`
```bash
# 将根提交也标记为边界
git blame --root src/main.py
```

---

## annotate 命令

**基本写法：使用 annotate（blame 别名）**
`git annotate <文件>`
```bash
# annotate 等价于 blame
git annotate src/main.py
```

---

**基本写法：annotate 限定范围**
`git annotate -L <起始>,<结束> <文件>`
```bash
# annotate 限定行范围
git annotate -L 1,20 src/main.py
```

---

## 实用场景

**基本写法：定位 bug 引入提交**
`git blame -L <行>,<行> <文件>`
```bash
# 定位某行代码的最后修改提交
git blame -L 42,42 src/main.py
```

---

**基本写法：查看某行完整提交信息**
`git show <提交>`
```bash
# 查看 blame 找到的提交详情
git show abc1234
```

---

**基本写法：忽略某些提交**
`git blame --ignore-rev <提交> <文件>`
```bash
# 跳过指定提交（如格式化提交）
git blame --ignore-rev abc1234 src/main.py
```

---

**基本写法：通过文件配置忽略列表**
`git blame --ignore-revs-file <文件> <目标文件>`
```bash
# 从文件读取要忽略的提交列表
git blame --ignore-revs-file .git-blame-ignore revs.txt src/main.py
```

---

**基本写法：配置默认忽略文件**
`git config blame.ignoreRevsFile <文件>`
```bash
# 配置项目默认的 blame 忽略文件
git config blame.ignoreRevsFile .git-blame-ignore-revs
```

---

**基本写法：按颜色高亮输出**
`git blame --color-by-age <文件>`
```bash
# 按提交年龄着色显示
git blame --color-by-age src/main.py
```

---

**基本写法：按作者着色**
`git blame --color-lines <文件>`
```bash
# 同一作者的行用相同颜色
git blame --color-lines src/main.py
```

---

## 与其他命令配合

**基本写法：blame 找到提交后查看历史**
`git log -p <提交> -- <文件>`
```bash
# 查看指定提交对该文件的所有改动
git log -p abc1234 -- src/main.py
```

---

**基本写法：定位后用 bisect 深入**
`git bisect start && git bisect bad HEAD && git bisect good <提交>`
```bash
# 由 blame 结果启动二分查找
git bisect start && git bisect bad HEAD && git bisect good abc1234
```



<!-- ============ 文档分隔线：003-git/022-GitSparseCheckout.md ============ -->

# Git sparse-checkout 与 partial clone

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## sparse-checkout 启用

**基本写法：初始化稀疏检出**
`git sparse-checkout init`
```bash
# 启用稀疏检出（默认仅根目录文件）
git sparse-checkout init
```

---

**基本写法：启用锥形模式**
`git sparse-checkout init --cone`
```bash
# 启用推荐的锥形模式（目录级匹配）
git sparse-checkout init --cone
```

---

**基本写法：启用模式模式**
`git sparse-checkout init --no-cone`
```bash
# 启用完整模式匹配（支持通配符）
git sparse-checkout init --no-cone
```

---

## 设置检出路径

**基本写法：设置需要检出的目录**
`git sparse-checkout set <路径1> <路径2>`
```bash
# 仅检出 src 与 docs 目录
git sparse-checkout set src docs
```

---

**基本写法：从标准输入读取路径**
`git sparse-checkout set --stdin < <文件>`
```bash
# 从文件读取路径列表
git sparse-checkout set --stdin < paths.txt
```

---

**基本写法：追加检出目录**
`git sparse-checkout add <路径>`
```bash
# 在已有基础上添加 tests 目录
git sparse-checkout add tests
```

---

**基本写法：重新应用稀疏规则**
`git sparse-checkout reapply`
```bash
# 修改规则后重新应用
git sparse-checkout reapply
```

---

## 查看与管理

**基本写法：查看当前检出规则**
`git sparse-checkout list`
```bash
# 列出当前所有稀疏检出路径
git sparse-checkout list
```

---

**基本写法：检查路径是否匹配**
`git sparse-checkout check-rules <路径>`
```bash
# 检查某路径是否会被检出
git sparse-checkout check-rules src/api/users.ts
```

---

**基本写法：禁用稀疏检出**
`git sparse-checkout disable`
```bash
# 关闭稀疏检出恢复完整工作区
git sparse-checkout disable
```

---

## cone 模式规则

**基本写法：添加根目录文件**
`git sparse-checkout set "/*"`
```bash
# 锥形模式下检出所有根目录文件
git sparse-checkout set "/*"
```

---

**基本写法：递归检出子目录**
`git sparse-checkout set src/`
```bash
# 检出 src 目录及其全部子目录
git sparse-checkout set src/
```

---

**基本写法：多层目录匹配**
`git sparse-checkout set src/api src/shared`
```bash
# 同时检出多个顶层子目录
git sparse-checkout set src/api src/shared
```

---

## 非 cone 模式规则

**基本写法：使用通配符匹配**
`git sparse-checkout set "/*.md"`
```bash
# 仅检出根目录 markdown 文件
git sparse-checkout set "/*.md"
```

---

**基本写法：排除某些路径**
`git sparse-checkout set "src/*" "!src/legacy/*"`
```bash
# 检出 src 但排除 legacy 子目录
git sparse-checkout set "src/*" "!src/legacy/*"
```

---

**基本写法：母目录与子目录同时配置**
`git sparse-checkout set "src/" "src/legacy/file.ts"`
```bash
# 检出 src 目录但只保留 legacy 中一个文件
git sparse-checkout set "src/" "src/legacy/file.ts"
```

---

## partial clone 部分克隆

**基本写法：克隆时跳过所有 blob**
`git clone --filter=blob:none <仓库URL>`
```bash
# 仅克隆提交历史，blob 按需获取
git clone --filter=blob:none https://github.com/org/repo.git
```

---

**基本写法：按大小过滤 blob**
`git clone --filter=blob:limit=<大小> <仓库URL>`
```bash
# 跳过大于 1MB 的 blob
git clone --filter=blob:limit=1m https://github.com/org/repo.git
```

---

**基本写法：仅克隆目录树**
`git clone --filter=tree:0 <仓库URL>`
```bash
# 仅克隆提交与目录结构
git clone --filter=tree:0 https://github.com/org/repo.git
```

---

**基本写法：仅克隆指定分支**
`git clone --branch <分支> --single-branch <仓库URL>`
```bash
# 仅克隆 main 分支历史
git clone --branch main --single-branch https://github.com/org/repo.git
```

---

## 组合使用

**基本写法：稀疏检出加部分克隆**
`git clone --filter=blob:none --sparse <仓库URL>`
```bash
# 同时启用部分克隆与稀疏检出
git clone --filter=blob:none --sparse https://github.com/org/repo.git
```

---

**基本写法：克隆后配置稀疏检出**
`git sparse-checkout set <路径>`
```bash
# 进入仓库后设置检出路径
git sparse-checkout set src/api
```

---

**基本写法：将现有仓库转为部分克隆**
`git remote set-origin --filter=blob:none origin`
```bash
# 修改远程配置启用过滤（需新克隆才生效）
git config remote.origin.partialclonefilter blob:none
```

---

## 浅克隆对比

**基本写法：浅克隆指定深度**
`git clone --depth=<深度> <仓库URL>`
```bash
# 仅克隆最近 10 次提交
git clone --depth=10 https://github.com/org/repo.git
```

---

**基本写法：浅克隆指定时间**
`git clone --shallow-since=<日期> <仓库URL>`
```bash
# 仅克隆 2024 年以来的提交
git clone --shallow-since=2024-01-01 https://github.com/org/repo.git
```

---

**基本写法：解除浅克隆**
`git fetch --unshallow`
```bash
# 拉取全部历史转为完整仓库
git fetch --unshallow
```

---

## 按需获取对象

**基本写法：手动获取缺失 blob**
`git fetch origin <路径>`
```bash
# 按需拉取指定路径的 blob
git fetch origin src/api/users.ts
```

---

**基本写法：批量获取某目录**
`git sparse-checkout add <路径>`
```bash
# 添加目录触发对象获取
git sparse-checkout add src/shared
```

---

**基本写法：检查缺失对象**
`git fsck --connectivity-only`
```bash
# 检查仓库对象连通性
git fsck --connectivity-only
```

---

## 配置与优化

**基本写法：配置部分克隆过滤**
`git config remote.origin.partialclonefilter <过滤>`
```bash
# 设置远程仓库部分克隆过滤规则
git config remote.origin.partialclonefilter blob:none
```

---

**基本写法：启用按需获取**
`git config remote.origin.promisor true`
```bash
# 标记远程为 promisor 允许按需获取
git config remote.origin.promisor true
```

---

**基本写法：查看 sparse 配置**
`git config --get-all core.sparseCheckout`
```bash
# 查看稀疏检出是否启用
git config --get-all core.sparseCheckout
```

---

**基本写法：查看 sparseCheckoutCone**
`git config core.sparseCheckoutCone`
```bash
# 查看是否启用锥形模式
git config core.sparseCheckoutCone
```



<!-- ============ 文档分隔线：003-git/023-GitHooks.md ============ -->

# Git hooks 钩子实战

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 钩子基础

**基本写法：查看可用钩子模板**
`ls .git/hooks`
```bash
# 列出当前仓库的钩子目录
ls .git/hooks
```

---

**基本写法：启用钩子**
`mv .git/hooks/<钩子名>.sample .git/hooks/<钩子名>`
```bash
# 移除 sample 后缀以激活钩子
mv .git/hooks/pre-commit.sample .git/hooks/pre-commit
```

---

**基本写法：使钩子可执行**
`chmod +x .git/hooks/<钩子名>`
```bash
# 赋予钩子脚本执行权限
chmod +x .git/hooks/pre-commit
```

---

**基本写法：查看全局钩子模板路径**
`git config --global core.hooksPath <路径>`
```bash
# 设置全局钩子目录
git config --global core.hooksPath ~/.git-hooks
```

---

**基本写法：本地仓库指定钩子路径**
`git config core.hooksPath <路径>`
```bash
# 为当前仓库指定自定义钩子目录
git config core.hooksPath .githooks
```

---

## 客户端钩子

**基本写法：pre-commit 钩子**
`.git/hooks/pre-commit`
```bash
# 在 git commit 前执行检查
#!/bin/sh
npm run lint
```

---

**基本写法：prepare-commit-msg 钩子**
`.git/hooks/prepare-commit-msg`
```bash
# 在编辑提交信息前自动填充
#!/bin/sh
echo "# 请按规范填写提交信息" >> "$1"
```

---

**基本写法：commit-msg 钩子**
`.git/hooks/commit-msg`
```bash
# 校验提交信息是否符合规范
#!/bin/sh
grep -qE "^(feat|fix|docs):" "$1" || exit 1
```

---

**基本写法：post-commit 钩子**
`.git/hooks/post-commit`
```bash
# 提交完成后通知
#!/bin/sh
echo "提交完成: $(git rev-parse HEAD)"
```

---

**基本写法：pre-push 钩子**
`.git/hooks/pre-push`
```bash
# 推送前执行测试
#!/bin/sh
npm test || exit 1
```

---

**基本写法：pre-rebase 钩子**
`.git/hooks/pre-rebase`
```bash
# 变基前检查
#!/bin/sh
echo "即将执行 rebase 操作" >&2
```

---

**基本写法：post-merge 钩子**
`.git/hooks/post-merge`
```bash
# 合并完成后安装依赖
#!/bin/sh
npm install
```

---

**基本写法：post-checkout 钩子**
`.git/hooks/post-checkout`
```bash
# 切换分支后切换依赖版本
#!/bin/sh
nvm use
```

---

## 服务端钩子

**基本写法：pre-receive 钩子**
`.git/hooks/pre-receive`
```bash
# 接收推送前校验所有引用
#!/bin/sh
while read oldrev newrev refname; do
  echo "推送引用: $refname"
done
```

---

**基本写法：update 针对单引用钩子**
`.git/hooks/update`
```bash
# 每个引用更新前调用
#!/bin/sh
refname="$1"
oldrev="$2"
newrev="$3"
```

---

**基本写法：post-receive 钩子**
`.git/hooks/post-receive`
```bash
# 接收推送后触发部署
#!/bin/sh
git --work-tree=/var/www --git-dir=/repo checkout -f
```

---

## 钩子脚本常用变量

**基本写法：在 pre-commit 中获取暂存文件**
`git diff --cached --name-only --diff-filter=ACM`
```bash
# 获取已暂存的修改文件列表
files=$(git diff --cached --name-only --diff-filter=ACM)
```

---

**基本写法：在 commit-msg 中读取提交信息**
`cat "$1"`
```bash
# 读取提交信息文件内容
msg=$(cat "$1")
```

---

**基本写法：在 pre-push 中读取推送信息**
`read <本地引用> <本地哈希> <远程引用> <远程哈希>`
```bash
# 从 stdin 读取推送引用信息
while read local_ref local_oid remote_ref remote_oid; do
  echo "$local_ref -> $remote_ref"
done
```

---

## Husky 等工具管理钩子

**基本写法：安装 Husky**
`npx husky init`
```bash
# 初始化 Husky 钩子管理
npx husky init
```

---

**基本写法：添加 Husky 钩子**
`npx husky add .husky/<钩子名> "<命令>"`
```bash
# 添加 pre-commit 钩子执行 lint
npx husky add .husky/pre-commit "npm run lint"
```

---

**基本写法：跳过钩子执行**
`git commit --no-verify`
```bash
# 提交时跳过 pre-commit 与 commit-msg 钩子
git commit --no-verify -m "msg"
```

---

**基本写法：推送时跳过钩子**
`git push --no-verify`
```bash
# 推送时跳过 pre-push 钩子
git push --no-verify
```

---

## 钩子实战示例

**基本写法：阻止提交到 main 分支**
`.git/hooks/pre-commit`
```bash
# 阻止直接在 main 分支提交
#!/bin/sh
branch=$(git rev-parse --abbrev-ref HEAD)
[ "$branch" = "main" ] && echo "禁止直接提交到 main" && exit 1
```

---

**基本写法：检查提交信息格式**
`.git/hooks/commit-msg`
```bash
# 校验 Conventional Commits 格式
#!/bin/sh
if ! grep -qE "^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+" "$1"; then
  echo "提交信息不符合规范"
  exit 1
fi
```

---

**基本写法：阻止提交大文件**
`.git/hooks/pre-commit`
```bash
# 阻止提交超过 5MB 的文件
#!/bin/sh
max_size=5242880
for file in $(git diff --cached --name-only); do
  size=$(git cat-file -s :"$file" 2>/dev/null || echo 0)
  [ "$size" -gt "$max_size" ] && echo "文件过大: $file" && exit 1
done
```

---

**基本写法：自动格式化代码**
`.git/hooks/pre-commit`
```bash
# 暂存前自动格式化
#!/bin/sh
files=$(git diff --cached --name-only --diff-filter=ACM | grep "\.js$")
echo "$files" | xargs -r prettier --write
echo "$files" | xargs -r git add
```

---

**基本写法：同步子模块**
`.git/hooks/post-checkout`
```bash
# 切换分支后同步子模块
#!/bin/sh
git submodule update --init --recursive
```

---

## 团队共享钩子

**基本写法：将钩子纳入版本控制**
`git config core.hooksPath .githooks`
```bash
# 设置仓库共享钩子目录
git config core.hooksPath .githooks
```

---

**基本写法：首次克隆后启用钩子**
`chmod +x .githooks/*`
```bash
# 克隆后赋予钩子可执行权限
chmod +x .githooks/*
```

---

**基本写法：在 README 中提示**
`cat README.md`
```bash
# 文档中说明启用共享钩子的步骤
# 执行: git config core.hooksPath .githooks && chmod +x .githooks/*
```

---

## 调试与排错

**基本写法：手动测试钩子**
`sh .git/hooks/pre-commit`
```bash
# 直接执行钩子脚本测试
sh .git/hooks/pre-commit
```

---

**基本写法：输出调试信息**
`echo "<消息>" >&2`
```bash
# 在钩子中输出到标准错误
echo "调试: 当前分支 $(git branch --show-current)" >&2
```

---

**基本写法：临时禁用所有钩子**
`git -c core.hooksPath=/dev/null <命令>`
```bash
# 单次命令跳过所有钩子
git -c core.hooksPath=/dev/null commit -m "msg"
```



<!-- ============ 文档分隔线：003-git/024-GitLFS.md ============ -->

# Git LFS 大文件存储

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 安装与初始化

**基本写法：安装 Git LFS**
`git lfs install`
```bash
# 在当前用户范围启用 Git LFS
git lfs install
```

---

**基本写法：在仓库中初始化 LFS**
`git lfs install --local`
```bash
# 仅在当前仓库启用 LFS
git lfs install --local
```

---

**基本写法：查看 LFS 版本**
`git lfs version`
```bash
# 输出当前 Git LFS 版本号
git lfs version
```

---

## 跟踪大文件

**基本写法：添加 LFS 跟踪规则**
`git lfs track "<模式>"`
```bash
# 跟踪所有 mp4 视频文件
git lfs track "*.mp4"
```

---

**基本写法：跟踪指定目录**
`git lfs track "<目录>/**"`
```bash
# 跟踪 assets 目录下所有文件
git lfs track "assets/**"
```

---

**基本写法：查看跟踪规则**
`git lfs track`
```bash
# 列出当前所有 LFS 跟踪规则
git lfs track
```

---

**基本写法：移除跟踪规则**
`git lfs untrack "<模式>"`
```bash
# 移除某类文件的 LFS 跟踪
git lfs untrack "*.mp4"
```

---

**基本写法：提交 .gitattributes**
`git add .gitattributes && git commit -m "<消息>"`
```bash
# 跟踪规则变更必须提交
git add .gitattributes && git commit -m "chore: configure LFS tracking"
```

---

## 操作 LFS 文件

**基本写法：添加大文件**
`git add <文件> && git commit -m "<消息>"`
```bash
# 添加大文件到 LFS 跟踪
git add video.mp4 && git commit -m "feat: add intro video"
```

---

**基本写法：查看 LFS 文件列表**
`git lfs ls-files`
```bash
# 列出仓库中所有 LFS 跟踪文件
git lfs ls-files
```

---

**基本写法：查看文件大小信息**
`git lfs ls-files --size`
```bash
# 显示 LFS 文件的实际大小
git lfs ls-files --size
```

---

## 拉取与推送

**基本写法：克隆含 LFS 的仓库**
`git clone <仓库URL>`
```bash
# 克隆时自动拉取 LFS 文件
git clone https://github.com/org/repo.git
```

---

**基本写法：跳过 LFS 内容克隆**
`GIT_LFS_SKIP_SMUDGE=1 git clone <仓库URL>`
```bash
# 仅克隆指针文件不下载大文件内容
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/org/repo.git
```

---

**基本写法：按需下载 LFS 文件**
`git lfs pull`
```bash
# 拉取所有 LFS 跟踪文件内容
git lfs pull
```

---

**基本写法：拉取指定文件**
`git lfs pull --include="<路径>"`
```bash
# 仅拉取指定目录下的 LFS 文件
git lfs pull --include="assets/videos/*"
```

---

**基本写法：推送 LFS 文件**
`git push origin <分支>`
```bash
# 推送时自动上传 LFS 文件
git push origin main
```

---

**基本写法：仅推送 LFS 内容**
`git lfs push origin <分支>`
```bash
# 单独推送 LFS 文件到远程
git lfs push origin main
```

---

**基本写法：推送所有 LFS 对象**
`git lfs push --all origin <分支>`
```bash
# 推送全部历史 LFS 对象
git lfs push --all origin main
```

---

## 检出与切换

**基本写法：检出指定分支的 LFS 文件**
`git lfs checkout`
```bash
# 用 LFS 内容替换工作区指针文件
git lfs checkout
```

---

**基本写法：仅检出指定路径**
`git lfs checkout --include="<路径>"`
```bash
# 仅检出 assets 目录的 LFS 内容
git lfs checkout --include="assets/*"
```

---

**基本写法：切换分支后同步**
`git checkout <分支> && git lfs checkout`
```bash
# 切换分支后重新检出 LFS 文件
git checkout feature && git lfs checkout
```

---

## 历史与迁移

**基本写法：将已有文件转为 LFS**
`git lfs migrate import --include="<模式>"`
```bash
# 将历史中的 mp4 文件迁移到 LFS
git lfs migrate import --include="*.mp4"
```

---

**基本写法：迁移指定分支历史**
`git lfs migrate import --include="<模式>" --include-ref=<分支>`
```bash
# 仅迁移 main 分支的历史文件
git lfs migrate import --include="*.mp4" --include-ref=main
```

---

**基本写法：迁移所有引用**
`git lfs migrate import --include="<模式>" --include-ref=refs/heads/*`
```bash
# 迁移所有分支的历史文件
git lfs migrate import --include="*.mp4" --include-ref=refs/heads/*
```

---

**基本写法：导出 LFS 文件回普通对象**
`git lfs migrate export --include="<模式>"`
```bash
# 取消 LFS 跟踪并还原文件
git lfs migrate export --include="*.mp4"
```

---

## 检查与状态

**基本写法：查看 LFS 状态**
`git lfs status`
```bash
# 显示工作区 LFS 文件状态
git lfs status
```

---

**基本写法：检查 LFS 文件完整性**
`git lfs fsck`
```bash
# 校验 LFS 对象完整性
git lfs fsck
```

---

**基本写法：查看 LFS 日志**
`git lfs logs last`
```bash
# 查看最近一次 LFS 操作日志
git lfs logs last
```

---

**基本写法：列出所有 LFS 对象**
`git lfs ls-files --all`
```bash
# 列出所有历史中的 LFS 文件
git lfs ls-files --all
```

---

## 远程配置

**基本写法：查看 LFS 端点**
`git config -l | grep lfs`
```bash
# 查看 LFS 相关配置
git config -l | grep lfs
```

---

**基本写法：指定 LFS 服务器**
`git config -f .lfsconfig lfs.url <URL>`
```bash
# 配置自定义 LFS 服务器地址
git config -f .lfsconfig lfs.url https://lfs.example.com/org/repo
```

---

**基本写法：跳过 smudge 过滤器**
`git config --local lfs.smudge false`
```bash
# 关闭自动下载 LFS 内容
git config --local lfs.smudge false
```

---

## 锁定文件（防冲突）

**基本写法：锁定 LFS 文件**
`git lfs lock <文件>`
```bash
# 锁定二进制文件防止并发编辑
git lfs lock assets/logo.psd
```

---

**基本写法：查看锁定列表**
`git lfs locks`
```bash
# 列出所有已锁定文件
git lfs locks
```

---

**基本写法：解锁文件**
`git lfs unlock <文件>`
```bash
# 释放文件锁
git lfs unlock assets/logo.psd
```

---

**基本写法：强制解锁**
`git lfs unlock <文件> --force`
```bash
# 强制解锁他人持有的锁
git lfs unlock assets/logo.psd --force
```

---

## 清理与优化

**基本写法：清理无用 LFS 对象**
`git lfs prune`
```bash
# 清理本地未引用的 LFS 对象
git lfs prune
```

---

**基本写法：查看待清理对象**
`git lfs prune --dry-run`
```bash
# 预览将被清理的对象
git lfs prune --dry-run
```

---

**基本写法：强制保留对象**
`git lfs fetch --recent`
```bash
# 拉取最近使用的 LFS 对象
git lfs fetch --recent
```



<!-- ============ 文档分隔线：003-git/025-GitFlowWorkflow.md ============ -->

# Git Flow 工作流

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 分支模型

**基本写法：主分支 main**
`main`
```bash
# 仅存放稳定的发布版本
# 每次合并都打标签
```

---

**基本写法：开发分支 develop**
`develop`
```bash
# 日常集成分支，反映最新开发状态
# feature 分支从此切出
```

---

**基本写法：功能分支 feature**
`feature/<功能名>`
```bash
# 单个功能开发分支
# 完成后合并回 develop
```

---

**基本写法：发布分支 release**
`release/<版本号>`
```bash
# 准备发布版本，仅修复 bug
# 完成后合并到 main 与 develop
```

---

**基本写法：热修分支 hotfix**
`hotfix/<编号>`
```bash
# 基于 main 修复线上问题
# 完成后合并到 main 与 develop
```

---

## git-flow 工具

**基本写法：安装 git-flow**
`apt-get install git-flow`
```bash
# Debian/Ubuntu 安装 git-flow 扩展
apt-get install git-flow
```

---

**基本写法：初始化 git-flow**
`git flow init`
```bash
# 交互式配置各分支命名
git flow init
```

---

**基本写法：非交互式初始化**
`git flow init -d`
```bash
# 使用默认配置初始化
git flow init -d
```

---

## feature 工作流

**基本写法：开始新功能**
`git flow feature start <功能名>`
```bash
# 从 develop 切出新功能分支
git flow feature start login
```

---

**基本写法：发布功能到远程**
`git flow feature publish <功能名>`
```bash
# 将功能分支推送到远程协作
git flow feature publish login
```

---

**基本写法：拉取远程功能分支**
`git flow feature track <功能名>`
```bash
# 跟踪远程已有的功能分支
git flow feature track login
```

---

**基本写法：完成功能**
`git flow feature finish <功能名>`
```bash
# 合并功能分支到 develop 并删除
git flow feature finish login
```

---

**基本写法：完成功能保留分支**
`git flow feature finish -k <功能名>`
```bash
# 合并后保留功能分支
git flow feature finish -k login
```

---

## release 工作流

**基本写法：开始发布分支**
`git flow release start <版本号>`
```bash
# 从 develop 创建发布分支
git flow release start 1.2.0
```

---

**基本写法：发布分支推到远程**
`git flow release publish <版本号>`
```bash
# 推送发布分支供团队协作
git flow release publish 1.2.0
```

---

**基本写法：完成发布**
`git flow release finish <版本号>`
```bash
# 合并到 main 与 develop 并打标签
git flow release finish 1.2.0
```

---

**基本写法：完成发布带推送**
`git flow release finish -p <版本号>`
```bash
# 完成后自动推送 main、develop 与标签
git flow release finish -p 1.2.0
```

---

**基本写法：完成发布带信息**
`git flow release finish -m "<消息>" <版本号>`
```bash
# 为合并提交与标签添加信息
git flow release finish -m "release 1.2.0" 1.2.0
```

---

## hotfix 工作流

**基本写法：开始热修**
`git flow hotfix start <版本号> [<基线>]`
```bash
# 基于 main 创建热修分支
git flow hotfix start 1.2.1
```

---

**基本写法：完成热修**
`git flow hotfix finish <版本号>`
```bash
# 合并到 main 与 develop 并打标签
git flow hotfix finish 1.2.1
```

---

**基本写法：完成热修带推送**
`git flow hotfix finish -p <版本号>`
```bash
# 完成后推送所有相关分支与标签
git flow hotfix finish -p 1.2.1
```

---

## 手动实现 Git Flow

**基本写法：手动创建 feature 分支**
`git checkout -b feature/<功能名> develop`
```bash
# 从 develop 创建功能分支
git checkout -b feature/login develop
```

---

**基本写法：完成 feature 合并**
`git checkout develop && git merge --no-ff feature/<功能名>`
```bash
# 用 --no-ff 保留合并记录
git checkout develop && git merge --no-ff feature/login
```

---

**基本写法：手动创建 release 分支**
`git checkout -b release/<版本号> develop`
```bash
# 从 develop 创建发布分支
git checkout -b release/1.2.0 develop
```

---

**基本写法：完成 release 合并到 main**
`git checkout main && git merge --no-ff release/<版本号>`
```bash
# 发布分支合并到 main
git checkout main && git merge --no-ff release/1.2.0
```

---

**基本写法：打版本标签**
`git tag -a <版本号> -m "<消息>"`
```bash
# 在 main 上打带注释标签
git tag -a v1.2.0 -m "Release 1.2.0"
```

---

**基本写法：release 合并回 develop**
`git checkout develop && git merge --no-ff release/<版本号>`
```bash
# 发布内容同步回 develop
git checkout develop && git merge --no-ff release/1.2.0
```

---

**基本写法：删除已合并分支**
`git branch -d <分支名>`
```bash
# 删除已合并的功能分支
git branch -d feature/login
```

---

## GitHub Flow 简化流程

**基本写法：从 main 切分支**
`git checkout -b <分支名> main`
```bash
# 简化流程仅使用 main 与功能分支
git checkout -b feature/login main
```

---

**基本写法：推送并创建 PR**
`git push -u origin <分支名>`
```bash
# 推送后通过 Pull Request 合并
git push -u origin feature/login
```

---

**基本写法：合并后删除分支**
`git branch -d <分支名> && git push origin --delete <分支名>`
```bash
# 本地与远程同时删除分支
git branch -d feature/login && git push origin --delete feature/login
```

---

## 版本号管理

**基本写法：语义化版本号格式**
`<主版本>.<次版本>.<修订号>`
```bash
# 例如 1.2.3 表示主版本 1 次版本 2 修订 3
```

---

**基本写法：发布标签命名规范**
`v<版本号>`
```bash
# 标签前加 v 表示版本
git tag -a v1.2.0 -m "Release 1.2.0"
```

---

## 与 CI/CD 协同

**基本写法：基于标签触发部署**
`git push origin --tags`
```bash
# 推送标签触发发布流水线
git push origin --tags
```

---

**基本写法：仅 main 触发生产部署**
`git push origin main`
```bash
# 主分支推送触发生产环境部署
git push origin main
```

---

**基本写法：develop 触发测试部署**
`git push origin develop`
```bash
# 开发分支推送触发测试环境部署
git push origin develop
```



<!-- ============ 文档分隔线：003-git/026-CommitMessageConvention.md ============ -->

# Git commit message 规范

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Conventional Commits 基础

**基本写法：标准提交格式**
`<类型>[可选作用域]: <描述>`
```bash
# 规范化提交信息基本结构
feat: 添加用户登录功能
```

---

**基本写法：带作用域的提交**
`<类型>(<作用域>): <描述>`
```bash
# 指定变更影响的模块
feat(auth): 添加 OAuth2 登录
```

---

**基本写法：带破坏性变更标记**
`<类型>!: <描述>`
```bash
# 用 ! 标记不兼容变更
refactor!: 重构用户模型接口
```

---

**基本写法：带作用域的破坏性变更**
`<类型>(<作用域>)!: <描述>`
```bash
# 指定作用域的破坏性变更
feat(api)!: 修改响应数据结构
```

---

## 提交类型

**基本写法：新功能**
`feat: <描述>`
```bash
# 新增功能特性
feat: 添加导出 PDF 功能
```

---

**基本写法：修复 bug**
`fix: <描述>`
```bash
# 修复缺陷
fix: 修正登录跳转错误
```

---

**基本写法：文档变更**
`docs: <描述>`
```bash
# 仅修改文档
docs: 更新 README 安装步骤
```

---

**基本写法：样式调整**
`style: <描述>`
```bash
# 不影响代码逻辑的格式调整
style: 统一缩进为 4 空格
```

---

**基本写法：重构**
`refactor: <描述>`
```bash
# 既不新增功能也不修复 bug 的代码重构
refactor: 抽离用户认证逻辑
```

---

**基本写法：性能优化**
`perf: <描述>`
```bash
# 提升性能的变更
perf: 优化列表查询缓存
```

---

**基本写法：测试相关**
`test: <描述>`
```bash
# 新增或修改测试
test: 补充用户模块单元测试
```

---

**基本写法：构建系统**
`build: <描述>`
```bash
# 修改构建系统或依赖
build: 升级 webpack 到 5.0
```

---

**基本写法：CI 配置**
`ci: <描述>`
```bash
# 修改持续集成配置
ci: 添加自动部署流水线
```

---

**基本写法：杂项**
`chore: <描述>`
```bash
# 其他不修改源码或测试的杂项
chore: 更新 .gitignore
```

---

**基本写法：代码回退**
`revert: <描述>`
```bash
# 回退某次提交
revert: feat: 添加用户登录功能
```

---

## 完整提交信息结构

**基本写法：带正文的提交**
`<类型>: <描述>\n\n<正文>`
```bash
# 标题后空一行再写正文
git commit -m "feat: 添加用户登录功能" -m "实现邮箱密码与 OAuth 两种方式"
```

---

**基本写法：带脚注的提交**
`<类型>: <描述>\n\n<脚注>`
```bash
# 用脚注标记 issue 或破坏性变更
git commit -m "fix: 修正登录超时" -m "Closes #123"
```

---

**基本写法：破坏性变更脚注**
`<类型>: <描述>\n\nBREAKING CHANGE: <说明>`
```bash
# 用脚注详细说明不兼容变更
git commit -m "feat!: 重构 API" -m "BREAKING CHANGE: 返回结构改为统一信封格式"
```

---

**基本写法：关联 issue**
`<类型>: <描述>\n\nCloses #<编号>`
```bash
# 提交时关闭指定 issue
git commit -m "fix: 修正订单计算" -m "Closes #456"
```

---

## 多行提交信息

**基本写法：使用多个 -m 参数**
`git commit -m "<标题>" -m "<正文>"`
```bash
# 多个 -m 自动以空行分隔
git commit -m "feat: 添加导出功能" -m "支持导出为 CSV 与 JSON 格式"
```

---

**基本写法：使用 HEREDOC**
`git commit -F - <<'EOF'`
```bash
# 通过 HEREDOC 传入复杂提交信息
git commit -F - <<'EOF'
feat: 添加导出功能

支持导出为 CSV 与 JSON 格式
Closes #789
EOF
```

---

**基本写法：从文件读取提交信息**
`git commit -F <文件>`
```bash
# 从文件读取完整提交信息
git commit -F commit-msg.txt
```

---

**基本写法：用编辑器撰写**
`git commit`
```bash
# 不带 -m 时打开编辑器撰写
git commit
```

---

## 修改提交信息

**基本写法：修改最近一次提交信息**
`git commit --amend -m "<新消息>"`
```bash
# 修改最近一次提交的描述
git commit --amend -m "feat: 添加导出功能"
```

---

**基本写法：保留原提交信息修改**
`git commit --amend --no-edit`
```bash
# 仅追加文件不变更信息
git commit --amend --no-edit
```

---

**基本写法：修改历史提交信息**
`git rebase -i <提交>^`
```bash
# 交互式 rebase 改写历史
git rebase -i HEAD~3
```

---

## commitizen 工具

**基本写法：安装 commitizen**
`npm install -g commitizen`
```bash
# 全局安装交互式提交工具
npm install -g commitizen
```

---

**基本写法：初始化 conventional 适配器**
`commitizen init cz-conventional-changelog --save-dev`
```bash
# 项目内配置 conventional 适配器
commitizen init cz-conventional-changelog --save-dev
```

---

**基本写法：用 git cz 代替 git commit**
`git cz`
```bash
# 启动交互式提交表单
git cz
```

---

## commitlint 校验

**基本写法：安装 commitlint**
`npm install --save-dev @commitlint/cli @commitlint/config-conventional`
```bash
# 安装 commitlint 与 conventional 配置
npm install --save-dev @commitlint/cli @commitlint/config-conventional
```

---

**基本写法：配置 commitlint**
`echo "module.exports = { extends: ['@commitlint/config-conventional'] };" > commitlint.config.js`
```bash
# 创建 commitlint 配置文件
echo "module.exports = { extends: ['@commitlint/config-conventional'] };" > commitlint.config.js
```

---

**基本写法：校验提交信息**
`echo "<消息>" | commitlint`
```bash
# 校验单条提交信息格式
echo "feat: 添加登录" | commitlint
```

---

**基本写法：从最近提交校验**
`commitlint --from=<提交> --to=<提交>`
```bash
# 校验范围内的所有提交
commitlint --from=HEAD~5 --to=HEAD
```

---

## 自动生成变更日志

**基本写法：安装 standard-version**
`npm install --save-dev standard-version`
```bash
# 安装自动版本与日志工具
npm install --save-dev standard-version
```

---

**基本写法：生成版本与日志**
`npx standard-version`
```bash
# 根据 conventional 提交生成 CHANGELOG
npx standard-version
```

---

**基本写法：指定发布类型**
`npx standard-version --release-as <类型>`
```bash
# 强制发布为主版本/次版本/修订版
npx standard-version --release-as major
```

---

**基本写法：使用 conventional-changelog**
`npx conventional-changelog -p angular -i CHANGELOG.md -s`
```bash
# 按 angular 预设生成变更日志
npx conventional-changelog -p angular -i CHANGELOG.md -s
```

---

## 配套钩子校验

**基本写法：在 commit-msg 钩子中校验**
`.husky/commit-msg`
```bash
# 用 husky 钩子调用 commitlint
npx --no-install commitlint --edit "$1"
```

---

**基本写法：跳过钩子校验**
`git commit --no-verify -m "<消息>"`
```bash
# 紧急情况跳过校验（不推荐）
git commit --no-verify -m "fix: 紧急修复"
```

---

## Angular 提交规范

**基本写法：Angular 类型**
`<type>(<scope>): <subject>`
```bash
# Angular 规范要求主题全小写且不超过 72 字符
feat(auth): add oauth2 login
```

---

**基本写法：主题用祈使句**
`<类型>: <动词原形> <宾语>`
```bash
# 主题用祈使句现在时
feat: add export feature
```

---

**基本写法：正文换行控制**
`<每行不超过 72 字符>`
```bash
# 正文每行限制 72 字符便于阅读
git commit -m "feat: add export" -m "支持 CSV 与 JSON 两种格式导出"
```



<!-- ============ 文档分隔线：003-git/027-GitStash.md ============ -->

# git stash 暂存命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

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



<!-- ============ 文档分隔线：003-git/028-GitLogAdvanced.md ============ -->

# git log 高级用法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

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



<!-- ============ 文档分隔线：003-git/029-GitShow.md ============ -->

# git show 查看命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 查看提交内容

**基本用法:查看某次提交**
`git show <提交>`

```bash
# 查看最新提交的详情
git show

# 查看指定提交
git show a1b2c3d

# 查看指定提交的元信息与统计
git show --stat HEAD
```

---

**基本用法:查看提交的文件差异**
`git show <提交> -- <路径>`

```bash
# 仅查看该提交中某个文件的改动
git show a1b2c3d -- src/main.py

# 查看合并提交的差异
git show -m a1b2c3d
```

---

## 查看特定对象

**基本用法:查看 blob 内容**
`git show <对象>`

```bash
# 查看某次提交中某文件的完整内容
git show HEAD:src/config.js

# 查看某分支某文件
git show feature:package.json

# 查看特定标签指向的提交
git show v1.0.0
```

---

## 格式化输出

**基本用法:自定义格式**
`git show --pretty=format:"<格式>"`

```bash
# 自定义提交信息格式
git show --pretty=format:"%H%n%an%n%s" HEAD

# 仅显示提交说明
git show --no-patch --format="%s"
```

---

**基本用法:差异输出格式**
`git show --<格式>`

```bash
# 仅显示文件名
git show --name-only HEAD

# word-level 差异
git show --word-diff HEAD

# 统计模式
git show --stat --oneline HEAD
```

---



<!-- ============ 文档分隔线：003-git/030-GitStatus.md ============ -->

# git status 状态命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 基础查看

**基本用法:查看工作区状态**
`git status`

```bash
# 查看完整状态
git status

# 简洁模式
git status -s

# 显示被忽略文件
git status --ignored
```

---

## 紧凑输出

**基本用法:短格式**
`git status -s`

```bash
# 左列暂存区,右列工作区
git status -s

# 带分支信息
git status -sb
```

---

状态码含义:
- `M` 已修改(modified)
- `A` 已新增到暂存区(added)
- `D` 已删除(deleted)
- `R` 重命名(renamed)
- `??` 未跟踪(untracked)

---

## 瓷器格式

**基本用法:机器可读输出**
`git status --porcelain`

```bash
# 稳定的脚本可解析格式
git status --porcelain

# v2 版本含分支与重命名信息
git status --porcelain=v2

# 仅列出未跟踪文件
git status --porcelain | grep '^??'
```

---

## 分支信息

**基本用法:查看与上游分支关系**
`git status -sb`

```bash
# 显示领先/落后远程的提交数
git status -sb
# 输出示例:## main...origin/main [ahead 2, behind 1]
```

---

**基本用法:查看指定分支**
`git status <分支>`

```bash
# 与指定分支比较
git status main
```

---

## 长格式选项

**基本用法:长格式说明**
`git status --long`

```bash
# 强制长格式(默认)
git status --long
```

---



<!-- ============ 文档分隔线：003-git/031-GitAddPatch.md ============ -->

# git add/restore/checkout 工作区命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

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



<!-- ============ 文档分隔线：003-git/032-GitClean.md ============ -->

# git clean 清理命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 预演与清理

**基本用法:预览将删除的文件**
`git clean -n`

```bash
# 干跑模式,只显示不删除
git clean -n
```

---

**基本用法:删除未跟踪文件**
`git clean -f`

```bash
# 强制删除未跟踪文件
git clean -f

# 删除未跟踪目录
git clean -fd

# 同时删除被忽略的文件
git clean -fdx
```

---

## 选择性清理

**基本用法:限定路径**
`git clean -f <路径>`

```bash
# 仅清理指定目录
git clean -f build/

# 排除指定模式
git clean -fd -e "*.log"
```

---

**基本用法:交互式确认**
`git clean -i`

```bash
# 交互式逐个确认删除
git clean -id
```

---

## 常见组合

**基本用法:彻底清理工作区**
`git clean -fdx`

```bash
# 删除所有未跟踪文件、目录与被忽略文件
git clean -fdx

# 配合重置回到干净状态
git reset --hard && git clean -fdx
```

---

## 与 reset 配合回滚

**基本用法:彻底放弃所有改动**
`git reset --hard && git clean -fd`

```bash
# 已跟踪改动用 reset,未跟踪文件用 clean
git reset --hard origin/main
git clean -fd
```

---



<!-- ============ 文档分隔线：003-git/033-GitMv.md ============ -->

# git mv 文件移动命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 重命名文件

**基本用法:重命名**
`git mv <源文件> <目标文件>`

```bash
# 重命名文件(自动记录为重命名)
git mv old_name.js new_name.js

# 移动文件到新目录
git mv src/utils.js src/helpers/utils.js
```

---

**基本用法:移动目录**
`git mv <源目录> <目标目录>`

```bash
# 移动整个目录
git mv old_dir/ new_dir/

# 批量移动目录下所有文件
git mv old_dir/* new_dir/
```

---

## 强制覆盖

**基本用法:覆盖已存在文件**
`git mv -f <源> <目标>`

```bash
# 强制覆盖目标文件
git mv -f temp.js existing.js
```

---

## 干跑预览

**基本用法:预演移动**
`git mv -n <源> <目标>`

```bash
# 显示将执行的移动但不实际执行
git mv -n old.js new.js
```

---

## 与原生 mv 的区别

**基本用法:原生移动后修复**
`mv <源> <目标> && git add -A`

```bash
# 用系统命令移动后,git 自动识别重命名
mv old.js new.js
git add -A
git status
```

---



<!-- ============ 文档分隔线：003-git/034-GitNotes.md ============ -->

# git notes 备注命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 添加备注

**基本用法:为提交添加备注**
`git notes add -m "<内容>" <提交>`

```bash
# 给指定提交添加备注(不修改原提交)
git notes add -m "代码审查通过" a1b2c3d

# 给最新提交添加备注
git notes add -m "上线前补充测试"
```

---

**基本用法:追加备注**
`git notes append -m "<内容>" <提交>`

```bash
# 在已有备注后追加
git notes append -m "补充说明:已修复" a1b2c3d
```

---

## 查看备注

**基本用法:查看某提交备注**
`git notes show <提交>`

```bash
# 查看指定提交的备注
git notes show a1b2c3d

# 在 log 中显示备注
git log --show-notes
```

---

**基本用法:列出所有有备注的提交**
`git notes list`

```bash
# 列出所有备注及其对应提交
git notes list

# 列出某提交树上的备注
git notes list a1b2c3d
```

---

## 管理备注

**基本用法:编辑备注**
`git notes edit <提交>`

```bash
# 调用编辑器修改备注
git notes edit a1b2c3d
```

---

**基本用法:复制备注**
`git notes copy <源提交> <目标提交>`

```bash
# 把备注从 A 复制到 B
git notes copy a1b2c3d d4e5f6g
```

---

**基本用法:删除备注**
`git notes remove <提交>`

```bash
# 删除指定提交的备注
git notes remove a1b2c3d

# 删除所有备注
git notes prune
```

---

## 共享备注

**基本用法:推送备注到远程**
`git push origin refs/notes/commits`

```bash
# 推送备注到远程仓库
git push origin refs/notes/commits

# 拉取他人备注
git fetch origin refs/notes/*:refs/notes/*
```

---



<!-- ============ 文档分隔线：003-git/035-GitGcPrune.md ============ -->

# git gc/prune/fsck 仓库维护命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## gc 垃圾回收

**基本用法:手动整理仓库**
`git gc [选项]`

```bash
# 执行垃圾回收与压缩
git gc

# 更彻底的整理(更耗时)
git gc --aggressive

# 自动判断是否需要整理
git gc --auto

# 仅整理不压缩
git gc --no-prune
```

---

**基本用法:压包**
`git repack [选项]`

```bash
# 重新打包松散对象
git repack -d

# 增量打包
git repack -a -d
```

---

## prune 清理松散对象

**基本用法:删除不可达对象**
`git prune [选项]`

```bash
# 删除超过 2 周的不可达松散对象
git prune --expire=2.weeks.ago

# 预演查看将删除什么
git prune -n

# 立即清理所有不可达对象
git prune --expire=now
```

---

## fsck 完整性检查

**基本用法:检查仓库完整性**
`git fsck [选项]`

```bash
# 检查所有对象的连通性与完整性
git fsck --full

# 显示悬挂的提交对象
git fsck --lost-found

# 检查不可达对象
git fsck --unreachable
```

---

## count-objects 统计

**基本用法:查看对象统计**
`git count-objects -v`

```bash
# 显示对象数量与占用空间
git count-objects -v
```

---

## maintenance 维护任务

**基本用法:启动后台维护**
`git maintenance run [选项]`

```bash
# 运行所有维护任务
git maintenance run --all

# 启用自动维护
git maintenance start

# 注册仓库到自动维护
git maintenance register
```

---



<!-- ============ 文档分隔线：003-git/036-GitBundle.md ============ -->

# git bundle 打包命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 bundle

**基本用法:打包整个仓库**
`git bundle create <文件> <引用>`

```bash
# 打包所有分支与标签
git bundle create repo.bundle --all

# 仅打包指定分支
git bundle create feature.bundle feature

# 打包指定区间提交
git bundle create diff.bundle main..feature
```

---

**基本用法:打包指定范围**
`git bundle create <文件> <旧提交>..<新提交>`

```bash
# 打包自上次同步以来的提交
git bundle create updates.bundle origin/main..main

# 打包最近 7 天的提交
git bundle create week.bundle --since="7 days ago" main
```

---

## 校验 bundle

**基本用法:校验 bundle 可用性**
`git bundle verify <文件>`

```bash
# 检查 bundle 是否包含所需引用
git bundle verify repo.bundle
```

---

**基本用法:查看 bundle 包含的引用**
`git bundle list-heads <文件>`

```bash
# 列出 bundle 中的所有分支头
git bundle list-heads repo.bundle
```

---

## 从 bundle 恢复

**基本用法:从 bundle 克隆**
`git clone <文件> <目录>`

```bash
# 从 bundle 克隆新仓库(离线传输)
git clone repo.bundle my-project
```

---

**基本用法:从 bundle 拉取**
`git fetch <文件> <引用>`

```bash
# 把 bundle 当作远程拉取
git fetch repo.bundle main:incoming-main
```

---



<!-- ============ 文档分隔线：003-git/037-GitRangeDiff.md ============ -->

# git range-diff 范围对比命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 对比提交范围

**基本用法:对比两段提交序列**
`git range-diff <旧基准>..<旧终点> <新基准>..<新终点>`

```bash
# 对比重排前后的分支提交
git range-diff main..old-feature main..new-feature

# 简写:用旧 tip 与新 tip 对比同一基准
git range-diff main...feature@{1} main...feature
```

---

**基本用法:rebase 前后对比**
`git range-diff <upstream> <分支>@{1} <分支>`

```bash
# 查看上次 rebase 后提交的变化
git range-diff main feature@{1} feature
```

---

## 创建与对比选项

**基本用法:控制输出**
`git range-diff --creation-factor=<百分比>`

```bash
# 调整视为新增的阈值(默认 60%)
git range-diff --creation-factor=80 main..old main..new

# 双向显示
git range-diff --dual-color main..old main..new
```

---

## 实战场景

**基本用法:检查 cherry-pick 后差异**
`git range-diff`

```bash
# 对比 cherry-pick 前后的提交差异
git range-diff main..original main..cherry-picked
```

---



<!-- ============ 文档分隔线：003-git/038-GitVerify.md ============ -->

# git verify 签名验证命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 签名提交与标签

**基本用法:GPG 签名提交**
`git commit -S [选项]`

```bash
# 用 GPG 密钥签名提交
git commit -S -m "release v2.0"

# 指定密钥签名
git commit -S --gpg-sign=<KEY_ID> -m "signed commit"
```

---

**基本用法:签名标签**
`git tag -s <标签名>`

```bash
# 创建带 GPG 签名的附注标签
git tag -s v1.0.0 -m "release 1.0"

# 用指定密钥签名
git tag -s v1.0.0 -u <KEY_ID> -m "release 1.0"
```

---

## 验证签名

**基本用法:验证提交签名**
`git verify-commit <提交>`

```bash
# 验证某提交是否被正确签名
git verify-commit a1b2c3d

# 显示原始签名信息
git verify-commit --raw a1b2c3d
```

---

**基本用法:验证标签签名**
`git verify-tag <标签>`

```bash
# 验证标签签名
git verify-tag v1.0.0

# 显示标签签名详情
git tag -v v1.0.0
```

---

## 查看签名信息

**基本用法:在 log 中显示签名**
`git log --show-signature`

```bash
# 查看提交历史时显示签名验证结果
git log --show-signature -5

# 仅显示 Good signature 的提交
git log --pretty="format:%G? %s" | grep "^G"
```

---

## 配置默认签名

**基本用法:开启全局签名**
`git config --global commit.gpgsign true`

```bash
# 默认所有提交都签名
git config --global commit.gpgsign true

# 默认所有标签都签名
git config --global tag.gpgsign true

# 指定签名密钥
git config --global user.signingkey <KEY_ID>
```

---



<!-- ============ 文档分隔线：003-git/039-GitAttributes.md ============ -->

# gitattributes 与 gitignore 速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## gitattributes 文件属性

**基本用法:指定换行符处理**
`<模式> <属性>`

```bash
# 创建 .gitattributes 文件
# 统一为 LF 换行符
* text=auto eol=lf

# Windows 文件保留 CRLF
*.bat text eol=crlf

# 二进制文件不做换行处理
*.png binary
```

---

**基本用法:指定合并策略**
`<模式> merge=<策略>`

```bash
# 锁定文件保留己方版本
package-lock.json merge=ours

# 指定 diff 算法
*.c diff=cpp
```

---

**基本用法:导出时忽略**
`<模式> export-ignore`

```bash
# 归档时排除测试文件
tests/ export-ignore
*.spec.js export-ignore
```

---

**基本用法:LFS 跟踪大文件**
`<模式> filter=lfs`

```bash
# 用 git-lfs 跟踪大文件
*.psd filter=lfs diff=lfs merge=lfs -text
*.zip filter=lfs
```

---

**基本用法:语言统计**
`<模式> linguist-language=<语言>`

```bash
# 指定 GitHub 语言识别
*.h linguist-language=cpp
docs/* linguist-documentation
vendor/* linguist-vendored
```

---

## gitignore 忽略规则

**基本用法:忽略文件**
`<模式>`

```bash
# 创建 .gitignore
# 忽略所有 .log 文件
*.log

# 忽略整个目录
node_modules/
dist/

# 但不忽略特定文件
!important.log

# 忽略某目录下除某文件外
temp/*
!temp/keep.md
```

---

**基本用法:全局忽略**
`git config --global core.excludesfile <文件>`

```bash
# 设置全局忽略文件
git config --global core.excludesfile ~/.gitignore_global
```

---

**基本用法:已跟踪文件停止跟踪**
`git rm --cached <文件>`

```bash
# 从仓库移除但保留本地文件
git rm --cached .env
git commit -m "stop tracking .env"
```

---

## 检查忽略原因

**基本用法:查看为何被忽略**
`git check-ignore -v <文件>`

```bash
# 显示是哪条规则忽略了该文件
git check-ignore -v secrets.key
```

---
