---
order: 10
title: github 模块文档合集
module: 'github'
category: 工具链
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：004-github/001-GitRepoInit.md ============ -->

# GitHub 仓库初始化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：004-github/002-GitCommitPush.md ============ -->

# GitHub 提交与推送

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 提交更改

**基本写法：提交暂存区**
`git commit -m "<提交信息>"`
```bash
# 提交暂存区内容并附带说明
git commit -m "feat: 添加用户登录功能"
```

---

**基本写法：提交所有已跟踪文件**
`git commit -am "<提交信息>"`
```bash
# 跳过 add 直接提交已跟踪文件的改动
git commit -am "fix: 修复样式问题"
```

---

**基本写法：多行提交信息**
`git commit -m "<标题>" -m "<描述>"`
```bash
# 添加标题和详细描述
git commit -m "feat: 添加搜索功能" -m "支持按关键词和日期范围搜索"
```

---

**基本写法：打开编辑器写提交信息**
`git commit`
```bash
# 打开默认编辑器编写提交信息
git commit
```

---

**基本写法：修改上次提交**
`git commit --amend -m "<新信息>"`
```bash
# 修改最近一次提交的信息
git commit --amend -m "feat: 添加用户注册功能"
```

---

**基本写法：追加文件到上次提交**
`git commit --amend --no-edit`
```bash
# 将新改动追加到上次提交不修改信息
git add forgotten.js && git commit --amend --no-edit
```

---

**基本写法：修改上次提交作者**
`git commit --amend --author="<名字> <<邮箱>>"`
```bash
# 修改上次提交的作者信息
git commit --amend --author="张三 <zhangsan@example.com>"
```

---

## 提交信息规范

**基本写法：feat 类型提交**
`git commit -m "feat: <功能描述>"`
```bash
# 新功能提交
git commit -m "feat: 添加购物车功能"
```

---

**基本写法：fix 类型提交**
`git commit -m "fix: <修复描述>"`
```bash
# Bug 修复提交
git commit -m "fix: 修复登录页面崩溃问题"
```

---

**基本写法：带作用域的提交**
`git commit -m "<类型>(<范围>): <描述>"`
```bash
# 带模块作用域的提交
git commit -m "feat(auth): 添加 OAuth 登录"
```

---

**基本写法：带 BREAKING CHANGE 的提交**
`git commit -m "<类型>: <描述>" -m "BREAKING CHANGE: <破坏性说明>"`
```bash
# 标记破坏性变更
git commit -m "feat: 重构 API 接口" -m "BREAKING CHANGE: 响应格式改为 JSON"
```

---

## 推送到远程

**基本写法：推送当前分支**
`git push`
```bash
# 推送当前分支到对应的远程分支
git push
```

---

**基本写法：推送指定分支**
`git push origin <分支名>`
```bash
# 推送指定分支到远程仓库
git push origin main
```

---

**基本写法：首次推送并建立追踪**
`git push -u origin <分支名>`
```bash
# 推送并设置上游追踪关系
git push -u origin feature/login
```

---

**基本写法：推送所有分支**
`git push --all origin`
```bash
# 推送所有本地分支到远程
git push --all origin
```

---

**基本写法：强制推送（安全方式）**
`git push --force-with-lease origin <分支名>`
```bash
# 安全的强制推送（避免覆盖他人提交）
git push --force-with-lease origin feature/login
```

---

**基本写法：强制推送（危险）**
`git push -f origin <分支名>`
```bash
# 强制覆盖远程分支（慎用）
git push -f origin feature/login
```

---

**基本写法：删除远程分支**
`git push origin --delete <分支名>`
```bash
# 删除远程仓库的指定分支
git push origin --delete old-feature
```

---

**基本写法：推送标签**
`git push origin <标签名>`
```bash
# 推送指定标签到远程
git push origin v1.0.0
```

---

**基本写法：推送所有标签**
`git push origin --tags`
```bash
# 推送所有本地标签到远程
git push origin --tags
```

---

## 提交历史查看

**基本写法：查看提交历史**
`git log`
```bash
# 查看完整提交历史
git log
```

---

**基本写法：简洁单行历史**
`git log --oneline`
```bash
# 每条提交一行显示
git log --oneline
```

---

**基本写法：图形化分支历史**
`git log --oneline --graph --all`
```bash
# 图形化显示所有分支提交历史
git log --oneline --graph --all
```

---

**基本写法：查看最近 N 条提交**
`git log -<数量>`
```bash
# 查看最近 5 条提交记录
git log -5
```

---

**基本写法：查看作者提交历史**
`git log --author="<作者>"`
```bash
# 查看指定作者的提交
git log --author="zhangsan"
```

---

**基本写法：按日期查看历史**
`git log --since="<日期>" --until="<日期>"`
```bash
# 查看指定日期范围的提交
git log --since="2026-01-01" --until="2026-07-31"
```



<!-- ============ 文档分隔线：004-github/003-GitPullFetch.md ============ -->

# GitHub 拉取与获取

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 拉取远程更新

**基本写法：拉取并合并**
`git pull`
```bash
# 拉取远程更新并合并到当前分支
git pull
```

---

**基本写法：拉取指定远程分支**
`git pull origin <分支名>`
```bash
# 拉取指定远程分支并合并
git pull origin main
```

---

**基本写法：拉取并变基**
`git pull --rebase`
```bash
# 拉取远程更新并使用 rebase 方式合并
git pull --rebase
```

---

**基本写法：拉取指定远程和分支并变基**
`git pull --rebase origin <分支名>`
```bash
# 拉取指定分支并使用 rebase
git pull --rebase origin main
```

---

**基本写法：允许不相关历史合并**
`git pull --allow-unrelated-histories`
```bash
# 合并不相关的历史（如初始化仓库后首次合并）
git pull origin main --allow-unrelated-histories
```

---

**基本写法：仅拉取不自动合并**
`git pull --no-commit`
```bash
# 拉取更新但不自动创建合并提交
git pull --no-commit
```

---

## 获取远程信息

**基本写法：获取所有远程更新**
`git fetch`
```bash
# 获取远程所有分支的更新（不合并）
git fetch
```

---

**基本写法：获取指定远程**
`git fetch origin`
```bash
# 获取 origin 远程的更新
git fetch origin
```

---

**基本写法：获取指定分支**
`git fetch origin <分支名>`
```bash
# 获取指定远程分支的更新
git fetch origin main
```

---

**基本写法：获取所有远程**
`git fetch --all`
```bash
# 获取所有远程仓库的更新
git fetch --all
```

---

**基本写法：获取并清理已删除分支**
`git fetch --prune`
```bash
# 获取更新并清理远程已删除的分支引用
git fetch --prune
```

---

**基本写法：获取指定标签**
`git fetch origin <标签名>`
```bash
# 获取远程指定的标签
git fetch origin v1.0.0
```

---

**基本写法：获取所有标签**
`git fetch --tags`
```bash
# 获取远程所有标签
git fetch --tags
```

---

## 远程分支操作

**基本写法：查看远程分支**
`git branch -r`
```bash
# 列出所有远程分支
git branch -r
```

---

**基本写法：查看所有分支**
`git branch -a`
```bash
# 列出本地和远程所有分支
git branch -a
```

---

**基本写法：查看分支详细信息**
`git branch -vv`
```bash
# 查看分支及其追踪关系和最新提交
git branch -vv
```

---

**基本写法：从远程分支创建本地分支**
`git switch -c <本地分支> origin/<远程分支>`
```bash
# 基于远程分支创建本地分支并切换
git switch -c feature origin/feature
```

---

**基本写法：直接跟踪远程分支**
`git switch <分支名>`
```bash
# 自动追踪同名远程分支
git switch feature
```

---

## 拉取冲突处理

**基本写法：中止合并**
`git merge --abort`
```bash
# 取消正在进行的合并操作
git merge --abort
```

---

**基本写法：中止变基**
`git rebase --abort`
```bash
# 取消正在进行的变基操作
git rebase --abort
```

---

**基本写法：继续合并**
`git merge --continue`
```bash
# 解决冲突后继续合并
git merge --continue
```

---

**基本写法：继续变基**
`git rebase --continue`
```bash
# 解决冲突后继续变基
git rebase --continue
```

---

**基本写法：跳过当前变基提交**
`git rebase --skip`
```bash
# 跳过当前冲突的提交继续变基
git rebase --skip
```

---

## 远程信息查看

**基本写法：查看远程仓库详情**
`git remote show origin`
```bash
# 显示 origin 远程仓库的详细信息
git remote show origin
```

---

**基本写法：查看远程分支列表**
`git ls-remote origin`
```bash
# 列出远程仓库的所有引用
git ls-remote origin
```

---

**基本写法：查看远程 HEAD 分支**
`git remote show origin | grep "HEAD branch"`
```bash
# 查看远程默认分支名
git remote show origin | grep "HEAD branch"
```



<!-- ============ 文档分隔线：004-github/004-GitBranchManage.md ============ -->

# GitHub 分支管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建分支

**基本写法：创建新分支**
`git branch <分支名>`
```bash
# 创建新分支但不切换
git branch feature/login
```

---

**基本写法：创建并切换分支**
`git switch -c <分支名>`
```bash
# 创建新分支并立即切换
git switch -c feature/login
```

---

**基本写法：checkout 方式创建并切换**
`git checkout -b <分支名>`
```bash
# 旧写法创建并切换分支
git checkout -b feature/login
```

---

**基本写法：从指定提交创建分支**
`git switch -c <分支名> <提交ID>`
```bash
# 从指定提交点创建新分支
git switch -c hotfix abc1234
```

---

**基本写法：从远程分支创建**
`git switch -c <本地分支> origin/<远程分支>`
```bash
# 基于远程分支创建本地分支
git switch -c feature origin/feature
```

---

**基本写法：创建追踪远程分支**
`git switch --track origin/<远程分支>`
```bash
# 创建并追踪同名远程分支
git switch --track origin/feature
```

---

## 查看分支

**基本写法：查看本地分支**
`git branch`
```bash
# 列出所有本地分支
git branch
```

---

**基本写法：查看所有分支**
`git branch -a`
```bash
# 列出本地和远程所有分支
git branch -a
```

---

**基本写法：查看远程分支**
`git branch -r`
```bash
# 仅列出远程分支
git branch -r
```

---

**基本写法：查看分支追踪信息**
`git branch -vv`
```bash
# 查看分支追踪关系和最新提交
git branch -vv
```

---

**基本写法：按最新提交排序**
`git branch --sort=-committerdate`
```bash
# 按最近提交时间排序分支
git branch --sort=-committerdate
```

---

**基本写法：查看已合并分支**
`git branch --merged`
```bash
# 查看已合并到当前分支的分支
git branch --merged
```

---

**基本写法：查看未合并分支**
`git branch --no-merged`
```bash
# 查看未合并到当前分支的分支
git branch --no-merged
```

---

## 切换分支

**基本写法：切换到指定分支**
`git switch <分支名>`
```bash
# 切换到指定分支（推荐写法）
git switch main
```

---

**基本写法：checkout 切换分支**
`git checkout <分支名>`
```bash
# 旧写法切换分支
git checkout main
```

---

**基本写法：切换到上一个分支**
`git switch -`
```bash
# 快速切换到上次所在的分支
git switch -
```

---

**基本写法：checkout 切换上一分支**
`git checkout -`
```bash
# 旧写法切换到上一个分支
git checkout -
```

---

**基本写法：切换到远程分支**
`git switch <远程分支名>`
```bash
# 自动追踪同名远程分支并切换
git switch origin/feature
```

---

## 删除分支

**基本写法：删除已合并分支**
`git branch -d <分支名>`
```bash
# 删除已合并的本地分支
git branch -d feature/login
```

---

**基本写法：强制删除分支**
`git branch -D <分支名>`
```bash
# 强制删除未合并的分支
git branch -D feature/abandoned
```

---

**基本写法：删除远程分支**
`git push origin --delete <分支名>`
```bash
# 删除远程仓库的分支
git push origin --delete old-feature
```

---

**基本写法：删除远程分支（替代方式）**
`git push origin :<分支名>`
```bash
# 通过推送空分支删除远程分支
git push origin :old-feature
```

---

## 重命名分支

**基本写法：重命名当前分支**
`git branch -m <新名>`
```bash
# 重命名当前所在分支
git branch -m main
```

---

**基本写法：重命名指定分支**
`git branch -m <旧名> <新名>`
```bash
# 重命名指定分支
git branch -m old-name new-name
```

---

**基本写法：重命名远程分支**
`git push origin :<旧名> <新名>`
```bash
# 删除旧远程分支并推送新名分支
git push origin :old-feature new-feature
```

---

**基本写法：设置新上游**
`git branch -u origin/<新名>`
```bash
# 为重命名后的分支设置新的追踪关系
git branch -u origin/new-feature
```

---

## 分支关联管理

**基本写法：设置上游分支**
`git branch --set-upstream-to=origin/<分支名>`
```bash
# 为当前分支设置远程追踪
git branch --set-upstream-to=origin/main
```

---

**基本写法：设置上游（短写法）**
`git branch -u origin/<分支名>`
```bash
# 设置当前分支的远程追踪
git branch -u origin/main
```

---

**基本写法：取消上游关联**
`git branch --unset-upstream`
```bash
# 移除当前分支的远程追踪关系
git branch --unset-upstream
```

---

**基本写法：查看所有分支的追踪关系**
`git branch -vv`
```bash
# 显示各分支的远程追踪状态
git branch -vv
```



<!-- ============ 文档分隔线：004-github/005-GitMergeRebase.md ============ -->

# GitHub 合并与变基

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 合并分支

**基本写法：合并指定分支**
`git merge <分支名>`
```bash
# 将指定分支合并到当前分支
git merge feature/login
```

---

**基本写法：禁止快进合并**
`git merge --no-ff <分支名>`
```bash
# 强制创建合并提交保留分支历史
git merge --no-ff feature/login
```

---

**基本写法：仅快进合并**
`git merge --ff-only <分支名>`
```bash
# 仅在可快进时合并否则失败
git merge --ff-only feature/login
```

---

**基本写法：压缩合并**
`git merge --squash <分支名>`
```bash
# 将所有提交压缩为一个后合并
git merge --squash feature/login
```

---

**基本写法：合并并编辑提交信息**
`git merge -e <分支名>`
```bash
# 合并时打开编辑器编辑提交信息
git merge -e feature/login
```

---

**基本写法：合并指定提交**
`git cherry-pick <提交ID>`
```bash
# 将指定提交应用到当前分支
git cherry-pick abc1234
```

---

**基本写法：合并多个提交**
`git cherry-pick <提交1> <提交2>`
```bash
# 将多个提交应用到当前分支
git cherry-pick abc1234 def5678
```

---

## 变基操作

**基本写法：变基到指定分支**
`git rebase <目标分支>`
```bash
# 将当前分支变基到目标分支
git rebase main
```

