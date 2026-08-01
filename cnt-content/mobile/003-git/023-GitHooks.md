# Git hooks 钩子实战

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 钩子基础

**基本写法：查看可用钩子模板**
`ls .git/hooks`
```bash
# 列出当前仓库的钩子目录
ls .git/hooks
```

---

**基本写法：启用钩子**
`mv .git/hooks/<钩子名>.sample .git/hooks/<钩子名>`
```bash
# 移除 sample 后缀以激活钩子
mv .git/hooks/pre-commit.sample .git/hooks/pre-commit
```

---

**基本写法：使钩子可执行**
`chmod +x .git/hooks/<钩子名>`
```bash
# 赋予钩子脚本执行权限
chmod +x .git/hooks/pre-commit
```

---

**基本写法：查看全局钩子模板路径**
`git config --global core.hooksPath <路径>`
```bash
# 设置全局钩子目录
git config --global core.hooksPath ~/.git-hooks
```

---

**基本写法：本地仓库指定钩子路径**
`git config core.hooksPath <路径>`
```bash
# 为当前仓库指定自定义钩子目录
git config core.hooksPath .githooks
```

---

## 客户端钩子

**基本写法：pre-commit 钩子**
`.git/hooks/pre-commit`
```bash
# 在 git commit 前执行检查
#!/bin/sh
npm run lint
```

---

**基本写法：prepare-commit-msg 钩子**
`.git/hooks/prepare-commit-msg`
```bash
# 在编辑提交信息前自动填充
#!/bin/sh
echo "# 请按规范填写提交信息" >> "$1"
```

---

**基本写法：commit-msg 钩子**
`.git/hooks/commit-msg`
```bash
# 校验提交信息是否符合规范
#!/bin/sh
grep -qE "^(feat|fix|docs):" "$1" || exit 1
```

---

**基本写法：post-commit 钩子**
`.git/hooks/post-commit`
```bash
# 提交完成后通知
#!/bin/sh
echo "提交完成: $(git rev-parse HEAD)"
```

---

**基本写法：pre-push 钩子**
`.git/hooks/pre-push`
```bash
# 推送前执行测试
#!/bin/sh
npm test || exit 1
```

---

**基本写法：pre-rebase 钩子**
`.git/hooks/pre-rebase`
```bash
# 变基前检查
#!/bin/sh
echo "即将执行 rebase 操作" >&2
```

---

**基本写法：post-merge 钩子**
`.git/hooks/post-merge`
```bash
# 合并完成后安装依赖
#!/bin/sh
npm install
```

---

**基本写法：post-checkout 钩子**
`.git/hooks/post-checkout`
```bash
# 切换分支后切换依赖版本
#!/bin/sh
nvm use
```

---

## 服务端钩子

**基本写法：pre-receive 钩子**
`.git/hooks/pre-receive`
```bash
# 接收推送前校验所有引用
#!/bin/sh
while read oldrev newrev refname; do
  echo "推送引用: $refname"
done
```

---

**基本写法：update 针对单引用钩子**
`.git/hooks/update`
```bash
# 每个引用更新前调用
#!/bin/sh
refname="$1"
oldrev="$2"
newrev="$3"
```

---

**基本写法：post-receive 钩子**
`.git/hooks/post-receive`
```bash
# 接收推送后触发部署
#!/bin/sh
git --work-tree=/var/www --git-dir=/repo checkout -f
```

---

## 钩子脚本常用变量

**基本写法：在 pre-commit 中获取暂存文件**
`git diff --cached --name-only --diff-filter=ACM`
```bash
# 获取已暂存的修改文件列表
files=$(git diff --cached --name-only --diff-filter=ACM)
```

---

**基本写法：在 commit-msg 中读取提交信息**
`cat "$1"`
```bash
# 读取提交信息文件内容
msg=$(cat "$1")
```

---

**基本写法：在 pre-push 中读取推送信息**
`read <本地引用> <本地哈希> <远程引用> <远程哈希>`
```bash
# 从 stdin 读取推送引用信息
while read local_ref local_oid remote_ref remote_oid; do
  echo "$local_ref -> $remote_ref"
done
```

---

## Husky 等工具管理钩子

**基本写法：安装 Husky**
`npx husky init`
```bash
# 初始化 Husky 钩子管理
npx husky init
```

---

**基本写法：添加 Husky 钩子**
`npx husky add .husky/<钩子名> "<命令>"`
```bash
# 添加 pre-commit 钩子执行 lint
npx husky add .husky/pre-commit "npm run lint"
```

---

**基本写法：跳过钩子执行**
`git commit --no-verify`
```bash
# 提交时跳过 pre-commit 与 commit-msg 钩子
git commit --no-verify -m "msg"
```

---

**基本写法：推送时跳过钩子**
`git push --no-verify`
```bash
# 推送时跳过 pre-push 钩子
git push --no-verify
```

---

## 钩子实战示例

**基本写法：阻止提交到 main 分支**
`.git/hooks/pre-commit`
```bash
# 阻止直接在 main 分支提交
#!/bin/sh
branch=$(git rev-parse --abbrev-ref HEAD)
[ "$branch" = "main" ] && echo "禁止直接提交到 main" && exit 1
```

---

**基本写法：检查提交信息格式**
`.git/hooks/commit-msg`
```bash
# 校验 Conventional Commits 格式
#!/bin/sh
if ! grep -qE "^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+" "$1"; then
  echo "提交信息不符合规范"
  exit 1
fi
```

---

**基本写法：阻止提交大文件**
`.git/hooks/pre-commit`
```bash
# 阻止提交超过 5MB 的文件
#!/bin/sh
max_size=5242880
for file in $(git diff --cached --name-only); do
  size=$(git cat-file -s :"$file" 2>/dev/null || echo 0)
  [ "$size" -gt "$max_size" ] && echo "文件过大: $file" && exit 1
done
```

---

**基本写法：自动格式化代码**
`.git/hooks/pre-commit`
```bash
# 暂存前自动格式化
#!/bin/sh
files=$(git diff --cached --name-only --diff-filter=ACM | grep "\.js$")
echo "$files" | xargs -r prettier --write
echo "$files" | xargs -r git add
```

---

**基本写法：同步子模块**
`.git/hooks/post-checkout`
```bash
# 切换分支后同步子模块
#!/bin/sh
git submodule update --init --recursive
```

---

## 团队共享钩子

**基本写法：将钩子纳入版本控制**
`git config core.hooksPath .githooks`
```bash
# 设置仓库共享钩子目录
git config core.hooksPath .githooks
```

---

**基本写法：首次克隆后启用钩子**
`chmod +x .githooks/*`
```bash
# 克隆后赋予钩子可执行权限
chmod +x .githooks/*
```

---

**基本写法：在 README 中提示**
`cat README.md`
```bash
# 文档中说明启用共享钩子的步骤
# 执行: git config core.hooksPath .githooks && chmod +x .githooks/*
```

---

## 调试与排错

**基本写法：手动测试钩子**
`sh .git/hooks/pre-commit`
```bash
# 直接执行钩子脚本测试
sh .git/hooks/pre-commit
```

---

**基本写法：输出调试信息**
`echo "<消息>" >&2`
```bash
# 在钩子中输出到标准错误
echo "调试: 当前分支 $(git branch --show-current)" >&2
```

---

**基本写法：临时禁用所有钩子**
`git -c core.hooksPath=/dev/null <命令>`
```bash
# 单次命令跳过所有钩子
git -c core.hooksPath=/dev/null commit -m "msg"
```
