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