---

**基本写法：交互式变基**
`git rebase -i HEAD~<数量>`
```bash
# 交互式整理最近 N 次提交
git rebase -i HEAD~5
```

---

**基本写法：交互式变基到指定提交**
`git rebase -i <提交ID>`
```bash
# 从指定提交开始交互式变基
git rebase -i abc1234
```

---

**基本写法：变基到远程分支**
`git rebase origin/<分支名>`
```bash
# 将当前分支变基到远程分支
git rebase origin/main
```

---

**基本写法：变基时保留空提交**
`git rebase --keep-empty <目标分支>`
```bash
# 变基时保留空提交
git rebase --keep-empty main
```

---

## 变基冲突处理

**基本写法：继续变基**
`git rebase --continue`
```bash
# 解决冲突后继续变基
git rebase --continue
```

---

**基本写法：跳过当前提交**
`git rebase --skip`
```bash
# 跳过当前冲突的提交
git rebase --skip
```

---

**基本写法：中止变基**
`git rebase --abort`
```bash
# 取消变基回到变基前状态
git rebase --abort
```

---

**基本写法：编辑待提交内容**
`git rebase --edit-todo`
```bash
# 编辑变基待办列表
git rebase --edit-todo
```

---

## 交互式变基操作

**基本写法：使用 pick 保留提交**
`pick <提交ID>`
```bash
# 在变基编辑器中使用保留该提交
pick abc1234 添加登录功能
```

---

**基本写法：使用 reword 修改信息**
`reword <提交ID>`
```bash
# 保留提交但修改提交信息
reword abc1234 修改提交说明
```

---

**基本写法：使用 squash 合并提交**
`squash <提交ID>`
```bash
# 将该提交合并到前一个提交
squash def5678 修复样式
```

---

**基本写法：使用 fixup 合并并丢弃信息**
`fixup <提交ID>`
```bash
# 合并到前一个提交并丢弃提交信息
fixup def5678 修复样式
```

---

**基本写法：使用 drop 删除提交**
`drop <提交ID>`
```bash
# 删除该提交
drop ghi9012 废弃的实验代码
```

---

**基本写法：使用 edit 暂停修改**
`edit <提交ID>`
```bash
# 在该提交处暂停以便修改内容
edit abc1234 添加登录功能
```

---

## 合并后清理

**基本写法：删除已合并的本地分支**
`git branch -d <分支名>`
```bash
# 合并完成后删除本地分支
git branch -d feature/login
```

---

**基本写法：删除已合并的远程分支**
`git push origin --delete <分支名>`
```bash
# 合并完成后删除远程分支
git push origin --delete feature/login
```

---

**基本写法：清理已删除的远程分支引用**
`git fetch --prune`
```bash
# 清理本地中已不存在的远程分支引用
git fetch --prune
```

---

**基本写法：查看可清理的分支**
`git branch --merged main`
```bash
# 查看已合并到 main 的分支
git branch --merged main
```

---

**基本写法：批量删除已合并分支**
`git branch --merged main | grep -v "main" | xargs git branch -d`
```bash
# 删除所有已合并到 main 的分支（保留 main）
git branch --merged main | grep -v "main" | xargs git branch -d
```



<!-- ============ 文档分隔线：004-github/006-GitConflictResolve.md ============ -->

# GitHub 冲突解决

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 冲突识别

**基本写法：查看冲突文件**
`git status`
```bash
# 查看哪些文件存在合并冲突
git status
```

---

**基本写法：查看冲突详情**
`git diff --name-only --diff-filter=U`
```bash
# 仅列出有冲突的文件名
git diff --name-only --diff-filter=U
```

---

**基本写法：查看冲突内容**
`git diff`
```bash
# 查看冲突的具体内容
git diff
```

---

**基本写法：使用 mergetool**
`git mergetool`
```bash
# 启动图形化合并工具解决冲突
git mergetool
```

---

**基本写法：指定合并工具**
`git mergetool --tool=<工具名>`
```bash
# 使用指定的合并工具
git mergetool --tool=vimdiff
```

---

## 冲突标记处理

**基本写法：冲突标记说明**
`<<<<<<< HEAD`
```bash
# 冲突标记开始（当前分支内容）
# <<<<<<< HEAD
# 当前分支的代码
# =======
# 传入分支的代码
# >>>>>>> feature/login
```

---

**基本写法：保留当前分支版本**
`git checkout --ours <文件>`
```bash
# 冲突时保留当前分支的版本
git checkout --ours index.js
```

---

**基本写法：保留传入分支版本**
`git checkout --theirs <文件>`
```bash
# 冲突时保留传入分支的版本
git checkout --theirs index.js
```

---

**基本写法：使用 VS Code 解决冲突**
`code <冲突文件>`
```bash
# 用 VS Code 打开冲突文件图形化解决
code index.js
```

---

## 冲突解决流程

**基本写法：标记冲突已解决**
`git add <文件>`
```bash
# 编辑文件解决冲突后添加到暂存区
git add index.js
```

---

**基本写法：完成合并提交**
`git commit -m "<合并信息>"`
```bash
# 所有冲突解决后完成合并提交
git commit -m "merge: 合并 feature/login 分支"
```

---

**基本写法：使用默认合并信息**
`git commit --no-edit`
```bash
# 使用默认的合并提交信息
git commit --no-edit
```

---

**基本写法：继续变基**
`git rebase --continue`
```bash
# 变基冲突解决后继续
git rebase --continue
```

---

**基本写法：完成 cherry-pick**
`git cherry-pick --continue`
```bash
# cherry-pick 冲突解决后继续
git cherry-pick --continue
```

---

## 中止操作

**基本写法：中止合并**
`git merge --abort`
```bash
# 取消合并回到合并前状态
git merge --abort
```

---

**基本写法：中止变基**
`git rebase --abort`
```bash
# 取消变基回到变基前状态
git rebase --abort
```

---

**基本写法：中止 cherry-pick**
`git cherry-pick --abort`
```bash
# 取消 cherry-pick 操作
git cherry-pick --abort
```

---

**基本写法：重置到合并前状态**
`git reset --hard HEAD`
```bash
# 强制重置到当前 HEAD（丢弃所有改动）
git reset --hard HEAD
```

---

## 冲突预防

**基本写法：拉取前先暂存**
`git stash && git pull && git stash pop`
```bash
# 暂存当前改动后拉取再恢复
git stash && git pull && git stash pop
```

---

**基本写法：使用 rebase 拉取**
`git pull --rebase`
```bash
# 拉取时使用变基避免合并提交
git pull --rebase
```

---

**基本写法：定期同步主分支**
`git fetch origin && git rebase origin/main`
```bash
# 定期将当前分支变基到最新主分支
git fetch origin && git rebase origin/main
```

---

**基本写法：查看分支差异**
`git diff main...feature`
```bash
# 查看 feature 分支相对 main 的差异
git diff main...feature
```

---

**基本写法：查看分支分叉点**
`git merge-base <分支1> <分支2>`
```bash
# 查看两个分支的共同祖先提交
git merge-base main feature
```



<!-- ============ 文档分隔线：004-github/007-GitTagManage.md ============ -->

# GitHub 标签管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建标签

**基本写法：创建轻量标签**
`git tag <标签名>`
```bash
# 在当前提交创建轻量标签
git tag v1.0.0
```

---

**基本写法：创建附注标签**
`git tag -a <标签名> -m "<说明>"`
```bash
# 创建带说明的附注标签（推荐）
git tag -a v1.0.0 -m "发布版本 1.0.0"
```

---

**基本写法：在指定提交创建标签**
`git tag -a <标签名> <提交ID> -m "<说明>"`
```bash
# 为历史提交创建标签
git tag -a v0.9.0 abc1234 -m "历史版本"
```

---

**基本写法：创建轻量标签在指定提交**
`git tag <标签名> <提交ID>`
```bash
# 在指定提交创建轻量标签
git tag v0.9.0 abc1234
```

---

## 查看标签

**基本写法：查看所有标签**
`git tag`
```bash
# 列出所有本地标签
git tag
```

---

**基本写法：按模式筛选标签**
`git tag -l "<模式>"`
```bash
# 列出匹配模式的标签
git tag -l "v1.*"
```

---

**基本写法：查看标签详情**
`git show <标签名>`
```bash
# 查看标签指向的提交信息
git show v1.0.0
```

---

**基本写法：按版本排序标签**
`git tag -l --sort=-v:refname`
```bash
# 按版本号倒序排列标签
git tag -l --sort=-v:refname
```

---

**基本写法：查看标签数量**
`git tag | wc -l`
```bash
# 统计标签总数
git tag | wc -l
```

---

## 推送标签

**基本写法：推送单个标签**
`git push origin <标签名>`
```bash
# 推送指定标签到远程
git push origin v1.0.0
```

---

**基本写法：推送所有标签**
`git push origin --tags`
```bash
# 推送所有本地标签到远程
git push origin --tags
```

---

**基本写法：推送带标签的分支**
`git push origin <分支名> --tags`
```bash
# 推送分支的同时推送所有标签
git push origin main --tags
```

---

**基本写法：强制推送标签**
`git push origin -f <标签名>`
```bash
# 强制更新远程标签（覆盖）
git push origin -f v1.0.0
```

---

## 删除标签

**基本写法：删除本地标签**
`git tag -d <标签名>`
```bash
# 删除本地指定标签
git tag -d v1.0.0
```

---

**基本写法：删除远程标签**
`git push origin --delete <标签名>`
```bash
# 删除远程仓库的标签
git push origin --delete v1.0.0
```

---

**基本写法：删除远程标签（替代方式）**
`git push origin :refs/tags/<标签名>`
```bash
# 通过推送空引用删除远程标签
git push origin :refs/tags/v1.0.0
```

---

**基本写法：批量删除本地标签**
`git tag -l "<模式>" | xargs git tag -d`
```bash
# 删除匹配模式的所有本地标签
git tag -l "v0.*" | xargs git tag -d
```

---

## 检出标签

**基本写法：检出标签代码**
`git checkout <标签名>`
```bash
# 切换到标签指向的提交（分离 HEAD）
git checkout v1.0.0
```

---

**基本写法：从标签创建分支**
`git switch -c <分支名> <标签名>`
```bash
# 基于标签创建新分支进行修改
git switch -c hotfix-1.0 v1.0.0
```

---

**基本写法：checkout 从标签创建分支**
`git checkout -b <分支名> <标签名>`
```bash
# 旧写法从标签创建分支
git checkout -b hotfix-1.0 v1.0.0
```

---

## 标签管理

**基本写法：验证标签签名**
`git tag -v <标签名>`
```bash
# 验证 GPG 签名的标签
git tag -v v1.0.0
```

---

**基本写法：查看标签指向的提交**
`git rev-list -n 1 <标签名>`
```bash
# 获取标签指向的提交 ID
git rev-list -n 1 v1.0.0
```

---

**基本写法：比较标签差异**
`git diff <标签1>..<标签2>`
```bash
# 查看两个标签之间的差异
git diff v1.0.0..v1.1.0
```

---

**基本写法：查看标签间日志**
`git log <标签1>..<标签2> --oneline`
```bash
# 查看两个标签之间的提交记录
git log v1.0.0..v1.1.0 --oneline
```

---

## 语义化版本标签

**基本写法：创建预发布标签**
`git tag -a v1.0.0-beta -m "<说明>"`
```bash
# 创建 beta 预发布版本标签
git tag -a v1.0.0-beta -m "1.0.0 测试版"
```

---

**基本写法：创建发布候选标签**
`git tag -a v1.0.0-rc.1 -m "<说明>"`
```bash
# 创建 release candidate 标签
git tag -a v1.0.0-rc.1 -m "1.0.0 候选版本"
```

---

**基本写法：查看正式版本标签**
`git tag -l "v[0-9]*.[0-9]*.[0-9]*" | grep -v "-"`
```bash
# 仅列出正式版本（不含预发布）
git tag -l "v[0-9]*.[0-9]*.[0-9]*" | grep -v "-"
```



<!-- ============ 文档分隔线：004-github/008-GitRemoteManage.md ============ -->

# GitHub 远程仓库管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 查看远程仓库

**基本写法：查看远程仓库名称**
`git remote`
```bash
# 列出所有已配置的远程仓库名
git remote
```

---

**基本写法：查看远程仓库详情**
`git remote -v`
```bash
# 列出远程仓库名及其 URL
git remote -v
```

---

**基本写法：查看指定远程详情**
`git remote show origin`
```bash
# 显示 origin 远程仓库的详细信息
git remote show origin
```

---

**基本写法：查看远程分支**
`git remote show origin`
```bash
# 查看 origin 的所有分支信息
git remote show origin
```

---

## 添加远程仓库

**基本写法：添加远程仓库**
`git remote add origin <仓库URL>`
```bash
# 添加名为 origin 的远程仓库
git remote add origin https://github.com/user/repo.git
```

---

**基本写法：添加 SSH 远程**
`git remote add origin git@github.com:<用户>/<仓库>.git`
```bash
# 通过 SSH 协议添加远程仓库
git remote add origin git@github.com:user/repo.git
```

---

**基本写法：添加多个远程**
`git remote add <名称> <URL>`
```bash
# 添加 upstream 远程仓库（用于 fork 项目）
git remote add upstream https://github.com/original/repo.git
```

---

**基本写法：添加自定义名称远程**
`git remote add <名称> <URL>`
```bash
# 添加自定义名称的远程仓库
git remote add backup https://github.com/user/backup.git
```

---

## 修改远程仓库

**基本写法：修改远程 URL**
`git remote set-url origin <新URL>`
```bash
# 修改 origin 的 URL 地址
git remote set-url origin https://github.com/user/new-repo.git
```

---

**基本写法：切换为 SSH 协议**
`git remote set-url origin git@github.com:<用户>/<仓库>.git`
```bash
# 从 HTTPS 切换为 SSH 协议
git remote set-url origin git@github.com:user/repo.git
```

---

**基本写法：切换为 HTTPS 协议**
`git remote set-url origin https://github.com/<用户>/<仓库>.git`
```bash
# 从 SSH 切换为 HTTPS 协议
git remote set-url origin https://github.com/user/repo.git
```

---

**基本写法：重命名远程仓库**
`git remote rename <旧名> <新名>`
```bash
# 重命名远程仓库名称
git remote rename origin upstream
```

---

## 删除远程仓库

**基本写法：删除远程仓库**
`git remote remove <名称>`
```bash
# 移除指定的远程仓库关联
git remote remove origin
```

---

**基本写法：删除远程仓库（rm 简写）**
`git remote rm <名称>`
```bash
# remove 的简写形式
git remote rm origin
```

---

**基本写法：删除后重新添加**
`git remote remove origin && git remote add origin <新URL>`
```bash
# 移除旧关联并添加新远程
git remote remove origin && git remote add origin https://github.com/user/new.git
```

