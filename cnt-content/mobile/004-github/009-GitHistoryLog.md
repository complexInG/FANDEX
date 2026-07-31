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
