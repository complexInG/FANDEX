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