---

## 远程分支管理

**基本写法：查看远程分支列表**
`git branch -r`
```bash
# 列出所有远程分支
git branch -r
```

---

**基本写法：清理无效远程分支**
`git remote prune origin`
```bash
# 清理本地中已不存在的远程分支引用
git remote prune origin
```

---

**基本写法：拉取时自动清理**
`git fetch --prune`
```bash
# 拉取远程更新同时清理无效分支
git fetch --prune
```

---

**基本写法：查看需要清理的分支**
`git remote prune origin --dry-run`
```bash
# 预览将被清理的分支（不实际执行）
git remote prune origin --dry-run
```

---

## Fork 工作流

**基本写法：克隆自己的 fork**
`git clone <自己的fork仓库URL>`
```bash
# 克隆自己 fork 的仓库
git clone https://github.com/yourname/repo.git
```

---

**基本写法：添加上游仓库**
`git remote add upstream <原仓库URL>`
```bash
# 添加原仓库作为 upstream
git remote add upstream https://github.com/original/repo.git
```

---

**基本写法：从上游同步**
`git fetch upstream`
```bash
# 获取上游仓库的更新
git fetch upstream
```

---

**基本写法：合并上游主分支**
`git merge upstream/main`
```bash
# 将上游 main 分支合并到本地
git merge upstream/main
```

---

**基本写法：推送同步到自己的 fork**
`git push origin main`
```bash
# 将同步后的代码推送到自己的 fork
git push origin main
```

---

## 凭证管理

**基本写法：缓存凭证（内存）**
`git config --global credential.helper cache`
```bash
# 临时缓存 Git 凭证避免重复输入
git config --global credential.helper cache
```

---

**基本写法：设置缓存时间**
`git config --global credential.helper 'cache --timeout=3600'`
```bash
# 缓存凭证 1 小时
git config --global credential.helper 'cache --timeout=3600'
```

---

**基本写法：永久存储凭证**
`git config --global credential.helper store`
```bash
# 永久存储凭证到磁盘（明文）
git config --global credential.helper store
```

---

**基本写法：Windows 凭证管理器**
`git config --global credential.helper manager`
```bash
# 使用 Windows 凭证管理器存储
git config --global credential.helper manager
```

---

**基本写法：macOS 钥匙串**
`git config --global credential.helper osxkeychain`
```bash
# 使用 macOS 钥匙串存储凭证
git config --global credential.helper osxkeychain
```



<!-- ============ 文档分隔线：004-github/009-GitHistoryLog.md ============ -->

# GitHub 历史与日志

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 提交历史查看

**基本写法：查看完整历史**
`git log`
```bash
# 查看完整提交历史
git log
```

---

**基本写法：单行简洁显示**
`git log --oneline`
```bash
# 每条提交一行显示
git log --oneline
```

---

**基本写法：图形化分支显示**
`git log --graph`
```bash
# 图形化显示分支合并历史
git log --graph
```

---

**基本写法：完整图形化显示**
`git log --oneline --graph --all`
```bash
# 图形化显示所有分支的简洁历史
git log --oneline --graph --all
```

---

**基本写法：查看最近 N 条提交**
`git log -<数量>`
```bash
# 查看最近 10 条提交
git log -10
```

---

**基本写法：查看指定数量并单行**
`git log -<数量> --oneline`
```bash
# 单行查看最近 5 条提交
git log -5 --oneline
```

---

## 历史筛选

**基本写法：按作者筛选**
`git log --author="<作者>"`
```bash
# 查看指定作者的提交
git log --author="zhangsan"
```

---

**基本写法：按提交信息搜索**
`git log --grep="<关键词>"`
```bash
# 搜索提交信息含关键词的提交
git log --grep="登录"
```

---

**基本写法：按日期筛选**
`git log --since="<开始日期>" --until="<结束日期>"`
```bash
# 查看指定日期范围的提交
git log --since="2026-01-01" --until="2026-07-31"
```

---

**基本写法：相对日期筛选**
`git log --since="<时间>"`
```bash
# 查看最近 2 周的提交
git log --since="2 weeks ago"
```

---

**基本写法：按文件筛选**
`git log -- <文件路径>`
```bash
# 查看指定文件的提交历史
git log -- src/index.js
```

---

**基本写法：按代码变更搜索**
`git log -S "<代码片段>"`
```bash
# 搜索添加或删除指定代码的提交
git log -S "console.log"
```

---

**基本写法：按正则搜索代码**
`git log -G "<正则表达式>"`
```bash
# 使用正则搜索代码变更
git log -G "function\s+login"
```

---

## 差异查看

**基本写法：查看工作区差异**
`git diff`
```bash
# 查看工作区与暂存区的差异
git diff
```

---

**基本写法：查看暂存区差异**
`git diff --staged`
```bash
# 查看暂存区与上次提交的差异
git diff --staged
```

---

**基本写法：查看所有改动**
`git diff HEAD`
```bash
# 查看工作区与上次提交的所有差异
git diff HEAD
```

---

**基本写法：查看指定文件差异**
`git diff <文件>`
```bash
# 查看指定文件的改动
git diff src/index.js
```

---

**基本写法：比较两个提交**
`git diff <提交1> <提交2>`
```bash
# 查看两个提交之间的差异
git diff abc1234 def5678
```

---

**基本写法：比较两个分支**
`git diff <分支1>..<分支2>`
```bash
# 查看两个分支之间的差异
git diff main..feature
```

---

**基本写法：三点差异比较**
`git diff <分支1>...<分支2>`
```bash
# 查看分支2 相对共同祖先的差异
git diff main...feature
```

---

**基本写法：仅查看文件名**
`git diff --name-only`
```bash
# 仅列出有改动的文件名
git diff --name-only
```

---

**基本写法：查看改动统计**
`git diff --stat`
```bash
# 显示文件改动行数统计
git diff --stat
```

---

## 文件历史分析

**基本写法：查看文件改动历史**
`git log -p <文件>`
```bash
# 查看文件的每次改动内容
git log -p src/index.js
```

---

**基本写法：查看文件改动（含重命名）**
`git log --follow -p <文件>`
```bash
# 跟踪文件重命名前的历史
git log --follow -p src/index.js
```

---

**基本写法：查看每行最后修改者**
`git blame <文件>`
```bash
# 显示文件每行最后的修改者
git blame src/index.js
```

---

**基本写法：查看指定行范围的 blame**
`git blame -L <起始>,<结束> <文件>`
```bash
# 查看 10 到 20 行的最后修改者
git blame -L 10,20 src/index.js
```

---

**基本写法：查看 blame 忽略空格**
`git blame -w <文件>`
```bash
# blame 时忽略空格改动
git blame -w src/index.js
```

---

## 提交详情

**基本写法：查看指定提交**
`git show <提交ID>`
```bash
# 查看指定提交的详情和改动
git show abc1234
```

---

**基本写法：查看提交的文件列表**
`git show --stat <提交ID>`
```bash
# 查看提交修改的文件列表
git show --stat abc1234
```

---

**基本写法：查看提交的指定文件**
`git show <提交ID>:<文件路径>`
```bash
# 查看指定提交中某文件的内容
git show abc1234:src/index.js
```

---

**基本写法：查看最近提交**
`git show HEAD`
```bash
# 查看最近一次提交的详情
git show HEAD
```

---

**基本写法：查看上一次提交**
`git show HEAD~1`
```bash
# 查看倒数第二次提交
git show HEAD~1
```

---

## 引用日志

**基本写法：查看引用日志**
`git reflog`
```bash
# 查看 HEAD 的变更历史
git reflog
```

---

**基本写法：查看指定分支引用日志**
`git reflog <分支名>`
```bash
# 查看指定分支的引用日志
git reflog feature
```

---

**基本写法：查看所有引用日志**
`git reflog --all`
```bash
# 查看所有引用的变更历史
git reflog --all
```

---

**基本写法：恢复到引用日志的提交**
`git reset --hard <引用日志ID>`
```bash
# 重置到引用日志记录的某个状态
git reset --hard HEAD@{2}
```

---

**基本写法：查看引用日志的相对引用**
`git show HEAD@{<n>}`
```bash
# 查看引用日志中第 n 个状态
git show HEAD@{3}
```



<!-- ============ 文档分隔线：004-github/010-GitStashReset.md ============ -->

# GitHub 暂存与回退

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 暂存改动

**基本写法：暂存当前改动**
`git stash`
```bash
# 暂存工作区和暂存区的改动
git stash
```

---

**基本写法：暂存并添加说明**
`git stash push -m "<说明>"`
```bash
# 暂存改动并附上描述信息
git stash push -m "登录功能开发中"
```

---

**基本写法：包含未跟踪文件**
`git stash -u`
```bash
# 暂存改动同时包含未跟踪文件
git stash -u
```

---

**基本写法：包含所有文件**
`git stash -a`
```bash
# 暂存所有改动（含忽略文件）
git stash -a
```

---

**基本写法：保留暂存区**
`git stash --keep-index`
```bash
# 暂存改动但保留暂存区内容
git stash --keep-index
```

---

## 查看暂存

**基本写法：查看暂存列表**
`git stash list`
```bash
# 列出所有暂存的改动
git stash list
```

---

**基本写法：查看暂存详情**
`git stash show stash@{<索引>}`
```bash
# 查看指定暂存的改动摘要
git stash show stash@{0}
```

---

**基本写法：查看暂存差异详情**
`git stash show -p stash@{<索引>}`
```bash
# 查看指定暂存的完整差异
git stash show -p stash@{0}
```

---

**基本写法：查看最近暂存详情**
`git stash show`
```bash
# 查看最近一次暂存的改动摘要
git stash show
```

---

## 恢复暂存

**基本写法：恢复最近暂存**
`git stash pop`
```bash
# 恢复最近暂存并删除该暂存记录
git stash pop
```

---

**基本写法：恢复指定暂存**
`git stash pop stash@{<索引>}`
```bash
# 恢复指定索引的暂存
git stash pop stash@{1}
```

---

**基本写法：恢复但不删除暂存**
`git stash apply`
```bash
# 恢复最近暂存但保留暂存记录
git stash apply
```

---

**基本写法：恢复指定暂存不删除**
`git stash apply stash@{<索引>}`
```bash
# 恢复指定暂存但保留记录
git stash apply stash@{1}
```

---

## 删除暂存

**基本写法：删除指定暂存**
`git stash drop stash@{<索引>}`
```bash
# 删除指定索引的暂存记录
git stash drop stash@{0}
```

---

**基本写法：清空所有暂存**
`git stash clear`
```bash
# 删除所有暂存记录
git stash clear
```

---

**基本写法：从暂存创建分支**
`git stash branch <分支名> stash@{<索引>}`
```bash
# 基于暂存创建新分支并恢复改动
git stash branch feature/recovery stash@{0}
```

---

## 撤销工作区改动

**基本写法：撤销工作区修改**
`git restore <文件>`
```bash
# 恢复文件到上次提交的状态
git restore index.js
```

---

**基本写法：checkout 撤销修改**
`git checkout -- <文件>`
```bash
# 旧写法撤销工作区修改
git checkout -- index.js
```

---

**基本写法：撤销所有修改**
`git restore .`
```bash
# 撤销当前目录所有改动
git restore .
```

---

**基本写法：取消暂存**
`git restore --staged <文件>`
```bash
# 将文件从暂存区移回工作区
git restore --staged index.js
```

---

**基本写法：取消所有暂存**
`git restore --staged .`
```bash
# 将所有文件从暂存区移回工作区
git restore --staged .
```

---

## 回退提交

**基本写法：软回退（保留改动）**
`git reset --soft HEAD~1`
```bash
# 撤销上次提交保留改动在暂存区
git reset --soft HEAD~1
```

---

**基本写法：混合回退（默认）**
`git reset --mixed HEAD~1`
```bash
# 撤销上次提交保留改动在工作区
git reset --mixed HEAD~1
```

---

**基本写法：硬回退（丢弃改动）**
`git reset --hard HEAD~1`
```bash
# 撤销上次提交并丢弃所有改动
git reset --hard HEAD~1
```

---

**基本写法：回退到指定提交**
`git reset --hard <提交ID>`
```bash
# 强制回退到指定提交
git reset --hard abc1234
```

---

**基本写法：回退单个文件**
`git reset HEAD~1 <文件>`
```bash
# 仅回退指定文件到上次提交状态
git reset HEAD~1 src/index.js
```

---

**基本写法：回退到远程分支状态**
`git reset --hard origin/<分支名>`
```bash
# 重置本地分支到远程分支状态
git reset --hard origin/main
```

---

## 反向提交

**基本写法：创建反向提交**
`git revert <提交ID>`
```bash
# 创建一个新提交撤销指定提交的改动
git revert abc1234
```

---

**基本写法：反向提交不自动提交**
`git revert -n <提交ID>`
```bash
# 反向提交但不自动创建提交
git revert -n abc1234
```

---

**基本写法：反向多个提交**
`git revert <提交1>..<提交2>`
```bash
# 反向指定范围内的提交
git revert abc1234..def5678
```

---

**基本写法：反向最近提交**
`git revert HEAD`
```bash
# 撤销最近一次提交
git revert HEAD
```

---

## 清理未跟踪文件

**基本写法：查看将被清理的文件**
`git clean -n`
```bash
# 预览将被删除的未跟踪文件
git clean -n
```

---

**基本写法：删除未跟踪文件**
`git clean -f`
```bash
# 强制删除未跟踪的文件
git clean -f
```

---

**基本写法：删除未跟踪目录**
`git clean -fd`
```bash
# 删除未跟踪的文件和目录
git clean -fd
```

---

**基本写法：包含忽略文件清理**
`git clean -fdx`
```bash
# 删除所有未跟踪文件含忽略文件
git clean -fdx
```

---

**基本写法：交互式清理**
`git clean -i`
```bash
# 交互式选择要删除的文件
git clean -i
```



<!-- ============ 文档分隔线：004-github/011-GhCliAuth.md ============ -->

# GitHub CLI 认证配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## gh 安装

**基本写法：winget 安装 gh**
`winget install GitHub.cli`
```bash
# 通过 Windows 包管理器安装 GitHub CLI
winget install GitHub.cli
```

---

**基本写法：Homebrew 安装 gh**
`brew install gh`
```bash
# macOS 通过 Homebrew 安装
brew install gh
```

---

**基本写法：apt 安装 gh（Ubuntu）**
`sudo apt install gh`
```bash
# Ubuntu 系统安装 GitHub CLI
sudo apt install gh
```

---

**基本写法：升级 gh**
`winget upgrade GitHub.cli`
```bash
# 升级到最新版本
winget upgrade GitHub.cli
```

---

**基本写法：验证安装**
`gh --version`
```bash
# 查看 gh 版本验证安装
gh --version
```

---

## 认证登录

**基本写法：交互式登录**
`gh auth login`
```bash
# 通过浏览器交互式登录 GitHub
gh auth login
```

