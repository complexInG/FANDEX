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
