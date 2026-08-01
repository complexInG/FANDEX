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