---

**基本写法：使用 token 登录**
`gh auth login --with-token < <token文件>`
```bash
# 通过 token 文件登录（适合脚本）
gh auth login --with-token < token.txt
```

---

**基本写法：通过环境变量登录**
`export GH_TOKEN=<token>`
```bash
# 设置环境变量后 gh 自动认证
export GH_TOKEN=ghp_xxxxxxxxxxxx
```

---

**基本写法：指定企业版登录**
`gh auth login --hostname <企业域名>`
```bash
# 登录 GitHub 企业版
gh auth login --hostname github.example.com
```

---

## 认证状态

**基本写法：查看认证状态**
`gh auth status`
```bash
# 查看当前登录状态和账户
gh auth status
```

---

**基本写法：查看 token**
`gh auth status --show-token`
```bash
# 查看认证状态并显示 token
gh auth status --show-token
```

---

**基本写法：获取当前 token**
`gh auth token`
```bash
# 输出当前 token 用于脚本
gh auth token
```

---

**基本写法：刷新 token 权限**
`gh auth refresh`
```bash
# 刷新凭证添加新的权限范围
gh auth refresh
```

---

**基本写法：添加指定权限**
`gh auth refresh -s <权限>`
```bash
# 添加 repo 和 workflow 权限
gh auth refresh -s repo,workflow
```

---

## 账户管理

**基本写法：切换账户**
`gh auth switch`
```bash
# 交互式切换到其他账户
gh auth switch
```

---

**基本写法：切换到指定账户**
`gh auth switch --user <用户名>`
```bash
# 切换到指定用户账户
gh auth switch --user alice
```

---

**基本写法：登出**
`gh auth logout`
```bash
# 登出当前 GitHub 账户
gh auth logout
```

---

**基本写法：登出指定账户**
`gh auth logout --user <用户名>`
```bash
# 登出指定用户账户
gh auth logout --user alice
```

---

## SSH 密钥管理

**基本写法：上传 SSH 密钥**
`gh ssh-key add <密钥文件>`
```bash
# 上传公钥到 GitHub 账户
gh ssh-key add ~/.ssh/id_ed25519.pub
```

---

**基本写法：上传并添加标题**
`gh ssh-key add <密钥文件> --title "<标题>"`
```bash
# 上传公钥并设置标题
gh ssh-key add ~/.ssh/id_ed25519.pub --title "我的笔记本"
```

---

**基本写法：查看已上传的密钥**
`gh ssh-key list`
```bash
# 列出 GitHub 账户中的所有 SSH 密钥
gh ssh-key list
```

---

**基本写法：删除 SSH 密钥**
`gh ssh-key delete <密钥ID>`
```bash
# 删除指定的 SSH 密钥
gh ssh-key delete 12345
```

---

## 配置管理

**基本写法：设置默认编辑器**
`gh config set editor "<编辑器命令>"`
```bash
# 设置 VS Code 为默认编辑器
gh config set editor "code --wait"
```

---

**基本写法：设置默认浏览器**
`gh config set browser "<浏览器>"`
```bash
# 设置 Firefox 为默认浏览器
gh config set browser firefox
```

---

**基本写法：设置默认协议**
`gh config set git_protocol <协议>`
```bash
# 设置默认 Git 协议为 SSH
gh config set git_protocol ssh
```

---

**基本写法：查看配置**
`gh config get <配置项>`
```bash
# 查看指定配置项的值
gh config get editor
```

---

**基本写法：查看所有配置**
`gh config list`
```bash
# 列出所有 gh 配置
gh config list
```

---

## 帮助与参考

**基本写法：查看 gh 帮助**
`gh --help`
```bash
# 查看 gh 顶层帮助
gh --help
```

---

**基本写法：查看命令帮助**
`gh <命令> --help`
```bash
# 查看指定命令的详细帮助
gh pr --help
```

---

**基本写法：查看命令参考**
`gh reference`
```bash
# 输出所有命令的完整参考
gh reference
```

---

**基本写法：在浏览器中打开**
`gh <命令> --web`
```bash
# 在浏览器中打开对应页面
gh repo view --web
```



<!-- ============ 文档分隔线：004-github/012-GhPrManage.md ============ -->

# GitHub CLI PR 管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 PR

**基本写法：交互式创建 PR**
`gh pr create`
```bash
# 通过交互式提示创建 PR
gh pr create
```

---

**基本写法：指定标题和正文**
`gh pr create --title "<标题>" --body "<正文>"`
```bash
# 直接指定 PR 标题和描述
gh pr create --title "feat: 添加用户认证" --body "实现 OAuth 登录流程"
```

---

**基本写法：使用提交信息填充**
`gh pr create --fill`
```bash
# 使用最近提交信息填充标题和正文
gh pr create --fill
```

---

**基本写法：创建草稿 PR**
`gh pr create --draft --title "<标题>"`
```bash
# 创建草稿 PR 待完善后再标记就绪
gh pr create --draft --title "WIP: 重构认证模块"
```

---

**基本写法：指定基础分支**
`gh pr create --base <分支> --head <分支>`
```bash
# 指定目标分支和源分支
gh pr create --base main --head feature/login
```

---

**基本写法：指定指派人**
`gh pr create --assignee <用户>`
```bash
# 创建 PR 并指派审查人
gh pr create --assignee @me
```

---

**基本写法：添加标签和审查人**
`gh pr create --label "<标签>" --reviewer <用户>`
```bash
# 创建 PR 并添加标签和审查人
gh pr create --label "需要审查" --reviewer alice
```

---

## 查看 PR

**基本写法：列出当前仓库 PR**
`gh pr list`
```bash
# 列出当前仓库的 PR
gh pr list
```

---

**基本写法：列出指定状态 PR**
`gh pr list --state <状态>`
```bash
# 列出指定状态的 PR
gh pr list --state open
```

---

**基本写法：查看自己的 PR**
`gh pr list --author @me`
```bash
# 列出自己创建的 PR
gh pr list --author @me
```

---

**基本写法：查看待审查 PR**
`gh pr list --reviewer @me`
```bash
# 列出等待自己审查的 PR
gh pr list --reviewer @me
```

---

**基本写法：按标签筛选**
`gh pr list --label "<标签>"`
```bash
# 按标签筛选 PR
gh pr list --label "bug"
```

---

**基本写法：限制返回数量**
`gh pr list --limit <数量>`
```bash
# 限制返回的 PR 数量
gh pr list --limit 50
```

---

**基本写法：查看 PR 详情**
`gh pr view <编号>`
```bash
# 查看指定 PR 的详细信息
gh pr view 42
```

---

**基本写法：在浏览器中查看**
`gh pr view <编号> --web`
```bash
# 在浏览器中打开 PR 页面
gh pr view 42 --web
```

---

## PR 代码审查

**基本写法：查看 PR 差异**
`gh pr diff <编号>`
```bash
# 查看 PR 的代码差异
gh pr diff 42
```

---

**基本写法：查看变更文件列表**
`gh pr diff <编号> --name-only`
```bash
# 仅列出 PR 变更的文件名
gh pr diff 42 --name-only
```

---

**基本写法：检出 PR 到本地**
`gh pr checkout <编号>`
```bash
# 检出 PR 分支到本地进行测试
gh pr checkout 42
```

---

**基本写法：强制检出 PR**
`gh pr checkout <编号> --force`
```bash
# 有本地改动时强制检出 PR
gh pr checkout 42 --force
```

---

**基本写法：查看检查状态**
`gh pr checks <编号>`
```bash
# 查看 PR 的 CI 检查状态
gh pr checks 42
```

---

**基本写法：等待检查完成**
`gh pr checks <编号> --watch`
```bash
# 实时监控 PR 检查状态直到完成
gh pr checks 42 --watch
```

---

**基本写法：仅查看必需检查**
`gh pr checks <编号> --required`
```bash
# 仅显示必需通过的检查
gh pr checks 42 --required
```

---

## 提交审查

**基本写法：批准 PR**
`gh pr review <编号> --approve --body "<评论>"`
```bash
# 批准 PR 并附带评论
gh pr review 42 --approve --body "代码质量很好"
```

---

**基本写法：请求修改**
`gh pr review <编号> --request-changes --body "<意见>"`
```bash
# 请求修改并说明原因
gh pr review 42 --request-changes --body "需要补充单元测试"
```

---

**基本写法：评论 PR**
`gh pr review <编号> --comment --body "<评论>"`
```bash
# 仅评论不批准也不拒绝
gh pr review 42 --comment --body "建议优化命名"
```

---

**基本写法：添加行内评论**
`gh api repos/<owner>/<repo>/pulls/<编号>/reviews --input -`
```bash
# 通过 API 提交带行内评论的审查
gh api repos/owner/repo/pulls/42/reviews --input - <<'EOF'
{"event":"COMMENT","body":"总体不错","comments":[{"path":"src/app.js","line":42,"side":"RIGHT","body":"建议使用常量"}]}
EOF
```

---

## PR 评论

**基本写法：添加评论**
`gh pr comment <编号> --body "<评论>"`
```bash
# 在 PR 中添加评论
gh pr comment 42 --body "已修复请重新审查"
```

---

**基本写法：查看评论列表**
`gh api repos/<owner>/<repo>/issues/<编号>/comments`
```bash
# 通过 API 查看 PR 评论
gh api repos/owner/repo/issues/42/comments
```

---

## 合并 PR

**基本写法：合并 PR（默认方式）**
`gh pr merge <编号>`
```bash
# 合并指定 PR
gh pr merge 42
```

---

**基本写法：压缩合并**
`gh pr merge <编号> --squash`
```bash
# 使用 squash 方式合并 PR
gh pr merge 42 --squash
```

---

**基本写法：变基合并**
`gh pr merge <编号> --rebase`
```bash
# 使用 rebase 方式合并 PR
gh pr merge 42 --rebase
```

---

**基本写法：合并并删除分支**
`gh pr merge <编号> --squash --delete-branch`
```bash
# 合并 PR 后删除源分支
gh pr merge 42 --squash --delete-branch
```

---

**基本写法：自动合并**
`gh pr merge <编号> --auto --squash`
```bash
# 检查通过后自动合并
gh pr merge 42 --auto --squash
```

---

## PR 状态管理

**基本写法：关闭 PR**
`gh pr close <编号>`
```bash
# 关闭指定 PR
gh pr close 42
```

---

**基本写法：关闭并添加评论**
`gh pr close <编号> --comment "<评论>"`
```bash
# 关闭 PR 并附带说明
gh pr close 42 --comment "不再需要此功能"
```

---

**基本写法：重新打开 PR**
`gh pr reopen <编号>`
```bash
# 重新打开已关闭的 PR
gh pr reopen 42
```

---

**基本写法：草稿转就绪**
`gh pr ready <编号>`
```bash
# 将草稿 PR 标记为就绪状态
gh pr ready 42
```

---

**基本写法：就绪转草稿**
`gh pr ready <编号> --undo`
```bash
# 将就绪 PR 转回草稿状态
gh pr ready 42 --undo
```

---

**基本写法：更新 PR 分支**
`gh pr update-branch <编号>`
```bash
# 用基础分支更新 PR 分支
gh pr update-branch 42
```

---

**基本写法：编辑 PR**
`gh pr edit <编号> --add-label "<标签>"`
```bash
# 为 PR 添加标签
gh pr edit 42 --add-label "优先级高"
```

---

**基本写法：添加审查人**
`gh pr edit <编号> --add-reviewer <用户>`
```bash
# 为 PR 添加审查人
gh pr edit 42 --add-reviewer alice
```



<!-- ============ 文档分隔线：004-github/013-GhIssueManage.md ============ -->

# GitHub CLI Issue 管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Issue

**基本写法：交互式创建 Issue**
`gh issue create`
```bash
# 通过交互式提示创建 Issue
gh issue create
```

---

**基本写法：指定标题和正文**
`gh issue create --title "<标题>" --body "<正文>"`
```bash
# 直接指定 Issue 标题和描述
gh issue create --title "Bug: 登录页面报错" --body "点击登录按钮无响应"
```

---

**基本写法：从文件读取正文**
`gh issue create --title "<标题>" --body-file <文件>`
```bash
# 从文件读取 Issue 正文内容
gh issue create --title "性能优化" --body-file issue-template.md
```

---

**基本写法：指定指派人**
`gh issue create --assignee <用户>`
```bash
# 创建 Issue 并指派处理人
gh issue create --title "修复 bug" --assignee @me
```

---

**基本写法：添加标签**
`gh issue create --label "<标签>"`
```bash
# 创建 Issue 并添加标签
gh issue create --title "新功能" --label "enhancement"
```

---

**基本写法：指定里程碑**
`gh issue create --milestone "<里程碑>"`
```bash
# 创建 Issue 并关联里程碑
gh issue create --title "任务" --milestone "v1.0"
```

---

**基本写法：在浏览器中创建**
`gh issue create --web`
```bash
# 打开浏览器创建 Issue
gh issue create --web
```

---

## 查看 Issue

**基本写法：列出当前仓库 Issue**
`gh issue list`
```bash
# 列出当前仓库的 Issue
gh issue list
```

---

**基本写法：列出指定状态**
`gh issue list --state <状态>`
```bash
# 列出指定状态的 Issue
gh issue list --state open
```

---

**基本写法：列出已关闭 Issue**
`gh issue list --state closed`
```bash
# 列出已关闭的 Issue
gh issue list --state closed
```

---

**基本写法：查看指派给自己的 Issue**
`gh issue list --assignee @me`
```bash
# 列出指派给自己的 Issue
gh issue list --assignee @me
```

---

**基本写法：查看自己创建的 Issue**
`gh issue list --author @me`
```bash
# 列出自己创建的 Issue
gh issue list --author @me
```

---

**基本写法：按标签筛选**
`gh issue list --label "<标签>"`
```bash
# 按标签筛选 Issue
gh issue list --label "bug"
```

---

**基本写法：限制返回数量**
`gh issue list --limit <数量>`
```bash
# 限制返回的 Issue 数量
gh issue list --limit 30
```

---

**基本写法：查看 Issue 详情**
`gh issue view <编号>`
```bash
# 查看指定 Issue 的详细信息
gh issue view 42
```

---

**基本写法：在浏览器中查看**
`gh issue view <编号> --web`
```bash
# 在浏览器中打开 Issue 页面
gh issue view 42 --web
```

---

**基本写法：查看 Issue 评论**
`gh issue view <编号> --comments`
```bash
# 查看 Issue 及其评论内容
gh issue view 42 --comments
```

---

## Issue 评论

**基本写法：添加评论**
`gh issue comment <编号> --body "<评论>"`
```bash
# 在 Issue 中添加评论
gh issue comment 42 --body "已复现此问题"
```

---

**基本写法：从文件读取评论**
`gh issue comment <编号> --body-file <文件>`
```bash
# 从文件读取评论内容
gh issue comment 42 --body-file comment.md
```

