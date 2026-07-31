# GitHub 远程仓库管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 查看远程仓库

**基本写法：查看远程仓库名称**
`git remote`
```bash
# 列出所有已配置的远程仓库名
git remote
```

---

**基本写法：查看远程仓库详情**
`git remote -v`
```bash
# 列出远程仓库名及其 URL
git remote -v
```

---

**基本写法：查看指定远程详情**
`git remote show origin`
```bash
# 显示 origin 远程仓库的详细信息
git remote show origin
```

---

**基本写法：查看远程分支**
`git remote show origin`
```bash
# 查看 origin 的所有分支信息
git remote show origin
```

---

## 添加远程仓库

**基本写法：添加远程仓库**
`git remote add origin <仓库URL>`
```bash
# 添加名为 origin 的远程仓库
git remote add origin https://github.com/user/repo.git
```

---

**基本写法：添加 SSH 远程**
`git remote add origin git@github.com:<用户>/<仓库>.git`
```bash
# 通过 SSH 协议添加远程仓库
git remote add origin git@github.com:user/repo.git
```

---

**基本写法：添加多个远程**
`git remote add <名称> <URL>`
```bash
# 添加 upstream 远程仓库（用于 fork 项目）
git remote add upstream https://github.com/original/repo.git
```

---

**基本写法：添加自定义名称远程**
`git remote add <名称> <URL>`
```bash
# 添加自定义名称的远程仓库
git remote add backup https://github.com/user/backup.git
```

---

## 修改远程仓库

**基本写法：修改远程 URL**
`git remote set-url origin <新URL>`
```bash
# 修改 origin 的 URL 地址
git remote set-url origin https://github.com/user/new-repo.git
```

---

**基本写法：切换为 SSH 协议**
`git remote set-url origin git@github.com:<用户>/<仓库>.git`
```bash
# 从 HTTPS 切换为 SSH 协议
git remote set-url origin git@github.com:user/repo.git
```

---

**基本写法：切换为 HTTPS 协议**
`git remote set-url origin https://github.com/<用户>/<仓库>.git`
```bash
# 从 SSH 切换为 HTTPS 协议
git remote set-url origin https://github.com/user/repo.git
```

---

**基本写法：重命名远程仓库**
`git remote rename <旧名> <新名>`
```bash
# 重命名远程仓库名称
git remote rename origin upstream
```

---

## 删除远程仓库

**基本写法：删除远程仓库**
`git remote remove <名称>`
```bash
# 移除指定的远程仓库关联
git remote remove origin
```

---

**基本写法：删除远程仓库（rm 简写）**
`git remote rm <名称>`
```bash
# remove 的简写形式
git remote rm origin
```

---

**基本写法：删除后重新添加**
`git remote remove origin && git remote add origin <新URL>`
```bash
# 移除旧关联并添加新远程
git remote remove origin && git remote add origin https://github.com/user/new.git
```

---

## 远程分支管理

**基本写法：查看远程分支列表**
`git branch -r`
```bash
# 列出所有远程分支
git branch -r
```

---

**基本写法：清理无效远程分支**
`git remote prune origin`
```bash
# 清理本地中已不存在的远程分支引用
git remote prune origin
```

---

**基本写法：拉取时自动清理**
`git fetch --prune`
```bash
# 拉取远程更新同时清理无效分支
git fetch --prune
```

---

**基本写法：查看需要清理的分支**
`git remote prune origin --dry-run`
```bash
# 预览将被清理的分支（不实际执行）
git remote prune origin --dry-run
```

---

## Fork 工作流

**基本写法：克隆自己的 fork**
`git clone <自己的fork仓库URL>`
```bash
# 克隆自己 fork 的仓库
git clone https://github.com/yourname/repo.git
```

---

**基本写法：添加上游仓库**
`git remote add upstream <原仓库URL>`
```bash
# 添加原仓库作为 upstream
git remote add upstream https://github.com/original/repo.git
```

---

**基本写法：从上游同步**
`git fetch upstream`
```bash
# 获取上游仓库的更新
git fetch upstream
```

---

**基本写法：合并上游主分支**
`git merge upstream/main`
```bash
# 将上游 main 分支合并到本地
git merge upstream/main
```

---

**基本写法：推送同步到自己的 fork**
`git push origin main`
```bash
# 将同步后的代码推送到自己的 fork
git push origin main
```

---

## 凭证管理

**基本写法：缓存凭证（内存）**
`git config --global credential.helper cache`
```bash
# 临时缓存 Git 凭证避免重复输入
git config --global credential.helper cache
```

---

**基本写法：设置缓存时间**
`git config --global credential.helper 'cache --timeout=3600'`
```bash
# 缓存凭证 1 小时
git config --global credential.helper 'cache --timeout=3600'
```

---

**基本写法：永久存储凭证**
`git config --global credential.helper store`
```bash
# 永久存储凭证到磁盘（明文）
git config --global credential.helper store
```

---

**基本写法：Windows 凭证管理器**
`git config --global credential.helper manager`
```bash
# 使用 Windows 凭证管理器存储
git config --global credential.helper manager
```

---

**基本写法：macOS 钥匙串**
`git config --global credential.helper osxkeychain`
```bash
# 使用 macOS 钥匙串存储凭证
git config --global credential.helper osxkeychain
```
