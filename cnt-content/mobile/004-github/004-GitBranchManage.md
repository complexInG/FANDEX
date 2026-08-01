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