---

**基本写法：编辑评论**
`gh api repos/<owner>/<repo>/issues/comments/<评论ID> -X PATCH -f body="<新内容>"`
```bash
# 通过 API 编辑指定评论
gh api repos/owner/repo/issues/comments/123 -X PATCH -f body="更新后的评论"
```

---

**基本写法：删除评论**
`gh api repos/<owner>/<repo>/issues/comments/<评论ID> -X DELETE`
```bash
# 通过 API 删除指定评论
gh api repos/owner/repo/issues/comments/123 -X DELETE
```

---

## Issue 状态管理

**基本写法：关闭 Issue**
`gh issue close <编号>`
```bash
# 关闭指定 Issue
gh issue close 42
```

---

**基本写法：关闭并添加评论**
`gh issue close <编号> --comment "<评论>"`
```bash
# 关闭 Issue 并附带说明
gh issue close 42 --comment "已在 v1.2 修复"
```

---

**基本写法：关闭并指定原因**
`gh issue close <编号> --reason <原因>`
```bash
# 关闭 Issue 并指定关闭原因
gh issue close 42 --reason "not planned"
```

---

**基本写法：重新打开 Issue**
`gh issue reopen <编号>`
```bash
# 重新打开已关闭的 Issue
gh issue reopen 42
```

---

## 编辑 Issue

**基本写法：修改标题**
`gh issue edit <编号> --title "<新标题>"`
```bash
# 修改 Issue 标题
gh issue edit 42 --title "Bug: 登录页面 500 错误"
```

---

**基本写法：修改正文**
`gh issue edit <编号> --body "<新正文>"`
```bash
# 修改 Issue 正文内容
gh issue edit 42 --body "更新后的描述"
```

---

**基本写法：添加标签**
`gh issue edit <编号> --add-label "<标签>"`
```bash
# 为 Issue 添加标签
gh issue edit 42 --add-label "优先级高"
```

---

**基本写法：移除标签**
`gh issue edit <编号> --remove-label "<标签>"`
```bash
# 移除 Issue 的标签
gh issue edit 42 --remove-label "优先级高"
```

---

**基本写法：添加指派人**
`gh issue edit <编号> --add-assignee <用户>`
```bash
# 为 Issue 添加处理人
gh issue edit 42 --add-assignee alice
```

---

**基本写法：移除指派人**
`gh issue edit <编号> --remove-assignee <用户>`
```bash
# 移除 Issue 的处理人
gh issue edit 42 --remove-assignee alice
```

---

## 批量操作

**基本写法：批量关闭 Issue**
`gh issue list --label "<标签>" --json number --jq ".[].number" | xargs -I {} gh issue close {}`
```bash
# 批量关闭指定标签的 Issue
gh issue list --label "wontfix" --json number --jq ".[].number" | xargs -I {} gh issue close {}
```

---

**基本写法：批量添加标签**
`gh issue list --state open --json number --jq ".[].number" | xargs -I {} gh issue edit {} --add-label "需要审查"`
```bash
# 为所有打开的 Issue 添加标签
gh issue list --state open --json number --jq ".[].number" | xargs -I {} gh issue edit {} --add-label "需要审查"
```

---

## Issue 传输与开发

**基本写法：将 Issue 转为分支开发**
`gh issue develop <编号>`
```bash
# 基于 Issue 创建开发分支
gh issue develop 42
```

---

**基本写法：指定分支名开发**
`gh issue develop <编号> -b <分支名>`
```bash
# 为 Issue 创建指定名称的分支
gh issue develop 42 -b fix/login-error
```

---

**基本写法：查看 Issue 关联的 PR**
`gh issue view <编号> --json trackedIssues`
```bash
# 查看 Issue 关联的追踪问题
gh issue view 42 --json trackedIssues
```

---

## JSON 输出

**基本写法：输出 JSON 格式**
`gh issue list --json <字段>`
```bash
# 以 JSON 格式输出指定字段
gh issue list --json number,title,state
```

---

**基本写法：使用 jq 过滤**
`gh issue list --json number,title | jq ".[] | select(.title | contains(\"bug\"))"`
```bash
# 使用 jq 过滤标题含 bug 的 Issue
gh issue list --json number,title | jq ".[] | select(.title | contains(\"bug\"))"
```

---

**基本写法：使用模板输出**
`gh issue list --template "<模板>"`
```bash
# 使用 Go 模板自定义输出格式
gh issue list --template "{{range .}}#{{.number}} {{.title}}{{end}}"
```



<!-- ============ 文档分隔线：004-github/014-GhRepoManage.md ============ -->

# GitHub CLI 仓库管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建仓库

**基本写法：创建公开仓库**
`gh repo create <仓库名> --public`
```bash
# 创建公开仓库
gh repo create myproject --public
```

---

**基本写法：创建私有仓库**
`gh repo create <仓库名> --private`
```bash
# 创建私有仓库
gh repo create myproject --private
```

---

**基本写法：创建并克隆**
`gh repo create <仓库名> --clone`
```bash
# 创建仓库并克隆到本地
gh repo create myproject --public --clone
```

---

**基本写法：从本地目录创建远程仓库**
`gh repo create <仓库名> --source <目录> --push`
```bash
# 基于本地目录创建远程仓库并推送
gh repo create myproject --source . --push
```

---

**基本写法：指定组织创建**
`gh repo create <组织>/<仓库名>`
```bash
# 在指定组织下创建仓库
gh repo create myorg/myproject --private
```

---

**基本写法：创建并添加描述**
`gh repo create <仓库名> --description "<描述>"`
```bash
# 创建仓库并添加描述
gh repo create myproject --description "我的项目"
```

---

**基本写法：创建带 README 的仓库**
`gh repo create <仓库名> --add-readme`
```bash
# 创建仓库并自动添加 README
gh repo create myproject --public --add-readme
```

---

## 查看仓库

**基本写法：查看当前仓库**
`gh repo view`
```bash
# 查看当前目录对应的仓库信息
gh repo view
```

---

**基本写法：查看指定仓库**
`gh repo view <owner>/<repo>`
```bash
# 查看指定仓库的详情
gh repo view facebook/react
```

---

**基本写法：在浏览器中查看**
`gh repo view --web`
```bash
# 在浏览器中打开仓库页面
gh repo view --web
```

---

**基本写法：查看仓库 README**
`gh repo view <owner>/<repo>`
```bash
# 查看 README 内容
gh repo view microsoft/vscode
```

---

**基本写法：列出自己的仓库**
`gh repo list`
```bash
# 列出自己账户下的仓库
gh repo list
```

---

**基本写法：列出指定用户仓库**
`gh repo list <用户名>`
```bash
# 列出指定用户的公开仓库
gh repo list torvalds
```

---

**基本写法：列出组织仓库**
`gh repo list <组织名>`
```bash
# 列出指定组织的仓库
gh repo list microsoft
```

---

**基本写法：限制返回数量**
`gh repo list --limit <数量>`
```bash
# 限制返回的仓库数量
gh repo list --limit 100
```

---

**基本写法：按语言筛选**
`gh repo list --language <语言>`
```bash
# 按编程语言筛选仓库
gh repo list --language TypeScript
```

---

## 克隆与 Fork

**基本写法：克隆仓库**
`gh repo clone <owner>/<repo>`
```bash
# 克隆指定仓库到本地
gh repo clone facebook/react
```

---

**基本写法：克隆当前仓库**
`gh repo clone`
```bash
# 克隆当前目录对应的仓库
gh repo clone
```

---

**基本写法：克隆到指定目录**
`gh repo clone <owner>/<repo> <目录>`
```bash
# 克隆仓库到指定目录名
gh repo clone facebook/react myreact
```

---

**基本写法：Fork 仓库**
`gh repo fork <owner>/<repo>`
```bash
# Fork 指定仓库到自己的账户
gh repo fork facebook/react
```

---

**基本写法：Fork 并克隆**
`gh repo fork <owner>/<repo> --clone`
```bash
# Fork 仓库并克隆到本地
gh repo fork facebook/react --clone
```

---

**基本写法：Fork 并添加远程**
`gh repo fork <owner>/<repo> --remote`
```bash
# Fork 仓库并自动添加原仓库为 upstream
gh repo fork facebook/react --remote
```

---

**基本写法：指定 upstream 名称**
`gh repo fork <owner>/<repo> --remote --remote-name <名称>`
```bash
# Fork 并自定义 upstream 远程名
gh repo fork facebook/react --remote --remote-name upstream
```

---

## 仓库编辑

**基本写法：修改仓库描述**
`gh repo edit --description "<描述>"`
```bash
# 修改当前仓库的描述
gh repo edit --description "更新后的项目描述"
```

---

**基本写法：修改主页 URL**
`gh repo edit --homepage "<URL>"`
```bash
# 设置仓库的主页地址
gh repo edit --homepage "https://myproject.com"
```

---

**基本写法：修改可见性为私有**
`gh repo edit --visibility private`
```bash
# 将仓库改为私有
gh repo edit --visibility private
```

---

**基本写法：修改可见性为公开**
`gh repo edit --visibility public`
```bash
# 将仓库改为公开
gh repo edit --visibility public
```

---

**基本写法：启用 Issues 功能**
`gh repo edit --enable-issues`
```bash
# 启用仓库的 Issues 功能
gh repo edit --enable-issues
```

---

**基本写法：启用 Wiki 功能**
`gh repo edit --enable-wiki`
```bash
# 启用仓库的 Wiki 功能
gh repo edit --enable-wiki
```

---

**基本写法：添加话题**
`gh repo edit --add-topic <话题>`
```bash
# 为仓库添加话题标签
gh repo edit --add-topic "javascript"
```

---

**基本写法：移除话题**
`gh repo edit --remove-topic <话题>`
```bash
# 移除仓库的话题标签
gh repo edit --remove-topic "javascript"
```

---

## 仓库同步与删除

**基本写法：同步 Fork**
`gh repo sync`
```bash
# 同步 Fork 仓库与上游
gh repo sync
```

---

**基本写法：同步指定 Fork**
`gh repo sync <owner>/<repo>`
```bash
# 同步指定的 Fork 仓库
gh repo sync myname/react
```

---

**基本写法：同步指定分支**
`gh repo sync --source <源> --branch <分支>`
```bash
# 从指定源同步指定分支
gh repo sync --source upstream --branch main
```

---

**基本写法：删除仓库**
`gh repo delete <仓库名>`
```bash
# 删除指定仓库（需确认）
gh repo delete myproject
```

---

**基本写法：删除当前仓库**
`gh repo delete`
```bash
# 删除当前目录对应的仓库
gh repo delete
```

---

**基本写法：强制删除不确认**
`gh repo delete <仓库名> --yes`
```bash
# 跳过确认直接删除
gh repo delete myproject --yes
```

---

## 归档与传输

**基本写法：归档仓库**
`gh repo archive <仓库名>`
```bash
# 将仓库设为只读归档状态
gh repo archive myproject
```

---

**基本写法：归档当前仓库**
`gh repo archive`
```bash
# 归档当前目录对应的仓库
gh repo archive
```

---

**基本写法：取消归档**
`gh repo unarchive <仓库名>`
```bash
# 取消仓库的归档状态
gh repo unarchive myproject
```

---

**基本写法：转移仓库**
`gh repo transfer <仓库> <新所有者>`
```bash
# 将仓库转移给其他用户或组织
gh repo transfer myproject myorg
```

---

## 仓库部署与发布

**基本写法：创建 Release**
`gh release create <标签名>`
```bash
# 基于标签创建发布
gh release create v1.0.0
```

---

**基本写法：创建带说明的 Release**
`gh release create <标签名> --title "<标题>" --notes "<说明>"`
```bash
# 创建发布并指定标题和说明
gh release create v1.0.0 --title "v1.0.0 正式版" --notes "首个正式版本"
```

---

**基本写法：上传附件到 Release**
`gh release upload <标签名> <文件>`
```bash
# 上传构建产物到指定发布
gh release upload v1.0.0 ./dist/app.zip
```

---

**基本写法：查看 Release 列表**
`gh release list`
```bash
# 列出仓库的所有发布
gh release list
```

---

**基本写法：下载 Release 资源**
`gh release download <标签名>`
```bash
# 下载指定发布的所有资源
gh release download v1.0.0
```

---

**基本写法：删除 Release**
`gh release delete <标签名>`
```bash
# 删除指定的发布
gh release delete v1.0.0
```



<!-- ============ 文档分隔线：004-github/015-GitHubActions.md ============ -->

# GitHub Actions 工作流配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 工作流文件结构

**基本写法：工作流文件命名**
`.github/workflows/<名称>.yml`
```bash
# 工作流文件必须放在此目录下
mkdir -p .github/workflows
```

---

**基本写法：基本工作流定义**
`name: <工作流名称>`
```yaml
# 工作流名称
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Hello"
```

---

**基本写法：触发条件配置**
`on: <触发事件>`
```yaml
# push 时触发
on:
  push:
    branches: [ main, develop ]
```

---

**基本写法：多事件触发**
`on: [<事件1>, <事件2>]`
```yaml
# 多种事件触发工作流
on: [push, pull_request, workflow_dispatch]
```

---

**基本写法：手动触发**
`on: workflow_dispatch`
```yaml
# 允许手动触发工作流
on:
  workflow_dispatch:
    inputs:
      environment:
        description: '部署环境'
        default: 'staging'
```

---

**基本写法：定时触发**
`on: schedule`
```yaml
# 每天凌晨 2 点执行（UTC 时间）
on:
  schedule:
    - cron: '0 2 * * *'
```

---

## 作业配置

**基本写法：指定运行环境**
`runs-on: <操作系统>`
```yaml
# 在最新版 Ubuntu 上运行
runs-on: ubuntu-latest
```

---

**基本写法：多操作系统矩阵**
`strategy: matrix`
```yaml
# 在多个操作系统上运行测试
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
runs-on: ${{ matrix.os }}
```

---

**基本写法：多版本矩阵**
`strategy: matrix`
```yaml
# 在多个 Node.js 版本上测试
strategy:
  matrix:
    node-version: [18, 20, 22, 24]
```

---

**基本写法：失败时继续**
`strategy: fail-fast`
```yaml
# 矩阵中一个失败不取消其他
strategy:
  fail-fast: false
  max-parallel: 4
```

---

**基本写法：作业依赖关系**
`needs: <作业名>`
```yaml
# deploy 作业依赖 build 作业
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "build"
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploy"
```

---

## 步骤与动作

**基本写法：检出代码**
`uses: actions/checkout@v4`
```yaml
# 检出仓库代码到工作目录
steps:
  - uses: actions/checkout@v4
```

---

**基本写法：设置 Node.js 环境**
`uses: actions/setup-node@v4`
```yaml
# 配置 Node.js 运行环境
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: '22'
      cache: 'npm'
```

