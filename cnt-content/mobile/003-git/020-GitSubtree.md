# Git subtree 子树管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 添加子树

**基本写法：添加远程仓库为子树**
`git subtree add --prefix=<路径> <仓库URL> <分支>`
```bash
# 将外部仓库添加到 lib/utils 目录
git subtree add --prefix=lib/utils https://github.com/org/utils.git main
```

---

**基本写法：指定子目录前缀**
`git subtree add --prefix=<路径> <仓库URL> <分支> --squash`
```bash
# 仅合并子树最新提交（压缩历史）
git subtree add --prefix=lib/utils https://github.com/org/utils.git main --squash
```

---

**基本写法：从本地路径添加子树**
`git subtree add --prefix=<路径> <本地路径> <分支>`
```bash
# 从本地仓库添加子树
git subtree add --prefix=lib/local ../local-repo main
```

---

## 拉取子树更新

**基本写法：拉取子树最新变更**
`git subtree pull --prefix=<路径> <仓库URL> <分支>`
```bash
# 拉取子树仓库 main 分支的更新
git subtree pull --prefix=lib/utils https://github.com/org/utils.git main
```

---

**基本写法：压缩方式拉取**
`git subtree pull --prefix=<路径> <仓库URL> <分支> --squash`
```bash
# 拉取并压缩为单次提交
git subtree pull --prefix=lib/utils https://github.com/org/utils.git main --squash
```

---

**基本写法：使用 rebase 方式拉取**
`git subtree pull --prefix=<路径> -X <策略> <仓库URL> <分支>`
```bash
# 拉取时优先采用子树内容
git subtree pull --prefix=lib/utils -X theirs https://github.com/org/utils.git main
```

---

## 推送子树变更

**基本写法：推送子树变更到上游**
`git subtree push --prefix=<路径> <仓库URL> <分支>`
```bash
# 推送子树变更回原仓库
git subtree push --prefix=lib/utils https://github.com/org/utils.git feature-update
```

---

**基本写法：拆分后推送**
`git subtree split --prefix=<路径> --branch <新分支>`
```bash
# 将子树拆分为独立分支
git subtree split --prefix=lib/utils --branch utils-sync
```

---

**基本写法：从拆分分支推送**
`git push <仓库URL> <本地分支>:<远程分支>`
```bash
# 推送拆分分支到远程
git push https://github.com/org/utils.git utils-sync:main
```

---

## 拆分历史

**基本写法：拆分子树为新分支**
`git subtree split --prefix=<路径> --branch <分支名>`
```bash
# 将 src 目录历史拆分到新分支
git subtree split --prefix=src --branch src-history
```

---

**基本写法：拆分到指定提交**
`git subtree split --prefix=<路径> --branch <分支> <提交>`
```bash
# 从指定提交开始拆分
git subtree split --prefix=src --branch src-history v1.0.0
```

---

**基本写法：拆分时重新生成历史**
`git subtree split --prefix=<路径> --rejoin`
```bash
# 拆分后标记主分支已同步
git subtree split --prefix=src --rejoin
```

---

## 合并策略

**基本写法：使用 subtree 合并策略**
`git merge -X subtree=<路径> <分支>`
```bash
# 用 subtree 策略合并子分支
git merge -X subtree=lib/utils utils-branch
```

---

**基本写法：以 ours 优先合并**
`git merge -X subtree=<路径> -X ours <分支>`
```bash
# 冲突时优先保留主仓库内容
git merge -X subtree=lib/utils -X ours utils-branch
```

---

## 初始化配置

**基本写法：为子树添加远程别名**
`git remote add <别名> <仓库URL>`
```bash
# 为子树来源仓库添加远程别名
git remote add utils https://github.com/org/utils.git
```

---

**基本写法：使用别名进行拉取**
`git subtree pull --prefix=<路径> <别名> <分支>`
```bash
# 通过别名简化拉取命令
git subtree pull --prefix=lib/utils utils main
```

---

**基本写法：使用别名进行推送**
`git subtree push --prefix=<路径> <别名> <分支>`
```bash
# 通过别名推送变更
git subtree push --prefix=lib/utils utils feature
```

---

## 与 submodule 对比

**基本写法：subtree 内容直接存放于主仓库**
`git subtree add --prefix=<路径> <URL> <分支>`
```bash
# 子目录文件直接属于主仓库历史
git subtree add --prefix=lib/utils https://github.com/org/utils.git main
```

---

**基本写法：submodule 仅存引用**
`git submodule add <URL> <路径>`
```bash
# submodule 仅记录子仓库引用（对比场景）
git submodule add https://github.com/org/utils.git lib/utils
```

---

## 常用查询

**基本写法：查看子树目录内容**
`git log --oneline --graph -- <路径>`
```bash
# 查看子树目录的所有提交
git log --oneline --graph -- lib/utils
```

---

**基本写法：查看子树来源**
`git remote -v`
```bash
# 查看配置的远程仓库别名
git remote -v
```

---

## 提交子树变更

**基本写法：在子树目录修改后提交**
`git commit -am "<消息>"`
```bash
# 修改 lib/utils 后直接在主仓库提交
git commit -am "update utils library"
```

---

**基本写法：仅提交子树目录**
`git commit -- <路径> -m "<消息>"`
```bash
# 仅提交子树目录变更
git commit -- lib/utils -m "feat: update utils"
```
