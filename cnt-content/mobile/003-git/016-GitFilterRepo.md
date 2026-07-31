# Git filter-repo 与历史改写

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 准备工作

**基本写法：安装 git-filter-repo**
`pip install git-filter-repo`
```bash
# 通过 pip 安装官方推荐工具
pip install git-filter-repo
```

---

**基本写法：克隆待改写仓库**
`git clone --mirror <仓库URL> <目录>`
```bash
# 镜像克隆保留所有引用
git clone --mirror https://github.com/org/repo.git repo.git
```

---

**基本写法：创建备份分支**
`git branch backup-main main`
```bash
# 改写前备份当前分支
git branch backup-main main
```

---

## filter-repo 基本用法

**基本写法：分析仓库历史**
`git filter-repo --analyze`
```bash
# 生成历史分析报告到 .git/filter-repo
git filter-repo --analyze
```

---

**基本写法：移除某文件历史**
`git filter-repo --path <路径> --invert-paths`
```bash
# 从所有历史中移除 secrets.env
git filter-repo --path secrets.env --invert-paths
```

---

**基本写法：保留某路径并移除其他**
`git filter-repo --path <路径>`
```bash
# 只保留 src 目录历史
git filter-repo --path src/
```

---

**基本写法：移除整个目录**
`git filter-repo --path <目录>/ --invert-paths`
```bash
# 移除 vendor 目录的所有历史
git filter-repo --path vendor/ --invert-paths
```

---

## 改写作者信息

**基本写法：替换作者邮箱**
`git filter-repo --mailmap <mailmap文件>`
```bash
# 用 mailmap 文件统一作者信息
git filter-repo --mailmap mailmap.txt
```

---

**基本写法：直接替换提交者**
`git filter-repo --commit-callback '<脚本>'`
```bash
# 用回调函数批量改写提交者
git filter-repo --commit-callback 'commit.author_email = b"new@example.com"'
```

---

**基本写法：mailmap 文件格式**
`<新姓名> <新邮箱> <旧邮箱>`
```bash
# 在 mailmap.txt 中映射旧邮箱到新身份
Alice Lee <alice@example.com> <old@domain.com>
```

---

## 移除敏感信息

**基本写法：移除包含密码的文件**
`git filter-repo --path <文件> --invert-paths`
```bash
# 从历史中彻底删除配置文件
git filter-repo --path config/passwords.yml --invert-paths
```

---

**基本写法：按内容替换文本**
`git filter-repo --replace-text <替换文件>`
```bash
# 用替换规则批量清除敏感字符串
git filter-repo --replace-text replacements.txt
```

---

**基本写法：替换文件格式**
`<旧字符串>==><新字符串>`
```bash
# 在 replacements.txt 中定义替换规则
SECRET_KEY==>REDACTED
```

---

**基本写法：正则替换**
`regex:<正则>==><替换>`
```bash
# 用正则匹配并替换
regex:\b\d{16}\b==>****-****-****-****
```

---

## 重命名与移动

**基本写法：重命名目录**
`git filter-repo --path-rename <旧路径>:<新路径>`
```bash
# 将 src 重命名为 lib/src
git filter-repo --path-rename src/:lib/src/
```

---

**基本写法：合并多目录**
`git filter-repo --path-rename <旧1>:<新> --path-rename <旧2>:<新>`
```bash
# 合并两个目录到同一位置
git filter-repo --path-rename old-a/:src/ --path-rename old-b/:src/
```

---

## 分支与标签处理

**基本写法：仅改写指定分支**
`git filter-repo --refs <分支>`
```bash
# 仅改写 main 分支历史
git filter-repo --refs main
```

---

**基本写法：保留所有标签**
`git filter-repo --tags`
```bash
# 改写时同时更新所有标签
git filter-repo --tags
```

---

**基本写法：删除某标签**
`git filter-repo --refs <分支> --invert-paths --path <文件>`
```bash
# 删除 main 中某文件并保留其他引用
git filter-repo --refs main --invert-paths --path secret.env
```

---

## 提交信息改写

**基本写法：修改提交信息**
`git filter-repo --message-callback '<脚本>'`
```bash
# 用回调函数改写提交信息
git filter-repo --message-callback b"feat: " + message if message.startswith(b"add") else message'
```

---

**基本写法：移除特定关键字**
`git filter-repo --replace-message <替换文件>`
```bash
# 替换提交信息中的敏感词
git filter-repo --replace-message replacements.txt
```

---

## 推送与协作

**基本写法：强制推送改写后的历史**
`git push --force-with-lease origin <分支>`
```bash
# 安全地强制推送改写历史
git push --force-with-lease origin main
```

---

**基本写法：推送所有引用**
`git push --mirror origin`
```bash
# 推送所有分支与标签（镜像推送）
git push --mirror origin
```

---

**基本写法：通知协作者重新克隆**
`git push --force origin <分支>`
```bash
# 改写后强制推送，要求团队重新克隆
git push --force origin main
```

---

## filter-branch（不推荐但仍可用）

**基本写法：用 filter-branch 移除文件**
`git filter-branch --tree-filter 'rm -f <文件>' HEAD`
```bash
# 旧式逐提交删除文件（速度慢）
git filter-branch --tree-filter 'rm -f secrets.env' HEAD
```

---

**基本写法：改写作者**
`git filter-branch --env-filter '<脚本>' HEAD`
```bash
# 用环境过滤器改写作者信息
git filter-branch --env-filter 'export GIT_AUTHOR_EMAIL="new@example.com"' HEAD
```

---

**基本写法：清理 filter-branch 备份**
`git for-each-ref --format="%(refname)" refs/original/ | xargs -n 1 git update-ref -d`
```bash
# 删除 filter-branch 创建的备份引用
git for-each-ref --format="%(refname)" refs/original/ | xargs -n 1 git update-ref -d
```

---

## 验证与回收

**基本写法：验证改写结果**
`git log --all --pretty=format:"%H %an <%ae> %s"`
```bash
# 检查所有提交作者信息
git log --all --pretty=format:"%H %an <%ae> %s"
```

---

**基本写法：回收空间**
`git reflog expire --expire=now --all && git gc --prune=now`
```bash
# 清理悬空对象并立即回收
git reflog expire --expire=now --all && git gc --prune=now
```

---

**基本写法：检查悬空对象**
`git fsck --full --unreachable`
```bash
# 列出所有不可达对象
git fsck --full --unreachable
```