---

**基本写法：设置 Python 环境**
`uses: actions/setup-python@v5`
```yaml
# 配置 Python 运行环境
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: '3.13'
```

---

**基本写法：设置 Java 环境**
`uses: actions/setup-java@v4`
```yaml
# 配置 JDK 环境
steps:
  - uses: actions/setup-java@v4
    with:
      distribution: 'temurin'
      java-version: '21'
```

---

**基本写法：运行命令**
`run: <命令>`
```yaml
# 执行 shell 命令
steps:
  - run: npm install
  - run: npm test
```

---

**基本写法：多行命令**
`run: |`
```yaml
# 执行多行命令
steps:
  - run: |
      npm install
      npm run build
      npm test
```

---

**基本写法：指定 shell 类型**
`shell: <shell>`
```yaml
# 指定使用 PowerShell 运行
steps:
  - run: Write-Host "Hello"
    shell: pwsh
```

---

## 环境变量与密钥

**基本写法：设置环境变量**
`env: <变量名>: <值>`
```yaml
# 设置工作流级环境变量
env:
  NODE_ENV: production
jobs:
  build:
    env:
      CI: true
```

---

**基本写法：使用密钥**
`secrets.<密钥名>`
```yaml
# 使用仓库配置的密钥
steps:
  - run: npm publish
    env:
      NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

---

**基本写法：步骤级环境变量**
`run: <命令> env: <变量>: <值>`
```yaml
# 仅在特定步骤设置环境变量
steps:
  - run: echo $SECRET_VALUE
    env:
      SECRET_VALUE: ${{ secrets.MY_SECRET }}
```

---

**基本写法：使用上下文变量**
`${{ <上下文> }}`
```yaml
# 使用 GitHub 上下文信息
steps:
  - run: echo "Branch is ${{ github.ref }}"
  - run: echo "Actor is ${{ github.actor }}"
```

---

## 缓存与产物

**基本写法：缓存依赖**
`uses: actions/cache@v4`
```yaml
# 缓存 npm 依赖加速构建
steps:
  - uses: actions/cache@v4
    with:
      path: ~/.npm
      key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

---

**基本写法：上传构建产物**
`uses: actions/upload-artifact@v4`
```yaml
# 上传构建结果
steps:
  - uses: actions/upload-artifact@v4
    with:
      name: build-output
      path: dist/
```

---

**基本写法：下载产物**
`uses: actions/download-artifact@v4`
```yaml
# 下载之前上传的产物
steps:
  - uses: actions/download-artifact@v4
    with:
      name: build-output
```

---

**基本写法：条件步骤**
`if: <条件>`
```yaml
# 仅在 main 分支执行
steps:
  - run: npm run deploy
    if: github.ref == 'refs/heads/main'
```

---

## gh CLI 管理工作流

**基本写法：查看工作流列表**
`gh workflow list`
```bash
# 列出仓库的所有工作流
gh workflow list
```

---

**基本写法：查看工作流详情**
`gh workflow view <工作流名>`
```bash
# 查看指定工作流的详情
gh workflow view CI
```

---

**基本写法：查看工作流文件**
`gh workflow view <工作流名> --yaml`
```bash
# 查看工作流的 YAML 内容
gh workflow view CI --yaml
```

---

**基本写法：手动触发工作流**
`gh workflow run <工作流>`
```bash
# 手动触发指定工作流
gh workflow run CI
```

---

**基本写法：指定分支触发**
`gh workflow run <工作流> --ref <分支>`
```bash
# 在指定分支上触发工作流
gh workflow run CI --ref develop
```

---

**基本写法：带参数触发**
`gh workflow run <工作流> -f <参数>=<值>`
```bash
# 传入参数触发工作流
gh workflow run deploy.yml -f environment=production
```

---

**基本写法：禁用工作流**
`gh workflow disable <工作流>`
```bash
# 禁用指定工作流
gh workflow disable CI
```

---

**基本写法：启用工作流**
`gh workflow enable <工作流>`
```bash
# 启用被禁用的工作流
gh workflow enable CI
```

---

## 运行记录管理

**基本写法：查看运行列表**
`gh run list`
```bash
# 列出工作流运行记录
gh run list
```

---

**基本写法：按工作流筛选**
`gh run list --workflow <工作流>`
```bash
# 查看指定工作流的运行记录
gh run list --workflow CI
```

---

**基本写法：按状态筛选**
`gh run list --status <状态>`
```bash
# 查看失败的运行记录
gh run list --status failure
```

---

**基本写法：限制返回数量**
`gh run list --limit <数量>`
```bash
# 限制返回的运行记录数量
gh run list --limit 10
```

---

**基本写法：查看运行详情**
`gh run view <运行ID>`
```bash
# 查看指定运行的详细信息
gh run view 123456
```

---

**基本写法：查看失败日志**
`gh run view <运行ID> --log-failed`
```bash
# 查看运行失败的日志
gh run view 123456 --log-failed
```

---

**基本写法：查看完整日志**
`gh run view <运行ID> --log`
```bash
# 查看运行的完整日志
gh run view 123456 --log
```

---

**基本写法：实时监控运行**
`gh run watch <运行ID>`
```bash
# 实时监控运行直到完成
gh run watch 123456
```

---

**基本写法：重新运行**
`gh run rerun <运行ID>`
```bash
# 重新运行指定的工作流
gh run rerun 123456
```

---

**基本写法：仅重跑失败的作业**
`gh run rerun <运行ID> --failed`
```bash
# 仅重新运行失败的作业
gh run rerun 123456 --failed
```

---

**基本写法：取消运行中的工作流**
`gh run cancel <运行ID>`
```bash
# 取消正在运行的工作流
gh run cancel 123456
```

---

**基本写法：删除运行记录**
`gh run delete <运行ID>`
```bash
# 删除指定的工作流运行记录
gh run delete 123456
```



<!-- ============ 文档分隔线：004-github/016-GhRelease.md ============ -->

# gh release 发布命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建发布

**基本用法:创建 release**
`gh release create <标签> [文件...]`

```bash
# 基于标签创建发布
gh release create v1.0.0 --title "v1.0.0" --notes "首次正式发布"

# 自动生成更新日志
gh release create v1.0.0 --generate-notes

# 上传构建产物
gh release create v1.0.0 ./dist/app.zip ./dist/app.tar.gz

# 标记为预发布
gh release create v1.0.0 --prerelease --notes "测试版本"

# 指定目标分支
gh release create v1.0.0 --target main --notes "发布"
```

---

## 查看发布

**基本用法:列出所有 release**
`gh release list`

```bash
# 列出当前仓库的发布
gh release list

# 限制条数
gh release list --limit 5
```

---

**基本用法:查看某个 release 详情**
`gh release view <标签>`

```bash
# 查看指定发布详情
gh release view v1.0.0

# 在浏览器中打开
gh release view v1.0.0 --web
```

---

## 下载与上传

**基本用法:下载 release 资源**
`gh release download <标签>`

```bash
# 下载所有资源到当前目录
gh release download v1.0.0

# 下载指定文件
gh release download v1.0.0 --pattern "*.zip"

# 下载到指定目录
gh release download v1.0.0 --dir ./downloads
```

---

**基本用法:补充上传资源**
`gh release upload <标签> <文件>`

```bash
# 给已有 release 追加文件
gh release upload v1.0.0 ./build/app.exe

# 删除已存在的同名文件后上传
gh release upload v1.0.0 ./app.zip --clobber
```

---

## 编辑与删除

**基本用法:编辑 release**
`gh release edit <标签>`

```bash
# 修改标题与说明
gh release edit v1.0.0 --title "v1.0.0 正式版" --notes "更新说明"

# 转为草稿
gh release edit v1.0.0 --draft
```

---

**基本用法:删除 release**
`gh release delete <标签>`

```bash
# 删除发布(不影响标签)
gh release delete v1.0.0 --yes

# 同时删除标签
gh release delete v1.0.0 --cleanup-tag
```

---



<!-- ============ 文档分隔线：004-github/017-GhRunActions.md ============ -->

# gh run Actions 运行命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 查看运行记录

**基本用法:列出工作流运行**
`gh run list`

```bash
# 列出最近的运行记录
gh run list

# 按工作流过滤
gh run list --workflow=deploy.yml

# 按状态过滤
gh run list --status=failure

# 按分支过滤并限制条数
gh run list --branch=main --limit 10
```

---

**基本用法:查看运行详情**
`gh run view <运行ID>`

```bash
# 查看某次运行的详情
gh run view 12345

# 查看日志
gh run view 12345 --log

# 仅查看失败步骤日志
gh run view 12345 --log-failed

# 在浏览器打开
gh run view 12345 --web
```

---

## 监视运行

**基本用法:实时监视运行**
`gh run watch <运行ID>`

```bash
# 持续监视直到完成
gh run watch 12345

# 完成后退出并显示结果
gh run watch 12345 --exit-status
```

---

## 控制运行

**基本用法:重新运行**
`gh run rerun <运行ID>`

```bash
# 重新运行所有任务
gh run rerun 12345

# 仅重新运行失败的任务
gh run rerun 12345 --failed

# 调试模式重新运行
gh run rerun 12345 --debug
```

---

**基本用法:取消运行**
`gh run cancel <运行ID>`

```bash
# 取消正在运行的流水线
gh run cancel 12345
```

---

**基本用法:删除运行记录**
`gh run delete <运行ID>`

```bash
# 删除某次运行记录
gh run delete 12345
```

---

## 下载产物

**基本用法:下载构建产物**
`gh run download <运行ID>`

```bash
# 下载所有产物到当前目录
gh run download 12345

# 下载指定产物
gh run download 12345 -n build-artifacts

# 下载到指定目录
gh run download 12345 --dir ./out
```

---



<!-- ============ 文档分隔线：004-github/018-GhWorkflow.md ============ -->

# gh workflow 工作流命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 查看工作流

**基本用法:列出工作流**
`gh workflow list`

```bash
# 列出所有工作流
gh workflow list

# 查看某工作流详情
gh workflow view deploy.yml

# 在浏览器中打开
gh workflow view deploy.yml --web
```

---

## 手动触发

**基本用法:触发工作流**
`gh workflow run <工作流>`

```bash
# 手动触发工作流
gh workflow run deploy.yml

# 指定分支触发
gh workflow run deploy.yml --ref feature

# 传入参数
gh workflow run deploy.yml -f environment=production -f version=1.2.3

# 从 JSON 文件读取参数
gh workflow run deploy.yml --raw-field config=@config.json
```

---

## 启用与禁用

**基本用法:启用工作流**
`gh workflow enable <工作流>`

```bash
# 启用被禁用的工作流
gh workflow enable deploy.yml
```

---

**基本用法:禁用工作流**
`gh workflow disable <工作流>`

```bash
# 临时禁用工作流
gh workflow disable deploy.yml
```

---



<!-- ============ 文档分隔线：004-github/019-GhSecretVar.md ============ -->

# gh secret 与变量命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 仓库密钥

**基本用法:设置 Actions 密钥**
`gh secret set <名称>`

```bash
# 交互式输入密钥值
gh secret set DATABASE_URL

# 从字符串设置
gh secret set API_KEY --body "sk-12345"

# 从文件读取
gh secret set DEPLOY_KEY < ~/.ssh/id_rsa

# 从环境变量读取
gh secret set TOKEN --body "$MY_TOKEN"
```

---

**基本用法:列出与删除密钥**
`gh secret list`

```bash
# 列出所有密钥(不显示值)
gh secret list

# 删除密钥
gh secret delete API_KEY
```

---

## 组织与环境密钥

**基本用法:设置组织级密钥**
`gh secret set <名称> --org <组织>`

```bash
# 设置组织密钥
gh secret set DEPLOY_TOKEN --org myorg

# 指定可见仓库
gh secret set TOKEN --org myorg --repos "repo1,repo2"

# 设置环境密钥
gh secret set DB_PASS --env production
```

---

## Codespaces 密钥

**基本用法:Codespaces 密钥**
`gh codespace secret set <名称>`

```bash
# 设置 Codespaces 用户密钥
gh codespace secret set API_KEY --body "sk-xxx"

# 设置组织 Codespaces 密钥
gh codespace secret set TOKEN --org myorg
```

---

## 变量管理

**基本用法:设置 Actions 变量**
`gh variable set <名称>`

```bash
# 设置变量(变量值可见,适合非敏感数据)
gh variable set NODE_ENV --body "production"

# 从文件设置
gh variable set CONFIG < config.json

# 列出变量
gh variable list

# 查看变量值
gh variable get NODE_ENV

# 删除变量
gh variable delete NODE_ENV
```

---



<!-- ============ 文档分隔线：004-github/020-GhGist.md ============ -->

# gh gist 代码片段命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Gist

**基本用法:创建公开 gist**
`gh gist create <文件>`

```bash
# 从文件创建公开 gist
gh gist create snippet.js

# 创建私密 gist(不可搜索但仍可访问)
gh gist create snippet.js --secret

# 从标准输入创建
echo "console.log(1)" | gh gist create -f script.js

# 添加描述
gh gist create note.md --desc "配置笔记"
```

---

## 查看 Gist

**基本用法:列出 gist**
`gh gist list`

```bash
# 列出自己的 gist
gh gist list

# 限制条数
gh gist list --limit 20
```

---

**基本用法:查看 gist 内容**
`gh gist view <ID>`

```bash
# 查看 gist 内容
gh gist view abc123

# 查看原始内容
gh gist view abc123 --raw

# 在浏览器打开
gh gist view abc123 --web
```

---

## 编辑与克隆

**基本用法:编辑 gist**
`gh gist edit <ID>`

```bash
# 编辑 gist 内容
gh gist edit abc123

# 用指定文件替换
gh gist edit abc123 new_content.js
```

---

**基本用法:克隆 gist**
`gh gist clone <ID>`

```bash
# 把 gist 克隆为本地仓库
gh gist clone abc123 my-snippet
```

---

## 删除与重命名

**基本用法:删除 gist**
`gh gist delete <ID>`

```bash
# 删除 gist
gh gist delete abc123 --yes
```

---

**基本用法:重命名文件**
`gh gist rename <ID> <旧名> <新名>`

```bash
# 重命名 gist 中的文件
gh gist rename abc123 old.js new.js
```

---



<!-- ============ 文档分隔线：004-github/021-GhCodespace.md ============ -->

# gh codespace 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建与列出

**基本用法:创建 codespace**
`gh codespace create`

```bash
# 交互式创建
gh codespace create

# 指定仓库与分支
gh codespace create --repo owner/repo --branch dev

# 指定机器规格
gh codespace create --machine basicLinux32gb
```

---

**基本用法:列出 codespace**
`gh codespace list`

```bash
# 列出所有 codespace
gh codespace list
```

---

## 连接与操作

**基本用法:SSH 连接**
`gh codespace ssh`

