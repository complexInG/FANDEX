# Git LFS 大文件存储

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 安装与初始化

**基本写法：安装 Git LFS**
`git lfs install`
```bash
# 在当前用户范围启用 Git LFS
git lfs install
```

---

**基本写法：在仓库中初始化 LFS**
`git lfs install --local`
```bash
# 仅在当前仓库启用 LFS
git lfs install --local
```

---

**基本写法：查看 LFS 版本**
`git lfs version`
```bash
# 输出当前 Git LFS 版本号
git lfs version
```

---

## 跟踪大文件

**基本写法：添加 LFS 跟踪规则**
`git lfs track "<模式>"`
```bash
# 跟踪所有 mp4 视频文件
git lfs track "*.mp4"
```

---

**基本写法：跟踪指定目录**
`git lfs track "<目录>/**"`
```bash
# 跟踪 assets 目录下所有文件
git lfs track "assets/**"
```

---

**基本写法：查看跟踪规则**
`git lfs track`
```bash
# 列出当前所有 LFS 跟踪规则
git lfs track
```

---

**基本写法：移除跟踪规则**
`git lfs untrack "<模式>"`
```bash
# 移除某类文件的 LFS 跟踪
git lfs untrack "*.mp4"
```

---

**基本写法：提交 .gitattributes**
`git add .gitattributes && git commit -m "<消息>"`
```bash
# 跟踪规则变更必须提交
git add .gitattributes && git commit -m "chore: configure LFS tracking"
```

---

## 操作 LFS 文件

**基本写法：添加大文件**
`git add <文件> && git commit -m "<消息>"`
```bash
# 添加大文件到 LFS 跟踪
git add video.mp4 && git commit -m "feat: add intro video"
```

---

**基本写法：查看 LFS 文件列表**
`git lfs ls-files`
```bash
# 列出仓库中所有 LFS 跟踪文件
git lfs ls-files
```

---

**基本写法：查看文件大小信息**
`git lfs ls-files --size`
```bash
# 显示 LFS 文件的实际大小
git lfs ls-files --size
```

---

## 拉取与推送

**基本写法：克隆含 LFS 的仓库**
`git clone <仓库URL>`
```bash
# 克隆时自动拉取 LFS 文件
git clone https://github.com/org/repo.git
```

---

**基本写法：跳过 LFS 内容克隆**
`GIT_LFS_SKIP_SMUDGE=1 git clone <仓库URL>`
```bash
# 仅克隆指针文件不下载大文件内容
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/org/repo.git
```

---

**基本写法：按需下载 LFS 文件**
`git lfs pull`
```bash
# 拉取所有 LFS 跟踪文件内容
git lfs pull
```

---

**基本写法：拉取指定文件**
`git lfs pull --include="<路径>"`
```bash
# 仅拉取指定目录下的 LFS 文件
git lfs pull --include="assets/videos/*"
```

---

**基本写法：推送 LFS 文件**
`git push origin <分支>`
```bash
# 推送时自动上传 LFS 文件
git push origin main
```

---

**基本写法：仅推送 LFS 内容**
`git lfs push origin <分支>`
```bash
# 单独推送 LFS 文件到远程
git lfs push origin main
```

---

**基本写法：推送所有 LFS 对象**
`git lfs push --all origin <分支>`
```bash
# 推送全部历史 LFS 对象
git lfs push --all origin main
```

---

## 检出与切换

**基本写法：检出指定分支的 LFS 文件**
`git lfs checkout`
```bash
# 用 LFS 内容替换工作区指针文件
git lfs checkout
```

---

**基本写法：仅检出指定路径**
`git lfs checkout --include="<路径>"`
```bash
# 仅检出 assets 目录的 LFS 内容
git lfs checkout --include="assets/*"
```

---

**基本写法：切换分支后同步**
`git checkout <分支> && git lfs checkout`
```bash
# 切换分支后重新检出 LFS 文件
git checkout feature && git lfs checkout
```

---

## 历史与迁移

**基本写法：将已有文件转为 LFS**
`git lfs migrate import --include="<模式>"`
```bash
# 将历史中的 mp4 文件迁移到 LFS
git lfs migrate import --include="*.mp4"
```

---

**基本写法：迁移指定分支历史**
`git lfs migrate import --include="<模式>" --include-ref=<分支>`
```bash
# 仅迁移 main 分支的历史文件
git lfs migrate import --include="*.mp4" --include-ref=main
```

---

**基本写法：迁移所有引用**
`git lfs migrate import --include="<模式>" --include-ref=refs/heads/*`
```bash
# 迁移所有分支的历史文件
git lfs migrate import --include="*.mp4" --include-ref=refs/heads/*
```

---

**基本写法：导出 LFS 文件回普通对象**
`git lfs migrate export --include="<模式>"`
```bash
# 取消 LFS 跟踪并还原文件
git lfs migrate export --include="*.mp4"
```

---

## 检查与状态

**基本写法：查看 LFS 状态**
`git lfs status`
```bash
# 显示工作区 LFS 文件状态
git lfs status
```

---

**基本写法：检查 LFS 文件完整性**
`git lfs fsck`
```bash
# 校验 LFS 对象完整性
git lfs fsck
```

---

**基本写法：查看 LFS 日志**
`git lfs logs last`
```bash
# 查看最近一次 LFS 操作日志
git lfs logs last
```

---

**基本写法：列出所有 LFS 对象**
`git lfs ls-files --all`
```bash
# 列出所有历史中的 LFS 文件
git lfs ls-files --all
```

---

## 远程配置

**基本写法：查看 LFS 端点**
`git config -l | grep lfs`
```bash
# 查看 LFS 相关配置
git config -l | grep lfs
```

---

**基本写法：指定 LFS 服务器**
`git config -f .lfsconfig lfs.url <URL>`
```bash
# 配置自定义 LFS 服务器地址
git config -f .lfsconfig lfs.url https://lfs.example.com/org/repo
```

---

**基本写法：跳过 smudge 过滤器**
`git config --local lfs.smudge false`
```bash
# 关闭自动下载 LFS 内容
git config --local lfs.smudge false
```

---

## 锁定文件（防冲突）

**基本写法：锁定 LFS 文件**
`git lfs lock <文件>`
```bash
# 锁定二进制文件防止并发编辑
git lfs lock assets/logo.psd
```

---

**基本写法：查看锁定列表**
`git lfs locks`
```bash
# 列出所有已锁定文件
git lfs locks
```

---

**基本写法：解锁文件**
`git lfs unlock <文件>`
```bash
# 释放文件锁
git lfs unlock assets/logo.psd
```

---

**基本写法：强制解锁**
`git lfs unlock <文件> --force`
```bash
# 强制解锁他人持有的锁
git lfs unlock assets/logo.psd --force
```

---

## 清理与优化

**基本写法：清理无用 LFS 对象**
`git lfs prune`
```bash
# 清理本地未引用的 LFS 对象
git lfs prune
```

---

**基本写法：查看待清理对象**
`git lfs prune --dry-run`
```bash
# 预览将被清理的对象
git lfs prune --dry-run
```

---

**基本写法：强制保留对象**
`git lfs fetch --recent`
```bash
# 拉取最近使用的 LFS 对象
git lfs fetch --recent
```
