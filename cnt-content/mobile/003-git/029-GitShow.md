# git show 查看命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 查看提交内容

**基本用法:查看某次提交**
`git show <提交>`

```bash
# 查看最新提交的详情
git show

# 查看指定提交
git show a1b2c3d

# 查看指定提交的元信息与统计
git show --stat HEAD
```

---

**基本用法:查看提交的文件差异**
`git show <提交> -- <路径>`

```bash
# 仅查看该提交中某个文件的改动
git show a1b2c3d -- src/main.py

# 查看合并提交的差异
git show -m a1b2c3d
```

---

## 查看特定对象

**基本用法:查看 blob 内容**
`git show <对象>`

```bash
# 查看某次提交中某文件的完整内容
git show HEAD:src/config.js

# 查看某分支某文件
git show feature:package.json

# 查看特定标签指向的提交
git show v1.0.0
```

---

## 格式化输出

**基本用法:自定义格式**
`git show --pretty=format:"<格式>"`

```bash
# 自定义提交信息格式
git show --pretty=format:"%H%n%an%n%s" HEAD

# 仅显示提交说明
git show --no-patch --format="%s"
```

---

**基本用法:差异输出格式**
`git show --<格式>`

```bash
# 仅显示文件名
git show --name-only HEAD

# word-level 差异
git show --word-diff HEAD

# 统计模式
git show --stat --oneline HEAD
```

---