```bash
# 通过 SSH 连接到 codespace
gh codespace ssh -c <codespace名>

# 在 VS Code 中打开
gh codespace code
```

---

**基本用法:查看日志**
`gh codespace logs`

```bash
# 实时查看创建日志
gh codespace logs -c <codespace名>
```

---

**基本用法:查看详情**
`gh codespace view`

```bash
# 查看 codespace 详情
gh codespace view -c <codespace名>
```

---

## 管理生命周期

**基本用法:停止 codespace**
`gh codespace stop`

```bash
# 停止运行中的 codespace
gh codespace stop -c <codespace名>
```

---

**基本用法:重建 codespace**
`gh codespace rebuild`

```bash
# 重建(应用 devcontainer 改动)
gh codespace rebuild -c <codespace名>
```

---

**基本用法:删除 codespace**
`gh codespace delete`

```bash
# 删除指定 codespace
gh codespace delete -c <codespace名> --force

# 删除所有已停止的 codespace
gh codespace delete --days 7
```

---

## 端口管理

**基本用法:查看端口转发**
`gh codespace ports`

```bash
# 列出转发端口
gh codespace ports -c <codespace名>

# 设置端口可见性
gh codespace ports visibility 3000:public -c <codespace名>
```

---



<!-- ============ 文档分隔线：004-github/022-GhExtension.md ============ -->

# gh extension 扩展命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 安装扩展

**基本用法:安装扩展**
`gh extension install <仓库>`

```bash
# 安装社区扩展
gh extension install dlvhdr/gh-dash

# 安装特定版本
gh extension install dlvhdr/gh-dash --pin v2.0.0
```

---

**基本用法:搜索扩展**
`gh extension search <关键词>`

```bash
# 搜索相关扩展
gh extension search notify
```

---

## 管理扩展

**基本用法:列出扩展**
`gh extension list`

```bash
# 查看已安装扩展
gh extension list
```

---

**基本用法:升级扩展**
`gh extension upgrade`

```bash
# 升级所有扩展
gh extension upgrade --all

# 升级指定扩展
gh extension upgrade gh-dash
```

---

**基本用法:移除扩展**
`gh extension remove <名称>`

```bash
# 卸载扩展
gh extension remove gh-dash
```

---

## 创建扩展

**基本用法:创建扩展脚手架**
`gh extension create <名称>`

```bash
# 创建新扩展(含脚手架)
gh extension create my-ext

# 创建预编译扩展(Go)
gh extension create my-ext --precompiled=go
```

---

**基本用法:本地开发扩展**
`gh extension install <路径>`

```bash
# 以本地目录方式安装用于开发
gh extension install .
```

---

## 浏览扩展

**基本用法:在浏览器打开**
`gh extension browse <名称>`

```bash
# 打开扩展仓库主页
gh extension browse gh-dash
```

---



<!-- ============ 文档分隔线：004-github/023-GhApi.md ============ -->

# gh api 调用命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 基础请求

**基本用法:GET 请求**
`gh api <端点>`

```bash
# 获取仓库信息
gh api repos/owner/repo

# 获取当前用户
gh api user

# 列出仓库的 issue
gh api repos/owner/repo/issues
```

---

## 指定方法与字段

**基本用法:POST 请求**
`gh api <端点> --method POST`

```bash
# 创建 issue
gh api repos/owner/repo/issues \
  --method POST \
  -f title="Bug 报告" \
  -f body="详细描述问题"

# 创建仓库
gh api user/repos --method POST -f name=new-repo -f private=true
```

---

**基本用法:传递参数**
`gh api <端点> -f <键>=<值>`

```bash
# 字符串字段(-f)
gh api repos/owner/repo/comments -f body="评论内容"

# 类型化字段(-F,支持数字/布尔/null)
gh api repos/owner/repo/issues -F milestone=12

# 从文件读取字段值
gh api user/repos -f name=@repo-name.txt
```

---

## 输出处理

**基本用法:jq 过滤输出**
`gh api <端点> --jq <表达式>`

```bash
# 仅提取仓库名称
gh api user/repos --jq '.[].full_name'

# 提取并统计
gh api repos/owner/repo/issues --jq 'length'
```

---

**基本用法:分页获取**
`gh api <端点> --paginate`

```bash
# 自动获取所有分页结果
gh api repos/owner/repo/issues --paginate --jq '.[].title'
```

---

## 高级用法

**基本用法:查看请求详情**
`gh api <端点> --include`

```bash
# 包含响应头与状态码
gh api user --include

# 显示完整请求与响应(调试)
gh api user --verbose
```

---

**基本用法:发送原始请求体**
`gh api <端点> --input <文件>`

```bash
# 从文件读取 JSON 请求体
gh api repos/owner/repo/labels --input labels.json
```

---



<!-- ============ 文档分隔线：004-github/024-GhSearch.md ============ -->

# gh search 搜索命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 搜索仓库

**基本用法:搜索仓库**
`gh search repos <查询>`

```bash
# 按关键词搜索仓库
gh search repos "react ui"

# 按语言与 star 数过滤
gh search repos --language=typescript --stars=">1000"

# 按主题过滤
gh search repos --topic=vue --limit 10

# 在指定组织中搜索
gh search repos --owner=microsoft --visibility=public
```

---

## 搜索 Issue 与 PR

**基本用法:搜索 issue**
`gh search issues <查询>`

```bash
# 搜索 open 状态的 bug
gh search issues "memory leak" --state=open --label=bug

# 搜索分配给自己的 issue
gh search issues --assignee=@me

# 搜索某仓库的 issue
gh search issues --repo=owner/repo "crash"
```

---

**基本用法:搜索 PR**
`gh search prs <查询>`

```bash
# 搜索已合并的 PR
gh search prs --merged --author=@me

# 搜索需要审查的 PR
gh search prs --review-requested=@me --open
```

---

## 搜索代码

**基本用法:搜索代码**
`gh search code <查询>`

```bash
# 在所有公开仓库搜索代码
gh search code "useState useEffect"

# 限定仓库与文件名
gh search code "TODO" --repo=owner/repo --filename=*.py

# 限定组织
gh search code "config" --org=myorg --language=go
```

---

## 搜索提交

**基本用法:搜索提交**
`gh search commits <查询>`

```bash
# 搜索提交信息
gh search commits "fix memory leak" --repo=owner/repo

# 按作者搜索
gh search commits --author=zhangsan
```

---

## 通用选项

**基本用法:控制输出**
`gh search <类型> --<选项>`

```bash
# 排序方式
gh search repos react --sort=stars --order=desc

# 输出 JSON
gh search repos react --json fullName,stargazersCount

# 在浏览器中打开搜索结果
gh search repos react --web
```

---



<!-- ============ 文档分隔线：004-github/025-GhLabel.md ============ -->

# gh label 与 alias/config 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 标签管理

**基本用法:列出标签**
`gh label list`

```bash
# 列出仓库标签
gh label list

# 按名称搜索
gh label list --search bug
```

---

**基本用法:创建标签**
`gh label create <名称>`

```bash
# 创建带颜色与描述的标签
gh label create "type:bug" --color "D73A4A" --description "Bug 问题"

# 从已有仓库复制所有标签
gh label clone owner/template-repo
```

---

**基本用法:编辑与删除**
`gh label edit <名称>`

```bash
# 修改标签颜色
gh label edit bug --color "B60205"

# 重命名标签
gh label edit bug --new-name "type:bug"

# 删除标签
gh label delete "type:bug" --yes
```

---

## 命令别名

**基本用法:设置别名**
`gh alias set <别名> <命令>`

```bash
# 创建常用命令别名
gh alias set co "pr checkout"

# 创建带 shell 的别名
gh alias set vp "pr view --web" --shell

# 列出所有别名
gh alias list

# 删除别名
gh alias delete co
```

---

## 配置管理

**基本用法:查看配置**
`gh config list`

```bash
# 列出所有配置
gh config list

# 查看单项配置
gh config get editor
```

---

**基本用法:设置配置**
`gh config set <键> <值>`

```bash
# 设置默认编辑器
gh config set editor "code --wait"

# 设置默认 Git 协议
gh config set git_protocol ssh

# 设置默认分页器
gh config set pager less
```

---

**基本用法:清理缓存**
`gh config clear-cache`

```bash
# 清除 CLI 缓存
gh config clear-cache
```

---



<!-- ============ 文档分隔线：004-github/026-GhAliasConfig.md ============ -->

# gh alias 与 config 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 别名管理

**基本用法:设置命令别名**
`gh alias set <别名> <展开>`

```bash
# 为 pr checkout 设置别名
gh alias set co "pr checkout"

# 设置 shell 别名(支持管道与变量)
gh alias set recent "run list --limit 5" --shell

# 列出全部别名
gh alias list

# 删除别名
gh alias delete co

# 从 YAML 文件导入别名
gh alias import aliases.yml --clobber
```

---

## 配置项

**基本用法:读取配置**
`gh config get <键>`

```bash
# 查看默认编辑器
gh config get editor

# 查看 git 协议
gh config get git_protocol

# 列出所有配置
gh config list
```

---

**基本用法:修改配置**
`gh config set <键> <值>`

```bash
# 设置编辑器
gh config set editor "code --wait"

# 设置 SSH 协议
gh config set git_protocol ssh

# 设置分页器关闭
gh config set pager ""

# 设置为指定主机
gh config set editor vim --host github.com
```

---

## 补全与状态

**基本用法:Shell 自动补全**
`gh completion -s <shell>`

```bash
# 生成 bash 补全脚本
gh completion -s bash > ~/.gh-completion.bash

# PowerShell 补全
gh completion -s powershell | Out-String | Invoke-Expression

# zsh 补全
gh completion -s zsh > "${fpath[1]}/_gh"
```

---

**基本用法:查看账户状态**
`gh status`

```bash
# 查看当前账户在所有仓库的工作概览
gh status
```

---



<!-- ============ 文档分隔线：004-github/027-ActionsSyntax.md ============ -->

# GitHub Actions 工作流语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 工作流基本结构

**基本用法:定义工作流**
`name: <名称>` (`.github/workflows/*.yml`)

```yaml
# 工作流名称
name: CI

# 触发条件
on: [push, pull_request]

# 任务集合
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install
      - run: npm test
```

---

## jobs 任务定义

**基本用法:定义任务依赖**
`jobs.<id>.needs`

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "build"
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "test"
  deploy:
    needs: [build, test]
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploy"
```

---

**基本用法:设置运行环境**
`jobs.<id>.runs-on`

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    # 自定义环境变量
    env:
      NODE_ENV: production
    # 超时设置
    timeout-minutes: 30
    # 失败时继续
    continue-on-error: false
```

---

## steps 步骤

**基本用法:引用 Action**
`uses: <action>@<版本>`

```yaml
steps:
  # 检出代码
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
  # 设置 Node 环境
  - uses: actions/setup-node@v4
    with:
      node-version: '20'
      cache: 'npm'
  # 缓存依赖
  - uses: actions/cache@v4
    with:
      path: ~/.npm
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

---

**基本用法:运行命令**
`run: <命令>`

```yaml
steps:
  - name: 安装依赖
    run: npm ci

  - name: 多行命令
    run: |
      npm run build
      npm run test

  - name: 条件执行
    if: github.ref == 'refs/heads/main'
    run: npm run deploy

  - name: 设置环境变量
    run: echo "VERSION=1.0" >> $GITHUB_ENV
```

---

## with 传参

**基本用法:给 Action 传参**
`with: <键>: <值>`

```yaml
- uses: actions/checkout@v4
  with:
    ref: develop
    submodules: true

- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    retention-days: 7
```

---

## 权限与并发

**基本用法:设置权限**
`permissions:`

```yaml
permissions:
  contents: read
  pull-requests: write
  issues: write
```

---

**基本用法:并发控制**
`concurrency:`

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

---



<!-- ============ 文档分隔线：004-github/028-ActionsTriggers.md ============ -->

# GitHub Actions 触发器速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 单一触发

**基本用法:push 触发**
`on: push`

```yaml
on:
  push:
    branches:
      - main
      - 'release/*'
    paths:
      - 'src/**'
      - 'package.json'
    tags:
      - 'v*'
```

---

**基本用法:pull_request 触发**
`on: pull_request`

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened]
    branches:
      - main
    paths-ignore:
      - '**.md'
      - 'docs/**'
```

---

## 定时触发

**基本用法:定时任务**
`on: schedule`

```yaml
on:
  schedule:
    # 每天 UTC 00:00 执行
    - cron: '0 0 * * *'
    # 每周一 9 点
    - cron: '0 9 * * 1'
```

---

## 手动触发

**基本用法:手动触发**
`on: workflow_dispatch`

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: '部署环境'
        required: true
        type: choice
        options:
          - staging
          - production
        default: staging
      version:
        description: '版本号'
        required: false
        default: '1.0.0'
```

---

## 仓库事件触发

**基本用法:issue 与 release**
`on: <事件>`

```yaml
on:
  issues:
    types: [opened, labeled]
  issue_comment:
    types: [created]
  release:
    types: [published]
  push:
    branches: [main]
```

---

## 工作流调用

**基本用法:被其他工作流调用**
`on: workflow_call`

```yaml
on:
  workflow_call:
    inputs:
      target:
        type: string
        required: true
    secrets:
      DEPLOY_KEY:
        required: true
```

---

## 触发过滤组合

**基本用法:多触发组合**
`on: [<事件>]`

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:
```

---



<!-- ============ 文档分隔线：004-github/029-ActionsContext.md ============ -->

# GitHub Actions 上下文与表达式速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 常用上下文

**基本用法:引用上下文值**
`${{ <上下文>.<属性> }}`

```yaml
# github 上下文
steps:
  - run: echo ${{ github.repository }}
  - run: echo ${{ github.event_name }}
  - run: echo ${{ github.ref }}
  - run: echo ${{ github.sha }}

# 环境变量上下文
steps:
  - run: echo ${{ env.NODE_ENV }}

# 作业上下文
steps:
  - if: ${{ failure() }}
    run: echo "前置步骤失败"
```

---

## 上下文一览

**基本用法:job 上下文**
`${{ job.<属性> }}`

```yaml
# 任务状态
${{ job.status }}
${{ job.container.id }}
```

---

**基本用法:steps 上下文**
`${{ steps.<id>.<属性> }}`

```yaml
steps:
  - id: setvar
    run: echo "result=hello" >> $GITHUB_OUTPUT
  - run: echo ${{ steps.setvar.outputs.result }}
```

---

**基本用法:secrets 与 vars 上下文**
`${{ secrets.<名称> }}`

```yaml
steps:
  - run: deploy.sh ${{ secrets.DEPLOY_TOKEN }}
  - run: echo ${{ vars.ENV_NAME }}
```

---

**基本用法:matrix 上下文**
`${{ matrix.<键> }}`

```yaml
strategy:
  matrix:
    node: [18, 20]
steps:
  - run: echo "Node ${{ matrix.node }}"
```

