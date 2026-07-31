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
