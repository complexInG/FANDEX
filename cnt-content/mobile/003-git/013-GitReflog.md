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