---

## 表达式函数

**基本用法:逻辑运算**
`${{ <表达式> }}`

```yaml
if: ${{ github.ref == 'refs/heads/main' && success() }}
if: ${{ failure() || cancelled() }}
```

---

**基本用法:常用函数**
`${{ <函数>(<参数>) }}`

```yaml
# 包含判断
if: ${{ contains(github.event.head_commit.message, '[skip ci]') }}
# 字符串开头匹配
if: ${{ startsWith(github.ref, 'refs/tags/') }}
# 字符串格式化
run: echo "${{ format('Hello {0} {1}', 'GitHub', 'Actions') }}"
# JSON 转字符串
run: echo "${{ toJSON(github.event) }}"
# 从 JSON 解析
run: echo "${{ fromJSON(env.CONFIG).key }}"
```

---

**基本用法:状态检查函数**
`${{ <状态函数>() }}`

```yaml
# 所有前置步骤成功
if: ${{ success() }}
# 任一前置步骤失败
if: ${{ failure() }}
# 任务被取消
if: ${{ cancelled() }}
# 总是执行(无论成功失败)
if: ${{ always() }}
```

---



<!-- ============ 文档分隔线：004-github/030-ActionsCache.md ============ -->

# GitHub Actions 缓存与产物速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## actions/cache 缓存

**基本用法:缓存依赖**
`uses: actions/cache@v4`

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    # 部分匹配回退
    restore-keys: |
      ${{ runner.os }}-node-
```

---

**基本用法:缓存不同包管理器**
`uses: actions/cache@v4`

```yaml
# pip 缓存
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}

# Gradle 缓存
- uses: actions/cache@v4
  with:
    path: |
      ~/.gradle/caches
      ~/.gradle/wrapper
    key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*') }}
```

---

## 缓存管理命令

**基本用法:通过 gh 管理缓存**
`gh cache <子命令>`

```bash
# 列出仓库缓存
gh cache list

# 按键删除缓存
gh cache delete <key>

# 删除所有缓存
gh cache delete --all
```

---

## 上传产物

**基本用法:上传构建产物**
`uses: actions/upload-artifact@v4`

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: dist-files
    path: |
      dist/
      build/
    # 保留天数
    retention-days: 14
    # 覆盖同名
    overwrite: true
    # 压缩级别
    compression-level: 6
```

---

## 下载产物

**基本用法:在工作流中下载**
`uses: actions/download-artifact@v4`

```yaml
- uses: actions/download-artifact@v4
  with:
    name: dist-files
    path: ./artifact

# 下载上一个工作流产物
- uses: actions/download-artifact@v4
  with:
    name: dist-files
    run-id: ${{ github.event.workflow_run.id }}
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

---

**基本用法:通过 gh 命令下载**
`gh run download`

```bash
# 下载某次运行的产物
gh run download 12345 -n dist-files
```

---



<!-- ============ 文档分隔线：004-github/031-ActionsMatrix.md ============ -->

# GitHub Actions 矩阵策略速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 基础矩阵

**基本用法:定义矩阵**
`strategy.matrix`

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [16, 18, 20]
        os: [ubuntu-latest, macos-latest, windows-latest]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

---

## 矩阵组合与排除

**基本用法:排除特定组合**
`strategy.matrix.exclude`

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [18, 20]
    exclude:
      # 跳过 Windows + Node18
      - os: windows-latest
        node: 18
```

---

**基本用法:额外包含组合**
`strategy.matrix.include`

```yaml
strategy:
  matrix:
    node: [18, 20]
    include:
      # 给 node 20 额外加一个变量
      - node: 20
        experimental: true
      # 追加一个完全独立的组合
      - node: 22
        os: ubuntu-latest
```

---

## 失败策略

**基本用法:控制失败行为**
`strategy:`

```yaml
strategy:
  fail-fast: false      # 一个失败不取消其他
  max-parallel: 4       # 最大并行数
  matrix:
    node: [16, 18, 20]
```

---

## 动态矩阵

**基本用法:从 JSON 输出动态生成**
`strategy.matrix: ${{ fromJSON(...) }}`

```yaml
jobs:
  dynamic:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run: echo "matrix=[\"a\",\"b\",\"c\"]" >> $GITHUB_OUTPUT

  use:
    needs: dynamic
    runs-on: ubuntu-latest
    strategy:
      matrix:
        target: ${{ fromJSON(needs.dynamic.outputs.matrix) }}
    steps:
      - run: echo ${{ matrix.target }}
```

---



<!-- ============ 文档分隔线：004-github/032-ActionsReuse.md ============ -->

# GitHub Actions 复用工作流速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 可调用工作流

**基本用法:定义可复用工作流**
`on: workflow_call` (`.github/workflows/reusable.yml`)

```yaml
name: Reusable Build

on:
  workflow_call:
    # 输入参数
    inputs:
      environment:
        type: string
        required: true
      debug:
        type: boolean
        default: false
    # 密钥参数
    secrets:
      DEPLOY_KEY:
        required: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Building for ${{ inputs.environment }}"
      - if: ${{ inputs.debug }}
        run: echo "Debug mode"
      - run: deploy.sh ${{ secrets.DEPLOY_KEY }}
```

---

## 调用工作流

**基本用法:同一仓库内调用**
`uses: ./.github/workflows/<文件>`

```yaml
jobs:
  call-build:
    uses: ./.github/workflows/reusable.yml
    with:
      environment: production
      debug: true
    secrets:
      DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
```

---

**基本用法:跨仓库调用**
`uses: <owner>/<repo>/.github/workflows/<文件>@<引用>`

```yaml
jobs:
  call-external:
    uses: org/shared-workflows/.github/workflows/build.yml@main
    with:
      environment: staging
    secrets: inherit
```

---

**基本用法:传递全部密钥**
`secrets: inherit`

```yaml
jobs:
  call-build:
    uses: ./.github/workflows/deploy.yml
    with:
      env: production
    secrets: inherit
```

---

## 串联与并联

**基本用法:依赖可调用工作流**
`needs:`

```yaml
jobs:
  call-build:
    uses: ./.github/workflows/build.yml
  call-deploy:
    needs: call-build
    uses: ./.github/workflows/deploy.yml
    secrets: inherit
```

---



<!-- ============ 文档分隔线：004-github/033-GitHubPages.md ============ -->

# GitHub Pages 部署配置速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Actions 部署 Pages

**基本用法:部署静态站点**
`uses: actions/deploy-pages@v4`

```yaml
name: Deploy Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

---

## gh-pages 分支方式

**基本用法:推送构建产物到 gh-pages**
`git push origin <子树>:gh-pages`

```bash
# 把 dist 子目录作为 gh-pages 分支根推送
git subtree push --prefix dist origin gh-pages

# 强制更新 gh-pages
git push origin `git subtree split --prefix dist`:gh-pages --force
```

---

## 配置 Pages 源

**基本用法:通过 gh 配置 Pages**
`gh api repos/<owner>/<repo>/pages`

```bash
# 设置 Pages 源为 GitHub Actions
gh api repos/owner/repo/pages -X POST -f source[branch]=main -f source[path]=/

# 修改 Pages 源
gh api repos/owner/repo/pages -X PUT -f source[branch]=gh-pages

# 查看 Pages 配置
gh api repos/owner/repo/pages
```

---

## 自定义域名

**基本用法:配置自定义域名**
`echo "<域名>" > CNAME`

```bash
# 在站点根目录创建 CNAME 文件
echo "docs.example.com" > dist/CNAME

# 配置 DNS:把 www 指向 <user>.github.io
```

---

## 通过 gh-pages 工具发布

**基本用法:用 gh-pages 工具**
`npx gh-pages -d <目录>`

```bash
# 把 dist 发布到 gh-pages 分支
npx gh-pages -d dist

# 指定分支与消息
npx gh-pages -d dist -b gh-pages -m "deploy [skip ci]"
```

---



<!-- ============ 文档分隔线：004-github/034-GitHubRepoSettings.md ============ -->

# GitHub 仓库设置命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 仓库信息

**基本用法:查看仓库设置**
`gh repo view <仓库>`

```bash
# 查看仓库详情
gh repo view owner/repo

# 以 JSON 输出
gh repo view owner/repo --json name,visibility,defaultBranchRef
```

---

**基本用法:修改仓库设置**
`gh repo edit <仓库>`

```bash
# 修改描述
gh repo edit owner/repo --description "项目描述"

# 修改主页地址
gh repo edit owner/repo --homepage "https://example.com"

# 切换可见性
gh repo edit owner/repo --visibility public
gh repo edit owner/repo --visibility internal

# 启用 issues 与 wiki
gh repo edit owner/repo --enable-issues --enable-wiki

# 关闭项目功能
gh repo edit owner/repo --enable-projects=false
```

---

## 仓库生命周期

**基本用法:归档仓库**
`gh repo archive <仓库>`

```bash
# 把仓库设为只读归档
gh repo archive owner/repo --yes
```

---

**基本用法:取消归档**
`gh repo unarchive <仓库>`

```bash
# 恢复归档仓库为可写
gh repo unarchive owner/repo --yes
```

---

**基本用法:删除仓库**
`gh repo delete <仓库>`

```bash
# 删除仓库(危险操作)
gh repo delete owner/repo --yes
```

---

## 仓库元数据

**基本用法:管理 topics**
`gh repo edit <仓库> --add-topic`

```bash
# 添加 topic 标签
gh repo edit owner/repo --add-topic vue --add-topic frontend

# 移除 topic
gh repo edit owner/repo --remove-topic legacy

# 清空 topics
gh repo edit owner/repo --clear-topics
```

---

## 部署密钥

**基本用法:添加部署密钥**
`gh repo deploy-key add <文件>`

```bash
# 添加只读部署密钥
gh repo deploy-key add ~/.ssh/deploy.pub -t "CI deploy key"

# 添加可写部署密钥
gh repo deploy-key add ~/.ssh/deploy.pub -t "write key" --allow-write

# 列出部署密钥
gh repo deploy-key list

# 删除密钥
gh repo deploy-key delete <key-id>
```

---

## 通过 API 操作

**基本用法:调用 API 修改设置**
`gh api repos/<owner>/<repo> -X PATCH`

```bash
# 修改默认分支
gh api repos/owner/repo -X PATCH -f default_branch=main

# 启用自动删除分支
gh api repos/owner/repo -X PATCH -F delete_branch_on_merge=true
```

---



<!-- ============ 文档分隔线：004-github/035-GitHubBranchProtection.md ============ -->

# GitHub 分支保护命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 通过 API 配置保护规则

**基本用法:设置分支保护**
`gh api repos/<owner>/<repo>/branches/<分支>/protection -X PUT`

```bash
# 要求 PR 评审再合并
gh api repos/owner/repo/branches/main/protection -X PUT \
  --input - <<'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["CI / build"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "dismiss_stale_reviews": true
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
```

---

**基本用法:查看保护规则**
`gh api repos/<owner>/<repo>/branches/<分支>/protection`

```bash
# 查看主分支的保护配置
gh api repos/owner/repo/branches/main/protection

# 查看是否受保护
gh api repos/owner/repo/branches/main --jq '.protected'
```

---

**基本用法:删除保护规则**
`gh api repos/<owner>/<repo>/branches/<分支>/protection -X DELETE`

```bash
# 取消分支保护
gh api repos/owner/repo/branches/main/protection -X DELETE
```

---

## 规则集(推荐方式)

**基本用法:创建规则集**
`gh api repos/<owner>/<repo>/rulesets -X POST`

```bash
# 创建针对 main 分支的规则集
gh api repos/owner/repo/rulesets -X POST --input - <<'EOF'
{
  "name": "main-protection",
  "target": "branch",
  "source_type": "Repository",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "exclude": [],
      "include": ["~DEFAULT_BRANCH"]
    }
  },
  "rules": [
    { "type": "required_status_checks", "parameters": { "required_status_checks": [] } },
    { "type": "required_pull_request_reviews", "parameters": { "required_approving_review_count": 1 } }
  ]
}
EOF
```

---

**基本用法:查看规则集**
`gh api repos/<owner>/<repo>/rulesets`

```bash
# 列出所有规则集
gh api repos/owner/repo/rulesets

# 查看某规则集详情
gh api repos/owner/repo/rulesets/123
```

---

## 常用保护项

**基本用法:通过 gh repo edit 设置**
`gh repo edit <仓库>`

```bash
# 启用合并时自动删除分支
gh repo edit owner/repo --enable-merge-commit
gh api repos/owner/repo -X PATCH -F delete_branch_on_merge=true

# 启用线性历史(仅 fast-forward / squash)
gh repo edit owner/repo --enable-squash-merge
gh repo edit owner/repo --disable-merge-commit
```

---



<!-- ============ 文档分隔线：004-github/036-GitHubProjects.md ============ -->

# GitHub Projects 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 项目管理

**基本用法:创建项目**
`gh project create`

```bash
# 创建组织级项目
gh project create --owner myorg --title "Q3 Roadmap" --format json

# 创建用户级项目
gh project create --owner @me --title "Personal Tasks"
```

---

**基本用法:查看项目**
`gh project view <编号>`

```bash
# 查看项目详情(按编号)
gh project view 1 --owner myorg

# 列出项目
gh project list --owner myorg

# 在浏览器中打开
gh project view 1 --owner myorg --web
```

---

**基本用法:编辑与关闭**
`gh project edit <编号>`

```bash
# 修改项目标题
gh project edit 1 --owner myorg --title "New Title"

# 关闭项目
gh project close 1 --owner myorg

# 重新打开
gh project reopen 1 --owner myorg

# 删除项目
gh project delete 1 --owner myorg
```

---

## 字段管理

**基本用法:添加字段**
`gh project field-create`

```bash
# 创建单选字段
gh project field-create 1 --owner myorg --name "Priority" --data-type SINGLE_SELECT --options "P0,P1,P2"

# 创建文本字段
gh project field-create 1 --owner myorg --name "Notes" --data-type TEXT

# 列出字段
gh project field-list 1 --owner myorg
```

---

## 添加项目条目

**基本用法:添加 issue/pr 到项目**
`gh project item-add <项目号>`

```bash
# 把 issue 加入项目
gh project item-add 1 --owner myorg --url https://github.com/owner/repo/issues/42

# 查看 items
gh project item-list 1 --owner myorg

# 修改字段值
gh project item-edit --id <item-id> --field-id <field-id> --project-id <project-id> --text "done"

# 从项目移除
gh project item-delete <item-id> --project-id <project-id>
```

---

## 通过 API 操作

**基本用法:GraphQL 操作项目**
`gh api graphql`

```bash
# 查询项目信息
gh api graphql -f query='
query {
  user(login: "username") {
    projectV2(number: 1) {
      title
      items(first: 10) {
        nodes { id content { ... on Issue { title } } }
      }
    }
  }
}'
```

---
