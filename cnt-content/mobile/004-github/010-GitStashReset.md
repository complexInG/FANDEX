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
