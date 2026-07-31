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
